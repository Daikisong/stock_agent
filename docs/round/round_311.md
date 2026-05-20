순서상 이번은 **R3 Loop 16 — 2차전지·전기차·친환경 trigger-level price validation 라운드**다.

이번 R3는 “배터리 좋다 / ESS 좋다 / 리튬 반등 좋다”로 묶으면 안 된다. 핵심은 **EV 수요 둔화, ESS 전환, LFP 계약, 리튬가격 반등, IRA/보조금 변화, JV 취소·공장 가동률, 유상증자·재무구조, 배터리 안전사고**를 각각 별도 trigger로 분리하는 것이다.

```text
round = R3 Loop 16
round_id = round_239
large_sector = SECONDARY_BATTERY_EV_GREEN
method = trigger_level_backtest_v1_after_redteam
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R4 Loop 16
```

이번에도 KRX/Naver/Yahoo/Stooq의 수정주가 일봉 OHLC 30D/90D/180D/1Y/2Y window는 안정적으로 직접 확보하지 못했다. 그래서 full MFE/MAE는 만들지 않고 `price_data_unavailable_after_deep_search`로 분리한다. 대신 Reuters/AP/WSJ/MarketWatch의 **reported event return, contract value, operating loss, plant layoff, cancellation value, policy/EV-demand shock, lithium-price event**를 trigger anchor로 사용한다. OHLC 미확보 때문에 Stage 후보 자체를 강등하지 않는다.

---

# 1. 이번 라운드 대섹터

```text
R3 = 2차전지·전기차·친환경
```

R3의 core gate는 아래다.

```text
EV battery:
OEM 계약 → GWh/기간 → 고객 모델/플랫폼 → 생산공장 → 가동률 → ASP/margin → IRA/보조금

ESS / LFP:
EV 라인 전환 → ESS 고객 계약 → LFP chemistry → delivery schedule → U.S. facility → margin

Battery materials:
리튬 가격 → cathode/anode ASP → inventory write-down → 고객사 pass-through → margin

JV / capex:
JV 설립·증설 → 보조금/대출 → 고객 수요 → ramp-up → utilization → impairment/cancellation

Safety / 4C:
배터리 화재 → 사망/품질결함 → 공장중단 → 고객 신뢰 → 보상/규제 → hard 4C

Policy:
IRA tax credit / EV subsidy expiry → OEM 생산계획 → 배터리 주문 취소 → 가동률 하락
```

---

# 2. 대상 canonical archetype

```text
ESS_LFP_LINE_CONVERSION_STAGE2_ACTIONABLE
EV_BATTERY_OEM_SUPPLY_STAGE2_WITH_UTILIZATION_GATE
EV_DEMAND_SLOWDOWN_4C_WATCH
BATTERY_JV_RESTRUCTURING_RELIEF_STAGE2_WITH_FINANCIAL_4B
LITHIUM_SUPPLY_SHOCK_CYCLICAL_STAGE2
BATTERY_MATERIAL_LITHIUM_BETA_EVENT_PREMIUM
BATTERY_FACTORY_SAFETY_HARD_4C
CAPITAL_RAISE_DILUTION_4B
```

---

# 3. deep sub-archetype

```text
Samsung SDI:
- U.S. unit signs 2T won / $1.36B LFP ESS deal
- shares +6.1% vs KOSPI -0.1%
- existing U.S. EV line conversion to ESS
- delivery starts 2027, three-year contract
- separate 2T won share issuance and pricing cut by 14%
- EV demand sluggish until H1 2026, Q4 2024 OP loss 257B won

LG Energy Solution:
- Rivian 67GWh / 4695 cylindrical cell contract
- Tesla LFP ESS $4.3B contract, stock +0.6%
- Ford cancels $6.5B / 9.6T won battery supply deal, LGES -7.6%, KOSPI -1.4%
- Q1 2026 operating loss 208B won; without IRA tax credit loss would be 398B won
- Ohio Ultium plant restart uncertain after about 850 layoffs/idling

SK Innovation / SK On:
- SK Innovation-SK E&S merger to support loss-making SK On
- shareholder approval, SK Innovation +5%, KOSPI -0.5%
- SK On cumulative operating losses 2.3T won, D/E 188% end-March 2024
- SK Battery America lays off 958 workers / 37% of workforce at Georgia plant
- Ford F-150 Lightning cancellation / EV strategy pivot

Battery materials:
- CATL Yichun lithium mine suspension
- lithium prices had fallen up to 90% from 2022 peak
- POSCO Future M +8.3%, L&F +10%, Samsung SDI +3.2%, LGES +2.8%
- event is lithium beta, not structural margin guarantee

Safety:
- Aricell lithium battery factory fire
- 23 deaths, 9 injuries
- majority-owned by S-Connect
- quality failures, rushed production, temporary/unskilled workers, emergency training failure
```

---

# 4. 선정 case 요약

| bucket                          | case                                          | 핵심 판정                                                                       |
| ------------------------------- | --------------------------------------------- | --------------------------------------------------------------------------- |
| Stage2-Actionable               | Samsung SDI / U.S. LFP ESS                    | 2T won / $1.36B ESS 계약, +6.1%, KOSPI -0.1%. EV 라인 전환이 실제 수주로 연결             |
| Stage2 with utilization gate    | LGES / Rivian·Tesla LFP                       | Rivian 67GWh, Tesla LFP ESS $4.3B. 계약은 좋지만 price muted / 가동률 gate           |
| 4C-watch                        | LGES / Ford cancellation·Ohio idling          | Ford $6.5B 계약 취소, LGES -7.6%, Ohio Ultium 재가동 불확실                           |
| Stage2 relief + 4B              | SK Innovation / SK E&S merger                 | SK On 재무구조 보강 목적, SK Innovation +5%, KOSPI -0.5%. 구조조정 relief               |
| 4C-watch                        | SK Battery America layoffs                    | Georgia plant 958명 / 37% layoff. Ford EV strategy shift가 공급망 타격             |
| cyclical Stage2 / event premium | CATL lithium mine suspension                  | POSCO Future M +8.3%, L&F +10%, Samsung SDI +3.2%, LGES +2.8%. lithium beta |
| 4B / dilution                   | Samsung SDI share-sale pricing cut            | 2T won 유상증자 가격 14% 인하, YTD -29.5%. capex funding but dilution               |
| hard 4C                         | Aricell battery fire / S-Connect read-through | 23명 사망, 품질결함·안전관리 실패. 배터리 안전 hard gate                                      |

---

# 5. Case별 trigger grid

## Case A — Samsung SDI / U.S. LFP ESS contract

```text
symbol = 006400
case_type = Stage2-Actionable
archetype = ESS_LFP_LINE_CONVERSION_STAGE2_ACTIONABLE
```

| trigger |                    type | date       | 당시 공개 evidence                                                                    | 가격 anchor                 | outcome           |
| ------- | ----------------------: | ---------- | --------------------------------------------------------------------------------- | ------------------------- | ----------------- |
| T0      |               awareness | 2025       | EV 수요 둔화, U.S. 보조금 변화, battery makers가 ESS로 라인 전환                                 | no price                  | Stage1            |
| T1      |         Stage2 evidence | 2025-12-10 | Samsung SDI America가 U.S. energy infrastructure customer와 LFP ESS battery 공급계약 체결 | shares +6.1%, KOSPI -0.1% | Stage2-Actionable |
| T2      |       Stage2 validation | 2025-12-10 | 계약규모 2T won 이상 / $1.36B, 2027년부터 3년간 공급, 기존 U.S. EV line을 ESS line으로 전환           | same                      | validation        |
| T3      | Stage3-Yellow candidate | N/A        | 고객명, margin, line conversion yield, repeat order 미확인                              | N/A                       | no Yellow         |
| T4      |                4B-watch | 2025~      | EV 수요 둔화로 ESS 전환은 좋지만 line retrofit risk 존재                                       | no OHLC                   | 4B                |
| T5      |            Stage3-Green | N/A        | full OHLC와 margin/가동률 확인 전 Green 보류                                               | N/A                       | no Green          |

Samsung SDI의 U.S. LFP ESS 계약은 이번 R3에서 가장 깨끗한 Stage2-Actionable이다. Samsung SDI America가 unnamed U.S. energy infrastructure customer와 2T won 이상, 약 $1.36B 규모의 LFP ESS battery 공급계약을 맺었고, 납품은 2027년부터 3년간 진행된다. 이 발표 후 Samsung SDI 주가는 장중 +6.1% 올랐고, KOSPI는 -0.1%였다. 회사는 기존 U.S. EV battery 생산라인 일부를 ESS용 LFP prismatic battery 생산으로 전환한다고 밝혔다. ([Reuters][1])

```json
{
  "case_id": "r3_loop16_samsung_sdi_lfp_ess",
  "symbol": "006400",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable",
  "trigger_date": "2025-12-10",
  "contract_value_krw_trn": 2.0,
  "contract_value_usd_bn": 1.36,
  "delivery_start_year": 2027,
  "contract_duration_years": 3,
  "battery_type": "LFP_prismatic_ESS",
  "line_conversion": "existing_U.S._EV_lines_to_ESS_lines",
  "event_return_pct": 6.1,
  "kospi_same_context_pct": -0.1,
  "market_relative_return_pp": 6.2,
  "stage3_gate_missing": [
    "customer_identity",
    "ESS_margin",
    "line_retrofit_yield",
    "repeat_order_visibility",
    "U.S._facility_utilization"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_stage2_actionable_ESS_conversion"
}
```

---

## Case B — LG Energy Solution / Rivian 67GWh and Tesla LFP ESS contracts

```text
symbol = 373220
case_type = Stage2 supply contract with utilization gate
archetype = EV_BATTERY_OEM_SUPPLY_STAGE2_WITH_UTILIZATION_GATE
```

| trigger |              type | date       | 당시 공개 evidence                                                           | 가격 anchor            | outcome             |
| ------- | ----------------: | ---------- | ------------------------------------------------------------------------ | -------------------- | ------------------- |
| T0      |   Stage2 evidence | 2024-11-07 | Rivian R2용 4695 cylindrical batteries 67GWh, 5년 이상 공급                    | no LGES price anchor | Stage2              |
| T1      |   Stage2 evidence | 2025-07-30 | Tesla LFP ESS battery contract $4.3B, 2027~2030, U.S. factories expected | LGES +0.6%           | Stage2, price muted |
| T2      | Stage2 validation | 2025       | LGES shifts focus from cooling EV market to ESS / LFP storage            | same                 | validation          |
| T3      |          4B-watch | 2025~      | 고객 비공개/ESS margin/line conversion/gigafactory utilization 미확인            | no OHLC              | 4B                  |
| T4      |     Stage3-Yellow | N/A        | actual utilization and margin unavailable                                | N/A                  | no Yellow           |

LGES의 Rivian trigger는 67GWh 규모의 확실한 supply contract다. LGES Arizona는 Rivian R2에 들어갈 4695 cylindrical batteries를 5년 이상 공급하며, 전체 공급량은 67GWh다. 이건 EV cylindrical cell Stage2 evidence다. ([Reuters][2])

다만 더 중요한 R3 calibration은 Tesla LFP ESS 계약의 “좋은 계약인데 price-muted” 구조다. LGES는 $4.3B 규모 LFP battery 공급계약을 체결했고, 공급기간은 2027년 8월부터 2030년 7월까지다. 보도상 고객은 Tesla로 확인됐고 U.S. factories에서 ESS용 LFP batteries를 생산할 것으로 알려졌다. 그런데 LGES 주가 반응은 +0.6%에 그쳤다. 즉 이 case는 Stage2지만 Green이 아니라 **utilization / ESS margin / customer schedule gate**가 남아 있다. ([월스트리트저널][3])

```json
{
  "case_id": "r3_loop16_lges_rivian_tesla_lfp",
  "symbol": "373220",
  "best_trigger": "T0/T1",
  "best_trigger_type": "Stage2_supply_contract_with_utilization_gate",
  "rivian_trigger_date": "2024-11-07",
  "rivian_contract_gwh": 67,
  "rivian_contract_duration_years": 5,
  "cell_type_rivian": "4695_cylindrical",
  "target_model": "Rivian_R2",
  "tesla_trigger_date": "2025-07-30",
  "tesla_lfp_contract_value_usd_bn": 4.3,
  "tesla_supply_period": "2027-08_to_2030-07",
  "tesla_contract_event_return_pct": 0.6,
  "stage3_gate_missing": [
    "ESS_line_utilization",
    "LFP_margin",
    "customer_take_or_pay_terms",
    "production_ramp_schedule",
    "IRA_credit_dependency"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_contract_price_muted"
}
```

---

## Case C — LG Energy Solution / Ford cancellation, Ohio Ultium uncertainty, Q1 loss

```text
symbol = 373220
case_type = 4C-watch / demand cancellation
archetype = EV_DEMAND_SLOWDOWN_4C_WATCH
```

| trigger |             type | date       | 당시 공개 evidence                                                                                 | 가격 anchor                   | outcome                  |
| ------- | ---------------: | ---------- | ---------------------------------------------------------------------------------------------- | --------------------------- | ------------------------ |
| T0      |         4C-watch | 2025-12-17 | Ford cancels EV battery supply deal worth 9.6T won / $6.5B                                     | no same-day price in source |                          |
| T1      | 4C price trigger | 2025-12-18 | LGES -7.6%, KOSPI -1.4% after cancellation                                                     | -7.6%                       | 4C-watch                 |
| T2      |       validation | 2026-04-30 | Q1 2026 OP loss 208B won; without IRA tax credit loss would be 398B won                        | no price                    | demand/profit validation |
| T3      |       validation | 2026-05-12 | GM-LG Ohio Ultium full restart date uncertain, around 850 workers laid off/idled since January | no LGES price               | utilization 4C           |
| T4      |           relief | N/A        | Q3 demand recovery or ESS conversion not confirmed                                             | N/A                         | no relief                |

LGES의 Ford cancellation은 R3에서 가장 직접적인 4C-watch다. Ford는 LGES와의 EV battery supply deal을 terminated 했고, 계약규모는 9.6T won, 약 $6.5B였다. 계약은 originally 2026~2027년부터 Ford Europe에 공급될 예정이었지만, Ford의 EV 모델 중단과 policy/demand 변화로 취소됐다. 다음 날 LGES 주가는 장중 -7.6% 하락했고 KOSPI는 -1.4%였다. ([Reuters][4])

이후 profit and utilization validation도 나왔다. LGES는 Q1 2026에 208B won operating loss를 기록했고, IRA tax credit이 없었다면 operating loss는 398B won이었다. GM-LG Ultium Ohio plant도 완전 재가동 일정이 불확실했고, January 이후 약 850 workers가 layoff/idled 상태였다. 이 case는 단순 “EV 수요 둔화”가 아니라 **계약취소 → 가동률 하락 → 보조금 의존 → 손실**로 이어지는 4C-watch다. ([Reuters][5])

```json
{
  "case_id": "r3_loop16_lges_ford_cancellation_ohio_loss",
  "symbol": "373220",
  "best_trigger": "T0/T3",
  "best_trigger_type": "4C_watch_demand_cancellation_utilization",
  "ford_cancellation_date": "2025-12-17",
  "cancelled_contract_value_krw_trn": 9.6,
  "cancelled_contract_value_usd_bn": 6.5,
  "stock_reaction_date": "2025-12-18",
  "event_mae_pct": -7.6,
  "kospi_same_context_pct": -1.4,
  "market_relative_return_pp": -6.2,
  "q1_2026_op_loss_krw_bn": 208,
  "q1_2026_loss_without_ira_credit_krw_bn": 398,
  "ultium_ohio_laid_off_or_idled_workers": 850,
  "restart_date_status": "uncertain",
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "demand_cancellation_4C_watch"
}
```

---

## Case D — SK Innovation / SK E&S merger to support SK On

```text
symbol = 096770
case_type = Stage2 relief with financial 4B
archetype = BATTERY_JV_RESTRUCTURING_RELIEF_STAGE2_WITH_FINANCIAL_4B
```

| trigger |               type | date       | 당시 공개 evidence                                                                             | 가격 anchor                      | outcome       |
| ------- | -----------------: | ---------- | ------------------------------------------------------------------------------------------ | ------------------------------ | ------------- |
| T0      |          awareness | 2024-07-17 | SK Innovation announces merger with SK E&S to improve profitability and support SK On      | no same-day price              |               |
| T1      |      Stage2 relief | 2024-08-27 | shareholders approve merger, merged asset company worth ~100T won                          | SK Innovation +5%, KOSPI -0.5% | Stage2 relief |
| T2      | 4B financial watch | 2024       | SK On never profitable since 2021 split, cumulative OP losses 2.3T won, D/E 188% end-March | same                           | 4B            |
| T3      |      Stage3-Yellow | N/A        | SK On profitability / utilization / debt improvement not confirmed                         | N/A                            | no Yellow     |

SK Innovation-SK E&S merger는 battery turnaround가 아니라 financial relief trigger다. SK Innovation은 loss-making battery unit SK On의 재무구조를 보강하기 위해 profitable LNG/city-gas affiliate SK E&S와 합병을 추진했고, merged company는 약 100T won asset company가 된다. SK On은 2021년 분사 이후 흑자를 낸 적이 없고, cumulative operating losses는 약 2.3T won, debt-to-equity ratio는 188%였다. ([Reuters][6])

주주승인일에는 SK Innovation 주가가 장중 +5% 올랐고, KOSPI는 -0.5%였다. 이건 Stage2 relief로는 좋지만, SK On의 cell shipment, utilization, margin, customer order가 확인되기 전에는 Yellow가 아니다. ([Reuters][7])

```json
{
  "case_id": "r3_loop16_sk_innovation_skes_merger_skon_relief",
  "symbol": "096770",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2_relief_with_financial_4B",
  "merger_announcement_date": "2024-07-17",
  "shareholder_approval_date": "2024-08-27",
  "merged_asset_company_krw_trn": 100,
  "event_return_pct": 5,
  "kospi_same_context_pct": -0.5,
  "market_relative_return_pp": 5.5,
  "sk_on_cumulative_op_losses_krw_trn": 2.3,
  "sk_on_debt_to_equity_pct": 188,
  "sk_es_2023_op_krw_trn": 1.3,
  "stage3_gate_missing": [
    "SK_On_profitability",
    "battery_shipment_recovery",
    "factory_utilization",
    "customer_order_visibility",
    "debt_ratio_improvement_after_merger"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_financial_relief_not_Green"
}
```

---

## Case E — SK Battery America layoffs / Ford EV strategy retreat

```text
symbol = 096770 read-through
case_type = 4C-watch / utilization and customer-demand shock
archetype = EV_DEMAND_SLOWDOWN_4C_WATCH
```

| trigger |       type | date       | 당시 공개 evidence                                                                                              | 가격 anchor              | outcome                    |
| ------- | ---------: | ---------- | ----------------------------------------------------------------------------------------------------------- | ---------------------- | -------------------------- |
| T0      |  awareness | 2025~2026  | U.S. EV credit expiry / automakers pivot to hybrids                                                         | no KRX price           |                            |
| T1      |   4C-watch | 2026-03-06 | SK Battery America lays off 958 workers, 37% workforce, at Georgia plant                                    | no SK Innovation price | 4C-watch                   |
| T2      | validation | 2026-03-06 | plant supplied Ford F-150 Lightning; Ford cancels fully electric version in favor of extended-range version | no price               | customer-demand validation |
| T3      |     relief | N/A        | new customers / ESS conversion not confirmed                                                                | N/A                    | no relief                  |

SK Battery America layoffs는 SK On/SK Innovation의 utilization 4C-watch다. AP는 SK Battery America가 Georgia Commerce plant에서 958명, 전체 workforce의 약 37%를 layoff 했다고 보도했다. 해당 plant는 Ford F-150 Lightning에 battery를 공급했지만, Ford는 fully electric version을 폐기하고 extended-range version으로 pivot했다. 이건 “EV 수요 둔화”라는 말보다 훨씬 구체적인 **고객 모델 취소 → 공장 가동률 리스크 → 인력 감축** trigger다. ([AP News][8])

```json
{
  "case_id": "r3_loop16_sk_battery_america_layoffs",
  "symbol": "096770_readthrough",
  "best_trigger": "T1/T2",
  "best_trigger_type": "4C_watch_utilization_customer_demand",
  "trigger_date": "2026-03-06",
  "laid_off_workers": 958,
  "workforce_cut_pct": 37,
  "remaining_workers": 1600,
  "plant_cost_usd_bn": 2.6,
  "customer_model": "Ford_F-150_Lightning",
  "ford_ev_strategy_change": "cancel_fully_electric_version_for_extended_range_version",
  "direct_krx_price_anchor": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "customer_demand_utilization_4C_watch"
}
```

---

## Case F — CATL Yichun mine suspension / Korean battery-material lithium beta

```text
symbols = 003670 / 066970 / 006400 / 373220
company_scope = POSCO Future M / L&F / Samsung SDI / LGES
case_type = cyclical Stage2 / event premium
archetype = LITHIUM_SUPPLY_SHOCK_CYCLICAL_STAGE2
```

| trigger |            type | date       | 당시 공개 evidence                                                                               | 가격 anchor                                                     | outcome        |
| ------- | --------------: | ---------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | -------------- |
| T0      |       awareness | 2024~2025  | lithium prices had fallen up to 90% from 2022 peak due oversupply                            | no price                                                      |                |
| T1      | Stage2 cyclical | 2025-08-11 | CATL suspends Yichun lithium mining project after license expiry                             | POSCO Future M +8.3%, L&F +10%, Samsung SDI +3.2%, LGES +2.8% | cyclical event |
| T2      |        4B-watch | 2025-08-11 | CATL says it can resume if license renewed and expects no material operational impact        | same                                                          | 4B             |
| T3      |   Stage3-Yellow | N/A        | sustained lithium price rebound, inventory write-down reversal, cathode margin not confirmed | N/A                                                           | no Yellow      |

CATL Yichun mine suspension은 R3 materials side에서 강한 cyclical Stage2 event다. CATL이 Jiangxi Yichun lithium mining project를 license expiry 때문에 중단하자 lithium supply 축소 기대가 생겼고, Korean battery-material names도 동반 상승했다. POSCO Future M은 +8.3%, L&F는 +10%, Samsung SDI는 +3.2%, LGES는 +2.8%였다. 다만 lithium prices는 2022 peak 이후 최대 90% 하락한 상태였고, CATL은 license renewal 시 생산을 재개할 수 있으며 material operational impact는 없다고 했다. 따라서 이건 structural Green이 아니라 **lithium beta / event premium**이다. ([월스트리트저널][9])

```json
{
  "case_id": "r3_loop16_catl_yichun_lithium_beta_korea_materials",
  "symbols": "003670/066970/006400/373220",
  "best_trigger": "T1/T2",
  "best_trigger_type": "cyclical_Stage2_with_4B_watch",
  "trigger_date": "2025-08-11",
  "catalyst": "CATL_Yichun_lithium_mine_license_expiry_suspension",
  "posco_future_m_event_return_pct": 8.3,
  "l_and_f_event_return_pct": 10,
  "samsung_sdi_event_return_pct": 3.2,
  "lges_event_return_pct": 2.8,
  "lithium_price_decline_from_2022_peak_pct": 90,
  "catl_material_impact_claim": "no_material_operational_impact",
  "license_renewal_risk": true,
  "stage3_gate_missing": [
    "sustained_lithium_price_rebound",
    "cathode_ASP_pass_through",
    "inventory_write_down_reversal",
    "material_margin_recovery",
    "customer_volume_recovery"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "cyclical_lithium_beta_event_premium"
}
```

---

## Case G — Samsung SDI capital raise / dilution and EV-demand 4B

```text
symbol = 006400
case_type = 4B / dilution and capex-funding risk
archetype = CAPITAL_RAISE_DILUTION_4B
```

| trigger |          type | date       | 당시 공개 evidence                                                              | 가격 anchor                    | outcome             |
| ------- | ------------: | ---------- | --------------------------------------------------------------------------- | ---------------------------- | ------------------- |
| T0      |     awareness | 2025-03    | Samsung SDI plans 2T won share issuance for GM JV and Hungary expansion     | no price                     |                     |
| T1      |   4B dilution | 2025-04-09 | share-sale price cut by 14% from 169,200 to 146,200 won after market tumble | Samsung SDI -1%, KOSPI -0.5% | 4B                  |
| T2      |    validation | 2025-04-09 | stock down 29.5% YTD; issuance size 11.821M new shares                      | same                         | dilution validation |
| T3      | Stage2 relief | N/A        | capex-funded capacity supports future but demand/margin not confirmed       | N/A                          | relief only         |

Samsung SDI의 capital raise는 EV battery capex funding이지만 4B를 붙여야 한다. Samsung SDI는 GM JV와 Hungary factory expansion 등을 위해 2T won 자금조달을 추진했고, 2025년 4월에는 신주 발행가를 169,200 won에서 146,200 won으로 14% 낮췄다. 보도 시점 주가는 -1%, KOSPI는 -0.5%였고, Samsung SDI 주가는 연초 대비 -29.5%였다. 이 case는 “capex = 성장”이 아니라 **dilution + demand uncertainty + funding risk**로 기록해야 한다. ([Reuters][10])

```json
{
  "case_id": "r3_loop16_samsung_sdi_share_sale_dilution",
  "symbol": "006400",
  "best_trigger": "T1/T2",
  "best_trigger_type": "4B_dilution_capex_funding",
  "trigger_date": "2025-04-09",
  "share_issuance_value_krw_trn": 2.0,
  "new_shares_count": 11821000,
  "original_offering_price_krw": 169200,
  "revised_offering_price_krw": 146200,
  "pricing_cut_pct": 14,
  "event_return_pct": -1,
  "kospi_same_context_pct": -0.5,
  "ytd_decline_pct": -29.5,
  "use_of_proceeds": [
    "GM_U.S._joint_venture",
    "Hungary_factory_expansion",
    "capacity_investment"
  ],
  "trigger_outcome_label": "capital_raise_dilution_4B"
}
```

---

## Case H — Aricell lithium battery factory fire / S-Connect read-through

```text
symbol = 096630 read-through
case_type = hard 4C safety
archetype = BATTERY_FACTORY_SAFETY_HARD_4C
```

| trigger |            type | date       | 당시 공개 evidence                                                                                             | 가격 anchor                   | outcome           |
| ------- | --------------: | ---------- | ---------------------------------------------------------------------------------------------------------- | --------------------------- | ----------------- |
| T0      |         hard 4C | 2024-06-24 | Aricell lithium battery factory fire, 23 deaths, 9 injuries                                                | S-Connect price unavailable | hard 4C           |
| T1      |      validation | 2024-08-23 | police blame quality failures and rushed production; Aricell majority owned by S-Connect                   | no price                    | safety validation |
| T2      | hard 4C details | 2024-08-23 | failed April quality inspection, temporary/unskilled workers, overheating defects, lack of escape training | no price                    | hard gate         |
| T3      |          relief | N/A        | remediation/insurance/contract recovery not confirmed                                                      | N/A                         | no relief         |

Aricell fire is the R3 hard safety gate. Reuters reported that the lithium battery maker Aricell, majority owned by S-Connect, suffered a fire that killed 23 people and injured nine. Police later said the fire happened after the company rushed production to meet a deadline despite dangerous quality-failure signals; it had failed an April quality inspection, used temporary and unskilled workers, saw defect rates including overheating rise, and did not take enough measures to contain safety risk. This is not a normal production issue. It is a hard 4C for battery manufacturing safety, quality and regulatory trust. ([Reuters][11])

```json
{
  "case_id": "r3_loop16_aricell_battery_factory_fire",
  "symbol": "096630_readthrough",
  "best_trigger": "T0/T2",
  "best_trigger_type": "hard_4C_safety_quality",
  "incident_date": "2024-06-24",
  "fatalities": 23,
  "injuries": 9,
  "company": "Aricell",
  "majority_owner": "S-Connect",
  "quality_failure_findings": [
    "failed_April_quality_inspection",
    "rushed_production_to_meet_deadline",
    "temporary_unskilled_workers",
    "overheating_defects",
    "lack_of_emergency_escape_training"
  ],
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "hard_4C_success_battery_safety"
}
```

---

# 6. Trigger별 가격경로 검증 요약

| case                       | best trigger | entry anchor |                                         event MFE/MAE |       market-relative | full MFE/MAE | outcome                     |
| -------------------------- | ------------ | -----------: | ----------------------------------------------------: | --------------------: | ------------ | --------------------------- |
| Samsung SDI LFP ESS        | T1/T2        |        event |                                                 +6.1% | +6.2pp vs KOSPI -0.1% | unavailable  | excellent Stage2-Actionable |
| LGES Rivian/Tesla          | T0/T1        |        event |                     Tesla deal +0.6%, Rivian no price |                 muted | unavailable  | Stage2, utilization gate    |
| LGES Ford cancellation     | T0/T3        |        event |                                                 -7.6% | -6.2pp vs KOSPI -1.4% | unavailable  | 4C-watch                    |
| SK Innovation merger       | T1/T2        |        event |                                                   +5% | +5.5pp vs KOSPI -0.5% | unavailable  | Stage2 relief + 4B          |
| SK Battery America layoffs | T1/T2        | no KRX price |                           958 layoffs / 37% workforce |                   N/A | unavailable  | utilization 4C              |
| CATL lithium beta          | T1/T2        |        event | POSCO Future M +8.3%, L&F +10%, SDI +3.2%, LGES +2.8% |           unavailable | unavailable  | cyclical Stage2             |
| Samsung SDI share sale     | T1/T2        |        event |                                    -1% vs KOSPI -0.5% |                -0.5pp | unavailable  | dilution 4B                 |
| Aricell fire               | T0/T2        | no KRX price |                                23 deaths / 9 injuries |                   N/A | unavailable  | hard 4C                     |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
LGES / Rivian·Tesla:
계약은 크지만 price reaction은 약하거나 unavailable. Utilization and margin gate.

SK Innovation / SK E&S:
재무구조 보강 relief는 있었지만 battery profitability는 아직 아님.

CATL lithium suspension:
materials basket 반응은 강했지만 lithium beta / cyclical event.
```

## Stage2-Actionable entry 성과

```text
Samsung SDI LFP ESS:
계약금액, 납품기간, U.S. line conversion, event return이 모두 닫힘.
이번 라운드의 가장 좋은 Stage2-Actionable.

CATL lithium beta:
POSCO Future M +8.3%, L&F +10%로 Actionable처럼 보이나,
license renewal과 lithium oversupply가 있어 cyclical event로 분리.
```

## Stage3-Yellow 후보

```text
Samsung SDI:
ESS LFP 계약의 margin, retrofit yield, repeat order가 확인되면 Yellow 후보.

LGES:
Tesla/Rivian 계약이 utilization improvement와 OP 회복으로 연결되면 Yellow 후보.

SK Innovation/SK On:
merger 이후 SK On의 가동률·손익·부채비율이 개선되면 Yellow 후보.

Battery materials:
lithium rebound가 cathode ASP/margin 회복으로 이어지면 Yellow 후보.
```

## Stage3-Green

```text
이번 R3 Loop 16에서 확정 Green 없음.

이유:
- EV cell makers는 contract는 있으나 utilization/margin이 아직 불안정하다.
- ESS 전환은 좋지만 line conversion yield와 customer repeat order가 필요하다.
- lithium beta는 structural margin이 아니라 cyclical event다.
- SK On은 restructuring relief 단계다.
- safety hard 4C가 battery manufacturing score를 제한한다.
```

---

# 8. score-price alignment 판정

```text
aligned:
- Samsung SDI LFP ESS
- LGES Ford cancellation
- SK Innovation shareholder approval relief
- CATL lithium beta

Stage2_promote_candidate:
- Samsung SDI LFP ESS
- LGES Rivian/Tesla LFP, but price muted
- SK Innovation/SK E&S merger, but relief not profit

Stage3-Yellow candidate:
- Samsung SDI ESS if margin/utilization confirms
- LGES if Tesla/Rivian contracts convert to utilization and OP recovery
- SK Innovation if SK On profitability improves
- POSCO Future M/L&F if lithium rebound drives ASP/margin

evidence_good_but_price_failed_or_muted:
- LGES Tesla LFP, +0.6% only
- LGES Rivian, no price anchor
- Samsung SDI share issuance, capex reason but dilution pressure

cyclical_success:
- CATL lithium mine suspension / Korean materials rally

event_premium:
- POSCO Future M / L&F lithium beta
- Samsung SDI LFP ESS if ESS margin not confirmed

thesis_break_watch:
- LGES Ford cancellation
- LGES Ohio Ultium idling
- SK Battery America layoffs
- Samsung SDI EV demand slump and capital raise

hard_4C_success:
- Aricell lithium battery factory fire
```

---

# 9. 점수비중 교정

## 올릴 축

```csv
axis,delta,reason,cases
ESS_LFP_contract_visibility,+5,"EV 둔화 속 ESS 전환이 실제 수주로 닫히면 Stage2-Actionable","Samsung SDI"
U.S._line_conversion_utilization,+5,"U.S. EV line을 ESS로 전환해 가동률을 방어하는지 중요","Samsung SDI, LGES"
OEM_contract_cancellation_risk,+5,"대형 OEM 계약취소는 즉시 4C-watch","LGES/Ford"
IRA_tax_credit_dependency,+4,"보조금 없으면 손실폭이 커지는 구조는 hard overlay","LGES"
battery_JV_financial_structure,+4,"loss-making SK On 보강은 relief지만 profit gate 필요","SK Innovation"
lithium_price_beta_duration,+4,"리튬 반등이 지속되어 ASP/margin으로 이어지는지 확인","POSCO Future M, L&F"
battery_factory_safety_trust,+5,"화재·품질·사망사고는 hard 4C","Aricell/S-Connect"
```

## 내릴 축

```csv
axis,delta,reason,cases
EV_growth_headline_without_utilization,-5,"계약/증설 headline만으로 Green 금지","LGES, Samsung SDI"
large_GWh_contract_without_margin,-4,"GWh 계약은 margin/가동률 확인 전 Stage2","LGES Rivian"
ESS_pivot_without_line_yield,-4,"ESS 전환은 retrofit yield 확인 전 4B","Samsung SDI"
lithium_price_spike_without_margin,-5,"리튬 beta는 cathode margin 확인 전 cyclical","CATL/POSCO Future M/L&F"
restructuring_relief_without_profit,-5,"합병/재무보강은 profit이 아니다","SK Innovation/SK On"
capex_funding_with_dilution,-4,"유상증자는 capex positive와 dilution negative를 병기","Samsung SDI"
```

---

# 10. Stage2-Actionable 승격 조건

R3 Loop 16 shadow rule:

```text
R3에서 Stage2 evidence가 아래 중 3개 이상이면 Stage2-Actionable로 승격한다.

1. 계약금액 또는 GWh 규모가 명확하다.
2. 납품기간과 생산공장이 명확하다.
3. event return이 +5% 이상이다.
4. market-relative return이 +5pp 이상이다.
5. EV line → ESS line 전환처럼 utilization 방어 논리가 있다.
6. 고객 수요가 model/platform 또는 ESS infrastructure use-case로 연결된다.
7. dilution, cancellation, safety, subsidy 4C overlay가 없다.
```

적용:

```text
Samsung SDI LFP ESS:
조건 1,2,3,4,5,6 충족 → Stage2-Actionable.

LGES Rivian/Tesla:
계약규모는 좋지만 price muted / utilization gate → Stage2, Actionable 보류.

SK Innovation merger:
price reaction은 좋지만 profit이 아니라 relief → Stage2 relief.

CATL lithium beta:
price reaction은 좋지만 company margin evidence 없음 → cyclical Stage2.
```

---

# 11. Stage3-Yellow 조건

```text
Stage3-Yellow:
- Stage2-Actionable 이후 EPS/OP/FCF 경로가 바뀔 가능성이 높아진 상태.
- 하지만 utilization, line conversion, margin, subsidy, safety 중 하나가 남은 상태.
```

Yellow 후보:

```text
Samsung SDI:
ESS LFP 계약이 line utilization and margin으로 확인되면 Yellow.

LGES:
Rivian/Tesla contracts가 Ford cancellation을 상쇄하고 OP 회복으로 이어지면 Yellow.

SK Innovation:
SK On 손익분기점과 부채비율 개선이 확인되면 Yellow.

POSCO Future M / L&F:
lithium rebound가 cathode ASP and margin으로 확인되면 Yellow.
```

---

# 12. Stage3-Green 조건

```text
Stage3-Green:
- GWh contract가 utilization and margin으로 연결됨
- ESS line conversion yield가 안정적임
- IRA/보조금 없어도 손익이 유지됨
- OEM cancellation risk가 낮음
- lithium price rebound가 inventory write-down reversal and ASP margin으로 연결됨
- safety/quality hard gate가 없음
- full-window MFE/MAE가 우호적임
```

이번 R3 Loop 16에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
reason = full OHLC unavailable + utilization/margin/subsidy/safety gates not fully closed
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- EV demand slowdown 속에서 capex funding을 성장으로만 해석
- ESS 전환 headline이 line yield/margin 없이 급등
- lithium price spike가 cathode margin으로 확인되기 전 과열
- restructuring merger를 profit turnaround로 오해
- GWh contract가 customer production plan 변경으로 취소될 수 있음
```

적용:

```text
Samsung SDI:
LFP ESS는 Stage2-Actionable, 하지만 line conversion yield and margin 전에는 4B-watch.

LGES:
Tesla/Rivian contracts are good, but Ford cancellation and Ohio idling require 4B/4C overlay.

SK Innovation:
SK E&S merger is relief, not profit. 4B financial overlay.

CATL lithium beta:
license renewal 가능성이 있어 event premium 4B.
```

---

# 14. 4C hard gate 조건

```text
R3 4C:
- OEM battery contract cancellation
- EV model cancellation causing plant idling
- subsidy expiry causing demand cliff
- factory fire / deaths / quality failures
- line utilization collapse
- capital raise under falling share price
- customer concentration loss
```

이번 R3 Loop 16 hard 4C:

```text
Aricell battery factory fire = hard_4C_success
```

Strong 4C-watch:

```text
- LGES Ford contract cancellation
- LGES Ohio Ultium plant idling
- SK Battery America layoffs
- Samsung SDI share-sale dilution
- Samsung SDI / LGES operating-loss and subsidy dependency
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

R3 production 설계 원칙:

```text
1. EV battery와 ESS battery를 같은 score로 보지 않는다.
2. GWh contract는 utilization/margin 전에는 Stage2다.
3. ESS line conversion은 좋은 trigger지만 retrofit yield가 gate다.
4. OEM cancellation은 hard 4C-watch다.
5. lithium price event는 material-company margin 확인 전 cyclical label이다.
6. safety/fire/death event는 hard 4C로 즉시 차감한다.
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_239.md 요약

```md
# R3 Loop 16. Secondary Battery / EV / Green Trigger-level Price Validation

이번 라운드는 R3 Loop 16 trigger-level validation 라운드다.

핵심 결론:
- Samsung SDI / U.S. LFP ESS is the cleanest Stage2-Actionable case. Samsung SDI America signed a contract worth more than 2T won / $1.36B to supply LFP batteries for ESS to a U.S. energy infrastructure customer, with deliveries from 2027 over three years. Shares rose 6.1% while KOSPI fell 0.1%. Green requires ESS margin, line-retrofit yield and repeat orders.
- LG Energy Solution / Rivian and Tesla is Stage2 with utilization gate. Rivian contract is 67GWh over five years for 4695 cylindrical cells. Tesla LFP ESS contract is $4.3B, but stock rose only 0.6%. Utilization and margin are not yet confirmed.
- LGES / Ford cancellation is 4C-watch. Ford cancelled a 9.6T won / $6.5B EV battery supply deal; LGES shares fell as much as 7.6% while KOSPI fell 1.4%. Q1 2026 OP loss was 208B won and would have been 398B won without IRA tax credit. Ohio Ultium restart remains uncertain after about 850 layoffs/idled workers.
- SK Innovation / SK E&S merger is Stage2 relief with financial 4B. Shareholder approval sent SK Innovation up 5% vs KOSPI -0.5%, but SK On had 2.3T won cumulative OP losses and 188% D/E. Profitability gate remains.
- SK Battery America layoffs are utilization 4C-watch. 958 workers / 37% of workforce laid off at Georgia plant after Ford’s EV strategy shifted away from F-150 Lightning.
- CATL Yichun lithium mine suspension is cyclical Stage2 / event premium. POSCO Future M +8.3%, L&F +10%, Samsung SDI +3.2%, LGES +2.8%. But lithium prices had fallen up to 90% from 2022 peak and CATL may resume if license renewed.
- Samsung SDI share-sale pricing cut is 4B. 2T won share issuance price cut by 14% amid falling stock and tariff/global slowdown fears.
- Aricell / S-Connect read-through is hard battery-safety 4C. Aricell fire killed 23 and injured nine; police cited quality failures, rushed production, temporary/unskilled workers and safety-training failures.

Main calibration:
- Raise ESS_LFP_contract_visibility, U.S._line_conversion_utilization, OEM_contract_cancellation_risk, IRA_tax_credit_dependency, battery_JV_financial_structure, lithium_price_beta_duration, battery_factory_safety_trust.
- Lower EV_growth_headline_without_utilization, large_GWh_contract_without_margin, ESS_pivot_without_line_yield, lithium_price_spike_without_margin, restructuring_relief_without_profit, capex_funding_with_dilution.
```

## docs/checkpoints/checkpoint_28a_round239_r3_loop16.md 요약

```md
# Checkpoint 28A Round 239 R3 Loop 16 Trigger-level Calibration

## 반영 내용
- R3 Loop 16 trigger-level validation을 수행했다.
- Samsung SDI LFP ESS, LGES Rivian/Tesla, LGES Ford cancellation/Ohio loss, SK Innovation-SK E&S merger, SK Battery America layoffs, CATL lithium beta, Samsung SDI share-sale, Aricell fire를 검토했다.
- full adjusted OHLC window는 확보하지 못했으므로 Reuters/AP/WSJ/MarketWatch의 reported event return과 event price anchor를 사용했다.
- OHLC 미확보를 이유로 Stage 후보를 강등하지 않고, price_data_unavailable_after_deep_search로 분리 기록했다.

## 핵심 보정
- EV battery와 ESS battery trigger를 분리한다.
- GWh contract는 utilization/margin 전에는 Stage2다.
- ESS line conversion은 좋은 trigger지만 retrofit yield and margin이 gate다.
- OEM contract cancellation and plant idling are 4C-watch.
- Lithium supply shock is cyclical Stage2 unless cathode ASP/margin improves.
- Battery fire and quality failure are hard 4C.
```

## data/e2r_case_library/cases_r3_loop16_round239.jsonl 초안

```jsonl
{"case_id":"r3_loop16_samsung_sdi_lfp_ess","symbol":"006400","company_name":"Samsung SDI","case_type":"Stage2_promote_candidate","primary_archetype":"ESS_LFP_LINE_CONVERSION_STAGE2_ACTIONABLE","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2025-12-10","contract_value_krw_trn":2.0,"contract_value_usd_bn":1.36,"delivery_start_year":2027,"contract_duration_years":3,"battery_type":"LFP_prismatic_ESS","line_conversion":"existing_U.S._EV_lines_to_ESS_lines","event_return_pct":6.1,"kospi_same_context_pct":-0.1,"market_relative_return_pp":6.2,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_actionable","notes":"ESS contract plus line conversion and strong relative price reaction. Margin and retrofit yield are gates."}
{"case_id":"r3_loop16_lges_rivian_tesla_lfp","symbol":"373220","company_name":"LG Energy Solution","case_type":"Stage2_supply_contract_with_utilization_gate","primary_archetype":"EV_BATTERY_OEM_SUPPLY_STAGE2_WITH_UTILIZATION_GATE","best_trigger":"T0/T1","stage_candidate":"Stage2","price_validation":{"rivian_trigger_date":"2024-11-07","rivian_contract_gwh":67,"rivian_contract_duration_years":5,"cell_type_rivian":"4695_cylindrical","target_model":"Rivian_R2","tesla_trigger_date":"2025-07-30","tesla_lfp_contract_value_usd_bn":4.3,"tesla_supply_period":"2027-08_to_2030-07","tesla_contract_event_return_pct":0.6,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_contract_price_muted","notes":"Large contracts are real, but price reaction was muted and utilization/margin are not yet confirmed."}
{"case_id":"r3_loop16_lges_ford_cancellation_ohio_loss","symbol":"373220","company_name":"LG Energy Solution","case_type":"4C_watch_demand_cancellation_utilization","primary_archetype":"EV_DEMAND_SLOWDOWN_4C_WATCH","best_trigger":"T0/T3","stage_candidate":"4C-watch","price_validation":{"ford_cancellation_date":"2025-12-17","cancelled_contract_value_krw_trn":9.6,"cancelled_contract_value_usd_bn":6.5,"stock_reaction_date":"2025-12-18","event_mae_pct":-7.6,"kospi_same_context_pct":-1.4,"market_relative_return_pp":-6.2,"q1_2026_op_loss_krw_bn":208,"q1_2026_loss_without_ira_credit_krw_bn":398,"ultium_ohio_laid_off_or_idled_workers":850,"restart_date_status":"uncertain","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","notes":"Contract cancellation, operating loss and plant idling are R3 4C-watch triggers."}
{"case_id":"r3_loop16_sk_innovation_skes_merger_skon_relief","symbol":"096770","company_name":"SK Innovation / SK On","case_type":"Stage2_relief_with_financial_4B","primary_archetype":"BATTERY_JV_RESTRUCTURING_RELIEF_STAGE2_WITH_FINANCIAL_4B","best_trigger":"T1/T2","stage_candidate":"Stage2_relief","price_validation":{"merger_announcement_date":"2024-07-17","shareholder_approval_date":"2024-08-27","merged_asset_company_krw_trn":100,"event_return_pct":5,"kospi_same_context_pct":-0.5,"market_relative_return_pp":5.5,"sk_on_cumulative_op_losses_krw_trn":2.3,"sk_on_debt_to_equity_pct":188,"sk_es_2023_op_krw_trn":1.3,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_financial_relief_not_Green","notes":"Merger supports SK On balance sheet, but battery profitability/utilization remain gates."}
{"case_id":"r3_loop16_sk_battery_america_layoffs","symbol":"096770_readthrough","company_name":"SK Battery America / SK On read-through","case_type":"4C_watch_utilization_customer_demand","primary_archetype":"EV_DEMAND_SLOWDOWN_4C_WATCH","best_trigger":"T1/T2","stage_candidate":"4C-watch","price_validation":{"trigger_date":"2026-03-06","laid_off_workers":958,"workforce_cut_pct":37,"remaining_workers":1600,"plant_cost_usd_bn":2.6,"customer_model":"Ford_F-150_Lightning","ford_ev_strategy_change":"cancel_fully_electric_version_for_extended_range_version","direct_krx_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","notes":"Customer EV model cancellation and plant layoffs are utilization 4C-watch."}
{"case_id":"r3_loop16_catl_yichun_lithium_beta_korea_materials","symbol":"003670/066970/006400/373220","company_name":"POSCO Future M / L&F / Samsung SDI / LGES","case_type":"cyclical_lithium_beta_event_premium","primary_archetype":"LITHIUM_SUPPLY_SHOCK_CYCLICAL_STAGE2","best_trigger":"T1/T2","stage_candidate":"cyclical_Stage2","price_validation":{"trigger_date":"2025-08-11","catalyst":"CATL_Yichun_lithium_mine_license_expiry_suspension","posco_future_m_event_return_pct":8.3,"l_and_f_event_return_pct":10,"samsung_sdi_event_return_pct":3.2,"lges_event_return_pct":2.8,"lithium_price_decline_from_2022_peak_pct":90,"catl_material_impact_claim":"no_material_operational_impact","license_renewal_risk":true,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"cyclical_success_event_premium","notes":"Lithium beta rally is Stage2 cyclical; cathode ASP/margin needed for Yellow."}
{"case_id":"r3_loop16_samsung_sdi_share_sale_dilution","symbol":"006400","company_name":"Samsung SDI","case_type":"4B_dilution_capex_funding","primary_archetype":"CAPITAL_RAISE_DILUTION_4B","best_trigger":"T1/T2","stage_candidate":"4B-watch","price_validation":{"trigger_date":"2025-04-09","share_issuance_value_krw_trn":2.0,"new_shares_count":11821000,"original_offering_price_krw":169200,"revised_offering_price_krw":146200,"pricing_cut_pct":14,"event_return_pct":-1,"kospi_same_context_pct":-0.5,"ytd_decline_pct":-29.5},"score_price_alignment":"capital_raise_dilution_4B","notes":"Capex funding is not automatically positive when dilution and demand weakness are present."}
{"case_id":"r3_loop16_aricell_battery_factory_fire","symbol":"096630_readthrough","company_name":"Aricell / S-Connect read-through","case_type":"hard_4C_safety_quality","primary_archetype":"BATTERY_FACTORY_SAFETY_HARD_4C","best_trigger":"T0/T2","stage_candidate":"4C","price_validation":{"incident_date":"2024-06-24","fatalities":23,"injuries":9,"company":"Aricell","majority_owner":"S-Connect","quality_failure_findings":["failed_April_quality_inspection","rushed_production_to_meet_deadline","temporary_unskilled_workers","overheating_defects","lack_of_emergency_escape_training"],"direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"hard_4c_success","notes":"Battery factory fire and quality failure are hard safety 4C triggers."}
```

## data/e2r_trigger_calibration/triggers_r3_loop16_round239.jsonl 초안

```jsonl
{"trigger_id":"r3l16_samsungsdi_lfp_ess_T1","case_id":"r3_loop16_samsung_sdi_lfp_ess","trigger_type":"Stage2-Actionable","trigger_date":"2025-12-10","evidence_available":"Samsung SDI America signs >2T won / $1.36B LFP ESS supply deal; deliveries from 2027 for 3 years; shares +6.1% vs KOSPI -0.1%","event_return_pct":6.1,"market_relative_return_pp":6.2,"trigger_outcome_label":"excellent_stage2_actionable_ESS_conversion","promote_to":"Stage2-Actionable"}
{"trigger_id":"r3l16_lges_rivian_T0","case_id":"r3_loop16_lges_rivian_tesla_lfp","trigger_type":"Stage2_supply_contract","trigger_date":"2024-11-07","evidence_available":"LGES Arizona signs 67GWh / 5-year 4695 cylindrical battery supply deal for Rivian R2","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_contract_utilization_gate","promote_to":"Stage2"}
{"trigger_id":"r3l16_lges_tesla_lfp_T1","case_id":"r3_loop16_lges_rivian_tesla_lfp","trigger_type":"Stage2_supply_contract_price_muted","trigger_date":"2025-07-30","evidence_available":"LGES signs $4.3B LFP battery supply deal believed to be Tesla ESS; stock +0.6%","event_return_pct":0.6,"trigger_outcome_label":"Stage2_contract_price_muted","promote_to":"Stage2"}
{"trigger_id":"r3l16_lges_ford_cancel_T1","case_id":"r3_loop16_lges_ford_cancellation_ohio_loss","trigger_type":"4C-watch","trigger_date":"2025-12-18","evidence_available":"Ford cancels 9.6T won / $6.5B LGES EV battery supply deal; LGES -7.6% vs KOSPI -1.4%","event_return_pct":-7.6,"market_relative_return_pp":-6.2,"trigger_outcome_label":"demand_cancellation_4C_watch","promote_to":"4C-watch"}
{"trigger_id":"r3l16_sk_inno_skes_T1","case_id":"r3_loop16_sk_innovation_skes_merger_skon_relief","trigger_type":"Stage2_relief","trigger_date":"2024-08-27","evidence_available":"SK Innovation shareholders approve SK E&S merger to support SK On; shares +5% vs KOSPI -0.5%; SK On cumulative losses 2.3T won","event_return_pct":5,"market_relative_return_pp":5.5,"trigger_outcome_label":"Stage2_financial_relief_not_Green","promote_to":"Stage2_relief"}
{"trigger_id":"r3l16_sk_georgia_layoff_T1","case_id":"r3_loop16_sk_battery_america_layoffs","trigger_type":"4C-watch","trigger_date":"2026-03-06","evidence_available":"SK Battery America lays off 958 workers / 37% workforce at Georgia plant after Ford EV strategy shift away from F-150 Lightning","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"customer_demand_utilization_4C_watch","promote_to":"4C-watch"}
{"trigger_id":"r3l16_catl_lithium_beta_T1","case_id":"r3_loop16_catl_yichun_lithium_beta_korea_materials","trigger_type":"cyclical_Stage2","trigger_date":"2025-08-11","evidence_available":"CATL suspends Yichun lithium mine after license expiry; POSCO Future M +8.3%, L&F +10%, Samsung SDI +3.2%, LGES +2.8%","event_return_pct":"POSCO Future M +8.3 / L&F +10 / Samsung SDI +3.2 / LGES +2.8","trigger_outcome_label":"cyclical_lithium_beta_event_premium","promote_to":"Stage2_cyclical"}
{"trigger_id":"r3l16_samsungsdi_share_sale_T1","case_id":"r3_loop16_samsung_sdi_share_sale_dilution","trigger_type":"4B-watch","trigger_date":"2025-04-09","evidence_available":"Samsung SDI cuts 2T won share-sale price by 14%; shares -1%, KOSPI -0.5%, stock -29.5% YTD","event_return_pct":-1,"trigger_outcome_label":"capital_raise_dilution_4B","promote_to":"4B-watch"}
{"trigger_id":"r3l16_aricell_fire_T0","case_id":"r3_loop16_aricell_battery_factory_fire","trigger_type":"hard_4C","trigger_date":"2024-06-24/2024-08-23","evidence_available":"Aricell battery fire killed 23 and injured 9; police cited quality failures, rushed production, temporary workers and safety-training failures","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"hard_4C_success_battery_safety","promote_to":"4C"}
```

## data/sector_taxonomy/score_weight_profiles_round239_r3_loop16_v1.csv 초안

```csv
archetype,ess_lfp_contract_visibility,us_line_conversion_utilization,oem_contract_cancellation_risk,ira_tax_credit_dependency,battery_jv_financial_structure,lithium_price_beta_duration,battery_factory_safety_trust,ev_growth_headline_without_utilization_penalty,large_gwh_contract_without_margin_penalty,ess_pivot_without_line_yield_penalty,lithium_price_spike_without_margin_penalty,restructuring_relief_without_profit_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
ESS_LFP_LINE_CONVERSION_STAGE2_ACTIONABLE,+5,+5,+2,+3,+1,+1,+2,-3,-3,-4,-1,-1,ESS contract+line conversion,margin/retrofit yield missing,ESS margin+utilization+repeat order,Samsung SDI LFP ESS.
EV_BATTERY_OEM_SUPPLY_STAGE2_WITH_UTILIZATION_GATE,+2,+5,+4,+4,+2,+1,+2,-5,-4,-2,-1,-1,GWh/OEM contract,utilization/margin missing,utilization+margin+customer schedule,LGES Rivian/Tesla.
EV_DEMAND_SLOWDOWN_4C_WATCH,+0,+4,+5,+5,+3,+0,+2,-5,-2,-1,-1,-2,contract cancellation/idling,demand recovery pending,N/A,LGES Ford/SK layoffs.
BATTERY_JV_RESTRUCTURING_RELIEF_STAGE2_WITH_FINANCIAL_4B,+0,+2,+3,+2,+5,+0,+1,-3,-2,-1,-1,-5,merger/financial relief,profitability missing,SK On breakeven+debt improvement,SK Innovation/SK E&S.
LITHIUM_SUPPLY_SHOCK_CYCLICAL_STAGE2,+1,+0,+1,+0,+0,+5,+1,-1,-1,-1,-5,-1,lithium supply shock,cathode margin missing,sustained lithium rebound+margin,CATL/POSCO Future M/L&F.
BATTERY_MATERIAL_LITHIUM_BETA_EVENT_PREMIUM,+0,+0,+1,+0,+0,+5,+1,-1,-1,-1,-5,-1,materials rally,inventory/ASP pass-through missing,ASP+margin recovery,POSCO Future M/L&F event premium.
BATTERY_FACTORY_SAFETY_HARD_4C,+0,+0,+2,+0,+1,+0,+5,-1,-1,-1,-1,-1,fire/death/quality failure,remediation missing,N/A,Aricell hard 4C.
CAPITAL_RAISE_DILUTION_4B,+1,+2,+2,+2,+3,+0,+1,-2,-2,-2,-1,-4,capex funding with dilution,demand/margin missing,capex utilization+margin,Samsung SDI share sale.
```

---

# 이번 R3 Loop 16 결론

```text
1. Samsung SDI LFP ESS는 이번 R3의 가장 강한 Stage2-Actionable이다.
   2T won / $1.36B 계약, 2027년부터 3년 공급, U.S. line conversion, +6.1% price reaction이 닫혔다.

2. LGES Rivian/Tesla 계약은 Stage2지만 Green은 아니다.
   Rivian 67GWh와 Tesla LFP $4.3B는 좋지만, price muted와 utilization/margin gate가 남아 있다.

3. LGES Ford cancellation은 R3 4C-watch다.
   $6.5B 계약 취소, -7.6% 주가반응, Q1 2026 손실, Ohio plant idling이 연결됐다.

4. SK Innovation-SK E&S merger는 Stage2 relief다.
   SK On 재무구조 보강에는 긍정적이지만, profit turnaround는 아니다.

5. SK Battery America layoffs는 utilization 4C-watch다.
   Ford F-150 Lightning 수요 변화가 실제 인력감축으로 나타났다.

6. CATL lithium mine suspension은 cyclical Stage2다.
   POSCO Future M/L&F가 급등했지만 lithium beta일 뿐, cathode margin 확인 전에는 Yellow가 아니다.

7. Samsung SDI share-sale cut은 4B다.
   capex funding과 dilution을 동시에 봐야 한다.

8. Aricell fire는 battery safety hard 4C다.
   품질결함·사망사고·안전훈련 실패는 배터리 제조 valuation의 hard gate다.
```

한 문장으로 압축하면:

> **R3 Loop 16에서 배운 핵심은 “EV/배터리 계약 headline”이 아니라, ESS 전환의 line utilization, LFP margin, OEM cancellation risk, IRA 보조금 의존도, lithium ASP pass-through, battery safety trust가 닫혀야 Stage3로 올릴 수 있다는 것이다. 반대로 GWh 계약, capex funding, lithium price spike, restructuring relief만으로는 4B/false positive가 되기 쉽다.**

[1]: https://www.reuters.com/world/asia-pacific/samsung-sdis-us-unit-signs-14-bln-lfp-battery-deal-us-customer-2025-12-09/?utm_source=chatgpt.com "Samsung SDI unit signs US battery deal worth over $1.36 bln for energy storage systems"
[2]: https://www.reuters.com/technology/lg-energy-solution-signs-5-year-battery-supply-deal-with-rivian-2024-11-07/?utm_source=chatgpt.com "LG Energy Solution signs 5-year battery supply deal with Rivian"
[3]: https://www.wsj.com/business/autos/lg-energy-clinches-4-3-billion-battery-deal-with-tesla-45c6e45c?utm_source=chatgpt.com "LG Energy Clinches $4.3 Billion Battery Deal With Tesla"
[4]: https://www.reuters.com/business/finance/south-koreas-lg-energy-solution-ends-65-billion-ev-battery-supply-deal-with-ford-2025-12-17/?utm_source=chatgpt.com "Ford cancels EV battery deal worth $6.5 billion with South Korea's LG Energy Solution"
[5]: https://www.reuters.com/world/asia-pacific/lg-energy-solution-swings-loss-amid-weak-ev-demand-2026-04-30/?utm_source=chatgpt.com "LG Energy Solution swings to loss amid weak North American EV demand"
[6]: https://www.reuters.com/markets/deals/south-koreas-sk-innovation-agrees-merger-with-sk-es-part-overhaul-2024-07-17/?utm_source=chatgpt.com "South Korea's SK Innovation agrees merger with SK E&S as part of overhaul"
[7]: https://www.reuters.com/markets/deals/sk-innovation-shareholders-approve-merger-plan-with-sk-es-yonhap-reports-2024-08-27/?utm_source=chatgpt.com "SK Innovation shareholders approve merger seen shoring up loss-making battery unit"
[8]: https://apnews.com/article/79a4ec7a5b7f2816f64033f8b3d4898d?utm_source=chatgpt.com "SK lays off nearly 1,000 workers at Georgia plant amid cooling automaker EV plans"
[9]: https://www.wsj.com/finance/commodities-futures/ev-battery-giant-catl-suspends-mining-project-67693725?utm_source=chatgpt.com "EV Battery Giant CATL Suspends Mining Project"
[10]: https://www.reuters.com/markets/asia/samsung-sdi-cuts-stock-offering-price-by-14-2025-04-09/?utm_source=chatgpt.com "Samsung SDI cuts pricing of $1.4 billion share-sale as global markets tumble"
[11]: https://www.reuters.com/world/asia-pacific/deadly-fire-south-korea-battery-maker-due-quality-failure-police-say-2024-08-23/?utm_source=chatgpt.com "South Korea police blame quality failures for fatal fire at battery maker"

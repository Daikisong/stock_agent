순서상 이번은 **R3 Loop 15 — 2차전지·전기차·친환경 trigger-level price validation 라운드**다.

이번 R3부터는 핵심을 이렇게 둔다.

```text
기존 질문:
"이 배터리 뉴스는 Stage 3인가?"

이번 질문:
"EV / ESS / 소재 / 리튬 / 안전 / 계약 trigger 중
어느 trigger에서 진입했으면 돈이 됐고,
어느 trigger는 이미 4B 또는 4C였는가?"
```

```text
round = R3 Loop 15
round_id = round_226
large_sector = SECONDARY_BATTERY_EV_GREEN
method = trigger_level_backtest_v1
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R4 Loop 15
```

이번에도 KRX/Naver/Yahoo/Stooq의 수정주가 일봉 OHLC 30D/90D/180D/1Y window를 안정적으로 직접 추출하지 못했다. 그래서 full MFE/MAE는 `price_data_unavailable_after_deep_search`로 두고, Reuters/FT/MarketWatch/AP의 **reported event return, event price, 계약금액, OP, 매출, subsidy, cancellation, fire/safety event**를 trigger anchor로 쓴다. 단, **OHLC 미확보를 이유로 Stage 후보 자체를 강등하지 않는다.**

---

# 1. 이번 라운드 대섹터

```text
R3 = 2차전지·전기차·친환경
```

이번 R3의 core gate는 아래다.

```text
EV battery:
EV demand → customer model plan → battery call-off → plant utilization → AMPC/subsidy → margin

ESS battery:
data center/grid demand → LFP/ESS contract → line conversion → delivery schedule → margin → repeat order

Cathode / materials:
lithium/nickel price → ASP pass-through → order call-off → inventory write-down → margin

Battery equipment / separator:
cell maker capex → actual equipment order → utilization → customer concentration → margin

Green capex / localization:
IRA/FEOC compliance → U.S. plant economics → subsidy durability → funding → ROIC

Safety:
fire / misleading battery disclosure / factory safety failure → regulatory cost → brand trust → demand impact
```

---

# 2. 대상 canonical archetype

```text
BATTERY_AMPC_PROFIT_STAGE2_YELLOW
ESS_LFP_PIVOT_STAGE2_ACTIONABLE
EV_DEMAND_CONTRACT_CANCELLATION_4C
SIGNED_CATHODE_CONTRACT_COLLAPSE_HARD_4C
LITHIUM_PRICE_EVENT_PREMIUM
UPSTREAM_LITHIUM_SUPPLY_STAGE2
FEOC_CATHODE_OWNERSHIP_STAGE2
BATTERY_SAFETY_TRUST_HARD_4C_REFERENCE
```

---

# 3. deep sub-archetype

```text
LG Energy Solution:
- AMPC tax credit profit beat
- Q2 2025 OP +152%
- AMPC 제외 OP 거의 0
- Ford / Freudenberg contract cancellation 13.5T won
- Ohio asset sale / Ultium restart uncertainty

Samsung SDI:
- EV demand slump / Q4 2024 OP loss
- ESS LFP pivot
- 2T won / $1.36B U.S. ESS contract
- line conversion from EV to ESS

SK Innovation / SK On:
- Ford JV dissolution
- $11.4B original JV
- Q3 2025 OP loss
- Georgia layoffs
- EV → ESS pivot

L&F:
- Tesla 4680 high-nickel cathode supply
- $2.9B → $7,386 contract collapse
- signed amount vs actual call-off hard 4C

POSCO Future M / L&F / battery material basket:
- CATL Yichun mine suspension
- lithium price supply-shock rally
- POSCO Future M +8.3%, L&F +10%
- event premium vs durable ASP/margin

POSCO / lithium upstream:
- MinRes Wodgina/Mt Marion JV stake
- $765M deal
- spodumene prices still far below 2022 peak
- upstream supply security vs price-cycle risk

LG Chem:
- Toyota Tsusho 25% cathode plant stake
- Huayou stake reduced from 49% to 24%
- FEOC / China exposure mitigation

Battery safety:
- Aricell / S-Connect Hwaseong fire
- EV battery-brand disclosure and Mercedes/Farasis fire
- safety trust / disclosure hard gate
```

---

# 4. 선정 case 요약

| bucket                           | case                                  | 핵심 판정                                                                          |
| -------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------ |
| Stage3-Yellow candidate          | LG Energy Solution AMPC profit beat   | OP +152%, 주가 +2.4%지만 AMPC 제외 OP 1.4B won이라 subsidy dependency overlay          |
| Stage2-Actionable                | Samsung SDI ESS LFP pivot             | 2T won / $1.36B ESS contract, +6.1%, EV line conversion                        |
| 4C-thesis-break                  | LGES / SK On / Ford cancellations     | LGES 9.6T + 3.9T won cancellations, SK On Ford JV 종료                           |
| hard 4C                          | L&F / Tesla                           | $2.9B cathode contract → $7,386                                                |
| event premium                    | CATL mine suspension lithium rally    | POSCO Future M +8.3%, L&F +10%, SDI +3.2%, LGES +2.8%                          |
| Stage2 supply-security           | POSCO / MinRes lithium JV             | $765M deal, upstream lithium 확보, but lithium price-cycle risk                  |
| Stage2 regulatory-risk reduction | LG Chem / Toyota Tsusho cathode plant | China Huayou stake 49%→24%, FEOC mitigation                                    |
| hard reference                   | Aricell/S-Connect + EV battery fires  | S-Connect -22.5%, 23 deaths, quality failure, EV battery disclosure regulation |

---

# 5. Case별 trigger grid

## Case A — LG Energy Solution / AMPC profit beat vs subsidy dependency

```text
symbol = 373220
case_type = Stage3-Yellow candidate + 4C subsidy/deal-risk overlay
archetype = BATTERY_AMPC_PROFIT_STAGE2_YELLOW
```

### Trigger grid

| trigger | type                           |       date | 당시 공개 evidence                                                           | 가격 anchor                        | outcome                            |
| ------- | ------------------------------ | ---------: | ------------------------------------------------------------------------ | -------------------------------- | ---------------------------------- |
| T0      | awareness                      |  2024~2025 | EV demand 둔화, U.S. IRA/AMPC 의존도 상승                                       | LGES shares -8% YTD context      | weak watch                         |
| T1      | Stage2 evidence                | 2025-07-07 | Q2 OP estimate 492B won, +152% YoY, consensus 294B won 상회                | +2.4%, 318,000 won               | Stage2-Actionable                  |
| T2      | Stage3-Yellow                  | 2025-07-07 | U.S. plant output + AMPC로 OP beat, non-China battery winner narrative    | sales -9.7%, AMPC 제외 OP 1.4B won | Yellow with subsidy overlay        |
| T3      | 4C-watch                       | 2025-12-17 | Ford 9.6T won / $6.5B EV battery supply deal cancellation                | direct price unavailable         | customer model plan break          |
| T4      | 4C-watch                       | 2025-12-26 | Freudenberg 3.9T won cancellation, total lost expected revenue 13.5T won | direct price unavailable         | hard watch                         |
| T5      | partial relief / restructuring | 2025-12-24 | Ohio factory assets sold to Honda for $2.86B, JV efficiency              | no price                         | balance-sheet / operational relief |
| T6      | 4C-watch                       | 2026-05-12 | GM-LGES Ohio plant restart uncertain, 850 workers laid off since Jan     | no price                         | demand-utilization watch           |

LGES는 R3에서 가장 미묘한 case다. 2025년 7월 Q2 OP가 492B won으로 +152% YoY였고 consensus 294B won을 크게 넘었다. 주가도 +2.4%로 318,000 won까지 올랐다. 그러나 FT는 AMPC를 제외하면 OP가 1.4B won에 불과하다고 보도했다. 즉 이 trigger는 **Stage3-Yellow 후보**지만, Green이 아니라 `subsidy_dependency_overlay`가 반드시 붙어야 한다. ([Financial Times][1])

그 뒤 Ford 9.6T won EV battery supply deal termination, Freudenberg 3.9T won cancellation이 이어지며 LGES는 10일도 안 되는 기간에 총 13.5T won expected revenue를 잃었다. 이건 AMPC profit beat가 Green이 아니라 **customer call-off와 EV model-plan risk를 같이 봐야 하는 Stage3-Yellow**였다는 증거다. ([Reuters][2])

### Trigger price validation row

```json
{
  "case_id": "r3_loop15_lges_ampc_profit_dealrisk",
  "symbol": "373220",
  "best_entry_trigger": "T1/T2",
  "best_entry_trigger_type": "Stage2-Actionable_to_Stage3-Yellow_with_subsidy_overlay",
  "t1_date": "2025-07-07",
  "t1_entry_price_anchor_krw": 318000,
  "t1_event_return_pct": 2.4,
  "q2_2025_op_krw_bn": 492,
  "q2_2025_op_yoy_pct": 152,
  "q2_2025_op_consensus_krw_bn": 294,
  "op_vs_consensus_pct": 67.3,
  "q2_2025_sales_krw_trn": 5.6,
  "q2_2025_sales_yoy_pct": -9.7,
  "op_ex_ampc_krw_bn": 1.4,
  "op_margin_ex_ampc_pct": 0.03,
  "ford_contract_cancel_krw_trn": 9.6,
  "freudenberg_contract_cancel_krw_trn": 3.9,
  "total_lost_expected_revenue_krw_trn": 13.5,
  "honda_asset_sale_usd_bn": 2.86,
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage3_Yellow_not_Green_due_subsidy_and_customer_calloff_risk",
  "stage_gate_correction": "AMPC-driven profit beat can be Yellow, but Green requires ex-subsidy margin and customer call-off durability"
}
```

### 판정

```text
score_price_alignment = Stage3-Yellow_with_4C_overlay
old_error = OP beat만 보고 Green 처리
new_rule = AMPC 제외 OP / customer cancellation risk를 반드시 overlay
```

---

## Case B — Samsung SDI / ESS LFP pivot

```text
symbol = 006400
case_type = Stage2-Actionable / Stage3-Yellow candidate
archetype = ESS_LFP_PIVOT_STAGE2_ACTIONABLE
```

### Trigger grid

| trigger | type            |       date | 당시 공개 evidence                                                                                     | 가격 anchor                 | outcome           |
| ------- | --------------- | ---------: | -------------------------------------------------------------------------------------------------- | ------------------------- | ----------------- |
| T0      | 4C-watch        | 2024-06-28 | Rivian sales target 57k vs market 82k, Samsung SDI net profit forecast -12%, target -14%           | shares +0.3%, 362,000 won | EV demand warning |
| T1      | 4C-watch        | 2025-03-05 | CEO: EV demand sluggish until H1 2026, Q4 2024 OP loss 257B won                                    | no price                  | thesis watch      |
| T2      | Stage2 evidence | 2025-12-10 | U.S. unit signs >2T won / $1.36B LFP ESS deal                                                      | +6.1%, KOSPI -0.1%        | Stage2-Actionable |
| T3      | Stage3-Yellow   | 2025-12-10 | delivery 2027부터 3년, U.S. plant existing lines converted from EV to ESS, data-center/storage demand | execution pending         | Yellow candidate  |
| T4      | 4B-watch        |        N/A | ESS pivot 과열/line conversion risk                                                                  | full OHLC unavailable     | watch             |
| T5      | hard 4C         |        N/A | delivery failure 없음                                                                                | no hard 4C                | pending           |

Samsung SDI는 R3에서 “EV 둔화 → ESS pivot”을 가장 잘 보여준다. 2024년에는 Rivian sales target miss와 EV battery demand 둔화 때문에 Nomura가 net profit forecast를 -12%, target을 -14% 낮췄다. 2025년 3월에는 CEO가 EV demand가 2026년 상반기까지 부진할 수 있다고 했고, Q4 2024 OP loss는 257B won이었다. ([마켓워치][3])

반대로 2025년 12월에는 Samsung SDI America가 U.S. customer에 LFP ESS battery를 2T won 이상, $1.36B 규모로 공급하는 계약을 맺었고, 주가는 +6.1%였다. 기존 EV production line을 ESS로 전환한다는 점도 중요하다. 이 trigger는 `Stage2-Actionable`, 보수적으로 `Stage3-Yellow candidate`다. 다만 delivery가 2027년부터라 Green은 아니다. ([Reuters][4])

### Trigger price validation row

```json
{
  "case_id": "r3_loop15_samsung_sdi_ess_lfp_pivot",
  "symbol": "006400",
  "best_entry_trigger": "T2/T3",
  "best_entry_trigger_type": "Stage2-Actionable_to_Stage3-Yellow_candidate",
  "t0_date": "2024-06-28",
  "t0_entry_price_anchor_krw": 362000,
  "t0_event_return_pct": 0.3,
  "rivian_sales_target_units": 57000,
  "rivian_market_expectation_units": 82000,
  "net_profit_forecast_cut_pct": -12,
  "target_price_cut_pct": -14,
  "target_price_after_krw": 480000,
  "t1_q4_2024_op_loss_krw_bn": 257,
  "t2_date": "2025-12-10",
  "t2_event_return_pct": 6.1,
  "kospi_same_context_pct": -0.1,
  "market_relative_return_pp": 6.2,
  "ess_contract_value_krw_trn": 2.0,
  "ess_contract_value_usd_bn": 1.36,
  "delivery_start": 2027,
  "delivery_duration_years": 3,
  "line_conversion_from_ev_to_ess": true,
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_Actionable_ESS_pivot",
  "stage_gate_correction": "ESS LFP contract + line conversion + relative strength can promote Stage2, but Green needs delivery and margin"
}
```

### 판정

```text
score_price_alignment = Stage2_promote_candidate
old_label = EV battery downturn watch
new_label = ESS pivot Stage2-Actionable
reason = EV 부진을 ESS LFP 계약과 line conversion으로 방어하는 trigger
```

---

## Case C — SK Innovation / SK On / Ford JV termination

```text
symbol = 096770
case_type = 4C-thesis-break / ESS pivot watch
archetype = EV_DEMAND_CONTRACT_CANCELLATION_4C
```

### Trigger grid

| trigger | type              |                                              date | 당시 공개 evidence                                                                                             | 가격 anchor           | outcome                 |
| ------- | ----------------- | ------------------------------------------------: | ---------------------------------------------------------------------------------------------------------- | ------------------- | ----------------------- |
| T0      | Stage2            |                                              2022 | SK On-Ford $11.4B U.S. battery JV, EV growth story                                                         | no current price    | original growth thesis  |
| T1      | 4C-watch          |                                        2025-12-11 | SK On/Ford U.S. JV 종료, Kentucky는 Ford, Tennessee는 SK On, Q3 2025 OP loss 124.8B won                        | no direct price     | thesis break            |
| T2      | 4C spread         |                                        2025-12-16 | Ford $20B charge / F-150 Lightning halt, SK Innovation -3%, LGES -6%, SK IE Tech -5%, EcoPro Materials -5% | reported returns    | Korea battery-chain hit |
| T3      | hard confirmation |                                        2026-03-06 | SK Battery America lays off 958 workers, 37% workforce, Georgia plant opened 2022 cost $2.6B               | no KRX direct price | operating impact        |
| T4      | relief candidate  |                                      2025-12~2026 | SK On to operate Tennessee, ESS business expansion / Flatiron LFP supply                                   | no price            | ESS pivot watch         |
| T5      | hard 4C           | if JV dissolution forces impairment / funding gap | not confirmed                                                                                              | pending             |                         |

SK On은 “EV growth contract가 실제로 깨지는” R3 4C case다. 2025년 12월 SK On은 Ford와의 U.S. battery JV를 종료하기로 했고, 원래 2022년에 $11.4B를 투자하기로 했던 battery plant story가 재편됐다. Reuters는 이 decision이 EV demand 둔화와 U.S. subsidy 종료 이후 한국 battery makers가 ESS로 전략을 바꾸는 맥락이라고 설명했다. Q3 2025 SK On OP loss는 124.8B won이었다. ([Reuters][5])

Ford가 EV strategy를 축소하며 F-150 Lightning을 중단하는 뉴스가 나오자 한국 battery supply chain은 바로 맞았다. MarketWatch는 SK Innovation -3%, LGES -6%, SK IE Tech -5%, EcoPro Materials -5%를 보도했다. 이후 AP는 SK Battery America가 Georgia plant에서 958명, 전체 인력 37%를 layoffs했다고 보도했다. 이건 Stage 2 EV contract story가 4C로 전환된 명확한 사례다. ([마켓워치][6])

### Trigger price validation row

```json
{
  "case_id": "r3_loop15_sk_on_ford_jv_termination",
  "symbol": "096770",
  "best_trigger": "T1/T2",
  "best_trigger_type": "4C-watch_to_thesis_break",
  "original_jv_investment_usd_bn": 11.4,
  "q3_2025_sk_on_op_loss_krw_bn": 124.8,
  "ford_full_ownership_plants": "Kentucky battery plants",
  "sk_on_full_ownership_plant": "Tennessee facility",
  "t2_sk_innovation_event_mae_pct": -3,
  "t2_lges_event_mae_pct": -6,
  "t2_sk_ie_tech_event_mae_pct": -5,
  "t2_ecopro_materials_event_mae_pct": -5,
  "georgia_layoffs_workers": 958,
  "georgia_layoffs_pct_workforce": 37,
  "georgia_plant_cost_usd_bn": 2.6,
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "thesis_break_watch",
  "stage_gate_correction": "EV JV / battery contract must be tied to customer model survival and production schedule; otherwise 4C"
}
```

### 판정

```text
score_price_alignment = thesis_break_watch
reason = EV customer model plan과 JV economics가 깨지면 기존 Stage2 성장 thesis가 4C로 전환
```

---

## Case D — L&F / Tesla cathode contract collapse

```text
symbol = 066970
case_type = hard_4C
archetype = SIGNED_CATHODE_CONTRACT_COLLAPSE_HARD_4C
```

### Trigger grid

| trigger | type               |       date | 당시 공개 evidence                                                              | 가격 anchor              | outcome               |
| ------- | ------------------ | ---------: | --------------------------------------------------------------------------- | ---------------------- | --------------------- |
| T0      | Stage2             |       2023 | Tesla affiliates high-nickel cathode supply deal, 2024~2025 supply period   | no price here          | contract headline     |
| T1      | Stage2-Actionable? |       2023 | expected value $2.9B, 4680 cell material link                               | no full price          | customer-name premium |
| T2      | 4C                 | 2025-12-29 | deal value cut from $2.9B to $7,386                                         | no KRX price in source | hard thesis break     |
| T3      | 4C cause           | 2025-12-29 | Tesla 4680 ramp difficulty, Cybertruck underperformance, EV demand slowdown | no price               | call-off failure      |
| T4      | hard 4C            | 2025-12-29 | contract value collapse -99.9997%                                           | no price               | hard_4c_success       |

L&F는 R3에서 반드시 들어가야 하는 hard 4C다. Reuters는 L&F의 Tesla cathode supply deal value가 $2.9B에서 $7,386로 줄었다고 보도했다. 공급 대상은 Tesla 4680 cells와 연결된 high-nickel cathode materials였고, EV demand slowdown, 4680 production yield/ramp issue, Cybertruck underperformance가 배경으로 언급됐다. 이 case는 “고객명 + 계약금액”이 실제 call-off가 아니면 Stage 3가 아니라는 hard rule이다. ([Reuters][7])

### Trigger price validation row

```json
{
  "case_id": "r3_loop15_lnf_tesla_cathode_contract_collapse",
  "symbol": "066970",
  "best_trigger": "T2",
  "best_trigger_type": "hard_4C",
  "initial_contract_value_usd_bn": 2.9,
  "revised_contract_value_usd": 7386,
  "contract_value_collapse_pct": -99.9997,
  "supply_period": "2024-01_to_2025-12",
  "material": "high-nickel cathode materials",
  "customer": "Tesla and affiliates",
  "application_context": "Tesla 4680 cells",
  "reported_likely_drivers": [
    "EV demand slowdown",
    "Tesla 4680 production/ramp difficulty",
    "Cybertruck underperformance"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "hard_4c_success",
  "stage_gate_correction": "signed contract amount must not be Green without actual call-off and customer model survival"
}
```

### 판정

```text
score_price_alignment = thesis_break
reason = signed contract collapse는 R3 hard 4C
```

---

## Case E — CATL mine suspension / lithium price event premium

```text
symbols = 003670 / 066970 / 006400 / 373220
company_scope = POSCO Future M / L&F / Samsung SDI / LGES
case_type = event_premium
archetype = LITHIUM_PRICE_EVENT_PREMIUM
```

### Trigger grid

| trigger | type            |       date | 당시 공개 evidence                                                                     | 가격 anchor                                                     | outcome              |
| ------- | --------------- | ---------: | ---------------------------------------------------------------------------------- | ------------------------------------------------------------- | -------------------- |
| T0      | awareness       |    2025-08 | lithium price had fallen up to 90% from 2022 peak, supply glut concerns easing     | no KRX direct                                                 | cycle watch          |
| T1      | Stage2 evidence | 2025-08-11 | CATL suspends Yichun mine after license expiry                                     | Ganfeng +21%, Tianqi +18%                                     | lithium supply shock |
| T2      | event premium   | 2025-08-11 | Korean material/battery stocks rally                                               | POSCO Future M +8.3%, L&F +10%, Samsung SDI +3.2%, LGES +2.8% | event premium        |
| T3      | 4B-watch        | 2025-08-11 | CATL says no material operational impact and production resumes if license renewed | no follow-through                                             | speculative          |
| T4      | Stage3-Yellow   |        N/A | durable lithium price recovery / ASP margin not confirmed                          | N/A                                                           | no Yellow            |

이 case는 R3 원자재 event premium이다. CATL이 Yichun lithium mine production을 license expiry로 중단하자 lithium producers가 크게 올랐고, 한국에서도 POSCO Future M +8.3%, L&F +10%, Samsung SDI +3.2%, LGES +2.8%가 나왔다. 하지만 CATL은 license renew 시 production을 재개할 수 있고 운영상 material impact가 없다고 했다. 따라서 이건 Stage3가 아니라 `lithium_price_event_premium`이다. ([월스트리트저널][8])

### Trigger price validation row

```json
{
  "case_id": "r3_loop15_catl_mine_lithium_price_event",
  "symbols": "003670/066970/006400/373220",
  "trigger_date": "2025-08-11",
  "trigger_type": "event_premium",
  "posco_future_m_event_mfe_pct": 8.3,
  "lnf_event_mfe_pct": 10.0,
  "samsung_sdi_event_mfe_pct": 3.2,
  "lges_event_mfe_pct": 2.8,
  "ganfeng_lithium_event_mfe_pct": 21,
  "tianqi_lithium_event_mfe_pct": 18,
  "lithium_price_decline_from_2022_peak_pct": -90,
  "catl_material_impact_claim": "no material impact",
  "license_renewal_possible": true,
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "event_premium_not_stage3",
  "stage_gate_correction": "lithium supply shock rallies require durable lithium price and ASP/margin confirmation before Stage3"
}
```

### 판정

```text
score_price_alignment = event_premium
reason = lithium price event는 material margin evidence 전에는 Stage3 금지
```

---

## Case F — POSCO / MinRes lithium upstream deal

```text
symbols = 005490 / 003670
company_scope = POSCO Holdings / POSCO Future M
case_type = Stage2 supply-security
archetype = UPSTREAM_LITHIUM_SUPPLY_STAGE2
```

### Trigger grid

| trigger | type                        |       date | 당시 공개 evidence                                                                      | 가격 anchor                      | outcome                |
| ------- | --------------------------- | ---------: | ----------------------------------------------------------------------------------- | ------------------------------ | ---------------------- |
| T0      | awareness                   |  2022~2025 | POSCO battery materials / lithium integration narrative                             | no full price                  | Stage1                 |
| T1      | Stage2 evidence             | 2025-11-11 | POSCO buys 30% stake in MinRes lithium JV for $765M                                 | MinRes +10.8%                  | supply-security Stage2 |
| T2      | Stage2-Actionable candidate | 2025-11-11 | Wodgina/Mt Marion indirect 15% interests, spodumene concentrate proportional rights | POSCO direct price unavailable | candidate              |
| T3      | 4C-watch                    | 2025-11-11 | spodumene $880/t vs 2022 peak >$6,000, lithium price still depressed                | no price                       | price-cycle risk       |
| T4      | Stage3-Yellow               |        N/A | downstream margin / cost advantage not confirmed                                    | N/A                            | no Yellow              |

POSCO는 R3 upstream supply security case다. MinRes가 POSCO에 lithium JV stake 30%를 $765M에 팔면서 POSCO는 Wodgina와 Mt Marion에 간접 15% interest를 갖게 되고, 지분 비율에 따라 spodumene concentrate를 받는다. MinRes shares는 +10.8%였다. 다만 Reuters는 spodumene prices가 2022년 $6,000/t 이상에서 2025년 중반 $610까지 내려갔다가 $880 수준으로 회복했지만 여전히 peak와는 거리가 멀다고 설명했다. 즉 이 trigger는 Stage2 supply-security이지 Green은 아니다. ([Reuters][9])

### Trigger price validation row

```json
{
  "case_id": "r3_loop15_posco_minres_lithium_supply_security",
  "symbols": "005490/003670",
  "trigger_date": "2025-11-11",
  "trigger_type": "Stage2_supply_security",
  "minres_deal_value_usd_mn": 765,
  "minres_event_mfe_pct": 10.8,
  "posco_effective_interest_wodgina_pct": 15,
  "posco_effective_interest_mt_marion_pct": 15,
  "spodumene_price_mid_2025_low_usd_t": 610,
  "spodumene_price_august_2025_usd_t": 880,
  "spodumene_2022_peak_usd_t": 6000,
  "operator": "MinRes",
  "posco_direct_price_anchor": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_supply_security_not_Green",
  "stage_gate_correction": "upstream stake improves supply security, but Stage3 requires cost advantage and downstream margin confirmation"
}
```

### 판정

```text
score_price_alignment = success_candidate_stage2
reason = 원재료 확보는 강하지만 lithium price-cycle과 downstream margin이 남음
```

---

## Case G — LG Chem / Toyota Tsusho cathode plant ownership restructuring

```text
symbol = 051910
case_type = Stage2 regulatory-risk reduction
archetype = FEOC_CATHODE_OWNERSHIP_STAGE2
```

### Trigger grid

| trigger | type                        |                   date | 당시 공개 evidence                                               | 가격 anchor         | outcome                   |
| ------- | --------------------------- | ---------------------: | ------------------------------------------------------------ | ----------------- | ------------------------- |
| T0      | awareness                   |              2024~2025 | U.S. IRA / FEOC rule, China exposure in cathode supply chain | no price          | policy watch              |
| T1      | Stage2 evidence             |             2025-09-08 | Toyota Tsusho acquires 25% stake in LG Chem cathode plant    | price unavailable | Stage2                    |
| T2      | Stage2-Actionable candidate |             2025-09-08 | Huayou stake reduced from 49% to 24%, China exposure lowered | price unavailable | regulatory-risk reduction |
| T3      | Stage3-Yellow               |                    N/A | customer qualification / IRA benefit / margin not confirmed  | N/A               | no Yellow                 |
| T4      | 4C-watch                    | if FEOC non-compliance | not confirmed                                                | pending           |                           |

LG Chem은 R3의 regulatory-risk reduction case다. Toyota Tsusho가 LG Chem의 Korea cathode material plant 지분 25%를 취득했고, 중국 Huayou Cobalt 지분은 49%에서 24%로 낮아졌다. 이건 FEOC/IRA 공급망 리스크를 낮추는 Stage2 trigger다. 하지만 실제 customer award, IRA qualification, cathode margin이 확인되기 전에는 Stage3가 아니다. ([Reuters][10])

### Trigger price validation row

```json
{
  "case_id": "r3_loop15_lg_chem_toyota_tsusho_cathode_feoc",
  "symbol": "051910",
  "trigger_date": "2025-09-08",
  "trigger_type": "Stage2_regulatory_risk_reduction",
  "toyota_tsusho_new_stake_pct": 25,
  "huayou_stake_before_pct": 49,
  "huayou_stake_after_pct": 24,
  "china_exposure_reduced": true,
  "feoc_ira_relevance": true,
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_not_Green",
  "stage_gate_correction": "ownership restructuring reduces FEOC risk but Stage3 requires customer award, IRA benefit and cathode margin"
}
```

### 판정

```text
score_price_alignment = success_candidate_stage2
reason = China exposure reduction은 좋지만 cashflow trigger는 아님
```

---

## Case H — Aricell / S-Connect battery safety hard reference

```text
symbol = 096630 / battery-safety basket
case_type = hard_4C_reference
archetype = BATTERY_SAFETY_TRUST_HARD_4C_REFERENCE
```

### Trigger grid

| trigger | type                 |       date | 당시 공개 evidence                                                                                  | 가격 anchor                                   | outcome              |
| ------- | -------------------- | ---------: | ----------------------------------------------------------------------------------------------- | ------------------------------------------- | -------------------- |
| T0      | safety incident      | 2024-06-24 | Hwaseong Aricell lithium battery factory fire                                                   | S-Connect -22.5% on Monday, -1.37% next day | hard 4C              |
| T1      | hard 4C validation   | 2024-06-25 | 23 deaths, 35,000 lithium batteries stored, temporary workers, safety investigation             | same                                        | hard 4C              |
| T2      | quality failure      | 2024-08-23 | police blame production deadline pressure and quality failures; failed April quality inspection | no new price                                | hard validation      |
| T3      | EV safety disclosure | 2024-08-13 | Mercedes EV Farasis fire, 140 cars damaged/destroyed, Korea urges battery-brand disclosure      | no direct battery-stock price               | sector safety watch  |
| T4      | regulatory penalty   | 2026-03-10 | Mercedes fined 11.2B won for misleading EV battery info                                         | no direct Korean battery price              | disclosure hard gate |

Battery safety는 R3의 hard 4C reference다. Aricell fire는 23명 사망, 35,000 lithium batteries, toxic smoke, safety training 문제로 번졌고, parent S-Connect는 사건 당일 -22.5%를 맞았다. 이후 경찰은 deadline을 맞추기 위해 quality failure signs를 무시했고, temporary/unskilled workers와 defect-rate 상승이 safety risk를 키웠다고 밝혔다. 이건 배터리 업종에서 안전/품질/공시가 단순 ESG가 아니라 valuation hard gate라는 뜻이다. ([Reuters][11])

또 EV fire disclosure도 R3의 4C overlay다. 2024년 8월 Incheon Mercedes EV fire는 Farasis battery로 알려졌고 약 140대 차량 피해를 냈으며, 정부는 automakers에 battery supplier disclosure를 요구했다. 2026년에는 Mercedes Korea가 일부 EV battery supplier 정보를 misrepresent한 혐의로 11.2B won fine을 받았다. 이건 battery cell supplier, OEM, 소재사 모두에 `battery_safety_disclosure_trust` 축이 필요하다는 근거다. ([Reuters][12])

### Trigger price validation row

```json
{
  "case_id": "r3_loop15_aricell_sconnect_battery_safety_hard_4c",
  "symbols": "096630/battery_safety_basket",
  "trigger_date": "2024-06-24/2024-08-23",
  "trigger_type": "hard_4C_reference",
  "fatalities": 23,
  "injuries": 9,
  "lithium_batteries_stored": 35000,
  "sconnect_event_mae_pct": -22.5,
  "sconnect_next_day_return_pct": -1.37,
  "quality_inspection_failed_before_fire": true,
  "temporary_unskilled_worker_factor": true,
  "defect_rate_increase_factor": true,
  "ev_fire_damaged_or_destroyed_cars": 140,
  "mercedes_kftc_fine_krw_bn": 11.2,
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "hard_4c_success",
  "stage_gate_correction": "battery safety and supplier disclosure must be explicit hard gate for all battery/EV names"
}
```

### 판정

```text
score_price_alignment = hard_4c_success
reason = 배터리 안전/품질/공시 신뢰는 R3 hard gate
```

---

# 6. Trigger별 가격경로 검증 요약

| case              | best trigger     |      entry anchor |                  event MFE/MAE |      market-relative | full MFE/MAE | outcome                            |
| ----------------- | ---------------- | ----------------: | -----------------------------: | -------------------: | ------------ | ---------------------------------- |
| LGES AMPC         | T1/T2 2025-07-07 |           318,000 |                          +2.4% | KOSPI little changed | unavailable  | Stage3-Yellow with subsidy overlay |
| Samsung SDI ESS   | T2 2025-12-10    |       unavailable |                          +6.1% |               +6.2pp | unavailable  | Stage2-Actionable                  |
| SK On/Ford        | T1/T2 2025-12    |             event |   SKI -3%, LGES -6%, SKIET -5% |          unavailable | unavailable  | thesis_break_watch                 |
| L&F/Tesla         | T2 2025-12-29    |       unavailable |             contract -99.9997% |                  N/A | unavailable  | hard 4C                            |
| CATL lithium      | T2 2025-08-11    |             event | POSCO Future M +8.3%, L&F +10% |          unavailable | unavailable  | event premium                      |
| POSCO/MinRes      | T1 2025-11-11    | POSCO unavailable |                  MinRes +10.8% |          unavailable | unavailable  | supply-security Stage2             |
| LG Chem/Toyota    | T1 2025-09-08    |       unavailable |              price unavailable |          unavailable | unavailable  | FEOC-risk Stage2                   |
| Aricell/S-Connect | T0/T1 2024-06    |             event |               S-Connect -22.5% |          unavailable | unavailable  | hard safety 4C                     |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
Samsung SDI ESS:
2T won LFP ESS contract + line conversion + +6.1%.
Stage2-Actionable로 승격 가능.

LG Chem FEOC ownership:
China Huayou stake 49%→24%.
가격 anchor가 없어서 Stage2까지만.

POSCO/MinRes:
upstream lithium supply-security.
Stage2지만 lithium price-cycle risk 때문에 Yellow 보류.
```

## Stage 2-Actionable entry 성과

```text
LGES AMPC:
OP beat가 강하지만 AMPC 제외 OP가 거의 0.
Stage2-Actionable은 맞지만 Green 금지.

Samsung SDI ESS:
EV demand 부진을 ESS contract로 상쇄하는 trigger.
Stage2-Actionable.

CATL lithium event:
MFE는 컸지만 license renewal 가능성과 no material impact comment 때문에 event premium.
```

## Stage 3-Yellow entry 성과

```text
LGES:
Q2 profit beat + AMPC + U.S. plant output.
Yellow 가능하지만 subsidy/customer-calloff overlay 필수.

Samsung SDI:
ESS LFP contract는 Yellow 후보지만 delivery 2027이라 아직 보수적으로 Stage2-Actionable.

R3에서는 확정 Green 없음.
```

## 기존 점수표가 놓쳤는지 여부

```text
missed_structural:
- 아직 확정 없음.
- Samsung SDI ESS pivot은 full OHLC에서 MFE가 크고 MAE가 얕으면 Stage2_promote_candidate로 승격.
- LGES AMPC profit trigger도 full OHLC에서 검증 필요.

missed_structural보다는 이번 R3의 핵심은:
- EV contract cancellation 4C
- signed contract call-off hard 4C
- ESS pivot Stage2-Actionable
- subsidy dependency overlay
```

---

# 8. score-price alignment 판정

```text
Stage2_promote_candidate:
- Samsung SDI ESS LFP pivot.
- LGES AMPC profit beat, 단 subsidy overlay.
- POSCO/MinRes lithium supply-security, 단 margin gate.

Stage3-Yellow candidate:
- LGES AMPC profit beat.
- Samsung SDI ESS LFP contract, pending delivery/margin.

Stage3-Green:
- 이번 라운드 확정 없음.

price_moved_without_evidence:
- CATL mine suspension에 따른 lithium rally가 durable price/margin evidence 없이 과열될 경우.

event_premium:
- POSCO Future M / L&F / Samsung SDI / LGES lithium rally.
- POSCO upstream JV, if treated as immediate earnings.

false_positive_score:
- LGES AMPC OP beat를 subsidy 제외 margin 없이 Green 처리하면 false positive 위험.
- Samsung SDI ESS contract를 delivery 전 Green 처리하면 false positive 위험.

thesis_break:
- SK On/Ford JV termination.
- LGES Ford/Freudenberg cancellations.
- L&F/Tesla contract collapse.

hard_4c_success:
- L&F/Tesla contract value collapse.
- Aricell/S-Connect battery safety reference.
```

---

# 9. 점수비중 교정

## 올릴 축

```text
actual_customer_calloff +5
contract_cancellation_risk +5
ex_subsidy_operating_margin +5
ampc_subsidy_durability +4
ess_lfp_contract_quality +4
line_conversion_execution +4
customer_model_survival +5
battery_safety_disclosure_trust +5
raw_material_price_durability +4
feoc_ira_compliance_quality +4
```

### 근거

L&F는 $2.9B 계약이 $7,386로 붕괴하면서 `actual_customer_calloff`가 R3의 최상위 gate임을 보여줬다. LGES는 OP beat가 강해도 AMPC 제외 OP가 거의 0이어서 `ex_subsidy_margin`이 필요하다. Samsung SDI는 EV demand 부진 속에서 ESS LFP로 pivot하는 Stage2-Actionable을 보여줬다. Aricell과 Mercedes/Farasis case는 battery safety와 disclosure trust가 hard gate라는 근거다.

## 내릴 축

```text
signed_contract_amount_only -5
ev_growth_headline_only -5
subsidy_included_op_only -5
lithium_price_event_only -4
upstream_stake_without_margin -4
line_conversion_without_delivery -4
customer_name_without_model_survival -5
battery_safety_ignored -5
```

### 근거

LGES/Ford, SK On/Ford, L&F/Tesla 모두 “고객명 + 계약금액 + EV growth”만으로는 충분하지 않다는 반례다. CATL lithium event는 강한 가격반응을 냈지만 durable lithium price와 소재 margin 확인 전에는 event premium이다. POSCO upstream stake도 supply security이지 즉시 earnings Green은 아니다.

---

# 10. Stage 2-Actionable 승격 조건

R3 Loop 15 shadow rule:

```text
R3에서 Stage 2 evidence가 아래 중 3개 이상이면 Stage2-Actionable로 승격한다.

1. 계약금액이 크고 delivery schedule이 명확하다.
2. customer / application / chemistry가 구체적이다.
3. 기존 EV line을 ESS 등 더 강한 수요처로 전환하는 execution evidence가 있다.
4. trigger 당일 market-relative +5pp 이상 가격 반응이 있다.
5. ex-subsidy margin 또는 subsidy durability가 구체적으로 계산된다.
6. FEOC/IRA compliance risk가 구조적으로 낮아진다.
```

적용 case:

```text
Samsung SDI ESS LFP
LGES AMPC profit beat, 단 subsidy overlay
POSCO/MinRes lithium supply security, 낮은 확신
LG Chem/Toyota cathode ownership, 낮은 확신
```

---

# 11. Stage 3-Yellow 조건

```text
Stage3-Yellow:
- 계약/수요/마진 중 2개 이상이 숫자로 닫힘
- 하지만 delivery, call-off, subsidy, plant utilization, line conversion, customer model survival 중 하나가 남아 있음
```

후보:

```text
LGES:
OP beat + AMPC + U.S. production.
남은 gate: ex-AMPC margin, Ford/Freudenberg call-off.

Samsung SDI:
ESS LFP contract + line conversion + strong event return.
남은 gate: delivery 2027, converted-line margin.

POSCO:
upstream lithium stake + offtake rights.
남은 gate: lithium price, downstream margin.
```

---

# 12. Stage 3-Green 조건

```text
Stage3-Green:
- 계약이 실제 call-off / shipment / revenue로 전환됨
- ex-subsidy margin이 양호함
- plant utilization이 올라감
- customer model plan이 유지됨
- full-window MFE/MAE가 우호적
```

이번 R3 Loop 15에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
```

이건 부정적인 결론이 아니라, R3의 현 시점 핵심이 **EV growth에서 ESS pivot / contract risk / safety risk로 전환 중**이라는 뜻이다.

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- lithium price event로 소재주가 +8~10% 급등하지만 durable price/margin 확인 없음
- subsidy 포함 OP beat가 크지만 ex-subsidy OP가 거의 없음
- ESS/data-center headline으로 EV line conversion 기대가 과도함
- upstream lithium stake를 즉시 earnings로 가격화
```

적용:

```text
CATL mine suspension lithium rally:
event premium, 4B-watch.

LGES AMPC:
OP beat는 좋지만 AMPC 제외 OP 거의 0이면 Green이 아니라 Yellow+4B risk.

Samsung SDI ESS:
line conversion execution 전 급등하면 4B-watch.
```

---

# 14. 4C hard gate 조건

```text
R3 4C:
- signed contract value collapse
- customer model cancellation / EV program halt
- JV dissolution
- plant layoff / utilization collapse
- battery fire / safety failure
- misleading battery supplier disclosure
- subsidy rollback that destroys economics
- line conversion failure
```

이번 R3 Loop 15 hard 4C:

```text
1. L&F / Tesla contract collapse
2. Aricell / S-Connect safety reference
```

Strong 4C-watch:

```text
LGES Ford/Freudenberg cancellations
SK On/Ford JV dissolution
SK Battery America layoffs
Mercedes/Farasis EV fire disclosure issue
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_226.md 요약

```md
# R3 Loop 15. Secondary Battery / EV / Green Trigger-level Price Validation

이번 라운드는 R3 Loop 15 trigger-level validation 라운드다.

핵심 결론:
- LG Energy Solution is Stage3-Yellow with subsidy and customer-calloff overlay. Q2 2025 OP was 492B won, +152% YoY and far above 294B won consensus; shares +2.4% to 318,000 won. But ex-AMPC OP was only 1.4B won and sales fell 9.7%. Later Ford and Freudenberg cancellations erased 13.5T won expected revenue.
- Samsung SDI ESS LFP pivot is Stage2-Actionable. U.S. unit signed a >2T won / $1.36B LFP ESS deal and shares rose +6.1% vs KOSPI -0.1%. EV-demand slump remains, but line conversion from EV to ESS is actionable. Green requires delivery and margin.
- SK On / SK Innovation Ford JV termination is 4C-watch. Original Ford/SK On U.S. JV was $11.4B. SK On ended the JV with Ford, while Ford EV retreat hit Korean battery-chain shares: SK Innovation -3%, LGES -6%, SK IE Tech -5%, EcoPro Materials -5%. SK Battery America later laid off 958 workers, 37% of its Georgia workforce.
- L&F / Tesla is hard 4C. Tesla cathode supply deal value collapsed from $2.9B to $7,386. Signed contract amount is not Green without actual call-off and customer model survival.
- CATL Yichun mine suspension is lithium event premium. POSCO Future M +8.3%, L&F +10%, Samsung SDI +3.2%, LGES +2.8%, but CATL said no material impact and production could resume if license renewed.
- POSCO / MinRes lithium JV is Stage2 supply-security. POSCO will pay $765M for a 30% stake in a MinRes lithium JV, gaining indirect 15% exposure to Wodgina and Mt Marion. Green requires cost advantage and downstream margin.
- LG Chem / Toyota Tsusho cathode plant ownership change is Stage2 regulatory-risk reduction. Toyota Tsusho takes 25%, Huayou stake falls from 49% to 24%. FEOC/IRA risk reduced, but customer awards and margin remain.
- Aricell / S-Connect is battery safety hard 4C reference. Hwaseong fire killed 23 workers; S-Connect plunged 22.5% on the fire news. Police later blamed quality failures and deadline pressure. EV battery supplier disclosure also becomes hard gate after Mercedes/Farasis fire and KFTC fine.

Main calibration:
- Raise actual_customer_calloff, contract_cancellation_risk, ex_subsidy_operating_margin, AMPC subsidy durability, ESS LFP contract quality, line conversion execution, customer model survival, battery safety disclosure trust, raw-material price durability, FEOC/IRA compliance quality.
- Lower signed_contract_amount_only, EV growth headline-only, subsidy-included OP-only, lithium price event-only, upstream stake without margin, line conversion without delivery, customer name without model survival, battery safety ignored.
```

## docs/checkpoints/checkpoint_28a_round226_r3_loop15.md 요약

```md
# Checkpoint 28A Round 226 R3 Loop 15 Trigger-level Calibration

## 반영 내용
- R3 Loop 15 trigger-level validation을 수행했다.
- LGES, Samsung SDI, SK On/SK Innovation, L&F, POSCO Future M/L&F lithium event, POSCO/MinRes, LG Chem/Toyota Tsusho, Aricell/S-Connect battery safety를 검토했다.
- full adjusted OHLC window는 확보하지 못했으므로 Reuters / FT / MarketWatch / AP의 reported event return과 event price anchor를 사용했다.
- OHLC 미확보를 이유로 Stage 후보를 강등하지 않고, price_data_unavailable_after_deep_search로 분리 기록했다.

## 핵심 보정
- EV battery Stage3는 subsidy 포함 OP가 아니라 ex-subsidy margin과 customer call-off로 검증한다.
- ESS LFP contract + line conversion + relative strength는 Stage2-Actionable 승격 후보.
- signed contract amount는 actual call-off가 없으면 Green 금지.
- lithium price event는 durable price/margin 확인 전까지 event premium.
- battery safety / supplier disclosure trust는 R3 hard gate.
```

## data/e2r_case_library/cases_r3_loop15_round226.jsonl 초안

```jsonl
{"case_id":"r3_loop15_lges_ampc_profit_dealrisk","symbol":"373220","company_name":"LG Energy Solution","case_type":"Stage3_Yellow_with_4C_overlay","primary_archetype":"BATTERY_AMPC_PROFIT_STAGE2_YELLOW","best_trigger":"T1/T2","stage_candidate":"Stage3-Yellow","price_validation":{"entry_price_anchor_krw":318000,"event_return_pct":2.4,"q2_2025_op_krw_bn":492,"q2_2025_op_yoy_pct":152,"q2_2025_op_consensus_krw_bn":294,"op_vs_consensus_pct":67.3,"q2_2025_sales_krw_trn":5.6,"q2_2025_sales_yoy_pct":-9.7,"op_ex_ampc_krw_bn":1.4,"op_margin_ex_ampc_pct":0.03,"ford_contract_cancel_krw_trn":9.6,"freudenberg_contract_cancel_krw_trn":3.9,"total_lost_expected_revenue_krw_trn":13.5,"honda_asset_sale_usd_bn":2.86,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage3-Yellow_with_4C_overlay","notes":"AMPC-driven OP beat can be Yellow, but Green needs ex-subsidy margin and durable customer call-off."}
{"case_id":"r3_loop15_samsung_sdi_ess_lfp_pivot","symbol":"006400","company_name":"Samsung SDI","case_type":"Stage2_promote_candidate","primary_archetype":"ESS_LFP_PIVOT_STAGE2_ACTIONABLE","best_trigger":"T2/T3","stage_candidate":"Stage2-Actionable_to_Stage3-Yellow_candidate","price_validation":{"rivian_sales_target_units":57000,"rivian_market_expectation_units":82000,"net_profit_forecast_cut_pct":-12,"target_price_cut_pct":-14,"target_price_after_krw":480000,"q4_2024_op_loss_krw_bn":257,"ess_contract_value_krw_trn":2.0,"ess_contract_value_usd_bn":1.36,"event_return_pct":6.1,"kospi_same_context_pct":-0.1,"market_relative_return_pp":6.2,"delivery_start":2027,"delivery_duration_years":3,"line_conversion_from_ev_to_ess":true,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate","notes":"ESS LFP contract and EV-to-ESS line conversion make this Stage2-Actionable; Green needs delivery and margin."}
{"case_id":"r3_loop15_sk_on_ford_jv_termination","symbol":"096770","company_name":"SK Innovation / SK On","case_type":"thesis_break_watch","primary_archetype":"EV_DEMAND_CONTRACT_CANCELLATION_4C","best_trigger":"T1/T2","stage_candidate":"4C-watch","price_validation":{"original_jv_investment_usd_bn":11.4,"q3_2025_sk_on_op_loss_krw_bn":124.8,"ford_full_ownership_plants":"Kentucky battery plants","sk_on_full_ownership_plant":"Tennessee facility","sk_innovation_event_mae_pct":-3,"lges_event_mae_pct":-6,"sk_ie_tech_event_mae_pct":-5,"ecopro_materials_event_mae_pct":-5,"georgia_layoffs_workers":958,"georgia_layoffs_pct_workforce":37,"georgia_plant_cost_usd_bn":2.6,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","notes":"EV JV / battery contract must be tied to customer model survival and production schedule."}
{"case_id":"r3_loop15_lnf_tesla_cathode_contract_collapse","symbol":"066970","company_name":"L&F","case_type":"hard_4c","primary_archetype":"SIGNED_CATHODE_CONTRACT_COLLAPSE_HARD_4C","best_trigger":"T2","stage_candidate":"4C","price_validation":{"initial_contract_value_usd_bn":2.9,"revised_contract_value_usd":7386,"contract_value_collapse_pct":-99.9997,"supply_period":"2024-01_to_2025-12","material":"high-nickel cathode materials","customer":"Tesla and affiliates","application_context":"Tesla 4680 cells","reported_likely_drivers":["EV demand slowdown","Tesla 4680 production/ramp difficulty","Cybertruck underperformance"],"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break","notes":"Signed contract amount is not Green without actual call-off and customer model survival."}
{"case_id":"r3_loop15_catl_mine_lithium_price_event","symbol":"003670/066970/006400/373220","company_name":"POSCO Future M / L&F / Samsung SDI / LGES","case_type":"event_premium","primary_archetype":"LITHIUM_PRICE_EVENT_PREMIUM","best_trigger":"T2","stage_candidate":"event_premium","price_validation":{"posco_future_m_event_mfe_pct":8.3,"lnf_event_mfe_pct":10.0,"samsung_sdi_event_mfe_pct":3.2,"lges_event_mfe_pct":2.8,"ganfeng_lithium_event_mfe_pct":21,"tianqi_lithium_event_mfe_pct":18,"lithium_price_decline_from_2022_peak_pct":-90,"catl_material_impact_claim":"no material impact","license_renewal_possible":true,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium","notes":"Lithium supply-shock rally needs durable lithium price and ASP/margin confirmation before Stage3."}
{"case_id":"r3_loop15_posco_minres_lithium_supply_security","symbol":"005490/003670","company_name":"POSCO Holdings / POSCO Future M","case_type":"success_candidate_stage2","primary_archetype":"UPSTREAM_LITHIUM_SUPPLY_STAGE2","best_trigger":"T1","stage_candidate":"Stage2_supply_security","price_validation":{"minres_deal_value_usd_mn":765,"minres_event_mfe_pct":10.8,"posco_effective_interest_wodgina_pct":15,"posco_effective_interest_mt_marion_pct":15,"spodumene_price_mid_2025_low_usd_t":610,"spodumene_price_august_2025_usd_t":880,"spodumene_2022_peak_usd_t":6000,"operator":"MinRes","posco_direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_stage2","notes":"Upstream stake improves supply security, but Stage3 requires cost advantage and downstream margin."}
{"case_id":"r3_loop15_lg_chem_toyota_tsusho_cathode_feoc","symbol":"051910","company_name":"LG Chem","case_type":"success_candidate_stage2","primary_archetype":"FEOC_CATHODE_OWNERSHIP_STAGE2","best_trigger":"T1","stage_candidate":"Stage2_regulatory_risk_reduction","price_validation":{"toyota_tsusho_new_stake_pct":25,"huayou_stake_before_pct":49,"huayou_stake_after_pct":24,"china_exposure_reduced":true,"feoc_ira_relevance":true,"direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_stage2","notes":"Ownership restructuring reduces FEOC risk but Stage3 requires customer award, IRA benefit and cathode margin."}
{"case_id":"r3_loop15_aricell_sconnect_battery_safety_hard_4c","symbol":"096630/battery_safety_basket","company_name":"S-Connect / Aricell reference","case_type":"hard_4c_reference","primary_archetype":"BATTERY_SAFETY_TRUST_HARD_4C_REFERENCE","best_trigger":"T0/T1","stage_candidate":"4C","price_validation":{"fatalities":23,"injuries":9,"lithium_batteries_stored":35000,"sconnect_event_mae_pct":-22.5,"sconnect_next_day_return_pct":-1.37,"quality_inspection_failed_before_fire":true,"temporary_unskilled_worker_factor":true,"defect_rate_increase_factor":true,"ev_fire_damaged_or_destroyed_cars":140,"mercedes_kftc_fine_krw_bn":11.2,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"hard_4c_success","notes":"Battery safety and supplier disclosure are explicit hard gates for battery/EV names."}
```

## data/e2r_trigger_calibration/triggers_r3_loop15_round226.jsonl 초안

```jsonl
{"trigger_id":"r3l15_lges_T1","case_id":"r3_loop15_lges_ampc_profit_dealrisk","trigger_type":"Stage3-Yellow_candidate","trigger_date":"2025-07-07","evidence_available":"Q2 OP 492B won, +152% YoY, above 294B consensus, shares +2.4%, but ex-AMPC OP only 1.4B won","entry_price_krw":318000,"event_return_pct":2.4,"trigger_outcome_label":"Stage3_Yellow_with_subsidy_overlay","promote_to":"Stage3-Yellow"}
{"trigger_id":"r3l15_lges_T4","case_id":"r3_loop15_lges_ampc_profit_dealrisk","trigger_type":"4C-watch","trigger_date":"2025-12-26","evidence_available":"Ford 9.6T won and Freudenberg 3.9T won cancellations, total 13.5T won expected revenue lost","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"thesis_break_watch","promote_to":"4C-watch"}
{"trigger_id":"r3l15_sdi_T2","case_id":"r3_loop15_samsung_sdi_ess_lfp_pivot","trigger_type":"Stage2-Actionable","trigger_date":"2025-12-10","evidence_available":"U.S. LFP ESS contract >2T won / $1.36B, deliveries from 2027, EV lines converted to ESS, shares +6.1% vs KOSPI -0.1%","event_return_pct":6.1,"market_relative_return_pp":6.2,"trigger_outcome_label":"Stage2_promote_candidate","promote_to":"Stage2-Actionable"}
{"trigger_id":"r3l15_skon_T2","case_id":"r3_loop15_sk_on_ford_jv_termination","trigger_type":"4C-watch","trigger_date":"2025-12-16","evidence_available":"Ford EV retreat hits Korean battery chain; SK Innovation -3%, LGES -6%, SK IE Tech -5%, EcoPro Materials -5%","event_return_pct":"SKI -3 / LGES -6 / SKIET -5 / EcoPro Materials -5","trigger_outcome_label":"thesis_break_watch","promote_to":"4C-watch"}
{"trigger_id":"r3l15_lnf_T2","case_id":"r3_loop15_lnf_tesla_cathode_contract_collapse","trigger_type":"hard_4C","trigger_date":"2025-12-29","evidence_available":"Tesla cathode supply deal cut from $2.9B to $7,386 due EV slowdown and 4680 ramp issues","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"hard_4c_success","promote_to":"4C"}
{"trigger_id":"r3l15_lithium_T2","case_id":"r3_loop15_catl_mine_lithium_price_event","trigger_type":"event_premium","trigger_date":"2025-08-11","evidence_available":"CATL Yichun mine suspended; POSCO Future M +8.3%, L&F +10%, Samsung SDI +3.2%, LGES +2.8%; CATL says no material impact","event_return_pct":"POSCO Future M +8.3 / L&F +10 / SDI +3.2 / LGES +2.8","trigger_outcome_label":"event_premium_not_stage3","promote_to":"4B-watch"}
{"trigger_id":"r3l15_posco_T1","case_id":"r3_loop15_posco_minres_lithium_supply_security","trigger_type":"Stage2_supply_security","trigger_date":"2025-11-11","evidence_available":"POSCO pays $765M for 30% of MinRes lithium JV, indirect 15% Wodgina/Mt Marion exposure, MinRes +10.8%","event_return_pct":"POSCO price unavailable / MinRes +10.8","trigger_outcome_label":"success_candidate_stage2","promote_to":"Stage2"}
{"trigger_id":"r3l15_lgchem_T1","case_id":"r3_loop15_lg_chem_toyota_tsusho_cathode_feoc","trigger_type":"Stage2_regulatory_risk_reduction","trigger_date":"2025-09-08","evidence_available":"Toyota Tsusho takes 25% stake in LG Chem cathode plant; Huayou stake falls from 49% to 24%","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"success_candidate_stage2","promote_to":"Stage2"}
{"trigger_id":"r3l15_aricell_T1","case_id":"r3_loop15_aricell_sconnect_battery_safety_hard_4c","trigger_type":"hard_4C","trigger_date":"2024-06-24","evidence_available":"Aricell fire killed 23; S-Connect -22.5%; later police blame quality failures and deadline pressure","event_return_pct":-22.5,"trigger_outcome_label":"hard_4c_success","promote_to":"4C"}
```

## data/sector_taxonomy/score_weight_profiles_round226_r3_loop15_v1.csv 초안

```csv
archetype,actual_customer_calloff,contract_cancellation_risk,ex_subsidy_operating_margin,ampc_subsidy_durability,ess_lfp_contract_quality,line_conversion_execution,customer_model_survival,battery_safety_disclosure_trust,raw_material_price_durability,feoc_ira_compliance_quality,signed_contract_amount_only_penalty,ev_growth_headline_only_penalty,subsidy_included_op_only_penalty,lithium_price_event_only_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
BATTERY_AMPC_PROFIT_STAGE2_YELLOW,+5,+5,+5,+5,+2,+2,+5,+3,+1,+3,-5,-5,-5,-3,OP beat+AMPC+relative strength,ex-AMPC margin/customer call-off pending,ex-subsidy margin+durable customer volumes,LGES AMPC beat is Yellow not Green.
ESS_LFP_PIVOT_STAGE2_ACTIONABLE,+4,+3,+3,+3,+5,+5,+4,+3,+2,+3,-4,-4,-3,-3,ESS contract+line conversion+relative strength,delivery/margin pending,delivery+repeat order+margin,Samsung SDI ESS pivot Stage2-Actionable.
EV_DEMAND_CONTRACT_CANCELLATION_4C,+5,+5,+2,+2,+3,+3,+5,+2,+2,+2,-5,-5,-3,-2,customer program cancellation or JV break,EV model survival pending,customer production schedule intact,SK On/Ford and LGES/Ford are 4C-watch patterns.
SIGNED_CATHODE_CONTRACT_COLLAPSE_HARD_4C,+5,+5,+2,+1,+0,+0,+5,+2,+2,+1,-5,-5,-2,-2,contract value collapse,call-off failure,actual shipment/revenue confirmed,L&F/Tesla is hard 4C.
LITHIUM_PRICE_EVENT_PREMIUM,+2,+2,+1,+1,+0,+0,+2,+1,+5,+1,-3,-3,-2,-5,lithium event rally,durable lithium price pending,ASP/margin confirmed,CATL mine suspension is event premium.
UPSTREAM_LITHIUM_SUPPLY_STAGE2,+3,+2,+2,+2,+0,+0,+3,+1,+5,+4,-3,-3,-2,-3,upstream stake/offtake rights,cost advantage pending,downstream margin/cost advantage,POSCO/MinRes is supply security Stage2.
FEOC_CATHODE_OWNERSHIP_STAGE2,+3,+2,+2,+3,+0,+0,+3,+2,+2,+5,-3,-3,-2,-2,China stake reduction/FEOC risk down,customer award pending,IRA benefit+margin confirmed,LG Chem/Toyota is regulatory-risk reduction Stage2.
BATTERY_SAFETY_TRUST_HARD_4C_REFERENCE,+2,+3,+1,+1,+0,+0,+2,+5,+1,+3,-2,-2,-1,-1,safety failure/disclosure issue,investigation/liability pending,safety compliance/trust restored,Aricell/S-Connect and Mercedes/Farasis are hard gate references.
```

---

# 이번 R3 Loop 15 결론

```text
1. LGES는 Stage3-Yellow지만 Green은 아니다.
   OP +152%는 강하지만 AMPC 제외 OP가 1.4B won에 불과했고, 이후 13.5T won expected revenue cancellation이 나왔다.

2. Samsung SDI는 ESS LFP pivot Stage2-Actionable이다.
   2T won / $1.36B U.S. ESS 계약과 EV line conversion은 좋은 trigger지만, delivery와 margin이 남았다.

3. SK On/Ford는 EV demand 4C-watch다.
   $11.4B JV story가 종료되고, Ford EV retreat가 한국 battery chain을 직접 때렸다.

4. L&F/Tesla는 R3 hard 4C다.
   $2.9B signed contract가 $7,386로 줄었다. 계약금액은 call-off가 아니다.

5. CATL mine suspension은 lithium event premium이다.
   POSCO Future M +8.3%, L&F +10%는 좋지만 durable lithium price와 margin이 없다.

6. POSCO/MinRes는 upstream supply-security Stage2다.
   $765M JV stake는 장기적으로 좋지만 lithium price와 downstream margin이 남아 있다.

7. LG Chem/Toyota Tsusho는 FEOC-risk reduction Stage2다.
   Huayou stake 49%→24%는 좋지만 customer award와 IRA benefit 확인 전에는 Green이 아니다.

8. Aricell/S-Connect는 battery safety hard reference다.
   배터리 업종은 수요와 계약보다 안전·품질·공시 신뢰가 먼저 깨질 수 있다.
```

한 문장으로 압축하면:

> **R3 Loop 15에서 배운 핵심은 “EV battery 성장” 자체가 아니라, actual call-off·ex-subsidy margin·ESS line conversion·customer model survival·battery safety trust가 닫혀야 Stage3로 올릴 수 있다는 것이다. 반대로 signed contract amount, lithium price event, subsidy-included OP만으로는 Green 금지다.**

[1]: https://www.ft.com/content/c8059c0c-b0a8-42dd-8b9c-2e0fb010ae13 "https://www.ft.com/content/c8059c0c-b0a8-42dd-8b9c-2e0fb010ae13"
[2]: https://www.reuters.com/business/finance/south-koreas-lg-energy-solution-ends-65-billion-ev-battery-supply-deal-with-ford-2025-12-17/ "https://www.reuters.com/business/finance/south-koreas-lg-energy-solution-ends-65-billion-ev-battery-supply-deal-with-ford-2025-12-17/"
[3]: https://www.marketwatch.com/story/samsung-sdi-s-2024-earnings-could-take-a-hit-from-sluggish-ev-battery-demand-market-talk-ceab3dde "https://www.marketwatch.com/story/samsung-sdi-s-2024-earnings-could-take-a-hit-from-sluggish-ev-battery-demand-market-talk-ceab3dde"
[4]: https://www.reuters.com/world/asia-pacific/samsung-sdis-us-unit-signs-14-bln-lfp-battery-deal-us-customer-2025-12-09/ "https://www.reuters.com/world/asia-pacific/samsung-sdis-us-unit-signs-14-bln-lfp-battery-deal-us-customer-2025-12-09/"
[5]: https://www.reuters.com/business/autos-transportation/south-koreas-sk-ford-motor-end-us-battery-joint-venture-2025-12-11/ "https://www.reuters.com/business/autos-transportation/south-koreas-sk-ford-motor-end-us-battery-joint-venture-2025-12-11/"
[6]: https://www.marketwatch.com/story/while-ford-shares-are-remarkably-steady-after-20-billion-charge-these-stocks-are-getting-battered-bbbcfa04 "https://www.marketwatch.com/story/while-ford-shares-are-remarkably-steady-after-20-billion-charge-these-stocks-are-getting-battered-bbbcfa04"
[7]: https://www.reuters.com/world/asia-pacific/south-koreas-lf-says-value-battery-material-supply-deal-with-tesla-cut-7386-2025-12-29/ "https://www.reuters.com/world/asia-pacific/south-koreas-lf-says-value-battery-material-supply-deal-with-tesla-cut-7386-2025-12-29/"
[8]: https://www.wsj.com/finance/commodities-futures/ev-battery-giant-catl-suspends-mining-project-67693725 "https://www.wsj.com/finance/commodities-futures/ev-battery-giant-catl-suspends-mining-project-67693725"
[9]: https://www.reuters.com/business/energy/australias-minres-sell-30-lithium-jv-stake-posco-765-mln-2025-11-11/ "https://www.reuters.com/business/energy/australias-minres-sell-30-lithium-jv-stake-posco-765-mln-2025-11-11/"
[10]: https://www.reuters.com/markets/emerging/lg-chem-says-japans-toyota-tsusho-acquires-25-stake-its-south-korea-cathode-2025-09-08/ "https://www.reuters.com/markets/emerging/lg-chem-says-japans-toyota-tsusho-acquires-25-stake-its-south-korea-cathode-2025-09-08/"
[11]: https://www.reuters.com/world/asia-pacific/south-korea-begins-search-answers-after-battery-plant-fire-kills-22-2024-06-25/ "https://www.reuters.com/world/asia-pacific/south-korea-begins-search-answers-after-battery-plant-fire-kills-22-2024-06-25/"
[12]: https://www.reuters.com/business/autos-transportation/south-korea-advise-automakers-disclose-battery-information-evs-2024-08-13/ "https://www.reuters.com/business/autos-transportation/south-korea-advise-automakers-disclose-battery-information-evs-2024-08-13/"

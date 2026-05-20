순서상 이번은 **R2 Loop 15 — AI·반도체·전자부품 trigger-level price validation 라운드**다.

이번 R2는 새 trigger 방식으로 본다. 핵심은 “HBM 좋다 / AI 좋다 / Nvidia 좋다”가 아니라, **어느 공개 trigger에서 진입했으면 돈이 됐고, 어느 trigger는 이미 늦었거나 4B였는지**다.

```text
round = R2 Loop 15
round_id = round_225
large_sector = AI_SEMICONDUCTOR_ELECTRONIC_PARTS
method = trigger_level_backtest_v1
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R3 Loop 15
```

제한부터 명확히 둔다. 이번 환경에서는 KRX/Naver/Yahoo/Stooq의 **수정주가 일봉 OHLC 30D/90D/180D/1Y window**를 안정적으로 직접 추출하지 못했다. Yahoo chart raw endpoint는 접근이 막혔고, `finance` tool은 KRX ticker를 안정적으로 지원하지 않았다. 그래서 이번도 full MFE/MAE는 만들지 않고, Reuters/WSJ/FT/MarketWatch/AP가 보도한 **event return, event price, YTD/annual return, earnings estimate, order value, target price, market-relative return**을 trigger anchor로 쓴다. full OHLC가 필요한 칸은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R2 = AI·반도체·전자부품
```

이번 R2의 핵심 gate는 아래다.

```text
Memory / HBM:
HBM customer qualification → shipment / mass production → HBM mix → ASP / margin → capex / capacity → forward allocation

Semiconductor equipment:
HBM packaging / bonding order → repeat order → customer concentration → capacity expansion → margin → backlog conversion

Samsung catch-up:
HBM qualification → Nvidia allocation → actual shipment timing → foundry/logic loss → labor continuity → valuation recovery

Electronic parts:
AI-device upgrade cycle → customer shipment → OP estimate beat → component ASP → sell-through → inventory

Export-control / geopolitics:
China fab exposure → U.S. equipment license → capacity upgrade block → alternative equipment → margin / competitiveness
```

---

# 2. 대상 canonical archetype

```text
HBM_FIRST_MOVER_STAGE2_TO_GREEN
HBM_EQUIPMENT_STAGE2_ACTIONABLE
HBM_CATCHUP_LATE_STAGE2
OPENAI_STARGATE_MEMORY_4B_WATCH
SEMICONDUCTOR_EXPORT_CONTROL_4C_WATCH
AI_DEVICE_COMPONENT_STAGE2_ACTIONABLE
DISPLAY_OLED_APPLE_RECOVERY_STAGE2
SEMICONDUCTOR_LABOR_SUPPLY_CHAIN_4C
```

---

# 3. deep sub-archetype

```text
SK Hynix:
- HBM3E mass production
- HBM4 internal certification
- OpenAI Stargate demand
- ASML EUV $8B order
- U.S. listing / dilution watch
- 2025 +274%, 2026 +200%+ move

Hanmi Semiconductor:
- SK Hynix HBM packaging equipment / TSV-TC bonders
- KRW21.48B supply deal
- recent wins totaling around KRW200B
- HBM equipment Stage2-Actionable

Samsung Electronics:
- HBM lag vs SK Hynix
- Nvidia HBM3E/HBM4 talks / certification
- OpenAI partnership
- labor strike 4C-watch
- foundry/logic losses vs memory rebound

LG Innotek:
- Apple Intelligence / OpenAI iPhone upgrade cycle
- OP estimate +33% vs consensus
- target +18%
- event +19%
- later demand uncertainty watch

LG Display:
- Apple OLED iPad / iPhone Pro Max orders
- operating loss beat
- revenue +42%
- profitability still uncertain

Memory export-control:
- U.S. revokes China equipment authorization
- Samsung -2.6%, SK Hynix -5%
- Hana Micron / Hanmi also affected
```

---

# 4. 선정 case 요약

| bucket                                  | case                                         | 핵심 판정                                                                                              |
| --------------------------------------- | -------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| structural_success / missed_structural  | SK Hynix                                     | HBM3E/HBM4 trigger는 Stage2가 아니라 Stage3-Yellow~Green 후보. 2025 +274%, 2026 +200%+로 Stage2 promote 강함 |
| Stage2_promote_candidate                | Hanmi Semiconductor                          | SK Hynix HBM packaging order + +16% event는 Stage2-Actionable                                       |
| Stage3-Yellow candidate / late catch-up | Samsung Electronics                          | OpenAI/Nvidia/HBM4 trigger는 Stage2-Actionable이지만 SK Hynix 대비 늦음. labor risk 4C-watch               |
| 4B-watch                                | SK Hynix OpenAI/Stargate + ASML EUV          | 수요는 진짜지만 2025~2026 급등 뒤 capex/listing/dilution overlay 필요                                          |
| 4C-watch                                | Samsung/SK Hynix China equipment restriction | Samsung -2.6%, SK Hynix -5%. China fab upgrade 제한은 4C-watch                                        |
| Stage2-Actionable                       | LG Innotek                                   | Apple AI upgrade 기대 + OP estimate 31~33% above consensus + +19% event                              |
| evidence_good_but_price_failed          | LG Display                                   | Apple OLED 수요로 loss beat, 그래도 profitability guide 불확실                                              |
| hard_4C-watch                           | Samsung labor strike                         | 18일 파업 가능성, DRAM/NAND supply impact, GDP impact 추정                                                 |

---

# 5. Case별 trigger grid

## Case A — SK Hynix / HBM first-mover cycle

```text
symbol = 000660
case_type = missed_structural / Stage2_promote_candidate / Stage3-Yellow→Green
archetype = HBM_FIRST_MOVER_STAGE2_TO_GREEN
```

### Trigger grid

| trigger | type                   |                              date | 당시 공개 evidence                                                                                    | 가격 anchor                                       | outcome                     |
| ------- | ---------------------- | --------------------------------: | ------------------------------------------------------------------------------------------------- | ----------------------------------------------- | --------------------------- |
| T0      | earliest awareness     |                        2024-03-26 | Micron AI/HBM rally 이후 한국 chip stocks 동반 rally. SK Hynix HBM3E premium, Daiwa EPS +41% forecast   | SK Hynix +4.3%, KOSPI +0.7%                     | Stage2-Actionable           |
| T1      | Stage2-Actionable      |                        2024-06-26 | HSBC 2Q OP estimate +12% to 5.2T won, HBM share 38% of DRAM revenue by end-2025, target 280,000   | shares 234,500                                  | Stage2 promote              |
| T2      | Stage3-Yellow          |                        2024-09-26 | 12-layer HBM3E mass production, 50% capacity increase vs 8-layer, supply to customers by year-end | SK Hynix +9%+, KOSPI +1.7%                      | strong Yellow               |
| T3      | Stage3-Green candidate |                        2025-01-22 | Q4 OP 8.1T won record, HBM 40% of DRAM revenue, HBM sales expected to double                      | shares -4% due legacy-memory price warning      | Green evidence, price mixed |
| T4      | Stage3-Green           |                        2025-07-23 | Q2 OP 9.2T won record, revenue +35%, HBM sales on track to double, 2026 volumes secured           | stock YTD +54.7%, but recently -9% on downgrade | Green with 4B-watch         |
| T5      | 4B-watch               | 2025-09-12 / 2025-10-02 / 2026-05 | HBM4 certification +7.3%, OpenAI deal SK Hynix +12%, 2025 +274%, 2026 +200%+                      | multiple rally anchors                          | 4B overlay                  |
| T6      | 4C-watch               |              2025-09-01 / 2026-03 | China equipment restriction -5%; U.S. listing 2~3% shares / up to $14B possible dilution          | SK Hynix -5%; listing day +1.13% vs KOSPI +1.9% | 4C/4B watch                 |

SK Hynix는 이번 R2의 핵심 `missed_structural` 후보가 아니라, 사실상 **Stage2→Stage3 승격 기준을 새로 만드는 기준 case**다. 2024년 3월 26일에는 SK Hynix +4.3%, Hanmi +16%, KOSPI +0.7%라는 HBM basket rally가 나왔고, Daiwa가 HBM3E contribution과 chip price를 이유로 2024 EPS forecast를 41% 올렸다는 보도가 있었다. 이건 단순 AI 테마가 아니라 **HBM 가격/제품 mix/earnings revision**이 붙은 Stage2-Actionable trigger다. ([월스트리트저널][1])

2024년 9월 26일에는 12-layer HBM3E mass production이 발표됐고, SK Hynix shares는 9% 이상 올랐으며 KOSPI는 1.7% 상승했다. 12-layer 제품은 기존 8-layer보다 capacity가 50% 높고, 고객 공급이 연말 예정이었다. 이 trigger는 단순 Stage2가 아니라 **Stage3-Yellow**에 가깝다. ([Reuters][2])

2025년 1월에는 Q4 OP 8.1T won record, HBM 40% of DRAM revenue, HBM sales doubling guide가 나왔지만 주가는 -4%였다. 여기서 중요한 건 “evidence는 Green인데 가격은 단기적으로 legacy-memory price warning을 더 봤다”는 점이다. 이건 `evidence_good_but_price_mixed`다. 이후 2025년 7월 Q2 OP 9.2T won, revenue +35%, HBM sales doubling, 2026 volume commitment까지 나오면서 Green에 가까워졌다. ([Reuters][3])

그리고 2025년에는 SK Hynix shares가 +274%, 2026년에는 이미 +200% 이상 오른 것으로 Reuters가 보도했다. 즉 Stage3를 2025년 record profit에만 주면 늦다. 2024년 3월~9월의 Stage2-Actionable/Yellow trigger가 실전 entry였을 가능성이 크다. ([Reuters][4])

### Trigger price validation row

```json
{
  "case_id": "r2_loop15_sk_hynix_hbm_first_mover",
  "symbol": "000660",
  "best_entry_trigger": "T1/T2",
  "best_entry_trigger_type": "Stage2-Actionable_to_Stage3-Yellow",
  "t0_date": "2024-03-26",
  "t0_event_return_pct": 4.3,
  "t0_kospi_return_pct": 0.7,
  "t0_market_relative_return_pp": 3.6,
  "t1_date": "2024-06-26",
  "t1_entry_price_anchor_krw": 234500,
  "t1_hsbc_2q_op_estimate_krw_trn": 5.2,
  "t1_hsbc_op_estimate_raise_pct": 12,
  "t1_hbm_dram_revenue_share_2025e_pct": 38,
  "t1_target_price_krw": 280000,
  "t2_date": "2024-09-26",
  "t2_event_return_pct": 9.0,
  "t2_kospi_return_pct": 1.7,
  "t2_market_relative_return_pp": 7.3,
  "t2_hbm3e_12_layer_capacity_increase_pct": 50,
  "t3_date": "2025-01-22",
  "t3_q4_op_krw_trn": 8.1,
  "t3_hbm_share_dram_revenue_pct": 40,
  "t3_event_return_pct": -4.0,
  "t4_date": "2025-07-23",
  "t4_q2_op_krw_trn": 9.2,
  "t4_revenue_yoy_pct": 35,
  "t4_ytd_gain_pct": 54.7,
  "forward_return_anchor_2025_pct": 274,
  "forward_return_anchor_2026_ytd_pct": 200,
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "missed_structural_if_stage3_waited_until_record_profit",
  "stage_gate_correction": "HBM product qualification + OP estimate raise + HBM mix + relative strength should promote Stage2 to Stage3-Yellow"
}
```

### 판정

```text
score_price_alignment = missed_structural_if_old_gate_used
old_label = Stage 2 / success_candidate
new_label = Stage2-Actionable → Stage3-Yellow → Stage3-Green
key_rule = HBM mix + OP estimate 상향 + mass production + 상대강도는 Stage3-Yellow 승격
```

---

## Case B — Hanmi Semiconductor / HBM packaging equipment

```text
symbol = 042700
case_type = Stage2_promote_candidate
archetype = HBM_EQUIPMENT_STAGE2_ACTIONABLE
```

### Trigger grid

| trigger | type                    |       date | 당시 공개 evidence                                                                                                                     | 가격 anchor               | outcome           |
| ------- | ----------------------- | ---------: | ---------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | ----------------- |
| T0      | awareness               |    2024-03 | HBM packaging / TSV-TC bonder supplier to SK Hynix                                                                                 | sector rally            | watch             |
| T1      | Stage2 evidence         | 2024-03-26 | Hanmi supplies SK Hynix with HBM packaging equipment; KRW21.48B SK Hynix supply deal; recent contract wins totaling around KRW200B | Hanmi +16%, KOSPI +0.7% | Stage2-Actionable |
| T2      | Stage3-Yellow candidate | 2024-03-26 | HBM U.S. demand and SK Hynix/TSMC/Nvidia supply-chain localization opportunity                                                     | same event              | Yellow candidate  |
| T3      | 4B-watch                |    2024 이후 | HBM equipment pure-play concentration / 고객 concentration / 주가 급등 risk                                                              | full OHLC unavailable   | 4B watch          |
| T4      | 4C-watch                | 2025-09-01 | U.S. China-equipment restriction day, related firms incl. Hanmi fell                                                               | event price unavailable | geopolitics watch |

Hanmi Semiconductor는 R2에서 **Stage2-Actionable의 모범**이다. 2024년 3월 26일에는 Hanmi shares가 +16%였고, SK Hynix는 +4.3%, KOSPI는 +0.7%였다. 보도는 Hanmi가 SK Hynix에 advanced HBM packaging equipment인 TSV-TC bonders를 공급하고, 최근 SK Hynix와 KRW21.48B supply deal 및 총 KRW200B 규모 최근 contract wins가 있었다고 설명했다. 이건 단순 “AI 테마”가 아니라 **고객·장비·계약·수급 상대강도**가 닫힌 trigger다. ([월스트리트저널][1])

### Trigger price validation row

```json
{
  "case_id": "r2_loop15_hanmi_semiconductor_hbm_equipment",
  "symbol": "042700",
  "best_entry_trigger": "T1",
  "best_entry_trigger_type": "Stage2-Actionable",
  "trigger_date": "2024-03-26",
  "event_return_pct": 16,
  "kospi_return_pct": 0.7,
  "market_relative_return_pp": 15.3,
  "sk_hynix_same_day_return_pct": 4.3,
  "specific_customer": "SK Hynix",
  "specific_equipment": "TSV-TC bonders / HBM packaging equipment",
  "sk_hynix_supply_deal_krw_bn": 21.48,
  "recent_contract_wins_krw_bn": 200,
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_promote_candidate",
  "stage_gate_correction": "specific HBM equipment + named customer order + repeated wins + +15pp relative strength should be Stage2-Actionable"
}
```

### 판정

```text
score_price_alignment = Stage2_promote_candidate
old_label = Stage 2
new_label = Stage2-Actionable
reason = HBM equipment의 고객·계약·장비명이 구체적이고 event relative strength가 매우 큼
```

---

## Case C — Samsung Electronics / HBM catch-up and labor 4C

```text
symbol = 005930
case_type = Stage2-Actionable / 4C-watch
archetype = HBM_CATCHUP_LATE_STAGE2
```

### Trigger grid

| trigger | type              |                           date | 당시 공개 evidence                                                                                                         | 가격 anchor                                                         | outcome                       |
| ------- | ----------------- | -----------------------------: | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------- |
| T0      | awareness         |                      2024~2025 | Samsung lagging SK Hynix in HBM                                                                                        | mixed                                                             | weak watch                    |
| T1      | 4C-watch          |                        2025-Q2 | semiconductor profit hit by delayed Nvidia memory shipments and China controls                                         | chip division slump                                               | thesis watch                  |
| T2      | Stage2 evidence   |                     2025-10-02 | OpenAI partnership, memory procurement demand                                                                          | Samsung +4.7%, SK Hynix +12%, KOSPI +3%                           | Stage2-Actionable but lagging |
| T3      | Stage2-Actionable |                     2025-10-31 | Nvidia acknowledged Samsung HBM3E/HBM4 partnership, Samsung in talks for HBM4, 12-layer HBM3E to all related customers | Samsung +4%+                                                      | catch-up Yellow candidate     |
| T4      | Stage3-Yellow     |                        2025-Q3 | Q3 OP +32.5% to 12.2T won, revenue 86T won, semiconductor OP 7T won, mass-producing HBM3E / HBM4 samples               | price unavailable                                                 | Yellow                        |
| T5      | 4B/4C-watch       |                        2026-05 | 18-day strike risk, 48k workers, DRAM 3~4% / NAND 2~3% supply impact estimate                                          | Samsung rose slightly after court injunction; strike risk remains | labor 4C-watch                |
| T6      | hard 4C           | strike execution severe impact | not yet confirmed                                                                                                      | pending                                                           |                               |

Samsung은 SK Hynix와 다르게 **late catch-up** case다. OpenAI partnership day에 Samsung +4.7%, SK Hynix +12%로, 같은 AI-memory demand trigger에서도 상대강도는 SK Hynix가 훨씬 강했다. 이건 Samsung trigger를 Stage3-Green으로 올리기 어렵다는 신호다. ([Reuters][5])

2025년 10월 31일에는 Samsung이 Nvidia와 HBM4 supply talks를 하고 있고, Nvidia가 Samsung의 HBM3E/HBM4 partnership을 인정했다는 Reuters 보도가 나왔다. Samsung stock은 4% 이상 상승했다. 다만 Reuters는 SK Hynix가 여전히 Nvidia의 primary HBM partner라고도 설명했다. 따라서 이 trigger는 `Stage2-Actionable` 또는 `Stage3-Yellow candidate`이지 Green은 아니다. ([Reuters][6])

또한 2026년 5월에는 Samsung union strike risk가 R2의 hard watch가 됐다. Reuters는 48,000명 규모의 18일 파업 가능성과 DRAM 3~4%, NAND 2~3% supply impact, 정부의 GDP 0.5%p 영향 우려를 보도했다. 이는 AI memory upcycle 안에서도 **labor continuity가 4C overlay**가 된다는 뜻이다. ([Reuters][7])

### Trigger price validation row

```json
{
  "case_id": "r2_loop15_samsung_electronics_hbm_catchup_labor_watch",
  "symbol": "005930",
  "best_entry_trigger": "T2/T3",
  "best_entry_trigger_type": "Stage2-Actionable_to_Stage3-Yellow_candidate",
  "t2_date": "2025-10-02",
  "t2_event_return_pct": 4.7,
  "t2_sk_hynix_return_pct": 12,
  "t2_kospi_return_pct": 3,
  "relative_to_sk_hynix_pp": -7.3,
  "t3_date": "2025-10-31",
  "t3_event_return_pct": 4.0,
  "nvidia_partnership_acknowledged": true,
  "hbm3e_supply_to_related_customers": true,
  "hbm4_talks_confirmed": true,
  "sk_hynix_primary_partner_still": true,
  "q3_2025_op_krw_trn": 12.2,
  "q3_2025_op_growth_pct": 32.5,
  "q3_2025_revenue_krw_trn": 86,
  "semiconductor_division_op_krw_trn": 7,
  "labor_strike_workers_context": 48000,
  "potential_dram_supply_impact_pct": "3-4",
  "potential_nand_supply_impact_pct": "2-3",
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "late_catchup_stage2_actionable_with_labor_4c_watch",
  "stage_gate_correction": "Samsung catch-up triggers need relative-strength discount vs SK Hynix and labor continuity overlay"
}
```

### 판정

```text
score_price_alignment = Stage2-Actionable_but_not_Green
reason = OpenAI/Nvidia trigger는 강하지만 SK Hynix 대비 late catch-up이고 labor 4C overlay 존재
```

---

## Case D — SK Hynix / OpenAI Stargate + ASML EUV capex

```text
symbol = 000660
case_type = Stage3-Green + 4B-watch
archetype = OPENAI_STARGATE_MEMORY_4B_WATCH
```

### Trigger grid

| trigger | type          |       date | 당시 공개 evidence                                                                                        | 가격 anchor                               | outcome                 |
| ------- | ------------- | ---------: | ----------------------------------------------------------------------------------------------------- | --------------------------------------- | ----------------------- |
| T1      | Stage3-Yellow | 2025-10-02 | OpenAI Stargate LOI, $500B AI infra project, DRAM wafer demand up to 900k/month                       | SK Hynix +12%, Samsung +4.7%, KOSPI +3% | strong trigger          |
| T2      | Stage3-Green  | 2026-05-04 | U.S. hyperscalers signal >$700B AI capex, memory prices rising, SK Hynix +13% to record 1,447,000 won | +13%, KOSPI +5.1%                       | Green but 4B            |
| T3      | 4B-watch      | 2026-03-24 | $7.97B ASML EUV order, 11.95T won, largest disclosed ASML customer order, about 30 EUV machines       | SK Hynix +5.7%                          | capex/valuation overlay |
| T4      | 4B-watch      | 2026-03-24 | possible U.S. listing 2~3% shares, up to $14.4B                                                       | shares +1.13% vs KOSPI +1.9%            | dilution watch          |
| T5      | 4C-watch      |    2026-05 | strike spillover from Samsung might benefit SK short-term, but systemic supply-chain risk             | no hard break                           | watch                   |

OpenAI/Stargate trigger는 SK Hynix의 Stage3-Green 성격을 강화했지만, 동시에 4B를 띄운다. 2025년 10월 2일 Reuters는 Samsung +4.7%, SK Hynix +12%, KOSPI +3%를 보도했다. OpenAI의 $500B Stargate project와 한국 data centers, HBM demand 완화 논리가 같이 붙었다. ([Reuters][5])

2026년 5월 4일에는 hyperscaler AI capex가 $700B+로 커졌다는 신호에 SK Hynix가 +13%로 1,447,000 won record high를 찍었다. KOSPI도 +5.1%였다. 이건 Green에 가까운 수요 confirmation이지만, 동시에 주가가 이미 2025년 +274%, 2026년 +200% 이상 오른 상태라 4B overlay가 필요하다. ([Reuters][8])

또한 2026년 3월 SK Hynix는 ASML EUV tools를 11.95T won, $7.97B 규모로 사기로 했고, Reuters는 이것이 공개된 ASML 고객 order 중 최대 규모라고 보도했다. 주가는 +5.7%였지만, capex와 U.S. listing/dilution watch를 같이 봐야 한다. ([Reuters][9])

### Trigger price validation row

```json
{
  "case_id": "r2_loop15_sk_hynix_openai_asml_4b",
  "symbol": "000660",
  "best_entry_trigger": "T1_before_full_4B",
  "stage_candidate": "Stage3-Green + 4B-watch",
  "t1_date": "2025-10-02",
  "t1_event_return_pct": 12,
  "t1_samsung_return_pct": 4.7,
  "t1_kospi_return_pct": 3,
  "openai_stargate_project_usd_bn": 500,
  "t2_date": "2026-05-04",
  "t2_event_return_pct": 13,
  "t2_event_price_krw": 1447000,
  "t2_kospi_return_pct": 5.1,
  "ai_capex_2026_usd_bn": 700,
  "t3_asml_order_krw_trn": 11.95,
  "t3_asml_order_usd_bn": 7.97,
  "t3_event_return_pct": 5.7,
  "t3_estimated_euv_machines": 30,
  "t4_us_listing_possible_raise_usd_bn": "9.6-14.4",
  "t4_possible_share_issuance_pct": "2-3",
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage3_Green_with_4B_overlay",
  "stage_gate_correction": "OpenAI/capex confirmation validates demand, but after +274%/+200% rally requires 4B sizing overlay"
}
```

### 판정

```text
score_price_alignment = aligned_if_Stage3_plus_4B_overlay_allowed
new_rule = demand confirmation과 valuation/capex/dilution watch를 동시에 기록
```

---

## Case E — Samsung/SK Hynix China equipment restriction

```text
symbols = 005930 / 000660 / 042700 / 067310
company_scope = Samsung Electronics / SK Hynix / Hanmi Semiconductor / Hana Micron
case_type = 4C-watch
archetype = SEMICONDUCTOR_EXPORT_CONTROL_4C_WATCH
```

### Trigger grid

| trigger | type          |       date | 당시 공개 evidence                                                | 가격 anchor                   | outcome               |
| ------- | ------------- | ---------: | ------------------------------------------------------------- | --------------------------- | --------------------- |
| T1      | 4C-watch      | 2025-09-01 | U.S. revokes VEU authorization for China fabs, 120-day expiry | Samsung -2.6%, SK Hynix -5% | 4C-watch              |
| T2      | Stage2 relief | 2025-09-01 | short-term impact may be limited; new capacity focus in Korea | same source                 | partial relief        |
| T3      | 4C spread     | 2025-09-01 | related firms incl. Hana Micron and Hanmi Semiconductor fell  | price unavailable           | supply-chain watch    |
| T4      | hard 4C       |        N/A | license denial / production disruption not confirmed          | N/A                         | hard_4c_not_confirmed |

이 case는 R2에서 **지정학·export-control 4C-watch**다. Reuters는 미국이 Samsung/SK Hynix의 중국 fab에 대한 U.S. semiconductor equipment purchase authorization을 철회했고, SK Hynix shares -5%, Samsung -2.6%를 보도했다. SK Hynix는 memory output의 30~40%를 중국에서 만들고, Samsung은 NAND의 약 1/3이 중국 생산 기반이라고 설명됐다. 다만 단기 영향은 제한적일 수 있다는 analyst view도 있었다. ([Reuters][10])

### Trigger price validation row

```json
{
  "case_id": "r2_loop15_memory_china_equipment_export_control",
  "symbols": "005930/000660/042700/067310",
  "trigger_date": "2025-09-01",
  "trigger_type": "4C-watch",
  "samsung_event_mae_pct": -2.6,
  "sk_hynix_event_mae_pct": -5.0,
  "license_expiry_days": 120,
  "sk_hynix_china_memory_output_share_pct": "30-40",
  "samsung_china_nand_output_share_pct": "about_one_third",
  "related_firms_affected": ["Hana Micron", "Hanmi Semiconductor"],
  "short_term_impact_limited_view": true,
  "hard_4c_confirmed": false,
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "thesis_break_watch",
  "stage_gate_correction": "China fab exposure and equipment-license status must be explicit 4C overlay even in AI memory upcycle"
}
```

### 판정

```text
score_price_alignment = thesis_break_watch
reason = AI memory thesis 자체는 유지되지만 중국 fab upgrade / equipment access가 4C overlay
```

---

## Case F — LG Innotek / Apple AI iPhone upgrade cycle

```text
symbol = 011070
case_type = Stage2-Actionable
archetype = AI_DEVICE_COMPONENT_STAGE2_ACTIONABLE
```

### Trigger grid

| trigger | type              |       date | 당시 공개 evidence                                                                    | 가격 anchor                                 | outcome                   |
| ------- | ----------------- | ---------: | --------------------------------------------------------------------------------- | ----------------------------------------- | ------------------------- |
| T0      | awareness         | 2024-06-10 | Apple Intelligence / OpenAI deal                                                  | Apple +7% overnight                       | external trigger          |
| T1      | Stage2 evidence   | 2024-06-12 | LG Innotek as iPhone camera/parts supplier, AI upgrade cycle expectation          | LG Innotek +19%, 272,000 won, KOSPI +0.4% | Stage2-Actionable         |
| T2      | Stage2-Actionable | 2024-06-27 | 2Q OP estimate 106.4B won, 31% above consensus 81.1B; target 330,000 from 280,000 | shares -0.4%, 272,000 won                 | evidence good, price flat |
| T3      | Stage3-Yellow     | 2024-Q3/Q4 | actual iPhone 16 sell-through required                                            | not available                             | pending                   |
| T4      | 4C-watch          |    2024-11 | IDC: iOS growth only 0.4%, AI not yet driving upgrade significantly               | Apple -0.3%; LG unavailable               | demand watch              |

LG Innotek은 R2 전자부품에서 **Stage2-Actionable**이다. 2024년 6월 12일 WSJ는 Apple이 OpenAI와 AI integration을 발표한 뒤 LG Innotek이 장중 +19%로 272,000 won까지 올랐고, KOSPI +0.4%를 크게 이겼다고 보도했다. Daishin은 AI iPhone upgrade cycle이 LG Innotek camera module demand를 끌어올릴 수 있고, 2024 OP가 1.110T won으로 33% 증가할 수 있다고 봤다. ([월스트리트저널][11])

6월 27일에는 Mirae가 2Q OP estimate를 106.4B won으로 제시했는데, consensus 81.1B won 대비 31% 높았고 target을 330,000 won으로 올렸다. 다만 당일 주가는 -0.4%였다. 그래서 T1은 가격이 강한 Stage2-Actionable이고, T2는 evidence는 좋지만 immediate price는 약한 trigger다. ([마켓워치][12])

### Trigger price validation row

```json
{
  "case_id": "r2_loop15_lg_innotek_apple_ai_upgrade",
  "symbol": "011070",
  "best_entry_trigger": "T1",
  "best_entry_trigger_type": "Stage2-Actionable",
  "t1_date": "2024-06-12",
  "t1_entry_price_anchor_krw": 272000,
  "t1_event_return_pct": 19,
  "t1_kospi_return_pct": 0.4,
  "t1_market_relative_return_pp": 18.6,
  "op_2024_forecast_krw_trn": 1.110,
  "op_2024_forecast_growth_pct": 33,
  "t2_date": "2024-06-27",
  "t2_op_estimate_krw_bn": 106.4,
  "t2_consensus_op_krw_bn": 81.1,
  "t2_op_estimate_vs_consensus_pct": 31.2,
  "t2_target_before_krw": 280000,
  "t2_target_after_krw": 330000,
  "t2_event_return_pct": -0.4,
  "stage3_gate_missing": ["actual_iPhone16_sellthrough", "camera_module_ASP", "inventory", "Apple_AI_upgrade_conversion"],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_Actionable_but_needs_sellthrough_validation"
}
```

### 판정

```text
score_price_alignment = Stage2_promote_candidate
reason = AI device cycle + OP estimate beat + +19% relative strength는 Stage2-Actionable
```

---

## Case G — LG Display / Apple OLED recovery

```text
symbol = 034220
case_type = evidence_good_but_price_incomplete
archetype = DISPLAY_OLED_APPLE_RECOVERY_STAGE2
```

### Trigger grid

| trigger | type                        |       date | 당시 공개 evidence                                                                                               | 가격 anchor         | outcome   |
| ------- | --------------------------- | ---------: | ------------------------------------------------------------------------------------------------------------ | ----------------- | --------- |
| T1      | Stage2 evidence             | 2024-07-25 | Q2 operating loss 94B vs expected 308B loss, revenue +42% to 6.7T, Apple OLED iPad and iPhone Pro Max orders | price unavailable | Stage2    |
| T2      | Stage2-Actionable candidate | 2024-07-25 | six consecutive losses ended previously, Apple OLED order timing helped                                      | no price          | candidate |
| T3      | 4C-watch                    | 2024-07-25 | company declined to guide 2H profitability due market volatility                                             | no price          | watch     |
| T4      | Stage3-Yellow               |        N/A | sustained profitability not confirmed                                                                        | N/A               | no Yellow |

LG Display는 evidence는 좋지만 Stage3로 올리기는 어렵다. Reuters는 Q2 operating loss가 94B won으로, expected 308B won loss보다 훨씬 좋았고 revenue는 42% 증가해 6.7T won이었다고 보도했다. Apple OLED iPad와 iPhone Pro Max order가 도움을 줬지만, 회사는 2H 흑자 전환 가능성에 대해 demand uncertainty를 이유로 말을 아꼈다. ([Reuters][13])

### Trigger price validation row

```json
{
  "case_id": "r2_loop15_lg_display_apple_oled_recovery",
  "symbol": "034220",
  "best_entry_trigger": "T1_pending_price",
  "trigger_date": "2024-07-25",
  "q2_operating_loss_krw_bn": 94,
  "expected_q2_loss_krw_bn": 308,
  "loss_beat_amount_krw_bn": 214,
  "prior_year_loss_krw_bn": 881,
  "revenue_krw_trn": 6.7,
  "revenue_growth_pct": 42,
  "apple_oled_ipad_orders": true,
  "iphone_pro_max_16_oled_orders": true,
  "second_half_profitability_guidance_refused": true,
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "evidence_good_but_price_data_incomplete",
  "stage_gate_correction": "loss beat and Apple OLED orders are Stage2, but no Green without sustained profitability"
}
```

### 판정

```text
score_price_alignment = evidence_good_but_price_data_incomplete
reason = loss beat는 좋지만 profitability guide 부재로 Yellow 이상 보류
```

---

## Case H — Samsung labor strike risk

```text
symbol = 005930
case_type = 4C-watch
archetype = SEMICONDUCTOR_LABOR_SUPPLY_CHAIN_4C
```

### Trigger grid

| trigger | type           |                             date | 당시 공개 evidence                                                     | 가격 anchor         | outcome      |
| ------- | -------------- | -------------------------------: | ------------------------------------------------------------------ | ----------------- | ------------ |
| T1      | 4C-watch       |                       2026-05-12 | Samsung union talks fail, strike risk from May 21                  | price unavailable | watch        |
| T2      | 4C-watch       |                       2026-05-19 | 48,000 workers, 18-day strike, bonus dispute, government mediation | no hard price     | watch        |
| T3      | partial relief |                       2026-05-19 | talks narrow some differences                                      | no price          | relief watch |
| T4      | hard 4C        | if strike starts/disrupts supply | not yet confirmed                                                  | N/A               | pending      |

Samsung labor risk는 R2에서 **기업 내부 이슈가 아니라 AI memory supply-chain 4C**다. Reuters는 nearly 48,000 workers가 18-day strike를 계획했고, union demand는 bonus cap 제거와 annual operating profit의 15%를 bonus pool로 배정하는 것이며, strike가 global DRAM 3~4%, NAND 2~3% supply에 영향을 줄 수 있다고 보도했다. ([Reuters][7])

### Trigger price validation row

```json
{
  "case_id": "r2_loop15_samsung_labor_supply_chain_4c",
  "symbol": "005930",
  "trigger_date": "2026-05-19",
  "trigger_type": "4C-watch",
  "strike_workers_count": 48000,
  "strike_days": 18,
  "union_profit_share_demand_pct": 15,
  "potential_dram_supply_impact_pct": "3-4",
  "potential_nand_supply_impact_pct": "2-3",
  "government_gdp_impact_estimate_pp": 0.5,
  "hard_4c_confirmed": false,
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "thesis_break_watch",
  "stage_gate_correction": "memory upcycle scoring must include labor continuity and production continuity overlay"
}
```

### 판정

```text
score_price_alignment = thesis_break_watch
reason = AI memory upcycle 안에서도 생산연속성/노동리스크가 4C overlay
```

---

# 6. Trigger별 가격경로 검증 요약

| case                 | best trigger       |            entry anchor |                event MFE/MAE |       market-relative | full MFE/MAE | outcome                           |
| -------------------- | ------------------ | ----------------------: | ---------------------------: | --------------------: | ------------ | --------------------------------- |
| SK Hynix HBM         | T1/T2 2024-06~09   |         234,500 / event | +9% on HBM3E mass production |                +7.3pp | unavailable  | missed_structural / Stage3-Yellow |
| Hanmi Semiconductor  | T1 2024-03-26      |             unavailable |                         +16% |               +15.3pp | unavailable  | Stage2-Actionable                 |
| Samsung HBM catch-up | T2/T3 2025-10      |                   event |                   +4.7%, +4% |  weaker than SK Hynix | unavailable  | late Stage2-Actionable            |
| SK Hynix OpenAI/ASML | T1/T2/T3 2025~2026 | 1,447,000 on 2026-05-04 |            +12%, +13%, +5.7% | +9pp / +7.9pp / mixed | unavailable  | Stage3-Green + 4B                 |
| Export-control       | T1 2025-09-01      |                   event |  Samsung -2.6%, SK Hynix -5% |           unavailable | unavailable  | 4C-watch                          |
| LG Innotek           | T1 2024-06-12      |                 272,000 |                         +19% |               +18.6pp | unavailable  | Stage2-Actionable                 |
| LG Display           | T1 2024-07-25      |                no price |                    loss beat |           unavailable | unavailable  | evidence good, price incomplete   |
| Samsung labor        | T1/T2 2026-05      |                no price |                  strike risk |           unavailable | unavailable  | 4C-watch                          |

---

# 7. Case별 trigger 비교

## 가장 좋은 entry 후보

```text
1. SK Hynix T1/T2:
   OP estimate 상향 + HBM mix + mass production + 상대강도.
   기존 Stage2로 두면 miss.

2. Hanmi Semiconductor T1:
   HBM 장비 고객/계약/장비명/반복수주 + +16%.
   Stage2-Actionable 확정 후보.

3. LG Innotek T1:
   Apple AI upgrade + OP growth forecast + +19%.
   전자부품 Stage2-Actionable.

4. SK Hynix OpenAI T1:
   수요가 이미 검증된 상태에서는 Stage3-Green이지만, 4B overlay 필요.
```

## 기존 점수표가 놓쳤을 가능성

```text
missed_structural:
- SK Hynix HBM cycle
- Hanmi Semiconductor HBM equipment
- LG Innotek Apple AI component cycle

기존 점수표가 “HBM 좋다”를 Stage2로만 두면,
실제 entry였던 OP estimate / HBM mass production / equipment order / 상대강도 trigger를 놓친다.
```

## late trigger

```text
Samsung Electronics:
OpenAI/Nvidia/HBM4 catch-up trigger는 강하지만 SK Hynix 대비 late.
Stage3-Green이 아니라 Stage2-Actionable 또는 Yellow 후보.
```

## 4B/4C overlay

```text
SK Hynix:
2025 +274%, 2026 +200%+ 이후 OpenAI/ASML/capex/listing은 Green이면서 4B.

Samsung/SK China restriction:
AI memory thesis 유지라도 China fab exposure는 4C-watch.

Samsung labor:
labor continuity는 AI memory upcycle 위에 얹히는 4C overlay.
```

---

# 8. score-price alignment 판정

```text
aligned:
- SK Hynix, if Stage2-Actionable→Stage3-Yellow→Green ladder is allowed.

missed_structural:
- SK Hynix HBM first-mover.
- Hanmi Semiconductor HBM equipment.
- LG Innotek Apple AI upgrade.

Stage2_promote_candidate:
- SK Hynix 2024-03/06/09 triggers.
- Hanmi 2024-03-26.
- LG Innotek 2024-06-12.
- Samsung 2025-10 catch-up, but weaker.

evidence_good_but_price_failed:
- SK Hynix 2025-01 record Q4 profit day: evidence good, price -4%.
- LS Electric-style issue repeated: immediate price failure does not always invalidate structural trigger.
- LG Display price incomplete.

event_premium:
- OpenAI/Stargate +12% SK Hynix, +4.7% Samsung.
- Apple/OpenAI LG Innotek +19%.

4B-watch:
- SK Hynix after 2025/2026 huge rally.
- SK Hynix ASML EUV capex / U.S. listing dilution.
- OpenAI/Stargate if scored after parabolic move.

thesis_break_watch:
- China equipment restriction.
- Samsung labor strike.
```

---

# 9. 점수비중 교정

## 올릴 축

```text
hbm_mix_revenue_share +5
op_estimate_revision_vs_consensus +5
mass_production_or_customer_qualification +5
named_customer_equipment_order +5
repeat_order_backlog_quality +4
relative_strength_on_evidence_day +5
ai_capex_customer_commitment +4
device_upgrade_op_estimate +4
```

### 근거

SK Hynix의 HBM cycle은 OP estimate revision, HBM mix, mass production trigger에서 이미 entry가 나왔다. Hanmi는 named customer + HBM equipment + repeat order + +16% relative strength가 Stage2-Actionable이었다. LG Innotek은 Apple AI trigger와 OP estimate beat가 같은 구조다.

## 내릴 축

```text
ai_theme_only -5
customer_name_without_allocation -4
target_price_raise_without_price_strength -3
late_catchup_without_relative_strength -4
capex_without_ROIC_or_dilution_check -4
openai_or_nvidia_headline_after_parabolic_rally -4
```

### 근거

Samsung은 OpenAI/Nvidia/HBM4 trigger가 강하지만 SK Hynix 대비 late catch-up이다. SK Hynix도 OpenAI/Stargate/ASML trigger는 demand validation이지만, 이미 parabolic move 후에는 4B overlay가 필요하다. LG Display는 Apple OLED order만으로 Green을 줄 수 없다.

---

# 10. Stage 2-Actionable 승격 조건

R2 Loop 15 shadow rule:

```text
반도체/전자부품에서 Stage 2 evidence가 아래 중 3개 이상을 충족하면 Stage2-Actionable로 승격한다.

1. HBM mix / AI-related revenue share / OP estimate가 숫자로 제시됨
2. 고객 또는 제품명이 구체적임: Nvidia, SK Hynix, Apple, OpenAI 등
3. mass production, certification, shipment, supply deal 중 하나가 확인됨
4. trigger 당일 market-relative +5pp 이상
5. target price / OP estimate가 consensus 대비 20% 이상 상향
6. 반복 order 또는 capacity allocation이 확인됨
```

적용 case:

```text
SK Hynix 2024-06/09
Hanmi Semiconductor 2024-03
LG Innotek 2024-06
Samsung Electronics 2025-10, 단 relative-strength discount 적용
```

---

# 11. Stage 3-Yellow 조건

```text
Stage3-Yellow:
- mass production 또는 customer qualification이 확인됨
- OP/EPS 또는 HBM mix가 숫자로 개선됨
- trigger 당일 상대강도가 강함
- 하지만 forward allocation, margin sustainability, capacity/capex, customer concentration 중 하나가 남아 있음
```

이번 라운드 후보:

```text
SK Hynix:
HBM3E 12-layer mass production + +9% + HBM mix.

Hanmi Semiconductor:
HBM packaging equipment order + +16%, 단 고객 concentration 때문에 Yellow까진 보수적.

LG Innotek:
AI iPhone upgrade + OP estimate + +19%, 단 sell-through gate 남음.

Samsung:
HBM3E/HBM4 catch-up + +4%, 단 SK Hynix 대비 late.
```

---

# 12. Stage 3-Green 조건

```text
Stage3-Green:
- HBM / AI component revenue가 실제 실적에서 크게 확인됨
- OP가 consensus 대비 강하게 beat하거나 record profit
- 제품이 mass production/qualification 후 실제 고객 매출로 이어짐
- full-window MFE/MAE가 우호적
```

이번 라운드 Green에 가장 가까운 case:

```text
SK Hynix:
Q2 2025 OP 9.2T, revenue +35%, HBM sales doubling, 2026 volume commitments.
다만 4B overlay 필요.
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- 1년 +200% 이상 또는 2년 누적 급등 뒤 신규 demand headline 발생
- OpenAI/Nvidia headline 이후 valuation이 이미 parabolic
- 대규모 capex / listing / dilution 가능성 등장
- consensus가 너무 빠르게 상향되고 downgrade가 나오기 시작
- customer concentration이 높고 single customer allocation 변화에 취약
```

적용:

```text
SK Hynix:
2025 +274%, 2026 +200%+.
OpenAI/Stargate, ASML EUV, U.S. listing은 Green evidence이면서 4B overlay.

Hanmi:
HBM equipment pure-play라 고객 concentration 4B-watch.

Samsung:
late catch-up인데 labor risk까지 있으면 4B보다 4C-watch.
```

---

# 14. 4C hard gate 조건

```text
4C:
- HBM qualification failure
- customer allocation loss
- actual shipment delay
- China fab equipment/license restriction that blocks upgrade
- major labor strike disrupting memory supply
- capex/dilution that changes EPS path
- AI capex slowdown by hyperscalers
```

이번 R2 Loop 15에서 hard 4C는 확정하지 않는다.

```text
hard_4c_not_confirmed = true
```

하지만 strong 4C-watch는 있다.

```text
Samsung/SK Hynix China equipment restriction
Samsung labor strike
Samsung HBM catch-up delay / Nvidia allocation uncertainty
SK Hynix U.S. listing dilution risk
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_225.md 요약

```md
# R2 Loop 15. AI / Semiconductor / Electronic Parts Trigger-level Price Validation

이번 라운드는 R2 Loop 15 trigger-level validation 라운드다.

핵심 결론:
- SK Hynix is the key missed_structural / Stage2-promote case. March 2024 AI/HBM rally, June OP estimate revision, and September 12-layer HBM3E mass production should not remain plain Stage 2. The September trigger produced a 9%+ move vs KOSPI +1.7%. Reuters later reported SK Hynix rose 274% in 2025 and more than 200% in 2026, proving the old Stage 3 gate would have been too late.
- Hanmi Semiconductor is Stage2-Actionable. On 2024-03-26, Hanmi +16% vs KOSPI +0.7% after SK Hynix HBM packaging equipment and KRW21.48B supply deal evidence, with recent contract wins around KRW200B.
- Samsung Electronics is late Stage2-Actionable, not Green. OpenAI partnership day Samsung +4.7% while SK Hynix +12%. Nvidia HBM3E/HBM4 talks produced a 4%+ move, but SK Hynix remains primary HBM partner. Labor strike risk is 4C-watch.
- SK Hynix OpenAI/Stargate and ASML EUV triggers validate demand but require 4B overlay. OpenAI day SK Hynix +12%; 2026 hyperscaler capex day +13% to 1,447,000 won; ASML EUV order worth 11.95T won / $7.97B produced +5.7%. After 2025 +274% and 2026 +200%+, this is Stage3-Green + 4B.
- China equipment restriction is semiconductor export-control 4C-watch. Samsung -2.6%, SK Hynix -5% after U.S. revoked authorizations for China fabs. SK Hynix produces 30~40% of memory output in China; Samsung has about one-third NAND exposure.
- LG Innotek is AI-device Stage2-Actionable. Apple/OpenAI trigger gave LG Innotek +19% to 272,000 won vs KOSPI +0.4%; later 2Q OP estimate 106.4B won was 31% above consensus.
- LG Display is Stage2 evidence but price incomplete. Q2 operating loss was 94B won vs expected 308B loss and revenue +42% to 6.7T, helped by Apple OLED orders, but company declined 2H profit guidance.
- Samsung labor strike is R2 4C-watch. Nearly 48,000 workers, 18-day strike risk, possible DRAM supply impact 3~4% and NAND 2~3%.

Main calibration:
- Raise hbm_mix_revenue_share, op_estimate_revision_vs_consensus, mass_production_or_customer_qualification, named_customer_equipment_order, repeat_order_backlog_quality, relative_strength_on_evidence_day, ai_capex_customer_commitment, device_upgrade_op_estimate.
- Lower ai_theme_only, customer_name_without_allocation, target_price_raise_without_price_strength, late_catchup_without_relative_strength, capex_without_ROIC_or_dilution_check, OpenAI/Nvidia headline after parabolic rally.
```

## docs/checkpoints/checkpoint_28a_round225_r2_loop15.md 요약

```md
# Checkpoint 28A Round 225 R2 Loop 15 Trigger-level Calibration

## 반영 내용
- R2 Loop 15 trigger-level validation을 수행했다.
- SK Hynix, Hanmi Semiconductor, Samsung Electronics, LG Innotek, LG Display, China export-control, Samsung labor risk를 검토했다.
- full adjusted OHLC window는 확보하지 못했으므로 Reuters / WSJ / MarketWatch / AP / FT의 reported event return과 event price anchor를 사용했다.
- OHLC 미확보를 이유로 Stage 후보를 강등하지 않고, price_data_unavailable_after_deep_search로 분리 기록했다.

## 핵심 보정
- HBM mix + OP estimate revision + mass production + relative strength 조합은 Stage2-Actionable 또는 Stage3-Yellow로 승격한다.
- Named customer equipment order + repeat wins + relative strength는 HBM equipment Stage2-Actionable.
- Late catch-up은 relative-strength discount를 적용한다.
- OpenAI/Nvidia headline은 demand validation일 수 있지만, parabolic rally 이후에는 4B overlay가 필요하다.
- China fab equipment restriction과 labor strike는 R2 4C overlay로 둔다.
```

## data/e2r_case_library/cases_r2_loop15_round225.jsonl 초안

```jsonl
{"case_id":"r2_loop15_sk_hynix_hbm_first_mover","symbol":"000660","company_name":"SK Hynix","case_type":"missed_structural_stage2_promote","primary_archetype":"HBM_FIRST_MOVER_STAGE2_TO_GREEN","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable_to_Stage3-Yellow_to_Green","price_validation":{"t0_event_return_pct":4.3,"t0_kospi_return_pct":0.7,"t1_entry_price_anchor_krw":234500,"t1_op_estimate_krw_trn":5.2,"t1_op_estimate_raise_pct":12,"t1_hbm_dram_revenue_share_2025e_pct":38,"t1_target_price_krw":280000,"t2_event_return_pct":9.0,"t2_kospi_return_pct":1.7,"t2_hbm3e_capacity_increase_pct":50,"t3_q4_op_krw_trn":8.1,"t3_hbm_share_dram_revenue_pct":40,"t3_event_return_pct":-4.0,"t4_q2_op_krw_trn":9.2,"t4_revenue_yoy_pct":35,"t4_ytd_gain_pct":54.7,"forward_return_anchor_2025_pct":274,"forward_return_anchor_2026_ytd_pct":200,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"missed_structural_if_old_gate_used","notes":"HBM mix, OP estimate revision, mass production and relative strength should promote Stage2 to Stage3-Yellow."}
{"case_id":"r2_loop15_hanmi_semiconductor_hbm_equipment","symbol":"042700","company_name":"Hanmi Semiconductor","case_type":"Stage2_promote_candidate","primary_archetype":"HBM_EQUIPMENT_STAGE2_ACTIONABLE","best_trigger":"T1","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2024-03-26","event_return_pct":16,"kospi_return_pct":0.7,"market_relative_return_pp":15.3,"sk_hynix_same_day_return_pct":4.3,"specific_customer":"SK Hynix","specific_equipment":"TSV-TC bonders / HBM packaging equipment","sk_hynix_supply_deal_krw_bn":21.48,"recent_contract_wins_krw_bn":200,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate","notes":"Named HBM equipment, named customer, repeated order wins and strong relative strength justify Stage2-Actionable."}
{"case_id":"r2_loop15_samsung_electronics_hbm_catchup_labor_watch","symbol":"005930","company_name":"Samsung Electronics","case_type":"late_stage2_actionable_4c_watch","primary_archetype":"HBM_CATCHUP_LATE_STAGE2","best_trigger":"T2/T3","stage_candidate":"Stage2-Actionable_to_Stage3-Yellow_candidate","price_validation":{"t2_event_return_pct":4.7,"t2_sk_hynix_return_pct":12,"t2_kospi_return_pct":3,"relative_to_sk_hynix_pp":-7.3,"t3_event_return_pct":4.0,"nvidia_partnership_acknowledged":true,"hbm3e_supply_to_related_customers":true,"hbm4_talks_confirmed":true,"sk_hynix_primary_partner_still":true,"q3_2025_op_krw_trn":12.2,"q3_2025_op_growth_pct":32.5,"q3_2025_revenue_krw_trn":86,"semiconductor_division_op_krw_trn":7,"labor_strike_workers_context":48000,"potential_dram_supply_impact_pct":"3-4","potential_nand_supply_impact_pct":"2-3","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2-Actionable_but_not_Green","notes":"Samsung catch-up triggers need relative-strength discount versus SK Hynix and labor continuity overlay."}
{"case_id":"r2_loop15_sk_hynix_openai_asml_4b","symbol":"000660","company_name":"SK Hynix","case_type":"Stage3_Green_with_4B_overlay","primary_archetype":"OPENAI_STARGATE_MEMORY_4B_WATCH","best_trigger":"T1_before_full_4B","stage_candidate":"Stage3-Green + 4B-watch","price_validation":{"openai_stargate_project_usd_bn":500,"t1_event_return_pct":12,"t1_samsung_return_pct":4.7,"t1_kospi_return_pct":3,"t2_event_return_pct":13,"t2_event_price_krw":1447000,"t2_kospi_return_pct":5.1,"ai_capex_2026_usd_bn":700,"asml_order_krw_trn":11.95,"asml_order_usd_bn":7.97,"asml_event_return_pct":5.7,"estimated_euv_machines":30,"us_listing_possible_raise_usd_bn":"9.6-14.4","possible_share_issuance_pct":"2-3","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"aligned_if_stage3_plus_4B_overlay_allowed","notes":"OpenAI/capex triggers validate demand but require 4B overlay after parabolic rally."}
{"case_id":"r2_loop15_memory_china_equipment_export_control","symbol":"005930/000660/042700/067310","company_name":"Samsung / SK Hynix / Hanmi / Hana Micron","case_type":"4c_watch","primary_archetype":"SEMICONDUCTOR_EXPORT_CONTROL_4C_WATCH","best_trigger":"T1","stage_candidate":"4C-watch","price_validation":{"trigger_date":"2025-09-01","samsung_event_mae_pct":-2.6,"sk_hynix_event_mae_pct":-5.0,"license_expiry_days":120,"sk_hynix_china_memory_output_share_pct":"30-40","samsung_china_nand_output_share_pct":"about_one_third","related_firms_affected":["Hana Micron","Hanmi Semiconductor"],"short_term_impact_limited_view":true,"hard_4c_confirmed":false,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","notes":"China fab exposure and U.S. equipment-license status must be explicit 4C overlay."}
{"case_id":"r2_loop15_lg_innotek_apple_ai_upgrade","symbol":"011070","company_name":"LG Innotek","case_type":"Stage2_promote_candidate","primary_archetype":"AI_DEVICE_COMPONENT_STAGE2_ACTIONABLE","best_trigger":"T1","stage_candidate":"Stage2-Actionable","price_validation":{"t1_date":"2024-06-12","t1_entry_price_anchor_krw":272000,"t1_event_return_pct":19,"t1_kospi_return_pct":0.4,"t1_market_relative_return_pp":18.6,"op_2024_forecast_krw_trn":1.110,"op_2024_forecast_growth_pct":33,"t2_date":"2024-06-27","t2_op_estimate_krw_bn":106.4,"t2_consensus_op_krw_bn":81.1,"t2_op_estimate_vs_consensus_pct":31.2,"t2_target_before_krw":280000,"t2_target_after_krw":330000,"t2_event_return_pct":-0.4,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate","notes":"Apple AI device cycle plus OP estimate beat and +19% relative strength justify Stage2-Actionable."}
{"case_id":"r2_loop15_lg_display_apple_oled_recovery","symbol":"034220","company_name":"LG Display","case_type":"evidence_good_but_price_data_incomplete","primary_archetype":"DISPLAY_OLED_APPLE_RECOVERY_STAGE2","best_trigger":"T1_pending_price","stage_candidate":"Stage2","price_validation":{"trigger_date":"2024-07-25","q2_operating_loss_krw_bn":94,"expected_q2_loss_krw_bn":308,"loss_beat_amount_krw_bn":214,"prior_year_loss_krw_bn":881,"revenue_krw_trn":6.7,"revenue_growth_pct":42,"apple_oled_ipad_orders":true,"iphone_pro_max_16_oled_orders":true,"second_half_profitability_guidance_refused":true,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"evidence_good_but_price_data_incomplete","notes":"Apple OLED and loss beat are Stage2 but no Yellow/Green without sustained profitability and price validation."}
{"case_id":"r2_loop15_samsung_labor_supply_chain_4c","symbol":"005930","company_name":"Samsung Electronics","case_type":"4c_watch","primary_archetype":"SEMICONDUCTOR_LABOR_SUPPLY_CHAIN_4C","best_trigger":"T2","stage_candidate":"4C-watch","price_validation":{"trigger_date":"2026-05-19","strike_workers_count":48000,"strike_days":18,"union_profit_share_demand_pct":15,"potential_dram_supply_impact_pct":"3-4","potential_nand_supply_impact_pct":"2-3","government_gdp_impact_estimate_pp":0.5,"hard_4c_confirmed":false,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","notes":"Memory upcycle scoring must include labor continuity and production continuity overlay."}
```

## data/e2r_trigger_calibration/triggers_r2_loop15_round225.jsonl 초안

```jsonl
{"trigger_id":"r2l15_skhynix_T0","case_id":"r2_loop15_sk_hynix_hbm_first_mover","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-26","evidence_available":"AI/HBM rally, Daiwa EPS forecast +41%, HBM3E contribution, SK Hynix +4.3% vs KOSPI +0.7%","event_return_pct":4.3,"market_relative_return_pp":3.6,"trigger_outcome_label":"early_stage2_actionable","promote_to":"Stage2-Actionable"}
{"trigger_id":"r2l15_skhynix_T1","case_id":"r2_loop15_sk_hynix_hbm_first_mover","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-26","evidence_available":"HSBC 2Q OP estimate +12% to 5.2T won, HBM share 38% of DRAM revenue by end-2025, target 280,000","entry_price_krw":234500,"trigger_outcome_label":"Stage2_promote_candidate","promote_to":"Stage3-Yellow_candidate"}
{"trigger_id":"r2l15_skhynix_T2","case_id":"r2_loop15_sk_hynix_hbm_first_mover","trigger_type":"Stage3-Yellow","trigger_date":"2024-09-26","evidence_available":"12-layer HBM3E mass production, 50% capacity increase, supply to customers by year-end","event_return_pct":9.0,"market_relative_return_pp":7.3,"trigger_outcome_label":"excellent_entry_candidate","promote_to":"Stage3-Yellow"}
{"trigger_id":"r2l15_hanmi_T1","case_id":"r2_loop15_hanmi_semiconductor_hbm_equipment","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-26","evidence_available":"SK Hynix HBM packaging equipment, KRW21.48B supply deal, recent wins KRW200B","event_return_pct":16,"market_relative_return_pp":15.3,"trigger_outcome_label":"excellent_stage2_promote_candidate","promote_to":"Stage2-Actionable"}
{"trigger_id":"r2l15_samsung_T2","case_id":"r2_loop15_samsung_electronics_hbm_catchup_labor_watch","trigger_type":"Stage2-Actionable","trigger_date":"2025-10-02","evidence_available":"OpenAI partnership, AI data center memory demand, Samsung +4.7%, SK Hynix +12%","event_return_pct":4.7,"relative_to_skhynix_pp":-7.3,"trigger_outcome_label":"late_catchup_candidate","promote_to":"Stage2-Actionable_only"}
{"trigger_id":"r2l15_skhynix_openai_T1","case_id":"r2_loop15_sk_hynix_openai_asml_4b","trigger_type":"Stage3-Green+4B-watch","trigger_date":"2025-10-02","evidence_available":"OpenAI Stargate partnership, Samsung +4.7%, SK Hynix +12%, KOSPI +3%","event_return_pct":12,"market_relative_return_pp":9,"trigger_outcome_label":"green_demand_confirmation_with_4b_overlay","promote_to":"Stage3-Green+4B"}
{"trigger_id":"r2l15_export_control_T1","case_id":"r2_loop15_memory_china_equipment_export_control","trigger_type":"4C-watch","trigger_date":"2025-09-01","evidence_available":"U.S. revoked authorizations for China fab equipment; Samsung -2.6%, SK Hynix -5%","event_return_pct":"Samsung -2.6 / SK Hynix -5.0","trigger_outcome_label":"thesis_break_watch","promote_to":"4C-watch"}
{"trigger_id":"r2l15_lginnotek_T1","case_id":"r2_loop15_lg_innotek_apple_ai_upgrade","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-12","evidence_available":"Apple/OpenAI AI iPhone upgrade cycle, LG Innotek +19%, OP growth forecast +33%","entry_price_krw":272000,"event_return_pct":19,"market_relative_return_pp":18.6,"trigger_outcome_label":"excellent_stage2_promote_candidate","promote_to":"Stage2-Actionable"}
{"trigger_id":"r2l15_lgdisplay_T1","case_id":"r2_loop15_lg_display_apple_oled_recovery","trigger_type":"Stage2","trigger_date":"2024-07-25","evidence_available":"Q2 loss 94B vs expected 308B, revenue +42%, Apple OLED orders, but no 2H profit guidance","trigger_outcome_label":"evidence_good_but_price_data_incomplete","promote_to":"Stage2_only"}
{"trigger_id":"r2l15_samsung_labor_T2","case_id":"r2_loop15_samsung_labor_supply_chain_4c","trigger_type":"4C-watch","trigger_date":"2026-05-19","evidence_available":"48,000 workers, 18-day strike risk, DRAM supply impact 3-4%, NAND 2-3%","trigger_outcome_label":"thesis_break_watch","promote_to":"4C-watch"}
```

## data/sector_taxonomy/score_weight_profiles_round225_r2_loop15_v1.csv 초안

```csv
archetype,hbm_mix_revenue_share,op_estimate_revision_vs_consensus,mass_production_or_customer_qualification,named_customer_equipment_order,repeat_order_backlog_quality,relative_strength_on_evidence_day,ai_capex_customer_commitment,device_upgrade_op_estimate,ai_theme_only_penalty,late_catchup_penalty,capex_dilution_4b_overlay,export_control_4c_overlay,labor_continuity_4c_overlay,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
HBM_FIRST_MOVER_STAGE2_TO_GREEN,+5,+5,+5,+3,+4,+5,+4,+1,-5,-1,+4,+4,+3,HBM mix+OP revision+mass production+relative strength,customer allocation/margin pending,record profit+volume commitments,SK Hynix missed-structural template.
HBM_EQUIPMENT_STAGE2_ACTIONABLE,+4,+3,+4,+5,+5,+5,+3,+0,-5,-1,+3,+3,+2,named HBM equipment+customer+repeat order+relative strength,customer concentration pending,margin/backlog conversion,Hanmi Stage2-Actionable template.
HBM_CATCHUP_LATE_STAGE2,+4,+4,+5,+3,+2,+3,+4,+1,-5,-4,+3,+4,+5,Nvidia/OpenAI catch-up requires relative-strength discount,allocation/timing pending,shipment+allocation+margin,Samsung catch-up not Green without allocation.
OPENAI_STARGATE_MEMORY_4B_WATCH,+5,+4,+4,+3,+3,+5,+5,+0,-4,-1,+5,+4,+4,large AI capex commitment+relative strength,valuation/capex overlay,volume+profit confirmed,OpenAI demand validates but 4B after parabolic rally.
SEMICONDUCTOR_EXPORT_CONTROL_4C_WATCH,+2,+1,+1,+1,+1,+2,+1,+0,-2,-1,+2,+5,+2,export equipment authorization risk,license uncertainty,license relief or alternative equipment,China fab exposure is explicit 4C overlay.
AI_DEVICE_COMPONENT_STAGE2_ACTIONABLE,+0,+5,+2,+3,+3,+5,+3,+5,-4,-1,+2,+2,+1,AI device upgrade+OP estimate+relative strength,sell-through pending,shipments/ASP confirmed,LG Innotek Stage2-Actionable template.
DISPLAY_OLED_APPLE_RECOVERY_STAGE2,+0,+4,+2,+3,+2,+2,+1,+4,-4,-1,+2,+2,+1,loss beat+Apple OLED order,profitability guidance missing,sustained profit and utilization,LG Display remains Stage2 until sustained profitability.
SEMICONDUCTOR_LABOR_SUPPLY_CHAIN_4C,+3,+2,+2,+1,+1,+1,+2,+0,-1,-1,+2,+3,+5,labor continuity affects memory supply,settlement pending,production continuity confirmed,Samsung labor strike is 4C-watch overlay.
```

---

# 이번 R2 Loop 15 결론

```text
1. SK Hynix는 R2의 핵심 missed_structural case다.
   2024년 HBM mix, OP estimate revision, HBM3E mass production trigger를 Stage2로만 두면 너무 늦다.

2. Hanmi Semiconductor는 Stage2-Actionable이다.
   named customer, HBM packaging equipment, KRW21.48B order, repeat wins, +16% relative strength가 동시에 있었다.

3. Samsung Electronics는 late catch-up이다.
   OpenAI/Nvidia/HBM4 trigger는 좋지만 SK Hynix 대비 상대강도가 약하고 labor risk가 4C overlay다.

4. SK Hynix OpenAI/Stargate/ASML trigger는 Stage3-Green + 4B-watch다.
   demand confirmation은 강하지만 2025 +274%, 2026 +200%+ 이후에는 sizing overlay가 필요하다.

5. China equipment restriction은 R2 4C-watch다.
   AI memory upcycle이 있어도 China fab exposure와 equipment-license risk는 별도로 점수화해야 한다.

6. LG Innotek은 AI-device Stage2-Actionable이다.
   Apple AI upgrade 기대, OP estimate beat, +19% event move가 강했다.

7. LG Display는 Stage2 evidence에 머문다.
   Apple OLED order와 loss beat는 좋지만 지속 흑자 guidance가 없었다.

8. Samsung labor strike는 R2 hard-watch다.
   AI memory supply chain에서 노동/생산연속성은 더 이상 부차 변수가 아니다.
```

한 문장으로 압축하면:

> **R2 Loop 15에서 새로 배운 핵심은 “AI/HBM 테마”가 아니라, HBM mix·OP estimate revision·mass production·named customer equipment order·relative strength가 동시에 나오면 Stage2를 Stage3-Yellow로 올려야 한다는 것이다. 반대로 late catch-up, China export-control, labor continuity, parabolic rally 후 OpenAI/Nvidia headline은 반드시 4B/4C overlay를 붙여야 한다.**

[1]: https://www.wsj.com/articles/south-korean-chip-shares-rally-as-ai-frenzy-persists-260f9996 "https://www.wsj.com/articles/south-korean-chip-shares-rally-as-ai-frenzy-persists-260f9996"
[2]: https://www.reuters.com/technology/nvidia-supplier-sk-hynix-says-begins-mass-production-12-layer-hbm3e-chips-2024-09-26/ "https://www.reuters.com/technology/nvidia-supplier-sk-hynix-says-begins-mass-production-12-layer-hbm3e-chips-2024-09-26/"
[3]: https://www.reuters.com/technology/nvidia-supplier-sk-hynix-posts-record-quarterly-profit-2025-01-22/ "https://www.reuters.com/technology/nvidia-supplier-sk-hynix-posts-record-quarterly-profit-2025-01-22/"
[4]: https://www.reuters.com/world/asia-pacific/ai-boom-puts-sk-hynix-cusp-1-trillion-market-value-2026-05-14/ "https://www.reuters.com/world/asia-pacific/ai-boom-puts-sk-hynix-cusp-1-trillion-market-value-2026-05-14/"
[5]: https://www.reuters.com/world/asia-pacific/samsung-sk-hynix-shares-rally-openai-partnerships-2025-10-02/ "https://www.reuters.com/world/asia-pacific/samsung-sk-hynix-shares-rally-openai-partnerships-2025-10-02/"
[6]: https://www.reuters.com/world/asia-pacific/samsung-electronics-says-it-is-talks-with-nvidia-supply-next-generation-hbm4-2025-10-31/ "https://www.reuters.com/world/asia-pacific/samsung-electronics-says-it-is-talks-with-nvidia-supply-next-generation-hbm4-2025-10-31/"
[7]: https://www.reuters.com/business/world-at-work/what-are-samsung-union-workers-demanding-how-might-strike-play-out-2026-05-19/ "https://www.reuters.com/business/world-at-work/what-are-samsung-union-workers-demanding-how-might-strike-play-out-2026-05-19/"
[8]: https://www.reuters.com/world/asia-pacific/sk-hynix-shares-rally-12-after-us-tech-firms-signal-strong-spending-ai-data-2026-05-04/ "https://www.reuters.com/world/asia-pacific/sk-hynix-shares-rally-12-after-us-tech-firms-signal-strong-spending-ai-data-2026-05-04/"
[9]: https://www.reuters.com/world/asia-pacific/sk-hynix-buy-euv-scanners-8-billion-asml-korea-2026-03-24/ "https://www.reuters.com/world/asia-pacific/sk-hynix-buy-euv-scanners-8-billion-asml-korea-2026-03-24/"
[10]: https://www.reuters.com/world/china/shares-samsung-sk-hynix-drop-after-us-makes-it-harder-produce-chips-china-2025-09-01/ "https://www.reuters.com/world/china/shares-samsung-sk-hynix-drop-after-us-makes-it-harder-produce-chips-china-2025-09-01/"
[11]: https://www.wsj.com/articles/lg-innotek-shares-rally-tracking-apple-s-ai-driven-gains-6e193cc3 "https://www.wsj.com/articles/lg-innotek-shares-rally-tracking-apple-s-ai-driven-gains-6e193cc3"
[12]: https://www.marketwatch.com/story/lg-innotek-could-post-2q-earnings-beat-market-talk-534689b2 "https://www.marketwatch.com/story/lg-innotek-could-post-2q-earnings-beat-market-talk-534689b2"
[13]: https://www.reuters.com/technology/lg-display-reports-q2-loss-weak-demand-panels-2024-07-25/ "https://www.reuters.com/technology/lg-display-reports-q2-loss-weak-demand-panels-2024-07-25/"

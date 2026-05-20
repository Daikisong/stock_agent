순서상 이번은 **R1 Loop 15 — 산업재·수주·인프라 trigger-level price validation 라운드**다.

이번부터 방식이 바뀐다. 기존처럼 “case 하나에 Stage 하나”를 붙이지 않고, **case 안의 T0~T6 trigger를 분해해서 어느 trigger가 실제 entry로 좋았는지** 본다.

```text
round = R1 Loop 15
round_id = round_224
large_sector = INDUSTRIALS_ORDERS_INFRASTRUCTURE
method = trigger_level_backtest_v1
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R2 Loop 15
```

중요한 제한부터 명확히 둔다. 이번 환경에서 KRX/Naver/Yahoo/Stooq의 **수정주가 일봉 OHLC 30D/90D/180D/1Y window**를 안정적으로 직접 추출하지 못했다. 그래서 이번은 `reported event price / reported event return` 기반의 trigger-level anchor validation으로 작성하고, full MFE/MAE window가 필요한 칸은 `price_data_unavailable_after_deep_search`로 둔다. 다만 이번부터는 **OHLC 미확보를 이유로 Stage 후보 자체를 강등하지 않는다.** Stage 판정과 가격검증 완료 여부를 분리한다.

---

# 1. 이번 라운드 대섹터

```text
R1 = 산업재·수주·인프라
```

이번 R1에서 보는 핵심은 이거다.

```text
방산:
수주 headline → 출하/인도 → OP estimate 상향 → backlog quality → 증자/희석 → delivery margin

조선:
선가 상승 → 수주잔고 → backlog duration → 원가/인건비 → 인도 margin → U.S. 협력/제재 risk

전력기기:
data center/grid demand → 미국 매출비중 → 수주/ASP → 생산능력 → backlog margin → lead time

EPC/플랜트:
mega order → advance payment → cost lock-in → working capital → claim risk → completion margin

원전:
preferred bidder → final contract → legal challenge 해소 → construction margin → long-cycle cashflow
```

---

# 2. 대상 canonical archetype

```text
DEFENSE_EXPORT_STAGE2_ACTIONABLE
MISSILE_DEFENSE_ORDER_4B_TIMING
DEFENSE_BACKLOG_DILUTION_OVERLAY
SHIPBUILDING_BACKLOG_PRICE_STAGE2_ACTIONABLE
GRID_EQUIPMENT_US_GROWTH_STAGE2_PROMOTE
OVERSEAS_EPC_ORDER_STAGE2_YELLOW
NUCLEAR_EXPORT_PREFERRED_BIDDER_STAGE2
```

---

# 3. deep sub-archetype

```text
Hyundai Rotem:
- K2 Poland tank shipments
- OP estimate beat
- second Poland contract
- Stage2 trigger가 사실상 Stage3-Yellow였는지 검증

LIG Nex1:
- Cheongung-II / M-SAM II
- Iraq / Saudi orders
- 1H surge 후 downgrade
- combat-validation 이후 추가 상승 가능성
- 4B가 너무 이른지 검증

Hanwha Aerospace:
- K9 Romania order
- backlog expansion
- share sale / dilution
- Stage3 + 4B overlay 허용 여부

Shipbuilding basket:
- Samsung Heavy / Hanwha Ocean / HD Hyundai Heavy
- Clarksons order/share-price/newbuilding price trigger
- MASGA / U.S. shipbuilding cooperation
- backlog quality vs event premium

LS Electric:
- U.S. data-center / renewable / EV value-chain electrical equipment demand
- U.S. revenue share forecast from below 5% to 20%
- target price +87%
- immediate price failed but possible Stage2_promote candidate

Samsung E&A:
- Saudi Aramco Fadhili $6B order
- strong event price but EPC execution gate
- Stage2-Actionable vs Stage3-Yellow 검증

Czech nuclear:
- KHNP preferred bidder
- Doosan / KEPCO E&C pre-event rerating
- legal challenge / final contract gate
```

---

# 4. 선정 case 요약

| bucket                              | case                   | 핵심 판정                                                                                       |
| ----------------------------------- | ---------------------- | ------------------------------------------------------------------------------------------- |
| structural_success / Stage2_promote | Hyundai Rotem          | OP estimate + Poland shipment + 주가 +9.3%는 Stage2가 아니라 Stage2-Actionable 또는 Stage3-Yellow 후보 |
| Stage3-Yellow candidate             | Samsung E&A            | $6B order + +8.5% + target upside 30.8%, 단 completion margin gate 남음                        |
| Stage2_promote_candidate            | LS Electric            | U.S. revenue mix와 target +87%는 강하지만 당일 -5.4%, immediate price failed                        |
| 4B-watch                            | LIG Nex1               | 1H +69% 후 downgrade -11%, 그런데 이후 Iraq order/전쟁 validation이 있어 4B threshold 재검토              |
| Stage3 + 4B overlay                 | Hanwha Aerospace       | order/backlog는 강하지만 2025년 dilution shock으로 4B overlay 필요                                    |
| event premium / Stage2              | Shipbuilding basket    | 수주·선가·3년 backlog로 +11~16%, Stage2-Actionable 후보                                             |
| Stage2 + legal 4C-watch             | Czech nuclear / Doosan | preferred bidder와 pre-event rerating은 강하지만 final contract/legal gate 남음                     |

---

# 5. Case별 trigger grid

## Case A — Hyundai Rotem / K2 Poland export

```text
symbol = 064350
case_type = Stage2_promote_candidate / Stage3-Yellow candidate
archetype = DEFENSE_EXPORT_STAGE2_ACTIONABLE
```

### Trigger grid

| trigger | type               |            date | 당시 공개 evidence                                                                                | 가격 anchor                          | outcome                            |
| ------- | ------------------ | --------------: | --------------------------------------------------------------------------------------------- | ---------------------------------- | ---------------------------------- |
| T0      | earliest awareness |            2022 | Poland 1차 K2 계약, 유럽 재무장 시작                                                                    | full OHLC unavailable              | watch                              |
| T1      | Stage 2 evidence   |      2024-04-09 | 18대 K2 Poland shipment, Q1 OP +85% YoY estimate, consensus 대비 +33.1%                          | +9.3%, 41,300 won, KOSPI -0.3%     | excellent Stage2 trigger candidate |
| T2      | Stage 2-Actionable |      2024-04-09 | K2 export revenue 270B won, forecast quarterly revenue의 nearly 1/3, target +19% to 47,500 won | target upside from 41,300 = +15.0% | Stage2_promote_candidate           |
| T3      | Stage3-Yellow      |      2024-04-09 | OP estimate 상향 + shipment + revenue contribution + relative strength 동시 충족                    | relative +9.6pp vs KOSPI           | should be Stage3-Yellow            |
| T4      | Stage3-Green       |      2025-08-01 | Poland 2차 180대 K2 계약 signing, 약 $6.5B, 61대 Poland local production                            | full OHLC unavailable              | late confirmation                  |
| T5      | 4B                 | 2025-03~2025-08 | FT: Hyundai Rotem +123% YTD, defense-sector overheat                                          | full OHLC unavailable              | 4B-watch                           |
| T6      | 4C                 |             N/A | hard break 없음                                                                                 | N/A                                | hard_4c_not_confirmed              |

Hyundai Rotem은 이번 trigger-level 방식에서 가장 중요한 case다. 2024년 4월 9일에는 단순 수주 기대가 아니라, **18대 K2 shipment, Q1 OP +85% YoY 추정, consensus 대비 33.1% 높은 OP estimate, Poland export revenue 270B won, target price +19%**가 동시에 나왔다. 주가는 +9.3%로 KOSPI -0.3%를 크게 이겼다. 이건 기존 방식에서 Stage 2로 두면 너무 낮다. 최소 `Stage2-Actionable`, 더 공격적으로는 `Stage3-Yellow`다. ([월스트리트저널][1])

이후 2025년에는 Poland 2차 180대 K2 계약이 체결됐고, Reuters는 이 계약이 약 $6.5B 규모로 알려졌으며 61대는 Poland 현지 생산이라고 보도했다. 이건 T4, 즉 늦은 confirmation이다. 만약 T4에서만 Stage3를 주면, T1/T2 구간의 상당한 rerating을 놓쳤을 가능성이 크다. ([Reuters][2])

### Trigger price validation row

```json
{
  "case_id": "r1_loop15_hyundai_rotem_k2_poland_trigger_grid",
  "symbol": "064350",
  "best_entry_trigger": "T2/T3",
  "best_entry_trigger_type": "Stage2-Actionable_to_Stage3-Yellow",
  "trigger_date": "2024-04-09",
  "entry_price_anchor": 41300,
  "entry_price_source_type": "reported intraday/last event price",
  "event_mfe_pct": 9.3,
  "kospi_same_context_pct": -0.3,
  "market_relative_return_pp": 9.6,
  "op_estimate_yoy_growth_pct": 85,
  "op_estimate_krw_bn": 59.10,
  "consensus_op_krw_bn": 44.40,
  "op_estimate_vs_consensus_pct": 33.1,
  "poland_k2_revenue_krw_bn": 270,
  "target_price_krw": 47500,
  "target_upside_from_event_price_pct": 15.0,
  "mfe_30d_90d_180d_1y_2y": "price_data_unavailable_after_deep_search",
  "mae_30d_90d_180d_1y": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_promote_candidate",
  "stage_gate_correction": "shipment + OP estimate beat + revenue contribution + relative strength should upgrade Stage2 to Stage3-Yellow"
}
```

### 판정

```text
score_price_alignment = missed_structural_risk
old_label = Stage 2
new_label = Stage2-Actionable / Stage3-Yellow
reason = 수주 기대가 아니라 출하·실적추정·매출기여·상대강도가 동시에 확인됨
```

---

## Case B — LIG Nex1 / Cheongung-II missile defense

```text
symbol = 079550
case_type = Stage3-Yellow + 4B timing audit
archetype = MISSILE_DEFENSE_ORDER_4B_TIMING
```

### Trigger grid

| trigger | type               |       date | 당시 공개 evidence                                                                    | 가격 anchor                    | outcome                |
| ------- | ------------------ | ---------: | --------------------------------------------------------------------------------- | ---------------------------- | ---------------------- |
| T0      | awareness          |    2024-02 | Saudi M-SAM II $3.2B deal context                                                 | price unavailable            | Stage 2                |
| T1      | Stage 2 evidence   | 2024-06-25 | DAPA 144B won domestic contract                                                   | price unavailable            | weak Stage 2           |
| T2      | 4B candidate       | 2024-07-02 | 1H 주가 +69%, KOSPI +5.4%, KB downgrade Buy→Hold                                    | -11%, close 195,700 won      | 4B early warning       |
| T3      | Stage 2-Actionable | 2024-09-20 | Iraq $2.8B M-SAM II order, Saudi $3.2B follow-on context                          | +3.6%, KOSPI +0.9%           | Stage2-Actionable      |
| T4      | Stage3-Yellow      | 2026-03-11 | FT: Cheongung-II combat validation, 96% success claim, shares +47% since conflict | reported +47% since conflict | Stage3-Yellow but late |
| T5      | 4B                 |    2026-03 | Iran-war validation + strong rally                                                | full OHLC unavailable        | 4B-watch               |
| T6      | 4C                 |        N/A | hard break 없음                                                                     | N/A                          | hard_4c_not_confirmed  |

LIG Nex1은 4B timing을 다시 봐야 하는 case다. 2024년 7월 2일 KB는 1H 주가 +69%와 KOSPI +5.4% 대비 과열을 근거로 rating을 Hold로 낮췄고, 주가는 -11%로 195,700 won에 마감했다. 이 trigger는 4B로 유효했다. 하지만 이후 2024년 9월 Iraq $2.8B order가 나왔고, 2026년에는 Cheongung-II의 전쟁 실전 validation narrative까지 붙었다. 즉 2024년 7월 4B는 “완전 exit”보다는 “position trim / 4B-watch”가 맞다. ([마켓워치][3])

2024년 9월 Iraq order는 단순 rumor가 아니라 3.71T won, 약 $2.8B order였고, 기존 Saudi $3.2B deal 뒤에 나온 export validation이었다. 주가는 +3.6%, KOSPI +0.9%였다. 이건 Stage 2에 머무르기엔 약간 강하고, `Stage2-Actionable`으로 승격할 만하다. ([Reuters][4])

2026년 FT는 Cheongung-II가 Iran missile/drone attack에 대해 96% success rate를 보였다는 국회 국방위원회 인용과 함께, LIG Nex1 shares가 conflict 이후 거의 +47% 올랐다고 보도했다. 이건 product validation이 붙은 Stage3-Yellow지만, entry로는 2024년 Iraq order보다 늦었을 가능성이 크다. ([Financial Times][5])

### Trigger price validation row

```json
{
  "case_id": "r1_loop15_lig_nex1_msam_trigger_grid",
  "symbol": "079550",
  "best_entry_trigger": "T3",
  "best_entry_trigger_type": "Stage2-Actionable",
  "trigger_date": "2024-09-20",
  "event_mfe_pct": 3.6,
  "kospi_same_context_pct": 0.9,
  "market_relative_return_pp": 2.7,
  "iraq_order_value_krw_trn": 3.71,
  "iraq_order_value_usd_bn": 2.8,
  "saudi_prior_order_usd_bn": 3.2,
  "four_country_operator_context": true,
  "t2_4b_date": "2024-07-02",
  "t2_4b_event_mae_pct": -11,
  "t2_4b_close_price_krw": 195700,
  "t2_pre_event_1h_gain_pct": 69,
  "t2_kospi_1h_gain_pct": 5.4,
  "t4_combat_validation_reported_gain_pct": 47,
  "mfe_30d_90d_180d_1y": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_promote_candidate_with_4B_overlay",
  "stage_gate_correction": "export order after prior large orders should upgrade Stage2 to Stage2-Actionable; 4B should be trim not hard exit when new order pipeline remains"
}
```

### 판정

```text
score_price_alignment = Stage2_promote_candidate
4B_timing = partially_too_early_if_used_as_full_exit
new_rule = 1H +69% 같은 과열은 4B-watch지만, 신규 order pipeline이 살아 있으면 exit가 아니라 sizing-down
```

---

## Case C — Hanwha Aerospace / K9 Romania + dilution overlay

```text
symbol = 012450
case_type = Stage3 + 4B overlay
archetype = DEFENSE_BACKLOG_DILUTION_OVERLAY
```

### Trigger grid

| trigger | type             |       date | 당시 공개 evidence                                                     | 가격 anchor             | outcome                     |
| ------- | ---------------- | ---------: | ------------------------------------------------------------------ | --------------------- | --------------------------- |
| T0      | awareness        |  2022~2024 | Europe rearmament, K9 export cycle                                 | full OHLC unavailable | Stage 1                     |
| T1      | Stage 2 evidence | 2024-07-09 | Romania $1B K9 order, 54 K9, 36 K10, contract to 2029              | +5%, record high      | Stage2-Actionable           |
| T2      | Stage3-Yellow    | 2024-07-09 | backlog 5.1T won → 30T won by Mar 2024, global howitzer share >50% | reported +5%          | Stage3-Yellow candidate     |
| T3      | Stage3-Green     |  2025-03 전 | defense order cycle + YTD >2x                                      | full OHLC unavailable | Green possible but overheat |
| T4      | 4B               | 2025-03-21 | 3.6T won share sale, 605,000 won issue price, 16% discount         | -13%                  | 4B success                  |
| T5      | 4C-watch         | 2025-03-27 | FSS filing revision order, disclosure quality issue                | full OHLC unavailable | disclosure gate             |
| T6      | hard 4C          |         없음 | 계약 붕괴는 아님                                                          | N/A                   | no hard 4C                  |

Hanwha Aerospace는 새 Stage 체계에서 반드시 **Stage3 + 4B overlay**로 처리해야 한다. Romania K9 order 자체는 $1B, 54 K9, 36 K10, 계약기간 2029년까지라 Stage2-Actionable이다. Reuters는 이 order와 함께 backlog가 2021년 말 5.1T won에서 2024년 3월 약 30T won까지 커졌고, Hanwha가 global howitzer export market에서 50% 이상을 차지한다고 설명했다. 이 정도면 기존 “단순 수주 Stage 2”보다 강하고, `Stage3-Yellow` 후보로 둬야 한다. ([Reuters][6])

하지만 2025년 3월에는 3.6T won share sale이 나왔고, 주가는 -13%를 맞았다. FT는 그 직전 Hanwha shares가 YTD 두 배 이상 올랐고, issue price가 전일 종가 대비 16% discount였다고 보도했다. 따라서 “Stage3가 틀렸다”가 아니라, **Stage3 위에 4B dilution overlay를 붙였어야 한다**는 결론이다. ([Financial Times][7])

### Trigger price validation row

```json
{
  "case_id": "r1_loop15_hanwha_aerospace_k9_backlog_dilution_overlay",
  "symbol": "012450",
  "best_entry_trigger": "T1/T2",
  "best_entry_trigger_type": "Stage2-Actionable_to_Stage3-Yellow",
  "stage4b_trigger": "T4",
  "stage4b_date": "2025-03-21",
  "romania_order_value_usd_bn": 1.0,
  "k9_howitzers": 54,
  "k10_resupply_vehicles": 36,
  "contract_end": "2029-07",
  "backlog_end_2021_krw_trn": 5.1,
  "backlog_march_2024_krw_trn": 30,
  "backlog_growth_multiple": 5.88,
  "t1_event_mfe_pct": 5.0,
  "share_sale_krw_trn": 3.6,
  "share_sale_usd_bn": 2.5,
  "offer_price_krw": 605000,
  "discount_to_prior_close_pct": 16,
  "t4_event_mae_pct": -13,
  "mfe_30d_90d_180d_1y": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage3_Yellow_with_4B_overlay",
  "stage_gate_correction": "do not cancel Stage3 because of 4B; attach dilution overlay and adjust position"
}
```

### 판정

```text
score_price_alignment = aligned_if_Stage3_plus_4B_overlay_allowed
old_error = 4B-watch 때문에 Stage3를 취소함
new_rule = order/backlog evidence가 강하면 Stage3-Yellow 가능, 이후 dilution은 4B overlay
```

---

## Case D — Shipbuilding basket / order momentum + rising newbuilding prices

```text
symbols = 010140 / 042660 / 329180 / 010620
company_scope = Samsung Heavy Industries / Hanwha Ocean / HD Hyundai Heavy / HD Hyundai Mipo
case_type = Stage2-Actionable / event_premium
archetype = SHIPBUILDING_BACKLOG_PRICE_STAGE2_ACTIONABLE
```

### Trigger grid

| trigger | type               |       date | 당시 공개 evidence                                                                              | 가격 anchor                                          | outcome                 |
| ------- | ------------------ | ---------: | ------------------------------------------------------------------------------------------- | -------------------------------------------------- | ----------------------- |
| T0      | awareness          |    2024-03 | Korea reclaimed top global shipbuilding orders in February                                  | sector rally                                       | Stage 2                 |
| T1      | Stage 2 evidence   | 2024-03-14 | new global orders +18% YoY, Korea 50% share, Clarksons newbuilding price index +0.2% weekly | Samsung Heavy +16%, Hanwha Ocean +13%, HD HHI +11% | Stage2-Actionable       |
| T2      | Stage3-Yellow      | 2024-03-14 | backlog enough for 3 years + rising ship prices + large orders                              | same anchors                                       | Stage3-Yellow candidate |
| T3      | Stage 2 evidence   | 2025-04-07 | HII-HD HHI MOU for U.S. commercial/defense shipbuilding cooperation                         | price unavailable                                  | Stage 2                 |
| T4      | 4B / event premium | 2025-08-27 | HD HHI-HD Mipo merger, MASGA / U.S.-Korea shipbuilding cooperation                          | HD HHI +11.3%, HD Mipo +14.6%                      | 4B-watch                |
| T5      | 4C-watch           |    2025-10 | Hanwha Ocean China sanctions read-through                                                   | from R11                                           | geopolitics watch       |
| T6      | hard 4C            |        N/A | no hard break for whole basket                                                              | N/A                                                | none                    |

조선 basket은 Stage2가 이미 action 가능했는지 봐야 한다. 2024년 3월 14일 WSJ 보도에 따르면 Samsung Heavy +16%, Hanwha Ocean +13%, HD Hyundai Heavy +11%가 나왔다. 단순 테마가 아니라, **2월 글로벌 신조선 발주 +18% YoY, 한국 50% 점유, Clarksons Newbuilding Price Index 상승, 3년치 backlog**가 같이 붙었다. 이 조합은 `Stage2-Actionable`이고, 보수적으로도 `Stage3-Yellow candidate`다. ([월스트리트저널][8])

2025년 8월 HD Hyundai Heavy와 HD Hyundai Mipo merger는 U.S. shipbuilding cooperation / MASGA narrative가 붙으면서 HD HHI +11.3%, HD Mipo +14.6%가 나왔다. 다만 이 trigger는 operational margin보다 control/merger/event premium 성격이 강해서 4B-watch로 둔다. ([Reuters][9])

### Trigger price validation row

```json
{
  "case_id": "r1_loop15_shipbuilding_order_price_trigger_grid",
  "symbols": "010140/042660/329180/010620",
  "best_entry_trigger": "T1/T2",
  "best_entry_trigger_type": "Stage2-Actionable_to_Stage3-Yellow",
  "stage4b_trigger": "T4",
  "t1_date": "2024-03-14",
  "samsung_heavy_event_mfe_pct": 16,
  "samsung_heavy_event_price_krw": 9210,
  "hanwha_ocean_event_mfe_pct": 13,
  "hanwha_ocean_event_price_krw": 27450,
  "hd_hhi_event_mfe_pct": 11,
  "hd_hhi_event_price_krw": 122900,
  "kospi_same_context_pct": 0.5,
  "global_new_orders_yoy_pct": 18,
  "korea_global_order_share_pct": 50,
  "china_global_order_share_pct": 41,
  "newbuilding_price_index": 181.81,
  "newbuilding_price_index_weekly_change_pct": 0.2,
  "backlog_duration_context_years": 3,
  "t4_hd_hhi_mfe_pct": 11.3,
  "t4_hd_mipo_mfe_pct": 14.6,
  "mfe_30d_90d_180d_1y": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_promote_candidate",
  "stage_gate_correction": "orders + price index + backlog duration + relative strength should upgrade from Stage2 to Stage3-Yellow candidate"
}
```

### 판정

```text
score_price_alignment = Stage2_promote_candidate
old_error = 수주/선가/잔고 조합을 단순 event premium으로만 처리할 위험
new_rule = order momentum + pricing + backlog duration이면 Stage2-Actionable 이상
```

---

## Case E — LS Electric / U.S. electrical equipment growth

```text
symbol = 010120
case_type = Stage2_promote_candidate / evidence_good_but_price_failed
archetype = GRID_EQUIPMENT_US_GROWTH_STAGE2_PROMOTE
```

### Trigger grid

| trigger | type              |       date | 당시 공개 evidence                                                                                              | 가격 anchor                           | outcome                                  |
| ------- | ----------------- | ---------: | ----------------------------------------------------------------------------------------------------------- | ----------------------------------- | ---------------------------------------- |
| T0      | awareness         |  2024~2025 | U.S. grid / data-center / EV value-chain demand                                                             | sector source                       | Stage 1                                  |
| T1      | Stage 2 evidence  | 2024-07-01 | U.S. revenue share forecast below 5% in 2022 → 20% in 2024                                                  | shares -5.4%, 208,500 won           | evidence good but immediate price failed |
| T2      | Stage2-Actionable | 2024-07-01 | Daiwa 2024~2026 revenue forecast +4%~22%, target 150k→280k, +87%                                            | target upside from 208,500 = +34.3% | promote candidate                        |
| T3      | Stage3-Yellow     |  2025~2026 | U.S. transformer shortage, GSU demand +274%, substation transformer demand +116%, prices +80% in five years | full OHLC unavailable               | structural candidate                     |
| T4      | 4B                |        N/A | valuation/overheat data unavailable                                                                         | N/A                                 | not confirmed                            |
| T5      | 4C                |        N/A | hard break 없음                                                                                               | N/A                                 | not confirmed                            |

LS Electric은 흥미로운 case다. 2024년 7월 1일에는 좋은 evidence가 나왔는데 주가는 당일 -5.4%였다. Daiwa는 U.S. operations revenue share가 2022년 5% 미만에서 2024년 약 20%로 올라갈 수 있다고 봤고, 2024~2026 revenue forecast를 4~22% 올리며 target price를 150,000 won에서 280,000 won으로 87% 상향했다. 그런데 주가는 208,500 won으로 -5.4%였다. 즉 trigger 자체는 좋았지만 당일 가격은 실패했다. ([마켓워치][10])

다만 2025~2026년 Reuters는 U.S. transformer shortage가 심화됐고, GSU transformer demand가 2019~2025년 274%, substation power transformer demand가 116% 증가했으며 transformer prices가 5년간 약 80% 올랐다고 보도했다. 그러면 LS Electric의 2024년 T1/T2는 당일은 `evidence_good_but_price_failed`였지만, 구조적으로는 `Stage2_promote_candidate`였을 수 있다. 이건 full OHLC로 재검증해야 한다. ([Reuters][11])

### Trigger price validation row

```json
{
  "case_id": "r1_loop15_ls_electric_us_grid_trigger_grid",
  "symbol": "010120",
  "best_entry_trigger": "T2_pending_full_ohlc",
  "trigger_date": "2024-07-01",
  "entry_price_anchor_krw": 208500,
  "event_mae_pct": -5.4,
  "us_revenue_share_2022_pct": "below_5",
  "us_revenue_share_2024_forecast_pct": 20,
  "revenue_forecast_raise_2024_2026_pct": "4-22",
  "target_price_before_krw": 150000,
  "target_price_after_krw": 280000,
  "target_raise_pct": 86.7,
  "target_upside_from_event_price_pct": 34.3,
  "gsu_transformer_demand_growth_2019_2025_pct": 274,
  "substation_transformer_demand_growth_2019_2025_pct": 116,
  "transformer_price_5y_growth_pct": 80,
  "mfe_30d_90d_180d_1y": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "evidence_good_but_price_failed_then_Stage2_promote_candidate",
  "stage_gate_correction": "immediate event price failure should not kill structural trigger; re-test with full OHLC"
}
```

### 판정

```text
score_price_alignment = inconclusive_but_promote_candidate
old_error = 당일 -5.4%만 보고 false positive 처리할 위험
new_rule = good evidence + immediate price fail은 full-window MFE/MAE로 재검증
```

---

## Case F — Samsung E&A / Saudi Aramco Fadhili EPC order

```text
symbol = 028050
case_type = Stage2-Actionable / Stage3-Yellow candidate
archetype = OVERSEAS_EPC_ORDER_STAGE2_YELLOW
```

### Trigger grid

| trigger | type             |       date | 당시 공개 evidence                                                                  | 가격 anchor               | outcome                 |
| ------- | ---------------- | ---------: | ------------------------------------------------------------------------------- | ----------------------- | ----------------------- |
| T0      | awareness        | 2024-04-02 | Saudi Aramco Fadhili expansion news                                             | N/A                     | Stage 1                 |
| T1      | Stage 2 evidence | 2024-04-03 | Samsung E&A $6B contract, Aramco $7.7B project                                  | +8.5%, 26,750 won       | Stage2-Actionable       |
| T2      | Stage3-Yellow    | 2024-04-03 | project capacity +60%, sulfur +2,300 tpd, completion by Nov 2027, target 35,000 | target upside +30.8%    | Stage3-Yellow candidate |
| T3      | Stage3-Green     |        N/A | advance payment/cost lock-in/completion margin 미확인                              | N/A                     | no Green                |
| T4      | 4B               | 2024-04-03 | event pop +8.5%, EPC execution risk                                             | full window unavailable | 4B-watch                |
| T5      | 4C               |        N/A | cost overrun / claim 없음                                                         | N/A                     | no 4C                   |

Samsung E&A는 기존 방식에선 “mega-order라 Stage 2”라고만 하기 쉬웠다. 그런데 trigger-level로 보면 T1은 꽤 강하다. 계약금액이 약 $6B로 회사의 2017~2023년 평균 annual contract wins와 비슷한 규모였고, 주가는 KOSPI -1.4% 속에서 +8.5%로 26,750 won까지 올랐다. KB target 35,000 won 기준 upside도 30.8%였다. 다만 EPC 특성상 advance payment, cost lock-in, working capital, claim risk가 남아 있어서 `Stage3-Green`은 아니고 `Stage3-Yellow candidate`가 맞다. ([월스트리트저널][12])

### Trigger price validation row

```json
{
  "case_id": "r1_loop15_samsung_ena_fadhili_trigger_grid",
  "symbol": "028050",
  "best_entry_trigger": "T1/T2",
  "best_entry_trigger_type": "Stage2-Actionable_to_Stage3-Yellow",
  "trigger_date": "2024-04-03",
  "entry_price_anchor_krw": 26750,
  "event_mfe_pct": 8.5,
  "kospi_same_context_pct": -1.4,
  "market_relative_return_pp": 9.9,
  "contract_value_usd_bn": 6.0,
  "project_total_value_usd_bn": 7.7,
  "gas_capacity_increase_pct": 60,
  "sulfur_production_increase_tpd": 2300,
  "completion_target": "2027-11",
  "target_price_krw": 35000,
  "target_upside_from_event_price_pct": 30.8,
  "stage3_green_gate_missing": ["advance_payment", "cost_lock_in", "working_capital", "completion_margin"],
  "mfe_30d_90d_180d_1y": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage3_Yellow_candidate"
}
```

### 판정

```text
score_price_alignment = Stage2_promote_candidate
old_label = Stage 2
new_label = Stage2-Actionable / Stage3-Yellow
reason = mega-order + relative strength + target upside가 동시에 있었으나 EPC completion gate는 남음
```

---

## Case G — Czech nuclear / Doosan Enerbility & KEPCO E&C

```text
symbols = 034020 / 052690 / 051600
case_type = Stage2_promote_candidate + legal_4C_watch
archetype = NUCLEAR_EXPORT_PREFERRED_BIDDER_STAGE2
```

### Trigger grid

| trigger | type              |          date | 당시 공개 evidence                                                                     | 가격 anchor                                                   | outcome                      |
| ------- | ----------------- | ------------: | ---------------------------------------------------------------------------------- | ----------------------------------------------------------- | ---------------------------- |
| T0      | awareness         |       2024-Q2 | Czech nuclear tender 기대                                                            | Doosan +48% over 3 months before/around event               | price moved on expectation   |
| T1      | Stage 2 evidence  |    2024-07-17 | KHNP preferred bidder, two reactors, first major overseas nuclear order since 2009 | Doosan +48%, KEPCO E&C +41%, KEPCO Plant +14% over 3 months | Stage2 but mostly pre-priced |
| T2      | Stage2-Actionable |    2024-07-17 | cost per unit 200B CZK / $8.65B, final contract targeted                           | full event OHLC unavailable                                 | candidate                    |
| T3      | 4C-watch          |    2024-09-03 | Westinghouse/EDF appeals start                                                     | no price window                                             | legal watch                  |
| T4      | 4C-watch          | 2024-10-30/31 | watchdog block/rejection but decisions not final                                   | no price window                                             | legal watch                  |
| T5      | 4C-watch          |    2025-05-06 | Czech court blocks signing of at least $18B contract after EDF complaint           | no price window                                             | hard watch                   |
| T6      | hard 4C           |           N/A | final cancellation 없음                                                              | N/A                                                         | hard_4c_not_confirmed        |

Czech nuclear는 Stage2_promote라기보다는 **pre-pricing audit**가 핵심이다. Reuters는 KHNP preferred bidder 선정과 함께 Doosan Enerbility가 3개월간 +48%, KEPCO E&C가 +41%, KEPCO Plant S&E가 +14% 올랐다고 보도했다. 즉 공식 preferred bidder 발표 전부터 이미 가격은 상당 부분 움직였다. 이건 `price_moved_with_evidence_expectation`에 가깝다. 단순 rumor는 아니지만, final contract는 아니었다. ([Reuters][13])

그 뒤 Westinghouse/EDF appeal, Czech watchdog proceedings, 2025년 Czech court의 $18B signing halt가 이어졌다. 따라서 이 case는 Stage2-Actionable이라기보다 `Stage2 + legal_4C-watch`가 맞고, Stage3-Green은 final contract와 legal clearance 이후에만 가능하다. ([Reuters][14])

### Trigger price validation row

```json
{
  "case_id": "r1_loop15_czech_nuclear_doosan_trigger_grid",
  "symbols": "034020/052690/051600",
  "best_entry_trigger": "T0/T1_if_preferred_bidder_probability_scored",
  "trigger_date": "2024-07-17",
  "khnp_status": "preferred_bidder",
  "reactors": 2,
  "estimated_cost_per_unit_czk_bn": 200,
  "estimated_cost_per_unit_usd_bn": 8.65,
  "first_major_overseas_nuclear_order_since": 2009,
  "doosan_enerbility_3m_gain_pct": 48,
  "kepco_ec_3m_gain_pct": 41,
  "kepco_plant_se_3m_gain_pct": 14,
  "court_blocked_contract_value_usd_bn_min": 18,
  "legal_challenge_parties": ["Westinghouse", "EDF"],
  "final_contract_signed": false,
  "mfe_30d_90d_180d_1y": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "event_premium_with_legal_4C_watch",
  "stage_gate_correction": "preferred bidder can be Stage2-Actionable, but if most price move occurred before formal evidence, mark pre-pricing risk"
}
```

### 판정

```text
score_price_alignment = event_premium_legal_4C_watch
old_error = preferred bidder를 Stage3처럼 처리할 위험
new_rule = preferred bidder는 Stage2-Actionable까지, final contract/legal clearance 전 Green 금지
```

---

# 6. Trigger별 가격경로 검증 요약

| case                | best trigger     |                         entry anchor |    event MFE/MAE |         market-relative | full MFE/MAE | outcome                               |
| ------------------- | ---------------- | -----------------------------------: | ---------------: | ----------------------: | ------------ | ------------------------------------- |
| Hyundai Rotem       | T2/T3 2024-04-09 |                               41,300 |            +9.3% |                  +9.6pp | unavailable  | Stage2→Stage3-Yellow 승격               |
| LIG Nex1            | T3 2024-09-20    |                          unavailable |            +3.6% |                  +2.7pp | unavailable  | Stage2-Actionable                     |
| Hanwha Aerospace    | T1/T2 2024-07-09 |                          unavailable |            +5.0% |             unavailable | unavailable  | Stage3-Yellow + 4B overlay            |
| Shipbuilding basket | T1 2024-03-14    | SHI 9,210 / HAO 27,450 / HHI 122,900 | +16 / +13 / +11% | +15.5 / +12.5 / +10.5pp | unavailable  | Stage2-Actionable                     |
| LS Electric         | T2 2024-07-01    |                              208,500 |            -5.4% |             unavailable | unavailable  | evidence good, immediate fail, retest |
| Samsung E&A         | T1/T2 2024-04-03 |                               26,750 |            +8.5% |                  +9.9pp | unavailable  | Stage3-Yellow candidate               |
| Czech nuclear       | T0/T1 2024-07-17 |                          unavailable |   Doosan +48% 3M |             unavailable | unavailable  | pre-priced Stage2 + legal 4C          |

---

# 7. Case별 trigger 비교

## 가장 좋은 entry 후보

```text
1. Hyundai Rotem T2/T3:
   shipment + OP estimate beat + revenue contribution + relative strength.
   기존 Stage2를 Stage3-Yellow로 올려야 할 후보.

2. Samsung E&A T1/T2:
   $6B order + +8.5% relative move + target upside 30.8%.
   EPC execution gate 때문에 Green은 아니지만 Yellow 가능.

3. Shipbuilding basket T1:
   order momentum + newbuilding price index + backlog duration + broad sector relative strength.
   Stage2-Actionable 이상.

4. Hanwha Aerospace T1/T2:
   Romania order + backlog expansion.
   단, 2025년 4B dilution overlay 필수.
```

## 기존 점수표가 놓쳤을 가능성

```text
missed_structural_risk:
- Hyundai Rotem
- Shipbuilding basket
- Samsung E&A
- Hanwha Aerospace

기존 점수표는 이들을 Stage2 또는 success_candidate로 낮게 잡을 가능성이 컸다.
하지만 trigger-level로 보면 적어도 Stage2-Actionable 또는 Stage3-Yellow 후보였다.
```

## Stage3-Green이 너무 늦은 case

```text
Hyundai Rotem:
2025 Poland 2차 계약 signing만 Green으로 잡으면 2024 OP estimate / shipment trigger의 rerating을 놓친다.

Czech nuclear:
공식 preferred bidder 발표도 이미 상당히 pre-priced였기 때문에,
Green은 final contract 전까지 금지하되,
T0 expectation trigger를 따로 backtest해야 한다.
```

---

# 8. score-price alignment 판정

```text
aligned:
- 없음. full OHLC window가 없어 완전 aligned 확정은 보류.

Stage2_promote_candidate:
- Hyundai Rotem
- Shipbuilding basket
- Samsung E&A
- LIG Nex1 Iraq order
- LS Electric, 단 immediate price failed라 retest 필요

missed_structural:
- Hyundai Rotem 가능성 큼.
- Shipbuilding basket 가능성 있음.
- Hanwha Aerospace는 Stage3 + 4B overlay로 봐야 함.

event_premium:
- HD Hyundai Heavy / Mipo MASGA merger
- Czech nuclear preferred bidder
- LIG Nex1 combat-validation rally

evidence_good_but_price_failed:
- LS Electric 2024-07-01
- immediate event -5.4 despite target +87%

false_positive_score:
- 아직 직접 확정 없음.
- 단, Czech nuclear를 final contract 전 Green으로 주면 false positive 위험.
- LS Electric을 당일 가격만 보고 Green 주면 false positive 위험.

thesis_break / 4C-watch:
- Czech nuclear legal challenge.
- Hanwha Aerospace share-sale disclosure / dilution.
- Hanwha Ocean China sanctions는 R11/R1 cross-watch.
```

---

# 9. 점수비중 교정

## 올릴 축

```text
shipment_revenue_contribution +5
op_estimate_vs_consensus +5
relative_strength_on_evidence_day +5
backlog_duration_quality +4
pricing_power_index_or_ASP +4
target_price_revision_with_estimate_raise +3
export_contract_repeatability +4
stage3_plus_4b_overlay_handling +5
```

### 근거

Hyundai Rotem은 shipment + OP estimate + revenue contribution + relative strength가 동시에 붙었을 때 entry로 강했다. 이 조합은 단순 수주보다 훨씬 강하다. Samsung E&A는 mega-order + relative strength + target upside가 있어 Stage3-Yellow 후보였다. Shipbuilding basket은 order momentum에 pricing index와 backlog duration이 붙으면서 Stage2를 넘어섰다.

## 내릴 축

```text
order_value_only -5
preferred_bidder_only -4
mou_or_partnership_only -5
target_price_raise_without_price_strength -3
event_pop_without_margin_visibility -3
sector_hype_without_company_estimate -4
```

### 근거

Czech nuclear는 preferred bidder만으로 Green을 주면 위험하다. LS Electric은 target +87%였지만 당일 주가는 -5.4%였으므로, target revision만으로는 부족하다. HD HHI/HII MOU 같은 partnership은 Stage2 evidence지만 계약/매출이 아니면 Actionable까지 바로 올리면 안 된다.

---

# 10. Stage 2-Actionable 승격 조건

이번 R1 Loop 15 기준 shadow rule:

```text
Stage 2 evidence가 아래 중 3개 이상을 충족하면 Stage2-Actionable로 승격한다.

1. 실제 shipment / delivery / call-off / revenue contribution이 확인됨
2. OP estimate 또는 revenue forecast가 consensus 대비 20% 이상 상향 또는 beat 가능성 제시
3. 해당 trigger 당일 시장 대비 +5pp 이상 상대강도
4. backlog duration 또는 repeat order 가능성이 확인됨
5. ASP / price index / target price revision이 동시에 확인됨
6. 단순 MOU나 preferred bidder가 아니라 binding order 또는 delivery evidence임
```

적용 case:

```text
Hyundai Rotem T2/T3
Shipbuilding basket T1
Samsung E&A T1/T2
LIG Nex1 Iraq order T3
```

---

# 11. Stage 3-Yellow 조건

```text
Stage 3-Yellow는 아래 조합에서 부여한다.

- 수주/계약/출하/승인 중 하나가 실제로 확인됨
- OP/EPS/매출 기여가 숫자로 제시됨
- trigger 당일 상대강도가 강함
- 하지만 margin, cash collection, final delivery, legal clearance 중 하나가 남아 있음
```

이번 라운드 Stage3-Yellow 후보:

```text
Hyundai Rotem:
OP estimate + shipment + revenue contribution + price strength.
남은 gate: 2차 Poland 계약, 장기 delivery/margin.

Samsung E&A:
$6B order + strong relative move + target upside.
남은 gate: EPC execution margin / working capital.

Hanwha Aerospace:
Romania order + backlog growth.
남은 gate: dilution/capex/overheat overlay.

Shipbuilding basket:
order momentum + price index + backlog duration.
남은 gate: delivery margin / labor cost / steel cost.
```

---

# 12. Stage 3-Green 조건

```text
Stage 3-Green은 이번 라운드에서 확정하지 않는다.

Green을 주려면:
- trigger-level full OHLC에서 MFE_90D/180D가 우수하고 MAE가 얕아야 함
- earnings 또는 margin이 후속 실적으로 확인되어야 함
- 4B overlay가 있으면 sizing-down 조건이 같이 붙어야 함
```

즉 이번 R1 Loop 15는 Green 확정 라운드라기보다 **Yellow와 Stage2-Actionable을 새로 분리하는 라운드**다.

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- 6개월~1년 내 +60~100% 이상 급등 후 target downgrade 또는 Hold 전환
- YTD 2배 이상 상승 후 대규모 증자/CB/capital raise 발표
- event trigger가 operating margin보다 control/M&A/governance premium에 가까움
- 신규 order가 있어도 valuation 부담이 명확함
```

적용:

```text
LIG Nex1:
1H +69% 후 KB Hold downgrade, -11%.
하지만 이후 Iraq order가 나와서 full exit보다는 trim signal.

Hanwha Aerospace:
YTD 2배 이상 상승 후 3.6T won share sale, -13%.
이건 강한 4B success.

HD HHI/Mipo merger:
+11.3/+14.6%는 U.S. shipbuilding cooperation/MASGA 기대가 섞인 event premium.
Stage3가 아니라 4B-watch.
```

---

# 14. 4C hard gate 조건

```text
R1 hard 4C:
- signed contract collapse
- export license / sanctions / legal block
- major cost overrun / claim
- dilution financing after overheat
- preferred bidder cancellation
- final contract blocked by court/regulator
```

이번 R1 Loop 15에서 hard 4C 확정은 없다.

```text
hard_4c_not_confirmed = true
```

다만 watch는 있다.

```text
Czech nuclear:
legal challenge / contract signing block.

Hanwha Aerospace:
dilution/disclosure quality.

Shipbuilding:
China sanctions / U.S.-China maritime conflict, 별도 R11/R1 cross-watch.
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_224.md 요약

```md
# R1 Loop 15. Industrials / Orders / Infrastructure Trigger-level Price Validation

이번 라운드는 R1 Loop 15 trigger-level validation 첫 적용 라운드다.

핵심 결론:
- Hyundai Rotem is Stage2_promote_candidate / Stage3-Yellow candidate. On 2024-04-09, shares rose 9.3% to 41,300 won vs KOSPI -0.3% after KB estimated Q1 OP +85% YoY to 59.10B won, 33.1% above consensus, backed by 18 K2 tank shipments to Poland and 270B won K2 export revenue contribution. Waiting until the 2025 Poland contract signing would be too late.
- LIG Nex1 is Stage2-Actionable with 4B timing nuance. July 2024 4B signal was valid after 1H +69% and -11% downgrade reaction, but later Iraq $2.8B order and 2026 combat-validation rally show 4B should be trim, not hard exit, when order pipeline remains.
- Hanwha Aerospace is Stage3-Yellow + 4B overlay. Romania $1B K9/K10 order and backlog expansion from 5.1T won to around 30T won justify Stage3-Yellow candidate, but 2025 3.6T won share sale and -13% price reaction require dilution overlay.
- Shipbuilding basket is Stage2-Actionable. On 2024-03-14, Samsung Heavy +16%, Hanwha Ocean +13%, HD Hyundai Heavy +11% after South Korea took 50% of global shipbuilding orders, new global orders rose 18% YoY, and newbuilding price index rose. Orders + pricing + backlog duration should be promoted beyond simple Stage 2.
- LS Electric is evidence_good_but_price_failed then Stage2_promote_candidate. Daiwa raised target 87% to 280,000 won and forecast U.S. revenue share rising from below 5% in 2022 to 20% in 2024, but shares were -5.4% at 208,500 won. Needs full OHLC retest.
- Samsung E&A is Stage3-Yellow candidate. $6B Fadhili contract, +8.5% event move to 26,750 won vs KOSPI -1.4%, and target upside 30.8%; Green blocked by EPC execution, working-capital and completion-margin gates.
- Czech nuclear / Doosan is Stage2 + legal 4C-watch. Doosan +48%, KEPCO E&C +41% over three months before/around KHNP preferred-bidder news, but final contract and legal challenge remain.

Main calibration:
- Raise shipment_revenue_contribution, op_estimate_vs_consensus, relative_strength_on_evidence_day, backlog_duration_quality, pricing_power_index_or_ASP, export_contract_repeatability, stage3_plus_4b_overlay_handling.
- Lower order_value_only, preferred_bidder_only, MOU_only, target_price_raise_without_price_strength, event_pop_without_margin_visibility.
```

## docs/checkpoints/checkpoint_28a_round224_r1_loop15.md 요약

```md
# Checkpoint 28A Round 224 R1 Loop 15 Trigger-level Calibration

## 반영 내용
- R1 Loop 15부터 trigger-level validation 방식을 적용했다.
- case당 단일 stage date가 아니라 T0~T6 trigger 후보를 분리했다.
- Hyundai Rotem, LIG Nex1, Hanwha Aerospace, shipbuilding basket, LS Electric, Samsung E&A, Czech nuclear/Doosan을 검토했다.
- full adjusted OHLC window는 확보하지 못했으므로 reported event price / event return anchor 기반으로 price validation을 수행했다.
- OHLC 미확보를 이유로 Stage 후보를 강등하지 않고, price_data_unavailable_after_deep_search로 분리 기록했다.

## 핵심 보정
- Stage 2 evidence가 shipment, OP estimate beat, revenue contribution, market-relative strength를 동시에 갖추면 Stage2-Actionable 또는 Stage3-Yellow로 승격한다.
- Stage 3를 취소하지 않고 4B overlay를 병기한다.
- Preferred bidder / MOU / order value only는 Green 금지.
```

## data/e2r_case_library/cases_r1_loop15_round224.jsonl 초안

```jsonl
{"case_id":"r1_loop15_hyundai_rotem_k2_poland","symbol":"064350","company_name":"Hyundai Rotem","case_type":"Stage2_promote_candidate","primary_archetype":"DEFENSE_EXPORT_STAGE2_ACTIONABLE","best_trigger":"T2/T3","stage_candidate":"Stage3-Yellow","price_validation":{"entry_price_anchor_krw":41300,"event_mfe_pct":9.3,"kospi_same_context_pct":-0.3,"market_relative_return_pp":9.6,"op_estimate_yoy_growth_pct":85,"op_estimate_krw_bn":59.10,"consensus_op_krw_bn":44.40,"op_estimate_vs_consensus_pct":33.1,"poland_k2_revenue_krw_bn":270,"target_price_krw":47500,"target_upside_from_event_price_pct":15.0,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"missed_structural_risk","notes":"Shipment + OP estimate beat + revenue contribution + relative strength should promote Stage2 to Stage3-Yellow."}
{"case_id":"r1_loop15_lig_nex1_msam","symbol":"079550","company_name":"LIG Nex1","case_type":"Stage2_promote_candidate_4B_timing_audit","primary_archetype":"MISSILE_DEFENSE_ORDER_4B_TIMING","best_trigger":"T3","stage_candidate":"Stage2-Actionable","price_validation":{"iraq_order_value_krw_trn":3.71,"iraq_order_value_usd_bn":2.8,"event_mfe_pct":3.6,"kospi_same_context_pct":0.9,"market_relative_return_pp":2.7,"prior_4b_1h_gain_pct":69,"prior_4b_kospi_gain_pct":5.4,"prior_4b_event_mae_pct":-11,"prior_4b_close_price_krw":195700,"combat_validation_reported_gain_pct":47,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate_with_4B_overlay","notes":"4B should be sizing-down, not hard exit, when new order pipeline and combat validation remain."}
{"case_id":"r1_loop15_hanwha_aerospace_k9_backlog_dilution","symbol":"012450","company_name":"Hanwha Aerospace","case_type":"Stage3_Yellow_with_4B_overlay","primary_archetype":"DEFENSE_BACKLOG_DILUTION_OVERLAY","best_trigger":"T1/T2","stage_candidate":"Stage3-Yellow + 4B-watch","price_validation":{"romania_order_value_usd_bn":1.0,"k9_howitzers":54,"k10_resupply_vehicles":36,"backlog_end_2021_krw_trn":5.1,"backlog_march_2024_krw_trn":30,"backlog_growth_multiple":5.88,"event_mfe_pct":5.0,"share_sale_krw_trn":3.6,"share_sale_usd_bn":2.5,"offer_price_krw":605000,"discount_to_prior_close_pct":16,"share_sale_event_mae_pct":-13,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"aligned_if_stage3_plus_4b_overlay_allowed","notes":"Order/backlog can be Stage3-Yellow; dilution is 4B overlay, not Stage3 cancellation."}
{"case_id":"r1_loop15_shipbuilding_order_price_basket","symbol":"010140/042660/329180/010620","company_name":"Samsung Heavy / Hanwha Ocean / HD Hyundai Heavy / HD Hyundai Mipo","case_type":"Stage2_promote_candidate","primary_archetype":"SHIPBUILDING_BACKLOG_PRICE_STAGE2_ACTIONABLE","best_trigger":"T1","stage_candidate":"Stage2-Actionable_to_Stage3-Yellow","price_validation":{"samsung_heavy_event_mfe_pct":16,"samsung_heavy_event_price_krw":9210,"hanwha_ocean_event_mfe_pct":13,"hanwha_ocean_event_price_krw":27450,"hd_hhi_event_mfe_pct":11,"hd_hhi_event_price_krw":122900,"kospi_same_context_pct":0.5,"global_new_orders_yoy_pct":18,"korea_global_order_share_pct":50,"china_global_order_share_pct":41,"newbuilding_price_index":181.81,"backlog_duration_context_years":3,"hd_hhi_masga_event_mfe_pct":11.3,"hd_mipo_masga_event_mfe_pct":14.6,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate","notes":"Order momentum + ship-price index + backlog duration + sector relative strength should not remain plain Stage2."}
{"case_id":"r1_loop15_ls_electric_us_grid","symbol":"010120","company_name":"LS Electric","case_type":"evidence_good_but_price_failed_then_promote_candidate","primary_archetype":"GRID_EQUIPMENT_US_GROWTH_STAGE2_PROMOTE","best_trigger":"T2_pending_full_ohlc","stage_candidate":"Stage2_promote_candidate","price_validation":{"entry_price_anchor_krw":208500,"event_mae_pct":-5.4,"us_revenue_share_2022_pct":"below_5","us_revenue_share_2024_forecast_pct":20,"revenue_forecast_raise_2024_2026_pct":"4-22","target_price_before_krw":150000,"target_price_after_krw":280000,"target_raise_pct":86.7,"target_upside_from_event_price_pct":34.3,"gsu_transformer_demand_growth_2019_2025_pct":274,"substation_transformer_demand_growth_2019_2025_pct":116,"transformer_price_5y_growth_pct":80,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"inconclusive_but_promote_candidate","notes":"Immediate price failed, but structural U.S. grid trigger needs full-window retest before rejection."}
{"case_id":"r1_loop15_samsung_ena_fadhili","symbol":"028050","company_name":"Samsung E&A","case_type":"Stage3_Yellow_candidate","primary_archetype":"OVERSEAS_EPC_ORDER_STAGE2_YELLOW","best_trigger":"T1/T2","stage_candidate":"Stage3-Yellow","price_validation":{"entry_price_anchor_krw":26750,"event_mfe_pct":8.5,"kospi_same_context_pct":-1.4,"market_relative_return_pp":9.9,"contract_value_usd_bn":6.0,"project_total_value_usd_bn":7.7,"gas_capacity_increase_pct":60,"sulfur_production_increase_tpd":2300,"completion_target":"2027-11","target_price_krw":35000,"target_upside_from_event_price_pct":30.8,"green_gate_missing":["advance_payment","cost_lock_in","working_capital","completion_margin"],"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate","notes":"Mega-order + relative strength + target upside supports Stage3-Yellow, not Green."}
{"case_id":"r1_loop15_czech_nuclear_doosan","symbol":"034020/052690/051600","company_name":"Doosan Enerbility / KEPCO E&C / KEPCO Plant S&E","case_type":"event_premium_legal_4c_watch","primary_archetype":"NUCLEAR_EXPORT_PREFERRED_BIDDER_STAGE2","best_trigger":"T0/T1","stage_candidate":"Stage2-Actionable_with_legal_watch","price_validation":{"khnp_status":"preferred_bidder","reactors":2,"estimated_cost_per_unit_czk_bn":200,"estimated_cost_per_unit_usd_bn":8.65,"doosan_enerbility_3m_gain_pct":48,"kepco_ec_3m_gain_pct":41,"kepco_plant_se_3m_gain_pct":14,"court_blocked_contract_value_usd_bn_min":18,"final_contract_signed":false,"legal_challenge_parties":["Westinghouse","EDF"],"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_legal_4C_watch","notes":"Preferred bidder is Stage2-Actionable at most; final contract/legal clearance needed for Green."}
```

## data/e2r_trigger_calibration/triggers_r1_loop15_round224.jsonl 초안

```jsonl
{"trigger_id":"r1l15_hyundai_rotem_T2","case_id":"r1_loop15_hyundai_rotem_k2_poland","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-09","evidence_available":"18 K2 shipments to Poland, Q1 OP estimate +85% YoY, consensus beat, 270B won export revenue contribution","entry_price_krw":41300,"event_return_pct":9.3,"market_relative_return_pp":9.6,"trigger_outcome_label":"excellent_stage2_promote_candidate","promote_to":"Stage3-Yellow"}
{"trigger_id":"r1l15_lig_nex1_T2","case_id":"r1_loop15_lig_nex1_msam","trigger_type":"4B-watch","trigger_date":"2024-07-02","evidence_available":"1H share gain 69%, KOSPI 5.4%, downgrade to Hold","entry_price_krw":195700,"event_return_pct":-11,"trigger_outcome_label":"4B_valid_but_not_hard_exit","promote_to":"4B_trim"}
{"trigger_id":"r1l15_lig_nex1_T3","case_id":"r1_loop15_lig_nex1_msam","trigger_type":"Stage2-Actionable","trigger_date":"2024-09-20","evidence_available":"Iraq 3.71T won / $2.8B Cheongung-II order after Saudi $3.2B order","event_return_pct":3.6,"market_relative_return_pp":2.7,"trigger_outcome_label":"good_entry_candidate","promote_to":"Stage2-Actionable"}
{"trigger_id":"r1l15_hanwha_aero_T1","case_id":"r1_loop15_hanwha_aerospace_k9_backlog_dilution","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-09","evidence_available":"Romania $1B K9/K10 order, backlog 5.1T to 30T won","event_return_pct":5.0,"trigger_outcome_label":"Stage3_Yellow_candidate","promote_to":"Stage3-Yellow"}
{"trigger_id":"r1l15_hanwha_aero_T4","case_id":"r1_loop15_hanwha_aerospace_k9_backlog_dilution","trigger_type":"4B-watch","trigger_date":"2025-03-21","evidence_available":"3.6T won share sale, 605,000 won issue price, 16% discount, YTD more than doubled","event_return_pct":-13,"trigger_outcome_label":"4B_success_dilution_overlay","promote_to":"4B"}
{"trigger_id":"r1l15_shipbuilding_T1","case_id":"r1_loop15_shipbuilding_order_price_basket","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-14","evidence_available":"global shipbuilding orders +18% YoY, Korea 50% share, newbuilding price index up, 3-year backlog","event_return_pct":"Samsung Heavy +16 / Hanwha Ocean +13 / HD HHI +11","market_relative_return_pp":"15.5/12.5/10.5","trigger_outcome_label":"Stage2_promote_candidate","promote_to":"Stage3-Yellow_candidate"}
{"trigger_id":"r1l15_ls_electric_T2","case_id":"r1_loop15_ls_electric_us_grid","trigger_type":"Stage2-Actionable_candidate","trigger_date":"2024-07-01","evidence_available":"U.S. revenue share forecast 20%, revenue forecast raised 4-22%, target raised 87%","entry_price_krw":208500,"event_return_pct":-5.4,"trigger_outcome_label":"evidence_good_but_price_failed_retest_required","promote_to":"pending_full_ohlc"}
{"trigger_id":"r1l15_samsung_ena_T2","case_id":"r1_loop15_samsung_ena_fadhili","trigger_type":"Stage3-Yellow_candidate","trigger_date":"2024-04-03","evidence_available":"$6B Fadhili order, +60% gas capacity, target upside 30.8%, event relative +9.9pp","entry_price_krw":26750,"event_return_pct":8.5,"market_relative_return_pp":9.9,"trigger_outcome_label":"Stage3_Yellow_candidate","promote_to":"Stage3-Yellow"}
{"trigger_id":"r1l15_czech_nuclear_T1","case_id":"r1_loop15_czech_nuclear_doosan","trigger_type":"Stage2-Actionable_with_legal_watch","trigger_date":"2024-07-17","evidence_available":"KHNP preferred bidder, two reactors, first large overseas nuclear order since 2009, related names already +14 to +48 over 3 months","event_return_pct":"Doosan +48 3M / KEPCO E&C +41 3M / KEPCO Plant +14 3M","trigger_outcome_label":"prepriced_event_premium_with_legal_4c_watch","promote_to":"Stage2-Actionable_only"}
```

## data/sector_taxonomy/score_weight_profiles_round224_r1_loop15_v1.csv 초안

```csv
archetype,shipment_revenue_contribution,op_estimate_vs_consensus,relative_strength_on_evidence_day,backlog_duration_quality,pricing_power_index_or_asp,target_revision_with_estimate_raise,export_contract_repeatability,stage3_plus_4b_overlay_handling,order_value_only_penalty,preferred_bidder_only_penalty,mou_only_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
DEFENSE_EXPORT_STAGE2_ACTIONABLE,+5,+5,+5,+4,+2,+3,+5,+4,-5,-3,-5,shipment+OP beat+relative strength,delivery+margin pending,delivery+margin+cash collection,Hyundai Rotem trigger should promote Stage2 to Stage3-Yellow.
MISSILE_DEFENSE_ORDER_4B_TIMING,+3,+3,+4,+4,+2,+2,+5,+5,-4,-3,-5,repeat export order+relative strength,combat validation pending,delivery+margin+follow-on orders,LIG 4B should be trim if new orders remain.
DEFENSE_BACKLOG_DILUTION_OVERLAY,+3,+4,+4,+5,+2,+2,+5,+5,-4,-3,-5,order+backlog expansion,strong backlog but dilution risk,delivery+cash+no dilution,Hanwha Aerospace requires Stage3 plus 4B overlay.
SHIPBUILDING_BACKLOG_PRICE_STAGE2_ACTIONABLE,+2,+2,+5,+5,+5,+2,+4,+3,-4,-2,-5,orders+price index+backlog duration,margin/labor/steel pending,delivery margin confirmed,Shipbuilding basket trigger should be promoted.
GRID_EQUIPMENT_US_GROWTH_STAGE2_PROMOTE,+2,+3,+3,+4,+5,+4,+3,+2,-4,-2,-5,US revenue mix+forecast raise+target revision,needs price confirmation,margin+backlog+capacity,LS Electric needs full-window retest after immediate price fail.
OVERSEAS_EPC_ORDER_STAGE2_YELLOW,+2,+2,+5,+4,+2,+3,+3,+3,-5,-3,-5,large order+relative strength+target upside,advance payment/cost lock pending,completion margin+cash collection,Samsung E&A supports Yellow not Green.
NUCLEAR_EXPORT_PREFERRED_BIDDER_STAGE2,+1,+1,+2,+4,+1,+2,+3,+2,-4,-5,-5,preferred bidder+project scale,legal/final contract pending,final contract+legal clearance+C/F visibility,Czech nuclear should not become Green before contract.
```

---

# 이번 R1 Loop 15 결론

```text
1. Hyundai Rotem은 이번 라운드의 핵심 missed_structural 후보다.
   2024-04-09의 OP estimate + shipment + revenue contribution + relative strength는 Stage2가 아니라 Stage3-Yellow급이다.

2. LIG Nex1은 Stage2-Actionable + 4B timing case다.
   2024-07 4B는 맞았지만 hard exit가 아니라 trim이어야 했고, Iraq order는 Stage2-Actionable로 봐야 한다.

3. Hanwha Aerospace는 Stage3 + 4B overlay 구조다.
   backlog/order는 강하지만, dilution shock 때문에 4B를 별도로 얹어야 한다.

4. Shipbuilding basket은 Stage2_promote_candidate다.
   수주, 선가, backlog duration, sector relative strength가 동시에 나오면 plain Stage2로 두면 늦다.

5. LS Electric은 evidence_good_but_price_failed이지만 retest가 필요하다.
   당일 -5.4% 때문에 버리면 안 되고, U.S. grid shortage theme의 forward MFE/MAE를 full OHLC로 다시 봐야 한다.

6. Samsung E&A는 Stage3-Yellow 후보다.
   $6B order와 상대강도는 강하지만, EPC execution margin이 남아 Green은 아니다.

7. Czech nuclear는 Stage2 + legal 4C-watch다.
   preferred bidder는 Actionable일 수 있지만, final contract와 legal clearance 전에는 Green이 아니다.
```

한 문장으로 압축하면:

> **R1 Loop 15에서 새로 배운 핵심은 “수주 자체”가 아니라, 수주·출하·OP estimate·매출기여·가격 상대강도가 동시에 닫히면 Stage2를 Stage3-Yellow로 올려야 한다는 것이다. 반대로 preferred bidder, MOU, order value only는 여전히 Green 금지다.**

[1]: https://www.wsj.com/articles/hyundai-rotem-rallies-on-hopes-tank-exports-will-boost-earnings-9322d840 "https://www.wsj.com/articles/hyundai-rotem-rallies-on-hopes-tank-exports-will-boost-earnings-9322d840"
[2]: https://www.reuters.com/markets/emerging/poland-signs-contract-buy-more-south-korean-battle-tanks-2025-08-01/ "https://www.reuters.com/markets/emerging/poland-signs-contract-buy-more-south-korean-battle-tanks-2025-08-01/"
[3]: https://www.marketwatch.com/story/lig-nex1-s-recent-surge-could-be-burden-for-future-gains-market-talk-662f12b3 "https://www.marketwatch.com/story/lig-nex1-s-recent-surge-could-be-burden-for-future-gains-market-talk-662f12b3"
[4]: https://www.reuters.com/business/aerospace-defense/south-koreas-lig-nex1-wins-28-bln-deal-with-iraq-export-missile-systems-2024-09-19/ "https://www.reuters.com/business/aerospace-defense/south-koreas-lig-nex1-wins-28-bln-deal-with-iraq-export-missile-systems-2024-09-19/"
[5]: https://www.ft.com/content/658c8411-df02-4b5e-a69d-2029114e4ca1 "https://www.ft.com/content/658c8411-df02-4b5e-a69d-2029114e4ca1"
[6]: https://www.reuters.com/business/aerospace-defense/south-koreas-hanwha-aerospace-wins-1-bln-order-romania-k9-howitzers-2024-07-09/ "https://www.reuters.com/business/aerospace-defense/south-koreas-hanwha-aerospace-wins-1-bln-order-romania-k9-howitzers-2024-07-09/"
[7]: https://www.ft.com/content/994a0a80-414f-442f-bf41-f2dbde5a04ca "https://www.ft.com/content/994a0a80-414f-442f-bf41-f2dbde5a04ca"
[8]: https://www.wsj.com/articles/south-korean-shipbuilders-rally-on-brisk-contract-wins-d44ecb8a "https://www.wsj.com/articles/south-korean-shipbuilders-rally-on-brisk-contract-wins-d44ecb8a"
[9]: https://www.reuters.com/markets/emerging/south-korean-shipbuilder-hd-hyundai-heavy-merge-with-affiliate-hd-hyundai-mipo-2025-08-27/ "https://www.reuters.com/markets/emerging/south-korean-shipbuilder-hd-hyundai-heavy-merge-with-affiliate-hd-hyundai-mipo-2025-08-27/"
[10]: https://www.marketwatch.com/story/ls-electric-could-gain-from-solid-u-s-business-growth-opportunity-market-talk-3e926067 "https://www.marketwatch.com/story/ls-electric-could-gain-from-solid-u-s-business-growth-opportunity-market-talk-3e926067"
[11]: https://www.reuters.com/business/energy/us-power-transformer-buyers-scramble-imports-factory-slots--reeii-2026-05-11/ "https://www.reuters.com/business/energy/us-power-transformer-buyers-scramble-imports-factory-slots--reeii-2026-05-11/"
[12]: https://www.wsj.com/articles/samsung-e-a-shares-rise-on-6-billion-saudi-contract-win-10a5b2f4 "https://www.wsj.com/articles/samsung-e-a-shares-rise-on-6-billion-saudi-contract-win-10a5b2f4"
[13]: https://www.reuters.com/business/energy/south-koreas-winning-bid-czech-nuclear-power-project-2024-07-17/ "https://www.reuters.com/business/energy/south-koreas-winning-bid-czech-nuclear-power-project-2024-07-17/"
[14]: https://www.reuters.com/business/energy/czech-watchdog-starts-proceedings-appeals-against-nuclear-power-tender-2024-09-03/ "https://www.reuters.com/business/energy/czech-watchdog-starts-proceedings-appeals-against-nuclear-power-tender-2024-09-03/"

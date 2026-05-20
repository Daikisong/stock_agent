순서상 이번은 **R5 Loop 16 — 소비재·유통·브랜드 trigger-level price validation 라운드**다.

이번 R5는 “K-food 좋다 / K-beauty 좋다 / 중국 관광객 온다 / 유통 재편된다”가 아니라, **수출 ASP·출하·생산능력·오프라인 채널 입점·고객 신뢰·보안 사고·M&A/JV·가격규제**가 실제 매출·마진·재구매로 이어지는지 따로 봐야 한다.

```text
round = R5 Loop 16
round_id = round_241
large_sector = CONSUMER_RETAIL_BRANDS
method = trigger_level_backtest_v1_after_redteam
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R6 Loop 16
```

이번 세션에서도 KRX 수정주가 일봉 OHLC를 직접 계산 가능한 형태로 확보하지 못했다. finance tool은 KRX ticker를 처리하지 못했고, Yahoo chart endpoint 직접 조회도 실패했다. 그래서 full MFE/MAE는 만들지 않고 `price_data_unavailable_after_deep_search`로 둔다. 대신 Reuters/FT/MarketWatch/Barron’s가 보도한 **event return, event price, 사용자·매출·수출·채널·정책 trigger**를 가격 anchor로 사용한다. 숫자를 만들지 않고, Stage 판정과 OHLC backfill 상태를 분리한다.

---

# 1. 이번 라운드 대섹터

```text
R5 = 소비재·유통·브랜드
```

R5의 core gate는 아래다.

```text
K-food:
수출 증가 → ASP 상승 → 생산능력 → 국가별 shipment → OP estimate → 반복 수요 → 관세/원가

K-beauty:
SNS viral → e-commerce sales → 오프라인 retailer 입점 → 재구매율 → 브랜드 margin → tariff/포화 리스크

뷰티 디바이스:
인플루언서/셀럽 trigger → 해외 매출 비중 → device ASP → repeat consumables → valuation overheat

면세·관광·호텔:
비자/중국 관광객 정책 → 입국자 수 → 객단가 → 면세점/호텔/백화점 매출 → 마진

이커머스:
고객 신뢰 → MAU/DAU → GMV/spending → 배송 경쟁력 → 보안 사고 → 규제/벌금

오프라인 유통:
구조조정 / JV / sale → traffic → margin → debt restructuring → liquidation risk

가격규제:
식품 가격·용량 규제 → ASP pass-through → margin squeeze → 소비자 신뢰
```

---

# 2. 대상 canonical archetype

```text
KFOOD_EXPORT_ASP_CAPACITY_STAGE3_YELLOW
KBEAUTY_US_CHANNEL_STAGE2_ACTIONABLE
BEAUTY_DEVICE_VIRAL_STAGE2_WITH_OVERHEAT_4B
CHINA_TOURISM_DUTYFREE_STAGE2_EVENT
ECOMMERCE_SECURITY_TRUST_4C_AND_RIVAL_STAGE2
RETAIL_PLATFORM_JV_STAGE2_WITH_INTEGRATION_4B
OFFLINE_GROCERY_RESTRUCTURING_HARD_4C
SHRINKFLATION_PRICE_REGULATION_4C_WATCH
```

---

# 3. deep sub-archetype

```text
Samyang Foods / Buldak:
- Kiwoom 2Q OP estimate 81.2B won
- OP estimate +84% YoY
- Buldak ASP 상승
- U.S./Europe shipment 증가
- 생산능력 확대
- shares +5.7%, close 647,000 won
- target price +26% to 830,000 won
- Stage2-Actionable / Stage3-Yellow candidate

K-beauty / U.S. channel:
- Korea surpassed France as biggest cosmetics exporter to U.S. in 2024
- Korean top-five U.S. e-commerce beauty brands average online sales +71% over two years
- French top-five +15%
- d'Alba shares more than doubled since debut
- Tirtir / d'Alba / Torriden / Beauty of Joseon negotiating or launching in Ulta, Sephora, Target, Costco
- Cosmax/Kolmar as outsourced ODM backbone
- Stage2-Actionable, but tariff/physical-store sell-through gate

APR / Medicube beauty device:
- APR stock more than four-fold since January
- market value around $6B
- beauty device promoted by Kylie Jenner
- nearly 80% of Q2 2025 revenue overseas
- device around one-third of U.S. sales
- Stage2 structural, but valuation/celebrity overheat 4B

China tourist visa-free / duty-free:
- Chinese group visa-free entry from Sep 29, 2025 to Jun 2026
- Hyundai Department Store +7.1%
- Hotel Shilla +4.8%
- Paradise +2.9%
- Hankook Cosmetics +9.9%
- Stage2 tourism demand event, not Green until visitor spending/margin

Coupang breach / retail share shift:
- Coupang breach affected around 34M users
- Coupang mobile MAU -3.5% Jan vs Nov
- average daily consumer spending -6.3% to 139.2B won
- Naver online users +23%
- CJ Logistics overnight/one-day volume +120% in Q4
- Coupang shares down around 34% since breach
- platform security hard 4C + rival Stage2 opportunity

Shinsegae/E-Mart + Alibaba:
- Shinsegae/E-Mart to set JV with Alibaba International
- Gmarket 100% stake contributed
- AliExpress Korea + Gmarket in JV
- Korea e-commerce is world’s fourth-largest
- Gmarket struggling against Coupang, Naver, AliExpress, Temu
- Stage2 platform JV, integration/regulatory 4B

Homeplus:
- court-led restructuring after liquidity stress and e-commerce competition
- liquidation value higher than going-concern value
- liquidation value 3.7T won, total assets 6.8T won
- MBK to write off 2.5T won shares
- offline grocery hard 4C reference

Shrinkflation / processed foods:
- KFTC labels undisclosed downsizing as unfair transaction
- rule from Aug 2024
- fines 5M won first offence, 10M won second
- examples include CJ CheilJedang sausage weight -12.5%
- food/household ASP hidden price increase 4C-watch
```

---

# 4. 선정 case 요약

| bucket                                       | case                                                   | 핵심 판정                                                                                                    |
| -------------------------------------------- | ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| structural_success / Stage3-Yellow candidate | Samyang Foods / Buldak                                 | ASP + U.S./Europe shipment + capacity + OP estimate +84%, shares +5.7%. 기존 Stage2로만 두면 missed_structural |
| Stage2-Actionable                            | K-beauty U.S. channel / d’Alba / ODM                   | U.S. cosmetics export leadership, top-five K-beauty e-commerce +71%, d’Alba >2x since debut              |
| Stage2 + overheat 4B                         | APR / Medicube beauty device                           | APR stock >4x since January, $6B value, overseas revenue near 80%. Celebrity/device hype 4B              |
| Stage2 tourism event                         | China visa-free / duty-free / department / cosmetics   | Hyundai Dept +7.1%, Hotel Shilla +4.8%, Hankook Cosmetics +9.9%. 실제 객단가/margin 전에는 Green 아님              |
| hard 4C + rival Stage2                       | Coupang breach / Naver-E-Mart-CJ Logistics opportunity | Coupang -34% since breach, MAU/spending decline, Naver users +23%, CJ shipment +120%                     |
| Stage2 JV + 4B                               | Shinsegae/E-Mart + Alibaba/Gmarket                     | Gmarket·AliExpress JV. 플랫폼 재편은 Stage2, integration/competition 4B                                        |
| hard 4C                                      | Homeplus restructuring                                 | liquidation value > going concern, 3.7T won liquidation value, MBK 2.5T won write-off                    |
| 4C-watch                                     | Shrinkflation price regulation                         | food/household downsizing disclosure rule, fines, CJ product example. hidden ASP pass-through 제한         |

---

# 5. Case별 trigger grid

## Case A — Samyang Foods / Buldak export, ASP, capacity

```text
symbol = 003230
case_type = structural_success / Stage3-Yellow candidate
archetype = KFOOD_EXPORT_ASP_CAPACITY_STAGE3_YELLOW
```

| trigger |                    type | date       | 당시 공개 evidence                                                             | 가격 anchor                       | outcome          |
| ------- | ----------------------: | ---------- | -------------------------------------------------------------------------- | ------------------------------- | ---------------- |
| T0      |               awareness | 2023~2024  | Buldak global viral demand, U.S./Europe shipment momentum                  | no trigger price                | Stage1           |
| T1      |       Stage2-Actionable | 2024-06-14 | Kiwoom raises 2Q OP estimate to 81.2B won, +84% YoY                        | shares +5.7%, close 647,000 won | excellent entry  |
| T2      | Stage3-Yellow candidate | 2024-06-14 | ASP 상승 + U.S./Europe shipment 증가 + production capacity 확대                  | target +26% to 830,000 won      | Yellow candidate |
| T3      |                4B-watch | 2024~      | single-product concentration, tariff, raw material cost, channel inventory | no full OHLC                    | 4B               |
| T4      |            Stage3-Green | N/A        | full OHLC + repeated quarterly margin unavailable                          | no Green                        | 보류               |

Samyang은 R5에서 가장 강한 Stage2→Yellow template이다. Kiwoom은 Buldak 수출 호조로 2Q operating profit estimate를 81.2B won, 전년 대비 +84%로 올렸고, 근거는 U.S./Europe shipment 증가, ASP 상승, 생산능력 확대였다. 같은 보도에서 Samyang shares는 +5.7%로 647,000 won에 마감했고, target price는 +26% 오른 830,000 won이었다. 이 조합은 단순 K-food theme가 아니라 **ASP + shipment + capacity + OP estimate + price reaction**이 동시에 닫힌 trigger다. ([마켓워치][1])

```json
{
  "case_id": "r5_loop16_samyang_buldak_export",
  "symbol": "003230",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable_to_Stage3-Yellow_candidate",
  "trigger_date": "2024-06-14",
  "op_estimate_2q_krw_bn": 81.2,
  "op_estimate_yoy_pct": 84,
  "event_return_pct": 5.7,
  "entry_price_anchor_krw": 647000,
  "target_price_krw": 830000,
  "target_price_raise_pct": 26,
  "evidence_bridge": [
    "Buldak_ASP_increase",
    "U.S._Europe_shipment_growth",
    "production_capacity_expansion",
    "OP_estimate_revision"
  ],
  "stage3_gate_missing": [
    "full_OHLC_MFE_MAE",
    "repeat_quarter_export_margin",
    "channel_inventory",
    "raw_material_cost_pass_through",
    "single_product_concentration"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_stage2_to_yellow_candidate"
}
```

---

## Case B — K-beauty U.S. channel / d’Alba / Cosmax·Kolmar ODM backbone

```text
symbols = 483650 / 257720 / 192820 / 161890 / 090430
case_type = Stage2-Actionable / channel expansion
archetype = KBEAUTY_US_CHANNEL_STAGE2_ACTIONABLE
```

| trigger |              type | date       | 당시 공개 evidence                                                                                  | 가격 anchor                     | outcome            |
| ------- | ----------------: | ---------- | ----------------------------------------------------------------------------------------------- | ----------------------------- | ------------------ |
| T0      |         awareness | 2024       | Korea surpasses France as biggest cosmetics exporter to U.S.                                    | no individual price           | Stage1             |
| T1      | Stage2-Actionable | 2025-06-05 | top-five Korean U.S. e-commerce beauty brands average online sales +71% over two years          | d’Alba shares >2x since debut | Stage2-Actionable  |
| T2      | Stage2 validation | 2025-06-05 | Tirtir, d’Alba, Torriden, Beauty of Joseon in talks/launches with Ulta, Sephora, Costco, Target | no full OHLC                  | channel validation |
| T3      |          4B-watch | 2025~      | U.S. tariff, China weakness, e-commerce saturation, need physical-store sell-through            | no OHLC                       | 4B                 |
| T4      |     Stage3-Yellow | N/A        | store sell-through, repeat order, listed-company margin not yet confirmed                       | no Yellow                     | 보류                 |

K-beauty는 R5에서 구조적 Stage2-Actionable이다. South Korea는 2024년 U.S. cosmetics exporter 1위로 France를 제쳤고, top-five Korean beauty brands in U.S. e-commerce는 최근 2년 평균 +71% 성장해 전체 U.S. market +21%, top-five French brands +15%를 앞섰다. d’Alba Global shares는 debut 이후 두 배 넘게 올랐고, Tirtir·d’Alba·Torriden·Beauty of Joseon은 Ulta, Sephora, Costco, Target 같은 physical retailers와 입점 또는 출시를 추진 중이다. 다만 Reuters는 tariffs, China export decline, saturation, physical-store sales durability가 gate라고 지적한다. ([Reuters][2])

```json
{
  "case_id": "r5_loop16_kbeauty_us_channel",
  "symbols": "483650/257720/192820/161890/090430",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable_with_4B_channel_gate",
  "trigger_date": "2025-06-05",
  "korea_us_cosmetics_export_rank_2024": 1,
  "top5_korean_us_ecommerce_growth_2y_pct": 71,
  "overall_us_market_growth_2y_pct": 21,
  "top5_french_brands_growth_2y_pct": 15,
  "dalba_post_debut_return": ">100%",
  "retailers": [
    "Ulta",
    "Sephora",
    "Costco",
    "Target"
  ],
  "odm_backbone": [
    "Cosmax",
    "Kolmar"
  ],
  "stage3_gate_missing": [
    "physical_store_sell_through",
    "repeat_orders",
    "brand_specific_margin",
    "tariff_pass_through",
    "China_decline_offset",
    "inventory_turnover"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_Actionable_channel_expansion"
}
```

---

## Case C — APR / Medicube beauty device viral growth

```text
symbol = 278470
case_type = Stage2 structural + overheat 4B
archetype = BEAUTY_DEVICE_VIRAL_STAGE2_WITH_OVERHEAT_4B
```

| trigger |              type | date            | 당시 공개 evidence                                                                                              | 가격 anchor             | outcome    |
| ------- | ----------------: | --------------- | ----------------------------------------------------------------------------------------------------------- | --------------------- | ---------- |
| T0      |         awareness | 2024 IPO / 2025 | Medicube beauty device global traction                                                                      | no single event price | Stage1     |
| T1      |   Stage2 evidence | 2025-10-20      | APR stock >4x since January, market value around $6B                                                        | >4x YTD/source-period | Stage2     |
| T2      | Stage2 validation | 2025-10-20      | skincare device promoted by Kylie Jenner; device about one-third U.S. sales; Q2 overseas revenue nearly 80% | no OHLC               | validation |
| T3      |          4B-watch | 2025~           | celebrity/viral concentration, device replacement cycle, tariff/regulation, valuation                       | no OHLC               | overheat   |
| T4      |     Stage3-Yellow | N/A             | recurring consumables, repeat device cycle, margin durability not confirmed                                 | no Yellow             | 보류         |

APR은 “K-beauty brand”라기보다 **beauty device + viral commerce + overseas revenue** case다. FT는 APR stock이 January 이후 네 배 넘게 올랐고, market value가 약 $6B에 달했다고 보도했다. 성장은 Kylie Jenner가 홍보한 $180 skincare gadget, Q2 2025 revenue의 거의 80%가 overseas에서 발생했다는 점, device가 U.S. sales의 약 3분의 1을 차지했다는 점이 핵심이다. 다만 이건 celebrity/viral trigger와 valuation overheat를 동반하므로 Stage2 structural + 4B overlay가 맞다. ([Financial Times][3])

```json
{
  "case_id": "r5_loop16_apr_medicube_beauty_device",
  "symbol": "278470",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2_structural_with_4B_overheat",
  "trigger_date": "2025-10-20",
  "stock_return_since_january": ">4x",
  "market_value_usd_bn": 6,
  "device_price_usd_context": 180,
  "q2_2025_overseas_revenue_share_pct": "~80",
  "device_share_of_us_sales_pct": "~33",
  "celebrity_trigger": "Kylie_Jenner_TikTok",
  "stage3_gate_missing": [
    "repeat_device_purchase_cycle",
    "consumables_or_recurring_revenue",
    "gross_margin_durability",
    "tariff_absorption",
    "channel_inventory",
    "valuation_multiple_absorption"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_structural_but_overheat_4B"
}
```

---

## Case D — China tourist visa-free / duty-free, department stores, cosmetics

```text
symbols = 069960 / 008770 / 034230 / 123690
company_scope = Hyundai Department Store / Hotel Shilla / Paradise / Hankook Cosmetics
case_type = Stage2 tourism demand event
archetype = CHINA_TOURISM_DUTYFREE_STAGE2_EVENT
```

| trigger |                    type | date       | 당시 공개 evidence                                                                                              | 가격 anchor                                                                       | outcome    |
| ------- | ----------------------: | ---------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ---------- |
| T0      |           Stage2 policy | 2025-03-20 | South Korea says it will offer temporary visa waiver for Chinese visitors in Q3                             | no specific stock return                                                        | Stage2     |
| T1      | Stage2-Actionable event | 2025-08-06 | visa-free Chinese tourist groups from Sep 29, 2025 to Jun 2026                                              | Hyundai Dept +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9% | Actionable |
| T2      |              validation | 2025-09-29 | pilot begins, Chinese groups of 3+ can stay 15 days visa-free; Shilla cruise tour, Baemin Alipay/WeChat Pay | no stock return                                                                 | validation |
| T3      |                4B-watch | 2025~2026  | anti-Chinese rallies, tourist safety/image risk, actual spending unknown                                    | no OHLC                                                                         | 4B         |
| T4      |           Stage3-Yellow | N/A        | visitor traffic, per-capita spend, duty-free margin not confirmed                                           | no Yellow                                                                       | 보류         |

중국 단체관광 비자면제는 R5의 강한 tourism Stage2 event다. South Korea는 2025년 9월 29일부터 2026년 6월까지 mainland China tourist groups에 visa-free entry를 제공하기로 했고, 발표 당일 Hyundai Department Store +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9%가 나왔다. 이는 policy-to-price alignment가 명확하다. 하지만 실제 Stage3는 visitor count, 객단가, 면세점 margin, hotel occupancy가 확인돼야 한다. ([Reuters][4])

프로그램은 2025년 9월 29일 시작됐고, 중국 mainland tourist group 3명 이상은 15일간 visa-free로 체류할 수 있다. Shilla Duty Free는 Chinese cruise tour를 조직했고, Baedal Minjok은 Alipay/WeChat Pay 결제를 도입했다는 Reuters 보도도 있어 수혜 채널이 실제로 움직이고 있다. ([Reuters][5])

```json
{
  "case_id": "r5_loop16_china_visa_free_tourism_retail",
  "symbols": "069960/008770/034230/123690",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable_tourism_event",
  "policy_announcement_date": "2025-08-06",
  "pilot_start_date": "2025-09-29",
  "pilot_end_date": "2026-06",
  "visa_free_stay_days": 15,
  "hyundai_department_store_event_return_pct": 7.1,
  "hotel_shilla_event_return_pct": 4.8,
  "paradise_event_return_pct": 2.9,
  "hankook_cosmetics_event_return_pct": 9.9,
  "stage3_gate_missing": [
    "actual_chinese_arrivals",
    "per_capita_spending",
    "duty_free_sales",
    "hotel_occupancy",
    "casino_drop_amount",
    "cosmetics_sell_through"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_tourism_event_not_Green"
}
```

---

## Case E — Coupang breach / Naver·E-Mart·CJ Logistics rival opportunity

```text
symbols = CPNG / 035420 / 139480 / 000120
company_scope = Coupang / Naver / E-Mart / CJ Logistics
case_type = hard 4C + rival Stage2
archetype = ECOMMERCE_SECURITY_TRUST_4C_AND_RIVAL_STAGE2
```

| trigger |          type | date       | 당시 공개 evidence                                                                       | 가격 anchor                                                        | outcome                  |
| ------- | ------------: | ---------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------- | ------------------------ |
| T0      |       hard 4C | 2025-12-01 | Coupang data breach affects 33.7M accounts                                           | Coupang -4.4% premarket / later -5% overnight in Reuters context | hard 4C                  |
| T1      | 4C validation | 2026-02-25 | Coupang shares down ~34% since breach; MAU -3.5%, daily spending -6.3% to 139.2B won | CPNG -34% since breach                                           | hard 4C validated        |
| T2      |  rival Stage2 | 2026-02-25 | Naver online users +23%; CJ Logistics overnight/one-day shipment +120% in Q4         | KRX rival price unavailable                                      | Stage2 rival opportunity |
| T3      |      4B-watch | 2026       | Coupang still has convenience/pricing moat; rivals must capture share                | no OHLC                                                          | 4B                       |
| T4      | Stage3-Yellow | N/A        | Naver/E-Mart/CJ revenue and margin conversion not confirmed                          | no Yellow                                                        | 보류                       |

Coupang breach는 R5 e-commerce trust hard 4C다. Coupang은 약 33.7M customer accounts exposure 이후 U.S.-listed shares가 premarket -4.4%였고, South Korea 정부는 corporate negligence penalties 강화를 검토했다. Reuters는 breach 이후 Coupang shares가 약 -34%, mobile MAU가 11월 대비 1월 -3.5%, average daily consumer spending이 -6.3%로 139.2B won까지 떨어졌다고 보도했다. ([Barron's][6])

동시에 rival Stage2도 생겼다. Naver online users는 같은 기간 +23%였고, CJ Logistics는 Naver를 고객으로 하는 overnight/one-day delivery shipment volume이 Q4에 전년 대비 +120% 늘었다. 다만 Reuters는 Coupang의 가격·편의성 moat가 여전히 강하다는 의견도 함께 전했다. 그래서 이 trigger는 `Coupang hard 4C + Naver/E-Mart/CJ Stage2 opportunity`, Green은 아직 아니다. ([Reuters][7])

```json
{
  "case_id": "r5_loop16_coupang_breach_rival_retail_shift",
  "symbols": "CPNG/035420/139480/000120",
  "best_trigger": "T0/T2",
  "best_trigger_type": "hard_4C_plus_rival_Stage2",
  "breach_disclosure_date": "2025-12-01",
  "affected_accounts_mn": 33.7,
  "coupang_premarket_event_return_pct": -4.4,
  "coupang_return_since_breach_pct": -34,
  "mobile_mau_change_jan_vs_nov_pct": -3.5,
  "daily_consumer_spending_change_pct": -6.3,
  "daily_consumer_spending_jan_krw_bn": 139.2,
  "naver_online_users_change_pct": 23,
  "cj_logistics_overnight_one_day_volume_q4_yoy_pct": 120,
  "stage3_gate_missing": [
    "Naver_GMV_conversion",
    "E_Mart_fast_delivery_revenue",
    "CJ_Logistics_margin",
    "Coupang_churn_persistence",
    "regulatory_penalty_final_amount"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "platform_security_4C_with_rival_stage2"
}
```

---

## Case F — Shinsegae / E-Mart / Alibaba / Gmarket JV

```text
symbols = 004170 / 139480
case_type = Stage2 JV with integration 4B
archetype = RETAIL_PLATFORM_JV_STAGE2_WITH_INTEGRATION_4B
```

| trigger |            type | date       | 당시 공개 evidence                                                                | 가격 anchor       | outcome                 |
| ------- | --------------: | ---------- | ----------------------------------------------------------------------------- | --------------- | ----------------------- |
| T0      | Stage2 evidence | 2024-12-26 | Shinsegae affiliate E-Mart to set JV with Alibaba International               | no price anchor | Stage2                  |
| T1      |      validation | 2024-12-26 | Shinsegae contributes 100% stake in Gmarket; AliExpress Korea + Gmarket in JV | no price        | platform restructuring  |
| T2      |        4B-watch | 2025       | Gmarket had been struggling against Coupang, Naver, AliExpress, Temu          | no OHLC         | integration/competition |
| T3      |   Stage3-Yellow | N/A        | GMV, take-rate, synergy, regulatory approval, seller retention not confirmed  | no Yellow       | 보류                      |

Shinsegae/E-Mart–Alibaba JV는 R5 retail platform Stage2다. E-Mart는 Shinsegae가 보유한 Gmarket 100% stake를 투입해 Alibaba International과 JV를 만들고, AliExpress Korea와 Gmarket을 JV 안에 넣기로 했다. Korea e-commerce market은 Euromonitor 기준 world’s fourth-largest로 언급됐고, Gmarket은 Coupang·Naver뿐 아니라 AliExpress·Temu 같은 중국계 경쟁자와도 싸우고 있었다. 이건 platform restructuring Stage2지만, GMV·take-rate·seller retention·regulatory approval이 없으면 Green이 아니다. ([Reuters][8])

```json
{
  "case_id": "r5_loop16_shinsegae_emart_alibaba_gmarket_jv",
  "symbols": "004170/139480",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage2_JV_with_integration_4B",
  "trigger_date": "2024-12-26",
  "assets_contributed": [
    "Gmarket_100pct_stake",
    "AliExpress_Korea"
  ],
  "market_context": "Korea_ecommerce_world_fourth_largest",
  "competitive_pressure": [
    "Coupang",
    "Naver",
    "AliExpress",
    "Temu"
  ],
  "direct_event_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "JV_completion",
    "GMV_growth",
    "take_rate",
    "seller_retention",
    "regulatory_approval",
    "logistics_integration",
    "loss_reduction"
  ],
  "trigger_outcome_label": "Stage2_platform_JV_not_Green"
}
```

---

## Case G — Homeplus restructuring / offline grocery hard 4C

```text
symbols = private / 139480 read-through / 004170 read-through
case_type = offline grocery restructuring hard 4C
archetype = OFFLINE_GROCERY_RESTRUCTURING_HARD_4C
```

| trigger |               type | date       | 당시 공개 evidence                                                                                       | 가격 anchor               | outcome         |
| ------- | -----------------: | ---------- | ---------------------------------------------------------------------------------------------------- | ----------------------- | --------------- |
| T0      |            hard 4C | 2025-03    | Homeplus enters court-led restructuring after liquidity stress                                       | private, no stock price | hard 4C         |
| T1      |         validation | 2025-06-13 | liquidation value higher than going-concern value; liquidation value 3.7T won, total assets 6.8T won | no price                | hard validation |
| T2      | restructuring sale | 2025-06-20 | court approves sale plan; MBK to write off 2.5T won common shares                                    | no price                | restructuring   |
| T3      |             relief | N/A        | strategic buyer and operating turnaround not confirmed                                               | no relief               | 보류              |

Homeplus는 private이지만 R5 offline grocery hard 4C reference로 중요하다. MBK는 Homeplus가 court-led restructuring에 들어간 뒤 liquidation을 피하기 위해 매각을 추진했고, court-commissioned review에서 liquidation value가 going concern value보다 높게 나왔다. Homeplus liquidation value는 3.7T won, total assets는 6.8T won으로 제시됐다. 이어 법원은 sale plan을 승인했고, MBK는 보유한 2.5T won common shares를 write off하겠다고 밝혔다. 이건 오프라인 grocery model의 hard 4C다. ([Reuters][9])

```json
{
  "case_id": "r5_loop16_homeplus_offline_grocery_restructuring",
  "symbols": "private/139480_readthrough/004170_readthrough",
  "best_trigger": "T0/T2",
  "best_trigger_type": "hard_4C_offline_retail_restructuring",
  "restructuring_start_context": "2025-03",
  "sale_plan_date": "2025-06-13/2025-06-20",
  "liquidation_value_krw_trn": 3.7,
  "total_assets_krw_trn": 6.8,
  "mbk_share_writeoff_krw_trn": 2.5,
  "court_sale_approval": true,
  "causes": [
    "COVID_fallout",
    "ecommerce_competition",
    "liquidity_stress",
    "creditor_repayment_need"
  ],
  "direct_price_anchor": "price_data_unavailable_after_deep_search_private_company",
  "trigger_outcome_label": "offline_grocery_hard_4C_reference"
}
```

---

## Case H — Shrinkflation regulation / food and household ASP constraint

```text
symbols = 097950 / 004370 / 003230 / processed_food_basket
company_scope = CJ CheilJedang / Nongshim / Samyang / processed foods
case_type = 4C-watch / price regulation
archetype = SHRINKFLATION_PRICE_REGULATION_4C_WATCH
```

| trigger |          type | date       | 당시 공개 evidence                                                                           | 가격 anchor      | outcome          |
| ------- | ------------: | ---------- | ---------------------------------------------------------------------------------------- | -------------- | ---------------- |
| T0      |      4C-watch | 2024-05-03 | KFTC designates undisclosed shrinkflation as unfair transaction                          | no stock price | price regulation |
| T1      |    validation | 2024-08    | rule effective from August; fines 5M won first offence, 10M won second offence           | no price       | regulation       |
| T2      |       example | 2024       | CJ CheilJedang sausage weight cut 12.5%; processed foods and household supplies included | no price       | margin/ASP watch |
| T3      | Stage2 relief | N/A        | transparent price hikes / brand pricing power not confirmed                              | no relief      | 보류               |

Shrinkflation regulation은 R5의 가격규제 4C-watch다. Korea Fair Trade Commission은 가격은 유지하면서 용량을 줄이고 알리지 않는 행위를 unfair transaction으로 지정했고, 2024년 8월부터 식품·생활용품 업체는 용량 축소 시 3개월간 공지해야 하며 첫 위반 5M won, 두 번째 10M won 벌금이 부과된다. FT는 예시로 CJ CheilJedang sausage weight -12.5%, Seoul Dairy cheese -10% 등을 언급했다. 이 case는 hidden ASP pass-through를 막는 규제이므로, 식품회사에는 margin/price-power 4C-watch다. ([Financial Times][10])

```json
{
  "case_id": "r5_loop16_shrinkflation_price_regulation",
  "symbols": "097950/004370/003230/processed_food_basket",
  "best_trigger": "T0/T2",
  "best_trigger_type": "4C_watch_price_regulation",
  "trigger_date": "2024-05-03",
  "rule_effective": "2024-08",
  "first_offence_fine_krw_mn": 5,
  "second_offence_fine_krw_mn": 10,
  "notice_period_months": 3,
  "cj_sausage_weight_cut_pct": 12.5,
  "covered_categories": [
    "processed_food",
    "ham",
    "cheese",
    "noodles",
    "toilet_paper",
    "toothpaste",
    "detergent"
  ],
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "transparent_price_hike_acceptance",
    "brand_pricing_power",
    "raw_material_cost_normalization",
    "volume_elasticity",
    "retailer_negotiation"
  ],
  "trigger_outcome_label": "consumer_price_regulation_4C_watch"
}
```

---

# 6. Trigger별 가격경로 검증 요약

| case                        | best trigger |              entry anchor |                                                   event MFE/MAE | market-relative | full MFE/MAE | outcome                   |
| --------------------------- | ------------ | ------------------------: | --------------------------------------------------------------: | --------------: | ------------ | ------------------------- |
| Samyang Buldak              | T1/T2        |         647,000 won close |                                                           +5.7% |     unavailable | unavailable  | Stage2→Yellow candidate   |
| K-beauty U.S. channel       | T1/T2        |    d’Alba >2x since debut |                                        >100% post-debut context |     unavailable | unavailable  | Stage2-Actionable         |
| APR Medicube                | T1/T2        |         APR >4x since Jan |                                                     >4x context |     unavailable | unavailable  | Stage2 + overheat 4B      |
| China visa-free tourism     | T1/T2        |             event returns | Hyundai Dept +7.1%, Hotel Shilla +4.8%, Hankook Cosmetics +9.9% |     unavailable | unavailable  | Stage2 tourism event      |
| Coupang breach / rivals     | T0/T2        | Coupang -34% since breach |                            CPNG -34%, rival data not full price |     unavailable | unavailable  | hard 4C + rival Stage2    |
| Shinsegae/E-Mart Alibaba JV | T0/T2        |               unavailable |                                                 no direct price |             N/A | unavailable  | Stage2 JV                 |
| Homeplus restructuring      | T0/T2        |                   private |                                                 no public stock |             N/A | unavailable  | offline hard 4C           |
| Shrinkflation regulation    | T0/T2        |               unavailable |                                           no direct stock price |             N/A | unavailable  | price-regulation 4C-watch |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
좋은 Stage2:
- K-beauty U.S. channel expansion
- China visa-free tourism
- Shinsegae/E-Mart + Alibaba JV
- APR/Medicube device export growth

약한 Stage2:
- Shinsegae/E-Mart JV는 price anchor와 integration economics 없음.
- China tourism은 visitor spending and margin 전에는 policy event.
- APR은 strong growth지만 valuation/celebrity concentration 4B.
```

## Stage2-Actionable entry 성과

```text
Actionable:
- Samyang: OP estimate +84%, ASP, U.S./Europe shipment, capacity, +5.7%.
- K-beauty: U.S. export rank, e-commerce +71%, d’Alba >2x, retailer channel expansion.
- China visa-free: policy announcement directly moved Hyundai Department Store, Hotel Shilla, Hankook Cosmetics.
```

## Stage3-Yellow 후보

```text
Yellow 후보:
- Samyang: repeat quarterly export margin 확인 시.
- K-beauty: physical-store sell-through and brand margin 확인 시.
- APR: recurring device/consumables revenue and overseas margin 확인 시.
- Naver/E-Mart/CJ Logistics: Coupang share loss가 실제 GMV/배송마진으로 연결되면.
```

## Stage3-Green

```text
이번 R5 Loop 16에서 확정 Green 없음.

이유:
- Samyang/K-beauty/APR은 강하지만 full OHLC와 반복 마진 확인이 필요.
- 관광/면세는 policy event이지 객단가·마진까지 아직 아님.
- 이커머스 경쟁 재편은 Coupang 4C와 rival Stage2가 섞여 있다.
- 오프라인 grocery는 Homeplus restructuring으로 hard 4C reference가 있다.
```

---

# 8. score-price alignment 판정

```text
aligned:
- Samyang Buldak
- China visa-free tourism basket
- Coupang breach hard 4C
- Homeplus offline grocery 4C

Stage2_promote_candidate:
- Samyang
- K-beauty U.S. channel
- China tourism/duty-free/cosmetics
- APR, but with 4B overheat

Stage3-Yellow candidate:
- Samyang if export margin repeats
- K-beauty if offline channel sell-through confirms
- APR if device revenue becomes recurring
- Naver/E-Mart/CJ Logistics if Coupang share leakage converts to revenue and margin

evidence_good_but_price_failed_or_muted:
- Shinsegae/E-Mart + Alibaba JV due no price anchor
- K-beauty ODM names without company-specific price/margin data

failed_rerating:
- Homeplus offline grocery model

event_premium:
- China visa-free tourism before actual spending
- APR celebrity/device hype
- d’Alba post-IPO K-beauty premium

thesis_break_watch:
- Coupang data breach
- Homeplus restructuring
- shrinkflation regulation

hard_4C_success:
- Coupang platform security
- Homeplus offline-grocery restructuring reference
```

---

# 9. 점수비중 교정

## 올릴 축

```csv
axis,delta,reason,cases
export_ASP_shipment_capacity,+5,"수출 ASP·출하·생산능력·OP estimate가 같이 닫히면 Yellow 후보","Samyang"
US_physical_channel_sellthrough,+5,"K-beauty는 e-commerce에서 physical retail로 넘어가는 sell-through가 핵심","K-beauty/d'Alba"
overseas_revenue_mix,+4,"해외 매출 비중이 높을수록 brand scalability 점수 상승","APR/K-beauty"
repeat_purchase_or_recurring_revenue,+5,"디바이스·뷰티는 recurring revenue가 Green gate","APR"
tourist_arrival_spending_margin,+5,"중국 관광객 policy는 실제 객단가·마진 확인 필요","Hotel Shilla/Hyundai Dept/Hankook Cosmetics"
platform_security_trust,+5,"e-commerce는 data breach가 hard 4C","Coupang"
rival_share_capture,+4,"Coupang 이탈이 Naver/E-Mart/CJ 매출로 전환되는지 확인","Naver/E-Mart/CJ Logistics"
retail_restructuring_risk,+5,"offline grocery liquidation risk는 hard 4C","Homeplus"
pricing_transparency_regulation,+4,"shrinkflation 규제는 hidden ASP pass-through 제한","CJ/Food basket"
```

## 내릴 축

```csv
axis,delta,reason,cases
brand_viral_without_margin,-5,"viral brand만으로 Green 금지","APR/K-beauty"
tourism_policy_without_spend,-5,"비자정책은 실제 spending 전에는 Stage2","Hotel Shilla/Hyundai Dept"
ecommerce_user_shift_without_GMV,-4,"MAU 변화는 GMV/margin 전에는 Stage2","Naver/E-Mart/CJ"
JV_without_integration_economics,-5,"Gmarket-Alibaba JV는 integration/take-rate 전에는 Green 금지","Shinsegae/E-Mart"
offline_retail_assets_without_cashflow,-5,"자산가치보다 liquidation value가 높으면 hard 4C","Homeplus"
hidden_price_increase_without_disclosure,-4,"shrinkflation은 규제 리스크","processed food basket"
post_IPO_or_ytd_rally_without_trigger_OHLC,-3,"APR/d'Alba 급등은 full OHLC 없으면 4B 병기","APR/d'Alba"
```

---

# 10. Stage2-Actionable 승격 조건

R5 Loop 16 shadow rule:

```text
R5에서 Stage2 evidence가 아래 중 3개 이상이면 Stage2-Actionable로 승격한다.

1. 수출 ASP, shipment, production capacity 중 2개 이상이 확인된다.
2. OP/EPS estimate revision이 있다.
3. event return이 +5% 이상이다.
4. U.S./China/Europe 등 해외 채널이 실제 retailer 입점 또는 shipment로 확인된다.
5. 해외 매출 비중 또는 e-commerce sales growth가 구체적이다.
6. platform/user shift가 GMV, spending, delivery volume으로 연결된다.
7. 보안사고, 가격규제, 구조조정, liquidation hard gate가 없다.
```

적용:

```text
Samyang:
조건 1,2,3 충족 → Stage2-Actionable / Yellow candidate.

K-beauty:
조건 4,5와 d’Alba price context 충족 → Stage2-Actionable, but tariff/sell-through gate.

China tourism:
조건 3 and policy/event alignment 충족 → Stage2 event, spending 확인 전 Yellow 보류.

APR:
조건 5 and price context 충족 → Stage2 structural, valuation/viral 4B 병기.
```

---

# 11. Stage3-Yellow 조건

```text
Stage3-Yellow:
- Stage2-Actionable 이후 EPS/OP/FCF 경로 변화 가능성이 높아진 상태.
- 하지만 channel sell-through, margin, repeat demand, regulation 중 하나가 남은 상태.
```

Yellow 후보:

```text
Samyang:
export margin and capacity ramp repeat 확인 시 Yellow.

K-beauty:
offline retailer sell-through and brand/ODM margin 확인 시 Yellow.

APR:
overseas device sales, recurring revenue, consumables margin 확인 시 Yellow.

China tourism:
visa-free visitors → duty-free/hotel/department/cosmetics sales margin 확인 시 Yellow.

Naver/E-Mart/CJ Logistics:
Coupang trust loss → user, GMV, delivery margin conversion 확인 시 Yellow.
```

---

# 12. Stage3-Green 조건

```text
Stage3-Green:
- export/brand/channel evidence가 quarterly OP and margin으로 확인됨
- 해외 채널 판매가 inventory push가 아니라 sell-through로 확인됨
- tourism event가 객단가와 margin으로 확인됨
- platform share capture가 GMV and delivery margin으로 확인됨
- data security / price regulation / restructuring hard gate가 없음
- full-window MFE/MAE가 우호적임
```

이번 R5 Loop 16에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
reason = full OHLC unavailable + channel/margin/repeat-demand gates not fully closed
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- viral beauty/device stock rises before repeat sales/margin are proven
- tourism policy moves stocks before visitor spending appears
- e-commerce rival stocks move on Coupang breach before GMV conversion
- JV/M&A announced before integration economics
- K-food single-product concentration becomes excessive
- shrinkflation/pricing regulation limits hidden ASP pass-through
```

적용:

```text
APR:
>4x rally and celebrity device trigger → 4B overheat.

d’Alba/K-beauty:
>2x post-debut and U.S. retailer talks → 4B sell-through/tariff gate.

China visa-free:
policy event → 4B if visitor spending disappoints.

Shinsegae/E-Mart:
Alibaba JV → 4B integration and competition risk.

Samyang:
Buldak concentration and channel inventory → 4B watch.
```

---

# 14. 4C hard gate 조건

```text
R5 4C:
- e-commerce data breach / customer trust collapse
- offline retail court-led restructuring / liquidation value > going concern
- hidden price increase regulation causing margin pass-through failure
- food safety / recall / contamination
- tourism demand collapse due geopolitics or anti-foreigner safety risk
- brand channel saturation and inventory write-down
```

이번 R5 Loop 16 hard 4C:

```text
Coupang data breach = platform security hard 4C
Homeplus restructuring = offline grocery hard 4C
```

Strong 4C-watch:

```text
- shrinkflation regulation
- K-beauty tariff and channel saturation
- tourism anti-foreigner safety/image risk
- Gmarket/Alibaba integration failure
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

R5 production 설계 원칙:

```text
1. K-food는 ASP, shipment, capacity, OP estimate를 분리한다.
2. K-beauty는 e-commerce growth와 physical-store sell-through를 분리한다.
3. beauty device는 viral trigger와 recurring revenue를 분리한다.
4. tourism policy는 visitor spending and margin 전까지 Stage2다.
5. e-commerce는 MAU/GMV/security trust를 따로 scoring한다.
6. offline retail은 asset value보다 going-concern cashflow를 본다.
7. price regulation은 hidden ASP pass-through를 제한하는 4C-watch로 둔다.
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_241.md 요약

```md
# R5 Loop 16. Consumer / Retail / Brands Trigger-level Price Validation

이번 라운드는 R5 Loop 16 trigger-level validation 라운드다.

핵심 결론:
- Samyang Foods / Buldak is the strongest Stage2-Actionable to Stage3-Yellow candidate. Kiwoom raised 2Q OP estimate to 81.2B won, +84% YoY, citing Buldak ASP increases, U.S./Europe shipment growth and capacity expansion. Shares rose 5.7% to 647,000 won, and target price was raised 26% to 830,000 won.
- K-beauty U.S. channel expansion is Stage2-Actionable. Korea became the biggest cosmetics exporter to the U.S. in 2024; top-five Korean beauty brands in U.S. e-commerce grew 71% over two years vs overall market +21% and French top-five +15%. d’Alba shares more than doubled since debut. Green requires physical-store sell-through, tariff absorption and margin.
- APR / Medicube beauty device is Stage2 structural with 4B overheat. APR stock rose more than four-fold since January, market value around $6B, Q2 overseas revenue nearly 80%, and devices around one-third of U.S. sales. Celebrity/viral concentration and valuation require 4B.
- China visa-free tourism is Stage2 event. Hyundai Department Store +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9% after visa-free Chinese tourist group policy. Green requires actual visitor spending and margin.
- Coupang breach is hard 4C and rival Stage2 opportunity. Coupang shares fell around 34% since breach, mobile MAU -3.5%, daily spending -6.3%; Naver online users +23%, CJ Logistics overnight/one-day shipment +120%. Rival conversion to revenue/margin is not yet confirmed.
- Shinsegae/E-Mart + Alibaba/Gmarket JV is Stage2 platform restructuring. Gmarket and AliExpress Korea will be placed in a JV. Integration, GMV, take-rate and seller retention are gates.
- Homeplus restructuring is offline grocery hard 4C. Liquidation value was higher than going-concern value; liquidation value 3.7T won, total assets 6.8T won, MBK write-off 2.5T won.
- Shrinkflation regulation is 4C-watch. KFTC rule forces disclosure of product downsizing; fines are 5M/10M won; CJ CheilJedang sausage weight cut example shows hidden ASP pass-through risk.

Main calibration:
- Raise export_ASP_shipment_capacity, US_physical_channel_sellthrough, overseas_revenue_mix, repeat_purchase_or_recurring_revenue, tourist_arrival_spending_margin, platform_security_trust, rival_share_capture, retail_restructuring_risk, pricing_transparency_regulation.
- Lower brand_viral_without_margin, tourism_policy_without_spend, ecommerce_user_shift_without_GMV, JV_without_integration_economics, offline_retail_assets_without_cashflow, hidden_price_increase_without_disclosure, post_IPO_or_ytd_rally_without_trigger_OHLC.
```

## docs/checkpoints/checkpoint_28a_round241_r5_loop16.md 요약

```md
# Checkpoint 28A Round 241 R5 Loop 16 Trigger-level Calibration

## 반영 내용
- R5 Loop 16 trigger-level validation을 수행했다.
- Samyang Buldak, K-beauty U.S. channel, APR Medicube, China visa-free tourism, Coupang breach/rival shift, Shinsegae-E-Mart/Alibaba JV, Homeplus restructuring, shrinkflation regulation을 검토했다.
- full adjusted OHLC window는 확보하지 못했으므로 Reuters / FT / MarketWatch / Barron’s의 reported event return과 event price anchor를 사용했다.
- OHLC 미확보를 이유로 Stage 후보를 강등하지 않고, price_data_unavailable_after_deep_search로 분리 기록했다.

## 핵심 보정
- K-food는 ASP/shipment/capacity/OP estimate가 같이 닫히면 Stage2-Actionable 또는 Yellow 후보로 승격한다.
- K-beauty는 U.S. e-commerce growth보다 physical-store sell-through and margin이 Green gate다.
- Beauty device rally는 recurring revenue 전에는 overheat 4B를 붙인다.
- Tourism policy rally는 visitor spending and margin 전에는 Stage2다.
- E-commerce는 security trust가 hard gate다.
- Offline grocery restructuring is hard 4C when liquidation value exceeds going-concern value.
- Shrinkflation regulation limits hidden ASP pass-through and is 4C-watch.
```

## data/e2r_case_library/cases_r5_loop16_round241.jsonl 초안

```jsonl
{"case_id":"r5_loop16_samyang_buldak_export","symbol":"003230","company_name":"Samyang Foods","case_type":"Stage2_promote_candidate","primary_archetype":"KFOOD_EXPORT_ASP_CAPACITY_STAGE3_YELLOW","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable_to_Stage3-Yellow_candidate","price_validation":{"trigger_date":"2024-06-14","op_estimate_2q_krw_bn":81.2,"op_estimate_yoy_pct":84,"event_return_pct":5.7,"entry_price_anchor_krw":647000,"target_price_krw":830000,"target_price_raise_pct":26,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_to_yellow_candidate","notes":"ASP+shipment+capacity+OP estimate bridge is strong enough for Yellow candidate, pending repeat margin and OHLC."}
{"case_id":"r5_loop16_kbeauty_us_channel","symbol":"483650/257720/192820/161890/090430","company_name":"d'Alba Global / Silicon2 / Cosmax / Kolmar / Amorepacific read-through","case_type":"Stage2_Actionable_channel_expansion","primary_archetype":"KBEAUTY_US_CHANNEL_STAGE2_ACTIONABLE","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2025-06-05","korea_us_cosmetics_export_rank_2024":1,"top5_korean_us_ecommerce_growth_2y_pct":71,"overall_us_market_growth_2y_pct":21,"top5_french_brands_growth_2y_pct":15,"dalba_post_debut_return":">100%","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_Actionable_with_4B_channel_gate","notes":"K-beauty U.S. channel expansion is real; Green requires physical-store sell-through and brand/ODM margin."}
{"case_id":"r5_loop16_apr_medicube_beauty_device","symbol":"278470","company_name":"APR / Medicube","case_type":"Stage2_structural_with_4B_overheat","primary_archetype":"BEAUTY_DEVICE_VIRAL_STAGE2_WITH_OVERHEAT_4B","best_trigger":"T1/T2","stage_candidate":"Stage2 + 4B-watch","price_validation":{"trigger_date":"2025-10-20","stock_return_since_january":">4x","market_value_usd_bn":6,"device_price_usd_context":180,"q2_2025_overseas_revenue_share_pct":"~80","device_share_of_us_sales_pct":"~33","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_structural_but_overheat_4B","notes":"Beauty-device export growth is structural, but celebrity/viral and valuation concentration require 4B."}
{"case_id":"r5_loop16_china_visa_free_tourism_retail","symbol":"069960/008770/034230/123690","company_name":"Hyundai Department Store / Hotel Shilla / Paradise / Hankook Cosmetics","case_type":"Stage2_tourism_event","primary_archetype":"CHINA_TOURISM_DUTYFREE_STAGE2_EVENT","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable_event","price_validation":{"policy_announcement_date":"2025-08-06","pilot_start_date":"2025-09-29","pilot_end_date":"2026-06","visa_free_stay_days":15,"hyundai_department_store_event_return_pct":7.1,"hotel_shilla_event_return_pct":4.8,"paradise_event_return_pct":2.9,"hankook_cosmetics_event_return_pct":9.9,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_tourism_event_not_Green","notes":"Tourism policy aligns with price reaction, but actual spending and margin are Green gates."}
{"case_id":"r5_loop16_coupang_breach_rival_retail_shift","symbol":"CPNG/035420/139480/000120","company_name":"Coupang / Naver / E-Mart / CJ Logistics","case_type":"hard_4C_plus_rival_Stage2","primary_archetype":"ECOMMERCE_SECURITY_TRUST_4C_AND_RIVAL_STAGE2","best_trigger":"T0/T2","stage_candidate":"4C + Stage2_rival_opportunity","price_validation":{"breach_disclosure_date":"2025-12-01","affected_accounts_mn":33.7,"coupang_premarket_event_return_pct":-4.4,"coupang_return_since_breach_pct":-34,"mobile_mau_change_jan_vs_nov_pct":-3.5,"daily_consumer_spending_change_pct":-6.3,"daily_consumer_spending_jan_krw_bn":139.2,"naver_online_users_change_pct":23,"cj_logistics_overnight_one_day_volume_q4_yoy_pct":120,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"platform_security_4C_with_rival_stage2","notes":"Coupang breach is hard 4C; rival share capture is Stage2 until GMV/margin converts."}
{"case_id":"r5_loop16_shinsegae_emart_alibaba_gmarket_jv","symbol":"004170/139480","company_name":"Shinsegae / E-Mart / Alibaba International / Gmarket","case_type":"Stage2_JV_with_integration_4B","primary_archetype":"RETAIL_PLATFORM_JV_STAGE2_WITH_INTEGRATION_4B","best_trigger":"T0/T2","stage_candidate":"Stage2_JV","price_validation":{"trigger_date":"2024-12-26","assets_contributed":["Gmarket_100pct_stake","AliExpress_Korea"],"market_context":"Korea_ecommerce_world_fourth_largest","direct_event_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_platform_JV_not_Green","notes":"JV is platform restructuring Stage2; GMV/take-rate/seller retention and approval are gates."}
{"case_id":"r5_loop16_homeplus_offline_grocery_restructuring","symbol":"private/139480_readthrough/004170_readthrough","company_name":"Homeplus / offline grocery reference","case_type":"hard_4C_offline_retail_restructuring","primary_archetype":"OFFLINE_GROCERY_RESTRUCTURING_HARD_4C","best_trigger":"T0/T2","stage_candidate":"4C","price_validation":{"sale_plan_date":"2025-06-13/2025-06-20","liquidation_value_krw_trn":3.7,"total_assets_krw_trn":6.8,"mbk_share_writeoff_krw_trn":2.5,"court_sale_approval":true,"direct_price_anchor":"price_data_unavailable_after_deep_search_private_company"},"score_price_alignment":"hard_4C_success_reference","notes":"Offline grocery court restructuring with liquidation value above going concern is hard 4C reference."}
{"case_id":"r5_loop16_shrinkflation_price_regulation","symbol":"097950/004370/003230/processed_food_basket","company_name":"CJ CheilJedang / Nongshim / Samyang / processed food basket","case_type":"4C_watch_price_regulation","primary_archetype":"SHRINKFLATION_PRICE_REGULATION_4C_WATCH","best_trigger":"T0/T2","stage_candidate":"4C-watch","price_validation":{"trigger_date":"2024-05-03","rule_effective":"2024-08","first_offence_fine_krw_mn":5,"second_offence_fine_krw_mn":10,"notice_period_months":3,"cj_sausage_weight_cut_pct":12.5,"direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"consumer_price_regulation_4C_watch","notes":"Shrinkflation crackdown limits hidden ASP pass-through and is a margin/regulatory 4C-watch."}
```

## data/e2r_trigger_calibration/triggers_r5_loop16_round241.jsonl 초안

```jsonl
{"trigger_id":"r5l16_samyang_buldak_T1","case_id":"r5_loop16_samyang_buldak_export","trigger_type":"Stage2-Actionable_to_Stage3-Yellow_candidate","trigger_date":"2024-06-14","evidence_available":"Kiwoom raises Samyang 2Q OP estimate to 81.2B won, +84% YoY, citing Buldak ASP increases, U.S./Europe shipments and capacity expansion; shares +5.7% to 647,000 won","event_return_pct":5.7,"entry_price_krw":647000,"trigger_outcome_label":"excellent_stage2_to_yellow_candidate","promote_to":"Stage3-Yellow_candidate"}
{"trigger_id":"r5l16_kbeauty_us_channel_T1","case_id":"r5_loop16_kbeauty_us_channel","trigger_type":"Stage2-Actionable","trigger_date":"2025-06-05","evidence_available":"Korea became top cosmetics exporter to U.S.; top-five Korean U.S. e-commerce beauty brands +71% over two years; d'Alba shares more than doubled since debut","event_return_pct":"d'Alba >100% post-debut context","trigger_outcome_label":"Stage2_Actionable_channel_expansion","promote_to":"Stage2-Actionable"}
{"trigger_id":"r5l16_apr_medicube_T1","case_id":"r5_loop16_apr_medicube_beauty_device","trigger_type":"Stage2_structural_with_4B","trigger_date":"2025-10-20","evidence_available":"APR stock more than four-fold since January, market value around $6B, Q2 overseas revenue nearly 80%, beauty device about one-third of U.S. sales","event_return_pct":">4x since January","trigger_outcome_label":"Stage2_structural_but_overheat_4B","promote_to":"Stage2+4B"}
{"trigger_id":"r5l16_china_tourism_T1","case_id":"r5_loop16_china_visa_free_tourism_retail","trigger_type":"Stage2_tourism_event","trigger_date":"2025-08-06","evidence_available":"South Korea announces Chinese tourist group visa-free entry from Sep 29 to Jun 2026; Hyundai Department Store +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9%","event_return_pct":"Hyundai Department Store +7.1 / Hotel Shilla +4.8 / Hankook Cosmetics +9.9","trigger_outcome_label":"Stage2_tourism_event_not_Green","promote_to":"Stage2-Actionable_event"}
{"trigger_id":"r5l16_coupang_breach_T0","case_id":"r5_loop16_coupang_breach_rival_retail_shift","trigger_type":"hard_4C","trigger_date":"2025-12-01","evidence_available":"Coupang data breach affects 33.7M accounts; stock -4.4% premarket; later shares down around 34% since breach","event_return_pct":-4.4,"trigger_outcome_label":"platform_security_hard_4C","promote_to":"4C"}
{"trigger_id":"r5l16_coupang_rival_T2","case_id":"r5_loop16_coupang_breach_rival_retail_shift","trigger_type":"rival_Stage2_opportunity","trigger_date":"2026-02-25","evidence_available":"Coupang MAU -3.5%, spending -6.3%; Naver online users +23%; CJ Logistics overnight/one-day delivery volume +120% in Q4","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"rival_share_capture_stage2","promote_to":"Stage2"}
{"trigger_id":"r5l16_emart_alibaba_T0","case_id":"r5_loop16_shinsegae_emart_alibaba_gmarket_jv","trigger_type":"Stage2_JV","trigger_date":"2024-12-26","evidence_available":"Shinsegae/E-Mart to set JV with Alibaba International, contributing 100% Gmarket stake; AliExpress Korea and Gmarket included","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_platform_JV_not_Green","promote_to":"Stage2"}
{"trigger_id":"r5l16_homeplus_T1","case_id":"r5_loop16_homeplus_offline_grocery_restructuring","trigger_type":"hard_4C","trigger_date":"2025-06-13/2025-06-20","evidence_available":"Homeplus liquidation value exceeds going-concern value; liquidation value 3.7T won, total assets 6.8T won, MBK to write off 2.5T won shares","event_return_pct":"private_company_no_stock_price","trigger_outcome_label":"offline_grocery_hard_4C_reference","promote_to":"4C"}
{"trigger_id":"r5l16_shrinkflation_T0","case_id":"r5_loop16_shrinkflation_price_regulation","trigger_type":"4C-watch","trigger_date":"2024-05-03","evidence_available":"KFTC designates undisclosed shrinkflation as unfair transaction; rule from Aug 2024, fines 5M/10M won; CJ sausage weight cut 12.5% example","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"consumer_price_regulation_4C_watch","promote_to":"4C-watch"}
```

## data/sector_taxonomy/score_weight_profiles_round241_r5_loop16_v1.csv 초안

```csv
archetype,export_asp_shipment_capacity,us_physical_channel_sellthrough,overseas_revenue_mix,repeat_purchase_or_recurring_revenue,tourist_arrival_spending_margin,platform_security_trust,rival_share_capture,retail_restructuring_risk,pricing_transparency_regulation,brand_viral_without_margin_penalty,tourism_policy_without_spend_penalty,ecommerce_user_shift_without_gmv_penalty,jv_without_integration_economics_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
KFOOD_EXPORT_ASP_CAPACITY_STAGE3_YELLOW,+5,+1,+4,+4,+0,+1,+0,+0,+2,-3,-1,-1,-1,ASP+shipment+capacity+OP estimate,repeat margin pending,quarterly OP+margin+OHLC,Samyang Buldak template.
KBEAUTY_US_CHANNEL_STAGE2_ACTIONABLE,+2,+5,+5,+4,+1,+1,+0,+0,+1,-5,-1,-1,-1,U.S. e-commerce+retailer channel,physical sell-through/margin pending,retail sell-through+margin,K-beauty/d'Alba/Cosmax.
BEAUTY_DEVICE_VIRAL_STAGE2_WITH_OVERHEAT_4B,+1,+3,+5,+5,+0,+1,+0,+0,+0,-5,-1,-1,-1,overseas device growth,recurring revenue/valuation pending,repeat device+consumables margin,APR/Medicube.
CHINA_TOURISM_DUTYFREE_STAGE2_EVENT,+0,+2,+1,+1,+5,+1,+0,+0,+0,-1,-5,-1,-1,visa-free tourism policy,actual spend/margin pending,visitor spend+dutyfree margin,Hotel Shilla/Hyundai Dept/Hankook Cosmetics.
ECOMMERCE_SECURITY_TRUST_4C_AND_RIVAL_STAGE2,+0,+0,+0,+1,+0,+5,+4,+2,+1,-1,-1,-4,-1,data breach/rival shift,GMV/margin conversion pending,security restored or rival GMV captured,Coupang/Naver/E-Mart/CJ.
RETAIL_PLATFORM_JV_STAGE2_WITH_INTEGRATION_4B,+0,+1,+1,+2,+0,+2,+3,+3,+1,-1,-1,-2,-5,Alibaba/Gmarket JV,integration/take-rate missing,GMV+take-rate+seller retention,Shinsegae/E-Mart.
OFFLINE_GROCERY_RESTRUCTURING_HARD_4C,+0,+0,+0,+0,+0,+1,+0,+5,+1,-1,-1,-1,-1,court-led restructuring,strategic buyer missing,N/A,Homeplus reference.
SHRINKFLATION_PRICE_REGULATION_4C_WATCH,+3,+0,+0,+1,+0,+1,+0,+1,+5,-2,-1,-1,-1,hidden ASP pass-through constrained,transparent pricing pending,pricing power+volume resilience,processed food basket.
```

---

# 이번 R5 Loop 16 결론

```text
1. Samyang Foods / Buldak은 R5의 가장 좋은 Stage2-Actionable → Yellow 후보다.
   ASP, shipment, capacity, OP estimate, price reaction이 동시에 닫혔다.

2. K-beauty U.S. channel은 Stage2-Actionable이다.
   e-commerce growth와 retailer channel은 강하지만 physical sell-through and margin이 Green gate다.

3. APR / Medicube는 Stage2 structural + 4B다.
   해외 매출과 device growth는 강하지만 celebrity/viral valuation overheat가 붙는다.

4. China visa-free tourism은 Stage2 event다.
   주가반응은 강하지만 실제 tourist spending and margin 전에는 Green이 아니다.

5. Coupang breach는 platform security hard 4C다.
   동시에 Naver/E-Mart/CJ Logistics에는 rival Stage2 기회가 생겼지만 GMV/margin 전환이 필요하다.

6. Shinsegae/E-Mart + Alibaba/Gmarket JV는 Stage2다.
   platform restructuring은 맞지만 integration economics 전에는 Green이 아니다.

7. Homeplus restructuring은 offline grocery hard 4C다.
   liquidation value가 going-concern value보다 높으면 asset story가 아니라 hard gate다.

8. Shrinkflation regulation은 price-power 4C-watch다.
   hidden ASP pass-through가 규제되므로 food/household names는 transparent pricing and volume resilience가 필요하다.
```

한 문장으로 압축하면:

> **R5 Loop 16에서 배운 핵심은 “브랜드·유통 narrative”가 아니라, 수출 ASP·출하·생산능력·오프라인 sell-through·해외 매출비중·관광객 객단가·GMV 전환·보안 신뢰·가격규제 대응이 닫혀야 Stage3로 올릴 수 있다는 것이다. 반대로 viral brand, 관광정책, e-commerce user shift, JV headline, hidden price increase만으로는 4B/false positive가 되기 쉽다.**

[1]: https://www.marketwatch.com/story/samyang-foods-set-to-post-strong-2q-earnings-market-talk-d654e045?utm_source=chatgpt.com "Samyang Foods Set to Post Strong 2Q Earnings -- Market Talk"
[2]: https://www.reuters.com/world/asia-pacific/korean-beauty-startups-bet-booming-us-demand-outlasts-tariff-pain-2025-06-05/?utm_source=chatgpt.com "Korean beauty startups bet booming US demand outlasts tariff pain"
[3]: https://www.ft.com/content/6a0f7e2c-f3b9-4eb6-961c-d69af28f7183?utm_source=chatgpt.com "Kardashian endorsement of skincare gadget creates K-beauty champion"
[4]: https://www.reuters.com/world/china/south-korea-offer-visa-free-entry-chinese-tourists-late-september-2025-08-06/?utm_source=chatgpt.com "South Korea to offer visa-free entry to Chinese tourists from late September"
[5]: https://www.reuters.com/world/china/south-korea-pilot-visa-free-entry-chinese-tourist-groups-cctv-reports-2025-09-29/?utm_source=chatgpt.com "South Korea begins visa-free entry for Chinese tourist groups"
[6]: https://www.barrons.com/articles/coupang-stock-price-data-breach-aad847d8?utm_source=chatgpt.com "Online Retailer Coupang Owns Up to Big Blunder. The Stock Drops."
[7]: https://www.reuters.com/business/retail-consumer/coupang-braces-increased-competition-amid-fallout-south-korea-data-breach-2026-02-25/?utm_source=chatgpt.com "Coupang braces for increased competition amid fallout from South Korea data breach"
[8]: https://www.reuters.com/markets/deals/south-koreas-shinsegae-set-up-joint-venture-with-alibaba-international-2024-12-26/?utm_source=chatgpt.com "South Korea's Shinsegae to set up joint venture with Alibaba International"
[9]: https://www.reuters.com/en/mbk-plans-sell-its-troubled-korean-supermarket-chain-homeplus-2025-06-13/?utm_source=chatgpt.com "MBK plans to sell its troubled Korean supermarket chain Homeplus"
[10]: https://www.ft.com/content/61c3975d-ca0e-4043-bc47-79120bb19347?utm_source=chatgpt.com "South Korea cracks down on 'shrinkflation'"

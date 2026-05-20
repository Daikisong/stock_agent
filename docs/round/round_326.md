순서상 이번은 **R5 Loop 17 — 소비재·유통·브랜드 trigger-level price validation 라운드**다.

```text
round = R5 Loop 17
round_id = round_254
large_sector = CONSUMER_RETAIL_BRAND
method = trigger_level_backtest_v1_after_redteam
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R6 Loop 17
```

이번 라운드도 국장 수정주가 일봉 OHLC window를 안정적으로 직접 확보하지 못했다. 그래서 MFE/MAE/peak/drawdown 숫자는 만들지 않고 `price_data_unavailable_after_deep_search`로 둔다. 대신 Reuters/FT/WSJ/MarketWatch의 **reported event return, event price, user/spending data, deal value, visitor/tourism policy trigger, brand export data**를 가격 anchor로 사용한다.

---

# 1. 이번 라운드 대섹터

```text
R5 = 소비재·유통·브랜드
```

R5의 core gate는 아래다.

```text
K-food:
해외 viral demand → ASP 상승 → shipment 증가 → 생산능력 증설 → 해외 유통망 → OP margin → 규제/리콜/현지 경쟁 4B

K-beauty:
e-commerce virality → U.S./Europe retail shelf-in → repeat purchase → offline sell-through → margin → tariff / saturation / China weakness 4B

면세/관광/백화점:
visa-free / 중국 관광객 → visitor volume → basket size → duty-free/department-store sales → operating leverage → low-spend tourism / protest / FX 4B

e-commerce / 생활유통:
trust → MAU/spending → delivery/logistics volume → gross margin → regulation / data breach / supplier abuse 4C

food delivery platform:
M&A / consolidation → market share / take-rate → regulatory approval → financing → integration margin

global brand M&A:
foreign strategic buyer → K-brand valuation benchmark → global distribution → but no listed-stock price unless direct beneficiary
```

---

# 2. 대상 canonical archetype

```text
K_FOOD_EXPORT_ASP_STAGE2_ACTIONABLE
K_BEAUTY_DEVICE_GLOBAL_STAGE2_YELLOW
K_BEAUTY_INDIE_US_RETAIL_STAGE2
CHINA_TOURISM_DUTY_FREE_STAGE2_ACTIONABLE
ECOMMERCE_TRUST_BREAK_HARD_4C
FOOD_DELIVERY_PLATFORM_MA_STAGE2_WITH_APPROVAL_4B
CHINA_PRESTIGE_BEAUTY_FAILED_RERATING
K_BEAUTY_MA_VALUATION_STAGE2_NO_PRICE
```

---

# 3. deep sub-archetype

```text
Samyang Foods / Buldak:
- Buldak export demand drives ASP and shipment growth.
- Kiwoom raised 2Q OP estimate to 81.2B won, +84% YoY.
- target price raised 26% to 830,000 won.
- shares closed +5.7% at 647,000 won.
- Stage2-Actionable; Green requires export sell-through durability and capacity/margin confirmation.

APR / Medicube / beauty device:
- APR stock more than 4x since Jan 2025; market value about $6B.
- $180 facial skincare device promoted by Kylie Jenner on TikTok.
- nearly 80% of Q2 2025 revenue from overseas; device about one-third of U.S. sales.
- Stage2_promote_candidate / Yellow candidate, but celebrity/viral overheat and tariff/regulation 4B.

K-beauty indie / d'Alba / Silicon2 / Olive Young:
- Korea replaced France as the biggest cosmetics exporter to the U.S. in 2024.
- top five Korean cosmetics brands in U.S. e-commerce grew 71% over two years vs U.S. market 21%.
- d'Alba shares more than doubled since debut.
- Silicon2 CEO says physical store sell-through is key.
- Stage2, but offline sell-through/tariff/saturation 4B.

Chinese visa-free tourism:
- South Korea offers visa-free entry to Chinese tourist groups from Sep 29, 2025 to Jun 2026.
- Hyundai Department Store +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9%.
- Stage2-Actionable tourism/retail trigger.
- 4B: low-spend tourism, short policy window, anti-Chinese protests, duty-free basket size.

Coupang:
- data breach affected about 34M users.
- shares around -34% since breach; MAU -3.5%; daily spending -6.3% to 139.2B won.
- Naver online users +23%; CJ Logistics overnight/one-day volume +120%.
- Q4 loss $26M, revenue $8.8B below expectations.
- KFTC fine 2.2B won for supplier pressure/delayed payments.
- hard 4C + rival Stage2.

Baemin / Naver / Uber:
- Uber/Naver consortium bid up to 8T won / $5.34B for Baemin.
- Uber 80%, Naver 20%; Naver received teaser letter but no decision.
- Uber increased Delivery Hero stake to 19.5%; Delivery Hero +5.6%.
- Stage2 M&A, but approval/final SPA/Naver economics 4B.

Amorepacific / China prestige beauty:
- FT noted Amorepacific had its worst market day since listing amid China beauty weakness and local “C-beauty” competition.
- L’Oréal and Estée Lauder also faced China demand pressure.
- failed_rerating / China exposure 4B.

Dr.G / L’Oréal K-beauty M&A:
- L’Oréal acquired Gowoonsesang Cosmetics, owner of Dr.G, to capture K-beauty demand.
- no valuation and no direct listed price anchor.
- Stage2 valuation reference, not Actionable.
```

---

# 4. 선정 case 요약

| bucket                                 | case                                                 | 핵심 판정                                                           |
| -------------------------------------- | ---------------------------------------------------- | --------------------------------------------------------------- |
| structural_success / Stage2-Actionable | **Samyang Foods / Buldak export**                    | +5.7%, 647,000원, OP estimate +84%, ASP·shipment·capacity        |
| Stage2_promote_candidate / Yellow      | **APR / Medicube beauty device**                     | stock >4x since Jan, $6B valuation, overseas revenue nearly 80% |
| Stage2 / channel expansion             | **K-beauty indie / d’Alba / Silicon2 / Olive Young** | U.S. K-beauty e-commerce +71%, d’Alba >2x since debut           |
| Stage2-Actionable                      | **China visa-free tourism / retail basket**          | Hyundai Dept +7.1%, Hotel Shilla +4.8%, Hankook Cosmetics +9.9% |
| hard 4C + rival Stage2                 | **Coupang breach / supplier regulation / rivals**    | Coupang -34%, MAU -3.5%, spending -6.3%, Naver users +23%       |
| Stage2 M&A + 4B                        | **Baemin / Uber-Naver**                              | 8T won bid, Delivery Hero +5.6%, Naver final decision 없음        |
| failed_rerating / 4B                   | **Amorepacific / China prestige weakness**           | China demand / C-beauty pressure, worst market day context      |
| Stage2 no-price                        | **Dr.G / L’Oréal K-beauty acquisition**              | K-beauty global M&A benchmark, valuation undisclosed            |

---

# 5. 각 case별 trigger grid

## Case A — Samyang Foods / Buldak global K-food export

```text
symbol = 003230
case_type = Stage2-Actionable K-food export
archetype = K_FOOD_EXPORT_ASP_STAGE2_ACTIONABLE
```

| trigger |              type | date       | 당시 공개 evidence                                                                   | 가격 anchor                       | outcome |
| ------- | ----------------: | ---------- | -------------------------------------------------------------------------------- | ------------------------------- | ------- |
| T0      |         awareness | 2023~2024  | Buldak viral demand, U.S./Europe export growth                                   | no entry                        |         |
| T1      | Stage2-Actionable | 2024-06-14 | Kiwoom raises 2Q OP estimate to 81.2B won, +84% YoY, ASP and shipments rising    | shares +5.7%, close 647,000 won |         |
| T2      |        validation | 2024-06-14 | U.S./Europe shipments and capacity expansion support earnings                    | same                            |         |
| T3      |          4B-watch | 2024-06~08 | Denmark recall for overly spicy product; two variants later allowed back         | regulatory/brand 4B             |         |
| T4      |     Stage3-Yellow | N/A        | sustained sell-through, capacity, gross margin, U.S./Europe repeat orders needed | 보류                              |         |

Samyang Foods는 R5의 가장 좋은 K-food Stage2-Actionable이다. 2024년 6월 Kiwoom은 Buldak-bokkeum-myeon export 호조로 Samyang의 2Q operating profit estimate를 81.2B won, 전년 대비 +84%로 올렸고, target price도 26% 상향한 830,000 won으로 제시했다. 같은 보도에서 shares는 +5.7%, 647,000원에 마감했다. 이 trigger가 좋은 이유는 “K-food 인기”라는 추상어가 아니라 **ASP 상승 + U.S./Europe shipment 증가 + capacity expansion**이 같이 잡혔기 때문이다. 다만 Denmark recall처럼 해외 food safety/regulatory 4B가 붙을 수 있고, 두 variant가 나중에 재허용됐다는 점은 brand resilience로 볼 수 있다. ([마켓워치][1])

```json
{
  "case_id": "r5_loop17_samyang_buldak_export",
  "symbol": "003230",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2-Actionable_K_food_export_with_regulatory_4B",
  "trigger_date": "2024-06-14",
  "op_estimate_q2_2024_krw_bn": 81.2,
  "op_estimate_yoy_pct": 84,
  "target_price_krw": 830000,
  "target_price_raise_pct": 26,
  "event_return_pct": 5.7,
  "entry_price_krw": 647000,
  "growth_drivers": [
    "Buldak_ASP_increase",
    "US_Europe_shipments",
    "capacity_expansion"
  ],
  "4B_overlay": [
    "food_safety_regulation",
    "spiciness_recall_risk",
    "viral_trend_fatigue",
    "capacity_margin_execution"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_stage2_actionable_k_food_export"
}
```

---

## Case B — APR / Medicube beauty device global brand

```text
symbol = 278470
case_type = Stage2_promote_candidate / Stage3-Yellow candidate
archetype = K_BEAUTY_DEVICE_GLOBAL_STAGE2_YELLOW
```

| trigger |             type | date       | 당시 공개 evidence                                                               | 가격 anchor      | outcome |
| ------- | ---------------: | ---------- | ---------------------------------------------------------------------------- | -------------- | ------- |
| T0      | Stage2 awareness | 2025H1     | Medicube skincare device promoted by Kylie Jenner / TikTok virality          | no exact entry |         |
| T1      |   Stage2_promote | 2025-10-20 | APR stock >4x since Jan; market value about $6B                              | reported >4x   |         |
| T2      |       validation | 2025-10-20 | overseas revenue nearly 80% of Q2 2025; device about one-third of U.S. sales | same           |         |
| T3      |         4B-watch | 2025~      | celebrity virality, U.S. tariffs, device regulation, competition             | 4B             |         |
| T4      |    Stage3-Yellow | N/A        | repeat purchase, retail sell-through, margin durability needed               | 보류             |         |

APR은 R5에서 기존 Amore/LG H&H와 다른 “new K-beauty device” 구조다. FT는 APR stock이 2025년 1월 이후 4배 이상 올랐고 market value가 약 $6B까지 올라 한국에서 가장 가치 있는 beauty group이 됐다고 보도했다. 또 $180 facial skincare device가 Kylie Jenner TikTok promotion 이후 미국에서 반응했고, Q2 revenue의 nearly 80%가 해외에서 나왔으며 device가 U.S. sales의 약 3분의 1을 차지한다고 설명했다. 이는 Stage2_promote / Yellow 후보지만, celebrity-driven overheat, tariff, beauty-device regulation이 4B다. ([Financial Times][2])

```json
{
  "case_id": "r5_loop17_apr_medicube_beauty_device",
  "symbol": "278470",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2_promote_candidate_K_beauty_device",
  "trigger_date": "2025-10-20",
  "reported_stock_return_since_jan_2025": ">4x",
  "market_value_context_usd_bn": 6,
  "device_price_usd_context": 180,
  "overseas_revenue_share_q2_2025_pct": "nearly_80",
  "device_share_of_us_sales_context": "about_one_third",
  "4B_overlay": [
    "celebrity_virality_overheat",
    "US_tariff",
    "beauty_device_regulation",
    "competition_from_global_beauty",
    "repeat_purchase_unknown"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage3_Yellow_candidate_K_beauty_device_not_Green"
}
```

---

## Case C — K-beauty indie brands / d’Alba / Silicon2 / Olive Young channel expansion

```text
symbols = 483650 / 257720 / CJ_Olive_Young_readthrough / 090430
case_type = Stage2 channel expansion
archetype = K_BEAUTY_INDIE_US_RETAIL_STAGE2
```

| trigger |              type | date       | 당시 공개 evidence                                                                               | 가격 anchor       | outcome |
| ------- | ----------------: | ---------- | -------------------------------------------------------------------------------------------- | --------------- | ------- |
| T0      |   Stage2 category | 2025-06-05 | Korea replaced France as top cosmetics exporter to U.S. in 2024                              | no single entry |         |
| T1      | Stage2 validation | 2025-06-05 | top five Korean cosmetics brands in U.S. e-commerce +71% over two years vs U.S. market +21%  | no OHLC         |         |
| T2      |       price proxy | 2025-06-05 | d’Alba shares more than doubled since debut                                                  | >2x context     |         |
| T3      |          4B-watch | 2025       | 10~25% U.S. tariff risk, saturation, COSRX plateau signs, physical-store sell-through needed | 4B              |         |
| T4      |     Stage3-Yellow | N/A        | offline sell-through, reorder, margin, channel inventory needed                              | 보류              |         |

이 case는 “K-beauty가 좋다”가 아니라 어떤 조건에서 Stage2가 되는지 보여준다. Reuters는 한국이 2024년 U.S. cosmetics export에서 France를 제치고 1위가 됐고, Beauty of Joseon·Medicube·Biodance 등이 포함된 U.S. e-commerce top five Korean brands의 online sales가 2년간 평균 +71% 성장했다고 보도했다. 같은 기사에서 d’Alba Global shares는 상장 후 한 달 만에 2배 이상 올랐고, Silicon2 CEO는 장기 성과에는 physical store sales가 필요하다고 했다. 따라서 Stage2는 맞지만, tariff, saturation, offline sell-through failure가 4B다. ([Reuters][3])

```json
{
  "case_id": "r5_loop17_kbeauty_indie_us_retail",
  "symbols": "483650/257720/CJ_Olive_Young_readthrough/090430",
  "best_trigger": "T0/T3",
  "best_trigger_type": "Stage2_K_beauty_US_retail_channel",
  "trigger_date": "2025-06-05",
  "korea_us_cosmetics_export_rank_2024": 1,
  "top5_korean_us_ecommerce_sales_growth_2yr_pct": 71,
  "overall_us_market_growth_2yr_pct": 21,
  "dalba_share_return_since_debut": ">2x",
  "channel_gate": [
    "Ulta",
    "Sephora",
    "Target",
    "Costco",
    "Olive_Young_US_store"
  ],
  "4B_overlay": [
    "US_tariff_10_to_25pct",
    "China_export_decline",
    "brand_saturation",
    "COSRX_growth_plateau",
    "offline_sellthrough_unknown"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_kbeauty_channel_expansion_not_Green"
}
```

---

## Case D — Chinese visa-free tourism / duty-free, department store, beauty basket

```text
symbols = 069960 / 008770 / 034230 / 123690
case_type = Stage2-Actionable tourism retail
archetype = CHINA_TOURISM_DUTY_FREE_STAGE2_ACTIONABLE
```

| trigger |              type | date       | 당시 공개 evidence                                                                           | 가격 anchor                                                                       | outcome |
| ------- | ----------------: | ---------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------- |
| T0      |     Stage2 policy | 2025-03-20 | South Korea announces Chinese group-tour visa waiver plan                                | no stock price in first report                                                  |         |
| T1      | Stage2-Actionable | 2025-08-06 | visa-free entry from Sep 29, 2025 through Jun 2026                                       | Hyundai Dept +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9% |         |
| T2      |        validation | 2025-09-29 | groups of 3+ can stay 15 days; Shilla Duty Free organizes Chinese cruise tour            | no new stock price                                                              |         |
| T3      |          4B-watch | 2025~2026  | budget traveler, experience-over-shopping, anti-Chinese rallies, temporary policy window | 4B                                                                              |         |
| T4      |     Stage3-Yellow | N/A        | visitor volume, basket size, duty-free margin, hotel occupancy needed                    | 보류                                                                              |         |

Chinese visa-free tourism은 R5에서 가장 직접적인 retail Stage2-Actionable이다. 2025년 8월 Reuters는 South Korea가 2025년 9월 29일부터 2026년 6월까지 Chinese tourist groups에 visa-free entry를 제공한다고 보도했고, Hyundai Department Store +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9%가 반응했다. 9월 29일 시행 보도에서는 groups of three or more가 15일간 무비자 체류 가능하고, Shilla Duty Free가 Chinese cruise tour를 준비하며 Baemin이 Alipay/WeChat Pay를 도입한다고 나왔다. 다만 Chinese visitors의 소비 패턴이 경험 소비로 바뀌고, 정책 기간이 한시적이며 반중 집회 risk가 있어 Yellow는 visitor/basket/margin 확인 후다. ([Reuters][4])

```json
{
  "case_id": "r5_loop17_china_visa_free_tourism_retail",
  "symbols": "069960/008770/034230/123690",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2-Actionable_tourism_retail_policy",
  "trigger_date": "2025-08-06",
  "visa_free_period": "2025-09-29_to_2026-06",
  "hyundai_department_store_event_return_pct": 7.1,
  "hotel_shilla_event_return_pct": 4.8,
  "paradise_event_return_pct": 2.9,
  "hankook_cosmetics_event_return_pct": 9.9,
  "pilot_rules": "groups_of_3_or_more_can_stay_15_days",
  "4B_overlay": [
    "temporary_policy_window",
    "low_spend_budget_tourism",
    "experience_over_shopping",
    "anti_chinese_rally_risk",
    "duty_free_basket_size_unknown"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_stage2_actionable_china_tourism_retail"
}
```

---

## Case E — Coupang data breach / supplier regulation / rival retail share shift

```text
symbols = CPNG / 035420 / 139480 / 000120 / retail_basket
case_type = hard 4C + rival Stage2
archetype = ECOMMERCE_TRUST_BREAK_HARD_4C
```

| trigger |                type | date       | 당시 공개 evidence                                                       | 가격 anchor                    | outcome |
| ------- | ------------------: | ---------- | -------------------------------------------------------------------- | ---------------------------- | ------- |
| T0      |             hard 4C | 2025-11~12 | Coupang breach disclosed, about 34M users affected                   | shares start drawdown        |         |
| T1      |       4C validation | 2026-02-25 | shares around -34%, MAU -3.5%, spending -6.3% to 139.2B won          | -34%                         |         |
| T2      |        rival Stage2 | 2026-02-25 | Naver online users +23%, CJ Logistics overnight/one-day volume +120% | rival price unavailable      |         |
| T3      |     4B / regulation | 2026-02-26 | KFTC fine 2.2B won for supplier pressure/delayed payments            | shares closed +1.9% after Q4 |         |
| T4      | earnings validation | 2026-02-26 | Q4 loss $26M, revenue $8.8B below estimate, muted near-term growth   | trust damage                 |         |
| T5      |              relief | 2026       | active customers +8% YoY, signs of stabilization                     | false-break possibility      |         |
| T6      | Stage3-Yellow rival | N/A        | rival GMV/revenue/margin conversion needed                           | 보류                           |         |

Coupang은 R5의 hard 4C다. Reuters는 breach 이후 Coupang shares가 약 -34%, mobile MAU가 -3.5%, daily consumer spending이 -6.3%로 139.2B won까지 감소했다고 보도했다. 동시에 Naver online users는 +23%, CJ Logistics overnight/one-day shipment volume은 +120%로 rival Stage2가 생겼다. 이후 Coupang은 Q4에 $26M loss를 냈고 revenue $8.8B로 estimate를 밑돌았으며, KFTC는 supplier pressure와 delayed payments로 2.2B won fine을 부과했다. 단, active customers +8% YoY와 reactivation signs가 있어 “완전 4C 끝”이 아니라 recovery monitor를 붙인다. ([Reuters][5])

```json
{
  "case_id": "r5_loop17_coupang_trust_break_retail_shift",
  "symbols": "CPNG/035420/139480/000120/retail_basket",
  "best_trigger": "T0/T5",
  "best_trigger_type": "hard_4C_ecommerce_trust_break_with_rival_stage2",
  "affected_users_mn": 34,
  "coupang_return_since_breach_pct": -34,
  "mobile_mau_change_pct": -3.5,
  "daily_spending_change_pct": -6.3,
  "daily_spending_krw_bn": 139.2,
  "naver_online_users_change_pct": 23,
  "cj_logistics_overnight_one_day_volume_yoy_pct": 120,
  "q4_2025_loss_usd_mn": 26,
  "q4_2025_revenue_usd_bn": 8.8,
  "kftc_fine_krw_bn": 2.2,
  "4B_overlay": [
    "supplier_pressure_regulation",
    "delayed_vendor_payments",
    "hypermarket_late_night_rule_easing",
    "trust_recovery_uncertain"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "hard_4C_success_with_rival_stage2_and_recovery_watch"
}
```

---

## Case F — Baemin / Uber-Naver food-delivery M&A

```text
symbols = 035420 / UBER / Delivery_Hero_readthrough
case_type = Stage2 M&A + approval 4B
archetype = FOOD_DELIVERY_PLATFORM_MA_STAGE2_WITH_APPROVAL_4B
```

| trigger |          type | date       | 당시 공개 evidence                                                               | 가격 anchor                      | outcome |
| ------- | ------------: | ---------- | ---------------------------------------------------------------------------- | ------------------------------ | ------- |
| T0      |    Stage2 M&A | 2026-05-18 | Uber/Naver consortium bids up to 8T won / $5.34B for Baemin                  | Naver direct price unavailable |         |
| T1      |    validation | 2026-05-18 | Uber/Naver 80:20 consortium; Naver received teaser letter, no final decision | no Naver price                 |         |
| T2      |   price proxy | 2026-05-18 | Uber increases Delivery Hero stake to 19.5%, stake about €1.7B               | Delivery Hero +5.6%            |         |
| T3      |      4B-watch | 2026       | no SPA, no approval, financing/integration/take-rate/regulation unknown      | 4B                             |         |
| T4      | Stage3-Yellow | N/A        | final deal, approval, Korean platform economics needed                       | 보류                             |         |

Baemin/Naver/Uber는 R5의 현재형 platform M&A Stage2다. Reuters는 2026년 5월 18일 Uber와 Naver가 Baemin 인수를 위해 최대 8T won, 약 $5.34B bid를 제출했고 Uber/Naver 80:20 구조라고 보도했다. Naver는 teaser letter 수령은 인정했지만 final decision은 없다고 했다. 같은 날 Uber는 Delivery Hero 지분을 19.5%로 늘렸고 Delivery Hero shares는 +5.6%였다. 그래서 이 case는 Stage2 M&A지만 final SPA/approval/Naver economics 전까지 Green 금지다. ([Reuters][6])

```json
{
  "case_id": "r5_loop17_baemin_uber_naver_ma",
  "symbols": "035420/UBER/Delivery_Hero_readthrough",
  "best_trigger": "T0/T3",
  "best_trigger_type": "Stage2_food_delivery_MA_with_approval_4B",
  "trigger_date": "2026-05-18",
  "baemin_bid_value_krw_trn": 8.0,
  "baemin_bid_value_usd_bn": 5.34,
  "consortium_ratio": "Uber_80pct_Naver_20pct",
  "naver_status": "teaser_letter_received_no_final_decision",
  "uber_delivery_hero_stake_pct": 19.5,
  "delivery_hero_stake_value_eur_bn": 1.7,
  "delivery_hero_event_return_pct": 5.6,
  "direct_naver_price_anchor": "price_data_unavailable_after_deep_search",
  "4B_overlay": [
    "final_SPA_missing",
    "regulatory_approval",
    "financing",
    "integration",
    "commission_regulation",
    "Naver_economics"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_platform_MA_not_Green"
}
```

---

## Case G — Amorepacific / China prestige beauty failed rerating

```text
symbol = 090430
case_type = failed_rerating / China exposure 4B
archetype = CHINA_PRESTIGE_BEAUTY_FAILED_RERATING
```

| trigger |              type | date      | 당시 공개 evidence                                                                      | 가격 anchor            | outcome |
| ------- | ----------------: | --------- | ----------------------------------------------------------------------------------- | -------------------- | ------- |
| T0      | 4B China exposure | 2024-08   | FT notes Amorepacific had worst market day since listing amid China beauty weakness | no exact % in source |         |
| T1      |        validation | 2024~2025 | China demand weak, domestic C-beauty gains share, global beauty peers pressured     | no KRX OHLC          |         |
| T2      |          contrast | 2025      | indie K-beauty / U.S. e-commerce grows while China-exposed prestige weakens         | factor rotation      |         |
| T3      |   Stage2 recovery | N/A       | U.S./Europe mix, COSRX/brand portfolio margin recovery needed                       | 보류                   |         |

Amorepacific은 R5에서 “K-beauty 전체가 좋다”라는 단순 판단을 막아주는 failed_rerating case다. FT는 China beauty weakness와 local C-beauty competition 속에서 Amorepacific이 14년 상장 역사상 worst market day를 겪었다고 보도했다. 같은 맥락에서 Shiseido, L’Oréal, Estée Lauder 등 China-exposed global beauty names도 압박을 받았다. 즉 R5에서는 **indie U.S. K-beauty와 China-exposed prestige beauty를 분리**해야 한다. ([Financial Times][7])

```json
{
  "case_id": "r5_loop17_amorepacific_china_prestige_failed_rerating",
  "symbol": "090430",
  "best_trigger": "T0/T3",
  "best_trigger_type": "failed_rerating_china_prestige_beauty",
  "trigger_period": "2024-08",
  "reported_price_context": "worst_market_day_since_listing_14_years",
  "negative_drivers": [
    "weak_China_demand",
    "C_beauty_competition",
    "daigou_and_tourist_shopping_weakness",
    "prestige_beauty_pressure"
  ],
  "recovery_gate_missing": [
    "US_Europe_mix_shift",
    "COSRX_growth_reacceleration",
    "offline_sellthrough",
    "gross_margin_recovery",
    "China_inventory_normalization"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "failed_rerating_china_exposure_4B"
}
```

---

## Case H — Dr.G / L’Oréal K-beauty acquisition

```text
symbols = Gowoonsesang_private / K_beauty_MA_reference / 090430_readthrough
case_type = Stage2 M&A valuation reference no price
archetype = K_BEAUTY_MA_VALUATION_STAGE2_NO_PRICE
```

| trigger |                 type | date       | 당시 공개 evidence                                                              | 가격 anchor             | outcome |
| ------- | -------------------: | ---------- | --------------------------------------------------------------------------- | --------------------- | ------- |
| T0      | Stage2 M&A reference | 2024-12-23 | L’Oréal acquires Gowoonsesang Cosmetics, owner of Dr.G                      | valuation undisclosed |         |
| T1      |           validation | 2024-12-23 | L’Oréal says Dr.G has pan-Asian and global growth potential                 | no listed KRX price   |         |
| T2      |             4B-watch | 2024~      | China slowdown, valuation undisclosed, no direct public-company beneficiary | 4B                    |         |
| T3      |        Stage3-Yellow | N/A        | direct listed readthrough or comparable valuation needed                    | 보류                    |         |

Dr.G acquisition은 K-beauty M&A valuation reference다. L’Oréal은 Gowoonsesang Cosmetics, Dr.G owner를 인수하며 K-beauty의 affordable skincare와 global growth potential을 강조했다. L’Oréal은 과거 3CE도 인수했다. 하지만 valuation이 공개되지 않았고, Gowoonsesang은 private asset이라 국장 listed price anchor가 없다. 따라서 Stage2 reference로만 둔다. ([Reuters][8])

```json
{
  "case_id": "r5_loop17_dr_g_loreal_kbeauty_ma",
  "symbols": "Gowoonsesang_private/K_beauty_MA_reference/090430_readthrough",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage2_K_beauty_MA_valuation_reference_no_price",
  "trigger_date": "2024-12-23",
  "buyer": "L_Oreal",
  "target": "Gowoonsesang_Cosmetics_Dr_G",
  "valuation": "undisclosed",
  "strategic_logic": [
    "K_beauty_demand",
    "affordable_effective_skincare",
    "pan_Asian_presence",
    "global_growth_potential"
  ],
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_MA_reference_not_actionable"
}
```

---

# 6. Trigger별 실제 가격경로 검증 요약

이번 R5 Loop 17은 full OHLC가 없으므로, 아래 표는 **reported event anchor 기준**이다.

| case                        | best trigger |                                            event return / price |     market-relative | full MFE/MAE | outcome                           |
| --------------------------- | -----------: | --------------------------------------------------------------: | ------------------: | ------------ | --------------------------------- |
| Samyang / Buldak            |           T1 |                                                 +5.7%, 647,000원 |         unavailable | unavailable  | excellent Stage2-Actionable       |
| APR / Medicube              |           T1 |                                   >4x since Jan 2025, $6B value |         unavailable | unavailable  | Stage2_promote / Yellow candidate |
| K-beauty indie / d’Alba     |        T1/T2 |                                          d’Alba >2x since debut |    no direct basket | unavailable  | Stage2 channel expansion          |
| China tourism retail        |           T1 | Hyundai Dept +7.1%, Hotel Shilla +4.8%, Hankook Cosmetics +9.9% |              strong | unavailable  | Stage2-Actionable                 |
| Coupang trust break         |        T1/T4 |                                      Coupang -34%, Q4 loss $26M | no KRX rivals price | unavailable  | hard 4C + rival Stage2            |
| Baemin / Naver-Uber         |        T0/T2 |                          Delivery Hero +5.6%, Naver unavailable |          proxy only | unavailable  | Stage2 M&A + 4B                   |
| Amorepacific China weakness |           T0 |                                        worst market day context | exact % unavailable | unavailable  | failed_rerating                   |
| Dr.G / L’Oréal              |           T0 |                                           valuation undisclosed |     no public price | unavailable  | Stage2 M&A reference              |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
가장 좋은 Stage2:
1. Samyang Foods / Buldak: ASP + shipment + capacity + +5.7% price.
2. China visa-free tourism retail basket: direct stock reaction across department store, hotel/duty-free, cosmetics.
3. APR / Medicube: >4x stock move and overseas revenue concentration.
4. K-beauty indie / d'Alba / Silicon2: U.S. e-commerce export data and d'Alba >2x.
5. Baemin / Naver-Uber: current M&A trigger, but final decision absent.
```

## Stage2-Actionable entry 성과

```text
Stage2-Actionable:
- Samyang Foods.
- China visa-free tourism retail basket.
- APR / Medicube, but overheat 4B.
- Coupang rivals only if Naver/CJ/E-Mart GMV and margin conversion appears.

Actionable 보류:
- Baemin / Naver-Uber: teaser letter and no final SPA.
- Dr.G / L'Oréal: no valuation, no direct public price.
- K-beauty indie basket: offline sell-through and tariff impact missing.
```

## Stage3-Yellow 후보

```text
Yellow 후보:
- Samyang if export sell-through, capacity, margin and repeat distributor orders continue.
- APR if device repeat purchases, overseas sell-through and margin are durable.
- K-beauty indie / Silicon2 if U.S. physical retail sell-through confirms.
- China tourism basket if visitor volume, duty-free basket size and hotel occupancy convert into OP.
- Coupang rivals if user migration converts to revenue and margin.
```

## Stage3-Green

```text
이번 R5 Loop 17에서 확정 Green 없음.

이유:
- Samyang은 강하지만 full OHLC와 long-window export sell-through 확인이 없다.
- APR은 강하지만 viral/celebrity overheat와 regulation/tariff gate가 있다.
- K-beauty indie는 U.S. physical-store sell-through가 아직 gate다.
- 관광/면세는 정책 window가 한시적이고 basket size가 불명확하다.
- Baemin은 final deal이 아니다.
- Coupang은 hard 4C 이후 recovery watch이지 Green이 아니다.
```

---

# 8. score-price alignment 판정

```text
aligned:
- Samyang Foods / Buldak export.
- China visa-free tourism retail.
- Coupang trust-break hard 4C.
- Baemin / Naver-Uber as Stage2 M&A, not Green.
- Amorepacific China weakness as failed_rerating.
- Dr.G / L’Oréal as valuation reference only.

Stage2_promote_candidate:
- Samyang Foods.
- APR / Medicube.
- d’Alba / Silicon2 / K-beauty U.S. channel.
- China tourism retail basket.
- Coupang rivals if revenue conversion appears.

Stage3-Yellow candidate:
- Samyang Foods if export margin and capacity hold.
- APR if device repeat purchase and sell-through hold.
- K-beauty indie brands if offline distribution scales.
- China tourism retail if visitor/basket metrics confirm.

false_positive_score:
- Baemin/Naver promoted before final SPA.
- Dr.G/L’Oréal readthrough promoted without listed beneficiary.
- K-beauty indie basket promoted without physical-store sell-through.
- China tourism basket promoted without basket-size/OP evidence.

evidence_good_but_price_failed:
- Amorepacific China prestige beauty exposure.
- Coupang Q4 loss despite some recovery signs.

event_premium:
- APR celebrity/TikTok premium.
- Baemin M&A premium.
- China visa-free tourism rally.
- Samyang Buldak viral export premium.

thesis_break:
- Coupang trust breach.
- China prestige beauty demand for Amorepacific-type legacy brands.

4B-watch:
- U.S. tariffs on K-beauty.
- K-beauty saturation and COSRX plateau.
- Chinese tourist low-spend pattern.
- Food safety/regulatory issue for spicy products.
- Supplier/payment regulation for Coupang.
```

---

# 9. 점수비중 교정

## 올릴 축

```csv
axis,delta,reason,cases
export_ASP_shipment_capacity,+5,"소비재 수출주는 ASP+shipment+capacity가 닫히면 Stage2-Actionable","Samyang"
brand_viral_to_export_conversion,+4,"viral brand가 실제 수출/매출로 전환되면 승격","Samyang, APR"
overseas_revenue_mix,+5,"해외매출 비중이 높고 성장성이 검증되면 Yellow 후보","APR"
US_retail_shelf_in,+5,"K-beauty는 e-commerce 다음 physical retail sell-through가 핵심","d'Alba, Silicon2, Olive Young"
tourism_policy_price_reaction,+5,"visa-free 정책과 리테일 주가반응이 동시에 닫히면 Stage2","Hotel Shilla, Hyundai Dept"
consumer_trust_security,+5,"생활유통 플랫폼 breach는 hard 4C","Coupang"
MAU_spending_conversion,+5,"유통 플랫폼은 MAU와 spending 변화가 price보다 선행지표","Coupang, Naver"
M&A_finality,+4,"Baemin 같은 platform M&A는 final SPA/approval이 핵심","Naver/Baemin"
```

## 내릴 축

```csv
axis,delta,reason,cases
viral_brand_without_sellthrough,-5,"viral/celebrity만으로 Green 금지","APR, Samyang"
Kbeauty_export_without_offline_sales,-4,"e-commerce growth만으로 Green 금지","d'Alba, Silicon2"
tourism_headline_without_basket_size,-5,"중국 관광객 headline만으로 면세/백화점 Green 금지","Hotel Shilla, Hyundai Dept"
legacy_china_exposure_ignored,-5,"China prestige weakness를 무시하면 false positive","Amorepacific"
M&A_teaser_without_final_SPA,-5,"teaser letter만으로 Actionable 금지","Naver/Baemin"
trust_recovery_claim_without_spending,-5,"Coupang recovery는 spending/MAU 회복 전까지 보류","Coupang"
supplier_regulation_ignored,-4,"유통 플랫폼 margin을 supplier abuse로 만든 경우 4B","Coupang"
tariff_margin_ignored,-4,"K-beauty U.S. tariff를 margin에서 빼야 함","K-beauty basket"
```

---

# 10. Stage2-Actionable 승격 조건

R5 Loop 17 shadow rule:

```text
R5에서 Stage2 evidence가 아래 중 4개 이상이면 Stage2-Actionable로 승격한다.

1. event return +5% 이상
2. brand export ASP / shipment / capacity 중 2개 이상 확인
3. overseas revenue mix or overseas channel expansion이 확인
4. tourism/retail policy가 stock reaction과 동시에 닫힘
5. MAU/spending/GMV가 실제로 움직임
6. M&A는 final SPA 또는 binding bid / approval path가 있음
7. tariff, regulation, data breach, China weakness 4B가 식별 가능하고 관리 가능
```

적용:

```text
Samyang:
1,2,3 일부 충족 → Stage2-Actionable.

APR:
1은 reported >4x broad move, 3 충족. 7은 overheat/tariff 4B → Stage2_promote / Yellow candidate.

China tourism:
1,4 충족. 5는 visitor/basket data 필요 → Stage2-Actionable but Yellow 보류.

Coupang:
5는 negative로 확인, 7은 hard breach → 4C, rival Stage2 only.

Baemin:
6 미충족; final SPA 없음 → Stage2 M&A only.

Dr.G:
M&A reference지만 price/valuation 없음 → Stage2 reference only.
```

---

# 11. Stage3-Yellow 조건

```text
Stage3-Yellow:
Stage2-Actionable 이후 아래 중 2개 이상이 추가로 닫히면 Yellow.

1. overseas sell-through and repeat orders
2. margin durability after tariff / distributor fee
3. capacity expansion without inventory build
4. physical retail shelf-in and reorder data
5. tourism visitor volume + basket size + OP conversion
6. MAU/spending recovery or rival GMV conversion
7. final M&A agreement / regulatory approval
```

Yellow 후보:

```text
Samyang:
export sell-through + margin + capacity 확인 시 Yellow.

APR:
repeat device sales + overseas margin + retail expansion 확인 시 Yellow.

K-beauty indie:
Ulta/Sephora/Target/Costco sell-through 확인 시 Yellow.

China tourism basket:
visitor volume + basket size + duty-free/hotel OP 확인 시 Yellow.

Coupang rivals:
Naver/CJ/E-Mart GMV and margin conversion 확인 시 Yellow.

Baemin:
final SPA and approval 확인 시 Yellow.
```

---

# 12. Stage3-Green 조건

```text
Stage3-Green:
- brand demand converts into repeat revenue and margin.
- overseas channel expansion produces sell-through, not inventory stuffing.
- tourism policy converts into OP, not only visitor count.
- platform trust recovery appears in MAU/spending/GMV.
- M&A finality and integration economics are confirmed.
- tariff/regulatory/China weakness 4B is reduced.
- full-window MFE/MAE is favorable.
```

이번 R5 Loop 17에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
reason = full OHLC unavailable + sell-through/margin/basket/finality gates not fully closed
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- viral brand without repeat sell-through.
- U.S. tariff risk for K-beauty.
- China prestige beauty weakness.
- tourism visitor count without basket size.
- data breach and supplier regulation.
- M&A teaser without final SPA.
- food safety / recall risk.
- platform growth based on supplier squeeze.
```

적용:

```text
Samyang:
regulatory/spiciness recall 4B, but brand resilience visible.

APR:
celebrity/TikTok overheat and device regulation 4B.

K-beauty indie:
tariff and saturation 4B.

China tourism:
temporary visa-free window and low-spend tourism 4B.

Coupang:
data breach hard 4C + supplier abuse 4B.

Baemin:
teaser/no final decision 4B.

Amorepacific:
China prestige weakness 4B.
```

---

# 14. 4C hard gate 조건

```text
R5 4C:
- consumer trust breach with MAU/spending deterioration.
- food-safety issue that creates sustained overseas ban.
- platform regulatory sanction that changes margin model.
- M&A failure after price premium.
- China demand collapse for legacy brand.
```

이번 R5 Loop 17 hard/strong 4C:

```text
Coupang breach = hard_4C_success
```

Strong 4B:

```text
- Amorepacific China prestige weakness
- K-beauty tariff/saturation
- Baemin M&A finality risk
- tourism low-spend/basket-size risk
- Samyang food-safety/regulatory monitoring
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

R5 production 설계 원칙:

```text
1. viral brand와 actual export sell-through를 분리한다.
2. e-commerce growth와 physical retail sell-through를 분리한다.
3. tourism policy와 duty-free/department-store OP conversion을 분리한다.
4. e-commerce trust breach는 MAU/spending이 깨지면 hard 4C다.
5. M&A teaser는 final SPA/approval 전까지 Stage2다.
6. China-exposed legacy beauty와 U.S.-focused indie K-beauty를 분리한다.
7. tariff/regulatory/supplier-abuse risk는 4B로 병기한다.
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_254.md 요약

```md
# R5 Loop 17. Consumer / Retail / Brand Trigger-level Price Validation

이번 라운드는 R5 Loop 17 trigger-level validation 라운드다.

핵심 결론:
- Samyang Foods / Buldak is the cleanest R5 Stage2-Actionable K-food case. Kiwoom raised 2Q OP estimate to 81.2B won, +84% YoY, and target price by 26% to 830,000 won; shares closed +5.7% at 647,000 won. ASP, U.S./Europe shipments and capacity expansion are the key gates.
- APR / Medicube is Stage2_promote / Stage3-Yellow candidate. APR stock rose more than four-fold since Jan 2025 to about $6B valuation, with overseas revenue nearly 80% of Q2 2025 and beauty devices about one-third of U.S. sales. Viral overheat, tariffs and device regulation remain 4B.
- K-beauty indie brands / d’Alba / Silicon2 / Olive Young are Stage2 channel-expansion cases. Korea became the top cosmetics exporter to the U.S. in 2024, top five Korean U.S. e-commerce brands grew 71% over two years, and d’Alba shares more than doubled since debut. Green requires offline sell-through.
- Chinese visa-free tourism is Stage2-Actionable. Hyundai Department Store +7.1%, Hotel Shilla +4.8%, Paradise +2.9% and Hankook Cosmetics +9.9% after visa-free entry was confirmed for Chinese groups from Sep 29, 2025 to Jun 2026. Green requires visitor volume, basket size and OP conversion.
- Coupang is hard 4C with rival Stage2. Shares fell around 34% after the breach, MAU -3.5%, spending -6.3%, while Naver users +23% and CJ Logistics one-day/overnight volume +120%. Q4 loss and KFTC fine add 4B.
- Baemin / Uber-Naver is Stage2 M&A with approval 4B. Consortium bid up to 8T won / $5.34B, but Naver only received a teaser letter and no final decision. Delivery Hero +5.6% proxy reaction.
- Amorepacific is failed_rerating / China exposure 4B. China prestige beauty weakness and C-beauty competition caused worst-market-day context.
- Dr.G / L’Oréal is K-beauty M&A valuation reference only. L’Oréal acquired Gowoonsesang/Dr.G, but valuation and listed price anchor are unavailable.

Main calibration:
- Raise export_ASP_shipment_capacity, brand_viral_to_export_conversion, overseas_revenue_mix, US_retail_shelf_in, tourism_policy_price_reaction, consumer_trust_security, MAU_spending_conversion, M&A_finality.
- Lower viral_brand_without_sellthrough, Kbeauty_export_without_offline_sales, tourism_headline_without_basket_size, legacy_china_exposure_ignored, M&A_teaser_without_final_SPA, trust_recovery_claim_without_spending, supplier_regulation_ignored, tariff_margin_ignored.
```

## docs/checkpoints/checkpoint_28a_round254_r5_loop17.md 요약

```md
# Checkpoint 28A Round 254 R5 Loop 17 Trigger-level Calibration

## 반영 내용
- R5 Loop 17 trigger-level validation을 수행했다.
- Samyang/Buldak, APR/Medicube, K-beauty indie/d’Alba/Silicon2, China visa-free tourism, Coupang trust break, Baemin/Naver-Uber M&A, Amorepacific China weakness, Dr.G/L’Oréal M&A를 검토했다.
- full adjusted OHLC는 확보하지 못했으므로 Reuters / FT / WSJ / MarketWatch reported event return과 event price anchor를 사용했다.
- MFE/MAE는 조작하지 않고 price_data_unavailable_after_deep_search로 분리했다.

## 핵심 보정
- Viral brand must be converted into export sell-through, ASP, shipment and margin.
- K-beauty e-commerce growth is Stage2; physical retail sell-through is Yellow gate.
- Tourism visa policy is Stage2-Actionable only if stock reaction is clear; Green requires basket size and OP conversion.
- E-commerce data breach with MAU/spending deterioration is hard 4C.
- M&A teaser letters are not final deal triggers.
- China-exposed prestige beauty and U.S.-focused indie K-beauty must be scored separately.
```

## data/e2r_case_library/cases_r5_loop17_round254.jsonl 초안

```jsonl
{"case_id":"r5_loop17_samyang_buldak_export","symbol":"003230","company_name":"Samyang Foods","case_type":"Stage2_Actionable_K_food_export_with_regulatory_4B","primary_archetype":"K_FOOD_EXPORT_ASP_STAGE2_ACTIONABLE","best_trigger":"T1/T3","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2024-06-14","op_estimate_q2_2024_krw_bn":81.2,"op_estimate_yoy_pct":84,"target_price_krw":830000,"target_price_raise_pct":26,"event_return_pct":5.7,"entry_price_krw":647000,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_actionable_k_food_export","notes":"Buldak ASP, shipments and capacity are strong, but food-safety/regulatory and viral fatigue remain 4B."}
{"case_id":"r5_loop17_apr_medicube_beauty_device","symbol":"278470","company_name":"APR / Medicube","case_type":"Stage2_promote_candidate_K_beauty_device","primary_archetype":"K_BEAUTY_DEVICE_GLOBAL_STAGE2_YELLOW","best_trigger":"T1/T3","stage_candidate":"Stage3-Yellow_candidate","price_validation":{"trigger_date":"2025-10-20","reported_stock_return_since_jan_2025":">4x","market_value_context_usd_bn":6,"device_price_usd_context":180,"overseas_revenue_share_q2_2025_pct":"nearly_80","device_share_of_us_sales_context":"about_one_third","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage3_Yellow_candidate_K_beauty_device_not_Green","notes":"Beauty-device global brand momentum is strong, but repeat purchase, margin and overheat/tariff risk remain gates."}
{"case_id":"r5_loop17_kbeauty_indie_us_retail","symbol":"483650/257720/CJ_Olive_Young_readthrough/090430","company_name":"d'Alba / Silicon2 / Olive Young / Amorepacific readthrough","case_type":"Stage2_K_beauty_US_retail_channel","primary_archetype":"K_BEAUTY_INDIE_US_RETAIL_STAGE2","best_trigger":"T0/T3","stage_candidate":"Stage2","price_validation":{"trigger_date":"2025-06-05","korea_us_cosmetics_export_rank_2024":1,"top5_korean_us_ecommerce_sales_growth_2yr_pct":71,"overall_us_market_growth_2yr_pct":21,"dalba_share_return_since_debut":">2x","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_kbeauty_channel_expansion_not_Green","notes":"U.S. K-beauty channel expansion is real, but physical sell-through, tariff and saturation are gates."}
{"case_id":"r5_loop17_china_visa_free_tourism_retail","symbol":"069960/008770/034230/123690","company_name":"Hyundai Department Store / Hotel Shilla / Paradise / Hankook Cosmetics","case_type":"Stage2_Actionable_tourism_retail_policy","primary_archetype":"CHINA_TOURISM_DUTY_FREE_STAGE2_ACTIONABLE","best_trigger":"T1/T3","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2025-08-06","visa_free_period":"2025-09-29_to_2026-06","hyundai_department_store_event_return_pct":7.1,"hotel_shilla_event_return_pct":4.8,"paradise_event_return_pct":2.9,"hankook_cosmetics_event_return_pct":9.9,"pilot_rules":"groups_of_3_or_more_can_stay_15_days","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_actionable_china_tourism_retail","notes":"Visa-free policy and stock reaction aligned; basket size and OP conversion are Yellow/Green gates."}
{"case_id":"r5_loop17_coupang_trust_break_retail_shift","symbol":"CPNG/035420/139480/000120/retail_basket","company_name":"Coupang / Naver / E-Mart / CJ Logistics","case_type":"hard_4C_ecommerce_trust_break_with_rival_stage2","primary_archetype":"ECOMMERCE_TRUST_BREAK_HARD_4C","best_trigger":"T0/T5","stage_candidate":"4C + rival Stage2","price_validation":{"affected_users_mn":34,"coupang_return_since_breach_pct":-34,"mobile_mau_change_pct":-3.5,"daily_spending_change_pct":-6.3,"daily_spending_krw_bn":139.2,"naver_online_users_change_pct":23,"cj_logistics_overnight_one_day_volume_yoy_pct":120,"q4_2025_loss_usd_mn":26,"q4_2025_revenue_usd_bn":8.8,"kftc_fine_krw_bn":2.2,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"hard_4C_success_with_rival_stage2_and_recovery_watch","notes":"Trust break damaged stock, MAU and spending; rivals need GMV/revenue/margin conversion for Yellow."}
{"case_id":"r5_loop17_baemin_uber_naver_ma","symbol":"035420/UBER/Delivery_Hero_readthrough","company_name":"Naver / Uber / Delivery Hero / Baemin","case_type":"Stage2_food_delivery_MA_with_approval_4B","primary_archetype":"FOOD_DELIVERY_PLATFORM_MA_STAGE2_WITH_APPROVAL_4B","best_trigger":"T0/T3","stage_candidate":"Stage2 + 4B-watch","price_validation":{"trigger_date":"2026-05-18","baemin_bid_value_krw_trn":8.0,"baemin_bid_value_usd_bn":5.34,"consortium_ratio":"Uber_80pct_Naver_20pct","naver_status":"teaser_letter_received_no_final_decision","uber_delivery_hero_stake_pct":19.5,"delivery_hero_stake_value_eur_bn":1.7,"delivery_hero_event_return_pct":5.6,"direct_naver_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_platform_MA_not_Green","notes":"Large M&A trigger but no final SPA, approval or Naver economics yet."}
{"case_id":"r5_loop17_amorepacific_china_prestige_failed_rerating","symbol":"090430","company_name":"Amorepacific","case_type":"failed_rerating_china_prestige_beauty","primary_archetype":"CHINA_PRESTIGE_BEAUTY_FAILED_RERATING","best_trigger":"T0/T3","stage_candidate":"failed_rerating + 4B-watch","price_validation":{"trigger_period":"2024-08","reported_price_context":"worst_market_day_since_listing_14_years","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"failed_rerating_china_exposure_4B","notes":"Legacy China-exposed prestige beauty must be separated from U.S.-focused indie K-beauty."}
{"case_id":"r5_loop17_dr_g_loreal_kbeauty_ma","symbol":"Gowoonsesang_private/K_beauty_MA_reference/090430_readthrough","company_name":"Dr.G / Gowoonsesang / L'Oréal","case_type":"Stage2_K_beauty_MA_valuation_reference_no_price","primary_archetype":"K_BEAUTY_MA_VALUATION_STAGE2_NO_PRICE","best_trigger":"T0/T2","stage_candidate":"Stage2 reference","price_validation":{"trigger_date":"2024-12-23","buyer":"L_Oreal","target":"Gowoonsesang_Cosmetics_Dr_G","valuation":"undisclosed","direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_MA_reference_not_actionable","notes":"Global buyer validates K-beauty M&A appetite, but valuation and public-stock price anchor are unavailable."}
```

## data/e2r_trigger_calibration/triggers_r5_loop17_round254.jsonl 초안

```jsonl
{"trigger_id":"r5l17_samyang_buldak_T1","case_id":"r5_loop17_samyang_buldak_export","trigger_type":"Stage2-Actionable_K_food_export","trigger_date":"2024-06-14","event_return_pct":5.7,"entry_price_krw":647000,"trigger_outcome_label":"excellent_stage2_actionable_k_food_export","promote_to":"Stage2-Actionable"}
{"trigger_id":"r5l17_samyang_denmark_T3","case_id":"r5_loop17_samyang_buldak_export","trigger_type":"4B_food_safety_regulatory_watch","trigger_date":"2024-06_to_2024-08","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"regulatory_4B_but_brand_resilience","promote_to":"4B-watch"}
{"trigger_id":"r5l17_apr_medicube_T1","case_id":"r5_loop17_apr_medicube_beauty_device","trigger_type":"Stage3-Yellow_candidate_K_beauty_device","trigger_date":"2025-10-20","event_return_pct":"reported_>4x_since_Jan_2025","trigger_outcome_label":"Stage3_Yellow_candidate_not_Green","promote_to":"Stage3-Yellow_candidate"}
{"trigger_id":"r5l17_kbeauty_us_channel_T0","case_id":"r5_loop17_kbeauty_indie_us_retail","trigger_type":"Stage2_Kbeauty_US_ecommerce_retail","trigger_date":"2025-06-05","event_return_pct":"dAlba_>2x_since_debut","trigger_outcome_label":"Stage2_channel_expansion_not_Green","promote_to":"Stage2"}
{"trigger_id":"r5l17_china_tourism_T1","case_id":"r5_loop17_china_visa_free_tourism_retail","trigger_type":"Stage2-Actionable_tourism_retail_policy","trigger_date":"2025-08-06","event_return_pct":"Hyundai_Dept_+7.1_Hotel_Shilla_+4.8_Hankook_Cosmetics_+9.9","trigger_outcome_label":"excellent_stage2_actionable_china_tourism_retail","promote_to":"Stage2-Actionable"}
{"trigger_id":"r5l17_coupang_breach_T1","case_id":"r5_loop17_coupang_trust_break_retail_shift","trigger_type":"hard_4C_ecommerce_trust_break","trigger_date":"2025-11_to_2026-02","event_return_pct":-34,"trigger_outcome_label":"hard_4C_success","promote_to":"4C"}
{"trigger_id":"r5l17_coupang_rival_T2","case_id":"r5_loop17_coupang_trust_break_retail_shift","trigger_type":"rival_Stage2_retail_share_shift","trigger_date":"2026-02-25","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"rival_stage2_needs_revenue_margin","promote_to":"Stage2"}
{"trigger_id":"r5l17_baemin_naver_T0","case_id":"r5_loop17_baemin_uber_naver_ma","trigger_type":"Stage2_food_delivery_platform_MA","trigger_date":"2026-05-18","event_return_pct":"Delivery_Hero_proxy_+5.6","trigger_outcome_label":"Stage2_MA_not_Green","promote_to":"Stage2+4B"}
{"trigger_id":"r5l17_amore_china_T0","case_id":"r5_loop17_amorepacific_china_prestige_failed_rerating","trigger_type":"failed_rerating_china_prestige_beauty","trigger_date":"2024-08","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"legacy_china_exposure_4B","promote_to":"4B-watch"}
{"trigger_id":"r5l17_dr_g_loreal_T0","case_id":"r5_loop17_dr_g_loreal_kbeauty_ma","trigger_type":"Stage2_Kbeauty_MA_reference_no_price","trigger_date":"2024-12-23","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"MA_reference_not_actionable","promote_to":"Stage2_reference"}
```

## data/sector_taxonomy/score_weight_profiles_round254_r5_loop17_v1.csv 초안

```csv
archetype,export_ASP_shipment_capacity,brand_viral_to_export_conversion,overseas_revenue_mix,US_retail_shelf_in,tourism_policy_price_reaction,consumer_trust_security,MAU_spending_conversion,M&A_finality,viral_brand_without_sellthrough_penalty,Kbeauty_export_without_offline_sales_penalty,tourism_headline_without_basket_size_penalty,legacy_china_exposure_ignored_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
K_FOOD_EXPORT_ASP_STAGE2_ACTIONABLE,+5,+5,+3,+2,+0,+1,+0,+0,-5,-1,-1,-1,Samyang Buldak export,regulatory/viral risk,repeat sell-through+margin+capacity,Samyang.
K_BEAUTY_DEVICE_GLOBAL_STAGE2_YELLOW,+2,+5,+5,+3,+0,+1,+0,+0,-5,-3,-1,-1,APR device global momentum,overheat/regulation/tariff,repeat device sales+margin,APR.
K_BEAUTY_INDIE_US_RETAIL_STAGE2,+1,+4,+4,+5,+0,+1,+0,+0,-4,-5,-1,-2,U.S. K-beauty ecommerce growth,physical sell-through missing,retail reorder+margin,d'Alba/Silicon2/Olive Young.
CHINA_TOURISM_DUTY_FREE_STAGE2_ACTIONABLE,+0,+1,+1,+0,+5,+1,+0,+0,-1,-1,-5,-2,visa-free Chinese tourism stock reaction,basket size missing,visitor volume+basket+OP,Hotel Shilla/Hyundai Dept.
ECOMMERCE_TRUST_BREAK_HARD_4C,+0,+0,+0,+0,+0,+5,+5,+0,-1,-1,-1,-1,Coupang breach damaged trust,hard 4C,rival GMV/margin conversion,Coupang/Naver/CJ.
FOOD_DELIVERY_PLATFORM_MA_STAGE2_WITH_APPROVAL_4B,+0,+1,+0,+0,+0,+1,+3,+5,-1,-1,-1,-1,Baemin M&A headline,final SPA missing,approval+economics,Baemin/Naver/Uber.
CHINA_PRESTIGE_BEAUTY_FAILED_RERATING,+0,+0,+2,+1,+1,+0,+0,+0,-1,-1,-1,-5,Amore China exposure,failed rerating,US/EU mix+margin recovery,Amorepacific.
K_BEAUTY_MA_VALUATION_STAGE2_NO_PRICE,+0,+2,+2,+2,+0,+0,+0,+3,-2,-1,-1,-1,Dr.G L'Oreal M&A reference,no valuation/public price,valuation comps+listed beneficiary,Dr.G.
```

---

# 이번 R5 Loop 17 결론

```text
1. Samyang Foods / Buldak은 R5의 가장 좋은 Stage2-Actionable이다.
   +5.7%, OP estimate +84%, ASP·shipment·capacity evidence가 닫혔다.

2. APR / Medicube는 Stage2_promote / Yellow 후보이다.
   stock >4x, $6B valuation, overseas revenue nearly 80%는 강하지만 celebrity/viral overheat와 tariff/regulation 4B가 있다.

3. K-beauty indie / d’Alba / Silicon2는 Stage2 channel expansion이다.
   U.S. e-commerce +71%, d’Alba >2x는 강하지만 physical-store sell-through가 gate다.

4. China visa-free tourism은 Stage2-Actionable이다.
   Hyundai Dept +7.1%, Hotel Shilla +4.8%, Hankook Cosmetics +9.9%가 바로 반응했다.

5. Coupang은 hard 4C다.
   -34%, MAU -3.5%, spending -6.3%, Q4 loss, KFTC fine까지 trust/margin model이 깨졌다.

6. Baemin / Uber-Naver는 Stage2 M&A다.
   8T won bid와 Delivery Hero +5.6% proxy는 좋지만, Naver final decision이 없다.

7. Amorepacific은 failed_rerating / China exposure 4B다.
   U.S.-focused indie K-beauty와 China-exposed prestige beauty를 반드시 분리해야 한다.

8. Dr.G / L’Oréal은 K-beauty M&A valuation reference다.
   글로벌 buyer의 K-beauty appetite는 확인되지만 valuation과 public price anchor가 없다.
```

한 문장으로 압축하면:

> **R5 Loop 17에서 배운 핵심은 “K-food·K-beauty·중국 관광·이커머스 headline”이 아니라, export ASP/shipments, overseas revenue mix, U.S. physical sell-through, visitor basket size, MAU/spending, final M&A agreement가 닫혀야 Stage3로 올릴 수 있다는 것이다. 반대로 viral brand, teaser M&A, 관광객 숫자, K-beauty export headline만으로 Green을 주면 tariff·China weakness·trust break·sell-through failure에 false positive가 난다.**

다음 순서는 **R6 Loop 17 — 금융·자본배분·디지털금융**이다.

[1]: https://www.marketwatch.com/story/samyang-foods-set-to-post-strong-2q-earnings-market-talk-d654e045 "https://www.marketwatch.com/story/samyang-foods-set-to-post-strong-2q-earnings-market-talk-d654e045"
[2]: https://www.ft.com/content/6a0f7e2c-f3b9-4eb6-961c-d69af28f7183 "https://www.ft.com/content/6a0f7e2c-f3b9-4eb6-961c-d69af28f7183"
[3]: https://www.reuters.com/world/asia-pacific/korean-beauty-startups-bet-booming-us-demand-outlasts-tariff-pain-2025-06-05/ "https://www.reuters.com/world/asia-pacific/korean-beauty-startups-bet-booming-us-demand-outlasts-tariff-pain-2025-06-05/"
[4]: https://www.reuters.com/world/china/south-korea-offer-visa-free-entry-chinese-tourists-late-september-2025-08-06/ "https://www.reuters.com/world/china/south-korea-offer-visa-free-entry-chinese-tourists-late-september-2025-08-06/"
[5]: https://www.reuters.com/business/retail-consumer/coupang-braces-increased-competition-amid-fallout-south-korea-data-breach-2026-02-25/ "https://www.reuters.com/business/retail-consumer/coupang-braces-increased-competition-amid-fallout-south-korea-data-breach-2026-02-25/"
[6]: https://www.reuters.com/world/asia-pacific/uber-naver-team-up-baemin-takeover-seoul-economic-daily-2026-05-18/ "https://www.reuters.com/world/asia-pacific/uber-naver-team-up-baemin-takeover-seoul-economic-daily-2026-05-18/"
[7]: https://www.ft.com/content/6b101349-55b1-4a72-bb21-0b77bf3c5f03 "https://www.ft.com/content/6b101349-55b1-4a72-bb21-0b77bf3c5f03"
[8]: https://www.reuters.com/markets/deals/frances-loreal-acquires-migros-south-korean-cosmetic-unit-2024-12-23/ "https://www.reuters.com/markets/deals/frances-loreal-acquires-migros-south-korean-cosmetic-unit-2024-12-23/"

순서상 이번은 **R5 Loop 15 — 소비재·유통·브랜드 trigger-level price validation 라운드**다.

이번 R5의 핵심은 “K-푸드 / K-뷰티 / 면세 / 유통 / 브랜드가 좋다”가 아니라, **브랜드 인지도·해외 수요·가격전가·오프라인 입점·관광객 회복·M&A·meme 이벤트 중 어느 trigger가 실제 entry였고, 어느 trigger는 4B/false positive였는지**를 분리하는 것이다.

```text
round = R5 Loop 15
round_id = round_228
large_sector = CONSUMER_RETAIL_BRAND
method = trigger_level_backtest_v1
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R6 Loop 15
```

이번에도 KRX/Naver/Yahoo/Stooq의 수정주가 일봉 OHLC 30D/90D/180D/1Y window를 안정적으로 직접 추출하지 못했다. 그래서 full MFE/MAE는 `price_data_unavailable_after_deep_search`로 두고, Reuters/FT/WSJ/MarketWatch/AP가 보도한 **reported event return, event price, target price, OP estimate, export/sales data, tourist-arrival data, deal value**를 trigger anchor로 쓴다. 단, **OHLC 미확보를 이유로 Stage 후보 자체를 강등하지 않는다.**

---

# 1. 이번 라운드 대섹터

```text
R5 = 소비재·유통·브랜드
```

R5의 핵심 gate는 아래다.

```text
K-food:
해외 바이럴 → 실제 수출/출하 → ASP 상승 → 생산능력 → OP estimate 상향 → regulatory recall risk

K-beauty:
SNS/인플루언서 → ecommerce sell-through → 미국/유럽 오프라인 입점 → ODM/brand margin → tariff/rival competition

면세/관광소비:
비자정책 → 실제 입국자 수 → 객단가/결제액 → 면세/호텔/카지노 매출 → 중국 정치 리스크

유통/e-commerce:
JV/M&A → market share → customer data / regulatory approval → take-rate / GMV → margin

프랜차이즈/외식:
유명인 이벤트 → same-store sales → franchise fee → 원가율 → 반복매출

브랜드 M&A:
전략투자 → control rights → full acquisition → funding → brand integration → ROIC
```

---

# 2. 대상 canonical archetype

```text
K_FOOD_EXPORT_STAGE2_TO_STAGE3_YELLOW
K_FOOD_REGULATORY_FALSE_BREAK_4C_WATCH
K_BEAUTY_US_EXPORT_STAGE2_ACTIONABLE
BEAUTY_DEVICE_VIRAL_STAGE3_WITH_4B
CHINA_TOURIST_DUTYFREE_STAGE2_ACTIONABLE
ECOMMERCE_JV_STAGE2_WITH_DATA_REGULATORY_4B
BRAND_MA_CONTROL_RIGHTS_STAGE2
FRIED_CHICKEN_MEME_PRICE_MOVED_WITHOUT_EVIDENCE
RAMEN_GLOBAL_EXPANSION_STAGE2
TOURISM_REROUTE_EVENT_PREMIUM
```

---

# 3. deep sub-archetype

```text
Samyang Foods:
- Buldak export
- ASP 상승
- 미국/유럽 shipment 증가
- 생산능력 증설
- OP estimate +84%
- Denmark recall / ban reversal as regulatory false-break

Nongshim:
- Shin Ramyun global expansion
- 2023 Shin Ramyun sales 1.2T won / $883M
- nearly 60% abroad
- U.S. $1.5B target by 2030
- China slowdown / Europe execution gate

K-beauty:
- Amorepacific / Silicon2 / Cosmax / Kolmar / APR / d'Alba
- U.S. ecommerce sell-through
- physical retail entry at Ulta / Sephora / Target / Costco
- Korea overtakes France as top cosmetics exporter to U.S.
- top-five Korean ecommerce brands +71% vs U.S. market +21%

APR / beauty devices:
- Medicube device
- Kylie Jenner TikTok trigger
- APR valuation $6B
- stock more than 4x since January
- overseas Q2 revenue nearly 80%
- 4B valuation / tariff / competition overlay

Chinese tourist recovery:
- Hotel Shilla / Hyundai Department Store / Hankook Cosmetics / Paradise / Lotte Tour
- China group visa-free policy
- Chinese visitor share 28% in 2024
- department stores / hotels / casinos / beauty makers rally
- anti-Chinese protests / diplomatic risk overlay

Shinsegae / E-Mart / Alibaba:
- Gmarket + AliExpress Korea JV
- $4B JV
- conditional KFTC approval
- cross-border ecommerce market share 41%
- customer-data sharing blocked for 3 years

F&F / TaylorMade:
- F&F consent rights / ROFR
- TaylorMade possible $3.5B sale
- brand M&A is Stage2, not Green until funding/control/ROIC

Kyochon / Cherrybro / Neuromeka:
- Jensen Huang Kkanbu Chicken event
- Kkanbu not listed
- Kyochon / Cherrybro / Neuromeka surge
- no direct revenue evidence
```

---

# 4. 선정 case 요약

| bucket                             | case                               | 핵심 판정                                                                                                        |
| ---------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| structural_success / Stage3-Yellow | Samyang Foods / Buldak             | OP estimate +84%, ASP 상승, U.S./Europe shipment, capacity, +5.7% close. 기존 Stage2로 두면 늦음                      |
| regulatory 4C false-break          | Samyang Denmark recall             | spiciness recall은 brand/regulatory watch였지만 일부 ban reversal로 hard 4C는 아님                                     |
| Stage2-Actionable                  | K-beauty basket                    | U.S. ecommerce +71%, Korea top U.S. cosmetics exporter, physical-store entry. 단 tariff/brick-and-mortar gate |
| Stage3-Yellow + 4B                 | APR / Medicube                     | stock 4x, valuation $6B, overseas Q2 revenue nearly 80%, beauty-device viral. 과열 overlay 필요                  |
| Stage2-Actionable                  | Chinese tourism / duty-free basket | Hyundai Dept +7.1%, Hotel Shilla +4.8%, Hankook Cosmetics +9.9% on visa-free policy                          |
| Stage2 with 4B/regulatory          | E-Mart / Shinsegae / Alibaba JV    | $4B JV, conditional approval, 41% cross-border share, 3-year data-sharing ban                                |
| Stage2 brand M&A                   | F&F / TaylorMade                   | $3.5B possible sale, F&F invested 358B won, consent rights/ROFR. control/funding gate                        |
| price_moved_without_evidence       | Kyochon / Cherrybro / Neuromeka    | Jensen chicken meme. Kkanbu not listed, no direct revenue link                                               |

---

# 5. Case별 trigger grid

## Case A — Samyang Foods / Buldak export

```text
symbol = 003230
case_type = structural_success / Stage2_promote_candidate / Stage3-Yellow
archetype = K_FOOD_EXPORT_STAGE2_TO_STAGE3_YELLOW
```

### Trigger grid

| trigger | type                   |                                  date | 당시 공개 evidence                                                                             | 가격 anchor                       | outcome               |
| ------- | ---------------------- | ------------------------------------: | ------------------------------------------------------------------------------------------ | ------------------------------- | --------------------- |
| T0      | earliest awareness     |                             2023~2024 | Buldak global viral demand, K-food export momentum                                         | full OHLC unavailable           | Stage1                |
| T1      | Stage2 evidence        |                            2024-06-14 | Kiwoom raises 2Q OP estimate to 81.2B won, +84% YoY                                        | shares +5.7%, close 647,000 won | Stage2-Actionable     |
| T2      | Stage3-Yellow          |                            2024-06-14 | ASP 상승, U.S./Europe shipment 증가, production capacity expansion, target +26% to 830,000 won | target upside 28.3%             | Stage3-Yellow         |
| T3      | 4C-watch               |                            2024-06-12 | Denmark recalls three Buldak variants over capsaicin / acute-poisoning risk                | price unavailable               | regulatory watch      |
| T4      | false-break / relief   |                            2024-08-08 | Denmark partially reverses ban; two of three variants return                               | no KRX price                    | false-break relief    |
| T5      | Stage3-Green candidate | 2024 actual export/sales confirmation | overseas sales surged in 2024, but exact trigger OHLC unavailable                          | unavailable                     | pending               |
| T6      | hard 4C                |                                   N/A | quality defect not confirmed                                                               | N/A                             | hard_4c_not_confirmed |

Samyang은 R5에서 가장 중요한 **missed_structural 후보**다. 2024년 6월 14일 MarketWatch/Dow Jones에 따르면 Kiwoom은 2Q OP estimate를 81.2B won으로 올렸고, 이는 전년 대비 +84%였다. 근거도 단순 “K-food 인기”가 아니라 **Buldak ASP 상승, 미국·유럽 shipment 증가, 생산능력 증설**이었다. 주가는 +5.7%로 647,000 won에 마감했고, target은 +26% 오른 830,000 won이었다. 이 조합은 기존 Stage2로만 두면 너무 보수적이고, 최소 `Stage2-Actionable`, 더 정확히는 `Stage3-Yellow`다. ([마켓워치][1])

반면 Denmark recall은 4C-watch였지만 hard 4C는 아니었다. AP는 Denmark가 세 가지 Buldak 제품을 capsaicin risk로 recall했다고 보도했고, Reuters는 이후 두 가지 variant의 ban이 뒤집혔다고 보도했다. 즉 이건 “브랜드 품질 붕괴”가 아니라 **spiciness/regulatory false-break**에 가깝다. ([AP News][2])

### Trigger price validation row

```json
{
  "case_id": "r5_loop15_samyang_buldak_export",
  "symbol": "003230",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable_to_Stage3-Yellow",
  "trigger_date": "2024-06-14",
  "entry_price_anchor_krw": 647000,
  "event_return_pct": 5.7,
  "q2_2024_op_estimate_krw_bn": 81.2,
  "q2_2024_op_estimate_yoy_pct": 84,
  "target_price_krw": 830000,
  "target_price_raise_pct": 26,
  "target_upside_from_entry_pct": 28.3,
  "evidence_factors": [
    "Buldak ASP increase",
    "U.S. shipment growth",
    "Europe shipment growth",
    "production capacity expansion"
  ],
  "regulatory_watch_date": "2024-06-12",
  "denmark_recall_variants": 3,
  "ban_partially_reversed_date": "2024-08-08",
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "missed_structural_if_old_stage2_gate_used",
  "stage_gate_correction": "ASP + shipment + capacity + OP estimate beat should promote Stage2 to Stage3-Yellow"
}
```

### 판정

```text
score_price_alignment = missed_structural_if_old_gate_used
old_label = Stage 2 / success_candidate
new_label = Stage2-Actionable → Stage3-Yellow
key_rule = 브랜드 viral만으로는 부족하지만, ASP·shipment·capacity·OP estimate가 같이 닫히면 Yellow 승격
```

---

## Case B — Nongshim / Shin Ramyun global expansion

```text
symbol = 004370
case_type = success_candidate_stage2
archetype = RAMEN_GLOBAL_EXPANSION_STAGE2
```

### Trigger grid

| trigger | type                        |       date | 당시 공개 evidence                                                        | 가격 anchor         | outcome               |
| ------- | --------------------------- | ---------: | --------------------------------------------------------------------- | ----------------- | --------------------- |
| T0      | awareness                   |       2023 | Korean ramen exports hit record $1B; Shin Ramyun global sales strong  | no direct price   | Stage1                |
| T1      | Stage2 evidence             | 2024-05-27 | Shin Ramyun 2023 sales 1.2T won / $883M, nearly 60% abroad            | price unavailable | Stage2                |
| T2      | Stage2-Actionable candidate | 2024-05-27 | Nongshim aims to triple U.S. annual sales to $1.5B by 2030            | price unavailable | candidate             |
| T3      | 4B-watch                    | 2024-05-27 | China sales slowed; Europe expansion has local-culture execution risk | no price          | execution watch       |
| T4      | Stage3-Yellow               |        N/A | OP estimate / ASP / shipment growth not located with price anchor     | N/A               | no Yellow             |
| T5      | hard 4C                     |        N/A | 없음                                                                    | N/A               | hard_4c_not_confirmed |

Nongshim은 Samyang보다 **Stage2 evidence는 강하지만 trigger price가 부족한 case**다. FT는 Korean ramen exports가 record $1B였고, Nongshim의 Shin Ramyun 2023 sales가 1.2T won, 약 $883M였으며 그중 거의 60%가 해외에서 나왔다고 보도했다. Nongshim은 2030년까지 미국 annual sales를 $1.5B로 키우겠다는 목표도 제시했다. 다만 이 trigger에는 OP estimate beat나 당일 주가 anchor가 없기 때문에 Stage3-Yellow로 올리기 어렵다. ([Financial Times][3])

### Trigger price validation row

```json
{
  "case_id": "r5_loop15_nongshim_shinramyun_global",
  "symbol": "004370",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2_success_candidate",
  "trigger_date": "2024-05-27",
  "korean_ramen_exports_2023_usd_bn": 1.0,
  "shin_ramyun_2023_sales_krw_trn": 1.2,
  "shin_ramyun_2023_sales_usd_mn": 883,
  "overseas_sales_share_pct": 60,
  "us_sales_target_2030_usd_bn": 1.5,
  "stage3_gate_missing": [
    "OP estimate revision",
    "ASP increase",
    "shipment data by region",
    "production capacity",
    "event price anchor"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "success_candidate_stage2_not_yellow"
}
```

### 판정

```text
score_price_alignment = success_candidate_stage2
reason = 해외 매출과 목표는 강하지만 OP estimate / price trigger가 없어 Stage2 유지
```

---

## Case C — K-beauty export / Silicon2·Cosmax·Kolmar·Amore basket

```text
symbols = 257720 / 192820 / 161890 / 090430 / beauty_basket
case_type = Stage2-Actionable / structural_success_candidate
archetype = K_BEAUTY_US_EXPORT_STAGE2_ACTIONABLE
```

### Trigger grid

| trigger | type                    |       date | 당시 공개 evidence                                                                                    | 가격 anchor             | outcome               |
| ------- | ----------------------- | ---------: | ------------------------------------------------------------------------------------------------- | --------------------- | --------------------- |
| T0      | awareness               |       2024 | Korea becomes world’s third-largest beauty exporter; U.S. demand expands                          | no direct price       | Stage1                |
| T1      | Stage2 evidence         | 2025-06-05 | Korea replaced France as biggest cosmetics exporter to U.S. in 2024                               | no specific KRX price | Stage2                |
| T2      | Stage2-Actionable       | 2025-06-05 | top five Korean cosmetics brands in U.S. ecommerce +71% over two years vs U.S. market +21%        | no direct price       | Actionable candidate  |
| T3      | Stage3-Yellow candidate | 2025-06-05 | Ulta/Sephora/Target/Costco physical-store talks; ODMs Cosmax/Kolmar benefit from outsourced model | no full OHLC          | Yellow candidate      |
| T4      | 4B-watch                | 2025-06-05 | tariffs, saturation, COSRX plateau, need physical-store success                                   | no price              | 4B/watch              |
| T5      | hard 4C                 |        N/A | 없음                                                                                                | N/A                   | hard_4c_not_confirmed |

K-beauty basket은 R5의 구조적 성공 후보지만, 아직 case 단위 full OHLC가 필요하다. Reuters는 South Korea가 2024년에 France를 제치고 U.S. 최대 cosmetics exporter가 됐고, U.S. ecommerce top-five Korean brands의 online sales가 2년간 평균 +71% 성장해 overall U.S. market +21%를 크게 이겼다고 보도했다. 또한 Tirtir, d’Alba, Torriden, Beauty of Joseon 등이 Ulta, Sephora, Target, Costco 등과 오프라인 입점을 논의하고 있으며, Cosmax와 Kolmar가 outsourced fast-beauty 생산 모델의 수혜 업체라고 설명했다. ([Reuters][4])

다만 Reuters는 COSRX growth plateau, 경쟁 심화, tariffs, physical-store execution 필요성도 같이 지적했다. 그래서 이 trigger는 `Stage2-Actionable` 또는 `Stage3-Yellow candidate`이지, 아직 Green은 아니다. ([Reuters][4])

### Trigger price validation row

```json
{
  "case_id": "r5_loop15_kbeauty_us_export_basket",
  "symbols": "257720/192820/161890/090430/beauty_basket",
  "best_trigger": "T2/T3",
  "best_trigger_type": "Stage2-Actionable_to_Stage3-Yellow_candidate",
  "trigger_date": "2025-06-05",
  "korea_replaced_france_as_top_us_cosmetics_exporter": true,
  "top5_korean_us_ecommerce_sales_growth_2y_pct": 71,
  "overall_us_market_growth_2y_pct": 21,
  "top5_french_brands_growth_2y_pct": 15,
  "retail_channels_under_discussion": [
    "Ulta Beauty",
    "Sephora",
    "Target",
    "Costco"
  ],
  "odm_beneficiaries": [
    "Cosmax",
    "Kolmar Korea"
  ],
  "stage3_gate_missing": [
    "physical_store_sell_through",
    "brand_repeat_purchase",
    "ODM margin",
    "tariff pass-through",
    "inventory"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_promote_candidate"
}
```

### 판정

```text
score_price_alignment = Stage2_promote_candidate
reason = ecommerce sell-through + U.S. export rank + physical-store channel trigger는 plain Stage2보다 강함
```

---

## Case D — APR / Medicube beauty-device viral cycle

```text
symbol = APR / beauty_device_basket
case_type = Stage3-Yellow candidate + 4B-watch
archetype = BEAUTY_DEVICE_VIRAL_STAGE3_WITH_4B
```

### Trigger grid

| trigger | type            |            date | 당시 공개 evidence                                                                           | 가격 anchor                                              | outcome               |
| ------- | --------------- | --------------: | ---------------------------------------------------------------------------------------- | ------------------------------------------------------ | --------------------- |
| T0      | awareness       |        2024 IPO | APR goes public; Medicube device category expands                                        | no direct price here                                   | Stage1                |
| T1      | Stage2 evidence | 2025-07~2025-10 | Kylie Jenner TikTok / Medicube Booster Pro viral success                                 | stock up 75% since IPO / 4x since Jan depending source | Stage2-Actionable     |
| T2      | Stage3-Yellow   |      2025-10-20 | APR valuation $6B, overseas nearly 80% Q2 revenue, beauty device one-third of U.S. sales | stock more than 4x since January                       | Yellow                |
| T3      | 4B-watch        |      2025-10-20 | valuation already $6B, tariff / Europe regulation / competition risk                     | no OHLC                                                | 4B-watch              |
| T4      | Stage3-Green    |             N/A | sustained margin / channel repeat purchase not confirmed                                 | N/A                                                    | no Green              |
| T5      | hard 4C         |             N/A | 없음                                                                                       | N/A                                                    | hard_4c_not_confirmed |

APR/Medicube는 K-beauty 안에서도 “화장품”보다 **beauty-device brand**에 가까운 case다. FT는 APR stock이 2025년 1월 이후 4배 이상 올랐고 valuation이 $6B에 가까워졌으며, 2025년 Q2 매출의 거의 80%가 해외에서 나왔다고 보도했다. Medicube facial device는 Kylie Jenner TikTok promotion 이후 U.S. consumers에게 반응했고, 해당 device category가 U.S. sales의 약 3분의 1을 형성했다. ([Financial Times][5])

이건 단순 influencer meme이 아니라 **제품 category + 해외 매출 mix + valuation rerating**이 연결된 trigger라 Stage3-Yellow 후보가 맞다. 하지만 주가가 이미 4배라 4B valuation overlay가 필요하다. ([Financial Times][5])

### Trigger price validation row

```json
{
  "case_id": "r5_loop15_apr_medicube_beauty_device",
  "symbol": "APR/beauty_device_basket",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage3-Yellow_with_4B_overlay",
  "trigger_date": "2025-10-20",
  "stock_return_since_january_pct": 300,
  "valuation_usd_bn": 6,
  "overseas_revenue_share_q2_2025_pct": 80,
  "beauty_device_share_of_us_sales_pct": 33,
  "product_price_usd": 180,
  "viral_trigger": "Kylie Jenner TikTok / Medicube device",
  "stage3_gate_missing": [
    "sustained_repeat_purchase",
    "retail_channel_expansion",
    "device_margin",
    "tariff_absorption",
    "competition_response"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage3_Yellow_with_4B_valuation_overlay"
}
```

### 판정

```text
score_price_alignment = Stage3-Yellow_candidate_with_4B
reason = 제품 category와 해외 매출이 실제로 붙었지만, 4배 상승 이후 valuation overlay 필요
```

---

## Case E — Chinese tourist visa-free / duty-free·department·beauty basket

```text
symbols = 008770 / 069960 / 123690 / 034230 / 032350
company_scope = Hotel Shilla / Hyundai Department Store / Hankook Cosmetics / Paradise / Lotte Tour Development
case_type = Stage2-Actionable / event premium
archetype = CHINA_TOURIST_DUTYFREE_STAGE2_ACTIONABLE
```

### Trigger grid

| trigger | type              |       date | 당시 공개 evidence                                                                 | 가격 anchor                                                                       | outcome               |
| ------- | ----------------- | ---------: | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- | --------------------- |
| T0      | awareness         | 2025-03-20 | government announces plan for temporary visa waiver for Chinese group tourists | no basket return                                                                | Stage1                |
| T1      | Stage2 evidence   | 2025-08-06 | visa-free entry for Chinese tourist groups Sep 29~Jun 2026 confirmed           | Hyundai Dept +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9% | Stage2-Actionable     |
| T2      | Stage2-Actionable | 2025-09-29 | program starts; groups of 3+ can stay 15 days visa-free                        | Shilla Duty Free Chinese cruise tours, Baemin Alipay/WeChat Pay                 | Actionable            |
| T3      | 4B-watch          | 2025-10-02 | anti-Chinese protests risk national image / safety; government crackdown       | no direct price                                                                 | political/social risk |
| T4      | event premium     | 2025-11-17 | Japan-China rift reroutes Chinese tourism, Lotte Tour +9.6%                    | Lotte Tour +9.6%                                                                | event premium         |
| T5      | Stage3-Green      |        N/A | actual foot traffic / duty-free sales / hotel ADR not confirmed                | N/A                                                                             | no Green              |

Chinese tourist recovery basket은 R5에서 **policy-to-consumption Stage2-Actionable**이다. 2025년 8월 6일 Reuters는 China tourist group visa-free policy를 보도했고, Hyundai Department Store +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9%가 올랐다. 이건 단순 관광 기대가 아니라 **비자정책 + department/hotel/casino/beauty basket relative strength**가 같이 닫힌 trigger다. ([Reuters][6])

9월 29일 실제 프로그램이 시작됐고, Reuters는 중국 group tourists가 3명 이상이면 15일간 visa-free stay가 가능하다고 보도했다. Shilla Duty Free는 Chinese cruise tour를 준비했고, Baemin은 Alipay/WeChat Pay 결제를 도입했다. 다만 foot traffic, 객단가, duty-free sales가 확인되기 전까지 Green은 아니다. ([Reuters][7])

### Trigger price validation row

```json
{
  "case_id": "r5_loop15_china_tourist_visa_free_retail_basket",
  "symbols": "008770/069960/123690/034230/032350",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable",
  "t1_date": "2025-08-06",
  "visa_free_period": "2025-09-29_to_2026-06",
  "hyundai_department_store_event_return_pct": 7.1,
  "hotel_shilla_event_return_pct": 4.8,
  "paradise_event_return_pct": 2.9,
  "hankook_cosmetics_event_return_pct": 9.9,
  "t2_date": "2025-09-29",
  "group_size_min": 3,
  "visa_free_stay_days": 15,
  "china_share_of_2024_korea_visitors_pct": 28,
  "korea_2024_visitors_mn": 16.4,
  "t4_lotte_tour_event_return_pct": 9.6,
  "stage3_gate_missing": [
    "actual_arrivals",
    "foreign_card_spending",
    "duty_free_sales",
    "hotel_ADR",
    "casino_drop",
    "beauty_store_sellthrough"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_Actionable_tourism_consumption"
}
```

### 판정

```text
score_price_alignment = Stage2_promote_candidate
reason = 비자정책 + 다수 소비주 동반 상승은 Stage2-Actionable, 하지만 실제 매출 전에는 Green 아님
```

---

## Case F — E-Mart / Shinsegae / Alibaba-Gmarket JV

```text
symbols = 139480 / 004170
company_scope = E-Mart / Shinsegae / Gmarket / AliExpress Korea
case_type = Stage2 with regulatory 4B
archetype = ECOMMERCE_JV_STAGE2_WITH_DATA_REGULATORY_4B
```

### Trigger grid

| trigger | type              |       date | 당시 공개 evidence                                                                        | 가격 anchor         | outcome              |
| ------- | ----------------- | ---------: | ------------------------------------------------------------------------------------- | ----------------- | -------------------- |
| T0      | Stage1            | 2024-12-26 | Shinsegae/E-Mart plans JV with Alibaba International; Gmarket + AliExpress Korea      | price unavailable | Stage2               |
| T1      | Stage2 evidence   | 2024-12-26 | JV estimated around $4B; Gmarket struggling against Coupang/Naver/AliExpress/Temu     | price unavailable | restructuring Stage2 |
| T2      | Stage2 validation | 2025-09-18 | KFTC conditionally approves JV                                                        | no price          | Stage2               |
| T3      | 4B/regulatory     | 2025-09-18 | 50M Gmarket customers, data sharing barred for 3 years, cross-border market share 41% | no price          | regulatory overlay   |
| T4      | Stage3-Yellow     |        N/A | GMV/take-rate/margin improvement not confirmed                                        | N/A               | no Yellow            |

E-Mart/Shinsegae-Alibaba JV는 R5 유통에서 **e-commerce restructuring Stage2**다. Reuters는 2024년 12월 Shinsegae affiliate E-Mart가 Gmarket을 Alibaba International과의 JV에 투입한다고 보도했고, Bloomberg 기반 보도는 deal value가 약 $4B라고 전했다. 이 구조는 Gmarket이 Coupang, Naver, AliExpress, Temu와 경쟁에서 어려움을 겪는 상황의 구조조정 trigger다. ([Reuters][8])

2025년 9월 KFTC는 JV를 조건부 승인했지만, Gmarket의 50M customer data와 Alibaba data analytics 결합을 우려했고, 3년간 Korean customers’ overseas shopping data 공유를 금지했다. JV의 cross-border e-commerce market share는 41%로 추정됐다. 따라서 Stage2는 맞지만, GMV/take-rate/margin 전에는 Green이 아니다. ([Reuters][9])

### Trigger price validation row

```json
{
  "case_id": "r5_loop15_emart_shinsegae_alibaba_gmarket_jv",
  "symbols": "139480/004170",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2_with_regulatory_4B_overlay",
  "t0_date": "2024-12-26",
  "jv_estimated_value_usd_bn": 4,
  "assets_combined": [
    "Gmarket",
    "AliExpress Korea"
  ],
  "t2_date": "2025-09-18",
  "kftc_conditional_approval": true,
  "gmarket_customer_database_mn": 50,
  "data_sharing_restriction_years": 3,
  "cross_border_ecommerce_market_share_pct": 41,
  "china_import_online_spending_2024_krw_trn": 4.7,
  "alibaba_share_of_china_online_import_sales_pct": 62,
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "GMV_growth",
    "take_rate",
    "customer_retention",
    "regulatory_compliance",
    "margin_improvement"
  ],
  "trigger_outcome_label": "Stage2_restructuring_with_data_regulatory_overlay"
}
```

### 판정

```text
score_price_alignment = success_candidate_stage2
reason = JV와 conditional approval은 구조조정 trigger지만, 데이터 규제와 수익성 확인 전에는 Green 아님
```

---

## Case G — F&F / TaylorMade strategic brand M&A

```text
symbol = 383220
case_type = Stage2 brand M&A / governance-control watch
archetype = BRAND_MA_CONTROL_RIGHTS_STAGE2
```

### Trigger grid

| trigger | type                        |       date | 당시 공개 evidence                                                          | 가격 anchor                | outcome          |
| ------- | --------------------------- | ---------: | ----------------------------------------------------------------------- | ------------------------ | ---------------- |
| T0      | awareness                   |       2021 | F&F invested 358B won in TaylorMade acquisition as strategic investor   | no current price         | Stage1           |
| T1      | Stage2 evidence             | 2025-07-21 | F&F hires Goldman Sachs for TaylorMade acquisition                      | direct price unavailable | Stage2           |
| T2      | Stage2-Actionable candidate | 2025-07-21 | TaylorMade potential sale value $3.5B, F&F claims consent rights / ROFR | no price                 | M&A optionality  |
| T3      | 4B-watch                    | 2025-07-21 | legal dispute with Centroid sale process; funding/control risk          | no price                 | governance watch |
| T4      | Stage3-Yellow               |        N/A | full acquisition/funding/ROIC not confirmed                             | N/A                      | no Yellow        |

F&F는 R5 브랜드 M&A case다. Reuters는 F&F가 TaylorMade acquisition 자문을 위해 Goldman Sachs를 고용했고, TaylorMade sale value가 약 $3.5B일 수 있다고 보도했다. F&F는 2021년 TaylorMade 인수에 358B won을 투자했고, consent rights와 ROFR을 갖고 있다고 주장했다. 이건 단순 apparel retail이 아니라 **global sports brand control optionality** trigger다. 다만 legal dispute, funding, full ownership, ROIC가 확인되기 전까지 Stage2에 머문다. ([Reuters][10])

### Trigger price validation row

```json
{
  "case_id": "r5_loop15_fnf_taylormade_brand_ma",
  "symbol": "383220",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2_brand_MA_optional",
  "trigger_date": "2025-07-21",
  "fnf_2021_investment_krw_bn": 358,
  "taylormade_possible_sale_value_usd_bn": 3.5,
  "advisor": "Goldman Sachs",
  "claimed_rights": [
    "Consent Rights",
    "ROFR"
  ],
  "dispute_party": "Centroid Investment Partners",
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "acquisition_price",
    "funding",
    "control execution",
    "brand integration",
    "ROIC",
    "legal resolution"
  ],
  "trigger_outcome_label": "Stage2_brand_MA_control_rights"
}
```

### 판정

```text
score_price_alignment = success_candidate_stage2
reason = global brand optionality는 Stage2지만 funding/control/ROIC 전에는 Green 아님
```

---

## Case H — Kyochon / Cherrybro / Neuromeka Jensen chicken rally

```text
symbols = 339770 / 066360 / 348340
case_type = price_moved_without_evidence
archetype = FRIED_CHICKEN_MEME_PRICE_MOVED_WITHOUT_EVIDENCE
```

### Trigger grid

| trigger | type                         |       date | 당시 공개 evidence                                                                  | 가격 anchor                                                                | outcome                       |
| ------- | ---------------------------- | ---------: | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ----------------------------- |
| T0      | meme event                   | 2025-10-31 | Nvidia CEO Jensen Huang dines at Kkanbu Chicken with Samsung/Hyundai executives | Kyochon/Cherrybro/Neuromeka surge                                        | meme                          |
| T1      | price_moved_without_evidence | 2025-10-31 | Kkanbu Chicken not listed; Kyochon peer only                                    | Kyochon up as much as 20%, Cherrybro up to 30%, Neuromeka retained gains | price without direct evidence |
| T2      | 4B-watch                     | 2025-10-31 | Nvidia chip deals in Korea but no chicken equity purchase                       | no direct revenue                                                        | 4B                            |
| T3      | Stage3                       |        N/A | same-store sales/franchise fee not confirmed                                    | N/A                                                                      | no Stage3                     |
| T4      | 4C                           |        N/A | 없음                                                                              | N/A                                                                      | no 4C                         |

Kyochon/Cherrybro/Neuromeka는 R5의 가장 명확한 `price_moved_without_evidence`다. MarketWatch는 Jensen Huang이 Samsung/Hyundai executives와 Kkanbu Chicken에서 식사한 뒤 Kyochon F&B, Cherrybro, Neuromeka shares가 급등했다고 보도했고, Kkanbu는 상장사가 아니며 Nvidia가 한국에 260,000 AI chips를 판매하는 deal은 있었지만 chicken stocks에 지분투자는 없었다고 설명했다. ([마켓워치][11])

Tom’s Hardware/Bloomberg 기반 보도는 Kyochon이 최대 20%, Cherrybro가 daily limit인 30%까지 올랐다고 설명했다. 이 trigger는 브랜드 소비가 아니라 **유명인 meme liquidity**다. ([Tom's Hardware][12])

### Trigger price validation row

```json
{
  "case_id": "r5_loop15_kyochon_cherrybro_jensen_meme",
  "symbols": "339770/066360/348340",
  "best_trigger": "T1",
  "best_trigger_type": "price_moved_without_evidence",
  "trigger_date": "2025-10-31",
  "kyochon_event_mfe_pct": 20,
  "cherrybro_event_mfe_pct": 30,
  "neuromeka_retained_gains_by_close": true,
  "kkanbu_listed": false,
  "nvidia_korea_ai_chip_deals_units": 260000,
  "direct_revenue_link_confirmed": false,
  "same_store_sales_confirmed": false,
  "franchise_fee_confirmed": false,
  "full_mfe_mae_status": "N/A_no_valid_stage3",
  "trigger_outcome_label": "price_moved_without_evidence"
}
```

### 판정

```text
score_price_alignment = price_moved_without_evidence
reason = 유명인/AI 방문 event는 direct same-store sales나 franchise economics 전에는 Stage3 금지
```

---

# 6. Trigger별 가격경로 검증 요약

| case                   | best trigger     |       entry anchor |                                         event MFE/MAE | market-relative | full MFE/MAE | outcome                           |
| ---------------------- | ---------------- | -----------------: | ----------------------------------------------------: | --------------: | ------------ | --------------------------------- |
| Samyang Buldak         | T1/T2 2024-06-14 |            647,000 |                                                 +5.7% |     unavailable | unavailable  | Stage3-Yellow / missed_structural |
| Nongshim               | T1/T2 2024-05-27 |        unavailable |                                                   N/A |             N/A | unavailable  | Stage2 success candidate          |
| K-beauty basket        | T2/T3 2025-06-05 |        unavailable |                                                   N/A |             N/A | unavailable  | Stage2-Actionable candidate       |
| APR / Medicube         | T1/T2 2025       | stock 4x since Jan |                                          +300% anchor |             N/A | unavailable  | Stage3-Yellow + 4B                |
| Chinese tourist basket | T1/T2 2025-08/09 |              event | Hyundai Dept +7.1%, Hotel Shilla +4.8%, Hankook +9.9% |     unavailable | unavailable  | Stage2-Actionable                 |
| E-Mart / Shinsegae JV  | T1/T2            |        unavailable |                                                   N/A |             N/A | unavailable  | Stage2 + data regulatory overlay  |
| F&F / TaylorMade       | T1/T2            |        unavailable |                                                   N/A |             N/A | unavailable  | Stage2 brand M&A                  |
| Kyochon meme           | T1               |              event |                          Kyochon +20%, Cherrybro +30% |             N/A | N/A          | price_moved_without_evidence      |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
Nongshim:
글로벌 매출·U.S. target은 강하지만 OP estimate / event price가 없어 Stage2 유지.

E-Mart / Shinsegae:
JV와 conditional approval은 Stage2지만 data-sharing restriction 때문에 Green 금지.

F&F:
TaylorMade control optionality는 Stage2지만 funding/control/ROIC 확인 전 Yellow 보류.
```

## Stage 2-Actionable entry 성과

```text
Samyang:
OP estimate +84%, ASP 상승, U.S./Europe shipment 증가, capacity 증설, +5.7%.
Stage2-Actionable을 넘어 Stage3-Yellow.

K-beauty basket:
U.S. ecommerce +71%, Korea top U.S. cosmetics exporter, physical retail entry 논의.
Stage2-Actionable.

Chinese tourist basket:
visa-free policy + department/hotel/casino/beauty basket rally.
Stage2-Actionable.
```

## Stage 3-Yellow entry 성과

```text
Samyang:
Buldak export trigger는 Yellow로 봐야 한다.
Regulatory recall은 4C-watch였지만 ban reversal로 false-break에 가까움.

APR:
stock 4x + overseas revenue nearly 80% + device category.
Yellow 가능하지만 valuation 4B overlay.
```

## Stage3-Green

```text
이번 R5 Loop 15에서 확정 Green은 없음.

이유:
- Samyang은 강하지만 full OHLC와 actual quarterly result / repeat export margin 확인 필요.
- K-beauty는 physical-store sell-through 필요.
- APR은 valuation 4B와 tariff/competition risk가 큼.
- Chinese tourism은 실제 spending / duty-free sales 필요.
```

## 기존 점수표가 놓쳤을 가능성

```text
missed_structural:
- Samyang Foods / Buldak
- K-beauty basket 일부
- APR, 단 4B overlay

Stage2_promote_candidate:
- Samyang
- K-beauty basket
- Chinese tourist retail basket

price_moved_without_evidence:
- Kyochon / Cherrybro / Neuromeka
```

---

# 8. score-price alignment 판정

```text
Stage2_promote_candidate:
- Samyang Foods
- K-beauty basket
- Chinese tourist retail basket

Stage3-Yellow candidate:
- Samyang Foods
- APR / Medicube, with 4B overlay

Stage3-Green:
- 없음

event_premium:
- Chinese tourist visa-free first reaction
- Lotte Tour tourism reroute
- APR social-media/beauty-device valuation spike if not tied to sell-through

price_moved_without_evidence:
- Kyochon / Cherrybro / Neuromeka Jensen chicken rally

evidence_good_but_price_failed:
- E-Mart / Shinsegae JV if data restriction prevents monetization
- F&F / TaylorMade if acquisition funding/control fails

false_positive_score:
- Kyochon meme if treated as brand Stage3
- APR if treated as Green after 4x rally without channel/margin confirmation

thesis_break_watch:
- Samyang regulatory/spiciness recall
- Chinese tourism anti-foreigner protest / diplomatic risk
- K-beauty tariffs / saturation / physical-store failure
- E-commerce data regulation
```

---

# 9. 점수비중 교정

## 올릴 축

```text
export_shipment_growth +5
ASP_increase +5
OP_estimate_revision +5
production_capacity_expansion +4
US_Europe_sellthrough +5
physical_retail_channel_entry +4
repeat_purchase_or_same_store_sales +5
tourist_arrival_spending_conversion +5
customer_data_monetization_permission +4
brand_MA_control_execution +4
```

### 근거

Samyang은 ASP·shipment·capacity·OP estimate가 동시에 붙으면서 Stage2를 Yellow로 승격해야 했다. K-beauty는 U.S. ecommerce sell-through와 physical-store entry 논의가 plain Stage2보다 강하다. Chinese tourism basket은 policy trigger가 다수 소비주 동반 상승으로 연결됐지만 실제 spending conversion이 필요하다.

## 내릴 축

```text
viral_celebrity_event_only -5
brand_name_only -4
tourism_policy_without_spending -4
JV_without_data_rights -4
M&A_option_without_funding_control -4
target_market_size_only -4
social_media_hype_without_repeat_purchase -5
```

### 근거

Kyochon은 Jensen meme만으로 움직였고 direct revenue가 없었다. E-Mart/Alibaba JV는 data-sharing restriction 때문에 monetization gate가 남았다. F&F는 TaylorMade optionality는 있지만 funding/control/ROIC 전에는 Stage2다. APR은 social-media virality가 실제 overseas revenue와 연결됐기 때문에 Yellow 가능하지만, 4x rally 후에는 4B overlay가 필요하다.

---

# 10. Stage 2-Actionable 승격 조건

R5 Loop 15 shadow rule:

```text
R5에서 Stage 2 evidence가 아래 중 3개 이상이면 Stage2-Actionable로 승격한다.

1. ASP 상승 또는 가격전가가 확인된다.
2. shipment / export / ecommerce sell-through가 지역별로 확인된다.
3. OP estimate 또는 target price가 실적 근거와 함께 상향된다.
4. 생산능력 또는 유통채널 확대가 확인된다.
5. trigger 당일 또는 이벤트 직후 market-relative 가격 반응이 강하다.
6. SNS/바이럴이 실제 매출/해외 revenue mix와 연결된다.
7. 관광/면세는 policy가 아니라 실제 입국자·결제액·점포 매출로 이어질 가능성이 보인다.
```

적용:

```text
Samyang:
ASP + shipment + capacity + OP estimate + price reaction.

K-beauty:
U.S. ecommerce sell-through + export rank + physical retail channel.

Chinese tourism:
visa-free policy + department/hotel/casino/beauty basket rally.
```

---

# 11. Stage 3-Yellow 조건

```text
Stage3-Yellow:
- 소비재 브랜드의 EPS/OP 경로가 바뀔 수 있는 숫자가 2~3개 이상 닫힘
- 하지만 repeat purchase, offline channel, regulatory risk, margin sustainability 중 하나가 남아 있음
```

후보:

```text
Samyang:
OP estimate +84%, ASP 상승, U.S./Europe shipment, capacity expansion.
남은 gate: actual quarterly result, repeat demand, regulatory risk.

APR:
overseas revenue nearly 80%, device category, stock 4x.
남은 gate: valuation, repeat purchase, tariff, channel sustainability.
```

---

# 12. Stage 3-Green 조건

```text
Stage3-Green:
- 해외 매출/출하가 실제 분기 실적으로 확인됨
- ASP와 volume이 동시에 유지됨
- 생산능력 확대가 매출/마진으로 연결됨
- 오프라인 입점 후 sell-through와 repeat purchase가 확인됨
- 관광/면세는 실제 객단가와 점포 매출이 확인됨
- full-window MFE/MAE가 우호적
```

이번 R5 Loop 15에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- SNS/influencer trigger로 주가가 단기간 20~30% 급등하지만 직접 매출 evidence 없음
- 주가가 3~4배 오른 뒤 channel/margin 확인 없이 valuation이 먼저 뜀
- 관광정책으로 소비주가 급등하지만 실제 spending data 없음
- JV/M&A headline이 있지만 data rights/funding/control이 미확정
- regulatory recall / food safety / social backlash 가능성이 발생
```

적용:

```text
APR:
4x 이후 4B valuation overlay.

Kyochon/Cherrybro:
celebrity meme 4B / price_moved_without_evidence.

Chinese tourist basket:
visa policy는 Stage2지만 anti-foreigner protest / diplomatic risk가 4B/4C overlay.

Samyang:
Denmark recall은 4C-watch였지만 false-break relief.
```

---

# 14. 4C hard gate 조건

```text
R5 4C:
- food safety / recall이 품질 문제로 확인됨
- major market ban이 지속됨
- influencer/meme rally 이후 direct revenue가 전혀 확인되지 않고 주가가 붕괴
- tourism policy reversal / diplomatic conflict로 visitor flow가 끊김
- e-commerce JV가 data regulation으로 monetization 실패
- brand M&A funding/control failure
```

이번 R5 Loop 15에서 hard 4C 확정은 없다.

```text
hard_4c_not_confirmed = true
```

Strong 4C-watch:

```text
- Samyang Denmark recall, but partially reversed → false-break watch
- Chinese tourism anti-foreigner protest / diplomatic risk
- E-Mart / Alibaba data-sharing restriction
- K-beauty tariff / physical-store sell-through failure
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_228.md 요약

```md
# R5 Loop 15. Consumer / Retail / Brand Trigger-level Price Validation

이번 라운드는 R5 Loop 15 trigger-level validation 라운드다.

핵심 결론:
- Samyang Foods / Buldak is the key Stage2-promote / Stage3-Yellow candidate. On 2024-06-14, Kiwoom raised 2Q OP estimate to 81.2B won, +84% YoY, citing Buldak ASP increase, U.S./Europe shipment growth and capacity expansion. Shares closed +5.7% at 647,000 won; target was raised 26% to 830,000 won. Plain Stage2 would be too conservative.
- Samyang Denmark recall was regulatory 4C-watch but not hard 4C. Denmark recalled three variants over capsaicin risk, but later reversed the ban for two variants.
- Nongshim / Shin Ramyun is Stage2 success candidate. 2023 Shin Ramyun sales were 1.2T won / $883M, nearly 60% abroad; U.S. sales target is $1.5B by 2030. No event-price / OP-estimate anchor, so Yellow is not confirmed.
- K-beauty basket is Stage2-Actionable. Korea replaced France as top U.S. cosmetics exporter in 2024; top-five Korean U.S. ecommerce brands grew 71% over two years vs overall U.S. market 21%. Physical-store sell-through and tariff/margin gates remain.
- APR / Medicube is Stage3-Yellow with 4B overlay. APR stock rose more than fourfold since January, valuation near $6B, overseas revenue nearly 80% of Q2, beauty device one-third of U.S. sales. But valuation/tariff/competition risk requires 4B overlay.
- Chinese tourist visa-free basket is Stage2-Actionable. Hyundai Department Store +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9% after China tourist group visa-free policy. Green needs arrivals, card spending, duty-free sales, hotel ADR and beauty sell-through.
- E-Mart / Shinsegae / Alibaba-Gmarket JV is Stage2 with regulatory overlay. JV value around $4B, KFTC conditional approval, Gmarket 50M customer database, but data-sharing barred for 3 years and cross-border market share 41% creates regulatory gate.
- F&F / TaylorMade is Stage2 brand M&A optionality. TaylorMade sale may fetch $3.5B; F&F invested 358B won and claims consent rights/ROFR. Green needs funding, control execution and ROIC.
- Kyochon / Cherrybro / Neuromeka Jensen chicken rally is price_moved_without_evidence. Kkanbu Chicken was not listed; Kyochon and Cherrybro moved on celebrity/AI meme without direct revenue link.

Main calibration:
- Raise export shipment growth, ASP increase, OP estimate revision, production capacity expansion, U.S./Europe sell-through, physical retail channel entry, repeat purchase / same-store sales, tourist arrival-to-spending conversion, customer-data monetization permission, brand M&A control execution.
- Lower viral celebrity event-only, brand name-only, tourism policy without spending, JV without data rights, M&A option without funding/control, target market size-only, social-media hype without repeat purchase.
```

## docs/checkpoints/checkpoint_28a_round228_r5_loop15.md 요약

```md
# Checkpoint 28A Round 228 R5 Loop 15 Trigger-level Calibration

## 반영 내용
- R5 Loop 15 trigger-level validation을 수행했다.
- Samyang Foods, Nongshim, K-beauty basket, APR/Medicube, Chinese tourism/duty-free basket, E-Mart/Shinsegae/Alibaba JV, F&F/TaylorMade, Kyochon/Cherrybro/Neuromeka를 검토했다.
- full adjusted OHLC window는 확보하지 못했으므로 Reuters / FT / WSJ / MarketWatch / AP의 reported event return과 event price anchor를 사용했다.
- OHLC 미확보를 이유로 Stage 후보를 강등하지 않고, price_data_unavailable_after_deep_search로 분리 기록했다.

## 핵심 보정
- 소비재 Stage2가 ASP, shipment, capacity, OP estimate, relative price reaction을 동시에 갖추면 Stage3-Yellow로 승격한다.
- SNS/celebrity meme은 direct same-store sales / franchise fee / repeat purchase 전에는 Stage3 금지.
- 관광정책은 실제 arrival, spending, duty-free sales로 전환되어야 Green.
- e-commerce JV는 data-sharing rights와 regulatory approval condition을 따로 scoring한다.
```

## data/e2r_case_library/cases_r5_loop15_round228.jsonl 초안

```jsonl
{"case_id":"r5_loop15_samyang_buldak_export","symbol":"003230","company_name":"Samyang Foods","case_type":"Stage2_promote_candidate","primary_archetype":"K_FOOD_EXPORT_STAGE2_TO_STAGE3_YELLOW","best_trigger":"T1/T2","stage_candidate":"Stage3-Yellow","price_validation":{"entry_price_anchor_krw":647000,"event_return_pct":5.7,"q2_2024_op_estimate_krw_bn":81.2,"q2_2024_op_estimate_yoy_pct":84,"target_price_krw":830000,"target_price_raise_pct":26,"target_upside_from_entry_pct":28.3,"evidence_factors":["Buldak ASP increase","U.S. shipment growth","Europe shipment growth","production capacity expansion"],"denmark_recall_variants":3,"ban_partially_reversed_date":"2024-08-08","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"missed_structural_if_old_gate_used","notes":"ASP + shipment + capacity + OP estimate beat should promote Stage2 to Stage3-Yellow."}
{"case_id":"r5_loop15_nongshim_shinramyun_global","symbol":"004370","company_name":"Nongshim","case_type":"success_candidate_stage2","primary_archetype":"RAMEN_GLOBAL_EXPANSION_STAGE2","best_trigger":"T1/T2","stage_candidate":"Stage2","price_validation":{"korean_ramen_exports_2023_usd_bn":1.0,"shin_ramyun_2023_sales_krw_trn":1.2,"shin_ramyun_2023_sales_usd_mn":883,"overseas_sales_share_pct":60,"us_sales_target_2030_usd_bn":1.5,"stage3_gate_missing":["OP estimate revision","ASP increase","shipment data by region","production capacity","event price anchor"],"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_stage2","notes":"Global sales and U.S. target are strong but no event-price / OP-estimate trigger found."}
{"case_id":"r5_loop15_kbeauty_us_export_basket","symbol":"257720/192820/161890/090430/beauty_basket","company_name":"Silicon2 / Cosmax / Kolmar Korea / Amorepacific / K-beauty basket","case_type":"Stage2_promote_candidate","primary_archetype":"K_BEAUTY_US_EXPORT_STAGE2_ACTIONABLE","best_trigger":"T2/T3","stage_candidate":"Stage2-Actionable_to_Stage3-Yellow_candidate","price_validation":{"korea_replaced_france_as_top_us_cosmetics_exporter":true,"top5_korean_us_ecommerce_sales_growth_2y_pct":71,"overall_us_market_growth_2y_pct":21,"top5_french_brands_growth_2y_pct":15,"retail_channels_under_discussion":["Ulta Beauty","Sephora","Target","Costco"],"odm_beneficiaries":["Cosmax","Kolmar Korea"],"stage3_gate_missing":["physical_store_sell_through","brand_repeat_purchase","ODM margin","tariff pass-through","inventory"],"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate","notes":"U.S. ecommerce sell-through + export rank + physical-channel trigger is stronger than plain Stage2."}
{"case_id":"r5_loop15_apr_medicube_beauty_device","symbol":"APR/beauty_device_basket","company_name":"APR / Medicube","case_type":"Stage3_Yellow_with_4B_overlay","primary_archetype":"BEAUTY_DEVICE_VIRAL_STAGE3_WITH_4B","best_trigger":"T1/T2","stage_candidate":"Stage3-Yellow + 4B-watch","price_validation":{"stock_return_since_january_pct":300,"valuation_usd_bn":6,"overseas_revenue_share_q2_2025_pct":80,"beauty_device_share_of_us_sales_pct":33,"product_price_usd":180,"viral_trigger":"Kylie Jenner TikTok / Medicube device","stage3_gate_missing":["sustained_repeat_purchase","retail_channel_expansion","device_margin","tariff_absorption","competition_response"],"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage3-Yellow_candidate_with_4B","notes":"Viral device demand links to overseas revenue, but fourfold rally requires valuation overlay."}
{"case_id":"r5_loop15_china_tourist_visa_free_retail_basket","symbol":"008770/069960/123690/034230/032350","company_name":"Hotel Shilla / Hyundai Department Store / Hankook Cosmetics / Paradise / Lotte Tour Development","case_type":"Stage2_promote_candidate","primary_archetype":"CHINA_TOURIST_DUTYFREE_STAGE2_ACTIONABLE","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable","price_validation":{"visa_free_period":"2025-09-29_to_2026-06","hyundai_department_store_event_return_pct":7.1,"hotel_shilla_event_return_pct":4.8,"paradise_event_return_pct":2.9,"hankook_cosmetics_event_return_pct":9.9,"group_size_min":3,"visa_free_stay_days":15,"china_share_of_2024_korea_visitors_pct":28,"korea_2024_visitors_mn":16.4,"lotte_tour_event_return_pct":9.6,"stage3_gate_missing":["actual_arrivals","foreign_card_spending","duty_free_sales","hotel_ADR","casino_drop","beauty_store_sellthrough"],"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate","notes":"Visa-free policy plus multi-consumer-stock rally is Stage2-Actionable, but Green needs spending conversion."}
{"case_id":"r5_loop15_emart_shinsegae_alibaba_gmarket_jv","symbol":"139480/004170","company_name":"E-Mart / Shinsegae / Gmarket / AliExpress Korea","case_type":"success_candidate_stage2_with_regulatory_overlay","primary_archetype":"ECOMMERCE_JV_STAGE2_WITH_DATA_REGULATORY_4B","best_trigger":"T1/T2","stage_candidate":"Stage2","price_validation":{"jv_estimated_value_usd_bn":4,"assets_combined":["Gmarket","AliExpress Korea"],"kftc_conditional_approval":true,"gmarket_customer_database_mn":50,"data_sharing_restriction_years":3,"cross_border_ecommerce_market_share_pct":41,"china_import_online_spending_2024_krw_trn":4.7,"alibaba_share_of_china_online_import_sales_pct":62,"direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_stage2","notes":"JV/conditional approval is Stage2; data-sharing restriction and GMV/take-rate gate block Green."}
{"case_id":"r5_loop15_fnf_taylormade_brand_ma","symbol":"383220","company_name":"F&F / TaylorMade","case_type":"success_candidate_stage2","primary_archetype":"BRAND_MA_CONTROL_RIGHTS_STAGE2","best_trigger":"T1/T2","stage_candidate":"Stage2_brand_MA_optional","price_validation":{"fnf_2021_investment_krw_bn":358,"taylormade_possible_sale_value_usd_bn":3.5,"advisor":"Goldman Sachs","claimed_rights":["Consent Rights","ROFR"],"dispute_party":"Centroid Investment Partners","direct_price_anchor":"price_data_unavailable_after_deep_search","stage3_gate_missing":["acquisition_price","funding","control execution","brand integration","ROIC","legal resolution"]},"score_price_alignment":"success_candidate_stage2","notes":"Global brand optionality is Stage2; funding/control/ROIC required for Yellow or Green."}
{"case_id":"r5_loop15_kyochon_cherrybro_jensen_meme","symbol":"339770/066360/348340","company_name":"Kyochon F&B / Cherrybro / Neuromeka","case_type":"price_moved_without_evidence","primary_archetype":"FRIED_CHICKEN_MEME_PRICE_MOVED_WITHOUT_EVIDENCE","best_trigger":"T1","stage_candidate":"N/A_no_valid_stage3","price_validation":{"kyochon_event_mfe_pct":20,"cherrybro_event_mfe_pct":30,"neuromeka_retained_gains_by_close":true,"kkanbu_listed":false,"nvidia_korea_ai_chip_deals_units":260000,"direct_revenue_link_confirmed":false,"same_store_sales_confirmed":false,"franchise_fee_confirmed":false,"full_ohlc_status":"N/A_no_valid_stage3"},"score_price_alignment":"price_moved_without_evidence","notes":"Celebrity/AI visit at non-listed Kkanbu moved peer stocks without direct sales evidence."}
```

## data/e2r_trigger_calibration/triggers_r5_loop15_round228.jsonl 초안

```jsonl
{"trigger_id":"r5l15_samyang_T1","case_id":"r5_loop15_samyang_buldak_export","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-14","evidence_available":"Kiwoom raises 2Q OP estimate to 81.2B won, +84% YoY, driven by ASP increase, U.S./Europe shipments and capacity expansion","entry_price_krw":647000,"event_return_pct":5.7,"target_price_krw":830000,"trigger_outcome_label":"excellent_stage2_promote_candidate","promote_to":"Stage3-Yellow"}
{"trigger_id":"r5l15_samyang_T3","case_id":"r5_loop15_samyang_buldak_export","trigger_type":"4C-watch","trigger_date":"2024-06-12","evidence_available":"Denmark recalls three Buldak variants due capsaicin/spiciness risk","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"regulatory_false_break_watch","promote_to":"4C-watch_false_break"}
{"trigger_id":"r5l15_nongshim_T1","case_id":"r5_loop15_nongshim_shinramyun_global","trigger_type":"Stage2","trigger_date":"2024-05-27","evidence_available":"Shin Ramyun 2023 sales 1.2T won / $883M, nearly 60% abroad, U.S. sales target $1.5B by 2030","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"success_candidate_stage2","promote_to":"Stage2"}
{"trigger_id":"r5l15_kbeauty_T2","case_id":"r5_loop15_kbeauty_us_export_basket","trigger_type":"Stage2-Actionable","trigger_date":"2025-06-05","evidence_available":"Korea top U.S. cosmetics exporter, top-five Korean U.S. ecommerce brands +71% over two years vs U.S. market +21%, physical retail talks","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_promote_candidate","promote_to":"Stage2-Actionable"}
{"trigger_id":"r5l15_apr_T2","case_id":"r5_loop15_apr_medicube_beauty_device","trigger_type":"Stage3-Yellow+4B-watch","trigger_date":"2025-10-20","evidence_available":"APR stock more than fourfold since January, valuation $6B, overseas revenue nearly 80% of Q2, beauty device about one-third of U.S. sales","event_return_pct":300,"trigger_outcome_label":"Stage3_Yellow_with_4B_overlay","promote_to":"Stage3-Yellow+4B"}
{"trigger_id":"r5l15_china_tourism_T1","case_id":"r5_loop15_china_tourist_visa_free_retail_basket","trigger_type":"Stage2-Actionable","trigger_date":"2025-08-06","evidence_available":"Chinese group visa-free policy confirmed; Hyundai Department +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9%","event_return_pct":"7.1/4.8/2.9/9.9","trigger_outcome_label":"Stage2_promote_candidate","promote_to":"Stage2-Actionable"}
{"trigger_id":"r5l15_emart_jv_T2","case_id":"r5_loop15_emart_shinsegae_alibaba_gmarket_jv","trigger_type":"Stage2_with_regulatory_overlay","trigger_date":"2025-09-18","evidence_available":"KFTC conditionally approves Gmarket/AliExpress JV; 50M customer database; 3-year data-sharing restriction; cross-border share 41%","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"success_candidate_stage2_with_data_gate","promote_to":"Stage2"}
{"trigger_id":"r5l15_fnf_T1","case_id":"r5_loop15_fnf_taylormade_brand_ma","trigger_type":"Stage2_brand_MA","trigger_date":"2025-07-21","evidence_available":"F&F hires Goldman for TaylorMade acquisition; potential $3.5B sale; F&F has 358B won prior investment and claims consent rights/ROFR","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"success_candidate_stage2","promote_to":"Stage2"}
{"trigger_id":"r5l15_kyochon_T1","case_id":"r5_loop15_kyochon_cherrybro_jensen_meme","trigger_type":"price_moved_without_evidence","trigger_date":"2025-10-31","evidence_available":"Jensen Huang dined at non-listed Kkanbu Chicken; Kyochon/Cherrybro/Neuromeka surged without direct revenue link","event_return_pct":"Kyochon up to 20 / Cherrybro up to 30","trigger_outcome_label":"price_moved_without_evidence","promote_to":"N/A"}
```

## data/sector_taxonomy/score_weight_profiles_round228_r5_loop15_v1.csv 초안

```csv
archetype,export_shipment_growth,asp_increase,op_estimate_revision,production_capacity_expansion,us_europe_sellthrough,physical_retail_channel_entry,repeat_purchase_same_store_sales,tourist_arrival_spending_conversion,customer_data_monetization_permission,brand_ma_control_execution,viral_celebrity_event_only_penalty,brand_name_only_penalty,tourism_policy_without_spending_penalty,jv_without_data_rights_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
K_FOOD_EXPORT_STAGE2_TO_STAGE3_YELLOW,+5,+5,+5,+4,+5,+1,+4,+0,+0,+0,-4,-3,-1,-1,ASP+shipment+capacity+OP revision,actual result/repeat demand pending,export margin+capacity+repeat demand,Samyang Buldak trigger should promote to Yellow.
K_FOOD_REGULATORY_FALSE_BREAK_4C_WATCH,+2,+2,+2,+1,+2,+0,+2,+0,+0,+0,-2,-2,-1,-1,recall/watch,quality defect or market ban pending,ban reversal or no sales impact,Denmark Buldak recall was watch not hard 4C.
RAMEN_GLOBAL_EXPANSION_STAGE2,+4,+2,+2,+3,+5,+2,+4,+0,+0,+0,-3,-2,-1,-1,global sales+U.S. target,OP/price trigger missing,ASP/OP/export margin confirmed,Nongshim remains Stage2 without price/OP trigger.
K_BEAUTY_US_EXPORT_STAGE2_ACTIONABLE,+4,+3,+3,+2,+5,+5,+5,+2,+0,+0,-4,-3,-1,-1,U.S. ecommerce sell-through+physical retail talks,store sell-through/tariff pending,repeat purchase+margin+offline channel,K-beauty basket Stage2-Actionable.
BEAUTY_DEVICE_VIRAL_STAGE3_WITH_4B,+4,+3,+4,+2,+5,+4,+5,+1,+0,+0,-2,-2,-1,-1,viral device demand+overseas revenue,valuation/tariff/channel pending,sustained repeat purchase+margin,APR Yellow with 4B overlay.
CHINA_TOURIST_DUTYFREE_STAGE2_ACTIONABLE,+0,+0,+1,+0,+2,+2,+3,+5,+0,+0,-2,-2,-5,-1,visa policy+multi-stock rally,arrival/spending conversion pending,duty-free sales+hotel ADR+beauty sellthrough,Chinese tourism basket Stage2-Actionable.
ECOMMERCE_JV_STAGE2_WITH_DATA_REGULATORY_4B,+0,+0,+1,+0,+0,+0,+2,+0,+5,+3,-2,-2,-1,-5,JV+conditional approval,GMV/take-rate/data rights pending,customer data monetization+margin,E-Mart/Alibaba JV Stage2 with data gate.
BRAND_MA_CONTROL_RIGHTS_STAGE2,+0,+0,+1,+0,+1,+1,+3,+0,+0,+5,-2,-4,-1,-2,brand M&A optionality,funding/control/ROIC pending,control execution+ROIC,F&F TaylorMade Stage2.
FRIED_CHICKEN_MEME_PRICE_MOVED_WITHOUT_EVIDENCE,+0,+0,+0,+0,+0,+0,+0,+0,+0,+0,-5,-5,-1,-1,no direct revenue,same-store/franchise fee missing,N/A,Kyochon/Jensen meme is price moved without evidence.
```

---

# 이번 R5 Loop 15 결론

```text
1. Samyang/Buldak은 R5의 핵심 missed_structural 후보다.
   ASP·shipment·capacity·OP estimate가 동시에 나왔으니 Stage2가 아니라 Stage3-Yellow로 봐야 한다.

2. Samyang Denmark recall은 4C-watch였지만 hard 4C는 아니다.
   품질 문제가 아니라 spiciness/regulatory issue였고 일부 ban이 뒤집혔다.

3. Nongshim은 Stage2 success candidate다.
   글로벌 매출과 U.S. target은 강하지만 OP estimate / event price trigger가 없어 Yellow 보류.

4. K-beauty basket은 Stage2-Actionable이다.
   U.S. ecommerce sell-through와 physical retail channel trigger가 붙었다.

5. APR/Medicube는 Stage3-Yellow + 4B다.
   해외 매출과 beauty-device category가 실제로 붙었지만 주가 4배 이후 valuation overlay가 필요하다.

6. Chinese tourism/duty-free basket은 Stage2-Actionable이다.
   비자정책과 소비주 동반 상승이 있었지만 실제 입국·결제·점포매출 전에는 Green이 아니다.

7. E-Mart/Shinsegae/Alibaba JV는 Stage2 with data-regulatory overlay다.
   고객 데이터와 take-rate monetization 전에는 Green이 아니다.

8. F&F/TaylorMade는 brand M&A Stage2다.
   control rights optionality는 있지만 funding/control/ROIC가 남아 있다.

9. Kyochon/Cherrybro/Neuromeka는 price_moved_without_evidence다.
   Jensen Huang meme은 direct same-store sales나 franchise fee가 아니었다.
```

한 문장으로 압축하면:

> **R5 Loop 15에서 배운 핵심은 “브랜드가 유명하다”가 아니라, ASP·shipment·capacity·OP estimate·ecommerce sell-through·physical channel·tourist spending conversion이 닫혀야 Stage3로 올릴 수 있다는 것이다. 반대로 celebrity meme, policy headline, JV headline, M&A optionality만으로는 Green 금지다.**

[1]: https://www.marketwatch.com/story/samyang-foods-set-to-post-strong-2q-earnings-market-talk-d654e045 "https://www.marketwatch.com/story/samyang-foods-set-to-post-strong-2q-earnings-market-talk-d654e045"
[2]: https://apnews.com/article/f622b2d901990a08d180eee3ce2260f2 "https://apnews.com/article/f622b2d901990a08d180eee3ce2260f2"
[3]: https://www.ft.com/content/4218f2b8-5498-411b-81fe-e3c836868d64 "https://www.ft.com/content/4218f2b8-5498-411b-81fe-e3c836868d64"
[4]: https://www.reuters.com/world/asia-pacific/korean-beauty-startups-bet-booming-us-demand-outlasts-tariff-pain-2025-06-05/ "https://www.reuters.com/world/asia-pacific/korean-beauty-startups-bet-booming-us-demand-outlasts-tariff-pain-2025-06-05/"
[5]: https://www.ft.com/content/6a0f7e2c-f3b9-4eb6-961c-d69af28f7183 "https://www.ft.com/content/6a0f7e2c-f3b9-4eb6-961c-d69af28f7183"
[6]: https://www.reuters.com/world/china/south-korea-offer-visa-free-entry-chinese-tourists-late-september-2025-08-06/ "https://www.reuters.com/world/china/south-korea-offer-visa-free-entry-chinese-tourists-late-september-2025-08-06/"
[7]: https://www.reuters.com/world/china/south-korea-pilot-visa-free-entry-chinese-tourist-groups-cctv-reports-2025-09-29/ "https://www.reuters.com/world/china/south-korea-pilot-visa-free-entry-chinese-tourist-groups-cctv-reports-2025-09-29/"
[8]: https://www.reuters.com/markets/deals/south-koreas-shinsegae-set-up-joint-venture-with-alibaba-international-2024-12-26/ "https://www.reuters.com/markets/deals/south-koreas-shinsegae-set-up-joint-venture-with-alibaba-international-2024-12-26/"
[9]: https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-conditionally-approves-aliexpress-shinsegae-unit-joint-venture-2025-09-18/ "https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-conditionally-approves-aliexpress-shinsegae-unit-joint-venture-2025-09-18/"
[10]: https://www.reuters.com/world/asia-pacific/s-korean-fashion-retailer-ff-hires-goldman-taylormade-acquisition-2025-07-21/ "https://www.reuters.com/world/asia-pacific/s-korean-fashion-retailer-ff-hires-goldman-taylormade-acquisition-2025-07-21/"
[11]: https://www.marketwatch.com/story/jensen-huang-spreads-nvidia-magic-to-fried-chicken-stocks-06b49648 "https://www.marketwatch.com/story/jensen-huang-spreads-nvidia-magic-to-fried-chicken-stocks-06b49648"
[12]: https://www.tomshardware.com/tech-industry/korean-fried-chicken-stocks-surge-30-percent-as-nvidia-ceo-jensen-huang-dines-out-on-local-delicacy-entire-industry-buoyed-by-secret-ingredient-jensanity "https://www.tomshardware.com/tech-industry/korean-fried-chicken-stocks-surge-30-percent-as-nvidia-ceo-jensen-huang-dines-out-on-local-delicacy-entire-industry-buoyed-by-secret-ingredient-jensanity"

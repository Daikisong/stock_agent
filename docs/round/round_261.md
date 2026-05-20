순서상 이번은 **R5 Loop 12 — 소비재·유통·브랜드 가격경로 검증 라운드**다.

```text
round = R5 Loop 12
round_id = round_189
large_sector = CONSUMER_RETAIL_BRAND
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true_for_retail_distress_reference
direct_krx_hard_4c_confirmed = false
```

이번 R5 Loop 12는 지난 R5의 Samyang/APR/이커머스 대표축을 일부 benchmark로만 남기고, **K-food export, H&B retail platform, K-beauty brand M&A, indie K-beauty physical-store test, e-commerce JV data gate, offline grocery distress, global confectionery localization, celebrity food-service overheat**를 중심으로 본다.

---

# 1. 이번 라운드 대섹터

```text
R5 = 소비재·유통·브랜드
```

R5에서 Stage 3는 “K-food”, “K-beauty”, “브랜드력”, “해외 진출”, “관광객”, “제휴”, “유명인 이벤트”가 아니다.

진짜 Stage 3는 **반복구매, 해외 sell-through, physical-store sell-through, ASP, OPM, 재고·채권 품질, 채널 유지율, 가격전가, 실제 FCF**가 확인되는 순간이다.

---

# 2. 대상 canonical archetype

```text
K_FOOD_EXPORT_ASP_CAPACITY
H_AND_B_RETAIL_GLOBAL_PLATFORM
K_BEAUTY_BRAND_M_AND_A_VALIDATION
K_BEAUTY_INDIE_PHYSICAL_STORE_TEST
ECOMMERCE_JV_SCALE_DATA_GATE
OFFLINE_GROCERY_DISTRESS_4C
GLOBAL_CONFECTIONERY_LOCALIZATION
FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM
```

---

# 3. deep sub-archetype

```text
K-food:
- Samyang Buldak export
- ASP 상승
- U.S. / Europe shipment
- capacity expansion
- single-SKU concentration / input-cost watch

H&B retail:
- CJ Olive Young
- K-beauty curation platform
- global online platform / U.S. store
- offline traffic vs paid conversion
- listed exposure: CJ Corp indirect

K-beauty M&A:
- Dr.G / Gowoonsesang
- L'Oreal acquisition
- brand validation vs listed-stock revenue bridge
- ODM / distribution read-through

Indie K-beauty:
- d'Alba / Tirtir / Torriden / Beauty of Joseon / Anua
- Ulta / Sephora / Target / Costco talks
- Cosmax / Kolmar / Silicon2 leverage
- physical-store sell-through gate

E-commerce:
- E-Mart / Shinsegae / Alibaba
- Gmarket + AliExpress Korea
- customer-data restriction
- cross-border market share
- product-safety and platform-trust gate

Offline grocery:
- Homeplus / MBK
- court-led restructuring
- liquidation value vs going-concern value
- debt issue / credit downgrade / job preservation
- unlisted but sector hard reference

Global confectionery:
- Lotte Wellfood / Lotte India
- Pepero / ChocoPie localization
- India snacks market
- capex vs EBITDA / volume conversion

Food service event:
- Kyochon / Cherrybro / Neuromeka
- Jensen Huang fried-chicken event
- meme demand vs same-store sales / franchise margin
```

---

# 4. 국장 신규 후보 case

## Case A — Samyang Foods `structural_success_candidate + single-SKU/input watch`

```text
symbol = 003230
case_type = structural_success_candidate + 4B-watch
archetype = K_FOOD_EXPORT_ASP_CAPACITY
```

### stage date

```text
Stage 1:
2023~2024
- Buldak global viral demand
- U.S. / Europe export expansion
- spicy ramen category premium

Stage 2:
2024-06-14
- Kiwoom raises 2Q OP estimate to 81.2B won
- +84% YoY operating profit estimate
- ASP continues to rise
- U.S. / Europe shipments increase
- capacity expansion supports revenue and earnings

Stage 3:
2024-06-14 candidate
- export + ASP + OP revision + capacity expansion이 동시에 확인된 구간

Stage 4B:
single-SKU Buldak premium이 valuation을 먼저 끌면 watch

Stage 4C:
input cost / packaging / single-product demand fade / channel inventory risk
```

Samyang은 R5의 K-food structural benchmark다. MarketWatch/WSJ Market Talk는 2024년 6월 14일 Kiwoom이 Samyang의 2Q 영업이익 추정치를 812억 원으로 올렸고, 이는 전년 대비 +84%이며, Buldak ASP 상승, U.S./Europe shipment 증가, capacity expansion이 근거였다고 보도했다. 같은 날 Samyang 주가는 5.7% 상승해 647,000원에 마감했고, 목표가는 830,000원으로 26% 상향됐다. ([마켓워치][1])

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch / WSJ Market Talk reported price and earnings anchor

entry_date:
2024-06-14

stage3_price:
647,000 won

event_MFE_1D:
+5.7%

implied_prior_close:
647,000 / 1.057
= 611,921 won

target_price:
830,000 won

target_upside_from_stage3_price:
830,000 / 647,000 - 1
= +28.3%

Q2_OP_estimate:
81.2B won

OP_growth_estimate:
+84% YoY

MFE_30D / 90D / 180D / 1Y / 2Y:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = aligned_partial
rerating_result = K_food_export_ASP_capacity_rerating_candidate
stage_failure_type = Green_candidate_but_single_SKU_4B_watch
```

---

## Case B — CJ Olive Young / CJ Corp exposure `success_candidate, but not Green`

```text
symbol = CJ Corp indirect exposure / CJ Olive Young unlisted
case_type = success_candidate + insufficient_price_data
archetype = H_AND_B_RETAIL_GLOBAL_PLATFORM
```

### stage date

```text
Stage 1:
2024~2025
- K-beauty global demand
- Olive Young as offline/online curation platform
- foreign tourist traffic + global online platform

Stage 2:
2025-06-05
- Olive Young plans first U.S. store in Los Angeles
- California is the biggest customer region for Olive Young global online platform
- K-beauty exports and U.S. demand support H&B retail platform narrative

Stage 3:
없음
- Olive Young is unlisted
- CJ Corp Green requires contribution to earnings, dividend/capital return, platform margin visibility
- store traffic alone is not Green

Stage 4B:
Olive Young IPO / U.S. store headline로 CJ Corp 또는 K-beauty basket이 먼저 오르면 watch

Stage 4C:
U.S. tariff, physical-store sell-through miss, inventory build, China demand weakness
```

Reuters는 Olive Young이 LA에 첫 U.S. store를 열 계획이라고 보도했고, Olive Young의 global online shopping platform에서 California 고객 비중이 가장 크다고 전했다. 같은 기사에서 한국 화장품 생산의 5분의 4가 수출이고, K-beauty가 e-commerce 중심으로 U.S. market에서 빠르게 성장하고 있다고 설명했다. 다만 Olive Young은 비상장이고, CJ Corp 주주 입장에서는 platform traffic이 실제 지분가치·배당·상장·이익기여로 닫혀야 Stage 3다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters K-beauty / Olive Young business anchor

stage3_price:
N/A

listed_exposure:
CJ Corp indirect

Olive_Young_US_store_plan:
Los Angeles, planned as early as 2025

California_customer_context:
largest customer region for Olive Young global online shopping platform

South_Korea_cosmetics_output:
$13B context in Reuters source

export_share:
about four-fifths of output

CJ_Corp_event_price:
price_data_unavailable_after_deep_search

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate_but_insufficient_price_data
rerating_result = H_and_B_retail_global_platform_watch
stage_failure_type = unlisted_subsidiary_not_parent_green
```

---

## Case C — Dr.G / Gowoonsesang `K-beauty brand M&A validation`

```text
listed_exposure = Cosmax / Kolmar / Amore / CJ Olive Young / K-beauty basket
direct_company = Gowoonsesang / Dr.G unlisted
case_type = success_candidate + M&A validation, not Green
archetype = K_BEAUTY_BRAND_M_AND_A_VALIDATION
```

### stage date

```text
Stage 1:
2024-12-20
- L'Oreal in final talks to acquire Gowoonsesang / Dr.G
- K-beauty brand M&A validation

Stage 2:
2024-12-23
- L'Oreal confirms acquisition
- Dr.G is Korean dermocosmetics facial-care leader
- buyer sees pan-Asian and global growth potential

Stage 3:
없음
- direct target is unlisted
- ODM / distributor / listed K-beauty firms need actual order, margin, sell-through bridge

Stage 4B:
K-beauty M&A headline만으로 ODM/brand basket 급등 시 watch

Stage 4C:
brand M&A validation fades, China slowdown, tariff, retailer inventory risk
```

Reuters는 L’Oreal이 Migros의 Gowoonsesang Cosmetics, 즉 Dr.G 브랜드를 인수한다고 보도했다. Dr.G는 Korean dermocosmetics facial care line에서 1위로 소개됐고, L’Oreal은 한국과 글로벌 시장에서 성장 잠재력을 기대한다고 밝혔다. 이건 K-beauty brand value의 Stage 2 validation이지만, direct listed revenue가 아니므로 Cosmax·Kolmar·Silicon2·Amore·CJ exposure에 곧바로 Green을 주면 안 된다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters L'Oreal / Dr.G acquisition anchor

stage3_price:
N/A

target:
Gowoonsesang Cosmetics / Dr.G

buyer:
L'Oreal

seller:
Migros / Mibelle Group

deal_value:
not disclosed

Mibelle_2023_revenue:
661M Swiss francs / about $739M in Reuters source

DrG_market_position:
No.1 facial care line in Korean dermocosmetics market, per source

listed_stock_price_path:
price_data_unavailable_after_deep_search

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate_M&A_validation
rerating_result = K_beauty_brand_value_validation_watch
stage_failure_type = brand_M&A_not_listed_revenue
```

---

## Case D — d’Alba / Silicon2 / Cosmax / Kolmar basket `success_candidate + 4B-watch`

```text
symbols = 483650 / 257720 / 192820 / 161890
case_type = success_candidate + overheat_watch
archetype = K_BEAUTY_INDIE_PHYSICAL_STORE_TEST
```

### stage date

```text
Stage 1:
2024~2025
- indie K-beauty U.S. e-commerce growth
- Amazon / TikTok / social commerce virality
- ODM and distributor leverage

Stage 2:
2025-06-05
- Tirtir / d'Alba / Torriden / Beauty of Joseon physical-store talks
- Ulta / Sephora / Target / Costco channel tests
- top-five K-beauty brands in U.S. e-commerce +71% over two years
- overall U.S. beauty market +21%

Stage 4B:
2025-06-05
- d'Alba shares more than doubled since debut last month
- price moved before physical-store sell-through

Stage 3:
없음
- physical-store sales, repeat order, inventory, OPM, working capital 확인 필요
```

Reuters는 Tirtir, d’Alba, Torriden, Beauty of Joseon 같은 Korean beauty brands가 Ulta, Sephora, Target, Costco 등 U.S. retailers와 physical-store 입점 논의를 진행 중이라고 보도했다. 같은 기사에서 U.S. e-commerce 상위 5개 K-beauty 브랜드 매출은 2년간 평균 +71% 성장해 전체 U.S. market +21%를 3.38배 웃돌았다. 그러나 d’Alba는 상장 후 한 달 만에 주가가 2배 이상 올랐고, Silicon2 CEO는 장기 성장을 위해 physical-store sales가 필요하다고 말했다. 즉 이 basket은 Stage 2가 강하지만, Green은 physical sell-through 뒤다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters K-beauty retail / e-commerce / d'Alba price anchor

stage3_price:
N/A

top5_K_beauty_US_ecommerce_growth:
+71% over two years

overall_US_market_growth:
+21%

relative_growth_multiple:
71 / 21
= 3.38x

dAlba_reported_return_since_debut:
> +100%

retail_talks:
Ulta / Sephora / Target / Costco

ODM_leverage:
Cosmax / Kolmar

distribution_leverage:
Silicon2

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate_plus_4B_watch
rerating_result = K_beauty_indie_physical_store_test
stage_failure_type = e-commerce_success_not_physical_store_green
```

---

## Case E — E-Mart / Shinsegae / Alibaba JV `Stage 2 scale + data gate`

```text
symbols = 139480 / 004170
case_type = success_candidate + data_gate_watch
archetype = ECOMMERCE_JV_SCALE_DATA_GATE
```

### stage date

```text
Stage 1:
2024-12-26
- Shinsegae / E-Mart e-commerce restructuring
- Gmarket + AliExpress Korea combination
- Chinese cross-border e-commerce pressure

Stage 2:
2024-12-26
- E-Mart / Alibaba 50:50 JV plan
- E-Mart shares +5.5%

Stage 2 validation:
2025-09-18
- KFTC conditional approval
- cross-border market share expected 41%
- Gmarket has 50M customer database
- 3-year restriction on Korean overseas-shopping data sharing

Stage 3:
없음
- GMV, take-rate, margin, retention, data compliance 확인 전 Green 금지

Stage 4B:
JV headline로 price가 먼저 오르면 watch

Stage 4C:
customer-data misuse, product safety, Temu/AliExpress price war, margin dilution
```

E-Mart/Alibaba JV는 R5 retail/e-commerce의 좋은 Stage 2다. WSJ는 E-Mart와 Alibaba가 AliExpress Korea와 Gmarket을 묶는 50:50 JV를 추진한다고 보도했고, 발표 당일 E-Mart 주가는 5.5% 올랐다. 이후 KFTC는 조건부 승인을 내리면서, Gmarket의 5,000만 고객 데이터와 Alibaba의 data analytics 결합이 market power를 키울 수 있다고 봤고, 3년간 한국 고객 해외쇼핑 데이터 공유를 제한했다. ([월스트리트저널][4])

### 실제 가격경로 검증

```text
price_data_source:
WSJ / Reuters JV and regulatory anchors

stage3_price:
N/A

E_Mart_event_MFE:
+5.5%

JV_structure:
50:50

assets:
Gmarket + AliExpress Korea

KFTC_approval:
conditional

expected_cross_border_market_share:
41%

Gmarket_customer_database:
50M customers

data_sharing_restriction:
3 years

Korean_spending_on_Chinese_online_imports_2024:
4.7T won / $3.4B

growth_2024:
+32%

Alibaba_share_by_value:
62%

MFE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate_data_gate_watch
rerating_result = e_commerce_JV_scale_watch
stage_failure_type = JV_headline_not_GMV_margin_green
```

---

## Case F — Homeplus / MBK `offline grocery distress hard reference`

```text
direct_company = Homeplus unlisted
listed_exposure = Lotte Shopping / E-Mart / grocery-retail sector read-through
case_type = 4C-thesis-break reference
archetype = OFFLINE_GROCERY_DISTRESS_4C
```

### stage date

```text
Stage 1:
2024~2025
- offline hypermarket/grocery competition
- COVID after-effect
- e-commerce competition
- private-equity ownership / credit risk

Stage 4C:
2025-03
- Homeplus enters court-led restructuring

Stage 4C validation:
2025-06-13
- liquidation value exceeds going-concern value
- liquidation value 3.7T won
- total assets 6.8T won
- MBK to cancel shares worth 2.5T won / $1.83B
- sale aimed to avoid liquidation

Stage 4C validation:
2025-06-20
- court approves sale plan
- purpose: repay creditors, protect jobs, protect partner firms

Stage 3:
없음
- offline grocery distress is sector hard reference, not Green
```

Homeplus는 비상장이라 직접 KRX price path는 없지만, R5 offline retail의 hard 4C reference로 넣어야 한다. Reuters는 Homeplus가 court-led restructuring에 들어갔고, court-commissioned review에서 liquidation value가 going-concern value보다 높았다고 보도했다. Homeplus liquidation value는 3.7조 원, total assets는 6.8조 원이었으며, MBK는 2.5조 원 상당 보통주를 write-off하고 sale을 추진했다. 이는 “오프라인 grocery 자산이 많다”가 Green이 아니라, 경쟁·부채·회전율이 깨지면 바로 hard gate가 된다는 사례다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters Homeplus restructuring / sale-plan anchors

stage3_price:
N/A

direct_listed_ticker:
N/A

court_led_restructuring:
2025-03

liquidation_value:
3.7T won

total_assets:
6.8T won

liquidation_value_to_assets:
3.7 / 6.8
= 54.4%

MBK_share_writeoff:
2.5T won / $1.83B

sale_plan:
approved by Seoul Bankruptcy Court

sale_purpose:
repay creditors
preserve jobs
protect partner firms

direct_MFE_MAE:
N/A

listed_sector_price_path:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_reference
rerating_result = offline_grocery_distress_hard_reference
stage_failure_type = unlisted_but_sector_4C_reference
```

---

## Case G — Lotte Wellfood / Lotte India `global confectionery localization candidate`

```text
symbol = 280360
case_type = success_candidate + insufficient_price_data
archetype = GLOBAL_CONFECTIONERY_LOCALIZATION
```

### stage date

```text
Stage 1:
2025
- Pepero / ChocoPie overseas localization
- India snacks market growth
- Lotte India + Havmor integration

Stage 2:
2025-07-24
- Lotte India targets turnover 3,000 crore rupees by 2027
- 2025 turnover expected over 2,000 crore rupees
- FY25-26 capex 475 crore rupees
- Pepero investment 225 crore rupees
- confectionery division EBITDA 13%
- overall snacks market 1.7 lakh crore rupees, growing 13~14%

Stage 3:
없음
- India localization은 Stage 2
- parent-company revenue recognition, margin, FCF, FX/capex risk 확인 필요

Stage 4B:
Pepero / India growth headline로 price가 먼저 오르면 watch

Stage 4C:
India execution miss, capex overrun, cocoa/sugar cost, FX, working capital
```

Lotte Wellfood는 R5 global confectionery localization 후보로 둘 수 있다. Times of India는 Lotte India가 2025년 매출 2,000 crore rupees 이상, 2027년 3,000 crore rupees 목표를 제시했고, FY25-26 capex 475 crore rupees 중 Pepero 관련 투자 225 crore rupees를 계획한다고 보도했다. 또한 confectionery division EBITDA가 13%이고, India snacks market이 1.7 lakh crore rupees 규모로 13~14% 성장 중이라고 전했다. 다만 parent Lotte Wellfood 주주 입장에서는 인도 매출·마진·FCF가 연결 실적으로 확인되어야 한다. ([The Times of India][6])

### 실제 가격경로 검증

```text
price_data_source:
Times of India / Lotte India business anchor

stage3_price:
N/A

Lotte_India_2025_turnover_expected:
>2,000 crore rupees

Lotte_India_2027_turnover_target:
3,000 crore rupees

target_growth_from_2025:
3,000 / 2,000 - 1
= at least +50%

FY25_26_capex:
475 crore rupees

Pepero_investment:
225 crore rupees

Pepero_share_of_capex:
225 / 475
= 47.4%

confectionery_division_EBITDA:
13%

India_snacks_market_size:
1.7 lakh crore rupees

India_snacks_market_growth:
13~14%

Lotte_Wellfood_stock_OHLC:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate_but_insufficient_price_data
rerating_result = global_confectionery_localization_watch
stage_failure_type = overseas_capex_not_parent_green
```

---

## Case H — Kyochon / Cherrybro / Neuromeka Jensen event `price_moved_without_evidence`

```text
symbols = 339770 / 066360 / 348340
case_type = overheat / price_moved_without_evidence
archetype = FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM
```

### stage date

```text
Stage 1:
2025-10-31
- Jensen Huang visits Korean fried-chicken restaurant
- Samsung / Hyundai executives present
- APEC and Nvidia Korea chip deal context

Stage 2:
없음
- no same-store sales evidence
- no franchise margin evidence
- no store traffic conversion evidence

Stage 4B:
2025-10-31
- Kyochon up to about +20%
- Cherrybro up to daily limit +30%
- Neuromeka also surged
- MarketWatch: only Neuromeka retained gains by close
- restaurant visited was non-listed Kkanbu Chicken

Stage 3:
없음
```

이 case는 R5의 가장 깨끗한 `price_moved_without_evidence`다. Nvidia CEO Jensen Huang이 Samsung·Hyundai 경영진과 비상장 Kkanbu Chicken에서 식사한 이벤트가 퍼지자, Kyochon F&B, Cherrybro, Neuromeka가 급등했다. Tom’s Hardware는 Kyochon이 최대 20%, Cherrybro가 daily limit 30%까지 올랐다고 보도했고, MarketWatch는 세 종목 중 Neuromeka만 종가까지 상승분을 유지했다고 전했다. 이건 브랜드·매장 매출 evidence가 아니라 meme/event premium이다. ([Tom's Hardware][7])

### 실제 가격경로 검증

```text
price_data_source:
Tom's Hardware / MarketWatch event-return anchors

stage3_price:
N/A

Kyochon_event_MFE:
up to +20%

Cherrybro_event_MFE:
up to +30%

Neuromeka_event:
surged; only one of three retained gains by close, per MarketWatch

event_driver:
Jensen Huang fried-chicken dinner at non-listed Kkanbu Chicken

fundamental_revenue_evidence:
not confirmed

same_store_sales:
not confirmed

franchise_margin:
not confirmed

MFE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = price_moved_without_evidence
rerating_result = celebrity_food_event_premium
stage_failure_type = should_have_been_stage1_or_4B_watch
```

---

# 5. 이번 R5 case별 요약표

| case                            | 분류                               |                                                             실제 가격검증 | alignment            |
| ------------------------------- | -------------------------------- | ------------------------------------------------------------------: | -------------------- |
| Samyang Foods                   | structural_success_candidate     |             647,000원, +5.7%, target upside +28.3%, OP estimate +84% | aligned_partial      |
| CJ Olive Young / CJ Corp        | success_candidate / insufficient | LA store plan, export/H&B platform evidence, no parent price anchor | platform Stage 2     |
| Dr.G / L’Oreal                  | M&A validation                   |  deal value undisclosed, Mibelle revenue 661M CHF, no listed direct | brand M&A Stage 2    |
| d’Alba / Silicon2 / ODM         | success + 4B                     |                     top-five K-beauty +71%, market +21%, d’Alba >2x | physical-store gate  |
| E-Mart / Alibaba                | success + data gate              |                        E-Mart +5.5%, JV share 41%, Gmarket 50M data | Stage 2              |
| Homeplus / MBK                  | retail distress reference        |             liquidation value 3.7T, assets 6.8T, MBK write-off 2.5T | sector 4C reference  |
| Lotte Wellfood / India          | success_candidate / insufficient |                          India target +50%, capex 475cr, EBITDA 13% | localization Stage 2 |
| Kyochon / Cherrybro / Neuromeka | overheat                         |                     Kyochon +20%, Cherrybro +30%, no sales evidence | price-only           |

---

# 6. score-price alignment 판정

```text
aligned / structural_success_candidate:
- Samyang Foods

success_candidate:
- CJ Olive Young / CJ Corp exposure
- Dr.G / K-beauty brand M&A validation
- d'Alba / Silicon2 / Cosmax / Kolmar
- E-Mart / Shinsegae-Alibaba JV
- Lotte Wellfood / India localization

event_premium:
- Dr.G / L'Oreal M&A read-through if ODM/brand basket moves before orders
- E-Mart Alibaba JV headline
- Kyochon / Cherrybro / Neuromeka Jensen event

price_moved_without_evidence:
- Kyochon / Cherrybro / Neuromeka
- d'Alba if physical-store sell-through not confirmed
- CJ/Olive Young if U.S. store headline moves parent before earnings bridge
- Lotte India capex if parent stock moves before consolidated margin/FCF

thesis_break_reference:
- Homeplus / MBK offline grocery distress

4B-watch:
- Samyang single-SKU premium
- d'Alba >2x post-debut
- E-Mart +5.5% JV event before GMV/margin
- Kyochon/Cherrybro +20~30% celebrity event
- Olive Young IPO/U.S. store speculation before parent earnings bridge

hard_4C:
- direct_krx_hard_4c_not_confirmed
- Homeplus = unlisted sector hard 4C reference
```

---

# 7. 점수비중 교정

## 올릴 축

```text
repeat_purchase +5
overseas_sell_through +5
physical_store_sell_through +5
ASP_uplift +4
channel_retention +5
inventory_quality +4
working_capital_quality +4
OPM_FCF_conversion +5
data_compliance +5
platform_trust +5
```

### 왜 올리나

Samyang은 export·ASP·OP revision·capacity가 동시에 붙었기 때문에 Green 후보가 가능했다. 반면 K-beauty indie와 Olive Young/CJ는 global traffic·retail talks·platform narrative는 강하지만, physical-store sell-through와 parent earnings bridge가 필요하다. E-Mart/Alibaba는 scale보다 data compliance가 더 중요해졌다. Homeplus는 offline grocery에서 회전율·부채·자금조달이 깨지면 자산가치가 무너지는 hard reference다.

## 내릴 축

```text
brand_heat_only -5
viral_event_only -5
M&A_validation_without_revenue -4
U.S._store_plan_without_sell_through -4
retail_talks_without_orders -5
JV_without_GMV_margin -5
offline_asset_value_without_cashflow -5
overseas_capex_without_parent_FCF -4
single_SKU_concentration -4
customer_data_risk -5
```

### 왜 내리나

Kyochon/Jensen event는 매출 evidence 없이 +20~30%가 나온 전형적 4B다. Dr.G/L’Oreal은 K-beauty brand value validation이지만 직접 상장 매출은 아니다. Lotte India capex는 성장성은 좋지만 parent FCF가 확인되어야 한다. E-Mart JV는 scale이 있어도 customer data gate가 있다.

## Green gate 강화 조건

```text
R5 Stage 3-Green 필수:
1. 반복구매 / 반복수요 확인
2. 해외 sell-through 확인
3. physical-store sell-through 확인
4. ASP 또는 mix 개선
5. OPM / FCF 개선
6. 재고·매출채권 안정
7. channel retention / reorder 확인
8. customer data / platform trust risk 통과
9. 가격경로가 evidence 이후 따라옴

금지:
K-food / K-beauty label only
U.S. store plan only
M&A validation only
retail talks only
celebrity food event only
JV headline only
offline asset value only
overseas capex only
```

## 4B 조기감지 조건

```text
4B-watch:
상장 직후 또는 debut 이후 2배 이상 상승
single-SKU / single-brand concentration 70~90%+
U.S. store / Sephora / Ulta / Target / Costco 입점 기대만으로 급등
M&A validation으로 ODM/brand basket 동반 급등
JV / platform data-scale headline로 급등
celebrity event로 +20~30% 급등
offline retail restructuring relief로 price만 반등

4B-elevated:
physical-store sell-through 미확인
same-store sales 미확인
franchise margin 미확인
data-sharing restriction 존재
inventory 증가
parent earnings bridge 없음
```

## 4C hard gate 조건

```text
channel stuffing
inventory build
receivables deterioration
physical-store sell-through failure
customer data misuse
platform trust break
offline grocery court-led restructuring
liquidation value > going-concern value
input cost shock without pass-through
single-SKU demand fade
celebrity event fade
```

이번 R5 Loop 12에서 직접 상장 hard 4C는 확정하지 않는다. 다만 **Homeplus는 unlisted offline grocery sector hard 4C reference**로 둔다. E-Mart/Alibaba data gate, K-beauty physical-store test, Kyochon meme rally는 각각 4C-watch / 4B-watch로 반영한다.

---

# 8. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
```

---

# 9. patch-ready 출력

## docs/round/round_189.md 요약

```md
# R5 Loop 12. Consumer / Retail / Brand Price Validation

이번 라운드는 R5 Loop 12 price-validation 라운드다.

핵심 결론:
- Samyang Foods remains the R5 K-food export benchmark. Stage anchor was 647,000 won, +5.7%, with target price 830,000 won and Q2 OP estimate +84% YoY. It is aligned_partial but single-SKU 4B-watch remains.
- CJ Olive Young / CJ Corp exposure is H&B global retail Stage 2. Olive Young plans its first U.S. store in Los Angeles and has strong global platform evidence, but parent-company earnings bridge and listed price path are unavailable.
- Dr.G / Gowoonsesang acquisition by L’Oreal validates K-beauty brand value, but it is unlisted and does not automatically make ODM/distributor/listed-brand names Green.
- d’Alba / Silicon2 / Cosmax / Kolmar basket is K-beauty Stage 2 plus 4B-watch. Top-five K-beauty U.S. e-commerce brands grew +71% vs U.S. market +21%, but d’Alba has more than doubled since debut and physical-store sell-through is required.
- E-Mart / Shinsegae-Alibaba JV is Stage 2 plus data gate. E-Mart +5.5%, JV expected cross-border share 41%, Gmarket 50M customer data, and three-year data-sharing restriction.
- Homeplus / MBK is offline grocery sector hard reference. Liquidation value 3.7T won, total assets 6.8T won, MBK write-off 2.5T won. It is unlisted but important as R5 offline retail 4C reference.
- Lotte Wellfood / Lotte India is global confectionery localization Stage 2. 2027 target turnover 3,000 crore rupees vs 2025 over 2,000 crore, capex 475 crore, Pepero investment 225 crore, confectionery EBITDA 13%.
- Kyochon / Cherrybro / Neuromeka Jensen event is price_moved_without_evidence. Kyochon up to +20%, Cherrybro up to +30%, but no same-store sales, franchise margin, or repeat demand evidence.
```

## docs/checkpoints/checkpoint_28a_round189_r5_loop12.md 요약

```md
# Checkpoint 28A Round 189 R5 Loop 12 Consumer Retail Brand Price Validation

## 반영 내용
- R5 Loop 12 price-validation 라운드를 추가했다.
- K-food export, H&B retail platform, K-beauty M&A validation, indie K-beauty physical-store test, e-commerce JV data gate, offline grocery distress, global confectionery localization, celebrity food-service event를 비교했다.
- Reuters / WSJ / MarketWatch / Times of India / Tom's Hardware anchors로 가능한 MFE/MAE 및 event metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- repeat purchase, overseas sell-through, physical-store sell-through, ASP uplift, channel retention, inventory quality, OPM/FCF, data compliance, platform trust 가중치 강화
- brand heat only, celebrity event only, M&A validation without revenue, U.S. store plan without sell-through, retail talks without orders, JV without GMV/margin, offline asset value without cashflow 감점 강화
```

## data/e2r_case_library/cases_r5_loop12_round189.jsonl 초안

```jsonl
{"case_id":"r5_loop12_samyang_buldak_export_asp_capacity","symbol":"003230","company_name":"Samyang Foods","case_type":"structural_success_candidate","primary_archetype":"K_FOOD_EXPORT_ASP_CAPACITY","stage2_date":"2024-06-14","stage3_date":"2024-06-14_candidate","stage4b_date":"single_sku_watch","price_validation":{"price_data_source":"MarketWatch/WSJ Market Talk reported price and earnings anchor","entry_date":"2024-06-14","stage3_price_krw":647000,"event_mfe_1d_pct":5.7,"implied_prior_close_krw":611921,"target_price_krw":830000,"target_upside_from_stage3_price_pct":28.3,"q2_op_estimate_krw_bn":81.2,"op_growth_estimate_pct":84,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"aligned_partial","rerating_result":"K_food_export_ASP_capacity_rerating_candidate","notes":"Export, ASP, OP revision and capacity expansion support Stage 3 candidate; single-SKU concentration remains 4B-watch."}
{"case_id":"r5_loop12_cj_olive_young_hb_global_platform","symbol":"CJ_Corp_indirect","company_name":"CJ Olive Young / CJ Corp exposure","case_type":"success_candidate","primary_archetype":"H_AND_B_RETAIL_GLOBAL_PLATFORM","stage2_date":"2025-06-05","price_validation":{"price_data_source":"Reuters K-beauty / Olive Young business anchor","stage3_price":null,"listed_exposure":"CJ Corp indirect","olive_young_us_store_plan":"Los Angeles, planned as early as 2025","california_customer_context":"largest customer region for Olive Young global online shopping platform","south_korea_cosmetics_output_usd_bn":13,"export_share_context":"about four-fifths of output","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_insufficient_price_data","rerating_result":"H_and_B_retail_global_platform_watch","notes":"Strong H&B retail platform evidence, but Olive Young is unlisted; parent earnings bridge and listed price path required."}
{"case_id":"r5_loop12_dr_g_loreal_kbeauty_brand_mna_validation","symbol":"K_beauty_ODM_brand_basket","company_name":"Dr.G / Gowoonsesang / L'Oreal acquisition read-through","case_type":"success_candidate","primary_archetype":"K_BEAUTY_BRAND_M_AND_A_VALIDATION","stage2_date":"2024-12-23","price_validation":{"price_data_source":"Reuters L'Oreal / Dr.G acquisition anchor","stage3_price":null,"target":"Gowoonsesang Cosmetics / Dr.G","buyer":"L'Oreal","seller":"Migros / Mibelle Group","deal_value":"not_disclosed","mibelle_2023_revenue_chf_mn":661,"mibelle_2023_revenue_usd_mn":739,"drg_market_position":"No.1 facial care line in Korean dermocosmetics market per source","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_M&A_validation","rerating_result":"K_beauty_brand_value_validation_watch","notes":"Brand M&A validates K-beauty value, but it is not listed-company revenue; ODM/distributor order bridge required."}
{"case_id":"r5_loop12_dalba_silicon2_cosmax_kolmar_physical_store_test","symbol":"483650/257720/192820/161890","company_name":"d'Alba / Silicon2 / Cosmax / Kolmar basket","case_type":"success_candidate","primary_archetype":"K_BEAUTY_INDIE_PHYSICAL_STORE_TEST","stage2_date":"2025-06-05","stage4b_date":"2025-06-05","price_validation":{"price_data_source":"Reuters K-beauty retail/e-commerce/d'Alba anchor","stage3_price":null,"top5_kbeauty_us_ecommerce_growth_pct":71,"overall_us_market_growth_pct":21,"relative_growth_multiple":3.38,"dalba_reported_return_since_debut_pct":100,"retail_talks":["Ulta","Sephora","Target","Costco"],"odm_leverage":["Cosmax","Kolmar"],"distribution_leverage":"Silicon2","price_validation_status":"reported_return_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_plus_4B_watch","rerating_result":"K_beauty_indie_physical_store_test","notes":"E-commerce growth is strong, but physical-store sell-through, repeat orders, inventory and OPM required before Green."}
{"case_id":"r5_loop12_emart_shinsegae_alibaba_jv_data_gate","symbol":"139480/004170","company_name":"E-Mart / Shinsegae / Alibaba JV","case_type":"success_candidate","primary_archetype":"ECOMMERCE_JV_SCALE_DATA_GATE","stage2_date":"2024-12-26/2025-09-18","price_validation":{"price_data_source":"WSJ/Reuters JV and KFTC regulatory anchors","stage3_price":null,"emart_event_mfe_pct":5.5,"jv_structure":"50:50","assets":["Gmarket","AliExpress Korea"],"kftc_approval":"conditional","expected_cross_border_market_share_pct":41,"gmarket_customer_database_mn":50,"data_sharing_restriction_years":3,"korean_spending_chinese_online_imports_2024_krw_trn":4.7,"growth_2024_pct":32,"alibaba_share_by_value_pct":62,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_data_gate_watch","rerating_result":"e_commerce_JV_scale_watch","notes":"JV scale is Stage 2; GMV, take-rate, margin, retention and data compliance required before Green."}
{"case_id":"r5_loop12_homeplus_mbk_offline_grocery_distress_reference","symbol":"unlisted_Homeplus/Lotte_Shopping_E-Mart_sector_readthrough","company_name":"Homeplus / MBK Partners","case_type":"4c_reference","primary_archetype":"OFFLINE_GROCERY_DISTRESS_4C","stage4c_date":"2025-03/2025-06","price_validation":{"price_data_source":"Reuters Homeplus restructuring / sale-plan anchors","stage3_price":null,"direct_listed_ticker":"N/A","court_led_restructuring":"2025-03","liquidation_value_krw_trn":3.7,"total_assets_krw_trn":6.8,"liquidation_value_to_assets_pct":54.4,"mbk_share_writeoff_krw_trn":2.5,"mbk_share_writeoff_usd_bn":1.83,"sale_plan":"approved by Seoul Bankruptcy Court","sale_purpose":["repay creditors","preserve jobs","protect partner firms"],"price_validation_status":"unlisted_sector_reference"},"score_price_alignment":"thesis_break_reference","rerating_result":"offline_grocery_distress_hard_reference","notes":"Unlisted but important R5 hard reference: offline grocery asset value is not Green without cashflow and debt stability."}
{"case_id":"r5_loop12_lotte_wellfood_india_pepero_localization","symbol":"280360","company_name":"Lotte Wellfood / Lotte India","case_type":"success_candidate","primary_archetype":"GLOBAL_CONFECTIONERY_LOCALIZATION","stage2_date":"2025-07-24","price_validation":{"price_data_source":"Times of India / Lotte India business anchor","stage3_price":null,"lotte_india_2025_turnover_expected_crore_inr":2000,"lotte_india_2027_turnover_target_crore_inr":3000,"target_growth_from_2025_pct":50,"fy25_26_capex_crore_inr":475,"pepero_investment_crore_inr":225,"pepero_share_of_capex_pct":47.4,"confectionery_division_ebitda_pct":13,"india_snacks_market_size_lakh_crore_inr":1.7,"india_snacks_market_growth_pct":"13-14","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_insufficient_price_data","rerating_result":"global_confectionery_localization_watch","notes":"India localization is Stage 2; parent-company revenue recognition, margin, FCF and FX/capex risk must confirm."}
{"case_id":"r5_loop12_kyochon_cherrybro_neuromeka_jensen_event","symbol":"339770/066360/348340","company_name":"Kyochon F&B / Cherrybro / Neuromeka","case_type":"overheat","primary_archetype":"FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM","stage1_date":"2025-10-31","stage4b_date":"2025-10-31","price_validation":{"price_data_source":"Tom's Hardware / MarketWatch event-return anchors","stage3_price":null,"kyochon_event_mfe_pct":20,"cherrybro_event_mfe_pct":30,"neuromeka_event":"surged; only one of three retained gains by close per MarketWatch","event_driver":"Jensen Huang fried-chicken dinner at non-listed Kkanbu Chicken","fundamental_revenue_evidence_confirmed":false,"same_store_sales_confirmed":false,"franchise_margin_confirmed":false,"price_validation_status":"reported_event_return_not_full_ohlc"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"celebrity_food_event_premium","notes":"Viral celebrity food-service event is 4B/event premium until same-store sales, franchise margin and repeat demand confirm."}
```

## data/sector_taxonomy/score_weight_profiles_round189_r5_loop12_v1.csv 초안

```csv
archetype,repeat_purchase,overseas_sell_through,physical_store_sell_through,asp_uplift,channel_retention,inventory_quality,working_capital_quality,opm_fcf,data_compliance,platform_trust,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
K_FOOD_EXPORT_ASP_CAPACITY,+5,+5,+3,+5,+4,+4,+4,+5,+1,+2,-2,+4,+4,Samyang supports Green candidate when export/ASP/OP revision/capacity align, but single-SKU watch remains.
H_AND_B_RETAIL_GLOBAL_PLATFORM,+5,+5,+5,+3,+5,+4,+4,+5,+4,+5,-4,+5,+4,Olive Young is Stage 2; parent earnings bridge and physical-store economics required.
K_BEAUTY_BRAND_M_AND_A_VALIDATION,+4,+5,+4,+3,+4,+3,+3,+4,+1,+2,-5,+5,+3,Dr.G/L'Oreal validates brand value but not listed-company revenue.
K_BEAUTY_INDIE_PHYSICAL_STORE_TEST,+5,+5,+5,+3,+5,+5,+5,+5,+1,+2,-4,+5,+4,d'Alba/Silicon2/Cosmax/Kolmar need physical-store sell-through and inventory control.
ECOMMERCE_JV_SCALE_DATA_GATE,+4,+3,+0,+2,+5,+4,+4,+5,+5,+5,-5,+5,+5,E-Mart/Alibaba JV is Stage 2 but data compliance and GMV/margin gate are essential.
OFFLINE_GROCERY_DISTRESS_4C,+0,+0,+0,+0,+0,+5,+5,+5,+2,+3,0,+3,+5,Homeplus is sector hard reference for offline grocery distress.
GLOBAL_CONFECTIONERY_LOCALIZATION,+5,+5,+4,+3,+4,+4,+4,+5,+1,+2,-3,+4,+4,Lotte India localization is Stage 2 until parent revenue/margin/FCF confirm.
FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM,+2,+1,+2,+2,+2,+3,+3,+4,+1,+2,-5,+5,+3,Kyochon/Cherrybro/Neuromeka Jensen event is price_moved_without_evidence.
```

---

# 이번 R5 Loop 12 결론

```text
1. Samyang은 R5의 K-food export benchmark다.
   export, ASP, OP revision, capacity가 같이 붙었기 때문에 Stage 3 후보가 가능했다.

2. CJ Olive Young은 H&B global platform Stage 2다.
   그러나 비상장 자회사라 CJ Corp Green은 earnings bridge가 필요하다.

3. Dr.G / L'Oreal deal은 K-beauty brand value validation이다.
   하지만 M&A validation이 곧 ODM/brand basket Green은 아니다.

4. d'Alba / Silicon2 / Cosmax / Kolmar는 K-beauty Stage 2다.
   e-commerce growth는 좋지만 physical-store sell-through 전에는 4B-watch다.

5. E-Mart / Alibaba JV는 retail/e-commerce Stage 2다.
   scale보다 data compliance, GMV, take-rate, margin 확인이 먼저다.

6. Homeplus는 unlisted지만 offline grocery hard reference다.
   liquidation value가 going-concern value보다 높다는 건 R5에서 강한 4C 신호다.

7. Lotte Wellfood / Lotte India는 global confectionery localization Stage 2다.
   Pepero/ChocoPie capex가 parent margin과 FCF로 닫혀야 한다.

8. Kyochon / Cherrybro / Neuromeka Jensen event는 price_moved_without_evidence다.
   celebrity event로 +20~30%가 나왔지만 same-store sales evidence는 없었다.
```

한 문장으로 압축하면:

> **R5에서 진짜 Stage 3는 “K-food·K-beauty·유통·브랜드가 핫하다”가 아니라, 반복구매·해외 sell-through·physical-store sell-through·ASP·OPM·재고/채권 품질·platform trust가 실제 돈으로 닫히는 순간이다.**

* [마켓워치](https://www.marketwatch.com/story/samyang-foods-set-to-post-strong-2q-earnings-market-talk-d654e045?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/korean-beauty-startups-bet-booming-us-demand-outlasts-tariff-pain-2025-06-05/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/markets/deals/frances-loreal-acquires-migros-south-korean-cosmetic-unit-2024-12-23/?utm_source=chatgpt.com)
* [월스트리트저널](https://www.wsj.com/business/e-mart-alibaba-plan-online-shopping-joint-venture-e5cfdc37?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-conditionally-approves-aliexpress-shinsegae-unit-joint-venture-2025-09-18/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/en/mbk-plans-sell-its-troubled-korean-supermarket-chain-homeplus-2025-06-13/?utm_source=chatgpt.com)
* [The Times of India](https://timesofindia.indiatimes.com/city/chennai/lotte-india-aiming-to-achieve-turnover-of-3000cr-by-2027/articleshow/122885066.cms?utm_source=chatgpt.com)
* [마켓워치](https://www.marketwatch.com/story/jensen-huang-spreads-nvidia-magic-to-fried-chicken-stocks-06b49648?utm_source=chatgpt.com)

[1]: https://www.marketwatch.com/story/samyang-foods-set-to-post-strong-2q-earnings-market-talk-d654e045?utm_source=chatgpt.com "Samyang Foods Set to Post Strong 2Q Earnings -- Market Talk"
[2]: https://www.reuters.com/world/asia-pacific/korean-beauty-startups-bet-booming-us-demand-outlasts-tariff-pain-2025-06-05/?utm_source=chatgpt.com "Korean beauty startups bet booming US demand outlasts tariff pain"
[3]: https://www.reuters.com/markets/deals/frances-loreal-acquires-migros-south-korean-cosmetic-unit-2024-12-23/?utm_source=chatgpt.com "L'Oreal acquires South Korea's Dr.G in skincare deal with Migros"
[4]: https://www.wsj.com/business/e-mart-alibaba-plan-online-shopping-joint-venture-e5cfdc37?utm_source=chatgpt.com "E-mart, Alibaba Plan Online-Shopping Joint Venture"
[5]: https://www.reuters.com/en/mbk-plans-sell-its-troubled-korean-supermarket-chain-homeplus-2025-06-13/?utm_source=chatgpt.com "MBK plans to sell its troubled Korean supermarket chain Homeplus"
[6]: https://timesofindia.indiatimes.com/city/chennai/lotte-india-aiming-to-achieve-turnover-of-3000cr-by-2027/articleshow/122885066.cms?utm_source=chatgpt.com "Lotte India aiming to achieve turnover of 3,000cr by 2027"
[7]: https://www.tomshardware.com/tech-industry/korean-fried-chicken-stocks-surge-30-percent-as-nvidia-ceo-jensen-huang-dines-out-on-local-delicacy-entire-industry-buoyed-by-secret-ingredient-jensanity?utm_source=chatgpt.com "Korean fried chicken stocks surge 30% as Nvidia CEO Jensen Huang dines out on local delicacy - entire industry buoyed by secret ingredient, Jensanity"

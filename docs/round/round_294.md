순서상 이번은 **R12 Loop 14 — 농업·생활서비스·기타 가격경로 검증 라운드**다.

```text
round = R12 Loop 14
round_id = round_222
large_sector = AGRICULTURE_LIFE_SERVICES_MISC
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
direct_KRX_hard_4c_confirmed = false
sector_hard_reference_confirmed = true
next_round = R13 Loop 14
```

이번 R12는 **Daedong/TYM 농기계, 농수산물·식품원가, Kyochon/Cherrybro/Neuromeka 치킨 meme rally, Naver/Uber/Baemin 배달앱 M&A, CJ Logistics/Hanjin/Coupang 배송노동·생활물류, KJ Environment/EQT 폐기물 플랫폼, 출산율·육아서비스, 사교육/hagwon 서비스**를 본다.

이번에도 KRX/Naver/Yahoo/Stooq의 **수정주가 일봉 OHLC 전체 window**는 안정적으로 확보하지 못했다. 그래서 30D/90D/180D/1Y/2Y full MFE·MAE는 만들지 않고, Reuters/FT/MarketWatch/AP/Barron’s가 보도한 **event return, event price, deal value, inflation metric, fertility metric, delivery-service operating event, recycling/waste data**를 가격 anchor로 썼다. 숫자를 만들 수 없는 구간은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R12 = 농업·생활서비스·기타
```

R12에서 진짜 Stage 3는 “농업”, “렌탈”, “육아”, “치킨”, “폐기물”, “배달”, “사교육”, “인구정책” 같은 생활권 headline이 아니다.

진짜 Stage 3는 아래가 같이 닫히는 순간이다.

```text
농기계:
농가소득 → 곡물가격 → 딜러 재고 → 북미/유럽 tractor 수요 → 수출 ASP → 재고/금융비용 → margin

식품·급식:
농수산물 가격 → 원가 전가 → 메뉴 가격 → 수요 탄력성 → 급식/외식 물량 → OP margin

프랜차이즈:
브랜드 화제성 → 실제 점포 매출 → royalty/franchise fee → 원재료비 → 가맹점 수익성 → 반복매출

배달·생활물류:
MAU/order → GMV → commission/take-rate → rider/labor cost → regulation → service continuity

폐기물·재활용:
폐기물 volume → gate fee → 처리단가 → recycling yield → CAPEX → regulatory contract → cash margin

육아·교육:
출생아 수 → 실제 enrolment/customer count → ARPU → 정책보조금 → 인건비 → retention

생활서비스:
반복계약 → churn → unit economics → 신뢰/품질 → 규제비용 → FCF
```

---

# 2. 대상 canonical archetype

```text
AGRI_EQUIPMENT_EXPORT_CYCLE_4C_WATCH
AGRI_FOOD_INPUT_COST_4C_WATCH
FRIED_CHICKEN_MEME_EVENT_PREMIUM
FOOD_DELIVERY_CONSOLIDATION_STAGE2
DELIVERY_LABOR_SERVICE_CONTINUITY_REFERENCE
WASTE_RECYCLING_INFRA_STAGE2
DEMOGRAPHIC_CHILDCARE_STAGE2
PRIVATE_EDUCATION_HAGWON_STAGE2_4C
```

---

# 3. deep sub-archetype

```text
농기계:
- Daedong / TYM
- North America tractor and dealer inventory cycle
- crop prices / farm income / equipment replacement cycle
- export channel and financing gate

식품 원가:
- CJ CheilJedang / Pulmuone / CJ Freshway / food-service basket
- rice, mandarin, agricultural/fishery price inflation
- cost pass-through and menu elasticity

치킨 meme:
- Kyochon F&B / Cherrybro / Neuromeka
- Jensen Huang Kkanbu Chicken event
- social-media rally disconnected from restaurant economics

배달앱:
- Naver / Uber / Baemin / Delivery Hero
- 8T won possible acquisition bid
- Korea order recovery, quick-commerce profitability
- regulation and integration gate

생활물류:
- CJ Logistics / Hanjin / Coupang read-through
- rare delivery-service halt for snap election
- rider/gig-worker labor continuity

폐기물:
- KJ Environment / EQT
- Insun ENT / KC Green / waste-management read-through
- plastic recycling vs actual recycling yield
- gate fee and cleanup-cost risk

육아:
- Agabang / Zero to Seven / child-care and infant-goods read-through
- fertility rebound but still structural population decline
- temporary echo-boomer effect vs durable childcare demand

사교육:
- MegaStudy / Chungdahm / education-service basket
- under-6 hagwon demand
- private-education spending vs demographic and regulation risk
```

---

# 4. 국장 신규 후보 case

## Case A — Daedong / TYM 농기계 export cycle

```text
symbols = 000490 / 002900
case_type = 4C-watch
archetype = AGRI_EQUIPMENT_EXPORT_CYCLE_4C_WATCH
```

### stage date

```text
Stage 1:
2024-05~2024-11
- global farm-equipment cycle turns down.
- Deere, CNH, AGCO all point to weaker farmer purchasing power, dealer inventory and lower crop income.

Stage 4C-watch:
2024-11-08
- CNH Industrial shares fell more than 10% premarket after profit miss and forecast cut.
- CNH cut 2024 adjusted EPS view from $1.30~$1.40 to $1.05~$1.15.
- agriculture segment sales expected down 22%~23%.
- tractor sales fell 20% in Europe/Middle East/Africa and combine sales fell 50% there.
- weak crop prices and high input costs delayed farmer purchases.

Stage 2 relief:
2026-02
- AGCO Q4 2025 beat and 2026 guidance imply possible farm-equipment bottoming.
- North America tractor sales still down 10% in 2025 and combine sales down 27%.
- AGCO +2.2%, Deere closed -0.3% after earlier boost.

Stage 3:
없음
- Korean tractor exporters need actual order recovery, dealer inventory normalization, export ASP and margin.
```

Daedong/TYM은 R12 농기계의 핵심 후보지만 이번 라운드에서는 Green을 주지 않는다. 글로벌 peer cycle이 아직 먼저다. CNH는 2024년 Q3 이후 profit outlook을 세 번째로 낮췄고, agriculture segment sales가 22~23% 줄 것으로 봤다. 이는 곡물가격·농가소득·dealer restocking이 농기계 수요의 본체라는 신호다. 2026년 AGCO가 일부 회복 신호를 냈지만 North America tractor sales는 2025년에 10%, combine sales는 27% 줄어 있었다. ([Reuters][1])

### 실제 가격경로 검증

```json
{
  "case_id": "r12_loop14_daedong_tym_agri_equipment_export_cycle",
  "symbols": "000490/002900",
  "stage4c_watch_date": "2024-11-08",
  "stage2_relief_date": "2026-02_AGCO_reference",
  "stage3_price": null,
  "price_data_source": "Reuters CNH / Barron's AGCO-Deere global farm-equipment anchors",
  "cnh_premarket_mae_pct": -10,
  "cnh_prior_eps_view_usd": "1.30-1.40",
  "cnh_revised_eps_view_usd": "1.05-1.15",
  "cnh_agriculture_sales_decline_2024_pct": "22-23",
  "cnh_emea_tractor_sales_decline_pct": -20,
  "cnh_emea_combine_sales_decline_pct": -50,
  "agco_2025_north_america_tractor_sales_decline_pct": -10,
  "agco_2025_combine_sales_decline_pct": -27,
  "agco_event_mfe_pct": 2.2,
  "deere_event_close_pct": -0.3,
  "daedong_tym_direct_ohlc": "price_data_unavailable_after_deep_search",
  "stage3_conditions": ["order recovery", "dealer inventory normalization", "export ASP", "financing cost", "gross margin"]
}
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = AGRI_EQUIPMENT_EXPORT_CYCLE_4C_WATCH
stage_failure_type = tractor_export_theme_not_green_without_farm_income_order_recovery
```

---

## Case B — 농수산물 가격·식품원가 basket

```text
symbols = 097950 / 017810 / 051500 / food_service_basket
company_scope = CJ CheilJedang / Pulmuone / CJ Freshway / food-service and processed-food basket
case_type = 4C-watch
archetype = AGRI_FOOD_INPUT_COST_4C_WATCH
```

### stage date

```text
Stage 1:
2025-12-01
- South Korea headline inflation stays above BOK target for a third straight month.
- food and service costs drive pressure.

Stage 4C-watch:
2025-12-01
- CPI +2.4% YoY.
- agricultural and fishery product price index +5.6% YoY.
- rice +18.6%.
- mandarins +26.5%.
- processed food prices remain high due weather disruptions and weak won.
- BOK keeps rate at 2.50%.

Stage 3:
없음
- food companies and food-service names need pass-through, demand retention and margin.
```

이 case는 R12 생활 식품·급식의 hard gate다. 농산물 가격이 오르면 식품주는 무조건 수혜가 아니다. 원재료 가격을 메뉴/제품 가격으로 전가하지 못하면 margin이 먼저 맞는다. Reuters는 2025년 11월 한국 CPI가 2.4%였고, 농수산물 가격지수가 5.6%, 쌀은 18.6%, 귤은 26.5% 상승했다고 보도했다. ([Reuters][2])

### 실제 가격경로 검증

```json
{
  "case_id": "r12_loop14_food_input_cost_inflation_basket",
  "symbols": "097950/017810/051500/food_service_basket",
  "stage4c_watch_date": "2025-12-01",
  "stage3_price": null,
  "price_data_source": "Reuters Korea inflation / food-cost anchor",
  "headline_cpi_yoy_pct": 2.4,
  "agri_fishery_price_index_yoy_pct": 5.6,
  "rice_price_yoy_pct": 18.6,
  "mandarin_price_yoy_pct": 26.5,
  "bok_policy_rate_pct": 2.50,
  "direct_company_ohlc": "price_data_unavailable_after_deep_search",
  "stage3_conditions": ["cost pass-through", "menu-price acceptance", "volume retention", "gross margin", "food-service contract repricing"]
}
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = AGRI_FOOD_INPUT_COST_4C_WATCH
stage_failure_type = input_cost_inflation_not_food_brand_green
```

---

## Case C — Kyochon / Cherrybro / Neuromeka “Jensen fried chicken” rally

```text
symbols = 339770 / 066360 / 348340
case_type = price_moved_without_evidence
archetype = FRIED_CHICKEN_MEME_EVENT_PREMIUM
```

### stage date

```text
Stage 1:
2025-10-31
- Nvidia CEO Jensen Huang visits Kkanbu Chicken with Samsung and Hyundai chiefs.
- photos/videos go viral during APEC-related South Korea visit.

Stage 4B:
2025-10-31
- Kkanbu Chicken is not listed.
- Kyochon F&B surged as much as 20%.
- Cherrybro surged daily limit +30%.
- Neuromeka also jumped; MarketWatch notes only Neuromeka retained gains by the close.
- Nvidia also announced South Korea AI-chip supply deals, but no equity stake buys in chicken names.

Stage 3:
없음
- meme/social-media virality is not franchise same-store sales, royalty, chicken input-cost margin or repeat demand.
```

이 case는 R12의 가장 좋은 `price_moved_without_evidence`다. Jensen Huang이 Kkanbu Chicken에서 치맥을 먹은 사진이 퍼지자 상장 peer인 Kyochon F&B, Cherrybro, Neuromeka가 급등했다. 하지만 Kkanbu는 상장사가 아니고, Kyochon이나 Cherrybro에 직접 매출·계약·원가 개선 evidence가 생긴 것도 아니다. FT와 MarketWatch 모두 이 rally를 AI hype가 생활서비스/치킨주까지 번진 speculative event로 설명했다. ([마켓워치][3])

### 실제 가격경로 검증

```json
{
  "case_id": "r12_loop14_fried_chicken_jensen_huang_meme_rally",
  "symbols": "339770/066360/348340",
  "stage4b_date": "2025-10-31",
  "stage3_price": null,
  "price_data_source": "MarketWatch / FT Jensen Huang fried-chicken rally anchors",
  "kyochon_event_mfe_pct": 20,
  "cherrybro_event_mfe_pct": 30,
  "neuromeka_retained_gains_by_close": true,
  "kkanbu_listed": false,
  "nvidia_korea_ai_chip_deals_context": true,
  "direct_revenue_link_confirmed": false,
  "same_store_sales_confirmed": false,
  "franchise_fee_margin_confirmed": false,
  "stage3_mfe_mae": "N/A_no_valid_stage3"
}
```

### alignment

```text
score_price_alignment = price_moved_without_evidence
rerating_result = FRIED_CHICKEN_MEME_EVENT_PREMIUM
stage_failure_type = celebrity_AI_visit_not_food_service_unit_economics
```

---

## Case D — Naver / Uber / Baemin food-delivery consolidation

```text
symbols = 035420 / Delivery Hero / Baemin read-through
case_type = success_candidate_stage2
archetype = FOOD_DELIVERY_CONSOLIDATION_STAGE2
```

### stage date

```text
Stage 1:
2025-11-13
- Delivery Hero says Korea orders returned to growth in October.
- Asia GMV had declined 3% in Q3, but Korea recovery supports Q4 turnaround.
- quick commerce achieves first quarterly profit.
- Delivery Hero shares +5% in early Frankfurt trade.

Stage 2:
2026-05-18
- Reuters reports Uber and Naver formed consortium to bid for Baemin.
- proposed bid up to 8T won / $5.34B.
- Uber/Naver consortium split: 80% / 20%.
- target: 100% stake in Baedal Minjok.
- Naver says it received teaser letter, no final decision.

Stage 3:
없음
- food-delivery M&A is not Green until approval, take-rate, rider cost, merchant churn, and integration economics close.
```

Baemin/Naver/Uber는 R12 생활서비스의 Stage 2 후보다. Korea food-delivery market의 회복 신호는 있었고, Baemin M&A는 scale catalyst다. 하지만 아직 final decision도 없고, food delivery는 GMV보다 take-rate, rider cost, merchant churn, regulation이 본체다. Reuters는 Uber/Naver consortium의 bid가 최대 8T won, Uber 80%/Naver 20% 구조라고 보도했고, Naver는 teaser letter를 받았지만 결정된 것은 없다고 밝혔다. ([Reuters][4])

### 실제 가격경로 검증

```json
{
  "case_id": "r12_loop14_naver_uber_baemin_food_delivery_consolidation",
  "symbols": "035420/DHER/Baemin_readthrough",
  "stage1_date": "2025-11-13",
  "stage2_date": "2026-05-18",
  "stage3_price": null,
  "price_data_source": "Reuters Delivery Hero Korea recovery and Uber/Naver Baemin bid anchors",
  "delivery_hero_q3_gmv_eur_bn": 12.2,
  "delivery_hero_q3_gmv_like_for_like_growth_pct": 7,
  "asia_gmv_q3_decline_pct": -3,
  "south_korea_orders_returned_to_growth": true,
  "quick_commerce_first_quarterly_profit": true,
  "delivery_hero_event_mfe_pct": 5,
  "baemin_bid_value_krw_trn": 8,
  "baemin_bid_value_usd_bn": 5.34,
  "uber_naver_consortium_split": "80/20",
  "final_decision_confirmed": false,
  "naver_direct_event_return": "price_data_unavailable_after_deep_search",
  "stage3_conditions": ["regulatory approval", "take-rate", "rider cost", "merchant churn", "integration economics"]
}
```

### alignment

```text
score_price_alignment = success_candidate_policy_deal_stage2
rerating_result = FOOD_DELIVERY_CONSOLIDATION_STAGE2
stage_failure_type = M&A_scale_not_take_rate_margin_green
```

---

## Case E — CJ Logistics / Hanjin / Coupang delivery-labor continuity

```text
symbols = 000120 / 002320 / CPNG read-through
case_type = service_continuity_reference
archetype = DELIVERY_LABOR_SERVICE_CONTINUITY_REFERENCE
```

### stage date

```text
Stage 1:
2025-06-03
- snap presidential election creates rare civic/labor event for delivery workers.

Stage 4C-reference:
2025-06-03
- Coupang pauses Rocket Delivery during the day for the first time since launch in 2014.
- pause window: 7 a.m. to 8 p.m.
- CJ Logistics, Hanjin and other delivery firms also join halt.
- reason: delivery workers allowed time to vote after pressure from unions and activists.
- couriers often classified as gig workers or self-employed, with weaker legal protections.

Stage 3:
N/A
- delivery-service Green requires labor continuity, unit economics, service reliability and regulation.
```

이 case는 R12 생활물류의 reference다. 배송 서비스는 “빠른 배송”이 아니라 노동·규제·운영 연속성으로 움직인다. Reuters는 Coupang의 Rocket Delivery가 2014년 출시 이후 처음으로 낮 시간대 중단됐고, CJ Logistics와 Hanjin도 동참했다고 보도했다. 이는 생활서비스 기업의 moat가 물류망만이 아니라 rider/courier labor model에 있다는 증거다. ([Reuters][5])

### 실제 가격경로 검증

```json
{
  "case_id": "r12_loop14_delivery_labor_service_continuity_reference",
  "symbols": "000120/002320/CPNG_readthrough",
  "stage4c_watch_date": "2025-06-03",
  "stage3_price": null,
  "price_data_source": "Reuters delivery-worker election pause anchor",
  "coupang_rocket_delivery_first_pause_since": 2014,
  "pause_window": "07:00-20:00",
  "participating_companies": ["Coupang", "CJ Logistics", "Hanjin Logistics"],
  "trigger": "snap presidential election voting access",
  "labor_model_risk": ["gig worker classification", "self-employed couriers", "union pressure", "service continuity"],
  "direct_listed_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_conditions": ["service reliability", "labor settlement durability", "unit economics", "regulatory compliance"]
}
```

### alignment

```text
score_price_alignment = thesis_break_reference
rerating_result = DELIVERY_LABOR_SERVICE_CONTINUITY_REFERENCE
stage_failure_type = delivery_speed_not_green_without_labor_operating_continuity
```

---

## Case F — EQT / KJ Environment waste-treatment platform

```text
symbols = 060150 / 009440 / waste_management_readthrough
company_scope = Insun ENT / KC Green Holdings / KJ Environment read-through
case_type = success_candidate_stage2 + 4C-watch
archetype = WASTE_RECYCLING_INFRA_STAGE2
```

### stage date

```text
Stage 1:
2024-08-16
- EQT agrees to acquire South Korean waste-treatment platform KJ Environment and affiliates.
- theme: plastic recycling, waste-to-energy, waste sorting.

Stage 2:
2024-08-16
- enterprise value exceeds 1T won / $733M.
- platform covers recyclable waste sorting, plastic recycling and waste-to-energy.
- Greater Seoul sites serve catchment areas covering more than 50% of South Korea population.
- transaction expected to close Q4 2024.

Stage 4C-watch:
2024-11-22
- Reuters reports South Korea claims 73% plastic recycling rate, but Greenpeace estimates actual recycling only 27%.
- plastic waste rose 31% from 2019 to 2022.
- Asan site had about 19,000 tonnes untreated ground plastic waste.
- cleanup expected to cost 2~3B won.
- recycling economics and regulation consistency remain hard gates.
```

폐기물/재활용은 R12의 structural candidate다. EQT가 KJ Environment platform을 1T won 이상 enterprise value로 인수한 것은 인프라 투자자들이 waste treatment를 반복현금흐름 asset으로 본다는 신호다. 하지만 Reuters는 한국의 “73% recycling rate”와 달리 실제 재활용률이 27%에 그칠 수 있고, untreated plastic waste가 쌓인 현장과 cleanup cost 문제를 보도했다. 즉 waste management Green은 volume과 gate fee뿐 아니라 실제 recycling yield와 처리경제성이 필요하다. ([Reuters][6])

### 실제 가격경로 검증

```json
{
  "case_id": "r12_loop14_waste_recycling_infra_stage2",
  "symbols": "060150/009440/waste_management_readthrough",
  "stage2_date": "2024-08-16",
  "stage4c_watch_date": "2024-11-22",
  "stage3_price": null,
  "price_data_source": "Reuters EQT KJ Environment acquisition and South Korea plastic-waste anchors",
  "kj_environment_platform_ev_krw_trn_min": 1.0,
  "kj_environment_platform_ev_usd_mn": 733,
  "catchment_population_coverage_pct": 50,
  "business_lines": ["recyclable waste sorting", "plastic recycling", "waste-to-energy"],
  "official_plastic_recycling_claim_pct": 73,
  "greenpeace_actual_recycling_estimate_pct": 27,
  "plastic_waste_growth_2019_2022_pct": 31,
  "untreated_plastic_waste_tonnes": 19000,
  "cleanup_cost_krw_bn": "2-3",
  "direct_listed_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_conditions": ["gate fee", "recycling yield", "utilization", "regulatory contract", "cleanup liability control"]
}
```

### alignment

```text
score_price_alignment = success_candidate_4C_watch
rerating_result = WASTE_RECYCLING_INFRA_STAGE2
stage_failure_type = infrastructure_EV_not_recycling_yield_cash_margin_green
```

---

## Case G — 출산율 반등 / 육아·아동서비스 basket

```text
symbols = 013990 / 159910 / childcare_infant_goods_basket
company_scope = Agabang / Zero to Seven / childcare and infant-goods read-through
case_type = success_candidate_stage2
archetype = DEMOGRAPHIC_CHILDCARE_STAGE2
```

### stage date

```text
Stage 1:
2025-02-26
- South Korea fertility rate rises for first time in nine years.
- 2024 fertility rate rises to 0.75 from 0.72.
- births rise 3.6% to 238,300.

Stage 2:
2026-02-25
- fertility rate rises again to 0.80 in 2025.
- births rise 6.8% to 254,500.
- marriages rise 8.1%.
- experts caution echo-boomer cohort effect may fade after 2027.
- deaths still outpace births by 108,900.

Stage 3:
없음
- childcare/infant-goods Green requires actual sales, enrolment, ARPU, policy subsidies and margin.
```

출산율 반등은 R12의 Stage 2 demographic catalyst다. Reuters는 2024년 출산율이 0.75로 9년 만에 반등했고, 2025년에는 0.80으로 다시 올랐다고 보도했다. 하지만 이건 아동복·육아용품·어린이집·교육서비스의 자동 Green이 아니다. 2025년에도 사망자가 출생아보다 108,900명 많았고, echo-boomer 효과가 2027년 이후 약해질 수 있다. ([Reuters][7])

### 실제 가격경로 검증

```json
{
  "case_id": "r12_loop14_birthrate_childcare_infant_goods_stage2",
  "symbols": "013990/159910/childcare_infant_goods_basket",
  "stage1_date": "2025-02-26",
  "stage2_date": "2026-02-25",
  "stage3_price": null,
  "price_data_source": "Reuters birthrate rebound anchors",
  "fertility_rate_2023": 0.72,
  "fertility_rate_2024": 0.75,
  "fertility_rate_2025": 0.80,
  "births_2024": 238300,
  "births_2024_growth_pct": 3.6,
  "births_2025": 254500,
  "births_2025_growth_pct": 6.8,
  "marriages_2025_growth_pct": 8.1,
  "deaths_exceeded_births_2025": 108900,
  "echo_boomer_effect_watch": true,
  "direct_listed_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_conditions": ["actual sales", "customer count", "enrolment", "ARPU", "subsidy capture", "margin"]
}
```

### alignment

```text
score_price_alignment = success_candidate_demographic_stage2
rerating_result = DEMOGRAPHIC_CHILDCARE_STAGE2
stage_failure_type = birthrate_rebound_not_childcare_revenue_green
```

---

## Case H — 사교육 / hagwon life-service demand

```text
symbols = 072870 / 096240 / education_service_basket
company_scope = MegaStudy Education / Chungdahm / private-education basket
case_type = success_candidate_stage2 + demographic_policy_4C_watch
archetype = PRIVATE_EDUCATION_HAGWON_STAGE2_4C
```

### stage date

```text
Stage 1:
2025-03-16
- South Korean under-6 private-education demand becomes visible in government survey.

Stage 2:
2025-03-16
- 47.6% of under-6 children attend hagwon/cram schools.
- 25% of under-2 children also attend.
- average monthly tuition for preschoolers: 332,000 won.
- average private-class time: 5.6 hours/week.
- English kindergartens in wealthy Seoul districts average 1.5M won/month.
- record private education spending burden remains.

Stage 4C-watch:
- high private-education spending contributes to child-rearing cost, household burden and low fertility.
- demographic base is still structurally shrinking.
- policy/regulation risk remains.

Stage 3:
없음
- education-service Green requires enrolment, pricing power, retention, online/offline margin and regulatory durability.
```

사교육은 R12 life-service의 특이한 case다. Demand는 강하지만 사회적 비용이 높다. FT는 under-6 아동의 47.6%가 hagwon에 다니고, under-2도 25%가 다닌다고 보도했다. 평균 월 tuition은 332,000 won이고, 강남권 영어유치원은 월 1.5M won 수준이다. 하지만 이 수요는 Green이면서 동시에 4C다. 사교육 부담이 출산율과 가계소비를 누르는 구조이기 때문이다. ([Financial Times][8])

### 실제 가격경로 검증

```json
{
  "case_id": "r12_loop14_private_education_hagwon_demand_stage2",
  "symbols": "072870/096240/education_service_basket",
  "stage2_date": "2025-03-16",
  "stage4c_watch_date": "2025-03-16",
  "stage3_price": null,
  "price_data_source": "FT under-6 hagwon survey anchor",
  "under6_hagwon_enrolment_pct": 47.6,
  "under2_hagwon_enrolment_pct": 25,
  "preschool_monthly_tuition_avg_krw": 332000,
  "private_class_hours_per_week_avg": 5.6,
  "english_kindergarten_monthly_tuition_avg_krw": 1500000,
  "direct_listed_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_conditions": ["enrolment growth", "pricing power", "retention", "teacher cost control", "online margin", "regulatory durability"]
}
```

### alignment

```text
score_price_alignment = success_candidate_4C_watch
rerating_result = PRIVATE_EDUCATION_HAGWON_STAGE2
stage_failure_type = high_private_education_demand_not_green_if_demographic_policy_burden
```

---

# 5. 이번 R12 case별 stage date 요약

| case                        | Stage 1                      | Stage 2                    | Stage 3 | Stage 4B                  | Stage 4C                        |
| --------------------------- | ---------------------------- | -------------------------- | ------- | ------------------------- | ------------------------------- |
| Daedong/TYM                 | 2024 farm-equipment downturn | 2026 AGCO relief reference | N/A     | recovery hope             | global ag equipment slump       |
| Food input cost basket      | 2025-12 inflation            | N/A                        | N/A     | N/A                       | rice/mandarin/agri-fishery cost |
| Kyochon/Cherrybro/Neuromeka | 2025-10-31 viral event       | N/A                        | N/A     | meme rally                | no direct economics             |
| Naver/Uber/Baemin           | 2025 Korea order recovery    | 2026-05 bid report         | N/A     | M&A scale premium         | regulation/integration          |
| Delivery labor              | 2025 election                | service halt reference     | N/A     | N/A                       | labor continuity                |
| Waste/recycling             | 2024 EQT deal                | 1T won platform            | N/A     | infra premium             | recycling yield/cleanup cost    |
| Childcare/birthrate         | 2025 rebound                 | 2026 second rebound        | N/A     | baby-stock theme          | echo-boomer/structural decline  |
| Hagwon/private education    | 2025 survey                  | strong demand              | N/A     | education-service premium | demographic/policy burden       |

---

# 6. 실제 가격경로 검증 총괄

| case                        |                                           가격·사업 anchor | 해석                               | 판정                           |
| --------------------------- | -----------------------------------------------------: | -------------------------------- | ---------------------------- |
| Daedong/TYM                 |            CNH -10% premarket, AGCO +2.2%, Deere -0.3% | global farm-equipment cycle gate | 4C-watch                     |
| Food input cost             |       agri/fishery +5.6%, rice +18.6%, mandarin +26.5% | food margin gate                 | 4C-watch                     |
| Kyochon/Cherrybro/Neuromeka |                           Kyochon +20%, Cherrybro +30% | meme event, no economics         | price_moved_without_evidence |
| Baemin/Naver/Uber           |                 Delivery Hero +5%, possible 8T won bid | consolidation Stage 2            | success_candidate            |
| Delivery labor              |                 Rocket Delivery first pause since 2014 | service continuity reference     | thesis_break_reference       |
| Waste/recycling             | EQT platform EV >1T won, actual recycling 27% estimate | infra Stage 2 + yield gate       | success_candidate            |
| Childcare/birthrate         |                 fertility 0.72→0.75→0.80, births +6.8% | demographic Stage 2              | success_candidate            |
| Hagwon                      |                  under-6 47.6%, tuition 332k won/month | demand strong, social/policy 4C  | success_candidate_4C         |

---

# 7. score-price alignment 판정

```text
aligned:
- 없음. R12는 대부분 reported event anchors, macro/service demand anchors, 또는 meme/event premium.

structural_success_candidate:
- Waste/recycling platform, if gate fee, recycling yield and margin confirm.
- Food delivery consolidation, if regulatory approval and take-rate economics confirm.
- Childcare/education services, if demographic rebound converts into paying customer growth.

success_candidate:
- Naver/Uber/Baemin.
- Waste/recycling platform.
- Childcare/birthrate basket.
- Hagwon/private education demand.

failed_rerating:
- Daedong/TYM if farm-equipment export recovery is scored before global demand/dealer inventory turns.
- Food-service basket if input-cost inflation is scored as pricing power without margin proof.

overheat / 4B:
- Kyochon/Cherrybro/Neuromeka Jensen rally.
- Baemin M&A scale premium before approval/economics.
- Childcare baby-stock theme on temporary birth rebound.

price_moved_without_evidence:
- Fried-chicken stocks after Jensen Huang/Kkanbu viral event.
- Baby/education stocks if traded only on fertility headline.
- Waste/recycling names if traded only on EQT EV without listed cashflow bridge.

evidence_good_but_price_failed:
- Agriculture equipment recovery references, if Korean names do not get order/price confirmation.
- Food input cost pass-through, if volume drops after price increases.

thesis_break_watch:
- Global farm-equipment downturn.
- Agricultural/fishery food-cost inflation.
- Delivery labor/service continuity.
- Recycling-yield and cleanup-liability risk.
- Hagwon demographic/policy burden.

hard_4C_confirmed:
- direct KRX hard 4C: false.
- sector hard reference: delivery labor continuity, recycling cleanup liability, food-cost inflation.
```

---

# 8. 점수비중 교정

## 올릴 축

```text
farm_income_equipment_order_visibility +5
dealer_inventory_normalization +5
food_input_cost_pass_through +5
same_store_sales_franchise_fee +5
delivery_take_rate_unit_economics +5
labor_service_continuity +5
recycling_yield_gate_fee_margin +5
childcare_actual_customer_growth +4
education_enrolment_retention +4
policy_regulatory_durability +5
```

### 왜 올리나

Daedong/TYM은 농기계 수출 테마가 글로벌 farm-equipment cycle과 dealer inventory를 피할 수 없음을 보여준다. 식품/급식주는 농산물 가격 상승이 margin 악재일 수도 있다. 치킨 meme rally는 가격이 evidence 없이 움직인 전형적 4B다. Baemin/Naver/Uber는 deal scale보다 take-rate과 rider cost가 중요하다. 폐기물은 EV가 커도 recycling yield와 cleanup liability가 닫혀야 한다. 출산율과 hagwon demand는 강한 생활서비스 signal이지만 실제 paying-customer growth와 regulation이 필요하다.

## 내릴 축

```text
celebrity_viral_event_only -5
resource_or_food_theme_without_margin -5
farm_equipment_recovery_headline_only -5
delivery_MA_scale_without_take_rate -5
birthrate_headline_only -5
hagwon_demand_without_demographic_base -4
waste_infra_EV_without_recycling_yield -5
input_cost_inflation_as_pricing_power -5
```

---

# 9. Green gate 강화 조건

```text
R12 Stage 3-Green 필수:
1. 농기계는 order backlog, dealer inventory, export ASP, financing cost 확인.
2. 식품/급식은 원가 전가, volume retention, contract repricing, gross margin 확인.
3. 프랜차이즈는 same-store sales, franchise fee, raw-material spread, 가맹점 수익성 확인.
4. 배달앱은 GMV보다 take-rate, rider cost, merchant churn, regulatory approval 확인.
5. 생활물류는 service continuity, labor settlement, unit economics 확인.
6. 폐기물/재활용은 gate fee, utilization, recycling yield, cleanup liability 확인.
7. 출산·육아는 fertility headline보다 실제 customer count, ARPU, subsidy capture 확인.
8. 사교육은 enrolment, retention, pricing power, teacher cost, regulatory durability 확인.
9. price path가 evidence 이후 따라옴.
```

---

# 10. 4B 조기감지 조건

```text
4B-watch:
- 유명인/CEO 방문 사진만으로 생활서비스주 급등.
- 출산율 반등 headline만으로 baby/education stocks 급등.
- M&A bid headline으로 배달앱/플랫폼주 급등.
- 폐기물 infra EV headline으로 listed read-through 과열.
- 농기계 recovery hope가 global order data 전 선반영.
- 식품가격 상승을 자동 pricing power로 해석.
```

---

# 11. 4C hard gate 조건

```text
Hard 4C / strong watch:
- 농가소득 하락과 dealer inventory overhang.
- 원재료 가격 상승이 가격전가 실패로 margin 훼손.
- labor action / election / regulation causing delivery-service interruption.
- food-delivery regulation blocking merger or take-rate.
- recycling economics failure / cleanup liability.
- demographic rebound proves temporary after echo-boomer cohort.
- hagwon regulation or child-population decline offsets high ARPU.
- franchisee profitability collapse despite brand virality.
```

이번 R12 Loop 14에서는 **직접 KRX hard 4C는 확정하지 않는다.** 대신 `fried_chicken_meme_event`, `agri_food_input_cost`, `delivery_labor_continuity`, `waste_recycling_cleanup_liability`, `birthrate_headline_only`를 strong watch/reference로 둔다.

---

# 12. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 13. 레포 반영용 patch-ready 출력

## docs/round/round_222.md 요약

```md
# R12 Loop 14. Agriculture / Life Services / Misc Price Validation

이번 라운드는 R12 Loop 14 price-validation 라운드다.

핵심 결론:
- Daedong/TYM agriculture-equipment read-through is 4C-watch. CNH fell more than 10% premarket after profit miss and forecast cut; agriculture sales expected -22%~-23%, EMEA tractor sales -20%, EMEA combine sales -50%. AGCO later gave 2026 recovery signals, but North America tractor sales were still -10% in 2025 and combine sales -27%.
- Food input-cost basket is 4C-watch. Korea CPI +2.4% YoY in Nov. 2025; agricultural/fishery prices +5.6%, rice +18.6%, mandarins +26.5%. Food companies need pass-through and volume retention.
- Kyochon/Cherrybro/Neuromeka Jensen fried-chicken rally is price_moved_without_evidence. Kyochon +20%, Cherrybro +30%; Kkanbu Chicken was not listed and direct economics were absent.
- Naver/Uber/Baemin food-delivery consolidation is Stage 2. Delivery Hero Korea orders returned to growth; Uber/Naver consortium reportedly bid up to 8T won for Baemin, 80/20 split. Regulatory approval, take-rate and rider-cost economics required.
- Delivery labor continuity is R12 service reference. Coupang paused Rocket Delivery during election day for the first time since 2014, joined by CJ Logistics and Hanjin. Labor continuity is part of delivery-service moat.
- Waste/recycling infrastructure is Stage 2 plus 4C-watch. EQT’s KJ Environment platform EV exceeds 1T won and covers more than 50% of Korea’s population catchment; but actual plastic recycling may be 27% vs official 73%, with untreated waste and cleanup liabilities.
- Birthrate/childcare basket is demographic Stage 2. Korea fertility rose from 0.72 to 0.75 to 0.80, births +6.8% in 2025, but deaths still exceeded births and echo-boomer effect may fade.
- Hagwon/private education is demand Stage 2 plus social-policy 4C. 47.6% of under-6 children and 25% of under-2 children attend hagwons; average monthly tuition 332,000 won, English kindergartens about 1.5M won/month in wealthy Seoul districts.
```

## docs/checkpoints/checkpoint_28a_round222_r12_loop14.md 요약

```md
# Checkpoint 28A Round 222 R12 Loop 14 Agriculture Life Services Misc Price Validation

## 반영 내용
- R12 Loop 14 price-validation 라운드를 추가했다.
- Daedong/TYM, food input-cost basket, Kyochon/Cherrybro/Neuromeka, Naver/Uber/Baemin, CJ Logistics/Hanjin/Coupang delivery labor, waste/recycling platform, childcare/birthrate basket, hagwon/private education basket을 비교했다.
- Reuters / FT / MarketWatch / AP / Barron’s anchors로 가능한 event MFE/MAE, deal value, food inflation, fertility, service-continuity and waste-liability metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- farm-income/order visibility, dealer inventory normalization, food input-cost pass-through, same-store sales/franchise fee, delivery take-rate economics, labor service continuity, recycling yield/gate-fee margin, childcare customer growth, education enrolment/retention, regulatory durability 가중치 강화.
- celebrity viral event-only, birthrate headline-only, delivery M&A scale without take-rate, waste infra EV without recycling yield, input-cost inflation as pricing power, farm-equipment recovery headline-only 감점 강화.
```

## data/e2r_case_library/cases_r12_loop14_round222.jsonl 초안

```jsonl
{"case_id":"r12_loop14_daedong_tym_agri_equipment_export_cycle","symbol":"000490/002900","company_name":"Daedong / TYM","case_type":"4c_watch","primary_archetype":"AGRI_EQUIPMENT_EXPORT_CYCLE_4C_WATCH","stage4c_date":"2024-11-08","stage2_date":"2026-02_AGCO_reference","price_validation":{"price_data_source":"Reuters CNH / Barron's AGCO-Deere global farm-equipment anchors","stage3_price":null,"cnh_premarket_mae_pct":-10,"cnh_prior_eps_view_usd":"1.30-1.40","cnh_revised_eps_view_usd":"1.05-1.15","cnh_agriculture_sales_decline_2024_pct":"22-23","cnh_emea_tractor_sales_decline_pct":-20,"cnh_emea_combine_sales_decline_pct":-50,"agco_2025_north_america_tractor_sales_decline_pct":-10,"agco_2025_combine_sales_decline_pct":-27,"agco_event_mfe_pct":2.2,"deere_event_close_pct":-0.3,"daedong_tym_direct_ohlc":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"AGRI_EQUIPMENT_EXPORT_CYCLE_4C_WATCH","notes":"Korean tractor export thesis needs farm income, dealer inventory, orders, export ASP and margin."}
{"case_id":"r12_loop14_food_input_cost_inflation_basket","symbol":"097950/017810/051500/food_service_basket","company_name":"CJ CheilJedang / Pulmuone / CJ Freshway / food-service basket","case_type":"4c_watch","primary_archetype":"AGRI_FOOD_INPUT_COST_4C_WATCH","stage4c_date":"2025-12-01","price_validation":{"price_data_source":"Reuters Korea inflation / food-cost anchor","stage3_price":null,"headline_cpi_yoy_pct":2.4,"agri_fishery_price_index_yoy_pct":5.6,"rice_price_yoy_pct":18.6,"mandarin_price_yoy_pct":26.5,"bok_policy_rate_pct":2.50,"direct_company_ohlc":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"AGRI_FOOD_INPUT_COST_4C_WATCH","notes":"Food input inflation is not pricing power unless pass-through, volume retention and margin confirm."}
{"case_id":"r12_loop14_fried_chicken_jensen_huang_meme_rally","symbol":"339770/066360/348340","company_name":"Kyochon F&B / Cherrybro / Neuromeka","case_type":"price_moved_without_evidence","primary_archetype":"FRIED_CHICKEN_MEME_EVENT_PREMIUM","stage4b_date":"2025-10-31","price_validation":{"price_data_source":"MarketWatch / FT Jensen Huang fried-chicken rally anchors","stage3_price":null,"kyochon_event_mfe_pct":20,"cherrybro_event_mfe_pct":30,"neuromeka_retained_gains_by_close":true,"kkanbu_listed":false,"nvidia_korea_ai_chip_deals_context":true,"direct_revenue_link_confirmed":false,"same_store_sales_confirmed":false,"franchise_fee_margin_confirmed":false},"score_price_alignment":"price_moved_without_evidence","rerating_result":"FRIED_CHICKEN_MEME_EVENT_PREMIUM","notes":"Celebrity/AI visit moved stocks without same-store sales, royalty, or input-cost margin evidence."}
{"case_id":"r12_loop14_naver_uber_baemin_food_delivery_consolidation","symbol":"035420/DHER/Baemin_readthrough","company_name":"Naver / Uber / Baemin / Delivery Hero","case_type":"success_candidate_stage2","primary_archetype":"FOOD_DELIVERY_CONSOLIDATION_STAGE2","stage1_date":"2025-11-13","stage2_date":"2026-05-18","price_validation":{"price_data_source":"Reuters Delivery Hero Korea recovery and Uber/Naver Baemin bid anchors","stage3_price":null,"delivery_hero_q3_gmv_eur_bn":12.2,"delivery_hero_q3_gmv_like_for_like_growth_pct":7,"asia_gmv_q3_decline_pct":-3,"south_korea_orders_returned_to_growth":true,"quick_commerce_first_quarterly_profit":true,"delivery_hero_event_mfe_pct":5,"baemin_bid_value_krw_trn":8,"baemin_bid_value_usd_bn":5.34,"uber_naver_consortium_split":"80/20","final_decision_confirmed":false,"naver_direct_event_return":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_policy_deal_stage2","rerating_result":"FOOD_DELIVERY_CONSOLIDATION_STAGE2","notes":"Food-delivery M&A scale needs approval, take-rate, rider cost, merchant churn and integration economics."}
{"case_id":"r12_loop14_delivery_labor_service_continuity_reference","symbol":"000120/002320/CPNG_readthrough","company_name":"CJ Logistics / Hanjin / Coupang read-through","case_type":"service_continuity_reference","primary_archetype":"DELIVERY_LABOR_SERVICE_CONTINUITY_REFERENCE","stage4c_date":"2025-06-03","price_validation":{"price_data_source":"Reuters delivery-worker election pause anchor","stage3_price":null,"coupang_rocket_delivery_first_pause_since":2014,"pause_window":"07:00-20:00","participating_companies":["Coupang","CJ Logistics","Hanjin Logistics"],"trigger":"snap presidential election voting access","labor_model_risk":["gig worker classification","self-employed couriers","union pressure","service continuity"],"direct_listed_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_reference","rerating_result":"DELIVERY_LABOR_SERVICE_CONTINUITY_REFERENCE","notes":"Delivery speed moat needs labor continuity, service reliability and unit economics."}
{"case_id":"r12_loop14_waste_recycling_infra_stage2","symbol":"060150/009440/waste_management_readthrough","company_name":"Insun ENT / KC Green / KJ Environment read-through","case_type":"success_candidate_4c_watch","primary_archetype":"WASTE_RECYCLING_INFRA_STAGE2","stage2_date":"2024-08-16","stage4c_date":"2024-11-22_watch","price_validation":{"price_data_source":"Reuters EQT KJ Environment acquisition and South Korea plastic-waste anchors","stage3_price":null,"kj_environment_platform_ev_krw_trn_min":1.0,"kj_environment_platform_ev_usd_mn":733,"catchment_population_coverage_pct":50,"business_lines":["recyclable waste sorting","plastic recycling","waste-to-energy"],"official_plastic_recycling_claim_pct":73,"greenpeace_actual_recycling_estimate_pct":27,"plastic_waste_growth_2019_2022_pct":31,"untreated_plastic_waste_tonnes":19000,"cleanup_cost_krw_bn":"2-3","direct_listed_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_4C_watch","rerating_result":"WASTE_RECYCLING_INFRA_STAGE2","notes":"Waste infra EV is Stage 2; recycling yield, gate fee, utilization and cleanup-liability control are Green gates."}
{"case_id":"r12_loop14_birthrate_childcare_infant_goods_stage2","symbol":"013990/159910/childcare_infant_goods_basket","company_name":"Agabang / Zero to Seven / childcare and infant-goods read-through","case_type":"success_candidate_demographic_stage2","primary_archetype":"DEMOGRAPHIC_CHILDCARE_STAGE2","stage1_date":"2025-02-26","stage2_date":"2026-02-25","price_validation":{"price_data_source":"Reuters birthrate rebound anchors","stage3_price":null,"fertility_rate_2023":0.72,"fertility_rate_2024":0.75,"fertility_rate_2025":0.80,"births_2024":238300,"births_2024_growth_pct":3.6,"births_2025":254500,"births_2025_growth_pct":6.8,"marriages_2025_growth_pct":8.1,"deaths_exceeded_births_2025":108900,"echo_boomer_effect_watch":true,"direct_listed_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_demographic_stage2","rerating_result":"DEMOGRAPHIC_CHILDCARE_STAGE2","notes":"Birthrate rebound is Stage 2; actual sales, customer count, ARPU, subsidy capture and margin required."}
{"case_id":"r12_loop14_private_education_hagwon_demand_stage2","symbol":"072870/096240/education_service_basket","company_name":"MegaStudy Education / Chungdahm / private-education basket","case_type":"success_candidate_4c_watch","primary_archetype":"PRIVATE_EDUCATION_HAGWON_STAGE2_4C","stage2_date":"2025-03-16","stage4c_date":"2025-03-16_watch","price_validation":{"price_data_source":"FT under-6 hagwon survey anchor","stage3_price":null,"under6_hagwon_enrolment_pct":47.6,"under2_hagwon_enrolment_pct":25,"preschool_monthly_tuition_avg_krw":332000,"private_class_hours_per_week_avg":5.6,"english_kindergarten_monthly_tuition_avg_krw":1500000,"direct_listed_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_4C_watch","rerating_result":"PRIVATE_EDUCATION_HAGWON_STAGE2","notes":"Private education demand is strong but demographic burden and policy/regulatory risk remain."}
```

## data/sector_taxonomy/score_weight_profiles_round222_r12_loop14_v1.csv 초안

```csv
archetype,farm_income_order_visibility,dealer_inventory_normalization,food_input_cost_pass_through,same_store_sales_franchise_fee,delivery_take_rate_unit_economics,labor_service_continuity,recycling_yield_gate_fee_margin,childcare_actual_customer_growth,education_enrolment_retention,policy_regulatory_durability,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
AGRI_EQUIPMENT_EXPORT_CYCLE_4C_WATCH,+5,+5,+1,+0,+0,+1,+0,+0,+0,+3,0,+4,+4,Daedong/TYM require farm income, dealer inventory, export orders and ASP/margin confirmation.
AGRI_FOOD_INPUT_COST_4C_WATCH,+1,+0,+5,+2,+0,+0,+0,+0,+0,+3,0,+4,+4,Food inflation can be margin-negative unless pass-through and volume retention confirm.
FRIED_CHICKEN_MEME_EVENT_PREMIUM,+0,+0,+2,+5,+0,+0,+0,+0,+0,+1,-5,+5,+3,Jensen fried-chicken rally is meme premium without same-store sales or franchise economics.
FOOD_DELIVERY_CONSOLIDATION_STAGE2,+0,+0,+1,+0,+5,+5,+0,+0,+0,+5,-5,+5,+4,Baemin M&A needs approval, take-rate, rider cost, merchant churn and integration economics.
DELIVERY_LABOR_SERVICE_CONTINUITY_REFERENCE,+0,+0,+0,+0,+5,+5,+0,+0,+0,+5,0,+4,+4,Delivery service moat depends on labor continuity and service reliability.
WASTE_RECYCLING_INFRA_STAGE2,+0,+0,+0,+0,+0,+2,+5,+0,+0,+5,-5,+4,+4,Waste infra needs recycling yield, gate fee, utilization and cleanup liability control.
DEMOGRAPHIC_CHILDCARE_STAGE2,+0,+0,+0,+0,+0,+1,+0,+5,+3,+5,-5,+5,+3,Birthrate rebound is Stage 2 until customer growth and ARPU/margin confirm.
PRIVATE_EDUCATION_HAGWON_STAGE2_4C,+0,+0,+0,+0,+0,+1,+0,+2,+5,+5,-4,+4,+3,Hagwon demand is strong but demographic and regulatory burden remain.
```

---

# 이번 R12 Loop 14 결론

```text
1. Daedong/TYM은 농기계 export-cycle 4C-watch다.
   농기계는 테마가 아니라 농가소득, dealer inventory, export order, ASP/margin으로 닫혀야 한다.

2. 식품·급식 basket은 input-cost 4C-watch다.
   쌀 +18.6%, 귤 +26.5% 같은 원가 상승은 가격전가 전에는 margin 악재다.

3. Kyochon/Cherrybro/Neuromeka는 price_moved_without_evidence다.
   Jensen Huang의 치킨 방문은 주가를 움직였지만 상장사 매출 evidence는 없었다.

4. Naver/Uber/Baemin은 food-delivery consolidation Stage 2다.
   8T won bid headline보다 approval, take-rate, rider cost, merchant churn이 중요하다.

5. CJ Logistics/Hanjin/Coupang delivery pause는 service-continuity reference다.
   생활물류 moat는 빠른 배송만이 아니라 노동·규제·운영 연속성이다.

6. Waste/recycling은 structural candidate지만 4C-watch다.
   폐기물 처리 EV는 강하지만 실제 recycling yield와 cleanup liability가 Green gate다.

7. 출산율 반등은 childcare Stage 2다.
   fertility 0.80 회복은 좋지만 실제 매출·고객수·ARPU·보조금 capture가 필요하다.

8. Hagwon/private education은 demand Stage 2이면서 social 4C다.
   수요는 강하지만 인구감소·정책규제·가계부담이 같이 따라온다.
```

한 문장으로 압축하면:

> **R12에서 진짜 Stage 3는 “농업·치킨·배달·폐기물·육아·사교육 headline이 좋다”가 아니라, order visibility·원가전가·same-store sales·take-rate·labor continuity·recycling yield·customer growth·retention이 실제 숫자로 닫히는 순간이다.**

* [Reuters](https://www.reuters.com/business/cnh-industrial-shares-fall-after-third-quarter-profit-miss-forecast-cut-2024-11-08/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/south-korea-nov-headline-inflation-24-yy-expected-2025-12-01/?utm_source=chatgpt.com)
* [마켓워치](https://www.marketwatch.com/story/jensen-huang-spreads-nvidia-magic-to-fried-chicken-stocks-06b49648?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/uber-naver-team-up-baemin-takeover-seoul-economic-daily-2026-05-18/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/retail-consumer/south-korean-delivery-workers-allowed-rare-pause-services-vote-snap-election-2025-06-03/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/markets/deals/eqt-strikes-deal-acquire-south-korean-waste-treatment-platform-2024-08-16/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/south-koreas-policy-push-springs-life-worlds-lowest-birthrate-rises-2025-02-26/?utm_source=chatgpt.com)
* [Financial Times](https://www.ft.com/content/4babaa33-5ad8-4290-b7d3-835165ed8091?utm_source=chatgpt.com)

[1]: https://www.reuters.com/business/cnh-industrial-shares-fall-after-third-quarter-profit-miss-forecast-cut-2024-11-08/?utm_source=chatgpt.com "CNH Industrial shares fall after third-quarter profit miss, forecast cut"
[2]: https://www.reuters.com/world/asia-pacific/south-korea-nov-headline-inflation-24-yy-expected-2025-12-01/?utm_source=chatgpt.com "South Korea headline inflation at 2.4% y/y, bolstering case for rate pause"
[3]: https://www.marketwatch.com/story/jensen-huang-spreads-nvidia-magic-to-fried-chicken-stocks-06b49648?utm_source=chatgpt.com "Jensen Huang spreads Nvidia magic to fried-chicken stocks"
[4]: https://www.reuters.com/world/china/delivery-hero-expects-pick-up-growth-fourth-quarter-2025-11-13/?utm_source=chatgpt.com "Delivery Hero expects Asia recovery to boost fourth-quarter growth"
[5]: https://www.reuters.com/business/retail-consumer/south-korean-delivery-workers-allowed-rare-pause-services-vote-snap-election-2025-06-03/?utm_source=chatgpt.com "South Korean delivery workers allowed rare pause in services to vote in snap election"
[6]: https://www.reuters.com/markets/deals/eqt-strikes-deal-acquire-south-korean-waste-treatment-platform-2024-08-16/?utm_source=chatgpt.com "EQT strikes deal to acquire South Korean waste treatment platform"
[7]: https://www.reuters.com/world/asia-pacific/south-koreas-policy-push-springs-life-worlds-lowest-birthrate-rises-2025-02-26/?utm_source=chatgpt.com "South Korea's policy push springs to life as world's lowest birthrate rises"
[8]: https://www.ft.com/content/4babaa33-5ad8-4290-b7d3-835165ed8091?utm_source=chatgpt.com "South Korea's academic race pushes half of under-6s into 'cram' schools"

순서상 이번은 **R12 Loop 13 — 농업·생활서비스·기타 가격경로 검증 라운드**다.

```text
round = R12 Loop 13
round_id = round_209
large_sector = AGRICULTURE_LIFE_SERVICE_OTHER
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true_for_life_service_trust_reference
direct_listed_hard_4c_confirmed = false
next_round = R13 Loop 13
```

이번 R12는 국장 중심으로 보되, 이 섹터 특성상 **비상장 생활서비스·폐기물·농식품 정책 reference**가 많다. 그래서 상장 직접 case는 **CJ Logistics, DN Solutions, Daedong/TYM, CJ·Daesang·Pulmuone/식품 basket, Harim/사료·계육 basket, Naver/E-Mart/CJ Logistics read-through**로 잡고, 비상장·해외상장 reference는 **Coupang, KJ Environment/EQT, food-waste RFID system**을 sector hard/reference로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R12 = 농업·생활서비스·기타
```

R12에서 진짜 Stage 3는 “생활필수재다”, “농산물 가격이 오른다”, “저출산 반등이다”, “폐기물은 구조적이다”, “물류 제휴다”, “IPO 대형주다” 같은 말이 아니다.

R12의 Stage 3는 아래처럼 닫혀야 한다.

```text
농업/식품:
실제 물량 → 원가 전가 → 재고/폐기 관리 → gross margin → cash conversion

사료/축산:
곡물·질병 shock → 구매단가 → 판가 전가 → 출하량 → 마진

생활서비스/물류:
계약 체결 → 물동량 → 단가 → 자동화/인건비 → operating leverage → FCF

폐기물/환경:
처리량 → tipping fee → utilization → 규제허가 → capex 회수

교육/돌봄:
정책/출생률 headline → 실제 enrolment / 이용률 → ARPU → margin

기타 IPO:
공모가 → 상장 후 수요 → 매출·수주·마진 → tariff/수출 리스크
```

---

# 2. 대상 canonical archetype

```text
FOOD_INFLATION_CLIMATE_INPUT_4C
ANIMAL_FEED_GRAIN_COST_4C
POULTRY_EGG_BIRD_FLU_SUPPLY_SHOCK
AGRI_MACHINERY_LABOR_SUBSTITUTION_OPTIONALITY
LIFE_SERVICE_LOGISTICS_CONTRACT_STAGE2
ECOMMERCE_SERVICE_TRUST_HARD_REFERENCE
WASTE_RECYCLING_INFRA_PLATFORM_STAGE2
DEMOGRAPHIC_CHILDCARE_EDUCATION_POLICY_EVENT
OTHER_MANUFACTURING_TOOLS_IPO_QUALITY_GATE
```

---

# 3. deep sub-archetype

```text
농산물/식품:
- napa cabbage / kimchi input cost
- heatwave crop damage
- government stock release
- CJ CheilJedang / Daesang / Pulmuone / kimchi-food basket

사료/축산:
- feed wheat tender not purchased due high offers
- chicken and egg prices from bird flu import disruption
- Harim / feed companies / poultry food processors
- imported egg tariff risk

농기계:
- Daedong / TYM
- tractors, combines, rice transplanters
- labor-shortage / aging-farmer / smart-farm optionality
- North America export cycle vs actual order/margin

생활물류:
- CJ Logistics / Shinsegae alliance
- SSG.com / e-commerce fulfilment
- revenue uplift vs local growth slowdown

생활서비스 trust:
- Coupang data breach
- Naver / E-Mart / Kurly / CJ Logistics read-through
- fast-delivery competition and consumer spending migration

폐기물/환경:
- KJ Environment / EQT waste-treatment platform
- plastic recycling / waste-to-energy
- food-waste RFID smart bins
- recycling rate / municipal economics

저출산·돌봄·교육:
- birthrate rebound
- baby/childcare/education-service basket
- temporary echo-boomer effect vs structural enrolment

기타:
- DN Solutions IPO
- machine tools for auto, semiconductor, aerospace, medical
- tariff risk and IPO-quality gate
```

---

# 4. 국장 신규 후보 case

## Case A — Kimchi cabbage / food-input inflation `4C-watch`

```text
symbols = 097950 / 001680 / 017810 / food-input basket
company_scope = CJ CheilJedang / Daesang / Pulmuone / kimchi-food processors
case_type = 4C-watch
archetype = FOOD_INFLATION_CLIMATE_INPUT_4C
```

### stage date

```text
Stage 1:
2024-06~2024-09
- record hot weather damages napa cabbage crop
- mountain-region cabbage supply disrupted
- kimchi peak-season input cost rises

Stage 4C-watch:
2024-10-23
- South Korea to supply 24,000 tonnes of kimchi cabbage from national stocks
- wholesale price reached 9,537 won per cabbage in September
- government to improve storage technology and emergency reserves

Stage 3:
없음
- crop-price spike is not food-company Green
- Green requires selling-price pass-through, inventory discipline, gross margin stability, export/order volume
```

이 case는 R12에서 “식품 가격 상승 = 식품주 수혜”가 아니라는 기준이다. Reuters는 폭염으로 napa cabbage 작황이 악화되자 정부가 김장철을 앞두고 24,000톤의 배추 비축분을 공급하기로 했고, 9월 도매가격이 배추 한 포기당 9,537원까지 올랐다고 보도했다. 식품기업에는 판가 전가가 되면 relief지만, 전가가 안 되면 바로 원가율 4C-watch다. ([Reuters][1])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters cabbage-climate input-cost anchor",
  "stage3_price": null,
  "stage4c_watch_date": "2024-10-23",
  "government_cabbage_stock_release_tonnes": 24000,
  "wholesale_price_per_cabbage_krw_september": 9537,
  "cause": "record hot weather damaged napa cabbage crop",
  "affected_businesses": ["kimchi processors", "food manufacturers", "restaurant/meal-service operators"],
  "selling_price_pass_through_confirmed": false,
  "company_level_ohlc": "price_data_unavailable_after_deep_search",
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = food_input_climate_cost_gate
stage_failure_type = crop_price_spike_not_margin_green
```

---

## Case B — Feed wheat / livestock input cost `4C-watch`

```text
symbols = 136480 / 028150 / 003960 / feed-livestock basket
company_scope = Harim / Easy Bio / 사료·계육 basket
case_type = 4C-watch
archetype = ANIMAL_FEED_GRAIN_COST_4C
```

### stage date

```text
Stage 1:
2026-05-13
- global wheat futures rise after lower U.S. harvest forecasts
- Korean feed buyers face elevated import offers
- livestock/feed cost pressure

Stage 4C-watch:
2026-05-13
- South Korea Feed Leaders Committee believed to make no purchase in tender for up to 65,000 tonnes feed wheat
- lowest offer: $298.50/ton c&f plus $2/ton additional unloading surcharge
- Black Sea loading ports in Russia/Ukraine prohibited

Stage 3:
없음
- feed tender failure is not Green
- feed/livestock Green requires cost pass-through, output price, feed conversion, flock/herd health, margin
```

사료 case는 R12의 input-cost 4C-watch다. Reuters는 한국 Feed Leaders Committee가 최대 65,000톤 feed wheat 입찰에서 가격이 높아 구매하지 않은 것으로 보인다고 보도했다. 최저 제안가격은 $298.50/ton c&f에 추가 하역 surcharge $2/ton이었다. 사료·축산주는 곡물가격이 오르면 테마로 움직일 수 있지만, 실제 Stage 3는 판가 전가와 feed conversion이 확인되어야 한다. ([Reuters][2])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters feed-wheat tender anchor",
  "stage3_price": null,
  "stage4c_watch_date": "2026-05-13",
  "tender_volume_tonnes": 65000,
  "purchase_result": "believed_no_purchase",
  "lowest_offer_usd_per_tonne": 298.50,
  "additional_unloading_surcharge_usd_per_tonne": 2.00,
  "effective_lowest_offer_usd_per_tonne": 300.50,
  "arrival_target": "2026-08-31",
  "black_sea_russia_ukraine_loading_ports_prohibited": true,
  "feed_cost_pass_through_confirmed": false,
  "company_level_ohlc": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = livestock_feed_cost_pressure
stage_failure_type = grain_cost_event_not_livestock_margin_green
```

---

## Case C — Poultry / egg supply shock `event premium + 4C-watch`

```text
symbols = 136480 / 003960 / poultry-food basket
company_scope = Harim / poultry processors / egg-food processors
case_type = event_premium + 4C-watch
archetype = POULTRY_EGG_BIRD_FLU_SUPPLY_SHOCK
```

### stage date

```text
Stage 1:
2025-05~2025-06
- Brazil bird flu outbreak disrupts poultry import flows
- chicken and egg prices rise in Korea
- government considers price-stabilisation measures

Stage 4C-watch:
2025-06-09
- Korean president asks officials to address rising living costs
- instant noodles, chicken, eggs cited
- Brazil bird flu outbreak contributed to chicken/egg price rise
- South Korea had restricted imports from affected Brazilian areas

Stage 2 relief:
2025-06-23
- Brazil says South Korea eases restrictions to affected region only after no new commercial outbreaks for 28 days

Stage 4B-watch:
2025-04-03
- U.S. imports eggs from Turkey, Brazil, South Korea to ease bird-flu shortage
- possible U.S. tariff on South Korean egg imports at 26%
```

Poultry/egg case는 R12에서 수혜와 비용이 동시에 붙는 양면 case다. 한국에서는 Brazil bird flu 때문에 chicken/egg 가격이 올라 생활물가 부담이 됐고, 이후 한국은 수입제한을 전국 ban에서 affected region 중심으로 완화했다. 반대로 미국은 bird flu로 South Korea eggs까지 수입했지만, 26% tariff 가능성이 거론됐다. 즉 “계란 수출/가격상승”만 보고 Green을 주면 안 되고, 질병·수입규제·tariff·원가 전가를 같이 봐야 한다. ([Reuters][3])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters bird-flu chicken/egg price and import-policy anchors",
  "stage3_price": null,
  "stage4c_watch_date": "2025-06-09",
  "price_items_flagged": ["instant noodles", "chicken", "eggs"],
  "brazil_import_restriction": "eased_to_affected_region_only",
  "brazil_commercial_flock_no_new_outbreak_period_days": 28,
  "us_south_korea_egg_import_tariff_risk_pct": 26,
  "us_import_context": "imports from Turkey, Brazil and South Korea to ease bird-flu shortage",
  "company_level_ohlc": "price_data_unavailable_after_deep_search",
  "margin_bridge_confirmed": false
}
```

### alignment

```text
score_price_alignment = event_premium_4C_watch
rerating_result = poultry_egg_supply_shock_two_sided
stage_failure_type = disease_supply_event_not_margin_green
```

---

## Case D — Daedong / TYM agricultural machinery `success_candidate + insufficient evidence`

```text
symbols = 000490 / 002900
company_scope = Daedong / TYM
case_type = success_candidate + insufficient_evidence
archetype = AGRI_MACHINERY_LABOR_SUBSTITUTION_OPTIONALITY
```

### stage date

```text
Stage 1:
2024~2026
- 농촌 고령화 / 인력 부족
- 농기계 자동화·스마트팜·정밀농업 필요성 증가
- North America compact tractor export optionality

Stage 2:
보류
- Daedong and TYM are listed Korean agricultural-machinery companies
- both sell tractors / combines / rice transplanters / cultivators
- Daedong uses Kioti brand in North America
- TYM operates in more than 40 countries

Stage 3:
없음
- labor-substitution theme alone is not Green
- actual order backlog, dealer inventory, North America sell-through, FX, financing cost, margin 확인 필요
```

Daedong/TYM은 R12의 정석적인 success_candidate지만, 이번 라운드에서는 강하게 Stage 3를 주지 않는다. Daedong은 tractor, combine, seeding/tillage equipment를 생산하고 North America에서는 Kioti brand로 알려져 있으며, TYM도 tractors, combines, rice transplanters 등을 만들고 40개국 이상에서 사업을 한다. 하지만 농촌 고령화와 자동화 필요성은 Stage 1/2일 뿐이다. 실제 Green은 dealer inventory와 North America sell-through, order backlog, financing cost, FX, margin이 닫혀야 한다. ([위키백과][4])

### 실제 가격경로 검증

```json
{
  "price_data_source": "company-profile / listed-business anchor; no reliable event OHLC located",
  "stage3_price": null,
  "daedong_ticker": "000490",
  "tym_ticker": "002900",
  "daedong_products": ["tractors", "combines", "forage equipment", "seeding/tillage equipment", "diesel engines"],
  "daedong_north_america_brand": "Kioti",
  "tym_products": ["tractors", "combine harvesters", "cultivators", "rice transplanters", "diesel engines"],
  "tym_country_presence": "more_than_40_countries",
  "actual_order_backlog_confirmed": false,
  "north_america_sellthrough_confirmed": false,
  "company_level_ohlc": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_but_insufficient_evidence
rerating_result = agri_machinery_labor_substitution_watch
stage_failure_type = aging_farm_theme_not_order_margin_green
```

---

## Case E — CJ Logistics / Shinsegae alliance `success_candidate + evidence_good_but_price_failed`

```text
symbol = 000120
case_type = success_candidate + evidence_good_but_price_failed
archetype = LIFE_SERVICE_LOGISTICS_CONTRACT_STAGE2
```

### stage date

```text
Stage 1:
2024-06-17
- CJ Logistics strengthens logistics alliance with Shinsegae Group
- SSG.com and e-commerce platform fulfilment demand
- one-day / overnight delivery competition

Stage 2:
2024-06-17
- Daiwa estimates alliance could boost CJ Logistics revenue by around 300B won annually
- three-year logistics partnership with Shinsegae / SSG.com
- target price cut 17% to 116,000 won
- outperform maintained
- shares trade 0.2% lower at 99,100 won

Stage 3:
없음
- revenue uplift is Stage 2
- Green requires shipment volume, unit economics, automation productivity, wage/fuel cost, overseas recovery
```

CJ Logistics는 R12 생활서비스/물류의 좋은 Stage 2지만, 당일 가격반응은 약했다. MarketWatch는 Shinsegae와의 3년 물류 제휴가 CJ Logistics revenue를 연 3,000억 원 정도 끌어올릴 수 있다고 전했지만, 국내 성장 둔화와 해외 회복 지연 때문에 목표가는 17% 하향됐고 주가는 99,100원에서 0.2% 하락했다. 즉 계약 자체보다 **물동량·단가·인건비·자동화 생산성**이 중요하다. ([마켓워치][5])

### 실제 가격경로 검증

```json
{
  "price_data_source": "MarketWatch / Dow Jones CJ Logistics alliance anchor",
  "stage3_price": null,
  "stage2_date": "2024-06-17",
  "annual_revenue_uplift_estimate_krw_bn": 300,
  "partnership_duration_years": 3,
  "partners": ["Shinsegae Group", "SSG.com"],
  "target_price_krw": 116000,
  "target_price_cut_pct": -17,
  "event_price_krw": 99100,
  "event_mae_pct": -0.2,
  "target_upside_from_event_price_pct": 17.1,
  "issues": ["slower local business growth", "delay in overseas-business recovery"],
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = evidence_good_but_price_failed
rerating_result = life_service_logistics_contract_stage2
stage_failure_type = revenue_uplift_not_unit_economics_green
```

---

## Case F — Coupang data breach / life-service trust `hard 4C reference`

```text
symbols = CPNG / 035420 / 139480 / 000120 read-through
company_scope = Coupang / Naver / E-Mart / CJ Logistics / Kurly
case_type = hard_4C_reference + competitor_event_premium
archetype = ECOMMERCE_SERVICE_TRUST_HARD_REFERENCE
```

### stage date

```text
Stage 1:
2025-11
- Coupang discloses massive data breach
- user names, phone numbers and addresses exposed
- no payment/login data, but trust damage material

Stage 4C:
2026-02-25
- around 34M users affected
- Science Ministry blames management failure rather than sophisticated cyberattack
- Coupang shares down around 34% since disclosure
- mobile MAU -3.5% from November to January
- daily consumer spending -6.3% to about 139.2B won
- revenue estimate cut 2.2%; core earnings estimate cut 6.7%

Stage 2 competitor read-through:
2026-02-25
- Naver online users and spending rose meaningfully
- Naver mobile users +23% from November to January
- CJ Logistics one-day / overnight shipment volume +120% YoY in Q4
```

Coupang case는 R12 생활서비스 hard reference다. 일상 서비스의 moat는 물류속도만이 아니라 **신뢰**다. Reuters는 Coupang breach가 약 3,400만 명에게 영향을 줬고, 정부가 sophisticated cyberattack보다 management failure에 가까운 문제로 봤으며, Coupang shares가 disclosure 이후 약 34% 하락했다고 보도했다. 동시에 Naver, E-Mart, Kurly, CJ Logistics가 수혜를 볼 수 있지만, 이 역시 competitor event premium이지 자동 Green은 아니다. ([Reuters][6])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters Coupang data-breach and competitor read-through anchor",
  "stage3_price": null,
  "affected_users_mn": 34,
  "exposed_data": ["names", "phone_numbers", "shipping_addresses"],
  "payment_or_login_data_exposed": false,
  "government_cause_assessment": "management_failure_rather_than_sophisticated_cyberattack",
  "coupang_share_decline_since_disclosure_pct": -34,
  "mobile_user_activity_change_pct": -3.5,
  "daily_consumer_spending_change_pct": -6.3,
  "daily_consumer_spending_jan_krw_bn": 139.2,
  "revenue_estimate_cut_pct": -2.2,
  "core_earnings_estimate_cut_pct": -6.7,
  "naver_mobile_users_change_pct": 23,
  "cj_logistics_overnight_one_day_volume_growth_q4_pct": 120,
  "direct_korean_competitor_stage3_confirmed": false
}
```

### alignment

```text
score_price_alignment = thesis_break_reference
rerating_result = ecommerce_life_service_trust_hard_gate
stage_failure_type = data_breach_trust_break
```

---

## Case G — Waste treatment / smart food-waste system `success_candidate + policy infrastructure`

```text
symbols = environmental-services basket / unlisted KJ Environment / smart-waste operators
case_type = success_candidate_policy_infra
archetype = WASTE_RECYCLING_INFRA_PLATFORM_STAGE2
```

### stage date

```text
Stage 1:
2024-08-16
- EQT acquires KJ Environment and affiliates to build Korea waste-treatment platform
- plastic recycling / waste-to-energy demand
- Seoul metropolitan waste catchment

Stage 2:
2024-08-16
- enterprise value over 1T won / $733M
- end-to-end portfolio in recyclable waste sorting, plastic recycling and waste-to-energy
- platform sites cover catchment areas over 50% of South Korea population

Stage 2 policy validation:
2025-12-18
- South Korea recycled 96.8% of 4.81M tonnes food waste in 2023
- Seoul operates 27,289 RFID food-waste units
- 81.6% of apartment residents served
- national RFID units: 150,738 serving 8.54M apartment households
- Seoul food waste down 23.9% in a decade
```

폐기물/음식물 쓰레기 case는 R12에서 구조적으로 좋은 영역이다. EQT는 KJ Environment를 인수해 recycled waste sorting, plastic recycling, waste-to-energy를 묶은 platform을 만들고, EV는 1조 원 이상으로 알려졌다. Guardian은 한국의 food-waste recycling rate가 2023년 96.8%였고, RFID 음식물쓰레기 bin이 서울에서 27,289대 운영되며 apartment residents의 81.6%를 커버한다고 보도했다. 다만 Green은 policy가 아니라 처리량, tipping fee, utilization, capex 회수다. ([Reuters][7])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters EQT waste-platform anchor + Guardian food-waste RFID policy anchor",
  "stage3_price": null,
  "kj_environment_platform_ev_krw_trn": 1.0,
  "kj_environment_platform_ev_usd_mn": 733,
  "catchment_population_coverage_pct": 50,
  "business_lines": ["recyclable_waste_sorting", "plastic_recycling", "waste_to_energy"],
  "food_waste_recycling_rate_2023_pct": 96.8,
  "food_waste_2023_mn_tonnes": 4.81,
  "seoul_rfid_units": 27289,
  "seoul_apartment_resident_coverage_pct": 81.6,
  "national_rfid_units": 150738,
  "national_apartment_households_served_mn": 8.54,
  "seoul_food_waste_decline_decade_pct": -23.9,
  "listed_company_ohlc": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_policy_infra
rerating_result = waste_recycling_infra_platform_stage2
stage_failure_type = recycling_policy_not_tipping_fee_FCF_green
```

---

## Case H — Birthrate rebound / childcare-education service basket `event premium + structural watch`

```text
symbols = 096240 / 068930 / 215200 / childcare-education-baby basket
company_scope = Cheil Worldwide? no; Megastudy Education / Woongjin Thinkbig / baby-childcare service basket
case_type = event_premium + structural_watch
archetype = DEMOGRAPHIC_CHILDCARE_EDUCATION_POLICY_EVENT
```

### stage date

```text
Stage 1:
2025-02-26
- 2024 births rise for first time in nine years
- fertility rate 0.75 vs 0.72 in 2023

Stage 2:
2026-02-25
- 2025 fertility rate rises again to 0.80
- births rise 6.8% to 254,500
- marriages +8.1%
- still population decline because deaths exceed births
- government plans five-year demographic response plan and extended childbirth incentives

Stage 4B-watch:
- baby/education/childcare basket may rerate on birth headline
- but structural cohorts still shrink after echo-boomer effect

Stage 3:
없음
- birthrate rebound is not company Green
- Green requires enrolment, ARPU, retention, margin, subsidy capture
```

저출산 반등은 R12 생활서비스에서 중요한 Stage 2지만, 바로 교육·아동주 Green은 아니다. Reuters는 2025년 합계출산율이 0.80으로 2년 연속 반등했고, 출생아 수가 254,500명으로 6.8% 증가했다고 보도했다. 그러나 Guardian은 echo-boomer 효과가 2027년 이후 약해질 수 있고, 사망자가 출생아보다 108,900명 많아 인구 감소가 지속됐다고 설명했다. 즉 출생률 headline은 event premium이고, 실제 enrolment·ARPU·retention 확인 전에는 Green 금지다. ([Reuters][8])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters / Guardian birthrate rebound anchors",
  "stage3_price": null,
  "fertility_rate_2023": 0.72,
  "fertility_rate_2024": 0.75,
  "fertility_rate_2025": 0.80,
  "births_2025": 254500,
  "births_2025_growth_pct": 6.8,
  "marriage_growth_2025_pct": 8.1,
  "deaths_exceeded_births_2025": 108900,
  "policy_plan": "five_year_demographic_response_plan_and_childbirth_incentives",
  "echo_boomer_temporary_effect_watch": true,
  "company_enrolment_ARPU_confirmed": false,
  "company_level_ohlc": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium_structural_watch
rerating_result = childcare_education_demographic_stage2
stage_failure_type = birthrate_headline_not_enrolment_ARPU_green
```

---

## Case I — DN Solutions IPO / other manufacturing services `IPO quality gate`

```text
symbol = DN Solutions
case_type = success_candidate + IPO_4B_watch
archetype = OTHER_MANUFACTURING_TOOLS_IPO_QUALITY_GATE
```

### stage date

```text
Stage 1:
2025-04-14
- DN Solutions opens bookbuilding for IPO
- machine tools for automotive, semiconductor, aerospace and medical sectors
- Korea IPO market quality test

Stage 2:
2025-04-14
- IPO raise up to 1.6T won / $1.1B
- 17.5M shares offered
- price range 65,000~89,700 won
- largest listing since LGES 2022 if completed at scale
- company acknowledges U.S. tariffs may dent market short term, while structural demand remains

Stage 2 추가:
2026-01-28 reference
- DN Solutions completes acquisition of German machine tool maker Heller, per company-profile reference
- global machine-tool scale-up optionality

Stage 3:
없음
- IPO bookbuilding and M&A optionality are not Green
- Green requires listed demand, order book, export margin, tariff pass-through, Heller integration
```

DN Solutions는 R12의 “기타” case로 둔다. Reuters는 DN Solutions가 최대 1.6조 원, 약 $1.1B IPO bookbuilding을 시작했으며, 자동차·반도체·항공우주·의료 sector에 machine tools를 공급한다고 보도했다. 다만 회사가 Trump tariff가 단기 시장에 영향을 줄 수 있다고 인정한 만큼, IPO는 Stage 2이고 Green은 상장 후 order book, export margin, tariff pass-through, Heller integration이 확인된 후다. ([Reuters][9])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters DN Solutions IPO anchor + company-profile Heller acquisition reference",
  "stage3_price": null,
  "ipo_raise_max_krw_trn": 1.6,
  "ipo_raise_max_usd_bn": 1.1,
  "shares_offered_mn": 17.5,
  "price_range_krw": "65000-89700",
  "final_price_set_date_planned": "2025-04-30",
  "listing_planned": "2025-05",
  "end_markets": ["automotive", "semiconductor", "aerospace", "medical"],
  "tariff_short_term_risk_acknowledged": true,
  "heller_acquisition_completed_reference": "2026-01-28",
  "post_listing_ohlc": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_IPO_4B_watch
rerating_result = other_manufacturing_tools_IPO_stage2
stage_failure_type = IPO_bookbuilding_not_order_margin_green
```

---

# 5. 이번 R12 case별 stage date 요약

| case           | Stage 1           | Stage 2                      | Stage 3 | Stage 4B               | Stage 4C                        |
| -------------- | ----------------- | ---------------------------- | ------- | ---------------------- | ------------------------------- |
| Kimchi cabbage | 2024-06~09        | stock release relief         | N/A     | food-inflation watch   | 2024-10-23 input-cost watch     |
| Feed wheat     | 2026-05-13        | N/A                          | N/A     | grain-cost watch       | 2026-05-13 tender failure watch |
| Poultry/egg    | 2025-05~06        | import easing relief         | N/A     | export/tariff event    | bird-flu supply watch           |
| Daedong/TYM    | 2024~2026         | business optionality         | N/A     | smart-farm theme watch | order/margin miss watch         |
| CJ Logistics   | 2024-06-17        | Shinsegae alliance           | N/A     | contract premium watch | local/overseas slowdown watch   |
| Coupang trust  | 2025-11           | competitor read-through      | N/A     | competitor premium     | 2026-02 hard reference          |
| Waste/RFID     | 2024-08 / 2025-12 | waste platform / RFID policy | N/A     | infra-policy premium   | capex/utilization watch         |
| Birthrate      | 2025~2026         | fertility rebound            | N/A     | baby/education theme   | cohort shrink watch             |
| DN Solutions   | 2025-04           | IPO bookbuilding             | N/A     | IPO valuation watch    | tariff/export watch             |

---

# 6. 실제 가격경로 검증 총괄

| case           |                                                         anchor | MFE / MAE 해석                              | 판정                             |
| -------------- | -------------------------------------------------------------: | ----------------------------------------- | ------------------------------ |
| Kimchi cabbage |                       24,000t stock release, 9,537 won/cabbage | food input-cost shock                     | 4C-watch                       |
| Feed wheat     |             65,000t no purchase, $300.50/t effective low offer | feed cost pressure                        | 4C-watch                       |
| Poultry/egg    | chicken/egg prices, Brazil import easing, 26% U.S. tariff risk | two-sided disease/tariff case             | event + 4C-watch               |
| Daedong/TYM    |                      products/global presence, no price anchor | agri automation optionality only          | insufficient                   |
| CJ Logistics   |          300B won annual revenue uplift estimate, shares -0.2% | good contract but price failed            | evidence_good_but_price_failed |
| Coupang trust  |      shares -34%, users -3.5%, spending -6.3%, CJ volume +120% | hard trust reference                      | thesis_break_reference         |
| Waste/RFID     |       platform EV >1T won, recycling 96.8%, RFID 150,738 units | structural policy infra                   | success_candidate              |
| Birthrate      |                        TFR 0.80, births +6.8%, marriages +8.1% | demographic headline, not company revenue | event_premium                  |
| DN Solutions   |                            IPO up to 1.6T won, price 65k~89.7k | IPO quality gate                          | success_candidate              |

---

# 7. score-price alignment 판정

```text
success_candidate:
- Daedong / TYM agricultural machinery
- CJ Logistics / Shinsegae alliance
- waste treatment / smart food-waste infrastructure
- DN Solutions IPO

event_premium:
- birthrate rebound baby/education basket
- poultry/egg export or price shock basket
- waste-policy / recycling-tech theme if traded before cashflow

evidence_good_but_price_failed:
- CJ Logistics, because annual revenue uplift estimate existed but shares were -0.2% and target was cut

price_moved_without_evidence:
- birthrate rebound if traded as childcare/education Green
- agri machinery if traded on aging-farmer theme without orders
- food inflation if traded as food-company Green without pass-through
- waste RFID if traded without tipping fee / utilisation / FCF

thesis_break_watch:
- kimchi cabbage input-cost shock
- feed wheat tender failure
- poultry/egg bird-flu supply shock
- DN Solutions tariff/export risk

thesis_break_reference:
- Coupang life-service trust break

hard_4C_confirmed:
- direct KRX listed hard 4C: false
- sector hard reference: Coupang service-trust/data breach
```

---

# 8. 점수비중 교정

## 올릴 축

```text
input_cost_pass_through +5
inventory_waste_control +5
feed_cost_hedging +5
disease_supply_chain_resilience +5
actual_order_backlog +5
dealer_sellthrough +5
logistics_unit_economics +5
data_trust_service_continuity +5
waste_tipping_fee_utilization +5
enrolment_ARPU_conversion +5
```

### 왜 올리나

Cabbage와 feed wheat는 “가격 상승”이 곧 수혜가 아니라 원가율 shock라는 점을 보여줬다. CJ Logistics는 계약이 있어도 unit economics와 국내/해외 growth가 확인되어야 한다. Coupang은 생활서비스에서 data trust가 깨지면 이용자·소비액·주가가 동시에 빠질 수 있다는 hard reference다. Birthrate rebound는 demographic headline일 뿐, 교육·돌봄 서비스의 enrolment와 ARPU로 내려와야 한다.

## 내릴 축

```text
food_inflation_headline_only -5
grain_price_event_only -5
disease_supply_shock_as_benefit_only -5
aging_farm_theme_only -5
logistics_revenue_uplift_without_margin -5
birthrate_headline_without_enrolment -5
recycling_policy_without_tipping_fee -5
IPO_size_without_aftermarket_demand -5
data_breach_or_trust_failure -5
```

### 왜 내리나

R12는 “생활필수재·필수서비스”라는 말 때문에 방어주처럼 보이지만, 실제로는 원가·인건비·신뢰·규제·물동량이 margin을 좌우한다. 특히 Coupang처럼 편의성이 큰 서비스도 trust가 깨지면 MAU와 spending이 바로 움직인다.

## Green gate 강화 조건

```text
R12 Stage 3-Green 필수:
1. 농식품은 input-cost pass-through 확인
2. 사료/축산은 feed cost hedge와 판가 전가 확인
3. 농기계는 order backlog, dealer inventory, financing cost 확인
4. 물류는 계약 물동량, 단가, 자동화 productivity, 인건비 확인
5. 생활서비스는 data trust와 service continuity 확인
6. 폐기물은 tipping fee, 처리량, utilisation, capex 회수 확인
7. 출산/교육은 enrolment, ARPU, retention, margin 확인
8. IPO는 상장 후 수요, order book, export margin 확인
9. price path가 evidence 이후 따라옴

금지:
식품가격 상승 headline only
출생률 rebound only
농기계 자동화 theme only
물류 제휴 headline only
폐기물 정책 headline only
IPO 규모 only
```

## 4B 조기감지 조건

```text
4B-watch:
배추/곡물/계란 가격 급등으로 식품·사료주 단기 급등
저출산 반등 headline으로 baby/education basket 급등
농기계/스마트팜 theme로 order 없이 급등
폐기물/recycling 정책으로 처리량·fee 전 가격화
대형 IPO bookbuilding으로 aftermarket demand 전 valuation 확장
Coupang breach 이후 경쟁사 수혜를 과도하게 선반영

4B-elevated:
원가 전가 불명확
질병/수입규제 불확실
dealer inventory 높음
물류 단가 낮음
서비스 trust 훼손
출생률 반등이 일시적 echo-boomer 효과
```

## 4C hard gate 조건

```text
crop failure / input-cost spike without pass-through
feed tender failure / grain shock
bird-flu or livestock-disease import disruption
data breach / service-trust failure
logistics labor or delivery interruption
waste-treatment permit loss / utilization collapse
birthrate rebound reversal
IPO weak debut / tariff export shock
```

이번 R12 Loop 13에서는 직접 국장 hard 4C는 확정하지 않는다. 다만 **Coupang data breach**를 생활서비스 trust hard reference로 두고, **cabbage/feed/poultry input shock**, **CJ Logistics unit-economics gap**, **birthrate headline risk**, **DN Solutions IPO/tariff risk**를 shadow gate로 둔다.

---

# 9. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 10. 레포 반영용 patch-ready 출력

## docs/round/round_209.md 요약

```md
# R12 Loop 13. Agriculture / Life Service / Other Price Validation

이번 라운드는 R12 Loop 13 price-validation 라운드다.

핵심 결론:
- Kimchi cabbage is food-input 4C-watch. Government released 24,000 tonnes of cabbage stocks after hot weather damaged crop; wholesale price reached 9,537 won per cabbage in September. Food-company Green requires price pass-through and margin stability.
- Feed wheat tender is livestock/feed input 4C-watch. South Korea FLC made no purchase in up to 65,000t feed-wheat tender due high prices; lowest offer was $298.50/t c&f plus $2/t surcharge. Feed/livestock Green requires pass-through and feed-conversion economics.
- Poultry/egg supply shock is event premium plus 4C-watch. Brazil bird flu drove Korean chicken/egg price concerns, import restrictions were later eased to affected regions, and U.S. South Korean egg import tariff risk was 26%.
- Daedong/TYM is agri-machinery success_candidate but insufficient evidence. Listed agricultural machinery makers have labor-substitution optionality, but Green requires order backlog, dealer sell-through, North America demand, FX and margin.
- CJ Logistics / Shinsegae alliance is success_candidate but evidence_good_but_price_failed. Daiwa estimated 300B won annual revenue uplift from three-year Shinsegae/SSG.com alliance, but shares were -0.2% at 99,100 won and target was cut 17%.
- Coupang data breach is life-service trust hard reference. 34M users affected, shares down about 34%, mobile users -3.5%, daily spending -6.3%; Naver users +23% and CJ Logistics overnight/one-day volume +120% are competitor event read-through, not automatic Green.
- Waste treatment / smart food-waste system is structural policy-infra Stage 2. EQT acquired KJ Environment platform with EV over 1T won; Korea recycled 96.8% of 4.81M tonnes food waste in 2023 and national RFID units served 8.54M apartment households. Tipping fee/utilization/FCF required.
- Birthrate rebound is demographic Stage 2, not childcare/education Green. Fertility rate rose to 0.80 in 2025, births +6.8% to 254,500, marriages +8.1%, but deaths still exceeded births by 108,900 and echo-boomer effect may fade.
- DN Solutions IPO is other-manufacturing Stage 2 plus IPO 4B-watch. IPO aimed to raise up to 1.6T won / $1.1B with price range 65,000~89,700 won; company serves auto, semiconductor, aerospace and medical sectors and acknowledged tariff risk.
```

## docs/checkpoints/checkpoint_28a_round209_r12_loop13.md 요약

```md
# Checkpoint 28A Round 209 R12 Loop 13 Agriculture Life Service Other Price Validation

## 반영 내용
- R12 Loop 13 price-validation 라운드를 추가했다.
- Kimchi cabbage climate input shock, feed wheat cost shock, poultry/egg bird-flu supply shock, Daedong/TYM agri machinery, CJ Logistics/Shinsegae alliance, Coupang service-trust break, waste/recycling infra, birthrate rebound, DN Solutions IPO를 비교했다.
- Reuters / MarketWatch / Guardian anchors로 가능한 event MFE/MAE 및 business metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- input cost pass-through, inventory/waste control, feed-cost hedging, disease supply-chain resilience, actual order backlog, dealer sell-through, logistics unit economics, data trust, waste tipping-fee utilisation, enrolment/ARPU conversion 가중치 강화
- food inflation headline-only, grain price event-only, disease shock as benefit-only, aging-farm theme-only, logistics revenue uplift without margin, birthrate headline without enrolment, recycling policy without tipping fee, IPO size without aftermarket demand 감점 강화
```

## data/e2r_case_library/cases_r12_loop13_round209.jsonl 초안

```jsonl
{"case_id":"r12_loop13_kimchi_cabbage_climate_food_input_cost","symbol":"097950/001680/017810_food_basket","company_name":"CJ CheilJedang / Daesang / Pulmuone food-input basket","case_type":"4c_watch","primary_archetype":"FOOD_INFLATION_CLIMATE_INPUT_4C","stage4c_date":"2024-10-23_watch","price_validation":{"price_data_source":"Reuters cabbage-climate input-cost anchor","stage3_price":null,"government_cabbage_stock_release_tonnes":24000,"wholesale_price_per_cabbage_krw_september":9537,"cause":"record hot weather damaged napa cabbage crop","affected_businesses":["kimchi processors","food manufacturers","restaurant/meal-service operators"],"selling_price_pass_through_confirmed":false,"company_level_ohlc":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"food_input_climate_cost_gate","notes":"Food inflation headline is not Green without pass-through and margin stability."}
{"case_id":"r12_loop13_feed_wheat_tender_livestock_cost_watch","symbol":"136480/028150/003960_feed_livestock_basket","company_name":"Harim / Easy Bio / livestock-feed basket","case_type":"4c_watch","primary_archetype":"ANIMAL_FEED_GRAIN_COST_4C","stage4c_date":"2026-05-13_watch","price_validation":{"price_data_source":"Reuters feed-wheat tender anchor","stage3_price":null,"tender_volume_tonnes":65000,"purchase_result":"believed_no_purchase","lowest_offer_usd_per_tonne":298.50,"additional_unloading_surcharge_usd_per_tonne":2.00,"effective_lowest_offer_usd_per_tonne":300.50,"arrival_target":"2026-08-31","black_sea_russia_ukraine_loading_ports_prohibited":true,"feed_cost_pass_through_confirmed":false,"company_level_ohlc":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"livestock_feed_cost_pressure","notes":"Grain-cost event is a margin gate, not automatic livestock/feed Green."}
{"case_id":"r12_loop13_poultry_egg_birdflu_supply_shock","symbol":"136480/003960_poultry_food_basket","company_name":"Harim / poultry and egg-food processors","case_type":"event_premium_4c_watch","primary_archetype":"POULTRY_EGG_BIRD_FLU_SUPPLY_SHOCK","stage4c_date":"2025-06_watch","stage2_date":"2025-06-23_relief","price_validation":{"price_data_source":"Reuters bird-flu chicken/egg price and import-policy anchors","stage3_price":null,"price_items_flagged":["instant noodles","chicken","eggs"],"brazil_import_restriction":"eased_to_affected_region_only","brazil_commercial_flock_no_new_outbreak_period_days":28,"us_south_korea_egg_import_tariff_risk_pct":26,"us_import_context":"imports from Turkey, Brazil and South Korea to ease bird-flu shortage","company_level_ohlc":"price_data_unavailable_after_deep_search","margin_bridge_confirmed":false},"score_price_alignment":"event_premium_4C_watch","rerating_result":"poultry_egg_supply_shock_two_sided","notes":"Disease and import-policy shock can be both price support and cost/regulatory risk."}
{"case_id":"r12_loop13_daedong_tym_agri_machinery_labor_substitution","symbol":"000490/002900","company_name":"Daedong / TYM","case_type":"success_candidate_insufficient_evidence","primary_archetype":"AGRI_MACHINERY_LABOR_SUBSTITUTION_OPTIONALITY","stage1_date":"2024-2026","price_validation":{"price_data_source":"company-profile / listed-business anchor; no reliable event OHLC located","stage3_price":null,"daedong_ticker":"000490","tym_ticker":"002900","daedong_products":["tractors","combines","forage equipment","seeding/tillage equipment","diesel engines"],"daedong_north_america_brand":"Kioti","tym_products":["tractors","combine harvesters","cultivators","rice transplanters","diesel engines"],"tym_country_presence":"more_than_40_countries","actual_order_backlog_confirmed":false,"north_america_sellthrough_confirmed":false,"company_level_ohlc":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_insufficient_evidence","rerating_result":"agri_machinery_labor_substitution_watch","notes":"Aging-farm theme is not Green until orders, dealer inventory, financing cost, FX and margin confirm."}
{"case_id":"r12_loop13_cj_logistics_shinsegae_alliance_unit_economics","symbol":"000120","company_name":"CJ Logistics","case_type":"success_candidate_evidence_good_but_price_failed","primary_archetype":"LIFE_SERVICE_LOGISTICS_CONTRACT_STAGE2","stage2_date":"2024-06-17","price_validation":{"price_data_source":"MarketWatch / Dow Jones CJ Logistics alliance anchor","stage3_price":null,"annual_revenue_uplift_estimate_krw_bn":300,"partnership_duration_years":3,"partners":["Shinsegae Group","SSG.com"],"target_price_krw":116000,"target_price_cut_pct":-17,"event_price_krw":99100,"event_mae_pct":-0.2,"target_upside_from_event_price_pct":17.1,"issues":["slower local business growth","delay in overseas-business recovery"],"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"evidence_good_but_price_failed","rerating_result":"life_service_logistics_contract_stage2","notes":"Revenue uplift estimate is Stage 2; logistics unit economics, automation productivity and cost control required."}
{"case_id":"r12_loop13_coupang_life_service_trust_break_reference","symbol":"CPNG/035420/139480/000120_readthrough","company_name":"Coupang / Naver / E-Mart / CJ Logistics read-through","case_type":"hard_4c_reference","primary_archetype":"ECOMMERCE_SERVICE_TRUST_HARD_REFERENCE","stage4c_date":"2026-02-25_reference","price_validation":{"price_data_source":"Reuters Coupang data-breach and competitor read-through anchor","stage3_price":null,"affected_users_mn":34,"exposed_data":["names","phone_numbers","shipping_addresses"],"payment_or_login_data_exposed":false,"government_cause_assessment":"management_failure_rather_than_sophisticated_cyberattack","coupang_share_decline_since_disclosure_pct":-34,"mobile_user_activity_change_pct":-3.5,"daily_consumer_spending_change_pct":-6.3,"daily_consumer_spending_jan_krw_bn":139.2,"revenue_estimate_cut_pct":-2.2,"core_earnings_estimate_cut_pct":-6.7,"naver_mobile_users_change_pct":23,"cj_logistics_overnight_one_day_volume_growth_q4_pct":120,"direct_korean_competitor_stage3_confirmed":false},"score_price_alignment":"thesis_break_reference","rerating_result":"ecommerce_life_service_trust_hard_gate","notes":"Life-service trust break can move users/spending; competitor read-through is not automatic Green."}
{"case_id":"r12_loop13_waste_recycling_food_waste_rfid_platform","symbol":"environmental_services_basket/unlisted_KJ_Environment","company_name":"KJ Environment / Korean food-waste RFID system","case_type":"success_candidate_policy_infra","primary_archetype":"WASTE_RECYCLING_INFRA_PLATFORM_STAGE2","stage2_date":"2024-08-16/2025-12-18","price_validation":{"price_data_source":"Reuters EQT waste-platform anchor + Guardian food-waste RFID policy anchor","stage3_price":null,"kj_environment_platform_ev_krw_trn":1.0,"kj_environment_platform_ev_usd_mn":733,"catchment_population_coverage_pct":50,"business_lines":["recyclable_waste_sorting","plastic_recycling","waste_to_energy"],"food_waste_recycling_rate_2023_pct":96.8,"food_waste_2023_mn_tonnes":4.81,"seoul_rfid_units":27289,"seoul_apartment_resident_coverage_pct":81.6,"national_rfid_units":150738,"national_apartment_households_served_mn":8.54,"seoul_food_waste_decline_decade_pct":-23.9,"listed_company_ohlc":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_policy_infra","rerating_result":"waste_recycling_infra_platform_stage2","notes":"Recycling policy and infra scale are Stage 2; tipping fee, utilization, permit and FCF required."}
{"case_id":"r12_loop13_birthrate_rebound_childcare_education_event","symbol":"096240/068930/215200_childcare_education_basket","company_name":"Childcare / baby / education-service basket","case_type":"event_premium_structural_watch","primary_archetype":"DEMOGRAPHIC_CHILDCARE_EDUCATION_POLICY_EVENT","stage2_date":"2026-02-25","price_validation":{"price_data_source":"Reuters / Guardian birthrate rebound anchors","stage3_price":null,"fertility_rate_2023":0.72,"fertility_rate_2024":0.75,"fertility_rate_2025":0.80,"births_2025":254500,"births_2025_growth_pct":6.8,"marriage_growth_2025_pct":8.1,"deaths_exceeded_births_2025":108900,"policy_plan":"five_year_demographic_response_plan_and_childbirth_incentives","echo_boomer_temporary_effect_watch":true,"company_enrolment_ARPU_confirmed":false,"company_level_ohlc":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_structural_watch","rerating_result":"childcare_education_demographic_stage2","notes":"Birthrate rebound is not company Green until enrolment, ARPU, retention and margin confirm."}
{"case_id":"r12_loop13_dn_solutions_other_manufacturing_tools_ipo","symbol":"DN_Solutions","company_name":"DN Solutions","case_type":"success_candidate_ipo_4b_watch","primary_archetype":"OTHER_MANUFACTURING_TOOLS_IPO_QUALITY_GATE","stage2_date":"2025-04-14","price_validation":{"price_data_source":"Reuters DN Solutions IPO anchor + company-profile Heller acquisition reference","stage3_price":null,"ipo_raise_max_krw_trn":1.6,"ipo_raise_max_usd_bn":1.1,"shares_offered_mn":17.5,"price_range_krw":"65000-89700","final_price_set_date_planned":"2025-04-30","listing_planned":"2025-05","end_markets":["automotive","semiconductor","aerospace","medical"],"tariff_short_term_risk_acknowledged":true,"heller_acquisition_completed_reference":"2026-01-28","post_listing_ohlc":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_IPO_4B_watch","rerating_result":"other_manufacturing_tools_IPO_stage2","notes":"IPO size and end-market exposure are Stage 2; listed demand, order book, export margin and tariff pass-through required."}
```

## data/sector_taxonomy/score_weight_profiles_round209_r12_loop13_v1.csv 초안

```csv
archetype,input_cost_pass_through,inventory_waste_control,feed_cost_hedging,disease_supply_chain_resilience,actual_order_backlog,dealer_sellthrough,logistics_unit_economics,data_trust_service_continuity,waste_tipping_fee_utilization,enrolment_arpu_conversion,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
FOOD_INFLATION_CLIMATE_INPUT_4C,+5,+5,+0,+2,+0,+0,+1,+1,+0,+0,-5,+5,+4,Cabbage price spike is input-cost gate unless pass-through and margin hold.
ANIMAL_FEED_GRAIN_COST_4C,+5,+4,+5,+3,+0,+0,+1,+1,+0,+0,-5,+5,+4,Feed wheat tender failure shows grain-cost pressure before margin proof.
POULTRY_EGG_BIRD_FLU_SUPPLY_SHOCK,+5,+4,+4,+5,+0,+0,+1,+1,+0,+0,-5,+5,+5,Disease shock needs import rules, flock health, pass-through and margin.
AGRI_MACHINERY_LABOR_SUBSTITUTION_OPTIONALITY,+1,+2,+0,+1,+5,+5,+1,+1,+0,+0,-5,+5,+3,Daedong/TYM aging-farm theme needs backlog, dealer sell-through, FX and margin.
LIFE_SERVICE_LOGISTICS_CONTRACT_STAGE2,+1,+2,+0,+1,+2,+0,+5,+4,+0,+0,-5,+5,+4,CJ Logistics needs unit economics, automation, wage/fuel cost and volume conversion.
ECOMMERCE_SERVICE_TRUST_HARD_REFERENCE,+0,+1,+0,+0,+0,+0,+5,+5,+0,+0,0,+4,+5,Coupang breach confirms trust hard gate for life-service platforms.
WASTE_RECYCLING_INFRA_PLATFORM_STAGE2,+0,+5,+0,+0,+2,+0,+2,+2,+5,+0,-5,+4,+4,Waste/recycling policy needs tipping fee, utilization, permit and FCF.
DEMOGRAPHIC_CHILDCARE_EDUCATION_POLICY_EVENT,+0,+1,+0,+0,+0,+0,+1,+2,+0,+5,-5,+5,+3,Birthrate rebound needs enrolment, ARPU, retention and margin.
OTHER_MANUFACTURING_TOOLS_IPO_QUALITY_GATE,+2,+2,+0,+0,+5,+3,+1,+1,+0,+0,-5,+5,+3,DN Solutions IPO needs order book, export margin, tariff pass-through and aftermarket demand.
```

---

# 이번 R12 Loop 13 결론

```text
1. Kimchi cabbage는 food-input 4C-watch다.
   배추 가격상승은 식품주 수혜가 아니라 원가율 gate다.

2. Feed wheat tender failure는 사료·축산 4C-watch다.
   구매를 못 할 만큼 가격이 높으면 feed-cost pass-through가 핵심이다.

3. Poultry/egg shock은 양면 event다.
   가격상승 수혜처럼 보이지만 bird flu, 수입규제, tariff, 질병 리스크가 같이 있다.

4. Daedong/TYM은 농기계 success_candidate지만 아직 insufficient evidence다.
   농촌 고령화 theme가 아니라 order backlog와 dealer sell-through가 Stage 3 조건이다.

5. CJ Logistics는 좋은 계약이 있어도 price failed다.
   300B won revenue uplift estimate가 있어도 unit economics가 닫히지 않으면 Green이 아니다.

6. Coupang data breach는 R12 생활서비스 hard reference다.
   편의성보다 trust가 먼저고, competitor read-through도 자동 Green은 아니다.

7. Waste/recycling infra는 구조적 Stage 2다.
   96.8% recycling rate와 RFID 보급은 좋지만 tipping fee, utilization, FCF가 필요하다.

8. Birthrate rebound는 demographic Stage 2다.
   baby/education service Green은 출생률이 아니라 enrolment, ARPU, retention이다.

9. DN Solutions IPO는 기타 제조서비스 Stage 2다.
   IPO 규모와 end-market exposure보다 상장 후 order book, tariff, margin이 중요하다.
```

한 문장으로 압축하면:

> **R12에서 진짜 Stage 3는 “생활필수·농산물 가격·출생률·폐기물·물류·IPO가 좋다”가 아니라, 원가 전가·물동량·처리량·신뢰·enrolment·order backlog·FCF가 실제 숫자로 닫히는 순간이다.**

[1]: https://www.reuters.com/world/asia-pacific/south-korea-supply-stocks-kimchi-cabbage-after-hot-weather-damages-crop-2024-10-23/ "https://www.reuters.com/world/asia-pacific/south-korea-supply-stocks-kimchi-cabbage-after-hot-weather-damages-crop-2024-10-23/"
[2]: https://www.reuters.com/world/asia-pacific/south-koreas-flc-believed-make-no-purchase-65000-ton-feed-wheat-tender-traders-2026-05-13/ "https://www.reuters.com/world/asia-pacific/south-koreas-flc-believed-make-no-purchase-65000-ton-feed-wheat-tender-traders-2026-05-13/"
[3]: https://www.reuters.com/markets/asia/south-korea-president-calls-measures-respond-rising-prices-2025-06-09/ "https://www.reuters.com/markets/asia/south-korea-president-calls-measures-respond-rising-prices-2025-06-09/"
[4]: https://en.wikipedia.org/wiki/Daedong_%28company%29 "https://en.wikipedia.org/wiki/Daedong_%28company%29"
[5]: https://www.marketwatch.com/story/cj-logistics-set-to-gain-from-stronger-ties-with-retailer-shinsegae-market-talk-5d3e0c7a "https://www.marketwatch.com/story/cj-logistics-set-to-gain-from-stronger-ties-with-retailer-shinsegae-market-talk-5d3e0c7a"
[6]: https://www.reuters.com/business/retail-consumer/coupang-braces-increased-competition-amid-fallout-south-korea-data-breach-2026-02-25/ "https://www.reuters.com/business/retail-consumer/coupang-braces-increased-competition-amid-fallout-south-korea-data-breach-2026-02-25/"
[7]: https://www.reuters.com/markets/deals/eqt-strikes-deal-acquire-south-korean-waste-treatment-platform-2024-08-16/ "https://www.reuters.com/markets/deals/eqt-strikes-deal-acquire-south-korean-waste-treatment-platform-2024-08-16/"
[8]: https://www.reuters.com/business/healthcare-pharmaceuticals/south-koreas-birthrate-worlds-lowest-rises-again-amid-signs-easing-demographic-2026-02-25/ "https://www.reuters.com/business/healthcare-pharmaceuticals/south-koreas-birthrate-worlds-lowest-rises-again-amid-signs-easing-demographic-2026-02-25/"
[9]: https://www.reuters.com/markets/deals/south-koreas-dn-solutions-opens-books-1-billion-plus-ipo-2025-04-14/ "https://www.reuters.com/markets/deals/south-koreas-dn-solutions-opens-books-1-billion-plus-ipo-2025-04-14/"

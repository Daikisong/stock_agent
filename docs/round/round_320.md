순서상 이번은 **R12 Loop 16 — 농업·생활서비스·기타 trigger-level price validation 라운드**다.

이번 R12는 “농업/생활서비스/기타”라서 겉보기엔 잡다해 보이지만, 실제로는 **생활 필수 소비 인프라** 라운드에 가깝다. 핵심은 식량·외식·배달·교육·반려동물·출산·의료교육 같은 생활권 이벤트가 **가격 전가, 사용자 이동, 정책 보조금, 플랫폼 M&A, 비용 압박, 구조적 수요**로 이어지는지 보는 것이다.

```text
round = R12 Loop 16
round_id = round_248
large_sector = AGRICULTURE_LIFE_SERVICES_MISC
method = trigger_level_backtest_v1_after_redteam
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R13 Loop 16
```

이번 라운드에서도 KRX/Naver/Yahoo/Stooq 수정주가 일봉 OHLC 30D/90D/180D/1Y/2Y window는 안정적으로 확보하지 못했다. 그래서 MFE/MAE를 숫자로 만들지 않는다. 대신 Reuters/AP의 **reported event return, user/spending metrics, policy budget, food-price data, tender price, education/exam demand data**를 trigger anchor로 쓴다. 특히 R12는 상장사 직접 가격 anchor가 약한 생활권 정책 이벤트가 많아서, `stage_candidate`와 `price_validation_status`를 철저히 분리한다.

---

# 1. 이번 라운드 대섹터

```text
R12 = 농업·생활서비스·기타
```

R12의 core gate는 아래다.

```text
식량 / 농업:
곡물·쌀·과일 가격 → 정부 import quota / 보조금 → 식품·외식 원가 → 가격전가 → volume elasticity

사료 / 축산:
feed wheat/corn/soy price → 사료업체 원가 → 축산마진 → 닭고기/돼지고기 가격 → 가공식품 margin

배달 / 생활 플랫폼:
M&A / regulation / data breach → user shift → GMV / spending → delivery volume → commission margin

교육 / 시험:
수능 응시자 수 → 사교육 수요 → 온라인/오프라인 교육 매출 → margin → 정부 규제

의료교육 / 필수생활 서비스:
의대정원 정책 → 교육/병원 운영 혼선 → 시스템 신뢰 → 정책 reversal / freeze → 관련 서비스 수요

반려동물 / 동물복지:
dog-meat ban → dog farms shutdown → subsidies / rehoming → pet-care/shelter/vet/pet-food demand

출산 / childcare:
fertility / marriages → childcare / baby goods / education pipeline → but demographic trend durability gate

기타 생활서비스:
household delivery, hypermarket operating rules, overnight delivery competition, consumer trust
```

---

# 2. 대상 canonical archetype

```text
FOOD_DELIVERY_PLATFORM_MA_STAGE2_WITH_APPROVAL_4B
EVERYDAY_DELIVERY_SHARE_SHIFT_STAGE2_WITH_SECURITY_4C
FOOD_PRICE_INFLATION_IMPORT_QUOTA_STAGE2_4B
FEED_WHEAT_COST_SHOCK_4B
PET_WELFARE_POLICY_TRANSITION_STAGE2_NO_PRICE
EDUCATION_EXAM_DEMAND_STAGE2_NO_PRICE
FERTILITY_CHILDCARE_POLICY_STAGE2_NO_PRICE
MEDICAL_EDUCATION_QUOTA_POLICY_4B_RELIEF
```

---

# 3. deep sub-archetype

```text
Baemin / Naver / Uber:
- Uber and Naver formed a consortium to bid up to 8T won / $5.34B for Baemin.
- Uber/Naver consortium ratio reported as 8:2.
- Naver confirmed teaser letter but said no decision.
- Delivery Hero shares +5.6% after Uber increased stake to 19.5%.
- Stage2 platform-M&A trigger, but approval / financing / Naver economics missing.

Coupang / Naver / E-Mart / CJ Logistics:
- Coupang breach affected around 34M users.
- Coupang mobile MAU -3.5%, average daily spending -6.3% to 139.2B won.
- Naver online users +23%.
- CJ Logistics overnight/one-day volume +120% in Q4.
- Coupang shares around -34% since breach.
- R12 생활배송 share-shift Stage2 + Coupang security hard 4C.

Food price / inflation:
- Korea Nov 2025 CPI +2.4% YoY.
- agricultural/fishery prices +5.6%; rice +18.6%; mandarins +26.5%.
- processed food prices high due weather and weak won.
- government second extra budget included support for food-price burden and import quota increases.
- Stage2 food-price policy relief, but food producers/restaurants may face margin 4B.

Feed wheat:
- South Korea FLC made no purchase in 65,000 ton feed wheat tender because offers were too high.
- lowest offer around $298.50/ton c&f plus $2 surcharge.
- Chicago wheat futures rose on reduced U.S. harvest forecast.
- Feed/livestock cost 4B for Harim/Farmsco/feed basket, no direct stock anchor.

Dog meat ban / pet transition:
- Government plans to spend around 100B won / $75M on incentives.
- up to 600,000 won per dog for surrender.
- nearly half a million dogs need rehoming or sheltering.
- dog meat ban effective early 2027.
- Pet-care/shelter/vet/pet-food Stage2 policy reference, but no clean listed price anchor.

CSAT / education services:
- 554,174 people registered for CSAT in Nov 2025, +6% YoY and highest since 2019.
- flights paused for 35 minutes, 140 flights affected.
- education service demand Stage2, but no listed price anchor.

Birthrate / childcare:
- total fertility rate rose to 0.80 in 2025 from 0.75 in 2024.
- births +6.8%, marriages +8.1%.
- government plans five-year demographic response plan and childbirth incentives.
- childcare/baby/education pipeline Stage2, but trend durability uncertain.

Medical education quota:
- Education ministry proposed freezing new medical students at around 3,000 annually to resolve 13-month dispute.
- 90% trainee doctors had resigned/walked out context.
- medical/education services policy relief, but not clean investible Stage3.
```

---

# 4. 선정 case 요약

| bucket                       | case                                       | 핵심 판정                                                                            |
| ---------------------------- | ------------------------------------------ | -------------------------------------------------------------------------------- |
| Stage2-Actionable 후보         | Baemin / Naver / Uber food-delivery M&A    | 8T won bid headline, Delivery Hero +5.6%. Naver 직접 가격·승인 없음                      |
| hard 4C + rival Stage2       | Coupang breach / Naver·E-Mart·CJ Logistics | Coupang -34%, Naver users +23%, CJ overnight volume +120%                        |
| Stage2 policy + 4B           | Food-price inflation / import quota        | rice +18.6%, mandarins +26.5%, food-price burden support                         |
| 4B cost shock                | Feed wheat tender failure                  | 65,000t feed wheat no purchase due high offers; livestock/feed margin risk       |
| Stage2 policy reference      | Dog-meat ban / pet transition              | 100B won incentives, 500k dogs, pet-care potential; price anchor 없음              |
| Stage2 demand reference      | CSAT / education services                  | 554,174 applicants, +6%, highest since 2019; education demand, price anchor 없음   |
| Stage2 demographic reference | Birthrate rebound / childcare              | fertility 0.80, marriages +8.1%, births +6.8%; trend durability gate             |
| 4B relief                    | Medical education quota freeze             | quota freeze proposal relieves service disruption, but policy trust gate remains |

---

# 5. Case별 trigger grid

## Case A — Baemin / Naver / Uber food-delivery M&A

```text
symbols = 035420 / UBER / Delivery_Hero_readthrough
case_type = Stage2 platform M&A
archetype = FOOD_DELIVERY_PLATFORM_MA_STAGE2_WITH_APPROVAL_4B
```

| trigger |            type | date       | 당시 공개 evidence                                                                         | 가격 anchor                      | outcome |
| ------- | --------------: | ---------- | -------------------------------------------------------------------------------------- | ------------------------------ | ------- |
| T0      |       awareness | 2026-05    | Delivery Hero / Baemin sale speculation, Korean food-delivery consolidation            | no Naver price                 |         |
| T1      | Stage2 evidence | 2026-05-18 | Uber + Naver consortium bid up to 8T won / $5.34B for Baemin, 8:2 consortium structure | Naver direct price unavailable |         |
| T2      |     price proxy | 2026-05-18 | Uber increased Delivery Hero stake to 19.5%, stake worth about €1.7B                   | Delivery Hero +5.6%            |         |
| T3      |        4B-watch | 2026       | no final decision, approval/financing/integration/commission regulation unknown        | 4B                             |         |
| T4      |   Stage3-Yellow | N/A        | final SPA, regulatory approval, Naver economics, GMV take-rate not confirmed           | no Yellow                      |         |

Baemin case는 R12 생활서비스에서 가장 직접적인 플랫폼 M&A trigger다. Reuters는 Uber와 Naver가 Baemin 인수를 위해 최대 8T won, 약 $5.34B 입찰을 제안했고, Uber 80%·Naver 20% 구조의 consortium이라고 보도했다. 다만 Naver는 teaser letter를 받은 것은 확인했지만 아직 결정된 것은 없다고 밝혔다. 같은 날 별도 Reuters 보도에서 Uber는 Delivery Hero 지분을 약 19.5%로 늘렸고, Delivery Hero shares는 +5.6%로 반응했다. 따라서 이 case는 **Stage2 platform-M&A**이지만, Naver 직접가격·최종계약·승인·GMV take-rate 전에는 Green이 아니다. ([Reuters][1])

```json
{
  "case_id": "r12_loop16_baemin_naver_uber_food_delivery_ma",
  "symbols": "035420/UBER/Delivery_Hero_readthrough",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2_platform_MA_with_approval_4B",
  "trigger_date": "2026-05-18",
  "baemin_bid_value_krw_trn": 8.0,
  "baemin_bid_value_usd_bn": 5.34,
  "consortium_ratio": "Uber_80pct_Naver_20pct",
  "naver_decision_status": "teaser_letter_received_no_final_decision",
  "uber_delivery_hero_stake_pct": 19.5,
  "delivery_hero_stake_value_eur_bn": 1.7,
  "delivery_hero_event_return_pct": 5.6,
  "direct_naver_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "final_SPA",
    "regulatory_approval",
    "financing_structure",
    "Naver_economics",
    "Baemin_GMV_take_rate",
    "commission_regulation",
    "full_OHLC_MFE_MAE"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_food_delivery_platform_MA_not_Green"
}
```

---

## Case B — Coupang breach / everyday delivery share shift

```text
symbols = CPNG / 035420 / 139480 / 000120 / Kurly_private
case_type = hard 4C + rival Stage2
archetype = EVERYDAY_DELIVERY_SHARE_SHIFT_STAGE2_WITH_SECURITY_4C
```

| trigger |          type | date       | 당시 공개 evidence                                                           | 가격 anchor                                   | outcome |
| ------- | ------------: | ---------- | ------------------------------------------------------------------------ | ------------------------------------------- | ------- |
| T0      |       hard 4C | 2025-11~12 | Coupang data breach disclosed; 33M+ users affected                       | Coupang -17% since disclosure in Dec report |         |
| T1      | 4C validation | 2026-02-25 | Coupang shares around -34% since breach, MAU -3.5%, daily spending -6.3% | -34%                                        |         |
| T2      |  rival Stage2 | 2026-02-25 | Naver online users +23%, CJ Logistics overnight/one-day volume +120% Q4  | rival KRX price unavailable                 |         |
| T3      |     policy 4B | 2026       | government plans to ease late-night hypermarket delivery restrictions    | 4B for Coupang moat                         |         |
| T4      | Stage3-Yellow | N/A        | Naver/E-Mart/CJ revenue/margin conversion not confirmed                  | no Yellow                                   |         |

이 case는 R5/R8에서도 나왔지만 R12 생활서비스에서는 “매일 쓰는 배송/장보기 서비스의 trust shift”로 다시 기록해야 한다. Reuters는 Coupang breach 이후 Coupang shares가 약 -34%, mobile MAU가 11월 대비 1월 -3.5%, average daily consumer spending이 -6.3%로 139.2B won까지 떨어졌다고 보도했다. 같은 기간 Naver online users는 +23%, CJ Logistics overnight/one-day delivery volume은 Q4에 +120% 증가했다. 이건 Coupang hard 4C와 동시에 rival Stage2가 생긴 case지만, Naver/E-Mart/CJ의 실제 GMV·margin conversion 전에는 Green이 아니다. ([Reuters][2])

```json
{
  "case_id": "r12_loop16_coupang_everyday_delivery_share_shift",
  "symbols": "CPNG/035420/139480/000120/Kurly_private",
  "best_trigger": "T0/T3",
  "best_trigger_type": "hard_4C_plus_rival_Stage2",
  "breach_disclosure_context": "2025-11_to_2025-12",
  "affected_users_mn": "33_to_34",
  "coupang_return_since_breach_pct": -34,
  "coupang_dec_report_return_since_disclosure_pct": -17,
  "mobile_mau_change_pct": -3.5,
  "daily_spending_change_pct": -6.3,
  "daily_spending_jan_krw_bn": 139.2,
  "naver_online_users_change_pct": 23,
  "cj_logistics_overnight_one_day_volume_yoy_q4_pct": 120,
  "rival_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "Naver_GMV_conversion",
    "E_Mart_delivery_revenue",
    "CJ_Logistics_margin",
    "Coupang_churn_duration",
    "hypermarket_late_night_rule_change",
    "fine_finalization"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "everyday_delivery_security_4C_with_rival_stage2"
}
```

---

## Case C — Food-price inflation / import-quota policy relief

```text
symbols = food_processor_basket / restaurant_basket / grocer_basket
case_type = Stage2 food-price policy + margin 4B
archetype = FOOD_PRICE_INFLATION_IMPORT_QUOTA_STAGE2_4B
```

| trigger |                 type | date       | 당시 공개 evidence                                                                               | 가격 anchor               | outcome |
| ------- | -------------------: | ---------- | -------------------------------------------------------------------------------------------- | ----------------------- | ------- |
| T0      |        4B cost shock | 2025-11    | CPI +2.4% YoY; agricultural/fishery prices +5.6%; rice +18.6%, mandarins +26.5%              | stock price unavailable |         |
| T1      | Stage2 policy relief | 2025-06    | second supplementary budget, food-price burden support, import quota increases               | no listed price         |         |
| T2      |           validation | 2025-06~12 | processed food prices high due weather, weak won; BOK says retail distribution reform needed | no price                |         |
| T3      |        Stage3-Yellow | N/A        | company-specific pass-through and volume resilience not confirmed                            | no Yellow               |         |

Food-price case는 R12 농업/생활서비스의 핵심이다. Reuters는 2025년 11월 한국 CPI가 +2.4% YoY였고, agricultural/fishery product prices가 +5.6%, rice +18.6%, mandarins +26.5%였다고 보도했다. 별도 Reuters 보도에서는 정부가 second supplementary budget에 food-price burden support, import quota increases, oil-tax break extension 등을 포함한다고 했다. 이는 생활비 안정 Stage2 policy relief지만, 식품·외식기업 입장에서는 원가 상승 4B이기도 하다. 정부가 가격을 눌러도 기업 margin이 바로 좋아지는 것이 아니라, **pass-through와 volume elasticity**를 봐야 한다. ([Reuters][3])

```json
{
  "case_id": "r12_loop16_food_price_inflation_import_quota",
  "symbols": "food_processor_basket/restaurant_basket/grocer_basket",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage2_policy_relief_with_margin_4B",
  "inflation_reference_date": "2025-12-01",
  "headline_cpi_yoy_pct": 2.4,
  "agri_fishery_price_yoy_pct": 5.6,
  "rice_price_yoy_pct": 18.6,
  "mandarin_price_yoy_pct": 26.5,
  "supplementary_budget_date": "2025-06-16",
  "policy_measures": [
    "food_price_burden_support",
    "import_quota_increases",
    "oil_tax_break_extension",
    "cash_like_consumption_support"
  ],
  "direct_stock_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "company_specific_price_pass_through",
    "volume_elasticity",
    "gross_margin_recovery",
    "retail_distribution_reform",
    "weather_normalization",
    "KRW_stabilization"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "food_price_policy_stage2_with_margin_4B"
}
```

---

## Case D — Feed wheat tender failure / livestock-feed cost shock

```text
symbols = 136480 / 027740 / 088910 / 003380 / feed_livestock_basket
case_type = 4B feed-cost shock
archetype = FEED_WHEAT_COST_SHOCK_4B
```

| trigger |            type | date       | 당시 공개 evidence                                                                        | 가격 anchor      | outcome |
| ------- | --------------: | ---------- | ------------------------------------------------------------------------------------- | -------------- | ------- |
| T0      | 4B cost trigger | 2026-05-13 | South Korea FLC made no purchase in 65,000t feed wheat tender because offers too high | no stock price |         |
| T1      |      validation | 2026-05-13 | lowest offer $298.50/t c&f + $2/t unloading surcharge; U.S. wheat futures surged      | no price       |         |
| T2      |   Stage2 relief | N/A        | pass-through to livestock product prices or government support not confirmed          | no relief      |         |
| T3      |   Stage3-Yellow | N/A        | feed margin recovery / livestock price pass-through not confirmed                     | no Yellow      |         |

Feed wheat tender failure는 R12 농업 cost 4B다. Reuters는 South Korea’s Feed Leaders Committee가 65,000 metric tons feed wheat tender에서 구매하지 않은 것으로 보인다고 전했고, 이유는 U.S. harvest forecast 악화 이후 Chicago wheat futures가 뛰며 offer가 너무 높았기 때문이었다. 최저 offer는 $298.50/t c&f에 추가 unloading surcharge $2/t였다고 보도됐다. 이는 feed/livestock basket에는 원가 4B다. Harim/Farmsco/Easy Bio 같은 feed-livestock 관련주는 **사료 원가 → 축산물 가격 전가 → 소비 감소**까지 봐야 한다. ([Reuters][4])

```json
{
  "case_id": "r12_loop16_feed_wheat_cost_shock",
  "symbols": "136480/027740/088910/003380/feed_livestock_basket",
  "best_trigger": "T0/T2",
  "best_trigger_type": "4B_feed_cost_shock",
  "trigger_date": "2026-05-13",
  "tender_volume_tons": 65000,
  "purchase_result": "believed_no_purchase",
  "reason": "offers_too_high_after_US_wheat_futures_surge",
  "lowest_offer_usd_per_ton_cf": 298.50,
  "additional_unloading_surcharge_usd_per_ton": 2.00,
  "arrival_target": "2026-08-31",
  "direct_feed_stock_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "feed_price_pass_through",
    "livestock_product_price",
    "gross_margin_recovery",
    "government_support",
    "volume_impact",
    "grain_price_normalization"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "feed_cost_4B_not_actionable"
}
```

---

## Case E — Dog-meat ban / pet welfare transition

```text
symbols = pet_food_vet_shelter_basket / policy_reference
case_type = Stage2 pet-welfare policy reference
archetype = PET_WELFARE_POLICY_TRANSITION_STAGE2_NO_PRICE
```

| trigger |              type | date       | 당시 공개 evidence                                                                     | 가격 anchor       | outcome |
| ------- | ----------------: | ---------- | ---------------------------------------------------------------------------------- | --------------- | ------- |
| T0      |     Stage2 policy | 2024-01    | parliament passed dog-meat ban, effective after grace period in 2027               | no listed price |         |
| T1      | Stage2 transition | 2024-09-26 | government to spend about 100B won / $75M on incentives; up to 600,000 won per dog | no price        |         |
| T2      |        validation | 2024-09-26 | nearly half a million dogs to be rehomed/adopted/sheltered                         | no price        |         |
| T3      |          4B-watch | 2024~2027  | shelter capacity, farmer resistance, subsidy adequacy, no clear listed beneficiary | 4B              |         |
| T4      |     Stage3-Yellow | N/A        | pet-food/vet listed revenue conversion not confirmed                               | no Yellow       |         |

Dog-meat ban은 R12 “생활문화가 정책으로 바뀌는” reference다. Reuters는 한국 정부가 dog-meat ban 시행 전 거의 half a million dogs를 rehome하고, dog breeders/farmers/restaurants 폐업을 돕기 위해 약 100B won, $75M를 투입하며, surrendered dog당 최대 600,000 won을 지급한다고 보도했다. 이건 animal welfare, shelter, vet, pet-care, pet-food 수요의 Stage2 policy reference다. 그러나 stock-specific price anchor가 없고, 농가 반발·보호소 capacity·입양수요가 모두 gate라서 Green은 금지한다. ([Reuters][5])

```json
{
  "case_id": "r12_loop16_dog_meat_ban_pet_welfare_transition",
  "symbols": "pet_food_vet_shelter_basket/policy_reference",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2_pet_welfare_policy_reference",
  "law_passed_context": "2024-01",
  "ban_effective": "early_2027",
  "incentive_plan_date": "2024-09-26",
  "government_incentives_krw_bn": 100,
  "government_incentives_usd_mn": 75,
  "max_payment_per_dog_krw": 600000,
  "dogs_to_rehome_context": "nearly_500000",
  "direct_listed_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "listed_pet_food_sales",
    "vet_service_revenue",
    "shelter_capacity",
    "adoption_rate",
    "farmer_transition_success",
    "subsidy_execution"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "pet_welfare_policy_stage2_reference_not_Green"
}
```

---

## Case F — CSAT / education-service demand

```text
symbols = education_service_basket / online_education / publishing_reference
case_type = Stage2 education-demand reference
archetype = EDUCATION_EXAM_DEMAND_STAGE2_NO_PRICE
```

| trigger |          type | date       | 당시 공개 evidence                                                                                         | 가격 anchor      | outcome |
| ------- | ------------: | ---------- | ------------------------------------------------------------------------------------------------------ | -------------- | ------- |
| T0      | Stage2 demand | 2025-11-13 | 554,174 CSAT applicants, +6% YoY, highest since 2019                                                   | no stock price |         |
| T1      |    validation | 2025-11-13 | financial markets/offices opened one hour later; 140 flights affected by listening section restriction | no price       |         |
| T2      |      4B-watch | 2025       | cohort spike from 2007 birth surge, not necessarily structural long-term demand                        | 4B             |         |
| T3      | Stage3-Yellow | N/A        | listed education revenue/ARPU not confirmed                                                            | no Yellow      |         |

CSAT case는 R12 교육서비스 demand reference다. Reuters는 2025년 CSAT registration이 554,174명으로 전년 대비 +6%, 2019년 이후 최고였다고 보도했다. 시험시간에는 35분간 모든 공항의 이착륙이 제한되어 140 flights가 영향을 받았고, 금융시장과 직장 출근시간도 1시간 늦춰졌다. 이것은 한국 교육서비스 수요의 강도를 보여주는 Stage2 demand signal이다. 다만 2007년 출생아 spike에 따른 cohort effect가 있어 구조적 Stage3로 올리려면 학원·온라인교육·출판사의 실제 매출/ARPU가 필요하다. ([Reuters][6])

```json
{
  "case_id": "r12_loop16_csat_education_service_demand",
  "symbols": "education_service_basket/online_education/publishing_reference",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage2_education_demand_reference",
  "trigger_date": "2025-11-13",
  "csat_registered_applicants": 554174,
  "csat_applicants_yoy_pct": 6,
  "highest_since": 2019,
  "flight_restriction_minutes": 35,
  "affected_flights": 140,
  "market_office_open_delay_hours": 1,
  "direct_listed_price_anchor": "price_data_unavailable_after_deep_search",
  "4B_overlay": [
    "cohort_spike_from_2007_births",
    "long_term_low_birthrate",
    "education_regulation",
    "household_affordability"
  ],
  "stage3_gate_missing": [
    "listed_education_revenue",
    "ARPU",
    "online_conversion",
    "margin",
    "repeat_enrollment"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "education_demand_stage2_reference_not_Green"
}
```

---

## Case G — Birthrate rebound / childcare and baby-service pipeline

```text
symbols = childcare_basket / baby_goods / education_pipeline_reference
case_type = demographic Stage2 reference
archetype = FERTILITY_CHILDCARE_POLICY_STAGE2_NO_PRICE
```

| trigger |               type | date       | 당시 공개 evidence                                                                                           | 가격 anchor      | outcome |
| ------- | -----------------: | ---------- | -------------------------------------------------------------------------------------------------------- | -------------- | ------- |
| T0      | Stage2 demographic | 2026-02-25 | 2025 fertility rate rose to 0.80 from 0.75 in 2024; second consecutive yearly rise                       | no stock price |         |
| T1      |         validation | 2026-02-25 | births +6.8%, marriages +8.1%; Seoul fertility +8.9%                                                     | no price       |         |
| T2      |  policy validation | 2026       | administration plans five-year demographic response plan, childbirth incentives, skilled foreign workers | no price       |         |
| T3      |           4B-watch | 2026       | still world’s lowest birthrate, population continues to decline                                          | 4B             |         |
| T4      |      Stage3-Yellow | N/A        | listed childcare/baby revenue conversion not confirmed                                                   | no Yellow      |         |

Birthrate rebound는 R12에서 가장 조심해야 할 demographic Stage2다. Reuters는 한국의 2025 total fertility rate가 2024년 0.75에서 0.80으로 올랐고, births는 +6.8%, marriages는 +8.1%였다고 보도했다. Seoul fertility도 +8.9%였다. 정부는 five-year demographic response plan, childbirth incentives, skilled foreign worker recruitment를 준비한다고 했다. 하지만 여전히 세계 최저권이고 인구 감소는 이어진다. 그래서 childcare/baby goods/education pipeline에는 Stage2 reference지만, “출산율 반등 = 아동주 Green”으로 바로 올리면 false positive다. ([Reuters][7])

```json
{
  "case_id": "r12_loop16_birthrate_childcare_pipeline",
  "symbols": "childcare_basket/baby_goods/education_pipeline_reference",
  "best_trigger": "T0/T3",
  "best_trigger_type": "Stage2_demographic_reference_with_4B_durability_gate",
  "trigger_date": "2026-02-25",
  "fertility_rate_2025": 0.80,
  "fertility_rate_2024": 0.75,
  "births_2025_yoy_pct": 6.8,
  "marriages_2025_yoy_pct": 8.1,
  "seoul_fertility_increase_pct": 8.9,
  "policy_plans": [
    "five_year_demographic_response_plan",
    "childbirth_incentives",
    "skilled_foreign_worker_recruitment"
  ],
  "direct_listed_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "listed_childcare_revenue",
    "baby_goods_sales",
    "daycare_enrollment",
    "education_pipeline_conversion",
    "policy_budget_execution",
    "multi_year_birthrate_durability"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "demographic_stage2_reference_not_Green"
}
```

---

## Case H — Medical education quota freeze / service disruption relief

```text
symbols = medical_education_reference / hospital_service_reference / education_policy
case_type = 4B policy relief
archetype = MEDICAL_EDUCATION_QUOTA_POLICY_4B_RELIEF
```

| trigger |                  type | date         | 당시 공개 evidence                                                                     | 가격 anchor      | outcome |
| ------- | --------------------: | ------------ | ---------------------------------------------------------------------------------- | -------------- | ------- |
| T0      | 4B service disruption | 2024-02~2025 | trainee doctors’ walkout, surgeries/emergency care delays                          | no stock price |         |
| T1      |        relief trigger | 2025-03-07   | education ministry offered to freeze new medical students at around 3,000 annually | no price       |         |
| T2      |            validation | 2025-03-07   | 90% of trainee doctors resigned/walked out context; trust restoration emphasized   | no price       |         |
| T3      |         Stage3-Yellow | N/A          | service normalization, trainee return, hospital margin not confirmed               | no Yellow      |         |

Medical education quota는 R7 healthcare와도 겹치지만, R12에서는 “교육·생활서비스 disruption relief”로 본다. Reuters는 South Korea’s education ministry가 13개월간 이어진 trainee-doctor dispute를 해결하기 위해 new medical student numbers를 약 3,000명 수준으로 freeze하겠다고 제안했다고 보도했다. Thousands of trainee doctors had walked off, and the dispute caused emergency-care stress and surgery delays. 이건 생활서비스 안정 관점에서 relief trigger지만, 병원·교육서비스 상장사 가격 anchor와 service normalization이 없으므로 Stage3가 아니다. ([Reuters][8])

```json
{
  "case_id": "r12_loop16_medical_education_quota_freeze",
  "symbols": "medical_education_reference/hospital_service_reference/education_policy",
  "best_trigger": "T1/T3",
  "best_trigger_type": "4B_service_disruption_relief",
  "relief_trigger_date": "2025-03-07",
  "proposed_medical_student_number": "about_3000_annually",
  "dispute_duration_months": 13,
  "trainee_doctor_walkout_context_pct": 90,
  "service_disruption_channels": [
    "emergency_care_stress",
    "surgery_delay",
    "medical_student_boycott",
    "trust_breakdown"
  ],
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "trainee_doctor_return",
    "hospital_service_normalization",
    "medical_school_schedule_normalization",
    "hospital_revenue_recovery",
    "policy_consensus"
  ],
  "trigger_outcome_label": "medical_education_service_relief_not_Green"
}
```

---

# 6. Trigger별 가격경로 검증 요약

| case                      | best trigger |        entry anchor |                                   event MFE/MAE | market-relative | full MFE/MAE | outcome                      |
| ------------------------- | ------------ | ------------------: | ----------------------------------------------: | --------------: | ------------ | ---------------------------- |
| Baemin / Naver / Uber     | T1/T3        | Delivery Hero proxy |          Delivery Hero +5.6%, Naver unavailable |     unavailable | unavailable  | Stage2 M&A + 4B              |
| Coupang everyday delivery | T0/T3        |          CPNG proxy | Coupang -34%; Naver users +23%; CJ volume +120% |     unavailable | unavailable  | hard 4C + rival Stage2       |
| Food-price inflation      | T0/T2        |    policy/inflation |                                  no stock price |             N/A | unavailable  | Stage2 policy + margin 4B    |
| Feed wheat tender         | T0/T2        |         cost/tender |                                  no stock price |             N/A | unavailable  | feed-cost 4B                 |
| Dog-meat ban / pet        | T1/T3        |       policy budget |                                  no stock price |             N/A | unavailable  | Stage2 policy reference      |
| CSAT / education          | T0/T2        |         demand data |                                  no stock price |             N/A | unavailable  | Stage2 demand reference      |
| Birthrate / childcare     | T0/T3        |    demographic data |                                  no stock price |             N/A | unavailable  | Stage2 demographic reference |
| Medical education quota   | T1/T3        |       policy relief |                                  no stock price |             N/A | unavailable  | 4B relief                    |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
좋은 Stage2:
- Baemin / Naver / Uber: platform M&A scale is large, but approval and economics missing.
- Coupang rival shift: user/spending data and logistics-volume data are strong.
- Food-price policy relief: living-cost policy is real, but margin effect mixed.
- Birthrate rebound: demographic signal improved, but trend durability missing.

약한 Stage2:
- Dog-meat ban: policy and budget are real, but listed beneficiary unclear.
- CSAT demand: applicant spike is real, but cohort effect and no listed-price anchor.
- Medical quota freeze: service relief, not investible Green.
```

## Stage2-Actionable entry 성과

```text
Actionable:
- Coupang breach as negative 4C and rival Stage2: user shift data is strong.
- Baemin M&A: deal size is strong, but Naver price/approval missing.
- Delivery Hero proxy reaction +5.6% supports platform-M&A interest, but not 국장 direct.

Actionable 보류:
- Food-price policy: no stock-specific pass-through data.
- Feed wheat: cost shock only, no margin recovery.
- Dog-meat ban / pet: no listed revenue conversion.
- CSAT / birthrate: demand references only.
```

## Stage3-Yellow 후보

```text
Yellow 후보:
- Naver/Baemin if final contract, approval, GMV, take-rate and Naver economics are confirmed.
- Naver/E-Mart/CJ Logistics if Coupang user leakage converts into GMV/revenue/margin.
- Food-price beneficiaries if import quotas and retail reform restore margins without volume loss.
- Childcare/baby/education names if birth rebound persists and listed revenue conversion appears.
```

## Stage3-Green

```text
이번 R12 Loop 16에서 확정 Green 없음.

이유:
- R12는 policy/reference signals가 많고 상장사 직접 가격 anchor가 부족하다.
- Baemin M&A는 final decision/approval 전이다.
- Food-price policy는 소비자에는 relief지만 기업에는 margin squeeze가 될 수 있다.
- Feed wheat는 cost 4B일 뿐 upside trigger가 아니다.
- Dog-meat ban, CSAT, birthrate, medical quota는 listed-company revenue conversion이 없다.
```

---

# 8. score-price alignment 판정

```text
aligned:
- Coupang security hard 4C and rival delivery Stage2
- Baemin platform-M&A as Stage2, using Delivery Hero proxy
- Food-price inflation as margin/policy 4B
- Feed wheat tender failure as feed-cost 4B

Stage2_promote_candidate:
- Baemin/Naver if final deal and approval appear
- Naver/E-Mart/CJ Logistics if delivery user shift converts to revenue
- childcare/education names only if demographic data converts to listed revenue

evidence_good_but_price_failed_or_unavailable:
- dog-meat ban / pet transition
- CSAT / education demand
- birthrate rebound / childcare
- medical education quota freeze
- food-price policy for listed names

event_premium:
- Baemin takeover headline
- birthrate rebound theme
- pet welfare policy theme

thesis_break_watch:
- Coupang data/security trust
- food-price inflation and weak won
- feed wheat cost shock
- medical education service disruption

hard_4C_success:
- Coupang breach, already validated through stock/user/spending data
```

---

# 9. 점수비중 교정

## 올릴 축

```csv
axis,delta,reason,cases
platform_MA_final_approval,+5,"생활서비스 M&A는 final SPA와 승인 전에는 Green 금지","Baemin/Naver/Uber"
delivery_GMV_take_rate_conversion,+5,"user shift는 GMV/take-rate/margin으로 확인돼야 Yellow","Coupang rivals"
consumer_trust_security,+5,"생활배송 platform은 data breach가 hard gate","Coupang"
food_price_pass_through,+5,"식품/외식은 원가 상승을 가격에 전가해야 Yellow","food basket"
import_quota_margin_relief,+4,"정부 import quota는 실제 원가 안정으로 연결돼야 함","food inflation case"
feed_cost_sensitivity,+5,"사료 원가는 축산/feed basket 4B 핵심","feed wheat"
pet_welfare_revenue_conversion,+4,"동물복지 정책은 pet-care/vet/pet-food 매출 전환 필요","dog meat ban"
education_demand_ARPU,+4,"응시자 수는 교육서비스 매출/ARPU로 확인해야 함","CSAT"
fertility_trend_durability,+4,"출산율 반등은 다년 지속성과 서비스 매출 전환 필요","birthrate"
service_disruption_normalization,+4,"의료교육/생활서비스는 정상화 지표가 필요","medical quota"
```

## 내릴 축

```csv
axis,delta,reason,cases
M&A_headline_without_approval,-5,"인수설/teaser만으로 Stage3 금지","Baemin/Naver/Uber"
user_shift_without_revenue,-5,"MAU 변화만으로 Green 금지","Naver/E-Mart/CJ"
food_policy_without_company_margin,-5,"식품가격 안정책이 기업 margin 개선이라는 보장 없음","food inflation"
commodity_cost_ignored,-5,"feed wheat/corn/soy shock 무시하면 false positive","feed/livestock"
pet_policy_without_listed_beneficiary,-4,"동물복지 정책을 pet stock 자동수혜로 처리 금지","dog meat ban"
education_cohort_spike_without_revenue,-4,"수능 응시자 spike는 구조적 교육주 Green 아님","CSAT"
birthrate_rebound_one_year,-5,"1~2년 출산율 반등만으로 baby/childcare Green 금지","birthrate"
medical_policy_relief_without_service_data,-4,"의대정원 완화만으로 병원/교육서비스 정상화 판단 금지","medical quota"
```

---

# 10. Stage2-Actionable 승격 조건

R12 Loop 16 shadow rule:

```text
R12에서 Stage2 evidence가 아래 중 3개 이상이면 Stage2-Actionable로 승격한다.

1. final M&A / approval / financing이 확인된다.
2. event return이 +5% 이상이다.
3. user shift가 GMV, spending, shipment, margin 중 하나로 연결된다.
4. food/agri policy가 실제 cost decline or margin recovery로 연결된다.
5. demographic or education demand가 listed revenue/ARPU로 연결된다.
6. pet/welfare policy가 listed pet-food/vet/service revenue로 연결된다.
7. data breach, commodity-cost shock, regulatory backlash 4B/4C가 없다.
```

적용:

```text
Baemin/Naver/Uber:
1 없음, 2는 Delivery Hero proxy만 있음 → Stage2, Actionable 보류.

Coupang rivals:
3 일부 충족: Naver users +23%, CJ volume +120%. 하지만 listed margin 미확인 → Stage2 rival opportunity.

Food inflation:
4 미충족. 정책은 있지만 company margin unknown → Stage2/4B.

Feed wheat:
cost shock only → 4B.

Dog-meat ban / pet:
6 미충족 → Stage2 reference only.

CSAT/birthrate:
5 미충족 → Stage2 demand reference only.
```

---

# 11. Stage3-Yellow 조건

```text
Stage3-Yellow:
- Stage2 signal 이후 EPS/OP/FCF 경로 변화 가능성이 높아짐.
- 하지만 approval, revenue conversion, margin, durability 중 하나가 남은 상태.
```

Yellow 후보:

```text
Baemin / Naver:
final deal, approval, Naver GMV/take-rate economics 확인 시 Yellow.

Naver/E-Mart/CJ Logistics:
Coupang leakage가 actual GMV, spending, shipment margin으로 연결되면 Yellow.

Food-price beneficiaries:
import quotas and distribution reform이 gross margin recovery로 연결되면 Yellow.

Childcare/education:
birthrate or CSAT demand가 listed revenue/ARPU로 확인되면 Yellow.

Pet-care:
dog-meat ban 이후 adoption/shelter/vet/pet-food 매출이 listed names에 잡히면 Yellow.
```

---

# 12. Stage3-Green 조건

```text
Stage3-Green:
- 생활서비스 M&A가 final approval을 받고 GMV/take-rate/margin으로 연결된다.
- user shift가 revenue and profit으로 확인된다.
- food/agri cost shock가 완화되고 price pass-through가 성공한다.
- education/birthrate/pet policy가 listed-company revenue로 전환된다.
- commodity-cost, data breach, regulation, subsidy execution 4B가 없다.
- full-window MFE/MAE가 favorable하다.
```

이번 R12 Loop 16에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
reason = full OHLC unavailable + approval/revenue/margin/durability gates not fully closed
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- food-delivery M&A headline before final decision.
- user/MAU shift before revenue and margin conversion.
- food-price policy before company margin recovery.
- feed wheat/corn cost spike before pass-through.
- demographic rebound before multi-year durability.
- pet welfare law before listed beneficiary appears.
- education cohort spike before revenue/ARPU.
- medical quota freeze before service normalization.
```

적용:

```text
Baemin:
M&A headline 4B until final SPA and approval.

Coupang rivals:
rival Stage2, but user shift must become revenue.

Food inflation:
consumer relief may become producer/restaurant margin pressure.

Feed wheat:
pure cost 4B.

Dog-meat ban:
policy reference, no listed beneficiary.

CSAT/birthrate:
demand reference, not stock-specific Green.

Medical quota:
relief signal, but service normalization required.
```

---

# 14. 4C hard gate 조건

```text
R12 4C:
- major data breach in everyday service platform
- food-price shock causing volume decline and margin squeeze
- commodity-cost spike without pass-through
- failed M&A / antitrust rejection
- subsidy execution failure
- service-system disruption such as medical/education crisis
```

이번 R12 Loop 16 hard 4C:

```text
Coupang data breach = hard_4C_success
```

Strong 4C-watch:

```text
- feed wheat cost shock
- food-price inflation / weak won
- Baemin deal approval failure
- medical education service disruption
- pet shelter capacity failure after dog-meat ban
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

R12 production 설계 원칙:

```text
1. 생활서비스 M&A headline과 final approval/economics를 분리한다.
2. MAU/user shift와 GMV/spending/margin conversion을 분리한다.
3. food-price policy와 company margin recovery를 분리한다.
4. feed/agri commodity cost shock는 4B로 따로 둔다.
5. demographic/education/pet policy는 listed-company revenue conversion 전까지 reference로만 둔다.
6. data breach는 everyday-service platform hard 4C로 즉시 차감한다.
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_248.md 요약

```md
# R12 Loop 16. Agriculture / Life Services / Misc Trigger-level Price Validation

이번 라운드는 R12 Loop 16 trigger-level validation 라운드다.

핵심 결론:
- Baemin / Naver / Uber is Stage2 food-delivery M&A. Uber and Naver formed a consortium to bid up to 8T won / $5.34B for Baemin, with an 80:20 Uber/Naver structure. Naver confirmed it received a teaser letter but said no final decision had been made. Delivery Hero shares rose 5.6% after Uber increased its Delivery Hero stake to 19.5%, but Naver direct price and deal approval are unavailable.
- Coupang breach is hard 4C and rival everyday-delivery Stage2. Coupang shares fell around 34% since breach disclosure, MAU -3.5%, daily spending -6.3% to 139.2B won. Naver online users +23% and CJ Logistics overnight/one-day delivery volume +120%.
- Food-price inflation is Stage2 policy relief plus margin 4B. CPI was +2.4% YoY in Nov 2025; agricultural/fishery prices +5.6%, rice +18.6%, mandarins +26.5%. Government food-price support and import quotas are relief, but company pass-through is unconfirmed.
- Feed wheat tender failure is 4B cost shock. South Korea’s FLC made no purchase in a 65,000t feed wheat tender because offers were too high; lowest offer was around $298.50/t c&f plus $2/t surcharge.
- Dog-meat ban / pet welfare transition is Stage2 policy reference. Government plans around 100B won / $75M incentives and up to 600,000 won per surrendered dog, with nearly half a million dogs needing rehoming. Listed pet revenue conversion is unavailable.
- CSAT / education services is Stage2 demand reference. 554,174 applicants, +6% YoY and highest since 2019, but no listed education revenue/ARPU anchor.
- Birthrate rebound / childcare is Stage2 demographic reference. Fertility rose to 0.80 in 2025 from 0.75 in 2024; births +6.8%, marriages +8.1%. Multi-year durability and listed revenue conversion are missing.
- Medical education quota freeze is service-disruption relief. Education ministry proposed freezing medical students at about 3,000 annually to resolve the 13-month dispute. Service normalization is not yet confirmed.

Main calibration:
- Raise platform_MA_final_approval, delivery_GMV_take_rate_conversion, consumer_trust_security, food_price_pass_through, import_quota_margin_relief, feed_cost_sensitivity, pet_welfare_revenue_conversion, education_demand_ARPU, fertility_trend_durability, service_disruption_normalization.
- Lower M&A_headline_without_approval, user_shift_without_revenue, food_policy_without_company_margin, commodity_cost_ignored, pet_policy_without_listed_beneficiary, education_cohort_spike_without_revenue, birthrate_rebound_one_year, medical_policy_relief_without_service_data.
```

## docs/checkpoints/checkpoint_28a_round248_r12_loop16.md 요약

```md
# Checkpoint 28A Round 248 R12 Loop 16 Trigger-level Calibration

## 반영 내용
- R12 Loop 16 trigger-level validation을 수행했다.
- Baemin/Naver/Uber, Coupang everyday delivery share shift, food-price inflation/import quotas, feed wheat cost shock, dog-meat ban/pet welfare, CSAT education demand, birthrate/childcare, medical education quota freeze를 검토했다.
- full adjusted OHLC window는 확보하지 못했으므로 Reuters / AP의 reported event return, user metrics, policy budget, food price and tender anchors를 사용했다.
- OHLC 미확보를 이유로 Stage 후보를 강등하지 않고, price_data_unavailable_after_deep_search로 분리 기록했다.

## 핵심 보정
- Lifestyle service M&A is Stage2 until final approval, financing and economics are closed.
- User shift is not Green unless it converts into GMV, spending, shipment and margin.
- Food/agri inflation policy is relief for consumers but may be margin 4B for companies.
- Feed wheat/corn/soy cost shocks require pass-through proof.
- Pet, education and childcare policy/demand signals are only references until listed revenue appears.
- Everyday-service data breach is hard 4C.
```

## data/e2r_case_library/cases_r12_loop16_round248.jsonl 초안

```jsonl
{"case_id":"r12_loop16_baemin_naver_uber_food_delivery_ma","symbol":"035420/UBER/Delivery_Hero_readthrough","company_name":"Naver / Uber / Baemin / Delivery Hero","case_type":"Stage2_platform_MA_with_approval_4B","primary_archetype":"FOOD_DELIVERY_PLATFORM_MA_STAGE2_WITH_APPROVAL_4B","best_trigger":"T1/T3","stage_candidate":"Stage2","price_validation":{"trigger_date":"2026-05-18","baemin_bid_value_krw_trn":8.0,"baemin_bid_value_usd_bn":5.34,"consortium_ratio":"Uber_80pct_Naver_20pct","naver_decision_status":"teaser_letter_received_no_final_decision","uber_delivery_hero_stake_pct":19.5,"delivery_hero_stake_value_eur_bn":1.7,"delivery_hero_event_return_pct":5.6,"direct_naver_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_MA_not_Green","notes":"Large lifestyle-platform M&A trigger, but final approval and Naver economics are missing."}
{"case_id":"r12_loop16_coupang_everyday_delivery_share_shift","symbol":"CPNG/035420/139480/000120/Kurly_private","company_name":"Coupang / Naver / E-Mart / CJ Logistics / Kurly","case_type":"hard_4C_plus_rival_Stage2","primary_archetype":"EVERYDAY_DELIVERY_SHARE_SHIFT_STAGE2_WITH_SECURITY_4C","best_trigger":"T0/T3","stage_candidate":"4C + Stage2 rival opportunity","price_validation":{"affected_users_mn":"33_to_34","coupang_return_since_breach_pct":-34,"mobile_mau_change_pct":-3.5,"daily_spending_change_pct":-6.3,"daily_spending_jan_krw_bn":139.2,"naver_online_users_change_pct":23,"cj_logistics_overnight_one_day_volume_yoy_q4_pct":120,"rival_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"hard_4C_with_rival_Stage2","notes":"Coupang trust break creates rival opportunity, but rival revenue/margin conversion is not confirmed."}
{"case_id":"r12_loop16_food_price_inflation_import_quota","symbol":"food_processor_basket/restaurant_basket/grocer_basket","company_name":"Food processors / restaurants / grocers basket","case_type":"Stage2_policy_relief_with_margin_4B","primary_archetype":"FOOD_PRICE_INFLATION_IMPORT_QUOTA_STAGE2_4B","best_trigger":"T0/T2","stage_candidate":"Stage2 + 4B-watch","price_validation":{"headline_cpi_yoy_pct":2.4,"agri_fishery_price_yoy_pct":5.6,"rice_price_yoy_pct":18.6,"mandarin_price_yoy_pct":26.5,"supplementary_budget_date":"2025-06-16","policy_measures":["food_price_burden_support","import_quota_increases","oil_tax_break_extension"],"direct_stock_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"food_price_policy_stage2_with_margin_4B","notes":"Food-price relief is real but company margin/pass-through is unconfirmed."}
{"case_id":"r12_loop16_feed_wheat_cost_shock","symbol":"136480/027740/088910/003380/feed_livestock_basket","company_name":"Harim / Farmsco / Easy Bio / feed-livestock basket","case_type":"4B_feed_cost_shock","primary_archetype":"FEED_WHEAT_COST_SHOCK_4B","best_trigger":"T0/T2","stage_candidate":"4B-watch","price_validation":{"trigger_date":"2026-05-13","tender_volume_tons":65000,"purchase_result":"believed_no_purchase","lowest_offer_usd_per_ton_cf":298.50,"additional_unloading_surcharge_usd_per_ton":2.00,"direct_feed_stock_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"cost_4B_not_actionable","notes":"High feed wheat prices are a cost shock until pass-through or relief is proven."}
{"case_id":"r12_loop16_dog_meat_ban_pet_welfare_transition","symbol":"pet_food_vet_shelter_basket/policy_reference","company_name":"Pet welfare / pet food / vet service reference","case_type":"Stage2_pet_welfare_policy_reference","primary_archetype":"PET_WELFARE_POLICY_TRANSITION_STAGE2_NO_PRICE","best_trigger":"T1/T3","stage_candidate":"Stage2 reference","price_validation":{"ban_effective":"early_2027","government_incentives_krw_bn":100,"government_incentives_usd_mn":75,"max_payment_per_dog_krw":600000,"dogs_to_rehome_context":"nearly_500000","direct_listed_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"policy_reference_not_Green","notes":"Pet-welfare transition is policy Stage2, but listed pet-care revenue conversion is missing."}
{"case_id":"r12_loop16_csat_education_service_demand","symbol":"education_service_basket/online_education/publishing_reference","company_name":"Education services / online education / publishing reference","case_type":"Stage2_education_demand_reference","primary_archetype":"EDUCATION_EXAM_DEMAND_STAGE2_NO_PRICE","best_trigger":"T0/T2","stage_candidate":"Stage2 reference","price_validation":{"trigger_date":"2025-11-13","csat_registered_applicants":554174,"csat_applicants_yoy_pct":6,"highest_since":2019,"flight_restriction_minutes":35,"affected_flights":140,"direct_listed_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"demand_reference_not_Green","notes":"CSAT demand spike is real, but listed education revenue/ARPU and cohort durability are missing."}
{"case_id":"r12_loop16_birthrate_childcare_pipeline","symbol":"childcare_basket/baby_goods/education_pipeline_reference","company_name":"Childcare / baby goods / education pipeline reference","case_type":"Stage2_demographic_reference_with_4B_durability_gate","primary_archetype":"FERTILITY_CHILDCARE_POLICY_STAGE2_NO_PRICE","best_trigger":"T0/T3","stage_candidate":"Stage2 reference","price_validation":{"trigger_date":"2026-02-25","fertility_rate_2025":0.80,"fertility_rate_2024":0.75,"births_2025_yoy_pct":6.8,"marriages_2025_yoy_pct":8.1,"seoul_fertility_increase_pct":8.9,"direct_listed_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"demographic_reference_not_Green","notes":"Birthrate rebound is Stage2 reference, but multi-year durability and listed revenue conversion are missing."}
{"case_id":"r12_loop16_medical_education_quota_freeze","symbol":"medical_education_reference/hospital_service_reference/education_policy","company_name":"Medical education / hospital service reference","case_type":"4B_service_disruption_relief","primary_archetype":"MEDICAL_EDUCATION_QUOTA_POLICY_4B_RELIEF","best_trigger":"T1/T3","stage_candidate":"relief reference","price_validation":{"relief_trigger_date":"2025-03-07","proposed_medical_student_number":"about_3000_annually","dispute_duration_months":13,"trainee_doctor_walkout_context_pct":90,"direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"service_relief_not_Green","notes":"Quota freeze is service-disruption relief, not investible Stage3 until service normalization is proven."}
```

## data/e2r_trigger_calibration/triggers_r12_loop16_round248.jsonl 초안

```jsonl
{"trigger_id":"r12l16_baemin_naver_uber_T1","case_id":"r12_loop16_baemin_naver_uber_food_delivery_ma","trigger_type":"Stage2_platform_MA","trigger_date":"2026-05-18","evidence_available":"Uber and Naver consortium reportedly bid up to 8T won / $5.34B for Baemin; Naver confirmed teaser letter but no final decision; Delivery Hero +5.6% after Uber increased stake","event_return_pct":"Delivery_Hero_proxy_+5.6","trigger_outcome_label":"Stage2_food_delivery_MA_not_Green","promote_to":"Stage2"}
{"trigger_id":"r12l16_coupang_delivery_shift_T0","case_id":"r12_loop16_coupang_everyday_delivery_share_shift","trigger_type":"hard_4C_plus_rival_Stage2","trigger_date":"2025-11_to_2026-02-25","evidence_available":"Coupang shares around -34% since breach, MAU -3.5%, spending -6.3%; Naver users +23%; CJ Logistics overnight/one-day volume +120%","event_return_pct":"Coupang_-34_context","trigger_outcome_label":"everyday_delivery_security_4C_with_rival_stage2","promote_to":"4C+Stage2"}
{"trigger_id":"r12l16_food_price_inflation_T0","case_id":"r12_loop16_food_price_inflation_import_quota","trigger_type":"Stage2_policy_relief_with_margin_4B","trigger_date":"2025-06_to_2025-12","evidence_available":"CPI +2.4%, agricultural/fishery +5.6%, rice +18.6%, mandarins +26.5%; second supplementary budget included food-price burden support and import quota increases","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"food_price_policy_stage2_with_margin_4B","promote_to":"Stage2+4B"}
{"trigger_id":"r12l16_feed_wheat_T0","case_id":"r12_loop16_feed_wheat_cost_shock","trigger_type":"4B_feed_cost_shock","trigger_date":"2026-05-13","evidence_available":"South Korea FLC believed to make no purchase in 65,000t feed wheat tender because prices were too high; lowest offer around $298.50/t plus $2/t surcharge","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"feed_cost_4B","promote_to":"4B-watch"}
{"trigger_id":"r12l16_dog_meat_pet_T1","case_id":"r12_loop16_dog_meat_ban_pet_welfare_transition","trigger_type":"Stage2_pet_welfare_policy","trigger_date":"2024-09-26","evidence_available":"Government to spend around 100B won / $75M incentives, pay up to 600,000 won per surrendered dog, and rehome nearly half a million dogs before 2027 dog-meat ban","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"pet_welfare_policy_reference_not_Green","promote_to":"Stage2_reference"}
{"trigger_id":"r12l16_csat_education_T0","case_id":"r12_loop16_csat_education_service_demand","trigger_type":"Stage2_education_demand_reference","trigger_date":"2025-11-13","evidence_available":"554,174 CSAT applicants, +6% YoY and highest since 2019; 140 flights affected by listening-section flight restrictions","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"education_demand_reference_not_Green","promote_to":"Stage2_reference"}
{"trigger_id":"r12l16_birthrate_childcare_T0","case_id":"r12_loop16_birthrate_childcare_pipeline","trigger_type":"Stage2_demographic_reference","trigger_date":"2026-02-25","evidence_available":"Total fertility rate rose to 0.80 in 2025 from 0.75 in 2024; births +6.8%, marriages +8.1%; government plans demographic response and childbirth incentives","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"demographic_stage2_reference_not_Green","promote_to":"Stage2_reference"}
{"trigger_id":"r12l16_medical_quota_relief_T1","case_id":"r12_loop16_medical_education_quota_freeze","trigger_type":"4B_service_disruption_relief","trigger_date":"2025-03-07","evidence_available":"Education ministry offered to freeze new medical students at about 3,000 annually to resolve 13-month dispute after trainee doctor walkout disrupted services","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"medical_education_service_relief_not_Green","promote_to":"relief_reference"}
```

## data/sector_taxonomy/score_weight_profiles_round248_r12_loop16_v1.csv 초안

```csv
archetype,platform_ma_final_approval,delivery_gmv_take_rate_conversion,consumer_trust_security,food_price_pass_through,import_quota_margin_relief,feed_cost_sensitivity,pet_welfare_revenue_conversion,education_demand_arpu,fertility_trend_durability,service_disruption_normalization,ma_headline_without_approval_penalty,user_shift_without_revenue_penalty,food_policy_without_company_margin_penalty,commodity_cost_ignored_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
FOOD_DELIVERY_PLATFORM_MA_STAGE2_WITH_APPROVAL_4B,+5,+5,+3,+0,+0,+0,+0,+0,+0,+1,-5,-4,-1,-1,large Baemin bid,approval/economics missing,final SPA+approval+GMV/take-rate,Baemin/Naver/Uber.
EVERYDAY_DELIVERY_SHARE_SHIFT_STAGE2_WITH_SECURITY_4C,+1,+5,+5,+0,+0,+0,+0,+0,+0,+2,-1,-5,-1,-1,Coupang trust break and rival metrics,revenue/margin conversion missing,rival GMV+shipment margin,Coupang/Naver/CJ.
FOOD_PRICE_INFLATION_IMPORT_QUOTA_STAGE2_4B,+0,+0,+1,+5,+4,+3,+0,+0,+0,+0,-1,-1,-5,-3,food-price policy relief,company margin missing,pass-through+margin recovery,food/restaurant basket.
FEED_WHEAT_COST_SHOCK_4B,+0,+0,+0,+3,+1,+5,+0,+0,+0,+0,-1,-1,-2,-5,feed wheat tender failure,pass-through missing,feed margin recovery+livestock price,feed/livestock basket.
PET_WELFARE_POLICY_TRANSITION_STAGE2_NO_PRICE,+0,+0,+1,+0,+0,+0,+5,+0,+1,+1,-1,-1,-1,-1,dog-meat ban and pet transition,listed beneficiary missing,pet-food/vet/shelter revenue,dog-meat ban.
EDUCATION_EXAM_DEMAND_STAGE2_NO_PRICE,+0,+0,+0,+0,+0,+0,+0,+5,+2,+0,-1,-1,-1,-1,CSAT applicant spike,listed revenue/ARPU missing,education revenue+margin,CSAT.
FERTILITY_CHILDCARE_POLICY_STAGE2_NO_PRICE,+0,+0,+0,+0,+0,+0,+1,+3,+5,+0,-1,-1,-1,-1,birthrate rebound,trend and listed revenue missing,multi-year fertility+childcare revenue,birthrate.
MEDICAL_EDUCATION_QUOTA_POLICY_4B_RELIEF,+0,+0,+1,+0,+0,+0,+0,+3,+1,+5,-1,-1,-1,-1,quota freeze relief,service normalization missing,trainee return+hospital/education normalization,medical quota.
```

---

# 이번 R12 Loop 16 결론

```text
1. Baemin / Naver / Uber는 Stage2 food-delivery M&A다.
   8T won bid headline과 Delivery Hero +5.6% proxy reaction은 있지만, Naver 직접가격·final approval·economics가 없다.

2. Coupang everyday delivery case는 hard 4C + rival Stage2다.
   Coupang -34%, MAU -3.5%, spending -6.3%, Naver users +23%, CJ delivery volume +120%가 닫혔다.

3. Food-price inflation은 Stage2 policy relief + company margin 4B다.
   rice +18.6%, mandarins +26.5%는 생활비 shock이고, import quota는 relief지만 company margin은 따로 봐야 한다.

4. Feed wheat tender failure는 feed/livestock 4B다.
   65,000t tender no-purchase와 $298.50/t offer는 원가 shock이지 entry trigger가 아니다.

5. Dog-meat ban / pet transition은 Stage2 policy reference다.
   100B won incentives와 nearly 500k dogs rehoming은 크지만 listed beneficiary가 없다.

6. CSAT / education demand는 Stage2 reference다.
   554,174 applicants, +6%, highest since 2019지만, listed education revenue/ARPU가 필요하다.

7. Birthrate rebound는 Stage2 demographic reference다.
   fertility 0.80, births +6.8%, marriages +8.1%는 의미 있지만, 다년 지속성과 매출 전환 전에는 Green이 아니다.

8. Medical education quota freeze는 service-disruption relief다.
   의대정원 동결 제안은 relief지만 trainee return and service normalization 전에는 투자 Stage3가 아니다.
```

한 문장으로 압축하면:

> **R12 Loop 16에서 배운 핵심은 “생활서비스·농업·교육·반려동물·출산 headline”이 아니라, final M&A approval, GMV/take-rate conversion, food-price pass-through, feed-cost absorption, listed pet-care revenue, education ARPU, fertility trend durability, medical-service normalization이 닫혀야 Stage3로 올릴 수 있다는 것이다. 반대로 M&A 인수설, 사용자 이동, 식품가격 안정책, 출산율 반등, 시험 응시자 증가, 동물복지 정책만으로는 4B/false positive가 되기 쉽다.**

[1]: https://www.reuters.com/world/asia-pacific/uber-naver-team-up-baemin-takeover-seoul-economic-daily-2026-05-18/?utm_source=chatgpt.com "Uber, Naver team up on Baemin takeover -Seoul Economic Daily"
[2]: https://www.reuters.com/world/asia-pacific/coupang-ceo-fails-appear-south-korean-parliamentary-hearing-data-breach-2025-12-17/?utm_source=chatgpt.com "Coupang CEO faces legal action for skipping South Korean hearing on data breach"
[3]: https://www.reuters.com/world/asia-pacific/south-korea-nov-headline-inflation-24-yy-expected-2025-12-01/?utm_source=chatgpt.com "South Korea headline inflation at 2.4% y/y, bolstering case for rate pause"
[4]: https://www.reuters.com/world/asia-pacific/south-koreas-flc-believed-make-no-purchase-65000-ton-feed-wheat-tender-traders-2026-05-13/?utm_source=chatgpt.com "South Korea's FLC believed to make no purchase in 65,000 ton feed wheat tender, traders say"
[5]: https://www.reuters.com/world/asia-pacific/south-korea-offers-incentives-adoptions-ahead-ban-farming-dogs-food-2024-09-26/?utm_source=chatgpt.com "South Korea offers incentives, adoptions ahead of ban on farming dogs for food"
[6]: https://www.reuters.com/world/asia-pacific/south-korea-bans-flights-500000-take-crucial-university-admission-test-2025-11-13/?utm_source=chatgpt.com "South Korea bans flights as 500,000 take crucial university admission test"
[7]: https://www.reuters.com/business/healthcare-pharmaceuticals/south-koreas-birthrate-worlds-lowest-rises-again-amid-signs-easing-demographic-2026-02-25/?utm_source=chatgpt.com "South Korea's birthrate, the world's lowest, rises again amid signs of easing demographic crisis"
[8]: https://www.reuters.com/world/asia-pacific/south-korea-prepared-freeze-new-medical-student-numbers-minister-says-2025-03-07/?utm_source=chatgpt.com "South Korea offers to freeze medical student numbers to resolve 13-month dispute"

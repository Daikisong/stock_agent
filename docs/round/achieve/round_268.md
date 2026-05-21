순서상 이번은 **R12 Loop 12 — 농업·생활서비스·기타 가격경로 검증 라운드**다.

```text
round = R12 Loop 12
round_id = round_196
large_sector = AGRI_LIFE_SERVICE_MISC
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = false
```

이번 R12 Loop 12는 지난 R12의 Coway·Kyochon·출산율·AI textbook만 반복하지 않고, **라면·K-food 수출, 김치 원재료 climate shock, 사료곡물 input cost, 의대정원 교육 이벤트, AI 교과서/교실 디바이스 정책 후퇴, 외국인 가사·돌봄 pilot, dog-meat ban/pet transition, celebrity food-service overheat**를 한 번에 비교한다.

---

# 1. 이번 라운드 대섹터

```text
R12 = 농업·생활서비스·기타
```

R12에서 Stage 3는 “생활필수품”, “정책 수혜”, “출산율 반등”, “교육정책”, “K-food”, “펫 전환”, “농산물 가격 상승”이라는 말이 아니다.

진짜 Stage 3는 **반복구매·유료전환·ARPU·가격전가·재고 품질·현금전환·원재료 pass-through·서비스 utilization**이 실제로 닫히는 순간이다.

---

# 2. 대상 canonical archetype

```text
K_FOOD_EXPORT_CAPACITY_RECURRING_CONSUMPTION
AGRI_FOOD_INPUT_COST_SHOCK
FEED_GRAIN_INPUT_COST_4C
EDUCATION_POLICY_MEDICAL_QUOTA_EVENT
EDTECH_POLICY_ROLLBACK_4C
CHILDCARE_FOREIGN_HELPER_POLICY_EVENT
PET_WELFARE_TRANSITION_POLICY_EVENT
FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM
```

---

# 3. deep sub-archetype

```text
K-food / 라면:
- Nongshim Shin Ramyun
- U.S. / Europe export
- 해외 생산능력 / Walmart·Costco 채널
- 해외 sell-through / ASP / capacity / China slowdown

김치·농산물:
- Daesang / CJ CheilJedang / kimchi processors
- napa cabbage heat shock
- cabbage national stock release
- Chinese kimchi price pressure

사료·축산:
- Harim / Maniker / Farm Story / feed-livestock basket
- feed wheat tender failure
- grain cost / FX / inventory / pass-through

교육:
- Megastudy / YBMNet / NE Neungyule / Woongjin Thinkbig basket
- medical-school quota
- AI textbook rollback
- classroom device ban
- paid enrollment / ARPU / repeat course

돌봄·출산:
- childcare / infant goods / care-service basket
- foreign housekeeper pilot
- fertility rebound
- utilization / margin / paid household demand

펫·동물복지:
- pet-food / shelter / care-service basket
- dog-meat ban transition
- subsidy / adoption / shelter capacity

생활서비스 이벤트:
- Kyochon F&B / Cherrybro / Neuromeka
- Jensen Huang fried-chicken event
- same-store sales / franchise margin / meme fade
```

---

# 4. 국장 신규 후보 case

## Case A — Nongshim `structural_success_candidate / K-food export capacity`

```text
symbol = 004370
case_type = structural_success_candidate
archetype = K_FOOD_EXPORT_CAPACITY_RECURRING_CONSUMPTION
```

### stage date

```text
Stage 1:
2023~2024
- Shin Ramyun global sales growth
- U.S. market penetration
- Korean noodle export record
- overseas plant/capacity expansion

Stage 2:
2024-05-27
- Shin Ramyun 2023 sales 1.2T won / $883M
- nearly 60% from overseas
- North America sales $538M, +10%
- U.S. market share 25.4%
- U.S. sales target $1.5B by 2030
- Europe sales +30% in 1Q context
- second LA plant lines / third U.S. plant consideration

Stage 3:
없음
- 해외 매출 구조는 강하지만, stock-level entry price와 30D/90D OHLC 확보 실패
- Stage 3는 해외 sell-through, ASP, capacity utilization, margin, FCF가 확인되어야 함

Stage 4B:
K-food / Shin Ramyun global story로 valuation이 먼저 확장되면 watch

Stage 4C:
China slowdown, Europe adoption miss, input cost, channel inventory, spicy-food fad fade
```

Nongshim은 R12에서 “식품 수출이 반복소비로 바뀌는가”를 보는 좋은 Stage 2 후보이다. FT는 Shin Ramyun 2023 sales가 1.2조 원, 약 $883M이었고 그중 거의 60%가 해외에서 발생했으며, North America sales가 $538M으로 +10% 성장했다고 보도했다. U.S. 시장 점유율은 25.4%이고, 회사는 2030년 U.S. annual sales $1.5B를 목표로 잡았다. 다만 이건 아직 Green이 아니라 **해외 sell-through와 margin이 stock price path로 닫혀야 하는 Stage 2**다. ([Financial Times][1])

### 실제 가격경로 검증

```text
price_data_source:
FT business anchor + attempted KRX/Naver/Yahoo/Stooq query

entry_date:
N/A

stage3_price:
N/A

Shin_Ramyun_2023_sales:
1.2T won / $883M

overseas_sales_share:
nearly 60%

North_America_sales:
$538M

North_America_sales_growth:
+10%

U.S._market_share:
25.4%

U.S._sales_target_2030:
$1.5B

U.S._target_growth_from_2023_NA_sales:
1.5B / 538M - 1
= +178.8%

Europe_1Q_sales_growth_context:
+30%

MFE_30D / 90D / 180D / 1Y / 2Y:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate_but_price_data_unavailable
rerating_result = K_food_export_capacity_watch
stage_failure_type = export_growth_not_green_until_margin_FCF_price_path
```

---

## Case B — Daesang / CJ CheilJedang kimchi processors `4C-watch / cabbage climate shock`

```text
symbols = 001680 / 097950 / kimchi-food processing basket
case_type = 4C-watch
archetype = AGRI_FOOD_INPUT_COST_SHOCK
```

### stage date

```text
Stage 1:
2024-09~10
- napa cabbage climate shock
- kimchi input cost inflation
- domestic kimchi producers vs Chinese import competition

Stage 4C-watch:
2024-10-23
- government releases 24,000 tonnes cabbage from national stocks
- wholesale cabbage price 3,000 won → 9,537 won → 5,610 won
- average June-August temperature highest since records began in 1973

Stage 4C-watch structural:
2024-09-03
- highland cabbage area 8,796ha → 3,995ha over 20 years
- climate change threatens future napa cabbage production

Stage 3:
없음
- 농산물 가격 상승은 Green이 아니라 원가 RedTeam
- pass-through, inventory control, domestic-vs-import price gap 확인 필요
```

김치·식품가공 basket은 원재료 price shock을 강하게 봐야 한다. Reuters는 정부가 김장철을 앞두고 24,000톤의 배추를 방출하기로 했고, 배추 도매가격이 7월 초 약 3,000원에서 9월 중순 9,537원으로 급등했다가 10월 말 5,610원으로 내려왔다고 보도했다. 또 고랭지 배추 재배면적은 20년 전 8,796ha에서 3,995ha로 줄었다. 이건 식품주 Green이 아니라 **input-cost 4C-watch**다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters crop/input-cost evidence + attempted stock-price query

stage3_price:
N/A

government_cabbage_release:
24,000 tonnes

cabbage_price_early_July:
about 3,000 won/head

cabbage_price_mid_September:
9,537 won/head

cabbage_price_jump:
9,537 / 3,000 - 1
= +217.9%

cabbage_price_late_October:
5,610 won/head

late_October_vs_mid_September:
5,610 / 9,537 - 1
= -41.2%

highland_cabbage_area_20Y_ago:
8,796 hectares

highland_cabbage_area_recent:
3,995 hectares

area_decline:
3,995 / 8,796 - 1
= -54.6%

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = kimchi_input_cost_4C_watch
stage_failure_type = raw_material_shock_not_green
```

---

## Case C — Harim / Farm Story / Maniker feed-livestock basket `4C-watch / feed wheat cost`

```text
symbols = 136480 / 027710 / 195500 / feed-livestock basket
case_type = 4C-watch
archetype = FEED_GRAIN_INPUT_COST_4C
```

### stage date

```text
Stage 1:
2026-05-13
- Korea Feed Leaders Committee feed wheat tender
- livestock/feed input-cost pressure
- U.S. wheat futures surge / harvest forecast concern

Stage 4C-watch:
2026-05-13
- FLC believed to make no purchase in 65,000t feed wheat tender
- prices regarded too high
- lowest offer $298.50/t c&f + $2/t surcharge
- arrival sought around 2026-08-31

Stage 3:
없음
- feed-cost shock is margin risk
- poultry/livestock Green requires price pass-through, feed inventory, demand, OPM
```

사료·축산 basket은 곡물 input cost를 RedTeam으로 넣어야 한다. Reuters는 Korea Feed Leaders Committee가 65,000톤 규모 feed wheat tender에서 가격이 너무 높아 구매를 하지 않은 것으로 보인다고 보도했다. 최저 offer는 $298.50/t c&f에 추가 $2/t port-unloading surcharge가 붙어 실질 $300.50/t로 계산된다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters feed-wheat tender evidence + attempted stock-price query

stage3_price:
N/A

tender_volume:
65,000 metric tons

purchase_result:
believed no purchase

lowest_offer:
$298.50/t c&f

extra_port_unloading_surcharge:
$2.00/t

effective_lowest_offer:
$300.50/t

effective_offer_for_65,000t:
300.50 * 65,000
= $19.53M

arrival_target:
around 2026-08-31

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = feed_grain_input_cost_watch
stage_failure_type = input_cost_4C_watch_not_green
```

---

## Case D — Megastudy / YBMNet / NE Neungyule education basket `event_premium / medical quota`

```text
symbols = 072870 / 057030 / 053290 / education basket
case_type = event_premium
archetype = EDUCATION_POLICY_MEDICAL_QUOTA_EVENT
```

### stage date

```text
Stage 1:
2024~2025
- medical-school quota dispute
- trainee doctor strike
- private education / repeat-course demand expectation

Stage 2:
2026-02-10
- medical quota 3,058 → 3,548 in 2027
- phased increase to 3,871 by 2030
- KMA criticism; renewed protest risk unclear

Stage 4C-watch:
2025-03-07
- 13-month dispute
- 90% of trainee doctors had resigned
- emergency care and surgery delays
- policy uncertainty can disrupt healthcare-service and education planning

Stage 3:
없음
- policy quota is not education-stock Green
- paid enrollment, repeat-course sales, ARPU, OPM, cash conversion 확인 필요
```

의대정원 정책은 교육주에 Stage 1~2 event는 될 수 있지만, Green은 아니다. Reuters는 정부가 2027년 의대정원을 3,058명에서 3,548명으로 늘리고, 2030년 3,871명까지 단계적으로 확대하겠다고 보도했다. 다만 같은 정책축은 2024~2025년 의료대란을 낳았고, 2025년 3월 기준 trainee doctors의 90%가 사직한 상태였다. 즉 교육주는 “정원 증가”보다 **실제 유료수강 전환과 정책 지속성**이 핵심이다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters policy evidence + attempted education-stock price query

stage3_price:
N/A

original_quota:
3,058

2027_quota:
3,548

quota_increase_2027:
490

quota_increase_2027_pct:
3,548 / 3,058 - 1
= +16.0%

2030_quota:
3,871

quota_increase_2030_vs_original:
813

quota_increase_2030_pct:
3,871 / 3,058 - 1
= +26.6%

trainee_doctor_resignation_share_2025:
90%

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium_policy_watch
rerating_result = education_policy_quota_watch
stage_failure_type = quota_policy_not_paid_enrollment_green
```

---

## Case E — Woongjin Thinkbig / YBMNet / AI textbook basket `4C-watch / edtech rollback`

```text
symbols = 095720 / 057030 / edtech basket
case_type = 4C-watch
archetype = EDTECH_POLICY_ROLLBACK_4C
```

### stage date

```text
Stage 1:
2024~2025
- AI textbook / AI tutor / edtech policy expectation
- digital classroom infrastructure narrative

Stage 4C-watch:
2025-08-04 / 2025-08-22
- AI textbooks reclassified from official textbooks to supplementary materials
- teacher/parent backlash
- 87.4% of teachers reported lack of preparation/support

Stage 4C-watch 추가:
2025-08-27
- nationwide mobile-phone/digital-device classroom ban passed
- effective March 2026
- 37% of middle/high school students say social media affects daily life
- 22% anxious without access

Stage 3:
없음
- AI education headline is not Green
- school adoption, paid contract, renewal, teacher acceptance, margin 확인 필요
```

AI 교과서와 edtech basket은 policy friction을 강하게 봐야 한다. Business Insider는 South Korea가 AI textbooks를 official textbooks에서 supplementary materials로 낮췄고, 교사 설문에서 87.4%가 준비와 지원이 부족하다고 답했다고 보도했다. Reuters는 2026년 3월부터 classroom mobile/digital-device ban이 시행된다고 보도했다. 이는 edtech theme의 Green gate를 막는 명확한 4C-watch다. ([Business Insider][5])

### 실제 가격경로 검증

```text
price_data_source:
Business Insider / Reuters policy evidence + attempted edtech stock-price query

stage3_price:
N/A

AI_textbook_status:
official textbook → supplementary material

teacher_unprepared_share:
87.4%

classroom_phone_device_ban_effective:
2026-03

students_social_media_affects_daily_life:
37%

students_anxious_without_social_media:
22%

device_exception:
disability / educational purpose

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = edtech_policy_rollback_watch
stage_failure_type = policy_rollback_blocks_green
```

---

## Case F — Childcare / foreign housekeeper / fertility basket `success_candidate policy event`

```text
symbols = childcare / infant goods / education / care-service basket
case_type = success_candidate_policy_event
archetype = CHILDCARE_FOREIGN_HELPER_POLICY_EVENT
```

### stage date

```text
Stage 1:
2024-07-28
- foreign housekeeper pilot
- childcare burden / female labor participation / birthrate policy
- 100 Filipina workers initially

Stage 2:
2024~2026
- pilot could expand to 1,200 workers
- fertility rate 0.72 in 2023 → 0.75 in 2024 → 0.80 in 2025
- births +6.8% in 2025
- marriages +8.1%
- Seoul fertility +8.9%

Stage 3:
없음
- demographic/policy event is not listed-company Green
- paid care demand, utilization, margin, repeat service, subsidy dependence 확인 필요

Stage 4B:
출산율 반등 / 돌봄정책 headline로 유아·교육·돌봄주가 먼저 오르면 watch
```

외국인 가사·돌봄 worker pilot과 출산율 반등은 R12에서 의미 있는 Stage 2다. FT는 약 100명의 Filipina workers가 들어오고, pilot 성공 시 1,200명까지 확대될 수 있다고 보도했다. Reuters는 2025년 합계출산율이 0.80으로 2023년 0.72, 2024년 0.75에서 반등했고, 2025년 출생아가 +6.8%, 혼인이 +8.1% 늘었다고 보도했다. 그러나 listed childcare/service Green은 **유료수요·utilization·margin**으로 확인되어야 한다. ([Financial Times][6])

### 실제 가격경로 검증

```text
price_data_source:
FT foreign-housekeeper policy anchor + Reuters fertility anchor

stage3_price:
N/A

foreign_housekeeper_pilot:
100 workers

possible_expansion:
1,200 workers

pilot_expansion_multiple:
1,200 / 100
= 12x

fertility_rate_2023:
0.72

fertility_rate_2024:
0.75

fertility_rate_2025:
0.80

fertility_rebound_2023_to_2025:
0.80 / 0.72 - 1
= +11.1%

births_2025_growth:
+6.8%

marriages_2025_growth:
+8.1%

Seoul_fertility_growth:
+8.9%

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate_policy_event
rerating_result = childcare_service_policy_watch
stage_failure_type = demographic_policy_not_paid_utilization_green
```

---

## Case G — Pet-food / animal welfare transition basket `event_premium / dog-meat ban`

```text
symbols = pet-food / pet-care / shelter / animal-welfare transition basket
case_type = event_premium
archetype = PET_WELFARE_TRANSITION_POLICY_EVENT
```

### stage date

```text
Stage 1:
2024-09-26
- dog-meat ban transition
- pet / animal welfare policy
- shelter / adoption / pet-care demand narrative

Stage 2:
2027-02 effective ban 예정
- government support about 100B won
- nearly 500,000 dogs to rehome
- farmers can receive up to 600,000 won per surrendered dog
- more than 1,500 dog breeding farms
- more than 200 slaughter houses
- about 2,300 restaurants serving dog meat

Stage 3:
없음
- policy transition is not listed-company Green
- pet-food demand, adoption-service revenue, shelter capacity, margin 확인 필요

Stage 4B:
펫/동물복지 테마주가 정책 발표만으로 먼저 급등하면 watch

Stage 4C:
shelter capacity failure, subsidy dissatisfaction, adoption bottleneck, policy delay
```

개식용 금지 전환은 pet/welfare transition policy event다. Reuters는 정부가 약 1,000억 원의 지원책을 마련하고, 식용견 약 50만 마리를 입양·보호시설로 전환하려 하며, 농가는 반납하는 개 한 마리당 최대 600,000원을 받을 수 있다고 보도했다. 하지만 이것은 **정책 이벤트**이지, pet-food/service 상장사의 매출 evidence는 아니다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters dog-meat ban / transition policy evidence

stage3_price:
N/A

government_support:
about 100B won

dogs_to_rehome:
nearly 500,000

farmer_subsidy_per_dog:
up to 600,000 won

dog_breeding_farms:
more than 1,500

slaughter_houses:
more than 200

restaurants_serving_dog_meat:
about 2,300

ban_effective:
2027-02

potential_subsidy_liability_if_all_dogs_max:
500,000 * 600,000
= 300B won

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium_policy_watch
rerating_result = pet_welfare_transition_watch
stage_failure_type = policy_not_revenue_green
```

---

## Case H — Kyochon / Cherrybro / Neuromeka Jensen event `overheat / price_moved_without_evidence`

```text
symbols = 339770 / 066360 / 348340
case_type = overheat
archetype = FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM
```

### stage date

```text
Stage 1:
2025-10-31
- Jensen Huang fried-chicken dinner
- Samsung / Hyundai executives present
- APEC / Nvidia Korea AI-chip deal context

Stage 2:
없음
- no same-store sales evidence
- no franchise margin evidence
- no repeat traffic evidence

Stage 4B:
2025-10-31
- Kyochon F&B up to +20%
- Cherrybro up to daily limit +30%
- Neuromeka surged
- MarketWatch: only Neuromeka retained gains by close
- restaurant visited was non-listed Kkanbu Chicken

Stage 3:
없음
```

이 case는 R12에서 가장 깨끗한 `price_moved_without_evidence`다. Jensen Huang이 Samsung·Hyundai 경영진과 비상장 Kkanbu Chicken에서 식사한 장면이 퍼지자, Kyochon F&B, Cherrybro, Neuromeka가 급등했다. Tom’s Hardware는 Kyochon이 최대 20%, Cherrybro가 daily limit 30%까지 올랐다고 보도했고, MarketWatch는 세 종목 중 Neuromeka만 종가까지 상승분을 유지했다고 전했다. 실제 same-store sales, franchise margin, repeat demand는 확인되지 않았다. ([Tom's Hardware][8])

### 실제 가격경로 검증

```text
price_data_source:
Tom's Hardware / MarketWatch event-return summary

stage3_price:
N/A

Kyochon_event_MFE:
up to +20%

Cherrybro_event_MFE:
up to +30%

Neuromeka_event:
surged; only one of three retained gains by close according to MarketWatch

event_driver:
viral dinner at non-listed Kkanbu Chicken

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

# 5. 이번 R12 case별 요약표

| case                            | 분류                             |                                                                 실제 가격검증 | alignment               |
| ------------------------------- | ------------------------------ | ----------------------------------------------------------------------: | ----------------------- |
| Nongshim                        | structural_success_candidate   |         Shin Ramyun 1.2T won, overseas 60%, NA $538M, U.S. target $1.5B | export capacity Stage 2 |
| Daesang / CJ kimchi             | 4C-watch                       |                       cabbage 3,000→9,537 won, +217.9%; 24,000t release | input-cost shock        |
| Harim / Farm Story feed         | 4C-watch                       |                         65,000t tender no purchase, effective $300.50/t | feed-cost shock         |
| Education quota basket          | event premium                  |                                  quota 3,058→3,548→3,871, +16.0%/+26.6% | policy event            |
| Edtech AI textbook              | 4C-watch                       | AI textbook official→supplementary, teacher unprepared 87.4%, phone ban | policy rollback         |
| Childcare / foreign helper      | success_candidate policy event |                    100→1,200 workers, fertility 0.72→0.80, births +6.8% | policy Stage 2          |
| Pet welfare transition          | event premium                  |                           100B won support, 500k dogs, max 600k won/dog | policy not revenue      |
| Kyochon / Cherrybro / Neuromeka | overheat                       |                         Kyochon +20%, Cherrybro +30%, no sales evidence | price-only              |

---

# 6. score-price alignment 판정

```text
structural_success_candidate:
- Nongshim

success_candidate_policy_event:
- Childcare / foreign housekeeper / fertility basket

event_premium:
- Medical quota education basket
- Dog-meat ban / pet-welfare transition
- Kyochon / Cherrybro / Neuromeka Jensen event

price_moved_without_evidence:
- Kyochon / Cherrybro / Neuromeka
- education stocks if quota headline moves before paid enrollment / ARPU
- pet basket if policy headline moves before monetization
- childcare basket if fertility headline moves before utilization/margin

thesis_break_watch:
- Daesang / CJ kimchi cabbage input cost
- Harim / Farm Story feed wheat cost
- Woongjin/YBMNet AI textbook rollback
- classroom device ban for edtech

hard_4C_confirmed:
- false
```

이번 R12 Loop 12에서는 hard 4C를 억지로 만들지 않는다. **cabbage input shock, feed wheat cost, AI textbook rollback, classroom phone/device ban**은 모두 강한 4C-watch이고, **Kyochon/Cherrybro/Neuromeka event**는 4B/event premium이다.

---

# 7. 점수비중 교정

## 올릴 축

```text
repeat_purchase +5
overseas_sell_through +5
capacity_utilization +5
paid_enrollment_conversion +5
service_utilization +5
ARPU_or_price_pass_through +5
input_cost_pass_through +5
inventory_quality +4
cash_conversion +5
policy_to_revenue_bridge +5
```

### 왜 올리나

Nongshim은 K-food export가 실제 매출 규모와 해외비중으로 확인된 좋은 Stage 2다. 하지만 Green은 해외 sell-through와 margin이 닫혀야 한다. childcare/foreign helper는 policy와 demographic data가 좋아졌지만, 실제 유료서비스 utilization이 필요하다. education·pet·edtech도 policy headline보다 paid conversion이 먼저다.

## 내릴 축

```text
policy_headline_only -5
fertility_headline_only -5
medical_quota_only -5
AI_textbook_theme_only -5
pet_welfare_policy_only -5
celebrity_food_event_only -5
raw_material_price_spike_without_pass_through -5
feed_cost_spike_without_inventory_buffer -5
unconfirmed_demand_conversion -5
```

### 왜 내리나

의대정원은 사교육 수요 가능성을 만들지만, 곧바로 유료수강 매출은 아니다. 출산율 반등도 childcare service revenue로 바로 닫히지 않는다. dog-meat ban은 pet transition event일 뿐이다. 배추와 사료곡물 가격 shock은 food/livestock 기업의 margin risk다. Jensen event는 sales evidence 없이 price만 움직인 case다.

## Green gate 강화 조건

```text
R12 Stage 3-Green 필수:
1. 반복구매 또는 반복서비스 이용 확인
2. 해외 sell-through / channel reorder 확인
3. capacity utilization 확인
4. paid enrollment / paid household usage / service utilization 확인
5. ARPU 또는 가격전가 확인
6. input cost pass-through 확인
7. 재고·매출채권 안정
8. subsidy / policy 의존도 낮음
9. cash conversion 확인
10. 가격경로가 evidence 이후 따라옴

금지:
정책 뉴스만 있음
의대정원 headline만 있음
AI textbook theme만 있음
출산율 반등만 있음
pet-welfare policy만 있음
농산물 가격 spike만 있음
feed cost spike만 있음
celebrity food event만 있음
```

## 4B 조기감지 조건

```text
4B-watch:
K-food export headline로 food stock이 margin 확인 전 급등
의대정원 뉴스로 교육주가 paid enrollment 전 급등
출산율 반등으로 childcare/infant basket 급등
AI textbook / edtech policy 기대만으로 급등
dog-meat ban / pet welfare policy로 pet basket 급등
celebrity food event로 restaurant/poultry/robot stock 급등
농산물 shock으로 식품주가 가격전가 전 급등

4B-elevated:
channel inventory 증가
raw material cost spike
feed cost spike
policy reversal
teacher/parent backlash
shelter capacity 부족
same-store sales 미확인
```

## 4C hard gate 조건

```text
raw material shock without pass-through
feed-cost spike with no inventory buffer
policy rollback
paid enrollment failure
service utilization failure
inventory build
cash conversion deterioration
product recall / food safety
shelter-capacity failure
celebrity event fade
```

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

## docs/round/round_196.md 요약

```md
# R12 Loop 12. Agriculture / Life Service / Misc Price Validation

이번 라운드는 R12 Loop 12 price-validation 라운드다.

핵심 결론:
- Nongshim is K-food export Stage 2. Shin Ramyun 2023 sales 1.2T won / $883M, nearly 60% overseas, North America sales $538M +10%, U.S. share 25.4%, target U.S. sales $1.5B by 2030. Stage 3 requires overseas sell-through, margin, capacity utilization and price path.
- Daesang / CJ kimchi processors are agri-food input-cost 4C-watch. Government released 24,000t cabbage; wholesale cabbage rose from about 3,000 won to 9,537 won, then fell to 5,610 won. Highland cabbage area fell from 8,796ha to 3,995ha over 20 years.
- Harim / Farm Story / Maniker feed-livestock basket is feed-cost 4C-watch. FLC made no purchase in a 65,000t feed wheat tender because prices were too high; effective low offer was $300.50/t.
- Medical quota education basket is event premium. Quota rises from 3,058 to 3,548 in 2027 and 3,871 by 2030. Paid enrollment, ARPU, repeat course, OPM and cash conversion required before Green.
- AI textbook / edtech basket is 4C-watch. AI textbooks were downgraded from official textbooks to supplementary materials; 87.4% of teachers reported lack of preparation/support. Classroom phone/device ban takes effect March 2026.
- Childcare / foreign housekeeper / fertility basket is policy Stage 2. Foreign helper pilot 100 workers could expand to 1,200; fertility rose 0.72→0.80, births +6.8%, marriages +8.1%. Paid utilization and margin required.
- Dog-meat ban / pet-welfare transition is policy event. Government support about 100B won, nearly 500k dogs to rehome, up to 600k won per surrendered dog. Pet revenue conversion required.
- Kyochon / Cherrybro / Neuromeka Jensen event is price_moved_without_evidence. Kyochon up to +20%, Cherrybro up to +30%, but no same-store sales, franchise margin or repeat demand evidence.
```

## docs/checkpoints/checkpoint_28a_round196_r12_loop12.md 요약

```md
# Checkpoint 28A Round 196 R12 Loop 12 Agri Life Service Misc Price Validation

## 반영 내용
- R12 Loop 12 price-validation 라운드를 추가했다.
- K-food export, kimchi/cabbage input shock, feed wheat input cost, medical quota education event, AI textbook rollback, foreign housekeeper/childcare policy, pet-welfare transition, celebrity food event를 비교했다.
- Reuters / FT / Business Insider / MarketWatch / Tom’s Hardware anchors로 가능한 event metrics와 price anchors를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- repeat purchase, overseas sell-through, capacity utilization, paid enrollment conversion, service utilization, price pass-through, input-cost pass-through, inventory quality, cash conversion 가중치 강화
- policy headline-only, fertility headline-only, medical quota-only, AI textbook theme-only, pet policy-only, celebrity food event-only, raw material spike without pass-through 감점 강화
```

## data/e2r_case_library/cases_r12_loop12_round196.jsonl 초안

```jsonl
{"case_id":"r12_loop12_nongshim_shin_export_capacity","symbol":"004370","company_name":"Nongshim","case_type":"structural_success_candidate","primary_archetype":"K_FOOD_EXPORT_CAPACITY_RECURRING_CONSUMPTION","stage2_date":"2024-05-27","price_validation":{"price_data_source":"FT business anchor + attempted KRX/Naver/Yahoo/Stooq query","stage3_price":null,"shin_ramyun_2023_sales_krw_trn":1.2,"shin_ramyun_2023_sales_usd_mn":883,"overseas_sales_share_pct":60,"north_america_sales_usd_mn":538,"north_america_sales_growth_pct":10,"us_market_share_pct":25.4,"us_sales_target_2030_usd_bn":1.5,"us_target_growth_from_2023_na_sales_pct":178.8,"europe_1q_sales_growth_context_pct":30,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_price_data_unavailable","rerating_result":"K_food_export_capacity_watch","notes":"K-food export structure is strong Stage 2; Green requires overseas sell-through, capacity utilization, margin, FCF and price path."}
{"case_id":"r12_loop12_kimchi_cabbage_input_cost_watch","symbol":"001680/097950/kimchi_food_processing_basket","company_name":"Daesang / CJ CheilJedang / kimchi processors","case_type":"4c_watch","primary_archetype":"AGRI_FOOD_INPUT_COST_SHOCK","stage4c_date":"2024-09/2024-10","price_validation":{"price_data_source":"Reuters crop/input-cost evidence + attempted stock-price query","stage3_price":null,"government_cabbage_release_tonnes":24000,"cabbage_price_early_july_krw":3000,"cabbage_price_mid_sept_krw":9537,"cabbage_price_jump_pct":217.9,"cabbage_price_late_oct_krw":5610,"late_oct_vs_mid_sept_pct":-41.2,"highland_cabbage_area_20y_ago_ha":8796,"highland_cabbage_area_recent_ha":3995,"area_decline_pct":-54.6,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"kimchi_input_cost_4C_watch","notes":"Cabbage climate/input shock is 4C-watch unless processors prove pass-through and inventory control."}
{"case_id":"r12_loop12_feed_wheat_livestock_cost_watch","symbol":"136480/027710/195500/feed_livestock_basket","company_name":"Harim / Farm Story / Maniker / feed-livestock basket","case_type":"4c_watch","primary_archetype":"FEED_GRAIN_INPUT_COST_4C","stage4c_date":"2026-05-13","price_validation":{"price_data_source":"Reuters feed-wheat tender evidence + attempted stock-price query","stage3_price":null,"tender_volume_tonnes":65000,"purchase_result":"believed_no_purchase","lowest_offer_usd_per_t":298.5,"extra_unloading_surcharge_usd_per_t":2.0,"effective_lowest_offer_usd_per_t":300.5,"effective_offer_for_65000t_usd_mn":19.53,"arrival_target":"2026-08-31","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"feed_grain_input_cost_watch","notes":"Feed wheat cost is 4C-watch for feed/livestock names until price pass-through and feed inventory buffer confirm."}
{"case_id":"r12_loop12_medical_quota_private_education_event","symbol":"072870/057030/053290/education_basket","company_name":"Megastudy / YBMNet / NE Neungyule / education basket","case_type":"event_premium","primary_archetype":"EDUCATION_POLICY_MEDICAL_QUOTA_EVENT","stage2_date":"2026-02-10","stage4c_date":"2025-03-07_watch","price_validation":{"price_data_source":"Reuters policy evidence + attempted education-stock price query","stage3_price":null,"original_quota":3058,"quota_2027":3548,"quota_increase_2027":490,"quota_increase_2027_pct":16.0,"quota_2030":3871,"quota_increase_2030_vs_original":813,"quota_increase_2030_pct":26.6,"trainee_doctor_resignation_share_2025_pct":90,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_policy_watch","rerating_result":"education_policy_quota_watch","notes":"Medical quota is Stage 2; paid enrollment, ARPU, repeat course, OPM and cash conversion required before Green."}
{"case_id":"r12_loop12_ai_textbook_edtech_policy_rollback","symbol":"095720/057030/edtech_basket","company_name":"Woongjin Thinkbig / YBMNet / edtech basket","case_type":"4c_watch","primary_archetype":"EDTECH_POLICY_ROLLBACK_4C","stage4c_date":"2025-08","price_validation":{"price_data_source":"Business Insider / Reuters policy evidence + attempted edtech stock-price query","stage3_price":null,"ai_textbook_status":"official_textbook_to_supplementary_material","teacher_unprepared_share_pct":87.4,"classroom_phone_device_ban_effective":"2026-03","students_social_media_affects_daily_life_pct":37,"students_anxious_without_social_media_pct":22,"device_exception":"disability_or_educational_purpose","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"edtech_policy_rollback_watch","notes":"AI education theme is blocked by policy rollback, teacher-preparation gap and classroom device restrictions."}
{"case_id":"r12_loop12_childcare_foreign_helper_fertility_policy","symbol":"childcare/infant_goods/care_service_basket","company_name":"Childcare / foreign housekeeper / fertility basket","case_type":"success_candidate_policy_event","primary_archetype":"CHILDCARE_FOREIGN_HELPER_POLICY_EVENT","stage2_date":"2024-07-28/2026-02-25","price_validation":{"price_data_source":"FT foreign-housekeeper policy anchor + Reuters fertility anchor","stage3_price":null,"foreign_housekeeper_pilot_workers":100,"possible_expansion_workers":1200,"pilot_expansion_multiple":12,"fertility_rate_2023":0.72,"fertility_rate_2024":0.75,"fertility_rate_2025":0.80,"fertility_rebound_2023_to_2025_pct":11.1,"births_2025_growth_pct":6.8,"marriages_2025_growth_pct":8.1,"seoul_fertility_growth_pct":8.9,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_policy_event","rerating_result":"childcare_service_policy_watch","notes":"Policy and fertility rebound are Stage 2; paid household demand, utilization, margin and cash conversion required before Green."}
{"case_id":"r12_loop12_dog_meat_ban_pet_welfare_transition","symbol":"pet_food/pet_care/animal_welfare_basket","company_name":"Dog-meat ban / pet-welfare transition basket","case_type":"event_premium","primary_archetype":"PET_WELFARE_TRANSITION_POLICY_EVENT","stage2_date":"2024-09-26","price_validation":{"price_data_source":"Reuters dog-meat ban / transition policy evidence","stage3_price":null,"government_support_krw_bn":100,"dogs_to_rehome":500000,"farmer_subsidy_per_dog_krw":600000,"dog_breeding_farms":1500,"slaughter_houses":200,"restaurants_serving_dog_meat":2300,"ban_effective":"2027-02","potential_subsidy_liability_if_all_dogs_max_krw_bn":300,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_policy_watch","rerating_result":"pet_welfare_transition_watch","notes":"Dog-meat ban transition is policy event; pet-food/service revenue conversion and shelter capacity required before Green."}
{"case_id":"r12_loop12_kyochon_cherrybro_neuromeka_jensen_event","symbol":"339770/066360/348340","company_name":"Kyochon F&B / Cherrybro / Neuromeka","case_type":"overheat","primary_archetype":"FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM","stage1_date":"2025-10-31","stage4b_date":"2025-10-31","price_validation":{"price_data_source":"Tom's Hardware / MarketWatch event-return summary","stage3_price":null,"kyochon_event_mfe_pct":20,"cherrybro_event_mfe_pct":30,"neuromeka_event":"surged; only one of three retained gains by close according to MarketWatch","event_driver":"viral dinner at non-listed Kkanbu Chicken","fundamental_revenue_evidence_confirmed":false,"same_store_sales_confirmed":false,"franchise_margin_confirmed":false,"price_validation_status":"reported_event_return_not_full_ohlc"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"celebrity_food_event_premium","notes":"Celebrity food-service event is 4B/event premium until same-store sales, franchise margin and repeat demand confirm."}
```

## data/sector_taxonomy/score_weight_profiles_round196_r12_loop12_v1.csv 초안

```csv
archetype,repeat_purchase,overseas_sell_through,capacity_utilization,paid_conversion,service_utilization,arpu_price_pass,input_cost_pass_through,inventory_quality,cash_conversion,policy_to_revenue_bridge,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
K_FOOD_EXPORT_CAPACITY_RECURRING_CONSUMPTION,+5,+5,+5,+2,+0,+5,+4,+4,+5,+3,-2,+4,+3,Nongshim export structure is Stage 2 until margin/FCF/price path confirm.
AGRI_FOOD_INPUT_COST_SHOCK,+2,+1,+1,+0,+0,+5,+5,+5,+5,+1,0,+4,+5,Cabbage climate/input shock is 4C-watch unless pass-through and inventory control prove out.
FEED_GRAIN_INPUT_COST_4C,+1,+0,+1,+0,+0,+4,+5,+5,+4,+0,0,+4,+5,Feed wheat cost shock hits livestock/feed margin unless pass-through and inventory buffer exist.
EDUCATION_POLICY_MEDICAL_QUOTA_EVENT,+2,+0,+0,+5,+4,+5,+0,+1,+5,+5,-5,+5,+4,Medical quota is event until paid enrollment, ARPU and repeat-course revenue confirm.
EDTECH_POLICY_ROLLBACK_4C,+2,+0,+0,+4,+4,+4,+0,+1,+4,+5,0,+4,+5,AI textbook rollback and phone ban block edtech Green.
CHILDCARE_FOREIGN_HELPER_POLICY_EVENT,+4,+0,+2,+5,+5,+5,+1,+2,+5,+5,-5,+5,+4,Fertility and foreign-helper policy need paid utilization and margin.
PET_WELFARE_TRANSITION_POLICY_EVENT,+4,+0,+2,+3,+5,+4,+1,+2,+4,+5,-5,+5,+4,Dog-meat ban is policy event until pet-service revenue and shelter capacity confirm.
FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM,+2,+0,+1,+2,+2,+3,+3,+3,+3,+0,-5,+5,+3,Kyochon/Cherrybro/Neuromeka Jensen event is price_moved_without_evidence.
```

---

# 이번 R12 Loop 12 결론

```text
1. Nongshim은 R12의 K-food export Stage 2다.
   해외 매출과 U.S. 목표는 좋지만, margin/FCF/price path 전에는 Stage 3가 아니다.

2. Daesang / CJ kimchi processors는 cabbage input-cost 4C-watch다.
   배추 가격 +217.9% shock은 Green이 아니라 원가 RedTeam이다.

3. Harim / Farm Story / Maniker feed basket은 feed wheat 4C-watch다.
   65,000t tender가 가격 때문에 무산될 정도면 livestock margin gate가 필요하다.

4. 의대정원 교육주는 event premium이다.
   quota 확대는 paid enrollment와 ARPU로 닫혀야 한다.

5. AI textbook / edtech는 policy rollback 4C-watch다.
   official textbook 지위 상실과 classroom device ban이 Green을 막는다.

6. foreign housekeeper / childcare는 policy Stage 2다.
   출산율 반등과 pilot 확대 가능성은 좋지만, 유료 utilization 전 Green 금지다.

7. dog-meat ban / pet transition은 policy event다.
   pet-food/service 매출과 shelter capacity가 확인되어야 한다.

8. Kyochon / Cherrybro / Neuromeka Jensen event는 price_moved_without_evidence다.
   celebrity event로 +20~30%가 나왔지만 same-store sales evidence는 없었다.
```

한 문장으로 압축하면:

> **R12에서 진짜 Stage 3는 “K-food·교육·돌봄·펫·생활서비스 정책이 좋다”가 아니라, 반복구매·유료전환·서비스 utilization·가격전가·재고 품질·현금전환이 실제 숫자로 닫히는 순간이다.**

[1]: https://www.ft.com/content/4218f2b8-5498-411b-81fe-e3c836868d64?utm_source=chatgpt.com "Maker of Shin instant ramen expands overseas as Korean noodles become hit"
[2]: https://www.reuters.com/world/asia-pacific/south-korea-supply-stocks-kimchi-cabbage-after-hot-weather-damages-crop-2024-10-23/?utm_source=chatgpt.com "South Korea to supply stocks of kimchi cabbage after hot weather damages crop"
[3]: https://www.reuters.com/world/asia-pacific/south-koreas-flc-believed-make-no-purchase-65000-ton-feed-wheat-tender-traders-2026-05-13/?utm_source=chatgpt.com "South Korea's FLC believed to make no purchase in 65,000 ton feed wheat tender, traders say"
[4]: https://www.reuters.com/business/healthcare-pharmaceuticals/south-korea-revives-plan-add-medical-students-doctors-criticise-bid-2026-02-10/?utm_source=chatgpt.com "South Korea revives plan to add medical students; doctors criticise bid"
[5]: https://www.businessinsider.com/ai-in-school-south-korea-textbook-rollback-jobs-education-2025-8?utm_source=chatgpt.com "Why South Korea's AI rollback in classrooms is a cautionary tale for the US"
[6]: https://www.ft.com/content/20b07600-765e-461b-8439-a0c6e7c7f4da?utm_source=chatgpt.com "South Korea bets on foreign housekeepers to ease women's workloads and boost birth rate"
[7]: https://www.reuters.com/world/asia-pacific/south-korea-offers-incentives-adoptions-ahead-ban-farming-dogs-food-2024-09-26/?utm_source=chatgpt.com "South Korea offers incentives, adoptions ahead of ban on farming dogs for food"
[8]: https://www.tomshardware.com/tech-industry/korean-fried-chicken-stocks-surge-30-percent-as-nvidia-ceo-jensen-huang-dines-out-on-local-delicacy-entire-industry-buoyed-by-secret-ingredient-jensanity?utm_source=chatgpt.com "Korean fried chicken stocks surge 30% as Nvidia CEO Jensen Huang dines out on local delicacy - entire industry buoyed by secret ingredient, Jensanity"

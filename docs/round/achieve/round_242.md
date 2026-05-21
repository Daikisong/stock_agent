순서상 이번은 **R12 Loop 10 — 농업·생활서비스·기타 가격경로 검증 라운드**다.

이번 R12는 **생활가전 렌탈, 의대정원·교육정책, AI 교과서·교실 기기 규제, 출산·돌봄정책, 농산물·김치 원재료 shock, 사료곡물 input cost, 동물복지·펫 전환, celebrity food event**를 같이 본다.

```text
round = R12 Loop 10
round_id = round_170
large_sector = AGRI_LIFE_SERVICE_MISC
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = false
```

이번 환경에서는 KRX/Naver/Yahoo/Stooq의 원시 수정주가 일봉 OHLC를 안정적으로 직접 확보하지 못했다. 대신 Reuters / FT / AP / MarketWatch / Tom’s Hardware / Business Insider / 공개 기업정보에서 확인되는 **이벤트 수익률, 정책 수치, 가격 anchor, 시장·비용·규제 지표**만 계산했다. 원시 OHLC가 없는 구간은 `price_data_unavailable_after_deep_search`로 표시한다.

---

# 1. 이번 라운드 대섹터

```text
R12 = 농업·생활서비스·기타
```

R12의 Stage 3는 “방어주다”, “정책 수혜다”, “교육정책이 바뀐다”, “농산물 가격이 오른다”, “밈 이벤트가 떴다”가 아니다.

**반복매출·반복구매·churn 안정·ARPU·unit economics·가격전가·재고/채권 품질·현금전환**이 확인되어야 한다.

---

# 2. 대상 canonical archetype

```text
HOME_LIVING_RENTAL_RECURRING
EDUCATION_POLICY_MEDICAL_QUOTA
EDTECH_AI_TEXTBOOK_POLICY_REVERSAL
CHILDCARE_DEMOGRAPHIC_POLICY_EVENT
AGRI_FOOD_INPUT_COST_SHOCK
FEED_GRAIN_INPUT_COST_4C
PET_WELFARE_POLICY_TRANSITION
FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM
PRICE_ONLY_RALLY
EVENT_PREMIUM
```

---

# 3. deep sub-archetype

```text
생활 렌탈:
- Coway
- water purifier / air purifier / bidet / mattress rental
- Malaysia / overseas expansion
- recurring account base
- churn / ARPU / service network / FCF

교육:
- Megastudy / YBM Net / NE Neungyule / Woongjin Thinkbig basket
- medical-school quota
- repeat course / ARPU / OPM
- AI textbook rollback
- classroom phone ban
- edtech policy friction

출산·돌봄:
- childcare / infant goods / education / care-service basket
- fertility rebound
- foreign housekeeper pilot
- childcare support policy
- policy event vs company revenue

농업·식품 input:
- Daesang / CJ CheilJedang / kimchi processors
- napa cabbage climate shock
- government cabbage stock release
- food-price stabilization policy
- price pass-through / margin

사료·축산 input:
- Harim / Maniker / Farm Story / feed-livestock basket
- feed wheat tender failure
- wheat price / FX / grain cost
- pass-through and inventory risk

동물복지·펫:
- pet food / animal welfare / shelter / service basket
- dog-meat ban
- subsidies / transition support
- policy event, not listed-company Green

생활서비스 이벤트:
- Kyochon F&B / Cherrybro / Neuromeka
- Jensen Huang fried-chicken event
- celebrity/AI-adjacent meme rally
- price before evidence
```

---

# 4. 국장 신규 후보 case

## Case A — Coway `structural_success_candidate / recurring rental`

```text
symbol = 021240
case_type = structural_success_candidate
archetype = HOME_LIVING_RENTAL_RECURRING
```

### stage date

```text
Stage 1:
2024~2026
- 생활가전 렌탈 반복매출
- 정수기 / 공기청정기 / 비데 / 매트리스 계정 기반
- Malaysia / U.S. / Thailand / Indonesia / Vietnam 등 해외 법인 확장

Stage 2:
보류
- rental account growth
- churn
- ARPU
- overseas account growth
- OPM / FCF 확인 필요

Stage 3:
조건부 후보
- recurring revenue + churn stability + ARPU + overseas growth + FCF conversion 확인 시 가능

Stage 4B:
방어적 렌탈·배당·반복매출 프레임으로 valuation이 성장률보다 먼저 확장되면 후보

Stage 4C:
product recall, churn spike, overseas slowdown, service-cost inflation, Netmarble capital-allocation risk
```

Coway는 R12에서 가장 Stage 3에 가까운 구조 후보 중 하나다. 공개 기업정보상 Coway는 국내 최대 정수기 회사로, 정수기·공기청정기·비데·매트리스 등 생활가전 렌탈 모델을 갖고 있고, Malaysia·U.S.·Thailand·Indonesia·Vietnam 등 해외 법인을 보유한다. 다만 이번 pass에서 최신 rental accounts, churn, ARPU, FCF, raw OHLC는 확인하지 못했다. 따라서 구조 후보로 두되 Stage 3는 보류한다. ([위키백과][1])

### 실제 가격경로 검증

```text
price_data_source:
public company profile only

stage3_price:
price_data_unavailable_after_deep_search

reason:
- Reuters / MarketWatch / FT에서 Coway event-day 주가 anchor를 찾지 못함.
- KRX / Naver / Yahoo / Stooq 원시 수정주가 일봉 OHLC 직접 확보 실패.
- 최신 rental accounts / churn / ARPU / FCF 원문 숫자 직접 확보 실패.

known_business_anchor:
domestic largest water purifier company
rental/service model
overseas subsidiaries present

MFE_30D / 90D / 180D / 1Y / 2Y:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = recurring_service_rerating_candidate
stage_failure_type = stage2_watch_success_candidate
```

---

## Case B — Medical-school quota / private-education basket `event_premium / policy watch`

```text
symbols = 215200 / YBMNet / NE Neungyule / Woongjin Thinkbig basket
case_type = event_premium / policy_watch
archetype = EDUCATION_POLICY_MEDICAL_QUOTA
```

### stage date

```text
Stage 1:
2024-02~2025
- 의대정원 확대 정책
- 사교육 / 의대 입시 / 재수 수요 기대
- trainee doctor strike로 정책 변동성 확대

Stage 2:
2026-02-10
- 2027년 의대정원 3,548명
- 2030년 3,871명까지 단계적 확대
- 2024년 aggressive 증원안보다 완화된 재추진

Stage 3:
없음
- 정책만으로 Green 금지
- 실제 수강생 증가, repeat course, ARPU, OPM, cash conversion 확인 필요

Stage 4B:
의대정원 뉴스로 교육주가 수강생 증가보다 먼저 급등하면 후보

Stage 4C:
정책 후퇴, 의사단체 재반발, 사교육 규제, 학령인구 감소, AI tutoring disruption
```

의대정원 정책은 교육주에 routing signal은 될 수 있다. 2026년 2월 정부는 2027년 의대정원을 기존 3,058명에서 3,548명으로 490명 늘리고, 2030년 3,871명까지 단계적으로 확대하겠다고 밝혔다. 증가율은 2027년 기준 약 16.0%, 2030년 기준 약 26.6%다. 하지만 이건 정책 Stage 2일 뿐이고, 교육주 Green은 실제 수강생·repeat course·ARPU·OPM으로 확인해야 한다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters policy evidence

stage3_price:
N/A

education_stock_OHLC:
price_data_unavailable_after_deep_search

original_quota:
3,058

2027_quota:
3,548

quota_increase_2027:
490

quota_increase_2027_pct:
490 / 3,058
= +16.0%

2030_quota:
3,871

quota_increase_2030_vs_original:
813

quota_increase_2030_pct:
813 / 3,058
= +26.6%

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium / policy_watch
rerating_result = education_policy_watch
stage_failure_type = stage1_or_stage2_attention_only
```

---

## Case C — AI textbook rollback / classroom device regulation `4C-watch for edtech`

```text
symbols = Woongjin Thinkbig / YBMNet / NE Neungyule / edtech basket
case_type = 4C-watch
archetype = EDTECH_AI_TEXTBOOK_POLICY_REVERSAL
```

### stage date

```text
Stage 1:
2024~2025
- AI textbook / AI tutor / edtech policy 기대
- public-school digital transformation narrative

Stage 2:
약함
- AI 교육정책 자체는 Stage 1~2 attention

Stage 3:
없음
- AI textbook adoption만으로 Green 금지

Stage 4C-watch:
2025-08
- AI textbooks reclassified from official textbooks to supplementary materials
- teacher/parent backlash
- classroom mobile/digital-device ban passed, effective 2026-03
```

R12 교육·에듀테크에서 가장 중요한 건 “AI 교육”이라는 말이 아니라, 실제 학교 채택과 예산이다. Business Insider는 한국 국회가 AI 교과서를 공식 교과서가 아니라 보조자료로 재분류했다고 보도했고, 교사·학부모 반발과 준비 부족이 핵심 원인이었다고 정리했다. Reuters도 한국이 2026년 3월부터 교실 내 휴대전화·디지털기기 사용을 전국적으로 금지하는 법안을 통과시켰다고 보도했다. 즉 edtech basket은 정책 기대와 동시에 policy-friction 4C-watch를 붙여야 한다. ([Business Insider][3])

### 실제 가격경로 검증

```text
price_data_source:
Business Insider / Reuters policy evidence

stage3_price:
N/A

edtech_stock_OHLC:
price_data_unavailable_after_deep_search

AI_textbook_status:
official textbook → supplementary material

phone_device_ban_effective:
2026-03

students_social_media_affects_daily_life:
37%

students_anxious_without_social_media:
22%

digital_device_exception:
disability / educational purpose

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = edtech_policy_friction_watch
stage_failure_type = should_have_been_yellow_or_red
```

---

## Case D — fertility / childcare / care-service basket `success_candidate / demographic policy event`

```text
symbols = childcare / infant goods / education / care-service basket
case_type = success_candidate + event_premium
archetype = CHILDCARE_DEMOGRAPHIC_POLICY_EVENT
```

### stage date

```text
Stage 1:
2024~2025
- low-birthrate policy push
- childcare support / parental leave / corporate childbirth bonus
- foreign housekeeper pilot

Stage 2:
2025-02-26 / 2026-02-25
- 2024 fertility rate rises to 0.75 from 0.72
- 2025 fertility rate rises again to 0.80
- marriages +8.1% in 2025
- births +6.8% in 2025
- foreign housekeeper pilot: 100 Filipina workers, possible 1,200 expansion if successful

Stage 3:
없음
- 출산율 반등과 정책만으로 Green 금지
- 실제 childcare demand, paid enrollment, utilization, margin, repeat revenue 확인 필요

Stage 4B:
출산율 반등 headline로 유아·교육·돌봄주가 먼저 급등하면 후보

Stage 4C:
fertility rebound가 일시적이면 실패, 학령인구 감소 지속, 돌봄 인건비 부담, 정책 축소
```

R12의 저출산/돌봄 테마는 Stage 2까지는 가능하다. Reuters는 한국의 합계출산율이 2023년 0.72에서 2024년 0.75로 9년 만에 반등했고, 2025년에는 0.80으로 2년 연속 상승했다고 보도했다. 2025년 혼인은 8.1%, 출생아는 6.8% 증가했다. FT는 외국인 가사·돌봄 근로자 pilot이 100명 규모로 시작되고, 성공 시 1,200명까지 확대될 수 있다고 보도했다. 그러나 childcare/infant-goods/education stocks의 Green은 실제 유료수요·utilization·margin으로 확인해야 한다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters fertility data + FT foreign-housekeeper policy anchor

stage3_price:
N/A

childcare_stock_OHLC:
price_data_unavailable_after_deep_search

fertility_rate_2023:
0.72

fertility_rate_2024:
0.75

fertility_rate_2025:
0.80

fertility_rebound_2023_to_2025:
0.80 / 0.72 - 1
= +11.1%

marriages_2025:
+8.1%

births_2025:
+6.8%

foreign_housekeeper_pilot:
100 Filipina workers

possible_expansion:
1,200 workers by mid-next year if successful

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate / event_premium
rerating_result = demographic_childcare_policy_watch
stage_failure_type = stage2_policy_not_green
```

---

## Case E — kimchi cabbage / food-input shock `4C-watch for food processors`

```text
symbols = Daesang / CJ CheilJedang / kimchi-food processing basket
case_type = 4C-watch
archetype = AGRI_FOOD_INPUT_COST_SHOCK
```

### stage date

```text
Stage 1:
2024-09~10
- hot weather damages napa cabbage crop
- kimchi input-cost inflation
- climate-adaptation / storage policy

Stage 2:
없음
- 원가 shock은 positive stage가 아니라 RedTeam input

Stage 3:
없음
- 식품 가격 상승만으로 Green 금지

Stage 4C-watch:
2024-10-23
- government releases 24,000 tonnes cabbage from national stocks
- wholesale cabbage price jumped to 9,537 won in mid-September from around 3,000 won in early July
- late October price 5,610 won
```

김치·식품가공 basket은 원재료 가격 shock을 꼭 RedTeam에 넣어야 한다. Reuters는 이상고온으로 배추 작황이 악화되자 정부가 김장철을 앞두고 24,000톤의 배추를 방출하기로 했고, 배추 도매가격은 7월 초 약 3,000원에서 9월 중순 9,537원까지 급등했다가 10월 말 5,610원으로 내려왔다고 보도했다. 별도 Reuters 기사에서는 고랭지 배추 재배면적이 20년 전 8,796ha에서 전년 3,995ha로 줄었고, 기후변화가 구조적 위협이라고 설명했다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters crop/input-cost evidence

stage3_price:
N/A

food_processor_stock_OHLC:
price_data_unavailable_after_deep_search

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
= -37.2%

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
rerating_result = agri_food_input_cost_watch
stage_failure_type = 4C_watch_not_green
```

---

## Case F — feed wheat / livestock input cost `4C-watch`

```text
symbols = Harim / Maniker / Farm Story / livestock-feed basket
case_type = 4C-watch
archetype = FEED_GRAIN_INPUT_COST_4C
```

### stage date

```text
Stage 1:
2025~2026
- grain price / FX / feed cost pressure
- livestock processor margin risk

Stage 2:
없음
- 사료곡물 가격 상승은 positive evidence가 아님

Stage 3:
없음

Stage 4C-watch:
2026-05-13
- Korea Feed Leaders Committee believed to make no purchase in 65,000-ton feed wheat tender
- prices regarded too high
- lowest offer $298.50/t c&f + $2/t surcharge
```

R12 축산·사료 basket은 곡물 input cost를 강하게 봐야 한다. Reuters는 한국 Feed Leaders Committee가 최대 65,000톤 사료용 밀 tender에서 구매를 하지 않은 것으로 보인다고 보도했고, 이유는 미국 밀 futures 급등 이후 제시 가격이 너무 높았기 때문이라고 전했다. 최저 제안가는 Cargill의 $298.50/t c&f에 추가 하역 surcharge $2/t였다. 이건 Harim/Maniker/Farm Story 같은 축산·사료 관련주에 cost 4C-watch다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters feed-wheat tender evidence

stage3_price:
N/A

livestock_feed_stock_OHLC:
price_data_unavailable_after_deep_search

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

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = feed_grain_input_cost_watch
stage_failure_type = 4C_watch_not_green
```

---

## Case G — dog-meat ban / pet-welfare transition `policy event, not Green`

```text
symbols = pet-food / animal-welfare / livestock-transition basket
case_type = event_premium / policy_watch
archetype = PET_WELFARE_POLICY_TRANSITION
```

### stage date

```text
Stage 1:
2024-09-26
- dog-meat ban transition
- pet / animal-welfare policy
- shelter / adoption / pet-food demand narrative

Stage 2:
2027-02 effective ban 예정
- government support about 100B won
- farmers can receive up to 600,000 won per surrendered dog
- nearly half a million dogs to be rehomed / adopted / sheltered

Stage 3:
없음
- 정책전환만으로 Green 금지
- actual pet-food demand, shelter-service revenue, adoption services, margin 확인 필요

Stage 4B:
펫/동물복지 테마주가 정책 발표만으로 먼저 급등하면 후보

Stage 4C:
shelter capacity failure, subsidy dissatisfaction, policy delay, transition cost burden
```

개식용 금지 전환은 R12에서 animal-welfare / pet-market policy event로 볼 수 있다. Reuters는 한국 정부가 2027년 초 시행될 개식용 금지에 앞서 약 1,000억 원을 투입해 농가·식당 전환을 지원하고, 사육견 약 50만 마리를 입양·보호시설로 전환하려 한다고 보도했다. 농가는 반납하는 개 한 마리당 최대 600,000원을 받을 수 있다. 하지만 이것은 정책 이벤트이지, 상장 pet-food/service 기업의 매출 evidence는 아니다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters dog-meat ban / transition policy evidence

stage3_price:
N/A

pet_welfare_stock_OHLC:
price_data_unavailable_after_deep_search

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

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium / policy_watch
rerating_result = pet_welfare_transition_watch
stage_failure_type = stage1_or_stage2_attention_only
```

---

## Case H — Kyochon / Cherrybro / Neuromeka `overheat / celebrity food event`

```text
symbols = 339770 / 066360 / 348340
case_type = overheat / price_moved_without_evidence
archetype = FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM
```

### stage date

```text
Stage 1:
2025-10-31
- Jensen Huang fried-chicken dinner
- APEC / Nvidia Korea AI-chip contracts
- Korean fried chicken meme event

Stage 2:
없음
- 실제 store traffic / franchise sales / margin 확인 전

Stage 3:
없음

Stage 4B:
2025-10-31
- Kyochon F&B surged up to 20%
- Cherrybro hit daily limit around 30%
- Neuromeka also jumped
- event driven by viral dinner at non-listed Kkanbu Chicken

Stage 4C:
viral fade, traffic not converting to repeat sales, chicken input-cost pressure, franchise margin miss
```

이건 R12에서 가장 깨끗한 `price_moved_without_evidence`다. Jensen Huang이 삼성전자·현대차 경영진과 비상장 Kkanbu Chicken에서 치킨을 먹은 장면이 퍼지자, 상장 동종주인 Kyochon F&B와 Cherrybro, chicken-frying robot maker Neuromeka가 급등했다. Tom’s Hardware는 Kyochon이 장중 최대 20%, Cherrybro가 일일 제한폭 30%까지 올랐다고 정리했고, MarketWatch는 Neuromeka만 장 마감까지 상승분을 유지했다고 보도했다. 실제 store traffic, same-store sales, franchise margin은 확인되지 않았다. ([Tom's Hardware][8])

### 실제 가격경로 검증

```text
price_data_source:
Tom's Hardware / MarketWatch event-return summary

stage3_price:
N/A

Kyochon_event_MFE:
up to +20%

Cherrybro_event_MFE:
up to daily limit +30%

Neuromeka_event:
jumped, only one of the three to retain gains by close according to MarketWatch

fundamental_revenue_evidence:
not confirmed

event_driver:
viral dinner at non-listed Kkanbu Chicken, not confirmed sales event

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
success
- revenue evidence 전 +20~30%면 4B/event premium.
```

### alignment

```text
score_price_alignment = price_moved_without_evidence
rerating_result = celebrity_food_event_premium
stage_failure_type = should_have_been_stage1_or_4B_watch
```

---

# 5. 이번 R12 case별 요약표

| case                            | 분류                    |                                               실제 가격검증 | alignment         |
| ------------------------------- | --------------------- | ----------------------------------------------------: | ----------------- |
| Coway                           | structural_success 후보 |                            렌탈 구조 확인, OHLC unavailable | success_candidate |
| 의대정원 / 교육 basket                | event premium         |                quota 3,058→3,548→3,871, +16.0%/+26.6% | policy watch      |
| AI textbook / classroom ban     | 4C-watch              |                  AI textbook 보조자료화, phone ban 2026-03 | edtech friction   |
| childcare / fertility basket    | success_candidate     |    fertility 0.72→0.80, marriages +8.1%, births +6.8% | policy Stage 2    |
| kimchi cabbage input            | 4C-watch              |     cabbage 3,000→9,537 won, +217.9%; 24,000t release | input-cost watch  |
| feed wheat / livestock          | 4C-watch              | 65,000t tender no purchase, effective offer $300.50/t | feed-cost watch   |
| dog-meat ban / pet transition   | event premium         |             support 100B won, 500k dogs, 600k won/dog | policy event      |
| Kyochon / Cherrybro / Neuromeka | overheat              |   Kyochon +20%, Cherrybro +30%, revenue not confirmed | price-only        |

---

# 6. score-price alignment 판정

```text
success_candidate:
- Coway
- childcare / fertility policy basket

event_premium:
- medical quota education basket
- dog-meat ban / pet-welfare transition
- Kyochon / Cherrybro / Neuromeka fried-chicken event

price_moved_without_evidence:
- Kyochon / Cherrybro / Neuromeka
- dog-meat ban pet transition rally if actual pet-service revenue not confirmed
- medical quota education rally before paid-enrollment / ARPU evidence

thesis_break_watch:
- AI textbook rollback / classroom device regulation
- kimchi cabbage input shock
- feed wheat / livestock input cost

unknown_insufficient_evidence:
- Coway 최신 rental accounts / churn / ARPU / FCF
- childcare basket company-level utilization / margin

4B-watch:
- celebrity food event +20~30%
- medical quota education rally before actual enrollment
- low-birthrate reversal policy rally before revenue
- pet-welfare policy rally before monetization

4C-watch:
- edtech policy rollback
- food/agri input cost spike
- feed grain price spike
- subsidy/policy transition failure

hard_4C_confirmed:
- false
```

---

# 7. 점수비중 교정

## 올릴 축

```text
recurring_revenue +5
churn_stability +5
ARPU_or_repeat_purchase +4
unit_economics +5
cash_conversion +5
paid_enrollment_conversion +4
utilization_rate +4
input_cost_pass_through +5
inventory_quality +4
subsidy_independence +4
```

### 왜 올리나

Coway 같은 렌탈 기업은 R12에서 가장 구조적인 Stage 3 후보가 될 수 있다. 하지만 렌탈 계정·churn·ARPU·FCF가 확인되어야 한다. 교육·돌봄·펫·농식품도 정책보다 실제 유료수요와 가격전가가 중요하다.

## 내릴 축

```text
policy_news_only -5
education_quota_only -5
AI_textbook_theme_only -5
birthrate_headline_only -4
pet_welfare_policy_only -4
celebrity_food_event_only -5
input_price_spike_without_pass_through -5
subsidy_dependent_revenue -4
unconfirmed_demand_conversion -5
```

### 왜 내리나

의대정원은 교육주 수요 가능성을 만들지만, 곧바로 매출은 아니다. 출산율 반등도 childcare revenue로 바로 닫히지 않는다. 김치 배추와 사료곡물 가격 shock은 식품·축산 기업의 margin risk다. Jensen Huang chicken event는 매출 evidence 없이 주가만 뛴 대표적인 4B다.

## Green gate 강화 조건

```text
R12 Stage 3-Green 필수:
1. 반복매출 또는 반복구매 확인
2. churn / retention 안정
3. ARPU 또는 가격전가 확인
4. paid enrollment / utilization / service usage 확인
5. unit economics 확인
6. cash conversion 확인
7. input cost pass-through 확인
8. 재고·매출채권 안정
9. 보조금 의존도 낮음
10. 가격경로가 evidence 이후 따라옴

금지:
정책 뉴스만 있음
의대정원 headline만 있음
AI textbook theme만 있음
출산율 반등만 있음
pet-welfare policy만 있음
농산물 가격 spike만 있음
celebrity food event만 있음
```

## 4B 조기감지 조건

```text
4B-watch:
정책 뉴스로 교육/돌봄/펫/스마트팜주 급등
의대정원 뉴스로 사교육주가 실제 수강생 증가 전 급등
출산율 반등으로 유아·교육주가 먼저 급등
농산물 shock으로 식품주가 가격전가 전 급등
celebrity food event로 외식·축산·robotics 관련주 급등
방어주·렌탈주가 성장률보다 multiple이 먼저 오름

4B-elevated:
churn 상승
input cost 상승
재고 증가
수강생 전환 미확인
보조금 축소
정책 후퇴
event fade
```

## 4C hard gate 조건

```text
product recall
churn spike
ARPU 하락
paid enrollment failure
AI education policy rollback
subsidy withdrawal
food-input cost spike without pass-through
feed-cost shock
inventory build
cash conversion deterioration
celebrity event fade
policy transition failure
```

이번 R12 Loop 10에서는 hard 4C를 억지로 확정하지 않는다. `AI textbook rollback`, `kimchi cabbage input shock`, `feed wheat input shock`은 강한 4C-watch이고, `Kyochon/Cherrybro/Neuromeka`는 4B/event premium이다.

---

# 8. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
```

---

# 9. patch-ready 출력

## docs/round/round_170.md 요약

```md
# R12 Loop 10. Agriculture / Life Service / Misc Price Validation

이번 라운드는 R12 Loop 10 price-validation 라운드다.

핵심 결론:
- Coway remains the cleanest recurring-service Stage 3 candidate in R12, but rental accounts, churn, ARPU, OPM/FCF and raw OHLC were unavailable in this pass.
- Medical-school quota policy is education Stage 1/2, not Green. Quota rises from 3,058 to 3,548 in 2027 and 3,871 by 2030, but actual paid enrollment, ARPU and OPM are required.
- AI textbook rollback and classroom device ban are edtech 4C-watch. AI textbooks were reclassified as supplementary materials, and classroom phone/device ban takes effect in March 2026.
- Fertility/childcare policy is Stage 2. Fertility rose from 0.72 in 2023 to 0.80 in 2025, marriages +8.1%, births +6.8%, and foreign housekeeper pilot may expand from 100 to 1,200 workers. Company revenue conversion required.
- Kimchi cabbage climate/input shock is 4C-watch. Government releases 24,000 tonnes of cabbage; cabbage price jumped from around 3,000 won to 9,537 won, then fell to 5,610 won.
- Feed wheat/livestock input cost is 4C-watch. Korea FLC made no purchase in a 65,000t feed wheat tender because prices were too high; effective low offer was about $300.50/t.
- Dog-meat ban / pet-welfare transition is policy event, not Green. Government support about 100B won, nearly 500k dogs, up to 600k won per surrendered dog.
- Kyochon/Cherrybro/Neuromeka fried-chicken event is price_moved_without_evidence. Kyochon surged up to 20%, Cherrybro up to 30%, but store traffic/same-store sales/margin were not confirmed.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 170 R12 Loop 10 Agri Life Service Misc Price Validation

## 반영 내용
- R12 Loop 10 price-validation 라운드를 추가했다.
- Recurring rental, medical quota education policy, AI textbook rollback, fertility/childcare policy, kimchi cabbage input shock, feed wheat livestock cost, dog-meat ban pet transition, fried-chicken celebrity event를 비교했다.
- Reuters/FT/AP/MarketWatch/Tom’s Hardware/Business Insider/public-company anchors로 가능한 MFE/MAE 및 policy/input-cost/event metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- recurring revenue, churn stability, ARPU, paid enrollment conversion, utilization, input-cost pass-through, unit economics, cash conversion 가중치 강화
- education quota-only, AI textbook theme-only, birthrate headline-only, pet policy-only, input-price spike without pass-through, celebrity food event-only 감점 강화
- R12 4B-watch와 input-cost / edtech policy 4C-watch 민감도 강화
```

## case row 초안

```jsonl
{"case_id":"r12_loop10_coway_recurring_rental_watch","symbol":"021240","company_name":"Coway","case_type":"success_candidate","primary_archetype":"HOME_LIVING_RENTAL_RECURRING","stage1_date":"2024-2026","price_validation":{"price_data_source":"public company profile","stage3_price":null,"business_anchor":"water purifier / air purifier / bidet / mattress rental recurring model","overseas_subsidiaries":["Malaysia","United States","Thailand","Indonesia","Vietnam","Europe","Japan","China"],"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"recurring_service_rerating_candidate","notes":"Recurring rental structure is R12 Stage 3 candidate, but rental accounts, churn, ARPU, OPM/FCF and OHLC are required."}
{"case_id":"r12_loop10_medical_quota_private_education_watch","symbol":"215200/YBMNet/NE_Neungyule/Woongjin_Thinkbig_basket","company_name":"Medical quota / private education basket","case_type":"event_premium","primary_archetype":"EDUCATION_POLICY_MEDICAL_QUOTA","stage2_date":"2026-02-10","price_validation":{"price_data_source":"Reuters policy evidence","stage3_price":null,"original_quota":3058,"quota_2027":3548,"quota_increase_2027":490,"quota_increase_2027_pct":16.0,"quota_2030":3871,"quota_increase_2030_vs_original":813,"quota_increase_2030_pct":26.6,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_policy_watch","rerating_result":"education_policy_watch","notes":"Medical quota is Stage 1/2; paid enrollment, repeat course, ARPU, OPM and cash conversion required before Green."}
{"case_id":"r12_loop10_edtech_ai_textbook_rollback_phone_ban","symbol":"Woongjin_Thinkbig/YBMNet/NE_Neungyule_edtech_basket","company_name":"Edtech / AI textbook / classroom device regulation basket","case_type":"4c_watch","primary_archetype":"EDTECH_AI_TEXTBOOK_POLICY_REVERSAL","stage4c_date":"2025-08/2026-03","price_validation":{"price_data_source":"Business Insider/Reuters policy evidence","stage3_price":null,"ai_textbook_status":"official_textbook_to_supplementary_material","phone_device_ban_effective":"2026-03","students_social_media_affects_daily_life_pct":37,"students_anxious_without_social_media_pct":22,"digital_device_exception":"disability_or_educational_purpose","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"edtech_policy_friction_watch","notes":"AI education theme is blocked by textbook rollback and classroom-device regulation until actual school adoption and revenue are proven."}
{"case_id":"r12_loop10_childcare_fertility_policy_watch","symbol":"childcare/infant_goods/education/care_service_basket","company_name":"Fertility / childcare / care-service basket","case_type":"success_candidate","primary_archetype":"CHILDCARE_DEMOGRAPHIC_POLICY_EVENT","stage2_date":"2025-02-26/2026-02-25","price_validation":{"price_data_source":"Reuters fertility data + FT foreign-housekeeper policy anchor","stage3_price":null,"fertility_rate_2023":0.72,"fertility_rate_2024":0.75,"fertility_rate_2025":0.80,"fertility_rebound_2023_to_2025_pct":11.1,"marriages_2025_growth_pct":8.1,"births_2025_growth_pct":6.8,"foreign_housekeeper_pilot_workers":100,"possible_expansion_workers":1200,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_event_premium","rerating_result":"demographic_childcare_policy_watch","notes":"Fertility rebound and care policy are Stage 2; paid demand, utilization, margin and recurring revenue required before Green."}
{"case_id":"r12_loop10_kimchi_cabbage_input_cost_watch","symbol":"Daesang/CJ_CheilJedang/kimchi_food_processing_basket","company_name":"Kimchi cabbage / agri-food input cost basket","case_type":"4c_watch","primary_archetype":"AGRI_FOOD_INPUT_COST_SHOCK","stage4c_date":"2024-09/2024-10","price_validation":{"price_data_source":"Reuters crop/input-cost evidence","stage3_price":null,"government_cabbage_release_tonnes":24000,"cabbage_price_early_july_krw":3000,"cabbage_price_mid_sept_krw":9537,"cabbage_price_jump_pct":217.9,"cabbage_price_late_oct_krw":5610,"late_oct_vs_mid_sept_pct":-37.2,"highland_cabbage_area_20y_ago_ha":8796,"highland_cabbage_area_recent_ha":3995,"area_decline_pct":-54.6,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"agri_food_input_cost_watch","notes":"Cabbage climate/input shock is 4C-watch unless food processors prove pass-through and margin stability."}
{"case_id":"r12_loop10_feed_wheat_livestock_input_cost_watch","symbol":"Harim/Maniker/Farm_Story/feed_livestock_basket","company_name":"Feed wheat / livestock input-cost basket","case_type":"4c_watch","primary_archetype":"FEED_GRAIN_INPUT_COST_4C","stage4c_date":"2026-05-13","price_validation":{"price_data_source":"Reuters feed-wheat tender evidence","stage3_price":null,"tender_volume_tonnes":65000,"purchase_result":"believed_no_purchase","lowest_offer_usd_per_t":298.5,"extra_unloading_surcharge_usd_per_t":2.0,"effective_lowest_offer_usd_per_t":300.5,"effective_offer_for_65000t_usd_mn":19.53,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"feed_grain_input_cost_watch","notes":"High feed-wheat cost is 4C-watch for feed/livestock processors until pass-through and inventory quality confirm."}
{"case_id":"r12_loop10_dog_meat_ban_pet_welfare_transition","symbol":"pet_food/animal_welfare/livestock_transition_basket","company_name":"Dog-meat ban / pet-welfare transition basket","case_type":"event_premium","primary_archetype":"PET_WELFARE_POLICY_TRANSITION","stage1_date":"2024-09-26","stage2_date":"2027-02_effective_ban","price_validation":{"price_data_source":"Reuters dog-meat ban / transition policy evidence","stage3_price":null,"government_support_krw_bn":100,"dogs_to_rehome":500000,"farmer_subsidy_per_dog_krw":600000,"dog_breeding_farms":1500,"slaughter_houses":200,"restaurants_serving_dog_meat":2300,"ban_effective":"2027-02","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_policy_watch","rerating_result":"pet_welfare_transition_watch","notes":"Dog-meat ban transition is Stage 1/2 policy event; pet-food/service revenue conversion required before Green."}
{"case_id":"r12_loop10_kyochon_cherrybro_neuromeka_jensen_event","symbol":"339770/066360/348340","company_name":"Kyochon F&B / Cherrybro / Neuromeka","case_type":"overheat","primary_archetype":"FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM","stage1_date":"2025-10-31","stage4b_date":"2025-10-31","price_validation":{"price_data_source":"Tom's Hardware/MarketWatch event-return summary","stage3_price":null,"kyochon_event_mfe_pct":20,"cherrybro_event_mfe_pct":30,"neuromeka_event":"jumped; only one of the three to retain gains by close according to MarketWatch","fundamental_revenue_evidence_confirmed":false,"event_driver":"viral dinner at non-listed Kkanbu Chicken","price_validation_status":"reported_event_return_not_full_ohlc"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"celebrity_food_event_premium","notes":"Celebrity fried-chicken event is 4B/event premium until store traffic, same-store sales, franchise margin and repeat demand confirm."}
```

## shadow weight row 초안

```csv
archetype,recurring_revenue,churn_stability,arpu_or_repeat_purchase,paid_conversion,unit_economics,cash_conversion,input_cost_pass_through,inventory_quality,subsidy_independence,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
HOME_LIVING_RENTAL_RECURRING,+5,+5,+4,+3,+5,+5,+2,+4,+3,-1,+3,+4,Coway recurring rental can be Stage 3 candidate but needs accounts/churn/ARPU/FCF.
EDUCATION_POLICY_MEDICAL_QUOTA,+3,+2,+5,+5,+4,+4,+0,+1,+2,-5,+5,+4,Medical quota is event until paid enrollment/ARPU/OPM confirm.
EDTECH_AI_TEXTBOOK_POLICY_REVERSAL,+2,+2,+3,+4,+4,+4,+0,+1,+2,-5,+4,+4,AI textbook rollback and phone ban create edtech policy friction.
CHILDCARE_DEMOGRAPHIC_POLICY_EVENT,+4,+3,+4,+5,+4,+4,+1,+1,+3,-4,+5,+3,Fertility rebound is Stage 2; company utilization and recurring revenue must confirm.
AGRI_FOOD_INPUT_COST_SHOCK,+2,+0,+3,+2,+4,+4,+5,+5,+2,-4,+4,+4,Kimchi cabbage shock requires pass-through and inventory control.
FEED_GRAIN_INPUT_COST_4C,+2,+0,+2,+1,+4,+4,+5,+5,+2,-4,+4,+4,Feed wheat cost spike is 4C-watch for livestock/feed names.
PET_WELFARE_POLICY_TRANSITION,+2,+2,+3,+3,+4,+4,+1,+2,+3,-5,+5,+3,Dog-meat ban is policy event until pet/service monetization confirms.
FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM,+2,+0,+3,+3,+4,+4,+3,+3,+1,-5,+5,+3,Celebrity food event is price_moved_without_evidence until traffic and margins confirm.
```

---

# 이번 R12 Loop 10 결론

R12는 **좋은 구조 후보와 잡음성 이벤트가 같이 섞이는 섹터**다. 그래서 Green gate는 느리게, 4B/Event Premium 분리는 빠르게 해야 한다.

```text
1. Coway는 R12에서 가장 구조적인 recurring-service 후보지만,
   rental accounts, churn, ARPU, FCF 확인 전 Stage 3는 보류다.

2. 의대정원 정책은 사교육주 Stage 1~2 이벤트다.
   실제 paid enrollment, repeat course, ARPU, OPM이 Stage 3다.

3. AI textbook rollback과 classroom phone ban은 edtech 4C-watch다.
   AI 교육 theme만으로 Green을 주면 안 된다.

4. 출산율 반등과 돌봄정책은 childcare/care-service Stage 2다.
   실제 유료수요와 utilization 전에는 Green이 아니다.

5. 김치 배추와 사료곡물 shock은 농식품·축산 basket의 input-cost 4C-watch다.
   가격전가와 재고 안정이 확인되어야 한다.

6. dog-meat ban은 pet/welfare transition policy event다.
   실제 pet-food/service revenue 전에는 Stage 3가 아니다.

7. Kyochon/Cherrybro/Neuromeka Jensen event는 대표적 price_moved_without_evidence다.
   매출 evidence 전 +20~30%는 4B다.
```

한 문장으로 압축하면:

> **R12에서 진짜 Stage 3는 “정책·교육·출산·농산물·생활서비스 테마가 좋아 보인다”가 아니라, 반복매출·유료전환·unit economics·가격전가·현금전환이 실제로 확인되는 순간이다.**
> **이번 R12 Loop 10은 렌탈·돌봄 같은 구조 후보를 인정하되, 교육정책·농산물 shock·펫정책·celebrity food event를 먼저 4B/Event Premium 또는 4C-watch로 분리하는 라운드다.**

[1]: https://en.wikipedia.org/wiki/Coway_%28company%29?utm_source=chatgpt.com "Coway (company)"
[2]: https://www.reuters.com/business/healthcare-pharmaceuticals/south-korea-revives-plan-add-medical-students-doctors-criticise-bid-2026-02-10/?utm_source=chatgpt.com "South Korea revives plan to add medical students; doctors criticise bid"
[3]: https://www.businessinsider.com/ai-in-school-south-korea-textbook-rollback-jobs-education-2025-8?utm_source=chatgpt.com "Why South Korea's AI rollback in classrooms is a cautionary tale for the US"
[4]: https://www.reuters.com/world/asia-pacific/south-korea-birthrate-rises-first-time-9-years-marriages-surge-2025-02-26/?utm_source=chatgpt.com "South Korea birthrate rises for first time in 9 years, marriages surge"
[5]: https://www.reuters.com/world/asia-pacific/south-korea-supply-stocks-kimchi-cabbage-after-hot-weather-damages-crop-2024-10-23/?utm_source=chatgpt.com "South Korea to supply stocks of kimchi cabbage after hot weather damages crop"
[6]: https://www.reuters.com/world/asia-pacific/south-koreas-flc-believed-make-no-purchase-65000-ton-feed-wheat-tender-traders-2026-05-13/?utm_source=chatgpt.com "South Korea's FLC believed to make no purchase in 65,000 ton feed wheat tender, traders say"
[7]: https://www.reuters.com/world/asia-pacific/south-korea-offers-incentives-adoptions-ahead-ban-farming-dogs-food-2024-09-26/?utm_source=chatgpt.com "South Korea offers incentives, adoptions ahead of ban on farming dogs for food"
[8]: https://www.tomshardware.com/tech-industry/korean-fried-chicken-stocks-surge-30-percent-as-nvidia-ceo-jensen-huang-dines-out-on-local-delicacy-entire-industry-buoyed-by-secret-ingredient-jensanity?utm_source=chatgpt.com "Korean fried chicken stocks surge 30% as Nvidia CEO Jensen Huang dines out on local delicacy - entire industry buoyed by secret ingredient, Jensanity"

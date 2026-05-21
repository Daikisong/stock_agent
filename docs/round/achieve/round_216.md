순서상 이번은 **R12 Loop 8 — 농업·생활서비스·기타 가격경로 검증 라운드**다.

이번 R12는 R5 소비재와 비슷해 보이지만, 더 조심해야 한다. 코웨이처럼 반복서비스 구조가 있는 기업은 Stage 3 후보가 될 수 있지만, 농기계·교육정책·조류독감·스마트팜·생활서비스 이벤트는 대부분 **Stage 1~2 또는 event premium**에 머문다.

이번에도 원시 수정주가 일봉 OHLC를 안정적으로 직접 추출하지 못한 종목은 숫자를 만들지 않았다. 대신 Reuters / AP / Tom’s Hardware / arXiv / 공개 기업정보에 남은 **가격 anchor, 이벤트 수익률, 정책·수요·기술 지표**로 계산 가능한 값만 계산했다.

```text
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
r12_default_stage3_bias = conservative_except_recurring_service
```

---

# 1. 이번 라운드 대섹터

```text
R12 = 농업·생활서비스·기타
large_sector = AGRI_LIFE_SERVICE_MISC
round = R12 Loop 8 / price-path validation
```

R12의 핵심은 “방어적이다”, “정책 수혜다”, “질병 이벤트다”, “스마트팜이다”가 아니라, **반복매출·unit economics·현금전환·규제 통과·가격전가·재고 안정**이 확인되는가다.

---

# 2. 대상 canonical archetype

```text
HOME_LIVING_APPLIANCE_RENTAL
AGRI_MACHINERY_DEMAND_CYCLE
AGRI_MACHINERY_SOFTWARE_LOCKIN
EDUCATION_SPECIALTY_SERVICES
HOME_CHILD_EDUCATION
EDTECH_AI_DISRUPTION
EDUCATION_POLICY_EVENT
LIVESTOCK_DISEASE_PRICE_REGULATORY
AGRI_DISEASE_EVENT_OVERLAY
FOOD_SERVICE_EVENT_PREMIUM
SMART_FARM_AGRI_TECH
VERTICAL_FARMING_UNIT_ECONOMICS
CONSUMER_REGULATED_PRODUCT
PRICE_ONLY_RALLY
EVENT_PREMIUM
```

이번 R12의 핵심 질문은 이거다.

```text
생활서비스·농업·교육·질병·스마트팜 테마인가?
아니면 반복매출, 가격전가, unit economics, 현금전환이 확인되는가?
```

---

# 3. deep sub-archetype

```text
렌탈 / 생활서비스:
- Coway
- water purifier rental
- air purifier / bidet / mattress rental
- Malaysia / overseas subsidiaries
- recurring account base
- churn / ARPU / service network
- product safety / recall risk

농기계:
- Daedong / KIOTI
- TYM
- North America tractor channel
- dealer sell-through
- inventory / financing
- autonomous tractor / precision agriculture
- export cycle

교육:
- MegaStudy Education
- medical school quota policy
- repeat course / ARPU
- phone ban / edtech friction
- AI education disruption
- birth-rate structural decline

축산 / 생활 이벤트:
- Brazil bird flu
- import restriction / easing
- Harim / Maniker / poultry basket
- Kyochon / chicken franchise event
- one-off disease demand
- celebrity / viral food event

스마트팜:
- Green Plus / Woomdungi Farm류
- greenhouse automation
- adoption barrier
- government subsidy
- unit economics
- maintenance / recurring service
```

---

# 4. 국장 신규 후보 case

## Case A — 코웨이 `structural_success 후보 / recurring rental service`

```text
symbol = 021240
case_type = structural_success 후보
archetype = HOME_LIVING_APPLIANCE_RENTAL
```

### evidence

코웨이는 정수기·공기청정기·비데·매트리스 등 생활가전 렌탈 기반의 반복서비스 기업이다. 공개 기업정보 기준 코웨이는 국내 최대 정수기 기업이고, 말레이시아·미국·태국·인도네시아·베트남·유럽·일본·중국 등에 해외 법인을 보유한다. 특히 말레이시아는 코웨이 해외 매출의 핵심 지역으로 정리된다. 다만 이번 pass에서는 최신 KRX/Naver/Yahoo OHLC와 최신 IR 원문 숫자를 안정적으로 직접 확보하지 못했기 때문에 Stage 3 확정은 보류한다. ([위키백과][1])

### stage date

```text
Stage 1:
2022~2025
- 정수기 / 공기청정기 / 비데 / 매트리스 렌탈 계정 기반 반복매출
- 말레이시아 등 해외 계정 성장

Stage 2:
보류
- 최신 IR에서 rental account growth, ARPU, churn, overseas revenue, OPM 확인 필요

Stage 3:
조건부 후보
- recurring revenue + churn stability + overseas growth + FCF conversion 확인 시 가능

Stage 4B:
렌탈 안정성만으로 valuation이 과도하게 확장되면 후보

Stage 4C:
제품 안전 리콜, churn 상승, 해외 성장 둔화, Netmarble 지배구조/자본배분 훼손 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Public company profile / Yahoo-reference summary only

stage3_price:
price_data_unavailable_after_deep_search

reason:
- Reuters / WSJ / MarketWatch / FT에서 코웨이 최신 주가 reaction anchor를 찾지 못함.
- KRX / Naver / Yahoo / Stooq 원시 일봉 OHLC를 이번 세션에서 안정적으로 직접 확보하지 못함.
- 최신 IR 원문 숫자도 이번 pass에서 직접 확인 실패.

known_business_anchor:
domestic largest water purifier company
global subsidiaries present
rental-service recurring model

MFE_30D / 90D / 180D / 1Y / 2Y:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
price_data_unavailable_after_deep_search

peak_price:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = recurring_service_rerating_candidate
stage_failure_type = stage2_watch_success 후보
```

### 교정

코웨이는 R12에서 거의 유일하게 “진짜 Stage 3 후보”가 될 수 있는 구조다. 다만 Green은 브랜드 안정성이 아니라 **렌탈 계정 증가·churn 안정·ARPU·OPM·FCF**로만 준다.

---

## Case B — 대동 / TYM `success_candidate / agri machinery export watch`

```text
symbols = 000490 / 002900
case_type = success_candidate / insufficient_evidence
archetype = AGRI_MACHINERY_DEMAND_CYCLE / AGRI_MACHINERY_SOFTWARE_LOCKIN
```

### evidence

대동은 KIOTI 브랜드로 북미 등 해외에서 알려진 농기계 기업이며, 트랙터·콤바인·UTV·엔진 등을 생산한다. TYM 역시 트랙터·콤바인·경운기·이앙기·디젤엔진 등을 생산하고 40개국 이상에서 사업하는 농기계 기업으로 정리된다. 이 구조는 R12에서 장기적으로 좋은 후보지만, 농기계는 export theme만으로는 부족하다. 북미 딜러 sell-through, 딜러 재고, 농가 financing, OPM, FCF가 확인되어야 한다. ([위키백과][2])

### stage date

```text
Stage 1:
2023~2025
- North America tractor channel
- KIOTI / TYM export narrative
- autonomous tractor / precision agriculture 기대

Stage 2:
보류
- dealer sell-through
- North America retail sales
- inventory
- financing condition
- OPM / FCF 확인 필요

Stage 3:
없음
- 농기계 export theme만으로 Green 금지

Stage 4B:
농기계 수요 회복 / 자율주행 농기계 테마로 주가가 먼저 급등하면 후보

Stage 4C:
미국 농가 수요 둔화, 딜러 재고 증가, 금융조건 악화, 농산물 가격 하락 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Public company profile evidence only

stage3_price:
N/A

stage1_price:
price_data_unavailable_after_deep_search

reason:
- Reuters / WSJ / MarketWatch / FT에서 대동·TYM의 관련 이벤트 주가 anchor를 찾지 못함.
- KRX / Naver / Yahoo / Stooq 원시 OHLC 직접 확보 실패.

business_anchor:
Daedong = KIOTI brand / tractors / combines / engines
TYM = tractors / combines / cultivators / rice transplanters / diesel engines / 40+ countries

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = unknown_insufficient_evidence
rerating_result = agri_machinery_watch
stage_failure_type = stage1_attention_only
```

### 교정

농기계는 R12에서 `export_growth`보다 `dealer_sell_through`, `inventory`, `farmer_financing`, `OPM`, `FCF`, `software/precision agriculture attachment`를 우선해야 한다.

---

## Case C — 메가스터디교육 / 교육주 `event_premium / medical-school quota policy`

```text
symbol = 215200
case_type = event_premium / policy_watch
archetype = EDUCATION_SPECIALTY_SERVICES / EDUCATION_POLICY_EVENT
```

### evidence

2025년 3월 한국 교육부는 13개월간 이어진 의료계 갈등을 해결하기 위해 2026학년도 의대 정원을 기존 약 3,000명 수준으로 동결할 수 있다고 밝혔다. 이는 2024년식 공격적 의대 증원 테마가 후퇴할 수 있음을 보여준다. 이후 2026년 2월에는 새 정부가 2027년 의대 정원을 3,548명으로 늘리고 2030년 3,871명까지 단계적으로 확대하겠다고 발표했다. 즉 교육주는 정책 이벤트에 민감하지만, 정책 방향이 계속 바뀌므로 Stage 3는 실제 수강생·ARPU·OPM으로만 줘야 한다. ([Reuters][3])

### stage date

```text
Stage 1:
2024-02 이후
- 의대 정원 확대 정책
- 의대 입시 사교육 수요 기대

Stage 2:
2025-03-07
- 2026학년도 의대 정원 동결 가능성
- 기존 강한 증원 narrative 약화

추가 Stage 2:
2026-02-10
- 2027년 의대 정원 3,548명
- 2030년 3,871명까지 단계 확대

Stage 3:
없음
- 정책 이벤트만으로 Green 금지
- 실제 수강생 증가, repeat course, ARPU, OPM 확인 필요

Stage 4B:
의대 증원 뉴스로 교육주가 먼저 급등하면 event premium 4B-watch

Stage 4C:
정책 후퇴, 사교육 규제, 학령인구 감소, AI 교육 disruption 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters / AP policy evidence

stage3_price:
N/A

stage1_price:
price_data_unavailable_after_deep_search

reason:
- Reuters / AP는 메가스터디교육 주가 reaction anchor를 제공하지 않음.
- KRX / Naver / Yahoo / Stooq 원시 OHLC 직접 확보 실패.

original_quota:
3,058

2027_quota:
3,548

quota_increase_2027:
3,548 - 3,058 = 490

quota_increase_2027_pct:
490 / 3,058 = +16.0%

2030_quota:
3,871

quota_increase_2030_vs_original:
3,871 - 3,058 = 813

quota_increase_2030_pct:
813 / 3,058 = +26.6%

MFE_5D / 20D / 60D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = event_premium / unknown_insufficient_evidence
rerating_result = education_policy_watch
stage_failure_type = stage1_or_stage2_attention_only
```

### 교정

교육주는 R12에서 정책 이벤트를 routing으로만 쓰고, Green은 **repeat course, ARPU, OPM, cash conversion** 확인 뒤에 준다.

---

## Case D — 교육/에듀테크 basket `4C-watch / classroom phone ban & edtech friction`

```text
symbols = NE능률 / YBM넷 / 웅진씽크빅 등 교육·에듀테크 basket
case_type = 4C-watch / policy_watch
archetype = EDTECH_AI_DISRUPTION / HOME_CHILD_EDUCATION
```

### evidence

2025년 8월 한국은 2026년 3월부터 학교 교실 내 휴대전화와 디지털기기 사용을 전국적으로 금지하는 법을 통과시켰다. Reuters는 중고생 37%가 소셜미디어가 일상생활에 영향을 준다고 답했고, 22%는 소셜미디어 접속이 안 되면 불안을 느낀다는 교육부 조사도 함께 전했다. 이 정책은 오프라인 학습 discipline에는 긍정적으로 해석될 수 있지만, 디지털 교재·에듀테크·교실 내 디지털 학습 플랫폼에는 friction이 될 수 있다. ([Reuters][4])

### stage date

```text
Stage 1:
2025-08-27
- 교실 내 휴대전화·디지털기기 금지 법안
- education policy / edtech friction

Stage 2:
없음
- 특정 상장사 매출 증가·감소 확인 전 policy event

Stage 3:
없음
- 정책 이벤트만으로 Green 금지

Stage 4B:
교육정책 뉴스로 교육주 basket이 급등하면 event premium

Stage 4C:
디지털 교재·에듀테크 사용 제한, AI 교육 disruption, 학령인구 감소가 매출 훼손으로 확인되면 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters policy evidence

stage3_price:
N/A

stage1_price:
price_data_unavailable_after_deep_search

reason:
- Reuters는 NE능률/YBM넷/웅진씽크빅 등 개별 주가 reaction anchor를 제공하지 않음.
- KRX / Naver / Yahoo / Stooq 원시 OHLC 직접 확보 실패.

law_effective_date:
2026-03

middle_high_students_social_media_daily_life_impact:
37%

students_anxious_without_social_media:
22%

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = policy_watch
rerating_result = education_regulation_watch
stage_failure_type = stage1_attention_only
```

### 교정

교육/에듀테크는 `policy_directionality`를 조심해야 한다. 같은 정책이 오프라인 학원에는 우호적일 수 있고, 디지털 학습 플랫폼에는 악재일 수 있다. 따라서 R12에서는 회사별 매출경로가 확인되기 전 Green 금지다.

---

## Case E — poultry basket `event_premium / one-off disease demand`

```text
symbols = Harim / Maniker / Cherrybro 등 poultry basket
case_type = event_premium / one_off_disease_event
archetype = LIVESTOCK_DISEASE_PRICE_REGULATORY / AGRI_DISEASE_EVENT_OVERLAY
```

### evidence

2025년 5월 브라질 상업농장에서 고병원성 조류독감이 확인되자 중국·EU·한국 등 주요 수입국이 브라질산 닭고기 수입제한을 적용했다. Reuters는 브라질이 세계 최대 poultry exporter이고 2024년 poultry meat 수출이 500만 톤을 넘었다고 보도했다. 하지만 2025년 6월 한국은 전국 단위 제한을 affected region 중심으로 완화했다. 즉 이 이벤트는 국내 poultry basket에 단기 MFE를 줄 수 있지만, 반복 수요가 아니라 **one-off disease event**다. ([Reuters][5])

### stage date

```text
Stage 1:
2025-05-19
- Brazil bird flu
- South Korea import restriction
- domestic poultry substitution theme

Stage 2:
보류
- 국내 업체별 판매가격, 출하량, 마진 확인 필요

Stage 3:
없음
- 질병 이벤트만으로 Green 금지

Stage 4B:
수입제한 뉴스로 poultry basket이 급등하면 4B-watch

Stage 4C:
2025-06-23
- South Korea eases restrictions
- one-off event fade
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters import restriction / easing evidence

stage3_price:
N/A

stage1_price:
price_data_unavailable_after_deep_search

reason:
- Reuters는 Harim / Maniker / Cherrybro 등 한국 poultry stock reaction anchor를 제공하지 않음.
- KRX / Naver / Yahoo / Stooq 원시 OHLC 직접 확보 실패.

Brazil_2024_poultry_exports:
>5M tons

restriction_start:
2025-05-19 Reuters report

restriction_easing:
2025-06-23

event_duration:
35 calendar days

MFE_5D / 20D / 60D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

Stage 4C 큰 하락 이전 포착 여부:
conceptual_success
- 수입제한 완화 뉴스가 event fade trigger.
```

### alignment

```text
score_price_alignment = event_premium
rerating_result = one_off_disease_event
stage_failure_type = should_have_been_stage1_or_4B_watch
```

### 교정

축산 질병 이벤트는 Stage 1이다. Stage 3는 국내 업체의 판매량 증가, 가격전가, feed cost 통과, OPM 개선이 확인될 때만 가능하다.

---

## Case F — Kyochon F&B / chicken-event basket `overheat / celebrity food event`

```text
symbols = Kyochon F&B / Cherrybro / Neuromeka 등 chicken-event basket
case_type = overheat / price_moved_without_evidence
archetype = FOOD_SERVICE_EVENT_PREMIUM / PRICE_ONLY_RALLY
```

### evidence

2025년 10월 Nvidia CEO 젠슨 황이 방한 중 삼성·현대 경영진과 Kkanbu Chicken에서 치킨·맥주를 먹은 장면이 viral해지면서 한국 fried-chicken 관련주가 급등했다. Tom’s Hardware는 Kyochon F&B 같은 KOSDAQ-listed fried chicken brands가 장중 20~30%까지 올랐고, poultry processor Cherrybro와 chicken-frying robot maker Neuromeka도 동반 상승했다고 보도했다. 이건 기업 매출·마진 evidence가 아니라 **celebrity/viral food event**다. ([Tom's Hardware][6])

### stage date

```text
Stage 1:
2025-10-31
- Jensen Huang chicken dinner viral event
- K-food / fried chicken / robotics side-theme

Stage 2:
없음
- 실제 매출, franchise traffic, order growth, margin 확인 전

Stage 3:
없음
- viral celebrity event만으로 Green 금지

Stage 4B:
2025-10-31
- Kyochon F&B 등 fried chicken basket +20~30%
- price moved before evidence

Stage 4C:
viral fade, 실제 매출 미반영, franchise margin 부진, 원가 상승 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Tom’s Hardware / Bloomberg-reported event summary

stage3_price:
N/A

reported_event_MFE_1D_range:
+20% to +30%

MFE_midpoint:
+25%

MFE_30D / 90D:
price_data_unavailable_after_deep_search

reason:
- Tom’s Hardware는 event-day 수익률 범위만 제공하고 종가 OHLC는 제공하지 않음.
- KRX / Naver / Yahoo / Stooq 원시 OHLC 직접 확보 실패.

below_stage3_price_flag:
N/A

Stage 4B peak-before 여부:
success
- 매출 evidence 전 +20~30%는 명확한 4B/event premium.
```

### alignment

```text
score_price_alignment = price_moved_without_evidence
rerating_result = celebrity_food_event_premium
stage_failure_type = should_have_been_stage1_or_4B_watch
```

### 교정

R12 생활서비스/외식 basket은 viral event를 Green으로 올리면 안 된다.

```text
내릴 축:
celebrity_event_only
viral_food_story
same-day theme basket rally

Stage 3 조건:
store traffic
same-store sales
franchise margin
repeat demand
FCF
```

---

## Case G — 스마트팜 basket `insufficient_evidence / unit economics watch`

```text
symbols = Green Plus / 우듬지팜류 smart-farm basket
case_type = insufficient_evidence
archetype = SMART_FARM_AGRI_TECH / VERTICAL_FARMING_UNIT_ECONOMICS
```

### evidence

2025년 한국 스마트팜 adoption 연구는 스마트팜 기술이 생산성과 지속가능성 측면에서 주목받고 있지만, 실제 adoption은 농가 연령, 교육 수준, 농지 규모, 정부 지원, 기술 장벽, 금융 제약에 좌우된다고 분석했다. 또 온실 내 UAV 기반 yield estimation 연구는 cherry tomato greenhouse에서 94.4% counting accuracy와 87.5% weight-estimation accuracy를 보여 기술적 가능성을 제시했지만, 이것은 상장사 단위 상업 매출이나 unit economics evidence가 아니다. ([arXiv][7])

### stage date

```text
Stage 1:
2024~2025
- smart farm / AI agriculture / labor shortage / climate adaptation narrative

Stage 2:
보류
- 회사별 commercial installation, order backlog, maintenance revenue 확인 필요

Stage 3:
없음
- 정책·기술 논문만으로 Green 금지

Stage 4B:
스마트팜 테마주가 정책/AI농업 뉴스로 먼저 급등하면 후보

Stage 4C:
설치 지연, unit economics 실패, 정부보조 축소, 농가 adoption 부진 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
arXiv smart-farm adoption / greenhouse UAV evidence

stage3_price:
N/A

stock_price:
price_data_unavailable_after_deep_search

reason:
- Reuters / WSJ / MarketWatch / FT에서 Green Plus / 우듬지팜류 smart-farm stock reaction anchor를 찾지 못함.
- KRX / Naver / Yahoo / Stooq 원시 OHLC 직접 확보 실패.

smart_farm_adoption_barriers:
farmer age
education
land size
government support
technical hurdles
financial constraints

UAV_greenhouse_counting_accuracy:
94.4%

UAV_weight_estimation_accuracy:
87.5%

flight_distance:
13.2m

flight_time:
10.5 seconds

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = unknown_insufficient_evidence
rerating_result = smart_farm_policy_tech_watch
stage_failure_type = stage1_attention_only
```

### 교정

스마트팜은 R12에서 장기 테마지만 Stage 3는 늦게 줘야 한다.

```text
Stage 1:
정책 / 기술 / 논문 / AI농업 narrative

Stage 2:
상업 설치
수주
농가 adoption
유지보수 계약

Stage 3:
반복서비스
unit economics
FCF
보조금 의존도 낮음
```

---

## Case H — KT&G `success_candidate / regulated consumer cashflow watch`

```text
symbol = 033780
case_type = success_candidate / regulatory_watch
archetype = CONSUMER_REGULATED_PRODUCT
```

### evidence

KT&G는 한국의 대표 담배·인삼 기업이고, 공개 기업정보 기준 국내 tobacco leader이며 Korea Ginseng Corporation 등 자회사를 보유한다. 2024년 매출은 약 5.9조 원으로 정리되어 있고, 담배·인삼·해외 확장·주주환원이 결합된 규제소비재 cashflow 후보로 볼 수 있다. 다만 이번 pass에서는 최신 주주환원 원문·자사주 소각·수정주가 OHLC를 안정적으로 확보하지 못했기 때문에 Stage 3는 보류한다. ([위키백과][8])

### stage date

```text
Stage 1:
2024~2025
- regulated consumer cashflow
- tobacco / HNB / ginseng
- shareholder return expectation

Stage 2:
보류
- latest buyback cancellation, dividend policy, HNB growth, global sales 확인 필요

Stage 3:
없음 또는 조건부 후보
- cashflow 안정성만으로 Green 금지
- volume decline, regulation, HNB competition 확인 필요

Stage 4B:
방어주·고배당·주주환원 기대만으로 valuation이 확장되면 후보

Stage 4C:
담배세/규제 강화, volume decline, HNB 경쟁 심화, 해외시장 부진 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Public company profile evidence only

stage3_price:
price_data_unavailable_after_deep_search

reason:
- Reuters / WSJ / MarketWatch / FT에서 KT&G 최신 주가 reaction anchor를 찾지 못함.
- KRX / Naver / Yahoo / Stooq 원시 OHLC 직접 확보 실패.
- 최신 shareholder return 원문 숫자 직접 확보 실패.

2024_revenue_anchor:
about 5.9T won, lower-confidence source

business_anchor:
tobacco + ginseng + regulated consumer cashflow

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = regulated_cashflow_watch
stage_failure_type = stage2_watch_success 후보
source_confidence = medium_low
```

### 교정

KT&G는 R12에서 `regulated_cashflow`, `pricing_power`, `shareholder_return` 후보지만, Stage 3는 최신 배당·소각·HNB 성장·volume decline·규제 리스크를 확인한 뒤다.

---

# 5. 이번 R12 case별 요약표

| case                         | 분류                               |                                             실제 가격검증 | alignment                    |
| ---------------------------- | -------------------------------- | --------------------------------------------------: | ---------------------------- |
| 코웨이                          | structural_success 후보            |                       반복 렌탈 구조 확인, OHLC unavailable | success_candidate            |
| 대동/TYM                       | success_candidate / insufficient |                    농기계·해외채널 구조 확인, OHLC unavailable | insufficient_evidence        |
| 메가스터디교육                      | event/policy watch               |             의대정원 3,058→3,548→3,871, +16.0% / +26.6% | event_premium                |
| 교육/에듀테크 basket               | 4C-watch                         |      2026-03 classroom phone ban, 학생 37%/22% survey | policy_watch                 |
| poultry basket               | event premium                    |       Brazil import restriction → easing in 35 days | one_off_disease_event        |
| Kyochon/chicken-event basket | overheat                         |         fried-chicken basket +20~30%, midpoint +25% | price_moved_without_evidence |
| 스마트팜 basket                  | insufficient                     |       adoption barriers, UAV accuracy 94.4% / 87.5% | stage1_attention_only        |
| KT&G                         | success_candidate                | regulated cashflow profile, latest OHLC unavailable | success_candidate            |

---

# 6. score-price alignment 판정

```text
success_candidate:
- 코웨이
- KT&G

unknown_insufficient_evidence:
- 대동/TYM
- 스마트팜 basket

event_premium:
- 메가스터디교육 / 의대정원 policy
- poultry basket / Brazil bird flu
- Kyochon/chicken-event basket

price_moved_without_evidence:
- Kyochon F&B / fried-chicken celebrity event
- poultry disease basket if stock rally occurred without margin evidence

policy_watch:
- 교육/에듀테크 phone-ban basket

4B-watch:
- fried-chicken basket +20~30%
- 의대정원/교육정책 뉴스로 교육주 급등 구간
- bird-flu import ban basket
- smart-farm 정책/AI농업 theme rally

4C-watch:
- poultry import restriction easing
- edtech classroom device friction
- smart-farm subsidy cut / unit economics failure
- KT&G regulation / volume decline
```

---

# 7. 점수비중 교정

## 올릴 축

```text
recurring_revenue +5
churn_stability +5
ARPU_or_repeat_course +4
cash_conversion +5
unit_economics +5
commercial_installation +4
service_contract_visibility +4
dealer_sell_through +4
inventory_quality +4
regulatory_pass +4
pricing_power_after_input_cost +4
```

### 이유

코웨이 같은 렌탈 기반 반복서비스는 R12에서 가장 Stage 3에 가까운 구조다. 하지만 이번 pass에서 가격경로와 최신 계정·churn·FCF를 확인하지 못했으므로 Stage 3 확정은 보류한다. 반대로 교육정책, 질병, 스마트팜, celebrity food event는 대부분 반복매출 증거가 없어 Stage 1~2 또는 event premium으로만 둔다. ([위키백과][1])

## 내릴 축

```text
defensive_theme_only -5
education_policy_only -5
agri_cycle_only -4
smart_farm_policy_only -5
disease_event_only -5
celebrity_food_event_only -5
import_ban_event_only -4
unconfirmed_export_theme -3
dealer_inventory_unknown -4
subsidy_dependent_unit_economics -4
regulated_product_without_growth -3
```

### 이유

의대정원 정책은 2025년 동결 가능성에서 2026년 단계적 확대안으로 바뀌었고, poultry event는 35일 만에 수입제한 완화 trigger가 나왔으며, Jensen Huang chicken event는 실제 매출 evidence 없이 basket이 20~30% 움직였다. 이런 이벤트는 R12에서 Green이 아니라 4B/event premium이다. ([Reuters][3])

## Green gate 강화 조건

```text
R12 Stage 3-Green 필수:
1. 반복매출 또는 반복구매 확인
2. churn / retention 안정
3. ARPU 또는 가격전가 확인
4. unit economics 확인
5. cash conversion 확인
6. 재고·매출채권 안정
7. 규제 리스크 통과
8. 보조금 의존도 낮음
9. 가격경로가 증거 이후 따라옴

금지:
정책 뉴스만 있음
질병 이벤트만 있음
수입금지 뉴스만 있음
스마트팜 테마만 있음
농기계 수출 테마만 있음
교육정책 기대만 있음
celebrity food event만 있음
방어주라서 좋다는 논리만 있음
```

## 4B 조기감지 조건

```text
4B-watch:
정책 뉴스로 교육/스마트팜/농기계주 급등
질병 이벤트로 poultry basket 급등
celebrity/viral food event로 food-service basket 급등
방어주·고배당 프레임만으로 valuation 확장
렌탈/규제소비재가 성장률보다 multiple이 먼저 오름
의대정원/사교육 정책 기대가 수강생 증가보다 먼저 가격에 반영

4B-elevated:
churn 상승
dealer inventory 증가
수입제한 완화
정책 후퇴
규제 강화
보조금 축소
성장률 둔화에도 valuation 유지
```

## 4C hard gate 조건

```text
recall / product safety issue
churn spike
ARPU 하락
dealer inventory build
farmer financing stress
education policy reversal
private education regulation
birth-rate demand collapse
import ban reversal
disease event cleared
celebrity event fade
regulatory ban / youth-safety restriction
subsidy withdrawal
unit economics failure
cash conversion deterioration
```

---

# 8. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
```

이번 세션에서 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉을 안정적으로 직접 확보하지 못했다. 대신 Reuters / AP / Tom’s Hardware / arXiv / 공개 기업정보의 이벤트 수익률, 정책·기술·사업 지표를 사용해 계산 가능한 부분은 직접 계산했다.

---

# 9. patch-ready 출력

## docs/round/round_144.md 요약

```md
# R12 Loop 8. Agriculture / Life Service / Misc Price Validation

이번 라운드는 R12 price-validation 라운드다.

핵심 결론:
- 코웨이는 R12에서 가장 구조적인 recurring-service 후보지만, 최신 rental account, churn, ARPU, FCF, OHLC 확인 전 Stage 3 확정은 보류한다.
- 대동/TYM은 농기계 export / KIOTI / North America channel story가 있지만, dealer sell-through, inventory, farmer financing, OPM 전 Green 금지다.
- 메가스터디교육과 교육주는 의대정원 정책에 민감하지만, 2025년 동결 가능성에서 2026년 단계적 확대안까지 정책이 흔들렸다. 실제 수강생·ARPU·OPM 전 Stage 3가 아니다.
- 교육/에듀테크 basket은 2026년 3월 classroom phone ban으로 policy friction이 생겼다. 회사별 매출 경로 확인 전 Green 금지다.
- poultry basket은 Brazil bird flu import restriction이 있었지만 한국이 35일 후 제한을 완화했다. one-off disease event로 분류한다.
- Kyochon/chicken-event basket은 Jensen Huang chicken dinner viral event로 +20~30% 급등했다. 이는 price_moved_without_evidence / event premium이다.
- 스마트팜 basket은 adoption barrier와 unit economics가 핵심이다. 기술 논문이나 정책 테마만으로 Green 금지다.
- KT&G는 regulated cashflow 후보지만, 최신 주주환원·HNB 성장·규제 리스크·OHLC 확인 전 Stage 3 보류다.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 144 R12 Loop 8 Agri Life Service Misc Price Validation

## 반영 내용
- R12 Loop 8 price-validation 라운드를 추가했다.
- Recurring rental service, agri machinery export, medical-school quota policy, classroom phone ban, bird flu import restriction, celebrity chicken event, smart-farm technology, regulated consumer cashflow를 비교했다.
- Reuters/AP/Tom’s Hardware/arXiv/public company profiles reported anchors로 가능한 MFE/MAE 및 policy/technology/business metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- recurring revenue, churn stability, ARPU, unit economics, cash conversion 가중치 강화
- education policy-only, disease event-only, celebrity food event-only, smart farm policy-only 감점 강화
- one-off event fade와 subsidy/unit economics 4C-watch 강화
```

## case row 초안

```jsonl
{"case_id":"r12_loop8_coway_recurring_rental_watch","symbol":"021240","company_name":"코웨이","case_type":"success_candidate","primary_archetype":"HOME_LIVING_APPLIANCE_RENTAL","stage2_date":null,"price_validation":{"price_data_source":"public company profile/Yahoo-reference summary","stage3_price":null,"business_anchor":"water purifier / air purifier / bidet / mattress rental recurring model","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"recurring_service_rerating_candidate","notes":"Recurring rental structure is R12 Stage 3 candidate, but rental accounts, churn, ARPU, OPM/FCF and OHLC are required."}
{"case_id":"r12_loop8_daedong_tym_agri_machinery_watch","symbol":"000490/002900","company_name":"대동/TYM","case_type":"success_candidate","primary_archetype":"AGRI_MACHINERY_DEMAND_CYCLE","stage1_date":"2024-2025","price_validation":{"price_data_source":"public company profile evidence","stage3_price":null,"business_anchor":"Daedong KIOTI / TYM tractors and agri machinery export channel","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"unknown_insufficient_evidence","rerating_result":"agri_machinery_watch","notes":"Export and autonomous tractor narratives need dealer sell-through, inventory, financing, OPM and FCF before Green."}
{"case_id":"r12_loop8_megastudy_medical_quota_policy","symbol":"215200","company_name":"메가스터디교육/교육주","case_type":"event_premium","primary_archetype":"EDUCATION_SPECIALTY_SERVICES","stage1_date":"2024-02","stage2_date":"2026-02-10","price_validation":{"price_data_source":"Reuters/AP policy evidence","stage3_price":null,"original_quota":3058,"quota_2027":3548,"quota_increase_2027":490,"quota_increase_2027_pct":16.0,"quota_2030":3871,"quota_increase_2030_vs_original":813,"quota_increase_2030_pct":26.6,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium","rerating_result":"education_policy_watch","notes":"Medical school quota policy is Stage 1/2; repeat course, ARPU, OPM and cash conversion required before Green."}
{"case_id":"r12_loop8_edtech_phone_ban_policy_watch","symbol":"education_edtech_basket","company_name":"교육/에듀테크 basket","case_type":"4c_watch","primary_archetype":"EDTECH_AI_DISRUPTION","stage1_date":"2025-08-27","stage4c_date":"2026-03","price_validation":{"price_data_source":"Reuters policy evidence","stage3_price":null,"law_effective_date":"2026-03","social_media_daily_life_impact_pct":37,"anxiety_without_social_media_pct":22,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"policy_watch","rerating_result":"education_regulation_watch","notes":"Classroom phone ban may support offline discipline but creates friction for digital learning platforms; company-level revenue impact required."}
{"case_id":"r12_loop8_poultry_bird_flu_import_event","symbol":"Harim/Maniker/Cherrybro_basket","company_name":"poultry basket","case_type":"event_premium","primary_archetype":"LIVESTOCK_DISEASE_PRICE_REGULATORY","stage1_date":"2025-05-19","stage4c_date":"2025-06-23","price_validation":{"price_data_source":"Reuters import restriction/easing evidence","stage3_price":null,"brazil_2024_poultry_exports_mn_tons":5.0,"restriction_start":"2025-05-19","restriction_easing":"2025-06-23","event_duration_days":35,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium","rerating_result":"one_off_disease_event","notes":"Import ban is Stage 1; restriction easing is event fade. Stage 3 requires domestic price pass-through, volume and OPM."}
{"case_id":"r12_loop8_kyochon_jensen_chicken_event","symbol":"Kyochon/Cherrybro/Neuromeka_basket","company_name":"fried chicken event basket","case_type":"overheat","primary_archetype":"FOOD_SERVICE_EVENT_PREMIUM","stage1_date":"2025-10-31","stage4b_date":"2025-10-31","price_validation":{"price_data_source":"Tom's Hardware/Bloomberg-reported event summary","stage3_price":null,"reported_event_mfe_range_pct":"20-30","reported_event_mfe_midpoint_pct":25,"price_validation_status":"reported_event_return_range_not_full_ohlc"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"celebrity_food_event_premium","notes":"Jensen chicken dinner viral event is not revenue evidence; same-store sales and franchise margin required before Green."}
{"case_id":"r12_loop8_smart_farm_unit_economics_watch","symbol":"GreenPlus/WoomdungiFarm_basket","company_name":"스마트팜 basket","case_type":"insufficient_evidence","primary_archetype":"SMART_FARM_AGRI_TECH","stage1_date":"2024-2025","price_validation":{"price_data_source":"arXiv adoption and greenhouse UAV evidence","stage3_price":null,"uav_counting_accuracy_pct":94.4,"uav_weight_estimation_accuracy_pct":87.5,"flight_distance_m":13.2,"flight_time_sec":10.5,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"unknown_insufficient_evidence","rerating_result":"smart_farm_policy_tech_watch","notes":"Smart farm technology is Stage 1 until commercial installations, service contracts, unit economics and FCF confirm."}
{"case_id":"r12_loop8_ktng_regulated_cashflow_watch","symbol":"033780","company_name":"KT&G","case_type":"success_candidate","primary_archetype":"CONSUMER_REGULATED_PRODUCT","stage1_date":"2024-2025","price_validation":{"price_data_source":"public company profile evidence","stage3_price":null,"revenue_2024_krw_trn":5.9,"business_anchor":"tobacco + ginseng + regulated consumer cashflow","source_confidence":"medium_low","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"regulated_cashflow_watch","notes":"Regulated cashflow candidate, but buyback/dividend/HNB growth, volume decline, regulation and OHLC required before Stage 3."}
```

## shadow weight row 초안

```csv
archetype,recurring_revenue,churn_stability,arpu_or_repeat_purchase,unit_economics,cash_conversion,inventory_quality,regulatory_pass,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
HOME_LIVING_APPLIANCE_RENTAL,+5,+5,+4,+5,+5,+4,+3,-1,+3,+4,Coway recurring rental can be Stage 3 candidate but needs accounts/churn/FCF/OHLC.
AGRI_MACHINERY_DEMAND_CYCLE,+2,+0,+1,+5,+4,+5,+2,-3,+4,+4,Daedong/TYM export story needs dealer sell-through, inventory and financing.
EDUCATION_SPECIALTY_SERVICES,+3,+2,+5,+4,+5,+1,+4,-5,+5,+4,Medical quota policy is event unless repeat course/ARPU/OPM confirm.
EDTECH_AI_DISRUPTION,+2,+2,+3,+4,+4,+1,+5,-4,+4,+4,Phone ban creates policy friction for edtech; company revenue impact required.
LIVESTOCK_DISEASE_PRICE_REGULATORY,+1,+0,+2,+3,+3,+5,+4,-5,+5,+5,Bird flu import ban is one-off; easing is event fade.
FOOD_SERVICE_EVENT_PREMIUM,+2,+0,+3,+4,+4,+3,+2,-5,+5,+3,Celebrity chicken event is price_moved_without_evidence until traffic/margin confirm.
SMART_FARM_AGRI_TECH,+2,+0,+1,+5,+5,+3,+4,-5,+5,+5,Smart farm tech needs commercial installation, service revenue and subsidy-independent unit economics.
CONSUMER_REGULATED_PRODUCT,+4,+2,+3,+4,+5,+3,+5,-2,+3,+4,KT&G regulated cashflow is candidate but growth/shareholder return/regulatory risk must be verified.
```

---

# 이번 R12 Loop 8 결론

R12는 구조 후보가 있긴 하지만, 대부분 Stage 1~2에 머문다.

```text
1. 코웨이는 R12에서 가장 구조적인 recurring-service 후보가 될 수 있다.
   하지만 rental accounts, churn, ARPU, OPM/FCF, 가격경로 확인 전 Stage 3 확정은 보류한다.

2. 대동/TYM은 농기계 export와 자율주행 농기계 narrative가 있지만,
   dealer sell-through, inventory, farmer financing, OPM 전 Green 금지다.

3. 메가스터디교육과 교육주는 의대정원 정책에 민감하지만,
   정책 방향이 계속 바뀌므로 실제 수강생·ARPU·OPM 전 Stage 3가 아니다.

4. 교실 휴대전화 금지법은 교육/에듀테크 basket에 policy friction이 될 수 있다.
   회사별 매출 경로 확인 전 Green 금지다.

5. poultry disease event는 one-off다.
   수입제한 완화가 곧 event fade trigger다.

6. Jensen Huang chicken event는 대표적인 price_moved_without_evidence다.
   +20~30% 움직였더라도 매출·마진 증거가 없으면 Stage 3가 아니다.

7. 스마트팜은 장기 테마지만, commercial installation·unit economics·반복서비스 전 Green 금지다.

8. KT&G는 regulated cashflow 후보지만,
   주주환원·HNB 성장·volume decline·규제 리스크와 가격경로 확인 전 Stage 3 보류다.
```

한 문장으로 압축하면:

> **R12에서 진짜 Stage 3는 “생활서비스·농업·교육·방어주가 좋아 보인다”가 아니라, 반복매출·unit economics·가격전가·현금전환이 실제로 확인되는 순간이다.**
> **R12는 코웨이 같은 recurring-service는 후보가 될 수 있지만, 교육정책·질병·스마트팜·celebrity food event는 기본적으로 Event Premium / Watch로 둬야 한다.**

[1]: https://en.wikipedia.org/wiki/Coway_%28company%29?utm_source=chatgpt.com "Coway (company)"
[2]: https://en.wikipedia.org/wiki/Daedong_%28company%29?utm_source=chatgpt.com "Daedong (company)"
[3]: https://www.reuters.com/world/asia-pacific/south-korea-prepared-freeze-new-medical-student-numbers-minister-says-2025-03-07/?utm_source=chatgpt.com "South Korea offers to freeze medical student numbers to resolve 13-month dispute"
[4]: https://www.reuters.com/business/media-telecom/south-korea-ban-mobile-phones-school-classrooms-2025-08-27/?utm_source=chatgpt.com "South Korea to ban mobile phones in school classrooms"
[5]: https://www.reuters.com/business/healthcare-pharmaceuticals/brazil-can-no-longer-export-poultry-meat-eu-due-bird-flu-2025-05-19/?utm_source=chatgpt.com "Brazil can no longer export poultry and meat to EU due to bird flu"
[6]: https://www.tomshardware.com/tech-industry/korean-fried-chicken-stocks-surge-30-percent-as-nvidia-ceo-jensen-huang-dines-out-on-local-delicacy-entire-industry-buoyed-by-secret-ingredient-jensanity?utm_source=chatgpt.com "Korean fried chicken stocks surge 30% as Nvidia CEO Jensen Huang dines out on local delicacy - entire industry buoyed by secret ingredient, Jensanity"
[7]: https://arxiv.org/abs/2504.01795?utm_source=chatgpt.com "Factors Influencing Farmers' Motivation to Adopt Smart Farm Technology in South Korea"
[8]: https://en.wikipedia.org/wiki/Korea_Tobacco_%26_Ginseng_Corporation?utm_source=chatgpt.com "Korea Tobacco & Ginseng Corporation"

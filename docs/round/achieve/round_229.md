순서상 이번은 **R12 Loop 9 — 농업·생활서비스·기타 가격경로 검증 라운드**다.

이번 R12는 “방어주·생활서비스·교육·농업·질병 이벤트·스마트팜”을 한 바구니로 보되, **진짜 반복매출 후보**와 **정책/바이럴/event premium**을 강하게 분리한다.

```text
round = R12 Loop 9
round_id = round_157
large_sector = AGRI_LIFE_SERVICE_MISC
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
r12_default_stage3_bias = conservative_except_recurring_service
```

이번 환경에서는 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉 OHLC를 안정적으로 직접 확보하지 못했다. 따라서 Reuters / AP / MarketWatch / Tom’s Hardware / arXiv / 공개 기업정보에 남은 **이벤트 수익률, 정책 수치, 사업지표, 기술지표**로 계산 가능한 값만 계산했다. 숫자는 만들지 않았다.

---

# 1. 이번 라운드 대섹터

```text
R12 = 농업·생활서비스·기타
```

R12의 핵심은 “방어적이다”, “정책 수혜다”, “질병 이벤트다”, “스마트팜이다”가 아니라, **반복매출·unit economics·가격전가·현금전환·재고 안정·규제 통과가 확인되는가**다.

---

# 2. 대상 canonical archetype

```text
HOME_LIVING_APPLIANCE_RENTAL
CONSUMER_REGULATED_CASHFLOW
AGRI_MACHINERY_EXPORT_CYCLE
AGRI_MACHINERY_SOFTWARE_LOCKIN
EDUCATION_POLICY_EVENT
HOME_CHILD_EDUCATION
EDTECH_AI_DISRUPTION
CLASSROOM_DEVICE_REGULATION
LIVESTOCK_DISEASE_PRICE_REGULATORY
FOOD_SERVICE_EVENT_PREMIUM
SMART_FARM_AGRI_TECH
VERTICAL_FARMING_UNIT_ECONOMICS
PRICE_ONLY_RALLY
EVENT_PREMIUM
```

---

# 3. deep sub-archetype

```text
생활 렌탈:
- Coway
- water purifier / air purifier / bidet / mattress rental
- Malaysia / overseas account growth
- recurring account base
- churn / ARPU / service network
- product safety / recall risk

규제소비재:
- KT&G
- tobacco / HNB / ginseng
- regulated cashflow
- dividend / buyback / shareholder return
- volume decline / tax-regulation risk

농기계:
- Daedong / KIOTI
- TYM
- North America tractor channel
- dealer sell-through
- farmer financing
- inventory / OPM / FCF
- autonomous tractor / precision agriculture

교육:
- MegaStudy Education
- medical school quota policy
- repeat course / ARPU / OPM
- phone ban / edtech friction
- AI education disruption
- birth-rate structural demand risk

축산·질병:
- Harim / Maniker / poultry basket
- Brazil bird flu
- import restriction / easing
- one-off disease demand
- feed cost / price pass-through

생활서비스·외식:
- Kyochon F&B
- Cherrybro / Neuromeka
- Jensen Huang chicken event
- celebrity / viral food event
- traffic / same-store sales / franchise margin

스마트팜:
- Green Plus / Woomdungi Farm류
- greenhouse automation
- UAV yield estimation
- government subsidy
- adoption barrier
- unit economics / maintenance revenue
```

---

# 4. 국장 신규 후보 case

## Case A — 코웨이 `structural_success_candidate / recurring rental service`

```text
symbol = 021240
case_type = structural_success_candidate
archetype = HOME_LIVING_APPLIANCE_RENTAL
```

### stage date

```text
Stage 1:
2022~2025
- 정수기 / 공기청정기 / 비데 / 매트리스 렌탈 계정 기반 반복매출
- 말레이시아·미국·태국·인도네시아·베트남 등 해외 법인 기반 확장

Stage 2:
보류
- 최신 rental account growth
- ARPU
- churn
- Malaysia account growth
- OPM / FCF 확인 필요

Stage 3:
조건부 후보
- recurring revenue + churn stability + ARPU + overseas growth + FCF conversion 확인 시 가능

Stage 4B:
렌탈 안정성만으로 valuation이 성장률보다 먼저 확장되면 후보

Stage 4C:
제품 안전 리콜, churn 상승, 해외 성장 둔화, ARPU 하락, Netmarble 지배구조/자본배분 훼손 시 후보
```

코웨이는 정수기·공기청정기·비데·매트리스 등 생활가전 렌탈 기반의 반복서비스 기업이고, 국내 최대 정수기 기업으로 정리된다. 말레이시아·미국·태국·인도네시아·베트남·유럽·일본·중국 등 해외 법인을 보유한다. 다만 이번 pass에서는 최신 rental account, churn, ARPU, FCF, 수정주가 OHLC를 안정적으로 직접 확인하지 못했으므로 Stage 3는 확정하지 않는다. ([위키백과][1])

### 실제 가격경로 검증

```text
price_data_source:
public company profile only

stage3_price:
price_data_unavailable_after_deep_search

reason:
- Reuters / WSJ / MarketWatch / FT에서 코웨이 최신 event-day 주가 anchor를 찾지 못함.
- KRX / Naver / Yahoo / Stooq 원시 수정주가 일봉 OHLC 직접 확보 실패.
- 최신 rental accounts / churn / ARPU / FCF 원문 숫자 직접 확보 실패.

known_business_anchor:
domestic largest water purifier company
water purifier / air purifier / bidet / mattress rental model
overseas subsidiaries present

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
stage_failure_type = stage2_watch_success_candidate
```

---

## Case B — KT&G `success_candidate / regulated consumer cashflow watch`

```text
symbol = 033780
case_type = success_candidate / regulatory_watch
archetype = CONSUMER_REGULATED_CASHFLOW
```

### stage date

```text
Stage 1:
2024~2025
- tobacco / HNB / ginseng cashflow
- 고배당·방어주·주주환원 기대
- regulated consumer cashflow candidate

Stage 2:
보류
- buyback cancellation
- dividend policy
- HNB growth
- overseas tobacco growth
- domestic volume decline / regulation 확인 필요

Stage 3:
없음 또는 조건부 후보
- cashflow 안정성만으로 Green 금지
- 주주환원 반복, HNB 성장, volume decline 방어, FCF 확인 필요

Stage 4B:
방어주·고배당·주주환원 기대만으로 valuation이 먼저 확장되면 후보

Stage 4C:
담배세/규제 강화, volume decline, HNB 경쟁 심화, 해외시장 부진, 인삼 소비 둔화 시 후보
```

KT&G는 한국의 대표 담배·인삼 기업이고, 국내 tobacco leader로 정리된다. 공개 기업정보 기준 2024년 매출은 약 5.9조 원으로 제시되어 있으며, R12에서는 regulated cashflow 후보로 볼 수 있다. 그러나 최신 자사주 소각·배당정책·HNB 성장·volume decline·수정주가 OHLC를 이번 pass에서 직접 검증하지 못했으므로 Stage 3는 보류한다. ([위키백과][2])

### 실제 가격경로 검증

```text
price_data_source:
public company profile evidence only

stage3_price:
price_data_unavailable_after_deep_search

reason:
- Reuters / WSJ / MarketWatch / FT에서 KT&G 최신 event-day 주가 anchor를 찾지 못함.
- KRX / Naver / Yahoo / Stooq 원시 수정주가 일봉 OHLC 직접 확보 실패.
- 최신 shareholder return / buyback cancellation / HNB growth 원문 숫자 직접 확보 실패.

2024_revenue_anchor:
about 5.9T won, source_confidence = medium_low

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
stage_failure_type = stage2_watch_success_candidate
source_confidence = medium_low
```

---

## Case C — 대동 / TYM `success_candidate / agri machinery export watch`

```text
symbols = 000490 / 002900
case_type = success_candidate / insufficient_evidence
archetype = AGRI_MACHINERY_EXPORT_CYCLE / AGRI_MACHINERY_SOFTWARE_LOCKIN
```

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
- dealer inventory
- farmer financing
- OPM / FCF 확인 필요

Stage 3:
없음
- 농기계 export theme만으로 Green 금지

Stage 4B:
농기계 수요 회복 / 자율주행 농기계 테마로 주가가 먼저 급등하면 후보

Stage 4C:
미국 농가 수요 둔화, 딜러 재고 증가, 금융조건 악화, 농산물 가격 하락, 재고평가손실 시 후보
```

대동은 KIOTI 브랜드로 북미에서 알려진 한국 농기계 기업이고, 트랙터·콤바인·UTV·엔진 등을 생산한다. 이 구조는 R12에서 장기 후보지만, 농기계는 단순 export story가 아니라 dealer sell-through, 재고, 농가 financing, OPM, FCF가 핵심이다. 이번 pass에서는 회사별 가격경로 anchor와 최신 딜러 재고·북미 판매 데이터를 충분히 확보하지 못했다. ([위키백과][3])

### 실제 가격경로 검증

```text
price_data_source:
public company profile evidence only

stage3_price:
N/A

stage1_price:
price_data_unavailable_after_deep_search

reason:
- Reuters / WSJ / MarketWatch / FT에서 대동·TYM 관련 event-day 주가 anchor를 찾지 못함.
- KRX / Naver / Yahoo / Stooq 원시 수정주가 일봉 OHLC 직접 확보 실패.
- dealer sell-through / inventory / farmer financing 원문 데이터 확보 실패.

business_anchor:
Daedong = KIOTI brand / tractors / combines / UTV / engines
TYM = tractors / combines / cultivators / rice transplanters / diesel engines

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

---

## Case D — 메가스터디교육 / 의대정원 정책 `event_premium / education policy watch`

```text
symbol = 215200
case_type = event_premium / policy_watch
archetype = EDUCATION_POLICY_EVENT / HOME_CHILD_EDUCATION
```

### stage date

```text
Stage 1:
2024-02 이후
- 의대정원 확대 정책
- 의대 입시 사교육 수요 기대

Stage 2:
2026-02
- 정부가 의대정원을 2027년 3,548명으로 확대
- 2031년 3,871명까지 단계적 확대 계획
- 2024년 공격적 증원안보다 완화된 정책

Stage 3:
없음
- 정책 이벤트만으로 Green 금지
- 실제 수강생 증가, repeat course, ARPU, OPM, cash conversion 확인 필요

Stage 4B:
의대정원 뉴스로 교육주가 수강생 증가보다 먼저 급등하면 후보

Stage 4C:
정책 후퇴, 사교육 규제, 학령인구 감소, AI 교육 disruption, 의사단체 반발에 따른 정책 불확실성 시 후보
```

AP는 한국 정부가 의대정원을 2027년 3,548명으로 늘리고, 2031년 3,871명까지 단계적으로 확대할 계획이라고 보도했다. 현재 정원은 3,058명이며, 이는 2024년에 제시됐던 연 2,000명 증원안보다 완화된 방식이다. 교육주는 이런 정책 이벤트에 민감하지만, Stage 3는 정책이 아니라 실제 수강생·ARPU·OPM으로 확인해야 한다. ([AP News][4])

### 실제 가격경로 검증

```text
price_data_source:
AP policy evidence

stage3_price:
N/A

stage1_price:
price_data_unavailable_after_deep_search

reason:
- AP / Reuters는 메가스터디교육 event-day 주가 reaction anchor를 제공하지 않음.
- KRX / Naver / Yahoo / Stooq 원시 수정주가 일봉 OHLC 직접 확보 실패.

original_quota:
3,058

2027_quota:
3,548

quota_increase_2027:
3,548 - 3,058 = 490

quota_increase_2027_pct:
490 / 3,058
= +16.0%

2031_quota:
3,871

quota_increase_2031_vs_original:
3,871 - 3,058 = 813

quota_increase_2031_pct:
813 / 3,058
= +26.6%

MFE_5D / 20D / 60D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium / unknown_insufficient_evidence
rerating_result = education_policy_watch
stage_failure_type = stage1_or_stage2_attention_only
```

---

## Case E — 교육·에듀테크 basket `4C-watch / classroom device regulation`

```text
symbols = NE능률 / YBM넷 / 웅진씽크빅 등 교육·에듀테크 basket
case_type = 4C-watch / policy_watch
archetype = EDTECH_AI_DISRUPTION / CLASSROOM_DEVICE_REGULATION
```

### stage date

```text
Stage 1:
2025-08-27
- 교실 내 휴대전화·디지털기기 금지 법안 통과
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

한국은 2026년 3월부터 학교 교실 내 휴대전화와 디지털기기 사용을 전국적으로 금지하는 법안을 통과시켰다. Reuters는 중고생 37%가 소셜미디어가 일상생활에 영향을 준다고 답했고, 22%는 소셜미디어 접속이 안 되면 불안을 느낀다는 교육부 조사도 전했다. 이 정책은 오프라인 학습 discipline에는 우호적일 수 있지만, 교실 내 디지털 학습 플랫폼에는 friction이 될 수 있다. 회사별 매출 경로가 확인되기 전까지는 Green 금지다. ([Reuters][5])

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
- KRX / Naver / Yahoo / Stooq 원시 수정주가 일봉 OHLC 직접 확보 실패.

law_effective_date:
2026-03

middle_high_students_social_media_daily_life_impact:
37%

students_anxious_without_social_media:
22%

digital_device_exception:
students with disabilities / educational purposes

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = policy_watch
rerating_result = education_regulation_watch
stage_failure_type = stage1_attention_only
```

---

## Case F — poultry basket `event_premium / one-off disease demand`

```text
symbols = Harim / Maniker / Cherrybro 등 poultry basket
case_type = event_premium / one_off_disease_event
archetype = LIVESTOCK_DISEASE_PRICE_REGULATORY
```

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
2025-06-23 이후
- Brazil bird flu-free recognition / import restriction easing
- one-off event fade
```

브라질 상업농장에서 고병원성 조류독감이 확인되자 중국·EU·한국 등 주요 수입국이 브라질산 닭고기 수입제한을 걸었다. Brazil은 세계 최대 poultry exporter이고 2024년 poultry meat 수출이 500만 톤을 넘었다. 그러나 이후 EU가 Brazil을 bird-flu-free로 인정하며 수출 제한 완화가 진행됐고, 이런 이벤트는 국내 poultry basket에 단기 MFE를 줄 수는 있어도 구조적 Stage 3가 아니다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters import restriction / bird-flu-free evidence

stage3_price:
N/A

stage1_price:
price_data_unavailable_after_deep_search

reason:
- Reuters는 Harim / Maniker / Cherrybro 등 한국 poultry stock reaction anchor를 제공하지 않음.
- KRX / Naver / Yahoo / Stooq 원시 수정주가 일봉 OHLC 직접 확보 실패.

Brazil_2024_poultry_exports:
>5M tons

EU_share_of_Brazil_exports:
4.4%

Brazil_outbreak:
2025-05 commercial farm HPAI

restriction_status:
temporary import bans / later easing or recognition of bird-flu-free status

MFE_5D / 20D / 60D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4C 큰 하락 이전 포착 여부:
conceptual_success
- 수입제한 완화 / bird-flu-free recognition이 event fade trigger.
```

### alignment

```text
score_price_alignment = event_premium
rerating_result = one_off_disease_event
stage_failure_type = should_have_been_stage1_or_4B_watch
```

---

## Case G — Kyochon F&B / Cherrybro / Neuromeka `overheat / celebrity food event`

```text
symbols = Kyochon F&B / Cherrybro / Neuromeka
case_type = overheat / price_moved_without_evidence
archetype = FOOD_SERVICE_EVENT_PREMIUM
```

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
- Kyochon F&B / Cherrybro / Neuromeka 등 fried chicken 관련주 급등
- Kyochon F&B 등 일부 장중 +20~30%
- price moved before evidence

Stage 4C:
viral fade, 실제 매출 미반영, franchise margin 부진, 원가 상승, chicken traffic 정상화 시 후보
```

Nvidia CEO Jensen Huang이 삼성·현대 경영진과 Kkanbu Chicken에서 치킨과 맥주를 먹은 장면이 viral해지면서, 한국 fried-chicken 관련주가 급등했다. MarketWatch는 Kyochon F&B, Cherrybro, Neuromeka 등이 Huang의 방문 효과를 받았다고 보도했고, Tom’s Hardware는 Kyochon F&B 같은 fried-chicken 관련주가 장중 20~30%까지 올랐다고 정리했다. 이건 매출·마진 evidence가 아니라 **celebrity/viral event premium**이다. ([마켓워치][7])

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch / Tom’s Hardware event-return summary

stage3_price:
N/A

reported_event_MFE_1D_range:
+20% to +30%

reported_event_MFE_midpoint:
+25%

related_names:
Kyochon F&B
Cherrybro
Neuromeka

fundamental_revenue_evidence:
not confirmed

MFE_30D / 90D:
price_data_unavailable_after_deep_search

reason:
- MarketWatch / Tom’s Hardware는 event-day 수익률 범위와 관련주를 제공하지만, 종가 OHLC와 30D/90D path는 제공하지 않음.
- KRX / Naver / Yahoo / Stooq 원시 수정주가 일봉 OHLC 직접 확보 실패.

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

---

## Case H — 스마트팜 basket `insufficient_evidence / unit economics watch`

```text
symbols = Green Plus / Woomdungi Farm류 smart-farm basket
case_type = insufficient_evidence
archetype = SMART_FARM_AGRI_TECH / VERTICAL_FARMING_UNIT_ECONOMICS
```

### stage date

```text
Stage 1:
2024~2025
- smart farm / AI agriculture / labor shortage / climate adaptation narrative

Stage 2:
보류
- 회사별 commercial installation
- order backlog
- maintenance revenue
- subsidy dependency 확인 필요

Stage 3:
없음
- 정책·기술 논문만으로 Green 금지

Stage 4B:
스마트팜 테마주가 정책/AI농업 뉴스로 먼저 급등하면 후보

Stage 4C:
설치 지연, unit economics 실패, 정부보조 축소, 농가 adoption 부진, maintenance revenue 부재 시 후보
```

스마트팜 adoption 연구는 농가 연령, 교육 수준, 토지 규모, 정부 지원, 기술 장벽, 금융 제약이 adoption을 좌우한다고 분석했다. 또 greenhouse UAV yield-estimation 연구는 cherry tomato greenhouse에서 94.4% counting accuracy와 87.5% weight-estimation accuracy를 보였지만, 이는 기술 가능성이지 상장사 단위 매출·마진·FCF evidence가 아니다. ([arXiv][8])

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
- KRX / Naver / Yahoo / Stooq 원시 수정주가 일봉 OHLC 직접 확보 실패.

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

---

# 5. 이번 R12 case별 요약표

| case                         | 분류                               |                                                                   실제 가격검증 | alignment                    |
| ---------------------------- | -------------------------------- | ------------------------------------------------------------------------: | ---------------------------- |
| 코웨이                          | structural_success 후보            |                                             반복 렌탈 구조 확인, OHLC unavailable | success_candidate            |
| KT&G                         | success_candidate                |         regulated cashflow profile, 2024 revenue 약 5.9T, OHLC unavailable | success_candidate            |
| 대동/TYM                       | success_candidate / insufficient |                                  KIOTI·농기계 export 구조 확인, OHLC unavailable | insufficient_evidence        |
| 메가스터디교육                      | event/policy watch               |                                   의대정원 3,058→3,548→3,871, +16.0% / +26.6% | event_premium                |
| 교육/에듀테크 basket               | 4C-watch                         |                            classroom phone ban 2026-03, 학생 37%/22% survey | policy_watch                 |
| poultry basket               | event premium                    | Brazil bird flu import restriction → later easing/free-status recognition | one_off_disease_event        |
| Kyochon/chicken-event basket | overheat                         |                               fried-chicken basket +20~30%, midpoint +25% | price_moved_without_evidence |
| 스마트팜 basket                  | insufficient                     |                             adoption barriers, UAV accuracy 94.4% / 87.5% | stage1_attention_only        |

---

# 6. score-price alignment 판정

```text
success_candidate:
- 코웨이
- KT&G

unknown_insufficient_evidence:
- 대동 / TYM
- 스마트팜 basket

event_premium:
- 메가스터디교육 / 의대정원 policy
- poultry basket / Brazil bird flu
- Kyochon / chicken-event basket

price_moved_without_evidence:
- Kyochon F&B / fried-chicken celebrity event
- poultry disease basket if stock rally occurred without margin evidence
- smart-farm policy/AI농업 theme rally without commercial installation

policy_watch:
- 교육/에듀테크 phone-ban basket

4B-watch:
- fried-chicken basket +20~30%
- 의대정원/교육정책 뉴스로 교육주 급등 구간
- bird-flu import-ban basket
- smart-farm 정책/AI농업 theme rally
- 방어주/고배당 frame으로 KT&G valuation만 선반영되는 구간

4C-watch:
- poultry import restriction easing / bird-flu-free recognition
- edtech classroom device friction
- smart-farm subsidy cut / unit economics failure
- KT&G regulation / volume decline
- 코웨이 churn spike / product recall
```

---

# 7. 점수비중 교정

## 올릴 축

```text
recurring_revenue +5
churn_stability +5
ARPU_or_repeat_purchase +4
cash_conversion +5
unit_economics +5
commercial_installation +4
service_contract_visibility +4
dealer_sell_through +4
inventory_quality +4
regulatory_pass +4
pricing_power_after_input_cost +4
```

### 왜 올리나

코웨이 같은 렌탈 기반 반복서비스는 R12에서 가장 Stage 3에 가까운 구조다. KT&G도 regulated cashflow 후보가 될 수 있다. 하지만 둘 다 Green은 “안정적이어 보인다”가 아니라 **반복매출·churn·ARPU·FCF·주주환원·규제통과**로 확인되어야 한다.

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

### 왜 내리나

의대정원 정책은 교육주 routing signal일 뿐이고, Brazil bird flu는 수입제한 완화가 나오면 event fade가 된다. Jensen Huang chicken event는 매출 evidence 없이 20~30% 움직인 대표적인 price_moved_without_evidence다. 스마트팜도 기술지표가 좋아도 상업 설치와 unit economics 전에는 Green이 아니다.

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

이번 R12 Loop 9에서는 hard 4C를 억지로 확정하지 않는다. `Kyochon/Jensen event`, `poultry disease`, `education policy`, `smart farm technology`는 기본적으로 Stage 1~2 또는 event premium이다. `Coway`와 `KT&G`만 구조 후보로 남기되, 가격경로와 현금흐름 검증 전 Stage 3 확정은 보류한다.

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

## docs/round/round_157.md 요약

```md
# R12 Loop 9. Agriculture / Life Service / Misc Price Validation

이번 라운드는 R12 Loop 9 price-validation 라운드다.

핵심 결론:
- Coway는 R12에서 가장 구조적인 recurring-service 후보지만, 최신 rental account, churn, ARPU, FCF, OHLC 확인 전 Stage 3 확정은 보류한다.
- KT&G는 regulated cashflow 후보지만, 최신 shareholder return, buyback cancellation, HNB growth, volume decline, regulation and OHLC 확인 전 Green 금지다.
- Daedong/TYM은 agri machinery export / KIOTI / North America channel story가 있지만, dealer sell-through, inventory, farmer financing, OPM 전 Green 금지다.
- MegaStudy/Education stocks are policy-sensitive. Medical-school quota rises from 3,058 to 3,548 in 2027 and 3,871 by 2031, but actual students, ARPU and OPM are required before Green.
- Edtech basket has policy friction from Korea’s nationwide classroom phone/device ban effective March 2026. Company-level revenue impact must be confirmed.
- Poultry basket is one-off disease event. Brazil bird flu import restrictions can fade once restrictions ease or bird-flu-free recognition appears.
- Kyochon/Cherrybro/Neuromeka chicken-event basket is price_moved_without_evidence. Jensen Huang viral dinner drove 20~30% event rally without revenue proof.
- Smart-farm basket remains insufficient_evidence. Adoption barriers and unit economics matter more than policy/AI-agriculture theme.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 157 R12 Loop 9 Agri Life Service Misc Price Validation

## 반영 내용
- R12 Loop 9 price-validation 라운드를 추가했다.
- Recurring rental service, regulated consumer cashflow, agri machinery export, medical-school quota policy, classroom phone ban, bird-flu import restriction, celebrity chicken event, smart-farm technology를 비교했다.
- Reuters/AP/MarketWatch/Tom’s Hardware/arXiv/public company profiles reported anchors로 가능한 MFE/MAE 및 policy/technology/business metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- recurring revenue, churn stability, ARPU, unit economics, cash conversion, dealer sell-through 가중치 강화
- education policy-only, disease event-only, celebrity food event-only, smart farm policy-only, defensive-theme-only 감점 강화
- one-off event fade와 subsidy/unit economics 4C-watch 강화
```

## case row 초안

```jsonl
{"case_id":"r12_loop9_coway_recurring_rental_watch","symbol":"021240","company_name":"코웨이","case_type":"success_candidate","primary_archetype":"HOME_LIVING_APPLIANCE_RENTAL","stage2_date":null,"price_validation":{"price_data_source":"public company profile","stage3_price":null,"business_anchor":"water purifier / air purifier / bidet / mattress rental recurring model","overseas_subsidiaries":["Malaysia","United States","Thailand","Indonesia","Vietnam","Europe","Japan","China"],"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"recurring_service_rerating_candidate","notes":"Recurring rental structure is R12 Stage 3 candidate, but rental accounts, churn, ARPU, OPM/FCF and OHLC are required."}
{"case_id":"r12_loop9_ktng_regulated_cashflow_watch","symbol":"033780","company_name":"KT&G","case_type":"success_candidate","primary_archetype":"CONSUMER_REGULATED_CASHFLOW","stage1_date":"2024-2025","price_validation":{"price_data_source":"public company profile evidence","stage3_price":null,"revenue_2024_krw_trn":5.9,"business_anchor":"tobacco + ginseng + regulated consumer cashflow","source_confidence":"medium_low","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"regulated_cashflow_watch","notes":"Regulated cashflow candidate, but buyback/dividend/HNB growth, volume decline, regulation and OHLC required before Stage 3."}
{"case_id":"r12_loop9_daedong_tym_agri_machinery_watch","symbol":"000490/002900","company_name":"대동/TYM","case_type":"success_candidate","primary_archetype":"AGRI_MACHINERY_EXPORT_CYCLE","stage1_date":"2024-2025","price_validation":{"price_data_source":"public company profile evidence","stage3_price":null,"business_anchor":"Daedong KIOTI / tractors / combines / UTV / engines; TYM agri machinery export channel","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"unknown_insufficient_evidence","rerating_result":"agri_machinery_watch","notes":"Export and autonomous tractor narratives need dealer sell-through, inventory, financing, OPM and FCF before Green."}
{"case_id":"r12_loop9_megastudy_medical_quota_policy","symbol":"215200","company_name":"메가스터디교육/교육주","case_type":"event_premium","primary_archetype":"EDUCATION_POLICY_EVENT","stage1_date":"2024-02","stage2_date":"2026-02","price_validation":{"price_data_source":"AP policy evidence","stage3_price":null,"original_quota":3058,"quota_2027":3548,"quota_increase_2027":490,"quota_increase_2027_pct":16.0,"quota_2031":3871,"quota_increase_2031_vs_original":813,"quota_increase_2031_pct":26.6,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium","rerating_result":"education_policy_watch","notes":"Medical-school quota policy is Stage 1/2; repeat course, student conversion, ARPU, OPM and cash conversion required before Green."}
{"case_id":"r12_loop9_edtech_phone_ban_policy_watch","symbol":"education_edtech_basket","company_name":"교육/에듀테크 basket","case_type":"4c_watch","primary_archetype":"CLASSROOM_DEVICE_REGULATION","stage1_date":"2025-08-27","stage4c_date":"2026-03","price_validation":{"price_data_source":"Reuters policy evidence","stage3_price":null,"law_effective_date":"2026-03","social_media_daily_life_impact_pct":37,"anxiety_without_social_media_pct":22,"digital_device_exception":"disability_or_educational_purpose","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"policy_watch","rerating_result":"education_regulation_watch","notes":"Classroom phone/device ban may support offline discipline but creates friction for digital learning platforms; company-level revenue impact required."}
{"case_id":"r12_loop9_poultry_bird_flu_import_event","symbol":"Harim/Maniker/Cherrybro_basket","company_name":"poultry basket","case_type":"event_premium","primary_archetype":"LIVESTOCK_DISEASE_PRICE_REGULATORY","stage1_date":"2025-05-19","stage4c_date":"event_fade_after_restriction_easing","price_validation":{"price_data_source":"Reuters import restriction / bird-flu-free evidence","stage3_price":null,"brazil_2024_poultry_exports_mn_tons":5.0,"eu_share_of_brazil_exports_pct":4.4,"event_type":"Brazil commercial farm bird flu import restriction followed by easing/free-status recognition","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium","rerating_result":"one_off_disease_event","notes":"Import restriction is Stage 1; easing or bird-flu-free recognition is event fade. Stage 3 requires domestic price pass-through, volume and OPM."}
{"case_id":"r12_loop9_kyochon_jensen_chicken_event","symbol":"Kyochon/Cherrybro/Neuromeka_basket","company_name":"fried chicken event basket","case_type":"overheat","primary_archetype":"FOOD_SERVICE_EVENT_PREMIUM","stage1_date":"2025-10-31","stage4b_date":"2025-10-31","price_validation":{"price_data_source":"MarketWatch/Tom's Hardware event-return summary","stage3_price":null,"reported_event_mfe_range_pct":"20-30","reported_event_mfe_midpoint_pct":25,"related_names":["Kyochon F&B","Cherrybro","Neuromeka"],"fundamental_revenue_evidence_confirmed":false,"price_validation_status":"reported_event_return_range_not_full_ohlc"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"celebrity_food_event_premium","notes":"Jensen chicken dinner viral event is not revenue evidence; store traffic, same-store sales, franchise margin and repeat demand required before Green."}
{"case_id":"r12_loop9_smart_farm_unit_economics_watch","symbol":"GreenPlus/WoomdungiFarm_basket","company_name":"스마트팜 basket","case_type":"insufficient_evidence","primary_archetype":"SMART_FARM_AGRI_TECH","stage1_date":"2024-2025","price_validation":{"price_data_source":"arXiv adoption and greenhouse UAV evidence","stage3_price":null,"adoption_barriers":["farmer_age","education","land_size","government_support","technical_hurdles","financial_constraints"],"uav_counting_accuracy_pct":94.4,"uav_weight_estimation_accuracy_pct":87.5,"flight_distance_m":13.2,"flight_time_sec":10.5,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"unknown_insufficient_evidence","rerating_result":"smart_farm_policy_tech_watch","notes":"Smart farm technology is Stage 1 until commercial installations, service contracts, unit economics and FCF confirm."}
```

## shadow weight row 초안

```csv
archetype,recurring_revenue,churn_stability,arpu_or_repeat_purchase,unit_economics,cash_conversion,inventory_quality,regulatory_pass,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
HOME_LIVING_APPLIANCE_RENTAL,+5,+5,+4,+5,+5,+4,+3,-1,+3,+4,Coway recurring rental can be Stage 3 candidate but needs accounts/churn/FCF/OHLC.
CONSUMER_REGULATED_CASHFLOW,+4,+2,+3,+4,+5,+3,+5,-2,+3,+4,KT&G regulated cashflow is candidate but growth/shareholder return/regulatory risk must be verified.
AGRI_MACHINERY_EXPORT_CYCLE,+2,+0,+1,+5,+4,+5,+2,-3,+4,+4,Daedong/TYM export story needs dealer sell-through, inventory and financing.
EDUCATION_POLICY_EVENT,+3,+2,+5,+4,+5,+1,+4,-5,+5,+4,Medical quota policy is event unless repeat course/ARPU/OPM confirm.
CLASSROOM_DEVICE_REGULATION,+2,+2,+3,+4,+4,+1,+5,-4,+4,+4,Phone ban creates policy friction for edtech; company revenue impact required.
LIVESTOCK_DISEASE_PRICE_REGULATORY,+1,+0,+2,+3,+3,+5,+4,-5,+5,+5,Bird flu import restriction is one-off; easing/free-status recognition is event fade.
FOOD_SERVICE_EVENT_PREMIUM,+2,+0,+3,+4,+4,+3,+2,-5,+5,+3,Celebrity chicken event is price_moved_without_evidence until traffic/margin confirm.
SMART_FARM_AGRI_TECH,+2,+0,+1,+5,+5,+3,+4,-5,+5,+5,Smart farm tech needs commercial installation, service revenue and subsidy-independent unit economics.
```

---

# 이번 R12 Loop 9 결론

R12는 구조 후보가 있긴 하지만, 대부분은 Stage 1~2에 머문다.

```text
1. 코웨이는 R12에서 가장 구조적인 recurring-service 후보가 될 수 있다.
   하지만 rental accounts, churn, ARPU, OPM/FCF, 가격경로 확인 전 Stage 3 확정은 보류한다.

2. KT&G는 regulated cashflow 후보지만,
   주주환원·HNB 성장·volume decline·규제 리스크와 가격경로 확인 전 Stage 3 보류다.

3. 대동/TYM은 농기계 export와 자율주행 농기계 narrative가 있지만,
   dealer sell-through, inventory, farmer financing, OPM 전 Green 금지다.

4. 메가스터디교육과 교육주는 의대정원 정책에 민감하지만,
   실제 수강생·ARPU·OPM 전 Stage 3가 아니다.

5. 교실 휴대전화 금지법은 교육/에듀테크 basket에 policy friction이 될 수 있다.
   회사별 매출 경로 확인 전 Green 금지다.

6. poultry disease event는 one-off다.
   수입제한 완화나 bird-flu-free recognition이 곧 event fade trigger다.

7. Jensen Huang chicken event는 대표적인 price_moved_without_evidence다.
   +20~30% 움직였더라도 매출·마진 증거가 없으면 Stage 3가 아니다.

8. 스마트팜은 장기 테마지만,
   commercial installation·unit economics·반복서비스 전 Green 금지다.
```

한 문장으로 압축하면:

> **R12에서 진짜 Stage 3는 “생활서비스·농업·교육·방어주가 좋아 보인다”가 아니라, 반복매출·unit economics·가격전가·현금전환이 실제로 확인되는 순간이다.**
> **R12는 코웨이 같은 recurring-service는 후보가 될 수 있지만, 교육정책·질병·스마트팜·celebrity food event는 기본적으로 Event Premium / Watch로 둬야 한다.**

[1]: https://en.wikipedia.org/wiki/Coway_%28company%29?utm_source=chatgpt.com "Coway (company)"
[2]: https://de.wikipedia.org/wiki/KT%26G_Corporation?utm_source=chatgpt.com "KT&G Corporation"
[3]: https://en.wikipedia.org/wiki/Daedong_%28company%29?utm_source=chatgpt.com "Daedong (company)"
[4]: https://apnews.com/article/5ad78e1ce91ed5c3dface44438dcb814?utm_source=chatgpt.com "South Korea will boost medical school admissions to tackle physician shortage"
[5]: https://www.reuters.com/business/media-telecom/south-korea-ban-mobile-phones-school-classrooms-2025-08-27/?utm_source=chatgpt.com "South Korea to ban mobile phones in school classrooms"
[6]: https://www.reuters.com/business/healthcare-pharmaceuticals/brazil-can-no-longer-export-poultry-meat-eu-due-bird-flu-2025-05-19/?utm_source=chatgpt.com "Brazil can no longer export poultry and meat to EU due to bird flu"
[7]: https://www.marketwatch.com/story/jensen-huang-spreads-nvidia-magic-to-fried-chicken-stocks-06b49648?utm_source=chatgpt.com "Jensen Huang spreads Nvidia magic to fried-chicken stocks"
[8]: https://arxiv.org/abs/2504.01795?utm_source=chatgpt.com "Factors Influencing Farmers' Motivation to Adopt Smart Farm Technology in South Korea"

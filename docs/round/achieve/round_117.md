좋아. **R11 Loop 6까지 끝났으니, 이번은 R12 Loop 6 — 농업·생활서비스·기타**다.

R12는 양돈주, 육계주, 배합사료, 대두, 농기계, 종자·비료·농약, 스마트팜, 참치 원양어업, 교육, 취업·일자리, 키즈·유아용품, 전자담배, 주정 같은 테마를 흡수하는 대섹터다. Theme Tag Map 기준으로도 R12는 대부분 **Watch/Red** 성격이고, 실제 수주·반복계약·판가전가·규제 승인·FCF 전환 전까지 Green을 제한해야 한다.

Checkpoint 20 원칙도 그대로 적용한다. 수주금액, 정부계약, 규제 승인, recurring revenue, 해지율, CAC, 판가전가, 사료비, 질병 이벤트 같은 값은 실제 확인된 증거만 써야 한다. R12는 “생활 필수”, “AI 교육”, “질병 수혜”, “스마트팜”, “규제 완화” 같은 말이 쉽게 점수를 부풀리기 때문에, 확인되지 않은 값을 채우면 테마주 false-positive가 바로 생긴다.

서생원식으로 보면 R12의 질문도 동일하다. “필수소비라서 좋다”가 아니라 **EPS/FCF 체급 변화와 밸류에이션 프레임 변화가 실제로 같이 일어나는가**다. 생활 필수라도 가격 사이클이면 cycle이고, 교육도 AI가 핵심 서비스를 대체하면 4C이며, 스마트팜도 unit economics가 안 맞으면 Green이 아니다.

---

# R12 Loop 6. 농업·생활서비스·기타

## 1. 이번 라운드 대섹터

```text
R12 = 농업·생활서비스·기타
Loop 6 목표 =
농기계 cycle / right-to-repair 규제 /
종자·비료·농약 IP·원가·farmer margin /
축산 질병 event / animal health stockpile /
수직농장 unit economics /
AI 교육 disruption / edtech monetization trade-off /
셀프체크아웃 local regulation /
니코틴 pouch youth-safety /
cannabis partial rescheduling /
생활가전 hardware cycle을 더 정밀 분리
```

이번 회차의 핵심 질문은 이거다.

```text
이 기업은 반복계약·반복매출·판가전가·규제 승인·FCF가 있는가?
아니면 질병, 날씨, 곡물가격, 정책, 저출산, AI 대체, 규제 뉴스로만 움직이는가?
```

R12에서 가장 위험한 오판은 이거다.

```text
생활 필수 / 농업 / 교육 / 규제 완화
= Green
```

Loop 6부터는 이렇게 본다.

```text
좋은 구조 후보:
렌탈 계정 + 해지율 안정 + 관리서비스 반복매출
B2B/B2G 교육계약 + completion rate + CAC 안정 + FCF
동물백신 + 조건부 승인 + 정부 비축 + 반복 접종 가능성
종자·작물보호제 + licensing/IP + 판가전가 + 소송·규제 통과
규제형 소비재 + FDA/DEA 승인 + 허가범위 + 반복소비
스마트팜 + 실제 수주 + 가동률 + 에너지비 통제 + unit economics

위험한 후보:
수직농장 기술 narrative만 있는 기업
농기계 자율화 기술만 있고 농가 capex cycle이 꺾인 기업
조류독감·ASF·계란값 급등만 보는 축산주
AI 교육 테마지만 핵심 서비스가 AI에 대체되는 기업
온라인 교육 OPM 고부채 모델
생활가전 hardware cycle
키오스크 설치대수만 보는 무인화 테마
전자담배·니코틴 pouch·마리화나 규제 뉴스만 보는 소비재
```

---

## 2. 대상 canonical archetype

| canonical archetype                      | Loop 6 정책                                                     |
| ---------------------------------------- | ------------------------------------------------------------- |
| `SMART_FARM_AGRI_TECH`                   | Watch-to-Green. 실제 수주·운영계약·unit economics 필요                  |
| `VERTICAL_FARMING_UNIT_ECONOMICS`        | Watch/Red. 에너지비·CAPEX·프리미엄 가격 실패 리스크 큼                        |
| `AGRI_MACHINERY_PRECISION_CYCLE`         | Watch. 자율농기계 기술보다 농가소득·금리·장비 cycle 확인                         |
| `AGRI_MACHINERY_DEMAND_CYCLE`            | Watch/Red. 농가소득·작물가격·금리·재고·관세가 먼저                             |
| `AGRI_MACHINERY_SOFTWARE_LOCKIN`         | Watch. software attach는 좋지만 right-to-repair 규제 감시             |
| `RIGHT_TO_REPAIR_REGULATORY_OVERLAY`     | RedTeam gate. 수리 독점·FTC·소송·settlement                         |
| `RIGHT_TO_REPAIR_CONSTRUCTION_EXPANSION` | RedTeam overlay. 농기계 right-to-repair가 건설·임업장비로 확장             |
| `AGRI_INPUT_SEED_CROP_PROTECTION`        | Watch-to-Green. 종자·작물보호제는 licensing, 판가전가, 소송·규제 확인           |
| `FERTILIZER_INPUT_COST_CYCLE`            | Watch. potash/phosphate/nitrogen은 수요보다 원재료·지정학·농가마진을 같이 봄     |
| `FERTILIZER_STRATEGIC_PHOSPHATE_OPTION`  | Watch. phosphate 전략광물·사업재편 가능성은 있으나 volume/FCF 확인 필요          |
| `AGRI_LIVESTOCK_FOOD_COMMODITY`          | Watch/Red. 질병·사료비·곡물·가격 cycle 중심                              |
| `LIVESTOCK_DISEASE_PRICE_REGULATORY`     | RedTeam overlay. 조류독감·계란값 급등 후 가격조사·담합 리스크                    |
| `ANIMAL_HEALTH_BIOSECURITY`              | Watch-to-Green. 정부 비축·반복 접종·승인·주문 필요                          |
| `AGRI_DISEASE_AI_MONITORING`             | Watch. 질병 AI 감시는 데이터품질·privacy·농장도입·반복계약 필요                   |
| `EDUCATION_SPECIALTY_SERVICES`           | Watch-to-Green. 반복수강·B2B/B2G 계약·CAC·completion rate 필요        |
| `EDTECH_AI_MONETIZATION_TRADEOFF`        | Watch. AI 기능 확대가 유저 증가와 monetization 사이 trade-off를 만듦         |
| `EDTECH_AI_DISRUPTION`                   | RedTeam overlay. Chegg식 AI 대체 리스크                             |
| `EDTECH_AI_SEARCH_DISINTERMEDIATION`     | RedTeam overlay. Google AI Overviews·검색트래픽 감소·콘텐츠 대체          |
| `ONLINE_EDUCATION_OPM_DISTRESS`          | Watch/Red. 부채·학생 ROI·규제·파트너 집중 감시                             |
| `HOME_CHILD_EDUCATION`                   | Watch/Red. 저출산·TAM 축소 hard risk                               |
| `HOME_LIVING_APPLIANCE_RENTAL`           | Watch-to-Green. 렌탈 계정·해지율·관리서비스 매출 필요                         |
| `HOME_APPLIANCE_HARDWARE_CYCLE`          | Watch/Red. 교체수요·주택경기·배당·FCF 확인                                |
| `SERVICE_KIOSK_SELF_CHECKOUT`            | Watch/Red. hardware one-off와 유지보수·결제수수료 반복매출 분리               |
| `SELF_CHECKOUT_LOCAL_REGULATION_OVERLAY` | RedTeam overlay. item limit, 직원 배치, staffed lane 의무           |
| `CONSUMER_REGULATED_PRODUCT`             | Watch-to-Green. FDA/DEA/국가별 규제 승인·판매범위·반복소비 필요                |
| `NICOTINE_ALTERNATIVE_REGULATED`         | Watch/Red. 전자담배·니코틴 pouch는 public health gate 필수              |
| `NICOTINE_POUCH_YOUTH_SAFETY_OVERLAY`    | RedTeam gate. youth addiction·flavor·광고·니코틴 함량                |
| `CANNABIS_REGULATED_PRODUCT`             | Watch. rescheduling과 합법화·실제 매출을 분리                            |
| `CANNABIS_PARTIAL_RESCHEDULING_LIMIT`    | RedTeam overlay. Schedule III 일부 전환은 federal legalization이 아님 |
| `FOOD_INPUT_REGULATED_CYCLE`             | Watch. 주정·식품 input은 원가·판가·규제 확인                               |
| `AGRI_DISEASE_EVENT_OVERLAY`             | RedTeam gate. 조류독감·ASF·질병 one-off                             |
| `REGULATED_CONSUMER_APPROVAL_OVERLAY`    | RedTeam gate. FDA/DEA 승인·불허가·public health                    |
| `DISCLOSURE_CONFIDENCE_CAP`              | RedTeam cap. 계약·해지율·규제승인 detail 부족 시 Stage 3 제한               |

---

## 3. deep sub-archetype

```text
SMART_FARM_AGRI_TECH
- 스마트팜
- 온실 자동화
- 농업 로봇
- 정밀농업 AI
- AI rover
- 농업 데이터 플랫폼
- 질병 모니터링 AI
- 운영계약
- 유지보수·SaaS
- unit economics

VERTICAL_FARMING_UNIT_ECONOMICS
- 수직농장
- indoor farm
- hydroponics
- leafy greens
- energy cost
- premium pricing
- yield loss
- CAPEX
- debt
- shutdown / Chapter 11

AGRI_MACHINERY_PRECISION_CYCLE
- 농기계
- 자율주행 트랙터
- 정밀농업 장비
- 농업용 드론
- 장비 교체 cycle
- 농가소득
- 금리·할부금융
- tariff
- dealer inventory
- right-to-repair

AGRI_INPUT_SEED_CROP_PROTECTION
- 종자
- 비료
- 농약
- 작물보호제
- soy seed licensing
- gene editing
- hybrid seed
- crop protection patent
- Roundup litigation
- farmer ROI
- 판가전가

FERTILIZER_INPUT_COST_CYCLE
- potash
- phosphate
- nitrogen
- urea
- ammonia
- sulfuric acid
- crop price
- farmer margin
- input cost spike
- supply disruption
- Middle East risk

AGRI_LIVESTOCK_FOOD_COMMODITY
- 양돈
- 육계
- 계란
- 배합사료
- 대두
- 참치 원양어업
- 사료비
- 유가
- 환율
- 조류독감
- ASF
- 가격 정상화
- 가격담합 조사

ANIMAL_HEALTH_BIOSECURITY
- 동물백신
- 조류독감 백신
- ASF 방역
- 정부 비축
- 반복 접종
- 조건부 승인
- 바이오시큐리티 앱/서비스
- 농장 감시 AI

EDUCATION_SPECIALTY_SERVICES
- 성인교육
- 취업교육
- AI 재교육
- B2B 기업교육
- B2G apprenticeship
- 언어교육 앱
- 자격증
- bootcamp
- completion rate
- student ROI
- CAC

EDTECH_AI_DISRUPTION
- Chegg
- homework help
- AI answer engine
- AI Overviews
- traffic decline
- subscriber decline
- revenue guide miss
- layoffs
- enterprise pivot

ONLINE_EDUCATION_OPM_DISTRESS
- 2U
- edX
- OPM
- revenue-share contracts
- high leverage
- student debt / ROI
- regulatory oversight
- Chapter 11

HOME_LIVING_APPLIANCE_RENTAL
- 정수기
- 공기청정기
- 비데
- 매트리스
- 밥솥
- 렌탈 계정
- 필터·관리 서비스
- 해지율
- 해외 렌탈

SERVICE_KIOSK_SELF_CHECKOUT
- 키오스크
- 셀프체크아웃
- 무인점포
- 결제수수료
- 유지보수
- theft/shrink
- 고객불만
- 직원 업무 재배치
- local regulation

CONSUMER_REGULATED_PRODUCT
- 전자담배
- nicotine pouch
- FDA authorization
- youth usage
- public health warning
- cannabis rescheduling
- medical cannabis
- DEA registration
- state/federal conflict
```

---

# 4. 성공사례 / 구조 후보

## 4-1. Bayer Crop Science — `AGRI_INPUT_SEED_CROP_PROTECTION`

Bayer는 2026년 1분기 조정 EBITDA가 9% 증가한 44.5억 유로로 예상치를 크게 웃돌았고, Crop Science 부문 EBITDA는 soy seed licensing dispute 해결 효과로 17.9% 증가했다. 이 케이스는 종자·작물보호제가 단순 commodity가 아니라 **licensing, IP, 특허, 농가 ROI, 소송 리스크**가 결합된 구조라는 점을 보여준다. 동시에 Roundup litigation은 계속 RedTeam이다. ([Reuters][1])

```text
가격경로 1차 판정:
AGRI_INPUT_LICENSED_SEED_CROP_PROTECTION_CANDIDATE

좋은 점:
- soy seed licensing 효과
- Crop Science EBITDA 증가
- 종자·작물보호제의 IP/라이선스 구조
- 농가 생산성 개선 수요
- 가격전가 가능성

주의:
- Roundup litigation
- 부채 부담
- crop price와 farmer margin 영향
- 규제·환경 리스크
```

**Loop 6 교정**

```text
AGRI_INPUT_SEED_CROP_PROTECTION:
비료·농약·종자는 한 덩어리가 아니다.

Seed/IP/licensing:
Visibility 가점 가능.

Crop protection:
규제·소송·특허만료 감점.

Fertilizer:
input-cost cycle과 농가 margin을 먼저 본다.
```

---

## 4-2. Nutrien potash / phosphate — `FERTILIZER_INPUT_COST_CYCLE` + `FERTILIZER_STRATEGIC_PHOSPHATE_OPTION`

Nutrien은 2026년 글로벌 potash 수요가 4년 연속 증가할 수 있다고 봤고, 2025년 큰 작황이 토양 영양분을 소모하면서 potash 수요를 지지한다고 설명했다. 동시에 phosphate 사업은 전략광물 지정 가능성, 높은 북미 phosphate 가격, 사업 재편 또는 매각 option이 붙어 있다. 하지만 이 구조는 Green이라기보다 **volume·price·farmer margin·supply discipline이 함께 움직이는 cycle/Watch**다. ([Reuters][2])

```text
가격경로 1차 판정:
FERTILIZER_POTASH_DEMAND_CYCLE_WATCH
+
PHOSPHATE_STRATEGIC_OPTION_WATCH

좋은 점:
- potash 수요 강함
- 토양 영양분 보충 수요
- phosphate 전략광물 narrative
- 사업 재편 option

주의:
- crop price 약세
- 농가 margin 악화
- input cost spike
- nitrogen/phosphate/potash 구조 차이
- fertilizer는 commodity cycle 성격 강함
```

**Loop 6 교정**

```text
FERTILIZER_INPUT_COST_CYCLE:
potash demand는 가점.
phosphate strategic option도 가점.

하지만 Stage 3-Green은 제한.

필수:
fertilizer_volume
price
farmer_margin
crop_price
input_cost
FCF
```

---

## 4-3. Zoetis 조류독감 백신 — `ANIMAL_HEALTH_BIOSECURITY`

Zoetis는 미국 USDA로부터 가금류 조류독감 백신 조건부 승인을 받았다. 조건부 license는 emergency나 special circumstance에서 safety와 reasonable expectation of efficacy를 근거로 부여되며, USDA는 현재 유행 strain에 맞춘 poultry vaccine stockpile을 재구축하려 했다. 이건 단순 질병 뉴스가 아니라 **조건부 승인 + 정부 비축 가능성**이 붙은 Stage 1~2 후보로 볼 수 있다. ([Reuters][3])

```text
가격경로 1차 판정:
ANIMAL_HEALTH_EVENT_TO_CONTRACT_CANDIDATE

좋은 점:
- USDA 조건부 승인
- HPAI 대응 필요성
- 정부 stockpile 가능성
- animal health distribution channel
- 반복 접종 가능성

주의:
- emergency license
- 실제 정부 구매 규모 미확인
- outbreak 정상화
- 무역 제한 우려
- one-off stockpile 가능성
```

**Loop 6 교정**

```text
ANIMAL_HEALTH_BIOSECURITY:
질병 뉴스만 있으면 Event/Watch.

조건부 승인
+ 정부 비축
+ 반복 접종 가능성

이 붙으면 Stage 2 후보.

Stage 3는 실제 주문·반복 매출·OPM 확인 후.
```

---

## 4-4. Duolingo — `EDTECH_AI_MONETIZATION_TRADEOFF`

Duolingo는 AI speaking 기능을 더 낮은 요금제와 무료 사용자에게 확대해 user growth를 우선하겠다고 밝혔다. 하지만 2026년 Q1과 연간 bookings 전망이 시장 예상보다 낮았고, 주가는 23% 넘게 하락했다. 이 사례는 교육 앱이 사용자 수와 AI 기능만으로 Green이 아니라, **bookings, paid conversion, AI 기능 비용, margin, FCF**를 통과해야 한다는 기준이다. ([Reuters][4])

```text
가격경로 1차 판정:
EDUCATION_APP_SUCCESS_CANDIDATE_BUT_MONETIZATION_WATCH

좋은 점:
- 대규모 사용자 기반
- AI speaking 기능
- subscription model
- global scale
- buyback authorization

주의:
- bookings miss
- monetization 후퇴
- AI 기능 비용
- user growth와 profitability trade-off
- DAU growth 둔화
```

**Loop 6 교정**

```text
EDTECH_AI_MONETIZATION_TRADEOFF 강화.

AI 기능 확대는 무조건 가점이 아니다.
AI가 engagement를 키우더라도 bookings와 margin이 꺾이면 Stage 3 제한.
```

---

## 4-5. Juul FDA authorization — `CONSUMER_REGULATED_PRODUCT`

Juul은 2025년 7월 FDA로부터 device와 tobacco·menthol flavored refill cartridges 판매 승인을 받았다. 이는 2022년 federal ban 이후 큰 반전이고, FDA가 public health 기준에서 marketing authorization이 적절하다고 판단한 사례다. 하지만 허가 범위는 tobacco/menthol 중심이고, youth vaping 논란과 public health regulation은 계속 RedTeam이다. ([Reuters][5])

```text
가격경로 1차 판정:
REGULATED_CONSUMER_APPROVAL_STAGE2_CANDIDATE

좋은 점:
- FDA marketing authorization
- 반복소비 가능성
- device + cartridge ecosystem
- 과거 ban 리스크 일부 해소

주의:
- 허가 범위 제한
- 청소년 사용 논란
- public health regulation
- flavored vape 규제
- 판매·마케팅 제한
```

**Loop 6 교정**

```text
CONSUMER_REGULATED_PRODUCT:
규제 승인 전에는 Watch/Red.
승인 후에도 허가 범위, 청소년 사용, 판매채널, 반복매출을 확인해야 Stage 3 가능.
```

---

## 4-6. Cannabis partial rescheduling — `CANNABIS_REGULATED_PRODUCT`

2026년 4월 DOJ와 DEA는 일부 cannabis-related substances를 Schedule I에서 Schedule III로 재분류했다. 다만 이 조치는 연방 차원의 완전 합법화가 아니고, FDA-approved cannabis products와 state-licensed medical cannabis 중심의 부분적 조치다. 의료 cannabis 사업자에는 280E 세금 부담 완화 같은 효과가 있을 수 있지만, recreational operator는 직접 수혜가 제한되고 DEA registration·state/federal conflict가 남는다. ([Reuters][6])

```text
가격경로 1차 판정:
CANNABIS_PARTIAL_RESCHEDULING_STAGE1_2_WATCH

좋은 점:
- medical cannabis federal recognition
- 280E tax burden 완화 가능성
- research / compliance path 일부 개선
- 규제형 소비재의 Stage 2 후보

주의:
- federal legalization 아님
- recreational operator 직접수혜 제한
- DEA registration 필요
- state/federal law conflict
- legal challenges 가능성
```

**Loop 6 교정**

```text
CANNABIS_REGULATED_PRODUCT:
규제 완화 뉴스는 Stage 1~2.
Stage 3는 실제 license, sales channel, tax effect, compliance cost, FCF 확인 후.
```

---

# 5. 반례 / RedTeam

## 5-1. Deere 농기계 demand cycle — `AGRI_MACHINERY_DEMAND_CYCLE`

Deere는 2025년 1분기 매출이 35% 감소했고, 약한 농가소득과 높은 차입비용 때문에 농가가 장비 구매 대신 렌탈을 택하면서 premarket에서 주가가 약 4.5% 하락했다. 생산·정밀농업 부문 매출도 15~20% 감소할 것으로 전망됐다. 즉 자율농기계·정밀농업 기술이 있어도, 농기계는 결국 농가 capex cycle을 통과해야 한다. ([Reuters][7])

```text
가격경로 1차 판정:
AGRI_MACHINERY_TECH_BUT_CYCLE_4C_WATCH

교훈:
자율농기계 기술
≠ 장비 cycle 면제

필수 확인:
- farm_income_indicator
- crop_price
- farmer_financing_cost
- dealer_inventory
- equipment_sales_growth
```

---

## 5-2. CNH demand slowdown — `AGRI_MACHINERY_DEMAND_CYCLE`

CNH Industrial도 2025년 full-year profit forecast를 낮췄고, 낮은 crop price와 높은 생산비 때문에 농가가 큰 장비 구매를 미루면서 dealer inventory가 높아졌다고 설명했다. 발표 후 주가는 7.1% 하락했다. 이 케이스는 농기계·정밀농업 관련주에서 기술 narrative보다 **farm income, crop price, financing cost, dealer inventory**를 먼저 봐야 한다는 기준이다. ([Reuters][8])

```text
가격경로 1차 판정:
AGRI_MACHINERY_DEMAND_CYCLE_4C_WATCH

감점 조건:
- crop_price_weakness
- farmer_margin_pressure
- high_financing_cost
- dealer_inventory_high
- production_cut
- profit_forecast_cut
```

---

## 5-3. Deere right-to-repair — `RIGHT_TO_REPAIR_REGULATORY_OVERLAY`

Deere는 농업장비 right-to-repair 집단소송을 9,900만 달러 settlement fund와 10년간 디지털 수리도구 제공 약속으로 해결하기로 했다. 별도로 FTC 소송도 남아 있다. 이건 농기계 software lock-in이 좋아 보여도, 수리 독점·dealer network·regulatory scrutiny가 lock-in thesis를 깨뜨릴 수 있음을 보여준다. ([Reuters][9])

```text
가격경로 1차 판정:
AGRI_MACHINERY_SOFTWARE_LOCKIN_REGULATORY_WATCH

교훈:
software-enabled equipment
≠ 무조건 좋은 lock-in

감점 조건:
- right_to_repair_flag
- repair_monopoly_allegation
- settlement_cost
- FTC_lawsuit_flag
- customer_backlash
```

---

## 5-4. Deere right-to-repair 건설·임업 확장 — `RIGHT_TO_REPAIR_CONSTRUCTION_EXPANSION`

Loop 6에서는 right-to-repair가 농기계에서 건설·임업 장비로 확장되는 점도 추가한다. 2026년 5월 15일에는 Chicago landscaping contractor가 Deere의 construction/forestry equipment 수리 소프트웨어 접근 제한을 문제 삼아 소송을 제기했다. 이 소송은 앞선 농업장비 right-to-repair settlement와 같은 연방법원에서 진행되며, Deere의 construction and forestry segment가 연간 약 110억 달러 매출을 낸다는 점도 지적됐다. ([월스트리트저널][10])

```text
가격경로 1차 판정:
RIGHT_TO_REPAIR_RISK_EXPANDS_BEYOND_AGRI

의미:
농기계 right-to-repair는 R12만의 문제가 아니다.
건설기계·임업장비·R1/R10 장비주에도 software lock-in regulatory gate를 확장해야 한다.

감점 조건:
- construction_equipment_repair_lawsuit
- independent_repair_access_restriction
- dealer_network_dependency
- class_action_expansion_risk
```

---

## 5-5. Bowery shutdown — `VERTICAL_FARMING_UNIT_ECONOMICS`

Bowery는 7억 달러 이상을 조달한 vertical farming unicorn이었지만 2024년 폐쇄됐다. Axios는 Bowery가 AeroFarms와 AppHarvest 같은 실패 사례를 뒤따랐고, 소비자가 “cleaner produce”에 충분한 premium을 지불하지 않았다고 설명했다. 수직농장은 기술적으로 좋아 보여도 전력비·CAPEX·가격 프리미엄·수율·수요가 맞지 않으면 hard 4C로 간다. ([Axios][11])

```text
가격경로 1차 판정:
VERTICAL_FARMING_UNIT_ECONOMICS_4C

교훈:
스마트팜 기술
≠ Green

4C 조건:
- energy_cost_failure
- premium_pricing_failure
- CAPEX_burden
- consumer_adoption_failure
- yield_loss
- debt_burden
- shutdown
```

**Loop 6 교정**

```text
SMART_FARM_AGRI_TECH와 VERTICAL_FARMING_UNIT_ECONOMICS를 분리한다.

온실·정밀농업 운영계약:
Watch-to-Green 가능.

수직농장 leafy greens:
unit economics 통과 전 Watch/Red.
```

---

## 5-6. Cal-Maine / 계란 가격 cycle — `LIVESTOCK_DISEASE_PRICE_REGULATORY`

계란·육계·양돈주는 질병과 가격 사이클로 이익이 폭발할 수 있지만, 구조적 Green과는 다르다. Cal-Maine은 조류독감에 따른 record egg price 속에서 DOJ 가격조사 대상이 되었고, 조사 뉴스 후 after-hours에서 주가가 4% 넘게 하락했다. 같은 분기 매출은 높은 계란가격 덕에 거의 두 배가 됐지만, EPS는 예상치를 살짝 밑돌았다. ([AP News][12])

```text
가격경로 1차 판정:
LIVESTOCK_PRICE_CYCLICAL_SUCCESS + REGULATORY_WATCH

좋은 점:
- 공급차질로 가격 급등
- 단기 EPS 폭발 가능
- 생산능력·재고 보유 기업 수혜

주의:
- 가격 정상화
- 조류독감 one-off
- DOJ price investigation
- 소비자·정책 반발
```

**Loop 6 교정**

```text
AGRI_LIVESTOCK_FOOD_COMMODITY:
EPS가 크게 뛰어도 대부분 cyclical_success.
Stage 3-Green은 매우 제한.
가격 정상화와 정부조사 flag를 반드시 둔다.
```

---

## 5-7. Chegg — `EDTECH_AI_DISRUPTION` + `EDTECH_AI_SEARCH_DISINTERMEDIATION`

Chegg는 생성AI가 기존 교육 서비스 비즈니스모델을 직접 잠식한 대표 반례다. 2023년에 ChatGPT가 신규 고객 성장에 영향을 준다고 인정한 뒤 주가가 거의 절반 가까이 급락했고, 이후 2025년에는 AI와 검색 노출 변화로 traffic·revenue가 훼손되며 대규모 구조조정이 이어졌다. ([Investopedia][13]) ([San Francisco Chronicle][14])

```text
가격경로 1차 판정:
EDTECH_AI_DISRUPTION_HARD_4C

교훈:
교육 플랫폼 반복매출
≠ Green

4C 조건:
- AI가 핵심 서비스를 대체
- traffic decline
- subscriber decline
- revenue guide miss
- layoffs
- strategic review
```

**Loop 6 교정**

```text
EDTECH_AI_SEARCH_DISINTERMEDIATION 신규 추가.

교육·콘텐츠·Q&A 서비스는:
ChatGPT류 answer engine
+ Google AI Overviews류 search disintermediation

을 동시에 RedTeam으로 둔다.
```

---

## 5-8. 2U Chapter 11 — `ONLINE_EDUCATION_OPM_DISTRESS`

2U는 온라인 교육·OPM 모델의 대표 반례다. 2U는 2024년 Chapter 11을 신청했고, 부채를 약 9.45억 달러에서 4.59억 달러 수준으로 줄이는 구조조정을 추진했다. 2U의 시가총액은 과거 50억 달러 이상에서 1,150만 달러 수준으로 떨어졌고, edX 인수, 경쟁 심화, 규제 변화, 높은 레버리지와 상환 압박이 복합적으로 작동했다. ([월스트리트저널][15])

```text
가격경로 1차 판정:
ONLINE_EDUCATION_OPM_HARD_4C

교훈:
온라인 교육 플랫폼
≠ Green

필수 확인:
- student ROI
- CAC
- partner concentration
- completion rate
- debt
- FCF
- regulatory oversight
```

---

## 5-9. Whirlpool hardware cycle — `HOME_APPLIANCE_HARDWARE_CYCLE`

Whirlpool은 생활가전 hardware cycle의 기준 반례다. 2026년 1분기 실적 부진 후 분기 배당 90센트를 중단했고, 2026년 EPS 전망을 7달러에서 3~3.50달러로 낮췄으며, free cash flow 전망도 4.5억 달러에서 3억 달러로 낮췄다. 주가는 52주 신저가를 기록했고, 2021년 고점 대비 83.8% 하락한 상태로 보도됐다. ([Barron's][16])

```text
가격경로 1차 판정:
HOME_APPLIANCE_HARDWARE_CYCLE_4C

교훈:
생활가전 hardware 판매
≠ Green

4C 조건:
- replacement_demand_collapse
- housing_turnover_weakness
- dividend_suspension
- guidance_cut
- debt_reduction_pressure
- promotional_environment
```

**Loop 6 교정**

```text
HOME_LIVING_APPLIANCE_RENTAL:
렌탈 계정·해지율·관리서비스 매출이 없으면 hardware cycle로 강등.
```

---

## 5-10. Target / Santa Ana self-checkout regulation — `SELF_CHECKOUT_LOCAL_REGULATION_OVERLAY`

키오스크·셀프체크아웃은 설치대수만 보면 안 된다. Target은 2024년에 약 2,000개 매장에서 self-checkout을 10개 품목 이하 express lane으로 제한했고, Santa Ana는 2026년 6월부터 food/drug retailer에 self-checkout 15개 품목 제한, staffed lane 유지, self-checkout 3대당 직원 1명 모니터링 등을 요구하는 ordinance를 시행한다. 즉 self-checkout은 theft, customer friction, 직원 배치, local regulation을 통과해야 한다. ([Axios][17]) ([The Sun][18])

```text
가격경로 1차 판정:
KIOSK_SELF_CHECKOUT_OPERATIONAL_COUNTEREXAMPLE

교훈:
키오스크 설치대수 증가
≠ Green

필수 확인:
- maintenance revenue
- 결제수수료
- theft/shrink 감소
- customer friction 감소
- retailer retention
- local regulation
```

---

## 5-11. Nicotine pouch youth-safety — `NICOTINE_POUCH_YOUTH_SAFETY_OVERLAY`

WHO는 2026년 5월 15일 nicotine pouch 규제가 느슨하면 youth addiction을 키울 수 있다고 경고했다. social media influencer, lifestyle branding, youth-oriented event sponsorship, flavor·packaging, 높은 니코틴 함량이 핵심 리스크로 지적됐고, WHO는 니코틴 함량 제한, 광고 제한, flavor restriction을 권고했다. 즉 니코틴 pouch는 반복소비 구조가 있어도 public health gate를 통과해야 한다. ([Reuters][19])

```text
가격경로 1차 판정:
NICOTINE_ALTERNATIVE_REGULATORY_WATCH

교훈:
반복소비
≠ Green

감점 조건:
- youth_usage_risk
- flavored_product_restriction
- public_health_warning
- unauthorized_product_status
- enforcement_policy_change
```

---

# 6. 4B-watch 사례

## 6-1. 스마트팜·수직농장 4B-watch

```text
4B 조건:
- AI 농업·스마트팜·수직농장 narrative로 관련주 동반 급등
- 실제 수주·운영계약·unit economics 없이 valuation 상승
- 전력비·CAPEX·수율·소비자 가격 프리미엄을 시장이 무시
```

Bowery shutdown은 스마트팜이 기술 narrative만으로 Green이 될 수 없다는 기준 반례다. ([Axios][11])

---

## 6-2. 농기계 자율화 4B-watch

```text
4B 조건:
- 자율농기계·정밀농업 기술 발표 후 관련주 과열
- 농가소득·금리·장비 교체 cycle이 나쁜데 기술만 반영
- right-to-repair 규제 리스크를 시장이 낮게 봄
```

Deere의 매출 35% 감소와 CNH의 forecast cut은 농기계가 기술주이면서 동시에 농가 capex-cycle 기업임을 보여준다. ([Reuters][7]) ([Reuters][8])

---

## 6-3. 농기계 software lock-in 4B-watch

```text
4B 조건:
- precision agriculture software와 repair lock-in을 고마진 recurring moat로만 해석
- right-to-repair settlement와 FTC litigation을 무시
- 건설·임업장비까지 소송이 확장될 수 있음을 낮게 봄
```

Deere의 9,900만 달러 settlement와 새 construction/forestry equipment lawsuit는 software lock-in이 규제·소송으로 깨질 수 있음을 보여준다. ([Reuters][9]) ([월스트리트저널][10])

---

## 6-4. 종자·비료·농약 4B-watch

```text
4B 조건:
- 식량안보·비료 가격·종자 IP narrative로 관련주 과열
- crop price와 farmer margin을 확인하지 않음
- 원재료 spike를 가격전가력으로 오판
- 소송·규제 리스크를 낮게 봄
```

Bayer의 soy licensing 효과와 Nutrien의 potash 수요는 좋은 Stage 2 근거가 될 수 있지만, 비료·작물보호제·종자는 각각 농가 ROI, 원재료, crop price, 소송·규제 리스크를 따로 봐야 한다. ([Reuters][1]) ([Reuters][2])

---

## 6-5. 조류독감·계란·육계·양돈 4B-watch

```text
4B 조건:
- 조류독감·ASF·공급차질로 계란/육계/양돈 관련주 급등
- 가격 정상화 가능성을 시장이 무시
- 정부조사·가격담합 리스크를 반영하지 않음
```

Cal-Maine의 계란가격 상승 수혜와 DOJ 조사 동시 발생은 축산 관련주를 구조적 Green으로 오분류하면 안 된다는 기준이다. ([AP News][12])

---

## 6-6. AI 교육·성인교육 4B-watch

```text
4B 조건:
- AI 재교육·reskilling narrative로 교육주 valuation 상승
- 실제 completion rate, CAC, B2B 계약, student ROI 미확인
- AI가 오히려 기존 교육 서비스를 대체할 수 있다는 점을 무시
```

Duolingo는 AI 기능 확대와 user growth를 제시했지만 bookings 전망 부진으로 급락했고, Chegg는 ChatGPT와 AI 검색이 core service 수요를 훼손한 대표 반례다. ([Reuters][4]) ([Investopedia][13])

---

## 6-7. 렌탈 생활가전 4B-watch

```text
4B 조건:
- 렌탈 계정 증가만 보고 valuation 상승
- 해지율·관리비용·해외 마진·품질 리스크 미확인
- hardware cycle 위험을 시장이 낮게 봄
```

Whirlpool 사례처럼 일반 생활가전 hardware cycle은 렌탈 반복매출과 완전히 다른 위험 구조다. ([Barron's][16])

---

## 6-8. 키오스크·셀프체크아웃 4B-watch

```text
4B 조건:
- 인건비 상승·무인화 narrative로 키오스크 관련주 급등
- retailer가 self-checkout을 줄이는 흐름을 무시
- theft/shrink와 customer friction을 반영하지 않음
- 지자체 규제를 무시
```

Target의 10-item self-checkout limit와 Santa Ana의 self-checkout regulation은 self-checkout이 항상 retailer ROI를 높이는 자동화가 아니라는 기준이다. ([Axios][17]) ([The Sun][18])

---

## 6-9. 규제형 소비재 4B-watch

```text
4B 조건:
- FDA 승인, enforcement 완화, cannabis rescheduling 뉴스만으로 관련주 동반 급등
- 실제 허가 범위·판매채널·반복매출·청소년 사용 리스크 미확인
- 규제 반전 가능성을 낮게 봄
```

Juul 승인과 cannabis rescheduling은 모두 Stage를 올릴 수 있는 정책 이벤트지만, public health·허가범위·state/federal conflict가 남아 있다. ([Reuters][5]) ([Reuters][6])

---

# 7. 4C-thesis-break 사례

## 7-1. 스마트팜 unit economics 붕괴

```text
4C:
vertical_farm_shutdown
Chapter_11
energy_cost_failure
premium_pricing_failure
yield_loss
CAPEX_burden
consumer_adoption_failure
```

Bowery는 수직농장·스마트팜의 hard 4C 기준이다. ([Axios][11])

---

## 7-2. 농기계 capex cycle 하락

```text
4C-watch:
farm_income_weakness
high_borrowing_costs
equipment_rental_instead_of_purchase
tariff_uncertainty
segment_sales_decline
dealer_inventory
```

Deere의 2025년 매출 35% 감소와 premarket -4.5% 반응은 농기계가 기술주가 아니라 capex-cycle 기업임을 보여준다. ([Reuters][7])

---

## 7-3. 농기계 software lock-in 규제

```text
4C-watch:
right_to_repair_lawsuit
repair_monopoly_allegation
settlement_cost
dealer_network_conflict
FTC_lawsuit
construction_equipment_litigation
customer_backlash
```

Deere의 right-to-repair settlement와 건설·임업장비 소송 확장은 농기계 소프트웨어 lock-in이 규제·소송으로 깨질 수 있음을 보여준다. ([Reuters][9]) ([월스트리트저널][10])

---

## 7-4. 종자·작물보호제 소송/규제 리스크

```text
4C-watch:
seed_licensing_dispute
crop_protection_litigation
patent_expiry
regulatory_restriction
farmer_margin_pressure
```

Bayer Crop Science는 soy licensing 효과로 실적이 좋아질 수 있지만, Roundup litigation과 부채 부담이 동시에 존재한다. 종자·농약은 IP가 강점이지만, 그 IP와 규제·소송이 같은 칼날의 양면이다. ([Reuters][1])

---

## 7-5. 비료 input cost / farmer margin break

```text
4C-watch:
fertilizer_input_cost_spike
crop_price_decline
farmer_margin_pressure
demand_deferral
guidance_withdrawal
```

Nutrien은 potash 수요가 강한 쪽이지만, 비료 전체는 crop price, farmer margin, nitrogen/phosphate 원재료, 지정학 공급차질에 매우 민감하다. 따라서 비료주는 “식량안보”가 아니라 volume·price·input cost·farmer ROI로 봐야 한다. ([Reuters][2])

---

## 7-6. 교육 AI disruption

```text
4C:
AI_substitutes_core_service
AI_search_disintermediation
traffic_decline
subscriber_decline
bookings_miss
layoffs
strategic_review
bankruptcy_or_distress
```

Chegg는 ChatGPT 충격으로 core service가 직접 훼손된 사례이고, 2U는 온라인 교육 OPM 모델의 부채·규제·경쟁 문제로 Chapter 11에 들어간 사례다. ([Investopedia][13]) ([월스트리트저널][15])

---

## 7-7. 생활가전 hardware cycle 붕괴

```text
4C:
replacement_demand_collapse
housing_turnover_weakness
dividend_suspension
guidance_cut
debt_reduction_pressure
FCF_cut
```

Whirlpool의 배당 중단과 EPS·FCF 전망 하향은 hardware 생활가전의 대표 4C다. ([Barron's][16])

---

## 7-8. 키오스크·셀프체크아웃 후퇴

```text
4C-watch:
retailer_retreat
theft_shrink
customer_friction
employee_workload
one_off_hardware_sales
local_regulation
```

Target의 self-checkout 제한과 Santa Ana의 self-checkout regulation은 키오스크 기업이 설치대수만으로 Stage 3-Green이 될 수 없다는 기준이다. ([Axios][17]) ([The Sun][18])

---

## 7-9. 규제형 소비재 불허가·정책 반전

```text
4C-watch:
FDA_ban
limited_authorization_scope
youth_usage_controversy
DEA_registration_failure
state_federal_law_conflict
public_health_backlash
```

Juul은 2022년 ban에서 2025년 승인으로 바뀐 사례이고, cannabis rescheduling도 완전 합법화가 아니라 제한적 정책 변화다. 그래서 규제형 소비재는 승인 전후 모두 hard RedTeam이 필요하다. ([Reuters][5]) ([Reuters][6])

---

## 7-10. Nicotine pouch youth-safety break

```text
4C-watch:
youth_addiction_warning
high_nicotine_content
flavor_restriction
advertising_ban
influencer_marketing_risk
public_health_backlash
```

WHO의 nicotine pouch 경고는 “담배 대체재라서 반복소비 Green”이라는 단순 프레임을 막아야 하는 기준이다. 반복소비가 있어도 youth addiction·flavor·광고·public health gate를 통과해야 한다. ([Reuters][19])

---

# 8. 점수비중 보정표 — R12 Loop 6 / v6.0

| canonical archetype                      | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | Loop 6 핵심 감점                                         |
| ---------------------------------------- | ------: | ---------: | ---------: | ---------: | --------: | ------: | ---: | ---------------------------------------------------- |
| `SMART_FARM_AGRI_TECH`                   |      17 |         13 |         12 |          9 |         8 |       0 |    5 | 에너지비, CAPEX, unit economics                          |
| `VERTICAL_FARMING_UNIT_ECONOMICS`        |       8 |          6 |          5 |          7 |         5 |       0 |    4 | shutdown, Chapter 11, premium pricing 실패             |
| `AGRI_MACHINERY_PRECISION_CYCLE`         |      16 |         13 |         10 |         10 |         9 |       1 |    5 | 농가소득, 금리, 장비 cycle                                   |
| `AGRI_MACHINERY_DEMAND_CYCLE`            |      14 |         11 |          8 |          9 |         7 |       1 |    5 | farm income, crop price, dealer inventory            |
| `AGRI_MACHINERY_SOFTWARE_LOCKIN`         |      16 |         14 |          9 |         11 |         9 |       1 |    5 | right-to-repair, settlement, FTC risk                |
| `RIGHT_TO_REPAIR_REGULATORY_OVERLAY`     |    gate |       gate |       gate |       gate |      gate |    gate | gate | 수리독점·소송·FTC·고객반발                                     |
| `RIGHT_TO_REPAIR_CONSTRUCTION_EXPANSION` |    gate |       gate |       gate |       gate |      gate |    gate | gate | 건설·임업장비로 소송 확장                                       |
| `AGRI_INPUT_SEED_CROP_PROTECTION`        |      18 |         16 |         11 |         12 |        10 |       1 |    5 | 소송, 특허만료, farmer margin, 규제                          |
| `FERTILIZER_INPUT_COST_CYCLE`            |      18 |         11 |         14 |          9 |         8 |       0 |    5 | crop price, input cost, 농가마진, 지정학 공급차질               |
| `FERTILIZER_STRATEGIC_PHOSPHATE_OPTION`  |      16 |         12 |         13 |         10 |         8 |       0 |    5 | 전략광물 narrative, 사업재편·매각 불확실성                         |
| `AGRI_LIVESTOCK_FOOD_COMMODITY`          |      18 |          8 |         14 |          8 |         7 |       0 |    5 | 질병, 사료비, 가격 정상화, 정부조사                                |
| `LIVESTOCK_DISEASE_PRICE_REGULATORY`     |    gate |       gate |       gate |       gate |      gate |    gate | gate | 가격조사·담합·소비자 반발                                       |
| `ANIMAL_HEALTH_BIOSECURITY`              |      18 |         16 |          8 |         11 |         9 |       0 |    5 | 정부 사용정책, one-off stockpile, outbreak 정상화             |
| `AGRI_DISEASE_AI_MONITORING`             |      14 |         12 |          8 |         10 |         8 |       0 |    5 | 데이터품질, farm privacy, 도입계약 부재                         |
| `EDUCATION_SPECIALTY_SERVICES`           |      17 |         16 |          5 |         12 |        10 |       2 |    5 | AI 대체, CAC, bookings miss, completion rate           |
| `EDTECH_AI_MONETIZATION_TRADEOFF`        |      16 |         15 |          5 |         12 |         9 |       1 |    5 | AI 기능비용, bookings miss, monetization 후퇴              |
| `EDTECH_AI_DISRUPTION`                   |    gate |       gate |       gate |       gate |      gate |    gate | gate | AI 대체, traffic/subscriber collapse                   |
| `EDTECH_AI_SEARCH_DISINTERMEDIATION`     |    gate |       gate |       gate |       gate |      gate |    gate | gate | 검색트래픽 감소, AI Overviews, 콘텐츠 대체                       |
| `ONLINE_EDUCATION_OPM_DISTRESS`          |      10 |          8 |          4 |          8 |         5 |       0 |    5 | 부채, student ROI, Chapter 11, 규제                      |
| `HOME_CHILD_EDUCATION`                   |      15 |         11 |          5 |         10 |         8 |       0 |    5 | 저출산, TAM 축소, 재고                                      |
| `HOME_LIVING_APPLIANCE_RENTAL`           |      18 |         16 |          6 |         12 |        11 |       2 |    5 | 해지율, 해외마진, hardware cycle, 품질 리콜                     |
| `HOME_APPLIANCE_HARDWARE_CYCLE`          |      14 |         10 |          5 |          8 |         6 |       0 |    5 | 교체수요 붕괴, 배당중단, guidance cut                          |
| `SERVICE_KIOSK_SELF_CHECKOUT`            |      15 |         13 |          7 |         10 |         8 |       0 |    5 | theft, 고객불만, retailer retreat, one-off hardware      |
| `SELF_CHECKOUT_LOCAL_REGULATION_OVERLAY` |    gate |       gate |       gate |       gate |      gate |    gate | gate | item limit, 직원 배치, local ordinance                   |
| `CONSUMER_REGULATED_PRODUCT`             |      18 |         15 |          8 |         12 |        10 |       0 |    5 | 규제, public health, 허가 범위                             |
| `NICOTINE_ALTERNATIVE_REGULATED`         |      16 |         13 |          8 |         10 |         8 |       0 |    5 | 청소년 사용, flavor restriction, WHO warning              |
| `NICOTINE_POUCH_YOUTH_SAFETY_OVERLAY`    |    gate |       gate |       gate |       gate |      gate |    gate | gate | youth addiction, high nicotine, influencer marketing |
| `CANNABIS_REGULATED_PRODUCT`             |      16 |         14 |          8 |         11 |         8 |       0 |    5 | 완전합법화 아님, DEA 등록, state/federal conflict             |
| `CANNABIS_PARTIAL_RESCHEDULING_LIMIT`    |    gate |       gate |       gate |       gate |      gate |    gate | gate | 의료 cannabis 한정, recreational 수혜 제한                   |
| `FOOD_INPUT_REGULATED_CYCLE`             |      17 |         11 |         12 |          8 |         8 |       0 |    5 | 원가, 판가전가, 규제                                         |
| `AGRI_DISEASE_EVENT_OVERLAY`             |    gate |       gate |       gate |       gate |      gate |    gate | gate | 조류독감·ASF·질병 one-off                                  |
| `REGULATED_CONSUMER_APPROVAL_OVERLAY`    |    gate |       gate |       gate |       gate |      gate |    gate | gate | FDA/DEA 승인·불허가·public health                         |
| `DISCLOSURE_CONFIDENCE_CAP`              |     cap |        cap |        cap |        cap |       cap |     cap |    + | 계약·해지율·규제승인 detail 부족                                |

Loop 6에서 핵심 보정은 이거다.

```text
1. RIGHT_TO_REPAIR_CONSTRUCTION_EXPANSION을 추가.
   Deere right-to-repair risk가 농기계에서 건설·임업장비로 확장되고 있다.

2. AGRI_MACHINERY_DEMAND_CYCLE을 더 강하게 유지.
   Deere/CNH 사례처럼 자율농기계 기술보다 농가 capex cycle이 먼저다.

3. FERTILIZER_STRATEGIC_PHOSPHATE_OPTION을 추가.
   phosphate 전략광물 narrative는 가능하지만 fertilizer cycle과 farmer margin gate를 통과해야 한다.

4. LIVESTOCK_DISEASE_PRICE_REGULATORY를 gate로 추가.
   Cal-Maine 사례처럼 질병 수혜와 가격조사·담합 리스크가 동시에 붙는다.

5. EDTECH_AI_SEARCH_DISINTERMEDIATION을 추가.
   Chegg식 AI 대체는 ChatGPT뿐 아니라 Google AI 검색 변화까지 포함해야 한다.

6. SELF_CHECKOUT_LOCAL_REGULATION_OVERLAY를 강화.
   Target 자체 제한뿐 아니라 Santa Ana류 지자체 규제가 kiosk economics를 바꾼다.

7. NICOTINE_POUCH_YOUTH_SAFETY_OVERLAY를 더 강화.
   WHO 경고 이후 youth addiction·광고·flavor gate를 강하게 둔다.

8. CANNABIS_PARTIAL_RESCHEDULING_LIMIT을 추가.
   Schedule III 일부 전환은 federal legalization이 아니며, medical cannabis 중심이다.

9. HOME_APPLIANCE_HARDWARE_CYCLE은 더 보수적으로.
   Whirlpool 사례처럼 hardware 생활가전은 배당·FCF·교체수요가 깨지면 hard 4C다.
```

---

# 9. stage date 후보

## `SMART_FARM_AGRI_TECH`

```text
Stage 1:
스마트팜 정책, 자율농업, 농업 AI 뉴스

Stage 2:
실제 수주, 운영계약, 반복 유지보수·SaaS 매출, 가동률 확인

Stage 3:
unit economics와 FCF가 확인되고 반복계약이 붙을 때만

Stage 4B:
스마트팜 narrative 과열

Stage 4C:
파산, 폐쇄, energy cost, premium pricing 실패, CAPEX 부담
```

## `VERTICAL_FARMING_UNIT_ECONOMICS`

```text
Stage 1:
수직농장, indoor farm, AI farming narrative

Stage 2:
가동률, 생산원가, 고객계약, yield 안정, 가격 premium 확인

Stage 3:
반복 FCF와 고객 수요가 확인될 때만

Stage 4B:
vertical farming unicorn narrative 과열

Stage 4C:
shutdown, Chapter 11, yield loss, energy cost, premium pricing failure
```

## `AGRI_MACHINERY_PRECISION_CYCLE`

```text
Stage 1:
자율농기계·정밀농업 기술 발표

Stage 2:
농기계 판매 증가, 농가 ROI, 소프트웨어 attachment 확인

Stage 3:
농기계 cycle이 아니라 반복 SW/서비스 매출이 커질 때만

Stage 4B:
자율농기계 테마 과열

Stage 4C:
농가소득 약화, 고금리, 장비 판매 감소, tariff, right-to-repair 규제
```

## `AGRI_MACHINERY_DEMAND_CYCLE`

```text
Stage 1:
농기계 교체수요, 농가 생산성 향상, 정밀농업 narrative

Stage 2:
실제 장비 판매, dealer inventory 정상화, 농가소득 개선 확인

Stage 3:
반복 SW/서비스 매출이 장비 cycle 변동성을 완화할 때만

Stage 4B:
자율화·정밀농업 기대 과열

Stage 4C:
crop price 하락, financing cost 상승, rental 전환, dealer inventory 증가
```

## `AGRI_MACHINERY_SOFTWARE_LOCKIN`

```text
Stage 1:
정밀농업 software, 진단툴, connected machine, dealer network lock-in

Stage 2:
software attach rate, recurring software revenue, customer retention 확인

Stage 3:
right-to-repair 리스크를 통과하고 software revenue가 장비 cycle을 보완할 때

Stage 4B:
software lock-in moat 과열

Stage 4C:
right-to-repair settlement, FTC lawsuit, independent repair access 확대, customer backlash
```

## `AGRI_INPUT_SEED_CROP_PROTECTION`

```text
Stage 1:
종자·농약·작물보호제 가격 인상, licensing, 신제품, 식량안보 뉴스

Stage 2:
licensing revenue, 판매량 증가, 판가전가, 농가 ROI, EBITDA 개선 확인

Stage 3:
반복 seed/crop protection revenue + 소송·규제 리스크 통과 + FCF 확인

Stage 4B:
식량안보·종자 IP narrative 과열

Stage 4C:
소송비용, 특허만료, 규제제한, farmer margin 악화, 판매 지연
```

## `FERTILIZER_INPUT_COST_CYCLE`

```text
Stage 1:
비료 가격 상승, potash/phosphate/nitrogen 공급차질, crop nutrient depletion 뉴스

Stage 2:
판매량·가격·마진 개선, farmer application rate 확인

Stage 3:
구조적 Green은 제한. 저비용 공급·장기 수요·FCF가 확인될 때만

Stage 4B:
비료 가격 spike와 식량안보 narrative 과열

Stage 4C:
crop price 하락, farmer margin 악화, demand deferral, input cost spike, guidance cut
```

## `ANIMAL_HEALTH_BIOSECURITY`

```text
Stage 1:
질병 outbreak, 백신 조건부 승인, 정부 비축 뉴스

Stage 2:
정부 구매계약, 반복 접종, 매출 가이던스 상향 확인

Stage 3:
동물의약품 반복매출과 고객 다변화가 확인될 때만

Stage 4B:
질병 뉴스 후 동물백신주 과열

Stage 4C:
정부 구매 종료, 질병 정상화, 백신 미사용, 무역 제한
```

## `AGRI_LIVESTOCK_FOOD_COMMODITY`

```text
Stage 1:
조류독감, ASF, 곡물가격, 사료비, 어가·유가 뉴스

Stage 2:
판가전가, 영업이익 증가, 원가 안정 확인

Stage 3:
구조적 Green은 제한. 대부분 cyclical_success로 분리

Stage 4B:
가격 급등으로 관련주 과열

Stage 4C:
가격 정상화, 사료비 급등, 정부조사, 질병 정상화
```

## `EDUCATION_SPECIALTY_SERVICES`

```text
Stage 1:
AI 교육, 취업교육, 성인교육, B2B training 뉴스

Stage 2:
반복수강, 기업계약, completion rate, OPM 개선 확인

Stage 3:
AI 대체를 피하고 B2B/B2G recurring revenue가 확인될 때

Stage 4B:
AI 교육 narrative 과열

Stage 4C:
AI가 핵심 서비스를 대체, CAC 상승, subscriber decline, bookings miss, bankruptcy
```

## `EDTECH_AI_MONETIZATION_TRADEOFF`

```text
Stage 1:
AI speaking, AI tutor, AI learning app 기능 확대

Stage 2:
AI 기능이 user growth·engagement를 실제로 올리는지 확인

Stage 3:
bookings, paid conversion, margin, FCF가 같이 유지될 때만

Stage 4B:
AI education app narrative 과열

Stage 4C:
AI 기능비용 증가, bookings miss, monetization 후퇴, paid conversion 둔화
```

## `EDTECH_AI_SEARCH_DISINTERMEDIATION`

```text
Stage 1:
AI answer engine, AI Overviews, search traffic decline 뉴스

Stage 2:
traffic, subscriber, paid conversion, B2B pivot 효과 확인

Stage 3:
AI 대체를 피하고 새로운 recurring revenue가 확인될 때만

Stage 4B:
AI education pivot narrative 과열

Stage 4C:
traffic collapse, subscriber decline, layoffs, revenue guide miss
```

## `ONLINE_EDUCATION_OPM_DISTRESS`

```text
Stage 1:
온라인 학위·bootcamp·OPM 성장 뉴스

Stage 2:
student ROI, completion rate, partner retention, FCF 확인

Stage 3:
부채와 규제 리스크를 통과한 반복계약 확인 전까지 제한

Stage 4B:
online education platform premium 과열

Stage 4C:
Chapter 11, high leverage, regulatory scrutiny, partner concentration failure
```

## `HOME_LIVING_APPLIANCE_RENTAL`

```text
Stage 1:
렌탈 계정 증가, 해외 진출, 신제품 출시

Stage 2:
해지율 안정, 필터·관리 반복매출, OPM/FCF 개선

Stage 3:
렌탈 recurring revenue가 hardware cycle을 압도할 때

Stage 4B:
렌탈 계정 성장 narrative 과열

Stage 4C:
교체수요 붕괴, 배당중단, 해지율 상승, 품질 리콜, 주택경기 악화
```

## `SERVICE_KIOSK_SELF_CHECKOUT`

```text
Stage 1:
인건비 상승, 무인화, 키오스크 도입 뉴스

Stage 2:
설치대수, 유지보수 매출, 결제수수료, shrink 감소 확인

Stage 3:
recurring service revenue가 hardware 매출을 넘을 때만

Stage 4B:
무인화 테마 과열

Stage 4C:
retailer retreat, theft, 고객불만, employee workload, local regulation, one-off hardware 판매
```

## `CONSUMER_REGULATED_PRODUCT`

```text
Stage 1:
FDA/DEA 규제 완화, 허가, rescheduling 뉴스

Stage 2:
실제 판매허가, 채널, 반복소비, 세금효과, FCF 확인

Stage 3:
규제 안정성과 반복매출이 확인될 때만

Stage 4B:
규제 완화 뉴스로 관련주 과열

Stage 4C:
허가 취소, 판매금지, 주·연방법 충돌, 청소년 사용 논란
```

## `NICOTINE_ALTERNATIVE_REGULATED`

```text
Stage 1:
전자담배·니코틴 pouch 승인, enforcement 완화, 시장확대 뉴스

Stage 2:
허가 범위, 판매채널, 반복매출, age verification 확인

Stage 3:
public health backlash 없이 반복소비와 FCF가 확인될 때

Stage 4B:
니코틴 대체재 narrative 과열

Stage 4C:
WHO/FDA warning, youth addiction, flavor ban, 광고제한, 허가범위 제한
```

## `CANNABIS_REGULATED_PRODUCT`

```text
Stage 1:
Schedule III 전환, 의료 cannabis recognition, tax relief 뉴스

Stage 2:
DEA registration, license, 실제 tax effect, sales channel 확인

Stage 3:
medical cannabis 반복매출과 FCF가 규제 안정 속에서 확인될 때

Stage 4B:
cannabis rescheduling 뉴스로 관련주 과열

Stage 4C:
federal legalization 지연, recreational operator 수혜 제한, legal challenge, state/federal conflict
```

---

# 10. 가격경로 검증계획

## R12 Loop 6 공통 검증 방식

```text
1. 각 case의 stage1_date, stage2_date, stage3_date를 지정한다.
2. 해당 날짜의 종가를 stage_price로 저장한다.
3. MFE_30D / 90D / 180D / 1Y / 2Y를 계산한다.
4. MAE_30D / 90D / 180D / 1Y를 계산한다.
5. peak_price와 drawdown_after_peak를 계산한다.
6. 농가소득, 장비판매, 상품가격, 질병 이벤트, 반복매출, CAC,
   해지율, 규제 이벤트와 가격경로를 비교한다.
```

## Loop 6에서 새로 강제할 판정

```text
SMART_FARM_UNIT_ECONOMICS_ALIGNED:
스마트팜 수주·가동률·에너지비·FCF가 확인된 경우.

VERTICAL_FARMING_4C:
수직농장 폐쇄·파산·프리미엄 가격 실패.

AGRI_MACHINERY_TECH_BUT_CYCLE_WATCH:
자율농기계 기술은 있으나 농가소득·금리·장비판매 둔화.

AGRI_MACHINERY_DEMAND_4C:
crop price·farm income·dealer inventory·financing cost가 장비 수요를 꺾는 경우.

AGRI_MACHINERY_LOCKIN_REGULATORY_WATCH:
software attach는 있으나 right-to-repair 규제·소송이 존재.

RIGHT_TO_REPAIR_EXPANSION_4C:
농기계 right-to-repair가 건설·임업장비까지 확장되는 경우.

AGRI_INPUT_LICENSED_IP_SUCCESS:
seed/crop protection licensing이 EBITDA와 반복매출로 연결.

FERTILIZER_CYCLE_WITH_INPUT_RISK:
비료 수요는 있으나 crop price·농가마진·원재료·지정학 리스크가 큼.

ANIMAL_HEALTH_EVENT_TO_CONTRACT:
질병 이벤트가 백신 승인·정부 비축·반복 접종으로 승격.

LIVESTOCK_CYCLICAL_SUCCESS:
가격 급등으로 이익은 났지만 구조적 지속성은 낮음.

LIVESTOCK_REGULATORY_4C:
질병·가격 급등 후 가격조사·담합·소비자 반발 발생.

EDUCATION_RECURRING_ALIGNED:
B2B/B2G 계약·completion rate·CAC·FCF가 통과된 교육 서비스.

EDTECH_AI_MONETIZATION_FAILED:
AI 기능 확대는 했지만 bookings·margin·paid conversion이 약화.

EDUCATION_AI_DISRUPTION_4C:
AI가 핵심 서비스를 대체해 traffic·subscriber·revenue가 훼손.

EDTECH_SEARCH_DISINTERMEDIATION_4C:
AI 검색·AI 답변이 유입과 paid conversion을 잠식.

ONLINE_EDUCATION_OPM_4C:
부채·규제·student ROI 문제로 OPM 모델이 무너짐.

RENTAL_RECURRING_SUCCESS:
렌탈 계정·해지율·관리서비스 매출·FCF가 확인.

HARDWARE_CYCLE_FAILURE:
교체수요 둔화·배당중단·guidance cut으로 무너진 생활가전.

KIOSK_OPERATIONAL_FAILURE:
self-checkout 축소·theft·customer friction 발생.

SELF_CHECKOUT_LOCAL_REGULATION_4C:
item limit, 직원 배치 의무, local ordinance로 unit economics 악화.

REGULATED_CONSUMER_APPROVAL_STAGE2:
FDA/DEA 승인으로 Stage 2가 되지만 허가 범위와 public health gate 필요.

NICOTINE_YOUTH_SAFETY_4C:
청소년 사용·flavor·광고·WHO/FDA warning으로 thesis가 제한.

CANNABIS_RESCHEDULING_LIMITED_STAGE2:
Schedule III 일부 전환은 좋지만 완전 합법화·FCF 전환 전까지 제한.
```

## 이번 R12 Loop 6에서 우선 검증할 가격 case

| case_id                                     |    stage2 후보일 | 현재 1차 가격판정                                           |
| ------------------------------------------- | ------------: | ---------------------------------------------------- |
| `deere_farm_equipment_demand_slowdown_case` |    2025-02-13 | -4.5% premarket, cycle 4C-watch                      |
| `cnh_weak_farm_equipment_demand_case`       |    2025-11-07 | -7.1%, 농기계 수요 cycle watch                            |
| `deere_right_to_repair_settlement_case`     |    2026-04-07 | $99m settlement, software lock-in regulatory watch   |
| `deere_construction_right_to_repair_case`   |    2026-05-15 | right-to-repair risk가 construction/forestry로 확장      |
| `zoetis_bird_flu_vaccine_conditional_case`  |    2025-02-14 | animal health event-to-contract 후보                   |
| `bayer_soy_seed_license_crop_science_case`  |    2026-05-12 | seed/crop protection licensing candidate             |
| `nutrien_potash_phosphate_option_case`      |    2025-11-06 | fertilizer demand + phosphate strategic option       |
| `calmaine_egg_price_regulatory_case`        |    2025-04-08 | -4% after-hours, cyclical success + regulatory watch |
| `bowery_vertical_farming_shutdown_case`     |    2024-11-05 | vertical farming hard 4C                             |
| `duolingo_ai_strategy_bookings_miss_case`   |    2026-02-26 | -23%, monetization 4C-watch                          |
| `chegg_ai_disruption_case`                  |    2023-05 이후 | AI education hard 4C                                 |
| `chegg_ai_search_disintermediation_case`    |     2025~2026 | AI 검색·검색트래픽 RedTeam                                  |
| `2u_chapter11_case`                         |    2024-07-25 | online education OPM hard 4C                         |
| `coway_rental_recurring_case`               |    계정/해지율 확인일 | recurring home service 후보                            |
| `whirlpool_dividend_suspension_case`        |       2026-05 | hardware cycle 4C                                    |
| `target_self_checkout_limit_case`           |    2024-03-17 | kiosk operational counterexample                     |
| `santa_ana_self_checkout_regulation_case`   | 2026-06-04 시행 | local regulation overlay                             |
| `juul_fda_approval_case`                    |    2025-07-17 | regulated product Stage 2 후보                         |
| `who_nicotine_pouch_youth_warning_case`     |    2026-05-15 | public health RedTeam                                |
| `cannabis_schedule3_limited_case`           |    2026-04~05 | regulatory watch, not full legalization              |

---

# 11. 다음에 에이전트가 채워야 할 price fields

R12 Loop 6에서는 아래 필드를 채우게 해야 한다.

```text
case_id
symbol
company_name
primary_archetype
secondary_archetypes

stage1_date
stage2_date
stage3_date
stage4b_date
stage4c_date

stage1_price
stage2_price
stage3_price
stage4b_price
stage4c_price
peak_price
peak_date

MFE_30D
MFE_90D
MFE_180D
MFE_1Y
MFE_2Y

MAE_30D
MAE_90D
MAE_180D
MAE_1Y

drawdown_after_peak
below_stage2_price_flag
below_stage3_price_flag

farm_income_indicator
crop_price_change
equipment_sales_growth
dealer_inventory
precision_agriculture_revenue
autonomous_equipment_order
software_attach_rate
farmer_financing_cost
tariff_exposure_flag
right_to_repair_flag
repair_settlement_amount
ftc_lawsuit_flag
construction_equipment_repair_lawsuit_flag
independent_repair_access_flag

seed_revenue_growth
crop_protection_revenue_growth
licensing_revenue
soy_seed_license_flag
patent_expiry_flag
roundup_litigation_flag
regulatory_restriction_flag
farmer_roi_metric

fertilizer_volume
potash_sales_volume
phosphate_revenue
phosphate_strategic_mineral_flag
phosphate_asset_review_flag
nitrogen_price_change
fertilizer_price_change
crop_price_change
farmer_margin_indicator
input_cost_spike_flag
guidance_withdrawal_flag
supply_disruption_flag

vertical_farming_revenue
vertical_farming_energy_cost
capacity_utilization
unit_economics_margin
premium_pricing_success_flag
yield_loss_flag
chapter11_flag
chapter7_flag
shutdown_flag
debt_burden_flag

livestock_price_change
egg_price_change
pork_price_change
chicken_price_change
feed_cost_change
soybean_price_change
disease_event_flag
avian_flu_flag
asf_flag
government_stockpile_flag
vaccine_approval_flag
conditional_license_flag
vaccine_order_value
price_fixing_investigation_flag
doj_investigation_flag

agri_disease_ai_monitoring_flag
farm_data_privacy_flag
dataset_quality_flag
farm_deployment_contract_flag

education_revenue_growth
bookings_growth
subscription_count
paid_conversion_rate
enterprise_contract_count
completion_rate
student_roi_metric
cac
churn_rate
ai_feature_cost
ai_monetization_tradeoff_flag
ai_disruption_flag
ai_search_disintermediation_flag
traffic_decline_flag
subscriber_decline_flag
layoff_flag
bankruptcy_flag
opm_model_flag
partner_concentration_flag
student_debt_risk_flag

rental_accounts
rental_churn
recurring_service_revenue_ratio
filter_service_revenue
hardware_sales_ratio
dividend_suspension_flag
replacement_demand_indicator
housing_turnover_indicator
quality_recall_flag
hardware_guidance_cut_flag
fcf_guidance_cut_flag

kiosk_installed_base
maintenance_revenue
payment_fee_revenue
retailer_retreat_flag
self_checkout_limit_flag
theft_shrink_indicator
customer_friction_flag
employee_workload_flag
local_self_checkout_regulation_flag
staffed_lane_requirement_flag
item_limit_flag
employee_per_kiosk_requirement

regulatory_approval_flag
fda_approval_flag
fda_enforcement_easing_flag
dea_rescheduling_flag
license_scope
medical_cannabis_only_flag
recreational_cannabis_benefit_flag
dea_registration_required_flag
state_federal_conflict_flag
youth_usage_risk_flag
public_health_warning_flag
legal_conflict_flag
compliance_cost
sales_channel_authorized_flag
nicotine_pouch_flag
flavor_restriction_flag
advertising_restriction_flag
who_warning_flag
influencer_marketing_risk_flag
high_nicotine_content_flag

opendart_rcept_no
opendart_detail_fetched_flag
disclosure_confidence_score
detail_parser_confidence
disclosure_signal_class
routine_disclosure_flag
risk_disclosure_flag
high_signal_disclosure_flag

score_price_alignment
price_validation_status
review_notes
```

---

# R12 Loop 6 결론

이번 6회차에서 R12는 더 좁혀졌다.

```text
Green 가능:
렌탈·관리 반복매출이 확인된 생활가전
B2B/B2G 반복계약과 FCF가 있는 성인교육·직무교육
정부 비축·반복 접종이 확인된 동물백신
규제 승인 후 판매채널·반복매출이 확인된 규제형 소비재
스마트팜 중 실제 수주·가동률·unit economics·FCF가 확인된 기업
종자·작물보호제 중 licensing/IP가 반복 EBITDA로 연결되고 소송·규제를 통과한 기업

Watch-to-Green:
자율농기계
정밀농업
종자·비료·농약
동물백신
교육·취업서비스
렌탈 생활가전
키오스크·무인화
전자담배·니코틴 대체재
의료 cannabis
농업 질병 AI 모니터링

Watch/Red:
양돈·육계·계란·사료·대두
수직농장
스마트팜 테마
비료 input cycle
키즈·유아용품
일회성 생활가전 hardware
self-checkout hardware
주정·식품 input cycle
온라인 교육 OPM
니코틴 pouch
일부 cannabis 규제 완화 테마

Hard 4C:
수직농장 폐쇄·파산
농기계 수요 둔화
right-to-repair 규제·소송
right-to-repair의 건설·임업장비 확장
종자·작물보호제 소송/규제
비료 input cost spike와 farmer margin 악화
조류독감/ASF 가격 정상화
계란 가격담합·정부조사
교육 AI 대체
AI 검색으로 인한 traffic disintermediation
AI 기능비용 증가와 bookings miss
2U식 OPM 파산
Whirlpool식 배당중단·hardware cycle 붕괴
self-checkout 축소·theft·고객불만·지자체 규제
규제형 소비재 불허가·허가범위 제한·public health backlash
니코틴 pouch youth-safety backlash
부분 cannabis rescheduling을 완전 합법화로 오분류
계약·반복매출·해지율·규제승인 detail 부족으로 인한 disclosure confidence cap
```

**R12 Loop 6 점수정규화의 핵심 문장:**

> 농업·생활서비스·기타는 “생활 필수”, “정책 수혜”, “질병 이벤트”, “AI 교육”, “무인화”, “규제 완화”라는 이름이 아니라 **반복계약, 반복매출, unit economics, 판가전가, 해지율, CAC, regulatory approval scope, public-health gate, FCF 전환, 실제 가격경로**로 봐야 한다.
> Loop 6부터는 특히 `RIGHT_TO_REPAIR_CONSTRUCTION_EXPANSION`, `AGRI_MACHINERY_DEMAND_CYCLE`, `EDTECH_AI_SEARCH_DISINTERMEDIATION`, `SELF_CHECKOUT_LOCAL_REGULATION_OVERLAY`, `NICOTINE_POUCH_YOUTH_SAFETY_OVERLAY`, `CANNABIS_PARTIAL_RESCHEDULING_LIMIT`, `DISCLOSURE_CONFIDENCE_CAP`을 강한 보정축으로 넣어야 한다.

다음 순서는 **R13 — Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리 Loop 6**다.

[1]: https://www.reuters.com/business/bayer-q1-operating-profit-up-9-crop-protection-unit-gains-2026-05-12/ "https://www.reuters.com/business/bayer-q1-operating-profit-up-9-crop-protection-unit-gains-2026-05-12/"
[2]: https://www.reuters.com/business/nutrien-expects-higher-global-potash-demand-eyes-future-its-phosphate-business-2025-11-06/ "https://www.reuters.com/business/nutrien-expects-higher-global-potash-demand-eyes-future-its-phosphate-business-2025-11-06/"
[3]: https://www.reuters.com/business/healthcare-pharmaceuticals/us-grants-conditional-clearance-zoetis-bird-flu-vaccine-poultry-2025-02-14/ "https://www.reuters.com/business/healthcare-pharmaceuticals/us-grants-conditional-clearance-zoetis-bird-flu-vaccine-poultry-2025-02-14/"
[4]: https://www.reuters.com/business/finance/duolingo-prioritizes-user-growth-over-monetization-forecasts-softer-bookings-2026-02-26/ "https://www.reuters.com/business/finance/duolingo-prioritizes-user-growth-over-monetization-forecasts-softer-bookings-2026-02-26/"
[5]: https://www.reuters.com/sustainability/boards-policy-regulation/fda-approves-juuls-tobacco-menthol-e-cigarettes-2025-07-17/ "https://www.reuters.com/sustainability/boards-policy-regulation/fda-approves-juuls-tobacco-menthol-e-cigarettes-2025-07-17/"
[6]: https://www.reuters.com/legal/litigation/cannabis-rescheduling-arrives-with-limits-what-dojs-final-order-does-doesnt-do--pracin-2026-05-12/ "https://www.reuters.com/legal/litigation/cannabis-rescheduling-arrives-with-limits-what-dojs-final-order-does-doesnt-do--pracin-2026-05-12/"
[7]: https://www.reuters.com/business/deere-reports-lower-profit-muted-farm-equipment-demand-2025-02-13/ "https://www.reuters.com/business/deere-reports-lower-profit-muted-farm-equipment-demand-2025-02-13/"
[8]: https://www.reuters.com/business/machinery-maker-cnh-cuts-full-year-profit-forecast-weak-demand-weighs-2025-11-07/ "https://www.reuters.com/business/machinery-maker-cnh-cuts-full-year-profit-forecast-weak-demand-weighs-2025-11-07/"
[9]: https://www.reuters.com/sustainability/boards-policy-regulation/deere-settles-us-right-to-repair-lawsuit-with-99-million-fund-repair-commitments-2026-04-07/ "https://www.reuters.com/sustainability/boards-policy-regulation/deere-settles-us-right-to-repair-lawsuit-with-99-million-fund-repair-commitments-2026-04-07/"
[10]: https://www.wsj.com/business/right-to-repair-advocates-are-taking-on-deere-againthis-time-in-construction-a93aa654 "https://www.wsj.com/business/right-to-repair-advocates-are-taking-on-deere-againthis-time-in-construction-a93aa654"
[11]: https://www.axios.com/2024/11/05/bowery-vertical-farming-close "https://www.axios.com/2024/11/05/bowery-vertical-farming-close"
[12]: https://apnews.com/article/62e581aca199912082c2a06b211248ab "https://apnews.com/article/62e581aca199912082c2a06b211248ab"
[13]: https://www.investopedia.com/chegg-shares-plunge-after-company-warns-that-chatgpt-is-impacting-growth-7487968 "https://www.investopedia.com/chegg-shares-plunge-after-company-warns-that-chatgpt-is-impacting-growth-7487968"
[14]: https://www.sfchronicle.com/tech/article/chegg-layoffs-ai-bay-area-21124921.php "https://www.sfchronicle.com/tech/article/chegg-layoffs-ai-bay-area-21124921.php"
[15]: https://www.wsj.com/business/2u-ed-tech-company-files-chapter-11-bankruptcy-24ca1017 "https://www.wsj.com/business/2u-ed-tech-company-files-chapter-11-bankruptcy-24ca1017"
[16]: https://www.barrons.com/articles/whirlpool-stock-falling-outlook-8d0bd413 "https://www.barrons.com/articles/whirlpool-stock-falling-outlook-8d0bd413"
[17]: https://www.axios.com/2024/03/14/self-checkout-target-express-lanes-limit-change "https://www.axios.com/2024/03/14/self-checkout-target-express-lanes-limit-change"
[18]: https://www.the-sun.com/money/16343669/target-self-checkout-limits-santa-ana-california/ "https://www.the-sun.com/money/16343669/target-self-checkout-limits-santa-ana-california/"
[19]: https://www.reuters.com/legal/litigation/who-warns-loosely-regulated-nicotine-pouches-risk-youth-addiction-2026-05-15/ "https://www.reuters.com/legal/litigation/who-warns-loosely-regulated-nicotine-pouches-risk-youth-addiction-2026-05-15/"

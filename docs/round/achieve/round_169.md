좋아. **R11 Loop 10까지 끝났으니, 이번은 R12 Loop 10 — 농업·생활서비스·기타**다.

R12는 양돈·육계·사료·대두, 농기계, 종자·비료·농약, 스마트팜, 원양어업, 교육·취업, 키즈·유아용품, 전자담배, 주정, 생활가전, 키오스크·셀프체크아웃 같은 잡다하지만 테마성이 강한 영역을 흡수한다. 이 구간은 대부분 Watch/Red이고, 실제 수주·반복계약·판가전가·규제 승인·FCF 전환 전까지 Green을 제한해야 한다.

서생원식으로 보면 R12의 질문은 “생활필수라서 좋다”, “농업이라 안정적이다”, “AI 교육이라 성장한다”가 아니다. 핵심은 **EPS/FCF 체급 변화가 실제로 생기고, 시장이 아직 그 변화를 과소평가하는가**다. 질병·곡물·규제·AI 교육·스마트팜·무인화 같은 뉴스는 Stage 1을 만들 수 있지만, 반복매출·unit economics·판가전가·해지율·CAC·규제승인 범위·FCF가 확인돼야 Stage 3다.

공시·데이터 작업에서도 계약금액, 수주기간, 규제 승인, 해지율, recurring revenue, 사료비, 판가전가, 질병 이벤트, 희석률, OP YoY 같은 detail을 실제 확인해야 한다. 값이 없으면 만들면 안 되고, routine disclosure나 단순 이벤트만으로 cheap-scan positive를 만들면 안 된다.

---

# R12 Loop 10. 농업·생활서비스·기타

## 1. 이번 라운드 대섹터

```text
R12 = 농업·생활서비스·기타

Loop 10 목표 =
농기계 cycle / right-to-repair /
종자·작물보호제 IP / 비료 input cycle /
동물백신·질병 stockpile /
축산 가격 cycle / 스마트팜 unit economics /
AI 교육 disruption / edtech monetization trade-off /
생활가전 hardware cycle /
키오스크·셀프체크아웃 규제 /
니코틴 pouch youth-safety /
cannabis partial rescheduling을

stage 포착
+ 실제 가격경로
+ 점수비중 정규화로 재분류
```

이번 R12 Loop 10의 핵심 질문은 이거다.

```text
이 기업은 반복계약·반복매출·판가전가·규제승인·FCF가 있는가?

아니면 질병, 날씨, 곡물가격, AI 교육, 무인화,
규제완화 뉴스로만 움직이는가?
```

R12 stage는 이렇게 잡는다.

```text
Stage 1:
질병 뉴스, 곡물·계란·육계 가격 급등,
스마트팜·AI 교육·무인화·규제완화·농기계 자율화 뉴스

Stage 2:
실제 수주, 정부계약, 조건부 승인, licensing revenue,
B2B/B2G 계약, bookings, recurring service, 규제 승인 확인

Stage 3:
반복매출, unit economics, 판가전가, OPM/FCF,
해지율·CAC 안정, 규제·public health gate 통과,
실제 가격경로 동행

Stage 4B:
스마트팜, AI 교육, 조류독감, 비료, 니코틴 대체재,
cannabis 규제완화가 모두에게 알려져 가격이 먼저 간 구간

Stage 4C:
농기계 수요 둔화, right-to-repair 소송,
수직농장 폐쇄, AI가 교육서비스 대체,
bookings miss, hardware cycle 붕괴,
self-checkout 규제, youth-safety backlash
```

R12 Loop 10에서 가장 중요한 분리는 이거다.

```text
질병 수혜
≠ 구조적 이익

농기계 자동화
≠ 농기계 cycle 탈피

스마트팜 기술
≠ unit economics

AI 교육 기능
≠ 유료전환·bookings

전자담배·니코틴 대체재
≠ public health risk 면제

cannabis rescheduling
≠ 완전 합법화

셀프체크아웃 설치
≠ 자동화 ROI
```

---

## 2. 대상 canonical archetype

| canonical archetype                      | Loop 10 판정 방향   | stage 포착 핵심                                                 |
| ---------------------------------------- | --------------- | ----------------------------------------------------------- |
| `SMART_FARM_AGRI_TECH`                   | Watch-to-Green  | 실제 수주, 운영계약, 가동률, unit economics                            |
| `VERTICAL_FARMING_UNIT_ECONOMICS`        | Watch/Red       | 에너지비, CAPEX, premium pricing, shutdown                      |
| `AGRI_MACHINERY_PRECISION_CYCLE`         | Watch           | 자율농기계보다 농가소득·금리·장비 cycle                                    |
| `AGRI_MACHINERY_DEMAND_CYCLE`            | Watch/Red       | crop price, farmer margin, dealer inventory, production cut |
| `AGRI_MACHINERY_SOFTWARE_LOCKIN`         | Watch           | software attach는 좋지만 right-to-repair 감시                     |
| `RIGHT_TO_REPAIR_REGULATORY_OVERLAY`     | hard gate       | 수리독점, FTC, settlement, 고객반발                                 |
| `RIGHT_TO_REPAIR_CONSTRUCTION_EXPANSION` | RedTeam overlay | 농기계에서 건설·임업장비로 소송 확장                                        |
| `AGRI_INPUT_SEED_CROP_PROTECTION`        | Watch-to-Green  | seed licensing, crop protection EBITDA, litigation          |
| `FERTILIZER_INPUT_COST_CYCLE`            | Watch           | potash/phosphate/nitrogen, crop price, farmer margin        |
| `FERTILIZER_STRATEGIC_PHOSPHATE_OPTION`  | Watch           | 전략광물·사업재편 가능성, volume/FCF 필요                                |
| `FERTILIZER_INPUT_COST_SULFURIC_ACID`    | RedTeam overlay | phosphate 가격보다 sulfuric acid·sulfur 비용                      |
| `AGRI_LIVESTOCK_FOOD_COMMODITY`          | Watch/Red       | 질병·사료비·가격 cycle                                             |
| `LIVESTOCK_DISEASE_PRICE_REGULATORY`     | hard gate       | 조류독감·계란값 급등 후 가격조사·담합 리스크                                   |
| `ANIMAL_HEALTH_BIOSECURITY`              | Watch-to-Green  | 조건부 승인, 정부 비축, 반복 접종 가능성                                    |
| `AGRI_DISEASE_AI_MONITORING`             | Watch           | 데이터품질, farm privacy, 실제 농장계약                                |
| `EDUCATION_SPECIALTY_SERVICES`           | Watch-to-Green  | 반복수강, B2B/B2G 계약, CAC, completion rate                      |
| `EDTECH_AI_MONETIZATION_TRADEOFF`        | Watch           | AI 기능 확대와 bookings/margin trade-off                         |
| `EDTECH_AI_DISRUPTION`                   | hard gate       | Chegg식 AI 대체, subscriber/traffic decline                    |
| `EDTECH_AI_SEARCH_DISINTERMEDIATION`     | hard gate       | Google AI Overviews, 검색트래픽 감소                               |
| `ONLINE_EDUCATION_OPM_DISTRESS`          | Watch/Red       | 부채, student ROI, partner concentration, Chapter 11          |
| `HOME_LIVING_APPLIANCE_RENTAL`           | Watch-to-Green  | 렌탈 계정, 해지율, 관리서비스 반복매출                                      |
| `HOME_APPLIANCE_HARDWARE_CYCLE`          | Watch/Red       | 교체수요, 주택경기, 배당·FCF                                          |
| `SERVICE_KIOSK_SELF_CHECKOUT`            | Watch/Red       | 설치대수보다 유지보수·결제수수료·regulation                                |
| `SELF_CHECKOUT_LOCAL_REGULATION_OVERLAY` | hard gate       | item limit, 직원 배치, staffed lane 의무                          |
| `CONSUMER_REGULATED_PRODUCT`             | Watch-to-Green  | FDA/DEA 승인, 허가 범위, 반복소비                                     |
| `NICOTINE_ALTERNATIVE_REGULATED`         | Watch/Red       | public health, youth usage, flavor restriction              |
| `NICOTINE_POUCH_YOUTH_SAFETY_OVERLAY`    | hard gate       | youth addiction, high nicotine, influencer marketing        |
| `CANNABIS_REGULATED_PRODUCT`             | Watch           | rescheduling과 실제 합법화·매출 분리                                  |
| `CANNABIS_PARTIAL_RESCHEDULING_LIMIT`    | RedTeam overlay | Schedule III 일부 전환은 federal legalization 아님                 |
| `DISCLOSURE_CONFIDENCE_CAP`              | 공통 cap          | 계약·해지율·규제승인 detail 부족 시 Stage 3 제한                          |

---

## 3. deep sub-archetype

```text
AGRI_MACHINERY_DEMAND_CYCLE
- Deere
- CNH Industrial
- Case IH / New Holland
- tractors / combines
- crop price
- farm income
- farmer financing cost
- dealer inventory
- production cut
- tariff exposure
- equipment rental instead of purchase

RIGHT_TO_REPAIR_REGULATORY_OVERLAY
- Deere right-to-repair
- repair software
- dealer network
- authorized service monopoly
- FTC lawsuit
- class-action settlement
- digital repair tools
- independent repair access

RIGHT_TO_REPAIR_CONSTRUCTION_EXPANSION
- Deere construction equipment
- forestry equipment
- landscaping contractor
- independent repair shops
- class-action expansion
- dealer-level diagnostics

AGRI_INPUT_SEED_CROP_PROTECTION
- Bayer Crop Science
- soy seed licensing
- Corteva dispute resolution
- seed traits
- crop protection
- Roundup litigation
- farmer ROI
- patent / licensing

FERTILIZER_INPUT_COST_CYCLE
- Nutrien
- Mosaic
- potash
- phosphate
- nitrogen
- sulfuric acid
- crop nutrient depletion
- farmer margin
- strategic phosphate
- supply story
- asset review / partnership / sale

ANIMAL_HEALTH_BIOSECURITY
- Zoetis
- HPAI / bird flu
- poultry vaccine
- USDA conditional license
- vaccine stockpile
- emergency use
- commercial flock vaccination policy

VERTICAL_FARMING_UNIT_ECONOMICS
- Bowery
- AeroFarms
- AppHarvest
- indoor farm
- leafy greens
- energy cost
- premium pricing
- yield loss
- debt
- shutdown

EDTECH_AI_MONETIZATION_TRADEOFF
- Duolingo
- AI speaking features
- Duolingo Max
- user growth vs monetization
- bookings
- adjusted EBITDA margin
- AI feature cost
- paid subscriber conversion

EDTECH_AI_DISRUPTION
- Chegg
- ChatGPT
- homework help
- AI Overviews
- traffic decline
- subscriber decline
- revenue guide miss
- layoffs
- strategic review

ONLINE_EDUCATION_OPM_DISTRESS
- 2U
- edX
- online program management
- high leverage
- Chapter 11
- student ROI
- partner concentration
- regulatory changes

SERVICE_KIOSK_SELF_CHECKOUT
- Target
- Walmart
- Santa Ana
- Long Beach
- self-checkout item limit
- staffed lane
- employee per kiosk
- shrink / theft
- customer friction

CONSUMER_REGULATED_PRODUCT
- Juul
- FDA marketing authorization
- tobacco / menthol pods
- nicotine pouch
- WHO youth addiction warning
- cannabis Schedule III
- DEA registration
- state/federal conflict
```

---

## 4. 성공사례

### 4-1. Bayer Crop Science — seed licensing/IP가 EBITDA와 가격경로로 연결된 Stage 2 사례

Bayer는 R12에서 가장 깔끔한 `AGRI_INPUT_SEED_CROP_PROTECTION` Stage 2 사례다. 2026년 1분기 adjusted EBITDA는 9% 증가한 44.5억 유로로 시장 예상 39.3억 유로를 웃돌았고, Corteva와의 soy seed licensing dispute 해결 효과로 Crop Science EBITDA가 17.9% 증가해 30억 유로가 됐다. 이 성과는 Xarelto·Eylea 특허 만료에 따른 약품 부문 압박을 상쇄했다. ([Reuters][1])

가격경로도 맞았다. Bayer 주가는 실적 발표 후 장중 최대 6.9% 상승했다. 즉 단순 “농업 테마”가 아니라 **seed/IP/licensing → EBITDA beat → 주가 반응**이 연결된 사례다. ([월스트리트저널][2])

```text
case_type:
AGRI_INPUT_LICENSED_IP_SUCCESS_STAGE2

stage 포착:
Stage 1 = 식량안보·종자·작물보호제 narrative
Stage 2 = soy seed licensing dispute resolution + Crop Science EBITDA +17.9%
Stage 3 = 반복 licensing revenue, litigation 비용 통제, FCF 확인 필요
Stage 4C-watch = Roundup litigation, 규제·특허 리스크
```

**가격경로 판정**

```text
Stage 2 포착이 가격경로와 잘 맞았다.
Bayer는 R12에서 “농업 input도 IP/licensing이면 구조 후보가 될 수 있다”는 기준사례다.
```

**정규화 결론**

```text
AGRI_INPUT_SEED_CROP_PROTECTION 점수 상향.

비료·농약·종자는 한 덩어리가 아니다.

Seed/IP/licensing:
Visibility 가점 가능

Crop protection:
litigation·regulation 감점

Fertilizer:
input cycle과 farmer margin을 먼저 본다
```

---

### 4-2. Nutrien potash / phosphate — 수요·전략광물 option은 있지만 아직 cycle/Watch

Nutrien은 2026년 global potash demand가 4년 연속 증가할 수 있다고 봤다. 2025년 큰 작황이 토양 영양분을 소모해 potash 수요를 지지한다는 설명이고, phosphate 사업은 높은 북미 가격, 전략광물 지정 가능성, 사업 재편·파트너십·매각 option이 붙어 있다. 다만 이건 Green이라기보다 **비료 가격·작물가격·농가마진·supply discipline이 함께 움직이는 cycle/Watch**다. ([Reuters][3])

반대로 Mosaic은 sulfuric acid·sulfur 같은 input cost shock 때문에 phosphate production guidance를 철회하고 CAPEX를 줄였으며, 2026년 1분기 손실을 냈다. 이는 비료 가격이 오르더라도 input cost가 더 세게 오르면 마진이 깨질 수 있다는 R12/R4 공통 RedTeam이다. ([월스트리트저널][4])

```text
case_type:
FERTILIZER_POTASH_DEMAND_CYCLE_WATCH
+
FERTILIZER_STRATEGIC_PHOSPHATE_OPTION
+
FERTILIZER_INPUT_COST_REDTEAM

stage 포착:
Stage 1 = 식량안보·비료수요·토양영양분 depletion
Stage 2 = potash demand outlook, phosphate strategic option
Stage 3 = volume + price + farmer margin + FCF 확인 필요
Stage 4C-watch = crop price 하락, input cost spike, farmer demand deferral
```

**정규화 결론**

```text
FERTILIZER_INPUT_COST_CYCLE은 Stage 3-Green 제한.

potash 수요와 phosphate option은 가점이지만,
farmer margin과 crop price,
그리고 sulfuric acid / ammonia / energy input cost가 나쁘면 바로 cap.
```

---

### 4-3. Zoetis bird flu vaccine — 질병 이벤트가 animal health Stage 2로 올라가는 조건

Zoetis는 USDA로부터 poultry bird flu vaccine 조건부 승인을 받았다. USDA conditional license는 emergency나 special circumstance에서 safety와 reasonable expectation of efficacy를 근거로 부여되는 구조이고, USDA가 상업·야생 조류에 유행하는 strain에 맞춘 poultry vaccine stockpile을 재구축하려 한다는 점도 보도됐다. ([Reuters][5])

```text
case_type:
ANIMAL_HEALTH_BIOSECURITY_STAGE1_2

stage 포착:
Stage 1 = 조류독감 outbreak, biosecurity demand
Stage 2 후보 = USDA conditional license, vaccine stockpile 가능성
Stage 3 = 실제 정부 주문, 반복 접종, 매출·OPM 확인 필요
Stage 4C-watch = outbreak 정상화, 백신 미사용, 무역 제한 우려
```

**가격경로 판정**

```text
질병 뉴스만이면 Event/Watch.
조건부 승인과 정부 비축 가능성이 붙으면 Stage 2 후보로 격상한다.
```

**정규화 결론**

```text
ANIMAL_HEALTH_BIOSECURITY 점수 상향.
단, Stage 3 조건은 실제 order와 반복 접종이다.
```

---

### 4-4. Juul FDA authorization — 규제형 소비재는 허가 범위가 Stage 2를 만든다

Juul은 2025년 7월 FDA로부터 device와 tobacco·menthol flavor refill cartridge 판매 승인을 받았다. 이는 2022년 federal ban 이후 큰 반전이며, FDA가 Juul의 자료를 검토한 뒤 해당 제품의 marketing authorization이 public health 기준에 적합하다고 판단한 사례다. ([Reuters][6])

다만 AP 보도 기준으로도 이 결정은 Juul 제품이 “safe”라는 뜻이 아니고, tobacco·menthol 제품에 한정되며, youth vaping 리스크 때문에 public health 논쟁이 계속된다. 즉 규제 승인 자체는 Stage 2 evidence지만, youth exposure·marketing restriction·허가 범위가 Stage 3 gate가 된다. ([AP News][7])

```text
case_type:
REGULATED_CONSUMER_APPROVAL_STAGE2

stage 포착:
Stage 1 = 전자담배 규제완화 기대
Stage 2 = FDA authorization, 허가 제품·향 범위 확인
Stage 3 = 판매채널, 반복매출, public health gate 통과 필요
Stage 4C-watch = youth usage, marketing restriction, flavor regulation
```

**정규화 결론**

```text
CONSUMER_REGULATED_PRODUCT는 승인 전 Watch/Red.
승인 후에도 허가 범위·판매채널·청소년 사용·반복매출을 확인해야 한다.
```

---

### 4-5. Cannabis partial rescheduling — 규제완화 Stage 1~2이지만 완전 합법화는 아님

2026년 4월 DOJ와 DEA는 일부 cannabis-related substances를 Schedule I에서 Schedule III로 재분류했다. 이 조치는 FDA-approved cannabis products와 state-licensed medical cannabis 중심의 제한적 조치이며, 연방 차원의 완전 합법화나 recreational cannabis 전체 수혜가 아니다. 의료 cannabis 사업자에는 280E 세금 부담 완화 같은 효과가 있을 수 있지만, DEA registration, state/federal conflict, 법적 도전 가능성이 남아 있다. ([Reuters][8])

```text
case_type:
CANNABIS_PARTIAL_RESCHEDULING_STAGE1_2_WATCH

stage 포착:
Stage 1 = cannabis rescheduling 기대
Stage 2 = 일부 Schedule III 전환, medical cannabis 중심
Stage 3 = 실제 license, tax effect, sales channel, FCF 확인 필요
Stage 4C-watch = federal legalization 아님, legal challenge, DEA registration
```

**정규화 결론**

```text
CANNABIS_REGULATED_PRODUCT는 Stage 1~2.
Stage 3는 실제 매출·세금효과·compliance cost·FCF 확인 후.
```

---

### 4-6. Duolingo — AI 교육이 성공하려면 bookings·유료전환·margin이 같이 가야 한다

Duolingo는 R12에서 양면 기준사례다. 좋은 쪽에서는 2025년 2분기에 매출이 41% 증가한 2.523억 달러, bookings도 41% 증가했고, paid subscribers가 37% 증가해 1,090만 명에 도달했다. 이 발표 뒤 주가는 35% 급등했다. ([Investopedia][9])

하지만 이후 2025년 3분기에는 revenue beat와 annual revenue forecast 상향에도 불구하고, 4분기 bookings 전망이 시장 예상보다 낮아 after-hours에서 20% 하락했다. 회사는 monetization보다 teaching quality 개선을 우선한다고 설명했고, AI 기능은 수익성 있는 서비스라고 했지만, 시장은 결국 bookings와 monetization을 봤다. ([Reuters][10])

```text
case_type:
EDTECH_AI_MONETIZATION_TRADEOFF

좋은 stage:
Stage 2 = paid subscriber growth + bookings growth + AI-enhanced service
가격경로 = strong bookings 때 +35%

나쁜 stage:
Stage 4C-watch = bookings miss, monetization 후퇴, margin/AI cost 압박
가격경로 = soft bookings 때 -20%

가격경로 판정:
Duolingo는 R12에서 양면 기준사례다.
AI 기능이 좋아도 bookings·paid conversion·margin이 동행하지 않으면 Stage 3 실패.
```

**정규화 결론**

```text
EDTECH_AI_MONETIZATION_TRADEOFF에서 AI 기능은 Stage 1~2.
Stage 3는 다음이 같이 유지될 때만 가능하다.

bookings
paid conversion
gross margin
adjusted EBITDA margin
retention
FCF
```

---

## 5. 반례

### 5-1. CNH / Deere — 자율농기계 기술보다 농가 capex cycle이 먼저다

CNH Industrial은 2025년 full-year profit forecast를 낮췄고, 약한 수요와 생산축소가 margin을 압박했다. 낮은 crop price와 높은 생산비 때문에 농가가 고가 장비 구매를 미루고, dealers가 높은 inventory를 안고 있다는 점이 핵심이다. 발표 후 CNH 주가는 7.1% 하락했다. ([Reuters][11])

```text
case_type:
AGRI_MACHINERY_DEMAND_CYCLE_4C_WATCH

stage 포착:
Stage 1 = 자율농기계·정밀농업·농업 자동화 narrative
Stage 2 = 장비 판매·dealer inventory 정상화
Stage 4C = crop price 약세, farmer margin 압박, dealer inventory, profit forecast cut
가격경로 = CNH -7.1%
```

**가격경로 판정**

```text
농기계 demand-cycle RedTeam이 실제 주가하락과 맞았다.
```

**정규화 결론**

```text
AGRI_MACHINERY_PRECISION_CYCLE에서 기술 narrative만으로 Green 금지.

필수:
farm_income
crop_price
financing_cost
dealer_inventory
production_cut
```

---

### 5-2. Deere right-to-repair — software lock-in은 규제·소송으로 깨질 수 있다

Deere는 농업장비 right-to-repair class action에서 9,900만 달러 settlement fund와 10년간 digital repair tools 제공을 약속했다. 별도로 FTC 소송도 받고 있으며, FTC는 Deere가 authorized dealer network와 repair tool access 제한으로 수리비를 높인다고 주장한다. ([Reuters][12])

이 리스크는 농업장비에 그치지 않는다. 최근 right-to-repair advocates는 Deere의 construction·forestry equipment로 소송 범위를 넓혔다. 새 소송은 diagnostic·repair software 접근 제한이 independent repair를 막고 repair cost를 높인다는 구조로 제기됐다. ([월스트리트저널][13])

```text
case_type:
AGRI_MACHINERY_SOFTWARE_LOCKIN_REGULATORY_4C_WATCH
+
RIGHT_TO_REPAIR_CONSTRUCTION_EXPANSION

stage 포착:
Stage 1 = connected machine / software lock-in / dealer network moat
Stage 2 = software attach, service revenue
Stage 4C-watch = $99m settlement, FTC lawsuit, construction equipment lawsuit
```

**가격경로 판정**

```text
소프트웨어 lock-in을 고마진 moat로만 보면 false-positive.
규제·소송이 반복매출 quality를 깎는다.
```

**정규화 결론**

```text
RIGHT_TO_REPAIR_REGULATORY_OVERLAY를 hard gate로 유지.
농기계뿐 아니라 건설·임업장비에도 확장 적용한다.
```

---

### 5-3. Bowery shutdown — 수직농장은 unit economics를 못 맞추면 hard 4C

Bowery는 7억 달러 이상을 조달한 vertical farming unicorn이었지만 2024년 폐쇄됐다. Bowery는 AeroFarms, AppHarvest 같은 실패 사례를 뒤따랐고, 소비자가 “cleaner produce”에 충분한 premium을 지불하지 않았다는 점이 핵심 원인으로 지적됐다. 수직농장은 기술적으로 좋아 보여도 전력비·CAPEX·가격 프리미엄·수율·수요가 맞지 않으면 hard 4C로 간다. ([Axios][14])

```text
case_type:
VERTICAL_FARMING_UNIT_ECONOMICS_4C

stage 포착:
Stage 1 = 스마트팜·AI 농업·수직농장 narrative
Stage 2 = 설비 확장·고객 입점
Stage 4C = shutdown, premium pricing failure, CAPEX/debt burden
```

**가격경로 판정**

```text
비상장 사례지만 smart farm 테마의 unit economics cap으로 강하게 반영.
```

**정규화 결론**

```text
SMART_FARM_AGRI_TECH와 VERTICAL_FARMING_UNIT_ECONOMICS를 분리한다.

온실 자동화·정밀농업 운영계약:
Watch-to-Green 가능

수직농장 leafy greens:
unit economics 통과 전 Watch/Red
```

---

### 5-4. Cal-Maine — 질병 수혜와 정부조사가 동시에 붙는 축산 cycle

Cal-Maine은 조류독감에 따른 record egg price 속에서 DOJ antitrust division의 가격조사 대상이 됐다. Cal-Maine의 3분기 매출은 계란가격 급등 덕분에 전년 대비 거의 두 배인 14.2억 달러였지만, EPS 10.38달러가 기대치를 밑돌았고, 조사 뉴스 이후 주가가 after-hours에서 4% 넘게 하락했다. ([AP News][15])

이후 DOJ의 더 큰 antitrust action 가능성 보도로 Cal-Maine 주가가 after-hours에서 3.7% 추가 하락했다는 보도도 나왔다. 질병·공급차질로 EPS가 튀어도, 가격조사·담합 리스크가 붙으면 구조적 Green이 아니라 cyclical success + regulatory watch로 분류해야 한다. ([마켓워치][16])

```text
case_type:
LIVESTOCK_CYCLICAL_SUCCESS_PLUS_REGULATORY_WATCH

stage 포착:
Stage 1 = 조류독감·공급차질·계란값 급등
Stage 2 = 매출 급증, EPS 상승
Stage 4C-watch = DOJ investigation, 가격 정상화, 소비자 반발
가격경로 = after-hours -4% 이상 / 추가 antitrust 우려
```

**가격경로 판정**

```text
축산 가격 cycle은 EPS가 폭발해도 structural Green으로 분류하면 안 된다.
```

**정규화 결론**

```text
AGRI_LIVESTOCK_FOOD_COMMODITY는 대부분 cyclical_success.

질병·가격 급등 후
price_investigation_flag
antitrust_probe_flag
price_normalization_flag

가 켜지면 Stage 3-Green 차단.
```

---

### 5-5. Chegg / 2U — AI 대체와 OPM 부채모델 붕괴

Chegg는 ChatGPT가 신규 고객 성장에 영향을 주고 있다고 인정한 뒤 주가가 거의 50% 급락했다. 회사의 현 분기 매출 가이던스는 시장 예상보다 약 10% 낮았고, subscription revenue도 전년 대비 감소할 것으로 예상됐다. 이는 AI가 교육서비스의 핵심 기능을 직접 대체한 hard 4C다. ([Investopedia][17])

2U는 온라인 교육·OPM 모델의 대표 반례다. 2U는 Chapter 11을 신청했고, 9.45억 달러 debt를 약 4.59억 달러로 줄이는 구조조정을 추진했다. 2018년 50억 달러 이상이던 market value는 약 1,150만 달러로 추락했다. ([월스트리트저널][18])

```text
case_type:
EDTECH_AI_DISRUPTION_HARD_4C
+
ONLINE_EDUCATION_OPM_DISTRESS_HARD_4C

stage 포착:
Stage 1 = 온라인 교육·AI 교육·re-skilling narrative
Stage 2 = subscriber / B2B / OPM contracts
Stage 4C = AI core-service substitution, traffic decline, debt burden, Chapter 11
```

**가격경로 판정**

```text
Chegg는 AI 대체로 즉시 price-path가 깨진 사례.
2U는 OPM 부채모델이 장기적으로 무너진 사례.
```

**정규화 결론**

```text
EDUCATION_SPECIALTY_SERVICES는 반복계약·completion rate·student ROI가 필요.
AI가 핵심 서비스를 대체하면 바로 4C.
```

---

### 5-6. Whirlpool — 생활가전 hardware cycle은 렌탈 반복매출과 완전히 다르다

Whirlpool은 2026년 1분기 실적 부진 이후 배당을 중단했고, 2026년 adjusted EPS 전망을 기존 7달러에서 3~3.50달러로 낮췄다. Reuters 기준 주가는 14년 저점으로 급락했고, 회사는 높은 금리, 주택거래 둔화, 인플레이션, 에너지 가격 부담, 소비심리 악화, 할인경쟁을 핵심 압박으로 제시했다. ([Reuters][19])

Barron’s도 Whirlpool이 52주 신저가를 기록했고, 2021년 고점 대비 83.8% 하락한 상태라고 보도했다. 즉 생활가전은 “생활필수”가 아니라 hardware replacement cycle에 묶인다. ([Barron's][20])

```text
case_type:
HOME_APPLIANCE_HARDWARE_CYCLE_4C

stage 포착:
Stage 1 = 생활가전 교체수요·주택경기 회복 기대
Stage 4C = dividend suspension, EPS guide cut, FCF guide cut, long-term price collapse
```

**가격경로 판정**

```text
hardware cycle RedTeam이 실제 가격경로와 매우 잘 맞았다.
```

**정규화 결론**

```text
HOME_LIVING_APPLIANCE_RENTAL:
렌탈 계정 + 해지율 + 관리서비스 반복매출이 있으면 Watch-to-Green

HOME_APPLIANCE_HARDWARE_CYCLE:
교체수요·주택경기에 묶이면 Watch/Red
```

---

### 5-7. 셀프체크아웃 — 설치대수보다 theft·고객불만·지자체 규제

Santa Ana는 2026년 6월부터 food/drug retailer에 self-checkout 15개 품목 제한, staffed checkout lane 유지, self-checkout 3대당 직원 1명 모니터링을 요구하는 ordinance를 시행한다. 이 조례는 Long Beach의 2025년 유사 규제와 닮아 있고, Target은 이미 10개 품목 제한을 테스트한 바 있다. ([The Sun][21])

Long Beach도 shoplifting 대응을 이유로 self-checkout lane에 직원 모니터링과 15개 품목 제한을 요구하는 규제를 도입했다. 이건 셀프체크아웃 설치대수가 늘어도, shrink·노동규제·지자체 규제가 unit economics를 깎을 수 있음을 보여준다. ([뉴욕 포스트][22])

```text
case_type:
SELF_CHECKOUT_LOCAL_REGULATION_4C_WATCH

stage 포착:
Stage 1 = 인건비 상승·무인화·키오스크 narrative
Stage 2 = 설치대수 증가
Stage 4C-watch = item limit, staffed lane, employee monitoring, local ordinance
```

**가격경로 판정**

```text
단일 종목 price-path보다 unit economics gate로 적용.
설치대수만 보면 false-positive.
```

**정규화 결론**

```text
SERVICE_KIOSK_SELF_CHECKOUT은 hardware one-off를 낮게 본다.

Stage 3는:
maintenance revenue
payment fee
shrink 감소
retailer retention
regulatory compliance

가 필요하다.
```

---

### 5-8. Nicotine pouch youth-safety — 반복소비라도 public health gate를 통과해야 한다

WHO는 2026년 5월 nicotine pouch 규제가 느슨하면 youth addiction을 키울 수 있다고 경고했다. WHO는 social media influencer, lifestyle branding, youth-oriented event sponsorship, flavor·packaging, 높은 니코틴 함량을 핵심 리스크로 봤고, 니코틴 함량 제한, 광고 제한, flavor restriction을 권고했다. ([Reuters][23])

```text
case_type:
NICOTINE_POUCH_YOUTH_SAFETY_4C_WATCH

stage 포착:
Stage 1 = nicotine alternative, 반복소비, cigarette substitution narrative
Stage 2 = 판매채널·점유율 확대
Stage 4C-watch = youth addiction, flavor restriction, public health warning
```

**가격경로 판정**

```text
반복소비가 있어도 public health gate를 통과해야 한다.
```

**정규화 결론**

```text
NICOTINE_ALTERNATIVE_REGULATED는 Green 가능성이 제한적.
허가·판매채널보다 youth-safety와 advertising restriction을 먼저 본다.
```

---

## 6. 지금 점수표로 실제 stage를 어떻게 포착했고, 주가 상승·하락과 맞았는지를 통한 점수비중정규화

R12 Loop 10부터 기본 점수표는 이렇게 재정규화한다.

```text
R12 v10 기본 점수표 = 100점

1. EPS/FCF·OPM 전환 가능성                 22점

2. 반복계약·반복매출·규제승인 visibility     20점
   - government order
   - recurring service
   - licensing revenue
   - FDA/USDA/DEA authorization

3. unit economics·판가전가·수요 지속성        18점
   - farm income
   - CAC
   - churn
   - energy cost
   - premium pricing
   - farmer margin

4. 규제·소송·public health·disclosure          16점

5. capital discipline / debt / cash runway     10점

6. 시장 오해·리레이팅 gap                    8점

7. valuation room / 4B 여지                   6점

Hard RedTeam:
farm equipment demand collapse, right-to-repair, vertical farming shutdown,
livestock price investigation, AI education disruption, bookings miss,
OPM bankruptcy, hardware dividend suspension, self-checkout local regulation,
youth-safety warning, partial rescheduling 오분류
```

### 6-1. stage별 점수 cap

```text
Stage 1 cap:
최대 45점

조건:
- 조류독감·ASF·계란값 뉴스
- 스마트팜·수직농장 narrative
- 자율농기계 발표
- AI 교육 기능 출시
- 무인화·키오스크 설치 확대
- 전자담배·니코틴 pouch·cannabis 규제 뉴스

예:
질병 수혜주
AI 교육 관련주
스마트팜 테마주
니코틴 대체재 테마
```

```text
Stage 2 cap:
최대 70점

조건:
- licensing revenue
- 정부 조건부 승인
- 규제 승인
- bookings/revenue guidance
- 반복서비스 계정
- 수주·운영계약
- 실제 가격반응 확인

예:
Bayer soy seed licensing
Zoetis USDA conditional license
Juul FDA authorization
Cannabis partial rescheduling
Duolingo bookings growth
```

```text
Stage 3:
70점 이상 가능

조건:
- 반복계약·반복매출
- unit economics 확인
- 판가전가
- CAC·churn 안정
- OPM/FCF 개선
- public health·regulatory gate 통과
- 실제 가격경로 동행

이번 R12 Loop 10에서도 확정 Stage 3 후보는 제한적.
Bayer는 Stage 2→3 후보이나 litigation/FCF 확인 필요.
```

```text
Stage 4B:
점수는 높지만 기대수익률 감점

조건:
- 조류독감·AI교육·스마트팜·규제완화·니코틴 대체재 테마가 모두에게 알려짐
- 실계약보다 가격이 먼저 감
- unit economics가 검증되기 전 valuation 확장

예:
수직농장 unicorn hype
AI education app hype
질병 수혜주 가격 급등
```

```text
Stage 4C:
hard RedTeam

조건:
- 농기계 forecast cut
- right-to-repair settlement/lawsuit
- 수직농장 shutdown
- DOJ price investigation
- bookings miss
- AI가 core service 대체
- Chapter 11
- dividend suspension
- self-checkout regulation
- youth-safety warning
```

---

### 6-2. 실제 가격경로와 맞은 case / 안 맞은 case

| case                              |   점수표가 잡은 stage |                                   실제 가격경로 확인 | 판정                                    | 정규화 조정                              |
| --------------------------------- | --------------: | -------------------------------------------: | ------------------------------------- | ----------------------------------- |
| Bayer Crop Science                |    Stage 2→3 후보 |                           shares up to +6.9% | seed licensing stage 잘 맞음             | IP/licensing 가중치 상향                 |
| Nutrien potash/phosphate          | Stage 1~2 Watch |                   demand/strategic option 확인 | cycle 분류 유지                           | farmer margin gate 유지               |
| Mosaic fertilizer input shock     |        4C-watch |          loss, phosphate guidance withdrawal | input cost RedTeam                    | sulfuric acid/input cost 강화         |
| Zoetis bird flu vaccine           |       Stage 1~2 |                          조건부 승인·stockpile 후보 | government order 전 Stage 3 제한         | biosecurity visibility 상향           |
| CNH weak demand                   |        4C-watch |                                     주가 -7.1% | 농기계 cycle RedTeam 잘 맞음                | farm income/dealer inventory 가중치 상향 |
| Deere right-to-repair             |        4C-watch |                   $99m settlement + FTC suit | software lock-in gate 강화              | right-to-repair hard overlay        |
| Deere construction repair lawsuit |        4C-watch |                                        소송 확장 | R1/R10 장비에도 확장                        | construction expansion overlay 추가   |
| Bowery shutdown                   |         hard 4C |                                 비상장 shutdown | vertical farm unit economics hard cap | 스마트팜/수직농장 분리                        |
| Cal-Maine                         |        4C-watch |                           after-hours -4% 이상 | 질병 수혜+규제 RedTeam 잘 맞음                 | livestock regulatory gate 강화        |
| Duolingo                          |           양면 사례 | strong bookings에는 +35%, soft bookings에는 -20% | AI 기능보다 bookings가 핵심                  | bookings/margin 가중치 상향              |
| Chegg                             |         hard 4C |                      ChatGPT 영향 인정 후 거의 -50% | AI core-service disruption 매우 강함      | education AI disruption hard gate   |
| 2U                                |         hard 4C |            Chapter 11, market value collapse | OPM debt model 반례                     | leverage/student ROI 가중치 상향         |
| Whirlpool                         |         hard 4C |                    배당 중단·guidance cut·14년 저점 | hardware cycle RedTeam 매우 잘 맞음        | hardware cycle 감점 강화                |
| Santa Ana self-checkout           |        4C-watch |                             local regulation | kiosk ROI gate                        | self-checkout local regulation 강화   |
| Juul                              |         Stage 2 |                            FDA authorization | 규제승인 stage 포착                         | public health gate 유지               |
| WHO nicotine pouch                |        4C-watch |                         youth-safety warning | 반복소비 RedTeam                          | youth-safety hard gate              |
| Cannabis Schedule III 일부 전환       |       Stage 1~2 |                         partial rescheduling | 완전합법화 오분류 방지                          | partial limit overlay 유지            |

---

### 6-3. R12 Loop 10 점수비중 재조정

이번 검증 결과 R12 점수표는 이렇게 조정한다.

```text
상향:
seed/IP/licensing revenue
government conditional approval / stockpile candidate
farm machinery demand-cycle gate
right-to-repair regulatory gate
vertical farming unit economics gate
livestock price-regulatory gate
edtech bookings / monetization gate
AI education disruption gate
OPM leverage/debt distress gate
hardware cycle gate
self-checkout local regulation gate
nicotine youth-safety gate

유지:
fertilizer input cycle
potash/phosphate strategic option
animal health biosecurity
regulated consumer product
cannabis regulated product
home living appliance rental
smart farm agritech

하향 또는 cap:
smart farm narrative-only
vertical farming tech-only
AI education feature-only
질병 수혜 headline-only
농기계 자율화 tech-only
self-checkout hardware-only
nicotine alternative 반복소비-only
cannabis rescheduling-only
생활가전 hardware replacement-only
```

구체적으로는 이렇게 간다.

| 항목                      | Loop 9 감각 |                           Loop 10 조정 |
| ----------------------- | --------: | -----------------------------------: |
| EPS/FCF·OPM             |        중요 |                 유지. 단 Stage 3 후보는 드묾 |
| 반복계약·규제승인               |        중요 |                상향. Bayer·Juul·Zoetis |
| unit economics          |        중요 | 더 상향. Bowery·Whirlpool·self-checkout |
| 농가 capex cycle          |        보조 |                              상향. CNH |
| right-to-repair         |        보조 |                     hard gate. Deere |
| AI education disruption |        보조 |            hard gate. Chegg·Duolingo |
| capital/debt            |        보조 |                        상향. 2U·Bowery |
| public health           |        보조 |        hard gate. WHO nicotine pouch |
| valuation room          |        보조 |                        테마성 강하면 감점 강화 |

---

### 6-4. R12 Loop 10 archetype별 최종 stage 규칙

```text
SMART_FARM_AGRI_TECH:
Stage 1 = 스마트팜·AI 농업 narrative
Stage 2 = 실제 수주·운영계약·가동률
Stage 3 = unit economics + FCF + 반복계약
Stage 4B = 스마트팜 테마 과열
Stage 4C = 수직농장 shutdown, energy cost, premium pricing failure
```

```text
AGRI_MACHINERY_DEMAND_CYCLE:
Stage 1 = 자율농기계·정밀농업 narrative
Stage 2 = 장비판매·dealer inventory 정상화
Stage 3 = 농가소득 개선 + software/service revenue + FCF
Stage 4B = 농기계 자동화 테마 과열
Stage 4C = crop price 약세, financing cost, dealer inventory, forecast cut
```

```text
AGRI_MACHINERY_SOFTWARE_LOCKIN:
Stage 1 = connected equipment·repair software moat
Stage 2 = software attach·service revenue
Stage 3 = right-to-repair 통과 후 recurring revenue
Stage 4C = settlement, FTC lawsuit, construction equipment lawsuit
```

```text
AGRI_INPUT_SEED_CROP_PROTECTION:
Stage 1 = 식량안보·종자·농약 narrative
Stage 2 = licensing revenue·EBITDA improvement
Stage 3 = 반복 licensing + litigation 안정 + FCF
Stage 4C = Roundup litigation, patent expiry, farmer margin 악화
```

```text
FERTILIZER_INPUT_COST_CYCLE:
Stage 1 = potash/phosphate/nitrogen 수요·가격
Stage 2 = volume·price·supply discipline 확인
Stage 3 = 저비용 구조 + farmer ROI + FCF 전까지 제한
Stage 4C = crop price 하락, demand deferral, sulfuric acid/input cost spike
```

```text
ANIMAL_HEALTH_BIOSECURITY:
Stage 1 = 질병 outbreak
Stage 2 = 조건부 승인·정부 비축 가능성
Stage 3 = 실제 정부 주문 + 반복 접종 + 매출·OPM
Stage 4C = outbreak 정상화, 백신 미사용, 무역 제한
```

```text
AGRI_LIVESTOCK_FOOD_COMMODITY:
Stage 1 = 조류독감·ASF·공급차질
Stage 2 = 가격상승·매출증가
Stage 3 = 구조적 Green 제한. 대부분 cyclical_success
Stage 4C = 가격 정상화, DOJ investigation, 담합·소비자 반발
```

```text
EDTECH_AI_MONETIZATION_TRADEOFF:
Stage 1 = AI tutor / speaking feature
Stage 2 = AI feature rollout·engagement·bookings growth
Stage 3 = bookings + paid conversion + margin + FCF
Stage 4C = bookings miss, AI feature cost, monetization 후퇴
```

```text
EDTECH_AI_DISRUPTION:
Stage 1 = AI answer engine emergence
Stage 2 = traffic/subscriber impact 확인
Stage 4C = AI가 core service 대체, subscriber decline, layoffs, guide miss
```

```text
ONLINE_EDUCATION_OPM_DISTRESS:
Stage 1 = online education growth
Stage 2 = university partnership·student enrollment
Stage 3 = student ROI + FCF + low leverage
Stage 4C = Chapter 11, high leverage, regulatory pressure
```

```text
HOME_LIVING_APPLIANCE_RENTAL:
Stage 1 = 렌탈 계정 증가
Stage 2 = 해지율 안정·관리서비스 반복매출
Stage 3 = recurring service revenue + FCF
Stage 4C = hardware cycle, dividend suspension, guide cut
```

```text
SERVICE_KIOSK_SELF_CHECKOUT:
Stage 1 = 무인화·인건비 상승
Stage 2 = 설치대수·유지보수 매출
Stage 3 = payment fee + shrink 감소 + retailer retention
Stage 4C = item limit, staffed lane, employee monitoring, local regulation
```

```text
CONSUMER_REGULATED_PRODUCT:
Stage 1 = FDA/DEA 규제완화 기대
Stage 2 = 허가·rescheduling·판매범위 확인
Stage 3 = 반복매출 + public health gate 통과 + FCF
Stage 4C = 허가취소, youth usage, flavor restriction, state/federal conflict
```

---

# R12 Loop 10 결론

이번 R12 Loop 10의 핵심은 이거다.

```text
R12는 “생활필수·농업·교육·규제완화”와 “반복현금흐름”을 분리하는 라운드다.
```

```text
Stage 포착이 잘 맞은 사례:
Bayer = soy seed licensing → Crop Science EBITDA +17.9%, 주가 최대 +6.9%
Nutrien = potash demand / phosphate strategic option, 단 cycle Watch
Zoetis = USDA conditional bird flu vaccine license, Stage 1~2
Juul = FDA authorization, 규제형 소비재 Stage 2
Cannabis partial rescheduling = Stage 1~2, 완전 합법화 아님
Duolingo = bookings가 강하면 +35%, 약하면 -20%로 stage gate가 뚜렷함

RedTeam이 가격·사업경로와 잘 맞은 사례:
CNH = 농기계 수요 둔화 → 주가 -7.1%
Deere = right-to-repair settlement·FTC·construction repair lawsuit
Bowery = vertical farming shutdown
Cal-Maine = 조류독감 수혜와 DOJ 조사, after-hours -4% 이상
Chegg = ChatGPT core-service disruption, 거의 -50%
2U = Chapter 11, OPM debt model 붕괴
Whirlpool = dividend suspension·guidance cut·14년 저점
Santa Ana / Long Beach self-checkout = local regulation
WHO nicotine pouch = youth-safety warning
```

**R12 Loop 10 점수정규화의 핵심 문장:**

> 농업·생활서비스·기타는 “농업”, “생활필수”, “질병 수혜”, “AI 교육”, “스마트팜”, “무인화”, “규제완화”라는 이름이 아니라 **반복계약, 반복매출, licensing revenue, unit economics, 판가전가, farm income, CAC, churn, bookings, 해지율, 규제승인 범위, public-health gate, debt, FCF, 실제 가격경로**로 봐야 한다.
> 이번 Loop 10에서는 `Bayer`, `Zoetis`, `Juul`, `Cannabis partial rescheduling`, `Duolingo bookings case`가 Stage 1~2 이상 포착 사례이고, `CNH`, `Deere`, `Bowery`, `Cal-Maine`, `Chegg`, `2U`, `Whirlpool`, `self-checkout regulation`, `nicotine pouch warning`이 R12 RedTeam이 실제 가격·사업경로와 맞는 반례다.

다음 순서는 **R13 — Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리 Loop 10**다.

[1]: https://www.reuters.com/business/bayer-q1-operating-profit-up-9-crop-protection-unit-gains-2026-05-12/?utm_source=chatgpt.com "Bayer Q1 operating profit jumps 9% on boost from soy business"
[2]: https://www.wsj.com/business/earnings/bayer-net-profit-surges-driven-by-growth-in-agricultural-division-0ecd9f4b?utm_source=chatgpt.com "Bayer Shares Climb After Earnings Beat Expectations"
[3]: https://www.reuters.com/business/nutrien-expects-higher-global-potash-demand-eyes-future-its-phosphate-business-2025-11-06/?utm_source=chatgpt.com "Nutrien expects higher global potash demand, eyes future of its phosphate business"
[4]: https://www.wsj.com/business/earnings/mosaic-swings-to-loss-on-surging-sulfuric-acid-prices-fec74551?utm_source=chatgpt.com "Mosaic Pulls Guidance, Cuts Spending as Fertilizer Costs Surge"
[5]: https://www.reuters.com/business/healthcare-pharmaceuticals/us-grants-conditional-clearance-zoetis-bird-flu-vaccine-poultry-2025-02-14/?utm_source=chatgpt.com "US gives conditional nod to Zoetis' bird flu vaccine for poultry"
[6]: https://www.reuters.com/sustainability/boards-policy-regulation/fda-approves-juuls-tobacco-menthol-e-cigarettes-2025-07-17/?utm_source=chatgpt.com "FDA approves Juul's tobacco and menthol e-cigarettes"
[7]: https://apnews.com/article/9561d6a26972c01613c4fd3ebbbd981e?utm_source=chatgpt.com "Juul gets FDA's OK to keep selling tobacco and menthol e-cigarettes"
[8]: https://www.reuters.com/legal/litigation/cannabis-rescheduling-arrives-with-limits-what-dojs-final-order-does-doesnt-do--pracin-2026-05-12/?utm_source=chatgpt.com "Cannabis rescheduling arrives, with limits: What the DOJ's final order does and doesn't do"
[9]: https://www.investopedia.com/duolingo-stock-soars-35-percent-as-language-learning-firm-adds-subscribers-bookings-11786564?utm_source=chatgpt.com "Duolingo Stock Soars 35% as Language-Learning Firm Adds Subscribers, Bookings"
[10]: https://www.reuters.com/business/duolingo-says-ai-features-profitable-it-beats-revenue-estimates-raises-forecast-2025-11-05/?utm_source=chatgpt.com "Duolingo's soft bookings forecast overshadows revenue beat, shares plunge"
[11]: https://www.reuters.com/business/machinery-maker-cnh-cuts-full-year-profit-forecast-weak-demand-weighs-2025-11-07/?utm_source=chatgpt.com "Machinery maker CNH cuts full-year profit forecast as weak demand weighs"
[12]: https://www.reuters.com/sustainability/boards-policy-regulation/deere-settles-us-right-to-repair-lawsuit-with-99-million-fund-repair-commitments-2026-04-07/?utm_source=chatgpt.com "Deere settles US right-to-repair lawsuit with $99 million fund, repair commitments"
[13]: https://www.wsj.com/business/right-to-repair-advocates-are-taking-on-deere-againthis-time-in-construction-a93aa654?utm_source=chatgpt.com "Right-to-Repair Advocates Are Taking On Deere Again-This Time in Construction"
[14]: https://www.axios.com/2024/11/05/bowery-vertical-farming-close?utm_source=chatgpt.com "Vertical farming \"unicorn\" Bowery to shut down"
[15]: https://apnews.com/article/62e581aca199912082c2a06b211248ab?utm_source=chatgpt.com "US egg giant Cal-Maine says government is investigating price increases"
[16]: https://www.marketwatch.com/story/cal-maines-stock-falls-as-doj-reportedly-weighs-bigger-crackdown-on-major-egg-producers-96e8315b?utm_source=chatgpt.com "Cal-Maine's stock falls as DOJ reportedly weighs bigger crackdown on major egg producers"
[17]: https://www.investopedia.com/chegg-shares-plunge-after-company-warns-that-chatgpt-is-impacting-growth-7487968?utm_source=chatgpt.com "Chegg Shares Plunge After Company Warns That ChatGPT Is Impacting Growth"
[18]: https://www.wsj.com/business/2u-ed-tech-company-files-chapter-11-bankruptcy-24ca1017?utm_source=chatgpt.com "2U, Once a Giant in Online Education, Files for Chapter 11 Bankruptcy"
[19]: https://www.reuters.com/business/whirlpool-shares-tumble-after-revenue-miss-dividend-suspension-2026-05-07/?utm_source=chatgpt.com "Whirlpool shares hit 14-year low after slashing annual targets, suspending dividend"
[20]: https://www.barrons.com/articles/whirlpool-stock-falling-outlook-8d0bd413?utm_source=chatgpt.com "Whirlpool Stock Is Still Falling. Last Week's Earnings Might Be Why."
[21]: https://www.the-sun.com/money/16343669/target-self-checkout-limits-santa-ana-california/?utm_source=chatgpt.com "All Target locations hit with checkout change under city's new 'limits policy' - and shoppers have 60 days"
[22]: https://nypost.com/2025/10/15/us-news/long-beach-restricts-self-checkouts-in-attempt-to-stop-shoplifters/?utm_source=chatgpt.com "California city severely restricts self-checkouts in attempt to stop shoplifters"
[23]: https://www.reuters.com/legal/litigation/who-warns-loosely-regulated-nicotine-pouches-risk-youth-addiction-2026-05-15/?utm_source=chatgpt.com "WHO warns loosely regulated nicotine pouches risk youth addiction"

좋아. 정해둔 순서대로 이번은 **R12 — 농업·생활서비스·기타**로 넘어간다.

R12는 겉으로 보면 잡다한 테마 묶음처럼 보이지만, 실제로는 에이전트 점수정규화에서 아주 중요해. 이유는 이쪽이 **질병·날씨·곡물·정책·저출산·규제·일회성 수요**에 많이 흔들리기 때문이다. 업로드된 Theme Tag Map에서도 양돈, 육계, 사료, 대두, 농기계, 스마트팜, 교육, 취업, 키즈, 전자담배, 주정 등은 대부분 Watch/Red 또는 Event/Watch로 잡혀 있고, 실제 수주·반복매출·판가전가·규제 승인 전까지 Green을 제한해야 한다고 정리되어 있다.

서생원식으로 보면 R12의 핵심은 “생활에 꼭 필요하다”가 아니다. **EPS/FCF 체급 변화가 반복적으로 지속되고, 시장이 그 구조를 아직 낮게 평가하는가**가 핵심이다. 사료비가 잠깐 내려가거나 조류독감으로 계란값이 오르거나 정책으로 스마트팜이 뜨는 것은 Stage 1일 뿐이고, 반복계약·가동률·판가전가·FCF가 확인돼야 한다.

---

# R12. 농업·생활서비스·기타

## 1. 이번 라운드 대섹터

```text
R12 = 농업·생활서비스·기타
```

R12의 기본 구조는 이렇게 나눈다.

```text
1. 농업·스마트팜·농기계
스마트팜 / 농기계 / 종자·비료·농약
→ 실제 수주·해외확장·운영계약·반복 서비스가 핵심

2. 농축산·식품 원가 cycle
양돈 / 육계 / 사료 / 대두 / 참치
→ 가격·질병·날씨·사료비 cycle
→ 대부분 Watch/Red

3. 교육·취업·키즈
교육 / 취업 / 에듀테크 / 키즈 / 유아용품
→ 반복수강·B2B·성인교육이면 후보
→ 저출산·AI 대체·규제는 hard risk

4. 생활가전·렌탈·키오스크
밥솥 / 렌탈 / 스마트홈 / 키오스크
→ 일회성 hardware는 Watch/Red
→ 렌탈·관리·유지보수 반복매출이면 Watch-to-Green

5. 규제형 소비재
전자담배 / 주정 / 마리화나
→ 반복소비는 있으나 규제 승인·불허가가 Stage를 좌우
```

---

## 2. 대상 canonical archetype

| 구분              | canonical archetype              | Green 정책       |
| --------------- | -------------------------------- | -------------- |
| 스마트팜·농업기술       | `SMART_FARM_AGRI_TECH`           | Watch-to-Green |
| 농기계·정밀농업        | `AGRI_MACHINERY_PRECISION_CYCLE` | Watch          |
| 농축산·식품 원가 cycle | `AGRI_LIVESTOCK_FOOD_COMMODITY`  | Watch/Red      |
| 동물백신·방역         | `ANIMAL_HEALTH_BIOSECURITY`      | Watch          |
| 교육·성인교육·취업      | `EDUCATION_SPECIALTY_SERVICES`   | Watch-to-Green |
| 키즈·유아용품         | `HOME_CHILD_EDUCATION`           | Watch/Red      |
| 생활가전·렌탈         | `HOME_LIVING_APPLIANCE_RENTAL`   | Watch-to-Green |
| 키오스크·셀프체크아웃     | `SERVICE_KIOSK_SELF_CHECKOUT`    | Watch          |
| 규제형 소비재         | `CONSUMER_REGULATED_PRODUCT`     | Watch          |
| 주정·식품 input     | `FOOD_INPUT_REGULATED_CYCLE`     | Watch          |
| 정책성 일자리·지역 서비스  | `POLICY_LOCAL_SERVICE_THEME`     | Event/Watch    |

---

## 3. deep sub-archetype

```text
SMART_FARM_AGRI_TECH
- 스마트팜
- 수직농장
- 온실 자동화
- 농업 로봇
- 정밀농업 AI
- 해외 수주
- 운영계약
- 유지보수·SaaS 매출

AGRI_MACHINERY_PRECISION_CYCLE
- 농기계
- 자율주행 트랙터
- 농업용 드론
- 정밀 살포
- 농가 소득
- 금리·할부금융
- 장비 교체 cycle

AGRI_LIVESTOCK_FOOD_COMMODITY
- 양돈
- 육계
- 배합사료
- 대두
- 참치 원양어업
- 어가
- 유가
- 환율
- 사료비
- 질병 이벤트

ANIMAL_HEALTH_BIOSECURITY
- 동물백신
- 조류독감 백신
- ASF 방역
- 정부 비축
- 반복 접종
- 방역 계약

EDUCATION_SPECIALTY_SERVICES
- 입시교육
- 성인교육
- 취업교육
- AI 교육
- B2B 기업교육
- 구독형 교육
- 자격증
- 직무교육

HOME_CHILD_EDUCATION
- 키즈
- 유아용품
- 학습지
- 저출산
- 프리미엄 육아
- 해외 확장

HOME_LIVING_APPLIANCE_RENTAL
- 밥솥
- 정수기
- 공기청정기
- 비데
- 매트리스
- 필터·관리 서비스
- 렌탈 계정
- 해지율

SERVICE_KIOSK_SELF_CHECKOUT
- 키오스크
- 셀프체크아웃
- 무인점포
- 결제수수료
- 유지보수
- theft
- 고객불만

CONSUMER_REGULATED_PRODUCT
- 전자담배
- 주정
- 마리화나
- 의료용 cannabis
- FDA/DEA 규제
- 사회적 반발
```

---

# 4. 성공사례

## 4-1. John Deere 자율농기계 — `AGRI_MACHINERY_PRECISION_CYCLE`

John Deere는 CES 2025에서 자율주행 트랙터, 무인 잔디깎이, 무인 덤프트럭, 과수원용 자율 트랙터 등을 공개했다. AP는 이 기술들이 노동력 부족과 기후·환경 압박에 대응하기 위한 정밀농업 기술로 소개됐고, 농약·비료 살포를 더 정확하게 하려는 목적도 있다고 보도했다. 이건 `SMART_FARM_AGRI_TECH`와 `AGRI_MACHINERY_PRECISION_CYCLE`의 Stage 1 성공 후보야. 다만 장비 판매와 농가 ROI가 확인되기 전까지 Green은 아니다. ([AP News][1])

**가격경로 1차 판정**

```text
판정:
precision_agri_stage1_success_candidate

좋은 점:
- 노동력 부족 해결
- 농약·비료 정밀살포
- 자율농기계 기술 진전
- 농업 생산성 개선 가능성

주의:
- 장비 가격
- 농가 소득
- 금리·할부금융
- 실제 adoption rate
- 반복 소프트웨어 매출 여부
```

**점수 교정**

```text
EPS/FCF: 중간
Structural Visibility: 중간
Bottleneck/Pricing: 낮음~중간
Market Mispricing: 중간
Risk: 농가 capex cycle, 금리, 장비 교체수요 둔화
```

---

## 4-2. Deere 장비 cycle 반례를 동반한 성공 후보

Deere는 정밀농업·자율농기계의 장기 후보지만, 2025년 1분기에는 농기계 수요 둔화로 매출이 35% 감소했고, 농가가 약한 소득과 높은 차입비용 때문에 장비 구매보다 임대를 선택하면서 주가가 premarket에서 약 4.5% 하락했다. 이 사례는 “농업 자동화 기술은 좋아도 농기계 기업은 농가 소득·금리·교체 cycle에 묶인다”는 점수정규화 기준을 준다. ([Reuters][2])

**가격경로 1차 판정**

```text
가격 반응:
premarket -4.5%

판정:
technology_success_but_cycle_watch

의미:
자율농기계 기술은 Stage 1 후보.
하지만 농기계 회사 점수는 농가소득·금리·장비 cycle 때문에 Green 제한.
```

---

## 4-3. Zoetis 조류독감 백신 — `ANIMAL_HEALTH_BIOSECURITY`

미국 USDA는 Zoetis의 가금류 조류독감 백신 사용을 조건부 승인했다. Reuters는 이 승인이 긴급·특수 상황에서 안전성과 기대 효능을 근거로 부여됐고, USDA가 상업·야생 조류에 퍼진 바이러스 strain에 맞춘 백신 비축을 재구축하려 한다고 보도했다. 이건 질병 뉴스가 실제 승인·비축 수요로 넘어가는 Stage 1~2 후보 사례다. ([Reuters][3])

**가격경로 1차 판정**

```text
판정:
animal_health_event_to_contract_candidate

좋은 점:
- 조건부 승인
- 정부 비축 가능성
- 반복 접종 가능성
- animal health 유통망

주의:
- emergency license
- 정부 사용정책 불확실
- outbreak 정상화
- one-off stockpile 가능성
```

**점수 교정**

```text
EPS/FCF: 중간
Structural Visibility: 낮음~중간
Bottleneck/Pricing: 낮음~중간
Risk: 질병 이벤트 정상화, 정부 구매 종료
```

---

## 4-4. Cal-Maine / 계란 가격 cycle — `AGRI_LIVESTOCK_FOOD_COMMODITY`

Cal-Maine은 미국 최대 계란 판매업체로, 조류독감에 따른 공급차질과 계란 가격 급등 속에 2024년 12월~2025년 2월 분기 순이익이 전년 대비 247% 증가한 5.085억 달러를 기록했다. FT는 도매 계란가격이 2025년 2월 dozen당 8.58달러까지 올랐다가 4월 초 3.91달러로 내려왔고, DOJ의 가격담합 조사도 존재한다고 보도했다. 이건 수익은 날 수 있지만 구조적 Green이 아니라 **질병·가격 cycle success**로 분류해야 하는 사례다. ([Financial Times][4])

**가격경로 1차 판정**

```text
판정:
cyclical_success_candidate + regulatory_watch

좋은 점:
- 가격 급등
- 생산능력·인수 효과
- 이익 급증

주의:
- 계란가격 정상화
- 조류독감 one-off
- DOJ price-fixing inquiry
- 소비자·정책 반발
```

---

## 4-5. Multiverse / AI workforce training — `EDUCATION_SPECIALTY_SERVICES`

Multiverse는 AI workforce training과 apprenticeship 플랫폼으로, 2026년 신규 funding에서 valuation이 21억 달러로 올라갔고 Microsoft, M&S 등 고객을 대상으로 약 3만 명의 apprentice를 훈련시킨 것으로 보도됐다. 다만 2025년 3월 종료 회계연도 매출은 7,960만 파운드로 늘었지만 손실도 6,240만 파운드로 확대되었고, 과정 completion rate가 sector average보다 낮다는 지적도 있었다. 이 사례는 성인교육·AI 재교육이 후보가 될 수 있지만, 아직 FCF와 교육성과를 검증해야 한다는 mixed case다. ([Financial Times][5])

**가격경로 1차 판정**

```text
판정:
adult_ai_training_success_candidate_but_profitability_watch

좋은 점:
- AI 재교육 수요
- B2B/B2G apprenticeship
- 대형 고객
- cash-positive quarter 언급

주의:
- 손실 확대
- completion rate
- 비상장 valuation
- 기업 교육 예산 cycle
```

---

## 4-6. Duolingo — `EDUCATION_SPECIALTY_SERVICES`

Duolingo는 교육 앱의 성공 후보지만, 가격경로상 강한 반례도 제공한다. 2026년 2월 Duolingo는 AI-powered speaking 기능을 더 넓게 제공하고 user growth를 우선하겠다고 밝혔지만, Q1·연간 bookings 전망이 시장 예상보다 낮아 주가가 23% 이상 하락했다. 이건 교육 앱도 “유저 성장”보다 **bookings, monetization, margin, AI 비용**이 중요하다는 사례다. ([Reuters][6])

**가격경로 1차 판정**

```text
가격 반응:
-23% 이상

판정:
education_app_monetization_4c_watch

의미:
AI 기능 확대와 user growth는 Stage 1.
bookings와 margin이 희생되면 Stage 3-Green 금지.
```

---

## 4-7. Coway 렌탈 모델 — `HOME_LIVING_APPLIANCE_RENTAL`

Coway는 정수기·공기청정기·비데·매트리스 등 생활가전 렌탈·관리 모델을 가진 기업이고, 한국뿐 아니라 말레이시아, 미국, 태국, 인도네시아, 베트남 등 해외 자회사도 보유한다. 생활가전이 일회성 hardware 판매에 머물면 Watch/Red지만, Coway처럼 렌탈 계정·필터·관리 서비스가 붙으면 반복매출 후보가 된다. ([위키백과][7])

**가격경로 1차 판정**

```text
판정:
recurring_home_service_candidate

좋은 점:
- 렌탈 계정
- 필터·관리 반복매출
- 해외 계정 확장
- 구독형 소비재 모델

주의:
- 해지율
- 경쟁
- 해외 마진
- 소비 경기
```

---

## 4-8. Juul FDA 승인 — `CONSUMER_REGULATED_PRODUCT`

FDA는 2025년 Juul의 tobacco·menthol e-cigarette 기기와 refill cartridge 판매를 승인했다. Reuters는 이 승인이 2022년 연방 판매 금지와 파산위기 이후의 큰 반전이라고 설명했다. 이 사례는 규제형 소비재에서 **FDA 승인 하나가 Stage를 크게 바꿀 수 있음**을 보여준다. 다만 같은 사실은 반대로 “불허가·규제 강화가 4C가 된다”는 뜻이기도 하다. ([Reuters][8])

**가격경로 1차 판정**

```text
판정:
regulated_consumer_approval_stage2_candidate

좋은 점:
- FDA 승인
- 반복소비
- 브랜드·디바이스 ecosystem

주의:
- 청소년 사용 논란
- 규제 반전 가능성
- 사회적 반발
- 판매 허가 범위 제한
```

---

# 5. 반례

## 5-1. 수직농장 / Bowery shutdown — `SMART_FARM_AGRI_TECH`

Bowery는 7억 달러 이상을 조달한 vertical farming unicorn이었지만, 2024년 폐쇄되었다. Axios는 Bowery가 AeroFarms와 AppHarvest 같은 vertical farming 실패 사례를 뒤따랐고, 소비자들이 더 비싼 “cleaner produce”에 충분한 프리미엄을 지불하지 않았다고 설명했다. 이건 스마트팜·수직농장이 기술적으로 그럴듯해도 **unit economics, 전력비, 소비자 가격, 자본비용**이 안 맞으면 무너질 수 있다는 대표 반례다. ([Axios][9])

**교훈**

```text
스마트팜 기술
≠ Green

반드시 볼 것:
- 실제 고객
- 생산 원가
- 에너지비
- 가격 프리미엄
- 가동률
- 반복 계약
- FCF
```

**가격경로 1차 판정**

```text
판정:
vertical_farming_unit_economics_4c
```

---

## 5-2. AppHarvest Chapter 11 — `SMART_FARM_AGRI_TECH`

AppHarvest는 SPAC으로 상장했던 hydroponics/vertical farming 기업이었지만, 2023년 Chapter 11 파산보호를 신청했고, 보유 greenhouses는 매각되었다. 이 사례는 “친환경 농업·스마트팜·대형 온실” 테마가 실제 생산성·노동·원가·안전·자본비용을 통과하지 못하면 상장사 관점에서 hard 4C로 갈 수 있음을 보여준다. ([위키백과][10])

**교훈**

```text
수직농장 CAPEX
≠ 구조적 수익성

4C 조건:
- Chapter 11
- greenhouse 매각
- 원가·노동·안전 문제
- SPAC hype 붕괴
```

---

## 5-3. Chegg / AI disruption — `EDUCATION_SPECIALTY_SERVICES`

Chegg는 AI가 기존 교육 서비스 비즈니스모델을 직접 잠식한 반례다. 2023년 Chegg가 ChatGPT를 심각한 경쟁자로 인정하자 주가가 하루 38% 급락했고, 이후 AI Overviews가 traffic과 revenue를 훼손한다며 Google을 상대로 소송까지 제기했다. 이 사례는 교육 서비스가 반복매출처럼 보여도 **AI가 답변·숙제도움·검색 유입을 대체하면 4C가 될 수 있음**을 보여준다. ([위키백과][11])

**가격경로 1차 판정**

```text
가격 반응:
ChatGPT threat 인정 후 -38%

판정:
education_ai_disruption_hard_4c

의미:
교육은 AI 수혜와 AI 피해를 반드시 분리해야 한다.
```

---

## 5-4. 2U Chapter 11 — `EDUCATION_SPECIALTY_SERVICES`

2U는 온라인 교육 플랫폼·OPM 모델의 대표 반례다. 2024년 Chapter 11 파산보호를 신청하며 4.5억 달러 이상 부채를 제거했고, 이전부터 profitability 문제와 온라인 학위 프로그램의 비용·성과 논란이 이어졌다. 온라인 교육도 B2B/B2C 반복매출처럼 보일 수 있지만, CAC, 대학 파트너십, 학생 성과, 부채 구조가 나쁘면 hard 4C로 간다. ([위키백과][12])

**교훈**

```text
온라인 교육 플랫폼
≠ Green

필수 확인:
- CAC
- partner concentration
- completion rate
- student ROI
- debt
- FCF
```

---

## 5-5. Whirlpool hardware cycle — `HOME_LIVING_APPLIANCE_RENTAL`

Whirlpool은 생활가전 hardware cycle의 핵심 반례다. 2026년 실적 전망을 절반 수준으로 낮추고 배당을 중단했으며, 고금리, 주택 거래 부진, 소비지출 약화, 에너지 가격 상승으로 교체수요가 줄었다. 주가는 14년 저점까지 하락했고, 발표 후 13% 이상 하락했다. ([Reuters][13])

**가격경로 1차 판정**

```text
가격 반응:
-13% 이상, 14년 저점

판정:
home_appliance_hardware_cycle_4c

의미:
생활가전은 렌탈·관리 반복매출이 없으면 Green 금지.
```

---

## 5-6. 셀프체크아웃 theft·고객경험 — `SERVICE_KIOSK_SELF_CHECKOUT`

Target은 self-checkout을 10개 품목 이하로 제한했고, 일부 Walmart 매장도 theft와 고객경험 문제로 self-checkout을 제거했다. 셀프체크아웃은 자동화처럼 보이지만 실제로는 theft, 고객불만, 직원 workload 증가, 매장 운영 복잡성을 키울 수 있다. Target 정책 변화는 “키오스크 설치대수 증가 = 자동 Green”이 아니라는 반례다. ([New York Post][14])

또 self-service machine은 실제 자동화가 아니라 고객에게 노동을 떠넘기는 pseudo-automation으로 작동할 수 있고, 직원들은 여러 고객 문제 해결·감시·갈등 관리를 동시에 떠안게 된다는 연구도 있다. ([arXiv][15])

**가격경로 1차 판정**

```text
판정:
kiosk_self_checkout_operational_counterexample

의미:
키오스크는 유지보수·결제수수료·loss prevention 매출이 있어야 Watch-to-Green.
장비 판매만 있으면 one-off hardware.
```

---

## 5-7. 마리화나 rescheduling의 한계 — `CONSUMER_REGULATED_PRODUCT`

2026년 DOJ·DEA는 일부 cannabis-related substances를 Schedule I에서 Schedule III로 재분류하는 final order를 냈지만, Reuters는 이것이 연방 차원의 완전 합법화를 의미하지 않고 주·연방법 충돌도 남아 있다고 설명했다. 의료 cannabis 사업자에는 280E 세금 부담 완화 등 긍정 효과가 있을 수 있지만, recreational operator는 직접 수혜가 제한적이고 DEA 등록도 필요하다. ([Reuters][16])

**교훈**

```text
규제 완화
≠ Green

필수 확인:
- 실제 허가
- 판매채널
- 세금효과
- 법적 충돌 해소
- 반복매출
- 사회적 반발
```

---

# 6. 4B-watch 사례

## 6-1. 농업 자동화·스마트팜 4B-watch

```text
4B 조건:
- 자율농기계·스마트팜 뉴스로 관련주 동반 급등
- 농가 ROI와 장비 판매 없이 기술 narrative가 먼저 반영
- 농가 소득·금리·할부금융 리스크를 시장이 무시
```

John Deere 자율농기계는 기술적으로 매력적이지만, Deere의 농기계 수요 둔화와 주가 하락 사례가 보여주듯 cycle risk를 같이 봐야 한다. ([Reuters][2])

---

## 6-2. 계란·육계·양돈 가격 급등 4B-watch

```text
4B 조건:
- 조류독감·ASF·공급차질로 가격 급등
- 관련 식품·축산주 동반 급등
- 가격 정상화와 정부조사 리스크를 시장이 무시
```

Cal-Maine의 이익 급증은 수익 기회지만, 계란가격 정상화와 DOJ price-fixing inquiry가 같이 붙어 있다. ([Financial Times][4])

---

## 6-3. AI 교육·성인교육 4B-watch

```text
4B 조건:
- AI 재교육·reskilling narrative 과열
- 매출보다 valuation이 먼저 상승
- completion rate·고객 retention·profitability가 불명확
```

Multiverse는 AI workforce training 후보지만, 매출 성장과 함께 손실 확대·completion rate 문제가 있었다. ([Financial Times][5])

---

## 6-4. 규제형 소비재 4B-watch

```text
4B 조건:
- FDA 승인 또는 cannabis rescheduling 뉴스만으로 관련주 급등
- 실제 판매 허가 범위·세금효과·채널·반복매출 확인 전 가격이 먼저 감
```

Juul의 FDA 승인은 강한 Stage 2 후보지만, 2022년 금지명령에서 2025년 승인으로 바뀐 것처럼 규제형 소비재는 policy reversal risk가 매우 크다. ([Reuters][8])

---

# 7. 4C-thesis-break 사례

## 7-1. 수직농장 파산

```text
4C:
Chapter 11 / Chapter 7
unit economics failure
energy cost
premium pricing failure
capex burden
consumer adoption failure
```

Bowery shutdown, AppHarvest Chapter 11, AeroFarms bankruptcy는 스마트팜·수직농장 관련주의 대표 4C다. ([Axios][9])

---

## 7-2. 농기계 cycle 하락

```text
4C-watch:
farm income weakness
high borrowing costs
equipment rental instead of purchase
tariff uncertainty
segment sales decline
```

Deere의 2025년 매출 35% 감소와 premarket -4.5% 반응은 정밀농업·농기계가 기술주가 아니라 capex-cycle 기업임을 보여준다. ([Reuters][2])

---

## 7-3. 교육 AI disruption

```text
4C:
AI substitutes core service
traffic decline
subscriber decline
strategic review
layoffs
lawsuit against platform gatekeeper
```

Chegg의 ChatGPT shock과 이후 Google AI Overviews 소송은 교육 콘텐츠 플랫폼의 hard 4C다. ([위키백과][11])

---

## 7-4. 생활가전 배당 중단

```text
4C:
replacement demand collapse
housing turnover weakness
dividend suspension
debt reduction pressure
stock at multi-year low
```

Whirlpool의 dividend suspension과 14년 저점은 hardware 생활가전의 대표 4C다. ([Reuters][13])

---

## 7-5. 키오스크·셀프체크아웃 축소

```text
4C-watch:
retailer retreats from self-checkout
theft/shrink
customer friction
employee workload
one-off hardware sales
```

Target과 Walmart의 self-checkout 제한·축소 사례는 키오스크 기업이 설치대수만으로 Green이 될 수 없음을 보여준다. ([New York Post][14])

---

## 7-6. 규제형 소비재 불허가·법적 충돌

```text
4C-watch:
FDA ban
DEA registration failure
state/federal law conflict
youth-use controversy
social backlash
```

Juul은 과거 FDA ban을 겪은 뒤 2025년 일부 제품 승인을 받았고, cannabis rescheduling도 연방 완전 합법화는 아니므로 규제형 소비재는 항상 hard RedTeam을 붙여야 한다. ([Reuters][8])

---

# 8. 점수비중 보정표 — R12 v1.0

| canonical archetype              | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | 핵심 감점                         |
| -------------------------------- | ------: | ---------: | ---------: | ---------: | --------: | ------: | ---: | ----------------------------- |
| `SMART_FARM_AGRI_TECH`           |      18 |         14 |         12 |          9 |         9 |       0 |    5 | 에너지비, CAPEX, unit economics   |
| `AGRI_MACHINERY_PRECISION_CYCLE` |      18 |         13 |         10 |         10 |         9 |       1 |    5 | 농가소득, 금리, 장비 cycle            |
| `AGRI_LIVESTOCK_FOOD_COMMODITY`  |      18 |         10 |         14 |          8 |         8 |       0 |    5 | 질병, 사료비, 날씨, 가격 정상화           |
| `ANIMAL_HEALTH_BIOSECURITY`      |      16 |         14 |          8 |         10 |         8 |       0 |    5 | 정부 사용정책, one-off stockpile    |
| `EDUCATION_SPECIALTY_SERVICES`   |      18 |         17 |          5 |         12 |        12 |       2 |    5 | AI 대체, CAC, completion rate   |
| `HOME_CHILD_EDUCATION`           |      16 |         12 |          5 |         10 |         8 |       0 |    5 | 저출산, TAM 축소, 규제               |
| `HOME_LIVING_APPLIANCE_RENTAL`   |      17 |         15 |          6 |         12 |        10 |       2 |    5 | 교체수요, 주택경기, 해지율               |
| `SERVICE_KIOSK_SELF_CHECKOUT`    |      17 |         15 |          7 |         12 |        10 |       0 |    5 | theft, 고객불만, one-off hardware |
| `CONSUMER_REGULATED_PRODUCT`     |      18 |         14 |          8 |         12 |        10 |       0 |    5 | 규제, public health, 사회적 반발     |
| `FOOD_INPUT_REGULATED_CYCLE`     |      17 |         11 |         12 |          8 |         8 |       0 |    5 | 원가, 판가전가, 규제                  |
| `POLICY_LOCAL_SERVICE_THEME`     |       5 |          5 |          5 |          8 |         5 |       0 |    3 | 정책 의존, 예산·계약 부재               |

---

# 9. stage date 후보

## `SMART_FARM_AGRI_TECH`

```text
Stage 1:
스마트팜 정책, 자율농기계, 수직농장, 농업 AI 뉴스

Stage 2:
실제 수주, 운영계약, 반복 유지보수·SaaS 매출, 가동률 확인

Stage 3:
unit economics와 FCF가 확인되고 반복계약이 붙을 때만

Stage 4B:
스마트팜·수직농장 narrative 과열

Stage 4C:
파산, energy cost, premium pricing 실패, CAPEX 부담
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
농가소득 약화, 고금리, 장비 판매 감소, tariff uncertainty
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
정부 구매 종료, 질병 정상화, 백신 미사용
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
AI가 핵심 서비스를 대체, CAC 상승, subscriber decline, bankruptcy
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
교체수요 붕괴, 배당중단, 해지율 상승, 주택경기 악화
```

## `SERVICE_KIOSK_SELF_CHECKOUT`

```text
Stage 1:
인건비 상승, 무인화, 키오스크 도입 뉴스

Stage 2:
설치대수, 유지보수 매출, 결제수수료, loss prevention 성과 확인

Stage 3:
recurring service revenue가 hardware 매출을 넘을 때만

Stage 4B:
무인화 테마 과열

Stage 4C:
retailer retreat, theft, 고객불만, one-off hardware 판매
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

---

# 10. 가격경로 검증계획

## R12 공통 검증 방식

```text
1. 각 case의 stage1_date, stage2_date, stage3_date를 지정한다.
2. 해당 날짜의 종가를 stage_price로 저장한다.
3. MFE_30D / 90D / 180D / 1Y / 2Y를 계산한다.
4. MAE_30D / 90D / 180D / 1Y를 계산한다.
5. peak_price와 drawdown_after_peak를 계산한다.
6. 농가소득, 장비판매, 상품가격, 질병 이벤트, 반복매출, CAC, 해지율, 규제 이벤트와 가격 경로를 비교한다.
```

## R12에서 반드시 분리할 판정

```text
aligned:
반복계약·반복매출·FCF와 주가 리레이팅이 같이 감.

cyclical_success:
계란·돼지고기·대두·사료·참치처럼 가격 cycle로 수익이 난 경우.

event_to_contract:
질병 이벤트가 실제 정부 비축·장기계약으로 이어진 경우.

theme_without_unit_economics:
스마트팜·수직농장·교육 앱·키오스크처럼 기술은 있으나 수익성 불명확.

regulatory_approval_stage2:
전자담배·cannabis처럼 규제 승인이 실제 판매 가능성을 바꾼 경우.

thesis_break:
파산, AI 대체, 배당중단, 규제불허, retailer retreat, 가격 정상화.
```

## 이번 R12에서 우선 검증할 가격 case

| case_id                                     |        stage2 후보일 | 현재 1차 가격판정                                |
| ------------------------------------------- | ----------------: | ----------------------------------------- |
| `john_deere_autonomous_agri_stage1_case`    |       2025-01 CES | 기술 후보, price backfill 필요                  |
| `deere_farm_equipment_demand_slowdown_case` |        2025-02-13 | -4.5% premarket, cycle 4C-watch           |
| `bowery_vertical_farming_shutdown_case`     |        2024-11-05 | vertical farming hard 4C                  |
| `appharvest_chapter11_case`                 |        2023-07-24 | smart farm hard 4C                        |
| `zoetis_bird_flu_vaccine_conditional_case`  |        2025-02-14 | animal health event-to-contract candidate |
| `calmaine_egg_price_profit_case`            |           2025 Q1 | cyclical success + regulatory watch       |
| `multiverse_ai_training_case`               |           2026-05 | adult education candidate, loss watch     |
| `duolingo_ai_strategy_bookings_miss_case`   |        2026-02-26 | -23%, monetization 4C-watch               |
| `chegg_ai_disruption_case`                  | 2023-05 / 2025-02 | -38%, AI disruption hard 4C               |
| `2u_chapter11_case`                         |        2024-07-25 | online education hard 4C                  |
| `coway_rental_recurring_case`               |        계정/해지율 확인일 | recurring home service candidate          |
| `whirlpool_dividend_suspension_case`        |        2026-05-07 | -13%, hardware cycle 4C                   |
| `target_self_checkout_limit_case`           |        2024-03-16 | kiosk operational counterexample          |
| `juul_fda_approval_case`                    |        2025-07-17 | regulated product Stage 2 candidate       |
| `cannabis_schedule3_limited_case`           |        2026-05-12 | regulatory watch, not full legalization   |

---

# 11. 다음에 에이전트가 채워야 할 price fields

R12 case library에는 아래 필드가 필요하다.

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
below_stage3_price_flag

farm_income_indicator
equipment_sales_growth
precision_agriculture_revenue
autonomous_equipment_order
software_attach_rate
farmer_financing_cost
tariff_exposure_flag

vertical_farming_revenue
vertical_farming_energy_cost
capacity_utilization
unit_economics_margin
chapter11_flag
chapter7_flag

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
vaccine_order_value

education_revenue_growth
subscription_count
enterprise_contract_count
completion_rate
student_roi_metric
cac
churn_rate
ai_disruption_flag
bankruptcy_flag

rental_accounts
rental_churn
recurring_service_revenue_ratio
filter_service_revenue
hardware_sales_ratio
dividend_suspension_flag

kiosk_installed_base
maintenance_revenue
payment_fee_revenue
retailer_retreat_flag
theft_shrink_indicator
customer_friction_flag

regulatory_approval_flag
fda_approval_flag
dea_rescheduling_flag
license_scope
youth_usage_risk_flag
public_health_warning_flag
legal_conflict_flag

score_price_alignment
price_validation_status
```

---

# R12 결론

R12는 “작은 테마들”처럼 보이지만, 실제로는 에이전트의 false-positive를 줄이는 데 매우 중요한 대섹터다.

```text
Green 가능성이 생기는 경우:
스마트팜이 실제 수주·운영계약·FCF를 보여주는 경우
동물백신이 정부 비축·반복 접종으로 이어지는 경우
교육이 B2B/B2G 반복계약과 OPM을 보여주는 경우
생활가전이 렌탈·관리 반복매출로 hardware cycle을 벗어나는 경우
규제형 소비재가 실제 허가·판매·반복매출을 보여주는 경우

Watch:
농기계
스마트팜
교육
키오스크
렌탈 생활가전
동물백신
전자담배
마리화나

Red/4C 방어 중심:
수직농장 파산
양돈·육계·사료·대두 가격 이벤트
전염병·조류독감 one-off 수요
AI가 대체하는 교육 플랫폼
일회성 생활가전 hardware
셀프체크아웃 theft·고객불만
저출산 직격 키즈·유아용품
규제 불확실한 cannabis·전자담배
```

**R12 점수정규화의 핵심 문장:**

> 농업·생활서비스·기타는 “생활 필수”나 “정책 수혜”가 아니라 **반복계약, 반복매출, unit economics, 판가전가, 해지율, CAC, 규제 승인, FCF 전환**으로 봐야 한다.
> 질병·날씨·곡물·저출산·규제·AI 대체가 개입되면 대부분은 structural_success가 아니라 `cyclical_success`, `event_to_contract`, `theme_without_unit_economics`, `thesis_break`로 분리해야 한다.

다음에 네가 “다음 라운드 진행해줘”라고 하면, 정해둔 순서에 따라 **R13 — Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리**로 넘어간다.

[1]: https://apnews.com/article/e1d7bc812bb20951dac7976f6b3527ad?utm_source=chatgpt.com "Farming tech is on display at CES as companies showcase their green innovations and initiatives"
[2]: https://www.reuters.com/business/deere-reports-lower-profit-muted-farm-equipment-demand-2025-02-13/?utm_source=chatgpt.com "Deere misses revenue estimates on subdued farm equipment demand"
[3]: https://www.reuters.com/business/healthcare-pharmaceuticals/us-grants-conditional-clearance-zoetis-bird-flu-vaccine-poultry-2025-02-14/?utm_source=chatgpt.com "US gives conditional nod to Zoetis' bird flu vaccine for poultry"
[4]: https://www.ft.com/content/b05d9645-8e1b-4f3b-b5da-a853bd51e00d?utm_source=chatgpt.com "Largest US egg seller reports soaring profits amid price-fixing inquiry"
[5]: https://www.ft.com/content/ec5764f0-b783-48ac-9f16-a0ecb9da9636?utm_source=chatgpt.com "Euan Blair's Multiverse hits $2.1bn valuation in AI workforce training push"
[6]: https://www.reuters.com/business/finance/duolingo-prioritizes-user-growth-over-monetization-forecasts-softer-bookings-2026-02-26/?utm_source=chatgpt.com "Duolingo shares drop after bookings outlook lags estimates amid strategy shift"
[7]: https://en.wikipedia.org/wiki/Coway_%28company%29?utm_source=chatgpt.com "Coway (company)"
[8]: https://www.reuters.com/sustainability/boards-policy-regulation/fda-approves-juuls-tobacco-menthol-e-cigarettes-2025-07-17/?utm_source=chatgpt.com "FDA approves Juul's tobacco and menthol e-cigarettes"
[9]: https://www.axios.com/2024/11/05/bowery-vertical-farming-close?utm_source=chatgpt.com "Vertical farming \"unicorn\" Bowery to shut down"
[10]: https://en.wikipedia.org/wiki/AppHarvest?utm_source=chatgpt.com "AppHarvest"
[11]: https://en.wikipedia.org/wiki/Chegg?utm_source=chatgpt.com "Chegg"
[12]: https://en.wikipedia.org/wiki/2U_%28company%29?utm_source=chatgpt.com "2U (company)"
[13]: https://www.reuters.com/business/whirlpool-shares-tumble-after-revenue-miss-dividend-suspension-2026-05-07/?utm_source=chatgpt.com "Whirlpool shares hit 14-year low after slashing annual targets, suspending dividend"
[14]: https://nypost.com/2024/03/16/target-to-limit-self-checkout-option-to-10-items/?utm_source=chatgpt.com "Target to limit self-checkout to 10 items as stores trend away from the technology amid concerns of theft"
[15]: https://arxiv.org/abs/2410.02888?utm_source=chatgpt.com "Pseudo-Automation: How Labor-Offsetting Technologies Reconfigure Roles and Relationships in Frontline Retail Work"
[16]: https://www.reuters.com/legal/litigation/cannabis-rescheduling-arrives-with-limits-what-dojs-final-order-does-doesnt-do--pracin-2026-05-12/?utm_source=chatgpt.com "Cannabis rescheduling arrives, with limits: What the DOJ's final order does and doesn't do"

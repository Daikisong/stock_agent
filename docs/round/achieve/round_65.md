좋아. **R11 Loop 2까지 끝났으니, 이번은 R12 Loop 2 — 농업·생활서비스·기타**로 넘어간다.

R12는 Theme Tag Map 기준으로 양돈주, 육계주, 배합사료, 대두, 농기계, 종자·비료·농약, 스마트팜, 참치 원양어업, 교육, 취업·일자리, 키즈·유아용품, 전자담배, 주정 같은 테마를 흡수하는 대섹터다. 이 지도에서도 R12는 대부분 **Watch/Red**로 잡혀 있고, 실제 수주·반복계약·판가전가·규제 승인·FCF 전환 전까지 Green을 제한해야 한다고 정리되어 있다.

또 Checkpoint 20 원칙처럼, 수주금액, 정부계약, 규제 승인, recurring revenue, 해지율, CAC, 판가전가, 사료비, 질병 이벤트 같은 값은 실제 확인된 증거만 써야 한다. 빈칸을 추정으로 메우면 R12는 바로 테마주 점수 오염이 생긴다.
서생원식으로도 이 라운드는 “생활 필수”나 “정책 수혜”가 아니라 **EPS/FCF 체급 변화와 밸류에이션 프레임 변화가 실제로 같이 일어나는가**를 봐야 한다.

---

# R12 Loop 2. 농업·생활서비스·기타

## 1. 이번 라운드 대섹터

```text
R12 = 농업·생활서비스·기타
Loop 2 목표 = 필수소비·생활서비스·정책/질병 이벤트와 실제 반복 FCF를 분리
```

이번 회차의 핵심 질문은 이거다.

```text
이 기업은 반복계약·반복매출·판가전가·규제 승인·FCF가 있는가?
아니면 질병, 날씨, 곡물가격, 정책, 저출산, AI 대체, 규제 뉴스로만 움직이는가?
```

R12에서 가장 흔한 오판은 아래다.

```text
1. 스마트팜·수직농장을 기술 narrative만으로 Green 처리
2. 농기계 자율화 기술을 농가 capex cycle 없이 점수화
3. 조류독감·ASF·계란값·돼지고기값 급등을 구조적 EPS로 오판
4. 교육 플랫폼의 반복매출을 AI 대체 리스크 없이 Green 처리
5. 키즈·유아용품을 프리미엄 소비만 보고 저출산 TAM 축소를 무시
6. 생활가전 hardware를 렌탈 반복매출과 섞어서 처리
7. 키오스크·셀프체크아웃을 설치대수만 보고 자동화 Green으로 오판
8. 전자담배·마리화나를 규제 승인/불허가 gate 없이 테마로 점수화
```

---

## 2. 대상 canonical archetype

| canonical archetype                   | Loop 2 정책                                              |
| ------------------------------------- | ------------------------------------------------------ |
| `SMART_FARM_AGRI_TECH`                | Watch-to-Green. 실제 수주·운영계약·unit economics 필요           |
| `AGRI_MACHINERY_PRECISION_CYCLE`      | Watch. 자율농기계 기술보다 농가소득·금리·장비 cycle 확인                  |
| `AGRI_LIVESTOCK_FOOD_COMMODITY`       | Watch/Red. 질병·사료비·곡물·가격 cycle 중심                       |
| `ANIMAL_HEALTH_BIOSECURITY`           | Watch. 정부 비축·반복 접종·승인·주문 필요                            |
| `EDUCATION_SPECIALTY_SERVICES`        | Watch-to-Green. 반복수강·B2B/B2G 계약·CAC·completion rate 필요 |
| `HOME_CHILD_EDUCATION`                | Watch/Red. 저출산·TAM 축소 hard risk                        |
| `HOME_LIVING_APPLIANCE_RENTAL`        | Watch-to-Green. 렌탈 계정·해지율·관리서비스 매출 필요                  |
| `SERVICE_KIOSK_SELF_CHECKOUT`         | Watch. hardware one-off와 유지보수·결제수수료 반복매출 분리            |
| `CONSUMER_REGULATED_PRODUCT`          | Watch. FDA/DEA/국가별 규제 승인·판매범위·반복소비 필요                  |
| `FOOD_INPUT_REGULATED_CYCLE`          | Watch. 주정·식품 input은 원가·판가·규제 확인                        |
| `POLICY_LOCAL_SERVICE_THEME`          | Event/Watch. 정책 발표만 있으면 Stage 1                        |
| `AGRI_DISEASE_EVENT_OVERLAY`          | RedTeam overlay. 조류독감·ASF·질병 one-off                   |
| `AI_EDUCATION_DISRUPTION_OVERLAY`     | RedTeam overlay. Chegg식 AI 대체 리스크                      |
| `REGULATED_CONSUMER_APPROVAL_OVERLAY` | RedTeam overlay. 승인·불허가·청소년 사용·public health           |

---

## 3. deep sub-archetype

```text
SMART_FARM_AGRI_TECH
- 스마트팜
- 수직농장
- 온실 자동화
- 농업 로봇
- 정밀농업 AI
- AI rover
- 농업 데이터 플랫폼
- 운영계약
- 유지보수·SaaS
- unit economics

AGRI_MACHINERY_PRECISION_CYCLE
- 농기계
- 자율주행 트랙터
- 정밀농업 장비
- 농업용 드론
- 장비 교체 cycle
- 농가소득
- 금리·할부금융
- right-to-repair

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
- 질병 이벤트
- 가격 정상화

ANIMAL_HEALTH_BIOSECURITY
- 동물백신
- 조류독감 백신
- ASF 방역
- 정부 비축
- 반복 접종
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

HOME_CHILD_EDUCATION
- 키즈
- 유아용품
- 학습지
- 프리미엄 육아
- 저출산
- 해외 확장

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

CONSUMER_REGULATED_PRODUCT
- 전자담배
- nicotine pouch
- 주정
- 마리화나
- 의료용 cannabis
- FDA authorization
- DEA rescheduling
- 청소년 사용 리스크
- public health regulation
```

---

# 4. 성공사례 / 성공후보

## 4-1. John Deere 자율농기계 — 기술 후보지만 cycle gate 필요

John Deere는 CES 2025에서 자율주행 트랙터, 무인 잔디깎이, 무인 덤프트럭, 과수원용 자율 트랙터를 공개했다. 농업 노동력 부족과 생산성 개선에 대응하는 정밀농업 기술이라는 점에서 `SMART_FARM_AGRI_TECH`와 `AGRI_MACHINERY_PRECISION_CYCLE`의 Stage 1 후보로 볼 수 있다. 다만 자율 농기계가 Green으로 가려면 실제 장비 판매, 농가 ROI, 소프트웨어 attach, 유지보수 매출이 확인되어야 한다. ([The Verge][1])

```text
가격경로 1차 판정:
PRECISION_AGRI_STAGE1_SUCCESS_CANDIDATE

좋은 점:
- 노동력 부족 대응
- 자율주행·센서·AI 기술 적용
- 농약·비료·수확 작업 생산성 개선 가능성
- 장비+소프트웨어 모델 가능성

주의:
- 장비 가격
- 농가소득
- 금리·할부금융
- 실제 adoption rate
- right-to-repair 리스크
```

**Loop 2 교정**

```text
AGRI_MACHINERY_PRECISION_CYCLE:
기술 발표는 Stage 1.
Stage 2는 실제 판매·농가 ROI·software attach.
Stage 3는 반복 SW/서비스 매출이 장비 cycle을 보완할 때만.
```

---

## 4-2. Zoetis 조류독감 백신 — 질병 이벤트가 승인·비축으로 승격되는 경우

Zoetis는 미국 USDA로부터 가금류 조류독감 백신 조건부 승인을 받았다. Reuters는 이 조건부 license가 긴급·특수 상황에서 안전성과 기대 효능을 근거로 부여됐고, USDA가 상업·야생 조류에 퍼진 strain에 맞춘 백신 stockpile을 재구축하려 한다고 보도했다. 이건 단순 질병 뉴스가 아니라 **조건부 승인 + 정부 비축 가능성**이 붙은 Stage 1~2 후보로 볼 수 있다. ([Reuters][2])

```text
가격경로 1차 판정:
ANIMAL_HEALTH_EVENT_TO_CONTRACT_CANDIDATE

좋은 점:
- USDA 조건부 승인
- HPAI 대응 필요성
- 정부 stockpile 가능성
- 동물의약품 유통망

주의:
- emergency license
- 실제 정부 구매 규모 미확인
- outbreak 정상화
- 무역 제한 우려
- one-off stockpile 가능성
```

**Loop 2 교정**

```text
ANIMAL_HEALTH_BIOSECURITY:
질병 뉴스만 있으면 Event/Watch.
조건부 승인 + 정부 비축 + 반복 접종 가능성이 붙으면 Stage 2 후보.
Stage 3는 실제 주문·반복 매출·OPM 확인 후.
```

---

## 4-3. Cal-Maine 계란 가격 cycle — 수익은 가능하지만 structural Green은 아님

Cal-Maine은 조류독감에 따른 공급차질과 계란 가격 급등 속에 2024년 12월~2025년 2월 분기 순이익이 전년 대비 247% 증가한 5.085억 달러를 기록했다. FT는 도매 계란가격이 2025년 2월 dozen당 8.58달러까지 올랐다가 4월 초 3.91달러로 내려왔다고 보도했고, DOJ의 가격담합 조사도 함께 언급했다. 이건 `AGRI_LIVESTOCK_FOOD_COMMODITY`에서 수익이 크게 날 수는 있지만, 구조적 Green이 아니라 **질병·가격 cycle success**로 분류해야 하는 사례다. ([Financial Times][3])

```text
가격경로 1차 판정:
LIVESTOCK_PRICE_CYCLICAL_SUCCESS + REGULATORY_WATCH

좋은 점:
- 공급차질로 가격 급등
- 이익 급증
- 생산능력·인수 효과

주의:
- 가격 정상화
- 조류독감 one-off
- DOJ price-fixing inquiry
- 소비자·정책 반발
```

**Loop 2 교정**

```text
AGRI_LIVESTOCK_FOOD_COMMODITY:
EPS가 크게 뛰어도 대부분 cyclical_success.
Stage 3-Green은 매우 제한.
```

---

## 4-4. Duolingo — 교육 앱은 성공 후보지만 monetization gate가 핵심

Duolingo는 AI speaking 기능 확대와 사용자 성장 우선 전략을 제시했지만, 2026년 Q1과 연간 bookings 전망이 시장 예상보다 낮아 주가가 23% 이상 하락했다. Reuters는 Duolingo가 AI-powered “Video Call with Lily” 기능을 더 낮은 요금제와 무료 사용자에게 확대하면서 단기 bookings와 profitability가 눌릴 것이라고 보도했다. 즉 교육 앱은 사용자 수와 AI 기능만으로 Green이 아니라, **bookings, monetization, AI 비용, margin**이 통과되어야 한다. ([Reuters][4])

```text
가격경로 1차 판정:
EDUCATION_APP_SUCCESS_CANDIDATE_BUT_MONETIZATION_WATCH

좋은 점:
- 대규모 사용자 기반
- AI speaking 기능
- subscription model
- global scale

주의:
- bookings miss
- monetization 후퇴
- AI 기능 비용
- user growth와 profitability trade-off
```

**Loop 2 교정**

```text
EDUCATION_SPECIALTY_SERVICES:
사용자 수·AI 기능은 Stage 1.
Stage 2는 bookings, paid conversion, CAC, margin.
Stage 3는 반복매출 + FCF + AI 대체 방어력.
```

---

## 4-5. Coway 렌탈·관리 모델 — 생활가전이 Green 후보가 되는 조건

Coway는 정수기, 공기청정기, 비데, 매트리스 등을 판매·렌탈·관리하는 기업이고, 한국 최대 정수기 업체로 정리된다. Coway는 말레이시아, 미국, 태국, 인도네시아, 베트남 등 해외 자회사를 보유하고 있어, 단순 hardware 판매보다 렌탈 계정·필터·관리 서비스·해외 계정 확장 모델로 봐야 한다. ([위키백과][5])

```text
가격경로 1차 판정:
RECURRING_HOME_SERVICE_CANDIDATE

좋은 점:
- 렌탈 계정 기반
- 필터·관리 반복매출
- 해외 자회사
- 생활 필수형 서비스

주의:
- 해지율
- 해외 마진
- 경쟁
- 품질 리콜
- 지배구조·자본배분
```

**Loop 2 교정**

```text
HOME_LIVING_APPLIANCE_RENTAL:
생활가전 hardware와 렌탈 반복매출을 완전히 분리.
렌탈 계정·해지율·서비스 매출비중 없으면 Green 금지.
```

---

## 4-6. Juul FDA 승인 — 규제형 소비재가 Stage 2로 승격되는 조건

Juul은 2025년 7월 FDA로부터 tobacco·menthol-flavored e-cigarette device와 refill cartridge 판매 승인을 받았다. Reuters는 이 승인이 2022년 federal ban 이후 큰 반전이며, FDA가 Juul의 데이터를 검토해 public health 기준에서 marketing approval이 적절하다고 판단했다고 보도했다. 이 사례는 `CONSUMER_REGULATED_PRODUCT`에서 **규제 승인 하나가 Stage를 바꿀 수 있음**을 보여준다. ([Reuters][6])

```text
가격경로 1차 판정:
REGULATED_CONSUMER_APPROVAL_STAGE2_CANDIDATE

좋은 점:
- FDA marketing authorization
- 반복소비 가능성
- device + cartridge ecosystem
- 과거 ban 리스크 일부 해소

주의:
- 허가 범위가 tobacco/menthol 중심
- 청소년 사용 논란
- public health regulation
- flavored vape 규제
- 판매·마케팅 제한
```

**Loop 2 교정**

```text
CONSUMER_REGULATED_PRODUCT:
규제 승인 전에는 Watch/Red.
승인 후에도 허가 범위, 청소년 사용, 판매채널, 반복매출을 확인해야 Stage 3 가능.
```

---

# 5. 반례

## 5-1. Bowery shutdown — 수직농장 unit economics hard 4C

Bowery는 7억 달러 이상을 조달한 vertical farming unicorn이었지만 2024년 폐쇄됐다. Axios는 Bowery가 AeroFarms, AppHarvest 같은 실패 사례를 뒤따랐고, 소비자들이 “cleaner produce”에 충분한 프리미엄을 지불하지 않았다고 설명했다. 수직농장은 기술적으로 그럴듯하지만, 전력비·CAPEX·소비자 가격·수요·수율이 맞지 않으면 hard 4C로 간다. ([Axios][7])

```text
가격경로 1차 판정:
VERTICAL_FARMING_UNIT_ECONOMICS_4C

교훈:
스마트팜 기술
≠ Green

4C 조건:
- 에너지비 과다
- premium pricing 실패
- CAPEX 부담
- 소비자 adoption 부족
- 수율·병해 이슈
- debt burden
```

---

## 5-2. AppHarvest Chapter 11 — 스마트팜 SPAC hype 붕괴

AppHarvest는 hydroponics/vertical farming 기업으로 상장했지만, 2023년 Chapter 11 파산보호를 신청했고 보유 greenhouses를 매각했다. 이 사례는 “친환경 농업·대형 온실·스마트팜” 테마가 실제 생산성, 원가, 노동, 안전, cash flow를 통과하지 못하면 상장사 관점에서 hard 4C가 된다는 기준이다. ([위키백과][8])

```text
가격경로 1차 판정:
SMART_FARM_SPAC_HARD_4C

교훈:
온실 CAPEX
≠ 반복 FCF

필수 확인:
- 생산 원가
- energy cost
- 가동률
- 고객계약
- FCF
- debt
```

---

## 5-3. Deere 장비 cycle — 기술이 좋아도 농가 capex가 꺾이면 4C-watch

Deere는 자율농기계와 정밀농업 기술을 갖고 있지만, 2025년 1분기 revenue가 35% 감소했고, 약한 농가소득과 높은 차입비용 때문에 농가가 장비 구매보다 렌탈을 선택하면서 주가가 premarket에서 약 4.5% 하락했다. Reuters는 Deere의 production and precision agriculture segment 매출 감소 전망도 언급했다. ([Reuters][9])

```text
가격경로 1차 판정:
AGRI_MACHINERY_CYCLE_4C_WATCH

교훈:
자율농기계 기술
≠ Green

감점 조건:
- 농가소득 약화
- 고금리
- 장비 구매 둔화
- 렌탈 전환
- tariff uncertainty
```

---

## 5-4. John Deere right-to-repair — 농기계 소프트웨어 lock-in의 규제 리스크

John Deere는 repair software와 장비 수리 접근권 문제로 소송·규제 리스크를 겪었다. Deere는 2026년 right-to-repair class action을 해결하기 위해 9,900만 달러 settlement에 합의했고, AP는 Deere가 장비 수리 소프트웨어와 도구 접근 제한으로 높은 수리비를 유발했다는 주장을 둘러싼 합의라고 보도했다. 이건 농기계가 software lock-in을 갖고 있어도, 그 lock-in이 규제·소송으로 깨질 수 있다는 RedTeam 기준이다. ([AP News][10])

```text
가격경로 1차 판정:
AGRI_MACHINERY_SOFTWARE_LOCKIN_REGULATORY_WATCH

교훈:
software-enabled equipment
≠ 무조건 좋은 lock-in

감점 조건:
- right-to-repair lawsuit
- repair monopoly allegation
- settlement cost
- dealer network conflict
- customer backlash
```

---

## 5-5. Chegg — AI가 교육 서비스를 직접 대체한 hard 4C

Chegg는 생성AI가 기존 교육 서비스 비즈니스모델을 직접 잠식한 대표 반례다. Chegg가 ChatGPT가 신규 고객 성장에 영향을 주고 있다고 인정하자 주가가 크게 급락했고, Investopedia는 당시 주가가 거의 절반 가까이 빠졌다고 보도했다. 이후 Chegg는 Google AI Overviews와 ChatGPT 같은 AI 도구가 traffic과 revenue를 훼손했다며 구조조정과 대규모 감원을 이어갔다. ([Investopedia][11])

```text
가격경로 1차 판정:
AI_EDUCATION_DISRUPTION_HARD_4C

교훈:
교육 플랫폼 반복매출
≠ Green

4C 조건:
- AI가 핵심 서비스를 대체
- traffic decline
- subscriber decline
- layoffs
- strategic review
- enterprise pivot 실패 가능성
```

---

## 5-6. 2U Chapter 11 — 온라인 교육 OPM 모델의 부채·성과 리스크

2U는 온라인 교육·OPM 모델의 대표 반례다. WSJ는 2U가 Chapter 11을 신청했고, 9.45억 달러 부채를 약 4.59억 달러로 줄이는 구조조정을 추진했다고 보도했다. 2U의 시장가치는 2018년 50억 달러 이상에서 파산 신청 당시 약 1,150만 달러 수준까지 무너졌고, 고레버리지·규제변화·경쟁·부채만기가 핵심 부담으로 언급됐다. ([월스트리트저널][12])

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

## 5-7. Whirlpool hardware cycle — 생활가전 hardware는 렌탈과 다르다

Whirlpool은 2026년 실적 전망을 크게 낮추고 배당을 중단했으며, 주가는 14년 저점까지 떨어졌다. Reuters는 고금리, 주택 거래 부진, 소비지출 약화, 에너지 가격 상승으로 교체수요가 줄었고, 회사가 EPS 전망을 7달러에서 3~3.50달러로 낮췄다고 보도했다. 이건 일회성 hardware 판매형 생활가전을 렌탈 반복매출과 섞으면 안 된다는 기준 반례다. ([Reuters][13])

```text
가격경로 1차 판정:
HOME_APPLIANCE_HARDWARE_CYCLE_4C

교훈:
생활가전 hardware 판매
≠ Green

4C 조건:
- replacement demand collapse
- housing turnover weakness
- dividend suspension
- debt reduction pressure
- guidance cut
```

---

## 5-8. 셀프체크아웃 축소 — 키오스크는 설치대수만으로 Green이 아니다

Target은 2024년 전국 약 2,000개 매장에서 self-checkout을 10개 품목 이하로 제한하고 staffed lane을 늘리겠다고 밝혔다. 해당 조치는 고객 경험 개선과 checkout 속도 개선을 명분으로 했지만, 업계 전반에서는 theft와 self-checkout 운영 부담도 중요한 배경으로 언급됐다. ([뉴욕 포스트][14])
또 self-checkout은 실제 자동화라기보다 고객에게 노동을 이전하는 pseudo-automation으로 작동할 수 있고, 직원은 여러 고객 문제 해결·감시·갈등 관리를 동시에 떠안게 된다는 연구도 있다. ([arXiv][15])

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
```

---

## 5-9. Cannabis rescheduling의 한계 — 규제 완화 뉴스와 실제 매출을 분리

2026년 4월 DOJ와 DEA는 일부 cannabis-related substances를 Schedule I에서 Schedule III로 재분류하는 final order를 냈지만, Reuters는 이 조치가 연방 차원의 완전 합법화를 의미하지 않고 주·연방법 충돌도 남아 있다고 설명했다. 의료 cannabis 사업자에는 280E 세금 부담 완화 등 긍정 효과가 있을 수 있지만, recreational operator는 직접 수혜가 제한적이고 DEA 등록 등 compliance가 필요하다. ([Reuters][16])

```text
가격경로 1차 판정:
REGULATED_CONSUMER_POLICY_STAGE1_WATCH

교훈:
규제 완화
≠ Green

필수 확인:
- 실제 허가
- 판매채널
- 세금효과
- 법적 충돌 해소
- 반복매출
- compliance cost
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

Bowery shutdown과 AppHarvest Chapter 11은 스마트팜이 기술 narrative만으로 Green이 될 수 없다는 기준 반례다. ([Axios][7])

---

## 6-2. 농기계 자율화 4B-watch

```text
4B 조건:
- 자율농기계·정밀농업 기술 발표 후 관련주 과열
- 농가소득·금리·장비 교체 cycle이 나쁜데 기술만 반영
- right-to-repair 규제 리스크를 시장이 낮게 봄
```

John Deere의 CES 자율농기계 발표는 좋은 Stage 1이지만, Deere의 매출 둔화와 right-to-repair 리스크는 강한 감점축이다. ([The Verge][1])

---

## 6-3. 조류독감·계란·육계·양돈 4B-watch

```text
4B 조건:
- 조류독감·ASF·공급차질로 계란/육계/양돈 관련주 급등
- 가격 정상화 가능성을 시장이 무시
- 정부조사·가격담합 리스크를 반영하지 않음
```

Cal-Maine의 이익 급증은 수익 가능성을 보여주지만, 계란가격 정상화와 DOJ 조사 리스크가 함께 있다. ([Financial Times][3])

---

## 6-4. AI 교육·성인교육 4B-watch

```text
4B 조건:
- AI 재교육·reskilling narrative로 교육주 valuation 상승
- 실제 completion rate, CAC, B2B 계약, student ROI 미확인
- AI가 오히려 기존 교육 서비스를 대체할 수 있다는 점을 무시
```

Duolingo는 AI 기능 확대와 user growth를 제시했지만 bookings 전망 부진으로 급락했고, Chegg는 ChatGPT가 핵심 서비스 수요를 훼손한 대표 반례다. ([Reuters][4])

---

## 6-5. 렌탈 생활가전 4B-watch

```text
4B 조건:
- 렌탈 계정 증가만 보고 valuation 상승
- 해지율·관리비용·해외 마진·품질 리스크 미확인
- hardware cycle 위험을 시장이 낮게 봄
```

Coway 같은 렌탈 모델은 Watch-to-Green 가능성이 있지만, Whirlpool 사례처럼 일반 생활가전 hardware cycle은 완전히 다른 위험 구조다. ([위키백과][5])

---

## 6-6. 키오스크·셀프체크아웃 4B-watch

```text
4B 조건:
- 인건비 상승·무인화 narrative로 키오스크 관련주 급등
- retailer가 self-checkout을 줄이는 흐름을 무시
- theft/shrink와 customer friction을 반영하지 않음
```

Target의 self-checkout 10-item limit와 pseudo-automation 연구는 키오스크가 설치대수만으로 Green이 될 수 없다는 기준이다. ([뉴욕 포스트][14])

---

## 6-7. 규제형 소비재 4B-watch

```text
4B 조건:
- FDA 승인, cannabis rescheduling 뉴스만으로 관련주 동반 급등
- 실제 허가 범위·판매채널·반복매출·청소년 사용 리스크 미확인
- 규제 반전 가능성을 낮게 봄
```

Juul의 FDA 승인은 Stage 2 후보지만, 허가 범위와 public health regulation을 계속 봐야 한다. Cannabis rescheduling도 완전 합법화가 아니므로 관련주는 정책 뉴스만으로 Green이 아니다. ([Reuters][6])

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

Bowery와 AppHarvest는 수직농장·스마트팜의 hard 4C 기준이다. ([Axios][7])

---

## 7-2. 농기계 capex cycle 하락

```text
4C-watch:
farm_income_weakness
high_borrowing_costs
equipment_rental_instead_of_purchase
tariff_uncertainty
segment_sales_decline
```

Deere의 2025년 revenue 35% 감소와 premarket -4.5% 반응은 농기계가 기술주가 아니라 capex-cycle 기업임을 보여준다. ([Reuters][9])

---

## 7-3. 농기계 software lock-in 규제

```text
4C-watch:
right_to_repair_lawsuit
repair_monopoly_allegation
settlement_cost
dealer_network_conflict
customer_backlash
```

John Deere의 right-to-repair settlement는 농기계 소프트웨어 lock-in이 규제·소송으로 깨질 수 있음을 보여준다. ([AP News][10])

---

## 7-4. 교육 AI disruption

```text
4C:
AI_substitutes_core_service
traffic_decline
subscriber_decline
layoffs
strategic_review
bankruptcy_or_distress
```

Chegg는 ChatGPT 충격 이후 구조조정과 대규모 감원을 이어갔고, 2U는 온라인 교육 OPM 모델의 부채·규제·경쟁 문제로 Chapter 11에 들어갔다. ([Investopedia][11])

---

## 7-5. 생활가전 hardware cycle 붕괴

```text
4C:
replacement_demand_collapse
housing_turnover_weakness
dividend_suspension
guidance_cut
debt_reduction_pressure
```

Whirlpool의 배당 중단, EPS 전망 하향, 14년 저점은 hardware 생활가전의 대표 4C다. ([Reuters][13])

---

## 7-6. 키오스크·셀프체크아웃 후퇴

```text
4C-watch:
retailer_retreat
theft_shrink
customer_friction
employee_workload
one_off_hardware_sales
```

Target의 self-checkout 제한과 pseudo-automation 연구는 키오스크 기업이 설치대수만으로 Stage 3-Green이 될 수 없다는 기준이다. ([뉴욕 포스트][14])

---

## 7-7. 규제형 소비재 불허가·정책 반전

```text
4C-watch:
FDA_ban
limited_authorization_scope
youth_usage_controversy
DEA_registration_failure
state_federal_law_conflict
public_health_backlash
```

Juul은 2022년 ban에서 2025년 승인으로 바뀐 사례이고, cannabis rescheduling도 완전 합법화가 아니라 제한적 정책 변화다. 그래서 규제형 소비재는 승인 전후 모두 hard RedTeam이 필요하다. ([Reuters][6])

---

# 8. 점수비중 보정표 — R12 Loop 2 / v2.0

| canonical archetype                   | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | Loop 2 핵심 감점                                    |
| ------------------------------------- | ------: | ---------: | ---------: | ---------: | --------: | ------: | ---: | ----------------------------------------------- |
| `SMART_FARM_AGRI_TECH`                |      17 |         13 |         12 |          9 |         8 |       0 |    5 | 에너지비, CAPEX, unit economics, 수직농장 실패            |
| `AGRI_MACHINERY_PRECISION_CYCLE`      |      17 |         13 |         10 |         10 |         9 |       1 |    5 | 농가소득, 금리, 장비 cycle, right-to-repair             |
| `AGRI_LIVESTOCK_FOOD_COMMODITY`       |      18 |          9 |         14 |          8 |         7 |       0 |    5 | 질병, 사료비, 가격 정상화, 정부조사                           |
| `ANIMAL_HEALTH_BIOSECURITY`           |      17 |         15 |          8 |         10 |         8 |       0 |    5 | 정부 사용정책, one-off stockpile, outbreak 정상화        |
| `EDUCATION_SPECIALTY_SERVICES`        |      17 |         16 |          5 |         12 |        11 |       2 |    5 | AI 대체, CAC, bookings miss, completion rate      |
| `HOME_CHILD_EDUCATION`                |      15 |         11 |          5 |         10 |         8 |       0 |    5 | 저출산, TAM 축소, 재고                                 |
| `HOME_LIVING_APPLIANCE_RENTAL`        |      18 |         16 |          6 |         12 |        11 |       2 |    5 | 해지율, 해외마진, hardware cycle, 품질 리콜                |
| `SERVICE_KIOSK_SELF_CHECKOUT`         |      16 |         14 |          7 |         11 |         9 |       0 |    5 | theft, 고객불만, retailer retreat, one-off hardware |
| `CONSUMER_REGULATED_PRODUCT`          |      18 |         15 |          8 |         12 |        10 |       0 |    5 | 규제, public health, 허가 범위, 청소년 사용                |
| `FOOD_INPUT_REGULATED_CYCLE`          |      17 |         11 |         12 |          8 |         8 |       0 |    5 | 원가, 판가전가, 규제                                    |
| `POLICY_LOCAL_SERVICE_THEME`          |       5 |          5 |          5 |          8 |         5 |       0 |    3 | 정책 의존, 예산·계약 부재                                 |
| `AGRI_DISEASE_EVENT_OVERLAY`          |    gate |       gate |       gate |       gate |      gate |    gate | gate | 조류독감·ASF·질병 one-off                             |
| `AI_EDUCATION_DISRUPTION_OVERLAY`     |    gate |       gate |       gate |       gate |      gate |    gate | gate | AI 대체, traffic collapse                         |
| `REGULATED_CONSUMER_APPROVAL_OVERLAY` |    gate |       gate |       gate |       gate |      gate |    gate | gate | FDA/DEA 승인·불허가·public health                    |

Loop 2에서 핵심 보정은 이거다.

```text
1. SMART_FARM_AGRI_TECH 점수는 소폭 하향.
   Bowery와 AppHarvest가 unit economics 실패를 강하게 보여줬기 때문.

2. AGRI_MACHINERY_PRECISION_CYCLE은 기술점수보다 cycle 감점을 강화.
   Deere의 매출 둔화와 right-to-repair 리스크 때문이다.

3. ANIMAL_HEALTH_BIOSECURITY는 소폭 상향.
   Zoetis처럼 조건부 승인·정부 stockpile 가능성이 붙는 경우가 있기 때문.

4. EDUCATION_SPECIALTY_SERVICES는 AI disruption overlay를 강화.
   Duolingo는 monetization watch, Chegg는 hard 4C다.

5. HOME_LIVING_APPLIANCE_RENTAL은 Green 가능 유지.
   단, 렌탈 계정·해지율·서비스 매출비중 없으면 hardware cycle로 강등.

6. SERVICE_KIOSK_SELF_CHECKOUT은 점수 하향.
   Target self-checkout 제한과 theft/customer friction 때문이다.

7. CONSUMER_REGULATED_PRODUCT는 승인 후에도 Green 제한.
   Juul·cannabis 모두 허가 범위와 public health gate가 필요하다.
```

---

# 9. stage date 후보

## `SMART_FARM_AGRI_TECH`

```text
Stage 1:
스마트팜 정책, 자율농업, 수직농장, 농업 AI 뉴스

Stage 2:
실제 수주, 운영계약, 반복 유지보수·SaaS 매출, 가동률 확인

Stage 3:
unit economics와 FCF가 확인되고 반복계약이 붙을 때만

Stage 4B:
스마트팜·수직농장 narrative 과열

Stage 4C:
파산, 폐쇄, energy cost, premium pricing 실패, CAPEX 부담
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
정부 구매 종료, 질병 정상화, 백신 미사용, 무역 제한
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
retailer retreat, theft, 고객불만, employee workload, one-off hardware 판매
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

## R12 Loop 2 공통 검증 방식

```text
1. 각 case의 stage1_date, stage2_date, stage3_date를 지정한다.
2. 해당 날짜의 종가를 stage_price로 저장한다.
3. MFE_30D / 90D / 180D / 1Y / 2Y를 계산한다.
4. MAE_30D / 90D / 180D / 1Y를 계산한다.
5. peak_price와 drawdown_after_peak를 계산한다.
6. 농가소득, 장비판매, 상품가격, 질병 이벤트, 반복매출, CAC, 해지율, 규제 이벤트와 가격경로를 비교한다.
```

## Loop 2에서 새로 강제할 판정

```text
SMART_FARM_UNIT_ECONOMICS_ALIGNED:
스마트팜 수주·가동률·에너지비·FCF가 확인된 경우.

VERTICAL_FARMING_4C:
수직농장 폐쇄·파산·프리미엄 가격 실패.

AGRI_MACHINERY_TECH_BUT_CYCLE_WATCH:
자율농기계 기술은 있으나 농가소득·금리·장비판매 둔화.

ANIMAL_HEALTH_EVENT_TO_CONTRACT:
질병 이벤트가 백신 승인·정부 비축·반복 접종으로 승격.

LIVESTOCK_CYCLICAL_SUCCESS:
가격 급등으로 이익은 났지만 구조적 지속성은 낮음.

EDUCATION_RECURRING_ALIGNED:
B2B/B2G 계약·completion rate·CAC·FCF가 통과된 교육 서비스.

EDUCATION_AI_DISRUPTION_4C:
AI가 핵심 서비스를 대체해 traffic·subscriber·revenue가 훼손.

RENTAL_RECURRING_SUCCESS:
렌탈 계정·해지율·관리서비스 매출·FCF가 확인.

HARDWARE_CYCLE_FAILURE:
교체수요 둔화·배당중단·guidance cut으로 무너진 생활가전.

KIOSK_OPERATIONAL_FAILURE:
self-checkout 축소·theft·customer friction 발생.

REGULATED_CONSUMER_APPROVAL_STAGE2:
FDA/DEA 승인으로 Stage 2가 되지만 허가 범위와 public health gate 필요.
```

## 이번 R12 Loop 2에서 우선 검증할 가격 case

| case_id                                     |        stage2 후보일 | 현재 1차 가격판정                              |
| ------------------------------------------- | ----------------: | --------------------------------------- |
| `john_deere_autonomous_agri_ces_case`       |        2025-01-06 | precision agri Stage 1 후보               |
| `deere_farm_equipment_demand_slowdown_case` |        2025-02-13 | -4.5% premarket, cycle 4C-watch         |
| `deere_right_to_repair_settlement_case`     |           2026-04 | software lock-in regulatory watch       |
| `zoetis_bird_flu_vaccine_conditional_case`  |        2025-02-14 | animal health event-to-contract 후보      |
| `calmaine_egg_price_profit_case`            |           2025 Q1 | cyclical success + regulatory watch     |
| `bowery_vertical_farming_shutdown_case`     |        2024-11-05 | vertical farming hard 4C                |
| `appharvest_chapter11_case`                 |        2023-07-24 | smart farm SPAC hard 4C                 |
| `duolingo_ai_strategy_bookings_miss_case`   |        2026-02-26 | -23%, monetization 4C-watch             |
| `chegg_ai_disruption_case`                  | 2023-05 / 2025-10 | AI education hard 4C                    |
| `2u_chapter11_case`                         |        2024-07-25 | online education OPM hard 4C            |
| `coway_rental_recurring_case`               |        계정/해지율 확인일 | recurring home service 후보               |
| `whirlpool_dividend_suspension_case`        |        2026-05-07 | -13%, hardware cycle 4C                 |
| `target_self_checkout_limit_case`           |        2024-03-16 | kiosk operational counterexample        |
| `juul_fda_approval_case`                    |        2025-07-17 | regulated product Stage 2 후보            |
| `cannabis_schedule3_limited_case`           |        2026-05-12 | regulatory watch, not full legalization |

---

# 11. 다음에 에이전트가 채워야 할 price fields

R12 Loop 2에서는 아래 필드를 채우게 해야 한다.

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
equipment_sales_growth
precision_agriculture_revenue
autonomous_equipment_order
software_attach_rate
farmer_financing_cost
tariff_exposure_flag
right_to_repair_flag
repair_settlement_amount

vertical_farming_revenue
vertical_farming_energy_cost
capacity_utilization
unit_economics_margin
premium_pricing_success_flag
yield_loss_flag
chapter11_flag
chapter7_flag
shutdown_flag

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
price_fixing_investigation_flag

education_revenue_growth
bookings_growth
subscription_count
paid_conversion_rate
enterprise_contract_count
completion_rate
student_roi_metric
cac
churn_rate
ai_disruption_flag
traffic_decline_flag
layoff_flag
bankruptcy_flag

rental_accounts
rental_churn
recurring_service_revenue_ratio
filter_service_revenue
hardware_sales_ratio
dividend_suspension_flag
replacement_demand_indicator
housing_turnover_indicator
quality_recall_flag

kiosk_installed_base
maintenance_revenue
payment_fee_revenue
retailer_retreat_flag
self_checkout_limit_flag
theft_shrink_indicator
customer_friction_flag
employee_workload_flag

regulatory_approval_flag
fda_approval_flag
dea_rescheduling_flag
license_scope
youth_usage_risk_flag
public_health_warning_flag
legal_conflict_flag
compliance_cost
sales_channel_authorized_flag

score_price_alignment
price_validation_status
review_notes
```

---

# R12 Loop 2 결론

이번 2회차에서 R12는 더 선명해졌다.

```text
Green 가능:
렌탈·관리 반복매출이 확인된 생활가전
B2B/B2G 반복계약과 FCF가 있는 성인교육·직무교육
정부 비축·반복 접종이 확인된 동물백신
규제 승인 후 판매채널·반복매출이 확인된 규제형 소비재
스마트팜 중 실제 수주·가동률·unit economics·FCF가 확인된 기업

Watch-to-Green:
자율농기계
정밀농업
동물백신
교육·취업서비스
렌탈 생활가전
키오스크·무인화
전자담배·의료 cannabis

Watch/Red:
양돈·육계·계란·사료·대두
수직농장
스마트팜 테마
키즈·유아용품
일회성 생활가전 hardware
self-checkout hardware
주정·식품 input cycle

Hard 4C:
수직농장 폐쇄·파산
농기계 수요 둔화·right-to-repair 규제
조류독감/ASF 가격 정상화
교육 AI 대체
2U식 OPM 파산
Whirlpool식 배당중단·hardware cycle 붕괴
self-checkout 축소·theft·고객불만
규제형 소비재 불허가·허가범위 제한·public health backlash
```

**R12 Loop 2 점수정규화의 핵심 문장:**

> 농업·생활서비스·기타는 “생활 필수”, “정책 수혜”, “질병 이벤트”, “AI 교육”, “무인화”, “규제 완화”라는 이름이 아니라 **반복계약, 반복매출, unit economics, 판가전가, 해지율, CAC, regulatory approval scope, FCF 전환, 실제 가격경로**로 봐야 한다.
> 질병·날씨·곡물·저출산·AI 대체·규제·키오스크 운영마찰이 개입되면 대부분은 `cyclical_success`, `event_to_contract`, `theme_without_unit_economics`, `thesis_break`로 분리해야 한다.

다음 순서는 **R13 — Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리 Loop 2**다.

[1]: https://www.theverge.com/2025/1/6/24334357/john-deere-autonomous-tractor-truck-orchard-mow-ces?utm_source=chatgpt.com "John Deere says its self-driving tractors and trucks will help address labor shortages"
[2]: https://www.reuters.com/business/healthcare-pharmaceuticals/us-grants-conditional-clearance-zoetis-bird-flu-vaccine-poultry-2025-02-14/?utm_source=chatgpt.com "US gives conditional nod to Zoetis' bird flu vaccine for poultry"
[3]: https://www.ft.com/content/b05d9645-8e1b-4f3b-b5da-a853bd51e00d?utm_source=chatgpt.com "Largest US egg seller reports soaring profits amid price-fixing inquiry"
[4]: https://www.reuters.com/business/finance/duolingo-prioritizes-user-growth-over-monetization-forecasts-softer-bookings-2026-02-26/?utm_source=chatgpt.com "Duolingo shares drop after bookings outlook lags estimates amid strategy shift"
[5]: https://en.wikipedia.org/wiki/Coway_%28company%29?utm_source=chatgpt.com "Coway (company)"
[6]: https://www.reuters.com/sustainability/boards-policy-regulation/fda-approves-juuls-tobacco-menthol-e-cigarettes-2025-07-17/?utm_source=chatgpt.com "FDA approves Juul's tobacco and menthol e-cigarettes"
[7]: https://www.axios.com/2024/11/05/bowery-vertical-farming-close?utm_source=chatgpt.com "Vertical farming \"unicorn\" Bowery to shut down"
[8]: https://en.wikipedia.org/wiki/AppHarvest?utm_source=chatgpt.com "AppHarvest"
[9]: https://www.reuters.com/business/deere-reports-lower-profit-muted-farm-equipment-demand-2025-02-13/?utm_source=chatgpt.com "Deere misses revenue estimates on subdued farm equipment demand"
[10]: https://apnews.com/article/595d4b089689cd94418991326275b68d?utm_source=chatgpt.com "Deere & Co agrees to pay $99 million to settle 'right to repair' lawsuit"
[11]: https://www.investopedia.com/chegg-shares-plunge-after-company-warns-that-chatgpt-is-impacting-growth-7487968?utm_source=chatgpt.com "Chegg Shares Plunge After Company Warns That ChatGPT Is Impacting Growth"
[12]: https://www.wsj.com/business/2u-ed-tech-company-files-chapter-11-bankruptcy-24ca1017?utm_source=chatgpt.com "2U, Once a Giant in Online Education, Files for Chapter 11 Bankruptcy"
[13]: https://www.reuters.com/business/whirlpool-shares-tumble-after-revenue-miss-dividend-suspension-2026-05-07/?utm_source=chatgpt.com "Whirlpool shares hit 14-year low after slashing annual targets, suspending dividend"
[14]: https://nypost.com/2024/03/16/target-to-limit-self-checkout-option-to-10-items/?utm_source=chatgpt.com "Target to limit self-checkout to 10 items as stores trend away from the technology amid concerns of theft"
[15]: https://arxiv.org/abs/2410.02888?utm_source=chatgpt.com "Pseudo-Automation: How Labor-Offsetting Technologies Reconfigure Roles and Relationships in Frontline Retail Work"
[16]: https://www.reuters.com/legal/litigation/cannabis-rescheduling-arrives-with-limits-what-dojs-final-order-does-doesnt-do--pracin-2026-05-12/?utm_source=chatgpt.com "Cannabis rescheduling arrives, with limits: What the DOJ's final order does and doesn't do"

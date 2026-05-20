좋아. **R6 Loop 3까지 끝났으니, 이번은 R7 Loop 3 — 바이오·헬스케어·의료기기**로 넘어간다.

R7은 CDMO, CMO, 원료의약품, CRO, 바이오시밀러, 의료AI, 원격의료, 유전체검사, AI 신약개발, 이중항체, 세포치료제, 줄기세포, 치매·비만·탈모 치료제, 보톡스, 임플란트, 미용기기, 수술용 로봇, 전염병 진단을 흡수하는 대섹터다. Theme Tag Map 기준으로도 이 섹터는 **pre-revenue biotech은 Green 거의 금지**, **royalty/commercialization biotech은 실제 매출화·로열티 필요**, **CDMO/medical device는 장기계약·반복매출이면 Green 가능**으로 갈라야 한다.

Checkpoint 20 원칙도 그대로 적용한다. 계약금액, 계약기간, 가동률, 처방량, 보험·수가, 매출 대비 계약금액, OP YoY, 임상 단계, cash runway 같은 값은 실제 공시·리포트·기사에서 확인될 때만 써야 한다. 바이오는 특히 “승인”, “AI”, “임상”, “세계 최초” 같은 말만으로 점수가 부풀기 쉬우므로, 없는 값을 추정으로 채우면 false-positive가 커진다.

서생원식으로 보면 R7의 질문은 “신약이 좋아 보이나?”가 아니라 **허가·임상·논문·AI 성능이 실제 처방, 매출, 반복계약, 수가, FCF로 넘어가서 EPS 체급과 밸류에이션 프레임을 바꾸는가**다. 허가는 시작일 뿐이고, 상업화가 안 되면 4C다.

---

# R7 Loop 3. 바이오·헬스케어·의료기기

## 1. 이번 라운드 대섹터

```text
R7 = 바이오·헬스케어·의료기기
Loop 3 목표 = 허가·임상·AI 논문·플랫폼 narrative와 실제 상업화·반복매출·FCF를 완전히 분리
```

이번 회차의 핵심 질문은 이거다.

```text
이 회사는 실제로 돈을 벌고 있는가?
아니면 허가, 임상, 논문, AI, TAM, 기술이전 기대만 있는가?
```

R7에서 가장 위험한 오판은 이거다.

```text
FDA 승인
= Green
```

실제로는 이렇게 갈라야 한다.

```text
좋은 구조 후보:
CDMO 장기계약 + capacity utilization + 고객 다변화 + OPM/FCF
의료기기 반복시술 + 소모품 + 해외 허가 + OPM
임플란트·미용기기 수출 + ASP 방어 + 반복수요
GLP-1 상업화 + 처방량 + 보험/가격 + OP/EPS
의료AI 병원도입 + 수가 + 반복매출
수술로봇 installed base + procedure growth + instruments/accessories

위험한 후보:
허가만 있고 uptake 없는 유전자치료제
AI 신약개발 platform hype
논문 성능만 있는 의료AI
biosimilar 승인만 있고 PBM/보험/처방전환 없는 경우
GLP-1 TAM만 있고 가격·경쟁·조제약 압박을 무시한 경우
DTC telehealth CAC/규제/compounding 리스크
전염병 진단 one-off
```

---

## 2. 대상 canonical archetype

| canonical archetype                  | Loop 3 정책                                                  |
| ------------------------------------ | ---------------------------------------------------------- |
| `CDMO_HEALTHCARE_CONTRACT`           | Green 가능. 장기계약·capacity·가동률·고객 다변화 필요                      |
| `CRO_CLINICAL_SERVICE`               | Watch-to-Green. backlog·고객 R&D 예산·biotech funding cycle 확인 |
| `BIOSIMILAR_COMMERCIALIZATION`       | Watch-to-Green. 허가보다 PBM/보험·처방전환·마진 필요                     |
| `BIOSIMILAR_ORIGINATOR_DEFENSE`      | Watch. patent cliff와 후속 신약 전환 분리                           |
| `OBESITY_GLP1_COMMERCIALIZATION`     | Green 가능하지만 4B/4C 강함. 처방량·보험·가격·경쟁 필요                      |
| `GLP1_TELEHEALTH_CHANNEL`            | High-risk Watch. DTC·compounding·branded pivot·CAC 확인      |
| `GENE_THERAPY_RARE_DISEASE`          | Watch/Red. 승인 후 상업화·환급·cash runway 없으면 Green 금지            |
| `AI_DRUG_DISCOVERY_PLATFORM`         | Watch/Red. AI 플랫폼보다 milestone·임상·승인 가능성 필요                 |
| `DIGITAL_HEALTHCARE_AI`              | Watch-to-Green. 외부검증 + 병원도입 + 수가 + 반복매출 필요                 |
| `DIGITAL_HEALTHCARE_REMOTE_MEDICINE` | Watch. 규제·수가·unit economics 필요                             |
| `TELEHEALTH_BEHAVIORAL_HEALTH`       | Watch/Red. CAC·privacy·impairment 리스크 큼                    |
| `PHARMA_CHANNEL_AND_PRIVACY_RISK`    | RedTeam gate. 조제약·광고·개인정보·품질 리스크                           |
| `MEDICAL_DEVICE_HEALTHCARE_EXPORT`   | Green 가능. 수출국·반복시술·소모품·OPM 확인                              |
| `MEDICAL_DEVICE_DENTAL_IMPLANT`      | Green 가능. 다만 VBP·가격통제 감시                                   |
| `SURGICAL_ROBOT_INSTALLED_BASE`      | Green 가능. installed base·procedure growth·소모품 매출 필요        |
| `BOTULINUM_AESTHETIC_REGULATED`      | Watch-to-Green. 허가·안전채널·반복시술 필요                            |
| `DIAGNOSTICS_INFECTIOUS_DISEASE`     | Red/Watch. one-off 진단 수요와 구조적 진단 플랫폼 분리                    |
| `COMMERCIALIZATION_FAILURE_OVERLAY`  | RedTeam gate. 승인 후 매출화 실패                                  |
| `REIMBURSEMENT_ACCESS_OVERLAY`       | RedTeam overlay. 보험·PBM·수가·환급 실패                           |
| `DEVICE_SAFETY_COUNTERFEIT_OVERLAY`  | RedTeam overlay. 위조품·무허가·리콜·제품안전                           |

---

## 3. deep sub-archetype

```text
CDMO_HEALTHCARE_CONTRACT
- CDMO
- CMO
- 원료의약품
- 항체 생산
- ADC 생산
- mRNA·세포치료 생산
- 미국 생산거점
- long-term manufacturing contract
- capacity utilization
- 고객사 다변화
- tariff hedge

CRO_CLINICAL_SERVICE
- CRO
- 임상시험수탁
- preclinical service
- lab service
- backlog
- 고객사 R&D 예산
- biotech funding cycle
- high-rate funding crunch

BIOSIMILAR_COMMERCIALIZATION
- Humira biosimilar
- Stelara biosimilar
- Prolia/Xgeva biosimilar
- PBM 등재
- 보험 커버리지
- 처방전환
- 가격경쟁
- interchangeability
- patent litigation

OBESITY_GLP1_COMMERCIALIZATION
- Wegovy
- Ozempic
- Zepbound
- Foundayo / orforglipron
- oral GLP-1
- compounded GLP-1
- direct-to-consumer channel
- weekly scripts
- insurance coverage
- gross-to-net discount
- price pressure

GENE_THERAPY_RARE_DISEASE
- 희귀질환
- 유전자치료제
- 고가 치료제
- 환자 모집
- 보험·환급
- 제조 안정성
- cash runway
- going concern
- discounted take-private

AI_DRUG_DISCOVERY_PLATFORM
- AI 신약개발
- 후보물질 발굴
- 임상 진입
- big pharma partnership
- milestone
- cash runway
- platform hype
- approved drug 없음

DIGITAL_HEALTHCARE_AI
- 의료영상 AI
- mammography AI
- DBT
- 병원 workflow
- 외부검증
- subgroup performance
- 수가/보험
- 의료책임
- deployment revenue

SURGICAL_ROBOT_INSTALLED_BASE
- da Vinci
- Ion
- installed base
- procedure growth
- instruments/accessories
- system placement
- procedure mix
- bariatric slowdown
- capital equipment cycle

MEDICAL_DEVICE_HEALTHCARE_EXPORT
- 미용기기
- 보톡스
- 임플란트
- 수술용 로봇
- 반복시술
- 소모품
- 해외 허가
- ASP/OPM
- counterfeit/safety

PHARMA_CHANNEL_AND_PRIVACY_RISK
- telehealth drug channel
- compounded drug
- branded drug transition
- FDA warning
- legal settlement
- revenue recognition
- CAC
- 개인정보
- 광고 규제
```

---

# 4. 성공사례

## 4-1. Samsung Biologics 미국 생산거점 — `CDMO_HEALTHCARE_CONTRACT`

Samsung Biologics는 GSK로부터 미국 Rockville 소재 Human Genome Sciences 생산시설을 2.8억 달러에 인수하기로 했다. 이 시설은 60,000L drug substance capacity를 갖고 있고, Samsung Biologics의 첫 미국 생산거점이 된다. Reuters는 이 거래가 미국 장기 수요 대응과 tariff risk에 대응하는 전략이라고 설명했고, 발표 당시 주가는 0.4% 하락해 코스피 2% 상승을 밑돌았다. 즉 전략적으론 좋지만, 가격경로는 즉시 aligned라고 보기 어렵다. ([Reuters][1])

```text
가격경로 1차 판정:
CDMO_STRATEGIC_CAPACITY_CANDIDATE / PRICE_ALIGNMENT_DELAYED

좋은 점:
- 첫 미국 생산거점
- 60,000L capacity
- 미국 수요 대응
- tariff hedge
- CDMO 글로벌 고객 접근성 강화

주의:
- 발표 직후 주가 부진
- 인수 후 가동률 필요
- 고객계약 필요
- 추가 CAPEX
- 미국 운영비·인건비
```

**Loop 3 교정**

```text
CDMO_HEALTHCARE_CONTRACT:
capacity 확보는 Stage 1.5~2.
Stage 3는 가동률 + 고객계약 + OPM/FCF 전환 확인 후.
```

---

## 4-2. Samsung Biologics 구조 reference — CDMO가 Green 후보가 되는 이유

CDMO는 R7에서 드물게 숫자로 검증 가능한 Green 후보군이다. Samsung Biologics는 항체, 이중항체, ADC, mRNA vaccine 등 대규모 바이오의약품 생산 서비스를 제공하는 CDMO로 정리되며, 글로벌 제약사들과 협력해 온 구조를 갖고 있다. 하지만 이 영역도 “공장 증설”만으로는 부족하고, 실제 장기 제조계약, capacity utilization, 고객 다변화, OP margin, FCF conversion이 붙어야 한다. ([위키백과][2])

```text
가격경로 1차 판정:
CDMO_STRUCTURAL_REFERENCE

Stage 3 조건:
- 장기 제조계약
- capacity utilization 상승
- 고객사 다변화
- 고부가 생산 mix
- OP margin / FCF 개선
```

---

## 4-3. Intuitive Surgical — `SURGICAL_ROBOT_INSTALLED_BASE`

수술용 로봇은 R7에서 단순 의료기기보다 더 좋은 구조가 나올 수 있다. Intuitive Surgical은 Q1 2026에 da Vinci와 Ion system procedure가 전년 대비 17% 증가했고, 매출은 23% 증가한 27.7억 달러, instruments/accessories 매출은 23% 증가한 16.9억 달러였다. 또 2026년 procedure growth guidance를 13.5~15.5%로 올렸고, 주가는 실적 후 7.2% 상승했다. 이 구조는 **installed base → procedure growth → 소모품/기구 반복매출**이 확인되는 좋은 의료기기 reference다. ([Investors][3])

```text
가격경로 1차 판정:
SURGICAL_ROBOT_RECURRING_CONSUMABLE_SUCCESS

좋은 점:
- procedure growth
- installed base
- instruments/accessories 반복매출
- guidance 상향
- 주가 +7.2%
- capital equipment + recurring consumable hybrid

주의:
- system placement cycle
- 병원 CAPEX
- bariatric procedure slowdown
- GLP-1이 일부 수술 수요를 잠식할 가능성
- medtech valuation compression
```

**Loop 3 교정**

```text
SURGICAL_ROBOT_INSTALLED_BASE를 별도 archetype으로 둔다.

Stage 2:
installed base + procedure growth + system placement.

Stage 3:
instruments/accessories recurring revenue + OPM/FCF 개선.
```

---

## 4-4. Straumann / 치아·임플란트 — `MEDICAL_DEVICE_DENTAL_IMPLANT`

Straumann은 치과 임플란트·디지털 치과 쪽에서 좋은 의료기기 reference다. 2025년 매출은 26.1억 스위스프랑으로 예상치를 웃돌았고, 2026년 high single-digit sales growth를 제시했다. 주가는 장중 최대 6% 상승했다. 다만 중국 VBP, 즉 volume-based procurement가 가격을 낮추고 현지 생산품을 우대할 가능성이 있어, 임플란트는 Green 가능이지만 가격통제 overlay를 반드시 붙여야 한다. ([Reuters][4])

```text
가격경로 1차 판정:
DENTAL_IMPLANT_ALIGNED_CANDIDATE + VBP_WATCH

좋은 점:
- 매출 예상 상회
- 지역 다변화
- 반복시술 수요
- 디지털 치과·임플란트 소모품/서비스 확장 가능
- 주가 반응 양호

주의:
- 중국 VBP 가격통제
- ASP 하락
- 현지 제조 우대
- 경쟁 심화
```

**Loop 3 교정**

```text
MEDICAL_DEVICE_DENTAL_IMPLANT:
Green 가능 유지.
하지만 VBP/가격통제 flag가 켜지면 Valuation과 Visibility 감점.
```

---

## 4-5. Lilly Foundayo — `OBESITY_GLP1_COMMERCIALIZATION`

Eli Lilly의 oral GLP-1 비만치료제 Foundayo, 즉 orforglipron은 2026년 4월 FDA 승인을 받았다. Reuters는 Foundayo가 임상에서 12~15% 체중감량을 보였고, LillyDirect에서 월 149달러로 판매되며, Novo의 Wegovy pill과 경쟁하게 된다고 보도했다. 승인 뉴스에서 Lilly 주가는 6% 올랐다. 이는 `OBESITY_GLP1_COMMERCIALIZATION`의 강한 Stage 2 후보지만, Stage 3는 처방량·보험·가격·OP/EPS가 따라와야 한다. ([Reuters][5])

```text
가격경로 1차 판정:
GLP1_ORAL_APPROVAL_STAGE2_CANDIDATE

좋은 점:
- FDA 승인
- oral GLP-1 편의성
- 가격 접근성
- LillyDirect channel
- 주가 +6%
- 글로벌 제출/확장 가능성

주의:
- 보험 커버리지
- Wegovy pill first-mover
- 주간 처방량
- 가격경쟁
- boxed warning / safety
```

**Loop 3 교정**

```text
OBESITY_GLP1_COMMERCIALIZATION:
FDA approval = Stage 2.
Stage 3 = weekly scripts + insurance coverage + OP/EPS revision + price defense.
```

---

## 4-6. Foundayo 처방량과 유지요법 — 성공 후보지만 script gate 필요

Foundayo는 4주차에 미국에서 7,335건 처방을 기록했지만, Q2 컨센서스 매출 1.6억 달러를 맞추려면 주당 약 22,000건 처방이 필요하다는 분석이 나왔다. 반면 Lilly의 late-stage trial에서는 주사 GLP-1에서 Foundayo로 전환한 환자들이 1년 동안 체중을 많이 되찾지 않았고, semaglutide 전환군은 52주차에 기존 감량의 79.3%, tirzepatide 전환군은 74.7%를 유지했다. 즉 장기 유지요법 구조는 좋지만, 초반 처방량은 아직 Stage 3를 보장하지 않는다. ([Reuters][6])

```text
가격경로 1차 판정:
GLP1_MAINTENANCE_CANDIDATE_BUT_SCRIPT_GATE_NEEDED

좋은 점:
- maintenance therapy 근거
- oral convenience
- 장기 obesity management 시장
- telehealth channel 확장

주의:
- 4주차 처방 7,335건은 modest
- 컨센서스 달성에는 주당 22,000건 필요
- telehealth prescription tracking gap
- price/insurance sensitivity
```

**Loop 3 교정**

```text
GLP-1 score는 TAM으로 주면 안 된다.

필수 필드:
weekly_scripts
script_growth_rate
insurance_coverage
gross_to_net_discount
monthly_price
OP/EPS revision
```

---

## 4-7. Lunit / 의료AI 외부검증 — `DIGITAL_HEALTHCARE_AI`

Lunit INSIGHT DBT 모델을 163,449건 screening mammography exams로 외부검증한 연구는 전체 AUC 0.91, recall 0.73을 보고했다. 하지만 non-invasive cancer, calcifications, dense breast tissue subgroup에서는 성능이 낮아져, 의료AI 도입에는 평균 AUC뿐 아니라 subgroup performance와 임상 deployment 리스크를 같이 봐야 한다. ([arXiv][7])

```text
가격경로 1차 판정:
CLINICAL_VALIDATION_CANDIDATE / COMMERCIALIZATION_UNPROVEN

좋은 점:
- 대규모 외부검증
- 전체 AUC 0.91
- DBT workflow 개선 가능성
- 의료영상 AI validation evidence

주의:
- subgroup performance
- 병원 도입
- 수가/보험
- 반복매출
- 의료책임
```

**Loop 3 교정**

```text
DIGITAL_HEALTHCARE_AI:
논문·AUC = Stage 1~2 evidence.
Stage 3 = 병원도입 + reimbursement code + recurring revenue + workflow lock-in.
```

---

## 4-8. Biosimilar 접근성 — 승인보다 처방전환이 핵심

Boehringer Ingelheim과 GoodRx는 Humira biosimilar를 정가 대비 92% 할인된 cash-pay 가격으로 제공하기로 했다. 그러나 biosimilar는 허가·할인만으로 충분하지 않다. 초기 Humira biosimilar demand가 느렸고, interchangeable approval이 있어도 PBM incentive, 보험, 의사·환자 전환이 따라오지 않으면 매출화가 느릴 수 있다. ([Axios][8])

```text
가격경로 1차 판정:
BIOSIMILAR_ACCESS_CANDIDATE_BUT_UPTAKE_WATCH

좋은 점:
- 92% discount
- 접근성 개선
- interchangeable biosimilar
- pharmacy substitution 가능성

주의:
- PBM incentive
- 보험 등재
- 처방전환 속도
- 가격경쟁으로 마진 압박
```

**Loop 3 교정**

```text
BIOSIMILAR_COMMERCIALIZATION:
허가와 가격할인만으로 Green 금지.
PBM/보험 등재 + 처방전환 + 마진 방어가 Stage 3 조건.
```

---

# 5. 반례

## 5-1. Novo Nordisk — GLP-1도 4B에서 4C로 갈 수 있다

Novo Nordisk는 GLP-1 시장의 대표 성장기업이지만, 2026년 sales와 operating profit이 5~13% 감소할 수 있다고 경고하자 주가가 16% 하락했고 약 500억 달러 시가총액이 사라졌다. Reuters는 미국 가격 하락 압박과 반복된 실망감이 핵심이라고 설명했다. ([Reuters][9])

```text
가격경로 1차 판정:
GLP1_GROWTH_MARKET_4B_TO_4C

교훈:
거대한 TAM
≠ Green 유지

4C 조건:
- price cut
- competition
- insurance/reimbursement pressure
- compounded/generic alternatives
- sales/profit decline
```

**Loop 3 교정**

```text
OBESITY_GLP1_COMMERCIALIZATION:
EPS/FCF 점수는 높게 둘 수 있지만,
price pressure와 competition penalty를 강하게 둔다.
```

---

## 5-2. Hims & Hers — GLP-1 telehealth channel의 고변동성

Hims & Hers는 compounded GLP-1에서 branded Wegovy 등으로 전환하면서 Q1 실적에서 예상 밖 손실을 냈고, 주가가 11% 하락했다. Reuters는 compounded drug에서 branded drug으로 전환하는 과정에서 restructuring cost, semaglutide ingredient write-down, legal cost, revenue recognition timing 문제가 발생했다고 보도했다. ([Reuters][10])

또 Hims는 Novo와 legal dispute를 해결하고 branded Wegovy·Ozempic을 팔기로 하면서 주가가 36% 이상 급등한 사례도 있다. 이 구조는 **채널 이벤트는 가격반응이 크지만, 장기 Green은 margin·CAC·legal risk·revenue recognition이 통과되어야 한다**는 뜻이다. ([AP News][11])

```text
가격경로 1차 판정:
GLP1_TELEHEALTH_CHANNEL_HIGH_VOLATILITY

좋은 점:
- telehealth distribution channel
- direct-to-consumer growth
- branded drug partnership 가능성

주의:
- compounded → branded 전환 비용
- CAC
- revenue recognition
- legal cost
- margin compression
```

---

## 5-3. Compounded GLP-1 crackdown — `PHARMA_CHANNEL_AND_PRIVACY_RISK`

Novo Nordisk는 Hims의 compounded Wegovy pill 계획에 대해 법적 조치를 예고했고, FDA는 GLP-1 성분을 사용한 compounded drug에 대해 안전·품질·연방법 위반 우려를 들어 단속 방침을 밝혔다. Hims는 이후 compounded semaglutide pill 제공을 중단했다. ([Reuters][12])

```text
가격경로 1차 판정:
COMPOUNDED_GLP1_REGULATORY_4C_WATCH

교훈:
비만치료제 수요가 커도 유통채널이 회색이면 Green 금지.

4C 조건:
- FDA crackdown
- unapproved copycat drug
- patent litigation
- DOJ referral risk
- quality/safety concern
```

---

## 5-4. Bluebird bio — 승인 후 상업화 실패

Bluebird bio는 승인된 유전자치료제를 갖고 있었지만 severe cash crunch로 Carlyle·SK Capital에 주당 3달러에 비상장화되기로 했고, 이 가격은 직전 종가 대비 57.4% 할인된 수준이었다. 발표 후 주가는 36% 하락했고, Reuters는 gene therapy uptake가 느렸으며 2024년 말 기준 57명만 세 치료제 중 하나를 시작했다고 보도했다. ([Reuters][13])

```text
가격경로 1차 판정:
GENE_THERAPY_COMMERCIALIZATION_FAILURE_HARD_4C

교훈:
FDA 승인
≠ 상업화
≠ EPS/FCF

4C 조건:
- slow uptake
- reimbursement uncertainty
- cash crunch
- going concern
- discounted take-private
```

**Loop 3 교정**

```text
GENE_THERAPY_RARE_DISEASE:
approval_status는 필요조건일 뿐.
patient_uptake, reimbursement_status, commercial_revenue, cash_runway가 없으면 Green 금지.
```

---

## 5-5. Charles River — CRO도 funding cycle에서 자유롭지 않다

Charles River Laboratories는 biotech 고객들의 funding crunch가 이어지면서 2024년 전망을 낮췄고, 주가는 premarket에서 15% 하락했다. 회사는 drug discovery·development service demand가 하반기에 개선될 것으로 보지 않는다고 밝혔고, 연간 매출 전망도 기존 증가에서 2.5~4.5% 감소로 낮췄다. ([Reuters][14])

```text
가격경로 1차 판정:
CRO_FUNDING_CYCLE_4C_WATCH

교훈:
CRO 반복계약
≠ 완전한 Green

감점 조건:
- biotech funding crunch
- 고객 R&D 예산 삭감
- backlog slowdown
- forecast cut
- high-rate environment
```

---

## 5-6. Teladoc / BetterHelp — telehealth DTC 모델의 실패

Teladoc은 BetterHelp 관련 7.9억 달러 impairment를 기록하고 연간·장기 전망을 철회했으며, 주가는 13% 하락해 record low를 기록했다. Reuters는 BetterHelp의 revenue decline, customer acquisition expense 증가, DTC mental health model의 성장 둔화가 핵심 문제라고 보도했다. ([Reuters][15])

```text
가격경로 1차 판정:
TELEHEALTH_DTC_FAILURE_4C

교훈:
원격의료 수요
≠ 지속가능한 business model

4C 조건:
- CAC increase
- impairment
- forecast withdrawal
- DTC demand slowdown
- privacy/advertising risk
```

---

## 5-7. AI 신약개발 platform hype — Recursion / Exscientia

Recursion은 Exscientia를 6.88억 달러 all-stock deal로 인수해 AI-driven drug discovery 역량과 pipeline을 강화하려 했다. Reuters는 합병 법인이 약 8.5억 달러 cash를 보유해 3년 운영을 지원할 수 있다고 보도했다. 하지만 이는 AI 신약개발의 잠재력을 보여주는 동시에, **cash runway는 필요조건이지 승인약·상업화·EPS의 충분조건이 아니다**라는 기준이 된다. ([Reuters][16])

```text
가격경로 1차 판정:
AI_DRUG_PLATFORM_WATCH

교훈:
AI 신약개발 플랫폼
≠ Green

필수 확인:
- big pharma milestone
- 임상 진입
- 임상 성공
- 승인 가능성
- commercial revenue
```

---

## 5-8. Botox counterfeit / safety risk

FDA는 Botox와 유사한 counterfeit 또는 unapproved injectable wrinkle-smoothing products를 판매한 18개 웹사이트에 warning letters를 보냈다. AP는 FDA가 부상과 toxic side effects 보고 이후 조치했고, Botox류 제품은 boxed warning을 갖고 있으며 호흡·삼킴에 영향을 줄 수 있는 위험도 있다고 보도했다. ([AP News][17])

```text
가격경로 1차 판정:
AESTHETIC_SAFETY_REGULATORY_4C_WATCH

교훈:
보톡스·미용시술 반복수요
≠ 안전채널 면제

4C 조건:
- counterfeit product
- unapproved injectable
- FDA warning
- injury reports
- licensed-channel failure
```

---

# 6. 4B-watch 사례

## 6-1. GLP-1 obesity market 4B-watch

```text
4B 조건:
- 비만치료제 시장규모 narrative가 과밀
- Lilly/Novo 목표가와 valuation이 처방량보다 먼저 상승
- 가격·보험·compounded/generic risk를 시장이 무시
- 실적 하향 하나로 큰 drawdown 발생
```

Novo의 16% 급락과 500억 달러 시총 증발은 GLP-1도 TAM만으로 Green 유지가 안 된다는 기준이다. ([Reuters][9])

---

## 6-2. Oral GLP-1 launch 4B-watch

```text
4B 조건:
- oral GLP-1 편의성 narrative로 valuation 상승
- 초기 scripts가 낮은데 장기 TAM만 반영
- 보험·가격·telehealth tracking gap을 시장이 무시
```

Foundayo는 approval과 maintenance data가 좋지만, 4주차 처방 7,335건과 Q2 consensus 달성에 필요한 weekly scripts gap은 반드시 가격검증에 넣어야 한다. ([Reuters][6])

---

## 6-3. CDMO capacity premium 4B-watch

```text
4B 조건:
- CDMO capacity 확장만으로 valuation 상승
- 실제 고객계약·가동률·OPM 확인 전 가격이 먼저 감
- 미국 생산거점·tariff hedge narrative가 과밀
```

Samsung Biologics의 미국 생산거점 인수는 전략적이지만, 발표 당일 주가는 0.4% 하락했고 시장을 이기지 못했다. 전략과 즉시 가격경로를 분리해야 한다. ([Reuters][1])

---

## 6-4. 의료기기·임플란트 4B-watch

```text
4B 조건:
- 임플란트·미용기기 수출 성장 narrative가 과밀
- 중국 VBP·가격통제 리스크를 낮게 봄
- ASP 하락보다 수요 증가만 반영
```

Straumann은 실적과 가이던스가 좋았지만, 중국 VBP 불확실성은 계속 남아 있다. ([Reuters][4])

---

## 6-5. 의료AI 4B-watch

```text
4B 조건:
- AI 의료영상 논문·AUC 수치만으로 관련주 급등
- 병원 도입·수가·반복매출 없음
- subgroup performance와 책임소재를 무시
```

Lunit DBT 외부검증은 의미 있는 clinical evidence지만, subgroup risk와 clinical deployment 문제를 동시에 보여준다. ([arXiv][7])

---

## 6-6. Biosimilar 4B-watch

```text
4B 조건:
- biosimilar approval만으로 관련주 급등
- PBM/보험/처방전환 확인 전 가격이 먼저 감
- 할인율은 큰데 마진 방어를 확인하지 않음
```

Humira biosimilar는 92% discount가 있어도 adoption은 PBM·보험·처방전환 구조를 통과해야 한다. ([Axios][8])

---

## 6-7. 수술로봇 4B-watch

```text
4B 조건:
- installed base와 procedure growth를 시장이 모두 인정
- system placement와 recurring consumables가 이미 valuation에 반영
- GLP-1이 일부 bariatric procedures를 줄일 가능성을 낮게 봄
```

Intuitive Surgical은 procedure growth와 instruments/accessories 매출이 좋아 좋은 성공 후보지만, bariatric slowdown과 hospital capex cycle은 감시해야 한다. ([Investors][3])

---

# 7. 4C-thesis-break 사례

## 7-1. Gene therapy cash crunch

```text
4C:
cash_crunch
slow_uptake
reimbursement_uncertainty
commercialization_failure
discounted_take_private
going_concern_risk
```

Bluebird는 유전자치료제 승인 후에도 상업화와 현금흐름이 따라오지 않으면 어떻게 무너지는지 보여주는 기준 사례다. ([Reuters][13])

---

## 7-2. GLP-1 price / competition collapse

```text
4C-watch:
price_cut
competition
compounded_alternatives
generic_pressure
insurance/reimbursement risk
sales/profit decline
```

Novo의 2026년 sales·operating profit 감소 경고와 주가 16% 하락은 GLP-1의 4B→4C 전환 기준이다. ([Reuters][9])

---

## 7-3. GLP-1 telehealth channel break

```text
4C-watch:
FDA crackdown
illegal mass compounding allegation
unapproved copycat drug
DOJ referral risk
branded-drug pivot cost
revenue recognition issue
```

Hims의 compounded GLP-1 중단과 branded drug 전환 비용은 pharma channel이 규제에 얼마나 민감한지 보여준다. ([Reuters][18])

---

## 7-4. CRO funding crunch

```text
4C:
biotech_funding_crunch
customer_R&D_budget_cut
backlog_slowdown
forecast_cut
revenue_decline
```

Charles River의 forecast cut과 premarket -15%는 CRO도 funding cycle에 묶인다는 기준이다. ([Reuters][14])

---

## 7-5. Telehealth CAC / impairment

```text
4C:
DTC_advertising_cost
CAC_increase
BetterHelp_impairment
forecast_withdrawal
record_low_stock
privacy_risk
```

Teladoc은 원격의료·온라인 정신건강이 사용자 수보다 CAC·privacy·반복계약·FCF가 중요하다는 hard counterexample이다. ([Reuters][15])

---

## 7-6. Medical device / aesthetic safety risk

```text
4C-watch:
counterfeit_product
unapproved_injectable
FDA_warning
injury_reports
licensed_channel_failure
```

보톡스·미용시술은 반복수요가 있어도 안전성과 허가 채널이 깨지면 Stage 3-Green을 유지하면 안 된다. ([AP News][17])

---

## 7-7. Biosimilar patent / litigation delay

```text
4C-watch:
patent_litigation
launch_delay
PBM_exclusion
price_competition
margin_compression
```

Amgen은 Samsung Bioepis의 Prolia/Xgeva biosimilar에 대해 34개 특허 침해를 주장하며 소송을 제기했다. 이건 biosimilar가 허가·신청 단계에 있어도 patent litigation이 launch timing과 economics를 흔들 수 있음을 보여준다. ([Reuters][19])

---

# 8. 점수비중 보정표 — R7 Loop 3 / v3.0

| canonical archetype                  | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | Loop 3 핵심 감점                                    |
| ------------------------------------ | ------: | ---------: | ---------: | ---------: | --------: | ------: | ---: | ----------------------------------------------- |
| `CDMO_HEALTHCARE_CONTRACT`           |      20 |         24 |         12 |         12 |        12 |       0 |    5 | 가동률, 고객집중, CAPEX, 미국 운영비                        |
| `CRO_CLINICAL_SERVICE`               |      16 |         17 |          7 |         11 |         9 |       0 |    5 | biotech funding, 고객 예산, forecast cut            |
| `BIOSIMILAR_COMMERCIALIZATION`       |      18 |         18 |          6 |         12 |         9 |       0 |    6 | 가격경쟁, PBM, 처방전환 지연, 특허소송                        |
| `BIOSIMILAR_ORIGINATOR_DEFENSE`      |      19 |         18 |          8 |         13 |        11 |       2 |    6 | patent cliff, 후속 신약 실패, pricing pressure        |
| `OBESITY_GLP1_COMMERCIALIZATION`     |      22 |         20 |         12 |         13 |        10 |       0 |    6 | 경쟁, 가격, 보험, 조제약, 초기 scripts                     |
| `GLP1_TELEHEALTH_CHANNEL`            |      18 |         15 |          5 |         13 |         8 |       0 |    6 | CAC, compounding crackdown, revenue recognition |
| `GENE_THERAPY_RARE_DISEASE`          |       7 |         10 |          8 |          9 |         5 |       0 |    5 | cash burn, 환급, 상업화 지연, going concern            |
| `AI_DRUG_DISCOVERY_PLATFORM`         |       6 |         10 |          7 |         12 |         6 |       0 |    5 | 승인약 부재, 임상실패, platform hype                     |
| `DIGITAL_HEALTHCARE_AI`              |      18 |         17 |          8 |         13 |        12 |       0 |    7 | 수가, 병원도입, subgroup risk, 책임소재                   |
| `DIGITAL_HEALTHCARE_REMOTE_MEDICINE` |      16 |         16 |          7 |         12 |         9 |       1 |    6 | 규제, 수가, unit economics                          |
| `TELEHEALTH_BEHAVIORAL_HEALTH`       |      15 |         13 |          5 |         10 |         8 |       0 |    6 | CAC, privacy, impairment, churn                 |
| `PHARMA_CHANNEL_AND_PRIVACY_RISK`    |    gate |       gate |       gate |       gate |      gate |    gate | gate | FDA/FTC, 조제약 품질, 개인정보                           |
| `MEDICAL_DEVICE_HEALTHCARE_EXPORT`   |      20 |         22 |         13 |         14 |        12 |       0 |    5 | 허가, 안전성, 경쟁, 채널 품질                              |
| `MEDICAL_DEVICE_DENTAL_IMPLANT`      |      20 |         22 |         13 |         14 |        12 |       0 |    5 | VBP, 가격통제, ASP 하락                               |
| `SURGICAL_ROBOT_INSTALLED_BASE`      |      21 |         23 |         13 |         14 |        12 |       1 |    5 | 병원 CAPEX, procedure mix, GLP-1 영향               |
| `BOTULINUM_AESTHETIC_REGULATED`      |      19 |         20 |         12 |         13 |        11 |       0 |    5 | 위조품, 허가, safety, 유통채널                           |
| `DIAGNOSTICS_INFECTIOUS_DISEASE`     |      20 |          5 |          5 |          5 |         5 |       0 |    5 | one-off demand, 정상화                             |
| `COMMERCIALIZATION_FAILURE_OVERLAY`  |    gate |       gate |       gate |       gate |      gate |    gate | gate | 승인 후 uptake·환급·매출 실패                            |
| `REIMBURSEMENT_ACCESS_OVERLAY`       |    gate |       gate |       gate |       gate |      gate |    gate | gate | 보험·PBM·수가·환급 실패                                 |
| `DEVICE_SAFETY_COUNTERFEIT_OVERLAY`  |    gate |       gate |       gate |       gate |      gate |    gate | gate | 위조품·무허가·리콜·제품안전                                 |

Loop 3에서 가장 크게 바뀐 건 여섯 가지다.

```text
1. SURGICAL_ROBOT_INSTALLED_BASE를 별도 archetype으로 추가.
   Intuitive Surgical처럼 installed base + procedure growth + instruments/accessories 반복매출 구조가 있기 때문.

2. GLP1_TELEHEALTH_CHANNEL을 GLP-1 본체와 분리.
   Hims처럼 channel은 성장성이 있어도 CAC·규제·compounding·revenue recognition 리스크가 크다.

3. OBESITY_GLP1_COMMERCIALIZATION은 EPS/FCF 점수 유지, Valuation 점수는 낮춤.
   Novo의 4B→4C 사례 때문이다.

4. GENE_THERAPY_RARE_DISEASE는 더 보수적으로 하향.
   Bluebird가 승인 후 상업화 실패의 기준 반례다.

5. DIGITAL_HEALTHCARE_AI는 Info 점수는 높지만 Stage 3 조건 강화.
   논문 성능보다 병원도입·수가·반복매출이 중요하다.

6. PHARMA_CHANNEL_AND_PRIVACY_RISK, REIMBURSEMENT_ACCESS_OVERLAY, COMMERCIALIZATION_FAILURE_OVERLAY를 gate로 둔다.
```

---

# 9. stage date 후보

## `CDMO_HEALTHCARE_CONTRACT`

```text
Stage 1:
대형 CDMO 계약, 미국/유럽 생산거점, capacity 증설 뉴스

Stage 2:
장기계약, 고객사 다변화, capacity utilization, OP/EPS 상향 확인

Stage 3:
다년 생산 visibility + FCF conversion + valuation frame 전환

Stage 4B:
CDMO capacity premium 과열, 미국 생산거점 narrative 과밀

Stage 4C:
가동률 하락, 계약 지연, CAPEX 부담, 고객사 주문 취소
```

## `CRO_CLINICAL_SERVICE`

```text
Stage 1:
임상 수주, 바이오 R&D 증가, backlog 증가 뉴스

Stage 2:
매출/OP 증가, 고객사 다변화, funding cycle 안정 확인

Stage 3:
다년 backlog와 높은 FCF conversion 확인

Stage 4B:
CRO 회복 기대 과열

Stage 4C:
biotech funding crunch, 고객 예산 삭감, forecast cut
```

## `BIOSIMILAR_COMMERCIALIZATION`

```text
Stage 1:
FDA/EMA 허가, 특허만료, biosimilar 출시 뉴스

Stage 2:
PBM/보험 등재, 처방전환, 실제 매출 확인

Stage 3:
처방량 증가 + 마진 방어 + 다국가 출시 확인

Stage 4B:
허가 뉴스만으로 관련주 과열

Stage 4C:
가격경쟁 심화, PBM incentive 부족, 처방전환 지연, 특허소송, 마진 붕괴
```

## `OBESITY_GLP1_COMMERCIALIZATION`

```text
Stage 1:
신약 허가, 임상 결과, oral GLP-1 출시

Stage 2:
처방량, 보험 커버리지, 공급능력, 매출 확인

Stage 3:
장기 처방 증가 + 가격 방어 + OP/EPS 상향 확인

Stage 4B:
비만치료제 시장규모 narrative 과열

Stage 4C:
가격 인하, compounded/generic 대체, 경쟁사 점유율 확대, 규제/광고 제재
```

## `GLP1_TELEHEALTH_CHANNEL`

```text
Stage 1:
telehealth GLP-1 offering, compounded product, branded partnership 뉴스

Stage 2:
subscriber growth, branded drug attach, revenue, legal settlement 확인

Stage 3:
CAC 안정 + gross margin + compliance + FCF 확인

Stage 4B:
DTC GLP-1 channel valuation 과열

Stage 4C:
FDA crackdown, compounding ban, legal cost, revenue recognition shock
```

## `GENE_THERAPY_RARE_DISEASE`

```text
Stage 1:
FDA 승인, 희귀질환 unmet need, 환자 모집 뉴스

Stage 2:
실제 환자 투여, 보험·환급, 매출 인식 확인

Stage 3:
극히 제한적. cash runway와 반복 pipeline 매출 필요

Stage 4B:
승인 뉴스만으로 주가 과열

Stage 4C:
slow uptake, cash crunch, going concern, discounted take-private
```

## `AI_DRUG_DISCOVERY_PLATFORM`

```text
Stage 1:
AI 신약 플랫폼, big pharma partnership, 후보물질 발굴 뉴스

Stage 2:
milestone, 임상 진입, 대형 제약사 계약금, cash runway 확인

Stage 3:
승인 가능성 높은 후보 + 반복 milestone + 상업화 경로 확인 전까지 제한

Stage 4B:
AI 신약개발 narrative 과열

Stage 4C:
임상 실패, 현금 고갈, 승인약 부재, platform hype 붕괴
```

## `DIGITAL_HEALTHCARE_AI`

```text
Stage 1:
AI 모델 성능·외부검증 논문, 인허가, 병원 pilot

Stage 2:
병원 도입, 수가/보험, 반복 과금, 매출 확인

Stage 3:
workflow 고착 + recurring revenue + OP 개선 확인

Stage 4B:
AI 의료 narrative 과열

Stage 4C:
subgroup 성능 문제, 의료책임, 도입 실패, 수가 부재
```

## `SURGICAL_ROBOT_INSTALLED_BASE`

```text
Stage 1:
신형 로봇 출시, installed base 증가, procedure growth 뉴스

Stage 2:
procedure growth, system placement, instruments/accessories 매출 확인

Stage 3:
반복 소모품 매출 + installed base 확대 + OPM/FCF 개선 확인

Stage 4B:
수술로봇 platform premium 과열

Stage 4C:
병원 CAPEX 둔화, procedure mix 악화, GLP-1로 일부 수술 감소, 경쟁 심화
```

## `MEDICAL_DEVICE_HEALTHCARE_EXPORT`

```text
Stage 1:
수출국 확대, 허가, 신제품 출시

Stage 2:
반복시술·소모품·채널 매출, OPM 개선 확인

Stage 3:
해외 반복매출 + ASP 유지 + FCF 개선 확인

Stage 4B:
미용기기·임플란트 premium 과열

Stage 4C:
가격통제, 허가 지연, safety issue, 위조품, 경쟁 심화
```

---

# 10. 가격경로 검증계획

## R7 Loop 3 공통 검증 방식

```text
1. 각 case의 stage1_date, stage2_date, stage3_date를 지정한다.
2. 해당 날짜의 종가를 stage_price로 저장한다.
3. MFE_30D / 90D / 180D / 1Y / 2Y를 계산한다.
4. MAE_30D / 90D / 180D / 1Y를 계산한다.
5. peak_price와 drawdown_after_peak를 계산한다.
6. 처방량, 매출, backlog, 가동률, 수가, 보험, 환급, cash runway, OPM과 가격경로를 비교한다.
```

## Loop 3에서 새로 강제할 판정

```text
COMMERCIALIZATION_ALIGNED:
허가·계약 이후 실제 처방·매출·OPM·주가가 동행.

APPROVAL_WITHOUT_UPTAKE:
허가는 받았지만 처방·환급·매출이 약함.

CAPACITY_WITHOUT_UTILIZATION:
CDMO/의료기기 capacity는 있으나 가동률·계약 미확인.

GLP1_APPROVAL_BUT_SCRIPT_GATE:
GLP-1 승인은 있었지만 weekly scripts·보험·가격 방어 확인 필요.

GLP1_4B_TO_4C:
거대 시장 narrative 이후 가격·경쟁·보험 문제로 급락.

TELEHEALTH_CHANNEL_VOLATILITY:
telehealth 제휴·compounded drug·branded pivot에 따라 주가 급변.

AI_CLINICAL_VALIDATION_NOT_COMMERCIAL:
논문·AUC는 좋지만 병원도입·수가·반복매출 없음.

GENE_THERAPY_CASH_CRUNCH:
승인 후에도 상업화 지연과 현금고갈로 thesis break.

DEVICE_SAFETY_REGULATORY_4C:
미용기기·보톡스·임플란트에서 safety·VBP·위조품 리스크 발생.

SURGICAL_ROBOT_RECURRING_CONSUMABLE_SUCCESS:
installed base + procedure growth + 소모품 매출이 동행.
```

## 이번 R7 Loop 3에서 우선 검증할 가격 case

| case_id                                            | stage2 후보일 | 현재 1차 가격판정                                         |
| -------------------------------------------------- | ---------: | -------------------------------------------------- |
| `samsung_biologics_gsk_us_facility_case`           | 2025-12-22 | -0.4%, strategic CDMO but price delayed            |
| `samsung_biologics_cdmo_capacity_reference`        |     계약/시설별 | CDMO structural reference                          |
| `intuitive_surgical_q1_2026_procedure_growth_case` |    2026-04 | +7.2%, surgical robot recurring consumable success |
| `straumann_dental_implant_vbp_case`                | 2026-02-18 | 장중 +6%, dental implant aligned                     |
| `lilly_foundayo_fda_approval_case`                 | 2026-04-01 | Lilly +6%, oral GLP-1 Stage 2                      |
| `lilly_foundayo_prescription_uptake_case`          | 2026-05-08 | 7,335 scripts, modest uptake                       |
| `lilly_foundayo_switch_maintenance_case`           | 2026-05-12 | maintenance therapy candidate                      |
| `novo_glp1_price_pressure_case`                    | 2026-02-04 | -16%, $50B wipeout, 4C-watch                       |
| `hims_branded_glp1_pivot_loss_case`                | 2026-05-12 | -11%, pharma channel risk                          |
| `hims_novo_partnership_case`                       | 2026-03-09 | +36%+, channel event premium                       |
| `hims_compounded_glp1_crackdown_case`              | 2026-02-07 | compounded drug regulatory 4C-watch                |
| `bluebird_gene_therapy_cash_crunch_case`           | 2025-02-21 | -36%, hard 4C                                      |
| `charles_river_cro_funding_crunch_case`            | 2024-08-07 | -15%, CRO funding 4C-watch                         |
| `teladoc_betterhelp_impairment_case`               | 2024-08-01 | -13%, record low                                   |
| `recursion_exscientia_ai_drug_case`                | 2024-08-08 | AI drug platform Watch                             |
| `lunit_dbt_subgroup_validation_case`               | 2025-03-17 | clinical validation, commercialization unproven    |
| `boehringer_goodrx_humira_biosimilar_case`         | 2024-07-18 | biosimilar access candidate, uptake/margin watch   |
| `amgen_samsung_bioepis_biosimilar_litigation_case` | 2024-08-13 | biosimilar patent litigation risk                  |
| `botox_counterfeit_fda_warning_case`               |    2025-11 | safety/regulatory 4C-watch                         |

---

# 11. 다음에 에이전트가 채워야 할 price fields

R7 Loop 3에서는 아래 필드를 채우게 해야 한다.

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

contract_value
contract_duration_months
capacity_liters
capacity_utilization
facility_location
customer_name
customer_concentration
backlog_growth
op_margin_change
fcf_margin
capex_amount
tariff_hedge_flag

prescription_volume
weekly_scripts
script_growth_rate
prescriber_count
new_prescriber_ratio
insurance_coverage
pbm_listing_flag
drug_price_change
monthly_price
gross_to_net_discount
compounded_alternative_flag
generic_competition_flag
telehealth_channel_flag

approval_status
launch_date
patient_uptake
reimbursement_status
commercial_revenue
cash_runway_months
going_concern_flag
dilution_flag
take_private_flag
discounted_take_private_flag

clinical_trial_phase
milestone_payment
big_pharma_partner
pipeline_count
ai_platform_flag
approved_drug_count
cash_runway_years

hospital_adoption_count
reimbursement_code_flag
recurring_revenue_ratio
ai_model_auc
subgroup_performance_risk
external_validation_flag
liability_risk_flag
workflow_integration_flag

surgical_robot_installed_base
procedure_growth
system_placements
instruments_accessories_revenue
procedure_mix_risk
hospital_capex_risk
bariatric_slowdown_flag

device_export_country_count
procedure_volume
consumable_revenue_ratio
asp_change
vbp_price_control_flag
counterfeit_safety_flag
fda_warning_flag
licensed_channel_flag

biosimilar_approval_flag
interchangeable_flag
pbm_coverage_flag
biosimilar_prescription_volume
price_discount_pct
patent_litigation_flag
launch_delay_flag
margin_compression_flag

cac
churn
privacy_incident_flag
impairment_charge
forecast_withdrawal_flag
advertising_cost_change
revenue_recognition_issue_flag

score_price_alignment
price_validation_status
review_notes
```

---

# R7 Loop 3 결론

이번 3회차에서 R7은 더 좁혀졌다.

```text
Green 가능:
CDMO 중 장기계약·capacity utilization·고객사 다변화가 확인된 기업
수술로봇 중 installed base·procedure growth·소모품 반복매출이 확인된 기업
의료기기 수출 중 반복시술·소모품·OPM이 확인된 기업
치아·임플란트 중 가격통제 리스크를 통과한 기업
GLP-1 상업화 기업 중 처방량·보험·가격·OP/EPS가 따라오는 기업

Watch-to-Green:
CRO
바이오시밀러
의료AI
원격의료
보톡스·미용시술
수술용 로봇 후발주
동물백신

Watch/Red:
AI 신약개발
유전자치료제
희귀질환 pre-revenue biotech
마이크로바이옴
줄기세포·면역세포 치료제
전염병 진단 one-off
DTC telehealth
GLP-1 telehealth channel

Hard 4C:
승인 후 상업화 실패
cash crunch
going concern
CRO funding crunch
BetterHelp식 impairment
compounded GLP-1 regulatory crackdown
GLP-1 가격·경쟁 압박
보톡스 위조품·무허가 유통
의료AI subgroup/수가/도입 실패
biosimilar patent litigation / PBM 미등재 / 처방전환 실패
```

**R7 Loop 3 점수정규화의 핵심 문장:**

> 바이오·헬스케어·의료기기는 “허가”, “임상”, “AI”, “논문”, “시장규모”가 아니라 **계약, 가동률, 처방량, PBM/보험, 수가, 반복시술, 소모품, 환급, cash runway, FCF 전환, 실제 가격경로 리레이팅**으로 봐야 한다.
> 허가를 받아도 상업화가 안 되면 4C이고, 논문 성능이 좋아도 병원도입·수가·반복매출이 없으면 Stage 3-Green은 금지다.

다음 순서는 **R8 — 플랫폼·콘텐츠·SW·보안 Loop 3**다.

[1]: https://www.reuters.com/business/healthcare-pharmaceuticals/samsung-biologics-buy-us-drug-production-facility-gsk-280-mln-2025-12-21/?utm_source=chatgpt.com "Samsung Biologics to buy US drug production facility from GSK for $280 million"
[2]: https://en.wikipedia.org/wiki/Samsung_Biologics?utm_source=chatgpt.com "Samsung Biologics"
[3]: https://www.investors.com/news/technology/intuitive-surgical-stock-intuitive-surgical-earnings-q1-2026/?utm_source=chatgpt.com "Why Robotic Surgery's Titan, Intuitive Surgical, Just Made A Bullish Move"
[4]: https://www.reuters.com/business/healthcare-pharmaceuticals/straumann-beats-earnings-expectations-2026-02-18/?utm_source=chatgpt.com "Straumann forecasts 2026 growth despite China procurement uncertainty, shares rise"
[5]: https://www.reuters.com/business/healthcare-pharmaceuticals/lillys-weight-loss-pill-wins-us-approval-2026-04-01/?utm_source=chatgpt.com "Lilly's weight-loss pill wins US approval, sets up next battle with rival Novo Nordisk"
[6]: https://www.reuters.com/legal/litigation/lillys-obesity-pill-tops-7000-prescriptions-fourth-week-signals-modest-uptake-2026-05-08/?utm_source=chatgpt.com "Lilly's obesity pill tops 7,000 prescriptions in fourth week, signals modest uptake"
[7]: https://arxiv.org/abs/2503.13581?utm_source=chatgpt.com "Subgroup Performance of a Commercial Digital Breast Tomosynthesis Model for Breast Cancer Detection"
[8]: https://www.axios.com/2024/07/18/goodrx-boehringer-humira-biosimilar?utm_source=chatgpt.com "GoodRx teams with Boehringer on Humira biosimilar"
[9]: https://www.reuters.com/business/healthcare-pharmaceuticals/novo-nordisk-plunge-wipes-50-billion-off-obesity-drug-giant-2026-02-04/?utm_source=chatgpt.com "Novo Nordisk plunge wipes $50 billion off obesity drug giant"
[10]: https://www.reuters.com/legal/litigation/hims-hers-plunges-after-weight-loss-pivot-hits-quarterly-results-2026-05-12/?utm_source=chatgpt.com "Hims & Hers plunges as branded weight-loss drug pivot hits results"
[11]: https://apnews.com/article/d56b8ad0737be75674bc05ffe488b948?utm_source=chatgpt.com "Hims & Hers Health and Novo Nordisk end lawsuit over weight loss medications, enter collaboration"
[12]: https://www.reuters.com/legal/litigation/novo-nordisk-take-legal-action-against-hims-hers-wegovy-compounding-2026-02-05/?utm_source=chatgpt.com "Novo Nordisk to take legal action against Hims & Hers for Wegovy compounding"
[13]: https://www.reuters.com/markets/deals/bluebird-bio-be-taken-private-by-carlyle-sk-capital-amid-cash-crunch-2025-02-21/?utm_source=chatgpt.com "Gene therapy maker bluebird to go private in discounted deal amid cash crunch"
[14]: https://www.reuters.com/business/healthcare-pharmaceuticals/charles-river-cuts-2024-forecast-funding-crunch-among-biotech-clients-persists-2024-08-07/?utm_source=chatgpt.com "Charles River cuts 2024 forecast as funding crunch among biotech clients persists"
[15]: https://www.reuters.com/business/healthcare-pharmaceuticals/teladoc-shares-hit-record-low-after-telehealth-firm-withdraws-2024-forecast-2024-08-01/?utm_source=chatgpt.com "Teladoc shares hit record low after telehealth firm withdraws 2024 forecast"
[16]: https://www.reuters.com/markets/deals/biotech-firm-recursion-buy-smaller-peer-exscientia-688-million-2024-08-08/?utm_source=chatgpt.com "Biotech firm Recursion to buy smaller peer Exscientia for $688 million"
[17]: https://apnews.com/article/67afcdc72e100204181c20aacec39d89?utm_source=chatgpt.com "FDA warns websites selling unapproved Botox for cosmetic purposes"
[18]: https://www.reuters.com/legal/litigation/hims-hers-stop-offering-compounded-semaglutide-pill-after-fda-crackdown-2026-02-07/?utm_source=chatgpt.com "Hims to stop offering GLP-1 pill after FDA warned of crackdown"
[19]: https://www.reuters.com/legal/litigation/amgen-sues-samsung-biotech-unit-over-bone-drug-copies-2024-08-13/?utm_source=chatgpt.com "Amgen sues Samsung biotech unit over bone drug copies"

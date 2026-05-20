좋아. **R6 Loop 8까지 끝났으니, 이번은 R7 Loop 8 — 바이오·헬스케어·의료기기**다.

R7은 CDMO, CMO, 원료의약품, CRO, 바이오시밀러, 의료AI, 원격의료, 유전체검사, AI 신약개발, 이중항체, 세포치료제, 줄기세포, 치매·비만·탈모 치료제, 보톡스, 임플란트, 미용기기, 수술용 로봇, 전염병 진단을 흡수한다. 기존 Theme Tag Map 기준으로도 R7은 세 갈래로 나뉜다. **pre-revenue biotech은 Green 거의 금지**, **royalty/commercialization biotech은 실제 매출화·로열티 필요**, **CDMO/medical device는 장기계약·반복매출이면 Green 가능**이다.

서생원식으로 보면 R7의 질문은 “허가를 받았나?”, “임상이 좋았나?”, “AI 모델 성능이 높나?”가 아니다. 핵심은 **허가·임상·논문·AI 성능이 실제 처방, 보험, 수가, 반복시술, 계약, 매출, FCF로 넘어가서 EPS 체급과 밸류에이션 프레임을 바꾸는가**다. 승인과 논문은 출발선이고, 상업화와 반복 현금흐름이 없으면 Stage 3가 아니다.

공시·데이터 작업에서도 같은 원칙이 들어간다. 계약금액, 계약기간, 고객명, 가동률, 처방량, PBM·보험 등재, 수가, cash runway, 희석률, OP YoY 같은 detail을 실제로 확인해야 한다. 값이 없으면 만들지 않아야 하고, list-level 공시나 보도 제목만으로 Stage 3-Green을 쉽게 올리면 안 된다.

---

# R7 Loop 8. 바이오·헬스케어·의료기기

## 1. 이번 라운드 대섹터

```text
R7 = 바이오·헬스케어·의료기기
Loop 8 목표 =
CDMO 미국 생산거점 / 수술로봇 반복소모품 /
oral GLP-1 approval / GLP-1 maintenance therapy /
GLP-1 price war / GLP-1 telehealth channel /
compounded GLP-1 crackdown / gene therapy commercialization failure /
CRO funding cycle / biosimilar PBM gate /
medical AI external validation / botox·device safety를

stage 포착 + 실제 가격경로 + 점수비중 재조정으로 다시 정규화
```

이번 R7 Loop 8의 핵심 질문은 이거다.

```text
이 기업은 허가·임상·AI·기술을 실제 매출과 FCF로 바꾸고 있는가?
아니면 승인, 논문, TAM, 플랫폼, 상용화 기대만으로 움직이는가?
```

R7 stage는 이렇게 잡는다.

```text
Stage 1:
임상 결과, FDA/EMA 승인 기대, AI 의료 논문, CDMO capacity,
GLP-1 TAM, 바이오시밀러 허가, 의료기기 출시 뉴스

Stage 2:
승인, 고객계약, 생산시설, PBM/보험 등재, 처방량,
procedure growth, hospital adoption, 매출 가이던스 확인

Stage 3:
실제 처방·매출·OPM·FCF·반복소모품·보험/수가·재주문이 확인되고
가격경로가 동행

Stage 4B:
모두가 GLP-1, 수술로봇, CDMO, 의료AI, 바이오시밀러 수혜를 인정해
valuation이 먼저 간 구간

Stage 4C:
승인 후 uptake 실패, 보험·수가 실패, cash crunch, funding crunch,
가격전쟁, compounded drug 단속, patent litigation, safety issue
```

R7에서 제일 중요한 분리는 이거다.

```text
FDA 승인
≠ 상업화

임상 성공
≠ 처방량

PBM/보험 등재
≠ 마진 방어

의료AI AUC
≠ 병원 도입·수가·반복매출

수술로봇 설치
≠ 반복소모품 매출

GLP-1 TAM
≠ 가격·보험·경쟁 리스크 면제

CDMO capacity
≠ 가동률·고객계약
```

---

## 2. 대상 canonical archetype

| canonical archetype                         | Loop 8 판정 방향         | stage 포착 핵심                                               |
| ------------------------------------------- | -------------------- | --------------------------------------------------------- |
| `CDMO_HEALTHCARE_CONTRACT`                  | Green 가능             | 장기계약, 가동률, 고객사, OPM, FCF                                  |
| `CDMO_US_TARIFF_HEDGE_CAPACITY`             | Watch-to-Green       | 미국 생산거점, 고객계약, 가동률, tariff hedge                          |
| `CDMO_ADC_CELL_GENE_CAPABILITY`             | Watch-to-Green       | ADC·세포/유전자 생산능력, 고객계약, tech transfer                      |
| `CRO_CLINICAL_SERVICE`                      | Watch-to-Green       | backlog, 고객 R&D 예산, FCF                                   |
| `CRO_FUNDING_CYCLE_OVERLAY`                 | RedTeam overlay      | biotech funding crunch, forecast cut                      |
| `BIOSIMILAR_COMMERCIALIZATION`              | Watch-to-Green       | 허가보다 PBM/보험·처방전환·마진                                       |
| `BIOSIMILAR_ACCESS_CASH_PAY`                | Watch                | 가격할인, access, 실제 처방·마진 확인                                 |
| `BIOSIMILAR_PBM_FORMULARY_SWITCH`           | Watch-to-Green       | PBM preferred list, $0 copay, 실제 scripts                  |
| `BIOSIMILAR_PATENT_LITIGATION`              | RedTeam overlay      | 특허소송, launch delay, injunction                            |
| `OBESITY_GLP1_COMMERCIALIZATION`            | Green 가능하지만 4B/4C 강함 | 처방량, 보험, 가격, gross-to-net, OP/EPS                         |
| `ORAL_GLP1_APPROVAL_COMMERCIALIZATION`      | Watch-to-Green       | approval은 Stage 2, scripts·보험·가격이 Stage 3                 |
| `ORAL_GLP1_MAINTENANCE_THERAPY`             | Watch-to-Green       | injection-to-pill switch, refill, adherence               |
| `GLP1_PRICE_WAR_OVERLAY`                    | RedTeam overlay      | 가격인하, 경쟁, copycat, 보험 압박                                  |
| `GLP1_TELEHEALTH_CHANNEL`                   | High-risk Watch      | DTC, CAC, branded pivot, compliance                       |
| `COMPOUNDED_GLP1_REGULATORY_RISK`           | hard gate            | FDA/DOJ, unapproved copycat, legal cost                   |
| `GENE_THERAPY_RARE_DISEASE`                 | Watch/Red            | 승인 후 uptake·환급·cash runway 필요                             |
| `AI_DRUG_DISCOVERY_PLATFORM`                | Watch/Red            | platform보다 milestone·임상·승인·매출                             |
| `DIGITAL_HEALTHCARE_AI`                     | Watch-to-Green       | 외부검증, 병원도입, 수가, 반복매출                                      |
| `MEDICAL_AI_EXTERNAL_VALIDATION`            | Stage 1~2            | 논문·AUC는 좋지만 deployment 전 Green 금지                         |
| `MEDICAL_AI_SUBGROUP_GENERALIZATION_RISK`   | RedTeam overlay      | subgroup 성능, dataset bias, liability                      |
| `DIGITAL_HEALTHCARE_REMOTE_MEDICINE`        | Watch                | 규제, 수가, CAC, retention, FCF                               |
| `TELEHEALTH_BEHAVIORAL_HEALTH`              | Watch/Red            | CAC, impairment, privacy, DTC demand                      |
| `MEDICAL_DEVICE_HEALTHCARE_EXPORT`          | Green 가능             | 반복시술, 소모품, 해외 허가, OPM                                     |
| `SURGICAL_ROBOT_INSTALLED_BASE`             | Green 가능             | installed base, procedure growth, instruments/accessories |
| `SURGICAL_ROBOT_GLP1_PROCEDURE_MIX_OVERLAY` | RedTeam overlay      | bariatric slowdown, GLP-1 procedure mix 영향                |
| `BOTULINUM_AESTHETIC_REGULATED`             | Watch-to-Green       | 허가, 안전 유통, 반복시술                                           |
| `DEVICE_SAFETY_COUNTERFEIT_OVERLAY`         | hard gate            | 위조품, 무허가, 리콜, injury report                               |
| `COMMERCIALIZATION_FAILURE_OVERLAY`         | hard gate            | 승인 후 uptake·환급·매출 실패                                      |
| `REIMBURSEMENT_ACCESS_OVERLAY`              | hard/soft gate       | 보험·PBM·수가·환급 실패                                           |
| `DISCLOSURE_CONFIDENCE_CAP`                 | 공통 cap               | 계약·처방량·수가·상대방 미공개 시 Stage 3 제한                            |

---

## 3. deep sub-archetype

```text
CDMO_HEALTHCARE_CONTRACT
- Samsung Biologics
- GSK Rockville facility
- Human Genome Sciences
- 60,000L drug substance capacity
- U.S. manufacturing site
- tariff hedge
- technology transfer
- customer qualification
- capacity utilization

SURGICAL_ROBOT_INSTALLED_BASE
- Intuitive Surgical
- da Vinci
- Ion
- installed base
- procedure growth
- instruments/accessories
- system placements
- da Vinci 5
- bariatric slowdown
- hospital CAPEX cycle

OBESITY_GLP1_COMMERCIALIZATION
- Eli Lilly Foundayo
- orforglipron
- Novo Wegovy pill
- Zepbound
- weekly scripts
- insurance coverage
- self-pay price
- gross-to-net
- boxed warning
- price pressure
- copycat/compounded GLP-1

GLP1_TELEHEALTH_CHANNEL
- Hims & Hers
- compounded semaglutide
- branded Wegovy pivot
- DTC channel
- CAC
- legal cost
- restructuring cost
- revenue recognition
- FDA crackdown
- DOJ referral risk

GENE_THERAPY_RARE_DISEASE
- Bluebird bio
- Lyfgenia
- Zynteglo
- Skysona
- slow uptake
- reimbursement
- cash runway
- going concern
- discounted take-private

CRO_CLINICAL_SERVICE
- Charles River
- drug discovery service
- biotech client funding
- backlog
- high-rate funding crunch
- forecast cut
- restructuring
- buyback plan

BIOSIMILAR_COMMERCIALIZATION
- Humira biosimilar
- Prolia / Xgeva biosimilar
- PBM
- Cigna / Accredo
- GoodRx cash-pay
- interchangeable biosimilar
- patent litigation
- price competition
- margin compression

MEDICAL_AI_EXTERNAL_VALIDATION
- Lunit INSIGHT DBT
- mammography AI
- external validation
- AUC
- recall
- subgroup performance
- dense breast tissue
- calcifications
- hospital deployment
- reimbursement code

BOTULINUM_AESTHETIC_REGULATED
- Botox
- botulinum toxin
- counterfeit product
- unapproved injectable
- FDA warning letters
- licensed provider channel
- boxed warning
```

---

## 4. 성공사례

### 4-1. Samsung Biologics 미국 생산거점 — 전략적 Stage 2, 가격경로는 아직 약함

Samsung Biologics는 GSK로부터 미국 Maryland Rockville 소재 Human Genome Sciences 생산시설을 2.8억 달러에 인수하기로 했다. 이 시설은 60,000L drug substance capacity를 보유하고 있고, Samsung Biologics의 첫 미국 생산거점이라는 점에서 `CDMO_US_TARIFF_HEDGE_CAPACITY`의 Stage 2 근거가 된다. 다만 발표 직후 Samsung Biologics 주가는 0.4% 하락해, broader market의 2% 상승을 밑돌았다. 즉 capacity와 위치는 좋지만, 고객계약·가동률·OPM/FCF 전까지 Stage 3는 아니다. ([Reuters][1])

```text
case_type:
CDMO_US_TARIFF_HEDGE_CAPACITY_STAGE2
+
PRICE_ALIGNMENT_DELAYED

stage 포착:
Stage 1 = 미국 생산거점, CDMO 글로벌화, tariff hedge narrative
Stage 2 = $280m 인수, 60,000L capacity, Rockville facility 확인
Stage 3 = 고객계약, 가동률, tech transfer, OPM/FCF 확인 전까지 제한

가격경로 판정:
전략 evidence는 강하지만 발표 당일 가격은 약했다.
즉 capacity만으로 Stage 3를 올리면 안 된다.
```

**정규화 결론**

```text
CDMO_US_TARIFF_HEDGE_CAPACITY는 Visibility를 올린다.
하지만 EPS/FCF 점수는 고객계약·가동률·tech transfer 후에만 올린다.
```

---

### 4-2. Intuitive Surgical — 수술로봇 installed base가 반복소모품으로 넘어가는 구조

Intuitive Surgical은 R7에서 가장 서생원식에 가까운 의료기기 구조다. 2026년 1분기 da Vinci와 Ion procedure는 전년 대비 17% 증가했고, 매출은 23% 증가한 27.7억 달러, 조정 EPS는 2.50달러로 예상치를 웃돌았다. 회사는 2026년 procedure growth guidance도 13.5~15.5%로 올렸다. 이건 단순 장비 판매가 아니라 **installed base → procedure growth → instruments/accessories 반복매출 → EPS/FCF visibility**로 이어지는 구조다. ([Investors.com][2])

다만 Intuitive도 모든 beat가 바로 강한 주가 리레이팅으로 이어지는 것은 아니다. 2025년 4분기에는 revenue와 EPS가 모두 예상치를 웃돌고 global procedure가 18% 증가했지만, 주가는 종가 기준 0.4% 상승에 그쳤다. 즉 surgical robot은 좋은 구조 후보지만, valuation이 이미 높으면 Stage 3 성공과 4B 감시가 동시에 붙는다. ([Barron's][3])

```text
case_type:
SURGICAL_ROBOT_INSTALLED_BASE_ALIGNED
+
STRUCTURAL_MEDTECH_RECURRING_SUCCESS
+
4B_VALUATION_WATCH

stage 포착:
Stage 1 = 수술로봇 installed base와 da Vinci 5 rollout
Stage 2 = procedure growth, system placement, revenue/EPS beat
Stage 3 후보 = instruments/accessories 반복매출 + guidance 상향
Stage 4B-watch = valuation, medtech sector compression, GLP-1에 따른 bariatric slowdown risk

가격경로 판정:
사업 stage는 매우 강하다.
다만 Q4 beat에도 주가 +0.4%에 그친 사례가 있어 valuation room을 같이 봐야 한다.
```

**정규화 결론**

```text
SURGICAL_ROBOT_INSTALLED_BASE는 R7 최상위 Green 후보군 유지.

단, Stage 3는:
procedure_growth
+ instruments_accessories_revenue
+ installed_base
+ OPM/FCF
+ valuation room
+ procedure_mix_risk 통과

가 모두 필요하다.
```

---

### 4-3. Lilly Foundayo / oral GLP-1 — approval은 Stage 2, scripts·보험·가격이 Stage 3

Eli Lilly의 oral GLP-1 비만치료제 Foundayo, 즉 orforglipron은 2026년 4월 미국 FDA 승인을 받았다. FT는 이 승인 뒤 Lilly 주가가 4% 상승했고, 가격은 월 149달러부터 시작하며 보험이 있으면 더 낮아질 수 있다고 보도했다. 이건 `ORAL_GLP1_APPROVAL_COMMERCIALIZATION`의 Stage 2 포착이 가격경로와 맞은 사례다. ([Financial Times][4])

이후 maintenance therapy 데이터도 Stage 2 근거를 강화했다. Reuters는 injectable Wegovy에서 Foundayo로 전환한 환자가 1년 뒤 평균 2파운드만 회복했고, Zepbound에서 전환한 환자는 평균 11파운드 회복했다고 보도했다. 52주차 기준 기존 semaglutide 사용자는 감량분의 79.3%, tirzepatide 사용자는 74.7%를 유지했다. 이 데이터는 “injection-to-pill maintenance therapy” thesis를 강화하지만, 여전히 실제 처방량, 보험, gross-to-net, refill rate가 Stage 3 gate다. ([Reuters][5])

```text
case_type:
ORAL_GLP1_APPROVAL_COMMERCIALIZATION_STAGE2
+
ORAL_GLP1_MAINTENANCE_THERAPY_STAGE2

stage 포착:
Stage 1 = oral GLP-1 convenience, obesity TAM
Stage 2 = FDA approval, launch price, Lilly +4%, maintenance data
Stage 3 = weekly scripts, insurance, gross-to-net, refill, OP/EPS 확인 필요
Stage 4B-watch = GLP-1 market consensus, price war, copycat risk

가격경로 판정:
approval stage 포착은 가격상승과 맞았다.
하지만 approval만으로 Stage 3로 올리면 안 된다.
```

**정규화 결론**

```text
ORAL_GLP1_APPROVAL_COMMERCIALIZATION은 Visibility를 올린다.
하지만 EPS/FCF 점수는 prescription volume과 insurance coverage 전까지 cap.
```

---

### 4-4. 바이오시밀러 PBM/formulary — 허가보다 처방전환 gate가 중요

Humira biosimilar는 R7에서 “허가만으로 부족하고 PBM·보험·처방전환이 핵심”이라는 기준을 만든다. Cigna는 Accredo specialty pharmacy를 통해 eligible patients에게 Humira biosimilar를 out-of-pocket $0로 제공하겠다고 했고, biosimilar 가격은 Humira list price 대비 약 85% 낮은 수준이었다. 하지만 AbbVie의 Humira는 biosimilar 출시 이후에도 98% 이상 점유율을 유지하고 있었다. ([Reuters][6])

GoodRx와 Boehringer Ingelheim도 Humira biosimilar를 92% 할인된 현금가로 제공했다. 그런데 Reuters는 Boehringer의 Cyltezo가 5월 기준 약 2,500건 처방에 그친 반면 Humira는 60만 건 이상이었다고 보도했다. 즉 가격할인과 interchangeability는 Stage 2 근거지만, Stage 3는 실제 prescription volume과 margin 방어가 필요하다. ([Reuters][7])

```text
case_type:
BIOSIMILAR_PBM_FORMULARY_SWITCH_STAGE2
+
BIOSIMILAR_ACCESS_WITHOUT_UPTAKE_WATCH

stage 포착:
Stage 1 = biosimilar approval / Humira patent cliff
Stage 2 = PBM/formulary, $0 copay, 85~92% discount
Stage 3 = prescription switch, revenue, margin 방어 확인 필요
Stage 4C-watch = PBM rebate 구조, price competition, slow uptake

가격경로 판정:
R7 점수표가 “승인보다 PBM/보험”을 핵심 stage로 잡은 것은 맞다.
하지만 access program만으로 Green은 아니다.
```

**정규화 결론**

```text
BIOSIMILAR_COMMERCIALIZATION은 approval 점수보다
PBM/보험 등재, 처방량, 마진 방어 가중치를 더 크게 둔다.
```

---

### 4-5. Lunit INSIGHT DBT 외부검증 — 의료AI Stage 1~2는 가능하지만, 병원도입·수가 전까지 Green 아님

Lunit INSIGHT DBT 모델을 163,449건 screening mammography exams로 외부검증한 연구는 전체 AUC 0.91, recall 0.73을 보고했다. 다만 non-invasive cancer, calcifications, dense breast tissue subgroup에서는 성능이 낮아졌다. 이건 의료AI에서 논문·AUC가 의미 있는 Stage 1~2 evidence가 될 수 있지만, subgroup risk, hospital deployment, reimbursement code, liability를 통과해야 Stage 3가 된다는 기준이다. ([arXiv][8])

```text
case_type:
MEDICAL_AI_EXTERNAL_VALIDATION_STAGE1_2
+
MEDICAL_AI_SUBGROUP_GENERALIZATION_RISK

stage 포착:
Stage 1 = 의료AI 성능·외부검증 논문
Stage 2 = 대규모 external validation, AUC/recall 확인
Stage 3 = 병원 도입, 수가, 반복매출, workflow lock-in 필요
Stage 4C-watch = subgroup underperformance, liability, dataset bias

가격경로 판정:
논문 evidence는 좋지만 상장사 price-path stage로 바로 번역하면 안 된다.
```

**정규화 결론**

```text
MEDICAL_AI_EXTERNAL_VALIDATION은 Info/Visibility 점수를 올린다.
하지만 EPS/FCF 점수는 deployment와 reimbursement 전까지 낮게 둔다.
```

---

## 5. 반례

### 5-1. Novo Nordisk — GLP-1도 price war가 오면 4B에서 4C로 내려간다

Novo Nordisk는 GLP-1 시장의 대표 성장기업이었지만, 2026년 sales와 operating profit이 5~13% 감소할 수 있다고 경고했다. 원인은 미국 가격 압박, 경쟁 심화, semaglutide 특허 만료, copycat drug 압박이었다. Reuters는 이 경고 이후 Novo의 미국 상장주가 12% 하락했다고 보도했다. ([Reuters][9])

다음 날 Novo Nordisk 주가는 16% 급락했고 약 500억 달러의 시가총액이 사라졌다. 이건 거대한 TAM과 기존 고성장도 가격·경쟁·보험·copycat 압박 앞에서는 Stage 4C로 내려갈 수 있다는 기준이다. ([Reuters][10])

```text
case_type:
GLP1_GROWTH_MARKET_4B_TO_4C

stage 포착:
Stage 1 = obesity GLP-1 mega-TAM
Stage 2~3 = Wegovy/Ozempic revenue growth
Stage 4C = price pressure, competition, sales/profit decline warning
가격경로 = -12% to -16%, 약 $50B 시총 감소

가격경로 판정:
GLP1_PRICE_WAR_OVERLAY가 실제 주가하락과 매우 잘 맞았다.
```

**정규화 결론**

```text
OBESITY_GLP1_COMMERCIALIZATION은 높은 EPS/FCF 점수를 줄 수 있다.
하지만 price_pressure, competition, insurance, gross_to_net, copycat risk가 켜지면 Stage 3를 강등한다.
```

---

### 5-2. Hims & Hers — GLP-1 telehealth channel은 CAC·규제·branded pivot 비용이 크다

Hims & Hers는 compounded GLP-1에서 branded Wegovy 등으로 전환하면서 2026년 1분기 예상 밖 손실을 냈고, 주가는 11% 하락했다. Reuters는 semaglutide ingredient write-down, legal fee, merger-related cost, revenue recognition timing, compounded drug에서 branded drug으로의 pivot 비용이 손실에 영향을 줬다고 보도했다. ([Reuters][11])

Barron’s 기준으로는 Hims 주가가 장중 14.6% 하락했고, compounded semaglutide 판매 환경이 바뀐 뒤 branded GLP-1로 전환하면서 margin과 수익성 가시성이 흔들렸다. 즉 GLP-1 수요가 아무리 커도 유통채널이 회색이면 Stage 3-Green을 막아야 한다. ([Barron's][12])

```text
case_type:
GLP1_TELEHEALTH_CHANNEL_HIGH_VOLATILITY
+
COMPOUNDED_GLP1_REGULATORY_RISK_HARD_GATE

stage 포착:
Stage 1 = DTC GLP-1, compounded cheap access
Stage 2 = branded partnership / platform user base
Stage 4C-watch = FDA/regulatory shift, loss, legal cost, revenue recognition issue
가격경로 = -11%~-14.6%

가격경로 판정:
telehealth GLP-1 RedTeam이 실제 주가하락과 맞았다.
```

**정규화 결론**

```text
GLP1_TELEHEALTH_CHANNEL은 사용자 수로 점수 올리면 안 된다.

필수:
CAC
gross margin
legal cost
regulatory compliance
branded partnership economics
revenue recognition
FCF
```

---

### 5-3. Bluebird bio — FDA 승인 후에도 uptake·현금흐름이 없으면 4C

Bluebird bio는 승인된 gene therapy를 갖고 있었지만 severe cash crunch로 Carlyle과 SK Capital에 주당 3달러에 비상장화되기로 했다. 이 가격은 직전 종가 대비 57.4% 할인된 수준이었고, 발표 후 주가는 36% 하락했다. Reuters는 Bluebird가 세 개의 commercial gene therapy를 보유했지만 uptake가 느렸고, 2024년 11월 기준 세 제품 전체에서 치료를 시작한 환자가 57명에 그쳤다고 보도했다. ([Reuters][13])

```text
case_type:
GENE_THERAPY_COMMERCIALIZATION_FAILURE_HARD_4C

stage 포착:
Stage 1 = 희귀질환 gene therapy approval
Stage 2 = approved products
Stage 4C = slow uptake, cash crunch, discounted take-private
가격경로 = -36%

가격경로 판정:
COMMERCIALIZATION_FAILURE_OVERLAY가 실제 주가하락과 정확히 맞았다.
```

**정규화 결론**

```text
GENE_THERAPY_RARE_DISEASE는 approval_status만으로 Stage 3 금지.

필수:
patient_uptake
reimbursement_status
commercial_revenue
cash_runway
going_concern_flag
```

---

### 5-4. Charles River — CRO도 biotech funding cycle을 피하지 못한다

Charles River Laboratories는 biotech 고객들의 funding crunch가 이어지면서 2024년 연간 전망을 낮췄고, 주가는 premarket에서 15% 하락했다. 회사는 drug discovery·development service 수요가 하반기에 개선될 것으로 보지 않는다고 밝혔고, 연간 adjusted profit 전망과 revenue 전망도 낮췄다. ([Reuters][14])

```text
case_type:
CRO_FUNDING_CYCLE_4C_WATCH

stage 포착:
Stage 1 = CRO 반복 서비스·임상수요
Stage 2 = backlog / customer R&D budget
Stage 4C = biotech funding crunch, forecast cut, revenue decline
가격경로 = premarket -15%

가격경로 판정:
CRO_FUNDING_CYCLE_OVERLAY가 실제 주가하락과 맞았다.
```

**정규화 결론**

```text
CRO_CLINICAL_SERVICE는 반복 서비스처럼 보이지만,
biotech funding cycle과 고객 R&D 예산을 반드시 통과해야 한다.
```

---

### 5-5. Teladoc / BetterHelp — 원격의료는 CAC·impairment·DTC demand가 무너지면 4C

Teladoc은 BetterHelp 관련 7.9억 달러 goodwill impairment를 기록했고, BetterHelp revenue는 9% 감소했다. 회사는 2024년 guidance를 철회했고, 주가는 extended session에서 15% 이상 하락했다. 이는 DTC telehealth가 사용자 수 narrative만으로 Green이 될 수 없고, CAC·retention·impairment·FCF를 통과해야 한다는 기준이다. ([마켓워치][15])

```text
case_type:
TELEHEALTH_DTC_FAILURE_4C

stage 포착:
Stage 1 = 원격의료·DTC mental health growth
Stage 2 = 사용자 기반·매출
Stage 4C = impairment, CAC pressure, forecast withdrawal
가격경로 = extended session -15% 이상

가격경로 판정:
DTC telehealth RedTeam이 실제 가격경로와 맞았다.
```

**정규화 결론**

```text
DIGITAL_HEALTHCARE_REMOTE_MEDICINE은 사용자 수가 아니라
payer contract, CAC, retention, FCF, privacy를 본다.
```

---

### 5-6. Biosimilar patent litigation — 허가·신청이 있어도 launch timing이 흔들린다

Amgen은 Samsung Bioepis의 Prolia/Xgeva biosimilar에 대해 34개 특허 침해를 주장하며 소송을 제기했다. Amgen은 biosimilar 생산·판매 금지와 손해배상을 요구했고, Prolia와 Xgeva의 미국 매출은 전년 기준 42억 달러 이상이었다. 이건 biosimilar가 FDA 신청·허가 단계에 있어도 patent litigation이 launch timing과 economics를 흔들 수 있음을 보여준다. ([Reuters][16])

```text
case_type:
BIOSIMILAR_PATENT_LITIGATION_4C_WATCH

stage 포착:
Stage 1 = biosimilar approval/application
Stage 2 = launch 준비
Stage 4C-watch = patent litigation, injunction risk, launch delay

가격경로 판정:
개별 price-path보다 commercialization gate로 적용.
```

**정규화 결론**

```text
BIOSIMILAR_COMMERCIALIZATION은 PBM/보험뿐 아니라 patent litigation도 필수 field.
```

---

### 5-7. Botox counterfeit / safety — 미용·반복시술도 안전채널이 깨지면 hard gate

FDA는 Botox와 유사한 counterfeit 또는 unapproved injectable wrinkle-smoothing products를 판매한 18개 웹사이트에 warning letters를 보냈다. AP는 FDA가 injury report와 toxic side effects 이후 조치했고, Botox류 제품은 호흡·삼킴에 영향을 줄 수 있는 boxed warning을 가진다고 보도했다. ([AP News][17])

```text
case_type:
DEVICE_SAFETY_COUNTERFEIT_OVERLAY_4C_WATCH

stage 포착:
Stage 1 = 미용시술 반복수요
Stage 2 = 허가·채널·수출
Stage 4C-watch = counterfeit product, unapproved injectable, injury report

가격경로 판정:
보톡스·미용기기는 반복수요가 있어도 licensed channel과 safety gate가 필수.
```

**정규화 결론**

```text
BOTULINUM_AESTHETIC_REGULATED는 허가·반복시술·수출이 있으면 후보.
하지만 counterfeit/safety flag가 켜지면 Stage 3-Green 차단.
```

---

## 6. 지금 점수표로 실제 stage를 어떻게 포착했고, 주가상승·하락과 잘 맞는지를 통한 점수비중정규화

R7 Loop 8부터 기본 점수표는 이렇게 재정규화한다.

```text
R7 v8 기본 점수표 = 100점

1. EPS/FCF·상업화 전환 가능성          24점
2. 처방·보험·수가·반복매출 visibility   22점
   - scripts
   - PBM/보험
   - reimbursement
   - procedure growth
   - instruments/accessories
   - CDMO 가동률
3. 병목·진입장벽·반복성                 14점
   - installed base
   - 장기계약
   - regulatory barrier
   - switching cost
4. cash runway·capital discipline         10점
5. 시장 오해·리레이팅 gap               8점
6. valuation room / 4B 여지              6점
7. 안전·규제·disclosure confidence       16점

Hard RedTeam:
승인 후 uptake 실패, reimbursement failure, cash crunch,
funding crunch, compounded GLP-1 crackdown, patent litigation,
subgroup AI failure, safety/counterfeit, device recall, CAC spike
```

### 6-1. stage별 점수 cap

```text
Stage 1 cap:
최대 45점

조건:
- 임상 결과
- FDA/EMA 승인 기대
- AI 의료 논문
- CDMO capacity 발표
- GLP-1 TAM
- biosimilar approval 기대
- 의료기기 신제품 뉴스

예:
pre-revenue biotech
AI 신약개발 platform
논문 성능만 있는 의료AI
```

```text
Stage 2 cap:
최대 70점

조건:
- FDA approval
- PBM/formulary 등재
- 계약·시설 인수
- procedure growth
- external validation
- pricing / launch plan
- stock reaction 확인

예:
Lilly Foundayo approval
Samsung Biologics Rockville facility
Cigna Humira biosimilar $0 copay
Lunit DBT external validation
```

```text
Stage 3:
70점 이상 가능

조건:
- 처방량·보험·reimbursement
- commercial revenue
- OPM/FCF
- procedure growth + instruments/accessories
- 반복 CDMO 계약·가동률
- 실제 가격경로 동행

예:
Intuitive Surgical은 사업구조상 Stage 2→3 후보.
Lilly oral GLP-1은 아직 scripts·보험·가격 데이터 전까지 Stage 2.
```

```text
Stage 4B:
점수는 높지만 기대수익률 감점

조건:
- GLP-1, 수술로봇, CDMO, 의료AI consensus 과밀
- valuation이 scripts/FCF보다 먼저 감
- TAM으로 multiple이 먼저 확장

예:
GLP-1 mega-TAM consensus
large-cap medtech valuation compression 구간
```

```text
Stage 4C:
hard RedTeam

조건:
- sales/profit decline warning
- price war
- compounded crackdown
- cash crunch
- discounted take-private
- forecast cut
- impairment
- patent litigation
- counterfeit/safety warning
```

---

### 6-2. 실제 가격경로와 맞은 case / 안 맞은 case

| case                           | 점수표가 잡은 stage |                                     실제 가격경로 확인 | 판정                                        | 정규화 조정                              |
| ------------------------------ | ------------: | ---------------------------------------------: | ----------------------------------------- | ----------------------------------- |
| Samsung Biologics Rockville    |       Stage 2 |                             발표 후 -0.4%, 시장 +2% | capacity만으로 Stage 3 금지                    | CDMO visibility 상향, EPS/FCF cap 유지  |
| Intuitive Surgical             |  Stage 2→3 후보 | Q1 procedure/revenue/EPS beat, Q4 beat에는 +0.4% | 사업구조는 강함, valuation room 확인 필요            | procedure/consumables 가중치 상향        |
| Lilly Foundayo approval        |       Stage 2 |                                      Lilly +4% | approval stage 포착 맞음                      | scripts·보험 전 Stage 3 제한             |
| Lilly maintenance data         |    Stage 2 강화 |   clinical data는 강함, price-path 추가 backfill 필요 | thesis 강화, commercial gate 필요             | refill/adherence field 추가           |
| Cigna/GoodRx Humira biosimilar |       Stage 2 |                  가격·access evidence, uptake 느림 | PBM/formulary gate 맞음                     | prescription volume 가중치 상향          |
| Lunit DBT external validation  |     Stage 1~2 |                    논문 evidence, price-path 미확정 | deployment 전 Green 금지                     | reimbursement/hospital adoption cap |
| Novo Nordisk                   |         4B→4C |                        -12%~-16%, 약 $50B 시총 감소 | GLP-1 price-war RedTeam 매우 잘 맞음           | price/gross-to-net 가중치 상향           |
| Hims & Hers                    |      4C-watch |                                    -11%~-14.6% | telehealth GLP-1 RedTeam 잘 맞음             | CAC/regulatory hard gate            |
| Bluebird bio                   |       hard 4C |                                           -36% | approval-without-commercialization 정확히 맞음 | patient uptake/cash runway 가중치 상향   |
| Charles River                  |      4C-watch |                                 premarket -15% | CRO funding cycle 잘 맞음                    | biotech funding overlay 강화          |
| Teladoc                        |       hard 4C |                               extended -15% 이상 | CAC/impairment gate 잘 맞음                  | DTC telehealth 감점 강화                |
| Amgen–Samsung Bioepis          |      4C-watch |                              patent litigation | launch timing gate                        | biosimilar patent field 필수          |
| Botox counterfeit              |      4C-watch |                         safety/regulatory gate | 반복시술 safety cap                           | licensed channel 필수                 |

---

### 6-3. R7 Loop 8 점수비중 재조정

이번 검증 결과 R7 점수표는 이렇게 조정한다.

```text
상향:
procedure growth + instruments/accessories
prescription volume / weekly scripts
PBM/보험/formulary gate
commercial revenue / reimbursement
cash runway
CRO funding-cycle overlay
GLP-1 price-war overlay
compounded GLP-1 regulatory gate
device safety/counterfeit gate
subgroup medical AI validation gate

유지:
CDMO capacity / U.S. manufacturing
biosimilar access program
medical AI external validation
oral GLP-1 approval
medical device export

하향 또는 cap:
approval-only biotech
AI drug discovery platform-only
medical AI AUC-only
telehealth user-growth-only
biosimilar discount-only
gene therapy approval without uptake
CDMO capacity without customer/utilization
```

구체적으로는 이렇게 간다.

| 항목                    | Loop 7 감각 |                                     Loop 8 조정 |
| --------------------- | --------: | --------------------------------------------: |
| EPS/FCF·상업화           |        중요 |           더 중요. Bluebird가 hard counterexample |
| 처방량·보험·수가             |        중요 |                    상향. GLP-1·biosimilar 모두 핵심 |
| 반복소모품                 |        중요 |                              상향. Intuitive 구조 |
| CDMO capacity         |        중요 |                유지. Samsung Bio는 price delayed |
| valuation room        |        보조 |             4B 감점 강화. GLP-1·medtech consensus |
| cash runway           |        보조 |                                  상향. Bluebird |
| funding cycle         |        보조 |                             상향. Charles River |
| safety/regulatory     |        보조 | hard gate. Hims, Botox, biosimilar litigation |
| medical AI validation |        보조 |          Stage 1~2로 제한. deployment 전 Green 금지 |

---

### 6-4. R7 Loop 8 archetype별 최종 stage 규칙

```text
CDMO_HEALTHCARE_CONTRACT:
Stage 1 = capacity / U.S. site / tariff hedge
Stage 2 = 고객계약, 생산시설, tech transfer, 가동률 계획
Stage 3 = 장기계약 + capacity utilization + OPM/FCF + 가격경로 동행
Stage 4B = CDMO premium 과열
Stage 4C = 고객계약 부재, 가동률 부진, CAPEX burden
```

```text
SURGICAL_ROBOT_INSTALLED_BASE:
Stage 1 = installed base / 신형 로봇 출시
Stage 2 = procedure growth, system placement
Stage 3 = instruments/accessories 반복매출 + guidance 상향 + FCF
Stage 4B = 수술로봇 platform premium 과열
Stage 4C = hospital CAPEX 둔화, procedure mix 악화, GLP-1 bariatric slowdown
```

```text
OBESITY_GLP1_COMMERCIALIZATION:
Stage 1 = GLP-1 TAM / 임상 결과
Stage 2 = FDA approval, pricing, launch, scripts 초기 데이터
Stage 3 = weekly scripts + insurance + gross-to-net + OP/EPS
Stage 4B = GLP-1 mega-TAM consensus 과열
Stage 4C = price war, copycat, competition, sales/profit decline
```

```text
GLP1_TELEHEALTH_CHANNEL:
Stage 1 = DTC GLP-1 access
Stage 2 = branded partnership, subscriber growth
Stage 3 = CAC 안정 + gross margin + compliance + FCF
Stage 4C = FDA crackdown, legal cost, revenue recognition shock, margin collapse
```

```text
GENE_THERAPY_RARE_DISEASE:
Stage 1 = FDA approval / 희귀질환 unmet need
Stage 2 = patient initiation, reimbursement, commercial launch
Stage 3 = 충분한 uptake + FCF + cash runway
Stage 4C = slow uptake, cash crunch, going concern, discounted take-private
```

```text
BIOSIMILAR_COMMERCIALIZATION:
Stage 1 = approval / interchangeable designation
Stage 2 = PBM/formulary, $0 copay, cash-pay access
Stage 3 = prescription switch + revenue + margin 방어
Stage 4C = patent litigation, PBM exclusion, price competition, slow uptake
```

```text
MEDICAL_AI_EXTERNAL_VALIDATION:
Stage 1 = 논문/AUC/외부검증
Stage 2 = subgroup analysis + pilot deployment
Stage 3 = hospital adoption + reimbursement code + recurring revenue
Stage 4C = subgroup underperformance, liability, no reimbursement, workflow failure
```

```text
BOTULINUM_AESTHETIC_REGULATED:
Stage 1 = 미용시술 반복수요
Stage 2 = 허가, 수출, licensed channel
Stage 3 = 반복시술 + OPM + 안전 유통
Stage 4C = counterfeit, unapproved injectable, FDA warning, injury reports
```

---

# R7 Loop 8 결론

이번 R7 Loop 8의 핵심은 이거다.

```text
R7은 “허가·논문·임상”과 “상업화·반복매출·FCF”를 가장 강하게 분리해야 하는 라운드다.
```

```text
Stage 포착이 잘 맞은 사례:
Samsung Biologics = 미국 Rockville 60,000L capacity, Stage 2이지만 가격경로 약함
Intuitive Surgical = procedure growth + 반복소모품 구조, Stage 2→3 후보
Lilly Foundayo = FDA approval + 가격경로 +4%, Stage 2
Humira biosimilar = PBM/formulary/access Stage 2, 실제 처방전환은 느림
Lunit DBT = external validation Stage 1~2, deployment 전 Green 금지

RedTeam이 가격경로와 잘 맞은 사례:
Novo Nordisk = price war / competition warning → -12%~-16%, 약 $50B 시총 감소
Hims & Hers = compounded GLP-1 / branded pivot cost → -11%~-14.6%
Bluebird bio = 승인 후 상업화 실패·cash crunch → -36%
Charles River = CRO funding crunch → premarket -15%
Teladoc = BetterHelp impairment·CAC → extended -15% 이상
Amgen–Samsung Bioepis = biosimilar patent litigation
Botox counterfeit = device/aesthetic safety gate
```

**R7 Loop 8 점수정규화의 핵심 문장:**

> 바이오·헬스케어·의료기기는 “FDA 승인”, “임상 성공”, “AI AUC”, “CDMO capacity”, “GLP-1 TAM”이 아니라 **처방량, 보험·PBM·수가, commercial revenue, 반복시술·소모품, 가동률, OPM/FCF, cash runway, safety/regulatory gate, 실제 가격경로**로 봐야 한다.
> 이번 Loop 8에서는 `Intuitive Surgical`, `Lilly Foundayo`, `Samsung Biologics`, `Humira biosimilar access`, `Lunit DBT validation`이 Stage 1~2 이상을 포착할 수 있는 사례이고, `Novo`, `Hims`, `Bluebird`, `Charles River`, `Teladoc`, `biosimilar patent litigation`, `Botox counterfeit`이 R7 RedTeam이 실제 가격·사업경로와 맞는 반례다.

다음 순서는 **R8 — 플랫폼·콘텐츠·SW·보안 Loop 8**다.

[1]: https://www.reuters.com/business/healthcare-pharmaceuticals/samsung-biologics-buy-us-drug-production-facility-gsk-280-mln-2025-12-21/?utm_source=chatgpt.com "Samsung Biologics to buy US drug production facility from GSK for $280 million"
[2]: https://www.investors.com/news/technology/intuitive-surgical-stock-intuitive-surgical-earnings-q1-2026/?utm_source=chatgpt.com "Why Robotic Surgery's Titan, Intuitive Surgical, Just Made A Bullish Move"
[3]: https://www.barrons.com/articles/intuitive-surgical-stock-price-earnings-f62a00a0?utm_source=chatgpt.com "Intuitive Surgical Stock Beats Earnings Estimates. The Stock Is Barely Moving."
[4]: https://www.ft.com/content/a64cd0a7-3ad2-4298-b2fa-22d57088ae4d?utm_source=chatgpt.com "Eli Lilly wins US approval for weight-loss pill"
[5]: https://www.reuters.com/legal/litigation/patients-dont-regain-much-weight-switching-injections-lillys-weight-loss-pill-2026-05-12/?utm_source=chatgpt.com "Patients don't regain much weight switching from injections to Lilly's weight-loss pill, study finds"
[6]: https://www.reuters.com/business/healthcare-pharmaceuticals/cigna-offer-humira-rivals-with-0-copay-specialty-pharmacy-2024-04-25/?utm_source=chatgpt.com "Cigna to offer Humira rivals with $0 copay at specialty pharmacy"
[7]: https://www.reuters.com/business/healthcare-pharmaceuticals/boehringer-goodrx-partner-offer-humira-rival-92-discount-2024-07-18/?utm_source=chatgpt.com "Boehringer-GoodRx partner to offer Humira rival at 92% discount"
[8]: https://arxiv.org/abs/2503.13581?utm_source=chatgpt.com "Subgroup Performance of a Commercial Digital Breast Tomosynthesis Model for Breast Cancer Detection"
[9]: https://www.reuters.com/business/novo-nordisk-warns-2026-sales-decline-2026-02-03/?utm_source=chatgpt.com "Novo Nordisk warns on profits and sales amid Trump drug price crackdown"
[10]: https://www.reuters.com/business/healthcare-pharmaceuticals/novo-nordisk-plunge-wipes-50-billion-off-obesity-drug-giant-2026-02-04/?utm_source=chatgpt.com "Novo Nordisk plunge wipes $50 billion off obesity drug giant"
[11]: https://www.reuters.com/legal/litigation/hims-hers-plunges-after-weight-loss-pivot-hits-quarterly-results-2026-05-12/?utm_source=chatgpt.com "Hims & Hers plunges as branded weight-loss drug pivot hits results"
[12]: https://www.barrons.com/articles/hims-hers-earnings-stock-price-84ffc4ae?utm_source=chatgpt.com "Hims & Hers Stock Sinks. Why Earnings Offered Wall Street a Big Surprise."
[13]: https://www.reuters.com/markets/deals/bluebird-bio-be-taken-private-by-carlyle-sk-capital-amid-cash-crunch-2025-02-21/?utm_source=chatgpt.com "Gene therapy maker bluebird to go private in discounted deal amid cash crunch"
[14]: https://www.reuters.com/business/healthcare-pharmaceuticals/charles-river-cuts-2024-forecast-funding-crunch-among-biotech-clients-persists-2024-08-07/?utm_source=chatgpt.com "Charles River cuts 2024 forecast as funding crunch among biotech clients persists"
[15]: https://www.marketwatch.com/story/teladoc-posts-another-quarterly-loss-and-online-mental-health-unit-sees-revenue-slip-c906e9f3?utm_source=chatgpt.com "Teladoc posts another quarterly loss, and online mental-health unit sees revenue slip"
[16]: https://www.reuters.com/legal/litigation/amgen-sues-samsung-biotech-unit-over-bone-drug-copies-2024-08-13/?utm_source=chatgpt.com "Amgen sues Samsung biotech unit over bone drug copies"
[17]: https://apnews.com/article/67afcdc72e100204181c20aacec39d89?utm_source=chatgpt.com "FDA warns websites selling unapproved Botox for cosmetic purposes"

좋아. **R6 Loop 2까지 끝났으니, 이번은 R7 Loop 2 — 바이오·헬스케어·의료기기**로 넘어간다.

이번 2회차 R7의 목표는 1회차보다 더 단단하게 잡는다.

```text
허가
≠ 상업화

임상 성공
≠ EPS/FCF 체급 변화

AI 신약개발
≠ 바로 Green

의료AI 성능 논문
≠ 병원 도입·수가·반복매출

CDMO·의료기기·임플란트·미용기기
= 계약·가동률·반복시술·수출·OPM이 있으면 Green 가능
```

R7은 Theme Tag Map 기준으로 CDMO, CRO, 바이오시밀러, 의료AI, 원격의료, AI 신약개발, 비만치료제, 유전자치료제, 보톡스, 임플란트, 미용기기, 수술용 로봇, 전염병 진단 등을 흡수하는 대섹터다. 여기서 핵심은 **pre-revenue biotech은 Green 거의 금지**, **royalty/commercialization biotech은 실제 매출화·로열티 필요**, **CDMO/medical device는 장기계약·반복매출이면 Green 가능**으로 나누는 것이다.

그리고 Checkpoint 20 원칙처럼, 계약금액, 생산 capacity, 처방량, 매출 대비 계약금액, OP YoY, 보험 등재, 수가, 반복매출 같은 필드는 실제 공시·리포트·기사에서 확인될 때만 써야 한다. 없는 숫자를 추정해서 넣으면 바이오 쪽에서는 특히 false-positive가 커진다.
서생원식으로도 이 라운드는 “바이오 뉴스”가 아니라 **EPS/FCF 체급 변화와 밸류에이션 리레이팅이 동시에 일어나는 구조**를 찾는 라운드다.

---

# R7 Loop 2. 바이오·헬스케어·의료기기

## 1. 이번 라운드 대섹터

```text
R7 = 바이오·헬스케어·의료기기
Loop 2 목표 = 허가·임상·AI·논문 뉴스와 실제 상업화·반복매출·FCF를 분리
```

이번 회차의 핵심 질문은 이거다.

```text
이 회사는 실제로 돈을 벌고 있는가?
아니면 허가·임상·논문·AI·시장규모 narrative만 있는가?
```

R7의 오판 포인트는 반복된다.

```text
1. FDA/EMA 허가를 실제 처방·매출로 착각
2. 바이오시밀러 승인을 PBM/보험 등재·처방전환으로 착각
3. GLP-1 시장 크기를 가격·경쟁·조제약 리스크 없이 Green 처리
4. 유전자치료제 승인 후 상업화·환급·현금 runway를 무시
5. AI 신약개발 플랫폼을 승인약·milestone 없이 Green 처리
6. 의료AI 논문 성능을 병원도입·수가·반복매출로 오판
7. 원격의료/telehealth 사용자 수를 CAC·privacy·FCF 없이 Green 처리
```

---

## 2. 대상 canonical archetype

| canonical archetype                  | Loop 2 정책                                           |
| ------------------------------------ | --------------------------------------------------- |
| `CDMO_HEALTHCARE_CONTRACT`           | Green 가능. 장기계약·capacity·가동률·고객사 다변화 필요              |
| `CRO_CLINICAL_SERVICE`               | Watch-to-Green. backlog·고객사 R&D 예산·funding cycle 확인 |
| `BIOSIMILAR_COMMERCIALIZATION`       | Watch-to-Green. 허가보다 PBM/보험·처방전환·마진 필요              |
| `BIOSIMILAR_ORIGINATOR_DEFENSE`      | Watch. patent cliff와 후속 신약 전환 분리                    |
| `OBESITY_GLP1_COMMERCIALIZATION`     | Green 가능하지만 4B/4C 감시 강함. 처방량·보험·가격·경쟁 필요            |
| `GENE_THERAPY_RARE_DISEASE`          | Watch/Red. 승인 후 상업화·환급·cash runway 없으면 Green 금지     |
| `AI_DRUG_DISCOVERY_PLATFORM`         | Watch/Red. AI 플랫폼보다 milestone·임상·승인 가능성 필요          |
| `DIGITAL_HEALTHCARE_AI`              | Watch-to-Green. 외부검증 + 병원도입 + 수가 + 반복매출 필요          |
| `DIGITAL_HEALTHCARE_REMOTE_MEDICINE` | Watch. 규제·수가·unit economics 필요                      |
| `TELEHEALTH_BEHAVIORAL_HEALTH`       | Watch/Red. CAC·privacy·impairment 리스크 큼             |
| `PHARMA_CHANNEL_AND_PRIVACY_RISK`    | RedTeam overlay. 조제약·광고·개인정보·품질 리스크                 |
| `MEDICAL_DEVICE_HEALTHCARE_EXPORT`   | Green 가능. 수출국·반복시술·소모품·OPM 확인                       |
| `MEDICAL_DEVICE_DENTAL_IMPLANT`      | Green 가능. 다만 VBP·가격통제 감시                            |
| `BOTULINUM_AESTHETIC_REGULATED`      | Watch-to-Green. 허가·안전채널·반복시술 필요                     |
| `DIAGNOSTICS_INFECTIOUS_DISEASE`     | Red/Watch. one-off 진단 수요와 구조적 진단 플랫폼 분리             |
| `ANIMAL_HEALTH_BIOSECURITY`          | Watch. 정부 비축·반복 접종 확인 필요                            |

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

CRO_CLINICAL_SERVICE
- CRO
- 임상시험수탁
- preclinical service
- lab service
- backlog
- 고객사 R&D 예산
- biotech funding cycle

BIOSIMILAR_COMMERCIALIZATION
- Humira biosimilar
- Stelara biosimilar
- Prolia biosimilar
- PBM 등재
- 보험 커버리지
- 처방전환
- 가격경쟁
- interchangeability

OBESITY_GLP1_COMMERCIALIZATION
- Wegovy
- Ozempic
- Zepbound
- oral GLP-1
- orforglipron / Foundayo
- compounded GLP-1
- telehealth channel
- 보험 커버리지
- 가격 인하
- 처방량

GENE_THERAPY_RARE_DISEASE
- 희귀질환
- 유전자치료제
- 고가 치료제
- 환자 모집
- 보험·환급
- 제조 안정성
- cash runway
- going concern

AI_DRUG_DISCOVERY_PLATFORM
- AI 신약개발
- 후보물질 발굴
- 임상 진입
- big pharma partnership
- milestone
- cash runway
- platform hype

DIGITAL_HEALTHCARE_AI
- 의료영상 AI
- mammography AI
- 병원 workflow
- 외부검증
- subgroup performance
- 수가/보험
- 의료책임

DIGITAL_HEALTHCARE_REMOTE_MEDICINE
- 원격의료
- 병원·보험 연동
- wearable
- EMR integration
- chronic care
- B2B/B2B2C 계약

TELEHEALTH_BEHAVIORAL_HEALTH
- 온라인 정신건강
- BetterHelp류 DTC
- CAC
- 광고비
- privacy
- churn
- impairment

MEDICAL_DEVICE_HEALTHCARE_EXPORT
- 미용기기
- 보톡스
- 임플란트
- 수술용 로봇
- 반복시술
- 소모품
- 해외 허가
- ASP/OPM

PHARMA_CHANNEL_AND_PRIVACY_RISK
- telehealth drug channel
- compounded drug
- branded drug transition
- FDA warning
- legal settlement
- 개인정보
- 광고 규제
```

---

# 4. 성공사례

## 4-1. Samsung Biologics 미국 생산거점 — `CDMO_HEALTHCARE_CONTRACT`

Samsung Biologics는 GSK로부터 미국 Rockville 소재 생산시설을 2.8억 달러에 인수해 첫 미국 생산거점을 확보하기로 했다. 해당 시설은 60,000L drug substance capacity를 갖고 있고, Samsung Biologics는 장기 미국 수요 대응과 기술 업그레이드를 위해 추가 투자를 계획했다. 다만 발표 당일 Samsung Biologics 주가는 0.4% 하락했고, 코스피가 2% 상승한 것과 비교하면 즉시 가격경로는 약했다. ([Reuters][1])

```text
가격경로 1차 판정:
STRATEGIC_CDMO_SUCCESS_CANDIDATE / PRICE_ALIGNMENT_DELAYED

좋은 점:
- 첫 미국 생산거점
- 60,000L capacity
- 장기 미국 수요 대응
- 관세·현지생산 리스크 완화

주의:
- 발표 직후 주가 부진
- 인수 후 가동률
- 고객계약
- 추가 CAPEX
- 미국 인건비·운영비
```

**Loop 2 교정**

```text
CDMO_HEALTHCARE_CONTRACT:
Green 가능 유지.
하지만 “capacity 확보”만으로 Stage 3 금지.
가동률 + 고객사 계약 + FCF 전환이 필요.
```

---

## 4-2. Samsung Biologics CDMO 구조 reference

Samsung Biologics는 항체, 이중항체, ADC, mRNA 백신 등 대규모 바이오의약품 생산 서비스를 제공하는 CDMO이고, Pfizer, GSK, Eli Lilly, AstraZeneca, Bristol-Myers Squibb 같은 대형 제약사와 협력해 온 회사로 정리된다. 2025년 기준 Plant 5 추가 후 총 capacity가 785,000L로 확대되는 구조도 언급된다. ([위키백과][2])

```text
가격경로 1차 판정:
CDMO_STRUCTURAL_REFERENCE

의미:
CDMO는 R7에서 드물게 숫자로 검증 가능한 Green 후보.
임상 뉴스가 아니라 계약·capacity·가동률·OPM으로 점수화 가능.
```

**Loop 2 교정**

```text
CDMO score 강화 조건:
- 장기 제조계약
- capacity utilization 상승
- 고객사 다변화
- ADC/mAb 등 고부가 생산 mix
- OP margin / FCF 개선
```

---

## 4-3. Straumann / 치아·임플란트 — `MEDICAL_DEVICE_DENTAL_IMPLANT`

Straumann은 2025년 매출 26.1억 스위스프랑으로 시장 예상치를 웃돌았고, 2026년 high single-digit sales growth를 제시했다. 중국 volume-based procurement, 즉 VBP 불확실성이 남아 있지만, 유럽·북미·아시아태평양에서 견조한 실적이 확인됐고, 발표 후 주가는 장중 최대 6%, 이후 1.6% 상승했다. ([Reuters][3])

```text
가격경로 1차 판정:
MEDICAL_DEVICE_ALIGNED_CANDIDATE

좋은 점:
- 매출 예상 상회
- 고정적 의료기기 수요
- 지역 다변화
- 가격경로 양호

주의:
- 중국 VBP 가격통제
- ASP 하락 가능성
- 현지 제조 우대 가능성
- 경쟁 심화
```

**Loop 2 교정**

```text
MEDICAL_DEVICE_DENTAL_IMPLANT:
Green 가능 유지.
다만 VBP/가격통제 overlay를 반드시 붙인다.
```

---

## 4-4. Lilly oral GLP-1 Foundayo — `OBESITY_GLP1_COMMERCIALIZATION`

Eli Lilly의 oral GLP-1 비만치료제 Foundayo는 2026년 4월 FDA 승인을 받았고, 월 149달러 가격으로 LillyDirect를 통해 출시됐다. Reuters는 Foundayo가 trial에서 12~15% 체중감량을 보였고, 음식·물 섭취 조건이 까다로운 Novo의 Wegovy pill과 달리 복용 편의성이 있다고 보도했다. 승인 뉴스에서 Lilly 주가는 6% 올랐고, Novo는 소폭 하락했다. ([Reuters][4])

그런데 출시 4주차 처방은 7,335건으로 초기 uptake가 modest했고, 2분기 컨센서스 매출 1.6억 달러를 맞추려면 주당 22,000건 처방이 필요하다는 분석도 나왔다. 즉 “승인+대형 시장”은 Stage 1~2이지만, Stage 3는 처방량·보험·가격·OP/EPS가 따라와야 한다. ([Reuters][5])

```text
가격경로 1차 판정:
HIGH_GROWTH_WATCH_TO_GREEN

좋은 점:
- FDA 승인
- oral GLP-1 편의성
- 대형 obesity market
- 주가 승인 반응 +6%

주의:
- 초기 처방량 modest
- 컨센서스 충족 불확실
- 경쟁, 보험, 가격
- telehealth 처방 추적 문제
```

**Loop 2 교정**

```text
OBESITY_GLP1_COMMERCIALIZATION:
시장규모는 점수 근거가 아니다.
weekly scripts, coverage, price, supply, OP/EPS가 필요.
```

---

## 4-5. Foundayo switch-maintenance data — GLP-1 장기 유지요법 후보

Lilly의 late-stage trial에서는 주사 GLP-1에서 Foundayo로 전환한 환자들이 체중을 크게 되찾지 않았다는 결과가 나왔다. Reuters에 따르면 Wegovy에서 전환한 환자는 1년 동안 평균 약 2파운드, Zepbound에서 전환한 환자는 약 11파운드만 되찾았고, 52주차에 semaglutide 전환군은 체중감량의 79.3%, tirzepatide 전환군은 74.7%를 유지했다. 이건 oral GLP-1이 단순 launch 제품이 아니라 **장기 유지요법 시장**으로 확장될 수 있는 근거다. ([Reuters][6])

```text
가격경로 1차 판정:
GLP1_MAINTENANCE_STRUCTURAL_CANDIDATE

의미:
GLP-1은 단순 체중감량 신약이 아니라 장기 유지요법·복용편의성 시장으로 확장 가능.
다만 보험·가격·경쟁이 valuation을 좌우한다.
```

---

## 4-6. 의료AI / Lunit DBT external validation — `DIGITAL_HEALTHCARE_AI`

Lunit INSIGHT DBT 모델을 163,449건 screening mammography exams에 대해 외부검증한 연구는 전체 AUC 0.91을 보였고, recall은 0.73이었다. 다만 non-invasive cancer, calcifications, dense breast tissue subgroup에서는 성능이 낮아질 수 있어, 의료AI를 도입할 때 전체 평균 성능뿐 아니라 subgroup risk를 봐야 한다고 정리된다. ([arXiv][7])

```text
가격경로 1차 판정:
CLINICAL_VALIDATION_CANDIDATE / COMMERCIALIZATION_UNPROVEN

좋은 점:
- 대규모 외부검증
- 전체 AUC 0.91
- 의료영상 workflow 개선 가능성

주의:
- subgroup performance
- 병원 도입
- 수가/보험
- 반복매출
- 의료책임
```

**Loop 2 교정**

```text
DIGITAL_HEALTHCARE_AI:
논문 성능은 Stage 1~2 증거.
Stage 3는 hospital adoption + reimbursement + recurring revenue가 필요.
```

---

## 4-7. 바이오시밀러 가격 접근성 — `BIOSIMILAR_COMMERCIALIZATION`

Boehringer Ingelheim과 GoodRx는 Humira biosimilar를 정가 대비 92% 할인된 가격으로 제공하기로 했다. 하지만 Reuters는 Boehringer의 Cyltezo가 2024년 5월 약 2,500건 처방에 그친 반면 Humira는 600,000건 이상 처방됐다고 보도했다. 즉 바이오시밀러는 “싸다”는 장점이 있어도 PBM·보험·의사·환자 전환이 느리면 EPS/FCF로 바로 이어지지 않는다. ([Reuters][8])

```text
가격경로 1차 판정:
BIOSIMILAR_ACCESS_CANDIDATE_BUT_SLOW_UPTAKE

좋은 점:
- 92% discount
- 접근성 개선 가능성
- 교체 가능성

주의:
- 처방 전환 느림
- PBM incentive 부족
- 가격경쟁으로 마진 압박
```

**Loop 2 교정**

```text
BIOSIMILAR_COMMERCIALIZATION:
허가와 가격할인만으로 Green 금지.
PBM/보험 등재 + 처방전환 + 마진 방어가 Stage 3 조건.
```

---

# 5. 반례

## 5-1. Novo Nordisk — GLP-1도 4B에서 4C로 갈 수 있다

Novo Nordisk는 GLP-1 비만치료제의 대표 성장기업이지만, 2026년 sales와 operating profit이 5~13% 감소할 수 있다고 경고하자 주가가 16% 하락해 약 500억 달러 시가총액이 사라졌다. 하락 원인은 미국 가격 하락 압박과 반복된 실망감이었다. ([Reuters][9])

```text
가격경로 1차 판정:
GLP1_4B_TO_4C_CASE

교훈:
거대한 시장규모
≠ Green 유지

4C 조건:
- 가격 하락
- 경쟁 심화
- 보험/환급 압박
- compounded/generic 대체
- 처방 성장 둔화
```

**Loop 2 교정**

```text
OBESITY_GLP1_COMMERCIALIZATION:
EPS/FCF 점수는 높게 둘 수 있지만,
price pressure와 competition penalty를 더 강하게 둔다.
```

---

## 5-2. Hims & Hers — GLP-1 telehealth channel risk

Hims & Hers는 compounded GLP-1에서 branded Wegovy 등으로 전환하면서 2026년 1분기 매출이 기대치를 밑돌고 예상 밖 손실을 냈다. Reuters는 이 전략 전환이 restructuring cost와 revenue recognition timing 문제를 만들었고, 주가가 장중 11% 하락해 약 7.3억 달러 시가총액이 사라질 수 있다고 보도했다. ([Reuters][10])
같은 회사는 Novo Nordisk와 Wegovy/Ozempic 판매 계약을 맺고 GLP-1 compounded 제품 광고를 중단하기로 했고, 이 합의 뉴스에서는 주가가 40% 이상 급등했다. 이건 telehealth channel이 큰 가격반응을 만들 수 있지만, 규제·제휴·마진·수익인식 리스크가 매우 크다는 뜻이다. ([Reuters][11])

```text
가격경로 1차 판정:
PHARMA_CHANNEL_HIGH_VOLATILITY_WATCH

교훈:
telehealth GLP-1 channel
≠ 안정적 Green

필수 확인:
- 합법적 처방채널
- branded/compounded mix
- CAC
- revenue recognition
- margin
- FCF
```

---

## 5-3. Hims compounded GLP-1 crackdown — `PHARMA_CHANNEL_AND_PRIVACY_RISK`

Novo Nordisk는 Hims가 compounded Wegovy pill을 월 49달러에 제공하려 하자 법적·규제 조치를 예고했고, FDA도 copycat GLP-1 단속을 시사했다. 이후 Hims는 compounded semaglutide pill 제공을 중단했다. Reuters는 FDA가 품질·안전·연방법 위반 가능성을 이유로 GLP-1 원료 사용을 제한하려 했고, HHS가 DOJ referral을 언급했다고 보도했다. ([Reuters][12])

```text
가격경로 1차 판정:
COMPOUNDED_GLP1_REGULATORY_4C_WATCH

의미:
비만치료제 수요가 커도 유통채널이 회색이면 Green 금지.
```

---

## 5-4. Bluebird bio — 유전자치료제 승인 후 상업화 실패

Bluebird bio는 승인된 유전자치료제를 갖고 있었지만 severe cash crunch로 Carlyle과 SK Capital에 주당 3달러에 비상장화되기로 했고, 이 가격은 직전 종가 대비 57.4% 할인된 수준이었다. 발표 후 주가는 36% 하락했고, 과거 2018년 약 150달러에 거래되던 주식은 극적으로 무너졌다. Reuters는 Bluebird의 gene therapy uptake가 느렸고 초기 사용도 중증 환자 중심이었다고 보도했다. ([Reuters][13])

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

---

## 5-5. Charles River — CRO도 funding cycle에서 자유롭지 않다

Charles River Laboratories는 biotech 고객들의 funding crunch가 이어지면서 2024년 전망을 낮췄고, 주가는 premarket에서 15% 하락했다. 회사는 drug discovery·development service 수요가 하반기에 개선될 것으로 기대하지 않는다고 밝혔고, 연간 매출도 2.5~4.5% 감소할 것으로 전망했다. ([Reuters][14])

```text
가격경로 1차 판정:
CRO_FUNDING_CYCLE_4C_WATCH

교훈:
CRO는 pre-revenue biotech보다 낫지만,
biotech funding cycle과 고객 R&D 예산이 꺾이면 Green 금지.
```

---

## 5-6. Teladoc / BetterHelp — telehealth DTC 모델의 실패

Teladoc은 BetterHelp 관련 7.9억 달러 impairment를 기록하고 연간·장기 전망을 철회했으며, 주가는 13% 하락해 record low를 기록했다. Reuters는 BetterHelp의 높은 광고비, 매출 둔화, customer acquisition expense 증가가 핵심 문제였다고 설명했다. ([Reuters][15])

```text
가격경로 1차 판정:
TELEHEALTH_DTC_FAILURE_4C

교훈:
원격의료 수요
≠ 지속가능한 business model

필수 확인:
- CAC
- churn
- 보험/고용주 계약
- privacy
- FCF
```

---

## 5-7. AI 신약개발 플랫폼 — 아직 대부분 Watch/Red

Recursion은 Exscientia를 6.88억 달러 all-stock deal로 인수해 AI-driven drug discovery 역량과 pipeline을 강화하려 했고, 합병 후 약 8.5억 달러 cash를 통해 3년 운영을 지원할 수 있다고 보도됐다. 하지만 drug development는 임상·승인·매출까지 매우 긴 시간이 걸리고, AI 플랫폼 자체가 EPS/FCF를 만드는 것은 아니다. ([Reuters][16])

```text
가격경로 1차 판정:
AI_DRUG_PLATFORM_WATCH

교훈:
AI 신약개발 플랫폼은 milestone과 임상 성공 전까지 Green 금지.
cash runway는 필요조건이지 충분조건이 아니다.
```

---

## 5-8. Botox counterfeit / safety risk

미국 FDA는 counterfeit 또는 unapproved Botox류 제품을 판매한 18개 웹사이트에 warning letters를 보냈고, 독성 부작용과 상해 사례도 보고됐다. Botox와 FDA 승인 대체품은 cosmetic·medical use가 가능하지만 boxed warning도 가진다. ([AP News][17])

```text
가격경로 1차 판정:
AESTHETIC_SAFETY_REGULATORY_4C_WATCH

교훈:
보톡스·미용시술은 반복수요가 있지만,
허가·유통채널·안전성이 깨지면 hard RedTeam.
```

---

# 6. 4B-watch 사례

## 6-1. GLP-1 obesity market 4B-watch

```text
4B 조건:
- 비만치료제 시장규모 narrative가 과밀
- Lilly/Novo 목표가와 valuation이 처방량보다 먼저 상승
- 가격·보험·compounded/generic risk를 시장이 무시
- telehealth 채널의 규제 리스크를 낮게 봄
```

Novo의 16% 급락과 500억 달러 시총 증발은 GLP-1도 거대한 TAM만으로 Green 유지가 안 된다는 기준이다. ([Reuters][9])

---

## 6-2. CDMO capacity premium 4B-watch

```text
4B 조건:
- CDMO capacity 확장만으로 valuation 상승
- 실제 고객계약·가동률·OPM 확인 전 가격이 먼저 감
- 미국 생산거점·tariff narrative가 과밀
```

Samsung Biologics의 미국 생산거점 인수는 전략적이지만, 발표 당일 주가는 0.4% 하락했고 시장을 이기지 못했다. 전략과 즉시 가격경로를 분리해야 한다. ([Reuters][1])

---

## 6-3. 의료기기·임플란트 4B-watch

```text
4B 조건:
- 임플란트·미용기기 수출 성장 narrative가 과밀
- 중국 VBP·가격통제 리스크를 낮게 봄
- ASP 하락보다 수요 증가만 반영
```

Straumann은 실적과 가이던스가 좋았지만, 중국 VBP 불확실성을 계속 언급했다. ([Reuters][3])

---

## 6-4. 의료AI 4B-watch

```text
4B 조건:
- AI 의료영상 논문·AUC 수치만으로 관련주 급등
- 병원 도입·수가·반복매출 없음
- subgroup performance와 책임소재를 무시
```

Lunit DBT 외부검증은 의미 있는 clinical evidence지만, subgroup risk와 임상 deployment 문제를 동시에 보여준다. ([arXiv][7])

---

## 6-5. 바이오시밀러 4B-watch

```text
4B 조건:
- biosimilar approval만으로 관련주 급등
- PBM/보험/처방전환 확인 전 가격이 먼저 감
- 할인율이 큰데 마진 방어를 확인하지 않음
```

Humira biosimilar는 92% discount가 있어도 처방전환이 매우 느렸다. ([Reuters][8])

---

# 7. 4C-thesis-break 사례

## 7-1. Bluebird gene therapy cash crunch

```text
4C:
cash crunch
slow uptake
reimbursement uncertainty
commercialization failure
discounted take-private
going concern risk
```

Bluebird는 유전자치료제 승인 후에도 상업화와 현금흐름이 따라오지 않으면 어떻게 무너지는지 보여주는 기준 사례다. ([Reuters][13])

---

## 7-2. GLP-1 price / competition collapse

```text
4C-watch:
price cut
competition
compounded alternatives
generic pressure
insurance/reimbursement risk
sales/profit decline
```

Novo의 2026년 sales·operating profit 감소 경고와 주가 16% 하락은 GLP-1의 4B→4C 전환 기준이다. ([Reuters][9])

---

## 7-3. CRO funding crunch

```text
4C:
biotech funding crunch
customer R&D budget cut
backlog slowdown
forecast cut
revenue decline
```

Charles River의 forecast cut과 premarket -15%는 CRO도 funding cycle에 묶인다는 기준이다. ([Reuters][14])

---

## 7-4. Telehealth CAC / impairment

```text
4C:
DTC advertising cost
CAC increase
BetterHelp impairment
forecast withdrawal
record-low stock
privacy risk
```

Teladoc은 원격의료·온라인 정신건강이 사용자 수보다 CAC·privacy·반복계약·FCF가 중요하다는 hard counterexample이다. ([Reuters][15])

---

## 7-5. Compounded GLP-1 regulatory break

```text
4C-watch:
FDA crackdown
illegal mass compounding allegation
unapproved copycat drug
DOJ referral risk
branded-drug pivot cost
```

Hims의 compounded GLP-1 중단과 branded drug 전환은 pharma channel이 규제에 얼마나 민감한지 보여준다. ([Reuters][12])

---

## 7-6. Botox counterfeit / unapproved product

```text
4C-watch:
counterfeit product
unapproved injectable
FDA warning
injury reports
licensed-channel failure
```

보톡스·미용시술은 반복수요가 있어도 안전성과 허가 채널이 깨지면 Stage 3-Green을 유지하면 안 된다. ([AP News][17])

---

# 8. 점수비중 보정표 — R7 Loop 2 / v2.0

| canonical archetype                  | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | Loop 2 핵심 감점                             |
| ------------------------------------ | ------: | ---------: | ---------: | ---------: | --------: | ------: | ---: | ---------------------------------------- |
| `CDMO_HEALTHCARE_CONTRACT`           |      20 |         24 |         12 |         12 |        12 |       0 |    5 | 가동률, 고객집중, CAPEX, 미국 운영비                 |
| `CRO_CLINICAL_SERVICE`               |      17 |         18 |          7 |         11 |        10 |       0 |    5 | biotech funding, 고객 예산, forecast cut     |
| `BIOSIMILAR_COMMERCIALIZATION`       |      18 |         19 |          6 |         12 |        10 |       0 |    6 | 가격경쟁, PBM, 처방전환 지연, 마진                   |
| `BIOSIMILAR_ORIGINATOR_DEFENSE`      |      19 |         18 |          8 |         13 |        11 |       2 |    6 | patent cliff, 후속 신약 실패, pricing pressure |
| `OBESITY_GLP1_COMMERCIALIZATION`     |      22 |         20 |         12 |         13 |        11 |       0 |    6 | 경쟁, 가격, 보험, 조제약, telehealth channel      |
| `GENE_THERAPY_RARE_DISEASE`          |       7 |         11 |          8 |          9 |         5 |       0 |    5 | cash burn, 환급, 상업화 지연, going concern     |
| `AI_DRUG_DISCOVERY_PLATFORM`         |       6 |         10 |          7 |         12 |         6 |       0 |    5 | 승인약 부재, 임상실패, platform hype              |
| `DIGITAL_HEALTHCARE_AI`              |      18 |         17 |          8 |         13 |        12 |       0 |    7 | 수가, 병원도입, subgroup risk, 책임소재            |
| `DIGITAL_HEALTHCARE_REMOTE_MEDICINE` |      17 |         17 |          7 |         12 |        10 |       1 |    6 | 규제, 수가, unit economics                   |
| `TELEHEALTH_BEHAVIORAL_HEALTH`       |      16 |         14 |          5 |         11 |         8 |       0 |    6 | CAC, privacy, impairment, churn          |
| `PHARMA_CHANNEL_AND_PRIVACY_RISK`    |    gate |       gate |       gate |       gate |      gate |    gate | gate | FDA/FTC, 조제약 품질, 개인정보                    |
| `MEDICAL_DEVICE_HEALTHCARE_EXPORT`   |      20 |         22 |         13 |         14 |        12 |       0 |    5 | 허가, 안전성, 경쟁, 채널 품질                       |
| `MEDICAL_DEVICE_DENTAL_IMPLANT`      |      20 |         22 |         13 |         14 |        12 |       0 |    5 | VBP, 가격통제, ASP 하락                        |
| `BOTULINUM_AESTHETIC_REGULATED`      |      19 |         20 |         12 |         13 |        11 |       0 |    5 | 위조품, 허가, safety, 유통채널                    |
| `DIAGNOSTICS_INFECTIOUS_DISEASE`     |      20 |          5 |          5 |          5 |         5 |       0 |    5 | one-off demand, 정상화                      |
| `ANIMAL_HEALTH_BIOSECURITY`          |      16 |         14 |          8 |         10 |         8 |       0 |    5 | 질병 이벤트 정상화, 정부 구매 종료                     |

Loop 2의 핵심 보정은 이거다.

```text
1. CDMO와 의료기기는 Green 가능 유지.
   계약·capacity·가동률·반복시술·OPM으로 검증 가능하기 때문.

2. CRO 점수는 소폭 하향.
   Charles River 사례처럼 biotech funding crunch가 수요를 바로 깎기 때문.

3. GLP-1은 EPS/FCF 점수는 유지하지만 4B/4C 감점축 강화.
   Novo 가격/경쟁 압박과 Hims channel risk가 확인됐기 때문.

4. Gene therapy는 더 보수적으로 하향.
   Bluebird가 승인 후 상업화 실패의 기준 반례를 제공했기 때문.

5. 의료AI는 Info 점수는 높지만 Stage 3 조건 강화.
   논문 성능보다 병원도입·수가·반복매출이 중요하다.

6. PHARMA_CHANNEL_AND_PRIVACY_RISK는 일반 점수가 아니라 gate로 승격.
   compounded drug, FDA, privacy, 광고 리스크가 thesis를 직접 깨기 때문.
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
가격경쟁 심화, PBM incentive 부족, 처방전환 지연, 마진 붕괴
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

## R7 Loop 2 공통 검증 방식

```text
1. 각 case의 stage1_date, stage2_date, stage3_date를 지정한다.
2. 해당 날짜의 종가를 stage_price로 저장한다.
3. MFE_30D / 90D / 180D / 1Y / 2Y를 계산한다.
4. MAE_30D / 90D / 180D / 1Y를 계산한다.
5. peak_price와 drawdown_after_peak를 계산한다.
6. 처방량, 매출, backlog, 가동률, 수가, 보험, 환급, cash runway, OPM과 가격경로를 비교한다.
```

## Loop 2에서 새로 강제할 판정

```text
COMMERCIALIZATION_ALIGNED:
허가·계약 이후 실제 처방·매출·OPM·주가가 동행.

APPROVAL_WITHOUT_UPTAKE:
허가는 받았지만 처방·환급·매출이 약함.

CAPACITY_WITHOUT_UTILIZATION:
CDMO/의료기기 capacity는 있으나 가동률·계약 미확인.

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
```

## 이번 R7 Loop 2에서 우선 검증할 가격 case

| case_id                                     | stage2 후보일 | 현재 1차 가격판정                                      |
| ------------------------------------------- | ---------: | ----------------------------------------------- |
| `samsung_biologics_gsk_us_facility_case`    | 2025-12-22 | -0.4%, strategic CDMO but price delayed         |
| `samsung_biologics_cdmo_capacity_reference` |     계약/시설별 | CDMO structural reference                       |
| `straumann_dental_implant_vbp_case`         | 2026-02-18 | 장중 +6%, medical device aligned                  |
| `lilly_foundayo_fda_approval_case`          | 2026-04-01 | Lilly +6%, GLP-1 oral Stage 2                   |
| `lilly_foundayo_prescription_uptake_case`   | 2026-05-08 | 7,335 scripts, modest uptake                    |
| `lilly_foundayo_switch_maintenance_case`    | 2026-05-12 | maintenance therapy candidate                   |
| `novo_glp1_price_pressure_case`             | 2026-02-04 | -16%, $50B wipeout, 4C-watch                    |
| `hims_branded_glp1_pivot_loss_case`         | 2026-05-12 | -11%, pharma channel risk                       |
| `hims_novo_partnership_case`                | 2026-03-09 | +40%+, channel event premium                    |
| `hims_compounded_glp1_crackdown_case`       | 2026-02-07 | compounded drug regulatory 4C-watch             |
| `bluebird_gene_therapy_cash_crunch_case`    | 2025-02-21 | -36%, hard 4C                                   |
| `charles_river_cro_funding_crunch_case`     | 2024-08-07 | -15%, CRO funding 4C-watch                      |
| `teladoc_betterhelp_impairment_case`        | 2024-08-01 | -13%, record low                                |
| `recursion_exscientia_ai_drug_case`         | 2024-08-08 | AI drug platform Watch                          |
| `lunit_dbt_subgroup_validation_case`        | 2025-03-17 | clinical validation, commercialization unproven |
| `botox_counterfeit_fda_warning_case`        |    2025-11 | safety/regulatory 4C-watch                      |

---

# 11. 다음에 에이전트가 채워야 할 price fields

R7 Loop 2에서는 아래 필드를 채우게 해야 한다.

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

prescription_volume
weekly_scripts
script_growth_rate
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

clinical_trial_phase
milestone_payment
big_pharma_partner
pipeline_count
ai_platform_flag
approved_drug_count

hospital_adoption_count
reimbursement_code_flag
recurring_revenue_ratio
ai_model_auc
subgroup_performance_risk
external_validation_flag
liability_risk_flag

device_export_country_count
procedure_volume
consumable_revenue_ratio
asp_change
vbp_price_control_flag
counterfeit_safety_flag
fda_warning_flag
licensed_channel_flag

cac
churn
privacy_incident_flag
impairment_charge
forecast_withdrawal_flag
advertising_cost_change

score_price_alignment
price_validation_status
review_notes
```

---

# R7 Loop 2 결론

이번 2회차에서 R7은 더 선명해졌다.

```text
강한 Green 후보:
CDMO 중 장기계약·capacity utilization·고객사 다변화가 확인된 기업
의료기기 수출 중 반복시술·소모품·OPM이 확인된 기업
치아·임플란트 중 가격통제 리스크를 통과한 기업
일부 GLP-1 상업화 기업 중 처방량·가격·보험·OP/EPS가 따라오는 기업

Watch-to-Green:
CRO
바이오시밀러
의료AI
원격의료
보톡스·미용시술
수술용 로봇
동물백신

Watch/Red:
AI 신약개발
유전자치료제
희귀질환 pre-revenue biotech
마이크로바이옴
줄기세포·면역세포 치료제
전염병 진단 one-off
DTC telehealth

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
```

**R7 Loop 2 점수정규화의 핵심 문장:**

> 바이오·헬스케어·의료기기는 “허가”, “임상”, “AI”, “논문”, “시장규모”가 아니라 **계약, 가동률, 처방량, PBM/보험, 수가, 반복시술, 소모품, 환급, cash runway, FCF 전환, 가격경로 리레이팅**으로 봐야 한다.
> 허가를 받아도 상업화가 안 되면 4C이고, 논문 성능이 좋아도 병원도입·수가·반복매출이 없으면 Stage 3-Green은 금지다.

다음에 같은 지시가 오면 순서대로 **R8 — 플랫폼·콘텐츠·SW·보안 Loop 2**로 넘어간다.

[1]: https://www.reuters.com/business/healthcare-pharmaceuticals/samsung-biologics-buy-us-drug-production-facility-gsk-280-mln-2025-12-21/?utm_source=chatgpt.com "Samsung Biologics to buy US drug production facility from GSK for $280 million"
[2]: https://en.wikipedia.org/wiki/Samsung_Biologics?utm_source=chatgpt.com "Samsung Biologics"
[3]: https://www.reuters.com/business/healthcare-pharmaceuticals/straumann-beats-earnings-expectations-2026-02-18/?utm_source=chatgpt.com "Straumann forecasts 2026 growth despite China procurement uncertainty, shares rise"
[4]: https://www.reuters.com/business/healthcare-pharmaceuticals/lillys-weight-loss-pill-wins-us-approval-2026-04-01/?utm_source=chatgpt.com "Lilly's weight-loss pill wins US approval, sets up next battle with rival Novo Nordisk"
[5]: https://www.reuters.com/legal/litigation/lillys-obesity-pill-tops-7000-prescriptions-fourth-week-signals-modest-uptake-2026-05-08/?utm_source=chatgpt.com "Lilly's obesity pill tops 7,000 prescriptions in fourth week, signals modest uptake"
[6]: https://www.reuters.com/legal/litigation/patients-dont-regain-much-weight-switching-injections-lillys-weight-loss-pill-2026-05-12/?utm_source=chatgpt.com "Patients don't regain much weight switching from injections to Lilly's weight-loss pill, study finds"
[7]: https://arxiv.org/abs/2503.13581?utm_source=chatgpt.com "Subgroup Performance of a Commercial Digital Breast Tomosynthesis Model for Breast Cancer Detection"
[8]: https://www.reuters.com/business/healthcare-pharmaceuticals/boehringer-goodrx-partner-offer-humira-rival-92-discount-2024-07-18/?utm_source=chatgpt.com "Boehringer-GoodRx partner to offer Humira rival at 92% discount"
[9]: https://www.reuters.com/business/healthcare-pharmaceuticals/novo-nordisk-plunge-wipes-50-billion-off-obesity-drug-giant-2026-02-04/?utm_source=chatgpt.com "Novo Nordisk plunge wipes $50 billion off obesity drug giant"
[10]: https://www.reuters.com/legal/litigation/hims-hers-plunges-after-weight-loss-pivot-hits-quarterly-results-2026-05-12/?utm_source=chatgpt.com "Hims & Hers plunges as branded weight-loss drug pivot hits results"
[11]: https://www.reuters.com/legal/litigation/novo-nordisk-strikes-deal-hims-sell-wegovy-ozempic-drops-lawsuit-2026-03-09/?utm_source=chatgpt.com "Novo Nordisk strikes deal for Hims to sell Wegovy and Ozempic, drops lawsuit"
[12]: https://www.reuters.com/legal/litigation/novo-nordisk-take-legal-action-against-hims-hers-wegovy-compounding-2026-02-05/?utm_source=chatgpt.com "Novo Nordisk to take legal action against Hims & Hers for Wegovy compounding"
[13]: https://www.reuters.com/markets/deals/bluebird-bio-be-taken-private-by-carlyle-sk-capital-amid-cash-crunch-2025-02-21/?utm_source=chatgpt.com "Gene therapy maker bluebird to go private in discounted deal amid cash crunch"
[14]: https://www.reuters.com/business/healthcare-pharmaceuticals/charles-river-cuts-2024-forecast-funding-crunch-among-biotech-clients-persists-2024-08-07/?utm_source=chatgpt.com "Charles River cuts 2024 forecast as funding crunch among biotech clients persists"
[15]: https://www.reuters.com/business/healthcare-pharmaceuticals/teladoc-shares-hit-record-low-after-telehealth-firm-withdraws-2024-forecast-2024-08-01/?utm_source=chatgpt.com "Teladoc shares hit record low after telehealth firm withdraws 2024 forecast"
[16]: https://www.reuters.com/markets/deals/biotech-firm-recursion-buy-smaller-peer-exscientia-688-million-2024-08-08/?utm_source=chatgpt.com "Biotech firm Recursion to buy smaller peer Exscientia for $688 million"
[17]: https://apnews.com/article/67afcdc72e100204181c20aacec39d89?utm_source=chatgpt.com "FDA warns websites selling unapproved Botox for cosmetic purposes"

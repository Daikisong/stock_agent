좋아. 정해둔 순서대로 이번은 **R7 — 바이오·헬스케어·의료기기**로 넘어간다.

R7은 특히 조심해야 해. 같은 바이오라도 **CDMO/의료기기처럼 실제 매출·계약·가동률·반복시술이 있는 축**과, **AI 신약개발·유전자치료제·임상 테마처럼 뉴스는 강하지만 상업화가 멀거나 cash burn이 큰 축**이 완전히 다르다. 업로드된 Theme Tag Map에서도 바이오는 세 갈래로 나눠야 한다고 정리되어 있다. 즉, pre-revenue biotech은 Green 거의 금지, royalty/commercialization biotech은 매출화·로열티 필요, CDMO/medical device는 장기계약·반복매출이면 Green 가능이다.

서생원식으로 보면 R7의 핵심도 같다. “허가받았다”, “임상 성공했다”, “AI 신약개발이다”가 아니라, **EPS/FCF 체급 변화와 밸류에이션 프레임 변화가 실제로 동시에 일어나는가**를 봐야 한다. 서생원식 초과수익 공식은 EPS 상향 × 밸류에이션 리레이팅 × 집중 보유이고, EPS만 있거나 멀티플만 있으면 부족하다.

---

# R7. 바이오·헬스케어·의료기기

## 1. 이번 라운드 대섹터

```text
R7 = 바이오·헬스케어·의료기기
```

R7의 기본 구조는 이렇게 세 갈래다.

```text
1. 생산·서비스·의료기기형
CDMO / CRO / 의료기기 / 미용기기 / 임플란트 / 보톡스
→ 계약, capacity, 가동률, 반복시술, 소모품, 수출
→ EPS/FCF 확인 가능

2. 상업화 바이오형
바이오시밀러 / GLP-1 / 오리지널 특허방어 / 일부 로열티
→ 허가보다 실제 처방·보험·PBM·마진·매출화가 핵심

3. pre-revenue / 플랫폼 / 이벤트형
AI 신약개발 / 유전자치료제 / 희귀질환 / 진단키트 / 의료AI PoC / 원격의료 테마
→ 뉴스는 강하지만 Green은 제한
```

R7에서 가장 위험한 오판은 이거다.

```text
허가 뉴스 = 매출화
임상 성공 = EPS 체급 변화
AI 신약개발 = 구조적 Green
진단 수요 = 반복 FCF
```

이런 식으로 등호를 놓으면 바로 false-positive가 나온다.

---

## 2. 대상 canonical archetype

| 구분                 | canonical archetype                  | Green 정책        |
| ------------------ | ------------------------------------ | --------------- |
| CDMO·CMO·원료의약품     | `CDMO_HEALTHCARE_CONTRACT`           | Green 가능        |
| CRO·임상서비스          | `CRO_CLINICAL_SERVICE`               | Watch-to-Green  |
| 바이오시밀러 상업화         | `BIOSIMILAR_COMMERCIALIZATION`       | Watch-to-Green  |
| 오리지널 제약사 특허방어      | `BIOSIMILAR_ORIGINATOR_DEFENSE`      | Watch           |
| GLP-1·비만치료제        | `OBESITY_GLP1_COMMERCIALIZATION`     | Green 가능, 경쟁 감시 |
| 희귀질환·유전자치료제        | `GENE_THERAPY_RARE_DISEASE`          | Watch/Red       |
| AI 신약개발            | `AI_DRUG_DISCOVERY_PLATFORM`         | Watch/Red       |
| 의료AI               | `DIGITAL_HEALTHCARE_AI`              | Watch-to-Green  |
| 원격의료·디지털헬스         | `DIGITAL_HEALTHCARE_REMOTE_MEDICINE` | Watch           |
| 온라인 정신건강·DTC 헬스    | `TELEHEALTH_BEHAVIORAL_HEALTH`       | Watch/Red       |
| 약물 유통·조제약·개인정보 리스크 | `PHARMA_CHANNEL_AND_PRIVACY_RISK`    | RedTeam overlay |
| 의료기기 수출            | `MEDICAL_DEVICE_HEALTHCARE_EXPORT`   | Green 가능        |
| 치아·임플란트            | `MEDICAL_DEVICE_DENTAL_IMPLANT`      | Green 가능        |
| 보톡스·미용시술           | `BOTULINUM_AESTHETIC_REGULATED`      | Watch-to-Green  |
| 전염병 진단             | `DIAGNOSTICS_INFECTIOUS_DISEASE`     | Red/Watch       |
| 동물백신·방역            | `ANIMAL_HEALTH_BIOSECURITY`          | Watch           |

---

## 3. deep sub-archetype

```text
CDMO_HEALTHCARE_CONTRACT
- CMO
- CDMO
- 원료의약품
- 항체 생산
- ADC 생산
- 미국 생산거점
- 장기 생산계약
- 가동률
- 고객사 다변화

CRO_CLINICAL_SERVICE
- 임상시험수탁
- 임상 데이터 서비스
- 고객사 R&D 예산
- backlog
- 바이오 funding cycle

BIOSIMILAR_COMMERCIALIZATION
- Humira biosimilar
- Stelara biosimilar
- Prolia biosimilar
- PBM 등재
- 보험 커버리지
- 처방 전환
- 가격경쟁

OBESITY_GLP1_COMMERCIALIZATION
- GLP-1
- Wegovy
- Zepbound
- oral GLP-1
- compounded GLP-1
- 보험 커버리지
- 처방량
- 공급능력

GENE_THERAPY_RARE_DISEASE
- 유전자치료제
- 희귀질환
- 고가 치료제
- 환자 모집
- 보험·환급
- cash burn
- manufacturing

AI_DRUG_DISCOVERY_PLATFORM
- AI 신약개발
- 후보물질
- milestone
- 임상 진입
- cash runway
- big pharma partnership

DIGITAL_HEALTHCARE_AI
- 의료영상 AI
- mammography AI
- 병원 workflow
- 수가/보험
- 외부 임상검증
- subgroup performance

DIGITAL_HEALTHCARE_REMOTE_MEDICINE
- 원격의료
- 디지털헬스 플랫폼
- 병원·보험 연동
- wearable
- EMR integration
- B2B/B2B2C 계약

MEDICAL_DEVICE_HEALTHCARE_EXPORT
- 미용기기
- 보톡스
- 임플란트
- 수술용 로봇
- 반복시술
- 소모품
- 해외 허가·채널

DIAGNOSTICS_INFECTIOUS_DISEASE
- 코로나 진단
- 엠폭스 진단
- 전염병 진단키트
- one-off demand
```

---

# 4. 성공사례

## 4-1. Samsung Biologics 미국 생산거점 — `CDMO_HEALTHCARE_CONTRACT`

Samsung Biologics는 GSK로부터 미국 Rockville 생산시설을 2억 8천만 달러에 인수해 첫 미국 생산거점을 확보하기로 했다. 해당 시설은 60,000L drug substance capacity를 갖고 있고, Samsung Biologics는 추가 투자로 capacity와 기술을 업그레이드하겠다고 밝혔다. 다만 발표 당일 Samsung Biologics 주가는 0.4% 하락했고, 코스피는 2% 상승해 가격경로는 즉시 aligned라고 보기 어렵다. ([Reuters][1])

**가격경로 1차 판정**

```text
판정:
strategic_success_candidate / price_alignment = delayed_or_uncertain

좋은 점:
미국 생산거점
60,000L capacity
장기 미국 수요 대응
관세·미국 내 생산 리스크 완화

주의:
발표 직후 주가는 시장 대비 부진.
즉, 전략은 좋아도 당장 EPS/FCF로 연결되는지 검증 필요.
```

**점수 교정**

```text
EPS/FCF: 중간~강함
Structural Visibility: 강함
Bottleneck/Pricing: 중간
Market Mispricing: 중간
Valuation Rerating: 중간
Risk: 인수 후 가동률, 추가 CAPEX, 고객계약, 미국 인건비·운영비
```

---

## 4-2. Samsung Biologics 계약 제조 누적 reference — `CDMO_HEALTHCARE_CONTRACT`

Samsung Biologics는 Pfizer, GSK, Lilly, AstraZeneca 등 대형 제약사와 생산계약을 맺어온 글로벌 CDMO로 정리된다. 특히 2023년 Pfizer와 수천억 원 규모 계약들이 있었고, 2024년 이후 ADC·미국 생산거점 확장까지 이어지면서 “임상 바이오”가 아니라 **계약·capacity·가동률로 점수화 가능한 생산형 바이오**에 가깝다. ([위키백과][2])

**가격경로 1차 판정**

```text
판정:
structural_reference_case

의미:
CDMO는 R7 안에서 Green 가능성이 가장 높은 축.
다만 계약 announcement가 아니라 backlog, 가동률, OP margin, FCF를 확인해야 한다.
```

---

## 4-3. Straumann / 치아·임플란트 — `MEDICAL_DEVICE_DENTAL_IMPLANT`

Straumann은 2025년 매출이 26.1억 스위스프랑으로 시장 예상치를 상회했고, 2026년 high single-digit sales growth를 제시했다. 중국 VBP, 즉 volume-based procurement 제도 불확실성이 남아 있지만, 유럽·북미·아시아태평양 실적이 견조했고, 발표 당일 주가는 장초반 최대 6% 상승 후 1.6% 상승 수준을 유지했다. ([Reuters][3])

**가격경로 1차 판정**

```text
가격 반응:
장중 최대 +6%, 이후 +1.6%

판정:
medical_device_aligned_candidate

의미:
치아·임플란트는 수요·해외채널·OPM이 있으면 Green 가능.
다만 중국 VBP 가격통제는 hard risk.
```

**점수 교정**

```text
EPS/FCF: 강함
Structural Visibility: 강함
Bottleneck/Pricing: 중간
Market Mispricing: 중간
Risk: VBP 가격통제, 허가, ASP 하락, 경쟁 심화
```

---

## 4-4. 보톡스·미용시술 — `BOTULINUM_AESTHETIC_REGULATED`

보툴리눔 톡신·미용시술은 반복 수요가 있어 `MEDICAL_DEVICE_HEALTHCARE_EXPORT`와 겹치는 Green 후보가 될 수 있다. 하지만 FDA가 18개 웹사이트에 counterfeit 또는 unapproved Botox류 제품 판매 경고를 보냈고, 상해 사례와 독성 부작용 보고가 있었다는 AP 보도는 이 archetype의 규제·안전성 리스크를 분명히 보여준다. ([AP News][4])

**가격경로 1차 판정**

```text
판정:
watch_to_green_with_safety_gate

의미:
허가된 제품 + 반복 시술 + 안전한 채널은 후보.
위조품, 무허가 유통, 안전성 이슈는 4C.
```

---

## 4-5. 의료AI / Lunit mammography AI — `DIGITAL_HEALTHCARE_AI`

Lunit INSIGHT DBT 모델의 대규모 외부평가 연구는 163,449건 screening mammography exams에서 전체 AUC 0.91을 기록했지만, non-invasive cancer, calcifications, dense breast tissue 같은 subgroup에서 성능이 낮아질 수 있음을 보였다. 이건 의료AI가 기술적으로 유망하다는 Stage 1~2 근거이면서, 동시에 “전체 성능이 좋다 = 바로 Green”이 아니라는 반례이기도 하다. ([arXiv][5])

**가격경로 1차 판정**

```text
판정:
clinical_validation_candidate / commercialization_unproven

의미:
의료AI는 외부검증이 있으면 점수 상승.
하지만 수가, 병원 도입, 반복 매출, 책임소재가 없으면 Stage 3-Green 금지.
```

---

## 4-6. GLP-1 / Lilly oral obesity pill — `OBESITY_GLP1_COMMERCIALIZATION`

Lilly의 oral GLP-1 비만치료제 Foundayo는 출시 4주차에 미국에서 7,335건 처방을 기록했지만, Q2 컨센서스 매출 1.6억 달러를 맞추려면 주당 약 22,000건 처방이 필요하다는 분석이 나왔다. 별도 후기 임상에서는 기존 주사 GLP-1 사용자가 Foundayo로 전환해도 체중 재증가가 제한적이라는 결과가 나와, oral GLP-1은 장기 시장 후보이지만 초기 uptake와 매출 기대 간극을 확인해야 한다. ([Reuters][6])

**가격경로 1차 판정**

```text
판정:
high_growth_watch_to_green

좋은 점:
대형 시장
oral 제형
장기 유지요법 가능성

주의:
초기 처방량은 기대보다 modest
매출 컨센서스 충족 여부 확인 필요
경쟁·보험·가격·telehealth 채널 리스크
```

---

# 5. 반례

## 5-1. Novo Nordisk / GLP-1 competition — `OBESITY_GLP1_COMMERCIALIZATION`

Novo Nordisk는 Wegovy 판매 둔화, Lilly Zepbound 경쟁, compounded alternatives 확산으로 2025년 전망을 낮췄다. 2026년에는 미국 가격 하락 전망으로 주가가 16% 급락해 약 500억 달러의 시가총액이 사라졌다는 Reuters 보도도 나왔다. 이건 GLP-1 시장이 커도 **경쟁, 가격, 보험, compounded drug, 처방 성장 둔화**가 valuation을 무너뜨릴 수 있음을 보여준다. ([Reuters][7])

**교훈**

```text
GLP-1 시장 크기
≠ 무조건 Green

Green 조건:
처방량 증가
보험 커버리지
공급능력
가격 방어
경쟁 우위
OP/EPS 상향

4C 조건:
가격 하락
compounded 대체
경쟁사 점유율 확대
처방 성장 둔화
```

---

## 5-2. Hims & Hers GLP-1 pivot — `PHARMA_CHANNEL_AND_PRIVACY_RISK`

Hims & Hers는 compounded GLP-1에서 Novo Nordisk Wegovy 같은 branded drug로 전략을 전환하는 과정에서 매출 기대를 밑돌고 예상 밖 손실을 냈으며, 주가는 시간외에서 12% 넘게 하락했다. 월간 가입자당 매출도 85달러에서 80달러로 낮아졌다. 이건 온라인 헬스·약물 플랫폼에서 **전략 전환, 조제약 규제, unit economics, 마진 훼손**이 얼마나 큰 리스크인지 보여준다. ([Reuters][8])

**교훈**

```text
온라인 약물 플랫폼
≠ Green

반드시 볼 것:
합법적 처방 채널
마진
CAC
가입자당 매출
regulatory scrutiny
FCF
```

---

## 5-3. Bluebird bio / gene therapy commercialization failure — `GENE_THERAPY_RARE_DISEASE`

bluebird bio는 승인된 유전자치료제들을 보유했지만 severe cash crunch로 Carlyle과 SK Capital에 비상장화되기로 했고, 처음 제안은 주당 3달러로 전일 종가 대비 57.4% 할인된 가격이었다. 발표 후 주가는 36% 하락했고, 2018년에는 약 150달러에 거래됐던 주식이 크게 무너졌다. Reuters는 gene therapy uptake가 느리고 초기 사용도 중증 환자 중심이었다고 보도했다. ([Reuters][9])

**가격경로 1차 판정**

```text
가격 반응:
발표 후 -36%
2018년 약 $150 → deal price $3~$5 수준

판정:
hard_counterexample / commercialization_failure

의미:
승인된 유전자치료제도 상업화·환급·현금 runway가 없으면 Green이 아니다.
```

---

## 5-4. Bluebird revised offer bounce — event premium

Carlyle과 SK Capital이 upfront offer를 주당 5달러로 높인 뒤 bluebird 주가는 50% 넘게 급등해 4.97달러가 되었다. 하지만 이건 구조적 리레이팅이 아니라 인수조건 조정에 따른 event premium이다. ([Reuters][10])

**교훈**

```text
M&A bounce
≠ structural success

분류:
event_premium
cash_crunch_resolution_attempt
not_E2R_success
```

---

## 5-5. Charles River / CRO funding crunch — `CRO_CLINICAL_SERVICE`

Charles River는 바이오 고객사의 funding crunch가 지속되며 2024년 전망을 낮췄고, premarket에서 주가가 15% 하락했다. 매출도 2.5~4.5% 감소할 것으로 예상했다. CRO는 실제 서비스 매출이 있는 점에서 pre-revenue biotech보다 강하지만, 바이오 funding cycle이 꺾이면 4C로 갈 수 있다. ([Reuters][11])

**가격경로 1차 판정**

```text
가격 반응:
premarket -15%

판정:
CRO_funding_cycle_4c

의미:
CRO는 backlog와 고객 다변화가 있어야 Watch-to-Green.
바이오 funding cycle이 약하면 Green 금지.
```

---

## 5-6. Teladoc / BetterHelp — `TELEHEALTH_BEHAVIORAL_HEALTH`

Teladoc은 BetterHelp 관련 7.9억 달러 impairment를 기록하고 연간·장기 전망을 철회했으며, 주가는 13% 하락해 사상 최저치를 기록했다. BetterHelp의 광고비 증가와 매출 둔화가 핵심 리스크로 지적됐다. ([Reuters][12])

**가격경로 1차 판정**

```text
가격 반응:
-13%, record low
2024년 약 -60%

판정:
telehealth_DTC_failure_4c

의미:
원격의료·온라인 정신건강은 사용자 수가 아니라 CAC, 반복계약, privacy, FCF가 핵심.
```

---

## 5-7. AI drug discovery platform — `AI_DRUG_DISCOVERY_PLATFORM`

Recursion은 Exscientia를 6.88억 달러 all-stock deal로 인수해 AI 신약개발 역량과 파이프라인을 강화하려 했다. 합병 후 약 8.5억 달러 현금을 보유해 3년 운영을 지원할 수 있다는 점은 긍정적이지만, AI 신약개발은 실제 승인·매출까지 거리가 길다. AI 신약개발에 대한 학술 리뷰도 AI가 여러 후보물질을 임상으로 올렸지만, drug discovery의 핵심은 약동학·약력학·임상 결과 최적화이며 충분한 ground truth와 인간 검증 없이는 한계가 있다고 지적한다. ([Reuters][13])

**교훈**

```text
AI 플랫폼
≠ Green

점수 강화:
대형 제약사 milestone
임상 진입
cash runway
후보물질 다변화

감점:
승인 약물 없음
임상 실패
cash burn
platform hype
```

---

# 6. 4B-watch 사례

## 6-1. GLP-1 obesity market 4B-watch

```text
4B 조건:
- GLP-1 시장 규모 narrative 과밀
- Lilly/Novo 목표가 상향 과열
- 실제 처방량보다 valuation이 먼저 감
- compounded alternatives와 가격경쟁이 무시됨
- 보험 커버리지 불확실성을 시장이 과소평가
```

Novo Nordisk의 주가 급락과 전망 하향은, 시장이 GLP-1 성장성을 과대평가했을 때 4B에서 4C로 전환될 수 있음을 보여준다. ([Reuters][14])

---

## 6-2. 의료기기 / 임플란트 4B-watch

Straumann은 좋은 성공 후보지만, 중국 VBP 같은 가격통제가 있는 영역에서는 valuation이 먼저 오르면 4B-watch가 필요하다. 주가는 실적·가이던스에 반응했지만, 중국 가격통제의 다음 round가 아직 불확실하다. ([Reuters][3])

```text
4B 조건:
- 임플란트·미용기기 목표가 과밀
- 중국 VBP 리스크 과소평가
- ASP 하락보다 수요 증가만 반영
```

---

## 6-3. CDMO capacity premium 4B-watch

CDMO는 Green 가능성이 있지만, capacity 확장만으로 valuation이 먼저 올라가면 4B-watch다. Samsung Biologics의 GSK 시설 인수도 전략적으로는 좋지만, 발표 당일 주가가 시장을 이기지 못했다는 점은 시장이 “전략적 capacity”와 “단기 EPS”를 분리해 봤다는 신호다. ([Reuters][1])

---

## 6-4. AI 의료·AI 신약개발 4B-watch

```text
4B 조건:
- AI 의료/AI 신약개발 이름만으로 관련주 급등
- 논문·PoC만 있고 매출 없음
- 병원 도입·수가·보험 없음
- 임상 success probability를 시장이 과대평가
```

Lunit DBT 연구처럼 외부검증은 중요하지만, subgroup 성능과 병원 도입·수가·반복매출을 확인하기 전까지 Green은 제한해야 한다. ([arXiv][5])

---

# 7. 4C-thesis-break 사례

## 7-1. Bluebird gene therapy cash crunch

```text
4C:
cash crunch
slow uptake
commercialization failure
dilutive/discounted take-private
going-concern risk
```

bluebird bio는 승인 제품이 있어도 상업화와 현금흐름이 없으면 어떻게 무너지는지 보여주는 대표 4C다. ([Reuters][9])

---

## 7-2. CRO funding crunch

```text
4C:
biotech funding crunch
customer R&D budget cut
backlog slowdown
revenue decline
forecast cut
```

Charles River의 -15% premarket 반응은 CRO도 바이오 funding cycle에서 자유롭지 않다는 기준이다. ([Reuters][11])

---

## 7-3. Telehealth CAC / impairment

```text
4C:
DTC 광고비 급증
BetterHelp impairment
전망 철회
record low stock
privacy risk
```

Teladoc은 “원격의료 수요”가 있다고 해서 지속 가능한 비즈니스가 되는 것은 아니라는 대표 반례다. ([Reuters][12])

---

## 7-4. Botox counterfeit / safety risk

```text
4C-watch:
counterfeit product
unapproved product
FDA warning
injury reports
licensed channel failure
```

FDA의 counterfeit Botox 경고는 미용의료·보톡스 관련주에서 제품안전·유통채널·허가 리스크를 hard gate로 둬야 한다는 근거다. ([AP News][4])

---

## 7-5. GLP-1 price / compounded alternative pressure

```text
4C-watch:
price cut
compounded alternative
보험 커버리지 부족
처방 성장 둔화
경쟁사 점유율 확대
```

Novo Nordisk의 전망 하향과 2026년 주가 급락은 GLP-1도 “시장 크기”만으로 Green을 줄 수 없다는 반례다. ([Reuters][7])

---

# 8. 점수비중 보정표 — R7 v1.0

| canonical archetype                  | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | 핵심 감점                                            |
| ------------------------------------ | ------: | ---------: | ---------: | ---------: | --------: | ------: | ---: | ------------------------------------------------ |
| `CDMO_HEALTHCARE_CONTRACT`           |      20 |         24 |         12 |         12 |        12 |       0 |    5 | 가동률, 고객집중, CAPEX, tariff                         |
| `CRO_CLINICAL_SERVICE`               |      18 |         20 |          8 |         12 |        12 |       0 |    5 | biotech funding, 고객 예산, backlog quality          |
| `BIOSIMILAR_COMMERCIALIZATION`       |      18 |         20 |          6 |         13 |        11 |       0 |    6 | 가격경쟁, PBM, 처방전환 지연                               |
| `BIOSIMILAR_ORIGINATOR_DEFENSE`      |      19 |         18 |          8 |         13 |        11 |       2 |    6 | patent cliff, pipeline failure, pricing pressure |
| `OBESITY_GLP1_COMMERCIALIZATION`     |      22 |         20 |         12 |         13 |        12 |       0 |    6 | 경쟁, 보험, 조제약, 가격규제                                |
| `GENE_THERAPY_RARE_DISEASE`          |       8 |         12 |          8 |         10 |         6 |       0 |    5 | cash burn, 환급, 상업화 지연                            |
| `AI_DRUG_DISCOVERY_PLATFORM`         |       6 |         10 |          7 |         12 |         6 |       0 |    5 | 승인약 부재, 임상실패, platform hype                      |
| `DIGITAL_HEALTHCARE_AI`              |      18 |         17 |          8 |         13 |        12 |       0 |    7 | 수가, 병원도입, subgroup bias, 책임소재                    |
| `DIGITAL_HEALTHCARE_REMOTE_MEDICINE` |      18 |         18 |          8 |         13 |        12 |       1 |    6 | 규제, 수가, unit economics                           |
| `TELEHEALTH_BEHAVIORAL_HEALTH`       |      17 |         16 |          6 |         12 |        10 |       0 |    6 | CAC, privacy, impairment, churn                  |
| `PHARMA_CHANNEL_AND_PRIVACY_RISK`    |      16 |         15 |          6 |         12 |        10 |       0 |    6 | FDA/FTC, 조제약 품질, 개인정보                            |
| `MEDICAL_DEVICE_HEALTHCARE_EXPORT`   |      20 |         22 |         13 |         14 |        12 |       0 |    5 | 허가, 안전성, 경쟁, 채널 품질                               |
| `MEDICAL_DEVICE_DENTAL_IMPLANT`      |      20 |         22 |         13 |         14 |        12 |       0 |    5 | VBP, 가격통제, ASP 하락                                |
| `BOTULINUM_AESTHETIC_REGULATED`      |      19 |         20 |         12 |         13 |        11 |       0 |    5 | 위조품, 허가, safety, 유통채널                            |
| `DIAGNOSTICS_INFECTIOUS_DISEASE`     |      20 |          5 |          5 |          5 |         5 |       0 |    5 | one-off demand, 정상화                              |
| `ANIMAL_HEALTH_BIOSECURITY`          |      16 |         14 |          8 |         10 |         8 |       0 |    5 | 질병 이벤트 정상화, 정책 불확실                               |

---

# 9. stage date 후보

## `CDMO_HEALTHCARE_CONTRACT`

```text
Stage 1:
대형 CDMO 계약, capacity 증설, 미국/유럽 생산거점 뉴스

Stage 2:
장기계약, 가동률, 고객사 다변화, OP/EPS 상향 확인

Stage 3:
다년 생산 visibility + FCF conversion + valuation frame 전환

Stage 4B:
CDMO capacity premium 과열, 인수·CAPEX 기대 과밀

Stage 4C:
가동률 하락, 계약 지연, CAPEX 부담, tariff, 고객사 주문 취소
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
FDA/EMA 허가, 특허만료, 출시 뉴스

Stage 2:
PBM/보험 등재, 처방전환, 실제 매출 확인

Stage 3:
처방량 증가 + 마진 방어 + 다국가 출시 확인

Stage 4B:
허가 뉴스만으로 biosimilar 관련주 과열

Stage 4C:
가격경쟁 심화, 처방전환 지연, 마진 붕괴
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
비만치료제 시장 규모 narrative 과열

Stage 4C:
compounded 대체, 가격인하, 경쟁사 점유율 확대, 규제/광고 제재
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

## R7 공통 검증 방식

```text
1. 각 case의 stage1_date, stage2_date, stage3_date를 지정한다.
2. 해당 날짜의 종가를 stage_price로 저장한다.
3. MFE_30D / 90D / 180D / 1Y / 2Y를 계산한다.
4. MAE_30D / 90D / 180D / 1Y를 계산한다.
5. peak_price와 drawdown_after_peak를 계산한다.
6. 처방량, 매출, backlog, 가동률, 수가, 보험, 환급, cash runway, OPM과 가격 경로를 비교한다.
```

## R7에서 반드시 분리할 판정

```text
aligned:
계약·매출·가동률·처방량·OPM과 주가 리레이팅이 같이 감.

approval_without_commercialization:
허가는 받았지만 처방·환급·매출이 없음.

clinical_or_ai_hype:
임상/AI 성능 뉴스로 주가만 상승.

commercialization_failure:
상업화 지연, cash burn, going concern, take-private.

recurring_revenue_success:
CDMO/의료기기/디지털헬스가 반복 매출과 FCF를 보여줌.

one_off_diagnostic:
전염병 진단처럼 EPS는 컸지만 지속성 없음.
```

## 이번 R7에서 우선 검증할 가격 case

| case_id                                      |              stage2 후보일 | 현재 1차 가격판정                                    |
| -------------------------------------------- | ----------------------: | --------------------------------------------- |
| `samsung_biologics_gsk_us_facility_case`     |              2025-12-22 | 주가 -0.4%, strategic success but delayed price |
| `samsung_biologics_cdmo_contract_reference`  |                 계약별 공시일 | CDMO structural reference                     |
| `straumann_dental_implant_growth_case`       |              2026-02-18 | 장중 +6%, medical device aligned                |
| `botox_counterfeit_fda_warning_case`         |              2025-11-05 | safety/regulatory 4C-watch                    |
| `lunit_mammography_ai_subgroup_case`         |              2025-03-17 | clinical validation + subgroup risk           |
| `lilly_oral_glp1_foundayo_case`              |              2026-05-08 | modest uptake, Watch-to-Green                 |
| `novo_wegovy_outlook_cut_case`               | 2025-05-07 / 2026-02-04 | 2026 -16%, GLP-1 4C-watch                     |
| `hims_glp1_strategy_shift_case`              |              2026-05-11 | -12% extended, channel/regulatory risk        |
| `bluebird_gene_therapy_cash_crunch_case`     |              2025-02-21 | -36%, hard 4C                                 |
| `bluebird_revised_offer_event_premium_case`  |              2025-05-14 | +50%, event premium                           |
| `charles_river_cro_funding_crunch_case`      |              2024-08-07 | -15%, CRO funding 4C                          |
| `teladoc_betterhelp_impairment_case`         |              2024-08-01 | -13%, record low                              |
| `recursion_exscientia_ai_drug_platform_case` |              2024-08-08 | AI drug platform, price backfill 필요           |

---

# 11. 다음에 에이전트가 채워야 할 price fields

R7 case library에는 아래 필드가 필요하다.

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

contract_value
contract_duration
capacity_liters
capacity_utilization
backlog_growth
customer_concentration
op_margin_change
fcf_margin

prescription_volume
weekly_scripts
insurance_coverage
pbm_listing_flag
biosimilar_discount_pct
drug_price_change
compounded_alternative_flag

clinical_trial_phase
approval_status
patient_uptake
reimbursement_status
cash_runway_months
going_concern_flag
dilution_or_take_private_flag

hospital_adoption_count
reimbursement_code_flag
recurring_revenue_ratio
ai_model_auc
subgroup_performance_risk
liability_risk_flag

device_export_country_count
procedure_volume
consumable_revenue_ratio
vbp_price_control_flag
counterfeit_safety_flag

cac
churn
privacy_incident_flag
impairment_charge
forecast_withdrawal_flag

score_price_alignment
price_validation_status
```

---

# R7 결론

R7은 “바이오라서 위험하다”가 아니라, **바이오 안에서도 점수화 가능한 사업모델과 점수화하면 안 되는 뉴스형 테마를 철저히 분리하는 라운드**다.

```text
Green 가능:
CDMO
의료기기 수출
치아·임플란트
일부 GLP-1 상업화
일부 보톡스·미용시술
실제 반복매출이 있는 디지털헬스

Watch-to-Green:
CRO
바이오시밀러
의료AI
원격의료
동물백신
수술용 로봇

Watch/Red:
AI 신약개발
유전자치료제
희귀질환 pre-revenue biotech
진단키트 one-off
전염병 이벤트
마이크로바이옴
줄기세포·면역세포 치료제
```

**R7 점수정규화의 핵심 문장:**

> 바이오·헬스케어·의료기기는 “허가·임상·AI·논문”이 아니라 **계약, 가동률, 처방량, 보험·수가, 반복시술, 소모품, 환급, cash runway, FCF 전환**으로 봐야 한다.
> 허가를 받았어도 상업화가 안 되면 4C이고, 논문 성능이 좋아도 병원 도입·수가·매출이 없으면 Stage 3-Green은 금지다.

다음에 네가 “다음 라운드 진행해줘”라고 하면, 정해둔 순서에 따라 **R8 — 플랫폼·콘텐츠·SW·보안**으로 넘어간다.

[1]: https://www.reuters.com/business/healthcare-pharmaceuticals/samsung-biologics-buy-us-drug-production-facility-gsk-280-mln-2025-12-21/?utm_source=chatgpt.com "Samsung Biologics to buy US drug production facility from GSK for $280 million"
[2]: https://en.wikipedia.org/wiki/Samsung_Biologics?utm_source=chatgpt.com "Samsung Biologics"
[3]: https://www.reuters.com/business/healthcare-pharmaceuticals/straumann-beats-earnings-expectations-2026-02-18/?utm_source=chatgpt.com "Straumann forecasts 2026 growth despite China procurement uncertainty, shares rise"
[4]: https://apnews.com/article/67afcdc72e100204181c20aacec39d89?utm_source=chatgpt.com "FDA warns websites selling unapproved Botox for cosmetic purposes"
[5]: https://arxiv.org/abs/2503.13581?utm_source=chatgpt.com "Subgroup Performance of a Commercial Digital Breast Tomosynthesis Model for Breast Cancer Detection"
[6]: https://www.reuters.com/legal/litigation/lillys-obesity-pill-tops-7000-prescriptions-fourth-week-signals-modest-uptake-2026-05-08/?utm_source=chatgpt.com "Lilly's obesity pill tops 7,000 prescriptions in fourth week, signals modest uptake"
[7]: https://www.reuters.com/business/healthcare-pharmaceuticals/obesity-drugmaker-novo-nordisk-cuts-2025-outlook-posts-q1-profit-above-forecast-2025-05-07/?utm_source=chatgpt.com "Novo Nordisk cuts 2025 outlook as Wegovy obesity drug sales slow"
[8]: https://www.reuters.com/legal/litigation/hims-hers-raises-2026-revenue-forecast-2026-05-11/?utm_source=chatgpt.com "Hims & Hers misses revenue estimates as strategy shift hits sales"
[9]: https://www.reuters.com/markets/deals/bluebird-bio-be-taken-private-by-carlyle-sk-capital-amid-cash-crunch-2025-02-21/?utm_source=chatgpt.com "Gene therapy maker bluebird to go private in discounted deal amid cash crunch"
[10]: https://www.reuters.com/business/healthcare-pharmaceuticals/bluebird-bio-receives-higher-upfront-offer-pe-firms-carlyle-sk-capital-2025-05-14/?utm_source=chatgpt.com "Bluebird bio receives higher upfront offer from PE firms Carlyle, SK Capital"
[11]: https://www.reuters.com/business/healthcare-pharmaceuticals/charles-river-cuts-2024-forecast-funding-crunch-among-biotech-clients-persists-2024-08-07/?utm_source=chatgpt.com "Charles River cuts 2024 forecast as funding crunch among biotech clients persists"
[12]: https://www.reuters.com/business/healthcare-pharmaceuticals/teladoc-shares-hit-record-low-after-telehealth-firm-withdraws-2024-forecast-2024-08-01/?utm_source=chatgpt.com "Teladoc shares hit record low after telehealth firm withdraws 2024 forecast"
[13]: https://www.reuters.com/markets/deals/biotech-firm-recursion-buy-smaller-peer-exscientia-688-million-2024-08-08/?utm_source=chatgpt.com "Biotech firm Recursion to buy smaller peer Exscientia for $688 million"
[14]: https://www.reuters.com/business/healthcare-pharmaceuticals/novo-nordisk-plunge-wipes-50-billion-off-obesity-drug-giant-2026-02-04/?utm_source=chatgpt.com "Novo Nordisk plunge wipes $50 billion off obesity drug giant"

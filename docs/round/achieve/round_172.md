좋아. **R13 Loop 10까지 끝났으니, 이번은 R1 Loop 11 — 산업재·수주·인프라**다.

이번부터 조건을 더 빡세게 바꾼다.

```text
Loop 11 추가 조건:
1. 국장 종목 중심
2. 기존에 썼던 성공/반례 최대한 제외
3. 단순 stage 설명이 아니라,
   “주가 대폭 상승 전 Stage 3 포착 가능했는가?”
   “상승 릴레이 끝나기 전에 Stage 4B 또는 4C로 식힐 수 있는가?”
   를 점수표에 반영
```

기존에 많이 쓴 `GE Vernova`, `Siemens Energy`, `LS Electric`, `Hyundai Rotem`, `Hanwha Aerospace`, `Constellation`, `Oklo`는 이번 성공/반례의 중심에서 제외한다. 이번 R1 Loop 11의 국장 중심 후보는 **HD현대일렉트릭, 효성중공업, 두산에너빌리티/한전기술/한전KPS, HD현대중공업·HD현대미포, HD현대마린솔루션, 한국항공우주, LIG넥스원, 한화오션**으로 잡는다.

R1은 전력설비, 전선·케이블, 피팅밸브, 조선, 방산, 원전, 철도, 건설기계, 우크라 재건, 네옴시티를 흡수한다. 이 대섹터는 성공 사례가 많이 나올 수 있지만, **수주 뉴스만으로는 부족하고 계약질 + 마진 + EPS 상향 + 주가 리레이팅이 같이 가야 한다**는 원칙을 유지한다.

서생원식으로 보면 R1은 “수주가 많다”가 아니라 **산업 성격이 바뀌면서 EPS/FCF가 폭발적으로 올라가고, 시장이 아직 과거 프레임으로 낮은 밸류를 주는가**가 핵심이다. 특히 변압기·조선·방산·원전은 표면 업종은 달라도 “과거 시클리컬/저평가 → 공급부족·수주잔고 증가 → 장기계약·가격전가 → EPS 체급 상승 → 리레이팅” 구조가 같아야 통과한다.

---

# R1 Loop 11. 산업재·수주·인프라 — 국장 중심

## 1. 이번 라운드 대섹터

```text
R1 = 산업재·수주·인프라

Loop 11 목표 =
국장 전력장비 / 변압기 / 조선 / 원전 / 방산 / 항공우주 후보를

Stage 2 뉴스 후보
→ Stage 3 실적·가격경로 후보
→ Stage 4B 과열 후보
→ Stage 4C 논리 훼손 후보

로 다시 분리
```

이번 R1 Loop 11의 핵심 질문은 이거다.

```text
이 종목이 “이후 실제 주가가 크게 오른 종목”이었다면,
우리 점수표는 그 전에 Stage 3로 잡았어야 한다.

반대로 이미 상승 릴레이가 과열되었거나
계약·마진·실적·정책 리스크가 꺾였으면,
Stage 4B 또는 Stage 4C로 빨리 낮춰야 한다.
```

R1 Loop 11의 stage 정의를 더 강하게 바꾼다.

```text
Stage 1:
AI 전력수요, 미국 전력망 부족, 조선 재건, 원전 수출,
방산 재무장, 항공기 수출, 정부정책 뉴스

Stage 2:
계약금액, 고객명, 납품기간, 수주잔고, 인수합병,
정부 preferred bidder, LOI, MoA, 항공기 계약 확인

Stage 3:
OP/EPS/FCF 상향 + 수주잔고 질 개선 + 마진 개선 +
주가가 이미 반응하기 시작했지만 아직 4B 과열 전

Stage 4B:
논리는 맞지만 이미 모두가 인정한 구간.
주가 급등, 신고가, 밸류 과밀, 리포트·뉴스 과밀.
여기서는 신규 진입 기대수익률을 낮춤.

Stage 4C:
계약 취소, 정부/경쟁당국 제동, 소송·제재,
대규모 증자, 저마진 수주, 원가 급등,
주가만 오른 event premium
```

---

## 2. 대상 canonical archetype

| canonical archetype                          | 국장 대상                     | Loop 11 판정 방향            |
| -------------------------------------------- | ------------------------- | ------------------------ |
| `GRID_TRANSFORMER_SHORTAGE_KOREA`            | HD현대일렉트릭, 효성중공업, 일진전기     | Stage 3 후보, 4B 감시        |
| `GRID_US_LOCALIZATION_CAPA`                  | 효성중공업/HICO, HD현대일렉트릭 미국법인 | Stage 2~3 후보             |
| `POWER_EQUIPMENT_BACKLOG_TO_FCF_KOREA`       | HD현대일렉트릭, 효성중공업           | Stage 3 후보               |
| `SHIPBUILDING_US_PLATFORM_RESTRUCTURING`     | HD현대중공업, HD현대미포           | Stage 2 후보, event/4B 감시  |
| `SHIP_MRO_RECURRING_PLATFORM`                | HD현대마린솔루션                 | Stage 2~3 후보, IPO 4B 감시  |
| `NUCLEAR_EXPORT_PREFERRED_BIDDER`            | 두산에너빌리티, 한전기술, 한전KPS      | Stage 2 후보, 계약체결 전 cap   |
| `DEFENSE_AIRCRAFT_EXPORT_BACKLOG`            | 한국항공우주                    | Stage 2 후보               |
| `DEFENSE_INTERCEPTOR_COMBAT_VALIDATION`      | LIG넥스원                    | Stage 2.5 후보, 계약 전 4B 감시 |
| `GEOPOLITICAL_SHIPBUILDING_SANCTION_OVERLAY` | 한화오션                      | hard RedTeam             |
| `MOU_LOI_NOT_CONTRACT`                       | 조선·원전·방산 공통               | Stage 3 금지               |
| `DISCLOSURE_CONFIDENCE_CAP`                  | 전 종목                      | 계약금액·기간·마진 없으면 cap       |

---

## 3. deep sub-archetype

```text
GRID_TRANSFORMER_SHORTAGE_KOREA
- HD현대일렉트릭
- 효성중공업
- 일진전기
- 초고압 변압기
- GSU transformer
- substation transformer
- AI data center
- 미국 전력망
- lead time 3~4년
- 가격 상승
- CAPA 증설
- 미국 현지생산
- 수주잔고
- OPM
- FCF

GRID_US_LOCALIZATION_CAPA
- Hyosung HICO
- Memphis transformer plant
- Alabama transformer facility
- 미국 전력설비 부족
- 현지 생산능력
- tariff / Buy America / utility customer
- long lead time
- capacity reservation

SHIPBUILDING_US_PLATFORM_RESTRUCTURING
- HD현대중공업
- HD현대미포
- MASGA
- 미국 조선 재건
- Arctic icebreaker
- naval defense
- merchant ship capacity
- merger
- share exchange ratio
- record high price reaction
- integration risk

SHIP_MRO_RECURRING_PLATFORM
- HD현대마린솔루션
- 선박 MRO
- retrofit
- 친환경 개조
- 부품·서비스
- IPO premium
- recurring service
- KKR overhang

NUCLEAR_EXPORT_PREFERRED_BIDDER
- 두산에너빌리티
- 한전기술
- 한전KPS
- KHNP
- Czech Dukovany
- preferred bidder
- contract signing
- EDF / Westinghouse appeals
- legal injunction
- reactor equipment
- EPC engineering
- maintenance service
- price path rally

DEFENSE_AIRCRAFT_EXPORT_BACKLOG
- 한국항공우주
- FA-50
- Philippines
- 12 aircraft
- 975.3bn won
- delivery by 2030
- fighter modernization
- prior delivery record

DEFENSE_INTERCEPTOR_COMBAT_VALIDATION
- LIG넥스원
- Cheongung-II / M-SAM II
- Patriot alternative
- Middle East demand
- combat validation
- missile defense
- unit cost advantage
- production scalability
- actual order required

GEOPOLITICAL_SHIPBUILDING_SANCTION_OVERLAY
- 한화오션
- Philly Shipyard
- U.S. Navy MRO
- China sanctions
- Section 301
- U.S.-China maritime tension
- shares decline
- geopolitical retaliation
```

---

## 4. 성공사례 / Stage 3 후보

### 4-1. HD현대일렉트릭 — 국장 R1에서 가장 정석적인 전력장비 Stage 3 후보

HD현대일렉트릭은 이번 국장 R1 Loop 11의 핵심 후보다. 미국 전력망은 데이터센터, 전기차, 공장, 재생에너지, 노후 전력망 교체 때문에 변압기 부족이 심해졌고, Wood Mackenzie 기준 미국 GSU transformer 수요는 2019~2025년 274%, substation transformer 수요는 116% 증가했다. 대형 변압기 lead time은 최대 4년까지 늘었고, 가격은 5년간 약 80% 올랐다. 이건 단순 테마가 아니라 **수요 증가 + 공급 병목 + 가격결정력**이 같이 있는 구조다. ([Reuters][1])

HD현대일렉트릭은 power transformer 제조사이고, 미국 power transformer subsidiary가 2026년 3월 Alabama 제2공장 착공에 들어간 것으로 정리된다. 이 회사는 미국과 사우디 초고압 변압기 시장에서 높은 점유율을 가진 기업으로 언급되고, AI 전력 인프라 수요에서 한국 전력장비 대표주로 분류된다. ([위키백과][2])

```text
case_type:
GRID_TRANSFORMER_SHORTAGE_KOREA
+
POWER_EQUIPMENT_BACKLOG_TO_FCF_KOREA
+
STRUCTURAL_SUCCESS_ALIGNED_CANDIDATE
+
4B_WATCH
```

**stage 포착**

```text
Stage 1:
미국 변압기 부족, AI data center 전력수요, lead time 장기화

Stage 2:
미국 CAPA 증설, 초고압 변압기 수출 visibility, 장기 수요 확인

Stage 3 후보:
OP/EPS/FCF 상향 + 수주잔고 질 개선 + OPM 유지가 확인되면 Stage 3

Stage 4B:
이미 시장에서 “K-변압기”가 consensus가 된 구간이면 신규 진입 기대수익률 감점
```

**가격경로 검증**

```text
정성 가격경로:
이미 K-전력장비 대표주로 시장이 강하게 재평가한 구간.

정량 price field:
agent가 반드시 KRX daily bars로
stage2_date, stage3_date, price_at_stage2, price_at_stage3,
60D/120D/252D return, MFE/MAE를 backfill해야 함.
```

**점수 보정**

```text
상향:
Bottleneck / Visibility / EPS-FCF 가중치

감점:
Valuation room / 4B risk

핵심:
HD현대일렉트릭은 Stage 3로 포착해야 하는 후보였지만,
현재는 Stage 3 후보 + 4B 감시를 동시에 붙여야 한다.
```

---

### 4-2. 효성중공업 — 미국 현지 생산·765kV·HVDC가 붙은 Stage 2→3 후보

효성중공업은 HD현대일렉트릭과 같은 전력장비 축이지만, 포인트가 조금 다르다. Hyosung HICO는 미국 Memphis에 transformer plant를 갖고 있고, Reuters는 미국 전력설비 부족 대응을 위해 Hyosung HICO가 1.57억 달러 규모의 transformer plant 확장 투자를 한다고 보도했다. 같은 보도는 미국 변압기 부족이 데이터센터, 전기차, 재생에너지, 노후 전력망 교체 수요에서 나온 구조적 병목이라고 설명한다. ([Reuters][3])

효성중공업은 초고압 변압기, 차단기, 전력시스템을 만드는 기업이고, 2024년 매출 4.3조 원, 영업이익 2,578억 원을 기록한 것으로 정리된다. 또한 2024년 200MW HVDC transformer 개발을 완료했고, 창원 HVDC transformer plant는 2027년 완공 예정으로 언급된다. ([위키백과][4])

```text
case_type:
GRID_US_LOCALIZATION_CAPA
+
GRID_TRANSFORMER_SHORTAGE_KOREA
+
HVDC_GRID_OPTION
```

**stage 포착**

```text
Stage 1:
미국 전력망 병목, 변압기 lead time, AI 전력수요

Stage 2:
미국 현지 생산 확장, HVDC 기술·CAPA, 765kV/초고압 exposure

Stage 3:
수주잔고가 OP/EPS/FCF로 전환되고,
미국 HICO 가동률과 margin이 확인될 때

Stage 4B:
전력장비 basket 전체가 과밀해지고,
목표가·리포트·테마가 한 방향으로 몰릴 때
```

**가격경로 검증**

```text
효성중공업은 Stage 2 evidence가 강하다.
그러나 “실제 주가 급등 전 Stage 3 포착” 검증에는
KRX OHLCV + 분기별 OP revision backfill이 필요하다.

이번 점수표에서는:
Stage 2.5 후보
→ OP/EPS revision 확인 시 Stage 3
→ 252D 급등 + valuation 과밀 시 Stage 4B
```

**점수 보정**

```text
HD현대일렉트릭보다 disclosure detail이 약하면 confidence cap.
하지만 미국 현지생산·HVDC option은 visibility 가점.
```

---

### 4-3. 두산에너빌리티 / 한전기술 / 한전KPS — 체코 원전 preferred bidder rally는 Stage 2, 계약 전 Stage 3 금지

두산에너빌리티·한전기술·한전KPS는 원전 수출 테마에서 국장 R1의 핵심 후보군이다. Reuters는 체코 정부가 KHNP를 신규 원전 2기 preferred bidder로 선정했고, 당시 두산에너빌리티 주가가 3개월간 48%, 한전KPS가 14%, 한전기술이 41% 상승했다고 보도했다. 이건 정책·수출 기대가 실제 가격경로를 만든 사례다. ([Reuters][5])

다만 이 케이스는 Stage 3가 아니다. 이후 EDF와 Westinghouse의 항소로 계약 체결이 일시적으로 막힌 적이 있고, 체코 경쟁당국이 항소를 기각하면서 2025년 4월에는 4000억 체코코루나, 약 182억 달러 규모 계약 체결이 가능해졌다는 보도가 나왔다. 즉 `preferred bidder`는 Stage 2이고, **최종 계약·두산/한전기술/한전KPS의 실제 공급범위·마진·매출 인식**이 확인돼야 Stage 3다. ([Reuters][6])

```text
case_type:
NUCLEAR_EXPORT_PREFERRED_BIDDER
+
EVENT_TO_CONTRACT_ESCALATION
+
CONTRACT_SIGNING_GATE
```

**stage 포착**

```text
Stage 1:
원전 수출 기대, Team Korea nuclear narrative

Stage 2:
KHNP preferred bidder, 체코 원전 수주 기대, 관련주 price-path rally

Stage 3:
최종 계약 체결
+ 두산에너빌리티 기자재 scope
+ 한전기술 engineering scope
+ 한전KPS maintenance/service scope
+ OP/EPS revision

Stage 4B:
preferred bidder만으로 이미 3개월 40~50% 이상 급등한 구간

Stage 4C:
계약 지연, 항소, Westinghouse IP 문제, 정치 교체, financing failure
```

**가격경로 판정**

```text
점수표가 Stage 1→2 price rally를 잡아야 한다.
그러나 Stage 3-Green은 계약 전 금지해야 한다.

이 케이스는 “주가가 크게 올랐으니 Stage 3”가 아니라,
“Stage 2 event-to-contract 후보가 price rally를 만든 것”이다.
```

**점수 보정**

```text
원전 preferred bidder:
Visibility +15

최종 계약 미체결:
Disclosure confidence cap -10

관련주 3개월 급등:
4B valuation room -8

실제 공급범위 확인:
Stage 3 승격 조건
```

---

### 4-4. HD현대중공업·HD현대미포 — 미국 조선 재건 narrative가 merger price-path를 만든 사례

HD현대중공업과 HD현대미포 합병은 R1 조선 쪽의 국장 신규 사례다. Reuters는 HD현대중공업이 미국 조선 수요를 잡기 위해 계열사 HD현대미포와 합병을 추진한다고 보도했고, 이 발표 후 HD현대중공업 주가는 11.3%, HD현대미포는 14.6% 상승해 record high로 마감했다. 이 흐름은 미국의 “Make American Shipbuilding Great Again” 협력, Arctic icebreaker, naval defense demand와 연결됐다. ([Reuters][7])

```text
case_type:
SHIPBUILDING_US_PLATFORM_RESTRUCTURING
+
EVENT_TO_STRUCTURAL_STAGE2
+
4B_WATCH
```

**stage 포착**

```text
Stage 1:
미국 조선 재건, MASGA, 방산·icebreaker 수요

Stage 2:
HD현대중공업-현대미포 merger, share exchange, 구조재편

Stage 3:
합병 후 실제 미국 조선/MRO/방산 계약
+ yard CAPA 활용
+ margin 개선
+ FCF 확인 필요

Stage 4B:
합병 발표만으로 record high와 10%대 급등이 나왔으면
신규 진입은 event premium 과열 감시
```

**가격경로 판정**

```text
점수표가 Stage 2 event-to-structural candidate로 잡아야 한다.
하지만 merger announcement만으로 Stage 3-Green은 금지.
```

**점수 보정**

```text
M&A/합병 구조재편:
Visibility +10

실제 선박·MRO 계약 부재:
Stage 3 cap

발표 당일 10%대 급등:
4B watch 즉시 부착
```

---

### 4-5. HD현대마린솔루션 — 선박 MRO recurring platform 후보지만 IPO 4B 감시

HD현대마린솔루션은 조선 본체보다 선박 lifecycle service, MRO, retrofit, 부품·서비스 반복매출에 가까운 구조라서 R1에서 별도 archetype으로 봐야 한다. WSJ는 HD현대마린솔루션이 2024년 한국 최대 IPO로 5.4억 달러를 조달했고, 상장 첫날 주가가 공모가 83,400원 대비 97% 오른 163,900원에 마감했다고 보도했다. 2023년 매출은 1.43조 원으로 7.2% 증가했고, 영업·순이익도 크게 증가했다고 정리된다. ([월스트리트저널][8])

```text
case_type:
SHIP_MRO_RECURRING_PLATFORM
+
IPO_EVENT_PREMIUM
+
4B_WATCH
```

**stage 포착**

```text
Stage 1:
선박 MRO·retrofit·친환경 개조 recurring platform narrative

Stage 2:
IPO, 2023 실적 증가, 서비스형 사업모델 visibility

Stage 3:
상장 후 반복 MRO 매출·OPM·FCF·고객다변화 확인 필요

Stage 4B:
상장 첫날 +97%는 명백한 IPO premium / 4B watch
```

**가격경로 판정**

```text
주가가 크게 올랐다고 Stage 3로 잡으면 오판이다.
이 케이스는 “좋은 사업모델 가능성 + IPO event premium”으로 분리해야 한다.
```

**점수 보정**

```text
Recurring MRO:
Business quality +12

IPO 첫날 +97%:
Valuation room -15

상장 후 quarterly FCF/OPM 확인 전:
Stage 3 금지
```

---

### 4-6. 한국항공우주 — FA-50 필리핀 계약은 Stage 2, 반복수출·마진 확인 전 Stage 3 제한

한국항공우주는 `DEFENSE_AIRCRAFT_EXPORT_BACKLOG`의 국장 신규 후보로 볼 수 있다. Reuters는 KAI가 필리핀 국방부와 약 9,753억 원, 7.13억 달러 규모 계약을 맺고 2030년까지 FA-50 12대를 공급하기로 했다고 보도했다. 이는 필리핀 군 현대화 수요와 연결되고, KAI가 2014년 계약으로 이미 12대를 2017년까지 인도한 이력도 있다. ([Reuters][9])

```text
case_type:
DEFENSE_AIRCRAFT_EXPORT_BACKLOG_STAGE2

stage 포착:
Stage 1 = K방산 항공기 수출 기대
Stage 2 = 필리핀 FA-50 12대, 975.3bn won, 2030년까지 납품
Stage 3 = 납품스케줄, 마진, 후속계약, OP/EPS revision 필요
```

**가격경로 판정**

```text
계약 visibility는 강하다.
하지만 항공기는 납품기간이 길고 개발·보증·정비 비용이 있어
계약금액만으로 Stage 3를 주면 안 된다.
```

**점수 보정**

```text
고객명·금액·납품기한:
Visibility +18

장기 납품·마진 불확실:
EPS/FCF cap

후속국가/반복수출 확인:
Stage 3 승격 조건
```

---

## 5. 반례 / 4B·4C 사례

### 5-1. LIG넥스원 — 전투검증·전쟁 이벤트로 47% 급등했지만, 계약 전 Stage 3는 조심

LIG넥스원은 이번 Loop 11에서 매우 중요한 케이스다. FT는 이란전쟁 이후 LIG넥스원의 Cheongung-II, 즉 M-SAM II가 저가 Patriot 대안으로 주목받으면서 주가가 전쟁 시작 이후 약 47% 상승했다고 보도했다. 해당 보도는 Cheongung-II가 Patriot PAC-3보다 단가가 낮고, 생산 확장 속도가 빠르며, 중동·유럽의 관심이 커졌다고 설명했다. ([Financial Times][10])

```text
case_type:
DEFENSE_INTERCEPTOR_COMBAT_VALIDATION
+
EVENT_PRICE_RALLY
+
STAGE2_5_NOT_FULL_STAGE3
```

**stage 포착**

```text
Stage 1:
미사일 방어 수요, 중동 전쟁, 방공체계 관심

Stage 2:
전투검증 narrative, 가격경로 +47%, 수요 관심 증가

Stage 3:
신규 수출계약, 계약금액, 납품일정, OP/EPS 상향 확인 필요

Stage 4B:
계약보다 주가가 먼저 40~50% 상승한 경우 즉시 4B watch

Stage 4C:
전쟁 이벤트 종료, 수출계약 지연, 경쟁체계 가격인하, 생산 bottleneck
```

**가격경로 판정**

```text
우리 점수표가 LIG넥스원을 Stage 1에만 묶어뒀다면 급등을 놓친다.
그래서 “combat validation + price-path + 수요관심”은 Stage 2.5로 올린다.

하지만 계약금액·납품·EPS revision 전에는 Stage 3-Green 금지.
```

**점수 보정**

```text
기존:
계약 전 defense event는 Stage 1~2

Loop 11 보정:
combat_validation_price_path가 있으면 Stage 2.5까지 허용

단:
actual_export_contract 없으면 Stage 3 cap
```

---

### 5-2. 한화오션 — 미국 조선/MRO narrative가 있어도 중국 제재가 붙으면 hard 4C

한화오션은 미국 조선 재건 narrative의 수혜 후보처럼 보일 수 있지만, 지정학 RedTeam이 바로 붙을 수 있음을 보여준다. AP는 중국이 미국의 중국 조선업 조사에 대한 보복으로 한화오션의 미국 소재 자회사 5곳을 제재했고, 제재 대상에는 Hanwha Shipping LLC, Hanwha Philly Shipyard Inc. 등이 포함됐다고 보도했다. 한화오션은 2024년 말 Philly Shipyard를 1억 달러에 인수했고, 미국 조선 인프라에 50억 달러 투자를 약속했으며, 미 해군 MRO 계약도 확보했지만, 제재 이후 서울에서 주가가 급락했다. ([AP News][11])

```text
case_type:
GEOPOLITICAL_SHIPBUILDING_SANCTION_OVERLAY
+
SHIPBUILDING_US_PLATFORM_4C_WATCH
```

**stage 포착**

```text
Stage 1:
미국 조선 재건, Philly Shipyard, 미 해군 MRO

Stage 2:
미국 자산 인수, MRO 계약, 미국 투자 pledge

Stage 4C:
중국 제재, 미중 조선 갈등, 주가 급락, 지정학 리스크
```

**가격경로 판정**

```text
한화오션은 “미국 조선 재건 수혜”만 보면 Stage 2 후보지만,
중국 제재가 붙으면 Stage 3-Green은 차단해야 한다.
```

**점수 보정**

```text
US shipbuilding exposure:
Visibility +10

China sanctions / retaliation:
RedTeam -20
Stage 3 hard cap
```

---

### 5-3. HD현대미포 $1.55B 수주설 — LOI·협의는 Stage 2도 약하다

HD현대미포는 2025년 4월 15.5억 달러 규모 수주 보도에 대해 계약 협의 중이라고 공시했다. Reuters는 HD현대미포와 HD현대삼호가 그리스 선주와 2027~2028년 인도 예정 20척 컨테이너선 LOI를 맺었다는 보도가 있었지만, 회사 공시는 협의 중이라고만 확인했고 세부 내용은 공개하지 않았다고 보도했다. ([Reuters][12])

```text
case_type:
MOU_LOI_NOT_CONTRACT
+
DISCLOSURE_CONFIDENCE_CAPPED

stage 포착:
Stage 1 = 대형 수주 보도
Stage 2 약함 = LOI/협의 확인
Stage 3 금지 = 계약금액·선주·마진·최종계약 미확정
```

**가격경로 판정**

```text
이런 케이스는 주가가 먼저 움직여도 Stage 3로 올리면 안 된다.
LOI와 본계약은 완전히 다르다.
```

**점수 보정**

```text
LOI:
Visibility +4

본계약 미확정:
Disclosure cap -12

계약금액·마진 미공개:
EPS/FCF 점수 제한
```

---

### 5-4. 두산에너빌리티 체코 원전 — preferred bidder는 가격을 만들지만, legal gate가 있었다

두산에너빌리티 계열 원전 후보군은 체코 preferred bidder 뉴스로 강하게 올랐지만, 이후 EDF·Westinghouse의 항소와 체코 경쟁당국의 절차가 있었다. Reuters는 2024년 10월 체코 반독점당국이 항소 심사 중 계약 체결을 일시적으로 금지했다고 보도했고, 이 프로젝트는 최대 180억 달러 규모의 국가 에너지 투자였다. ([Reuters][6])

```text
case_type:
NUCLEAR_EXPORT_LEGAL_GATE
+
PREFERRED_BIDDER_NOT_FINAL_CONTRACT

stage 포착:
Stage 2 = preferred bidder + 관련주 rally
Stage 4C-watch = 항소, 계약체결 금지, Westinghouse IP issue
Stage 3 조건 = 최종계약 + 공급범위 + OP/EPS 상향
```

**점수 보정**

```text
preferred_bidder:
Stage 2

legal_injunction:
Stage 3 금지

final_contract_signed:
Stage 3 후보 재검토
```

---

## 6. Stage 포착·주가상승/하락 반영을 위한 점수비중 정규화

이번 Loop 11부터 R1 점수표를 “급등 전 Stage 3 포착”과 “상승릴레이 말기 4B/4C 식힘”에 맞게 바꾼다.

```text
R1 Loop 11 기본 점수표 = 100점

1. EPS/FCF·OPM 전환 가능성              24점
2. 계약·수주잔고·고객 visibility          20점
3. 병목·가격결정력                       18점
4. 가격경로 조기검증                     12점
5. capital discipline / dilution          8점
6. disclosure confidence / RedTeam        8점
7. valuation room / 4B 여지               10점
```

기존보다 **가격경로 조기검증 12점**을 새로 올렸다. 이건 “이미 오른 종목을 나중에 좋다고 하는 점수표”를 막기 위한 장치다.

---

### 6-1. Stage 3 조기 포착 조건

```text
Stage 3 조기 포착 =
아래 6개 중 4개 이상 충족

1. OP/EPS 컨센서스 상향 또는 분기 OP beat
2. 수주잔고 증가 + 납품기간 장기화
3. margin이 저가수주 소진/가격전가로 개선
4. 주가가 stage2_date 이후 60D 안에 +20% 이상 MFE
5. 아직 PER/PBR이 peer 대비 과열 전
6. 계약 detail이 DART/detail disclosure로 확인됨
```

즉, **주가가 이미 조금 반응하기 시작한 초입**을 Stage 3로 잡는다. 너무 늦게 잡으면 서생원식이 아니다.

---

### 6-2. Stage 4B 조기 종료 조건

```text
Stage 4B 조기 전환 =
아래 5개 중 3개 이상 충족

1. Stage 2 이후 120D MFE +80% 이상
2. Stage 3 이후 252D MFE +150% 이상
3. 리포트/뉴스에서 같은 narrative가 과밀
4. valuation이 peer top-quartile 이상
5. EPS revision 속도보다 주가 상승속도가 빠름
```

이 조건은 특히 **HD현대일렉트릭, 효성중공업, LIG넥스원, HD현대마린솔루션** 같은 “좋은데 이미 많이 간 종목”에 필요하다.

---

### 6-3. Stage 4C 즉시 강등 조건

```text
Stage 4C 즉시 강등 =
하나만 떠도 hard gate

1. 계약 취소 / 계약 정정 / 수주 취소
2. 대규모 증자 / CB / BW / 희석
3. 감사·공시 문제
4. 정부·경쟁당국·법원 제동
5. 제재 / 수출통제 / 지정학 보복
6. 저마진 수주로 OP/EPS 하향
7. LOI/MOU가 본계약으로 전환 실패
```

한화오션 중국 제재, 두산에너빌리티 체코 원전 legal gate, HD현대미포 LOI-only는 이 규칙에 들어간다.

---

### 6-4. 이번 국장 R1 Loop 11 케이스별 점수 보정표

| 종목/케이스    |                 stage 판정 | 가격경로 판정                                  | 점수 보정                                 |
| --------- | -----------------------: | ---------------------------------------- | ------------------------------------- |
| HD현대일렉트릭  |    Stage 3 후보 + 4B watch | K-변압기 리레이팅 대표주, KRX backfill 필수          | EPS/FCF·병목 상향, valuation 감점           |
| 효성중공업     |           Stage 2.5~3 후보 | 미국 HICO·HVDC evidence, price backfill 필요 | 미국 현지 CAPA 가점, disclosure cap         |
| 두산에너빌리티   | Stage 2, 계약 전 Stage 3 금지 | 체코 preferred bidder로 3개월 +48%            | event-to-contract 가점, legal gate cap  |
| 한전기술      | Stage 2, 계약 전 Stage 3 금지 | 체코 원전 기대 3개월 +41%                        | engineering scope 확인 전 cap            |
| 한전KPS     | Stage 2, 계약 전 Stage 3 금지 | 체코 원전 기대 3개월 +14%                        | maintenance scope 확인 전 cap            |
| HD현대중공업   |       Stage 2 + 4B watch | 합병 발표 후 +11.3%, record high              | 구조재편 가점, event premium 감점             |
| HD현대미포    |       Stage 2 + 4B watch | 합병 발표 후 +14.6%, LOI-only 수주설 cap         | 본계약 전 Stage 3 금지                      |
| HD현대마린솔루션 |    Stage 2~3 후보 + IPO 4B | 상장 첫날 +97%                               | recurring MRO 가점, valuation 강한 감점     |
| 한국항공우주    |                  Stage 2 | 975.3bn won FA-50 필리핀 계약                 | 고객·금액 가점, 장기납품/margin cap             |
| LIG넥스원    |     Stage 2.5 + 4B watch | 전쟁 후 +47%                                | combat validation 가점, 계약 전 Stage 3 금지 |
| 한화오션      |    Stage 2 후보 → 4C watch | 중국 제재 후 주가 급락                            | 지정학 제재 hard RedTeam                   |

---

## 7. 다음에 에이전트가 반드시 채워야 할 price fields

이번 사용자 요구의 핵심은 “정말 오른 종목을 Stage 3로 잡았냐”다. 그래서 다음 필드는 선택이 아니라 필수다.

```text
price fields:

ticker
company_name
stage1_date
stage2_date
stage3_date
stage4b_date
stage4c_date

price_at_stage1
price_at_stage2
price_at_stage3
price_at_stage4b
price_at_stage4c

return_20d_after_stage2
return_60d_after_stage2
return_120d_after_stage2
return_252d_after_stage2

return_20d_after_stage3
return_60d_after_stage3
return_120d_after_stage3
return_252d_after_stage3

mfe_60d_after_stage2
mae_60d_after_stage2
mfe_120d_after_stage2
mae_120d_after_stage2
mfe_252d_after_stage2
mae_252d_after_stage2

volume_spike_flag
relative_strength_vs_kospi
relative_strength_vs_sector
valuation_at_stage3
valuation_at_stage4b
eps_revision_before_stage3
eps_revision_after_stage3
op_revision_before_stage3
op_revision_after_stage3
```

OpenDART list만으로는 부족하다. detail fetch에서는 공급계약, 신규시설투자, 잠정실적, 영업실적 전망, 유상증자, CB/BW, 감사의견, 거래정지, 계약 해지·취소·정정 같은 watch disclosure만 골라서 계약금액, 기간, 상대방, 시설투자금액, OP YoY, 희석유형을 뽑아야 한다. 빠진 값은 만들면 안 된다.

---

# R1 Loop 11 결론

이번 R1 Loop 11의 핵심은 이거다.

```text
국장 R1에서는 전력장비·원전·조선·방산 모두 좋아 보일 수 있다.
하지만 Stage 3-Green은 “수주 뉴스”가 아니라
OP/EPS/FCF와 가격경로가 같이 움직일 때만 준다.
```

```text
Stage 3로 조기 포착해야 할 후보:
HD현대일렉트릭
효성중공업
단, 이미 많이 오른 구간은 4B watch

Stage 2지만 아직 Green 금지:
두산에너빌리티 / 한전기술 / 한전KPS 체코 원전
한국항공우주 FA-50 필리핀
HD현대중공업·현대미포 합병
HD현대마린솔루션 IPO 이후 MRO platform

Stage 2.5 특수 후보:
LIG넥스원
전투검증 + price-path는 강하지만, 실제 수출계약 전 Stage 3 cap

4C 또는 hard watch:
한화오션 중국 제재
HD현대미포 LOI-only 수주설
두산에너빌리티 체코 원전 legal gate
HD현대마린솔루션 IPO premium 과열
```

**R1 Loop 11 점수정규화의 핵심 문장:**

> 산업재·수주·인프라는 “수주”, “전력망”, “원전”, “조선 재건”, “방산 수요”라는 이름이 아니라 **계약금액, 고객명, 납품기간, 수주잔고 질, OP/EPS/FCF 상향, margin, price-path MFE/MAE, valuation room, LOI/MOU 여부, legal gate, sanction risk**로 봐야 한다.
> 특히 이번 Loop 11부터는 우리 점수표가 **대폭 상승 전 Stage 3를 잡았는지**, 그리고 **상승 릴레이 말기 Stage 4B/4C로 식혔는지**를 의무 검증한다.

다음 순서는 **R2 — AI·반도체·전자부품 Loop 11**, 역시 **국장 중심 + 기존 사례 제외 + 실제 가격경로 검증 강화**로 간다.

[1]: https://www.reuters.com/business/energy/us-power-transformer-buyers-scramble-imports-factory-slots--reeii-2026-05-11/?utm_source=chatgpt.com "US power transformer buyers scramble for imports, factory slots"
[2]: https://en.wikipedia.org/wiki/HD_Hyundai_Electric?utm_source=chatgpt.com "HD Hyundai Electric"
[3]: https://www.reuters.com/business/energy/grid-equipment-makers-invest-us-ease-supply-shortage--reeii-2025-12-02/?utm_source=chatgpt.com "Grid equipment makers invest in US to ease supply shortage"
[4]: https://en.wikipedia.org/wiki/Hyosung_Heavy_Industries?utm_source=chatgpt.com "Hyosung Heavy Industries"
[5]: https://www.reuters.com/business/energy/south-koreas-winning-bid-czech-nuclear-power-project-2024-07-17/?utm_source=chatgpt.com "South Korea's winning bid for Czech nuclear power project"
[6]: https://www.reuters.com/business/energy/czech-watchdog-prohibits-nuclear-power-contract-signing-amid-appeals-2024-10-30/?utm_source=chatgpt.com "Czech watchdog prohibits nuclear power contract signing amid appeals"
[7]: https://www.reuters.com/markets/emerging/south-korean-shipbuilder-hd-hyundai-heavy-merge-with-affiliate-hd-hyundai-mipo-2025-08-27/?utm_source=chatgpt.com "South Korean shipbuilder HD Hyundai Heavy to merge with affiliate HD Hyundai Mipo"
[8]: https://www.wsj.com/business/hd-hyundai-marine-solution-makes-strong-debut-in-south-korea-e5e63451?utm_source=chatgpt.com "KKR-Backed HD Hyundai Marine Makes Strong Debut in South Korea"
[9]: https://www.reuters.com/en/south-koreas-kai-signs-700-mln-aircraft-deal-with-philippines-2025-06-04/?utm_source=chatgpt.com "South Korea's KAI signs $700 mln aircraft deal with Philippines"
[10]: https://www.ft.com/content/658c8411-df02-4b5e-a69d-2029114e4ca1?utm_source=chatgpt.com "Iran war lifts K-defence company offering cheap Patriot rival"
[11]: https://apnews.com/article/cb72348bb00cb95801c2d6b5a47702fa?utm_source=chatgpt.com "China sanctions 5 US units of South Korean shipbuilder Hanwha Ocean over probe by Washington"
[12]: https://www.reuters.com/business/autos-transportation/south-korean-shipbuilder-hd-hyundai-mipo-confirms-contract-talks-after-report-2025-04-08/?utm_source=chatgpt.com "South Korean shipbuilder HD Hyundai Mipo confirms contract talks after report of $1.55 billion order"

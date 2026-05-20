좋아. **R13 Loop 2까지 끝났으니, 규칙대로 다시 R1로 돌아와서 이번은 R1 Loop 3 — 산업재·수주·인프라**로 간다.

이번 Loop 3의 핵심은 1~2회차보다 더 좁혀서 보는 거다. R1은 전력설비, 전선·케이블, 조선, 조선 기자재, 방산, 원전, 철도, 건설기계, 우크라 재건, 네옴시티를 품는 대섹터이고, Theme Tag Map에서도 “성공 사례가 많이 나올 수 있지만 수주 뉴스만으로는 부족하고 계약질 + 마진 + EPS 상향 + 주가 리레이팅이 같이 가야 한다”고 정리돼 있다.

또 Checkpoint 20 원칙처럼 계약금액, 계약기간, 계약금액/매출, 거래상대방, 계약 시작·종료일, OP YoY, dilution 같은 필드는 실제 공시·리포트·기사에서 확인될 때만 써야 한다. R1은 특히 수주 숫자가 예뻐 보이기 쉬운 섹터라서, 없는 값을 추정으로 채우면 바로 Green 오판이 난다.

서생원식으로는 R1도 “수주가 많다”가 아니라 **산업 구조 변화 → EPS/FCF 체급 변화 → 시장의 과거 프레임 오해 → 밸류에이션 리레이팅**이 이어지는지를 보는 라운드다. 전력기기, 방산, 조선은 이 구조가 나올 수 있지만, 정책형 재건·네옴·SMR 테마는 실제 계약·마진·현금흐름 전까지 훨씬 보수적으로 봐야 한다.

---

# R1 Loop 3. 산업재·수주·인프라

## 1. 이번 라운드 대섹터

```text
R1 = 산업재·수주·인프라
Loop 3 목표 = 수주형 structural Green과 수주/정책/event premium을 더 강하게 분리
```

이번 회차의 질문은 하나다.

```text
이 수주는 EPS/FCF 체급을 바꾸는 수주인가?
아니면 뉴스성 수주, 저마진 수주, 정책 기대, CAPEX 부담, dilution, project delay인가?
```

R1에서 제일 위험한 오판은 이거다.

```text
수주잔고 증가
= 무조건 Green
```

실제로는 이렇게 봐야 한다.

```text
좋은 수주:
계약금액 큼
계약기간 김
납품 스케줄 명확
매출 대비 계약금액 큼
마진 개선 가능
수주잔고가 FY1/FY2/FY3 EPS로 전환
주가가 실적경로와 같이 리레이팅

나쁜 수주:
계약금액 불명확
마진 불명확
MOU/LOI 수준
financing 미확정
납기 지연 위험
CAPEX나 유상증자가 따라옴
정책 테마만 있고 실제 매출화 없음
```

---

## 2. 대상 canonical archetype

| canonical archetype                   | Loop 3 정책                                            |
| ------------------------------------- | ---------------------------------------------------- |
| `GRID_TRANSFORMER_SHORTAGE`           | R1 최상위 Green 후보. 리드타임·가격·계약·CAPA 확인                  |
| `AI_DATA_CENTER_POWER_EQUIPMENT`      | Green 가능. 데이터센터 orders/backlog와 project delay를 같이 확인 |
| `CONTRACT_BACKLOG_INDUSTRIAL`         | Green 가능. 계약질·마진·EPS 전환 필수                           |
| `DEFENSE_GOVERNMENT_BACKLOG`          | Green 가능. 다년계약·정부고객·납품스케줄 핵심                         |
| `DEFENSE_TECH_AUTONOMOUS_SYSTEMS`     | Watch-to-Green. 실제 조달·양산 전까지 제한                      |
| `DEFENSE_DRONE_COUNTER_UAS`           | Watch-to-Green. prototype/MOU는 Green 금지              |
| `DEFENSE_AI_SOFTWARE_INTELLIGENCE`    | Watch. 반복 SW 매출 전까지 보수적                              |
| `SHIPBUILDING_OFFSHORE_BACKLOG`       | Green 가능. 선가·저가수주 소진·후판가·인도마진 확인                     |
| `SHIPBUILDING_NAVAL_MRO`              | Watch-to-Green. MRO 경험은 좋지만 신조/고마진 전환 필요             |
| `RAIL_INFRASTRUCTURE`                 | Watch-to-Green. 대형계약은 좋지만 마진·financing 확인            |
| `NUCLEAR_EXISTING_PPA`                | Watch-to-Green. 기존 원전 PPA는 SMR보다 증거 강함               |
| `NUCLEAR_SMR_GRID_POLICY`             | Watch/Red. 비용초과·고객확보 실패·허가 리스크                       |
| `GEOPOLITICAL_RECONSTRUCTION`         | Event/Watch. 실제 수주 전 Green 금지                        |
| `SMART_FACTORY_AUTOMATION`            | Watch. PoC/MOU와 반복매출 분리                              |
| `PROJECT_DELAY_CAPEX_OVERLAY`         | RedTeam overlay. 데이터센터·원전·철도 지연                      |
| `CAPITAL_ALLOCATION_DILUTION_OVERLAY` | RedTeam overlay. 유상증자·CAPEX 부담·목적 불명확                |

---

## 3. deep sub-archetype

```text
GRID_TRANSFORMER_SHORTAGE
- 초고압 변압기
- GSU transformer
- substation transformer
- 배전반
- 전선·케이블
- transformer lead time
- transformer price increase
- factory slot pre-buying
- 한국·튀르키예 수입
- grid modernization

AI_DATA_CENTER_POWER_EQUIPMENT
- 데이터센터 전력장비
- switchgear
- UPS
- PDU
- modular power
- electrification equipment
- substation equipment
- high-voltage systems
- 데이터센터 quarterly orders
- backlog

DEFENSE_GOVERNMENT_BACKLOG
- K9
- K10
- K2
- 천무
- 탄약
- 엔진
- 현지생산
- NATO 재무장
- 수출허가
- 정부고객 다년계약

DEFENSE_TECH_AUTONOMOUS_SYSTEMS
- 드론
- counter-UAS
- loitering munition
- autonomous system
- low-cost missile
- prototype
- 양산계약
- 정부 조달

SHIPBUILDING_OFFSHORE_BACKLOG
- LNG선
- 컨테이너선
- VLGC
- 해양플랜트
- 조선 기자재
- 엔진
- 피팅밸브
- 선가
- 저가수주 소진
- 후판가
- 인건비
- 인도 시점 마진

SHIPBUILDING_NAVAL_MRO
- 미 해군 MRO
- MSRA
- 미국 조선소 인수
- 군함 정비
- 신조 라이선스
- low-margin experience work
- naval backlog

RAIL_INFRASTRUCTURE
- 고속철
- 도시철도
- 전동차
- 해외 철도수출
- 납품 스케줄
- financing
- warranty
- project margin

NUCLEAR_EXISTING_PPA
- 기존 원전 PPA
- 20년 전력계약
- 재허가
- 무탄소 전력
- 데이터센터 전력수요

NUCLEAR_SMR_GRID_POLICY
- SMR
- NRC approval
- 고객 subscription
- PPA
- target power price
- cost overrun
- project cancellation

GEOPOLITICAL_RECONSTRUCTION
- 우크라 재건
- 네옴시티
- 해외 인프라
- 실제 계약
- financing
- 착공
- 매출 인식
```

---

# 4. 성공사례

## 4-1. 미국 변압기 쇼티지 — `GRID_TRANSFORMER_SHORTAGE`

미국 전력망은 데이터센터, EV, 공장, 재생에너지 프로젝트 때문에 변압기 병목이 심해졌다. Reuters는 2019년 이후 GSU 변압기 수요가 274%, 변전소용 power transformer 수요가 116% 늘었고, 대형 변압기 리드타임은 최대 4년, 가격은 5년간 약 80% 상승했다고 보도했다. 미국 개발사들이 한국·튀르키예 등 수입과 생산 슬롯 선점으로 대응하고 있다는 점도 중요하다. ([Reuters][1])

```text
가격경로 1차 판정:
STRUCTURAL_GRID_BOTTLENECK_REFERENCE

좋은 점:
- 수요 증가율 명확
- 리드타임 장기화
- 가격 상승
- 한국 업체 수출 기회
- 데이터센터·EV·재생에너지·전력망이 동시에 수요를 만듦

주의:
- CAPA 증설 이후 병목 정상화 가능성
- 데이터센터 project delay
- 구리·철강·관세 원가
- 저마진 장기계약 가능성
```

**Loop 3 교정**

```text
GRID_TRANSFORMER_SHORTAGE는 R1 최상위 Green 후보 유지.
다만 stage3 조건을 더 엄격하게 한다.

필수:
계약금액
계약기간
납품시기
매출 대비 계약금액
OP/EPS 상향
수주잔고 증가
마진 개선
```

---

## 4-2. GE Vernova — 데이터센터 전력장비가 실제 orders/backlog로 연결된 사례

GE Vernova는 AI 데이터센터 전력수요가 실제 orders와 backlog로 연결된 좋은 reference다. WSJ는 GE Vernova가 2026년 매출 전망을 445억~455억 달러로 올렸고, 1분기 orders가 71% 증가한 183억 달러, backlog가 1,630억 달러까지 늘었다고 보도했다. 특히 데이터센터 관련 장비 orders가 분기 24억 달러로 전년 전체보다 컸고, 발표 후 주가는 약 15% 상승했으며 2026년 들어 거의 70% 올랐다. ([월스트리트저널][2])

```text
가격경로 1차 판정:
AI_DATA_CENTER_POWER_EQUIPMENT_ALIGNED + 4B_WATCH

좋은 점:
- 데이터센터 orders가 실제 수치로 확인
- electrification unit 매출 성장
- backlog 증가
- 가이던스 상향
- 주가 즉시 반응

주의:
- 이미 2026년 YTD 약 +70%
- valuation crowding
- 데이터센터 project delay
- 풍력 부문 약세와 mix risk
```

**Loop 3 교정**

```text
AI_DATA_CENTER_POWER_EQUIPMENT:
Stage 2까지는 orders/backlog로 가능.
Stage 3는 EPS/FCF 전환과 valuation frame 변화까지 확인.
이미 급등한 경우 SECTOR_SUCCESS_BUT_4B_WATCH로 분리.
```

---

## 4-3. Hanwha Aerospace 루마니아 K9 계약 — `DEFENSE_GOVERNMENT_BACKLOG`

한화에어로스페이스는 루마니아에 K9 자주포 54문, K10 탄약운반장갑차 36대, 탄약·지원 패키지를 공급하는 10억 달러 계약을 체결했고, 계약기간은 2029년 7월까지다. Reuters는 이 계약 후 한화에어로스페이스 주가가 5% 이상 올라 record high를 기록했고, 방산 수주잔고가 2021년 말 5.1조 원에서 2024년 3월 약 30조 원으로 증가했다고 보도했다. ([Reuters][3])

```text
가격경로 1차 판정:
DEFENSE_BACKLOG_ALIGNED_CANDIDATE

좋은 점:
- 정부 고객
- 계약금액 큼
- 계약기간 명확
- 납품 패키지 포함
- 수주잔고 급증
- 주가 record high 반응

주의:
- 현지생산 요구
- 납기
- 원가
- 수출허가
- 환율
- CAPEX/dilution 가능성
```

**Loop 3 교정**

```text
DEFENSE_GOVERNMENT_BACKLOG:
Green 가능 유지.
하지만 backlog만 보지 말고 delivery schedule과 margin을 반드시 확인.
```

---

## 4-4. 한화 유럽 방산 매출 가시성 — 단발 수주에서 지역 플랫폼으로

Reuters는 한화에어로스페이스 CEO가 유럽 육상무기 매출이 2027년까지 두 배가 될 것으로 예상한다고 보도했다. 폴란드 92억 달러, 루마니아 10억 달러 계약과 현지생산 선호가 배경이고, 육상무기 수주잔고가 2020년 이후 10배 증가했다는 점도 중요하다. ([Reuters][4])

```text
가격경로 1차 판정:
MULTI_YEAR_DEFENSE_VISIBILITY_CANDIDATE

좋은 점:
- 단일 계약이 아니라 유럽 지역 반복수요
- 현지생산 모델
- NATO 재무장
- 수주잔고 10배 증가
- 2027년 매출 전망

주의:
- 현지공장 CAPEX
- 유상증자
- 납기 지연
- 정치 리스크
- 유럽 자체 조달 선호
```

**Loop 3 교정**

```text
방산은 단일 계약보다 “지역 플랫폼화”가 되면 visibility 점수 상향.
그러나 CAPEX/dilution이 붙으면 capital allocation overlay를 즉시 적용.
```

---

## 4-5. 한화에어로스페이스 유상증자 — 성공논리 위의 capital allocation shock

방산 구조가 좋아도 자본배분이 나쁘면 가격경로가 깨진다. 한화에어로스페이스는 해외 확장을 위해 3.6조 원 규모 자본조달 계획을 냈고, Reuters는 금융감독원이 공시 보완을 요구했으며 발표 후 주가가 13% 하락했다고 보도했다. ([Reuters][5])

```text
가격경로 1차 판정:
CAPITAL_ALLOCATION_DILUTION_4C_WATCH

의미:
좋은 방산 수주잔고
≠ 무조건 Green 유지

감점 조건:
- 대규모 유상증자
- 목적 불명확
- 해외공장 CAPEX 부담
- 주주가치 희석
- FSS 정정 요구
```

**Loop 3 교정**

```text
DEFENSE_GOVERNMENT_BACKLOG:
수주점수와 별도로 dilution_flag를 hard overlay로 둔다.
수주가 좋아도 유상증자·CAPEX 부담이 EPS/FCF를 훼손하면 Stage 강등.
```

---

## 4-6. 조선 수주·선가 리레이팅 — `SHIPBUILDING_OFFSHORE_BACKLOG`

WSJ는 한국 조선주가 계약 수주 재개와 신조선가 상승으로 급등했고, 삼성중공업 +16%, 한화오션 +13%, HD현대중공업 +11% 가격반응이 나왔다고 보도했다. Clarksons Research 기준 한국이 2월 글로벌 신규 조선 수주 50%를 차지하며 중국을 제치고 1위를 회복했고, 신조선가 지수도 상승했다. ([월스트리트저널][6])

```text
가격경로 1차 판정:
SHIPBUILDING_PRICE_ALIGNED_CANDIDATE

좋은 점:
- 신조선가 상승
- 신규 수주 momentum
- 한국 조선 점유율 회복
- 주가 강한 반응
- 저가수주 소진 기대

주의:
- 후판가
- 인건비
- 납기
- 선종 mix
- 인도 시점 마진
- 이미 주가 반영된 4B 가능성
```

**Loop 3 교정**

```text
SHIPBUILDING_OFFSHORE_BACKLOG:
수주잔고 양보다 수주잔고 질.
선가, 저가수주 소진, 후판가, 인도시점 OPM을 필수 필드로 둔다.
```

---

## 4-7. 한화오션 미 해군 MRO — `SHIPBUILDING_NAVAL_MRO`

한화오션은 미국 해군 MRO 사업을 교두보로 해외 군함 사업을 키우려 한다. Reuters는 한화오션이 필라델피아 조선소를 인수했고, 미국 해군 ship repair and overhaul 계약 2건을 확보했으며, 2030년까지 해외 군함 매출 약 4조 원을 목표로 한다고 보도했다. 다만 해당 MRO 계약 자체는 고수익이라기보다 신조 수주 가능성을 위한 경험·레퍼런스 성격이 크다고 설명됐다. ([Reuters][7])

```text
가격경로 1차 판정:
NAVAL_MRO_OPTION_CANDIDATE

좋은 점:
- 미국 조선소 인수
- 미 해군 MRO 계약 경험
- 해외 군함 매출 목표
- 미국 조선 재건 정책과 연결 가능

주의:
- 초기 MRO는 저마진 가능성
- 미국 법적 제한
- 설비 현대화 CAPEX
- 신조 라이선스 불확실
```

**Loop 3 교정**

```text
SHIPBUILDING_NAVAL_MRO:
MRO 계약 자체는 Stage 2 reference.
Stage 3는 고마진 반복 MRO 또는 신조/군함 수주로 확장될 때만.
```

---

## 4-8. 현대로템 모로코 철도 수주 — `RAIL_INFRASTRUCTURE`

현대로템은 모로코 국영철도 ONCF로부터 약 2.2조 원, 15.4억 달러 규모 2층 전동차 수주를 확보했다. Reuters는 이 계약이 현대로템 철도사업 사상 최대 수주라고 보도했다. ([Reuters][8])

```text
가격경로 1차 판정:
RAIL_INFRASTRUCTURE_STAGE2_CANDIDATE

좋은 점:
- 계약금액 큼
- 해외 철도 인프라 수주
- 회사 철도사업 최대 계약
- 장기 납품 visibility 가능

주의:
- 마진 불명확
- 납품 스케줄
- warranty
- 환율
- 프로젝트 financing
- 원가 상승
```

**Loop 3 교정**

```text
RAIL_INFRASTRUCTURE:
대형 수주만으로 Green 금지.
계약금액/매출, 납품기간, 마진, financing, OP/EPS 상향 확인 필요.
```

---

## 4-9. 기존 원전 PPA — `NUCLEAR_EXISTING_PPA`

Meta는 Constellation의 Illinois Clinton 원전과 20년 계약을 맺어 2027년 이후 원전 운영과 재허가를 지원하기로 했다. Reuters는 Clinton plant가 1,121MW 규모로 약 80만 가구에 전력을 공급할 수 있고, Meta 계약이 AI·데이터센터 전력수요 속에서 Big Tech가 장기 무탄소 전력을 확보하려는 흐름이라고 설명했다. ([Reuters][9])

```text
가격경로 1차 판정:
NUCLEAR_EXISTING_PPA_ALIGNED_REFERENCE

좋은 점:
- 20년 계약
- 기존 원전 자산
- 재허가·운영 지속성
- AI 데이터센터 전력수요와 직접 연결
- SMR보다 증거 강함

주의:
- 한국 원전 기자재로 매핑하려면 직접 계약 필요
- 기존 원전 PPA와 SMR 테마를 절대 섞으면 안 됨
```

**Loop 3 교정**

```text
NUCLEAR_EXISTING_PPA:
Watch-to-Green 가능.
하지만 NUCLEAR_SMR_GRID_POLICY와 분리.
기존 원전 PPA는 cash-flow visibility가 있고, SMR은 execution risk가 크다.
```

---

# 5. 반례

## 5-1. 데이터센터 지역반발·전력·수자원 지연 — `PROJECT_DELAY_CAPEX_OVERLAY`

전력설비 수요가 강해도 데이터센터 자체가 지연되면 신규수주 증가율이 꺾일 수 있다. Gallup 조사 기반 보도에 따르면 미국인 70% 이상이 자기 동네 AI 데이터센터 건설에 반대했고, 반대 이유로 전기·물 사용, 생활비 상승, 오염, 삶의 질 문제가 제시됐다. ([The Verge][10])

또 Utah의 대형 AI 데이터센터 프로젝트는 9GW 전력수요와 대규모 물 사용 우려로 강한 반발을 받고 있고, 지역 주민들이 referendum을 추진하는 등 local opposition이 실제 개발 리스크로 나타나고 있다. ([가디언][11])

```text
가격경로 1차 판정:
DATA_CENTER_PROJECT_DELAY_SOFT_4C

의미:
전력장비 수요는 구조적이지만,
데이터센터 project delay는 전력기기·변압기·케이블 신규수주에 soft 4C로 붙여야 한다.

감점 조건:
- local opposition
- water permitting delay
- grid interconnection delay
- power price backlash
- project cancellation
```

---

## 5-2. SMR 비용초과·프로젝트 취소 — `NUCLEAR_SMR_GRID_POLICY`

NuScale의 UAMPS Carbon Free Power Project는 비용 증가와 고객 확보 부족으로 2023년 취소됐다. 공개 자료 기준 프로젝트 비용은 2020년 36억 달러에서 2023년 93억 달러로 증가했고, 충분한 subscription을 확보하지 못해 UAMPS와 NuScale이 프로젝트 취소를 결정했다. ([위키백과][12])

```text
가격경로 1차 판정:
SMR_COST_OVERRUN_HARD_4C

의미:
SMR 정책 뉴스
≠ 기존 원전 PPA
≠ Green

4C 조건:
- cost overrun
- 고객 subscription 부족
- PPA 전력가격 상승
- financing failure
- project cancellation
```

**Loop 3 교정**

```text
NUCLEAR_SMR_GRID_POLICY:
기본값 Watch/Red.
Stage 2 조건:
PPA, 고객확보, 비용확정, 허가, financing.
Stage 3는 실제 건설·매출 visibility 전까지 제한.
```

---

## 5-3. 방산 dilution — 수주가 좋아도 주주가치가 희석되면 4C-watch

방산 수출이 강해도, 유상증자·해외공장 CAPEX·목적 불명확 자금조달이 붙으면 가격경로가 깨진다. 한화에어로스페이스의 3.6조 원 자본조달 계획은 주가 13% 하락과 감독당국 정정 요구를 불렀다. ([Reuters][5])

```text
가격경로 1차 판정:
DEFENSE_DILUTION_4C_WATCH

감점 조건:
- share_issuance_amount 큼
- use_of_proceeds_clarity 낮음
- overseas_factory_CAPEX
- M&A 자금조달
- regulator_revision_request
```

---

## 5-4. 조선 MRO 저마진·법적 제한

한화오션의 미 해군 MRO 진출은 좋은 옵션이지만, Reuters는 초기 MRO 계약이 고수익이 아니고 향후 신조 수주 가능성을 위한 경험 성격이 크다고 설명했다. 또한 미국 해군 함정 신조에는 법적 제한이 존재하므로, MRO 경험을 곧바로 고마진 신조 backlog로 점수화하면 안 된다. ([Reuters][7])

```text
가격경로 1차 판정:
NAVAL_MRO_OPTION_NOT_YET_STRUCTURAL

의미:
MRO는 Stage 2 reference.
Stage 3는 반복 고마진 MRO나 신조 수주로 연결될 때만 가능.
```

---

## 5-5. 재건·네옴 정책형 인프라

우크라 재건, 네옴시티, 세종시 같은 정책형 인프라는 Theme Tag Map 기준으로 Event/Watch다. 실제 계약·financing·착공·매출 인식 전까지 Green을 주면 안 된다.

```text
가격경로 1차 판정:
POLICY_INFRA_EVENT_PREMIUM

감점 조건:
- MOU only
- funding 없음
- budget 없음
- contractor 불명확
- revenue recognition 없음
```

---

# 6. 4B-watch 사례

## 6-1. 전력설비 4B-watch

```text
4B 조건:
- 변압기 리드타임·가격 상승이 시장에 널리 알려짐
- 전력설비주 전반이 AI 데이터센터 수혜로 동반 상승
- 수주잔고는 강하지만 신규수주 증가율이 둔화
- CAPA 증설 뉴스 증가
- 데이터센터 지역반발·전력망 지연 뉴스 증가
```

GE Vernova처럼 orders·backlog·가이던스·주가가 모두 맞아떨어진 사례는 structural success지만, 이미 큰 폭으로 오른 구간에서는 4B 감시가 필요하다. ([월스트리트저널][2])

---

## 6-2. 방산 4B-watch

```text
4B 조건:
- K방산 수출 narrative를 모두가 인정
- NATO 재무장 기대 과밀
- 목표가 상향 집중
- 현지생산·유상증자·CAPEX를 시장이 낮게 봄
- 수출허가·정치 리스크 무시
```

루마니아 K9 계약과 유럽 매출 전망은 성공 후보지만, 한화에어로스페이스 dilution 사례는 방산에도 4B/4C 감시가 필요하다는 증거다. ([Reuters][3])

---

## 6-3. 조선 4B-watch

```text
4B 조건:
- 신조선가 상승과 수주 회복을 모두가 인정
- 조선주 동반 급등
- 저가수주 소진 기대가 이미 가격에 반영
- 후판가·인건비·납기 리스크 무시
- naval MRO 옵션을 과대평가
```

한국 조선주 급등과 신조선가 상승은 좋은 가격경로지만, Stage 3는 인도 시점 마진과 EPS 전환이 확인되어야 한다. ([월스트리트저널][6])

---

## 6-4. 원전 4B-watch

```text
4B 조건:
- Big Tech nuclear PPA 뉴스로 원전 관련주 동반 과열
- 기존 원전 PPA와 SMR 테마를 섞음
- SMR 비용초과·고객확보 실패 리스크 무시
```

Meta–Constellation PPA는 강한 기존 원전 reference지만, NuScale CFPP 취소는 SMR의 실행 리스크를 보여준다. ([Reuters][9])

---

## 6-5. 철도·인프라 대형수주 4B-watch

```text
4B 조건:
- 대형 해외 철도 계약 뉴스로 관련주 급등
- 계약금액만 보고 마진·warranty·납기·financing 무시
- 실제 OP/EPS 전환 전 가격이 먼저 감
```

현대로템의 모로코 수주는 Stage 2 후보지만, 계약마진과 납품 스케줄, financing을 확인해야 한다. ([Reuters][8])

---

# 7. 4C-thesis-break 사례

## 7-1. 데이터센터 project delay

```text
4C-watch:
local_opposition
water_permitting_delay
grid_interconnection_delay
power_price_backlash
project_cancelled_or_delayed
```

AI 데이터센터 수요는 전력설비의 근거지만, 데이터센터 자체가 지역 반발과 전력·수자원 문제로 지연되면 전력기기 신규수주 속도도 꺾일 수 있다. ([The Verge][10])

---

## 7-2. 방산 dilution / capital allocation shock

```text
4C-watch:
large_equity_issuance
dilution
use_of_proceeds_unclear
regulator_revision_request
overseas_factory_CAPEX_burden
```

한화에어로스페이스 유상증자 사례는 수주잔고가 좋아도 capital allocation이 나쁘면 가격경로가 깨진다는 기준이다. ([Reuters][5])

---

## 7-3. SMR project cancellation

```text
4C:
cost_overrun
customer_subscription_failure
financing_failure
project_cancelled
staff_reduction
```

NuScale CFPP는 SMR archetype에서 hard counterexample이다. ([위키백과][12])

---

## 7-4. 조선 저마진·MRO 옵션 과대평가

```text
4C-watch:
low_margin_MRO
newbuild_license_uncertain
US_legal_restriction
shipyard_modernization_CAPEX
naval_MRO_not_yet_high_margin
```

한화오션의 미국 MRO는 전략적으로 좋지만, MRO 경험을 곧바로 고마진 신조 매출로 처리하면 false-positive가 된다. ([Reuters][7])

---

## 7-5. 철도 project margin / financing risk

```text
4C-watch:
project_financing_delay
low_margin_contract
delivery_delay
warranty_cost
FX_cost
```

현대로템 모로코 수주는 대형 계약이지만, 철도는 계약금액과 실제 이익률이 다를 수 있어 margin과 납품 스케줄을 반드시 분리해야 한다. ([Reuters][8])

---

# 8. 점수비중 보정표 — R1 Loop 3 / v3.0

| canonical archetype                   | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | Loop 3 핵심 감점                                 |
| ------------------------------------- | ------: | ---------: | ---------: | ---------: | --------: | ------: | ---: | -------------------------------------------- |
| `GRID_TRANSFORMER_SHORTAGE`           |      24 |         25 |         24 |         12 |        12 |       1 |    5 | CAPA 정상화, 데이터센터 지연, 저마진 장기계약                 |
| `AI_DATA_CENTER_POWER_EQUIPMENT`      |      22 |         23 |         19 |         13 |        12 |       0 |    5 | project delay, valuation crowding, orders 둔화 |
| `CONTRACT_BACKLOG_INDUSTRIAL`         |      20 |         24 |         18 |         13 |        12 |       1 |    5 | 계약질 불명확, 납기, 마진                              |
| `DEFENSE_GOVERNMENT_BACKLOG`          |      21 |         24 |         17 |         14 |        14 |       3 |    5 | 납기, 수출허가, 현지생산 CAPEX, dilution               |
| `DEFENSE_TECH_AUTONOMOUS_SYSTEMS`     |      19 |         21 |         15 |         15 |        13 |       2 |    5 | prototype, 양산 지연, valuation 과열               |
| `DEFENSE_DRONE_COUNTER_UAS`           |      19 |         21 |         14 |         14 |        13 |       3 |    5 | 생산능력, 수출통제, M&A/dilution                     |
| `DEFENSE_AI_SOFTWARE_INTELLIGENCE`    |      18 |         20 |         10 |         15 |        13 |       0 |    5 | prototype, 반복 SW 매출 부재                       |
| `SHIPBUILDING_OFFSHORE_BACKLOG`       |      21 |         22 |         18 |         13 |        13 |       1 |    5 | 저가수주, 후판가, 인건비, 납기                           |
| `SHIPBUILDING_NAVAL_MRO`              |      17 |         17 |         11 |         13 |        10 |       1 |    5 | 저마진 MRO, 미국 법적 제한, CAPEX                     |
| `RAIL_INFRASTRUCTURE`                 |      20 |         22 |         12 |         14 |        11 |       1 |    5 | 납기, 마진, financing, warranty                  |
| `NUCLEAR_EXISTING_PPA`                |      18 |         22 |         12 |         14 |        12 |       2 |    5 | 재허가, 정책, 특정 plant 리스크                        |
| `NUCLEAR_SMR_GRID_POLICY`             |      14 |         13 |         10 |         13 |         8 |       1 |    5 | 비용초과, 고객확보 실패, 허가, 취소                        |
| `GEOPOLITICAL_RECONSTRUCTION`         |      10 |          8 |          8 |         10 |         7 |       0 |    4 | 실제 계약 없음, financing 없음                       |
| `SMART_FACTORY_AUTOMATION`            |      18 |         16 |          8 |         12 |        10 |       0 |    5 | MOU/PoC, 반복매출 부재                             |
| `PROJECT_DELAY_CAPEX_OVERLAY`         |    gate |       gate |       gate |       gate |      gate |    gate | gate | 데이터센터·철도·원전 project delay                    |
| `CAPITAL_ALLOCATION_DILUTION_OVERLAY` |    gate |       gate |       gate |       gate |      gate |    gate | gate | 대규모 증자, 목적 불명확, CAPEX 부담                     |

Loop 3에서 가장 크게 바뀐 건 네 가지다.

```text
1. GRID_TRANSFORMER_SHORTAGE 점수는 더 강화.
   수요 증가율, 리드타임, 가격 상승, 한국 수입 수요가 모두 확인됐기 때문.

2. AI_DATA_CENTER_POWER_EQUIPMENT도 강화.
   GE Vernova처럼 orders/backlog/가이던스/가격경로가 맞는 사례가 있기 때문.

3. NUCLEAR_EXISTING_PPA와 NUCLEAR_SMR_GRID_POLICY를 완전히 분리.
   기존 원전 PPA는 cash-flow evidence가 있지만, SMR은 cost overrun과 cancellation risk가 크다.

4. CAPITAL_ALLOCATION_DILUTION_OVERLAY를 hard gate로 격상.
   방산 수주가 좋아도 dilution이 나오면 가격경로가 깨질 수 있기 때문.
```

---

# 9. stage date 후보

## `GRID_TRANSFORMER_SHORTAGE`

```text
Stage 1:
데이터센터·EV·재생에너지·전력망 현대화로 변압기 부족 뉴스가 본격화된 날

Stage 2:
개별 기업의 초고압 변압기 공급계약, 수주잔고 급증, 실적 서프라이즈 발생일

Stage 3:
다년 수주잔고 + 가격전가 + FY1/FY2/FY3 OP/EPS 상향이 같이 확인된 날

Stage 4B:
전력설비주 전체가 AI 전력망 수혜로 인정되고 valuation band가 확장된 날

Stage 4C:
데이터센터 프로젝트 지연, 신규수주 둔화, CAPA 정상화, 저마진 계약 확인일
```

## `AI_DATA_CENTER_POWER_EQUIPMENT`

```text
Stage 1:
AI 데이터센터 전력장비 demand, grid modernization, hyperscaler power news

Stage 2:
데이터센터 equipment orders, backlog, revenue guidance 상향 확인일

Stage 3:
orders가 OP/EPS/FCF로 전환되고 valuation frame이 바뀐 날

Stage 4B:
데이터센터 전력장비 수혜 consensus가 과밀해진 날

Stage 4C:
project delay, local opposition, 전력/수자원 permitting 지연, 신규수주 둔화
```

## `DEFENSE_GOVERNMENT_BACKLOG`

```text
Stage 1:
유럽 재무장, NATO 수요, 국방예산 증가 뉴스

Stage 2:
공식 수주계약, 계약금액, 납품 스케줄, 수주잔고 증가 확인일

Stage 3:
다년 매출 visibility + OPM 개선 + EPS 상향 확인일

Stage 4B:
K방산 수출 narrative가 과밀해지고 목표가가 집중 상향되는 날

Stage 4C:
대규모 dilution, 수출허가 문제, 납기 지연, 계약 취소 확인일
```

## `SHIPBUILDING_OFFSHORE_BACKLOG`

```text
Stage 1:
신조선가 상승, LNG선·컨테이너선 발주 회복 뉴스

Stage 2:
대형 수주, 선가 상승, 저가수주 소진 확인일

Stage 3:
고마진 선박 인도와 FY2/FY3 OP 상향이 같이 확인된 날

Stage 4B:
조선주 동반 급등, 선가 narrative 과밀, MRO 기대 과열

Stage 4C:
후판가·인건비 상승, 발주 둔화, 저마진 수주, 납기 지연
```

## `SHIPBUILDING_NAVAL_MRO`

```text
Stage 1:
MSRA, 미 해군 MRO 자격, 미국 조선소 인수 뉴스

Stage 2:
실제 MRO 계약, 작업 기간, 매출 인식 확인일

Stage 3:
반복 고마진 MRO 또는 신조/군함 수주로 확장 확인일

Stage 4B:
미 해군 MRO narrative가 과도하게 반영된 날

Stage 4C:
저마진 MRO, 미국 법적 제한, CAPEX 부담, 신조 라이선스 실패
```

## `RAIL_INFRASTRUCTURE`

```text
Stage 1:
해외 철도 투자·입찰 뉴스

Stage 2:
공식 계약, 계약금액/매출 비중, 납품 스케줄 확인일

Stage 3:
납품 visibility와 OP/EPS 상향이 같이 확인된 날

Stage 4B:
대형 수주 기대가 가격에 대부분 반영된 날

Stage 4C:
프로젝트 지연, financing 문제, 마진 악화, warranty cost
```

## `NUCLEAR_EXISTING_PPA`

```text
Stage 1:
Big Tech 장기 무탄소 전력수요, 기존 원전 PPA 뉴스

Stage 2:
실제 PPA, 계약기간, plant capacity, 재허가 지원 확인일

Stage 3:
PPA가 장기 FCF와 valuation frame 변화로 연결된 날

Stage 4B:
원전 PPA theme가 관련주 전체로 과열된 날

Stage 4C:
재허가 실패, 정책 변화, plant outage, PPA economics 훼손
```

## `NUCLEAR_SMR_GRID_POLICY`

```text
Stage 1:
SMR 정책, AI 전력수요, 원전 기자재 뉴스

Stage 2:
PPA, 고객 subscription, 비용 확정, 허가, financing 확인일

Stage 3:
실제 건설과 매출 visibility가 확인된 날

Stage 4B:
SMR 관련주 동반 과열

Stage 4C:
비용초과, 고객 확보 실패, project cancellation, 허가 지연
```

---

# 10. 가격경로 검증계획

## R1 Loop 3 공통 검증 방식

```text
1. 각 case의 stage1_date, stage2_date, stage3_date를 지정한다.
2. 해당 날짜의 종가를 stage_price로 저장한다.
3. MFE_30D / 90D / 180D / 1Y / 2Y를 계산한다.
4. MAE_30D / 90D / 180D / 1Y를 계산한다.
5. peak_price와 drawdown_after_peak를 계산한다.
6. 계약금액, 계약기간, 납품스케줄, 수주잔고, OP/EPS revision, 마진 변화와 가격경로를 비교한다.
```

## Loop 3에서 새로 강제할 판정

```text
CONTRACT_QUALITY_ALIGNED:
계약금액·기간·납품·마진·OP/EPS가 확인되고 주가도 리레이팅.

BACKLOG_WITHOUT_MARGIN:
수주잔고는 늘었지만 마진·EPS가 불명확.

GRID_BOTTLENECK_STRUCTURAL:
리드타임·가격·수입·CAPA 병목이 동시에 확인.

DATA_CENTER_POWER_4B:
orders/backlog는 강하지만 이미 valuation이 과열.

PROJECT_DELAY_RISK:
수요는 강하지만 데이터센터·철도·원전 프로젝트 지연 가능성.

CAPITAL_ALLOCATION_SHOCK:
수주형 기업이 유상증자·대규모 CAPEX로 주주가치를 희석.

NAVAL_MRO_OPTION_ONLY:
MRO 자격·초기계약은 있지만 고마진 반복매출이나 신조 전환 미확인.

EXISTING_NUCLEAR_PPA_ALIGNED:
기존 원전 장기 PPA가 FCF visibility로 연결.

SMR_POLICY_FALSE_GREEN:
SMR 정책·테마는 있으나 비용·고객·허가·financing 미확인.

POLICY_TO_CONTRACT_FAILED:
재건·네옴·철도·원전 정책 뉴스가 실제 계약으로 연결되지 않음.
```

## 이번 R1 Loop 3에서 우선 검증할 가격 case

| case_id                                         | stage2 후보일 | 현재 1차 가격판정                               |
| ----------------------------------------------- | ---------: | ---------------------------------------- |
| `us_transformer_shortage_import_slots_case`     | 2026-05-11 | 구조적 전력망 병목 reference                     |
| `ge_vernova_data_center_orders_case`            |    2026-04 | +15%, aligned + 4B-watch                 |
| `data_center_local_opposition_grid_case`        |    2026-05 | project delay soft 4C                    |
| `hanwha_aerospace_romania_k9_case`              | 2024-07-09 | +5% record high, defense backlog aligned |
| `hanwha_aerospace_europe_sales_visibility_case` | 2024-10-07 | 유럽 육상무기 매출 visibility                    |
| `hanwha_aerospace_dilution_case`                | 2025-03-27 | -13%, capital allocation 4C-watch        |
| `korean_shipbuilder_contract_rally_case`        |    WSJ 보도일 | 삼성중공업 +16%, 한화오션 +13%, HD현대중공업 +11%      |
| `hanwha_ocean_us_navy_mro_case`                 | 2025-05-05 | MRO option candidate, low-margin watch   |
| `hyundai_rotem_morocco_rail_case`               | 2025-02-26 | 2.2조 원 철도 Stage 2 후보                     |
| `meta_constellation_existing_nuclear_ppa_case`  | 2025-06-03 | 기존 원전 PPA reference                      |
| `nuscale_uamps_smrcancel_case`                  |    2023-11 | SMR hard 4C                              |
| `ukraine_reconstruction_policy_case`            |        계약별 | actual contract before Green             |
| `neom_city_policy_case`                         |        계약별 | actual contract before Green             |

---

# 11. 다음에 에이전트가 채워야 할 price fields

R1 Loop 3에서는 아래 필드를 채우게 해야 한다.

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
contract_value_to_sales
contract_duration_months
contract_start_date
contract_end_date
counterparty
delivery_schedule
backlog_growth
backlog_to_revenue
new_order_growth
book_to_bill

gross_margin_change
op_margin_change
eps_revision_1q
eps_revision_1y
op_revision_1q
op_revision_1y
fcf_margin_change

transformer_type
transformer_lead_time_months
transformer_price_change
factory_slot_prebuy_flag
grid_modernization_flag
data_center_customer_flag

data_center_orders
data_center_backlog
data_center_power_equipment_revenue
project_delay_flag
local_opposition_flag
water_permitting_delay_flag
grid_interconnection_delay_flag

defense_customer_country
government_customer_flag
local_production_flag
export_license_risk_flag
delivery_batch_count
defense_backlog

capex_amount
dilution_flag
share_issuance_amount
use_of_proceeds_clarity
regulator_revision_request_flag

ship_newbuilding_price_index
low_margin_backlog_flag
steel_plate_cost_change
labor_cost_change
naval_mro_contract_flag
msra_flag
naval_newbuild_license_flag
mro_margin_signal

rail_contract_value
rail_delivery_schedule
rail_warranty_risk
rail_financing_secured_flag

nuclear_ppa_flag
ppa_duration_years
plant_capacity_mw
relicensing_support_flag
smr_flag
smr_cost_overrun_flag
customer_subscription_flag
project_cancelled_flag

reconstruction_contract_flag
financing_secured_flag
budget_allocated_flag
construction_started_flag
revenue_recognized_flag

score_price_alignment
price_validation_status
review_notes
```

---

# R1 Loop 3 결론

이번 3회차에서 R1은 이렇게 더 좁혀졌다.

```text
강한 Green 후보:
전력설비·변압기
AI 데이터센터 전력장비
정부고객 다년계약 방산
고마진 조선 수주
기존 원전 장기 PPA

Watch-to-Green:
철도 대형계약
조선 MRO
방산테크·드론·counter-UAS
원전 기자재
산업재 장기계약
스마트팩토리 자동화

Event/Watch:
우크라 재건
네옴시티
정책형 인프라
SMR 정책 테마

Hard 4C:
데이터센터 project delay
방산 dilution
SMR 비용초과·고객확보 실패
조선 저마진/MRO 과대평가
철도 financing·마진 리스크
재건·네옴 실제 계약 부재
```

**R1 Loop 3 점수정규화의 핵심 문장:**

> 산업재·수주·인프라는 “수주가 있다”가 아니라 **계약금액, 계약기간, 거래상대방, 납품스케줄, 수주잔고 질, 마진, OP/EPS 상향, FCF 전환, 가격경로 리레이팅**이 같이 있어야 Green이다.
> Loop 3부터는 특히 `project_delay`, `capital_allocation_shock`, `low_margin_backlog`, `MRO_option_only`, `SMR_policy_false_green`을 강한 감점축으로 넣어야 한다.

다음 순서는 **R2 — AI·반도체·전자부품 Loop 3**다.

[1]: https://www.reuters.com/business/energy/us-power-transformer-buyers-scramble-imports-factory-slots--reeii-2026-05-11/?utm_source=chatgpt.com "US power transformer buyers scramble for imports, factory slots"
[2]: https://www.wsj.com/business/earnings/ge-vernova-lifts-outlook-on-accelerating-power-demand-d81d21e8?utm_source=chatgpt.com "GE Vernova Lifts Outlook on Surge From Data Center Demand"
[3]: https://www.reuters.com/business/aerospace-defense/south-koreas-hanwha-aerospace-wins-1-bln-order-romania-k9-howitzers-2024-07-09/?utm_source=chatgpt.com "South Korea's Hanwha Aerospace wins $1 bln order from Romania for self-propelled howitzers"
[4]: https://www.reuters.com/business/aerospace-defense/hanwha-aerospaces-europe-land-arms-sales-double-by-2027-ceo-says-2024-10-07/?utm_source=chatgpt.com "Hanwha Aerospace's Europe land arms sales to double by 2027, CEO says"
[5]: https://www.reuters.com/business/aerospace-defense/south-korea-market-watchdog-orders-hanwha-aerospace-revise-share-issuance-plan-2025-03-27/?utm_source=chatgpt.com "S. Korea watchdog blocks Hanwha Aerospace $2.5 billion capital raising plan"
[6]: https://www.wsj.com/articles/south-korean-shipbuilders-rally-on-brisk-contract-wins-d44ecb8a?utm_source=chatgpt.com "South Korean Shipbuilders Rally on Brisk Contract Wins"
[7]: https://www.reuters.com/world/asia-pacific/south-koreas-hanwha-ocean-targets-us-navy-orders-trump-seeks-shipbuilding-ties-2025-05-05/?utm_source=chatgpt.com "South Korea's Hanwha Ocean targets US Navy orders as Trump seeks shipbuilding ties"
[8]: https://www.reuters.com/markets/deals/hyundai-rotem-wins-15-billion-order-moroccos-national-rail-operator-2025-02-26/?utm_source=chatgpt.com "Hyundai Rotem wins $1.5 billion order from Morocco's national rail operator"
[9]: https://www.reuters.com/sustainability/climate-energy/meta-signs-power-agreement-with-constellation-nuclear-plant-2025-06-03/?utm_source=chatgpt.com "Meta signs power agreement with Constellation nuclear plant"
[10]: https://www.theverge.com/ai-artificial-intelligence/930477/ai-data-centers-gallup-survey-70-percent-opposition?utm_source=chatgpt.com "Americans do not want AI data centers in their backyards"
[11]: https://www.theguardian.com/us-news/2026/may/13/utah-approves-datacenter-backlash?utm_source=chatgpt.com "'Irresponsible': backlash as Utah approves datacenter twice the size of Manhattan"
[12]: https://en.wikipedia.org/wiki/NuScale_Power?utm_source=chatgpt.com "NuScale Power"

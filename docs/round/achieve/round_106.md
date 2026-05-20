좋아. **R13 Loop 5까지 끝났으니, 규칙대로 다시 R1로 돌아와서 이번은 R1 Loop 6 — 산업재·수주·인프라**다.

R1은 전력설비, 전선·케이블, 피팅밸브, 조선, 조선 기자재, 방산, 원전, 철도, 건설기계, 우크라 재건, 네옴시티를 품는 대섹터다. Theme Tag Map 기준으로도 이 구간은 Green 가능 사례가 많이 나오지만, 수주 뉴스만으로는 부족하고 **계약질 + 마진 + EPS 상향 + 주가 리레이팅**이 같이 가야 한다.

Checkpoint 20 원칙도 계속 강제한다. OpenDART list만 보고 “수주 있음”으로 끝내면 안 되고, 단일판매·공급계약, 신규시설투자, 유상증자, 전환사채, 계약 해지·정정 같은 watch disclosure는 detail에서 계약금액, 계약기간, 매출 대비 계약금액, 거래상대방, OP YoY, 희석률을 실제 확인해야 한다. 없는 값은 만들면 안 된다.

서생원식으로 보면 R1의 질문은 “수주가 많나?”가 아니라 **수주와 병목이 EPS/FCF 체급 변화로 이어지고, 시장이 아직 과거 시클리컬 프레임으로 낮게 보고 있는가**다. 수주잔고가 늘어도 저마진·증자·납기지연·정책 이벤트라면 Stage 3-Green이 아니다.

---

# R1 Loop 6. 산업재·수주·인프라

## 1. 이번 라운드 대섹터

```text
R1 = 산업재·수주·인프라
Loop 6 목표 =
전력망 병목 / 변압기 slot 선점 / 중전압 장비 CAPA /
가스터빈 backlog / AI 데이터센터 전력·수자원·지역반발 /
기존 원전 PPA / SMR false-green /
방산 현지생산·증자 shock / 해군 MRO·미국 조선 option /
철도 대형계약 margin gate를 더 정밀 분리
```

이번 회차의 핵심 질문은 이거다.

```text
이 수주는 이익 체급을 바꾸는 수주인가?
아니면 뉴스성 수주, 정책 수주, 저마진 경험 수주,
CAPEX 부담, dilution, 인허가 지연, 또는 계약 detail 부족인가?
```

R1 Loop 6부터 특히 중요해진 구분은 이거다.

```text
전력설비 수요는 진짜다.
하지만 Green은 “수요가 있다”에서 나오지 않는다.

Green은:
계약금액
계약기간
생산 slot
납품시기
거래상대방
수주잔고
마진
OP/EPS 상향
FCF
가격경로

가 같이 확인될 때 나온다.
```

---

## 2. 대상 canonical archetype

| canonical archetype                    | Loop 6 정책                                                        |
| -------------------------------------- | ---------------------------------------------------------------- |
| `GRID_TRANSFORMER_SHORTAGE`            | R1 최상위 Green 후보. 리드타임·가격·계약·CAPA 확인                              |
| `GRID_EHV_TRANSFORMER_EXPORT`          | Watch-to-Green. 525kV/765kV 등 초고압 변압기 직접계약이면 강화                  |
| `GRID_SUPPLY_SLOT_PREBUY`              | Watch-to-Green. 생산 slot 선점·장기공급·선수금이면 visibility 강화              |
| `GRID_MEDIUM_VOLTAGE_EXPANSION`        | Watch-to-Green. switchgear·MV 장비 CAPA와 수주 확인                     |
| `AI_DATA_CENTER_POWER_EQUIPMENT`       | Green 가능. orders/backlog/guidance와 project delay를 같이 확인          |
| `GAS_TURBINE_POWER_BACKLOG`            | Watch-to-Green. AI 전력수요 수혜지만 turbine slot·tariff·wind drag 확인    |
| `POWER_EQUIPMENT_CAPITAL_RETURN`       | Watch-to-Green. FCF·buyback이 붙으면 4B와 Green을 동시에 감시               |
| `DATA_CENTER_GRID_FLEXIBILITY_OVERLAY` | Watch. AI load flexibility는 전력망 투자지연 완화 후보지만 직접매출 확인 필요          |
| `DATA_CENTER_POWER_WATER_PERMITTING`   | RedTeam gate. 전력·수자원·지역반발·moratorium                             |
| `CONTRACT_BACKLOG_INDUSTRIAL`          | Green 가능. 계약질·마진·EPS 전환 필수                                       |
| `DEFENSE_GOVERNMENT_BACKLOG`           | Green 가능. 정부고객·다년계약·납품스케줄 핵심                                     |
| `DEFENSE_LOCAL_PRODUCTION_PLATFORM`    | Watch-to-Green. 현지생산은 visibility와 CAPEX/dilution을 동시에 봄          |
| `DEFENSE_CAPITAL_ALLOCATION_SHOCK`     | RedTeam gate. 대규모 증자·목적 불명확 CAPEX는 Stage 강등                      |
| `DEFENSE_US_SHIPBUILDING_PLATFORM`     | Watch. 미국 조선 재건·해군 option은 좋지만 실제 수주·CAPEX 확인                    |
| `SHIPBUILDING_OFFSHORE_BACKLOG`        | Green 가능. 선가·저가수주 소진·후판가·인도마진 확인                                 |
| `SHIPBUILDING_NAVAL_MRO`               | Watch-to-Green. MRO 자격·초기계약은 Stage 1~2, 반복 고마진 확인 필요             |
| `SHIPBUILDING_PROCUREMENT_LEADTIME`    | RedTeam overlay. 기자재·pipe spool·procurement delay가 납기와 마진을 훼손    |
| `RAIL_INFRASTRUCTURE`                  | Watch-to-Green. 대형계약은 좋지만 마진·financing·납품스케줄 확인                  |
| `NUCLEAR_EXISTING_PPA_RESTART`         | Watch-to-Green. 기존 원전 PPA·재가동·재허가가 SMR보다 증거 강함                   |
| `NUCLEAR_GRID_INJECTION_RIGHTS`        | RedTeam overlay. 원전 재가동은 grid injection rights와 FERC/PJM gate 필요 |
| `NUCLEAR_SMR_GRID_POLICY`              | Watch/Red. 비용초과·고객확보 실패·허가 리스크                                   |
| `GEOPOLITICAL_RECONSTRUCTION`          | Event/Watch. 실제 수주·financing 전 Green 금지                          |
| `CAPITAL_ALLOCATION_DILUTION_OVERLAY`  | RedTeam gate. 유상증자·CAPEX 부담·목적 불명확                               |
| `DISCLOSURE_CONFIDENCE_CAP`            | RedTeam cap. 계약금액·기간·상대방·마진 미공개 시 Stage 3 제한                     |

---

## 3. deep sub-archetype

```text
GRID_TRANSFORMER_SHORTAGE
- 초고압 변압기
- GSU transformer
- substation transformer
- 525kV EHV transformer
- 765kV transformer
- transformer lead time
- transformer price increase
- factory slot pre-buying
- 한국·튀르키예 수입
- copper / GOES input
- grid modernization

GRID_MEDIUM_VOLTAGE_EXPANSION
- medium-voltage equipment
- switchgear
- substation automation
- utility customer
- grid operator
- data center electrification
- EV / heat pump electrification
- industrial onshoring
- factory capacity expansion

AI_DATA_CENTER_POWER_EQUIPMENT
- 데이터센터 전력장비
- gas turbine
- transformer
- switchgear
- UPS
- PDU
- modular power
- electrification equipment
- backlog
- data center orders
- tariff cost
- wind segment offset risk

GAS_TURBINE_POWER_BACKLOG
- gas turbine slot
- turbine reservation agreement
- power plant backlog
- on-site data center power
- hyperscaler power demand
- tariff
- lead time
- wind segment drag

DEFENSE_GOVERNMENT_BACKLOG
- K9
- K10
- 천무
- K2
- 탄약
- 엔진
- NATO 재무장
- 정부고객
- 다년계약
- 수출허가

DEFENSE_LOCAL_PRODUCTION_PLATFORM
- 루마니아 현지생산
- 폴란드 현지생산
- 유럽 생산거점
- customer-country manufacturing
- local content
- delivery batch
- factory CAPEX
- dilution risk

DEFENSE_US_SHIPBUILDING_PLATFORM
- Philly Shipyard
- Huntington Ingalls
- U.S. Navy auxiliary ships
- Jones Act
- U.S. shipyard acquisition
- shipyard automation
- workforce bottleneck
- MRO
- naval drone option
- nuclear submarine political option

SHIPBUILDING_PROCUREMENT_LEADTIME
- engineered-to-order
- pipe spool
- dynamic procurement event log
- lead-time prediction
- supplier delay
- downstream block assembly delay
- margin penalty

RAIL_INFRASTRUCTURE
- 고속철
- 도시철도
- 이층 전동차
- 해외 철도수출
- 납품 스케줄
- warranty
- FX
- concessionary financing
- local industry support
- project margin

NUCLEAR_EXISTING_PPA_RESTART
- 기존 원전 PPA
- 원전 재가동
- 20년 전력계약
- Microsoft / Meta
- relicensing
- grid injection rights
- 재가동 CAPEX
- data center power demand

NUCLEAR_SMR_GRID_POLICY
- SMR
- NRC approval
- 고객 subscription
- PPA
- target power price
- cost overrun
- project cancellation
- DOE subsidy

DATA_CENTER_POWER_WATER_PERMITTING
- local opposition
- water rights
- power interconnection
- moratorium
- noise pollution
- diesel generator
- referendum
- project withdrawal
```

---

# 4. 성공사례 / 구조 후보

## 4-1. 미국 변압기 쇼티지 + LS Electric 525kV 계약 — `GRID_EHV_TRANSFORMER_EXPORT`

미국 전력망은 데이터센터, EV, 공장, 재생에너지 프로젝트 때문에 변압기 병목이 강해졌다. Reuters는 2019~2025년 GSU transformer 수요가 274%, substation power transformer 수요가 116% 증가했고, 변압기 가격은 5년간 약 80% 올랐으며, 일부 대형 변압기 lead time은 최대 4년까지 늘었다고 보도했다. 같은 보도에서 LS Electric은 2025년 11월 미국 utility와 3.12억 달러 규모 525kV 초고압 변압기 공급계약을 맺어 미국 남동부 대형 데이터센터에 2027~2029년 공급하기로 했다고 언급됐다. ([Reuters][1])

```text
가격경로 1차 판정:
GRID_EHV_TRANSFORMER_EXPORT_STAGE2_CANDIDATE

좋은 점:
- 525kV EHV transformer 직접계약
- 미국 대형 데이터센터 use-case
- 2027~2029년 납품 visibility
- 미국 transformer shortage와 직접 연결
- 한국 업체 수출 reference

주의:
- 계약 마진 미확인
- copper / GOES cost
- 장기계약의 가격전가 조건 필요
- 고객 프로젝트 지연 가능성
- CAPA 증설 후 병목 정상화 가능성
```

**Loop 6 교정**

```text
GRID_TRANSFORMER_SHORTAGE 안에서
GRID_EHV_TRANSFORMER_EXPORT를 더 강하게 분리한다.

일반 전력설비 뉴스:
Stage 1

EHV 계약금액 + 납품기간 + data-center use-case:
Stage 2

OP/EPS 상향 + 수주잔고 + 마진 + FCF:
Stage 3
```

---

## 4-2. ABB 중전압 장비 CAPA — `GRID_MEDIUM_VOLTAGE_EXPANSION`

전력설비 병목은 초고압 변압기만이 아니다. ABB는 유럽 중전압 장비 생산 확대를 위해 3년간 2억 달러를 투자하기로 했고, 제품군에 따라 생산능력을 50~300% 늘릴 수 있다고 밝혔다. 수요 배경은 데이터센터, EV, 난방 전기화, 산업 onshoring, 전력망 운영자 수요다. ([Reuters][2])

```text
가격경로 1차 판정:
GRID_MEDIUM_VOLTAGE_EXPANSION_REFERENCE

좋은 점:
- 중전압 장비까지 병목 확산
- utility / grid operator 수요
- 데이터센터·전기화 수요와 직접 연결
- CAPA 증설 규모 명확

주의:
- CAPA 증설은 수혜이자 미래 공급완화 요인
- 제품 mix별 수익성 확인 필요
- 개별 한국 전력기기주에 매핑하려면 수주·마진 확인 필요
```

**Loop 6 교정**

```text
GRID_MEDIUM_VOLTAGE_EXPANSION은 유지/강화한다.

전력설비 점수는:
EHV transformer
+ MV equipment
+ switchgear
+ substation automation
+ UPS/PDU
+ data-center power chain

으로 확장한다.
```

---

## 4-3. Siemens Energy — `POWER_EQUIPMENT_CAPITAL_RETURN`

Siemens Energy는 전력장비 수요가 FCF와 환원으로 넘어가는 좋은 reference다. Reuters는 Siemens Energy가 AI 데이터센터 수요에 힘입어 2분기 pre-tax free cash flow가 42% 증가했고, 2026년 자사주 매입 규모를 기존 20억 유로에서 30억 유로로 앞당기겠다고 보도했다. WSJ 보도 기준으로도 Siemens Energy는 2026년 1분기 주문이 전년 대비 30% 이상 증가했고, order backlog가 1,460억 유로로 사상 최대를 기록했다. ([Reuters][3])

```text
가격경로 1차 판정:
POWER_EQUIPMENT_BACKLOG_TO_FCF_CANDIDATE

좋은 점:
- AI 데이터센터 전력수요가 orders/backlog로 확인
- FCF 증가
- buyback acceleration
- grid/power generation equipment 양쪽 exposure
- backlog 체급 큼

주의:
- 이미 4B-watch 가능
- 풍력 legacy risk
- tariff cost
- order peak 가능성
- valuation crowding
```

**Loop 6 교정**

```text
POWER_EQUIPMENT_CAPITAL_RETURN 신규 강화.

전력장비 Green 후보는 이제:
backlog
+ margin
+ FCF
+ buyback/dividend
까지 같이 보면 점수 상향.

하지만 4B 구간이면 Valuation 점수는 감점한다.
```

---

## 4-4. GE Vernova — `GAS_TURBINE_POWER_BACKLOG`

GE Vernova는 AI 데이터센터 전력장비 수요가 실제 guidance와 backlog로 연결된 사례다. Reuters는 GE Vernova가 2026년 매출 가이던스를 445억~455억 달러로 올리고 adjusted EBITDA margin 전망도 12~14%로 높였으며, backlog가 1,630억 달러까지 늘었다고 보도했다. 회사는 가스터빈 backlog와 slot reservation이 커지고 있고, 발표 후 주가가 13% 넘게 올랐다. 다만 wind segment 손실과 2026년 2.5억~3.5억 달러 규모 tariff cost는 RedTeam이다. ([Reuters][4])

```text
가격경로 1차 판정:
GAS_TURBINE_POWER_BACKLOG_ALIGNED + 4B_WATCH

좋은 점:
- AI 데이터센터 전력수요가 turbine/grid backlog로 확인
- revenue guidance 상향
- EBITDA margin guidance 상향
- backlog $163B
- 가격경로 +13% 이상

주의:
- wind segment drag
- tariff cost
- gas turbine slot 과열
- 데이터센터 project delay
- 이미 valuation crowding 가능
```

**Loop 6 교정**

```text
GAS_TURBINE_POWER_BACKLOG를 AI_DATA_CENTER_POWER_EQUIPMENT에서 계속 분리한다.

전력장비:
orders/backlog가 강하면 Stage 2.

Stage 3:
power/electrification segment margin
+ FCF
+ legacy wind 손실 통제
+ tariff pass-through
까지 확인해야 한다.
```

---

## 4-5. AI 데이터센터 전력망 stress — `DATA_CENTER_GRID_FLEXIBILITY_OVERLAY`

AI 데이터센터 전력수요는 단순 수요 증가가 아니라 지역 전력망 stress를 만든다. 2026년 arXiv 연구는 상위 AI 기업들의 전력소비가 2024년 약 118TWh에서 2030년 239~295TWh로 늘 수 있고, Oregon, Virginia, Ireland 같은 지역은 지역 전력망 취약성이 커질 수 있다고 분석했다. 또 다른 연구는 AI load flexibility가 위치·부하조건에 따라 grid investment와 운영비를 3~21% 줄일 수 있지만, flexibility가 항상 발전설비 필요량을 줄이는 것은 아니라고 분석했다. ([arXiv][5])

```text
가격경로 1차 판정:
DATA_CENTER_GRID_FLEXIBILITY_WATCH

좋은 점:
- 전력망 병목이 구조적으로 커짐
- grid flexibility / demand response / storage / UPS / MV equipment 수요 연결
- 데이터센터가 power-system planning의 구조요소로 변함

주의:
- 논문·모델 evidence는 Stage 1~2 reference
- 개별 기업 매출 연결 필요
- 지역별 차이가 큼
- flexibility가 모든 CAPEX를 줄이는 것은 아님
```

**Loop 6 교정**

```text
DATA_CENTER_GRID_FLEXIBILITY_OVERLAY 신규 추가.

이 overlay는:
전력설비 수요를 보강하지만,
개별 종목 Stage 3 근거는 아니다.

Stage 3는:
계약
+ 수주
+ 매출
+ OPM/FCF
가 있어야 한다.
```

---

## 4-6. 기존 원전 PPA·재가동 — `NUCLEAR_EXISTING_PPA_RESTART`

기존 원전 PPA는 SMR보다 훨씬 강한 증거다. Meta는 Constellation의 Illinois Clinton Clean Energy Center와 20년 전력계약을 맺어 2027년 zero-emission credit 종료 이후 원전 운영과 재허가를 지원하기로 했다. Microsoft 관련 Three Mile Island 재가동도 Constellation이 FERC 결정을 2026년 6~7월 기대하고 있으며, 핵심 쟁점은 Eddystone gas plant의 grid injection rights를 Crane facility로 이전하는 문제다. ([Reuters][6])

```text
가격경로 1차 판정:
NUCLEAR_EXISTING_PPA_RESTART_CANDIDATE

좋은 점:
- Big Tech 장기 전력수요
- 기존 원전 자산 활용
- 20년 PPA 구조
- 재허가·운영 지속성
- AI 데이터센터 전력수요와 직접 연결

주의:
- grid injection rights
- FERC/PJM gate
- 재가동 CAPEX
- 지역·규제 리스크
- 한국 원전 기자재로 매핑하려면 직접 계약 필요
```

**Loop 6 교정**

```text
NUCLEAR_EXISTING_PPA_RESTART는 NUCLEAR_SMR_GRID_POLICY와 강하게 분리.

기존 원전 PPA:
cash-flow visibility 있음.

SMR:
cost, subscription, licensing, financing risk가 큼.
```

---

## 4-7. Hanwha Aerospace 증자 축소 — `DEFENSE_CAPITAL_ALLOCATION_SHOCK`

방산 구조가 좋아도 자본배분이 나쁘면 가격경로가 깨진다. 한화에어로스페이스는 2025년 3월 3.6조 원 증자 계획을 발표했다가 금융감독원의 정정 요구를 받은 뒤 약 2.3조 원, 16억 달러 규모로 축소했다. Reuters는 회사가 2025년 매출 30조 원, 영업이익 3조 원을 전망했지만, FSS가 증자 목적과 구조조정 전략의 설명이 부족하다고 봤다고 보도했다. ([Reuters][7])

```text
가격경로 1차 판정:
DEFENSE_BACKLOG_GOOD_BUT_CAPITAL_ALLOCATION_GATE

좋은 점:
- 방산 수요와 backlog 성장
- 해외·국내 생산능력 확대 필요성
- 중장기 매출/OP 성장 전망

주의:
- 대규모 dilution
- 사용처 설명 부족
- CAPEX/현지생산 부담
- regulator revision request
- 주주가치 희석
```

**Loop 6 교정**

```text
DEFENSE_GOVERNMENT_BACKLOG에는 dilution gate를 계속 붙인다.

좋은 backlog
+ 대규모 증자
+ 목적 불명확
= stage_after_redteam 강등.
```

---

## 4-8. HD Hyundai Heavy–Huntington Ingalls — `DEFENSE_US_SHIPBUILDING_PLATFORM`

HD Hyundai Heavy와 Huntington Ingalls는 미국 해군 auxiliary ships 공동건조를 위한 협약을 맺었다. Reuters는 이 협약이 미국 군함 건조협력과 미국 조선산업 재건 흐름에 맞닿아 있고, 한국이 미국 조선산업에 1,500억 달러 규모 투자를 약속한 큰 흐름 속에서 나왔다고 보도했다. 다만 이 단계는 MoA와 potential joint investment이지, 반복 고마진 매출이 확인된 Stage 3는 아니다. ([Reuters][8])

```text
가격경로 1차 판정:
US_NAVAL_SHIPBUILDING_OPTION_STAGE1_2

좋은 점:
- 미국 해군 보조함 건조협력 option
- 한국 조선 기술과 미국 수요 결합
- 미국 내 조선능력 재건 narrative
- 장기적으로 MRO/신조/현지투자 option

주의:
- 아직 MoA 단계
- 실제 수주·계약금액 미확인
- 미국 조선소 CAPEX·인력 병목
- 법적·정치적 조건
- margin 미확인
```

**Loop 6 교정**

```text
DEFENSE_US_SHIPBUILDING_PLATFORM 신규 추가.

Stage 1:
MoA / partnership / summit narrative

Stage 2:
계약금액, vessel count, yard investment, schedule

Stage 3:
반복 MRO/newbuild revenue + margin + FCF
```

---

## 4-9. 현대 로템 모로코 철도 — `RAIL_INFRASTRUCTURE`

현대로템은 모로코 국영철도 ONCF로부터 약 2.2조 원, 15.4억 달러 규모 이층 전동차 수주를 확보했다. Reuters는 이 계약이 현대로템 철도사업 사상 최대 수주라고 보도했고, 모로코의 2030 월드컵 대비 철도 확장 계획은 프랑스·스페인·한국 공급사가 참여하는 29억 디르함 규모 열차 구매와도 연결되어 있다. ([Reuters][9])

```text
가격경로 1차 판정:
RAIL_INFRASTRUCTURE_STAGE2_CANDIDATE

좋은 점:
- 계약금액 큼
- 해외 철도 인프라 수주
- 회사 철도사업 최대 계약
- 모로코 2030 월드컵 인프라 확장과 연결
- concessionary financing 구조 존재

주의:
- 마진 불명확
- 납품 스케줄
- warranty
- 환율
- local industry support 조건
```

**Loop 6 교정**

```text
RAIL_INFRASTRUCTURE:
대형 수주만으로 Green 금지.

Stage 3 조건:
계약금액/매출
+ 납품기간
+ financing
+ warranty risk
+ OP/EPS 상향
+ 가격경로 alignment
```

---

# 5. 반례 / RedTeam

## 5-1. 데이터센터 지역반발·moratorium — `DATA_CENTER_POWER_WATER_PERMITTING`

AI 데이터센터 수요는 진짜지만, 지역반발·전력·수자원·소음 문제가 실제 프로젝트 지연으로 바뀌고 있다. Perth 인근 120MW 데이터센터 계획은 약 1,900건의 public submission과 디젤 발전기 소음·문화·환경 민감지역 이슈로 철회됐다. Indianapolis는 데이터센터 moratorium 결의를 통과시켰고, Seattle도 large data center 1년 moratorium을 검토 중이다. ([가디언][10])

```text
가격경로 1차 판정:
DATA_CENTER_PERMITTING_AND_LOCAL_OPPOSITION_4C_WATCH

감점 조건:
- local_opposition_flag
- moratorium_flag
- water_permitting_delay_flag
- grid_interconnection_delay_flag
- diesel_generator_noise_flag
- project_withdrawal_flag
```

**Loop 6 교정**

```text
AI_DATA_CENTER_POWER_EQUIPMENT에도 permitting overlay를 붙인다.

전력설비는 수혜지만,
데이터센터 project delay가 생기면 신규수주 timing과 backlog conversion이 밀린다.
```

---

## 5-2. 데이터센터 water capacity bottleneck

데이터센터는 전력뿐 아니라 물도 병목이다. 2026년 arXiv 연구는 2024년 water use intensity가 유지될 경우 미국 데이터센터가 2030년까지 하루 697~1,451 million gallons의 신규 water capacity를 필요로 할 수 있고, 이는 뉴욕시 평균 일일 공급량 약 1,000 million gallons에 견줄 수 있다고 분석했다. 물 병목은 dry cooling 전환과 전력망 stress를 동시에 만들 수 있다. ([arXiv][11])

```text
가격경로 1차 판정:
DATA_CENTER_WATER_CAPACITY_GATE

의미:
AI 데이터센터 수요가 강해도
water capacity와 cooling 방식이 project economics를 바꾼다.

R1 적용:
전력설비 수주 후보에도 water/permitting delay flag를 붙인다.
```

---

## 5-3. SMR UAMPS 취소 — `NUCLEAR_SMR_GRID_POLICY`

NuScale의 UAMPS Carbon Free Power Project는 비용 증가와 고객 확보 부족으로 2023년 취소됐다. WIRED는 프로젝트가 충분한 power subscription을 확보하지 못했고, 비용 상승으로 첫 미국 SMR deployment의 경제성이 흔들렸다고 설명했다. 즉 SMR은 AI 전력수요와 원전 정책 덕분에 테마가 붙기 쉽지만, 고객확보·비용·허가·financing 전까지 Green을 주면 안 된다. ([WIRED][12])

```text
가격경로 1차 판정:
SMR_COST_AND_SUBSCRIPTION_HARD_4C

4C 조건:
- cost_overrun
- customer_subscription_failure
- financing_failure
- project_cancelled
- staff_reduction
```

**Loop 6 교정**

```text
NUCLEAR_SMR_GRID_POLICY:
기본값 Watch/Red.

Stage 2 조건:
PPA
+ 고객확보
+ 비용확정
+ 허가
+ financing

Stage 3는 실제 건설·매출 visibility 전까지 제한.
```

---

## 5-4. 방산 현지생산·증자 shock

방산 현지생산은 수주 visibility를 높이지만 동시에 CAPEX와 dilution을 만든다. 한화에어로스페이스 증자 축소 사례는 좋은 방산 backlog가 있어도 자본배분이 주가경로를 훼손할 수 있다는 기준이다. ([Reuters][7])

```text
4C-watch:
large_equity_issuance
dilution
use_of_proceeds_unclear
regulator_revision_request
overseas_factory_CAPEX_burden
```

---

## 5-5. 미국 해군·미국 조선 option 과대평가

HD Hyundai–Huntington Ingalls 협약은 긍정적 Stage 1~2 reference지만, MoA를 실제 multi-year revenue로 바로 매핑하면 안 된다. 미국 조선은 인력·dock·CAPEX·법적 제한·정치 조건이 모두 gate가 된다. ([Reuters][8])

```text
4C-watch:
MoA_without_contract
yard_CAPEX_uncertain
US_workforce_bottleneck
legal_political_condition
margin_unknown
delivery_schedule_unknown
```

---

## 5-6. 철도 대형계약 margin / warranty risk

현대로템 모로코 수주는 좋은 Stage 2 후보지만, 철도는 납품기간이 길고 warranty·FX·financing·local content 조건이 붙기 쉽다. 계약금액이 커도 실제 OP/EPS 전환을 확인해야 한다. ([Reuters][9])

```text
4C-watch:
project_financing_delay
low_margin_contract
delivery_delay
warranty_cost
FX_cost
local_content_cost
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
- 데이터센터 moratorium·지역반발 뉴스 증가
```

미국 transformer shortage는 강한 구조증거지만, ABB·Siemens·Hitachi 등 글로벌 업체 CAPA 증설과 데이터센터 지역반발이 동시에 늘면 신규수주 증가율과 valuation을 같이 봐야 한다. ([Reuters][1])

---

## 6-2. AI 전력장비 / gas turbine 4B-watch

```text
4B 조건:
- GE Vernova류 power equipment backlog가 시장에 모두 알려짐
- AI 전력망 narrative로 valuation이 먼저 감
- wind segment 손실·tariff cost를 시장이 무시
- data-center project delay를 반영하지 않음
```

GE Vernova는 orders/backlog/guidance가 실제로 좋아 주가도 급등했지만, 풍력 손실과 tariff cost가 동시에 남아 있다. ([Reuters][4])

---

## 6-3. Power equipment capital return 4B-watch

```text
4B 조건:
- 전력장비 업체가 FCF·buyback을 발표하며 리레이팅
- backlog와 FCF가 모두 알려짐
- buyback이 이미 valuation에 반영
- order peak와 margin normalization을 무시
```

Siemens Energy는 backlog와 FCF가 강하지만, buyback acceleration 이후에는 “좋은 구조”와 “이미 반영된 구조”를 분리해야 한다. ([Reuters][3])

---

## 6-4. 데이터센터 grid flexibility 4B-watch

```text
4B 조건:
- AI load flexibility, demand response, grid software narrative가 과밀
- 실제 utility contract와 software revenue 없이 관련주가 먼저 상승
- 모델 논문 결과를 개별 기업 EPS로 바로 연결
```

AI load flexibility 연구는 전력망 병목의 구조성을 보여주지만, 개별 종목은 실제 계약·매출이 있어야 한다. ([arXiv][13])

---

## 6-5. 방산 4B-watch

```text
4B 조건:
- K방산 수출 narrative를 모두가 인정
- NATO 재무장 기대 과밀
- 목표가 상향 집중
- 현지생산·유상증자·CAPEX를 시장이 낮게 봄
- 수출허가·정치 리스크 무시
```

한화에어로스페이스는 방산 수주와 현지생산 플랫폼이 강하지만, 증자 정정·축소 사례가 보여주듯 자본배분 shock을 반드시 붙여야 한다. ([Reuters][7])

---

## 6-6. 미국 조선·해군 MRO 4B-watch

```text
4B 조건:
- 미국 조선 재건 narrative로 조선주 valuation 상승
- MoA/partnership을 실제 수주처럼 반영
- 미국 yard CAPEX와 인력 병목을 무시
- 정치적 summit headline을 반복매출로 오분류
```

HD Hyundai–Huntington Ingalls 협약은 좋은 option이지만, 계약금액·vessel count·margin·yard investment가 확인되기 전까지 Stage 3는 막아야 한다. ([Reuters][8])

---

## 6-7. 철도·인프라 대형수주 4B-watch

```text
4B 조건:
- 대형 해외 철도 계약 뉴스로 관련주 급등
- 계약금액만 보고 마진·warranty·납기·financing 무시
- 실제 OP/EPS 전환 전 가격이 먼저 감
```

현대로템의 모로코 수주는 Stage 2 후보지만, 계약마진과 납품 스케줄, financing을 확인해야 한다. ([Reuters][9])

---

## 6-8. 원전 4B-watch

```text
4B 조건:
- Big Tech nuclear PPA 뉴스로 원전 관련주 동반 과열
- 기존 원전 PPA와 SMR 테마를 섞음
- grid injection rights와 재가동 CAPEX를 무시
- SMR 비용초과·고객확보 실패 리스크 무시
```

Meta–Constellation PPA와 Microsoft–Three Mile Island 재가동 논의는 기존 원전에는 강한 구조증거지만, NuScale UAMPS 취소는 SMR 실행 리스크를 보여준다. ([Reuters][6])

---

# 7. 4C-thesis-break 사례

## 7-1. 데이터센터 project delay / local opposition

```text
4C-watch:
data_center_project_withdrawal
moratorium
grid_interconnection_delay
water_permitting_delay
local_opposition
utility_cost_pushback
```

Perth의 120MW 데이터센터 철회, Indianapolis moratorium, Seattle moratorium 검토는 AI 데이터센터 수요가 전력장비 수주로 자동 연결되지 않는다는 기준이다. ([가디언][10])

---

## 7-2. 데이터센터 water capacity break

```text
4C-watch:
water_capacity_shortage
dry_cooling_cost_increase
summer_peak_grid_stress
community_water_conflict
project_delay
```

데이터센터가 2030년까지 대규모 신규 water capacity를 필요로 할 수 있다는 연구는 R1 전력설비와 R10 데이터센터 모두에 water gate를 강하게 붙여야 하는 이유다. ([arXiv][11])

---

## 7-3. 방산 자본배분 shock

```text
4C-watch:
share_issuance_amount_large
dilution_flag
regulator_revision_request
use_of_proceeds_unclear
local_factory_capex_flag
```

한화에어로스페이스의 증자 계획 축소는 “좋은 backlog + 나쁜 자본배분”이 같이 나올 수 있음을 보여준다. ([Reuters][7])

---

## 7-4. SMR false-green

```text
4C:
SMR_cost_overrun
customer_subscription_failure
financing_failure
project_cancelled
DOE_support_not_enough
```

SMR은 AI 전력수요와 원전 정책 덕분에 테마가 붙기 쉽지만, NuScale UAMPS처럼 고객 확보와 비용이 맞지 않으면 hard 4C다. ([WIRED][12])

---

## 7-5. 기존 원전 PPA execution risk

```text
4C-watch:
relicensing_failure
grid_injection_rights_failure
restart_capex_overrun
regulatory_delay
PPA_economics_dispute
```

기존 원전 PPA는 SMR보다 증거가 강하지만, Three Mile Island 재가동처럼 grid injection rights와 FERC 결정이 핵심 gate가 될 수 있다. ([Reuters][14])

---

## 7-6. 철도 대형계약 margin failure

```text
4C-watch:
low_margin_contract
FX_cost
warranty_cost
delivery_delay
financing_delay
cost_escalation
```

철도는 대형 계약 발표가 좋아 보여도, 납품기간이 길고 warranty·FX·원가 리스크가 커서 EPS 전환을 반드시 확인해야 한다. ([Reuters][9])

---

## 7-7. 조선 procurement lead-time risk

```text
4C-watch:
supplier_delay
pipe_spool_delay
downstream_block_delay
procurement_lead_time_miss
delivery_delay
margin_penalty
```

2026년 조선 procurement lead-time 연구는 shipbuilding·plant 같은 engineered-to-order 산업에서 pipe spool 같은 핵심 기자재 지연이 downstream 공정을 멈출 수 있음을 보여준다. 즉 조선·플랜트 수주잔고가 좋아도 procurement delay가 납기와 마진을 깨뜨릴 수 있다. ([arXiv][15])

---

# 8. 점수비중 보정표 — R1 Loop 6 / v6.0

| canonical archetype                    | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | Loop 6 핵심 감점                                 |
| -------------------------------------- | ------: | ---------: | ---------: | ---------: | --------: | ------: | ---: | -------------------------------------------- |
| `GRID_TRANSFORMER_SHORTAGE`            |      24 |         25 |         24 |         12 |         9 |       1 |    5 | CAPA 정상화, 데이터센터 지연, 저마진 장기계약                 |
| `GRID_EHV_TRANSFORMER_EXPORT`          |      24 |         25 |         24 |         13 |        10 |       1 |    6 | 계약마진, 납품지연, 구리/GOES, 고객 project delay        |
| `GRID_SUPPLY_SLOT_PREBUY`              |      22 |         24 |         22 |         12 |        10 |       1 |    5 | 선점 슬롯 취소, 고객 프로젝트 지연                         |
| `GRID_MEDIUM_VOLTAGE_EXPANSION`        |      22 |         23 |         20 |         12 |        10 |       1 |    5 | CAPA 증설 후 가격정상화, 제품 mix                      |
| `AI_DATA_CENTER_POWER_EQUIPMENT`       |      22 |         23 |         19 |         13 |        10 |       0 |    5 | project delay, valuation crowding, orders 둔화 |
| `GAS_TURBINE_POWER_BACKLOG`            |      21 |         22 |         18 |         12 |        10 |       0 |    5 | turbine slot, tariff, wind drag, CAPEX       |
| `POWER_EQUIPMENT_CAPITAL_RETURN`       |      22 |         22 |         18 |         12 |         9 |       4 |    5 | buyback 반영, order peak, legacy 손실            |
| `DATA_CENTER_GRID_FLEXIBILITY_OVERLAY` |    gate |       gate |       gate |       gate |      gate |    gate | gate | 모델 evidence를 매출로 오분류                         |
| `DATA_CENTER_POWER_WATER_PERMITTING`   |    gate |       gate |       gate |       gate |      gate |    gate | gate | 지역반발·수자원·전력망·moratorium                      |
| `CONTRACT_BACKLOG_INDUSTRIAL`          |      20 |         24 |         18 |         13 |        12 |       1 |    5 | 계약질 불명확, 납기, 마진                              |
| `DEFENSE_GOVERNMENT_BACKLOG`           |      21 |         24 |         17 |         14 |        14 |       3 |    5 | 납기, 수출허가, 현지생산 CAPEX, dilution               |
| `DEFENSE_LOCAL_PRODUCTION_PLATFORM`    |      21 |         23 |         16 |         14 |        13 |       2 |    5 | 현지공장 CAPEX, margin dilution, 정치 리스크          |
| `DEFENSE_CAPITAL_ALLOCATION_SHOCK`     |    gate |       gate |       gate |       gate |      gate |    gate | gate | 대규모 증자, 목적 불명확, FSS 정정요구                     |
| `DEFENSE_US_SHIPBUILDING_PLATFORM`     |      16 |         16 |         12 |         13 |         9 |       1 |    5 | MoA-only, yard CAPEX, 인력 병목, 미국 법적 조건        |
| `SHIPBUILDING_OFFSHORE_BACKLOG`        |      21 |         22 |         18 |         13 |        13 |       1 |    5 | 저가수주, 후판가, 인건비, 납기                           |
| `SHIPBUILDING_NAVAL_MRO`               |      16 |         17 |         11 |         13 |        10 |       1 |    5 | 저마진 MRO, 미국 법적 제한, CAPEX                     |
| `SHIPBUILDING_PROCUREMENT_LEADTIME`    |    gate |       gate |       gate |       gate |      gate |    gate | gate | 기자재 지연, 납기, margin penalty                   |
| `RAIL_INFRASTRUCTURE`                  |      20 |         22 |         12 |         14 |        11 |       1 |    5 | 납기, 마진, financing, warranty                  |
| `NUCLEAR_EXISTING_PPA_RESTART`         |      19 |         23 |         13 |         14 |        12 |       2 |    5 | 재허가, grid rights, 재가동 CAPEX                  |
| `NUCLEAR_GRID_INJECTION_RIGHTS`        |    gate |       gate |       gate |       gate |      gate |    gate | gate | FERC/PJM, grid capacity transfer 실패          |
| `NUCLEAR_SMR_GRID_POLICY`              |      13 |         12 |         10 |         13 |         7 |       1 |    5 | 비용초과, 고객확보 실패, 허가, 취소                        |
| `GEOPOLITICAL_RECONSTRUCTION`          |      10 |          8 |          8 |         10 |         7 |       0 |    4 | 실제 계약 없음, financing 없음                       |
| `CAPITAL_ALLOCATION_DILUTION_OVERLAY`  |    gate |       gate |       gate |       gate |      gate |    gate | gate | 유상증자, CAPEX 부담, 목적 불명확                       |
| `DISCLOSURE_CONFIDENCE_CAP`            |     cap |        cap |        cap |        cap |       cap |     cap |    + | 계약금액·기간·상대방·마진 미공개                           |

Loop 6에서 가장 크게 바뀐 건 여섯 가지다.

```text
1. GRID_EHV_TRANSFORMER_EXPORT를 추가.
   LS Electric 525kV 미국 데이터센터 계약처럼 직접계약이 확인되는 경우를 일반 전력설비 뉴스와 분리한다.

2. POWER_EQUIPMENT_CAPITAL_RETURN을 추가.
   Siemens Energy처럼 backlog가 FCF와 buyback으로 넘어가면 점수는 올라가지만 4B-watch도 같이 켜진다.

3. DATA_CENTER_GRID_FLEXIBILITY_OVERLAY를 추가.
   AI load flexibility와 grid planning은 구조수요를 보강하지만, 개별 기업 Stage 3 근거는 아니다.

4. DATA_CENTER_POWER_WATER_PERMITTING을 더 강화.
   데이터센터 수요는 진짜지만 지역반발·수자원·moratorium이 project timing을 깨고 있다.

5. DEFENSE_US_SHIPBUILDING_PLATFORM을 추가.
   미국 조선 재건과 한국 조선 협력은 option이지만 MoA-only 단계에서는 Green 금지.

6. SHIPBUILDING_PROCUREMENT_LEADTIME을 추가.
   조선·플랜트 수주잔고는 좋더라도 기자재 조달 지연이 납기와 마진을 훼손할 수 있다.
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

## `GRID_EHV_TRANSFORMER_EXPORT`

```text
Stage 1:
미국·유럽 EHV transformer shortage, 수입 확대, lead time 장기화 뉴스

Stage 2:
525kV/765kV 등 초고압 계약금액·납품기간·고객 use-case 확인

Stage 3:
수주잔고·마진·OP/EPS 상향·FCF 전환 확인

Stage 4B:
K-transformer 수출 narrative 과열

Stage 4C:
납품지연, 고객 project delay, 원가전가 실패, CAPA 정상화
```

## `GRID_MEDIUM_VOLTAGE_EXPANSION`

```text
Stage 1:
중전압 장비·switchgear 수요 증가와 CAPA 증설 뉴스

Stage 2:
개별 기업의 중전압 장비 수주·납품·가이던스 상향 확인일

Stage 3:
제품 mix 개선과 OP/EPS 상향이 같이 확인된 날

Stage 4B:
중전압 장비까지 AI grid narrative가 과밀해진 날

Stage 4C:
CAPA 증설로 리드타임·가격이 정상화되거나 신규수주가 둔화된 날
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

## `GAS_TURBINE_POWER_BACKLOG`

```text
Stage 1:
AI 전력수요와 gas turbine slot shortage 뉴스

Stage 2:
turbine backlog, reservation agreement, power revenue guidance 상향

Stage 3:
turbine backlog가 OP/EPS/FCF와 margin 개선으로 전환

Stage 4B:
gas turbine / AI power narrative 과열

Stage 4C:
tariff cost, turbine delivery delay, wind segment loss, project cancellation
```

## `POWER_EQUIPMENT_CAPITAL_RETURN`

```text
Stage 1:
전력장비 backlog와 AI power demand 확인

Stage 2:
FCF 증가, buyback/dividend, margin guidance 상향 확인

Stage 3:
orders → FCF → capital return이 반복되는 구조 확인

Stage 4B:
capital return까지 시장이 모두 반영한 구간

Stage 4C:
order peak, FCF 둔화, buyback 축소, legacy segment 손실
```

## `DATA_CENTER_POWER_WATER_PERMITTING`

```text
Stage 1:
AI data-center campus / hyperscale project 발표

Stage 2:
전력계통 접속, water rights, zoning, community approval, PPA 확인

Stage 3:
인허가·전력·수자원 확보 후 tenant·NOI/AFFO·equipment order가 붙을 때

Stage 4B:
전력·수자원 리스크 무시한 AI infrastructure 과열

Stage 4C:
moratorium, referendum, project withdrawal, water permit failure, noise/environmental rejection
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

## `DEFENSE_US_SHIPBUILDING_PLATFORM`

```text
Stage 1:
미국 조선 재건, MoA, MRO 자격, summit headline

Stage 2:
실제 vessel contract, MRO order, yard investment, schedule 확인

Stage 3:
반복 MRO/newbuild revenue와 margin이 확인될 때

Stage 4B:
미국 조선 재건 narrative 과열

Stage 4C:
MoA 종료, CAPEX 지연, 인력 병목, 미국 법적·정치 조건 실패
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

## `NUCLEAR_EXISTING_PPA_RESTART`

```text
Stage 1:
Big Tech 장기 무탄소 전력수요, 기존 원전 PPA·재가동 뉴스

Stage 2:
실제 PPA, 계약기간, plant capacity, 재허가·재가동 지원 확인일

Stage 3:
PPA가 장기 FCF와 valuation frame 변화로 연결된 날

Stage 4B:
원전 PPA/restart theme가 관련주 전체로 과열된 날

Stage 4C:
재허가 실패, grid rights 실패, 재가동 CAPEX 초과, PPA economics 훼손
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

## R1 Loop 6 공통 검증 방식

```text
1. 각 case의 stage1_date, stage2_date, stage3_date를 지정한다.
2. 해당 날짜의 종가를 stage_price로 저장한다.
3. MFE_30D / 90D / 180D / 1Y / 2Y를 계산한다.
4. MAE_30D / 90D / 180D / 1Y를 계산한다.
5. peak_price와 drawdown_after_peak를 계산한다.
6. 계약금액, 계약기간, 납품스케줄, 수주잔고, OP/EPS revision,
   마진 변화와 가격경로를 비교한다.
```

## Loop 6에서 새로 강제할 판정

```text
GRID_BOTTLENECK_STRUCTURAL:
리드타임·가격·수입·CAPA 병목이 동시에 확인.

EHV_EXPORT_CONTRACT_ALIGNED:
525kV/765kV 등 초고압 계약금액·납품기간·고객 use-case가 확인.

GRID_SLOT_VISIBILITY:
생산 slot 선점·장기계약·선수금이 확인되어 multi-year visibility가 생김.

MEDIUM_VOLTAGE_EXPANSION_ALIGNED:
중전압 장비 수요와 CAPA 확대가 실제 수주·OPM으로 연결.

POWER_EQUIPMENT_BACKLOG_TO_FCF:
orders/backlog가 FCF와 buyback/dividend로 이어짐.

POWER_EQUIPMENT_4B:
FCF와 buyback이 붙었지만 이미 valuation이 과열된 구간.

GAS_TURBINE_BACKLOG_ALIGNED:
AI 전력수요가 turbine backlog, reservations, guidance로 연결.

DATA_CENTER_PERMITTING_4C:
지역반발, water, grid, moratorium으로 project timing이 깨짐.

DATA_CENTER_GRID_FLEXIBILITY_REFERENCE:
AI load flexibility는 구조수요 보강 근거지만 개별 Stage 3 근거는 아님.

DEFENSE_LOCAL_PRODUCTION_PLATFORM:
단일 수출을 넘어 고객국 현지생산과 반복수요로 확장.

CAPITAL_ALLOCATION_SHOCK:
수주형 기업이 유상증자·대규모 CAPEX로 주주가치를 희석.

US_NAVAL_SHIPBUILDING_OPTION:
MoA·MRO·미국 조선 재건 option은 있으나 실제 수주·마진 전까지 Watch.

SHIPBUILDING_PROCUREMENT_DELAY_RISK:
조선·플랜트 기자재 조달 지연이 납기·마진을 훼손.

EXISTING_NUCLEAR_PPA_RESTART_ALIGNED:
기존 원전 장기 PPA·재가동이 FCF visibility로 연결.

NUCLEAR_GRID_INJECTION_GATE:
원전 재가동은 grid injection rights·FERC/PJM 승인 전까지 cap.

SMR_POLICY_FALSE_GREEN:
SMR 정책·테마는 있으나 비용·고객·허가·financing 미확인.

RAIL_CONTRACT_STAGE2_NOT_GREEN:
대형 철도계약은 있으나 마진·납기·warranty 확인 전.

DISCLOSURE_CONFIDENCE_CAPPED:
계약금액·기간·상대방·마진이 detail에서 확인되지 않아 Stage 3 제한.
```

## 이번 R1 Loop 6에서 우선 검증할 가격 case

| case_id                                            | stage2 후보일 | 현재 1차 가격판정                                    |
| -------------------------------------------------- | ---------: | --------------------------------------------- |
| `us_transformer_shortage_import_slots_case`        | 2026-05-11 | 구조적 전력망 병목 reference                          |
| `ls_electric_525kv_us_datacenter_transformer_case` |    2025-11 | $312m, EHV transformer direct mapping 후보      |
| `abb_medium_voltage_expansion_case`                | 2026-05-11 | 중전압 장비 CAPA 확대 reference                      |
| `siemens_energy_fcf_buyback_case`                  | 2026-05-12 | FCF + buyback, power equipment capital return |
| `siemens_energy_record_backlog_case`               |    2026-02 | €146B backlog, AI DC order reference          |
| `ge_vernova_data_center_orders_case`               | 2026-04-22 | AI power equipment aligned + 4B-watch         |
| `ge_vernova_gas_turbine_backlog_case`              | 2026-04-22 | turbine/storage/power backlog candidate       |
| `data_center_grid_flexibility_case`                |    2026-04 | grid flexibility reference, not company Green |
| `perth_data_center_withdrawal_case`                | 2026-05-15 | data center permitting 4C-watch               |
| `indianapolis_data_center_moratorium_case`         | 2026-05-15 | local moratorium overlay                      |
| `seattle_data_center_moratorium_case`              | 2026-05-15 | urban moratorium overlay                      |
| `water_capacity_data_center_case`                  |    2026-03 | water capacity bottleneck reference           |
| `hanwha_aerospace_dilution_trim_case`              | 2025-04-07 | defense cap allocation shock                  |
| `hd_hyundai_huntington_us_navy_aux_case`           | 2025-10-26 | U.S. naval shipbuilding option                |
| `hyundai_rotem_morocco_rail_case`                  | 2025-02-26 | $1.54B rail Stage 2 후보                        |
| `meta_constellation_clinton_ppa_case`              | 2025-06-03 | 기존 원전 20년 PPA reference                       |
| `constellation_tmi_microsoft_restart_case`         | 2026-05-11 | 원전 재가동 + grid injection rights gate           |
| `nuscale_uamps_smr_cancel_case`                    |    2023-11 | SMR hard 4C                                   |
| `shipbuilding_procurement_leadtime_case`           |    2026-01 | procurement delay/margin risk overlay         |
| `ukraine_reconstruction_policy_case`               |        계약별 | actual contract before Green                  |
| `neom_city_policy_case`                            |        계약별 | actual contract before Green                  |

---

# 11. 다음에 에이전트가 채워야 할 price fields

R1 Loop 6에서는 아래 필드를 채우게 해야 한다.

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
buyback_amount
dividend_change

transformer_type
transformer_voltage_kv
ehv_transformer_flag
transformer_lead_time_months
transformer_price_change
factory_slot_prebuy_flag
grid_modernization_flag
data_center_customer_flag
foreign_import_flag
korea_export_flag
goes_cost_change
copper_cost_change

medium_voltage_order
medium_voltage_capacity_expansion
switchgear_order
substation_equipment_order
utility_customer_flag
grid_operator_customer_flag

gas_turbine_backlog_gw
gas_turbine_slot_reservation_gw
power_equipment_backlog
storage_equipment_order
electrification_profit_growth
wind_segment_loss
tariff_cost_amount

data_center_orders
data_center_backlog
data_center_power_equipment_revenue
data_center_grid_flexibility_flag
data_center_flexibility_savings_estimate
project_delay_flag
local_opposition_flag
moratorium_flag
water_permitting_delay_flag
water_capacity_requirement
grid_interconnection_delay_flag
diesel_generator_noise_flag
project_withdrawal_flag

defense_customer_country
government_customer_flag
local_production_flag
local_content_requirement
export_license_risk_flag
delivery_batch_count
defense_backlog
nato_customer_flag
technology_transfer_flag

capex_amount
dilution_flag
share_issuance_amount
use_of_proceeds_clarity
regulator_revision_request_flag
local_factory_capex_flag
margin_dilution_flag

us_shipbuilding_platform_flag
naval_auxiliary_ship_flag
us_navy_customer_flag
mro_contract_flag
moa_only_flag
yard_capex_amount
us_workforce_bottleneck_flag
jones_act_flag

shipbuilding_procurement_delay_flag
pipe_spool_delay_flag
procurement_lead_time_days
supplier_delay_flag
delivery_delay_flag
margin_penalty_flag

rail_contract_value
rail_delivery_schedule
rail_warranty_risk
rail_financing_secured_flag
rail_local_content_requirement
rail_fx_risk

nuclear_ppa_flag
ppa_duration_years
plant_capacity_mw
relicensing_support_flag
nuclear_restart_flag
grid_injection_rights_flag
restart_capex_amount
ferc_approval_flag
pjm_interconnection_delay_flag

smr_flag
smr_cost_overrun_flag
customer_subscription_flag
project_cancelled_flag
doe_subsidy_flag

reconstruction_contract_flag
financing_secured_flag
budget_allocated_flag
construction_started_flag
revenue_recognized_flag

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

# R1 Loop 6 결론

이번 6회차에서 R1은 더 촘촘해졌다.

```text
강한 Green 후보:
초고압 변압기·전력설비 병목
EHV transformer 직접 수출계약
생산 slot 선점이 확인되는 전력장비
중전압 장비·switchgear 확장
AI 데이터센터 전력장비 중 orders/backlog/guidance가 확인된 기업
가스터빈 backlog와 전력장비 FCF가 확인되는 기업
정부고객 다년계약 방산
고마진 조선 수주
기존 원전 장기 PPA·재가동

Watch-to-Green:
철도 대형계약
조선 MRO
미국 조선 재건 platform
방산 현지생산 플랫폼
방산 무인 해양시스템
원전 기자재
산업재 장기계약
스마트팩토리 자동화
grid flexibility / demand response / data-center power software

Event/Watch:
우크라 재건
네옴시티
정책형 인프라
SMR 정책 테마
미 해군 MRO option
미국 조선 MoA
무인 해양시스템 partnership

Hard 4C:
데이터센터 project delay / moratorium / 지역반발
데이터센터 water capacity bottleneck
방산 dilution
SMR 비용초과·고객확보 실패
미국 조선 MoA-only 과대평가
조선 procurement lead-time delay
철도 financing·마진·warranty 리스크
기존 원전 grid injection rights 실패
재건·네옴 실제 계약 부재
계약 detail 부족으로 인한 disclosure confidence cap
```

**R1 Loop 6 점수정규화의 핵심 문장:**

> 산업재·수주·인프라는 “수주가 있다”가 아니라 **계약금액, 계약기간, 거래상대방, 납품스케줄, 수주잔고 질, 생산 slot, 마진, OP/EPS 상향, FCF 전환, 가격경로 리레이팅**이 같이 있어야 Green이다.
> Loop 6부터는 특히 `GRID_EHV_TRANSFORMER_EXPORT`, `POWER_EQUIPMENT_CAPITAL_RETURN`, `DATA_CENTER_GRID_FLEXIBILITY_OVERLAY`, `DATA_CENTER_POWER_WATER_PERMITTING`, `DEFENSE_US_SHIPBUILDING_PLATFORM`, `SHIPBUILDING_PROCUREMENT_LEADTIME`, `NUCLEAR_GRID_INJECTION_RIGHTS`, `DISCLOSURE_CONFIDENCE_CAP`을 강한 보정축으로 넣어야 한다.

다음 순서는 **R2 — AI·반도체·전자부품 Loop 6**다.

[1]: https://www.reuters.com/business/energy/us-power-transformer-buyers-scramble-imports-factory-slots--reeii-2026-05-11/?utm_source=chatgpt.com "US power transformer buyers scramble for imports, factory slots"
[2]: https://www.reuters.com/sustainability/boards-policy-regulation/abb-invest-200-million-medium-voltage-equipment-production-europe-2026-05-11/?utm_source=chatgpt.com "ABB to invest $200 million in medium-voltage equipment production in Europe"
[3]: https://www.reuters.com/sustainability/climate-energy/siemens-energy-accelerates-share-buyback-after-q2-cash-flow-jumps-2026-05-12/?utm_source=chatgpt.com "Siemens Energy accelerates share buyback after Q2 cash flow jumps"
[4]: https://www.reuters.com/business/energy/ge-vernova-lifts-annual-revenue-forecast-data-center-demand-2026-04-22/?utm_source=chatgpt.com "GE Vernova lifts 2026 outlook as AI boom fuels power equipment demand"
[5]: https://arxiv.org/abs/2604.06198?utm_source=chatgpt.com "Concentrated siting of AI data centers drives regional power-system stress under rising global compute demand"
[6]: https://www.reuters.com/sustainability/climate-energy/meta-signs-power-agreement-with-constellation-nuclear-plant-2025-06-03/?utm_source=chatgpt.com "Meta signs power agreement with Constellation nuclear plant"
[7]: https://www.reuters.com/business/aerospace-defense/south-koreas-hanwha-aerospace-trims-capital-increase-plan-16-bln-2025-04-07/?utm_source=chatgpt.com "South Korea's Hanwha Aerospace trims capital increase plan to $1.6 bln"
[8]: https://www.reuters.com/world/asia-pacific/hd-hyundai-heavy-huntington-ingalls-jointly-build-us-navy-auxiliary-ships-2025-10-26/?utm_source=chatgpt.com "HD Hyundai Heavy, Huntington Ingalls to jointly build U.S. navy auxiliary ships"
[9]: https://www.reuters.com/markets/deals/hyundai-rotem-wins-15-billion-order-moroccos-national-rail-operator-2025-02-26/?utm_source=chatgpt.com "Hyundai Rotem wins $1.5 billion order from Morocco's national rail operator"
[10]: https://www.theguardian.com/technology/2026/may/15/developer-withdraws-plans-for-perth-datacentre-after-fierce-community-opposition?utm_source=chatgpt.com "Developer withdraws plans for Perth datacentre after fierce community opposition"
[11]: https://arxiv.org/abs/2603.02705?utm_source=chatgpt.com "Small Bottle, Big Pipe: Quantifying and Addressing the Impact of Data Centers on Public Water Systems"
[12]: https://www.wired.com/story/first-small-scale-nuclear-plant-us-nuscale-canceled?utm_source=chatgpt.com "The First Small-Scale Nuclear Plant in the US Died Before It Could Live"
[13]: https://arxiv.org/abs/2604.05376?utm_source=chatgpt.com "To Defer or To Shift? The Role of AI Data Center Flexibility on Grid Interconnection"
[14]: https://www.reuters.com/business/energy/us-may-decide-three-mile-island-restart-june-constellation-execs-say-2026-05-11/?utm_source=chatgpt.com "US may decide on Three Mile Island restart in June, Constellation execs say"
[15]: https://arxiv.org/abs/2601.19296?utm_source=chatgpt.com "Process-Aware Procurement Lead Time Prediction for Shipyard Delay Mitigation"

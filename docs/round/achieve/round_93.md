좋아. **R13 Loop 4까지 끝났으니, 규칙대로 다시 R1로 돌아와서 이번은 R1 Loop 5 — 산업재·수주·인프라**다.

R1은 전력설비, 전선·케이블, 피팅밸브, 조선, 조선 기자재, 방산, 원전, 철도, 건설기계, 우크라 재건, 네옴시티를 품는 대섹터다. Theme Tag Map 기준으로도 이 구간은 Green 가능 사례가 많이 나오지만, 수주 뉴스만으로는 부족하고 **계약질 + 마진 + EPS 상향 + 주가 리레이팅**이 같이 가야 한다.

또 Checkpoint 20 원칙상 OpenDART list만 보면 안 되고, 단일판매·공급계약, 신규시설투자, 유상증자, 전환사채, 감사의견, 거래정지, 계약 해지·취소·정정 같은 watch disclosure는 detail에서 계약금액, 계약기간, 매출 대비 계약금액, 거래상대방, OP YoY, dilution 등을 실제 확인해야 한다. 없는 값을 만들면 R1에서는 “수주가 크다”, “전력설비 수혜다”, “방산 수주다” 같은 false-positive가 바로 생긴다.

서생원식으로 보면 R1의 질문은 “수주가 많나?”가 아니라 **수주와 병목이 EPS/FCF 체급 변화로 이어지고, 시장이 아직 과거 시클리컬 프레임으로 낮게 보고 있는가**다. 수주잔고가 늘어도 저마진·증자·납기지연·정책 이벤트라면 Stage 3-Green이 아니다.

---

# R1 Loop 5. 산업재·수주·인프라

## 1. 이번 라운드 대섹터

```text
R1 = 산업재·수주·인프라
Loop 5 목표 =
전력 병목 / 방산 다년계약 / 현지생산 플랫폼 / 방산 dilution /
기존 원전 PPA·재가동 / SMR false-green / 철도 대형계약 /
조선 MRO option / 데이터센터 permitting risk를 더 정밀 분리
```

이번 회차의 핵심 질문은 이거다.

```text
이 수주는 이익 체급을 바꾸는 수주인가?
아니면 뉴스성 수주, 정책 수주, 저마진 경험 수주, 프로젝트 지연,
CAPEX 부담, dilution, 또는 계약 detail 부족인가?
```

R1에서 가장 위험한 오판은 여전히 이거다.

```text
수주잔고 증가
= 무조건 Green
```

Loop 5부터는 특히 아래처럼 본다.

```text
좋은 수주:
계약금액 큼
계약기간 김
납품 스케줄 명확
매출 대비 계약금액 큼
거래상대방 신용도 높음
가격전가 또는 마진 개선 가능
수주잔고가 FY1/FY2/FY3 EPS로 전환
주가가 실적경로와 같이 리레이팅

나쁜 수주:
계약금액 불명확
마진 불명확
MOU/LOI 수준
financing 미확정
납기·인허가 지연 위험
CAPEX나 유상증자가 따라옴
저마진 reference work
정책 테마만 있고 실제 매출화 없음
```

---

## 2. 대상 canonical archetype

| canonical archetype                   | Loop 5 정책                                                     |
| ------------------------------------- | ------------------------------------------------------------- |
| `GRID_TRANSFORMER_SHORTAGE`           | R1 최상위 Green 후보. 리드타임·가격·계약·CAPA 확인                           |
| `GRID_MEDIUM_VOLTAGE_EXPANSION`       | Watch-to-Green. 변압기뿐 아니라 switchgear·MV 장비 CAPA 확인             |
| `GRID_SUPPLY_SLOT_PREBUY`             | Watch-to-Green. 생산 슬롯 선점·장기공급계약이면 visibility 강화               |
| `AI_DATA_CENTER_POWER_EQUIPMENT`      | Green 가능. orders/backlog/guidance와 project delay를 같이 확인       |
| `GAS_TURBINE_POWER_BACKLOG`           | Watch-to-Green. AI 전력수요 수혜지만 turbine slot·tariff·wind drag 확인 |
| `CONTRACT_BACKLOG_INDUSTRIAL`         | Green 가능. 계약질·마진·EPS 전환 필수                                    |
| `DEFENSE_GOVERNMENT_BACKLOG`          | Green 가능. 정부고객·다년계약·납품스케줄 핵심                                  |
| `DEFENSE_LOCAL_PRODUCTION_PLATFORM`   | Watch-to-Green. 현지생산은 visibility와 CAPEX/dilution을 동시에 봄       |
| `DEFENSE_CAPITAL_ALLOCATION_SHOCK`    | RedTeam gate. 대규모 증자·목적 불명확 CAPEX는 Stage 강등                   |
| `DEFENSE_UNMANNED_NAVAL_SYSTEMS`      | Watch. 실제 국방계약·양산·납품 전 Green 제한                               |
| `SHIPBUILDING_OFFSHORE_BACKLOG`       | Green 가능. 선가·저가수주 소진·후판가·인도마진 확인                              |
| `SHIPBUILDING_NAVAL_MRO`              | Watch-to-Green. MRO 경험은 좋지만 신조/고마진 전환 필요                      |
| `RAIL_INFRASTRUCTURE`                 | Watch-to-Green. 대형계약은 좋지만 마진·financing·납품스케줄 확인               |
| `NUCLEAR_EXISTING_PPA_RESTART`        | Watch-to-Green. 기존 원전 PPA·재가동·재허가가 SMR보다 증거 강함                |
| `NUCLEAR_SMR_GRID_POLICY`             | Watch/Red. 비용초과·고객확보 실패·허가 리스크                                |
| `GEOPOLITICAL_RECONSTRUCTION`         | Event/Watch. 실제 수주·financing 전 Green 금지                       |
| `DATA_CENTER_GRID_PERMITTING_OVERLAY` | RedTeam overlay. 데이터센터·전력망 지역반발·수자원·인허가 지연                    |
| `CAPITAL_ALLOCATION_DILUTION_OVERLAY` | RedTeam gate. 유상증자·CAPEX 부담·목적 불명확                            |
| `DISCLOSURE_CONFIDENCE_CAP`           | RedTeam cap. 계약금액·상대방·기간·마진 미공개 시 Stage 3 제한                  |

---

## 3. deep sub-archetype

```text
GRID_TRANSFORMER_SHORTAGE
- 초고압 변압기
- GSU transformer
- substation transformer
- 525kV EHV transformer
- transformer lead time
- transformer price increase
- factory slot pre-buying
- 한국·튀르키예 수입
- grid modernization
- copper / GOES input

GRID_MEDIUM_VOLTAGE_EXPANSION
- 중전압 장비
- switchgear
- substation automation
- medium-voltage product line
- utility demand
- data center electrification
- EV / heat pump electrification
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

SHIPBUILDING_NAVAL_MRO
- 미국 해군 MRO
- MSRA
- Philly Shipyard
- Jones Act
- 미 해군 정비
- autonomous underwater drone
- China sanction risk
- low-margin reference work

RAIL_INFRASTRUCTURE
- 고속철
- 도시철도
- 전동차
- 해외 철도수출
- 납품 스케줄
- warranty
- FX
- financing
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

DATA_CENTER_GRID_PERMITTING_OVERLAY
- local opposition
- water rights
- power interconnection
- moratorium
- noise pollution
- community opposition
- referendum
- project withdrawal
```

---

# 4. 성공사례 / 구조 후보

## 4-1. 미국 변압기 쇼티지 — `GRID_TRANSFORMER_SHORTAGE`

미국 전력망은 데이터센터, EV, 공장, 재생에너지 프로젝트 때문에 변압기 병목이 심해졌다. Reuters는 2019~2025년 사이 GSU transformer 수요가 274%, substation power transformer 수요가 116% 증가했고, 변압기 가격은 5년간 약 80% 올랐으며, 일부 고용량 변압기는 lead time이 최대 4년까지 늘었다고 보도했다. 또 미국 개발사들이 한국·튀르키예 수입, 생산 슬롯 선점, 노후 장비 재활용까지 동원하고 있다고 했다. ([Reuters][1])

```text
가격경로 1차 판정:
GRID_BOTTLENECK_STRUCTURAL_REFERENCE

좋은 점:
- 수요 증가율 명확
- 리드타임 장기화
- 가격 상승
- 한국 업체 수출 기회
- 데이터센터·EV·재생에너지·공장 수요가 동시에 작동
- factory slot pre-buying까지 등장

주의:
- CAPA 증설 후 병목 정상화 가능성
- 데이터센터 project delay
- 구리·GOES·철강·관세 원가
- 저마진 장기계약 가능성
```

**Loop 5 교정**

```text
GRID_TRANSFORMER_SHORTAGE는 R1 최상위 Green 후보 유지.

다만 Stage 3 조건을 더 엄격하게 한다:
계약금액
계약기간
납품시기
매출 대비 계약금액
거래상대방
OP/EPS 상향
수주잔고 증가
마진 개선
```

---

## 4-2. ABB 중전압 장비 투자 — `GRID_MEDIUM_VOLTAGE_EXPANSION`

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
- ABB 개별 capex는 공급 완화 요인이기도 함
- CAPA 증설 이후 가격·리드타임 정상화 가능
- 개별 한국 전력기기주에 매핑하려면 수주·마진 확인 필요
```

**Loop 5 교정**

```text
GRID_MEDIUM_VOLTAGE_EXPANSION은 GRID_TRANSFORMER_SHORTAGE의 하위축이 아니라
별도 canonical로 유지한다.

전력설비 scoring은:
초고압 변압기
+ 중전압 장비
+ switchgear
+ substation automation
+ PDU/UPS
+ grid software

로 확장하되, CAPA 정상화 flag를 같이 둔다.
```

---

## 4-3. GE Vernova — `AI_DATA_CENTER_POWER_EQUIPMENT` + `GAS_TURBINE_POWER_BACKLOG`

GE Vernova는 AI 데이터센터 전력장비 수요가 실제 orders/backlog/guidance로 연결된 사례다. 2026년 4월 GE Vernova는 revenue guidance를 445억~455억 달러로 올렸고, adjusted EBITDA margin도 12~14%로 상향했다. backlog는 1,630억 달러까지 늘었고, 회사는 2027년까지 backlog 2,000억 달러 달성을 기대한다고 밝혔다. 발표 후 주가는 13% 넘게 상승했다. 다만 wind segment 손실, tariff cost 2.5억~3.5억 달러는 RedTeam이다. ([Reuters][3])

```text
가격경로 1차 판정:
AI_DATA_CENTER_POWER_EQUIPMENT_ALIGNED + 4B_WATCH

좋은 점:
- AI 데이터센터 전력수요가 orders/backlog로 확인
- 매출·마진 전망 상향
- backlog 증가
- 전력·전기화 부문 이익 개선
- 가격경로 +13% 이상

주의:
- 이미 주가가 강하게 반영된 4B 가능성
- 풍력 부문 손실
- tariff cost
- 데이터센터 project delay
```

**Loop 5 교정**

```text
AI_DATA_CENTER_POWER_EQUIPMENT:
Stage 2까지는 orders/backlog/guidance로 가능.

Stage 3는:
EPS/FCF 전환
+ segment mix 개선
+ wind/legacy 손실 통제
+ valuation frame 변화

까지 확인해야 한다.
```

---

## 4-4. 미국 전력수요 record 경로 — R1 전체 macro tailwind

EIA는 미국 전력소비가 2025년 4,195 billion kWh에서 2026년 4,248 billion kWh, 2027년 4,379 billion kWh로 올라 새 기록을 세울 것으로 전망했다. 특히 AI·crypto 데이터센터, 난방·수송 전기화가 수요를 끌고, 2027년에는 commercial electricity sales가 residential을 처음 넘어설 것으로 봤다. 이는 R1 전력설비의 macro tailwind지만, 개별 종목 Green은 여전히 계약·마진·EPS 전환으로 확인해야 한다. ([Reuters][4])

```text
가격경로 1차 판정:
GRID_MACRO_TAILWIND_NOT_COMPANY_GREEN

의미:
전력수요 증가는 R1 전체 점수의 배경 가점.
하지만 개별 종목은 contract/detail evidence 없으면 Stage 3 금지.
```

---

## 4-5. 데이터센터 지역반발 — 전력설비 수요의 soft 4C

전력설비 수요는 구조적으로 강하지만, 데이터센터 프로젝트 자체가 지연되면 전력장비 신규수주 timing도 흔들릴 수 있다. Perth 인근 120MW 데이터센터 계획은 약 1,900건의 반대 의견, 문화·환경 민감지역, 학교·주거지 인접, 비상 디젤 발전기 소음 우려 때문에 철회됐다. Seattle은 대형 데이터센터 moratorium을 검토 중이고, Indianapolis도 새로운 데이터센터 건설 moratorium을 통과시켰다. ([가디언][5])

```text
가격경로 1차 판정:
DATA_CENTER_GRID_PERMITTING_SOFT_4C

의미:
전력설비 수요는 강하다.
하지만 데이터센터 project delay는 신규수주 증가율과 order timing을 흔들 수 있다.

감점 조건:
- local_opposition_flag
- moratorium_flag
- water_permitting_delay_flag
- grid_interconnection_delay_flag
- diesel_generator_noise_flag
- project_withdrawal_flag
```

**Loop 5 교정**

```text
전력설비 Green 후보에도 DATA_CENTER_GRID_PERMITTING_OVERLAY를 붙인다.

수요 강함:
가점

프로젝트 인허가·지역반발:
납품시기/신규수주 지연 감점
```

---

## 4-6. Hanwha Aerospace 루마니아 K9 계약 — `DEFENSE_GOVERNMENT_BACKLOG`

한화에어로스페이스는 루마니아에 K9 자주포 54문, K10 탄약운반장갑차 36대, 탄약·지원 패키지를 공급하는 10억 달러 계약을 체결했고, 계약기간은 2029년 7월까지다. Reuters는 이 계약 발표 후 주가가 5% 이상 올라 record high를 기록했고, 방산 수주잔고가 2021년 말 5.1조 원에서 2024년 3월 약 30조 원으로 증가했다고 보도했다. ([Reuters][6])

```text
가격경로 1차 판정:
DEFENSE_BACKLOG_ALIGNED_CANDIDATE

좋은 점:
- 정부 고객
- 계약금액 큼
- 계약기간 명확
- K9 + K10 + 탄약·지원 패키지
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

**Loop 5 교정**

```text
DEFENSE_GOVERNMENT_BACKLOG:
Green 가능 유지.

Stage 3 조건:
다년계약
+ 납품스케줄
+ 수주잔고 증가
+ OPM/EPS 상향
+ 자본조달 shock 없음
```

---

## 4-7. Hanwha 유럽 방산 플랫폼화 — `DEFENSE_LOCAL_PRODUCTION_PLATFORM`

한화에어로스페이스는 유럽 육상무기 매출이 2027년까지 두 배가 될 것으로 봤고, 유럽 고객국들이 단순 구매보다 자국 내 생산능력 확보를 선호한다고 설명했다. 폴란드 92억 달러, 루마니아 10억 달러 계약에는 현지생산 조항이 포함되어 있고, land arms backlog는 2020년 3.1조 원에서 2024년 6월 30.3조 원으로 거의 10배 증가했다. ([Reuters][7])

```text
가격경로 1차 판정:
DEFENSE_LOCAL_PRODUCTION_PLATFORM_CANDIDATE

좋은 점:
- 단발 수주가 아니라 지역 플랫폼화
- NATO 재무장
- customer-country manufacturing
- 현지생산으로 정치·조달 안정성 강화
- 다년 매출 visibility

주의:
- 현지공장 CAPEX
- dilution
- 납기 지연
- 현지 고용·원가 구조
- 정치 리스크
```

**Loop 5 교정**

```text
DEFENSE_LOCAL_PRODUCTION_PLATFORM:
단일 수주보다 강한 점:
지역 반복수요와 현지생산 플랫폼.

하지만:
local production CAPEX
+ dilution
+ margin dilution
+ technology transfer condition

을 반드시 같이 본다.
```

---

## 4-8. Hanwha Aerospace 증자 shock — `DEFENSE_CAPITAL_ALLOCATION_SHOCK`

방산 구조가 좋아도 자본배분이 나쁘면 가격경로가 깨진다. 한화에어로스페이스는 3.6조 원 규모 자본조달 계획을 냈고, 금융감독원은 투자자 판단에 필요한 정보가 부족하다며 정정 요구를 했다. 발표 다음 날 주가는 13% 하락했다. ([Reuters][8])

```text
가격경로 1차 판정:
DEFENSE_CAPITAL_ALLOCATION_SHOCK

의미:
좋은 방산 수주잔고
≠ 무조건 Green 유지

감점 조건:
- large_equity_issuance
- dilution
- use_of_proceeds_unclear
- overseas_factory_CAPEX
- regulator_revision_request
```

**Loop 5 교정**

```text
DEFENSE_GOVERNMENT_BACKLOG에는 dilution gate를 붙인다.

수주점수 높음
+ 대규모 증자
+ 목적 불명확
= stage_after_redteam 강등.
```

---

## 4-9. Hyundai Rotem 모로코 철도 수주 — `RAIL_INFRASTRUCTURE`

현대로템은 모로코 국영철도 ONCF로부터 약 2.2조 원, 15.4억 달러 규모 2층 전동차 수주를 확보했다. 이 계약은 현대로템 철도사업 사상 최대 수주로 보도됐다. ([Reuters][9])

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

**Loop 5 교정**

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

## 4-10. 기존 원전 PPA / 재가동 — `NUCLEAR_EXISTING_PPA_RESTART`

기존 원전 PPA는 SMR 테마보다 증거가 훨씬 강하다. Meta는 Constellation의 Illinois Clinton 원전과 20년 전력계약을 맺어 2027년 이후 원전 운영과 재허가를 지원하기로 했다. Clinton plant는 1,121MW 규모이고, 이번 계약은 Big Tech가 AI 데이터센터 전력수요를 장기 무탄소 전력으로 고정하려는 흐름을 보여준다. ([가디언][10])

Constellation은 Microsoft 데이터센터 전력공급을 위해 Three Mile Island 1호기 재가동도 추진하고 있고, 2026년 6~7월 FERC 결정 가능성을 언급했다. 핵심 변수는 Eddystone gas plant의 grid injection rights를 Crane facility로 이전하는 문제다. ([Reuters][11])

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
- 원전별 재허가·grid injection rights
- 재가동 CAPEX
- 지역·규제 리스크
- 한국 원전 기자재로 매핑하려면 직접 계약 필요
```

**Loop 5 교정**

```text
NUCLEAR_EXISTING_PPA_RESTART를 NUCLEAR_SMR_GRID_POLICY와 강하게 분리한다.

기존 원전 PPA:
cash-flow visibility 있음.

SMR:
cost overrun / customer subscription / financing / licensing risk 큼.
```

---

## 4-11. NuScale UAMPS 취소 — `NUCLEAR_SMR_GRID_POLICY`

NuScale의 UAMPS Carbon Free Power Project는 비용 증가와 고객 확보 부족으로 2023년 취소됐다. 당시 프로젝트는 충분한 subscription을 확보하지 못했고, 비용 상승으로 첫 미국 SMR deployment의 경제성이 흔들렸다는 평가가 나왔다. Wired도 DOE 지원에도 불구하고 비용 증가와 고객 확보 실패가 취소의 핵심이었다고 정리했다. ([WIRED][12])

```text
가격경로 1차 판정:
SMR_COST_OVERRUN_HARD_4C

교훈:
SMR 정책 뉴스
≠ 기존 원전 PPA
≠ Green

4C 조건:
- cost_overrun
- customer_subscription_failure
- financing_failure
- project_cancelled
- staff_reduction
```

**Loop 5 교정**

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

## 4-12. Hanwha–Vatn 수중 드론 — `DEFENSE_UNMANNED_NAVAL_SYSTEMS`

한화는 미국 방산 스타트업 Vatn Systems와 협력해 미 해군용 autonomous underwater drones를 공동 개발하기로 했다. Vatn은 Pentagon contracts를 확보했고, Hanwha는 잠수함·해양 플랫폼 역량을 결합할 수 있다. 다만 이 단계는 **prototype/partnership option**이지, 양산·납품·마진이 확인된 방산 backlog가 아니다. ([Reuters][13])

```text
가격경로 1차 판정:
DEFENSE_UNMANNED_NAVAL_SYSTEMS_OPTION

좋은 점:
- 미 해군 무인화 수요
- 저가 수중 드론 concept
- autonomous naval system theme
- Hanwha의 해양·조선 역량과 결합 가능

주의:
- 스타트업 단계
- 실제 양산계약 전
- 기술·규제·작전검증 필요
- 매출화 전 Green 금지
```

**Loop 5 교정**

```text
DEFENSE_UNMANNED_NAVAL_SYSTEMS:
prototype / partnership = Stage 1.
Pentagon production contract + delivery schedule + margin = Stage 2~3 후보.
```

---

# 5. 반례 / RedTeam

## 5-1. 데이터센터 project delay / local opposition

```text
4C-watch:
local_opposition
water_permitting_delay
grid_interconnection_delay
moratorium
noise_pollution
project_withdrawal
```

Perth의 120MW 데이터센터 철회, Seattle·Indianapolis의 moratorium 논의는 AI 데이터센터 수요가 전력장비 수주로 자동 연결되지 않는다는 기준이다. ([가디언][5])

---

## 5-2. 방산 dilution / capital allocation shock

```text
4C-watch:
large_equity_issuance
dilution
use_of_proceeds_unclear
regulator_revision_request
overseas_factory_CAPEX_burden
```

한화에어로스페이스 유상증자 사례는 수주잔고가 좋아도 capital allocation이 나쁘면 가격경로가 깨진다는 기준이다. ([Reuters][8])

---

## 5-3. SMR project cancellation

```text
4C:
cost_overrun
customer_subscription_failure
financing_failure
project_cancelled
staff_reduction
```

NuScale UAMPS 취소는 SMR archetype에서 hard counterexample이다. ([WIRED][12])

---

## 5-4. 철도 project margin / financing risk

```text
4C-watch:
project_financing_delay
low_margin_contract
delivery_delay
warranty_cost
FX_cost
```

현대로템 모로코 수주는 대형 계약이지만, 철도는 계약금액과 실제 이익률이 다를 수 있어 margin과 납품 스케줄을 반드시 분리해야 한다. ([Reuters][9])

---

## 5-5. 전력설비 CAPA 정상화 / input-cost squeeze

```text
4C-watch:
transformer_capacity_normalization
medium_voltage_capacity_expansion
copper_cost_spike
GOES_shortage
tariff_cost
low_margin_long_term_contract
```

변압기와 중전압 장비는 지금 병목이 강하지만, Hitachi Energy·Siemens·ABB 등 대형 업체들이 CAPA를 늘리고 있다. 병목이 완화되는 시점에는 신규수주 증가율과 가격전가력이 둔화될 수 있다. ([Reuters][1])

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

변압기 쇼티지는 강한 구조증거지만, ABB처럼 대규모 CAPA 증설이 시작되고, 데이터센터 moratorium·지역반발이 늘면 신규수주 증가율과 valuation을 같이 봐야 한다. ([Reuters][1])

---

## 6-2. AI 전력장비 / gas turbine 4B-watch

```text
4B 조건:
- GE Vernova류 power equipment backlog가 시장에 모두 알려짐
- AI 전력망 narrative로 valuation이 먼저 감
- wind segment 손실·tariff cost를 시장이 무시
- data-center project delay를 반영하지 않음
```

GE Vernova는 orders/backlog/guidance가 실제로 좋아 주가도 급등했지만, 풍력 손실과 tariff cost가 동시에 남아 있다. ([Reuters][3])

---

## 6-3. 방산 4B-watch

```text
4B 조건:
- K방산 수출 narrative를 모두가 인정
- NATO 재무장 기대 과밀
- 목표가 상향 집중
- 현지생산·유상증자·CAPEX를 시장이 낮게 봄
- 수출허가·정치 리스크 무시
```

루마니아 K9 계약과 유럽 매출 전망은 성공 후보지만, 한화에어로스페이스의 증자 shock은 방산에도 4B/4C 감시가 필요하다는 증거다. ([Reuters][6])

---

## 6-4. 철도·인프라 대형수주 4B-watch

```text
4B 조건:
- 대형 해외 철도 계약 뉴스로 관련주 급등
- 계약금액만 보고 마진·warranty·납기·financing 무시
- 실제 OP/EPS 전환 전 가격이 먼저 감
```

현대로템의 모로코 수주는 Stage 2 후보지만, 계약마진과 납품 스케줄, financing을 확인해야 한다. ([Reuters][9])

---

## 6-5. 원전 4B-watch

```text
4B 조건:
- Big Tech nuclear PPA 뉴스로 원전 관련주 동반 과열
- 기존 원전 PPA와 SMR 테마를 섞음
- SMR 비용초과·고객확보 실패 리스크 무시
```

Meta–Constellation PPA와 Microsoft–Three Mile Island 재가동 논의는 기존 원전에는 강한 구조증거지만, NuScale UAMPS 취소는 SMR 실행 리스크를 보여준다. ([가디언][10])

---

## 6-6. 무인 해양 방산 4B-watch

```text
4B 조건:
- underwater drone, autonomous naval system narrative로 방산·조선 관련주 과열
- Pentagon contract가 스타트업에 있다는 사실을 한화 매출로 과잉 매핑
- 양산계약·delivery schedule·margin 확인 전 가격이 먼저 감
```

Hanwha–Vatn은 좋은 option이지만, production contract와 delivery schedule 전까지 Stage 3-Green은 막아야 한다. ([Reuters][13])

---

# 7. 4C-thesis-break 사례

## 7-1. 전력설비 프로젝트 지연

```text
4C-watch:
data_center_project_withdrawal
moratorium
grid_interconnection_delay
water_permitting_delay
local_opposition
utility_cost_pushback
```

R1 전력설비는 AI 데이터센터 수요 덕분에 강하지만, 데이터센터 자체가 멈추면 변압기·switchgear·PDU 수주 timing도 밀린다. ([가디언][5])

---

## 7-2. 방산 자본배분 shock

```text
4C-watch:
share_issuance_amount_large
dilution_flag
regulator_revision_request
use_of_proceeds_unclear
local_factory_capex_flag
```

한화에어로스페이스의 3.6조 원 증자 정정 요구와 주가 -13% 반응은 “좋은 backlog + 나쁜 자본배분”이 같이 나올 수 있음을 보여준다. ([Reuters][8])

---

## 7-3. SMR false-green

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

## 7-4. 철도 대형계약 margin failure

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

## 7-5. 기존 원전 PPA execution risk

```text
4C-watch:
relicensing_failure
grid_injection_rights_failure
restart_capex_overrun
regulatory_delay
PPA_economics_dispute
```

기존 원전 PPA는 SMR보다 증거가 강하지만, Three Mile Island 재가동처럼 grid injection rights와 FERC 결정이 핵심 gate가 될 수 있다. ([Reuters][11])

---

# 8. 점수비중 보정표 — R1 Loop 5 / v5.0

| canonical archetype                   | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | Loop 5 핵심 감점                                 |
| ------------------------------------- | ------: | ---------: | ---------: | ---------: | --------: | ------: | ---: | -------------------------------------------- |
| `GRID_TRANSFORMER_SHORTAGE`           |      24 |         25 |         24 |         12 |        10 |       1 |    5 | CAPA 정상화, 데이터센터 지연, 저마진 장기계약                 |
| `GRID_MEDIUM_VOLTAGE_EXPANSION`       |      22 |         23 |         20 |         12 |        10 |       1 |    5 | CAPA 증설 후 가격정상화, 제품 mix                      |
| `GRID_SUPPLY_SLOT_PREBUY`             |      22 |         24 |         22 |         12 |        10 |       1 |    5 | 선점 슬롯 취소, 고객 프로젝트 지연                         |
| `AI_DATA_CENTER_POWER_EQUIPMENT`      |      22 |         23 |         19 |         13 |        10 |       0 |    5 | project delay, valuation crowding, orders 둔화 |
| `GAS_TURBINE_POWER_BACKLOG`           |      21 |         22 |         18 |         12 |        10 |       0 |    5 | turbine slot, tariff, wind drag, CAPEX       |
| `CONTRACT_BACKLOG_INDUSTRIAL`         |      20 |         24 |         18 |         13 |        12 |       1 |    5 | 계약질 불명확, 납기, 마진                              |
| `DEFENSE_GOVERNMENT_BACKLOG`          |      21 |         24 |         17 |         14 |        14 |       3 |    5 | 납기, 수출허가, 현지생산 CAPEX, dilution               |
| `DEFENSE_LOCAL_PRODUCTION_PLATFORM`   |      21 |         23 |         16 |         14 |        13 |       2 |    5 | 현지공장 CAPEX, margin dilution, 정치 리스크          |
| `DEFENSE_CAPITAL_ALLOCATION_SHOCK`    |    gate |       gate |       gate |       gate |      gate |    gate | gate | 대규모 증자, 목적 불명확, FSS 정정요구                     |
| `DEFENSE_UNMANNED_NAVAL_SYSTEMS`      |      16 |         15 |         12 |         13 |         9 |       0 |    5 | prototype, 양산계약 부재, 기술검증                     |
| `SHIPBUILDING_OFFSHORE_BACKLOG`       |      21 |         22 |         18 |         13 |        13 |       1 |    5 | 저가수주, 후판가, 인건비, 납기                           |
| `SHIPBUILDING_NAVAL_MRO`              |      16 |         17 |         11 |         13 |        10 |       1 |    5 | 저마진 MRO, 미국 법적 제한, 중국 제재, CAPEX              |
| `RAIL_INFRASTRUCTURE`                 |      20 |         22 |         12 |         14 |        11 |       1 |    5 | 납기, 마진, financing, warranty                  |
| `NUCLEAR_EXISTING_PPA_RESTART`        |      19 |         23 |         13 |         14 |        12 |       2 |    5 | 재허가, grid rights, 재가동 CAPEX                  |
| `NUCLEAR_SMR_GRID_POLICY`             |      13 |         12 |         10 |         13 |         7 |       1 |    5 | 비용초과, 고객확보 실패, 허가, 취소                        |
| `GEOPOLITICAL_RECONSTRUCTION`         |      10 |          8 |          8 |         10 |         7 |       0 |    4 | 실제 계약 없음, financing 없음                       |
| `DATA_CENTER_GRID_PERMITTING_OVERLAY` |    gate |       gate |       gate |       gate |      gate |    gate | gate | 지역반발·수자원·전력망·moratorium                      |
| `CAPITAL_ALLOCATION_DILUTION_OVERLAY` |    gate |       gate |       gate |       gate |      gate |    gate | gate | 유상증자, CAPEX 부담, 목적 불명확                       |
| `DISCLOSURE_CONFIDENCE_CAP`           |     cap |        cap |        cap |        cap |       cap |     cap |    + | 계약금액·기간·상대방·마진 미공개                           |

Loop 5에서 가장 크게 바뀐 건 다섯 가지다.

```text
1. GRID_SUPPLY_SLOT_PREBUY를 추가.
   변압기 병목에서 단순 수요가 아니라 생산 슬롯 선점까지 나타났기 때문.

2. GAS_TURBINE_POWER_BACKLOG를 AI_DATA_CENTER_POWER_EQUIPMENT에서 분리.
   GE Vernova처럼 turbine backlog와 electrification backlog는 좋지만 wind drag와 tariff cost를 따로 본다.

3. DEFENSE_LOCAL_PRODUCTION_PLATFORM은 유지하되 CAPEX/dilution 감점을 강화.
   현지생산은 수주 visibility를 높이지만 자본조달 shock도 만든다.

4. NUCLEAR_EXISTING_PPA_RESTART와 NUCLEAR_SMR_GRID_POLICY는 더 강하게 분리.
   기존 원전 PPA·재가동은 cash-flow evidence가 있고, SMR은 cost/subscription risk가 크다.

5. DISCLOSURE_CONFIDENCE_CAP를 R1 전반에 적용.
   OpenDART detail에서 계약금액·기간·상대방·마진을 못 확인하면 Stage 3-Green을 제한한다.
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

## `GRID_SUPPLY_SLOT_PREBUY`

```text
Stage 1:
lead time 장기화와 production slot 선점 보도

Stage 2:
개별 기업의 slot-based long-term agreement, prepayment, 생산배정 확인

Stage 3:
slot 선점이 매출·마진·수주잔고로 전환되는 날

Stage 4B:
공급 슬롯 narrative가 valuation에 과도하게 반영

Stage 4C:
고객 프로젝트 지연, 슬롯 취소, CAPA 증설로 slot premium 축소
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

## `DEFENSE_LOCAL_PRODUCTION_PLATFORM`

```text
Stage 1:
고객국 현지생산 요구, local content, 생산거점 발표

Stage 2:
현지공장 착공, 납품 batch, 장기계약, 고객국 추가수요 확인일

Stage 3:
현지생산이 반복 매출과 OPM으로 전환되는 날

Stage 4B:
현지생산 platform narrative가 과도하게 반영된 날

Stage 4C:
CAPEX 부담, margin dilution, 현지 정치 리스크, 증자 shock
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

## R1 Loop 5 공통 검증 방식

```text
1. 각 case의 stage1_date, stage2_date, stage3_date를 지정한다.
2. 해당 날짜의 종가를 stage_price로 저장한다.
3. MFE_30D / 90D / 180D / 1Y / 2Y를 계산한다.
4. MAE_30D / 90D / 180D / 1Y를 계산한다.
5. peak_price와 drawdown_after_peak를 계산한다.
6. 계약금액, 계약기간, 납품스케줄, 수주잔고, OP/EPS revision,
   마진 변화와 가격경로를 비교한다.
```

## Loop 5에서 새로 강제할 판정

```text
GRID_BOTTLENECK_STRUCTURAL:
리드타임·가격·수입·CAPA 병목이 동시에 확인.

GRID_SLOT_VISIBILITY:
생산 슬롯 선점·장기계약·선수금이 확인되어 multi-year visibility가 생김.

MEDIUM_VOLTAGE_EXPANSION_ALIGNED:
중전압 장비 수요와 CAPA 확대가 실제 수주·OPM으로 연결.

POWER_EQUIPMENT_BACKLOG_ALIGNED:
AI 전력수요가 equipment backlog, guidance, EPS로 연결.

BACKLOG_WITHOUT_MARGIN:
수주잔고는 늘었지만 마진·EPS가 불명확.

DATA_CENTER_POWER_4B:
orders/backlog는 강하지만 이미 valuation이 과열.

PROJECT_DELAY_RISK:
수요는 강하지만 데이터센터·철도·원전 프로젝트 지연 가능성.

DEFENSE_LOCAL_PRODUCTION_PLATFORM:
단일 수출을 넘어 고객국 현지생산과 반복수요로 확장.

CAPITAL_ALLOCATION_SHOCK:
수주형 기업이 유상증자·대규모 CAPEX로 주주가치를 희석.

NAVAL_MRO_OPTION_ONLY:
MRO 자격·초기계약은 있지만 고마진 반복매출이나 신조 전환 미확인.

EXISTING_NUCLEAR_PPA_RESTART_ALIGNED:
기존 원전 장기 PPA·재가동이 FCF visibility로 연결.

SMR_POLICY_FALSE_GREEN:
SMR 정책·테마는 있으나 비용·고객·허가·financing 미확인.

POLICY_TO_CONTRACT_FAILED:
재건·네옴·철도·원전 정책 뉴스가 실제 계약으로 연결되지 않음.

DISCLOSURE_CONFIDENCE_CAPPED:
계약금액·기간·상대방·마진이 detail에서 확인되지 않아 Stage 3 제한.
```

## 이번 R1 Loop 5에서 우선 검증할 가격 case

| case_id                                            | stage2 후보일 | 현재 1차 가격판정                               |
| -------------------------------------------------- | ---------: | ---------------------------------------- |
| `us_transformer_shortage_import_slots_case`        | 2026-05-11 | 구조적 전력망 병목 reference                     |
| `ls_electric_525kv_us_datacenter_transformer_case` |    2025-11 | 한국 EHV transformer direct mapping 후보     |
| `abb_medium_voltage_expansion_case`                | 2026-05-11 | 중전압 장비 CAPA 확대 reference                 |
| `ge_vernova_data_center_orders_case`               | 2026-04-22 | AI power equipment aligned + 4B-watch    |
| `ge_vernova_power_backlog_turbine_case`            | 2026-01~04 | turbine/storage/power backlog candidate  |
| `us_power_demand_record_eia_case`                  | 2026-05-12 | macro tailwind, company Green 아님         |
| `perth_data_center_withdrawal_case`                | 2026-05-15 | data center project delay overlay        |
| `seattle_indianapolis_data_center_moratorium_case` | 2026-05-15 | moratorium / local opposition overlay    |
| `hanwha_aerospace_romania_k9_case`                 | 2024-07-09 | +5% record high, defense backlog aligned |
| `hanwha_aerospace_europe_sales_visibility_case`    | 2024-10-07 | local production platform candidate      |
| `hanwha_aerospace_dilution_case`                   | 2025-03-27 | -13%, capital allocation shock           |
| `hyundai_rotem_morocco_rail_case`                  | 2025-02-26 | 2.2조 원 철도 Stage 2 후보                     |
| `meta_constellation_existing_nuclear_ppa_case`     | 2025-06-03 | 기존 원전 PPA reference                      |
| `constellation_tmi_microsoft_restart_case`         | 2026-05-11 | 원전 재가동 + Microsoft power demand          |
| `nuscale_uamps_smr_cancel_case`                    |    2023-11 | SMR hard 4C                              |
| `hanwha_vatn_underwater_drone_case`                |    2025-12 | unmanned naval system option             |
| `ukraine_reconstruction_policy_case`               |        계약별 | actual contract before Green             |
| `neom_city_policy_case`                            |        계약별 | actual contract before Green             |

---

# 11. 다음에 에이전트가 채워야 할 price fields

R1 Loop 5에서는 아래 필드를 채우게 해야 한다.

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
transformer_voltage_kv
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
project_delay_flag
local_opposition_flag
moratorium_flag
water_permitting_delay_flag
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

unmanned_system_contract_flag
prototype_flag
pentagon_contract_flag
production_contract_flag
autonomous_naval_system_flag

ship_newbuilding_price_index
low_margin_backlog_flag
steel_plate_cost_change
labor_cost_change
naval_mro_contract_flag
msra_flag
naval_newbuild_license_flag
mro_margin_signal
geopolitical_sanction_flag

rail_contract_value
rail_delivery_schedule
rail_warranty_risk
rail_financing_secured_flag
rail_fx_risk

nuclear_ppa_flag
ppa_duration_years
plant_capacity_mw
relicensing_support_flag
nuclear_restart_flag
grid_injection_rights_flag
restart_capex_amount
ferc_approval_flag

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

# R1 Loop 5 결론

이번 5회차에서 R1은 더 좁혀졌다.

```text
강한 Green 후보:
초고압 변압기·전력설비 병목
생산 슬롯 선점이 확인되는 전력장비
중전압 장비·switchgear 확장
AI 데이터센터 전력장비 중 orders/backlog/guidance가 확인된 기업
정부고객 다년계약 방산
고마진 조선 수주
기존 원전 장기 PPA·재가동

Watch-to-Green:
철도 대형계약
조선 MRO
방산 현지생산 플랫폼
방산 무인 해양시스템
원전 기자재
산업재 장기계약
스마트팩토리 자동화

Event/Watch:
우크라 재건
네옴시티
정책형 인프라
SMR 정책 테마
미 해군 MRO option
무인 해양시스템 partnership

Hard 4C:
데이터센터 project delay / moratorium / 지역반발
방산 dilution
SMR 비용초과·고객확보 실패
조선 MRO 과대평가·중국 제재
철도 financing·마진 리스크
기존 원전 grid injection rights 실패
재건·네옴 실제 계약 부재
계약 detail 부족으로 인한 disclosure confidence cap
```

**R1 Loop 5 점수정규화의 핵심 문장:**

> 산업재·수주·인프라는 “수주가 있다”가 아니라 **계약금액, 계약기간, 거래상대방, 납품스케줄, 수주잔고 질, 마진, OP/EPS 상향, FCF 전환, 가격경로 리레이팅**이 같이 있어야 Green이다.
> Loop 5부터는 특히 `grid_supply_slot_prebuy`, `gas_turbine_power_backlog`, `data_center_grid_permitting`, `defense_capital_allocation_shock`, `local_production_margin_dilution`, `SMR_policy_false_green`, `disclosure_confidence_cap`을 강한 보정축으로 넣어야 한다.

다음 순서는 **R2 — AI·반도체·전자부품 Loop 5**다.

[1]: https://www.reuters.com/business/energy/us-power-transformer-buyers-scramble-imports-factory-slots--reeii-2026-05-11/?utm_source=chatgpt.com "US power transformer buyers scramble for imports, factory slots"
[2]: https://www.reuters.com/sustainability/boards-policy-regulation/abb-invest-200-million-medium-voltage-equipment-production-europe-2026-05-11/?utm_source=chatgpt.com "ABB to invest $200 million in medium-voltage equipment production in Europe"
[3]: https://www.reuters.com/business/energy/ge-vernova-lifts-annual-revenue-forecast-data-center-demand-2026-04-22/?utm_source=chatgpt.com "GE Vernova lifts 2026 outlook as AI boom fuels power equipment demand"
[4]: https://www.reuters.com/business/energy/us-power-use-beat-record-highs-2026-2027-ai-use-surges-eia-says-2026-05-12/?utm_source=chatgpt.com "US power use to beat record highs in 2026 and 2027 as AI use surges, EIA says"
[5]: https://www.theguardian.com/technology/2026/may/15/developer-withdraws-plans-for-perth-datacentre-after-fierce-community-opposition?utm_source=chatgpt.com "Developer withdraws plans for Perth datacentre after fierce community opposition"
[6]: https://www.reuters.com/business/aerospace-defense/south-koreas-hanwha-aerospace-wins-1-bln-order-romania-k9-howitzers-2024-07-09/?utm_source=chatgpt.com "South Korea's Hanwha Aerospace wins $1 bln order from Romania for self-propelled howitzers"
[7]: https://www.reuters.com/business/aerospace-defense/hanwha-aerospaces-europe-land-arms-sales-double-by-2027-ceo-says-2024-10-07/?utm_source=chatgpt.com "Hanwha Aerospace's Europe land arms sales to double by 2027, CEO says"
[8]: https://www.reuters.com/business/aerospace-defense/south-korea-market-watchdog-orders-hanwha-aerospace-revise-share-issuance-plan-2025-03-27/?utm_source=chatgpt.com "S. Korea watchdog blocks Hanwha Aerospace $2.5 billion capital raising plan"
[9]: https://www.reuters.com/markets/deals/hyundai-rotem-wins-15-billion-order-moroccos-national-rail-operator-2025-02-26/?utm_source=chatgpt.com "Hyundai Rotem wins $1.5 billion order from Morocco's national rail operator"
[10]: https://www.theguardian.com/technology/2025/jun/03/meta-nuclear-power-ai?utm_source=chatgpt.com "Meta signs deal with nuclear plant to power AI and datacenters for 20 years"
[11]: https://www.reuters.com/business/energy/us-may-decide-three-mile-island-restart-june-constellation-execs-say-2026-05-11/?utm_source=chatgpt.com "US may decide on Three Mile Island restart in June, Constellation execs say"
[12]: https://www.wired.com/story/first-small-scale-nuclear-plant-us-nuscale-canceled?utm_source=chatgpt.com "The First Small-Scale Nuclear Plant in the US Died Before It Could Live"
[13]: https://www.reuters.com/business/aerospace-defense/south-koreas-hanwha-us-defense-startup-vatn-build-underwater-drones-2025-12-10/?utm_source=chatgpt.com "South Korea's Hanwha, US defense startup Vatn to build underwater drones"

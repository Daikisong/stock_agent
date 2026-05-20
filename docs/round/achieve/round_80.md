좋아. **R13 Loop 3까지 끝났으니, 규칙대로 다시 R1로 돌아와서 이번은 R1 Loop 4 — 산업재·수주·인프라**다.

이번 Loop 4는 R1을 한 번 더 날카롭게 깎는다. R1은 전력설비, 전선·케이블, 피팅밸브, 조선, 조선 기자재, 방산, 원전, 철도, 건설기계, 우크라 재건, 네옴시티를 품는 대섹터이고, Theme Tag Map에서도 “수주 뉴스만으로는 부족하고 계약질 + 마진 + EPS 상향 + 주가 리레이팅이 같이 가야 한다”고 정리돼 있다.

Checkpoint 20 원칙도 그대로 적용한다. 단일판매·공급계약, 신규시설투자, 유상증자, 계약 해지·취소·정정 같은 공시는 list만 보면 오판이 생기므로 detail에서 계약금액, 계약기간, 매출 대비 계약금액, 거래상대방, OP YoY, dilution 등을 실제 확인해야 한다. 없는 값은 절대 만들면 안 된다.

서생원식으로 보면 R1의 질문은 “수주가 많나?”가 아니라 **수주와 병목이 EPS/FCF 체급 변화로 이어지고, 시장이 아직 과거 시클리컬 프레임으로 낮게 보고 있는가**다.

---

# R1 Loop 4. 산업재·수주·인프라

## 1. 이번 라운드 대섹터

```text
R1 = 산업재·수주·인프라
Loop 4 목표 = 전력설비·방산·조선·철도·원전·재건 중
“수주가 실제 EPS/FCF로 전환되는 케이스”와
“정책/테마/저마진/증자/프로젝트 지연 케이스”를 더 강하게 분리
```

이번 회차의 핵심 질문은 이거다.

```text
이 수주는 이익 체급을 바꾸는 수주인가?
아니면 뉴스성 수주, 정책 수주, 저마진 경험 수주, 프로젝트 지연, CAPEX 부담, dilution인가?
```

R1에서 가장 위험한 오판은 여전히 이거다.

```text
수주잔고 증가
= 무조건 Green
```

Loop 4부터는 이렇게 본다.

```text
좋은 수주:
계약금액 큼
계약기간 김
납품 스케줄 명확
매출 대비 계약금액 큼
고객 신용도 높음
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

| canonical archetype                   | Loop 4 정책                                               |
| ------------------------------------- | ------------------------------------------------------- |
| `GRID_TRANSFORMER_SHORTAGE`           | R1 최상위 Green 후보. 리드타임·가격·계약·CAPA 확인                     |
| `GRID_MEDIUM_VOLTAGE_EXPANSION`       | Watch-to-Green. 변압기뿐 아니라 중전압 장비 CAPA 증설 확인              |
| `AI_DATA_CENTER_POWER_EQUIPMENT`      | Green 가능. orders/backlog/guidance와 project delay를 같이 확인 |
| `CONTRACT_BACKLOG_INDUSTRIAL`         | Green 가능. 계약질·마진·EPS 전환 필수                              |
| `DEFENSE_GOVERNMENT_BACKLOG`          | Green 가능. 정부고객·다년계약·납품스케줄 핵심                            |
| `DEFENSE_LOCAL_PRODUCTION_PLATFORM`   | Watch-to-Green. 현지생산은 visibility와 CAPEX/dilution을 동시에 봄 |
| `DEFENSE_CAPITAL_ALLOCATION_SHOCK`    | RedTeam gate. 대규모 증자·목적 불명확 CAPEX는 Stage 강등             |
| `DEFENSE_UNMANNED_NAVAL_SYSTEMS`      | Watch. 실제 국방계약·양산·납품 전 Green 제한                         |
| `SHIPBUILDING_OFFSHORE_BACKLOG`       | Green 가능. 선가·저가수주 소진·후판가·인도마진 확인                        |
| `SHIPBUILDING_NAVAL_MRO`              | Watch-to-Green. MRO 경험은 좋지만 신조/고마진 전환 필요                |
| `RAIL_INFRASTRUCTURE`                 | Watch-to-Green. 대형계약은 좋지만 마진·financing·납품스케줄 확인         |
| `NUCLEAR_EXISTING_PPA_RESTART`        | Watch-to-Green. 기존 원전 PPA·재가동·재허가가 SMR보다 증거 강함          |
| `NUCLEAR_SMR_GRID_POLICY`             | Watch/Red. 비용초과·고객확보 실패·허가 리스크                          |
| `GEOPOLITICAL_RECONSTRUCTION`         | Event/Watch. 실제 수주·financing 전 Green 금지                 |
| `DATA_CENTER_GRID_PERMITTING_OVERLAY` | RedTeam overlay. 데이터센터·전력망 지역반발·수자원·인허가 지연              |
| `CAPITAL_ALLOCATION_DILUTION_OVERLAY` | RedTeam gate. 유상증자·CAPEX 부담·목적 불명확                      |

---

## 3. deep sub-archetype

```text
GRID_TRANSFORMER_SHORTAGE
- 초고압 변압기
- GSU transformer
- substation transformer
- transformer lead time
- transformer price increase
- factory slot pre-buying
- 한국·튀르키예 수입
- grid modernization

GRID_MEDIUM_VOLTAGE_EXPANSION
- 중전압 장비
- switchgear
- substation automation
- medium-voltage product line
- utility demand
- data center electrification
- EV / heating electrification
- factory capacity expansion

AI_DATA_CENTER_POWER_EQUIPMENT
- 데이터센터 전력장비
- gas turbine
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

미국 전력망은 데이터센터, EV, 공장, 재생에너지 프로젝트 때문에 변압기 병목이 심해졌다. GSU 변압기 수요는 2019년 이후 274%, 변전소용 power transformer 수요는 116% 늘었고, 대형 변압기 리드타임은 최대 4년, 가격은 5년 동안 약 80% 상승했다. 미국 개발사들은 한국·튀르키예 수입, 생산 슬롯 선점, 노후 장비 재활용까지 동원하고 있다. ([Reuters][1])

```text
가격경로 1차 판정:
GRID_BOTTLENECK_STRUCTURAL_REFERENCE

좋은 점:
- 수요 증가율 명확
- 리드타임 장기화
- 가격 상승
- 한국 업체 수출 기회
- 데이터센터·EV·재생에너지·공장 수요가 동시에 작동

주의:
- CAPA 증설 후 병목 정상화 가능성
- 데이터센터 project delay
- 구리·철강·관세 원가
- 저마진 장기계약 가능성
```

**Loop 4 교정**

```text
GRID_TRANSFORMER_SHORTAGE는 R1 최상위 Green 후보 유지.

다만 Stage 3 조건을 더 엄격하게 한다:
계약금액
계약기간
납품시기
매출 대비 계약금액
OP/EPS 상향
수주잔고 증가
마진 개선
```

---

## 4-2. ABB 중전압 장비 투자 — `GRID_MEDIUM_VOLTAGE_EXPANSION`

전력설비 병목은 초고압 변압기만이 아니다. ABB는 유럽 중전압 장비 생산 확대를 위해 3년간 2억 달러를 투자하기로 했고, 이 투자로 제품군에 따라 생산능력이 50~300% 늘 수 있다고 밝혔다. 수요 배경은 데이터센터, EV, 난방 전기화, 산업 onshoring, 전력망 운영자 수요다. ([Reuters][2])

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

**Loop 4 교정**

```text
GRID_MEDIUM_VOLTAGE_EXPANSION을 GRID_TRANSFORMER_SHORTAGE의 하위축으로 추가.

전력설비 scoring은:
초고압 변압기
+ 중전압 장비
+ switchgear
+ PDU/UPS
+ grid automation

으로 확장하되, CAPA 정상화 flag를 같이 둔다.
```

---

## 4-3. GE Vernova — `AI_DATA_CENTER_POWER_EQUIPMENT`

GE Vernova는 AI 데이터센터 전력장비 수요가 실제 orders/backlog/guidance로 연결된 사례다. 2026년 매출 전망을 445억~455억 달러로 올렸고, backlog는 1,630억 달러까지 늘었다. 전력·전기화 부문 이익이 크게 개선됐고, 회사는 2027년까지 backlog 2,000억 달러 달성을 기대한다고 밝혔다. 다만 풍력 부문은 계속 부진하고, 2026년 tariff cost도 2.5억~3.5억 달러로 예상된다. ([Reuters][3])

```text
가격경로 1차 판정:
AI_DATA_CENTER_POWER_EQUIPMENT_ALIGNED + 4B_WATCH

좋은 점:
- AI 데이터센터 전력수요가 orders/backlog로 확인
- 매출·마진 전망 상향
- backlog 증가
- 전력·전기화 부문 이익 개선

주의:
- 이미 주가가 강하게 반영된 4B 가능성
- 풍력 부문 손실
- tariff cost
- 데이터센터 project delay
```

**Loop 4 교정**

```text
AI_DATA_CENTER_POWER_EQUIPMENT:
Stage 2까지는 orders/backlog/guidance로 가능.
Stage 3는 EPS/FCF 전환과 valuation frame 변화까지 확인.
이미 급등한 경우 SECTOR_SUCCESS_BUT_4B_WATCH로 분리.
```

---

## 4-4. 데이터센터 지역반발 — 전력설비 수요의 soft 4C

전력설비 수요는 구조적으로 강하지만, 데이터센터 프로젝트 자체가 지연되면 전력장비 신규수주 속도도 둔화될 수 있다. Perth 인근 120MW 데이터센터 계획은 1,900건에 가까운 반대 의견과 문화·환경 민감지역, 학교·주거지 인접, 비상 디젤 발전기 소음 우려 때문에 철회됐다. ([Guardian][4])

Seattle과 Indianapolis에서도 대형 데이터센터 moratorium 또는 규제 논의가 진행되고 있으며, 에너지 사용·환경영향·전기요금 상승·소음·utility strain이 핵심 쟁점으로 거론된다. ([Axios][5])

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

**Loop 4 교정**

```text
전력설비 Green 후보에도 DATA_CENTER_GRID_PERMITTING_OVERLAY를 붙인다.

수요 강함:
가점

프로젝트 인허가·지역반발:
납품시기/신규수주 지연 감점
```

---

## 4-5. Hanwha Aerospace 루마니아 K9 계약 — `DEFENSE_GOVERNMENT_BACKLOG`

한화에어로스페이스는 루마니아에 K9 자주포 54문, K10 탄약운반장갑차 36대, 탄약·지원 패키지를 공급하는 10억 달러 계약을 체결했고, 계약기간은 2029년 7월까지다. 계약 발표 후 주가는 5% 이상 올라 record high를 기록했고, 방산 수주잔고는 2021년 말 5.1조 원에서 2024년 3월 약 30조 원으로 증가했다. ([Reuters][6])

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

**Loop 4 교정**

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

## 4-6. 한화 유럽 방산 플랫폼화 — `DEFENSE_LOCAL_PRODUCTION_PLATFORM`

한화에어로스페이스는 유럽 육상무기 매출이 2027년까지 두 배가 될 것으로 봤고, 폴란드 92억 달러, 루마니아 10억 달러 계약과 현지생산 선호가 배경이다. CEO는 유럽 국가들이 단순 구매보다 자국 내 생산능력 확보를 선호한다고 설명했고, 육상무기 수주잔고는 2020년 이후 10배 증가했다. ([Reuters][7])

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

**Loop 4 교정**

```text
DEFENSE_LOCAL_PRODUCTION_PLATFORM을 추가한다.

단일 수주보다 강한 점:
지역 반복수요와 현지생산 플랫폼.

하지만:
local production CAPEX
+ dilution
+ margin dilution

을 반드시 같이 본다.
```

---

## 4-7. 한화에어로스페이스 증자 shock — `DEFENSE_CAPITAL_ALLOCATION_SHOCK`

방산 구조가 좋아도 자본배분이 나쁘면 가격경로가 깨진다. 한화에어로스페이스는 해외 생산 확대와 기술 개발을 위해 3.6조 원 규모 자본조달 계획을 냈고, 금융감독원은 투자자 판단에 필요한 정보가 부족하다며 정정 요구를 했다. 이 뉴스 이후 주가는 13% 하락했다. ([Reuters][8])

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

**Loop 4 교정**

```text
DEFENSE_GOVERNMENT_BACKLOG에는 dilution gate를 붙인다.

수주점수 높음
+ 대규모 증자
+ 목적 불명확
= stage_after_redteam 강등.
```

---

## 4-8. 현대 로템 모로코 철도 수주 — `RAIL_INFRASTRUCTURE`

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

**Loop 4 교정**

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

## 4-9. 기존 원전 PPA / 재가동 — `NUCLEAR_EXISTING_PPA_RESTART`

기존 원전 PPA는 SMR 테마보다 증거가 훨씬 강하다. Meta는 Constellation의 Illinois Clinton 원전과 20년 전력계약을 맺어 2027년 이후 원전 운영과 재허가를 지원하기로 했다. Clinton plant는 1,121MW 규모이고, 이번 계약은 Big Tech가 AI 데이터센터 전력수요를 장기 무탄소 전력으로 고정하려는 흐름을 보여준다. ([Reuters][10])

Constellation은 또 Microsoft 데이터센터 전력공급을 위해 Three Mile Island 1호기 재가동을 추진하고 있고, 2026년 6~7월 FERC 결정 가능성을 언급했다. 이 경우 완전히 닫힌 원전을 되살리는 전례 없는 재가동 케이스가 된다. ([Reuters][11])

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

**Loop 4 교정**

```text
NUCLEAR_EXISTING_PPA_RESTART를 NUCLEAR_SMR_GRID_POLICY와 분리한다.

기존 원전 PPA:
cash-flow visibility 있음.

SMR:
cost overrun / customer subscription / financing / licensing risk 큼.
```

---

# 5. 반례

## 5-1. NuScale UAMPS 취소 — `NUCLEAR_SMR_GRID_POLICY`

NuScale의 UAMPS Carbon Free Power Project는 비용 증가와 고객 확보 부족으로 2023년 취소됐다. 프로젝트 비용은 2020년 36억 달러에서 2023년 93억 달러로 늘었고, 고객 subscription을 충분히 확보하지 못해 UAMPS와 NuScale이 취소를 결정했다. 취소 후 NuScale은 인력 감축도 했다. ([위키백과][12])

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

**Loop 4 교정**

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

## 5-2. 조선 MRO와 미국 조선 재건 — `SHIPBUILDING_NAVAL_MRO`

한화오션은 미국 Philly Shipyard를 인수했고, 미국 해군 MRO 계약도 확보한 것으로 보도됐다. 동시에 중국은 미국의 중국 조선업 조사에 대한 보복으로 한화오션의 미국 자회사 5곳을 제재했고, 한화오션 주가도 서울에서 큰 폭으로 하락했다. ([AP News][13])

```text
가격경로 1차 판정:
NAVAL_MRO_OPTION_WITH_GEOPOLITICAL_RISK

좋은 점:
- 미국 조선 재건 narrative
- Philly Shipyard
- 미 해군 MRO reference
- Jones Act / 미국 해양 인프라 option

주의:
- 중국 제재
- 초기 MRO 저마진 가능성
- 미국 법적 제한
- 설비 현대화 CAPEX
- 신조 수주로 이어지는지 미확인
```

**Loop 4 교정**

```text
SHIPBUILDING_NAVAL_MRO:
Stage 2 reference는 가능.
하지만 Stage 3는 반복 고마진 MRO 또는 신조/군함 수주가 확인될 때만.

geopolitical_sanction_flag를 추가한다.
```

---

## 5-3. 무인 해양 방산 — option은 있으나 양산계약 전 Green 금지

한화는 미국 방산 스타트업 Vatn Systems와 협력해 미 해군용 autonomous underwater drones를 공동 개발하기로 했다. Vatn은 이미 Pentagon contracts를 확보했고, 수중 드론은 중국 위협과 무인 해양전 수요에 대응하는 옵션이지만, 아직 대량양산·장기계약·매출 visibility가 확인된 방산 backlog와는 다르게 봐야 한다. ([Reuters][14])

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

**Loop 4 교정**

```text
DEFENSE_UNMANNED_NAVAL_SYSTEMS:
prototype / partnership = Stage 1.
Pentagon production contract + delivery schedule + margin = Stage 2~3 후보.
```

---

## 5-4. 데이터센터 전력망 공동설계 필요 — 수요는 강하지만 병목은 복잡해진다

최근 연구는 AI training data center가 기존 전력망의 load diversity 가정을 깨고, 수백 MW 단위의 동기화된 부하 변동을 만들 수 있다고 지적한다. 이는 전력장비 수요를 키우는 구조증거이지만, 동시에 data center와 grid의 공동설계가 없으면 interconnection·grid stability 문제가 project delay로 전환될 수 있다는 뜻이기도 하다. ([arXiv][15])

```text
가격경로 1차 판정:
AI_DATA_CENTER_GRID_COMPLEXITY_WATCH

의미:
AI 전력수요는 구조적.
하지만 전력장비 수주가 자동으로 매출화되는 것은 아니다.

감점 조건:
- grid_interconnection_delay
- load_volatility_risk
- utility coordination failure
- storage/UPS integration cost
```

**Loop 4 교정**

```text
AI_DATA_CENTER_POWER_EQUIPMENT:
전력수요 자체는 Green 근거.
하지만 grid integration complexity는 delivery risk로 별도 감점.
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

변압기 쇼티지는 강한 구조증거지만, ABB처럼 대규모 CAPA 증설이 시작되고, 데이터센터 moratorium·지역반발이 늘면 신규수주 증가율과 valuation을 같이 봐야 한다. ([Reuters][1])

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

루마니아 K9 계약과 유럽 매출 전망은 성공 후보지만, 한화에어로스페이스의 증자 shock은 방산에도 4B/4C 감시가 필요하다는 증거다. ([Reuters][6])

---

## 6-3. 철도·인프라 대형수주 4B-watch

```text
4B 조건:
- 대형 해외 철도 계약 뉴스로 관련주 급등
- 계약금액만 보고 마진·warranty·납기·financing 무시
- 실제 OP/EPS 전환 전 가격이 먼저 감
```

현대로템의 모로코 수주는 Stage 2 후보지만, 계약마진과 납품 스케줄, financing을 확인해야 한다. ([Reuters][9])

---

## 6-4. 원전 4B-watch

```text
4B 조건:
- Big Tech nuclear PPA 뉴스로 원전 관련주 동반 과열
- 기존 원전 PPA와 SMR 테마를 섞음
- SMR 비용초과·고객확보 실패 리스크 무시
```

Meta–Constellation PPA와 Microsoft–Three Mile Island 재가동 논의는 기존 원전에는 강한 구조증거지만, NuScale UAMPS 취소는 SMR 실행 리스크를 보여준다. ([Reuters][10])

---

## 6-5. 조선·미국 해군 MRO 4B-watch

```text
4B 조건:
- 미국 조선 재건 narrative가 과열
- MRO reference를 곧바로 고마진 신조 수주로 오해
- Philly Shipyard 인수와 미 해군 MRO를 과대평가
- 중국 제재·CAPEX·저마진 초기작업을 무시
```

한화오션의 미국 조선 exposure는 option이지만, 중국 제재와 MRO 저마진/신조 전환 불확실성을 반드시 붙여야 한다. ([AP News][13])

---

# 7. 4C-thesis-break 사례

## 7-1. 데이터센터 project delay

```text
4C-watch:
local_opposition
water_permitting_delay
grid_interconnection_delay
moratorium
noise_pollution
project_withdrawal
```

Perth의 120MW 데이터센터 철회, Seattle·Indianapolis의 moratorium 논의는 AI 데이터센터 수요가 전력장비 수주로 자동 연결되지 않는다는 기준이다. ([Guardian][4])

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

한화에어로스페이스 유상증자 사례는 수주잔고가 좋아도 capital allocation이 나쁘면 가격경로가 깨진다는 기준이다. ([Reuters][8])

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

NuScale UAMPS는 SMR archetype에서 hard counterexample이다. ([위키백과][12])

---

## 7-4. 조선 MRO option 과대평가

```text
4C-watch:
low_margin_MRO
newbuild_license_uncertain
US_legal_restriction
shipyard_modernization_CAPEX
geopolitical_sanction
naval_MRO_not_yet_high_margin
```

한화오션의 미국 조선 exposure는 전략적으로 중요하지만, MRO 경험을 곧바로 고마진 신조 backlog로 처리하면 false-positive가 된다. ([AP News][13])

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

현대로템 모로코 수주는 대형 계약이지만, 철도는 계약금액과 실제 이익률이 다를 수 있어 margin과 납품 스케줄을 반드시 분리해야 한다. ([Reuters][9])

---

# 8. 점수비중 보정표 — R1 Loop 4 / v4.0

| canonical archetype                   | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | Loop 4 핵심 감점                                 |
| ------------------------------------- | ------: | ---------: | ---------: | ---------: | --------: | ------: | ---: | -------------------------------------------- |
| `GRID_TRANSFORMER_SHORTAGE`           |      24 |         25 |         24 |         12 |        11 |       1 |    5 | CAPA 정상화, 데이터센터 지연, 저마진 장기계약                 |
| `GRID_MEDIUM_VOLTAGE_EXPANSION`       |      22 |         23 |         20 |         12 |        11 |       1 |    5 | CAPA 증설 후 가격정상화, 제품 mix                      |
| `AI_DATA_CENTER_POWER_EQUIPMENT`      |      22 |         23 |         19 |         13 |        11 |       0 |    5 | project delay, valuation crowding, orders 둔화 |
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

Loop 4에서 가장 크게 바뀐 건 다섯 가지다.

```text
1. GRID_MEDIUM_VOLTAGE_EXPANSION을 추가.
   전력설비 병목이 초고압 변압기에서 중전압 장비·switchgear로 확장됐기 때문.

2. DEFENSE_LOCAL_PRODUCTION_PLATFORM을 추가.
   방산 수주는 단발 수출보다 고객국 현지생산 플랫폼화가 더 강한 visibility를 줄 수 있다.

3. DEFENSE_CAPITAL_ALLOCATION_SHOCK를 gate로 격상.
   수주가 좋아도 대규모 증자와 목적 불명확 CAPEX가 나오면 Stage 강등.

4. NUCLEAR_EXISTING_PPA_RESTART와 NUCLEAR_SMR_GRID_POLICY를 더 강하게 분리.
   기존 원전 PPA/재가동은 cash-flow evidence가 있지만, SMR은 cost overrun과 cancellation risk가 크다.

5. DATA_CENTER_GRID_PERMITTING_OVERLAY를 전력설비에도 본격 적용.
   데이터센터 지역반발·수자원·전력망 지연이 전력장비 신규수주 timing을 흔들 수 있기 때문.
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
저마진 MRO, 미국 법적 제한, CAPEX 부담, 제재·정치 리스크
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

## R1 Loop 4 공통 검증 방식

```text
1. 각 case의 stage1_date, stage2_date, stage3_date를 지정한다.
2. 해당 날짜의 종가를 stage_price로 저장한다.
3. MFE_30D / 90D / 180D / 1Y / 2Y를 계산한다.
4. MAE_30D / 90D / 180D / 1Y를 계산한다.
5. peak_price와 drawdown_after_peak를 계산한다.
6. 계약금액, 계약기간, 납품스케줄, 수주잔고, OP/EPS revision, 마진 변화와 가격경로를 비교한다.
```

## Loop 4에서 새로 강제할 판정

```text
GRID_BOTTLENECK_STRUCTURAL:
리드타임·가격·수입·CAPA 병목이 동시에 확인.

MEDIUM_VOLTAGE_EXPANSION_ALIGNED:
중전압 장비 수요와 CAPA 확대가 실제 수주·OPM으로 연결.

CONTRACT_QUALITY_ALIGNED:
계약금액·기간·납품·마진·OP/EPS가 확인되고 주가도 리레이팅.

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
```

## 이번 R1 Loop 4에서 우선 검증할 가격 case

| case_id                                            | stage2 후보일 | 현재 1차 가격판정                               |
| -------------------------------------------------- | ---------: | ---------------------------------------- |
| `us_transformer_shortage_import_slots_case`        | 2026-05-11 | 구조적 전력망 병목 reference                     |
| `abb_medium_voltage_expansion_case`                | 2026-05-11 | 중전압 장비 CAPA 확대 reference                 |
| `ge_vernova_data_center_orders_case`               | 2026-04-22 | AI power equipment aligned + 4B-watch    |
| `perth_data_center_withdrawal_case`                | 2026-05-15 | data center project delay overlay        |
| `seattle_indianapolis_data_center_moratorium_case` | 2026-05-15 | moratorium / local opposition overlay    |
| `hanwha_aerospace_romania_k9_case`                 | 2024-07-09 | +5% record high, defense backlog aligned |
| `hanwha_aerospace_europe_sales_visibility_case`    | 2024-10-07 | local production platform candidate      |
| `hanwha_aerospace_dilution_case`                   | 2025-03-27 | -13%, capital allocation shock           |
| `hanwha_ocean_us_shipbuilding_sanction_case`       |    2025-10 | naval MRO option + geopolitical risk     |
| `hanwha_vatn_underwater_drone_case`                |    2025-12 | unmanned naval system option             |
| `hyundai_rotem_morocco_rail_case`                  | 2025-02-26 | 2.2조 원 철도 Stage 2 후보                     |
| `meta_constellation_existing_nuclear_ppa_case`     | 2025-06-03 | 기존 원전 PPA reference                      |
| `constellation_tmi_microsoft_restart_case`         | 2026-05-11 | 원전 재가동 + Microsoft power demand          |
| `nuscale_uamps_smr_cancel_case`                    |    2023-11 | SMR hard 4C                              |
| `ukraine_reconstruction_policy_case`               |        계약별 | actual contract before Green             |
| `neom_city_policy_case`                            |        계약별 | actual contract before Green             |

---

# 11. 다음에 에이전트가 채워야 할 price fields

R1 Loop 4에서는 아래 필드를 채우게 해야 한다.

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

medium_voltage_order
medium_voltage_capacity_expansion
switchgear_order
substation_equipment_order
utility_customer_flag
grid_operator_customer_flag

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

score_price_alignment
price_validation_status
review_notes
```

---

# R1 Loop 4 결론

이번 4회차에서 R1은 더 좁혀졌다.

```text
강한 Green 후보:
초고압 변압기·전력설비 병목
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

Hard 4C:
데이터센터 project delay / moratorium / 지역반발
방산 dilution
SMR 비용초과·고객확보 실패
조선 MRO 과대평가·중국 제재
철도 financing·마진 리스크
재건·네옴 실제 계약 부재
```

**R1 Loop 4 점수정규화의 핵심 문장:**

> 산업재·수주·인프라는 “수주가 있다”가 아니라 **계약금액, 계약기간, 거래상대방, 납품스케줄, 수주잔고 질, 마진, OP/EPS 상향, FCF 전환, 가격경로 리레이팅**이 같이 있어야 Green이다.
> Loop 4부터는 특히 `data_center_grid_permitting`, `defense_capital_allocation_shock`, `local_production_margin_dilution`, `MRO_option_only`, `SMR_policy_false_green`을 강한 감점축으로 넣어야 한다.

다음 순서는 **R2 — AI·반도체·전자부품 Loop 4**다.

[1]: https://www.reuters.com/business/energy/us-power-transformer-buyers-scramble-imports-factory-slots--reeii-2026-05-11/?utm_source=chatgpt.com "US power transformer buyers scramble for imports, factory slots"
[2]: https://www.reuters.com/sustainability/boards-policy-regulation/abb-invest-200-million-medium-voltage-equipment-production-europe-2026-05-11/?utm_source=chatgpt.com "ABB to invest $200 million in medium-voltage equipment production in Europe"
[3]: https://www.reuters.com/business/energy/ge-vernova-lifts-annual-revenue-forecast-data-center-demand-2026-04-22/?utm_source=chatgpt.com "GE Vernova lifts 2026 outlook as AI boom fuels power equipment demand"
[4]: https://www.theguardian.com/technology/2026/may/15/developer-withdraws-plans-for-perth-datacentre-after-fierce-community-opposition?utm_source=chatgpt.com "Developer withdraws plans for Perth datacentre after fierce community opposition"
[5]: https://www.axios.com/local/seattle/2026/05/15/seattle-data-center-moratorium-ai-energy?utm_source=chatgpt.com "Seattle weighs pause on large data centers"
[6]: https://www.reuters.com/business/aerospace-defense/south-koreas-hanwha-aerospace-wins-1-bln-order-romania-k9-howitzers-2024-07-09/?utm_source=chatgpt.com "South Korea's Hanwha Aerospace wins $1 bln order from Romania for self-propelled howitzers"
[7]: https://www.reuters.com/business/aerospace-defense/hanwha-aerospaces-europe-land-arms-sales-double-by-2027-ceo-says-2024-10-07/?utm_source=chatgpt.com "Hanwha Aerospace's Europe land arms sales to double by 2027, CEO says"
[8]: https://www.reuters.com/business/aerospace-defense/south-korea-market-watchdog-orders-hanwha-aerospace-revise-share-issuance-plan-2025-03-27/?utm_source=chatgpt.com "S. Korea watchdog blocks Hanwha Aerospace $2.5 billion capital raising plan"
[9]: https://www.reuters.com/markets/deals/hyundai-rotem-wins-15-billion-order-moroccos-national-rail-operator-2025-02-26/?utm_source=chatgpt.com "Hyundai Rotem wins $1.5 billion order from Morocco's national rail operator"
[10]: https://www.reuters.com/sustainability/climate-energy/meta-signs-power-agreement-with-constellation-nuclear-plant-2025-06-03/?utm_source=chatgpt.com "Meta signs power agreement with Constellation nuclear plant"
[11]: https://www.reuters.com/business/energy/us-may-decide-three-mile-island-restart-june-constellation-execs-say-2026-05-11/?utm_source=chatgpt.com "US may decide on Three Mile Island restart in June, Constellation execs say"
[12]: https://en.wikipedia.org/wiki/NuScale_Power?utm_source=chatgpt.com "NuScale Power"
[13]: https://apnews.com/article/cb72348bb00cb95801c2d6b5a47702fa?utm_source=chatgpt.com "China sanctions 5 US units of South Korean shipbuilder Hanwha Ocean over probe by Washington"
[14]: https://www.reuters.com/business/aerospace-defense/south-koreas-hanwha-us-defense-startup-vatn-build-underwater-drones-2025-12-10/?utm_source=chatgpt.com "South Korea's Hanwha, US defense startup Vatn to build underwater drones"
[15]: https://arxiv.org/abs/2605.03090?utm_source=chatgpt.com "From Barrier to Bridge: The Case for AI Data Center/Power Grid Co-Design"

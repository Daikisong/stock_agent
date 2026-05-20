좋아. **R13까지 1회전이 끝났으니, 규칙대로 다시 R1로 돌아와서 2회차를 시작한다.**

이번은 **R1 — 산업재·수주·인프라, Loop 2 / v2.0**이다.
1회차 R1이 “지도 고정”이었다면, 2회차 R1은 **실제 가격경로와 RedTeam 조건을 더 강하게 붙이는 보강 라운드**로 간다.

R1의 기본 원칙은 그대로다. 전력설비, 전선·케이블, 조선, 조선 기자재, 방산, 원전, 철도, 건설기계, 우크라 재건, 네옴시티는 모두 이 대섹터에 들어오지만, 수주 뉴스만으로 Green을 주면 안 된다. 계약질, 납품기간, 수주잔고, 마진, EPS 상향, 가격 리레이팅이 같이 확인되어야 한다.
또 OpenDART detail fetch 원칙처럼 계약금액, 계약기간, 매출 대비 계약금액, 거래상대방, 계약 시작·종료일 같은 값은 실제 공시·리포트에서 확인될 때만 써야 하고, 없는 숫자는 절대 만들면 안 된다.
서생원식으로도 R1은 “수주가 많다”가 아니라, **산업 구조 변화 → EPS/FCF 체급 변화 → 시장의 과거 프레임 오해 → 밸류에이션 리레이팅**이 이어지는지를 보는 라운드다.

---

# R1 Loop 2. 산업재·수주·인프라

## 1. 이번 라운드 대섹터

```text
R1 = 산업재·수주·인프라
Loop 2 목표 = 수주형 Green 후보와 정책/Event 후보를 더 엄격히 분리
```

이번 회차의 핵심은 이거다.

```text
좋은 수주형:
계약금액
계약기간
납품 스케줄
수주잔고
마진
EPS/OP 상향
가격경로 리레이팅

나쁜 수주형:
MOU
정책 기대
저마진 계약
법적 지연
프로젝트 financing 불확실
자본조달/dilution
CAPA 정상화
```

R1은 Green 가능성이 높은 대섹터지만, 동시에 “수주 뉴스 과열”도 자주 나오는 대섹터다.

---

## 2. 대상 canonical archetype

Loop 2에서 R1 canonical archetype은 아래처럼 유지하되, 일부는 더 세분화한다.

| canonical archetype                | Loop 2 정책                                 |
| ---------------------------------- | ----------------------------------------- |
| `GRID_TRANSFORMER_SHORTAGE`        | Green 가능. R1 최상위 핵심축                      |
| `AI_DATA_CENTER_POWER_EQUIPMENT`   | Green 가능. 변압기와 데이터센터 내부 전력장비 분리           |
| `CONTRACT_BACKLOG_INDUSTRIAL`      | Green 가능. 계약질·마진 확인 필수                    |
| `DEFENSE_GOVERNMENT_BACKLOG`       | Green 가능. 다년계약·수주잔고·납품 스케줄 핵심             |
| `DEFENSE_TECH_AUTONOMOUS_SYSTEMS`  | Watch-to-Green. framework → 실제 조달 전환 필요   |
| `DEFENSE_DRONE_COUNTER_UAS`        | Watch-to-Green. prototype만 있으면 Green 금지   |
| `DEFENSE_AI_SOFTWARE_INTELLIGENCE` | Watch-to-Green. prototype 계약과 반복 SW 매출 분리 |
| `SHIPBUILDING_OFFSHORE_BACKLOG`    | Green 가능. 선가·저가수주 소진·마진 확인 필요             |
| `RAIL_INFRASTRUCTURE`              | Watch-to-Green. 대형계약은 좋지만 마진·financing 확인 |
| `NUCLEAR_SMR_GRID_POLICY`          | Watch-to-Green. 기존 원전 PPA와 신규 SMR을 분리     |
| `GEOPOLITICAL_RECONSTRUCTION`      | Event/Watch. 실제 수주 전 Green 금지             |
| `SMART_FACTORY_AUTOMATION`         | Watch. PoC/MOU와 반복 매출 분리                  |

---

## 3. deep sub-archetype

이번 Loop 2에서는 R1을 아래 하위 렌즈로 더 고정한다.

```text
GRID_TRANSFORMER_SHORTAGE
- 변압기
- 초고압 변압기
- 전선·케이블
- 배전반
- 전력기기
- GSU transformer
- substation transformer
- 리드타임 장기화
- 가격 상승
- 데이터센터 전력망

AI_DATA_CENTER_POWER_EQUIPMENT
- UPS
- PDU
- switchgear
- modular power
- 데이터센터 내부 전력장비
- 전력품질·전력분배

DEFENSE_GOVERNMENT_BACKLOG
- K9
- K10
- K2
- 천무
- 탄약
- 엔진
- AESA radar
- KF-21
- 현지생산
- NATO 재무장

DEFENSE_TECH_AUTONOMOUS_SYSTEMS
- 드론
- 저가 대량 미사일
- containerized munitions
- autonomous system
- unmanned vehicle
- counter-UAS

SHIPBUILDING_OFFSHORE_BACKLOG
- LNG선
- VLGC
- 컨테이너선
- 해양플랜트
- 조선 기자재
- 엔진
- 피팅밸브
- 선가
- 저가수주 소진
- 미 해군 MRO

RAIL_INFRASTRUCTURE
- 철도차량
- 고속철
- 도시철도
- 해외 철도수출
- 납품 스케줄
- 프로젝트 financing

NUCLEAR_SMR_GRID_POLICY
- 기존 원전 PPA
- 원전 수명연장
- SMR
- 원전 기자재
- 법적 리스크
- 비용초과
- PPA 가격
```

---

# 4. 성공사례

## 4-1. 변압기·전력망 병목: R1 최상위 Green 후보

미국에서는 데이터센터, EV, 공장, 재생에너지, 전력망 현대화 수요 때문에 GSU 변압기 수요가 2019~2025년에 274%, 변전소용 power transformer 수요가 116% 증가했고, 대형 변압기 리드타임은 최대 4년, 가격은 5년 동안 약 80% 상승했다. Reuters는 미국 전력 개발사들이 한국·튀르키예 등 해외 수입과 생산 슬롯 선점으로 대응하고 있으며, LS ELECTRIC이 2025년 11월 미국 유틸리티와 3.12억 달러 규모 525kV 초고압 변압기 공급계약을 맺어 미국 남동부 대형 데이터센터에 2027~2029년 납품하기로 했다고 보도했다. ([Reuters][1])

**가격경로 1차 판정**

```text
case_type:
structural_success_candidate

현재 공개 가격경로:
개별 한국 종목별 MFE/MAE는 agent price backfill 필요.
다만 산업 병목, 가격 상승, 리드타임, 실제 한국 업체 계약까지 확인됨.

R1 Loop 2 판정:
GRID_TRANSFORMER_SHORTAGE는 R1 최상위 Green 가능 archetype으로 유지.
```

**점수 교정**

| 축                     | 보정                         |
| --------------------- | -------------------------- |
| EPS/FCF               | 22 → 23                    |
| Structural Visibility | 25 유지                      |
| Bottleneck/Pricing    | 23 유지                      |
| Market Mispricing     | 12 유지                      |
| 4B risk               | CAPA 증설·생산 슬롯 정상화 시 강하게 감시 |

---

## 4-2. GE Vernova: 전력기기·데이터센터 전력장비의 글로벌 가격경로 reference

GE Vernova는 데이터센터 전력수요 덕분에 2026년 매출 전망을 445억~455억 달러로 높였고, 1분기 orders는 71% 증가한 183억 달러, backlog는 1,630억 달러까지 늘었다. WSJ 보도 기준으로 electrification unit 매출은 61% 성장했고, 데이터센터 관련 orders가 분기 24억 달러로 전년 전체보다 컸으며, 발표 후 주가는 약 15% 상승했고 2026년 들어 거의 70% 오른 상태였다. ([The Wall Street Journal][2])

**가격경로 1차 판정**

```text
가격 반응:
실적/가이던스 후 +15%
2026년 YTD 약 +70%

판정:
AI_data_center_power_equipment_aligned + 4B_watch

의미:
전력장비는 실제 orders/backlog/EPS가 확인되면 가격경로가 강하게 따라올 수 있음.
다만 이미 급등한 상태에서는 4B-watch 필요.
```

**R1 적용**

```text
한국 전력설비주 검증 시:
GE Vernova식 orders/backlog/revenue guidance 패턴을 비교 reference로 사용.
```

---

## 4-3. 한화에어로스페이스 K9 루마니아 계약: 방산 수주형 aligned 후보

한화에어로스페이스는 루마니아에 K9 자주포 54문, K10 탄약운반장갑차 36대, 탄약·지원 패키지를 공급하는 약 10억 달러 계약을 맺었고, 계약기간은 2029년까지다. Reuters는 한화 방산 수주잔고가 2021년 말 5.1조 원에서 2024년 3월 약 30조 원으로 증가했고, 계약 보도 후 한화에어로스페이스 주가가 5% 이상 올라 record high를 기록했다고 보도했다. ([Reuters][3])

**가격경로 1차 판정**

```text
가격 반응:
계약 보도 후 +5% 이상, record high

판정:
defense_backlog_aligned_candidate

검증 필요:
2024-07-09 이후 180D / 1Y / 2Y MFE
수주잔고 증가율
OP margin 변화
유럽 매출 인식 속도
```

**점수 교정**

| 축                     | 보정                        |
| --------------------- | ------------------------- |
| EPS/FCF               | 20 유지                     |
| Structural Visibility | 24 유지                     |
| Bottleneck/Pricing    | 17 유지                     |
| Capital Allocation    | 3 유지, dilution 발생 시 강한 감점 |

---

## 4-4. 한화 유럽 방산 매출 visibility: 단발계약이 아니라 지역 생산·장기 공급

한화에어로스페이스 CEO는 유럽 육상무기 매출이 2027년까지 두 배가 될 것으로 기대한다고 밝혔고, Reuters는 폴란드 92억 달러, 루마니아 10억 달러 계약과 현지생산 선호가 배경이라고 설명했다. 회사의 육상무기 수주잔고는 2020년 이후 10배 증가한 것으로 보도됐다. ([Reuters][4])

**가격경로 1차 판정**

```text
case_type:
multi_year_visibility_candidate

의미:
R1에서 진짜 강한 수주형은 단일 계약보다
지역별 반복계약·현지생산·수주잔고 전환이 중요함.
```

**추가 검증**

```text
유럽 매출 성장률
현지공장 CAPEX
수출허가
OPM 변화
납품 지연 여부
```

---

## 4-5. 현대로템 모로코 철도 수주: 철도 Stage 2 후보

현대로템은 모로코 국영철도 ONCF로부터 약 2.2조 원, 15.4억 달러 규모의 2층 전동차 수주를 확보했고, 회사는 이 계약이 철도사업 사상 최대 수주라고 밝혔다. ([Reuters][5])

**가격경로 1차 판정**

```text
stage2_date:
2025-02-26

판정:
rail_infrastructure_stage2_candidate

현재 부족한 것:
즉시 주가 반응
계약 마진
납품 스케줄별 매출 인식
프로젝트 financing
```

**점수 교정**

```text
철도는 계약 규모가 커도 방산·변압기보다 Bottleneck/Pricing 점수를 낮게 둔다.
이유는 프로젝트 마진·납기·financing 불확실성이 더 크기 때문.
```

---

## 4-6. 조선: 수주·선가·가격반응이 같이 나온 cyclical-to-structural 후보

WSJ는 한국 조선주들이 계약 수주 재개와 신조선가 상승으로 급등했고, Samsung Heavy Industries는 16%, Hanwha Ocean은 13%, HD Hyundai Heavy Industries는 11% 상승했다고 보도했다. Clarksons Research 기준 한국은 2월 글로벌 신규 조선 수주에서 중국을 제치고 50% 점유율로 1위를 회복했고, 신조선가 지수도 상승했다고 설명됐다. ([The Wall Street Journal][6])

**가격경로 1차 판정**

```text
가격 반응:
삼성중공업 +16%
한화오션 +13%
HD현대중공업 +11%

판정:
shipbuilding_price_aligned_candidate

주의:
조선은 수주잔고의 양보다 수주잔고의 질,
저가수주 소진,
선가,
후판가,
인건비,
인도 시점 마진이 핵심.
```

---

## 4-7. 한화오션: 조선+방산+미 해군 MRO 옵션

Reuters는 한국산업은행이 한화오션 지분 19.5% 매각을 추진한다는 보도와 함께, 한화오션 주가가 2025년에 139% 상승해 2015년 7월 이후 최고치에 도달했다고 전했다. 상승 배경에는 한화그룹 편입 이후 미국과 한국의 조선 협력 기대, 특히 한화오션의 필라델피아 조선소 인수와 미국 해군 MRO 기대가 포함됐다. ([Reuters][7])

**가격경로 1차 판정**

```text
가격 반응:
2025년 +139%

판정:
shipbuilding_defense_MRO_success_candidate + 4B_watch

의미:
조선에서 방산/MRO 옵션이 붙으면 valuation frame이 바뀔 수 있음.
다만 139% 상승 후에는 4B-watch 필수.
```

---

## 4-8. Meta–Constellation 원전 PPA: 기존 원전 PPA는 SMR보다 증거 강도 높음

Meta는 Constellation의 Illinois Clinton 원전과 20년 계약을 맺어 2027년 이후 원전 운영과 재허가를 지원하기로 했고, Reuters는 이 계약이 AI·데이터센터 전력 수요 증가 속에서 Big Tech가 장기 무탄소 전력을 확보하려는 흐름이라고 설명했다. Constellation 주가는 premarket에서 13.4% 상승했다. ([Reuters][8])

**가격경로 1차 판정**

```text
가격 반응:
Constellation premarket +13.4%

판정:
nuclear_PPA_aligned_reference

의미:
기존 원전 PPA는 확정 수요와 현금흐름 visibility가 있어 SMR 테마보다 훨씬 강한 evidence.
한국 원전 기자재주는 직접 계약·납품·매출화 evidence가 있어야 매핑 가능.
```

---

# 5. 반례

## 5-1. 데이터센터 프로젝트 지연: 변압기·전력장비의 soft 4C

AI 데이터센터 전력수요가 전력설비 수주를 밀어주는 건 맞지만, Guardian은 미국에서 데이터센터 계획의 취소·지연이 늘고 있고, 공급망 병목, 에너지 부족, 관세, 지역 반발, 투자자들의 AI 버블 우려가 복합적으로 작용하고 있다고 보도했다. 전력망 접속 지연, 변압기·구리 공급 부족, local opposition은 데이터센터 전력장비의 soft 4C 조건으로 봐야 한다. ([가디언][9])

**교훈**

```text
AI 데이터센터 수요
≠ 모든 전력설비 계약 자동 Green

감점 조건:
데이터센터 프로젝트 취소
지역 반발
전력망 접속 지연
관세·구리·철강 원가
financing cost 상승
```

---

## 5-2. 방산 dilution: 수주잔고가 좋아도 capital allocation이 깨지면 주가가 무너짐

한화에어로스페이스는 해외 확장 재원을 위해 3.6조 원 규모 주식 발행을 추진했고, FT는 발표 후 주가가 13% 급락했다고 보도했다. Reuters도 한화가 드론·엔진 개발 등을 위해 1.3조 원 신주 발행과 2.3조 원 주주배정 유상증자를 계획했다고 보도했다. ([파이낸셜 타임스][10])

**교훈**

```text
방산 수주잔고
≠ 무조건 Green 유지

dilution
unclear use of proceeds
해외공장 CAPEX
M&A 자금조달
주주가치 희석

이 나오면 4B/4C-watch.
```

---

## 5-3. SMR 비용초과: 신규 SMR은 기존 원전 PPA와 완전히 다르게 봐야 함

NuScale의 UAMPS Carbon Free Power Project는 비용 증가와 충분한 전력 구매자 확보 실패로 2023년 취소됐다. 공개 자료 기준으로 프로젝트 비용은 2020년 36억 달러에서 2023년 93억 달러로 증가했고, 목표 전력가격도 상승했으며, 취소 이후 NuScale은 인력 감축을 진행했다. ([위키백과][11])

**교훈**

```text
SMR 정책·AI 전력 narrative
≠ Green

필수:
PPA
전력가격
financing
NRC/허가
고객 subscription
건설비 확정

없으면 Watch/Red.
```

---

## 5-4. 조선 KDB block sale / 지분 overhang

한화오션은 2025년 139% 상승이라는 강한 가격경로를 보였지만, KDB의 19.5% 지분 매각 추진 보도는 잠재 supply overhang이다. R1에서 조선·방산 복합 리레이팅은 긍정적이지만, 대주주 지분 매각·블록딜 가능성은 4B-watch로 들어가야 한다. ([Reuters][7])

---

## 5-5. 재건·네옴·정책형 인프라: 실제 계약 전 Green 금지

Theme Tag Map 기준으로 우크라 재건과 네옴시티는 Event/Watch이며, 실제 계약·매출화 전까지 Green 금지다.

**교훈**

```text
정책 발표
MOU
재건회의
대통령 발언
도시계획

이것들은 Stage 1일 뿐.
Stage 2는 실제 계약·예산·착공·매출 인식.
```

---

# 6. 4B-watch 사례

## 6-1. 전력설비 4B-watch

```text
4B 조건:
- 전력설비주 전반이 AI 데이터센터 수혜로 인정됨
- 변압기 가격·리드타임이 모두에게 알려짐
- 수주잔고는 높지만 신규수주 증가율이 둔화
- CAPA 증설 뉴스 증가
- 고객 프로젝트 지연 뉴스 증가
```

GE Vernova처럼 orders·backlog·주가가 같이 뛴 사례는 성공 후보지만, 주가가 2026년 YTD 약 70% 오른 구간에서는 4B-watch가 필요하다. ([The Wall Street Journal][2])

---

## 6-2. 방산 4B-watch

```text
4B 조건:
- K방산 수출 narrative가 모두에게 알려짐
- NATO 재무장 기대 과밀
- 목표가 상향 집중
- 현지공장 CAPEX·dilution 우려 부각
- 수출허가·정치 리스크가 시장에서 무시됨
```

한화에어로스페이스는 루마니아 계약 후 +5% record high라는 강한 aligned 가격경로가 있었지만, 이후 대규모 자본조달 발표에 -13% 급락했다는 점 때문에 4B-watch를 강하게 둬야 한다. ([Reuters][3])

---

## 6-3. 조선 4B-watch

```text
4B 조건:
- 조선주 동반 급등
- 선가 상승 narrative 과밀
- 저가수주 소진이 이미 가격에 반영
- KDB/대주주 지분 매각 overhang
- 후판가·인건비 리스크 무시
```

조선주는 삼성중공업 +16%, 한화오션 +13%, HD현대중공업 +11% 같은 강한 하루 가격반응이 확인됐지만, 이후에는 선가·마진·인도 시점이 가격경로와 맞는지 검증해야 한다. ([The Wall Street Journal][6])

---

## 6-4. 원전 4B-watch

```text
4B 조건:
- Big Tech nuclear PPA 뉴스 후 원전 관련주 동반 과열
- 기존 원전 PPA와 신규 SMR을 구분하지 않음
- 법적·허가·financing 리스크를 무시
```

Meta–Constellation PPA는 강한 기존 원전 reference지만, NuScale CFPP 취소는 신규 SMR의 비용·고객확보 리스크를 보여준다. ([Reuters][8])

---

# 7. 4C-thesis-break 사례

## 7-1. 데이터센터 프로젝트 취소·전력망 접속 지연

```text
4C-watch:
data_center_project_cancelled
grid_interconnection_delay
local_opposition
tariff_cost_spike
transformer_supply_delay
```

AI 데이터센터가 전력장비 수요를 밀어주는 건 맞지만, 데이터센터 자체가 취소·지연되면 전력장비 신규수주 증가율도 꺾일 수 있다. ([가디언][9])

---

## 7-2. 방산 dilution / unclear capital allocation

```text
4C-watch:
large_equity_issuance
dilution
use_of_proceeds_unclear
regulator_revision_request
overseas_factory_CAPEX_burden
```

한화에어로스페이스의 주식발행 발표와 -13% 가격반응은 방산 수주형에서도 capital allocation을 반드시 점수화해야 한다는 기준이다. ([파이낸셜 타임스][10])

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

NuScale CFPP는 SMR archetype에서 hard counterexample이다. ([위키백과][11])

---

## 7-4. 조선 지분 overhang / block sale

```text
4C-watch:
major_shareholder_block_sale
supply_overhang
state_bank_exit
valuation_after_rapid_rise
```

한화오션은 주가가 2025년에 139% 올랐다는 점에서 성공 후보지만, KDB 지분 매각 보도는 4B/4C-watch다. ([Reuters][7])

---

# 8. 점수비중 보정표 — R1 Loop 2 / v2.0

| canonical archetype                | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | Loop 2 핵심 감점                    |
| ---------------------------------- | ------: | ---------: | ---------: | ---------: | --------: | ------: | ---: | ------------------------------- |
| `GRID_TRANSFORMER_SHORTAGE`        |      23 |         25 |         23 |         12 |        12 |       1 |    5 | CAPA 정상화, 데이터센터 지연, 저마진 계약      |
| `AI_DATA_CENTER_POWER_EQUIPMENT`   |      21 |         22 |         18 |         13 |        12 |       0 |    5 | bookings 둔화, project delay, 저마진 |
| `CONTRACT_BACKLOG_INDUSTRIAL`      |      20 |         24 |         18 |         13 |        12 |       1 |    5 | 계약질 불명확, 납기, 마진                 |
| `DEFENSE_GOVERNMENT_BACKLOG`       |      20 |         24 |         17 |         14 |        14 |       3 |    5 | 납기, 원가, 수출허가, dilution          |
| `DEFENSE_TECH_AUTONOMOUS_SYSTEMS`  |      20 |         22 |         15 |         15 |        14 |       2 |    5 | prototype, 조달 지연, valuation 과열  |
| `DEFENSE_DRONE_COUNTER_UAS`        |      20 |         22 |         14 |         14 |        13 |       3 |    5 | 생산능력, M&A dilution, 수출통제        |
| `DEFENSE_AI_SOFTWARE_INTELLIGENCE` |      19 |         21 |         10 |         15 |        14 |       0 |    5 | prototype 단계, 정치·윤리 리스크         |
| `SHIPBUILDING_OFFSHORE_BACKLOG`    |      20 |         22 |         18 |         13 |        13 |       1 |    5 | 저가수주, 후판가, 인건비, 지분 overhang     |
| `RAIL_INFRASTRUCTURE`              |      20 |         23 |         12 |         14 |        12 |       1 |    5 | 납기, 마진, financing               |
| `NUCLEAR_SMR_GRID_POLICY`          |      18 |         22 |         10 |         14 |        12 |       2 |    5 | 허가, 소송, 비용초과, 고객확보 실패           |
| `GEOPOLITICAL_RECONSTRUCTION`      |      10 |          8 |          8 |         10 |         7 |       0 |    4 | 실제 계약 없음, 정책 이벤트                |
| `SMART_FACTORY_AUTOMATION`         |      18 |         16 |          8 |         12 |        10 |       0 |    5 | MOU/PoC, 매출화 실패                 |

Loop 2에서 가장 크게 바뀐 건 두 가지다.

```text
1. GRID_TRANSFORMER_SHORTAGE는 더 강하게 본다.
   실제 수요, 가격, 리드타임, 한국 업체 계약 reference가 모두 붙었기 때문.

2. R1 전체에 capital allocation / project delay 감점을 더 강하게 붙인다.
   방산 dilution, 데이터센터 지연, SMR 취소가 반례를 제공했기 때문.
```

---

# 9. stage date 후보

## `GRID_TRANSFORMER_SHORTAGE`

```text
Stage 1:
AI 데이터센터·EV·재생에너지·전력망 현대화로 변압기 부족 뉴스가 본격화된 날

Stage 2:
개별 기업의 초고압 변압기 공급계약, 수주잔고 급증, 실적 서프라이즈 발생일

Stage 3:
다년 수주잔고 + 가격전가 + FY1/FY2/FY3 OP/EPS 상향이 같이 확인된 날

Stage 4B:
전력설비주 전체가 AI 전력망 수혜로 인정되고 valuation band가 확장된 날

Stage 4C:
데이터센터 프로젝트 지연, 신규수주 둔화, CAPA 정상화, 저마진 계약 확인일
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
후판가·인건비 상승, 발주 둔화, 저마진 수주, 대주주 매각 overhang
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
프로젝트 지연, financing 문제, 마진 악화 확인일
```

## `NUCLEAR_SMR_GRID_POLICY`

```text
Stage 1:
원전 정책, AI 전력수요, PPA, SMR 뉴스

Stage 2:
기존 원전 PPA, 실제 계약 서명, 기자재 매출화 경로 확인일

Stage 3:
허가·소송·financing 리스크 낮고 FY2/FY3 매출 visibility 확인일

Stage 4B:
원전/SMR 관련주 동반 과열

Stage 4C:
SMR 프로젝트 취소, 비용초과, 고객 확보 실패, 법원 가처분
```

---

# 10. 가격경로 검증계획

## R1 Loop 2 공통 검증 방식

```text
1. 각 case의 stage1_date, stage2_date, stage3_date를 지정한다.
2. 해당 날짜의 종가를 stage_price로 저장한다.
3. MFE_30D / 90D / 180D / 1Y / 2Y를 계산한다.
4. MAE_30D / 90D / 180D / 1Y를 계산한다.
5. peak_price와 drawdown_after_peak를 계산한다.
6. 수주잔고, 계약기간, 계약금액/매출, OP/EPS revision, 마진 변화와 가격경로를 비교한다.
```

## Loop 2에서 새로 강제할 판정

```text
contract_quality_aligned:
계약금액·기간·마진·납품 스케줄이 확인되고 주가도 리레이팅.

backlog_without_margin:
수주잔고는 늘었지만 마진·EPS가 불명확.

project_delay_risk:
수요는 강하지만 데이터센터·원전·철도 프로젝트 지연 가능성.

capital_allocation_shock:
수주형 기업이 유상증자·대규모 CAPEX로 주주가치 희석.

policy_to_contract_failed:
재건·원전·철도·네옴 같은 정책 뉴스가 실제 계약으로 연결되지 않음.

crowded_rerating_4b:
좋은 구조지만 이미 시장이 모두 인정한 구간.
```

## 이번 R1 Loop 2에서 우선 검증할 가격 case

| case_id                                         |  stage2 후보일 | 현재 1차 가격판정                                  |
| ----------------------------------------------- | ----------: | ------------------------------------------- |
| `us_transformer_shortage_korea_import_case`     |  2026-05-11 | 구조적 병목 확인, 한국 업체 price backfill 필요          |
| `ls_electric_525kv_datacenter_transformer_case` | 2025-11 계약일 | 한국 전력설비 Stage 2 후보                          |
| `ge_vernova_data_center_orders_case`            |  2026-04-22 | +15%, aligned + 4B-watch                    |
| `hanwha_aerospace_romania_k9_case`              |  2024-07-09 | +5% 이상 record high, aligned candidate       |
| `hanwha_aerospace_europe_sales_case`            |  2024-10-07 | 다년 visibility 후보                            |
| `hanwha_aerospace_dilution_case`                |  2025-03~04 | -13%, capital allocation 4C-watch           |
| `hyundai_rotem_morocco_rail_case`               |  2025-02-26 | 대형 철도 Stage 2, price backfill 필요            |
| `korean_shipbuilder_contract_rally_case`        |     WSJ 보도일 | 삼성중공업 +16%, 한화오션 +13%, HD현대중공업 +11%         |
| `hanwha_ocean_mro_rerating_case`                |  2025-04-28 | 2025년 +139%, success + 4B-watch             |
| `meta_constellation_nuclear_ppa_case`           |  2025-06-03 | Constellation premarket +13.4%, PPA aligned |
| `nuscale_cfpp_cancel_case`                      |     2023-11 | SMR hard 4C                                 |
| `data_center_delay_transformer_soft_4c_case`    |  2026-02~05 | 전력설비 soft 4C overlay                        |

---

# 11. 다음에 에이전트가 채워야 할 price fields

R1 Loop 2에서는 기존 R1 필드에 아래를 추가로 강제한다.

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

capex_amount
dilution_flag
share_issuance_amount
use_of_proceeds_clarity
regulator_revision_request_flag

project_delay_flag
data_center_delay_flag
local_opposition_flag
grid_interconnection_delay_flag
financing_secured_flag

ship_newbuilding_price_index
low_margin_backlog_flag
steel_plate_cost_change
labor_cost_change
naval_mro_contract_flag
block_sale_overhang_flag

nuclear_ppa_flag
smr_flag
cost_overrun_flag
licensing_risk_flag
customer_subscription_flag

score_price_alignment
price_validation_status
review_notes
```

---

# R1 Loop 2 결론

이번 2회차에서 R1은 더 선명해졌다.

```text
강한 Green 후보:
전력설비·변압기
데이터센터 전력장비
방산 정부 백로그
조선 고마진 수주/MRO 옵션

Watch-to-Green:
철도
방산테크
방산 AI software
원전 PPA
일부 산업재 장기계약

Event/Watch:
우크라 재건
네옴시티
정책형 인프라

Red/4C 방어:
SMR 비용초과
방산 dilution
데이터센터 프로젝트 지연
조선 저마진/지분 overhang
철도 financing 지연
```

**R1 Loop 2 점수정규화의 핵심 문장:**

> 산업재·수주·인프라는 “수주가 있다”가 아니라 **계약질, 납품기간, 수주잔고, 마진, EPS 상향, 가격경로 리레이팅**이 같이 있어야 Green이다.
> 2회차부터는 특히 `project_delay`, `capital_allocation_shock`, `CAPA_normalization`, `low_margin_backlog`를 강한 감점축으로 넣어야 한다.

이제 다시 루프가 시작됐고, 다음에 같은 지시가 오면 순서대로 **R2 — AI·반도체·전자부품 Loop 2**로 넘어간다.

[1]: https://www.reuters.com/business/energy/us-power-transformer-buyers-scramble-imports-factory-slots--reeii-2026-05-11/?utm_source=chatgpt.com "US power transformer buyers scramble for imports, factory slots"
[2]: https://www.wsj.com/business/earnings/ge-vernova-lifts-outlook-on-accelerating-power-demand-d81d21e8?utm_source=chatgpt.com "GE Vernova Lifts Outlook on Surge From Data Center Demand"
[3]: https://www.reuters.com/business/aerospace-defense/south-koreas-hanwha-aerospace-wins-1-bln-order-romania-k9-howitzers-2024-07-09/?utm_source=chatgpt.com "South Korea's Hanwha Aerospace wins $1 bln order from Romania for self-propelled howitzers"
[4]: https://www.reuters.com/business/aerospace-defense/hanwha-aerospaces-europe-land-arms-sales-double-by-2027-ceo-says-2024-10-07/?utm_source=chatgpt.com "Hanwha Aerospace's Europe land arms sales to double by 2027, CEO says"
[5]: https://www.reuters.com/markets/deals/hyundai-rotem-wins-15-billion-order-moroccos-national-rail-operator-2025-02-26/?utm_source=chatgpt.com "Hyundai Rotem wins $1.5 billion order from Morocco's national rail operator"
[6]: https://www.wsj.com/articles/south-korean-shipbuilders-rally-on-brisk-contract-wins-d44ecb8a?utm_source=chatgpt.com "South Korean Shipbuilders Rally on Brisk Contract Wins"
[7]: https://www.reuters.com/markets/europe/korea-development-bank-sell-shares-hanwha-ocean-paper-reports-2025-04-28/?utm_source=chatgpt.com "Korea Development Bank to sell shares in Hanwha Ocean, paper reports"
[8]: https://www.reuters.com/sustainability/climate-energy/meta-signs-power-agreement-with-constellation-nuclear-plant-2025-06-03/?utm_source=chatgpt.com "Meta signs power agreement with Constellation nuclear plant"
[9]: https://www.theguardian.com/business/2026/feb/24/datacenters-ai-construction?utm_source=chatgpt.com "US datacenters face slew of problems amid grassroots protests against AI"
[10]: https://www.ft.com/content/994a0a80-414f-442f-bf41-f2dbde5a04ca?utm_source=chatgpt.com "South Korea's biggest defence group plans $2.5bn share sale to expand overseas"
[11]: https://en.wikipedia.org/wiki/NuScale_Power?utm_source=chatgpt.com "NuScale Power"

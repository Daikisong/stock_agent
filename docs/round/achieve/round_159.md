좋아. **R13 Loop 9까지 끝났으니, 규칙대로 다시 R1로 돌아와서 이번은 R1 Loop 10 — 산업재·수주·인프라**다.

R1은 전력설비, 전선·케이블, 피팅밸브, 조선, 방산, 원전, 철도, 건설기계, 우크라 재건, 네옴시티를 흡수한다. 이 대섹터는 성공 사례가 많이 나올 수 있지만, 수주 뉴스만으로는 부족하고 **계약질 + 마진 + EPS/FCF 상향 + 실제 주가 리레이팅**이 같이 가야 한다.

서생원식으로 보면 R1에서 찾는 것은 “수주가 많은 회사”가 아니라, **산업의 성격이 바뀌면서 EPS/FCF가 폭발적으로 올라가고, 시장이 아직 과거 프레임으로 낮은 밸류에이션을 주는 후보**다. 즉 전력망·변압기·가스터빈·방산·철도·원전 모두 같은 공식으로 본다.

공시 기반 검증에서는 단일판매·공급계약, 신규시설투자, 잠정실적, 영업실적 전망, 유상증자, CB/BW, 감사의견, 거래정지, 계약 해지·정정 같은 watch disclosure를 detail에서 확인해야 한다. 계약금액, 계약기간, 상대방, 매출 대비 계약금액, OP YoY, 희석률이 없으면 만들지 않는다.

---

# R1 Loop 10. 산업재·수주·인프라

## 1. 이번 라운드 대섹터

```text
R1 = 산업재·수주·인프라

Loop 10 목표 =
전력장비·변압기·가스터빈·철도·원전·방산·조선 후보를
“수주 뉴스”가 아니라

계약질
+ backlog
+ margin
+ EPS/FCF 전환
+ 자본배분
+ 가격경로
+ 4B/4C RedTeam

으로 다시 정규화
```

이번 R1 Loop 10의 핵심 질문은 이거다.

```text
이 회사는 수주가 많은가?
X

이 회사는 수주가 EPS/FCF 체급 변화로 넘어갔고,
시장이 과거 프레임을 버리며 valuation을 다시 주고 있는가?
O
```

R1 stage는 이렇게 잡는다.

```text
Stage 1:
AI 데이터센터 전력수요, 전력망 부족, 방산 재무장,
철도투자, 원전 재가동, 미국 조선 재건, 재건정책 뉴스

Stage 2:
계약금액, 계약기간, 고객명, 납품스케줄, backlog,
slot reservation, PPA, 정부계약, 수주공시 확인

Stage 3:
OP/EPS/FCF 상향, margin 개선, 자본환원,
수주잔고의 질 개선, 실제 가격경로 동행

Stage 4B:
모두가 전력설비·AI power·방산·원전 수혜를 인정해서
valuation이 먼저 간 구간

Stage 4C:
대규모 증자, 저마진 수주, 납기 지연, 관세·원가 shock,
wind loss, grid approval delay, MoU-only, no-revenue SMR,
회계·공시 문제
```

R1 Loop 10의 핵심 분리는 이거다.

```text
전력수요 증가
≠ 전력장비 Green

수주잔고 증가
≠ FCF 증가

MoU/MoA
≠ 계약

PPA
≠ 발전소 재가동 성공

방산 수요
≠ 주주가치 상승

현지공장·CAPEX
≠ margin 방어

재건정책
≠ 실제 수주
```

---

## 2. 대상 canonical archetype

| canonical archetype                | Loop 10 판정 방향  | stage 포착 핵심                                      |
| ---------------------------------- | -------------- | ------------------------------------------------ |
| `GRID_TRANSFORMER_SHORTAGE`        | Green 후보       | lead time, price, GSU/substation demand, CAPA    |
| `GRID_EHV_TRANSFORMER_EXPORT`      | Stage 2 강함     | 525kV/765kV, 고객, 계약금액, 납품기간                      |
| `GRID_SUPPLY_SLOT_PREBUY`          | Watch-to-Green | slot reservation, production slot 선점, 장기계약       |
| `POWER_EQUIPMENT_BACKLOG_TO_FCF`   | Stage 3 후보     | backlog → margin → FCF → buyback                 |
| `GAS_TURBINE_POWER_BACKLOG`        | Stage 2~3 후보   | turbine backlog, reservation, data-center power  |
| `AI_DATA_CENTER_POWER_EQUIPMENT`   | Green 후보       | data-center orders, electrification backlog, FCF |
| `DEFENSE_GOVERNMENT_BACKLOG`       | Green 가능       | 정부고객, 다년계약, 납품스케줄                                |
| `DEFENSE_CAPITAL_ALLOCATION_SHOCK` | hard gate      | 대규모 증자, dilution, FSS 정정요구                       |
| `DEFENSE_US_SHIPBUILDING_PLATFORM` | Stage 1~2      | MoU/MoA와 실제 계약 분리                                |
| `SHIPBUILDING_NAVAL_MRO`           | Watch-to-Green | 실제 MRO 계약, 반복수리, margin                          |
| `RAIL_INFRASTRUCTURE`              | Stage 2 후보     | 대형계약, financing, warranty, local content         |
| `NUCLEAR_EXISTING_PPA_RESTART`     | Watch-to-Green | Big Tech PPA, grid rights, FERC/NRC approval     |
| `NUCLEAR_SMR_GRID_POLICY`          | Watch/Red      | no revenue면 Stage 3 금지                           |
| `GEOPOLITICAL_RECONSTRUCTION`      | Event/Watch    | 실제 계약·financing·착공 전 Green 금지                    |
| `DISCLOSURE_CONFIDENCE_CAP`        | 공통 cap         | 계약금액·기간·마진 detail 부족 시 Stage 3 제한                |

---

## 3. deep sub-archetype

```text
GRID_TRANSFORMER_SHORTAGE
- GSU transformer
- substation transformer
- EHV transformer
- lead time up to four years
- transformer price +80%
- copper
- GOES
- AI data center
- EV
- grid modernization
- import dependence
- factory slot pre-buying

GRID_EHV_TRANSFORMER_EXPORT
- LS Electric
- 525kV transformer
- U.S. utility
- southeastern U.S. data center
- $312m contract
- 2027~2029 delivery
- South Korea supplier
- import substitution

POWER_EQUIPMENT_BACKLOG_TO_FCF
- GE Vernova
- Siemens Energy
- electrification
- grid equipment
- gas turbine
- backlog
- slot reservation
- FCF
- buyback
- tariff cost
- wind segment drag

GAS_TURBINE_POWER_BACKLOG
- gas turbine reservations
- data center power
- 110GW backlog/reservation target
- power unit profit
- capacity ramp
- AI electricity demand

DEFENSE_GOVERNMENT_BACKLOG
- Hanwha Aerospace
- K9
- K10
- Chunmoo
- overseas production
- defense export
- government customer
- capacity expansion
- dilution risk

DEFENSE_US_SHIPBUILDING_PLATFORM
- HD Hyundai Heavy
- Huntington Ingalls
- U.S. Navy auxiliary ships
- MoA
- U.S. shipyard investment
- MASGA
- U.S. workforce bottleneck
- tariff negotiation
- actual vessel contract

RAIL_INFRASTRUCTURE
- Hyundai Rotem
- Morocco ONCF
- double-decker trains
- $1.54B order
- largest rail order
- delivery schedule
- warranty
- local content
- financing

NUCLEAR_EXISTING_PPA_RESTART
- Constellation
- Three Mile Island / Crane Clean Energy Center
- Microsoft data center PPA
- FERC approval
- grid injection rights
- Eddystone transfer
- 2027 restart goal
- 2031 grid delay risk

NUCLEAR_SMR_GRID_POLICY
- Oklo
- Aurora powerhouse
- NRC Principal Design Criteria
- no revenue
- Q1 net loss
- cash runway
- commercial launch target
- nuclear AI power narrative
```

---

## 4. 성공사례

### 4-1. GE Vernova — R1 Loop 10의 가장 강한 `stage → price-path` 성공사례

GE Vernova는 R1에서 점수표가 가장 잘 맞은 사례다. AI 데이터센터와 전력망 수요가 실제 backlog, guidance, margin, 주가 반응으로 연결됐다. 회사는 2026년 매출 전망을 445억~455억 달러로 올렸고, adjusted EBITDA margin 전망도 12~14%로 상향했다. backlog는 130억 달러 증가해 1,630억 달러가 됐고, 발표 후 주가는 13% 넘게 상승했다. 전력·electrification 부문은 강했지만, wind 부문 매출 감소와 손실 확대, 2026년 tariff cost 2.5억~3.5억 달러는 RedTeam으로 남는다. ([Reuters][1])

```text
case_type:
POWER_EQUIPMENT_BACKLOG_TO_FCF
+
GAS_TURBINE_POWER_BACKLOG
+
STRUCTURAL_SUCCESS_ALIGNED
+
STRUCTURAL_SUCCESS_BUT_4B_WATCH

stage 포착:
Stage 1 = AI 데이터센터 전력수요, grid infrastructure demand
Stage 2 = revenue guide 상향, EBITDA margin guide 상향, backlog $163B
Stage 3 = 주가 +13% 이상, power/electrification profit 개선
Stage 4B = 주가가 이미 크게 리레이팅, consensus 과밀 가능성
Stage 4C-watch = wind loss, tariff cost
```

**가격경로 판정**

```text
매우 잘 맞음.
R1 점수표가 Stage 2→3를 정확히 잡았다.

정규화:
EPS/FCF revision + Visibility + Bottleneck 가중치 상향.
단, valuation room은 4B로 감점.
wind/tariff는 Stage 4C-watch로 유지.
```

---

### 4-2. Siemens Energy — FCF와 buyback으로 Stage 3 후보가 된 사례

Siemens Energy는 “수주잔고가 현금흐름과 자본환원으로 넘어가면 R1 점수가 올라간다”는 기준사례다. 회사는 2분기 pre-tax free cash flow가 42% 증가했고, AI 데이터센터 전력수요의 수혜를 받으면서 2026년 자사주 매입 규모를 기존 20억 유로에서 30억 유로로 앞당기기로 했다. 전체 60억 유로 buyback 프로그램의 총액은 유지됐다. ([Reuters][2])

```text
case_type:
POWER_EQUIPMENT_BACKLOG_TO_FCF_STAGE3_CANDIDATE

stage 포착:
Stage 1 = AI 데이터센터 전력수요
Stage 2 = raised outlook, demand visibility
Stage 3 후보 = FCF +42%, buyback acceleration
Stage 4B-watch = 전력장비 consensus 과밀 가능성
```

**가격경로 판정**

```text
사업 stage evidence는 강함.
이번 근거에서는 단순 수주보다 FCF·자본환원 evidence가 핵심이다.

정규화:
수주잔고만보다 FCF + 환원이 더 높은 Stage 3 근거.
Capital/FCF 전환 가중치 상향.
```

---

### 4-3. 미국 변압기 쇼티지 + LS Electric 525kV 계약 — Stage 2가 강한 사례

미국 전력망은 데이터센터, EV, 공장, 재생에너지, grid modernization 때문에 변압기 병목이 심해졌다. Wood Mackenzie 기준 2019~2025년 미국 GSU transformer 수요는 274%, substation transformer 수요는 116% 증가했고, 변압기 가격은 5년간 약 80% 상승했으며, 대형 변압기 lead time은 최대 4년까지 늘었다. 미국 개발사들은 수입, factory slot 선점, 중고 transformer refurbishing까지 쓰고 있다. ([Reuters][3])

이 macro bottleneck이 개별 계약으로 연결된 사례가 LS Electric이다. Reuters는 LS Electric이 2025년 11월 미국 utility와 3.12억 달러 규모 계약을 맺고, 미국 남동부 대형 데이터센터에 525kV 초고압 변압기를 2027~2029년 공급하기로 했다고 보도했다. 같은 기사에서 확인되는 포인트는 “전력망 부족”이라는 추상 뉴스가 아니라 **고객·전압·계약금액·납품기간·데이터센터 use-case**가 붙었다는 점이다. ([Reuters][3])

```text
case_type:
GRID_TRANSFORMER_SHORTAGE_STAGE1_2
+
GRID_EHV_TRANSFORMER_EXPORT_STAGE2

stage 포착:
Stage 1 = 미국 변압기 부족, 가격 상승, lead time 장기화
Stage 2 = LS Electric $312m 525kV 계약, 고객 use-case, 2027~2029 납품
Stage 3 = OP/EPS/FCF 전환, margin, 실제 가격경로 backfill 필요
```

**가격경로 판정**

```text
Stage 2 evidence는 강함.
하지만 계약 수주만으로 Stage 3는 아니다.

정규화:
GRID_TRANSFORMER_SHORTAGE와 GRID_EHV_TRANSFORMER_EXPORT 가중치 상향.
단, Stage 3는 OP/EPS revision과 price-path 확인 전까지 제한.
```

---

### 4-4. Hyundai Rotem Morocco ONCF — 계약금액은 강하지만 Stage 2에서 멈춰야 하는 철도 사례

현대로템은 모로코 국영철도 ONCF로부터 약 2.2조 원, 15.4억 달러 규모 이층 전동차 수주를 확보했다. Reuters는 이 계약이 현대로템 철도사업 사상 최대 수주라고 보도했다. ([Reuters][4])

```text
case_type:
RAIL_INFRASTRUCTURE_STAGE2

stage 포착:
Stage 1 = 모로코 철도 인프라 투자
Stage 2 = $1.54B 계약, 고객명 ONCF, 대형 수주 확인
Stage 3 = margin, warranty, financing, 납품스케줄, OP/EPS 상향 필요
```

**가격경로 판정**

```text
계약 visibility는 강함.
하지만 철도는 저마진·warranty·FX·local content 리스크가 있으므로
수주만으로 Stage 3 금지.

정규화:
RAIL_INFRASTRUCTURE는 Visibility 점수는 올리되,
EPS/FCF 점수는 margin 확인 전까지 cap.
```

---

### 4-5. Constellation / Three Mile Island restart — Big Tech PPA는 Stage 2, grid approval이 Stage 3 gate

Constellation은 Microsoft 데이터센터에 전력을 공급하기 위해 Three Mile Island의 Crane Clean Energy Center 재가동을 추진하고 있다. 핵심은 발전소 자체보다 FERC가 Eddystone gas plant의 grid injection rights를 Crane으로 이전할지 여부다. 이 승인이 없으면 grid connection이 2031년까지 밀릴 수 있고, Constellation은 2026년 6~7월 결정을 기대하고 있다. ([Reuters][5])

Q1 실적은 EPS와 매출이 예상치를 웃돌았지만, full-year guidance를 유지하자 주가는 2.3% 하락했다. 즉 PPA와 원전 재가동 narrative는 Stage 2지만, 규제·grid rights·guidance가 가격경로를 제한한다. ([Barron's][6])

```text
case_type:
NUCLEAR_EXISTING_PPA_RESTART_STAGE2
+
GRID_APPROVAL_AND_GUIDANCE_WATCH

stage 포착:
Stage 1 = AI 데이터센터 전력수요, 원전 재가동 narrative
Stage 2 = Microsoft PPA, FERC/grid injection rights pending
Stage 3 = FERC 승인, grid connection, restart CAPEX, EPS/FCF 확인 필요
Stage 4C-watch = grid delay, regulatory failure, guidance disappointment
```

**가격경로 판정**

```text
PPA alone은 가격경로를 완전히 방어하지 못했다.
Q1 beat에도 주가 -2.3%는 Stage 3 제한이 맞다는 신호.

정규화:
NUCLEAR_EXISTING_PPA_RESTART는 Watch-to-Green.
하지만 PPA보다 grid approval, regulatory timeline, CAPEX, guidance를 더 크게 본다.
```

---

## 5. 반례

### 5-1. Hanwha Aerospace — 방산 구조수요가 좋아도 대규모 증자·희석이면 stage 강등

한화에어로스페이스는 방산 수요와 생산능력 확대 narrative가 강하지만, 대규모 자본조달은 hard RedTeam이다. 회사가 3.6조 원 규모 증자를 발표한 뒤 금융감독원이 정정신고서 제출을 요구했고, initial filing이 투자자 의사결정에 필요한 정보를 충분히 제공하지 못했다고 밝혔다. 증자 발표 다음 날 주가는 13% 하락해 2016년 11월 이후 최악의 하루를 기록했다. ([Reuters][7])

이후 회사는 증자 규모를 2.3조 원으로 줄였지만, 금융감독원은 다시 수정 제출을 요구했다. 즉 방산 backlog가 좋아도 **use of proceeds, dilution, governance clarity**가 부족하면 Stage 3-Green을 막아야 한다. ([Reuters][8])

```text
case_type:
DEFENSE_GOVERNMENT_BACKLOG_WITH_CAPITAL_ALLOCATION_SHOCK

stage 포착:
Stage 1 = 방산 수요 증가, 해외 생산능력 확대
Stage 2 = capacity expansion plan
Stage 4C-watch = 3.6조 원 증자, FSS 정정요구, 주가 -13%
```

**가격경로 판정**

```text
Capital RedTeam이 실제 가격하락과 정확히 맞았다.
방산 backlog가 좋아도 dilution shock은 Stage를 강등시킨다.

정규화:
DEFENSE_CAPITAL_ALLOCATION_SHOCK를 hard gate로 유지.
share_issuance_amount, dilution, use_of_proceeds_clarity 필수.
```

---

### 5-2. HD Hyundai Heavy–Huntington Ingalls — MoA는 Stage 1~2, Green이 아니다

HD Hyundai Heavy Industries와 Huntington Ingalls는 미국 해군 보조함 공동건조를 위한 memorandum of agreement를 체결했다. 양사는 미국 내 새 조선소 건설 또는 기존 시설 인수를 포함한 공동투자 가능성을 검토한다. 이 흐름은 미국 조선산업 재건과 한국의 대미 조선 투자 pledge와 연결된다. ([Reuters][9])

하지만 이것은 아직 실제 vessel contract, 계약금액, 인도스케줄, yard CAPEX, margin이 확인된 Stage 3가 아니다. Reuters 보도에서도 관세협상 세부사항은 아직 확정되지 않았다고 설명됐다. ([Reuters][9])

```text
case_type:
DEFENSE_US_SHIPBUILDING_PLATFORM_STAGE1_2
+
MOU_MOA_NOT_CONTRACT

stage 포착:
Stage 1 = 미국 조선 재건, MASGA, summit narrative
Stage 2 후보 = MoA, joint investment exploration
Stage 3 금지 = vessel count, contract value, delivery schedule, margin 없음
```

**가격경로 판정**

```text
MoA/MoU는 price event가 될 수 있지만 구조적 Green은 아니다.

정규화:
DEFENSE_US_SHIPBUILDING_PLATFORM은 유지.
하지만 MoU/MoA only면 Stage 3 cap.
```

---

### 5-3. Siemens — orders는 강하지만 profit miss면 Stage 3 확정은 보류

Siemens는 데이터센터, utilities, defense 수요 덕분에 2026년 2분기 orders가 11% 증가했고, record order backlog는 1,240억 유로였다. 하지만 revenue는 197.6억 유로로 예상 201.4억 유로를 밑돌았고, industrial profit은 8% 감소해 29.7억 유로였다. 주가는 early trading에서 소폭 하락했다. ([Reuters][10])

```text
case_type:
ORDERS_STRONG_BUT_PROFIT_MISS

stage 포착:
Stage 1 = AI/data-center/defense demand
Stage 2 = order growth + record backlog
Stage 3 실패 = sales/profit miss, FX hit, margin pressure
가격경로 = early trading 약세
```

**가격경로 판정**

```text
수주·orders만으로 Stage 3를 올리면 false-positive.
profit/margin이 같이 가야 한다.

정규화:
수주잔고 visibility는 가점.
하지만 profit miss와 margin pressure가 있으면 EPS/FCF 점수 cap.
```

---

### 5-4. Oklo / SMR — 규제 milestone은 있어도 no revenue면 Stage 3 금지

Oklo는 advanced nuclear/SMR narrative가 강하지만 아직 no revenue 상태다. 2026년 1분기 net loss는 3,310만 달러로 전년보다 크게 확대됐고, Aurora powerhouse의 Principal Design Criteria 승인이라는 규제 milestone은 있었지만 상업운전 목표는 아직 2028년이다. 주가는 정규장에서 5.8% 하락했고 after-hours에서도 약세를 보였다. ([Barron's][11])

Investors.com도 Oklo가 Q1에서 operating cash burn과 CAPEX를 기록했고, 주가가 5.4% 하락했다고 보도했다. 즉 SMR은 정책·AI 전력수요·규제 milestone이 있어도, revenue·license·construction·financing이 실제로 이어지기 전까지 Stage 3는 금지다. ([Investors][12])

```text
case_type:
NUCLEAR_SMR_POLICY_MILESTONE_NO_REVENUE_WATCH

stage 포착:
Stage 1 = SMR/AI power/nuclear policy narrative
Stage 2 = regulatory design milestone
Stage 3 금지 = no revenue, commercial launch 전, cash burn
Stage 4C-watch = wider loss, financing need, certification delay
```

**가격경로 판정**

```text
규제 milestone은 Stage 2 후보지만 no revenue면 Stage 3 금지.
Q1 이후 주가 하락은 capital/cash burn gate가 필요하다는 신호.

정규화:
NUCLEAR_SMR_GRID_POLICY는 Watch/Red 유지.
existing PPA restart와 pre-revenue SMR을 분리한다.
```

---

### 5-5. GE Vernova도 wind loss·tariff cost가 남으면 4B/4C-watch

GE Vernova는 성공사례이지만, 완전 무위험 성공은 아니다. 같은 실적 발표에서 wind segment revenue는 23% 감소했고 손실은 약 3.82억 달러로 확대됐다. 또한 2026년 global tariffs 비용은 2.5억~3.5억 달러로 예상된다. ([Reuters][1])

```text
case_type:
POWER_EQUIPMENT_SUCCESS_WITH_SEGMENT_DRAG

stage 포착:
Stage 3 = power/electrification 성공
Stage 4C-watch = wind loss, tariff cost, segment drag
```

**가격경로 판정**

```text
주가는 +13% 이상으로 Stage 3를 인정했다.
하지만 R13 기준으로는 wind/tariff를 4B 이후 리스크로 추적해야 한다.

정규화:
성공사례도 RedTeam을 같이 저장한다.
good_case ≠ risk_free_case.
```

---

## 6. 지금 점수표로 실제 stage를 어떻게 포착했고, 주가상승·하락과 맞는지를 통한 점수비중정규화

R1 Loop 10부터 기본 점수표는 이렇게 재정규화한다.

```text
R1 v10 기본 점수표 = 100점

1. EPS/FCF·margin 전환 가능성             25점

2. 계약·수주잔고·고객 visibility           22점
   - 계약금액
   - 계약기간
   - 고객명
   - 납품스케줄
   - backlog
   - PPA
   - slot reservation

3. 병목·가격결정력                         18점
   - transformer lead time
   - turbine slot
   - grid bottleneck
   - defense capacity

4. capital discipline / 자본배분 / dilution 10점

5. disclosure confidence / RedTeam          9점

6. 시장 오해·리레이팅 gap                  9점

7. valuation room / 4B 여지                 7점

Hard RedTeam:
대규모 증자, dilution, FSS 정정요구, MoU-only, profit miss,
low-margin contract, wind loss, tariff cost, grid approval delay,
no revenue nuclear/SMR, contract cancellation, 회계·공시 문제
```

### 6-1. stage별 점수 cap

```text
Stage 1 cap:
최대 45점

조건:
- AI 전력수요 뉴스
- 전력망 부족 뉴스
- 방산 수요 증가
- 원전 재가동 narrative
- 미국 조선 재건 MoU
- 재건정책
- 철도투자 계획

예:
HD Hyundai-HII MoA
SMR policy milestone
우크라 재건회의
```

```text
Stage 2 cap:
최대 70점

조건:
- 계약금액
- 고객명
- 납품기간
- backlog
- PPA
- FERC/NRC pending milestone
- production slot reservation
- 대형 수주

예:
LS Electric $312m 525kV 계약
Hyundai Rotem $1.54B ONCF 계약
Constellation-Microsoft PPA
Siemens order/backlog 증가
```

```text
Stage 3:
70점 이상 가능

조건:
- OP/EPS/FCF 상향
- margin 개선
- 자본환원
- 수주잔고가 매출·현금흐름으로 전환
- 실제 가격경로 상승

예:
GE Vernova = Stage 2→3 price-path 성공
Siemens Energy = FCF + buyback으로 Stage 3 후보
```

```text
Stage 4B:
점수는 높지만 기대수익률 감점

조건:
- 전력설비·AI power·방산·원전 수혜가 consensus화
- 주가가 이미 크게 상승
- valuation이 EPS보다 먼저 확장
- 수주보다 multiple이 먼저 감

예:
GE Vernova after +13% and all-time high
전력장비 AI data-center basket 과열
```

```text
Stage 4C:
hard RedTeam

조건:
- 대규모 증자
- profit miss
- FSS 정정요구
- MoU-only를 계약으로 오분류
- grid approval 지연
- no revenue SMR
- tariff/wind loss
- low-margin/warranty risk
```

---

### 6-2. 실제 가격경로와 맞은 case / 안 맞은 case

| case                      |   점수표가 잡은 stage |                                          실제 가격경로 확인 | 판정                            | 정규화 조정                         |
| ------------------------- | --------------: | --------------------------------------------------: | ----------------------------- | ------------------------------ |
| GE Vernova                |       Stage 2→3 |                                          주가 +13% 이상 | 매우 잘 맞음                       | EPS/FCF·backlog·bottleneck 상향  |
| Siemens Energy            |      Stage 3 후보 |                      FCF +42%, buyback acceleration | 사업 stage 강함                   | Capital/FCF 가중치 상향             |
| U.S. transformer shortage |       Stage 1~2 | 수요 +274%/+116%, price +80%, lead time up to 4 years | bottleneck 포착 맞음              | transformer shortage 가중치 상향    |
| LS Electric 525kV         |         Stage 2 |              $312m, 2027~2029, data-center use-case | Stage 2 cap이 맞음               | 계약 visibility 상향, EPS cap 유지   |
| Hyundai Rotem ONCF        |         Stage 2 |                                      $1.54B 최대 철도수주 | Stage 2 cap이 맞음               | rail margin/warranty gate 강화   |
| Constellation TMI         |         Stage 2 |                                  Q1 beat에도 주가 -2.3% | PPA alone 부족                  | grid approval/guidance gate 강화 |
| Hanwha Aerospace          |  Stage 4C-watch |                                 증자 후 -13%, FSS 정정요구 | Capital RedTeam 매우 잘 맞음       | dilution penalty 강화            |
| HD Hyundai-HII            |       Stage 1~2 |                                            MoA only | Green 차단이 맞음                  | MoU/MoA cap 강화                 |
| Siemens                   |      Stage 2 실패 |                orders +11%, but revenue/profit miss | orders-only false-positive 방지 | profit/margin gate 강화          |
| Oklo                      | Stage 1~2 Watch |                     no revenue, loss 확대, 주가 -5%대 하락 | pre-revenue nuclear cap 맞음    | SMR no-revenue penalty 강화      |

---

### 6-3. R1 Loop 10 점수비중 재조정

이번 검증 결과 R1 점수표는 이렇게 조정한다.

```text
상향:
전력장비 backlog → margin → FCF 전환
gas turbine / grid equipment bottleneck
transformer shortage
EHV transformer export contract
capital return tied to FCF
grid/PPA approval gate
MoU vs contract 분리

유지:
방산 government backlog
철도 대형수주
원전 existing PPA restart
조선·naval MRO platform
재건 policy event

하향 또는 cap:
MoU/MoA-only
pre-revenue SMR
orders-only with profit miss
방산 증자·희석
PPA without grid approval
수주만 있고 margin 미확인
```

구체적으로는 이렇게 간다.

| 항목                    | Loop 9 감각 |                         Loop 10 조정 |
| --------------------- | --------: | ---------------------------------: |
| EPS/FCF·margin        |       최상위 |               더 강화. GE Vernova로 확인 |
| 계약·backlog visibility |        중요 |                 유지·상향. LS/Rotem/GE |
| 병목·가격결정력              |        중요 |     유지·상향. transformer/gas turbine |
| capital discipline    |        중요 |        더 상향. Hanwha/Siemens Energy |
| PPA·grid approval     |        보조 |         핵심 gate로 격상. Constellation |
| MoU/MoA               |     약한 가점 |                 Stage 1~2 cap으로 제한 |
| profit/margin miss    |        감점 |               hard cap. Siemens 사례 |
| no revenue nuclear    |     Watch |                Stage 3 금지. Oklo 사례 |
| valuation room        |        보조 | 4B 감점 강화. GE Vernova all-time high |

---

### 6-4. R1 Loop 10 archetype별 최종 stage 규칙

```text
GRID_TRANSFORMER_SHORTAGE:
Stage 1 = transformer shortage, lead time, 가격상승
Stage 2 = 계약금액 + 고객 + voltage + 납품기간
Stage 3 = OP/EPS/FCF 상향 + 가격경로 동행
Stage 4B = 전력장비 valuation 과열
Stage 4C = CAPA 정상화, 원가전가 실패, 납품지연
```

```text
POWER_EQUIPMENT_BACKLOG_TO_FCF:
Stage 1 = AI/data-center power demand
Stage 2 = orders/backlog/guidance
Stage 3 = FCF + margin + capital return + price reaction
Stage 4B = 주가 급등, consensus 과밀
Stage 4C = wind loss, tariff cost, project delay, order peak
```

```text
GAS_TURBINE_POWER_BACKLOG:
Stage 1 = data-center/gas power demand
Stage 2 = turbine backlog, slot reservation, capacity ramp
Stage 3 = margin + delivery + FCF + price-path
Stage 4B = turbine slot scarcity 과열
Stage 4C = project delay, tariff, gas policy shift
```

```text
DEFENSE_GOVERNMENT_BACKLOG:
Stage 1 = 재무장·방산수요
Stage 2 = 정부계약·수출계약·납품스케줄
Stage 3 = OP/EPS/FCF + 반복계약 + 자본효율
Stage 4B = K방산 consensus 과열
Stage 4C = 대규모 dilution, 수출허가, 납기지연
```

```text
DEFENSE_US_SHIPBUILDING_PLATFORM:
Stage 1 = 미국 조선 재건, MoU/MoA
Stage 2 = 실제 vessel/MRO contract, yard investment, schedule
Stage 3 = 반복 revenue + margin + FCF
Stage 4B = 미국 조선 재건 narrative 과열
Stage 4C = MoU-only, CAPEX 지연, 인력 병목, 법적 제한
```

```text
RAIL_INFRASTRUCTURE:
Stage 1 = 철도투자 계획
Stage 2 = 계약금액·고객·납품스케줄
Stage 3 = margin·warranty·financing 통과 + OP/EPS 상향
Stage 4B = 대형수주 뉴스 과열
Stage 4C = 저마진, warranty cost, FX, financing delay
```

```text
NUCLEAR_EXISTING_PPA_RESTART:
Stage 1 = Big Tech 전력수요·원전 재가동 narrative
Stage 2 = PPA + regulatory filing + grid rights plan
Stage 3 = FERC/NRC 승인 + restart CAPEX + EPS/FCF
Stage 4B = AI nuclear trade 과열
Stage 4C = grid delay, regulatory failure, CAPEX overrun
```

```text
NUCLEAR_SMR_GRID_POLICY:
Stage 1 = SMR/advanced nuclear policy
Stage 2 = regulatory design milestone, pilot, customer MoU
Stage 3 = revenue + construction + financing + certification 전까지 금지
Stage 4B = pre-revenue nuclear valuation 과열
Stage 4C = cash burn, certification delay, funding gap
```

---

# R1 Loop 10 결론

이번 R1 Loop 10의 핵심은 이거다.

```text
R1은 “수주가 있다”와 “수주가 EPS/FCF로 바뀐다”를 분리하는 라운드다.
```

```text
Stage 포착이 잘 맞은 사례:
GE Vernova = backlog + guidance + margin + 주가 +13% 이상
Siemens Energy = FCF +42% + buyback acceleration, Stage 3 후보
U.S. transformer shortage = 수요·가격·lead time 병목 확인
LS Electric = $312m 525kV transformer contract, Stage 2
Hyundai Rotem = $1.54B Morocco ONCF rail order, Stage 2
Constellation = Microsoft PPA + FERC grid rights, Stage 2

RedTeam이 가격·사업경로와 잘 맞은 사례:
Hanwha Aerospace = 대규모 증자·FSS 정정요구·주가 -13%
HD Hyundai-HII = MoA only, Green 금지
Siemens = orders +11%에도 revenue/profit miss
Oklo = no revenue SMR, loss 확대, 주가 하락
GE Vernova = 성공사례지만 wind loss·tariff cost watch
```

**R1 Loop 10 점수정규화의 핵심 문장:**

> 산업재·수주·인프라는 “수주”, “전력망”, “방산”, “원전”, “철도”, “미국 조선 재건”이라는 이름이 아니라 **계약금액, 고객명, 계약기간, backlog, 납품스케줄, margin, OP/EPS/FCF 전환, 자본배분, grid/regulatory approval, dilution, MoU-only 여부, 실제 가격경로**로 봐야 한다.
> 이번 Loop 10에서는 `GE Vernova`가 Stage 2→3 포착과 주가 상승이 가장 잘 맞은 사례이고, `Hanwha Aerospace`, `Siemens`, `Oklo`, `HD Hyundai-HII MoA-only`가 R1 RedTeam이 실제 가격·사업경로와 맞는 반례다.

다음 순서는 **R2 — AI·반도체·전자부품 Loop 10**다.

[1]: https://www.reuters.com/business/energy/ge-vernova-lifts-annual-revenue-forecast-data-center-demand-2026-04-22/?utm_source=chatgpt.com "GE Vernova lifts 2026 outlook as AI boom fuels power equipment demand"
[2]: https://www.reuters.com/sustainability/climate-energy/siemens-energy-accelerates-share-buyback-after-q2-cash-flow-jumps-2026-05-12/?utm_source=chatgpt.com "Siemens Energy accelerates share buyback after Q2 cash flow jumps"
[3]: https://www.reuters.com/business/energy/us-power-transformer-buyers-scramble-imports-factory-slots--reeii-2026-05-11/?utm_source=chatgpt.com "US power transformer buyers scramble for imports, factory slots"
[4]: https://www.reuters.com/markets/deals/hyundai-rotem-wins-15-billion-order-moroccos-national-rail-operator-2025-02-26/?utm_source=chatgpt.com "Hyundai Rotem wins $1.5 billion order from Morocco's national rail operator"
[5]: https://www.reuters.com/business/energy/us-may-decide-three-mile-island-restart-june-constellation-execs-say-2026-05-11/?utm_source=chatgpt.com "US may decide on Three Mile Island restart in June, Constellation execs say"
[6]: https://www.barrons.com/articles/constellation-energy-earnings-stock-price-d3b7c846?utm_source=chatgpt.com "Constellation Energy Beats Earnings Estimates. Its Outlook Pulls the Stock Lower."
[7]: https://www.reuters.com/business/aerospace-defense/south-korea-market-watchdog-orders-hanwha-aerospace-revise-share-issuance-plan-2025-03-27/?utm_source=chatgpt.com "S. Korea watchdog blocks Hanwha Aerospace $2.5 billion capital raising plan"
[8]: https://www.reuters.com/business/aerospace-defense/south-korea-watchdog-orders-hanwha-aerospace-resubmit-share-issue-plan-2025-04-17/?utm_source=chatgpt.com "South Korea watchdog orders Hanwha Aerospace to resubmit share issue plan"
[9]: https://www.reuters.com/world/asia-pacific/hd-hyundai-heavy-huntington-ingalls-jointly-build-us-navy-auxiliary-ships-2025-10-26/?utm_source=chatgpt.com "HD Hyundai Heavy, Huntington Ingalls to jointly build U.S. navy auxiliary ships"
[10]: https://www.reuters.com/business/siemens-q2-profit-misses-forecasts-orders-surge-2026-05-13/?utm_source=chatgpt.com "Siemens orders rise more than expected despite Iranian war tension"
[11]: https://www.barrons.com/articles/oklos-regulatory-nuclear-earnings-stock-8228360e?utm_source=chatgpt.com "Oklo's Losses Widen. A Major Regulatory Win Keeps the Nuclear Dream Alive."
[12]: https://www.investors.com/news/oklo-earnings-q1-oklo-stock-nuclear-stocks/?utm_source=chatgpt.com "Nuclear Reactor Startup Oklo Reports Wider Losses Amid AI Boom"

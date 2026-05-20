좋아. **R13 Loop 6까지 끝났으니, 규칙대로 다시 R1로 돌아와서 이번은 R1 Loop 7 — 산업재·수주·인프라**다.

이번부터는 네가 바꾼 포맷대로 **“점수표가 실제 stage를 어떻게 포착했고, 그 stage가 실제 주가 상승·하락과 맞았는지”**를 6번에 더 크게 넣는다.

서생원 원칙은 그대로 유지한다. 즉 R1에서도 단순히 “수주가 많다”, “AI 전력망 수혜다”, “방산 수출이다”가 아니라, **EPS/FCF 체급 변화 → 시장의 과거 프레임 오해 → 밸류에이션 리레이팅 → 실제 가격경로 검증**이 같이 가야 한다. 서생원식 핵심은 “폭발적인 EPS 상승 후 밸류에이션 리레이팅되는 종목”이고, 단순 저PER·저PBR·테마가 아니라 구조 변화와 이익 체급 변화가 같이 나와야 한다는 점이다.

R1은 Theme Tag Map상 전력설비, 전선·케이블, 피팅밸브, 조선, 방산, 원전, 철도, 건설기계, 우크라 재건, 네옴시티를 흡수한다. 여기서는 성공 사례가 많이 나올 수 있지만, 수주 뉴스만으로는 부족하고 **계약질 + 마진 + EPS 상향 + 주가 리레이팅**이 같이 가야 한다는 정규화 원칙이 이미 잡혀 있다.

또 Checkpoint 20 원칙상 OpenDART list 공시만으로는 부족하다. 단일판매·공급계약, 신규시설투자, 잠정실적, 유상증자, 전환사채, 감사의견, 거래정지, 계약 해지·정정 같은 watch disclosure는 detail에서 계약금액, 계약기간, 상대방, 매출 대비 계약금액, OP YoY, 희석률 등을 실제 파싱해야 하고, 값이 없으면 만들면 안 된다.

---

# R1 Loop 7. 산업재·수주·인프라

## 1. 이번 라운드 대섹터

```text
R1 = 산업재·수주·인프라
Loop 7 목표 =
전력망·변압기·가스터빈·중전압 장비·방산·철도·조선·원전·재건 후보를
“수주 뉴스”가 아니라
stage 포착 + 실제 가격경로 검증 + 점수비중 재조정으로 다시 정규화
```

이번 R1 Loop 7의 핵심 질문은 이거다.

```text
이 수주와 backlog가 실제 EPS/FCF 체급 변화를 만들었는가?
아니면 Stage 1 뉴스, Stage 2 수주, Stage 4B 과열, Stage 4C 자본조달 shock인가?
```

R1에서는 특히 이 구분이 중요하다.

```text
Stage 1:
전력망 부족, AI 데이터센터 전력수요, 방산 재무장, 재건 정책 같은 산업 뉴스

Stage 2:
계약금액, 계약기간, 고객사, 납품시기, backlog, 공식 guidance 확인

Stage 3:
OP/EPS/FCF 상향, margin 개선, 자본환원, valuation frame 전환, 가격경로 동행

Stage 4B:
모두가 수혜를 인정하고 valuation이 이미 확장된 구간

Stage 4C:
계약 취소, 납기 지연, 저마진, dilution, 회계·규제·자본배분 shock
```

R1 Loop 7에서는 **전력설비·가스터빈·전력장비** 쪽은 Stage 2~3 성공사례가 실제로 나오고 있다. 반대로 **방산·미국 조선·철도·재건**은 수주나 MoU는 강하지만, capital allocation, margin, 실제 매출 인식 전까지는 Stage 3를 제한해야 한다.

---

## 2. 대상 canonical archetype

| canonical archetype                | Loop 7 판정 방향   | stage 포착 핵심                                   |
| ---------------------------------- | -------------- | --------------------------------------------- |
| `GRID_TRANSFORMER_SHORTAGE`        | Green 후보 유지    | transformer lead time, price, demand growth   |
| `GRID_EHV_TRANSFORMER_EXPORT`      | Stage 2 강함     | 525kV/765kV, 계약금액, 고객, 납품기간                   |
| `GRID_SUPPLY_SLOT_PREBUY`          | Watch-to-Green | 생산 slot 선점, 장기계약, 선수금                         |
| `GRID_MEDIUM_VOLTAGE_EXPANSION`    | Watch-to-Green | switchgear/MV CAPA, utility/data-center order |
| `POWER_EQUIPMENT_BACKLOG_TO_FCF`   | Stage 3 후보     | backlog → FCF → buyback/dividend              |
| `GAS_TURBINE_POWER_BACKLOG`        | Stage 2~3 후보   | turbine backlog, reservation, margin guide    |
| `AI_DATA_CENTER_POWER_EQUIPMENT`   | Green 가능       | data-center orders, guidance, OPM             |
| `DEFENSE_GOVERNMENT_BACKLOG`       | Green 가능       | 정부고객, 다년계약, 납품스케줄                             |
| `DEFENSE_CAPITAL_ALLOCATION_SHOCK` | RedTeam gate   | 유상증자, dilution, FSS 정정요구                      |
| `DEFENSE_US_SHIPBUILDING_PLATFORM` | Stage 1~2      | MoU/MoA는 가능성, 실제 계약 전 Green 금지                |
| `SHIPBUILDING_OFFSHORE_BACKLOG`    | Green 가능       | 선가, 저가수주 소진, 후판가, 인도마진                        |
| `SHIPBUILDING_NAVAL_MRO`           | Watch-to-Green | MRO 자격, 반복 수리계약, margin                       |
| `RAIL_INFRASTRUCTURE`              | Stage 2 후보     | 대형계약, financing, warranty, margin             |
| `NUCLEAR_EXISTING_PPA_RESTART`     | Watch-to-Green | 장기 PPA, 재가동 CAPEX, grid rights                |
| `NUCLEAR_SMR_GRID_POLICY`          | Watch/Red      | 고객확보, 비용, 허가, financing                       |
| `GEOPOLITICAL_RECONSTRUCTION`      | Event/Watch    | 실제 계약·financing·착공 전 Green 금지                 |
| `DISCLOSURE_CONFIDENCE_CAP`        | 공통 cap         | detail 없으면 Stage 3 제한                         |

---

## 3. deep sub-archetype

```text
GRID_TRANSFORMER_SHORTAGE
- GSU transformer
- substation transformer
- EHV transformer
- transformer lead time
- transformer price increase
- factory slot pre-buying
- copper / GOES input
- grid modernization
- AI data center power demand

GRID_EHV_TRANSFORMER_EXPORT
- 525kV transformer
- 765kV transformer
- U.S. utility customer
- data-center use-case
- 2027~2029 delivery
- South Korea / Turkey import supply
- contract amount
- delivery schedule

POWER_EQUIPMENT_BACKLOG_TO_FCF
- order backlog
- FCF jump
- buyback acceleration
- data center demand
- grid equipment
- gas turbine
- capital return
- margin guidance

GAS_TURBINE_POWER_BACKLOG
- turbine slot reservation
- data-center power demand
- grid infrastructure
- power segment profit
- wind segment loss
- tariff cost
- reservation agreements

DEFENSE_GOVERNMENT_BACKLOG
- K9
- K10
- 천무
- K2
- 탄약
- NATO 재무장
- government customer
- export license
- delivery batch

DEFENSE_CAPITAL_ALLOCATION_SHOCK
- large share issuance
- dilution
- overseas factory CAPEX
- use of proceeds unclear
- FSS correction request
- shareholder value dilution

DEFENSE_US_SHIPBUILDING_PLATFORM
- Huntington Ingalls
- HD Hyundai Heavy
- U.S. Navy auxiliary ships
- MoU / MoA
- U.S. shipyard investment
- workforce bottleneck
- legal/political condition

RAIL_INFRASTRUCTURE
- ONCF
- Morocco rail
- double-decker train
- delivery schedule
- financing
- warranty
- FX
- local content

NUCLEAR_EXISTING_PPA_RESTART
- Big Tech PPA
- existing nuclear plant
- restart CAPEX
- grid injection rights
- FERC/PJM approval

GEOPOLITICAL_RECONSTRUCTION
- Ukraine reconstruction
- port concession
- power grid rebuild
- transformer shelter
- financing
- construction start
```

---

## 4. 성공사례

### 4-1. 미국 변압기 쇼티지 + LS Electric 525kV 계약

미국 전력망은 데이터센터, EV, 공장, 재생에너지, grid modernization 때문에 변압기 병목이 실제로 커졌다. Reuters는 2019~2025년 미국 GSU transformer 수요가 274%, substation power transformer 수요가 116% 증가했고, 변압기 가격은 5년간 약 80% 올랐으며, 대형 변압기 lead time은 최대 4년까지 늘었다고 보도했다. 같은 보도에서 LS Electric은 2025년 11월 미국 utility와 3.12억 달러 규모 525kV 초고압 변압기 공급계약을 맺어 미국 남동부 대형 데이터센터에 2027~2029년 공급하기로 했다. ([Reuters][1])

```text
case_type:
GRID_EHV_TRANSFORMER_EXPORT_STAGE2

stage 포착:
Stage 1 = 미국 변압기 부족, 가격 상승, lead time 장기화
Stage 2 = LS Electric $312m 525kV 계약, 고객 use-case, 납품기간 확인
Stage 3 = 아직 OP/EPS/FCF 전환과 margin 확인 필요

가격경로 판정:
sector stage는 강하게 맞음.
개별 LS Electric은 계약 detail은 강하지만,
이 답변에서 확인된 출처만으로는 stage2_date 이후 OHLCV MFE/MAE를 확정하지 않음.
따라서 price_validation_status = price_backfill_required.
```

**정규화 결론**

```text
GRID_TRANSFORMER_SHORTAGE 점수는 유지/상향.
GRID_EHV_TRANSFORMER_EXPORT는 일반 전력설비 뉴스보다 높은 Visibility 점수 부여.
하지만 Stage 3는 OP/EPS revision, margin, FCF, 실제 가격경로 backfill 전까지 제한.
```

---

### 4-2. GE Vernova — backlog, guidance, 주가 반응이 같이 나온 R1 성공사례

GE Vernova는 R1 Loop 7에서 가장 명확한 **Stage 2 → Stage 3 후보**다. Reuters는 GE Vernova가 AI 데이터센터와 grid infrastructure 수요 덕분에 2026년 매출 전망을 445억~455억 달러로, adjusted EBITDA margin 전망을 12~14%로 올렸고, backlog가 1,630억 달러까지 증가했다고 보도했다. 발표 후 주가는 13% 넘게 올라 사상 최고가를 기록했다. 동시에 wind segment 손실과 2026년 2.5억~3.5억 달러 tariff cost는 RedTeam으로 남는다. ([Reuters][2])

IBD 보도 기준으로도 GE Vernova는 Q1에서 data-center related electrification orders 24억 달러를 기록했고, backlog는 1,630억 달러, 주가는 실적 후 13.6% 상승했으며 2024년 4월 분사 이후 235% 상승한 상태라고 정리됐다. 이건 구조적 성공과 4B 감시가 동시에 붙는 사례다. ([Investors][3])

```text
case_type:
POWER_EQUIPMENT_BACKLOG_TO_FCF / GAS_TURBINE_POWER_BACKLOG
+
STRUCTURAL_SUCCESS_BUT_4B_WATCH

stage 포착:
Stage 1 = AI 데이터센터 전력수요와 grid infrastructure 수요
Stage 2 = revenue guidance 상향, EBITDA margin guide 상향, backlog 증가
Stage 3 = 주가 +13% 이상, backlog와 실적이 price-path와 동행
Stage 4B = 분사 이후 큰 폭 상승, valuation crowding 가능성

가격경로 판정:
score가 잡은 Stage 2~3가 실제 주가 상승과 잘 맞았다.
단, wind loss와 tariff cost 때문에 RedTeam overlay 필요.
```

**정규화 결론**

```text
GE Vernova형 case는 R1 점수표에서
EPS/FCF + Visibility + Bottleneck을 모두 상향한다.

하지만 이미 주가가 크게 리레이팅된 경우
Valuation/Mispricing 점수는 낮추고,
Stage 4B flag를 켠다.
```

---

### 4-3. Siemens Energy — backlog가 FCF와 buyback으로 넘어간 사례

Siemens Energy는 **수주잔고가 현금흐름과 자본환원으로 넘어갈 때 R1 점수가 어떻게 올라가는지** 보여준다. Reuters는 Siemens Energy가 AI 데이터센터 전력수요 수혜 속에서 2분기 pre-tax free cash flow가 42% 증가했고, 기존 자사주 매입 프로그램에서 2026년 매입 규모를 20억 유로에서 30억 유로로 앞당기겠다고 보도했다. ([Reuters][4])

또 Siemens는 별도 기사에서 미국 data center, utilities, defense 수요에 힘입어 2026년 1~3월 주문이 11% 증가했고, record order backlog가 1,240억 유로였으며, 연간 comparable revenue growth 6~8%와 EPS 10.70~11.10유로 가이던스를 유지했다. 다만 산업이익은 8% 감소했고, 일부 FX·one-off 효과도 있어 사업별 분리를 계속해야 한다. ([Reuters][5])

```text
case_type:
POWER_EQUIPMENT_BACKLOG_TO_FCF

stage 포착:
Stage 1 = AI/data-center 전력장비 수요
Stage 2 = 주문 증가, record backlog, guidance 유지
Stage 3 후보 = FCF +42%, buyback acceleration

가격경로 판정:
현금흐름과 자본환원 증거는 강하다.
다만 이 답변에서 인용한 Reuters 기사만으로는 당일 주가반응을 확정하지 않는다.
따라서 Stage 3 evidence는 높지만 price_validation_status = needs_OHLCV_backfill.
```

**정규화 결론**

```text
R1에서 buyback/dividend는 단독 가점이 아니라,
수주잔고 → FCF → 자본환원으로 이어질 때 Capital/FCF 점수를 높인다.

Siemens Energy형은 Stage 3 후보.
단, price-path backfill 전까지 확정 Green이 아니라 high-confidence candidate.
```

---

### 4-4. 현대 로템 모로코 철도 수주 — 큰 Stage 2, 아직 Stage 3 아님

현대로템은 모로코 국영철도 ONCF로부터 약 2.2조 원, 15.4억 달러 규모 이층 전동차 수주를 확보했다. Reuters는 이 계약이 현대로템 철도사업 사상 최대 수주라고 보도했다. ([Reuters][6])

```text
case_type:
RAIL_INFRASTRUCTURE_STAGE2

stage 포착:
Stage 1 = 모로코 철도 인프라 투자
Stage 2 = $1.54B 계약, 회사 철도사업 최대 수주
Stage 3 = 납품기간, margin, financing, warranty, OP/EPS 상향 확인 전까지 제한

가격경로 판정:
계약 크기와 visibility는 강하다.
하지만 이 출처만으로는 수주 후 주가 MFE/MAE를 확정하지 않음.
price_validation_status = price_backfill_required.
```

**정규화 결론**

```text
RAIL_INFRASTRUCTURE는 Visibility 점수는 올린다.
하지만 철도는 margin, warranty, FX, financing을 확인하기 전까지 EPS/FCF 점수 상한을 둔다.
```

---

## 5. 반례

### 5-1. 한화에어로스페이스 — 좋은 방산 backlog도 dilution shock을 맞으면 stage가 강등된다

한화에어로스페이스는 방산 구조수요와 backlog가 강하지만, 대규모 자본조달은 R1의 hard RedTeam이다. Reuters는 한화에어로스페이스가 처음 3.6조 원 규모 증자를 추진했다가 금융감독원의 정정 요구 이후 약 2.3조 원, 16억 달러 규모로 축소했다고 보도했다. 금융감독원은 자본조달이 회사 구조조정 전략과 어떻게 맞물리는지 더 명확한 설명이 필요하다고 봤다. ([Reuters][7])

FT 보도 기준으로는 3.6조 원 share sale 발표 이후 주가가 13% 하락했다. 이건 “방산 구조가 좋다”와 “주주가치 희석이 price-path를 깨뜨린다”가 동시에 존재하는 사례다. ([Financial Times][8])

```text
case_type:
DEFENSE_GOVERNMENT_BACKLOG_WITH_CAPITAL_ALLOCATION_SHOCK

stage 포착:
Stage 1~2 = 방산 수요, 해외 생산능력 확대, 매출/OP 성장 계획
Stage 4C-watch = 대규모 증자, dilution, FSS 정정요구, 주가 급락

가격경로 판정:
Capital/FCF penalty가 실제 주가 하락과 잘 맞았다.
좋은 backlog라도 자본배분 shock이 나오면 stage_after_redteam을 강등해야 한다.
```

**정규화 결론**

```text
DEFENSE_GOVERNMENT_BACKLOG 점수는 유지하되,
share_issuance_amount / dilution_flag / use_of_proceeds_clarity가 나쁘면
Capital 점수와 Valuation 점수를 강하게 깎는다.

한화에어로스페이스형은:
수요 구조는 Green 후보
자본배분은 4C-watch
```

---

### 5-2. HD현대중공업–Huntington Ingalls — MoU/MoA는 Stage 1~2이지 Green이 아니다

HD Hyundai Heavy Industries와 Huntington Ingalls는 미국 해군 보조함 공동건조 협약을 맺었다. Reuters는 이 협약이 미국 군함 건조 협력, 미국 조선산업 재건, 한국의 미국 조선업 투자 약속과 연결되어 있다고 보도했다. 그러나 이 단계는 아직 MoA/MoU와 potential joint investment 구조이지, 반복 매출·margin·vessel count·공식 계약금액이 확인된 Stage 3는 아니다. ([Reuters][9])

```text
case_type:
DEFENSE_US_SHIPBUILDING_PLATFORM_STAGE1_2

stage 포착:
Stage 1 = 미국 조선 재건, MoU/MoA, summit narrative
Stage 2 후보 = 실제 vessel contract, yard investment, schedule 확인 시
Stage 3 = 반복 MRO/newbuild revenue + margin + FCF 확인 시

가격경로 판정:
지금은 price 움직임이 있어도 event premium으로 분리해야 한다.
MoU-only는 Green 금지.
```

**정규화 결론**

```text
DEFENSE_US_SHIPBUILDING_PLATFORM은 유지.
하지만 MoU/MoA only면 total score cap을 둔다.

contract_value
vessel_count
delivery_schedule
margin
yard_CAPEX
US_workforce_bottleneck

이 확인되기 전까지 Stage 3 제한.
```

---

### 5-3. 전력장비 성공사례도 wind/tariff 같은 legacy drag가 있으면 점수 제한

GE Vernova는 강한 성공사례지만 wind segment 손실과 tariff cost가 동시에 남아 있다. Reuters는 GE Vernova의 wind segment가 부진했고, 2026년 2.5억~3.5억 달러 tariff cost를 예상한다고 보도했다. ([Reuters][2])

```text
case_type:
POWER_EQUIPMENT_SUCCESS_WITH_SEGMENT_DRAG

교훈:
전력장비 수혜가 진짜여도
legacy wind loss, tariff, segment mix가 있으면
Stage 3 점수는 유지하되 4B/4C-watch overlay를 붙인다.
```

---

## 6. 지금 점수표로 실제 stage를 어떻게 포착했고, 주가 상승·하락과 맞았는지에 따른 점수비중 정규화

이번 R1 Loop 7부터 R1 기본 점수표는 아래처럼 정규화한다.

```text
R1 v7 기본 점수표 = 100점

1. EPS/FCF revision 가능성        25점
2. 계약·수주잔고 visibility        24점
3. 병목·가격결정력                 20점
4. 시장 오해·리레이팅 gap          12점
5. valuation room / 4B 여지         8점
6. capital discipline / FCF 전환     6점
7. 정보 신뢰도 / disclosure detail   5점

Hard RedTeam:
회계·공시·계약취소·대규모 dilution·낮은 계약질·저마진·납기실패·정책 shock은 별도 gate.
```

### 6-1. stage별 점수 cap

```text
Stage 1 cap:
최대 45점

조건:
- 산업 뉴스, 정책 뉴스, MoU, 공급부족 macro evidence만 있음
- 개별 계약금액·고객·납품기간 없음

예:
미국 변압기 부족 뉴스만 있는 전력설비 관련주
미국 조선 재건 MoU
우크라 재건 MOU
```

```text
Stage 2 cap:
최대 70점

조건:
- 계약금액, 고객, 기간, 납품스케줄, backlog, guidance 중 일부 확인
- 하지만 OP/EPS/FCF 전환은 아직 불충분

예:
LS Electric $312m 525kV transformer 계약
현대로템 $1.54B 모로코 철도 수주
HD Hyundai-HII MoU는 Stage 2가 아니라 Stage 1.5에 가까움
```

```text
Stage 3:
70점 이상 가능

조건:
- 수주/backlog가 OP/EPS/FCF 상향으로 연결
- margin이나 FCF가 확인
- 실제 주가경로가 Stage 2 이후 우상향 또는 즉시 반응

예:
GE Vernova revenue/margin guide 상향 + backlog + 주가 +13% 이상
Siemens Energy FCF +42% + buyback acceleration, 단 가격경로 backfill 필요
```

```text
Stage 4B:
점수 자체는 높을 수 있지만 기대수익률 감점

조건:
- 성공 논리가 이미 시장에 널리 알려짐
- 주가가 이미 크게 리레이팅
- valuation room이 줄어듦

예:
GE Vernova 분사 이후 큰 폭 상승
전력장비 AI 수혜 consensus 과밀
```

```text
Stage 4C:
hard RedTeam

조건:
- 대규모 dilution
- 계약 취소
- 납기·품질·회계·공시 문제
- 저마진 수주
- legacy segment 손실
- 정책·관세 shock

예:
한화에어로스페이스 share sale / FSS 정정요구 / 주가 하락
```

---

### 6-2. 실제 가격경로와 맞은 case / 안 맞은 case

| case                  |         점수표가 잡은 stage |                                실제 가격경로 확인 | 판정           | 정규화 조정                                      |
| --------------------- | --------------------: | ----------------------------------------: | ------------ | ------------------------------------------- |
| GE Vernova            |             Stage 2→3 |                         발표 후 주가 13% 이상 상승 | 잘 맞음         | EPS/FCF, Visibility, Bottleneck 가중치 유지·상향   |
| Siemens Energy        |            Stage 3 후보 | FCF·buyback 증거는 강함, 당일 가격은 추가 backfill 필요 | 부분 확인        | Capital/FCF 가중치 상향, price_backfill_required |
| LS Electric 525kV     |               Stage 2 |          계약 detail은 강함, 주가경로는 backfill 필요 | 아직 미완        | Visibility 상향, EPS/FCF cap 유지               |
| Hyundai Rotem Morocco |               Stage 2 |          계약 detail은 강함, 주가경로는 backfill 필요 | 아직 미완        | Rail은 margin/financing 확인 전 cap             |
| Hanwha Aerospace      | Stage 2 구조 + 4C-watch |                     share sale 뉴스 후 주가 하락 | RedTeam 잘 맞음 | Capital penalty 강화                          |
| HD Hyundai-HII        |             Stage 1~2 |                              MoU/MoA only | Green 차단이 맞음 | Event/MoU score cap 강화                      |

GE Vernova는 점수표가 제대로 잡은 케이스다. backlog, guidance, margin, data-center demand가 동시에 나오자 주가가 즉시 반응했다. 이런 case는 R1에서 **EPS/FCF revision, 계약 visibility, 병목·가격결정력**을 높은 가중치로 유지하는 근거가 된다. ([Reuters][2])

Siemens Energy는 FCF와 buyback으로 stage quality가 올라가는 케이스다. 다만 기사에서 명시된 주가 반응보다는 FCF·자본환원 evidence가 핵심이므로, agent는 OHLCV backfill로 MFE/MAE를 확인해야 한다. ([Reuters][4])

LS Electric과 현대로템은 Stage 2 계약 evidence가 강하지만, 서생원식으로는 아직 “수주 뉴스” 단계다. 계약금액·기간·고객은 좋지만, OP/EPS/FCF와 실제 가격경로를 backfill해야 Stage 3로 올라간다. ([Reuters][1])

한화에어로스페이스는 RedTeam이 실제 가격경로와 맞은 케이스다. 방산 backlog와 구조수요가 좋아도 대규모 증자·희석·FSS 정정요구가 나오면 Stage 3-Green을 유지하면 안 된다. ([Reuters][7])

---

### 6-3. R1 Loop 7 점수비중 재조정

이번 검증 결과 R1 점수표는 이렇게 조정한다.

```text
상향:
계약·수주잔고 visibility      +2
EPS/FCF revision             +2
Capital/FCF 전환             +2

유지:
병목·가격결정력
시장 오해·리레이팅 gap

하향 또는 cap:
MoU/MoA only
정책·재건 event only
철도 대형계약의 margin 미확인
방산 현지생산의 dilution risk
전력장비 성공 후 4B valuation room
```

구체적으로는 이렇게 간다.

| 항목                    | 기존 감각 |                        Loop 7 조정 |
| --------------------- | ----: | -------------------------------: |
| EPS/FCF revision      |    중요 |             더 중요. Stage 3 승격의 핵심 |
| 계약 visibility         |    중요 |            더 중요. 단, detail 있어야 함 |
| 병목·가격결정력              |    중요 | 유지. transformer/gas turbine에서 강함 |
| 리레이팅 gap              |    중요 |                   유지. 하지만 4B면 감점 |
| valuation room        |    보조 |               이미 급등한 전력장비는 감점 강화 |
| capital discipline    |    보조 |     상향. Siemens는 +, Hanwha는 - 사례 |
| disclosure confidence |    보조 |        강화. detail 없으면 Stage 3 제한 |

---

### 6-4. R1 Loop 7 최종 stage 규칙

```text
GRID/EHV transformer:
Stage 1 = transformer shortage macro
Stage 2 = 계약금액 + 고객 + voltage + 납품기간
Stage 3 = OP/EPS/FCF 상향 + 가격경로 동행
Stage 4B = 전력장비주 valuation 과열
Stage 4C = 납품지연, 저마진, CAPA 정상화, 원가전가 실패
```

```text
Power equipment / gas turbine:
Stage 1 = AI/data-center power demand
Stage 2 = orders/backlog/guidance
Stage 3 = FCF + margin + capital return + price reaction
Stage 4B = 주가 급등, consensus 과밀
Stage 4C = wind loss, tariff, project delay, order peak
```

```text
Defense:
Stage 1 = NATO 재무장, 방산 수요
Stage 2 = 정부계약, 수출계약, 납품스케줄
Stage 3 = OP/EPS/FCF + 반복계약 + 환원 또는 자본효율
Stage 4B = K방산 narrative 과밀
Stage 4C = 대규모 dilution, 수출허가 문제, 납기 지연
```

```text
Rail:
Stage 1 = 철도 투자계획
Stage 2 = 계약금액·고객·납품스케줄
Stage 3 = margin·warranty·financing 통과 + OP/EPS 상향
Stage 4B = 대형수주 뉴스 과열
Stage 4C = 저마진, warranty cost, FX, financing delay
```

```text
U.S. shipbuilding / naval MRO:
Stage 1 = MoU/MoA, 정책, summit narrative
Stage 2 = 실제 vessel/MRO contract, yard investment, schedule
Stage 3 = 반복 revenue + margin + FCF
Stage 4B = 미국 조선 재건 narrative 과열
Stage 4C = MoU-only, CAPEX 지연, 인력 병목, 법적 제한
```

---

# R1 Loop 7 결론

이번 R1 Loop 7의 핵심은 이거다.

```text
전력설비·가스터빈·전력장비:
실제 Stage 2~3 사례가 나오고 있다.
GE Vernova는 점수표와 가격경로가 잘 맞은 성공사례다.

Siemens Energy:
수주잔고가 FCF와 자본환원으로 넘어간 좋은 후보지만,
가격경로 backfill이 필요하다.

LS Electric / Hyundai Rotem:
계약 evidence는 좋지만 Stage 2다.
OP/EPS/FCF와 가격경로 검증 전까지 Stage 3-Green 금지.

Hanwha Aerospace:
방산 구조수요가 좋아도 dilution shock이 나오면 stage 강등.
Capital penalty가 실제 주가 하락과 잘 맞았다.

HD Hyundai-HII:
미국 조선 재건 narrative는 좋지만 MoU/MoA only는 Event/Watch다.
```

**R1 Loop 7 점수정규화의 핵심 문장:**

> 산업재·수주·인프라는 “수주가 있다”가 아니라 **계약금액, 계약기간, 고객, 납품스케줄, backlog, 병목, 마진, OP/EPS 상향, FCF 전환, 자본배분, 실제 가격경로**가 같이 맞아야 Stage 3로 올라간다.
> 이번 Loop 7에서는 특히 GE Vernova가 `score → stage → price-path`가 잘 맞은 성공사례이고, Hanwha Aerospace는 `좋은 구조 + 나쁜 자본배분 = stage 강등`이 실제 가격경로와 맞은 반례다.

다음 순서는 **R2 — AI·반도체·전자부품 Loop 7**다.

[1]: https://www.reuters.com/business/energy/us-power-transformer-buyers-scramble-imports-factory-slots--reeii-2026-05-11/?utm_source=chatgpt.com "US power transformer buyers scramble for imports, factory slots"
[2]: https://www.reuters.com/business/energy/ge-vernova-lifts-annual-revenue-forecast-data-center-demand-2026-04-22/?utm_source=chatgpt.com "GE Vernova lifts 2026 outlook as AI boom fuels power equipment demand"
[3]: https://www.investors.com/news/ge-vernova-earnings-ai-data-center-power-gev-stock/?utm_source=chatgpt.com "AI Data Center Boom Supercharges GE Vernova Earnings. This Is How Much."
[4]: https://www.reuters.com/sustainability/climate-energy/siemens-energy-accelerates-share-buyback-after-q2-cash-flow-jumps-2026-05-12/?utm_source=chatgpt.com "Siemens Energy accelerates share buyback after Q2 cash flow jumps"
[5]: https://www.reuters.com/business/siemens-q2-profit-misses-forecasts-orders-surge-2026-05-13/?utm_source=chatgpt.com "Siemens orders rise more than expected despite Iranian war tension"
[6]: https://www.reuters.com/markets/deals/hyundai-rotem-wins-15-billion-order-moroccos-national-rail-operator-2025-02-26/?utm_source=chatgpt.com "Hyundai Rotem wins $1.5 billion order from Morocco's national rail operator"
[7]: https://www.reuters.com/business/aerospace-defense/south-koreas-hanwha-aerospace-trims-capital-increase-plan-16-bln-2025-04-07/?utm_source=chatgpt.com "South Korea's Hanwha Aerospace trims capital increase plan to $1.6 bln"
[8]: https://www.ft.com/content/994a0a80-414f-442f-bf41-f2dbde5a04ca?utm_source=chatgpt.com "South Korea's biggest defence group plans $2.5bn share sale to expand overseas"
[9]: https://www.reuters.com/world/asia-pacific/hd-hyundai-heavy-huntington-ingalls-jointly-build-us-navy-auxiliary-ships-2025-10-26/?utm_source=chatgpt.com "HD Hyundai Heavy, Huntington Ingalls to jointly build U.S. navy auxiliary ships"

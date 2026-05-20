좋아. **R2 Loop 7까지 끝났으니, 이번은 R3 Loop 7 — 2차전지·전기차·친환경**이다.

이번 Loop 7부터는 단순히 archetype을 더 늘리는 게 아니라, **지금 점수표가 stage를 실제로 잘 잡았는지, 그 stage가 주가 상승·하락과 맞았는지, 그래서 점수비중을 어떻게 다시 정규화할지**를 중심에 둔다.

R3는 2차전지 소재·부품·공정장비, ESS, 폐배터리, 전고체, 전기차 인프라, 수소, 태양광, 풍력, 탄소배출권, 폐기물처리, 탈플라스틱을 흡수한다. Theme Tag Map 기준으로도 이 구간은 **Green보다 과열 방어가 우선**이고, 소재·전고체·폐배터리는 실제 계약·수익성·FCF 확인 전까지 Stage 3-Green을 제한해야 한다.

서생원 원칙으로 보면 R3의 핵심은 “EV가 성장하냐”가 아니다. **앞으로 EPS/FCF 체급이 바뀌는데 시장이 아직 과거 프레임으로 보고 있는가**다. EV CAPA가 많아도 공장이 놀면 4C고, ESS 계약이 실제 고객·금액·기간·GWh·마진으로 확인되면 Stage 2~3 후보가 된다.

공시·데이터 작업에서는 계약금액, 계약기간, 고객명, GWh, 생산개시일, 매출 대비 계약금액, OP YoY, 희석률 같은 detail을 실제로 확인해야 한다. 없으면 만들면 안 된다. 이 원칙은 R3에서 특히 중요하다. “ESS 계약”, “전고체 license”, “폐배터리”, “AI 데이터센터 storage”라는 단어만으로 Stage 3를 올리면 false-positive가 바로 커진다.

---

# R3 Loop 7. 2차전지·전기차·친환경

## 1. 이번 라운드 대섹터

```text
R3 = 2차전지·전기차·친환경
Loop 7 목표 =
EV CAPA 과열 / EV 계약취소 / EV→ESS 전환 /
Tesla Megapack supply chain / SK On ESS 계약 /
AI data-center storage / 폐배터리+ESS /
전고체 license / 태양광 UFLPA /
풍력 impairment / EV·BESS 안전규제를

stage 포착 + 실제 가격경로 + 점수비중 재조정으로 다시 정규화
```

이번 R3 Loop 7의 핵심 질문은 이거다.

```text
이 기업은 EV 성장 narrative에 기대고 있는가?
아니면 EV 둔화 속에서도 ESS, storage, recycling, grid, data-center power로
새로운 EPS/FCF 체급을 만들고 있는가?
```

R3 stage는 이렇게 잡는다.

```text
Stage 1:
EV 성장, ESS 성장, 폐배터리, 전고체, 태양광, 풍력, 수소, 정책 뉴스

Stage 2:
계약금액, 고객, 계약기간, GWh, 생산공장, 생산개시일, license, 정부/utility 계약 확인

Stage 3:
ESS OPM, 매출 인식, 가동률, FCF, EPS revision, 실제 가격경로 동행

Stage 4B:
ESS·전고체·폐배터리·AI storage narrative가 모두에게 알려져 valuation이 먼저 간 구간

Stage 4C:
EV 계약취소, 공장 idle, CAPA 과잉, 통관·관세, 화재·안전규제, project impairment, SOH 불투명성
```

R3 Loop 7에서 가장 크게 갈라야 하는 축은 이것이다.

```text
EV battery CAPA
≠ ESS battery visibility

ESS 계약
≠ ESS margin

전고체 license
≠ 전고체 상업화

폐배터리 회수량
≠ second-life ESS 수익성

태양광 미국공장
≠ 통관·UFLPA 통과

풍력 PPA
≠ project economics
```

---

## 2. 대상 canonical archetype

| canonical archetype                      | Loop 7 판정 방향    | stage 포착 핵심                                    |
| ---------------------------------------- | --------------- | ---------------------------------------------- |
| `BATTERY_MATERIALS_CAPEX_OVERHEAT`       | Watch/Red       | EV 수요, CAPA, 계약취소, 판가·원가 spread                |
| `BATTERY_EQUIPMENT_PARTS`                | Watch-to-Green  | 고객사 CAPEX, 장비 납품, OPM                          |
| `ESS_LFP_GRID_STORAGE`                   | Green 후보        | 계약금액, 고객, 기간, GWh, ESS OPM                     |
| `ESS_TESLA_MEGAPACK_SUPPLY_CHAIN`        | Stage 2 강함      | Tesla/Megapack 3, Lansing, $4.3B, 2027 생산      |
| `ESS_AI_DATA_CENTER_STORAGE`             | Watch-to-Green  | data-center storage 고객, deployment GWh, margin |
| `EV_TO_ESS_CAPACITY_REDEPLOYMENT`        | Watch           | EV line idle을 ESS로 전환, 실제 계약·가동률 필요            |
| `EV_BATTERY_JV_RESTRUCTURING`            | Watch/Red       | JV 해체, 고정비 절감, ESS pivot, 영업손실                 |
| `EV_CAPA_CONTRACT_CANCELLATION`          | hard 4C         | EV 계약취소, expected revenue loss, utilization 하락 |
| `BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE` | 공통 cap          | 고객·금액·용도·기간 미공개 시 Stage 3 제한                   |
| `BATTERY_RECYCLING_ESS_SHIFT`            | Watch-to-Green  | 회수량, 금속 회수, ESS/grid/data-center 고객            |
| `SECOND_LIFE_BATTERY_GRID_STORAGE`       | Watch-to-Green  | SOH 검증, 잔존용량, 안전성, warranty                    |
| `BATTERY_SOH_SECOND_LIFE_TRANSPARENCY`   | RedTeam overlay | BMS SOH 신뢰도, battery passport, 잔존가치            |
| `BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY`  | Watch           | 중국 의존도, 미국 생산비, offtake, 정책금융                  |
| `LITHIUM_ESS_DEMAND_CYCLE`               | Cycle/Watch     | ESS 수요는 가점, 공급반응·sodium-ion 감점                 |
| `SODIUM_ION_SUBSTITUTION_OVERLAY`        | RedTeam overlay | 저가 ESS/저가 EV에서 lithium/LFP 가격상한                |
| `SOLID_STATE_COMMERCIALIZATION_LICENSE`  | Watch           | license는 Stage 2, 양산·royalty·차종 전 Green 금지     |
| `EV_INFRASTRUCTURE`                      | Watch           | 이용률, 충전매출, 안전규제                                |
| `EV_FIRE_BESS_SAFETY_OVERLAY`            | hard gate       | EV/BESS 화재, 인증, 보험, 시설규제                       |
| `BESS_SAFETY_PERMITTING`                 | hard gate       | BESS 화재, 대피, 보험, 인허가, 지역반발                     |
| `SOLAR_TARIFF_SUPPLYCHAIN`               | Watch/Red       | UFLPA, 통관, FEOC, 관세, 부품 억류                     |
| `RENEWABLE_ENERGY_PROJECT_ECONOMICS`     | Watch/Red       | 풍력 원가, financing, 인허가, impairment              |
| `WASTE_RECYCLING_ENVIRONMENT`            | Green 가능        | 허가권, 처리량, 반복 FCF                               |
| `DATA_CENTER_WATER_REUSE_INFRA`          | Watch-to-Green  | data-center water/cooling 계약, 반복매출             |

---

## 3. deep sub-archetype

```text
ESS_TESLA_MEGAPACK_SUPPLY_CHAIN
- LG Energy Solution
- Tesla
- Megapack 3
- LFP prismatic cell
- Lansing, Michigan
- Houston Megapack production
- $4.3B contract
- 2027 production start
- China LFP dependency reduction
- tariff / FEOC risk
- ESS OPM

ESS_LFP_GRID_STORAGE
- SK On
- Flatiron Energy
- 7.2GWh
- 2026~2030
- Georgia EV line conversion
- ESS-dedicated LFP
- contract value missing
- utility-scale storage
- customer concentration

EV_TO_ESS_CAPACITY_REDEPLOYMENT
- Ultium Ohio idle
- Tennessee ESS conversion
- Ford Energy
- Ford-SK JV dissolution
- EV tax credit expiry
- EV demand slowdown
- battery plant utilization
- fixed cost absorption
- ESS gross margin

EV_CAPA_CONTRACT_CANCELLATION
- Ford-LGES cancellation
- Freudenberg cancellation
- expected revenue loss
- EV model discontinuation
- customer strategy reversal
- European plant utilization delay
- policy change
- contract cancellation filing

BATTERY_RECYCLING_ESS_SHIFT
- Redwood Materials
- battery recycling
- lithium/cobalt/nickel/copper recovery
- grid services
- data-center power
- second-life EV batteries
- Volkswagen / Panasonic / Toyota / Lyft
- Nvidia / Google / AI infra capital

SOLID_STATE_COMMERCIALIZATION_LICENSE
- QuantumScape
- Volkswagen PowerCo
- 40GWh license
- 80GWh expansion option
- royalty
- technology milestone
- mass production
- vehicle series adoption
- pre-revenue risk

SOLAR_TARIFF_SUPPLYCHAIN
- Qcells
- Georgia solar factories
- UFLPA
- customs detention
- component delay
- worker furlough
- contractor layoffs
- domestic solar supply chain
- FEOC risk

RENEWABLE_ENERGY_PROJECT_ECONOMICS
- Ørsted
- Sunrise Wind
- impairment
- monopile foundation cost
- financing cost
- project delay
- PPA
- offshore wind execution risk

EV_FIRE_BESS_SAFETY_OVERLAY
- Korea EV fire
- battery supplier disclosure
- battery certification
- underground parking
- Moss Landing BESS fire
- evacuation
- toxic smoke
- insurance / permitting cost

BATTERY_SOH_SECOND_LIFE_TRANSPARENCY
- BMS SOH reliability
- actual capacity gap
- battery passport
- second-life grading
- warranty enforcement
- used EV valuation
- grid storage residual value
```

---

## 4. 성공사례

### 4-1. LGES–Tesla Megapack 3 LFP 계약 — Stage 2는 강하지만, Stage 3는 아직 아니다

LG에너지솔루션과 Tesla의 43억 달러 LFP 계약은 R3 Loop 7에서 가장 좋은 `ESS_TESLA_MEGAPACK_SUPPLY_CHAIN` Stage 2 사례다. 미국 정부는 Tesla와 LGES의 43억 달러 LFP prismatic cell agreement를 확인했고, Lansing, Michigan에서 2027년 생산을 시작해 Houston에서 생산되는 Tesla Megapack 3 ESS에 들어간다고 밝혔다. 이건 처음에는 고객·용도가 불명확했던 LFP 계약이 **Tesla / Megapack 3 / ESS / Lansing / 2027**로 구체화된 케이스다. ([Reuters][1])

다만 가격경로는 “폭발적 Stage 3”라기보다 “Stage 2 visibility 확인”에 가깝다. WSJ 보도 기준 LGES는 2025년 7월 43억 달러 LFP 계약을 공시했고, 고객은 Tesla로 확인됐지만, LGES 주가 반응은 0.6% 상승 수준이었다. 즉 시장은 계약의 질은 인정했지만, 아직 ESS OPM·가동률·FCF까지는 확신하지 않았다고 보는 게 맞다. ([월스트리트저널][2])

```text
case_type:
ESS_TESLA_MEGAPACK_SUPPLY_CHAIN_STAGE2

stage 포착:
Stage 1 = ESS/LFP/미중 공급망 대체 narrative
Stage 2 = $4.3B, Tesla, Megapack 3, Lansing, 2027 생산 확인
Stage 3 = 아직 ESS OPM, ramp-up, 매출 인식, FCF 확인 필요

가격경로 판정:
계약 detail이 풀린 것은 stage 포착 성공.
하지만 주가 반응은 제한적이므로 EPS/FCF 점수는 아직 cap.
```

**정규화 결론**

```text
ESS_TESLA_MEGAPACK_SUPPLY_CHAIN은 Visibility와 Info 점수를 강하게 올린다.
하지만 Stage 3-Green은 생산 ramp-up, ESS margin, 가동률, FCF 전까지 제한한다.
```

---

### 4-2. SK On–Flatiron ESS 7.2GWh — Stage 2 후보지만 계약금액 미공개 cap

SK On은 미국 Flatiron Energy Development에 ESS용 LFP 배터리를 최대 7.2GWh 공급하기로 했다. 공급기간은 2026~2030년이고, SK On은 2026년 하반기 ESS 전용 LFP 배터리 양산을 시작하며 일부 EV 라인을 ESS 제조용으로 전환할 계획이라고 밝혔다. 하지만 계약금액은 공개되지 않았다. ([Reuters][3])

```text
case_type:
ESS_LFP_GRID_STORAGE_STAGE2_WITH_DISCLOSURE_CAP

stage 포착:
Stage 1 = EV 둔화 속 ESS 전환 narrative
Stage 2 = 최대 7.2GWh, 2026~2030, 고객명, 생산계획 확인
Stage 3 = 계약금액·ESS OPM·매출 인식 전까지 제한

가격경로 판정:
계약 evidence는 강하지만, contract_value_missing = true.
따라서 price-path가 올라도 Stage 3로 바로 올리지 않는다.
```

**정규화 결론**

```text
GWh와 계약기간은 Visibility 가점.
계약금액 미공개는 Disclosure Confidence cap.

즉:
7.2GWh는 좋다.
하지만 매출·마진으로 환산할 수 없으면 EPS/FCF 점수 상한을 둔다.
```

---

### 4-3. Ford Energy — EV 실패가 ESS pivot으로 가격경로를 만들 수 있음을 보여준 사례

Ford는 EV 사업의 큰 손상 이후 Ford Energy를 통해 data-center battery storage 시장을 겨냥했다. FT 보도 기준 Ford 주가는 Ford Energy 출범 이후 이틀 동안 20% 넘게 올랐고, 해당일에는 6.7% 상승해 약 99억 달러 시가총액 증가가 있었다. Ford Energy는 CATL LFP 기술을 활용해 data-center storage를 겨냥하며, 기존 Ford-SK On JV 해체 이후 Kentucky battery plant를 LFP energy-storage battery 생산으로 전환하려는 흐름과 연결된다. ([Financial Times][4])

이 케이스는 R3에서 중요하다. EV CAPA가 실패했다고 끝이 아니라, **EV 설비·제조역량이 ESS/data-center power로 재배치될 때 시장이 다시 re-rating할 수 있다**는 뜻이다. 다만 이건 Ford 자체의 price-path이고, 한국 배터리 밸류체인에 그대로 일반화하면 안 된다.

```text
case_type:
EV_TO_ESS_CAPACITY_REDEPLOYMENT_PRICE_ALIGNED_BUT_EXECUTION_WATCH

stage 포착:
Stage 1 = EV 사업 write-down, JV 해체, CAPA 재배치
Stage 2 = Ford Energy, LFP storage, data-center 고객 narrative
Stage 3 = 아직 실제 storage 계약, gross margin, plant utilization 확인 필요
Stage 4B-watch = AI data-center storage narrative 과열 가능

가격경로 판정:
EV→ESS pivot이 주가 리레이팅을 만들 수 있다는 점은 가격경로로 확인.
하지만 한국 battery supplier 전체에 자동 Green 적용 금지.
```

**정규화 결론**

```text
EV_TO_ESS_CAPACITY_REDEPLOYMENT 점수 상향.
단, 실제 고객계약·가동률·ESS gross margin 확인 전 Stage 3 제한.
```

---

### 4-4. Redwood Materials — 폐배터리 + critical minerals + ESS + AI data-center reference

Redwood Materials는 상장사는 아니지만 R3 archetype 정규화에 중요한 reference다. Reuters는 Redwood가 Eclipse Ventures 주도, Nvidia NVentures 참여로 3.5억 달러를 조달했고, lithium·cobalt·nickel·copper 회수뿐 아니라 grid services와 data-center power용 energy storage systems도 제공한다고 보도했다. Volkswagen, Panasonic, Toyota, Lyft와의 partnership도 확인됐다. ([Reuters][5])

```text
case_type:
BATTERY_RECYCLING_ESS_SHIFT_STRUCTURAL_REFERENCE

stage 포착:
Stage 1 = 폐배터리·critical minerals narrative
Stage 2 = 투자유치, major partnership, ESS/grid/data-center 사업 확인
Stage 3 = 상장사 매핑 시 회수량·매출·OPM·FCF 필요

가격경로 판정:
비상장 reference라 직접 주가경로 검증은 불가.
하지만 archetype 구조 설계에는 매우 유효.
```

**정규화 결론**

```text
폐배터리는 회수량만으로 Green 금지.

Stage 3 조건:
recycling volume
+ recovered material revenue
+ customer contract
+ ESS/grid/data-center 매출
+ FCF
+ SOH 검증
```

---

### 4-5. QuantumScape–Volkswagen PowerCo — 가격은 강하게 반응했지만, Stage 2일 뿐

Volkswagen의 PowerCo는 QuantumScape 전고체 배터리 기술을 대량생산할 수 있는 license를 받았다. 연간 40GWh 생산권과 최대 80GWh 확장 가능성이 포함됐고, 발표 당시 Reuters는 QuantumScape 주가가 premarket에서 40% 상승했다고 보도했다. ([Reuters][6])

이건 전고체 테마 중에서는 확실히 Stage 2 evidence다. 하지만 기술진전과 royalty payment 조건부이고, 아직 양산·차량 탑재·royalty revenue·cost/yield가 확인되지 않았다. 그래서 가격경로는 강했지만, structural Green으로 바로 올리면 안 된다.

```text
case_type:
SOLID_STATE_LICENSE_STAGE2
+
EVENT_PREMIUM_4B_WATCH

stage 포착:
Stage 1 = 전고체 상용화 기대
Stage 2 = VW PowerCo license, 40GWh/80GWh option, 주가 +40% premarket
Stage 3 = 양산·차량탑재·royalty revenue·yield/cost 확인 전까지 제한

가격경로 판정:
Stage 2 포착은 가격경로와 잘 맞았다.
하지만 이건 상업화 성공이 아니라 license event premium에 가깝다.
```

**정규화 결론**

```text
SOLID_STATE_COMMERCIALIZATION_LICENSE는 Visibility를 올리되,
EPS/FCF는 낮게 시작한다.

전고체는:
license = Stage 2
mass production + royalty + vehicle series = Stage 3
```

---

## 5. 반례

### 5-1. LGES–Ford 계약취소 — R3 hard 4C가 실제 주가하락과 정확히 맞은 사례

Ford가 LGES와의 EV battery supply deal을 취소하자 LGES 주가는 장중 최대 7.6% 하락했다. Reuters는 Ford가 일부 EV 모델 생산 중단과 EV 수요·정책 변화 때문에 계약을 취소했고, 해당 계약은 2027년 1월부터 시작될 예정이었다고 보도했다. ([Reuters][7])

더 나쁘게는 LGES가 Freudenberg Battery Power Systems와의 3.9조 원 계약도 취소했고, Reuters는 Ford 계약까지 합쳐 LGES가 10일도 안 돼 약 13.5조 원의 예상매출을 잃었다고 보도했다. 이는 2024년 매출 25.62조 원의 절반 이상에 해당하는 규모다. ([Reuters][8])

```text
case_type:
EV_CAPA_CONTRACT_CANCELLATION_HARD_4C

stage 포착:
Stage 1~2 = 장기 EV 배터리 공급계약
Stage 4C = 고객사의 EV 전략 후퇴, 계약취소, expected revenue loss
주가경로 = LGES -7.6%

가격경로 판정:
EV_CAPA_CONTRACT_CANCELLATION gate가 실제 주가하락과 매우 잘 맞았다.
```

**정규화 결론**

```text
EV 배터리 장기계약은 Stage 2 근거다.
하지만 contract_cancelled_flag가 켜지면 즉시 Stage 4C.

R3에서는 계약 크기만큼
고객 전략 리스크와 EV model risk도 같이 점수화해야 한다.
```

---

### 5-2. GM–LG Ultium Ohio idle — EV CAPA는 더 이상 자동 Green이 아니다

Reuters는 GM과 LGES의 Ultium Cells Ohio EV battery plant 재가동 일정이 불확실하다고 보도했다. 약 850명의 근로자 복귀가 전면적으로 예정되지 않았고, 해당 공장은 EV 수요 둔화와 2025년 9월 미국 EV 세액공제 종료 이후 idling 상태였다. 반면 Tennessee plant는 EV 대신 ESS battery cell 생산을 위해 근로자 복귀가 진행됐다. ([Reuters][9])

```text
case_type:
EV_CAPA_FALSE_GREEN
+
EV_TO_ESS_SHIFT_WATCH

stage 포착:
Stage 1 = EV battery CAPA 증설
Stage 4C = Ohio plant idle, worker recall uncertainty, EV demand slowdown
Stage 2 후보 = Tennessee ESS 전환

가격경로 판정:
공장 idle은 개별 주가보다 operational stage를 강등하는 신호다.
EV CAPA 점수는 강하게 낮추고, ESS 전환은 별도 Watch로 분리.
```

**정규화 결론**

```text
EV battery CAPA:
더 이상 자동 가점 금지.

plant_idle_flag
layoff_furlough_flag
capacity_utilization_low

가 있으면 Stage 3-Green 차단.
```

---

### 5-3. Qcells UFLPA 통관 차질 — 태양광 미국 제조 narrative의 hard 4C

Qcells는 미국 Georgia 공장에서 약 1,000명 근로자를 furlough하고 300명 contract worker를 감축했다. 원인은 미국 세관이 Xinjiang forced-labor 우려와 관련된 UFLPA 집행으로 해외 부품 선적을 지연했기 때문이다. Qcells는 미국 내 full solar supply chain 구축을 계속 추진한다고 했지만, 이 사건은 미국 제조·보조금 narrative가 있어도 **부품 통관·공급망 투명성 하나로 생산이 멈출 수 있음**을 보여준다. ([Reuters][10])

```text
case_type:
SOLAR_TARIFF_SUPPLYCHAIN_HARD_4C

stage 포착:
Stage 1 = 미국 태양광 제조·보조금 narrative
Stage 4C = UFLPA customs detention, component delay, furlough

가격경로 판정:
태양광은 정책수혜보다 통관·관세·부품공급이 먼저다.
```

**정규화 결론**

```text
SOLAR_TARIFF_SUPPLYCHAIN은 Green 제한.
UFLPA / FEOC / customs_detention_flag가 있으면 Visibility와 EPS/FCF 모두 감점.
```

---

### 5-4. Ørsted Sunrise Wind impairment — 재생에너지 project economics 4C

Ørsted는 Sunrise Wind 지연, monopile foundation 비용 증가, 미국 financing cost 상승 때문에 12.1 billion Danish crowns, 약 16.9억 달러 impairment를 발표했다. 프로젝트 commissioning은 2027년 하반기로 밀렸다. ([Reuters][11])

MarketWatch 보도 기준으로는 해당 write-down 이후 Ørsted 주가가 장중 최대 18% 하락했다. 이건 풍력·재생에너지에서 “정책·PPA·탈탄소 수요”보다 financing cost, foundation cost, project delay가 더 중요할 수 있음을 보여준다. ([마켓워치][12])

```text
case_type:
RENEWABLE_ENERGY_PROJECT_ECONOMICS_4C

stage 포착:
Stage 1 = offshore wind policy / PPA / energy transition
Stage 4C = impairment, project delay, financing cost, foundation cost
주가경로 = 최대 -18%

가격경로 판정:
project economics RedTeam이 주가하락과 잘 맞았다.
```

**정규화 결론**

```text
RENEWABLE_ENERGY_PROJECT_ECONOMICS는 정책점수보다
financing_cost / capex_overrun / impairment flag를 더 강하게 본다.
```

---

### 5-5. EV·BESS safety — 수요는 좋아도 안전·보험·인허가가 Stage gate

한국에서는 Mercedes-Benz EV 화재 이후 정부가 완성차 업체에 EV battery supplier disclosure를 권고했고, Mercedes, Hyundai, Genesis, Kia 등이 battery supplier를 공개하기 시작했다. 이는 EV 화재가 소비자 불안, battery brand disclosure, 인증·규제로 이어질 수 있음을 보여준다. ([Reuters][13])

BESS 쪽에서는 California Moss Landing의 대형 battery storage plant fire가 약 1,500명 대피와 toxic smoke 우려를 불렀고, 기존에도 여러 차례 battery-related incident가 있었다. 이는 ESS 수요가 강해도 safety, permitting, insurance, local opposition이 project economics를 바꿀 수 있음을 보여준다. ([가디언][14])

```text
case_type:
EV_FIRE_BESS_SAFETY_OVERLAY
+
BESS_SAFETY_PERMITTING_4C_WATCH

stage 포착:
Stage 1 = EV/ESS 수요 증가
Stage 4C-watch = 화재, battery disclosure, evacuation, permitting/insurance risk

가격경로 판정:
안전 이벤트는 특정 종목 가격뿐 아니라 sector score cap으로 작동한다.
```

**정규화 결론**

```text
ESS_LFP_GRID_STORAGE는 Green 후보가 될 수 있다.
하지만 BESS_SAFETY_PERMITTING gate를 통과해야 한다.

fire_event_flag
evacuation_flag
insurance_cost_change
facility_permitting_delay_flag

필수.
```

---

### 5-6. Battery SOH 불투명성 — 폐배터리·second-life ESS valuation의 숨은 4C

2026년 arXiv 연구는 1,114대 EV와 5개 제조사를 대상으로 BMS가 보고하는 battery state-of-health가 실제 capacity 차이를 충분히 반영하지 못한다고 분석했다. 모델별 실제 capacity 차이는 12~25% 존재했지만, BMS SOH와의 상관은 약하거나 일부 차량은 SOH를 제공하지 않았다. 이건 폐배터리·second-life ESS에서 잔존가치, warranty, battery passport, grading cost가 매우 중요하다는 뜻이다. ([arXiv][15])

```text
case_type:
BATTERY_SOH_SECOND_LIFE_TRANSPARENCY_REDTEAM

stage 포착:
Stage 1 = 폐배터리·second-life ESS narrative
Stage 4C-watch = SOH 불확실성, 잔존가치·보증·안전성 검증비용

가격경로 판정:
직접 가격 이벤트는 아니지만, second-life ESS 점수 cap으로 강하게 반영.
```

**정규화 결론**

```text
BATTERY_RECYCLING_ESS_SHIFT는 회수량만으로 Green 금지.

필수:
SOH validation
residual capacity
battery passport
fire safety
warranty risk
```

---

## 6. 지금 점수표로 실제 stage를 어떻게 포착했고, 주가 상승·하락과 맞았는지에 따른 점수비중정규화

이번 R3 Loop 7부터 기본 점수표는 아래처럼 재정규화한다.

```text
R3 v7 기본 점수표 = 100점

1. EPS/FCF·OPM 전환 가능성              24점
2. 계약 visibility                         22점
   - 고객명
   - 계약금액
   - 계약기간
   - GWh
   - 생산공장
   - 생산개시일
3. 수요 지속성·구조 변화                  16점
   - EV → ESS
   - AI data-center storage
   - grid storage
   - recycling/critical minerals
4. 시장 오해·리레이팅 gap                 10점
5. valuation room / 4B 여지                8점
6. CAPA 활용·자본효율·FCF 안정성          10점
7. 안전·규제·disclosure confidence         10점

Hard RedTeam:
계약취소, 공장 idle, UFLPA, project impairment, EV/BESS fire,
SOH 불투명성, 전고체 상업화 실패, sodium-ion 대체, CAPA 과잉
```

---

### 6-1. stage별 점수 cap

```text
Stage 1 cap:
최대 45점

조건:
- EV 성장, ESS, 폐배터리, 전고체, 태양광, 풍력, 수소 narrative만 있음
- 고객·계약·금액·GWh·생산시점 없음

예:
전고체 테마주
폐배터리 회수설비 계획
AI 데이터센터 ESS 관련주 이름만 있는 경우
```

```text
Stage 2 cap:
최대 70점

조건:
- 계약금액·고객·기간·GWh·license·생산시점 중 일부 확인
- 하지만 매출 인식·OPM·FCF는 미확인

예:
LGES–Tesla $4.3B Megapack 3
SK On–Flatiron 7.2GWh
QuantumScape–VW 40GWh license
```

```text
Stage 3:
70점 이상 가능

조건:
- 실제 매출 인식
- ESS OPM 또는 battery margin 확인
- 가동률 개선
- FCF 전환
- EPS revision
- 가격경로 동행

예:
현재 R3 Loop 7에서 확정 Stage 3는 제한적.
대부분 Stage 2 후보 또는 4C 반례가 더 선명함.
```

```text
Stage 4B:
점수는 높지만 기대수익률 감점

조건:
- 전고체·ESS·폐배터리·AI storage narrative가 모두에게 알려짐
- 주가가 계약·매출보다 먼저 크게 감
- valuation이 EPS/FCF보다 앞서 확장

예:
QuantumScape license 발표 후 premarket +40%는 Stage 2와 4B-watch가 동시에 붙음.
```

```text
Stage 4C:
hard RedTeam

조건:
- 계약취소
- expected revenue loss
- 공장 idle
- CAPA underutilization
- UFLPA 통관 차질
- 풍력 impairment
- EV/BESS 화재
- SOH 불투명성
```

---

### 6-2. 실제 가격경로와 맞은 case / 안 맞은 case

| case                   |        점수표가 잡은 stage |                    실제 가격경로 확인 | 판정                             | 정규화 조정                            |
| ---------------------- | -------------------: | ----------------------------: | ------------------------------ | --------------------------------- |
| LGES–Tesla Megapack 3  |              Stage 2 |            계약 공시 후 LGES +0.6% | visibility는 맞았지만 Stage 3 아님    | 계약 detail 가점, EPS/FCF cap 유지      |
| SK On–Flatiron         |              Stage 2 |   계약금액 미공개, price backfill 필요 | Stage 2 cap이 맞음                | contract_value_missing penalty 강화 |
| Ford Energy            |       EV→ESS Stage 2 |    Ford 이틀간 +20% 이상, 당일 +6.7% | EV→ESS pivot 가격경로 확인           | EV_TO_ESS 점수 상향, supplier 일반화 금지  |
| Redwood                | structural reference |      비상장, price validation 불가 | archetype reference            | 상장사 매핑 시 direct exposure 필수       |
| QuantumScape–VW        |   Stage 2 + 4B-watch |                premarket +40% | event premium은 맞음, Green 아님    | 전고체 license cap 유지                |
| LGES–Ford 취소           |             Stage 4C |                    LGES -7.6% | RedTeam 매우 잘 맞음                | 계약취소 gate 강화                      |
| LGES–Freudenberg 취소    |             Stage 4C | 13.5조 원 expected revenue loss | 4C 강화                          | expected_revenue_loss 필드 필수       |
| Ultium Ohio idle       |             Stage 4C |                       운영단계 강등 | EV CAPA false Green            | plant_idle penalty 강화             |
| Qcells UFLPA           |             Stage 4C |               furlough 1,000명 | solar supply-chain risk 확인     | UFLPA gate 강화                     |
| Ørsted Sunrise Wind    |             Stage 4C |                       최대 -18% | project economics RedTeam 잘 맞음 | financing/cost impairment 강화      |
| Moss Landing BESS fire |             4C-watch |            sector safety gate | BESS safety cap 필요             | BESS safety/permitting 강화         |
| Battery SOH study      |             4C-watch |                price event 아님 | second-life valuation cap      | SOH validation 필수화                |

---

### 6-3. R3 Loop 7 점수비중 재조정

이번 검증 결과 R3 점수표는 이렇게 조정한다.

```text
상향:
ESS 계약 visibility
EV→ESS capacity redeployment
AI data-center storage linkage
계약취소 RedTeam
BESS safety/permitting gate
SOH transparency gate

유지:
폐배터리 + ESS 구조
graphite supply security
solid-state license Stage 2
수소·탄소·폐기물 처리

하향 또는 cap:
EV battery CAPA growth
2차전지 소재 CAPEX
전고체 상용화 전 narrative
태양광 미국 제조 narrative
풍력 PPA-only narrative
계약금액 미공개 ESS 계약
```

구체적으로는 이렇게 간다.

| 항목            | Loop 6 감각 |                             Loop 7 조정 |
| ------------- | --------: | ------------------------------------: |
| EPS/FCF·OPM   |        중요 |                   더 중요. Stage 3 승격 핵심 |
| 계약 visibility |        중요 |        유지/상향. 단, 금액·고객·기간·GWh 모두 봐야 함 |
| EV CAPA       |        중립 |                  하향. idle·계약취소가 너무 강함 |
| ESS 계약        |        상향 | 유지/상향. Tesla/Flatiron/Ford Energy로 확인 |
| EV→ESS 전환     |     Watch |                     상향. 단, 실계약·가동률 필요 |
| 전고체 license   |     Watch |                  가격반응은 인정, EPS cap 유지 |
| 폐배터리          |     Watch | Redwood reference로 구조 유지, SOH gate 강화 |
| 태양광           | Watch/Red |                          UFLPA로 더 보수적 |
| 풍력            | Watch/Red |                     impairment로 더 보수적 |
| 안전규제          |        보조 |                         hard gate로 격상 |

---

### 6-4. R3 Loop 7 archetype별 최종 stage 규칙

```text
ESS_TESLA_MEGAPACK_SUPPLY_CHAIN:
Stage 1 = ESS/LFP/China dependency reduction
Stage 2 = Tesla, Megapack 3, $4.3B, Lansing, 2027
Stage 3 = production ramp + ESS OPM + FCF + EPS revision
Stage 4B = Tesla ESS supply-chain narrative 과열
Stage 4C = ramp delay, tariff/FEOC, Megapack demand cut, margin miss
```

```text
ESS_LFP_GRID_STORAGE:
Stage 1 = grid storage demand
Stage 2 = GWh + 고객 + 기간
Stage 3 = contract value + OPM + revenue recognition + FCF
Stage 4B = ESS 관련주 동반 과열
Stage 4C = BESS fire, LFP price war, customer delay
```

```text
EV_TO_ESS_CAPACITY_REDEPLOYMENT:
Stage 1 = EV plant idle / EV slowdown
Stage 2 = ESS conversion + customer interest + line conversion plan
Stage 3 = utilization + gross margin + FCF
Stage 4B = AI data-center storage narrative 과열
Stage 4C = EV write-down 지속, ESS 계약 부재, 전환비용 증가
```

```text
EV_CAPA_CONTRACT_CANCELLATION:
Stage 1~2 = EV supply agreement
Stage 4C = contract cancellation, expected revenue loss, utilization delay
이 archetype은 hard gate.
```

```text
BATTERY_RECYCLING_ESS_SHIFT:
Stage 1 = recycling / critical minerals narrative
Stage 2 = 회수량 + 고객계약 + ESS/grid/data-center 사업
Stage 3 = recovered material revenue + ESS revenue + FCF
Stage 4B = 폐배터리·AI storage narrative 과열
Stage 4C = SOH 불투명성, 금속가격 하락, 회수량 부족
```

```text
SOLID_STATE_COMMERCIALIZATION_LICENSE:
Stage 1 = 기술 기대
Stage 2 = license, capacity right, royalty framework
Stage 3 = mass production + vehicle series + royalty revenue + cost/yield
Stage 4B = 전고체 관련주 급등
Stage 4C = 기술조건 미달, 양산 지연, cash burn
```

```text
SOLAR_TARIFF_SUPPLYCHAIN:
Stage 1 = 미국 제조·보조금
Stage 2 = 가동률·부품공급·OPM 확인
Stage 3 = 보조금 없이도 FCF
Stage 4C = UFLPA, customs detention, FEOC, furlough
```

```text
RENEWABLE_ENERGY_PROJECT_ECONOMICS:
Stage 1 = PPA / 정책 / 탈탄소
Stage 2 = financing + cost lock-in + construction progress
Stage 3 = project economics + FCF
Stage 4C = impairment, project delay, financing cost, foundation cost
```

---

# R3 Loop 7 결론

이번 R3 Loop 7의 핵심은 이거다.

```text
R3는 아직 R2 HBM처럼 Stage 3 성공사례가 압도적으로 많지 않다.
오히려 Stage 2 후보와 Stage 4C 반례가 훨씬 선명하다.
```

```text
Stage 2가 강한 후보:
LGES–Tesla Megapack 3
SK On–Flatiron ESS 7.2GWh
QuantumScape–VW solid-state license
Redwood recycling+ESS reference
Ford Energy EV→ESS pivot

Stage 4C가 강하게 확인된 반례:
LGES–Ford 계약취소
LGES–Freudenberg 계약취소
GM/LG Ultium Ohio idle
Qcells UFLPA 통관 차질
Ørsted Sunrise Wind impairment
Moss Landing BESS fire
EV battery supplier disclosure / EV fire
Battery SOH transparency failure
```

**R3 Loop 7 점수정규화의 핵심 문장:**

> 2차전지·전기차·친환경은 “EV 성장”, “ESS”, “폐배터리”, “전고체”, “태양광”, “풍력”이라는 이름이 아니라 **계약금액, 고객, GWh, 생산시점, 가동률, ESS OPM, FCF, contract cancellation, plant idle, UFLPA, project impairment, fire/safety, SOH transparency, 실제 가격경로**로 봐야 한다.
> 이번 Loop 7에서는 `LGES–Tesla`와 `SK On–Flatiron`이 Stage 2 visibility를 보여줬고, `LGES–Ford cancellation`, `Ultium Ohio idle`, `Qcells UFLPA`, `Ørsted impairment`가 4C RedTeam이 실제 가격·운영경로와 맞았음을 확인했다.

다음 순서는 **R4 — 소재·스프레드·전략자원 Loop 7**다.

[1]: https://www.reuters.com/business/energy/us-government-confirms-tesla-lg-energy-solutions-43-billion-battery-deal-2026-03-17/?utm_source=chatgpt.com "US government confirms Tesla and LG Energy Solution's $4.3 billion battery deal"
[2]: https://www.wsj.com/business/autos/lg-energy-clinches-4-3-billion-battery-deal-with-tesla-45c6e45c?utm_source=chatgpt.com "LG Energy Clinches $4.3 Billion Battery Deal With Tesla"
[3]: https://www.reuters.com/business/energy/south-koreas-sk-signs-ess-battery-supply-deal-with-us-based-flatiron-energy-2025-09-03/?utm_source=chatgpt.com "South Korea's SK On signs ESS battery supply deal with US-based Flatiron Energy"
[4]: https://www.ft.com/content/3788778f-ea93-4811-80a8-4c8f4c5c0b1f?utm_source=chatgpt.com "Ford shares surge after launch of power unit for data centres"
[5]: https://www.reuters.com/business/battery-recycling-firm-redwood-raises-350-million-eclipse-ventures-nvidia-2025-10-23/?utm_source=chatgpt.com "Battery recycling firm Redwood raises $350 million from Eclipse Ventures, Nvidia"
[6]: https://www.reuters.com/business/autos-transportation/volkswagen-ramp-up-solid-state-battery-production-quantumscape-deal-2024-07-11/?utm_source=chatgpt.com "Volkswagen, QuantumScape strike deal on solid-state batteries"
[7]: https://www.reuters.com/business/energy/shares-south-koreas-lges-drop-more-than-7-after-ford-cancels-ev-battery-deal-2025-12-18/?utm_source=chatgpt.com "Shares in South Korea's LGES drop more than 7% after Ford cancels EV battery deal"
[8]: https://www.reuters.com/business/energy/lg-energy-solution-cancels-39-trillion-won-battery-order-with-freudenberg-2025-12-26/?utm_source=chatgpt.com "LG Energy Solution cancels 3.9 trillion won battery order with Freudenberg"
[9]: https://www.reuters.com/legal/litigation/gms-restart-date-ohio-battery-plant-uncertain-2026-05-12/?utm_source=chatgpt.com "GM-LG's restart date at Ohio battery plant uncertain"
[10]: https://www.reuters.com/sustainability/climate-energy/qcells-furloughs-1000-workers-us-solar-factories-due-stalled-shipments-2025-11-08/?utm_source=chatgpt.com "Qcells furloughs 1,000 workers at US solar factories due to stalled shipments"
[11]: https://www.reuters.com/business/energy/orsted-flags-impairments-about-17-billion-us-rate-increases-2025-01-20/?utm_source=chatgpt.com "Orsted flags $1.7 bln impairment on Sunrise Wind delays, increased costs"
[12]: https://www.marketwatch.com/story/this-wind-power-company-just-took-a-1-7-billion-write-down-and-that-excludes-trump-executive-order-impact-7488a3dc?utm_source=chatgpt.com "This wind-power company just took a $1.7 billion write-down - and that excludes impact of Trump's executive order"
[13]: https://www.reuters.com/business/autos-transportation/south-korea-advise-automakers-disclose-battery-information-evs-2024-08-13/?utm_source=chatgpt.com "South Korea urges automakers to disclose EV battery brands after fires"
[14]: https://www.theguardian.com/us-news/2025/jan/17/california-battery-plant-fire-monterey?utm_source=chatgpt.com "Fire reignites at California battery plant after evacuations amid toxic smoke"
[15]: https://arxiv.org/abs/2603.21592?utm_source=chatgpt.com "Battery health reporting fails independent validation across manufacturers"

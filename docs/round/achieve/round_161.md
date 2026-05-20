좋아. **R2 Loop 10까지 끝났으니, 이번은 R3 Loop 10 — 2차전지·전기차·친환경**이다.

R3는 2차전지 소재·부품·공정장비, ESS, 폐배터리, 전고체, 전기차 인프라, 수소, 태양광, 풍력, 탄소배출권, 폐기물처리, 탈플라스틱을 흡수한다. 이 구간은 Theme Tag Map 기준으로도 **Green보다 과열 방어가 우선**이고, 소재·전고체·폐배터리는 실제 계약·수익성·FCF가 확인되기 전까지 Stage 3-Green을 제한해야 한다.

서생원식으로 보면 R3의 질문은 “EV가 성장하나?”, “ESS가 뜨나?”, “전고체가 유망하나?”가 아니다. 핵심은 **EV·ESS·폐배터리·전고체·태양광·풍력이라는 변화가 EPS/FCF 체급 변화로 바뀌고, 시장이 아직 그 변화를 과소평가하는가**다. 즉 테마가 아니라 계약금액, GWh, 고객, 가동률, OPM, FCF, 가격경로가 같이 맞아야 한다.

공시 기반으로는 단일판매·공급계약, 신규시설투자, 계약 취소·정정, 유상증자, CB/BW, 잠정실적 같은 watch disclosure를 detail에서 확인해야 한다. 계약금액, 계약기간, 고객명, 매출 대비 계약금액, OP YoY, 희석률을 실제 확인해야 하고, 없는 값은 만들면 안 된다.

---

# R3 Loop 10. 2차전지·전기차·친환경

## 1. 이번 라운드 대섹터

```text
R3 = 2차전지·전기차·친환경

Loop 10 목표 =
EV CAPA 과열 / EV 계약취소 / EV 공장 idle /
EV → ESS 전환 / Tesla Megapack supply chain /
SK On ESS 계약 / Ford Energy / Redwood recycling+ESS /
전고체 license / 태양광 UFLPA /
풍력 impairment / EV·BESS safety /
battery SOH transparency를

stage 포착
+ 실제 가격경로
+ 점수비중 정규화로 재분류
```

이번 R3 Loop 10의 핵심 질문은 이거다.

```text
이 회사는 EV 성장 narrative에 기대고 있는가?

아니면 EV 둔화 속에서도 ESS, grid storage, data-center power,
recycling, critical minerals로 새로운 EPS/FCF 체급을 만들고 있는가?
```

R3 stage는 이렇게 잡는다.

```text
Stage 1:
EV 성장, ESS 성장, 폐배터리, 전고체, 태양광, 풍력, 수소, 정책 뉴스

Stage 2:
계약금액, 고객, 기간, GWh, 생산공장, 생산개시일,
license, 정부/utility 계약, line conversion 확인

Stage 3:
ESS OPM, 매출 인식, 가동률, FCF, EPS revision,
recycling revenue, 반복 grid/data-center storage 매출,
실제 가격경로 동행

Stage 4B:
ESS·전고체·폐배터리·AI data-center storage narrative가
모두에게 알려져 valuation이 먼저 간 구간

Stage 4C:
EV 계약취소, 공장 idle, CAPA 과잉, 통관·관세,
화재·안전규제, project impairment, SOH 불투명성
```

R3 Loop 10에서 가장 중요한 분리는 이거다.

```text
EV battery CAPA
≠ Green

ESS 계약
≠ ESS margin

EV → ESS 전환
≠ 즉시 FCF

전고체 license
≠ 전고체 상업화

폐배터리 회수량
≠ second-life ESS 수익성

태양광 미국공장
≠ UFLPA 통과

풍력 PPA
≠ project economics
```

---

## 2. 대상 canonical archetype

| canonical archetype                      | Loop 10 판정 방향     | stage 포착 핵심                                    |
| ---------------------------------------- | ----------------- | ---------------------------------------------- |
| `BATTERY_MATERIALS_CAPEX_OVERHEAT`       | Watch/Red         | EV 수요, CAPA, 계약취소, 판가·원가 spread                |
| `BATTERY_EQUIPMENT_PARTS`                | Watch-to-Green    | 고객사 CAPEX, 장비 납품, OPM                          |
| `ESS_LFP_GRID_STORAGE`                   | Green 후보          | 계약금액, 고객, 기간, GWh, ESS OPM                     |
| `ESS_TESLA_MEGAPACK_SUPPLY_CHAIN`        | Stage 2 강함        | Tesla/Megapack 3, Lansing, $4.3B, 2027 생산      |
| `ESS_AI_DATA_CENTER_STORAGE`             | Watch-to-Green    | data-center storage 고객, deployment GWh, margin |
| `EV_TO_ESS_CAPACITY_REDEPLOYMENT`        | Watch-to-Green 후보 | EV line idle을 ESS로 전환, 실제 계약·가동률 필요            |
| `EV_BATTERY_JV_RESTRUCTURING`            | Watch/Red         | JV 해체, 고정비 절감, ESS pivot, 영업손실                 |
| `EV_CAPA_CONTRACT_CANCELLATION`          | hard 4C           | EV 계약취소, expected revenue loss, utilization 하락 |
| `BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE` | 공통 cap            | 고객·금액·용도·기간 미공개 시 Stage 3 제한                   |
| `BATTERY_RECYCLING_ESS_SHIFT`            | Watch-to-Green    | 회수량, 금속 회수, ESS/grid/data-center 고객            |
| `SECOND_LIFE_BATTERY_GRID_STORAGE`       | Watch-to-Green    | SOH 검증, 잔존용량, 안전성, warranty                    |
| `BATTERY_SOH_SECOND_LIFE_TRANSPARENCY`   | RedTeam overlay   | BMS SOH 신뢰도, battery passport, 잔존가치            |
| `BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY`  | Watch             | 중국 의존도, 미국 생산비, offtake, 정책금융                  |
| `LITHIUM_ESS_DEMAND_CYCLE`               | Cycle/Watch       | ESS 수요는 가점, 공급반응·sodium-ion 감점                 |
| `SODIUM_ION_SUBSTITUTION_OVERLAY`        | RedTeam overlay   | 저가 ESS/저가 EV에서 lithium/LFP 가격상한                |
| `SOLID_STATE_COMMERCIALIZATION_LICENSE`  | Watch             | license는 Stage 2, 양산·royalty·차종 전 Green 금지     |
| `EV_INFRASTRUCTURE`                      | Watch             | 이용률, 충전매출, 안전규제                                |
| `EV_FIRE_BESS_SAFETY_OVERLAY`            | hard gate         | EV/BESS 화재, 인증, 보험, 시설규제                       |
| `BESS_SAFETY_PERMITTING`                 | hard gate         | BESS 화재, 대피, 보험, 인허가, 지역반발                     |
| `SOLAR_TARIFF_SUPPLYCHAIN`               | Watch/Red         | UFLPA, 통관, FEOC, 관세, 부품 억류                     |
| `RENEWABLE_ENERGY_PROJECT_ECONOMICS`     | Watch/Red         | 풍력 원가, financing, 인허가, impairment              |
| `WASTE_RECYCLING_ENVIRONMENT`            | Green 가능          | 허가권, 처리량, 반복 FCF                               |
| `DATA_CENTER_WATER_REUSE_INFRA`          | Watch-to-Green    | data-center water/cooling 계약, 반복매출             |

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
- $4.3B agreement
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
- Ford Energy
- data-center battery storage
- utility-scale storage
- 20GWh annual deployment plan
- Kentucky plant
- CATL LFP technology
- EV write-down
- EV plant repurposing
- gross margin target
- execution risk

EV_CAPA_CONTRACT_CANCELLATION
- LGES-Ford cancellation
- LGES-Freudenberg cancellation
- expected revenue loss
- EV model discontinuation
- customer strategy reversal
- European plant utilization delay
- contract cancellation filing

EV_BATTERY_JV_RESTRUCTURING
- Ultium Cells
- GM-LG Ohio plant idle
- Tennessee ESS conversion
- EV tax credit expiry
- EV demand slowdown
- worker recall uncertainty
- fixed cost absorption

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

### 4-1. LGES–Tesla Megapack 3 LFP 계약 — Stage 2는 강하지만 Stage 3는 아직 아니다

LG에너지솔루션과 Tesla의 43억 달러 LFP 계약은 R3 Loop 10에서 가장 좋은 `ESS_TESLA_MEGAPACK_SUPPLY_CHAIN` Stage 2 사례다. 미국 정부는 Tesla와 LGES가 Lansing, Michigan에 LFP prismatic battery cell 공급 구조를 만들고, 2027년 생산을 시작해 Houston에서 생산되는 Tesla Megapack 3 ESS에 들어간다고 확인했다. 핵심은 과거에는 고객·용도가 불명확했던 LFP 계약이 **Tesla / Megapack 3 / ESS / Lansing / 2027**로 구체화됐다는 점이다. ([Reuters][1])

또 2025년 Reuters 보도에서는 LGES가 43억 달러 규모 LFP 공급계약을 공시했지만 고객명을 밝히지 않았고, 이후 source 보도로 Tesla ESS용이라는 맥락이 제시됐다. 이 계약은 2027년 8월부터 2030년 7월까지 3년 공급이며, 최대 7년 연장과 공급량 확대 option이 포함된 것으로 보도됐다. 고객·용도·기간이 명확해진 건 Stage 2의 질을 크게 높인다. ([Reuters][2])

```text
case_type:
ESS_TESLA_MEGAPACK_SUPPLY_CHAIN_STAGE2

stage 포착:
Stage 1 = ESS/LFP/미중 공급망 대체 narrative
Stage 2 = $4.3B, Tesla, Megapack 3, Lansing, 2027 생산 확인
Stage 3 = 아직 ESS OPM, ramp-up, 매출 인식, FCF 확인 필요

가격경로 판정:
계약 detail이 풀린 것은 stage 포착 성공.
하지만 Stage 3는 production ramp-up과 ESS margin 확인 전까지 제한.
```

**정규화 결론**

```text
ESS_TESLA_MEGAPACK_SUPPLY_CHAIN은 Visibility와 Info 점수를 강하게 올린다.
하지만 Stage 3-Green은 생산 ramp-up, ESS margin, 가동률, FCF 전까지 제한한다.
```

---

### 4-2. SK On–Flatiron 7.2GWh ESS 계약 — Stage 2 후보지만 계약금액 미공개 cap

SK On은 미국 Flatiron Energy Development에 ESS용 LFP 배터리를 최대 7.2GWh 공급하기로 했고, 공급기간은 2026~2030년이다. SK On은 2026년 하반기 ESS 전용 LFP 배터리 양산을 시작하고 일부 EV 라인을 ESS 제조용으로 전환할 계획이라고 밝혔다. 다만 계약금액은 공개되지 않았다. ([Reuters][3])

Reuters의 별도 보도도 같은 내용을 확인하면서, 이 계약이 SK On의 ESS용 LFP 첫 주문이고, EV 둔화에 대응해 ESS 사업을 키우려는 흐름이라고 설명했다. 즉 GWh·기간·고객명은 Stage 2에 충분하지만, 금액과 margin이 없어서 EPS/FCF stage로 올리기는 아직 이르다. ([Reuters][4])

```text
case_type:
ESS_LFP_GRID_STORAGE_STAGE2_WITH_DISCLOSURE_CAP

stage 포착:
Stage 1 = EV 둔화 속 ESS 전환 narrative
Stage 2 = 최대 7.2GWh, 2026~2030, 고객명, 생산계획 확인
Stage 3 = 계약금액·ESS OPM·매출 인식 전까지 제한

가격경로 판정:
계약 evidence는 강하지만, contract_value_missing = true.
따라서 price-path가 좋아도 Stage 3로 바로 올리지 않는다.
```

**정규화 결론**

```text
GWh와 계약기간은 Visibility 가점.
계약금액 미공개는 Disclosure Confidence cap.

7.2GWh는 좋다.
하지만 매출·마진으로 환산할 수 없으면 EPS/FCF 점수 상한을 둔다.
```

---

### 4-3. Ford Energy — EV 실패 CAPA가 ESS/data-center storage로 재배치될 때 가격경로가 바뀔 수 있음

Ford Energy는 R3에서 매우 중요한 reference다. Ford 주가는 Ford Energy 관련 투자자 낙관론으로 하루 13% 상승했고, 이는 약 6년 만의 최대 일일 상승이었다. 핵심은 Ford가 EV 사업에서 축적한 battery·manufacturing 자산을 data center, utility, commercial customer용 energy storage로 돌리려는 구조다. ([Reuters][5])

FT 보도 기준 Ford 주가는 Ford Energy 출범 후 이틀 동안 20% 넘게 올랐고, Ford Energy는 CATL LFP 기술을 활용해 data-center storage 시장을 겨냥한다. 동시에 Ford는 EV 관련 약 195억 달러 write-down을 겪었고, 기존 EV 사업의 실패 CAPA를 ESS로 재배치한다는 점에서 “EV 성장주”가 아니라 “EV 실패 CAPA의 ESS 재활용”이라는 별도 archetype으로 분류해야 한다. ([Financial Times][6])

MarketWatch 보도 기준으로는 Ford Energy가 2027년 말부터 연간 최소 20GWh storage deployment를 목표로 하고, 약 20억 달러를 투자하며, Morgan Stanley가 2028년 25% gross margin과 3.46억 달러 EBIT 가능성을 언급했다. 이건 price-path는 강하지만, 아직 실제 고객계약·가동률·gross margin이 확인된 Stage 3는 아니다. ([마켓워치][7])

```text
case_type:
EV_TO_ESS_CAPACITY_REDEPLOYMENT_PRICE_ALIGNED_BUT_EXECUTION_WATCH

stage 포착:
Stage 1 = EV 사업 write-down, EV 수요 둔화, CAPA 재배치
Stage 2 = Ford Energy, LFP storage, data-center 고객 narrative
Stage 3 = 실제 storage 계약, gross margin, plant utilization 확인 필요
Stage 4B-watch = AI data-center storage narrative 과열 가능

가격경로 판정:
EV → ESS pivot이 주가 리레이팅을 만들 수 있다는 점은 가격경로로 확인.
하지만 Ford 자체의 case를 한국 battery supplier 전체에 자동 적용하면 안 된다.
```

**정규화 결론**

```text
EV_TO_ESS_CAPACITY_REDEPLOYMENT 점수 상향.
단, 실제 고객계약·가동률·ESS gross margin 확인 전 Stage 3 제한.
```

---

### 4-4. Redwood Materials — 폐배터리 + critical minerals + ESS + AI data-center reference

Redwood Materials는 비상장사라 직접 주가경로 검증은 어렵지만, R3 archetype 설계에 중요한 reference다. Redwood는 Eclipse Ventures 주도, Nvidia NVentures 참여로 3.5억 달러를 조달했고, lithium·cobalt·nickel·copper 회수뿐 아니라 grid services와 data-center power용 energy storage systems도 제공한다고 밝혔다. Volkswagen, Panasonic, Toyota, Lyft와의 partnership도 확인됐다. ([Reuters][8])

이후 Google도 Redwood의 expanded Series E funding에 참여했고, Redwood는 second-life EV battery를 활용한 energy-storage platform을 AI data center power infrastructure로 확장하는 구조로 보도됐다. 이건 “폐배터리 = 금속 회수”에서 끝나는 게 아니라 **recycling + second-life ESS + AI power infrastructure**로 archetype이 확장될 수 있음을 보여준다. ([Business Insider][9])

```text
case_type:
BATTERY_RECYCLING_ESS_SHIFT_STRUCTURAL_REFERENCE

stage 포착:
Stage 1 = 폐배터리·critical minerals narrative
Stage 2 = 투자유치, major partnership, ESS/grid/data-center 사업 확인
Stage 3 = 상장사 매핑 시 회수량·매출·OPM·FCF 필요

가격경로 판정:
비상장 reference라 직접 주가경로 검증은 불가.
하지만 폐배터리 archetype이 단순 recycling에서 grid/data-center storage로 확장되는 구조는 유효.
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

### 4-5. QuantumScape–Volkswagen PowerCo — 전고체 license는 Stage 2, 상업화는 아직 아님

QuantumScape와 Volkswagen PowerCo의 전고체 license deal은 `SOLID_STATE_COMMERCIALIZATION_LICENSE`의 Stage 2 사례다. PowerCo는 QuantumScape 기술을 기반으로 최대 40GWh 규모 cell을 생산할 수 있고, 80GWh까지 확장할 수 있는 option도 받았다. 발표 당시 QuantumScape 주가는 급등했다. ([Investopedia][10])

```text
case_type:
SOLID_STATE_LICENSE_STAGE2
+
EVENT_PREMIUM_4B_WATCH

stage 포착:
Stage 1 = 전고체 상용화 기대
Stage 2 = VW PowerCo license, 40GWh/80GWh option, 주가 반응
Stage 3 = 양산·차량탑재·royalty revenue·yield/cost 확인 전까지 제한

가격경로 판정:
Stage 2 포착은 가격경로와 맞았다.
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

### 5-1. LGES–Ford 계약취소 — EV 장기계약도 고객 전략이 바뀌면 hard 4C

Ford는 LGES와의 약 9.6조 원, 65억 달러 EV battery supply deal을 취소했다. Ford는 일부 EV 모델 생산 중단과 EV 수요·정책 변화 때문에 계약을 종료했고, 이 계약은 Ford 유럽 EV용 배터리 공급으로 2026~2027년부터 시작될 예정이었다. ([Reuters][11])

```text
case_type:
EV_CAPA_CONTRACT_CANCELLATION_HARD_4C

stage 포착:
Stage 1~2 = 장기 EV 배터리 공급계약
Stage 4C = 고객사의 EV 전략 후퇴, 계약취소, expected revenue loss

가격경로 판정:
EV_CAPA_CONTRACT_CANCELLATION gate가 실제 사업경로 훼손과 매우 잘 맞았다.
```

**정규화 결론**

```text
EV 배터리 장기계약은 Stage 2 근거다.
하지만 contract_cancelled_flag가 켜지면 즉시 Stage 4C.

계약 크기만큼:
customer_strategy_risk
EV_model_risk
utilization_delay
expected_revenue_loss

도 같이 점수화해야 한다.
```

---

### 5-2. LGES–Freudenberg 취소 — 짧은 기간에 expected revenue loss가 누적되는 4C

LGES는 Freudenberg Battery Power Systems와의 3.9조 원, 27억 달러 계약도 취소했다. Reuters는 이 계약 취소가 Ford 계약취소 직후 나왔고, LGES가 10일도 안 되는 기간에 약 13.5조 원의 expected revenue를 잃었다고 보도했다. 이는 LGES의 2024년 매출 25.62조 원의 절반 이상에 해당한다. ([Reuters][12])

```text
case_type:
EV_CONTRACT_CLUSTER_CANCELLATION_4C

stage 포착:
Stage 1~2 = EV battery long-term contracts
Stage 4C = Ford + Freudenberg cancellation, expected revenue loss 13.5조 원

가격경로 판정:
Ford 취소와 Freudenberg 취소의 expected revenue loss가
EV battery CAPA false-positive를 강하게 보여준다.
```

**정규화 결론**

```text
contract_value만 보는 점수표는 위험하다.
contract_cancelled_flag와 customer_exit_flag를 hard gate로 둔다.
```

---

### 5-3. GM-LG Ultium Ohio idle — EV CAPA는 자동 Green이 아니다

GM과 LGES의 Ultium Cells Ohio plant는 EV 수요 둔화로 idled 상태이고, 약 850명 근로자의 전면 복귀 일정도 불확실하다. Reuters는 일부 근로자만 복귀해 재개 준비 작업을 할 예정이며, 생산 재개 시점은 EV 시장 수요에 달려 있다고 보도했다. 동시에 Tennessee Ultium plant에서는 EV 대신 ESS battery cell 생산을 위해 근로자 복귀가 이뤄지고 있다. ([Reuters][13])

AP도 GM이 EV 수요 둔화와 세액공제 종료 이후 Michigan·Ohio 공장에서 약 1,700명 규모의 감원을 발표했고, Ultium Ohio와 Tennessee 생산 일시중단이 포함됐다고 보도했다. 즉 EV CAPA 자체는 더 이상 가점이 아니라, utilization과 전환능력을 봐야 한다. ([AP News][14])

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
EV CAPA 점수는 강하게 낮추고, ESS 전환은 별도 Watch로 분리한다.
```

**정규화 결론**

```text
EV battery CAPA:
더 이상 자동 가점 금지.

plant_idle_flag
layoff_furlough_flag
capacity_utilization_low
worker_recall_uncertain

가 있으면 Stage 3-Green 차단.
```

---

### 5-4. Qcells UFLPA 통관 차질 — 미국 태양광 제조 narrative의 hard 4C

Qcells는 Georgia 태양광 공장에서 약 1,000명 근로자를 furlough하고 300명 contract worker를 감축했다. 원인은 미국 세관이 UFLPA, 즉 Xinjiang forced-labor 관련 법 집행으로 해외 부품 선적을 지연했기 때문이다. Qcells는 미국 내 full solar supply chain 구축을 계속 추진한다고 밝혔지만, 이 사건은 미국 제조·보조금 narrative가 있어도 **부품 통관·공급망 투명성 하나로 생산이 멈출 수 있음**을 보여준다. ([Reuters][15])

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

UFLPA
FEOC
customs_detention
component_delay
furlough

가 있으면 Visibility와 EPS/FCF 모두 감점.
```

---

### 5-5. Ørsted Sunrise Wind impairment — 재생에너지 project economics 4C

Ørsted는 Sunrise Wind 지연과 비용 증가, 미국 financing cost 상승 때문에 121억 덴마크크로네, 약 16.9억 달러 impairment를 발표했다. Sunrise Wind project는 monopile foundation 비용 상승과 지연으로 commissioning이 2027년 하반기로 밀렸다. ([Reuters][16])

WSJ도 Ørsted 주가가 해당 impairment 소식 이후 Stoxx Europe 600 내 하락 상위권으로 밀렸고, project delay와 cost overrun, financing cost가 핵심이었다고 보도했다. 정책·PPA·탈탄소 수요보다 project economics가 먼저라는 점이 확인된다. ([월스트리트저널][17])

```text
case_type:
RENEWABLE_ENERGY_PROJECT_ECONOMICS_4C

stage 포착:
Stage 1 = offshore wind policy / PPA / energy transition
Stage 4C = impairment, project delay, financing cost, foundation cost

가격경로 판정:
project economics RedTeam이 사업경로와 맞았다.
정책·PPA·탈탄소 수요보다 financing cost, foundation cost, project delay가 더 중요할 수 있다.
```

**정규화 결론**

```text
RENEWABLE_ENERGY_PROJECT_ECONOMICS는 정책점수보다
financing_cost / capex_overrun / impairment flag를 더 강하게 본다.
```

---

### 5-6. EV·BESS safety — 수요는 좋아도 안전·보험·인허가가 stage gate

BESS 쪽에서는 California Moss Landing의 대형 battery storage plant fire가 약 1,500명 대피와 toxic smoke 우려를 불렀다. lithium battery fire 특성상 당국은 불이 자연 소진되길 기다리는 방식으로 대응했고, 이 사건은 ESS 수요가 강해도 safety, permitting, insurance, local opposition이 project economics를 바꿀 수 있음을 보여준다. ([가디언][18])

SF Chronicle 보도 기준으로도 Moss Landing 화재는 1,200~1,500명 대피, 300MW lithium-ion battery facility 피해, 약 40% 건물 소실, fire suppression failure 우려를 남겼다. BESS는 전력망에 필요하지만, 화재·보험·인허가·지역 반발이 붙으면 Stage 3-Green이 막힌다. ([San Francisco Chronicle][19])

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
battery_supplier_disclosure_flag

필수.
```

---

### 5-7. Battery SOH 불투명성 — second-life ESS valuation의 숨은 4C

2026년 arXiv 연구는 1,114대 EV와 5개 제조사를 대상으로 BMS가 보고하는 battery state-of-health가 실제 capacity 차이를 충분히 반영하지 못한다고 분석했다. 모델별 실제 capacity 차이는 12~25% 존재했지만, BMS SOH와의 상관은 약하거나 일부 차량은 SOH를 제공하지 않았다. 이건 폐배터리·second-life ESS에서 잔존가치, warranty, battery passport, grading cost가 매우 중요하다는 뜻이다. ([arXiv][20])

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

R3 Loop 10부터 기본 점수표는 이렇게 재정규화한다.

```text
R3 v10 기본 점수표 = 100점

1. EPS/FCF·OPM 전환 가능성              24점

2. 계약 visibility                       22점
   - 고객명
   - 계약금액
   - 계약기간
   - GWh
   - 생산공장
   - 생산개시일

3. 수요 지속성·구조 변화                 16점
   - EV → ESS
   - AI data-center storage
   - grid storage
   - recycling/critical minerals

4. 안전·규제·disclosure confidence        14점

5. CAPA 활용·자본효율·FCF 안정성          10점

6. 시장 오해·리레이팅 gap                 8점

7. valuation room / 4B 여지                6점

Hard RedTeam:
계약취소, 공장 idle, UFLPA, project impairment, EV/BESS fire,
SOH 불투명성, 전고체 상업화 실패, sodium-ion 대체, CAPA 과잉
```

### 6-1. stage별 점수 cap

```text
Stage 1 cap:
최대 45점

조건:
- EV 성장
- ESS
- 폐배터리
- 전고체
- 태양광
- 풍력
- 수소 narrative만 있음
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
- 계약금액
- 고객
- 기간
- GWh
- license
- 생산시점
- line conversion
- government/utility 계약 중 일부 확인

예:
LGES–Tesla $4.3B Megapack 3
SK On–Flatiron 7.2GWh
QuantumScape–VW 40GWh license
Ford Energy data-center storage pivot
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
- price-path 동행
- 안전·규제 gate 통과

현재 R3 Loop 10에서도 확정 Stage 3 사례가 제한적이다.
대부분 Stage 2 후보 또는 Stage 4C 반례가 더 선명하다.
```

```text
Stage 4B:
점수는 높지만 기대수익률 감점

조건:
- 전고체·ESS·폐배터리·AI storage narrative가 모두에게 알려짐
- 주가가 계약·매출보다 먼저 크게 감
- valuation이 EPS/FCF보다 앞서 확장

예:
QuantumScape license 발표 후 급등
Ford Energy 발표 후 이틀간 +20% 이상
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

| case                   |        점수표가 잡은 stage |                          실제 가격경로 확인 | 판정                          | 정규화 조정                            |
| ---------------------- | -------------------: | ----------------------------------: | --------------------------- | --------------------------------- |
| LGES–Tesla Megapack 3  |              Stage 2 |      $4.3B·Tesla·Megapack 3·2027 확인 | visibility는 강함, Stage 3 아님  | 계약 detail 가점, EPS/FCF cap 유지      |
| SK On–Flatiron         |              Stage 2 |             7.2GWh·2026~2030·금액 미공개 | Stage 2 cap이 맞음             | contract_value_missing penalty 강화 |
| Ford Energy            |       EV→ESS Stage 2 |     Reuters +13%, FT 기준 이틀간 +20% 이상 | EV→ESS pivot 가격경로 확인        | EV_TO_ESS 점수 상향, 실행 gate 유지       |
| Redwood                | structural reference |            비상장, price validation 불가 | archetype reference         | 상장사 매핑 시 direct exposure 필수       |
| QuantumScape–VW        |   Stage 2 + 4B-watch |                     license 발표 후 급등 | event premium은 맞음, Green 아님 | 전고체 license cap 유지                |
| LGES–Ford 취소           |             Stage 4C |          $6.5B contract termination | RedTeam 매우 잘 맞음             | 계약취소 gate 강화                      |
| LGES–Freudenberg 취소    |             Stage 4C |       13.5조 원 expected revenue loss | 4C 강화                       | expected_revenue_loss 필드 필수       |
| Ultium Ohio idle       |             Stage 4C |          운영단계 강등, worker recall 불확실 | EV CAPA false Green         | plant_idle penalty 강화             |
| Qcells UFLPA           |             Stage 4C | 1,000명 furlough, 300명 contractor 감축 | solar supply-chain risk 확인  | UFLPA gate 강화                     |
| Ørsted Sunrise Wind    |             Stage 4C |        $1.69B impairment, 2027H2 지연 | project economics RedTeam   | financing/cost impairment 강화      |
| Moss Landing BESS fire |             4C-watch |      1,200~1,500명 대피·toxic smoke 우려 | BESS safety cap 필요          | BESS safety/permitting 강화         |
| Battery SOH study      |             4C-watch |                   직접 price event 아님 | second-life valuation cap   | SOH validation 필수화                |

---

### 6-3. R3 Loop 10 점수비중 재조정

이번 검증 결과 R3 점수표는 이렇게 조정한다.

```text
상향:
ESS 계약 visibility
EV→ESS capacity redeployment
AI data-center storage linkage
계약취소 RedTeam
plant idle / utilization penalty
BESS safety/permitting gate
SOH transparency gate
UFLPA/FEOC supply-chain gate
renewable project economics gate

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

| 항목            | Loop 9 감각 |                            Loop 10 조정 |
| ------------- | --------: | ------------------------------------: |
| EPS/FCF·OPM   |       최상위 |                     유지. Stage 3 승격 핵심 |
| 계약 visibility |        중요 |             유지. 단, 금액·고객·기간·GWh 모두 필요 |
| EV CAPA       |        중립 |                  하향. idle·계약취소가 너무 강함 |
| ESS 계약        |        상향 | 유지·상향. Tesla/Flatiron/Ford Energy로 확인 |
| EV→ESS 전환     |     Watch |              상향. 단, 실계약·가동률·margin 필요 |
| 전고체 license   |     Watch |                  가격반응은 인정, EPS cap 유지 |
| 폐배터리          |     Watch | Redwood reference로 구조 유지, SOH gate 강화 |
| 태양광           | Watch/Red |                          UFLPA로 더 보수적 |
| 풍력            | Watch/Red |                     impairment로 더 보수적 |
| 안전규제          |        보조 |                         hard gate로 격상 |

---

### 6-4. R3 Loop 10 archetype별 최종 stage 규칙

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
EV_BATTERY_JV_RESTRUCTURING:
Stage 1 = EV JV CAPA expansion
Stage 2 = ESS 전환·asset sale·line conversion plan
Stage 3 = utilization 회복 + OPM/FCF 확인
Stage 4C = plant idle, worker layoff, JV dissolution, EV demand collapse
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

```text
EV_FIRE_BESS_SAFETY_OVERLAY:
Stage 1 = EV/ESS demand
Stage 2 = safety certification, disclosure, insurance/permitting 통과
Stage 3 = safety record + recurring deployment + FCF
Stage 4C = fire, evacuation, toxic smoke, supplier disclosure shock, permitting delay
```

---

# R3 Loop 10 결론

이번 R3 Loop 10의 핵심은 이거다.

```text
R3는 아직 R2 HBM처럼 확정 Stage 3 성공사례가 많지 않다.
오히려 Stage 2 후보와 Stage 4C 반례가 훨씬 선명하다.
```

```text
Stage 포착이 잘 맞은 후보:
LGES–Tesla = $4.3B Megapack 3 LFP, Stage 2
SK On–Flatiron = 7.2GWh ESS, Stage 2 with disclosure cap
Ford Energy = EV→ESS/data-center storage pivot, 가격경로 확인
Redwood = recycling + ESS + AI data-center power 구조 reference
QuantumScape–VW = 전고체 license Stage 2, 가격반응 강함

RedTeam이 가격·사업경로와 잘 맞은 사례:
LGES–Ford = $6.5B EV battery contract cancellation
LGES–Freudenberg = 13.5조 원 expected revenue loss 누적
GM/LG Ultium Ohio = EV plant idle, worker recall 불확실
Qcells = UFLPA 통관 차질로 1,000명 furlough
Ørsted = Sunrise Wind impairment와 2027H2 지연
Moss Landing = BESS fire·대피·toxic smoke
Battery SOH study = second-life ESS valuation cap
```

**R3 Loop 10 점수정규화의 핵심 문장:**

> 2차전지·전기차·친환경은 “EV 성장”, “ESS”, “폐배터리”, “전고체”, “태양광”, “풍력”이라는 이름이 아니라 **계약금액, 고객, GWh, 생산시점, 가동률, ESS OPM, FCF, contract cancellation, plant idle, UFLPA, project impairment, fire/safety, SOH transparency, 실제 가격경로**로 봐야 한다.
> 이번 Loop 10에서는 `LGES–Tesla`, `SK On–Flatiron`, `Ford Energy`, `Redwood`, `QuantumScape–VW`가 Stage 1~2 포착 사례이고, `LGES–Ford cancellation`, `LGES–Freudenberg cancellation`, `Ultium Ohio idle`, `Qcells UFLPA`, `Ørsted impairment`, `Moss Landing fire`, `Battery SOH opacity`가 R3 RedTeam이 실제 가격·사업경로와 맞는 반례다.

다음 순서는 **R4 — 소재·스프레드·전략자원 Loop 10**다.

[1]: https://www.reuters.com/business/energy/us-government-confirms-tesla-lg-energy-solutions-43-billion-battery-deal-2026-03-17/?utm_source=chatgpt.com "US government confirms Tesla and LG Energy Solution's $4.3 billion battery deal"
[2]: https://www.reuters.com/business/energy/tesla-signs-43-billion-battery-deal-with-lges-source-says-reducing-china-2025-07-30/?utm_source=chatgpt.com "Tesla signs $4.3 billion battery deal with LGES, source says, reducing China reliance"
[3]: https://www.reuters.com/business/energy/south-koreas-sk-signs-ess-battery-supply-deal-with-us-based-flatiron-energy-2025-09-03/?utm_source=chatgpt.com "South Korea's SK On signs ESS battery supply deal with US-based Flatiron Energy"
[4]: https://www.reuters.com/business/energy/south-koreas-sk-signs-energy-storage-battery-supply-deal-with-flatiron-energy-2025-09-03/?utm_source=chatgpt.com "South Korea's SK On signs energy storage battery supply deal with Flatiron Energy"
[5]: https://www.reuters.com/business/autos-transportation/ford-stock-surges-13-investor-optimism-new-energy-storage-business-2026-05-13/?utm_source=chatgpt.com "Ford stock surges 13% on investor optimism for new energy storage business"
[6]: https://www.ft.com/content/3788778f-ea93-4811-80a8-4c8f4c5c0b1f?utm_source=chatgpt.com "Ford shares surge after launch of power unit for data centres"
[7]: https://www.marketwatch.com/story/fords-stock-is-the-s-p-500s-biggest-gainer-the-carmaker-is-putting-a-very-tesla-spin-on-things-c3291673?utm_source=chatgpt.com "Ford's stock paces the S&P 500. The carmaker is putting a very Tesla spin on things."
[8]: https://www.reuters.com/business/battery-recycling-firm-redwood-raises-350-million-eclipse-ventures-nvidia-2025-10-23/?utm_source=chatgpt.com "Battery recycling firm Redwood raises $350 million from Eclipse Ventures, Nvidia"
[9]: https://www.businessinsider.com/google-redwood-materials-funding-round-2026-1?utm_source=chatgpt.com "Redwood Materials lands Google as a new investor"
[10]: https://www.investopedia.com/quantumscape-stock-pops-on-ev-battery-deal-with-volkswagen-s-powerco-8676584?utm_source=chatgpt.com "QuantumScape Stock Pops on EV Battery Deal with Volkswagen's PowerCo"
[11]: https://www.reuters.com/business/finance/south-koreas-lg-energy-solution-ends-65-billion-ev-battery-supply-deal-with-ford-2025-12-17/?utm_source=chatgpt.com "Ford cancels EV battery deal worth $6.5 billion with South Korea's LG Energy Solution"
[12]: https://www.reuters.com/business/energy/lg-energy-solution-cancels-39-trillion-won-battery-order-with-freudenberg-2025-12-26/?utm_source=chatgpt.com "LG Energy Solution cancels 3.9 trillion won battery order with Freudenberg"
[13]: https://www.reuters.com/legal/litigation/gms-restart-date-ohio-battery-plant-uncertain-2026-05-12/?utm_source=chatgpt.com "GM-LG's restart date at Ohio battery plant uncertain"
[14]: https://apnews.com/article/30792ad41c5148fb5528a2d0bcc0b59b?utm_source=chatgpt.com "GM lays off 1,700 workers at plants in Michigan and Ohio amid slower EV demand"
[15]: https://www.reuters.com/sustainability/climate-energy/qcells-furloughs-1000-workers-us-solar-factories-due-stalled-shipments-2025-11-08/?utm_source=chatgpt.com "Qcells furloughs 1,000 workers at US solar factories due to stalled shipments"
[16]: https://www.reuters.com/business/energy/orsted-flags-impairments-about-17-billion-us-rate-increases-2025-01-20/?utm_source=chatgpt.com "Orsted flags $1.7 bln impairment on Sunrise Wind delays, increased costs"
[17]: https://www.wsj.com/business/earnings/orsted-hits-earnings-target-despite-1-7-billion-impairment-on-u-s-project-delays-6e570d89?utm_source=chatgpt.com "Orsted Shares Plunge on $1.7 Billion Impairment"
[18]: https://www.theguardian.com/us-news/2025/jan/17/california-battery-plant-fire-monterey?utm_source=chatgpt.com "Fire reignites at California battery plant after evacuations amid toxic smoke"
[19]: https://www.sfchronicle.com/bayarea/article/fire-moss-landing-power-plant-forces-evacuations-20039639.php?utm_source=chatgpt.com "Evacuations lifted with still-burning Moss Landing fire under investigation"
[20]: https://arxiv.org/abs/2603.21592?utm_source=chatgpt.com "Battery health reporting fails independent validation across manufacturers"

좋아. **R1 Loop 2까지 끝났으니, 이번은 R2 Loop 2 — AI·반도체·전자부품**으로 넘어간다.

이번 R2 2회차의 목표는 1회차보다 더 날카롭게 나누는 거야.

```text
AI 수혜처럼 보이는 것
≠ 전부 같은 구조

HBM
AI 서버 ODM
Neocloud
반도체 장비
CoWoS/첨단패키징
광통신/PCB
AI 데이터센터 냉각
AI칩 pure-play
범용 DRAM/NAND
CXL·유리기판·뉴로모픽 테마

이걸 전부 따로 봐야 한다.
```

R2는 Theme Tag Map 기준으로 HBM, CXL, 시스템반도체, AI칩, 전공정/후공정 장비, 소재, PCB, 유리기판, OLED, MLCC, 클린룸, 스마트폰 부품 등을 흡수하는 대섹터다. 여기서 HBM은 Green 가능성이 높지만, CXL·뉴로모픽·유리기판·AI칩 관련주는 실제 채택·매출 전까지 Watch/Red로 둬야 한다는 기준이 이미 잡혀 있다.
또 R2에서 특히 중요한 건 공시·리포트에 없는 값을 만들지 않는 거다. Checkpoint 20의 OpenDART detail fetch 원칙처럼 계약금액, 계약기간, 매출 대비 계약금액, OP YoY 같은 값은 실제 확인된 필드만 써야 한다.
서생원식으로도 이 라운드는 “AI 테마”가 아니라 **EPS/FCF 체급 변화와 밸류에이션 리레이팅이 동시에 일어나는 구조**를 찾는 라운드다.

---

# R2 Loop 2. AI·반도체·전자부품

## 1. 이번 라운드 대섹터

```text
R2 = AI·반도체·전자부품
Loop 2 목표 = AI 인프라 안의 진짜 병목과 false-positive를 더 세밀하게 분리
```

기본 흐름은 이거다.

```text
AI CAPEX 증가
→ GPU / HBM / DRAM / NAND / CoWoS / PCB / optical / cooling / AI server 수요 증가
→ 공급 병목 또는 장기계약 발생
→ EPS/FCF 상향
→ 시장이 과거 시클리컬·부품주 프레임을 버림
→ 리레이팅
```

하지만 Loop 2에서는 이렇게 더 엄격하게 본다.

```text
HBM:
진짜 구조적 Green 후보. 단, 이미 급등한 뒤에는 4B-watch.

범용 DRAM/NAND:
EPS 회복은 강할 수 있지만 HBM식 장기 visibility는 낮음.

AI 서버 ODM/EMS:
매출은 커도 저마진·재고·회계·고객집중 리스크 큼.

Neocloud/GPU rental:
계약 visibility는 있으나 고부채·GPU 감가상각·고객집중이 큼.

첨단패키징/CoWoS:
병목은 강하지만 CAPA 정상화와 CAPEX cycle 감시.

광통신/PCB:
AI 데이터센터 병목으로 Green 가능성이 생겼지만 고객집중·과열 감시.

AI 냉각:
Green 가능. 다만 M&A 가격, debt, EPS accretion 확인.

AI칩 pure-play:
실제 고객·양산·수율·매출 전까지 Watch/Red.
```

---

## 2. 대상 canonical archetype

| canonical archetype                    | Loop 2 정책                                   |
| -------------------------------------- | ------------------------------------------- |
| `MEMORY_HBM_CAPACITY`                  | Green 가능. R2 최상위 핵심축                        |
| `COMMODITY_MEMORY_GENERAL_SEMI`        | Watch-to-Green. HBM보다 visibility 낮음         |
| `SEMI_EQUIPMENT_CAPEX`                 | Watch-to-Green. 고객사 CAPEX cycle 감시          |
| `SEMI_MATERIALS_PROCESS`               | Watch-to-Green. 반복납품·고객 다변화 확인              |
| `ADVANCED_PACKAGING_PCB`               | Watch-to-Green. AI optical PCB면 점수 강화       |
| `ADVANCED_PACKAGING_COWOS_EMIB`        | Green 가능. CAPA 정상화 4B 감시                    |
| `DISPLAY_OLED_SUPPLYCHAIN`             | Watch. 고객사 CAPEX·가격경쟁 확인                    |
| `ELECTRONIC_COMPONENTS_MLCC_SENSOR`    | Watch. 재고·고객집중 감시                           |
| `AI_CHIP_FABRIC_INFRA`                 | Watch. 고객사 계약·양산 전 Green 제한                 |
| `AI_ACCELERATOR_CHIP_PUREPLAY`         | High-risk Watch. valuation·Nvidia 경쟁 감시     |
| `AI_SERVER_ODM_EMS_SUPPLY_CHAIN`       | Watch-to-Green. 저마진·회계 overlay 필수           |
| `NEOCLOUD_GPU_RENTAL`                  | High-risk Watch. 고부채·FCF 전환 전 Green 금지      |
| `OPTICAL_NETWORKING_AI_DATACENTER`     | Green 가능. hyperscaler 계약·납품 필요              |
| `INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA` | Watch-to-Green. fab utility-like 매출 확인      |
| `AI_DATA_CENTER_COOLING`               | Green 가능. 실제 고객·수주·서비스 필요                   |
| `DATA_CENTER_REIT_INFRASTRUCTURE`      | Watch-to-Green. AFFO·tenant·funding cost 확인 |
| `AI_GRID_FLEXIBILITY_SOFTWARE`         | Watch. PoC → 반복 SW 매출 전환 필요                 |
| `REDTEAM_ACCOUNTING_TRUST_OVERLAY`     | hard gate. 감사·공시·내부통제 이슈 즉시 차단              |

---

## 3. deep sub-archetype

```text
MEMORY_HBM_CAPACITY
- HBM3E
- HBM4
- Nvidia supply chain
- CAPA constraint
- 장기계약
- 선수금
- price band
- AI memory rerating

COMMODITY_MEMORY_GENERAL_SEMI
- 범용 DRAM
- NAND
- AI server memory shortage
- HBM 생산 전환에 따른 범용 memory squeeze
- spot/contract price rebound

SEMI_EQUIPMENT_CAPEX
- EUV
- wafer fab equipment
- HBM fab CAPEX
- advanced node CAPEX
- packaging 장비
- 고객사 CAPEX cycle

ADVANCED_PACKAGING_COWOS_EMIB
- CoWoS-S
- CoWoS-L
- EMIB
- 2.5D packaging
- interposer
- substrate
- packaging bottleneck

ADVANCED_PACKAGING_PCB
- AI server PCB
- optical transceiver PCB
- high-layer PCB
- 유리기판
- CXL substrate
- lead time bottleneck

OPTICAL_NETWORKING_AI_DATACENTER
- 광섬유
- 광케이블
- optical transceiver
- laser
- silicon photonics
- AI data center interconnect

AI_SERVER_ODM_EMS_SUPPLY_CHAIN
- AI server rack
- ODM/EMS
- Foxconn
- Supermicro
- ASIC server
- consignment model
- inventory
- accounting risk

NEOCLOUD_GPU_RENTAL
- CoreWeave
- GPU cloud
- Nvidia GPU collateral
- OpenAI/Microsoft contract
- debt financing
- GPU depreciation
- customer concentration

AI_DATA_CENTER_COOLING
- liquid cooling
- direct liquid cooling
- immersion cooling
- HVAC
- coolant monitoring
- data center thermal management

AI_CHIP_FABRIC_INFRA
- system semiconductor
- foundry
- Tesla AI chip
- AI accelerator
- tape-out
- yield
- customer validation

INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA
- 초고순도 질소
- fab gas plant
- onsite utility
- long-term supply contract

REDTEAM_ACCOUNTING_TRUST_OVERLAY
- auditor resignation
- filing delay
- internal control weakness
- DOJ/SEC investigation
- related-party transaction
```

---

# 4. 성공사례

## 4-1. SK하이닉스 HBM / AI memory rerating — `MEMORY_HBM_CAPACITY`

SK하이닉스는 R2의 가장 강한 구조적 성공사례다. AI 서버에 필요한 HBM과 기존 메모리 수요가 겹치면서 주가가 2025년에 274%, 2026년에 200% 이상 상승했고, 시가총액은 16개월 전 1,000억 달러 미만에서 약 9,420억 달러까지 올라 1조 달러에 근접했다. 이건 단순 DRAM 사이클이 아니라 **메모리 = AI 인프라 병목**이라는 밸류에이션 프레임 전환이 가격경로로 확인된 사례다. ([Reuters][1])

**가격경로 1차 판정**

```text
가격경로:
2025년 +274%
2026년 +200% 이상
시총 약 $942B

판정:
STRUCTURAL_SUCCESS_ALIGNED + 4B_WATCH

의미:
Stage 3 성공사례로 유지.
다만 이미 모두가 AI memory rerating을 인정하는 구간이라 4B-watch 필수.
```

**Loop 2 교정**

```text
MEMORY_HBM_CAPACITY는 R2 최상위 Green 가능 archetype.
하지만 2회차부터는 4B 조건을 더 강하게 둔다.

4B 조건:
- 1~2년 급등
- 시총/밸류에이션 포화
- 모두가 AI memory rerating 인정
- 고객사 가격저항 가능성
- CAPA 증설 뉴스 증가
- AI CAPEX 둔화 가능성
```

---

## 4-2. Applied Materials / AI 장비·패키징 CAPEX — `SEMI_EQUIPMENT_CAPEX`, `ADVANCED_PACKAGING_COWOS_EMIB`

Applied Materials는 AI CAPEX가 장비·패키징 매출로 연결되는 좋은 성공 후보야. 2026년 3분기 매출 전망을 약 89.5억 달러로 제시해 시장 예상 80.9억 달러를 웃돌았고, 2026년 반도체 장비 사업은 30% 이상, packaging revenue는 50% 이상 증가할 것으로 전망했다. 발표 후 주가는 시간외에서 3% 상승했다. ([Reuters][2])

**가격경로 1차 판정**

```text
가격 반응:
실적·가이던스 후 시간외 +3%

판정:
EARLY_ALIGNED_CANDIDATE

의미:
AI CAPEX가 장비·패키징으로 실제 매출 가이던스에 반영됨.
하지만 고객사 CAPEX cycle과 order push-out은 계속 감시해야 함.
```

**Loop 2 교정**

```text
SEMI_EQUIPMENT_CAPEX:
Green 가능은 아니고 Watch-to-Green.
HBM 생산업체보다 visibility를 낮춘다.

이유:
- 고객사 CAPEX에 종속
- 수출통제
- order push-out
- CAPEX peak 이후 둔화
```

---

## 4-3. Nvidia CoWoS-L / packaging 병목 — `ADVANCED_PACKAGING_COWOS_EMIB`

Nvidia CEO Jensen Huang은 Blackwell에서 CoWoS-L을 주로 사용하고 있으며, advanced packaging 수요가 줄어든 것이 아니라 CoWoS-S에서 CoWoS-L로 바뀌고 있다고 설명했다. 그는 packaging capacity가 2년 사이 크게 늘었지만, 여전히 병목이라고 말했다. ([Reuters][3])

**가격경로 1차 판정**

```text
판정:
PACKAGING_BOTTLENECK_REFERENCE

의미:
CoWoS/첨단패키징은 AI 공급망의 독립 병목으로 유지.
단, CAPA가 계속 늘면 4B-watch.
```

**Loop 2 교정**

```text
ADVANCED_PACKAGING_COWOS_EMIB:
Bottleneck/Pricing 점수 유지.
Risk penalty에 bottleneck_normalization 추가.
```

---

## 4-4. Broadcom / optical PCB·laser 병목 — `OPTICAL_NETWORKING_AI_DATACENTER`, `ADVANCED_PACKAGING_PCB`

Broadcom은 AI 칩 수요가 TSMC capacity뿐 아니라 laser와 optical transceiver PCB supply chain까지 압박하고 있다고 밝혔다. 특히 optical transceiver용 PCB lead time이 6주에서 6개월로 늘었다고 설명했다. 이건 AI 병목이 GPU/HBM에서 광통신·PCB·laser로 확산되고 있음을 보여준다. ([Reuters][4])

**가격경로 1차 판정**

```text
판정:
OPTICAL_PCB_BOTTLENECK_REFERENCE

의미:
AI optical networking과 AI server PCB는 R2에서 Green 가능 하위축으로 상향.
다만 고객사 수주·납품·OPM 확인 전까지 Stage 3 금지.
```

**Loop 2 교정**

```text
OPTICAL_NETWORKING_AI_DATACENTER:
Visibility와 Bottleneck 점수 유지/강화.

ADVANCED_PACKAGING_PCB:
일반 PCB와 AI optical PCB를 분리.
AI optical PCB는 점수 강화.
```

---

## 4-5. Foxconn AI 서버 ODM — `AI_SERVER_ODM_EMS_SUPPLY_CHAIN`

Foxconn은 2026년 1분기 순이익이 전년 대비 19% 증가했고, AI 서버 rack shipments가 올해 두 배 이상 늘 것으로 예상했다. AI 서버 생산능력 확장을 위해 CAPEX도 전년 대비 30% 늘릴 계획이다. 다만 Foxconn 주가는 올해 6% 상승에 그쳐 대만 지수 44% 상승을 밑돌았고, 일부 cloud/networking 제품은 고객이 핵심 부품을 제공하는 consignment model로 바뀌고 있다고 설명했다. ([Reuters][5])

**가격경로 1차 판정**

```text
판정:
AI_SERVER_REVENUE_SUCCESS_BUT_MARGIN_VISIBILITY_WATCH

좋은 점:
- 순이익 증가
- AI server rack shipment 2배 이상 전망
- AI server CAPEX 확대

주의:
- 주가가 지수 대비 강하지 않음
- consignment model이면 매출·마진 구조 해석 필요
- ODM/EMS는 HBM보다 margin power가 약할 수 있음
```

**Loop 2 교정**

```text
AI_SERVER_ODM_EMS:
EPS/FCF 점수는 유지.
Visibility는 중간.
Bottleneck은 HBM보다 낮게.
Risk penalty에 low_margin_assembly, inventory, accounting_trust 강화.
```

---

## 4-6. Ecolab–CoolIT / AI 데이터센터 냉각 — `AI_DATA_CENTER_COOLING`

Ecolab은 AI 데이터센터 액체냉각 수요를 잡기 위해 CoolIT Systems를 47.5억 달러에 인수하기로 했다. CoolIT은 Nvidia와 AMD 같은 칩메이커에 액체냉각 시스템을 공급하고, 향후 12개월 매출이 약 5.5억 달러로 예상된다. 이 딜은 2026년 3분기 종결 예정이며, Ecolab은 2028년부터 조정 EPS에 accretive할 것으로 봤다. ([Reuters][6])

**가격경로 1차 판정**

```text
판정:
STRATEGIC_COOLING_SUCCESS_CANDIDATE

좋은 점:
- AI 데이터센터 냉각 수요
- Nvidia/AMD supply exposure
- CoolIT 매출 가시성
- EPS accretion 계획

주의:
- 인수가 47.5억 달러
- 주가는 premarket -1%
- debt financing과 valuation multiple 확인 필요
```

**Loop 2 교정**

```text
AI_DATA_CENTER_COOLING:
Green 가능 유지.
다만 M&A 가격과 debt 부담을 4B/RedTeam에 포함.
```

---

## 4-7. CoreWeave / Neocloud — `NEOCLOUD_GPU_RENTAL`

CoreWeave는 OpenAI와 5년 119억 달러 계약을 맺고 IPO를 추진했으며, 2024년 매출은 19.2억 달러였지만 순손실은 8.634억 달러였다. Microsoft가 매출의 약 3분의 2를 차지했고, IPO 목표 valuation은 최대 260억 달러였지만 이후 IPO가 40달러로 낮아지고 raise 규모도 줄었다. ([Reuters][7])
CoreWeave는 원래 47~55달러 범위를 목표로 했지만 40달러에 가격을 정했고, 매출의 62%가 Microsoft에서 나오며 80억 달러 부채와 2024년 8.63억 달러 순손실을 안고 있었다는 점도 보고됐다. ([Investopedia][8])

**가격경로 1차 판정**

```text
판정:
HIGH_RISK_WATCH_CANDIDATE

좋은 점:
- OpenAI 대형계약
- AI compute 수요
- revenue growth

주의:
- IPO downsize
- Microsoft 집중
- 고부채
- 대규모 순손실
- GPU 감가상각
- refinancing risk
```

**Loop 2 교정**

```text
NEOCLOUD_GPU_RENTAL:
Visibility는 계약 때문에 높게 줄 수 있음.
하지만 EPS/FCF와 Capital risk가 너무 커서 Green 금지.

Stage 3 조건:
- FCF 전환
- debt/EBITDA 안정
- 고객 다변화
- GPU depreciation 관리
```

---

## 4-8. Supermicro / AI 서버 회계 hard 4C — `REDTEAM_ACCOUNTING_TRUST_OVERLAY`

Supermicro는 AI 서버 수요로 2023년 초 약 44억 달러였던 시가총액이 2024년 3월 670억 달러까지 올랐지만, Ernst & Young이 감사인에서 사임하자 주가가 30% 이상 급락했다. EY는 경영진과 감사위원회의 진술을 더 이상 신뢰할 수 없다고 밝혔다. Supermicro는 annual report filing delay, Hindenburg의 회계조작 주장, DOJ 조사 보도까지 겹쳤다. ([Reuters][9])

**가격경로 1차 판정**

```text
판정:
EARLY_RERATING_SUCCESS_THEN_HARD_4C

의미:
AI 서버 매출 성장만으로 Stage 3 유지 불가.
회계·감사 신뢰도는 R2 전체 hard gate.
```

**Loop 2 교정**

```text
R2 전체 hard gate:
- auditor_resignation
- filing_delay
- internal_control_issue
- related_party_transaction
- DOJ/SEC investigation

발생 시:
Stage 3-Green 즉시 금지
RedTeam hard finding
price_validation 우선순위 최상위
```

---

# 5. 반례

## 5-1. AI 서버 ODM/EMS 저마진·재고 리스크

Foxconn의 AI 서버 rack shipment 전망은 강하지만, ODM/EMS 모델은 HBM처럼 가격결정력을 쥔 병목이 아니다. 특히 고객이 핵심 부품을 제공하는 consignment model이 확대되면 매출총액, 마진, working capital 해석이 복잡해진다. Foxconn 주가가 올해 6% 상승에 그쳐 대만 지수 44% 상승을 밑돈 점도 가격경로상 “실적은 좋지만 리레이팅은 제한적”이라는 신호다. ([Reuters][5])

```text
교훈:
AI server shipment growth
≠ HBM식 Green

필수 확인:
gross margin
inventory
customer concentration
consignment model impact
OP/EPS revision
```

---

## 5-2. Neocloud 고부채·고객집중

CoreWeave는 AI cloud 수요의 직접 수혜지만, IPO가 낮아진 것과 고부채·고객집중·순손실은 R2의 강한 반례다. OpenAI 계약은 visibility를 높이지만, Microsoft 집중, 80억 달러 부채, 순손실 구조가 해결되지 않으면 Green이 아니라 high-risk Watch다. ([Reuters][7])

```text
교훈:
take-or-pay 또는 대형계약
≠ FCF 안정

Neocloud는:
revenue growth보다 debt/FCF/customer concentration을 먼저 봐야 한다.
```

---

## 5-3. Supermicro 회계 신뢰도 붕괴

Supermicro는 R2에서 “좋은 AI 서버 수요 + 나쁜 회계 신뢰도”가 어떻게 가격경로를 뒤집는지 보여주는 기준 반례다. AI 서버 매출 성장과 시가총액 폭증이 있었더라도 감사인 사임 하나로 Stage 3 논리는 즉시 깨진다. ([Reuters][9])

```text
교훈:
R2 후보는 회계·공시 신뢰도가 깨지면 점수가 의미 없다.
```

---

## 5-4. Samsung one-stop strategy / 내부 갈등 리스크

Samsung은 AI boom 속에서 메모리 부문과 logic/foundry 부문 간 보상 격차가 커지며 노조가 2026년 5월 21일부터 18일 파업을 예고한 상태로 보도됐다. 이 사안은 단순 노사 이슈를 넘어, Samsung의 memory·logic·foundry를 아우르는 one-stop semiconductor 전략에도 부담이 될 수 있다는 지적이 있다. ([Reuters][10])

```text
교훈:
반도체 대형주도 내부 실행력·인력 이탈·파업 리스크를 RedTeam에 넣어야 한다.

특히:
HBM 경쟁력
foundry 수율
logic chip execution
인력 유지
```

---

## 5-5. Cooling M&A valuation risk

Ecolab–CoolIT은 전략적으로는 성공 후보지만, 47.5억 달러 현금 인수와 2028년부터 EPS accretive라는 긴 시간표 때문에 valuation·debt risk가 존재한다. Reuters는 발표 당시 Ecolab 주가가 premarket에서 1% 하락했다고 보도했다. ([Reuters][6])

```text
교훈:
AI 냉각은 Green 가능하지만,
M&A 가격과 EPS accretion timing을 확인해야 한다.
```

---

# 6. 4B-watch 사례

## 6-1. SK하이닉스 / HBM 4B-watch

```text
4B 조건:
- 2025년 +274%, 2026년 +200% 이상
- 시총 $942B 수준
- 모두가 AI memory rerating 인정
- SK하이닉스가 Nvidia HBM 핵심 공급자로 인식
- 고객사 가격저항과 CAPA 증설 가능성 증가
```

SK하이닉스는 R2의 최고 성공사례이면서 동시에 가장 중요한 4B-watch다. ([Reuters][1])

---

## 6-2. Applied Materials / 장비 CAPEX 4B-watch

```text
4B 조건:
- AI WFE·packaging growth를 모두가 인정
- 장비업체 가이던스가 연속 상향
- 고객사 CAPEX peak 가능성
- 수출통제·order push-out 리스크를 시장이 무시
```

Applied Materials는 가이던스 상향과 주가 +3% 반응이 있는 성공 후보지만, 장비주는 항상 고객 CAPEX cycle의 4B/4C를 봐야 한다. ([Reuters][2])

---

## 6-3. CoWoS / packaging 4B-watch

```text
4B 조건:
- CoWoS 병목을 모두가 인정
- 장비·기판·소재주가 동반 과열
- CAPA 확장 뉴스 증가
- lead time 정상화
- CoWoS-S → CoWoS-L 전환을 수요 감소로 오해하거나 반대로 과대해석
```

Nvidia는 CoWoS 수요가 줄어드는 게 아니라 기술 종류가 바뀌고 있다고 설명했지만, capacity가 지난 2년간 크게 늘었다는 점도 같이 봐야 한다. ([Reuters][3])

---

## 6-4. Optical networking / PCB 4B-watch

```text
4B 조건:
- optical transceiver, laser, PCB lead time 병목이 알려짐
- 관련주 valuation 과열
- 고객사 집중
- 신규 진입·CAPA 증설로 병목 완화 가능성
```

Broadcom은 optical transceiver PCB lead time이 6주에서 6개월로 늘었다고 했지만, 신규 진입과 capacity expansion이 eventual solution이 될 수 있다고도 봤다. ([Reuters][4])

---

## 6-5. Neocloud 4B-watch

```text
4B 조건:
- AI cloud 계약 규모만 보고 valuation 상승
- FCF 적자와 부채를 시장이 무시
- Microsoft/OpenAI/Nvidia 관계를 circular growth로 과대평가
- GPU 감가상각과 refinancing risk가 후행 반영
```

CoreWeave는 큰 계약과 높은 성장성이 있지만, IPO downsize와 부채·고객집중 때문에 4B가 아니라 4C-watch까지 같이 봐야 한다. ([Reuters][7])

---

# 7. 4C-thesis-break 사례

## 7-1. 감사인 사임 / Supermicro

```text
4C:
auditor_resignation
filing_delay
internal_control_weakness
DOJ/SEC investigation
related_party_transaction_risk
```

Supermicro는 이 4C 기준을 R2 전체에 박아야 하는 사례다. ([Reuters][9])

---

## 7-2. Neocloud refinancing pressure

```text
4C-watch:
debt_refinancing_pressure
GPU_obsolescence
customer_concentration
FCF_negative
IPO_downsize
```

CoreWeave는 매출 성장만으로는 Green이 될 수 없고, debt/FCF/customer concentration이 먼저 통과되어야 한다. ([Investopedia][8])

---

## 7-3. 고객사 CAPEX cut / 장비·패키징

```text
4C-watch:
AI_CAPEX_cut
order_pushout
export_control
customer_CAPEX_peak
packaging_CAPA_normalization
```

Applied Materials와 Nvidia/CoWoS 사례는 성공 근거지만, 바로 같은 이유로 고객사 CAPEX가 꺾이면 장비·패키징은 빠르게 4C로 전환될 수 있다. ([Reuters][2])

---

## 7-4. Optical·PCB 병목 정상화

```text
4C-watch:
lead_time_normalization
new_capacity
hyperscaler_order_delay
inventory_build
customer_concentration
```

Broadcom은 병목을 인정하면서도 신규 진입과 capacity expansion이 해결책이 될 수 있다고 말했다. 즉 optical/PCB는 Green 가능이지만, lead time 정상화가 4B/4C 조건이다. ([Reuters][4])

---

## 7-5. Cooling M&A debt/overpay

```text
4C-watch:
M&A_overpay
debt_financing
EPS_accretion_delay
integration_risk
AI_CAPEX_delay
```

Ecolab–CoolIT은 AI cooling 성공 후보지만, 인수가격·debt·2028년 EPS accretion 시점은 반드시 검증해야 한다. ([Reuters][6])

---

# 8. 점수비중 보정표 — R2 Loop 2 / v2.0

| canonical archetype                    | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | Loop 2 핵심 감점                                 |
| -------------------------------------- | ------: | ---------: | ---------: | ---------: | --------: | ------: | ---: | -------------------------------------------- |
| `MEMORY_HBM_CAPACITY`                  |      24 |         21 |         19 |         14 |        11 |       0 |    5 | crowding, CAPEX reversal, 고객 가격저항            |
| `COMMODITY_MEMORY_GENERAL_SEMI`        |      22 |         16 |         17 |         13 |        10 |       0 |    5 | spot rebound, supply rebound, HBM lag        |
| `SEMI_EQUIPMENT_CAPEX`                 |      22 |         20 |         18 |         14 |        12 |       0 |    5 | 고객 CAPEX, order delay, 수출통제                  |
| `SEMI_MATERIALS_PROCESS`               |      20 |         18 |         14 |         13 |        11 |       0 |    5 | 고객집중, 재고, 단가 압박                              |
| `ADVANCED_PACKAGING_PCB`               |      21 |         21 |         19 |         13 |        12 |       0 |    5 | 고객집중, CAPA 정상화, inventory                    |
| `ADVANCED_PACKAGING_COWOS_EMIB`        |      22 |         21 |         20 |         14 |        12 |       0 |    5 | CAPEX cycle, yield, bottleneck normalization |
| `DISPLAY_OLED_SUPPLYCHAIN`             |      19 |         18 |         12 |         13 |        11 |       0 |    5 | 패널 가격경쟁, CAPEX cycle                         |
| `ELECTRONIC_COMPONENTS_MLCC_SENSOR`    |      19 |         17 |         13 |         12 |        11 |       1 |    5 | 재고, 고객집중, 중국 공급망                             |
| `AI_CHIP_FABRIC_INFRA`                 |      18 |         15 |         12 |         14 |        11 |       0 |    5 | 고객검증, 수율, 매출 부재                              |
| `AI_ACCELERATOR_CHIP_PUREPLAY`         |      18 |         15 |         13 |         15 |        10 |       0 |    5 | Nvidia 경쟁, valuation 과열, R&D burn            |
| `AI_SERVER_ODM_EMS_SUPPLY_CHAIN`       |      22 |         18 |         15 |         14 |        10 |       0 |    5 | 저마진, inventory, 회계, 고객집중                     |
| `NEOCLOUD_GPU_RENTAL`                  |      18 |         21 |         18 |         14 |         9 |       0 |    5 | 고부채, GPU 감가상각, FCF 적자                        |
| `OPTICAL_NETWORKING_AI_DATACENTER`     |      21 |         22 |         20 |         13 |        12 |       0 |    5 | 고객집중, valuation crowding, lead time 정상화      |
| `INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA` |      19 |         23 |         13 |         13 |        12 |       3 |    5 | fab 지연, 고객집중, 에너지비                           |
| `AI_DATA_CENTER_COOLING`               |      21 |         22 |         22 |         13 |        12 |       0 |    5 | M&A overpay, debt, AI CAPEX 지연               |
| `DATA_CENTER_REIT_INFRASTRUCTURE`      |      18 |         23 |         18 |         13 |        13 |       5 |    5 | CAPEX, funding cost, tenant concentration    |
| `AI_GRID_FLEXIBILITY_SOFTWARE`         |      17 |         17 |         15 |         13 |        10 |       0 |    6 | PoC, 상용화 지연                                  |
| `REDTEAM_ACCOUNTING_TRUST_OVERLAY`     |    gate |       gate |       gate |       gate |      gate |    gate | gate | auditor resignation, filing delay            |

Loop 2에서 가장 중요한 보정은 이거다.

```text
1. HBM은 성공사례지만 mispricing/valuation 점수는 일부 낮춘다.
   이미 시장이 많이 인정했기 때문이다.

2. AI server ODM은 EPS 점수는 높게 유지하되,
   Visibility와 Valuation 점수를 낮춘다.
   이유는 저마진·재고·회계 리스크 때문이다.

3. Neocloud는 visibility는 계약 때문에 높지만,
   valuation/capital risk가 너무 커서 Green 금지.

4. Optical/PCB는 AI 병목으로 점수 강화.
   단, lead time 정상화가 4B/4C 조건.

5. Cooling은 Green 가능 유지.
   단, M&A overpay/debt risk 추가.
```

---

# 9. stage date 후보

## `MEMORY_HBM_CAPACITY`

```text
Stage 1:
AI 서버 HBM 수요 급증, Nvidia 공급망, HBM 가격/계약 뉴스

Stage 2:
HBM 매출 비중 상승, 실적 서프라이즈, OP/EPS 상향 확인일

Stage 3:
장기계약·선수금·CAPA constraint·multi-year EPS revision 확인일

Stage 4B:
시총/valuation 포화, 모두가 AI memory rerating 인정, crowded trade 확인일

Stage 4C:
AI CAPEX 둔화, HBM 가격 하락, CAPA 과잉, 고객사 주문 축소
```

## `SEMI_EQUIPMENT_CAPEX`

```text
Stage 1:
고객사 AI/HBM fab CAPEX 발표

Stage 2:
장비사 수주·가이던스 상향·backlog 증가

Stage 3:
수주가 매출/OP/EPS로 전환되고 valuation frame 변화

Stage 4B:
장비주 동반 과열, 고객사 CAPEX peak, 목표가 과밀

Stage 4C:
order push-out, 수출통제, CAPEX cut
```

## `ADVANCED_PACKAGING_COWOS_EMIB`

```text
Stage 1:
Nvidia/AMD/Broadcom 등 packaging bottleneck 언급

Stage 2:
CoWoS/EMIB 장비·기판·소재 수주 증가

Stage 3:
packaging revenue growth와 EPS 상향 확인

Stage 4B:
병목 consensus 과밀, CAPA 증설 본격화

Stage 4C:
병목 완화, yield issue, 고객사 CAPEX 지연
```

## `AI_SERVER_ODM_EMS_SUPPLY_CHAIN`

```text
Stage 1:
AI server rack 수요 증가, hyperscaler·Nvidia server demand 뉴스

Stage 2:
AI server 매출·shipment·OP 증가 확인

Stage 3:
AI server mix가 회사 전체 EPS/FCF 체급을 바꾼 시점

Stage 4B:
AI server 관련주 valuation 과열

Stage 4C:
감사인 사임, filing delay, 재고 증가, 저마진, 고객집중
```

## `NEOCLOUD_GPU_RENTAL`

```text
Stage 1:
대형 GPU cloud 계약, IPO filing, OpenAI/Microsoft 계약

Stage 2:
contract backlog, revenue growth, EBITDA improvement 확인

Stage 3:
FCF 전환 또는 debt/EBITDA 안정화 확인

Stage 4B:
AI cloud valuation 과열

Stage 4C:
refinancing pressure, GPU obsolescence, customer concentration, FCF negative
```

## `OPTICAL_NETWORKING_AI_DATACENTER`

```text
Stage 1:
AI 데이터센터 optical networking 병목 뉴스

Stage 2:
hyperscaler 계약, lead time 증가, 수주 evidence 확인

Stage 3:
OP/EPS 상향 + 장기계약 + 병목 프레임 전환

Stage 4B:
valuation crowding, optical 관련주 동반 과열

Stage 4C:
CAPA 정상화, 고객사 CAPEX 지연, 주문 취소
```

## `AI_DATA_CENTER_COOLING`

```text
Stage 1:
AI 데이터센터 열밀도 상승, liquid cooling adoption 뉴스

Stage 2:
실제 고객·수주·인수·매출 가시성 확인

Stage 3:
반복 서비스·유지보수·EPS accretion 확인

Stage 4B:
AI cooling M&A/valuation 과열

Stage 4C:
AI CAPEX 지연, M&A overpay, debt 부담, EPS accretion 지연
```

---

# 10. 가격경로 검증계획

## R2 Loop 2 공통 검증 방식

```text
1. 각 case의 stage1_date, stage2_date, stage3_date를 지정한다.
2. 해당 날짜의 종가를 stage_price로 저장한다.
3. MFE_30D / 90D / 180D / 1Y / 2Y를 계산한다.
4. MAE_30D / 90D / 180D / 1Y를 계산한다.
5. peak_price와 drawdown_after_peak를 계산한다.
6. EPS revision, revenue guidance, backlog, margin, customer concentration, accounting flag와 가격경로를 비교한다.
```

## Loop 2에서 새로 강제할 판정

```text
structural_ai_bottleneck_aligned:
AI 병목이 실제 매출/EPS/가격경로로 이어짐.

ai_revenue_but_margin_watch:
매출은 늘었지만 마진·재고·고객집중 때문에 Green 제한.

ai_contract_visibility_but_leverage_risk:
계약은 강하지만 고부채·FCF 적자로 Green 금지.

bottleneck_normalization_4b:
병목은 맞지만 CAPA·신규 진입으로 정상화 위험.

accounting_trust_break_4c:
감사·공시·내부통제 이슈로 thesis break.

theme_without_revenue:
CXL·유리기판·AI칩·뉴로모픽이 실제 매출 없이 테마로만 움직임.
```

## 이번 R2 Loop 2에서 우선 검증할 가격 case

| case_id                                      |              stage2 후보일 | 현재 1차 가격판정                                  |
| -------------------------------------------- | ----------------------: | ------------------------------------------- |
| `sk_hynix_hbm_rerating_success_case`         | 2025~2026 주요 실적·HBM 계약일 | +274%, +200% 이상. structural aligned + 4B    |
| `applied_materials_ai_packaging_growth_case` |              2026-05-14 | 시간외 +3%, early aligned                      |
| `nvidia_cowos_l_transition_case`             |              2025-01-16 | packaging bottleneck reference              |
| `broadcom_optical_pcb_leadtime_case`         |              2026-03-24 | optical/PCB bottleneck reference            |
| `foxconn_ai_server_rack_growth_case`         |              2026-05-14 | AI server revenue success but margin watch  |
| `ecolab_coolit_liquid_cooling_case`          |              2026-03-20 | strategic cooling candidate, M&A/debt watch |
| `coreweave_openai_contract_ipo_case`         |                 2025-03 | high-risk neocloud watch                    |
| `coreweave_downsized_ipo_debt_case`          |                 2025-03 | debt/customer concentration 4C-watch        |
| `supermicro_ey_resignation_case`             |              2024-10-30 | hard 4C                                     |
| `samsung_ai_boom_labor_execution_case`       |              2026-05-15 | execution/labor RedTeam                     |
| `commodity_memory_price_rebound_case`        |                   case별 | HBM과 구분 필요                                  |
| `cxl_glass_substrate_theme_case`             |                   case별 | actual revenue before Green                 |

---

# 11. 다음에 에이전트가 채워야 할 price fields

R2 Loop 2에서는 아래 필드를 채우게 해야 한다.

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

hbm_revenue_share
hbm_capacity_growth
hbm_contract_duration
hbm_price_band_flag
prepayment_flag
customer_name
nvidia_supply_chain_flag

memory_spot_price_change
memory_contract_price_change
dram_nand_mix
commodity_memory_supply_rebound_flag

equipment_order_growth
equipment_backlog
customer_capex_growth
order_pushout_flag
export_control_flag

packaging_revenue_growth
cowos_capacity_growth
cowos_l_flag
yield_issue_flag
bottleneck_normalization_flag

pcb_lead_time_weeks
optical_transceiver_order
laser_supply_constraint_flag
hyperscaler_contract_flag

ai_server_revenue
ai_server_rack_shipments
ai_server_margin
consignment_model_flag
inventory_growth
customer_concentration

gpu_cloud_revenue
gpu_cloud_contract_value
take_or_pay_flag
debt_to_ebitda
net_debt
fcf_margin
gpu_depreciation
refinancing_risk_flag

cooling_revenue
liquid_cooling_order
mna_price
mna_debt_financing_flag
eps_accretion_year

auditor_resignation_flag
filing_delay_flag
internal_control_issue_flag
regulatory_probe_flag
related_party_risk_flag

labor_strike_flag
execution_risk_flag
foundry_yield_risk_flag

score_price_alignment
price_validation_status
review_notes
```

---

# R2 Loop 2 결론

이번 2회차에서 R2는 더 선명해졌다.

```text
강한 Green 후보:
HBM
AI optical networking
advanced packaging
AI data center cooling
반도체용 industrial gas
일부 AI data center power/infra

Watch-to-Green:
반도체 장비
반도체 소재
AI server ODM
범용 DRAM/NAND
AI server PCB
AI chip fabric infra

High-risk Watch:
Neocloud GPU rental
AI accelerator pure-play
AI server ODM 중 저마진·고객집중 높은 기업
데이터센터 REIT

Red/4C 방어:
Supermicro식 회계·감사 리스크
CoreWeave식 고부채·고객집중
CXL·유리기판·뉴로모픽 theme-only
AI칩 관련주 but 실제 매출 없음
AI CAPEX cut
packaging/optical bottleneck normalization
```

**R2 Loop 2 점수정규화의 핵심 문장:**

> AI·반도체·전자부품은 “AI 수혜”가 아니라 **HBM, 장비, 패키징, 광통신, 냉각, 서버 ODM, neocloud, AI칩 pure-play의 경제구조가 서로 다르다**는 걸 먼저 인정해야 한다.
> EPS/FCF와 가격경로가 같이 맞은 축만 Green 후보이고, 고부채·회계·고객집중·매출 부재·CAPA 정상화는 즉시 RedTeam이다.

다음에 같은 지시가 오면 순서대로 **R3 — 2차전지·전기차·친환경 Loop 2**로 넘어간다.

[1]: https://www.reuters.com/world/asia-pacific/ai-boom-puts-sk-hynix-cusp-1-trillion-market-value-2026-05-14/?utm_source=chatgpt.com "AI boom puts SK Hynix on cusp of $1 trillion market value"
[2]: https://www.reuters.com/business/applied-materials-sees-quarterly-revenue-above-estimates-2026-05-14/?utm_source=chatgpt.com "Applied Materials sees quarterly revenue above estimates on sustained AI spending"
[3]: https://www.reuters.com/technology/nvidia-ceo-says-its-advanced-packaging-technology-needs-are-changing-2025-01-16/?utm_source=chatgpt.com "Nvidia CEO says its advanced packaging technology needs are changing"
[4]: https://www.reuters.com/world/asia-pacific/broadcom-flags-supply-constraints-says-tsmc-capacity-bottleneck-2026-03-24/?utm_source=chatgpt.com "Broadcom flags supply constraints, says TSMC capacity a bottleneck"
[5]: https://www.reuters.com/world/china/taiwans-foxconn-reports-185-rise-q1-profit-beats-forecast-2026-05-14/?utm_source=chatgpt.com "Foxconn reports forecast-beating 19% jump in Q1 profit on AI demand"
[6]: https://www.reuters.com/business/ecolab-acquire-coolit-systems-475-billion-2026-03-20/?utm_source=chatgpt.com "Ecolab to buy CoolIT for $4.75 billion to tap into AI data center boom"
[7]: https://www.reuters.com/technology/nvidia-backed-coreweave-aims-raise-up-27-billion-us-ipo-2025-03-20/?utm_source=chatgpt.com "Nvidia-backed CoreWeave targets $26 billion valuation in AI IPO test"
[8]: https://www.investopedia.com/nvidia-backed-coreweave-prices-its-ipo-at-usd40-per-share-below-expectations-11701963?utm_source=chatgpt.com "Nvidia-Backed CoreWeave Prices Its IPO at $40 Per Share, Below Expectations"
[9]: https://www.reuters.com/technology/super-micro-computer-says-ernst-young-resigns-its-accountant-shares-tank-2024-10-30/?utm_source=chatgpt.com "Super Micro Computer says Ernst & Young resigns as auditor, shares tank"
[10]: https://www.reuters.com/business/world-at-work/samsung-global-ai-boom-spurred-looming-strike-deep-divisions-2026-05-15/?utm_source=chatgpt.com "At Samsung, the global AI boom spurred a looming strike and deep divisions"

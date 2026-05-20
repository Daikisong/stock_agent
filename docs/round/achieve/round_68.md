좋아. **R1 Loop 3까지 끝났으니, 이번은 R2 Loop 3 — AI·반도체·전자부품**으로 넘어간다.

R2는 Theme Tag Map 기준으로 HBM, CXL, 시스템반도체, 뉴로모픽, 퓨리오사AI 관련주, 전공정·후공정 장비, 반도체 소재, PCB, 유리기판, MLCC, OLED, 클린룸, 스마트폰 부품, 카메라, 무선충전까지 흡수하는 대섹터다. 이 지도에서도 핵심은 **HBM은 Green 가능성이 높지만, CXL·뉴로모픽·유리기판·AI칩 관련주는 실제 채택·매출 전까지 Watch/Red**로 분리하는 것이다.

또 Checkpoint 20 원칙처럼 계약금액, 계약기간, 매출 대비 계약금액, 고객사, 납품기간, OP YoY, CAPA, 가동률, 장기계약, 선수금 같은 값은 실제 공시·리포트·기사에서 확인될 때만 써야 한다. 특히 R2는 AI 수혜라는 단어 하나로 점수가 과열되기 쉬우므로, 없는 값을 추정으로 채우면 바로 false-positive가 된다.

서생원식으로 보면 R2는 “AI 테마”가 아니라 **AI 인프라 병목 → EPS/FCF 체급 변화 → 시장의 과거 사이클 프레임 붕괴 → 밸류에이션 리레이팅**이 실제로 연결되는지를 보는 라운드다.

---

# R2 Loop 3. AI·반도체·전자부품

## 1. 이번 라운드 대섹터

```text
R2 = AI·반도체·전자부품
Loop 3 목표 = AI 수혜를 HBM / 범용 메모리 / 장비 / 패키징 / 광통신 / 서버 ODM / 네오클라우드 / 냉각 / AI칩 테마로 더 잘게 분해
```

이번 회차의 핵심 질문은 이거다.

```text
이 회사는 AI 수혜주인가?
아니면 AI 인프라 병목을 실제 매출·마진·EPS·FCF로 바꾸는 회사인가?
```

R2에서 제일 위험한 오판은 이거다.

```text
AI 수혜
= 무조건 Green
```

실제로는 이렇게 갈라야 한다.

```text
진짜 구조 후보:
HBM
첨단패키징
AI optical networking
AI 데이터센터 냉각
일부 반도체 장비·소재
반도체용 industrial gas
실제 반복계약이 있는 AI infrastructure software

위험한 후보:
AI server ODM
Neocloud GPU rental
AI accelerator pure-play
CXL / 유리기판 / 뉴로모픽 theme-only
매출 없는 퓨리오사AI 관련주
회계·공시·내부통제 리스크가 있는 AI 서버주
```

---

## 2. 대상 canonical archetype

| canonical archetype                    | Loop 3 정책                                               |
| -------------------------------------- | ------------------------------------------------------- |
| `MEMORY_HBM_CAPACITY`                  | R2 최상위 Green 후보. 단, 이미 급등한 뒤에는 4B-watch                 |
| `COMMODITY_MEMORY_GENERAL_SEMI`        | Watch-to-Green. NAND/DRAM 공급부족은 좋지만 HBM보다 visibility 낮음 |
| `SEMI_EQUIPMENT_CAPEX`                 | Watch-to-Green. 고객사 AI/HBM CAPEX와 order push-out 동시 확인  |
| `SEMI_MATERIALS_PROCESS`               | Watch-to-Green. 반복납품·고객 다변화·OPM 필요                      |
| `ADVANCED_PACKAGING_COWOS_EMIB`        | Green 가능. CoWoS 병목은 강하지만 CAPA 정상화 감시                    |
| `ADVANCED_PACKAGING_PCB`               | Watch-to-Green. AI optical PCB는 일반 PCB보다 점수 강화          |
| `OPTICAL_NETWORKING_AI_DATACENTER`     | Green 가능. hyperscaler 계약·lead time·OPM 확인 필요            |
| `AI_SERVER_ODM_EMS_SUPPLY_CHAIN`       | Watch-to-Green. 매출은 크지만 저마진·재고·고객집중·회계 overlay 필수       |
| `NEOCLOUD_GPU_RENTAL`                  | High-risk Watch. 계약 visibility는 있어도 고부채·GPU 감가상각·FCF 적자 |
| `AI_DATA_CENTER_COOLING`               | Green 가능. 실제 고객·수주·매출·M&A 가격 검증 필요                      |
| `INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA` | Watch-to-Green. fab utility-like 장기계약이면 점수 강화           |
| `AI_CHIP_FABRIC_INFRA`                 | Watch. 고객검증·tape-out·양산·매출 전 Green 제한                   |
| `AI_ACCELERATOR_CHIP_PUREPLAY`         | High-risk Watch. Nvidia 경쟁·수율·R&D burn·valuation 감시     |
| `DISPLAY_OLED_SUPPLYCHAIN`             | Watch. 고객사 CAPEX·패널 가격·cycle risk                       |
| `ELECTRONIC_COMPONENTS_MLCC_SENSOR`    | Watch. 재고·고객집중·전장 수요 확인                                 |
| `REDTEAM_ACCOUNTING_TRUST_OVERLAY`     | hard gate. 감사인 사임·공시지연·내부통제 이슈 즉시 차단                    |
| `AI_CAPEX_CROWDING_OVERLAY`            | 4B overlay. 실적은 좋아도 valuation이 이미 포화된 경우                |

---

## 3. deep sub-archetype

```text
MEMORY_HBM_CAPACITY
- HBM3E
- HBM4
- HBM4E
- Nvidia supply chain
- CAPA constraint
- 장기계약
- 선수금
- price band
- AI memory rerating
- 고객사 가격저항
- CAPA 정상화

COMMODITY_MEMORY_GENERAL_SEMI
- DRAM
- NAND
- SSD
- enterprise storage
- AI server memory shortage
- HBM 전환에 따른 범용 memory squeeze
- spot/contract price
- Kioxia / Micron / Samsung / SK Hynix

SEMI_EQUIPMENT_CAPEX
- wafer fab equipment
- EUV
- HBM fab CAPEX
- advanced node CAPEX
- packaging equipment
- 고객사 CAPEX cycle
- order push-out
- export control

ADVANCED_PACKAGING_COWOS_EMIB
- CoWoS-S
- CoWoS-L
- EMIB
- 2.5D packaging
- interposer
- substrate
- HBM-GPU integration
- packaging bottleneck
- yield

ADVANCED_PACKAGING_PCB
- high-layer PCB
- AI server PCB
- optical transceiver PCB
- glass substrate
- CXL substrate
- lead time bottleneck
- 고객사 집중

OPTICAL_NETWORKING_AI_DATACENTER
- optical transceiver
- laser
- silicon photonics
- 광섬유
- 광케이블
- AI data center interconnect
- 800G / 1.6T
- lead time expansion

AI_SERVER_ODM_EMS_SUPPLY_CHAIN
- Foxconn
- Supermicro
- Quanta
- Wistron
- AI server rack
- GPU server
- ASIC server
- consignment model
- inventory
- gross margin
- accounting trust

NEOCLOUD_GPU_RENTAL
- CoreWeave
- GPU cloud
- Nvidia GPU collateral
- OpenAI/Microsoft contract
- take-or-pay
- debt financing
- GPU depreciation
- customer concentration
- refinancing risk

AI_DATA_CENTER_COOLING
- liquid cooling
- direct-to-chip cooling
- immersion cooling
- coolant monitoring
- leak detection
- thermal management
- CoolIT / Vertiv / Schneider / Ecolab류

AI_CHIP_FABRIC_INFRA
- system semiconductor
- AI accelerator
- custom ASIC
- tape-out
- foundry yield
- customer validation
- 퓨리사AI 관련주
- CXL / 뉴로모픽 / 유리기판 theme

REDTEAM_ACCOUNTING_TRUST_OVERLAY
- auditor resignation
- filing delay
- internal control weakness
- related-party transaction
- DOJ/SEC investigation
- revenue recognition risk
```

---

# 4. 성공사례

## 4-1. SK하이닉스 HBM — `MEMORY_HBM_CAPACITY`

SK하이닉스는 R2에서 여전히 가장 강한 구조적 성공사례다. Reuters는 SK하이닉스가 AI 서버용 HBM과 전통 메모리 수요에 힘입어 2025년에 274%, 2026년에 200% 이상 상승했고, 시가총액이 약 9,420억 달러까지 올라 1조 달러에 근접했다고 보도했다. 이는 단순 메모리 업황 회복이 아니라 **메모리 = AI 인프라 병목**이라는 프레임 전환이 가격경로로 확인된 사례다. ([Reuters][1])

```text
가격경로 1차 판정:
STRUCTURAL_SUCCESS_ALIGNED + SECTOR_SUCCESS_BUT_4B_WATCH

좋은 점:
- HBM 핵심 공급망
- AI 서버 메모리 병목
- 범용 DRAM/NAND까지 수급 squeeze 가능
- EPS/OP 체급 변화
- 시장 프레임 전환

주의:
- 이미 1~2년 급등
- 시총/valuation 포화 가능성
- 고객사 가격저항
- CAPA 증설
- AI CAPEX 둔화 가능성
```

**Loop 3 교정**

```text
MEMORY_HBM_CAPACITY는 R2 최상위 Green 후보 유지.
다만 Loop 3부터는 “Green 후보”와 “이미 4B인 성공사례”를 분리한다.

Stage 3:
HBM 계약·CAPA·EPS 상향이 확인된 구간.

Stage 4B:
모두가 AI memory rerating을 인정하고,
valuation band와 시총이 이미 크게 확장된 구간.
```

---

## 4-2. 삼성전자 HBM4 — `MEMORY_HBM_CAPACITY`의 catch-up candidate

삼성전자는 2026년 2월 HBM4 칩을 고객사에 출하하기 시작했다고 밝혔고, HBM4가 HBM3E 대비 22% 빠른 11.7Gbps 안정 처리속도와 최대 13Gbps 속도를 제공한다고 설명했다. 삼성은 HBM4E 샘플도 2026년 하반기 제공할 계획이다. 발표 당일 삼성전자 주가는 6.4%, SK하이닉스는 3.3% 상승했다. ([Reuters][2])

```text
가격경로 1차 판정:
HBM_CATCHUP_STAGE2_CANDIDATE

좋은 점:
- HBM4 출하 시작
- 성능 개선 수치 제시
- HBM4E 로드맵
- 메모리 대형주 내 경쟁력 회복 가능성

주의:
- unnamed customers
- Nvidia qualification 여부
- yield
- 고객사 실제 volume
- SK하이닉스와의 점유율 격차
```

**Loop 3 교정**

```text
삼성전자는 MEMORY_HBM_CAPACITY 안에서도 “catch-up candidate”로 따로 둔다.

점수 강화 조건:
- 고객사 명시
- HBM4 volume shipment
- yield 안정
- HBM 매출비중 상승
- FY1/FY2 EPS revision

감점 조건:
- 고객 qualification 지연
- foundry/logic 사업부 실행력 문제
- 노사 리스크
```

---

## 4-3. 삼성전자 노조 리스크 — HBM catch-up 위의 execution RedTeam

삼성전자는 HBM4 catch-up 후보지만, 2026년 5월 21일부터 18일 파업을 예고한 노조 리스크가 동시에 커졌다. Reuters는 삼성전자의 한국 노조가 임금·보너스 협상 결렬 후 파업 계획을 유지했고, 보도 기준 삼성전자 주가가 9.3% 하락했다고 전했다. AI boom으로 메모리 부문 보너스는 커진 반면 logic/foundry 부문과의 보상 격차가 커지며 내부 분열과 공급 차질 우려가 부각됐다. ([Reuters][3])

```text
가격경로 1차 판정:
HBM_CATCHUP_WITH_EXECUTION_REDTEAM

의미:
삼성은 HBM4 출하로 Stage 2 후보지만,
노사·생산차질·foundry 실행력 리스크를 동시에 봐야 한다.

감점 조건:
- labor_strike_flag
- production_disruption_risk
- foundry_yield_risk
- talent_retention_risk
```

**Loop 3 교정**

```text
MEMORY_HBM_CAPACITY에서 삼성형 후보는 SK하이닉스와 다르게 scoring한다.

SK하이닉스:
already structural success + 4B-watch

삼성전자:
catch-up upside + execution RedTeam
```

---

## 4-4. Kioxia NAND — `COMMODITY_MEMORY_GENERAL_SEMI`가 AI 구조후보로 승격되는 경우

Kioxia는 NAND 중심 업체라서 과거에는 범용 메모리 cycle로만 볼 수 있었지만, AI 데이터 저장 수요가 붙으면서 다른 그림이 생겼다. Reuters는 Kioxia가 2026년 4~6월 분기에 1.3조 엔, 약 82억 달러 영업이익을 예상한다고 보도했다. 이는 AI boom이 메모리 칩 수요를 끌어올린 결과다. ([Reuters][4])

FT도 Kioxia의 2026년 1~3월 순이익이 전 분기 대비 4배, 전년 동기 대비 30배 증가했고, 주가가 20배 올라 MSCI World index 최고 성과주가 됐다고 보도했다. ([Financial Times][5])

```text
가격경로 1차 판정:
COMMODITY_MEMORY_TO_AI_STORAGE_STRUCTURAL_CANDIDATE + 4B_WATCH

좋은 점:
- AI storage demand
- NAND underinvestment
- profit explosion
- 주가 20배
- memory shortage가 NAND까지 확산

주의:
- 이미 매우 큰 가격 반응
- NAND 공급 회복
- 고객 가격저항
- SSD/consumer demand destruction
- HBM보다 계약 visibility 낮음
```

**Loop 3 교정**

```text
COMMODITY_MEMORY_GENERAL_SEMI:
기본은 Watch-to-Green.
하지만 AI storage shortage + profit explosion + 공급제약이 확인되면 Stage 2~3 후보.

단, HBM보다 4B와 cycle reversal penalty를 더 크게 둔다.
```

---

## 4-5. Applied Materials — `SEMI_EQUIPMENT_CAPEX` / `ADVANCED_PACKAGING_COWOS_EMIB`

Applied Materials는 AI CAPEX가 장비·패키징 매출로 실제 연결되는 좋은 후보사례다. Reuters는 Applied가 2026년 3분기 매출을 약 89.5억 달러로 전망해 시장 예상 80.9억 달러를 웃돌았고, 2026년 반도체 장비 사업은 30% 이상, packaging revenue는 50% 이상 성장할 것으로 예상한다고 보도했다. 발표 후 주가는 시간외에서 3% 상승했다. ([Reuters][6])

```text
가격경로 1차 판정:
SEMI_EQUIPMENT_AI_CAPEX_ALIGNED_CANDIDATE

좋은 점:
- AI와 데이터센터 인프라 CAPEX 수혜
- 장비 매출 전망 상향
- packaging revenue 고성장 전망
- 주가 시간외 +3%

주의:
- 장비주는 고객사 CAPEX cycle에 종속
- order push-out
- export control
- 고객 CAPEX peak
- 장비 업종 4B 가능성
```

**Loop 3 교정**

```text
SEMI_EQUIPMENT_CAPEX:
Green 가능보다는 Watch-to-Green.
Stage 3 조건은 장비 수주가 매출·OP·EPS로 전환되고,
고객 CAPEX가 일회성이 아니라 multi-year로 확인될 때.
```

---

## 4-6. Nvidia CoWoS-L — `ADVANCED_PACKAGING_COWOS_EMIB`

Nvidia CEO Jensen Huang은 Blackwell에서 CoWoS-L을 주로 쓰고 있으며, CoWoS-S 수요가 줄어든 것이 아니라 CoWoS-L로 기술 mix가 바뀌고 있다고 설명했다. 그는 advanced packaging capacity가 2년 전보다 약 4배 커졌지만, 여전히 packaging이 병목이라고 말했다. ([Reuters][7])

```text
가격경로 1차 판정:
ADVANCED_PACKAGING_BOTTLENECK_REFERENCE

좋은 점:
- Blackwell 핵심 packaging 구조
- CoWoS-L 수요 증가
- packaging bottleneck 지속
- HBM/GPU integration 병목

주의:
- capacity가 이미 크게 증가
- CoWoS-S → CoWoS-L mix 변화 오해 가능
- CAPA 정상화 시 4B/4C
- TSMC 의존
```

**Loop 3 교정**

```text
ADVANCED_PACKAGING_COWOS_EMIB:
Bottleneck 점수는 높게 유지.
다만 bottleneck_normalization_flag를 필수로 추가.
```

---

## 4-7. Broadcom optical / PCB 병목 — `OPTICAL_NETWORKING_AI_DATACENTER`

Broadcom은 2026년 3월 AI chip 수요가 TSMC capacity뿐 아니라 laser와 optical transceiver PCB supply chain까지 압박한다고 밝혔다. 특히 optical transceiver용 PCB lead time이 약 6주에서 6개월로 늘었다고 설명했다. 이는 AI 병목이 GPU/HBM에서 광통신·PCB·laser로 확산되고 있음을 보여준다. ([Reuters][8])

```text
가격경로 1차 판정:
OPTICAL_PCB_BOTTLENECK_STAGE2_REFERENCE

좋은 점:
- optical transceiver PCB lead time 급증
- laser supply constraint
- AI data center interconnect 수요
- long-term supply agreements 증가

주의:
- 신규 진입과 CAPA 확장 가능
- 고객사 집중
- hyperscaler CAPEX 둔화
- lead time 정상화
```

**Loop 3 교정**

```text
OPTICAL_NETWORKING_AI_DATACENTER:
Green 가능 하위축으로 유지.
AI optical PCB는 일반 PCB보다 점수 강화.

단:
lead_time_normalization
customer_concentration
inventory_build
를 강한 4B/4C 감점축으로 둔다.
```

---

## 4-8. Foxconn AI 서버 ODM — `AI_SERVER_ODM_EMS_SUPPLY_CHAIN`

Foxconn은 2026년 1분기 순이익이 전년 대비 19% 증가한 499.2억 대만달러를 기록했고, AI server rack shipments가 올해 두 배 이상 늘 것으로 예상했다. 회사는 AI server 생산능력 확대를 위해 CAPEX를 전년 대비 30% 늘릴 계획이다. 다만 일부 제품은 고객이 핵심 부품을 제공하는 consignment model로 전환되고 있으며, Foxconn 주가는 올해 6% 상승에 그쳐 대만 broader market 상승률에는 못 미쳤다. ([Reuters][9])

```text
가격경로 1차 판정:
AI_SERVER_REVENUE_SUCCESS_BUT_MARGIN_VISIBILITY_WATCH

좋은 점:
- AI server rack shipment 2배 이상 전망
- 순이익 증가
- CAPEX 확대
- GPU/ASIC server 수요

주의:
- ODM/EMS 저마진 구조
- consignment model
- 고객사 집중
- 재고·working capital
- AI 서버 매출이 OPM으로 얼마나 남는지 확인 필요
```

**Loop 3 교정**

```text
AI_SERVER_ODM_EMS_SUPPLY_CHAIN:
EPS/FCF 점수는 높일 수 있지만 Bottleneck/Pricing은 HBM보다 낮다.

Stage 3 조건:
AI server revenue growth
+ AI server margin
+ inventory 안정
+ customer concentration 낮음
+ 회계 신뢰도 통과
```

---

## 4-9. Ecolab–CoolIT — `AI_DATA_CENTER_COOLING`

Ecolab은 AI 데이터센터 액체냉각 수요를 잡기 위해 CoolIT Systems를 47.5억 달러에 인수하기로 했다. CoolIT은 Nvidia와 AMD 같은 칩메이커에 액체냉각 시스템을 공급하고, 향후 12개월 매출이 약 5.5억 달러로 예상된다. Ecolab은 2028년부터 조정 EPS에 accretive할 것으로 봤지만, 발표 당시 Ecolab 주가는 premarket에서 1% 하락했다. ([Reuters][10])

```text
가격경로 1차 판정:
AI_COOLING_STRATEGIC_SUCCESS_CANDIDATE + MNA_VALUATION_WATCH

좋은 점:
- AI 데이터센터 열밀도 증가
- liquid cooling 구조 수요
- Nvidia/AMD supply exposure
- CoolIT 매출 가시성
- Ecolab의 water/chemistry/digital monitoring과 결합 가능

주의:
- 47.5억 달러 현금 인수
- EPS accretion이 2028년부터
- M&A valuation
- debt financing
- AI CAPEX 지연
```

**Loop 3 교정**

```text
AI_DATA_CENTER_COOLING:
Green 가능 유지.
다만 M&A overpay, debt, EPS accretion delay를 반드시 RedTeam에 넣는다.
```

---

## 4-10. CoreWeave — `NEOCLOUD_GPU_RENTAL`

CoreWeave는 OpenAI와 약 119억 달러, 5년 계약을 맺은 AI cloud visibility 후보지만, 동시에 R2에서 가장 위험한 구조 중 하나다. FT는 OpenAI가 CoreWeave와 5년 컴퓨팅 계약을 맺고 3.5억 달러 지분도 취득하기로 했다고 보도했다. 하지만 Microsoft가 delivery issue 때문에 계획했던 거래에서 물러났다는 보도와, Microsoft가 CoreWeave 매출의 62%를 차지했다는 점도 같이 언급된다. ([Financial Times][11])

CoreWeave IPO는 예상가 47~55달러보다 낮은 40달러에 가격이 정해졌고, 2024년 매출 19억 달러에 순손실 8.63억 달러, 부채 80억 달러, Microsoft 매출 비중 62%라는 위험요인이 확인됐다. ([Investopedia][12])

```text
가격경로 1차 판정:
CONTRACT_VISIBILITY_BUT_LEVERAGE_FCF_RISK

좋은 점:
- OpenAI 5년 대형계약
- AI compute demand 직접 노출
- Nvidia GPU 기반 cloud
- revenue growth

주의:
- IPO downsize
- 고부채
- FCF/순손실
- Microsoft 고객집중
- GPU 감가상각
- refinancing risk
- delivery risk
```

**Loop 3 교정**

```text
NEOCLOUD_GPU_RENTAL:
Visibility는 계약 때문에 높게 줄 수 있음.
하지만 Capital/FCF risk가 너무 커서 Stage 3-Green 금지.

Stage 3 조건:
FCF 전환
debt/EBITDA 안정
고객 다변화
GPU depreciation 관리
refinancing risk 낮음
```

---

# 5. 반례

## 5-1. Supermicro — `REDTEAM_ACCOUNTING_TRUST_OVERLAY`

Supermicro는 R2의 가장 중요한 hard 4C 반례다. Reuters는 Supermicro의 감사인이던 Ernst & Young이 사임하자 주가가 30% 이상 급락했고, EY가 회사의 governance와 financial reporting control에 대한 우려를 제기했다고 보도했다. 이 사안은 Hindenburg의 회계조작 주장, annual report filing delay, DOJ 조사 보도 이후 나온 것이다. ([Reuters][13])

```text
가격경로 1차 판정:
AI_SERVER_RERATING_THEN_ACCOUNTING_HARD_4C

교훈:
AI server revenue growth
≠ Stage 3 유지

hard 4C:
- auditor_resignation
- filing_delay
- internal_control_issue
- DOJ/SEC investigation
- related_party_risk
```

**Loop 3 교정**

```text
R2 전체에 accounting trust gate 적용.

발생 시:
score_after_redteam 강제 하향
stage_after_redteam 강등
Stage 3-Green 즉시 차단
```

---

## 5-2. AI 서버 ODM 저마진·consignment model

Foxconn 사례에서 보듯 AI server shipments가 두 배 늘어도, ODM/EMS는 HBM처럼 가격결정력을 가진 병목이 아니다. 일부 cloud/networking 제품은 고객이 핵심 부품을 제공하는 consignment model로 바뀌고 있어 매출총액·마진·working capital 해석이 복잡해진다. ([Reuters][9])

```text
가격경로 1차 판정:
AI_REVENUE_BUT_MARGIN_WATCH

교훈:
AI server shipment growth
≠ HBM식 Green

필수 확인:
- gross margin
- inventory
- customer concentration
- consignment model impact
- AI server revenue to OP conversion
```

---

## 5-3. Neocloud 고부채·고객집중

CoreWeave는 OpenAI 계약이라는 강한 visibility가 있지만, IPO downsize, 80억 달러 부채, 8.63억 달러 순손실, Microsoft 매출비중 62%는 `LEVERAGE_FCF_BREAKDOWN`의 전형이다. ([Investopedia][12])

```text
가격경로 1차 판정:
NEOCLOUD_LEVERAGE_FCF_4C_WATCH

교훈:
대형계약
≠ FCF 안정

감점 조건:
- debt_to_ebitda 악화
- GPU depreciation
- customer concentration
- refinancing pressure
- delivery issue
```

---

## 5-4. 삼성 execution / labor RedTeam

삼성전자는 HBM4 출하로 catch-up 후보지만, 2026년 5월 대규모 파업 리스크가 실제 주가 하락으로 이어졌다. Reuters는 협상 결렬 이후 노조가 파업 계획을 유지했고, 삼성전자 주가가 9.3% 하락했다고 보도했다. ([Reuters][3])

```text
가격경로 1차 판정:
EXECUTION_LABOR_REDTEAM

교훈:
HBM 기술 진전
≠ execution risk 면제

감점 조건:
- labor_strike_flag
- production_disruption
- talent_drain
- foundry/logic division conflict
```

---

## 5-5. CXL·유리기판·뉴로모픽·AI칩 theme-only

Theme Tag Map 기준으로 CXL, 유리기판, 뉴로모픽, 퓨리사AI 관련주는 실제 채택·매출·고객사·지분구조가 확인되기 전까지 Watch/Red다.

```text
가격경로 1차 판정:
THEME_WITHOUT_REVENUE

교훈:
기술 이름
≠ 매출
≠ EPS/FCF

Stage 2 조건:
- 고객사 검증
- tape-out
- 양산
- 매출 인식
- 계약금액
```

---

# 6. 4B-watch 사례

## 6-1. HBM 4B-watch

```text
4B 조건:
- SK하이닉스 2025년 +274%, 2026년 +200% 이상
- 시총 약 $942B
- 모두가 AI memory rerating 인정
- 고객사 가격저항 가능성
- CAPA 증설 뉴스 증가
- EPS 상향은 지속되지만 multiple 확장 여지가 줄어듦
```

SK하이닉스는 구조적으로 맞은 사례지만, 가격경로상 이미 4B 감시가 필요하다. ([Reuters][1])

---

## 6-2. 범용 메모리 / NAND 4B-watch

```text
4B 조건:
- NAND shortage와 AI storage narrative가 과밀
- Kioxia 같은 종목이 이미 20배 급등
- consumer SSD 가격저항 가능성
- NAND 공급회복 또는 CAPEX 증가 가능성
```

Kioxia는 AI storage 수혜가 강하지만, 이미 주가 20배와 기록적 이익이라는 가격반응이 확인됐으므로 성공사례와 4B를 동시에 붙여야 한다. ([Financial Times][5])

---

## 6-3. 반도체 장비 / packaging 4B-watch

```text
4B 조건:
- AI WFE와 packaging growth를 모두가 인정
- 장비업체 가이던스가 연속 상향
- 고객사 CAPEX peak 우려
- order push-out / export control을 시장이 무시
```

Applied Materials는 실적·가이던스가 좋지만, 장비업체는 항상 고객 CAPEX cycle이 thesis break가 될 수 있다. ([Reuters][6])

---

## 6-4. CoWoS / advanced packaging 4B-watch

```text
4B 조건:
- CoWoS 병목을 모두가 인정
- 장비·기판·소재주 동반 과열
- CAPA가 이미 크게 증가
- CoWoS-S → CoWoS-L 전환을 오해하거나 과대해석
```

Nvidia는 packaging bottleneck이 여전하다고 했지만, 동시에 capacity가 2년 전보다 약 4배 커졌다는 점도 언급했다. ([Reuters][7])

---

## 6-5. Optical / PCB 4B-watch

```text
4B 조건:
- optical transceiver PCB lead time 병목이 알려짐
- 관련주 valuation 급등
- 고객사 집중
- 신규 진입과 CAPA 확장으로 병목 완화 가능성
```

Broadcom은 optical transceiver PCB lead time이 6주에서 6개월로 늘었다고 했지만, 신규 진입과 capacity expansion이 해결책이 될 수 있다고도 봤다. ([Reuters][8])

---

## 6-6. Neocloud 4B/4C-watch

```text
4B 조건:
- OpenAI·Microsoft 계약 규모만 보고 valuation 상승
- FCF 적자·고부채·고객집중 무시
- GPU 감가상각과 refinancing risk가 후행 반영
```

CoreWeave는 계약 visibility는 강하지만 IPO downsize와 재무위험이 너무 커서 Stage 3-Green을 막아야 한다. ([Investopedia][12])

---

# 7. 4C-thesis-break 사례

## 7-1. 회계·감사 4C

```text
4C:
auditor_resignation
filing_delay
internal_control_weakness
DOJ_or_SEC_investigation
related_party_transaction_risk
```

Supermicro는 R2 전체에 적용할 hard 4C 기준이다. ([Reuters][13])

---

## 7-2. Neocloud refinancing pressure

```text
4C-watch:
debt_refinancing_pressure
GPU_obsolescence
customer_concentration
FCF_negative
IPO_downsize
delivery_issue
```

CoreWeave는 visibility는 좋지만, debt/FCF/customer concentration이 먼저 통과되어야 한다. ([Investopedia][12])

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

Applied Materials와 Nvidia CoWoS 사례는 성공 근거이면서 동시에 CAPEX peak와 capacity normalization을 감시해야 하는 이유다. ([Reuters][6])

---

## 7-4. Optical / PCB 병목 정상화

```text
4C-watch:
lead_time_normalization
new_capacity
hyperscaler_order_delay
inventory_build
customer_concentration
```

Broadcom은 병목을 인정하면서도 신규 진입과 capacity expansion이 eventual solution이 될 수 있다고 말했다. ([Reuters][8])

---

## 7-5. Cooling M&A overpay / debt

```text
4C-watch:
M&A_overpay
debt_financing
EPS_accretion_delay
integration_risk
AI_CAPEX_delay
```

Ecolab–CoolIT은 좋은 AI cooling 후보지만, 47.5억 달러 현금 인수와 2028년 EPS accretion이라는 긴 시간표 때문에 RedTeam이 필요하다. ([Reuters][10])

---

## 7-6. Samsung labor / execution risk

```text
4C-watch:
labor_strike
production_disruption
delivery_reliability_risk
talent_retention_issue
division_conflict
```

삼성전자의 HBM4 출하는 긍정적이지만, 대규모 파업 리스크와 주가 -9.3% 반응은 execution RedTeam으로 넣어야 한다. ([Reuters][3])

---

# 8. 점수비중 보정표 — R2 Loop 3 / v3.0

| canonical archetype                    | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | Loop 3 핵심 감점                             |
| -------------------------------------- | ------: | ---------: | ---------: | ---------: | --------: | ------: | ---: | ---------------------------------------- |
| `MEMORY_HBM_CAPACITY`                  |      24 |         22 |         20 |         13 |        10 |       0 |    5 | 4B crowding, CAPA 정상화, 고객 가격저항           |
| `COMMODITY_MEMORY_GENERAL_SEMI`        |      23 |         17 |         17 |         12 |         9 |       0 |    5 | NAND/DRAM cycle reversal, supply rebound |
| `SEMI_EQUIPMENT_CAPEX`                 |      22 |         20 |         18 |         14 |        12 |       0 |    5 | 고객 CAPEX, order delay, export control    |
| `SEMI_MATERIALS_PROCESS`               |      20 |         18 |         14 |         13 |        11 |       0 |    5 | 고객집중, 재고, 단가 압박                          |
| `ADVANCED_PACKAGING_COWOS_EMIB`        |      22 |         21 |         20 |         14 |        11 |       0 |    5 | CAPA 정상화, yield, customer CAPEX          |
| `ADVANCED_PACKAGING_PCB`               |      21 |         21 |         19 |         13 |        11 |       0 |    5 | 고객집중, inventory, lead time 정상화           |
| `OPTICAL_NETWORKING_AI_DATACENTER`     |      22 |         22 |         21 |         13 |        12 |       0 |    5 | 고객집중, CAPA 확장, valuation crowding        |
| `AI_SERVER_ODM_EMS_SUPPLY_CHAIN`       |      22 |         17 |         14 |         13 |         9 |       0 |    5 | 저마진, consignment, inventory, 회계          |
| `NEOCLOUD_GPU_RENTAL`                  |      18 |         22 |         18 |         14 |         8 |       0 |    5 | 고부채, GPU 감가상각, FCF 적자                    |
| `AI_DATA_CENTER_COOLING`               |      21 |         22 |         22 |         13 |        11 |       0 |    5 | M&A overpay, debt, EPS accretion 지연      |
| `INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA` |      19 |         23 |         13 |         13 |        12 |       3 |    5 | fab 지연, 고객집중, 에너지비                       |
| `AI_CHIP_FABRIC_INFRA`                 |      18 |         15 |         12 |         14 |        10 |       0 |    5 | 고객검증, 수율, 양산·매출 부재                       |
| `AI_ACCELERATOR_CHIP_PUREPLAY`         |      17 |         14 |         13 |         15 |         9 |       0 |    5 | Nvidia 경쟁, R&D burn, valuation 과열        |
| `DISPLAY_OLED_SUPPLYCHAIN`             |      19 |         18 |         12 |         13 |        11 |       0 |    5 | 패널 가격경쟁, CAPEX cycle                     |
| `ELECTRONIC_COMPONENTS_MLCC_SENSOR`    |      19 |         17 |         13 |         12 |        11 |       1 |    5 | 재고, 고객집중, 스마트폰 cycle                     |
| `REDTEAM_ACCOUNTING_TRUST_OVERLAY`     |    gate |       gate |       gate |       gate |      gate |    gate | gate | 감사인 사임, 공시지연, 내부통제                       |
| `AI_CAPEX_CROWDING_OVERLAY`            |    gate |       gate |       gate |       gate |      gate |    gate | gate | 실적 호조에도 valuation 포화                     |

Loop 3에서 가장 크게 바뀐 건 다섯 가지다.

```text
1. HBM은 Green 유지, 하지만 Valuation 점수는 낮춘다.
   이미 SK하이닉스가 구조적 성공 + 4B 구간에 들어갔기 때문.

2. 범용 메모리/NAND 점수는 소폭 상향.
   Kioxia처럼 AI storage shortage가 profit explosion으로 연결된 사례가 나왔기 때문.

3. Optical networking은 점수 강화.
   Broadcom의 PCB lead time 6주 → 6개월 사례가 실제 병목을 보여줬기 때문.

4. AI server ODM은 Valuation/Visibility를 낮춘다.
   Foxconn은 매출은 좋지만 ODM/EMS 저마진과 consignment 리스크가 있다.

5. Neocloud는 visibility는 높지만 Green 금지.
   CoreWeave처럼 계약은 강해도 고부채·FCF 적자·고객집중이 너무 크다.
```

---

# 9. stage date 후보

## `MEMORY_HBM_CAPACITY`

```text
Stage 1:
AI 서버 HBM 수요 급증, Nvidia 공급망, HBM 가격/계약 뉴스

Stage 2:
HBM 매출비중 상승, 고객사 qualification, 실적 서프라이즈, OP/EPS 상향 확인일

Stage 3:
장기계약·선수금·CAPA constraint·multi-year EPS revision 확인일

Stage 4B:
시총/valuation 포화, 모두가 AI memory rerating 인정, crowded trade 확인일

Stage 4C:
AI CAPEX 둔화, HBM 가격 하락, CAPA 과잉, 고객사 주문 축소
```

## `COMMODITY_MEMORY_GENERAL_SEMI`

```text
Stage 1:
AI storage demand, DRAM/NAND shortage, SSD 가격 상승 뉴스

Stage 2:
contract price 상승, 실적 서프라이즈, guidance 상향

Stage 3:
HBM이 아닌 범용 메모리도 multi-year shortage와 EPS 상향이 확인될 때

Stage 4B:
NAND/DRAM 관련주 급등과 memory shortage consensus 과밀

Stage 4C:
supply rebound, consumer demand destruction, price reversal
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

## `AI_SERVER_ODM_EMS_SUPPLY_CHAIN`

```text
Stage 1:
AI server rack 수요 증가, GPU/ASIC server demand 뉴스

Stage 2:
AI server 매출·shipment·OP 증가 확인

Stage 3:
AI server mix가 회사 전체 EPS/FCF 체급을 바꾸고 마진이 방어될 때

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
FCF 전환 또는 debt/EBITDA 안정화 확인 전까지 제한

Stage 4B:
AI cloud valuation 과열

Stage 4C:
refinancing pressure, GPU obsolescence, customer concentration, FCF negative
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

## R2 Loop 3 공통 검증 방식

```text
1. 각 case의 stage1_date, stage2_date, stage3_date를 지정한다.
2. 해당 날짜의 종가를 stage_price로 저장한다.
3. MFE_30D / 90D / 180D / 1Y / 2Y를 계산한다.
4. MAE_30D / 90D / 180D / 1Y를 계산한다.
5. peak_price와 drawdown_after_peak를 계산한다.
6. EPS revision, revenue guidance, backlog, margin, customer concentration, accounting flag와 가격경로를 비교한다.
```

## Loop 3에서 새로 강제할 판정

```text
HBM_STRUCTURAL_SUCCESS_BUT_4B:
HBM 구조는 맞지만 이미 시장이 대부분 인정한 상태.

HBM_CATCHUP_EXECUTION_CANDIDATE:
후발 HBM 업체가 출하·qualification·yield로 따라붙는 후보.

COMMODITY_MEMORY_AI_STORAGE_SUCCESS:
NAND/DRAM이 AI storage 수요로 실제 profit explosion을 만든 경우.

SEMI_CAPEX_ALIGNED:
AI CAPEX가 장비 수주·가이던스·EPS로 전환.

PACKAGING_BOTTLENECK_ALIGNED:
CoWoS/advanced packaging 병목이 실제 매출·수주로 연결.

OPTICAL_PCB_BOTTLENECK_ALIGNED:
optical transceiver, laser, PCB lead time이 수주와 OPM으로 연결.

AI_REVENUE_BUT_MARGIN_WATCH:
AI 서버 매출은 늘었지만 저마진·consignment·재고 리스크가 남은 경우.

CONTRACT_VISIBILITY_BUT_LEVERAGE_RISK:
대형 AI cloud 계약은 있으나 고부채·FCF 적자·고객집중.

ACCOUNTING_TRUST_BREAK_4C:
AI 서버 성장주라도 감사·공시·내부통제가 깨진 경우.

THEME_WITHOUT_REVENUE:
CXL·유리기판·AI칩·뉴로모픽이 매출 없이 테마만 있는 경우.
```

## 이번 R2 Loop 3에서 우선 검증할 가격 case

| case_id                                      |              stage2 후보일 | 현재 1차 가격판정                                 |
| -------------------------------------------- | ----------------------: | ------------------------------------------ |
| `sk_hynix_hbm_trillion_case`                 | 2025~2026 주요 실적·HBM 계약일 | structural aligned + 4B                    |
| `samsung_hbm4_shipping_case`                 |              2026-02-12 | +6.4%, HBM catch-up Stage 2 후보             |
| `samsung_labor_strike_execution_case`        |              2026-05-15 | -9.3%, execution RedTeam                   |
| `kioxia_ai_nand_profit_case`                 |              2026-05-15 | commodity memory → AI storage success + 4B |
| `applied_materials_ai_packaging_growth_case` |              2026-05-14 | +3% extended, semi capex aligned           |
| `nvidia_cowos_l_transition_case`             |              2025-01-16 | packaging bottleneck reference             |
| `broadcom_optical_pcb_leadtime_case`         |              2026-03-24 | optical/PCB bottleneck reference           |
| `foxconn_ai_server_rack_growth_case`         |              2026-05-14 | AI revenue success but margin watch        |
| `ecolab_coolit_liquid_cooling_case`          |              2026-03-20 | cooling success candidate + M&A watch      |
| `coreweave_openai_contract_case`             |                 2025-03 | contract visibility but leverage risk      |
| `coreweave_downsized_ipo_debt_case`          |              2025-03-28 | IPO downsize, high debt, FCF risk          |
| `supermicro_ey_resignation_case`             |              2024-10-30 | accounting hard 4C                         |
| `cxl_glass_substrate_theme_case`             |                   case별 | actual revenue before Green                |
| `furiosa_ai_related_stock_case`              |                   case별 | 지분·계약·매출 전 Watch/Red                       |

---

# 11. 다음에 에이전트가 채워야 할 price fields

R2 Loop 3에서는 아래 필드를 채우게 해야 한다.

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
hbm4_shipping_flag
hbm4_yield_signal
qualification_status
volume_shipment_flag

memory_spot_price_change
memory_contract_price_change
dram_nand_mix
nand_profit_growth
ssd_price_change
commodity_memory_supply_rebound_flag

equipment_order_growth
equipment_backlog
customer_capex_growth
order_pushout_flag
export_control_flag

packaging_revenue_growth
cowos_capacity_growth
cowos_l_flag
cowos_s_flag
yield_issue_flag
bottleneck_normalization_flag

pcb_lead_time_weeks
optical_transceiver_order
laser_supply_constraint_flag
hyperscaler_contract_flag
silicon_photonics_revenue

ai_server_revenue
ai_server_rack_shipments
ai_server_margin
consignment_model_flag
inventory_growth
customer_concentration
working_capital_pressure

gpu_cloud_revenue
gpu_cloud_contract_value
take_or_pay_flag
debt_to_ebitda
net_debt
fcf_margin
gpu_depreciation
refinancing_risk_flag
customer_concentration
delivery_issue_flag

cooling_revenue
liquid_cooling_order
mna_price
mna_multiple
mna_debt_financing_flag
eps_accretion_year
integration_risk_flag

auditor_resignation_flag
filing_delay_flag
internal_control_issue_flag
regulatory_probe_flag
related_party_risk_flag

labor_strike_flag
production_disruption_flag
execution_risk_flag
foundry_yield_risk_flag

theme_only_flag
actual_revenue_flag
customer_validation_flag
tapeout_flag
mass_production_flag

score_price_alignment
price_validation_status
review_notes
```

---

# R2 Loop 3 결론

이번 3회차에서 R2는 더 좁혀졌다.

```text
강한 Green 후보:
HBM
advanced packaging
AI optical networking
AI data center cooling
반도체용 industrial gas
일부 AI storage memory

Watch-to-Green:
반도체 장비
반도체 소재
AI server PCB
AI server ODM 중 마진·재고·회계가 통과되는 기업
범용 DRAM/NAND 중 AI storage 수요와 EPS가 실제 맞는 기업

High-risk Watch:
Neocloud GPU rental
AI accelerator pure-play
CXL
유리기판
뉴로모픽
퓨리오사AI 관련주
AI server ODM 중 저마진·고객집중 높은 기업

Hard 4C:
Supermicro식 회계·감사 리스크
CoreWeave식 고부채·FCF 적자·고객집중
삼성식 execution/labor shock
AI CAPEX cut
packaging/optical bottleneck normalization
theme-only AI chip 관련주
```

**R2 Loop 3 점수정규화의 핵심 문장:**

> AI·반도체·전자부품은 “AI 수혜”가 아니라 **HBM, 범용 메모리, 장비, 패키징, 광통신, 서버 ODM, 네오클라우드, 냉각, AI칩 pure-play가 각각 다른 경제구조를 가진다**는 걸 먼저 인정해야 한다.
> EPS/FCF와 가격경로가 같이 맞은 축만 Green 후보이고, 고부채·회계·고객집중·저마진·매출 부재·CAPA 정상화·execution shock은 즉시 RedTeam이다.

다음 순서는 **R3 — 2차전지·전기차·친환경 Loop 3**다.

[1]: https://www.reuters.com/world/asia-pacific/ai-boom-puts-sk-hynix-cusp-1-trillion-market-value-2026-05-14/?utm_source=chatgpt.com "AI boom puts SK Hynix on cusp of $1 trillion market value"
[2]: https://www.reuters.com/technology/samsung-electronics-says-it-has-shipped-hbm4-chips-customers-2026-02-12/?utm_source=chatgpt.com "Samsung ships latest HBM4 chips to catch-up in AI race"
[3]: https://www.reuters.com/business/world-at-work/samsung-elecs-union-says-samsung-proposed-unconditional-talks-strike-plan-holds-2026-05-15/?utm_source=chatgpt.com "Samsung's South Korean union sticks to strike plan after talks offer; shares slide"
[4]: https://www.reuters.com/world/asia-pacific/memory-maker-kioxia-sees-82-billion-q1-profit-ai-boom-2026-05-15/?utm_source=chatgpt.com "Memory maker Kioxia sees $8.2 billion Q1 profit on AI boom"
[5]: https://www.ft.com/content/1e2641ba-14ba-403d-86eb-e484df00964b?utm_source=chatgpt.com "Japanese flash memory maker's profits surge on AI frenzy"
[6]: https://www.reuters.com/business/applied-materials-sees-quarterly-revenue-above-estimates-2026-05-14/?utm_source=chatgpt.com "Applied Materials sees quarterly revenue above estimates on sustained AI spending"
[7]: https://www.reuters.com/technology/nvidia-ceo-says-its-advanced-packaging-technology-needs-are-changing-2025-01-16/?utm_source=chatgpt.com "Nvidia CEO says its advanced packaging technology needs are changing"
[8]: https://www.reuters.com/world/asia-pacific/broadcom-flags-supply-constraints-says-tsmc-capacity-bottleneck-2026-03-24/?utm_source=chatgpt.com "Broadcom flags supply constraints, says TSMC capacity a bottleneck"
[9]: https://www.reuters.com/world/china/taiwans-foxconn-reports-185-rise-q1-profit-beats-forecast-2026-05-14/?utm_source=chatgpt.com "Foxconn reports forecast-beating 19% jump in Q1 profit on AI demand"
[10]: https://www.reuters.com/business/ecolab-acquire-coolit-systems-475-billion-2026-03-20/?utm_source=chatgpt.com "Ecolab to buy CoolIT for $4.75 billion to tap into AI data center boom"
[11]: https://www.ft.com/content/4b52fdbb-ca8e-4208-bb99-f1e7f9313863?utm_source=chatgpt.com "OpenAI forges $12bn contract with CoreWeave"
[12]: https://www.investopedia.com/nvidia-backed-coreweave-prices-its-ipo-at-usd40-per-share-below-expectations-11701963?utm_source=chatgpt.com "Nvidia-Backed CoreWeave Prices Its IPO at $40 Per Share, Below Expectations"
[13]: https://www.reuters.com/technology/super-micro-computer-says-ernst-young-resigns-its-accountant-shares-tank-2024-10-30/?utm_source=chatgpt.com "Super Micro Computer says Ernst & Young resigns as auditor, shares tank"

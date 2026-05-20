좋아. **R1 Loop 7까지 끝났으니, 이번은 R2 Loop 7 — AI·반도체·전자부품**이다.

이번 라운드부터는 네가 바꾼 기준대로, 단순히 archetype을 채우는 게 아니라 **“점수표가 실제 stage를 잘 포착했는지 → 그 stage가 실제 주가 상승·하락과 맞았는지 → 그래서 점수비중을 어떻게 정규화할지”**를 6번에서 크게 다룬다.

서생원 원칙은 그대로 깐다. R2에서도 핵심은 “AI 수혜”가 아니라 **EPS/FCF 체급 변화 + 시장의 과거 프레임 오해 + 밸류에이션 리레이팅 + 실제 가격경로 검증**이다. 즉 “AI칩”, “HBM”, “CXL”, “유리기판”, “AI 서버”라는 이름이 아니라, 실제로 이익 체급이 바뀌고 시장이 뒤늦게 프레임을 바꾸는지를 봐야 한다.

Theme Tag Map 기준으로 R2는 HBM, CXL, 시스템반도체, 뉴로모픽, 전공정·후공정 장비, 소재, PCB, 유리기판, MLCC, OLED, 클린룸, 스마트폰 부품, 카메라, 무선충전을 흡수한다. 여기서 **HBM은 Green 가능성이 높지만, CXL·뉴로모픽·유리기판·AI칩 관련주는 실제 채택·매출화 전까지 Watch/Red**로 둬야 한다는 원칙이 이미 잡혀 있다.

OpenDART·공시 기반으로는 list만 보고 “AI 수주 있음” 처리하면 안 된다. 공급계약, 신규시설투자, 전환사채, 유상증자, 잠정실적, 감사의견 같은 watch disclosure는 detail에서 계약금액, 계약기간, 고객, 매출 대비 계약금액, OP YoY, 희석률 등을 실제 확인해야 하고, 없는 값은 만들면 안 된다.

---

# R2 Loop 7. AI·반도체·전자부품

## 1. 이번 라운드 대섹터

```text
R2 = AI·반도체·전자부품
Loop 7 목표 =
HBM 구조적 성공 / HBM catch-up / NAND AI storage /
custom AI ASIC / advanced packaging / optical PCB /
AI networking / photonics / semiconductor equipment /
AI server ODM / neocloud / AI accelerator IPO를

stage 포착 + 가격경로 정합성 + 점수비중 재조정으로 다시 정규화
```

이번 R2 Loop 7의 핵심 질문은 이거다.

```text
이 회사는 AI 수혜주인가?
아니면 AI 인프라 병목을 실제 EPS/FCF 체급 변화로 바꿨는가?
```

R2에서 stage는 이렇게 고정한다.

```text
Stage 1:
AI 수요, HBM 부족, custom ASIC 기대, AI 서버·패키징·광통신 narrative

Stage 2:
실제 매출 가이던스, 계약, 고객명, 출하, capacity, backlog, guidance 상향 확인

Stage 3:
OP/EPS/FCF 상향 + margin 개선 + 실제 가격경로 동행

Stage 4B:
모두가 AI 반도체 리레이팅을 인정하고 valuation이 이미 크게 확장된 구간

Stage 4C:
회계·감사 문제, 고객집중, 고부채, FCF 적자, IPO 과열, CAPA 정상화, 가격경쟁
```

R2는 이번 Loop 7에서 확실히 둘로 갈린다.

```text
진짜 stage 포착이 맞았던 축:
HBM
AI storage NAND
반도체 장비
custom AI ASIC
AI networking
photonics / optical PCB

가격은 올랐지만 RedTeam이 강한 축:
AI server ODM
neocloud GPU rental
AI accelerator pure-play IPO
HBM catch-up execution
AI data-center cooling M&A
```

---

## 2. 대상 canonical archetype

| canonical archetype                   | Loop 7 판정 방향               | stage 포착 핵심                                           |
| ------------------------------------- | -------------------------- | ----------------------------------------------------- |
| `MEMORY_HBM_CAPACITY`                 | R2 최상위 Green 후보, 단 4B 감시   | HBM 매출, 점유율, OP/EPS, 가격경로                             |
| `MEMORY_HBM_LTA_PREPAYMENT`           | Watch-to-Green             | 장기계약, 가격밴드, 선수금, capacity reservation                 |
| `HBM_CATCHUP_EXECUTION`               | Watch-to-Green             | 출하, 고객 qualification, yield, volume shipment          |
| `HBM_CATCHUP_EXECUTION_RISK`          | RedTeam overlay            | 파업, 생산차질, foundry/logic execution                     |
| `MEMORY_SUPPLY_REALLOCATION`          | Watch-to-Green             | consumer exit, AI/HBM strategic allocation            |
| `AI_STORAGE_NAND_SHORTAGE`            | Green 후보지만 4B 강함           | NAND profit, enterprise SSD, AI storage, 주가           |
| `SEMI_EQUIPMENT_AI_CAPEX`             | Watch-to-Green             | AI/HBM CAPEX, 장비 매출 가이던스, packaging revenue           |
| `CUSTOM_AI_ASIC_HYPERSCALER`          | Green 후보                   | 고객명, AI chip revenue, TSMC capacity, delivery         |
| `CUSTOM_AI_ASIC_MARGIN_CONCENTRATION` | RedTeam overlay            | 고객집중, 낮은 custom margin, startup customer              |
| `ADVANCED_PACKAGING_COWOS_EMIB`       | Green 후보                   | CoWoS/EMIB, HBM integration, packaging revenue        |
| `ADVANCED_PACKAGING_PCB`              | Watch-to-Green             | optical transceiver PCB, lead time, LTA               |
| `OPTICAL_NETWORKING_AI_DATACENTER`    | Green 후보                   | optical PCB, laser, transceiver, long-term supply     |
| `PHOTONICS_AI_DATACENTER_CHIPS`       | Watch-to-Green             | 계약금액, 납품연도, AI DC light-based chips                   |
| `AI_NETWORKING_SWITCHING_INFRA`       | Watch-to-Green             | AI infra orders, hyperscaler orders, switching orders |
| `AI_SERVER_ODM_EMS_SUPPLY_CHAIN`      | Watch-to-Green, margin cap | AI server shipments, consignment, gross margin        |
| `NEOCLOUD_GPU_RENTAL`                 | High-risk Watch            | 대형계약, 고부채, GPU 감가상각, FCF                              |
| `CIRCULAR_AI_FINANCING_OVERLAY`       | hard review                | 공급자·투자자·고객 순환구조                                       |
| `AI_DATA_CENTER_COOLING`              | Watch-to-Green             | liquid cooling revenue, M&A multiple, EPS accretion   |
| `AI_ACCELERATOR_CHIP_PUREPLAY`        | High-risk Watch            | IPO, 고객집중, Nvidia 경쟁, gross margin                    |
| `REDTEAM_ACCOUNTING_TRUST_OVERLAY`    | hard gate                  | 감사인 사임, 공시지연, 내부통제                                    |
| `DISCLOSURE_CONFIDENCE_CAP`           | 공통 cap                     | 계약금액·고객명·기간·마진 미공개                                    |

---

## 3. deep sub-archetype

```text
MEMORY_HBM_CAPACITY
- HBM3E
- HBM4
- HBM4E
- Nvidia supply chain
- AMD AI accelerator
- CAPA constraint
- HBM market share
- treasury share cancellation
- OP/EPS explosion
- 4B valuation crowding

MEMORY_HBM_LTA_PREPAYMENT
- 3~5년 장기계약
- price band
- prepayment
- RPO
- capacity reservation
- supply security
- customer commitment

HBM_CATCHUP_EXECUTION
- Samsung HBM4
- Micron HBM4
- customer shipments
- qualification
- yield
- volume production
- AMD MOU
- Nvidia qualification
- foundry partnership
- labor strike

AI_STORAGE_NAND_SHORTAGE
- NAND
- enterprise SSD
- AI storage
- inference storage
- underinvestment
- Kioxia
- SanDisk
- SSD ASP
- supply rebound
- 4B after 20x rally

SEMI_EQUIPMENT_AI_CAPEX
- Applied Materials
- Lam Research
- KLA
- WFE
- HBM fab CAPEX
- DRAM equipment
- advanced packaging equipment
- 3D chiplet stacking
- customer visibility
- order pushout

CUSTOM_AI_ASIC_HYPERSCALER
- Broadcom
- Google TPU
- OpenAI custom chip
- Anthropic TPU
- Meta MTIA
- Amazon custom silicon
- TSMC capacity
- AI networking
- custom margin
- customer concentration

OPTICAL_NETWORKING_AI_DATACENTER
- optical transceiver
- laser
- silicon photonics
- optical PCB
- 800G / 1.6T
- co-packaged optics
- lead time 6 weeks → 6 months
- LTA 3~4년

AI_NETWORKING_SWITCHING_INFRA
- Cisco
- Ethernet AI fabric
- hyperscaler orders
- silicon
- optics
- security
- data-center switching
- restructuring cost

AI_SERVER_ODM_EMS_SUPPLY_CHAIN
- Foxconn
- Quanta
- Wistron
- Supermicro
- GPU server
- ASIC server
- rack shipment
- consignment model
- inventory
- working capital
- accounting trust

NEOCLOUD_GPU_RENTAL
- CoreWeave
- GPU cloud
- OpenAI contract
- Meta contract
- Nvidia investment
- unused capacity guarantee
- GPU collateral debt
- FCF negative
- refinancing risk

AI_ACCELERATOR_CHIP_PUREPLAY
- Cerebras
- wafer-scale engine
- OpenAI customer
- AWS customer
- IPO first-day return
- revenue concentration
- gross margin
- Nvidia competition
- valuation overheat
```

---

## 4. 성공사례

### 4-1. SK하이닉스 HBM — 점수표가 stage와 가격경로를 가장 잘 잡은 구조적 성공

SK하이닉스는 R2 Loop 7에서 가장 명확한 `MEMORY_HBM_CAPACITY` 성공사례다. 2025년 4분기 영업이익은 19.2조 원으로 전년 대비 137% 증가했고, 시장 예상 17.7조 원을 크게 웃돌았다. Reuters는 SK하이닉스가 HBM 시장에서 61% 점유율을 가진 것으로 보도했고, 실적 발표와 함께 12.2조 원 규모 treasury share cancellation을 발표하면서 주가가 after-hours에서 9% 상승했다고 전했다. ([Reuters][1])

이후 2026년 5월에는 SK하이닉스 주가가 2025년 274% 상승 후 2026년에도 200% 이상 상승했고, 시가총액이 약 9,420억 달러까지 올라 1조 달러에 근접했다고 Reuters가 보도했다. 이건 “메모리 = 과거 시클리컬” 프레임이 “메모리 = AI 인프라 병목” 프레임으로 바뀐 실제 가격경로다. ([Reuters][2])

```text
case_type:
MEMORY_HBM_CAPACITY
+
STRUCTURAL_SUCCESS_ALIGNED
+
STRUCTURAL_SUCCESS_BUT_4B_WATCH

stage 포착:
Stage 1 = AI 서버 HBM 수요, 메모리 shortage
Stage 2 = HBM 매출·점유율·OP surprise 확인
Stage 3 = OP/EPS 체급 변화 + treasury cancellation + 주가 +9%
Stage 4B = 2025년 +274%, 2026년 +200% 이상, 시총 $942B

가격경로 판정:
점수표가 매우 잘 맞았다.
HBM 병목, EPS 폭발, 자본환원, 가격경로가 모두 동행했다.

정규화:
MEMORY_HBM_CAPACITY의 EPS/FCF, Visibility, Bottleneck 가중치 유지·상향.
다만 Valuation/Mispricing은 Stage 4B 이후 감점.
```

**R2 정규화 결론**

```text
HBM은 R2 최상위 Green 후보군 유지.
하지만 SK하이닉스식 성공사례는 이미 4B 감시 구간이다.

즉:
“좋은 구조”와 “아직 싼 구조”를 분리해야 한다.
```

---

### 4-2. 삼성전자 HBM4 catch-up — Stage 2는 맞지만, Stage 3는 execution gate 필요

삼성전자는 2026년 2월 HBM4 출하를 시작했고, HBM4가 HBM3E 대비 22% 빠른 11.7Gbps 안정 처리속도와 최대 13Gbps 속도를 제공한다고 밝혔다. Reuters는 발표 당일 삼성전자 주가가 6.4%, SK하이닉스가 3.3% 상승했다고 보도했다. ([Reuters][3])

이어 삼성전자는 AMD와 AI 메모리 MOU를 맺어 AMD의 차세대 Instinct MI455X용 HBM4와 EPYC용 DDR5 공급, 그리고 foundry partnership 가능성을 논의했다. 하지만 이 MOU는 구속력 있는 매출계약이 아니라 Stage 1~2 근거이고, Counterpoint 기준 삼성의 HBM 점유율은 22%로 SK하이닉스 57%보다 낮았다. ([Reuters][4])

동시에 2026년 5월에는 45,000명 이상 근로자의 파업 가능성과 memory 부문·logic/foundry 부문 보너스 격차 문제가 부각됐다. Reuters는 이 갈등이 생산차질, 인재유출, 공급망 신뢰에 부담이 될 수 있다고 보도했다. ([Reuters][5])

```text
case_type:
HBM_CATCHUP_EXECUTION_STAGE2
+
HBM_CATCHUP_EXECUTION_RISK

stage 포착:
Stage 1 = HBM4 기술 발표·출하
Stage 2 = 고객 출하 + AMD MOU + 주가 +6.4%
Stage 3 = 아직 고객 qualification, volume shipment, yield, margin, EPS 전환 필요
Stage 4C-watch = 파업·생산차질·foundry/logic execution risk

가격경로 판정:
Stage 2 포착은 가격과 맞았다.
하지만 Stage 3로 바로 올리면 안 된다.
```

**R2 정규화 결론**

```text
HBM_CATCHUP_EXECUTION은 Visibility를 올리되,
EPS/FCF 점수는 낮게 시작한다.

qualification_status
yield_signal
volume_shipment
customer_name
labor_strike_flag

이 확인되기 전까지 Stage 3-Green 제한.
```

---

### 4-3. Kioxia / AI storage NAND — 점수표가 맞았지만 이미 4B가 강한 사례

Kioxia는 NAND가 AI storage 병목으로 재평가될 수 있음을 보여준다. Reuters는 Kioxia가 2026년 4~6월 분기 영업이익을 1.3조 엔, 약 82억 달러로 예상했다고 보도했다. ([Reuters][6])

FT는 Kioxia의 이익 급증이 generative AI 수요와 memory shortage에 의해 발생했고, Kioxia 주가가 20배 상승했으며, 시장가치가 24.3조 엔에 도달했다고 보도했다. 즉 점수표가 `AI_STORAGE_NAND_SHORTAGE`를 잡은 건 맞지만, 가격경로상 이미 4B 감시가 매우 강하다. ([Financial Times][7])

```text
case_type:
AI_STORAGE_NAND_SHORTAGE_SUCCESS
+
STRUCTURAL_SUCCESS_BUT_4B_WATCH

stage 포착:
Stage 1 = AI storage / NAND underinvestment
Stage 2 = profit guidance explosion
Stage 3 = AI storage shortage가 profit으로 확인
Stage 4B = 주가 20배 상승

가격경로 판정:
점수표가 구조를 잘 잡았다.
하지만 기대수익률 관점에서는 이미 4B risk가 큼.
```

**R2 정규화 결론**

```text
AI_STORAGE_NAND_SHORTAGE 점수는 EPS/FCF를 높게 준다.
하지만 10배~20배 가격경로가 확인되면 Valuation/Mispricing 점수는 강하게 낮춘다.

NAND는 HBM보다 cycle reversal risk가 더 크므로
supply_rebound_flag와 consumer_demand_destruction_flag를 필수로 둔다.
```

---

### 4-4. Applied Materials — 장비주 Stage 2→3 포착이 가격과 맞은 사례

Applied Materials는 `SEMI_EQUIPMENT_AI_CAPEX`의 좋은 stage 검증 사례다. 2026년 2월에는 AI processor와 memory shortage 수요를 근거로 2분기 매출·이익 가이던스를 시장 예상보다 높게 제시했고, 주가는 extended trading에서 12% 넘게 상승했다. 특히 HBM, leading-edge logic, advanced packaging, 3D chiplet stacking이 핵심 성장축으로 언급됐다. ([Reuters][8])

2026년 5월에도 Applied Materials는 Q2 매출·이익 beat 후 Q3 매출 89.5억 달러, adjusted EPS 3.36달러를 제시해 시장 예상보다 높았고, 반도체 장비 사업 30% 이상 성장과 packaging revenue 50% 이상 성장을 예상했다. 발표 후 주가는 extended trading에서 3% 상승했다. ([Reuters][9])

```text
case_type:
SEMI_EQUIPMENT_AI_CAPEX_ALIGNED

stage 포착:
Stage 1 = AI/HBM/advanced packaging CAPEX 수요
Stage 2 = revenue/EPS guidance 상향
Stage 3 후보 = equipment growth + packaging revenue growth + 가격반응
Stage 4B-watch = 장비주 CAPEX cycle 과열 가능성

가격경로 판정:
2월 +12%, 5월 +3% 반응으로 stage 포착이 가격경로와 잘 맞았다.
```

**R2 정규화 결론**

```text
SEMI_EQUIPMENT_AI_CAPEX는 Watch-to-Green 유지.
이번 Loop 7에서 EPS/FCF와 Visibility 점수 상향.

하지만 장비주는 고객사 CAPEX cycle에 묶인다.
order_pushout_flag, export_control_flag, capex_peak_flag는 계속 hard overlay.
```

---

### 4-5. Broadcom custom AI ASIC — hyperscaler custom silicon이 독립 archetype으로 승격

Broadcom은 R2 Loop 7에서 `CUSTOM_AI_ASIC_HYPERSCALER`를 강하게 만든 사례다. Reuters는 Broadcom이 2027년 AI chip revenue가 1,000억 달러를 넘을 수 있다고 전망했고, 2026년 2분기 AI chip revenue를 107억 달러로 제시했으며, 발표 후 주가가 extended trading에서 거의 5% 상승했다고 보도했다. Broadcom은 Google TPU, OpenAI custom chip, Anthropic, Meta MTIA 등 hyperscaler custom chip 수요에 노출돼 있다. ([Reuters][10])

동시에 Broadcom은 TSMC capacity가 2026년 supply-chain bottleneck이 되고 있고, laser와 optical transceiver용 PCB에서도 공급제약이 있으며, optical transceiver PCB lead time이 6주에서 6개월로 늘었다고 밝혔다. 즉 custom ASIC은 chip revenue만이 아니라 TSMC capacity, optical PCB, laser, advanced networking까지 같이 보는 archetype이다. ([Reuters][11])

```text
case_type:
CUSTOM_AI_ASIC_HYPERSCALER_STAGE2_3_CANDIDATE
+
OPTICAL_NETWORKING_AI_DATACENTER_BOTTLENECK

stage 포착:
Stage 1 = hyperscaler custom silicon narrative
Stage 2 = AI chip revenue guide, 고객명, 2027 visibility, TSMC bottleneck
Stage 3 후보 = AI revenue growth + stock +5% + buyback
Stage 4B-watch = custom ASIC narrative가 과밀해질 가능성

가격경로 판정:
stage 포착이 실제 가격 상승과 맞았다.
Broadcom은 custom ASIC archetype 가중치를 올리는 근거다.
```

**R2 정규화 결론**

```text
CUSTOM_AI_ASIC_HYPERSCALER는 R2 핵심 archetype으로 승격.

상향:
Visibility
Bottleneck
EPS/FCF

감점:
customer_concentration
custom_chip_margin
TSMC_capacity_miss
startup_customer_credit_risk
```

---

### 4-6. Cisco / Tower / Foxconn — AI networking·photonics·server ODM을 다르게 점수화해야 한다

Cisco는 AI networking/switching이 실제 order와 가격경로로 연결되는 사례다. Reuters는 Cisco의 hyperscaler AI infrastructure orders가 fiscal year-to-date 53억 달러, full-year expectation이 90억 달러로 올라갔고, data-center switching orders가 전년 대비 40% 이상 증가했으며, 발표 후 주가가 extended trading에서 16% 넘게 상승했다고 보도했다. 다만 약 4,000명 감원과 10억 달러 restructuring cost도 함께 있었다. ([Reuters][12])

Tower Semiconductor는 AI data-center photonics chip의 Stage 2 사례다. Reuters는 Tower가 2027년 공급 예정인 light-based AI data-center chip deals 13억 달러를 확보했고, 발표 후 미국 상장주가 early trading에서 17% 넘게 상승했다고 보도했다. ([Reuters][13])

Foxconn은 AI server ODM이 실제 수요를 받는 사례지만, HBM·custom ASIC 같은 병목기업과 점수 구조가 다르다. Reuters는 Foxconn의 2026년 1분기 순이익이 전년 대비 19% 증가했고, AI server rack shipments가 올해 두 배 이상 늘 것으로 예상되며, 일부 cloud/networking 제품이 고객이 핵심 부품을 제공하는 consignment model로 이동했다고 보도했다. ([Reuters][14])

```text
case_type:
Cisco = AI_NETWORKING_SWITCHING_INFRA_STAGE2_3
Tower = PHOTONICS_AI_DATACENTER_CHIPS_STAGE2
Foxconn = AI_SERVER_ODM_REVENUE_SUCCESS_BUT_MARGIN_WATCH

가격경로 판정:
Cisco +16%, Tower +17%는 stage 포착이 가격경로와 잘 맞음.
Foxconn은 profit growth evidence는 좋지만 ODM margin cap이 필요.
```

**R2 정규화 결론**

```text
AI networking과 photonics는 Bottleneck/Visibility 점수 상향.
AI server ODM은 Revenue/EPS는 올리되 Bottleneck/Pricing 점수는 낮게 유지.

Foxconn형은:
AI server revenue growth
≠ HBM식 가격결정력
```

---

## 5. 반례

### 5-1. Supermicro — AI 서버 성장도 회계 신뢰도가 깨지면 hard 4C

Supermicro는 R2 전체의 hard counterexample이다. Reuters는 Ernst & Young이 Supermicro 감사인에서 사임하자 주가가 30% 이상 급락했다고 보도했다. EY는 governance와 internal control over financial reporting에 대한 우려를 제기했고, 이 사안은 annual report filing delay, Hindenburg의 회계조작 주장, DOJ 조사 보도 이후 나왔다. ([Reuters][15])

```text
case_type:
AI_SERVER_RERATING_THEN_ACCOUNTING_HARD_4C

stage 포착:
Stage 1~2 = AI server revenue growth
Stage 3 후보처럼 보였음
Stage 4C = auditor resignation, filing delay, governance/internal control concern

가격경로 판정:
회계 RedTeam이 실제 -30% 이상 주가 하락과 강하게 맞았다.
```

**정규화 결론**

```text
REDTEAM_ACCOUNTING_TRUST_OVERLAY는 R2 hard gate.

AI server ODM/EMS는:
revenue growth가 좋아도
auditor_resignation_flag
filing_delay_flag
internal_control_issue_flag
가 나오면 Stage 3-Green 즉시 차단.
```

---

### 5-2. CoreWeave — 계약 visibility가 있어도 circular financing·leverage가 있으면 Green 금지

CoreWeave류 neocloud는 대형계약이 visibility를 높이지만, R2에서는 `NEOCLOUD_GPU_RENTAL`을 high-risk Watch로 둬야 한다. Reuters는 Nvidia CEO Jensen Huang 부부 재단이 CoreWeave에서 1.083억 달러 규모 AI computing resources를 구매해 연구기관에 기부했고, 기사에서 Nvidia의 CoreWeave 20억 달러 투자, 63억 달러 unused cloud capacity 구매 구조가 investor concern, 즉 circular financing 우려를 낳고 있다고 설명했다. ([Reuters][16])

```text
case_type:
CONTRACT_VISIBILITY_BUT_CIRCULAR_FINANCING_WATCH

stage 포착:
Stage 1 = GPU cloud / AI compute shortage
Stage 2 = 대형 AI customer contract, Nvidia-linked capacity
Stage 3 제한 = FCF, debt, utilization, customer diversification 필요
Stage 4C-watch = circular financing, GPU collateral debt, customer concentration

가격경로 판정:
계약 visibility만으로 stage를 올리면 false-positive 위험이 큼.
```

**정규화 결론**

```text
NEOCLOUD_GPU_RENTAL은 Visibility는 높게 줄 수 있다.
하지만 Capital/FCF 점수는 매우 낮게 시작한다.

Stage 3 조건:
FCF 전환
debt/EBITDA 안정
customer concentration 완화
GPU depreciation 관리
supplier-investor-customer loop 해소
```

---

### 5-3. Cerebras — AI accelerator pure-play IPO는 가격은 강하지만 4B/valuation RedTeam이 크다

Cerebras는 AI accelerator pure-play가 강한 가격 이벤트를 만들 수 있지만, R2에서는 high-risk Watch로 둬야 한다. IBD는 Cerebras IPO가 주당 185달러에 pricing된 뒤 첫 거래일 350달러에 개장하고 385달러까지 올랐다가 311.07달러에 마감했으며, 다음 날에는 10.1% 하락했다고 보도했다. ([Investors][17])

MarketWatch는 Cerebras가 2025년 forecast revenue 5.1억 달러 대비 131.3배 수준의 매출 배수로 거래됐다고 지적하며, OpenAI partnership이 credibility를 주지만 여전히 상업화 초기와 valuation risk가 크다고 평가했다. ([마켓워치][18])

```text
case_type:
AI_ACCELERATOR_CHIP_PUREPLAY_EVENT_PREMIUM
+
IPO_4B_VALUATION_WATCH

stage 포착:
Stage 1 = AI accelerator pure-play IPO
Stage 2 = OpenAI/AWS customer narrative, revenue, IPO demand
Stage 3 제한 = repeat orders, margin, customer diversification, ecosystem 필요
Stage 4B = 첫날 급등, valuation 과열, 다음 날 급락

가격경로 판정:
가격 상승은 있었지만 구조적 Green이라기보다 IPO event premium + 4B.
```

**정규화 결론**

```text
AI_ACCELERATOR_CHIP_PUREPLAY는 EPS/FCF 점수 낮게 시작.
Valuation penalty 강하게 둔다.

필수:
customer_count
gross_margin
repeat_order_flag
software_ecosystem_score
cash_burn
Nvidia_competition_flag
```

---

### 5-4. Ecolab–CoolIT — AI cooling은 좋지만 M&A overpay와 EPS accretion delay를 봐야 한다

Ecolab은 CoolIT Systems를 47.5억 달러에 현금 인수하기로 했다. CoolIT은 Nvidia와 AMD 같은 칩메이커에 liquid cooling systems를 공급하고, 향후 12개월 매출은 약 5.5억 달러로 예상됐다. 하지만 거래는 2028년부터 EPS accretive할 것으로 예상되고, deal value와 부채조달, integration risk를 검증해야 한다. ([Reuters][19])

Barron’s는 같은 거래에서 Ecolab 주가가 1.5% 하락했고, 거래가 CoolIT의 next-year EBITDA 약 29배에 해당한다고 보도했다. ([Barron's][20])

```text
case_type:
AI_DATA_CENTER_COOLING_MNA_STAGE2
+
MNA_VALUATION_WATCH

stage 포착:
Stage 1 = AI data-center liquid cooling 수요
Stage 2 = CoolIT 매출·고객·M&A 계약
Stage 3 제한 = EPS accretion 2028년, debt, integration, margin 확인 필요

가격경로 판정:
AI cooling narrative는 좋지만, 발표 후 주가 하락은 M&A valuation risk가 실제로 작동한 사례.
```

**정규화 결론**

```text
AI_DATA_CENTER_COOLING은 R2/R10 cross-archetype으로 유지.
하지만 M&A multiple과 EPS accretion delay가 있으면 Capital/Valuation 점수를 깎는다.
```

---

## 6. 지금 점수표로 실제 stage를 어떻게 포착했고, 주가 상승·하락과 맞았는지에 따른 점수비중정규화

이번 R2 Loop 7부터 기본 점수표는 아래처럼 정규화한다.

```text
R2 v7 기본 점수표 = 100점

1. EPS/FCF revision 가능성             25점
2. 계약·고객·출하·매출 visibility       22점
3. 병목·가격결정력                      19점
4. 시장 오해·리레이팅 gap               12점
5. valuation room / 4B 여지              8점
6. capital discipline / FCF 안정성        6점
7. 정보 신뢰도 / disclosure detail        8점

Hard RedTeam:
회계·감사·공시지연·내부통제·circular financing·고부채·고객집중·IPO 과열·상업화 초기·M&A overpay
```

### 6-1. stage별 점수 cap

```text
Stage 1 cap:
최대 45점

조건:
- AI, HBM, custom ASIC, CXL, 유리기판, 뉴로모픽, AI 서버 narrative만 있음
- 고객·계약·출하·매출·가이던스 없음

예:
CXL 테마
뉴로모픽 테마
AI칩 관련주 이름만 있는 경우
유리기판 상용화 전 뉴스
```

```text
Stage 2 cap:
최대 70점

조건:
- 고객명, 출하, 계약, 매출 가이던스, 장비 수주, AI orders 확인
- 하지만 EPS/FCF 지속성과 margin은 아직 불충분

예:
Samsung HBM4 shipment
Samsung-AMD HBM4 MOU
Tower $1.3B photonics deals
Cisco AI infrastructure orders
Applied Materials guidance
```

```text
Stage 3:
70점 이상 가능

조건:
- OP/EPS/FCF 상향이 확인
- margin 또는 capital return 확인
- 실제 주가경로가 stage와 동행

예:
SK하이닉스 HBM record profit + treasury cancellation + 주가 +9%
Applied Materials AI/HBM equipment guide + 주가 +12%
Broadcom AI revenue guide + 주가 +5%
Cisco AI orders + 주가 +16%
```

```text
Stage 4B:
점수는 높지만 기대수익률 감점

조건:
- 이미 1년 이상 대폭 상승
- 모두가 AI 반도체 리레이팅을 인정
- valuation이 EPS보다 먼저 확장
- 신규 투자자는 drawdown 위험이 커짐

예:
SK하이닉스 +274% 후 +200% 이상
Kioxia 20배 상승
Cerebras IPO 첫날 급등
```

```text
Stage 4C:
hard RedTeam

조건:
- 감사인 사임
- 공시 지연
- FCF 적자 + 고부채
- 고객·투자자·공급자 순환금융
- IPO valuation 과열 후 급락
- 파업·생산차질
- CAPA 정상화 또는 order pushout
```

---

### 6-2. 실제 가격경로와 맞은 case / 안 맞은 case

| case                 |                점수표가 잡은 stage |                               실제 가격경로 확인 | 판정                    | 정규화 조정                                     |
| -------------------- | ---------------------------: | ---------------------------------------: | --------------------- | ------------------------------------------ |
| SK하이닉스 HBM           |                   Stage 3→4B | Q4 발표 후 +9%, 2025년 +274%, 2026년 +200% 이상 | 매우 잘 맞음               | HBM EPS/FCF·Bottleneck 상향, Valuation 감점    |
| Samsung HBM4         |                      Stage 2 |                       HBM4 출하 후 삼성 +6.4% | Stage 2 포착 맞음         | Catch-up visibility 상향, execution risk cap |
| Applied Materials    |                    Stage 2→3 |                          2월 +12%, 5월 +3% | 잘 맞음                  | 장비 EPS/Visibility 상향                       |
| Broadcom custom ASIC |                    Stage 2→3 |                   AI revenue guide 후 +5% | 잘 맞음                  | Custom ASIC 독립 archetype 강화                |
| Cisco AI networking  |                    Stage 2→3 |                         AI orders 후 +16% | 잘 맞음                  | AI networking/switching 가중치 상향             |
| Tower photonics      |                      Stage 2 |                        $1.3B deal 후 +17% | 잘 맞음                  | Photonics Stage 2 visibility 상향            |
| Foxconn AI server    |                      Stage 2 |                 순이익 +19%, shipment 2배 전망 | 매출 증거는 맞음             | ODM은 margin cap 유지                         |
| Kioxia NAND          |                   Stage 3→4B |               주가 20배, profit guidance 급증 | 구조 포착 맞음, 4B 큼        | NAND EPS 상향, Valuation 강한 감점               |
| Supermicro           |            Stage 3처럼 보였다가 4C |                          EY 사임 후 -30% 이상 | RedTeam 매우 잘 맞음       | Accounting hard gate 강화                    |
| CoreWeave            | Stage 2 visibility, 4C-watch |           계약은 강하지만 circular financing 우려 | Green 제한이 맞음          | Capital/FCF penalty 강화                     |
| Cerebras             |            IPO event premium |                       첫날 급등 후 다음날 -10.1% | 4B/valuation watch 맞음 | AI accelerator pure-play cap 강화            |
| Ecolab-CoolIT        |                  Stage 2 M&A |           AI cooling deal에도 Ecolab -1.5% | M&A valuation risk 맞음 | M&A multiple/capital penalty 강화            |

---

### 6-3. R2 Loop 7 점수비중 재조정

이번 검증 결과 R2 점수표는 이렇게 바꾼다.

```text
상향:
HBM EPS/FCF revision
AI storage NAND EPS evidence
반도체 장비 guidance
custom AI ASIC visibility
AI networking orders
photonics/optical PCB bottleneck

유지:
AI server ODM revenue evidence
HBM catch-up optionality
advanced packaging
AI cooling

하향 또는 cap:
AI server ODM 병목점수
neocloud capital/FCF
AI accelerator pure-play valuation
CXL·유리기판·뉴로모픽 theme-only
M&A overpay
회계·공시 신뢰도 없는 AI server 기업
```

구체적으로는 이렇게 간다.

| 항목                     | Loop 6 감각 |                                         Loop 7 조정 |
| ---------------------- | --------: | ------------------------------------------------: |
| EPS/FCF revision       |        중요 |            더 중요. SK하이닉스·Applied·Broadcom에서 가격과 맞음 |
| Visibility             |        중요 |               더 중요. 고객명·출하·AI orders가 가격 반응을 만들었음 |
| Bottleneck             |        중요 | 유지/상향. HBM, NAND, optical PCB, TSMC capacity에서 강함 |
| Mispricing gap         |        중요 |                       유지. 다만 SK하이닉스·Kioxia는 이미 4B |
| Valuation room         |        보조 |                        강한 감점축. 20배 상승·IPO 급등은 cap |
| Capital/FCF            |        보조 |                상향. CoreWeave/Ecolab/Cerebras에서 중요 |
| Information confidence |        보조 |                  상향. Supermicro로 hard gate 필요성 확인 |

---

### 6-4. R2 Loop 7 archetype별 최종 stage 규칙

```text
MEMORY_HBM_CAPACITY:
Stage 1 = AI HBM shortage
Stage 2 = HBM 매출·점유율·고객·출하
Stage 3 = OP/EPS 폭발 + 자본환원 + 가격경로 동행
Stage 4B = 1~2년 급등, consensus 과밀
Stage 4C = HBM 가격하락, CAPA 정상화, 고객 가격저항
```

```text
HBM_CATCHUP_EXECUTION:
Stage 1 = HBM4 기술 발표
Stage 2 = 고객 출하, MOU, initial qualification
Stage 3 = volume shipment + yield + 고객 매출 + EPS
Stage 4B = catch-up 기대 과열
Stage 4C = 파업, production disruption, qualification delay
```

```text
AI_STORAGE_NAND_SHORTAGE:
Stage 1 = AI storage demand / NAND underinvestment
Stage 2 = NAND price/profit guidance
Stage 3 = enterprise SSD/AI storage 매출 + EPS
Stage 4B = 주가 10배~20배 상승
Stage 4C = supply rebound, consumer demand destruction
```

```text
SEMI_EQUIPMENT_AI_CAPEX:
Stage 1 = AI/HBM CAPEX 수요
Stage 2 = 장비 매출·이익 가이던스 상향
Stage 3 = packaging/DRAM equipment growth + EPS/FCF + 가격 동행
Stage 4B = WFE cycle 과열
Stage 4C = order pushout, export control, CAPEX cut
```

```text
CUSTOM_AI_ASIC_HYPERSCALER:
Stage 1 = hyperscaler custom silicon narrative
Stage 2 = 고객명, AI revenue guide, TSMC capacity
Stage 3 = 반복 revenue + margin + FCF + 고객다변화
Stage 4B = custom ASIC consensus 과열
Stage 4C = 낮은 custom margin, 고객 프로젝트 지연, TSMC capacity miss
```

```text
AI_NETWORKING / PHOTONICS / OPTICAL PCB:
Stage 1 = AI data-center interconnect 병목
Stage 2 = AI infra orders, lead time, photonics deal
Stage 3 = revenue/OPM/FCF + repeat orders
Stage 4B = 관련주 동반 과열
Stage 4C = CAPA 정상화, 고객 CAPEX 지연, inventory build
```

```text
AI_SERVER_ODM:
Stage 1 = AI server shipment growth
Stage 2 = revenue/profit growth
Stage 3 = margin, inventory, working capital, customer concentration 통과
Stage 4B = AI server revenue 과열
Stage 4C = accounting trust break, consignment margin squeeze
```

```text
NEOCLOUD_GPU_RENTAL:
Stage 1 = AI compute shortage
Stage 2 = 대형 고객계약
Stage 3 = FCF, debt, depreciation, customer diversification 통과 전까지 제한
Stage 4B = AI cloud contract valuation 과열
Stage 4C = circular financing, refinancing pressure, GPU obsolescence
```

---

# R2 Loop 7 결론

이번 R2 Loop 7의 핵심은 이거다.

```text
HBM:
점수표가 stage와 가격경로를 가장 잘 잡았다.
SK하이닉스는 진짜 structural success지만 이미 4B 감시가 강하다.

HBM catch-up:
삼성 HBM4 출하와 AMD MOU는 Stage 2 포착이 맞았다.
하지만 파업·yield·volume shipment·qualification 확인 전 Stage 3 금지.

NAND:
Kioxia는 AI storage NAND shortage가 실제 profit과 가격으로 연결된 성공사례다.
하지만 주가 20배 상승으로 4B가 매우 강하다.

장비:
Applied Materials는 AI/HBM CAPEX가 장비 가이던스와 가격에 연결된 좋은 사례다.

custom ASIC:
Broadcom은 hyperscaler custom ASIC archetype을 R2 핵심축으로 승격시킨다.

AI networking / photonics:
Cisco와 Tower는 stage 포착과 가격경로가 잘 맞았다.

AI server ODM:
Foxconn은 수요는 맞았지만 ODM margin cap이 필요하다.

반례:
Supermicro는 회계 hard 4C,
CoreWeave는 circular financing/고부채,
Cerebras는 IPO 4B/valuation,
Ecolab-CoolIT은 M&A overpay/accetion delay가 핵심 RedTeam이다.
```

**R2 Loop 7 점수정규화의 핵심 문장:**

> AI·반도체·전자부품은 “AI 수혜”라는 이름이 아니라 **HBM·NAND·장비·custom ASIC·AI networking·photonics·ODM·neocloud·AI accelerator가 각각 어떤 방식으로 EPS/FCF와 가격경로를 만들었는지**로 분리해야 한다.
> 이번 Loop 7에서는 SK하이닉스, Applied Materials, Broadcom, Cisco, Tower가 `stage 포착 → 실제 주가 상승`이 잘 맞은 사례이고, Supermicro, CoreWeave, Cerebras, Ecolab-CoolIT은 `성장 narrative가 있어도 RedTeam이 가격경로를 깨는 사례`다.

다음 순서는 **R3 — 2차전지·전기차·친환경 Loop 7**다.

[1]: https://www.reuters.com/world/asia-pacific/sk-hynix-posts-forecast-beating-q4-profit-huge-ai-demand-2026-01-28/?utm_source=chatgpt.com "SK Hynix's record quarterly profit smashes forecasts, sees explosive memory chip demand"
[2]: https://www.reuters.com/world/asia-pacific/ai-boom-puts-sk-hynix-cusp-1-trillion-market-value-2026-05-14/?utm_source=chatgpt.com "AI boom puts SK Hynix on cusp of $1 trillion market value"
[3]: https://www.reuters.com/technology/samsung-electronics-says-it-has-shipped-hbm4-chips-customers-2026-02-12/?utm_source=chatgpt.com "Samsung ships latest HBM4 chips to catch-up in AI race"
[4]: https://www.reuters.com/world/asia-pacific/samsung-elec-amd-sign-mou-ai-memory-explore-foundry-partnership-2026-03-18/?utm_source=chatgpt.com "Samsung Elec and AMD sign MoU on AI memory, explore foundry partnership"
[5]: https://www.reuters.com/business/world-at-work/samsung-global-ai-boom-spurred-looming-strike-deep-divisions-2026-05-15/?utm_source=chatgpt.com "At Samsung, the global AI boom spurred a looming strike and deep divisions"
[6]: https://www.reuters.com/world/asia-pacific/memory-maker-kioxia-sees-82-billion-q1-profit-ai-boom-2026-05-15/?utm_source=chatgpt.com "Memory maker Kioxia sees $8.2 billion Q1 profit on AI boom"
[7]: https://www.ft.com/content/1e2641ba-14ba-403d-86eb-e484df00964b?utm_source=chatgpt.com "Japanese flash memory maker's profits surge on AI frenzy"
[8]: https://www.reuters.com/business/applied-materials-forecasts-second-quarter-sales-above-estimates-2026-02-12/?utm_source=chatgpt.com "Applied Materials forecasts upbeat results on AI demand, memory shortage"
[9]: https://www.reuters.com/business/applied-materials-sees-quarterly-revenue-above-estimates-2026-05-14/?utm_source=chatgpt.com "Applied Materials sees quarterly revenue above estimates on sustained AI spending"
[10]: https://www.reuters.com/technology/broadcom-forecasts-second-quarter-revenue-above-estimates-2026-03-04/?utm_source=chatgpt.com "Broadcom sees over $100 billion in AI chip sales by 2027 on robust custom chip demand"
[11]: https://www.reuters.com/world/asia-pacific/broadcom-flags-supply-constraints-says-tsmc-capacity-bottleneck-2026-03-24/?utm_source=chatgpt.com "Broadcom flags supply constraints, says TSMC capacity a bottleneck"
[12]: https://www.reuters.com/technology/cisco-raises-annual-revenue-forecast-2026-05-13/?utm_source=chatgpt.com "Cisco to cut about 4,000 jobs in AI-focused restructuring as orders surge"
[13]: https://www.reuters.com/business/tower-semi-forecasts-upbeat-quarterly-revenue-signs-13-billion-ai-chip-deals-2026-05-13/?utm_source=chatgpt.com "Tower Semi forecasts upbeat quarterly revenue, signs $1.3 billion in AI chip deals"
[14]: https://www.reuters.com/world/china/taiwans-foxconn-reports-185-rise-q1-profit-beats-forecast-2026-05-14/?utm_source=chatgpt.com "Foxconn reports forecast-beating 19% jump in Q1 profit on AI demand"
[15]: https://www.reuters.com/technology/super-micro-computer-says-ernst-young-resigns-its-accountant-shares-tank-2024-10-30/?utm_source=chatgpt.com "Super Micro Computer says Ernst & Young resigns as auditor, shares tank"
[16]: https://www.reuters.com/legal/transactional/nvidia-ceos-foundation-buys-108-million-ai-computing-coreweave-donates-it-2026-05-13/?utm_source=chatgpt.com "Nvidia CEO's foundation buys $108 million of AI computing from CoreWeave, donates it to researchers"
[17]: https://www.investors.com/news/technology/cerebras-ipo-cbrs-stock-begins-trading/?utm_source=chatgpt.com "Cerebras Stock Slides A Day After Blockbuster IPO"
[18]: https://www.marketwatch.com/story/cerebrass-stock-looks-like-a-risky-bet-on-ai-hype-a26d66ee?utm_source=chatgpt.com "Cerebras's stock looks like a risky bet on AI hype"
[19]: https://www.reuters.com/business/ecolab-acquire-coolit-systems-475-billion-2026-03-20/?utm_source=chatgpt.com "Ecolab to buy CoolIT for $4.75 billion to tap into AI data center boom"
[20]: https://www.barrons.com/articles/ecolab-cool-it-ai-766f259e?utm_source=chatgpt.com "Ecolab Buys CoolIT Systems for $4.75 Billion. It's All About AI for the Struggling Stock."

좋아. 정해둔 순서대로 이번은 **R2 — AI·반도체·전자부품**으로 넘어간다.

R2는 제일 중요하면서도 제일 위험한 라운드야. 이유는 간단해. 여기에는 **HBM처럼 진짜 구조적 Green이 가능한 축**도 있고, **CXL·유리기판·AI칩·뉴로모픽처럼 아직 매출화 전이면 Watch/Red로 봐야 하는 축**도 같이 섞여 있다. 업로드된 Theme Tag Map v0.5에서도 R2는 HBM, CXL, 시스템반도체, AI칩, 전공정/후공정 장비, 소재, PCB, 유리기판, OLED, MLCC, 클린룸, 스마트폰 부품 같은 테마를 모두 흡수하되, HBM은 Green 가능, CXL·뉴로모픽·AI칩 관련주는 실제 채택·매출 전까지 Watch/Red로 분리해야 한다고 정리되어 있다.

서생원식 원칙으로 보면 R2의 핵심은 “AI 테마라서 좋다”가 아니라, **AI 인프라 수요가 EPS/FCF 체급 변화와 밸류에이션 리레이팅으로 실제 연결되는가**다. 테마명은 점수 근거가 아니고, 실제 수요·계약·CAPA 병목·컨센서스 상향·가격경로가 같이 맞아야 한다.

---

# R2. AI·반도체·전자부품

## 1. 이번 라운드 대섹터

```text
R2 = AI·반도체·전자부품
```

이 라운드의 기본 구조는 이거다.

```text
AI CAPEX 증가
→ GPU / HBM / DRAM / NAND / CoWoS / PCB / 광통신 / 냉각 / 전력 / 서버 수요 증가
→ 공급 병목 또는 고객사 장기계약
→ EPS/FCF 상향
→ 시장이 과거 시클리컬·부품주 프레임을 버림
→ 리레이팅
```

다만 모든 AI 관련주가 같은 점수를 받으면 안 된다.

```text
HBM:
진짜 구조적 Green 가능.

장비·소재·PCB:
고객사 CAPEX와 수주가 확인되면 Watch-to-Green.

AI 서버 ODM:
매출은 커도 저마진·재고·회계 리스크 큼.

Neocloud:
take-or-pay 계약은 좋지만 고부채·GPU 감가상각 리스크 큼.

AI칩 pure-play:
실제 고객·양산·매출 전까지 Watch/Red.

CXL·유리기판·뉴로모픽:
상용화·매출 전까지 Watch/Red.
```

---

## 2. 대상 canonical archetype

이번 R2에서 기준으로 삼을 canonical archetype은 아래로 고정한다.

| 구분                       | canonical archetype                    | Green 정책                     |
| ------------------------ | -------------------------------------- | ---------------------------- |
| HBM·메모리 병목               | `MEMORY_HBM_CAPACITY`                  | Green 가능                     |
| 범용 DRAM/NAND             | `COMMODITY_MEMORY_GENERAL_SEMI`        | Watch-to-Green               |
| 반도체 장비                   | `SEMI_EQUIPMENT_CAPEX`                 | Watch-to-Green               |
| 반도체 소재                   | `SEMI_MATERIALS_PROCESS`               | Watch-to-Green               |
| PCB·고급기판                 | `ADVANCED_PACKAGING_PCB`               | Watch-to-Green               |
| CoWoS·EMIB·첨단패키징         | `ADVANCED_PACKAGING_COWOS_EMIB`        | Green 가능, CAPEX cycle 감시     |
| OLED·디스플레이               | `DISPLAY_OLED_SUPPLYCHAIN`             | Watch                        |
| MLCC·센서·전자부품             | `ELECTRONIC_COMPONENTS_MLCC_SENSOR`    | Watch-to-Green               |
| AI칩·시스템반도체               | `AI_CHIP_FABRIC_INFRA`                 | Watch                        |
| AI accelerator pure-play | `AI_ACCELERATOR_CHIP_PUREPLAY`         | Watch-to-Green, valuation 위험 |
| AI 서버 ODM/EMS            | `AI_SERVER_ODM_EMS_SUPPLY_CHAIN`       | Watch-to-Green               |
| Neocloud / GPU rental    | `NEOCLOUD_GPU_RENTAL`                  | High-risk Watch              |
| 광통신·광케이블                 | `OPTICAL_NETWORKING_AI_DATACENTER`     | Green 가능                     |
| 반도체 산업가스                 | `INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA` | Watch-to-Green               |
| AI 데이터센터 냉각              | `AI_DATA_CENTER_COOLING`               | Green 가능                     |
| 데이터센터 REIT               | `DATA_CENTER_REIT_INFRASTRUCTURE`      | Watch-to-Green               |
| AI grid flexibility      | `AI_GRID_FLEXIBILITY_SOFTWARE`         | Watch                        |
| 회계·감사 신뢰도 overlay        | `REDTEAM_ACCOUNTING_TRUST_OVERLAY`     | hard gate                    |

---

## 3. deep sub-archetype

R2는 canonical archetype 밑에서 이렇게 더 쪼개야 한다.

```text
MEMORY_HBM_CAPACITY
- HBM3E / HBM4
- HBM CAPA constraint
- 장기계약 / 선수금 / price band
- Nvidia 공급망
- 메모리 PBR → PER 프레임 전환

COMMODITY_MEMORY_GENERAL_SEMI
- 범용 DRAM
- NAND
- AI 서버 수요에 의한 범용 memory 가격 상승
- HBM 생산 전환으로 범용 memory 공급 squeeze

SEMI_EQUIPMENT_CAPEX
- EUV
- 전공정 장비
- 후공정 장비
- AI/HBM fab CAPEX
- packaging 장비

ADVANCED_PACKAGING_COWOS_EMIB
- CoWoS-S
- CoWoS-L
- EMIB
- 2.5D packaging
- interposer / substrate
- packaging bottleneck

ADVANCED_PACKAGING_PCB
- AI 서버 PCB
- optical transceiver PCB
- 유리기판
- CXL 관련 기판

OPTICAL_NETWORKING_AI_DATACENTER
- 광섬유
- 광케이블
- optical transceiver
- laser
- AI 데이터센터 내부 네트워크

AI_SERVER_ODM_EMS_SUPPLY_CHAIN
- AI server rack
- ODM/EMS
- Foxconn류
- Supermicro류
- 저마진·재고·회계 리스크

NEOCLOUD_GPU_RENTAL
- GPU cloud
- CoreWeave류
- take-or-pay 계약
- GPU 담보부채
- 고객집중

AI_CHIP_FABRIC_INFRA
- 시스템반도체
- 파운드리
- Tesla AI6
- AI칩 국산화
- tape-out / 양산 / 수율

AI_ACCELERATOR_CHIP_PUREPLAY
- Cerebras류
- wafer-scale engine
- AI accelerator IPO
- Nvidia 경쟁

DISPLAY_OLED_SUPPLYCHAIN
- OLED 소재
- OLED 장비
- LCD → OLED 전환
- Apple OLED 전환

ELECTRONIC_COMPONENTS_MLCC_SENSOR
- MLCC
- 센서
- 스마트폰 부품
- 카메라
- LED
- 무선충전

INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA
- 초고순도 질소
- fab gas plant
- onsite utility
- long-term gas supply

AI_DATA_CENTER_COOLING
- 액침냉각
- direct liquid cooling
- HVAC
- thermal management

REDTEAM_ACCOUNTING_TRUST_OVERLAY
- auditor resignation
- filing delay
- internal control weakness
- related-party transaction
```

---

# 4. 성공사례

## 4-1. SK하이닉스 — `MEMORY_HBM_CAPACITY`

SK하이닉스는 R2의 핵심 성공사례다. Reuters는 AI 수요와 HBM 중요성으로 SK하이닉스 주가가 2025년에 274%, 2026년에 200% 이상 상승했고, 시가총액이 약 9,420억 달러까지 올라 1조 달러에 근접했다고 보도했다. 이건 단순 메모리 업황 회복이 아니라, **메모리 = AI 인프라 병목**이라는 시장 프레임 전환이 실제 가격 경로로 확인된 사례다. ([Reuters][1])

**가격경로 1차 판정**

```text
가격 검증:
2025년 +274%
2026년 +200% 이상
시총 16개월 전 1,000억 달러 미만 → 약 9,420억 달러

판정:
aligned_success + 4B_watch

의미:
Stage 2/3 이후 EPS/FCF와 valuation frame이 같이 리레이팅된 강한 성공사례.
다만 이미 시장이 AI memory rerating을 강하게 인정했으므로 4B-watch 필요.
```

**점수 교정**

```text
EPS/FCF: 매우 강하게
Structural Visibility: 강하게
Bottleneck/Pricing: 강하게
Market Mispricing: 초반에는 강했으나, 현재는 축소
Valuation Rerating: 이미 많이 진행
Risk Penalty: crowding, CAPEX reversal, 고객사 가격저항
```

---

## 4-2. SK하이닉스 EUV 대형 CAPEX — `SEMI_EQUIPMENT_CAPEX`

SK하이닉스는 ASML의 EUV 장비 약 80억 달러어치를 2027년 말까지 구매하기로 했다. 이 장비는 차세대 공정과 HBM 경쟁력 유지에 필요한 CAPEX로 설명된다. 이 사례는 HBM 수요가 단순 가격 상승을 넘어 **고객사·메모리 업체의 실제 장비 CAPEX**로 연결된다는 신호다. ([월스트리트저널][2])

**가격경로 1차 판정**

```text
판정:
equipment_capex_success_signal

확인할 것:
ASML·반도체 장비주·국내 장비/소재주가 이 CAPEX cycle에서 실제 수주·매출을 얻었는지.
```

**점수 교정**

```text
장비주는 HBM 생산업체보다 visibility를 낮게 둔다.
이유:
고객사 CAPEX cycle, order push-out, 수출통제, CAPEX peak risk 때문.
```

---

## 4-3. Applied Materials — `SEMI_EQUIPMENT_CAPEX` / `ADVANCED_PACKAGING_COWOS_EMIB`

Applied Materials는 AI·데이터센터 투자 수요로 2026년 3분기 매출 전망을 시장 예상보다 높게 제시했고, 반도체 장비 사업은 30% 이상, packaging revenue는 50% 이상 성장할 것으로 전망했다. 실적 발표 후 주가는 시간외에서 약 3% 상승했다. ([Reuters][3])

**가격경로 1차 판정**

```text
가격 반응:
가이던스 상향 후 시간외 +3%

판정:
early_aligned_candidate

검증 필요:
180D / 1Y MFE
packaging revenue growth가 실제 EPS revision과 동행하는지
CAPEX cycle peak 이후 drawdown 여부
```

**점수 교정**

```text
EPS/FCF: 강함
Visibility: 중간~강함
Bottleneck: 강함
Risk: 고객사 CAPEX cycle, order delay, 수출통제
```

---

## 4-4. Nvidia CoWoS-L / packaging 병목 — `ADVANCED_PACKAGING_COWOS_EMIB`

Nvidia CEO Jensen Huang은 Blackwell이 CoWoS-L을 사용하며, Nvidia의 advanced packaging 수요는 줄어드는 게 아니라 기술 종류가 바뀌고 있다고 설명했다. 그는 CoWoS capacity가 2년 전보다 크게 늘었지만 여전히 packaging은 병목이라고 말했다. ([Reuters][4])

**가격경로 1차 판정**

```text
판정:
structural_bottleneck_reference

검증 대상:
CoWoS 장비·소재·기판 업체의 수주와 EPS revision
```

**점수 교정**

```text
CoWoS/advanced packaging은 Green 가능.
다만 capacity expansion으로 병목이 완화되는 시점에는 4B-watch 필요.
```

---

## 4-5. Broadcom supply constraint — `OPTICAL_NETWORKING_AI_DATACENTER` / `ADVANCED_PACKAGING_PCB`

Broadcom은 TSMC capacity가 병목이 되었고, AI 칩 수요가 급증하면서 lasers와 optical transceiver용 PCB도 병목이라고 밝혔다. 특히 optical transceiver PCB lead time이 6주에서 6개월로 늘었다고 언급했다. ([Reuters][5])

**가격경로 1차 판정**

```text
판정:
supply_chain_bottleneck_reference

의미:
AI 병목이 GPU/HBM에서 optical, PCB, laser까지 확산.
```

**점수 교정**

```text
OPTICAL_NETWORKING_AI_DC:
Green 가능 하위축으로 상향.

ADVANCED_PACKAGING_PCB:
기존 Watch-to-Green 유지하되, AI optical PCB 직접 노출이면 점수 강화.
```

---

## 4-6. Meta–Corning 광섬유 계약 — `OPTICAL_NETWORKING_AI_DATACENTER`

Meta는 AI 데이터센터 확장을 위해 Corning과 최대 60억 달러 규모의 광섬유 케이블 공급계약을 체결했다. 계약은 2030년까지 이어지고, Corning은 고급 optical fiber, cable, connectivity 제품을 공급하며, Corning 주가는 2025년에 84% 이상 오른 뒤 이 계약 보도에서 premarket 7% 추가 상승했다. ([Reuters][6])

**가격경로 1차 판정**

```text
가격 반응:
2025년 +84% 이상
계약 보도 premarket +7%

판정:
aligned_candidate + 4B_watch

의미:
AI 데이터센터 광통신 병목이 실제 장기계약과 주가 리레이팅으로 연결된 사례.
다만 이미 많이 오른 상태라 4B-watch 필요.
```

---

## 4-7. Tower Semiconductor — `AI_CHIP_FABRIC_INFRA` / silicon photonics

Tower Semiconductor는 2027년에 AI 데이터센터 내 고속 데이터 이동을 위한 light-based chip 공급계약 13억 달러를 체결했고, 이 소식에 미국 상장주가가 장초반 17% 이상 상승했다. ([Reuters][7])

**가격경로 1차 판정**

```text
가격 반응:
계약 보도 후 +17% 이상

판정:
event_aligned_candidate

검증 필요:
계약이 2027년 매출·OP로 실제 연결되는지
이후 180D/1Y MFE와 MAE
```

**점수 교정**

```text
AI chip/fabric infra는 대부분 Watch지만,
실제 10억 달러급 계약 + 매출 시점이 있으면 Stage 2 이상 가능.
```

---

## 4-8. Air Liquide–Micron — `INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA`

Air Liquide는 Micron의 Idaho fab에 초고순도 질소와 기타 가스를 공급하기 위해 2.5억 달러 규모 신규 플랜트를 짓기로 했다. 이 플랜트는 AI에 필요한 advanced memory 생산을 지원하고 2025년 말 가동 예정으로 보도됐다. ([Reuters][8])

**가격경로 1차 판정**

```text
판정:
utility_like_success_candidate

의미:
반도체 산업가스는 일회성 장비가 아니라 fab이 돌아가는 동안 필요한 반복 utility 매출.
```

**점수 교정**

```text
Visibility: 강함
Bottleneck: 중간
Capital Allocation: 중간
Risk: fab delay, customer concentration, energy cost
```

---

## 4-9. Ecolab–CoolIT — `AI_DATA_CENTER_COOLING`

Ecolab은 AI 데이터센터 액체냉각 수요를 잡기 위해 CoolIT Systems를 47.5억 달러에 인수하기로 했다. CoolIT은 Nvidia·AMD 같은 칩메이커에 액체냉각 시스템을 공급하고, 향후 1년 매출이 약 5.5억 달러로 예상된다고 보도됐다. ([Reuters][9])

**가격경로 1차 판정**

```text
판정:
strategic_success_candidate

검증 필요:
인수 후 EPS accretion
CoolIT 매출 성장
부채 조달 부담
Ecolab 주가 180D/1Y 경로
```

**점수 교정**

```text
AI 냉각은 Green 가능.
다만 M&A 가격이 높거나 debt 부담이 있으면 4B/RedTeam.
```

---

## 4-10. CoreWeave — `NEOCLOUD_GPU_RENTAL`

CoreWeave는 Nvidia-backed GPU cloud 업체로 IPO를 했지만, IPO 가격은 기대 범위인 47~55달러보다 낮은 40달러에 책정됐다. 회사는 2024년 매출 19억 달러에 순손실 8.63억 달러를 기록했고, 부채가 약 80억 달러였으며, Microsoft가 2024년 매출의 62%를 차지했다. ([Investopedia][10])

**가격경로 1차 판정**

```text
판정:
high_risk_watch_candidate

의미:
neocloud는 계약 visibility가 강할 수 있지만, 고부채·고객집중·GPU 감가상각·FCF 적자가 너무 크다.
```

**점수 교정**

```text
Visibility: take-or-pay 계약이 있으면 높게
EPS/FCF: FCF 전환 전까지 제한
Risk Penalty: 매우 강함
Green: FCF·부채 안정 확인 전 금지
```

---

## 4-11. Blackstone Digital Infrastructure Trust — `DATA_CENTER_REIT_INFRASTRUCTURE`

Blackstone Digital Infrastructure Trust는 17.5억 달러 IPO를 통해 데이터센터 자산에 투자하려 하지만, 상장 첫날 20달러로 IPO가와 같은 수준에서 출발했다. 이 REIT는 아직 데이터센터 자산을 취득하지 않은 상태이고, hyperscale tenant 대상 신규 데이터센터 자산에 투자할 계획이라고 보도됐다. ([Reuters][11])

**가격경로 1차 판정**

```text
가격 반응:
IPO가와 동일한 flat debut

판정:
no_rerating_yet / infrastructure_theme_needs_assets

의미:
AI 데이터센터 REIT는 Green 가능성이 있지만, 실제 자산·tenant·AFFO가 없으면 아직 테마.
```

---

# 5. 반례

## 5-1. Supermicro — `AI_SERVER_ACCOUNTING_GOVERNANCE_RISK`

Supermicro는 AI 서버 수요로 2023년 초 약 44억 달러였던 시가총액이 2024년 3월 약 670억 달러까지 급등했지만, 이후 Ernst & Young이 감사인에서 사임하며 주가가 30% 이상 급락했다. EY는 경영진과 감사위원회의 진술을 더 이상 신뢰할 수 없다고 밝혔다. ([Reuters][12])

**교훈**

```text
AI 서버 매출 성장
≠ 회계 신뢰도 통과

감사인 사임, filing delay, 내부통제 문제는 hard 4C.
```

**가격경로 1차 판정**

```text
초기:
AI 서버 리레이팅 성공

이후:
감사인 사임 후 -30% 이상

판정:
early_rerating_success_then_hard_4c
```

---

## 5-2. AI server ODM/EMS 저마진·재고 리스크

Foxconn은 AI 서버 수요로 실적이 좋아졌지만, AI server ODM/EMS는 HBM과 다르게 고마진 병목이라기보다 대량 생산·조립·공급망 관리 모델에 가깝다. Foxconn은 AI server rack shipments가 2배 이상 늘 것으로 예상하지만, 주가가 시장 전체를 압도했다는 증거는 아직 제한적이다. ([월스트리트저널][13])

**교훈**

```text
AI server 매출 증가만으로 HBM식 Green을 주면 안 된다.
OP margin, 재고, 고객사 집중, 회계 신뢰도 확인 필요.
```

---

## 5-3. 범용 DRAM/NAND와 HBM 혼동

Samsung은 AI 서버와 데이터센터 인프라 수요로 범용 DRAM·NAND 가격이 올라 2025년 3분기 실적을 개선했지만, 동시에 HBM 공급에서는 SK하이닉스보다 뒤처졌다는 평가를 받았다. 범용 memory 가격 상승은 EPS를 크게 올릴 수 있지만, HBM의 장기계약·병목성과 같은 구조적 visibility는 더 낮게 봐야 한다. ([AP News][14])

**교훈**

```text
범용 DRAM/NAND price rebound
≠ HBM structural rerating

범용 메모리는 EPS 점수는 높게,
visibility와 rerating 점수는 HBM보다 낮게.
```

---

## 5-4. AI chip pure-play valuation 과열

Cerebras는 AI chip pure-play 성공 후보지만, IPO 기대와 valuation이 너무 빠르게 앞서갈 수 있다. 보도에 따르면 Cerebras는 IPO 첫날 강하게 상승했고, wafer-scale AI chip narrative로 큰 valuation을 받았다. 하지만 AI accelerator pure-play는 Nvidia 경쟁, 고객 검증, 수율, R&D burn, valuation overheat를 동시에 봐야 한다. ([Investors][15])

**교훈**

```text
AI chip 기술력
≠ 바로 Green

실제 고객, 양산, gross margin, FCF, valuation을 확인해야 한다.
```

---

## 5-5. Neocloud 고부채·고객집중 반례

CoreWeave는 AI compute 수요를 직접 받지만, IPO가가 낮아졌고, Microsoft 매출 집중, 80억 달러 부채, 2024년 순손실 8.63억 달러가 핵심 리스크로 드러났다. ([Investopedia][10])

**교훈**

```text
take-or-pay 계약은 visibility를 높이지만,
debt/FCF/customer concentration이 해결되지 않으면 Green 금지.
```

---

# 6. 4B-watch 사례

## 6-1. SK하이닉스

SK하이닉스는 구조적 성공사례지만, 주가가 2025년 274%, 2026년 200% 이상 오른 만큼 4B-watch를 강하게 켜야 한다. ([Reuters][1])

```text
4B 조건:
- 모두가 AI memory rerating 인정
- 시총 1조 달러 근접
- 글로벌 자금 crowded
- 고객사 가격 저항 가능성
- CAPEX 증설 뉴스 증가
```

---

## 6-2. Corning / optical networking

Corning은 AI 데이터센터 광섬유 수요로 2025년 84% 이상 올랐고, Meta 계약 보도에서 추가 상승했다. 이건 성공사례지만 이미 많이 오른 상태라 optical networking 전체에 4B-watch가 필요하다. ([Reuters][6])

```text
4B 조건:
- optical networking 관련주 동반 급등
- hyperscaler 계약 기대 과밀
- valuation multiple 과열
- CAPA 증설로 lead time 정상화 가능성
```

---

## 6-3. Advanced packaging

Nvidia는 CoWoS 수요가 줄어든 게 아니라 CoWoS-L 중심으로 바뀌고 있다고 설명했지만, Jensen Huang은 지난 2년 동안 packaging capacity가 크게 늘었다고도 말했다. 병목이 강한 건 맞지만, CAPA가 계속 늘면 4B-watch가 필요하다. ([Reuters][4])

```text
4B 조건:
- CoWoS 병목을 모두가 인정
- 장비·기판·소재주 동반 과열
- CAPA 확장 뉴스 증가
- lead time 정상화
```

---

# 7. 4C-thesis-break 사례

## 7-1. Supermicro 감사인 사임

감사인 사임, 내부통제 우려, annual filing delay, DOJ 조사 보도는 AI 서버 고성장주에 대한 hard 4C다. ([Reuters][12])

```text
4C:
auditor_resignation
filing_delay
internal_control_weakness
DOJ/SEC investigation
related_party_transaction_risk
```

---

## 7-2. Neocloud debt/FCF breakdown

CoreWeave 같은 neocloud는 매출 성장에도 불구하고 debt, FCF 적자, 고객집중이 악화되면 4C로 갈 수 있다. IPO가가 기대보다 낮게 책정된 것 자체가 시장이 이 리스크를 이미 반영한 신호다. ([Investopedia][10])

```text
4C:
debt_refinancing_pressure
GPU_obsolescence
customer_concentration
FCF_negative
```

---

## 7-3. AI chip 고객 검증 실패

AI accelerator pure-play는 실제 고객·양산·수율 검증 전까지 4C 위험이 크다. Cerebras처럼 IPO 흥행이 있더라도, 이후 고객 다변화와 gross margin, FCF 전환을 확인해야 한다. ([Investors][15])

```text
4C:
customer_validation_failed
foundry_yield_issue
valuation_overheat
Nvidia_competition
```

---

## 7-4. 범용 memory supply rebound

Samsung식 범용 memory 회복은 EPS를 강하게 만들 수 있지만, 공급이 다시 풀리거나 HBM 경쟁력 격차가 유지되면 HBM식 리레이팅으로 오판한 케이스는 4C 또는 false-positive가 된다. ([AP News][14])

---

# 8. 점수비중 보정표 — R2 v1.0

| canonical archetype                    | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | 핵심 감점                                     |
| -------------------------------------- | ------: | ---------: | ---------: | ---------: | --------: | ------: | ---: | ----------------------------------------- |
| `MEMORY_HBM_CAPACITY`                  |      24 |         21 |         19 |         15 |        12 |       0 |    5 | CAPEX reversal, crowding, 고객 가격저항         |
| `COMMODITY_MEMORY_GENERAL_SEMI`        |      22 |         16 |         17 |         13 |        10 |       0 |    5 | spot rebound, supply rebound, HBM lag     |
| `SEMI_EQUIPMENT_CAPEX`                 |      22 |         20 |         18 |         14 |        12 |       0 |    5 | 고객 CAPEX, order delay, 수출통제               |
| `SEMI_MATERIALS_PROCESS`               |      20 |         18 |         14 |         13 |        11 |       0 |    5 | 고객집중, 재고, 단가 압박                           |
| `ADVANCED_PACKAGING_PCB`               |      21 |         20 |         18 |         13 |        12 |       0 |    5 | 고객집중, CAPA 정상화                            |
| `ADVANCED_PACKAGING_COWOS_EMIB`        |      22 |         21 |         20 |         14 |        12 |       0 |    5 | CAPEX cycle, yield, 병목 완화                 |
| `DISPLAY_OLED_SUPPLYCHAIN`             |      19 |         18 |         12 |         13 |        11 |       0 |    5 | 패널 가격경쟁, CAPEX cycle                      |
| `ELECTRONIC_COMPONENTS_MLCC_SENSOR`    |      19 |         17 |         13 |         12 |        11 |       1 |    5 | 재고, 고객집중, 중국 공급망                          |
| `AI_CHIP_FABRIC_INFRA`                 |      18 |         15 |         12 |         14 |        11 |       0 |    5 | 고객검증, 수율, 매출 부재                           |
| `AI_ACCELERATOR_CHIP_PUREPLAY`         |      18 |         15 |         13 |         15 |        10 |       0 |    5 | Nvidia 경쟁, valuation 과열                   |
| `AI_SERVER_ODM_EMS_SUPPLY_CHAIN`       |      22 |         19 |         16 |         14 |        11 |       0 |    5 | 저마진, 재고, 회계, 고객집중                         |
| `NEOCLOUD_GPU_RENTAL`                  |      18 |         21 |         18 |         14 |        10 |       0 |    5 | 고부채, GPU 감가상각, FCF 적자                     |
| `OPTICAL_NETWORKING_AI_DATACENTER`     |      21 |         22 |         20 |         13 |        12 |       0 |    5 | 고객집중, valuation crowding                  |
| `INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA` |      19 |         23 |         13 |         13 |        12 |       3 |    5 | fab 지연, 고객집중, 에너지비                        |
| `AI_DATA_CENTER_COOLING`               |      21 |         22 |         22 |         13 |        12 |       0 |    5 | AI CAPEX 지연, 저마진 프로젝트                     |
| `DATA_CENTER_REIT_INFRASTRUCTURE`      |      18 |         23 |         18 |         13 |        13 |       5 |    5 | CAPEX, funding cost, tenant concentration |
| `AI_GRID_FLEXIBILITY_SOFTWARE`         |      17 |         17 |         15 |         13 |        10 |       0 |    6 | PoC, 상용화 지연                               |
| `REDTEAM_ACCOUNTING_TRUST_OVERLAY`     |    gate |       gate |       gate |       gate |      gate |    gate | gate | auditor resignation, filing delay         |

---

# 9. stage date 후보

## `MEMORY_HBM_CAPACITY`

```text
Stage 1:
AI 서버 HBM 수요 급증, Nvidia향 HBM 수요, HBM price/contract 뉴스

Stage 2:
실제 실적 서프라이즈, HBM 매출 비중 상승, OP/EPS 상향 리포트

Stage 3:
장기계약·선수금·price band·CAPA constraint와 multi-year EPS revision 확인

Stage 4B:
시총/valuation 포화, 모두가 AI memory rerating 인정, 글로벌 자금 crowded

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
장비주 동반 과열, 고객사 CAPEX peak

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
AI server rack 수요 증가 뉴스

Stage 2:
AI server 매출·shipment·OP 증가 확인

Stage 3:
AI server mix가 회사 전체 EPS/FCF 체급을 바꾼 시점

Stage 4B:
AI server 관련주 valuation 과열

Stage 4C:
회계·감사·재고·저마진·고객집중 이슈
```

## `NEOCLOUD_GPU_RENTAL`

```text
Stage 1:
대형 GPU cloud 계약, IPO filing, OpenAI/Microsoft 계약

Stage 2:
take-or-pay backlog, 매출 성장, EBITDA 개선 확인

Stage 3:
FCF 전환 또는 부채 안정화 확인

Stage 4B:
AI cloud valuation 과열

Stage 4C:
refinancing pressure, GPU obsolescence, customer concentration
```

## `OPTICAL_NETWORKING_AI_DATACENTER`

```text
Stage 1:
AI 데이터센터 optical networking 병목 뉴스

Stage 2:
hyperscaler 계약, lead time 증가, 수주 evidence

Stage 3:
OP/EPS 상향 + 장기계약 + 병목 프레임 전환

Stage 4B:
valuation crowding, optical 관련주 동반 과열

Stage 4C:
CAPA 정상화, 고객사 CAPEX 지연, 주문 취소
```

---

# 10. 가격경로 검증계획

## R2 공통 검증 방식

```text
1. 각 case의 stage1_date, stage2_date, stage3_date를 지정한다.
2. 해당 날짜의 종가를 stage_price로 저장한다.
3. 30D / 90D / 180D / 1Y / 2Y MFE를 계산한다.
4. 30D / 90D / 180D / 1Y MAE를 계산한다.
5. peak_price와 drawdown_after_peak를 계산한다.
6. EPS revision, revenue guidance, backlog, margin, customer concentration과 가격 경로를 비교한다.
```

## R2 가격경로에서 반드시 분리할 판정

```text
aligned:
AI 수요 evidence 이후 매출·EPS·주가가 같이 리레이팅.

4B-watch:
실적은 좋지만 valuation과 crowding이 너무 앞선 상태.

thesis_break:
회계·감사·고객사 주문·CAPEX cut으로 논리 훼손.

false_positive_score:
AI 테마로 점수는 높았지만 매출·EPS가 안 따라옴.

price_moved_without_evidence:
주가만 올랐고 실제 계약·수주·매출 없음.

cyclical_success:
범용 DRAM/NAND 가격 상승처럼 수익은 가능하지만 구조적 HBM 리레이팅은 아님.
```

## 이번 R2에서 우선 검증할 가격 case

| case_id                                       |                 stage2 후보일 | 현재 1차 가격판정                              |
| --------------------------------------------- | -------------------------: | --------------------------------------- |
| `sk_hynix_hbm_rerating_success_case`          | 2025~2026 주요 실적·HBM 계약 확인일 | +274%, +200% 이상. aligned + 4B-watch     |
| `samsung_commodity_memory_recovery_case`      |               2025 Q3 실적발표 | EPS 회복 후보, HBM lag 감점                   |
| `sk_hynix_asml_euv_capex_case`                |                 2026-03-24 | equipment capex signal                  |
| `applied_materials_ai_packaging_growth_case`  |                 2026-05-14 | 시간외 +3%, early aligned                  |
| `nvidia_cowos_l_packaging_bottleneck_case`    |                 2025-01-16 | bottleneck reference                    |
| `broadcom_optical_pcb_leadtime_case`          |                 2026-03-24 | optical/PCB bottleneck reference        |
| `meta_corning_fiber_contract_case`            |                 2026-01-27 | 2025 +84%, 보도 후 +7%, aligned + 4B-watch |
| `tower_semiconductor_ai_light_chip_deal_case` |                 2026-05-13 | +17% 이상, event aligned candidate        |
| `air_liquide_micron_gas_plant_case`           |                 2024-06-05 | utility-like success candidate          |
| `ecolab_coolit_liquid_cooling_case`           |                 2026-03-20 | strategic cooling candidate             |
| `coreweave_neocloud_high_debt_case`           |                2025-03 IPO | high-risk watch                         |
| `blackstone_data_center_reit_case`            |                 2026-05-14 | flat IPO debut, no-rerating-yet         |
| `supermicro_ey_resignation_4c_case`           |                 2024-10-30 | -30% 이상, hard 4C                        |

---

# 11. 다음에 에이전트가 채워야 할 price fields

R2 case library에는 아래 필드가 필요하다.

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
below_stage3_price_flag

revenue_revision_1q
revenue_revision_1y
op_revision_1q
op_revision_1y
eps_revision_1q
eps_revision_1y

gross_margin_change
op_margin_change
inventory_growth
capex_growth
backlog_growth
customer_concentration
debt_to_ebitda
fcf_margin

accounting_red_flag
auditor_resignation
filing_delay
internal_control_issue

score_price_alignment
price_validation_status
```

---

# R2 결론

R2는 “AI 수혜”라는 한 단어로 묶으면 망한다. 반드시 하위축별로 나눠야 한다.

```text
진짜 Green 가능:
HBM
AI optical networking
AI data center cooling
advanced packaging
반도체용 industrial gases
AI data center power/infra 일부

Watch-to-Green:
반도체 장비
반도체 소재
AI server ODM
범용 DRAM/NAND
데이터센터 REIT
AI chip fabric infra
AI accelerator pure-play

High-risk Watch:
Neocloud GPU rental
AI server ODM 중 저마진·회계 리스크 있는 기업

Red / hard 4C:
감사인 사임
filing delay
내부통제 문제
AI칩 관련주지만 실제 매출 없음
CXL/유리기판/뉴로모픽 테마만 있음
```

**R2 점수정규화의 핵심 문장:**

> AI·반도체·전자부품은 “AI 테마”가 아니라 **HBM, packaging, optical, cooling, equipment, server ODM, neocloud, AI chip pure-play의 경제구조가 서로 다르다.**
> EPS/FCF와 가격경로가 같이 움직인 축만 Green 후보이고, 회계·고부채·고객집중·매출 부재는 즉시 RedTeam이다.

다음에 네가 “다음 라운드 진행해줘”라고 하면, 정해둔 순서에 따라 **R3 — 2차전지·전기차·친환경**으로 넘어간다.

[1]: https://www.reuters.com/world/asia-pacific/ai-boom-puts-sk-hynix-cusp-1-trillion-market-value-2026-05-14/?utm_source=chatgpt.com "AI boom puts SK Hynix on cusp of $1 trillion market value"
[2]: https://www.wsj.com/business/sk-hynix-to-buy-8-billion-of-asml-euv-equipment-ebdf1753?utm_source=chatgpt.com "SK Hynix to Buy $8 Billion of ASML EUV Equipment"
[3]: https://www.reuters.com/business/applied-materials-sees-quarterly-revenue-above-estimates-2026-05-14/?utm_source=chatgpt.com "Applied Materials sees quarterly revenue above estimates on sustained AI spending"
[4]: https://www.reuters.com/technology/nvidia-ceo-says-its-advanced-packaging-technology-needs-are-changing-2025-01-16/?utm_source=chatgpt.com "Nvidia CEO says its advanced packaging technology needs are changing"
[5]: https://www.reuters.com/world/asia-pacific/broadcom-flags-supply-constraints-says-tsmc-capacity-bottleneck-2026-03-24/?utm_source=chatgpt.com "Broadcom flags supply constraints, says TSMC capacity a bottleneck"
[6]: https://www.reuters.com/business/meta-signs-deal-pay-corning-up-6-billion-fiber-optic-cables-cnbc-reports-2026-01-27/?utm_source=chatgpt.com "Meta, Corning sign deal worth up to $6 billion for fiber-optic cables in AI data centers"
[7]: https://www.reuters.com/business/tower-semi-forecasts-upbeat-quarterly-revenue-signs-13-billion-ai-chip-deals-2026-05-13/?utm_source=chatgpt.com "Tower Semi forecasts upbeat quarterly revenue, signs $1.3 billion in AI chip deals"
[8]: https://www.reuters.com/business/energy/air-liquide-plans-250-mln-plant-supply-gas-chipmaker-micron-2024-06-05/?utm_source=chatgpt.com "Air Liquide plans $250 mln plant to supply gas for chipmaker Micron"
[9]: https://www.reuters.com/business/ecolab-acquire-coolit-systems-475-billion-2026-03-20/?utm_source=chatgpt.com "Ecolab to buy CoolIT for $4.75 billion to tap into AI data center boom"
[10]: https://www.investopedia.com/nvidia-backed-coreweave-prices-its-ipo-at-usd40-per-share-below-expectations-11701963?utm_source=chatgpt.com "Nvidia-Backed CoreWeave Prices Its IPO at $40 Per Share, Below Expectations"
[11]: https://www.reuters.com/technology/blackstone-data-center-vehicle-opens-flat-new-york-debut-after-175-billion-ipo-2026-05-14/?utm_source=chatgpt.com "Blackstone data center vehicle makes muted debut after $1.75 billion IPO"
[12]: https://www.reuters.com/technology/super-micro-computer-says-ernst-young-resigns-its-accountant-shares-tank-2024-10-30/?utm_source=chatgpt.com "Super Micro Computer says Ernst & Young resigns as auditor, shares tank"
[13]: https://www.wsj.com/tech/foxconn-posts-strong-results-on-ai-hardware-sales-81f2ab18?utm_source=chatgpt.com "Foxconn Posts Strong Results on AI Hardware Sales"
[14]: https://apnews.com/article/88898e96dc8e9343f2f78fdb07dd425c?utm_source=chatgpt.com "Samsung reports 32% rise in operating profit and predicts continued AI-related growth"
[15]: https://www.investors.com/news/technology/cerebras-ipo-cbrs-stock-begins-trading/?utm_source=chatgpt.com "Cerebras IPO Scores Blockbuster Debut As Next Hot AI Stock"

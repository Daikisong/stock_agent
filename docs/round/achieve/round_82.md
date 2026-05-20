좋아. **R2 Loop 4까지 끝났으니, 이번은 R3 Loop 4 — 2차전지·전기차·친환경**으로 간다.

R3는 2차전지 소재·부품·공정장비, 폐배터리, 전고체, 전기차 인프라, 전기차 화재, 수소차 연료전지·인프라, 태양광, 풍력, 탄소배출권, 폐기물처리, 탈플라스틱을 흡수하는 대섹터다. Theme Tag Map 기준으로도 R3는 **Green보다 과열 방어가 우선**이고, 소재·전고체·폐배터리는 실제 계약·수익성·FCF 확인 전까지 Stage 3-Green을 제한해야 한다.

Checkpoint 20 원칙도 그대로 적용한다. 공급계약, 투자금액, 계약기간, 매출 대비 계약금액, 고객사, 가동률, OP YoY, 회수량, 금속 회수 매출, 공장 idle, 계약 취소 같은 값은 실제 공시·기사·리포트에서 확인될 때만 써야 한다. R3는 “ESS”, “폐배터리”, “전고체”, “AI 데이터센터 전력”, “친환경” 같은 단어만으로 점수가 쉽게 부풀기 때문에, 빈 값을 추정하면 false-positive가 커진다.

서생원식으로 보면 R3의 질문은 “전기차가 성장하나?”가 아니다. **EV 성장 narrative가 아니라 EPS/FCF 체급 변화가 지속되고, 시장이 아직 과거 프레임으로 낮게 보는가**다. EV CAPA가 늘어도 공장이 멈추면 4C이고, ESS 계약이 실제 금액·기간·고객·마진으로 확인되면 Stage 2~3 후보가 된다.

---

# R3 Loop 4. 2차전지·전기차·친환경

## 1. 이번 라운드 대섹터

```text
R3 = 2차전지·전기차·친환경
Loop 4 목표 =
EV CAPA 과열 / ESS 장기계약 / AI 데이터센터 저장장치 / EV→ESS 라인전환 /
폐배터리·second-life / 태양광 공급망 / 풍력 project economics /
리튬 cycle / EV·BESS 안전규제를 완전히 분리
```

이번 회차의 핵심 질문은 이거다.

```text
이 회사는 EV 성장 narrative에 기대고 있는가?
아니면 EV 둔화 속에서도 ESS, AI 데이터센터 저장장치, 재활용, 폐기물처리,
수소, 탄소·수처리 인프라로 반복 FCF를 만들 수 있는가?
```

R3에서 가장 위험한 오판은 여전히 이거다.

```text
EV 성장 산업
= 모든 2차전지주 Green
```

Loop 4부터는 이렇게 본다.

```text
좋은 구조 후보:
ESS 장기계약 + 계약금액 + 계약기간 + 고객 + GWh + ESS OPM
EV 공장 idle을 ESS 라인으로 전환하고 실제 고객계약이 붙는 기업
폐배터리 + 금속 회수 + ESS/grid storage + 고객계약
폐기물처리 허가권 + 처리량 + 반복 FCF
수소 CAPEX + 실제 고객 + 가동률 + OPM
AI 데이터센터 water/energy reuse 계약

위험한 후보:
EV CAPA 증설만 있는 소재주
계약금액·고객명 없는 ESS 계약 과대해석
전고체·폐배터리 테마만 있는 기업
태양광 보조금·관세 의존 기업
풍력 project economics가 약한 기업
리튬 가격 반등만 보는 광물주
EV·BESS 화재와 인증·보험·주차장 규제 overlay가 붙은 기업
```

---

## 2. 대상 canonical archetype

| canonical archetype                      | Loop 4 정책                                         |
| ---------------------------------------- | ------------------------------------------------- |
| `BATTERY_MATERIALS_CAPEX_OVERHEAT`       | Watch/Red. EV 수요·CAPA·계약취소·광물가격 감점 강화             |
| `BATTERY_EQUIPMENT_PARTS`                | Watch-to-Green. 고객사 CAPEX와 실제 납품·마진 필요            |
| `ESS_LFP_GRID_STORAGE`                   | Green 후보. 계약금액·계약기간·고객·GWh·OPM 필요                 |
| `ESS_AI_DATA_CENTER_STORAGE`             | Watch-to-Green. 데이터센터 전력수요와 실제 storage 계약 필요      |
| `EV_TO_ESS_CAPACITY_REDEPLOYMENT`        | Watch. EV 라인 전환은 좋지만 idle plant·전환비용·계약 확인 필요     |
| `BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE` | RedTeam overlay. 고객명·계약금액·용도 미공개 시 score cap      |
| `BATTERY_RECYCLING_ESS_SHIFT`            | Watch-to-Green. 회수량·금속 회수·ESS/grid 고객 필요          |
| `BATTERY_SOH_SECOND_LIFE_TRANSPARENCY`   | RedTeam overlay. SOH·battery passport·잔존가치 검증     |
| `EV_INFRASTRUCTURE`                      | Watch. 충전소 이용률·수익성·화재규제 확인                        |
| `EV_FIRE_BESS_SAFETY_OVERLAY`            | RedTeam gate. EV·ESS 화재, 인증, 보험, 주차장·시설 규제        |
| `HYDROGEN_FUEL_CELL_INFRA`               | Watch-to-Green. 실제 CAPEX·고객·가동률 필요                |
| `SOLAR_TARIFF_SUPPLYCHAIN`               | Watch/Red. 보조금·관세·통관·UFLPA 리스크 큼                  |
| `RENEWABLE_ENERGY_PROJECT_ECONOMICS`     | Watch/Red. 풍력은 원가·금리·인허가·impairment 4C 가능         |
| `WASTE_RECYCLING_ENVIRONMENT`            | Green 가능. 허가권·처리량·반복 FCF 필요                       |
| `CARBON_CREDIT_CBAM_COMPLIANCE`          | Watch. 탄소가격보다 탄소회계·검증·비용전가 매출 필요                  |
| `DATA_CENTER_WATER_REUSE_INFRA`          | Watch-to-Green. 데이터센터 물 재활용·냉각 계약 필요              |
| `LITHIUM_ESS_DEMAND_CYCLE`               | Cycle/Watch. ESS 수요가 붙어도 공급·광산 재가동·sodium-ion 리스크 |
| `SPECULATIVE_BATTERY_TECH`               | Watch/Red. 전고체·신소재는 상용화·고객·양산 전 Green 금지          |

---

## 3. deep sub-archetype

```text
BATTERY_MATERIALS_CAPEX_OVERHEAT
- 양극재
- 음극재
- 전해액
- 분리막
- 리튬
- 니켈
- 흑연
- CAPA 증설
- 고객사 EV 계획
- EV 공장 idle
- 계약 취소
- 판가/원가 spread

ESS_LFP_GRID_STORAGE
- LFP ESS
- grid-scale ESS
- Tesla Megapack류
- 북미 ESS 생산
- 계약금액
- 계약기간
- 고객사
- GWh
- ESS OPM
- LFP 원가경쟁

ESS_AI_DATA_CENTER_STORAGE
- AI 데이터센터 전력수요
- backup/storage
- grid balancing
- utility-scale battery
- Ford Energy
- Redwood Energy
- data center storage customer
- battery deployment GWh
- gross margin target

EV_TO_ESS_CAPACITY_REDEPLOYMENT
- EV line idle
- EV line → ESS line 전환
- Ultium Tennessee ESS
- SK On Georgia line conversion
- Ford Energy
- LFP licensing
- EV demand overhang
- 전환비용
- 가동률

BATTERY_RECYCLING_ESS_SHIFT
- 폐배터리
- black mass
- pCAM
- 금속 회수
- 회수율
- 회수량
- Redwood Materials
- Volkswagen / Panasonic / Toyota / Lyft partnerships
- ESS/grid services
- data center power

BATTERY_SOH_SECOND_LIFE_TRANSPARENCY
- BMS SOH
- battery passport
- second-life grading
- residual capacity
- warranty enforcement
- used EV valuation
- SOH validation cost
- battery pack information asymmetry

EV_INFRASTRUCTURE
- 초급속 충전
- 충전기
- 충전소 이용률
- 결제/운영수익
- 과충전 방지
- 지하주차장 규제
- charger liability insurance

EV_FIRE_BESS_SAFETY_OVERLAY
- EV fire
- BESS fire
- battery certification
- battery supplier disclosure
- thermal runaway
- sprinkler retrofit
- insurance cost
- safety regulation
- recall

HYDROGEN_FUEL_CELL_INFRA
- 수소연료전지
- 전해조
- 상용차
- 버스
- 건설기계
- 선박
- 수소충전소
- 공장 착공
- 고객사
- 가동률

SOLAR_TARIFF_SUPPLYCHAIN
- 태양광 모듈
- 태양광 셀
- 미국 공장
- 중국 공급망
- UFLPA
- customs detention
- FEOC
- 보조금
- 관세

RENEWABLE_ENERGY_PROJECT_ECONOMICS
- 풍력
- 해상풍력
- monopile foundation
- PPA
- financing cost
- project delay
- impairment
- 인허가
- grid interconnection

WASTE_RECYCLING_ENVIRONMENT
- 폐기물처리
- 플라스틱 재활용
- 폐기물 에너지화
- 허가권
- 처리량
- 반복 FCF
- M&A platform
- 수도권 catchment area
```

---

# 4. 성공사례 / 구조 후보

## 4-1. LGES 43억 달러 LFP 계약 — `ESS_LFP_GRID_STORAGE` 후보지만 disclosure cap 필요

LG에너지솔루션은 2025년 7월 LFP 배터리 43억 달러 공급계약을 발표했다. 계약기간은 2027년 8월부터 2030년 7월까지 3년이고, 최대 7년 연장 및 공급량 확대 옵션이 포함되어 있다. 다만 Reuters 기준으로 고객사는 공개되지 않았고, EV용인지 ESS용인지도 회사가 명시하지 않았다. 이전 라운드에서 “Tesla ESS용”으로 시장 해석을 붙였지만, Loop 4에서는 **공시·Reuters 기준으로는 customer/use-case undisclosed**로 처리해야 한다. ([Reuters][1])

```text
가격경로 1차 판정:
ESS_OR_LFP_CONTRACT_STAGE2_CANDIDATE_WITH_DISCLOSURE_CAP

좋은 점:
- 계약금액 $4.3B
- 계약기간 2027.08~2030.07
- 최대 7년 연장 옵션
- LFP 배터리 장기계약
- 북미 ESS/EV 양쪽 가능성

주의:
- 고객명 미공개
- ESS용인지 EV용인지 미공개
- OPM 미확인
- 고객사 concentration 확인 불가
- FEOC/관세/IRA 리스크
```

**Loop 4 교정**

```text
BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE overlay 추가.

계약금액은 확인됨:
+ Visibility 점수 가점

고객명·용도 미공개:
- Stage 3-Green score cap
- customer_confidential_flag = true
- use_case_unknown_flag = true

Stage 3 조건:
실제 매출 인식
+ ESS/EV 용도 확인
+ margin/OPM
+ 고객 다변화
```

---

## 4-2. SK On–Flatiron ESS 공급계약 — `ESS_LFP_GRID_STORAGE`

SK On은 미국 Flatiron Energy Development에 ESS용 LFP 배터리를 최대 7.2GWh 공급하기로 했다. 공급기간은 2026~2030년이고, SK On은 2026년 하반기부터 ESS 전용 LFP 배터리 양산을 시작하며 일부 미국 EV 라인을 ESS 제조용으로 전환할 계획이라고 밝혔다. 다만 계약금액은 공개되지 않았다. ([Reuters][2])

```text
가격경로 1차 판정:
ESS_CONTRACT_STAGE2_CANDIDATE_WITH_VALUE_CAP

좋은 점:
- 최대 7.2GWh
- 공급기간 2026~2030년
- ESS 전용 LFP 양산 계획
- EV 라인 일부 ESS 전환
- 미국 ESS 수요에 직접 노출

주의:
- 계약금액 미공개
- ESS OPM 미확인
- 고객사 수요 지속성 확인 필요
- EV 라인 전환 비용
```

**Loop 4 교정**

```text
contract_value_missing = true이면 EPS/FCF 점수 상한을 둔다.

GWh와 기간은 Stage 2 근거.
하지만 Stage 3-Green은 매출·마진·FCF 확인 전까지 제한.
```

---

## 4-3. GM–LG Ultium Ohio idle / Tennessee ESS 전환 — `EV_TO_ESS_CAPACITY_REDEPLOYMENT`

GM과 LG에너지솔루션의 Ultium Cells는 Ohio EV 배터리 공장을 2026년 1월부터 멈췄고, 850명가량 근로자의 복귀 일정도 불확실했다. Reuters는 EV 수요 둔화와 2025년 9월 미국 EV 세액공제 종료가 배경이라고 설명했다. 동시에 Tennessee 공장에서는 EV 대신 ESS용 배터리 셀 생산을 위해 근로자들이 복귀했다. 즉 이 케이스는 **EV CAPA thesis 4C + ESS 전환 Watch**가 동시에 붙는 복합 사례다. ([Reuters][3])

```text
가격경로 1차 판정:
EV_CAPA_THESIS_4C + ESS_SHIFT_WATCH

좋은 점:
- Tennessee에서 ESS 전환 시도
- EV 라인을 ESS로 돌릴 수 있는 유연성
- grid storage demand 대응 가능성

주의:
- Ohio 공장 idle
- EV 수요 둔화
- 세액공제 종료 영향
- 근로자 layoff/furlough
- 가동률·고정비 부담
```

**Loop 4 교정**

```text
EV CAPA는 더 이상 자동 가점이 아니다.

plant_idle_flag = true
layoff_furlough_flag = true
capacity_utilization_low = true

이면 BATTERY_MATERIALS_CAPEX_OVERHEAT에서 강한 감점.

ESS conversion이 있더라도:
ESS 고객계약
ESS 가동률
ESS OPM
이 없으면 Stage 3 금지.
```

---

## 4-4. Ford Energy — EV 실패 이후 ESS·AI 데이터센터 저장장치로 전환하는 후보

Ford는 EV 사업 부진 이후 Ford Energy를 출범시키며, 데이터센터·유틸리티·대형 상업고객용 배터리 저장장치 사업을 추진하고 있다. FT 보도 기준 Ford 주가는 Ford Energy 발표 후 이틀간 20% 넘게 올랐고, 사업은 CATL 라이선스 기반 LFP 기술을 활용해 2027년 말부터 연 20GWh 이상 배치를 목표로 한다. 다만 Ford는 2025년에 EV 관련 약 195억 달러 write-down을 겪었고, Ford Energy가 EV 손실을 얼마나 상쇄할지는 execution risk가 남아 있다. ([Financial Times][4])

```text
가격경로 1차 판정:
EV_TO_ESS_REDEPLOYMENT_EVENT_PREMIUM + EXECUTION_WATCH

좋은 점:
- AI 데이터센터 전력수요와 ESS 수요에 직접 노출
- LFP 기반 저장장치 전략
- EV CAPA overhang의 재활용 가능성
- 발표 후 강한 주가반응

주의:
- EV write-down 이후 전환 narrative
- CATL 라이선스 정치·안보 리스크
- 실제 고객계약·마진 미확인
- Tesla ESS와의 경쟁
- 2027년 말 이후 execution timeline
```

**Loop 4 교정**

```text
ESS_AI_DATA_CENTER_STORAGE와 EV_TO_ESS_CAPACITY_REDEPLOYMENT를 분리한다.

좋은 ESS 전환:
계약
+ 고객
+ GWh
+ margin
+ 가동률

나쁜 ESS 전환:
EV 실패를 덮는 narrative
+ 고객 미확인
+ CAPEX 부담
+ 정치/FEOC 리스크
```

---

## 4-5. Redwood Materials — `BATTERY_RECYCLING_ESS_SHIFT`

Redwood Materials는 폐배터리·금속 회수·ESS가 결합되는 좋은 구조 reference다. Redwood는 Eclipse Ventures가 주도하고 Nvidia의 NVentures가 참여한 라운드에서 3.5억 달러를 조달했다. 회사는 리튬, 코발트, 니켈, 구리 같은 핵심 소재를 회수하고, grid services와 데이터센터용 energy storage systems도 제공한다. Volkswagen, Panasonic, Toyota, Lyft 등과의 파트너십도 보도됐다. ([Reuters][5])

```text
가격경로 1차 판정:
RECYCLING_PLUS_STORAGE_STRUCTURAL_REFERENCE

좋은 점:
- 금속 회수
- ESS/grid services
- 데이터센터 전력수요와 연결
- 대형 파트너십
- Nvidia/AI 인프라 자금 관심

주의:
- 비상장 reference
- 실제 매출·마진·회수량 상장사 매핑 필요
- 금속가격 변동
- CAPEX와 scaling risk
```

**Loop 4 교정**

```text
폐배터리 단독:
Watch

폐배터리 + 회수량 + 회수금속 매출 + 고객계약:
Watch-to-Green

폐배터리 + ESS + 데이터센터/grid 고객:
Stage 2~3 후보 가능

단:
상장사 매핑 시 direct_exposure_flag 필요.
```

---

## 4-6. EQT–KJ Environment — `WASTE_RECYCLING_ENVIRONMENT`

EQT는 한국 KJ Environment와 계열사를 인수해 플라스틱 재활용, 재활용 폐기물 선별, 폐기물 에너지화까지 포함하는 폐기물처리 플랫폼을 만들기로 했다. 플랫폼 기업가치는 1조 원 이상으로 알려졌고, 수도권을 중심으로 한국 인구 절반 이상을 커버하는 입지를 가진 것으로 보도됐다. ([Reuters][6])

```text
가격경로 1차 판정:
WASTE_PLATFORM_STRUCTURAL_REFERENCE

좋은 점:
- 허가권·처리시설 기반
- 수도권 catchment area
- 반복 처리량
- 플라스틱 재활용·waste-to-energy
- 인프라 투자자 관심

주의:
- 상장사 직접 매핑 필요
- 처리량·가동률·FCF 확인 필요
- CAPEX와 규제비용
```

**Loop 4 교정**

```text
WASTE_RECYCLING_ENVIRONMENT는 R3에서 드문 Green 가능 축으로 유지.

조건:
허가권
처리량
장기 고객
반복 FCF
가동률
규제 강화 수혜
```

---

## 4-7. 현대차 울산 수소연료전지 공장 — `HYDROGEN_FUEL_CELL_INFRA`

현대차는 울산에 9,300억 원, 약 6.54억 달러 규모 수소연료전지 생산시설을 착공했다. 2027년 완공 예정이며, 승용차, 상용 트럭·버스, 건설기계, 선박용 연료전지와 전해조를 생산할 계획이다. ([Reuters][7])

```text
가격경로 1차 판정:
HYDROGEN_CAPEX_STAGE1_TO_STAGE2_CANDIDATE

좋은 점:
- 실제 CAPEX
- 완공 예정일
- 연료전지·전해조 생산
- 상용차·선박·건설기계 응용 가능
- 내연기관 부지 전환 상징성

주의:
- 고객계약 미확인
- 가동률 미확인
- 수소차 인프라 부족
- 보조금 의존
- OPM/FCF 전환 전 Green 금지
```

**Loop 4 교정**

```text
HYDROGEN_FUEL_CELL_INFRA:
정책 뉴스만 있으면 Watch.
공장 착공은 Stage 1.5~2.
고객·가동률·매출·OPM 전까지 Stage 3-Green 금지.
```

---

# 5. 반례 / RedTeam

## 5-1. Ford–LGES 65억 달러 EV 배터리 계약 취소 — `BATTERY_MATERIALS_CAPEX_OVERHEAT`

Ford는 LG에너지솔루션과의 약 65억 달러 EV 배터리 공급계약을 취소했다. 이 계약은 2024년에 체결됐고 2026~2027년 Ford 유럽 사업에 배터리를 공급할 예정이었지만, EV 수요 둔화와 정책 변화 속에서 취소됐다. Ford는 EV 모델 중단과 약 195억 달러 write-down도 발표했다. ([Reuters][8])

```text
가격경로 1차 판정:
EV_BATTERY_CONTRACT_CANCELLATION_HARD_4C

교훈:
장기 EV 배터리 계약
≠ 무조건 Green

4C 조건:
- contract_cancelled_flag
- automaker_EV_cutback_flag
- EV_model_discontinued
- capacity_underutilization
- EV_policy_change
```

**Loop 4 교정**

```text
BATTERY_MATERIALS_CAPEX_OVERHEAT:
장기공급계약이 있어도 고객사 EV 전략이 바뀌면 4C.

계약 점수 강화 조건:
취소불가 조항
고객사 생산계획 유지
보조금·관세 리스크 낮음
라인 가동률 확인
OPM/FCF 확인
```

---

## 5-2. Qcells 통관·UFLPA 리스크 — `SOLAR_TARIFF_SUPPLYCHAIN`

Qcells는 미국 조지아 태양광 공장에서 약 1,000명 근로자에 대해 furlough를 실시했다. 해외 부품 선적이 미국 세관에서 지연됐고, 중국 신장 관련 강제노동방지법, 즉 UFLPA 집행 때문에 핵심 부품이 억류되면서 생산차질이 발생했다. Qcells는 미국 내 공급망 구축 투자를 계속하겠다고 했지만, 이 사례는 미국 제조·보조금 narrative가 통관·관세·공급망 리스크에 바로 흔들릴 수 있음을 보여준다. ([Reuters][9])

```text
가격경로 1차 판정:
SOLAR_SUPPLYCHAIN_HARD_4C

교훈:
미국 태양광 제조
≠ 자동 Green

4C 조건:
- customs_detention_flag
- UFLPA_flag
- component_delay_flag
- furlough_layoff_flag
- supply_chain_transparency_risk
```

**Loop 4 교정**

```text
SOLAR_TARIFF_SUPPLYCHAIN:
Stage 3-Green 매우 제한.
미국 공장·보조금보다 부품 공급망, 통관, UFLPA, FEOC를 먼저 본다.
```

---

## 5-3. Ørsted Sunrise Wind impairment — `RENEWABLE_ENERGY_PROJECT_ECONOMICS`

Ørsted는 Sunrise Wind 프로젝트 지연과 비용 상승, 미국 financing cost 증가로 약 17억 달러 impairment를 발표했다. 프로젝트는 2027년 하반기로 지연됐고, monopile foundation 비용 증가가 주요 원인으로 언급됐다. ([Reuters][10])

```text
가격경로 1차 판정:
OFFSHORE_WIND_PROJECT_4C

교훈:
해상풍력 정책·PPA
≠ Green

4C 조건:
- cost_overrun
- project_delay
- financing_cost_increase
- foundation_cost_increase
- impairment
```

**Loop 4 교정**

```text
RENEWABLE_ENERGY_PROJECT_ECONOMICS:
정책·PPA만으로 Green 금지.
project economics, financing cost, foundation cost, grid connection을 반드시 확인.
```

---

## 5-4. 리튬 가격 86% 급락과 공급 재가동 리스크 — `LITHIUM_ESS_DEMAND_CYCLE`

리튬 가격은 2022년 11월 고점 이후 약 86% 급락했고, 전 세계 광산 폐쇄를 유발했다. 2025년에 일부 안정 기대가 있었지만, 가격이 오르면 폐쇄 광산이 다시 재가동될 수 있어 상승폭을 제한할 수 있다는 분석도 있었다. ([Reuters][11])

```text
가격경로 1차 판정:
LITHIUM_CYCLE_HARD_COUNTEREXAMPLE

교훈:
리튬 가격 반등
≠ 구조적 Green

4C 조건:
- lithium_price_crash
- mine_shutdown
- mine_restart_supply_rebound
- EV_demand_slowdown
- CAPEX_cut
```

2026년에는 ESS 수요가 리튬 outlook을 개선했다. 중국 전력시장 개혁과 글로벌 데이터센터 건설 붐이 ESS용 리튬 수요를 키웠고, Reuters는 2026년 energy storage 수요가 55% 성장할 수 있다고 보도했다. 하지만 sodium-ion 전환, EV 세제혜택 종료, 공급 증가가 가격 상승을 제한할 수 있다는 리스크도 함께 제시됐다. ([Reuters][12])

**Loop 4 교정**

```text
LITHIUM_ESS_DEMAND_CYCLE:
ESS 수요 증가는 Stage 1~2 보조근거.

Stage 3 조건:
저비용 구조
장기 offtake
FCF 방어
CAPEX 절제
supply response에도 가격 방어

단:
광산 재가동
sodium-ion 대체
EV 수요 둔화
공급 증가

가 있으면 Green 제한.
```

---

## 5-5. EV 화재·배터리 인증 — `EV_FIRE_BESS_SAFETY_OVERLAY`

한국 정부와 여당은 EV 화재 우려가 커진 뒤 배터리 인증제 시행을 앞당기고, 자동차 회사가 EV에 들어가는 배터리 정보를 공개하도록 하는 방안을 추진했다. 2024년 8월 Mercedes-Benz EV 화재가 지하주차장에서 발생해 수백 대 차량을 파손시키고 주민 대피를 불렀으며, 이후 지하주차장 스프링클러와 과충전 방지 충전기 확대 같은 안전대책도 논의됐다. ([Reuters][13])

```text
가격경로 1차 판정:
EV_FIRE_REGULATORY_OVERLAY

의미:
EV 화재는 단순 뉴스가 아니라
배터리 제조사 공개, 인증, 충전 규제, 보험비용, 수요심리에 영향을 주는 RedTeam이다.

감점 조건:
- battery_certification_flag
- battery_supplier_disclosure_flag
- fire_event_flag
- parking_charging_regulation_flag
- insurance_cost_change
```

ESS도 별도 안전 overlay가 필요하다. California Moss Landing의 대형 battery storage facility 화재는 energy storage boom 속에서 주민 대피와 highway closure까지 유발했고, 대형 BESS가 지역 안전·허가 리스크를 가진다는 점을 보여줬다. ([AP News][14])

**Loop 4 교정**

```text
EV_FIRE_BESS_SAFETY_OVERLAY를 gate로 둔다.

EV:
배터리 인증·제조사 공개·지하주차장 규제.

BESS:
시설화재·지역반발·보험·허가·소방설비.

안전규제는 ESS demand를 없애지는 않지만,
CAPEX, permitting, insurance, site selection을 바꾼다.
```

---

## 5-6. Battery SOH 투명성 — `BATTERY_SOH_SECOND_LIFE_TRANSPARENCY`

2026년 arXiv 연구는 1,114대 EV와 5개 제조사를 대상으로 차량 내 BMS가 보고하는 battery state-of-health가 실제 capacity 차이를 충분히 반영하지 못한다고 분석했다. 모델별 실제 capacity 차이가 12~25% 존재했지만, BMS SOH와의 상관관계는 약하거나 일부 차량은 SOH 자체를 제공하지 않았다. 이건 중고 EV valuation, warranty, second-life battery, 폐배터리 회수품질 평가에 중요한 정보 비대칭 리스크다. ([arXiv][15])

```text
가격경로 1차 판정:
BATTERY_HEALTH_TRANSPARENCY_REDTEAM

의미:
폐배터리·second-life ESS는 회수량만으로 부족하다.
실제 잔존용량, SOH 신뢰도, 인증·검증 비용을 봐야 한다.
```

**Loop 4 교정**

```text
BATTERY_RECYCLING_ESS_SHIFT:
회수량 + 회수금속 매출만으로 부족.

추가 필수:
SOH validation
battery passport
second-life grading cost
warranty enforcement risk
residual capacity uncertainty
```

---

# 6. 4B-watch 사례

## 6-1. ESS 전환 4B-watch

```text
4B 조건:
- EV 둔화에도 ESS 전환 narrative로 배터리주 동반 상승
- 실제 계약금액·계약기간·ESS OPM 확인 전 가격이 먼저 감
- LFP ESS 경쟁과 보조금 의존을 시장이 무시
- EV 공장 idle을 ESS 전환으로 과도하게 덮음
```

LGES 43억 달러 LFP 계약과 SK On–Flatiron 계약은 Stage 2 후보지만, LGES 계약은 고객명·용도 미공개이고, SK On 계약은 계약금액이 공개되지 않았다. 따라서 ESS contract score는 올리되, disclosure confidence cap을 같이 붙여야 한다. ([Reuters][1])

---

## 6-2. EV→ESS capacity redeployment 4B-watch

```text
4B 조건:
- EV 공장 idle을 ESS 전환으로 긍정만 해석
- 전환비용·가동률·고객계약·마진이 미확인
- EV write-down을 ESS growth가 즉시 상쇄한다고 가정
```

GM–LG Ultium은 Ohio 공장 idle과 Tennessee ESS 전환이 동시에 존재하고, Ford Energy는 EV write-down 이후 ESS·AI 데이터센터 storage로 방향을 돌린 사례다. 둘 다 후보지만, “전환 narrative”를 “수익화”로 오분류하면 안 된다. ([Reuters][3])

---

## 6-3. 폐배터리·재활용 4B-watch

```text
4B 조건:
- battery recycling과 critical minerals narrative가 과밀
- 회수량·금속 회수율·마진 없이 valuation 상승
- AI 데이터센터 ESS와 연결한다는 말만 있고 실제 매출화 없음
- second-life battery SOH 검증비용을 무시
```

Redwood는 좋은 reference지만, 한국 상장사로 매핑하려면 회수량, 회수소재 매출, 고객계약, SOH 검증, FCF를 따로 확인해야 한다. ([Reuters][5])

---

## 6-4. 수소 CAPEX 4B-watch

```text
4B 조건:
- 수소 공장 착공 뉴스만으로 관련주 동반 급등
- 고객·가동률·OPM 전환 전 가격이 먼저 감
- 보조금·수소충전소 부족 리스크를 무시
```

현대차 울산 수소연료전지 공장은 실제 CAPEX라는 점에서 Stage 1.5~2 후보지만, 2027년 완공 후 고객·가동률·매출이 확인되기 전까지 Stage 3-Green은 제한된다. ([Reuters][7])

---

## 6-5. 태양광 미국 제조 4B-watch

```text
4B 조건:
- 미국 제조·보조금 narrative로 관련주 상승
- 부품 공급망과 통관 리스크를 시장이 무시
- 중국 공급망 배제를 생산차질로 연결하지 않음
```

Qcells 사례는 미국 제조 투자와 보조금 narrative가 있어도, 통관·UFLPA·부품 지연 하나로 생산이 차질을 받을 수 있음을 보여준다. ([Reuters][9])

---

## 6-6. 풍력 PPA·정책 4B-watch

```text
4B 조건:
- PPA·정책·탈탄소 수요로 관련주 급등
- foundation cost, financing cost, project delay를 무시
- impairment 가능성을 낮게 봄
```

Ørsted의 Sunrise Wind impairment는 해상풍력 프로젝트가 정책 수혜에도 불구하고 비용·금리·일정 지연으로 4C로 갈 수 있음을 보여준다. ([Reuters][10])

---

## 6-7. 리튬 반등 4B-watch

```text
4B 조건:
- 리튬 가격 반등으로 광물주 동반 급등
- 광산 재가동과 공급반응을 무시
- ESS 수요 증가를 곧장 구조적 shortage로 오판
- sodium-ion 대체 가능성 무시
```

리튬은 ESS 수요가 새 회복축이 될 수 있지만, 광산 재가동과 공급반응이 빠르면 구조적 Green이 아니라 cycle에 머문다. ([Reuters][11])

---

# 7. 4C-thesis-break 사례

## 7-1. EV 배터리 공장 idle / 계약 취소

```text
4C:
EV_demand_slowdown
plant_idle
layoff
contract_cancellation
capacity_underutilization
automaker_EV_cutback
```

Ultium Ohio 공장 재가동 불확실성과 Ford–LGES 65억 달러 계약 취소는 EV 배터리 CAPA thesis의 대표 4C다. ([Reuters][3])

---

## 7-2. 태양광 통관·관세·부품 억류

```text
4C:
customs_detention
UFLPA_risk
tariff_risk
production_disruption
worker_furlough
contractor_layoff
```

Qcells의 1,000명 furlough와 300명 계약직 감축은 `SOLAR_TARIFF_SUPPLYCHAIN`의 hard 4C다. ([Reuters][9])

---

## 7-3. 풍력 impairment

```text
4C:
cost_overrun
project_delay
financing_cost_increase
foundation_cost
impairment
```

Ørsted의 17억 달러 impairment는 재생에너지 프로젝트가 financing과 원가를 통과하지 못하면 Green이 아니라 thesis break가 된다는 기준이다. ([Reuters][10])

---

## 7-4. 리튬 가격 급락·공급 재가동

```text
4C:
lithium_price_crash
mine_shutdown
mine_restart_supply_rebound
CAPEX_cut
EV_demand_slowdown
sodium_ion_substitution
```

리튬 가격이 반등해도 광산 재가동과 공급반응이 빠르면 구조적 Green이 아니라 `cyclical_success_or_failure`가 된다. ([Reuters][11])

---

## 7-5. EV·ESS 안전규제

```text
4C-watch:
battery_fire
BESS_fire
certification_requirement
battery_supplier_disclosure
insurance_cost
underground_parking_regulation
facility_permitting_delay
recall_risk
```

한국의 EV 배터리 인증제 조기 시행과 배터리 제조사 공개 요구, California 대형 BESS 화재는 EV·ESS 관련주에 안전·인증·보험·시설 인허가 overlay를 붙여야 한다는 기준이다. ([Reuters][13])

---

## 7-6. Second-life battery / SOH 정보비대칭

```text
4C-watch:
SOH_unreliable
residual_capacity_uncertainty
second_life_grading_cost
warranty_enforcement_risk
battery_passport_compliance
```

SOH 신뢰도가 약하면 폐배터리·second-life ESS의 잔존가치와 회수 마진을 과대평가할 수 있다. ([arXiv][15])

---

# 8. 점수비중 보정표 — R3 Loop 4 / v4.0

| canonical archetype                      | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | Loop 4 핵심 감점                              |
| ---------------------------------------- | ------: | ---------: | ---------: | ---------: | --------: | ------: | ---: | ----------------------------------------- |
| `BATTERY_MATERIALS_CAPEX_OVERHEAT`       |      16 |         11 |         12 |          8 |         7 |       0 |    5 | EV 둔화, CAPA 과잉, 계약취소, 광물가격                |
| `BATTERY_EQUIPMENT_PARTS`                |      19 |         16 |         11 |         11 |         9 |       0 |    5 | 고객사 CAPEX cut, 납품 지연, EV line idle        |
| `ESS_LFP_GRID_STORAGE`                   |      22 |         21 |         15 |         12 |        11 |       0 |    5 | ESS 마진, LFP 경쟁, 고객집중, 보조금                 |
| `ESS_AI_DATA_CENTER_STORAGE`             |      22 |         20 |         16 |         13 |        11 |       0 |    5 | 고객계약 미확인, 데이터센터 CAPEX 지연, 안전규제            |
| `EV_TO_ESS_CAPACITY_REDEPLOYMENT`        |      18 |         17 |         13 |         12 |         9 |       0 |    5 | EV idle overhang, 전환비용, 계약·마진 미확인         |
| `BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE` |    gate |       gate |       gate |       gate |      gate |    gate | gate | 고객명·계약금액·용도 미공개 시 score cap               |
| `BATTERY_RECYCLING_ESS_SHIFT`            |      20 |         18 |         14 |         11 |        10 |       0 |    5 | 회수량 부족, SOH 검증, 금속가격, 계약금액 미공개            |
| `BATTERY_SOH_SECOND_LIFE_TRANSPARENCY`   |    gate |       gate |       gate |       gate |      gate |    gate | gate | SOH 신뢰도, second-life 검증, battery passport |
| `EV_INFRASTRUCTURE`                      |      16 |         13 |          7 |         10 |         8 |       0 |    5 | 이용률 부족, 화재규제, 충전 제한, 보조금 의존               |
| `EV_FIRE_BESS_SAFETY_OVERLAY`            |    gate |       gate |       gate |       gate |      gate |    gate | gate | EV/BESS 화재, 인증, 리콜, 보험, 시설 규제             |
| `HYDROGEN_FUEL_CELL_INFRA`               |      18 |         18 |         12 |         12 |        10 |       0 |    5 | 고객 부재, 가동률, 보조금, 인프라 부족                   |
| `SOLAR_TARIFF_SUPPLYCHAIN`               |      15 |         12 |         11 |          9 |         7 |       0 |    5 | 통관, 관세, UFLPA, FEOC, 공급망 차질               |
| `RENEWABLE_ENERGY_PROJECT_ECONOMICS`     |      15 |         12 |          9 |          9 |         7 |       0 |    5 | 금리, 원가, 인허가, impairment                   |
| `WASTE_RECYCLING_ENVIRONMENT`            |      18 |         22 |         15 |         13 |        12 |       3 |    5 | 가동률, CAPEX, 금속가격, 규제비용                    |
| `CARBON_CREDIT_CBAM_COMPLIANCE`          |      14 |         17 |         10 |         12 |         8 |       2 |    6 | 제도개편, 가격변동, greenwashing                  |
| `DATA_CENTER_WATER_REUSE_INFRA`          |      16 |         18 |         14 |         12 |        10 |       2 |    5 | 고객 부재, 지역반발, 경제성                          |
| `LITHIUM_ESS_DEMAND_CYCLE`               |   cycle |      cycle |      cycle |      cycle |     cycle |   cycle |    5 | 가격 급락, 광산 재가동, sodium-ion, EV 둔화          |
| `SPECULATIVE_BATTERY_TECH`               |       6 |          5 |          6 |          8 |         5 |       0 |    4 | 상용화 전, 고객 부재, 양산 전                        |

Loop 4에서 핵심 보정은 이거다.

```text
1. ESS_AI_DATA_CENTER_STORAGE를 ESS_LFP_GRID_STORAGE에서 분리.
   AI 데이터센터 storage는 수요가 강하지만 고객계약·마진·안전규제가 별도다.

2. EV_TO_ESS_CAPACITY_REDEPLOYMENT를 추가.
   EV 라인 idle과 ESS 전환은 동시에 존재하므로, 무조건 Green이 아니다.

3. BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE를 gate로 추가.
   고객명·계약금액·용도가 미공개면 Stage 3-Green을 제한한다.

4. BATTERY_SOH_SECOND_LIFE_TRANSPARENCY를 gate로 추가.
   폐배터리·second-life는 SOH와 battery passport 없이는 잔존가치가 불투명하다.

5. EV_FIRE_BESS_SAFETY_OVERLAY를 EV와 ESS 모두에 적용.
   화재·인증·보험·시설 인허가가 demand를 비용과 시간으로 바꾼다.

6. SOLAR_TARIFF_SUPPLYCHAIN과 RENEWABLE_ENERGY_PROJECT_ECONOMICS는 더 보수적으로.
   Qcells 통관과 Ørsted impairment가 hard 4C다.

7. WASTE_RECYCLING_ENVIRONMENT는 Green 가능 유지.
   허가권·처리량·반복 FCF가 있는 인프라형 사업이기 때문.
```

---

# 9. stage date 후보

## `BATTERY_MATERIALS_CAPEX_OVERHEAT`

```text
Stage 1:
EV 성장, 장기공급계약, CAPA 증설 뉴스

Stage 2:
실제 계약, 판가·마진 개선, OP/EPS 상향 확인일

Stage 3:
장기계약 + 가격전가 + FCF 훼손 없는 CAPEX가 확인된 경우만

Stage 4B:
PER/PBR 과열, CAPA 경쟁, 목표가 과밀 상향

Stage 4C:
EV 수요 둔화, 광물가격 하락, CAPA 과잉, 고객사 계약 취소, 공장 idle
```

## `ESS_LFP_GRID_STORAGE`

```text
Stage 1:
ESS 전환, LFP ESS 생산, 북미 ESS 수요 뉴스

Stage 2:
ESS 고객계약, 계약금액, 계약기간, GWh, 생산공장 확인

Stage 3:
ESS 매출 성장 + ESS OPM + FCF 전환 + 고객 다변화 확인

Stage 4B:
ESS narrative 과열, LFP ESS 관련주 동반 상승

Stage 4C:
ESS 마진 부진, LFP 경쟁 심화, 고객사 수요 둔화, 보조금/관세 훼손
```

## `ESS_AI_DATA_CENTER_STORAGE`

```text
Stage 1:
AI 데이터센터 전력수요와 storage demand 뉴스

Stage 2:
데이터센터·유틸리티 고객계약, deployment GWh, margin signal 확인

Stage 3:
반복 storage 매출 + OPM/FCF + 고객 다변화 확인

Stage 4B:
AI power storage narrative 과열

Stage 4C:
데이터센터 project delay, 안전규제, 고객계약 지연, LFP 경쟁 심화
```

## `EV_TO_ESS_CAPACITY_REDEPLOYMENT`

```text
Stage 1:
EV 공장 idle, EV 라인 ESS 전환 발표

Stage 2:
ESS 생산라인 전환 완료, 고객계약, GWh, 가동률 확인

Stage 3:
EV idle 고정비를 ESS 매출·OPM으로 상쇄하는 시점

Stage 4B:
EV 실패를 ESS 전환으로 과잉 미화하는 narrative 과열

Stage 4C:
전환비용 증가, ESS 계약 부재, 가동률 낮음, EV write-down 지속
```

## `BATTERY_RECYCLING_ESS_SHIFT`

```text
Stage 1:
폐배터리, second-life battery, black mass, 재활용 정책 뉴스

Stage 2:
회수량, 회수금속 매출, 고객계약, ESS 활용 확인

Stage 3:
재활용/second-life 매출이 반복 FCF로 이어질 때만

Stage 4B:
recycling premium 과열, critical minerals narrative 과밀

Stage 4C:
회수량 부족, SOH 검증 실패, 금속가격 하락, second-life 수익성 부진
```

## `HYDROGEN_FUEL_CELL_INFRA`

```text
Stage 1:
수소 공장 착공, 정책, 설비투자 뉴스

Stage 2:
고객사·수요처·생산능력·납품계약 확인

Stage 3:
가동률과 OP/EPS 전환 확인

Stage 4B:
수소 테마 동반 과열

Stage 4C:
보조금 축소, 고객 부재, 가동률 낮음, 프로젝트 지연
```

## `SOLAR_TARIFF_SUPPLYCHAIN`

```text
Stage 1:
미국 공장, 보조금, 태양광 수요 뉴스

Stage 2:
가동률, 고객사, 부품 공급 안정, OP 전환 확인

Stage 3:
보조금 없이도 FCF가 나올 때만

Stage 4B:
미국 태양광 제조 narrative 과열

Stage 4C:
관세, 통관, UFLPA 억류, 보조금 축소, worker furlough
```

## `RENEWABLE_ENERGY_PROJECT_ECONOMICS`

```text
Stage 1:
풍력·재생에너지 정책, PPA, 프로젝트 뉴스

Stage 2:
인허가, financing, 공사 착수, 비용 확정, 매출 인식 확인

Stage 3:
프로젝트 경제성과 반복 수주가 확인될 때만

Stage 4B:
재생에너지 정책 기대 과열

Stage 4C:
impairment, project delay, financing cost 상승, 원가 초과
```

## `WASTE_RECYCLING_ENVIRONMENT`

```text
Stage 1:
폐기물처리 M&A, 규제 강화, 재활용 수요 뉴스

Stage 2:
처리량, 장기계약, 가동률, FCF 확인

Stage 3:
허가권·처리시설·반복 FCF가 valuation frame을 바꿀 때

Stage 4B:
M&A 프리미엄 과열

Stage 4C:
가동률 하락, CAPEX 부담, 금속가격 하락, 규제비용 증가
```

## `EV_FIRE_BESS_SAFETY_OVERLAY`

```text
Stage 1:
EV/BESS 화재, 배터리 제조사 공개, 인증제 뉴스

Stage 2:
인증·공개 의무, 안전설비 규제, 리콜·보험비용 확인

Stage 3:
안전성 개선이 실제 수요 회복과 비용 안정으로 이어질 때만

Stage 4B:
안전규제 대응 narrative 과열

Stage 4C:
대형 화재, 배터리 리콜, 충전 제한, 보험비용 상승, 소비심리 훼손
```

---

# 10. 가격경로 검증계획

## R3 Loop 4 공통 검증 방식

```text
1. 각 case의 stage1_date, stage2_date, stage3_date를 지정한다.
2. 해당 날짜의 종가를 stage_price로 저장한다.
3. MFE_30D / 90D / 180D / 1Y / 2Y를 계산한다.
4. MAE_30D / 90D / 180D / 1Y를 계산한다.
5. peak_price와 drawdown_after_peak를 계산한다.
6. EV 수요, ESS 계약, 공장 가동률, CAPEX, 광물가격, 보조금/관세,
   화재·인증 이벤트와 가격경로를 비교한다.
```

## Loop 4에서 새로 강제할 판정

```text
EV_CAPA_FALSE_GREEN:
EV CAPA 증설은 있었지만 공장 idle, 계약취소, 수요 둔화가 발생.

ESS_CONTRACT_ALIGNED:
ESS 계약금액·기간·고객·GWh가 확인되고 주가·EPS가 동행.

ESS_DISCLOSURE_CAPPED:
계약은 있으나 고객명·용도·금액 중 핵심값이 미공개라 Stage 3 제한.

ESS_SHIFT_BUT_EV_OVERHANG:
ESS 전환 근거는 있으나 EV 둔화와 idle plant가 주가를 누름.

EV_TO_ESS_REDEPLOYMENT_WATCH:
EV 설비·사업을 ESS로 재배치하나 고객·마진·가동률 확인 필요.

RECYCLING_INFRA_SUCCESS:
허가권·처리량·반복 FCF가 확인된 폐기물/재활용 사업.

RECYCLING_SECOND_LIFE_RISK:
폐배터리·second-life ESS에서 SOH·잔존가치 검증비용이 큰 경우.

SOLAR_POLICY_SUPPLYCHAIN_4C:
보조금·미국공장 narrative가 통관·관세·부품 억류로 깨짐.

WIND_PROJECT_IMPAIRMENT_4C:
원가·금리·일정 지연으로 프로젝트 손상.

LITHIUM_CYCLICAL_SUCCESS_OR_FAILURE:
리튬 가격·광산 폐쇄·재가동·ESS 수요에 따른 cycle 판정.

EV_BESS_SAFETY_REGULATORY_OVERLAY:
화재·배터리 인증·시설규제·보험비용을 별도 RedTeam으로 적용.
```

## 이번 R3 Loop 4에서 우선 검증할 가격 case

| case_id                                    | stage2 후보일 | 현재 1차 가격판정                                       |
| ------------------------------------------ | ---------: | ------------------------------------------------ |
| `lg_energy_lfp_4_3b_contract_case`         | 2025-07-30 | $4.3B, 2027~2030, 고객·용도 미공개                      |
| `sk_on_flatiron_ess_7_2gwh_case`           | 2025-09-03 | 최대 7.2GWh, 계약금액 미공개                              |
| `gm_lg_ultium_ohio_idle_case`              | 2026-05-12 | EV CAPA 4C + ESS shift watch                     |
| `ford_energy_storage_pivot_case`           |    2026-05 | EV→ESS redeployment, AI DC storage event premium |
| `ford_lges_ev_contract_cancel_case`        | 2025-12-17 | $6.5B 계약취소, hard 4C                              |
| `redwood_recycling_energy_storage_case`    | 2025-10-23 | 재활용+ESS+AI DC reference                          |
| `eqt_kj_environment_waste_platform_case`   | 2024-08-16 | 폐기물 Green reference                              |
| `hyundai_hydrogen_fuel_cell_plant_case`    | 2025-10-30 | 수소 CAPEX Stage 1.5~2                             |
| `qcells_customs_detention_furlough_case`   | 2025-11-08 | 태양광 공급망 hard 4C                                  |
| `orsted_sunrise_wind_impairment_case`      | 2025-01-20 | 풍력 project 4C                                    |
| `lithium_price_86pct_crash_case`           | 2025-01-13 | 리튬 cycle hard counterexample                     |
| `lithium_ess_demand_recovery_case`         | 2026-01-05 | ESS 수요로 리튬 outlook 개선, cycle watch               |
| `korea_ev_battery_certification_fire_case` | 2024-08-25 | EV fire regulatory overlay                       |
| `moss_landing_bess_fire_case`              |    2025-01 | BESS safety/permitting overlay                   |
| `battery_soh_transparency_case`            |    2026-03 | second-life/recycling 정보비대칭 overlay              |

---

# 11. 다음에 에이전트가 채워야 할 price fields

R3 Loop 4에서는 아래 필드를 채우게 해야 한다.

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

ev_demand_indicator
ev_sales_growth
ev_subsidy_change_flag
ev_tax_credit_expiry_flag
automaker_ev_cutback_flag
ev_model_discontinued_flag
plant_idle_flag
layoff_furlough_flag
contract_cancelled_flag
capacity_utilization
capex_amount
capex_to_revenue
capex_cut_flag

ess_contract_value
ess_contract_duration_months
ess_contract_customer
ess_customer_disclosed_flag
ess_use_case_disclosed_flag
ess_contract_volume_gwh
ess_capacity_gwh
ess_capacity_utilization
ess_margin
ess_revenue_growth
lfp_ess_flag
grid_storage_flag
data_center_storage_flag
contract_extension_option_years
disclosure_confidence_score

ev_to_ess_conversion_flag
ev_line_conversion_cost
converted_line_capacity_gwh
converted_line_utilization
storage_customer_contract_flag
ai_data_center_storage_customer_flag
gross_margin_target
catl_license_flag
feoc_or_national_security_risk_flag

battery_material_contract_value
battery_material_contract_duration
price_pass_through_flag
raw_material_price_change
lithium_price_change
nickel_price_change
cobalt_price_change
black_mass_price
metal_recovery_revenue

recycling_volume
recovered_material_volume
recovery_rate
pCAM_output
recycling_customer_contract
second_life_battery_flag
soh_validation_flag
battery_passport_compliance_flag
battery_grading_cost
residual_capacity_uncertainty_flag
warranty_enforcement_risk_flag

waste_treatment_volume
waste_treatment_capacity
permit_asset_flag
recurring_fcf_flag
waste_to_energy_flag
plastic_recycling_revenue
catchment_area_population_share

hydrogen_capex_amount
hydrogen_plant_completion_date
fuel_cell_capacity
electrolyzer_capacity
hydrogen_customer_contract
hydrogen_subsidy_dependency
hydrogen_capacity_utilization

solar_tariff_event
customs_detention_flag
uflpa_flag
feoc_flag
component_delay_flag
solar_capacity_utilization
furlough_layoff_flag

wind_project_delay_flag
wind_project_impairment
financing_cost_change
foundation_cost_increase
permitting_delay_flag
grid_connection_delay_flag

carbon_credit_price
cbam_exposure
carbon_accounting_revenue
pass_through_ability

ev_fire_event_flag
bess_fire_event_flag
battery_certification_flag
battery_supplier_disclosure_flag
recall_flag
insurance_cost_change
underground_parking_regulation_flag
overcharge_prevention_charger_flag
facility_permitting_delay_flag
fire_safety_capex_flag

score_price_alignment
price_validation_status
review_notes
```

---

# R3 Loop 4 결론

이번 4회차에서 R3는 더 좁혀졌다.

```text
Green 가능:
LFP ESS 장기계약이 실제 금액·기간·고객·GWh·마진으로 확인된 기업
AI 데이터센터 storage 계약과 OPM/FCF가 확인된 기업
폐기물처리 허가권·처리량·반복 FCF가 확인된 기업
재활용 + ESS + 고객계약 + 회수금속 매출이 연결된 기업
수소 CAPEX가 고객·가동률·OPM으로 연결되는 기업
탄소회계·CBAM compliance 반복매출이 확인되는 기업

Watch-to-Green:
2차전지 장비
ESS 전환
EV→ESS 라인 재배치
폐배터리
수소연료전지
데이터센터 물 재활용
EV 인프라 중 실제 이용률·운영수익이 확인된 기업

Watch/Red:
2차전지 소재 CAPA 과열
EV 충전 인프라
태양광
풍력
리튬 원재료
전고체 배터리
폐배터리 테마주
탄소배출권 가격 테마
계약정보가 불완전한 ESS 계약

Hard 4C:
EV 공장 idle
EV 배터리 계약 취소
태양광 통관·관세·부품 억류
풍력 impairment
리튬 가격 급락·공급 재가동
EV/BESS 화재·배터리 인증 규제
SOH 불확실성으로 인한 second-life/recycling 가치 훼손
```

**R3 Loop 4 점수정규화의 핵심 문장:**

> 2차전지·전기차·친환경은 “EV 성장”, “ESS”, “폐배터리”, “수소”, “태양광”, “풍력”이라는 이름이 아니라 **계약금액, 계약기간, 고객사, GWh, 가동률, ESS OPM, 회수량, 금속 회수 매출, SOH 검증, 보조금 의존도, 통관·관세 리스크, 화재·안전규제, FCF 전환, 실제 가격경로**로 봐야 한다.
> EV CAPA와 리튬 가격은 쉽게 4C로 바뀌고, ESS·폐기물·재활용은 실제 계약과 반복 FCF가 붙을 때만 Green 후보가 된다.

다음 순서는 **R4 — 소재·스프레드·전략자원 Loop 4**다.

[1]: https://www.reuters.com/business/energy/lg-energy-solution-signs-43-billion-battery-supply-contract-2025-07-30/?utm_source=chatgpt.com "LG Energy Solution signs $4.3 billion battery supply contract"
[2]: https://www.reuters.com/business/energy/south-koreas-sk-signs-ess-battery-supply-deal-with-us-based-flatiron-energy-2025-09-03/?utm_source=chatgpt.com "South Korea's SK On signs ESS battery supply deal with US-based Flatiron Energy"
[3]: https://www.reuters.com/legal/litigation/gms-restart-date-ohio-battery-plant-uncertain-2026-05-12/?utm_source=chatgpt.com "GM-LG's restart date at Ohio battery plant uncertain"
[4]: https://www.ft.com/content/3788778f-ea93-4811-80a8-4c8f4c5c0b1f?utm_source=chatgpt.com "Ford shares surge after launch of power unit for data centres"
[5]: https://www.reuters.com/business/battery-recycling-firm-redwood-raises-350-million-eclipse-ventures-nvidia-2025-10-23/?utm_source=chatgpt.com "Battery recycling firm Redwood raises $350 million from Eclipse Ventures, Nvidia"
[6]: https://www.reuters.com/markets/deals/eqt-strikes-deal-acquire-south-korean-waste-treatment-platform-2024-08-16/?utm_source=chatgpt.com "EQT strikes deal to acquire South Korean waste treatment platform"
[7]: https://www.reuters.com/world/asia-pacific/hyundai-motor-breaks-ground-680-million-hydrogen-fuel-cell-plant-south-korea-2025-10-30/?utm_source=chatgpt.com "Hyundai Motor breaks ground on $680 million hydrogen fuel cell plant in South Korea"
[8]: https://www.reuters.com/business/finance/south-koreas-lg-energy-solution-ends-65-billion-ev-battery-supply-deal-with-ford-2025-12-17/?utm_source=chatgpt.com "Ford cancels EV battery deal worth $6.5 billion with South Korea's LG Energy Solution"
[9]: https://www.reuters.com/sustainability/climate-energy/qcells-furloughs-1000-workers-us-solar-factories-due-stalled-shipments-2025-11-08/?utm_source=chatgpt.com "Qcells furloughs 1,000 workers at US solar factories due to stalled shipments"
[10]: https://www.reuters.com/business/energy/orsted-flags-impairments-about-17-billion-us-rate-increases-2025-01-20/?utm_source=chatgpt.com "Orsted flags $1.7 bln impairment on Sunrise Wind delays, increased costs"
[11]: https://www.reuters.com/markets/commodities/lithium-prices-stabilise-2025-mine-closures-china-ev-sales-ease-glut-analysts-2025-01-13/?utm_source=chatgpt.com "Lithium prices to stabilise in 2025 as mine closures, China EV sales ease glut, analysts say"
[12]: https://www.reuters.com/sustainability/climate-energy/energy-storage-boom-strengthens-demand-outlook-beaten-down-lithium-2026-01-04/?utm_source=chatgpt.com "Energy storage boom strengthens demand outlook for beaten-down lithium"
[13]: https://www.reuters.com/business/autos-transportation/south-korea-advance-ev-battery-certification-scheme-after-fires-2024-08-25/?utm_source=chatgpt.com "South Korea to advance EV battery certification scheme after fires"
[14]: https://apnews.com/article/e5957a710670930ca23c4b2d2e3ed75f?utm_source=chatgpt.com "A battery plant fire in California started during a boom for energy storage"
[15]: https://arxiv.org/abs/2603.21592?utm_source=chatgpt.com "Battery health reporting fails independent validation across manufacturers"

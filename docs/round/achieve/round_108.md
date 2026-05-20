좋아. **R2 Loop 6까지 끝났으니, 이번은 R3 Loop 6 — 2차전지·전기차·친환경**이다.

R3는 2차전지 소재·부품·공정장비, 폐배터리, 전고체, 전기차 인프라, 전기차 화재, 수소차 연료전지·인프라, 태양광, 풍력, 탄소배출권, 폐기물처리, 탈플라스틱을 흡수하는 대섹터다. Theme Tag Map 기준으로도 R3는 **Green보다 과열 방어가 우선**이고, 소재·전고체·폐배터리는 실제 계약·수익성·FCF 확인 전까지 Stage 3-Green을 제한해야 한다.

Checkpoint 20 원칙도 그대로 적용한다. 공급계약, 투자금액, 계약기간, 매출 대비 계약금액, 고객사, 가동률, OP YoY, 회수량, 금속 회수 매출, 공장 idle, 계약 취소 같은 값은 실제 공시·기사·리포트에서 확인될 때만 써야 한다. R3는 “ESS”, “폐배터리”, “전고체”, “AI 데이터센터 전력”, “친환경” 같은 단어만으로 점수가 쉽게 부풀기 때문에, 빈 값을 추정하면 false-positive가 커진다.

서생원식으로 보면 R3의 질문은 “전기차가 성장하나?”가 아니다. **EV 성장 narrative가 아니라 EPS/FCF 체급 변화가 지속되고, 시장이 아직 과거 프레임으로 낮게 보는가**다. EV CAPA가 늘어도 공장이 멈추면 4C이고, ESS 계약이 실제 금액·기간·고객·마진으로 확인되면 Stage 2~3 후보가 된다.

---

# R3 Loop 6. 2차전지·전기차·친환경

## 1. 이번 라운드 대섹터

```text
R3 = 2차전지·전기차·친환경
Loop 6 목표 =
EV CAPA 과열 / EV 계약취소 / SK-Ford·GM-LG JV 재편 /
ESS 장기계약 / Tesla Megapack supply chain /
EV→ESS 라인전환 / 폐배터리+AI DC storage /
SOH·second-life 투명성 / 리튬 ESS cycle /
sodium-ion 대체 / graphite supply security /
태양광 UFLPA / 풍력 impairment / EV·BESS 안전규제를 더 정밀 분리
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

Loop 6부터는 이렇게 갈라야 한다.

```text
좋은 구조 후보:
ESS 장기계약 + 계약금액 + 계약기간 + 고객 + GWh + ESS OPM
Tesla Megapack / hyperscaler / utility storage로 확인된 LFP supply chain
EV 공장 idle을 ESS 라인으로 전환하고 실제 고객계약이 붙는 기업
폐배터리 + 금속 회수 + ESS/grid storage + 고객계약
폐기물처리 허가권 + 처리량 + 반복 FCF
AI 데이터센터 storage / water / cooling 계약
친환경 시멘트·폐기물·재활용처럼 허가권과 반복 현금흐름이 붙는 사업

위험한 후보:
EV CAPA 증설만 있는 소재주
계약금액·고객명 없는 ESS 계약 과대해석
전고체·폐배터리 테마만 있는 기업
태양광 보조금·관세 의존 기업
풍력 project economics가 약한 기업
리튬 가격 반등만 보는 광물주
sodium-ion 대체를 무시한 리튬·LFP 테마
EV·BESS 화재와 인증·보험·시설규제 overlay가 붙은 기업
```

---

## 2. 대상 canonical archetype

| canonical archetype                      | Loop 6 정책                                                    |
| ---------------------------------------- | ------------------------------------------------------------ |
| `BATTERY_MATERIALS_CAPEX_OVERHEAT`       | Watch/Red. EV 수요·CAPA·계약취소·광물가격 감점 강화                        |
| `BATTERY_EQUIPMENT_PARTS`                | Watch-to-Green. 고객사 CAPEX와 실제 납품·마진 필요                       |
| `ESS_LFP_GRID_STORAGE`                   | Green 후보. 계약금액·계약기간·고객·GWh·OPM 필요                            |
| `ESS_TESLA_MEGAPACK_SUPPLY_CHAIN`        | Watch-to-Green. Tesla/Megapack 확인 시 visibility 강화, 마진·가동률 필요 |
| `ESS_AI_DATA_CENTER_STORAGE`             | Watch-to-Green. 데이터센터 전력수요와 실제 storage 계약 필요                 |
| `EV_TO_ESS_CAPACITY_REDEPLOYMENT`        | Watch. EV 라인 전환은 좋지만 idle plant·전환비용·계약 확인 필요                |
| `EV_BATTERY_JV_RESTRUCTURING`            | Watch/Red. JV 해체·자산 이전은 고정비 절감과 수요둔화를 동시에 의미                 |
| `EV_CAPA_CONTRACT_CANCELLATION`          | RedTeam gate. EV 수요둔화·계약취소·write-down                        |
| `BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE` | RedTeam overlay. 고객명·계약금액·용도 미공개 시 score cap                 |
| `BATTERY_RECYCLING_ESS_SHIFT`            | Watch-to-Green. 회수량·금속 회수·ESS/grid 고객 필요                     |
| `SECOND_LIFE_BATTERY_GRID_STORAGE`       | Watch-to-Green. second-life ESS는 SOH·잔존가치·안전검증 필요            |
| `BATTERY_SOH_SECOND_LIFE_TRANSPARENCY`   | RedTeam overlay. SOH·battery passport·잔존가치 검증                |
| `BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY`  | Watch. 중국 의존도·미국 생산비·정책지원·고객계약 확인                            |
| `LITHIUM_ESS_DEMAND_CYCLE`               | Cycle/Watch. ESS 수요가 붙어도 공급·광산 재가동·sodium-ion 리스크            |
| `SODIUM_ION_SUBSTITUTION_OVERLAY`        | RedTeam overlay. ESS·저가 EV에서 리튬/LFP 가격상한 역할                  |
| `SOLID_STATE_COMMERCIALIZATION_LICENSE`  | Watch. licensing은 Stage 2 후보, 양산·royalty·고객차종 전 Green 금지     |
| `SPECULATIVE_BATTERY_TECH`               | Watch/Red. 전고체·신소재는 상용화·고객·양산 전 Green 금지                     |
| `EV_INFRASTRUCTURE`                      | Watch. 충전소 이용률·수익성·화재규제 확인                                   |
| `EV_FIRE_BESS_SAFETY_OVERLAY`            | RedTeam gate. EV·ESS 화재, 인증, 보험, 주차장·시설 규제                   |
| `BESS_SAFETY_PERMITTING`                 | RedTeam gate. BESS 화재·대피·지역반발·시설허가·보험비용                      |
| `HYDROGEN_FUEL_CELL_INFRA`               | Watch-to-Green. 실제 CAPEX·고객·가동률 필요                           |
| `SOLAR_TARIFF_SUPPLYCHAIN`               | Watch/Red. 보조금·관세·통관·UFLPA 리스크 큼                             |
| `RENEWABLE_ENERGY_PROJECT_ECONOMICS`     | Watch/Red. 풍력은 원가·금리·인허가·impairment 4C 가능                    |
| `WASTE_RECYCLING_ENVIRONMENT`            | Green 가능. 허가권·처리량·반복 FCF 필요                                  |
| `CARBON_CREDIT_CBAM_COMPLIANCE`          | Watch. 탄소가격보다 탄소회계·검증·비용전가 매출 필요                             |
| `DATA_CENTER_WATER_REUSE_INFRA`          | Watch-to-Green. 데이터센터 물 재활용·냉각 계약 필요                         |

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
- Tesla Megapack
- Megapack 3
- Megablock
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
- SK On Tennessee facility
- Ford Energy
- LFP licensing
- EV demand overhang
- 전환비용
- 가동률

EV_BATTERY_JV_RESTRUCTURING
- SK On-Ford JV dissolution
- GM-LG Ultium idle
- Ford full ownership Kentucky
- SK On Tennessee ownership
- debt reduction
- fixed cost reduction
- ESS pivot
- operating loss
- EV subsidy expiry

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
- AI data center power

SECOND_LIFE_BATTERY_GRID_STORAGE
- second-life EV battery
- used EV battery pack
- SOH validation
- battery passport
- residual capacity
- warranty
- fire safety
- grid services
- data center backup

BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY
- graphite
- anode material
- natural graphite
- synthetic graphite
- China dependency
- US production cost
- policy financing
- methane pyrolysis
- catalytic graphitization

LITHIUM_ESS_DEMAND_CYCLE
- 리튬
- 리튬 정제
- 광산 폐쇄
- 광산 재가동
- EV 수요
- ESS 수요
- sodium-ion 대체
- 가격 급락
- CAPEX cut

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
```

---

# 4. 성공사례 / 구조 후보

## 4-1. LGES–Tesla 43억 달러 LFP 계약 — `ESS_TESLA_MEGAPACK_SUPPLY_CHAIN`

LG에너지솔루션의 43억 달러 LFP 계약은 Loop 6에서 더 강한 Stage 2 후보로 승격한다. 2025년 최초 발표 때는 고객·용도가 공개되지 않아 `BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE` cap이 필요했지만, 2026년 3월 미국 정부가 Tesla와 LGES의 43억 달러 LFP prismatic cell agreement를 확인했고, 해당 셀은 Houston에서 생산되는 Tesla Megapack 3 ESS에 쓰이며 Lansing, Michigan에서 2027년 생산 개시 예정이라고 밝혔다. 즉 이 케이스는 “미공개 LFP 계약”에서 **Tesla Megapack 3 ESS supply chain**으로 정보 신뢰도가 크게 올라간 사례다. ([Reuters][1])

```text
가격경로 1차 판정:
ESS_TESLA_MEGAPACK_SUPPLY_CHAIN_STAGE2_CANDIDATE

좋은 점:
- 계약금액 $4.3B
- 고객/용도 확인: Tesla Megapack 3 ESS
- Lansing, Michigan 생산
- 2027년 생산 개시 예정
- 미국 LFP prismatic cell supply chain
- 중국 LFP 의존도 축소 narrative와 직접 연결

주의:
- ESS OPM 미확인
- Lansing ramp-up 필요
- Megapack 3 수요 지속성 확인 필요
- LFP 가격경쟁
- IRA/관세/FEOC 규정 변화
```

**Loop 6 교정**

```text
BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE:
2025년 7월 최초 발표 기준:
customer/use_case_unknown = true
Stage 3 cap

2026년 3월 확인 이후:
customer = Tesla
use_case = Megapack 3 ESS
visibility score 상향

하지만 Stage 3는:
생산 ramp-up
+ 실제 매출 인식
+ ESS OPM
+ 가동률
+ FCF
확인 후.
```

---

## 4-2. SK On–Flatiron ESS 공급계약 — `ESS_LFP_GRID_STORAGE`

SK On은 미국 Flatiron Energy Development에 ESS용 LFP 배터리를 최대 7.2GWh 공급하기로 했다. 공급기간은 2026~2030년이고, SK On은 2026년 하반기부터 ESS 전용 LFP 배터리 양산을 시작하며 일부 미국 EV 라인을 ESS 제조용으로 전환할 계획이라고 밝혔다. 다만 계약금액은 공개되지 않았기 때문에 Stage 2 후보는 가능하지만 Stage 3-Green에는 value cap을 둔다. ([Reuters][2])

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

**Loop 6 교정**

```text
contract_value_missing = true이면 EPS/FCF 점수 상한을 둔다.

GWh와 기간은 Stage 2 근거.
하지만 Stage 3-Green은 매출·마진·FCF 확인 전까지 제한.
```

---

## 4-3. GM–LG Ultium Ohio idle / Tennessee ESS 전환 — `EV_TO_ESS_CAPACITY_REDEPLOYMENT`

GM과 LG에너지솔루션의 Ultium Cells는 Ohio EV 배터리 공장 재가동 일정이 불확실했고, January 2026 이후 약 850명 규모 근로자 복귀도 전면적으로 예정되지 않았다. Reuters는 EV 수요 둔화와 2025년 9월 미국 EV 세액공제 종료가 배경이라고 설명했다. 동시에 Tennessee 공장에서는 EV 대신 ESS용 배터리 셀 생산을 위해 근로자들이 복귀했다. 즉 이 케이스는 **EV CAPA thesis 4C + ESS 전환 Watch**가 동시에 붙는 복합 사례다. ([Reuters][3])

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

**Loop 6 교정**

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

## 4-4. SK On–Ford JV 해체 — `EV_BATTERY_JV_RESTRUCTURING`

SK On과 Ford는 미국 배터리 JV를 끝내기로 했고, Ford는 Kentucky 공장을 가져가며 SK On은 Tennessee 시설을 맡는 구조로 재편했다. Reuters는 이 결정이 EV 수요 둔화와 보조금 종료 속에서 한국 배터리 업체들이 ESS로 전략을 옮기는 흐름과 연결된다고 설명했고, SK On은 Q3 2025에 1,248억 원 영업손실을 냈다고 보도했다. 즉 이 케이스는 “나쁜 뉴스”만이 아니라 **EV 고정비 축소 + ESS pivot**이라는 재편 후보지만, 동시에 EV demand 4C가 강하게 붙는다. ([Reuters][4])

```text
가격경로 1차 판정:
EV_JV_RESTRUCTURING_WITH_ESS_PIVOT

좋은 점:
- 고정비 절감 가능성
- Tennessee ESS 전환 option
- 북미 ESS 사업 대응 속도 향상
- EV 둔화에 대한 자산 재배치

주의:
- JV 해체 자체는 EV 수요둔화 증거
- SK On 영업손실
- 생산 일정 유연화 = visibility 낮음
- ESS 매출·마진 전까지 Green 제한
```

**Loop 6 교정**

```text
EV_BATTERY_JV_RESTRUCTURING 신규 강화.

JV 해체는:
Stage 1 = 구조조정
Stage 2 = 자산 재배치 + ESS 계약
Stage 3 = 고정비 절감 + ESS OPM + FCF 확인

그 전까지는 Green이 아니라 Watch.
```

---

## 4-5. EV 계약취소 hard 4C — `EV_CAPA_CONTRACT_CANCELLATION`

Ford는 LGES와의 EV 배터리 공급계약 약 65억 달러를 취소했고, LGES는 Freudenberg Battery Power Systems와의 3.9조 원 계약도 취소했다. Reuters는 두 취소로 LGES가 10일 안에 약 13.5조 원 기대 매출을 잃었다고 보도했다. 이건 EV 배터리 계약이 공시되어 있어도 고객의 EV 전략·정책 환경·수요 전망이 바뀌면 thesis가 깨질 수 있다는 hard 4C다. ([Reuters][5])

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
- expected_revenue_loss
- capacity_underutilization
- EV_policy_change
```

**Loop 6 교정**

```text
BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE:
계약 detail이 있어도 고객 전략 리스크를 따로 본다.

customer_strategy_risk_flag = true
contract_cancelled_flag = true

이면 기존 Stage 2~3 후보도 즉시 재평가.
```

---

## 4-6. Redwood Materials — `BATTERY_RECYCLING_ESS_SHIFT`

Redwood Materials는 폐배터리·금속 회수·ESS가 결합되는 좋은 구조 reference다. Redwood는 Eclipse Ventures가 주도하고 Nvidia의 NVentures가 참여한 라운드에서 3.5억 달러를 조달했고, 리튬·코발트·니켈·구리 같은 핵심 소재 회수뿐 아니라 grid services와 데이터센터용 energy storage systems도 제공한다. Volkswagen, Panasonic, Toyota, Lyft 등과의 파트너십도 보도됐다. ([Reuters][6])

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

**Loop 6 교정**

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

## 4-7. 리튬 ESS 수요 회복 — `LITHIUM_ESS_DEMAND_CYCLE`

ESS 수요는 리튬 outlook을 실제로 바꾸고 있다. Reuters는 중국 전력시장 개혁과 글로벌 데이터센터 건설 붐이 ESS용 리튬 수요를 끌어올리고 있으며, energy storage demand가 2026년에 55% 성장할 수 있고 리튬 수요 중 energy storage 비중이 2025년 23%에서 2026년 31%로 올라갈 수 있다고 보도했다. 다만 sodium-ion 전환, EV 보조금 종료, 공급 증가가 가격 상승을 제한할 수 있다는 리스크도 함께 제시됐다. ([Reuters][7])

```text
가격경로 1차 판정:
LITHIUM_ESS_DEMAND_RECOVERY_BUT_CYCLE_WATCH

좋은 점:
- ESS 수요가 리튬 수요의 새 축으로 부상
- AI 데이터센터·전력망 storage 수요
- 중국 전력시장 개혁
- supply glut 완화 가능성

주의:
- sodium-ion 대체
- EV 수요 둔화
- 광산 재가동
- 가격 전망 분산
- 리튬주는 commodity cycle 우선
```

리튬은 2022년 11월 고점 이후 약 86% 급락했고, 폐쇄된 광산이 가격 반등 시 재가동될 수 있어 상승폭을 제한할 수 있다는 분석도 있다. 그래서 리튬은 ESS 수요가 붙어도 structural Green이 아니라 `cycle/watch`로 먼저 둔다. ([Reuters][8])

**Loop 6 교정**

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

## 4-8. Graphite supply security — `BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY`

Loop 6에서 흑연 공급망을 더 분리한다. 2025년 arXiv 연구는 배터리용 anode material의 92% 이상이 중국에서 생산된다고 분석했고, 미국 내 battery-grade graphite 생산은 자본집약도와 투입비용 때문에 현재 가격에서 경쟁력이 약하다고 평가했다. 이건 “중국 의존도 때문에 미국 흑연 생산 수혜”라는 단순 프레임이 아니라, **공급망 안보 + 높은 원가 + 정책금융 필요**가 동시에 붙는 구조다. ([arXiv][9])

```text
가격경로 1차 판정:
GRAPHITE_SUPPLYCHAIN_SECURITY_WATCH

좋은 점:
- 중국 의존도 극단적으로 높음
- EV/ESS anode supply chain security 중요
- 정책금융·지원 가능성
- alternative graphite pathway 가능성

주의:
- 미국 생산비 높음
- 현재 가격에서 경제성 약함
- 고객계약·offtake 필요
- 보조금·financing 의존 가능성
```

**Loop 6 교정**

```text
BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY 신규 추가.

Stage 1:
중국 의존도·수입규제·공급망 안보 뉴스.

Stage 2:
정책금융 + offtake + 생산원가 경로 + 고객계약.

Stage 3:
실제 매출·마진·FCF 전환.
```

---

## 4-9. 전고체 licensing — `SOLID_STATE_COMMERCIALIZATION_LICENSE`

Volkswagen의 PowerCo는 QuantumScape의 전고체 배터리 기술을 대량생산할 수 있는 license를 받았고, 연간 40GWh 생산권과 최대 80GWh 확장 가능성을 확보했다. 발표 당시 QuantumScape 주가는 premarket에서 40% 뛰었다. 다만 Reuters는 이 계약이 기술진전과 royalty payment 조건에 달려 있다고 보도했기 때문에, 전고체는 Stage 2 후보가 될 수는 있어도 고객차종 양산·royalty·수율 전까지 Stage 3-Green은 막아야 한다. ([Reuters][10])

```text
가격경로 1차 판정:
SOLID_STATE_LICENSE_STAGE2_BUT_COMMERCIALIZATION_WATCH

좋은 점:
- VW PowerCo license
- 40GWh / 최대 80GWh 생산권
- royalty 구조 가능성
- 기존 JV보다 asset-light 구조 가능

주의:
- 기술진전 조건부
- mass production 전
- yield / cost / safety / cycle life 확인 필요
- 실제 차량 탑재·매출 전 Green 제한
```

**Loop 6 교정**

```text
전고체:
논문·샘플·기술홍보 = Stage 1
license + royalty 구조 = Stage 2
양산 + 고객차종 + 매출 + margin = Stage 3
```

---

# 5. 반례 / RedTeam

## 5-1. EV 배터리 계약 취소

```text
4C:
EV_demand_slowdown
contract_cancellation
automaker_EV_cutback
EV_model_discontinued
expected_revenue_loss
capacity_underutilization
```

Ford–LGES 65억 달러 계약 취소와 LGES–Freudenberg 3.9조 원 계약 취소는 EV 배터리 계약도 고객 전략이 바뀌면 바로 thesis break가 된다는 기준이다. ([Reuters][5])

---

## 5-2. EV 배터리 공장 idle

```text
4C:
EV_demand_slowdown
plant_idle
layoff_furlough
fixed_cost_burden
capacity_underutilization
tax_credit_expiry
```

Ultium Ohio 공장 재가동 불확실성은 EV CAPA overhang의 대표 사례다. 다만 Tennessee ESS 전환은 별도 Watch-to-Green 후보로 보되, 고객계약·가동률·OPM 확인 전까지 Stage 3-Green은 막는다. ([Reuters][3])

---

## 5-3. SK-Ford JV 해체

```text
4C-watch:
JV_dissolution
EV_subsidy_expiry
operating_loss
fixed_cost_restructuring
capacity_reassignment
ESS_pivot_unproven
```

SK On–Ford JV 해체는 EV 수요 둔화와 보조금 종료가 북미 배터리 설비 전략을 바꾼 사례다. ESS pivot은 긍정적 option이지만, ESS 매출·마진·FCF로 넘어가기 전까지는 restructuring Watch다. ([Reuters][4])

---

## 5-4. Qcells 통관·UFLPA 리스크 — `SOLAR_TARIFF_SUPPLYCHAIN`

Qcells는 미국 조지아 태양광 공장에서 약 1,000명 근로자에 대해 furlough를 실시했다. 해외 부품 선적이 미국 세관에서 지연됐고, UFLPA 집행 때문에 핵심 부품이 억류되면서 생산차질이 발생했다. 미국 제조·보조금 narrative가 있어도 통관·관세·공급망 투명성 하나로 생산이 흔들릴 수 있다는 hard 4C다. ([Reuters][11])

```text
가격경로 1차 판정:
SOLAR_SUPPLYCHAIN_HARD_4C

4C 조건:
- customs_detention_flag
- UFLPA_flag
- component_delay_flag
- furlough_layoff_flag
- supply_chain_transparency_risk
```

---

## 5-5. Ørsted Sunrise Wind impairment — `RENEWABLE_ENERGY_PROJECT_ECONOMICS`

Ørsted는 Sunrise Wind 프로젝트 지연과 비용 상승, 미국 financing cost 증가로 약 17억 달러 impairment를 발표했다. 프로젝트는 2027년 하반기로 지연됐고, monopile foundation 비용 증가가 주요 원인으로 언급됐다. 해상풍력은 정책·PPA가 있어도 financing·원가·공정이 맞지 않으면 4C로 간다. ([Reuters][12])

```text
가격경로 1차 판정:
OFFSHORE_WIND_PROJECT_4C

4C 조건:
- cost_overrun
- project_delay
- financing_cost_increase
- foundation_cost_increase
- impairment
```

---

## 5-6. EV 화재·배터리 인증 — `EV_FIRE_BESS_SAFETY_OVERLAY`

한국 정부와 여당은 EV 화재 우려가 커진 뒤 배터리 인증제 시행을 앞당기고, 자동차 회사가 EV에 들어가는 배터리 정보를 공개하도록 하는 방안을 추진했다. 2024년 8월 Mercedes-Benz EV 화재가 지하주차장에서 발생해 수백 대 차량을 파손시키고 주민 대피를 불렀으며, 이후 지하주차장 스프링클러와 과충전 방지 충전기 확대 같은 안전대책도 논의됐다. ([Reuters][13])

```text
가격경로 1차 판정:
EV_FIRE_REGULATORY_OVERLAY

감점 조건:
- battery_certification_flag
- battery_supplier_disclosure_flag
- fire_event_flag
- parking_charging_regulation_flag
- insurance_cost_change
```

---

## 5-7. Moss Landing BESS 화재 — `BESS_SAFETY_PERMITTING`

California Moss Landing의 대형 battery storage plant에서는 화재와 재발화가 발생했고, 약 1,500명 대피와 유독연기 우려가 나왔다. 이 사례는 ESS 수요가 강해도 시설허가·소방·보험·지역사회 수용성이 project economics와 timeline을 바꿀 수 있음을 보여준다. ([가디언][14])

```text
가격경로 1차 판정:
BESS_SAFETY_PERMITTING_4C_WATCH

감점 조건:
- bess_fire_event_flag
- evacuation_flag
- fire_safety_capex
- permitting_delay
- insurance_cost_change
- local_opposition
```

---

## 5-8. Battery SOH 투명성 — `BATTERY_SOH_SECOND_LIFE_TRANSPARENCY`

2026년 arXiv 연구는 1,114대 EV와 5개 제조사를 대상으로 차량 내 BMS가 보고하는 battery state-of-health가 실제 capacity 차이를 충분히 반영하지 못한다고 분석했다. 모델별 실제 capacity 차이가 12~25% 존재했지만, BMS SOH와의 상관관계는 약하거나 일부 차량은 SOH 자체를 제공하지 않았다. 이건 중고 EV valuation, warranty, second-life battery, 폐배터리 회수품질 평가에 중요한 정보 비대칭 리스크다. ([arXiv][15])

```text
가격경로 1차 판정:
BATTERY_HEALTH_TRANSPARENCY_REDTEAM

의미:
폐배터리·second-life ESS는 회수량만으로 부족하다.
실제 잔존용량, SOH 신뢰도, 인증·검증 비용을 봐야 한다.
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

LGES 43억 달러 LFP 계약은 Tesla/Megapack use-case가 확인되어 Stage 2 신뢰도가 올라갔지만, SK On–Flatiron 계약은 계약금액이 공개되지 않았기 때문에 value cap을 걸어야 한다. ([Reuters][1])

---

## 6-2. EV→ESS capacity redeployment 4B-watch

```text
4B 조건:
- EV 공장 idle을 ESS 전환으로 긍정만 해석
- 전환비용·가동률·고객계약·마진이 미확인
- EV write-down을 ESS growth가 즉시 상쇄한다고 가정
```

GM/LG Ultium은 Ohio 공장 idle과 Tennessee ESS 전환이 동시에 존재한다. 이건 전환 후보이지만, “전환 narrative”를 “수익화”로 오분류하면 안 된다. ([Reuters][3])

---

## 6-3. EV battery JV restructuring 4B-watch

```text
4B 조건:
- SK-Ford JV 해체를 ESS pivot으로만 긍정 해석
- EV 수요둔화·영업손실·보조금 종료를 낮게 봄
- 구조조정 후 실제 ESS 매출·마진 확인 전 가격이 먼저 감
```

SK On–Ford JV 해체는 고정비 절감 option과 EV 수요둔화 4C가 동시에 붙는 사례다. ([Reuters][4])

---

## 6-4. 폐배터리·second-life ESS 4B-watch

```text
4B 조건:
- battery recycling과 critical minerals narrative가 과밀
- 회수량·금속 회수율·마진 없이 valuation 상승
- AI 데이터센터 ESS와 연결한다는 말만 있고 실제 매출화 없음
- second-life battery SOH 검증비용을 무시
```

Redwood는 좋은 reference지만, 한국 상장사로 매핑하려면 회수량, 회수소재 매출, 고객계약, SOH 검증, FCF를 따로 확인해야 한다. ([Reuters][6])

---

## 6-5. 리튬 ESS 반등 4B-watch

```text
4B 조건:
- 리튬 가격 반등으로 광물주 동반 급등
- 광산 재가동과 공급반응을 무시
- ESS 수요 증가를 곧장 구조적 shortage로 오판
- sodium-ion 대체 가능성 무시
```

ESS 수요는 리튬 outlook을 개선하지만, Reuters가 함께 지적한 sodium-ion 대체와 EV 보조금 종료·공급 증가 리스크 때문에 리튬주는 먼저 `cycle`로 봐야 한다. ([Reuters][7])

---

## 6-6. 태양광 미국 제조 4B-watch

```text
4B 조건:
- 미국 제조·보조금 narrative로 관련주 상승
- 부품 공급망과 통관 리스크를 시장이 무시
- 중국 공급망 배제를 생산차질로 연결하지 않음
```

Qcells 사례는 미국 제조 투자와 보조금 narrative가 있어도, 통관·UFLPA·부품 지연 하나로 생산이 차질을 받을 수 있음을 보여준다. ([Reuters][11])

---

## 6-7. 풍력 PPA·정책 4B-watch

```text
4B 조건:
- PPA·정책·탈탄소 수요로 관련주 급등
- foundation cost, financing cost, project delay를 무시
- impairment 가능성을 낮게 봄
```

Ørsted의 Sunrise Wind impairment는 해상풍력 프로젝트가 정책 수혜에도 불구하고 비용·금리·일정 지연으로 4C로 갈 수 있음을 보여준다. ([Reuters][12])

---

## 6-8. 전고체 4B-watch

```text
4B 조건:
- license 또는 JV 뉴스만으로 전고체 관련주 급등
- 실제 양산·수율·차량 탑재·royalty 확인 전 가격이 먼저 감
- 기술진전 조건부 계약을 확정 매출처럼 오판
```

Volkswagen–QuantumScape deal은 의미 있는 Stage 2 후보지만, 기술진전 조건과 royalty 구조가 실제 양산으로 이어져야 Stage 3가 가능하다. ([Reuters][10])

---

# 7. 4C-thesis-break 사례

## 7-1. EV 배터리 계약 취소

```text
4C:
EV_demand_slowdown
contract_cancellation
automaker_EV_cutback
EV_model_discontinued
expected_revenue_loss
capacity_underutilization
```

Ford–LGES 계약 취소와 Freudenberg 계약 취소는 EV 배터리 계약도 고객 전략이 바뀌면 바로 thesis break가 된다는 기준이다. ([Reuters][5])

---

## 7-2. EV 배터리 공장 idle

```text
4C:
EV_demand_slowdown
plant_idle
layoff_furlough
fixed_cost_burden
capacity_underutilization
tax_credit_expiry
```

Ultium Ohio 공장 재가동 불확실성은 EV CAPA overhang의 대표 사례다. ([Reuters][3])

---

## 7-3. 태양광 통관·관세·부품 억류

```text
4C:
customs_detention
UFLPA_risk
tariff_risk
production_disruption
worker_furlough
contractor_layoff
```

Qcells의 1,000명 furlough와 부품 억류는 `SOLAR_TARIFF_SUPPLYCHAIN`의 hard 4C다. ([Reuters][11])

---

## 7-4. 풍력 impairment

```text
4C:
cost_overrun
project_delay
financing_cost_increase
foundation_cost
impairment
```

Ørsted의 17억 달러 impairment는 재생에너지 프로젝트가 financing과 원가를 통과하지 못하면 Green이 아니라 thesis break가 된다는 기준이다. ([Reuters][12])

---

## 7-5. 리튬 가격·공급반응

```text
4C-watch:
lithium_price_reversal
mine_restart_supply_rebound
CAPEX_cut
EV_demand_slowdown
sodium_ion_substitution
```

리튬 가격이 반등해도 폐쇄 광산이 재가동되면 상승폭이 제한될 수 있다. 그래서 리튬은 structural_success가 아니라 `cyclical_success_or_failure`로 우선 분류해야 한다. ([Reuters][8])

---

## 7-6. EV·ESS 안전규제

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

한국의 EV 배터리 인증제 조기 시행과 Moss Landing BESS 화재는 EV·ESS 관련주에 안전·인증·보험·시설 인허가 overlay를 붙여야 한다는 기준이다. ([Reuters][13])

---

## 7-7. Second-life battery / SOH 정보비대칭

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

## 7-8. Graphite supply-chain economics failure

```text
4C-watch:
US_graphite_cost_uncompetitive
policy_financing_absent
offtake_missing
China_price_pressure
CAPEX_burden
```

흑연은 공급망 안보 관점에선 중요하지만, 미국 생산비가 높고 현재 가격에서 경쟁력이 약하다는 분석이 있다. 따라서 `중국 의존도 높음 = 무조건 Green`이 아니라, 정책금융·offtake·원가경로·고객계약을 봐야 한다. ([arXiv][9])

---

# 8. 점수비중 보정표 — R3 Loop 6 / v6.0

| canonical archetype                      | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | Loop 6 핵심 감점                                      |
| ---------------------------------------- | ------: | ---------: | ---------: | ---------: | --------: | ------: | ---: | ------------------------------------------------- |
| `BATTERY_MATERIALS_CAPEX_OVERHEAT`       |      14 |          9 |         11 |          8 |         6 |       0 |    5 | EV 둔화, CAPA 과잉, 계약취소, 광물가격                        |
| `BATTERY_EQUIPMENT_PARTS`                |      18 |         15 |         10 |         11 |         9 |       0 |    5 | 고객사 CAPEX cut, 납품 지연, EV line idle                |
| `ESS_LFP_GRID_STORAGE`                   |      22 |         21 |         15 |         12 |        11 |       0 |    5 | ESS 마진, LFP 경쟁, 고객집중, 보조금                         |
| `ESS_TESLA_MEGAPACK_SUPPLY_CHAIN`        |      23 |         24 |         16 |         13 |        11 |       0 |    6 | Lansing ramp-up, Tesla concentration, ESS OPM 미확인 |
| `ESS_AI_DATA_CENTER_STORAGE`             |      22 |         20 |         16 |         13 |        11 |       0 |    5 | 고객계약 미확인, 데이터센터 CAPEX 지연, 안전규제                    |
| `EV_TO_ESS_CAPACITY_REDEPLOYMENT`        |      18 |         17 |         13 |         12 |         9 |       0 |    5 | EV idle overhang, 전환비용, 계약·마진 미확인                 |
| `EV_BATTERY_JV_RESTRUCTURING`            |      15 |         13 |         10 |         11 |         8 |       0 |    5 | JV 해체, 영업손실, fixed cost, ESS pivot 미검증            |
| `EV_CAPA_CONTRACT_CANCELLATION`          |    gate |       gate |       gate |       gate |      gate |    gate | gate | 계약취소, 고객 EV 전략 후퇴, expected revenue loss          |
| `BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE` |    gate |       gate |       gate |       gate |      gate |    gate | gate | 고객명·계약금액·용도 미공개 시 score cap                       |
| `BATTERY_RECYCLING_ESS_SHIFT`            |      20 |         18 |         14 |         11 |        10 |       0 |    5 | 회수량 부족, SOH 검증, 금속가격, 계약금액 미공개                    |
| `SECOND_LIFE_BATTERY_GRID_STORAGE`       |      18 |         16 |         12 |         11 |         9 |       0 |    5 | SOH 불확실성, 안전성, warranty, 잔존가치                     |
| `BATTERY_SOH_SECOND_LIFE_TRANSPARENCY`   |    gate |       gate |       gate |       gate |      gate |    gate | gate | SOH 신뢰도, second-life 검증, battery passport         |
| `BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY`  |      17 |         15 |         16 |         12 |         9 |       0 |    5 | 미국 생산비, 정책금융 부재, offtake 미확인                      |
| `LITHIUM_ESS_DEMAND_CYCLE`               |   cycle |      cycle |      cycle |      cycle |     cycle |   cycle |    5 | 가격 급락, 광산 재가동, sodium-ion, EV 둔화                  |
| `SODIUM_ION_SUBSTITUTION_OVERLAY`        |    gate |       gate |       gate |       gate |      gate |    gate | gate | 리튬/LFP 가격상한, 저가 ESS 대체                            |
| `SOLID_STATE_COMMERCIALIZATION_LICENSE`  |      12 |         13 |         10 |         12 |         8 |       0 |    5 | 기술조건부, 양산 전, 수율·cost 미확인                          |
| `SPECULATIVE_BATTERY_TECH`               |       6 |          5 |          6 |          8 |         5 |       0 |    4 | 상용화 전, 고객 부재, 양산 전                                |
| `EV_INFRASTRUCTURE`                      |      16 |         13 |          7 |         10 |         8 |       0 |    5 | 이용률 부족, 화재규제, 충전 제한, 보조금 의존                       |
| `EV_FIRE_BESS_SAFETY_OVERLAY`            |    gate |       gate |       gate |       gate |      gate |    gate | gate | EV/BESS 화재, 인증, 리콜, 보험, 시설 규제                     |
| `BESS_SAFETY_PERMITTING`                 |    gate |       gate |       gate |       gate |      gate |    gate | gate | 화재, 대피, 보험, 시설허가, 지역반발                            |
| `HYDROGEN_FUEL_CELL_INFRA`               |      18 |         18 |         12 |         12 |        10 |       0 |    5 | 고객 부재, 가동률, 보조금, 인프라 부족                           |
| `SOLAR_TARIFF_SUPPLYCHAIN`               |      14 |         11 |         11 |          9 |         7 |       0 |    5 | 통관, 관세, UFLPA, FEOC, 공급망 차질                       |
| `RENEWABLE_ENERGY_PROJECT_ECONOMICS`     |      14 |         11 |          9 |          9 |         7 |       0 |    5 | 금리, 원가, 인허가, impairment                           |
| `WASTE_RECYCLING_ENVIRONMENT`            |      18 |         22 |         15 |         13 |        12 |       3 |    5 | 가동률, CAPEX, 금속가격, 규제비용                            |
| `CARBON_CREDIT_CBAM_COMPLIANCE`          |      14 |         17 |         10 |         12 |         8 |       2 |    6 | 제도개편, 가격변동, greenwashing                          |
| `DATA_CENTER_WATER_REUSE_INFRA`          |      16 |         18 |         14 |         12 |        10 |       2 |    5 | 고객 부재, 지역반발, 경제성                                  |

Loop 6에서 핵심 보정은 이거다.

```text
1. ESS_TESLA_MEGAPACK_SUPPLY_CHAIN 점수 상향.
   고객·용도 미공개 계약이 Tesla/Megapack 3로 확인되며 information score가 올라갔다.

2. EV_BATTERY_JV_RESTRUCTURING 추가.
   SK On–Ford JV 해체처럼 EV 수요둔화와 ESS pivot이 동시에 존재하는 복합 case를 분리한다.

3. EV_CAPA_CONTRACT_CANCELLATION gate 강화.
   Ford·Freudenberg 계약취소로 expected revenue loss가 실제화됐기 때문이다.

4. SECOND_LIFE_BATTERY_GRID_STORAGE와 SOH gate 강화.
   SOH 불투명성은 폐배터리·second-life ESS valuation의 핵심 RedTeam이다.

5. BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY 추가.
   중국 의존도는 구조적이지만, 미국 생산비와 정책금융이 따로 검증되어야 한다.

6. LITHIUM_ESS_DEMAND_CYCLE은 점수 유지하되 cycle로 고정.
   ESS 수요는 좋지만 sodium-ion, 광산 재가동, EV 둔화가 가격상한이다.

7. SOLID_STATE_COMMERCIALIZATION_LICENSE 추가.
   license는 Stage 2 후보지만 양산·royalty·차량탑재 전까지 Green 금지.

8. BESS_SAFETY_PERMITTING gate 강화.
   Moss Landing 사례처럼 ESS도 안전·보험·지역수용성 gate를 통과해야 한다.
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

## `ESS_TESLA_MEGAPACK_SUPPLY_CHAIN`

```text
Stage 1:
LFP supply 계약 발표, 고객·용도 미공개

Stage 2:
Tesla/Megapack ESS 용도 확인, 생산공장·생산시점·계약기간 확인

Stage 3:
Lansing ramp-up + Megapack 매출 인식 + ESS OPM + FCF 확인

Stage 4B:
Tesla ESS supply chain narrative 과열

Stage 4C:
Lansing ramp delay, Tesla order cut, LFP ASP 하락, FEOC/관세 변화
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

## `EV_BATTERY_JV_RESTRUCTURING`

```text
Stage 1:
JV 해체, 공장 ownership 변경, EV 수요둔화 뉴스

Stage 2:
고정비 절감, debt reduction, ESS 전환계획, 신규 고객계약 확인

Stage 3:
구조조정 후 ESS/EV mix가 OPM·FCF를 실제 개선할 때

Stage 4B:
ESS pivot narrative 과열

Stage 4C:
EV 수요 추가둔화, 공장 idle 지속, 영업손실 확대, ESS 전환 실패
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

## `BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY`

```text
Stage 1:
중국 graphite/anode 의존도, 수입규제, 공급망 안보 뉴스

Stage 2:
정책금융, offtake, 고객계약, 생산원가 개선 경로 확인

Stage 3:
battery-grade graphite 매출·마진·FCF 확인

Stage 4B:
흑연 공급망 안보 narrative 과열

Stage 4C:
미국 생산비 경쟁력 실패, 고객계약 부재, 보조금 축소, 중국 가격압박
```

## `LITHIUM_ESS_DEMAND_CYCLE`

```text
Stage 1:
리튬 가격 반등, 광산 폐쇄, EV/ESS 수요 뉴스

Stage 2:
저비용 광산, 장기 offtake, FCF 방어 확인

Stage 3:
극히 제한적. 가격 cycle을 넘어선 현금흐름 지속성 필요

Stage 4B:
리튬 가격 반등 기대 과열

Stage 4C:
가격 급락, 광산 재가동, EV 수요 둔화, CAPEX cut, sodium-ion 대체
```

## `SOLID_STATE_COMMERCIALIZATION_LICENSE`

```text
Stage 1:
전고체 sample, 기술발표, 성능 claim

Stage 2:
license, royalty framework, 생산권, OEM partnership 확인

Stage 3:
양산, 고객차종, 매출 인식, royalty revenue, cost/yield 확인

Stage 4B:
전고체 상용화 기대 과열

Stage 4C:
기술조건 미달, 수율 실패, 비용초과, 양산 지연, 고객차종 부재
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

## R3 Loop 6 공통 검증 방식

```text
1. 각 case의 stage1_date, stage2_date, stage3_date를 지정한다.
2. 해당 날짜의 종가를 stage_price로 저장한다.
3. MFE_30D / 90D / 180D / 1Y / 2Y를 계산한다.
4. MAE_30D / 90D / 180D / 1Y를 계산한다.
5. peak_price와 drawdown_after_peak를 계산한다.
6. EV 수요, ESS 계약, 공장 가동률, CAPEX, 광물가격, 보조금/관세,
   화재·인증 이벤트와 가격경로를 비교한다.
```

## Loop 6에서 새로 강제할 판정

```text
EV_CAPA_FALSE_GREEN:
EV CAPA 증설은 있었지만 공장 idle, 계약취소, 수요 둔화가 발생.

EV_CONTRACT_CANCELLATION_4C:
계약공시는 있었지만 고객사의 EV 전략 후퇴로 계약이 취소됨.

EV_JV_RESTRUCTURING_WATCH:
JV 해체·공장 ownership 변경은 구조조정 후보이나 EV demand 4C도 같이 존재.

ESS_CONTRACT_ALIGNED:
ESS 계약금액·기간·고객·GWh가 확인되고 주가·EPS가 동행.

ESS_TESLA_MEGAPACK_ALIGNED:
Tesla/Megapack use-case가 확인되고 생산·매출·OPM으로 연결.

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

GRAPHITE_SECURITY_BUT_COST_RISK:
중국 의존도는 높지만 미국 생산비와 고객계약이 미확인.

SOLID_STATE_LICENSE_NOT_COMMERCIALIZATION:
license는 있지만 양산·수율·royalty·차량탑재 미확인.

SOLAR_POLICY_SUPPLYCHAIN_4C:
보조금·미국공장 narrative가 통관·관세·부품 억류로 깨짐.

WIND_PROJECT_IMPAIRMENT_4C:
원가·금리·일정 지연으로 프로젝트 손상.

LITHIUM_CYCLICAL_SUCCESS_OR_FAILURE:
리튬 가격·광산 폐쇄·재가동·ESS 수요에 따른 cycle 판정.

SODIUM_ION_SUBSTITUTION_WATCH:
저가 ESS/저가 EV에서 sodium-ion이 lithium/LFP 가격상한 역할.

EV_BESS_SAFETY_REGULATORY_OVERLAY:
화재·배터리 인증·시설규제·보험비용을 별도 RedTeam으로 적용.
```

## 이번 R3 Loop 6에서 우선 검증할 가격 case

| case_id                                    | stage2 후보일 | 현재 1차 가격판정                                           |
| ------------------------------------------ | ---------: | ---------------------------------------------------- |
| `lg_energy_lfp_4_3b_contract_initial_case` | 2025-07-30 | $4.3B, 최초 고객·용도 미공개                                  |
| `tesla_lges_megapack3_lansing_case`        | 2026-03-17 | Tesla/Megapack 3 ESS 용도 확인, disclosure cap 일부 해소     |
| `sk_on_flatiron_ess_7_2gwh_case`           | 2025-09-03 | 최대 7.2GWh, 계약금액 미공개                                  |
| `gm_lg_ultium_ohio_idle_case`              | 2026-05-12 | EV CAPA 4C + ESS shift watch                         |
| `sk_on_ford_jv_dissolution_case`           | 2025-12-11 | EV JV restructuring + ESS pivot watch                |
| `ford_lges_ev_contract_cancel_case`        | 2025-12-17 | $6.5B 계약취소, hard 4C                                  |
| `lges_freudenberg_contract_cancel_case`    | 2025-12-26 | 추가 계약취소, expected revenue loss                       |
| `redwood_recycling_energy_storage_case`    | 2025-10-23 | 재활용+ESS+AI DC reference                              |
| `lithium_ess_demand_recovery_case`         | 2026-01-04 | ESS 수요로 리튬 outlook 개선, cycle watch                   |
| `lithium_86pct_crash_mine_restart_case`    | 2025-01-13 | lithium hard cycle counterexample                    |
| `graphite_supply_security_case`            |    2025-03 | graphite supply security + cost risk                 |
| `quantumscape_vw_solid_state_license_case` | 2024-07-11 | solid-state license Stage 2, commercialization watch |
| `qcells_customs_detention_furlough_case`   | 2025-11-08 | 태양광 공급망 hard 4C                                      |
| `orsted_sunrise_wind_impairment_case`      | 2025-01-20 | 풍력 project 4C                                        |
| `korea_ev_battery_certification_fire_case` | 2024-08-25 | EV fire regulatory overlay                           |
| `moss_landing_bess_fire_case`              |    2025-01 | BESS safety/permitting overlay                       |
| `battery_soh_transparency_case`            |    2026-03 | second-life/recycling 정보비대칭 overlay                  |
| `waste_recycling_infra_case`               |      case별 | 허가권·처리량·FCF 확인 전까지 Watch                             |

---

# 11. 다음에 에이전트가 채워야 할 price fields

R3 Loop 6에서는 아래 필드를 채우게 해야 한다.

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
contract_cancellation_reason
expected_revenue_loss
capacity_utilization
capex_amount
capex_to_revenue
capex_cut_flag

ev_battery_jv_restructuring_flag
jv_dissolution_flag
plant_ownership_change
fixed_cost_reduction_flag
operating_loss_amount
debt_reduction_flag
ess_pivot_flag
ess_pivot_revenue_confirmed_flag

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
tesla_megapack_flag
megapack_version
lansing_production_flag
production_start_year
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
graphite_price_change
black_mass_price
metal_recovery_revenue

graphite_supplychain_security_flag
china_graphite_dependency_pct
us_graphite_cost_premium
policy_financing_flag
graphite_offtake_flag
graphite_customer_contract_flag

recycling_volume
recovered_material_volume
recovery_rate
pCAM_output
recycling_customer_contract
second_life_battery_flag
second_life_grid_storage_flag
soh_validation_flag
battery_passport_compliance_flag
battery_grading_cost
residual_capacity_uncertainty_flag
warranty_enforcement_risk_flag

solid_state_license_flag
solid_state_license_capacity_gwh
royalty_structure_flag
mass_production_flag
vehicle_series_adoption_flag
solid_state_yield_signal
solid_state_cost_signal
commercialization_condition_flag

sodium_ion_substitution_flag
sodium_ion_customer_contract_flag
sodium_ion_ess_flag
sodium_ion_price_pressure_flag

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
evacuation_flag
local_opposition_flag

opendart_rcept_no
opendart_detail_fetched_flag
disclosure_confidence_score
detail_parser_confidence
disclosure_signal_class
routine_disclosure_flag
risk_disclosure_flag
high_signal_disclosure_flag

score_price_alignment
price_validation_status
review_notes
```

---

# R3 Loop 6 결론

이번 6회차에서 R3는 더 촘촘해졌다.

```text
Green 가능:
LFP ESS 장기계약이 실제 금액·기간·고객·GWh·마진으로 확인된 기업
Tesla Megapack / hyperscaler / utility storage supply chain이 매출·OPM으로 연결되는 기업
AI 데이터센터 storage 계약과 OPM/FCF가 확인된 기업
폐기물처리 허가권·처리량·반복 FCF가 확인된 기업
재활용 + ESS + 고객계약 + 회수금속 매출이 연결된 기업
수소 CAPEX가 고객·가동률·OPM으로 연결되는 기업
탄소회계·CBAM compliance 반복매출이 확인되는 기업

Watch-to-Green:
2차전지 장비
ESS 전환
EV→ESS 라인 재배치
SK On–Ford류 JV restructuring 후 ESS pivot
폐배터리
second-life ESS
graphite supply-chain security
solid-state license
수소연료전지
데이터센터 물 재활용
EV 인프라 중 실제 이용률·운영수익이 확인된 기업
LGES처럼 고객·용도 확인이 뒤늦게 풀리는 계약형 ESS 후보

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
sodium-ion 대체를 무시한 lithium/LFP 순수 테마
graphite 안보 테마 중 원가·offtake 미확인 기업

Hard 4C:
EV 공장 idle
EV 배터리 계약 취소
EV battery JV 해체 후 수요둔화 노출
expected revenue loss
태양광 통관·관세·부품 억류
풍력 impairment
리튬 가격 급락·공급 재가동
sodium-ion 대체로 인한 lithium/LFP 가격상한
EV/BESS 화재·배터리 인증 규제
BESS facility fire / evacuation / permitting delay
SOH 불확실성으로 인한 second-life/recycling 가치 훼손
계약 detail 부족으로 인한 disclosure confidence cap
```

**R3 Loop 6 점수정규화의 핵심 문장:**

> 2차전지·전기차·친환경은 “EV 성장”, “ESS”, “폐배터리”, “수소”, “태양광”, “풍력”이라는 이름이 아니라 **계약금액, 계약기간, 고객사, GWh, 가동률, ESS OPM, 회수량, 금속 회수 매출, SOH 검증, graphite 원가·offtake, 보조금 의존도, 통관·관세 리스크, 화재·안전규제, FCF 전환, 실제 가격경로**로 봐야 한다.
> Loop 6부터는 특히 `EV_BATTERY_JV_RESTRUCTURING`, `ESS_TESLA_MEGAPACK_SUPPLY_CHAIN`, `EV_CAPA_CONTRACT_CANCELLATION`, `SECOND_LIFE_BATTERY_GRID_STORAGE`, `BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY`, `SOLID_STATE_COMMERCIALIZATION_LICENSE`, `SODIUM_ION_SUBSTITUTION_OVERLAY`, `BESS_SAFETY_PERMITTING`, `DISCLOSURE_CONFIDENCE_CAP`을 강한 보정축으로 넣어야 한다.

다음 순서는 **R4 — 소재·스프레드·전략자원 Loop 6**다.

[1]: https://www.reuters.com/business/energy/us-government-confirms-tesla-lg-energy-solutions-43-billion-battery-deal-2026-03-17/?utm_source=chatgpt.com "US government confirms Tesla and LG Energy Solution's $4.3 billion battery deal"
[2]: https://www.reuters.com/business/energy/south-koreas-sk-signs-ess-battery-supply-deal-with-us-based-flatiron-energy-2025-09-03/?utm_source=chatgpt.com "South Korea's SK On signs ESS battery supply deal with US-based Flatiron Energy"
[3]: https://www.reuters.com/legal/litigation/gms-restart-date-ohio-battery-plant-uncertain-2026-05-12/?utm_source=chatgpt.com "GM-LG's restart date at Ohio battery plant uncertain"
[4]: https://www.reuters.com/business/autos-transportation/south-koreas-sk-ford-motor-end-us-battery-joint-venture-2025-12-11/?utm_source=chatgpt.com "South Korea's SK On, Ford Motor to end US battery joint venture"
[5]: https://www.reuters.com/business/finance/south-koreas-lg-energy-solution-ends-65-billion-ev-battery-supply-deal-with-ford-2025-12-17/?utm_source=chatgpt.com "Ford cancels EV battery deal worth $6.5 billion with South Korea's LG Energy Solution"
[6]: https://www.reuters.com/business/battery-recycling-firm-redwood-raises-350-million-eclipse-ventures-nvidia-2025-10-23/?utm_source=chatgpt.com "Battery recycling firm Redwood raises $350 million from Eclipse Ventures, Nvidia"
[7]: https://www.reuters.com/sustainability/climate-energy/energy-storage-boom-strengthens-demand-outlook-beaten-down-lithium-2026-01-04/?utm_source=chatgpt.com "Energy storage boom strengthens demand outlook for beaten-down lithium"
[8]: https://www.reuters.com/markets/commodities/lithium-prices-stabilise-2025-mine-closures-china-ev-sales-ease-glut-analysts-2025-01-13/?utm_source=chatgpt.com "Lithium prices to stabilise in 2025 as mine closures, China EV sales ease glut, analysts say"
[9]: https://arxiv.org/abs/2503.21521?utm_source=chatgpt.com "Securing the supply of graphite for batteries"
[10]: https://www.reuters.com/business/autos-transportation/volkswagen-ramp-up-solid-state-battery-production-quantumscape-deal-2024-07-11/?utm_source=chatgpt.com "Volkswagen, QuantumScape strike deal on solid-state batteries"
[11]: https://www.reuters.com/sustainability/climate-energy/qcells-furloughs-1000-workers-us-solar-factories-due-stalled-shipments-2025-11-08/?utm_source=chatgpt.com "Qcells furloughs 1,000 workers at US solar factories due to stalled shipments"
[12]: https://www.reuters.com/business/energy/orsted-flags-impairments-about-17-billion-us-rate-increases-2025-01-20/?utm_source=chatgpt.com "Orsted flags $1.7 bln impairment on Sunrise Wind delays, increased costs"
[13]: https://www.reuters.com/business/autos-transportation/south-korea-advance-ev-battery-certification-scheme-after-fires-2024-08-25/?utm_source=chatgpt.com "South Korea to advance EV battery certification scheme after fires"
[14]: https://www.theguardian.com/us-news/2025/jan/17/california-battery-plant-fire-monterey?utm_source=chatgpt.com "Fire reignites at California battery plant after evacuations amid toxic smoke"
[15]: https://arxiv.org/abs/2603.21592?utm_source=chatgpt.com "Battery health reporting fails independent validation across manufacturers"

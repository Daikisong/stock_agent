좋아. **R2 Loop 2까지 끝났으니, 이번은 R3 Loop 2 — 2차전지·전기차·친환경**으로 넘어간다.

이번 2회차 R3의 목표는 1회차보다 훨씬 더 명확해졌다.

```text
EV 배터리 성장주
≠ 무조건 Green

ESS 전환
≠ 자동 Green

폐배터리·재활용
≠ 회수량/마진 전까지 Green

수소·태양광·풍력
≠ 정책·보조금만으로 Green

폐기물처리
= 허가권·처리량·반복 FCF가 있으면 Green 가능
```

R3는 Theme Tag Map 기준으로 2차전지 소재, 부품, 공정장비, 폐배터리, 전고체, 전기차 인프라, 전기차 화재, 수소차 연료전지, 태양광, 풍력, 탄소배출권, 폐기물처리, 탈플라스틱을 흡수하는 대섹터다. 이 지도에서도 2차전지는 Green보다 과열 방어가 우선이고, 소재·전고체·폐배터리는 실제 계약·수익성·FCF 전까지 Stage 3-Green을 제한해야 한다고 정리되어 있다.

그리고 R3에서도 Checkpoint 20 원칙을 그대로 적용해야 한다. 공급계약, 시설투자, 실적 전망 같은 공시는 detail fetch로 계약금액, 계약기간, 매출 대비 계약금액, 투자금액, 완료일, OP YoY 같은 필드가 실제 확인될 때만 증거로 써야 하고, 비어 있는 값은 만들면 안 된다.

서생원식으로 보면 이 라운드의 핵심도 결국 같다. “친환경”이나 “전기차 성장”이 아니라, **EPS/FCF 체급 변화가 지속되고 시장이 아직 과거 프레임으로 오해하는가**를 봐야 한다.

---

# R3 Loop 2. 2차전지·전기차·친환경

## 1. 이번 라운드 대섹터

```text
R3 = 2차전지·전기차·친환경
Loop 2 목표 = EV 성장 narrative와 실제 FCF 구조를 분리
```

이번 회차의 핵심 질문은 이거다.

```text
이 기업은 EV 성장 테마인가?
아니면 EV 둔화 속에서도 ESS, 재활용, 폐기물처리, 수소, 탄소회계 등으로
반복 FCF를 만들 수 있는 구조인가?
```

R3에서 점수를 잘못 주는 가장 흔한 실수는 아래 네 가지다.

```text
1. EV 수요 둔화를 무시하고 CAPA 증설을 Green으로 처리
2. ESS 전환 뉴스를 실제 수익성 검증 없이 Green으로 처리
3. 폐배터리·전고체·수소·태양광을 정책 테마만으로 Green 처리
4. 리튬·니켈·태양광·풍력의 가격/보조금 사이클을 구조적 성공으로 착각
```

---

## 2. 대상 canonical archetype

| canonical archetype                | Loop 2 정책                              |
| ---------------------------------- | -------------------------------------- |
| `BATTERY_MATERIALS_CAPEX_OVERHEAT` | Watch/Red. EV 수요·CAPA·광물가격 감점 강화       |
| `BATTERY_EQUIPMENT_PARTS`          | Watch-to-Green. 고객사 CAPEX와 실제 납품 필요    |
| `BATTERY_RECYCLING_ESS_SHIFT`      | Watch-to-Green. ESS 계약·회수량·금속 회수 수익 필요 |
| `EV_INFRASTRUCTURE`                | Watch. 충전소 이용률·수익성·화재규제 확인             |
| `HYDROGEN_FUEL_CELL_INFRA`         | Watch-to-Green. 실제 CAPEX·고객·가동률 필요     |
| `SOLAR_TARIFF_SUPPLYCHAIN`         | Watch/Red. 보조금·관세·통관 리스크 강함            |
| `RENEWABLE_ENERGY_POLICY`          | Watch/Red. 풍력은 원가·금리·인허가 4C 가능         |
| `ENERGY_DISTRIBUTION_FUEL`         | Watch. 에너지 가격·재고손익·정책 리스크              |
| `WASTE_RECYCLING_ENVIRONMENT`      | Green 가능. 허가권·처리량·반복 FCF 필요            |
| `CARBON_CREDIT_CBAM_COMPLIANCE`    | Watch. 탄소가격보다 비용전가·탄소회계 매출 필요          |
| `DATA_CENTER_WATER_REUSE_INFRA`    | Watch-to-Green. 데이터센터 물 재활용 계약 필요      |
| `EV_FIRE_RISK_OVERLAY`             | RedTeam overlay. 화재·리콜·인증·보험 리스크       |

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
- EV 수요 둔화
- 고객사 계약 취소
- 광물가격 하락

BATTERY_EQUIPMENT_PARTS
- 셀 공정장비
- 2차전지 장비
- 2차전지 부품
- 고객사 CAPEX
- 납품 스케줄
- 장비 수주잔고

BATTERY_RECYCLING_ESS_SHIFT
- ESS
- LFP ESS
- EV 라인 → ESS 전환
- 폐배터리
- second-life battery
- black mass
- pCAM
- 금속 회수 수익
- 회수량

EV_INFRASTRUCTURE
- 충전소
- 충전기
- 초급속 충전
- 이용률
- 전기차 화재
- 배터리 인증
- 주차장 규제

HYDROGEN_FUEL_CELL_INFRA
- 수소연료전지
- 수소차 인프라
- 전해조
- 상용차
- 버스
- 건설기계
- 선박
- 수소 트램

SOLAR_TARIFF_SUPPLYCHAIN
- 태양광 모듈
- 태양광 셀
- 미국 공장
- 중국 공급망
- UFLPA 통관
- 보조금
- FEOC
- 관세

RENEWABLE_ENERGY_POLICY
- 풍력
- 해상풍력
- 프로젝트 financing
- monopile foundation
- 인허가
- impairment
- 금리

WASTE_RECYCLING_ENVIRONMENT
- 폐기물처리
- 플라스틱 재활용
- 폐기물 에너지화
- 허가권
- 처리량
- 반복 FCF
- M&A 프리미엄

CARBON_CREDIT_CBAM_COMPLIANCE
- EU ETS
- CBAM
- 탄소회계
- 탄소검증
- 저탄소 제품 premium
- 비용전가

DATA_CENTER_WATER_REUSE_INFRA
- AI 데이터센터 물 사용
- 수처리
- water reuse
- closed-loop cooling
- 지역 반발
- permitting
```

---

# 4. 성공사례

## 4-1. LG에너지솔루션 ESS 전환 — `BATTERY_RECYCLING_ESS_SHIFT`

LG에너지솔루션은 EV 배터리 수요 둔화와 미국 관세·보조금 종료 리스크를 경고하면서, ESS 배터리 생산 확대를 대응축으로 제시했다. 회사는 미국 일부 EV 배터리 라인의 ESS 전환을 검토하고 있고, 미시간 공장에서 LFP 배터리 생산을 시작했으며, ESS 생산능력을 2025년 17GWh에서 2026년 30GWh 이상으로 늘리겠다고 밝혔다. 다만 같은 날 LGES 주가는 1.6% 하락했고, Q2 영업이익 4,920억 원도 IRA 세액공제를 제외하면 14억 원에 그쳤다. ([Reuters][1])

**가격경로 1차 판정**

```text
가격 반응:
발표 후 -1.6%

판정:
ESS_shift_candidate_but_EV_slowdown_overhang

의미:
ESS 전환은 확실히 Stage 1~2 후보.
하지만 시장은 EV 둔화와 보조금 의존도를 더 크게 봤다.
```

**Loop 2 교정**

```text
ESS 전환:
점수 강화 가능.

단, Green 조건:
- ESS 고객계약
- LFP ESS 생산 가동률
- ESS OPM
- full-system sale margin
- IRA credit 제외 후 수익성

EV 라인 전환 뉴스만으로 Stage 3 금지.
```

---

## 4-2. LGES–Tesla LFP ESS 공급계약 — ESS가 EV 둔화의 대안이 될 수 있는 강한 Stage 2 후보

LG에너지솔루션은 Tesla로 알려진 고객과 43억 달러 규모 LFP 배터리 공급계약을 맺었고, 계약 기간은 2027년 8월부터 2030년 7월까지 3년이며, 최대 7년 연장 옵션도 포함되어 있다. 배터리는 Tesla의 energy-storage systems용으로 미국 공장에서 생산될 것으로 보도됐고, LGES 주가는 해당 보도에서 0.6% 상승했다. ([The Wall Street Journal][2])

**가격경로 1차 판정**

```text
가격 반응:
+0.6%

판정:
ESS_contract_stage2_candidate

의미:
이건 단순 ESS narrative가 아니라 계약금액·기간·고객·용도가 있는 Stage 2 후보.
다만 주가 반응은 크지 않으므로 180D/1Y MFE 확인 필요.
```

**Loop 2 교정**

```text
BATTERY_RECYCLING_ESS_SHIFT 점수 강화 조건:
- contract_value 확인
- contract_duration 확인
- 고객사 확인
- ESS용 생산라인 확인
- 매출 인식 시점 확인
- EV용 대비 OPM 비교
```

---

## 4-3. SK On–Flatiron ESS 공급계약 — `BATTERY_RECYCLING_ESS_SHIFT`

SK On은 미국 Flatiron Energy Development에 ESS용 LFP 배터리를 최대 7.2GWh 공급하기로 했고, 공급 기간은 2026~2030년이다. SK On은 2026년 하반기 ESS 전용 LFP 배터리 양산을 시작할 계획이며, 일부 미국 EV 배터리 라인을 ESS 제조용으로 전환할 예정이다. ([Reuters][3])

**가격경로 1차 판정**

```text
판정:
ESS_contract_stage2_candidate

좋은 점:
- 최대 7.2GWh
- 2026~2030년 공급기간
- ESS 전용 LFP 양산 계획
- EV 라인 전환

주의:
- 계약금액 미공개
- OPM/FCF 미확인
- 고객사 수요 지속성 확인 필요
```

**Loop 2 교정**

```text
SK On류 ESS 계약은 Stage 2 후보.
하지만 계약금액이 없으면 score cap을 둬야 한다.

contract_value_missing = true이면:
EPS/FCF 점수 상한 제한.
```

---

## 4-4. Redwood Materials — 폐배터리·ESS·AI 데이터센터 전력수요 교차 후보

Redwood Materials는 Eclipse Ventures와 Nvidia 투자부문 NVentures가 참여한 라운드에서 3.5억 달러를 조달했고, 배터리 재활용으로 lithium, cobalt, nickel, copper 등을 회수하며 grid services와 데이터센터용 energy storage systems도 제공한다. Redwood는 Volkswagen, Panasonic, Toyota, Lyft 등과 파트너십을 갖고 있고, 이번 자금은 energy storage operations와 materials production 확장에 쓰일 예정이다. ([Reuters][4])

**가격경로 1차 판정**

```text
판정:
battery_recycling_energy_storage_success_reference

의미:
폐배터리·재활용이 단순 테마에서 벗어나려면
실제 회수 소재, 고객사, ESS 활용, 데이터센터 전력 수요가 연결되어야 한다.

주의:
비상장 reference.
한국 상장주 매핑 시 회수량·매출·마진 확인 필수.
```

**Loop 2 교정**

```text
BATTERY_RECYCLING_ESS_SHIFT:
폐배터리 단독이면 Watch.
폐배터리 + ESS + 고객계약 + 회수소재 매출이면 Watch-to-Green.
```

---

## 4-5. 현대차 울산 수소연료전지 공장 — `HYDROGEN_FUEL_CELL_INFRA`

현대차는 울산에 9,300억 원, 약 6.54억 달러 규모의 수소연료전지 생산시설을 착공했다. 이 공장은 2027년 완공 예정이며 승용차, 상용 트럭·버스, 건설장비, 선박용 연료전지와 전해조를 생산할 예정이다. ([Reuters][5])

**가격경로 1차 판정**

```text
판정:
hydrogen_capex_stage1_to_stage2_candidate

좋은 점:
- 실제 CAPEX
- 완공 예정일
- 연료전지·전해조 생산
- 상용차·선박·건설기계 응용

주의:
- 고객사·가동률·OP 전환 확인 필요
- 수소차 인프라 부족
- 보조금 의존도 확인 필요
```

**Loop 2 교정**

```text
HYDROGEN_FUEL_CELL_INFRA:
정책 뉴스만 있으면 Watch.
실제 공장 착공은 Stage 1.5~2.
고객·가동률·매출 전까지 Green 금지.
```

---

## 4-6. 폐기물처리 플랫폼 — `WASTE_RECYCLING_ENVIRONMENT`

EQT는 한국 KJ Environment와 계열사를 인수해 폐기물 처리 플랫폼을 만들기로 했고, 이 플랫폼은 플라스틱 재활용, 폐기물 에너지화, 재활용 폐기물 선별을 포함한다. Reuters는 이 플랫폼의 기업가치가 1조 원, 약 7.33억 달러 이상이며 수도권을 중심으로 한국 인구 절반 이상을 커버할 수 있다고 보도했다. ([Reuters][6])

**가격경로 1차 판정**

```text
판정:
waste_platform_structural_success_reference

의미:
R3에서 드물게 Green 가능성이 높은 축.
폐기물처리는 허가권·처리시설·반복 FCF가 핵심.
```

**Loop 2 교정**

```text
WASTE_RECYCLING_ENVIRONMENT:
Green 가능 유지.

단, 폐배터리·재활용 테마와 구분:
- 폐기물처리 허가권/처리량/FCF = Green 가능
- 폐배터리 테마/금속 회수 계획 = Watch
```

---

# 5. 반례

## 5-1. GM–LG Ultium Ohio 공장 재가동 불확실 — EV CAPA thesis 4C

GM과 LG에너지솔루션의 합작사 Ultium Cells는 Ohio EV 배터리 공장의 완전 재가동 일정을 확정하지 못한 상태다. 이 공장은 EV 수요 약화로 2026년 1월부터 6개월간 가동이 중단됐고, 약 850명이 일시 해고 상태였으며, 회사는 5월 말 소수 인력만 복귀시킬 예정이라고 밝혔다. Tennessee 공장 쪽은 EV 대신 ESS용 배터리 셀 생산으로 전환하는 흐름도 보도됐다. ([Reuters][7])

**가격경로 1차 판정**

```text
판정:
EV_CAPA_THESIS_4C + ESS_shift_watch

의미:
EV 배터리 공장 CAPA는 Green이 아니라 risk가 될 수 있다.
ESS 전환은 후보지만, EV 공장 idle은 hard 4C에 가깝다.
```

**Loop 2 교정**

```text
BATTERY_MATERIALS_CAPEX_OVERHEAT:
risk penalty 강화.

CAPA 증설 뉴스는:
고객 수요
가동률
OPM
FCF
없으면 점수 제한.
```

---

## 5-2. Ford–LGES 65억 달러 EV 배터리 계약 취소 — `BATTERY_MATERIALS_CAPEX_OVERHEAT`

Ford는 LG에너지솔루션과의 약 65억 달러 규모 EV 배터리 공급계약을 취소했다. Reuters는 Ford가 EV 모델 일부를 중단하고 195억 달러 규모 write-down을 발표했으며, EV 수요 전망 변화와 정책 변화가 계약 취소의 배경이라고 보도했다. Ford는 SK On과의 미국 배터리 합작도 종료한 상태다. ([Reuters][8])

**가격경로 1차 판정**

```text
판정:
EV_battery_contract_cancellation_4C

의미:
EV 배터리 장기공급계약도 취소될 수 있다.
R3에서 계약은 반드시 취소 가능성·고객사 EV 전략·정책 리스크와 같이 봐야 한다.
```

**Loop 2 교정**

```text
계약 점수 강화 조건:
- 취소불가 조항
- 고객사 생산계획 유지
- 보조금/관세 리스크 낮음
- line utilization 확인

계약 취소 발생 시:
Stage 4C.
```

---

## 5-3. Qcells 통관·부품 억류 — `SOLAR_TARIFF_SUPPLYCHAIN`

Qcells는 미국 조지아 공장에서 약 1,000명의 직원에게 furlough를 실시했다. 이유는 해외 부품 선적이 미국 세관에서 반복적으로 지연됐기 때문이다. 일부 부품은 중국 신장 관련 강제노동방지법에 따라 항구에서 억류됐고, 회사는 Cartersville과 Dalton 공장의 약 절반 제조 인력에 임시 단축근무와 furlough를 적용했으며, 300명가량의 staffing agency workers도 감축했다. ([Reuters][9])

**가격경로 1차 판정**

```text
판정:
solar_supply_chain_4C

의미:
태양광은 보조금·미국공장 narrative가 있어도
통관·관세·부품 공급망이 바로 생산차질로 연결될 수 있다.
```

**Loop 2 교정**

```text
SOLAR_TARIFF_SUPPLYCHAIN:
Green 매우 제한.
관세·통관·UFLPA·FEOC flag가 있으면 RedTeam 우선.
```

---

## 5-4. Ørsted Sunrise Wind impairment — `RENEWABLE_ENERGY_POLICY`

Ørsted는 Sunrise Wind 프로젝트 지연과 비용 상승, 미국 financing cost 증가로 약 17억 달러 impairment를 발표했다. Sunrise Wind는 2027년 하반기 가동 예정으로 밀렸고, monopile foundation 비용 증가가 주요 원인으로 언급됐다. ([Reuters][10])

**가격경로 1차 판정**

```text
판정:
offshore_wind_project_4C

의미:
풍력은 정책·PPA·친환경 수요가 있어도
금리, 원가, foundation, 인허가, 일정 지연이 thesis를 깨뜨릴 수 있다.
```

**Loop 2 교정**

```text
RENEWABLE_ENERGY_POLICY:
수주/정책만으로 Green 금지.
프로젝트 economics와 financing cost가 핵심.
```

---

## 5-5. 리튬 가격 86% 급락과 광산 재가동 리스크 — `LITHIUM_BATTERY_RAW_MATERIAL`

리튬 가격은 2022년 11월 고점 이후 약 86% 하락했고, 이로 인해 전 세계 광산 폐쇄가 발생했다. 2025년에는 폐쇄 광산과 중국 EV 판매가 공급과잉을 흡수하며 가격 안정 가능성이 제기됐지만, 가격이 오르면 닫혔던 광산이 재가동되어 상승폭을 제한할 수 있다는 분석도 있었다. ([Reuters][11])

**가격경로 1차 판정**

```text
판정:
lithium_cycle_hard_counterexample

의미:
리튬 가격 반등은 구조적 Green이 아니다.
저비용 구조·장기 offtake·FCF 방어가 없으면 Watch/Red.
```

---

## 5-6. Albemarle cost-cut survival — 리튬 반등이 아니라 비용절감 생존

Albemarle은 리튬 가격 하락 속에서도 비용절감으로 분기 흑자전환했지만, Energy Storage 부문 매출은 리튬 가격 53% 하락 때문에 11억 달러 줄었다. 회사는 2025년 CAPEX를 전년의 절반 수준인 7억~8억 달러로 낮추기로 했고, 주가는 시간외에서 2.5% 올랐다. ([Reuters][12])

**가격경로 1차 판정**

```text
가격 반응:
시간외 +2.5%

판정:
cost_cut_cyclical_survival

의미:
리튬 업체의 주가 반응은 가능하지만,
이건 구조적 Green이 아니라 cost-cut/cycle survival에 가깝다.
```

---

## 5-7. EV 화재·배터리 인증 — `EV_FIRE_RISK_OVERLAY`

한국 정부는 EV 화재 우려 이후 배터리 인증제 시행을 앞당기기로 했고, 완성차 업체가 차량에 사용한 배터리 정보를 공개하도록 하는 조치도 추진했다. 2024년 8월 전기차 화재로 수백 대 차량이 손상된 이후 대중 우려가 커졌고, 지하주차장 충전시설 스프링클러, 과충전 방지 충전기 확대 같은 안전대책도 논의됐다. ([Reuters][13])

**가격경로 1차 판정**

```text
판정:
EV_fire_regulatory_overlay

의미:
전기차 화재는 개별 배터리·충전·ESS 관련주에 hard RedTeam으로 붙여야 한다.
수요 둔화와 규제비용을 동시에 만들 수 있다.
```

---

# 6. 4B-watch 사례

## 6-1. ESS 전환 4B-watch

```text
4B 조건:
- EV 둔화에도 ESS 전환 narrative로 배터리주 동반 상승
- 실제 ESS 계약금액·마진·가동률 확인 전 가격이 먼저 감
- LFP ESS 경쟁과 보조금 의존을 시장이 무시
```

LGES의 ESS 생산능력 확대와 Tesla ESS 계약은 좋은 Stage 2 후보지만, 발표 직후 LGES 주가는 EV 둔화 우려로 하락했다. 이는 시장이 아직 ESS 전환을 완전한 Green으로 인정하지 않았다는 신호다. ([Reuters][1])

---

## 6-2. 폐배터리·재활용 4B-watch

```text
4B 조건:
- battery recycling과 critical minerals narrative가 과밀
- 회수량·금속 회수율·마진 없이 valuation 상승
- AI 데이터센터 ESS와 연결한다는 말만 있고 실제 수익화 없음
```

Redwood는 좋은 reference지만, 비상장이고 대형 고객·자금조달·ESS 확장에도 불구하고 한국 상장사로 매핑하려면 회수량, 고객, 매출, 마진을 다시 확인해야 한다. ([Reuters][4])

---

## 6-3. 수소 CAPEX 4B-watch

```text
4B 조건:
- 수소 공장 착공 뉴스만으로 관련주 동반 급등
- 고객·가동률·OP 전환 전 가격이 먼저 감
- 보조금·수소충전소 부족 리스크를 무시
```

현대차 울산 공장은 실제 CAPEX라는 점에서 좋지만, 2027년 완공 후 수요처와 가동률이 확인되기 전까지 Stage 3-Green은 제한된다. ([Reuters][5])

---

## 6-4. 태양광 미국 제조 4B-watch

```text
4B 조건:
- 미국 제조·보조금 narrative로 주가 상승
- 실제 부품 공급망·통관 리스크를 시장이 무시
- 중국 공급망 배제가 생산 차질로 이어지는지 확인하지 않음
```

Qcells 사례는 미국 제조 투자가 있어도 통관·부품 억류 하나로 생산차질이 날 수 있다는 기준 반례다. ([Reuters][9])

---

## 6-5. 풍력 PPA·정책 4B-watch

```text
4B 조건:
- PPA·정부정책·탈탄소 수요로 관련주 급등
- foundation cost, financing cost, project delay를 무시
```

Ørsted의 Sunrise Wind impairment는 해상풍력 프로젝트가 정책 수혜에도 불구하고 4C로 갈 수 있음을 보여준다. ([Reuters][10])

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
```

Ultium Ohio 공장 재가동 불확실성과 Ford–LGES 65억 달러 계약 취소는 EV 배터리 CAPA thesis의 대표 4C다. ([Reuters][7])

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

Qcells의 1,000명 furlough와 300명 contractor 감축은 `SOLAR_TARIFF_SUPPLYCHAIN`의 hard 4C다. ([Reuters][9])

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

## 7-4. 리튬 가격 급락·CAPEX 축소

```text
4C:
lithium_price_crash
mine_shutdown
capex_cut
revenue_drop
supply_rebound
```

리튬 가격 86% 급락과 Albemarle의 2025년 CAPEX 절반 축소는 리튬 원재료 archetype을 구조적 Green이 아니라 cycle/Watch로 둬야 하는 핵심 근거다. ([Reuters][11])

---

## 7-5. EV 화재·배터리 인증 리스크

```text
4C-watch:
battery_fire
certification_requirement
battery_supplier_disclosure
insurance_cost
parking/charging regulation
recall_risk
```

한국의 EV 배터리 인증제 조기 시행은 EV 배터리와 충전 인프라에 안전·규제 overlay를 붙여야 한다는 기준이다. ([Reuters][13])

---

# 8. 점수비중 보정표 — R3 Loop 2 / v2.0

| canonical archetype                | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | Loop 2 핵심 감점                |
| ---------------------------------- | ------: | ---------: | ---------: | ---------: | --------: | ------: | ---: | --------------------------- |
| `BATTERY_MATERIALS_CAPEX_OVERHEAT` |      18 |         13 |         12 |          9 |         8 |       0 |    5 | EV 둔화, CAPA 과잉, 계약 취소, 광물가격 |
| `BATTERY_EQUIPMENT_PARTS`          |      19 |         16 |         11 |         11 |         9 |       0 |    5 | 고객사 CAPEX cut, 납품 지연        |
| `BATTERY_RECYCLING_ESS_SHIFT`      |      21 |         18 |         14 |         11 |        10 |       0 |    5 | ESS 마진, 회수량 부족, 계약금액 미공개    |
| `EV_INFRASTRUCTURE`                |      16 |         13 |          7 |         10 |         8 |       0 |    5 | 이용률 부족, 화재규제, 보조금 의존        |
| `HYDROGEN_FUEL_CELL_INFRA`         |      18 |         18 |         12 |         12 |        10 |       0 |    5 | 고객 부재, 가동률, 보조금 의존          |
| `SOLAR_TARIFF_SUPPLYCHAIN`         |      17 |         14 |         11 |         10 |         8 |       0 |    5 | 통관, 관세, UFLPA, 공급망 차질       |
| `RENEWABLE_ENERGY_POLICY`          |      17 |         14 |          9 |         10 |         8 |       0 |    5 | 금리, 원가, 인허가, impairment     |
| `ENERGY_DISTRIBUTION_FUEL`         |      18 |         15 |         16 |         10 |        10 |       2 |    5 | 에너지 가격, 재고손익, 정책            |
| `WASTE_RECYCLING_ENVIRONMENT`      |      18 |         22 |         15 |         13 |        12 |       3 |    5 | 가동률, CAPEX, 금속가격            |
| `CARBON_CREDIT_CBAM_COMPLIANCE`    |      14 |         17 |         10 |         12 |         8 |       2 |    6 | 정책개편, 가격변동, greenwashing    |
| `DATA_CENTER_WATER_REUSE_INFRA`    |      16 |         18 |         14 |         12 |        10 |       2 |    5 | 고객 부재, 지역반발, 경제성            |
| `EV_FIRE_RISK_OVERLAY`             |    gate |       gate |       gate |       gate |      gate |    gate | gate | 화재, 인증, 리콜, 규제, 보험비용        |

Loop 2의 핵심 보정은 이거다.

```text
1. 2차전지 소재 점수 하향.
   EV 둔화·계약취소·CAPA 과잉이 더 분명해졌기 때문.

2. ESS 전환 점수 상향.
   LGES–Tesla, SK On–Flatiron처럼 실제 계약/기간이 붙은 사례가 나왔기 때문.

3. 태양광·풍력 점수 하향.
   Qcells 통관·Ørsted impairment가 강한 4C를 제공했기 때문.

4. 폐기물처리 Green 가능 유지.
   허가권·처리시설·반복 FCF가 있는 인프라형 사업이기 때문.

5. EV fire overlay 강화.
   배터리 인증·공급사 공개·충전시설 규제가 실제 제도화되고 있기 때문.
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

## `BATTERY_RECYCLING_ESS_SHIFT`

```text
Stage 1:
ESS 전환, 폐배터리, LFP ESS 생산 뉴스

Stage 2:
ESS 고객계약, 계약금액, 계약기간, 회수량, 금속 회수 수익 확인

Stage 3:
ESS/재활용 매출이 반복 FCF로 이어질 때만

Stage 4B:
ESS narrative 과열, recycling premium 과열

Stage 4C:
회수량 부족, 금속가격 하락, ESS 마진 부진, 고객사 수요 둔화
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

## `RENEWABLE_ENERGY_POLICY`

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
가동률 하락, CAPEX 부담, 금속가격 하락
```

---

# 10. 가격경로 검증계획

## R3 Loop 2 공통 검증 방식

```text
1. 각 case의 stage1_date, stage2_date, stage3_date를 지정한다.
2. 해당 날짜의 종가를 stage_price로 저장한다.
3. MFE_30D / 90D / 180D / 1Y / 2Y를 계산한다.
4. MAE_30D / 90D / 180D / 1Y를 계산한다.
5. peak_price와 drawdown_after_peak를 계산한다.
6. EV 수요, ESS 계약, 공장 가동률, CAPEX, 광물가격, 보조금/관세 이벤트와 가격경로를 비교한다.
```

## Loop 2에서 새로 강제할 판정

```text
EV_CAPA_FALSE_GREEN:
EV CAPA 증설은 있었지만 공장 idle, 계약취소, 수요 둔화가 발생.

ESS_CONTRACT_ALIGNED:
ESS 계약금액·기간·고객이 확인되고 주가·EPS가 동행.

ESS_SHIFT_BUT_PRICE_FAILED:
ESS 전환 근거는 있으나 EV 둔화가 주가를 누름.

RECYCLING_INFRA_SUCCESS:
허가권·처리량·반복 FCF가 확인된 폐기물/재활용 사업.

SOLAR_POLICY_SUPPLYCHAIN_4C:
보조금·미국공장 narrative가 통관·관세·부품 억류로 깨짐.

WIND_PROJECT_IMPAIRMENT_4C:
원가·금리·일정 지연으로 프로젝트 손상.

LITHIUM_CYCLICAL_SUCCESS_OR_FAILURE:
리튬 가격·광산 폐쇄·재가동에 따른 cycle 판정.

EV_FIRE_REGULATORY_OVERLAY:
화재·배터리 인증·리콜·보험비용을 별도 RedTeam으로 적용.
```

## 이번 R3 Loop 2에서 우선 검증할 가격 case

| case_id                                    | stage2 후보일 | 현재 1차 가격판정                           |
| ------------------------------------------ | ---------: | ------------------------------------ |
| `lg_energy_solution_ess_shift_case`        | 2025-07-25 | 발표 후 -1.6%, ESS 후보지만 EV overhang     |
| `lg_energy_tesla_lfp_ess_contract_case`    | 2025-07-30 | +0.6%, ESS Stage 2 후보                |
| `sk_on_flatiron_ess_7_2gwh_case`           | 2025-09-03 | ESS 계약 후보, 계약금액 미공개                  |
| `gm_lg_ultium_ohio_idle_case`              | 2026-05-12 | EV CAPA 4C + ESS shift watch         |
| `ford_lges_ev_contract_cancel_case`        | 2025-12-17 | $6.5B 계약취소, hard 4C                  |
| `redwood_recycling_energy_storage_case`    | 2025-10-23 | 재활용+ESS success reference            |
| `hyundai_hydrogen_fuel_cell_plant_case`    | 2025-10-30 | 수소 CAPEX Stage 1~2 후보                |
| `eqt_kj_environment_waste_platform_case`   | 2024-08-16 | 폐기물 Green reference                  |
| `qcells_customs_detention_furlough_case`   | 2025-11-08 | 태양광 공급망 hard 4C                      |
| `orsted_sunrise_wind_impairment_case`      | 2025-01-20 | 풍력 project 4C                        |
| `lithium_price_86pct_crash_case`           | 2025-01-13 | 리튬 cycle hard counterexample         |
| `albemarle_cost_cut_low_lithium_case`      | 2025-02-12 | +2.5% after-hours, cost-cut survival |
| `korea_ev_battery_certification_fire_case` | 2024-08-25 | EV fire regulatory overlay           |

---

# 11. 다음에 에이전트가 채워야 할 price fields

R3 Loop 2에서는 아래 필드를 채우게 해야 한다.

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
ess_contract_volume_gwh
ess_capacity_gwh
ess_capacity_utilization
ess_margin
ess_revenue_growth
lfp_ess_flag

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
pCAM_output
recycling_customer_contract
waste_treatment_volume
waste_treatment_capacity
permit_asset_flag
recurring_fcf_flag

hydrogen_capex_amount
hydrogen_plant_completion_date
fuel_cell_capacity
electrolyzer_capacity
hydrogen_customer_contract
hydrogen_subsidy_dependency

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

carbon_credit_price
cbam_exposure
carbon_accounting_revenue
pass_through_ability

ev_fire_event_flag
battery_certification_flag
battery_supplier_disclosure_flag
recall_flag
insurance_cost_change

score_price_alignment
price_validation_status
review_notes
```

---

# R3 Loop 2 결론

이번 2회차에서 R3는 훨씬 더 분명해졌다.

```text
Green 가능:
폐기물처리
ESS 계약이 실제로 붙은 LFP ESS
재활용+ESS+고객계약이 결합된 구조
일부 수소 CAPEX가 고객·가동률까지 연결되는 경우
탄소회계·CBAM compliance 반복매출

Watch-to-Green:
2차전지 장비
ESS 전환
폐배터리
수소연료전지
데이터센터 물 재활용

Watch/Red:
2차전지 소재 CAPA 과열
EV 충전 인프라
태양광
풍력
리튬 원재료
전고체 배터리

Hard 4C:
EV 공장 idle
EV 배터리 계약 취소
태양광 통관·관세·부품 억류
풍력 impairment
리튬 가격 급락
EV 화재·배터리 인증 규제
```

**R3 Loop 2 점수정규화의 핵심 문장:**

> 2차전지·전기차·친환경은 “EV 성장”이나 “친환경 정책”이 아니라 **계약금액, 계약기간, 가동률, ESS 전환 수익성, 회수량, 금속 회수 매출, 보조금 의존도, 통관·관세 리스크, FCF 전환**으로 봐야 한다.
> EV CAPA와 광물가격은 쉽게 4C로 바뀌고, ESS·폐기물·재활용은 실제 계약과 반복 FCF가 붙을 때만 Green 후보가 된다.

다음에 같은 지시가 오면 순서대로 **R4 — 소재·스프레드·전략자원 Loop 2**로 넘어간다.

[1]: https://www.reuters.com/business/autos-transportation/lg-energy-solution-warns-slowing-ev-battery-demand-due-us-tariffs-policy-2025-07-25/?utm_source=chatgpt.com "LG Energy Solution warns of slowing EV battery demand due to U.S. tariffs, policy headwinds"
[2]: https://www.wsj.com/business/autos/lg-energy-clinches-4-3-billion-battery-deal-with-tesla-45c6e45c?utm_source=chatgpt.com "LG Energy Clinches $4.3 Billion Battery Deal With Tesla"
[3]: https://www.reuters.com/business/energy/south-koreas-sk-signs-ess-battery-supply-deal-with-us-based-flatiron-energy-2025-09-03/?utm_source=chatgpt.com "South Korea's SK On signs ESS battery supply deal with US-based Flatiron Energy"
[4]: https://www.reuters.com/business/battery-recycling-firm-redwood-raises-350-million-eclipse-ventures-nvidia-2025-10-23/?utm_source=chatgpt.com "Battery recycling firm Redwood raises $350 million from Eclipse Ventures, Nvidia"
[5]: https://www.reuters.com/world/asia-pacific/hyundai-motor-breaks-ground-680-million-hydrogen-fuel-cell-plant-south-korea-2025-10-30/?utm_source=chatgpt.com "Hyundai Motor breaks ground on $680 million hydrogen fuel cell plant in South Korea"
[6]: https://www.reuters.com/markets/deals/eqt-strikes-deal-acquire-south-korean-waste-treatment-platform-2024-08-16/?utm_source=chatgpt.com "EQT strikes deal to acquire South Korean waste treatment platform"
[7]: https://www.reuters.com/legal/litigation/gms-restart-date-ohio-battery-plant-uncertain-2026-05-12/?utm_source=chatgpt.com "GM-LG's restart date at Ohio battery plant uncertain"
[8]: https://www.reuters.com/business/finance/south-koreas-lg-energy-solution-ends-65-billion-ev-battery-supply-deal-with-ford-2025-12-17/?utm_source=chatgpt.com "Ford cancels EV battery deal worth $6.5 billion with South Korea's LG Energy Solution"
[9]: https://www.reuters.com/sustainability/climate-energy/qcells-furloughs-1000-workers-us-solar-factories-due-stalled-shipments-2025-11-08/?utm_source=chatgpt.com "Qcells furloughs 1,000 workers at US solar factories due to stalled shipments"
[10]: https://www.reuters.com/business/energy/orsted-flags-impairments-about-17-billion-us-rate-increases-2025-01-20/?utm_source=chatgpt.com "Orsted flags $1.7 bln impairment on Sunrise Wind delays, increased costs"
[11]: https://www.reuters.com/markets/commodities/lithium-prices-stabilise-2025-mine-closures-china-ev-sales-ease-glut-analysts-2025-01-13/?utm_source=chatgpt.com "Lithium prices to stabilise in 2025 as mine closures, China EV sales ease glut, analysts say"
[12]: https://www.reuters.com/markets/commodities/albemarle-swings-quarterly-profit-cost-cuts-offset-lithium-price-drop-2025-02-12/?utm_source=chatgpt.com "Cost cuts help Albemarle's results offset low lithium prices"
[13]: https://www.reuters.com/business/autos-transportation/south-korea-advance-ev-battery-certification-scheme-after-fires-2024-08-25/?utm_source=chatgpt.com "South Korea to advance EV battery certification scheme after fires"

순서상 이번은 **R10 Loop 8 — 건설·부동산·건자재 가격경로 검증 라운드**다.

이번 라운드도 원시 수정주가 일봉 OHLC를 안정적으로 직접 추출하지 못한 종목은 숫자를 만들지 않았다. 대신 Reuters / WSJ / Washington Post / 공개 사고기록에 남은 **가격 anchor, 이벤트 수익률, 계약금액, PF 지표, 안전사고 지표, 데이터센터 투자금액**으로 계산 가능한 값은 직접 계산했다.

```text
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
```

---

# 1. 이번 라운드 대섹터

```text
R10 = 건설·부동산·건자재
large_sector = CONSTRUCTION_REAL_ESTATE_MATERIALS
round = R10 Loop 8 / price-path validation
```

R10의 핵심은 “수주가 있다”가 아니라 **수주가 마진·현금흐름·NOI/AFFO·PF 안정·안전신뢰로 닫히는가**다. 이번 라운드는 해외 EPC 수주, PF credit, 건설 안전, AI 데이터센터 real asset을 중심으로 본다.

---

# 2. 대상 canonical archetype

```text
OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA
EPC_LOW_MARGIN_ORDER_OVERLAY
PF_RESTRUCTURING_RELIEF
PF_CREDIT_REDTEAM_OVERLAY
APARTMENT_QUALITY_SAFETY_OVERLAY
OPERATIONAL_TRUST_HARD_4C
AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT
AI_DATA_CENTER_NO_REVENUE_NO_TENANT
DATA_CENTER_POWER_WATER_PERMITTING
PRICE_ONLY_RALLY
THESIS_BREAK_4C
```

이번 R10의 핵심 질문은 이거다.

```text
수주·PF relief·데이터센터 테마인가?
아니면 마진, 공정률, 현금회수, 임차계약, NOI/AFFO, 안전신뢰가 확인되는가?
```

---

# 3. deep sub-archetype

```text
해외 EPC:
- Samsung E&A Fadhili gas expansion
- Hyundai E&C Jafurah / Saudi gas network
- Daewoo E&C Grand Faw port
- contract size vs margin
- working capital / cost overrun
- handover milestone

PF / 주택 건설:
- Taeyoung Engineering debt reschedule
- real estate PF delinquency
- syndicated loan
- profitable project filtering
- liquidity support vs true rerating

품질·안전:
- HDC Hyundai Development Gwangju collapse
- POSCO E&C worksite shutdown
- DL Construction executive resignations
- fatal workplace accident
- license / operating profit fine risk

AI 데이터센터 real asset:
- SK / AWS Ulsan AI data center
- OpenAI / Samsung SDS / SK Telecom data centers
- tenant contract
- power / water / permitting
- capex per share
- listed exposure clarity
```

---

# 4. 국장 신규 후보 case

## Case A — 삼성E&A `success_candidate / EPC backlog`

```text
symbol = 028050
case_type = success_candidate
archetype = OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA / EPC_LOW_MARGIN_ORDER_OVERLAY
```

### evidence

Saudi Aramco는 2024년 4월 Fadhili gas plant 확장에 총 77억 달러 EPC 계약을 발주했고, Samsung Engineering, GS Engineering & Construction, Nesma & Partners가 수주자로 포함됐다. 이 프로젝트는 Fadhili 처리능력을 하루 25억 scf에서 40억 scf로 높이고, 2027년 11월 완공 예정이다. ([Reuters][1])

WSJ는 삼성E&A가 이 중 약 60억 달러 규모 계약을 따냈고, 발표 후 삼성E&A 주가가 장중 8.5% 올라 26,750원까지 갔다고 보도했다. 같은 보도에서 KOSPI는 1.4% 하락 중이었고, KB증권 목표가는 35,000원이었다. ([월스트리트저널][2])

### stage date

```text
Stage 1:
2024-04-02
- Saudi gas EPC cycle
- Fadhili gas expansion

Stage 2:
2024-04-03
- Samsung E&A 약 $6B Fadhili contract
- 주가 장중 +8.5%, 26,750원

Stage 3:
보류
- 대형 EPC 수주는 강한 Stage 2
- Stage 3는 EPC margin, cost control, progress revenue, cash collection 확인 후

Stage 4B:
2024-04-03
- 수주 발표 당일 event rally

Stage 4C:
cost overrun, 저마진 수주, 공정 지연, working capital 악화 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
WSJ / Reuters reported price and contract anchors

stage3_price:
N/A

stage2_event_peak_price:
26,750원

stage2_event_MFE_1D:
+8.5%

implied_pre_event_reference_price:
26,750 / 1.085
= 약 24,654원

KOSPI_same_context_return:
-1.4%

relative_intraday_outperformance_vs_KOSPI:
8.5 - (-1.4)
= +9.9 percentage points

contract_value:
약 $6B

Aramco_total_project:
$7.7B

Samsung_share_of_project:
6.0 / 7.7
= 77.9%

KB_target_price:
35,000원

target_upside_from_event_peak:
(35,000 / 26,750) - 1
= +30.8%

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

peak_price:
26,750원 event anchor, later peak unavailable

drawdown_after_peak:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = EPC_backlog_watch
stage_failure_type = stage2_watch_success
```

### 교정

삼성E&A는 R10에서 `contract_size`를 올릴 수 있지만, Stage 3는 **EPC margin·공정률·현금흐름** 확인 뒤다. 대형 수주 발표 당일 +8.5%는 Stage 2이면서 동시에 event 4B-watch다.

---

## Case B — 현대건설 `success_candidate / Saudi gas infrastructure`

```text
symbol = 000720
case_type = success_candidate
archetype = OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA / INFRA_CONTRACT_BACKLOG
```

### evidence

2024년 6월 Aramco는 Jafurah gas field 2단계와 main gas network 3단계 확장에 250억 달러 이상 계약을 체결했다. Jafurah는 229조 입방피트 가스와 750억 배럴 condensate를 보유한 대형 비전통 가스전이며, 2030년 하루 20억 scf 판매가스 생산을 목표로 한다. Reuters는 Jafurah 확장 계약 수주자에 Hyundai Engineering & Construction이 포함된 consortium이 있다고 보도했다. ([Reuters][3])

### stage date

```text
Stage 1:
2024-06
- Saudi gas infrastructure capex cycle
- Jafurah / main gas network expansion

Stage 2:
2024-06-30
- Aramco $25B+ contracts
- Hyundai E&C consortium included

Stage 3:
보류
- 대형 sovereign EPC 수주는 강한 Stage 2
- Stage 3는 수주잔고의 마진, 공정률, 현금회수 확인 후

Stage 4B:
중동 EPC 수주 기대만으로 주가가 먼저 과열되면 후보

Stage 4C:
project delay, cost overrun, 발주처 지급 지연, 저마진 수주 확인 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters contract / infrastructure evidence

stage3_price:
N/A

stage2_price:
price_data_unavailable_after_deep_search
- Reuters는 현대건설 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

Aramco_contract_package:
>$25B

Jafurah_sales_gas_target:
2.0B scf/day by 2030

main_gas_network_added_capacity:
3.2B scf/day

main_gas_network_added_pipeline:
4,000km

Jafurah_gas_reserves:
229T cubic feet

Jafurah_condensates:
75B barrels

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

peak_price:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = overseas_EPC_watch
stage_failure_type = stage2_watch_success
```

### 교정

현대건설은 `sovereign_contract`, `project_scale`, `backlog`는 가점 가능하다. 하지만 R10 Green은 `low_margin_EPC`, `cost_overrun`, `working_capital_burden`을 통과해야 한다.

---

## Case C — 대우건설 `success_candidate / infrastructure handover milestone`

```text
symbol = 047040
case_type = success_candidate
archetype = OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA / INFRA_RECONSTRUCTION_POLICY
```

### evidence

2024년 11월 Reuters는 Iraq Grand Faw port의 운영사 선정 절차를 보도하면서, South Korea의 Daewoo Engineering & Construction이 건설한 5개 부두가 이라크 항만당국에 인도됐다고 전했다. Grand Faw port는 2026년 운영 시작, 2028년 350만 컨테이너 처리능력을 목표로 하며, 이라크가 2023년 시작한 170억 달러 Development Road 프로젝트의 핵심이다. ([Reuters][4])

### stage date

```text
Stage 1:
2023~2024
- Iraq Development Road
- Grand Faw port / Middle East-Europe corridor

Stage 2:
2024-11-12
- Grand Faw 5개 부두 인도
- handover milestone
- 2026년 운영 시작 계획

Stage 3:
보류
- 완공·인도 milestone은 강한 Stage 2
- Daewoo E&C 이익 인식, 현금회수, 추가 수주 전환 확인 필요

Stage 4B:
이라크 개발도로 / 재건 기대가 주가에 과도 반영되면 후보

Stage 4C:
미수금, 정치 리스크, 대금 회수 지연, 추가 공정 지연 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters infrastructure handover evidence

stage3_price:
N/A

stage2_price:
price_data_unavailable_after_deep_search
- Reuters는 대우건설 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

completed_docks:
5

planned_operation_start:
2026

expected_capacity_2028:
3.5M containers

Iraq_Development_Road_project:
$17B

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

peak_price:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = infrastructure_completion_watch
stage_failure_type = stage2_watch_success
```

### 교정

대우건설은 R10에서 `handover_milestone`을 Stage 2 evidence로 인정할 수 있다. Stage 3는 **수익 인식·현금 회수·추가수주·마진** 확인 뒤다.

---

## Case D — 태영건설 / PF stress `4C-thesis-break`

```text
symbol = 009410
case_type = 4C-thesis-break
archetype = PF_CREDIT_REDTEAM_OVERLAY / PF_RESTRUCTURING_RELIEF
```

### evidence

Reuters는 2024년 3월 한국 정부가 고금리와 건설업 유동성 우려에 대응해 중소기업과 건설사를 위한 40.6조 원 금융지원책을 마련했다고 보도했다. 같은 기사에서 2023년 12월 태영건설이 debt reschedule 계획을 밝혔고, 이로 인해 다른 건설사 유동성 우려가 커졌다고 설명했다. ([Reuters][5])

2024년 5월 금융감독원은 부동산 PF 구조조정 속도를 높이기 위해 평가 기준을 강화했다. Reuters는 real estate project financing 연체율이 2021년 말 0.37%에서 2023년 말 2.70%로 상승했고, commercial banks와 insurers가 1조 원 syndicated loan을 준비했으며 필요 시 최대 5조 원까지 확대 가능하다고 보도했다. ([Reuters][6])

### stage date

```text
Stage 1:
2023
- PF liquidity stress
- high rates / housing downturn / raw material cost pressure

Stage 2:
없음
- debt reschedule은 positive stage가 아니라 RedTeam input

Stage 3:
없음
- workout / debt reschedule / liquidity support는 Green 금지

Stage 4B:
과거 주택경기 회복 기대만으로 주가가 올랐다면 후보

Stage 4C:
2023-12
- Taeyoung debt reschedule plan
- PF liquidity stress
- sector contagion
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters PF stress / policy support anchors

stage3_price:
N/A

stage4c_price:
price_data_unavailable_after_deep_search
- Reuters는 태영건설 주가 anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

government_support_package:
40.6T won

PF_delinquency_2021_end:
0.37%

PF_delinquency_2023_end:
2.70%

PF_delinquency_increase_absolute:
2.70 - 0.37
= +2.33 percentage points

PF_delinquency_increase_relative:
2.70 / 0.37 - 1
= +629.7%

syndicated_loan_initial:
1T won

syndicated_loan_max:
5T won

loan_expandability:
5x

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = PF_credit_break
stage_failure_type = hard_4C
```

### 교정

태영건설은 R10의 PF hard gate 기준점이다.

```text
Green 금지:
debt reschedule
workout
PF delinquency spike
liquidity support dependency

Stage 2 relief:
government support
syndicated loan
profitable project filtering

Stage 3 조건:
credit cleanup
cashflow recovery
funding cost stabilization
no new PF contagion
```

---

## Case E — HDC현대산업개발 `hard 4C / apartment quality safety`

```text
symbol = 294870
case_type = 4C-thesis-break
archetype = APARTMENT_QUALITY_SAFETY_OVERLAY / OPERATIONAL_TRUST_HARD_4C
```

### evidence

2022년 1월 11일 광주 화정 아이파크 외벽 붕괴 사고로 6명이 사망했다. 공개 사고기록은 HDC Hyundai Development Company가 정부 조사를 받았고 회장이 사임했으며, 조사위원회가 잘못된 시공 방식과 부실 자재를 원인으로 봤다고 정리한다. 같은 기록은 HDC가 2021년 광주 철거건물 붕괴 사고에도 연루되어 있었고, 그 사고는 버스 승객 9명이 사망한 사건이었다고 설명한다. ([위키백과][7])

### stage date

```text
Stage 1:
2021~2022
- 주택 브랜드 / 개발사업 기대

Stage 2:
없음
- 품질·안전 사고 후 positive stage 부여 금지

Stage 3:
없음
- 품질·안전 신뢰 회복, 비용 정리, 수주 정상화 전 Green 금지

Stage 4B:
과거 주택경기 회복 기대만으로 주가가 올랐다면 후보

Stage 4C:
2022-01-11
- 광주 화정 아이파크 붕괴
- 6명 사망
- construction quality / operational trust break
```

### 실제 가격경로 검증

```text
price_data_source:
Public accident record, lower-confidence for stock-price validation

stage3_price:
N/A

stage4c_price:
price_data_unavailable_after_deep_search
- Reuters/WSJ/AP 등에서 HDC 주가 reaction anchor를 찾지 못함.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

fatalities_2022_collapse:
6

prior_2021_related_Gwangju_collapse_fatalities:
9

combined_related_Gwangju_fatalities:
15

source_confidence:
medium for accident facts, low for price validation

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = construction_quality_trust_break
stage_failure_type = hard_4C
```

### 교정

HDC현대산업개발은 R10에서 `quality_safety_trust`를 가장 강한 4C hard gate로 만든다. 건설주는 수주잔고보다 **브랜드 신뢰와 현장 안전**이 먼저 깨질 수 있다.

---

## Case F — POSCO E&C / DL Construction safety `4C-watch / operational trust`

```text
symbols = POSCO E&C / DL Construction exposure
case_type = 4C-watch
archetype = OPERATIONAL_TRUST_HARD_4C / APARTMENT_QUALITY_SAFETY_OVERLAY
```

### evidence

Reuters는 2025년 한국의 새 정부가 산업재해 단속을 강화하고 있다고 보도했다. 한국의 2023년 industrial fatality rate는 3.9명/10만 명으로 OECD 평균 2.6명을 웃돌고, 건설 사망률은 15.9명/10만 명으로 OECD 회원국 중 두 번째로 높았다. 같은 기사에 따르면 POSCO E&C는 고속도로 공사 사망사고 후 CEO를 해임하고 103개 공사현장을 중단했으며, DL Construction에서는 사망사고 후 약 80명의 임원이 사의를 냈다. ([Reuters][8])

또 Reuters는 한국 정부가 반복 사망사고 기업에 영업이익의 최대 5% 벌금을 부과하고, 반복 공사중지 명령을 받은 건설사의 면허 취소가 가능하도록 법 개정을 추진한다고 보도했다. 2024년 한국에서 산업재해로 사망한 589명 중 거의 절반은 건설업에서 발생했다. ([Reuters][9])

### stage date

```text
Stage 1:
2025
- industrial safety crackdown
- construction safety regulation 강화

Stage 2:
없음
- 안전사고는 positive evidence가 아니라 RedTeam input

Stage 3:
없음
- 안전 신뢰 회복, 현장 정상화, 비용 영향 확인 전 Green 금지

Stage 4B:
PF relief나 건설 회복 기대 속 안전 리스크가 무시되는 구간이면 후보

Stage 4C-watch:
2025
- POSCO E&C CEO dismissal / 103 sites halted
- DL Construction executives resign
- repeated fatal accident regulation risk
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters safety-regulation / operational evidence anchors

stage3_price:
N/A

stock_price:
price_data_unavailable_after_deep_search
- Reuters는 POSCO E&C/DL Construction 주가 reaction anchor를 제공하지 않음.
- 비상장/계열 exposure가 섞여 direct listed vehicle mapping도 불명확.

Korea_industrial_death_rate_2023:
3.9 per 100,000 workers

OECD_average:
2.6 per 100,000 workers

relative_excess_vs_OECD:
3.9 / 2.6 - 1
= +50.0%

Korea_construction_death_rate:
15.9 per 100,000 workers

POSCO_EC_sites_halted:
103

DL_Construction_executives_resigned:
about 80

proposed_fine:
up to 5% of operating profit

2024_workplace_deaths:
589

construction_share:
nearly half

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = operational_safety_redteam
stage_failure_type = should_have_been_red_or_watch
```

### 교정

POSCO E&C / DL Construction safety case는 R10에서 `workplace_fatality_repeated`, `site_shutdown`, `license_risk`, `operating_profit_fine`을 4C-watch로 강화한다.

---

## Case G — SK/AWS·OpenAI 데이터센터 real asset `success_candidate + price-only basket watch`

```text
listed exposure = SK 계열 / Samsung SDS / SK Telecom / AI-data-center related basket
case_type = success_candidate + event_premium
archetype = AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT / AI_DATA_CENTER_NO_REVENUE_NO_TENANT
```

### evidence

2025년 6월 20일 한국 과기정통부는 SK Group과 Amazon Web Services가 약 7조 원, 약 51억 달러를 투자해 울산에 국내 최대 AI 데이터센터를 건설한다고 발표했다. 이 시설은 2025년 9월 착공, 2029년 100MW 완전 가동을 목표로 하며, SK 회장은 향후 1GW 확장 가능성을 언급했다. Reuters는 발표 당일 AI 관련주가 정책 기대에 랠리를 이어갔고, SK Hynix는 3% 이상, Kakao는 11%, LG CNS는 9% 상승해 KOSPI가 3,000선을 넘었다고 보도했다. ([Reuters][10])

2026년 2월 Reuters는 OpenAI, Samsung SDS, SK Telecom이 한국 데이터센터 건설을 3월부터 시작할 준비를 하고 있다고 보도했다. 한국 정부는 앞서 OpenAI가 두 한국 기업과 joint venture를 만들어 초기 20MW 규모 데이터센터 2곳을 짓겠다고 밝혔다. ([Reuters][11])

2025년 10월 AWS는 한국에 2031년까지 최소 50억 달러를 추가 투자해 AI 데이터센터를 짓겠다고 밝혔다. Reuters는 이 투자와 별개로 6월 SK/AWS 울산 데이터센터의 AWS 40억 달러 투자 계획도 언급했다. ([Reuters][12])

### stage date

```text
Stage 1:
2025-06-20
- SK/AWS Ulsan AI data center
- 7조 원 / $5.11B investment
- 100MW initial capacity, 2029 full operation

Stage 2:
2026-02-11
- OpenAI / Samsung SDS / SK Telecom data-center construction plan
- initial 20MW capacity

Stage 3:
없음
- R10 관점에서는 listed real-estate vehicle, tenant contract, NOI/AFFO, power/water, capex per share 확인 필요
- Samsung SDS / SK Telecom은 R8/R2 성격도 강함

Stage 4B:
2025-06-20
- AI data center policy/event rally
- SK Hynix +3% 이상, Kakao +11%, LG CNS +9%

Stage 4C:
power/water/permitting failure, tenant revenue absence, capex dilution, funding cost spike 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters investment / event return anchors

stage3_price:
N/A

SK_AWS_investment:
7.0T won / $5.11B

AWS_component:
$4B

initial_capacity:
100MW

potential_expansion:
1GW

capacity_expansion_potential:
1GW / 100MW = 10x

construction_start:
2025-09 planned

full_operation:
2029 planned

OpenAI_Samsung_SK_initial_capacity:
20MW

AWS_additional_Korea_investment_by_2031:
at least $5B

event_basket_MFE_1D:
SK Hynix > +3%
Kakao +11%
LG CNS +9%

KOSPI_milestone:
above 3,000 for first time in 3.5 years

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = success_candidate + event_premium
rerating_result = AI_data_center_real_asset_watch
stage_failure_type = stage2_evidence_not_green
```

### 교정

AI 데이터센터는 R10에서 좋은 구조 후보지만, 상장 건설·부동산 관점의 Stage 3는 **tenant / NOI / AFFO / power-water secured / capex per share**가 확인된 뒤다. 정책·투자 발표 당일 AI basket 급등은 4B/event premium으로 분리한다.

---

# 5. 이번 R10 case별 요약표

| case                        | 분류                                |                                                    실제 가격검증 | alignment                         |
| --------------------------- | --------------------------------- | ---------------------------------------------------------: | --------------------------------- |
| 삼성E&A                       | success_candidate                 |          26,750원, +8.5%; KOSPI -1.4%; target upside +30.8% | success_candidate                 |
| 현대건설                        | success_candidate                 |     Aramco $25B+ package, Jafurah 2B scf/day, 주가 anchor 없음 | success_candidate                 |
| 대우건설                        | success_candidate                 | Grand Faw 5 docks handover, 3.5M containers, $17B corridor | success_candidate                 |
| 태영건설/PF                     | hard 4C                           |         PF delinquency 0.37%→2.70%, +629.7%; 40.6T support | thesis_break                      |
| HDC현산                       | hard 4C                           |                      6명 사망, 2021 관련 붕괴 9명 사망, combined 15명 | thesis_break                      |
| POSCO E&C / DL Construction | 4C-watch                          |   103 sites halted, 80 executives resigned, max 5% OP fine | thesis_break_watch                |
| SK/AWS·OpenAI data center   | success_candidate + event premium |         7T won / $5.11B, 100MW→1GW, Kakao +11%, LG CNS +9% | event_premium + success_candidate |

---

# 6. score-price alignment 판정

```text
success_candidate:
- 삼성E&A
- 현대건설
- 대우건설
- SK/AWS·OpenAI 데이터센터

event_premium:
- 삼성E&A 수주 발표 당일 +8.5%
- AI 데이터센터 정책/투자 발표일 AI basket rally

thesis_break:
- 태영건설 / PF stress
- HDC현대산업개발 safety / quality break

thesis_break_watch:
- POSCO E&C / DL Construction safety crackdown

price_moved_without_evidence:
- AI data center related basket 중 tenant/NOI/AFFO 확인 전 급등한 구간

4B-watch:
- 해외 EPC 수주 발표 직후 급등
- AI data center investment news로 관련주 동반 급등

4C-hard:
- PF debt reschedule / liquidity stress
- fatal apartment collapse / quality safety trust break
```

---

# 7. 점수비중 교정

## 올릴 축

```text
cash_flow_after_working_capital +5
EPC_margin_visibility +5
project_cost_control +5
handover_milestone +4
PF_credit_cleanup +5
funding_cost_control +5
tenant_contract_quality +5
NOI_AFFO_visibility +5
power_water_permitting_secured +4
safety_quality_trust +5
```

### 이유

삼성E&A와 현대건설은 대형 해외 EPC 수주 evidence가 있지만, 건설/EPC에서는 수주금액보다 **마진·공정률·현금회수**가 Stage 3를 결정한다. 대우건설 Grand Faw의 5개 부두 인도는 handover milestone으로 Stage 2 가치가 있지만, 이익 인식과 현금회수 확인 전 Green은 보류해야 한다. ([월스트리트저널][2])

## 내릴 축

```text
contract_headline_only -5
PF_relief_policy_only -5
real_estate_rebound_theme_only -4
data_center_theme_without_tenant -5
asset_headline_without_NOI_AFFO -5
EPC_backlog_without_margin -5
low_margin_order_risk -4
capex_per_share_dilution -4
quality_safety_incident -5
workplace_fatality_repeated -5
```

### 이유

태영건설/PF stress는 liquidity support가 Green이 아니라 RedTeam이라는 걸 보여준다. HDC현산 붕괴와 POSCO E&C/DL Construction 안전사고 이슈는 건설사에서 operational trust가 EPS보다 먼저 꺾일 수 있음을 보여준다. ([Reuters][5])

## Green gate 강화 조건

```text
R10 Stage 3-Green 필수:
1. 수주 또는 임차계약이 회사 단위로 확인됨
2. 마진 또는 NOI/AFFO가 확인됨
3. 현금흐름이 working capital에 먹히지 않음
4. PF / funding cost 리스크 통과
5. 공정률 / 원가율 안정
6. tenant / occupancy / utilization 확인
7. capex per share / dilution 통과
8. 안전·품질 hard risk 없음
9. 가격경로가 evidence 이후 따라옴

금지:
수주 headline만 있음
PF 지원책만 있음
데이터센터 테마만 있음
자산 보유 headline만 있음
REIT 배당 headline만 있음
안전사고 발생
working capital 악화
저마진 EPC 수주
```

## 4B 조기감지 조건

```text
4B-watch:
대형 해외 EPC 수주 발표 직후 급등
PF 지원책으로 건설주 동반 급등
데이터센터 테마로 부동산/건설주 일괄 상승
REIT가 금리 인하 기대만으로 급등
재건/재난복구 테마로 가격이 먼저 감

4B-elevated:
수주는 늘지만 마진 가시성이 약함
PF 부실이 아직 정리되지 않음
공사비·인건비·금융비용 상승
데이터센터 tenant는 있지만 power/water/capex 문제가 남음
AFFO보다 배당 기대가 먼저 반영
```

## 4C hard gate 조건

```text
PF workout / 채무재조정
부동산 PF 연체율 급등
미분양 / 분양 실패
공사비 원가율 급등
working capital 악화
수주 취소 / 발주처 지급 지연
저마진 EPC 손실 인식
아파트 붕괴 / 품질사고
사망사고 반복 / 현장중단
면허 취소 리스크
tenant 부재
power/water/permitting failure
AFFO integrity 훼손
capex dilution
```

---

# 8. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
```

이번 세션에서 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉을 안정적으로 직접 확보하지 못했다. 대신 Reuters / WSJ / Washington Post / 공개 사고기록의 가격 anchor와 이벤트 수익률, 계약·안전·PF 지표를 사용해 계산 가능한 부분은 직접 계산했다.

---

# 9. patch-ready 출력

## docs/round/round_142.md 요약

```md
# R10 Loop 8. Construction / Real Estate / Building Materials Price Validation

이번 라운드는 R10 price-validation 라운드다.

핵심 결론:
- 삼성E&A는 Fadhili $6B contract로 Stage 2 후보가 된다. 주가는 26,750원, 장중 +8.5%, KOSPI 대비 +9.9pp 아웃퍼폼했다. 하지만 Stage 3는 EPC margin, progress revenue, cash collection 확인 후다.
- 현대건설은 Aramco $25B+ Jafurah/main gas network package에 포함된 Stage 2 후보지만, 주가 anchor는 확보하지 못했다.
- 대우건설은 Grand Faw 5개 부두 handover로 Stage 2 milestone을 갖지만, 이익 인식과 현금회수 전 Green 금지다.
- 태영건설/PF stress는 R10 hard 4C 기준점이다. PF delinquency는 0.37%에서 2.70%로 +629.7% 상승했다.
- HDC현산 광주 붕괴는 apartment quality / operational trust hard 4C다.
- POSCO E&C / DL Construction safety cases는 repeated fatal accident / worksite shutdown 4C-watch다.
- SK/AWS·OpenAI 데이터센터는 구조 후보지만, tenant·NOI/AFFO·power/water·capex per share 전 Stage 3가 아니다. 발표 당일 Kakao +11%, LG CNS +9% 등은 event premium이다.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 142 R10 Loop 8 Construction Real Estate Materials Price Validation

## 반영 내용
- R10 Loop 8 price-validation 라운드를 추가했다.
- Overseas EPC, infrastructure handover, PF credit stress, apartment safety, workplace safety, AI data center real asset을 비교했다.
- Reuters/WSJ/Washington Post/public accident records reported anchors로 가능한 MFE/MAE 및 contract/safety/PF 지표를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- EPC margin, cash flow after working capital, handover milestone, PF cleanup, tenant/NOI/AFFO, safety trust 가중치 강화
- contract headline only, PF relief only, data-center theme without tenant, safety incident 감점 강화
- PF hard 4C와 construction safety hard 4C 강화
```

## case row 초안

```jsonl
{"case_id":"r10_loop8_samsung_ea_fadhili_epc","symbol":"028050","company_name":"삼성E&A","case_type":"success_candidate","primary_archetype":"OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA","stage2_date":"2024-04-03","stage4b_date":"2024-04-03","price_validation":{"price_data_source":"WSJ/Reuters reported anchors","stage3_price":null,"stage2_event_peak_price":26750,"stage2_event_mfe_1d_pct":8.5,"implied_pre_event_reference_price":24654,"kospi_same_context_return_pct":-1.4,"relative_outperformance_pp":9.9,"contract_value_usd_bn":6.0,"aramco_total_project_usd_bn":7.7,"samsung_share_of_project_pct":77.9,"kb_target_price":35000,"target_upside_from_event_peak_pct":30.8,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate","rerating_result":"EPC_backlog_watch","notes":"Large EPC contract is Stage 2; Stage 3 requires margin, progress revenue and cash collection."}
{"case_id":"r10_loop8_hyundai_ec_jafurah_gas_infra","symbol":"000720","company_name":"현대건설","case_type":"success_candidate","primary_archetype":"OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA","stage2_date":"2024-06-30","price_validation":{"price_data_source":"Reuters contract evidence","stage3_price":null,"aramco_contract_package_usd_bn":25.0,"jafurah_sales_gas_target_bscfd":2.0,"main_gas_network_added_capacity_bscfd":3.2,"main_gas_network_added_pipeline_km":4000,"jafurah_gas_reserves_tcf":229,"jafurah_condensates_bbl_bn":75,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"overseas_EPC_watch","notes":"Sovereign EPC Stage 2; Stage 3 requires margin, working capital and cash recovery."}
{"case_id":"r10_loop8_daewoo_ec_grand_faw_handover","symbol":"047040","company_name":"대우건설","case_type":"success_candidate","primary_archetype":"INFRA_RECONSTRUCTION_POLICY","stage2_date":"2024-11-12","price_validation":{"price_data_source":"Reuters infrastructure handover evidence","stage3_price":null,"completed_docks":5,"planned_operation_start_year":2026,"expected_capacity_2028_mn_containers":3.5,"iraq_development_road_project_usd_bn":17,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"infrastructure_completion_watch","notes":"Handover milestone is Stage 2; profit recognition and cash collection required for Stage 3."}
{"case_id":"r10_loop8_taeyoung_pf_hard_4c","symbol":"009410","company_name":"태영건설/PF stress","case_type":"4c_thesis_break","primary_archetype":"PF_CREDIT_REDTEAM_OVERLAY","stage4c_date":"2023-12","price_validation":{"price_data_source":"Reuters PF stress anchors","stage3_price":null,"government_support_package_krw_trn":40.6,"pf_delinquency_2021_pct":0.37,"pf_delinquency_2023_pct":2.70,"pf_delinquency_absolute_increase_pp":2.33,"pf_delinquency_relative_increase_pct":629.7,"syndicated_loan_initial_krw_trn":1,"syndicated_loan_max_krw_trn":5,"loan_expandability_multiple":5,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break","rerating_result":"PF_credit_break","notes":"Debt reschedule and PF delinquency spike are hard 4C; liquidity support is relief, not Green."}
{"case_id":"r10_loop8_hdc_hyundai_development_quality_safety_4c","symbol":"294870","company_name":"HDC현대산업개발","case_type":"4c_thesis_break","primary_archetype":"APARTMENT_QUALITY_SAFETY_OVERLAY","stage4c_date":"2022-01-11","price_validation":{"price_data_source":"public accident record; stock OHLC unavailable","stage3_price":null,"fatalities_2022_collapse":6,"prior_2021_related_gwangju_fatalities":9,"combined_related_gwangju_fatalities":15,"source_confidence":"medium_for_accident_facts_low_for_price_validation","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break","rerating_result":"construction_quality_trust_break","notes":"Apartment collapse and repeated Gwangju safety incidents are hard 4C for construction quality trust."}
{"case_id":"r10_loop8_posco_ec_dl_construction_safety_watch","symbol":"POSCO_EC/DL_CONSTRUCTION","company_name":"POSCO E&C / DL Construction","case_type":"4c_watch","primary_archetype":"OPERATIONAL_TRUST_HARD_4C","stage4c_date":"2025","price_validation":{"price_data_source":"Reuters safety-regulation anchors","stage3_price":null,"korea_industrial_death_rate_per_100k":3.9,"oecd_average_death_rate_per_100k":2.6,"relative_excess_vs_oecd_pct":50.0,"korea_construction_death_rate_per_100k":15.9,"posco_ec_sites_halted":103,"dl_construction_executives_resigned":80,"proposed_fine_pct_of_operating_profit":5,"workplace_deaths_2024":589,"construction_share":"nearly_half","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"operational_safety_redteam","notes":"Repeated fatal accidents and worksite shutdowns require 4C-watch and safety-trust gate."}
{"case_id":"r10_loop8_ai_data_center_real_asset_watch","symbol":"SK/AWS/Samsung_SDS/SK_Telecom_related","company_name":"SK/AWS·OpenAI 데이터센터","case_type":"success_candidate","primary_archetype":"AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT","stage1_date":"2025-06-20","stage2_date":"2026-02-11","stage4b_date":"2025-06-20","price_validation":{"price_data_source":"Reuters investment and event-return anchors","stage3_price":null,"sk_aws_investment_krw_trn":7.0,"sk_aws_investment_usd_bn":5.11,"aws_component_usd_bn":4.0,"initial_capacity_mw":100,"potential_expansion_gw":1.0,"capacity_expansion_potential_multiple":10,"construction_start_planned":"2025-09","full_operation_planned_year":2029,"openai_samsung_sk_initial_capacity_mw":20,"aws_additional_korea_investment_usd_bn":5.0,"sk_hynix_event_mfe_pct":3,"kakao_event_mfe_pct":11,"lg_cns_event_mfe_pct":9,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"AI_data_center_real_asset_watch","notes":"AI data center investment is Stage 1/2; tenant, NOI/AFFO, power/water and capex per share required before Green."}
```

## shadow weight row 초안

```csv
archetype,cash_flow_after_wc,epc_margin,project_cost_control,handover_milestone,pf_cleanup,funding_cost,tenant_noi_affo,safety_trust,event_penalty,hard_4c_sensitivity,notes
OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA,+5,+5,+5,+3,+0,+3,+0,+2,-3,+3,Samsung E&A and Hyundai E&C show large EPC Stage 2; Stage 3 requires margin/cash collection.
INFRA_RECONSTRUCTION_POLICY,+4,+4,+4,+5,+1,+3,+0,+2,-3,+3,Daewoo Grand Faw handover is Stage 2 milestone; cash recovery and additional orders needed.
PF_CREDIT_REDTEAM_OVERLAY,+5,+0,+0,+0,+5,+5,+0,+2,-5,+5,Taeyoung/PF delinquency spike is hard 4C; liquidity support is not Green.
APARTMENT_QUALITY_SAFETY_OVERLAY,+0,+0,+0,+0,+0,+0,+0,+5,-0,+5,HDC collapse is hard 4C for quality/safety trust.
OPERATIONAL_TRUST_HARD_4C,+0,+0,+0,+0,+0,+0,+0,+5,-0,+5,POSCO E&C/DL safety cases require 4C-watch and license/fine risk.
AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT,+4,+0,+4,+2,+0,+5,+5,+3,-5,+4,AI data center theme is Stage 1/2 until tenant, NOI/AFFO, power/water and capex per share confirm.
AI_DATA_CENTER_NO_REVENUE_NO_TENANT,+0,+0,+0,+0,+0,+0,+5,+2,-5,+5,No tenant/no revenue data center theme must not become Green.
```

---

# 이번 R10 Loop 8 결론

R10은 Stage 3를 매우 보수적으로 줘야 한다.

```text
1. 삼성E&A·현대건설·대우건설은 모두 좋은 Stage 2 후보가 될 수 있다.
   하지만 수주·handover가 Stage 3는 아니다. 마진·공정률·현금회수가 필요하다.

2. 태영건설/PF stress는 R10 hard 4C 기준점이다.
   PF 연체율 +629.7%, debt reschedule, liquidity support는 Green이 아니라 RedTeam이다.

3. HDC현산은 품질·안전 hard 4C 기준점이다.
   건설주는 안전신뢰가 깨지면 수주잔고보다 RedTeam이 먼저다.

4. POSCO E&C / DL Construction safety case는 반복 사망사고와 현장중단이 operational trust 4C-watch가 되어야 함을 보여준다.

5. AI 데이터센터 real asset은 구조 후보지만,
   tenant·NOI/AFFO·power/water·capex per share 전에는 Stage 3가 아니다.
   발표 당일 관련주 급등은 4B/event premium이다.
```

한 문장으로 압축하면:

> **R10에서 진짜 Stage 3는 “수주가 있다”나 “데이터센터를 짓는다”가 아니라, 수주·자산·임차계약이 마진·현금흐름·NOI/AFFO로 닫히고 PF·안전·funding cost를 통과하는 순간이다.**
> **R10은 PF와 안전사고를 가장 강한 4C hard gate로 둬야 한다.**

[1]: https://www.reuters.com/markets/commodities/aramco-awards-77-bln-contracts-fadhili-gas-expansion-2024-04-02/?utm_source=chatgpt.com "Aramco awards $7.7 bln in contracts for Fadhili gas expansion"
[2]: https://www.wsj.com/articles/samsung-e-a-shares-rise-on-6-billion-saudi-contract-win-10a5b2f4?utm_source=chatgpt.com "Samsung E&A Shares Rise on $6 Billion Saudi Contract Win"
[3]: https://www.reuters.com/business/energy/aramco-signs-over-25-bln-deals-main-gas-network-jafurah-gas-field-2024-06-30/?utm_source=chatgpt.com "Aramco signs over $25 bln of deals for main gas network and Jafurah gas field"
[4]: https://www.reuters.com/world/middle-east/iraq-shortlists-11-firms-grand-faw-port-operation-decision-january-2025-2024-11-12/?utm_source=chatgpt.com "Iraq shortlists 11 firms for Grand Faw port operation, decision in January 2025"
[5]: https://www.reuters.com/markets/asia/south-korea-prepares-financial-support-small-businesses-builders-2024-03-27/?utm_source=chatgpt.com "South Korea prepares financial support for small businesses, builders"
[6]: https://www.reuters.com/markets/asia/south-korea-tightens-scrutiny-speed-up-real-estate-restructuring-2024-05-13/?utm_source=chatgpt.com "South Korea tightens scrutiny to speed up real estate restructuring"
[7]: https://en.wikipedia.org/wiki/Gwangju_Hwajeong_I-Park_exterior_wall_collapse?utm_source=chatgpt.com "Gwangju Hwajeong I-Park exterior wall collapse"
[8]: https://www.reuters.com/world/asia-pacific/south-koreas-new-president-injured-child-labourer-cracks-down-workplaces-death-2025-11-16/?utm_source=chatgpt.com "South Korea's new president, injured as a child labourer, cracks down on 'workplaces of death'"
[9]: https://www.reuters.com/sustainability/sustainable-finance-reporting/south-korea-fine-companies-up-5-profit-recurring-fatal-accidents-ministry-says-2025-09-15/?utm_source=chatgpt.com "South Korea to fine companies up to 5% of profit for recurring fatal accidents, ministry says"
[10]: https://www.reuters.com/business/retail-consumer/south-korea-says-sk-amazon-invest-5-bln-countrys-biggest-data-centre-2025-06-20/?utm_source=chatgpt.com "South Korea says SK and Amazon to invest $5 billion in country's biggest data centre"
[11]: https://www.reuters.com/world/asia-pacific/openai-samsung-sk-set-start-building-data-centres-korea-march-minister-says-2026-02-11/?utm_source=chatgpt.com "OpenAI, Samsung SDS and SK Telecom set to start building data centres in Korea in March, minister says"
[12]: https://www.reuters.com/business/retail-consumer/amazon-web-services-invest-least-5-billion-south-korea-by-2031-presidential-2025-10-29/?utm_source=chatgpt.com "Amazon subsidiary to invest $5 billion in South Korea, presidential office says"

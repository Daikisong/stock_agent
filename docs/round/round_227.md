순서상 이번은 **R10 Loop 9 — 건설·부동산·건자재 가격경로 검증 라운드**다.

이번 R10 Loop 9는 이전 R10의 HDC·태영·데이터센터만 반복하지 않고, **해외 EPC 수주, 사우디 가스 인프라, 국내 PF 구조조정, 주택정책/서울 공급, 건설 안전사고, 데이터센터 real asset, 건자재/철근 수요 약화**를 같이 본다.

```text
round = R10 Loop 9
round_id = round_155
large_sector = CONSTRUCTION_REAL_ESTATE_MATERIALS
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
```

이번 환경에서는 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉 OHLC를 안정적으로 직접 확보하지 못했다. 그래서 Reuters / WSJ / Washington Post / MarketWatch가 제공한 **가격 anchor, 이벤트 수익률, 계약금액, PF 연체율, 안전사고 지표, 데이터센터 투자금액**만 계산했다. 숫자를 만들지는 않았다.

---

# 1. 이번 라운드 대섹터

```text
R10 = 건설·부동산·건자재
```

R10의 핵심은 “수주가 있다”, “주택공급 정책이 있다”, “데이터센터를 짓는다”가 아니라, **수주가 마진·현금회수·working capital·NOI/AFFO·PF 안정·안전신뢰로 닫히는가**다.

---

# 2. 대상 canonical archetype

```text
OVERSEAS_EPC_CONTRACT_BACKLOG
EPC_LOW_MARGIN_ORDER_OVERLAY
SAUDI_GAS_INFRA_BACKLOG
PF_CREDIT_REDTEAM_OVERLAY
HOUSING_POLICY_SUPPLY_EVENT
SEOUL_RECONSTRUCTION_POLICY_EVENT
CONSTRUCTION_SAFETY_OPERATIONAL_TRUST_4C
WORKPLACE_FATALITY_REGULATORY_4C
AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT
FLOATING_DATA_CENTER_CONSTRUCTION_EVENT
BUILDING_MATERIALS_DEMAND_CYCLE
REBAR_CONSTRUCTION_DEMAND_4C_WATCH
PRICE_ONLY_RALLY
EVENT_PREMIUM
```

---

# 3. deep sub-archetype

```text
해외 EPC:
- Samsung E&A
- GS E&C
- Hyundai E&C
- Saudi Aramco Fadhili / Jafurah
- contract headline vs margin / cash collection
- progress revenue / working capital / cost overrun

PF / 주택:
- Taeyoung Engineering debt reschedule
- real estate PF delinquency
- syndicated loan
- Seoul housing supply / reconstruction policy
- mortgage tightening
- policy relief vs company-level FCF

건설 안전:
- Hyundai Engineering Cheonan bridge collapse
- POSCO E&C site shutdown
- DL Construction executive resignations
- recurring fatal accident fines
- construction license risk

데이터센터 real asset:
- SK / AWS Ulsan AI data center
- OpenAI / Samsung SDS / SK Telecom Korea data centers
- Samsung C&T / Samsung Heavy floating data centers
- tenant / power / water / permitting / capex per share

건자재:
- Hyundai Steel rebar demand
- cement / ready-mix / aggregate proxies
- construction demand cycle
- rebar price / shipbuilding steel plate competition
```

---

# 4. 국장 신규 후보 case

## Case A — 삼성E&A / GS건설 `success_candidate / Fadhili EPC backlog`

```text
symbols = 028050 / 006360
case_type = success_candidate + 4B-watch
archetype = OVERSEAS_EPC_CONTRACT_BACKLOG / EPC_LOW_MARGIN_ORDER_OVERLAY
```

### stage date

```text
Stage 1:
2024-04-02
- Saudi Aramco Fadhili gas expansion
- Middle East gas EPC cycle

Stage 2:
2024-04-03
- Aramco awards $7.7B Fadhili EPC contracts
- Samsung E&A, GS E&C, Nesma & Partners included
- Samsung E&A estimated contract around $6B
- Samsung E&A shares +8.5% to 26,750원

Stage 3:
없음
- EPC 수주금액만으로 Green 금지
- EPC margin, progress revenue, cash collection, working capital 확인 필요

Stage 4B:
2024-04-03
- 수주 발표 당일 event rally

Stage 4C:
cost overrun, 저마진 수주, 발주처 지급 지연, working-capital 악화 시 후보
```

Aramco는 Fadhili gas plant 확장에 77억 달러 EPC 계약을 발주했고, Samsung Engineering, GS E&C, Nesma & Partners가 수주자로 포함됐다. 이 프로젝트는 처리능력을 하루 25억 scf에서 40억 scf로 높이고, 2027년 11월 완공 예정이다. WSJ는 Samsung E&A가 이 중 약 60억 달러 계약을 따냈고 주가가 장중 8.5% 올라 26,750원까지 갔다고 보도했다. ([월스트리트저널][1])

### 실제 가격경로 검증

```text
price_data_source:
WSJ / Reuters reported contract and price anchors

entry_date:
2024-04-03

stage3_price:
N/A

Samsung_E&A_stage2_event_peak_price:
26,750원

Samsung_E&A_stage2_event_MFE_1D:
+8.5%

implied_pre_event_reference_price:
26,750 / 1.085
= 약 24,654원

KOSPI_same_context:
-1.4%

relative_outperformance_vs_KOSPI:
8.5 - (-1.4)
= +9.9pp

Aramco_total_Fadhili_contracts:
$7.7B

Samsung_E&A_contract_estimate:
about $6B

Samsung_share_of_total_project:
6.0 / 7.7
= 77.9%

Fadhili_capacity_increase:
2.5B scf/day → 4.0B scf/day

capacity_increase_pct:
(4.0 / 2.5) - 1
= +60%

KB_target_price:
35,000원

target_upside_from_event_peak:
(35,000 / 26,750) - 1
= +30.8%

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = EPC_backlog_watch
stage_failure_type = stage2_watch_success
```

---

## Case B — 현대건설 `success_candidate / Jafurah gas infra backlog`

```text
symbol = 000720
case_type = success_candidate
archetype = SAUDI_GAS_INFRA_BACKLOG
```

### stage date

```text
Stage 1:
2024-06
- Saudi Jafurah gas field expansion
- main gas network expansion
- Middle East gas infrastructure capex

Stage 2:
2024-06-30
- Aramco signs >$25B deals
- Hyundai E&C consortium included in Jafurah expansion
- main gas network adds 4,000km pipelines
- network capacity +3.2B scf/day

Stage 3:
보류
- sovereign EPC 수주는 Stage 2
- Stage 3는 수주잔고의 마진, 공정률, 현금회수 확인 후

Stage 4B:
중동 EPC 수주 기대만으로 주가가 먼저 과열되면 후보

Stage 4C:
project delay, cost overrun, 발주처 지급 지연, 저마진 수주 확인 시 후보
```

Aramco는 Jafurah gas field 2단계와 main gas network 3단계 확장에 250억 달러 이상 계약을 체결했다. Jafurah는 229조 입방피트 가스와 750억 배럴 condensates를 가진 대형 비전통 가스전이고, 2030년 하루 20억 scf 판매가스 생산을 목표로 한다. 현대건설 컨소시엄이 Jafurah 확장 계약 수주자에 포함됐다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters contract / infrastructure evidence

stage3_price:
N/A

Hyundai_E&C_stock_OHLC:
price_data_unavailable_after_deep_search
- Reuters는 현대건설 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 일봉 OHLC 직접 확보 실패.

Aramco_contract_package:
>$25B

Jafurah_reserves:
229T cubic feet gas

Jafurah_condensates:
75B barrels

Jafurah_sales_gas_target:
2.0B scf/day by 2030

main_gas_network_added_capacity:
3.2B scf/day

main_gas_network_added_pipeline:
4,000km

Jafurah_first_phase_output_2025:
450M scf/day

target_2030_vs_first_phase:
2.0B / 0.45B - 1
= +344.4%

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = Saudi_gas_infra_backlog_watch
stage_failure_type = stage2_watch_success
```

---

## Case C — 태영건설 / PF sector `hard 4C / PF credit break`

```text
symbol = 009410 / construction PF basket
case_type = 4C-thesis-break
archetype = PF_CREDIT_REDTEAM_OVERLAY
```

### stage date

```text
Stage 1:
2023
- 고금리
- 주택경기 둔화
- PF refinancing stress

Stage 2:
없음
- debt reschedule / liquidity support는 positive stage가 아니라 RedTeam input

Stage 3:
없음
- workout / debt reschedule / 정부 유동성 지원만으로 Green 금지

Stage 4C:
2023-12
- Taeyoung debt reschedule plan
- PF liquidity stress
- sector contagion

추가 4C:
2024-05-13
- real estate PF delinquency 0.37% → 2.70%
- FSS strengthens project assessment
```

한국 정부는 중소기업·건설사 지원을 위해 40.6조 원 금융지원책을 마련했고, Reuters는 태영건설의 2023년 12월 debt reschedule 계획이 다른 건설사 유동성 우려를 키웠다고 보도했다. 이후 금융감독원은 부동산 PF 구조조정을 가속하기 위해 평가 기준을 강화했고, real estate project financing 연체율은 2021년 말 0.37%에서 2023년 말 2.70%로 상승했다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters PF stress / policy-support anchors

stage3_price:
N/A

Taeyoung_stock_OHLC:
price_data_unavailable_after_deep_search
- Reuters는 태영건설 event-day 주가 anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 일봉 OHLC 직접 확보 실패.

government_support_package:
40.6T won

PF_delinquency_2021_end:
0.37%

PF_delinquency_2022_end:
1.19%

PF_delinquency_2023_end:
2.70%

PF_delinquency_increase_2021_to_2023_absolute:
2.70 - 0.37
= +2.33pp

PF_delinquency_increase_2021_to_2023_relative:
2.70 / 0.37 - 1
= +629.7%

PF_delinquency_2022_to_2023_relative:
2.70 / 1.19 - 1
= +126.9%

syndicated_loan_initial:
1T won

syndicated_loan_max:
5T won

loan_expandability:
5x

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = PF_credit_break
stage_failure_type = hard_4C
```

---

## Case D — 서울 주택공급 / 재건축 정책 basket `event_premium / housing policy watch`

```text
symbols = GS E&C / DL E&C / HDC / housing-construction basket
case_type = event_premium / success_candidate
archetype = HOUSING_POLICY_SUPPLY_EVENT / SEOUL_RECONSTRUCTION_POLICY_EVENT
```

### stage date

```text
Stage 1:
2024-08-16
- Seoul home prices jump fastest since 2019
- reconstruction demand
- government supply plan >400,000 homes over six years

Stage 2:
2025-09-07
- Seoul mortgage LTV tightened 50% → 40% in Gangnam/Yongsan
- government also plans to boost housing supply
- state-owned land / reconstruction rule simplification

Stage 3:
없음
- 주택공급 정책만으로 Green 금지
- 분양률, 수주, 원가율, PF 안정, FCF 확인 필요

Stage 4B:
공급정책 / 금리인하 기대만으로 건설주가 동반 급등하면 후보

Stage 4C:
LTV tightening demand shock, unsold inventory, construction cost inflation, PF refinancing stress 시 후보
```

2024년 7월 서울 주택가격은 전월 대비 0.76% 올라 2019년 12월 이후 가장 큰 월간 상승폭을 보였고, 정부는 6년간 40만 호 이상 공급 계획을 제시했다. 2025년 9월에는 강남·용산 등 고가 지역의 LTV를 50%에서 40%로 낮추는 동시에, LH 등 공기업 보유 토지를 활용하고 재건축 규제를 단순화해 공급을 늘리겠다고 밝혔다. 이는 건설사에 Stage 1~2 정책 이벤트지만, Green은 아니다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters housing-policy and property-price evidence

stage3_price:
N/A

housing_basket_OHLC:
price_data_unavailable_after_deep_search
- Reuters는 GS E&C / DL E&C / HDC 등 건설주 basket reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 일봉 OHLC 직접 확보 실패.

Seoul_home_price_monthly_change_July_2024:
+0.76%

national_house_transaction_index_July_2024:
+0.15%

planned_new_homes:
>400,000 over six years

annualized_supply_target:
400,000 / 6
= 약 66,667 homes/year

LTV_tightening:
50% → 40%

LTV_reduction_absolute:
-10pp

LTV_reduction_relative:
40 / 50 - 1
= -20%

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium / policy_watch
rerating_result = housing_supply_policy_watch
stage_failure_type = stage1_or_stage2_attention_only
```

---

## Case E — 현대엔지니어링 / 고속도로 교량 붕괴 `4C-watch / safety trust`

```text
listed exposure = Hyundai group / Hyundai E&C sentiment only
case_type = 4C-watch
archetype = CONSTRUCTION_SAFETY_OPERATIONAL_TRUST_4C
```

### stage date

```text
Stage 1:
2025-02-25 이전
- infrastructure construction
- expressway expansion project

Stage 2:
없음
- 안전사고는 positive evidence가 아니라 RedTeam input

Stage 3:
없음

Stage 4C-watch:
2025-02-25
- Cheonan highway bridge under construction collapsed
- 4 workers killed, 6 injured
- Hyundai Engineering was company in charge of site
- direct listed vehicle mapping unclear
```

2025년 2월 25일 천안의 고속도로 확장 공사 구간에서 교량이 붕괴해 4명이 사망하고 6명이 부상했다. Washington Post는 Hyundai Engineering이 해당 현장 담당 회사였고, 당국 조사에 협조 중이라고 보도했다. 현대엔지니어링은 직접 상장사가 아니기 때문에 R10 scoring에서는 **직접 종목 Green/Red가 아니라 건설 안전 RedTeam 사례**로 둔다. ([The Washington Post][5])

### 실제 가격경로 검증

```text
price_data_source:
Washington Post safety-event evidence

stage3_price:
N/A

listed_stock_mapping:
unclear / not direct listed vehicle

stock_OHLC:
price_data_unavailable_after_deep_search
- Hyundai Engineering is not directly listed.
- event-day Hyundai E&C / Hyundai Motor group sentiment OHLC not confirmed from reliable source in this pass.

fatalities:
4

injuries:
6

critical_injuries:
5 of 6 survivors described as critical

workers_fell:
10

event_type:
partially constructed highway bridge collapse

MFE / MAE:
N/A
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = construction_safety_trust_watch
stage_failure_type = 4C_watch_not_direct_listed_hard_4C
```

---

## Case F — POSCO E&C / DL Construction `4C-watch / recurring fatal accident regulation`

```text
listed exposure = POSCO Holdings / DL Construction exposure
case_type = 4C-watch
archetype = WORKPLACE_FATALITY_REGULATORY_4C
```

### stage date

```text
Stage 1:
2025
- industrial-safety crackdown
- construction fatality regulation 강화

Stage 2:
없음

Stage 3:
없음
- 안전 신뢰 회복, 현장 정상화, 비용 영향 확인 전 Green 금지

Stage 4C-watch:
2025
- POSCO E&C CEO dismissal / 103 construction sites halted
- DL Construction about 80 executives resigned
- repeated fatal accident regulation risk

추가 4C-watch:
2025-09-15
- recurring fatal accidents fine up to 5% of operating profit
- repeated site suspension can lead to construction license revocation
```

Reuters는 한국의 건설 사망률이 15.9명/10만 명으로 OECD 회원국 중 두 번째로 높고, 2024년 산업재해 사망 589명 중 거의 절반이 건설업에서 발생했다고 보도했다. POSCO E&C는 고속도로 공사 사망사고 후 CEO를 해임하고 103개 공사현장을 중단했으며, DL Construction에서는 사망사고 후 약 80명의 임원이 사의를 냈다. 정부는 반복 사망사고 기업에 영업이익의 최대 5% 벌금과 건설 면허 취소 가능성까지 추진했다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters safety-regulation / operational evidence anchors

stage3_price:
N/A

direct_listed_stock_OHLC:
price_data_unavailable_after_deep_search
- POSCO E&C is not separately listed.
- DL Construction / group-level event-day OHLC not confirmed from reliable source.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

Korea_industrial_death_rate_2023:
3.9 per 100,000 workers

OECD_average:
2.6 per 100,000 workers

relative_excess_vs_OECD:
3.9 / 2.6 - 1
= +50.0%

Korea_construction_death_rate:
15.9 per 100,000 workers

2024_workplace_deaths:
589

construction_share:
nearly half

POSCO_EC_sites_halted:
103

DL_Construction_executives_resigned:
about 80

proposed_fine:
up to 5% of operating profit

license_revocation_risk:
true for repeated work-suspension construction firms
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = operational_safety_redteam
stage_failure_type = should_have_been_red_or_watch
```

---

## Case G — SK/AWS·OpenAI·Samsung C&T 데이터센터 `success_candidate + event premium`

```text
listed exposure = SK group / Samsung SDS / SK Telecom / Samsung C&T / Samsung Heavy
case_type = success_candidate + event_premium
archetype = AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT / FLOATING_DATA_CENTER_CONSTRUCTION_EVENT
```

### stage date

```text
Stage 1:
2025-06-20
- SK / AWS Ulsan AI data center
- 7조 원 / $5.11B investment
- 100MW initial capacity, 2029 full operation
- possible 1GW expansion

Stage 2:
2025-10~2026-02
- OpenAI / Samsung SDS / SK Telecom Korea data-center JV plan
- initial two data centers, 20MW
- Samsung C&T / Samsung Heavy explore floating data-center designs

Stage 3:
없음
- 데이터센터 headline만으로 Green 금지
- tenant contract, power, water, permitting, capex per share, NOI/AFFO 확인 필요

Stage 4B:
2025-06-20
- AI data center policy/event rally
- SK Hynix +3% 이상
- Kakao +11%
- LG CNS +9%

Stage 4C:
power/water/permitting failure, tenant revenue absence, capex dilution, funding cost spike 시 후보
```

SK Group과 AWS는 울산에 7조 원, 약 51억 달러를 투자해 국내 최대 AI 데이터센터를 짓겠다고 발표했다. 이 시설은 2025년 9월 착공, 2029년 100MW 완전가동을 목표로 하고, SK 측은 1GW 확장 가능성도 언급했다. 발표 당일 AI 관련주가 정책 기대에 랠리했고 SK하이닉스는 3% 이상, 카카오는 11%, LG CNS는 9% 상승했다. ([Reuters][7])

OpenAI는 Samsung SDS, SK Telecom과 한국 데이터센터 건설을 추진했고, AP는 OpenAI와 Samsung C&T·Samsung Heavy가 floating data center 기술 협력도 논의한다고 보도했다. 이건 R10의 real-asset Stage 2 후보지만, 상장 건설사 Green은 tenant·NOI/AFFO·power/water·capex per share가 확인돼야 한다. ([Reuters][8])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / AP investment and event-return anchors

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
1GW / 100MW
= 10x

construction_start:
2025-09 planned

full_operation:
2029 planned

OpenAI_Samsung_SK_initial_capacity:
20MW

event_basket_MFE_1D:
SK Hynix > +3%
Kakao +11%
LG CNS +9%

KOSPI_milestone:
above 3,000 for first time in 3.5 years

Samsung_C&T / Samsung_Heavy:
floating data center collaboration discussed

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate + event_premium
rerating_result = AI_data_center_real_asset_watch
stage_failure_type = stage2_evidence_not_green
```

---

## Case H — 현대제철 / 건자재·철근 수요 proxy `4C-watch / building-material demand cycle`

```text
symbol = 004020
case_type = 4C-watch
archetype = BUILDING_MATERIALS_DEMAND_CYCLE / REBAR_CONSTRUCTION_DEMAND_4C_WATCH
```

### stage date

```text
Stage 1:
2024
- 건설경기 둔화
- 철근 / 건자재 수요 약화

Stage 2:
없음
- weak demand event는 positive stage가 아님

Stage 3:
없음
- 건설회복 전 Green 금지

Stage 4C-watch:
2024-06-21
- Nomura cuts Hyundai Steel 2024 net profit forecast by 73%
- target price -14% to 30,000원
- shares -1.2% to 29,000원
- rebar price expected -10% in 2024
```

Nomura는 건설·조선 수요 약화로 Hyundai Steel의 2024년 실적이 타격을 받을 수 있다고 봤고, 2024년 순이익 추정치를 73% 낮춰 2,150억 원으로 조정했다. 목표주가는 14% 낮춘 30,000원, 주가는 1.2% 하락한 29,000원으로 보도됐다. 철근 가격은 2024년 10% 하락 가능성이 언급됐다. 이건 R10 건자재·철근 수요 proxy로서 `construction_demand_4C-watch`다. ([마켓워치][9])

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch reported price / target / estimate anchor

stage3_price:
N/A

event_price_anchor:
29,000원

event_MAE:
-1.2%

implied_pre_event_reference_price:
29,000 / (1 - 0.012)
= 약 29,352원

target_price:
30,000원

target_cut:
-14%

implied_prior_target:
30,000 / (1 - 0.14)
= 약 34,884원

target_upside_from_event_price:
(30,000 / 29,000) - 1
= +3.45%

net_profit_forecast_2024:
215B won

net_profit_forecast_cut:
-73%

implied_prior_net_profit_forecast:
215B / (1 - 0.73)
= 약 796.3B won

rebar_price_expected_decline:
-10%

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = building_materials_demand_cycle_watch
stage_failure_type = should_have_been_yellow_or_red
```

---

# 5. 이번 R10 case별 요약표

| case                        | 분류                        |                                                       실제 가격검증 | alignment                      |
| --------------------------- | ------------------------- | ------------------------------------------------------------: | ------------------------------ |
| 삼성E&A / GS건설                | success_candidate + 4B    |      Samsung E&A 26,750원, +8.5%; Fadhili $7.7B, Samsung 약 $6B | EPC Stage 2                    |
| 현대건설                        | success_candidate         | Aramco Jafurah/main gas >$25B, 4,000km pipeline, 3.2B scf/day | Stage 2                        |
| 태영건설 / PF                   | hard 4C                   |            PF delinquency 0.37%→2.70%, +629.7%; support 40.6T | PF credit break                |
| 주택공급 정책 basket              | event premium             |          Seoul +0.76% monthly, LTV 50→40%, supply >400k homes | policy watch                   |
| 현대엔지니어링 bridge collapse     | 4C-watch                  |                          4 killed, 6 injured, 10 workers fell | safety trust watch             |
| POSCO E&C / DL Construction | 4C-watch                  |        103 sites halted, ~80 execs resigned, fine up to 5% OP | safety regulation              |
| SK/AWS·OpenAI data center   | success_candidate + event |            7T won / $5.11B, 100MW→1GW, Kakao +11%, LG CNS +9% | Stage 2 / event                |
| 현대제철 rebar proxy            | 4C-watch                  |            29,000원, -1.2%; NP forecast -73%; rebar price -10% | building-material demand watch |

---

# 6. score-price alignment 판정

```text
success_candidate:
- 삼성E&A / GS건설 Fadhili EPC
- 현대건설 Jafurah / gas network
- SK/AWS·OpenAI data center

event_premium:
- 데이터센터 발표일 AI/부동산/인프라 관련주 basket
- 주택공급·재건축 정책 기대

thesis_break:
- 태영건설 / PF stress

thesis_break_watch:
- 현대엔지니어링 bridge collapse
- POSCO E&C / DL Construction safety crackdown
- 현대제철 rebar / construction demand proxy

price_moved_without_evidence:
- 데이터센터 headline로 tenant/NOI/AFFO 확인 전 급등한 관련주
- 주택공급 정책만으로 건설주가 급등하는 구간

4B-watch:
- 대형 해외 EPC 수주 발표 직후 급등
- AI data center investment news로 관련주 동반 급등
- 주택공급 정책 / 재건축 policy rally

4C-hard:
- PF debt reschedule / PF delinquency spike

4C-watch:
- 건설 안전사고
- repeated fatal accidents regulation
- 건자재 수요 둔화
```

---

# 7. 점수비중 교정

## 올릴 축

```text
cash_flow_after_working_capital +5
EPC_margin_visibility +5
project_cost_control +5
progress_revenue_visibility +4
handover_milestone +4
PF_credit_cleanup +5
funding_cost_control +5
tenant_contract_quality +5
NOI_AFFO_visibility +5
power_water_permitting_secured +4
safety_quality_trust +5
```

### 왜 올리나

삼성E&A와 현대건설은 대형 EPC 수주/가스 인프라 Stage 2 후보가 된다. 그러나 R10에서 수주금액은 첫 관문일 뿐이고, **마진·공정률·현금회수·working capital**이 확인되어야 Stage 3가 된다. 데이터센터도 tenant와 NOI/AFFO가 나오기 전에는 자산 headline에 불과하다.

## 내릴 축

```text
contract_headline_only -5
PF_relief_policy_only -5
real_estate_rebound_theme_only -4
housing_supply_policy_only -4
data_center_theme_without_tenant -5
asset_headline_without_NOI_AFFO -5
EPC_backlog_without_margin -5
low_margin_order_risk -4
capex_per_share_dilution -4
quality_safety_incident -5
workplace_fatality_repeated -5
building_material_demand_weakness -4
```

### 왜 내리나

PF 지원책은 Green이 아니라 RedTeam relief다. 건설 안전사고는 수주잔고보다 강한 4C-watch다. 주택공급 정책은 장기적으로 수주 후보가 될 수 있지만, 분양률·원가율·PF 안정이 확인되기 전에는 Stage 3가 아니다. 데이터센터는 power/water/permitting과 tenant economics가 빠지면 price-only rally가 되기 쉽다.

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
주택공급 정책만 있음
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
주택공급 정책 발표일 건설주 급등

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

이번 R10 Loop 9에서는 **PF는 hard 4C**, **건설 안전은 강한 4C-watch**, **데이터센터는 Stage 2 + event premium**, **EPC 수주는 Stage 2 success_candidate**, **건자재 수요 약화는 4C-watch**로 둔다.

---

# 8. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
```

---

# 9. patch-ready 출력

## docs/round/round_155.md 요약

```md
# R10 Loop 9. Construction / Real Estate / Building Materials Price Validation

이번 라운드는 R10 Loop 9 price-validation 라운드다.

핵심 결론:
- Samsung E&A / GS E&C Fadhili EPC는 Stage 2 후보가 된다. Samsung E&A는 26,750원, +8.5%, KOSPI 대비 +9.9pp 아웃퍼폼했다. 그러나 Stage 3는 EPC margin, progress revenue, cash collection 확인 후다.
- Hyundai E&C는 Aramco Jafurah / main gas network >$25B package에 포함된 Stage 2 후보지만, 회사 주가 reaction anchor는 확보하지 못했다.
- Taeyoung / PF stress는 hard 4C 기준점이다. PF delinquency는 0.37%에서 2.70%로 +629.7% 상승했다.
- Seoul housing supply / reconstruction policy는 Stage 1~2 event다. Seoul home prices +0.76% monthly, LTV 50%→40%, supply >400k homes가 확인되지만 company-level margin/FCF 전 Green 금지다.
- Hyundai Engineering Cheonan bridge collapse는 direct listed vehicle은 불명확하지만 construction safety 4C-watch다. 4 killed, 6 injured.
- POSCO E&C / DL Construction safety cases는 recurring fatal accident 4C-watch다. 103 sites halted, ~80 executives resigned, fine up to 5% operating profit risk.
- SK/AWS·OpenAI/Samsung C&T data center is Stage 2 real-asset candidate, but tenant, NOI/AFFO, power/water, capex per share 전 Stage 3 금지다.
- Hyundai Steel rebar proxy는 건자재·철근 수요 약화 4C-watch다. Shares -1.2% to 29,000원, NP forecast cut -73%, rebar price expected -10%.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 155 R10 Loop 9 Construction Real Estate Materials Price Validation

## 반영 내용
- R10 Loop 9 price-validation 라운드를 추가했다.
- Overseas EPC, Saudi gas infrastructure, PF credit stress, Seoul housing supply policy, bridge-collapse safety risk, recurring fatal-accident regulation, AI data-center real asset, building-material demand cycle을 비교했다.
- Reuters/WSJ/Washington Post/MarketWatch reported anchors로 가능한 MFE/MAE 및 contract/safety/PF/policy metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- EPC margin, cash flow after working capital, progress revenue, PF cleanup, tenant/NOI/AFFO, safety trust 가중치 강화
- contract headline only, PF relief only, housing policy-only, data-center theme without tenant, safety incident 감점 강화
- PF hard 4C와 construction safety 4C-watch 강화
```

## case row 초안

```jsonl
{"case_id":"r10_loop9_samsung_ea_gs_fadhili_epc","symbol":"028050/006360","company_name":"Samsung E&A / GS E&C","case_type":"success_candidate","primary_archetype":"OVERSEAS_EPC_CONTRACT_BACKLOG","stage2_date":"2024-04-03","stage4b_date":"2024-04-03","price_validation":{"price_data_source":"WSJ/Reuters reported contract and price anchors","stage3_price":null,"samsung_ea_event_peak_price":26750,"samsung_ea_event_mfe_1d_pct":8.5,"implied_pre_event_reference_price":24654,"kospi_same_context_pct":-1.4,"relative_outperformance_pp":9.9,"aramco_total_fadhili_contracts_usd_bn":7.7,"samsung_ea_contract_estimate_usd_bn":6.0,"samsung_share_of_total_project_pct":77.9,"fadhili_capacity_before_bscfd":2.5,"fadhili_capacity_after_bscfd":4.0,"capacity_increase_pct":60,"kb_target_price":35000,"target_upside_from_event_peak_pct":30.8,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate","rerating_result":"EPC_backlog_watch","notes":"Large EPC contract is Stage 2; Stage 3 requires margin, progress revenue, cash collection and working-capital control."}
{"case_id":"r10_loop9_hyundai_ec_jafurah_gas_infra","symbol":"000720","company_name":"Hyundai E&C","case_type":"success_candidate","primary_archetype":"SAUDI_GAS_INFRA_BACKLOG","stage2_date":"2024-06-30","price_validation":{"price_data_source":"Reuters contract/infrastructure evidence","stage3_price":null,"aramco_contract_package_usd_bn":25.0,"jafurah_reserves_tcf":229,"jafurah_condensates_bbl_bn":75,"jafurah_sales_gas_target_bscfd":2.0,"main_gas_network_added_capacity_bscfd":3.2,"main_gas_network_added_pipeline_km":4000,"jafurah_first_phase_output_mmcfd":450,"target_2030_vs_first_phase_pct":344.4,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"Saudi_gas_infra_backlog_watch","notes":"Sovereign gas-infra contract is Stage 2; margin, progress revenue and cash recovery required before Green."}
{"case_id":"r10_loop9_taeyoung_pf_credit_hard_4c","symbol":"009410/PF_basket","company_name":"Taeyoung / construction PF stress","case_type":"4c_thesis_break","primary_archetype":"PF_CREDIT_REDTEAM_OVERLAY","stage4c_date":"2023-12/2024-05-13","price_validation":{"price_data_source":"Reuters PF stress/policy-support anchors","stage3_price":null,"government_support_package_krw_trn":40.6,"pf_delinquency_2021_pct":0.37,"pf_delinquency_2022_pct":1.19,"pf_delinquency_2023_pct":2.70,"pf_delinquency_increase_2021_to_2023_pp":2.33,"pf_delinquency_increase_2021_to_2023_pct":629.7,"pf_delinquency_increase_2022_to_2023_pct":126.9,"syndicated_loan_initial_krw_trn":1,"syndicated_loan_max_krw_trn":5,"loan_expandability_multiple":5,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break","rerating_result":"PF_credit_break","notes":"Debt reschedule and PF delinquency spike are hard 4C; liquidity support is relief, not Green."}
{"case_id":"r10_loop9_seoul_housing_supply_policy_watch","symbol":"housing_construction_basket","company_name":"Seoul housing supply / reconstruction policy basket","case_type":"event_premium","primary_archetype":"HOUSING_POLICY_SUPPLY_EVENT","stage1_date":"2024-08-16","stage2_date":"2025-09-07","price_validation":{"price_data_source":"Reuters housing-policy and property-price evidence","stage3_price":null,"seoul_home_price_monthly_change_pct":0.76,"national_house_transaction_index_monthly_change_pct":0.15,"planned_new_homes":400000,"annualized_supply_target_homes":66667,"ltv_before_pct":50,"ltv_after_pct":40,"ltv_reduction_pp":-10,"ltv_reduction_relative_pct":-20,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_policy_watch","rerating_result":"housing_supply_policy_watch","notes":"Housing supply/reconstruction policy is Stage 1/2; sales rate, margin, PF stability and FCF required before Green."}
{"case_id":"r10_loop9_hyundai_engineering_bridge_collapse_watch","symbol":"unlisted_Hyundai_Engineering","company_name":"Hyundai Engineering / Cheonan bridge collapse","case_type":"4c_watch","primary_archetype":"CONSTRUCTION_SAFETY_OPERATIONAL_TRUST_4C","stage4c_date":"2025-02-25","price_validation":{"price_data_source":"Washington Post safety-event evidence","stage3_price":null,"listed_stock_mapping":"unclear_not_direct_listed_vehicle","fatalities":4,"injuries":6,"critical_injuries":5,"workers_fell":10,"event_type":"partially constructed highway bridge collapse","price_validation_status":"not_direct_listed_stock_price_unavailable"},"score_price_alignment":"thesis_break_watch","rerating_result":"construction_safety_trust_watch","notes":"Safety event is 4C-watch for construction operational trust; direct listed vehicle mapping unclear."}
{"case_id":"r10_loop9_posco_ec_dl_construction_safety_regulation","symbol":"POSCO_EC/DL_Construction_exposure","company_name":"POSCO E&C / DL Construction safety cases","case_type":"4c_watch","primary_archetype":"WORKPLACE_FATALITY_REGULATORY_4C","stage4c_date":"2025","price_validation":{"price_data_source":"Reuters safety-regulation evidence","stage3_price":null,"korea_industrial_death_rate_per_100k":3.9,"oecd_average_death_rate_per_100k":2.6,"relative_excess_vs_oecd_pct":50.0,"korea_construction_death_rate_per_100k":15.9,"workplace_deaths_2024":589,"construction_share":"nearly_half","posco_ec_sites_halted":103,"dl_construction_executives_resigned":80,"proposed_fine_pct_of_operating_profit":5,"license_revocation_risk":true,"price_validation_status":"direct_listed_event_ohlc_unavailable"},"score_price_alignment":"thesis_break_watch","rerating_result":"operational_safety_redteam","notes":"Recurring fatal accidents and site shutdowns require 4C-watch and safety-trust gate."}
{"case_id":"r10_loop9_ai_data_center_real_asset_event","symbol":"SK_group/Samsung_SDS/SK_Telecom/Samsung_CT/Samsung_Heavy_related","company_name":"SK/AWS·OpenAI·Samsung C&T data-center real asset","case_type":"success_candidate","primary_archetype":"AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT","stage1_date":"2025-06-20","stage2_date":"2025-10_to_2026-02","stage4b_date":"2025-06-20","price_validation":{"price_data_source":"Reuters/AP investment and event-return anchors","stage3_price":null,"sk_aws_investment_krw_trn":7.0,"sk_aws_investment_usd_bn":5.11,"aws_component_usd_bn":4.0,"initial_capacity_mw":100,"potential_expansion_gw":1.0,"capacity_expansion_potential_multiple":10,"construction_start_planned":"2025-09","full_operation_planned_year":2029,"openai_samsung_sk_initial_capacity_mw":20,"sk_hynix_event_mfe_pct":3,"kakao_event_mfe_pct":11,"lg_cns_event_mfe_pct":9,"floating_data_center_collaboration":true,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"AI_data_center_real_asset_watch","notes":"AI data-center investment is Stage 1/2; tenant, NOI/AFFO, power/water/permitting and capex per share required before Green."}
{"case_id":"r10_loop9_hyundai_steel_rebar_construction_demand_watch","symbol":"004020","company_name":"Hyundai Steel / rebar construction demand proxy","case_type":"4c_watch","primary_archetype":"BUILDING_MATERIALS_DEMAND_CYCLE","stage4c_date":"2024-06-21","price_validation":{"price_data_source":"MarketWatch reported price/target/estimate anchor","stage3_price":null,"event_price_anchor":29000,"event_mae_pct":-1.2,"implied_pre_event_reference_price":29352,"target_price":30000,"target_cut_pct":-14,"implied_prior_target":34884,"target_upside_from_event_price_pct":3.45,"net_profit_forecast_2024_krw_bn":215,"net_profit_forecast_cut_pct":-73,"implied_prior_net_profit_forecast_krw_bn":796.3,"rebar_price_expected_decline_pct":-10,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"building_materials_demand_cycle_watch","notes":"Rebar/construction-demand weakness blocks building-material Green until demand, spread and margin stabilize."}
```

## shadow weight row 초안

```csv
archetype,cash_flow_after_wc,epc_margin,project_cost_control,progress_revenue,pf_cleanup,funding_cost,tenant_noi_affo,safety_trust,event_penalty,hard_4c_sensitivity,notes
OVERSEAS_EPC_CONTRACT_BACKLOG,+5,+5,+5,+4,+0,+3,+0,+2,-3,+4,Large EPC contract is Stage 2; Stage 3 requires margin/progress revenue/cash collection.
SAUDI_GAS_INFRA_BACKLOG,+5,+5,+5,+4,+0,+3,+0,+2,-3,+4,Hyundai E&C Jafurah is Stage 2 until margin and cash recovery confirm.
PF_CREDIT_REDTEAM_OVERLAY,+5,+0,+0,+0,+5,+5,+0,+2,-5,+5,PF delinquency spike and debt reschedule are hard 4C.
HOUSING_POLICY_SUPPLY_EVENT,+3,+2,+3,+2,+4,+4,+0,+2,-5,+4,Housing supply policy is not Green before presales/margin/PF/FCF confirm.
CONSTRUCTION_SAFETY_OPERATIONAL_TRUST_4C,+0,+0,+0,+0,+0,+0,+0,+5,0,+5,Bridge collapse/fatal safety events are 4C-watch or hard 4C depending listed impact.
WORKPLACE_FATALITY_REGULATORY_4C,+0,+0,+0,+0,+0,+0,+0,+5,0,+5,Recurring fatal accidents create fine/license risk and block Green.
AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT,+4,+0,+4,+2,+0,+5,+5,+3,-5,+4,Data-center theme is Stage 1/2 until tenant, NOI/AFFO, power/water and capex per share confirm.
BUILDING_MATERIALS_DEMAND_CYCLE,+4,+4,+3,+0,+3,+4,+0,+2,-4,+4,Rebar/building-material demand weakness requires margin and demand stabilization before Green.
```

---

# 이번 R10 Loop 9 결론

R10은 Stage 3를 보수적으로 줘야 한다.

```text
1. 삼성E&A·GS건설·현대건설의 해외 EPC는 좋은 Stage 2 후보가 될 수 있다.
   하지만 수주 headline이 Stage 3는 아니다. 마진·공정률·현금회수가 필요하다.

2. 태영건설/PF stress는 R10 hard 4C 기준점이다.
   PF 연체율 +629.7%, debt reschedule, liquidity support는 Green이 아니라 RedTeam이다.

3. 서울 주택공급/재건축 정책은 건설주 Stage 1~2 event다.
   분양률·원가율·PF 안정·FCF 확인 전 Green 금지다.

4. 현대엔지니어링 교량 붕괴와 POSCO E&C / DL Construction 안전사고 이슈는
   R10에서 safety trust가 얼마나 강한 4C gate인지 보여준다.

5. AI 데이터센터 real asset은 구조 후보지만,
   tenant·NOI/AFFO·power/water·capex per share 전에는 Stage 3가 아니다.

6. 현대제철 rebar proxy는 건설·건자재 수요 약화가 margin과 earnings를 꺾을 수 있음을 보여준다.
```

한 문장으로 압축하면:

> **R10에서 진짜 Stage 3는 “수주가 있다”나 “데이터센터를 짓는다”가 아니라, 수주·자산·임차계약이 마진·현금흐름·NOI/AFFO로 닫히고 PF·안전·funding cost를 통과하는 순간이다.**
> **R10은 PF와 안전사고를 가장 강한 4C gate로 둬야 한다.**

[1]: https://www.wsj.com/articles/aramco-awards-7-7-bln-in-contracts-to-expand-fadhili-gas-plant-capacity-244a6dee?utm_source=chatgpt.com "Aramco Awards $7.7 Bln in Contracts to Expand Fadhili Gas Plant Capacity"
[2]: https://www.reuters.com/business/energy/aramco-signs-over-25-bln-deals-main-gas-network-jafurah-gas-field-2024-06-30/?utm_source=chatgpt.com "Aramco signs over $25 bln of deals for main gas network and Jafurah gas field"
[3]: https://www.reuters.com/markets/asia/south-korea-prepares-financial-support-small-businesses-builders-2024-03-27/?utm_source=chatgpt.com "South Korea prepares financial support for small businesses, builders"
[4]: https://www.reuters.com/markets/asia/home-prices-seoul-rise-fastest-pace-more-than-4-years-2024-08-16/?utm_source=chatgpt.com "Home prices in Seoul rise at fastest pace in more than 4 years"
[5]: https://www.washingtonpost.com/world/2025/02/25/korea-highway-bridge-collapse/?utm_source=chatgpt.com "4 killed as South Korean highway bridge collapses during construction"
[6]: https://www.reuters.com/world/asia-pacific/south-koreas-new-president-injured-child-labourer-cracks-down-workplaces-death-2025-11-16/?utm_source=chatgpt.com "South Korea's new president, injured as a child labourer, cracks down on 'workplaces of death'"
[7]: https://www.reuters.com/business/retail-consumer/south-korea-says-sk-amazon-invest-5-bln-countrys-biggest-data-centre-2025-06-20/?utm_source=chatgpt.com "South Korea says SK and Amazon to invest $5 billion in country's biggest data centre"
[8]: https://www.reuters.com/world/asia-pacific/openai-samsung-sk-set-start-building-data-centres-korea-march-minister-says-2026-02-11/?utm_source=chatgpt.com "OpenAI, Samsung SDS and SK Telecom set to start building data centres in Korea in March, minister says"
[9]: https://www.marketwatch.com/story/hyundai-steel-s-2024-earnings-could-be-hit-by-weak-demand-market-talk-bcbe77c8?utm_source=chatgpt.com "Hyundai Steel's 2024 Earnings Could Be Hit by Weak Demand -- Market Talk"

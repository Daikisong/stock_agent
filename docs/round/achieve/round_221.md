순서상 이번은 **R4 Loop 9 — 소재·스프레드·전략자원 가격경로 검증 라운드**다.

이번 라운드는 철강 관세, 전략광물, 석유화학 구조조정, 정유 스프레드, 리튬 자원, 비중국 폴리실리콘, 구리·방산 이벤트를 섞어서 본다.

```text
round = R4 Loop 9
round_id = round_149
large_sector = MATERIALS_SPREAD_STRATEGIC_RESOURCES
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
```

원시 수정주가 일봉 OHLC는 이번 환경에서 안정적으로 직접 확보하지 못했다. 대신 Reuters / WSJ / FT / MarketWatch가 제공한 **가격 anchor, 이벤트 수익률, 계약·투자·스프레드·원자재 지표**로 계산 가능한 값만 계산했다.

---

# 1. 이번 라운드 대섹터

```text
R4 = 소재·스프레드·전략자원
```

R4의 핵심은 “원자재 가격이 오른다”가 아니라, **제품 스프레드·cost curve·offtake·supply discipline·FCF가 잠겨서 이익 체급이 바뀌는가**다.

---

# 2. 대상 canonical archetype

```text
STEEL_TARIFF_SPREAD_OVERLAY
STEEL_EXPORT_COMPETITIVENESS_4C_WATCH
NONFERROUS_STRATEGIC_METALS
CRITICAL_MINERALS_US_SUPPLY_CHAIN
GOVERNANCE_DILUTION_EVENT
PETROCHEMICAL_RESTRUCTURING_KOREA
CHEMICAL_SPREAD_4C
REFINING_SPREAD_CYCLE
LITHIUM_RESOURCE_SECURITY
LITHIUM_CYCLE_OVERLAY
POLYSILICON_NON_CHINA_SUPPLY_OPTION
COPPER_PROCESSING_PLUS_DEFENSE
M_AND_A_OPTIONALITY_EVENT
PRICE_ONLY_RALLY
EVENT_PREMIUM
```

---

# 3. deep sub-archetype

```text
철강 / 관세:
- POSCO Holdings
- Hyundai Steel
- U.S. steel/aluminum tariff
- export competitiveness
- U.S. price umbrella vs Korean exporter margin
- tariff shock as 4C-watch

전략광물:
- Korea Zinc
- antimony / gallium / germanium / zinc / copper / precious metals
- U.S. critical minerals smelter
- U.S.-led supply-chain restructuring
- share issuance / dilution / governance fight

석유화학:
- Lotte Chemical
- HD Hyundai Chemical
- Daesan NCC shutdown
- China / Middle East oversupply
- government restructuring support
- capacity discipline vs true spread recovery

정유:
- SK Innovation
- S-Oil
- refining margin / crack spread
- Middle East supply disruption
- cyclical success vs structural Stage 3

리튬:
- POSCO Holdings
- MinRes Wodgina / Mt Marion
- spodumene concentrate
- resource security vs lithium-cycle risk

폴리실리콘:
- OCI Holdings
- non-China polysilicon
- Texas solar capacity
- SpaceX media report
- confirmed contract vs unconfirmed report

구리·방산:
- Poongsan
- ammunition business
- copper processing
- Hanwha acquisition report
- event premium / rumor fade
```

---

# 4. 국장 신규 후보 case

## Case A — POSCO Holdings / Hyundai Steel `4C-watch / steel tariff shock`

```text
symbols = 005490 / 004020
case_type = 4C-watch
archetype = STEEL_TARIFF_SPREAD_OVERLAY / STEEL_EXPORT_COMPETITIVENESS_4C_WATCH
```

### stage date

```text
Stage 1:
2025-02-10
- U.S. 25% steel/aluminum tariff threat
- Korean steel export competitiveness risk

Stage 2:
없음
- 관세 shock은 positive stage가 아니라 RedTeam input

Stage 3:
없음
- tariff event만으로 Green 금지

Stage 4B:
철강 관세가 미국 내 가격상승 기대만으로 steel basket을 밀면 후보

Stage 4C-watch:
2025-02-10
- POSCO Holdings 장중 -3.6%, 230,500원
- Hyundai Steel 장중 -2.9%, record low
- KOSPI -0.5%

추가 4C-watch:
2025-06-02
- U.S. steel/aluminum tariff 25% → 50% threat
- Hyundai Steel -5.1%
- POSCO Holdings -3.2%
```

2025년 2월 미국의 신규 25% 철강·알루미늄 관세 발언 이후 POSCO Holdings는 장중 3.6% 하락해 230,500원, Hyundai Steel은 장중 2.9% 하락해 record low를 기록했다. 2025년 6월에는 관세를 25%에서 50%로 올릴 수 있다는 위협에 Hyundai Steel이 최대 5.1%, POSCO Holdings가 최대 3.2% 하락했다. 이는 철강주에서 **policy/tariff shock이 Stage 3를 막는 4C-watch**로 들어가야 한다. ([Reuters][1])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / WSJ reported event-return anchors

stage3_price:
N/A

POSCO_2025-02-10_event_price:
230,500원

POSCO_2025-02-10_MAE_1D:
-3.6%

POSCO_implied_pre_event_reference_price:
230,500 / (1 - 0.036)
= 약 239,108원

Hyundai_Steel_2025-02-10_MAE_1D:
-2.9%

KOSPI_2025-02-10_same_context:
-0.5%

POSCO_relative_underperformance_vs_KOSPI:
-3.6 - (-0.5)
= -3.1pp

Hyundai_Steel_relative_underperformance_vs_KOSPI:
-2.9 - (-0.5)
= -2.4pp

2025-06-02_event:
Hyundai Steel = -5.1%
POSCO Holdings = -3.2%
KOSPI = -0.2%

Hyundai_Steel_relative_underperformance_2025-06-02:
-5.1 - (-0.2)
= -4.9pp

POSCO_relative_underperformance_2025-06-02:
-3.2 - (-0.2)
= -3.0pp

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = steel_tariff_competitiveness_watch
stage_failure_type = 4C_watch_not_hard_4C
```

### 교정

철강은 `tariff_protection`이 미국 steelmaker에는 호재일 수 있지만, 한국 수출업체에는 **가격경쟁력 훼손**이다.

```text
내릴 축:
tariff_export_competitiveness_risk -5
steel_price_event_without_margin -4
policy_shock_unpriced -4

Green 조건:
actual spread
domestic price pass-through
export margin resilience
customer mix
FCF
```

---

## Case B — 고려아연 / 영풍 `success_candidate + governance/dilution 4B·4C-watch`

```text
symbols = 010130 / 000670
case_type = success_candidate + event_premium + governance_watch
archetype = NONFERROUS_STRATEGIC_METALS / CRITICAL_MINERALS_US_SUPPLY_CHAIN / GOVERNANCE_DILUTION_EVENT
```

### stage date

```text
Stage 1:
2024-09~10
- MBK / YoungPoong control battle
- tender offer / buyback / governance event

Stage 2:
2025-12-15
- U.S. critical minerals smelter project
- $7.4B Tennessee facility
- antimony / germanium / gallium / zinc / lead / copper / precious metals

Stage 3:
없음
- offtake, capex, FCF, dilution, execution 확인 전 Green 금지

Stage 4B:
2025-12-15
- U.S. smelter local media report 후 Korea Zinc 최대 +27%

Stage 4C-watch:
2025-12-16
- MBK / YoungPoong injunction filing
- Korea Zinc -13%

4C relief / still governance watch:
2025-12-24
- court rejects injunction
- Korea Zinc 최대 +5%
- YoungPoong -10.5%
```

고려아연은 2025년 12월 미국 Tennessee에 74억 달러 규모 critical minerals refinery를 짓겠다고 밝혔다. 이 시설은 antimony, germanium, gallium, zinc, lead, copper, precious metals 등을 생산하고, 상업가동은 2027~2029년에 단계적으로 시작될 계획이다. 그러나 이 프로젝트는 19억~19.4억 달러 규모 신주발행과 지배구조 분쟁을 동반했다. MBK·영풍이 share sale injunction을 제기하자 Korea Zinc는 13% 하락했고, 법원이 injunction을 기각하자 Korea Zinc는 최대 5% 올랐지만 YoungPoong은 최대 10.5% 하락했다. ([Financial Times][2])

### 실제 가격경로 검증

```text
price_data_source:
FT / Reuters reported event anchors

stage3_price:
N/A

U.S._smelter_project_value:
$7.4B

commercial_operations:
2027~2029 gradual start

U.S._smelter_event_MFE:
+27%

injunction_event_MAE:
-13%

court_rejection_event_MFE:
+5%

YoungPoong_court_event_MAE:
-10.5%

share_issuance_initial:
$1.9B

share_issuance_revised:
$1.94B / 2.833T won

share_issuance_vs_project_value:
1.94 / 7.4
= 26.2%

new_investor_stake:
about 10%

MBK_YoungPoong_stake:
about 44~46%

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = success_candidate + event_premium + governance_watch
rerating_result = strategic_material_project_watch
stage_failure_type = stage2_evidence_not_green
```

### 교정

고려아연은 R4에서 **전략자원 Stage 2와 governance/dilution RedTeam이 동시에 뜨는 케이스**다.

```text
올릴 축:
strategic_material_status +4
U.S._government_support +4
critical_mineral_supply_chain +4

내릴 축:
governance_battle -5
share_issuance_dilution -5
capex_heavy_project_pre_revenue -4
offtake_unconfirmed -4
```

---

## Case C — 롯데케미칼 / HD현대케미칼 `failed_rerating + restructuring relief`

```text
symbols = 011170 / HD Hyundai Chemical exposure
case_type = failed_rerating + restructuring_watch
archetype = PETROCHEMICAL_RESTRUCTURING_KOREA / CHEMICAL_SPREAD_4C
```

### stage date

```text
Stage 1:
2024~2025
- 석유화학 바닥론
- China / Middle East oversupply
- 구조조정 기대

Stage 2:
2026-02-24
- 정부가 첫 석유화학 구조조정 승인
- Lotte Chemical Daesan NCC 1.1M tpy, 3년 가동중단
- HD Hyundai Chemical과 통합
- 2조 원 이상 지원 package
- 1.2조 원 capital increase

Stage 3:
없음
- 구조조정 승인만으로 Green 금지
- spread, OPM, FCF, debt/funding cost 확인 필요

Stage 4B:
구조조정 기대만으로 chemical basket이 급등하면 후보

Stage 4C:
oversupply 지속, spread reversal, inventory build, debt burden, capacity cut insufficient 시 후보
```

한국 정부는 2026년 2월 Lotte Chemical, HD Hyundai Oilbank, HD Hyundai Chemical이 제출한 Daesan 석유화학 구조조정안을 승인했다. Lotte Chemical Daesan NCC 1.1M tpy 설비는 3년간 가동중단되고, 양사는 HD Hyundai Chemical 지분을 50:50으로 맞추기 위해 총 1.2조 원을 투입한다. 정부는 2조 원 이상 금융지원, 세제·규제 지원, utility 비용 경감 등을 제공한다. 이건 Stage 2 relief지 Stage 3가 아니다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters restructuring evidence

stage3_price:
N/A

stock_OHLC:
price_data_unavailable_after_deep_search
- Reuters는 Lotte Chemical / HD Hyundai Oilbank 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 일봉 OHLC 직접 확보 실패.

Daesan_NCC_capacity_halted:
1.1M tpy

shutdown_duration:
3 years

support_package:
>2.0T won

capital_increase:
1.2T won

utility_cost_savings_estimate:
up to 115B won

R&D_funding:
26B won

equity_split_after_restructuring:
50:50

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = failed_rerating_then_restructuring_watch
rerating_result = petrochemical_restructuring_relief
stage_failure_type = stage2_relief_not_green
```

### 교정

```text
Stage 2 가능:
capacity shutdown
government support
capital injection

Stage 3 조건:
spread recovery
OPM recovery
FCF turn
working capital improvement
debt stabilization
```

---

## Case D — SK이노베이션 / S-Oil `cyclical_success / refining spread watch`

```text
symbols = 096770 / 010950
case_type = cyclical_success
archetype = REFINING_SPREAD_CYCLE
```

### stage date

```text
Stage 1:
2025~2026
- refining margins / crack spreads recovery
- Middle East supply disruption
- U.S. refinery closure support

Stage 2:
2026-01-28
- SK Innovation Q4 OP 2,950억 원, YoY 증가
- 그러나 analyst estimate 3,510억 원 하회
- SK On battery loss 확대
- SK Innovation 주가 +0.4%, KOSPI +1.3%

추가 Stage 2:
2026-05-13
- SK Innovation Q1 OP 2.2조 원
- 전년 동기 300억 원 손실에서 반전
- LSEG estimate 1.4조 원 대비 +57.1% beat

Stage 3:
없음
- 정유마진은 cycle
- multi-quarter margin floor, FCF, deleveraging, capital return 확인 전 Green 금지

Stage 4B:
refining margin spike / geopolitical supply shock으로 가격이 먼저 반영되면 후보

Stage 4C:
margin normalization, crude cost shock, battery loss 재확대, working capital drag 시 후보
```

SK Innovation은 2026년 1월 Q4 영업이익 2,950억 원을 발표했지만 analyst forecast 3,510억 원을 밑돌았고, 주가는 +0.4%로 KOSPI +1.3%를 언더퍼폼했다. 같은 보도에서 S-Oil은 Q4 영업이익이 91% 증가했고 robust refining margins를 예상했다. 2026년 5월에는 SK Innovation이 Q1 영업이익 2.2조 원을 내며 전년 동기 300억 원 손실에서 반전했고, LSEG estimate 1.4조 원을 57.1% 웃돌았다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported financial / event anchors

stage3_price:
N/A

2026_Q4_OP_event:
SK Innovation operating profit = 295B won
prior_year_Q4_OP = 176B won

Q4_OP_growth_YoY:
295 / 176 - 1
= +67.6%

analyst_forecast:
351B won

miss_vs_forecast:
295 / 351 - 1
= -16.0%

SK_Innovation_event_return:
+0.4%

KOSPI_same_context:
+1.3%

relative_underperformance:
0.4 - 1.3
= -0.9pp

SK_On_Q4_loss:
441B won

SK_On_prior_quarter_loss:
125B won

SK_On_loss_worsening:
441 / 125 - 1
= +252.8%

2026_Q1_OP:
2.2T won

2025_Q1_comparable:
-30B won

profit_swing:
2.2T - (-0.03T)
= +2.23T won

LSEG_estimate:
1.4T won

beat_vs_estimate:
2.2 / 1.4 - 1
= +57.1%

S_Oil_Q4_OP_growth:
+91%

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = cyclical_success
rerating_result = refining_cycle_rebound_with_battery_drag
stage_failure_type = stage2_watch_success
```

### 교정

정유는 R4에서 **cycle success와 structural Stage 3를 분리**해야 한다.

```text
Stage 2 가능:
crack spread improvement
OP beat
geopolitical supply disruption

Stage 3 조건:
multi-quarter margin floor
FCF
deleveraging
capital return
battery loss control
```

---

## Case E — POSCO Holdings / MinRes lithium JV `success_candidate / resource-security watch`

```text
symbol = 005490
case_type = success_candidate + cyclical_watch
archetype = LITHIUM_RESOURCE_SECURITY / LITHIUM_CYCLE_OVERLAY
```

### stage date

```text
Stage 1:
2023~2025
- POSCO lithium / battery raw-material internalization
- Australia hard-rock lithium exposure

Stage 2:
2025-11-11
- MinRes sells 30% stake in part of lithium business to POSCO for $765M
- POSCO gets indirect 15% stakes in Wodgina and Mt Marion
- POSCO receives spodumene concentrate in proportion to JV stake

Stage 3:
없음
- resource security는 Stage 2
- lithium hydroxide margin, offtake economics, downstream FCF 확인 전 Green 금지

Stage 4B:
lithium price rebound로 자원주가 먼저 움직이면 후보

Stage 4C:
lithium price 재하락, project write-down, demand slowdown, downstream margin failure 시 후보
```

POSCO는 MinRes의 Wodgina·Mt Marion 리튬 광산 지분 일부를 7.65억 달러에 인수해 각 광산에 간접 15% 지분을 확보한다. MinRes 주가는 발표 후 최대 10.8% 올랐다. 그러나 spodumene 가격은 2022년 톤당 6,000달러 이상에서 2025년 6월 약 610달러까지 떨어졌고, 8월 880달러까지 반등했지만 여전히 2022년 고점 대비 크게 낮았다. 이건 Stage 2 resource security이지 Stage 3가 아니다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters commodity / transaction anchors

stage3_price:
N/A

POSCO_stock_OHLC:
price_data_unavailable_after_deep_search
- Reuters는 POSCO 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 일봉 OHLC 직접 확보 실패.

transaction_value:
$765M

POSCO_indirect_stake:
15% in Wodgina and Mt Marion each

MinRes_event_MFE:
+10.8%

spodumene_peak_2022:
> $6,000/t

spodumene_low_2025_June:
about $610/t

spodumene_drawdown_peak_to_low:
1 - 610 / 6000
= -89.8% 이상

spodumene_rebound_610_to_880:
880 / 610 - 1
= +44.3%

spodumene_880_vs_6000_peak:
880 / 6000 - 1
= -85.3% 이상

MFE / MAE:
POSCO stock OHLC unavailable
```

### alignment

```text
score_price_alignment = success_candidate / cyclical_watch
rerating_result = resource_security_watch
stage_failure_type = stage2_watch_success
```

### 교정

```text
올릴 축:
resource_security +4
offtake_or_concentrate_access +4

내릴 축:
lithium_price_event -5
downstream_margin_unconfirmed -4
commodity_cycle_risk -4
```

---

## Case F — OCI Holdings `success_candidate + unconfirmed media 4B-watch`

```text
symbol = 010060
case_type = success_candidate + event_premium
archetype = POLYSILICON_NON_CHINA_SUPPLY_OPTION
```

### stage date

```text
Stage 1:
2025-06-07
- U.S. solar-cell expansion
- non-China solar supply chain
- AI data center power demand

Stage 2:
2025-06-07
- Texas plant capacity expansion
- $1.2B investment
- target 10GW by 2027

Stage 3:
없음
- capex-heavy project
- confirmed customer contract, margin, FCF 확인 전 Green 금지

Stage 4B:
2026-04-14
- OCI TerraSus / SpaceX polysilicon supply talk media report
- spokesperson cannot confirm
- event premium watch

Stage 4C:
SpaceX deal not confirmed, subsidy rollback, polysilicon price decline, capex overrun 시 후보
```

OCI는 미국 Texas solar cell 생산능력을 2027년까지 10GW로 늘리기 위해 12억 달러를 투자할 계획이다. 이는 AI 데이터센터 전력 수요와 중국산 태양광 규제의 틈을 노리는 Stage 2 후보지만, 아직 capex-heavy project다. 2026년에는 OCI TerraSus가 SpaceX에 polysilicon을 공급하기 위한 다년 계약을 논의 중이라는 보도가 있었지만, SpaceX는 답변하지 않았고 OCI 대변인은 보도를 확인할 수 없다고 밝혔다. ([Financial Times][6])

### 실제 가격경로 검증

```text
price_data_source:
FT / Reuters evidence anchors

stage3_price:
N/A

stock_OHLC:
price_data_unavailable_after_deep_search
- FT/Reuters는 OCI Holdings 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 일봉 OHLC 직접 확보 실패.

U.S._investment:
$1.2B

target_capacity:
10GW by 2027

capacity_equivalent:
10 nuclear power plants equivalent, per FT description

SpaceX_contract_status:
unconfirmed media report

SpaceX_planned_solar_satellite_constellation:
1M solar-powered satellites, according to FCC filing cited by Reuters

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate + event_premium
rerating_result = non_China_polysilicon_watch
stage_failure_type = stage2_evidence_not_green
```

### 교정

```text
Stage 2:
non-China supply option
U.S. capacity expansion

Stage 3 조건:
confirmed contract
volume
price
duration
margin
FCF after capex

감점:
unconfirmed media report
capex-heavy pre-revenue
subsidy uncertainty
```

---

## Case G — 풍산 `event_premium / M&A rumor fade`

```text
symbol = 103140
case_type = event_premium / price_moved_without_evidence
archetype = COPPER_PROCESSING_PLUS_DEFENSE / M_AND_A_OPTIONALITY_EVENT
```

### stage date

```text
Stage 1:
2026-04-03
- Hanwha Aerospace bid report for Poongsan ammunition business
- reported value 1.5T won / $1.1B
- copper + defense optionality

Stage 2:
없음 또는 약한 Stage 2
- confirmed transaction 없음

Stage 3:
없음
- M&A rumor / restructuring review만으로 Green 금지

Stage 4B:
M&A 기대만으로 가격이 급등하면 event premium

Stage 4C:
2026-04-09
- Hanwha Aerospace drops plan
- Poongsan says no plan to sell ammunition division
- rumor fade
```

2026년 4월 한화에어로스페이스가 풍산의 방산사업부를 약 1.5조 원에 인수하려 한다는 보도가 나왔다. 풍산은 구조개편 방안을 검토 중이지만 결정된 것은 없다고 했다. 6일 뒤 한화에어로스페이스는 검토를 중단했다고 공시했고, 풍산도 방산부문 매각 계획이 없다고 밝혔다. 이는 **M&A optionality event가 빠르게 fade되는 케이스**다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters M&A report / termination anchors

stage3_price:
N/A

stock_OHLC:
price_data_unavailable_after_deep_search
- Reuters는 풍산 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 일봉 OHLC 직접 확보 실패.

reported_deal_value:
1.5T won / about $1.1B

rumor_date:
2026-04-03

termination_date:
2026-04-09

rumor_duration:
6 calendar days

transaction_status:
not decided → dropped / no sale plan

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium
rerating_result = copper_defense_M&A_optionality_fade
stage_failure_type = stage1_attention_only
```

### 교정

풍산은 R4에서 `copper_processing + defense` 구조가 있을 수 있지만, M&A rumor만으로 Stage 3 금지다.

```text
Stage 3 조건:
copper spread
ammunition order
defense margin
FCF
confirmed transaction or EPS accretion
```

---

# 5. 이번 R4 case별 요약표

| case                                 | 분류                                   |                                                              실제 가격검증 | alignment               |
| ------------------------------------ | ------------------------------------ | -------------------------------------------------------------------: | ----------------------- |
| POSCO / Hyundai Steel                | 4C-watch                             |    POSCO -3.6% to 230,500원; Hyundai Steel -5.1% on 50% tariff threat | tariff 4C-watch         |
| Korea Zinc / YoungPoong              | success_candidate + governance watch |  KZ +27%, -13%, +5%; YoungPoong -10.5%; share issue 26.2% of project | event + governance      |
| Lotte Chemical / HD Hyundai Chemical | failed_rerating + restructuring      | Daesan NCC 1.1M tpy shut 3 years; support >2T; capital increase 1.2T | restructuring relief    |
| SK Innovation / S-Oil                | cyclical_success                     |    SK OP 2.2T, estimate beat +57.1%; SK Q4 shares +0.4 vs KOSPI +1.3 | refining cycle          |
| POSCO lithium / MinRes               | success_candidate                    |          MinRes +10.8%; spodumene -89.8% peak-to-low, +44.3% rebound | resource security watch |
| OCI Holdings                         | success_candidate + event            |       $1.2B Texas expansion, 10GW by 2027; SpaceX report unconfirmed | stage2_not_green        |
| Poongsan                             | event premium                        |                              1.5T won M&A report → dropped in 6 days | M&A rumor fade          |

---

# 6. score-price alignment 판정

```text
success_candidate:
- Korea Zinc strategic minerals
- POSCO lithium resource security
- OCI non-China polysilicon

cyclical_success:
- SK Innovation / S-Oil refining spread
- POSCO lithium raw material exposure

failed_rerating / restructuring relief:
- Lotte Chemical / petrochemical restructuring

event_premium:
- Korea Zinc governance / share-sale event
- OCI SpaceX unconfirmed media report
- Poongsan M&A rumor
- lithium rebound event

thesis_break_watch:
- POSCO / Hyundai Steel tariff shock
- Korea Zinc dilution / governance fight
- petrochemical oversupply

price_moved_without_evidence:
- Poongsan M&A rumor
- OCI SpaceX unconfirmed report
- Korea Zinc control-battle price moves
```

---

# 7. 점수비중 교정

## 올릴 축

```text
actual_product_spread +5
fcf_after_working_capital +5
supply_discipline_confirmed +5
capacity_shutdown_confirmed +4
price_floor_or_offtake +5
cost_curve_advantage +4
strategic_customer_or_government_offtake +4
inventory_normalization +4
tariff_resilience +4
resource_security_with_downstream_margin +4
```

### 왜 올리나

Lotte Chemical 구조조정은 capacity shutdown 자체는 Stage 2 relief로 볼 수 있고, Korea Zinc와 POSCO lithium은 strategic resource/security 측면에서 Stage 2 후보가 될 수 있다. 하지만 모두 Stage 3로 가려면 **스프레드·offtake·마진·FCF**가 확인되어야 한다.

## 내릴 축

```text
commodity_price_up_only -5
tariff_event_only -4
restructuring_plan_without_margin -4
policy_support_without_fcf -4
tender_offer_or_governance_premium -5
unconfirmed_media_report -5
M&A_rumor_without_transaction -5
capacity_cut_expectation_only -3
lithium_price_event -5
refining_margin_geopolitical_shock -3
capex_heavy_project_pre_revenue -4
```

### 왜 내리나

철강 관세는 한국 steel exporters에 가격경쟁력 리스크로 작동했다. Korea Zinc는 전략광물 사업성이 있어도 dilution/governance event가 price path를 흔들었다. OCI와 Poongsan은 각각 SpaceX 보도와 Hanwha 인수 보도가 확인되지 않거나 빠르게 fade됐다.

## Green gate 강화 조건

```text
R4 Stage 3-Green 필수:
1. product spread 개선이 실제 확인됨
2. cost curve advantage 있음
3. supply discipline 또는 capacity shutdown이 확인됨
4. inventory build가 아님
5. FCF 전환 또는 현금흐름 개선
6. price floor / offtake / long-term contract 존재
7. EPS revision이 1개 분기 이벤트가 아니라 중기 경로로 연결
8. capex 부담과 dilution risk 통과
9. 정책/관세/제재 stress를 통과
10. 가격경로가 evidence 이후 따라옴

금지:
commodity price spike
tariff headline only
tender offer premium
governance battle
정책 지원 기대
미확정 media report
M&A rumor
구조조정 계획만 있음
리튬/폴리실리콘 가격 이벤트
전쟁성 refining margin
```

## 4B 조기감지 조건

```text
4B-watch:
원자재 가격 급등 후 관련주 동반 급등
구조조정 기대만으로 multiple 확장
공개매수 / 자사주 / governance battle로 주가 급등
리튬 / 폴리실리콘 supply discipline 뉴스로 소재주 동반 급등
정제마진 공급차질성 spike
미확정 고객 보도에 급등
M&A rumor에 급등

4B-elevated:
실적보다 가격이 먼저 감
보고서가 commodity upside만 반복
신규 CAPEX 발표로 dilution / FCF 부담 커짐
계약보다 정책/루머가 주가를 끌고 감
```

## 4C hard gate 조건

```text
spread reversal
china_oversupply
middle_east_capacity_overhang
inventory_build
NCC 가동 중단
계약/매각/공개매수 이벤트 불발
regulator revision order
대규모 신주발행 / dilution
commodity price 재하락
project capex overrun
offtake 부재
FCF 악화
tariff shock causing export margin damage
```

이번 R4에서는 **hard 4C보다는 watch가 많다.** Steel tariff, Korea Zinc dilution/governance, petrochemical oversupply, Poongsan rumor fade는 모두 4C-watch 또는 event-fade로 둔다. Hard 4C는 실제 스프레드 붕괴, 대규모 손실, financing failure, offtake failure가 확정될 때 승격한다.

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

## docs/round/round_149.md 요약

```md
# R4 Loop 9. Materials / Spread / Strategic Resources Price Validation

이번 라운드는 R4 Loop 9 price-validation 라운드다.

핵심 결론:
- POSCO Holdings / Hyundai Steel은 U.S. steel tariff shock에 민감하다. POSCO는 -3.6% to 230,500원, Hyundai Steel은 50% tariff threat에서 -5.1%까지 하락했다. tariff export competitiveness risk는 4C-watch다.
- Korea Zinc는 U.S. critical minerals smelter로 Stage 2 후보지만, share issuance/dilution/governance fight가 크다. U.S. smelter event +27%, injunction event -13%, court relief +5% 등 price path는 event premium 성격이 강하다.
- Lotte Chemical / HD Hyundai Chemical restructuring은 Daesan NCC 1.1M tpy 3년 중단, support >2T won, capital increase 1.2T won으로 Stage 2 relief지만, spread/OPM/FCF 확인 전 Stage 3가 아니다.
- SK Innovation / S-Oil refining margin rebound는 cyclical success다. SK Innovation Q1 OP 2.2T won은 estimate를 +57.1% beat했지만, refining margin은 cycle이므로 Green은 multi-quarter FCF 확인 후다.
- POSCO lithium / MinRes JV는 resource-security Stage 2다. MinRes는 +10.8%였지만 spodumene은 2022 peak 대비 여전히 -85% 이상 낮다.
- OCI Holdings는 U.S. non-China polysilicon Stage 2 후보지만, SpaceX supply report는 unconfirmed event premium이다.
- Poongsan은 Hanwha acquisition report가 6일 만에 dropped되며 M&A optionality fade로 분류된다.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 149 R4 Loop 9 Materials Spread Strategic Resources Price Validation

## 반영 내용
- R4 Loop 9 price-validation 라운드를 추가했다.
- Steel tariff shock, Korea Zinc strategic minerals/governance, petrochemical restructuring, refining spread cycle, POSCO lithium JV, OCI non-China polysilicon, Poongsan M&A rumor fade를 비교했다.
- Reuters/WSJ/FT/MarketWatch reported anchors로 가능한 MFE/MAE 및 contract/event metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- product spread, FCF after working capital, supply discipline, offtake, tariff resilience 가중치 강화
- commodity price-only, tariff headline-only, governance premium, unconfirmed media report, M&A rumor 감점 강화
- strategic resource Stage 2와 governance/dilution RedTeam 분리
```

## case row 초안

```jsonl
{"case_id":"r4_loop9_posco_hyundai_steel_tariff_watch","symbol":"005490/004020","company_name":"POSCO Holdings / Hyundai Steel","case_type":"4c_watch","primary_archetype":"STEEL_TARIFF_SPREAD_OVERLAY","stage4c_date":"2025-02-10","price_validation":{"price_data_source":"Reuters/WSJ reported event anchors","stage3_price":null,"posco_event_price_2025_02_10":230500,"posco_mae_2025_02_10_pct":-3.6,"posco_implied_pre_event_reference_price":239108,"hyundai_steel_mae_2025_02_10_pct":-2.9,"kospi_2025_02_10_pct":-0.5,"posco_relative_underperformance_pp":-3.1,"hyundai_steel_relative_underperformance_pp":-2.4,"hyundai_steel_mae_2025_06_02_pct":-5.1,"posco_mae_2025_06_02_pct":-3.2,"kospi_2025_06_02_pct":-0.2,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"steel_tariff_competitiveness_watch","notes":"U.S. tariff shock is 4C-watch for Korean steel exporters; Green requires spread and margin resilience."}
{"case_id":"r4_loop9_korea_zinc_strategic_governance","symbol":"010130/000670","company_name":"Korea Zinc / YoungPoong","case_type":"success_candidate","primary_archetype":"CRITICAL_MINERALS_US_SUPPLY_CHAIN","stage2_date":"2025-12-15","stage4b_date":"2025-12-15","stage4c_date":"2025-12-16","price_validation":{"price_data_source":"FT/Reuters reported event anchors","stage3_price":null,"us_smelter_project_usd_bn":7.4,"commercial_operations":"2027-2029 gradual","us_smelter_event_mfe_pct":27,"injunction_event_mae_pct":-13,"court_rejection_event_mfe_pct":5,"youngpoong_court_event_mae_pct":-10.5,"share_issuance_usd_bn":1.94,"share_issuance_vs_project_value_pct":26.2,"new_investor_stake_pct":10,"mbk_youngpoong_stake_pct":"44-46","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_event_premium_governance_watch","rerating_result":"strategic_material_project_watch","notes":"Strategic minerals are Stage 2; governance/dilution/offtake/FCF must clear before Stage 3."}
{"case_id":"r4_loop9_lotte_hd_petrochemical_restructuring","symbol":"011170/HD_Hyundai_Chemical","company_name":"Lotte Chemical / HD Hyundai Chemical","case_type":"failed_rerating","primary_archetype":"PETROCHEMICAL_RESTRUCTURING_KOREA","stage2_date":"2026-02-24","price_validation":{"price_data_source":"Reuters restructuring evidence","stage3_price":null,"daesan_ncc_capacity_mn_tpy":1.1,"shutdown_duration_years":3,"support_package_krw_trn":2.0,"capital_increase_krw_trn":1.2,"utility_cost_savings_krw_bn":115,"rnd_funding_krw_bn":26,"equity_split_after_restructuring":"50:50","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"failed_rerating_then_restructuring_watch","rerating_result":"petrochemical_restructuring_relief","notes":"Capacity shutdown/support is Stage 2 relief; spread, OPM and FCF recovery required for Green."}
{"case_id":"r4_loop9_sk_innovation_soil_refining_cycle","symbol":"096770/010950","company_name":"SK Innovation / S-Oil","case_type":"cyclical_success","primary_archetype":"REFINING_SPREAD_CYCLE","stage2_date":"2026-01-28","price_validation":{"price_data_source":"Reuters reported financial/event anchors","stage3_price":null,"sk_q4_op_krw_bn":295,"sk_q4_prior_year_op_krw_bn":176,"sk_q4_op_growth_pct":67.6,"analyst_forecast_krw_bn":351,"miss_vs_forecast_pct":-16.0,"sk_event_return_pct":0.4,"kospi_same_context_pct":1.3,"relative_underperformance_pp":-0.9,"sk_on_q4_loss_krw_bn":441,"sk_on_prior_quarter_loss_krw_bn":125,"sk_on_loss_worsening_pct":252.8,"sk_q1_2026_op_krw_trn":2.2,"profit_swing_2026_vs_2025_krw_trn":2.23,"beat_vs_lseg_estimate_pct":57.1,"s_oil_q4_op_growth_pct":91,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"cyclical_success","rerating_result":"refining_cycle_rebound_with_battery_drag","notes":"Refining rebound is Stage 2/cyclical; Stage 3 requires multi-quarter margin floor, FCF, capital return and battery loss control."}
{"case_id":"r4_loop9_posco_minres_lithium_jv","symbol":"005490","company_name":"POSCO Holdings / MinRes lithium JV","case_type":"success_candidate","primary_archetype":"LITHIUM_RESOURCE_SECURITY","stage2_date":"2025-11-11","price_validation":{"price_data_source":"Reuters commodity/transaction anchors","stage3_price":null,"transaction_value_usd_mn":765,"posco_indirect_stake_pct":15,"minres_event_mfe_pct":10.8,"spodumene_peak_2022_usd_per_t":6000,"spodumene_low_2025_usd_per_t":610,"spodumene_drawdown_peak_to_low_pct":-89.8,"spodumene_rebound_610_to_880_pct":44.3,"spodumene_880_vs_peak_pct":-85.3,"price_validation_status":"posco_stock_ohlc_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_cyclical_watch","rerating_result":"resource_security_watch","notes":"Lithium mine stake is Stage 2; Stage 3 requires offtake economics, downstream margin and FCF."}
{"case_id":"r4_loop9_oci_non_china_polysilicon","symbol":"010060","company_name":"OCI Holdings","case_type":"success_candidate","primary_archetype":"POLYSILICON_NON_CHINA_SUPPLY_OPTION","stage2_date":"2025-06-07","stage4b_date":"2026-04-14","price_validation":{"price_data_source":"FT/Reuters evidence anchors","stage3_price":null,"us_investment_usd_bn":1.2,"target_capacity_gw":10,"target_year":2027,"spacex_contract_status":"unconfirmed media report","spacex_solar_satellite_constellation":1000000,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_event_premium","rerating_result":"non_China_polysilicon_watch","notes":"U.S. expansion is Stage 2; unconfirmed SpaceX report is event premium until contract terms/margin/FCF confirm."}
{"case_id":"r4_loop9_poongsan_hanwha_mna_rumor_fade","symbol":"103140","company_name":"Poongsan","case_type":"event_premium","primary_archetype":"COPPER_PROCESSING_PLUS_DEFENSE","stage1_date":"2026-04-03","stage4c_date":"2026-04-09","price_validation":{"price_data_source":"Reuters M&A report/termination anchors","stage3_price":null,"reported_deal_value_krw_trn":1.5,"reported_deal_value_usd_bn":1.1,"rumor_date":"2026-04-03","termination_date":"2026-04-09","rumor_duration_days":6,"transaction_status":"not_decided_to_dropped_no_sale_plan","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium","rerating_result":"copper_defense_M&A_optionality_fade","notes":"M&A rumor faded in six days; Stage 3 requires confirmed transaction or copper/ammunition margin/FCF."}
```

## shadow weight row 초안

```csv
archetype,product_spread,fcf_after_wc,supply_discipline,capacity_shutdown,offtake,cost_curve,tariff_resilience,resource_security,event_penalty,governance_redteam,4b_watch_sensitivity,hard_4c_sensitivity,notes
STEEL_TARIFF_SPREAD_OVERLAY,+5,+4,+3,+0,+1,+3,+5,+0,-4,+1,+4,+4,POSCO/Hyundai Steel tariff shock shows export competitiveness 4C-watch.
CRITICAL_MINERALS_US_SUPPLY_CHAIN,+3,+4,+3,+0,+5,+4,+2,+5,-3,+5,+5,+4,Korea Zinc strategic minerals are Stage 2 but governance/dilution blocks Green.
PETROCHEMICAL_RESTRUCTURING_KOREA,+5,+5,+5,+5,+1,+4,+0,+0,-3,+2,+3,+5,Lotte Daesan shutdown is restructuring relief, not Green before spread/FCF.
REFINING_SPREAD_CYCLE,+5,+4,+2,+0,+1,+3,+0,+0,-3,+1,+4,+3,SK/S-Oil refining rebound is cyclical; battery drag and margin durability matter.
LITHIUM_RESOURCE_SECURITY,+2,+4,+2,+0,+5,+4,+0,+5,-5,+1,+4,+4,POSCO lithium JV is resource-security Stage 2 but lithium cycle risk remains.
POLYSILICON_NON_CHINA_SUPPLY_OPTION,+3,+4,+3,+0,+5,+3,+2,+3,-5,+1,+5,+3,OCI U.S. expansion is Stage 2; unconfirmed SpaceX report is event premium.
COPPER_PROCESSING_PLUS_DEFENSE,+4,+4,+2,+0,+3,+3,+1,+0,-5,+2,+5,+3,Poongsan M&A rumor faded; Green requires confirmed transaction or margin/FCF.
M_AND_A_OPTIONALITY_EVENT,+0,+0,+0,+0,+0,+0,+0,+0,-5,+3,+5,+3,M&A rumor without signed transaction should not become Green.
```

---

# 이번 R4 Loop 9 결론

R4는 Stage 3를 아주 보수적으로 줘야 한다.

```text
1. 철강주는 관세가 무조건 호재가 아니다.
   한국 수출업체에는 export competitiveness 4C-watch가 될 수 있다.

2. 고려아연은 전략광물 Stage 2 후보지만,
   governance / dilution / offtake / FCF를 통과해야 Stage 3다.

3. 롯데케미칼 구조조정은 relief이지 Green이 아니다.
   spread·OPM·FCF 회복 전 Stage 3 금지다.

4. SK Innovation / S-Oil 정유 rebound는 cyclical_success다.
   multi-quarter margin floor와 FCF 전에는 구조적 Green이 아니다.

5. POSCO lithium JV는 resource-security Stage 2다.
   리튬 가격 cycle과 downstream margin을 통과해야 한다.

6. OCI는 non-China polysilicon 후보지만,
   SpaceX 보도는 미확정 media report라 4B/event premium이다.

7. Poongsan은 copper + defense optionality가 있어도,
   Hanwha M&A rumor가 6일 만에 fade됐으므로 Stage 3 금지다.
```

한 문장으로 압축하면:

> **R4에서 진짜 Stage 3는 “원자재·관세·전략자원 뉴스가 좋다”가 아니라, 제품 스프레드·offtake·cost curve·supply discipline·FCF가 실제로 잠겨서 이익 체급이 바뀌는 순간이다.**
> **이번 R4 Loop 9는 전략자원과 구조조정 Stage 2를 인정하되, 관세 shock·governance/dilution·미확정 media report·M&A rumor를 4B/4C로 분리하는 라운드다.**

[1]: https://www.reuters.com/markets/asia/shares-south-korean-steelmakers-drop-trump-talks-tariffs-2025-02-10/?utm_source=chatgpt.com "Shares of South Korean steelmakers drop as Trump talks tariffs"
[2]: https://www.ft.com/content/d885ab55-b4f8-4c8f-a213-94f2778863ac?utm_source=chatgpt.com "US backs $7.4bn critical minerals smelter to counter China"
[3]: https://www.reuters.com/world/asia-pacific/south-korea-approves-first-petrochemical-restructuring-deal-supply-glut-weighs-2026-02-24/?utm_source=chatgpt.com "South Korea approves first petrochemical restructuring deal as supply glut weighs"
[4]: https://www.reuters.com/business/energy/sk-innovation-reports-q4-operating-profit-235-million-2026-01-27/?utm_source=chatgpt.com "SK Innovation posts quarterly profit surge, projects strong crack spreads"
[5]: https://www.reuters.com/business/energy/australias-minres-sell-30-lithium-jv-stake-posco-765-mln-2025-11-11/?utm_source=chatgpt.com "Australia's MinRes inks $765 million deal with POSCO for lithium JV stake, shares surge"
[6]: https://www.ft.com/content/e618a7e3-6388-42f9-beb8-c32599f7239d?utm_source=chatgpt.com "Solar group OCI doubles down on US despite Donald Trump's war on clean energy"
[7]: https://www.reuters.com/world/asia-pacific/hanwha-seeks-buy-poongsans-ammunition-business-about-11-billion-newspaper-says-2026-04-03/?utm_source=chatgpt.com "Hanwha seeks to buy Poongsan's ammunition business for about $1.1 billion, newspaper says"

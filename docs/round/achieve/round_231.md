순서상 이번은 **R1 Loop 10 — 산업재·수주·인프라 가격경로 검증 라운드**다.

이번 라운드는 전력기기·변압기, 방산 수출, 해외 EPC, 조선정책, 지정학 제재를 같이 본다. 핵심은 “수주가 있다”가 아니라, **계약금액·납기·고객·마진·EPS revision·현금흐름이 같이 확인되는가**다.

```text
round = R1 Loop 10
round_id = round_159
large_sector = INDUSTRIAL_ORDERS_INFRA
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
```

이번 환경에서는 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉 OHLC를 안정적으로 직접 확보하지 못했다. 대신 Reuters / WSJ / MarketWatch / FT가 제공한 **가격 anchor, 이벤트 수익률, 계약금액, 목표가, 정책·산업 지표**로 계산 가능한 값만 계산했다. 원시 OHLC가 없는 구간은 `price_data_unavailable_after_deep_search`로 명시했다.

---

# 1. 이번 라운드 대섹터

```text
R1 = 산업재·수주·인프라
```

R1의 Stage 3는 “수주공시”가 아니라 **order → delivery → revenue → margin → EPS/FCF**까지 내려오는 순간이다. 수주 잔고는 씨앗이고, Stage 3는 그 씨앗이 실제 영업이익으로 익어 들어오는 순간이다.

---

# 2. 대상 canonical archetype

```text
GRID_POWER_EQUIPMENT_AI_DATACENTER
TRANSFORMER_CAPACITY_BOTTLENECK
DEFENSE_EXPORT_ORDER_TO_REVENUE
MISSILE_DEFENSE_EXPORT_PLATFORM
DEFENSE_LOCAL_PRODUCTION_JV
CAPITAL_ALLOCATION_DILUTION_OVERLAY
OVERSEAS_EPC_CONTRACT_BACKLOG
SAUDI_GAS_INFRA_BACKLOG
SHIPBUILDING_US_POLICY_MASGA
GEOPOLITICAL_SHIPBUILDING_SANCTION
CONTRACT_HEADLINE_NOT_STAGE3
PRICE_ONLY_RALLY
```

---

# 3. deep sub-archetype

```text
전력기기 / 변압기:
- LS Electric
- U.S. transformer shortage
- AI data center / EV / renewable grid demand
- 525kV extra-high-voltage transformers
- company-specific order vs sector bottleneck

방산:
- Hyundai Rotem K2
- LIG Nex1 Cheongung-II / M-SAM
- Hanwha Aerospace K239 Chunmoo missile JV
- Poland / Iraq / Peru / Middle East export expansion
- order-to-revenue vs export headline

해외 EPC:
- Samsung E&A
- GS E&C
- Hyundai E&C
- Saudi Aramco Fadhili / Jafurah / gas network
- contract size vs EPC margin / cash collection

조선 / MRO / 정책:
- HD Hyundai Heavy / HD Hyundai Mipo
- Hanwha Ocean
- MASGA / U.S.-Korea shipbuilding cooperation
- merger / record-high event premium
- China sanctions / U.S. shipbuilding exposure

RedTeam:
- dilution after defence rerating
- policy premium before funded order
- geopolitical sanction
- EPC low-margin / working-capital risk
```

---

# 4. 국장 신규 후보 case

## Case A — LS ELECTRIC `success_candidate / evidence_good_but_price_failed`

```text
symbol = 010120
case_type = success_candidate / evidence_good_but_price_failed
archetype = GRID_POWER_EQUIPMENT_AI_DATACENTER / POWER_EQUIPMENT_EXPORT_US_GRID
```

### stage date

```text
Stage 1:
2024년 상반기
- U.S. data-center construction boom
- renewable / EV grid expansion
- 전력기기 수출 기대

Stage 2:
2024-07-01
- Daiwa가 LS Electric target price 150,000원 → 280,000원으로 상향
- U.S. revenue share가 2022년 5% 미만에서 2024년 약 20%로 상승 가능하다고 전망
- 하지만 당일 주가는 5.4% 하락해 208,500원

추가 Stage 2:
2025-11
- LS Electric announced $312M contract with U.S. utility
- 525kV extra-high-voltage transformers
- supply to southeastern U.S. large-scale data center, 2027~2029

Stage 3:
보류
- sector bottleneck과 company contract는 강함
- 그러나 event-day price failed + margin/FCF 확인 전 Green 금지

Stage 4B:
AI/data-center 전력기기 theme이 company-level delivery/margin보다 먼저 multiple로 확장되면 후보

Stage 4C:
project delay, transformer price normalization, copper/GOES cost pressure, margin miss 시 후보
```

LS Electric은 U.S. grid/data-center 전력기기 수혜 후보로 볼 수 있다. Daiwa는 미국 매출 비중이 2022년 5% 미만에서 2024년 약 20%까지 올라갈 수 있다고 봤고, 목표가를 150,000원에서 280,000원으로 올렸다. 그런데 정작 보도 시점 주가는 5.4% 하락해 208,500원이었다. 이건 **증거는 좋지만 가격경로가 즉시 실패한 Stage 2 후보**다. 이후 Reuters는 미국 transformer shortage 기사에서 LS Electric이 U.S. utility와 3.12억 달러 규모 525kV 초고압 변압기 공급계약을 발표했다고 언급했다. 이 계약은 2027~2029년 미국 남동부 대형 데이터센터에 공급되는 구조다. ([마켓워치][1])

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch price/target anchor + Reuters transformer-sector contract anchor

entry_date:
2024-07-01

stage3_price:
N/A

stage2_price_anchor:
208,500원

stage2_event_MAE_1D:
-5.4%

target_price:
280,000원

target_upside_from_stage2_price:
(280,000 / 208,500) - 1
= +34.3%

target_price_raise:
(280,000 / 150,000) - 1
= +86.7%

U.S._revenue_share_expected_2024:
약 20%

U.S._revenue_share_2022:
5% 미만

minimum_relative_mix_increase:
20 / 5 - 1
= +300% 이상

U.S._utility_transformer_contract:
$312M

contract_product:
525kV extra-high-voltage transformers

delivery_window:
2027~2029

GSU_transformer_demand_growth_since_2019:
+274%

substation_transformer_demand_growth_since_2019:
+116%

transformer_price_increase_5Y:
+80%

large_transformer_lead_time:
up to 4 years

MFE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = evidence_good_but_price_failed
rerating_result = U.S._grid_power_equipment_watch
stage_failure_type = stage2_watch_not_green
```

---

## Case B — 현대 로템 `structural_success / defense order-to-revenue`

```text
symbol = 064350
case_type = structural_success
archetype = DEFENSE_EXPORT_ORDER_TO_REVENUE
```

### stage date

```text
Stage 1:
2022~2024
- Poland K2 tank export
- European rearmament
- Korean ground-equipment export platform

Stage 2:
2024-04-09
- K2 18대 폴란드 납품이 1Q 실적을 견인할 것으로 추정
- K2 export revenue 2,700억 원
- 1Q OP estimate +85% YoY
- shares +9.3%, 41,300원

Stage 3:
2024-04-09 후보
- order headline이 아니라 delivery/revenue/OP revision이 동시에 확인된 구간

추가 Stage 2 / validation:
2025-08-01
- Poland signs second contract for 180 K2 tanks
- contract worth about $6.5B
- 61 tanks to be produced in Poland
- first deliveries planned 2026, local production 2028~2030

추가 Stage 2:
2025-12-09
- Peru framework agreement for 54 K2 tanks + 141 wheeled armored vehicles
- largest South Korean ground-equipment export to Latin America if implementation contract completes

Stage 4B:
Poland second batch / Latin America expansion이 가격에 먼저 과도 반영되면 후보

Stage 4C:
local production delay, margin dilution from technology transfer, payment risk, delivery delay 시 후보
```

현대로템은 R1에서 “수주 headline”과 “Stage 3”의 차이를 가장 잘 보여주는 사례다. 2024년 4월에는 K2 18대 폴란드 납품이 1분기 매출과 영업이익을 끌어올릴 것으로 추정되며 주가가 9.3% 올라 41,300원을 기록했다. KB증권은 1분기 영업이익이 전년 대비 85% 증가하고, K2 폴란드 수출 매출이 2,700억 원으로 분기 매출의 약 3분의 1을 차지할 수 있다고 봤다. 2025년 8월에는 폴란드가 두 번째 180대 K2 계약을 체결했고, 이 계약은 65억 달러 규모로 알려졌다. 2025년 12월에는 페루가 K2 54대와 장갑차 141대 도입을 위한 framework agreement를 체결했다. ([월스트리트저널][2])

### 실제 가격경로 검증

```text
price_data_source:
WSJ / Reuters reported price and contract anchors

entry_date:
2024-04-09

stage3_price:
41,300원

stage3_event_MFE_1D:
+9.3%

implied_pre_event_reference_price:
41,300 / 1.093
= 약 37,786원

KOSPI_same_context_return:
-0.3%

relative_outperformance_vs_KOSPI:
9.3 - (-0.3)
= +9.6pp

K2_export_revenue_1Q_estimate:
270B won

OP_growth_estimate:
+85% YoY

KB_target_price:
47,500원

target_upside_from_stage3_price:
(47,500 / 41,300) - 1
= +15.0%

Poland_second_K2_contract:
$6.5B

Poland_second_contract_units:
180 K2 tanks

Poland_local_production:
61 tanks

Peru_framework_units:
54 K2 tanks + 141 wheeled armored vehicles = 195 units

MFE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = aligned_partial
rerating_result = defense_export_revenue_conversion
stage_failure_type = green_success_candidate
```

---

## Case C — LIG Nex1 `success_candidate + 4B/crowding watch`

```text
symbol = 079550
case_type = success_candidate + 4B-watch
archetype = MISSILE_DEFENSE_EXPORT_PLATFORM
```

### stage date

```text
Stage 1:
2024년
- Cheongung-II / M-SAM export platform
- Middle East air-defense demand

Stage 2:
2024-09-20
- Iraq order 3.71조 원 / $2.8B
- M-SAM II / Cheongung-II missile-defense export
- shares +3.6% in early morning trade
- wider market +0.9%

Stage 3:
보류
- 대형 수출계약은 강한 Stage 2
- delivery schedule, margin, cash collection, EPS revision 확인 필요

Stage 4B:
2024-07-02
- stock had jumped 69% in 1H
- KB downgraded to hold despite raising target
- shares -11% to 195,700원
- valuation/crowding 부담

Stage 4C:
export-license delay, delivery delay, customer payment risk, margin dilution, geopolitical reversal 시 후보
```

LIG Nex1은 Iraq와 3.71조 원, 약 28억 달러 규모 Cheongung-II / M-SAM II 수출계약을 체결했고, 발표 직후 주가는 3.6% 올랐다. 이 계약은 Saudi Arabia 32억 달러 계약 이후 이어진 대형 export validation이다. 다만 2024년 7월에는 주가가 상반기에 69% 급등한 뒤 KB증권이 target price를 올리면서도 hold로 낮췄고, 주가는 11% 하락했다. 이건 **좋은 방산 export platform도 4B/crowding을 동시에 봐야 한다**는 기준점이다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / MarketWatch reported price and contract anchors

stage3_price:
N/A

Iraq_contract_value:
3.71T won / $2.8B

Saudi_prior_contract:
$3.2B

stage2_event_MFE_1D:
+3.6%

wider_market_same_context:
+0.9%

relative_outperformance:
3.6 - 0.9
= +2.7pp

1H_2024_reported_stock_gain:
+69%

KOSPI_1H_2024_gain:
+5.4%

1H_relative_outperformance:
69 - 5.4
= +63.6pp

2024-07-02_4B_event_MAE:
-11%

4B_event_close_price:
195,700원

implied_pre_4B_reference_price:
195,700 / (1 - 0.11)
= 약 219,888원

2Q_OP_estimate:
56.2B won

2Q_OP_growth_estimate:
+40% YoY

target_price:
200,000원

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate + 4B_watch
rerating_result = missile_defense_export_platform_watch
stage_failure_type = stage2_watch_success_with_crowding
```

---

## Case D — 한화에어로스페이스 `success_candidate + dilution 4B-watch`

```text
symbol = 012450
case_type = success_candidate + 4B-watch
archetype = DEFENSE_LOCAL_PRODUCTION_JV / CAPITAL_ALLOCATION_DILUTION_OVERLAY
```

### stage date

```text
Stage 1:
2024~2025
- K-defense export cycle
- Europe rearmament
- Poland / Romania / Middle East localization demand

Stage 2:
2025-04-15
- Hanwha Aerospace and Poland’s WB Electronics agree missile-production JV
- Poland to produce CGR-080 missiles used by K239 Chunmoo
- technology transfer / local production model

Stage 3:
보류
- JV / localization agreement는 Stage 2
- actual order volume, margin, delivery, cash collection, local production economics 필요

Stage 4B:
2025-03-21
- 3.6조 원 capital raising plan announced
- shares -13% next day
- share sale after defense rerating signals 4B/capital allocation risk

Stage 4C:
dilution without FCF, overseas factory overbuild, local production margin dilution, funding/regulator issue 시 후보
```

한화에어로스페이스는 Polish WB Electronics와 CGR-080 guided missile을 폴란드에서 생산하는 joint venture 설립에 합의했다. CGR-080은 Poland가 구매한 K239 Chunmoo system에 쓰이는 missile이다. 이는 단순 수출을 넘어 현지생산·기술이전 모델로 Stage 2 가치가 있다. 하지만 2025년 3월에는 해외생산 확장과 투자 목적의 3.6조 원 유상증자 계획 발표 후 주가가 13% 급락했고, 금융감독원은 공시 보완을 요구했다. 이후 회사는 1.3조 원 affiliate share issue와 2.3조 원 rights offering 계획을 밝혔다. 좋은 방산 수요와 dilution/capital allocation watch가 동시에 존재하는 케이스다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / FT reported event and capital-raising anchors

stage3_price:
N/A

Poland_missile_JV:
CGR-080 guided missile production in Poland

capital_raise_initial:
3.6T won / $2.46B

capital_raise_event_MAE:
-13%

affiliate_share_issue:
1.3T won

rights_offering:
2.3T won

total_revised_raise:
1.3T + 2.3T
= 3.6T won

affiliate_issue_price:
758,000원/share

capital_raise_usd_equivalent_at_Reuters_FX:
3.6T / 1,464
= 약 $2.46B

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate + aligned_4B_detection
rerating_result = defense_localization_watch_with_dilution
stage_failure_type = 4B_watch_not_hard_4C
```

---

## Case E — Samsung E&A / GS건설 `success_candidate / overseas EPC backlog`

```text
symbols = 028050 / 006360
case_type = success_candidate + 4B-watch
archetype = OVERSEAS_EPC_CONTRACT_BACKLOG
```

### stage date

```text
Stage 1:
2024-04-02
- Saudi Aramco Fadhili gas expansion
- Middle East gas EPC capex cycle

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

Saudi Aramco는 Fadhili gas plant 확장을 위해 77억 달러 EPC 계약을 발주했고, Samsung Engineering, GS E&C, Nesma & Partners가 수주자로 포함됐다. Samsung E&A는 이 중 약 60억 달러 계약을 따낸 것으로 보도됐고, 주가는 장중 8.5% 상승해 26,750원까지 올랐다. Fadhili plant의 처리능력은 하루 25억 scf에서 40억 scf로 늘어나는 구조다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / WSJ reported contract and price anchors

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

Fadhili_capacity_before:
2.5B scf/day

Fadhili_capacity_after:
4.0B scf/day

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

## Case F — 현대건설 `success_candidate / Saudi gas infra backlog`

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

Aramco는 Jafurah gas field 2단계와 main gas network 3단계 확장에 250억 달러 이상 계약을 체결했다. Jafurah는 229조 입방피트 가스와 750억 배럴 condensates를 가진 대형 비전통 가스전이고, 2030년 하루 20억 scf 판매가스 생산을 목표로 한다. Hyundai Engineering & Construction consortium이 Jafurah 확장 계약 수주자에 포함됐다. ([Reuters][6])

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

## Case G — HD현대중공업 / HD현대미포 `event_premium + success_candidate`

```text
symbols = 329180 / 010620
case_type = success_candidate + 4B-watch
archetype = SHIPBUILDING_US_POLICY_MASGA
```

### stage date

```text
Stage 1:
2025-08
- U.S.-Korea shipbuilding cooperation
- MASGA / U.S. naval and maritime capacity theme

Stage 2:
2025-08-27
- HD Hyundai Heavy / HD Hyundai Mipo merger announcement
- U.S. shipbuilding market expansion target

Stage 3:
없음
- 합병·정책·MOU만으로 Green 금지
- funded order, contract amount, margin, FCF 확인 필요

Stage 4B:
2025-08-27
- HD Hyundai Heavy +11.3%
- HD Hyundai Mipo +14.6%
- both record highs

Stage 4C:
MOU 불발, 미국 예산 미반영, 수주 지연, integration cost, sanction risk 시 후보
```

HD현대중공업은 HD현대미포와 합병해 미국 조선시장 진출을 확대하겠다고 발표했고, 이는 한미 정상회담 이후의 MASGA 협력과 연결됐다. 발표 전후 HD현대중공업은 11.3%, HD현대미포는 14.6% 상승해 record high로 마감했다. 이는 좋은 Stage 2 후보이지만, funded order와 margin 전에는 Stage 3가 아니라 **4B-watch**다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported event return anchor

stage3_price:
N/A

HD_Hyundai_Heavy_event_MFE_1D:
+11.3%

HD_Hyundai_Mipo_event_MFE_1D:
+14.6%

record_high_status:
true

share_exchange_ratio:
1 HD Hyundai Mipo share = 1.04059146 HD Hyundai Heavy shares

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
success
- 정책/합병 뉴스로 record high면 4B-watch.
```

### alignment

```text
score_price_alignment = event_premium + success_candidate
rerating_result = U.S._shipbuilding_policy_watch
stage_failure_type = stage2_watch_success
```

---

## Case H — 한화오션 `4C-watch / geopolitical shipbuilding sanction`

```text
symbol = 042660
case_type = 4C-watch
archetype = GEOPOLITICAL_SHIPBUILDING_SANCTION
```

### stage date

```text
Stage 1:
2024~2025
- Philly Shipyard acquisition
- U.S. shipbuilding rebuild
- U.S. Navy MRO exposure

Stage 2:
미국 조선 재건 exposure는 Stage 2 후보

Stage 3:
없음
- U.S. 정책 / MRO / 투자계획만으로 Green 금지

Stage 4B:
미국 조선정책 기대가 가격에 먼저 반영된 구간이면 후보

Stage 4C-watch:
2025-10-14
- China sanctions five U.S.-linked Hanwha Ocean subsidiaries
- Hanwha Ocean close -5.8%
- China bans Chinese organizations/individuals from dealing with those entities
```

중국은 한화오션의 미국 관련 자회사 5곳을 제재했고, 중국 내 기업·개인이 이들과 거래·협력하는 것을 금지했다. Reuters는 이 발표 이후 한화오션 주가가 5.8% 하락했다고 보도했다. AP는 한화오션이 2024년 Philly Shipyard를 1억 달러에 인수했고, 2025년에는 미국 조선 인프라에 50억 달러 투자 계획을 발표했다고 정리했다. 이건 hard 4C라기보다 **geopolitical 4C-watch**다. 실제 매출·수주·중국 모듈 공급 차질이 확인되면 hard 4C로 승격한다. ([Reuters][8])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / AP reported event-return and investment anchors

stage3_price:
N/A

Hanwha_Ocean_event_MAE_close:
-5.8%

Philly_Shipyard_acquisition:
$100M

announced_U.S._investment:
$5B

investment_vs_acquisition_price:
5.0B / 0.1B
= 50x

sanctioned_entities:
5 U.S.-linked subsidiaries

sanction_type:
Chinese organizations and individuals banned from transactions/cooperation with those entities

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4C 큰 하락 이전 포착 여부:
partial_success
- sanction 당일 4C-watch 가능.
- hard 4C는 실제 revenue/contract disruption 확인 후.
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = geopolitical_sanction_watch
stage_failure_type = 4C_watch_not_hard_4C
```

---

# 5. 이번 R1 case별 요약표

| case               | 분류                               |                                                                실제 가격검증 | alignment                      |
| ------------------ | -------------------------------- | ---------------------------------------------------------------------: | ------------------------------ |
| LS Electric        | success_candidate / price failed | 208,500원, -5.4%; target upside +34.3%; $312M U.S. transformer contract | evidence_good_but_price_failed |
| 현대 로템              | structural_success               |        41,300원, +9.3%; K2 revenue 2,700억; Poland $6.5B second contract | aligned_partial                |
| LIG Nex1           | success_candidate + 4B           |                                      Iraq $2.8B, +3.6%; 1H +69% 후 -11% | export + crowding              |
| 한화에어로스페이스          | success_candidate + 4B           |                                   Poland missile JV; 3.6조 증자 발표 후 -13% | dilution 4B                    |
| Samsung E&A / GS건설 | success_candidate + 4B           |               Samsung E&A 26,750원, +8.5%; Fadhili $7.7B, Samsung 약 $6B | EPC Stage 2                    |
| 현대건설               | success_candidate                |          Aramco Jafurah/main gas >$25B, 4,000km pipeline, 3.2B scf/day | Stage 2                        |
| HD현대중공업/미포         | event + success_candidate        |                                          +11.3% / +14.6%, record highs | policy 4B                      |
| 한화오션               | 4C-watch                         |                            China sanctions, -5.8%; U.S. investment $5B | geopolitical watch             |

---

# 6. score-price alignment 판정

```text
aligned / structural_success_candidate:
- 현대 로템

success_candidate:
- LS Electric
- LIG Nex1
- 한화에어로스페이스
- Samsung E&A / GS건설
- 현대건설
- HD현대중공업 / HD현대미포

evidence_good_but_price_failed:
- LS Electric

event_premium:
- HD현대중공업 / HD현대미포 MASGA/merger event
- Samsung E&A 수주 발표일 rally

thesis_break_watch:
- 한화오션 China sanctions
- 한화에어로스페이스 dilution/capital allocation
- EPC working-capital / low-margin risk

4B-watch:
- LIG Nex1 1H +69% 후 downgrade/매도
- 한화에어로스페이스 3.6조 증자 shock
- Samsung E&A 수주 발표 당일 +8.5%
- HD현대중공업/미포 record highs
- 전력기기 transformer theme이 company-level margin보다 먼저 multiple화되는 구간

4C-watch:
- 한화오션 China sanctions
- EPC cost overrun / margin miss
- transformer cycle peak-out
- local production / technology transfer margin dilution
```

---

# 7. 점수비중 교정

## 올릴 축

```text
confirmed_contract_amount +5
order_to_revenue_conversion +5
delivery_schedule +4
backlog_margin_visibility +5
customer_quality +4
capacity_bottleneck +4
U.S._grid_exposure +4
defense_localization_with_margin +4
price_path_alignment +5
```

### 왜 올리나

현대로템은 수주가 납품·매출·영업이익 revision으로 내려온 Stage 3 후보이고, LS Electric은 U.S. transformer shortage 속에서 회사 단위 계약까지 확인된 Stage 2 후보다. Samsung E&A와 현대건설도 대형 EPC 수주와 가스 인프라 cycle이라는 Stage 2 evidence가 있다. 하지만 모두 **마진·현금회수·working capital** 확인 전 Green은 아니다.

## 내릴 축

```text
contract_headline_without_margin -5
policy_or_MOU_without_order -5
record_high_on_policy_event -4
unconfirmed_US_shipbuilding_policy_premium -4
geopolitical_sanction_unpriced -4
equipment_cycle_without_margin -3
EPC_backlog_without_cashflow -4
dilution_after_rerating -5
local_production_margin_unclear -3
```

### 왜 내리나

HD현대중공업/미포는 좋은 조선정책 Stage 2지만 record high는 4B다. 한화에어로스페이스는 좋은 방산 수요에도 대형 증자가 나오면 4B/capital allocation watch가 붙는다. 한화오션은 U.S. shipbuilding exposure가 좋아도 중국 제재라는 지정학 4C-watch가 붙는다.

## Green gate 강화 조건

```text
R1 Stage 3-Green 필수:
1. 계약금액 확인
2. 계약기간 / 납기 확인
3. 실제 납품 또는 매출 인식 확인
4. OPM / EPS revision 확인
5. 수주잔고 품질 확인
6. 현금흐름 / working capital 통과
7. 지정학·제재·financing·dilution risk 통과
8. 가격경로가 evidence 이후 따라옴

금지:
수주 headline만 있음
정책/MOU만 있음
record high event rally
마진 불명
EPC cash collection 불명
local production economics 불명
geopolitical sanction risk 무시
```

## 4B 조기감지 조건

```text
4B-watch:
정책/합병/MOU 이벤트로 record high
preferred bidder / export headline 단계에서 이미 +40~70% 상승
대형 수주 발표일 급등
전력기기 theme이 company-level order보다 먼저 multiple화
대형 증자 / CB / CAPEX after rerating
좋은 뉴스에도 주가 반응 둔화 또는 하락

4B-elevated:
증자 / CB / 대형 CAPEX
margin visibility 약화
EPC working capital 악화
미국/중국 제재 충돌
수주잔고 대비 valuation 과열
```

## 4C hard gate 조건

```text
계약 취소
final contract failure
EPC cost overrun
margin collapse
working capital deterioration
고객 지급 지연
geopolitical sanction causing revenue disruption
U.S. / China policy reversal
local production failure
equipment order cycle peak-out
dilution without FCF conversion
```

이번 R1 Loop 10에서 hard 4C는 억지로 확정하지 않는다. 한화오션은 hard 4C가 아니라 **4C-watch**다. 실제 매출·수주·중국 모듈 공급 차질이 확인되면 hard 4C로 승격한다.

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

## docs/round/round_159.md 요약

```md
# R1 Loop 10. Industrial Orders / Infrastructure Price Validation

이번 라운드는 R1 Loop 10 price-validation 라운드다.

핵심 결론:
- LS Electric은 U.S. grid/data-center growth story가 강하고, Reuters에서 $312M U.S. transformer contract가 확인된다. 그러나 2024-07-01 Daiwa target upgrade 당일 주가는 -5.4% to 208,500원이었다. Evidence good but price failed.
- Hyundai Rotem은 R1 structural success benchmark다. 2024-04-09 K2 delivery/revenue/OP revision evidence에서 +9.3% to 41,300원, KOSPI 대비 +9.6pp 아웃퍼폼했다. 2025 Poland second K2 contract $6.5B and Peru framework support Stage 2 continuation.
- LIG Nex1 is a missile-defense export platform candidate. Iraq $2.8B order drove +3.6%, but after a +69% 1H rally, shares fell -11% after downgrade/crowding concern.
- Hanwha Aerospace has Poland missile local-production JV Stage 2 evidence, but the 3.6T won capital raise plan caused -13% selloff. This is 4B/dilution watch, not hard 4C.
- Samsung E&A / GS E&C Fadhili EPC is Stage 2. Samsung E&A rose +8.5% to 26,750원 on estimated $6B contract within Aramco’s $7.7B project, but EPC margin/cash collection are required before Stage 3.
- Hyundai E&C Jafurah/main gas network exposure is Stage 2. Aramco package >$25B, 4,000km pipelines, +3.2B scf/day network capacity, but company margin/cashflow and price path unavailable.
- HD Hyundai Heavy / HD Hyundai Mipo MASGA merger event is Stage 2 + 4B. Shares rose +11.3% / +14.6% to record highs before funded U.S. orders or margin evidence.
- Hanwha Ocean China sanctions are geopolitical 4C-watch. Shares fell -5.8%; hard 4C requires actual contract/revenue disruption.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 159 R1 Loop 10 Industrial Infra Price Validation

## 반영 내용
- R1 Loop 10 price-validation 라운드를 추가했다.
- Power-equipment/grid, missile-defense export, K2 order-to-revenue, defense localization JV, overseas EPC, Saudi gas infra, U.S. shipbuilding policy, geopolitical shipbuilding sanction을 비교했다.
- Reuters/WSJ/MarketWatch/FT reported anchors로 가능한 MFE/MAE 및 contract/event metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- confirmed contract amount, order-to-revenue conversion, delivery schedule, backlog margin visibility, customer quality, U.S. grid exposure 가중치 강화
- contract headline without margin, policy/MOU without funded order, record-high policy event, dilution after rerating, geopolitical sanction unpriced 감점 강화
- R1 4B-watch와 geopolitical 4C-watch 민감도 강화
```

## case row 초안

```jsonl
{"case_id":"r1_loop10_ls_electric_grid_transformer_price_failed","symbol":"010120","company_name":"LS ELECTRIC","case_type":"success_candidate","primary_archetype":"GRID_POWER_EQUIPMENT_AI_DATACENTER","stage2_date":"2024-07-01/2025-11","price_validation":{"price_data_source":"MarketWatch price/target anchor + Reuters transformer contract anchor","stage3_price":null,"stage2_price_anchor":208500,"stage2_event_mae_1d_pct":-5.4,"target_price":280000,"target_upside_pct":34.3,"target_raise_pct":86.7,"us_revenue_share_2024_expected_pct":20,"us_revenue_share_2022_max_pct":5,"minimum_relative_mix_increase_pct":300,"us_utility_transformer_contract_usd_mn":312,"contract_product":"525kV extra-high-voltage transformers","delivery_window":"2027-2029","gsu_transformer_demand_growth_pct":274,"substation_transformer_demand_growth_pct":116,"transformer_price_increase_5y_pct":80,"large_transformer_lead_time_years":4,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"evidence_good_but_price_failed","rerating_result":"U.S._grid_power_equipment_watch","notes":"Strong grid/data-center evidence and company contract, but event price failed; Stage 3 requires delivery, margin and FCF."}
{"case_id":"r1_loop10_hyundai_rotem_k2_export_aligned","symbol":"064350","company_name":"Hyundai Rotem","case_type":"structural_success","primary_archetype":"DEFENSE_EXPORT_ORDER_TO_REVENUE","stage3_date":"2024-04-09","stage2_followup_date":"2025-08-01/2025-12-09","price_validation":{"price_data_source":"WSJ/Reuters price and contract anchors","stage3_price":41300,"stage3_event_mfe_1d_pct":9.3,"implied_pre_event_reference_price":37786,"kospi_same_context_pct":-0.3,"relative_outperformance_pp":9.6,"k2_export_revenue_1q_krw_bn":270,"op_growth_estimate_pct":85,"kb_target_price":47500,"target_upside_from_stage3_price_pct":15.0,"poland_second_contract_usd_bn":6.5,"poland_second_contract_units":180,"poland_local_production_units":61,"peru_framework_units_total":195,"peru_k2_units":54,"peru_wheeled_armored_units":141,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"aligned_partial","rerating_result":"defense_export_revenue_conversion","notes":"K2 delivery/revenue/OP revision makes this a Stage 3 candidate; follow-up Poland/Peru contracts support Stage 2 continuation."}
{"case_id":"r1_loop10_lig_nex1_cheongung_export_crowding","symbol":"079550","company_name":"LIG Nex1","case_type":"success_candidate","primary_archetype":"MISSILE_DEFENSE_EXPORT_PLATFORM","stage2_date":"2024-09-20","stage4b_date":"2024-07-02","price_validation":{"price_data_source":"Reuters/MarketWatch reported price and contract anchors","stage3_price":null,"iraq_contract_krw_trn":3.71,"iraq_contract_usd_bn":2.8,"saudi_prior_contract_usd_bn":3.2,"stage2_event_mfe_1d_pct":3.6,"wider_market_same_context_pct":0.9,"relative_outperformance_pp":2.7,"first_half_2024_stock_gain_pct":69,"kospi_first_half_2024_gain_pct":5.4,"first_half_relative_outperformance_pp":63.6,"stage4b_event_mae_pct":-11,"stage4b_close_price":195700,"implied_pre_4b_reference_price":219888,"q2_op_estimate_krw_bn":56.2,"q2_op_growth_estimate_pct":40,"target_price":200000,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_4b_watch","rerating_result":"missile_defense_export_platform_watch","notes":"Iraq export validates Stage 2, but 1H +69% and downgrade selloff show 4B/crowding risk."}
{"case_id":"r1_loop10_hanwha_aerospace_poland_missile_jv_dilution_watch","symbol":"012450","company_name":"Hanwha Aerospace","case_type":"success_candidate","primary_archetype":"DEFENSE_LOCAL_PRODUCTION_JV","stage2_date":"2025-04-15","stage4b_date":"2025-03-21","price_validation":{"price_data_source":"Reuters/FT event and capital-raising anchors","stage3_price":null,"poland_missile_jv_product":"CGR-080 guided missiles for K239 Chunmoo","capital_raise_initial_krw_trn":3.6,"capital_raise_initial_usd_bn":2.46,"capital_raise_event_mae_pct":-13,"affiliate_share_issue_krw_trn":1.3,"rights_offering_krw_trn":2.3,"total_revised_raise_krw_trn":3.6,"affiliate_issue_price_krw":758000,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_aligned_4B_detection","rerating_result":"defense_localization_watch_with_dilution","notes":"Poland missile JV is Stage 2; large capital raise after rerating is 4B/dilution watch, not hard 4C."}
{"case_id":"r1_loop10_samsung_ea_gs_fadhili_epc","symbol":"028050/006360","company_name":"Samsung E&A / GS E&C","case_type":"success_candidate","primary_archetype":"OVERSEAS_EPC_CONTRACT_BACKLOG","stage2_date":"2024-04-03","stage4b_date":"2024-04-03","price_validation":{"price_data_source":"Reuters/WSJ contract and price anchors","stage3_price":null,"samsung_ea_event_peak_price":26750,"samsung_ea_event_mfe_1d_pct":8.5,"implied_pre_event_reference_price":24654,"kospi_same_context_pct":-1.4,"relative_outperformance_pp":9.9,"aramco_total_fadhili_contracts_usd_bn":7.7,"samsung_ea_contract_estimate_usd_bn":6.0,"samsung_share_of_total_project_pct":77.9,"fadhili_capacity_before_bscfd":2.5,"fadhili_capacity_after_bscfd":4.0,"capacity_increase_pct":60,"kb_target_price":35000,"target_upside_from_event_peak_pct":30.8,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate","rerating_result":"EPC_backlog_watch","notes":"Large EPC contract is Stage 2; Stage 3 requires margin, progress revenue, cash collection and working-capital control."}
{"case_id":"r1_loop10_hyundai_ec_jafurah_gas_infra","symbol":"000720","company_name":"Hyundai E&C","case_type":"success_candidate","primary_archetype":"SAUDI_GAS_INFRA_BACKLOG","stage2_date":"2024-06-30","price_validation":{"price_data_source":"Reuters contract/infrastructure evidence","stage3_price":null,"aramco_contract_package_usd_bn":25.0,"jafurah_reserves_tcf":229,"jafurah_condensates_bbl_bn":75,"jafurah_sales_gas_target_bscfd":2.0,"main_gas_network_added_capacity_bscfd":3.2,"main_gas_network_added_pipeline_km":4000,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"Saudi_gas_infra_backlog_watch","notes":"Sovereign gas-infra contract is Stage 2; margin, progress revenue and cash recovery required before Green."}
{"case_id":"r1_loop10_hd_hyundai_heavy_mipo_masga_event","symbol":"329180/010620","company_name":"HD Hyundai Heavy / HD Hyundai Mipo","case_type":"success_candidate","primary_archetype":"SHIPBUILDING_US_POLICY_MASGA","stage2_date":"2025-08-27","stage4b_date":"2025-08-27","price_validation":{"price_data_source":"Reuters reported event return anchor","stage3_price":null,"hd_hyundai_heavy_mfe_1d_pct":11.3,"hd_hyundai_mipo_mfe_1d_pct":14.6,"record_high_status":true,"share_exchange_ratio_mipo_per_heavy":1.04059146,"price_validation_status":"reported_event_return_not_full_ohlc"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"U.S._shipbuilding_policy_watch","notes":"Merger/MASGA is Stage 2 and 4B-watch; funded order and margin required for Stage 3."}
{"case_id":"r1_loop10_hanwha_ocean_china_sanction_watch","symbol":"042660","company_name":"Hanwha Ocean","case_type":"4c_watch","primary_archetype":"GEOPOLITICAL_SHIPBUILDING_SANCTION","stage4c_date":"2025-10-14","price_validation":{"price_data_source":"Reuters/AP event-return and investment anchors","stage3_price":null,"hanwha_ocean_close_mae_pct":-5.8,"philly_shipyard_acquisition_usd_mn":100,"announced_us_investment_usd_bn":5.0,"investment_vs_acquisition_multiple":50,"sanctioned_entities":5,"sanction_type":"Chinese entities banned from transactions/cooperation with sanctioned U.S.-linked subsidiaries","price_validation_status":"reported_event_return_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"geopolitical_sanction_watch","notes":"China sanctions are 4C-watch; hard 4C requires actual revenue/contract disruption."}
```

## shadow weight row 초안

```csv
archetype,contract_amount,order_to_revenue,delivery_schedule,backlog_margin,customer_quality,capacity_bottleneck,us_grid_exposure,price_path_alignment,event_penalty,geopolitical_redteam,dilution_redteam,4b_watch_sensitivity,hard_4c_sensitivity,notes
GRID_POWER_EQUIPMENT_AI_DATACENTER,+4,+4,+4,+5,+4,+5,+5,+3,-2,+1,+1,+4,+3,LS Electric has strong U.S. grid evidence but event price failed; margin/FCF required.
DEFENSE_EXPORT_ORDER_TO_REVENUE,+5,+5,+5,+5,+5,+0,+0,+5,-1,+2,+1,+4,+3,Hyundai Rotem shows delivery/revenue/OP revision can support Stage 3.
MISSILE_DEFENSE_EXPORT_PLATFORM,+5,+4,+4,+5,+5,+0,+0,+3,-2,+2,+1,+5,+3,LIG Nex1 export platform is good but crowding after +69% rally requires 4B-watch.
DEFENSE_LOCAL_PRODUCTION_JV,+4,+4,+5,+5,+5,+0,+0,+3,-3,+2,+5,+5,+4,Hanwha Aerospace localization is Stage 2; dilution after rerating is 4B-watch.
OVERSEAS_EPC_CONTRACT_BACKLOG,+5,+4,+4,+5,+5,+0,+0,+4,-3,+2,+2,+4,+4,Samsung E&A/GS Fadhili is Stage 2; margin/cash collection required.
SAUDI_GAS_INFRA_BACKLOG,+5,+4,+4,+5,+5,+0,+0,+2,-3,+2,+1,+3,+4,Hyundai E&C Jafurah is Stage 2 until margin and cash recovery confirm.
SHIPBUILDING_US_POLICY_MASGA,+4,+3,+4,+5,+4,+2,+0,+3,-5,+3,+1,+5,+4,HD Hyundai/Mipo merger is Stage 2 and 4B-watch until funded orders/margins confirm.
GEOPOLITICAL_SHIPBUILDING_SANCTION,+0,+0,+0,+0,+0,+0,+0,+2,0,+5,+1,+3,+5,Hanwha Ocean China sanctions require 4C-watch.
```

---

# 이번 R1 Loop 10 결론

R1은 Stage 3가 실제로 대형 수익률을 만들 수 있는 섹터지만, **수주 headline과 Stage 3를 혼동하면 false positive가 빠르게 쌓인다.**

```text
1. LS Electric은 transformer bottleneck과 U.S. data-center contract가 확인된 좋은 Stage 2 후보지만,
   event-day price가 실패했으므로 Green은 보류해야 한다.

2. Hyundai Rotem은 R1의 aligned success 후보다.
   K2 납품이 매출·OP revision으로 내려온 뒤 가격이 반응했다.

3. LIG Nex1은 missile-defense export platform이지만,
   상반기 +69% 후 -11% 조정이 보여주듯 4B/crowding을 빨리 붙여야 한다.

4. Hanwha Aerospace는 defense localization Stage 2 후보지만,
   대형 증자와 dilution risk가 4B-watch다.

5. Samsung E&A / GS E&C와 Hyundai E&C는 좋은 EPC Stage 2 후보지만,
   마진·공정률·현금회수 전 Stage 3 금지다.

6. HD Hyundai Heavy / Mipo는 MASGA/merger record-high event이므로
   funded U.S. order와 margin 전에는 Stage 2 + 4B-watch다.

7. Hanwha Ocean은 U.S. shipbuilding exposure가 좋아도
   China sanctions라는 지정학 4C-watch가 붙는다.
```

한 문장으로 압축하면:

> **R1에서 진짜 Stage 3는 “수주·전력기기·방산·조선정책이 좋다”가 아니라, 계약이 납품·매출·마진·EPS revision·현금흐름으로 내려오고 가격경로가 그 뒤를 따라오는 순간이다.**
> **이번 R1 Loop 10은 전력기기·방산·EPC·조선의 좋은 Stage 2 후보를 인정하되, price-fail·crowding·dilution·정책 record high·지정학 제재를 4B/4C로 분리하는 라운드다.**

[1]: https://www.marketwatch.com/story/ls-electric-could-gain-from-solid-u-s-business-growth-opportunity-market-talk-3e926067?utm_source=chatgpt.com "LS Electric Could Gain From Solid U.S. Business Growth Opportunity -- Market Talk"
[2]: https://www.wsj.com/articles/hyundai-rotem-rallies-on-hopes-tank-exports-will-boost-earnings-9322d840?utm_source=chatgpt.com "Hyundai Rotem Rallies on Hopes Tank Exports Will Boost Earnings"
[3]: https://www.reuters.com/business/aerospace-defense/south-koreas-lig-nex1-wins-28-bln-deal-with-iraq-export-missile-systems-2024-09-19/?utm_source=chatgpt.com "South Korea's LIG Nex1 wins $2.8 bln Iraq deal to export missile systems"
[4]: https://www.reuters.com/business/aerospace-defense/south-koreas-hanwha-aerospace-produce-missiles-poland-2025-04-15/?utm_source=chatgpt.com "South Korea's Hanwha Aerospace to produce missiles in Poland"
[5]: https://www.reuters.com/markets/commodities/aramco-awards-77-bln-contracts-fadhili-gas-expansion-2024-04-02/?utm_source=chatgpt.com "Aramco awards $7.7 bln in contracts for Fadhili gas expansion"
[6]: https://www.reuters.com/business/energy/aramco-signs-over-25-bln-deals-main-gas-network-jafurah-gas-field-2024-06-30/?utm_source=chatgpt.com "Aramco signs over $25 bln of deals for main gas network and Jafurah gas field"
[7]: https://www.reuters.com/markets/emerging/south-korean-shipbuilder-hd-hyundai-heavy-merge-with-affiliate-hd-hyundai-mipo-2025-08-27/?utm_source=chatgpt.com "South Korean shipbuilder HD Hyundai Heavy to merge with affiliate HD Hyundai Mipo"
[8]: https://www.reuters.com/world/asia-pacific/china-takes-steps-against-us-linked-units-skorea-shipbuilder-hanwha-2025-10-14/?utm_source=chatgpt.com "China takes steps against US-linked units of S.Korea shipbuilder Hanwha"

순서상 이번은 **R1 Loop 11 — 산업재·수주·인프라 가격경로 검증 라운드**다.

이번 R1 Loop 11은 이전 R1에서 많이 쓴 “전력기기·방산이 좋다” 수준을 넘겨서, **원전 EPC 수출, 조선 MRO/IPO, 전력망·케이블, MASGA 조선정책, 방산 현지생산, rail export, shipbuilding contract cancellation, 지정학 제재**를 한 번에 비교한다.

```text
round = R1 Loop 11
round_id = round_172
large_sector = INDUSTRIAL_ORDERS_INFRA
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true
```

이번에도 full adjusted OHLC 전체 구간은 안정적으로 확보하지 못했다. 대신 Reuters / AP / WSJ / MarketWatch가 제공한 **가격 anchor, 이벤트 수익률, 계약금액, 수주규모, IPO 가격, 취소계약금액, dilution event**로 계산 가능한 값만 계산했다. 30D/90D/180D 전체 OHLC가 없는 항목은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R1 = 산업재·수주·인프라
```

R1의 Stage 3는 “수주가 있다”가 아니라, **수주가 납품·매출·마진·EPS revision·현금회수로 내려오고, 가격경로가 그 뒤를 따라오는 순간**이다.

---

# 2. 대상 canonical archetype

```text
NUCLEAR_EPC_EXPORT_ORDER
NUCLEAR_SMR_POLICY_MOU
POWER_GRID_CABLE_TRANSFORMER_EXPORT
MARINE_MRO_RECURRING_SERVICE
SHIPBUILDING_US_POLICY_MASGA
SHIPBUILDING_CONTRACT_CANCELLATION_4C
DEFENSE_LOCAL_PRODUCTION_DILUTION_WATCH
RAIL_EXPORT_ORDER_TO_DELIVERY
GEOPOLITICAL_SHIPBUILDING_SANCTION
CONTRACT_HEADLINE_NOT_STAGE3
PRICE_ONLY_POLICY_RALLY
```

---

# 3. deep sub-archetype

```text
원전 EPC:
- KHNP / Doosan Enerbility / KEPCO E&C / KEPCO KPS
- Czech Dukovany preferred bidder → legal block → signed contract
- $18.7B project
- subcontract package / margin / cash collection before Green

SMR / AI power:
- Doosan Enerbility / X-energy / AWS / Fermi America
- SMR equipment MOU / U.S. AI project
- policy/MOU event vs funded order

전력망·케이블:
- LS Electric
- LS Corp / LS Cable
- U.S. data-center grid demand
- Belgium Elia cable contract
- transformer/cable bottleneck
- event price failed vs contract visibility

조선 MRO:
- HD Hyundai Marine Solution
- maintenance / repair / retrofit
- eco-friendly vessel servicing
- IPO premium vs recurring service margin

조선정책:
- HD Hyundai Heavy / HD Hyundai Mipo
- MASGA / U.S. shipbuilding revival
- merger / record-high event
- funded U.S. order before Green

계약취소:
- Samsung Heavy / Zvezda
- Russia sanctions / war
- $3.54B icebreaker LNG/tanker order cancellation
- arbitration / advance-payment risk

방산 현지생산:
- Hanwha Aerospace
- Poland missile JV
- CGR-080 for K239 Chunmoo
- dilution / capital raise after rerating

철도:
- Hyundai Rotem Morocco ONCF
- 110 urban trains
- $1.54B / 2.2T won order
- delivery / margin / working capital before Green

지정학 제재:
- Hanwha Ocean
- China sanctions on U.S.-linked subsidiaries
- U.S. shipbuilding support vs China retaliation
```

---

# 4. 국장 신규 후보 case

## Case A — Doosan Enerbility / Czech nuclear `success_candidate + legal-watch`

```text
symbol = 034020 / 052690 / 051600 / 015760
case_type = success_candidate + legal_watch
archetype = NUCLEAR_EPC_EXPORT_ORDER
```

### stage date

```text
Stage 1:
2024-07-17
- KHNP selected as preferred bidder for Czech Dukovany reactors
- South Korea’s first large overseas nuclear order since 2009
- Doosan Enerbility / KEPCO E&C / KEPCO KPS pre-rally

Stage 2:
2025-06-04
- Czech Republic signs contract with KHNP
- two new Dukovany reactors
- total cost 407B koruna / $18.7B
- first trial operation expected 2036, second around 2038

Stage 3:
없음
- KHNP contract signing은 강한 Stage 2
- Doosan / KEPCO E&C / KEPCO KPS의 actual package, margin, cash collection 확인 전 Green 금지

Stage 4B:
2024-07 이전
- Doosan Enerbility +48% over three months
- KEPCO E&C +41%
- KEPCO Plant S&E +14%

Stage 4C-watch:
2025-05-06
- EDF legal challenge temporarily blocked signing
- court/legal delay risk
```

Reuters는 2024년 7월 KHNP가 Czech Dukovany 원전 2기 우선협상대상자로 선정됐고, 관련 기대 속에서 Doosan Enerbility가 3개월 동안 48%, KEPCO E&C가 41%, KEPCO Plant S&E가 14% 올랐다고 보도했다. 이후 2025년 5월 EDF의 법적 challenge로 계약 체결이 일시 차단됐지만, 2025년 6월 Czech 정부는 KHNP와 407B koruna, 약 187억 달러 규모의 2기 계약을 체결했다. 이건 “preferred bidder”에서 “signed contract”로 올라온 강한 Stage 2다. 하지만 상장사별 실제 package와 margin이 확인되기 전 Stage 3는 아니다. ([Reuters][1])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / AP nuclear-contract and sector-return anchors

stage3_price:
N/A

reported_3M_MFE_before_preferred_bidder:
Doosan Enerbility +48%
KEPCO Plant S&E +14%
KEPCO E&C +41%

Czech_contract_value:
407B koruna / $18.7B

reactors:
2 new Dukovany units

unit_cost_context:
about 200B koruna / $9.1B per reactor

trial_operation_expected:
first reactor 2036
second reactor around 2038

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
partial_success
- preferred bidder 전후 이미 3개월 +48% / +41%라 4B-watch 필요.
```

### alignment

```text
score_price_alignment = success_candidate + 4B_watch
rerating_result = nuclear_EPC_export_watch
stage_failure_type = stage2_watch_success_not_green
```

---

## Case B — Doosan Enerbility / U.S. SMR·AI power `event_premium / MOU watch`

```text
symbol = 034020
case_type = success_candidate + event_premium
archetype = NUCLEAR_SMR_POLICY_MOU
```

### stage date

```text
Stage 1:
2025-08-26
- Korea-U.S. summit investment package
- AI / nuclear / SMR / U.S. infrastructure cooperation

Stage 2:
2025-08-26
- Doosan Enerbility joins X-energy / AWS SMR cooperation
- Doosan also strikes agreement with Fermi America for nuclear/SMR equipment for Texas AI project
- KHNP / Samsung C&T also linked to Fermi construction MOU

Stage 3:
없음
- MOU / policy cooperation만으로 Green 금지
- funded order, equipment package, delivery schedule, margin, cash collection 확인 필요

Stage 4B:
SMR / AI power headline로 원전주가 먼저 과열되면 후보

Stage 4C:
MOU 미전환, U.S. permitting delay, SMR economics failure, financing failure
```

Reuters는 2025년 한미 정상회담 관련 투자계획에서 KHNP와 Doosan Enerbility가 X-energy·AWS와 SMR design, construction, supply-chain 협력을 추진하고, Doosan Enerbility가 Fermi America의 Texas AI project에 nuclear/SMR equipment 공급 관련 agreement를 맺었다고 보도했다. 이건 AI 전력수요와 원전 공급망이 만나는 좋은 Stage 2 후보지만, funded order가 아니면 Green이 아니다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters U.S. investment / SMR policy-MOU anchor

stage3_price:
N/A

Doosan_stock_OHLC:
price_data_unavailable_after_deep_search

announced_context:
South Korean firms pledge $150B U.S. investments

nuclear_partners:
X-energy
Amazon Web Services
Fermi America
KHNP
Samsung C&T

confirmed_revenue:
false

funded_order:
not confirmed

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium / success_candidate
rerating_result = SMR_AI_power_policy_watch
stage_failure_type = MOU_not_green
```

---

## Case C — LS Electric / LS Corp cable-grid `success_candidate + evidence_good_but_price_failed`

```text
symbols = 010120 / 006260
case_type = success_candidate + evidence_good_but_price_failed
archetype = POWER_GRID_CABLE_TRANSFORMER_EXPORT
```

### stage date

```text
Stage 1:
2024
- U.S. data-center construction boom
- renewable grid expansion
- EV value-chain grid demand
- cable / transformer bottleneck

Stage 2:
2024-06-20
- LS secures 282.13B won contract to supply electrical power cables to Belgium’s Elia Asset NV

Stage 2:
2024-07-01
- Daiwa raises LS Electric target 150,000원 → 280,000원
- U.S. revenue share expected to rise from below 5% in 2022 to around 20% in 2024
- but shares -5.4% at 208,500원

Stage 3:
보류
- 계약·U.S. mix는 좋음
- event-day price failed + delivery/margin/FCF 확인 전 Green 금지

Stage 4B:
grid / transformer / cable theme이 company delivery보다 먼저 multiple화되면 후보

Stage 4C:
data-center grid order delay, copper/steel cost, margin squeeze, transformer cycle normalization
```

LS 쪽은 좋은 R1 Stage 2 후보다. LS는 Belgium Elia Asset NV에 2,821.3억 원 규모 전력케이블 공급계약을 확보했고, LS Electric은 U.S. data-center와 renewable grid 수요로 미국 매출 비중이 2022년 5% 미만에서 2024년 20% 수준까지 올라갈 수 있다는 분석을 받았다. 다만 LS Electric은 목표가 상향 당일 오히려 5.4% 하락해 208,500원이었다. 즉 증거는 좋지만 가격경로는 즉시 실패한 `evidence_good_but_price_failed`다. ([마켓워치][3])

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch contract / target / price anchors

stage3_price:
N/A

LS_power_cable_contract:
282.13B won

customer:
Elia Asset NV, Belgium

LS_Electric_stage2_price_anchor:
208,500원

LS_Electric_stage2_event_MAE:
-5.4%

target_price:
280,000원

target_raise:
280,000 / 150,000 - 1
= +86.7%

target_upside_from_stage2_price:
280,000 / 208,500 - 1
= +34.3%

U.S._revenue_share_2022:
below 5%

U.S._revenue_share_expected_2024:
around 20%

minimum_mix_increase:
20 / 5 - 1
= +300% 이상

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = evidence_good_but_price_failed
rerating_result = grid_cable_transformer_watch
stage_failure_type = stage2_not_green
```

---

## Case D — HD Hyundai Marine Solution `success_candidate + IPO 4B-watch`

```text
symbol = 443060
case_type = success_candidate + 4B-watch
archetype = MARINE_MRO_RECURRING_SERVICE
```

### stage date

```text
Stage 1:
2024-05
- marine after-sales / maintenance / repair / retrofit
- eco-friendly vessel servicing demand
- shipbuilding MRO recurring-service story

Stage 2:
2024-05-08
- IPO priced at 83,400원
- opened around 119,900원, +44%
- first-day close 163,900원, +97%
- IPO raised about 742B won
- 2023 earnings 151.1B won, +44%
- parent HD Hyundai retains 55.8%, KKR-managed vehicle 24.2%

Stage 3:
없음
- IPO premium만으로 Green 금지
- recurring service revenue, MRO backlog, retrofit margin, FCF 확인 필요

Stage 4B:
2024-05-08
- IPO debut +44% open / +97% close
- 가격이 실적검증보다 먼저 감

Stage 4C:
post-IPO valuation compression, ship-cycle slowdown, retrofit demand fade, KKR overhang
```

HD Hyundai Marine Solution은 “조선 MRO recurring service”라는 R1 구조 후보가 될 수 있다. Reuters Breakingviews는 이 회사가 maintenance, repair, reconstruction 같은 marine after-sales/retrofit 서비스를 제공하고, eco-friendly vessels demand 덕분에 2023년 earnings가 44% 증가해 1,511억 원을 기록했다고 보도했다. 하지만 IPO 가격 83,400원 대비 첫날 개장 +44%, 종가 +97%는 Stage 3가 아니라 4B다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters Breakingviews / WSJ IPO price anchors

IPO_price:
83,400원

opening_price:
119,900원

opening_MFE:
119,900 / 83,400 - 1
= +43.8%

first_day_close:
163,900원

first_day_close_MFE:
163,900 / 83,400 - 1
= +96.5%

IPO_raise:
742B won / about $546M

market_cap_close_context:
about 7.29T won / $5.36B

2023_earnings:
151.1B won

earnings_growth:
+44%

parent_HD_Hyundai_post_IPO_stake:
55.8%

KKR_vehicle_post_IPO_stake:
24.2%

MFE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
success
- IPO debut +96.5%면 recurring revenue 검증 전 4B.
```

### alignment

```text
score_price_alignment = success_candidate + 4B_watch
rerating_result = marine_MRO_recurring_service_watch
stage_failure_type = IPO_event_not_green
```

---

## Case E — HD Hyundai Heavy / HD Hyundai Mipo `event_premium + shipbuilding policy 4B`

```text
symbols = 329180 / 010620
case_type = success_candidate + event_premium
archetype = SHIPBUILDING_US_POLICY_MASGA
```

### stage date

```text
Stage 1:
2025-08
- MASGA / U.S.-Korea shipbuilding cooperation
- U.S. shipbuilding revival
- naval / icebreaker / Arctic demand

Stage 2:
2025-08-27
- HD Hyundai Heavy to merge with HD Hyundai Mipo
- exchange ratio: 1 Mipo share = 1.04059146 HD Hyundai Heavy shares
- U.S. shipbuilding expansion target
- U.S. icebreaker fleet allocation $8.6B cited as demand background

Stage 3:
없음
- merger / MASGA policy / U.S. demand headline만으로 Green 금지
- funded U.S. order, yard utilization, margin, FCF 확인 필요

Stage 4B:
2025-08-27
- HD Hyundai Heavy +11.3%
- HD Hyundai Mipo +14.6%
- both record highs
```

HD Hyundai Heavy와 HD Hyundai Mipo merger는 조선정책 Stage 2와 4B가 동시에 뜬 케이스다. Reuters는 합병이 U.S.-Korea shipbuilding cooperation, MASGA, naval/icebreaker 수요를 겨냥한 것이라고 설명했고, 발표일 HD Hyundai Heavy는 11.3%, HD Hyundai Mipo는 14.6% 상승해 record high를 기록했다. 하지만 funded U.S. order와 margin 전에는 Stage 3가 아니다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters merger / event-return anchor

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

U.S._Coast_Guard_icebreaker_fleet_context:
$8.6B allocation cited in Reuters source

MFE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
success
- funded U.S. order 전 record high면 4B.
```

### alignment

```text
score_price_alignment = event_premium + success_candidate
rerating_result = U.S._shipbuilding_policy_watch
stage_failure_type = stage2_watch_4B
```

---

## Case F — Samsung Heavy Industries / Zvezda cancellation `hard 4C / contract cancellation`

```text
symbol = 010140
case_type = 4C-thesis-break
archetype = SHIPBUILDING_CONTRACT_CANCELLATION_4C
```

### stage date

```text
Stage 1:
2020~2021
- Russia Zvezda icebreaker LNG / shuttle tanker orders
- Arctic LNG / Russia-linked shipbuilding backlog

Stage 2:
약함
- 대형 수주 backlog headline

Stage 3:
없음
- sanctions / shipowner / advance-payment / arbitration risk가 컸음

Stage 4C:
2025-06-18
- two Zvezda orders worth 4.85T won / $3.54B cancelled
- 10 icebreaker LNG carriers + 7 icebreaker shuttle tankers
- Samsung Heavy calls Zvezda termination illegal
- Singapore arbitration / damages claim
```

Samsung Heavy는 R1 조선의 contract-quality hard 4C다. Reuters는 Samsung Heavy가 Russia Zvezda와의 icebreaker LNG carrier·shuttle tanker 관련 2개 계약, 총 4.85조 원·35.4억 달러를 취소했다고 보도했다. 회사는 Zvezda가 2024년 6월 일방적으로 계약 해지를 통보하고 선급금 반환을 요구했으며, Samsung Heavy가 Singapore arbitration과 손해배상 청구에 나섰다고 밝혔다. 수주잔고 headline만으로 Green을 주면 안 된다는 기준점이다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters contract-cancellation anchor

stage3_price:
N/A

cancelled_contract_value:
4.85T won / $3.54B

orders:
10 icebreaker LNG carriers
7 icebreaker shuttle tankers

contract_origin:
2020 and 2021

shipowner:
Russia’s Zvezda

arbitration:
Singapore arbitration requested

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4C 큰 하락 이전 포착 여부:
hard gate event itself
- sanctions/war-linked customer risk should have been RedTeam before Green.
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = shipbuilding_contract_quality_failure
stage_failure_type = hard_4C
```

---

## Case G — Hanwha Aerospace `success_candidate + dilution 4B-watch`

```text
symbol = 012450
case_type = success_candidate + 4B-watch
archetype = DEFENSE_LOCAL_PRODUCTION_DILUTION_WATCH
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
- CGR-080 guided missiles for K239 Chunmoo
- technology transfer / local production model

Stage 3:
보류
- actual order volume, missile delivery, margin, cash collection, local production economics 필요

Stage 4B:
2025-03-21
- 3.6T won capital raise plan announced
- shares -13% next day
- FSS later ordered revision
- revised plan reduced to 2.3T won, plus affiliate issue 1.3T won

Stage 4C:
dilution without FCF, overseas factory overbuild, local-production margin dilution, governance issue
```

Hanwha Aerospace는 방산 현지생산 Stage 2 후보지만, 동시에 dilution 4B-watch다. Reuters는 Polish WB Electronics와 CGR-080 guided missile 생산 JV를 만들기로 했다고 보도했다. 그러나 그 직전 3.6조 원 유상증자 계획을 발표한 뒤 주가가 13% 급락했고, 금융감독원이 공시 보완을 요구했다. 이후 회사는 계획을 2.3조 원으로 줄이고, 별도 1.3조 원 affiliate share issue도 계획했다. 즉 좋은 수요와 dilution risk를 동시에 넣어야 한다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters missile-JV / capital-raising anchors

stage3_price:
N/A

Poland_missile_JV:
CGR-080 guided missiles in Poland

capital_raise_initial:
3.6T won / $2.46B

capital_raise_event_MAE:
-13%

revised_rights_offering:
2.3T won / $1.6B

affiliate_share_issue:
1.3T won

total_revised_related_raise:
2.3T + 1.3T
= 3.6T won

affiliate_issue_price:
758,000원/share

2025_guidance_revenue:
30T won

2025_guidance_OP:
3T won

2024_revenue:
11.24T won

2024_OP:
1.73T won

2025_OP_growth_vs_2024_guidance:
3 / 1.73 - 1
= +73.4%

MFE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
success
- rerating 이후 대형 증자 shock은 4B/dilution watch.
```

### alignment

```text
score_price_alignment = success_candidate + aligned_4B_detection
rerating_result = defense_localization_watch_with_dilution
stage_failure_type = 4B_watch_not_hard_4C
```

---

## Case H — Hyundai Rotem Morocco rail `success_candidate / rail export order`

```text
symbol = 064350
case_type = success_candidate
archetype = RAIL_EXPORT_ORDER_TO_DELIVERY
```

### stage date

```text
Stage 1:
2024~2025
- Morocco rail expansion
- 2030 World Cup transport infrastructure
- Korean rail export platform

Stage 2:
2025-02-26
- Morocco ONCF order
- Hyundai Rotem wins around 2.2T won / $1.54B order
- 110 urban / double-decker trains
- largest railway-business order for Hyundai Rotem

Stage 3:
보류
- order headline은 강함
- delivery schedule, margin, working capital, cash collection 확인 전 Green 금지

Stage 4B:
철도 수출 headline로 주가가 먼저 과열되면 후보

Stage 4C:
concessionary financing delay, delivery delay, cost overrun, FX/margin deterioration
```

Reuters는 Morocco ONCF가 2030 World Cup 준비를 위해 168대 train을 총 29억 달러에 구매하고, Hyundai Rotem이 110대 urban trains, 약 2.2조 원·15.4억 달러 규모 주문을 수주했다고 보도했다. 이는 Hyundai Rotem 철도사업부 역대 최대 수주다. 강한 Stage 2지만, 납품·마진·working capital 전 Stage 3는 아니다. ([Reuters][8])

### 실제 가격경로 검증

```text
price_data_source:
Reuters rail-contract evidence

stage3_price:
N/A

Hyundai_Rotem_stock_OHLC:
price_data_unavailable_after_deep_search

Morocco_total_train_purchase:
168 trains

Morocco_total_program_value:
$2.9B

Hyundai_Rotem_order_value:
2.2T won / $1.54B

Hyundai_Rotem_train_count:
110 urban trains

Hyundai_order_share_of_total_program:
1.54 / 2.9
= 53.1%

other_orders:
Alstom 18 high-speed trains
CAF 40 intercity trains

network_target:
43 cities / 87% of population by 2040

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = rail_export_order_watch
stage_failure_type = stage2_watch_success
```

---

## Case I — Hanwha Ocean China sanctions `4C-watch / geopolitical shipbuilding sanction`

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
- MASGA / U.S.-Korea shipbuilding cooperation

Stage 2:
미국 조선 재건 exposure는 Stage 2 후보

Stage 3:
없음
- U.S. 정책 / MRO / 투자계획만으로 Green 금지

Stage 4C-watch:
2025-10-14
- China sanctions five U.S.-linked Hanwha Ocean subsidiaries
- Hanwha Ocean close -5.8%
- HD Hyundai Heavy -4.1%
- China bans Chinese entities from transactions/cooperation with sanctioned units
```

Hanwha Ocean은 U.S. shipbuilding exposure가 좋아도 geopolitical 4C-watch가 붙는 케이스다. China는 Hanwha Ocean의 U.S.-linked subsidiaries 5곳을 제재했고, 중국 내 기관·개인이 이들과 거래·협력하는 것을 금지했다. Reuters는 발표 후 Hanwha Ocean이 5.8%, HD Hyundai Heavy가 4.1% 하락했다고 보도했다. Hanwha는 Philly Shipyard를 1억 달러에 인수했고, 이후 50억 달러 투자계획을 밝혔지만, 중국 제재가 실제 매출·부품·모듈 조달로 번지면 hard 4C로 승격된다. ([Reuters][9])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / AP sanction and price anchors

stage3_price:
N/A

Hanwha_Ocean_event_MAE_close:
-5.8%

HD_Hyundai_Heavy_same_context:
-4.1%

FT_intraday_context:
Hanwha Ocean down as much as -8%

sanctioned_entities:
5 U.S.-linked subsidiaries

Philly_Shipyard_acquisition:
$100M

announced_U.S._investment:
$5B

investment_vs_acquisition_price:
5.0B / 0.1B
= 50x

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4C 큰 하락 이전 포착 여부:
partial_success
- sanction 당일 4C-watch 가능.
- hard 4C는 실제 revenue / module / contract disruption 확인 후.
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = geopolitical_sanction_watch
stage_failure_type = 4C_watch_not_hard_4C
```

---

# 5. 이번 R1 case별 요약표

| case                       | 분류                             |                                                    실제 가격검증 | alignment          |
| -------------------------- | ------------------------------ | ---------------------------------------------------------: | ------------------ |
| Doosan / Czech nuclear     | success_candidate + 4B         |                 Doosan +48%, KEPCO E&C +41%, signed $18.7B | Stage 2            |
| Doosan / U.S. SMR-AI       | event premium                  |             X-energy/AWS/Fermi agreement, funded order 미확인 | MOU watch          |
| LS Electric / LS Corp      | evidence good but price failed | LS Electric 208,500원, -5.4%; LS cable 282.13B won contract | price failed       |
| HD Hyundai Marine Solution | success_candidate + 4B         |                  IPO 83,400→163,900, +96.5%; earnings +44% | IPO 4B             |
| HD Hyundai Heavy / Mipo    | event premium + 4B             |                              +11.3% / +14.6%, record highs | MASGA policy 4B    |
| Samsung Heavy              | hard 4C                        |                 Zvezda orders 4.85T won / $3.54B cancelled | contract failure   |
| Hanwha Aerospace           | success_candidate + 4B         |                   Poland missile JV; 3.6T raise shock -13% | dilution watch     |
| Hyundai Rotem rail         | success_candidate              |                      Morocco 2.2T won / $1.54B, 110 trains | Stage 2            |
| Hanwha Ocean               | 4C-watch                       |             China sanctions, -5.8%, HD Hyundai Heavy -4.1% | geopolitical watch |

---

# 6. score-price alignment 판정

```text
aligned / structural_success_candidate:
- 아직 이번 R1 Loop 11에서 full Stage 3 aligned 확정 없음

success_candidate:
- Czech nuclear infra
- LS grid/cable, 단 price failed
- HD Hyundai Marine Solution marine MRO
- Hanwha Aerospace defense localization
- Hyundai Rotem rail export
- Doosan SMR-AI power MOU, 단 MOU watch

event_premium:
- HD Hyundai Marine IPO
- HD Hyundai Heavy / Mipo MASGA merger
- Doosan SMR / AI power policy package

evidence_good_but_price_failed:
- LS Electric
- 일부 power-grid evidence는 좋지만 event-day 가격 실패

price_moved_without_evidence:
- SMR / AI power MOU rally if revenue/order not confirmed
- MASGA / U.S. shipbuilding policy rally before funded order
- IPO premium before recurring MRO margin

hard_4C:
- Samsung Heavy / Zvezda contract cancellation

4C-watch:
- Hanwha Ocean China sanctions
- Hanwha Aerospace dilution/capital allocation
- Czech nuclear legal delay
```

---

# 7. 점수비중 교정

## 올릴 축

```text
signed_contract +5
confirmed_contract_amount +5
order_to_revenue_conversion +5
delivery_schedule +4
backlog_margin_visibility +5
cash_collection_quality +5
recurring_MRO_service +4
customer_quality +4
geopolitical_risk_cleared +4
```

### 왜 올리나

Czech nuclear는 preferred bidder에서 signed contract로 승격됐고, Hyundai Rotem Morocco rail은 2.2조 원 규모의 확정 order가 있다. LS의 cable contract와 HD Hyundai Marine의 recurring MRO 구조도 Stage 2 가치가 있다. 다만 모두 **납품·마진·현금회수**가 없으면 Stage 3가 아니다.

## 내릴 축

```text
preferred_bidder_only -4
MOU_without_funded_order -5
policy_shipbuilding_headline -5
IPO_premium_without_post_listing_FCF -5
contract_headline_without_execution -5
geopolitical_customer_risk -5
Russia_or_sanctioned_customer_exposure -5
dilution_after_rerating -5
legal_delay_risk -4
```

### 왜 내리나

Samsung Heavy는 러시아 customer / war / sanctions risk가 contract cancellation으로 이어졌다. Hanwha Aerospace는 좋은 방산 cycle에서도 대형 증자 shock이 나타났다. HD Hyundai Marine과 HD Hyundai Heavy/Mipo는 좋은 story지만 IPO·MASGA·merger price가 실적보다 먼저 달렸다.

## Green gate 강화 조건

```text
R1 Stage 3-Green 필수:
1. signed contract 또는 firm order
2. 계약금액 / 고객 / 납기 확인
3. 실제 납품 또는 매출 인식 시작
4. OPM / EPS revision 확인
5. working capital / cash collection 안정
6. geopolitical / legal / sanction risk 통과
7. dilution / capital allocation risk 통과
8. 가격경로가 evidence 이후 따라옴

금지:
preferred bidder만 있음
MOU만 있음
정책 summit headline만 있음
IPO 첫날 급등만 있음
record high policy rally
러시아·제재 고객 exposure
수주잔고 있지만 취소위험 큼
```

## 4B 조기감지 조건

```text
4B-watch:
preferred bidder 전후 3개월 +40~50% 상승
IPO 첫날 +40~100% 급등
정책/MASGA/MOU 뉴스로 record high
대형 수주 발표일 급등
좋은 수요 뒤 대형 증자 / CB / dilution
U.S. shipbuilding / SMR / AI power 테마가 실제 order보다 먼저 가격화

4B-elevated:
funded order 없음
납품 schedule 불명
margin / working capital 불명
geopolitical customer risk 남음
capital raise announcement after rerating
```

## 4C hard gate 조건

```text
contract cancellation
customer unilateral termination
advance-payment dispute
sanctions / war exposure
arbitration risk
legal injunction blocking contract
geopolitical sanction causing transaction ban
capital raise blocking / regulator revision order
delivery delay
cost overrun
cash collection failure
```

이번 R1 Loop 11에서 hard 4C는 **Samsung Heavy / Zvezda contract cancellation**이다. Hanwha Ocean sanctions는 4C-watch이며, 실제 매출·부품·모듈·계약 차질이 확인되면 hard 4C로 승격한다.

---

# 8. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 9. patch-ready 출력

## docs/round/round_172.md 요약

```md
# R1 Loop 11. Industrial Orders / Infrastructure Price Validation

이번 라운드는 R1 Loop 11 price-validation 라운드다.

핵심 결론:
- Czech nuclear infra is strong Stage 2. Doosan Enerbility +48%, KEPCO E&C +41%, KEPCO Plant S&E +14% in the preferred-bidder period; final KHNP contract was signed at 407B koruna / $18.7B. Listed-company package, margin and cash collection required before Green.
- Doosan SMR / AI power is policy-MOU Stage 2, not Green. X-energy/AWS/Fermi cooperation is meaningful but funded order, equipment package and margin are needed.
- LS Electric / LS Corp grid-cable exposure is Stage 2 but price failed. LS power-cable contract was 282.13B won; LS Electric target was raised to 280,000 won, but shares were -5.4% at 208,500 won.
- HD Hyundai Marine Solution is marine MRO recurring-service candidate, but IPO debut +96.5% is 4B. IPO price 83,400 won, first-day close 163,900 won, earnings +44% in 2023.
- HD Hyundai Heavy / Mipo MASGA merger is Stage 2 + 4B. Shares rose +11.3% / +14.6% to record highs before funded U.S. orders or margin evidence.
- Samsung Heavy Industries is hard 4C. Zvezda icebreaker LNG/shuttle tanker orders worth 4.85T won / $3.54B were cancelled, with arbitration and advance-payment risk.
- Hanwha Aerospace has defense-localization Stage 2 evidence via Poland missile JV, but the 3.6T won capital raise shock and -13% selloff require 4B/dilution watch.
- Hyundai Rotem Morocco rail order is Stage 2. 110 urban trains, 2.2T won / $1.54B, largest railway-business order; delivery and margin required.
- Hanwha Ocean China sanctions are geopolitical 4C-watch. Shares -5.8%; hard 4C requires actual contract/revenue/module disruption.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 172 R1 Loop 11 Industrial Orders Infra Price Validation

## 반영 내용
- R1 Loop 11 price-validation 라운드를 추가했다.
- Nuclear EPC export, SMR/AI power MOU, grid/cable export, marine MRO IPO, MASGA shipbuilding policy, shipbuilding contract cancellation, defense localization dilution, rail export, geopolitical shipbuilding sanctions를 비교했다.
- Reuters/AP/WSJ/MarketWatch reported anchors로 가능한 MFE/MAE 및 contract/event metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- signed contract, confirmed amount, delivery schedule, backlog margin visibility, cash collection, recurring MRO service 가중치 강화
- preferred bidder-only, MOU without funded order, IPO premium, policy shipbuilding headline, geopolitical customer risk, dilution after rerating 감점 강화
- Samsung Heavy contract cancellation hard 4C 추가
```

## case row 초안

```jsonl
{"case_id":"r1_loop11_czech_nuclear_doosan_kepco_stage2","symbol":"034020/052690/051600/015760","company_name":"Doosan Enerbility / KEPCO E&C / KEPCO Plant S&E / KEPCO","case_type":"success_candidate","primary_archetype":"NUCLEAR_EPC_EXPORT_ORDER","stage1_date":"2024-07-17","stage2_date":"2025-06-04","stage4c_date":"2025-05-06_watch","price_validation":{"price_data_source":"Reuters/AP nuclear contract and sector-return anchors","stage3_price":null,"doosan_3m_mfe_pct":48,"kepco_plant_se_3m_mfe_pct":14,"kepco_ec_3m_mfe_pct":41,"czech_contract_value_koruna_bn":407,"czech_contract_value_usd_bn":18.7,"reactor_count":2,"unit_cost_context_koruna_bn":200,"trial_operation_expected":"2036_first_reactor_2038_second_reactor","price_validation_status":"reported_sector_return_not_full_ohlc"},"score_price_alignment":"success_candidate_4b_watch","rerating_result":"nuclear_EPC_export_watch","notes":"Preferred bidder to signed contract is Stage 2; listed-company package, margin and cash collection required before Green."}
{"case_id":"r1_loop11_doosan_smr_ai_power_mou","symbol":"034020","company_name":"Doosan Enerbility / SMR-AI power cooperation","case_type":"success_candidate","primary_archetype":"NUCLEAR_SMR_POLICY_MOU","stage1_date":"2025-08-26","stage2_date":"2025-08-26","price_validation":{"price_data_source":"Reuters U.S. investment / SMR policy-MOU anchor","stage3_price":null,"partners":["X-energy","Amazon Web Services","Fermi America","KHNP","Samsung C&T"],"confirmed_revenue":false,"funded_order_confirmed":false,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"SMR_AI_power_policy_watch","notes":"SMR/AI power MOU is Stage 2 attention, not Green before funded order/equipment package/margin."}
{"case_id":"r1_loop11_ls_grid_cable_transformer_price_failed","symbol":"010120/006260","company_name":"LS Electric / LS Corp","case_type":"success_candidate","primary_archetype":"POWER_GRID_CABLE_TRANSFORMER_EXPORT","stage2_date":"2024-06-20/2024-07-01","price_validation":{"price_data_source":"MarketWatch contract/target/price anchors","stage3_price":null,"ls_power_cable_contract_krw_bn":282.13,"customer":"Elia Asset NV Belgium","ls_electric_stage2_price_anchor_krw":208500,"stage2_event_mae_pct":-5.4,"target_price_krw":280000,"target_raise_pct":86.7,"target_upside_from_stage2_price_pct":34.3,"us_revenue_share_2022_max_pct":5,"us_revenue_share_expected_2024_pct":20,"minimum_mix_increase_pct":300,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"evidence_good_but_price_failed","rerating_result":"grid_cable_transformer_watch","notes":"Contract/U.S. mix evidence is good, but event price failed; delivery, margin and FCF required before Green."}
{"case_id":"r1_loop11_hd_hyundai_marine_solution_ipo_4b","symbol":"443060","company_name":"HD Hyundai Marine Solution","case_type":"success_candidate","primary_archetype":"MARINE_MRO_RECURRING_SERVICE","stage2_date":"2024-05-08","stage4b_date":"2024-05-08","price_validation":{"price_data_source":"Reuters Breakingviews/WSJ IPO anchors","ipo_price_krw":83400,"opening_price_krw":119900,"opening_mfe_pct":43.8,"first_day_close_krw":163900,"first_day_close_mfe_pct":96.5,"ipo_raise_krw_bn":742,"market_cap_close_context_krw_trn":7.29,"earnings_2023_krw_bn":151.1,"earnings_growth_pct":44,"parent_hd_hyundai_stake_pct":55.8,"kkr_vehicle_stake_pct":24.2,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_4b_watch","rerating_result":"marine_MRO_recurring_service_watch","notes":"Marine MRO recurring story is Stage 2; IPO debut +96.5% is 4B until recurring revenue/margin/FCF confirm."}
{"case_id":"r1_loop11_hd_hyundai_heavy_mipo_masga_merger","symbol":"329180/010620","company_name":"HD Hyundai Heavy / HD Hyundai Mipo","case_type":"success_candidate","primary_archetype":"SHIPBUILDING_US_POLICY_MASGA","stage2_date":"2025-08-27","stage4b_date":"2025-08-27","price_validation":{"price_data_source":"Reuters merger/event-return anchor","stage3_price":null,"hd_hyundai_heavy_mfe_1d_pct":11.3,"hd_hyundai_mipo_mfe_1d_pct":14.6,"record_high_status":true,"share_exchange_ratio_mipo_per_heavy":1.04059146,"us_coast_guard_icebreaker_allocation_usd_bn":8.6,"price_validation_status":"reported_event_return_not_full_ohlc"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"U.S._shipbuilding_policy_watch","notes":"MASGA/merger is Stage 2 and 4B-watch; funded U.S. order and margin required before Green."}
{"case_id":"r1_loop11_samsung_heavy_zvezda_contract_cancellation","symbol":"010140","company_name":"Samsung Heavy Industries","case_type":"4c_thesis_break","primary_archetype":"SHIPBUILDING_CONTRACT_CANCELLATION_4C","stage4c_date":"2025-06-18","price_validation":{"price_data_source":"Reuters contract-cancellation anchor","stage3_price":null,"cancelled_contract_value_krw_trn":4.85,"cancelled_contract_value_usd_bn":3.54,"orders":["10 icebreaker LNG carriers","7 icebreaker shuttle tankers"],"contract_origin":"2020-2021","shipowner":"Russia Zvezda","arbitration":"Singapore arbitration requested","price_validation_status":"reported_contract_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"shipbuilding_contract_quality_failure","notes":"Russia/Zvezda contract cancellation is hard 4C; sanctioned-customer backlog should be RedTeam before Green."}
{"case_id":"r1_loop11_hanwha_aerospace_poland_jv_dilution_watch","symbol":"012450","company_name":"Hanwha Aerospace","case_type":"success_candidate","primary_archetype":"DEFENSE_LOCAL_PRODUCTION_DILUTION_WATCH","stage2_date":"2025-04-15","stage4b_date":"2025-03-21","price_validation":{"price_data_source":"Reuters missile-JV/capital-raising anchors","stage3_price":null,"poland_missile_jv_product":"CGR-080 guided missiles for K239 Chunmoo","capital_raise_initial_krw_trn":3.6,"capital_raise_initial_usd_bn":2.46,"capital_raise_event_mae_pct":-13,"revised_rights_offering_krw_trn":2.3,"affiliate_share_issue_krw_trn":1.3,"total_revised_related_raise_krw_trn":3.6,"affiliate_issue_price_krw":758000,"guidance_2025_revenue_krw_trn":30,"guidance_2025_op_krw_trn":3,"op_growth_vs_2024_guidance_pct":73.4,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_aligned_4B_detection","rerating_result":"defense_localization_watch_with_dilution","notes":"Poland missile JV is Stage 2; capital raise after rerating is 4B/dilution watch."}
{"case_id":"r1_loop11_hyundai_rotem_morocco_rail_order","symbol":"064350","company_name":"Hyundai Rotem","case_type":"success_candidate","primary_archetype":"RAIL_EXPORT_ORDER_TO_DELIVERY","stage2_date":"2025-02-26","price_validation":{"price_data_source":"Reuters rail-contract evidence","stage3_price":null,"morocco_total_train_purchase":168,"morocco_total_program_value_usd_bn":2.9,"hyundai_rotem_order_krw_trn":2.2,"hyundai_rotem_order_usd_bn":1.54,"hyundai_train_count":110,"hyundai_order_share_of_total_program_pct":53.1,"alstom_high_speed_trains":18,"caf_intercity_trains":40,"network_target_cities":43,"network_target_population_coverage_pct":87,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"rail_export_order_watch","notes":"Morocco rail order is Stage 2; delivery, margin, working capital and cash collection required before Green."}
{"case_id":"r1_loop11_hanwha_ocean_china_sanction_watch","symbol":"042660","company_name":"Hanwha Ocean","case_type":"4c_watch","primary_archetype":"GEOPOLITICAL_SHIPBUILDING_SANCTION","stage4c_date":"2025-10-14","price_validation":{"price_data_source":"Reuters/AP sanction and price anchors","stage3_price":null,"hanwha_ocean_close_mae_pct":-5.8,"hd_hyundai_heavy_same_context_pct":-4.1,"ft_intraday_context_pct":-8,"sanctioned_entities":5,"philly_shipyard_acquisition_usd_mn":100,"announced_us_investment_usd_bn":5.0,"investment_vs_acquisition_multiple":50,"price_validation_status":"reported_event_return_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"geopolitical_sanction_watch","notes":"China sanctions are 4C-watch; hard 4C requires actual revenue/contract/module disruption."}
```

## shadow weight row 초안

```csv
archetype,signed_contract,contract_amount,order_to_revenue,delivery_schedule,backlog_margin,cash_collection,recurring_service,geopolitical_risk,event_penalty,dilution_redteam,4b_watch_sensitivity,hard_4c_sensitivity,notes
NUCLEAR_EPC_EXPORT_ORDER,+5,+5,+4,+4,+5,+5,+0,+4,-2,+1,+5,+4,Czech signed contract is Stage 2; listed-company package/margin/cashflow required.
NUCLEAR_SMR_POLICY_MOU,+2,+2,+1,+1,+3,+3,+0,+3,-5,+1,+5,+3,SMR/AI MOU is attention only until funded order.
POWER_GRID_CABLE_TRANSFORMER_EXPORT,+5,+5,+4,+4,+5,+4,+0,+2,-2,+1,+4,+3,LS contract and U.S. grid mix are good but event price failed.
MARINE_MRO_RECURRING_SERVICE,+4,+3,+4,+3,+5,+5,+5,+2,-5,+2,+5,+3,HD Hyundai Marine has recurring-service story but IPO premium is 4B.
SHIPBUILDING_US_POLICY_MASGA,+3,+3,+2,+2,+4,+4,+0,+4,-5,+1,+5,+4,MASGA/merger is Stage 2 and 4B until funded U.S. orders/margins confirm.
SHIPBUILDING_CONTRACT_CANCELLATION_4C,+0,+0,+0,+0,+0,+0,+0,+5,0,+1,+3,+5,Samsung Heavy/Zvezda cancellation is hard 4C.
DEFENSE_LOCAL_PRODUCTION_DILUTION_WATCH,+4,+4,+4,+4,+5,+4,+0,+3,-3,+5,+5,+4,Hanwha Aerospace JV is Stage 2 but dilution after rerating is 4B-watch.
RAIL_EXPORT_ORDER_TO_DELIVERY,+5,+5,+4,+5,+5,+5,+0,+3,-2,+1,+3,+4,Hyundai Rotem rail order is Stage 2 until delivery/margin/cash collection confirm.
GEOPOLITICAL_SHIPBUILDING_SANCTION,+0,+0,+0,+0,+0,+0,+0,+5,0,+1,+4,+5,Hanwha Ocean China sanctions require 4C-watch.
```

---

# 이번 R1 Loop 11 결론

R1은 좋은 후보가 많지만, **수주 headline과 Stage 3를 구분하지 않으면 바로 false positive가 쌓이는 섹터**다.

```text
1. Czech nuclear는 preferred bidder에서 signed contract로 올라왔기 때문에 강한 Stage 2다.
   하지만 listed-company package, margin, cash collection 전 Stage 3는 아니다.

2. Doosan SMR / AI power cooperation은 좋은 정책·MOU 후보지만,
   funded order 전 Green 금지다.

3. LS grid/cable은 계약과 U.S. exposure가 좋지만,
   LS Electric 가격반응은 바로 실패했다. evidence_good_but_price_failed다.

4. HD Hyundai Marine Solution은 marine MRO recurring story가 좋지만,
   IPO 첫날 +96.5%는 4B다.

5. HD Hyundai Heavy / Mipo MASGA merger는 Stage 2 + 4B다.
   funded U.S. order와 margin 전에는 Green이 아니다.

6. Samsung Heavy / Zvezda cancellation은 hard 4C다.
   Russia/sanctioned customer backlog는 contract quality RedTeam으로 강하게 깎아야 한다.

7. Hanwha Aerospace는 Poland missile JV로 Stage 2지만,
   대형 증자 shock 때문에 dilution 4B-watch가 필수다.

8. Hyundai Rotem Morocco rail은 강한 rail export Stage 2다.
   납품·마진·working capital 전 Stage 3는 보류다.

9. Hanwha Ocean은 U.S. shipbuilding exposure가 좋아도 China sanctions 4C-watch가 붙는다.
```

한 문장으로 압축하면:

> **R1에서 진짜 Stage 3는 “수주·정책·MOU·IPO·합병이 있다”가 아니라, 그 이벤트가 납품·매출·마진·EPS revision·현금회수로 닫히고, 법적·지정학·dilution·계약취소 risk를 통과하는 순간이다.**

[1]: https://www.reuters.com/business/energy/south-koreas-winning-bid-czech-nuclear-power-project-2024-07-17/?utm_source=chatgpt.com "South Korea's winning bid for Czech nuclear power project"
[2]: https://www.reuters.com/business/aerospace-defense/south-korean-firms-pledge-150-billion-us-investments-summit-2025-08-26/?utm_source=chatgpt.com "South Korean firms pledge $150 billion in US investments at summit"
[3]: https://www.marketwatch.com/story/ls-secures-krw282-13b-contract-to-supply-electrical-power-cables-to-elia-asset-nv-of-belgium-16d5ba28?utm_source=chatgpt.com "LS Secures KRW282.13B Contract to Supply Electrical Power Cables to Elia Asset NV of Belgium"
[4]: https://www.reuters.com/breakingviews/ship-ipo-puts-wind-back-korea-incs-sails-2024-05-08/?utm_source=chatgpt.com "Ship IPO puts wind back in Korea Inc's sails"
[5]: https://www.reuters.com/markets/emerging/south-korean-shipbuilder-hd-hyundai-heavy-merge-with-affiliate-hd-hyundai-mipo-2025-08-27/?utm_source=chatgpt.com "South Korean shipbuilder HD Hyundai Heavy to merge with affiliate HD Hyundai Mipo"
[6]: https://www.reuters.com/business/retail-consumer/samsung-heavy-says-354-billion-icebreaker-orders-russias-zvezda-cancelled-2025-06-18/?utm_source=chatgpt.com "Samsung Heavy says $3.54 billion icebreaker orders from Russia's Zvezda cancelled"
[7]: https://www.reuters.com/business/aerospace-defense/south-koreas-hanwha-aerospace-produce-missiles-poland-2025-04-15/?utm_source=chatgpt.com "South Korea's Hanwha Aerospace to produce missiles in Poland"
[8]: https://www.reuters.com/business/autos-transportation/morocco-buy-168-trains-france-spain-south-korea-29-bln-2025-02-26/?utm_source=chatgpt.com "Morocco to buy 168 trains from France, Spain and South Korea for $2.9 bln"
[9]: https://www.reuters.com/world/asia-pacific/china-takes-steps-against-us-linked-units-skorea-shipbuilder-hanwha-2025-10-14/?utm_source=chatgpt.com "China takes steps against US-linked units of S.Korea shipbuilder Hanwha"

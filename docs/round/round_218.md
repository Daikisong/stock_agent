순서상 이번은 **R1 Loop 9 — 산업재·수주·인프라 가격경로 검증 라운드**다.

이번 라운드는 방산만 반복하지 않고, **전력기기·변압기·해외 EPC·원전 기자재·조선/MRO·지정학 제재**를 섞어서 봤다. 원시 수정주가 일봉 OHLC를 안정적으로 직접 추출하지 못한 항목은 숫자를 만들지 않았고, Reuters / WSJ / MarketWatch / AP에 남은 **가격 anchor, 이벤트 수익률, 계약금액, 목표가, 정책·산업 지표**로 계산 가능한 값만 계산했다.

```text
round = R1 Loop 9
round_id = round_146
large_sector = INDUSTRIAL_ORDERS_INFRA
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
```

---

# 1. 이번 라운드 대섹터

```text
R1 = 산업재·수주·인프라
```

R1의 핵심은 “수주가 있다”가 아니라, **계약금액·납기·수주잔고·고객·마진·EPS revision·현금흐름이 같이 확인되는가**다. 이번 라운드에서는 특히 AI 데이터센터 전력수요와 미국 송배전 병목이 한국 전력기기 업체에 어떻게 Stage 2 후보를 만드는지, 그리고 조선·원전·EPC 이벤트가 어디서 4B-watch로 바뀌는지를 봤다.

---

# 2. 대상 canonical archetype

```text
GRID_POWER_EQUIPMENT_AI_DATACENTER
TRANSFORMER_CAPACITY_BOTTLENECK
POWER_EQUIPMENT_EXPORT_US_GRID
OVERSEAS_EPC_CONTRACT_BACKLOG
NUCLEAR_POLICY_TO_EQUIPMENT_BACKLOG
SHIPBUILDING_US_POLICY_MASGA
SHIP_MRO_RECURRING_PLATFORM
GEOPOLITICAL_SHIPBUILDING_SANCTION
IPO_EVENT_PREMIUM
CONTRACT_HEADLINE_NOT_STAGE3
PRICE_ONLY_RALLY
THESIS_BREAK_4C_WATCH
```

---

# 3. deep sub-archetype

```text
전력기기 / 변압기:
- LS Electric
- HD Hyundai Electric
- Hyosung Heavy Industries
- U.S. transformer shortage
- AI data center grid demand
- renewable / EV grid buildout
- capacity bottleneck
- U.S. revenue mix
- price increase / lead-time expansion

해외 EPC:
- Samsung E&A
- Saudi Aramco Fadhili gas expansion
- contract size vs annual wins
- EPC margin / cost overrun / cash collection

원전 기자재:
- Doosan Enerbility
- Czech nuclear preferred bidder
- final contract vs equipment backlog
- court delay / legal 4C-watch
- SMR policy/MOU vs funded order

조선 / MRO:
- HD Hyundai Heavy / HD Hyundai Mipo
- MASGA / U.S. shipbuilding rebuild
- HD Hyundai Marine Solution
- IPO premium vs recurring MRO platform
- funded order vs policy premium

지정학 RedTeam:
- Hanwha Ocean
- China sanctions against U.S.-linked subsidiaries
- U.S.-China maritime conflict
- China module supply exposure
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
- Daiwa가 LS Electric 목표가를 150,000원 → 280,000원으로 상향
- U.S. revenue share가 2022년 5% 미만에서 2024년 약 20%로 상승 가능하다고 전망
- 하지만 당일 주가는 5.4% 하락해 208,500원

Stage 3:
보류
- U.S. 매출비중과 수요 전망은 강하지만, event 당일 가격은 실패
- 실제 수주잔고, 마진, EPS revision, FCF 확인 필요

Stage 4B:
AI/data-center 전력기기 theme으로 multiple이 먼저 확장된 구간이면 후보

Stage 4C:
미국 프로젝트 지연, transformer cycle peak-out, 원가 상승, margin miss 시 후보
```

Daiwa는 LS Electric의 미국 매출 비중이 2022년 5% 미만에서 2024년 약 20%로 올라갈 수 있다고 봤고, 데이터센터·재생에너지·EV value chain 수요를 근거로 2024~2026년 매출 전망을 4~22% 상향했다. 목표가는 150,000원에서 280,000원으로 87% 올렸지만, 보도 시점 주가는 오히려 5.4% 하락해 208,500원이었다. 이건 **evidence는 좋지만 가격경로가 즉시 실패한 Stage 2 후보**다. ([마켓워치][1])

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch reported price / target anchor

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

MFE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D / 1Y:
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
score_price_alignment = evidence_good_but_price_failed
rerating_result = U.S._grid_power_equipment_watch
stage_failure_type = stage2_watch_not_green
```

---

## Case B — HD현대일렉트릭 / 효성중공업 `success_candidate / transformer bottleneck watch`

```text
symbols = 267260 / 298040
case_type = success_candidate / insufficient_price_data
archetype = TRANSFORMER_CAPACITY_BOTTLENECK / GRID_POWER_EQUIPMENT_AI_DATACENTER
```

### stage date

```text
Stage 1:
2024~2026
- AI data center / EV / renewable grid demand
- U.S. transformer shortage
- South Korea transformer import demand

Stage 2:
2026-05-11
- Reuters가 U.S. transformer shortage를 구조적으로 보도
- GSU transformer demand +274%, substation transformer demand +116% since 2019
- transformer prices +80% in five years
- large-unit lead time up to four years
- U.S. buyers turning to imports including South Korea

Stage 3:
보류
- 산업 수요는 강하지만 회사별 confirmed order, backlog, margin, capacity expansion, FCF 확인 필요

Stage 4B:
K-transformer theme이 수주·마진보다 먼저 multiple로 확장되면 후보

Stage 4C:
U.S. supply expansion, order delay, price normalization, capacity overbuild, margin pressure 시 후보
```

Reuters는 미국 전력망 증설과 AI 데이터센터·EV·재생에너지 수요 때문에 전력 변압기 shortage가 심해졌고, 2019년 이후 generator step-up transformer 수요가 274%, substation transformer 수요가 116% 늘었다고 보도했다. 대형 변압기 가격은 5년간 약 80% 올랐고 lead time은 최대 4년까지 길어졌으며, 미국 구매자들이 한국 등 해외 수입에 의존하고 있다. 이건 R1 전력기기의 강한 Stage 2 산업 evidence다. ([Reuters][2])

효성중공업은 공개 기업정보 기준 2024년 매출 4.3조 원, 영업이익 2,578억 원을 기록했고, 전력 송배전·변압기·건설·신재생 관련 사업을 영위한다. 다만 이 출처는 company profile 성격이라 가격검증 confidence는 낮게 둔다. ([위키백과][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters sector evidence + public company profiles

stage3_price:
N/A

company_stock_OHLC:
price_data_unavailable_after_deep_search
- Reuters는 HD현대일렉트릭/효성중공업 개별 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC를 이번 세션에서 안정적으로 확보하지 못함.

GSU_transformer_demand_growth_since_2019:
+274%

substation_transformer_demand_growth_since_2019:
+116%

transformer_price_increase_5Y:
+80%

large_transformer_lead_time:
up to 4 years

Hyosung_Heavy_2024_revenue:
4.3T won

Hyosung_Heavy_2024_operating_income:
257.8B won

Hyosung_Heavy_OP_margin:
257.8 / 4,300
= 6.0%

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = success_candidate / unknown_insufficient_evidence
rerating_result = transformer_bottleneck_watch
stage_failure_type = sector_stage2_not_company_green
```

---

## Case C — 삼성E&A `success_candidate / overseas EPC backlog`

```text
symbol = 028050
case_type = success_candidate
archetype = OVERSEAS_EPC_CONTRACT_BACKLOG / EPC_LOW_MARGIN_ORDER_OVERLAY
```

### stage date

```text
Stage 1:
2024-04-02
- Saudi Aramco Fadhili gas expansion
- Middle East EPC capex cycle

Stage 2:
2024-04-03
- Samsung E&A 약 $6B Fadhili contract
- 주가 장중 +8.5%, 26,750원
- KOSPI -1.4% 대비 강한 아웃퍼폼

Stage 3:
보류
- 대형 EPC 수주는 강한 Stage 2
- Stage 3는 margin, progress revenue, cost control, working capital 확인 뒤

Stage 4B:
2024-04-03
- 수주 발표 당일 event rally

Stage 4C:
저마진 수주, cost overrun, 발주처 지급 지연, working-capital 악화 시 후보
```

Samsung E&A는 Saudi Aramco Fadhili gas plant 확장 프로젝트에서 약 60억 달러 계약을 따냈고, 주가는 장중 8.5% 상승해 26,750원까지 올랐다. 같은 시점 KOSPI는 1.4% 하락했고, KB증권 목표가는 35,000원이었다. 이건 수주 headline으로는 강하지만, R1 Green은 **마진과 현금흐름 확인 뒤**다. ([월스트리트저널][4])

### 실제 가격경로 검증

```text
price_data_source:
WSJ / Reuters reported price and contract anchors

entry_date:
2024-04-03

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

relative_outperformance_vs_KOSPI:
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

MAE_30D / 90D / 180D:
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

---

## Case D — 두산에너빌리티 `success_candidate / nuclear policy-to-contract watch`

```text
symbol = 034020
case_type = success_candidate + 4B-watch
archetype = NUCLEAR_POLICY_TO_EQUIPMENT_BACKLOG
```

### stage date

```text
Stage 1:
2024-07-17
- KHNP selected as preferred bidder for Czech nuclear project
- Korean nuclear export revival

Stage 2:
2025-06-04
- Czech deal signed after court clearance
- 407B koruna / $18.7B contract
- 2 reactors

Stage 3:
보류
- 두산에너빌리티의 실제 장비 수주잔고, 마진, 납기, EPS revision 확인 필요

Stage 4B:
2024-07-17 전후
- 두산에너빌리티 주가 3개월 +48%
- preferred bidder 단계에서 가격이 선반영

Stage 4C-watch:
2025-05-06
- Czech court temporarily blocks signing
- legal delay / final-contract risk

4C relief:
2025-06-04
- deal signed after court clearance
```

2024년 7월 체코 정부가 KHNP를 신규 원전 2기 우선협상대상자로 선정했을 때, 두산에너빌리티 주가는 최근 3개월간 48% 상승한 상태였다. 당시 최종 계약금액은 아직 협상 전이었다. 2025년 5월에는 EDF의 법적 이의로 계약 서명이 일시적으로 막혔지만, 2025년 6월 체코 정부는 KHNP와 407B koruna, 약 187억 달러 규모 계약을 체결했다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / AP reported return and contract anchors

stage3_price:
N/A

reported_MFE_3M:
+48%

signed_contract_value:
407B koruna / $18.7B

reactor_count:
2

contract_value_per_reactor:
407B / 2
= 203.5B koruna

earlier_cost_estimate_per_unit:
200B koruna

signed_contract_per_reactor_vs_estimate:
203.5 / 200 - 1
= +1.75%

MFE_30D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

Stage 4B peak-before 여부:
partial_success
- preferred-bidder 단계에서 이미 +48%라면 4B-watch 필요.
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = nuclear_policy_to_contract_watch
stage_failure_type = stage2_watch_success
```

---

## Case E — HD현대중공업 / HD현대미포 `event_premium + success_candidate`

```text
symbols = 329180 / 010620
case_type = success_candidate + 4B-watch
archetype = SHIPBUILDING_US_POLICY_MASGA / SHIPBUILDING_OFFSHORE_BACKLOG
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

HD현대중공업은 HD현대미포와 합병해 미국 조선시장 진출을 확대하겠다고 발표했고, 이는 한미 정상회담 이후의 MASGA 협력과 연결됐다. 발표 전후 HD현대중공업은 11.3%, HD현대미포는 14.6% 상승해 record high로 마감했다. 이는 Stage 2 후보이면서 동시에 **4B-watch**다. ([Reuters][6])

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

below_stage3_price_flag:
N/A

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

## Case F — 한화오션 `4C-watch / geopolitical sanction`

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
- intraday over -8% per AP
- HD Hyundai Heavy also -4.1%
```

중국은 한화오션의 미국 관련 자회사 5곳을 제재했고, 중국 내 기업·개인이 이들과 거래·협력하는 것을 금지했다. Reuters는 한화오션 주가가 5.8% 하락했고, HD현대중공업도 4.1% 내렸다고 보도했다. AP는 장중 8% 넘게 하락했고, 한화오션이 2024년 Philly Shipyard를 1억 달러에 인수했으며 2025년에는 미국 조선 인프라에 50억 달러 투자 계획을 발표했다고 정리했다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / AP reported event return anchors

stage3_price:
N/A

Hanwha_Ocean_event_MAE_close:
-5.8%

Hanwha_Ocean_intraday_MAE:
over -8%

HD_Hyundai_Heavy_event_MAE:
-4.1%

Philly_Shipyard_acquisition:
$100M

announced_U.S._investment:
$5B

investment_vs_acquisition_price:
5.0B / 0.1B
= 50x

sanctioned_entities:
5 U.S.-linked subsidiaries

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4C 큰 하락 이전 포착 여부:
partial_success
- sanction 당일 4C-watch 가능.
- hard 4C는 실제 매출/계약 차질 확인 필요.
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = geopolitical_sanction_watch
stage_failure_type = 4C_watch_not_hard_4C
```

---

## Case G — HD현대마린솔루션 `overheat / IPO event premium`

```text
symbol = 443060
case_type = overheat / price_moved_without_evidence
archetype = SHIP_MRO_RECURRING_PLATFORM / IPO_EVENT_PREMIUM
```

### stage date

```text
Stage 1:
2024-04~05
- ship MRO / after-sales / retrofit platform IPO
- eco-friendly vessel servicing demand

Stage 2:
2024-05-08
- IPO listing
- 2023 revenue +7.2%
- operating/net profit increased

Stage 3:
없음
- 좋은 MRO 구조일 수 있지만 IPO 첫날 급등은 Stage 3 아님
- recurring MRO revenue, margin, FCF, order visibility 확인 필요

Stage 4B:
2024-05-08
- IPO price 83,400원 → first-day close 163,900원
- +96.5%

Stage 4C:
post-IPO multiple compression, KKR stake sell-down, MRO margin miss 시 후보
```

HD현대마린솔루션은 2024년 5월 IPO 첫날 공모가 83,400원 대비 163,900원으로 마감해 97% 상승했다. WSJ는 이 상장으로 시가총액이 약 7.29조 원, 53.6억 달러가 됐고, 2023년 매출은 1.43조 원으로 7.2% 증가했다고 보도했다. Reuters Breakingviews는 2023년 earnings가 44% 증가해 1,511억 원이었다고 정리했다. 이는 사업모델은 좋을 수 있지만 **가격경로는 IPO event premium**이다. ([월스트리트저널][8])

### 실제 가격경로 검증

```text
price_data_source:
WSJ / Reuters Breakingviews reported IPO anchors

IPO_price:
83,400원

first_day_close:
163,900원

event_MFE_1D:
(163,900 / 83,400) - 1
= +96.5%

IPO_market_cap:
$2.70B

first_day_market_cap:
$5.36B

market_cap_MFE_1D:
(5.36 / 2.70) - 1
= +98.5%

IPO_proceeds:
742.26B won / about $546M

shares_outstanding:
44.5M

2023_revenue:
1.43T won

2023_revenue_growth:
+7.2%

2023_earnings:
151.1B won

2023_earnings_growth:
+44%

stage3_price:
N/A

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
success
- 상장 첫날 +96.5%는 바로 4B/event premium.
```

### alignment

```text
score_price_alignment = price_moved_without_evidence
rerating_result = IPO_event_premium
stage_failure_type = should_have_been_4B_watch_not_green
```

---

# 5. 이번 R1 case별 요약표

| case           | 분류                               |                                                    실제 가격검증 | alignment                      |
| -------------- | -------------------------------- | ---------------------------------------------------------: | ------------------------------ |
| LS Electric    | success_candidate / price failed |                      208,500원, -5.4%; target upside +34.3% | evidence_good_but_price_failed |
| HD현대일렉트릭/효성중공업 | success_candidate                | transformer demand +274% / +116%, price +80%, lead time 4년 | sector Stage 2                 |
| 삼성E&A          | success_candidate                |                            26,750원, +8.5%; KOSPI 대비 +9.9pp | stage2_watch_success           |
| 두산에너빌리티        | success_candidate + 4B           |                       3개월 +48%, Czech contract 407B koruna | policy_to_contract_watch       |
| HD현대중공업/미포     | event + success_candidate        |                              +11.3% / +14.6%, record highs | event_premium_watch            |
| 한화오션           | 4C-watch                         |                  close -5.8%, intraday >-8%, HD현대중공업 -4.1% | geopolitical_sanction_watch    |
| HD현대마린솔루션      | overheat                         |                                 IPO 83,400→163,900, +96.5% | price_moved_without_evidence   |

---

# 6. score-price alignment 판정

```text
success_candidate:
- LS Electric
- HD현대일렉트릭 / 효성중공업 transformer basket
- 삼성E&A
- 두산에너빌리티
- HD현대중공업 / HD현대미포

evidence_good_but_price_failed:
- LS Electric

event_premium:
- HD현대중공업 / HD현대미포 MASGA/merger event
- HD현대마린솔루션 IPO

price_moved_without_evidence:
- HD현대마린솔루션 IPO first-day rally

thesis_break_watch:
- 한화오션 China sanction

4B-watch:
- HD현대마린솔루션 +96.5%
- HD현대중공업/미포 record highs
- 두산에너빌리티 preferred-bidder 기대 +48%
- 전력기기 transformer theme이 company-level order보다 먼저 valuation화되는 구간

4C-watch:
- 한화오션 sanctions
- EPC cost overrun / margin miss
- transformer cycle peak-out
- nuclear contract legal delay
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
power_equipment_export_mix +4
price_path_alignment +5
```

### 왜 올리나

삼성E&A는 계약금액과 가격반응이 명확했고, LS Electric은 미국 매출 mix 개선 가능성과 target upside가 확인됐다. 전력기기 basket은 미국 transformer shortage라는 산업 병목이 구조적으로 강하다. 다만 이들은 모두 **company-level margin/FCF 확인 전 Stage 2**다.

## 내릴 축

```text
contract_headline_without_margin -5
policy_or_MOU_without_order -5
IPO_first_day_rally -5
record_high_on_policy_event -4
unconfirmed_US_shipbuilding_policy_premium -4
geopolitical_sanction_unpriced -4
equipment_cycle_without_margin -3
EPC_backlog_without_cashflow -4
```

### 왜 내리나

HD현대마린솔루션은 좋은 MRO 구조일 수 있지만 IPO 첫날 +96.5%는 Stage 3가 아니라 event premium이다. HD현대중공업/미포는 record high를 찍었지만 funded U.S. order와 margin 전에는 Green이 아니다. 한화오션은 미국 조선정책 exposure가 좋아도 중국 제재가 4C-watch로 붙는다.

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
IPO 첫날 급등
record high event rally
마진 불명
EPC cash collection 불명
geopolitical sanction risk 무시
```

## 4B 조기감지 조건

```text
4B-watch:
IPO 첫날 50~100% 급등
정책/합병/MOU 이벤트로 record high
preferred bidder 단계에서 이미 +40~50% 상승
전력기기 theme이 company-level order보다 먼저 multiple화
대형 수주 발표일 급등
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
IPO lock-up / PE sell-down pressure
equipment order cycle peak-out
```

이번 라운드에서 한화오션은 hard 4C가 아니라 **4C-watch**다. 실제 매출·수주·중국 모듈 공급 차질이 확인되면 hard 4C로 승격한다.

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

## docs/round/round_146.md 요약

```md
# R1 Loop 9. Industrial Orders / Infrastructure Price Validation

이번 라운드는 R1 Loop 9 price-validation 라운드다.

핵심 결론:
- LS Electric은 미국 전력기기 growth story가 강하지만, 보도 시점 주가는 -5.4%였다. Evidence good but price failed로 분류한다.
- HD현대일렉트릭/효성중공업 transformer basket은 미국 transformer shortage로 Stage 2 sector evidence가 강하다. 하지만 회사별 order/margin/FCF 전 Stage 3는 보류한다.
- 삼성E&A는 Fadhili $6B contract로 Stage 2 후보이며, 주가는 26,750원, +8.5%, KOSPI 대비 +9.9pp 아웃퍼폼했다. Stage 3는 margin/cash collection 확인 후다.
- 두산에너빌리티는 Czech nuclear preferred bidder 기대에 3개월 +48%였고, 이후 407B koruna contract로 policy-to-contract path가 일부 검증됐다. 장비 backlog/margin 전 Green은 아니다.
- HD현대중공업/미포는 MASGA·U.S. shipbuilding policy와 합병 이벤트로 +11.3% / +14.6% record high를 기록했다. funded order 전 Stage 3 금지다.
- 한화오션은 China sanctions로 -5.8% 하락해 geopolitical 4C-watch다.
- HD현대마린솔루션은 IPO 첫날 83,400원에서 163,900원으로 +96.5% 상승했다. 좋은 MRO 구조일 수 있지만 IPO first-day rally는 Stage 3가 아니라 4B/event premium이다.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 146 R1 Loop 9 Industrial Infra Price Validation

## 반영 내용
- R1 Loop 9 price-validation 라운드를 추가했다.
- Power-equipment/grid, transformer bottleneck, overseas EPC, nuclear equipment, U.S. shipbuilding policy, ship MRO IPO, geopolitical sanction을 비교했다.
- Reuters/WSJ/MarketWatch/AP reported anchors로 가능한 MFE/MAE 및 contract/event metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- confirmed contract amount, order-to-revenue conversion, backlog margin visibility, U.S. grid exposure 가중치 강화
- IPO first-day rally, policy/MOU without order, contract headline without margin 감점 강화
- geopolitical sanction 4C-watch와 transformer-cycle 4B-watch 추가
```

## case row 초안

```jsonl
{"case_id":"r1_loop9_ls_electric_us_grid_watch","symbol":"010120","company_name":"LS ELECTRIC","case_type":"success_candidate","primary_archetype":"POWER_EQUIPMENT_EXPORT_US_GRID","stage2_date":"2024-07-01","price_validation":{"price_data_source":"MarketWatch reported price/target anchor","stage3_price":null,"stage2_price_anchor":208500,"stage2_event_mae_1d_pct":-5.4,"target_price":280000,"target_upside_pct":34.3,"target_raise_pct":86.7,"us_revenue_share_2024_expected_pct":20,"us_revenue_share_2022_max_pct":5,"minimum_relative_mix_increase_pct":300,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"evidence_good_but_price_failed","rerating_result":"U.S._grid_power_equipment_watch","notes":"Good U.S. grid/data-center growth evidence, but event price action failed; Stage 3 requires orders/margin/FCF."}
{"case_id":"r1_loop9_k_transformer_bottleneck_basket","symbol":"267260/298040","company_name":"HD현대일렉트릭/효성중공업","case_type":"success_candidate","primary_archetype":"TRANSFORMER_CAPACITY_BOTTLENECK","stage2_date":"2026-05-11","price_validation":{"price_data_source":"Reuters sector evidence + public company profiles","stage3_price":null,"gsu_transformer_demand_growth_pct":274,"substation_transformer_demand_growth_pct":116,"transformer_price_increase_5y_pct":80,"large_transformer_lead_time_years":4,"hyosung_revenue_2024_krw_trn":4.3,"hyosung_op_income_2024_krw_bn":257.8,"hyosung_op_margin_pct":6.0,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"transformer_bottleneck_watch","notes":"Strong sector bottleneck, but company-level order/margin/FCF and OHLC unavailable."}
{"case_id":"r1_loop9_samsung_ea_fadhili_epc","symbol":"028050","company_name":"삼성E&A","case_type":"success_candidate","primary_archetype":"OVERSEAS_EPC_CONTRACT_BACKLOG","stage2_date":"2024-04-03","stage4b_date":"2024-04-03","price_validation":{"price_data_source":"WSJ/Reuters reported anchors","stage3_price":null,"stage2_event_peak_price":26750,"stage2_event_mfe_1d_pct":8.5,"implied_pre_event_reference_price":24654,"kospi_same_context_return_pct":-1.4,"relative_outperformance_pp":9.9,"contract_value_usd_bn":6.0,"aramco_total_project_usd_bn":7.7,"samsung_share_of_project_pct":77.9,"kb_target_price":35000,"target_upside_from_event_peak_pct":30.8,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate","rerating_result":"EPC_backlog_watch","notes":"Large EPC contract is Stage 2; Stage 3 requires margin, progress revenue and cash collection."}
{"case_id":"r1_loop9_doosan_czech_nuclear_policy_to_contract","symbol":"034020","company_name":"두산에너빌리티","case_type":"success_candidate","primary_archetype":"NUCLEAR_POLICY_TO_EQUIPMENT_BACKLOG","stage1_date":"2024-07-17","stage2_date":"2025-06-04","stage4b_date":"2024-07-17","stage4c_date":"2025-05-06","price_validation":{"price_data_source":"Reuters/AP reported anchors","stage3_price":null,"reported_mfe_3m_pct":48,"signed_contract_value_koruna_bn":407,"signed_contract_value_usd_bn":18.7,"reactor_count":2,"contract_value_per_reactor_koruna_bn":203.5,"signed_contract_per_reactor_vs_estimate_pct":1.75,"price_validation_status":"reported_return_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate","rerating_result":"nuclear_policy_to_contract_watch","notes":"Preferred bidder to final contract is Stage 2; Doosan equipment backlog/margin required for Green."}
{"case_id":"r1_loop9_hd_hyundai_heavy_mipo_masga_event","symbol":"329180/010620","company_name":"HD현대중공업/HD현대미포","case_type":"success_candidate","primary_archetype":"SHIPBUILDING_US_POLICY_MASGA","stage2_date":"2025-08-27","stage4b_date":"2025-08-27","price_validation":{"price_data_source":"Reuters reported event return anchor","stage3_price":null,"hd_hyundai_heavy_mfe_1d_pct":11.3,"hd_hyundai_mipo_mfe_1d_pct":14.6,"record_high_status":true,"share_exchange_ratio_mipo_per_heavy":1.04059146,"price_validation_status":"reported_event_return_not_full_ohlc"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"U.S._shipbuilding_policy_watch","notes":"Merger/MASGA is Stage 2 and 4B-watch; funded order and margin required for Stage 3."}
{"case_id":"r1_loop9_hanwha_ocean_china_sanction_watch","symbol":"042660","company_name":"한화오션","case_type":"4c_watch","primary_archetype":"GEOPOLITICAL_SHIPBUILDING_SANCTION","stage4c_date":"2025-10-14","price_validation":{"price_data_source":"Reuters/AP reported event anchors","stage3_price":null,"hanwha_ocean_close_mae_pct":-5.8,"hanwha_ocean_intraday_mae_pct":-8.0,"hd_hyundai_heavy_mae_pct":-4.1,"philly_shipyard_acquisition_usd_mn":100,"announced_us_investment_usd_bn":5.0,"investment_vs_acquisition_multiple":50,"sanctioned_entities":5,"price_validation_status":"reported_event_return_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"geopolitical_sanction_watch","notes":"China sanctions are 4C-watch; hard 4C requires actual revenue/contract disruption."}
{"case_id":"r1_loop9_hd_hyundai_marine_solution_ipo_premium","symbol":"443060","company_name":"HD현대마린솔루션","case_type":"overheat","primary_archetype":"SHIP_MRO_RECURRING_PLATFORM","stage2_date":"2024-05-08","stage4b_date":"2024-05-08","price_validation":{"price_data_source":"WSJ/Reuters Breakingviews IPO anchors","stage3_price":null,"ipo_price":83400,"first_day_close":163900,"mfe_1d_pct":96.5,"ipo_market_cap_usd_bn":2.70,"first_day_market_cap_usd_bn":5.36,"market_cap_mfe_1d_pct":98.5,"ipo_proceeds_krw_bn":742.26,"shares_outstanding_mn":44.5,"revenue_2023_krw_trn":1.43,"revenue_growth_2023_pct":7.2,"earnings_2023_krw_bn":151.1,"earnings_growth_2023_pct":44,"price_validation_status":"reported_price_anchor_not_stage3"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"IPO_event_premium","notes":"Ship MRO platform may be attractive, but first-day +96.5% is 4B/event premium, not Stage 3."}
```

## shadow weight row 초안

```csv
archetype,contract_amount,order_to_revenue,delivery_schedule,backlog_margin,customer_quality,capacity_bottleneck,us_grid_exposure,price_path_alignment,event_penalty,geopolitical_redteam,4b_watch_sensitivity,hard_4c_sensitivity,notes
POWER_EQUIPMENT_EXPORT_US_GRID,+3,+4,+3,+5,+4,+4,+5,+3,-2,+1,+4,+3,LS Electric has strong U.S. grid evidence but event price failed.
TRANSFORMER_CAPACITY_BOTTLENECK,+3,+3,+4,+5,+4,+5,+5,+2,-2,+1,+5,+3,K-transformer basket has structural bottleneck but needs company orders/margins.
OVERSEAS_EPC_CONTRACT_BACKLOG,+5,+4,+4,+5,+5,+0,+0,+4,-3,+2,+4,+4,Samsung E&A confirms Stage 2 contract; Stage 3 requires margins and cash collection.
NUCLEAR_POLICY_TO_EQUIPMENT_BACKLOG,+4,+4,+5,+5,+5,+2,+0,+4,-4,+2,+5,+4,Doosan preferred bidder/final contract is Stage 2; equipment backlog needed.
SHIPBUILDING_US_POLICY_MASGA,+4,+3,+4,+5,+4,+2,+0,+3,-5,+3,+5,+4,HD Hyundai/Mipo merger is Stage 2 and 4B-watch until funded orders/margins confirm.
GEOPOLITICAL_SHIPBUILDING_SANCTION,+0,+0,+0,+0,+0,+0,+0,+2,0,+5,+3,+5,Hanwha Ocean China sanctions require 4C-watch.
SHIP_MRO_RECURRING_PLATFORM,+3,+3,+3,+4,+3,+0,+0,+1,-5,+1,+5,+3,HD Hyundai Marine IPO rally is 4B/event premium; recurring MRO needs post-IPO revenue/margin/FCF.
IPO_EVENT_PREMIUM,+0,+0,+0,+0,+0,+0,+0,+0,-5,+0,+5,+2,First-day IPO rally should block Stage 3 until operating evidence appears.
```

---

# 이번 R1 Loop 9 결론

R1은 Stage 3가 실제로 대형 수익률을 만들 수 있는 섹터지만, 이번 라운드는 특히 **전력기기·조선·원전·EPC에서 Stage 2와 4B가 겹치는 구조**가 많았다.

```text
1. LS Electric은 미국 grid/data-center 성장 근거가 좋지만,
   보도 시점 주가가 -5.4%였으므로 evidence_good_but_price_failed다.

2. HD현대일렉트릭/효성중공업 transformer basket은 구조적으로 강한 Stage 2 후보지만,
   회사별 주문·마진·FCF·가격경로가 필요하다.

3. 삼성E&A는 대형 EPC 수주가 주가를 밀었지만,
   Stage 3는 EPC margin과 cash collection 확인 뒤다.

4. 두산에너빌리티는 policy-to-contract 경로가 일부 검증됐지만,
   장비 수주잔고·마진·EPS revision 전 Stage 3가 아니다.

5. HD현대중공업/미포는 MASGA·합병 이벤트로 record high를 찍었으므로,
   funded order 전에는 Stage 2 + 4B-watch다.

6. 한화오션은 미국 조선정책 exposure가 좋더라도 중국 제재라는 4C-watch가 붙는다.

7. HD현대마린솔루션은 좋은 MRO 플랫폼일 수 있지만,
   IPO 첫날 +96.5%는 Stage 3가 아니라 4B/event premium이다.
```

한 문장으로 압축하면:

> **R1에서 진짜 Stage 3는 “수주·전력기기·조선정책이 좋다”가 아니라, 계약이 납품·매출·마진·EPS revision·현금흐름으로 내려오고 가격경로가 그 뒤를 따라오는 순간이다.**
> **이번 R1 Loop 9는 transformer bottleneck과 조선정책 같은 좋은 Stage 2 후보를 인정하되, IPO premium·정책 record high·지정학 제재를 4B/4C로 분리하는 라운드다.**

[1]: https://www.marketwatch.com/story/ls-electric-could-gain-from-solid-u-s-business-growth-opportunity-market-talk-3e926067?utm_source=chatgpt.com "LS Electric Could Gain From Solid U.S. Business Growth Opportunity -- Market Talk"
[2]: https://www.reuters.com/business/energy/us-power-transformer-buyers-scramble-imports-factory-slots--reeii-2026-05-11/?utm_source=chatgpt.com "US power transformer buyers scramble for imports, factory slots"
[3]: https://en.wikipedia.org/wiki/Hyosung_Heavy_Industries?utm_source=chatgpt.com "Hyosung Heavy Industries"
[4]: https://www.wsj.com/articles/samsung-e-a-shares-rise-on-6-billion-saudi-contract-win-10a5b2f4?utm_source=chatgpt.com "Samsung E&A Shares Rise on $6 Billion Saudi Contract Win"
[5]: https://www.reuters.com/business/energy/south-koreas-winning-bid-czech-nuclear-power-project-2024-07-17/?utm_source=chatgpt.com "South Korea's winning bid for Czech nuclear power project"
[6]: https://www.reuters.com/markets/emerging/south-korean-shipbuilder-hd-hyundai-heavy-merge-with-affiliate-hd-hyundai-mipo-2025-08-27/?utm_source=chatgpt.com "South Korean shipbuilder HD Hyundai Heavy to merge with affiliate HD Hyundai Mipo"
[7]: https://www.reuters.com/world/asia-pacific/china-takes-steps-against-us-linked-units-skorea-shipbuilder-hanwha-2025-10-14/?utm_source=chatgpt.com "China takes steps against US-linked units of S.Korea shipbuilder Hanwha"
[8]: https://www.wsj.com/business/hd-hyundai-marine-solution-makes-strong-debut-in-south-korea-e5e63451?utm_source=chatgpt.com "KKR-Backed HD Hyundai Marine Makes Strong Debut in South Korea"

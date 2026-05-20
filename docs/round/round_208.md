순서상 이번은 **R4 Loop 8 — 소재·스프레드·전략자원 가격경로 검증 라운드**다.

이번 라운드는 원시 수정주가 일봉 OHLC를 안정적으로 직접 추출하지 못한 종목에 대해 숫자를 지어내지 않고, **Reuters / FT / WSJ / MarketWatch에 남은 가격 anchor, 이벤트 수익률, 계약·재무 수치**로 계산 가능한 값만 계산했다.

```text
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
```

---

# 1. 이번 라운드 대섹터

```text
R4 = 소재·스프레드·전략자원
large_sector = MATERIALS_SPREAD_STRATEGIC
round = R4 Loop 8 / price-path validation
```

R4의 기본 검증축은 `product_spread`, `cost_curve`, `capacity_discipline`, `commodity_peak`, `eps_normalization`이다. R4는 정유, 화학, 철강, 비철금속, 희토류, 리튬, 귀금속, 제지, LNG, 종합상사, 전략자원 테마를 포함한다. 

Round 119 기준으로 R4에서 부족한 증거는 단순 `commodity_price_up`이고, 필요한 증거는 `price_floor`, `offtake`, `cost_curve`, `fcf`, `supply_discipline`다. Green blocker는 `spread_reversal`, `china_oversupply`, `inventory_build`다. 

---

# 2. 대상 canonical archetype

```text
REFINING_OIL_SPREAD
CHEMICAL_SPREAD
PETROCHEMICAL_RESTRUCTURING_KOREA
COMMODITY_SPREAD_CYCLE_NOT_STRUCTURAL
NONFERROUS_STRATEGIC_METALS
RARE_METALS_STRATEGIC_MATERIALS
RARE_METALS_PRICE_FLOOR_OFFTAKE
LITHIUM_BATTERY_RAW_MATERIAL
LITHIUM_CYCLE_OVERLAY
POLYSILICON_NON_CHINA_SUPPLY_OPTION
COPPER_PROCESSING_PLUS_DEFENSE
EVENT_PREMIUM_GOVERNANCE_OVERLAY
COMMODITY_PRICE_4C_OVERLAY
```

이번 R4의 핵심 질문은 이거다.

```text
원자재 가격·스프레드·정책·지분 이벤트로 오른 것인가?
아니면 price floor, offtake, cost curve, supply discipline, FCF가 잠겨서
이익 체급이 구조적으로 바뀌는가?
```

---

# 3. deep sub-archetype

```text
비철·전략광물:
- Korea Zinc
- zinc / lead / copper / gold / silver
- antimony / germanium / gallium
- U.S. critical minerals smelter
- governance battle
- tender offer / buyback / new share issue
- dilution vs strategic growth

석유화학 구조조정:
- Lotte Chemical
- LG Chem
- Daesan NCC
- Yeochun NCC
- naphtha cracking overcapacity
- China / Middle East oversupply
- capacity cut / shutdown
- restructuring relief vs true rerating

정유·스프레드:
- SK Innovation
- refining margin
- geopolitical refinery squeeze
- operating profit swing
- cyclical_success vs structural E2R

리튬·전략자원:
- POSCO Holdings
- MinRes Wodgina / Mt Marion
- spodumene offtake
- lithium price collapse/rebound
- resource security vs commodity cycle

폴리실리콘 / 비중국 소재:
- OCI Holdings
- non-China polysilicon
- U.S. solar cell expansion
- SpaceX media report
- confirmed contract vs unconfirmed report

구리·방산 이벤트:
- Poongsan
- ammunition business
- copper processing
- Hanwha acquisition report
- management premium rumor
- event premium vs recurring FCF
```

---

# 4. 국장 신규 후보 case

## Case A — 고려아연 `event_premium + strategic success_candidate + 4B/4C-watch`

```text
symbol = 010130
case_type = event_premium + success_candidate + 4B-watch
archetype = NONFERROUS_STRATEGIC_METALS / EVENT_PREMIUM_GOVERNANCE_OVERLAY
```

### evidence

2024년 9월 MBK파트너스와 영풍은 고려아연에 대해 주당 660,000원 공개매수를 시작했다. 직전 종가는 556,000원이었고, 공개매수 발표 후 고려아연 주가는 19.8% 상승했다. WSJ는 장중 690,000원까지 올라 24% 상승했다고 보도했다. 이 구간은 전략금속 Stage 3가 아니라 **경영권 event premium**이다. ([Reuters][1])

2024년 10월 21일 법원이 고려아연의 자사주 공개매수 저지 가처분을 기각하자 고려아연은 877,000원으로 6.4% 상승해 사상 최고가를 기록했다. 이는 9월 12일 종가 556,000원 대비 +57.7%다. 하지만 2024년 10월 30일에는 1.8B달러 규모 신주발행 계획 발표 후 주가가 하한가 수준인 -29.9%까지 급락했다. 당시 신주 발행 예정가는 670,000원으로 전일 종가 1,543,000원 대비 약 -56.6% 낮았다. ([Reuters][2])

2025년 12월에는 미국 정부가 고려아연의 74억 달러 Tennessee critical minerals plant를 지원한다는 보도가 나왔고, 해당 시설은 antimony, germanium, gallium, zinc, lead, copper, precious metals 등을 생산할 예정이며 상업가동은 2027~2029년에 단계적으로 시작될 예정이다. 해당 보도 후 고려아연 주가는 최대 27% 상승했다. ([Financial Times][3])

### stage date

```text
Stage 1:
2024-09-13
- MBK/Young Poong tender offer
- governance / control premium event

Stage 2:
2025-12-15
- U.S. critical minerals plant support
- $7.4B Tennessee project
- strategic metals supply-chain evidence

Stage 3:
보류
- 상업가동 2027~2029
- offtake, FCF, dilution, capex burden 확인 필요

Stage 4B:
2024-09-13 ~ 2024-10-21
- 공개매수·자사주·Bain·경영권 분쟁으로 price-first rally
- 556,000원 → 877,000원

Stage 4C-watch:
2024-10-30
- $1.8B new share issue
- 주가 -29.9%
- dilution / governance trust shock

추가 Stage 2 / 4B-watch:
2025-12-24
- 법원이 U.S. smelter funding share sale 저지 요청 기각
- 고려아연 주가 최대 +5%, 영풍 -10.5%
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters / WSJ / FT reported price anchors

stage3_price:
N/A

event_base_price:
556,000원

tender_offer_price:
660,000원

event_intraday_peak_2024-09-13:
690,000원

MFE_1D_from_base_to_intraday_peak:
(690,000 / 556,000) - 1
= +24.1%

Reuters_event_return_2024-09-13:
+19.8%

record_close_2024-10-21:
877,000원

MFE_from_556000_to_877000:
(877,000 / 556,000) - 1
= +57.7%

pre_share_issue_close_2024-10-29:
1,543,000원

share_issue_event_MAE_1D:
-29.9%

implied_limit_down_price:
1,543,000 * (1 - 0.299)
= 약 1,081,643원

new_share_issue_price:
670,000원

issue_price_discount_vs_prior_close:
(670,000 / 1,543,000) - 1
= -56.6%

critical_minerals_project_event_MFE:
+27% reported max move

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

drawdown_after_peak:
at least -29.9% event drawdown from pre-issue close
```

### alignment

```text
score_price_alignment = event_premium + success_candidate
rerating_result = strategic_material_watch
stage_failure_type = should_not_be_green_until_project_fcf
```

### 교정

고려아연은 R4에서 `strategic_metal` 자체보다 **event premium / dilution / capex / governance**를 분리해야 한다.

```text
올릴 축:
strategic_material_status
U.S._government_support
offtake_or_price_floor
future_FCF_visibility

내릴 축:
tender_offer_premium
governance_battle
share_issue_dilution
capex_heavy_project_pre_revenue
```

---

## Case B — 롯데케미칼 `4C-thesis-break + restructuring_watch`

```text
symbol = 011170
case_type = 4C-thesis-break + restructuring_watch
archetype = PETROCHEMICAL_RESTRUCTURING_KOREA / CHEMICAL_SPREAD
```

### evidence

2024년 롯데케미칼은 영업손실이 전년 대비 157% 확대된 8,950억 원을 기록했고, 이는 2011년 이후 가장 큰 영업손실이었다. Reuters는 한국 석유화학 기업들이 중국·중동 증설과 수요 둔화에 따른 구조적 공급과잉에 눌리고 있다고 설명했다. ([Reuters][4])

2025년 11월 롯데케미칼과 HD현대 측은 석유화학 구조조정 계획을 제출했고, 2026년 2월 정부는 첫 석유화학 구조조정 프로젝트를 승인했다. 계획에는 롯데케미칼 대산 NCC 1.1 million ton 설비의 3년 가동중단, HD현대케미칼과의 통합, 2조 원 이상 지원 패키지, 1.2조 원 자본확충이 포함됐다. ([Reuters][5])

### stage date

```text
Stage 1:
2024~2025
- 석유화학 바닥론
- 중국 부양 기대
- 구조조정 기대

Stage 2:
2025-11-26
- HD Hyundai / Lotte Chemical Daesan restructuring plan
- overcapacity relief direction

Stage 3:
없음
- 구조조정 계획만으로 Green 금지
- spread, OPM, FCF 전환 확인 필요

Stage 4B:
구조조정 기대만으로 급등하면 4B-watch

Stage 4C:
2025-02-07
- 2024 영업손실 8,950억 원
- YoY 손실 +157%
- China / Middle East oversupply
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters financial and restructuring evidence

stage3_price:
N/A

stock OHLC:
price_data_unavailable_after_deep_search

operating_loss_2024:
895.0 billion won

operating_loss_worsening:
+157% YoY

Daesan_NCC_capacity_to_halt:
1.1 million tons per year

shutdown_duration:
3 years

support_package:
>2.0 trillion won

capital_increase:
1.2 trillion won

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
score_price_alignment = thesis_break_then_restructuring_watch
rerating_result = no_rerating / restructuring_relief_candidate
stage_failure_type = should_have_been_red_or_watch
```

### 교정

롯데케미칼은 R4에서 `capacity_cut`만으로 Stage 3를 주면 안 되는 케이스다.

```text
Stage 2 가능:
capacity cut
government restructuring support

Stage 3 조건:
spread recovery
OPM recovery
FCF turn
working capital improvement
debt burden stabilization
```

---

## Case C — LG화학 `failed_rerating / petrochemical 4C-watch`

```text
symbol = 051910
case_type = failed_rerating / 4C-watch
archetype = CHEMICAL_SPREAD / PETROCHEMICAL_RESTRUCTURING_KOREA
```

### evidence

2024년 LG화학의 영업이익은 전년 대비 63.75% 감소해 9,168억 원을 기록했고, 이는 2019년 이후 최저였다. 석유화학 부문은 2024년 4분기 990억 원 영업손실을 냈다. 회사 측은 중국의 공급과잉과 수요 부진이 지속되고 있다고 설명했다. ([Reuters][4])

2025년 12월 LG화학은 정부에 석유화학 구조조정 계획을 제출했다. 다만 세부 내용은 공개하지 않았다. ([Reuters][6])

2025년 11월에는 LG화학이 LG에너지솔루션 지분을 약 80%에서 70%로 낮춰 장기 재무건전성과 주주환원을 강화하겠다고 발표했지만, 발표 후 LG화학 주가는 2.9%, LG에너지솔루션은 6% 하락했다. ([Reuters][7])

### stage date

```text
Stage 1:
2024~2025
- 석유화학 업황 바닥론
- 중국 부양 기대
- 주주환원 / 지분매각 기대

Stage 2:
2025-12-19
- petrochemical restructuring plan submitted to government

Stage 3:
없음
- 구조조정 계획, 지분매각 계획만으로 Green 금지
- spread, OPM, FCF 회복 확인 필요

Stage 4B:
주주환원 기대만으로 가격이 먼저 반응하면 4B-watch

Stage 4C:
2025-02-07
- petrochemical loss
- operating profit down 63.75%
- oversupply thesis break
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters financial and event return anchors

stage3_price:
N/A

operating_profit_2024:
916.8 billion won

operating_profit_decline:
-63.75% YoY

petrochemical_Q4_loss:
99.0 billion won

LGES_stake_sale_event_MAE_1D:
LG Chem = -2.9%
LG Energy Solution = -6.0%

MFE / MAE:
price_data_unavailable_after_deep_search beyond reported event returns

below_stage3_price_flag:
N/A

peak_price:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break / evidence_good_but_price_failed
rerating_result = failed_petrochemical_rerating
stage_failure_type = should_have_been_red_or_watch
```

### 교정

LG화학은 R4에서 `spread_recovery_hope`를 낮추고 `actual_spread`, `OPM`, `FCF`, `working_capital`, `governance_capital_allocation`을 요구해야 한다.

---

## Case D — SK이노베이션 `cyclical_success / refining spread watch`

```text
symbol = 096770
case_type = cyclical_success
archetype = REFINING_OIL_SPREAD / COMMODITY_SPREAD_CYCLE_NOT_STRUCTURAL
```

### evidence

2025년 4월 SK이노베이션은 1분기 영업손실 450억 원을 기록했다. 이는 전년 동기 6,250억 원 영업이익에서 크게 악화된 것이고, 시장 예상 3,930억 원 영업이익을 크게 밑돌았다. Reuters는 해당 실적 발표 전 주가가 2.5% 하락 마감했다고 보도했다. ([Reuters][8])

2026년 5월에는 1분기 영업이익 2.2조 원을 기록해 전년 동기 300억 원 손실에서 크게 반전했고, LSEG SmartEstimate 1.4조 원을 웃돌았다. 다만 회사는 정유사업 정상화가 중동 갈등 해소 이후에도 시간이 걸릴 것이라고 경고했다. ([Reuters][9])

### stage date

```text
Stage 1:
2025-04-30
- refining margin recovery expectation
- 1Q loss despite margin recovery hope

Stage 2:
2026-05-13
- 1Q 2026 OP 2.2조 원
- LSEG estimate beat
- cyclical profit rebound

Stage 3:
없음
- 정유마진은 commodity cycle
- multi-quarter margin floor, FCF, capital return 확인 전 Green 금지

Stage 4B:
정제마진 / 중동 공급차질로 정유주가 급등하면 4B-watch

Stage 4C:
refining margin normalization, crude cost shock, supply recovery 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters financial and event return anchors

stage3_price:
N/A

2025_Q1_operating_result:
-45.0 billion won

2024_Q1_operating_result:
+625.0 billion won

profit_swing_2025_vs_2024:
-670.0 billion won

2025_event_MAE:
shares closed -2.5% before earnings announcement

2026_Q1_operating_profit:
2.2 trillion won

2025_Q1_comparable:
-30.0 billion won

profit_swing_2026_vs_2025:
+2.23 trillion won

LSEG_estimate:
1.4 trillion won

beat_vs_estimate:
2.2 / 1.4 - 1
= +57.1%

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
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
score_price_alignment = cyclical_success
rerating_result = refining_cycle_rebound
stage_failure_type = stage2_watch_success
```

### 교정

SK이노베이션은 R4에서 `refining_margin_rebound`를 Stage 2로 볼 수 있지만, Stage 3는 아니다.

```text
Stage 3 조건:
multi-quarter margin floor
FCF
deleveraging
shareholder return
non-refining loss control
```

---

## Case E — POSCO홀딩스 `success_candidate / lithium resource security watch`

```text
symbol = 005490
case_type = success_candidate / cyclical_watch
archetype = LITHIUM_BATTERY_RAW_MATERIAL / RARE_METALS_PRICE_FLOOR_OFFTAKE
```

### evidence

2025년 11월 호주 Mineral Resources는 리튬 사업 일부 지분 30%를 POSCO에 7.65억 달러에 매각한다고 발표했다. 이 거래로 POSCO는 Wodgina와 Mt Marion 리튬 광산 각각에 간접 15% 지분을 갖게 되며, 보유 지분에 따라 spodumene concentrate를 받는 구조다. Reuters는 MinRes 주가가 발표 후 최대 10.8% 상승해 2024년 10월 이후 최고 수준을 기록했다고 보도했다. ([Reuters][10])

하지만 같은 Reuters 보도에 따르면 spodumene 가격은 2022년 톤당 6,000달러 이상에서 2025년 6월 약 610달러까지 하락했고, 8월 약 880달러로 반등했지만 여전히 2022년 고점에는 크게 못 미쳤다. 이는 원료 지분 확보가 Stage 2 후보는 될 수 있지만, 리튬 가격 이벤트만으로 Stage 3를 줄 수 없다는 뜻이다. ([Reuters][10])

### stage date

```text
Stage 1:
2023~2025
- 포스코 리튬 / 배터리 원료 내재화 기대

Stage 2:
2025-11-11
- MinRes lithium JV stake deal
- Wodgina / Mt Marion 간접 지분
- spodumene concentrate 확보

Stage 3:
없음
- 실제 lithium hydroxide margin, offtake, FCF 확인 필요

Stage 4B:
리튬 가격 반등으로 자원주가 먼저 뛰면 4B-watch

Stage 4C:
lithium price 재하락, project write-down, demand slowdown 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters commodity and transaction anchors

POSCO_stage2_stock_price:
price_data_unavailable_after_deep_search
- Reuters는 MinRes 주가 반응만 제공하고 POSCO 주가 reaction anchor는 제공하지 않음.

MinRes_event_MFE_1D:
+10.8%

transaction_value:
$765 million

POSCO_indirect_stake:
15% in Wodgina and Mt Marion each

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

POSCO홀딩스는 `resource_security`를 Stage 2로 올려줄 수 있다. 그러나 Stage 3는 price floor, offtake economics, downstream margin, FCF가 필요하다.

---

## Case F — OCI홀딩스 `success_candidate + event_premium / unconfirmed SpaceX`

```text
symbol = 010060
case_type = success_candidate + event_premium
archetype = POLYSILICON_NON_CHINA_SUPPLY_OPTION
```

### evidence

2025년 6월 FT는 OCI가 미국 Texas plant 생산능력을 2027년까지 10GW로 늘리기 위해 12억 달러를 투자할 계획이라고 보도했다. OCI는 AI 데이터센터 전력수요와 중국산 태양광 규제를 기회로 보고 미국 solar cell 생산 확대를 추진하고 있다. ([Financial Times][11])

2026년 4월 Reuters는 OCI의 말레이시아 자회사 OCI TerraSus가 SpaceX에 polysilicon을 공급하기 위한 다년 계약을 논의 중이라는 한국 매체 보도를 전했다. 그러나 SpaceX는 답변하지 않았고, OCI 대변인은 해당 보도를 확인할 수 없다고 밝혔다. ([Reuters][12])

### stage date

```text
Stage 1:
2025-06-07
- U.S. solar cell capacity expansion
- AI data center power demand narrative

Stage 2:
2025-06-07 후보
- $1.2B investment
- Texas capacity to 10GW by 2027

Stage 3:
없음
- capex-heavy project
- margin, customer contract, FCF 확인 전 Green 금지

Stage 4B:
2026-04-14
- SpaceX supply talk media report
- unconfirmed event premium

Stage 4C:
계약 불발, U.S. subsidy rollback, polysilicon price decline, capex overrun 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
FT / Reuters evidence anchors

stage3_price:
N/A

stock OHLC:
price_data_unavailable_after_deep_search

U.S._investment:
$1.2B

target_capacity:
10GW by 2027

SpaceX_contract_status:
unconfirmed media report

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
score_price_alignment = success_candidate + event_premium
rerating_result = non_china_polysilicon_watch
stage_failure_type = stage2_evidence_not_green
```

### 교정

OCI는 R4에서 `non-China supply`는 좋은 Stage 2지만, SpaceX media report는 Green 금지다.

```text
Stage 3 조건:
confirmed contract
volume
price
duration
margin
FCF after capex
```

---

## Case G — 풍산 `event_premium / copper + defense rumor`

```text
symbol = 103140
case_type = event_premium / price_moved_without_evidence
archetype = COPPER_PROCESSING_PLUS_DEFENSE / EVENT_PREMIUM_GOVERNANCE_OVERLAY
```

### evidence

2026년 4월 Reuters는 한화에어로스페이스가 풍산의 방산사업부 인수를 위해 약 1.5조 원 규모 제안을 냈다는 한국경제 보도를 전했다. 한화에어로스페이스는 논평을 거부했고, 풍산은 사업구조 재편 등 여러 방안을 검토 중이나 결정된 것은 없다고 밝혔다. 풍산은 탄약과 미사일 탄두를 생산하고 수출하는 업체로 설명됐다. ([Reuters][13])

### stage date

```text
Stage 1:
2026-04-03
- Hanwha Aerospace acquisition report
- Poongsan defense unit / ammunition premium
- copper + defense theme

Stage 2:
없음 또는 약한 Stage 2
- 결정된 것 없음
- confirmed transaction 없음

Stage 3:
없음
- 매각 루머/구조개편 검토만으로 Green 금지

Stage 4B:
거래 기대만으로 주가 급등 시 4B-watch

Stage 4C:
거래 불발, copper spread reversal, defense order slowdown 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters evidence source only

stage3_price:
N/A

stock OHLC:
price_data_unavailable_after_deep_search
- Reuters 기사에 풍산 주가 reaction anchor 없음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

deal_value_reported:
1.5 trillion won

transaction_status:
not decided

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
score_price_alignment = event_premium / unknown_insufficient_evidence
rerating_result = copper_defense_event_watch
stage_failure_type = stage1_attention_only
```

### 교정

풍산은 `copper + defense`가 좋아 보여도 Stage 3 조건은 본업의 **copper spread, ammunition order, margin, FCF**다. 매각 루머는 event premium이다.

---

# 5. 이번 R4 case별 요약표

| case     | 분류                                |                                                                        실제 가격검증 | alignment                       |
| -------- | --------------------------------- | -----------------------------------------------------------------------------: | ------------------------------- |
| 고려아연     | event premium + success_candidate | 556,000→690,000 +24.1%; 556,000→877,000 +57.7%; 신주발행 -29.9%; U.S. smelter +27% | event_premium + strategic_watch |
| 롯데케미칼    | 4C / restructuring watch          |                                      2024 영업손실 8,950억, +157%; Daesan NCC 3년 중단 | thesis_break                    |
| LG화학     | failed_rerating                   |                             OP -63.75%, petrochem Q4 loss 990억; 지분매각 이벤트 -2.9% | failed_rerating                 |
| SK이노베이션  | cyclical_success                  |               2025 Q1 loss -450억, 주가 -2.5%; 2026 OP 2.2조, estimate beat +57.1% | cyclical_success                |
| POSCO홀딩스 | success_candidate / lithium watch |                    MinRes +10.8%; spodumene -89.8% peak-to-low, +44.3% rebound | resource_security_watch         |
| OCI홀딩스   | success_candidate + event premium |                                $1.2B U.S. expansion, SpaceX report unconfirmed | insufficient_evidence           |
| 풍산       | event_premium                     |                                                       1.5조 원 방산부문 인수 보도, 결정 없음 | event_premium                   |

---

# 6. score-price alignment 판정

```text
event_premium:
- 고려아연 tender / buyback / governance battle
- 풍산 Hanwha acquisition report
- OCI SpaceX media report

success_candidate:
- 고려아연 U.S. critical minerals plant
- POSCO Holdings lithium resource stake
- OCI U.S. solar/polysilicon expansion

cyclical_success:
- SK Innovation refining profit rebound
- POSCO lithium resource security with commodity-cycle exposure

thesis_break:
- 롯데케미칼 petrochemical loss / oversupply
- LG Chem petrochemical profit collapse

price_moved_without_evidence:
- 고려아연 governance premium 구간
- 풍산 acquisition rumor 구간
- OCI SpaceX unconfirmed media report

4B-watch:
- 고려아연 tender/buyback rally
- 고려아연 U.S. smelter +27% event
- lithium price rebound event
- SpaceX polysilicon report
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
capital_return_from_cashflow +3
```

### 이유

롯데케미칼 구조조정은 Stage 2까지는 의미가 있지만, 손실 축소와 FCF 전환이 나오기 전 Stage 3가 아니다. 고려아연의 U.S. critical minerals project도 전략성은 높지만 상업가동이 2027~2029년이고 capex·dilution·offtake·FCF 확인이 필요하다. ([Reuters][14])

## 내릴 축

```text
commodity_price_up_only -5
restructuring_plan_without_margin -4
policy_support_without_fcf -4
tender_offer_or_governance_premium -5
unconfirmed_media_report -5
capacity_cut_expectation_only -3
lithium_price_event -4
refining_margin_geopolitical_shock -3
customer_or_contract_unconfirmed -4
capex_heavy_project_pre_revenue -4
```

### 이유

고려아연의 공개매수·자사주·신주발행 구간은 가격 변동이 크지만 구조적 Stage 3가 아니라 governance/event premium이다. OCI의 SpaceX 보도는 회사가 확인하지 못한 media report였고, 풍산도 방산부문 인수 보도에 대해 결정된 것이 없다고 밝혔다. ([Reuters][1])

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
9. 가격경로가 evidence 이후 따라옴

금지:
commodity price spike
tender offer premium
governance battle
정책 지원 기대
미확정 media report
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

이번 세션에서 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉을 안정적으로 직접 확보하지 못했다. 대신 Reuters / FT / WSJ / MarketWatch의 가격 anchor와 이벤트 수익률을 사용해 계산 가능한 부분은 직접 계산했다.

---

# 9. patch-ready 출력

## docs/round/round_136.md 요약

```md
# R4 Loop 8. Materials / Spread / Strategic Resources Price Validation

이번 라운드는 R4 price-validation 라운드다.

핵심 결론:
- 고려아연은 strategic metals 후보이지만, 2024년 tender/buyback/new-share-issue 구간은 구조적 Stage 3가 아니라 event premium / governance 4B·4C-watch다.
- 고려아연은 556,000원에서 877,000원까지 +57.7% 상승했지만, 이후 신주발행 발표로 -29.9% 급락했다.
- Lotte Chemical은 2024년 영업손실 8,950억 원, 손실 +157%로 petrochemical thesis break다. Daesan NCC 3년 중단은 Stage 2 restructuring relief이지 Stage 3가 아니다.
- LG Chem은 영업이익 -63.75%, petrochemical Q4 loss 990억 원으로 failed rerating이다.
- SK Innovation의 2026년 OP 2.2조 원은 refining-cycle rebound지만, 구조적 Stage 3는 multi-quarter margin floor와 FCF 확인 전 보류다.
- POSCO Holdings의 MinRes lithium JV는 Stage 2 resource-security 후보지만, lithium price collapse/rebound cycle을 통과해야 한다.
- OCI의 SpaceX polysilicon report와 Poongsan-Hanwha acquisition report는 unconfirmed event premium이며 Stage 3 금지다.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 136 R4 Loop 8 Materials Spread Strategic Price Validation

## 반영 내용
- R4 Loop 8 price-validation 라운드를 추가했다.
- Korea Zinc governance event, petrochemical restructuring, refining cycle, lithium resource security, polysilicon media report, copper-defense event를 비교했다.
- Reuters/FT/WSJ/MarketWatch reported price anchors로 가능한 MFE/MAE를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- product spread, FCF, supply discipline, offtake 가중치 강화
- governance premium, restructuring plan without margin, unconfirmed media report 감점 강화
- dilution / new share issue / event premium 4B·4C watch 강화
```

## case row 초안

```jsonl
{"case_id":"r4_loop8_korea_zinc_event_strategic_watch","symbol":"010130","company_name":"고려아연","case_type":"event_premium","primary_archetype":"NONFERROUS_STRATEGIC_METALS","stage1_date":"2024-09-13","stage2_date":"2025-12-15","stage4b_date":"2024-10-21","stage4c_date":"2024-10-30","price_validation":{"price_data_source":"Reuters/WSJ/FT reported anchors","stage3_price":null,"event_base_price":556000,"event_intraday_peak":690000,"mfe_1d":24.1,"record_close":877000,"mfe_from_base_to_record_close":57.7,"pre_share_issue_close":1543000,"share_issue_mae_1d":-29.9,"issue_price_discount_pct":-56.6,"critical_minerals_event_mfe":27.0,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"strategic_material_watch","notes":"Governance/tender/buyback are event premium; U.S. critical minerals plant is Stage 2 until offtake, FCF and dilution risk clear."}
{"case_id":"r4_loop8_lotte_chemical_petrochem_break","symbol":"011170","company_name":"롯데케미칼","case_type":"4c_thesis_break","primary_archetype":"PETROCHEMICAL_RESTRUCTURING_KOREA","stage2_date":"2025-11-26","stage4c_date":"2025-02-07","price_validation":{"price_data_source":"Reuters financial/restructuring anchors","stage3_price":null,"operating_loss_2024_krw_bn":895.0,"operating_loss_worsening_pct":157.0,"daesan_ncc_capacity_mn_tpy":1.1,"shutdown_years":3,"support_package_krw_trn":2.0,"capital_increase_krw_trn":1.2,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_then_restructuring_watch","rerating_result":"restructuring_relief_candidate","notes":"Capacity cut is Stage 2; Stage 3 requires spread, OPM and FCF recovery."}
{"case_id":"r4_loop8_lg_chem_petrochem_failed_rerating","symbol":"051910","company_name":"LG화학","case_type":"failed_rerating","primary_archetype":"CHEMICAL_SPREAD","stage2_date":"2025-12-19","stage4c_date":"2025-02-07","price_validation":{"price_data_source":"Reuters financial/event anchors","stage3_price":null,"operating_profit_2024_krw_bn":916.8,"operating_profit_decline_pct":-63.75,"petrochemical_q4_loss_krw_bn":99.0,"lges_stake_sale_event_mae_1d":-2.9,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"failed_petrochemical_rerating","notes":"Petrochemical spread hope is not Green without actual spread, OPM and FCF recovery."}
{"case_id":"r4_loop8_sk_innovation_refining_cycle","symbol":"096770","company_name":"SK이노베이션","case_type":"cyclical_success","primary_archetype":"REFINING_OIL_SPREAD","stage2_date":"2026-05-13","price_validation":{"price_data_source":"Reuters financial/event anchors","stage3_price":null,"q1_2025_op_loss_krw_bn":-45.0,"q1_2025_event_mae":-2.5,"q1_2026_op_krw_trn":2.2,"profit_swing_2026_vs_2025_krw_trn":2.23,"beat_vs_lseg_estimate_pct":57.1,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"cyclical_success","rerating_result":"refining_cycle_rebound","notes":"Refining rebound is Stage 2/cyclical; Stage 3 requires multi-quarter margin floor and FCF."}
{"case_id":"r4_loop8_posco_lithium_resource_security","symbol":"005490","company_name":"POSCO홀딩스","case_type":"success_candidate","primary_archetype":"LITHIUM_BATTERY_RAW_MATERIAL","stage2_date":"2025-11-11","price_validation":{"price_data_source":"Reuters commodity/transaction anchors","stage3_price":null,"minres_event_mfe_1d":10.8,"transaction_value_usd_mn":765,"posco_indirect_stake_pct":15.0,"spodumene_peak_to_low_drawdown_pct":-89.8,"spodumene_low_to_rebound_pct":44.3,"spodumene_rebound_vs_peak_pct":-85.3,"price_validation_status":"posco_stock_ohlc_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_cyclical_watch","rerating_result":"resource_security_watch","notes":"Lithium mine stake is Stage 2; Stage 3 requires price floor, offtake economics, downstream margin and FCF."}
{"case_id":"r4_loop8_oci_non_china_polysilicon_event","symbol":"010060","company_name":"OCI홀딩스","case_type":"success_candidate","primary_archetype":"POLYSILICON_NON_CHINA_SUPPLY_OPTION","stage1_date":"2025-06-07","stage4b_date":"2026-04-14","price_validation":{"price_data_source":"FT/Reuters evidence anchors","stage3_price":null,"us_investment_usd_bn":1.2,"target_capacity_gw":10,"target_year":2027,"spacex_report_status":"unconfirmed","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_event_premium","rerating_result":"non_china_polysilicon_watch","notes":"U.S. expansion is Stage 2; unconfirmed SpaceX report is event premium."}
{"case_id":"r4_loop8_poongsan_copper_defense_event","symbol":"103140","company_name":"풍산","case_type":"event_premium","primary_archetype":"COPPER_PROCESSING_PLUS_DEFENSE","stage1_date":"2026-04-03","price_validation":{"price_data_source":"Reuters evidence anchor","stage3_price":null,"reported_deal_value_krw_trn":1.5,"transaction_status":"not_decided","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium","rerating_result":"copper_defense_event_watch","notes":"Hanwha acquisition report is not Stage 3; confirmed order/margin/FCF needed."}
```

## shadow weight row 초안

```csv
archetype,product_spread,fcf,supply_discipline,offtake,cost_curve,event_penalty,dilution_redteam,4b_watch_sensitivity,hard_4c_sensitivity,notes
NONFERROUS_STRATEGIC_METALS,+3,+4,+3,+5,+4,-5,+5,+5,+3,Korea Zinc strategic project is Stage 2; governance/tender/share issue are event and dilution risk.
PETROCHEMICAL_RESTRUCTURING_KOREA,+5,+5,+5,+1,+3,-3,+2,+3,+5,Lotte Chemical restructuring is Stage 2; losses and oversupply are 4C until spread/FCF recover.
CHEMICAL_SPREAD,+5,+5,+4,+1,+3,-3,+2,+3,+5,LG Chem petrochem loss blocks Green until actual spread and OPM recovery.
REFINING_OIL_SPREAD,+5,+4,+2,+1,+3,-3,+1,+4,+3,SK Innovation profit rebound is cyclical success; Stage 3 requires multi-quarter margin floor.
LITHIUM_BATTERY_RAW_MATERIAL,+2,+4,+2,+5,+4,-4,+2,+4,+4,POSCO lithium stake is resource-security Stage 2; lithium price event remains cyclical.
POLYSILICON_NON_CHINA_SUPPLY_OPTION,+2,+4,+3,+4,+3,-5,+3,+5,+3,OCI U.S. expansion is Stage 2; unconfirmed SpaceX report is event premium.
COPPER_PROCESSING_PLUS_DEFENSE,+3,+4,+2,+3,+3,-5,+1,+5,+3,Poongsan acquisition rumor is event premium until confirmed transaction or order/margin/FCF.
```

---

# 이번 R4 Loop 8 결론

R4는 Stage 3를 매우 보수적으로 줘야 한다. 가격이 먼저 움직이는 재료가 너무 많다.

```text
1. 고려아연은 전략광물로 좋은 Stage 2 후보지만,
   공개매수·자사주·신주발행·경영권 분쟁 구간은 구조적 Stage 3가 아니라 event premium이다.

2. 롯데케미칼과 LG화학은 석유화학 oversupply thesis break다.
   구조조정은 relief이지, spread·OPM·FCF 회복 전 Stage 3가 아니다.

3. SK이노베이션의 2026년 이익 반등은 cyclical_success다.
   정유마진은 multi-quarter floor와 FCF 확인 전 Green 금지다.

4. POSCO홀딩스의 lithium JV는 resource-security Stage 2다.
   리튬 가격은 peak 대비 아직 크게 낮고, offtake economics와 downstream margin이 필요하다.

5. OCI와 풍산은 미확정 media report / acquisition rumor를 Stage 3로 올리면 안 된다.
   확인된 계약·물량·가격·마진·FCF가 필요하다.
```

한 문장으로 압축하면:

> **R4에서 진짜 Stage 3는 “원자재 가격이 오른다”나 “전략자원 테마가 붙는다”가 아니라, 가격·원가·공급규율·offtake·FCF가 잠겨서 이익 체급이 구조적으로 바뀌는 순간이다.**
> **R4는 governance event, commodity event, restructuring relief, unconfirmed media report를 전부 4B/Event Premium으로 먼저 분리해야 점수표가 산다.**

[1]: https://www.reuters.com/markets/deals/private-equity-mbk-young-poong-launch-15-bln-tender-offer-korea-zinc-shares-2024-09-13/?utm_source=chatgpt.com "Private equity MBK, Young Poong launch $1.5 bln tender offer for Korea Zinc shares"
[2]: https://www.reuters.com/markets/deals/korea-zinc-shares-surge-record-high-after-court-clears-hurdle-buyback-offer-2024-10-21/?utm_source=chatgpt.com "Korea Zinc shares surge to record high after court clears hurdle for buyback offer"
[3]: https://www.ft.com/content/d885ab55-b4f8-4c8f-a213-94f2778863ac?utm_source=chatgpt.com "US backs $7.4bn critical minerals smelter to counter China"
[4]: https://www.reuters.com/markets/commodities/south-korean-petrochemical-firms-profits-plunge-2024-oversupply-persists-2025-02-07/?utm_source=chatgpt.com "South Korean petrochemical firms' profits plunge in 2024 as oversupply persists"
[5]: https://www.reuters.com/world/asia-pacific/south-koreas-hd-hyundai-lotte-chemical-submit-plan-restructure-petrochemical-2025-11-26/?utm_source=chatgpt.com "South Korea's HD Hyundai, Lotte Chemical submit plan to restructure petrochemical businesses"
[6]: https://www.reuters.com/world/asia-pacific/lg-chem-submits-petrochem-restructuring-plan-government-2025-12-19/?utm_source=chatgpt.com "LG Chem submits petrochem restructuring plan to government"
[7]: https://www.reuters.com/sustainability/sustainable-finance-reporting/lg-chem-plans-sell-lg-energy-solution-stake-shareholder-returns-2025-11-28/?utm_source=chatgpt.com "LG Chem plans to sell LG Energy Solution stake for shareholder returns"
[8]: https://www.reuters.com/business/energy/sk-innovation-expects-refining-margins-gradually-improve-q2-2025-04-30/?utm_source=chatgpt.com "SK Innovation sinks to Q1 operating loss, sees refining margins improving"
[9]: https://www.reuters.com/world/asia-pacific/sk-innovation-warns-refining-recovery-take-time-beats-q1-profit-estimates-2026-05-13/?utm_source=chatgpt.com "SK Innovation warns refining recovery to take time, beats Q1 profit estimates"
[10]: https://www.reuters.com/business/energy/australias-minres-sell-30-lithium-jv-stake-posco-765-mln-2025-11-11/?utm_source=chatgpt.com "Australia's MinRes inks $765 million deal with POSCO for lithium JV stake, shares surge"
[11]: https://www.ft.com/content/e618a7e3-6388-42f9-beb8-c32599f7239d?utm_source=chatgpt.com "Solar group OCI doubles down on US despite Donald Trump's war on clean energy"
[12]: https://www.reuters.com/world/asia-pacific/unit-south-koreas-oci-talks-with-spacex-supply-polysilicon-media-says-2026-04-14/?utm_source=chatgpt.com "Unit of South Korea's OCI in talks with SpaceX to supply polysilicon, media says"
[13]: https://www.reuters.com/world/asia-pacific/hanwha-seeks-buy-poongsans-ammunition-business-about-11-billion-newspaper-says-2026-04-03/?utm_source=chatgpt.com "Hanwha seeks to buy Poongsan's ammunition business for about $1.1 billion, newspaper says"
[14]: https://www.reuters.com/world/asia-pacific/south-korea-approves-first-petrochemical-restructuring-deal-supply-glut-weighs-2026-02-24/?utm_source=chatgpt.com "South Korea approves first petrochemical restructuring deal as supply glut weighs"

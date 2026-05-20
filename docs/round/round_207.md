순서상 이번은 **R3 Loop 8 — 2차전지·전기차·친환경 가격경로 검증 라운드**다.

이번 라운드는 R3 특성상 결론이 꽤 보수적이다. 배터리 섹터는 ESS 전환, LFP, 미국 현지화, 세액공제 같은 좋은 재료가 분명 있지만, 동시에 EV 수요 둔화, 계약 취소, 계약가치 축소, CAPA 부담, AMPC 의존, 유상증자·부채 리스크가 강하게 남아 있다. 그래서 이번 R3 Loop 8의 기본값은 **Stage 3-Green 발굴이 아니라 false Green 차단**이다.

이번에도 원시 수정주가 일봉 OHLC를 안정적으로 직접 추출하지 못한 종목은 숫자를 지어내지 않았다. 대신 Reuters / WSJ / FT / MarketWatch가 제공한 **가격 anchor, 이벤트 수익률, 계약가치 변화**로 계산 가능한 값은 직접 계산했다.

```text
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
```

---

# 1. 이번 라운드 대섹터

```text
R3 = 2차전지·전기차·친환경
large_sector = BATTERY_EV_GREEN
round = R3 Loop 8 / price-path validation
```

R3의 기본 검증축은 `contract_quality`, `utilization`, `fcf`, `ev_demand`, `capa_overbuild`, `commodity_price`다. R3는 배터리 소재·장비·재활용·ESS·수소·재생에너지·CBAM·폐기물·데이터센터 물 재활용까지 포함하지만, 핵심은 계약이 실제 **GWh, 가동률, OPM, FCF, EPS revision**으로 내려오는지다. 

Round 119 기준으로 R3에서 부족한 증거는 `ev_theme`, `ess_theme`, `capa_announcement`이고, 필요한 증거는 `contract_amount`, `gwh_volume`, `opm`, `fcf`, `customer_quality`다. Green blocker는 `overcapacity`, `mineral_price_down`, `negative_fcf`다. 

---

# 2. 대상 canonical archetype

```text
BATTERY_MATERIALS_CAPEX_OVERHEAT
CATHODE_LONG_CONTRACT_VISIBILITY
BATTERY_CONTRACT_CANCELLATION_4C
BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE
ESS_LFP_GRID_STORAGE
EV_TO_ESS_CAPACITY_REDEPLOYMENT
EV_BATTERY_JV_RESTRUCTURING
SEPARATOR_EV_DEMAND_CYCLE
LITHIUM_CYCLE_OVERLAY
EVENT_LITHIUM_PRICE_RALLY
CHANNEL_STUFFING_INVENTORY_OVERLAY
PRICE_ONLY_RALLY
THESIS_BREAK_4C
```

이번 R3의 핵심 질문은 이거다.

```text
EV·ESS·배터리 테마인가?
아니면 계약이 실제 GWh·가동률·OPM·FCF·EPS revision으로 내려오는가?
```

---

# 3. deep sub-archetype

```text
셀 메이커:
- LG Energy Solution
- Samsung SDI
- SK On via SK Innovation
- ESS LFP pivot
- U.S. production line conversion
- AMPC / IRA tax credit quality
- EV demand slowdown
- Ford / GM / Tesla order risk
- contract cancellation
- utilization delay

양극재 / 전구체:
- L&F high-nickel cathode
- Tesla 4680 exposure
- POSCO Future M cathode/anode
- EcoPro Materials precursor
- long-term supply contract
- order call-off
- contract value reduction
- lithium price event
- inventory valuation

분리막 / 부품:
- SK IE Technology
- separator demand cycle
- SK On financial stress
- sale / restructuring risk
- customer concentration

R3 RedTeam:
- contract cancellation
- contract value collapse
- negative FCF
- subsidy-quality profit
- EV demand slowdown
- capex overbuild
- inventory / receivables
```

---

# 4. 국장 신규 후보 case

## Case A — LG에너지솔루션 `success_candidate + 4C-thesis-break`

```text
symbol = 373220
case_type = success_candidate + 4C-thesis-break
archetype = ESS_LFP_GRID_STORAGE / EV_TO_ESS_CAPACITY_REDEPLOYMENT / BATTERY_CONTRACT_CANCELLATION_4C
```

### evidence

2025년 7월 25일 LG에너지솔루션은 2분기 영업이익이 4,920억 원으로 전년 1,950억 원 대비 두 배 이상 증가했다고 밝혔지만, 그 이익은 미국 생산세액공제와 고객사의 선제 재고축적 효과가 컸다. Reuters는 AMPC 제외 시 영업이익이 14억 원에 그쳤고, 회사가 EV 수요 둔화에 대응해 ESS 생산을 늘리고 일부 EV 라인을 ESS로 전환하는 방안을 검토한다고 보도했다. 주가는 발표 후 오전장에서 1.6% 하락했다. ([Reuters][1])

2025년 7월 30일 LGES는 43억 달러 규모 LFP 배터리 공급계약을 발표했고, Reuters는 Tesla향 ESS 배터리 공급으로 보도했다. 계약 기간은 2027년 8월부터 2030년 7월까지이며, 미국 공장에서 공급하는 구조다. 이건 R3에서 좋은 Stage 2 evidence지만, 매출 인식이 2027년 이후이고 OPM/FCF가 아직 확인되지 않았으므로 Stage 3는 보류다. ([Reuters][2])

반대로 2025년 12월 Ford가 EV 모델을 중단하면서 LGES 공급계약을 취소했고, LGES 주가는 장중 최대 7.6% 하락했다. 이후 Freudenberg 계약 3.9조 원까지 종료되면서, Reuters는 LGES가 Ford와 Freudenberg 계약 종료로 약 13.5조 원의 기대 매출을 잃게 됐고 이는 2024년 매출 25.62조 원의 절반을 넘는 규모라고 보도했다. ([Reuters][3])

### stage date

```text
Stage 1:
2025-07-25
- EV 수요 둔화 속 ESS 전환 기대
- 미국 LFP ESS 생산 확대

Stage 2:
2025-07-30
- $4.3B LFP ESS supply contract
- Tesla향으로 보도
- 2027-08~2030-07 공급

Stage 3:
없음
- 매출 인식이 2027년 이후
- AMPC 제외 이익이 거의 없고, OPM/FCF 확인 전 Green 금지

Stage 4B:
ESS 전환 기대만으로 급등한 구간이 있으면 후보
- 이번 pass에서는 reported event peak anchor 없음

Stage 4C:
2025-12-18
- Ford EV battery supply deal cancellation
- 주가 장중 -7.6%

추가 4C:
2025-12-26
- Freudenberg 3.9조 원 계약 종료
- 총 13.5조 원 기대매출 손실
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported event returns and contract anchors

stage3_price:
N/A

stage2_price:
price_data_unavailable_after_deep_search
- Reuters는 2025-07-30 계약 보도에는 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

stage2_quality_check:
$4.3B contract is strong Stage 2, but delivery starts 2027 and margin/FCF unknown.

Q2_2025_event_MAE:
-1.6% after Q2 earnings / demand slowdown warning

Ford_cancellation_stage4c_MAE_1D:
-7.6%

lost_expected_revenue:
13.5조 원

lost_revenue_vs_2024_revenue:
13.5 / 25.62 = 52.7%

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

peak_price:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search

Stage 4C 큰 하락 이전 포착 여부:
partial_success
- Ford cancellation 당일 -7.6%는 이미 event 하락.
- 하지만 Ford EV 전략 후퇴와 EV 수요 둔화는 4C-watch를 앞당길 수 있었음.
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = ESS_success_candidate_but_EV_contract_break
stage_failure_type = stage2_watch_success_then_4C_watch
```

### 교정

LGES는 R3에서 가장 중요한 분리 기준을 만든다.

```text
ESS LFP contract:
Stage 2 가능

Stage 3 조건:
GWh delivery
utilization
OPM
FCF
AMPC 제외 이익
EV contract cancellation risk 통과

4C hard/watch:
contract cancellation
customer EV model cancellation
expected revenue loss > 50% of prior-year revenue
```

---

## Case B — L&F `4C-thesis-break / contract value collapse`

```text
symbol = 066970
case_type = 4C-thesis-break
archetype = CATHODE_LONG_CONTRACT_VISIBILITY / BATTERY_CONTRACT_CANCELLATION_4C
```

### evidence

L&F는 Tesla향 high-nickel cathode 공급계약으로 한때 강한 Stage 2 후보처럼 보였지만, 2025년 12월 29일 Reuters는 해당 계약의 예상 가치가 29억 달러에서 7,386달러로 축소됐다고 보도했다. 이는 Tesla 4680 생산 난항, Cybertruck 부진, EV 수요 둔화와 연결된 것으로 설명됐다. ([Reuters][4])

### stage date

```text
Stage 1:
2023
- Tesla 4680 / high-nickel cathode 기대

Stage 2:
2023 Tesla supply deal
- 단, 실제 call-off / 4680 ramp / margin 확인 전 Stage 3 금지였어야 함

Stage 3:
없음
- 고객명과 계약금액 headline만으로 Green 금지

Stage 4B:
2023~2024 배터리 소재 과열 구간 후보
- exact OHLC unavailable

Stage 4C:
2025-12-29
- Tesla contract expected value $2.9B → $7,386
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters contract value anchor

stage3_price:
N/A

stock OHLC:
price_data_unavailable_after_deep_search

contract_value_initial:
$2,900,000,000

contract_value_revised:
$7,386

contract_value_drawdown:
1 - 7,386 / 2,900,000,000
= 99.999745% collapse

MFE / MAE:
stock OHLC unavailable

below_stage3_price_flag:
N/A

peak_price:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search

Stage 4C 큰 하락 이전 포착 여부:
success_by_contract_quality
- Tesla 4680 ramp와 actual call-off를 Stage 3 gate로 요구했다면 false Green 방지 가능.
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = contract_quality_failure
stage_failure_type = false_green_prevention_case
```

### 교정

L&F는 R3에서 `contract_amount` 자체보다 `actual_calloff`, `take_or_pay`, `customer_ramp`, `GWh/tonnage delivery`를 더 강하게 봐야 한다는 기준점이다.

```text
내릴 축:
customer_name_only
contract_value_headline
4680_story_without_volume

올릴 축:
binding_volume
take_or_pay
actual_calloff
revenue_recognition
margin_visibility
```

---

## Case C — 삼성SDI `success_candidate / ESS Stage 2, dilution-capex watch`

```text
symbol = 006400
case_type = success_candidate + capital_allocation_watch
archetype = ESS_LFP_GRID_STORAGE / BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE
```

### evidence

2025년 3월 5일 삼성SDI CEO는 EV 수요가 2026년 상반기까지 부진할 것으로 본다고 밝혔고, 회사는 2024년 4분기 2,570억 원 영업손실을 기록했다. 이 시점에서 EV battery Green은 막아야 한다. ([Reuters][5])

2025년 11월에는 Tesla가 삼성SDI로부터 3년간 3조 원 이상 ESS 배터리를 구매하기로 했다는 보도가 있었지만, 삼성SDI는 “아직 결정된 것이 없다”고 밝혔다. 즉 이 이벤트는 Stage 1~2 attention이지 Stage 3가 아니다. ([Reuters][6])

2025년 12월 10일에는 삼성SDI 미국 법인이 2조 원 이상 규모의 LFP ESS 공급계약을 체결했고, 배송은 2027년부터 3년간 진행될 예정이라고 발표했다. Reuters는 이 발표 후 삼성SDI 주가가 장중 최대 6.1% 상승했다고 보도했다. 이는 Stage 2로 강하지만, 기존 라인 전환·매출 인식·마진 확인 전 Stage 3는 보류해야 한다. ([Reuters][7])

또 2025년 4월 삼성SDI는 2조 원 규모 유상증자 가격을 기존 169,200원에서 146,200원으로 14% 낮췄고, 당시 주가는 연초 대비 29.5% 하락한 상태였다. 이는 CAPEX와 자금조달 부담을 R3 RedTeam에 넣어야 한다는 증거다. ([Reuters][8])

### stage date

```text
Stage 1:
2025-03-05
- EV demand sluggish until H1 2026
- Q4 operating loss

Stage 2:
2025-12-10
- U.S. LFP ESS supply deal >2조 원
- deliveries from 2027 for three years
- shares up as much as +6.1%

Stage 3:
없음
- delivery 2027 이후
- U.S. line conversion, OPM, FCF, AMPC quality 확인 필요

Stage 4B:
2025-12-10
- ESS contract 발표 당일 +6.1%는 Stage 2 event rally

Stage 4C:
2025-04-09 watch
- equity offering price cut
- YTD -29.5%
- CAPEX funding pressure
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters event returns and offer-price anchor

stage3_price:
N/A

ESS_stage2_event_MFE_1D:
+6.1%

share_sale_old_price:
169,200원

share_sale_revised_price:
146,200원

offering_price_reduction:
(146,200 / 169,200) - 1
= -13.6%

reported_YTD_drawdown_by_2025-04-09:
-29.5%

same_day_stock_return_on_2025-04-09:
-1.0%

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D:
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
score_price_alignment = success_candidate / capital_allocation_watch
rerating_result = ESS_stage2_watch
stage_failure_type = stage2_watch_success
```

### 교정

삼성SDI는 `confirmed_ESS_contract`는 올리되, `equity_issuance`, `capex_funding_pressure`, `delivery_after_2027`, `EV_demand_sluggish`를 감점한다.

---

## Case D — SK이노베이션 / SK온 `failed_rerating + restructuring relief`

```text
symbol = 096770
case_type = failed_rerating + restructuring_relief
archetype = EV_BATTERY_JV_RESTRUCTURING / LEVERAGE_FCF_BREAKDOWN
```

### evidence

2024년 7월 FT는 SK온이 분사 이후 10개 분기 연속 손실을 냈고, 순부채가 2.9조 원에서 15.6조 원으로 5배 이상 증가했다고 보도했다. CEO는 “비상경영”을 선언했고, SK그룹은 SK이노베이션과 SK E&S 합병 등 재무 보강 방안을 검토했다. ([Financial Times][9])

2024년 8월 27일 SK이노베이션 주주들은 SK E&S와의 합병을 승인했다. Reuters는 이 합병이 손실 배터리 자회사 SK온의 재무를 보강하기 위한 구조라고 설명했고, 승인 후 SK이노베이션 주가가 장중 최대 5% 상승했다고 보도했다. ([Reuters][10])

2026년 5월에는 SK이노베이션이 1분기 영업이익 2.2조 원을 기록했지만, 이는 정유 부문 회복과도 연결되어 있어 R3 배터리 Stage 3로 직접 해석하면 안 된다. ([Reuters][11])

### stage date

```text
Stage 1:
2021~2023
- SK온 글로벌 EV battery growth 기대

Stage 2:
2024-08-27
- SK Innovation / SK E&S merger approval
- restructuring relief
- shares up as much as +5%

Stage 3:
없음
- SK온은 10개 분기 연속 손실, 순부채 급증
- restructuring relief는 Green이 아님

Stage 4B:
합병 승인 이벤트로 가격 반등한 구간

Stage 4C:
2024-07-07
- SK On emergency management
- 10 consecutive quarterly losses
- net debt 2.9조 → 15.6조
```

### 실제 가격경로 검증

```text
price_data_source:
FT debt/loss anchor + Reuters merger return anchor

stage3_price:
N/A

merger_approval_event_MFE_1D:
+5%

net_debt_increase:
15.6 / 2.9 - 1
= +437.9%

loss_record:
10 consecutive quarters

MFE_30D / 90D:
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
score_price_alignment = failed_rerating_then_restructuring_relief
rerating_result = failed_EV_battery_growth_thesis
stage_failure_type = should_have_been_red_or_watch
```

### 교정

SK온은 R3에서 `negative_FCF`, `debt_burden`, `loss_making_battery_unit`, `parent_support_dependency`를 강하게 감점한다. 합병승인 +5%는 Stage 3가 아니라 restructuring relief다.

---

## Case E — SK아이이테크놀로지 `failed_rerating / separator demand-cycle break`

```text
symbol = 361610
case_type = failed_rerating / 4C-watch
archetype = SEPARATOR_EV_DEMAND_CYCLE / EV_BATTERY_JV_RESTRUCTURING
```

### evidence

2024년 5월 Reuters는 SK이노베이션이 EV 수요 약화와 SK온 재무난 때문에 분리막 자회사 SK아이이테크놀로지 매각을 검토하고 있다고 보도했다. SKIET는 EV 배터리 분리막 업체이고, Panasonic 등 EV 배터리 제조사에 공급하는 기업으로 설명됐다. 당시 SKIET 시가총액은 약 4.09조 원이었다. 같은 기사에서 SK온의 1분기 영업손실은 전 분기 186억 원에서 3,320억 원으로 확대됐고, EV 배터리 출하가 줄었다고 정리됐다. ([Reuters][12])

### stage date

```text
Stage 1:
2021~2023
- EV separator growth
- SK On / Panasonic / EV battery demand

Stage 2:
없음
- 고객 수요·가동률·OPM 개선 전 Stage 2도 약함

Stage 3:
없음
- EV 수요 둔화와 SK온 재무난으로 Green 금지

Stage 4B:
과거 EV separator overheat 구간 후보

Stage 4C:
2024-05-15
- SKIET sale consideration
- EV demand weakening
- SK On financial difficulty
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters business event anchor

stage3_price:
N/A

stock OHLC:
price_data_unavailable_after_deep_search

market_cap_anchor:
4.09조 원 as of 2024-05-14

SK_On_operating_loss_Q1_2024:
332.0 billion won

prior_quarter_loss:
18.6 billion won

loss_worsening:
332.0 / 18.6 - 1
= +1,684.9%

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
score_price_alignment = thesis_break_watch
rerating_result = separator_demand_cycle_break
stage_failure_type = should_have_been_red_or_watch
```

### 교정

SKIET는 R3에서 `separator_is_essential`이라는 논리만으로 Green을 주면 안 된다는 반례다. 가동률·고객 출하·OPM·FCF·고객 다변화가 필수다.

---

## Case F — 포스코퓨처엠 `event_premium / lithium-cycle watch`

```text
symbol = 003670
case_type = event_premium / cyclical_success
archetype = CATHODE_LONG_CONTRACT_VISIBILITY / LITHIUM_CYCLE_OVERLAY
```

### evidence

2025년 8월 CATL이 중국 Yichun lithium mine 운영을 중단하자 리튬 가격과 관련주가 급등했다. WSJ는 이 이벤트로 한국 battery-material suppliers인 POSCO Future M과 L&F가 각각 8.3%, 10% 상승했다고 보도했다. 동시에 lithium prices는 2022년 peak 이후 최대 90% 하락한 상태였고, CATL의 면허 갱신 가능성도 남아 있었다. ([월스트리트저널][13])

2025년 12월 Ford가 EV 전략을 후퇴시키자 Reuters는 LGES -6%, 삼성SDI -3.5%, POSCO Future M -8.2% 하락을 보도했다. 이건 양극재·소재주가 고객 EV 전략 후퇴에 그대로 노출되어 있음을 보여준다. ([Reuters][14])

### stage date

```text
Stage 1:
2025-08-11
- CATL lithium mine suspension
- lithium price sentiment rebound

Stage 2:
보류
- 리튬 가격 이벤트는 회사 단위 계약/마진/FCF evidence가 아님

Stage 3:
없음
- lithium price rally만으로 Green 금지

Stage 4B:
2025-08-11
- POSCO Future M +8.3%
- lithium event premium

Stage 4C:
2025-12-16
- Ford EV retreat
- POSCO Future M -8.2%
```

### 실제 가격경로 검증

```text
price_data_source:
WSJ / Reuters event return anchors

stage3_price:
N/A

CATL_lithium_event_MFE_1D:
+8.3%

Ford_EV_retreat_event_MAE_1D:
-8.2%

MFE_30D / 90D:
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
score_price_alignment = cyclical_success / event_premium
rerating_result = lithium_event_watch
stage_failure_type = should_not_be_green
```

### 교정

포스코퓨처엠은 R3에서 `commodity_price_event`와 `customer_order_quality`를 분리해야 한다.

```text
내릴 축:
lithium_price_event
inventory_valuation_gain
customer_EV_strategy_risk

올릴 축:
actual_calloff
OPM
FCF
customer_order_durability
```

---

## Case G — 에코프로머티리얼즈 `overheat / price_moved_without_evidence`

```text
symbol = 450080
case_type = overheat / insufficient_evidence
archetype = BATTERY_MATERIALS_CAPEX_OVERHEAT / PRECURSOR_SUPPLY_CHAIN
```

### evidence

2024년 6월 14일 MarketWatch는 에코프로머티리얼즈 주가가 11% 하락해 119,200원으로 떨어졌다고 보도했다. ([마켓워치][15])

2025년 12월 Ford의 EV 전략 후퇴는 국내 배터리 supply chain 전반을 압박했고, MarketWatch는 SK Innovation, LGES, SKIET, EcoPro Materials가 3~6% 하락했다고 보도했다. 특히 EcoPro Materials는 전구체/수직계열화 narrative가 강하지만, EV 수요 둔화와 고객 프로젝트 축소에 그대로 노출된다. ([마켓워치][16])

### stage date

```text
Stage 1:
2023-11 IPO / EcoPro group precursor story
- 전구체 / 수직계열화 / 배터리 소재 내재화

Stage 2:
없음 또는 보류
- 외부 고객, 가동률, OPM, FCF 확인 전

Stage 3:
없음
- IPO / 전구체 story만으로 Green 금지

Stage 4B:
IPO 이후 과열 구간 후보

Stage 4C:
2024-06-14
- 주가 -11% to 119,200원
추가 4C-watch:
2025-12-16 Ford EV retreat, battery supply chain 동반 하락
```

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch price anchor / event return

stage3_price:
N/A

2024-06-14_event_MAE_1D:
-11%

2024-06-14_close_anchor:
119,200원

implied_pre_event_reference_price:
119,200 / (1 - 0.11)
= 약 133,933원

2025-12-16_event_MAE:
about -5% per MarketWatch battery supply chain report

MFE:
N/A

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
score_price_alignment = price_moved_without_evidence / insufficient_evidence
rerating_result = theme_overheat
stage_failure_type = should_have_been_watch_or_red
```

### 교정

에코프로머티리얼즈는 R3에서 `vertical_integration_story`, `precursor_theme`, `IPO_premium`을 Stage 3로 올리면 안 되는 반례다.

---

# 5. 이번 R3 case별 요약표

| case        | 분류                              |                                                                  실제 가격검증 | alignment                        |
| ----------- | ------------------------------- | -----------------------------------------------------------------------: | -------------------------------- |
| LG에너지솔루션    | success_candidate + 4C          | Q2 event -1.6%; Ford cancellation -7.6%; 기대매출 13.5조 손실, 2024 매출 대비 52.7% | thesis_break_watch               |
| L&F         | hard 4C                         |                                   Tesla 계약가치 $2.9B → $7,386, -99.999745% | thesis_break                     |
| 삼성SDI       | success_candidate + capex watch |                                     ESS 계약 +6.1%; 유증가 -13.6%, YTD -29.5% | stage2_watch                     |
| SK이노베이션/SK온 | failed_rerating                 |                                        합병승인 +5%; 순부채 +437.9%, 10분기 연속 손실 | failed_rerating                  |
| SKIET       | failed_rerating / 4C-watch      |                               SK온 손실 18.6B → 332B, +1,684.9%; SKIET 매각검토 | thesis_break_watch               |
| 포스코퓨처엠      | event_premium / cyclical        |                                       CATL event +8.3%; Ford shock -8.2% | cyclical_success / event_premium |
| 에코프로머티리얼즈   | overheat                        |                                 -11% to 119,200원; implied prior 133,933원 | price_moved_without_evidence     |

---

# 6. score-price alignment 판정

```text
thesis_break:
- L&F
- LGES contract cancellation leg

thesis_break_watch:
- SKIET
- LGES
- SK Innovation / SK On

stage2_watch_success:
- Samsung SDI ESS LFP contract
- LGES ESS LFP contract

event_premium / cyclical_success:
- POSCO Future M lithium event
- L&F lithium event

price_moved_without_evidence:
- EcoPro Materials precursor / IPO / vertical integration theme
```

---

# 7. 점수비중 교정

## 올릴 축

```text
binding_contract_quality +5
actual_calloff +5
GWh_or_tonnage_volume +5
utilization_rate +5
OPM_visibility +5
FCF_after_capex +5
ESS_revenue_conversion +4
customer_quality +4
subsidy_quality_adjustment +4
```

### 이유

삼성SDI의 2조 원 이상 ESS 계약은 주가를 +6.1% 밀었고, LGES의 43억 달러 LFP ESS 계약도 Stage 2로는 강하다. 하지만 배송 시작이 2027년 이후이고, 라인 전환·마진·FCF가 아직 확인되지 않아 Stage 3는 보류해야 한다. ([Reuters][7])

## 내릴 축

```text
ev_theme_only -5
ess_theme_only -4
customer_name_only -5
contract_value_headline_without_calloff -5
capa_announcement -4
subsidy_dependent_profit -5
negative_fcf_or_debt_burden -5
ipo_or_vertical_integration_story -4
lithium_price_event -4
```

### 이유

LGES는 2분기 이익이 좋아 보였지만 AMPC 제외 영업이익이 14억 원에 불과했고, 주가는 발표 후 하락했다. L&F는 Tesla 계약이라는 강한 headline이 있었지만 계약가치가 사실상 사라졌다. SK온은 10개 분기 연속 손실과 순부채 급증을 겪었다. ([Reuters][1])

## Green gate 강화 조건

```text
R3 Stage 3-Green 필수:
1. binding contract
2. actual call-off
3. GWh / tonnage volume
4. utilization improvement
5. OPM or gross margin improvement
6. FCF after capex
7. AMPC / subsidy 제외 이익 품질 확인
8. customer EV strategy risk 통과
9. price path follows evidence

금지:
고객명만 있음
계약금액 headline만 있음
ESS/LFP 테마만 있음
CAPA 전환만 있음
AMPC 제외 적자
EV 수요 둔화 무시
```

## 4B 조기감지 조건

```text
4B-watch:
battery supply-chain이 lithium price event로 동반 급등
ESS/LFP 계약 발표만으로 주가 급등
배터리 소재주가 call-off 없이 valuation만 확장
IPO/수직계열화 narrative로 주가가 먼저 감
AMPC 포함 이익으로만 실적 서프라이즈

4B-elevated:
EV 수요 둔화에도 valuation 유지
고객 주문 확인 없이 CAPA 전환 기대만 반영
리튬 가격 반등이 재고평가 이익으로만 연결
```

## 4C hard gate 조건

```text
contract cancellation
contract value collapse
customer EV model cancellation
customer strategy pullback
take-or-pay absence confirmed
GWh call-off failure
utilization delay
negative FCF
debt burden / emergency management
subsidy-quality profit collapse
share issuance / dilution under weak demand
```

L&F는 `contract_value_collapse_hard_4C`, LGES는 `customer_strategy_contract_loss_4C`, SK온은 `leverage_FCF_breakdown_4C_watch`, SKIET는 `separator_demand_cycle_break_watch`로 기록한다.

---

# 8. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
```

이번 세션에서 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉을 안정적으로 직접 확보하지 못했다. 대신 Reuters / WSJ / FT / MarketWatch의 가격 anchor와 이벤트 수익률을 사용해 계산 가능한 부분은 직접 계산했다.

---

# 9. patch-ready 출력

## docs/round/round_135.md 요약

```md
# R3 Loop 8. Battery / EV / Green Price Validation

이번 라운드는 R3 price-validation 라운드다.

핵심 결론:
- R3는 현재 Stage 3-Green 발굴보다 false Green 차단이 더 중요하다.
- LGES는 43억 달러 LFP ESS 계약으로 Stage 2 후보지만, Ford/Freudenberg 계약 종료로 약 13.5조 원 기대매출 손실이 발생해 4C-watch가 강하다.
- L&F는 Tesla 계약가치가 $2.9B에서 $7,386로 축소되어 contract-value hard 4C 기준점이다.
- Samsung SDI는 2조 원 이상 ESS LFP 계약으로 Stage 2 후보지만, EV 수요 부진과 유상증자 부담 때문에 Stage 3는 보류다.
- SK Innovation/SK On은 10분기 연속 손실과 순부채 급증으로 failed rerating / restructuring relief다.
- POSCO Future M은 lithium event +8.3%, Ford shock -8.2%로 commodity/event 민감도가 크다.
- EcoPro Materials는 IPO/precursor story만으로 Green 금지다.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 135 R3 Loop 8 Battery EV Green Price Validation

## 반영 내용
- R3 Loop 8 price-validation 라운드를 추가했다.
- ESS LFP pivot, battery contract cancellation, cathode contract value collapse, SK On restructuring, lithium event premium을 비교했다.
- Reuters/WSJ/FT/MarketWatch reported price anchors로 가능한 MFE/MAE를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- binding contract quality, actual call-off, utilization, OPM/FCF 가중치 강화
- customer-name-only, contract headline, subsidy-dependent profit, lithium event 감점 강화
- contract cancellation / contract value collapse hard 4C 강화
```

## case row 초안

```jsonl
{"case_id":"r3_loop8_lges_ess_pivot_contract_break","symbol":"373220","company_name":"LG에너지솔루션","case_type":"success_candidate","primary_archetype":"ESS_LFP_GRID_STORAGE","stage2_date":"2025-07-30","stage4c_date":"2025-12-18","price_validation":{"price_data_source":"Reuters reported anchors","stage3_price":null,"q2_event_mae":-1.6,"ford_cancellation_mae_1d":-7.6,"lost_expected_revenue_krw_trn":13.5,"lost_revenue_vs_2024_revenue_pct":52.7,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"ESS_success_candidate_but_EV_contract_break","notes":"ESS LFP contract is Stage 2; Ford/Freudenberg cancellations trigger 4C-watch."}
{"case_id":"r3_loop8_lnf_tesla_contract_collapse","symbol":"066970","company_name":"L&F","case_type":"4c_thesis_break","primary_archetype":"BATTERY_CONTRACT_CANCELLATION_4C","stage4c_date":"2025-12-29","price_validation":{"price_data_source":"Reuters contract value anchor","stage3_price":null,"contract_value_initial_usd":2900000000,"contract_value_revised_usd":7386,"contract_value_drawdown_pct":-99.999745,"price_validation_status":"contract_value_anchor_stock_ohlc_unavailable"},"score_price_alignment":"thesis_break","rerating_result":"contract_quality_failure","notes":"Tesla customer name and supply deal headline were insufficient without actual call-off and 4680 ramp."}
{"case_id":"r3_loop8_samsung_sdi_ess_lfp_stage2","symbol":"006400","company_name":"삼성SDI","case_type":"success_candidate","primary_archetype":"ESS_LFP_GRID_STORAGE","stage2_date":"2025-12-10","price_validation":{"price_data_source":"Reuters reported anchors","stage3_price":null,"ess_event_mfe_1d":6.1,"offering_price_reduction_pct":-13.6,"reported_ytd_drawdown_pct":-29.5,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate","rerating_result":"ESS_stage2_watch","notes":"ESS contract is Stage 2; delivery, OPM, FCF and dilution/capex burden must be checked before Green."}
{"case_id":"r3_loop8_sk_innovation_skon_failed_rerating","symbol":"096770","company_name":"SK이노베이션/SK온","case_type":"failed_rerating","primary_archetype":"EV_BATTERY_JV_RESTRUCTURING","stage4c_date":"2024-07-07","price_validation":{"price_data_source":"FT/Reuters reported anchors","stage3_price":null,"merger_event_mfe_1d":5.0,"net_debt_increase_pct":437.9,"loss_record":"10 consecutive quarters","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"failed_rerating_then_restructuring_relief","rerating_result":"failed_EV_battery_growth_thesis","notes":"SK On emergency management and debt burden block Green; SK E&S merger is restructuring relief."}
{"case_id":"r3_loop8_skiet_separator_demand_break","symbol":"361610","company_name":"SK아이이테크놀로지","case_type":"4c_watch","primary_archetype":"SEPARATOR_EV_DEMAND_CYCLE","stage4c_date":"2024-05-15","price_validation":{"price_data_source":"Reuters business event anchor","stage3_price":null,"market_cap_anchor_krw_trn":4.09,"sk_on_loss_worsening_pct":1684.9,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"separator_demand_cycle_break","notes":"Separator essentiality is not enough; utilization, customer demand, OPM and FCF required."}
{"case_id":"r3_loop8_posco_future_m_lithium_event","symbol":"003670","company_name":"포스코퓨처엠","case_type":"event_premium","primary_archetype":"LITHIUM_CYCLE_OVERLAY","stage1_date":"2025-08-11","stage4c_date":"2025-12-16","price_validation":{"price_data_source":"WSJ/Reuters reported anchors","stage3_price":null,"catl_lithium_event_mfe_1d":8.3,"ford_ev_retreat_mae_1d":-8.2,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"cyclical_success","rerating_result":"lithium_event_watch","notes":"Lithium price event is not Stage 3; customer order quality and OPM/FCF needed."}
{"case_id":"r3_loop8_ecopro_materials_precursor_overheat","symbol":"450080","company_name":"에코프로머티리얼즈","case_type":"overheat","primary_archetype":"BATTERY_MATERIALS_CAPEX_OVERHEAT","stage4c_date":"2024-06-14","price_validation":{"price_data_source":"MarketWatch reported price anchor","stage3_price":null,"mae_1d":-11.0,"close_anchor":119200,"implied_pre_event_reference_price":133933,"ford_supply_chain_mae_1d":-5.0,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"theme_overheat","notes":"IPO/precursor/vertical integration story is insufficient without external customers, utilization, OPM and FCF."}
```

## shadow weight row 초안

```csv
archetype,binding_contract,actual_calloff,gwh_volume,utilization,opm_fcf,subsidy_quality,event_penalty,hard_4c_sensitivity,notes
ESS_LFP_GRID_STORAGE,+4,+4,+4,+4,+5,+4,-1,+3,LGES and Samsung SDI ESS contracts are Stage 2; Stage 3 requires delivery, utilization and OPM/FCF.
BATTERY_CONTRACT_CANCELLATION_4C,+5,+5,+5,+3,+4,+2,0,+5,L&F and LGES show contract cancellation/value collapse as hard 4C.
EV_BATTERY_JV_RESTRUCTURING,+2,+3,+3,+4,+5,+3,-1,+5,SK On losses and debt show failed rerating and restructuring relief.
SEPARATOR_EV_DEMAND_CYCLE,+3,+4,+3,+5,+5,+2,-2,+4,SKIET sale consideration shows separator demand cycle break.
LITHIUM_CYCLE_OVERLAY,+1,+1,+1,+1,+2,0,-5,+3,POSCO Future M lithium-event move is cyclical/event premium, not Green.
BATTERY_MATERIALS_CAPEX_OVERHEAT,+2,+3,+3,+4,+5,+2,-4,+4,EcoPro Materials precursor story needs external customers/utilization/OPM before Green.
```

---

# 이번 R3 Loop 8 결론

R3의 방향은 명확하다. **ESS 전환은 Stage 2 후보가 될 수 있지만, R3 Stage 3-Green은 매우 늦게 줘야 한다.**

```text
1. LGES와 Samsung SDI는 ESS LFP pivot으로 Stage 2 후보가 될 수 있다.
   하지만 배송, utilization, OPM, FCF 확인 전에는 Stage 3 금지다.

2. LGES와 L&F는 contract-quality hard 4C의 기준점이다.
   계약 취소, 계약가치 붕괴, 고객 EV 전략 후퇴는 가장 강한 RedTeam이다.

3. SK On / SK Innovation은 EV battery 성장 thesis가 실패하면 parent restructuring relief로만 봐야 한다.
   순부채 +437.9%, 10분기 연속 손실은 Green을 막는다.

4. SKIET는 분리막이 필수소재라도 고객 수요·가동률·OPM이 없으면 Green이 아니다.

5. POSCO Future M은 lithium event로 +8.3% 오르고 Ford shock에 -8.2% 빠졌다.
   이는 commodity/event 민감도이지 구조적 Stage 3가 아니다.

6. EcoPro Materials는 precursor / vertical integration / IPO premium만으로 Stage 3 금지다.
```

한 문장으로 압축하면:

> **R3에서 진짜 Stage 3는 “배터리·ESS 수혜”가 아니라, 계약이 실제 GWh·call-off·가동률·OPM·FCF로 내려오고, 보조금 제외 이익과 고객 주문 지속성이 확인되는 순간이다.**
> **현재 R3는 Green 발굴보다 contract-quality 4C와 false Green 차단이 훨씬 중요하다.**

[1]: https://www.reuters.com/business/autos-transportation/lg-energy-solution-warns-slowing-ev-battery-demand-due-us-tariffs-policy-2025-07-25/?utm_source=chatgpt.com "LG Energy Solution warns of slowing EV battery demand due to U.S. tariffs, policy headwinds"
[2]: https://www.reuters.com/business/energy/lg-energy-solution-tesla-sign-43-billion-battery-supply-deal-source-says-2025-07-30/?utm_source=chatgpt.com "LG Energy Solution, Tesla sign $4.3 billion battery supply deal, source says"
[3]: https://www.reuters.com/business/energy/shares-south-koreas-lges-drop-more-than-7-after-ford-cancels-ev-battery-deal-2025-12-18/?utm_source=chatgpt.com "Shares in South Korea's LGES drop more than 7% after Ford cancels EV battery deal"
[4]: https://www.reuters.com/world/asia-pacific/south-koreas-lf-says-value-battery-material-supply-deal-with-tesla-cut-7386-2025-12-29/?utm_source=chatgpt.com "South Korea's L&F slashes value of battery material supply deal with Tesla"
[5]: https://www.reuters.com/business/autos-transportation/samsung-sdi-ceo-says-ev-demand-remain-sluggish-until-h1-2026-2025-03-05/?utm_source=chatgpt.com "Samsung SDI CEO says EV demand to remain sluggish until H1 of 2026"
[6]: https://www.reuters.com/business/autos-transportation/tesla-buy-2-bln-ess-batteries-samsung-sdi-over-3-years-newspaper-says-2025-11-03/?utm_source=chatgpt.com "Tesla to buy $2 bln of ESS batteries from Samsung SDI over 3 years, newspaper says"
[7]: https://www.reuters.com/world/asia-pacific/samsung-sdis-us-unit-signs-14-bln-lfp-battery-deal-us-customer-2025-12-09/?utm_source=chatgpt.com "Samsung SDI unit signs US battery deal worth over $1.36 bln for energy storage systems"
[8]: https://www.reuters.com/markets/asia/samsung-sdi-cuts-stock-offering-price-by-14-2025-04-09/?utm_source=chatgpt.com "Samsung SDI cuts pricing of $1.4 billion share-sale as global markets tumble"
[9]: https://www.ft.com/content/5affede6-1f1d-458e-b4d0-e2e7e902dcca?utm_source=chatgpt.com "Battery maker SK On declares 'emergency' as EV sales disappoint"
[10]: https://www.reuters.com/markets/deals/sk-innovation-shareholders-approve-merger-plan-with-sk-es-yonhap-reports-2024-08-27/?utm_source=chatgpt.com "SK Innovation shareholders approve merger seen shoring up loss-making battery unit"
[11]: https://www.reuters.com/world/asia-pacific/sk-innovation-warns-refining-recovery-take-time-beats-q1-profit-estimates-2026-05-13/?utm_source=chatgpt.com "SK Innovation warns refining recovery to take time, beats Q1 profit estimates"
[12]: https://www.reuters.com/technology/sk-innovation-considering-sale-battery-materials-unit-skiet-paper-reports-2024-05-15/?utm_source=chatgpt.com "SK Innovation considering sale of battery materials unit SKIET, paper reports"
[13]: https://www.wsj.com/finance/commodities-futures/ev-battery-giant-catl-suspends-mining-project-67693725?utm_source=chatgpt.com "EV Battery Giant CATL Suspends Mining Project"
[14]: https://www.reuters.com/world/asia-pacific/shares-lg-energy-solution-fall-6-after-ford-retreats-ev-push-2025-12-16/?utm_source=chatgpt.com "Shares of LG Energy Solution fall 6% after Ford retreats from EV push"
[15]: https://www.marketwatch.com/story/ecopro-materials-shares-fall-11-to-krw119-200-103f38d7?utm_source=chatgpt.com "Ecopro Materials Shares Fall 11% to KRW119,200"
[16]: https://www.marketwatch.com/story/while-ford-shares-are-remarkably-steady-after-20-billion-charge-these-stocks-are-getting-battered-bbbcfa04?utm_source=chatgpt.com "While Ford shares are remarkably steady after $20 billion charge, these stocks are getting battered"

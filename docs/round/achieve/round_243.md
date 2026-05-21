순서상 이번은 **R13 Loop 10 — Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리**다.

이번 R13은 새 섹터 발굴이 아니라, **R1~R12 Loop 10에서 나온 후보를 다시 부수는 라운드**다. 핵심은 세 가지다. 첫째, Stage 3가 실제 대형 MFE를 만들었는가. 둘째, 4B가 가격 선반영·crowding·event premium을 너무 늦지 않게 잡았는가. 셋째, 4C가 계약·안전·보안·정책·운영 신뢰 붕괴를 제대로 차단했는가.

```text
round = R13 Loop 10
round_id = round_171
large_sector = CROSS_ARCHETYPE_REDTEAM_PRICE_VALIDATION
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true
```

이번에도 full adjusted OHLC 전체 구간은 안정적으로 확보하지 못했다. 대신 Reuters / FT / MarketWatch / Vogue Business / Business Insider / AP가 제공한 **공개 가격 anchor, event return, contract value, market-cap, policy-shock, loss/cost 지표**로 계산 가능한 값만 계산했다. 원시 일봉 OHLC가 없는 항목은 `price_data_unavailable_after_deep_search`로 명시한다.

---

# 1. 이번 라운드 대섹터

```text
R13 = Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리
```

R13의 질문은 단순하다.

```text
이 후보가 진짜 돈을 벌었나?
아니면 뉴스가 먼저 가격을 끌고 갔나?
그리고 깨질 때는 어떤 gate가 먼저 깨졌나?
```

---

# 2. 대상 canonical archetype

```text
STRUCTURAL_SUCCESS_ALIGNED
STRUCTURAL_SUCCESS_BUT_4B_WATCH
CROWDED_RERATING_4B_WATCH
AI_CAPITAL_ALLOCATION_EVENT_PREMIUM
POLICY_CAPEX_FALSE_POSITIVE
CONTRACT_QUALITY_HARD_4C
OPERATIONAL_SAFETY_HARD_4C
MACRO_GEOPOLITICAL_HARD_4C
DIGITAL_ASSET_POLICY_OVERHEAT
PRICE_MOVED_WITHOUT_EVIDENCE
EVIDENCE_GOOD_BUT_PRICE_FAILED
```

---

# 3. deep sub-archetype

```text
성공 검증:
- SK Hynix HBM / HBM4 / EUV / AI memory
- APR / Medicube K-beauty device + global sell-through

4B 검증:
- SK Hynix trillion-dollar proximity
- APR fourfold rally / single-brand concentration
- Samsung SDS KKR / AI capital-allocation event
- stablecoin policy basket 2~3배 rally

false positive 방지:
- Hyundai Steel U.S. steel capex / tariff hedge
- policy capex without funding / margin / FCF

hard 4C:
- L&F Tesla cathode contract collapse
- Jeju Air fatal safety accident
- Hormuz / Iran macro energy shock

price-only:
- KRW stablecoin basket
- AI / digital asset / policy theme before regulated revenue
```

---

# 4. 국장 신규 후보 case

## Case A — SK하이닉스 `structural_success_aligned + 4B-watch`

```text
symbol = 000660
source_sector = R2
case_type = structural_success + 4B-watch
archetype = STRUCTURAL_SUCCESS_ALIGNED / STRUCTURAL_SUCCESS_BUT_4B_WATCH
```

SK하이닉스는 R13의 Stage 3 성공 benchmark다. 2024년 6월 Nomura가 HBM 지배력과 메모리 가격 상승을 이유로 2024년·2025년 영업이익 전망을 크게 올렸고, 당시 SK하이닉스 주가 anchor는 222,000원이었다. 이후 2026년 5월에는 미국 빅테크의 AI capex 확대 신호로 SK하이닉스가 1,447,000원 record high를 기록했고, 며칠 뒤 Reuters는 SK하이닉스가 2025년 +274%, 2026년 +200% 이상 상승해 시총 약 9,420억 달러에 도달했다고 보도했다. ([마켓워치][1])

### stage date

```text
Stage 1:
2024년 상반기
- AI server / HBM demand
- old commodity memory frame break

Stage 2:
2024-06-25
- HBM dominance
- DRAM price upcycle
- EPS revision
- stage3 candidate anchor = 222,000원

Stage 3:
2024-06-25 후보
- HBM 지배력 + EPS revision + 가격경로 반응

Stage 4B:
2026-05-04
- 1,447,000원 record high
- AI capex / memory shortage / 외국인 수급

Stage 4B-elevated:
2026-05-14
- 2025년 +274%
- 2026년 +200% 이상
- market cap 약 $942B
- 1조 달러 근접

Stage 4C:
아직 thesis break 없음
- 단, AI capex slowdown / HBM supply normalization / Samsung strike reversal / memory price reversal 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch / Reuters reported price and return anchors

entry_date:
2024-06-25

stage3_price:
222,000원

reported_peak_price:
1,447,000원

MFE_from_stage3_to_reported_peak:
(1,447,000 / 222,000) - 1
= +551.8%

reported_return_2025:
+274%

reported_return_2026_to_2026-05-14:
> +200%

minimum_compounded_return_from_start_2025_to_2026-05-14:
(1 + 2.74) * (1 + 2.00) - 1
= +1,022% 이상

market_cap_path:
< $100B → 약 $942B

minimum_market_cap_MFE:
(942 / 100) - 1
= +842% 이상

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
price_data_unavailable_after_deep_search
```

### R13 판정

```text
score_price_alignment = aligned
rerating_result = true_rerating
4B_status = 4B-watch / 4B-elevated
```

SK하이닉스는 **Stage 3가 실제 대형 MFE를 만들 수 있음을 증명한 case**다. 하지만 지금은 신규 Stage 3가 아니라, 이미 대시세가 진행된 **4B-watch / crowding watch**다.

---

## Case B — APR / Medicube `structural_success_aligned + 4B-watch`

```text
symbol = 278470
source_sector = R5
case_type = structural_success + 4B-watch
archetype = K_BEAUTY_DEVICE_GLOBAL_BRAND / STRUCTURAL_SUCCESS_BUT_4B_WATCH
```

APR/Medicube는 R5에서 “viral이 매출로 내려온” 구조 후보다. Vogue Business는 APR의 2025년 4분기 매출이 약 4.4억 달러로 전년 대비 124% 증가했고, 해외 매출은 약 3.62억 달러로 203% 증가했다고 보도했다. FY 2025 매출은 약 12억 달러, Medicube 매출은 약 11억 달러로 전체의 91.7% 수준이다. Business Insider는 APR 주가가 IPO 이후 75% 이상 올라 158,300원에 거래됐고 시총이 약 42억 달러라고 보도했다. ([Vogue][2])

### stage date

```text
Stage 1:
2024 IPO / 2025 K-beauty device virality
- Medicube beauty device
- TikTok / Amazon / Ulta / creator-affiliate distribution

Stage 2:
2025-07-08
- APR stock 158,300원
- IPO 이후 +75% 이상
- market cap 약 $4.2B

Stage 3:
2025 Q4 후보
- Q4 revenue 약 $440M, +124% YoY
- overseas revenue 약 $362M, +203% YoY
- FY revenue 약 $1.2B
- Medicube revenue 약 $1.1B
- Ulta 1,400+ store expansion
- TikTok Shop revenue $102.9M+

Stage 4B:
2025~2026
- 이미 IPO 이후 큰 상승
- Medicube 매출 집중도 91.7%
- device / single-brand concentration

Stage 4C:
미국 sell-through 둔화, device trend fade, inventory build, tariff/margin squeeze 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Vogue Business / Business Insider anchors

stage2_price:
158,300원

IPO_to_stage2_MFE_minimum:
> +75%

implied_IPO_reference_price_from_75pct_gain:
158,300 / 1.75
= 약 90,457원 이하

market_cap_July_2025:
$4.2B

Q4_2025_revenue:
$440M

Q4_2025_revenue_growth:
+124% YoY

Q4_2025_overseas_revenue:
$362M

Q4_2025_overseas_growth:
+203% YoY

FY_2025_revenue:
$1.2B

Medicube_FY_2025_revenue:
$1.1B

Medicube_share_of_APR_revenue:
1.1 / 1.2
= 91.7%

TikTok_Shop_revenue:
$102.9M+

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D:
price_data_unavailable_after_deep_search
```

### R13 판정

```text
score_price_alignment = aligned
rerating_result = K_beauty_device_true_rerating_plus_4B_watch
stage_failure_type = green_success_candidate
```

APR은 **R5 Stage 3 후보 성공 case**다. 하지만 single-brand/device concentration 때문에 4B-watch가 반드시 붙어야 한다.

---

## Case C — 삼성SDS `4B-watch / AI capital allocation event`

```text
symbol = 018260
source_sector = R8 / R6
case_type = success_candidate + event_premium
archetype = AI_CAPITAL_ALLOCATION_EVENT_PREMIUM
```

KKR은 삼성SDS 신규 전환사채 8.2억 달러를 인수하기로 했고, 삼성SDS 주가는 장중 최대 20.8% 급등했다. 회사는 기존 현금 6.4조 원과 KKR 자금을 활용해 AI infrastructure, physical AI, stablecoin 등 신사업과 M&A를 추진하겠다고 밝혔다. 이것은 좋은 Stage 2지만, recurring AI revenue 전에는 Green이 아니라 4B-watch다. ([Reuters][3])

### stage date

```text
Stage 1:
2025~2026
- enterprise AI transformation
- Samsung group AI infra / IT services 기대

Stage 2:
2026-04-15
- KKR $820M convertible bond investment
- AI infra / M&A / capital allocation 기대

Stage 3:
없음
- recurring AI revenue, cloud revenue, AI transformation margin, FCF 확인 전 Green 금지

Stage 4B:
2026-04-15
- 장중 +20.8%
- KOSPI 대비 강한 아웃퍼폼
- AI revenue보다 가격이 먼저 움직임

Stage 4C:
CB dilution, AI capex 대비 매출 부진, M&A 실패, stablecoin regulatory risk
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported event-return anchor

stage3_price:
N/A

stage2_event_MFE_1D:
+20.8%

morning_trade_return:
+19.4%

KOSPI_same_context_return:
+3.0%

relative_intraday_outperformance_vs_KOSPI:
20.8 - 3.0
= +17.8pp

CB_investment:
$820M

KRW_equivalent_at_Reuters_FX_approx:
820M * 1,472
= 약 1.207T won

Samsung_SDS_existing_cash:
6.4T won

combined_cash_plus_CB:
6.4T + 1.207T
= 약 7.607T won

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### R13 판정

```text
score_price_alignment = event_premium + success_candidate
rerating_result = AI_cloud_capital_allocation_watch
stage_failure_type = should_not_be_green_yet
```

삼성SDS는 **Stage 2 + 4B 성공감지 case**다. “좋은 뉴스”와 “Green”을 분리해야 한다.

---

## Case D — 현대제철 `false_positive_score_prevention / policy capex failure`

```text
symbol = 004020
source_sector = R4 / R11
case_type = failed_rerating / false_positive_score_prevention
archetype = POLICY_CAPEX_FALSE_POSITIVE
```

현대제철은 정책·관세 대응 CAPEX를 Green으로 주면 안 되는 대표 사례다. 회사는 미국 Louisiana에 58억~60억 달러 규모 steel plant를 짓겠다고 발표했고, 발표 당일 처음에는 주가가 5% 넘게 올랐지만 결국 -4.4%로 뒤집혔다. 이후 자금조달·전략 불확실성이 커지면서 발표 후 주가가 21.2% 하락했고, POSCO Holdings와 KOSPI보다 더 부진했다. 별도 Nomura 코멘트에서는 2024년 순이익 추정치가 73% 낮아지고 철근 가격이 10% 하락할 수 있다는 약한 수요도 확인됐다. ([Reuters][4])

### stage date

```text
Stage 1:
2024~2025
- U.S. tariff pressure
- steel localization / U.S. plant narrative
- weak domestic construction demand

Stage 2:
2025-03-25
- $5.8B Louisiana plant
- annual capacity 2.7M tonnes
- initial +5% then -4.4%

Stage 3:
없음
- funding, tariff benefit, plant utilization, margin, FCF 확인 전 Green 금지

Stage 4B:
2025-03-25
- 정책 CAPEX headline에 초반 가격 반응

Stage 4C-watch:
2025-04-22
- funding uncertainty
- stock -21.2% after announcement
- weak domestic demand / Chinese imports / labor disputes
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters / MarketWatch capex and weak-demand anchors

stage3_price:
N/A

U.S._plant_investment:
$5.8B~$6.0B

U.S._plant_capacity:
2.7M tonnes/year

announcement_session_initial_MFE:
> +5%

announcement_session_MAE:
-4.4%

post_announcement_drawdown:
-21.2%

POSCO_Holdings_same_period:
-18.3%

benchmark_same_period:
-5.5%

relative_underperformance_vs_benchmark:
-21.2 - (-5.5)
= -15.7pp

funding_plan:
50% borrowing, rest unclear / possible POSCO equity

2024_net_profit_forecast:
215B won

net_profit_forecast_cut:
-73%

implied_prior_net_profit_forecast:
215B / (1 - 0.73)
= 약 796.3B won

rebar_price_expected_decline:
-10%

weak_demand_event_price:
29,000원

weak_demand_event_MAE:
-1.2%

MFE / MAE_30D:
price_data_unavailable_after_deep_search
```

### R13 판정

```text
score_price_alignment = false_positive_score_prevention
rerating_result = policy_capex_without_funding_failed
stage_failure_type = 4C_watch
```

현대제철은 **정책·관세 대응 CAPEX를 Green으로 착각하지 말라는 반례**다.

---

## Case E — L&F `hard 4C / contract quality break`

```text
symbol = 066970
source_sector = R3 / R4
case_type = 4C-thesis-break
archetype = CONTRACT_QUALITY_HARD_4C
```

L&F는 고객명과 계약금액 headline만으로 Green을 주면 안 된다는 hard 4C 기준점이다. Tesla향 high-nickel cathode 공급계약 가치는 29억 달러에서 7,386달러로 사실상 붕괴했다. Reuters는 Tesla 4680 생산 문제, EV demand slowdown, Cybertruck 수요 부진 등이 배경이라고 설명했다. ([Reuters][5])

### stage date

```text
Stage 1:
2023
- Tesla 4680 high-nickel cathode supply deal
- customer-name / EV material growth narrative

Stage 2:
약함
- 고객명과 계약금액 headline은 있었음

Stage 3:
없음
- actual call-off, volume, margin, FCF 확인 전 Green 금지

Stage 4C:
2025-12-29
- contract value $2.9B → $7,386
- 4680 yield issue / EV demand slowdown / Cybertruck demand disappointment
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters contract-value collapse anchor

stage3_price:
N/A

initial_contract_value:
$2.9B

revised_contract_value:
$7,386

contract_value_drawdown:
1 - 7,386 / 2,900,000,000
= 99.999745% collapse

contract_period:
2024~2025

product:
high-nickel cathode materials for Tesla 4680 cells

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### R13 판정

```text
score_price_alignment = thesis_break
rerating_result = battery_material_contract_quality_failure
stage_failure_type = hard_4C
```

L&F는 **R3/R4의 contract-quality hard 4C 기준점**이다.

---

## Case F — 제주항공 `hard 4C / operational safety trust break`

```text
symbol = 089590
source_sector = R9
case_type = 4C-thesis-break
archetype = OPERATIONAL_SAFETY_HARD_4C
```

제주항공은 R9뿐 아니라 R13 전체에서 가장 명확한 operational hard 4C다. Muan 사고로 179명이 사망했고, Jeju Air 주가는 장중 최대 15.7% 하락해 6,920원까지 떨어졌다. 이 하락으로 최대 957억 원의 시가총액이 사라졌고, 이후 정부는 항공운항 시스템 전반의 안전점검을 지시했다. ([Reuters][6])

### stage date

```text
Stage 1:
2023~2024
- LCC travel recovery
- Japan / Southeast Asia leisure demand

Stage 2:
없음

Stage 3:
없음

Stage 4C:
2024-12-30
- fatal crash
- 179 fatalities
- Jeju Air intraday -15.7%
- event low 6,920원
- market cap wipeout up to 95.7B won
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters crash / price / safety-probe anchors

stage3_price:
N/A

Jeju_Air_event_MAE_1D:
-15.7%

event_low_price:
6,920원

implied_pre_event_reference_price:
6,920 / (1 - 0.157)
= 약 8,209원

market_cap_wipeout:
95.7B won

fatalities:
179

AK_Holdings_MAE:
-12%

Boeing_related_headline_risk:
Boeing shares about -2% in related Reuters safety-probe article

MFE:
N/A

below_stage3_price_flag:
N/A

Stage 4C 큰 하락 이전 포착 여부:
event itself
- fatal accident 발생 즉시 hard 4C gate.
```

### R13 판정

```text
score_price_alignment = thesis_break
rerating_result = operational_safety_trust_break
stage_failure_type = hard_4C
```

제주항공은 **수요 회복 논리보다 safety trust가 먼저라는 hard gate**다.

---

## Case G — Hormuz / Iran shock `macro hard 4C`

```text
symbol = KOSPI / KRW / exporters / refiners / airlines / autos / chips
source_sector = R11
case_type = macro hard 4C
archetype = MACRO_GEOPOLITICAL_HARD_4C
```

Hormuz / Iran shock은 R11의 macro hard 4C다. Reuters는 Iran war와 Hormuz disruption이 글로벌 원유 공급·기업 비용·운송비·원자재 비용을 압박하고 있다고 보도했다. IEA는 2026년 global oil supply가 demand를 크게 밑돌 수 있다고 봤고, 별도 Reuters 분석은 전쟁이 글로벌 기업들에 최소 250억 달러 비용을 안기고 있다고 정리했다. 한국은 에너지 수입 의존도가 높기 때문에 이런 shock은 개별 기업 이슈를 넘어 KOSPI/KRW macro gate로 작동한다. ([Reuters][7])

### stage date

```text
Stage 1:
2026-03~05
- Iran war / Hormuz blockade
- oil / LNG / shipping / raw-material cost shock
- South Korea energy-security vulnerability

Stage 2:
없음
- 지정학 shock은 positive stage가 아니라 RedTeam input

Stage 3:
없음

Stage 4C:
2026-03~05
- energy chokepoint disruption
- global oil supply shortfall
- shipping / raw-material / airline cost shock
- Korean exporter / airline / refiner / chip basket risk
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters geopolitical energy-shock / IEA / corporate-cost anchors

stage3_price:
N/A

global_company_cost_from_Iran_war:
at least $25B and counting

oil_price_context:
above $100/bbl in Reuters corporate-cost report

IEA_supply_shortfall_2026:
1.78M bpd through 2026

IEA_Q2_deficit:
6M bpd expected

global_supply_decline_expected:
3.9M bpd

shut_in_oil_context:
over 14M bpd currently shut in, per Reuters/IEA summary

Korea_specific_equity_OHLC:
price_data_unavailable_after_deep_search in this pass

Stage 4C 큰 하락 이전 포착 여부:
hard macro event
- Hormuz closure / oil supply shock itself is the trigger.
```

### R13 판정

```text
score_price_alignment = thesis_break
rerating_result = geopolitical_energy_security_hard_4C
stage_failure_type = macro_hard_4C
```

Hormuz는 **R11뿐 아니라 R1~R12 전체를 덮는 macro 4C overlay**다.

---

## Case H — KRW stablecoin basket `price_moved_without_evidence`

```text
symbols = 377300 / LG CNS / Aton / ME2ON
source_sector = R6 / R11
case_type = overheat / price_moved_without_evidence
archetype = DIGITAL_ASSET_POLICY_OVERHEAT
```

KRW stablecoin basket은 R13의 대표적인 price-only case다. FT는 Kakao Pay가 한 달 동안 2배 이상, LG CNS가 약 70%, Aton이 80%, ME2ON이 3배 상승했다고 보도했다. 그러나 같은 기사에서 규제 프레임은 아직 불명확했고, margin loan이 20.5조 원까지 늘었으며, 별도 FT 기사에서는 Bank of Korea가 비은행 stablecoin 발행이 자본유출과 금융안정을 흔들 수 있다고 우려한다고 정리했다. ([Financial Times][8])

### stage date

```text
Stage 1:
2025-06
- won stablecoin policy pledge
- digital asset reform 기대
- private won-backed stablecoin issuance debate

Stage 2:
약함
- 법안·정책 기대는 있었지만 회사별 수익모델 미확인

Stage 3:
없음
- issuer license, reserve income, fee revenue, regulatory capital 확인 전 Green 금지

Stage 4B:
2025-06
- Kakao Pay >2배
- LG CNS +70%
- Aton +80%
- ME2ON 3배

Stage 4C:
비은행 발행 제한, 외환리스크 우려, 규제 지연, 실질 revenue 부재
```

### 실제 가격경로 검증

```text
price_data_source:
FT reported return and policy-risk anchors

stage3_price:
N/A

Kakao_Pay_reported_MFE_month:
> +100%

LG_CNS_reported_MFE_month:
+70%

Aton_reported_MFE_month:
+80%

ME2ON_reported_MFE_month:
+200%

margin_loan_context:
20.5T won

proposed_minimum_equity_for_issuers:
500M won

regulated_revenue_confirmed:
false

issuer_license_confirmed:
false

reserve_income_confirmed:
false

MFE_30D:
reported return anchors available

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### R13 판정

```text
score_price_alignment = price_moved_without_evidence
rerating_result = stablecoin_policy_theme_overheat
stage_failure_type = should_have_been_stage1_or_4B_watch
```

Stablecoin basket은 **R6/R11의 가격 선행 오염 case**다.

---

# 5. 이번 R13 case별 요약표

| case              | source R | 분류                        |                                                   실제 가격검증 | R13 판정                       |
| ----------------- | -------: | ------------------------- | --------------------------------------------------------: | ---------------------------- |
| SK하이닉스            |       R2 | structural_success + 4B   | 222,000원 → 1,447,000원, +551.8%; 2025 +274%, 2026 +200% 이상 | Stage 3 성공, 현재 4B            |
| APR / Medicube    |       R5 | structural_success + 4B   |             IPO 이후 >75%; Q4 revenue +124%, overseas +203% | Stage 3 후보 성공, 4B            |
| 삼성SDS             |    R8/R6 | success_candidate + event |                 KKR CB $820M, 장중 +20.8%, relative +17.8pp | Stage 2 + 4B                 |
| 현대제철              |   R4/R11 | false_positive 방지         |               U.S. CAPEX 후 -21.2%; rebar NP forecast -73% | policy capex failure         |
| L&F               |    R3/R4 | hard 4C                   |                         Tesla cathode deal $2.9B → $7,386 | contract-quality hard 4C     |
| 제주항공              |       R9 | hard 4C                   |          -15.7%, 6,920원, 시총 95.7B wipeout, 179 fatalities | safety hard 4C               |
| Hormuz / Iran     |      R11 | macro hard 4C             |       oil supply shock, corporate cost ≥$25B, IEA deficit | macro hard 4C                |
| stablecoin basket |   R6/R11 | price-only                |           Kakao Pay >2x, LG CNS +70%, Aton +80%, ME2ON 3x | price_moved_without_evidence |

---

# 6. score-price alignment 판정

```text
aligned:
- SK하이닉스
- APR / Medicube

4B-watch_success:
- SK하이닉스 market-cap milestone
- APR valuation / single-brand concentration
- 삼성SDS KKR/AI capital allocation +20.8%
- stablecoin basket 2~3배

false_positive_score_prevention:
- 현대제철 U.S. policy CAPEX
- tariff hedge / policy capex without funding and margin clarity

price_moved_without_evidence:
- KRW stablecoin basket
- AI / digital asset / policy theme before regulated revenue

hard_4C:
- L&F contract-quality break
- 제주항공 fatal safety accident
- Hormuz / Iran geopolitical energy shock

watch_to_hard_upgrade_candidate:
- cybersecurity / privacy trust breaks
- governance legal breaks
- PF credit breaks
- construction safety accidents
```

---

# 7. 점수비중 교정

## 올릴 축

```text
price_path_alignment +5
stage3_to_large_MFE_confirmation +5
revenue_or_EPS_revision +5
commercial_revenue_conversion +5
actual_contract_quality +5
actual_calloff_or_take_or_pay +5
operational_trust +5
security_privacy_trust +5
macro_risk_overlay +5
hard_4c_early_warning +5
```

### 왜 올리나

SK하이닉스와 APR은 Stage 3 또는 Stage 3 후보가 실제 가격경로와 매출경로로 이어질 수 있음을 보여준다. SK하이닉스는 HBM/EPS revision 이후 +551.8% reported MFE가 나왔고, APR은 Q4 매출 +124%, 해외 매출 +203%라는 실적 전환이 있었다. 반대로 L&F, 제주항공, Hormuz는 계약·안전·거시 리스크가 한 번 깨지면 Green 논리를 즉시 닫아야 한다는 hard 4C 기준이다.

## 내릴 축

```text
policy_news_only -5
resource_or_digital_asset_theme_only -5
stablecoin_policy_theme_only -5
AI_capital_allocation_without_revenue -5
contract_headline_without_calloff -5
capex_without_funding_or_margin -5
M&A_or_CB_event_without_revenue -4
IPO_or_debut_premium -4
high_score_without_price_validation -5
```

### 왜 내리나

삼성SDS는 AI capital allocation으로 장중 +20.8% 올랐지만 recurring AI revenue 전에는 Green이 아니다. 현대제철은 U.S. CAPEX와 tariff hedge 논리에도 funding·margin clarity 부재로 무너졌다. stablecoin basket은 issuer license·reserve income·fee revenue 없이 2~3배 올랐다.

## Green gate 강화 조건

```text
R13 공통 Stage 3-Green 필수:
1. 회사 단위 evidence가 있음
2. revenue / EPS / FCF로 내려오는 경로가 있음
3. price path가 evidence 이후 따라옴
4. Stage 3 이후 MFE가 의미 있게 큼
5. MAE가 과도하지 않음
6. 4B saturation 상태가 아님
7. hard RedTeam 없음
8. contract / operational / governance / security / macro trust 통과
```

## 4B 조기감지 조건

```text
4B-watch:
Stage 3 이후 2~5배 이상 상승
시총 milestone이 headline화
대형 CB / 증자 / M&A event
뉴스 발표일 20~30% 급등
정책·MOU·자원발견·stablecoin 테마 급등
IPO/debut 후 단기 2배
좋은 뉴스에도 주가 반응 둔화 또는 하락
valuation이 evidence보다 먼저 감

4B-elevated:
SK하이닉스처럼 1조 달러 근접
APR처럼 single-brand/device 매출 집중 속 valuation 급등
삼성SDS처럼 AI revenue 전 +20%급 상승
stablecoin처럼 regulated revenue 전 2~3배 상승
policy capex가 funding/margin보다 먼저 가격화
```

## 4C hard gate 조건

```text
contract_cancellation
contract_value_collapse
fatal_safety_accident
operational_trust_break
security_or_privacy_breach_with_revenue_cut
major_governance_legal_break
PF_workout_or_credit_break
regulatory_reversal
geopolitical_energy_chokepoint_shock
commercialization_failure
financing_failure
capex_without_funding_clarity
```

이번 R13 Loop 10에서 확정 hard 4C는 **L&F 계약가치 붕괴**, **제주항공 fatal safety accident**, **Hormuz/Iran macro energy shock**이다. 현대제철은 hard 4C라기보다 false-positive prevention / 4C-watch다. 삼성SDS와 stablecoin basket은 4B/Event Premium이다.

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

## docs/round/round_171.md 요약

```md
# R13 Loop 10. Cross-archetype RedTeam / 4B / Price Validation

이번 라운드는 R1~R12 Loop 10을 다시 검증한 R13 price-validation 라운드다.

핵심 결론:
- SK Hynix is the clean Stage 3 success benchmark. Stage 3 anchor was 222,000 won, and later reported record high was 1,447,000 won, implying +551.8% MFE. It also gained +274% in 2025 and >+200% in 2026, with market cap around $942B. Current state is 4B-watch.
- APR / Medicube is R5 structural-success benchmark. Q4 2025 revenue +124%, overseas revenue +203%, FY revenue about $1.2B, Medicube about $1.1B. Single-brand/device concentration means 4B-watch.
- Samsung SDS is Stage 2 + 4B-watch. KKR $820M CB and AI capital allocation drove +20.8% before recurring AI revenue was proven.
- Hyundai Steel is false-positive prevention. U.S. steel capex initially rallied, then reversed, and shares lost -21.2% after the announcement due to funding/margin uncertainty.
- L&F is hard 4C contract-quality anchor. Tesla cathode deal value collapsed from $2.9B to $7,386.
- Jeju Air is hard 4C operational-safety anchor. Fatal crash killed 179, shares fell -15.7% to 6,920 won, and 95.7B won market cap was wiped out.
- Hormuz/Iran shock is macro hard 4C. Oil supply disruption, corporate costs of at least $25B, and IEA deficit forecasts make this a cross-sector macro gate.
- Stablecoin basket is price_moved_without_evidence. Kakao Pay >2x, LG CNS +70%, Aton +80%, ME2ON 3x before issuer license, reserve income or fee revenue were confirmed.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 171 R13 Loop 10 Cross-archetype Price Validation

## 반영 내용
- R13 Loop 10 cross-archetype price-validation 라운드를 추가했다.
- Structural success, 4B timing, policy capex false-positive, contract hard 4C, operational-safety hard 4C, macro hard 4C, digital-asset price-only rally를 비교했다.
- Reuters/FT/MarketWatch/Vogue Business/Business Insider/AP reported anchors로 가능한 MFE/MAE 및 event/contract/trust/macro metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- price_path_alignment, stage3_to_large_MFE_confirmation, revenue/EPS conversion, actual contract quality, operational/security/macro trust 가중치 강화
- policy news-only, stablecoin policy theme-only, AI capital allocation without revenue, contract headline without call-off, capex without funding/margin 감점 강화
- 4B-watch와 hard 4C 구분 강화
```

## case row 초안

```jsonl
{"case_id":"r13_loop10_sk_hynix_hbm_stage3_4b","symbol":"000660","company_name":"SK Hynix","source_sector":"R2","case_type":"structural_success","primary_archetype":"STRUCTURAL_SUCCESS_BUT_4B_WATCH","stage3_date":"2024-06-25","stage4b_date":"2026-05-04/2026-05-14","price_validation":{"price_data_source":"MarketWatch/Reuters reported anchors","stage3_price":222000,"reported_peak_price":1447000,"peak_return_from_stage3_pct":551.8,"reported_return_2025_pct":274,"reported_return_2026_ytd_pct":200,"minimum_compounded_return_from_2025_start_pct":1022,"market_cap_mfe_minimum_pct":842,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"aligned","rerating_result":"true_rerating","notes":"HBM dominance and EPS revision produced large MFE; current state is 4B-watch."}
{"case_id":"r13_loop10_apr_medicube_structural_4b","symbol":"278470","company_name":"APR / Medicube","source_sector":"R5","case_type":"structural_success","primary_archetype":"K_BEAUTY_DEVICE_GLOBAL_BRAND","stage2_date":"2025-07-08","stage3_date":"2025-Q4_candidate","stage4b_date":"2025-2026","price_validation":{"price_data_source":"Vogue Business/Business Insider anchors","stage2_price":158300,"implied_ipo_reference_price_max":90457,"ipo_to_stage2_mfe_min_pct":75,"market_cap_july_2025_usd_bn":4.2,"q4_2025_revenue_usd_mn":440,"q4_2025_revenue_growth_pct":124,"q4_2025_overseas_revenue_usd_mn":362,"q4_2025_overseas_growth_pct":203,"fy_2025_revenue_usd_bn":1.2,"medicube_fy_2025_revenue_usd_bn":1.1,"medicube_revenue_share_pct":91.7,"tiktok_shop_revenue_usd_mn":102.9,"price_validation_status":"reported_price_and_revenue_anchor_not_full_ohlc"},"score_price_alignment":"aligned","rerating_result":"K_beauty_device_true_rerating_plus_4B_watch","notes":"Revenue conversion supports structural success, but single-brand/device concentration and valuation require 4B-watch."}
{"case_id":"r13_loop10_samsung_sds_kkr_ai_event_4b","symbol":"018260","company_name":"Samsung SDS","source_sector":"R8/R6","case_type":"success_candidate","primary_archetype":"AI_CAPITAL_ALLOCATION_EVENT_PREMIUM","stage2_date":"2026-04-15","stage4b_date":"2026-04-15","price_validation":{"price_data_source":"Reuters reported event return anchor","stage3_price":null,"event_mfe_1d_pct":20.8,"morning_trade_return_pct":19.4,"kospi_same_context_pct":3.0,"relative_intraday_outperformance_pp":17.8,"cb_investment_usd_mn":820,"cb_investment_krw_trn":1.207,"existing_cash_krw_trn":6.4,"combined_cash_plus_cb_krw_trn":7.607,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"AI_cloud_capital_allocation_watch","notes":"AI/KKR capital allocation is Stage 2 and 4B before AI revenue/FCF."}
{"case_id":"r13_loop10_hyundai_steel_policy_capex_failure","symbol":"004020","company_name":"Hyundai Steel","source_sector":"R4/R11","case_type":"failed_rerating","primary_archetype":"POLICY_CAPEX_FALSE_POSITIVE","stage2_date":"2025-03-25","stage4c_date":"2025-04-22/2024-06-21","price_validation":{"price_data_source":"Reuters/MarketWatch capex and weak-demand anchors","stage3_price":null,"us_plant_investment_usd_bn":"5.8-6.0","us_plant_capacity_mn_tpy":2.7,"announcement_initial_mfe_pct":5,"announcement_session_mae_pct":-4.4,"post_announcement_drawdown_pct":-21.2,"posco_holdings_same_period_pct":-18.3,"benchmark_same_period_pct":-5.5,"relative_underperformance_vs_benchmark_pp":-15.7,"funding_plan":"50pct_borrowing_rest_unclear_possible_posco_equity","net_profit_forecast_2024_krw_bn":215,"net_profit_forecast_cut_pct":-73,"implied_prior_net_profit_forecast_krw_bn":796.3,"rebar_price_expected_decline_pct":-10,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"false_positive_score_prevention","rerating_result":"policy_capex_without_funding_failed","notes":"Tariff-hedge capex without funding/margin clarity is 4C-watch, not Green."}
{"case_id":"r13_loop10_lnf_tesla_cathode_contract_hard_4c","symbol":"066970","company_name":"L&F","source_sector":"R3/R4","case_type":"4c_thesis_break","primary_archetype":"CONTRACT_QUALITY_HARD_4C","stage4c_date":"2025-12-29","price_validation":{"price_data_source":"Reuters contract-value collapse anchor","stage3_price":null,"initial_contract_value_usd_bn":2.9,"revised_contract_value_usd":7386,"contract_value_drawdown_pct":-99.999745,"contract_period":"2024-2025","product":"high-nickel cathode materials for Tesla 4680 cells","reason_context":["4680_yield_issue","EV_demand_slowdown","Cybertruck_demand_disappointment"],"price_validation_status":"reported_contract_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"battery_material_contract_quality_failure","notes":"Customer name and contract headline cannot be Green without actual call-off and volume/margin conversion."}
{"case_id":"r13_loop10_jeju_air_operational_safety_hard_4c","symbol":"089590","company_name":"Jeju Air","source_sector":"R9","case_type":"4c_thesis_break","primary_archetype":"OPERATIONAL_SAFETY_HARD_4C","stage4c_date":"2024-12-30","price_validation":{"price_data_source":"Reuters crash/price/safety-probe anchors","stage3_price":null,"event_mae_1d_pct":-15.7,"event_low_price":6920,"implied_pre_event_reference_price":8209,"market_cap_wipeout_krw_bn":95.7,"fatalities":179,"ak_holdings_mae_pct":-12,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"operational_safety_trust_break","notes":"Fatal accident is hard 4C and blocks travel/LCC demand Green."}
{"case_id":"r13_loop10_hormuz_iran_macro_hard_4c","symbol":"KOSPI/KRW/exporters/refiners/airlines/autos/chips","company_name":"Hormuz / Iran macro energy shock","source_sector":"R11","case_type":"4c_thesis_break","primary_archetype":"MACRO_GEOPOLITICAL_HARD_4C","stage4c_date":"2026-03_to_2026-05","price_validation":{"price_data_source":"Reuters geopolitical energy-shock / IEA / corporate-cost anchors","stage3_price":null,"global_company_cost_usd_bn":25,"oil_price_context_usd_per_bbl":100,"iea_supply_shortfall_2026_mn_bpd":1.78,"iea_q2_deficit_mn_bpd":6.0,"global_supply_decline_expected_mn_bpd":3.9,"shut_in_oil_context_mn_bpd":14,"price_validation_status":"macro_anchor_not_company_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"geopolitical_energy_security_hard_4C","notes":"Hormuz/Iran shock is cross-sector macro hard 4C due to energy, shipping, raw-material and FX pressure."}
{"case_id":"r13_loop10_stablecoin_policy_theme_overheat","symbol":"377300/LG_CNS/Aton/ME2ON","company_name":"KRW stablecoin policy basket","source_sector":"R6/R11","case_type":"overheat","primary_archetype":"DIGITAL_ASSET_POLICY_OVERHEAT","stage1_date":"2025-06","stage4b_date":"2025-06","price_validation":{"price_data_source":"FT return and policy-risk anchors","stage3_price":null,"kakao_pay_mfe_month_pct":100,"lg_cns_mfe_month_pct":70,"aton_mfe_month_pct":80,"me2on_mfe_month_pct":200,"margin_loan_context_krw_trn":20.5,"proposed_minimum_equity_for_issuers_krw_mn":500,"regulated_revenue_confirmed":false,"issuer_license_confirmed":false,"reserve_income_confirmed":false,"price_validation_status":"reported_return_anchor_not_full_ohlc"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"stablecoin_policy_theme_overheat","notes":"Stablecoin theme rallied before licensed issuer, reserve income, fee revenue or regulatory capital clarity."}
```

## shadow weight row 초안

```csv
archetype,price_path_alignment,stage3_mfe_confirmation,revenue_eps_conversion,actual_contract_quality,operational_trust,macro_risk_overlay,event_penalty,capex_funding_redteam,governance_security_redteam,4b_watch_sensitivity,hard_4c_sensitivity,notes
STRUCTURAL_SUCCESS_ALIGNED,+5,+5,+5,+4,+3,+2,0,+0,+0,+4,+2,SK Hynix and APR prove Stage 3 can produce large MFE when revenue/EPS conversion exists.
STRUCTURAL_SUCCESS_BUT_4B_WATCH,+5,+5,+5,+4,+3,+2,-1,+1,+1,+5,+3,Large MFE plus market-cap/valuation milestone requires 4B-watch.
AI_CAPITAL_ALLOCATION_EVENT_PREMIUM,+3,+2,+3,+2,+3,+2,-5,+3,+2,+5,+3,Samsung SDS KKR event is Stage 2 and 4B before AI revenue/FCF.
POLICY_CAPEX_FALSE_POSITIVE,+0,+0,+0,+1,+2,+2,-5,+5,+2,+4,+4,Hyundai Steel shows policy capex without funding/margin can fail.
CONTRACT_QUALITY_HARD_4C,+0,+0,+0,+5,+2,+1,0,+1,+1,+3,+5,L&F contract value collapse is hard 4C.
OPERATIONAL_SAFETY_HARD_4C,+0,+0,+0,+0,+5,+2,0,+0,+2,+3,+5,Jeju Air fatal crash is hard operational trust 4C.
MACRO_GEOPOLITICAL_HARD_4C,+0,+0,+0,+0,+3,+5,0,+2,+2,+4,+5,Hormuz/Iran shock is cross-sector macro hard 4C.
DIGITAL_ASSET_POLICY_OVERHEAT,+0,+0,+0,+0,+1,+3,-5,+1,+3,+5,+4,Stablecoin rallies are price_moved_without_evidence until licensing/revenue clarity.
```

---

# 이번 R13 Loop 10 결론

R13의 결론은 단단하다.

```text
1. Stage 3는 잘 잡히면 진짜 대형 MFE를 만든다.
   SK하이닉스와 APR이 그 증거다.

2. 그러나 대형 MFE 이후에는 4B-watch가 빨리 붙어야 한다.
   SK하이닉스의 시총 milestone, APR의 single-brand concentration이 그렇다.

3. 좋은 Stage 2라도 Green은 아니다.
   삼성SDS의 KKR/AI capital allocation은 좋은 후보지만 +20.8%는 4B다.

4. 정책 CAPEX는 Green이 아니라 false positive가 될 수 있다.
   현대제철 U.S. plant가 그 반례다.

5. 계약 headline은 actual call-off 없으면 무너질 수 있다.
   L&F는 R3/R4 hard 4C 기준점이다.

6. 안전사고는 가장 강한 hard 4C다.
   제주항공은 operational trust가 깨지면 여행수요가 아무 의미 없음을 보여준다.

7. macro shock은 모든 섹터 위에 덮이는 4C gate다.
   Hormuz/Iran shock은 에너지·운송·제조·환율 리스크를 동시에 찌른다.

8. 디지털자산 정책 테마는 price-only rally가 가장 많다.
   stablecoin basket은 발행권·reserve income·fee revenue 전 Green 금지다.
```

한 문장으로 압축하면:

> **R13의 역할은 “좋아 보이는 후보”를 한 번 더 부수는 것이다. Stage 3는 대형 MFE와 revenue/EPS conversion으로 증명되고, 4B는 가격 선반영·crowding·event premium으로 증명되며, 4C는 계약·안전·거시·운영·규제·신뢰 훼손으로 증명된다.**

[1]: https://www.marketwatch.com/story/sk-hynix-s-hbm-dominance-higher-chip-prices-could-lift-earnings-market-talk-6508cbf8?utm_source=chatgpt.com "SK Hynix's HBM Dominance, Higher Chip Prices Could Lift Earnings -- Market Talk"
[2]: https://www.vogue.com/article/how-k-beauty-brand-medicube-pulled-off-its-global-breakout?utm_source=chatgpt.com "How K-Beauty Brand Medicube Pulled Off Its Global Breakout"
[3]: https://www.reuters.com/world/asia-pacific/kkr-buy-820-million-samsung-sds-convertible-bonds-shares-jump-20-2026-04-15/?utm_source=chatgpt.com "KKR to buy $820 million of Samsung SDS convertible bonds, shares jump 20%"
[4]: https://www.reuters.com/markets/commodities/hyundai-steel-build-plant-louisiana-with-annual-output-27-million-tonnes-2025-03-25/?utm_source=chatgpt.com "Hyundai Steel unveils US factory plan, shares skid"
[5]: https://www.reuters.com/world/asia-pacific/south-koreas-lf-says-value-battery-material-supply-deal-with-tesla-cut-7386-2025-12-29/?utm_source=chatgpt.com "South Korea's L&F slashes value of battery material supply deal with Tesla"
[6]: https://www.reuters.com/business/aerospace-defense/jeju-air-shares-plunge-record-low-after-deadly-plane-crash-2024-12-30/?utm_source=chatgpt.com "Jeju Air shares plummet to record low after deadly plane crash"
[7]: https://www.reuters.com/world/europe/iran-war-saddles-global-companies-with-25-billion-bill-counting-2026-05-18/?utm_source=chatgpt.com "Iran war saddles global companies with $25 billion bill - and counting"
[8]: https://www.ft.com/content/4b19bf90-4202-4fe7-8caf-d7db6deeb768?utm_source=chatgpt.com "Crypto-crazy investors make South Korea the best-performing market in Asia"

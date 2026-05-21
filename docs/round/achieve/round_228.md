순서상 이번은 **R11 Loop 9 — 정책·지정학·재난·이벤트 가격경로 검증 라운드**다.

이번 R11은 “새로운 대박 종목을 찾는 라운드”가 아니라, **정책·지정학·재난 뉴스가 실제 계약·예산·매출·EPS/FCF로 승격됐는지**를 확인하는 라운드다. R11의 기본값은 Green이 아니라 **Stage 1 / Stage 2 / Event Premium / Macro Overlay**다.

```text
round = R11 Loop 9
round_id = round_156
large_sector = POLICY_GEOPOLITICAL_EVENT
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
r11_default_stage3_bias = very_conservative
hard_4c_confirmed = false
```

이번에도 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉 OHLC는 안정적으로 직접 확보하지 못했다. 대신 Reuters / FT / WSJ / MarketWatch가 제공한 **가격 anchor, 이벤트 수익률, 정책금액, 계약기간, 관세율, 거시충격 수치**로 계산 가능한 값만 계산했다.

---

# 1. 이번 라운드 대섹터

```text
R11 = 정책·지정학·재난·이벤트
```

R11의 핵심 질문은 이거다.

```text
정책 뉴스가 큰가?
아니면 정책이 실제 계약·예산·발주·수익·EPS/FCF로 내려왔는가?
```

---

# 2. 대상 canonical archetype

```text
GOVERNANCE_REFORM_VALUEUP_POLICY
TAX_POLICY_MARKET_SHOCK
US_KOREA_TARIFF_TRADE_DEAL
POLICY_INDUCED_CAPEX_TARIFF_HEDGE
SEMICONDUCTOR_POLICY_SUPPORT
FISCAL_STIMULUS_CONSUMPTION_EVENT
ENERGY_SECURITY_LONG_TERM_OFFTAKE
DOMESTIC_RESOURCE_DISCOVERY_EVENT
MARKET_STRUCTURE_REFORM
MACRO_FX_OUTFLOW_OVERLAY
PRICE_ONLY_RALLY
EVENT_PREMIUM
```

---

# 3. deep sub-archetype

```text
거버넌스 / 밸류업:
- Commercial Act amendment
- fiduciary duty to all shareholders
- treasury share cancellation
- Korea discount
- KOSPI 5,000 narrative
- market-level rerating vs company-level EPS

세제 / 시장충격:
- capital gains tax threshold
- dividend / corporate / transaction tax proposals
- KOSPI drawdown
- policy surprise as 4C-watch

미국 관세 / 무역협상:
- 25% tariff threat
- 15% tariff deal
- $350B U.S. investment pledge
- FX outflow / won risk
- auto / steel / shipbuilding exposure

반도체 정책:
- 33T won chip support package
- financial assistance 20T won
- Samsung / SK Hynix policy support
- policy budget vs company order / margin

재정·소비 부양:
- 30.5T won supplementary budget
- 150,000~500,000 won vouchers
- consumption event vs retail revenue conversion

에너지 안보:
- POSCO International Alaska LNG 20-year offtake
- 1 mtpa LNG
- pipeline steel supply
- FID and margin before Green

자원발견 이벤트:
- East Sea oil/gas
- Korea Gas +30%
- drilling cost 100B won per well
- commerciality unknown
```

---

# 4. 국장 신규 후보 case

## Case A — Commercial Act / 밸류업 거버넌스 개혁 `success_candidate / market-structure Stage 2`

```text
symbols = KOSPI / 저PBR·지주·금융·자사주소각 basket
case_type = success_candidate / market_structure_watch
archetype = GOVERNANCE_REFORM_VALUEUP_POLICY
```

### stage date

```text
Stage 1:
2025-07-03
- Commercial Act revision passed
- directors’ fiduciary duty expanded to protect minority shareholders
- Korea Discount 해소 정책

Stage 2:
2025-08-25 / 2026-02-25
- audit committee separate voting / minority shareholder representation 강화
- newly acquired treasury shares must be cancelled within one year
- shareholder-return infrastructure 강화

Stage 3:
없음
- market structure positive지만 개별 종목 Green 아님
- 실제 소각, 배당, ROE, EPS/FCF 확인 필요

Stage 4B:
Korea discount 해소 기대만으로 저PBR·지주·금융 basket이 먼저 급등하면 후보

Stage 4C:
법안 후퇴, litigation risk, 기업 반발, tax-policy shock으로 market confidence 훼손 시 후보
```

Commercial Act 개정은 R11에서 드문 **positive market-structure Stage 2**다. 2025년 7월 개정안은 이사의 충실의무를 소액주주 보호 쪽으로 확장했고, 당시 KOSPI는 1.34% 올라 3,116.27로 마감했다. 2025년 8월 후속 개정은 감사위원 분리선출과 소액주주 대표 선임 가능성을 강화했다. 2026년 2월에는 새로 취득한 자사주를 1년 내 소각하도록 하는 개정도 통과된 것으로 보도됐다. 이건 “Green”이 아니라 **Green을 가능하게 만드는 제도적 토양**이다. ([Reuters][1])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / FT market-structure anchors

stage3_price:
N/A

KOSPI_2025-07-03_close:
3,116.27

KOSPI_event_return:
+1.34%

treasury_share_cancellation_rule:
newly acquired treasury shares must be cancelled within one year

2026_KOSPI_context:
FT reported KOSPI topped 6,000 after 76% gain in 2025 and >40% gain in 2026

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

Stage 3 판정:
개별 기업 Stage 3 아님.
회사별 실제 소각·배당·ROE/EPS 확인 필요.
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = market_structure_valueup_watch
stage_failure_type = market_structure_stage2_not_company_green
```

---

## Case B — 세제안 shock `4C-watch / policy confidence break`

```text
symbols = KOSPI / 저PBR·배당·개인투자자 민감 basket
case_type = 4C-watch / macro_policy_shock
archetype = TAX_POLICY_MARKET_SHOCK
```

### stage date

```text
Stage 1:
2025-08-01
- capital gains tax threshold reduction proposal
- corporate / dividend / transaction tax increase proposal

Stage 2:
없음
- 세제 shock은 positive stage가 아니라 RedTeam input

Stage 3:
없음

Stage 4C-watch:
2025-08-01
- KOSPI -3.9%
- 2025년 강세장 momentum이 급격히 흔들림
```

정책개혁은 항상 한 방향으로만 작동하지 않는다. MarketWatch는 2025년 8월 Lee Jae Myung 정부의 세제안이 KOSPI를 3.9% 끌어내렸다고 보도했다. 제안에는 양도소득세 과세 기준을 50억 원에서 10억 원으로 낮추는 방안, 법인세·배당소득세·증권거래세 인상 등이 포함됐다. R11에서는 이런 사건을 **Korea Discount 해소 정책의 반대편에 있는 policy-confidence 4C-watch**로 둔다. ([마켓워치][2])

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch reported market-return and tax-policy anchor

stage3_price:
N/A

KOSPI_event_MAE:
-3.9%

capital_gains_tax_threshold_before:
5B won

capital_gains_tax_threshold_after_proposal:
1B won

threshold_reduction:
1B / 5B - 1
= -80%

transaction_tax_change:
15bp → 20bp

transaction_tax_increase:
20 / 15 - 1
= +33.3%

petition_context:
42,000 signatures out of 50,000 needed for review

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = macro_policy_shock
rerating_result = tax_policy_confidence_break_watch
stage_failure_type = 4C_watch_not_hard_4C
```

---

## Case C — 한미 관세·$350B 투자 deal `success_candidate + FX/macro 4C-watch`

```text
symbols = Hyundai / Kia / steel / shipbuilding / FX-sensitive exporters
case_type = success_candidate + macro_4C_watch
archetype = US_KOREA_TARIFF_TRADE_DEAL / MACRO_FX_OUTFLOW_OVERLAY
```

### stage date

```text
Stage 1:
2025-04~07
- U.S. tariffs on South Korean autos and steel
- 25% tariff threat
- export competitiveness risk

Stage 2:
2025-10-29 / 2025-12-01
- trade deal effectively finalized
- tariff lowered to 15%, retroactive to 2025-11-01
- semiconductor / pharma national-security tariffs capped at 15%
- South Korea commits $350B strategic U.S. investments

Stage 3:
없음
- tariff deal은 macro relief
- 개별 기업 Stage 3는 margin recovery, FCF, order, EPS 확인 후

Stage 4C-watch:
2025-08~12
- BOK expects significant growth shock even after deal
- $350B investment pledge can pressure won / FX outflows
```

한미 무역 deal은 R11에서 **Stage 2 relief**다. 자동차 관세가 25%에서 15%로 낮아진 점은 Hyundai/Kia 등 수출주에 긍정적이지만, Bank of Korea는 평균 관세율이 기존 FTA상 0%에서 약 15%로 올라 국내 경제에 여전히 큰 충격을 준다고 봤다. BOK는 tariff impact가 2025년 성장률을 -0.45pp, 2026년을 -0.60pp 낮출 수 있다고 추정했다. FT는 $350B 미국 투자 pledge가 대규모 달러 유출 우려를 만들고, 한국이 외평채 발행 한도를 2026년 record $5B로 늘렸다고 보도했다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / FT macro-trade anchors

stage3_price:
N/A

tariff_before_deal:
25% for autos / high product-specific tariffs

tariff_after_deal:
15%

tariff_reduction:
15 / 25 - 1
= -40%

average_tariff_change_vs_prior_FTA:
0% → about 15%

BOK_estimated_growth_hit_2025:
-0.45pp

BOK_estimated_growth_hit_2026:
-0.60pp

South_Korea_US_investment_pledge:
$350B

agreed_annual_dollar_outflow_limit:
$20B

foreign_exchange_bond_cap_2026:
$5B

foreign_exchange_bond_cap_2025:
$3.5B

cap_increase:
5 / 3.5 - 1
= +42.9%

won_reaction_on_deal_headline:
+0.54% vs USD on Reuters report

MFE / MAE:
company-specific unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate + macro_4C_watch
rerating_result = tariff_relief_but_fx_outflow_watch
stage_failure_type = macro_stage2_not_company_green
```

---

## Case D — 현대제철 U.S. 투자 `failed_rerating / policy-induced capex watch`

```text
symbol = 004020
case_type = failed_rerating / 4C-watch
archetype = POLICY_INDUCED_CAPEX_TARIFF_HEDGE
```

### stage date

```text
Stage 1:
2025-03~04
- U.S. tariff pressure
- Korean steel exporter seeks U.S. local investment

Stage 2:
약함
- $6B U.S. steel plant plan
- tariff hedge 목적

Stage 3:
없음
- 투자계획만으로 Green 금지
- funding, tariff benefit, margin, FCF 확인 필요

Stage 4C-watch:
2025-04-22
- investors criticized lack of funding detail
- Hyundai Steel shares hammered, dropped over 21%
- weak domestic demand / Chinese imports / labor disputes also present
```

Hyundai Steel의 미국 $6B steel plant 계획은 tariff hedge처럼 보이지만, 투자자들은 funding detail 부재와 전략 불확실성을 우려했다. Reuters는 이 계획 발표 후 Hyundai Steel 주가가 21% 넘게 하락했고, 회사가 투자자들과 call을 열어 “세부 내용 검토 중에 발표해 미안하다”고 설명했다고 보도했다. R11에서는 이것을 **정책 유도 CAPEX가 Green이 아니라 4C-watch로 바뀌는 사례**로 둔다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters policy-induced capex / market-reaction anchor

stage3_price:
N/A

U.S._plant_investment:
$6B

Hyundai_Motor_Group_U.S._package:
$21B

reported_share_drop_after_announcement:
> -21%

funding_plan:
half via borrowing, possible POSCO equity input

policy_goal:
tariff exemption / tariff mitigation

risk_factors:
funding uncertainty
domestic demand weakness
Chinese imports
labor disputes

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = false_positive_score_prevention
rerating_result = policy_capex_without_funding_failed
stage_failure_type = 4C_watch
```

---

## Case E — 반도체 33조 지원 package `success_candidate / policy support not Green`

```text
symbols = Samsung Electronics / SK Hynix / semiconductor ecosystem
case_type = success_candidate
archetype = SEMICONDUCTOR_POLICY_SUPPORT
```

### stage date

```text
Stage 1:
2025-04-15
- U.S. tariff uncertainty
- China competition
- Korean chip sector policy support 확대

Stage 2:
2025-04-15
- semiconductor support package expanded to 33T won
- financial assistance programme increased to 20T won
- chips were 21% of exports in 2024, $141.9B

Stage 3:
없음
- 정책 지원만으로 Green 금지
- company-level orders, capex efficiency, margin, EPS/FCF 확인 필요

Stage 4B:
정책지원 뉴스로 반도체 후발주가 실적 없이 급등하면 후보

Stage 4C:
지원에도 수요 둔화, capex inefficiency, export control, China competition, tariff shock 시 후보
```

정부는 2025년 4월 반도체 지원 package를 26조 원에서 33조 원으로 확대했고, chip-sector 금융지원도 17조 원에서 20조 원으로 늘렸다. Reuters는 반도체가 2024년 한국 수출의 21%, 1,419억 달러를 차지한다고 보도했다. 이건 R11에서 강한 Stage 2 policy support지만, 개별 기업 Green은 아니다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters policy-support anchor

stage3_price:
N/A

support_package_before:
26T won

support_package_after:
33T won

support_package_increase:
33 / 26 - 1
= +26.9%

financial_assistance_before:
17T won

financial_assistance_after:
20T won

financial_assistance_increase:
20 / 17 - 1
= +17.6%

semiconductor_export_value_2024:
$141.9B

semiconductor_share_of_exports_2024:
21%

MFE / MAE:
company-specific unavailable_after_deep_search

Stage 3 판정:
company-level order / EPS / margin 확인 전 Green 금지
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = semiconductor_policy_support_watch
stage_failure_type = policy_stage2_not_company_green
```

---

## Case F — 30.5조 추경·소비쿠폰 `event_premium / domestic-demand policy`

```text
symbols = retail / food / local consumption / construction / SME basket
case_type = event_premium / success_candidate
archetype = FISCAL_STIMULUS_CONSUMPTION_EVENT
```

### stage date

```text
Stage 1:
2025-06-19
- second supplementary budget
- domestic demand support
- cash-equivalent voucher policy

Stage 2:
2025-07-07
- legislature approves larger fiscal stimulus, 31.8T won
- cash handouts / gift coupons
- construction-sector support
- AI infrastructure
- small business support

Stage 3:
없음
- fiscal stimulus만으로 retail/consumer Green 금지
- same-store sales, margins, credit recovery, revenue conversion 확인 필요

Stage 4B:
소비쿠폰 뉴스로 유통·외식·로컬소비주가 먼저 급등하면 후보

Stage 4C:
재정적자, 일회성 소비, 물가압력, 소비 지속성 실패 시 후보
```

Lee Jae Myung 정부는 2025년 6월 30.5조 원 규모 두 번째 추경을 제안했고, 여기에는 모든 국민에게 15만~50만 원 상당 vouchers를 지급하는 10.3조 원 규모 소비지원책이 포함됐다. 이후 WSJ는 국회가 31.8조 원 규모 fiscal stimulus를 승인했다고 보도했다. 이 정책은 R11에서 Stage 1~2 consumption event지만, R5/R12 소비주 Stage 3는 실제 same-store sales·margin·FCF로 확인해야 한다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / WSJ fiscal-policy anchors

stage3_price:
N/A

supplementary_budget_initial:
30.5T won

approved_stimulus:
31.8T won

increase_vs_initial:
31.8 / 30.5 - 1
= +4.3%

new_spending_to_spur_growth:
20.2T won

tax_revenue_shortfall_makeup:
10.3T won

voucher_program:
10.3T won

voucher_amount:
150,000~500,000 won per person

most_people_voucher:
250,000 won

eligible_recipients:
about 51M

share_receiving_250k:
84%

treasury_bond_financing:
19.8T won

fiscal_deficit_after_budget:
4.2% of GDP

government_debt_after_budget:
about 49.0~49.1% of GDP

MFE / MAE:
sector stock data unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium / policy_support
rerating_result = domestic_demand_policy_watch
stage_failure_type = stage1_or_stage2_attention_only
```

---

## Case G — POSCO International / Alaska LNG `success_candidate / actual long-term offtake Stage 2`

```text
symbol = 047050
case_type = success_candidate
archetype = ENERGY_SECURITY_LONG_TERM_OFFTAKE
```

### stage date

```text
Stage 1:
2025-09
- preliminary Alaska LNG agreement
- U.S. LNG / energy-security sourcing

Stage 2:
2025-12-04
- Glenfarne Alaska LNG finalizes 20-year LNG supply deal with POSCO International
- 1 mtpa LNG for 20 years
- POSCO to make capital investment before FID
- POSCO to supply significant portion of steel for 807-mile pipeline

Stage 3:
보류
- final investment decision
- LNG price/margin
- steel supply margin
- cashflow and offtake economics 확인 필요

Stage 4B:
energy-security headline만으로 주가가 선반영되면 후보

Stage 4C:
FID delay, LNG price collapse, pipeline permitting, cost overrun, offtake margin failure 시 후보
```

POSCO International은 Glenfarne의 Alaska LNG project에서 20년간 연 100만 톤 LNG를 공급받는 계약을 확정했다. POSCO는 FID 전 capital investment를 하고, 807-mile pipeline에 필요한 steel 상당 부분을 공급할 예정이다. 이건 R11에서 단순 정책 뉴스보다 한 단계 높은 **실제 장기 offtake Stage 2**다. 그러나 FID, 가격·마진, 철강 공급 수익성, 현금흐름이 확인되기 전 Stage 3는 아니다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters LNG offtake / project anchor

stage3_price:
N/A

POSCO_International_stock_OHLC:
price_data_unavailable_after_deep_search
- Reuters는 contract metrics는 제공하지만 POSCO International event-day OHLC anchor는 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 일봉 OHLC 직접 확보 실패.

LNG_supply_volume:
1 mtpa

contract_duration:
20 years

total_contract_volume:
1 mtpa * 20
= 20 mt LNG

pipeline_length:
807 miles

preliminary_commitments_secured_by_Alaska_LNG:
11 mtpa

FID_status:
not yet, planned before year-end

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = energy_security_offtake_watch
stage_failure_type = stage2_watch_success
```

---

## Case H — 한국가스공사 / 동해 석유·가스 `price_moved_without_evidence`

```text
symbol = 036460
case_type = event_premium / price_moved_without_evidence
archetype = DOMESTIC_RESOURCE_DISCOVERY_EVENT
```

### stage date

```text
Stage 1:
2024-06-03
- East Sea oil/gas exploration approval
- up to 14B barrels resource possibility
- exploration drilling authorized

Stage 2:
없음
- drilling result 없음
- commerciality 없음
- production 없음

Stage 3:
없음
- resource estimate와 drilling approval만으로 Green 금지

Stage 4B:
2024-06-03
- Korea Gas +30% to 38,700원
- Daesung Energy +30%
- SK Innovation +6%
- SK Gas +7%

Stage 4C:
drilling failure, commerciality absence, budget/policy reversal, development cost burden 시 후보
```

한국가스공사는 동해 석유·가스 탐사 승인 발표 당일 30% 올라 38,700원을 기록했다. Reuters는 Korea Gas +30%, Daesung Energy +30%, SK Innovation +6%, SK Gas +7%를 보도했다. 하지만 탐사 성공률은 약 20%였고, 최대 10개 시추공이 필요할 수 있으며 각 시추 비용은 약 1,000억 원으로 언급됐다. WSJ도 경제성이 아직 확인되지 않았고 최소 5차례 시추가 필요하다고 정리했다. 이건 R11의 대표적인 **price_moved_without_evidence**다. ([Reuters][8])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / WSJ reported price and exploration anchors

stage3_price:
N/A

Korea_Gas_event_peak_price:
38,700원

Korea_Gas_event_MFE_1D:
+30.0%

implied_pre_event_reference_price:
38,700 / 1.30
= 약 29,769원

Daesung_Energy_event_MFE:
+30.0%

SK_Innovation_event_MFE:
+6.0%

SK_Gas_event_MFE:
+7.0%

estimated_resource_possibility:
up to 14B barrels oil/gas

success_rate:
about 20%

failure_probability:
80%

drilling_cost_per_well:
100B won

possible_wells:
up to 10

possible_total_drilling_cost:
100B * 10
= 1T won

commercial_production_target:
2035, if successful

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
success
- commerciality 전 +30%면 즉시 4B/event premium.
```

### alignment

```text
score_price_alignment = price_moved_without_evidence
rerating_result = resource_discovery_event_premium
stage_failure_type = should_have_been_stage1_or_4B_watch
```

---

# 5. 이번 R11 case별 요약표

| case                    | 분류                              |                                                   실제 가격검증 | alignment                    |
| ----------------------- | ------------------------------- | --------------------------------------------------------: | ---------------------------- |
| Commercial Act / 밸류업 개혁 | success_candidate               |                  KOSPI +1.34%, 3,116.27; 자사주 1년 내 소각 rule | market-structure Stage 2     |
| 세제안 shock               | 4C-watch                        |                    KOSPI -3.9%; CGT threshold 5B→1B, -80% | policy confidence break      |
| 한미 tariff / $350B deal  | success_candidate + macro watch |        tariff 25→15, -40%; BOK growth hit -0.45pp/-0.60pp | macro Stage 2                |
| 현대제철 U.S. plant         | failed_rerating                 |           $6B U.S. plant, shares >-21% after announcement | policy capex failed          |
| 반도체 33T 지원              | success_candidate               |                  support 26T→33T, +26.9%; finance 17T→20T | policy support Stage 2       |
| 30.5T 추경·소비쿠폰           | event premium                   |      31.8T approved; vouchers 150k~500k; deficit 4.2% GDP | domestic-demand event        |
| POSCO Int’l Alaska LNG  | success_candidate               |    1 mtpa x 20 years = 20 mt LNG; 807-mile pipeline steel | long-term offtake Stage 2    |
| 한국가스공사 East Sea         | overheat                        | 38,700원, +30%; 20% success, 1T won possible drilling cost | price_moved_without_evidence |

---

# 6. score-price alignment 판정

```text
success_candidate:
- Commercial Act / governance reform
- U.S.-Korea tariff deal, as macro relief
- semiconductor support package
- POSCO International Alaska LNG offtake

event_premium:
- fiscal stimulus / consumption vouchers
- Korea Gas East Sea oil/gas exploration
- housing / consumer / AI baskets if moved only on policy

price_moved_without_evidence:
- Korea Gas +30% before commerciality
- any consumer/retail basket rally before voucher-driven same-store sales
- chip 후발주 rally before actual order / EPS

thesis_break_watch / macro 4C-watch:
- tax proposal shock
- Hyundai Steel policy-induced capex/funding risk
- U.S.-Korea $350B FX outflow pressure

market_structure_stage2:
- Commercial Act / treasury share cancellation reform

hard_4c_confirmed:
- false
```

---

# 7. 점수비중 교정

## 올릴 축

```text
actual_contract_or_budget +5
funded_policy +5
policy_to_company_revenue_bridge +5
shareholder_rights_reform +4
treasury_share_cancellation_rule +4
long_term_offtake +5
project_FID_or_financing +4
macro_relief_with_margin_recovery +4
```

### 왜 올리나

Commercial Act와 자사주 소각 의무화는 한국 증시의 구조적 discount를 줄일 수 있는 market-structure Stage 2다. POSCO International의 Alaska LNG 20년 offtake는 단순 정책 뉴스보다 강한 실제 계약 Stage 2다. 반도체 33조 지원도 funded-policy 성격이 있지만, 개별 기업 Stage 3는 주문·마진·EPS로 확인되어야 한다.

## 내릴 축

```text
policy_news_only -5
resource_estimate_without_drilling -5
tax_policy_surprise -5
capex_for_tariff_without_funding -5
macro_FX_outflow_risk -4
stimulus_without_revenue_conversion -4
support_package_without_order -4
energy_security_headline_only -4
price_rally_before_commerciality -5
```

### 왜 내리나

한국가스공사는 경제성·상업성 전 +30%였고, Hyundai Steel의 미국 공장 계획은 tariff hedge로 보였지만 funding 불확실성 때문에 주가가 21% 넘게 하락했다. 세제안 shock은 value-up 정책과 정반대로 market confidence를 꺾는 macro 4C-watch다.

## Green gate 강화 조건

```text
R11 Stage 3-Green 필수:
1. 정책/이벤트가 회사 단위 계약으로 승격
2. 계약금액 또는 예산 확인
3. financing / FID 확인
4. 실제 발주 또는 조달계약
5. 매출 인식 가능성
6. margin 또는 EPS/FCF revision 확인
7. event fade가 아니라 반복 수요 확인
8. 가격경로가 증거 이후 따라옴

금지:
정책 뉴스만 있음
MOU만 있음
지정학 headline만 있음
자원 매장 가능성만 있음
소비쿠폰·재정지출만 있음
정부 지원 package만 있음
세제안·관세안 등 policy surprise를 무시함
```

## 4B 조기감지 조건

```text
4B-watch:
뉴스 발표일 장중 상한가/급등
정책·MOU·자원발견 테마주 동반 급등
지원 package 발표 후 후발주 급등
소비쿠폰 뉴스로 local-consumption basket 급등
자원발견 발표 후 commerciality 전 +20~30% 급등
trade deal / governance reform으로 저PBR basket 동반 과열

4B-elevated:
후속 공시 없이 가격만 유지
정부 예산/financing이 불명확
시추/검증/재현 결과가 나오기 전 valuation 확장
정책 기대가 기업 이익보다 먼저 반영
```

## 4C hard gate 조건

```text
정책 후퇴
세제 shock
시추 실패
경제성 부재
MOU 불발
예산 미반영
관세 재상승
FX outflow shock
funding failure
FID delay
project cancellation
regulatory reversal
policy-induced capex loss
```

이번 R11 Loop 9에서는 hard 4C를 억지로 확정하지 않는다. 다만 `tax_policy_shock`, `policy_induced_capex_failure`, `FX_outflow_pressure`, `resource_event_without_commerciality`는 강한 4C-watch로 둔다.

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

## docs/round/round_156.md 요약

```md
# R11 Loop 9. Policy / Geopolitical / Disaster / Event Price Validation

이번 라운드는 R11 Loop 9 price-validation 라운드다.

핵심 결론:
- Commercial Act reform은 positive market-structure Stage 2다. KOSPI +1.34%, 3,116.27 anchor가 있고, treasury shares must be cancelled within one year rule도 추가됐다. 하지만 회사별 Stage 3는 실제 소각·배당·ROE/EPS 확인 후다.
- Tax-policy proposal shock은 KOSPI -3.9%를 만들었다. CGT threshold 5B won → 1B won, transaction tax 15bp → 20bp proposal은 policy-confidence 4C-watch다.
- U.S.-Korea trade deal은 tariff 25% → 15% relief지만, BOK는 growth hit -0.45pp in 2025 and -0.60pp in 2026을 봤다. $350B U.S. investment pledge also creates FX outflow watch.
- Hyundai Steel’s $6B U.S. plant plan is a policy-induced capex watch. Shares fell more than 21% after announcement due to funding uncertainty and tariff-strategy doubts.
- Semiconductor support package increased 26T → 33T won and chip finance 17T → 20T won. This is policy Stage 2, not company Green.
- Fiscal stimulus / vouchers are domestic-demand Stage 1/2. 31.8T won stimulus and 150k~500k vouchers need retail same-store sales and margin conversion before Green.
- POSCO International Alaska LNG offtake is stronger than headline policy: 1 mtpa for 20 years, total 20 mt LNG. But FID, pricing, margin and cashflow are required before Green.
- Korea Gas East Sea resource event remains price_moved_without_evidence: Korea Gas +30% to 38,700 won before drilling/commerciality, with 20% success rate and possible 1T won drilling cost.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 156 R11 Loop 9 Policy Geopolitical Event Price Validation

## 반영 내용
- R11 Loop 9 price-validation 라운드를 추가했다.
- Governance reform, tax-policy shock, U.S.-Korea tariff deal, policy-induced capex, semiconductor support, fiscal stimulus, LNG offtake, domestic resource discovery event를 비교했다.
- Reuters/FT/WSJ/MarketWatch reported anchors로 가능한 MFE/MAE 및 policy/contract/macro metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- funded policy, actual contract/budget, shareholder-rights reform, long-term offtake, policy-to-revenue bridge 가중치 강화
- policy news-only, tax surprise, resource estimate without commerciality, policy-induced capex without funding, macro FX outflow risk 감점 강화
- R11 기본 Stage 3 bias를 very conservative로 유지
```

## case row 초안

```jsonl
{"case_id":"r11_loop9_commercial_act_valueup_reform","symbol":"KOSPI/valueup_basket","company_name":"Commercial Act / value-up reform","case_type":"success_candidate","primary_archetype":"GOVERNANCE_REFORM_VALUEUP_POLICY","stage1_date":"2025-07-03","stage2_date":"2025-08-25/2026-02-25","price_validation":{"price_data_source":"Reuters/FT market-structure anchors","stage3_price":null,"kospi_close_2025_07_03":3116.27,"kospi_event_return_pct":1.34,"treasury_share_cancellation_rule":"newly acquired treasury shares must be cancelled within one year","price_validation_status":"market_structure_anchor_not_company_ohlc"},"score_price_alignment":"success_candidate","rerating_result":"market_structure_valueup_watch","notes":"Positive market-structure Stage 2; company Green requires actual cancellation, payout, ROE/EPS and price path."}
{"case_id":"r11_loop9_tax_policy_market_shock","symbol":"KOSPI/tax_sensitive_basket","company_name":"Tax-policy shock","case_type":"4c_watch","primary_archetype":"TAX_POLICY_MARKET_SHOCK","stage4c_date":"2025-08-01","price_validation":{"price_data_source":"MarketWatch reported market-return and tax-policy anchor","stage3_price":null,"kospi_event_mae_pct":-3.9,"capital_gains_threshold_before_krw_bn":5.0,"capital_gains_threshold_after_krw_bn":1.0,"threshold_reduction_pct":-80,"transaction_tax_before_bp":15,"transaction_tax_after_bp":20,"transaction_tax_increase_pct":33.3,"petition_signatures":42000,"petition_review_threshold":50000,"price_validation_status":"reported_market_anchor_not_company_ohlc"},"score_price_alignment":"macro_policy_shock","rerating_result":"tax_policy_confidence_break_watch","notes":"Tax surprise is 4C-watch against value-up momentum; no company Green."}
{"case_id":"r11_loop9_us_korea_trade_tariff_fx_watch","symbol":"auto_steel_shipbuilding_exporters","company_name":"U.S.-Korea trade/tariff deal","case_type":"success_candidate","primary_archetype":"US_KOREA_TARIFF_TRADE_DEAL","stage2_date":"2025-10-29/2025-12-01","stage4c_date":"macro_fx_watch","price_validation":{"price_data_source":"Reuters/FT macro-trade anchors","stage3_price":null,"tariff_before_pct":25,"tariff_after_pct":15,"tariff_reduction_pct":-40,"average_tariff_vs_prior_fta_pct":15,"bok_growth_hit_2025_pp":-0.45,"bok_growth_hit_2026_pp":-0.60,"us_investment_pledge_usd_bn":350,"annual_dollar_outflow_limit_usd_bn":20,"foreign_exchange_bond_cap_2026_usd_bn":5,"foreign_exchange_bond_cap_2025_usd_bn":3.5,"bond_cap_increase_pct":42.9,"won_reaction_pct":0.54,"price_validation_status":"macro_anchor_not_company_ohlc"},"score_price_alignment":"success_candidate_macro_4c_watch","rerating_result":"tariff_relief_but_fx_outflow_watch","notes":"Tariff relief is Stage 2; company Green requires margin recovery, FCF and EPS confirmation. $350B pledge creates FX-outflow watch."}
{"case_id":"r11_loop9_hyundai_steel_us_capex_tariff_strategy_fail","symbol":"004020","company_name":"Hyundai Steel","case_type":"failed_rerating","primary_archetype":"POLICY_INDUCED_CAPEX_TARIFF_HEDGE","stage4c_date":"2025-04-22","price_validation":{"price_data_source":"Reuters policy-induced capex / market-reaction anchor","stage3_price":null,"us_plant_investment_usd_bn":6,"hyundai_motor_group_us_package_usd_bn":21,"reported_share_drop_after_announcement_pct":-21,"funding_plan":"half_borrowing_possible_posco_equity","policy_goal":"tariff_mitigation","price_validation_status":"reported_event_return_not_full_ohlc"},"score_price_alignment":"false_positive_score_prevention","rerating_result":"policy_capex_without_funding_failed","notes":"Tariff hedge capex without funding/margin clarity is 4C-watch, not Green."}
{"case_id":"r11_loop9_semiconductor_support_package","symbol":"005930/000660/semiconductor_basket","company_name":"Semiconductor support package","case_type":"success_candidate","primary_archetype":"SEMICONDUCTOR_POLICY_SUPPORT","stage2_date":"2025-04-15","price_validation":{"price_data_source":"Reuters policy-support anchor","stage3_price":null,"support_package_before_krw_trn":26,"support_package_after_krw_trn":33,"support_package_increase_pct":26.9,"financial_assistance_before_krw_trn":17,"financial_assistance_after_krw_trn":20,"financial_assistance_increase_pct":17.6,"semiconductor_export_value_2024_usd_bn":141.9,"semiconductor_share_exports_2024_pct":21,"price_validation_status":"policy_anchor_company_ohlc_unavailable"},"score_price_alignment":"success_candidate","rerating_result":"semiconductor_policy_support_watch","notes":"Policy support is Stage 2; company Green requires order, margin, EPS/FCF and price-path confirmation."}
{"case_id":"r11_loop9_fiscal_stimulus_voucher_event","symbol":"domestic_consumption_basket","company_name":"Fiscal stimulus / consumer vouchers","case_type":"event_premium","primary_archetype":"FISCAL_STIMULUS_CONSUMPTION_EVENT","stage1_date":"2025-06-19","stage2_date":"2025-07-07","price_validation":{"price_data_source":"Reuters/WSJ fiscal-policy anchors","stage3_price":null,"supplementary_budget_initial_krw_trn":30.5,"approved_stimulus_krw_trn":31.8,"increase_vs_initial_pct":4.3,"growth_spending_krw_trn":20.2,"tax_shortfall_makeup_krw_trn":10.3,"voucher_program_krw_trn":10.3,"voucher_amount_krw":"150000-500000","most_people_voucher_krw":250000,"eligible_recipients_mn":51,"share_receiving_250k_pct":84,"treasury_bond_financing_krw_trn":19.8,"fiscal_deficit_gdp_pct":4.2,"government_debt_gdp_pct":"49.0-49.1","price_validation_status":"policy_anchor_sector_ohlc_unavailable"},"score_price_alignment":"event_premium_policy_support","rerating_result":"domestic_demand_policy_watch","notes":"Consumption stimulus is Stage 1/2; company Green requires same-store sales, margin and FCF conversion."}
{"case_id":"r11_loop9_posco_international_alaska_lng_offtake","symbol":"047050","company_name":"POSCO International","case_type":"success_candidate","primary_archetype":"ENERGY_SECURITY_LONG_TERM_OFFTAKE","stage2_date":"2025-12-04","price_validation":{"price_data_source":"Reuters LNG offtake/project anchor","stage3_price":null,"lng_supply_volume_mtpa":1,"contract_duration_years":20,"total_contract_volume_mt":20,"pipeline_length_miles":807,"preliminary_commitments_secured_mtpa":11,"fid_status":"not_yet_planned_before_year_end","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"energy_security_offtake_watch","notes":"Actual long-term LNG offtake is Stage 2; FID, pricing, margin, steel supply economics and FCF required for Green."}
{"case_id":"r11_loop9_kogas_east_sea_resource_event","symbol":"036460","company_name":"Korea Gas / East Sea resource event","case_type":"event_premium","primary_archetype":"DOMESTIC_RESOURCE_DISCOVERY_EVENT","stage1_date":"2024-06-03","stage4b_date":"2024-06-03","price_validation":{"price_data_source":"Reuters/WSJ price and exploration anchors","stage3_price":null,"kogas_event_peak_price":38700,"kogas_event_mfe_1d_pct":30,"implied_pre_event_reference_price":29769,"daesung_energy_event_mfe_pct":30,"sk_innovation_event_mfe_pct":6,"sk_gas_event_mfe_pct":7,"resource_possibility_bbl_bn":14,"success_rate_pct":20,"failure_probability_pct":80,"drilling_cost_per_well_krw_bn":100,"possible_wells":10,"possible_total_drilling_cost_krw_trn":1,"commercial_production_target_year":2035,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"resource_discovery_event_premium","notes":"Resource estimate and drilling approval are Stage 1; commerciality and revenue conversion required for Stage 3."}
```

## shadow weight row 초안

```csv
archetype,actual_contract_or_budget,funded_policy,policy_to_revenue_bridge,shareholder_rights_reform,long_term_offtake,financing_or_fid,macro_fx_risk,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
GOVERNANCE_REFORM_VALUEUP_POLICY,+3,+4,+3,+5,+0,+0,+1,-2,+4,+3,Commercial Act reform is market-structure Stage 2, not company Green.
TAX_POLICY_MARKET_SHOCK,+0,+0,+0,+0,+0,+0,+3,-5,+3,+5,Tax-policy surprise can break value-up confidence.
US_KOREA_TARIFF_TRADE_DEAL,+4,+4,+4,+0,+0,+3,+5,-3,+4,+4,Tariff relief is Stage 2 but FX outflow and growth shock remain.
POLICY_INDUCED_CAPEX_TARIFF_HEDGE,+2,+2,+3,+0,+0,+5,+3,-5,+4,+4,Hyundai Steel shows capex without funding/margin clarity can fail.
SEMICONDUCTOR_POLICY_SUPPORT,+3,+5,+4,+0,+0,+3,+1,-3,+4,+3,Chip support is Stage 2; company orders/margins/EPS required.
FISCAL_STIMULUS_CONSUMPTION_EVENT,+2,+5,+3,+0,+0,+0,+2,-4,+5,+3,Vouchers are Stage 1/2; retail Green requires sales/margin conversion.
ENERGY_SECURITY_LONG_TERM_OFFTAKE,+5,+3,+5,+0,+5,+5,+2,-2,+3,+4,POSCO Alaska LNG offtake is Stage 2; FID/margin/cashflow required.
DOMESTIC_RESOURCE_DISCOVERY_EVENT,+0,+0,+0,+0,+0,+0,+2,-5,+5,+5,Korea Gas +30% before drilling/commerciality is price_moved_without_evidence.
```

---

# 이번 R11 Loop 9 결론

R11은 거의 항상 Stage 3를 보류해야 한다.

```text
1. Commercial Act 개혁은 긍정적인 market-structure Stage 2다.
   하지만 회사별 실제 소각·배당·ROE/EPS 전 Green은 아니다.

2. 세제안 shock은 value-up momentum을 꺾는 4C-watch다.
   KOSPI -3.9%가 정책 신뢰 훼손을 보여준다.

3. 한미 관세 deal은 25%→15% relief지만,
   BOK 성장률 충격과 $350B 투자 pledge에 따른 FX outflow watch가 남는다.

4. 현대제철의 미국 CAPEX는 tariff hedge처럼 보였지만,
   funding·마진 불확실성 때문에 실패한 policy-induced capex case다.

5. 반도체 33조 지원은 Stage 2 policy support다.
   하지만 개별 기업 Stage 3는 주문·마진·EPS/FCF로만 준다.

6. 소비쿠폰·추경은 domestic-demand event다.
   실제 same-store sales와 margin 전에는 소비주 Green 금지다.

7. POSCO International의 Alaska LNG 20년 offtake는 강한 Stage 2다.
   그래도 FID·pricing·margin·cashflow 전에는 Stage 3가 아니다.

8. 한국가스공사 East Sea 이벤트는 R11의 대표적 price_moved_without_evidence다.
   시추·경제성·상업성 전 +30%는 Green이 아니라 4B/event premium이다.
```

한 문장으로 압축하면:

> **R11에서 진짜 Stage 3는 “정책·지정학·재난 뉴스가 크다”가 아니라, 그 뉴스가 계약·예산·financing·발주·매출·EPS/FCF로 승격되는 순간이다.**
> **R11의 기본값은 Green이 아니라 Event Premium이며, 가격이 먼저 뛴 경우 4B-watch를 가장 빨리 붙여야 한다.**

[1]: https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-assembly-passes-commerce-bill-expanding-duty-boards-shareholders-2025-07-03/?utm_source=chatgpt.com "South Korea assembly passes commerce bill expanding duty of boards to shareholders"
[2]: https://www.marketwatch.com/story/south-koreas-new-tax-proposals-derail-one-of-the-worlds-best-performing-stock-markets-of-2025-9432538d?utm_source=chatgpt.com "South Korea's new tax proposals derail one of the world's best performing stock markets of 2025."
[3]: https://www.reuters.com/business/autos-transportation/bank-korea-expects-significant-economic-shock-even-after-us-trade-deal-2025-08-28/?utm_source=chatgpt.com "Bank of Korea expects 'significant' economic shock even after US trade deal"
[4]: https://www.reuters.com/business/autos-transportation/hyundai-steels-6-bln-us-investment-draws-investor-ire-tests-seouls-tariff-2025-04-22/?utm_source=chatgpt.com "Hyundai Steel's $6 billion US investment draws investor ire, tests Seoul's tariff strategy"
[5]: https://www.reuters.com/technology/south-korea-unveils-23-billion-support-package-chips-amid-us-tariff-uncertainty-2025-04-14/?utm_source=chatgpt.com "South Korea unveils $23 billion support package for chips amid US tariff uncertainty"
[6]: https://www.reuters.com/world/asia-pacific/south-korea-drafts-second-extra-budget-new-leader-seeks-spur-growth-2025-06-19/?utm_source=chatgpt.com "South Korea drafts second extra budget as new leader seeks to spur growth"
[7]: https://www.reuters.com/business/energy/glenfarne-finalizes-20-year-lng-supply-deal-with-south-koreas-posco-2025-12-04/?utm_source=chatgpt.com "Glenfarne finalizes 20-year LNG supply deal with South Korea's POSCO"
[8]: https://www.reuters.com/world/asia-pacific/skoreas-yoon-says-vast-amount-oil-gas-reserve-possible-off-east-coast-2024-06-03/?utm_source=chatgpt.com "South Korea's Yoon approves exploration of vast oil and gas prospects"

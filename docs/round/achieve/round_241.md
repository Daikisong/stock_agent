순서상 이번은 **R11 Loop 10 — 정책·지정학·재난·이벤트 가격경로 검증 라운드**다.

이번 R11은 **정치 신뢰 shock, 시장구조 개혁, WGBI 편입, short-selling 정상화, AI dividend/tax 논란, Hormuz 에너지 shock, FX 유동성 대응, stablecoin/해외투자 자본유출**을 같이 본다.

```text
round = R11 Loop 10
round_id = round_169
large_sector = POLICY_GEOPOLITICAL_DISASTER_EVENT
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true
```

이번 환경에서는 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉 OHLC를 안정적으로 직접 확보하지 못했다. 대신 Reuters / FT / Barron’s / MarketWatch가 제공한 **지수 수익률, 섹터 수익률, 환율, 정책금액, 외국인 순매수, 예상 자금유입, shock 수치**로 계산 가능한 값만 계산했다.

---

# 1. 이번 라운드 대섹터

```text
R11 = 정책·지정학·재난·이벤트
```

R11의 Stage 3는 “정책이 좋다”, “이벤트가 크다”, “테마가 생겼다”가 아니다. **정책·지정학·재난 이벤트가 실제 계약·예산·수익·세금·자본유입·EPS/FCF로 내려오는 순간**이다.

---

# 2. 대상 canonical archetype

```text
POLITICAL_INSTITUTIONAL_TRUST_BREAK
MARKET_STRUCTURE_REFORM
GLOBAL_INDEX_INCLUSION
SHORT_SELLING_NORMALIZATION
AI_WINDFALL_TAX_POLICY_SHOCK
GEOPOLITICAL_ENERGY_SUPPLY_SHOCK
FX_LIQUIDITY_POLICY_RESPONSE
STABLECOIN_AND_OVERSEAS_OUTFLOW_MACRO
POLICY_CONFIDENCE_EVENT_PREMIUM
PRICE_ONLY_RALLY
MACRO_HARD_4C
```

---

# 3. deep sub-archetype

```text
정치·제도 신뢰:
- martial law crisis
- impeachment / acting president chain
- Korea discount risk premium
- won / KOSPI shock
- foreign investor confidence

시장구조:
- WGBI inclusion
- MSCI developed-market access
- short-selling ban lift
- illegal short-selling detection system
- one-strike-out unfair trading policy

AI windfall / tax:
- AI dividend / citizen dividend
- chip tax revenue
- AI profit redistribution fear
- Samsung / SK Hynix / KOSPI drawdown

지정학·에너지:
- Iran / Hormuz conflict
- South Korea oil import dependency
- KOSPI circuit breaker
- won 17-year low
- auto / chip / exporter shock

FX / capital flow:
- kimchi bond deregulation
- WGBI inflow
- $350B U.S. investment pledge
- foreign bond cap
- retail U.S. stock buying
- dollar-backed stablecoin frenzy
```

---

# 4. 국장 신규 후보 case

## Case A — Martial law political shock `macro 4C-watch / institutional trust break`

```text
symbol = KOSPI / KRW / Korea risk premium
case_type = 4C-watch
archetype = POLITICAL_INSTITUTIONAL_TRUST_BREAK
```

### stage date

```text
Stage 1:
2024-12-03 night
- President Yoon declares emergency martial law
- political/institutional trust shock

Stage 2:
없음
- 정치 shock은 positive stage가 아니라 RedTeam input

Stage 3:
없음

Stage 4C-watch:
2024-12-04
- Korean shares drop nearly 2%
- won hits two-year low
- Korea discount risk premium rises
```

Reuters는 2024년 12월 4일, 윤석열 대통령의 계엄 선포와 철회 이후 한국 자산이 매도 압력을 받았고, 원화가 2년 저점까지 밀렸으며 KOSPI가 거의 2% 하락했다고 보도했다. 이는 기업 실적 이벤트가 아니라 **institutional trust shock**이다. R11에서는 이런 이벤트를 hard 4C로 바로 확정하기보다는, 시장 시스템이 빠르게 정상화됐는지와 외국인 자금 이탈이 구조화됐는지를 따지는 `macro 4C-watch`로 둔다. ([Reuters][1])

### 실제 가격경로 검증

```text
price_data_source:
Reuters political-crisis / market-reaction anchor

stage3_price:
N/A

KOSPI_event_MAE:
nearly -2%

KRW_status:
two-year low

ETF / individual Korean-stock OHLC:
price_data_unavailable_after_deep_search

reason:
- Reuters provides market-level reaction, not raw adjusted OHLC for each Korean stock.
- KRX/Naver/Yahoo/Stooq raw daily OHLC unavailable in this pass.

Stage 4C 큰 하락 이전 포착 여부:
partial_success
- martial law declaration itself is the trigger.
- the market-level shock was immediately observable.
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = institutional_trust_break_watch
stage_failure_type = macro_4C_watch_not_company_green
```

---

## Case B — WGBI inclusion `success_candidate / market-structure Stage 2`

```text
symbol = Korean government bonds / KRW / Korea asset market
case_type = success_candidate
archetype = GLOBAL_INDEX_INCLUSION / MARKET_STRUCTURE_REFORM
```

### stage date

```text
Stage 1:
2024-10-08
- FTSE Russell adds South Korea government bonds to WGBI
- global fixed-income index inclusion
- Korea market-access reform validation

Stage 2:
2025-11부터 단계적 편입
- WGBI weight 2.22%
- inclusion phased over one year
- expected inflows up to 80T won / about $59.7B

Stage 3:
없음
- market-structure positive지만 개별 종목 Green 아님
- 실제 외국인 채권 유입, 금리 안정, FX 안정, 기업 자금조달비용 개선 확인 필요

Stage 4B:
index-inclusion 기대만으로 금융·증권·저PBR주가 먼저 급등하면 후보

Stage 4C:
Euroclear settlement volume 부족, FX 접근성 문제, MSCI upgrade 지연, 외국인 flow 부재 시 후보
```

South Korea의 WGBI 편입은 R11에서 명확한 **market-structure Stage 2**다. Reuters는 정부가 최대 80조 원, 약 597억 달러의 유입을 예상했고, FTSE Russell 기준 한국 국채가 WGBI에서 2.22% 비중을 차지하며 2025년 11월부터 1년간 분기별로 편입될 예정이라고 보도했다. 하지만 이것은 개별 주식 Stage 3가 아니다. 실제 외국인 채권 유입, 금리 안정, 원화 안정, 기업 자금조달비용 개선까지 내려와야 한다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters WGBI inclusion anchors

stage3_price:
N/A

expected_inflows:
80T won / $59.7B

WGBI_weight:
2.22%

inclusion_start:
2025-11

phase_in_period:
one year, quarterly basis

bond_market_size_context:
$2.2T bond market

KOSPI_2024_context_before_inclusion:
-2.3% YTD, underperforming S&P 500 and Nikkei

MFE / MAE:
price_data_unavailable_after_deep_search

reason:
- Source provides index-inclusion and inflow metrics, not individual-stock OHLC.
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = market_structure_bond_inflow_watch
stage_failure_type = stage2_market_structure_not_company_green
```

---

## Case C — Short-selling ban lift / unfair-trading crackdown `success_candidate / market-access Stage 2`

```text
symbol = KOSPI / KOSDAQ / brokerages / foreign-access-sensitive basket
case_type = success_candidate
archetype = SHORT_SELLING_NORMALIZATION / MARKET_STRUCTURE_REFORM
```

### stage date

```text
Stage 1:
2025-03
- South Korea lifts full market-wide short-selling ban for first time in five years
- illegal short-selling detection system prepared
- MSCI developed-market accessibility issue partially resolved

Stage 2:
2025-04-21
- regulator says high chance of MSCI developed-market inclusion
- over 90% of MSCI issues addressed
- short-selling ban lift is key market-access evidence

추가 Stage 2:
2025-07-09
- one-strike-out policy against unfair trading
- severe penalties up to 100% of short-sale orders
- listing criteria tightening planned

Stage 3:
없음
- 시장구조 개선은 Stage 2
- 실제 MSCI watchlist/inclusion, foreign flow, valuation uplift 확인 필요

Stage 4B:
MSCI upgrade 기대로 증권·저PBR·외국인수급 basket이 먼저 급등하면 후보

Stage 4C:
불법 공매도 재발, 외국인 접근성 실망, MSCI upgrade 지연, 시장 신뢰 훼손 시 후보
```

Reuters는 한국이 2025년 3월 5년 만에 공매도 전면 금지를 해제했고, 이는 MSCI가 지적해온 market-access 문제를 해결하는 핵심 요소였다고 보도했다. 2025년 4월 금융당국자는 MSCI 선진시장 편입 가능성이 높다고 말했고, MSCI가 지적한 문제의 90% 이상이 해결됐다고 설명했다. 2025년 7월에는 불공정거래와 불법 공매도에 대해 `one-strike-out` 방식의 강한 제재 방안도 나왔다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters market-access / short-selling reform anchors

stage3_price:
N/A

short_selling_ban_lift:
2025-03

ban_duration:
first full market-wide lift in five years

MSCI_issue_resolution:
over 90%

penalty_for_serious_short_sale_violation:
up to 100% of short-sale orders

direct_sector_OHLC:
price_data_unavailable_after_deep_search

reason:
- Reuters provides reform details but not full OHLC path for securities/brokerage basket.
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = MSCI_market_access_watch
stage_failure_type = stage2_market_structure_not_green
```

---

## Case D — AI dividend / AI windfall tax shock `4C-watch / policy confidence break`

```text
symbol = KOSPI / Samsung / SK Hynix / AI semiconductor basket
case_type = 4C-watch / policy_confidence_break
archetype = AI_WINDFALL_TAX_POLICY_SHOCK
```

### stage date

```text
Stage 1:
2026-05-12
- presidential policy chief suggests AI/citizen dividend idea
- market interprets as possible redistribution of AI windfall
- later clarification: excess tax revenue, not corporate profit tax

Stage 2:
없음
- redistribution/tax fear는 positive evidence가 아니라 RedTeam input

Stage 3:
없음

Stage 4C-watch:
2026-05-12
- KOSPI falls as much as 5.1%
- closes -2.3%
- AI semiconductor leaders sell off
```

이 이벤트는 다이키가 말했던 “AI 배당금” 논의와 정확히 맞물린다. FT는 대통령 정책실장 김용범이 AI·반도체 호황에서 나오는 초과 세수를 국민에게 배당처럼 돌려주는 아이디어를 언급했고, 이후 기업이익 자체를 과세하자는 뜻이 아니라 초과 세수 활용을 말한 것이라고 해명했다고 보도했다. MarketWatch와 Barron’s는 이 발언 이후 KOSPI가 장중 5% 안팎까지 밀리고, 종가 기준 2.3% 하락했다고 보도했다. R11에서는 이것을 “새로운 사회계약” 후보로 보되, 주식 점수표에서는 **policy-confidence 4C-watch**로 처리한다. ([Financial Times][4])

### 실제 가격경로 검증

```text
price_data_source:
FT / Barron's / MarketWatch policy-shock anchors

stage3_price:
N/A

KOSPI_intraday_MAE:
-5.1% approximately

KOSPI_close_MAE:
-2.3%

policy_claim_initial_market_read:
AI windfall redistribution / possible tax concern

clarification:
excess tax revenue, not direct corporate-profit windfall tax

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4C 큰 하락 이전 포착 여부:
partial_success
- policy statement itself triggered the shock.
- if such language appears again, 4C-watch should be immediate.
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = AI_windfall_tax_policy_confidence_break
stage_failure_type = 4C_watch_not_hard_4C
```

---

## Case E — Hormuz / Iran conflict `macro hard 4C / energy-security shock`

```text
symbol = KOSPI / KRW / exporters / refiners / airlines / autos / chips
case_type = macro hard 4C
archetype = GEOPOLITICAL_ENERGY_SUPPLY_SHOCK
```

### stage date

```text
Stage 1:
2026-03-04
- Iran / U.S.-Israel conflict escalates
- Strait of Hormuz disruption
- South Korea oil-import dependency exposed

Stage 2:
없음

Stage 3:
없음

Stage 4C:
2026-03-04
- KOSPI -12.06%, largest single-day drop
- close 5,093.54
- market cap wiped out $553.82B over two days
- won touches 17-year low at 1,505.8/USD
- Hyundai Motor -15.8%
- Samsung Electronics -11.7%
- SK Hynix -9.6%
```

Reuters는 2026년 3월 4일, 이란 분쟁과 Hormuz 불안으로 한국 증시가 사상 최악의 하루를 겪었다고 보도했다. KOSPI는 12.06% 하락해 5,093.54로 마감했고, 이틀 동안 시총 5,538억 달러가 증발했다. 원화는 달러당 1,505.8까지 밀려 17년 저점을 찍었다. South Korea는 중동 원유 의존도가 약 70%라서, 이건 단순 지정학 뉴스가 아니라 **macro hard 4C**다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters geopolitical energy-shock / market-return anchor

stage3_price:
N/A

KOSPI_event_MAE:
-12.06%

KOSPI_close:
5,093.54

market_cap_wipeout_2D:
$553.82B

KRW_intraday_low:
1,505.8 per USD

KRW_close:
1,485.7 per USD

Hyundai_Motor_MAE:
-15.8%

Samsung_Electronics_MAE:
-11.7%

SK_Hynix_MAE:
-9.6%

oil_import_dependency:
about 70% of oil imports from Middle East

MFE:
N/A

Stage 4C 큰 하락 이전 포착 여부:
hard event
- actual geopolitical shock was the trigger.
- future early warning should come from Hormuz tension, oil shock, KRW weakness, and KOSPI circuit-breaker risk.
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = geopolitical_energy_security_hard_4C
stage_failure_type = macro_hard_4C
```

---

## Case F — Hormuz supply-security policy response `success_candidate / policy relief, not Green`

```text
symbol = refiners / LNG / shipping / defense / energy-security basket
case_type = success_candidate + policy_relief
archetype = GEOPOLITICAL_ENERGY_SUPPLY_SHOCK / POLICY_RELIEF_RESPONSE
```

### stage date

```text
Stage 1:
2026-04-06
- Lee Jae Myung says Korea must balance risk as Hormuz disruptions threaten oil supplies
- Korea explores alternative routes and suppliers
- Saudi Arabia / Oman / Algeria discussions
- strategic oil reserves and Red Sea vessel deployment considered

Stage 2:
2026-05-12
- Korea considers phased role in Hormuz maritime security after U.S. talks
- political support / personnel / information sharing / assets possible
- no troop expansion yet

Stage 3:
없음
- policy response는 relief
- 실제 oil-cost stabilization, LNG supply, refinery margin, shipping risk premium 완화 확인 전 Green 금지

Stage 4B:
energy-security headlines로 정유·해운·방산 basket이 먼저 급등하면 후보

Stage 4C:
Hormuz 재봉쇄, 유가 재급등, LNG disruption, KRW shock, insurance premium spike 시 후보
```

Hormuz shock 이후 한국 정부는 대체 공급처와 경로, 전략비축유, Red Sea 선박 운용, maritime security contribution 등을 검토했다. Reuters는 2026년 4월 Lee Jae Myung 대통령이 Hormuz disruption에 대해 oil supply risk를 균형 있게 관리해야 한다고 말했고, Saudi Arabia·Oman·Algeria와 공급망 논의를 추진했다고 보도했다. 5월에는 Washington에서 한국이 Hormuz maritime security에 정치적 지원, 정보공유, 인력, 자산 제공 등을 단계적으로 검토한다고 밝혔다. 이것은 Stage 2 relief이지 Green이 아니다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters energy-security policy-response anchors

stage3_price:
N/A

policy_tools_discussed:
alternative routes/suppliers
Saudi Arabia / Oman / Algeria talks
strategic oil reserves
five Korean vessels via Red Sea
Hormuz maritime security support

market_OHLC:
price_data_unavailable_after_deep_search

reason:
- Reuters provides policy-response details, not individual sector OHLC path.
```

### alignment

```text
score_price_alignment = success_candidate_policy_relief
rerating_result = energy_security_policy_response_watch
stage_failure_type = stage2_relief_not_green
```

---

## Case G — Kimchi bond / FX liquidity deregulation `success_candidate / FX policy Stage 2`

```text
symbol = KRW / banks / brokers / exporters / FX-sensitive basket
case_type = success_candidate
archetype = FX_LIQUIDITY_POLICY_RESPONSE
```

### stage date

```text
Stage 1:
2024-12-20
- won at 15-year low
- authorities loosen FX regulations
- allow more corporate foreign-currency borrowing
- FX futures ceiling raised

Stage 2:
2025-06-30
- 14-year kimchi bond investment ban lifted
- dollar-backed stablecoin / overseas-stock outflow strains FX liquidity
- won rises to 1,347/USD before stabilizing near 1,353/USD
- Q1 stablecoin trading 57T won / $42B

Stage 3:
없음
- FX liquidity policy는 macro Stage 2
- 실제 KRW stabilization, funding-cost relief, foreign inflow 확인 전 Green 금지

Stage 4B:
FX policy relief로 banks/brokers/exporters가 먼저 rerating되면 후보

Stage 4C:
retail overseas outflow 확대, stablecoin dollarization, KRW 1,500 재돌파, hedging failure 시 후보
```

FT는 2025년 6월 한국이 14년 만에 kimchi bond 투자 금지를 해제했다고 보도했다. 배경은 한국 개인투자자의 해외주식과 달러-backed stablecoin 거래 급증으로, Q1 stablecoin 거래가 57조 원, 약 420억 달러에 달해 FX 유동성 압박을 키웠기 때문이다. 조치 이후 원화는 달러당 1,347까지 강해졌다가 1,353 부근에서 안정됐다고 보도됐다. Reuters도 2024년 12월 원화가 15년 저점에 있을 때, 기업의 외화차입과 선물환 한도 완화를 통해 FX 유동성을 보강하려 했다고 전했다. ([Financial Times][7])

### 실제 가격경로 검증

```text
price_data_source:
FT / Reuters FX-policy anchors

stage3_price:
N/A

Q1_stablecoin_trading:
57T won / $42B

KRW_strength_after_policy:
1,347 per USD

KRW_stabilization_level:
around 1,353 per USD

FX_futures_ceiling_local_banks:
50% → 75% of capital holdings

FX_futures_ceiling_foreign_bank_branches:
250% → 375%

local_bank_ceiling_increase:
75 / 50 - 1
= +50%

foreign_branch_ceiling_increase:
375 / 250 - 1
= +50%

MFE / MAE:
price_data_unavailable_after_deep_search

reason:
- sources provide FX-policy and currency anchors, not equity OHLC.
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = FX_liquidity_policy_watch
stage_failure_type = stage2_macro_relief_not_company_green
```

---

## Case H — $350B U.S. investment / foreign-bond cap `macro 4C-watch + relief`

```text
symbol = KRW / exporters / banks / FX-sensitive basket
case_type = macro_4C_watch + policy_relief
archetype = FX_OUTFLOW_TRADE_DEAL_OVERLAY
```

### stage date

```text
Stage 1:
2025-12
- Korea prepares for $350B U.S. investment pledge under trade deal
- tariff relief but dollar outflow risk
- won pressure

Stage 2:
2025-12-03
- foreign exchange bond issuance cap raised to record $5B for 2026
- 2025 cap was $3.5B
- annual U.S. dollar outflow limit agreed at $20B
- retail investors bought record net $30B U.S. stocks in 2025

Stage 3:
없음
- FX bond cap는 policy relief
- actual KRW stabilization / FX reserves / exporter margin 확인 전 Green 금지

Stage 4C:
U.S. investment pledge creates structural dollar outflow
- won down 8% since end-June
- retail U.S. stock holdings record $160B
```

FT는 한국이 미국과의 trade deal에 따른 3,500억 달러 투자 약속을 준비하면서 2026년 외평채 발행 한도를 50억 달러로 높였다고 보도했다. 2025년 한도 35억 달러보다 42.9% 높은 수준이다. 동시에 한국 개인투자자들은 2025년에 미국 주식을 순매수 300억 달러어치 사들였고, 미국 주식 보유액은 1,600억 달러까지 늘었다. 이는 tariff relief와 동시에 **FX outflow 4C-watch**다. ([Financial Times][8])

### 실제 가격경로 검증

```text
price_data_source:
FT FX-bond / capital-outflow anchor

stage3_price:
N/A

U.S._investment_pledge:
$350B

annual_dollar_outflow_limit:
$20B

FX_bond_cap_2026:
$5B

FX_bond_cap_2025:
$3.5B

cap_increase:
5 / 3.5 - 1
= +42.9%

KRW_decline_since_end_June:
-8%

retail_US_stock_net_buy_2025:
$30B

retail_US_stock_holdings:
$160B

FX_reserves_context:
$430.7B

MFE / MAE:
price_data_unavailable_after_deep_search

reason:
- source provides FX/capital-flow anchors, not equity OHLC path.
```

### alignment

```text
score_price_alignment = macro_4C_watch + policy_relief
rerating_result = tariff_relief_with_FX_outflow_watch
stage_failure_type = macro_watch_not_green
```

---

# 5. 이번 R11 case별 요약표

| case                          | 분류                |                                                    실제 가격검증 | alignment                 |
| ----------------------------- | ----------------- | ---------------------------------------------------------: | ------------------------- |
| Martial law political shock   | 4C-watch          |                         KOSPI nearly -2%, won two-year low | institutional trust break |
| WGBI inclusion                | success_candidate |                 expected inflow 80T won, WGBI weight 2.22% | market-structure Stage 2  |
| Short-selling normalization   | success_candidate |           five-year ban lifted, >90% MSCI issues addressed | market-access Stage 2     |
| AI dividend/tax shock         | 4C-watch          |                          KOSPI intraday -5.1%, close -2.3% | policy-confidence break   |
| Hormuz/Iran shock             | hard 4C           |             KOSPI -12.06%, won 17-year low, Hyundai -15.8% | macro hard 4C             |
| Hormuz policy response        | policy relief     | alternative suppliers / reserves / maritime role discussed | Stage 2 relief            |
| Kimchi bond / FX liquidity    | success_candidate |                    stablecoin trading 57T, KRW 1,347→1,353 | FX policy Stage 2         |
| $350B U.S. investment outflow | macro 4C-watch    |   FX bond cap $3.5B→$5B, KRW -8%, retail U.S. stocks $160B | FX outflow watch          |

---

# 6. score-price alignment 판정

```text
success_candidate:
- WGBI inclusion
- short-selling normalization / MSCI access reform
- Kimchi bond / FX liquidity deregulation
- Hormuz policy response, 단 relief 성격

event_premium / policy_watch:
- WGBI / MSCI / market-structure 기대
- FX liquidity policy relief
- energy-security policy response

price_moved_without_evidence:
- AI dividend/tax 관련 수혜·피해주가 실질 정책안 없이 움직이는 구간
- WGBI/MSCI 기대만으로 금융·증권주가 과열되는 구간
- energy-security headline만으로 정유·해운·방산주가 먼저 급등하는 구간

thesis_break_watch:
- martial law political shock
- AI dividend/tax policy-confidence shock
- $350B U.S. investment FX outflow risk

hard_4C:
- Hormuz / Iran geopolitical energy shock

4B-watch:
- WGBI/MSCI 기대 rally
- short-selling normalization 기대 rally
- energy-security policy response rally
- FX policy relief rally without actual KRW stabilization
```

---

# 7. 점수비중 교정

## 올릴 축

```text
funded_policy +5
actual_capital_inflow +5
index_inclusion_confirmed +5
market_access_improvement +4
institutional_trust +5
FX_stability +5
energy_security_resilience +5
policy_to_company_revenue_bridge +5
regulatory_clarity +4
```

### 왜 올리나

WGBI 편입은 단순 구호가 아니라 실제 index inclusion이다. 공매도 정상화도 MSCI 접근성 문제를 줄인 market-structure evidence다. 그러나 이 둘은 개별 종목 Green이 아니라, 한국 시장 전체 risk premium을 낮출 수 있는 Stage 2다.

## 내릴 축

```text
policy_speech_only -5
tax_or_redistribution_surprise -5
political_institutional_shock -5
geopolitical_energy_shock -5
capital_outflow_pressure -4
FX_policy_without_flow -4
index_inclusion_expectation_only -3
market_reform_without_foreign_flow -3
event_rally_before_earnings_bridge -5
```

### 왜 내리나

AI dividend/tax shock은 실제 법안이 없어도 KOSPI를 흔들었다. Martial law crisis는 Korea discount risk premium을 즉시 키웠다. Hormuz shock은 한국의 원유 의존성과 환율 취약성을 동시에 찔렀다. R11은 policy speech 자체가 가격을 움직일 수 있기 때문에, 실체 없는 이벤트를 Green으로 올리면 점수표가 바로 오염된다.

## Green gate 강화 조건

```text
R11 Stage 3-Green 필수:
1. 정책이 실제 법안 / 예산 / index inclusion / 계약 / capital inflow로 확정
2. 회사 단위 revenue / EPS / FCF bridge 존재
3. FX / 금리 / credit cost에 긍정적 효과가 확인됨
4. 일회성 headline이 아니라 지속 효과가 있음
5. 정치·제도·규제 신뢰 훼손 없음
6. 가격경로가 evidence 이후 따라옴

금지:
정책 발언만 있음
선거공약만 있음
세금/재분배 surprise
지정학 headline만 있음
WGBI/MSCI 기대만 있음
FX 정책 발표만 있고 실제 flow 없음
energy-security headline만 있음
```

## 4B 조기감지 조건

```text
4B-watch:
WGBI/MSCI 기대만으로 금융·증권주 급등
정책 발언만으로 특정 테마 급등
AI dividend/tax 해명 전후로 AI 반도체 basket 급락·반등
energy-security headline로 정유·해운·방산주 급등
FX policy relief로 은행/수출주가 먼저 rerating
short-selling normalization 기대가 거래대금/증권주에 과도 반영

4B-elevated:
실제 flow 없이 price만 감
정책 디테일이 없는데 테마주가 먼저 감
외국인 flow가 반대로 나감
환율이 안정되지 않음
실적 bridge가 없음
```

## 4C hard gate 조건

```text
martial law / coup-like institutional shock
major political legitimacy crisis
tax or windfall redistribution shock
geopolitical energy chokepoint closure
KOSPI circuit breaker
KRW disorderly depreciation
foreign capital flight
index-inclusion failure
MSCI access disappointment
FX liquidity breakdown
policy reversal
```

이번 R11 Loop 10에서는 **Hormuz/Iran energy shock을 macro hard 4C로 확정**한다. Martial law와 AI dividend/tax는 강한 4C-watch다. 두 이벤트 모두 실제 기업 실적보다 먼저 risk premium을 움직였다.

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

## docs/round/round_169.md 요약

```md
# R11 Loop 10. Policy / Geopolitical / Disaster / Event Price Validation

이번 라운드는 R11 Loop 10 price-validation 라운드다.

핵심 결론:
- Martial law crisis is institutional-trust 4C-watch. Reuters reported Korean shares fell nearly 2% and the won hit a two-year low after the short-lived martial law declaration and reversal.
- WGBI inclusion is market-structure Stage 2. Expected inflows are up to 80T won / $59.7B, WGBI weight 2.22%, with inclusion starting November 2025 over one year.
- Short-selling normalization is market-access Stage 2. Korea lifted its five-year short-selling ban in March 2025 and regulators said over 90% of MSCI issues had been addressed.
- AI dividend / AI windfall-tax talk is policy-confidence 4C-watch. KOSPI fell as much as about 5.1% intraday and closed -2.3% after comments about redistributing AI boom tax revenue were interpreted as windfall-tax risk.
- Hormuz/Iran energy shock is macro hard 4C. KOSPI fell -12.06% to 5,093.54, won touched 1,505.8/USD, Hyundai -15.8%, Samsung -11.7%, SK Hynix -9.6%.
- Hormuz policy response is Stage 2 relief, not Green. Korea discussed alternative suppliers/routes, reserves, Red Sea vessels and phased maritime-security support.
- Kimchi bond / FX liquidity deregulation is FX-policy Stage 2. Dollar-backed stablecoin trading reached 57T won in Q1 2025, and the won strengthened to 1,347/USD before stabilizing around 1,353.
- $350B U.S. investment pledge is tariff relief plus FX-outflow 4C-watch. FX bond cap rose from $3.5B to $5B for 2026, retail U.S. stock holdings reached $160B, and KRW fell 8% since end-June.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 169 R11 Loop 10 Policy Geopolitical Event Price Validation

## 반영 내용
- R11 Loop 10 price-validation 라운드를 추가했다.
- Political institutional shock, WGBI inclusion, short-selling normalization, AI dividend/tax shock, Hormuz hard macro shock, Hormuz policy relief, kimchi bond FX liquidity, U.S. investment FX-outflow watch를 비교했다.
- Reuters/FT/Barron’s/MarketWatch anchors로 가능한 MFE/MAE 및 policy/macro metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- funded policy, actual capital inflow, index inclusion, market access improvement, institutional trust, FX stability, energy-security resilience 가중치 강화
- policy speech-only, tax/redistribution surprise, political institutional shock, geopolitical energy shock, capital outflow pressure 감점 강화
- R11 macro hard 4C와 policy-confidence 4C-watch 민감도 강화
```

## case row 초안

```jsonl
{"case_id":"r11_loop10_martial_law_institutional_trust_shock","symbol":"KOSPI/KRW","company_name":"South Korea political institutional trust shock","case_type":"4c_watch","primary_archetype":"POLITICAL_INSTITUTIONAL_TRUST_BREAK","stage4c_date":"2024-12-04","price_validation":{"price_data_source":"Reuters political-crisis / market-reaction anchor","stage3_price":null,"kospi_event_mae_pct":"nearly -2","krw_status":"two-year low","price_validation_status":"market_level_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"institutional_trust_break_watch","notes":"Martial law crisis is macro 4C-watch; no company Green until institutional risk premium normalizes."}
{"case_id":"r11_loop10_wgbi_inclusion_market_structure","symbol":"Korean_government_bonds/KRW/Korea_assets","company_name":"WGBI inclusion","case_type":"success_candidate","primary_archetype":"GLOBAL_INDEX_INCLUSION","stage2_date":"2024-10-08/2025-11","price_validation":{"price_data_source":"Reuters WGBI inclusion anchors","stage3_price":null,"expected_inflows_krw_trn":80,"expected_inflows_usd_bn":59.7,"wgbi_weight_pct":2.22,"inclusion_start":"2025-11","phase_in_period":"one_year_quarterly","bond_market_size_usd_trn":2.2,"kospi_2024_context_pct":-2.3,"price_validation_status":"market_structure_anchor_not_company_ohlc"},"score_price_alignment":"success_candidate","rerating_result":"market_structure_bond_inflow_watch","notes":"WGBI is Stage 2 market-structure evidence; actual inflows, rates, FX and corporate funding-cost effects required before company Green."}
{"case_id":"r11_loop10_short_selling_mscI_access_reform","symbol":"KOSPI/KOSDAQ/brokerage_foreign_access_basket","company_name":"Short-selling normalization / MSCI access reform","case_type":"success_candidate","primary_archetype":"SHORT_SELLING_NORMALIZATION","stage2_date":"2025-03/2025-04-21/2025-07-09","price_validation":{"price_data_source":"Reuters market-access / short-selling reform anchors","stage3_price":null,"short_selling_ban_lift":"2025-03","ban_duration_years":5,"msci_issue_resolution_pct":90,"penalty_for_serious_short_sale_violation_pct_of_orders":100,"price_validation_status":"policy_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate","rerating_result":"MSCI_market_access_watch","notes":"Short-selling normalization is Stage 2 market access; MSCI watchlist/inclusion and foreign flow required before Green."}
{"case_id":"r11_loop10_ai_dividend_tax_policy_confidence_shock","symbol":"KOSPI/Samsung/SK_Hynix/AI_semiconductor_basket","company_name":"AI dividend / AI windfall policy shock","case_type":"4c_watch","primary_archetype":"AI_WINDFALL_TAX_POLICY_SHOCK","stage4c_date":"2026-05-12","price_validation":{"price_data_source":"FT/Barron's/MarketWatch policy-shock anchors","stage3_price":null,"kospi_intraday_mae_pct":-5.1,"kospi_close_mae_pct":-2.3,"policy_read":"AI windfall redistribution / possible tax concern","clarification":"excess tax revenue, not direct corporate-profit windfall tax","price_validation_status":"reported_market_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"AI_windfall_tax_policy_confidence_break","notes":"AI dividend/tax language is 4C-watch because it hit risk premium before any law or company earnings bridge."}
{"case_id":"r11_loop10_hormuz_iran_energy_shock_hard_4c","symbol":"KOSPI/KRW/exporters/refiners/airlines/autos/chips","company_name":"Hormuz / Iran geopolitical energy shock","case_type":"4c_thesis_break","primary_archetype":"GEOPOLITICAL_ENERGY_SUPPLY_SHOCK","stage4c_date":"2026-03-04","price_validation":{"price_data_source":"Reuters geopolitical energy-shock / market-return anchor","stage3_price":null,"kospi_event_mae_pct":-12.06,"kospi_close":5093.54,"market_cap_wipeout_2d_usd_bn":553.82,"krw_intraday_low_per_usd":1505.8,"krw_close_per_usd":1485.7,"hyundai_motor_mae_pct":-15.8,"samsung_electronics_mae_pct":-11.7,"sk_hynix_mae_pct":-9.6,"middle_east_oil_import_dependency_pct":70,"price_validation_status":"reported_market_and_stock_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"geopolitical_energy_security_hard_4C","notes":"Hormuz/Iran shock is macro hard 4C due to KOSPI crash, KRW 17-year low, and exporter/chip/auto drawdown."}
{"case_id":"r11_loop10_hormuz_energy_security_policy_relief","symbol":"refiners/LNG/shipping/defense/energy_security_basket","company_name":"Hormuz energy-security policy response","case_type":"success_candidate","primary_archetype":"POLICY_RELIEF_RESPONSE","stage2_date":"2026-04-06/2026-05-12","price_validation":{"price_data_source":"Reuters energy-security policy-response anchors","stage3_price":null,"policy_tools":["alternative_routes_suppliers","Saudi/Oman/Algeria_talks","strategic_oil_reserves","five_Korean_vessels_via_Red_Sea","phased_Hormuz_maritime_security_support"],"price_validation_status":"policy_anchor_not_equity_ohlc"},"score_price_alignment":"success_candidate_policy_relief","rerating_result":"energy_security_policy_response_watch","notes":"Policy response is Stage 2 relief, not Green, until oil/LNG costs and sector margins stabilize."}
{"case_id":"r11_loop10_kimchi_bond_fx_liquidity_policy","symbol":"KRW/banks/brokers/exporters","company_name":"Kimchi bond / FX liquidity policy response","case_type":"success_candidate","primary_archetype":"FX_LIQUIDITY_POLICY_RESPONSE","stage2_date":"2024-12-20/2025-06-30","price_validation":{"price_data_source":"FT/Reuters FX-policy anchors","stage3_price":null,"q1_stablecoin_trading_krw_trn":57,"q1_stablecoin_trading_usd_bn":42,"krw_strength_after_policy_per_usd":1347,"krw_stabilization_level_per_usd":1353,"fx_futures_ceiling_local_banks_before_pct":50,"fx_futures_ceiling_local_banks_after_pct":75,"fx_futures_ceiling_foreign_branches_before_pct":250,"fx_futures_ceiling_foreign_branches_after_pct":375,"ceiling_increase_pct":50,"price_validation_status":"fx_policy_anchor_not_company_ohlc"},"score_price_alignment":"success_candidate","rerating_result":"FX_liquidity_policy_watch","notes":"FX policy response is Stage 2; actual KRW stabilization, funding-cost relief and foreign inflows required before Green."}
{"case_id":"r11_loop10_us_investment_fx_outflow_watch","symbol":"KRW/exporters/banks/FX_sensitive_basket","company_name":"$350B U.S. investment pledge / FX outflow watch","case_type":"4c_watch","primary_archetype":"FX_OUTFLOW_TRADE_DEAL_OVERLAY","stage2_date":"2025-12-03","stage4c_date":"2025-12_watch","price_validation":{"price_data_source":"FT FX-bond / capital-outflow anchor","stage3_price":null,"us_investment_pledge_usd_bn":350,"annual_dollar_outflow_limit_usd_bn":20,"fx_bond_cap_2026_usd_bn":5,"fx_bond_cap_2025_usd_bn":3.5,"cap_increase_pct":42.9,"krw_decline_since_end_june_pct":-8,"retail_us_stock_net_buy_2025_usd_bn":30,"retail_us_stock_holdings_usd_bn":160,"fx_reserves_context_usd_bn":430.7,"price_validation_status":"macro_anchor_not_equity_ohlc"},"score_price_alignment":"macro_4C_watch_policy_relief","rerating_result":"tariff_relief_with_FX_outflow_watch","notes":"Tariff relief is offset by structural dollar-outflow pressure; FX stabilization needed before Green."}
```

## shadow weight row 초안

```csv
archetype,funded_policy,capital_inflow,index_inclusion,market_access,institutional_trust,fx_stability,energy_security,policy_to_revenue,event_penalty,macro_4c_sensitivity,notes
POLITICAL_INSTITUTIONAL_TRUST_BREAK,+0,+0,+0,+0,+5,+3,+0,+0,-5,+5,Martial law crisis raises Korea discount and should trigger macro 4C-watch.
GLOBAL_INDEX_INCLUSION,+4,+5,+5,+4,+4,+5,+0,+2,-2,+3,WGBI inclusion is Stage 2; actual flow and funding-cost impact needed for Green.
SHORT_SELLING_NORMALIZATION,+3,+4,+3,+5,+4,+2,+0,+1,-2,+3,Short-selling normalization helps MSCI access but is not company Green.
AI_WINDFALL_TAX_POLICY_SHOCK,+0,+0,+0,+0,+3,+2,+0,+0,-5,+5,AI dividend/tax surprise can break policy confidence even if clarified later.
GEOPOLITICAL_ENERGY_SUPPLY_SHOCK,+0,+0,+0,+0,+3,+5,+5,+0,0,+5,Hormuz/Iran shock is macro hard 4C for oil-import dependent Korea.
POLICY_RELIEF_RESPONSE,+5,+2,+0,+0,+3,+4,+5,+2,-3,+3,Energy-security policy response is relief, not Green, until cost/margin improves.
FX_LIQUIDITY_POLICY_RESPONSE,+4,+4,+0,+3,+3,+5,+0,+1,-3,+4,Kimchi bond/FX reform is Stage 2; actual KRW stabilization and inflow required.
FX_OUTFLOW_TRADE_DEAL_OVERLAY,+3,+2,+0,+2,+3,+5,+0,+2,-4,+5,$350B U.S. pledge creates FX-outflow watch despite tariff relief.
```

---

# 이번 R11 Loop 10 결론

R11은 **정책과 이벤트가 너무 강해서 가격이 먼저 움직이는 섹터**다. 그래서 Stage 3를 가장 보수적으로 줘야 한다.

```text
1. Martial law crisis는 institutional trust 4C-watch다.
   KOSPI와 원화가 바로 흔들렸고, Korea discount risk premium이 올라갔다.

2. WGBI 편입은 좋은 market-structure Stage 2다.
   하지만 실제 자금유입과 금리·환율·자금조달비용 개선 전 개별 종목 Green은 아니다.

3. Short-selling 정상화와 불공정거래 단속은 MSCI access Stage 2다.
   그러나 실제 MSCI 편입과 외국인 flow 전 Stage 3는 아니다.

4. AI dividend/tax 논란은 policy-confidence 4C-watch다.
   “초과 세수 활용”이라는 해명이 있었어도, 시장은 먼저 세금·재분배 risk로 반응했다.

5. Hormuz/Iran shock은 R11 macro hard 4C다.
   KOSPI -12.06%, 원화 17년 저점, 현대차·삼성전자·SK하이닉스 급락이 동시에 나왔다.

6. Hormuz 대응 정책은 relief다.
   정유·해운·방산 Green은 actual cost stabilization과 margin 확인 후다.

7. Kimchi bond / FX liquidity deregulation은 FX policy Stage 2다.
   stablecoin·해외주식 자금유출이 만든 FX stress를 줄이려는 조치다.

8. $350B U.S. investment pledge는 tariff relief와 FX outflow watch가 동시에 붙는다.
   외평채 cap 확대는 방어책이지 Green이 아니다.
```

한 문장으로 압축하면:

> **R11에서 진짜 Stage 3는 “정책·지정학·재난 뉴스가 크다”가 아니라, 그 이벤트가 실제 자본유입·계약·예산·수익·EPS/FCF로 내려오고 정치·환율·에너지 risk premium을 통과하는 순간이다.**
> **이번 R11 Loop 10은 WGBI·short-selling 정상화를 Stage 2로 인정하되, AI dividend/tax shock과 Hormuz shock처럼 risk premium을 깨는 이벤트는 즉시 4C gate로 분리하는 라운드다.**

* [Financial Times](https://www.ft.com/content/fefa0641-7fb0-4d78-81c8-0180f1b618ed?utm_source=chatgpt.com)
* [배런스](https://www.barrons.com/articles/ai-tax-stock-market-kospi-2e468921?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/korean-stocks-dive-won-hits-17-year-low-iran-conflict-2026-03-04/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/energy/south-koreas-lee-says-country-must-balance-risk-hormuz-disruptions-threaten-oil-2026-04-06/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/aerospace-defense/south-korea-weighs-phased-role-hormuz-mission-after-us-talks-defense-minister-2026-05-12/?utm_source=chatgpt.com)

[1]: https://www.reuters.com/markets/asia/investor-reaction-south-koreas-political-crisis-2024-12-04/?utm_source=chatgpt.com "Investor reaction to South Korea's political crisis"
[2]: https://www.reuters.com/markets/rates-bonds/korean-inclusion-ftse-russell-bond-index-seen-shoring-up-local-markets-2024-10-09/?utm_source=chatgpt.com "Korean inclusion in FTSE Russell bond index seen shoring up local markets"
[3]: https://www.reuters.com/sustainability/boards-policy-regulation/skorea-stock-market-likely-join-developed-market-index-regulator-2025-04-21/?utm_source=chatgpt.com "High chance of S.Korean stocks joining developed market index: regulator"
[4]: https://www.ft.com/content/fefa0641-7fb0-4d78-81c8-0180f1b618ed?utm_source=chatgpt.com "South Koreans should all get an AI bonus, says presidential adviser"
[5]: https://www.reuters.com/world/asia-pacific/korean-stocks-dive-won-hits-17-year-low-iran-conflict-2026-03-04/?utm_source=chatgpt.com "Korean stocks record worst day, won sinks on Iran conflict"
[6]: https://www.reuters.com/business/energy/south-koreas-lee-says-country-must-balance-risk-hormuz-disruptions-threaten-oil-2026-04-06/?utm_source=chatgpt.com "South Korea's Lee says country must balance risk as Hormuz disruptions threaten oil supplies"
[7]: https://www.ft.com/content/0f93c015-6e1f-4ef3-accc-8d060983284a?utm_source=chatgpt.com "South Korea lifts 14-year ban on 'kimchi bonds' after dollar-backed stablecoins frenzy"
[8]: https://www.ft.com/content/ea8ece91-ecc6-48ec-a21a-6d3c5148726f?utm_source=chatgpt.com "South Korea raises foreign bond cap to prepare for $350bn US investment"

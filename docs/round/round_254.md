순서상 이번은 **R11 Loop 11 — 정책·지정학·재난·이벤트 가격경로 검증 라운드**다.

```text
round = R11 Loop 11
round_id = round_182
large_sector = POLICY_GEOPOLITICAL_DISASTER_EVENT
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true
```

KRX/Naver/Yahoo/Stooq의 원시 수정주가 일봉 OHLC 전체 구간은 이번 환경에서 안정적으로 직접 확보하지 못했다. 대신 Reuters / FT / Barron’s / MarketWatch가 제공한 **지수 수익률, 섹터·종목 이벤트 수익률, 환율, 자금유입, 정책금액, 외환·채권·디지털자산 지표**로 계산 가능한 값만 계산했다. 계산 불가능한 30D/90D/180D full OHLC는 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R11 = 정책·지정학·재난·이벤트
```

R11의 Stage 3는 “정책이 나왔다”, “지정학 이벤트가 크다”, “시장구조가 좋아졌다”가 아니다.

**정책이 실제 자본유입·자본환원·외환안정·기업 EPS/FCF·risk premium 축소로 내려오고, 정치·지정학·세금·FX·에너지 hard gate를 통과하는 순간**이다.

---

# 2. 대상 canonical archetype

```text
POLITICAL_INSTITUTIONAL_TRUST_BREAK
GLOBAL_INDEX_INCLUSION_CAPITAL_FLOW
SHORT_SELLING_MARKET_ACCESS_REFORM
CORPORATE_GOVERNANCE_VALUEUP_POLICY
AI_WINDFALL_TAX_POLICY_CONFIDENCE_SHOCK
GEOPOLITICAL_ENERGY_SECURITY_HARD_4C
HORMUZ_POLICY_RELIEF_RESPONSE
FX_LIQUIDITY_STABLECOIN_OUTFLOW
FOREIGN_INVESTMENT_PLEDGE_FX_OUTFLOW
POLICY_HEADLINE_NOT_GREEN
```

---

# 3. deep sub-archetype

```text
정치·제도 신뢰:
- martial law crisis
- Korea discount risk premium
- won / KOSPI shock
- unlimited liquidity and market-stabilization response

시장구조:
- WGBI inclusion
- actual foreign bond inflow
- short-selling normalization
- MSCI accessibility
- one-strike-out unfair trading regulation

밸류업·상법:
- treasury share cancellation mandate
- minority shareholder rights
- Korea Discount policy
- policy Stage 2 vs company ROE/PBR Stage 3

AI dividend / tax:
- AI boom excess tax revenue redistribution
- Samsung / SK Hynix / KOSPI shock
- policy-confidence 4C-watch

지정학·에너지:
- Iran / Hormuz conflict
- Korea oil import dependency
- KOSPI circuit breaker
- won 17-year low
- auto / chip / exporter drawdown

FX / capital flow:
- kimchi bond deregulation
- dollar-backed stablecoin trading
- overseas-stock retail outflow
- $350B U.S. investment pledge
- foreign exchange bond cap
```

---

# 4. 국장 신규 후보 case

## Case A — Martial law crisis `4C-watch / institutional trust break`

```text
symbol = KOSPI / KRW / Korea risk premium
case_type = 4C-watch
archetype = POLITICAL_INSTITUTIONAL_TRUST_BREAK
```

### stage date

```text
Stage 1:
2024-12-03 night
- emergency martial law declaration
- institutional trust shock

Stage 2:
없음
- 정치 shock은 positive stage가 아니라 RedTeam input

Stage 3:
없음

Stage 4C-watch:
2024-12-04
- Korean assets broad selloff
- won reaches two-year low
- KOSPI nearly -2%
- finance ministry promises unlimited liquidity
- regulator prepared up to 10T won market-stabilization fund
```

이 case는 R11의 기본 4C-watch다. Reuters는 martial law 선언과 철회 이후 한국 자산이 매도 압력을 받았고, 원화가 2년 저점, KOSPI가 거의 2% 하락했다고 보도했다. 정부는 주식·채권·단기자금·외환시장에 “unlimited liquidity”를 투입하겠다고 밝혔고, 금융당국은 최대 10조 원 규모 시장안정자금 동원 가능성도 제시했다. 즉 이것은 회사별 실적 문제가 아니라 **Korea discount risk premium**이 바로 올라가는 이벤트다. ([Reuters][1])

### 실제 가격경로 검증

```text
price_data_source:
Reuters political-crisis / market-stabilization anchors

stage3_price:
N/A

KOSPI_event_MAE:
nearly -2%

KRW_status:
two-year low

liquidity_response:
"unlimited" liquidity pledge

market_stabilization_fund:
up to 10T won possible

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4C 큰 하락 이전 포착 여부:
partial_success
- martial law declaration 자체가 trigger.
- 제도 신뢰 shock은 당일 4C-watch로 즉시 분류 가능.
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = institutional_trust_break_watch
stage_failure_type = macro_4C_watch_not_company_green
```

---

## Case B — WGBI inclusion / actual bond inflow `success_candidate / capital-flow Stage 2`

```text
symbol = Korean government bonds / KRW / financial-market access basket
case_type = success_candidate
archetype = GLOBAL_INDEX_INCLUSION_CAPITAL_FLOW
```

### stage date

```text
Stage 1:
2024-10-08
- FTSE Russell adds South Korean government bonds to WGBI
- market-access reform validation

Stage 2:
2025-11 inclusion start originally
- WGBI weight 2.22%
- WGBI inclusion over phased period

Stage 2 validation:
2025-12-15
- South Korean bonds draw $11.08B net foreign inflow in November 2025
- largest monthly net inflow since at least 2016
- driven by WGBI inclusion optimism

Stage 3:
없음
- bond inflow는 Korea risk premium 완화 Stage 2
- company-level funding cost / bank NIM / equity rerating 확인 전 Green 금지

Stage 4B:
WGBI/MSCI 기대만으로 금융·증권·저PBR주가 먼저 급등하면 후보
```

WGBI 편입은 R11에서 가장 깨끗한 market-structure Stage 2다. FTSE Russell은 한국 국채가 WGBI에 편입되며 2.22% 비중을 차지한다고 발표했고, 이후 2025년 11월 한국 채권은 110.8억 달러 순유입을 받아 2016년 이후 최대 월간 유입을 기록했다. 다만 이건 주식 Stage 3가 아니라 **자본유입·금리·FX·자금조달비용 개선으로 이어지는지 보는 Stage 2**다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters WGBI inclusion / foreign bond inflow anchors

stage3_price:
N/A

WGBI_weight:
2.22%

foreign_bond_inflow_Nov_2025:
$11.08B

record_status:
largest monthly net inflow since at least 2016

regional_bond_inflows_Nov_2025:
$10.86B across South Korea / Thailand / Malaysia / India / Indonesia

MFE / MAE:
price_data_unavailable_after_deep_search

reason:
- bond-flow evidence는 확보됐지만 개별 국장 종목 adjusted OHLC와 직접 연결 불가.
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = global_index_inclusion_capital_flow_watch
stage_failure_type = stage2_market_structure_not_company_green
```

---

## Case C — Short-selling normalization / unfair-trading crackdown `success_candidate / market-access Stage 2`

```text
symbol = KOSPI / KOSDAQ / brokerages / foreign-access-sensitive basket
case_type = success_candidate
archetype = SHORT_SELLING_MARKET_ACCESS_REFORM
```

### stage date

```text
Stage 1:
2025-03
- five-year market-wide short-selling ban lifted
- illegal short-selling detection system
- foreign investor market-access issue 개선

Stage 2:
2025-06-20
- MSCI says short-selling accessibility has improved
- no major issue noted on short-selling access
- still not enough alone for developed-market upgrade

Stage 2 강화:
2025-07-09
- one-strike-out policy
- severe penalties up to 100% of short-sale orders
- business suspension / trading restrictions possible

Stage 3:
없음
- market-access reform은 Stage 2
- MSCI watchlist, foreign flow, broker revenue, valuation uplift 확인 필요

Stage 4B:
MSCI upgrade 기대만으로 증권주·저PBR주가 먼저 급등하면 후보

Stage 4C:
illegal short-selling recurrence, MSCI disappointment, foreign flow reversal
```

공매도 정상화는 단기적으로 불편한 뉴스처럼 보이지만, 외국인 시장접근성 관점에서는 Stage 2다. MSCI는 한국의 short-selling accessibility가 개선됐다고 평가했지만, FX 접근성 등 다른 한계 때문에 선진시장 편입 가능성은 여전히 제한적으로 봤다. 이후 금융당국은 불공정거래·불법 공매도에 대해 “one-strike-out” 방식의 강한 제재와 최대 100% 주문금액 과징금 가능성을 제시했다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters market-access / short-selling reform anchors

stage3_price:
N/A

short_selling_ban_lift:
2025-03

ban_duration:
about five years

MSCI_assessment:
short-selling accessibility improved / no major issue

penalty_for_serious_short_sale_violation:
up to 100% of short-sale orders

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = MSCI_market_access_watch
stage_failure_type = stage2_market_structure_not_green
```

---

## Case D — Commercial Act treasury-share cancellation `success_candidate / governance value-up Stage 2`

```text
symbol = KOSPI / low-PBR basket / financial holding basket
case_type = success_candidate
archetype = CORPORATE_GOVERNANCE_VALUEUP_POLICY
```

### stage date

```text
Stage 1:
2024~2026
- Korea Discount 해소
- minority shareholder protection
- treasury-share misuse 문제

Stage 2:
2026-02-25
- listed companies must cancel newly acquired treasury shares within one year
- administrative fines if not
- existing treasury shares receive six-month grace period
- policy linked to value-up / Korea Discount reform

Stage 3:
없음
- policy alone is not company Green
- actual buyback cancellation, ROE, PBR gap, dividend policy 확인 필요

Stage 4B:
상법개정 기대만으로 저PBR주가 먼저 rerating되면 후보

Stage 4C:
business group resistance, implementation delay, buyback without cancellation, weak ROE
```

상법개정은 R11의 명확한 Stage 2다. 새로 취득한 treasury shares를 1년 내 소각하게 하고, 기존 treasury shares에는 6개월 유예기간을 부여했다. Reuters는 이 개정이 Korea Discount를 줄이고 minority shareholder rights를 높이기 위한 정책이라고 설명했다. 하지만 회사별 Stage 3는 실제 소각·배당·ROE·PBR gap 축소가 확인될 때다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters Commercial Act / value-up policy anchor

stage3_price:
N/A

newly_acquired_treasury_share_rule:
cancel within 1 year

existing_treasury_share_grace_period:
6 months

administrative_fine:
possible for non-compliance

policy_context:
Korea Discount / minority shareholder rights

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = governance_valueup_policy_watch
stage_failure_type = policy_stage2_not_company_green
```

---

## Case E — AI dividend / AI tax shock `4C-watch / policy confidence break`

```text
symbol = KOSPI / Samsung / SK Hynix / AI-semiconductor basket
case_type = 4C-watch
archetype = AI_WINDFALL_TAX_POLICY_CONFIDENCE_SHOCK
```

### stage date

```text
Stage 1:
2026-05-12
- presidential policy aide discusses AI bonus / redistribution idea
- market interprets as possible AI windfall-tax or redistribution risk

Stage 2:
없음
- tax / redistribution surprise는 positive stage가 아니라 RedTeam input

Stage 3:
없음

Stage 4C-watch:
2026-05-12
- KOSPI intraday -5.1%
- KOSPI close -2.3%
- Samsung / SK Hynix selloff
- clarification: using excess tax revenue, not direct corporate-profit tax
```

AI dividend 논란은 R11에서 policy-confidence 4C-watch다. MarketWatch는 KOSPI가 장중 5.1% 하락하고 종가 기준 2.3% 내렸다고 보도했고, Barron’s는 AI windfall tax 우려가 세계에서 가장 뜨거웠던 한국 증시를 흔들었다고 정리했다. FT는 이후 정책실장이 기업이익 자체를 과세하자는 뜻이 아니라 AI·반도체 boom에서 나오는 초과 세수를 활용하는 아이디어였다고 설명했다고 보도했다. 그래도 시장은 먼저 “세금·재분배 risk”로 반응했다. ([마켓워치][5])

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch / Barron's / FT policy-shock anchors

stage3_price:
N/A

KOSPI_intraday_MAE:
-5.1%

KOSPI_close_MAE:
-2.3%

policy_read_initial:
AI windfall tax / redistribution concern

clarification:
excess tax revenue, not direct corporate profit tax

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4C 큰 하락 이전 포착 여부:
partial_success
- 발언 자체가 trigger.
- 유사 발언 재등장 시 즉시 4C-watch 부여.
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = AI_policy_confidence_break
stage_failure_type = 4C_watch_not_hard_4C
```

---

## Case F — Hormuz / Iran energy shock `macro hard 4C`

```text
symbol = KOSPI / KRW / exporters / autos / chips / airlines / refiners
case_type = macro hard 4C
archetype = GEOPOLITICAL_ENERGY_SECURITY_HARD_4C
```

### stage date

```text
Stage 1:
2026-03-04
- Iran / U.S.-Israel conflict escalation
- Hormuz disruption
- oil / LNG / shipping / raw-material shock
- Korea oil-import dependency exposed

Stage 2:
없음

Stage 3:
없음

Stage 4C:
2026-03-04
- KOSPI -12.06%
- close 5,093.54
- market cap wipeout $553.82B over two days
- won touches 1,505.8/USD, 17-year low
- Hyundai Motor -15.8%
- Samsung Electronics -11.7%
- SK Hynix -9.6%
```

Hormuz/Iran shock은 이번 R11의 hard 4C다. Reuters는 2026년 3월 4일 KOSPI가 12.06% 하락해 5,093.54로 마감했고, 이틀 동안 5,538.2억 달러 시총이 증발했으며, 원화가 달러당 1,505.8까지 밀렸다고 보도했다. 같은 기사에서 Hyundai Motor -15.8%, Samsung Electronics -11.7%, SK Hynix -9.6%가 확인됐다. 한국은 중동 원유 의존도가 약 70%이므로, 이건 단순 지정학 뉴스가 아니라 모든 섹터 위에 덮이는 **macro hard gate**다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters Korean-market geopolitical shock anchor

stage3_price:
N/A

KOSPI_event_MAE:
-12.06%

KOSPI_close:
5,093.54

market_cap_wipeout_2D:
$553.82B

KRW_intraday_low:
1,505.8/USD

KRW_close:
1,485.7/USD

Hyundai_Motor_MAE:
-15.8%

Samsung_Electronics_MAE:
-11.7%

SK_Hynix_MAE:
-9.6%

oil_import_dependency:
about 70% from Middle East

MFE:
N/A

Stage 4C 큰 하락 이전 포착 여부:
hard event
- Hormuz escalation / oil shock / KRW disorderly weakness가 즉시 hard 4C.
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = geopolitical_energy_security_hard_4C
stage_failure_type = macro_hard_4C
```

---

## Case G — Hormuz policy response `success_candidate relief, not Green`

```text
symbol = refiners / LNG / shipping / defense / energy-security basket
case_type = success_candidate + policy_relief
archetype = HORMUZ_POLICY_RELIEF_RESPONSE
```

### stage date

```text
Stage 1:
2026-04~05
- Hormuz disruption aftershock
- oil / LNG security
- maritime-security contribution 논의

Stage 2:
2026-05-12
- South Korea considers phased Hormuz role after U.S. talks
- possible political support, personnel, information sharing, assets
- no immediate troop expansion
- decision subject to domestic legal process

Stage 3:
없음
- policy response는 relief
- actual oil-cost stabilization, shipping insurance cost, refinery margin, LNG supply 안정 확인 필요

Stage 4B:
energy-security headline로 정유·해운·방산 basket이 먼저 급등하면 후보

Stage 4C:
Hormuz 재봉쇄, 유가 재급등, LNG disruption, KRW shock, war-risk premium spike
```

Hormuz 대응 정책은 Green이 아니라 relief다. Reuters는 한국이 미국과의 회담 이후 Hormuz maritime-security role을 단계적으로 검토하고 있으며, 정치적 지원·인력·정보공유·군사자산 제공 등이 가능하지만 즉각적 병력 확대는 아니라고 보도했다. 동시에 Reuters는 Iran war가 글로벌 기업에 최소 250억 달러 비용을 안기고, 유가가 배럴당 100달러를 넘는 환경에서 항공·제조·석유화학 비용 압박이 커졌다고 보도했다. 즉 정책대응은 Stage 2 relief이지, 정유·해운·방산주 Green은 아니다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters Hormuz policy-response / global corporate-cost anchors

stage3_price:
N/A

possible_policy_tools:
political support
personnel deployment
information sharing
military assets

troop_expansion:
not immediate

global_company_cost_from_Iran_war:
at least $25B

oil_price_context:
above $100/bbl

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate_policy_relief
rerating_result = energy_security_policy_response_watch
stage_failure_type = stage2_relief_not_green
```

---

## Case H — FX liquidity / stablecoin outflow / kimchi bond `success_candidate + FX 4C-watch`

```text
symbol = KRW / banks / brokers / fintech / FX-sensitive basket
case_type = success_candidate + 4C-watch
archetype = FX_LIQUIDITY_STABLECOIN_OUTFLOW
```

### stage date

```text
Stage 1:
2025-06~07
- dollar-backed stablecoin frenzy
- overseas-stock retail buying
- weak won / FX liquidity strain

Stage 2:
2025-06-30
- South Korea lifts 14-year ban on institutional investment in kimchi bonds
- goal: attract dollar inflows, stabilize FX liquidity
- Q1 dollar-backed stablecoin trading 57T won / $42B
- won strengthens to 1,347/USD, then stabilizes around 1,353/USD

Stage 4C-watch:
2025-07-27
- BOK warns non-bank stablecoin issuance could create capital outflow / FX crisis response risk
- ruling-party bill could allow issuers with 500M won equity
- capital outflows via stablecoins >$19B in Q1 context

Stage 3:
없음
- FX policy relief만으로 Green 금지
- actual KRW stability, foreign inflow, regulated stablecoin revenue, bank issuance framework 확인 필요
```

FX liquidity case는 R11과 R6가 만나는 지점이다. FT는 한국이 달러-backed stablecoin 거래 급증과 해외주식 투자로 FX 유동성이 압박받자 14년 만에 kimchi bond 투자 금지를 해제했다고 보도했다. Q1 stablecoin trading은 57조 원, 약 420억 달러였고, 조치 후 원화는 1,347/USD까지 강해진 뒤 1,353/USD 부근에서 안정됐다. 그러나 BoK는 비은행 stablecoin 발행이 자본유출과 FX crisis 대응력 훼손을 만들 수 있다고 경고했다. ([Financial Times][8])

### 실제 가격경로 검증

```text
price_data_source:
FT FX-liquidity / stablecoin policy anchors

stage3_price:
N/A

stablecoin_trading_Q1_2025:
57T won / $42B

KRW_strength_after_policy:
1,347/USD

KRW_stabilization_level:
around 1,353/USD

kimchi_bond_ban_duration:
14 years

capital_outflow_context:
>$19B in Q1 via stablecoin-related channels per FT summary

proposed_minimum_equity_for_won_stablecoin_issuers:
500M won

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate_fx_relief_plus_4C_watch
rerating_result = FX_liquidity_policy_watch
stage_failure_type = stage2_macro_relief_not_green
```

---

## Case I — $350B U.S. investment pledge / FX bond cap `macro 4C-watch + policy relief`

```text
symbol = KRW / exporters / banks / FX-sensitive basket
case_type = macro_4C_watch + policy_relief
archetype = FOREIGN_INVESTMENT_PLEDGE_FX_OUTFLOW
```

### stage date

```text
Stage 1:
2025-12
- $350B U.S. investment pledge under trade deal
- tariff relief but dollar outflow risk
- KRW pressure

Stage 2:
2025-12-03
- FX bond issuance cap raised to record $5B for 2026
- 2025 cap was $3.5B
- annual U.S. dollar outflow limit agreed at $20B
- retail investors bought $30B U.S. stocks in 2025
- retail U.S. stock holdings $160B
- KRW down 8% since end-June

Stage 3:
없음
- FX bond cap는 policy relief
- actual KRW stabilization / FX reserves / exporter margin 확인 전 Green 금지

Stage 4C:
structural dollar outflow worsens, won decline accelerates, FX reserves pressure, exporter margin shock
```

$350B U.S. investment pledge는 관세 relief와 FX outflow risk가 동시에 붙는 case다. FT는 한국이 미국과의 trade deal에 따른 3,500억 달러 투자 약속을 준비하면서 2026년 외평채 발행한도를 2025년 35억 달러에서 50억 달러로 높였다고 보도했다. 연간 달러 유출 한도는 200억 달러로 합의됐고, 한국 개인투자자는 2025년에 미국 주식을 300억 달러 순매수했으며 보유액은 1,600억 달러에 이르렀다. 원화는 6월 말 이후 8% 하락했다. ([Financial Times][9])

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

retail_US_stock_net_buy_2025:
$30B

retail_US_stock_holdings:
$160B

KRW_decline_since_end_June:
-8%

FX_reserves_context:
$430.7B

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = macro_4C_watch + policy_relief
rerating_result = tariff_relief_with_FX_outflow_watch
stage_failure_type = macro_watch_not_green
```

---

# 5. 이번 R11 case별 요약표

| case                      | 분류                 |                                                           실제 가격검증 | alignment                 |
| ------------------------- | ------------------ | ----------------------------------------------------------------: | ------------------------- |
| Martial law crisis        | 4C-watch           |           KOSPI nearly -2%, won two-year low, unlimited liquidity | institutional trust break |
| WGBI inclusion            | success_candidate  |                      WGBI 2.22%, Korean bonds +$11.08B net inflow | capital-flow Stage 2      |
| Short-selling reform      | success_candidate  | five-year ban lifted, MSCI access improved, 100% penalty possible | market-access Stage 2     |
| Commercial Act value-up   | success_candidate  |                 treasury shares must be cancelled within one year | governance Stage 2        |
| AI dividend/tax shock     | 4C-watch           |                                 KOSPI intraday -5.1%, close -2.3% | policy-confidence break   |
| Hormuz/Iran shock         | hard 4C            |        KOSPI -12.06%, won 1,505.8, Hyundai -15.8%, Samsung -11.7% | macro hard 4C             |
| Hormuz policy response    | policy relief      |                phased maritime support; global company cost ≥$25B | relief, not Green         |
| FX stablecoin/kimchi bond | success + 4C-watch |                               stablecoin 57T won, KRW 1,347→1,353 | FX relief/watch           |
| $350B U.S. pledge         | macro 4C-watch     |             FX cap $3.5B→$5B, KRW -8%, retail U.S. holdings $160B | FX outflow watch          |

---

# 6. score-price alignment 판정

```text
success_candidate:
- WGBI inclusion / actual bond inflow
- short-selling normalization / market-access reform
- Commercial Act treasury-share cancellation
- FX liquidity / kimchi bond relief

policy_relief:
- Hormuz maritime-security response
- $350B U.S. investment FX bond cap

event_premium:
- WGBI / MSCI / value-up expectation rally
- FX policy relief rally
- energy-security headline rally

thesis_break_watch:
- Martial law institutional trust shock
- AI dividend / tax policy-confidence shock
- stablecoin / FX outflow risk
- $350B U.S. investment dollar-outflow risk

hard_4C:
- Hormuz / Iran geopolitical energy shock

price_moved_without_evidence:
- 정책 발언만으로 AI/반도체 basket selloff/rally
- stablecoin policy theme without regulated revenue
- market-structure reform rally before foreign flow / company earnings bridge
```

---

# 7. 점수비중 교정

## 올릴 축

```text
actual_capital_inflow +5
funded_policy +5
market_access_improvement +5
governance_implementation +4
institutional_trust +5
FX_stability +5
energy_security_resilience +5
policy_to_company_revenue_bridge +5
foreign_flow_confirmation +5
```

### 왜 올리나

WGBI는 말뿐인 정책이 아니라 실제 bond inflow로 이어졌다. short-selling 정상화와 상법개정은 Korea Discount 축소에 필요한 market structure evidence다. 하지만 이들은 개별 종목 Stage 3가 아니라, **risk premium을 낮출 수 있는 Stage 2**다.

## 내릴 축

```text
policy_speech_only -5
tax_or_redistribution_surprise -5
political_institutional_shock -5
geopolitical_energy_shock -5
stablecoin_policy_theme_only -5
FX_policy_without_flow -4
index_inclusion_expectation_only -3
market_reform_without_foreign_flow -3
foreign_investment_pledge_outflow -4
event_rally_before_earnings_bridge -5
```

### 왜 내리나

AI dividend/tax shock은 법안이 없어도 KOSPI를 흔들었다. Martial law는 institutional trust를 직접 깨뜨렸다. Hormuz shock은 한국의 에너지 의존도와 환율 취약성을 동시에 찔렀다. Stablecoin·U.S. investment pledge는 디지털금융/무역정책처럼 보여도 실제로는 FX outflow risk를 만든다.

## Green gate 강화 조건

```text
R11 Stage 3-Green 필수:
1. 정책이 실제 법안 / 예산 / index inclusion / 자본유입으로 확정
2. 회사 단위 revenue / EPS / FCF bridge 존재
3. 외국인 flow 또는 funding cost 개선 확인
4. FX / 금리 / credit cost에 긍정효과 확인
5. 정치·제도·규제 신뢰 훼손 없음
6. 세금·재분배 surprise 없음
7. 에너지·지정학 hard risk 없음
8. 가격경로가 evidence 이후 따라옴

금지:
정책 발언만 있음
선거공약만 있음
세금/재분배 surprise
지정학 headline만 있음
WGBI/MSCI 기대만 있음
FX 정책 발표만 있고 실제 flow 없음
stablecoin theme only
```

## 4B 조기감지 조건

```text
4B-watch:
WGBI/MSCI 기대만으로 금융·증권·저PBR주 급등
상법개정 기대만으로 자사주소각주 급등
정책 발언만으로 특정 테마 급등
AI dividend/tax 해명 전후로 AI 반도체 basket 급락·반등
energy-security headline로 정유·해운·방산주 급등
FX policy relief로 은행/수출주가 먼저 rerating
stablecoin policy theme으로 2~3배 급등

4B-elevated:
실제 flow 없이 price만 감
정책 디테일 없이 테마주가 먼저 감
외국인 flow가 반대로 나감
환율이 안정되지 않음
회사별 EPS/FCF bridge가 없음
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
stablecoin-driven capital outflow
policy reversal
```

이번 R11 Loop 11에서 확정 hard 4C는 **Hormuz/Iran energy shock**이다. Martial law와 AI dividend/tax는 강한 4C-watch이며, stablecoin·$350B U.S. investment pledge는 FX 4C-watch다.

---

# 8. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
```

---

# 9. patch-ready 출력

## docs/round/round_182.md 요약

```md
# R11 Loop 11. Policy / Geopolitical / Disaster / Event Price Validation

이번 라운드는 R11 Loop 11 price-validation 라운드다.

핵심 결론:
- Martial law crisis is institutional-trust 4C-watch. KOSPI fell nearly 2%, won hit a two-year low, and authorities pledged unlimited liquidity plus possible 10T won market-stabilization support.
- WGBI inclusion is capital-flow Stage 2. South Korean government bonds were added at 2.22% weight, and Korean bonds drew $11.08B net foreign inflow in November 2025, the largest since at least 2016.
- Short-selling normalization is market-access Stage 2. Five-year ban lifted, MSCI said accessibility improved, and regulators introduced one-strike-out penalties up to 100% of short-sale orders.
- Commercial Act revision is governance value-up Stage 2. Newly acquired treasury shares must be cancelled within one year, with six-month grace for existing treasury shares.
- AI dividend/tax shock is policy-confidence 4C-watch. KOSPI fell as much as 5.1% and closed -2.3% after comments on AI boom tax-revenue redistribution were interpreted as windfall-tax risk.
- Hormuz/Iran shock is macro hard 4C. KOSPI -12.06%, close 5,093.54, two-day market-cap wipeout $553.82B, won 1,505.8/USD, Hyundai -15.8%, Samsung -11.7%, SK Hynix -9.6%.
- Hormuz policy response is relief, not Green. Korea may support maritime security through political support, personnel, information sharing or assets, but actual cost stabilization is required.
- FX/stablecoin/kimchi bond case is Stage 2 relief plus 4C-watch. Q1 stablecoin trading was 57T won / $42B, kimchi bond ban was lifted, won strengthened to 1,347 then stabilized near 1,353.
- $350B U.S. investment pledge is FX-outflow 4C-watch. FX bond cap raised from $3.5B to $5B, annual dollar outflow limit $20B, retail U.S. stock holdings $160B, KRW down 8% since end-June.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 182 R11 Loop 11 Policy Geopolitical Event Price Validation

## 반영 내용
- R11 Loop 11 price-validation 라운드를 추가했다.
- Institutional shock, WGBI flow, short-selling reform, Commercial Act value-up, AI dividend/tax shock, Hormuz hard macro shock, Hormuz policy relief, FX/stablecoin outflow, $350B U.S. investment FX overlay를 비교했다.
- Reuters/FT/Barron’s/MarketWatch anchors로 가능한 MFE/MAE 및 policy/macro/FX metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- actual capital inflow, funded policy, market access improvement, governance implementation, institutional trust, FX stability, energy-security resilience 가중치 강화
- policy speech-only, tax/redistribution surprise, political institutional shock, geopolitical energy shock, stablecoin theme-only, FX outflow pressure 감점 강화
- R11 macro hard 4C와 policy-confidence 4C-watch 민감도 강화
```

## case row 초안

```jsonl
{"case_id":"r11_loop11_martial_law_institutional_trust_shock","symbol":"KOSPI/KRW","company_name":"South Korea institutional trust shock","case_type":"4c_watch","primary_archetype":"POLITICAL_INSTITUTIONAL_TRUST_BREAK","stage4c_date":"2024-12-04","price_validation":{"price_data_source":"Reuters political-crisis / market-stabilization anchors","stage3_price":null,"kospi_event_mae_pct":"nearly -2","krw_status":"two-year low","liquidity_response":"unlimited liquidity pledge","market_stabilization_fund_krw_trn":10,"price_validation_status":"reported_market_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"institutional_trust_break_watch","notes":"Martial law crisis raises Korea Discount and should trigger macro 4C-watch."}
{"case_id":"r11_loop11_wgbi_inclusion_actual_bond_inflow","symbol":"Korean_government_bonds/KRW/Korea_assets","company_name":"WGBI inclusion and foreign bond inflow","case_type":"success_candidate","primary_archetype":"GLOBAL_INDEX_INCLUSION_CAPITAL_FLOW","stage2_date":"2024-10-08/2025-11/2025-12-15","price_validation":{"price_data_source":"Reuters WGBI inclusion and bond-inflow anchors","stage3_price":null,"wgbi_weight_pct":2.22,"foreign_bond_inflow_nov_2025_usd_bn":11.08,"record_status":"largest monthly net inflow since at least 2016","regional_bond_inflows_nov_2025_usd_bn":10.86,"price_validation_status":"market_structure_anchor_not_company_ohlc"},"score_price_alignment":"success_candidate","rerating_result":"global_index_inclusion_capital_flow_watch","notes":"WGBI produced actual bond inflow, but company-level funding-cost/EPS bridge is required before Green."}
{"case_id":"r11_loop11_short_selling_market_access_reform","symbol":"KOSPI/KOSDAQ/brokerage_foreign_access_basket","company_name":"Short-selling normalization and unfair-trading crackdown","case_type":"success_candidate","primary_archetype":"SHORT_SELLING_MARKET_ACCESS_REFORM","stage2_date":"2025-03/2025-06-20/2025-07-09","price_validation":{"price_data_source":"Reuters market-access and unfair-trading anchors","stage3_price":null,"ban_duration_years":5,"msci_assessment":"short-selling accessibility improved","serious_violation_penalty_pct_of_short_sale_orders":100,"price_validation_status":"policy_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate","rerating_result":"MSCI_market_access_watch","notes":"Short-selling normalization helps market access but is not company Green until flows and earnings bridge confirm."}
{"case_id":"r11_loop11_commercial_act_treasury_cancellation_valueup","symbol":"KOSPI/low_PBR_basket/financial_holding_basket","company_name":"Commercial Act treasury-share cancellation reform","case_type":"success_candidate","primary_archetype":"CORPORATE_GOVERNANCE_VALUEUP_POLICY","stage2_date":"2026-02-25","price_validation":{"price_data_source":"Reuters Commercial Act value-up anchor","stage3_price":null,"newly_acquired_treasury_share_rule":"cancel_within_1_year","existing_treasury_share_grace_period_months":6,"administrative_fine_possible":true,"policy_context":"Korea Discount and minority shareholder rights","price_validation_status":"policy_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate","rerating_result":"governance_valueup_policy_watch","notes":"Treasury-share cancellation mandate is Stage 2; actual cancellation, ROE/PBR and dividends required before Green."}
{"case_id":"r11_loop11_ai_dividend_tax_policy_confidence_shock","symbol":"KOSPI/Samsung/SK_Hynix/AI_semiconductor_basket","company_name":"AI dividend / AI tax policy shock","case_type":"4c_watch","primary_archetype":"AI_WINDFALL_TAX_POLICY_CONFIDENCE_SHOCK","stage4c_date":"2026-05-12","price_validation":{"price_data_source":"MarketWatch/Barron's/FT policy-shock anchors","stage3_price":null,"kospi_intraday_mae_pct":-5.1,"kospi_close_mae_pct":-2.3,"policy_read_initial":"AI windfall tax / redistribution concern","clarification":"excess tax revenue, not direct corporate profit tax","price_validation_status":"reported_market_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"AI_policy_confidence_break","notes":"AI dividend/tax language can break policy confidence even without formal bill; immediate 4C-watch."}
{"case_id":"r11_loop11_hormuz_iran_energy_shock_hard_4c","symbol":"KOSPI/KRW/exporters/refiners/airlines/autos/chips","company_name":"Hormuz / Iran geopolitical energy shock","case_type":"4c_thesis_break","primary_archetype":"GEOPOLITICAL_ENERGY_SECURITY_HARD_4C","stage4c_date":"2026-03-04","price_validation":{"price_data_source":"Reuters Korean-market geopolitical shock anchor","stage3_price":null,"kospi_event_mae_pct":-12.06,"kospi_close":5093.54,"market_cap_wipeout_2d_usd_bn":553.82,"krw_intraday_low_per_usd":1505.8,"krw_close_per_usd":1485.7,"hyundai_motor_mae_pct":-15.8,"samsung_electronics_mae_pct":-11.7,"sk_hynix_mae_pct":-9.6,"middle_east_oil_import_dependency_pct":70,"price_validation_status":"reported_market_and_stock_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"geopolitical_energy_security_hard_4C","notes":"Hormuz/Iran shock is macro hard 4C due to KOSPI crash, KRW 17-year low and auto/chip drawdown."}
{"case_id":"r11_loop11_hormuz_policy_relief_response","symbol":"refiners/LNG/shipping/defense/energy_security_basket","company_name":"Hormuz maritime-security policy response","case_type":"success_candidate","primary_archetype":"HORMUZ_POLICY_RELIEF_RESPONSE","stage2_date":"2026-05-12","price_validation":{"price_data_source":"Reuters Hormuz policy-response and global corporate-cost anchors","stage3_price":null,"possible_policy_tools":["political_support","personnel_deployment","information_sharing","military_assets"],"troop_expansion_immediate":false,"global_company_cost_from_iran_war_usd_bn":25,"oil_price_context_usd_per_bbl":100,"price_validation_status":"policy_anchor_not_equity_ohlc"},"score_price_alignment":"success_candidate_policy_relief","rerating_result":"energy_security_policy_response_watch","notes":"Policy response is relief, not Green, until oil/LNG costs, insurance and margins stabilize."}
{"case_id":"r11_loop11_fx_stablecoin_kimchi_bond_relief_watch","symbol":"KRW/banks/brokers/fintech/FX_sensitive_basket","company_name":"FX liquidity / stablecoin outflow / kimchi bond deregulation","case_type":"success_candidate","primary_archetype":"FX_LIQUIDITY_STABLECOIN_OUTFLOW","stage2_date":"2025-06-30","stage4c_date":"2025-07-27_watch","price_validation":{"price_data_source":"FT FX-liquidity and stablecoin policy anchors","stage3_price":null,"stablecoin_trading_q1_2025_krw_trn":57,"stablecoin_trading_q1_2025_usd_bn":42,"krw_strength_after_policy_per_usd":1347,"krw_stabilization_level_per_usd":1353,"kimchi_bond_ban_duration_years":14,"capital_outflow_context_usd_bn":19,"proposed_minimum_equity_for_won_stablecoin_issuers_krw_mn":500,"price_validation_status":"fx_policy_anchor_not_company_ohlc"},"score_price_alignment":"success_candidate_fx_relief_plus_4C_watch","rerating_result":"FX_liquidity_policy_watch","notes":"Kimchi bond deregulation is FX relief; stablecoin-driven outflow and non-bank issuance risk remain 4C-watch."}
{"case_id":"r11_loop11_us_investment_pledge_fx_outflow_watch","symbol":"KRW/exporters/banks/FX_sensitive_basket","company_name":"$350B U.S. investment pledge / FX outflow watch","case_type":"4c_watch","primary_archetype":"FOREIGN_INVESTMENT_PLEDGE_FX_OUTFLOW","stage2_date":"2025-12-03","stage4c_date":"2025-12_watch","price_validation":{"price_data_source":"FT FX-bond / capital-outflow anchor","stage3_price":null,"us_investment_pledge_usd_bn":350,"annual_dollar_outflow_limit_usd_bn":20,"fx_bond_cap_2026_usd_bn":5,"fx_bond_cap_2025_usd_bn":3.5,"cap_increase_pct":42.9,"retail_us_stock_net_buy_2025_usd_bn":30,"retail_us_stock_holdings_usd_bn":160,"krw_decline_since_end_june_pct":-8,"fx_reserves_context_usd_bn":430.7,"price_validation_status":"macro_anchor_not_equity_ohlc"},"score_price_alignment":"macro_4C_watch_policy_relief","rerating_result":"tariff_relief_with_FX_outflow_watch","notes":"U.S. investment pledge reduces tariff pressure but adds structural dollar-outflow risk; FX stabilization required before Green."}
```

## shadow weight row 초안

```csv
archetype,actual_capital_inflow,funded_policy,market_access,governance_implementation,institutional_trust,fx_stability,energy_security,policy_to_revenue,event_penalty,macro_4c_sensitivity,notes
POLITICAL_INSTITUTIONAL_TRUST_BREAK,+0,+0,+0,+0,+5,+4,+0,+0,-5,+5,Martial law crisis raises Korea Discount and triggers macro 4C-watch.
GLOBAL_INDEX_INCLUSION_CAPITAL_FLOW,+5,+4,+4,+3,+4,+5,+0,+2,-2,+3,WGBI actual inflow is Stage 2; company funding-cost/EPS bridge required.
SHORT_SELLING_MARKET_ACCESS_REFORM,+3,+4,+5,+4,+4,+2,+0,+1,-2,+3,Short-selling normalization improves market access but is not company Green.
CORPORATE_GOVERNANCE_VALUEUP_POLICY,+3,+4,+3,+5,+4,+2,+0,+2,-3,+3,Treasury cancellation mandate is Stage 2; actual cancellation/ROE/PBR bridge required.
AI_WINDFALL_TAX_POLICY_CONFIDENCE_SHOCK,+0,+0,+0,+0,+3,+3,+0,+0,-5,+5,AI dividend/tax surprise breaks policy confidence and gets 4C-watch.
GEOPOLITICAL_ENERGY_SECURITY_HARD_4C,+0,+0,+0,+0,+3,+5,+5,+0,0,+5,Hormuz/Iran shock is macro hard 4C for energy-import dependent Korea.
HORMUZ_POLICY_RELIEF_RESPONSE,+2,+5,+0,+0,+3,+4,+5,+2,-3,+4,Energy-security response is relief until costs and margins stabilize.
FX_LIQUIDITY_STABLECOIN_OUTFLOW,+4,+4,+3,+2,+3,+5,+0,+1,-4,+5,Kimchi bond relief helps FX, but stablecoin outflow remains 4C-watch.
FOREIGN_INVESTMENT_PLEDGE_FX_OUTFLOW,+2,+3,+2,+1,+3,+5,+0,+2,-4,+5,$350B pledge creates tariff relief plus structural dollar-outflow risk.
```

---

# 이번 R11 Loop 11 결론

R11은 **가장 “뉴스가 가격을 먼저 때리는” 섹터**다. 그래서 Stage 3는 느리게, 4B/4C는 빠르게 줘야 한다.

```text
1. Martial law crisis는 institutional trust 4C-watch다.
   기업 실적 이전에 Korea Discount risk premium이 바로 올라갔다.

2. WGBI inclusion은 실제 foreign bond inflow까지 확인된 좋은 Stage 2다.
   하지만 개별 종목 Green은 funding-cost/EPS bridge가 확인된 뒤다.

3. Short-selling normalization은 market access Stage 2다.
   MSCI 접근성 개선은 좋지만 실제 foreign flow와 valuation uplift 확인이 필요하다.

4. Commercial Act treasury-share cancellation은 value-up Stage 2다.
   실제 소각, ROE, PBR gap 축소 전에는 Green이 아니다.

5. AI dividend/tax shock은 policy-confidence 4C-watch다.
   해명이 있어도 시장은 먼저 세금·재분배 risk로 반응했다.

6. Hormuz/Iran shock은 macro hard 4C다.
   KOSPI -12.06%, 원화 17년 저점, 자동차·반도체 급락이 동시에 나왔다.

7. Hormuz policy response는 relief다.
   정유·해운·방산 Green은 oil/LNG cost와 margin 안정 후다.

8. Kimchi bond / stablecoin case는 FX relief와 FX 4C-watch가 동시에 붙는다.
   stablecoin 자금유출은 디지털금융 테마가 아니라 외환 gate다.

9. $350B U.S. investment pledge는 tariff relief와 FX outflow risk가 같이 붙는다.
   외평채 cap 확대는 방어책이지 Green이 아니다.
```

한 문장으로 압축하면:

> **R11에서 진짜 Stage 3는 “정책·지정학·시장구조 뉴스가 크다”가 아니라, 그 이벤트가 실제 자본유입·외환안정·funding cost 개선·기업 EPS/FCF로 내려오고 정치·세금·에너지·FX hard gate를 통과하는 순간이다.**

* [Reuters](https://www.reuters.com/world/asia-pacific/korean-stocks-dive-won-hits-17-year-low-iran-conflict-2026-03-04/?utm_source=chatgpt.com)
* [Barron's](https://www.barrons.com/articles/ai-tax-stock-market-kospi-2e468921?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/markets/rates-bonds/india-south-korea-bonds-join-ftse-russell-government-indexes-2025-2024-10-08/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/foreign-inflows-into-asian-bonds-hit-six-month-high-november-2025-12-15/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/markets/asia/investor-reaction-south-koreas-political-crisis-2024-12-04/?utm_source=chatgpt.com)
* [Financial Times](https://www.ft.com/content/0f93c015-6e1f-4ef3-accc-8d060983284a?utm_source=chatgpt.com)

[1]: https://www.reuters.com/markets/asia/investor-reaction-south-koreas-political-crisis-2024-12-04/?utm_source=chatgpt.com "Investor reaction to South Korea's political crisis"
[2]: https://www.reuters.com/markets/rates-bonds/india-south-korea-bonds-join-ftse-russell-government-indexes-2025-2024-10-08/?utm_source=chatgpt.com "India, S. Korea bonds to join FTSE Russell government indexes in 2025"
[3]: https://www.reuters.com/world/asia-pacific/south-koreas-short-selling-accessibility-has-improved-msci-says-2025-06-20/?utm_source=chatgpt.com "South Korea's short-selling accessibility has improved, MSCI says"
[4]: https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-parliament-approves-commercial-act-revision-aimed-boosting-share-2026-02-25/?utm_source=chatgpt.com "South Korea parliament approves commercial act revision aimed at boosting share valuations"
[5]: https://www.marketwatch.com/story/the-hottest-stock-market-in-the-world-finally-met-its-match-taxes-55cf54c6?utm_source=chatgpt.com "The hottest stock market in the world finally met its match: taxes"
[6]: https://www.reuters.com/world/asia-pacific/korean-stocks-dive-won-hits-17-year-low-iran-conflict-2026-03-04/?utm_source=chatgpt.com "Korean stocks record worst day, won sinks on Iran conflict"
[7]: https://www.reuters.com/business/aerospace-defense/south-korea-weighs-phased-role-hormuz-mission-after-us-talks-defense-minister-2026-05-12/?utm_source=chatgpt.com "South Korea weighs phased Hormuz role after US talks, minister says"
[8]: https://www.ft.com/content/0f93c015-6e1f-4ef3-accc-8d060983284a?utm_source=chatgpt.com "South Korea lifts 14-year ban on 'kimchi bonds' after dollar-backed stablecoins frenzy"
[9]: https://www.ft.com/content/ea8ece91-ecc6-48ec-a21a-6d3c5148726f?utm_source=chatgpt.com "South Korea raises foreign bond cap to prepare for $350bn US investment"

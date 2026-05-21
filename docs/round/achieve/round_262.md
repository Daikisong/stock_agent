순서상 이번은 **R6 Loop 12 — 금융·자본배분·디지털금융 가격경로 검증 라운드**다.

```text
round = R6 Loop 12
round_id = round_190
large_sector = FINANCIAL_CAPITAL_DIGITAL
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = false
```

이번 R6 Loop 12는 은행 value-up만 반복하지 않고, **금융지주 value-up, 증권주 거래대금 cycle, 보험 NAV capital release, 은행의 디지털자산 지분투자, Naver/Dunamu platform trust, Toss biometric payment/IPO, KakaoBank governance risk, stablecoin·FX gate**를 같이 본다.

원시 수정주가 일봉 OHLC는 이번 환경에서 안정적으로 확보하지 못했다. 대신 Reuters / WSJ / FT가 제공한 **가격 anchor, 이벤트 수익률, 거래금액, 지분율, 정책 수치, FX·stablecoin 지표, governance risk 지표**만 계산했다. 그래서 30D/90D/180D full OHLC가 없는 항목은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R6 = 금융·자본배분·디지털금융
```

R6에서 Stage 3는 “저PBR”, “밸류업”, “증권주”, “디지털자산”, “스테이블코인”이라는 단어가 아니다.

진짜 Stage 3는 **ROE, CET1/K-ICS, credit cost, 실제 소각, 배당 반복성, fee income, 거래대금 지속성, regulated digital revenue, platform trust, FX stability**가 같이 닫힐 때다.

---

# 2. 대상 canonical archetype

```text
BANK_VALUEUP_ROE_PBR_RERATING
BROKERAGE_MARKET_VOLUME_CYCLE
INSURANCE_NAV_CAPITAL_RELEASE
BANK_DIGITAL_ASSET_EQUITY_OPTION
DIGITAL_ASSET_PLATFORM_MERGER_TRUST_WATCH
FINTECH_SUPERAPP_BIOMETRIC_PAYMENT
INTERNET_BANK_GOVERNANCE_4C
STABLECOIN_POLICY_OVERHEAT_FX_GATE
```

---

# 3. deep sub-archetype

```text
금융지주 value-up:
- KB / Shinhan / Hana / Woori
- Commercial Act treasury-share cancellation
- ROE / CET1 / credit cost
- PBR rerating vs actual recurring capital return

증권:
- securities basket
- KOSPI 7,000 / 거래대금 cycle
- brokerage revenue / IB / trading income
- cyclical success vs structural Green

보험/NAV:
- Samsung Life
- Samsung Electronics stake sale
- financial-company governance regulation
- capital release vs shareholder return

디지털자산 은행:
- Hana Bank / Dunamu / Upbit
- equity-method optionality
- remittance / stablecoin / blockchain service
- regulatory and exchange-trust risk

플랫폼 금융:
- NAVER Financial / Dunamu
- Naver Pay / Upbit
- abnormal withdrawal / exchange trust
- stock swap / regulatory approval

핀테크:
- Toss / FacePay / Toss Bank / Toss Securities
- biometric payment
- U.S. IPO / global expansion
- privacy / data / stablecoin regulation

인터넷은행:
- KakaoBank
- Kakao founder legal risk
- major shareholder suitability
- bank ownership restriction

Stablecoin / FX:
- Kakao Pay / LG CNS / Aton / ME2ON
- won stablecoin policy
- kimchi bond deregulation
- capital outflow / non-bank issuer risk
```

---

# 4. 국장 신규 후보 case

## Case A — 금융지주 value-up basket `success_candidate / Stage 2, not Green`

```text
symbols = 105560 / 055550 / 086790 / 316140
case_type = success_candidate
archetype = BANK_VALUEUP_ROE_PBR_RERATING
```

### stage date

```text
Stage 1:
2024~2026
- Korea Discount 해소
- value-up policy
- low-PBR financial holding rerating
- 배당 / 자사주 / 소각 기대

Stage 2:
2026-02-25
- listed companies must cancel newly acquired treasury shares within one year
- existing treasury shares have six-month grace period
- administrative fines possible

Stage 2 price validation:
2026-05-06
- KOSPI closes +6.45% at 7,384.56
- financial groups rally +4.2%
- foreign investors buy 3.1T won local shares

Stage 3:
없음
- financial holding Green requires ROE, CET1, credit cost, recurring cancellation/dividend proof

Stage 4B:
PBR rerating이 ROE·capital return보다 먼저 진행되면 watch

Stage 4C:
credit cost spike, CET1 deterioration, PF stress, shareholder return retreat
```

상법 개정으로 새로 취득한 treasury shares는 1년 안에 소각해야 하고, 기존 treasury shares에는 6개월 유예기간이 부여됐다. 이는 금융지주 value-up의 Stage 2다. 그러나 2026년 5월 6일 KOSPI가 7,000을 넘은 날 financial groups는 +4.2% 올랐지만, 같은 날 KOSPI는 +6.45%였기 때문에 금융지주가 아직 구조적 Green을 증명했다고 보기 어렵다. ([Reuters][1])

### 실제 가격경로 검증

```text
price_data_source:
Reuters Commercial Act / KOSPI 7000 event-return anchors

entry_date:
N/A

stage3_price:
N/A

Commercial_Act_revision:
newly acquired treasury shares must be cancelled within 1 year

existing_treasury_share_grace_period:
6 months

financial_groups_event_MFE:
+4.2%

KOSPI_same_context:
+6.45%

relative_performance_vs_KOSPI:
4.2 - 6.45
= -2.25pp

foreign_net_purchase:
3.1T won / $2.13B

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = financial_holding_valueup_stage2
stage_failure_type = policy_and_market_rally_not_green
```

---

## Case B — 증권주 basket `cyclical_success + 4B-watch`

```text
symbols = securities basket / Mirae Asset / Samsung Securities / Kiwoom / NH exposure
case_type = cyclical_success + 4B-watch
archetype = BROKERAGE_MARKET_VOLUME_CYCLE
```

### stage date

```text
Stage 1:
2025~2026
- KOSPI bull market
- foreign inflow
- 거래대금 / brokerage / IB / trading income 기대

Stage 2:
2026-05-06
- KOSPI closes +6.45%
- securities firms jump +13.5%
- financial groups +4.2%
- foreign investors buy 3.1T won

Stage 3:
없음
- brokerage revenue, IB revenue, ROE, client asset growth 확인 전 Green 금지

Stage 4B:
2026-05-06
- securities basket +13.5%
- price outruns confirmed brokerage/IB earnings
```

증권주는 이번 R6에서 가장 깨끗한 `cyclical_success`다. KOSPI 7,000 돌파일에 securities firms는 +13.5%로 KOSPI를 7.05pp 아웃퍼폼했다. 그러나 이는 거래대금 cycle과 market-confidence rally이지, 아직 Stage 3 Green은 아니다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters KOSPI 7000 sector-return anchor

stage3_price:
N/A

KOSPI_event_return:
+6.45%

KOSPI_intraday_high_return:
+7.06%

securities_firms_event_MFE:
+13.5%

financial_groups_event_MFE:
+4.2%

securities_relative_outperformance_vs_KOSPI:
13.5 - 6.45
= +7.05pp

foreign_net_purchase:
3.1T won / $2.13B

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = cyclical_success
rerating_result = brokerage_market_volume_cycle_watch
stage_failure_type = stage2_cycle_not_green
```

---

## Case C — Samsung Life `success_candidate / insurance NAV capital release`

```text
symbol = 032830
case_type = success_candidate + regulatory_watch
archetype = INSURANCE_NAV_CAPITAL_RELEASE
```

### stage date

```text
Stage 1:
2025~2026
- Samsung Electronics stake value
- insurance NAV discount
- capital release / governance regulation compliance

Stage 2:
2026-03-19
- Samsung Life to divest 1.3T won worth of Samsung Electronics shares
- purpose: resolve local financial-company governance regulation risk

Stage 3:
없음
- 매각대금의 capital policy, K-ICS, CSM, dividend/buyback 확인 필요

Stage 4B:
Samsung Electronics rally가 Samsung Life NAV trade에 과도하게 반영되면 watch

Stage 4C:
Samsung Electronics drawdown, regulatory sale pressure, capital ratio weakness
```

Samsung Life는 삼성전자 지분 1.3조 원어치를 매각한다고 공시했고, 목적은 금융회사 지배구조 관련 regulation risk를 해소하기 위한 조치였다. 이는 insurance NAV capital release Stage 2다. 그러나 실제 Stage 3는 매각대금이 K-ICS, 배당, 소각, CSM, shareholder return으로 이어질 때다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters regulatory share-sale anchor

stage3_price:
N/A

Samsung_Electronics_stake_sale:
1.3T won / $867.07M

transaction_purpose:
resolve financial-company governance regulation risk

FX_rate_context:
1,499.3 won/USD

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate_regulatory_watch
rerating_result = insurance_NAV_capital_release_watch
stage_failure_type = capital_release_not_green_until_use_of_proceeds
```

---

## Case D — Hana Bank / Dunamu `success_candidate / regulated digital-asset equity option`

```text
symbol = 086790
case_type = success_candidate
archetype = BANK_DIGITAL_ASSET_EQUITY_OPTION
```

### stage date

```text
Stage 1:
2025~2026
- digital asset institutionalization
- bank-stablecoin / remittance / blockchain service optionality

Stage 2:
2026-05-14 / 2026-05-15
- Hana Bank acquires 6.55% Dunamu stake
- transaction value about 1T won / $700M
- Upbit handles more than 80% of virtual asset trading volume
- Kakao Investment stake falls to 4.03%

Stage 2 validation:
2026-06-15 expected closing per WSJ
- Hana becomes fourth-largest shareholder
- remittance service technical verification completed

Stage 3:
없음
- equity-method earnings, regulated revenue, capital impact, compliance 확인 필요

Stage 4B:
digital-asset optionality가 bank valuation에 과도 반영되면 watch

Stage 4C:
crypto volume collapse, exchange trust incident, stablecoin regulation delay, capital charge
```

Hana Bank는 Dunamu 지분 6.55%를 약 1조 원에 인수하기로 했고, Upbit은 국내 virtual asset trading volume의 80% 이상을 처리한다. WSJ는 이 투자가 국내 은행의 단일 digital-asset 투자 중 최대 규모이며, Hana와 Dunamu의 blockchain-based overseas remittance service가 technical verification을 마쳤다고 보도했다. 이건 강한 Stage 2지만, 아직 Hana Financial의 Green은 아니다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / WSJ transaction anchors

stage3_price:
N/A

transaction_value:
1.0T won / about $700M

WSJ_transaction_value:
1.003T won / $672.5M

stake_acquired:
6.55%

shares_acquired:
2.284M shares

implied_Dunamu_equity_value_Reuters:
1.0T / 0.0655
= 약 15.27T won

Upbit_trading_volume_share:
>80%

Kakao_Investment_remaining_stake:
4.03%

expected_closing:
2026-06-15

business_validation:
blockchain-based overseas remittance technical verification completed

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = bank_digital_asset_equity_option_watch
stage_failure_type = stage2_equity_option_not_green
```

---

## Case E — NAVER Financial / Dunamu `event_premium + exchange-trust 4C-watch`

```text
symbol = 035420
case_type = success_candidate + event_premium + 4C-watch
archetype = DIGITAL_ASSET_PLATFORM_MERGER_TRUST_WATCH
```

### stage date

```text
Stage 1:
2025
- Naver fintech expansion
- digital-asset / stablecoin growth expectation

Stage 2:
2025-11-27
- Naver Financial agrees to acquire Dunamu
- all-stock deal value 15.13T won / $10.27B
- exchange ratio 2.54 Naver Financial shares per Dunamu share
- Upbit market share around 70%

Stage 4B:
2025-11-27
- Naver shares initially +7%+

Stage 4C-watch:
2025-11-27
- Upbit abnormal withdrawal 54B won
- Naver later -4.2%
- Upbit said it would cover loss using own assets

Stage 3:
없음
- regulatory approval, closing, platform revenue, trust recovery 확인 필요
```

NAVER Financial의 Dunamu 인수는 digital-asset platform Stage 2다. 하지만 같은 날 Upbit abnormal withdrawal 540억 원이 나오면서, NAVER 주가는 초반 +7%에서 -4.2%로 돌아섰다. 즉 이 case는 R6에서 “digital asset growth”와 “exchange trust”를 반드시 동시에 봐야 한다는 기준점이다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters transaction / event-return / trust-risk anchor

stage3_price:
N/A

deal_value:
15.13T won / $10.27B

exchange_ratio:
2.54 Naver Financial shares per Dunamu share

Upbit_market_share:
about 70%

event_initial_MFE:
> +7%

event_later_MAE:
-4.2%

event_swing:
-11.2pp

abnormal_withdrawal:
54B won

loss_coverage:
Upbit to cover using own assets

MFE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium_trust_watch
rerating_result = digital_asset_platform_merger_watch
stage_failure_type = platform_stage2_with_exchange_trust_4C_watch
```

---

## Case F — Toss / FacePay / U.S. IPO `success_candidate + privacy/data 4C-watch`

```text
direct_company = Viva Republica / Toss unlisted
listed_exposure = banks / fintech / payment / platform-finance read-through
case_type = success_candidate + privacy_watch
archetype = FINTECH_SUPERAPP_BIOMETRIC_PAYMENT
```

### stage date

```text
Stage 1:
2025
- Toss super-app
- Toss Bank / Toss Securities / Toss Payments
- biometric payment / global expansion

Stage 2:
2025-09-09
- Toss plans Australia launch by end-2025
- over 30M users
- aims to issue won stablecoin pending regulation
- preparing U.S. IPO in Q2 2026
- target valuation >$10B, possibly >$15B

Stage 2 validation:
2026-05
- FacePay reaches 4.8M users
- about 330,000 merchants
- target 10M users and 1M merchants by year-end

Stage 3:
없음
- unlisted
- payment take-rate, credit loss, bank NIM, data/privacy compliance, IPO pricing 확인 필요

Stage 4B:
IPO / FacePay / stablecoin narrative가 revenue보다 먼저 price에 반영되면 watch

Stage 4C:
biometric data breach, privacy regulation, credit cost, overseas launch failure
```

Toss는 R6에서 가장 흥미로운 unlisted fintech Stage 2다. Reuters는 Toss가 3,000만 명 이상 사용자를 보유하고, 2025년 말 호주 진출과 won stablecoin 발행, 2026년 Q2 U.S. IPO를 준비한다고 보도했다. FT는 Toss FacePay가 출시 이후 480만 명 사용자와 33만 retail locations를 확보했고, 연말 1,000만 사용자와 100만 merchants를 목표로 한다고 보도했다. 그러나 biometric payment는 privacy/data hard gate가 붙는다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters global expansion / FT FacePay anchors

stage3_price:
N/A

direct_listed_ticker:
N/A

Toss_users:
>30M

FacePay_users:
4.8M

FacePay_merchant_locations:
330,000

FacePay_user_target_year_end:
10M

FacePay_merchant_target_year_end:
1M

user_target_growth_needed:
10 / 4.8 - 1
= +108.3%

merchant_target_growth_needed:
1,000,000 / 330,000 - 1
= +203.0%

IPO_timing:
Q2 2026 planned

IPO_valuation_target:
> $10B, possibly > $15B

stablecoin_ambition:
won stablecoin pending regulation

MFE / MAE:
N/A, unlisted
```

### alignment

```text
score_price_alignment = success_candidate_unlisted
rerating_result = fintech_superapp_biometric_payment_watch
stage_failure_type = unlisted_stage2_privacy_gate
```

---

## Case G — Kakao / KakaoBank `governance 4C-watch`

```text
symbols = 035720 / 323410
case_type = 4C-watch
archetype = INTERNET_BANK_GOVERNANCE_4C
```

### stage date

```text
Stage 1:
2024
- KakaoBank mobile bank profitability
- Kakao financial ecosystem
- platform banking

Stage 4C-watch:
2024-07-22
- Kakao founder Kim Beom-su arrested
- suspected stock manipulation in SM Entertainment acquisition
- Kakao shares -3.4%
- Kakao group value around 86T won
- Kim controls 24% stake
- conviction could affect Kakao control of KakaoBank
- financial crime convicts cannot own significant bank stakes

Stage 3:
없음
- user growth / digital bank profit보다 major shareholder suitability gate가 먼저
```

KakaoBank는 mobile bank로 좋은 구조를 갖고 있어도, Kakao founder legal risk가 Green을 막는다. Reuters는 Kim Beom-su가 stock manipulation 혐의로 체포됐고, Kakao 주가는 3.4% 하락했다고 보도했다. 또한 유죄 확정 시 금융범죄자가 은행 지분을 크게 보유할 수 없는 규정 때문에 KakaoBank 지배력 문제가 생길 수 있다고 설명했다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters Kakao founder arrest / bank ownership-risk anchors

stage3_price:
N/A

Kakao_event_MAE:
-3.4%

Kakao_group_value_context:
86T won / $62B

Kim_controlled_stake:
24%

legal_risk:
suspected stock manipulation in SM Entertainment acquisition

bank_ownership_risk:
financial crime convicts cannot own significant bank stakes

KakaoBank_OHLC:
price_data_unavailable_after_deep_search

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = internet_bank_governance_gate
stage_failure_type = governance_4C_watch
```

---

## Case H — Stablecoin / kimchi bond / FX gate `overheat + macro 4C-watch`

```text
symbols = 377300 / LG CNS / Aton / ME2ON / banks / KRW
case_type = overheat + 4C-watch
archetype = STABLECOIN_POLICY_OVERHEAT_FX_GATE
```

### stage date

```text
Stage 1:
2025-06
- won stablecoin policy pledge
- digital-asset reform
- retail crypto / fintech frenzy

Stage 4B:
2025-06
- Kakao Pay >2x
- LG CNS +70%
- Aton +80%
- ME2ON 3x
- margin loans 20.5T won
- issuer license / reserve income / fee revenue not confirmed

Stage 4C-watch:
2025-06-30 / 2025-07-27
- Q1 dollar-backed stablecoin trading 57T won / $42B
- capital outflow via stablecoin channels >$19B in Q1 context
- BOK opposes non-bank issuance
- proposed bill allows issuers with 500M won equity
- Korea lifts 14-year kimchi-bond ban to attract FX liquidity

Stage 3:
없음
- regulated issuer framework, reserve income, fee revenue, FX stability 확인 전 Green 금지
```

stablecoin basket은 R6의 대표 `price_moved_without_evidence`다. FT는 Kakao Pay가 한 달 만에 2배 이상, LG CNS +70%, Aton +80%, ME2ON 3배를 기록했다고 보도했다. 그러나 같은 시기 dollar-backed stablecoin 거래는 Q1 57조 원, 약 420억 달러에 달했고, BoK는 capital outflow와 FX crisis 대응력을 우려했다. 한국은 이런 FX 압박에 대응해 14년간 금지했던 kimchi bond 투자를 다시 허용했다. ([Financial Times][8])

### 실제 가격경로 검증

```text
price_data_source:
FT stablecoin / kimchi-bond / FX-risk anchors

stage3_price:
N/A

Kakao_Pay_MFE:
> +100%

LG_CNS_MFE:
+70%

Aton_MFE:
+80%

ME2ON_MFE:
+200%

margin_loan_context:
20.5T won / $15B

stablecoin_trading_Q1:
57T won / $42B

capital_outflow_context:
> $19B in Q1 via stablecoin-related channels

proposed_minimum_equity_for_issuer:
500M won

kimchi_bond_ban_duration:
14 years

KRW_strength_after_policy:
1,347/USD

KRW_stabilization_level:
around 1,353/USD

issuer_license_confirmed:
false

reserve_income_confirmed:
false

fee_revenue_confirmed:
false

MFE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = price_moved_without_evidence + FX_4C_watch
rerating_result = stablecoin_policy_overheat
stage_failure_type = 4B_before_regulated_revenue
```

---

# 5. 이번 R6 case별 요약표

| case                 | 분류                    |                                                               실제 가격검증 | alignment        |
| -------------------- | --------------------- | --------------------------------------------------------------------: | ---------------- |
| 금융지주 value-up basket | success_candidate     | financial groups +4.2%, KOSPI +6.45%, treasury-share cancellation law | Stage 2          |
| 증권주 basket           | cyclical_success + 4B |                                   securities +13.5%, relative +7.05pp | cycle            |
| Samsung Life         | success_candidate     |                               Samsung Electronics stake sale 1.3T won | capital release  |
| Hana Bank / Dunamu   | success_candidate     |                   1T won for 6.55%, implied Dunamu 15.27T, Upbit >80% | digital equity   |
| NAVER / Dunamu       | event + 4C-watch      |                 15.13T deal, +7% → -4.2%, abnormal withdrawal 54B won | trust watch      |
| Toss / FacePay       | success_candidate     |                          4.8M users, 330k merchants, IPO >$10B target | unlisted Stage 2 |
| Kakao / KakaoBank    | 4C-watch              |                   Kakao -3.4%, founder 24% stake, bank ownership risk | governance gate  |
| stablecoin / FX      | overheat + 4C         |   Kakao Pay >2x, LG CNS +70%, Aton +80%, ME2ON 3x; stablecoin 57T won | price-only       |

---

# 6. score-price alignment 판정

```text
success_candidate:
- 금융지주 value-up basket
- Samsung Life
- Hana Bank / Dunamu
- Toss / FacePay

cyclical_success:
- 증권주 basket

event_premium:
- NAVER / Dunamu
- Hana Bank / Dunamu if bank valuation moves before equity-method revenue
- stablecoin policy basket

price_moved_without_evidence:
- stablecoin basket
- Toss IPO / FacePay if valuation moves before take-rate / credit-cost proof
- NAVER / Dunamu if digital-asset synergy priced before regulatory approval

thesis_break_watch:
- NAVER / Dunamu abnormal withdrawal
- Kakao / KakaoBank governance
- stablecoin FX outflow risk

4B-watch:
- securities +13.5% cycle rally
- stablecoin names +70%~3x
- NAVER +7% then -4.2% event reversal
- financial groups rerating if PBR moves before ROE/CET1/shareholder return

hard_4C_confirmed:
- false
```

---

# 7. 점수비중 교정

## 올릴 축

```text
ROE_sustainability +5
CET1_or_capital_buffer +5
real_buyback_cancellation +5
recurring_dividend_policy +4
credit_cost_control +5
brokerage_fee_sustainability +4
regulated_digital_revenue +5
equity_method_visibility +4
platform_trust +5
FX_stability +5
data_privacy_control +5
```

### 왜 올리나

금융지주 value-up은 policy와 PBR만으로는 부족하다. 실제 ROE, CET1, credit cost, 반복 소각·배당이 필요하다. Hana/Dunamu, NAVER/Dunamu, Toss는 디지털금융 Stage 2가 강하지만, regulated revenue, equity-method earnings, platform trust, privacy/data gate가 확인되어야 한다.

## 내릴 축

```text
low_PBR_only -5
policy_valueup_only -5
market_volume_spike_only -4
digital_asset_equity_option_only -4
stablecoin_policy_theme_only -5
nonbank_stablecoin_FX_risk -5
exchange_trust_break -5
biometric_data_risk -4
major_shareholder_legal_risk -5
event_rally_before_regulated_revenue -5
```

### 왜 내리나

증권주 +13.5%는 좋은 cycle이지만 Green은 아니다. stablecoin basket은 regulated revenue 없이 2~3배 움직였다. NAVER/Dunamu는 deal과 동시에 abnormal withdrawal이 나왔다. KakaoBank는 모바일은행 성장성보다 대주주 적격성 risk가 먼저다.

## Green gate 강화 조건

```text
R6 Stage 3-Green 필수:
1. ROE 개선 또는 유지
2. CET1 / K-ICS / capital buffer 충분
3. credit cost / PF risk 안정
4. 실제 자사주 소각 / 반복 배당 확인
5. brokerage / IB / trading income 지속성 확인
6. 디지털자산은 regulated revenue 또는 equity-method earnings 확인
7. platform / exchange trust risk 없음
8. data privacy / biometric risk 통과
9. FX outflow / stablecoin macro risk 통과
10. 가격경로가 evidence 이후 따라옴

금지:
저PBR만 있음
정책 value-up만 있음
증권주 거래대금 spike만 있음
stablecoin theme only
디지털자산 지분투자만 있음
대주주 법적 risk 존재
exchange trust incident 존재
privacy/data gate unresolved
```

## 4B 조기감지 조건

```text
4B-watch:
PBR rerating이 ROE/CET1보다 먼저 진행
증권주가 거래대금 cycle 하나로 +10% 이상 급등
디지털자산 지분투자로 은행주가 먼저 rerating
stablecoin 관련주가 실제 수익모델 없이 2~3배 급등
Naver/Dunamu 같은 대형 deal이 regulatory approval 전 가격화
Toss IPO / FacePay narrative가 take-rate / credit cost 전 valuation화
금융지주 value-up이 실제 소각/배당보다 먼저 가격화

4B-elevated:
credit cost가 낮아 보이지만 PF risk 남음
CET1 buffer가 줄어드는데 주주환원 기대 과도
exchange volume peak와 digital-asset equity investment가 겹침
FX outflow가 심한데 stablecoin theme이 급등
privacy/data issue가 있는데 biometric payment가 premium 받음
```

## 4C hard gate 조건

```text
PF credit cost spike
CET1 / K-ICS deterioration
buyback cancellation failure
dividend retreat
bank ownership-suitability failure
financial crime conviction affecting bank control
exchange abnormal withdrawal / hack
stablecoin-driven FX outflow
non-bank issuer failure
biometric data breach
major credit loss from fintech lending
```

이번 R6 Loop 12에서는 hard 4C를 억지로 확정하지 않는다. 다만 **Kakao/KakaoBank governance**, **NAVER/Dunamu abnormal withdrawal**, **stablecoin FX outflow**, **Toss biometric privacy gate**는 모두 강한 4C-watch로 둔다.

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

## docs/round/round_190.md 요약

```md
# R6 Loop 12. Financial / Capital Allocation / Digital Finance Price Validation

이번 라운드는 R6 Loop 12 price-validation 라운드다.

핵심 결론:
- Financial holding value-up basket is Stage 2, not Green. Commercial Act revision requires newly acquired treasury shares to be cancelled within one year. On KOSPI 7000 day, financial groups rose +4.2% while KOSPI rose +6.45%, implying -2.25pp relative underperformance.
- Securities basket is cyclical_success and 4B-watch. On 2026-05-06, securities firms jumped +13.5%, outperforming KOSPI by +7.05pp. Brokerage/IB revenue and ROE must confirm before Green.
- Samsung Life is insurance NAV capital-release Stage 2. It will divest 1.3T won worth of Samsung Electronics shares to resolve financial-company governance regulation risk.
- Hana Bank / Dunamu is bank digital-asset equity-option Stage 2. Hana acquires 6.55% of Dunamu for about 1T won, implying about 15.27T won Dunamu equity value. Upbit handles more than 80% of Korean virtual asset trading volume.
- NAVER / Dunamu is platform-merger Stage 2 plus exchange-trust 4C-watch. Deal value 15.13T won, Naver initially +7% but later -4.2% after 54B won abnormal withdrawal from Upbit.
- Toss / FacePay is unlisted fintech Stage 2. Toss has over 30M users, FacePay has 4.8M users and 330k merchant locations, and IPO valuation target is above $10B. Privacy/data gate remains.
- Kakao / KakaoBank is governance 4C-watch. Kakao founder arrest caused Kakao -3.4%, and conviction risk could affect KakaoBank control due bank ownership restrictions.
- Stablecoin / kimchi bond / FX gate is overheat plus 4C-watch. Kakao Pay >2x, LG CNS +70%, Aton +80%, ME2ON 3x before issuer license, reserve income or fee revenue; Q1 stablecoin trading reached 57T won / $42B.
```

## docs/checkpoints/checkpoint_28a_round190_r6_loop12.md 요약

```md
# Checkpoint 28A Round 190 R6 Loop 12 Financial Capital Digital Price Validation

## 반영 내용
- R6 Loop 12 price-validation 라운드를 추가했다.
- Financial value-up, brokerage cycle, insurance NAV capital release, bank digital-asset equity option, platform merger trust watch, fintech biometric payment, internet-bank governance, stablecoin FX risk를 비교했다.
- Reuters / WSJ / FT anchors로 가능한 MFE/MAE 및 event metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- ROE sustainability, CET1/capital buffer, real buyback cancellation, credit-cost control, brokerage fee sustainability, regulated digital revenue, platform trust, FX stability, data privacy control 가중치 강화
- low-PBR only, policy value-up only, market-volume spike only, stablecoin theme-only, exchange trust break, biometric data risk, major shareholder legal risk 감점 강화
```

## data/e2r_case_library/cases_r6_loop12_round190.jsonl 초안

```jsonl
{"case_id":"r6_loop12_financial_holdings_valueup_stage2","symbol":"105560/055550/086790/316140","company_name":"Korean financial holding value-up basket","case_type":"success_candidate","primary_archetype":"BANK_VALUEUP_ROE_PBR_RERATING","stage2_date":"2026-02-25/2026-05-06","price_validation":{"price_data_source":"Reuters Commercial Act / KOSPI 7000 anchors","stage3_price":null,"treasury_share_rule":"newly acquired treasury shares must be cancelled within 1 year","existing_treasury_share_grace_period_months":6,"financial_groups_event_mfe_pct":4.2,"kospi_same_context_pct":6.45,"relative_performance_vs_kospi_pp":-2.25,"foreign_net_purchase_krw_trn":3.1,"foreign_net_purchase_usd_bn":2.13,"price_validation_status":"reported_sector_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate","rerating_result":"financial_holding_valueup_stage2","notes":"Value-up policy and sector rally are Stage 2; ROE/CET1/credit cost and actual recurring shareholder return required before Green."}
{"case_id":"r6_loop12_securities_market_volume_cycle","symbol":"securities_basket","company_name":"Korean securities firms basket","case_type":"cyclical_success","primary_archetype":"BROKERAGE_MARKET_VOLUME_CYCLE","stage2_date":"2026-05-06","stage4b_date":"2026-05-06","price_validation":{"price_data_source":"Reuters KOSPI 7000 sector-return anchor","stage3_price":null,"kospi_event_return_pct":6.45,"kospi_intraday_high_return_pct":7.06,"securities_firms_event_mfe_pct":13.5,"financial_groups_event_mfe_pct":4.2,"securities_relative_outperformance_vs_kospi_pp":7.05,"foreign_net_purchase_krw_trn":3.1,"foreign_net_purchase_usd_bn":2.13,"price_validation_status":"reported_sector_anchor_not_full_ohlc"},"score_price_alignment":"cyclical_success","rerating_result":"brokerage_market_volume_cycle_watch","notes":"Securities +13.5% is cyclical success and 4B-watch until brokerage/IB revenue and ROE confirm."}
{"case_id":"r6_loop12_samsung_life_nav_capital_release","symbol":"032830","company_name":"Samsung Life","case_type":"success_candidate","primary_archetype":"INSURANCE_NAV_CAPITAL_RELEASE","stage2_date":"2026-03-19","price_validation":{"price_data_source":"Reuters Samsung Electronics stake-sale anchor","stage3_price":null,"samsung_electronics_stake_sale_krw_trn":1.3,"samsung_electronics_stake_sale_usd_mn":867.07,"transaction_purpose":"resolve financial-company governance regulation risk","fx_rate":1499.3,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_regulatory_watch","rerating_result":"insurance_NAV_capital_release_watch","notes":"Capital release is Stage 2; K-ICS, CSM, dividend/buyback and use of proceeds required before Green."}
{"case_id":"r6_loop12_hana_bank_dunamu_equity_option","symbol":"086790","company_name":"Hana Financial / Hana Bank / Dunamu","case_type":"success_candidate","primary_archetype":"BANK_DIGITAL_ASSET_EQUITY_OPTION","stage2_date":"2026-05-14/2026-05-15","price_validation":{"price_data_source":"Reuters/WSJ transaction anchors","stage3_price":null,"transaction_value_krw_trn":1.0,"wsj_transaction_value_krw_trn":1.003,"stake_acquired_pct":6.55,"shares_acquired_mn":2.284,"implied_dunamu_equity_value_krw_trn":15.27,"upbit_trading_volume_share_pct":80,"kakao_investment_remaining_stake_pct":4.03,"expected_closing":"2026-06-15","business_validation":"blockchain-based overseas remittance technical verification completed","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"bank_digital_asset_equity_option_watch","notes":"Dunamu stake is Stage 2; regulated revenue, equity-method earnings, capital impact and exchange trust required before Green."}
{"case_id":"r6_loop12_naver_dunamu_platform_merger_trust_watch","symbol":"035420","company_name":"NAVER / NAVER Financial / Dunamu","case_type":"success_candidate","primary_archetype":"DIGITAL_ASSET_PLATFORM_MERGER_TRUST_WATCH","stage2_date":"2025-11-27","stage4b_date":"2025-11-27","stage4c_date":"2025-11-27_watch","price_validation":{"price_data_source":"Reuters transaction/event-return/trust-risk anchor","stage3_price":null,"deal_value_krw_trn":15.13,"deal_value_usd_bn":10.27,"exchange_ratio_naver_financial_per_dunamu":2.54,"upbit_market_share_pct":70,"event_initial_mfe_pct":7.0,"event_later_mae_pct":-4.2,"event_swing_pp":-11.2,"abnormal_withdrawal_krw_bn":54,"loss_coverage":"Upbit to cover using own assets","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_trust_watch","rerating_result":"digital_asset_platform_merger_watch","notes":"Digital-asset platform Stage 2 but abnormal withdrawal creates exchange-trust 4C-watch."}
{"case_id":"r6_loop12_toss_facepay_fintech_superapp_privacy_watch","symbol":"unlisted_Toss/payment_fintech_readthrough","company_name":"Toss / Viva Republica / FacePay","case_type":"success_candidate","primary_archetype":"FINTECH_SUPERAPP_BIOMETRIC_PAYMENT","stage2_date":"2025-09-09/2026-05","price_validation":{"price_data_source":"Reuters global expansion + FT FacePay anchors","stage3_price":null,"direct_listed_ticker":"N/A","toss_users_mn":30,"facepay_users_mn":4.8,"facepay_merchant_locations":330000,"facepay_user_target_year_end_mn":10,"facepay_merchant_target_year_end":1000000,"user_target_growth_needed_pct":108.3,"merchant_target_growth_needed_pct":203.0,"ipo_timing":"Q2 2026 planned","ipo_valuation_target_usd_bn":10,"ipo_valuation_possible_usd_bn":15,"stablecoin_ambition":"won stablecoin pending regulation","price_validation_status":"unlisted_no_ohlc"},"score_price_alignment":"success_candidate_unlisted","rerating_result":"fintech_superapp_biometric_payment_watch","notes":"Biometric payment is Stage 2; take-rate, credit cost, privacy/data compliance and IPO pricing required."}
{"case_id":"r6_loop12_kakao_kakaobank_governance_gate","symbol":"035720/323410","company_name":"Kakao / KakaoBank","case_type":"4c_watch","primary_archetype":"INTERNET_BANK_GOVERNANCE_4C","stage4c_date":"2024-07-22","price_validation":{"price_data_source":"Reuters Kakao founder arrest / bank ownership-risk anchors","stage3_price":null,"kakao_event_mae_pct":-3.4,"kakao_group_value_krw_trn":86,"kakao_group_value_usd_bn":62,"kim_controlled_stake_pct":24,"legal_risk":"suspected stock manipulation in SM Entertainment acquisition","bank_ownership_risk":"financial crime convicts cannot own significant bank stakes","price_validation_status":"kakaobank_ohlc_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"internet_bank_governance_gate","notes":"KakaoBank Green is blocked by major-shareholder legal and bank-ownership suitability risk."}
{"case_id":"r6_loop12_stablecoin_policy_overheat_fx_gate","symbol":"377300/LG_CNS/Aton/ME2ON/KRW/banks","company_name":"Stablecoin policy basket / FX gate","case_type":"overheat","primary_archetype":"STABLECOIN_POLICY_OVERHEAT_FX_GATE","stage1_date":"2025-06","stage4b_date":"2025-06","stage4c_date":"2025-06-30/2025-07-27_watch","price_validation":{"price_data_source":"FT stablecoin / kimchi-bond / FX-risk anchors","stage3_price":null,"kakao_pay_mfe_pct":100,"lg_cns_mfe_pct":70,"aton_mfe_pct":80,"me2on_mfe_pct":200,"margin_loan_context_krw_trn":20.5,"stablecoin_trading_q1_krw_trn":57,"stablecoin_trading_q1_usd_bn":42,"capital_outflow_context_usd_bn":19,"proposed_minimum_equity_for_issuer_krw_mn":500,"kimchi_bond_ban_duration_years":14,"krw_strength_after_policy_per_usd":1347,"krw_stabilization_level_per_usd":1353,"issuer_license_confirmed":false,"reserve_income_confirmed":false,"fee_revenue_confirmed":false,"price_validation_status":"reported_return_anchor_not_full_ohlc"},"score_price_alignment":"price_moved_without_evidence_FX_4C_watch","rerating_result":"stablecoin_policy_overheat","notes":"Stablecoin policy rally happened before regulated revenue, while FX outflow risk remains 4C-watch."}
```

## data/sector_taxonomy/score_weight_profiles_round190_r6_loop12_v1.csv 초안

```csv
archetype,roe_sustainability,capital_buffer,real_buyback_cancel,recurring_dividend,credit_cost,brokerage_fee_sustainability,regulated_digital_revenue,equity_method_visibility,platform_trust,fx_stability,data_privacy,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
BANK_VALUEUP_ROE_PBR_RERATING,+5,+5,+5,+4,+5,+0,+0,+0,+3,+3,+1,-5,+4,+5,Financial holding value-up is Stage 2 until ROE/CET1/credit cost and recurring capital return confirm.
BROKERAGE_MARKET_VOLUME_CYCLE,+4,+3,+0,+2,+3,+5,+0,+0,+3,+3,+1,-4,+5,+4,Securities +13.5% is cyclical success and 4B-watch before revenue/ROE confirmation.
INSURANCE_NAV_CAPITAL_RELEASE,+3,+5,+2,+4,+3,+0,+0,+0,+3,+2,+1,-3,+4,+4,Samsung Life stake sale is capital release Stage 2; K-ICS/CSM/use of proceeds needed.
BANK_DIGITAL_ASSET_EQUITY_OPTION,+2,+4,+0,+1,+2,+1,+5,+5,+5,+4,+3,-4,+5,+5,Hana/Dunamu is Stage 2 until regulated revenue/equity-method earnings and trust confirm.
DIGITAL_ASSET_PLATFORM_MERGER_TRUST_WATCH,+2,+3,+0,+1,+2,+1,+5,+4,+5,+4,+4,-5,+5,+5,Naver/Dunamu has exchange abnormal-withdrawal 4C-watch.
FINTECH_SUPERAPP_BIOMETRIC_PAYMENT,+3,+3,+0,+0,+4,+3,+5,+0,+5,+4,+5,-4,+5,+5,Toss FacePay is unlisted Stage 2 with biometric privacy/data gate.
INTERNET_BANK_GOVERNANCE_4C,+0,+4,+0,+0,+4,+2,+2,+0,+5,+2,+3,0,+4,+5,KakaoBank Green blocked by major-shareholder legal/ownership risk.
STABLECOIN_POLICY_OVERHEAT_FX_GATE,+0,+2,+0,+0,+0,+0,+5,+0,+3,+5,+4,-5,+5,+5,Stablecoin basket moved before issuer license/reserve income/fee revenue and creates FX 4C-watch.
```

---

# 이번 R6 Loop 12 결론

```text
1. 금융지주 value-up은 아직 Stage 2다.
   상법개정과 PBR rerating 기대는 좋지만, ROE/CET1/credit cost/반복 소각 전 Green은 아니다.

2. 증권주는 cyclical_success다.
   +13.5%는 거래대금 cycle 수혜지만, brokerage/IB revenue와 ROE 확인 전 Stage 3는 아니다.

3. Samsung Life는 insurance NAV capital release Stage 2다.
   지분 매각대금이 K-ICS, CSM, 배당·소각으로 닫혀야 한다.

4. Hana Bank / Dunamu는 은행 digital-asset equity option Stage 2다.
   지분법 이익, regulated revenue, 자본비율 영향, exchange trust 전 Green 금지다.

5. NAVER / Dunamu는 platform Stage 2와 exchange-trust 4C-watch가 동시에 떴다.
   +7%에서 -4.2%로 뒤집힌 가격경로가 그 증거다.

6. Toss / FacePay는 unlisted fintech Stage 2다.
   biometric payment 성장성은 크지만 privacy/data gate가 붙는다.

7. KakaoBank는 governance 4C-watch다.
   모바일은행 성장성보다 대주주 적격성 risk가 먼저다.

8. Stablecoin basket은 R6의 대표 price_moved_without_evidence다.
   regulated revenue 전 2~3배 상승했고, 동시에 FX outflow gate가 붙는다.
```

한 문장으로 압축하면:

> **R6에서 진짜 Stage 3는 “저PBR·밸류업·증권주·디지털자산·스테이블코인이 뜬다”가 아니라, ROE·자본비율·credit cost·실제 소각·반복 fee income·regulated digital revenue·platform trust·FX stability가 실제로 확인되는 순간이다.**

* [Reuters](https://www.reuters.com/world/asia-pacific/south-koreas-kospi-share-index-tops-7000-first-time-2026-05-06/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-parliament-approves-commercial-act-revision-aimed-boosting-share-2026-02-25/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/samsung-life-divest-13-trln-won-worth-samsung-electronics-shares-2026-03-19/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/hana-bank-acquire-stake-dunamu-700-mln-filing-says-2026-05-14/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/navers-payment-arm-acquire-south-korean-crypto-exchange-operator-10-bln-deal-2025-11-27/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/finance/south-korean-fintech-toss-plans-global-push-starting-australia-aims-issue-won-2025-09-09/?utm_source=chatgpt.com)
* [Financial Times](https://www.ft.com/content/f48b4605-1aa9-4549-9197-fc1c2a361b90?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/technology/south-korean-court-approves-arrest-warrant-kakao-founder-2024-07-22/?utm_source=chatgpt.com)
* [Financial Times](https://www.ft.com/content/4b19bf90-4202-4fe7-8caf-d7db6deeb768?utm_source=chatgpt.com)
* [Financial Times](https://www.ft.com/content/0f93c015-6e1f-4ef3-accc-8d060983284a?utm_source=chatgpt.com)
* [Financial Times](https://www.ft.com/content/106a1e79-0a64-4c51-b74f-ad4d4f8896f6?utm_source=chatgpt.com)

[1]: https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-parliament-approves-commercial-act-revision-aimed-boosting-share-2026-02-25/?utm_source=chatgpt.com "South Korea parliament approves commercial act revision aimed at boosting share valuations"
[2]: https://www.reuters.com/world/asia-pacific/south-koreas-kospi-share-index-tops-7000-first-time-2026-05-06/?utm_source=chatgpt.com "Korea's KOSPI breaks 7,000 as AI rally catapults Samsung into $1 trillion club"
[3]: https://www.reuters.com/world/asia-pacific/samsung-life-divest-13-trln-won-worth-samsung-electronics-shares-2026-03-19/?utm_source=chatgpt.com "Samsung Life to divest 1.3 trln won worth of Samsung Electronics' shares"
[4]: https://www.reuters.com/world/asia-pacific/hana-bank-acquire-stake-dunamu-700-mln-filing-says-2026-05-14/?utm_source=chatgpt.com "Hana Bank to acquire stake in Dunamu for $700 mln, filing says"
[5]: https://www.reuters.com/world/asia-pacific/navers-payment-arm-acquire-south-korean-crypto-exchange-operator-10-bln-deal-2025-11-27/?utm_source=chatgpt.com "Naver's payment arm to acquire South Korean crypto exchange operator in $10 bln deal"
[6]: https://www.reuters.com/business/finance/south-korean-fintech-toss-plans-global-push-starting-australia-aims-issue-won-2025-09-09/?utm_source=chatgpt.com "South Korean fintech Toss plans global push starting in Australia, aims to issue won stablecoin"
[7]: https://www.reuters.com/business/south-korea-court-decide-arrest-warrant-kakao-founder-2024-07-22/?utm_source=chatgpt.com "South Korea court to decide on arrest warrant for Kakao founder"
[8]: https://www.ft.com/content/4b19bf90-4202-4fe7-8caf-d7db6deeb768?utm_source=chatgpt.com "Crypto-crazy investors make South Korea the best-performing market in Asia"

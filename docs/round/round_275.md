순서상 이번은 **R6 Loop 13 — 금융·자본배분·디지털금융 가격경로 검증 라운드**다.

```text
round = R6 Loop 13
round_id = round_203
large_sector = FINANCIALS_CAPITAL_ALLOCATION_DIGITAL_FINANCE
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true_for_digital_asset_operational_reference
direct_listed_hard_4c_confirmed = false
next_round = R7 Loop 13
```

이번 R6 Loop 13은 **금융지주 value-up, 지주사 할인 해소, 보험사 보유지분 규제, 은행의 디지털자산 지분투자, 인터넷은행 IPO, stablecoin 과열, crypto exchange 운영사고, 증권·금융주 거래대금 event premium**을 본다.

이번에도 KRX/Naver/Yahoo/Stooq 기준 **수정주가 일봉 전체 구간**은 안정적으로 확보하지 못했다. 그래서 30D/90D/180D full OHLC는 만들지 않고, Reuters / FT / WSJ / Barron’s가 보도한 **event return, 거래금액, buyback·지분매각·IPO 금액, 시장점유율, 규제·운영사고 anchor**만 계산했다. full OHLC가 필요한 칸은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R6 = 금융·자본배분·디지털금융
```

R6에서 진짜 Stage 3는 “value-up”, “자사주”, “금융지주”, “stablecoin”, “Dunamu”, “인터넷은행”, “증권주 거래대금”, “보험사 보유지분”이라는 단어가 아니다.

진짜 Stage 3는 **자본환원 실행, 보통주자본비율 방어, ROE 개선, 순이자마진·수수료 안정, 리스크가중자산 통제, 규제 승인, 디지털자산 trust, 사이버·운영 리스크 통과, 실제 EPS/FCF bridge**가 같이 닫히는 순간이다.

---

# 2. 대상 canonical archetype

```text
BANK_VALUE_UP_RERATING_STAGE2
HOLDCO_DISCOUNT_BUYBACK_CANCELLATION
INSURANCE_HOLDING_STAKE_REGULATORY_GATE
DIGITAL_ASSET_BANK_STAKE_STAGE2
FINTECH_CRYPTO_M_AND_A_TRUST_GATE
INTERNET_BANK_IPO_OVERHANG
STABLECOIN_POLICY_OVERHEAT_FX_GATE
CRYPTO_EXCHANGE_OPERATIONAL_HARD_REFERENCE
SECURITIES_TRADING_VOLUME_EVENT_PREMIUM
```

---

# 3. deep sub-archetype

```text
금융지주 value-up:
- KB / Shinhan / Hana / Woori
- corporate reform / treasury share cancellation
- PBR rerating / shareholder return
- CET1 / NIM / credit cost / RWA risk

지주사 할인:
- SK Square
- SK Hynix 20% stake
- buyback + cancellation
- activist / Palliser / Korea Discount

보험·보유지분:
- Samsung Life
- Samsung Electronics stake divestiture
- financial-company governance regulation
- book-value discount / holding-company optionality

디지털자산:
- Hana Bank / Dunamu
- Naver Financial / Dunamu
- Upbit market share
- abnormal withdrawal / exchange trust gate

인터넷은행:
- K Bank IPO
- customer base 10M+
- operating profit growth
- IPO valuation vs deposit/loan quality / Upbit dependence

Stablecoin:
- Kakao Pay / LG CNS / Aton / ME2ON
- won stablecoin policy
- issuer equity threshold
- FX outflow / BOK concern

Crypto operation:
- Bithumb accidental bitcoin distribution
- 620,000 BTC error
- 99.7% recovery
- 17% BTC price drop on exchange
- regulator inspection risk

증권·거래대금:
- securities firms rally during KOSPI 7,000
- financial groups +4.2%
- securities +13.5%
- trading-volume event premium, not Green
```

---

# 4. 국장 신규 후보 case

## Case A — 금융지주 value-up basket `success_candidate + 4B-watch`

```text
symbols = 105560 / 055550 / 086790 / 316140
case_type = success_candidate + 4B-watch
archetype = BANK_VALUE_UP_RERATING_STAGE2
```

### stage date

```text
Stage 1:
2024-02~2024-05
- Corporate Value-up Programme
- shareholder return / Korea discount 해소 기대
- 은행·보험·증권 저PBR sector rerating

Stage 2:
2024-05-02
- FSC publishes voluntary value-up guidelines
- companies encouraged to disclose mid/long-term targets
- plans include investment, shareholder return, business portfolio reorganisation
- KOSPI reaction muted, down about -0.2%

Stage 2 강화:
2026-02-25
- Commercial Act revision requires newly acquired treasury shares to be cancelled within one year
- governance reform strengthens value-up narrative

Stage 4B:
2026-05-06
- KOSPI 7,000 event
- financial groups +4.2%
- securities firms +13.5%
- financial-sector rally driven by market confidence and trading-volume expectations

Stage 3:
없음
- value-up policy and sector rally are not Green
- actual buyback cancellation, dividend payout, CET1, credit cost, ROE, NIM 확인 필요
```

금융지주 value-up basket은 R6의 좋은 Stage 2다. 2024년 5월 value-up guideline은 기업이 중장기 목표와 투자·주주환원·사업재편 계획을 세우도록 유도했지만, 시장 반응은 KOSPI -0.2%로 밋밋했다. 2026년 Commercial Act 개정으로 새로 취득한 treasury shares를 1년 내 소각해야 하는 규제가 붙으면서 구조적 의미는 강해졌다. 그러나 KOSPI 7,000 당일 금융그룹 +4.2%, 증권주 +13.5%는 trading-volume event premium도 같이 붙는다. ([Reuters][1])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters / FT policy and sector-return anchors",
  "stage3_price": null,
  "value_up_guideline_event_kospi_pct": -0.2,
  "commercial_act_treasury_cancellation_rule": "newly acquired treasury shares must be cancelled within one year",
  "kospi_7000_event_date": "2026-05-06",
  "kospi_event_mfe_pct": 6.45,
  "securities_firms_event_mfe_pct": 13.5,
  "financial_groups_event_mfe_pct": 4.2,
  "foreign_net_purchase_krw_trn": 3.1,
  "actual_bank_cet1_credit_cost_nim_verified": false,
  "mfe_30d_90d_180d_1y": "price_data_unavailable_after_deep_search",
  "mae_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_4B_watch
rerating_result = bank_value_up_stage2
stage_failure_type = policy_and_sector_rally_not_bank_quality_green
```

---

## Case B — SK Square `structural_success_candidate / holdco discount buyback`

```text
symbol = 402340
case_type = structural_success_candidate
archetype = HOLDCO_DISCOUNT_BUYBACK_CANCELLATION
```

### stage date

```text
Stage 1:
2024
- activist engagement by Palliser Capital
- SK Square discount to SK Hynix stake
- Korea discount / holding-company value-up narrative

Stage 2:
2024-11-21
- SK Square announces buyback / cancellation plan
- cancel 100B won worth of shares bought in April
- repurchase another 100B won and cancel within three months
- nominates independent director
- SK Square holds 20% stake in SK Hynix
- market value less than half of $18B stake value

Stage 3:
없음
- buyback/cancellation is strong Stage 2
- Green requires NAV discount narrowing, recurring capital return, governance durability, non-Hynix asset clarity

Stage 4B:
SK Hynix rally alone drives SK Square before own capital-return discipline proves durable
```

SK Square는 R6 자본배분 case로 아주 깔끔하다. 단순 지주사 할인 이야기가 아니라, 1000억 원 규모 기존 매입분 소각과 추가 1000억 원 매입·소각 계획이 나왔고, 독립이사 선임까지 같이 붙었다. 또 SK Square는 SK Hynix 지분 20%를 보유하고, 당시 그 지분가치 $18B보다 회사 시가총액이 절반 이하라는 discount가 확인됐다. 다만 Green은 한 번의 buyback이 아니라 **지속적 소각, NAV discount 축소, governance durability**로 확인해야 한다. ([Reuters][2])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters SK Square buyback / discount anchor",
  "stage3_price": null,
  "cancel_existing_buyback_krw_bn": 100,
  "new_buyback_krw_bn": 100,
  "total_announced_cancel_buyback_krw_bn": 200,
  "sk_hynix_stake_pct": 20,
  "sk_hynix_stake_value_usd_bn": 18,
  "market_value_status": "less_than_half_of_stake_value",
  "implied_market_cap_upper_bound_usd_bn": 9,
  "discount_to_stake_value_min_pct": 50,
  "palliser_stake_pct": 1,
  "independent_director_nomination": true,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = holdco_discount_buyback_cancellation_stage2
stage_failure_type = buyback_plan_not_NAV_discount_green_until_executed_and_repeated
```

---

## Case C — Samsung Life `insurance holding-stake regulatory gate`

```text
symbol = 032830
case_type = success_candidate + 4C-watch
archetype = INSURANCE_HOLDING_STAKE_REGULATORY_GATE
```

### stage date

```text
Stage 1:
2026-03
- Samsung Life holds large Samsung Electronics stake
- insurance governance / financial-company ownership regulation
- holding-company discount optionality

Stage 2:
2026-03-19
- Samsung Life to divest 1.3T won / $867.07M worth of Samsung Electronics shares
- sale aimed at addressing local financial-company governance regulation risk

Stage 2 valuation context:
2026-05
- hedge-fund investors identify Samsung Life as indirect Samsung Electronics exposure
- Samsung Life owns about 10% stake in Samsung Electronics
- trades around 50% of book value, per Barron's summary

Stage 3:
없음
- stake sale/regulatory compliance is not Green
- insurance earnings, capital adequacy, shareholder return, realized gain use required

Stage 4B:
Samsung Electronics $1T rally drives Samsung Life before insurance capital-return bridge
```

Samsung Life는 R6에서 보험사·지주성 보유지분의 교차 case다. Samsung Electronics 지분가치가 커지면 valuation optionality가 생기지만, 금융회사 지배구조 규제 때문에 1.3조 원 규모 Samsung Electronics 지분 매각이 필요해졌다. Barron’s는 Samsung Life가 Samsung Electronics 지분 약 10%를 보유하고도 book value의 약 50%에 거래된다고 소개했다. 그러나 이건 보험영업 Green이 아니다. **지분매각 후 자본적정성, 배당·자사주, 보험 손익**이 확인되어야 한다. ([Reuters][3])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters Samsung Life divestiture + Barron's valuation context",
  "stage3_price": null,
  "samsung_electronics_stake_sale_krw_trn": 1.3,
  "samsung_electronics_stake_sale_usd_mn": 867.07,
  "samsung_life_samsung_electronics_stake_context_pct": 10,
  "book_value_multiple_context": "about_0.5x_book_value",
  "regulatory_driver": "financial-company governance regulation risk",
  "use_of_proceeds_confirmed_for_shareholder_return": false,
  "insurance_capital_return_bridge_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_4C_watch
rerating_result = insurance_holdco_value_stage2
stage_failure_type = stake_value_and_regulatory_sale_not_insurance_green
```

---

## Case D — Hana Bank / Dunamu `digital asset bank stake Stage 2`

```text
symbol = 086790
case_type = success_candidate + 4B-watch
archetype = DIGITAL_ASSET_BANK_STAKE_STAGE2
```

### stage date

```text
Stage 1:
2026-05-14
- Hana Bank enters Dunamu shareholder base
- commercial bank direct digital-asset exposure
- Upbit dominance / stablecoin / overseas remittance optionality

Stage 2:
2026-05-14 / 2026-05-15
- Hana Bank to buy 6.55% Dunamu stake
- purchase price about 1.003T won / $672.5M~$700M
- shares bought from Kakao affiliate
- Hana becomes fourth-largest shareholder
- Dunamu operates Upbit
- Upbit handles more than 80% of Korean virtual-asset trading volume, per Reuters source
- Hana/Dunamu blockchain overseas-remittance technical verification completed, per WSJ summary

Stage 3:
없음
- equity stake is Stage 2
- regulatory approval, earnings pickup, capital charge, exchange trust, stablecoin framework required

Stage 4B:
bank stock rerates on crypto optionality before capital/earnings contribution proves out
```

Hana/Dunamu는 R6의 핵심 신규 case다. Hana Bank가 Dunamu 지분 6.55%를 1.003조 원에 사들이며, 한국 은행권의 가장 큰 digital-asset investment가 됐다. Upbit은 한국 virtual asset trading volume의 80% 이상을 차지하는 dominant exchange로 소개됐다. 하지만 은행 Green은 지분투자가 아니라 **자본규제, 손익 인식, digital-remittance revenue, exchange trust, stablecoin regulation**이 통과될 때다. ([Reuters][4])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters / WSJ Hana-Dunamu stake anchors",
  "stage3_price": null,
  "dunamu_stake_pct": 6.55,
  "purchase_price_krw_trn": 1.003,
  "purchase_price_usd_mn": 672.5,
  "implied_dunamu_equity_value_krw_trn": 15.31,
  "seller": "Kakao affiliate",
  "hana_resulting_rank": "fourth_largest_shareholder",
  "upbit_virtual_asset_trading_share_pct": 80,
  "remittance_technical_verification_completed": true,
  "regulatory_capital_earnings_bridge_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_4B_watch
rerating_result = bank_digital_asset_stake_stage2
stage_failure_type = equity_stake_not_regulated_revenue_green
```

---

## Case E — Naver Financial / Dunamu `fintech M&A trust gate`

```text
symbol = 035420
case_type = success_candidate + event_premium + 4C-watch
archetype = FINTECH_CRYPTO_M_AND_A_TRUST_GATE
```

### stage date

```text
Stage 1:
2025-11-27
- Naver Financial to acquire Dunamu via all-stock deal
- Upbit / Naver Pay / stablecoin optionality
- fintech expansion beyond advertising/commerce/content

Stage 2:
2025-11-27
- all-stock deal value 15.13T won / $10.27B
- Naver Financial issues 2.54 shares for every one Dunamu share
- Upbit has about 70% Korean crypto exchange market share in source context

Stage 4B:
2025-11-27
- Naver shares initially +7%+

Stage 4C-watch:
2025-11-27
- Upbit abnormal withdrawal 54B won
- Naver later trades -4.2%
- Upbit says it will cover loss using own assets

Stage 3:
없음
- deal announcement is not Green
- closing, regulatory approval, exchange trust recovery, take-rate / earnings bridge required
```

Naver/Dunamu는 R6의 “digital finance M&A는 trust gate가 먼저”라는 표본이다. 15.13조 원 all-stock deal은 거대하지만, 같은 날 540억 원 abnormal withdrawal 뉴스가 나오자 Naver는 +7%에서 -4.2%로 뒤집혔다. 이 가격경로 자체가 R6 교정값이다. **M&A synergy보다 exchange trust가 먼저**다. ([Reuters][5])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters Naver-Dunamu deal and abnormal-withdrawal anchor",
  "stage3_price": null,
  "deal_value_krw_trn": 15.13,
  "deal_value_usd_bn": 10.27,
  "exchange_ratio_naver_financial_per_dunamu": 2.54,
  "upbit_market_share_pct": 70,
  "event_initial_mfe_pct": 7,
  "event_later_mae_pct": -4.2,
  "event_swing_pp": -11.2,
  "abnormal_withdrawal_krw_bn": 54,
  "loss_coverage": "Upbit_to_cover_using_own_assets",
  "closing_regulatory_approval_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium_trust_watch
rerating_result = fintech_crypto_MA_stage2_with_trust_gate
stage_failure_type = digital_asset_MA_not_green_until_trust_and_closing
```

---

## Case F — K Bank IPO `internet-bank IPO overhang`

```text
symbol = unlisted IPO candidate
case_type = event_premium + insufficient_evidence
archetype = INTERNET_BANK_IPO_OVERHANG
```

### stage date

```text
Stage 1:
2024-09-10
- Korea’s first internet-only bank seeks IPO
- digital banking / online lender valuation test
- prior IPO attempt scrapped in 2022

Stage 2:
2024-09-10
- planned IPO raise up to 984B won / $731.64M
- 82M shares offered
- price range 9,500~12,000 won
- valuation up to 5T won
- H1 2024 operating profit 86.7B won, more than triple YoY
- more than 10M customers as of early 2024
- listing planned for 2024-10-30

Stage 3:
없음
- IPO plan is not Green
- deposit quality, NIM, credit cost, customer acquisition cost, Upbit/deposit concentration, capital adequacy needed

Stage 4B:
IPO valuation approaches 5T won before listed track record
```

K Bank은 R6 internet-bank IPO overhang case다. 운영이익이 커지고 고객 수가 1000만 명을 넘은 것은 Stage 2지만, IPO value 5조 원은 credit quality와 funding mix를 확인해야 한다. 인터넷은행은 user growth보다 **예대마진, credit cost, 예금 concentration, capital ratio**가 먼저다. ([Reuters][6])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters K Bank IPO anchor",
  "stage3_price": null,
  "ipo_raise_max_krw_bn": 984,
  "ipo_raise_max_usd_mn": 731.64,
  "shares_offered_mn": 82,
  "new_shares_mn": 41,
  "existing_shares_mn": 41,
  "price_range_krw": "9500-12000",
  "max_valuation_krw_trn": 5,
  "ipo_raise_to_max_valuation_pct": 19.68,
  "h1_2024_operating_profit_krw_bn": 86.7,
  "h1_op_growth": "more_than_triple_yoy",
  "customer_count_mn": 10,
  "listing_target": "2024-10-30",
  "credit_cost_nim_deposit_concentration_confirmed": false,
  "mfe_mae": "N/A_unlisted"
}
```

### alignment

```text
score_price_alignment = event_premium_insufficient_evidence
rerating_result = internet_bank_IPO_stage2
stage_failure_type = IPO_valuation_not_bank_quality_green
```

---

## Case G — Stablecoin basket `overheat / FX gate`

```text
symbols = Kakao Pay / LG CNS / Aton / ME2ON
case_type = overheat + 4C-watch
archetype = STABLECOIN_POLICY_OVERHEAT_FX_GATE
```

### stage date

```text
Stage 1:
2025-06
- Lee Jae-myung administration pledges won-backed stablecoin reform
- digital currency pilot / BOK project names rerate
- retail margin loans expand

Stage 4B:
2025-06
- Kakao Pay more than doubled
- LG CNS +70%
- Aton +80%
- ME2ON 3x
- margin loans reach 20.5T won / $15B

Stage 4C-watch:
2025-06~2025-12
- proposed issuer equity threshold as low as 500M won
- BOK concerned about non-bank stablecoin impact on monetary policy and capital flows
- won weakness / retail overseas investment FX-hedging risk reviewed by watchdog
- no issuer license / reserve income / fee revenue confirmed

Stage 3:
없음
```

Stablecoin basket은 R6의 가장 확실한 `price_moved_without_evidence`다. Kakao Pay, LG CNS, Aton, ME2ON은 stablecoin 기대만으로 70%~3배 움직였지만, 실제 issuer license·reserve income·fee revenue는 확인되지 않았다. 게다가 BOK와 금융감독당국은 capital flow와 FX-hedging risk를 계속 문제로 본다. ([Financial Times][7])

### 실제 가격경로 검증

```json
{
  "price_data_source": "FT stablecoin return anchor + Reuters FSS FX-risk anchor",
  "stage3_price": null,
  "kakao_pay_mfe_pct": 100,
  "lg_cns_mfe_pct": 70,
  "aton_mfe_pct": 80,
  "me2on_mfe_pct": 200,
  "margin_loans_krw_trn": 20.5,
  "proposed_minimum_issuer_equity_krw_mn": 500,
  "won_weakness_quarter_pct": 4,
  "issuer_license_confirmed": false,
  "reserve_income_confirmed": false,
  "fee_revenue_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = price_moved_without_evidence
rerating_result = stablecoin_policy_overheat_FX_gate
stage_failure_type = 4B_before_regulated_revenue
```

---

## Case H — Bithumb operational error `crypto exchange hard reference`

```text
direct_company = Bithumb, unlisted / exchange reference
case_type = hard_4C_reference
archetype = CRYPTO_EXCHANGE_OPERATIONAL_HARD_REFERENCE
```

### stage date

```text
Stage 1:
2026-02-06
- Bithumb promotion reward error
- internal-control failure in crypto exchange operation

Stage 4C-reference:
2026-02-07
- Bithumb accidentally distributes more than $44B worth of bitcoins
- at least 2,000 BTC received by affected users
- 695 affected customers
- withdrawals/trading restricted within 35 minutes
- 99.7% of 620,000 BTC recovered
- bitcoin price briefly -17% to 81.1M won on Bithumb
- regulator says virtual-asset vulnerabilities exposed and may inspect exchanges

Stage 3:
N/A
```

Bithumb case는 R6 digital finance hard reference다. 외부 해킹은 아니었다고 했지만, exchange internal control failure만으로도 거래소 가격과 규제신뢰가 흔들렸다. 특히 Bithumb 내 bitcoin 가격이 17% 급락했고, 금융당국은 internal control과 asset operations inspection 가능성을 언급했다. 이건 상장사가 아니더라도 Upbit/Dunamu/Naver/Hana 같은 digital-asset exposure를 평가할 때 반드시 hard gate로 둬야 한다. ([Reuters][8])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters Bithumb operational error anchor",
  "stage3_price": null,
  "erroneous_bitcoin_distribution_usd_bn": 44,
  "erroneous_btc_total": 620000,
  "affected_customers": 695,
  "btc_received_per_affected_user_min": 2000,
  "recovered_share_pct": 99.7,
  "trading_withdrawal_restriction_minutes": 35,
  "bithumb_btc_event_mae_pct": -17,
  "bithumb_btc_event_low_krw_mn": 81.1,
  "bithumb_btc_recovered_price_krw_mn": 104.5,
  "external_hack": false,
  "regulator_inspection_risk": true,
  "mfe_mae": "N/A_unlisted_exchange_reference"
}
```

### alignment

```text
score_price_alignment = thesis_break_reference
rerating_result = crypto_exchange_operational_hard_reference
stage_failure_type = exchange_internal_control_hard_gate
```

---

# 5. 이번 R6 case별 stage date 요약

| case              | Stage 1    | Stage 2           | Stage 3 | Stage 4B                      | Stage 4C                           |
| ----------------- | ---------- | ----------------- | ------- | ----------------------------- | ---------------------------------- |
| 금융지주 value-up     | 2024-02~05 | 2024-05 / 2026-02 | N/A     | 2026-05-06                    | credit/NIM watch                   |
| SK Square         | 2024       | 2024-11-21        | N/A     | SK Hynix-led watch            | N/A                                |
| Samsung Life      | 2026-03    | 2026-03 / 2026-05 | N/A     | Samsung Electronics-led watch | regulatory stake-sale watch        |
| Hana/Dunamu       | 2026-05-14 | 2026-05-14/15     | N/A     | crypto optionality watch      | exchange trust watch               |
| Naver/Dunamu      | 2025-11-27 | 2025-11-27        | N/A     | +7%                           | 54B won abnormal withdrawal        |
| K Bank IPO        | 2024-09-10 | 2024-09-10        | N/A     | IPO valuation watch           | credit/deposit concentration watch |
| Stablecoin basket | 2025-06    | N/A               | N/A     | 2025-06                       | FX / regulatory watch              |
| Bithumb           | 2026-02-06 | N/A               | N/A     | N/A                           | 2026-02-07 hard reference          |

---

# 6. 실제 가격경로 검증 총괄

| case              |                                          anchor | MFE / MAE 해석                                  | 판정                      |
| ----------------- | ----------------------------------------------: | --------------------------------------------- | ----------------------- |
| 금융지주 value-up     |       financial groups +4.2%, securities +13.5% | market-confidence event premium               | 4B-watch                |
| SK Square         |              200B won buyback/cancellation plan | capital-return Stage 2                        | success_candidate       |
| Samsung Life      |         1.3T won Samsung Electronics stake sale | regulatory capital event, not insurance Green | success_candidate/watch |
| Hana/Dunamu       | 1.003T won for 6.55%, implied Dunamu 15.31T won | bank digital-asset Stage 2                    | success_candidate       |
| Naver/Dunamu      |        +7% → -4.2%, 54B won abnormal withdrawal | trust gate reversed event premium             | 4C-watch                |
| K Bank IPO        |          up to 984B won raise, 5T won valuation | IPO valuation not bank-quality proof          | insufficient            |
| Stablecoin basket |                         Kakao Pay >2x, ME2ON 3x | price moved without regulated revenue         | overheat                |
| Bithumb           |                BTC -17% on exchange, $44B error | operational hard reference                    | thesis_break_reference  |

---

# 7. score-price alignment 판정

```text
success_candidate:
- SK Square
- 금융지주 value-up basket
- Samsung Life
- Hana/Dunamu
- K Bank, only as IPO candidate

event_premium:
- financial groups / securities rally on KOSPI 7,000
- Naver/Dunamu initial +7%
- K Bank IPO valuation
- Hana/Dunamu crypto optionality

overheat:
- stablecoin basket
- securities +13.5% on trading-volume expectation

price_moved_without_evidence:
- stablecoin basket before issuer license / reserve income
- K Bank IPO before listed credit-cost proof
- Hana/Dunamu if treated as bank earnings Green before regulatory bridge
- financial groups if sector rally used as Stage 3 without CET1/NIM/credit-cost evidence

thesis_break_watch:
- Naver/Dunamu abnormal withdrawal
- Bithumb operational error reference
- stablecoin FX gate
- Samsung Life regulatory stake-sale gate

hard_4C_confirmed:
- direct listed hard 4C: false
- sector hard reference: Bithumb operational error
```

---

# 8. 점수비중 교정

## 올릴 축

```text
actual_buyback_cancellation +5
sustainable_dividend_payout +5
CET1_buffer +5
credit_cost_control +5
NIM_stability +4
ROE_improvement +5
regulatory_approval_clearance +5
digital_asset_trust +5
exchange_internal_control +5
fee_revenue_bridge +5
```

### 왜 올리나

SK Square는 실제 buyback/cancellation 계획이 있으므로 “말뿐인 value-up”보다 점수를 올릴 수 있다. 그러나 금융지주 basket은 정책·거래대금만으로는 Green이 아니다. Hana/Dunamu, Naver/Dunamu, stablecoin basket은 digital finance의 핵심이 **규제 승인과 trust**임을 보여준다. Bithumb은 internal-control failure 하나로 거래소 가격과 규제 리스크가 동시에 터질 수 있음을 보여준다.

## 내릴 축

```text
policy_valueup_headline_only -5
sector_rally_without_bank_metrics -5
IPO_valuation_without_credit_quality -5
digital_asset_equity_stake_only -5
stablecoin_theme_only -5
exchange_trust_incident -5
regulatory_capital_uncertainty -4
data_or_internal_control_failure -5
trading_volume_event_only -4
```

### 왜 내리나

KOSPI rally 때 증권주 +13.5%는 거래대금 event premium이지 지속 가능한 ROE 개선 증거가 아니다. K Bank IPO는 고객 수와 OP가 좋아도 신용비용과 예금구조가 확인되어야 한다. Hana/Dunamu 지분투자는 digital-asset optionality지만 은행 이익으로 바로 닫히지 않는다. Stablecoin basket은 issuer license 없는 price-only case다.

## Green gate 강화 조건

```text
R6 Stage 3-Green 필수:
1. buyback cancellation / dividend payout 실제 집행
2. CET1 / RBC / capital buffer 안정
3. NIM / fee income / credit cost 확인
4. ROE 개선이 일회성이 아님
5. M&A / stake deal은 regulatory approval과 capital charge 확인
6. digital finance는 trust / custody / internal control 통과
7. stablecoin은 issuer license / reserve income / fee revenue 확인
8. IPO는 상장 후 credit quality와 funding mix 확인
9. price path가 evidence 이후 따라옴

금지:
value-up headline only
sector rally only
digital-asset stake only
stablecoin theme only
IPO valuation only
exchange abnormal withdrawal / operational error unresolved
```

## 4B 조기감지 조건

```text
4B-watch:
securities / financials가 거래대금 기대만으로 +10% 이상 급등
stablecoin basket 2~3배 상승
Dunamu / Upbit 지분투자만으로 은행주 rerating
IPO valuation 5T won 이상이 credit data 없이 가격화
holding-company discount 축소가 buyback 반복성보다 먼저 가격화
Samsung Electronics stake-value로 보험주가 insurance earnings보다 먼저 상승

4B-elevated:
CET1 buffer 낮음
credit cost 상승
regulatory approval 미확정
exchange trust incident 발생
stablecoin FX gate 미해소
IPO funding mix / deposit concentration 미확인
```

## 4C hard gate 조건

```text
bank credit-cost spike
CET1 / RBC deterioration
regulatory rejection of M&A / stake investment
crypto exchange abnormal withdrawal / hack / operational error
stablecoin-driven FX outflow
data breach / internal-control failure
IPO cancellation due valuation or concentration risk
dividend / buyback cancellation reversal
```

이번 R6 Loop 13에서는 direct listed hard 4C를 확정하지 않는다. 대신 **Bithumb operational error**를 digital-asset hard reference로 두고, **Naver/Dunamu abnormal withdrawal**, **stablecoin FX gate**, **Samsung Life regulatory stake-sale**, **K Bank IPO valuation**을 strong watch로 둔다.

---

# 9. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 10. 레포 반영용 patch-ready 출력

## docs/round/round_203.md 요약

```md
# R6 Loop 13. Financials / Capital Allocation / Digital Finance Price Validation

이번 라운드는 R6 Loop 13 price-validation 라운드다.

핵심 결론:
- Financial holding value-up basket is Stage 2 plus 4B-watch. Value-up guidelines in 2024 were voluntary and KOSPI reaction was muted, but the 2026 Commercial Act treasury-cancellation rule strengthened the structure. On the KOSPI 7,000 event, securities firms +13.5% and financial groups +4.2%, which is event premium until CET1, NIM, credit cost, ROE and payout execution confirm.
- SK Square is holding-discount capital allocation Stage 2. It planned to cancel 100B won of prior buybacks and repurchase/cancel another 100B won. It holds 20% of SK Hynix, and its market value was less than half of the $18B stake value.
- Samsung Life is insurance holding-stake Stage 2 with regulatory gate. It plans to divest 1.3T won / $867.07M of Samsung Electronics shares to address financial-company governance regulation risk. Samsung Life also offers indirect Samsung Electronics exposure but insurance Green needs capital-return and earnings bridge.
- Hana Bank / Dunamu is digital-asset bank stake Stage 2. Hana buys 6.55% of Dunamu for 1.003T won / about $672.5M, implying about 15.31T won Dunamu equity value. Upbit has more than 80% Korean virtual-asset trading share in Reuters context.
- Naver Financial / Dunamu is fintech M&A Stage 2 plus trust 4C-watch. Deal value 15.13T won, exchange ratio 2.54. Naver initially +7% but later -4.2% after 54B won abnormal withdrawal from Upbit.
- K Bank IPO is internet-bank event premium / insufficient evidence. Planned raise up to 984B won, valuation up to 5T won, H1 2024 OP 86.7B won, 10M+ customers. Credit quality, NIM, funding mix and deposit concentration required.
- Stablecoin basket is overheat. Kakao Pay >2x, LG CNS +70%, Aton +80%, ME2ON 3x before issuer license, reserve income or fee revenue. FX and capital-flow gate remains.
- Bithumb operational error is crypto-exchange hard reference. $44B worth of bitcoins mistakenly distributed, 99.7% recovered, 695 affected customers, trading/withdrawals restricted within 35 minutes, BTC briefly -17% on Bithumb.
```

## docs/checkpoints/checkpoint_28a_round203_r6_loop13.md 요약

```md
# Checkpoint 28A Round 203 R6 Loop 13 Financials Capital Allocation Digital Finance Price Validation

## 반영 내용
- R6 Loop 13 price-validation 라운드를 추가했다.
- Financial holding value-up, SK Square holdco buyback, Samsung Life stake regulation, Hana/Dunamu stake, Naver/Dunamu M&A trust gate, K Bank IPO, stablecoin overheat, Bithumb operational error를 비교했다.
- Reuters / FT / WSJ / Barron's anchors로 가능한 event MFE/MAE, deal value, implied valuation, policy metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- actual buyback cancellation, sustainable dividend payout, CET1 buffer, credit cost control, NIM stability, ROE improvement, regulatory approval, digital-asset trust, exchange internal control, fee-revenue bridge 가중치 강화
- policy value-up headline-only, sector rally without bank metrics, IPO valuation without credit quality, digital-asset equity stake-only, stablecoin theme-only, exchange trust incident 감점 강화
```

## data/e2r_case_library/cases_r6_loop13_round203.jsonl 초안

```jsonl
{"case_id":"r6_loop13_financial_holdings_valueup_sector_4b","symbol":"105560/055550/086790/316140","company_name":"KB / Shinhan / Hana / Woori financial holding basket","case_type":"success_candidate_4b_watch","primary_archetype":"BANK_VALUE_UP_RERATING_STAGE2","stage1_date":"2024-02_to_2024-05","stage2_date":"2024-05-02/2026-02-25","stage4b_date":"2026-05-06","price_validation":{"price_data_source":"Reuters / FT policy and sector-return anchors","stage3_price":null,"value_up_guideline_event_kospi_pct":-0.2,"commercial_act_treasury_cancellation_rule":"newly_acquired_treasury_shares_cancel_within_one_year","kospi_event_mfe_pct":6.45,"securities_firms_event_mfe_pct":13.5,"financial_groups_event_mfe_pct":4.2,"foreign_net_purchase_krw_trn":3.1,"actual_bank_cet1_credit_cost_nim_verified":false,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_4B_watch","rerating_result":"bank_value_up_stage2","notes":"Value-up and financial-sector rally are Stage 2; CET1, NIM, credit cost, ROE and payout execution required before Green."}
{"case_id":"r6_loop13_sk_square_holdco_discount_buyback","symbol":"402340","company_name":"SK Square","case_type":"success_candidate","primary_archetype":"HOLDCO_DISCOUNT_BUYBACK_CANCELLATION","stage2_date":"2024-11-21","price_validation":{"price_data_source":"Reuters SK Square buyback / discount anchor","stage3_price":null,"cancel_existing_buyback_krw_bn":100,"new_buyback_krw_bn":100,"total_announced_cancel_buyback_krw_bn":200,"sk_hynix_stake_pct":20,"sk_hynix_stake_value_usd_bn":18,"market_value_status":"less_than_half_of_stake_value","implied_market_cap_upper_bound_usd_bn":9,"discount_to_stake_value_min_pct":50,"palliser_stake_pct":1,"independent_director_nomination":true,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"holdco_discount_buyback_cancellation_stage2","notes":"Buyback/cancellation is strong Stage 2; NAV discount narrowing and repeated capital-return discipline required."}
{"case_id":"r6_loop13_samsung_life_samsung_electronics_stake_regulatory_gate","symbol":"032830","company_name":"Samsung Life Insurance","case_type":"success_candidate_4c_watch","primary_archetype":"INSURANCE_HOLDING_STAKE_REGULATORY_GATE","stage2_date":"2026-03-19/2026-05_context","price_validation":{"price_data_source":"Reuters Samsung Life divestiture + Barron's valuation context","stage3_price":null,"samsung_electronics_stake_sale_krw_trn":1.3,"samsung_electronics_stake_sale_usd_mn":867.07,"samsung_life_samsung_electronics_stake_context_pct":10,"book_value_multiple_context":"about_0.5x_book_value","regulatory_driver":"financial-company governance regulation risk","use_of_proceeds_confirmed_for_shareholder_return":false,"insurance_capital_return_bridge_confirmed":false,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_4C_watch","rerating_result":"insurance_holdco_value_stage2","notes":"Samsung Electronics stake value is optionality; regulatory sale and insurance capital-return bridge must clear."}
{"case_id":"r6_loop13_hana_bank_dunamu_digital_asset_stake","symbol":"086790","company_name":"Hana Financial Group / Hana Bank / Dunamu","case_type":"success_candidate_4b_watch","primary_archetype":"DIGITAL_ASSET_BANK_STAKE_STAGE2","stage2_date":"2026-05-14/2026-05-15","price_validation":{"price_data_source":"Reuters / WSJ Hana-Dunamu stake anchors","stage3_price":null,"dunamu_stake_pct":6.55,"purchase_price_krw_trn":1.003,"purchase_price_usd_mn":672.5,"implied_dunamu_equity_value_krw_trn":15.31,"seller":"Kakao affiliate","hana_resulting_rank":"fourth_largest_shareholder","upbit_virtual_asset_trading_share_pct":80,"remittance_technical_verification_completed":true,"regulatory_capital_earnings_bridge_confirmed":false,"price_validation_status":"reported_deal_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_4B_watch","rerating_result":"bank_digital_asset_stake_stage2","notes":"Equity stake is Stage 2; bank Green requires regulatory capital, earnings pickup, trust and stablecoin framework."}
{"case_id":"r6_loop13_naver_dunamu_fintech_ma_trust_gate","symbol":"035420","company_name":"Naver Financial / Dunamu / Upbit","case_type":"success_candidate_4c_watch","primary_archetype":"FINTECH_CRYPTO_M_AND_A_TRUST_GATE","stage2_date":"2025-11-27","stage4b_date":"2025-11-27","stage4c_date":"2025-11-27_watch","price_validation":{"price_data_source":"Reuters Naver-Dunamu deal and abnormal-withdrawal anchor","stage3_price":null,"deal_value_krw_trn":15.13,"deal_value_usd_bn":10.27,"exchange_ratio_naver_financial_per_dunamu":2.54,"upbit_market_share_pct":70,"event_initial_mfe_pct":7,"event_later_mae_pct":-4.2,"event_swing_pp":-11.2,"abnormal_withdrawal_krw_bn":54,"loss_coverage":"Upbit_to_cover_using_own_assets","closing_regulatory_approval_confirmed":false,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_trust_watch","rerating_result":"fintech_crypto_MA_stage2_with_trust_gate","notes":"M&A synergy is Stage 2; abnormal withdrawal shows exchange trust gate comes first."}
{"case_id":"r6_loop13_kbank_internet_bank_ipo_overhang","symbol":"unlisted_KBank_IPO_candidate","company_name":"K Bank","case_type":"event_premium_insufficient_evidence","primary_archetype":"INTERNET_BANK_IPO_OVERHANG","stage2_date":"2024-09-10","price_validation":{"price_data_source":"Reuters K Bank IPO anchor","stage3_price":null,"ipo_raise_max_krw_bn":984,"ipo_raise_max_usd_mn":731.64,"shares_offered_mn":82,"new_shares_mn":41,"existing_shares_mn":41,"price_range_krw":"9500-12000","max_valuation_krw_trn":5,"ipo_raise_to_max_valuation_pct":19.68,"h1_2024_operating_profit_krw_bn":86.7,"h1_op_growth":"more_than_triple_yoy","customer_count_mn":10,"listing_target":"2024-10-30","credit_cost_nim_deposit_concentration_confirmed":false,"price_validation_status":"unlisted_ipo_candidate"},"score_price_alignment":"event_premium_insufficient_evidence","rerating_result":"internet_bank_IPO_stage2","notes":"Internet-bank IPO is not Green until credit quality, NIM, funding mix, deposit concentration and capital adequacy confirm."}
{"case_id":"r6_loop13_stablecoin_policy_overheat_fx_gate","symbol":"KakaoPay/LG_CNS/Aton/ME2ON","company_name":"Stablecoin policy basket","case_type":"overheat_4c_watch","primary_archetype":"STABLECOIN_POLICY_OVERHEAT_FX_GATE","stage4b_date":"2025-06","stage4c_date":"2025-06_to_2025-12_watch","price_validation":{"price_data_source":"FT stablecoin return anchor + Reuters FSS FX-risk anchor","stage3_price":null,"kakao_pay_mfe_pct":100,"lg_cns_mfe_pct":70,"aton_mfe_pct":80,"me2on_mfe_pct":200,"margin_loans_krw_trn":20.5,"proposed_minimum_issuer_equity_krw_mn":500,"won_weakness_quarter_pct":4,"issuer_license_confirmed":false,"reserve_income_confirmed":false,"fee_revenue_confirmed":false,"price_validation_status":"reported_return_anchor_not_full_ohlc"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"stablecoin_policy_overheat_FX_gate","notes":"Stablecoin basket moved before regulated revenue; FX and capital-flow gate remains."}
{"case_id":"r6_loop13_bithumb_operational_error_hard_reference","symbol":"unlisted_Bithumb/crypto_exchange_reference","company_name":"Bithumb","case_type":"hard_4c_reference","primary_archetype":"CRYPTO_EXCHANGE_OPERATIONAL_HARD_REFERENCE","stage4c_date":"2026-02-07","price_validation":{"price_data_source":"Reuters Bithumb operational error anchor","stage3_price":null,"erroneous_bitcoin_distribution_usd_bn":44,"erroneous_btc_total":620000,"affected_customers":695,"btc_received_per_affected_user_min":2000,"recovered_share_pct":99.7,"trading_withdrawal_restriction_minutes":35,"bithumb_btc_event_mae_pct":-17,"bithumb_btc_event_low_krw_mn":81.1,"bithumb_btc_recovered_price_krw_mn":104.5,"external_hack":false,"regulator_inspection_risk":true,"price_validation_status":"unlisted_exchange_hard_reference"},"score_price_alignment":"thesis_break_reference","rerating_result":"crypto_exchange_operational_hard_reference","notes":"Crypto exchange internal-control failure is a hard reference for digital-asset financial exposures."}
```

## data/sector_taxonomy/score_weight_profiles_round203_r6_loop13_v1.csv 초안

```csv
archetype,actual_buyback_cancellation,sustainable_dividend_payout,cet1_buffer,credit_cost_control,nim_stability,roe_improvement,regulatory_approval_clearance,digital_asset_trust,exchange_internal_control,fee_revenue_bridge,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
BANK_VALUE_UP_RERATING_STAGE2,+5,+5,+5,+5,+4,+5,+3,+0,+0,+3,-5,+5,+4,Financial value-up requires executed payout plus CET1/NIM/credit-cost proof.
HOLDCO_DISCOUNT_BUYBACK_CANCELLATION,+5,+4,+2,+1,+0,+4,+2,+0,+0,+2,-3,+4,+3,SK Square buyback/cancellation is Stage 2; repeated capital-return and NAV discount narrowing required.
INSURANCE_HOLDING_STAKE_REGULATORY_GATE,+3,+5,+5,+3,+1,+5,+5,+0,+0,+3,-4,+4,+4,Samsung Life stake value needs regulatory clarity, capital adequacy and shareholder-return bridge.
DIGITAL_ASSET_BANK_STAKE_STAGE2,+2,+3,+5,+4,+3,+4,+5,+5,+5,+5,-5,+5,+5,Hana/Dunamu equity stake needs regulatory capital, earnings pickup and exchange trust.
FINTECH_CRYPTO_M_AND_A_TRUST_GATE,+2,+3,+4,+3,+2,+4,+5,+5,+5,+5,-5,+5,+5,Naver/Dunamu shows trust incident can reverse M&A premium immediately.
INTERNET_BANK_IPO_OVERHANG,+0,+1,+5,+5,+5,+5,+4,+2,+3,+4,-5,+5,+4,K Bank IPO needs NIM, credit cost, funding mix, capital adequacy and concentration proof.
STABLECOIN_POLICY_OVERHEAT_FX_GATE,+0,+0,+2,+1,+1,+2,+5,+5,+5,+5,-5,+5,+5,Stablecoin basket is 4B without issuer license/reserve income/fee revenue.
CRYPTO_EXCHANGE_OPERATIONAL_HARD_REFERENCE,+0,+0,+0,+0,+0,+0,+5,+5,+5,+4,0,+4,+5,Bithumb operational error is digital-asset hard reference.
SECURITIES_TRADING_VOLUME_EVENT_PREMIUM,+2,+3,+3,+3,+2,+4,+2,+0,+0,+5,-4,+5,+3,Securities rally on KOSPI volume is event premium until recurring fee revenue proves out.
```

---

# 이번 R6 Loop 13 결론

```text
1. 금융지주 value-up basket은 Stage 2다.
   하지만 금융그룹 +4.2%, 증권주 +13.5%는 trading-volume event premium도 같이 붙는다.

2. SK Square는 holding discount buyback/cancellation Stage 2다.
   실제 소각이 있고 NAV discount가 줄어야 Stage 3다.

3. Samsung Life는 insurance holding-stake optionality다.
   Samsung Electronics 지분가치보다 regulatory sale과 capital-return bridge가 핵심이다.

4. Hana Bank / Dunamu는 bank digital-asset Stage 2다.
   1.003T won 지분투자는 크지만, regulated revenue와 exchange trust 전에는 Green이 아니다.

5. Naver/Dunamu는 M&A trust gate의 교과서다.
   +7%에서 -4.2%로 뒤집힌 가격경로가 Upbit abnormal withdrawal risk를 보여준다.

6. K Bank IPO는 internet-bank event premium이다.
   고객 수와 OP보다 credit cost, NIM, funding mix, deposit concentration이 먼저다.

7. Stablecoin basket은 price_moved_without_evidence다.
   issuer license, reserve income, fee revenue 전 2~3배 움직였다.

8. Bithumb operational error는 crypto exchange hard reference다.
   해킹이 아니어도 internal-control failure만으로 digital finance thesis가 끊긴다.
```

한 문장으로 압축하면:

> **R6에서 진짜 Stage 3는 “value-up·자사주·Dunamu·stablecoin·인터넷은행 IPO가 좋다”가 아니라, 자본환원 실행·CET1·NIM·credit cost·regulatory approval·digital trust·수수료 수익이 실제 숫자로 닫히는 순간이다.**

* [Reuters](https://www.reuters.com/markets/asia/south-korea-unveils-guidelines-corporate-value-up-programme-2024-05-02/?utm_source=chatgpt.com)
* [Financial Times](https://www.ft.com/content/3c39cd79-bce6-467b-9671-f13de70d05fb?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/south-koreas-kospi-share-index-tops-7000-first-time-2026-05-06/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/technology/artificial-intelligence/south-koreas-ai-chip-investor-announces-plan-share-buybacks-2024-11-21/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/samsung-life-divest-13-trln-won-worth-samsung-electronics-shares-2026-03-19/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/hana-bank-acquire-stake-dunamu-700-mln-filing-says-2026-05-14/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/navers-payment-arm-acquire-south-korean-crypto-exchange-operator-10-bln-deal-2025-11-27/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/markets/asia/south-koreas-k-bank-announces-ipo-plan-worth-up-732-million-2024-09-10/?utm_source=chatgpt.com)
* [Financial Times](https://www.ft.com/content/4b19bf90-4202-4fe7-8caf-d7db6deeb768?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/crypto-firm-accidentally-sends-44-billion-bitcoins-users-2026-02-07/?utm_source=chatgpt.com)

[1]: https://www.reuters.com/markets/asia/south-korea-unveils-guidelines-corporate-value-up-programme-2024-05-02/?utm_source=chatgpt.com "South Korea unveils voluntary guidelines to unlock shareholder value"
[2]: https://www.reuters.com/technology/artificial-intelligence/south-koreas-ai-chip-investor-announces-plan-share-buybacks-2024-11-21/?utm_source=chatgpt.com "South Korea's AI chip investor announces plan for share buybacks"
[3]: https://www.reuters.com/world/asia-pacific/samsung-life-divest-13-trln-won-worth-samsung-electronics-shares-2026-03-19/?utm_source=chatgpt.com "Samsung Life to divest 1.3 trln won worth of Samsung Electronics' shares"
[4]: https://www.reuters.com/world/asia-pacific/hana-bank-acquire-stake-dunamu-700-mln-filing-says-2026-05-14/?utm_source=chatgpt.com "Hana Bank to acquire stake in Dunamu for $700 mln, filing says"
[5]: https://www.reuters.com/world/asia-pacific/navers-payment-arm-acquire-south-korean-crypto-exchange-operator-10-bln-deal-2025-11-27/?utm_source=chatgpt.com "Naver's payment arm to acquire South Korean crypto exchange operator in $10 bln deal"
[6]: https://www.reuters.com/markets/asia/south-koreas-k-bank-announces-ipo-plan-worth-up-732-million-2024-09-10/?utm_source=chatgpt.com "South Korea's K Bank announces IPO plan worth up to $732 million"
[7]: https://www.ft.com/content/4b19bf90-4202-4fe7-8caf-d7db6deeb768?utm_source=chatgpt.com "Crypto-crazy investors make South Korea the best-performing market in Asia"
[8]: https://www.reuters.com/world/asia-pacific/crypto-firm-accidentally-sends-44-billion-bitcoins-users-2026-02-07/?utm_source=chatgpt.com "South Korean crypto firm accidentally sends $44 billion in bitcoins to users"

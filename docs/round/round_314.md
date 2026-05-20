순서상 이번은 **R6 Loop 16 — 금융·자본배분·디지털금융 trigger-level price validation 라운드**다.

이번 R6는 은행·증권·보험만 보는 라운드가 아니라, **자본배분, 주주환원, 밸류업, 디지털자산, 스테이블코인, 금융소비자보호, 플랫폼 금융 보안**까지 같이 본다. 핵심은 “주주환원 발표했다 / 스테이블코인 테마다 / crypto 거래소 지분 샀다”가 아니라, **실제 소각·배당·ROE·자본비율·규제승인·수익화·고객신뢰·보안사고**가 닫혔는지다.

```text
round = R6 Loop 16
round_id = round_242
large_sector = FINANCIALS_CAPITAL_ALLOCATION_DIGITAL_FINANCE
method = trigger_level_backtest_v1_after_redteam
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R7 Loop 16
```

이번에도 KRX/Naver/Yahoo/Stooq 수정주가 일봉 OHLC 30D/90D/180D/1Y/2Y window는 안정적으로 직접 확보하지 못했다. 그래서 full MFE/MAE는 만들지 않고 `price_data_unavailable_after_deep_search`로 둔다. 대신 Reuters/FT/WSJ/MarketWatch/Barron’s가 보도한 **event return, event price, buyback size, sector move, deal value, regulatory fine, user/transaction data**를 trigger anchor로 사용한다.

---

# 1. 이번 라운드 대섹터

```text
R6 = 금융·자본배분·디지털금융
```

R6의 core gate는 아래다.

```text
주주환원 / 밸류업:
buyback announcement → actual repurchase → cancellation → dividend policy → CET1 / capital ratio → ROE → discount 축소

은행 / 금융지주:
NIM / credit cost → fee income → shareholder return → regulatory fines → capital buffer → non-bank expansion

증권:
거래대금 / KOSPI rally → brokerage commission → IB/deal flow → overseas-stock FX risk → margin loans → bubble risk

디지털금융 / 스테이블코인:
policy bill → issuer eligibility → bank vs non-bank regulation → license / reserve rule → actual issuance → transaction revenue

Crypto / exchange:
exchange stake / M&A → regulatory approval → cyber incident → trading volume share → custody / AML / reserve risk

플랫폼 금융 보안:
data breach / abnormal withdrawal → customer trust → compensation → regulatory penalty → business model damage

소비자보호:
ELS / derivatives mis-selling → compensation → fine → product ban / sales restriction → capital hit
```

---

# 2. 대상 canonical archetype

```text
BUYBACK_CANCELLATION_VALUEUP_STAGE2_ACTIONABLE
HOLDCO_DISCOUNT_BUYBACK_STAGE2
BROKERAGE_TRADING_VOLUME_STAGE2_BETA
BANK_DIGITAL_ASSET_STAKE_STAGE2_WITH_CAPITAL_GATE
FINTECH_CRYPTO_EXCHANGE_MA_STAGE2_WITH_SECURITY_4B
STABLECOIN_POLICY_EVENT_PREMIUM_4B
ELS_MISSELLING_CONSUMER_PROTECTION_4C
FX_OVERSEAS_STOCK_FLOW_4C_WATCH
PRIVATE_FINTECH_STABLECOIN_IPO_OPTIONALITY_STAGE2
```

---

# 3. deep sub-archetype

```text
Samsung Electronics buyback / capital allocation template:
- 10T won / $7.17B one-year buyback
- first buyback since 2017
- 3T won of shares repurchased in first three months and cancelled
- shares +7.2%, biggest daily jump since March 2020
- but business-plan/HBM competitiveness gate remains

SK Square:
- 100B won shares previously bought back to be cancelled
- additional 100B won repurchase and cancellation plan
- Palliser Capital activism
- SK Square market value less than half value of 20% SK Hynix stake
- Value-Up / holdco discount case

KOSPI brokerage / financial beta:
- KOSPI +6.45% to 7,384.56 on May 6, 2026
- securities firms sector +13.5%
- financial groups +4.2%
- foreign investors bought record 3.1T won Korean shares
- trading-volume and market-confidence Stage2, but bubble/turnover cyclicality 4B

Naver Financial / Dunamu:
- Naver Financial to acquire Dunamu in 15.13T won / $10.27B all-stock deal
- Naver +7% initially, then -4.2% after Upbit abnormal 54B won crypto withdrawal
- Upbit ~70% Korea crypto exchange share by some reports
- digital asset growth + security 4B

Hana Bank / Dunamu:
- Hana Bank to buy 6.55% Dunamu stake for 1T won / ~$700M
- Upbit handles more than 80% of Korea virtual asset trading volume according to Reuters
- Kakao Investment stake drops to 4.03%
- strategic bank digital-asset entry, but valuation/capital/regulation gate

Stablecoin mania:
- Kakao Pay more than doubled in a month
- LG CNS rose almost 70%
- Aton +80%
- ME2ON tripled
- proposed won stablecoin bill allows issuers with as little as 500M won equity
- BOK warns on non-bank issuance, FX/capital-flow risk

ELS mis-selling:
- FSS to impose around 1T won fines each on local banks over Hong Kong equity-linked derivatives
- earlier FT reported expected investor losses around 5.8T won
- compensation 20~60% of principal discussed
- consumer-protection hard 4C

FX / overseas stock flow:
- Korean retail held nearly $171B overseas stocks as of Jan 29, 2026
- January net U.S. stock purchases $5B vs December $1.9B
- won near 17-year lows
- FSS reviews FX-risk explanations for overseas investment
- securities firms benefit from overseas brokerage but FX/consumer-protection 4C watch

Toss:
- Toss has 30M+ users
- plans Australia launch, won stablecoin issuance when regulation allows
- preparing U.S. IPO in Q2 2026, valuation over $10B and possibly >$15B
- private fintech optionality; no KRX price
```

---

# 4. 선정 case 요약

| bucket                        | case                                  | 핵심 판정                                                                                            |
| ----------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Stage2-Actionable             | Samsung Electronics buyback           | 10T won buyback, first since 2017, +7.2%. 자본배분 trigger는 강하지만 사업개선 gate 필요                        |
| Stage2 / holdco discount      | SK Square buyback                     | 100B won cancellation + 100B won repurchase/cancel, Palliser activism, SK Hynix stake discount   |
| Stage2 beta / 4B              | Securities and financial groups rally | KOSPI +6.45%, securities +13.5%, financial groups +4.2%. 거래대금 beta지만 bubble risk                 |
| Stage2 + 4B/4C                | Naver Financial / Dunamu              | $10.27B all-stock deal, Naver +7% then -4.2% after Upbit 54B won abnormal withdrawal             |
| Stage2 bank digital-asset     | Hana Bank / Dunamu                    | 1T won / 6.55% stake, Upbit >80% volume. 전략적이지만 capital/regulatory gate                          |
| event premium / 4B            | Stablecoin policy mania               | Kakao Pay >2x, LG CNS +70%, Aton +80%, ME2ON 3x. 법안/규제 전 테마 과열                                   |
| hard 4C                       | Hong Kong ELS mis-selling             | banks face around 1T won fines each, estimated 5.8T won retail losses                            |
| 4C-watch / broker opportunity | Overseas-stock FX flow                | $171B overseas holdings, Jan U.S. net purchases $5B, won pressure and consumer-protection review |
| private Stage2                | Toss stablecoin/global IPO            | 30M+ users, Australia launch, won stablecoin, U.S. IPO plan. 비상장 reference                       |

---

# 5. Case별 trigger grid

## Case A — Samsung Electronics buyback as capital-allocation template

```text
symbol = 005930
case_type = Stage2-Actionable / capital allocation
archetype = BUYBACK_CANCELLATION_VALUEUP_STAGE2_ACTIONABLE
```

| trigger |              type | date       | 당시 공개 evidence                                                         | 가격 anchor    | outcome               |
| ------- | ----------------: | ---------- | ---------------------------------------------------------------------- | ------------ | --------------------- |
| T0      |     4B background | 2024-11    | shares down 32% YTD, HBM/Nvidia lag, weak chip profit                  | no entry     | background            |
| T1      | Stage2-Actionable | 2024-11-15 | 10T won / $7.17B one-year buyback, first buyback since 2017            | shares +7.2% | excellent event       |
| T2      |        validation | 2024-11-15 | 3T won of shares to be bought in first three months and cancelled      | same         | cancellation evidence |
| T3      |          4B-watch | 2024~2025  | buyback supports price but does not solve HBM/business competitiveness | same         | 4B                    |
| T4      |     Stage3-Yellow | N/A        | sustained ROE/EPS/business improvement not confirmed at trigger        | no Yellow    | 보류                    |

Samsung buyback은 R6에서 가장 좋은 capital-allocation trigger template다. Samsung Electronics는 10T won, 약 $7.17B 규모의 1년 buyback을 발표했고, 이는 2017년 이후 첫 buyback이었다. 그중 3T won 규모는 3개월 안에 repurchase 후 cancellation 예정이었고, 발표 당일 shares는 +7.2%로 2020년 3월 이후 최대 daily jump를 기록했다. 다만 Reuters도 “short-term support는 되지만 concrete business plans가 필요하다”고 전했기 때문에, 이건 Stage2-Actionable이지 Green은 아니다. ([Reuters][1])

```json
{
  "case_id": "r6_loop16_samsung_buyback_capital_allocation",
  "symbol": "005930",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable_capital_allocation",
  "trigger_date": "2024-11-15",
  "buyback_value_krw_trn": 10,
  "buyback_value_usd_bn": 7.17,
  "first_buyback_since": 2017,
  "initial_cancelled_repurchase_krw_trn": 3,
  "event_return_pct": 7.2,
  "ytd_decline_before_buyback_pct": -32,
  "stage3_gate_missing": [
    "business_plan",
    "HBM_competitiveness",
    "sustained_EPS_recovery",
    "ROE_improvement",
    "full_OHLC_MFE_MAE"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_stage2_actionable_buyback"
}
```

---

## Case B — SK Square buyback / holdco discount

```text
symbol = 402340
case_type = Stage2 / holdco discount capital allocation
archetype = HOLDCO_DISCOUNT_BUYBACK_STAGE2
```

| trigger |            type | date       | 당시 공개 evidence                                                                               | 가격 anchor      | outcome               |
| ------- | --------------: | ---------- | -------------------------------------------------------------------------------------------- | -------------- | --------------------- |
| T0      |       awareness | 2024       | SK Square trades at large discount to SK Hynix stake                                         | no price       | Stage1                |
| T1      | Stage2 evidence | 2024-11-21 | SK Square to cancel 100B won previously bought shares and repurchase/cancel another 100B won | no event price | Stage2                |
| T2      |      validation | 2024-11-21 | Palliser Capital activism, independent director, Korea Value-Up program                      | no price       | governance validation |
| T3      |        4B-watch | 2024~      | holdco discount may persist if governance/capital allocation not repeated                    | no OHLC        | 4B                    |
| T4      |   Stage3-Yellow | N/A        | discount narrowing, repeated buyback, dividend/ROE not confirmed                             | no Yellow      | 보류                    |

SK Square는 R6 “holding company discount + buyback + activism” template다. Reuters는 SK Square가 4월 매입한 100B won 자사주를 소각하고, 추가 100B won 자사주를 3개월 내 매입해 소각하겠다고 보도했다. Palliser Capital activism, independent director nomination, Korea Value-Up program이 함께 작동했고, SK Square의 market value는 보유 중인 SK Hynix 20% stake value보다 절반에도 못 미친다고 전해졌다. 다만 event price anchor가 없으므로 Actionable 확정은 보류하고 Stage2 capital-allocation row로 둔다. ([Reuters][2])

```json
{
  "case_id": "r6_loop16_sk_square_buyback_holdco_discount",
  "symbol": "402340",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2_holdco_discount_buyback",
  "trigger_date": "2024-11-21",
  "cancel_previous_buyback_krw_bn": 100,
  "new_repurchase_cancel_plan_krw_bn": 100,
  "sk_hynix_stake_pct": 20,
  "market_value_vs_stake_value": "<50%",
  "activist": "Palliser_Capital",
  "palliser_stake_pct_context": 1,
  "direct_event_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "discount_narrowing",
    "repeat_buyback",
    "capital_allocation_policy",
    "dividend_policy",
    "governance_follow_through"
  ],
  "trigger_outcome_label": "Stage2_holdco_valueup_not_Green"
}
```

---

## Case C — Securities firms / financial groups rally on KOSPI boom

```text
symbols = securities_sector / financial_groups_sector / 039490 / 005940 / 071050 / 105560
case_type = Stage2 market beta with 4B bubble risk
archetype = BROKERAGE_TRADING_VOLUME_STAGE2_BETA
```

| trigger |          type | date       | 당시 공개 evidence                                                                         | 가격 anchor                                 | outcome     |
| ------- | ------------: | ---------- | -------------------------------------------------------------------------------------- | ----------------------------------------- | ----------- |
| T0      |     awareness | 2025~2026  | Korea market reforms, AI rally, foreign inflows                                        | no price                                  | Stage1      |
| T1      |   Stage2 beta | 2026-05-06 | KOSPI closes +6.45% at 7,384.56; foreign investors buy 3.1T won, record daily purchase | securities +13.5%, financial groups +4.2% | Stage2 beta |
| T2      |      4B-watch | 2026-05    | market concentration, AI chip dependency, options/speculation, bubble-risk commentary  | no full OHLC                              | 4B          |
| T3      | Stage3-Yellow | N/A        | brokerage commission/IB earnings and credit-loss data not confirmed                    | no Yellow                                 | 보류          |

R6에서 증권주는 “주식시장 거래대금 beta”다. 2026년 5월 6일 KOSPI가 +6.45%로 7,384.56에 마감했고, 외국인은 3.1T won, 약 $2.13B를 순매수했다. 같은 날 securities firms sector는 +13.5%, financial groups sector는 +4.2% 올랐다. 이건 brokerage commission, margin loan, wealth-management flow에 대한 Stage2 beta다. 그러나 Reuters는 동시에 AI chip dependence와 급격한 rally 구조를 설명했고, 다른 보도에서는 BofA가 Korea market action을 “textbook bubble”로 봤다고 전해져 4B overheat가 필요하다. ([Reuters][3])

```json
{
  "case_id": "r6_loop16_kospi_brokerage_financial_beta",
  "symbols": "securities_sector/financial_groups_sector",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2_market_beta_with_4B_overheat",
  "trigger_date": "2026-05-06",
  "kospi_event_return_pct": 6.45,
  "kospi_close": 7384.56,
  "foreign_net_buy_krw_trn": 3.1,
  "foreign_net_buy_usd_bn": 2.13,
  "securities_sector_event_return_pct": 13.5,
  "financial_groups_event_return_pct": 4.2,
  "stage3_gate_missing": [
    "brokerage_commission_growth",
    "margin_loan_quality",
    "IB_pipeline",
    "wealth_management_fee",
    "credit_cost",
    "turnover_durability"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_brokerage_beta_with_4B_bubble_watch"
}
```

---

## Case D — Naver Financial / Dunamu acquisition

```text
symbols = 035420 / Dunamu_private
case_type = Stage2 digital-asset M&A with security 4B
archetype = FINTECH_CRYPTO_EXCHANGE_MA_STAGE2_WITH_SECURITY_4B
```

| trigger |            type | date       | 당시 공개 evidence                                                                                         | 가격 anchor           | outcome              |
| ------- | --------------: | ---------- | ------------------------------------------------------------------------------------------------------ | ------------------- | -------------------- |
| T0      | Stage2 evidence | 2025-11-27 | Naver Financial to acquire Dunamu in all-stock 15.13T won / $10.27B deal                               | Naver initially +7% | Stage2 M&A           |
| T1      |     4B/security | 2025-11-27 | Naver later -4.2% after Upbit abnormal 54B won crypto withdrawal                                       | -4.2%               | security 4B          |
| T2      |      validation | 2025-11-27 | Naver Financial issues 2.54 shares for each Dunamu share; Upbit about 70% market share by some reports | same                | strategic validation |
| T3      |   Stage3-Yellow | N/A        | regulator/shareholder approval, custody, AML, stablecoin monetization not confirmed                    | no Yellow           | 보류                   |

Naver Financial-Dunamu는 R6 digital finance에서 가장 중요한 M&A trigger다. Reuters는 Naver Financial이 Dunamu를 15.13T won, 약 $10.27B all-stock deal로 인수한다고 보도했다. Naver shares는 news 이후 7% 넘게 뛰었지만, Upbit의 54B won abnormal crypto withdrawal 소식이 나오자 같은 날 4.2% 하락세로 돌아섰다. 이건 `digital asset growth Stage2 + exchange security 4B`가 동시에 나온 case다. ([Reuters][4])

```json
{
  "case_id": "r6_loop16_naver_financial_dunamu_ma",
  "symbol": "035420/Dunamu_private",
  "best_trigger": "T0/T1",
  "best_trigger_type": "Stage2_MA_with_security_4B",
  "trigger_date": "2025-11-27",
  "deal_value_krw_trn": 15.13,
  "deal_value_usd_bn": 10.27,
  "stock_swap_ratio": "2.54_Naver_Financial_shares_per_Dunamu_share",
  "naver_initial_event_return_pct": 7,
  "naver_later_event_return_pct": -4.2,
  "abnormal_withdrawal_krw_bn": 54,
  "upbit_market_share_context_pct": 70,
  "stage3_gate_missing": [
    "regulatory_approval",
    "shareholder_approval",
    "AML_custody_controls",
    "stablecoin_revenue_model",
    "Upbit_security_resolution",
    "Naver_Financial_integration"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_digital_asset_MA_with_security_4B"
}
```

---

## Case E — Hana Bank / Dunamu stake acquisition

```text
symbols = 086790 / Dunamu_private / Kakao_readthrough
case_type = Stage2 bank digital-asset stake
archetype = BANK_DIGITAL_ASSET_STAKE_STAGE2_WITH_CAPITAL_GATE
```

| trigger |                  type | date          | 당시 공개 evidence                                                                        | 가격 anchor              | outcome                  |
| ------- | --------------------: | ------------- | ------------------------------------------------------------------------------------- | ---------------------- | ------------------------ |
| T0      |       Stage2 evidence | 2026-05-14/15 | Hana Bank to acquire 6.55% Dunamu stake for 1T won / ~$700M                           | Hana price unavailable | Stage2                   |
| T1      |            validation | 2026-05-15    | Upbit handles more than 80% of Korea virtual-asset trading volume, per Reuters        | no price               | digital asset validation |
| T2      | capital/regulatory 4B | 2026          | bank capital usage, valuation, crypto regulation, BOK stablecoin concerns             | no OHLC                | 4B                       |
| T3      |         Stage3-Yellow | N/A           | digital-asset revenue contribution, capital charge, regulatory approval not confirmed | no Yellow              | 보류                       |

Hana Bank의 Dunamu stake acquisition은 전통 은행이 digital asset로 들어가는 Stage2다. Reuters는 Hana Bank가 Dunamu 6.55% stake를 1T won, 약 $700M에 취득한다고 보도했고, Dunamu의 Upbit은 Korea virtual asset trading volume의 80% 이상을 처리한다고 전했다. WSJ도 이 거래가 Korean bank의 largest digital-asset investment라고 설명했다. 다만 bank capital usage, regulatory treatment, crypto-cycle risk가 남아 있어 Green이 아니다. ([Reuters][5])

```json
{
  "case_id": "r6_loop16_hana_bank_dunamu_stake",
  "symbol": "086790/Dunamu_private",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage2_bank_digital_asset_stake",
  "trigger_date": "2026-05-14/2026-05-15",
  "stake_pct": 6.55,
  "transaction_value_krw_trn": 1.0,
  "transaction_value_usd_bn": 0.7,
  "shares_acquired_mn": 2.284,
  "upbit_trading_volume_share_reuters_pct": ">80",
  "kakao_investment_post_sale_stake_pct": 4.03,
  "direct_hana_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "regulatory_approval",
    "capital_ratio_impact",
    "digital_asset_revenue",
    "remittance_product_monetization",
    "crypto_cycle_risk",
    "AML_custody_controls"
  ],
  "trigger_outcome_label": "Stage2_bank_digital_asset_not_Green"
}
```

---

## Case F — Won stablecoin policy mania / Kakao Pay, LG CNS, Aton, ME2ON

```text
symbols = 377300 / LG_CNS / 158430 / 201490
case_type = policy event premium / 4B
archetype = STABLECOIN_POLICY_EVENT_PREMIUM_4B
```

| trigger |                type | date    | 당시 공개 evidence                                                                                                | 가격 anchor           | outcome       |
| ------- | ------------------: | ------- | ------------------------------------------------------------------------------------------------------------- | ------------------- | ------------- |
| T0      |       policy Stage2 | 2025-06 | Lee Jae-myung pledge / won stablecoin expectation                                                             | no single day price | Stage2 policy |
| T1      |       event premium | 2025-06 | Kakao Pay more than doubled in month, LG CNS +70%, Aton +80%, ME2ON tripled                                   | huge rally          | event premium |
| T2      | 4B/regulatory watch | 2025-07 | proposed bill allows issuers with as little as 500M won equity; BOK warns about non-bank issuance and FX risk | no OHLC             | 4B            |
| T3      |       Stage3-Yellow | N/A     | actual issuer license, reserve rule, revenue model not confirmed                                              | no Yellow           | 보류            |

Stablecoin mania는 R6에서 가장 위험한 “Stage2를 Green으로 착각하기 쉬운” case다. FT는 Lee Jae-myung 정부의 won-based stablecoin 기대 때문에 Kakao Pay가 한 달에 두 배 넘게 올랐고, LG CNS는 거의 +70%, Aton은 +80%, ME2ON은 세 배가 됐다고 보도했다. 그러나 같은 보도는 proposed bill이 equity capital 500M won만 있어도 발행을 허용할 수 있어 systemic risk 논란이 있다고 지적했다. 별도 FT 기사에서 Bank of Korea는 non-bank stablecoin issuance가 FX와 통화정책 안정성을 흔들 수 있다고 경고했다. Reuters도 BOK governor가 won stablecoin 자체에 반대하지는 않지만 FX/capital-flow 우려를 제기했다고 전했다. ([Financial Times][6])

```json
{
  "case_id": "r6_loop16_won_stablecoin_policy_mania",
  "symbols": "377300/LG_CNS/158430/201490",
  "best_trigger": "T1/T2",
  "best_trigger_type": "policy_event_premium_with_4B_regulatory_watch",
  "trigger_period": "2025-06/2025-07",
  "kakao_pay_monthly_return_context": ">100%",
  "lg_cns_return_context_pct": 70,
  "aton_return_context_pct": 80,
  "me2on_return_context": "tripled",
  "proposed_minimum_equity_for_issuer_krw_mn": 500,
  "q1_2025_stablecoin_capital_outflow_context_usd_bn": 19,
  "regulatory_risks": [
    "BOK_non_bank_issuer_concern",
    "FX_outflow",
    "reserve_rule_uncertainty",
    "issuer_license_uncertainty",
    "systemic_risk"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "event_premium_not_Green"
}
```

---

## Case G — Hong Kong ELS mis-selling / Korean banks

```text
symbols = 105560 / 055550 / 086790 / 316140 / bank_basket
case_type = hard 4C consumer protection
archetype = ELS_MISSELLING_CONSUMER_PROTECTION_4C
```

| trigger |            type | date       | 당시 공개 evidence                                                                        | 가격 anchor      | outcome         |
| ------- | --------------: | ---------- | ------------------------------------------------------------------------------------- | -------------- | --------------- |
| T0      |         hard 4C | 2024-03-11 | FSS finds banks/brokers mis-sold Hong Kong equity-linked securities                   | no bank price  | 4C              |
| T1      |      validation | 2024-03    | estimated retail investor losses 5.8T won, compensation 20~60% of principal discussed | no price       | loss validation |
| T2      | penalty trigger | 2026-02-12 | FSS to impose fines of around 1T won each on local banks                              | no stock price | hard 4C         |
| T3      |          relief | N/A        | final FSC decision, compensation reserve, product controls not completed              | no relief      | 보류              |

ELS mis-selling은 R6 금융소비자보호 hard 4C다. FT는 FSS investigation이 five banks and six brokerages의 poor compliance and lack of consumer protection을 발견했고, Hong Kong equity-linked securities 관련 retail investor losses가 2024년 약 5.8T won으로 추정되며, compensation이 principal의 20~60% 범위에서 논의됐다고 보도했다. 2026년 Reuters는 FSS가 local banks에 각 around 1T won fines를 부과할 것이라고 전했다. 이는 은행의 NIM/배당보다 먼저 차감해야 하는 consumer-protection hard gate다. ([Financial Times][7])

```json
{
  "case_id": "r6_loop16_hongkong_els_misselling_banks",
  "symbols": "105560/055550/086790/316140/bank_basket",
  "best_trigger": "T0/T2",
  "best_trigger_type": "hard_4C_consumer_protection",
  "mis_selling_investigation_date": "2024-03-11",
  "estimated_retail_losses_krw_trn": 5.8,
  "compensation_range_pct": "20-60",
  "penalty_announcement_date": "2026-02-12",
  "expected_fine_per_bank_krw_trn": 1.0,
  "final_approval_required": "Financial_Services_Commission",
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "hard_4C_success_consumer_protection"
}
```

---

## Case H — Overseas-stock FX flow / securities and FX-risk watch

```text
symbols = securities_basket / banks / 039490 / 005940 / 003540
case_type = Stage2 brokerage opportunity + 4C FX-risk watch
archetype = FX_OVERSEAS_STOCK_FLOW_4C_WATCH
```

| trigger |                      type | date       | 당시 공개 evidence                                                                                          | 가격 anchor             | outcome    |
| ------- | ------------------------: | ---------- | ------------------------------------------------------------------------------------------------------- | --------------------- | ---------- |
| T0      |        Stage2 opportunity | 2025~2026  | Korean retail demand for U.S. stocks keeps brokerage FX/trading flow high                               | no sector price       | Stage2     |
| T1      |               4C FX watch | 2026-02-04 | Korean retail held nearly $171B overseas stocks; January net U.S. stock purchases $5B vs December $1.9B | won near 17-year lows | FX watch   |
| T2      | consumer-protection watch | 2025-12-01 | FSS reviews whether firms explain FX hedging risks for overseas investments                             | no price              | regulation |
| T3      |             Stage3-Yellow | N/A        | securities fee revenue and FX-risk controls not confirmed                                               | no Yellow             | 보류         |

해외주식 열풍은 증권사에는 brokerage revenue Stage2지만, R6 관점에서는 FX·소비자보호 4C-watch도 붙는다. Reuters는 Korean retail investors가 2026년 1월 29일 기준 nearly $171B 해외주식을 보유했고, 1월 U.S. stocks net purchases가 $5B로 12월 $1.9B의 두 배 이상이었다고 보도했다. won은 17-year lows 근처였고, FSS는 해외투자 관련 FX hedging risk 설명이 충분한지 점검하겠다고 했다. 즉 “해외주식 수수료 증가”만 보고 금융주 Green을 주면 안 되고, FX risk와 consumer protection을 병기해야 한다. ([Reuters][8])

```json
{
  "case_id": "r6_loop16_overseas_stock_fx_flow",
  "symbols": "securities_basket/banks",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2_brokerage_opportunity_with_4C_FX_watch",
  "retail_overseas_stock_holdings_usd_bn": 171,
  "date_holdings": "2026-01-29",
  "january_us_stock_net_purchases_usd_bn": 5.0,
  "december_us_stock_net_purchases_usd_bn": 1.9,
  "won_context": "near_17_year_lows",
  "fss_fx_risk_review": true,
  "direct_sector_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "brokerage_fee_revenue",
    "FX_hedging_compliance",
    "margin_loan_quality",
    "customer_loss_incidents",
    "retail_flow_durability"
  ],
  "trigger_outcome_label": "brokerage_stage2_with_fx_4C_watch"
}
```

---

## Case I — Toss global expansion / won stablecoin / IPO optionality

```text
symbol = private / possible fintech read-through
case_type = private Stage2 optionality
archetype = PRIVATE_FINTECH_STABLECOIN_IPO_OPTIONALITY_STAGE2
```

| trigger |           type | date       | 당시 공개 evidence                                                                                   | 가격 anchor         | outcome     |
| ------- | -------------: | ---------- | ------------------------------------------------------------------------------------------------ | ----------------- | ----------- |
| T0      | Stage2 private | 2025-09-09 | Toss plans Australia launch, global finance app expansion, won stablecoin once regulation allows | private, no stock | Stage2      |
| T1      |     validation | 2025-09-09 | Toss has 30M+ Korea users; U.S. IPO planned Q2 2026, valuation >$10B and possibly >$15B          | no price          | optionality |
| T2      |       4B-watch | 2025~2026  | stablecoin regulation, overseas execution, IPO market, profitability                             | no price          | 4B          |
| T3      |  Stage3-Yellow | N/A        | listed price / revenue / license not confirmed                                                   | no Yellow         | 보류          |

Toss는 private이지만 R6 digital-finance reference로 필요하다. Reuters는 Toss가 Australia에서 finance super-app을 출시하고, regulation이 허용되면 won-based stablecoin 발행을 목표로 하며, Q2 2026 U.S. IPO를 준비 중이라고 보도했다. Toss는 Korea에서 30M+ users를 확보했고, IPO valuation은 $10B 이상, 일부 보도상 $15B 이상 가능성이 언급됐다. 다만 비상장이라 KRX 가격검증은 불가능하므로 `private Stage2 optionality`로만 둔다. ([Reuters][9])

```json
{
  "case_id": "r6_loop16_toss_global_stablecoin_ipo",
  "symbol": "private",
  "best_trigger": "T0/T1",
  "best_trigger_type": "private_Stage2_fintech_optionality",
  "trigger_date": "2025-09-09",
  "korea_users_mn": 30,
  "australia_launch_target": "end_2025",
  "won_stablecoin_plan": true,
  "ipo_target": "U.S._IPO_Q2_2026",
  "ipo_valuation_context_usd_bn": ">10_to_>15",
  "price_anchor": "price_data_unavailable_private_company",
  "stage3_gate_missing": [
    "public_listing",
    "stablecoin_license",
    "overseas_user_growth",
    "profitability",
    "regulatory_approval"
  ],
  "trigger_outcome_label": "private_fintech_stage2_reference"
}
```

---

# 6. Trigger별 가격경로 검증 요약

| case                      | best trigger |    entry anchor |                                   event MFE/MAE | market-relative | full MFE/MAE | outcome                   |
| ------------------------- | ------------ | --------------: | ----------------------------------------------: | --------------: | ------------ | ------------------------- |
| Samsung buyback           | T1/T2        |           event |                                           +7.2% |     unavailable | unavailable  | Stage2-Actionable         |
| SK Square buyback         | T1/T2        |  no event price |                                     unavailable |             N/A | unavailable  | Stage2 holdco discount    |
| Securities/financial beta | T1/T2        |          sector |       securities +13.5%, financial groups +4.2% |    KOSPI +6.45% | unavailable  | Stage2 beta + 4B          |
| Naver/Dunamu              | T0/T1        |           event |                                  +7% then -4.2% |     unavailable | unavailable  | Stage2 + security 4B      |
| Hana/Dunamu               | T0/T2        |   no Hana price |                                     unavailable |             N/A | unavailable  | Stage2 bank digital-asset |
| Stablecoin mania          | T1/T2        |           theme | Kakao Pay >2x, LG CNS +70%, Aton +80%, ME2ON 3x |     unavailable | unavailable  | event premium / 4B        |
| ELS mis-selling           | T0/T2        | no direct price |                                    fines/losses |             N/A | unavailable  | hard 4C                   |
| Overseas-stock FX flow    | T1/T2        |      macro/flow |                                 no sector price |             N/A | unavailable  | Stage2 brokerage + 4C     |
| Toss                      | T0/T1        |         private |                                  no stock price |             N/A | unavailable  | private Stage2            |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
좋은 Stage2:
- Samsung buyback: 실제 repurchase/cancellation plan과 +7.2% price reaction.
- SK Square buyback: cancellation and discount narrowing attempt.
- Hana Bank / Dunamu: 전통은행의 digital asset stake.
- Toss: private fintech optionality, but no public price.

약한 Stage2:
- stablecoin policy names: price reaction은 강하지만 license/revenue 없음.
- Naver/Dunamu: M&A는 강하지만 Upbit security issue가 즉시 붙음.
```

## Stage2-Actionable entry 성과

```text
Actionable:
- Samsung buyback: size, cancellation, price reaction이 닫힘.
- Naver/Dunamu: initial +7% price reaction and $10.27B deal, but security 4B.
- securities sector: +13.5% sector rally, but market beta and bubble 4B.

Actionable 보류:
- SK Square: price anchor 없음.
- Hana/Dunamu: Hana price anchor 없음.
- Toss: private.
```

## Stage3-Yellow 후보

```text
Yellow 후보:
- Samsung buyback: business recovery and ROE/EPS confirmation 시.
- SK Square: holdco discount narrowing and repeated buyback/dividend policy 확인 시.
- Naver/Dunamu: regulatory approval, security controls, transaction revenue 확인 시.
- Hana/Dunamu: bank capital impact and digital-asset revenue 확인 시.
- securities sector: trading volume and brokerage earnings conversion 확인 시.
```

## Stage3-Green

```text
이번 R6 Loop 16에서 확정 Green 없음.

이유:
- buyback은 강하지만 business/ROE recovery가 필요하다.
- digital-asset M&A는 regulatory approval and security control이 필요하다.
- stablecoin theme는 아직 license/reserve/revenue rule이 없다.
- banks face ELS consumer-protection hard gate.
- brokerage beta는 market turnover and bubble risk에 민감하다.
```

---

# 8. score-price alignment 판정

```text
aligned:
- Samsung buyback
- Naver/Dunamu initial rally and security reversal
- stablecoin mania as event premium
- ELS mis-selling as hard 4C
- securities sector market beta

Stage2_promote_candidate:
- Samsung buyback
- Naver/Dunamu, but 4B security overlay
- Hana/Dunamu, if capital/regulatory treatment clears
- SK Square, if discount narrows

Stage3-Yellow candidate:
- Samsung buyback if ROE/EPS/business recovery follows
- SK Square if buyback/cancellation is repeated and discount narrows
- Naver/Hana digital-asset cases if regulation, custody and revenue close

evidence_good_but_price_failed_or_muted:
- Hana/Dunamu due no Hana price anchor
- SK Square due no event price anchor
- Toss due private status

event_premium:
- stablecoin mania
- securities rally tied to KOSPI boom
- Naver/Dunamu if treated as stablecoin/crypto rerating before approval

thesis_break_watch:
- Upbit abnormal withdrawal
- ELS mis-selling
- FX overseas-investment consumer-protection review
- non-bank stablecoin FX/capital-flow risk

hard_4C_success:
- Hong Kong ELS mis-selling consumer-protection case
```

---

# 9. 점수비중 교정

## 올릴 축

```csv
axis,delta,reason,cases
actual_buyback_cancellation,+5,"단순 buyback보다 cancellation이 있어야 자본배분 score 상승","Samsung, SK Square"
ROE_EPS_recovery_after_buyback,+5,"주주환원 후 EPS/ROE 개선이 Yellow gate","Samsung"
holdco_discount_narrowing,+4,"holding-company discount는 반복 소각/배당/지배구조가 필요","SK Square"
brokerage_turnover_fee_conversion,+4,"증권주 beta는 거래대금이 fee로 전환되어야 함","securities sector"
digital_asset_regulatory_approval,+5,"Dunamu/M&A/stablecoin은 regulatory approval이 핵심","Naver, Hana, Toss"
custody_security_AML,+5,"crypto exchange abnormal withdrawal은 4B/4C overlay","Naver/Dunamu"
bank_capital_ratio_after_digital_asset,+4,"은행이 crypto stake를 사면 capital ratio impact 확인","Hana"
consumer_protection_compliance,+5,"ELS mis-selling은 hard gate","bank basket"
FX_risk_disclosure,+4,"해외주식/FX 흐름은 소비자보호·원화안정성 overlay","securities/banks"
```

## 내릴 축

```csv
axis,delta,reason,cases
buyback_without_business_recovery,-4,"buyback만으로 Green 금지","Samsung"
shareholder_return_without_cancellation,-3,"소각 없는 자사주는 score 낮게","Value-up names"
stablecoin_policy_without_license,-5,"stablecoin 법안 기대만으로 Green 금지","Kakao Pay, LG CNS, Aton, ME2ON"
crypto_MA_without_security_controls,-5,"exchange M&A는 custody/security 전 Green 금지","Naver/Dunamu"
bank_digital_asset_without_capital_clarity,-4,"은행의 crypto stake는 capital/regulatory gate 필요","Hana"
market_beta_without_earnings,-4,"증권주 급등은 거래대금/IB 수익 확인 전 Stage2","securities sector"
overseas_stock_flow_without_FX_risk,-4,"해외주식 flow는 FX/consumer risk 병기","securities/banks"
```

---

# 10. Stage2-Actionable 승격 조건

R6 Loop 16 shadow rule:

```text
R6에서 Stage2 evidence가 아래 중 3개 이상이면 Stage2-Actionable로 승격한다.

1. buyback 규모가 크고 실제 cancellation이 명시된다.
2. event return이 +5% 이상이다.
3. market-relative return이 +5pp 이상이다.
4. capital allocation이 EPS/ROE/discount narrowing으로 연결될 수 있다.
5. digital-asset deal은 deal value, stake, approval path, revenue model이 구체적이다.
6. brokerage beta는 거래대금/foreign inflow/fee income으로 연결된다.
7. consumer-protection, custody/security, FX risk hard gate가 없다.
```

적용:

```text
Samsung buyback:
1,2 충족 → Stage2-Actionable.

Naver/Dunamu:
2,5 충족하지만 security 4B → Stage2 + 4B.

SK Square:
1,4 충족하지만 price anchor 없음 → Stage2.

Stablecoin mania:
2는 강하지만 5,7 부재 → event premium / 4B.

Hana/Dunamu:
5는 강하지만 price/capital/regulatory gate → Stage2.
```

---

# 11. Stage3-Yellow 조건

```text
Stage3-Yellow:
- Stage2-Actionable 이후 EPS/ROE/fee income/revenue model이 바뀔 가능성이 높아진 상태.
- 하지만 approval, security, capital ratio, consumer-protection 중 하나가 남은 상태.
```

Yellow 후보:

```text
Samsung buyback:
EPS/ROE recovery and business improvement 확인 시 Yellow.

SK Square:
discount narrowing and repeated capital return 확인 시 Yellow.

Naver/Dunamu:
regulatory approval + security remediation + transaction revenue 확인 시 Yellow.

Hana/Dunamu:
capital ratio impact + digital asset revenue + regulatory treatment 확인 시 Yellow.

Securities sector:
turnover and brokerage-fee earnings 확인 시 Yellow.
```

---

# 12. Stage3-Green 조건

```text
Stage3-Green:
- buyback is executed and cancelled.
- ROE/EPS improves after capital return.
- digital-asset M&A receives regulatory approval.
- custody/security/AML controls are proven.
- stablecoin issuer license, reserve rule and revenue model are confirmed.
- ELS/consumer-protection liabilities are provisioned and cleared.
- FX overseas-stock risk is managed.
- full-window MFE/MAE is favorable.
```

이번 R6 Loop 16에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
reason = full OHLC unavailable + regulatory/security/capital/ROE gates not fully closed
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- buyback rally occurs without business recovery.
- stablecoin theme rallies before issuer license/reserve rules.
- crypto exchange M&A rallies before security/custody controls.
- brokerage stocks rally on market beta before fee earnings.
- bank buys crypto stake before capital/risk-weight treatment is known.
- retail overseas-stock flow grows while won/FX risk worsens.
```

적용:

```text
Samsung:
buyback + business competitiveness gate → 4B watch.

Naver/Dunamu:
M&A + abnormal withdrawal → 4B/security.

Stablecoin names:
huge price action + regulatory uncertainty → 4B event premium.

Hana/Dunamu:
strategic stake + capital/regulatory gate → 4B.

Securities sector:
+13.5% sector jump + bubble commentary → 4B.
```

---

# 14. 4C hard gate 조건

```text
R6 4C:
- mis-selling / consumer-protection fine
- crypto exchange abnormal withdrawal / custody failure
- data breach in financial platform
- stablecoin issuer failure / reserve mismatch
- FX-risk mis-disclosure to retail investors
- capital ratio breach after acquisition or digital-asset exposure
```

이번 R6 Loop 16 hard 4C:

```text
Hong Kong ELS mis-selling = hard_4C_success
```

Strong 4C-watch:

```text
- Upbit abnormal withdrawal
- stablecoin non-bank issuer / FX risk
- overseas-stock FX risk disclosure
- bank crypto stake capital treatment
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

R6 production 설계 원칙:

```text
1. buyback announcement, actual repurchase, cancellation을 분리한다.
2. shareholder return과 business recovery를 분리한다.
3. stablecoin policy, issuer license, reserve rule, actual issuance를 분리한다.
4. crypto exchange M&A와 custody/security event를 같은 row에 섞지 않는다.
5. brokerage beta와 fee income을 분리한다.
6. consumer-protection liability는 hard 4C로 별도 row에 둔다.
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_242.md 요약

```md
# R6 Loop 16. Financials / Capital Allocation / Digital Finance Trigger-level Price Validation

이번 라운드는 R6 Loop 16 trigger-level validation 라운드다.

핵심 결론:
- Samsung Electronics buyback is the cleanest Stage2-Actionable capital-allocation template. Samsung announced a 10T won / $7.17B one-year buyback, first since 2017, with 3T won to be repurchased and cancelled in the first three months. Shares rose 7.2%, the biggest daily jump since March 2020. Green requires business recovery, ROE/EPS improvement and full OHLC.
- SK Square buyback is Stage2 holdco discount. It will cancel 100B won already bought back and repurchase/cancel another 100B won. Palliser activism and Value-Up support are real, but price anchor and discount-narrowing evidence are missing.
- Securities and financial groups are Stage2 market beta with 4B. On May 6, 2026 KOSPI closed +6.45% at 7,384.56, foreign investors bought 3.1T won, securities sector rose 13.5%, financial groups 4.2%. Brokerage earnings confirmation is required.
- Naver Financial / Dunamu is Stage2 M&A with security 4B. Naver Financial will acquire Dunamu in a 15.13T won / $10.27B all-stock deal. Naver initially rose over 7% but later fell 4.2% after a 54B won abnormal withdrawal at Upbit.
- Hana Bank / Dunamu is Stage2 bank digital-asset entry. Hana Bank will buy a 6.55% stake for 1T won / about $700M; Upbit handles more than 80% of Korea virtual asset trading volume according to Reuters. Capital and regulatory treatment are gates.
- Won stablecoin mania is event premium / 4B. Kakao Pay more than doubled in a month, LG CNS rose nearly 70%, Aton 80%, ME2ON tripled, but issuer license, reserve rules, BOK concerns and FX risk remain unresolved.
- Hong Kong ELS mis-selling is hard 4C. FSS is set to impose around 1T won fines each on local banks; earlier estimated retail losses were 5.8T won and compensation of 20~60% of principal was discussed.
- Overseas-stock FX flow is Stage2 brokerage opportunity with 4C FX watch. Korean retail held nearly $171B overseas stocks and bought $5B net U.S. stocks in January 2026, while the won was near 17-year lows and FSS reviewed FX-risk disclosures.
- Toss is private Stage2 fintech optionality. 30M+ users, Australia launch, won stablecoin ambition and U.S. IPO plan are meaningful, but no public price or license yet.

Main calibration:
- Raise actual_buyback_cancellation, ROE_EPS_recovery_after_buyback, holdco_discount_narrowing, brokerage_turnover_fee_conversion, digital_asset_regulatory_approval, custody_security_AML, bank_capital_ratio_after_digital_asset, consumer_protection_compliance, FX_risk_disclosure.
- Lower buyback_without_business_recovery, shareholder_return_without_cancellation, stablecoin_policy_without_license, crypto_MA_without_security_controls, bank_digital_asset_without_capital_clarity, market_beta_without_earnings, overseas_stock_flow_without_FX_risk.
```

## docs/checkpoints/checkpoint_28a_round242_r6_loop16.md 요약

```md
# Checkpoint 28A Round 242 R6 Loop 16 Trigger-level Calibration

## 반영 내용
- R6 Loop 16 trigger-level validation을 수행했다.
- Samsung buyback, SK Square buyback, securities/financial sector market beta, Naver Financial/Dunamu, Hana Bank/Dunamu, won stablecoin mania, Hong Kong ELS mis-selling, overseas-stock FX flow, Toss private fintech optionality를 검토했다.
- full adjusted OHLC window는 확보하지 못했으므로 Reuters / FT / WSJ / MarketWatch / Barron’s의 reported event return과 event price anchor를 사용했다.
- OHLC 미확보를 이유로 Stage 후보를 강등하지 않고, price_data_unavailable_after_deep_search로 분리 기록했다.

## 핵심 보정
- buyback announcement, actual repurchase and cancellation을 분리한다.
- 주주환원은 business recovery and ROE/EPS 개선 전에는 Green이 아니다.
- stablecoin policy theme는 issuer license, reserve rule and revenue model 전까지 4B event premium이다.
- crypto exchange M&A는 custody/security/AML controls 없으면 4B/4C overlay가 붙는다.
- bank digital-asset stake는 capital ratio and regulatory treatment를 확인해야 한다.
- ELS mis-selling and consumer-protection penalties are hard 4C.
- 해외주식 flow는 brokerage opportunity이지만 FX-risk disclosure and won pressure를 병기한다.
```

## data/e2r_case_library/cases_r6_loop16_round242.jsonl 초안

```jsonl
{"case_id":"r6_loop16_samsung_buyback_capital_allocation","symbol":"005930","company_name":"Samsung Electronics","case_type":"Stage2_Actionable_capital_allocation","primary_archetype":"BUYBACK_CANCELLATION_VALUEUP_STAGE2_ACTIONABLE","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2024-11-15","buyback_value_krw_trn":10,"buyback_value_usd_bn":7.17,"first_buyback_since":2017,"initial_cancelled_repurchase_krw_trn":3,"event_return_pct":7.2,"ytd_decline_before_buyback_pct":-32,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_actionable_buyback","notes":"Large buyback with cancellation and strong price reaction; business/ROE recovery needed for Yellow/Green."}
{"case_id":"r6_loop16_sk_square_buyback_holdco_discount","symbol":"402340","company_name":"SK Square","case_type":"Stage2_holdco_discount_buyback","primary_archetype":"HOLDCO_DISCOUNT_BUYBACK_STAGE2","best_trigger":"T1/T2","stage_candidate":"Stage2","price_validation":{"trigger_date":"2024-11-21","cancel_previous_buyback_krw_bn":100,"new_repurchase_cancel_plan_krw_bn":100,"sk_hynix_stake_pct":20,"market_value_vs_stake_value":"<50%","activist":"Palliser_Capital","palliser_stake_pct_context":1,"direct_event_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_holdco_valueup_not_Green","notes":"Buyback/cancellation and activism are real, but event price and discount narrowing are missing."}
{"case_id":"r6_loop16_kospi_brokerage_financial_beta","symbol":"securities_sector/financial_groups_sector","company_name":"Korean securities and financial groups basket","case_type":"Stage2_brokerage_beta_with_4B_bubble_watch","primary_archetype":"BROKERAGE_TRADING_VOLUME_STAGE2_BETA","best_trigger":"T1/T2","stage_candidate":"Stage2_beta","price_validation":{"trigger_date":"2026-05-06","kospi_event_return_pct":6.45,"kospi_close":7384.56,"foreign_net_buy_krw_trn":3.1,"foreign_net_buy_usd_bn":2.13,"securities_sector_event_return_pct":13.5,"financial_groups_event_return_pct":4.2,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_market_beta_with_4B","notes":"Trading-volume and market-confidence beta are strong, but brokerage earnings and bubble risk must be checked."}
{"case_id":"r6_loop16_naver_financial_dunamu_ma","symbol":"035420/Dunamu_private","company_name":"Naver Financial / Dunamu","case_type":"Stage2_MA_with_security_4B","primary_archetype":"FINTECH_CRYPTO_EXCHANGE_MA_STAGE2_WITH_SECURITY_4B","best_trigger":"T0/T1","stage_candidate":"Stage2 + 4B-watch","price_validation":{"trigger_date":"2025-11-27","deal_value_krw_trn":15.13,"deal_value_usd_bn":10.27,"stock_swap_ratio":"2.54_Naver_Financial_shares_per_Dunamu_share","naver_initial_event_return_pct":7,"naver_later_event_return_pct":-4.2,"abnormal_withdrawal_krw_bn":54,"upbit_market_share_context_pct":70,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_digital_asset_MA_with_security_4B","notes":"Large digital-asset M&A is real, but abnormal withdrawal requires security/custody overlay."}
{"case_id":"r6_loop16_hana_bank_dunamu_stake","symbol":"086790/Dunamu_private","company_name":"Hana Financial / Hana Bank / Dunamu","case_type":"Stage2_bank_digital_asset_stake","primary_archetype":"BANK_DIGITAL_ASSET_STAKE_STAGE2_WITH_CAPITAL_GATE","best_trigger":"T0/T2","stage_candidate":"Stage2","price_validation":{"trigger_date":"2026-05-14/2026-05-15","stake_pct":6.55,"transaction_value_krw_trn":1.0,"transaction_value_usd_bn":0.7,"shares_acquired_mn":2.284,"upbit_trading_volume_share_reuters_pct":">80","kakao_investment_post_sale_stake_pct":4.03,"direct_hana_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_bank_digital_asset_not_Green","notes":"Bank digital-asset entry is strategic, but capital ratio, regulatory treatment and revenue model are gates."}
{"case_id":"r6_loop16_won_stablecoin_policy_mania","symbol":"377300/LG_CNS/158430/201490","company_name":"Kakao Pay / LG CNS / Aton / ME2ON","case_type":"policy_event_premium_with_4B_regulatory_watch","primary_archetype":"STABLECOIN_POLICY_EVENT_PREMIUM_4B","best_trigger":"T1/T2","stage_candidate":"event_premium_4B","price_validation":{"trigger_period":"2025-06/2025-07","kakao_pay_monthly_return_context":">100%","lg_cns_return_context_pct":70,"aton_return_context_pct":80,"me2on_return_context":"tripled","proposed_minimum_equity_for_issuer_krw_mn":500,"q1_2025_stablecoin_capital_outflow_context_usd_bn":19,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_not_Green","notes":"Won stablecoin policy rally lacks license, reserve rules and revenue model; BOK FX/capital-flow concern is 4B/4C."}
{"case_id":"r6_loop16_hongkong_els_misselling_banks","symbol":"105560/055550/086790/316140/bank_basket","company_name":"KB / Shinhan / Hana / Woori bank basket","case_type":"hard_4C_consumer_protection","primary_archetype":"ELS_MISSELLING_CONSUMER_PROTECTION_4C","best_trigger":"T0/T2","stage_candidate":"4C","price_validation":{"mis_selling_investigation_date":"2024-03-11","estimated_retail_losses_krw_trn":5.8,"compensation_range_pct":"20-60","penalty_announcement_date":"2026-02-12","expected_fine_per_bank_krw_trn":1.0,"final_approval_required":"Financial_Services_Commission","direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"hard_4C_success","notes":"Consumer-protection liability and fines are hard 4C for banks."}
{"case_id":"r6_loop16_overseas_stock_fx_flow","symbol":"securities_basket/banks","company_name":"Korean securities / banks FX-flow basket","case_type":"Stage2_brokerage_opportunity_with_4C_FX_watch","primary_archetype":"FX_OVERSEAS_STOCK_FLOW_4C_WATCH","best_trigger":"T1/T2","stage_candidate":"Stage2 + 4C-watch","price_validation":{"retail_overseas_stock_holdings_usd_bn":171,"date_holdings":"2026-01-29","january_us_stock_net_purchases_usd_bn":5.0,"december_us_stock_net_purchases_usd_bn":1.9,"won_context":"near_17_year_lows","fss_fx_risk_review":true,"direct_sector_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"brokerage_stage2_with_fx_4C_watch","notes":"Overseas-stock flow can lift brokerage revenue but adds won/FX and consumer-protection risk."}
{"case_id":"r6_loop16_toss_global_stablecoin_ipo","symbol":"private","company_name":"Toss / Viva Republica","case_type":"private_fintech_stage2_reference","primary_archetype":"PRIVATE_FINTECH_STABLECOIN_IPO_OPTIONALITY_STAGE2","best_trigger":"T0/T1","stage_candidate":"private_Stage2","price_validation":{"trigger_date":"2025-09-09","korea_users_mn":30,"australia_launch_target":"end_2025","won_stablecoin_plan":true,"ipo_target":"U.S._IPO_Q2_2026","ipo_valuation_context_usd_bn":">10_to_>15","price_anchor":"price_data_unavailable_private_company"},"score_price_alignment":"private_reference","notes":"Private fintech optionality only; no public price, stablecoin license or IPO yet."}
```

## data/e2r_trigger_calibration/triggers_r6_loop16_round242.jsonl 초안

```jsonl
{"trigger_id":"r6l16_samsung_buyback_T1","case_id":"r6_loop16_samsung_buyback_capital_allocation","trigger_type":"Stage2-Actionable","trigger_date":"2024-11-15","evidence_available":"Samsung announces 10T won / $7.17B one-year buyback, first since 2017, with 3T won to be repurchased and cancelled first; shares +7.2%","event_return_pct":7.2,"trigger_outcome_label":"excellent_stage2_actionable_buyback","promote_to":"Stage2-Actionable"}
{"trigger_id":"r6l16_sksquare_buyback_T1","case_id":"r6_loop16_sk_square_buyback_holdco_discount","trigger_type":"Stage2_buyback_holdco_discount","trigger_date":"2024-11-21","evidence_available":"SK Square to cancel 100B won shares already bought and repurchase/cancel another 100B won; Palliser activism and Value-Up context","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_holdco_valueup_not_Green","promote_to":"Stage2"}
{"trigger_id":"r6l16_brokerage_beta_T1","case_id":"r6_loop16_kospi_brokerage_financial_beta","trigger_type":"Stage2_market_beta","trigger_date":"2026-05-06","evidence_available":"KOSPI +6.45% to 7,384.56; foreign net buy 3.1T won; securities sector +13.5%, financial groups +4.2%","event_return_pct":"securities +13.5 / financial groups +4.2","trigger_outcome_label":"Stage2_brokerage_beta_with_4B_bubble_watch","promote_to":"Stage2+4B"}
{"trigger_id":"r6l16_naver_dunamu_T0","case_id":"r6_loop16_naver_financial_dunamu_ma","trigger_type":"Stage2_MA_with_4B_security","trigger_date":"2025-11-27","evidence_available":"Naver Financial to acquire Dunamu in 15.13T won / $10.27B all-stock deal; Naver initially +7%, later -4.2% after 54B won Upbit abnormal withdrawal","event_return_pct":"initial +7 / later -4.2","trigger_outcome_label":"Stage2_digital_asset_MA_with_security_4B","promote_to":"Stage2+4B"}
{"trigger_id":"r6l16_hana_dunamu_T0","case_id":"r6_loop16_hana_bank_dunamu_stake","trigger_type":"Stage2_bank_digital_asset","trigger_date":"2026-05-14/2026-05-15","evidence_available":"Hana Bank to buy 6.55% Dunamu stake for 1T won / about $700M; Upbit handles more than 80% Korea virtual asset trading volume per Reuters","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_bank_digital_asset_not_Green","promote_to":"Stage2"}
{"trigger_id":"r6l16_stablecoin_mania_T1","case_id":"r6_loop16_won_stablecoin_policy_mania","trigger_type":"event_premium_4B","trigger_date":"2025-06/2025-07","evidence_available":"Kakao Pay more than doubled, LG CNS almost +70%, Aton +80%, ME2ON tripled on won stablecoin expectations; BOK warns on non-bank issuer/FX risks","event_return_pct":"Kakao Pay >100 / LG CNS +70 / Aton +80 / ME2ON 3x","trigger_outcome_label":"stablecoin_policy_event_premium_not_Green","promote_to":"4B-watch"}
{"trigger_id":"r6l16_els_misselling_T0","case_id":"r6_loop16_hongkong_els_misselling_banks","trigger_type":"hard_4C","trigger_date":"2024-03-11/2026-02-12","evidence_available":"FSS found Hong Kong ELS mis-selling; estimated 5.8T won retail losses, compensation 20-60%, later around 1T won fines each for local banks","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"hard_4C_success_consumer_protection","promote_to":"4C"}
{"trigger_id":"r6l16_overseas_stock_fx_T1","case_id":"r6_loop16_overseas_stock_fx_flow","trigger_type":"Stage2_brokerage_plus_4C_FX_watch","trigger_date":"2026-02-04/2025-12-01","evidence_available":"Korean retail held nearly $171B overseas stocks, January net U.S. stock purchases $5B vs December $1.9B; FSS reviews FX-risk explanations","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"brokerage_stage2_with_fx_4C_watch","promote_to":"Stage2+4C-watch"}
{"trigger_id":"r6l16_toss_private_T0","case_id":"r6_loop16_toss_global_stablecoin_ipo","trigger_type":"private_Stage2_reference","trigger_date":"2025-09-09","evidence_available":"Toss has 30M+ users, plans Australia launch, won stablecoin when regulation allows, and U.S. IPO in Q2 2026 at >$10B valuation context","event_return_pct":"private_company_no_public_price","trigger_outcome_label":"private_fintech_stage2_reference","promote_to":"Stage2_reference"}
```

## data/sector_taxonomy/score_weight_profiles_round242_r6_loop16_v1.csv 초안

```csv
archetype,actual_buyback_cancellation,roe_eps_recovery_after_buyback,holdco_discount_narrowing,brokerage_turnover_fee_conversion,digital_asset_regulatory_approval,custody_security_aml,bank_capital_ratio_after_digital_asset,consumer_protection_compliance,fx_risk_disclosure,buyback_without_business_recovery_penalty,stablecoin_policy_without_license_penalty,crypto_ma_without_security_controls_penalty,market_beta_without_earnings_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
BUYBACK_CANCELLATION_VALUEUP_STAGE2_ACTIONABLE,+5,+5,+1,+0,+0,+0,+0,+1,+0,-4,-1,-1,-1,buyback+cancellation+price reaction,business recovery pending,executed cancellation+ROE/EPS,Samsung buyback template.
HOLDCO_DISCOUNT_BUYBACK_STAGE2,+5,+2,+5,+0,+0,+0,+0,+1,+0,-3,-1,-1,-1,buyback cancellation+activism,discount narrowing missing,repeated return+discount narrowing,SK Square.
BROKERAGE_TRADING_VOLUME_STAGE2_BETA,+0,+1,+0,+5,+0,+0,+0,+2,+3,-1,-1,-1,-4,market rally+sector beta,fee earnings missing,turnover+fee+IB earnings,securities sector.
BANK_DIGITAL_ASSET_STAKE_STAGE2_WITH_CAPITAL_GATE,+0,+1,+0,+1,+5,+5,+5,+3,+2,-1,-3,-4,-1,bank crypto stake,capital/regulation/revenue missing,approval+capital ratio+revenue,Hana/Dunamu.
FINTECH_CRYPTO_EXCHANGE_MA_STAGE2_WITH_SECURITY_4B,+0,+1,+0,+2,+5,+5,+1,+3,+1,-1,-3,-5,-1,crypto exchange M&A,security/approval missing,approval+custody+revenue,Naver/Dunamu.
STABLECOIN_POLICY_EVENT_PREMIUM_4B,+0,+0,+0,+1,+5,+4,+2,+2,+5,-1,-5,-3,-1,policy rally,license/reserve/revenue missing,licensed issuance+reserve+revenue,Kakao Pay/LG CNS/Aton/ME2ON.
ELS_MISSELLING_CONSUMER_PROTECTION_4C,+0,+0,+0,+0,+0,+0,+3,+5,+1,-1,-1,-1,-1,mis-selling fines/losses,final compensation pending,N/A,bank ELS hard 4C.
FX_OVERSEAS_STOCK_FLOW_4C_WATCH,+0,+0,+0,+5,+0,+1,+2,+4,+5,-1,-1,-1,-3,overseas-stock flow,FX disclosure/margin quality pending,fee income+FX risk controlled,securities/banks.
PRIVATE_FINTECH_STABLECOIN_IPO_OPTIONALITY_STAGE2,+0,+1,+0,+1,+5,+4,+2,+2,+2,-1,-5,-2,-1,private fintech optionality,listing/license missing,public listing+license+profit,Toss reference.
```

---

# 이번 R6 Loop 16 결론

```text
1. Samsung buyback은 R6의 가장 깨끗한 Stage2-Actionable이다.
   10T won buyback, 3T won cancellation, +7.2% event reaction이 닫혔다.

2. SK Square buyback은 Stage2 holdco-discount case다.
   자사주 소각과 activist pressure는 좋지만, discount narrowing과 event price가 필요하다.

3. 증권·금융 sector rally는 Stage2 market beta다.
   securities +13.5%, financial groups +4.2%는 강하지만, brokerage fee earnings 전에는 Green이 아니다.

4. Naver Financial / Dunamu는 Stage2 M&A + 4B다.
   $10.27B deal은 크지만 Upbit 54B won abnormal withdrawal이 security overlay를 만들었다.

5. Hana Bank / Dunamu는 Stage2 bank digital-asset entry다.
   1T won stake는 전략적이지만 capital ratio, regulation, revenue model이 필요하다.

6. Stablecoin mania는 event premium / 4B다.
   Kakao Pay >2x, LG CNS +70%, Aton +80%, ME2ON 3x는 강하지만 license/reserve/revenue가 없다.

7. Hong Kong ELS mis-selling은 hard 4C다.
   5.8T won retail losses and around 1T won fines each for banks는 consumer-protection hard gate다.

8. Overseas-stock FX flow는 Stage2 brokerage opportunity + 4C-watch다.
   $171B overseas holdings and $5B January U.S. stock purchases are fee opportunities but FX/consumer-risk overlay가 붙는다.

9. Toss는 private Stage2 optionality다.
   30M+ users, global expansion, stablecoin and IPO plan은 좋지만 public price and license가 없다.
```

한 문장으로 압축하면:

> **R6 Loop 16에서 배운 핵심은 “주주환원·스테이블코인·디지털자산 headline”이 아니라, 실제 소각, ROE/EPS 개선, discount narrowing, regulatory approval, custody/security, bank capital impact, consumer-protection liability, FX-risk disclosure가 닫혀야 Stage3로 올릴 수 있다는 것이다. 반대로 buyback만, stablecoin policy만, crypto M&A만, market beta만으로는 4B/false positive가 되기 쉽다.**

[1]: https://www.reuters.com/technology/samsung-electronics-plans-72-bln-buyback-boost-shareholder-value-2024-11-15/?utm_source=chatgpt.com "Samsung Electronics plans $7.2 billion buyback after share price plunges"
[2]: https://www.reuters.com/technology/artificial-intelligence/south-koreas-ai-chip-investor-announces-plan-share-buybacks-2024-11-21/?utm_source=chatgpt.com "South Korea's AI chip investor announces plan for share buybacks"
[3]: https://www.reuters.com/world/asia-pacific/south-koreas-kospi-share-index-tops-7000-first-time-2026-05-06/?utm_source=chatgpt.com "Korea's KOSPI breaks 7,000 as AI rally catapults Samsung into $1 trillion club"
[4]: https://www.reuters.com/world/asia-pacific/navers-payment-arm-acquire-south-korean-crypto-exchange-operator-10-bln-deal-2025-11-27/?utm_source=chatgpt.com "Naver's payment arm to acquire South Korean crypto exchange operator in $10 bln deal"
[5]: https://www.reuters.com/world/asia-pacific/hana-bank-acquire-stake-dunamu-700-mln-filing-says-2026-05-14/?utm_source=chatgpt.com "Hana Bank to acquire stake in Dunamu for $700 mln, filing says"
[6]: https://www.ft.com/content/4b19bf90-4202-4fe7-8caf-d7db6deeb768?utm_source=chatgpt.com "Crypto-crazy investors make South Korea the best-performing market in Asia"
[7]: https://www.ft.com/content/5dd7c59d-3198-42ba-b6a0-7cc4baa92ae0?utm_source=chatgpt.com "South Korea says banks 'mis-sold' China-linked derivatives"
[8]: https://www.reuters.com/world/asia-pacific/koreas-fight-fx-stability-undermined-by-its-wall-street-mania-2026-02-04/?utm_source=chatgpt.com "Korea's fight for FX stability undermined by its Wall Street mania"
[9]: https://www.reuters.com/business/finance/south-korean-fintech-toss-plans-global-push-starting-australia-aims-issue-won-2025-09-09/?utm_source=chatgpt.com "South Korean fintech Toss plans global push starting in Australia, aims to issue won stablecoin"

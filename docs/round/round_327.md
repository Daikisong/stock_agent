순서상 이번은 **R6 Loop 17 — 금융·자본배분·디지털금융 trigger-level price validation 라운드**다.

```text
round = R6 Loop 17
round_id = round_255
large_sector = FINANCIALS_CAPITAL_ALLOCATION_DIGITAL_FINANCE
method = trigger_level_backtest_v1_after_redteam
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R7 Loop 17
```

이번 라운드도 KRX/Naver/Yahoo/Stooq 수정주가 일봉 OHLC window를 안정적으로 직접 확보하지 못했다. 그래서 MFE/MAE/peak/drawdown 숫자는 만들지 않는다. 대신 Reuters/FT/WSJ의 **reported event return, sector-index move, deal value, stake %, buyback amount, abnormal-withdrawal amount, regulatory fine, trading-volume/policy trigger**를 가격 anchor로 쓴다. 즉 `MFE_30D/90D/180D/1Y/2Y = price_data_unavailable_after_deep_search`다.

---

# 1. 이번 라운드 대섹터

```text
R6 = 금융·자본배분·디지털금융
```

R6의 core gate는 아래다.

```text
은행 / 금융지주:
ROE → CET1 → 배당/자사주 소각 → PBR 재평가 → NIM / 대손비용 / ELS·PF·규제 4B

증권:
KOSPI 거래대금 / IPO / margin loan / short-selling normalization → brokerage fee / IB / WM → risk appetite → market correction 4B

보험:
IFRS17 / CSM / 금리 / 자본비율 → 배당여력 → holding-company discount → RBC/K-ICS / cyber / guarantee risk 4B

자본배분:
buyback + cancellation → holding discount 축소 → activist pressure → governance reform → cash-flow sustainability

디지털금융:
crypto exchange stake / stablecoin / payment platform / CBDC / deposit token → regulation → cybersecurity / abnormal withdrawal / AML 4B

금융소비자 보호:
ELS mis-selling, FX risk, data breach, supplier-like abusive practice, bank sanctions → trust / fine / capital buffer 4B
```

---

# 2. 대상 canonical archetype

```text
KOSPI_BOOM_SECURITIES_STAGE2_ACTIONABLE
VALUE_UP_CAPITAL_RETURN_HOLDCO_STAGE2_ACTIONABLE
BANK_CRYPTO_EXCHANGE_STRATEGIC_STAKE_STAGE2
FINTECH_CRYPTO_EXCHANGE_MA_STAGE2_WITH_CYBER_4B
WON_STABLECOIN_RETAIL_FRENZY_STAGE2_OVERHEAT
BANK_STABLECOIN_POLICY_STAGE2_WITH_FX_4B
ELS_MISSELLING_SANCTION_4B
SHORT_SELLING_NORMALIZATION_INFRA_STAGE2_4B
```

---

# 3. deep sub-archetype

```text
Securities / brokerage beta:
- KOSPI crossed 7,000 for the first time on May 6, 2026.
- Securities firms jumped 13.5%, financial groups rose 4.2%.
- This is Stage2-Actionable for securities/brokerage fee beta, but not automatically Green for banks.
- 4B: market correction, AI concentration, tax hikes, retail leverage.

Value-up / capital return:
- South Korea passed governance reform expanding directors’ duties to shareholders in July 2025.
- Buybacks in H1 2025 already exceeded all of 2024.
- SK Square announced 100B won cancellation of prior buyback + another 100B won buyback/cancellation.
- Its market value was less than half the value of its SK Hynix stake.
- Stage2-Actionable capital-return / holding-discount case.

Hana Bank / Dunamu:
- Hana Bank to buy 6.55% Dunamu stake for 1T won / about $700M.
- Upbit handles more than 80% of Korea’s virtual-asset trading volume.
- Largest digital-asset investment by a Korean bank per WSJ context.
- Stage2 digital-asset strategic stake; no price anchor.

Naver Financial / Dunamu:
- Naver Financial agreed to acquire Dunamu in all-stock deal worth 15.13T won / $10.27B.
- Naver shares jumped more than 7%, then traded down 4.2% after a 54B won abnormal crypto withdrawal from Upbit.
- Stage2 M&A with cyber/operational 4B.

Won stablecoin frenzy:
- Kakao Pay more than doubled in June 2025.
- LG CNS rose almost 70%, Aton +80%, ME2ON tripled.
- Trigger was newly elected President Lee’s won-backed stablecoin pledge.
- Stage2 speculative policy theme / overheat, not Green.

BOK / stablecoin / kimchi bonds:
- BOK governor nominee said won stablecoins could coexist with CBDC/deposit tokens.
- Dollar-backed stablecoin trading hit 57T won / $42B in Q1 2025.
- Korea lifted 14-year kimchi bond investment ban to relieve FX imbalance.
- Stage2 policy infrastructure but FX/liquidity/issuer-quality 4B.

Hong Kong ELS sanctions:
- FSS planned around 1T won in fines on local banks over Hong Kong ELS misconduct.
- This is consumer-protection / sales-practice 4B for banks.
- Not hard 4C unless capital/earnings or trust damage becomes structural.

Short-selling normalization:
- Korea planned to lift market-wide short-selling ban in March 2025 after illegal naked short-selling concerns.
- HSBC was cleared by court in a 16B won illegal short-selling case.
- Stage2 capital-market infrastructure normalization, but retail backlash / volatility 4B.
```

---

# 4. 선정 case 요약

| bucket                                 | case                                          | 핵심 판정                                                                                 |
| -------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------- |
| structural_success / Stage2-Actionable | **KOSPI boom / securities firms**             | KOSPI +6.45%, securities firms +13.5%, financial groups +4.2%                         |
| Stage2-Actionable                      | **SK Square buyback / holding-discount**      | 100B won cancellation + 100B won new buyback/cancel, Palliser activist                |
| Stage2 digital finance                 | **Hana Bank / Dunamu stake**                  | 1T won, 6.55%, Upbit >80% virtual-asset volume                                        |
| Stage2 + 4B                            | **Naver Financial / Dunamu all-stock merger** | 15.13T won deal, Naver +7% then -4.2% after Upbit 54B won abnormal withdrawal         |
| overheat / Stage2 speculative          | **Kakao Pay / won stablecoin frenzy**         | Kakao Pay >2x, LG CNS +70%, Aton +80%, ME2ON x3                                       |
| Stage2 policy + FX 4B                  | **BOK stablecoin / kimchi bonds**             | stablecoin positive stance, 57T won dollar-stablecoin trading, kimchi bond ban lifted |
| 4B consumer protection                 | **Hong Kong ELS bank sanctions**              | FSS around 1T won fines on local banks                                                |
| Stage2 market infra + 4B               | **Short-selling normalization / HSBC case**   | ban-lift plan + naked short-selling detection system, retail-volatility 4B            |

---

# 5. 각 case별 trigger grid

## Case A — KOSPI boom / securities firms and financial groups

```text
symbols = 039490 / 005940 / 016360 / 071050 / 105560 / 055550 / 086790 / 316140
case_type = Stage2-Actionable brokerage beta + bank value-up beta
archetype = KOSPI_BOOM_SECURITIES_STAGE2_ACTIONABLE
```

| trigger |              type | date       | 당시 공개 evidence                                                                 | 가격 anchor                      | outcome |
| ------- | ----------------: | ---------- | ------------------------------------------------------------------------------ | ------------------------------ | ------- |
| T0      |            Stage1 | 2025-07-03 | revised Commercial Act expands board duties to shareholders                    | KOSPI +1.34% on reform passage |         |
| T1      |     Stage2 sector | 2025H1~H2  | financials +57%, industrials +54%, tech +45%; buybacks rising                  | sector rerating                |         |
| T2      | Stage2-Actionable | 2026-05-06 | KOSPI breaks 7,000; securities firms +13.5%, financial groups +4.2%            | securities +13.5%              |         |
| T3      |          4B-watch | 2026       | AI concentration, oil/bond shock, retail leverage, tax hike, market correction | 4B                             |         |
| T4      |     Stage3-Yellow | N/A        | brokerage fee/IB/WM earnings confirmation 필요                                   | 보류                             |         |

이 case는 R6에서 가장 직접적인 securities trigger다. 2026년 5월 6일 KOSPI는 7,000을 돌파하고 종가 기준 +6.45%를 기록했으며, 같은 날 securities firms index는 +13.5%, financial groups는 +4.2% 올랐다. 증권주는 거래대금·신용·IPO·IB beta가 바로 붙기 때문에 Stage2-Actionable로 올릴 수 있지만, 은행/금융지주는 그날 KOSPI를 이기지 못했으므로 “금융주 전체 Green”은 아니다. 2025년 rally의 뼈대에는 주주권 보호 법안, value-up 기대, foreign inflow, buyback 확대가 있었다. ([Reuters][1])

```json
{
  "case_id": "r6_loop17_kospi_boom_securities_financials",
  "symbols": "039490/005940/016360/071050/105560/055550/086790/316140",
  "best_trigger": "T2/T3",
  "best_trigger_type": "Stage2-Actionable_brokerage_beta_with_market_4B",
  "trigger_date": "2026-05-06",
  "kospi_event_return_pct": 6.45,
  "securities_firms_index_event_return_pct": 13.5,
  "financial_groups_index_event_return_pct": 4.2,
  "governance_reform_date": "2025-07-03",
  "stage2_logic": [
    "stock_market_turnover_beta",
    "brokerage_fee_beta",
    "IB_and_WM_activity",
    "value_up_rerating"
  ],
  "4B_overlay": [
    "AI_concentration",
    "market_correction",
    "retail_leverage",
    "tax_hike",
    "short_selling_volatility"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_stage2_actionable_for_securities_not_bank_green"
}
```

---

## Case B — SK Square capital return / holding-company discount

```text
symbol = 402340
case_type = Stage2-Actionable capital allocation
archetype = VALUE_UP_CAPITAL_RETURN_HOLDCO_STAGE2_ACTIONABLE
```

| trigger |              type | date       | 당시 공개 evidence                                                                                       | 가격 anchor                 | outcome |
| ------- | ----------------: | ---------- | ---------------------------------------------------------------------------------------------------- | ------------------------- | ------- |
| T0      |            Stage1 | 2024       | Palliser Capital pressure, value-up program, holding discount debate                                 | no clean entry            |         |
| T1      | Stage2-Actionable | 2024-11-21 | SK Square to cancel 100B won previously bought shares and buy back another 100B won for cancellation | no event return in source |         |
| T2      |        validation | 2024-11-21 | market value less than half of $18B SK Hynix stake value                                             | holding discount          |         |
| T3      |          4B-watch | 2024~2026  | discount persists if SK Hynix stake monetization and cash-return policy are not repeated             | 4B                        |         |
| T4      |     Stage3-Yellow | N/A        | recurring buyback/cancel + portfolio monetization needed                                             | 보류                        |         |

SK Square는 R6에서 capital allocation rule을 세우는 데 좋은 case다. Reuters는 SK Square가 2024년 4월 매입했던 100B won 규모 자사주를 소각하고, 추가로 100B won을 매입해 3개월 안에 소각하겠다고 보도했다. Palliser Capital의 undervaluation 개선 요구와 정부 value-up program이 같이 배경에 있고, SK Square의 market value는 보유한 SK Hynix stake value $18B의 절반에도 못 미친다고 보도됐다. 가격 anchor는 없지만, “buyback + cancellation + holding discount”가 동시에 닫힌 Stage2-Actionable이다. ([Reuters][2])

```json
{
  "case_id": "r6_loop17_sk_square_buyback_holding_discount",
  "symbol": "402340",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2-Actionable_capital_return_holding_discount",
  "trigger_date": "2024-11-21",
  "prior_buyback_cancel_krw_bn": 100,
  "new_buyback_cancel_krw_bn": 100,
  "sk_hynix_stake_value_context_usd_bn": 18,
  "market_value_vs_stake_value_context": "less_than_half",
  "activist_context": "Palliser_Capital_1pct_stake_and_engagement",
  "4B_overlay": [
    "one_off_buyback_risk",
    "portfolio_monetization_uncertain",
    "SK_Hynix_price_dependence",
    "holding_company_discount_persistence"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "capital_return_stage2_actionable_no_ohlc"
}
```

---

## Case C — Hana Bank / Dunamu strategic stake

```text
symbols = 086790 / Dunamu_private / 035720_seller_readthrough
case_type = Stage2 digital-asset strategic stake
archetype = BANK_CRYPTO_EXCHANGE_STRATEGIC_STAKE_STAGE2
```

| trigger |                   type | date          | 당시 공개 evidence                                                                                                      | 가격 anchor              | outcome |
| ------- | ---------------------: | ------------- | ------------------------------------------------------------------------------------------------------------------- | ---------------------- | ------- |
| T0      | Stage2 digital finance | 2026-05-14/15 | Hana Bank to buy 6.55% Dunamu stake for 1T won / about $700M                                                        | Hana price unavailable |         |
| T1      |             validation | 2026-05-15    | Upbit handles more than 80% of Korea virtual-asset trading volume                                                   | no listed Dunamu price |         |
| T2      |   strategic validation | 2026-05-15    | WSJ: largest single digital-asset investment by Korean bank; blockchain remittance technical verification completed | no event return        |         |
| T3      |               4B-watch | 2026          | crypto regulation, Upbit operational/cyber risk, valuation, capital allocation                                      | 4B                     |         |
| T4      |          Stage3-Yellow | N/A           | contribution to bank fee income / remittance revenue / regulatory approval needed                                   | 보류                     |         |

Hana Bank/Dunamu는 R6의 가장 직접적인 bank-to-crypto Stage2다. Reuters는 Hana Bank가 Dunamu 6.55% 지분을 1T won, 약 $700M에 인수한다고 보도했고, Dunamu의 Upbit는 한국 virtual-asset trading volume의 80% 이상을 처리한다고 설명했다. WSJ는 이 거래를 한국 은행의 단일 최대 digital-asset investment로 설명했고, Hana와 Dunamu가 blockchain-based overseas remittance service의 technical verification을 마쳤다고 보도했다. 다만 Hana Financial의 직접 event return은 확보하지 못했고, crypto regulation과 Upbit operational risk가 4B다. ([Reuters][3])

```json
{
  "case_id": "r6_loop17_hana_bank_dunamu_stake",
  "symbols": "086790/Dunamu_private/035720_seller_readthrough",
  "best_trigger": "T0/T3",
  "best_trigger_type": "Stage2_bank_crypto_exchange_strategic_stake",
  "trigger_date": "2026-05-14",
  "deal_value_krw_trn": 1.0,
  "deal_value_usd_mn": 700,
  "hana_bank_dunamu_stake_pct": 6.55,
  "upbit_korea_virtual_asset_volume_share_pct": ">80",
  "kakao_investment_post_sale_stake_pct": 4.03,
  "strategic_logic": [
    "digital_asset_strategy",
    "blockchain_remittance",
    "fee_income_optionality",
    "Upbit_market_leadership"
  ],
  "4B_overlay": [
    "crypto_regulation",
    "Upbit_operational_risk",
    "valuation_risk",
    "capital_allocation_risk"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_digital_asset_stake_no_direct_price"
}
```

---

## Case D — Naver Financial / Dunamu all-stock merger

```text
symbols = 035420 / Dunamu_private / Naver_Financial_private
case_type = Stage2 fintech M&A + cyber/operational 4B
archetype = FINTECH_CRYPTO_EXCHANGE_MA_STAGE2_WITH_CYBER_4B
```

| trigger |           type | date       | 당시 공개 evidence                                                                    | 가격 anchor           | outcome |
| ------- | -------------: | ---------- | --------------------------------------------------------------------------------- | ------------------- | ------- |
| T0      |     Stage2 M&A | 2025-11-27 | Naver Financial to acquire Dunamu in all-stock deal worth 15.13T won / $10.27B    | Naver +7% initially |         |
| T1      |     validation | 2025-11-27 | exchange ratio 2.54 Naver Financial shares per 1 Dunamu share                     | same                |         |
| T2      | 4B operational | 2025-11-27 | Upbit abnormal withdrawal 54B won; Upbit to cover with own assets                 | Naver later -4.2%   |         |
| T3      |       4B-watch | 2025~2026  | shareholder/regulatory approval, crypto custody/cybersecurity, Nasdaq speculation | 4B                  |         |
| T4      |  Stage3-Yellow | N/A        | regulatory approval, exchange revenue consolidation, cyber controls needed        | 보류                  |         |

Naver Financial/Dunamu는 digital finance M&A의 textbook Stage2 + 4B다. Reuters는 Naver Financial이 Upbit operator Dunamu를 15.13T won, $10.27B all-stock deal로 인수하기로 했고, Dunamu 1주당 Naver Financial 2.54주를 발행한다고 보도했다. Naver shares는 처음 7% 이상 올랐지만, Upbit에서 54B won abnormal withdrawal 보도가 나오자 4.2% 하락 전환했다. 이건 “digital-asset M&A는 매력적이지만, cyber/operational risk가 즉시 valuation을 때린다”는 case다. ([Reuters][4])

```json
{
  "case_id": "r6_loop17_naver_financial_dunamu_merger",
  "symbols": "035420/Dunamu_private/Naver_Financial_private",
  "best_trigger": "T0/T3",
  "best_trigger_type": "Stage2_fintech_crypto_MA_with_cyber_4B",
  "trigger_date": "2025-11-27",
  "deal_value_krw_trn": 15.13,
  "deal_value_usd_bn": 10.27,
  "exchange_ratio": "2.54_Naver_Financial_shares_per_1_Dunamu_share",
  "naver_initial_event_return_pct": ">7",
  "naver_later_event_return_pct": -4.2,
  "upbit_abnormal_withdrawal_krw_bn": 54,
  "4B_overlay": [
    "regulatory_approval",
    "shareholder_approval",
    "crypto_custody_cybersecurity",
    "abnormal_withdrawal",
    "valuation_and_Nasdaq_speculation"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_fintech_MA_with_operational_4B"
}
```

---

## Case E — Kakao Pay / won-stablecoin retail frenzy

```text
symbols = 377300 / 012510 / 158430 / 201490
case_type = Stage2 speculative digital-money theme / overheat
archetype = WON_STABLECOIN_RETAIL_FRENZY_STAGE2_OVERHEAT
```

| trigger |               type | date    | 당시 공개 evidence                                                                           | 가격 anchor          | outcome |
| ------- | -----------------: | ------- | ---------------------------------------------------------------------------------------- | ------------------ | ------- |
| T0      |      Stage1 policy | 2025-06 | President Lee pledge to allow won-backed crypto assets                                   | no single entry    |         |
| T1      | Stage2 speculative | 2025-06 | Kakao Pay more than doubled; LG CNS almost +70%; Aton +80%; ME2ON tripled                | broad event return |         |
| T2      |         validation | 2025-06 | BOK digital-currency project names caught bid; won-based stablecoin bill discussion      | same               |         |
| T3      |        4B-overheat | 2025    | margin loans 20.5T won, low capital threshold bill criticized, regulatory clarity absent | 4B                 |         |
| T4      |      Stage3-Yellow | N/A     | stablecoin law, licensed issuers, revenue model, reserve rules needed                    | 보류                 |         |

Kakao Pay stablecoin frenzy는 R6에서 “Stage2지만 Green 금지”의 대표다. FT는 2025년 6월 won-backed stablecoin 기대감으로 Kakao Pay shares가 한 달에 2배 이상 올랐고, LG CNS가 거의 70%, Aton이 80%, ME2ON이 3배 올랐다고 보도했다. 이 랠리는 정부의 won-based digital money 기대와 retail leverage가 섞인 theme다. 하지만 법안의 issuer capital threshold, BOK의 non-bank issuer 우려, 규제 framework 부재가 모두 4B다. ([Financial Times][5])

```json
{
  "case_id": "r6_loop17_kakao_pay_won_stablecoin_frenzy",
  "symbols": "377300/012510/158430/201490",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2_speculative_won_stablecoin_theme_with_overheat_4B",
  "trigger_period": "2025-06",
  "kakao_pay_event_return_context": ">2x",
  "lg_cns_event_return_context_pct": "almost_70",
  "aton_event_return_context_pct": 80,
  "me2on_event_return_context": "tripled",
  "margin_loans_context_krw_trn": 20.5,
  "4B_overlay": [
    "regulatory_framework_missing",
    "issuer_capital_threshold_risk",
    "BOK_non_bank_issuer_concern",
    "retail_leverage",
    "theme_overheat"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_speculative_overheat_not_Green"
}
```

---

## Case F — BOK stablecoin stance / kimchi bond FX-liquidity policy

```text
symbols = bank_payment_stablecoin_basket / 377300 / 035420 / 086790
case_type = Stage2 policy infrastructure + FX 4B
archetype = BANK_STABLECOIN_POLICY_STAGE2_WITH_FX_4B
```

| trigger |                 type | date       | 당시 공개 evidence                                                                                   | 가격 anchor      | outcome |
| ------- | -------------------: | ---------- | ------------------------------------------------------------------------------------------------ | -------------- | ------- |
| T0      |        Stage2 policy | 2026-04-14 | BOK governor nominee positive on won-denominated stablecoins coexisting with CBDC/deposit tokens | no stock price |         |
| T1      | FX-policy validation | 2025-06-30 | dollar-backed stablecoin trading hit 57T won / $42B in Q1 2025                                   | no stock price |         |
| T2      |      policy response | 2025-06-30 | Korea lifts 14-year ban on local financial institutions investing in kimchi bonds                | no price       |         |
| T3      |             4B-watch | 2025~2026  | FX liquidity, won weakness, issuer quality, reserve rules, capital flow                          | 4B             |         |
| T4      |        Stage3-Yellow | N/A        | law / licensed issuers / bank revenue model needed                                               | 보류             |         |

BOK stablecoin stance는 speculative stock theme와 분리해야 한다. Reuters는 BOK governor nominee Shin Hyun-song이 won-denominated stablecoins가 CBDC와 deposit tokens와 함께 미래 currency ecosystem에서 역할을 할 수 있다고 밝혔다고 보도했다. FT는 dollar-backed stablecoin trading이 2025년 1분기 57T won, $42B에 달하면서 외화유동성 부담이 커졌고, 한국이 14년간 금지했던 kimchi bond 투자를 허용해 FX imbalance 완화를 노렸다고 보도했다. 이는 R6 policy Stage2지만, 금융주 Green이 아니라 FX/liquidity 4B가 붙는 infrastructure signal이다. ([Reuters][6])

```json
{
  "case_id": "r6_loop17_bok_stablecoin_kimchi_bond_fx_policy",
  "symbols": "bank_payment_stablecoin_basket/377300/035420/086790",
  "best_trigger": "T0/T3",
  "best_trigger_type": "Stage2_policy_infrastructure_with_FX_4B",
  "stablecoin_policy_date": "2026-04-14",
  "stablecoin_trading_q1_2025_krw_trn": 57,
  "stablecoin_trading_q1_2025_usd_bn": 42,
  "kimchi_bond_ban_lifted": true,
  "kimchi_bond_ban_duration_years": 14,
  "4B_overlay": [
    "FX_liquidity_pressure",
    "won_weakness",
    "issuer_quality",
    "reserve_rules",
    "capital_flow_volatility"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "policy_stage2_with_fx_liquidity_4B"
}
```

---

## Case G — Hong Kong ELS mis-selling sanctions on banks

```text
symbols = 105560 / 055550 / 086790 / 316140
case_type = 4B consumer-protection sanction
archetype = ELS_MISSELLING_SANCTION_4B
```

| trigger |          type | date       | 당시 공개 evidence                                                                               | 가격 anchor             | outcome |
| ------- | ------------: | ---------- | -------------------------------------------------------------------------------------------- | --------------------- | ------- |
| T0      | 4B background | 2024-03    | FSS investigations into Hong Kong ELS sales misconduct                                       | no single price       |         |
| T1      |   4B sanction | 2026-02-12 | FSS to impose around 1T won in fines on local banks over Hong Kong equity-linked derivatives | no bank-price anchor  |         |
| T2      |    validation | 2026       | sanctions to be finalized by FSC; consumer-protection pressure continues                     | 4B                    |         |
| T3      |       hard 4C | N/A        | capital impairment / persistent deposit outflow not confirmed                                | hard 4C not confirmed |         |
| T4      |        relief | N/A        | final fine size, provision, compensation closure needed                                      | 보류                    |         |

Hong Kong ELS는 R6 은행 4B의 대표다. Reuters는 FSS가 Hong Kong equity-linked derivatives sales misconduct와 관련해 local banks에 약 1T won 규모 fines를 부과할 예정이라고 보도했다. 이는 대출 성장이나 value-up보다 먼저 깎아야 하는 consumer-protection risk다. 다만 final FSC approval, 각 은행별 provision, capital hit가 닫히기 전에는 hard 4C로 단정하지 않는다. ([Reuters][7])

```json
{
  "case_id": "r6_loop17_hong_kong_els_bank_sanctions",
  "symbols": "105560/055550/086790/316140",
  "best_trigger": "T1/T3",
  "best_trigger_type": "4B_bank_consumer_protection_sanction",
  "trigger_date": "2026-02-12",
  "fine_context_krw_trn": 1.0,
  "regulator": "Financial_Supervisory_Service",
  "finalization_body": "Financial_Services_Commission",
  "product": "Hong_Kong_equity_linked_derivatives",
  "4B_overlay": [
    "consumer_protection",
    "sales_practice_misconduct",
    "compensation_cost",
    "capital_buffer",
    "trust_damage"
  ],
  "hard_4C_status": "not_confirmed",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "bank_ELS_sanction_4B_not_hard_4C"
}
```

---

## Case H — Short-selling normalization / illegal short-selling detection

```text
symbols = brokerage_basket / 039490 / 016360 / 005940 / 071050
case_type = Stage2 market infrastructure + retail-volatility 4B
archetype = SHORT_SELLING_NORMALIZATION_INFRA_STAGE2_4B
```

| trigger |          type | date         | 당시 공개 evidence                                                                                   | 가격 anchor           | outcome |
| ------- | ------------: | ------------ | ------------------------------------------------------------------------------------------------ | ------------------- | ------- |
| T0      | 4B background | 2023-11~2024 | market-wide short-selling ban after illegal naked short-selling concerns                         | no price            |         |
| T1      |  Stage2 infra | 2025-02-11   | Reuters reports Korea plans to lift market-wide ban in March with illegal-trade detection system | no securities price |         |
| T2      |    validation | 2025-02-11   | Seoul court clears HSBC Hong Kong unit in nearly 16B won illegal short-selling case              | no price            |         |
| T3      |      4B-watch | 2025~        | retail backlash, volatility, foreign-flow normalization, long-short liquidity                    | 4B                  |         |
| T4      | Stage3-Yellow | N/A          | trading volume / foreign participation / securities earnings needed                              | 보류                  |         |

Short-selling normalization은 증권주에는 market infrastructure Stage2다. Reuters는 한국이 2025년 3월 market-wide short-selling ban을 해제할 계획이며, illegal trades detection system을 준비하고 있다고 보도했다. 같은 기사에서 Seoul court는 HSBC Hong Kong unit의 nearly 16B won illegal short-selling case를 무죄로 봤다. 이건 외국인 long-short liquidity 회복에는 긍정적일 수 있지만, retail backlash와 변동성 4B를 반드시 병기해야 한다. ([Reuters][8])

```json
{
  "case_id": "r6_loop17_short_selling_normalization",
  "symbols": "brokerage_basket/039490/016360/005940/071050",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2_market_infrastructure_with_retail_4B",
  "trigger_date": "2025-02-11",
  "ban_lift_target_month": "2025-03",
  "illegal_trade_detection_system": true,
  "hsbc_case_value_krw_bn": 16,
  "court_outcome": "cleared",
  "4B_overlay": [
    "retail_backlash",
    "market_volatility",
    "foreign_short_selling_sensitivity",
    "implementation_risk"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "market_infrastructure_stage2_with_volatility_4B"
}
```

---

# 6. Trigger별 실제 가격경로 검증 요약

이번 R6 Loop 17은 full OHLC가 없으므로, 아래 표는 **reported event anchor 기준**이다.

| case                          | best trigger |                                    event return / price |       market-relative | full MFE/MAE | outcome                          |
| ----------------------------- | -----------: | ------------------------------------------------------: | --------------------: | ------------ | -------------------------------- |
| KOSPI boom / securities       |           T2 | KOSPI +6.45%, securities +13.5%, financial groups +4.2% | securities outperform | unavailable  | Stage2-Actionable for brokerages |
| SK Square buyback             |           T1 |                                       price unavailable |                   N/A | unavailable  | Stage2 capital return            |
| Hana Bank / Dunamu            |           T0 |                                       price unavailable |                   N/A | unavailable  | Stage2 digital-asset stake       |
| Naver / Dunamu                |        T0/T2 |                                    Naver +7% then -4.2% |                 mixed | unavailable  | Stage2 M&A + operational 4B      |
| Kakao Pay stablecoin          |           T1 |         Kakao Pay >2x, LG CNS +70%, Aton +80%, ME2ON x3 |           speculative | unavailable  | Stage2 overheat                  |
| BOK stablecoin / kimchi bonds |        T0/T2 |                                          no stock price |                   N/A | unavailable  | policy Stage2 + FX 4B            |
| Hong Kong ELS sanctions       |           T1 |                                    no bank-price anchor |                   N/A | unavailable  | bank 4B                          |
| Short-selling normalization   |           T1 |                              no securities-price anchor |                   N/A | unavailable  | infra Stage2 + volatility 4B     |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
가장 좋은 Stage2:
1. KOSPI boom / securities firms: reported sector-index return +13.5%.
2. SK Square: buyback + cancellation + activist + holding discount.
3. Hana Bank / Dunamu: 1T won digital-asset strategic stake.
4. Naver Financial / Dunamu: 15.13T won all-stock deal, but cyber 4B.
5. Kakao Pay / stablecoin frenzy: strong price move but overheat.
```

## Stage2-Actionable entry 성과

```text
Stage2-Actionable:
- Securities firms on KOSPI boom.
- SK Square capital return.
- Naver-Dunamu if cyber/withdrawal issue is contained.
- Hana-Dunamu if regulatory approval and fee-income path are visible.

Actionable 보류:
- Kakao Pay stablecoin theme: too speculative until law/issuer/reserve rules.
- BOK kimchi bond / stablecoin policy: policy infrastructure, not company EPS.
- ELS sanctions: negative 4B.
- Short-selling normalization: infrastructure Stage2, but price anchor unavailable.
```

## Stage3-Yellow 후보

```text
Yellow 후보:
- Securities firms if transaction value, margin lending, IB/IPO and brokerage earnings confirm.
- SK Square if buyback/cancel becomes recurring and holding discount narrows.
- Hana/Dunamu if blockchain remittance or digital-asset fee income appears.
- Naver/Dunamu if regulatory approval closes and Upbit cyber risk is contained.
- Stablecoin basket if law, licensed issuers and reserve economics become clear.
```

## Stage3-Green

```text
이번 R6 Loop 17에서 확정 Green 없음.

이유:
- securities는 strong Stage2지만 market beta라 correction 4B가 크다.
- SK Square는 buyback은 좋지만 recurring capital-return and discount closure가 필요하다.
- Hana/Naver crypto exposure는 digital finance option이지만 regulation/cyber risk가 크다.
- stablecoin theme는 price action이 강하지만 speculative overheat다.
- ELS sanctions and short-selling normalization are regulatory overlays, not Green triggers.
```

---

# 8. score-price alignment 판정

```text
aligned:
- KOSPI boom / securities firms as Stage2-Actionable.
- SK Square buyback as Stage2 capital-return.
- Hana Bank / Dunamu as digital-finance Stage2.
- Naver / Dunamu as Stage2 M&A + cyber 4B.
- Kakao Pay stablecoin as speculative Stage2 / overheat.
- ELS sanction as bank 4B.
- Short-selling normalization as infra Stage2 + retail 4B.

Stage2_promote_candidate:
- securities firms after transaction-value/earnings validation.
- SK Square after recurring buyback/cancel.
- Hana/Dunamu after fee-income and approval.
- Naver/Dunamu after cyber issue containment and approval.

false_positive_score:
- banks promoted to Green just because financial groups rallied +4.2%.
- Kakao Pay/stablecoin promoted without regulation and revenue.
- Hana/Dunamu promoted without contribution to earnings.
- Naver/Dunamu promoted while Upbit abnormal withdrawal remains unresolved.
- SK Square promoted without recurring capital return.

evidence_good_but_price_failed:
- Naver/Dunamu: initial +7% but later -4.2% on Upbit abnormal withdrawal.

event_premium:
- stablecoin frenzy.
- Dunamu M&A / stake transactions.
- KOSPI brokerage beta.

thesis_break:
- none confirmed as hard stock-specific 4C in R6.
- ELS sanctions, crypto cyber, and trust/regulatory risks are strong 4B.

hard_4C:
- hard_4C_not_confirmed.
```

---

# 9. 점수비중 교정

## 올릴 축

```csv
axis,delta,reason,cases
securities_turnover_beta,+5,"KOSPI boom에서 securities index +13.5%는 직접 Stage2","KOSPI boom"
market_infrastructure_liquidity,+4,"short-selling normalization and foreign-flow liquidity can lift broker earnings","short-selling"
capital_return_cancellation,+5,"buyback + cancellation is stronger than buyback-only","SK Square"
holding_discount_closure,+4,"stake value 대비 market value discount 축소가 R6 핵심","SK Square"
digital_asset_strategic_stake,+4,"bank/fintech의 Upbit/Dunamu stake is real option value","Hana Bank, Naver"
stablecoin_policy_optionality,+4,"won-stablecoin policy can create new payment/settlement optionality","Kakao Pay, banks"
MAU_fee_income_conversion,+5,"crypto/payment theme는 실제 fee income으로 전환돼야 Yellow","Hana, Naver, Kakao Pay"
consumer_protection_risk,+5,"ELS mis-selling sanctions are bank 4B core","Big banks"
cyber_custody_risk,+5,"crypto platform abnormal withdrawal hits valuation immediately","Naver/Dunamu"
```

## 내릴 축

```csv
axis,delta,reason,cases
financials_index_without_company_trigger,-4,"financial groups +4.2%만으로 은행 Green 금지","banks"
buyback_without_cancellation,-4,"소각 없는 buyback은 효과 약함","capital return basket"
one_off_buyback_without_recurring_policy,-5,"일회성 buyback만으로 Stage3 금지","SK Square"
crypto_stake_without_earnings,-5,"Dunamu 지분이 은행 EPS에 기여하기 전 Green 금지","Hana Bank"
stablecoin_theme_without_regulation,-5,"법/준비금/인가 없는 stablecoin theme Green 금지","Kakao Pay"
cyber_incident_ignored,-5,"Upbit abnormal withdrawal 같은 custody risk 무시 금지","Naver/Dunamu"
ELS_sanction_ignored,-5,"금융소비자 보호 비용을 무시하면 bank false positive","KB/Shinhan/Hana/Woori"
short_selling_retail_backlash_ignored,-4,"short-selling 정상화는 retail backlash와 volatility 4B","brokerage basket"
```

---

# 10. Stage2-Actionable 승격 조건

R6 Loop 17 shadow rule:

```text
R6에서 Stage2 evidence가 아래 중 4개 이상이면 Stage2-Actionable로 승격한다.

1. event return or sector-index return +5% 이상
2. buyback + cancellation이 명확하다
3. holding-discount 축소 논리가 숫자로 보인다
4. digital-asset stake / M&A value가 명확하다
5. 거래대금 / fee income / brokerage activity로 연결될 수 있다
6. regulatory approval / license path가 있다
7. cyber / consumer-protection / ELS / retail-backlash 4B가 식별 가능하고 관리 가능하다
```

적용:

```text
KOSPI securities:
1,5 충족. earnings validation 필요 → Stage2-Actionable.

SK Square:
2,3,7 충족. recurring policy 필요 → Stage2-Actionable.

Hana/Dunamu:
4,6 일부, 7 식별 → Stage2.

Naver/Dunamu:
1 초기,4,6 일부,7 큼 → Stage2 + 4B.

Kakao Pay stablecoin:
1 충족, but 6 미충족 and 7 큼 → speculative Stage2 only.

BOK policy:
6 일부, but no stock EPS → policy Stage2.

ELS:
negative 4B → 승격 금지.

Short-selling:
5,6 일부 → infra Stage2, price anchor 필요.
```

---

# 11. Stage3-Yellow 조건

```text
Stage3-Yellow:
Stage2-Actionable 이후 아래 중 2개 이상이 추가로 닫히면 Yellow.

1. brokerage earnings from turnover / IB / WM confirm.
2. recurring buyback-cancel policy appears.
3. digital-asset stake contributes to fee income or remittance revenue.
4. stablecoin law passes and licensed issuers/reserve rules are clear.
5. cyber/custody event is contained.
6. ELS/sales-practice fines are provisioned and capital impact limited.
7. discount/PBR rerating continues with balance-sheet discipline.
```

Yellow 후보:

```text
Securities firms:
turnover and brokerage earnings confirm → Yellow.

SK Square:
recurring buyback + discount compression → Yellow.

Hana/Dunamu:
Dunamu stake + remittance/fee income visible → Yellow.

Naver/Dunamu:
approval + cyber resolution + revenue contribution → Yellow.

Kakao Pay:
stablecoin law + issuer license + payment revenue model → Yellow.
```

---

# 12. Stage3-Green 조건

```text
Stage3-Green:
- capital-return policy is recurring and funded by cash flow.
- digital-finance revenue is visible, not just equity stake/theme.
- stablecoin framework is passed and reserve/issuer rules are investable.
- cyber/custody/AML risk is controlled.
- ELS/consumer-protection costs are provisioned and non-recurring.
- securities turnover boom converts into recurring brokerage/IB earnings.
- full-window MFE/MAE is favorable.
```

이번 R6 Loop 17에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
reason = full OHLC unavailable + recurring capital-return / digital-revenue / regulatory-finality gates not fully closed
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- securities beta after market overheat.
- buyback not recurring.
- crypto stake without earnings contribution.
- stablecoin theme without law/reserve/issuer rules.
- cyber or abnormal withdrawal at crypto exchange.
- ELS / mis-selling sanctions.
- short-selling retail backlash.
- FX liquidity pressure from dollar stablecoin trading.
```

적용:

```text
KOSPI securities:
market beta strong, but correction 4B.

SK Square:
one-off buyback risk 4B.

Hana/Dunamu:
crypto regulation and earnings contribution 4B.

Naver/Dunamu:
Upbit abnormal withdrawal 4B.

Kakao Pay:
stablecoin overheat 4B.

BOK policy:
FX liquidity 4B.

Banks:
ELS sanctions 4B.

Short-selling:
retail backlash and volatility 4B.
```

---

# 14. 4C hard gate 조건

```text
R6 4C:
- bank capital impairment from regulatory penalties
- crypto custody failure causing unrecoverable customer loss
- stablecoin issuer collapse / reserve mismatch
- repeated mis-selling sanctions damaging funding/trust
- broker liquidity/credit event from retail leverage or market crash
```

이번 R6 Loop 17에서는 **hard stock-specific 4C 확정 없음**.

```text
hard_4c_not_confirmed = true
strong_4c_watch = [
  "Upbit abnormal withdrawal if not contained",
  "ELS fines if bank capital/earnings materially impaired",
  "stablecoin issuer rule failure",
  "brokerage margin-loan correction",
  "short-selling retail backlash"
]
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

R6 production 설계 원칙:

```text
1. 금융주 value-up과 실제 capital return을 분리한다.
2. buyback은 cancellation 여부를 반드시 따로 본다.
3. 증권주는 KOSPI beta와 실제 brokerage earnings를 분리한다.
4. stablecoin/crypto theme는 regulation, reserve, cyber, AML gate 전까지 Green 금지한다.
5. Dunamu/Upbit exposure는 stake value와 earnings contribution을 분리한다.
6. ELS/sales-practice penalties는 bank 4B로 선차감한다.
7. short-selling normalization은 liquidity Stage2지만 retail backlash 4B를 병기한다.
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_255.md 요약

```md
# R6 Loop 17. Financials / Capital Allocation / Digital Finance Trigger-level Price Validation

이번 라운드는 R6 Loop 17 trigger-level validation 라운드다.

핵심 결론:
- KOSPI boom / securities firms is the cleanest R6 Stage2-Actionable. On May 6, 2026, KOSPI closed +6.45%, securities firms jumped 13.5%, and financial groups rose 4.2%. Securities are direct turnover/fee beta, but banks are not Green from index move alone.
- SK Square buyback/cancellation is Stage2-Actionable capital allocation. It planned to cancel 100B won of previously bought shares and buy back/cancel another 100B won, while trading at less than half the value of its SK Hynix stake.
- Hana Bank / Dunamu is Stage2 digital-asset strategic stake. Hana Bank will buy a 6.55% Dunamu stake for 1T won / about $700M; Upbit handles more than 80% of Korea's virtual-asset volume.
- Naver Financial / Dunamu is Stage2 fintech M&A with cyber/operational 4B. The all-stock deal is worth 15.13T won / $10.27B; Naver initially rose more than 7% but later fell 4.2% after Upbit reported a 54B won abnormal withdrawal.
- Kakao Pay / won-stablecoin frenzy is speculative Stage2 / overheat. Kakao Pay more than doubled in June 2025, LG CNS rose almost 70%, Aton +80%, and ME2ON tripled. Law, reserve and issuer rules are missing.
- BOK stablecoin / kimchi bond policy is Stage2 infrastructure with FX 4B. BOK governor nominee supported won-stablecoins coexisting with CBDC/deposit tokens; dollar-stablecoin trading hit 57T won / $42B in Q1 2025; Korea lifted a 14-year kimchi bond ban.
- Hong Kong ELS bank sanctions are 4B. FSS planned around 1T won in fines on local banks over Hong Kong equity-linked derivatives misconduct.
- Short-selling normalization is Stage2 market infrastructure with retail-volatility 4B. Korea planned to lift the market-wide ban in March 2025 with an illegal-trade detection system.

Main calibration:
- Raise securities_turnover_beta, market_infrastructure_liquidity, capital_return_cancellation, holding_discount_closure, digital_asset_strategic_stake, stablecoin_policy_optionality, MAU_fee_income_conversion, consumer_protection_risk, cyber_custody_risk.
- Lower financials_index_without_company_trigger, buyback_without_cancellation, one_off_buyback_without_recurring_policy, crypto_stake_without_earnings, stablecoin_theme_without_regulation, cyber_incident_ignored, ELS_sanction_ignored, short_selling_retail_backlash_ignored.
```

## docs/checkpoints/checkpoint_28a_round255_r6_loop17.md 요약

```md
# Checkpoint 28A Round 255 R6 Loop 17 Trigger-level Calibration

## 반영 내용
- R6 Loop 17 trigger-level validation을 수행했다.
- KOSPI securities beta, SK Square capital return, Hana Bank/Dunamu, Naver Financial/Dunamu, Kakao Pay stablecoin frenzy, BOK stablecoin/kimchi bond policy, Hong Kong ELS sanctions, short-selling normalization을 검토했다.
- full adjusted OHLC는 확보하지 못했으므로 Reuters / FT / WSJ reported event return과 event price anchor를 사용했다.
- MFE/MAE는 조작하지 않고 price_data_unavailable_after_deep_search로 분리했다.

## 핵심 보정
- Securities firms can be Stage2-Actionable when index/turnover beta is explicit.
- Financial groups/banks are not Green from sector beta alone.
- Buyback must be separated from buyback-plus-cancellation.
- Crypto/stablecoin themes require regulatory clarity, reserve rules, cyber controls and earnings contribution before Yellow/Green.
- ELS and mis-selling sanctions are bank 4B.
- Short-selling normalization is infrastructure Stage2 but retail backlash and volatility remain 4B.
```

## data/e2r_case_library/cases_r6_loop17_round255.jsonl 초안

```jsonl
{"case_id":"r6_loop17_kospi_boom_securities_financials","symbol":"039490/005940/016360/071050/105560/055550/086790/316140","company_name":"Korea securities and financial groups basket","case_type":"Stage2_Actionable_brokerage_beta_with_market_4B","primary_archetype":"KOSPI_BOOM_SECURITIES_STAGE2_ACTIONABLE","best_trigger":"T2/T3","stage_candidate":"Stage2-Actionable for brokerages","price_validation":{"trigger_date":"2026-05-06","kospi_event_return_pct":6.45,"securities_firms_index_event_return_pct":13.5,"financial_groups_index_event_return_pct":4.2,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_actionable_for_securities_not_bank_green","notes":"Securities beta is clear; financial groups require bank-specific capital return and earnings validation."}
{"case_id":"r6_loop17_sk_square_buyback_holding_discount","symbol":"402340","company_name":"SK Square","case_type":"Stage2_Actionable_capital_return_holding_discount","primary_archetype":"VALUE_UP_CAPITAL_RETURN_HOLDCO_STAGE2_ACTIONABLE","best_trigger":"T1/T3","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2024-11-21","prior_buyback_cancel_krw_bn":100,"new_buyback_cancel_krw_bn":100,"sk_hynix_stake_value_context_usd_bn":18,"market_value_vs_stake_value_context":"less_than_half","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"capital_return_stage2_actionable_no_ohlc","notes":"Buyback plus cancellation and holding discount are strong, but recurring capital return is needed for Yellow."}
{"case_id":"r6_loop17_hana_bank_dunamu_stake","symbol":"086790/Dunamu_private/035720_seller_readthrough","company_name":"Hana Bank / Dunamu / Kakao Investment","case_type":"Stage2_bank_crypto_exchange_strategic_stake","primary_archetype":"BANK_CRYPTO_EXCHANGE_STRATEGIC_STAKE_STAGE2","best_trigger":"T0/T3","stage_candidate":"Stage2","price_validation":{"trigger_date":"2026-05-14","deal_value_krw_trn":1.0,"deal_value_usd_mn":700,"hana_bank_dunamu_stake_pct":6.55,"upbit_korea_virtual_asset_volume_share_pct":">80","kakao_investment_post_sale_stake_pct":4.03,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_digital_asset_stake_no_direct_price","notes":"Strategic crypto exposure is real; earnings contribution and regulation are gates."}
{"case_id":"r6_loop17_naver_financial_dunamu_merger","symbol":"035420/Dunamu_private/Naver_Financial_private","company_name":"Naver Financial / Dunamu / Upbit","case_type":"Stage2_fintech_crypto_MA_with_cyber_4B","primary_archetype":"FINTECH_CRYPTO_EXCHANGE_MA_STAGE2_WITH_CYBER_4B","best_trigger":"T0/T3","stage_candidate":"Stage2 + 4B-watch","price_validation":{"trigger_date":"2025-11-27","deal_value_krw_trn":15.13,"deal_value_usd_bn":10.27,"exchange_ratio":"2.54_Naver_Financial_shares_per_1_Dunamu_share","naver_initial_event_return_pct":">7","naver_later_event_return_pct":-4.2,"upbit_abnormal_withdrawal_krw_bn":54,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_fintech_MA_with_operational_4B","notes":"Digital finance M&A is strong, but abnormal withdrawal/cyber and approval risks are immediate 4B."}
{"case_id":"r6_loop17_kakao_pay_won_stablecoin_frenzy","symbol":"377300/012510/158430/201490","company_name":"Kakao Pay / LG CNS / Aton / ME2ON","case_type":"Stage2_speculative_won_stablecoin_theme_with_overheat_4B","primary_archetype":"WON_STABLECOIN_RETAIL_FRENZY_STAGE2_OVERHEAT","best_trigger":"T1/T3","stage_candidate":"speculative Stage2","price_validation":{"trigger_period":"2025-06","kakao_pay_event_return_context":">2x","lg_cns_event_return_context_pct":"almost_70","aton_event_return_context_pct":80,"me2on_event_return_context":"tripled","margin_loans_context_krw_trn":20.5,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_speculative_overheat_not_Green","notes":"Stablecoin theme moved stocks strongly, but law, reserve rules and issuer quality are missing."}
{"case_id":"r6_loop17_bok_stablecoin_kimchi_bond_fx_policy","symbol":"bank_payment_stablecoin_basket/377300/035420/086790","company_name":"BOK / bank-payment stablecoin basket","case_type":"Stage2_policy_infrastructure_with_FX_4B","primary_archetype":"BANK_STABLECOIN_POLICY_STAGE2_WITH_FX_4B","best_trigger":"T0/T3","stage_candidate":"policy Stage2","price_validation":{"stablecoin_policy_date":"2026-04-14","stablecoin_trading_q1_2025_krw_trn":57,"stablecoin_trading_q1_2025_usd_bn":42,"kimchi_bond_ban_lifted":true,"kimchi_bond_ban_duration_years":14,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"policy_stage2_with_fx_liquidity_4B","notes":"Stablecoin policy infrastructure is real, but FX liquidity and issuer/reserve rules remain 4B."}
{"case_id":"r6_loop17_hong_kong_els_bank_sanctions","symbol":"105560/055550/086790/316140","company_name":"KB / Shinhan / Hana / Woori financial groups","case_type":"4B_bank_consumer_protection_sanction","primary_archetype":"ELS_MISSELLING_SANCTION_4B","best_trigger":"T1/T3","stage_candidate":"4B-watch","price_validation":{"trigger_date":"2026-02-12","fine_context_krw_trn":1.0,"regulator":"Financial_Supervisory_Service","finalization_body":"Financial_Services_Commission","product":"Hong_Kong_equity_linked_derivatives","hard_4C_status":"not_confirmed","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"bank_ELS_sanction_4B_not_hard_4C","notes":"Consumer-protection penalties must be deducted before bank value-up scoring."}
{"case_id":"r6_loop17_short_selling_normalization","symbol":"brokerage_basket/039490/016360/005940/071050","company_name":"Korea brokerage basket","case_type":"Stage2_market_infrastructure_with_retail_4B","primary_archetype":"SHORT_SELLING_NORMALIZATION_INFRA_STAGE2_4B","best_trigger":"T1/T3","stage_candidate":"Stage2 infrastructure","price_validation":{"trigger_date":"2025-02-11","ban_lift_target_month":"2025-03","illegal_trade_detection_system":true,"hsbc_case_value_krw_bn":16,"court_outcome":"cleared","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"market_infrastructure_stage2_with_volatility_4B","notes":"Short-selling normalization can improve market liquidity, but retail backlash and volatility remain 4B."}
```

## data/e2r_trigger_calibration/triggers_r6_loop17_round255.jsonl 초안

```jsonl
{"trigger_id":"r6l17_kospi_securities_T2","case_id":"r6_loop17_kospi_boom_securities_financials","trigger_type":"Stage2-Actionable_brokerage_beta","trigger_date":"2026-05-06","event_return_pct":"securities_index_+13.5_financial_groups_+4.2_kospi_+6.45","trigger_outcome_label":"excellent_stage2_actionable_for_brokerage_beta","promote_to":"Stage2-Actionable"}
{"trigger_id":"r6l17_sk_square_buyback_T1","case_id":"r6_loop17_sk_square_buyback_holding_discount","trigger_type":"Stage2-Actionable_capital_return","trigger_date":"2024-11-21","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"buyback_cancellation_holding_discount_stage2","promote_to":"Stage2-Actionable"}
{"trigger_id":"r6l17_hana_dunamu_T0","case_id":"r6_loop17_hana_bank_dunamu_stake","trigger_type":"Stage2_bank_crypto_exchange_stake","trigger_date":"2026-05-14","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"digital_asset_stake_stage2_no_price","promote_to":"Stage2"}
{"trigger_id":"r6l17_naver_dunamu_T0","case_id":"r6_loop17_naver_financial_dunamu_merger","trigger_type":"Stage2_fintech_crypto_MA","trigger_date":"2025-11-27","event_return_pct":"Naver_initial_+7_then_-4.2","trigger_outcome_label":"Stage2_MA_with_cyber_4B","promote_to":"Stage2+4B"}
{"trigger_id":"r6l17_upbit_withdrawal_T2","case_id":"r6_loop17_naver_financial_dunamu_merger","trigger_type":"4B_crypto_custody_operational","trigger_date":"2025-11-27","event_return_pct":-4.2,"trigger_outcome_label":"abnormal_withdrawal_4B","promote_to":"4B-watch"}
{"trigger_id":"r6l17_kakao_pay_stablecoin_T1","case_id":"r6_loop17_kakao_pay_won_stablecoin_frenzy","trigger_type":"Stage2_speculative_stablecoin_theme","trigger_date":"2025-06","event_return_pct":"KakaoPay_>2x_LGCNS_+70_Aton_+80_ME2ON_tripled","trigger_outcome_label":"speculative_stage2_overheat","promote_to":"Stage2_overheat"}
{"trigger_id":"r6l17_bok_stablecoin_policy_T0","case_id":"r6_loop17_bok_stablecoin_kimchi_bond_fx_policy","trigger_type":"Stage2_policy_infrastructure","trigger_date":"2026-04-14","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"stablecoin_policy_stage2_fx_4B","promote_to":"Stage2"}
{"trigger_id":"r6l17_kimchi_bond_T2","case_id":"r6_loop17_bok_stablecoin_kimchi_bond_fx_policy","trigger_type":"Stage2_FX_liquidity_policy","trigger_date":"2025-06-30","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"kimchi_bond_fx_liquidity_stage2","promote_to":"Stage2"}
{"trigger_id":"r6l17_els_sanction_T1","case_id":"r6_loop17_hong_kong_els_bank_sanctions","trigger_type":"4B_consumer_protection_sanction","trigger_date":"2026-02-12","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"bank_ELS_sanction_4B","promote_to":"4B-watch"}
{"trigger_id":"r6l17_short_selling_normalization_T1","case_id":"r6_loop17_short_selling_normalization","trigger_type":"Stage2_market_infrastructure","trigger_date":"2025-02-11","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"short_selling_normalization_stage2_with_retail_4B","promote_to":"Stage2"}
```

## data/sector_taxonomy/score_weight_profiles_round255_r6_loop17_v1.csv 초안

```csv
archetype,securities_turnover_beta,market_infrastructure_liquidity,capital_return_cancellation,holding_discount_closure,digital_asset_strategic_stake,stablecoin_policy_optionality,MAU_fee_income_conversion,consumer_protection_risk,cyber_custody_risk,financials_index_without_company_trigger_penalty,buyback_without_cancellation_penalty,crypto_stake_without_earnings_penalty,stablecoin_theme_without_regulation_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
KOSPI_BOOM_SECURITIES_STAGE2_ACTIONABLE,+5,+4,+0,+0,+0,+0,+3,+1,+1,-4,-1,-1,-1,securities index +13.5,banks not green from index beta,brokerage earnings confirmation,KOSPI securities.
VALUE_UP_CAPITAL_RETURN_HOLDCO_STAGE2_ACTIONABLE,+1,+1,+5,+5,+0,+0,+0,+0,+0,-2,-4,-1,-1,buyback+cancel+holding discount,recurring policy missing,recurring buyback+discount compression,SK Square.
BANK_CRYPTO_EXCHANGE_STRATEGIC_STAKE_STAGE2,+0,+1,+0,+1,+5,+3,+5,+2,+4,-1,-1,-5,-3,Hana 6.55% Dunamu stake,earnings contribution missing,fee income/remittance revenue,Hana Bank.
FINTECH_CRYPTO_EXCHANGE_MA_STAGE2_WITH_CYBER_4B,+0,+2,+0,+0,+5,+4,+5,+3,+5,-1,-1,-4,-3,Naver-Dunamu large M&A,abnormal withdrawal 4B,approval+cyber containment+revenue,Naver.
WON_STABLECOIN_RETAIL_FRENZY_STAGE2_OVERHEAT,+1,+2,+0,+0,+2,+5,+3,+2,+3,-1,-1,-3,-5,stablecoin stock frenzy,regulation missing,law+reserve rules+issuer license,Kakao Pay.
BANK_STABLECOIN_POLICY_STAGE2_WITH_FX_4B,+0,+4,+0,+0,+2,+5,+2,+2,+2,-1,-1,-2,-5,BOK stablecoin stance and kimchi bonds,FX liquidity 4B,licensed issuers+bank revenue model,BOK policy basket.
ELS_MISSELLING_SANCTION_4B,+0,+0,+0,+0,+0,+0,+0,+5,+1,-1,-1,-1,-1,ELS sanctions hurt bank trust/capital,final provision missing,fine/provision closure,big banks.
SHORT_SELLING_NORMALIZATION_INFRA_STAGE2_4B,+4,+5,+0,+0,+0,+0,+2,+1,+0,-1,-1,-1,-1,short-selling normalization supports liquidity,retail backlash 4B,turnover+broker earnings+stable implementation,brokerage basket.
```

---

# 이번 R6 Loop 17 결론

```text
1. KOSPI boom / securities firms는 R6의 가장 좋은 Stage2-Actionable이다.
   KOSPI +6.45%, securities +13.5%라서 증권주 beta는 닫혔다. 단, financial groups +4.2%는 KOSPI를 못 이겼으므로 은행 Green은 아니다.

2. SK Square는 capital-return Stage2-Actionable이다.
   100B won 소각 + 100B won 신규 buyback/cancel + holding discount가 닫혔다.

3. Hana Bank / Dunamu는 bank-to-crypto Stage2다.
   1T won, 6.55%, Upbit >80% volume은 강하지만 은행 EPS contribution은 아직 없다.

4. Naver Financial / Dunamu는 Stage2 M&A + cyber 4B다.
   15.13T won deal은 강하지만, Upbit 54B won abnormal withdrawal에 Naver가 +7%에서 -4.2%로 꺾였다.

5. Kakao Pay / won-stablecoin은 speculative Stage2 overheat다.
   Kakao Pay >2x, LG CNS +70%, Aton +80%, ME2ON x3였지만 법/준비금/issuer rule 전에는 Green 금지다.

6. BOK stablecoin / kimchi bond policy는 Stage2 infrastructure다.
   stablecoin 제도화 가능성은 있지만 FX liquidity와 issuer-quality 4B가 크다.

7. Hong Kong ELS sanctions는 bank 4B다.
   소비자보호/판매관행 비용은 bank value-up score에서 선차감해야 한다.

8. Short-selling normalization은 market-infra Stage2다.
   증권 거래유동성에는 긍정적이지만 retail backlash와 volatility 4B가 붙는다.
```

한 문장으로 압축하면:

> **R6 Loop 17에서 배운 핵심은 “금융주 value-up·증권주 beta·stablecoin·crypto M&A headline”이 아니라, buyback cancellation, recurring capital return, brokerage earnings, fee-income conversion, regulatory finality, cyber custody, ELS consumer-protection cost가 닫혀야 Stage3로 올릴 수 있다는 것이다. 반대로 sector index 상승, 일회성 buyback, crypto stake, stablecoin theme만으로 Green을 주면 규제·사이버·ELS·시장과열 4B에 false positive가 난다.**

다음 순서는 **R7 Loop 17 — 바이오·헬스케어·의료기기**다.

[1]: https://www.reuters.com/world/asia-pacific/south-koreas-kospi-share-index-tops-7000-first-time-2026-05-06/ "https://www.reuters.com/world/asia-pacific/south-koreas-kospi-share-index-tops-7000-first-time-2026-05-06/"
[2]: https://www.reuters.com/technology/artificial-intelligence/south-koreas-ai-chip-investor-announces-plan-share-buybacks-2024-11-21/ "https://www.reuters.com/technology/artificial-intelligence/south-koreas-ai-chip-investor-announces-plan-share-buybacks-2024-11-21/"
[3]: https://www.reuters.com/world/asia-pacific/hana-bank-acquire-stake-dunamu-700-mln-filing-says-2026-05-14/ "https://www.reuters.com/world/asia-pacific/hana-bank-acquire-stake-dunamu-700-mln-filing-says-2026-05-14/"
[4]: https://www.reuters.com/world/asia-pacific/navers-payment-arm-acquire-south-korean-crypto-exchange-operator-10-bln-deal-2025-11-27/ "https://www.reuters.com/world/asia-pacific/navers-payment-arm-acquire-south-korean-crypto-exchange-operator-10-bln-deal-2025-11-27/"
[5]: https://www.ft.com/content/4b19bf90-4202-4fe7-8caf-d7db6deeb768 "https://www.ft.com/content/4b19bf90-4202-4fe7-8caf-d7db6deeb768"
[6]: https://www.reuters.com/world/asia-pacific/bank-korea-governor-nominee-positive-about-won-denominated-stablecoins-2026-04-14/ "https://www.reuters.com/world/asia-pacific/bank-korea-governor-nominee-positive-about-won-denominated-stablecoins-2026-04-14/"
[7]: https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-impose-sanctions-banks-over-sales-hong-kong-equity-linked-2026-02-12/ "https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-impose-sanctions-banks-over-sales-hong-kong-equity-linked-2026-02-12/"
[8]: https://www.reuters.com/business/finance/south-korean-court-clears-hsbc-charges-violating-short-selling-rules-yonhap-2025-02-11/ "https://www.reuters.com/business/finance/south-korean-court-clears-hsbc-charges-violating-short-selling-rules-yonhap-2025-02-11/"

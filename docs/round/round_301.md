순서상 이번은 **R6 Loop 15 — 금융·자본배분·디지털금융 trigger-level price validation 라운드**다.

이번 R6의 핵심은 “은행/증권/핀테크/주주환원 좋다”가 아니라, **자본시장 호황, 배당·자사주, Value-Up, 디지털자산 M&A, stablecoin 정책, 보안/규제 리스크 중 어느 trigger가 실제 entry였고, 어느 trigger가 4B/4C였는지**를 분리하는 것이다.

```text
round = R6 Loop 15
round_id = round_229
large_sector = FINANCIALS_CAPITAL_ALLOCATION_DIGITAL_FINANCE
method = trigger_level_backtest_v1
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R7 Loop 15
```

이번에도 KRX/Naver/Yahoo/Stooq의 수정주가 일봉 OHLC 30D/90D/180D/1Y window를 안정적으로 직접 추출하지 못했다. 그래서 full MFE/MAE는 `price_data_unavailable_after_deep_search`로 두고, Reuters/FT/WSJ/MarketWatch의 **reported event return, event price, buyback amount, deal value, data-breach amount, sector index return, market-relative return**을 trigger anchor로 쓴다. 단, **OHLC 미확보를 이유로 Stage 후보 자체를 강등하지 않는다.**

---

# 1. 이번 라운드 대섹터

```text
R6 = 금융·자본배분·디지털금융
```

R6의 핵심 gate는 아래다.

```text
은행/금융지주:
CET1 → 배당/자사주 소각 → ROE → 대손비용 → NIM → 자본비율 → 총주주환원율

증권:
KOSPI rally → 거래대금 → 신용융자/IB 수수료 → 브로커리지 이익 → PF/부동산 리스크 → valuation

보험:
금리/자산가격 → CSM/자본비율 → 배당여력 → 계열사 지분가치 → RBC/K-ICS risk

자본배분:
buyback announcement → 실제 매입 → 소각 → EPS accretion → business recovery

디지털금융:
crypto exchange stake / M&A → 거래대금 → regulatory approval → security → stablecoin law → monetization

핀테크/플랫폼:
payment MAU → take-rate → data rights → regulatory approval → security / privacy → financial crime risk
```

---

# 2. 대상 canonical archetype

```text
BROKERAGE_MARKET_VOLUME_STAGE2_ACTIONABLE
FINANCIAL_GROUP_VALUEUP_STAGE2
BUYBACK_CAPITAL_ALLOCATION_STAGE2_ACTIONABLE
HOLDCO_DISCOUNT_ACTIVIST_STAGE2
DIGITAL_ASSET_BANK_ENTRY_STAGE2
CRYPTO_EXCHANGE_MA_STAGE2_WITH_SECURITY_4C
STABLECOIN_POLICY_4B_OVERHEAT
FINTECH_DATA_GOVERNANCE_4C
KAKAO_BANK_CONTROL_REGULATORY_4C
```

---

# 3. deep sub-archetype

```text
증권/브로커리지:
- Samsung Securities / Kiwoom / Mirae / NH Investment / Korea Investment read-through
- KOSPI 7,000 돌파
- securities firms +13.5%
- financial groups +4.2%
- foreign record purchase 3.1T won
- trading-value / brokerage earnings gate

금융지주 Value-Up:
- KB / Shinhan / Hana / Woori
- Korea discount
- corporate governance reform
- dividend tax / board fiduciary duty
- capital return vs actual CET1 / buyback execution

자본배분:
- Samsung Electronics 10T won buyback
- SK Square 100B cancellation + 100B buyback
- buyback announcement vs cancellation / underlying business

디지털자산:
- Hana Bank / Dunamu
- Naver Financial / Dunamu
- Upbit market share 70~80%+
- stablecoin policy rally
- data/security / abnormal withdrawal / customer trust

핀테크/규제:
- Kakao Pay stablecoin frenzy
- Kakao founder indictment / KakaoBank ownership risk
- payment data / Alipay / financial crime ownership restriction
```

---

# 4. 선정 case 요약

| bucket              | case                              | 핵심 판정                                                                                              |
| ------------------- | --------------------------------- | -------------------------------------------------------------------------------------------------- |
| Stage2-Actionable   | Securities / brokerage basket     | KOSPI 7,000 돌파일 securities +13.5%, financial groups +4.2%. 거래대금·브로커리지 이익 확인 전 Green 아님             |
| Stage2 정책           | Financial groups / Value-Up       | governance reform·Korea discount 해소 기대. 단 bank별 CET1/ROE/주주환원 execution 필요                         |
| Stage2-Actionable   | Samsung buyback                   | 10T won buyback, 3T won immediate cancellation, 주가 +7.2%. 자본배분 trigger지만 business recovery gate 남음 |
| Stage2-Actionable   | SK Square activist / buyback      | 100B won cancellation + 100B buyback, Palliser, SK Hynix stake discount. 가격자료 미흡                   |
| Stage2 digital bank | Hana Bank / Dunamu stake          | 1T won, 6.55%, Upbit >80% volume. 디지털자산 진입 trigger지만 regulatory/crypto-cycle gate                  |
| Stage2 + 4C-watch   | Naver Financial / Dunamu          | 15.13T won all-stock deal, Naver +7% 후 -4.2%, Upbit 54B won abnormal withdrawal                    |
| 4B-overheat         | Stablecoin policy / Kakao Pay     | Kakao Pay 한 달 2배+, LG CNS +70%, Aton +80%, ME2ON 3배. policy hype + leverage 과열                     |
| 4C-watch            | Kakao founder / KakaoBank control | founder indictment/arrest, KakaoBank ownership risk, Kakao -4.6% after arrest source               |

---

# 5. Case별 trigger grid

## Case A — 증권·브로커리지 basket / KOSPI liquidity boom

```text
symbols = 016360 / 039490 / 005940 / 006800 / brokerage_basket
company_scope = Samsung Securities / Kiwoom Securities / NH Investment / Mirae Asset / Korea Investment read-through
case_type = Stage2-Actionable
archetype = BROKERAGE_MARKET_VOLUME_STAGE2_ACTIONABLE
```

### Trigger grid

| trigger | type                    |       date | 당시 공개 evidence                                                                     | 가격 anchor                                               | outcome           |
| ------- | ----------------------- | ---------: | ---------------------------------------------------------------------------------- | ------------------------------------------------------- | ----------------- |
| T0      | awareness               |  2025~2026 | Korea market re-rating, AI rally, governance reform                                | KOSPI multi-year rally                                  | Stage1            |
| T1      | Stage2 evidence         | 2026-05-06 | KOSPI first crosses 7,000; record foreign buying 3.1T won                          | KOSPI +6.45%, securities +13.5%, financial groups +4.2% | Stage2-Actionable |
| T2      | Stage3-Yellow candidate | 2026-05-06 | securities earnings could rise from trading volume / margin finance / IB activity  | no company OHLC                                         | Yellow candidate  |
| T3      | 4B-watch                | 2026-05-06 | KOSPI sidecar, AI-led concentration, possible fall to 4,500 if AI demand collapses | no full OHLC                                            | 4B                |
| T4      | Stage3-Green            |        N/A | brokerage net profit / trading value / credit balance not confirmed                | N/A                                                     | no Green          |

2026년 5월 6일은 R6에서 가장 강한 시장유동성 trigger다. Reuters는 KOSPI가 처음 7,000을 넘었고, 외국인이 하루 3.1T won을 순매수했으며, securities firms index가 +13.5%, financial groups index가 +4.2% 올랐다고 보도했다. 이건 단순 “증시 좋다”가 아니라 증권주 입장에서는 **거래대금·브로커리지·신용융자·IB수수료 기대가 동시에 붙는 Stage2-Actionable**이다. 다만 실제 거래대금과 증권사 순이익이 확인되기 전에는 Green이 아니다. ([Reuters][1])

### Trigger price validation row

```json
{
  "case_id": "r6_loop15_brokerage_kospi_liquidity_boom",
  "symbols": "016360/039490/005940/006800/brokerage_basket",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable_to_Stage3-Yellow_candidate",
  "trigger_date": "2026-05-06",
  "kospi_close_return_pct": 6.45,
  "kospi_intraday_high_return_pct": 7.06,
  "kospi_close": 7384.56,
  "foreign_net_buying_krw_trn": 3.1,
  "foreign_net_buying_usd_bn": 2.13,
  "securities_firms_index_return_pct": 13.5,
  "financial_groups_index_return_pct": 4.2,
  "stage3_gate_missing": [
    "daily_trading_value",
    "brokerage_commission_revenue",
    "margin_finance_balance",
    "IB_fee_income",
    "PF_risk_absorption"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_Actionable_liquidity_brokerage"
}
```

### 판정

```text
score_price_alignment = Stage2_promote_candidate
new_rule = securities index +13.5% 같은 시장유동성 trigger는 Stage2-Actionable
but = 거래대금/브로커리지 이익 확인 전 Green 금지
```

---

## Case B — 금융지주 / Value-Up reform basket

```text
symbols = 105560 / 055550 / 086790 / 316140
company_scope = KB Financial / Shinhan Financial / Hana Financial / Woori Financial
case_type = Stage2 policy / success_candidate
archetype = FINANCIAL_GROUP_VALUEUP_STAGE2
```

### Trigger grid

| trigger | type                        |       date | 당시 공개 evidence                                                                                | 가격 anchor                                          | outcome   |
| ------- | --------------------------- | ---------: | --------------------------------------------------------------------------------------------- | -------------------------------------------------- | --------- |
| T0      | awareness                   |    2024-02 | Corporate Value-Up programme announced; Korea discount / low dividends problem                | financial/auto sectors rallied but details limited | Stage1    |
| T1      | Stage2 evidence             | 2024-02-28 | FSS considers penalties / delisting for firms failing shareholder-return criteria             | no bank-specific price                             | Stage2    |
| T2      | Stage2-Actionable candidate |  2025~2026 | corporate governance reform, fiduciary duty, dividend tax incentives support market re-rating | broad market rerating                              | Stage2    |
| T3      | Stage3-Yellow               |        N/A | bank별 CET1, payout, buyback/cancellation, ROE 확인 필요                                           | unavailable                                        | no Yellow |
| T4      | 4B-watch                    |  2025~2026 | reform euphoria without bank-specific execution                                               | no direct                                          | watch     |

Value-Up은 R6 금융지주의 broad trigger다. Reuters는 2024년 2월 FSS가 shareholder-return 기준 미충족 기업에 대해 장기적으로 제재나 상장폐지 가능성까지 논의하고 있다고 보도했다. 이건 은행·보험·지주사의 주주환원 기대를 키우는 Stage2 policy trigger다. 다만 bank별 CET1, payout, buyback cancellation, 대손비용, ROE가 없으면 Stage3로 올리면 안 된다. ([Reuters][2])

FT는 이후 한국 증시의 강세 배경으로 AI뿐 아니라 corporate governance reform, dividend tax incentives, director fiduciary duty 변화 등을 짚었다. 즉 Value-Up은 “R6 전체 beta”로는 의미가 있지만, bank별 trigger에는 **자본비율과 실제 환원 execution**을 붙여야 한다. ([Financial Times][3])

### Trigger price validation row

```json
{
  "case_id": "r6_loop15_financial_group_valueup_basket",
  "symbols": "105560/055550/086790/316140",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2_policy_success_candidate",
  "trigger_date": "2024-02-28",
  "policy_trigger": "Corporate Value-Up / shareholder-return penalties under discussion",
  "possible_penalties": [
    "shareholder_return_criteria_penalty",
    "possible_delisting_for_non_compliance"
  ],
  "broad_market_support": [
    "corporate_governance_reform",
    "dividend_tax_incentives",
    "director_fiduciary_duty_discussion"
  ],
  "bank_specific_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "CET1_ratio",
    "payout_ratio",
    "buyback_cancellation",
    "ROE",
    "NIM",
    "credit_cost"
  ],
  "trigger_outcome_label": "Stage2_policy_not_Green"
}
```

### 판정

```text
score_price_alignment = success_candidate_stage2
new_rule = Value-Up 정책은 bank beta를 올리는 Stage2
but = 은행별 CET1/ROE/환원 execution 없으면 Yellow/Green 금지
```

---

## Case C — Samsung Electronics buyback as capital allocation trigger

```text
symbol = 005930
case_type = Stage2-Actionable / evidence_good_but_business_gate
archetype = BUYBACK_CAPITAL_ALLOCATION_STAGE2_ACTIONABLE
```

### Trigger grid

| trigger | type                    |       date | 당시 공개 evidence                                                         | 가격 anchor           | outcome                      |
| ------- | ----------------------- | ---------: | ---------------------------------------------------------------------- | ------------------- | ---------------------------- |
| T0      | 4C context              |    2024-11 | Samsung stock at four-year lows, down 32% YTD, HBM/Nvidia lag          | depressed valuation | context                      |
| T1      | Stage2 evidence         | 2024-11-15 | 10T won / $7.17B one-year buyback announced                            | Samsung +7.2%       | Stage2-Actionable            |
| T2      | Stage2-Actionable       | 2024-11-15 | immediate 3T won repurchase and cancellation, first buyback since 2017 | same                | Actionable                   |
| T3      | 4B/false-positive watch |    2024-11 | analysts say concrete business plans needed; buyback partly defensive  | no full OHLC        | watch                        |
| T4      | Stage3-Yellow           |        N/A | HBM recovery / OP trajectory needed                                    | N/A                 | no Yellow from buyback alone |

삼성전자 buyback은 R6 자본배분에서 좋은 calibration이다. Reuters는 삼성전자가 10T won 규모의 1년 buyback을 발표했고, 그중 3T won은 3개월 내 매입·소각한다고 보도했다. 주가는 당일 +7.2%로 2020년 3월 이후 최대 일일 상승을 기록했다. 이건 **Stage2-Actionable capital allocation trigger**다. ([Reuters][4])

하지만 Reuters는 동시에 삼성 주가가 여전히 YTD -32%였고, AI/HBM에서 SK Hynix 대비 뒤처진 문제가 있었으며, 장기 회복에는 구체적인 사업계획이 필요하다는 analyst view도 전했다. 그래서 buyback alone은 Green이 아니라, 사업 회복 gate와 붙어야 한다. ([Reuters][4])

### Trigger price validation row

```json
{
  "case_id": "r6_loop15_samsung_buyback_capital_allocation",
  "symbol": "005930",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable",
  "trigger_date": "2024-11-15",
  "buyback_total_krw_trn": 10,
  "buyback_total_usd_bn": 7.17,
  "immediate_buyback_cancel_krw_trn": 3,
  "first_buyback_since": 2017,
  "event_return_pct": 7.2,
  "ytd_pre_event_return_pct": -32,
  "stage3_gate_missing": [
    "HBM_competitiveness_recovery",
    "Nvidia_qualification",
    "foundry_loss_reduction",
    "sustained_OP_recovery",
    "remaining_7T_execution"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_Actionable_buyback_not_business_Green"
}
```

### 판정

```text
score_price_alignment = Stage2_promote_candidate
new_rule = buyback + cancellation + depressed valuation은 Stage2-Actionable
but = 사업 회복 없이 Green 금지
```

---

## Case D — SK Square / activist + buyback + holding-company discount

```text
symbol = 402340
case_type = Stage2-Actionable / holdco discount
archetype = HOLDCO_DISCOUNT_ACTIVIST_STAGE2
```

### Trigger grid

| trigger | type              |                                              date | 당시 공개 evidence                                                                                            | 가격 anchor       | outcome           |
| ------- | ----------------- | ------------------------------------------------: | --------------------------------------------------------------------------------------------------------- | --------------- | ----------------- |
| T0      | awareness         |                                              2024 | SK Square discount vs SK Hynix stake; Palliser activism                                                   | no price        | Stage1            |
| T1      | Stage2 evidence   |                                        2024-11-21 | cancel 100B won shares bought in April; new 100B won buyback and cancellation                             | no direct price | Stage2-Actionable |
| T2      | Stage2-Actionable |                                        2024-11-21 | independent director nomination; Palliser 1% stake; SK Square market value < half of SK Hynix stake value | no price        | Actionable        |
| T3      | Stage3-Yellow     |                                               N/A | discount narrowing / NAV monetization / repeated cancellation needed                                      | N/A             | no Yellow         |
| T4      | 4B-watch          | if SK Hynix stake rally drives only event premium | no OHLC                                                                                                   | watch           |                   |

SK Square는 R6에서 “자본배분 + holding-company discount”의 정석이다. Reuters는 SK Square가 기존 100B won 자사주를 소각하고, 추가로 100B won을 매입해 3개월 내 소각할 계획이라고 보도했다. 또한 Palliser Capital이 약 1% stake를 보유하고 주주환원 개선을 요구했으며, SK Square의 market value가 보유 중인 SK Hynix stake 가치의 절반에도 못 미친다고 전했다. 이건 plain Stage2보다 강한 `Stage2-Actionable`이다. ([Reuters][5])

### Trigger price validation row

```json
{
  "case_id": "r6_loop15_sk_square_activist_buyback",
  "symbol": "402340",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable",
  "trigger_date": "2024-11-21",
  "existing_buyback_cancel_krw_bn": 100,
  "new_buyback_krw_bn": 100,
  "new_buyback_cancel_timing_months": 3,
  "sk_hynix_stake_pct": 20,
  "sk_hynix_stake_value_usd_bn": 18,
  "sk_square_market_value_discount_context": "less_than_half_of_SK_Hynix_stake_value",
  "activist": "Palliser Capital",
  "activist_stake_pct": 1,
  "independent_director_nomination": true,
  "direct_event_return": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "NAV_discount_narrowing",
    "repeat_buyback",
    "asset_monetization",
    "governance_execution",
    "SK_Hynix_stake_risk_control"
  ],
  "trigger_outcome_label": "Stage2_Actionable_holdco_discount"
}
```

### 판정

```text
score_price_alignment = Stage2_promote_candidate
new_rule = activist + cancellation + NAV discount는 Stage2-Actionable
but = NAV discount narrowing / repeated execution 없으면 Green 금지
```

---

## Case E — Hana Bank / Dunamu stake acquisition

```text
symbols = 086790 / private_Dunamu
company_scope = Hana Financial / Hana Bank / Dunamu / Upbit
case_type = Stage2 digital bank
archetype = DIGITAL_ASSET_BANK_ENTRY_STAGE2
```

### Trigger grid

| trigger | type                        |          date | 당시 공개 evidence                                                                  | 가격 anchor     | outcome                         |
| ------- | --------------------------- | ------------: | ------------------------------------------------------------------------------- | ------------- | ------------------------------- |
| T0      | awareness                   |     2025~2026 | Korean crypto market / Upbit dominance                                          | no price      | Stage1                          |
| T1      | Stage2 evidence             | 2026-05-14/15 | Hana Bank acquires 6.55% Dunamu stake for 1T won / ~$700M                       | no Hana price | Stage2                          |
| T2      | Stage2-Actionable candidate |    2026-05-15 | Upbit handles >80% Korea virtual-asset trading volume; Dunamu highly profitable | no price      | digital-asset banking candidate |
| T3      | 4B-watch                    |       2026-05 | regulatory / crypto-cycle / valuation risk                                      | no price      | watch                           |
| T4      | Stage3-Yellow               |           N/A | revenue synergy, remittance monetization, regulatory approval needed            | N/A           | no Yellow                       |

Hana-Dunamu는 R6 디지털금융의 Stage2 trigger다. Reuters는 Hana Bank가 Dunamu 6.55% stake를 1T won, 약 $700M에 인수한다고 보도했고, Upbit이 한국 virtual asset trading volume의 80% 이상을 처리하며 수익성이 높다고 설명했다. 이건 전통 은행이 디지털자산 infrastructure에 들어가는 명확한 Stage2다. ([Reuters][6])

WSJ는 이 투자가 한국 은행의 단일 디지털자산 entity 투자 중 최대 규모이고, Hana와 Dunamu가 blockchain-based overseas remittance service를 공동 개발해 기술검증까지 마쳤다고 보도했다. 다만 regulatory approval, crypto-cycle, capital allocation efficiency가 남아 있어서 Green은 아니다. ([월스트리트저널][7])

### Trigger price validation row

```json
{
  "case_id": "r6_loop15_hana_dunamu_digital_asset_entry",
  "symbols": "086790/private_Dunamu",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2_digital_asset_entry",
  "trigger_date": "2026-05-14/2026-05-15",
  "stake_acquired_pct": 6.55,
  "transaction_value_krw_trn": 1.0,
  "transaction_value_usd_mn": 700,
  "upbit_korea_virtual_asset_volume_share_pct": 80,
  "kakao_investment_remaining_stake_pct": 4.03,
  "blockchain_remittance_technical_verification": true,
  "direct_hana_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "regulatory_approval",
    "crypto_trading_volume_durability",
    "remittance_revenue_model",
    "capital_ratio_impact",
    "Dunamu_valuation_mark"
  ],
  "trigger_outcome_label": "Stage2_digital_asset_bank_entry"
}
```

### 판정

```text
score_price_alignment = success_candidate_stage2
new_rule = bank + crypto-exchange stake는 Stage2
but = 규제/거래대금/수익모델/자본비율 전에는 Green 금지
```

---

## Case F — Naver Financial / Dunamu all-stock acquisition + Upbit security event

```text
symbols = 035420 / private_Dunamu
case_type = Stage2 with security 4C-watch
archetype = CRYPTO_EXCHANGE_MA_STAGE2_WITH_SECURITY_4C
```

### Trigger grid

| trigger | type              |       date | 당시 공개 evidence                                                                | 가격 anchor           | outcome              |
| ------- | ----------------- | ---------: | ----------------------------------------------------------------------------- | ------------------- | -------------------- |
| T0      | awareness         |       2025 | Korean crypto/stablecoin growth                                               | no price            | Stage1               |
| T1      | Stage2 evidence   | 2025-11-27 | Naver Financial to acquire Dunamu in all-stock 15.13T won / $10.27B deal      | Naver initially +7% | Stage2-Actionable    |
| T2      | 4C-watch          | 2025-11-27 | Upbit abnormal withdrawal 54B won; Naver later -4.2%                          | +7% → -4.2%         | security trust watch |
| T3      | Stage2-Actionable | 2025-11-27 | Upbit ~70% Korea market share, profitable; Naver traffic synergy              | no full OHLC        | candidate            |
| T4      | Stage3-Yellow     |        N/A | regulatory/shareholder approval, security remediation, revenue synergy needed | N/A                 | no Yellow            |

Naver-Dunamu는 R6 digital finance에서 trigger 분해가 아주 중요하다. Reuters는 Naver Financial이 Dunamu를 15.13T won, $10.27B all-stock deal로 인수한다고 보도했고, Naver shares가 처음에는 +7% 이상 올랐다고 전했다. Upbit은 South Korea largest crypto exchange로 약 70% market share와 높은 수익성을 갖는다고 보도됐다. ([Reuters][8])

하지만 같은 날 Upbit에서 54B won abnormal withdrawal이 발생했다는 소식으로 Naver shares는 -4.2%로 돌아섰다. 따라서 이 case는 `Stage2-Actionable M&A`이면서 동시에 **security / custody / operational trust 4C-watch**가 붙는다. ([Reuters][8])

### Trigger price validation row

```json
{
  "case_id": "r6_loop15_naver_financial_dunamu_ma_security",
  "symbols": "035420/private_Dunamu",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2_MA_with_security_4C_watch",
  "trigger_date": "2025-11-27",
  "deal_value_krw_trn": 15.13,
  "deal_value_usd_bn": 10.27,
  "share_exchange_ratio": "2.54_Naver_Financial_shares_per_Dunamu_share",
  "naver_initial_event_mfe_pct": 7.0,
  "naver_later_event_return_pct": -4.2,
  "upbit_market_share_pct_context": 70,
  "abnormal_withdrawal_krw_bn": 54,
  "upbit_cover_loss_with_own_assets": true,
  "stage3_gate_missing": [
    "regulatory_approval",
    "shareholder_approval",
    "security_remediation",
    "crypto_revenue_durability",
    "fintech_synergy",
    "Nasdaq_or_value_unlock_clarity"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_Actionable_MA_with_security_4C_overlay"
}
```

### 판정

```text
score_price_alignment = evidence_good_but_security_4C_watch
new_rule = crypto exchange M&A는 market share와 수익성만이 아니라 custody/security를 hard overlay
```

---

## Case G — Stablecoin policy / Kakao Pay·LG CNS·Aton·ME2ON frenzy

```text
symbols = 377300 / 064400 / 158430 / 201490
company_scope = Kakao Pay / LG CNS / Aton / ME2ON
case_type = 4B-overheat / policy event premium
archetype = STABLECOIN_POLICY_4B_OVERHEAT
```

### Trigger grid

| trigger | type            |    date | 당시 공개 evidence                                                                      | 가격 anchor                    | outcome                 |
| ------- | --------------- | ------: | ----------------------------------------------------------------------------------- | ---------------------------- | ----------------------- |
| T0      | awareness       | 2025-06 | President Lee pledge to allow won-based crypto assets / stablecoins                 | sector frenzy                | Stage1                  |
| T1      | Stage2 evidence | 2025-06 | proposed bill allows firms with equity as low as 500M won to issue won stablecoins  | no single trigger date price | policy Stage2           |
| T2      | 4B-overheat     | 2025-06 | Kakao Pay more than doubled in month; LG CNS +70%; Aton +80%; ME2ON tripled         | broad frenzy                 | 4B                      |
| T3      | 4C-watch        | 2025-06 | BOK wary of non-bank stablecoin issuers; margin loans 20.5T won; regulation unclear | no hard break                | policy/regulatory watch |
| T4      | Stage3-Yellow   |     N/A | license / issuance volume / fee revenue / risk management needed                    | N/A                          | no Yellow               |

Stablecoin theme는 R6의 대표 4B다. FT는 won-based stablecoin 정책 기대와 함께 Kakao Pay shares가 한 달 만에 두 배 이상, LG CNS가 약 +70%, Aton이 +80%, ME2ON이 세 배 올랐다고 보도했다. 또 margin loans가 20.5T won으로 늘었고, proposed bill은 500M won equity만 있어도 stablecoin 발행이 가능하게 하는 내용이라 systemic risk 논란이 있었다. ([Financial Times][9])

이건 Stage2 policy trigger는 맞지만, 실제 license, issuance volume, fee revenue, risk management가 없으면 Stage3가 아니다. BOK도 non-bank stablecoin issuer가 통화정책과 자본흐름에 미치는 영향을 우려했다. ([Financial Times][9])

### Trigger price validation row

```json
{
  "case_id": "r6_loop15_stablecoin_policy_fintech_frenzy",
  "symbols": "377300/064400/158430/201490",
  "best_trigger": "T2",
  "best_trigger_type": "4B_policy_overheat",
  "trigger_period": "2025-06",
  "kakao_pay_monthly_return_pct": 100,
  "lg_cns_return_pct": 70,
  "aton_return_pct": 80,
  "me2on_return_pct": 200,
  "margin_loans_krw_trn": 20.5,
  "stablecoin_bill_min_equity_krw_mn": 500,
  "bok_concern_nonbank_issuers": true,
  "regulatory_framework_unclear": true,
  "stage3_gate_missing": [
    "stablecoin_license",
    "issuance_volume",
    "transaction_fee_revenue",
    "reserve_management",
    "BOK_regulatory_clearance",
    "AML_KYC_controls"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "4B_policy_overheat_not_stage3"
}
```

### 판정

```text
score_price_alignment = event_premium_4B_watch
new_rule = stablecoin policy theme는 실제 license/volume/revenue 전까지 Stage3 금지
```

---

## Case H — Kakao founder indictment / KakaoBank control risk

```text
symbols = 035720 / 323410 / 377300
company_scope = Kakao / KakaoBank / Kakao Pay
case_type = 4C governance/regulatory watch
archetype = KAKAO_BANK_CONTROL_REGULATORY_4C
```

### Trigger grid

| trigger | type          |                                                              date | 당시 공개 evidence                                                                      | 가격 anchor                        | outcome         |
| ------- | ------------- | ----------------------------------------------------------------: | ----------------------------------------------------------------------------------- | -------------------------------- | --------------- |
| T0      | awareness     |                                                         2023~2024 | SM Entertainment acquisition probe / Kakao regulatory scrutiny                      | no price                         | watch           |
| T1      | 4C-watch      |                                                        2024-07-22 | court reviews arrest warrant for Kakao founder over stock manipulation accusation   | KakaoBank control risk mentioned | 4C-watch        |
| T2      | 4C-watch      |                                                        2024-07-23 | founder arrested; Kakao shares -4.6% after arrest source                            | Kakao -4.6%                      | governance risk |
| T3      | 4C validation |                                                        2024-08-08 | prosecutors indict Kakao founder; Kakao posts OP +18.5% but legal overhang persists | no price                         | watch           |
| T4      | hard 4C       | if conviction triggers ownership restriction / forced stake issue | not confirmed                                                                       | pending                          |                 |

Kakao founder case는 R6에서 핀테크·인터넷은행 governance 4C-watch다. Reuters는 Kakao founder가 SM Entertainment acquisition 관련 stock manipulation 혐의로 arrest warrant review를 받았고, conviction이 발생하면 금융범죄 전력자가 은행 지분 10% 초과 보유를 제한받기 때문에 KakaoBank control에 영향이 있을 수 있다고 보도했다. ([Reuters][10])

FT는 founder arrest 이후 Kakao shares가 4.6% 더 하락했다고 보도했다. 이후 Reuters는 founder와 전직 경영진들이 indictment 됐고, Kakao는 Q2 OP +18.5%를 냈음에도 법적 리스크가 남아 있다고 전했다. 즉 실적이 좋아도 **financial-license / bank-control / governance risk**가 R6 4C overlay다. ([Financial Times][11])

### Trigger price validation row

```json
{
  "case_id": "r6_loop15_kakao_founder_kakaobank_control_risk",
  "symbols": "035720/323410/377300",
  "best_trigger": "T1/T2/T3",
  "best_trigger_type": "4C_governance_regulatory_watch",
  "t1_date": "2024-07-22",
  "founder_stake_control_context_pct": 24,
  "kakaobank_control_risk_if_convicted": true,
  "financial_crime_bank_stake_threshold_pct": 10,
  "t2_date": "2024-07-23",
  "kakao_event_mae_pct": -4.6,
  "t3_date": "2024-08-08",
  "q2_op_krw_bn": 134,
  "q2_op_yoy_pct": 18.5,
  "founder_indicted": true,
  "hard_4c_confirmed": false,
  "stage3_gate_missing": [
    "legal_resolution",
    "bank_ownership_clearance",
    "financial_license_stability",
    "governance_reform",
    "affiliate_fundraising_recovery"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "4C_watch_not_hard_until_conviction_or_ownership_action"
}
```

### 판정

```text
score_price_alignment = thesis_break_watch
new_rule = 핀테크/인터넷은행은 founder/governance/legal risk를 license-control 4C로 overlay
```

---

# 6. Trigger별 가격경로 검증 요약

| case                 | best trigger     |  entry anchor |                                   event MFE/MAE | market-relative | full MFE/MAE | outcome              |
| -------------------- | ---------------- | ------------: | ----------------------------------------------: | --------------: | ------------ | -------------------- |
| Brokerage basket     | T1 2026-05-06    |  sector index |              securities +13.5%, financial +4.2% |    KOSPI +6.45% | unavailable  | Stage2-Actionable    |
| Financial Value-Up   | T1/T2            |        policy |                            no direct bank price |             N/A | unavailable  | Stage2 policy        |
| Samsung buyback      | T1/T2 2024-11-15 |         event |                                           +7.2% |     unavailable | unavailable  | Stage2-Actionable    |
| SK Square buyback    | T1/T2 2024-11-21 |      no price |                                             N/A |             N/A | unavailable  | Stage2-Actionable    |
| Hana/Dunamu          | T1/T2 2026-05    | no Hana price |                                             N/A |             N/A | unavailable  | Stage2 digital asset |
| Naver/Dunamu         | T1/T2 2025-11-27 |         event |                                  +7% then -4.2% |     unavailable | unavailable  | Stage2 + security 4C |
| Stablecoin/Kakao Pay | T2 2025-06       |      thematic | Kakao Pay 2x+, LG CNS +70%, Aton +80%, ME2ON 3x |     unavailable | unavailable  | 4B overheat          |
| Kakao/KakaoBank risk | T1/T2/T3         |         event |                        Kakao -4.6% after arrest |     unavailable | unavailable  | 4C-watch             |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
Financial Value-Up:
정책 beta는 생겼지만 bank별 CET1/ROE/환원 실행 없이는 Stage2에 머문다.

Hana/Dunamu:
digital-asset entry는 명확하지만 Hana 주가 anchor와 수익모델 확인 전 Stage2.

F&F 같은 M&A optionality와 마찬가지로, Naver/Hana의 crypto exposure도 deal value만으로 Green 금지.
```

## Stage 2-Actionable entry 성과

```text
Brokerage basket:
KOSPI rally day에 securities +13.5%.
시장유동성 trigger는 Stage2-Actionable로 승격 가능.

Samsung buyback:
10T won buyback + 3T won cancellation + +7.2%.
자본배분 trigger는 Actionable이지만 underlying business gate 필요.

SK Square:
100B cancellation + 100B new buyback + activist + NAV discount.
가격자료는 부족하지만 Actionable capital allocation trigger.
```

## Stage 3-Yellow 후보

```text
Naver/Dunamu:
Upbit 70% market share, 15.13T won deal, Naver initial +7%.
하지만 abnormal withdrawal 54B won으로 security 4C가 즉시 붙어 Yellow 보류.

Brokerage basket:
full OHLC와 증권사 순이익/거래대금 확인되면 Yellow 가능.

Samsung buyback:
소각 execution은 강하지만 HBM/영업 회복 없으면 Yellow 보류.
```

## Stage3-Green

```text
이번 R6 Loop 15에서 확정 Green 없음.

이유:
- 증권주는 실제 거래대금/브로커리지 순이익 확인 필요
- 금융지주는 CET1/ROE/환원율 확인 필요
- buyback은 소각과 EPS accretion, business recovery 필요
- crypto M&A는 regulatory/security/revenue synergy 확인 필요
- stablecoin은 license/volume/revenue 전까지 4B
```

## 기존 점수표가 놓쳤을 가능성

```text
Stage2_promote_candidate:
- Brokerage basket
- Samsung buyback
- SK Square buyback / activist
- Naver/Dunamu, 단 security overlay

missed_structural 가능성:
- Brokerage basket은 full OHLC와 실적 확인 시 Stage2→Yellow 승격 가능.
- SK Square는 NAV discount narrowing 확인 시 Stage2→Yellow 가능.

false positive risk:
- stablecoin policy rally
- crypto M&A without security/regulatory control
- buyback without business recovery
```

---

# 8. score-price alignment 판정

```text
Stage2_promote_candidate:
- Brokerage basket
- Samsung buyback
- SK Square buyback
- Naver/Dunamu, with security overlay

Stage3-Yellow candidate:
- Brokerage basket, if trading value/earnings confirm
- SK Square, if NAV discount narrowing confirms
- Naver/Dunamu, if security/regulatory approval clears

Stage3-Green:
- 없음

event_premium:
- Stablecoin policy frenzy
- Naver/Dunamu first +7% pop
- Samsung buyback first rebound

false_positive_score:
- Stablecoin policy stocks if treated as real financial revenue before license/volume
- Buyback if treated as Green without business recovery
- Crypto exchange M&A if security/custody risk ignored

evidence_good_but_price_failed:
- Naver/Dunamu: +7% initial → -4.2% after abnormal withdrawal

thesis_break_watch:
- Kakao founder/KakaoBank control risk
- Upbit abnormal withdrawal
- Stablecoin regulatory uncertainty
```

---

# 9. 점수비중 교정

## 올릴 축

```text
actual_buyback_cancellation +5
CET1_capital_return_capacity +5
ROE_and_credit_cost_visibility +5
brokerage_trading_value_conversion +5
NAV_discount_narrowing +5
regulatory_approval_for_fintech_MA +5
custody_security_trust +5
stablecoin_license_and_reserve_quality +5
customer_data_rights_and_privacy +4
financial_license_governance_risk +5
```

### 근거

삼성 buyback은 매입 발표보다 **실제 소각**이 중요하다는 것을 보여줬고, SK Square는 NAV discount와 반복 소각이 holding company rerating의 핵심임을 보여줬다. Brokerage basket은 KOSPI rally 자체보다 거래대금/브로커리지 수익 전환이 중요하다. Naver/Dunamu는 market share보다 custody/security가 즉시 4C가 될 수 있음을 보여줬다.

## 내릴 축

```text
policy_valueup_headline_only -5
buyback_announcement_without_cancellation -4
crypto_exchange_market_share_only -5
stablecoin_policy_hype_only -5
fintech_MA_without_regulatory_approval -4
brokerage_beta_without_trading_value -4
founder_legal_risk_ignored -5
```

### 근거

Value-Up headline은 bank별 CET1/ROE/환원 execution 없이는 Stage2다. Stablecoin theme은 Kakao Pay·LG CNS·Aton·ME2ON을 급등시켰지만 license/fee revenue가 없었다. Naver/Dunamu는 Upbit의 market share가 좋아도 abnormal withdrawal이 나오자 바로 -4.2%로 돌아섰다.

---

# 10. Stage 2-Actionable 승격 조건

R6 Loop 15 shadow rule:

```text
R6에서 Stage 2 evidence가 아래 중 3개 이상이면 Stage2-Actionable로 승격한다.

1. buyback 금액뿐 아니라 실제 cancellation이 명시된다.
2. CET1 / capital buffer / payout capacity가 같이 확인된다.
3. sector beta가 아니라 trading value / brokerage fee / margin finance로 연결될 가능성이 있다.
4. fintech M&A가 market share뿐 아니라 regulatory approval path와 revenue synergy를 갖는다.
5. NAV discount가 숫자로 확인되고, activist/buyback/asset monetization trigger가 있다.
6. trigger 당일 또는 이벤트 직후 market-relative 가격 반응이 강하다.
```

적용:

```text
Brokerage basket:
securities +13.5%, market rally liquidity.

Samsung buyback:
10T won buyback + 3T cancellation + +7.2%.

SK Square:
100B cancellation + 100B new buyback + activist + NAV discount.

Naver/Dunamu:
15.13T won M&A + initial +7%, but security overlay.
```

---

# 11. Stage 3-Yellow 조건

```text
Stage3-Yellow:
- 자본배분 / fintech / 금융 trigger가 실제 이익경로로 연결될 가능성이 높아짐
- 하지만 핵심 gate 하나가 남음
```

후보:

```text
Brokerage basket:
거래대금/브로커리지 수익 확인 시 Yellow.

SK Square:
NAV discount narrowing과 추가 cancellation 확인 시 Yellow.

Naver/Dunamu:
security remediation + regulatory approval + crypto revenue durability 확인 시 Yellow.

Financial groups:
CET1 > target, payout/buyback/cancellation, ROE improvement가 동시에 확인되면 Yellow.
```

---

# 12. Stage 3-Green 조건

```text
Stage3-Green:
- buyback이 실제 소각되어 EPS accretion이 확인됨
- 금융지주는 CET1/ROE/payout/credit cost가 동시에 안정됨
- 증권주는 거래대금 → 순이익으로 연결됨
- fintech M&A는 승인/보안/수익모델이 닫힘
- stablecoin은 license, reserve quality, fee revenue, AML/KYC가 확인됨
- full-window MFE/MAE가 우호적
```

이번 R6 Loop 15에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- stablecoin/crypto policy만으로 핀테크주가 2~3배 급등
- M&A headline 직후 security/custody issue 발생
- KOSPI rally로 증권주가 급등하지만 거래대금·이익 전환 확인 안 됨
- buyback announcement가 사업 회복 없이 주가 방어용으로만 해석됨
- Value-Up policy 기대만 있고 firm-level execution 없음
```

적용:

```text
Stablecoin/Kakao Pay:
한 달 2배+, margin loans 20.5T won, regulatory uncertainty → 4B.

Naver/Dunamu:
+7% initial pop, then -4.2% security issue → 4B/4C overlay.

Samsung buyback:
+7.2% rebound but still business recovery gate → Stage2 + 4B-watch 가능.
```

---

# 14. 4C hard gate 조건

```text
R6 4C:
- crypto exchange abnormal withdrawal / custody failure
- fintech customer-data violation
- founder / major shareholder legal risk threatening bank license or ownership
- stablecoin reserve failure / regulatory ban
- broker PF loss or margin-loan unwind
- bank credit-cost spike / CET1 deterioration blocking capital return
- buyback cancellation not executed after announcement
```

이번 R6 Loop 15에서 hard 4C 확정은 없다.

```text
hard_4c_not_confirmed = true
```

Strong 4C-watch:

```text
- Upbit abnormal withdrawal in Naver/Dunamu deal
- Kakao founder indictment / KakaoBank control risk
- Stablecoin regulatory uncertainty
- Value-Up execution gap
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_229.md 요약

```md
# R6 Loop 15. Financials / Capital Allocation / Digital Finance Trigger-level Price Validation

이번 라운드는 R6 Loop 15 trigger-level validation 라운드다.

핵심 결론:
- Brokerage basket is Stage2-Actionable. On 2026-05-06, KOSPI crossed 7,000 for the first time, foreign net buying hit 3.1T won, securities firms rallied 13.5%, and financial groups gained 4.2%. Green requires actual trading value, brokerage fee income, margin finance and IB earnings.
- Financial-group Value-Up is Stage2 policy. FSS discussed penalties including possible delisting for firms failing shareholder-return criteria, but bank-level Yellow requires CET1, ROE, payout ratio, buyback cancellation and credit-cost visibility.
- Samsung Electronics buyback is Stage2-Actionable capital allocation. 10T won buyback, 3T won immediate cancellation, shares +7.2%. Green requires business recovery and execution of remaining buyback.
- SK Square is Stage2-Actionable holdco discount. 100B won cancellation, new 100B won buyback/cancellation, Palliser activism and SK Hynix stake discount. Green requires NAV discount narrowing and repeated execution.
- Hana Bank / Dunamu is Stage2 digital-asset bank entry. Hana buys 6.55% of Dunamu for 1T won / about $700M; Upbit handles over 80% of Korean virtual-asset trading volume. Green requires regulatory approval, revenue synergy and capital-ratio impact.
- Naver Financial / Dunamu is Stage2 M&A with security 4C-watch. 15.13T won all-stock deal, Naver initially +7%, then -4.2% after 54B won abnormal withdrawal from Upbit. Security/custody is hard overlay.
- Stablecoin policy stocks are 4B overheat. Kakao Pay more than doubled in a month, LG CNS +70%, Aton +80%, ME2ON tripled, while margin loans reached 20.5T won and regulation remained unclear.
- Kakao founder / KakaoBank control risk is governance 4C-watch. Founder arrest/indictment and possible bank-ownership implications create fintech license/control overlay.

Main calibration:
- Raise actual_buyback_cancellation, CET1 capital-return capacity, ROE/credit-cost visibility, brokerage trading-value conversion, NAV discount narrowing, fintech M&A regulatory approval, custody/security trust, stablecoin license/reserve quality, data rights/privacy, financial-license governance risk.
- Lower policy headline only, buyback announcement without cancellation, crypto market-share only, stablecoin hype only, fintech M&A without approval, brokerage beta without trading value, founder legal risk ignored.
```

## docs/checkpoints/checkpoint_28a_round229_r6_loop15.md 요약

```md
# Checkpoint 28A Round 229 R6 Loop 15 Trigger-level Calibration

## 반영 내용
- R6 Loop 15 trigger-level validation을 수행했다.
- brokerage basket, financial-group Value-Up, Samsung buyback, SK Square activist/buyback, Hana/Dunamu, Naver/Dunamu, stablecoin policy/Kakao Pay, Kakao founder/KakaoBank risk를 검토했다.
- full adjusted OHLC window는 확보하지 못했으므로 Reuters / FT / WSJ / MarketWatch의 reported event return과 event price anchor를 사용했다.
- OHLC 미확보를 이유로 Stage 후보를 강등하지 않고, price_data_unavailable_after_deep_search로 분리 기록했다.

## 핵심 보정
- 자본배분은 announcement보다 actual cancellation을 중시한다.
- 은행/금융지주는 Value-Up headline이 아니라 CET1, ROE, payout, credit cost가 Stage gate다.
- 증권주는 KOSPI beta가 아니라 trading value → brokerage earnings conversion이 Stage gate다.
- crypto/fintech M&A는 market share보다 security/custody/regulatory approval이 hard overlay다.
- stablecoin policy rally는 license/reserve/revenue 전까지 4B overheat로 둔다.
```

## data/e2r_case_library/cases_r6_loop15_round229.jsonl 초안

```jsonl
{"case_id":"r6_loop15_brokerage_kospi_liquidity_boom","symbol":"016360/039490/005940/006800/brokerage_basket","company_name":"Samsung Securities / Kiwoom / NH Investment / Mirae / brokerage basket","case_type":"Stage2_promote_candidate","primary_archetype":"BROKERAGE_MARKET_VOLUME_STAGE2_ACTIONABLE","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable_to_Stage3-Yellow_candidate","price_validation":{"trigger_date":"2026-05-06","kospi_close_return_pct":6.45,"kospi_intraday_high_return_pct":7.06,"kospi_close":7384.56,"foreign_net_buying_krw_trn":3.1,"foreign_net_buying_usd_bn":2.13,"securities_firms_index_return_pct":13.5,"financial_groups_index_return_pct":4.2,"stage3_gate_missing":["daily_trading_value","brokerage_commission_revenue","margin_finance_balance","IB_fee_income","PF_risk_absorption"],"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate","notes":"Market liquidity boom and securities index +13.5% are Stage2-Actionable, but Green needs earnings conversion."}
{"case_id":"r6_loop15_financial_group_valueup_basket","symbol":"105560/055550/086790/316140","company_name":"KB Financial / Shinhan / Hana / Woori","case_type":"success_candidate_stage2","primary_archetype":"FINANCIAL_GROUP_VALUEUP_STAGE2","best_trigger":"T1/T2","stage_candidate":"Stage2_policy","price_validation":{"trigger_date":"2024-02-28","policy_trigger":"Corporate Value-Up / shareholder-return penalties under discussion","possible_penalties":["shareholder_return_criteria_penalty","possible_delisting_for_non_compliance"],"broad_market_support":["corporate_governance_reform","dividend_tax_incentives","director_fiduciary_duty_discussion"],"bank_specific_price_anchor":"price_data_unavailable_after_deep_search","stage3_gate_missing":["CET1_ratio","payout_ratio","buyback_cancellation","ROE","NIM","credit_cost"]},"score_price_alignment":"success_candidate_stage2","notes":"Value-Up policy is Stage2 beta; bank-level Yellow requires CET1/ROE/capital-return execution."}
{"case_id":"r6_loop15_samsung_buyback_capital_allocation","symbol":"005930","company_name":"Samsung Electronics","case_type":"Stage2_promote_candidate","primary_archetype":"BUYBACK_CAPITAL_ALLOCATION_STAGE2_ACTIONABLE","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2024-11-15","buyback_total_krw_trn":10,"buyback_total_usd_bn":7.17,"immediate_buyback_cancel_krw_trn":3,"first_buyback_since":2017,"event_return_pct":7.2,"ytd_pre_event_return_pct":-32,"stage3_gate_missing":["HBM_competitiveness_recovery","Nvidia_qualification","foundry_loss_reduction","sustained_OP_recovery","remaining_7T_execution"],"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate","notes":"Buyback + cancellation is actionable capital allocation, but Green requires business recovery and execution."}
{"case_id":"r6_loop15_sk_square_activist_buyback","symbol":"402340","company_name":"SK Square","case_type":"Stage2_promote_candidate","primary_archetype":"HOLDCO_DISCOUNT_ACTIVIST_STAGE2","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2024-11-21","existing_buyback_cancel_krw_bn":100,"new_buyback_krw_bn":100,"new_buyback_cancel_timing_months":3,"sk_hynix_stake_pct":20,"sk_hynix_stake_value_usd_bn":18,"sk_square_market_value_discount_context":"less_than_half_of_SK_Hynix_stake_value","activist":"Palliser Capital","activist_stake_pct":1,"independent_director_nomination":true,"direct_event_return":"price_data_unavailable_after_deep_search","stage3_gate_missing":["NAV_discount_narrowing","repeat_buyback","asset_monetization","governance_execution","SK_Hynix_stake_risk_control"]},"score_price_alignment":"Stage2_promote_candidate","notes":"Activist + cancellation + NAV discount is Stage2-Actionable; Green needs discount narrowing and repeated execution."}
{"case_id":"r6_loop15_hana_dunamu_digital_asset_entry","symbol":"086790/private_Dunamu","company_name":"Hana Financial / Hana Bank / Dunamu","case_type":"success_candidate_stage2","primary_archetype":"DIGITAL_ASSET_BANK_ENTRY_STAGE2","best_trigger":"T1/T2","stage_candidate":"Stage2_digital_asset_entry","price_validation":{"trigger_date":"2026-05-14/2026-05-15","stake_acquired_pct":6.55,"transaction_value_krw_trn":1.0,"transaction_value_usd_mn":700,"upbit_korea_virtual_asset_volume_share_pct":80,"kakao_investment_remaining_stake_pct":4.03,"blockchain_remittance_technical_verification":true,"direct_hana_price_anchor":"price_data_unavailable_after_deep_search","stage3_gate_missing":["regulatory_approval","crypto_trading_volume_durability","remittance_revenue_model","capital_ratio_impact","Dunamu_valuation_mark"]},"score_price_alignment":"success_candidate_stage2","notes":"Bank entry into digital assets is Stage2; Green requires regulatory approval, monetization and capital-ratio clarity."}
{"case_id":"r6_loop15_naver_financial_dunamu_ma_security","symbol":"035420/private_Dunamu","company_name":"Naver Financial / Dunamu / Upbit","case_type":"Stage2_with_4C_overlay","primary_archetype":"CRYPTO_EXCHANGE_MA_STAGE2_WITH_SECURITY_4C","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable_with_security_4C","price_validation":{"trigger_date":"2025-11-27","deal_value_krw_trn":15.13,"deal_value_usd_bn":10.27,"share_exchange_ratio":"2.54_Naver_Financial_shares_per_Dunamu_share","naver_initial_event_mfe_pct":7.0,"naver_later_event_return_pct":-4.2,"upbit_market_share_pct_context":70,"abnormal_withdrawal_krw_bn":54,"upbit_cover_loss_with_own_assets":true,"stage3_gate_missing":["regulatory_approval","shareholder_approval","security_remediation","crypto_revenue_durability","fintech_synergy","Nasdaq_or_value_unlock_clarity"],"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"evidence_good_but_security_4C_watch","notes":"Crypto exchange M&A must include custody/security overlay; market share alone is not Green."}
{"case_id":"r6_loop15_stablecoin_policy_fintech_frenzy","symbol":"377300/064400/158430/201490","company_name":"Kakao Pay / LG CNS / Aton / ME2ON","case_type":"event_premium_4B_watch","primary_archetype":"STABLECOIN_POLICY_4B_OVERHEAT","best_trigger":"T2","stage_candidate":"4B-watch","price_validation":{"trigger_period":"2025-06","kakao_pay_monthly_return_pct":100,"lg_cns_return_pct":70,"aton_return_pct":80,"me2on_return_pct":200,"margin_loans_krw_trn":20.5,"stablecoin_bill_min_equity_krw_mn":500,"bok_concern_nonbank_issuers":true,"regulatory_framework_unclear":true,"stage3_gate_missing":["stablecoin_license","issuance_volume","transaction_fee_revenue","reserve_management","BOK_regulatory_clearance","AML_KYC_controls"],"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_4B_watch","notes":"Stablecoin policy rally is 4B overheat until license, reserve quality and revenue are confirmed."}
{"case_id":"r6_loop15_kakao_founder_kakaobank_control_risk","symbol":"035720/323410/377300","company_name":"Kakao / KakaoBank / Kakao Pay","case_type":"4c_watch","primary_archetype":"KAKAO_BANK_CONTROL_REGULATORY_4C","best_trigger":"T1/T2/T3","stage_candidate":"4C-watch","price_validation":{"founder_stake_control_context_pct":24,"kakaobank_control_risk_if_convicted":true,"financial_crime_bank_stake_threshold_pct":10,"kakao_event_mae_pct":-4.6,"q2_op_krw_bn":134,"q2_op_yoy_pct":18.5,"founder_indicted":true,"hard_4c_confirmed":false,"stage3_gate_missing":["legal_resolution","bank_ownership_clearance","financial_license_stability","governance_reform","affiliate_fundraising_recovery"],"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","notes":"Founder/legal risk is a financial-license and bank-control 4C overlay for fintech/online-bank names."}
```

## data/e2r_trigger_calibration/triggers_r6_loop15_round229.jsonl 초안

```jsonl
{"trigger_id":"r6l15_brokerage_T1","case_id":"r6_loop15_brokerage_kospi_liquidity_boom","trigger_type":"Stage2-Actionable","trigger_date":"2026-05-06","evidence_available":"KOSPI crosses 7,000, foreign net buying 3.1T won, securities firms +13.5%, financial groups +4.2%","event_return_pct":"securities +13.5 / financial groups +4.2","trigger_outcome_label":"Stage2_promote_candidate","promote_to":"Stage2-Actionable"}
{"trigger_id":"r6l15_valueup_T1","case_id":"r6_loop15_financial_group_valueup_basket","trigger_type":"Stage2_policy","trigger_date":"2024-02-28","evidence_available":"FSS considers penalties including possible delisting for firms failing shareholder-return criteria","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"success_candidate_stage2","promote_to":"Stage2"}
{"trigger_id":"r6l15_samsung_buyback_T1","case_id":"r6_loop15_samsung_buyback_capital_allocation","trigger_type":"Stage2-Actionable","trigger_date":"2024-11-15","evidence_available":"10T won buyback, 3T won immediate repurchase and cancellation, first buyback since 2017, shares +7.2%","event_return_pct":7.2,"trigger_outcome_label":"Stage2_promote_candidate","promote_to":"Stage2-Actionable"}
{"trigger_id":"r6l15_sksquare_T1","case_id":"r6_loop15_sk_square_activist_buyback","trigger_type":"Stage2-Actionable","trigger_date":"2024-11-21","evidence_available":"Cancel 100B won shares, new 100B won buyback/cancellation, Palliser activism, market value less than half SK Hynix stake value","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_promote_candidate","promote_to":"Stage2-Actionable"}
{"trigger_id":"r6l15_hana_dunamu_T1","case_id":"r6_loop15_hana_dunamu_digital_asset_entry","trigger_type":"Stage2_digital_asset_entry","trigger_date":"2026-05-15","evidence_available":"Hana Bank acquires 6.55% Dunamu stake for 1T won; Upbit handles over 80% Korean virtual-asset trading volume","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"success_candidate_stage2","promote_to":"Stage2"}
{"trigger_id":"r6l15_naver_dunamu_T1","case_id":"r6_loop15_naver_financial_dunamu_ma_security","trigger_type":"Stage2-Actionable","trigger_date":"2025-11-27","evidence_available":"Naver Financial agrees 15.13T won all-stock Dunamu deal; Naver initially +7%","event_return_pct":7.0,"trigger_outcome_label":"Stage2_MA_candidate","promote_to":"Stage2-Actionable"}
{"trigger_id":"r6l15_naver_dunamu_T2","case_id":"r6_loop15_naver_financial_dunamu_ma_security","trigger_type":"4C-watch","trigger_date":"2025-11-27","evidence_available":"Upbit abnormal withdrawal 54B won; Naver later -4.2%","event_return_pct":-4.2,"trigger_outcome_label":"security_4C_watch","promote_to":"4C-watch"}
{"trigger_id":"r6l15_stablecoin_T2","case_id":"r6_loop15_stablecoin_policy_fintech_frenzy","trigger_type":"4B-watch","trigger_date":"2025-06","evidence_available":"Kakao Pay >2x in month, LG CNS +70%, Aton +80%, ME2ON tripled, margin loans 20.5T won, regulatory framework unclear","event_return_pct":"KakaoPay +100 / LG CNS +70 / Aton +80 / ME2ON +200","trigger_outcome_label":"4B_policy_overheat","promote_to":"4B-watch"}
{"trigger_id":"r6l15_kakao_control_T1","case_id":"r6_loop15_kakao_founder_kakaobank_control_risk","trigger_type":"4C-watch","trigger_date":"2024-07-22","evidence_available":"Kakao founder arrest-warrant review; conviction could jeopardise KakaoBank control due financial-crime ownership rules","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"financial_license_governance_4C_watch","promote_to":"4C-watch"}
```

## data/sector_taxonomy/score_weight_profiles_round229_r6_loop15_v1.csv 초안

```csv
archetype,actual_buyback_cancellation,cet1_capital_return_capacity,roe_credit_cost_visibility,brokerage_trading_value_conversion,nav_discount_narrowing,regulatory_approval_for_fintech_ma,custody_security_trust,stablecoin_license_reserve_quality,customer_data_rights_privacy,financial_license_governance_risk,policy_valueup_headline_only_penalty,buyback_without_cancellation_penalty,crypto_market_share_only_penalty,stablecoin_policy_hype_only_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
BROKERAGE_MARKET_VOLUME_STAGE2_ACTIONABLE,+1,+1,+2,+5,+0,+1,+1,+0,+1,+1,-2,-1,-1,-2,securities index rally+foreign flow,trading value/fee income pending,brokerage earnings confirmed,Brokerage basket +13.5% is Stage2-Actionable.
FINANCIAL_GROUP_VALUEUP_STAGE2,+3,+5,+5,+1,+1,+1,+1,+0,+1,+3,-5,-3,-1,-1,Value-Up policy,CET1/payout/ROE pending,capital return execution+ROE stable,Financial groups need firm-level execution.
BUYBACK_CAPITAL_ALLOCATION_STAGE2_ACTIONABLE,+5,+2,+4,+0,+1,+0,+0,+0,+0,+1,-2,-5,-1,-1,buyback+cancellation,business recovery pending,EPS accretion+business recovery,Samsung buyback is Stage2-Actionable.
HOLDCO_DISCOUNT_ACTIVIST_STAGE2,+5,+1,+2,+0,+5,+0,+0,+0,+1,+3,-2,-4,-1,-1,activist+buyback+NAV discount,discount narrowing pending,NAV narrowing+asset monetization,SK Square template.
DIGITAL_ASSET_BANK_ENTRY_STAGE2,+1,+4,+3,+0,+1,+5,+5,+5,+4,+4,-2,-1,-5,-4,bank stake in crypto exchange,regulatory/revenue/capital ratio pending,approved digital-asset revenue,Hana/Dunamu Stage2.
CRYPTO_EXCHANGE_MA_STAGE2_WITH_SECURITY_4C,+1,+2,+3,+0,+1,+5,+5,+5,+5,+4,-2,-1,-5,-4,M&A+market share,security/regulatory approval pending,approved+secure+revenue synergy,Naver/Dunamu needs security overlay.
STABLECOIN_POLICY_4B_OVERHEAT,+0,+1,+1,+1,+0,+5,+4,+5,+5,+3,-4,-1,-4,-5,policy rally,license/reserve/revenue missing,licensed fee revenue+reserve compliance,Stablecoin theme is 4B until regulated monetization.
KAKAO_BANK_CONTROL_REGULATORY_4C,+0,+3,+3,+0,+1,+4,+3,+2,+4,+5,-2,-1,-2,-2,founder legal/ownership risk,legal resolution pending,license/control stability,KakaoBank control risk is 4C-watch.
```

---

# 이번 R6 Loop 15 결론

```text
1. 증권·브로커리지 basket은 Stage2-Actionable이다.
   KOSPI 7,000 돌파일 securities +13.5%, financial groups +4.2%는 강한 trigger지만, 실제 거래대금과 순이익 전환이 필요하다.

2. 금융지주 Value-Up은 Stage2 policy다.
   CET1, ROE, payout, buyback cancellation, credit cost가 없으면 bank-level Yellow/Green은 금지다.

3. Samsung buyback은 Stage2-Actionable 자본배분 trigger다.
   10T won buyback과 3T won cancellation, +7.2% 반응은 강하지만 business recovery gate가 남아 있다.

4. SK Square는 holdco discount Stage2-Actionable이다.
   activist + cancellation + NAV discount 조합은 좋지만, discount narrowing이 확인되어야 한다.

5. Hana Bank / Dunamu는 digital-asset bank entry Stage2다.
   Upbit의 시장지배력은 강하지만 regulation, monetization, capital ratio가 남아 있다.

6. Naver Financial / Dunamu는 Stage2 M&A + security 4C-watch다.
   +7% pop이 있었지만 Upbit abnormal withdrawal로 -4.2%로 돌아섰다.

7. Stablecoin policy stocks는 4B overheat다.
   Kakao Pay 2배+, LG CNS +70%, Aton +80%, ME2ON 3배는 license/revenue 전에는 Stage3가 아니다.

8. Kakao founder / KakaoBank control risk는 R6 governance 4C-watch다.
   핀테크와 인터넷은행은 창업자·지배구조·금융범죄 소유제한이 valuation hard gate가 될 수 있다.
```

한 문장으로 압축하면:

> **R6 Loop 15에서 배운 핵심은 “금융주는 정책·M&A·buyback headline”이 아니라, 실제 소각·CET1·ROE·거래대금의 이익 전환·regulatory approval·custody/security·license quality가 닫혀야 Stage3로 올릴 수 있다는 것이다. Stablecoin/crypto policy hype와 buyback announcement만으로는 4B/false positive가 되기 쉽다.**

[1]: https://www.reuters.com/world/asia-pacific/south-koreas-kospi-share-index-tops-7000-first-time-2026-05-06/ "https://www.reuters.com/world/asia-pacific/south-koreas-kospi-share-index-tops-7000-first-time-2026-05-06/"
[2]: https://www.reuters.com/markets/asia/skorea-considering-penalties-firms-failing-boost-shareholder-return-2024-02-28/ "https://www.reuters.com/markets/asia/skorea-considering-penalties-firms-failing-boost-shareholder-return-2024-02-28/"
[3]: https://www.ft.com/content/238f5fd4-e8f6-4eb0-9e3d-78066d6ccbe8 "https://www.ft.com/content/238f5fd4-e8f6-4eb0-9e3d-78066d6ccbe8"
[4]: https://www.reuters.com/technology/samsung-electronics-plans-72-bln-buyback-boost-shareholder-value-2024-11-15/ "https://www.reuters.com/technology/samsung-electronics-plans-72-bln-buyback-boost-shareholder-value-2024-11-15/"
[5]: https://www.reuters.com/technology/artificial-intelligence/south-koreas-ai-chip-investor-announces-plan-share-buybacks-2024-11-21/ "https://www.reuters.com/technology/artificial-intelligence/south-koreas-ai-chip-investor-announces-plan-share-buybacks-2024-11-21/"
[6]: https://www.reuters.com/world/asia-pacific/hana-bank-acquire-stake-dunamu-700-mln-filing-says-2026-05-14/ "https://www.reuters.com/world/asia-pacific/hana-bank-acquire-stake-dunamu-700-mln-filing-says-2026-05-14/"
[7]: https://www.wsj.com/business/hana-bank-to-buy-670-million-stake-in-crypto-exchange-operator-dunamu-08f99cb5 "https://www.wsj.com/business/hana-bank-to-buy-670-million-stake-in-crypto-exchange-operator-dunamu-08f99cb5"
[8]: https://www.reuters.com/world/asia-pacific/navers-payment-arm-acquire-south-korean-crypto-exchange-operator-10-bln-deal-2025-11-27/ "https://www.reuters.com/world/asia-pacific/navers-payment-arm-acquire-south-korean-crypto-exchange-operator-10-bln-deal-2025-11-27/"
[9]: https://www.ft.com/content/4b19bf90-4202-4fe7-8caf-d7db6deeb768 "https://www.ft.com/content/4b19bf90-4202-4fe7-8caf-d7db6deeb768"
[10]: https://www.reuters.com/business/south-korea-court-decide-arrest-warrant-kakao-founder-2024-07-22/ "https://www.reuters.com/business/south-korea-court-decide-arrest-warrant-kakao-founder-2024-07-22/"
[11]: https://www.ft.com/content/49141512-96db-4f2b-a776-da350e531aa0 "https://www.ft.com/content/49141512-96db-4f2b-a776-da350e531aa0"

순서상 이번은 **R6 Loop 14 — 금융·자본배분·디지털금융 가격경로 검증 라운드**다.

```text
round = R6 Loop 14
round_id = round_216
large_sector = FINANCE_CAPITAL_ALLOCATION_DIGITAL_FINANCE
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = false
hard_4c_not_confirmed = true
next_round = R7 Loop 14
```

이번 R6는 **금융지주 Value-Up, SK Square 자사주 소각, Samsung C&T 주주환원 실패, K Bank IPO, KakaoBank control risk, Naver Financial–Dunamu/Upbit, Hana Bank–Dunamu, Samsung SDS–KKR CB/stablecoin optionality**를 본다.

이번에도 KRX/Naver/Yahoo/Stooq 기준 **수정주가 일봉 OHLC 전체 구간**은 안정적으로 확보하지 못했다. 그래서 30D/90D/180D/1Y full MFE·MAE는 만들지 않고, Reuters/FT/WSJ/MarketWatch가 제공한 **event return, event price, deal value, buyback amount, IPO range, CB value, stake %, regulatory restriction**을 가격 anchor로 사용했다. full OHLC가 필요한 칸은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R6 = 금융·자본배분·디지털금융
```

R6에서 진짜 Stage 3는 “Value-Up”, “자사주”, “배당”, “PBR 저평가”, “인터넷은행”, “가상자산”, “스테이블코인”, “외국계 PE 투자”, “금융지주 리레이팅”이라는 단어가 아니다.

진짜 Stage 3는 아래가 같이 닫히는 순간이다.

```text
은행/금융지주:
자본비율 → CET1 buffer → 배당/자사주 소각 → NIM/credit cost → 대손비용 → ROE → PBR 재평가

보험/금융지주:
규제자본 → 보유지분 매각 → RBC/K-ICS 안정 → 배당여력 → 회계변동 리스크

증권/지주:
보유지분 discount → 실제 소각/배당 → governance 개선 → minority shareholder protection

핀테크/인터넷은행:
MAU/고객수 → 예대마진/수수료 → credit quality → IPO aftermarket demand → 규제 승인

디지털자산:
거래소 점유율 → custody/internal control → AML/KYC → abnormal withdrawal risk → 은행/핀테크 integration

자본배분:
CB/PE 투자/M&A → 희석률 → capital deployment → ROIC → 주주환원
```

---

# 2. 대상 canonical archetype

```text
VALUE_UP_FINANCIAL_HOLDING_STAGE2
HOLDCO_DISCOUNT_BUYBACK_STAGE2
SHAREHOLDER_RETURN_FAILURE_FALSE_POSITIVE
DIGITAL_BANK_IPO_QUALITY_GATE
DIGITAL_BANK_CONTROL_RISK_4C_WATCH
DIGITAL_ASSET_MA_TRUST_4C_WATCH
BANK_DIGITAL_ASSET_STAKE_STAGE2
PRIVATE_CAPITAL_CB_STABLECOIN_EVENT_PREMIUM
```

---

# 3. deep sub-archetype

```text
Value-Up / 금융지주:
- KB / Shinhan / Hana / Woori financial holding basket
- Commercial Act revision / treasury-share cancellation
- PBR rerating vs actual CET1 and payout execution

지주 할인:
- SK Square
- SK Hynix stake value vs holding-company market value
- buyback / cancellation / activist pressure

주주환원 실패:
- Samsung C&T
- activist proposals backed by large foreign investors
- NPS vote / management defence / stock -10%

인터넷은행:
- K Bank
- 10M+ customers
- IPO range 9,500~12,000 won
- up to 984B won raise
- valuation up to 5T won
- IPO quality and aftermarket demand gate

디지털은행 governance:
- KakaoBank
- Kakao founder legal risk
- financial-crime rule restricting bank stake above 10%
- later acquittal relief

디지털자산:
- Naver Financial / Dunamu / Upbit
- all-stock deal 15.13T won
- Naver +7% then -4.2% on abnormal withdrawal
- exchange/custody trust gate

은행의 가상자산 지분:
- Hana Bank / Dunamu
- 1T won stake
- 6.55% ownership
- Upbit >80% trading-volume context
- bank digital-asset entry vs regulatory/custody gate

PE/CB/stablecoin:
- Samsung SDS / KKR
- $820M CB
- shares +20.8%
- AI infra / physical AI / stablecoins
- CB dilution and capital-allocation gate
```

---

# 4. 국장 신규 후보 case

## Case A — 금융지주 Value-Up basket `policy Stage 2, not Green`

```text
symbols = 105560 / 055550 / 086790 / 316140
company_scope = KB Financial / Shinhan Financial / Hana Financial / Woori Financial
case_type = success_candidate_policy_stage2
archetype = VALUE_UP_FINANCIAL_HOLDING_STAGE2
```

### stage date

```text
Stage 1:
2024-02~2025-01
- Korea Value-Up programme / listing-rule reform / governance reform 기대 형성.
- 저PBR 금융지주가 대표 수혜군으로 분류됨.

Stage 2:
2026-02-25
- Commercial Act revision passed.
- newly acquired treasury shares must be cancelled within one year.
- existing treasury shares get six-month grace period.
- purpose: Korea Discount 해소, treasury-share misuse 제한, minority shareholder protection.
- KOSPI crossed 6,000 in the reform rally context.

Stage 3:
없음
- 금융지주 Green은 법안 자체가 아니라 CET1, payout ratio, buyback cancellation, credit cost, ROE/PBR rerating 확인 후.
```

금융지주 Value-Up은 R6의 큰 방향성으로는 맞다. 하지만 정책은 Stage 2다. Reuters는 2026년 2월 25일 개정 상법이 통과되어 새로 취득하는 treasury shares는 1년 안에 소각해야 하고, 기존 treasury shares에는 6개월 유예기간이 주어진다고 보도했다. FT도 같은 개정이 지배주주 방어용 자사주 활용 관행을 줄이고 minority shareholders를 보호하려는 목적이라고 설명했다. 다만 은행주 Green은 법안이 아니라 **실제 자사주 소각, 배당, CET1 buffer, credit cost, ROE**로 닫혀야 한다. ([Reuters][1])

### 실제 가격경로 검증

```json
{
  "case_id": "r6_loop14_financial_holding_value_up_policy_stage2",
  "symbols": "105560/055550/086790/316140",
  "stage2_date": "2026-02-25",
  "stage3_price": null,
  "price_data_source": "Reuters/FT Commercial Act and Value-Up reform anchors",
  "treasury_share_new_cancellation_deadline_years": 1,
  "existing_treasury_share_grace_period_months": 6,
  "policy_goal": "Korea Discount reduction and minority shareholder protection",
  "kospi_reform_context": "KOSPI crossed 6000 in reform rally context",
  "financial_holding_direct_event_prices": "price_data_unavailable_after_deep_search",
  "stage3_conditions": ["CET1 buffer", "actual buyback cancellation", "payout ratio", "credit cost", "ROE/PBR rerating"],
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_policy_stage2
rerating_result = financial_holding_value_up_stage2
stage_failure_type = policy_law_not_bank_ROE_payout_green
```

---

## Case B — SK Square `holdco discount / buyback Stage 2`

```text
symbol = 402340
case_type = success_candidate
archetype = HOLDCO_DISCOUNT_BUYBACK_STAGE2
```

### stage date

```text
Stage 1:
2024-04~2024-11
- SK Hynix HBM profit cycle makes SK Square holding-company discount visible.
- activist Palliser Capital pushes undervaluation / capital allocation discussion.

Stage 2:
2024-11-21
- SK Square announces buyback/cancellation plan.
- cancel 100B won worth of shares bought in April.
- repurchase another 100B won and cancel within three months.
- nominate independent director.
- SK Square holds 20% stake in SK Hynix.
- market value is less than half the $18B value of its SK Hynix stake.

Stage 3:
없음
- holding discount narrowing requires repeated cancellation, governance change, dividend flow from SK Hynix, and discount compression.
```

SK Square는 R6 capital-allocation의 좋은 Stage 2다. Reuters는 SK Square가 100B won worth of shares를 소각하고, 추가 100B won를 매입해 3개월 안에 소각하겠다고 밝혔으며, independent director nomination도 발표했다고 보도했다. 또한 SK Square는 SK Hynix 지분 20%를 보유하고 있고, 회사의 market value가 그 지분가치 $18B의 절반에도 못 미친다고 설명했다. 이 case는 “holding discount는 thesis가 아니라 자본배분 execution으로만 좁혀진다”는 교정값이다. ([Reuters][2])

### 실제 가격경로 검증

```json
{
  "case_id": "r6_loop14_sk_square_holdco_discount_buyback",
  "symbol": "402340",
  "stage2_date": "2024-11-21",
  "stage3_price": null,
  "price_data_source": "Reuters SK Square buyback / activist / holdco discount anchor",
  "first_cancellation_krw_bn": 100,
  "new_repurchase_and_cancellation_krw_bn": 100,
  "total_announced_cancellation_related_krw_bn": 200,
  "sk_hynix_stake_pct": 20,
  "sk_hynix_stake_value_usd_bn_context": 18,
  "market_value_vs_stake_value_context": "less_than_half",
  "activist_stake_context_pct": 1,
  "direct_event_return": "price_data_unavailable_after_deep_search",
  "stage3_conditions": ["repeated cancellation", "governance improvement", "dividend flow", "holdco discount compression"]
}
```

### alignment

```text
score_price_alignment = success_candidate_but_price_data_unavailable
rerating_result = holdco_discount_buyback_stage2
stage_failure_type = announced_buyback_not_discount_compression_green
```

---

## Case C — Samsung C&T activist proposal failure `false_positive_score`

```text
symbol = 028260
case_type = false_positive_score
archetype = SHAREHOLDER_RETURN_FAILURE_FALSE_POSITIVE
```

### stage date

```text
Stage 1:
2024-03
- activist investors push Samsung C&T to increase dividends and buybacks.
- Value-Up programme raises expectation that chaebol capital allocation will change.

Stage 4C-watch / false positive:
2024-03-15
- activist proposal fails.
- proposals backed by large investors including Norway's oil fund and Canadian pension investors.
- National Pension Service sides with Samsung management.
- Samsung C&T shares close almost -10%.
- KOSPI had been pushed to 23-month high earlier on Value-Up optimism.

Stage 3:
없음
- activist pressure alone is not Green.
- actual board adoption / payout / cancellation required.
```

Samsung C&T는 “Value-Up 기대만 보고 Green 주면 안 된다”는 반례다. FT는 Norway oil fund와 Canadian pension investors가 지지한 배당·자사주 확대 제안이 실패했고, National Pension Service가 Samsung management 편에 섰으며, Samsung C&T shares가 거의 10% 하락했다고 보도했다. 이 case는 R6에서 **shareholder-return proposal ≠ shareholder-return execution**이라는 hard calibration이다. ([Financial Times][3])

### 실제 가격경로 검증

```json
{
  "case_id": "r6_loop14_samsung_ct_activist_valueup_failure",
  "symbol": "028260",
  "stage4c_watch_date": "2024-03-15",
  "stage3_price": null,
  "price_data_source": "FT activist proposal / share-price failure anchor",
  "event_mae_pct": -10.0,
  "activist_backers": ["Norway oil fund", "Canadian pension investors"],
  "nps_vote": "sided_with_management",
  "proposal_type": ["dividend increase", "share buyback increase"],
  "proposal_passed": false,
  "stage3_conditions": ["board adoption", "payout execution", "treasury-share cancellation", "minority shareholder alignment"],
  "mfe_30d_90d": "N/A_no_valid_stage3"
}
```

### alignment

```text
score_price_alignment = false_positive_score
rerating_result = shareholder_return_proposal_failed
stage_failure_type = activist_proposal_not_capital_return_execution
```

---

## Case D — K Bank IPO `digital bank IPO quality gate`

```text
symbol = unlisted / KT-Kakao-related fintech read-through
case_type = success_candidate + IPO_quality_gate
archetype = DIGITAL_BANK_IPO_QUALITY_GATE
```

### stage date

```text
Stage 1:
2024-09-10
- K Bank announces IPO plan.
- internet-only bank IPO becomes digital-finance test after earlier 2022 plan was scrapped.

Stage 2:
2024-09-10
- IPO raise up to 984B won / $731.64M.
- 82M shares to be sold: 41M new + 41M existing.
- price range: 9,500~12,000 won.
- valuation up to 5T won.
- H1 2024 operating profit: 86.7B won, more than triple YoY.
- more than 10M customers.

Stage 3:
없음
- IPO plan is not Green.
- listed aftermarket demand, credit quality, deposit funding cost, fee income, NIM, CAC required.
```

K Bank는 디지털은행 Stage 2다. Reuters는 K Bank가 최대 984B won를 조달하는 IPO를 추진했고, 82M shares를 9,500~12,000 won range에 팔 계획이었다고 보도했다. H1 2024 operating profit은 86.7B won으로 전년 대비 3배 이상이었고, 고객은 10M명을 넘었다. 다만 인터넷은행은 고객수와 IPO size만으로 Stage 3가 아니다. credit quality, deposit funding cost, fee income, CAC, aftermarket demand가 필요하다. ([Reuters][4])

### 실제 가격경로 검증

```json
{
  "case_id": "r6_loop14_kbank_digital_bank_ipo_quality_gate",
  "symbol": "unlisted_KBank_readthrough",
  "stage2_date": "2024-09-10",
  "stage3_price": null,
  "price_data_source": "Reuters K Bank IPO plan anchor",
  "ipo_raise_max_krw_bn": 984,
  "ipo_raise_max_usd_mn": 731.64,
  "shares_to_sell_mn": 82,
  "new_shares_mn": 41,
  "existing_shares_mn": 41,
  "price_range_krw": "9500-12000",
  "valuation_max_krw_trn": 5,
  "h1_2024_operating_profit_krw_bn": 86.7,
  "customer_count_context_mn": 10,
  "stage3_conditions": ["aftermarket demand", "credit quality", "deposit funding cost", "fee income", "CAC"],
  "price_validation_status": "unlisted_ipo_plan_no_aftermarket_ohlc"
}
```

### alignment

```text
score_price_alignment = success_candidate_IPO_quality_gate
rerating_result = digital_bank_IPO_stage2
stage_failure_type = customer_count_and_IPO_size_not_aftermarket_NIM_green
```

---

## Case E — KakaoBank control risk via Kakao founder case `digital bank governance 4C-watch`

```text
symbols = 323410 / 035720
case_type = 4C-watch
archetype = DIGITAL_BANK_CONTROL_RISK_4C_WATCH
```

### stage date

```text
Stage 1:
2024-07-22
- Kakao founder Kim Beom-su warrant review.
- KakaoBank control risk enters financial-sector thesis.

Stage 4C-watch:
2024-07-23
- Kim arrested on suspected SM Entertainment stock manipulation.
- Kakao shares -3.4%, lowest since November.
- Kakao had fallen 24% YTD.
- Kim/affiliates control 24% Kakao stake.
- if convicted of financial crime, Kakao could lose ability to own more than 10% bank stake.
- KakaoBank control risk becomes explicit.

Stage 2 relief:
2025-10-21
- South Korean court clears Kim of stock manipulation charges, Yonhap via Reuters.
- prosecutors had sought 15-year jail term and 500M won fine.
- relief, but governance/control risk remains scoring gate.
```

KakaoBank는 digital bank라도 governance가 먼저다. Reuters는 Kakao founder Kim Beom-su 체포가 KakaoBank control을 위협할 수 있다고 보도했다. 한국 규정상 금융범죄로 유죄가 되면 은행 지분 10% 초과 보유가 제한될 수 있기 때문이다. Kakao shares는 체포 소식에 -3.4%였고, 2025년 10월 무죄 판결은 relief지만, digital bank scoring에는 founder/legal risk gate를 남겨야 한다. ([Reuters][5])

### 실제 가격경로 검증

```json
{
  "case_id": "r6_loop14_kakaobank_control_risk_kakao_founder",
  "symbols": "323410/035720",
  "stage4c_watch_date": "2024-07-23",
  "stage2_relief_date": "2025-10-21",
  "stage3_price": null,
  "price_data_source": "Reuters Kakao founder arrest / KakaoBank control-risk anchors",
  "kakao_event_mae_pct": -3.4,
  "kakao_ytd_decline_context_pct": -24,
  "founder_affiliated_stake_pct": 24,
  "bank_ownership_limit_if_financial_crime_conviction_pct": 10,
  "group_assets_krw_trn_context": 86,
  "prosecutor_sought_sentence_years": 15,
  "prosecutor_sought_fine_krw_mn": 500,
  "acquittal_relief": true,
  "kakaobank_direct_event_price": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break_watch_then_relief
rerating_result = digital_bank_control_risk_gate
stage_failure_type = fintech_bank_growth_not_green_without_ownership_regulatory_clearance
```

---

## Case F — Naver Financial / Dunamu / Upbit `digital asset M&A 4B → trust 4C-watch`

```text
symbol = 035420
case_type = event_premium + 4C-watch
archetype = DIGITAL_ASSET_MA_TRUST_4C_WATCH
```

### stage date

```text
Stage 1:
2025-11-27
- Naver Financial agrees to acquire Dunamu.
- digital-asset and fintech growth narrative becomes explicit.

Stage 2:
2025-11-27
- all-stock deal value: 15.13T won / $10.27B.
- exchange ratio: 2.54 Naver Financial shares per Dunamu share.
- Upbit is Korea’s largest crypto exchange with about 70% market share in some reports.
- strategic logic: user traffic, digital assets, stablecoin/fintech expansion.

Stage 4B:
2025-11-27
- Naver shares initially +7%+ after deal.

Stage 4C-watch:
2025-11-27
- Naver later trades -4.2%.
- abnormal withdrawal from Upbit: 54B won worth of cryptocurrencies.
- Upbit says it will cover loss with own assets.
- same-day swing: about -11.2pp from initial +7% to -4.2%.
```

Naver–Dunamu는 R6의 가장 중요한 digital-finance calibration이다. Deal size는 15.13T won으로 크고, Upbit는 국내 최대 crypto exchange다. 하지만 같은 날 abnormal withdrawal이 나오자 Naver 주가는 +7% 이상에서 -4.2%로 뒤집혔다. 즉 digital-finance M&A는 synergy보다 **custody/internal control/trust gate**가 먼저다. ([Reuters][6])

### 실제 가격경로 검증

```json
{
  "case_id": "r6_loop14_naver_financial_dunamu_upbit_trust_gate",
  "symbol": "035420",
  "stage2_date": "2025-11-27",
  "stage4b_date": "2025-11-27",
  "stage4c_watch_date": "2025-11-27",
  "stage3_price": null,
  "price_data_source": "Reuters Naver Financial-Dunamu deal and Upbit abnormal withdrawal anchor",
  "deal_value_krw_trn": 15.13,
  "deal_value_usd_bn": 10.27,
  "exchange_ratio_naver_financial_per_dunamu": 2.54,
  "upbit_market_share_context_pct": 70,
  "event_initial_mfe_pct": 7.0,
  "event_later_mae_pct": -4.2,
  "event_swing_pp": -11.2,
  "abnormal_withdrawal_krw_bn": 54,
  "loss_coverage": "Upbit_to_cover_using_own_assets",
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium_trust_watch
rerating_result = digital_asset_MA_stage2_4C_watch
stage_failure_type = deal_synergy_not_green_without_custody_internal_control
```

---

## Case G — Hana Bank / Dunamu stake `bank digital-asset Stage 2`

```text
symbol = 086790
case_type = success_candidate + custody/regulatory watch
archetype = BANK_DIGITAL_ASSET_STAKE_STAGE2
```

### stage date

```text
Stage 1:
2026-05-14 / 2026-05-15
- Hana Bank enters Dunamu shareholder base.
- large Korean bank digital-asset exposure becomes explicit.

Stage 2:
2026-05-14
- Hana Bank to acquire 1T won / about $700M stake in Dunamu.
- stake size: 6.55%.
- Kakao investment subsidiary sells the stake.
- Kakao Investment share in Dunamu falls to 4.03%.
- Upbit handles more than 80% of Korea virtual asset trading volume in Reuters context.

Stage 3:
없음
- bank digital-asset exposure is Stage 2.
- Green requires regulatory approval, custody-risk control, AML/KYC, revenue contribution, capital treatment.
```

Hana Bank의 Dunamu stake는 R6 금융권 digital-asset Stage 2다. Reuters는 Hana Bank가 Dunamu 지분 6.55%를 1T won에 인수한다고 보도했고, Dunamu의 Upbit가 한국 virtual asset market에서 80% 이상의 trading volume을 처리한다고 설명했다. 하지만 은행 입장에서는 단순 지분투자가 Green이 아니다. 규제승인, AML/KYC, custody risk, capital treatment, 실제 수익기여가 필요하다. ([Reuters][7])

### 실제 가격경로 검증

```json
{
  "case_id": "r6_loop14_hana_bank_dunamu_digital_asset_stake",
  "symbol": "086790",
  "stage2_date": "2026-05-14",
  "stage3_price": null,
  "price_data_source": "Reuters Hana Bank-Dunamu stake acquisition anchor",
  "stake_purchase_krw_trn": 1.0,
  "stake_purchase_usd_mn_context": 700,
  "dunamu_stake_acquired_pct": 6.55,
  "implied_dunamu_equity_value_krw_trn": 15.27,
  "kakao_investment_remaining_stake_pct": 4.03,
  "upbit_trading_volume_share_context_pct": 80,
  "direct_event_return": "price_data_unavailable_after_deep_search",
  "stage3_conditions": ["regulatory approval", "custody controls", "AML/KYC", "revenue contribution", "capital treatment"]
}
```

### alignment

```text
score_price_alignment = success_candidate_but_price_data_unavailable
rerating_result = bank_digital_asset_stake_stage2
stage_failure_type = strategic_crypto_stake_not_bank_EPS_green
```

---

## Case H — Samsung SDS / KKR CB / stablecoin optionality `event premium + 4B-watch`

```text
symbol = 018260
case_type = event_premium + 4B-watch
archetype = PRIVATE_CAPITAL_CB_STABLECOIN_EVENT_PREMIUM
```

### stage date

```text
Stage 1:
2026-04-15
- KKR invests in Samsung SDS via newly issued convertible bonds.
- AI infrastructure, global M&A, physical AI, stablecoins become capital-allocation narrative.

Stage 2:
2026-04-15
- KKR to buy $820M newly issued CB.
- Samsung SDS has existing cash and cash equivalents of 6.4T won / $4.35B.
- KKR to advise on M&A, capital allocation and full-stack AI.
- advisor role for six years.
- funds to support global growth, AI infrastructure, physical AI, stablecoins, M&A.

Stage 4B:
2026-04-15
- Samsung SDS shares +20.8% intraday.
- morning +19.4%.
- KOSPI +3.0%.
- relative outperformance about +17.8pp based on intraday high.
```

Samsung SDS는 R6의 자본배분/디지털금융 4B-watch case다. KKR CB는 credible capital-allocation catalyst지만, CB는 희석 가능성이 있고 “stablecoin”은 아직 매출이 아니다. Reuters는 KKR이 $820M CB를 인수하고, Samsung SDS가 AI infra, physical AI, stablecoins, M&A에 자금을 활용할 계획이라고 보도했다. 주가는 장중 +20.8%로 크게 뛰었지만, Stage 3는 실제 capital deployment, ROIC, dilution terms, stablecoin revenue가 확인된 후다. ([Reuters][8])

### 실제 가격경로 검증

```json
{
  "case_id": "r6_loop14_samsung_sds_kkr_cb_stablecoin_event",
  "symbol": "018260",
  "stage2_date": "2026-04-15",
  "stage4b_date": "2026-04-15",
  "stage3_price": null,
  "price_data_source": "Reuters KKR convertible-bond and Samsung SDS share reaction anchor",
  "kkr_cb_investment_usd_mn": 820,
  "kkr_cb_investment_krw_trn_context": 1.207,
  "cash_and_equivalents_krw_trn": 6.4,
  "cash_and_equivalents_usd_bn": 4.35,
  "advisor_period_years": 6,
  "event_intraday_mfe_pct": 20.8,
  "event_morning_mfe_pct": 19.4,
  "kospi_same_context_pct": 3.0,
  "relative_outperformance_intraday_pp": 17.8,
  "use_of_funds": ["global growth", "AI infrastructure", "physical AI", "stablecoins", "M&A"],
  "dilution_terms_fully_modelled": false,
  "stablecoin_revenue_confirmed": false
}
```

### alignment

```text
score_price_alignment = event_premium_4B_watch
rerating_result = private_capital_CB_digital_finance_option_stage2
stage_failure_type = PE_CB_stablecoin_headline_not_ROIC_revenue_green
```

---

# 5. 이번 R6 case별 stage date 요약

| case            | Stage 1   | Stage 2               | Stage 3 | Stage 4B                   | Stage 4C                        |
| --------------- | --------- | --------------------- | ------- | -------------------------- | ------------------------------- |
| 금융지주 Value-Up   | 2024~2025 | 2026-02-25 law        | N/A     | policy rerating watch      | credit-cost / CET1 watch        |
| SK Square       | 2024-11   | buyback/cancellation  | N/A     | Hynix stake discount watch | holdco governance watch         |
| Samsung C&T     | 2024-03   | activist proposal     | N/A     | Value-Up expectation       | 2024-03-15 proposal failure     |
| K Bank          | 2024-09   | IPO plan              | N/A     | IPO valuation watch        | aftermarket/credit-quality gate |
| KakaoBank       | 2024-07   | 2025 acquittal relief | N/A     | N/A                        | 2024 founder control-risk watch |
| Naver/Dunamu    | 2025-11   | all-stock M&A         | N/A     | +7% initial                | Upbit withdrawal / -4.2%        |
| Hana/Dunamu     | 2026-05   | 1T won stake          | N/A     | digital-asset bank premium | custody/regulatory watch        |
| Samsung SDS/KKR | 2026-04   | $820M CB              | N/A     | +20.8%                     | dilution/ROIC/stablecoin watch  |

---

# 6. 실제 가격경로 검증 총괄

| case          |                                          가격·거래 anchor | 해석                               | 판정                   |
| ------------- | ----------------------------------------------------: | -------------------------------- | -------------------- |
| 금융지주 Value-Up |                       treasury-share cancellation law | 정책 Stage 2, 개별 PBR/ROE 확인 필요     | success_candidate    |
| SK Square     | 200B won buyback/cancel plan, SK Hynix stake discount | holdco discount Stage 2          | success_candidate    |
| Samsung C&T   |         activist proposal failure, shares almost -10% | 주주환원 기대 false positive           | false_positive_score |
| K Bank        |                  IPO up to 984B won, valuation 5T won | digital bank IPO Stage 2         | IPO quality gate     |
| KakaoBank     |             Kakao -3.4%, bank ownership 10% rule risk | digital bank governance 4C-watch | thesis_break_watch   |
| Naver/Dunamu  |              +7% → -4.2%, 54B won abnormal withdrawal | M&A 4B then trust 4C-watch       | event_premium        |
| Hana/Dunamu   |                     1T won, 6.55%, implied 15.27T won | bank digital-asset Stage 2       | success_candidate    |
| Samsung SDS   |                         +20.8%, $820M CB, KOSPI +3.0% | PE/CB/stablecoin 4B-watch        | event_premium        |

---

# 7. score-price alignment 판정

```text
aligned:
- 없음. R6는 대부분 policy / capital allocation / digital-finance Stage 2.

structural_success_candidate:
- 금융지주 Value-Up basket, if CET1/payout/credit-cost execution confirms.
- SK Square, if repeated cancellation and holdco discount compression confirm.
- Hana Bank–Dunamu, if digital-asset revenue and custody/regulatory control confirm.

success_candidate:
- K Bank IPO.
- Samsung SDS KKR CB.
- Naver Financial–Dunamu, but trust gate attached.

false_positive_score:
- Samsung C&T activist proposal failure.
- Value-Up policy headline if treated as immediate payout execution.
- Samsung SDS if +20.8% is treated as ROIC/stablecoin revenue before deployment.

event_premium:
- Naver/Dunamu initial +7%.
- Samsung SDS/KKR +20.8%.
- Value-Up law and financial holding rerating, if price moves before payout execution.

price_moved_without_evidence:
- K Bank IPO valuation if treated as credit-quality Green.
- Hana/Dunamu stake if treated as bank EPS before regulatory/custody revenue.
- Samsung SDS stablecoin optionality before actual revenue.

thesis_break_watch:
- KakaoBank control risk.
- Upbit abnormal withdrawal / digital-asset custody.
- Samsung C&T governance failure.
- CB dilution / capital allocation risk.

hard_4C_confirmed:
- 없음.
```

---

# 8. 점수비중 교정

## 올릴 축

```text
CET1_capital_buffer +5
actual_payout_execution +5
treasury_share_cancellation +5
credit_cost_control +5
holdco_discount_compression +4
IPO_aftermarket_demand +5
digital_asset_custody_control +5
AML_KYC_regulatory_clearance +5
CB_dilution_adjusted_ROIC +5
minority_shareholder_alignment +5
```

### 왜 올리나

Samsung C&T는 activist proposal이 실패하자 거의 -10%가 나왔다. Naver/Dunamu는 15.13T won deal이 있어도 Upbit abnormal withdrawal 하나로 +7%에서 -4.2%로 뒤집혔다. Samsung SDS는 KKR CB와 stablecoin optionality만으로 +20.8%였지만, 실제 ROIC와 희석 조건이 닫혀야 한다. K Bank는 고객수와 IPO size가 좋아도 aftermarket demand와 credit quality를 통과해야 한다. 금융지주는 Value-Up law보다 CET1과 실제 소각·배당이 중요하다.

## 내릴 축

```text
Value_Up_headline_only -5
shareholder_return_proposal_only -5
announced_buyback_without_cancellation -5
IPO_size_or_customer_count_only -5
crypto_exchange_market_share_only -5
M&A_synergy_without_custody_control -5
CB_or_PE_investment_headline_only -5
stablecoin_keyword_without_revenue -5
founder_legal_risk_unresolved -5
```

### 왜 내리나

R6에서 가장 큰 함정은 “자본배분 개선 기대”를 실제 현금흐름처럼 취급하는 것이다. 자사주 매입은 소각되어야 가치가 생기고, IPO는 상장 후 가격이 검증해야 하며, 디지털자산은 거래량보다 custody와 internal control이 먼저다.

---

# 9. Green gate 강화 조건

```text
R6 Stage 3-Green 필수:
1. 금융지주는 CET1 buffer와 credit cost 안정 확인.
2. 배당/자사주는 발표가 아니라 실제 집행과 소각 확인.
3. holding company는 discount compression과 governance 개선 확인.
4. IPO는 고객수보다 aftermarket demand, NIM, credit quality 확인.
5. 디지털자산 M&A는 custody/internal control, AML/KYC, regulator approval 확인.
6. 은행의 crypto stake는 capital treatment와 revenue contribution 확인.
7. CB/PE 투자는 희석 조정 ROIC와 자금사용 성과 확인.
8. founder/legal risk가 은행 ownership에 영향을 주지 않는지 확인.
9. price path가 evidence 이후 따라옴.
```

---

# 10. 4B 조기감지 조건

```text
4B-watch:
- Value-Up law/policy로 금융지주 선반영.
- 자사주 매입 발표만으로 소각 전 급등.
- activist proposal 기대만으로 rally.
- digital-asset M&A 발표 직후 +5~10% 급등.
- PE/CB 투자 발표로 +15~20% 이상 급등.
- stablecoin/crypto keyword로 revenue 전 valuation 확장.
- IPO valuation이 고객수/MAU만으로 과대평가.
```

---

# 11. 4C hard gate 조건

```text
Hard 4C / strong watch:
- bank ownership loss due founder/financial-crime conviction.
- abnormal withdrawal / custody failure at digital-asset exchange.
- AML/KYC or regulatory rejection of crypto-finance deal.
- shareholder-return proposal failure after Value-Up rally.
- CB dilution without clear ROIC.
- credit-cost spike / PF or real-estate loan deterioration.
- CET1 buffer below payout requirement.
- IPO weak debut after aggressive pricing.
```

이번 R6 Loop 14에서는 직접 hard 4C는 확정하지 않는다. 대신 **Naver/Dunamu–Upbit abnormal withdrawal**, **KakaoBank control risk**, **Samsung C&T shareholder-return failure**, **Samsung SDS CB dilution/ROIC risk**를 strong 4C/4B watch로 둔다.

---

# 12. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 13. 레포 반영용 patch-ready 출력

## docs/round/round_216.md 요약

```md
# R6 Loop 14. Finance / Capital Allocation / Digital Finance Price Validation

이번 라운드는 R6 Loop 14 price-validation 라운드다.

핵심 결론:
- Financial holding Value-Up basket is policy Stage 2, not Green. Commercial Act revision requires newly acquired treasury shares to be cancelled within one year and gives existing treasury shares six-month grace. Bank Green requires CET1 buffer, actual payout/cancellation, credit cost and ROE/PBR rerating.
- SK Square is holdco-discount Stage 2. It will cancel 100B won shares bought in April and repurchase/cancel another 100B won within three months. It holds 20% of SK Hynix and trades at less than half of the $18B stake value context. Discount compression still needs execution.
- Samsung C&T is false_positive_score. Activist dividend/buyback proposals backed by large global investors failed; NPS sided with management; shares closed almost -10%.
- K Bank is digital-bank IPO Stage 2. IPO planned to raise up to 984B won, price range 9,500~12,000 won, valuation up to 5T won, H1 2024 OP 86.7B won and 10M+ customers. Aftermarket demand and credit quality required.
- KakaoBank is digital-bank governance 4C-watch. Kakao founder arrest made bank-control risk explicit because financial-crime convictions restrict bank stakes above 10%. Kakao -3.4%; later acquittal was relief.
- Naver Financial / Dunamu is digital-asset M&A Stage 2 plus trust 4C-watch. 15.13T won all-stock deal, exchange ratio 2.54, Naver initially +7% but later -4.2% after 54B won abnormal withdrawal from Upbit.
- Hana Bank / Dunamu is bank digital-asset Stage 2. 1T won stake for 6.55%, implied Dunamu value around 15.27T won; Upbit handles more than 80% of Korean virtual-asset trading volume in Reuters context. Custody, AML/KYC and capital treatment required.
- Samsung SDS / KKR CB is event premium plus 4B-watch. KKR buys $820M CB; shares +20.8% vs KOSPI +3.0%; use of funds includes AI infra, physical AI, stablecoins and M&A. ROIC, dilution terms and actual stablecoin revenue required.
```

## docs/checkpoints/checkpoint_28a_round216_r6_loop14.md 요약

```md
# Checkpoint 28A Round 216 R6 Loop 14 Finance Capital Allocation Digital Finance Price Validation

## 반영 내용
- R6 Loop 14 price-validation 라운드를 추가했다.
- Financial holding Value-Up basket, SK Square, Samsung C&T, K Bank, KakaoBank control risk, Naver/Dunamu, Hana/Dunamu, Samsung SDS/KKR CB를 비교했다.
- Reuters / FT / WSJ anchors로 가능한 event MFE/MAE, deal value, buyback amount, IPO range, CB value, ownership stake, regulatory restriction을 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- CET1 capital buffer, actual payout execution, treasury-share cancellation, credit-cost control, holdco discount compression, IPO aftermarket demand, digital-asset custody control, AML/KYC regulatory clearance, CB dilution-adjusted ROIC, minority-shareholder alignment 가중치 강화.
- Value-Up headline-only, shareholder-return proposal-only, announced buyback without cancellation, IPO size/customer count-only, crypto exchange market share-only, M&A synergy without custody control, CB/PE headline-only, stablecoin keyword without revenue 감점 강화.
```

## data/e2r_case_library/cases_r6_loop14_round216.jsonl 초안

```jsonl
{"case_id":"r6_loop14_financial_holding_value_up_policy_stage2","symbol":"105560/055550/086790/316140","company_name":"KB Financial / Shinhan Financial / Hana Financial / Woori Financial basket","case_type":"success_candidate_policy_stage2","primary_archetype":"VALUE_UP_FINANCIAL_HOLDING_STAGE2","stage2_date":"2026-02-25","price_validation":{"price_data_source":"Reuters/FT Commercial Act and Value-Up reform anchors","stage3_price":null,"treasury_share_new_cancellation_deadline_years":1,"existing_treasury_share_grace_period_months":6,"policy_goal":"Korea Discount reduction and minority shareholder protection","financial_holding_direct_event_prices":"price_data_unavailable_after_deep_search","stage3_conditions":["CET1 buffer","actual buyback cancellation","payout ratio","credit cost","ROE/PBR rerating"]},"score_price_alignment":"success_candidate_policy_stage2","rerating_result":"financial_holding_value_up_stage2","notes":"Policy reform is Stage 2; bank Green requires capital buffer, payout execution and credit-cost stability."}
{"case_id":"r6_loop14_sk_square_holdco_discount_buyback","symbol":"402340","company_name":"SK Square","case_type":"success_candidate_price_unavailable","primary_archetype":"HOLDCO_DISCOUNT_BUYBACK_STAGE2","stage2_date":"2024-11-21","price_validation":{"price_data_source":"Reuters SK Square buyback / activist / holdco discount anchor","stage3_price":null,"first_cancellation_krw_bn":100,"new_repurchase_and_cancellation_krw_bn":100,"total_announced_cancellation_related_krw_bn":200,"sk_hynix_stake_pct":20,"sk_hynix_stake_value_usd_bn_context":18,"market_value_vs_stake_value_context":"less_than_half","activist_stake_context_pct":1,"direct_event_return":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_price_data_unavailable","rerating_result":"holdco_discount_buyback_stage2","notes":"Buyback/cancellation is positive but holdco-discount compression and governance execution required."}
{"case_id":"r6_loop14_samsung_ct_activist_valueup_failure","symbol":"028260","company_name":"Samsung C&T","case_type":"false_positive_score","primary_archetype":"SHAREHOLDER_RETURN_FAILURE_FALSE_POSITIVE","stage4c_date":"2024-03-15_watch","price_validation":{"price_data_source":"FT activist proposal / share-price failure anchor","stage3_price":null,"event_mae_pct":-10.0,"activist_backers":["Norway oil fund","Canadian pension investors"],"nps_vote":"sided_with_management","proposal_type":["dividend increase","share buyback increase"],"proposal_passed":false,"stage3_conditions":["board adoption","payout execution","treasury-share cancellation","minority shareholder alignment"]},"score_price_alignment":"false_positive_score","rerating_result":"shareholder_return_proposal_failed","notes":"Value-Up/activist proposal is not Green unless actually adopted and executed."}
{"case_id":"r6_loop14_kbank_digital_bank_ipo_quality_gate","symbol":"unlisted_KBank_readthrough","company_name":"K Bank","case_type":"success_candidate_ipo_quality_gate","primary_archetype":"DIGITAL_BANK_IPO_QUALITY_GATE","stage2_date":"2024-09-10","price_validation":{"price_data_source":"Reuters K Bank IPO plan anchor","stage3_price":null,"ipo_raise_max_krw_bn":984,"ipo_raise_max_usd_mn":731.64,"shares_to_sell_mn":82,"new_shares_mn":41,"existing_shares_mn":41,"price_range_krw":"9500-12000","valuation_max_krw_trn":5,"h1_2024_operating_profit_krw_bn":86.7,"customer_count_context_mn":10,"price_validation_status":"unlisted_ipo_plan_no_aftermarket_ohlc"},"score_price_alignment":"success_candidate_IPO_quality_gate","rerating_result":"digital_bank_IPO_stage2","notes":"Customer count and IPO size need aftermarket demand, NIM, credit quality and CAC proof."}
{"case_id":"r6_loop14_kakaobank_control_risk_kakao_founder","symbol":"323410/035720","company_name":"KakaoBank / Kakao","case_type":"4c_watch_then_relief","primary_archetype":"DIGITAL_BANK_CONTROL_RISK_4C_WATCH","stage4c_date":"2024-07-23_watch","stage2_date":"2025-10-21_relief","price_validation":{"price_data_source":"Reuters Kakao founder arrest / KakaoBank control-risk anchors","stage3_price":null,"kakao_event_mae_pct":-3.4,"kakao_ytd_decline_context_pct":-24,"founder_affiliated_stake_pct":24,"bank_ownership_limit_if_financial_crime_conviction_pct":10,"group_assets_krw_trn_context":86,"prosecutor_sought_sentence_years":15,"prosecutor_sought_fine_krw_mn":500,"acquittal_relief":true,"kakaobank_direct_event_price":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch_then_relief","rerating_result":"digital_bank_control_risk_gate","notes":"Digital-bank growth is not Green without ownership/regulatory clearance."}
{"case_id":"r6_loop14_naver_financial_dunamu_upbit_trust_gate","symbol":"035420","company_name":"Naver Financial / Dunamu / Upbit","case_type":"event_premium_4c_watch","primary_archetype":"DIGITAL_ASSET_MA_TRUST_4C_WATCH","stage2_date":"2025-11-27","stage4b_date":"2025-11-27","stage4c_date":"2025-11-27_watch","price_validation":{"price_data_source":"Reuters Naver Financial-Dunamu deal and Upbit abnormal withdrawal anchor","stage3_price":null,"deal_value_krw_trn":15.13,"deal_value_usd_bn":10.27,"exchange_ratio_naver_financial_per_dunamu":2.54,"upbit_market_share_context_pct":70,"event_initial_mfe_pct":7.0,"event_later_mae_pct":-4.2,"event_swing_pp":-11.2,"abnormal_withdrawal_krw_bn":54,"loss_coverage":"Upbit_to_cover_using_own_assets","mfe_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_trust_watch","rerating_result":"digital_asset_MA_stage2_4C_watch","notes":"Deal synergy was immediately checked by custody/internal-control risk."}
{"case_id":"r6_loop14_hana_bank_dunamu_digital_asset_stake","symbol":"086790","company_name":"Hana Financial / Hana Bank / Dunamu","case_type":"success_candidate_price_unavailable","primary_archetype":"BANK_DIGITAL_ASSET_STAKE_STAGE2","stage2_date":"2026-05-14","price_validation":{"price_data_source":"Reuters Hana Bank-Dunamu stake acquisition anchor","stage3_price":null,"stake_purchase_krw_trn":1.0,"stake_purchase_usd_mn_context":700,"dunamu_stake_acquired_pct":6.55,"implied_dunamu_equity_value_krw_trn":15.27,"kakao_investment_remaining_stake_pct":4.03,"upbit_trading_volume_share_context_pct":80,"direct_event_return":"price_data_unavailable_after_deep_search","stage3_conditions":["regulatory approval","custody controls","AML/KYC","revenue contribution","capital treatment"]},"score_price_alignment":"success_candidate_but_price_data_unavailable","rerating_result":"bank_digital_asset_stake_stage2","notes":"Strategic crypto stake is not bank EPS Green until custody, regulatory and revenue gates clear."}
{"case_id":"r6_loop14_samsung_sds_kkr_cb_stablecoin_event","symbol":"018260","company_name":"Samsung SDS / KKR","case_type":"event_premium_4b_watch","primary_archetype":"PRIVATE_CAPITAL_CB_STABLECOIN_EVENT_PREMIUM","stage2_date":"2026-04-15","stage4b_date":"2026-04-15","price_validation":{"price_data_source":"Reuters KKR convertible-bond and Samsung SDS share reaction anchor","stage3_price":null,"kkr_cb_investment_usd_mn":820,"kkr_cb_investment_krw_trn_context":1.207,"cash_and_equivalents_krw_trn":6.4,"cash_and_equivalents_usd_bn":4.35,"advisor_period_years":6,"event_intraday_mfe_pct":20.8,"event_morning_mfe_pct":19.4,"kospi_same_context_pct":3.0,"relative_outperformance_intraday_pp":17.8,"use_of_funds":["global growth","AI infrastructure","physical AI","stablecoins","M&A"],"dilution_terms_fully_modelled":false,"stablecoin_revenue_confirmed":false},"score_price_alignment":"event_premium_4B_watch","rerating_result":"private_capital_CB_digital_finance_option_stage2","notes":"CB/KKR/stablecoin headline needs dilution-adjusted ROIC and real revenue."}
```

## data/sector_taxonomy/score_weight_profiles_round216_r6_loop14_v1.csv 초안

```csv
archetype,cet1_capital_buffer,actual_payout_execution,treasury_share_cancellation,credit_cost_control,holdco_discount_compression,ipo_aftermarket_demand,digital_asset_custody_control,aml_kyc_regulatory_clearance,cb_dilution_adjusted_roic,minority_shareholder_alignment,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
VALUE_UP_FINANCIAL_HOLDING_STAGE2,+5,+5,+5,+5,+2,+1,+0,+2,+1,+5,-5,+4,+4,Financial holding Green needs CET1, actual payout/cancellation and credit-cost stability.
HOLDCO_DISCOUNT_BUYBACK_STAGE2,+1,+5,+5,+1,+5,+0,+0,+1,+2,+5,-4,+4,+3,SK Square buyback is Stage 2 until discount compression and governance execution.
SHAREHOLDER_RETURN_FAILURE_FALSE_POSITIVE,+1,+5,+5,+1,+3,+0,+0,+1,+1,+5,0,+5,+4,Samsung C&T shows proposal failure can create false positives.
DIGITAL_BANK_IPO_QUALITY_GATE,+4,+1,+1,+5,+0,+5,+2,+5,+0,+3,-5,+5,+4,K Bank IPO needs credit quality, funding cost, NIM and aftermarket demand.
DIGITAL_BANK_CONTROL_RISK_4C_WATCH,+4,+2,+1,+4,+0,+2,+2,+5,+0,+5,0,+4,+5,KakaoBank control risk shows founder/legal gate for digital banks.
DIGITAL_ASSET_MA_TRUST_4C_WATCH,+2,+1,+1,+2,+0,+2,+5,+5,+1,+4,-5,+5,+5,Naver/Dunamu shows M&A premium can reverse on custody/internal-control risk.
BANK_DIGITAL_ASSET_STAKE_STAGE2,+4,+2,+1,+4,+0,+1,+5,+5,+2,+4,-5,+4,+5,Hana/Dunamu stake needs custody, AML/KYC, capital treatment and revenue bridge.
PRIVATE_CAPITAL_CB_STABLECOIN_EVENT_PREMIUM,+1,+2,+1,+1,+1,+2,+4,+4,+5,+4,-5,+5,+4,Samsung SDS/KKR CB needs dilution-adjusted ROIC and actual stablecoin/AI revenue.
```

---

# 이번 R6 Loop 14 결론

```text
1. 금융지주 Value-Up은 Stage 2다.
   법안과 제도는 좋지만, CET1·credit cost·실제 소각·배당이 Stage 3 조건이다.

2. SK Square는 holdco discount 축소 후보지만 아직 Stage 2다.
   buyback/cancellation은 좋지만 discount compression과 governance execution이 필요하다.

3. Samsung C&T는 false_positive_score다.
   activist proposal이 실패하자 주가가 거의 -10%였고, Value-Up 기대만으로 Green을 주면 안 된다.

4. K Bank는 digital bank IPO Stage 2다.
   고객 10M명과 IPO 규모가 아니라 aftermarket demand, NIM, credit quality가 Green 조건이다.

5. KakaoBank는 digital bank governance 4C-watch다.
   founder legal risk가 은행 ownership rule과 연결되면 digital bank thesis가 바로 흔들린다.

6. Naver/Dunamu는 digital-asset M&A 4B → trust 4C-watch다.
   +7% initial reaction이 Upbit abnormal withdrawal로 -4.2%까지 뒤집혔다.

7. Hana Bank/Dunamu는 은행 digital-asset Stage 2다.
   1T won 지분투자는 좋지만 custody, AML/KYC, capital treatment, revenue bridge가 필요하다.

8. Samsung SDS/KKR CB는 capital-allocation event premium이다.
   +20.8% 급등은 4B-watch이고, stablecoin keyword보다 희석 조정 ROIC가 중요하다.
```

한 문장으로 압축하면:

> **R6에서 진짜 Stage 3는 “Value-Up·자사주·IPO·가상자산·스테이블코인·PE 투자 뉴스가 좋다”가 아니라, CET1·실제 소각·credit cost·aftermarket demand·custody control·AML/KYC·희석 조정 ROIC·minority alignment가 숫자로 닫히는 순간이다.**

[1]: https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-parliament-approves-commercial-act-revision-aimed-boosting-share-2026-02-25/?utm_source=chatgpt.com "South Korea parliament approves commercial act revision aimed at boosting share valuations"
[2]: https://www.reuters.com/technology/artificial-intelligence/south-koreas-ai-chip-investor-announces-plan-share-buybacks-2024-11-21/?utm_source=chatgpt.com "South Korea's AI chip investor announces plan for share buybacks"
[3]: https://www.ft.com/content/647fe2ef-9b01-4ab9-a93b-15b18f474563?utm_source=chatgpt.com "Samsung quashes activist proposals backed by Norway's oil fund"
[4]: https://www.reuters.com/markets/asia/south-koreas-k-bank-announces-ipo-plan-worth-up-732-million-2024-09-10/?utm_source=chatgpt.com "South Korea's K Bank announces IPO plan worth up to $732 million"
[5]: https://www.reuters.com/technology/south-korean-court-approves-arrest-warrant-kakao-founder-2024-07-22/?utm_source=chatgpt.com "Founder of South Korea's Kakao arrested for suspected stock manipulation"
[6]: https://www.reuters.com/world/asia-pacific/navers-payment-arm-acquire-south-korean-crypto-exchange-operator-10-bln-deal-2025-11-27/?utm_source=chatgpt.com "Naver's payment arm to acquire South Korean crypto exchange operator in $10 bln deal"
[7]: https://www.reuters.com/world/asia-pacific/hana-bank-acquire-stake-dunamu-700-mln-filing-says-2026-05-14/?utm_source=chatgpt.com "Hana Bank to acquire stake in Dunamu for $700 mln, filing says"
[8]: https://www.reuters.com/world/asia-pacific/kkr-buy-820-million-samsung-sds-convertible-bonds-shares-jump-20-2026-04-15/?utm_source=chatgpt.com "KKR to buy $820 million of Samsung SDS convertible bonds, shares jump 20%"

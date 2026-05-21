순서상 이번은 **R13 Loop 13 — Cross-archetype RedTeam / 4B / 회계·신뢰도 / 가격검증 총정리 라운드**다.

```text
round = R13 Loop 13
round_id = round_210
large_sector = CROSS_ARCHETYPE_REDTEAM_4B_ACCOUNTING_TRUST_PRICE_VALIDATION
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true
next_round = R1 Loop 14
```

이번 R13은 새 archetype을 늘리는 라운드가 아니라, R1~R12에서 반복적으로 드러난 **점수표의 약점**을 잡는 라운드다. 핵심은 “좋은 뉴스”가 아니라 **좋은 뉴스가 실제 가격경로와 현금흐름으로 닫혔는가**, 그리고 **어떤 gate가 깨지면 한순간에 thesis가 끊겼는가**다.

이번에도 KRX/Naver/Yahoo/Stooq의 수정주가 일봉 전체 구간은 안정적으로 확보하지 못했다. 따라서 30D/90D/180D/1Y full MFE·MAE는 만들지 않고, Reuters/WSJ가 보도한 **event price, event return, deal value, IPO price, fine, revenue-cut, market-cap wipeout, contract-collapse value**를 가격 anchor로 사용했다. full adjusted OHLC가 필요한 칸은 `price_data_unavailable_after_deep_search`로 명시한다.

---

# 1. 이번 라운드 대섹터

```text
R13 = Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증
```

R13에서 보는 핵심 질문은 하나다.

> “Stage 3처럼 보였던 사건이 실제로는 4B, false positive, trust break, accounting/control risk, policy premium, IPO premium, order headline이 아니었나?”

---

# 2. 대상 canonical archetype

```text
CYBERSECURITY_TRUST_HARD_4C
AVIATION_SAFETY_HARD_4C
CONTRACT_VALUE_COLLAPSE_HARD_4C
DIGITAL_ASSET_TRUST_4C_WATCH
IPO_QUALITY_GATE_FALSE_POSITIVE
CONTROL_PREMIUM_DILUTION_4B
ORDER_HEADLINE_NOT_MARGIN_GREEN
CAPITAL_RECYCLING_IPO_FAILED_RERATING
```

---

# 3. deep sub-archetype

```text
Trust break:
- SK Telecom data breach
- Upbit abnormal withdrawal
- Coupang-type service trust reference

Safety hard gate:
- Jeju Air fatal crash
- construction / battery / aviation safety as sector-wide hard gate

Contract quality:
- L&F / Tesla 4680 cathode contract collapse
- customer-name headline vs actual call-off

IPO quality:
- LG CNS AI/cloud IPO weak debut
- Hyundai Motor India weak debut
- valuation vs post-listing demand

Control / governance:
- Korea Zinc tender offer
- new-share issue / dilution / alleged accounting-fraud investigation
- management-control premium vs shareholder dilution

Order headline:
- Samsung E&A Fadhili mega EPC order
- order value vs EPC margin / working capital / completion risk
```

---

# 4. 국장 신규 후보 case

## Case A — SK Telecom data breach `hard 4C`

```text
symbol = 017670
case_type = hard_4C
archetype = CYBERSECURITY_TRUST_HARD_4C
```

### stage date

```text
Stage 1:
2025-04-18
- SK Telecom detects malware-linked customer-data leak.
- USIM / subscriber identity trust becomes core issue.

Stage 4C:
2025-04-28
- SK Telecom shares fall as much as -8.5%.
- close -6.7%, while KOSPI +0.1%.
- 23M users offered free USIM replacement.
- more than 2,600 retail stores used for replacement.
- 5.54M users signed up for USIM Protection Service.

Stage 4C validation:
2025-07-04
- 26.96M pieces of user data leaked.
- shares close -5.6%.
- 700B won five-year data-protection investment.
- 50% August bill discount for 24M customers.
- 2025 revenue forecast cut by 800B won.
- customer-benefit package cost around 500B won.

Stage 4C legal/financial validation:
2025-08-28
- Personal Information Protection Commission fines SK Telecom about 134B won.
```

이 case는 R13의 가장 중요한 hard 4C다. 단순 보안사고가 아니라 **매출전망 하향, 보상비용, 보안투자, 과징금, 고객 신뢰 훼손**으로 바로 연결됐다. SKT는 4월 disclosure 이후 장중 -8.5%, 종가 -6.7%였고, 7월 조사결과 이후에도 -5.6% 하락했다. 이후 134B won 과징금이 확정됐다. ([Reuters][1])

### 실제 가격경로 검증

```json
{
  "case_id": "r13_loop13_skt_cybersecurity_hard_4c",
  "symbol": "017670",
  "stage3_price": null,
  "stage4c_date": "2025-04-28",
  "price_data_source": "Reuters event-return anchors",
  "initial_intraday_mae_pct": -8.5,
  "initial_close_mae_pct": -6.7,
  "kospi_same_context_pct": 0.1,
  "relative_underperformance_initial_pp": -6.8,
  "usim_replacement_users_mn": 23,
  "retail_stores_involved": 2600,
  "usim_protection_service_signups_mn": 5.54,
  "leaked_data_pieces_mn": 26.96,
  "july_event_close_mae_pct": -5.6,
  "data_protection_investment_krw_bn": 700,
  "revenue_forecast_cut_krw_bn": 800,
  "customer_benefit_package_cost_krw_bn": 500,
  "pipc_fine_krw_bn": 134,
  "mfe_30d_90d": "N/A_after_4C",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break
stage_result = hard_4C_successfully_identified
calibration = data_trust / cybersecurity_internal_control must be hard gate
```

---

## Case B — Jeju Air crash `hard 4C`

```text
symbol = 089590
case_type = hard_4C
archetype = AVIATION_SAFETY_HARD_4C
```

### stage date

```text
Stage 1:
2024-12-29
- Jeju Air crash at Muan International Airport.
- deadliest aviation accident in South Korea.

Stage 4C:
2024-12-30
- 179 deaths.
- Jeju Air shares fall as much as -15.7%.
- event low 6,920 won.
- market-cap wipeout up to 95.7B won / $65.2M.
- AK Holdings -12%.
- government orders emergency safety inspection of full airline operation system.
```

Jeju Air는 안전 hard 4C다. 항공·건설·배터리·의료기기처럼 safety trust가 제품 그 자체인 산업에서는, demand나 capacity보다 **사망사고 / 안전조사 / 운영 신뢰**가 먼저다. Jeju Air는 사고 다음 거래일 장중 -15.7%까지 빠졌고, 시총 95.7B won이 증발했다. ([Reuters][2])

### 실제 가격경로 검증

```json
{
  "case_id": "r13_loop13_jeju_air_safety_hard_4c",
  "symbol": "089590",
  "stage3_price": null,
  "stage4c_date": "2024-12-30",
  "price_data_source": "Reuters event-price anchor",
  "fatalities": 179,
  "event_low_price_krw": 6920,
  "event_intraday_mae_pct": -15.7,
  "event_midday_mae_pct": -8.5,
  "market_cap_wipeout_krw_bn": 95.7,
  "market_cap_wipeout_usd_mn": 65.2,
  "ak_holdings_mae_pct": -12,
  "mfe": "N/A_after_4C",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break
stage_result = hard_4C_successfully_identified
calibration = fatal safety event must override demand/capacity score
```

---

## Case C — L&F / Tesla 4680 cathode `contract-collapse hard 4C`

```text
symbol = 066970
case_type = hard_4C
archetype = CONTRACT_VALUE_COLLAPSE_HARD_4C
```

### stage date

```text
Stage 1:
2023-02
- L&F signs cathode-material supply deal with Tesla and affiliates.
- market links deal to Tesla 4680 battery ramp.

Stage 2:
2023-02
- initially projected value: $2.9B.
- supply period: January 2024 to December 2025.
- customer-name headline was strong.

Stage 4C:
2025-12-29
- contract value cut to $7,386.
- Tesla 4680 ramp struggled.
- EV demand slowed.
- Tesla did not need as much cathode material as expected.

Stage 3:
없음
- customer-name contract never became actual call-off / revenue.
```

이 case는 “고객명이 Tesla면 Stage 3”라는 scoring을 박살낸다. L&F의 Tesla 계약은 처음 $2.9B로 기대됐지만, 실제 공시 수정 후 가치는 $7,386로 사실상 0에 가까워졌다. 계약 headline과 실제 call-off는 전혀 다른 층위다. ([Reuters][3])

### 실제 가격경로 검증

```json
{
  "case_id": "r13_loop13_lnf_tesla_contract_collapse",
  "symbol": "066970",
  "stage3_price": null,
  "stage4c_date": "2025-12-29",
  "price_data_source": "Reuters contract-collapse anchor",
  "initial_contract_projection_usd_bn": 2.9,
  "revised_contract_value_usd": 7386,
  "contract_value_collapse_pct": -99.9997,
  "supply_period": "2024-01_to_2025-12",
  "customer": "Tesla and affiliates",
  "application_context": "4680 high-nickel cathode materials",
  "mfe": "N/A_no_valid_stage3",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break
stage_result = hard_4C_successfully_identified
calibration = signed contract value without call-off must not become Green
```

---

## Case D — Naver Financial / Dunamu / Upbit `digital trust 4C-watch`

```text
symbol = 035420
case_type = event_premium + 4C-watch
archetype = DIGITAL_ASSET_TRUST_4C_WATCH
```

### stage date

```text
Stage 1:
2025-11-27
- Naver Financial agrees to acquire Dunamu.
- digital-asset / fintech expansion narrative.

Stage 2:
2025-11-27
- all-stock deal value: 15.13T won / $10.27B.
- exchange ratio: 2.54 Naver Financial shares per one Dunamu share.
- Upbit has about 70% crypto-exchange market share in Korea in source context.

Stage 4B:
2025-11-27
- Naver shares initially +7%+.

Stage 4C-watch:
2025-11-27
- Naver later trades -4.2%.
- abnormal withdrawal from Upbit: 54B won worth of cryptocurrencies.
- Upbit says it will cover the loss using own assets.

Stage 3:
없음
- M&A announcement is not Green until closing, regulatory approval, custody/security trust and earnings bridge.
```

이 case는 R13에서 “디지털 금융은 deal보다 trust가 먼저”라는 교정값이다. Naver는 Dunamu 인수 발표 직후 +7% 이상 올랐지만, 같은 날 Upbit abnormal withdrawal 소식으로 -4.2%까지 뒤집혔다. 이 11.2pp swing은 digital-asset M&A의 핵심 gate가 synergy가 아니라 **custody / internal control / exchange trust**라는 증거다. ([Reuters][4])

### 실제 가격경로 검증

```json
{
  "case_id": "r13_loop13_naver_dunamu_upbit_trust_gate",
  "symbol": "035420",
  "stage3_price": null,
  "stage2_date": "2025-11-27",
  "stage4b_date": "2025-11-27",
  "stage4c_watch_date": "2025-11-27",
  "price_data_source": "Reuters deal and abnormal-withdrawal anchor",
  "deal_value_krw_trn": 15.13,
  "deal_value_usd_bn": 10.27,
  "exchange_ratio_naver_financial_per_dunamu": 2.54,
  "upbit_market_share_pct": 70,
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
stage_result = 4B_then_4C_watch_successfully_identified
calibration = digital_asset deal value must be discounted by custody/internal-control risk
```

---

## Case E — LG CNS IPO `evidence_good_but_price_failed`

```text
symbol = 064400
case_type = evidence_good_but_price_failed
archetype = IPO_QUALITY_GATE_FALSE_POSITIVE
```

### stage date

```text
Stage 1:
2025-01
- LG CNS IPO.
- AI/cloud IT-service growth narrative.

Stage 2:
2025-02-05
- IPO price: 61,900 won.
- opened at 60,500 won.
- traded at 59,700 won in morning.
- IPO raised 1.2T won / $827.1M.
- market valuation around 5.79T won.
- retail oversubscription nearly 123x.
- institutional bids worth 76T won.
- cloud and AI were 54% of 9M 2024 sales.
- 9M 2024 revenue about 4T won, OP 313B won.

Stage 3:
없음
- AI/cloud evidence was real, but IPO price failed.
```

LG CNS는 “좋은 사업지표가 있어도 IPO valuation이 비싸면 바로 Green이 아니다”라는 case다. cloud/AI가 매출의 54%였고 9M OP도 313B won이었지만, 상장 첫날 issue price 61,900원 아래인 59,700원에 거래됐다. evidence가 좋아도 price가 못 받으면 `evidence_good_but_price_failed`로 둬야 한다. ([Reuters][5])

### 실제 가격경로 검증

```json
{
  "case_id": "r13_loop13_lg_cns_ipo_quality_gate",
  "symbol": "064400",
  "stage3_price": null,
  "stage2_date": "2025-02-05",
  "price_data_source": "Reuters IPO/debut anchor",
  "ipo_price_krw": 61900,
  "open_price_krw": 60500,
  "morning_trading_price_krw": 59700,
  "debut_mae_vs_ipo_pct": -3.23,
  "ipo_raise_krw_trn": 1.2,
  "ipo_raise_usd_mn": 827.1,
  "market_valuation_morning_krw_trn": 5.79,
  "retail_oversubscription_multiple": 123,
  "institutional_bids_krw_trn": 76,
  "cloud_ai_sales_share_9m2024_pct": 54,
  "revenue_9m2024_krw_trn": 4.0,
  "op_9m2024_krw_bn": 313,
  "op_margin_9m2024_pct": 7.8,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = evidence_good_but_price_failed
stage_result = false_positive_prevented_if_IPO_quality_gate_applied
calibration = AI/cloud keyword must be tied to recurring margin and aftermarket demand
```

---

## Case F — Korea Zinc control premium / dilution `4B governance watch`

```text
symbol = 010130
case_type = 4B-watch + governance/dilution watch
archetype = CONTROL_PREMIUM_DILUTION_4B
```

### stage date

```text
Stage 1:
2024-09-13
- MBK Partners + Young Poong tender offer.
- Korea Zinc control premium.
- critical minerals / nonferrous metal strategic value.

Stage 2:
2024-09-13
- tender offer value: 2T won / $1.5B.
- offer price: 660,000 won.
- offer targets 6.98%~14.61% stake.
- Korea Zinc shares +19.8% in Reuters source.
- WSJ source: shares as much as +24% to 690,000 won.

Stage 4B:
2024-09-13
- control premium repriced stock before operating Green.

Stage 4C-watch:
2024-10-31
- regulator investigates Korea Zinc’s $1.8B new-share issuance plan.
- shares had plunged after share-issue announcement.
- regulator also said it was looking into alleged accounting fraud and whether to launch formal investigation.
```

Korea Zinc는 R13의 governance calibration이다. control premium은 강력하지만, 그 자체가 operating Stage 3는 아니다. 오히려 tender offer → buyback → new-share issue → regulator investigation → alleged accounting-fraud review로 이어지며, **governance / dilution / accounting trust**가 4B 이후 바로 핵심 gate가 됐다. ([Reuters][6])

### 실제 가격경로 검증

```json
{
  "case_id": "r13_loop13_korea_zinc_control_premium_dilution_watch",
  "symbol": "010130",
  "stage3_price": null,
  "stage2_date": "2024-09-13",
  "stage4b_date": "2024-09-13",
  "stage4c_watch_date": "2024-10-31",
  "price_data_source": "Reuters/WSJ tender-offer and share-issue investigation anchors",
  "tender_offer_value_krw_trn": 2.0,
  "tender_offer_value_usd_bn": 1.5,
  "offer_price_krw": 660000,
  "prior_close_krw": 556000,
  "reuters_event_mfe_pct": 19.8,
  "wsj_event_mfe_pct": 24.0,
  "wsj_event_high_price_krw": 690000,
  "target_stake_min_pct": 6.98,
  "target_stake_max_pct": 14.61,
  "new_share_issue_plan_usd_bn": 1.8,
  "accounting_fraud_review_flag": true,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium_4B_watch
stage_result = 4B_watch_successfully_identified
calibration = control premium must be separated from operating cashflow and dilution/accounting risk
```

---

## Case G — Samsung E&A Fadhili mega-order `order headline not Green`

```text
symbol = 028050
case_type = success_candidate + event_premium
archetype = ORDER_HEADLINE_NOT_MARGIN_GREEN
```

### stage date

```text
Stage 1:
2024-04-02
- Saudi Aramco Fadhili gas expansion.
- Korean EPC mega-order cycle.

Stage 2:
2024-04-03
- Samsung E&A signs around $6B contract.
- part of Aramco’s $7.7B Fadhili expansion.
- Fadhili gas-processing capacity to rise 60% to 4B cubic feet/day.
- sulphur production +2,300 metric tons/day.
- completion due November 2027.

Stage 4B:
2024-04-03
- Samsung E&A shares +8.5% to 26,750 won.
- KOSPI -1.4%.
- target price 35,000 won.

Stage 3:
없음
- order headline is Stage 2.
- EPC Green requires cost control, variation order, working capital, unbilled receivables, completion margin.
```

Samsung E&A는 “수주 = Stage 3”가 아니라는 R13 교정 case다. $6B 계약과 +8.5% event return은 강하지만, EPC는 수주 다음부터 risk가 시작된다. 원가율, 설계변경, 미청구공사, cash collection이 닫혀야 Green이다. ([월스트리트저널][7])

### 실제 가격경로 검증

```json
{
  "case_id": "r13_loop13_samsung_ena_fadhili_order_not_margin_green",
  "symbol": "028050",
  "stage3_price": null,
  "stage2_date": "2024-04-03",
  "price_data_source": "WSJ/Aramco contract event anchor",
  "contract_value_usd_bn": 6.0,
  "project_total_value_usd_bn": 7.7,
  "samsung_contract_share_of_total_pct": 77.9,
  "event_price_krw": 26750,
  "event_mfe_pct": 8.5,
  "kospi_same_context_pct": -1.4,
  "relative_outperformance_pp": 9.9,
  "target_price_krw": 35000,
  "target_upside_from_event_price_pct": 30.8,
  "capacity_increase_pct": 60,
  "completion_target": "2027-11",
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium_success_candidate
stage_result = Stage2_valid_but_not_Stage3
calibration = backlog/order score must be gated by EPC margin and working-capital score
```

---

## Case H — Hyundai Motor India IPO `failed rerating`

```text
symbol = 005380 / HYUN.NS
case_type = failed_rerating
archetype = CAPITAL_RECYCLING_IPO_FAILED_RERATING
```

### stage date

```text
Stage 1:
2024-10
- Hyundai Motor India IPO.
- India growth / SUV portfolio / capital recycling narrative.

Stage 2:
2024-10-14
- $3.3B IPO.
- parent sells 17.5% stake.
- target valuation $19B.
- Hyundai India market share 15%.
- IPO oversubscribed more than 2x.

Stage 4C-watch / failed debut:
2024-10-22
- offer price 1,960 rupees.
- listed at 1,934 rupees.
- traded at 1,882.10 rupees.
- dropped as much as -6% on debut.
- valuation 1.53T rupees / $18.2B, below target.
```

Hyundai India IPO는 capital recycling이지만, 가격경로는 failed rerating이다. IPO 규모가 크고 India 성장 narrative가 있어도, offer price가 비싸면 debut에서 바로 깨진다. 모회사 Green은 IPO 자체가 아니라 proceeds use, India margin, SUV mix, shareholder return bridge로 확인해야 한다. ([Reuters][8])

### 실제 가격경로 검증

```json
{
  "case_id": "r13_loop13_hyundai_india_ipo_failed_rerating",
  "symbol": "005380/HYUN.NS",
  "stage3_price": null,
  "stage2_date": "2024-10-14",
  "stage4c_watch_date": "2024-10-22",
  "price_data_source": "Reuters IPO/debut anchor",
  "ipo_value_usd_bn": 3.3,
  "parent_stake_sale_pct": 17.5,
  "target_valuation_usd_bn": 19,
  "offer_price_inr": 1960,
  "listing_price_inr": 1934,
  "morning_trade_price_inr": 1882.10,
  "listing_discount_pct": -1.33,
  "debut_mae_pct": -6.0,
  "valuation_debut_inr_trn": 1.53,
  "valuation_debut_usd_bn": 18.2,
  "market_share_india_pct": 15,
  "ipo_oversubscription": "more_than_2x",
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = failed_rerating
stage_result = IPO_quality_gate_needed
calibration = capital recycling / IPO size must be gated by aftermarket demand and parent ROI bridge
```

---

# 5. 이번 R13 case별 stage date 요약

| case              | Stage 1       | Stage 2           | Stage 3 | Stage 4B         | Stage 4C                  |
| ----------------- | ------------- | ----------------- | ------- | ---------------- | ------------------------- |
| SK Telecom        | 2025-04-18    | remediation       | N/A     | N/A              | 2025-04/07/08 hard        |
| Jeju Air          | 2024-12-29    | N/A               | N/A     | N/A              | 2024-12-30 hard           |
| L&F / Tesla       | 2023 contract | 2023 headline     | N/A     | N/A              | 2025-12-29 hard           |
| Naver/Dunamu      | 2025-11-27    | 2025-11-27        | N/A     | 2025-11-27 +7%   | 2025-11-27 watch          |
| LG CNS            | 2025-01       | 2025-02-05        | N/A     | IPO demand watch | debut failure             |
| Korea Zinc        | 2024-09-13    | tender offer      | N/A     | +19.8%~+24%      | dilution/accounting watch |
| Samsung E&A       | 2024-04-02    | $6B Fadhili order | N/A     | +8.5%            | EPC margin watch          |
| Hyundai India IPO | 2024-10       | $3.3B IPO         | N/A     | valuation watch  | debut -6%                 |

---

# 6. 실제 가격경로 검증 총괄

| case          |                                            가격 anchor | 해석                                          | 판정                             |
| ------------- | ---------------------------------------------------: | ------------------------------------------- | ------------------------------ |
| SK Telecom    |  -8.5% intraday, -6.7% close, -5.6% later, 134B fine | trust break가 매출·비용·과징금으로 연결                 | hard_4C                        |
| Jeju Air      |                 -15.7%, 6,920 won, 95.7B won wipeout | fatal safety event                          | hard_4C                        |
| L&F           |                                       $2.9B → $7,386 | customer-name contract collapse             | hard_4C                        |
| Naver/Dunamu  |             +7% → -4.2%, 54B won abnormal withdrawal | M&A premium이 trust gate에 뒤집힘                | 4C-watch                       |
| LG CNS        |                              61,900 → 59,700, -3.23% | AI/cloud evidence good but IPO price failed | evidence_good_but_price_failed |
| Korea Zinc    | +19.8%~+24%, later dilution/accounting investigation | control premium 4B, governance gate         | 4B-watch                       |
| Samsung E&A   |                                   +8.5%, KOSPI -1.4% | order event premium, margin 미확인             | success_candidate              |
| Hyundai India |                                        IPO debut -6% | capital recycling valuation failed          | failed_rerating                |

---

# 7. score-price alignment 판정

```text
aligned:
- 없음. R13은 성공 검증보다 RedTeam 라운드.

false_positive_score:
- LG CNS, if AI/cloud mix was scored as Green before aftermarket demand.
- Hyundai India IPO, if capital recycling was scored as parent Green before listing response.
- Samsung E&A, if order headline was scored as Stage 3 without EPC margin/cashflow.

price_moved_without_evidence:
- Korea Zinc control premium before operating cashflow.
- Naver/Dunamu M&A premium before exchange trust.
- Samsung E&A order reaction before project cash collection.

evidence_good_but_price_failed:
- LG CNS.
- Hyundai India IPO.
- Naver/Dunamu after abnormal withdrawal.

event_premium:
- Korea Zinc tender.
- Samsung E&A Fadhili.
- Naver/Dunamu initial M&A reaction.

thesis_break:
- SK Telecom.
- Jeju Air.
- L&F / Tesla contract collapse.

thesis_break_watch:
- Korea Zinc dilution/accounting investigation.
- Naver/Dunamu / Upbit trust.
- Samsung E&A EPC margin/working capital.

hard_4C_confirmed:
- SK Telecom cybersecurity trust break.
- Jeju Air fatal safety event.
- L&F contract-value collapse.
```

---

# 8. 점수비중 교정

## 올릴 축

```text
trust_and_internal_control +5
fatal_safety_event +5
actual_calloff_vs_contract +5
custody_and_digital_asset_control +5
aftermarket_IPO_demand +5
governance_dilution_control +5
accounting_investigation_flag +5
project_margin_cash_conversion +5
working_capital_unbilled_receivables +5
parent_ROI_bridge +4
```

### 왜 올리나

SKT는 trust/internal control이 매출·비용·과징금까지 직접 연결됐다. Jeju Air는 safety가 demand보다 먼저라는 hard gate를 확정했다. L&F는 contract value가 실제 call-off로 닫히지 않으면 고객명 자체가 무의미하다는 증거다. Korea Zinc는 control premium이 있어도 dilution/accounting investigation이 붙으면 4B다. Samsung E&A는 order headline 뒤에 working capital과 EPC margin을 봐야 한다. Hyundai India와 LG CNS는 IPO demand가 valuation quality를 바로 드러낸다.

## 내릴 축

```text
customer_name_headline_only -5
order_backlog_headline_only -5
IPO_size_or_oversubscription_only -5
control_premium_only -5
M&A_synergy_before_trust -5
AI_cloud_keyword_without_aftermarket_demand -5
governance_fight_or_dilution -5
accounting_fraud_review -5
safety_or_data_trust_unresolved -5
```

### 왜 내리나

이번 R13의 공통 패턴은 “좋은 단어가 주가를 먼저 밀었지만, 하부 gate가 닫히지 않았다”는 것이다. Tesla, AI/cloud, M&A, tender offer, mega-order, India IPO 같은 단어는 Stage 2를 만들 수는 있지만, Stage 3는 만들지 못한다. Stage 3는 현금흐름과 신뢰가 닫힐 때만 줘야 한다.

---

# 9. Green gate 강화 조건

```text
Cross-sector Stage 3-Green 필수:
1. 고객명 / 계약금액이 아니라 실제 call-off / shipment / revenue recognition 확인.
2. IPO는 공모가가 아니라 상장 후 수요와 aftermarket price 확인.
3. M&A는 deal value가 아니라 closing, regulatory approval, integration, trust 확인.
4. 수주는 backlog가 아니라 project margin, working capital, cash collection 확인.
5. 플랫폼/통신/금융은 data trust, custody, internal control 확인.
6. 항공/건설/배터리는 safety event absence 확인.
7. governance case는 dilution, control premium, accounting investigation flag 확인.
8. price path가 evidence 이후 따라오는지 확인.
```

---

# 10. 4B 조기감지 조건

```text
4B-watch trigger:
- tender/control premium으로 +15~25% 급등
- IPO oversubscription 또는 대형 IPO headline 후 공모가 부근 과열
- mega-order 발표일 +5~10% 급등
- M&A 발표 직후 +5% 이상 급등
- AI/cloud/stablecoin/robotics/customer-name headline로 revenue bridge 전 급등
- contract value가 크지만 actual call-off가 불명확
- management-control fight / new-share issue / dilution risk가 동반됨
```

---

# 11. 4C hard gate 조건

```text
Hard 4C trigger:
- data breach with revenue/fine/compensation impact
- fatal safety event
- contract value collapse / customer program cancellation
- abnormal withdrawal / custody failure in digital asset platform
- accounting-fraud investigation or serious disclosure-control failure
- dilutive issuance after control-premium rally
- IPO debut failure after valuation-heavy bookbuilding
- EPC cost overrun / unbilled receivables / working-capital stress
```

이번 R13에서 hard 4C는 **SK Telecom, Jeju Air, L&F**로 확정한다. Korea Zinc, Naver/Dunamu, Samsung E&A, LG CNS, Hyundai India는 hard 4C가 아니라 **4B/false-positive/quality-gate calibration row**로 둔다.

---

# 12. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 13. 레포 반영용 patch-ready 출력

## docs/round/round_210.md 요약

```md
# R13 Loop 13. Cross-archetype RedTeam / 4B / Accounting Trust / Price Validation

이번 라운드는 R13 Loop 13 cross-archetype RedTeam 라운드다.

핵심 결론:
- SK Telecom is hard 4C. Data breach drove shares -8.5% intraday and -6.7% close versus KOSPI +0.1%; later 26.96M pieces of data leaked, 700B won security investment, 800B won revenue forecast cut, 500B won customer package cost, and about 134B won fine.
- Jeju Air is hard 4C. Fatal crash killed 179 people; shares fell as much as -15.7% to 6,920 won and wiped out 95.7B won market cap.
- L&F / Tesla is contract-collapse hard 4C. Initial $2.9B cathode-material deal value was cut to $7,386. Customer name and contract headline failed actual call-off.
- Naver Financial / Dunamu is M&A event premium plus trust 4C-watch. Deal value 15.13T won; Naver initially +7% but later -4.2% after 54B won abnormal withdrawal from Upbit.
- LG CNS is evidence_good_but_price_failed. IPO price 61,900 won; debut trading at 59,700 won despite cloud/AI at 54% of 9M 2024 sales.
- Korea Zinc is 4B governance/dilution watch. Tender offer drove +19.8% to +24%, but later new-share issue plan and accounting-fraud review flag created governance gate.
- Samsung E&A Fadhili is order-headline Stage 2, not Green. $6B contract and +8.5% event reaction require EPC margin, working capital, unbilled receivables and cash collection.
- Hyundai Motor India IPO is failed rerating / capital-recycling watch. $3.3B IPO fell as much as -6% on debut; parent Green requires proceeds use and ROI/shareholder-return bridge.
```

## docs/checkpoints/checkpoint_28a_round210_r13_loop13.md 요약

```md
# Checkpoint 28A Round 210 R13 Loop 13 Cross-archetype RedTeam

## 반영 내용
- R13 Loop 13 cross-archetype RedTeam / 4B / accounting-trust 라운드를 추가했다.
- SK Telecom, Jeju Air, L&F, Naver/Dunamu, LG CNS, Korea Zinc, Samsung E&A, Hyundai Motor India를 cross-sector calibration case로 비교했다.
- Reuters / WSJ anchors로 가능한 event MFE/MAE, deal value, IPO price, fine, contract-collapse value, market-cap wipeout을 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- trust/internal control, fatal safety event, actual call-off, custody control, aftermarket IPO demand, governance/dilution control, accounting investigation flag, project margin/cash conversion 가중치 강화
- customer-name headline-only, order backlog headline-only, IPO size/oversubscription-only, control premium-only, M&A synergy before trust, AI/cloud keyword without aftermarket demand 감점 강화
```

## data/e2r_case_library/cases_r13_loop13_round210.jsonl 초안

```jsonl
{"case_id":"r13_loop13_skt_cybersecurity_hard_4c","symbol":"017670","company_name":"SK Telecom","case_type":"hard_4c","primary_archetype":"CYBERSECURITY_TRUST_HARD_4C","stage4c_date":"2025-04-28/2025-07-04/2025-08-28","price_validation":{"price_data_source":"Reuters event-return anchors","stage3_price":null,"initial_intraday_mae_pct":-8.5,"initial_close_mae_pct":-6.7,"kospi_same_context_pct":0.1,"relative_underperformance_initial_pp":-6.8,"usim_replacement_users_mn":23,"leaked_data_pieces_mn":26.96,"july_event_close_mae_pct":-5.6,"data_protection_investment_krw_bn":700,"revenue_forecast_cut_krw_bn":800,"customer_benefit_package_cost_krw_bn":500,"pipc_fine_krw_bn":134,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"cybersecurity_trust_hard_4C","notes":"Data trust/internal control failure became revenue cut, security capex, fine and compensation risk."}
{"case_id":"r13_loop13_jeju_air_safety_hard_4c","symbol":"089590","company_name":"Jeju Air","case_type":"hard_4c","primary_archetype":"AVIATION_SAFETY_HARD_4C","stage4c_date":"2024-12-30","price_validation":{"price_data_source":"Reuters event-price anchor","stage3_price":null,"fatalities":179,"event_low_price_krw":6920,"event_intraday_mae_pct":-15.7,"event_midday_mae_pct":-8.5,"market_cap_wipeout_krw_bn":95.7,"market_cap_wipeout_usd_mn":65.2,"ak_holdings_mae_pct":-12,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"aviation_safety_hard_4C","notes":"Fatal safety event overrides demand/capacity and must be hard gate."}
{"case_id":"r13_loop13_lnf_tesla_contract_collapse","symbol":"066970","company_name":"L&F","case_type":"hard_4c","primary_archetype":"CONTRACT_VALUE_COLLAPSE_HARD_4C","stage1_date":"2023-02","stage4c_date":"2025-12-29","price_validation":{"price_data_source":"Reuters contract-collapse anchor","stage3_price":null,"initial_contract_projection_usd_bn":2.9,"revised_contract_value_usd":7386,"contract_value_collapse_pct":-99.9997,"supply_period":"2024-01_to_2025-12","customer":"Tesla and affiliates","application_context":"4680 high-nickel cathode materials","price_validation_status":"contract_value_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"customer_contract_calloff_failure","notes":"Customer-name contract headline failed actual call-off; hard 4C."}
{"case_id":"r13_loop13_naver_dunamu_upbit_trust_gate","symbol":"035420","company_name":"Naver Financial / Dunamu / Upbit","case_type":"event_premium_4c_watch","primary_archetype":"DIGITAL_ASSET_TRUST_4C_WATCH","stage2_date":"2025-11-27","stage4b_date":"2025-11-27","stage4c_date":"2025-11-27_watch","price_validation":{"price_data_source":"Reuters deal and abnormal-withdrawal anchor","stage3_price":null,"deal_value_krw_trn":15.13,"deal_value_usd_bn":10.27,"exchange_ratio_naver_financial_per_dunamu":2.54,"upbit_market_share_pct":70,"event_initial_mfe_pct":7.0,"event_later_mae_pct":-4.2,"event_swing_pp":-11.2,"abnormal_withdrawal_krw_bn":54,"loss_coverage":"Upbit_to_cover_using_own_assets","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_trust_watch","rerating_result":"digital_asset_MA_trust_gate","notes":"M&A premium reversed on custody/internal-control concern; digital trust gate required."}
{"case_id":"r13_loop13_lg_cns_ipo_quality_gate","symbol":"064400","company_name":"LG CNS","case_type":"evidence_good_but_price_failed","primary_archetype":"IPO_QUALITY_GATE_FALSE_POSITIVE","stage2_date":"2025-02-05","price_validation":{"price_data_source":"Reuters IPO/debut anchor","stage3_price":null,"ipo_price_krw":61900,"open_price_krw":60500,"morning_trading_price_krw":59700,"debut_mae_vs_ipo_pct":-3.23,"ipo_raise_krw_trn":1.2,"ipo_raise_usd_mn":827.1,"market_valuation_morning_krw_trn":5.79,"retail_oversubscription_multiple":123,"institutional_bids_krw_trn":76,"cloud_ai_sales_share_9m2024_pct":54,"revenue_9m2024_krw_trn":4.0,"op_9m2024_krw_bn":313,"op_margin_9m2024_pct":7.8,"price_validation_status":"reported_ipo_anchor_not_full_ohlc"},"score_price_alignment":"evidence_good_but_price_failed","rerating_result":"AI_cloud_IPO_quality_gate","notes":"AI/cloud mix was real, but aftermarket demand failed issue price."}
{"case_id":"r13_loop13_korea_zinc_control_premium_dilution_watch","symbol":"010130","company_name":"Korea Zinc","case_type":"event_premium_4b_watch","primary_archetype":"CONTROL_PREMIUM_DILUTION_4B","stage2_date":"2024-09-13","stage4b_date":"2024-09-13","stage4c_date":"2024-10-31_watch","price_validation":{"price_data_source":"Reuters/WSJ tender-offer and share-issue investigation anchors","stage3_price":null,"tender_offer_value_krw_trn":2.0,"tender_offer_value_usd_bn":1.5,"offer_price_krw":660000,"prior_close_krw":556000,"reuters_event_mfe_pct":19.8,"wsj_event_mfe_pct":24.0,"wsj_event_high_price_krw":690000,"target_stake_min_pct":6.98,"target_stake_max_pct":14.61,"new_share_issue_plan_usd_bn":1.8,"accounting_fraud_review_flag":true,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_4B_watch","rerating_result":"control_premium_governance_dilution_watch","notes":"Control premium must be separated from operating Green and dilution/accounting risk."}
{"case_id":"r13_loop13_samsung_ena_fadhili_order_not_margin_green","symbol":"028050","company_name":"Samsung E&A","case_type":"success_candidate_event_premium","primary_archetype":"ORDER_HEADLINE_NOT_MARGIN_GREEN","stage2_date":"2024-04-03","stage4b_date":"2024-04-03","price_validation":{"price_data_source":"WSJ/Aramco contract event anchor","stage3_price":null,"contract_value_usd_bn":6.0,"project_total_value_usd_bn":7.7,"samsung_contract_share_of_total_pct":77.9,"event_price_krw":26750,"event_mfe_pct":8.5,"kospi_same_context_pct":-1.4,"relative_outperformance_pp":9.9,"target_price_krw":35000,"target_upside_from_event_price_pct":30.8,"capacity_increase_pct":60,"completion_target":"2027-11","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"order_headline_stage2_not_margin_green","notes":"Mega-order is Stage 2; EPC margin, working capital and cash collection required."}
{"case_id":"r13_loop13_hyundai_india_ipo_failed_rerating","symbol":"005380/HYUN.NS","company_name":"Hyundai Motor / Hyundai Motor India","case_type":"failed_rerating","primary_archetype":"CAPITAL_RECYCLING_IPO_FAILED_RERATING","stage2_date":"2024-10-14","stage4c_date":"2024-10-22_watch","price_validation":{"price_data_source":"Reuters IPO/debut anchor","stage3_price":null,"ipo_value_usd_bn":3.3,"parent_stake_sale_pct":17.5,"target_valuation_usd_bn":19,"offer_price_inr":1960,"listing_price_inr":1934,"morning_trade_price_inr":1882.10,"listing_discount_pct":-1.33,"debut_mae_pct":-6.0,"valuation_debut_inr_trn":1.53,"valuation_debut_usd_bn":18.2,"market_share_india_pct":15,"ipo_oversubscription":"more_than_2x","price_validation_status":"reported_ipo_anchor_not_full_ohlc"},"score_price_alignment":"failed_rerating","rerating_result":"capital_recycling_IPO_quality_gate","notes":"Large IPO did not translate to parent Green; aftermarket demand and ROI bridge required."}
```

## data/sector_taxonomy/score_weight_profiles_round210_r13_loop13_v1.csv 초안

```csv
archetype,trust_internal_control,fatal_safety_event,actual_calloff_vs_contract,custody_digital_asset_control,aftermarket_ipo_demand,governance_dilution_control,accounting_investigation_flag,project_margin_cash_conversion,working_capital_unbilled_receivables,parent_roi_bridge,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
CYBERSECURITY_TRUST_HARD_4C,+5,+1,+0,+3,+0,+3,+3,+2,+2,+0,0,+4,+5,SK Telecom confirms trust/internal-control hard gate.
AVIATION_SAFETY_HARD_4C,+2,+5,+0,+0,+0,+2,+1,+1,+0,+0,0,+3,+5,Jeju Air confirms fatal safety event hard gate.
CONTRACT_VALUE_COLLAPSE_HARD_4C,+2,+1,+5,+0,+0,+2,+2,+3,+2,+2,0,+4,+5,L&F confirms customer-name contract needs actual call-off.
DIGITAL_ASSET_TRUST_4C_WATCH,+5,+0,+0,+5,+0,+3,+3,+1,+0,+4,-5,+5,+5,Naver/Dunamu shows M&A premium must pass custody/internal-control gate.
IPO_QUALITY_GATE_FALSE_POSITIVE,+2,+0,+1,+0,+5,+2,+1,+3,+1,+5,-5,+5,+4,LG CNS shows good AI/cloud evidence can still fail issue price.
CONTROL_PREMIUM_DILUTION_4B,+3,+1,+1,+0,+0,+5,+5,+3,+2,+4,-5,+5,+5,Korea Zinc control premium requires dilution/accounting governance gate.
ORDER_HEADLINE_NOT_MARGIN_GREEN,+2,+1,+3,+0,+0,+2,+2,+5,+5,+3,-5,+5,+4,Samsung E&A order needs EPC margin, working capital and cash collection.
CAPITAL_RECYCLING_IPO_FAILED_RERATING,+2,+0,+1,+0,+5,+3,+1,+2,+1,+5,-5,+5,+4,Hyundai India IPO needs aftermarket demand and parent ROI bridge.
```

---

# 이번 R13 Loop 13 결론

```text
1. SK Telecom은 trust/internal-control hard 4C다.
   데이터 유출이 주가, 매출전망, 보상비용, 과징금으로 직접 내려왔다.

2. Jeju Air는 safety hard 4C다.
   fatal accident는 수요·capacity·valuation보다 먼저 본다.

3. L&F는 contract-quality hard 4C다.
   Tesla라는 고객명과 $2.9B 계약 headline도 실제 call-off가 없으면 0에 가까워질 수 있다.

4. Naver/Dunamu는 digital-asset trust 4C-watch다.
   M&A premium은 Upbit abnormal withdrawal 하나로 바로 뒤집혔다.

5. LG CNS는 evidence_good_but_price_failed다.
   AI/cloud 매출비중이 높아도 IPO aftermarket demand가 받지 않으면 Stage 3가 아니다.

6. Korea Zinc는 control premium 4B-watch다.
   tender premium은 강하지만 dilution/accounting/governance gate가 따라붙었다.

7. Samsung E&A는 mega-order success_candidate지만 Stage 3는 아니다.
   order headline 뒤에는 EPC margin, working capital, cash collection이 남는다.

8. Hyundai India IPO는 failed rerating이다.
   IPO 규모와 India 성장 narrative보다 공모가·상장 후 수요·parent ROI bridge가 중요하다.
```

한 문장으로 압축하면:

> **R13에서 Stage 3를 막아야 하는 가장 큰 함정은 “좋은 단어”다. 고객명, IPO, M&A, mega-order, control premium, AI/cloud, 성장시장, 정책수혜는 Stage 2를 만들 수는 있지만, trust·safety·call-off·margin·aftermarket demand·governance·cash conversion을 통과해야만 Stage 3가 된다.**

* [Reuters](https://www.reuters.com/sustainability/boards-policy-regulation/sk-telecom-shares-plunge-after-data-breach-due-cyberattack-2025-04-28/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-orders-sk-telecom-strengthen-data-security-after-leak-2025-07-04/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-agency-fines-sk-telecom-97-million-over-major-data-leak-2025-08-28/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/aerospace-defense/jeju-air-shares-plunge-record-low-after-deadly-plane-crash-2024-12-30/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/south-koreas-lf-says-value-battery-material-supply-deal-with-tesla-cut-7386-2025-12-29/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/navers-payment-arm-acquire-south-korean-crypto-exchange-operator-10-bln-deal-2025-11-27/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/technology/skorean-tech-services-firm-lg-cns-falls-stock-market-debut-2025-02-05/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/markets/deals/private-equity-mbk-young-poong-launch-15-bln-tender-offer-korea-zinc-shares-2024-09-13/?utm_source=chatgpt.com)
* [월스트리트저널](https://www.wsj.com/articles/samsung-e-a-shares-rise-on-6-billion-saudi-contract-win-10a5b2f4?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/autos-transportation/hyundai-indias-shares-fall-13-debut-trade-after-record-33-bln-ipo-2024-10-22/?utm_source=chatgpt.com)

[1]: https://www.reuters.com/sustainability/boards-policy-regulation/sk-telecom-shares-plunge-after-data-breach-due-cyberattack-2025-04-28/?utm_source=chatgpt.com "SK Telecom shares plunge after data breach due to cyberattack"
[2]: https://www.reuters.com/business/aerospace-defense/jeju-air-shares-plunge-record-low-after-deadly-plane-crash-2024-12-30/?utm_source=chatgpt.com "Jeju Air shares plummet to record low after deadly plane crash"
[3]: https://www.reuters.com/world/asia-pacific/south-koreas-lf-says-value-battery-material-supply-deal-with-tesla-cut-7386-2025-12-29/?utm_source=chatgpt.com "South Korea's L&F slashes value of battery material supply deal with Tesla"
[4]: https://www.reuters.com/world/asia-pacific/navers-payment-arm-acquire-south-korean-crypto-exchange-operator-10-bln-deal-2025-11-27/?utm_source=chatgpt.com "Naver's payment arm to acquire South Korean crypto exchange operator in $10 bln deal"
[5]: https://www.reuters.com/technology/skorean-tech-services-firm-lg-cns-falls-stock-market-debut-2025-02-05/?utm_source=chatgpt.com "South Korean tech services firm LG CNS drops in market debut"
[6]: https://www.reuters.com/markets/deals/private-equity-mbk-young-poong-launch-15-bln-tender-offer-korea-zinc-shares-2024-09-13/?utm_source=chatgpt.com "Private equity MBK, Young Poong launch $1.5 bln tender offer for Korea Zinc shares"
[7]: https://www.wsj.com/articles/samsung-e-a-shares-rise-on-6-billion-saudi-contract-win-10a5b2f4?utm_source=chatgpt.com "Samsung E&A Shares Rise on $6 Billion Saudi Contract Win"
[8]: https://www.reuters.com/business/autos-transportation/hyundai-indias-shares-fall-13-debut-trade-after-record-33-bln-ipo-2024-10-22/?utm_source=chatgpt.com "Hyundai Motor India drops 6% in debut after country's biggest IPO"

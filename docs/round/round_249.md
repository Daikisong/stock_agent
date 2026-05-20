순서상 이번은 **R6 Loop 11 — 금융·자본배분·디지털금융 가격경로 검증 라운드**다.

이번 R6 Loop 11은 기존 은행 value-up 반복을 줄이고, **금융지주 value-up, 증권주 거래대금 cycle, holding NAV discount, 보험 NAV capital release, 은행의 디지털자산 지분투자, Naver/Dunamu fintech-platform deal, 인터넷은행 IPO·governance, stablecoin 과열**을 같이 본다.

```text
round = R6 Loop 11
round_id = round_177
large_sector = FINANCIAL_CAPITAL_DIGITAL
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = false
```

이번에도 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉 OHLC 전체 구간은 안정적으로 확보하지 못했다. 대신 Reuters / FT / WSJ가 제공한 **가격 anchor, 이벤트 수익률, 거래금액, 지분율, 정책 수치, 금융사고 지표**로 계산 가능한 값만 계산했다. 30D/90D/180D full OHLC가 없는 항목은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R6 = 금융·자본배분·디지털금융
```

R6의 Stage 3는 “저PBR”, “밸류업”, “디지털자산”, “스테이블코인”이 아니다. **ROE·CET1/K-ICS·credit cost·실제 소각·반복 배당·지분법 이익·규제수익·플랫폼 신뢰**가 같이 확인되는 순간이다.

---

# 2. 대상 canonical archetype

```text
BANK_VALUEUP_ROE_PBR_RERATING
SECURITIES_MARKET_VOLUME_CYCLE
HOLDING_NAV_DISCOUNT_VALUEUP
INSURANCE_NAV_CAPITAL_RELEASE
DIGITAL_ASSET_BANK_EQUITY_OPTION
DIGITAL_ASSET_PLATFORM_MERGER_TRUST_WATCH
INTERNET_BANK_IPO_PROFITABILITY
INTERNET_BANK_GOVERNANCE_4C
KRW_STABLECOIN_POLICY_OVERHEAT
PRICE_ONLY_RALLY
EVENT_PREMIUM
```

---

# 3. deep sub-archetype

```text
은행 value-up:
- KB / Shinhan / Hana / Woori
- Commercial Act treasury-share cancellation
- ROE / CET1 / credit cost
- buyback cancellation / dividend payout
- low-PBR rerating vs actual capital return

증권:
- securities basket
- KOSPI 7,000 / trading-volume cycle
- brokerage / IB / trading revenue
- cyclical revenue vs structural ROE

Holding NAV:
- SK Square
- SK Hynix stake
- buyback cancellation
- activist pressure / NAV discount narrowing

보험 NAV:
- Samsung Life
- Samsung Electronics stake
- regulatory share sale
- K-ICS / CSM / capital release

디지털자산:
- Hana Bank / Dunamu
- Naver Financial / Dunamu
- Upbit share
- exchange abnormal withdrawal / trust watch

인터넷은행:
- K Bank IPO profitability
- KakaoBank governance risk
- major shareholder suitability

스테이블코인:
- Kakao Pay / LG CNS / Aton / ME2ON
- won stablecoin policy
- issuer license / reserve income / fee revenue 전 가격 과열
```

---

# 4. 국장 신규 후보 case

## Case A — Big-4 금융지주 value-up basket `success_candidate / market-structure Stage 2`

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
- Corporate Value-up Programme
- 저PBR 금융지주 rerating 기대
- 배당 / 자사주 / 소각 확대 기대

Stage 2:
2026-02-25
- Commercial Act revision
- listed companies must cancel newly acquired treasury shares within one year
- 기존 treasury shares에는 6개월 grace period
- 주주환원·소각 실행력 강화

Stage 2 price event:
2026-05-06
- KOSPI 7,000 돌파
- financial groups +4.2%
- securities firms +13.5%
- foreign net purchase 3.1T won

Stage 3:
없음
- 금융지주 value-up은 Stage 2
- ROE, CET1, credit cost, 실제 반복 소각, 배당성향 확인 전 Green 금지

Stage 4B:
PBR rerating이 ROE와 소각보다 먼저 가격에 반영되면 후보

Stage 4C:
PF credit cost, CET1 약화, 주주환원 후퇴, tax shock, 경기둔화 credit shock
```

한국 국회는 2026년 2월 새로 취득한 자사주를 1년 내 소각하도록 하는 상법 개정안을 통과시켰고, 기존 treasury shares에는 6개월 유예기간을 부여했다. 이건 금융지주 value-up에 좋은 Stage 2지만, 은행주 Green은 아직 아니다. 2026년 5월 6일 KOSPI가 7,000을 넘은 날 금융지주는 4.2%, 증권주는 13.5% 상승했고 외국인은 3.1조 원을 순매수했다. 다만 이 가격반응은 market confidence 회복이지, 개별 금융지주의 ROE/CET1/credit cost가 확인된 Stage 3는 아니다. ([Reuters][1])

### 실제 가격경로 검증

```text
price_data_source:
Reuters Commercial Act / KOSPI 7,000 sector-return anchors

stage3_price:
N/A

Commercial_Act_revision:
newly acquired treasury shares must be cancelled within 1 year

existing_treasury_shares:
6-month grace period

financial_groups_event_MFE_1D:
+4.2%

KOSPI_same_context:
+6.45%

financial_groups_relative_underperformance_vs_KOSPI:
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
rerating_result = bank_valueup_ROE_PBR_watch
stage_failure_type = market_structure_stage2_not_green
```

---

## Case B — 증권주 basket `cyclical_success + 4B-watch`

```text
symbols = securities basket / Mirae Asset / Samsung Securities / Kiwoom / NH / Korea Investment exposure
case_type = cyclical_success + 4B-watch
archetype = SECURITIES_MARKET_VOLUME_CYCLE
```

### stage date

```text
Stage 1:
2025~2026
- KOSPI bull market
- 거래대금 / brokerage / IB / trading revenue 기대
- capital-market confidence recovery

Stage 2:
2026-05-06
- KOSPI closes +6.45% at 7,384.56
- securities firms +13.5%
- foreign net purchase 3.1T won

Stage 3:
없음
- 증권주 rally는 market-cycle Stage 2
- brokerage revenue, IB revenue, ROE, risk controls 확인 전 Green 금지

Stage 4B:
2026-05-06
- securities basket +13.5%
- 실적 확인 전 거래대금 cycle 기대가 가격에 먼저 반영
```

증권주는 R6에서 “좋은 cyclicality”와 “구조적 Stage 3”를 분리해야 한다. KOSPI가 7,000을 돌파한 날 증권업종은 13.5% 상승해 KOSPI를 7.05pp 아웃퍼폼했다. 하지만 이건 거래대금·위탁매매·IB 호황 기대의 Stage 2다. Green은 실제 brokerage revenue, IB revenue, trading income, ROE 개선이 확인될 때다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters sector-return anchor

stage3_price:
N/A

KOSPI_event_return:
+6.45%

KOSPI_intraday_high_return:
+7.06%

securities_firms_event_MFE_1D:
+13.5%

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
rerating_result = securities_market_volume_boom_watch
stage_failure_type = stage2_cyclical_not_green
```

---

## Case C — SK Square `success_candidate / NAV discount value-up`

```text
symbol = 402340
case_type = success_candidate
archetype = HOLDING_NAV_DISCOUNT_VALUEUP
```

### stage date

```text
Stage 1:
2024
- SK Hynix NAV discount
- activist engagement
- Korea Value-up programme

Stage 2:
2024-11-21
- 100B won 자사주 소각
- 추가 100B won 매입·소각 계획
- independent director nomination
- SK Hynix 20% stake
- SK Square market value < half of $18B SK Hynix stake value

Stage 3:
보류
- 반복 소각
- discount narrowing
- NAV 상승이 실제 주주환원으로 연결되는지 확인 필요

Stage 4B:
SK Hynix 대시세 이후 SK Square NAV trade가 crowded해지면 후보

Stage 4C:
소각 중단, SK Hynix 급락, discount 재확대, governance 후퇴
```

SK Square는 R6에서 가장 깔끔한 NAV discount Stage 2 후보다. 회사는 2024년 11월 1,000억 원 규모 자사주 소각과 추가 1,000억 원 매입·소각 계획을 발표했고, SK Hynix 지분 20%를 보유한다. Reuters는 당시 SK Square 시가총액이 보유 SK Hynix 지분가치 180억 달러의 절반보다 낮다고 보도했다. 이건 자본배분 evidence지만, Stage 3는 반복 소각과 NAV discount 실제 축소가 확인될 때다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters buyback / NAV-discount anchor

stage3_price:
N/A

cancelled_buyback:
100B won

additional_buyback_cancel_plan:
100B won

total_buyback_cancel_program:
200B won

SK_Hynix_stake:
20%

SK_Hynix_stake_value_2024:
$18B

SK_Square_market_value_vs_stake_value:
less than 50%

minimum_NAV_discount_2024:
>50%

Palliser_stake:
about 1%

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = NAV_discount_valueup_watch
stage_failure_type = stage2_watch_success_not_green
```

---

## Case D — Samsung Life `success_candidate / insurance NAV capital-release`

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
- capital release / regulation compliance 기대

Stage 2:
2026-03-19
- Samsung Life sells 1.3T won Samsung Electronics shares
- purpose: local financial-company governance regulation risk 해소

Stage 3:
없음
- 매각대금의 배당·소각·자본정책 활용 확인 필요
- K-ICS / CSM / 보험 본업 이익 확인 필요

Stage 4B:
Samsung Electronics NAV rally가 삼성생명 valuation에 과도하게 반영되면 후보

Stage 4C:
규제성 지분매각 반복, 삼성전자 급락, 보험 자본비율 악화, CSM 훼손
```

Samsung Life는 삼성전자 지분 1.3조 원어치를 매각한다고 공시했고, 회사는 금융회사 지배구조 관련 local regulation risk를 해소하기 위한 조치라고 밝혔다. 이건 insurance NAV capital-release Stage 2지만, 매각대금이 실제 K-ICS 개선·배당·소각·자본정책으로 내려오는지 확인되기 전에는 Green이 아니다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters regulatory share-sale anchor

stage3_price:
N/A

Samsung_Electronics_stake_sale:
1.3T won / $867.07M

transaction_purpose:
resolve local financial-company governance regulation risk

FX_rate_context:
1,499.3 won per USD

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate + regulatory_watch
rerating_result = insurance_NAV_valueup_watch
stage_failure_type = stage2_watch_success_not_green
```

---

## Case E — Hana Bank / Dunamu `success_candidate / regulated digital-asset equity option`

```text
symbol = 086790
case_type = success_candidate
archetype = DIGITAL_ASSET_BANK_EQUITY_OPTION
```

### stage date

```text
Stage 1:
2025~2026
- 디지털자산 제도화
- 은행권 stablecoin / blockchain remittance 기대
- regulated crypto equity exposure

Stage 2:
2026-05-14
- Hana Bank acquires 6.55% Dunamu stake
- transaction value 1T won / about $700M
- Upbit trading volume share >80%
- Kakao Investment remaining stake 4.03%

Stage 3:
보류
- 지분법 이익
- regulatory approval
- capital ratio impact
- digital asset revenue / remittance revenue 확인 필요

Stage 4B:
디지털자산 equity-option 기대가 은행주 valuation에 과도 반영되면 후보

Stage 4C:
거래량 급감, 규제 지연, capital charge, exchange trust incident, crypto market drawdown
```

Hana Bank는 Dunamu 지분 6.55%를 1조 원에 인수하기로 했다. Dunamu는 Upbit을 운영하고, Reuters는 Upbit이 국내 가상자산 거래량의 80% 이상을 처리한다고 보도했다. 지분율과 거래금액을 기준으로 보면 Dunamu implied equity value는 약 15.27조 원이다. 다만 이건 은행의 regulated digital-asset equity option이지, 아직 Hana Financial의 Stage 3가 아니다. 지분법 이익, 자본비율 영향, 규제수익, 송금·stablecoin revenue가 확인되어야 한다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / WSJ transaction anchor

stage3_price:
N/A

transaction_value:
1.0T won / about $700M

stake_acquired:
6.55%

implied_Dunamu_equity_value:
1.0T / 0.0655
= 약 15.27T won

Upbit_trading_volume_share:
>80%

Kakao_Investment_remaining_stake:
4.03%

WSJ_completion_timing:
2026-06-15 expected

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = regulated_digital_asset_equity_option
stage_failure_type = stage2_watch_success_not_green
```

---

## Case F — NAVER Financial / Dunamu `event_premium + exchange-trust 4C-watch`

```text
symbol = 035420
case_type = success_candidate + event_premium + 4C-watch
archetype = DIGITAL_ASSET_PLATFORM_MERGER_TRUST_WATCH
```

### stage date

```text
Stage 1:
2025
- NAVER fintech expansion
- digital asset / stablecoin growth 기대

Stage 2:
2025-11-27
- NAVER Financial agrees to acquire Dunamu
- all-stock deal value 15.13T won / $10.27B
- exchange ratio 2.54 NAVER Financial shares per Dunamu share
- Upbit market share about 70%

Stage 3:
없음
- regulatory approval
- merger closing
- digital asset revenue integration
- exchange volume durability
- trust/security risk 통과 필요

Stage 4B:
2025-11-27
- NAVER shares initially +7% 이상

Stage 4C-watch:
2025-11-27
- Upbit abnormal withdrawal 54B won
- NAVER shares later -4.2%
```

Naver Financial은 Dunamu를 15.13조 원 규모 all-stock deal로 인수하기로 했고, Upbit은 국내 crypto exchange 시장 약 70%를 차지하는 플랫폼으로 설명됐다. 발표 직후 NAVER 주가는 7% 넘게 올랐지만, Upbit에서 540억 원 규모 abnormal withdrawal이 발생했다는 소식 이후 -4.2%로 전환했다. 이 case는 R6에서 **digital-asset Stage 2 + exchange trust 4C-watch**를 동시에 보여준다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters transaction / event-return anchor

stage3_price:
N/A

deal_value:
15.13T won / $10.27B

exchange_ratio:
2.54 NAVER Financial shares per Dunamu share

Upbit_market_share:
about 70%

event_MFE_initial:
> +7%

event_MAE_same_day_after_abnormal_withdrawal:
-4.2%

event_swing_from_initial_plus_7_to_minus_4_2:
-11.2pp

abnormal_withdrawal:
54B won

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium + trust_watch
rerating_result = digital_asset_platform_watch
stage_failure_type = stage2_watch_success_with_4C_watch
```

---

## Case G — K Bank / KakaoBank `internet-bank profitability + governance 4C-watch`

```text
symbols = K Bank unlisted / 323410 / 035720
case_type = success_candidate + governance_4C_watch
archetype = INTERNET_BANK_IPO_PROFITABILITY / INTERNET_BANK_GOVERNANCE_4C
```

### stage date

```text
K Bank Stage 1:
2024-09-10
- South Korea first internet-only bank
- 10M+ customers
- digital bank profitability

K Bank Stage 2:
2024-09-10
- IPO plan up to 984B won
- price range 9,500~12,000 won
- valuation up to about 5T won
- 1H 2024 operating profit 86.7B won, more than triple YoY

K Bank Stage 3:
없음
- unlisted / IPO plan only
- listed price path, credit quality, NIM, funding cost, fee income 필요

Kakao/KakaoBank 4C-watch:
2024-07-23
- Kakao founder Kim Beom-su arrested
- Kakao shares -3.4%
- YTD -24%
- founder controls 24% stake
- conviction could jeopardize KakaoBank control due to >10% bank ownership restriction
```

K Bank는 인터넷은행 profitability Stage 2 후보다. IPO 계획은 최대 9,840억 원 조달, 공모가 9,500~12,000원, valuation 최대 5조 원으로 제시됐고, 2024년 상반기 영업이익은 867억 원으로 전년 대비 3배 이상 증가했다. 반면 KakaoBank 쪽은 성장성보다 governance gate가 먼저다. Kakao 창업자 김범수 구속 뉴스 당시 Kakao는 3.4% 하락했고, 당시 연초 대비 24% 하락한 상태였다. Reuters는 유죄 확정 시 금융범죄자의 은행 지분 10% 초과 보유 제한 때문에 KakaoBank 지배력 문제가 생길 수 있다고 설명했다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters IPO / legal-governance anchors

K_Bank:
stage3_price = N/A
IPO_status = unlisted / IPO candidate

IPO_raise_max:
984B won

IPO_price_range:
9,500~12,000 won

shares_to_sell:
82M shares
- 41M new shares
- 41M existing shares

max_offer_value_check:
82M * 12,000
= 984B won

reported_valuation_up_to:
5T won

1H_2024_operating_profit:
86.7B won

customer_count:
>10M

Kakao/KakaoBank:
Kakao_event_MAE_1D:
-3.4%

Kakao_YTD_drawdown_context:
-24%

Kim_controlled_stake:
24%

Kakao_group_assets_context:
86T won / $62B

bank_ownership_cap_risk:
>10% if convicted of financial crime

MFE / MAE for KakaoBank:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate_for_KBank / thesis_break_watch_for_KakaoBank
rerating_result = internet_bank_profitability_watch_with_governance_gate
stage_failure_type = stage2_unlisted_not_green / governance_4C_watch
```

---

## Case H — KRW stablecoin basket `overheat / price_moved_without_evidence`

```text
symbols = 377300 / LG CNS / Aton / ME2ON
case_type = overheat / price_moved_without_evidence
archetype = KRW_STABLECOIN_POLICY_OVERHEAT
```

### stage date

```text
Stage 1:
2025-06
- won stablecoin policy pledge
- digital asset reform 기대
- private won-backed stablecoin issuance debate

Stage 2:
없음 또는 약한 Stage 2
- 법안·정책 기대는 있었지만 회사별 수익모델 미확인

Stage 3:
없음
- issuer license, reserve income, fee revenue, regulatory capital 확인 전 Green 금지

Stage 4B:
2025-06
- Kakao Pay >2배
- LG CNS +70%
- Aton +80%
- ME2ON 3배

Stage 4C:
비은행 발행 제한, 외환리스크 우려, 규제 지연, 실질 revenue 부재
```

KRW stablecoin basket은 이번 R6 Loop 11의 대표적인 `price_moved_without_evidence`다. FT는 Kakao Pay가 한 달 동안 2배 이상, LG CNS가 약 70%, Aton이 80%, ME2ON이 3배 올랐다고 보도했다. 그러나 같은 보도에서 margin loan이 20.5조 원까지 늘었고, proposed bill은 5억 원 자본만 있어도 won-based stablecoin 발행을 허용할 수 있다는 점 때문에 과열 우려가 제기됐다. 별도 FT 보도에서는 Bank of Korea가 비은행 stablecoin 발행이 FX crisis 대응을 어렵게 만들 수 있다고 우려한다고 설명했다. ([Financial Times][8])

### 실제 가격경로 검증

```text
price_data_source:
FT reported return and policy-risk anchors

stage3_price:
N/A

Kakao_Pay_reported_MFE_month:
> +100%

LG_CNS_reported_MFE_month:
+70%

Aton_reported_MFE_month:
+80%

ME2ON_reported_MFE_month:
+200%

margin_loan_context:
20.5T won

proposed_minimum_equity_for_issuers:
500M won

regulated_revenue_confirmed:
false

issuer_license_confirmed:
false

reserve_income_confirmed:
false

MFE_30D:
reported return anchors available

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = price_moved_without_evidence
rerating_result = stablecoin_policy_theme_overheat
stage_failure_type = should_have_been_stage1_or_4B_watch
```

---

# 5. 이번 R6 case별 요약표

| case                | 분류                         |                                                               실제 가격검증 | alignment      |
| ------------------- | -------------------------- | --------------------------------------------------------------------: | -------------- |
| Big-4 금융지주 value-up | success_candidate          | financial groups +4.2%, KOSPI +6.45%, treasury-share cancellation law | Stage 2        |
| 증권주 basket          | cyclical_success + 4B      |                 securities +13.5%, relative +7.05pp, foreign buy 3.1T | cycle          |
| SK Square           | success_candidate          |   200B won buyback/cancel programme, SKH stake 20%, NAV discount >50% | NAV value-up   |
| Samsung Life        | success_candidate          |                               Samsung Electronics stake sale 1.3T won | insurance NAV  |
| Hana Bank / Dunamu  | success_candidate          |                   1T won for 6.55%, implied Dunamu 15.27T, Upbit >80% | digital equity |
| NAVER / Dunamu      | event + 4C-watch           |                     15.13T deal, +7% → -4.2%, abnormal withdrawal 54B | trust watch    |
| K Bank / KakaoBank  | success + governance watch |       K Bank IPO max 984B; Kakao -3.4%, YTD -24%, bank ownership risk | mixed          |
| stablecoin basket   | overheat                   |                       Kakao Pay >2x, LG CNS +70%, Aton +80%, ME2ON 3x | price-only     |

---

# 6. score-price alignment 판정

```text
success_candidate:
- Big-4 금융지주 value-up
- SK Square
- Samsung Life
- Hana Bank / Dunamu
- K Bank

cyclical_success:
- 증권주 basket

event_premium:
- NAVER / Dunamu
- stablecoin basket
- financial groups / securities if price outruns ROE and shareholder-return execution

price_moved_without_evidence:
- Kakao Pay / LG CNS / Aton / ME2ON stablecoin basket

thesis_break_watch:
- Kakao / KakaoBank legal-governance risk
- NAVER / Upbit abnormal withdrawal trust watch
- stablecoin non-bank issuer regulatory risk

4B-watch:
- securities +13.5%
- stablecoin basket 2~3배
- NAVER / Dunamu initial +7%
- SK Square / Samsung Life NAV trade가 underlying asset rally 뒤 crowded해질 경우

4C-watch:
- KakaoBank ownership-risk
- Upbit abnormal withdrawal
- stablecoin non-bank issuer regulation
- PF / credit cost / CET1 risk for financial groups

hard_4C_confirmed:
- false
```

---

# 7. 점수비중 교정

## 올릴 축

```text
roe_sustainability +5
cet1_or_capital_buffer +5
real_buyback_cancellation +5
dividend_payout_visibility +4
credit_cost_control +5
pbr_roe_gap +4
capital_release_quality +4
regulated_revenue_visibility +4
nav_discount_with_monetization +4
digital_asset_equity_value_with_regulation +3
platform_trust +5
```

### 왜 올리나

SK Square는 실제 자사주 소각과 추가 매입·소각 계획이 있다. Samsung Life는 삼성전자 지분 매각으로 capital release 후보가 됐다. Hana Bank는 1조 원을 들여 Dunamu 지분을 취득했다. 그러나 모두 Stage 3는 **ROE·자본비율·반복 주주환원·규제수익·지분법 이익·플랫폼 신뢰**가 확인될 때다.

## 내릴 축

```text
low_pbr_only -5
policy_valueup_only -4
treasury_buyback_without_cancellation -4
stablecoin_policy_theme_only -5
digital_asset_equity_option_without_revenue -3
fintech_user_growth_without_profit -3
exchange_trust_break -5
major_shareholder_legal_risk -5
capital_ratio_weakening -4
event_rally_before_regulated_revenue -5
```

### 왜 내리나

Stablecoin basket은 issuer license, reserve income, fee revenue 없이 2~3배 급등했다. NAVER/Dunamu는 deal 자체는 크지만, abnormal withdrawal이 당일 trust risk를 만들었다. KakaoBank는 인터넷은행 성장성보다 major shareholder legal risk가 Green을 막는다.

## Green gate 강화 조건

```text
R6 Stage 3-Green 필수:
1. ROE 개선 또는 유지
2. CET1 / K-ICS / capital buffer 충분
3. 자사주 매입이 실제 소각으로 이어짐
4. 배당·소각이 반복 policy로 고정
5. credit cost / PF risk 통과
6. PBR-ROE gap 축소 여지 존재
7. 디지털자산은 규제수익·지분법·수수료 구조 확인
8. platform / exchange trust hard risk 없음
9. major shareholder legal risk 없음
10. 가격경로가 evidence 이후 따라옴

금지:
저PBR만 있음
밸류업 정책 기대만 있음
자사주 매입만 있고 소각 없음
스테이블코인 테마만 있음
비은행 디지털자산 수혜만 있음
대주주 법적 리스크
거래소 신뢰 훼손
```

## 4B 조기감지 조건

```text
4B-watch:
은행·보험주가 PBR rerating 후 book value 근처 또는 이상으로 빠르게 이동
자사주 소각 뉴스가 반복되어 surprise가 사라짐
NAV rally가 지주·보험주에 과도 반영
증권주가 거래대금 cycle 하나로 +10% 이상 급등
stablecoin 관련주가 실제 수익모델 없이 2~3배 급등
디지털자산 지분투자가 crypto 거래량 peak와 맞물림
M&A / all-stock deal이 regulatory approval 전 가격에 선반영

4B-elevated:
credit cost가 낮아 보이지만 PF 리스크가 남음
CET1 buffer가 줄어드는데 주주환원 기대가 과도
M&A/비은행 확장으로 자본부담이 커짐
규제 변경 기대가 가격에 먼저 반영됨
```

## 4C hard gate 조건

```text
PF credit cost 급증
CET1 / K-ICS 약화
자사주 소각 취소
배당성향 후퇴
대형 인수 후 자본비율 훼손
대주주 적격성 리스크
금융범죄 / governance legal break
exchange abnormal withdrawal
stablecoin issuer regulation reversal
디지털자산 거래량 급감
지분투자 손상
```

이번 R6 Loop 11에서는 KRX 직접 hard 4C를 확정하지 않는다. 다만 **Kakao/KakaoBank legal risk**, **Upbit abnormal withdrawal**, **stablecoin non-bank issuer uncertainty**는 강한 4C-watch다.

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

## docs/round/round_177.md 요약

```md
# R6 Loop 11. Financial / Capital Allocation / Digital Finance Price Validation

이번 라운드는 R6 Loop 11 price-validation 라운드다.

핵심 결론:
- Big-4 financial groups value-up is Stage 2, not Green. Commercial Act revision requires newly acquired treasury shares to be cancelled within one year. Financial groups rose +4.2% on the KOSPI 7,000 day, but ROE/CET1/credit cost/repeated shareholder return must confirm.
- Securities basket is cyclical_success and 4B-watch. On 2026-05-06, KOSPI closed +6.45%, securities firms +13.5%, foreign net purchase 3.1T won. Brokerage/IB revenue and ROE required before Green.
- SK Square is NAV-discount value-up Stage 2. It announced 100B won cancellation plus another 100B won repurchase/cancel plan, while holding a 20% SK Hynix stake valued far above its market cap.
- Samsung Life is insurance NAV capital-release Stage 2. It will divest 1.3T won Samsung Electronics shares to address financial-company governance regulation risk.
- Hana Bank / Dunamu is regulated digital-asset equity-option Stage 2. Hana buys 6.55% of Dunamu for 1T won, implying about 15.27T won Dunamu equity value. Regulated revenue, equity-method earnings and capital impact are required.
- NAVER / Dunamu is Stage 2 plus exchange-trust 4C-watch. 15.13T won all-stock deal, initial NAVER +7%, then -4.2% after 54B won abnormal withdrawal from Upbit.
- K Bank is internet-bank profitability Stage 2, but unlisted. KakaoBank has governance 4C-watch due to founder legal risk and bank ownership-rule risk.
- Stablecoin basket is price_moved_without_evidence. Kakao Pay >2x, LG CNS +70%, Aton +80%, ME2ON 3x before issuer license, reserve income or fee revenue were confirmed.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 177 R6 Loop 11 Financial Capital Digital Price Validation

## 반영 내용
- R6 Loop 11 price-validation 라운드를 추가했다.
- Bank value-up, securities-cycle, SK Square NAV discount, Samsung Life capital release, Hana/Dunamu equity option, NAVER/Dunamu platform merger, internet-bank IPO/governance, stablecoin overheat를 비교했다.
- Reuters/FT/WSJ anchors로 가능한 MFE/MAE 및 transaction/valuation/policy metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- ROE sustainability, capital buffer, real buyback cancellation, capital release, regulated digital revenue, platform trust 가중치 강화
- low-PBR only, stablecoin policy theme-only, event rally before revenue, legal-governance risk, exchange-trust break 감점 강화
- R6 4B-watch와 digital-asset 4C-watch 민감도 강화
```

## case row 초안

```jsonl
{"case_id":"r6_loop11_big4_financial_valueup_stage2","symbol":"105560/055550/086790/316140","company_name":"KB/Shinhan/Hana/Woori financial groups","case_type":"success_candidate","primary_archetype":"BANK_VALUEUP_ROE_PBR_RERATING","stage2_date":"2026-02-25/2026-05-06","price_validation":{"price_data_source":"Reuters Commercial Act / KOSPI 7000 sector-return anchors","stage3_price":null,"commercial_act_revision":"newly acquired treasury shares must be cancelled within 1 year","existing_treasury_share_grace_period_months":6,"financial_groups_event_mfe_1d_pct":4.2,"kospi_same_context_pct":6.45,"financial_groups_relative_underperformance_pp":-2.25,"foreign_net_purchase_krw_trn":3.1,"foreign_net_purchase_usd_bn":2.13,"price_validation_status":"reported_sector_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate","rerating_result":"bank_valueup_ROE_PBR_watch","notes":"Bank value-up is Stage 2; ROE/CET1/credit cost and repeated shareholder return required before Green."}
{"case_id":"r6_loop11_securities_capital_market_boom","symbol":"securities_basket","company_name":"Korean securities firms basket","case_type":"cyclical_success","primary_archetype":"SECURITIES_MARKET_VOLUME_CYCLE","stage2_date":"2026-05-06","stage4b_date":"2026-05-06","price_validation":{"price_data_source":"Reuters sector return anchor","stage3_price":null,"kospi_event_return_pct":6.45,"kospi_intraday_high_return_pct":7.06,"securities_firms_mfe_1d_pct":13.5,"securities_relative_outperformance_pp":7.05,"foreign_net_purchase_krw_trn":3.1,"foreign_net_purchase_usd_bn":2.13,"price_validation_status":"reported_sector_return_not_full_ohlc"},"score_price_alignment":"cyclical_success","rerating_result":"securities_market_volume_boom_watch","notes":"Securities rally is Stage 2/cyclical and 4B-watch; brokerage/IB revenue and ROE required before Green."}
{"case_id":"r6_loop11_sk_square_nav_discount_valueup","symbol":"402340","company_name":"SK Square","case_type":"success_candidate","primary_archetype":"HOLDING_NAV_DISCOUNT_VALUEUP","stage2_date":"2024-11-21","price_validation":{"price_data_source":"Reuters buyback/NAV-discount anchor","stage3_price":null,"cancelled_buyback_krw_bn":100,"additional_buyback_cancel_plan_krw_bn":100,"total_buyback_cancel_program_krw_bn":200,"sk_hynix_stake_pct":20,"sk_hynix_stake_value_2024_usd_bn":18,"minimum_nav_discount_2024_pct":50,"palliser_stake_pct":1,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"NAV_discount_valueup_watch","notes":"Actual cancellation supports Stage 2; repeated cancellation and discount narrowing required for Stage 3."}
{"case_id":"r6_loop11_samsung_life_nav_capital_release","symbol":"032830","company_name":"Samsung Life","case_type":"success_candidate","primary_archetype":"INSURANCE_NAV_CAPITAL_RELEASE","stage2_date":"2026-03-19","price_validation":{"price_data_source":"Reuters regulatory share-sale anchor","stage3_price":null,"samsung_electronics_stake_sale_krw_trn":1.3,"samsung_electronics_stake_sale_usd_mn":867.07,"transaction_purpose":"resolve_financial_company_governance_regulation_risk","fx_rate":1499.3,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_regulatory_watch","rerating_result":"insurance_NAV_valueup_watch","notes":"Capital release is Stage 2; use of proceeds, K-ICS/CSM and shareholder return required before Green."}
{"case_id":"r6_loop11_hana_dunamu_equity_option","symbol":"086790","company_name":"Hana Financial / Hana Bank / Dunamu","case_type":"success_candidate","primary_archetype":"DIGITAL_ASSET_BANK_EQUITY_OPTION","stage2_date":"2026-05-14","price_validation":{"price_data_source":"Reuters/WSJ transaction anchor","stage3_price":null,"transaction_value_krw_trn":1.0,"transaction_value_usd_mn":700,"stake_acquired_pct":6.55,"implied_dunamu_equity_value_krw_trn":15.27,"upbit_trading_volume_share_pct":80,"kakao_investment_remaining_stake_pct":4.03,"completion_timing":"2026-06-15_expected_by_WSJ","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"regulated_digital_asset_equity_option","notes":"Dunamu stake is Stage 2; regulated revenue, equity-method earnings, capital impact and exchange trust required for Stage 3."}
{"case_id":"r6_loop11_naver_dunamu_platform_merger_trust_watch","symbol":"035420","company_name":"NAVER / NAVER Financial / Dunamu","case_type":"success_candidate","primary_archetype":"DIGITAL_ASSET_PLATFORM_MERGER_TRUST_WATCH","stage2_date":"2025-11-27","stage4b_date":"2025-11-27","stage4c_date":"2025-11-27","price_validation":{"price_data_source":"Reuters transaction/event-return anchor","stage3_price":null,"deal_value_krw_trn":15.13,"deal_value_usd_bn":10.27,"exchange_ratio_naver_financial_per_dunamu":2.54,"upbit_market_share_pct":70,"event_mfe_initial_pct":7.0,"event_mae_same_day_pct":-4.2,"event_swing_pp":-11.2,"abnormal_withdrawal_krw_bn":54,"price_validation_status":"reported_event_return_not_full_ohlc"},"score_price_alignment":"event_premium_trust_watch","rerating_result":"digital_asset_platform_watch","notes":"Strong Stage 2 digital-asset merger, but abnormal withdrawal creates exchange-trust 4C-watch."}
{"case_id":"r6_loop11_internet_bank_kbank_kakaobank_watch","symbol":"unlisted_KBank/323410/035720","company_name":"K Bank / KakaoBank / Kakao","case_type":"success_candidate","primary_archetype":"INTERNET_BANK_IPO_PROFITABILITY","stage2_date":"2024-09-10","stage4c_date":"2024-07-23","price_validation":{"price_data_source":"Reuters IPO/legal-governance anchors","stage3_price":null,"kbank_ipo_status":"unlisted_ipo_candidate","kbank_ipo_raise_max_krw_bn":984,"kbank_price_range_krw":"9500-12000","kbank_shares_to_sell_mn":82,"kbank_max_offer_value_check_krw_bn":984,"kbank_reported_valuation_up_to_krw_trn":5.0,"kbank_h1_2024_operating_profit_krw_bn":86.7,"kbank_customer_count_mn":10,"kakao_event_mae_1d_pct":-3.4,"kakao_ytd_drawdown_context_pct":-24,"kim_controlled_stake_pct":24,"kakao_group_assets_krw_trn":86,"bank_ownership_cap_risk_pct":10,"price_validation_status":"kbank_unlisted_kakaobank_ohlc_unavailable"},"score_price_alignment":"success_candidate_for_KBank_thesis_break_watch_for_KakaoBank","rerating_result":"internet_bank_profitability_watch_with_governance_gate","notes":"K Bank is unlisted Stage 2; KakaoBank Green is blocked by major shareholder legal/ownership risk."}
{"case_id":"r6_loop11_stablecoin_policy_theme_overheat","symbol":"377300/LG_CNS/Aton/ME2ON","company_name":"Kakao Pay / stablecoin policy basket","case_type":"overheat","primary_archetype":"KRW_STABLECOIN_POLICY_OVERHEAT","stage1_date":"2025-06","stage4b_date":"2025-06","price_validation":{"price_data_source":"FT return and policy-risk anchors","stage3_price":null,"kakao_pay_mfe_month_pct":100,"lg_cns_mfe_month_pct":70,"aton_mfe_month_pct":80,"me2on_mfe_month_pct":200,"margin_loan_context_krw_trn":20.5,"proposed_minimum_equity_for_issuers_krw_mn":500,"regulated_revenue_confirmed":false,"issuer_license_confirmed":false,"reserve_income_confirmed":false,"price_validation_status":"reported_return_anchor_not_full_ohlc"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"stablecoin_policy_theme_overheat","notes":"Stablecoin theme rallied before licensed issuer, reserve income, fee revenue or regulatory capital clarity."}
```

## shadow weight row 초안

```csv
archetype,roe,capital_buffer,buyback_cancel,shareholder_return,pbr_roe_gap,credit_cost,regulated_revenue,nav_monetization,platform_trust,event_penalty,governance_trust_redteam,4b_watch_sensitivity,hard_4c_sensitivity,notes
BANK_VALUEUP_ROE_PBR_RERATING,+5,+5,+5,+5,+5,+5,+0,+0,+2,-3,+3,+4,+4,Bank value-up needs ROE/CET1/credit cost and repeated shareholder return.
SECURITIES_MARKET_VOLUME_CYCLE,+4,+3,+0,+2,+3,+3,+0,+0,+2,-3,+2,+5,+4,Securities +13.5% is cyclical; revenue/ROE must confirm before Green.
HOLDING_NAV_DISCOUNT_VALUEUP,+2,+2,+5,+5,+5,+1,+0,+5,+2,-2,+2,+4,+3,SK Square needs actual cancellation and discount narrowing.
INSURANCE_NAV_CAPITAL_RELEASE,+3,+5,+1,+4,+5,+3,+0,+5,+2,-2,+3,+4,+4,Samsung Life needs use of proceeds and K-ICS/CSM confirmation.
DIGITAL_ASSET_BANK_EQUITY_OPTION,+2,+4,+0,+1,+2,+2,+5,+2,+4,-3,+4,+5,+4,Hana/Dunamu is Stage 2 until regulated revenue and capital impact confirm.
DIGITAL_ASSET_PLATFORM_MERGER_TRUST_WATCH,+2,+3,+0,+1,+2,+2,+5,+1,+5,-4,+5,+5,+5,Naver/Dunamu has exchange-trust 4C-watch from abnormal withdrawal.
INTERNET_BANK_IPO_PROFITABILITY,+5,+4,+0,+1,+4,+5,+2,+0,+3,-4,+3,+5,+4,K Bank IPO candidate needs listed price path, ROE/NIM/credit quality.
INTERNET_BANK_GOVERNANCE_4C,+0,+0,+0,+0,+0,+0,+0,+0,+5,-3,+5,+3,+5,KakaoBank Green blocked by major shareholder legal/ownership risk.
KRW_STABLECOIN_POLICY_OVERHEAT,+0,+1,+0,+0,+1,+0,+1,+0,+3,-5,+4,+5,+4,Stablecoin rally is price_moved_without_evidence until licensing/revenue clarity.
```

---

# 이번 R6 Loop 11 결론

R6는 **정책·자본환원·디지털자산이 모두 valuation을 움직이는 섹터**다. 그래서 “좋은 Stage 2”와 “진짜 Green”을 강하게 분리해야 한다.

```text
1. Big-4 금융지주는 value-up Stage 2다.
   하지만 ROE, CET1, credit cost, 반복 소각 전 Stage 3는 아니다.

2. 증권주는 거래대금 cycle의 좋은 수혜지만,
   +13.5% 급등은 brokerage/IB 실적 전 4B-watch다.

3. SK Square는 NAV discount와 소각이 있는 좋은 Stage 2다.
   반복 소각과 discount 축소 전 Green은 아니다.

4. Samsung Life는 Samsung Electronics 지분 매각으로 capital-release Stage 2다.
   K-ICS, CSM, 배당·소각 활용이 Stage 3 조건이다.

5. Hana Bank / Dunamu는 은행권 digital-asset equity option Stage 2다.
   지분법 이익, 규제수익, 자본비율 영향 전 Green 금지다.

6. NAVER / Dunamu는 digital-asset platform Stage 2와 exchange-trust 4C-watch가 동시에 떴다.
   abnormal withdrawal이 곧바로 가격을 뒤집었다.

7. K Bank는 인터넷은행 profitability Stage 2지만 unlisted다.
   KakaoBank는 growth보다 major shareholder governance risk가 먼저다.

8. Stablecoin basket은 R6의 대표적 price_moved_without_evidence다.
   issuer license, reserve income, fee revenue 전 2~3배 상승은 4B다.
```

한 문장으로 압축하면:

> **R6에서 진짜 Stage 3는 “저PBR·밸류업·디지털자산·스테이블코인 수혜”가 아니라, ROE·자본비율·실제 소각·규제수익·지분법 이익·platform trust가 확인되어 PBR 프레임을 바꾸는 순간이다.**

[1]: https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-parliament-approves-commercial-act-revision-aimed-boosting-share-2026-02-25/?utm_source=chatgpt.com "South Korea parliament approves commercial act revision aimed at boosting share valuations"
[2]: https://www.reuters.com/world/asia-pacific/south-koreas-kospi-share-index-tops-7000-first-time-2026-05-06/?utm_source=chatgpt.com "Korea's KOSPI breaks 7,000 as AI rally catapults Samsung into $1 trillion club"
[3]: https://www.reuters.com/technology/artificial-intelligence/south-koreas-ai-chip-investor-announces-plan-share-buybacks-2024-11-21/?utm_source=chatgpt.com "South Korea's AI chip investor announces plan for share buybacks"
[4]: https://www.reuters.com/world/asia-pacific/samsung-life-divest-13-trln-won-worth-samsung-electronics-shares-2026-03-19/?utm_source=chatgpt.com "Samsung Life to divest 1.3 trln won worth of Samsung Electronics' shares"
[5]: https://www.reuters.com/world/asia-pacific/hana-bank-acquire-stake-dunamu-700-mln-filing-says-2026-05-14/?utm_source=chatgpt.com "Hana Bank to acquire stake in Dunamu for $700 mln, filing says"
[6]: https://www.reuters.com/world/asia-pacific/navers-payment-arm-acquire-south-korean-crypto-exchange-operator-10-bln-deal-2025-11-27/?utm_source=chatgpt.com "Naver's payment arm to acquire South Korean crypto exchange operator in $10 bln deal"
[7]: https://www.reuters.com/markets/asia/south-koreas-k-bank-announces-ipo-plan-worth-up-732-million-2024-09-10/?utm_source=chatgpt.com "South Korea's K Bank announces IPO plan worth up to $732 million"
[8]: https://www.ft.com/content/4b19bf90-4202-4fe7-8caf-d7db6deeb768?utm_source=chatgpt.com "Crypto-crazy investors make South Korea the best-performing market in Asia"

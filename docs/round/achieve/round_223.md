순서상 이번은 **R6 Loop 9 — 금융·자본배분·디지털금융 가격경로 검증 라운드**다.

이번 라운드는 은행·증권·보험·지주·인터넷은행·디지털자산을 섞어서 본다. R6의 핵심은 “저PBR이다”, “밸류업이다”, “스테이블코인 수혜다”가 아니라 **ROE·자본비율·실제 소각·주주환원·규제수익·신뢰 리스크가 PBR 프레임을 바꾸는가**다.

```text
round = R6 Loop 9
round_id = round_151
large_sector = FINANCIAL_CAPITAL_DIGITAL
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
```

원시 수정주가 일봉 OHLC는 이번 환경에서 안정적으로 직접 확보하지 못했다. 대신 Reuters / WSJ / FT / Barron’s / 공개 기업정보에 남은 **가격 anchor, 이벤트 수익률, 거래금액, 할인율, 순이익·지분가치 지표**로 계산 가능한 값만 계산했다.

---

# 1. 이번 라운드 대섹터

```text
R6 = 금융·자본배분·디지털금융
```

R6의 핵심 질문은 이거다.

```text
저PBR·밸류업·디지털자산 테마인가?
아니면 실제 ROE, CET1/K-ICS, 소각, 배당, 규제수익, 지분법 이익,
privacy/governance trust가 함께 확인되는가?
```

---

# 2. 대상 canonical archetype

```text
BANK_VALUEUP_ROE_PBR_RERATING
BANK_CAPITAL_RETURN_EXECUTION
SECURITIES_CAPITAL_MARKET_BOOM
HOLDING_NAV_DISCOUNT_VALUEUP
INSURANCE_NAV_CAPITAL_RELEASE
DIGITAL_ASSET_BANK_EQUITY_OPTION
DIGITAL_ASSET_PLATFORM_MERGER
INTERNET_BANK_IPO_PROFITABILITY
INTERNET_BANK_GOVERNANCE_4C
KRW_STABLECOIN_POLICY_THEME
PAYMENT_PRIVACY_REGULATORY_4C
PRICE_ONLY_RALLY
EVENT_PREMIUM
```

---

# 3. deep sub-archetype

```text
은행 밸류업:
- KB Financial
- Shinhan / Hana / Woori
- ROE / CET1 / credit cost / shareholder return
- PBR 1x breakthrough
- 저PBR theme vs actual capital return

증권 / 자본시장:
- securities firms basket
- KOSPI rally
- brokerage revenue / IB revenue / margin loan
- market-cycle revenue vs structural ROE

지주 / NAV:
- SK Square
- SK Hynix stake
- buyback cancellation
- activist engagement
- holding-company discount narrowing

보험 NAV:
- Samsung Life
- Samsung Electronics stake
- book-value discount
- regulatory share sale
- K-ICS / CSM / capital release

디지털자산:
- Hana Bank / Dunamu
- Naver Financial / Dunamu
- Upbit market share
- stablecoin / remittance
- abnormal withdrawal / exchange trust

인터넷은행:
- K Bank IPO
- KakaoBank / Kakao legal overhang
- operating profit vs listing valuation
- major shareholder suitability
```

---

# 4. 국장 신규 후보 case

## Case A — KB금융 중심 은행주 `success_candidate / value-up ROE-PBR rerating`

```text
symbol = 105560
case_type = success_candidate
archetype = BANK_VALUEUP_ROE_PBR_RERATING / BANK_CAPITAL_RETURN_EXECUTION
```

### stage date

```text
Stage 1:
2024-02 이후
- Corporate Value-up programme
- 저PBR 은행주 rerating 기대
- 자사주 소각 / 배당 확대 기대

Stage 2:
2025~2026
- KB Financial 2025 순이익 5.84조 원, +15.1%
- Big 4 financial groups 합산 순이익 nearly 18조 원
- KB가 book value 위로 거래됐다는 보도

Stage 3:
보류
- ROE / CET1 / credit cost / 실제 소각 반복 / 배당성향이 확인되어야 함
- 단순 저PBR과 밸류업 기대만으로 Green 금지

Stage 4B:
은행주가 PBR 1x 근처 또는 이상으로 빠르게 rerating되면 후보

Stage 4C:
PF credit cost, CET1 약화, 주주환원 후퇴, 규제 리스크, 경기둔화 credit shock 시 후보
```

KB금융은 2025년 순이익이 5.84조 원으로 15.1% 증가했고, 국내 Big 4 금융지주 합산 순이익은 nearly 18조 원으로 정리된다. 또 2026년 2월 KB가 처음으로 book value 위로 거래됐다는 보도가 있어, 은행주 저PBR 프레임이 실제 PBR rerating으로 연결될 수 있는 Stage 2 후보로 볼 수 있다. 다만 이 출처는 공개 기업정보 요약 기반이라 `source_confidence = medium_low`로 둔다. ([위키백과][1])

### 실제 가격경로 검증

```text
price_data_source:
public company profile / KED-derived summary via indexed source

stage3_price:
N/A

KB_2025_net_profit:
5.84T won

KB_net_profit_growth:
+15.1%

Big4_financial_groups_2025_net_profit:
nearly 18T won

KB_share_of_Big4_profit:
5.84 / 18.0
= 32.4%

book_value_breakthrough:
reported, source_confidence = medium_low

MFE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search

reason:
- Reuters / WSJ / FT에서 KB금융 개별 event-day OHLC anchor를 찾지 못함.
- KRX / Naver / Yahoo / Stooq 원시 일봉 OHLC 직접 확보 실패.

MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = bank_valueup_ROE_PBR_watch
stage_failure_type = stage2_watch_success
```

---

## Case B — 증권주 / 금융주 basket `cyclical_success + 4B-watch`

```text
symbols = securities basket / financial groups basket
case_type = cyclical_success + 4B-watch
archetype = SECURITIES_CAPITAL_MARKET_BOOM / BANK_VALUEUP_ROE_PBR_RERATING
```

### stage date

```text
Stage 1:
2025~2026
- KOSPI bull market
- 거래대금 / brokerage / IB revenue 기대
- financial value-up 기대

Stage 2:
2026-05-06
- KOSPI 7,000 돌파
- securities firms +13.5%
- financial groups +4.2%
- foreign investors record daily purchase 3.1조 원

Stage 3:
없음
- 증권주/금융주 rally는 Stage 2 또는 cyclical_success
- 실제 brokerage revenue, IB revenue, ROE, credit cost, capital return 확인 전 Green 금지

Stage 4B:
2026-05-06
- securities basket +13.5%
- market-cycle revenue가 가격에 먼저 반영

Stage 4C:
거래대금 급감, margin loan unwind, KOSPI drawdown, IB loss, credit cost spike 시 후보
```

2026년 5월 6일 KOSPI는 7,000을 돌파해 6.45% 상승 마감했고, 증권업 지수는 13.5%, 금융지주는 4.2% 올랐다. 외국인은 3.1조 원을 순매수했고, Reuters는 금융·증권주 상승을 주식시장 호황이 실적을 끌어올릴 것이라는 기대와 연결했다. 이건 R6에서 좋은 Stage 2/cyclical evidence지만, Stage 3는 증권사별 위탁매매·IB·운용손익·ROE로 확인해야 한다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported market-sector return anchors

stage3_price:
N/A

KOSPI_event_return:
+6.45%

KOSPI_intraday_high_return:
+7.06%

securities_firms_event_MFE_1D:
+13.5%

financial_groups_event_MFE_1D:
+4.2%

securities_relative_outperformance_vs_KOSPI:
13.5 - 6.45
= +7.05pp

financial_groups_relative_underperformance_vs_KOSPI:
4.2 - 6.45
= -2.25pp

foreign_net_purchase:
3.1T won / $2.13B

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
success
- 증권업 +13.5%는 event-day 4B-watch 필요.
```

### alignment

```text
score_price_alignment = cyclical_success
rerating_result = capital_market_boom_watch
stage_failure_type = stage2_cyclical_not_green
```

---

## Case C — SK스퀘어 `success_candidate / NAV discount value-up`

```text
symbol = 402340
case_type = success_candidate
archetype = HOLDING_NAV_DISCOUNT_VALUEUP
```

### stage date

```text
Stage 1:
2024년
- SK Hynix NAV discount
- activist engagement
- Korea Value-up programme

Stage 2:
2024-11-21
- 1,000억 원 자사주 소각
- 추가 1,000억 원 매입·소각 계획
- independent director nomination
- SK Hynix 지분 20% 보유

Stage 3:
보류
- 반복 소각
- discount narrowing
- SK Hynix NAV 상승이 SK스퀘어 주주환원으로 연결되는지 확인 필요

Stage 4B:
2026-05
- SK Hynix 대시세 이후 SK Square NAV trade가 대중화되면 후보

Stage 4C:
소각 중단, SK Hynix 급락, discount 재확대, governance 후퇴 시 후보
```

SK스퀘어는 2024년 11월 1,000억 원 자사주 소각과 추가 1,000억 원 매입·소각 계획을 발표했고, SK하이닉스 지분 20%를 보유하고 있음에도 시장가치가 SK하이닉스 지분가치 180억 달러의 절반보다 낮다는 Reuters 보도가 있었다. Barron’s도 2026년 5월 SK스퀘어가 SK하이닉스에 대한 간접 노출을 47% discount로 제공한다고 전했다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / Barron’s valuation anchors

stage3_price:
N/A

cancelled_buyback:
100B won

additional_buyback_cancel_plan:
100B won

total_announced_buyback_cancel_program:
200B won

SK_Hynix_stake:
20%

SK_Hynix_stake_value_2024:
$18B

SK_Square_market_value_vs_stake_value:
less than 50%

minimum_NAV_discount_2024:
>50%

Barrons_discount_2026:
47%

implied_value_capture_ratio_2026:
1 - 0.47
= 53%

MFE / MAE:
price_data_unavailable_after_deep_search

reason:
- Reuters/Barron’s는 valuation anchor는 제공하지만 SK스퀘어 event-day OHLC는 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 일봉 OHLC 직접 확보 실패.
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = NAV_discount_valueup_watch
stage_failure_type = stage2_watch_success
```

---

## Case D — 삼성생명 `success_candidate / insurance NAV capital-release watch`

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
- capital release / value-up 기대

Stage 2:
2026-03-19
- Samsung Life sells 1.3조 원 worth of Samsung Electronics shares
- local financial-company governance regulation risk 대응

Stage 3:
보류
- 매각대금의 배당·소각·자본정책 활용 확인 필요
- K-ICS / CSM / 보험 본업 이익 확인 필요

Stage 4B:
Samsung Electronics NAV rally가 삼성생명 valuation에 과도하게 반영되면 후보

Stage 4C:
규제성 지분매각 반복, 삼성전자 급락, 보험 자본비율 악화, CSM 훼손 시 후보
```

삼성생명은 2026년 3월 삼성전자 지분 1.3조 원을 매각한다고 공시했고, 이는 금융회사 지배구조 규제 리스크를 해소하기 위한 조치로 설명됐다. Barron’s는 삼성생명이 삼성전자 지분 10%를 보유하고 있으며 book value의 약 50% 수준에서 거래된다는 헤지펀드 의견을 전했다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / Barron’s valuation anchors

stage3_price:
N/A

Samsung_Electronics_stake_sale:
1.3T won / $867.07M

Samsung_Electronics_stake_owned:
about 10%

trading_level_vs_book:
about 50%

implied_book_discount:
50%

MFE / MAE:
price_data_unavailable_after_deep_search

reason:
- Reuters/Barron’s는 valuation/regulatory anchor는 제공하지만 삼성생명 event-day 주가 reaction anchor는 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 일봉 OHLC 직접 확보 실패.
```

### alignment

```text
score_price_alignment = success_candidate + regulatory_watch
rerating_result = insurance_NAV_valueup_watch
stage_failure_type = stage2_watch_success
```

---

## Case E — 하나금융 / 하나은행 `success_candidate / regulated digital-asset equity option`

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

Stage 2:
2026-05-14
- Hana Bank acquires 6.55% Dunamu stake
- transaction value 1.003조 원
- Upbit trading volume share >80%
- blockchain remittance technical verification

Stage 3:
보류
- 지분법 이익
- regulatory approval
- capital ratio impact
- digital asset revenue / remittance revenue 확인 필요

Stage 4B:
디지털자산 equity-option 기대가 은행주 valuation에 과도 반영되면 후보

Stage 4C:
거래량 급감, 규제 지연, capital charge, exchange trust incident, crypto market drawdown 시 후보
```

하나은행은 두나무 지분 6.55%를 1.003조 원에 인수하기로 했다. Reuters는 두나무가 Upbit을 운영하고 Upbit이 국내 가상자산 거래량 80% 이상을 처리한다고 설명했고, WSJ는 이 거래가 국내 은행의 디지털자산 업체 투자 중 최대 규모이며 하나은행이 두나무의 4대 주주가 된다고 보도했다. 하나와 두나무는 blockchain 기반 해외송금 기술검증도 완료한 상태로 정리된다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / WSJ transaction anchors

stage3_price:
N/A

transaction_value:
1.003T won

stake_acquired:
6.55%

implied_Dunamu_equity_value:
1.003T / 0.0655
= 약 15.31T won

shares_acquired:
2.284M shares

price_per_Dunamu_share:
1.003T / 2.284M
= 약 439,142원

Upbit_trading_volume_share:
>80%

Kakao_Investment_remaining_stake:
4.03%

MFE / MAE:
price_data_unavailable_after_deep_search

reason:
- Reuters/WSJ는 거래금액과 지분율은 제공하지만 하나금융 event-day OHLC anchor는 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 일봉 OHLC 직접 확보 실패.
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = regulated_digital_asset_equity_option
stage_failure_type = stage2_watch_success
```

---

## Case F — NAVER Financial / Dunamu `event_premium + trust 4C-watch`

```text
symbol = 035420
case_type = success_candidate + event_premium + 4C-watch
archetype = DIGITAL_ASSET_PLATFORM_MERGER
```

### stage date

```text
Stage 1:
2025년
- Naver fintech expansion
- digital asset / stablecoin growth 기대

Stage 2:
2025-11-27
- Naver Financial agrees to acquire Dunamu
- all-stock deal value 15.13조 원 / $10.27B
- Upbit market share about 70%
- exchange ratio 2.54 Naver Financial shares per Dunamu share

Stage 3:
보류
- regulatory approval
- merger closing
- digital asset revenue integration
- exchange volume durability
- trust/security risk 통과 필요

Stage 4B:
2025-11-27
- Naver shares initially +7% 이상

Stage 4C-watch:
2025-11-27
- Upbit abnormal withdrawal 540억 원
- Naver shares later -4.2%
```

NAVER Financial은 Dunamu를 15.13조 원 규모 all-stock deal로 인수하기로 했다. Reuters는 Upbit이 국내 crypto exchange 시장 약 70%를 차지하며 높은 수익성을 가진 플랫폼으로 평가된다고 보도했다. Naver 주가는 인수 뉴스 직후 7% 넘게 올랐지만, 같은 날 Upbit에서 540억 원 규모 비정상 출금이 발생했다는 보도 후 4.2% 하락 전환했다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported event-return and transaction anchors

stage3_price:
N/A

deal_value:
15.13T won / $10.27B

event_MFE_initial:
> +7%

event_MAE_same_day_after_abnormal_withdrawal:
-4.2%

event_swing_from_initial_plus_7_to_minus_4_2:
-11.2pp

abnormal_withdrawal:
54B won

exchange_ratio:
2.54 Naver Financial shares per Dunamu share

Upbit_market_share:
about 70%

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4C 큰 하락 이전 포착 여부:
partial_success
- abnormal withdrawal 뉴스가 당일 4C-watch trigger.
```

### alignment

```text
score_price_alignment = event_premium + trust_watch
rerating_result = digital_asset_platform_watch
stage_failure_type = stage2_watch_success_with_4C_watch
```

---

## Case G — K Bank `success_candidate / internet-bank IPO valuation watch`

```text
symbol = unlisted / IPO candidate
case_type = success_candidate + IPO_watch
archetype = INTERNET_BANK_IPO_PROFITABILITY
```

### stage date

```text
Stage 1:
2024-09-10
- K Bank IPO plan
- South Korea first internet-only bank
- 10M+ customers
- digital bank profitability

Stage 2:
2024-09-10
- planned IPO up to 984B won
- price range 9,500~12,000 won
- valuation up to about 5T won
- 1H 2024 operating profit 86.7B won, more than triple YoY

Stage 3:
없음
- IPO plan / operating profit alone is not Green
- listed price path, credit quality, NIM, funding cost, fee income 확인 필요

Stage 4B:
IPO valuation이 profitability보다 먼저 과도하게 반영되면 후보

Stage 4C:
IPO withdrawal, credit cost, deposit funding pressure, valuation compression 시 후보
```

K Bank는 2024년 9월 최대 9840억 원 IPO 계획을 발표했다. 공모가는 9,500~12,000원, IPO valuation은 최대 5조 원으로 제시됐고, 2024년 상반기 영업이익은 867억 원으로 전년 동기 대비 3배 이상 증가했다. 다만 이건 상장 전 Stage 2 후보이며, 실제 상장 후 가격경로와 ROE·credit cost·NIM 확인 전 Stage 3는 아니다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters IPO plan anchor

stage3_price:
N/A

IPO_status:
unlisted / IPO candidate at report date

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

shares_outstanding:
376M

implied_market_cap_at_12,000:
376M * 12,000
= 4.512T won
Reuters described valuation up to 5T won

1H_2024_operating_profit:
86.7B won

customer_count:
>10M

MFE / MAE:
N/A because not listed in this evidence window
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = internet_bank_IPO_watch
stage_failure_type = stage2_unlisted_not_green
```

---

## Case H — Kakao / KakaoBank `4C-watch / legal-governance overhang`

```text
symbols = 035720 / 323410
case_type = 4C-watch / failed_rerating
archetype = INTERNET_BANK_GOVERNANCE_4C
```

### stage date

```text
Stage 1:
2021~2024
- KakaoBank internet-bank growth
- mobile banking scale
- Kakao ecosystem financial platform

Stage 2:
없음 또는 보류
- ROE, NIM, fee income, credit quality, ownership-risk 해소 필요

Stage 3:
없음
- founder legal risk와 bank ownership-risk 해소 전 Green 금지

Stage 4C-watch:
2024-07-23
- Kakao founder Kim Beom-su arrested
- Kakao shares -3.4%
- Kakao YTD -24%
- conviction could jeopardize KakaoBank control due to >10% bank ownership rule

4C relief:
2025-10-21
- court clears Kim of stock manipulation charges
```

Kakao 창업자 김범수는 2024년 7월 SM Entertainment 인수 과정의 주가조작 혐의로 구속됐고, Kakao 주가는 장중 3.4% 하락해 11월 이후 최저 수준으로 떨어졌으며 연초 대비 24% 하락한 상태였다. Reuters는 금융범죄 유죄가 확정될 경우 한국 법상 은행 지분 10% 초과 보유가 제한될 수 있어 KakaoBank 지배력에 영향을 줄 수 있다고 설명했다. 2025년 10월에는 법원이 김범수에게 무죄를 선고했다. ([Reuters][8])

### 실제 가격경로 검증

```text
price_data_source:
Reuters legal event anchors

stage3_price:
N/A

Kakao_event_MAE_1D:
-3.4%

Kakao_YTD_drawdown_context:
-24%

Kakao_group_assets_context:
86T won / $62B

Kim_controlled_stake:
24%

bank_ownership_cap_risk:
>10% if convicted of financial crime

4C_relief_date:
2025-10-21 acquittal

MFE / MAE for KakaoBank:
price_data_unavailable_after_deep_search

reason:
- Reuters는 Kakao event return은 제공하지만 KakaoBank 직접 event-day OHLC는 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 일봉 OHLC 직접 확보 실패.
```

### alignment

```text
score_price_alignment = thesis_break_watch / legal_governance_watch
rerating_result = internet_bank_governance_overhang
stage_failure_type = should_have_been_red_or_watch
```

---

## Case I — Kakao Pay / stablecoin basket `overheat / price_moved_without_evidence`

```text
symbols = 377300 / LG CNS / Aton / ME2ON
case_type = overheat / price_moved_without_evidence
archetype = KRW_STABLECOIN_POLICY_THEME
```

### stage date

```text
Stage 1:
2025-06
- won stablecoin policy pledge
- crypto/digital-asset reform 기대

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
비은행 발행 제한, 외환리스크 우려, 규제 지연, 실질 revenue 부재 시 후보
```

FT는 원화 스테이블코인 기대 속에 Kakao Pay가 한 달 동안 두 배 이상, LG CNS가 약 70%, Aton이 80%, ME2ON이 세 배 올랐다고 보도했다. 하지만 정부의 crypto regulatory framework는 아직 명확하지 않았고, 한국은행은 비은행 스테이블코인 발행이 통화정책과 자본흐름에 부담을 줄 수 있다고 우려했다. ([Financial Times][9])

### 실제 가격경로 검증

```text
price_data_source:
FT reported return anchors

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

Stage 4B peak-before 여부:
success
- 실제 수익모델 전 2~3배 상승은 4B/event premium.
```

### alignment

```text
score_price_alignment = price_moved_without_evidence
rerating_result = stablecoin_policy_theme_overheat
stage_failure_type = should_have_been_stage1_or_4B_watch
```

---

# 5. 이번 R6 case별 요약표

| case                        | 분류                            |                                                            실제 가격검증 | alignment                    |
| --------------------------- | ----------------------------- | -----------------------------------------------------------------: | ---------------------------- |
| KB금융 / 은행주                  | success_candidate             |                          2025 NP 5.84T, +15.1%; Big4 NP nearly 18T | value-up watch               |
| 증권주 / 금융주 basket            | cyclical_success + 4B         |            securities +13.5%, financial groups +4.2%, KOSPI +6.45% | cyclical_success             |
| SK스퀘어                       | success_candidate             | 200B won buyback/cancel programme, SKH stake 20%, discount 47~50%+ | NAV value-up                 |
| 삼성생명                        | success_candidate             |     Samsung Electronics stake sale 1.3T, 10% stake, 50% book value | NAV capital release          |
| 하나금융 / Dunamu               | success_candidate             |                      1.003T for 6.55%, implied Dunamu value 15.31T | digital-asset equity option  |
| NAVER / Dunamu              | event + trust watch           |                  15.13T deal, +7% → -4.2%, abnormal withdrawal 54B | event + 4C-watch             |
| K Bank                      | success_candidate / IPO watch |                      IPO max 984B, valuation up to 5T, 1H OP 86.7B | unlisted Stage 2             |
| Kakao / KakaoBank           | 4C-watch                      |                         Kakao -3.4%, YTD -24%, bank ownership-risk | legal-governance watch       |
| Kakao Pay stablecoin basket | overheat                      |                      Kakao Pay >2x, ME2ON 3x, no regulated revenue | price_moved_without_evidence |

---

# 6. score-price alignment 판정

```text
success_candidate:
- KB금융 / 은행주 value-up
- SK스퀘어
- 삼성생명
- 하나금융 / Dunamu
- K Bank

cyclical_success:
- 증권주 / 금융주 basket

event_premium:
- NAVER Financial / Dunamu
- Kakao Pay stablecoin basket

price_moved_without_evidence:
- Kakao Pay / LG CNS / Aton / ME2ON stablecoin basket

thesis_break_watch:
- Kakao / KakaoBank legal-governance risk
- NAVER / Upbit abnormal withdrawal trust watch

4B-watch:
- 증권주 +13.5%
- stablecoin basket 2~3배
- NAVER / Dunamu initial +7%
- SK Square / Samsung Life NAV trade가 underlying rally 뒤 crowded해질 경우

4C-watch:
- KakaoBank ownership-risk
- Upbit abnormal withdrawal
- privacy/data trust events
- credit cost / PF risk for banks
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
```

### 왜 올리나

SK스퀘어는 실제 소각과 추가 매입·소각 계획이 있고, 하나은행은 1조 원을 들여 두나무 지분을 취득하면서 regulated digital-asset equity option을 만들었다. 삼성생명은 삼성전자 지분과 book-value discount가 있지만, 매각대금의 주주환원 연결을 확인해야 한다. ([Reuters][3])

## 내릴 축

```text
low_pbr_only -5
policy_valueup_only -4
treasury_buyback_without_cancellation -4
stablecoin_policy_theme_only -5
digital_asset_equity_option_without_revenue -3
fintech_user_growth_without_profit -3
privacy_or_data_trust_break -5
major_shareholder_legal_risk -5
capital_ratio_weakening -4
mna_expansion_without_capital_buffer -3
event_rally_before_regulated_revenue -5
```

### 왜 내리나

스테이블코인 basket은 실제 발행권·수수료·reserve income 없이 2~3배 급등이 먼저 나왔다. KakaoBank는 인터넷은행 성장성보다 대주주 법적 리스크와 은행 지분 규제가 먼저 작동했다. NAVER/Dunamu도 acquisition news 후 +7%에서 Upbit abnormal withdrawal 이슈로 -4.2% 전환했다. ([Financial Times][9])

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
8. privacy / data / governance hard risk 없음
9. 가격경로가 evidence 이후 따라옴

금지:
저PBR만 있음
밸류업 정책 기대만 있음
자사주 매입만 있고 소각 없음
스테이블코인 테마만 있음
비은행 인수 후 자본비율 불명
대주주 법적 리스크
개인정보·거래소 신뢰 훼손
```

## 4B 조기감지 조건

```text
4B-watch:
은행·보험주가 PBR rerating 후 book value에 근접하거나 상회
자사주 소각 뉴스가 반복되어 surprise가 사라짐
NAV rally가 지주·보험주에 과도 반영
증권주가 거래대금 cycle 하나로 +10% 이상 급등
스테이블코인 관련주가 실제 수익모델 없이 2~3배 급등
디지털자산 지분투자가 거래량 peak와 맞물림
M&A/stock-swap event가 regulatory approval 전 가격에 선반영

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
privacy / data transfer fine
스테이블코인 외환리스크 규제 강화
디지털자산 거래량 급감
거래소 보안사고 / abnormal withdrawal
지분투자 손상
```

이번 라운드에서는 **Kakao/KakaoBank legal risk와 Upbit abnormal withdrawal은 4C-watch**, **stablecoin basket은 price_moved_without_evidence**, **KB·SK Square·Samsung Life·Hana는 Stage 2 success_candidate**로 둔다.

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

## docs/round/round_151.md 요약

```md
# R6 Loop 9. Financial / Capital Allocation / Digital Finance Price Validation

이번 라운드는 R6 Loop 9 price-validation 라운드다.

핵심 결론:
- KB금융은 은행 value-up Stage 2 후보로 본다. 2025년 순이익 5.84조 원, +15.1%, Big4 금융지주 합산 nearly 18조 원 중 32.4% 비중이다. 다만 ROE/CET1/소각 반복 확인 전 Stage 3는 보류한다.
- 증권주 basket은 KOSPI 7,000 돌파일 +13.5%, 금융지주 +4.2%로 cyclical_success다. 거래대금과 brokerage/IB revenue 확인 전 Green 금지다.
- SK스퀘어는 2,000억 원 buyback/cancel programme과 SK하이닉스 NAV discount로 Stage 2 value-up 후보지만, 반복 소각과 discount narrowing 가격경로가 Stage 3 조건이다.
- 삼성생명은 삼성전자 지분 1.3조 원 매각과 book value 50% discount로 NAV capital-release 후보지만, 매각대금 활용과 K-ICS/CSM 확인 전 Green 금지다.
- 하나금융은 두나무 6.55%를 1.003조 원에 인수해 implied Dunamu value 약 15.31조 원을 만든다. 규제수익·지분법·자본비율 확인 전 Stage 3는 아니다.
- NAVER/Dunamu는 15.13조 원 all-stock deal로 강한 Stage 2지만, Upbit abnormal withdrawal 540억 원으로 trust 4C-watch가 동시에 붙는다.
- K Bank는 IPO 계획 기준 Stage 2 후보지만, 상장 후 가격경로와 credit quality/NIM 확인 전 Green 금지다.
- Kakao/KakaoBank는 founder legal risk와 bank ownership cap risk가 Green을 막는 4C-watch다.
- Kakao Pay/stablecoin basket은 실제 규제수익 전 2~3배 급등한 price_moved_without_evidence다.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 151 R6 Loop 9 Financial Capital Digital Price Validation

## 반영 내용
- R6 Loop 9 price-validation 라운드를 추가했다.
- Bank value-up, securities-cycle, NAV holding-company discount, insurance NAV, bank digital-asset equity option, digital-asset platform merger, internet-bank IPO, legal-governance risk, stablecoin policy overheat를 비교했다.
- Reuters/WSJ/FT/Barron’s/public company profiles reported anchors로 가능한 MFE/MAE 및 transaction/valuation metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- ROE sustainability, capital buffer, real buyback cancellation, capital release, regulated digital revenue 가중치 강화
- low-PBR only, stablecoin policy theme only, event rally before revenue, legal-governance risk, exchange trust break 감점 강화
- R6 4B-watch와 digital-asset 4C-watch 민감도 강화
```

## case row 초안

```jsonl
{"case_id":"r6_loop9_kb_financial_bank_valueup","symbol":"105560","company_name":"KB금융","case_type":"success_candidate","primary_archetype":"BANK_VALUEUP_ROE_PBR_RERATING","stage2_date":"2025-2026","price_validation":{"price_data_source":"public company profile / KED-derived summary via indexed source","stage3_price":null,"kb_2025_net_profit_krw_trn":5.84,"kb_net_profit_growth_pct":15.1,"big4_2025_net_profit_krw_trn":18.0,"kb_share_of_big4_profit_pct":32.4,"book_value_breakthrough_reported":true,"source_confidence":"medium_low","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"bank_valueup_ROE_PBR_watch","notes":"Value-up Stage 2 candidate; Stage 3 requires ROE/CET1/credit cost and repeated shareholder return execution."}
{"case_id":"r6_loop9_securities_financial_basket_capital_market_boom","symbol":"securities_basket/financial_groups_basket","company_name":"증권주/금융주 basket","case_type":"cyclical_success","primary_archetype":"SECURITIES_CAPITAL_MARKET_BOOM","stage2_date":"2026-05-06","stage4b_date":"2026-05-06","price_validation":{"price_data_source":"Reuters reported sector return anchors","stage3_price":null,"kospi_event_return_pct":6.45,"kospi_intraday_high_return_pct":7.06,"securities_firms_mfe_1d_pct":13.5,"financial_groups_mfe_1d_pct":4.2,"securities_relative_outperformance_pp":7.05,"financial_groups_relative_underperformance_pp":-2.25,"foreign_net_purchase_krw_trn":3.1,"price_validation_status":"reported_sector_return_not_full_ohlc"},"score_price_alignment":"cyclical_success","rerating_result":"capital_market_boom_watch","notes":"Securities rally is Stage 2/cyclical; brokerage/IB revenue, ROE and risk controls required before Green."}
{"case_id":"r6_loop9_sk_square_nav_discount_valueup","symbol":"402340","company_name":"SK스퀘어","case_type":"success_candidate","primary_archetype":"HOLDING_NAV_DISCOUNT_VALUEUP","stage2_date":"2024-11-21","stage4b_date":"2026-05","price_validation":{"price_data_source":"Reuters/Barron's valuation anchors","stage3_price":null,"cancelled_buyback_krw_bn":100,"additional_buyback_cancel_plan_krw_bn":100,"total_buyback_cancel_program_krw_bn":200,"sk_hynix_stake_pct":20,"sk_hynix_stake_value_2024_usd_bn":18,"minimum_nav_discount_2024_pct":50,"barrons_discount_2026_pct":47,"implied_value_capture_ratio_2026_pct":53,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"NAV_discount_valueup_watch","notes":"Actual cancellation supports Stage 2; repeated cancellation and discount narrowing required for Stage 3."}
{"case_id":"r6_loop9_samsung_life_nav_capital_release","symbol":"032830","company_name":"삼성생명","case_type":"success_candidate","primary_archetype":"INSURANCE_NAV_CAPITAL_RELEASE","stage2_date":"2026-03-19","price_validation":{"price_data_source":"Reuters/Barron's valuation anchors","stage3_price":null,"samsung_electronics_stake_sale_krw_trn":1.3,"samsung_electronics_stake_sale_usd_mn":867.07,"samsung_electronics_stake_owned_pct":10,"trading_level_vs_book_pct":50,"implied_book_discount_pct":50,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_regulatory_watch","rerating_result":"insurance_NAV_valueup_watch","notes":"Hidden NAV and capital release are Stage 2; use of proceeds, K-ICS/CSM and shareholder return required for Stage 3."}
{"case_id":"r6_loop9_hana_dunamu_equity_option","symbol":"086790","company_name":"하나금융/하나은행","case_type":"success_candidate","primary_archetype":"DIGITAL_ASSET_BANK_EQUITY_OPTION","stage2_date":"2026-05-14","price_validation":{"price_data_source":"Reuters/WSJ transaction anchors","stage3_price":null,"transaction_value_krw_trn":1.003,"stake_acquired_pct":6.55,"implied_dunamu_equity_value_krw_trn":15.31,"shares_acquired_mn":2.284,"price_per_dunamu_share_krw":439142,"upbit_trading_volume_share_pct":80,"kakao_investment_remaining_stake_pct":4.03,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"regulated_digital_asset_equity_option","notes":"Dunamu stake is Stage 2; regulated revenue, equity-method earnings, capital impact and exchange trust required for Stage 3."}
{"case_id":"r6_loop9_naver_dunamu_platform_merger_trust_watch","symbol":"035420","company_name":"NAVER / NAVER Financial / Dunamu","case_type":"success_candidate","primary_archetype":"DIGITAL_ASSET_PLATFORM_MERGER","stage2_date":"2025-11-27","stage4b_date":"2025-11-27","stage4c_date":"2025-11-27","price_validation":{"price_data_source":"Reuters event-return and transaction anchors","stage3_price":null,"deal_value_krw_trn":15.13,"deal_value_usd_bn":10.27,"event_mfe_initial_pct":7.0,"event_mae_same_day_pct":-4.2,"event_swing_pp":-11.2,"abnormal_withdrawal_krw_bn":54,"exchange_ratio_naver_financial_per_dunamu":2.54,"upbit_market_share_pct":70,"price_validation_status":"reported_event_return_not_full_ohlc"},"score_price_alignment":"event_premium_trust_watch","rerating_result":"digital_asset_platform_watch","notes":"Strong Stage 2 digital-asset merger, but abnormal withdrawal creates exchange-trust 4C-watch."}
{"case_id":"r6_loop9_kbank_internet_bank_ipo_watch","symbol":"unlisted_KBank","company_name":"K Bank","case_type":"success_candidate","primary_archetype":"INTERNET_BANK_IPO_PROFITABILITY","stage2_date":"2024-09-10","price_validation":{"price_data_source":"Reuters IPO plan anchor","stage3_price":null,"ipo_status":"unlisted_ipo_candidate","ipo_raise_max_krw_bn":984,"ipo_price_range_krw":"9500-12000","shares_to_sell_mn":82,"new_shares_mn":41,"existing_shares_mn":41,"max_offer_value_check_krw_bn":984,"shares_outstanding_mn":376,"implied_market_cap_at_12000_krw_trn":4.512,"reported_valuation_up_to_krw_trn":5.0,"h1_2024_operating_profit_krw_bn":86.7,"customer_count_mn":10,"price_validation_status":"unlisted_no_stock_ohlc"},"score_price_alignment":"success_candidate","rerating_result":"internet_bank_IPO_watch","notes":"IPO profitability Stage 2 candidate; listed price path, ROE/NIM/credit cost required before Green."}
{"case_id":"r6_loop9_kakao_kakaobank_legal_governance_watch","symbol":"035720/323410","company_name":"Kakao / KakaoBank","case_type":"4c_watch","primary_archetype":"INTERNET_BANK_GOVERNANCE_4C","stage4c_date":"2024-07-23","price_validation":{"price_data_source":"Reuters legal event anchors","stage3_price":null,"kakao_event_mae_1d_pct":-3.4,"kakao_ytd_drawdown_context_pct":-24,"kakao_group_assets_krw_trn":86,"kim_controlled_stake_pct":24,"bank_ownership_cap_risk_pct":10,"legal_relief_date":"2025-10-21 acquittal","price_validation_status":"reported_event_return_not_full_ohlc_for_kakao_kakaobank_ohlc_unavailable"},"score_price_alignment":"thesis_break_watch","rerating_result":"internet_bank_governance_overhang","notes":"Major shareholder legal risk blocks KakaoBank Green until ownership-risk and profitability metrics clear."}
{"case_id":"r6_loop9_stablecoin_policy_theme_overheat","symbol":"377300/LG_CNS/158430/ME2ON","company_name":"Kakao Pay / stablecoin basket","case_type":"overheat","primary_archetype":"KRW_STABLECOIN_POLICY_THEME","stage1_date":"2025-06","stage4b_date":"2025-06","price_validation":{"price_data_source":"FT reported return anchors","stage3_price":null,"kakao_pay_mfe_month_pct":100,"lg_cns_mfe_month_pct":70,"aton_mfe_month_pct":80,"me2on_mfe_month_pct":200,"margin_loan_context_krw_trn":20.5,"regulated_revenue_confirmed":false,"issuer_license_confirmed":false,"reserve_income_confirmed":false,"price_validation_status":"reported_return_anchor_not_full_ohlc"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"stablecoin_policy_theme_overheat","notes":"Stablecoin theme rallied before licensed issuer, reserve income, fee revenue or regulatory capital clarity."}
```

## shadow weight row 초안

```csv
archetype,roe,capital_buffer,buyback_cancel,shareholder_return,pbr_roe_gap,credit_cost,regulated_revenue,nav_monetization,event_penalty,privacy_governance_redteam,4b_watch_sensitivity,hard_4c_sensitivity,notes
BANK_VALUEUP_ROE_PBR_RERATING,+5,+5,+4,+5,+5,+5,+0,+0,-3,+2,+4,+4,KB/bank value-up needs ROE/CET1/credit cost and repeated shareholder return.
SECURITIES_CAPITAL_MARKET_BOOM,+4,+3,+0,+2,+3,+3,+0,+0,-3,+2,+5,+4,Securities +13.5% is cyclical; revenue/ROE must confirm before Green.
HOLDING_NAV_DISCOUNT_VALUEUP,+2,+2,+5,+5,+5,+1,+0,+5,-2,+2,+4,+3,SK Square needs actual cancellation and discount narrowing.
INSURANCE_NAV_CAPITAL_RELEASE,+3,+5,+1,+4,+5,+3,+0,+5,-2,+3,+4,+4,Samsung Life needs use of proceeds and K-ICS/CSM confirmation.
DIGITAL_ASSET_BANK_EQUITY_OPTION,+2,+4,+0,+1,+2,+2,+5,+2,-3,+4,+5,+4,Hana/Dunamu is Stage 2 until regulated revenue and capital impact confirm.
DIGITAL_ASSET_PLATFORM_MERGER,+2,+3,+0,+1,+2,+2,+5,+1,-4,+5,+5,+5,Naver/Dunamu has exchange-trust 4C-watch from abnormal withdrawal.
INTERNET_BANK_IPO_PROFITABILITY,+5,+4,+0,+1,+4,+5,+2,+0,-4,+3,+5,+4,K Bank IPO candidate needs listed price path, ROE/NIM/credit quality.
INTERNET_BANK_GOVERNANCE_4C,+0,+0,+0,+0,+0,+0,+0,+0,-3,+5,+3,+5,KakaoBank Green blocked by major shareholder legal/ownership risk.
KRW_STABLECOIN_POLICY_THEME,+0,+1,+0,+0,+1,+0,+1,+0,-5,+4,+5,+4,Stablecoin rally is price_moved_without_evidence until licensing/revenue clarity.
```

---

# 이번 R6 Loop 9 결론

R6는 Stage 3 후보가 있지만, **저PBR과 정책 기대를 너무 쉽게 Green으로 올리면 바로 망가진다.**

```text
1. KB금융과 은행주는 value-up Stage 2 후보가 될 수 있다.
   하지만 ROE, CET1, credit cost, 실제 소각 반복 전 Stage 3는 보류해야 한다.

2. 증권주는 KOSPI bull market에서 +13.5% 급등했지만,
   이건 cyclical_success다. brokerage/IB revenue와 ROE 확인 전 Green이 아니다.

3. SK스퀘어와 삼성생명은 NAV discount 후보지만,
   NAV가 주주환원·capital release로 연결되는지 확인해야 Stage 3다.

4. 하나금융의 두나무 지분 인수는 강한 Stage 2다.
   하지만 규제수익, 지분법 이익, 자본비율 영향 확인 전 Stage 3는 아니다.

5. NAVER/Dunamu는 디지털자산 플랫폼 Stage 2 후보이면서 동시에 exchange-trust 4C-watch다.
   acquisition news 후 +7%에서 abnormal withdrawal 이슈로 -4.2% 전환했다.

6. K Bank는 IPO 후보로 Stage 2는 가능하지만,
   상장 후 가격경로와 ROE/NIM/credit quality 전 Green 금지다.

7. KakaoBank는 internet bank growth보다 major shareholder legal risk가 먼저다.

8. stablecoin basket은 R6의 대표적인 price_moved_without_evidence다.
   실제 발행권·reserve income·fee revenue 전 2~3배 상승은 4B/Event Premium이다.
```

한 문장으로 압축하면:

> **R6에서 진짜 Stage 3는 “저PBR·밸류업·디지털자산 수혜”가 아니라, ROE·자본비율·실제 소각·주주환원·규제수익이 확인되어 PBR 프레임을 바꾸는 순간이다.**
> **R6는 디지털자산/스테이블코인 테마가 가격을 너무 빨리 앞질러 가므로, event premium과 privacy/governance/exchange-trust 4C gate를 강하게 둬야 한다.**

[1]: https://en.wikipedia.org/wiki/KB_Financial_Group?utm_source=chatgpt.com "KB Financial Group"
[2]: https://www.reuters.com/world/asia-pacific/south-koreas-kospi-share-index-tops-7000-first-time-2026-05-06/?utm_source=chatgpt.com "Korea's KOSPI breaks 7,000 as AI rally catapults Samsung into $1 trillion club"
[3]: https://www.reuters.com/technology/artificial-intelligence/south-koreas-ai-chip-investor-announces-plan-share-buybacks-2024-11-21/?utm_source=chatgpt.com "South Korea's AI chip investor announces plan for share buybacks"
[4]: https://www.reuters.com/world/asia-pacific/samsung-life-divest-13-trln-won-worth-samsung-electronics-shares-2026-03-19/?utm_source=chatgpt.com "Samsung Life to divest 1.3 trln won worth of Samsung Electronics' shares"
[5]: https://www.reuters.com/world/asia-pacific/hana-bank-acquire-stake-dunamu-700-mln-filing-says-2026-05-14/?utm_source=chatgpt.com "Hana Bank to acquire stake in Dunamu for $700 mln, filing says"
[6]: https://www.reuters.com/world/asia-pacific/navers-payment-arm-acquire-south-korean-crypto-exchange-operator-10-bln-deal-2025-11-27/?utm_source=chatgpt.com "Naver's payment arm to acquire South Korean crypto exchange operator in $10 bln deal"
[7]: https://www.reuters.com/markets/asia/south-koreas-k-bank-announces-ipo-plan-worth-up-732-million-2024-09-10/?utm_source=chatgpt.com "South Korea's K Bank announces IPO plan worth up to $732 million"
[8]: https://www.reuters.com/technology/south-korean-court-approves-arrest-warrant-kakao-founder-2024-07-22/?utm_source=chatgpt.com "Founder of South Korea's Kakao arrested for suspected stock manipulation"
[9]: https://www.ft.com/content/4b19bf90-4202-4fe7-8caf-d7db6deeb768?utm_source=chatgpt.com "Crypto-crazy investors make South Korea the best-performing market in Asia"

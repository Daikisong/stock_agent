순서상 이번은 **R6 Loop 8 — 금융·자본배분·디지털금융 가격경로 검증 라운드**다.

이번 라운드는 원시 수정주가 일봉 OHLC를 안정적으로 직접 추출하지 못한 종목에 대해 숫자를 지어내지 않고, **Reuters / FT / WSJ / Barron’s에 남은 가격 anchor, 이벤트 수익률, 할인율, 지분가치, 거래금액**으로 계산 가능한 값만 계산했다.

```text
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
```

---

# 1. 이번 라운드 대섹터

```text
R6 = 금융·자본배분·디지털금융
large_sector = FINANCIAL_CAPITAL_DIGITAL
round = R6 Loop 8 / price-path validation
```

R6의 기본 검증축은 `roe`, `capital_ratio`, `csm`, `loss_ratio`, `buyback_cancel`, `pbr_roe_gap`, `regulated_revenue`다. R6는 은행·보험·증권·밸류업·지주사 구조조정·결제·핀테크·디지털자산/토큰화를 다루지만, 핵심은 **저PBR/정책 테마가 아니라 ROE·자본비율·실제 소각·주주환원·규제수익이 PBR 프레임을 바꾸는가**다. 

Round 119 기준으로 R6에서 부족한 증거는 `low_pbr`, `policy_valueup`이고, 필요한 증거는 `roe`, `cet1`, `buyback_cancellation`, `shareholder_return`, `credit_cost`다. Green blocker는 `pf_credit_cost`, `capital_ratio_weak`, `event_premium_only`다. 

---

# 2. 대상 canonical archetype

```text
VALUE_UP_SHAREHOLDER_RETURN
HOLDING_RESTRUCTURING_GOVERNANCE
TREASURY_SHARE_CANCEL_EXECUTION
FINANCIAL_SPREAD_BALANCE_SHEET
BANK_HOLDING_VALUEUP_CAPITAL_RETURN
BANK_ROE_PBR_RERATING_KOREA
INSURANCE_NAV_VALUEUP_SAMSUNG_ELECTRONICS_STAKE
INSURANCE_CAPITAL_RELEASE_VALUEUP
DIGITAL_ASSET_BANK_EQUITY_OPTION
REGULATED_STABLECOIN_INFRA
KRW_STABLECOIN_POLICY_THEME
PAYMENT_FINTECH_INFRA
PAYMENT_PRIVACY_REGULATORY_4C
PLATFORM_GOVERNANCE_LEGAL_RISK
DIGITAL_ASSET_THEME_OVERHEAT
PRICE_ONLY_RALLY
```

이번 R6의 핵심 질문은 이거다.

```text
저PBR·밸류업·스테이블코인·디지털자산 테마인가?
아니면 실제 소각·ROE·자본비율·규제수익·PBR 재평가가 확인되는가?
```

---

# 3. deep sub-archetype

```text
지주사 밸류업:
- SK Square
- SK Hynix NAV discount
- buyback cancellation
- activist engagement
- value-up index
- holding-company discount narrowing
- 4B if SK Hynix rally saturates

은행 / 디지털자산:
- Hana Bank / Hana Financial
- Dunamu / Upbit stake
- regulated digital asset equity option
- stablecoin remittance / blockchain business
- capital ratio impact
- regulatory approval

보험 NAV:
- Samsung Life
- Samsung Electronics stake
- book-value discount
- forced share divestment
- capital release
- K-ICS / CSM
- use of proceeds / shareholder return

핀테크 / 디지털자산:
- Naver Financial / Dunamu merger
- Kakao Pay stablecoin rally
- Aton / ME2ON crypto policy rally
- Upbit abnormal withdrawal
- non-bank stablecoin systemic risk

인터넷은행 / governance:
- KakaoBank
- Kakao founder legal risk
- major shareholder suitability
- bank ownership cap
- digital bank profitability vs legal overhang

결제 / privacy:
- Kakao Pay
- user data transfer to Alipay Singapore
- FSS fine
- payment trust / data trust hard gate
```

---

# 4. 국장 신규 후보 case

## Case A — SK스퀘어 `structural_success 후보 / value-up NAV discount`

```text
symbol = 402340
case_type = structural_success 후보
archetype = VALUE_UP_SHAREHOLDER_RETURN / HOLDING_RESTRUCTURING_GOVERNANCE
```

### evidence

2024년 11월 21일 SK스퀘어는 1,000억 원 규모 자사주 소각과 추가 1,000억 원 자사주 매입·소각 계획을 발표했다. Reuters는 이 조치가 Palliser Capital의 저평가 해소 요구와 한국 정부의 Value-Up 프로그램 흐름 속에서 나왔고, SK스퀘어가 SK하이닉스 지분 20%를 보유하고 있음에도 시장가치는 그 지분가치의 절반보다 낮다고 보도했다. ([Reuters][1])

2026년 5월 Barron’s는 SK스퀘어가 SK하이닉스에 대한 간접 노출을 제공하면서도 SK하이닉스 대비 47% 할인되어 거래된다는 헤지펀드 의견을 전했다. 같은 맥락에서 한국 증시의 기업지배구조·자본배분 개혁이 Korea discount 축소 catalyst로 언급됐다. ([Barron's][2])

### stage date

```text
Stage 1:
2024년
- Value-Up program
- SK Hynix 지분가치 대비 holding-company discount
- activist engagement

Stage 2:
2024-11-21
- 1,000억 원 자사주 소각
- 추가 1,000억 원 매입·소각 계획
- independent director nomination

Stage 3:
조건부 후보
- 반복적인 소각
- SK하이닉스 NAV 상승이 SK스퀘어 주주환원으로 연결
- discount narrowing이 가격경로로 확인될 때

Stage 4B:
2026-05
- SK하이닉스 대시세 후 SK스퀘어 discount trade가 대중화된 구간
- 47% discount가 여전히 남아 있지만, AI/HBM valuation crowding과 연결됨

Stage 4C:
소각 중단, discount 재확대, SK하이닉스 급락, governance 후퇴 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters / Barron’s reported valuation anchors

stage3_price:
price_data_unavailable_after_deep_search
- Reuters와 Barron’s는 SK스퀘어 주가 OHLC anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

buyback_cancelled:
100 billion won

additional_buyback_cancel_plan:
100 billion won

total_announced_buyback_cancel_program:
200 billion won

SK_Hynix_stake:
20%

SK_Square_market_value_vs_SK_Hynix_stake_value:
less than 50% in 2024 Reuters report

discount_to_SK_Hynix_exposure_2026:
47%

implied_value_capture_ratio:
1 - 0.47 = 53%

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
price_data_unavailable_after_deep_search

peak_price:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = NAV_discount_valueup_watch
stage_failure_type = stage2_watch_success 후보
```

### 교정

SK스퀘어는 R6에서 `buyback_cancellation`, `NAV_discount`, `activist_engagement`, `holding_discount_narrowing`을 올려준다. 다만 Stage 3는 단순 저평가가 아니라 **반복 소각과 실제 discount 축소 가격경로**로 확정해야 한다.

---

## Case B — 하나금융 / 하나은행 `success_candidate / regulated digital-asset equity option`

```text
symbol = 086790
case_type = success_candidate
archetype = DIGITAL_ASSET_BANK_EQUITY_OPTION / REGULATED_STABLECOIN_INFRA
```

### evidence

2026년 5월 14일 하나은행은 업비트 운영사 두나무 지분 6.55%를 1조 원, 약 7억 달러에 인수한다고 공시했다. Reuters는 업비트가 국내 가상자산 거래량의 80% 이상을 처리하고, 두나무가 높은 수익성을 가진 플랫폼이라고 설명했다. ([Reuters][3])

WSJ는 같은 거래가 한국 은행의 디지털자산 업체 투자 중 가장 큰 단일 투자이며, 하나은행이 두나무의 4대 주주가 된다고 보도했다. 하나금융 회장은 이 투자가 디지털자산 기반 금융혁신을 가속하기 위한 전략적 결정이라고 설명했고, 하나와 두나무는 블록체인 기반 해외송금 서비스 기술검증을 마친 상태로 보도됐다. ([월스트리트저널][4])

### stage date

```text
Stage 1:
2025~2026
- 원화 스테이블코인 정책 기대
- 디지털자산 제도화 기대

Stage 2:
2026-05-14
- 하나은행, 두나무 6.55% 지분 1조 원 인수
- Upbit 거래량 80% 이상
- blockchain remittance 기술검증

Stage 3:
보류
- 지분법 이익
- 규제 승인
- 자본비율 영향
- 실제 디지털자산 수익화 확인 필요

Stage 4B:
디지털자산/스테이블코인 테마로 은행주가 선반영되면 후보

Stage 4C:
가상자산 거래량 급감, 규제 지연, 자본규제 강화, 스테이블코인 외환 리스크 현실화 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters / WSJ transaction anchors

stage3_price:
N/A

stage2_price:
price_data_unavailable_after_deep_search
- Reuters/WSJ는 하나금융 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

transaction_value:
1.003 trillion won, approx $672.5M-$700M

stake_acquired:
6.55%

implied_Dunamu_equity_value:
1.003T / 0.0655
= 약 15.31 trillion won

Upbit_market_share:
>80% by Reuters, about 70% by some reports cited in Naver/Dunamu deal

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

peak_price:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = regulated_digital_asset_equity_option
stage_failure_type = stage2_watch_success 후보
```

### 교정

하나금융은 R6에서 `regulated_digital_asset_equity_option`을 Stage 2로 인정할 수 있다. 하지만 Stage 3는 **지분법 이익·규제수익·자본비율 영향·거래량 지속성** 확인 뒤다.

---

## Case C — 삼성생명 `success_candidate / NAV value-up + regulatory watch`

```text
symbol = 032830
case_type = success_candidate + regulatory_watch
archetype = INSURANCE_NAV_VALUEUP_SAMSUNG_ELECTRONICS_STAKE / INSURANCE_CAPITAL_RELEASE_VALUEUP
```

### evidence

2026년 3월 19일 삼성생명은 삼성전자 지분 1.3조 원, 약 8.67억 달러어치를 매각한다고 공시했다. 회사는 금융회사 지배구조 관련 국내 규제 리스크를 해소하기 위한 조치라고 설명했다. ([Reuters][5])

2026년 5월 Barron’s는 삼성생명이 삼성전자 지분 10%를 보유하면서도 약 50%의 book value 수준에서 거래된다는 헤지펀드 의견을 전했다. 즉 이 케이스는 `hidden NAV + regulation + capital release`가 섞인 구조다. ([Barron's][2])

### stage date

```text
Stage 1:
2025~2026
- Samsung Electronics AI rally
- 삼성전자 지분가치 부각
- 보험 NAV value-up 기대

Stage 2:
2026-03-19
- 삼성전자 지분 1.3조 원 매각 발표
- 금융회사 지배구조 규제 리스크 대응

Stage 3:
보류
- 매각대금 활용
- 배당/소각
- K-ICS/CSM
- 보험 본업 이익 확인 필요

Stage 4B:
삼성전자 NAV discount 축소가 가격에 과도하게 반영되면 후보

Stage 4C:
규제성 지분매각 반복, 삼성전자 주가 급락, 보험 자본비율 악화 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters / Barron’s valuation anchors

stage3_price:
N/A

stage2_price:
price_data_unavailable_after_deep_search
- Reuters는 삼성생명 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

Samsung_Electronics_stake_sale:
1.3 trillion won

Samsung_Electronics_stake_owned:
about 10%

trading_level:
about 50% of book value

implied_book_discount:
50%

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

peak_price:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate + regulatory_watch
rerating_result = NAV_valueup_candidate
stage_failure_type = stage2_watch_success 후보
```

### 교정

삼성생명은 `hidden_NAV`, `book_value_discount`, `capital_release`를 올려줄 수 있다. 하지만 규제성 매각과 매각대금 활용이 불명확하면 Green은 보류한다.

---

## Case D — 네이버파이낸셜 / 두나무 `event_premium + success_candidate`

```text
symbol = 035420
case_type = success_candidate + event_premium
archetype = DIGITAL_ASSET_TOKENIZATION / DIGITAL_ASSET_THEME_OVERHEAT
```

### evidence

2025년 11월 27일 네이버파이낸셜은 업비트 운영사 두나무를 15.13조 원, 약 102.7억 달러 규모의 주식교환으로 인수하기로 했다. Reuters는 두나무가 국내 최대 가상자산거래소이고, Upbit가 약 70% 시장점유율과 높은 수익성을 가진 플랫폼으로 설명됐다고 보도했다. 네이버 주가는 인수 소식 후 7% 넘게 올랐지만, Upbit에서 540억 원 규모 비정상 출금 뉴스가 나오면서 4.2% 하락 전환했다. ([Reuters][6])

### stage date

```text
Stage 1:
2025년
- digital asset / stablecoin / fintech expansion 기대

Stage 2:
2025-11-27
- Naver Financial / Dunamu all-stock merger
- deal value 15.13조 원
- Upbit market leadership

Stage 3:
보류
- regulatory approval
- merger closing
- fintech monetization
- exchange volume durability
- security/trust risk 통과 필요

Stage 4B:
2025-11-27
- acquisition news 직후 +7% 이상
- digital-asset event premium

Stage 4C-watch:
2025-11-27
- Upbit abnormal withdrawal 540억 원
- Naver 주가 -4.2% 하락 전환
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported event returns and deal anchor

stage3_price:
N/A

deal_value:
15.13 trillion won

event_MFE_intraday_or_initial:
> +7%

event_MAE_same_day_after_abnormal_withdrawal:
-4.2%

abnormal_withdrawal:
54.0 billion won

event_swing_from_initial_plus_7_to_minus_4_2:
-11.2 percentage points

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

peak_price:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium + success_candidate + trust_watch
rerating_result = digital_asset_platform_watch
stage_failure_type = stage2_watch_success_with_4C_watch
```

### 교정

네이버/두나무는 R6에서 `digital_asset_equity_option`은 Stage 2로 인정하지만, **거래소 보안·규제·거래량·수익모델**을 통과해야 Stage 3가 된다.

---

## Case E — 카카오뱅크 / 카카오 governance `failed_rerating / legal-governance 4C-watch`

```text
symbol = 323410 / 035720
case_type = failed_rerating / 4C-watch
archetype = INTERNET_BANK_PROFITABILITY / PLATFORM_GOVERNANCE_LEGAL_RISK
```

### evidence

2024년 7월 Kakao 창업자 김범수에 대한 구속영장 심사와 이후 구속은 KakaoBank ownership risk로 연결됐다. Reuters는 금융범죄로 유죄가 확정되면 은행 지분 10% 초과 보유가 제한될 수 있어 Kakao 그룹의 KakaoBank 지배력에 영향을 줄 수 있다고 설명했다. 구속 보도 후 Kakao 주가는 장중 3.4% 하락했고, 2024년 연초 대비 24% 하락한 상태였다. ([Reuters][7])

2025년 10월에는 법원이 김범수에게 무죄를 선고했다. 이는 legal overhang relief이지만, KakaoBank의 Stage 3-Green을 의미하지는 않는다. 인터넷은행 Stage 3는 순이자마진, 비이자수익, 건전성, ROE, 대주주 적격성 리스크 해소가 함께 필요하다. ([Reuters][8])

### stage date

```text
Stage 1:
2021 IPO 이후
- internet bank growth
- mobile banking scale

Stage 2:
보류
- NIM, fee income, ROE, credit quality 확인 필요

Stage 3:
없음
- legal-governance overhang 해소 전 Green 금지

Stage 4B:
IPO 직후 고평가 구간 후보

Stage 4C:
2024-07-23
- Kakao founder arrest
- KakaoBank ownership cap risk
- Kakao shares -3.4%, YTD -24%

4C relief:
2025-10-21
- Kim Beom-su acquitted
- hard 4C 일부 완화
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported event returns and legal anchors

stage3_price:
N/A

Kakao_event_MAE_1D:
-3.4%

Kakao_YTD_drawdown_by_2024-07-23:
-24%

KakaoBank_direct_price:
price_data_unavailable_after_deep_search
- Reuters는 KakaoBank 직접 주가 reaction anchor를 제공하지 않음.
- KakaoBank risk는 Kakao ownership/legal overhang 경유.

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

peak_price:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = failed_rerating / legal_governance_watch
rerating_result = internet_bank_governance_overhang
stage_failure_type = should_have_been_red_or_watch
```

### 교정

KakaoBank는 R6에서 `internet_bank_profitability`보다 `major_shareholder_legal_risk`가 먼저다.

```text
Green 조건:
ROE
NIM
fee income
credit quality
major shareholder suitability

4C gate:
financial crime ownership cap
founder legal risk
governance trust break
```

---

## Case F — 카카오페이 / 원화 스테이블코인 테마 `overheat / price_moved_without_evidence`

```text
symbol = 377300 / 158430 등
case_type = overheat / price_moved_without_evidence
archetype = KRW_STABLECOIN_POLICY_THEME / DIGITAL_ASSET_THEME_OVERHEAT
```

### evidence

2025년 6월 FT는 한국 증시가 원화 스테이블코인 기대에 힘입어 강하게 올랐고, Kakao Pay 주가는 그달 두 배 이상, LG CNS는 약 70%, Aton은 80%, ME2ON은 세 배 올랐다고 보도했다. 하지만 정부의 구체적 crypto 규제 프레임워크는 아직 나오지 않았고, 원화 스테이블코인 발행을 둘러싼 논쟁이 계속되고 있었다. ([Financial Times][9])

2025년 7월 FT는 한국은행이 비은행 스테이블코인 발행이 대규모 자본유출과 외환리스크를 만들 수 있다고 우려했고, 은행권 중심의 엄격한 발행을 선호한다고 보도했다. ([Financial Times][10])

### stage date

```text
Stage 1:
2025-06
- won stablecoin policy pledge
- crypto / digital asset reform 기대

Stage 2:
없음 또는 약한 Stage 2
- 법안·규제안은 있었지만 회사별 수익모델 미확인

Stage 3:
없음
- 발행권, reserve income, fee revenue, regulatory approval 전 Green 금지

Stage 4B:
2025-06
- Kakao Pay >2배
- LG CNS +70%
- Aton +80%
- ME2ON 3배

Stage 4C:
규제 지연, 비은행 발행 제한, 외환리스크 우려 현실화 시 후보
```

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

MFE_30D:
reported event basket MFE available as above

MAE_30D / 90D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

peak_price:
price_data_unavailable_after_deep_search

drawdown_after_peak:
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

### 교정

스테이블코인은 R6에서 가장 강한 event-premium 감점축이다.

```text
정책 기대:
Stage 1

Stage 3 조건:
licensed issuer
bank partnership
reserve income
fee revenue
regulatory capital
risk control

Green blocker:
non-bank systemic risk
FX outflow risk
regulatory uncertainty
```

---

## Case G — 카카오페이 privacy/data trust `4C-watch`

```text
symbol = 377300
case_type = 4C-watch
archetype = PAYMENT_PRIVACY_REGULATORY_4C / PAYMENT_FINTECH_INFRA
```

### evidence

공개 요약 기준 2025년 4월 금융감독원은 카카오페이가 이용자 동의 없이 Alipay Singapore Holdings에 약 4,000만 명의 사용자 데이터를 제공했다는 이유로 150억 원 과징금을 부과했다. 이 출처는 Reuters가 아니라 Wikipedia/Korea Times 경유 요약이므로 confidence는 낮게 기록한다. ([위키백과][11])

### stage date

```text
Stage 1:
2021 IPO 이후
- 간편결제 / 플랫폼 금융 성장주

Stage 2:
보류
- 결제액, take rate, 금융상품 수익, 영업이익 확인 필요

Stage 3:
없음
- privacy/data trust break 전후 Green 금지

Stage 4B:
IPO 직후 고평가 / stablecoin 테마 과열 구간 후보

Stage 4C:
2025-04
- user-data transfer fine
- payment privacy regulatory break
```

### 실제 가격경로 검증

```text
price_data_source:
Wikipedia/Korea Times summary only, lower confidence

stage3_price:
N/A

fine_amount:
15.0 billion won

affected_user_data:
about 40 million users

stock OHLC:
price_data_unavailable_after_deep_search
- Reuters anchor 없음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = payment_privacy_trust_break
stage_failure_type = should_have_been_red_or_watch
source_confidence = medium_low
```

### 교정

카카오페이는 R6에서 `payment_volume`보다 `privacy_regulatory_trust`가 우선한다.

---

# 5. 이번 R6 case별 요약표

| case                        | 분류                                   |                                            실제 가격검증 | alignment                    |
| --------------------------- | ------------------------------------ | -------------------------------------------------: | ---------------------------- |
| SK스퀘어                       | structural_success 후보                |     2,000억 원 소각/매입·소각, SKH 20% stake, 47% discount | success_candidate            |
| 하나금융                        | success_candidate                    |    Dunamu 6.55% = 1.003조 원, implied value 15.31조 원 | success_candidate            |
| 삼성생명                        | success_candidate + regulatory watch |                 삼성전자 지분 1.3조 매각, book value 대비 50% | success_candidate            |
| 네이버파이낸셜/Dunamu              | event + success_candidate            |          deal 15.13조 원, +7% → -4.2%, swing -11.2pp | event_premium + trust_watch  |
| 카카오뱅크/Kakao                 | failed / legal watch                 |         Kakao -3.4%, YTD -24%, bank ownership risk | legal_governance_watch       |
| Kakao Pay/stablecoin basket | overheat                             | Kakao Pay >2배, LG CNS +70%, Aton +80%, ME2ON +200% | price_moved_without_evidence |
| Kakao Pay privacy           | 4C-watch                             |                           150억 과징금, 4,000만 사용자 데이터 | thesis_break_watch           |

---

# 6. score-price alignment 판정

```text
success_candidate:
- SK스퀘어
- 하나금융
- 삼성생명

event_premium + success_candidate:
- 네이버파이낸셜 / 두나무

price_moved_without_evidence:
- 카카오페이 / Aton / ME2ON 스테이블코인 basket

failed_rerating / legal_governance_watch:
- 카카오뱅크 / 카카오 governance

thesis_break_watch:
- 카카오페이 privacy/data trust

4B-watch:
- 스테이블코인 theme basket
- 네이버/두나무 acquisition initial rally
- SK스퀘어가 SK하이닉스 대시세 뒤 NAV trade로 몰릴 경우
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

### 이유

SK스퀘어는 실제 소각과 추가 매입·소각 계획이 있다. 하나금융은 1조 원을 들여 두나무 6.55%를 취득하면서 regulated digital-asset equity option을 만들었다. 삼성생명은 삼성전자 지분·book value discount·규제성 지분매각이라는 NAV value-up 구조를 갖는다. ([Reuters][1])

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

### 이유

스테이블코인 basket은 실제 발행권·수수료·reserve income 없이 Kakao Pay >2배, ME2ON 3배 같은 급등이 먼저 나왔다. 카카오뱅크는 internet bank growth보다 대주주 법적 리스크와 은행 지분 규제가 먼저 작동했다. 네이버/Dunamu도 acquisition news 뒤 +7%에서 Upbit withdrawal 이슈로 -4.2% 전환했다. ([Financial Times][9])

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
개인정보·데이터 신뢰 훼손
```

## 4B 조기감지 조건

```text
4B-watch:
은행·보험주가 PBR rerating 후 book value에 근접하거나 상회
자사주 소각 뉴스가 반복되어 surprise가 사라짐
SK하이닉스/Samsung NAV 랠리가 지주·보험주에 과도 반영
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

---

# 8. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
```

이번 세션에서 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉을 안정적으로 직접 확보하지 못했다. 대신 Reuters / FT / WSJ / Barron’s의 가격 anchor, 이벤트 수익률, 거래금액, 할인율을 사용해 계산 가능한 부분은 직접 계산했다.

---

# 9. patch-ready 출력

## docs/round/round_138.md 요약

```md
# R6 Loop 8. Financial / Capital Allocation / Digital Finance Price Validation

이번 라운드는 R6 price-validation 라운드다.

핵심 결론:
- SK스퀘어는 1,000억 원 자사주 소각과 추가 1,000억 원 매입·소각 계획으로 Stage 2 value-up 후보가 된다. SK하이닉스 지분 20% 보유와 47% discount는 NAV rerating 후보지만, 반복 소각과 discount 축소 가격경로가 Stage 3 조건이다.
- 하나금융은 두나무 6.55% 지분을 1.003조 원에 인수해 regulated digital-asset equity option을 만들었다. Implied Dunamu value는 약 15.31조 원이다.
- 삼성생명은 삼성전자 지분 1.3조 원 매각과 50% book-value discount로 NAV value-up 후보지만, 규제성 매각과 capital release 확인 전 Stage 3는 보류다.
- 네이버파이낸셜/Dunamu deal은 15.13조 원 규모로 강한 Stage 2지만, Naver 주가는 acquisition news +7% 이후 Upbit 540억 원 abnormal withdrawal 이슈로 -4.2% 하락 전환했다.
- KakaoBank는 internet bank growth보다 Kakao founder legal risk와 bank ownership cap risk가 먼저다.
- Kakao Pay / stablecoin basket은 실제 규제수익 전 Kakao Pay >2배, LG CNS +70%, Aton +80%, ME2ON +200%로 4B/event premium이다.
- Kakao Pay privacy fine은 payment/data trust 4C-watch다.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 138 R6 Loop 8 Financial Capital Digital Price Validation

## 반영 내용
- R6 Loop 8 price-validation 라운드를 추가했다.
- Value-up holding company, bank digital-asset equity option, insurance NAV, stablecoin policy theme, fintech privacy trust, internet-bank governance risk를 비교했다.
- Reuters/FT/WSJ/Barron’s reported anchors로 가능한 MFE/MAE와 valuation ratios를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- buyback cancellation, capital buffer, NAV monetization, regulated digital asset revenue 가중치 강화
- low PBR only, stablecoin policy theme only, privacy/data trust break, legal governance risk 감점 강화
- digital asset / stablecoin 4B-watch 민감도 강화
```

## case row 초안

```jsonl
{"case_id":"r6_loop8_sk_square_valueup_nav_discount","symbol":"402340","company_name":"SK스퀘어","case_type":"success_candidate","primary_archetype":"VALUE_UP_SHAREHOLDER_RETURN","stage2_date":"2024-11-21","stage4b_date":"2026-05-14","price_validation":{"price_data_source":"Reuters/Barron's valuation anchors","stage3_price":null,"buyback_cancelled_krw_bn":100,"additional_buyback_cancel_plan_krw_bn":100,"total_announced_buyback_cancel_krw_bn":200,"sk_hynix_stake_pct":20,"discount_to_sk_hynix_exposure_pct":47,"implied_value_capture_ratio_pct":53,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"NAV_discount_valueup_watch","notes":"Actual cancellation supports Stage 2; Stage 3 requires repeated cancellation and discount narrowing price path."}
{"case_id":"r6_loop8_hana_dunamu_equity_option","symbol":"086790","company_name":"하나금융지주/하나은행","case_type":"success_candidate","primary_archetype":"DIGITAL_ASSET_BANK_EQUITY_OPTION","stage2_date":"2026-05-14","price_validation":{"price_data_source":"Reuters/WSJ transaction anchors","stage3_price":null,"transaction_value_krw_trn":1.003,"stake_acquired_pct":6.55,"implied_dunamu_value_krw_trn":15.31,"upbit_market_share_pct":80,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"regulated_digital_asset_equity_option","notes":"Dunamu stake is Stage 2; Stage 3 requires regulatory approval, earnings contribution and capital-ratio impact."}
{"case_id":"r6_loop8_samsung_life_nav_valueup","symbol":"032830","company_name":"삼성생명","case_type":"success_candidate","primary_archetype":"INSURANCE_NAV_VALUEUP_SAMSUNG_ELECTRONICS_STAKE","stage2_date":"2026-03-19","price_validation":{"price_data_source":"Reuters/Barron's valuation anchors","stage3_price":null,"samsung_electronics_stake_sale_krw_trn":1.3,"samsung_electronics_stake_owned_pct":10,"trading_level_vs_book_pct":50,"implied_book_discount_pct":50,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_regulatory_watch","rerating_result":"NAV_valueup_candidate","notes":"Hidden NAV and book discount support Stage 2; use of proceeds and K-ICS/CSM required for Stage 3."}
{"case_id":"r6_loop8_naver_dunamu_digital_asset_event","symbol":"035420","company_name":"네이버/네이버파이낸셜","case_type":"success_candidate","primary_archetype":"DIGITAL_ASSET_TOKENIZATION","stage2_date":"2025-11-27","stage4b_date":"2025-11-27","stage4c_date":"2025-11-27","price_validation":{"price_data_source":"Reuters reported event returns","stage3_price":null,"deal_value_krw_trn":15.13,"event_mfe_initial_pct":7.0,"event_mae_same_day_pct":-4.2,"abnormal_withdrawal_krw_bn":54,"event_swing_pp":-11.2,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_success_candidate_trust_watch","rerating_result":"digital_asset_platform_watch","notes":"Strong digital asset Stage 2, but abnormal withdrawal creates trust 4C-watch."}
{"case_id":"r6_loop8_kakaobank_kakao_governance_watch","symbol":"323410/035720","company_name":"카카오뱅크/카카오","case_type":"failed_rerating","primary_archetype":"PLATFORM_GOVERNANCE_LEGAL_RISK","stage4c_date":"2024-07-23","price_validation":{"price_data_source":"Reuters reported event returns","stage3_price":null,"kakao_event_mae_1d":-3.4,"kakao_ytd_drawdown_pct":-24,"kakaobank_direct_price_status":"price_data_unavailable_after_deep_search","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"legal_governance_watch","rerating_result":"internet_bank_governance_overhang","notes":"Founder legal risk and bank ownership cap block Green until governance overhang clears and profitability metrics confirm."}
{"case_id":"r6_loop8_stablecoin_theme_overheat","symbol":"377300/368970/158430/201490","company_name":"Kakao Pay/LG CNS/Aton/ME2ON","case_type":"overheat","primary_archetype":"KRW_STABLECOIN_POLICY_THEME","stage1_date":"2025-06-29","stage4b_date":"2025-06-29","price_validation":{"price_data_source":"FT reported return anchors","stage3_price":null,"kakao_pay_mfe_month_pct":100,"lg_cns_mfe_month_pct":70,"aton_mfe_month_pct":80,"me2on_mfe_month_pct":200,"price_validation_status":"reported_return_anchor_not_full_ohlc"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"stablecoin_policy_theme_overheat","notes":"Stablecoin policy theme rallied before regulated revenue or licensing clarity."}
{"case_id":"r6_loop8_kakao_pay_privacy_4c_watch","symbol":"377300","company_name":"카카오페이","case_type":"4c_watch","primary_archetype":"PAYMENT_PRIVACY_REGULATORY_4C","stage4c_date":"2025-04","price_validation":{"price_data_source":"Wikipedia/Korea Times summary","stage3_price":null,"fine_amount_krw_bn":15,"affected_user_count_mn":40,"price_validation_status":"price_data_unavailable_after_deep_search","source_confidence":"medium_low"},"score_price_alignment":"thesis_break_watch","rerating_result":"payment_privacy_trust_break","notes":"Payment fintech Green should be blocked by privacy/data transfer trust break."}
```

## shadow weight row 초안

```csv
archetype,roe,capital_buffer,buyback_cancel,shareholder_return,pbr_roe_gap,regulated_revenue,nav_monetization,event_penalty,privacy_governance_redteam,4b_watch_sensitivity,notes
VALUE_UP_SHAREHOLDER_RETURN,+3,+3,+5,+5,+4,+0,+4,-2,+1,+4,SK Square shows real cancellation matters more than low-PBR theme.
DIGITAL_ASSET_BANK_EQUITY_OPTION,+2,+4,+0,+1,+2,+4,+2,-2,+2,+5,Hana/Dunamu is Stage 2 until regulated revenue and capital impact confirm.
INSURANCE_NAV_VALUEUP_SAMSUNG_ELECTRONICS_STAKE,+3,+5,+1,+4,+5,+0,+5,-2,+2,+4,Samsung Life needs capital release/use of proceeds beyond hidden NAV.
DIGITAL_ASSET_TOKENIZATION,+2,+3,+0,+1,+2,+4,+1,-4,+4,+5,Naver/Dunamu shows digital asset option plus exchange trust risk.
PLATFORM_GOVERNANCE_LEGAL_RISK,+0,+0,+0,+0,+0,+0,+0,-3,+5,+3,KakaoBank/Kakao legal overhang blocks Green.
KRW_STABLECOIN_POLICY_THEME,+0,+1,+0,+0,+1,+1,+0,-5,+4,+5,Stablecoin theme rally is price_moved_without_evidence until licensing/revenue clarity.
PAYMENT_PRIVACY_REGULATORY_4C,+0,+0,+0,+0,+0,+0,+0,-3,+5,+3,Kakao Pay privacy fine is payment trust 4C-watch.
```

---

# 이번 R6 Loop 8 결론

R6는 Stage 3 후보가 있지만, **저PBR과 정책 기대를 너무 쉽게 Green으로 올리면 바로 망가진다.**

```text
1. SK스퀘어는 자사주 소각과 NAV discount가 있는 좋은 Stage 2 후보지만,
   Stage 3는 반복 소각과 discount narrowing 가격경로로 확인해야 한다.

2. 하나금융의 두나무 지분 인수는 강한 Stage 2다.
   하지만 규제수익, 지분법 이익, 자본비율 영향 확인 전 Stage 3는 아니다.

3. 삼성생명은 hidden NAV와 book-value discount가 매력적이지만,
   규제성 지분매각과 capital release를 같이 봐야 한다.

4. 네이버/Dunamu는 디지털자산 Stage 2 후보이면서 동시에 trust 4C-watch다.
   acquisition news 후 +7%에서 abnormal withdrawal 이슈로 -4.2% 전환했다.

5. 카카오뱅크는 인터넷은행 성장성보다 대주주 legal/governance risk가 먼저다.

6. 스테이블코인 테마는 R6의 대표적인 price_moved_without_evidence다.
   Kakao Pay >2배, ME2ON 3배 같은 움직임은 실제 규제수익 전에는 4B/Event Premium이다.

7. 카카오페이 privacy fine은 payment fintech에서 hard RedTeam 후보로 둬야 한다.
```

한 문장으로 압축하면:

> **R6에서 진짜 Stage 3는 “저PBR·밸류업·스테이블코인 수혜”가 아니라, ROE·자본비율·실제 소각·주주환원·규제수익이 확인되어 PBR 프레임을 바꾸는 순간이다.**
> **R6는 디지털자산/스테이블코인 테마가 가격을 너무 빨리 앞질러 가므로, event premium과 privacy/governance 4C gate를 강하게 둬야 한다.**

[1]: https://www.reuters.com/technology/artificial-intelligence/south-koreas-ai-chip-investor-announces-plan-share-buybacks-2024-11-21/?utm_source=chatgpt.com "South Korea's AI chip investor announces plan for share buybacks"
[2]: https://www.barrons.com/articles/hedge-funds-south-korea-stocks-samsung-sk-hynix-bb2aa94f?utm_source=chatgpt.com "Why Hedge Funds Still See Value in Red-Hot South Korean Stocks"
[3]: https://www.reuters.com/world/asia-pacific/hana-bank-acquire-stake-dunamu-700-mln-filing-says-2026-05-14/?utm_source=chatgpt.com "Hana Bank to acquire stake in Dunamu for $700 mln, filing says"
[4]: https://www.wsj.com/business/hana-bank-to-buy-670-million-stake-in-crypto-exchange-operator-dunamu-08f99cb5?utm_source=chatgpt.com "Hana Bank to Buy $670 Million Stake in Crypto Exchange Operator Dunamu"
[5]: https://www.reuters.com/world/asia-pacific/samsung-life-divest-13-trln-won-worth-samsung-electronics-shares-2026-03-19/?utm_source=chatgpt.com "Samsung Life to divest 1.3 trln won worth of Samsung Electronics' shares"
[6]: https://www.reuters.com/world/asia-pacific/navers-payment-arm-acquire-south-korean-crypto-exchange-operator-10-bln-deal-2025-11-27/?utm_source=chatgpt.com "Naver's payment arm to acquire South Korean crypto exchange operator in $10 bln deal"
[7]: https://www.reuters.com/business/south-korea-court-decide-arrest-warrant-kakao-founder-2024-07-22/?utm_source=chatgpt.com "South Korea court to decide on arrest warrant for Kakao founder"
[8]: https://www.reuters.com/world/asia-pacific/south-korean-court-clears-kakao-founder-stock-manipulation-charges-yonhap-2025-10-21/?utm_source=chatgpt.com "South Korean court clears Kakao founder of stock manipulation charges, Yonhap reports"
[9]: https://www.ft.com/content/4b19bf90-4202-4fe7-8caf-d7db6deeb768?utm_source=chatgpt.com "Crypto-crazy investors make South Korea the best-performing market in Asia"
[10]: https://www.ft.com/content/106a1e79-0a64-4c51-b74f-ad4d4f8896f6?utm_source=chatgpt.com "Stablecoins craze pits central bank against lawmakers in South Korea"
[11]: https://en.wikipedia.org/wiki/Kakao_Pay?utm_source=chatgpt.com "Kakao Pay"

좋아. 순서상 이번은 **R6 Loop 7 — 금융·자본배분·디지털금융 가격경로 검증 라운드**로 진행한다.

이번 R6는 “은행 저PBR이 싸다”가 아니라, **ROE·CET1·실제 자사주 소각·배당성향·비은행 확장·디지털자산 규제수익**이 PBR 프레임을 바꾸는지 보는 라운드야. 특히 R6는 정책·밸류업·스테이블코인 테마가 가격을 먼저 밀기 쉬워서, Stage 3와 event premium을 강하게 분리해야 한다.

---

# 1. 이번 라운드 대섹터

```text
R6 = 금융·자본배분·디지털금융
large_sector = FINANCIAL_CAPITAL_DIGITAL
round = R6 Loop 7 / price-path validation
목표 = Stage 3 / 4B / 4C가 실제 가격경로와 맞았는지 검증하고 shadow weight 보정
```

R6의 기본 영역은 은행, 보험, 증권, 밸류업, 지주사 구조조정, 결제, 핀테크, 디지털자산/토큰화다. Round 40 기준 R6 validation focus는 `roe`, `capital_ratio`, `csm`, `loss_ratio`, `buyback_cancel`, `pbr_roe_gap`, `regulated_revenue`로 잡혀 있다. 

Round 119 기준으로 R6에서 부족한 증거는 `low_pbr`, `policy_valueup`이고, 필요한 증거는 `roe`, `cet1`, `buyback_cancellation`, `shareholder_return`, `credit_cost`다. Green blocker는 `pf_credit_cost`, `capital_ratio_weak`, `event_premium_only`다. 

---

# 2. 대상 canonical archetype

```text
FINANCIAL_SPREAD_BALANCE_SHEET
BANK_HOLDING_VALUEUP_CAPITAL_RETURN
BANK_ROE_PBR_RERATING_KOREA
INSURANCE_CAPITAL_RELEASE_VALUEUP
INSURANCE_KICS_CSM_GATE
INSURANCE_NAV_VALUEUP_SAMSUNG_ELECTRONICS_STAKE
VALUE_UP_SHAREHOLDER_RETURN
HOLDING_RESTRUCTURING_GOVERNANCE
TREASURY_SHARE_CANCEL_EXECUTION
PAYMENT_FINTECH_INFRA
PAYMENT_PRIVACY_REGULATORY_4C
DIGITAL_ASSET_TOKENIZATION
DIGITAL_ASSET_BANK_EQUITY_OPTION
KRW_STABLECOIN_POLICY_THEME
DIGITAL_ASSET_THEME_OVERHEAT
STABLECOIN_CONVERTIBILITY_OVERLAY
```

이번 R6의 핵심 질문은 이거다.

```text
이 회사는 저PBR·밸류업·스테이블코인 테마주인가?
아니면 ROE, 자본비율, 실제 소각, 규제수익, 자본배분이 바뀌며
시장 PBR 프레임이 구조적으로 바뀌는 회사인가?
```

---

# 3. deep sub-archetype

```text
은행 / 금융지주:
- ROE
- CET1
- credit cost
- PF exposure
- dividend payout
- buyback cancellation
- treasury share cancellation
- non-bank expansion
- insurance / securities acquisition
- PBR above book test

보험:
- K-ICS
- CSM
- loss ratio
- capital release
- Samsung Electronics stake NAV
- regulation-driven stake sale
- dividend capacity
- book value discount

지주 / 밸류업:
- SK Square NAV discount
- holding company discount
- treasury share cancellation
- activist pressure
- duplicate listing reform
- subsidiary stake monetization

핀테크 / 결제:
- Kakao Pay
- KakaoBank
- payment take rate
- privacy / data transfer risk
- founder governance risk
- regulatory ownership cap

디지털자산:
- Hana Bank / Dunamu stake
- Upbit exchange economics
- won stablecoin policy
- digital asset basic act
- bank-issued stablecoin
- non-bank stablecoin systemic risk
- event premium / crypto-theme overheat
```

---

# 4. 국장 신규 후보 case

## Case A — SK스퀘어 `structural_success 후보 + 4B-watch`

```text
symbol = 402340
archetype = VALUE_UP_SHAREHOLDER_RETURN / HOLDING_RESTRUCTURING_GOVERNANCE
case_type = structural_success 후보 + 4B-watch
```

SK스퀘어는 금융업은 아니지만 R6의 “자본배분·지주사 밸류업” archetype에 들어가는 좋은 가격검증 후보야. 2024년 11월 SK스퀘어는 1,000억 원 규모 자사주 소각과 추가 1,000억 원 자사주 매입·소각 계획을 발표했다. Reuters는 이 조치가 Palliser Capital의 저평가 해소 요구와 정부 밸류업 프로그램 흐름 속에서 나왔다고 설명했고, SK스퀘어의 시장가치가 보유한 SK하이닉스 지분 가치의 절반보다 낮다고 보도했다. ([Reuters][1])

2026년에는 한국 증시가 크게 오른 가운데, Barron’s는 SK스퀘어가 SK하이닉스에 대한 간접 노출을 제공하면서도 SK하이닉스 대비 47% 할인되어 거래된다는 헤지펀드 의견을 전했다. 이건 R6의 `old_frame_mispricing`과 `valuation_rerating_runway`를 시험하기 좋은 사례다. ([Barron's][2])

### stage date 후보

```text
Stage 1:
2024년
- 밸류업 정책
- SK하이닉스 지분가치 대비 지주사 저평가
- activist engagement

Stage 2:
2024-11-21
- 1,000억 원 자사주 소각
- 추가 1,000억 원 매입·소각 계획
- 독립이사 후보 지명

Stage 3:
조건부 후보
- NAV discount 축소
- 반복적인 자사주 소각
- SK하이닉스 지분가치 상승이 SK스퀘어 주주환원으로 연결되는지 확인 필요

Stage 4B:
2026년 한국 증시/AI 반도체 랠리 이후 후보
- SK하이닉스 폭등과 지주사 discount 축소가 동시에 가격에 반영되면 4B-watch

Stage 4C:
없음
- 단, 자사주 소각 중단, discount 재확대, SK하이닉스 급락, governance 후퇴 시 후보
```

### 가격경로 검증

```text
stage3_price:
2024-11-21 OHLC backfill 필요.

MFE_30D / 90D / 180D / 1Y / 2Y:
needs_ohlc_backfill

MAE_30D / 90D / 180D / 1Y:
needs_ohlc_backfill

below_stage3_price_flag:
needs_ohlc_backfill

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = aligned 후보
rerating_result = true_rerating 후보
stage_failure_type = green_success 후보
```

### 교정 포인트

SK스퀘어는 R6에서 `buyback_cancel`과 `NAV_discount`를 올려주는 케이스다. 다만 SK하이닉스 가격이 너무 앞서가면 SK스퀘어도 4B-watch를 붙여야 한다.

---

## Case B — 하나금융지주 / 하나은행 `success_candidate + digital_asset_option`

```text
symbol = 086790
archetype = DIGITAL_ASSET_BANK_EQUITY_OPTION / REGULATED_STABLECOIN_INFRA
case_type = success_candidate
```

하나금융은 R6 디지털자산 축에서 가장 선명한 신규 case다. 2026년 5월 하나은행은 국내 최대 가상자산거래소 업비트 운영사 두나무 지분 6.55%를 1조 원에 인수한다고 공시했다. Reuters는 두나무가 국내 가상자산 거래량의 80% 이상을 처리하고, 매우 높은 수익성을 가진 플랫폼이라고 설명했다. ([Reuters][3])

다만 이건 바로 Stage 3-Green이 아니다. 한국은행 총재는 2025년 6월 원화 스테이블코인 발행 자체에 반대하지는 않지만, 달러 스테이블코인 수요 증가와 외환·자본흐름 관리 리스크를 우려한다고 밝혔다. 즉 디지털자산은 구조 후보지만, 규제수익·자본소모·회계·리스크가 확인되기 전에는 Stage 2에 머무는 게 맞다. ([Reuters][4])

### stage date 후보

```text
Stage 1:
2025-06
- 원화 스테이블코인 정책 기대
- 디지털자산 제도화 기대

Stage 2:
2026-05-14
- 하나은행, 두나무 6.55% 지분 1조 원 인수
- Upbit 거래량 80% 이상 플랫폼 경제성

Stage 3:
보류
- 지분법 이익, 규제승인, 자본비율 영향, 디지털자산 수익화 확인 필요

Stage 4B:
정책/스테이블코인 테마로 은행·핀테크주가 선반영되면 후보

Stage 4C:
규제 지연, 자본규제 강화, 가상자산 거래량 급감, 스테이블코인 외환 리스크 현실화 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage2_price:
2026-05-14 OHLC backfill 필요.

MFE / MAE:
Stage 2 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = success_candidate
rerating_result = unknown
stage_failure_type = stage2_watch_success 후보
```

### 교정 포인트

하나금융은 `regulated_digital_asset_equity_option`을 R6에 추가로 강화할 수 있지만, `stablecoin_policy_theme`만으로 Stage 3를 주면 안 된다.

---

## Case C — 삼성생명 `success_candidate + regulatory_4C_watch`

```text
symbol = 032830
archetype = INSURANCE_NAV_VALUEUP_SAMSUNG_ELECTRONICS_STAKE / INSURANCE_CAPITAL_RELEASE_VALUEUP
case_type = success_candidate + 4C-watch
```

삼성생명은 R6에서 보험 NAV value-up을 검증하는 case다. Barron’s는 2026년 한국 주식 세미나에서 삼성생명이 삼성전자 지분 10%를 보유하고도 약 50%의 book value 수준에서 거래된다는 헤지펀드 의견을 전했다. 이건 “보험 본업 + 삼성전자 NAV discount + governance/regulation”이 같이 걸린 구조다. ([Barron's][2])

하지만 동시에 2026년 3월 삼성생명은 금융회사 지배구조 관련 국내 규제 리스크를 해소하기 위해 삼성전자 지분 1.3조 원어치를 매각하겠다고 공시했다. 이건 NAV 할인 해소 측면에서는 이벤트지만, 보유지분 매각이 강제 규제 대응이라면 Stage 3-Green을 바로 주면 안 된다. ([Reuters][5])

### stage date 후보

```text
Stage 1:
2025~2026
- 삼성전자 AI 랠리
- 삼성생명 보유 삼성전자 지분가치 부각
- 보험 NAV value-up 기대

Stage 2:
2026-03-19
- 삼성전자 지분 1.3조 원 매각 발표
- 금융회사 지배구조 규제 리스크 대응

Stage 3:
보류
- 매각대금 활용, 배당/소각, K-ICS, CSM, 보험 본업 이익 확인 필요

Stage 4B:
삼성전자 랠리와 함께 NAV discount 축소가 이미 가격에 크게 반영되면 후보

Stage 4C:
규제성 지분매각이 반복되거나, 보유지분가치 하락·보험자본비율 악화가 확인되면 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage2_price:
2026-03-19 OHLC backfill 필요.

MFE / MAE:
Stage 2 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = success_candidate + regulatory_watch
rerating_result = NAV_rerating_candidate
stage_failure_type = stage2_watch_success 후보
```

### 교정 포인트

삼성생명은 `hidden_NAV`, `book_value_discount`, `capital_release` 점수는 올릴 수 있지만, `forced_sale_or_regulatory_overhang` 감점도 같이 붙여야 한다.

---

## Case D — 카카오뱅크 `failed_rerating / governance_ownership_risk`

```text
symbol = 323410
archetype = INTERNET_BANK_PROFITABILITY / PLATFORM_GOVERNANCE_LEGAL_RISK
case_type = failed_rerating / 4C-watch
```

카카오뱅크는 디지털은행 성장성과 governance risk가 충돌하는 케이스다. 2024년 7월 Reuters는 카카오 창업자 김범수의 SM엔터 주가조작 의혹 관련 구속영장 심사를 보도하면서, 유죄가 확정될 경우 금융범죄자는 은행 지분 10% 초과 보유가 제한될 수 있어 카카오그룹의 카카오뱅크 지배력에도 영향을 줄 수 있다고 설명했다. 보도 당시 카카오 주가는 3.4% 하락했다. ([Reuters][6])

카카오뱅크 자체는 인터넷은행으로 수익성 개선 여지가 있지만, R6 Stage 3-Green을 주려면 플랫폼 사용자 수가 아니라 순이자마진, 비이자수익, 건전성, 대주주 적격성 리스크 해소가 필요하다.

### stage date 후보

```text
Stage 1:
2021 IPO 이후
- 인터넷은행 성장주 / 핀테크 프리미엄

Stage 2:
보류
- 수익성·비이자수익 개선 확인 필요

Stage 3:
없음
- governance/legal ownership overhang 해소 전 Green 금지

Stage 4B:
IPO 직후 고평가 구간은 4B/overheat 후보

Stage 4C:
2024-07-22
- 카카오 창업자 법적 리스크
- 카카오뱅크 지배력 규제 리스크
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage1_price:
IPO 이후 OHLC backfill 필요.

MFE / MAE:
IPO / governance event 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
IPO 이후 peak backfill 필요.

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = failed_rerating / legal_governance_4C_watch
rerating_result = no_rerating
stage_failure_type = should_have_been_red_or_watch
```

### 교정 포인트

카카오뱅크는 R6에서 `internet_bank_profitability`와 `major_shareholder_legal_risk`를 분리해야 한다.

```text
사용자 수 / 모바일뱅크 테마:
Stage 1

수익성 + 비이자수익 + 건전성:
Stage 2~3 후보

대주주 적격성 리스크:
Green block / 4C-watch
```

---

## Case E — 카카오페이 / 아톤 / 스테이블코인 테마 `overheat / price_moved_without_evidence`

```text
symbols = 377300 / 158430 등
archetype = KRW_STABLECOIN_POLICY_THEME / DIGITAL_ASSET_THEME_OVERHEAT
case_type = overheat / price_moved_without_evidence
```

스테이블코인 테마는 R6에서 반드시 과열/false Green 방지용으로 남겨야 한다. FT는 2025년 상반기 한국 증시가 아시아 최고 성과를 냈고, 그 배경 중 하나로 정부의 원화 스테이블코인 지원 기대를 들었다. 보도에서는 카카오페이, LG CNS, 아톤, 미투온 같은 관련주가 강하게 올랐고, 투자자들이 디지털자산 개혁에 베팅했다고 설명했다. ([Financial Times][7])

하지만 한국은행은 원화 스테이블코인에 대해 외환·자본흐름 관리 리스크를 우려했고, 비은행 발행이 금융시스템에 부담을 줄 수 있다는 논쟁도 이어졌다. 따라서 R6에서는 `stablecoin_policy_theme`을 Stage 1 attention으로만 인정하고, 실제 라이선스·수수료·예치금 수익·규제자본 기준이 나오기 전에는 Green을 주면 안 된다. ([Reuters][4])

### stage date 후보

```text
Stage 1:
2025-06
- 원화 스테이블코인 정책 기대
- 관련주 급등

Stage 2:
보류
- 실제 라이선스, 발행권, 은행 컨소시엄, 수수료 구조 확인 필요

Stage 3:
없음
- 정책 기대만으로 Green 금지

Stage 4B:
2025년 상반기 관련주 급등 구간
- crypto/stablecoin theme overheat

Stage 4C:
규제 지연, 비은행 발행 제한, 외환리스크 규제로 테마 훼손 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage1_price:
2025-06 정책/법안 기대일 기준 OHLC backfill 필요.

MFE_5D / 20D / 60D:
event premium 검증용으로 필요.

MAE_30D / 90D:
event fade 검증 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = price_moved_without_evidence
rerating_result = event_premium / theme_overheat
stage_failure_type = should_have_been_stage1_or_4B_watch
```

### 교정 포인트

R6에서 스테이블코인은 “정책 테마”와 “규제수익 모델”을 분리해야 한다.

```text
정책 기대:
Stage 1

실제 발행권 / 은행 파트너 / 수수료 / reserve income:
Stage 2~3 후보

비은행 무분별 발행 / 외환 리스크:
RedTeam
```

---

## Case F — 카카오페이 `4C-thesis-break / payment_privacy_regulatory`

```text
symbol = 377300
archetype = PAYMENT_PRIVACY_REGULATORY_4C / PAYMENT_FINTECH_INFRA
case_type = 4C-thesis-break
```

카카오페이는 결제·핀테크 infrastructure로는 R6에 들어오지만, privacy/data trust가 깨지면 Stage 3-Green을 막아야 하는 케이스다. 공개 요약 기준 2025년 4월 금융감독원은 카카오페이가 이용자 동의 없이 알리페이 싱가포르에 약 4,000만 명의 사용자 데이터를 제공했다는 이유로 150억 원 과징금을 부과했다. 이 출처는 Reuters가 아니라 위키 경유 요약이라 confidence는 낮지만, R6 RedTeam case로는 기록할 가치가 있다. ([위키백과][8])

### stage date 후보

```text
Stage 1:
2021 IPO 이후
- 간편결제 / 플랫폼 금융 성장주

Stage 2:
보류
- 결제액, take rate, 금융상품 수익, 규제수익 확인 필요

Stage 3:
없음
- privacy trust break 전후로 Green 금지

Stage 4B:
IPO 직후 고평가 구간 후보

Stage 4C:
2025-04
- 사용자 데이터 제공 관련 과징금
- payment privacy regulatory break
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage4c_price:
2025-04 제재일 OHLC backfill 필요.

MFE / MAE:
IPO 이후 및 제재 전후 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
IPO 이후 peak backfill 필요.

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = thesis_break
rerating_result = no_rerating
stage_failure_type = should_have_been_red_or_watch
```

### 교정 포인트

카카오페이는 R6에서 `payment_volume`보다 `privacy_regulatory_trust`가 먼저다.

```text
결제액 증가:
Stage 1~2

take rate + 영업이익 + 규제 신뢰:
Stage 3 후보

개인정보 / 데이터 이전 / 과징금:
4C hard gate 후보
```

---

## Case G — 우리금융지주 `success_candidate / capital_buffer_watch`

```text
symbol = 316140
archetype = FINANCIAL_SPREAD_BALANCE_SHEET / BANK_HOLDING_VALUEUP_CAPITAL_RETURN
case_type = success_candidate / insufficient_evidence
```

우리금융은 R6에서 “저PBR 은행 + 비은행 확장”을 검증하는 케이스로 쓸 수 있다. 공개 요약 기준 2025년 우리금융 순이익은 3.14조 원으로 증가했지만, Tongyang·ABL Life 인수 이후 capital buffer를 보강하기 위해 Digital Tower 매각을 추진했다는 내용이 남아 있다. 이 출처는 위키 경유 요약이므로 confidence는 낮게 둔다. ([위키백과][9])

이 케이스는 Stage 3-Green보다 `capital_buffer_watch`가 핵심이다. 비은행 확장은 장기적으로 좋지만, 인수로 CET1이 압박받으면 주주환원 여력이 줄 수 있다.

### stage date 후보

```text
Stage 1:
2024~2025
- 밸류업 은행주
- 저PBR 금융지주 re-rating 기대

Stage 2:
2025년 실적 / 비은행 확장 구간
- 순이익 증가
- 보험사 인수로 비은행 포트폴리오 확대

Stage 3:
보류
- CET1, credit cost, 배당/소각, 인수 후 자본부담 확인 필요

Stage 4B:
은행주 동반 rerating 후 PBR re-rating이 선반영되면 후보

Stage 4C:
capital ratio 약화, PF credit cost, 인수 integration 비용, 주주환원 축소 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage2_price:
2025 실적 발표일 / 인수 승인일 OHLC backfill 필요.

MFE / MAE:
Stage 2 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = unknown_insufficient_evidence
rerating_result = success_candidate / capital_buffer_watch
stage_failure_type = stage2_watch_success 후보
```

### 교정 포인트

우리금융은 R6에서 `non_bank_expansion`을 무조건 가점하면 안 된다는 케이스다.

```text
비은행 확장:
좋은 Stage 2 후보

Stage 3 조건:
CET1 유지
credit cost 안정
인수 후 ROE 개선
주주환원 유지
```

---

# 5. 이번 R6 case별 요약표

| case            | 분류                                   | Stage 3 판정 |               4B/4C 판정 | 가격경로 1차 판단                                    |
| --------------- | ------------------------------------ | ---------: | ---------------------: | --------------------------------------------- |
| SK스퀘어           | structural_success 후보 + 4B-watch     |     조건부 가능 |  SK하이닉스 랠리 이후 4B-watch | 소각·NAV discount가 실제 rerating으로 연결되는지 backfill |
| 하나금융            | success_candidate                    |         보류 | 디지털자산 정책 과열 시 4B-watch | 두나무 지분은 Stage 2, 규제수익 전 Green 금지              |
| 삼성생명            | success_candidate + regulatory watch |         보류 |   지분 강제매각/규제는 4C-watch | NAV value-up은 좋지만 capital release 확인 필요       |
| 카카오뱅크           | failed_rerating / governance risk    |         없음 |   대주주 법적 리스크는 4C-watch | 인터넷은행 성장주에 governance cap 필요                  |
| 카카오페이/스테이블코인 테마 | overheat                             |         없음 |     정책 테마 급등은 4B-watch | 실제 발행권/수익 전 Green 금지                          |
| 카카오페이 privacy   | 4C-thesis-break                      |         없음 |     사용자 데이터 과징금은 4C 후보 | payment trust break                           |
| 우리금융            | success_candidate / insufficient     |         보류 |     자본비율 약화 시 4C-watch | 비은행 확장과 CET1을 같이 봐야 함                         |

---

# 6. 각 case별 stage date 후보 요약

```text
SK스퀘어:
Stage 1 = 2024 밸류업 / activist / SK하이닉스 NAV discount
Stage 2 = 2024-11-21 자사주 소각·추가 매입·소각 계획
Stage 3 = 조건부 후보
Stage 4B = 2026 AI 반도체/한국증시 랠리 이후 discount 축소 시 후보
Stage 4C = 소각 중단 / discount 재확대 / SK하이닉스 급락 시 후보

하나금융:
Stage 1 = 2025-06 원화 스테이블코인 정책 기대
Stage 2 = 2026-05-14 하나은행 두나무 6.55% 지분 1조 원 인수
Stage 3 = 보류
Stage 4B = 디지털자산 테마 선반영 시 후보
Stage 4C = 규제 지연 / 거래량 급감 / 외환 리스크 시 후보

삼성생명:
Stage 1 = 2025~2026 삼성전자 NAV / 보험 value-up
Stage 2 = 2026-03-19 삼성전자 지분 1.3조 원 매각 발표
Stage 3 = 보류
Stage 4B = 삼성전자 NAV discount 축소 과열 시 후보
Stage 4C = 규제성 지분매각 반복 / 자본비율 악화 시 후보

카카오뱅크:
Stage 1 = IPO 이후 인터넷은행 성장주
Stage 2 = 보류
Stage 3 = 없음
Stage 4B = IPO 고평가 구간 후보
Stage 4C = 2024-07-22 카카오 창업자 법적 리스크 / 지배력 규제 리스크

스테이블코인 테마:
Stage 1 = 2025-06 정책 기대
Stage 2 = 보류
Stage 3 = 없음
Stage 4B = 관련주 급등 구간
Stage 4C = 규제 지연 / 비은행 발행 제한 / 외환 리스크 현실화

카카오페이 privacy:
Stage 1 = 간편결제 플랫폼 금융 성장주
Stage 2 = 보류
Stage 3 = 없음
Stage 4B = IPO 고평가 구간 후보
Stage 4C = 2025-04 사용자 데이터 관련 과징금

우리금융:
Stage 1 = 밸류업 은행주
Stage 2 = 2025 실적 / 보험사 인수 구간
Stage 3 = 보류
Stage 4B = 은행주 PBR rerating 과열 시 후보
Stage 4C = CET1 약화 / PF credit cost / 주주환원 축소 시 후보
```

---

# 7. 가격경로 검증

R6는 정확한 OHLC backfill 없이는 수익률을 확정하면 안 된다. 금융주는 단기 이벤트보다 `PBR rerating`, `dividend/buyback`, `CET1`, `credit cost`, `regulatory overhang`이 같이 움직이기 때문에 stage별로 분리해야 한다.

| case          |               stage3_price | MFE/MAE                               | below_stage3   | peak/drawdown                         |
| ------------- | -------------------------: | ------------------------------------- | -------------- | ------------------------------------- |
| SK스퀘어         | 2024-11-21 후보, backfill 필요 | needs_ohlc_backfill                   | needs backfill | 2026 AI/NAV rally 후 peak 필요           |
| 하나금융          |                 Stage 3 없음 | Stage 2 기준 backfill                   | N/A            | Dunamu event 후 drawdown 필요            |
| 삼성생명          |                 Stage 3 없음 | Stage 2 기준 backfill                   | N/A            | Samsung NAV rally / forced sale 구간 필요 |
| 카카오뱅크         |                 Stage 3 없음 | IPO 및 2024-07 legal event 기준 backfill | N/A            | IPO peak/drawdown 필요                  |
| 스테이블코인 테마     |                 Stage 3 없음 | MFE_5D/20D/60D 필요                     | N/A            | event fade drawdown 필요                |
| 카카오페이 privacy |                 Stage 3 없음 | 제재 전후 backfill                        | N/A            | IPO peak/drawdown 필요                  |
| 우리금융          |                 Stage 3 없음 | Stage 2 기준 backfill                   | N/A            | capital buffer watch 구간 필요            |

핵심은 이거다.

```text
R6에서 Stage 3는 저PBR이 아니라
ROE + CET1 + 실제 소각 + 주주환원 지속성 + credit cost 안정이 같이 확인될 때만 준다.
```

---

# 8. score-price alignment 판정

```text
SK스퀘어:
alignment = aligned 후보
소각 + NAV discount + activist pressure는 좋은 구조.
다만 SK하이닉스 랠리 후에는 4B-watch 필요.

하나금융:
alignment = success_candidate
두나무 지분은 강한 Stage 2.
규제수익과 자본효율 확인 전 Stage 3 금지.

삼성생명:
alignment = success_candidate + regulatory_watch
NAV discount는 매력적이지만 규제성 지분매각과 자본활용 확인 필요.

카카오뱅크:
alignment = failed_rerating / legal_governance_watch
디지털은행 성장성보다 대주주 적격성 리스크가 Green을 막음.

스테이블코인 테마:
alignment = price_moved_without_evidence
정책 기대와 관련주 급등은 Stage 1/4B-watch.

카카오페이 privacy:
alignment = thesis_break
payment fintech에서 privacy trust break는 hard RedTeam.

우리금융:
alignment = unknown_insufficient_evidence
비은행 확장은 좋지만 capital buffer와 CET1 확인 필요.
```

---

# 9. 점수비중 교정

## 올릴 축

```text
roe_sustainability +4
cet1_buffer +4
real_buyback_cancellation +5
dividend_payout_visibility +3
credit_cost_control +4
pbr_roe_gap +3
capital_release_quality +3
regulated_revenue_visibility +3
nav_discount_with_monetization +3
non_bank_expansion_with_capital_buffer +2
```

R6에서 가장 강한 건 “싸다”가 아니라 **자본이 실제로 주주에게 돌아오고, 그 과정에서 자본비율이 깨지지 않는 것**이다.

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
pf_credit_cost_unknown -3
mna_expansion_without_cet1_buffer -3
```

R6는 “저PBR”이 가장 위험한 false Green이다. 저PBR은 Stage 1 attention일 뿐이고, ROE·CET1·소각·credit cost가 없으면 Stage 3가 아니다.

## Green gate 강화 조건

R6 Stage 3-Green은 앞으로 이렇게 줘야 한다.

```text
필수 gate:
1. ROE가 구조적으로 개선되거나 유지됨
2. CET1 / K-ICS 등 자본비율 충분
3. 자사주 매입이 실제 소각으로 이어짐
4. 배당·소각이 일회성이 아니라 policy로 고정됨
5. credit cost / PF risk 통과
6. PBR rerating 여지 존재
7. 정책 테마가 아니라 회사 단위 자본배분 증거 존재
8. 디지털자산은 규제수익·지분법·수수료 구조 확인

금지:
저PBR
밸류업 정책 기대
자사주 매입만 있고 미소각
스테이블코인 테마만 있음
비은행 인수 후 자본비율 약화
대주주 법적 리스크
개인정보·데이터 신뢰 훼손
```

## 4B 조기감지 조건

```text
4B-watch:
은행·보험주가 PBR rerating 후 book value에 근접하거나 상회
자사주 소각 뉴스가 반복되어 surprise가 사라짐
SK하이닉스/Samsung NAV 랠리가 지주·보험주에 과도 반영
스테이블코인 관련주가 실제 수익모델 없이 급등
디지털자산 지분투자가 거래량 peak에 맞물림

4B-elevated:
credit cost가 낮아 보이지만 PF 리스크가 남음
CET1 buffer가 줄어드는데 주주환원 기대가 과도
M&A/비은행 확장으로 자본부담이 커짐
규제 변경 기대가 가격에 먼저 반영됨

4B-graduated:
ROE 개선이 더 이상 가속되지 않음
PBR rerating이 이미 끝남
추가 소각에도 주가 반응 둔화
금리/credit cycle이 우호적이지 않음
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
지분투자 손상
```

---

# 10. shadow-only 기록

이번 R6 Loop 7은 production scoring에 바로 반영하면 안 된다.

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
needs_ohlc_backfill = true
```

레포에 넣는다면 파일명은 이렇게 가는 게 자연스럽다.

```text
docs/round/round_125.md
docs/checkpoints/checkpoint_28a_round125_r6_loop7_financial_capital_digital_price_validation.md
src/e2r/sector/round125_r6_loop7_financial_capital_digital.py
data/e2r_case_library/cases_r6_loop7_round125.jsonl
data/sector_taxonomy/score_weight_profiles_round125_r6_loop7_v7.csv
output/e2r_round125_r6_loop7_financial_capital_digital/
```

---

# 이번 R6 Loop 7 결론

R6는 Stage 3 후보가 있다. 다만 **저PBR과 정책 밸류업을 너무 쉽게 Green으로 올리면 바로 망가진다.**

이번 라운드의 핵심 교정은 이거다.

```text
1. 금융주 Stage 3는 저PBR이 아니라 ROE·CET1·실제 소각·credit cost 안정에서 나온다.

2. SK스퀘어처럼 자사주 소각과 NAV discount 축소가 같이 있는 case는 좋은 Stage 3 후보가 될 수 있다.
   단, SK하이닉스 랠리 이후에는 4B-watch를 붙여야 한다.

3. 하나금융의 두나무 지분 인수는 강한 Stage 2다.
   그러나 디지털자산 규제수익과 자본효율 확인 전 Stage 3는 아니다.

4. 삼성생명은 NAV discount가 좋지만, 규제성 지분매각과 capital release를 같이 봐야 한다.

5. 카카오뱅크·카카오페이는 디지털금융 성장성보다 governance, privacy, regulatory trust가 먼저다.

6. 스테이블코인 테마는 R6에서 가장 위험한 price_moved_without_evidence다.
   실제 발행권·수수료·reserve income 전에는 Stage 3 금지다.
```

한 문장으로 압축하면:

> **R6에서 진짜 Stage 3는 “저PBR 금융주가 밸류업 수혜를 받는다”가 아니라, 자본비율을 훼손하지 않고 ROE·소각·배당·규제수익이 실제로 PBR 프레임을 바꾸는 순간이다.**
> **스테이블코인·디지털자산·NAV 할인은 좋은 Stage 1~2 재료지만, 수익모델과 자본배분이 확인되기 전에는 4B/event premium으로 따로 둬야 한다.**

[1]: https://www.reuters.com/technology/artificial-intelligence/south-koreas-ai-chip-investor-announces-plan-share-buybacks-2024-11-21/?utm_source=chatgpt.com "South Korea's AI chip investor announces plan for share buybacks"
[2]: https://www.barrons.com/articles/hedge-funds-south-korea-stocks-samsung-sk-hynix-bb2aa94f?utm_source=chatgpt.com "Why Hedge Funds Still See Value in Red-Hot South Korean Stocks"
[3]: https://www.reuters.com/world/asia-pacific/hana-bank-acquire-stake-dunamu-700-mln-filing-says-2026-05-14/?utm_source=chatgpt.com "Hana Bank to acquire stake in Dunamu for $700 mln, filing says"
[4]: https://www.reuters.com/world/asia-pacific/bok-chief-says-he-is-not-against-won-based-stablecoins-has-forex-concerns-2025-06-18/?utm_source=chatgpt.com "BOK chief says he is not against won-based stablecoins but has forex concerns"
[5]: https://www.reuters.com/world/asia-pacific/samsung-life-divest-13-trln-won-worth-samsung-electronics-shares-2026-03-19/?utm_source=chatgpt.com "Samsung Life to divest 1.3 trln won worth of Samsung Electronics' shares"
[6]: https://www.reuters.com/business/south-korea-court-decide-arrest-warrant-kakao-founder-2024-07-22/?utm_source=chatgpt.com "South Korea court to decide on arrest warrant for Kakao founder"
[7]: https://www.ft.com/content/4b19bf90-4202-4fe7-8caf-d7db6deeb768?utm_source=chatgpt.com "Crypto-crazy investors make South Korea the best-performing market in Asia"
[8]: https://en.wikipedia.org/wiki/Kakao_Pay?utm_source=chatgpt.com "Kakao Pay"
[9]: https://en.wikipedia.org/wiki/Woori_Financial_Group?utm_source=chatgpt.com "Woori Financial Group"

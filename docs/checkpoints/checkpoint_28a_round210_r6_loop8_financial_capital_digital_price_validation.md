# Checkpoint 28A Round 210 R6 Loop 8 Financial Capital Digital Price Validation

## 반영 범위

`docs/round/round_210.md`의 R6 금융·자본배분·디지털금융 가격경로 검증 내용을 case-library 보강팩으로 반영했다.

- 대섹터: `FINANCIAL_CAPITAL_DIGITAL`
- 원천 라운드: `docs/round/round_210.md`
- production scoring 변경: `false`
- candidate generation input: `false`
- shadow weight only: `true`
- price validation: `partial_with_reported_price_anchors`
- full OHLC complete: `false`

## 핵심 해석

R6의 Stage 3 후보는 “저PBR·밸류업·스테이블코인 수혜”가 아니다. 다음 묶음이 같이 확인되어야 한다.

- ROE 개선 또는 유지
- CET1/K-ICS 등 자본 buffer
- 실제 자사주 소각
- 반복 가능한 배당·소각 정책
- credit cost/PF risk 통과
- PBR-ROE gap 축소 여지
- 디지털자산은 규제수익, 지분법, 수수료 구조 확인
- privacy/data/governance hard risk 없음

쉬운 예시:

- `저PBR + 밸류업 정책`은 Stage 1 attention이다.
- `실제 소각 + ROE + 자본 buffer + credit cost 안정`이 붙어야 Stage 3 후보가 된다.
- `스테이블코인 정책 + 주가 2배`는 실제 규제수익 전에는 4B/event premium이다.

## 추가 케이스

| case | company | classification | interpretation |
|---|---|---|---|
| `r6_loop8_sk_square_valueup_nav_discount` | SK스퀘어 | success_candidate | 실제 소각과 NAV discount가 Stage 2 근거, 반복 소각과 discount 축소 가격경로 필요 |
| `r6_loop8_hana_dunamu_equity_option` | 하나금융/하나은행 | success_candidate | 두나무 지분 옵션은 Stage 2, 지분법·규제승인·자본비율 영향 확인 필요 |
| `r6_loop8_samsung_life_nav_valueup` | 삼성생명 | success_candidate | hidden NAV와 book discount는 Stage 2, 매각대금 활용과 K-ICS/CSM 필요 |
| `r6_loop8_naver_dunamu_digital_asset_event` | 네이버/네이버파이낸셜 | event_premium | 디지털자산 Stage 2/event material이지만 Upbit abnormal withdrawal로 trust watch |
| `r6_loop8_kakaobank_kakao_governance_watch` | 카카오뱅크/카카오 | failed_rerating | 인터넷은행 성장성보다 대주주 법적 리스크와 은행 지분 규제가 먼저 |
| `r6_loop8_stablecoin_theme_overheat` | Kakao Pay/LG CNS/Aton/ME2ON | overheat | 실제 규제수익 전 2~3배 가격 이동은 4B/event premium |
| `r6_loop8_kakao_pay_privacy_4c_watch` | 카카오페이 | 4c_thesis_break | privacy/data transfer fine은 payment fintech Green hard gate |

## 산출물

- `src/e2r/sector/round210_r6_loop8_financial_capital_digital_price_validation.py`
- `src/e2r/cli/build_round210_r6_loop8_report.py`
- `tests/test_round210_r6_loop8_financial_capital_digital_price_validation.py`
- `data/e2r_case_library/cases_r6_loop8_round210.jsonl`
- `data/sector_taxonomy/round210_r6_loop8_financial_capital_digital_price_validation_audit.json`
- `output/e2r_round210_r6_loop8_financial_capital_digital_price_validation/`

## Green Gate

필수:

- ROE 개선 또는 유지
- CET1/K-ICS capital buffer
- 실제 자사주 소각
- 반복 가능한 배당·소각
- credit cost/PF risk 통과
- PBR-ROE gap 축소 여지
- 규제수익 또는 지분법 수익
- privacy/data/governance trust 통과
- evidence 이후 가격경로

금지:

- low PBR only
- policy value-up only
- buyback without cancellation
- stablecoin policy theme only
- digital asset equity option without revenue
- fintech user growth without profit
- privacy/data trust break
- major shareholder legal risk

## 남은 작업

원시 수정주가 OHLC가 확보되지 않은 항목은 `price_data_unavailable_after_deep_search` 또는 `reported_*_anchor_not_full_ohlc`로 남겼다. 다음 단계에서 KRX/Naver/공식 가격 cache로 Stage 2/4B/4C 이후 MFE/MAE를 채워야 한다.

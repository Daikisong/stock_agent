# Checkpoint 28A Round 236 R6 Loop 10 Financial Capital Digital Price Validation

## 반영 범위

`docs/round/round_236.md`의 R6 금융·자본배분·디지털금융 가격경로 검증 라운드를 case-library 보강팩으로 반영했다.

- source round: `docs/round/round_236.md`
- analyst round id: `round_164`
- large sector: `FINANCIAL_CAPITAL_DIGITAL`
- production scoring changed: `false`
- candidate generation input: `false`
- shadow weight only: `true`
- price validation: `partial_with_reported_price_anchors`
- full OHLC complete: `false`

## 핵심 해석

이번 라운드의 핵심은 `저PBR`, `밸류업`, `스테이블코인`, `디지털자산 지분`, `IPO 기대`를 Stage 3-Green으로 바로 올리지 않는 것이다.

쉬운 예시:

- 은행주가 저PBR이라 올랐더라도 ROE, CET1, credit cost, 실제 소각·배당 반복성이 없으면 Stage 3-Green이 아니다.
- 증권주가 거래대금 사이클로 하루 13% 올라도 회사별 ROE와 brokerage/IB 수익 지속성이 없으면 cyclical Stage 2 또는 4B-watch다.
- 스테이블코인 관련주가 2~3배 올라도 발행 라이선스, reserve income, fee revenue가 없으면 가격 선반영 이벤트다.

## 추가 케이스

| case | company | classification | interpretation |
| --- | --- | --- | --- |
| `r6_loop10_bank_valueup_big4_kb_watch` | KB/Shinhan/Hana/Woori | `success_candidate` | Big4 이익과 밸류업 기대는 Stage 2 근거지만 ROE/CET1/credit cost와 반복 환원 실행 전 Green 금지 |
| `r6_loop10_securities_capital_market_boom` | 증권주 basket | `cyclical_success` | KOSPI bull market과 증권업종 급등은 cyclical Stage 2 및 4B-watch |
| `r6_loop10_sk_square_nav_discount_valueup` | SK스퀘어 | `success_candidate` | 실제 소각과 NAV discount는 Stage 2 근거, 반복 소각과 discount 축소 가격경로 필요 |
| `r6_loop10_samsung_life_nav_capital_release` | 삼성생명 | `success_candidate` | 삼성전자 지분 매각은 capital release 후보, K-ICS/CSM과 환원정책 확인 필요 |
| `r6_loop10_hana_dunamu_equity_option` | 하나금융/하나은행/Dunamu | `success_candidate` | 두나무 지분 옵션은 Stage 2, 지분법·규제수익·자본비율 영향 확인 전 Green 금지 |
| `r6_loop10_naver_dunamu_platform_merger_trust_watch` | NAVER/NAVER Financial/Dunamu | `event_premium` | 플랫폼 M&A는 Stage 2 이벤트지만 abnormal withdrawal은 exchange trust 4C-watch |
| `r6_loop10_internet_bank_kbank_kakaobank_watch` | K Bank/KakaoBank/Kakao | `success_candidate` | K Bank IPO는 Stage 2 후보, KakaoBank는 대주주 법적 리스크가 Green을 차단 |
| `r6_loop10_stablecoin_policy_theme_overheat` | Kakao Pay/stablecoin basket | `overheat` | 라이선스·reserve income·fee revenue 전 가격 급등은 4B/event premium |

## Green Gate

R6 Stage 3-Green 후보에는 다음 증거가 필요하다.

- `roe_improvement_or_sustainability`
- `cet1_kics_or_capital_buffer`
- `actual_buyback_cancellation_or_repeated_dividend_execution`
- `credit_cost_pf_risk_passed`
- `pbr_roe_gap_rerating_runway`
- `capital_release_or_nav_monetization_quality`
- `regulated_digital_revenue_or_equity_method_income`
- `privacy_exchange_trust_governance_passed`
- `price_path_after_evidence`

다음 패턴은 Green을 막는다.

- `low_pbr_only`
- `policy_valueup_only`
- `treasury_buyback_without_cancellation`
- `stablecoin_policy_theme_only`
- `digital_asset_equity_option_without_revenue`
- `fintech_user_growth_without_profit`
- `internet_bank_ipo_without_listed_price_path`
- `major_shareholder_legal_risk`
- `exchange_trust_break`
- `capital_ratio_weakening_after_mna`
- `event_rally_before_regulated_revenue`

## 산출물

- `src/e2r/sector/round236_r6_loop10_financial_capital_digital_price_validation.py`
- `src/e2r/cli/build_round236_r6_loop10_report.py`
- `tests/test_round236_r6_loop10_financial_capital_digital_price_validation.py`
- `data/e2r_case_library/cases_r6_loop10_round236.jsonl`
- `data/sector_taxonomy/round236_r6_loop10_financial_capital_digital_price_validation_audit.json`
- `output/e2r_round236_r6_loop10_financial_capital_digital_price_validation/`

## 검증 명령

```bash
PYTHONPATH=src python -m e2r.cli.build_round236_r6_loop10_report
PYTHONPATH=src python -m unittest tests.test_round236_r6_loop10_financial_capital_digital_price_validation -v
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
git diff --check
```

## 남은 작업

원시 수정주가 OHLC가 없는 항목은 `reported_*_anchor_not_full_ohlc`로 남겼다. 다음 가격 backfill 라운드에서 Stage 2/4B/4C 기준 가격, MFE/MAE, peak/drawdown을 채워야 한다.

이번 패치는 production scoring을 바꾸지 않는다. 예를 들어 `스테이블코인 테마 + 주가 급등`은 학습용 반례로 남을 뿐, 라이브 후보 생성이나 Stage 3-Green 승격 입력으로 쓰이지 않는다.

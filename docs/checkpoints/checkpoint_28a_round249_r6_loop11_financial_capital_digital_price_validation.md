# Checkpoint 28A Round 249: R6 금융·자본배분·디지털금융 가격경로 검증

## 목적

`docs/round/round_249.md`의 R6 Loop 11 내용을 calibration/evaluation 전용 데이터팩으로 반영했다. 이번 라운드는 금융지주 value-up, 증권 거래대금 cycle, holding NAV discount, 보험 NAV capital release, 은행의 디지털자산 지분투자, NAVER/Dunamu deal, 인터넷은행 IPO/governance, KRW stablecoin 과열을 비교한다.

쉬운 예시는 이렇다. 은행주가 `저PBR`과 `밸류업` 뉴스로 오를 수는 있지만, ROE, CET1, credit cost, 실제 자사주 소각과 반복 배당이 확인되기 전에는 Stage 3-Green이 아니다.

## 반영 파일

- `src/e2r/sector/round249_r6_loop11_financial_capital_digital_price_validation.py`
- `src/e2r/cli/build_round249_r6_loop11_report.py`
- `tests/test_round249_r6_loop11_financial_capital_digital_price_validation.py`
- `data/e2r_case_library/cases_r6_loop11_round249.jsonl`
- `data/sector_taxonomy/round249_r6_loop11_financial_capital_digital_price_validation_audit.json`
- `output/e2r_round249_r6_loop11_financial_capital_digital_price_validation/`

## 추가/확인한 Archetype

- `BANK_VALUEUP_ROE_PBR_RERATING`
- `SECURITIES_MARKET_VOLUME_CYCLE`
- `HOLDING_NAV_DISCOUNT_VALUEUP`
- `INSURANCE_NAV_CAPITAL_RELEASE`
- `DIGITAL_ASSET_BANK_EQUITY_OPTION`
- `DIGITAL_ASSET_PLATFORM_MERGER_TRUST_WATCH`
- `INTERNET_BANK_IPO_PROFITABILITY`
- `INTERNET_BANK_GOVERNANCE_4C`
- `KRW_STABLECOIN_POLICY_OVERHEAT`
- `PRICE_ONLY_RALLY`
- `EVENT_PREMIUM`

## 케이스 요약

- 총 케이스: 8
- success_candidate: 5
- cyclical_success: 1
- event_premium: 1
- overheat: 1
- dated Stage 3 케이스: 0
- Stage 4B-watch 케이스: 8
- 4C-watch 케이스: 2
- hard 4C confirmed: false
- full OHLC 완료: false
- price validation 상태: `partial_with_reported_price_anchors`

주요 케이스는 Big-4 금융지주 value-up, 증권주 basket, SK Square, Samsung Life, Hana Bank/Dunamu, NAVER Financial/Dunamu, K Bank/KakaoBank, KRW stablecoin basket이다.

## Green Gate

R6 Stage 3-Green은 `저PBR`, `밸류업`, `디지털자산`, `스테이블코인`이라는 이름표만으로 부여하지 않는다. 필요한 필드는 다음이다.

- ROE 개선 또는 유지
- CET1 또는 K-ICS capital buffer
- credit cost 또는 PF risk 통과
- 실제 자사주 소각
- 반복 배당 또는 반복 소각 정책
- PBR-ROE gap과 rerating runway
- capital release 활용처 확인
- 규제수익 또는 지분법 이익 확인
- platform/exchange trust 통과
- 증거 이후 가격경로 확인

반대로 저PBR 단독, 정책 value-up 단독, 소각 없는 자사주 매입, stablecoin 정책 테마, 지분법/규제수익 없는 디지털자산 지분투자, user growth without profit, 대주주 법적 리스크, 거래소 신뢰 훼손은 Green 금지 또는 RedTeam 입력이다.

## 4B/4C 판단

4B-watch는 다음처럼 “가격이 먼저 간” 상태를 감시한다.

- ROE와 환원 실행 전 PBR rerating
- 증권업종 +10% 이상 급등 전 brokerage/IB revenue 미확인
- underlying asset rally 뒤 지주 NAV trade crowded
- 보험 NAV rally가 capital policy보다 먼저 반영
- 디지털자산 지분가치가 규제수익보다 먼저 반영
- M&A/all-stock deal이 승인 전 가격에 반영
- stablecoin 관련주가 license 전 2~3배 상승

Hard 4C gate는 PF credit cost 급증, CET1/K-ICS 약화, 소각 취소, 배당정책 후퇴, 인수 후 자본비율 훼손, 대주주 적격성 리스크, 금융범죄/governance legal break, exchange abnormal withdrawal, stablecoin issuer regulation reversal 등이다.

## 산출물

- `round249_r6_loop11_price_validation_summary.md`
- `round249_r6_loop11_case_matrix.csv`
- `round249_r6_loop11_target_aliases.csv`
- `round249_r6_loop11_score_adjustments.csv`
- `round249_r6_loop11_shadow_weights.csv`
- `round249_r6_loop11_deep_sub_archetypes.csv`
- `round249_r6_loop11_price_validation_fields.csv`
- `round249_r6_loop11_green_gate_review.md`
- `round249_r6_loop11_price_validation_plan.md`
- `round249_r6_loop11_stage4b_4c_review.md`

## 검증

실행 명령:

```bash
PYTHONPATH=src python -m e2r.cli.build_round249_r6_loop11_report
PYTHONPATH=src python -m unittest tests.test_round249_r6_loop11_financial_capital_digital_price_validation -v
```

전체 검증은 커밋 전 `compileall`, 전체 unittest, `git diff --check`로 확인했다.

## 변경하지 않은 것

- production scoring 변경 없음
- candidate generation 입력으로 사용하지 않음
- Stage 3-Green threshold 완화 없음
- full OHLC, CET1, K-ICS, credit cost, 지분법 이익, stablecoin revenue를 임의 생성하지 않음
- 투자 권고 문구 없음

이번 라운드는 점수 엔진을 바꾼 것이 아니라, 나중에 R6 금융·자본배분·디지털금융 scoring을 설계할 때 쓸 검증용 케이스와 gate를 추가한 것이다.

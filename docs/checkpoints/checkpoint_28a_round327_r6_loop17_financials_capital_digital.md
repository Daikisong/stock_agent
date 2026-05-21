# Checkpoint 28A Round 327 R6 Loop 17 Financials / Capital Allocation / Digital Finance

## 반영 내용

- `docs/round/round_327.md`의 R6 Loop 17 트리거 검증 내용을 calibration-only 데이터로 반영했다.
- 신규 canonical archetype 8개를 추가했다.
- case library, trigger calibration, shadow weight profile, audit JSON, Markdown 보고서를 생성했다.
- production scoring, StageClassifier, candidate generation은 변경하지 않았다.

## 핵심 결론

- KOSPI boom / securities firms는 Stage2-Actionable이다. 예를 들어 KOSPI +6.45%, 증권업 +13.5%처럼 증권주 거래대금 beta가 직접 보일 때는 Layer-1/Stage2 신호로 쓸 수 있다.
- 은행은 금융지수 +4.2%만으로 Green이 아니다. 은행은 ROE, CET1, credit cost, 실제 환원정책이 따로 닫혀야 한다.
- SK Square는 buyback + cancellation + holding discount가 닫힌 Stage2-Actionable이다. 다만 일회성 자사주가 아니라 반복 가능한 정책인지가 Yellow/Green gate다.
- Hana Bank / Dunamu는 crypto exchange strategic stake Stage2다. Upbit 점유율과 지분가치는 강하지만 은행 EPS/fee income으로 이어지기 전에는 Green이 아니다.
- Naver Financial / Dunamu는 Stage2 M&A와 cyber/custody 4B가 동시에 있다. Upbit abnormal withdrawal 같은 운영 리스크를 무시하면 false positive가 된다.
- Kakao Pay / won-stablecoin은 speculative Stage2 overheat다. 법, 준비금, issuer rule, 실제 결제수익 전에는 Green 금지다.
- BOK stablecoin / kimchi bond policy는 Stage2 infrastructure지만 FX liquidity와 issuer-quality 4B가 붙는다.
- Hong Kong ELS sanction은 bank 4B다. value-up 점수 전에 소비자보호 비용을 선차감해야 한다.
- Short-selling normalization은 market-infra Stage2지만 retail backlash와 volatility 4B를 병기한다.

## 생성 파일

- `src/e2r/sector/round327_r6_loop17_financials_capital_digital_trigger_validation.py`
- `src/e2r/cli/build_round327_r6_loop17_report.py`
- `tests/test_round327_r6_loop17_financials_capital_digital_trigger_validation.py`
- `data/e2r_case_library/cases_r6_loop17_round255.jsonl`
- `data/e2r_trigger_calibration/triggers_r6_loop17_round255.jsonl`
- `data/sector_taxonomy/round327_r6_loop17_financials_capital_digital_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round255_r6_loop17_v1.csv`
- `output/e2r_round327_r6_loop17_financials_capital_digital_trigger_validation/`

## Stage 판정

- Stage2-Actionable: 2건
- Stage2 / policy Stage2 / speculative Stage2: 5건
- Stage3-Yellow: 0건
- Stage3-Green: 0건
- 4B-watch: 8건
- hard 4C 확정: 0건

## 바꾸지 않은 것

- production scoring 변경 없음
- StageClassifier threshold 변경 없음
- case library를 candidate-generation input으로 사용하지 않음
- full adjusted OHLC가 없으므로 MFE/MAE/peak/drawdown을 만들지 않음
- 금융 beta, 자사주, crypto stake, stablecoin, 공매도 정상화 headline만으로 Stage3-Green을 만들지 않음

## 다음 작업

R7 Loop 17에서는 바이오, 헬스케어, 의료기기 쪽에서 같은 방식으로 trigger-level validation을 이어간다.

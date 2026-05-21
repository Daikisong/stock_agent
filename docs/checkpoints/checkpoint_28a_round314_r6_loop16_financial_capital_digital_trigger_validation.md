# Checkpoint 28A Round 314: R6 Loop 16 금융 자본배분 / 디지털금융 트리거 검증

## 목적

`docs/round/round_314.md`의 R6 Loop 16 내용을 케이스 라이브러리와 트리거 검증팩으로 반영했다.

이번 라운드는 생산 점수 로직을 바꾸지 않는다. 예를 들어 삼성전자 자사주 매입/소각은 Stage2 후보 신호가 될 수 있지만, 실제 ROE/EPS 또는 FCF 개선이 확인되기 전에는 Stage3-Green으로 올리지 않는다.

## 추가된 아키타입

- `BUYBACK_CANCELLATION_VALUEUP_STAGE2_ACTIONABLE`
- `BROKERAGE_TRADING_VOLUME_STAGE2_BETA`
- `BANK_DIGITAL_ASSET_STAKE_STAGE2_WITH_CAPITAL_GATE`
- `FINTECH_CRYPTO_EXCHANGE_MA_STAGE2_WITH_SECURITY_4B`
- `STABLECOIN_POLICY_EVENT_PREMIUM_4B`
- `ELS_MISSELLING_CONSUMER_PROTECTION_4C`
- `FX_OVERSEAS_STOCK_FLOW_4C_WATCH`
- `PRIVATE_FINTECH_STABLECOIN_IPO_OPTIONALITY_STAGE2`

기존 `HOLDCO_DISCOUNT_BUYBACK_STAGE2`도 이번 라운드의 목표 아키타입으로 사용했다.

## 케이스 요약

- 케이스 수: 9
- 트리거 수: 9
- Stage2-Actionable 후보: 3
- Stage2 이벤트/참조 후보: 5
- 비상장 Stage2 참조: 1
- Stage3-Green 확정: 0
- 4B-watch: 6
- 4C-watch: 4
- hard 4C: 1

## 핵심 규칙

- 자사주 매입은 소각과 ROE/EPS 회복이 같이 있어야 Green 후보가 된다.
- 증권주 거래대금 베타는 수수료 수익과 ROE로 연결되기 전까지 Green이 아니다.
- 디지털자산 지분/인수합병은 승인, 자본비율, 커스터디, AML, 보안 통제가 필요하다.
- 스테이블코인 정책 테마는 발행자 라이선스, 준비금 규칙, 수익모델이 없으면 4B-watch다.
- ELS 불완전판매는 은행 리레이팅을 막는 소비자보호 hard 4C 게이트다.

## 생성 파일

- `src/e2r/sector/round314_r6_loop16_financial_capital_digital_trigger_validation.py`
- `src/e2r/cli/build_round314_r6_loop16_report.py`
- `tests/test_round314_r6_loop16_financial_capital_digital_trigger_validation.py`
- `data/e2r_case_library/cases_r6_loop16_round242.jsonl`
- `data/e2r_trigger_calibration/triggers_r6_loop16_round242.jsonl`
- `data/sector_taxonomy/round314_r6_loop16_financial_capital_digital_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round242_r6_loop16_v1.csv`
- `output/e2r_round314_r6_loop16_financial_capital_digital_trigger_validation/`

## 바꾸지 않은 것

- production scoring 변경 없음
- StageClassifier threshold 변경 없음
- 케이스 라이브러리를 후보 생성 입력으로 사용하지 않음
- full adjusted OHLC가 없는데 MFE/MAE를 발명하지 않음
- 투자 권고 문구 없음

## 다음 라운드

R7 Loop 16에서는 이 라운드의 금융 자본배분/디지털금융 케이스를 더 넓은 은행, 증권, 핀테크, 정책 이벤트 사례와 비교해 4B/4C 게이트를 더 정교화해야 한다.

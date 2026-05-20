# Checkpoint 28A Round 275 R6 Loop 13 Financial Capital Digital Price Validation

## 목적

`docs/round/round_275.md`의 금융·자본배분·디지털금융 케이스를 calibration-only 자료로 구조화했다.

이번 라운드의 핵심은 단순한 `value-up`, `자사주`, `Dunamu 지분`, `인터넷은행 IPO`, `스테이블코인`, `거래대금 증가`를 Stage 3-Green으로 보지 않는 것이다. 예를 들어 은행주가 정책 기대감으로 움직여도 CET1, ROE, NIM, credit cost, RWA control, 실제 환원 실행이 확인되기 전에는 Stage 2 또는 4B-watch로 남긴다.

## 반영 내용

- canonical archetype 8개 추가, 기존 stablecoin gate 1개 재사용
- Round 275 전용 케이스 팩 추가
- JSONL case library 생성
- audit JSON 생성
- shadow weight, deep sub-archetype, green gate, 4B/4C review 출력
- production scoring, 후보 생성, StageClassifier threshold는 변경하지 않음

## 추가/사용 archetype

- `BANK_VALUE_UP_RERATING_STAGE2`
- `HOLDCO_DISCOUNT_BUYBACK_CANCELLATION`
- `INSURANCE_HOLDING_STAKE_REGULATORY_GATE`
- `DIGITAL_ASSET_BANK_STAKE_STAGE2`
- `FINTECH_CRYPTO_M_AND_A_TRUST_GATE`
- `INTERNET_BANK_IPO_OVERHANG`
- `STABLECOIN_POLICY_OVERHEAT_FX_GATE`
- `CRYPTO_EXCHANGE_OPERATIONAL_HARD_REFERENCE`
- `SECURITIES_TRADING_VOLUME_EVENT_PREMIUM`

## 케이스 요약

- 케이스 수: 8
- Stage 3 dated case: 0
- success_candidate: 5
- event_premium: 2
- overheat: 1
- hard 4C reference: 1
- direct listed hard 4C: 0

## 핵심 가드레일

- Value-up headline만으로 Green 금지
- 섹터 랠리만으로 은행 Green 금지
- 인터넷은행 IPO valuation만으로 Green 금지
- Dunamu/Upbit 지분만으로 은행 EPS 증거를 만들지 않음
- Stablecoin policy basket은 issuer economics와 FX gate 전까지 4B/4C watch
- 거래소 운영 오류는 hard 4C reference로 RedTeam에 남기고 Green 근거로 쓰지 않음

## 생성 파일

- `src/e2r/sector/round275_r6_loop13_financial_capital_digital_price_validation.py`
- `src/e2r/cli/build_round275_r6_loop13_report.py`
- `tests/test_round275_r6_loop13_financial_capital_digital_price_validation.py`
- `data/e2r_case_library/cases_r6_loop13_round275.jsonl`
- `data/sector_taxonomy/round275_r6_loop13_financial_capital_digital_price_validation_audit.json`
- `output/e2r_round275_r6_loop13_financial_capital_digital_price_validation/`

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_round275_r6_loop13_financial_capital_digital_price_validation -v
PYTHONPATH=src python -m compileall -q src/e2r/sector/archetypes.py src/e2r/sector/round275_r6_loop13_financial_capital_digital_price_validation.py src/e2r/cli/build_round275_r6_loop13_report.py tests/test_round275_r6_loop13_financial_capital_digital_price_validation.py
PYTHONPATH=src python -m e2r.cli.build_round275_r6_loop13_report
```

라운드 전용 테스트 7개는 통과했다. 전체 테스트는 최종 커밋 전에 별도로 실행한다.

## 해석

이번 패치는 점수를 바꾸는 작업이 아니라 금융 archetype의 실패 패턴을 더 정확히 기록하는 작업이다. 예를 들어 `SK Square`는 NAV discount와 자사주 소각이 강한 Stage 2 후보지만, 반복 실행과 NAV bridge가 확인되기 전에는 Green으로 올리지 않는다. `Bithumb`은 상장 직접 케이스가 아니라 crypto exchange operational hard reference다.

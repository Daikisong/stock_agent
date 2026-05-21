# Checkpoint 28A Round 301 R6 Loop 15 Financial/Capital/Digital Trigger Validation

## 반영 내용

- `docs/round/round_301.md`를 R6 금융/자본배분/디지털금융 trigger-level calibration pack으로 구조화했다.
- production scoring은 바꾸지 않았다.
- case library는 candidate-generation input이 아니라 calibration/evaluation material로만 남겼다.
- full adjusted OHLC 30D/90D/180D/1Y는 확보하지 못했으므로 reported event return과 event anchor만 기록했다.
- OHLC 미확보를 이유로 Stage2 또는 Yellow 후보를 임의 강등하지 않고 `reported_event_anchor_not_full_ohlc`로 분리했다.

쉬운 예:
삼성전자의 10T won buyback과 3T won cancellation은 Stage2-Actionable 신호다. 하지만 HBM 경쟁력 회복, OP/FCF 회복, 나머지 buyback 실행이 없으면 Stage3-Green 근거가 아니다.

## 추가된 canonical archetype

- `BROKERAGE_MARKET_VOLUME_STAGE2_ACTIONABLE`
- `FINANCIAL_GROUP_VALUEUP_STAGE2`
- `BUYBACK_CAPITAL_ALLOCATION_STAGE2_ACTIONABLE`
- `HOLDCO_DISCOUNT_ACTIVIST_STAGE2`
- `DIGITAL_ASSET_BANK_ENTRY_STAGE2`
- `CRYPTO_EXCHANGE_MA_STAGE2_WITH_SECURITY_4C`
- `STABLECOIN_POLICY_4B_OVERHEAT`
- `FINTECH_DATA_GOVERNANCE_4C`
- `KAKAO_BANK_CONTROL_REGULATORY_4C`

## 산출물

- `src/e2r/sector/round301_r6_loop15_financial_capital_digital_trigger_validation.py`
- `src/e2r/cli/build_round301_r6_loop15_report.py`
- `tests/test_round301_r6_loop15_financial_capital_digital_trigger_validation.py`
- `data/e2r_case_library/cases_r6_loop15_round229.jsonl`
- `data/e2r_trigger_calibration/triggers_r6_loop15_round229.jsonl`
- `data/sector_taxonomy/round301_r6_loop15_financial_capital_digital_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round229_r6_loop15_v1.csv`
- `output/e2r_round301_r6_loop15_financial_capital_digital_trigger_validation/`

## 핵심 판정

- Brokerage basket: KOSPI 7,000 돌파일 securities +13.5%로 Stage2-Actionable. 다만 거래대금, brokerage revenue, margin finance, IB fee 확인 전 Green 금지.
- Financial Value-Up: 정책 beta는 Stage2. 은행별 CET1, ROE, payout, buyback cancellation, credit cost가 Stage gate.
- Samsung buyback: 10T won buyback, 3T won immediate cancellation, event +7.2%로 Stage2-Actionable. business recovery gate가 남음.
- SK Square: 100B won cancellation, new 100B won buyback, activist, NAV discount로 Stage2-Actionable. discount narrowing과 반복 실행 필요.
- Hana/Dunamu: bank digital-asset entry Stage2. regulatory approval, monetization, capital-ratio impact, exchange trust가 필요.
- Naver/Dunamu: Stage2 M&A와 security 4C-watch가 동시에 붙음. Upbit abnormal withdrawal은 custody/security hard overlay.
- Stablecoin policy frenzy: Kakao Pay 2x+, LG CNS +70%, Aton +80%, ME2ON 3x는 4B-overheat. license, reserve, fee revenue 전까지 Stage3 금지.
- Kakao founder/KakaoBank risk: founder/legal risk는 financial-license 및 bank-control 4C-watch.

## Shadow score 조정축

올릴 축:

- `actual_buyback_cancellation`
- `cet1_capital_return_capacity`
- `roe_and_credit_cost_visibility`
- `brokerage_trading_value_conversion`
- `nav_discount_narrowing`
- `regulatory_approval_for_fintech_ma`
- `custody_security_trust`
- `stablecoin_license_and_reserve_quality`
- `customer_data_rights_and_privacy`
- `financial_license_governance_risk_cleared`

내릴 축:

- `policy_valueup_headline_only`
- `buyback_announcement_without_cancellation`
- `crypto_exchange_market_share_only`
- `stablecoin_policy_hype_only`
- `fintech_ma_without_regulatory_approval`
- `brokerage_beta_without_trading_value`
- `founder_legal_risk_ignored`

## What Not To Change

- Stage3-Green threshold를 낮추지 않는다.
- policy, buyback, M&A, market share, stablecoin headline만으로 Green을 만들지 않는다.
- case library를 production candidate generation input으로 쓰지 않는다.
- full OHLC가 없는데 MFE/MAE를 발명하지 않는다.
- crypto/fintech에서는 security, custody, data rights, regulatory approval을 무시하지 않는다.

## 검증

- `PYTHONPATH=src python -m unittest tests.test_round301_r6_loop15_financial_capital_digital_trigger_validation -v`
- `PYTHONPATH=src python -m e2r.cli.build_round301_r6_loop15_report`

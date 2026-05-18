# Checkpoint 28A Round 191: R6 Loop 12 Financial / Capital / Digital Audit

`docs/round/round_191.md`의 R6 Loop 12 내용을 Round190 팩에 대한 follow-up audit으로 반영했다.

## 반영 범위

- `src/e2r/sector/round191_r6_loop12_financial_capital_digital_audit.py`
- `src/e2r/cli/build_round191_r6_loop12_audit_report.py`
- `tests/test_round191_r6_loop12_financial_capital_digital_audit.py`
- `data/sector_taxonomy/round191_r6_loop12_financial_capital_digital_audit.json`
- `output/e2r_round191_r6_loop12_financial_capital_digital_audit/*`

## 왜 audit으로 처리했나

Round191은 새 섹터나 새 canonical target을 추가하기보다, Round190의 R6 금융·자본배분·디지털금융 팩이 문서의 필수 요건을 빠짐없이 담았는지 확인하는 내용이다.

예를 들어 삼성생명, 메리츠금융, 하나금융-Dunamu, Toss FacePay, NICE, 원화 스테이블코인, 카카오페이 privacy, 삼성전자 자사주 소각 price-fail은 Round190에 이미 케이스로 들어갔다. Round191에서는 같은 케이스를 복제하지 않고, 다음 항목이 실제 산출물에 존재하는지 검증했다.

- 11개 required target
- 13개 required case
- Stage 3 `6 of 9` 조건
- Stage 4B `4 of 6` 조건
- Stage 4C hard gate
- R6 price/backfill fields
- production scoring unchanged guardrail
- case records not candidate-generation input guardrail

## Audit 결과

- audit_check_count: 9
- passed_check_count: 9
- failed_check_count: 0
- required_target_count: 11
- required_case_count: 13
- hard_gate_target_count: 3
- production_scoring_changed: false
- case_records_are_candidate_generation_input: false

## 핵심 확인 사항

Stage 3-Green은 다음 같은 이름만으로 만들 수 없도록 유지했다.

- 저PBR
- 밸류업
- 스테이블코인
- Dunamu
- FacePay
- 고배당
- 자사주 소각 기대

예를 들어 `스테이블코인 + 주가 급등`은 관심 신호지만, 실제 `stablecoin_issuance_volume`, `reserve_income`, `take_rate`, 규제 안정성이 없으면 Stage 3가 아니라 4B-watch다.

## 생성 산출물

```bash
PYTHONPATH=src python -m e2r.cli.build_round191_r6_loop12_audit_report
```

생성 파일:

- `data/sector_taxonomy/round191_r6_loop12_financial_capital_digital_audit.json`
- `output/e2r_round191_r6_loop12_financial_capital_digital_audit/round191_r6_loop12_audit_summary.md`
- `output/e2r_round191_r6_loop12_financial_capital_digital_audit/round191_r6_loop12_coverage_matrix.csv`
- `output/e2r_round191_r6_loop12_financial_capital_digital_audit/round191_r6_loop12_followup_backfill.md`
- `output/e2r_round191_r6_loop12_financial_capital_digital_audit/round191_r6_loop12_guardrail_review.md`

## 검증

```bash
PYTHONPATH=src python -m unittest tests/test_round191_r6_loop12_financial_capital_digital_audit.py -v
```

결과: 통과.

## 다음 작업

R6는 이제 구조와 guardrail이 맞다. 다음에는 실제 backfill이 필요하다.

- 삼성생명: `nav_discount`, `major_equity_stake_value`, `k_ics_ratio`, `csm`, `roe`, `dividend_per_share`
- 메리츠금융: `buyback_amount`, `cancelled_share_amount`, `total_shareholder_return_ratio`, `credit_cost`
- 하나금융-Dunamu: `digital_asset_stake_value`, `equity_method_income`, `regulatory_approval_pending`, `exchange_security_incident_flag`
- 원화 스테이블코인: `stablecoin_issuance_volume`, `reserve_income`, `take_rate`, `stablecoin_regulatory_status`
- FacePay: `merchant_count`, `user_count`, `transaction_volume`, `biometric_data_risk_flag`

이 값들이 들어오기 전에는 생산 점수나 StageClassifier threshold를 바꾸면 안 된다.

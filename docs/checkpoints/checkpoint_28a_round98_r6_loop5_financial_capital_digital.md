# Checkpoint 28A Round 98 R6 Loop 5

## 목적

`docs/round/round_98.md`의 금융·자본배분·디지털금융 분류를 case-library calibration pack으로 반영했다. 이 pack은 생산 scoring 입력이 아니다. 예를 들면 `저PBR`이나 `원화 스테이블코인 발행 의향`은 Stage 1 재료일 수 있지만, ROE/CET1/소각 실행 또는 준비금/상환/수익모델이 없으면 Stage 3-Green 근거가 아니다.

## 반영 내용

- R6 Loop 5 score target 25개를 생성했다.
- 신규/분리 archetype을 추가했다.
  - `BANK_HOLDING_VALUEUP_CAPITAL_RETURN`
  - `TREASURY_CANCEL_MANDATE_POLICY`
  - `KRW_STABLECOIN_INFRA_OPTION`
  - `STABLECOIN_BANK_DEPOSIT_DISINTERMEDIATION`
  - `FINTECH_IPO_VALUATION_RISK`
  - `AI_WINDFALL_CITIZEN_DIVIDEND_POLICY_SHOCK`
- 우선 검증 case 19개를 `cases_r6_loop5_round98.jsonl`에 기록했다.
- price validation field schema를 R6 문서 기준으로 확장했다.
- 생산 scoring, staging, RedTeam, E2R standard flow는 이 pack을 import하지 않는다.

## 산출물

- `data/e2r_case_library/cases_r6_loop5_round98.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round98_r6_loop5_v5.csv`
- `output/e2r_round98_r6_loop5_financial_capital_digital/round98_r6_loop5_financial_capital_digital_summary.md`
- `output/e2r_round98_r6_loop5_financial_capital_digital/round98_r6_loop5_case_matrix.csv`
- `output/e2r_round98_r6_loop5_financial_capital_digital/round98_r6_loop5_stage_date_plan.csv`
- `output/e2r_round98_r6_loop5_financial_capital_digital/round98_r6_loop5_green_guardrails.md`
- `output/e2r_round98_r6_loop5_financial_capital_digital/round98_r6_loop5_risk_overlays.md`
- `output/e2r_round98_r6_loop5_financial_capital_digital/round98_r6_loop5_price_validation_plan.md`
- `output/e2r_round98_r6_loop5_financial_capital_digital/round98_r6_loop5_price_fields.csv`

## 요약 수치

- target_count: 25
- case_candidate_count: 19
- success_candidate_count: 8
- failed_rerating_count: 1
- event_premium_count: 1
- stage4b_case_count: 1
- stage4c_case_count: 8
- green_possible_count: 3
- watch_yellow_first_count: 13
- redteam_first_count: 9
- gate_only_target_count: 6

## 핵심 Guardrail

- 자사주 매입은 자사주 소각이 아니다.
- 자사주 소각 의무화 정책은 macro tailwind이지 개별 종목 Stage 3 근거가 아니다.
- 은행·금융지주 Green은 ROE, CET1, credit cost, PF exposure, 실제 환원 실행이 함께 필요하다.
- 핀테크 user count나 IPO valuation은 Stage 1/2 재료일 뿐이다.
- 원화 스테이블코인과 regulated stablecoin은 규제 승인, 준비금, 상환, 발행량, 수수료/이자수익 모델 전까지 Green이 아니다.
- 은행의 거래소 지분투자는 지분법이익, 협업매출, 규제, 보안 안정성 전까지 Stage 1/2다.
- 알고리즘형 stablecoin, 예금 유출/무이자 준비금 규제, 보안 사고, 지배구조 실행 실패는 RedTeam overlay다.

## 검증

- `PYTHONPATH=src python -m unittest tests.test_round98_r6_loop5_financial_capital_digital -v`
- `PYTHONPATH=src python -m e2r.cli.build_round98_r6_loop5_report`

전체 테스트 결과는 커밋 전 검증 기록에 따른다.

# Checkpoint 28A Round 319 R11 Loop 16 Policy / Geopolitics / Disaster Trigger Validation

## 반영 내용

- `docs/round/round_319.md`의 R11 Loop 16 내용을 calibration-only 데이터로 반영했다.
- 새 canonical archetype 8개를 추가했다.
  - `GEOPOLITICAL_DEFENSE_EXPORT_STAGE2_ACTIONABLE`
  - `MISSILE_DEFENSE_COMBAT_VALIDATION_STAGE3_YELLOW`
  - `NUCLEAR_EXPORT_POLICY_STAGE2_WITH_LEGAL_4B`
  - `POLITICAL_CRISIS_MARKET_HARD_4C`
  - `COMMERCIAL_ACT_VALUEUP_STAGE2_POLICY`
  - `FOREIGN_STRATEGIC_CAPITAL_POLICY_STAGE2_ACTIONABLE`
  - `SHORT_SELLING_MARKET_INTEGRITY_STAGE2_4B`
  - `NATURAL_DISASTER_RECONSTRUCTION_4C_RELIEF`
- Round319 전용 케이스 라이브러리, 트리거 캘리브레이션, shadow weight, 감사 파일, 보고서를 생성했다.
- 생산 scoring, staging, candidate generation은 변경하지 않았다.

## 산출 파일

- `src/e2r/sector/round319_r11_loop16_policy_geopolitics_disaster_event_trigger_validation.py`
- `src/e2r/cli/build_round319_r11_loop16_report.py`
- `tests/test_round319_r11_loop16_policy_geopolitics_disaster_event_trigger_validation.py`
- `data/e2r_case_library/cases_r11_loop16_round247.jsonl`
- `data/e2r_trigger_calibration/triggers_r11_loop16_round247.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round247_r11_loop16_v1.csv`
- `data/sector_taxonomy/round319_r11_loop16_policy_geopolitics_disaster_event_trigger_validation_audit.json`
- `output/e2r_round319_r11_loop16_policy_geopolitics_disaster_event_trigger_validation/`

## 핵심 판정

- Hanwha Aerospace / Romania K9 export는 Stage2-Actionable이다. 다만 대규모 equity raise 이후 dilution 4B를 붙인다.
- LIG Nex1 / Iraq M-SAM II와 Iran-war combat validation은 Stage3-Yellow 후보이다. 생산 ramp, 납기, 마진, 반복 수주가 닫히기 전에는 Green이 아니다.
- KHNP / Czech nuclear는 preferred bidder 기준 Stage2지만, EDF legal challenge와 final contract 미확정 때문에 legal 4B가 붙는다.
- Martial law shock는 broad-market hard 4C다. 예를 들어 `KOSPI/KRW` 충격은 개별 기업 EPS 근거가 아니므로 회사별 Stage2로 바꾸면 안 된다.
- Commercial Act / Value-Up은 Stage2 policy reform이다. 회사별 buyback cancellation, dividend, board action 전에는 Green이 아니다.
- Samsung SDS / KKR은 Stage2-Actionable foreign strategic capital이다. CB dilution, AI execution, M&A ROIC가 4B gate다.
- Short-selling market-integrity policy는 Stage2 + liquidity/foreign-flow 4B다.
- 2025 wildfires는 disaster hard 4C reference다. 재건 수요는 가능하지만 listed-company contract가 없으면 투자 trigger로 만들지 않는다.

## Green 금지 기준

이번 라운드의 핵심은 headline과 실행 증거를 분리하는 것이다.

쉬운 예:

- 원전 `preferred bidder`는 좋은 Stage2 신호지만, 최종계약과 소송 해소 전에는 Green이 아니다.
- 상법 개정은 Value-Up Stage2 신호지만, 특정 회사가 실제로 자사주 소각이나 배당정책을 바꾸기 전에는 Green이 아니다.
- 재난 복구는 reconstruction theme이지만, 상장사 계약이나 보험손실 추정이 없으면 Stage2 후보로 만들지 않는다.

## Shadow Weight

올릴 축:

- `defense_export_contract_value`
- `defense_backlog_delivery_visibility`
- `combat_validation`
- `nuclear_final_contract_signing`
- `nuclear_legal_resolution`
- `board_fiduciary_reform_execution`
- `foreign_strategic_capital_execution`
- `market_integrity_enforcement`
- `political_stability_risk`
- `disaster_reconstruction_budget`

내릴 축:

- `defense_order_without_capacity`
- `defense_growth_with_dilution_ignored`
- `preferred_bidder_without_contract`
- `policy_reform_without_company_action`
- `foreign_capital_without_ROIC`
- `market_rule_without_flow_data`
- `political_crisis_treated_as_one_day_event`
- `disaster_relief_without_listed_contract`

이 weight는 `shadow_weight_only=true`이며 생산 점수에 적용하지 않았다.

## 검증

- Round319 단위 테스트 통과.
- 전체 테스트는 최종 커밋 전 다시 실행한다.

## 다음 작업

- R12 Loop 16도 동일하게 case row, trigger row, full-OHLC row를 분리한다.
- R11 방산/정책/원전/재난 아키타입은 아직 score implementation 대상이 아니다.
- 향후 scoring 반영 전에는 full adjusted OHLC MFE/MAE와 delivery/margin/legal/company-action evidence를 추가로 채워야 한다.

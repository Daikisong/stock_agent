# Checkpoint 28A Round 29: Score-Weight v1.4 Calibration Pack

## Summary

Round 29 반영은 production scoring 변경이 아니라 calibration/evaluation pack 추가다.
예를 들면 `방산`이라는 테마명 자체는 점수가 아니고, 정부 고객, 다년 계약, 수주잔고, 납품 스케줄, OPM 개선, dilution 리스크처럼 실제 EPS/FCF 지속성을 설명하는 증거만 미래 점수 설계 후보가 된다.

## Added

- `src/e2r/sector/round29_score_weight_v14.py`
- `src/e2r/cli/build_round29_score_weight_report.py`
- `tests/test_round29_score_weight_v14.py`
- `data/e2r_case_library/cases_v11_round29.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round29_v14.csv`
- `output/e2r_round29_score_weight_v14/round29_score_weight_v14_summary.md`
- `output/e2r_round29_score_weight_v14/round29_case_candidate_matrix.csv`
- `output/e2r_round29_score_weight_v14/round29_green_guardrail_review.md`
- `output/e2r_round29_score_weight_v14/round29_risk_boundary_review.md`
- `output/e2r_round29_score_weight_v14/round29_capital_allocation_risk_review.md`
- `output/e2r_round29_score_weight_v14/round29_price_validation_plan.md`

## Coverage

- score target count: 12
- case candidate count: 40
- success / structural candidate count: 13
- 4C thesis-break case count: 10
- Green-possible target count: 7
- Watch-first target count: 5
- RedTeam-first target count: 0

## Main Calibration Changes

- Defense remains Green-possible, but dilution and capital allocation are explicit guardrails.
- Shipbuilding needs newbuilding price, low-margin backlog rolloff, and margin recognition, not backlog size alone.
- Export consumer can pass visibility without contract quality when repeat demand, overseas channel, ASP, OPM, and FY1/FY2 evidence exist.
- Rail is contract-backlog style, but project margin, delivery, and financing risks are stronger gates.
- Chemicals, digital assets, ecommerce, battery/ESS, and securities stay Watch-first until cycle and risk evidence improves.
- Insurance and value-up use PBR-ROE-return execution logic, not generic EPS explosion logic.

## Guardrails

- Case IDs and theme labels are not production candidate input.
- No production scoring, staging, or RedTeam thresholds changed.
- No stage dates, prices, contract amounts, OP YoY, ASP, OPM, CSM, ROE, or transaction volume were invented.
- Stage 3-Green remains strict and must still require cross-evidence plus price-path validation.

## Verification

```bash
PYTHONPATH=src python -m unittest tests.test_round29_score_weight_v14 -v
PYTHONPATH=src python -m e2r.cli.build_round29_score_weight_report
```

The full suite is still expected to show the pre-existing unrelated `round_17.md` deletion failures until that deleted round document is restored or the old test is retired.

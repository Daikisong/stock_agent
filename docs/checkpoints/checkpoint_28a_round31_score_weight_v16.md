# Checkpoint 28A Round 31: Score-Weight v1.6 Calibration Pack

## Summary

Round 31 반영은 production scoring 변경이 아니라 calibration/evaluation pack 추가다.
예를 들면 데이터센터 REIT는 AI 테마라서 점수를 주는 것이 아니라, hyperscale tenant, 장기 임대계약, occupancy, 전력·냉각·토지 확보, FFO/AFFO 성장, funding cost 통제가 있어야 Green 가능 후보가 된다.

## Added

- `src/e2r/sector/round31_score_weight_v16.py`
- `src/e2r/cli/build_round31_score_weight_report.py`
- `tests/test_round31_score_weight_v16.py`
- `data/e2r_case_library/cases_v13_round31.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round31_v16.csv`
- `output/e2r_round31_score_weight_v16/round31_score_weight_v16_summary.md`
- `output/e2r_round31_score_weight_v16/round31_case_candidate_matrix.csv`
- `output/e2r_round31_score_weight_v16/round31_green_guardrail_review.md`
- `output/e2r_round31_score_weight_v16/round31_regulated_risk_review.md`
- `output/e2r_round31_score_weight_v16/round31_ai_infra_split_review.md`
- `output/e2r_round31_score_weight_v16/round31_price_validation_plan.md`

## Coverage

- score target count: 8
- case candidate count: 32
- success / structural candidate count: 12
- 4C thesis-break case count: 6
- Green-possible target count: 5
- Watch-first target count: 3
- RedTeam-first target count: 0

## Main Calibration Changes

- Data-center REIT is Green-possible, but FFO/AFFO, tenant quality, occupancy, power/cooling/land, and funding cost are required gates.
- Waste treatment/recycling is Green-possible when permits, facilities, utilization, long-term processing contracts, and recurring FCF are source-backed.
- Dental/medical devices are Green-possible with export expansion, repeat procedures/consumables, approval stability, and OPM/ROE improvement.
- Regulated consumer products remain Watch-first because approval, sales bans, public-health litigation, and social backlash can flip the stage.
- Apparel and fast fashion are more conservative than K-food/K-beauty because inventory, markdown, IP litigation, and ultra-low-price competition are strong risks.
- Digital assets split stablecoin/STO infrastructure from NFT/theme exposure.
- AI data-center infrastructure must be split into power, cooling, real estate, PPA, and PCB axes.
- Value-up is execution, not policy label: cancellation, dividend, ROE/NAV, governance, and FCF are gates.

## Guardrails

- Case IDs and theme labels are not production candidate input.
- No production scoring, staging, or RedTeam thresholds changed.
- No stage dates, prices, FFO/AFFO, tenant terms, utilization, VBP impact, approval status, markdown rate, or transaction volume were invented.
- Stage 3-Green remains strict and must still require cross-evidence plus price-path validation.

## Verification

```bash
PYTHONPATH=src python -m unittest tests.test_round31_score_weight_v16 -v
PYTHONPATH=src python -m e2r.cli.build_round31_score_weight_report
```

The full suite is still expected to show the pre-existing unrelated `round_17.md` deletion failures until that deleted round document is restored or the old test is retired.

# Checkpoint 28A-24: Round 24 Score-Weight v0.9 Calibration

## Purpose

Round 24 was applied as calibration material only.

The change adds v0.9 score-weight hypotheses and case candidates for:

- RAIL_INFRASTRUCTURE
- CLOUD_AI_SOFTWARE_INFRA
- CRO_CLINICAL_SERVICE
- RETAIL_ECOMMERCE_LOGISTICS
- SOLAR_TARIFF_SUPPLYCHAIN
- INSURANCE_UNDERWRITING_CYCLE
- DIGITAL_HEALTHCARE_AI
- SECURITY_IDENTITY_DEEPFAKE
- BATTERY_RECYCLING_ESS_SHIFT
- SECURITIES_BROKERAGE_CYCLE

Production scoring, StageClassifier thresholds, RedTeam rules, and candidate generation were not changed.

## Outputs

- `src/e2r/sector/round24_score_weight_v09.py`
- `src/e2r/cli/build_round24_score_weight_report.py`
- `tests/test_round24_score_weight_v09.py`
- `data/e2r_case_library/cases_v06_round24.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round24_v09.csv`
- `output/e2r_round24_score_weight_v09/round24_score_weight_v09_summary.md`
- `output/e2r_round24_score_weight_v09/round24_case_candidate_matrix.csv`
- `output/e2r_round24_score_weight_v09/round24_green_guardrail_review.md`
- `output/e2r_round24_score_weight_v09/round24_risk_boundary_review.md`
- `output/e2r_round24_score_weight_v09/round24_price_validation_plan.md`

## Summary

- target_count: 10
- case_candidate_count: 40
- success_candidate_count: 14
- counterexample_or_risk_count: 26
- stage4c_case_count: 9
- green_possible_count: 4
- watch_yellow_first_count: 6
- production_scoring_changed: false
- case_records_are_candidate_generation_input: false

## Key Interpretation

Round 24 makes the risk boundary more explicit.

Example: a large rail contract can be Stage 2+ material only after signed contract, delivery schedule, margin visibility, OP revision, and financing-risk checks. A rail policy headline or reconstruction theme is only routing/event evidence.

Example: cloud/SaaS can be Green-possible, but only through recurring revenue, retention, OPM, and FCF. An AI feature announcement alone is like a signboard on a store: it tells us where to look, but it does not prove cash flow.

Example: security software may have structural demand, but a major outage is hard 4C-style thesis-break evidence. Recurring subscription revenue cannot hide operational trust failure.

## Green-Possible With Strict Gates

- RAIL_INFRASTRUCTURE
- CLOUD_AI_SOFTWARE_INFRA
- INSURANCE_UNDERWRITING_CYCLE
- SECURITY_IDENTITY_DEEPFAKE

## Watch-First / 4C-Sensitive

- CRO_CLINICAL_SERVICE
- RETAIL_ECOMMERCE_LOGISTICS
- SOLAR_TARIFF_SUPPLYCHAIN
- DIGITAL_HEALTHCARE_AI
- BATTERY_RECYCLING_ESS_SHIFT
- SECURITIES_BROKERAGE_CYCLE

## Guardrails

- Do not use Round 24 case IDs as candidate-generation input.
- Do not apply v0.9 weights to production scoring yet.
- Do not score policies, AI features, PoCs, revenue headlines, or theme labels without source-backed economics.
- Do not invent stage dates, prices, margins, retention, FCF, reimbursement, or contract values.
- Keep Stage 3-Green strict and cross-evidence based.

## Commands Run

```bash
PYTHONPATH=src python -m unittest tests.test_round24_score_weight_v09 -v
PYTHONPATH=src python -m compileall -q src/e2r/sector/round24_score_weight_v09.py src/e2r/cli/build_round24_score_weight_report.py tests/test_round24_score_weight_v09.py
PYTHONPATH=src python -m e2r.cli.build_round24_score_weight_report \
  --output-directory output/e2r_round24_score_weight_v09 \
  --cases data/e2r_case_library/cases_v06_round24.jsonl \
  --score-profiles data/sector_taxonomy/score_weight_profiles_round24_v09.csv
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Verification Result

- Round 24 unit tests passed.
- Compileall passed.
- Full repository test run still has an unrelated pre-existing blocker: `docs/round/round_17.md` is deleted in the working tree, so Round 17 tests cannot read their source document.

## Next Step

Continue the case-library loop: add more success/counterexample records, backfill price paths, run shadow score-price alignment, and only then consider production scoring changes.

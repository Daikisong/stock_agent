# Checkpoint 28A-27: Round 27 Score-Weight v1.2 Calibration

## Purpose

Round 27 was applied as calibration material only.

The change adds v1.2 score-weight hypotheses and case candidates for:

- GAME_CONTENT_IP
- MEDICAL_DEVICE_HEALTHCARE_EXPORT
- DIGITAL_HEALTHCARE_AI
- RETAIL_ECOMMERCE_LOGISTICS
- EDUCATION_SPECIALTY_SERVICES
- TELECOM_GRID_AI_NETWORK
- AI_DATA_CENTER_COOLING
- SECURITY_IDENTITY_DEEPFAKE
- CLOUD_AI_SOFTWARE_INFRA
- INSURANCE_UNDERWRITING_CYCLE

Production scoring, StageClassifier thresholds, RedTeam rules, and candidate generation were not changed.

## Outputs

- `src/e2r/sector/round27_score_weight_v12.py`
- `src/e2r/cli/build_round27_score_weight_report.py`
- `tests/test_round27_score_weight_v12.py`
- `data/e2r_case_library/cases_v09_round27.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round27_v12.csv`
- `output/e2r_round27_score_weight_v12/round27_score_weight_v12_summary.md`
- `output/e2r_round27_score_weight_v12/round27_case_candidate_matrix.csv`
- `output/e2r_round27_score_weight_v12/round27_green_guardrail_review.md`
- `output/e2r_round27_score_weight_v12/round27_false_success_boundary_review.md`
- `output/e2r_round27_score_weight_v12/round27_risk_boundary_review.md`
- `output/e2r_round27_score_weight_v12/round27_price_validation_plan.md`

## Summary

- target_count: 10
- case_candidate_count: 28
- success_candidate_count: 12
- counterexample_or_risk_count: 16
- stage4b_case_count: 0
- stage4c_case_count: 6
- green_possible_count: 5
- watch_yellow_first_count: 5
- production_scoring_changed: false
- case_records_are_candidate_generation_input: false

## Key Interpretation

Round 27 sharpens false-success boundaries.

Example: a game can have large downloads, but downloads alone do not prove E2R. A stronger game/IP case needs monetization, OP/EPS confirmation, region/platform diversification, and low regulation or data-security risk.

Example: medical AI can have strong paper performance, but paper performance alone is not enough. It needs external validation plus approval, hospital adoption, reimbursement or paid usage, and actual revenue conversion.

Example: retail/e-commerce scale can look strong, but supplier pressure, data breach, inventory, logistics cost, or weak FCF can make it a counterexample.

## Green-Possible With Strict Gates

- MEDICAL_DEVICE_HEALTHCARE_EXPORT
- AI_DATA_CENTER_COOLING
- SECURITY_IDENTITY_DEEPFAKE
- CLOUD_AI_SOFTWARE_INFRA
- INSURANCE_UNDERWRITING_CYCLE

## Watch-First / 4C-Sensitive

- GAME_CONTENT_IP
- DIGITAL_HEALTHCARE_AI
- RETAIL_ECOMMERCE_LOGISTICS
- EDUCATION_SPECIALTY_SERVICES
- TELECOM_GRID_AI_NETWORK

## Guardrails

- Do not use Round 27 case IDs as candidate-generation input.
- Do not apply v1.2 weights to production scoring yet.
- Do not score downloads, store counts, papers, policies, PoCs, or traffic without source-backed economics.
- Do not invent stage dates, prices, monetization, reimbursement, OPM, FCF, retention, or approval status.
- Keep Stage 3-Green strict and cross-evidence based.

## Commands Run

```bash
PYTHONPATH=src python -m unittest tests.test_round27_score_weight_v12 -v
PYTHONPATH=src python -m compileall -q src/e2r/sector/round27_score_weight_v12.py src/e2r/cli/build_round27_score_weight_report.py tests/test_round27_score_weight_v12.py
PYTHONPATH=src python -m e2r.cli.build_round27_score_weight_report \
  --output-directory output/e2r_round27_score_weight_v12 \
  --cases data/e2r_case_library/cases_v09_round27.jsonl \
  --score-profiles data/sector_taxonomy/score_weight_profiles_round27_v12.csv
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Verification Result

- Round 27 unit tests passed.
- Compileall passed.
- Full repository test run still has an unrelated pre-existing blocker: `docs/round/round_17.md` is deleted in the working tree, so Round 17 tests cannot read their source document.

## Next Step

1. Backfill tradable case price paths.
2. Verify score-price alignment for game/IP, medical device, medical AI, retail/e-commerce, education, and telecom/grid cases.
3. Keep game/IP, medical AI, retail/e-commerce, education, and telecom/grid Watch-first until price-path and source evidence support stricter calibration.
4. Do not apply v1.2 weights to production scoring before shadow validation.

# Checkpoint 28A-25: Round 25 Score-Weight v1.0 Calibration

## Purpose

Round 25 was applied as calibration material only.

The change adds v1.0 score-weight hypotheses and case candidates for:

- AI_DATA_CENTER_COOLING
- SECURITY_IDENTITY_DEEPFAKE
- CRO_CLINICAL_SERVICE
- SOLAR_TARIFF_SUPPLYCHAIN
- RETAIL_ECOMMERCE_LOGISTICS
- INSURANCE_UNDERWRITING_CYCLE
- DIGITAL_HEALTHCARE_AI
- BATTERY_RECYCLING_ESS_SHIFT
- SECURITIES_BROKERAGE_CYCLE
- MEMORY_HBM_CAPACITY

Production scoring, StageClassifier thresholds, RedTeam rules, and candidate generation were not changed.

## Outputs

- `src/e2r/sector/round25_score_weight_v10.py`
- `src/e2r/cli/build_round25_score_weight_report.py`
- `tests/test_round25_score_weight_v10.py`
- `data/e2r_case_library/cases_v07_round25.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round25_v10.csv`
- `output/e2r_round25_score_weight_v10/round25_score_weight_v10_summary.md`
- `output/e2r_round25_score_weight_v10/round25_case_candidate_matrix.csv`
- `output/e2r_round25_score_weight_v10/round25_green_guardrail_review.md`
- `output/e2r_round25_score_weight_v10/round25_stage4b_watch_review.md`
- `output/e2r_round25_score_weight_v10/round25_risk_boundary_review.md`
- `output/e2r_round25_score_weight_v10/round25_price_validation_plan.md`

## Summary

- target_count: 10
- case_candidate_count: 40
- success_candidate_count: 15
- counterexample_or_risk_count: 25
- stage4b_case_count: 1
- stage4c_case_count: 9
- green_possible_count: 4
- watch_yellow_first_count: 6
- production_scoring_changed: false
- case_records_are_candidate_generation_input: false

## Key Interpretation

Round 25 promotes AI data-center cooling into a Green-possible calibration target, but only with strict evidence.

Example: “liquid cooling” as a keyword is just a search clue. It is not score evidence. A stronger case needs direct data-center CAPEX linkage, confirmed order or delivery, cooling bottleneck evidence, service revenue, and OP/EPS revision.

Example: cybersecurity can have recurring subscription revenue, but a major outage or legal trust break is hard 4C-style evidence. Recurring revenue does not excuse operational trust failure.

Example: HBM can be Green, but a successful rerating must turn on 4B-watch diagnostics after crowding, market-cap saturation, customer price resistance, or capex expansion news.

## Green-Possible With Strict Gates

- AI_DATA_CENTER_COOLING
- SECURITY_IDENTITY_DEEPFAKE
- INSURANCE_UNDERWRITING_CYCLE
- MEMORY_HBM_CAPACITY

## Watch-First / 4C-Sensitive

- CRO_CLINICAL_SERVICE
- SOLAR_TARIFF_SUPPLYCHAIN
- RETAIL_ECOMMERCE_LOGISTICS
- DIGITAL_HEALTHCARE_AI
- BATTERY_RECYCLING_ESS_SHIFT
- SECURITIES_BROKERAGE_CYCLE

## Guardrails

- Do not use Round 25 case IDs as candidate-generation input.
- Do not apply v1.0 weights to production scoring yet.
- Do not score policies, AI features, PoCs, revenue headlines, or theme labels without source-backed economics.
- Do not invent stage dates, prices, margins, retention, FCF, reimbursement, or contract values.
- Keep Stage 3-Green strict and cross-evidence based.

## Commands Run

```bash
PYTHONPATH=src python -m unittest tests.test_round25_score_weight_v10 -v
PYTHONPATH=src python -m compileall -q src/e2r/sector/round25_score_weight_v10.py src/e2r/cli/build_round25_score_weight_report.py tests/test_round25_score_weight_v10.py
PYTHONPATH=src python -m e2r.cli.build_round25_score_weight_report \
  --output-directory output/e2r_round25_score_weight_v10 \
  --cases data/e2r_case_library/cases_v07_round25.jsonl \
  --score-profiles data/sector_taxonomy/score_weight_profiles_round25_v10.csv
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Verification Result

- Round 25 unit tests passed.
- Compileall passed.
- Full repository test run still has an unrelated pre-existing blocker: `docs/round/round_17.md` is deleted in the working tree, so Round 17 tests cannot read their source document.

## Next Step

The next phase should shift from adding more hypotheses to validation:

1. Backfill price paths for tradable cases.
2. Compute MFE, MAE, drawdown, and below-entry flags.
3. Run shadow score-price alignment.
4. Recalibrate archetypes that fail price-path validation.

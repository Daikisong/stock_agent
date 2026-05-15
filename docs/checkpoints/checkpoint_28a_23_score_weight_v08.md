# Checkpoint 28A-23: Round 23 Score-Weight v0.8 Calibration

## Purpose

Round 23 was applied as calibration material only.

The change expands thin archetype coverage and adds v0.8 score-weight hypotheses for:

- DIGITAL_HEALTHCARE_AI
- TELECOM_5G_6G_AI_NETWORK
- MEDIA_AD_CONTENT_CYCLE
- SERVICE_KIOSK_AUTOMATION
- SMART_FARM_AGRI_TECH
- HOME_LIVING_APPLIANCE
- CONSUMER_REGULATED_PRODUCT
- MEMORY_HBM_CAPACITY
- AI_DATA_CENTER_INFRASTRUCTURE

Production scoring, StageClassifier thresholds, RedTeam rules, and candidate generation were not changed.

## Outputs

- `src/e2r/sector/round23_score_weight_v08.py`
- `src/e2r/cli/build_round23_score_weight_report.py`
- `tests/test_round23_score_weight_v08.py`
- `data/e2r_case_library/cases_v05_round23.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round23_v08.csv`
- `output/e2r_round23_score_weight_v08/round23_score_weight_v08_summary.md`
- `output/e2r_round23_score_weight_v08/round23_case_candidate_matrix.csv`
- `output/e2r_round23_score_weight_v08/round23_green_guardrail_review.md`
- `output/e2r_round23_score_weight_v08/round23_price_validation_plan.md`
- `output/e2r_round23_score_weight_v08/round23_stage4b_watch_review.md`

## Summary

- target_count: 9
- case_candidate_count: 28
- success_candidate_count: 12
- counterexample_or_risk_count: 16
- green_possible_count: 2
- watch_yellow_first_count: 7
- production_scoring_changed: false
- case_records_are_candidate_generation_input: false

## Key Interpretation

Round 23 is mostly a guardrail round.

Example: medical AI can have strong research papers, but paper evidence is not enough. It needs clearance, hospital adoption, reimbursement or paid usage, external validation, and revenue or operating profit conversion before it can be considered for higher conviction.

Example: 6G policy headlines can help route search queries, but they are not revenue evidence. Without equipment orders, IDC revenue, ARPU impact, or confirmed capex conversion, the case stays Watch/Yellow-first.

Example: HBM and AI data-center infrastructure remain Green-possible archetypes, but after a large rerating they need stronger 4B-watch diagnostics. A price-only warning remains `price_only_4b_watch`, not full evidence-based 4B.

## Green Guardrails

- Do not use Round 23 case IDs as candidate-generation input.
- Do not apply v0.8 weights to production scoring yet.
- Do not score papers, policy plans, PoCs, or theme labels without revenue, paid usage, order, or margin evidence.
- Do not invent stage dates, prices, reimbursement, paid usage, ARR, EPS, FCF, or contract values.
- Keep Stage 3-Green strict and cross-evidence based.

## Commands Run

```bash
PYTHONPATH=src python -m unittest tests.test_round23_score_weight_v08 -v
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m e2r.cli.build_round23_score_weight_report \
  --output-directory output/e2r_round23_score_weight_v08 \
  --cases data/e2r_case_library/cases_v05_round23.jsonl \
  --score-profiles data/sector_taxonomy/score_weight_profiles_round23_v08.csv
```

## Verification Result

- Round 23 unit tests passed.
- Compileall passed.
- Full repository test run still has an unrelated pre-existing blocker: `docs/round/round_17.md` is deleted in the working tree, so Round 17 tests cannot read their source document.

## Next Step

Round 24+ should continue expanding case coverage and price-path validation before any production scoring change.

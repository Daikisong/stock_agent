# Checkpoint 28A-21: cases_v04 Expansion and v0.6 Guardrail Pack

## Purpose

Round 21 extends the calibration library, not production scoring.

The analyst note in `docs/round/round_21.md` adds thin archetype candidates where the earlier case library was still sparse:

- `RAIL_INFRASTRUCTURE`
- `AI_DATA_CENTER_COOLING`
- `WASTE_RECYCLING_ENVIRONMENT`
- `CLOUD_AI_SOFTWARE_INFRA`
- `SECURITY_IDENTITY_DEEPFAKE`
- `CRO_CLINICAL_SERVICE`
- `APPAREL_BRAND_OEM`
- `BUILDING_MATERIALS_REIT`
- `CDMO_HEALTHCARE_CONTRACT`
- `RARE_METALS_STRATEGIC_MATERIALS`

This checkpoint records those as case-mining and shadow score-weight hypotheses only.

## Files Added

- `src/e2r/sector/round21_cases_v04_expansion.py`
- `src/e2r/cli/build_round21_case_expansion_report.py`
- `tests/test_round21_cases_v04_expansion.py`
- `data/e2r_case_library/cases_v04_round21.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round21_v06.csv`
- `output/e2r_round21_cases_v04/round21_cases_v04_summary.md`
- `output/e2r_round21_cases_v04/round21_case_candidate_matrix.csv`
- `output/e2r_round21_cases_v04/round21_green_guardrail_review.md`
- `output/e2r_round21_cases_v04/round21_price_validation_plan.md`

## Summary

- target_count: 10
- case_candidate_count: 39
- success_candidate_count: 15
- counterexample_or_risk_count: 24
- green_possible_count: 4
- watch_yellow_first_count: 6
- production_scoring_changed: false
- case_records_are_candidate_generation_input: false

## Interpretation

Round 21 makes the calibration pack richer. It does not make Stage 3-Green easier.

Easy example:

- `현대로템 모로코 철도 수주` is now a case-mining candidate.
- It still has no filled stage price, peak price, MFE/MAE, or validated Stage 3 date.
- Therefore it is useful for future validation, but it is not allowed to drive production scoring.

Another example:

- `고려아연 공개매수` is stored as `event_premium`.
- A tender-offer premium is not treated as structural FCF rerating unless separate FCF/governance evidence is proven.

## Guardrails

- Do not use `cases_v04_round21.jsonl` as candidate-generation input.
- Do not use case IDs or theme tags as scoring evidence.
- Do not invent stage dates, prices, utilization, ARR, FCF, margins, or contract size.
- Do not apply the v0.6 score weights to production scoring yet.

## Commands Run

```bash
PYTHONPATH=src python -m unittest tests.test_round21_cases_v04_expansion -v
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m e2r.cli.build_round21_case_expansion_report \
  --output-directory output/e2r_round21_cases_v04 \
  --cases data/e2r_case_library/cases_v04_round21.jsonl \
  --score-profiles data/sector_taxonomy/score_weight_profiles_round21_v06.csv
```

## Result

Round 21 is now represented as a report-only case expansion and score-weight hypothesis pack. The next step is price-path backfill and shadow score-price validation, not production scoring changes.

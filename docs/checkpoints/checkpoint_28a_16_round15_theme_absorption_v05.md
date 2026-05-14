# Checkpoint 28A-16: Round 15 Theme Absorption v0.5

## Summary

Round 15 was converted into report-only calibration material.

It extends Round 14 by absorbing missing or under-specified theme groups and connecting each group to:

- score-weight hypothesis
- must-have evidence
- Green guardrails
- 4B / 4C risk conditions
- success candidates
- counterexamples

## Key Principle

Theme names are not scoring logic.

Example:

`폐배터리` is a useful search tag, but it does not create a candidate by itself. The system needs collection volume, utilization, customer demand, metal recovery economics, and FCF evidence.

## Added

- `src/e2r/sector/round15_theme_absorption_v05.py`
- `src/e2r/cli/build_round15_theme_absorption_report.py`
- `tests/test_round15_theme_absorption_v05.py`
- `docs/e2r_theme_absorption_round15.md`
- Round 15 CSV outputs under `data/sector_taxonomy/`
- Round 15 report outputs under `output/e2r_round15_theme_absorption_v05/`

## Covered Families

- Waste / recycling / waste-to-energy
- Refining / chemical / steel spread
- Retail / e-commerce / logistics
- Insurance / financial value-up
- Digital asset / tokenization / payment
- Hydrogen / renewables
- Battery recycling / ESS
- Tire / auto components
- Infectious diagnostics / event demand
- Speculative science
- Agri / livestock / food commodity

## Guardrails

- `production_scoring_changed: false`
- `theme_tags_are_score_input: false`
- StageClassifier thresholds unchanged
- Green remains strict
- One-off EPS spikes and cheap cyclical rebounds are not treated as structural E2R

## Verification

- Round 15 unit tests added.
- Production scoring modules are tested to ensure they do not import the Round 15 calibration module.
- Full test suite passed after implementation.

## Next Step

Convert the Round 15 success/counterexample plan into `cases_v03.jsonl`, then backfill price paths and run score-price alignment before any shadow scoring.

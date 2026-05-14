# Checkpoint 28A-8: Round 6 Missing-Sector Correction

## Summary

Round 6 was applied as calibration material only. Production scoring and
StageClassifier thresholds were not changed.

Round 6 adds a six-overlay correction layer on top of the Round 5 large-sector
framework:

```text
Round 5 large sector -> Round 6 overlay -> E2R archetype -> price-path validation
```

Easy example:

```text
AI data-center CAPEX can move transformers, grid, cooling, PCB, memory, and IDC together.
If price moves first without orders, delivery, or EPS revision, it is not structural Green.
```

## Implemented Files

- `src/e2r/sector/round6_missing_sector_correction.py`
- `src/e2r/cli/build_round6_missing_sector_report.py`
- `tests/test_round6_missing_sector_correction.py`
- `docs/e2r_missing_sector_correction_round6.md`
- `output/e2r_round6_missing_sector_correction/round6_missing_sector_framework.md`
- `output/e2r_round6_missing_sector_correction/round6_archetype_overlay_matrix.csv`
- `output/e2r_round6_missing_sector_correction/round6_price_path_validation_contract.md`
- `output/e2r_round6_missing_sector_correction/round6_case_coverage_by_overlay.csv`
- `output/e2r_round6_missing_sector_correction/round6_next_case_backfill_plan.md`

## Six Overlays

- `AI_POWER_INFRA`: AI/전력/인프라
- `NATIONAL_STRATEGY_POLICY`: 정책/국가전략
- `CAPITAL_ALLOCATION_VALUEUP`: 자본배분/밸류업
- `CYCLE_MACRO_CREDIT`: 경기/사이클
- `THEME_TECH_EXPECTATION`: 테마/기술 기대
- `RECURRING_EXPORT_BRAND`: 반복수출/브랜드

## Schema Updates

`PriceValidation` now also supports:

- `mfe_30d`
- `mfe_2y`
- `mae_30d`
- `mae_2y`

These fields make price-path validation closer to the Round 6 contract:

```text
Stage 2/3 signal -> MFE/MAE path -> time to +50%/+100% -> 4B/4C timing
```

## Current Output

The current case pack still needs price-path backfill across overlays. That is
expected. Round 6’s purpose is to make that missing work visible before score
weights are changed.

## What Not To Change

- Do not lower Stage 3-Green thresholds.
- Do not use overlay labels as candidate-generation input.
- Do not treat price-only rallies as EPS/FCF evidence.
- Do not apply score weights until price-path validation is filled.

## Verification

Commands run:

```bash
PYTHONPATH=src python -m unittest tests.test_round6_missing_sector_correction -v
PYTHONPATH=src python -m e2r.cli.build_round6_missing_sector_report --cases data/e2r_case_library/cases_v02.jsonl --output-directory output/e2r_round6_missing_sector_correction
```

Full test run was executed after the patch before commit.

# Checkpoint 28A Round 42: R2 AI / Semiconductor / Electronics

## Summary

Round 42 was converted into a calibration-only R2 case pack for `AI_SEMICONDUCTOR_ELECTRONICS`.

This patch does not change production scoring, staging, RedTeam, or candidate generation. It only records the research matrix as:

- R2 target sub-archetypes
- shadow score-weight drafts
- stage-date guidance
- case records
- price-validation fields
- Green/RedTeam guardrails

Simple example: `HBM demand + capacity constraint + multi-year EPS revision` can be a Green-capable evidence pattern later, but `AI chip keyword + no revenue` remains Watch/Red. The case pack stores that distinction without changing live scoring.

## Files Added

- `src/e2r/sector/round42_r2_ai_semiconductor.py`
- `src/e2r/cli/build_round42_r2_report.py`
- `tests/test_round42_r2_ai_semiconductor.py`
- `data/e2r_case_library/cases_r2_round42.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round42_r2_v1.csv`
- `output/e2r_round42_r2_ai_semiconductor/round42_r2_ai_semiconductor_summary.md`
- `output/e2r_round42_r2_ai_semiconductor/round42_r2_case_matrix.csv`
- `output/e2r_round42_r2_ai_semiconductor/round42_r2_stage_date_plan.csv`
- `output/e2r_round42_r2_ai_semiconductor/round42_r2_green_guardrails.md`
- `output/e2r_round42_r2_ai_semiconductor/round42_r2_price_validation_plan.md`
- `output/e2r_round42_r2_ai_semiconductor/round42_r2_price_fields.csv`

## Coverage

- target_count: 18
- case_candidate_count: 18
- structural_success_count: 1
- success_candidate_count: 8
- cyclical_success_count: 1
- overheat_count: 1
- failed_rerating_count: 3
- stage4b_case_count: 2
- stage4c_case_count: 2
- green_possible_count: 4
- watch_yellow_first_count: 13
- redteam_first_count: 1

## Key Guardrails

- HBM is not the same as every AI semiconductor theme.
- Commodity DRAM/NAND recovery is Watch-to-Green, not automatic Green.
- Equipment/materials/PCB need order-to-revenue and margin conversion.
- Neocloud requires debt, FCF, GPU depreciation, and customer concentration checks.
- Auditor resignation, filing delay, internal-control weakness, and trust issues are hard RedTeam evidence.
- Case records are calibration/evaluation material only and are not production candidate-generation input.

## Verification

Commands run:

```bash
PYTHONPATH=src python -m unittest tests/test_round42_r2_ai_semiconductor.py -v
PYTHONPATH=src python -m e2r.cli.build_round42_r2_report
```

Result:

- Round 42 tests passed.
- Reports and JSONL/CSV outputs were generated.
- Production modules are tested to avoid importing the Round 42 case pack.

Full-suite note: the broader repo currently has unrelated round-file deletions in the working tree, including `docs/round/round_17.md`, which is known to break existing round17 tests until restored or intentionally handled.

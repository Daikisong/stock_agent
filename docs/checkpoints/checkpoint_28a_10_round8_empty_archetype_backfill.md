# Checkpoint 28A-10: Round 8 Empty Archetype Backfill

## Summary

Round 8 was applied as calibration/report material only. Production scoring and
StageClassifier thresholds were not changed.

Round 8 adds a backfill plan for empty or thin archetypes:

```text
case record
-> score_price_alignment
-> rerating_result
-> price_pattern
-> Stage 4B/4C explanation
```

쉬운 예시:

```text
해운은 EPS와 주가가 폭발해도 운임 정상화로 꺾이면 structural Green이 아니라 cycle_boom_bust다.
```

## Implemented Files

- `src/e2r/sector/round8_empty_archetype_backfill.py`
- `src/e2r/cli/build_round8_empty_archetype_report.py`
- `tests/test_round8_empty_archetype_backfill.py`
- `docs/e2r_empty_archetype_backfill_round8.md`
- `output/e2r_round8_empty_archetype_backfill/round8_empty_archetype_backfill_framework.md`
- `output/e2r_round8_empty_archetype_backfill/round8_backfill_target_matrix.csv`
- `output/e2r_round8_empty_archetype_backfill/round8_case_gap_report.md`
- `output/e2r_round8_empty_archetype_backfill/round8_price_pattern_contract.md`
- `output/e2r_round8_empty_archetype_backfill/round8_next_case_record_plan.md`

## Round 8 Targets

- `TURNAROUND_COST_RESTRUCTURING`
- `COMMODITY_SPREAD`
- `AUTO_MOBILITY_COMPLETED_VEHICLE`
- `AUTO_MOBILITY_COMPONENTS`
- `FINANCIAL_SPREAD_BALANCE_SHEET`
- `VALUE_UP_SHAREHOLDER_RETURN`
- `CDMO_HEALTHCARE_CONTRACT`
- `BIOTECH_ROYALTY_COMMERCIALIZATION`
- `PLATFORM_SOFTWARE_INTERNET`
- `SHIPPING_FREIGHT_CYCLE`
- `NUCLEAR_SMR_GRID_POLICY`
- `AI_DATA_CENTER_INFRASTRUCTURE`
- `MEMORY_HBM_CAPACITY`

## Key Additions

- `policy_contract_delay` price pattern is documented for nuclear/policy cases.
- Turnaround requires durable OPM/FCF, not one-time cost cuts.
- Commodity and shipping stay RedTeam/cycle guarded.
- Financial/value-up requires ROE/PBR/capital ratio/shareholder-return execution.
- Memory/HBM now explicitly pairs Stage 3 success with 4B-watch after a large rerating.

## What Not To Change

- Do not lower Stage 3-Green thresholds.
- Do not use case records as production candidate-generation input.
- Do not treat event premium, reopening cycle, or credit relief as true rerating.
- Do not apply score weights until case records and price paths are filled.

## Verification

Commands run:

```bash
PYTHONPATH=src python -m unittest tests.test_round8_empty_archetype_backfill -v
PYTHONPATH=src python -m e2r.cli.build_round8_empty_archetype_report --cases data/e2r_case_library/cases_v02.jsonl --output-directory output/e2r_round8_empty_archetype_backfill
```

Full test run was executed after the patch before commit.

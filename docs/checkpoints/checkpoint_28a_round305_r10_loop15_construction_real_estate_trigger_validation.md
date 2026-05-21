# Checkpoint 28A Round 305 R10 Loop 15 Construction / Real Estate / Building Materials Trigger Validation

## Scope

`docs/round/round_305.md` 내용을 calibration/evaluation 전용 케이스 팩으로 반영했다.

쉬운 예: `대형 EPC 수주`는 좋은 Stage2 신호다. 하지만 수주가 실제 이익과 현금으로 바뀌는지 보려면 margin, cash collection, cost overrun을 따로 닫아야 한다.

## Commands Run

```bash
PYTHONPATH=src python -m unittest tests.test_round305_r10_loop15_construction_real_estate_trigger_validation -v
PYTHONPATH=src python -m compileall -q src/e2r/sector/archetypes.py src/e2r/sector/round305_r10_loop15_construction_real_estate_trigger_validation.py src/e2r/cli/build_round305_r10_loop15_report.py tests/test_round305_r10_loop15_construction_real_estate_trigger_validation.py
PYTHONPATH=src python -m e2r.cli.build_round305_r10_loop15_report
```

## Outputs

- `data/e2r_case_library/cases_r10_loop15_round233.jsonl`
- `data/e2r_trigger_calibration/triggers_r10_loop15_round233.jsonl`
- `data/sector_taxonomy/round305_r10_loop15_construction_real_estate_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round233_r10_loop15_v1.csv`
- `output/e2r_round305_r10_loop15_construction_real_estate_trigger_validation/`

## Summary

- case candidates: 8
- trigger records: 9
- Stage2-Actionable candidates: 2
- Stage2 policy/relief cases: 3
- Stage3-Yellow candidates: 3
- Stage3-Green confirmed: 0
- Stage4B-watch: 5
- Stage4C-watch: 4
- hard 4C: 1
- failed rerating: 1
- production scoring changed: false
- candidate generation input: false
- shadow weight only: true

## Added Canonical Archetypes

- `OVERSEAS_EPC_MEGA_ORDER_STAGE2_ACTIONABLE`
- `NUCLEAR_CONSTRUCTION_EXPORT_STAGE2_WITH_LEGAL_4B`
- `REAL_ESTATE_PF_RESTRUCTURING_4C_WATCH`
- `HOUSING_SUPPLY_RECONSTRUCTION_STAGE2_POLICY`
- `CONSTRUCTION_QUALITY_SAFETY_HARD_4C`
- `BUILDER_LIQUIDITY_SUPPORT_FALSE_POSITIVE_WATCH`

Existing archetype reused:

- `BUILDING_MATERIAL_WEAK_DEMAND_FAILED_RERATING`

## Core Findings

- Samsung E&A / Fadhili is the cleanest Stage2-Actionable case: large signed EPC contract, strong relative return, and concrete completion context.
- GS E&C / Fadhili is Stage2 evidence only because company-specific contract value, price reaction, margin, and PF/quality overlay remain missing.
- Czech nuclear basket is Stage2-Actionable with legal 4B overlay. Preferred bidder and sector rally are strong, but legal clearance and work allocation are required before Yellow/Green.
- Taeyoung / PF restructuring is 4C-watch with policy relief. Liquidity support is not earnings recovery.
- Seoul housing supply/reconstruction is Stage2 policy. Green requires permits, starts, presales, unsold inventory absorption, and PF repayment.
- HDC Gwangju collapse is a hard construction-quality 4C reference.
- Hyundai Steel rebar weak demand is a building-material failed-rerating reference.
- Builder liquidity support is false-positive watch; survival support must not be scored as margin recovery.

## What Not To Change

- Do not apply Round 305 shadow weights to production scoring yet.
- Do not use Round 305 case records as candidate-generation input.
- Do not treat construction order, policy, PF support, or housing supply headlines as Stage3-Green.
- Do not invent MFE/MAE or adjusted OHLC where full price history is unavailable.

## Next Step

Backfill adjusted OHLC and source snapshots for Round 305 trigger dates. Then compare shadow scores only, especially for EPC margin/cash conversion, nuclear legal clearance, housing starts/presales, PF cleanup, and building-material spread recovery.

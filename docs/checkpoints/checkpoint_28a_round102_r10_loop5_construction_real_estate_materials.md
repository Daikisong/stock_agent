# Checkpoint 28A Round 102 R10 Loop 5: Construction / Real Estate / Building Materials

## Purpose

Round 102 expands the R10 construction, real-estate, REIT, data-center real-asset, cold-chain, and building-materials calibration pack.

This is still calibration and evaluation material only. It does not change production scoring, staging, RedTeam, or candidate generation.

Simple example: a data-center REIT IPO can be a useful Stage 1 signal. It is not Stage 3 evidence until acquired assets, binding tenant leases, NOI/AFFO, power, water, and dividend coverage are source-backed.

## Implemented

- Added `src/e2r/sector/round102_r10_loop5_construction_real_estate_materials.py`.
- Added `src/e2r/cli/build_round102_r10_loop5_report.py`.
- Added `tests/test_round102_r10_loop5_construction_real_estate_materials.py`.
- Added Round 102 output files under `output/e2r_round102_r10_loop5_construction_real_estate_materials/`.
- Added case records to `data/e2r_case_library/cases_r10_loop5_round102.jsonl`.
- Added score profiles to `data/sector_taxonomy/score_weight_profiles_round102_r10_loop5_v5.csv`.

## New Or Expanded Archetypes

- `PF_SYNDICATED_LOAN_SOFT_LANDING`
- `AI_POWER_DATA_CENTER_CAMPUS`
- `DATA_CENTER_LOCAL_MORATORIUM_OVERLAY`
- `LOW_CARBON_CEMENT_PREMIUM`
- `BUILDING_PRODUCTS_MNA_SHIFT`
- `DISCLOSURE_CONFIDENCE_CAP`

## Counts

- Score targets: 25
- Case candidates: 24
- Success candidates: 5
- Event-premium cases: 5
- Failed-rerating cases: 1
- Stage 4B-watch cases: 13
- Stage 4C cases: 7
- Green-possible targets: 5
- Watch/Yellow-first targets: 8
- RedTeam-first targets: 12
- Gate-only targets: 7

## Guardrails

- PF policy support is not recovery until refinancing, PF exposure decline, and cash conversion are visible.
- Data-center power-campus narratives stay Watch without tenant, power delivery, permitting, financing, and revenue.
- Local moratorium and zoning pause can block real-asset promotion even when AI demand is real.
- Low-carbon cement needs durable green premium and FCF beyond CCS/pre-sale headlines.
- Building-products M&A needs accretion, synergy, margin, FCF, and leverage validation.
- Contract, tenant, NOI/AFFO, PF detail, or parser-confidence gaps trigger a Stage 3 confidence cap.

## Commands

```bash
PYTHONPATH=src python -m e2r.cli.build_round102_r10_loop5_report
PYTHONPATH=src python -m unittest tests.test_round102_r10_loop5_construction_real_estate_materials -v
```

## Verification Result

- Round 102 targeted tests passed.
- Production scoring modules are guarded from importing the Round 102 pack.
- Generated case records keep price fields unfilled where historical price data is not backfilled.

# Checkpoint 28A Round 50 - R10 Construction / Real Estate / Building Materials

Round 50 reflects `docs/round/round_50.md` as calibration data, not production scoring.

## What Changed

- Added R10 canonical archetypes:
  - `REIT_DEVELOPMENT_TRUST`
  - `BUILDING_MATERIALS_CYCLE`
  - `DATA_CENTER_REIT_INFRASTRUCTURE`
  - `COLD_CHAIN_REIT_LOGISTICS`
  - `INFRA_RECONSTRUCTION_POLICY`
  - `DISASTER_REBUILD_EVENT`
  - `COMMERCIAL_REAL_ESTATE_CREDIT`
  - `RESIDENTIAL_HOUSING_CYCLE`
  - `AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT`
- Added `src/e2r/sector/round50_r10_construction_real_estate_materials.py`.
- Added CLI:
  - `PYTHONPATH=src python -m e2r.cli.build_round50_r10_report`
- Generated:
  - `data/e2r_case_library/cases_r10_round50.jsonl`
  - `data/sector_taxonomy/score_weight_profiles_round50_r10_v1.csv`
  - `output/e2r_round50_r10_construction_real_estate_materials/`

## Interpretation

R10 is Green-restricted and RedTeam-first.

Simple example:

- A builder can rally on a government PF support package.
- That is `Stage 1 relief`, not structural success.
- It can only improve after evidence such as refinancing success, lower unsold inventory, cash-flow recovery, and stable construction cost ratio.

For REIT and real-asset cases, asset cash flow comes first:

- occupancy
- NOI/AFFO
- dividend coverage
- LTV
- funding cost
- tenant quality

For AI data-center real estate, the AI label is not enough. Green needs actual assets, hyperscale tenant contracts, power/cooling/water availability, and AFFO visibility.

## Case Coverage

- target_count: 10
- case_candidate_count: 12
- success_candidate_count: 3
- event_premium_count: 3
- one_off_count: 1
- stage4b_case_count: 1
- stage4c_case_count: 3

Priority cases include:

- `korea_pf_delinquency_restructuring_case`
- `korea_builder_support_relief_case`
- `blackstone_mortgage_trust_dividend_cut_case`
- `blackstone_data_center_reit_flat_debut_case`
- `ntt_dc_reit_tepid_debut_case`
- `fermi_ai_data_center_reit_case`
- `lineage_cold_storage_reit_ipo_case`
- `heidelberg_materials_price_cost_case`
- `cemex_demand_slowdown_price_offset_case`
- `ukraine_reconstruction_event_watch_case`
- `neom_city_event_watch_case`
- `disaster_rebuild_materials_event_case`

## Guardrails

- Do not apply R10 v1.0 weights to production scoring yet.
- Do not use case records as candidate-generation input.
- Do not treat PF support, rate cuts, asset value, dividend yield, reconstruction policy, or AI data-center labels as Green evidence by itself.
- Do not invent PF exposure, unsold inventory, NOI/AFFO, dividend coverage, LTV, tenant, power, or price-path fields.

## Verification

Commands run:

```bash
PYTHONPATH=src python -m e2r.cli.build_round50_r10_report
PYTHONPATH=src python -m unittest tests.test_round50_r10_construction_real_estate_materials -v
```

Result:

- Round 50 CLI generated expected reports.
- Round 50 tests passed.

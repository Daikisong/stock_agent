# Checkpoint 28A Round 122 R3 Loop 7 Battery / EV / Green-Energy

## Scope

Round 122 updates the R3 battery, EV, ESS, recycling, solar, wind, and green-energy calibration pack.

This is still calibration/evaluation material only. It does not change production scoring, StageClassifier thresholds, RedTeam rules, or candidate generation.

## What Changed

- Added `src/e2r/sector/round122_r3_loop7_battery_ev_green.py`.
- Added `src/e2r/cli/build_round122_r3_loop7_report.py`.
- Added Round-122 tests in `tests/test_round122_r3_loop7_battery_ev_green.py`.
- Generated case records:
  - `data/e2r_case_library/cases_r3_loop7_round122.jsonl`
- Generated score profile:
  - `data/sector_taxonomy/score_weight_profiles_round122_r3_loop7_v7.csv`
- Generated Round-122 reports under:
  - `output/e2r_round122_r3_loop7_battery_ev_green/`

## Main Interpretation

R3 Loop 7 separates Stage 2 visibility from Stage 3 operating confirmation.

Simple example:

- `LGES-Tesla Megapack 3` has customer, use case, contract value, contract duration, Lansing production, and 2027 production timing. That supports Stage 2 visibility.
- It is not Stage 3-Green until production ramp, utilization, ESS OPM, FCF, and EPS revision are visible.

## Base Score Table

Round 122 records seven calibration score axes:

- EPS/FCF and OPM transition: 24
- Contract visibility: 22
- Demand durability / structural change: 16
- Market mispricing / rerating gap: 10
- Valuation room / 4B runway: 8
- CAPA utilization / capital efficiency / FCF stability: 10
- Safety / regulatory / disclosure confidence: 10

These weights are report material only and are not applied to live scoring.

## Stage Caps

- Narrative-only EV/ESS/recycling/solid-state/solar/wind/hydrogen remains capped at Stage 1.
- Contract/customer/GWh/license/production-date evidence can support Stage 2.
- Stage 3 requires operating confirmation: revenue recognition, ESS OPM, utilization, FCF, EPS revision, and price path.
- Narrative price movement ahead of operating proof is 4B-watch.
- Contract cancellation, expected revenue loss, idle plant, customs/UFLPA, project impairment, BESS/EV fire, and SOH opacity are 4C/RedTeam gates.

## Price Alignment Findings

The new `round122_r3_loop7_score_stage_price_alignment` report records 12 cases.

Key examples:

- `tesla_lges_megapack3_lansing_case`: Stage 2 visibility, but Stage 3 cap remains.
- `sk_on_flatiron_ess_7_2gwh_case`: Stage 2 cap due to missing contract value.
- `ford_energy_storage_pivot_case`: EV-to-ESS pivot price reaction confirmed, but suppliers need direct evidence.
- `quantumscape_vw_solid_state_license_case`: Stage 2 plus 4B-watch, not commercialization Green.
- `ford_lges_ev_contract_cancel_case`: 4C gate aligned with price decline.
- `qcells_customs_detention_furlough_case`: UFLPA/customs risk is a hard gate.
- `orsted_sunrise_wind_impairment_case`: project economics failure is a hard gate.

## Guardrails

- Do not use Round-122 case records as candidate-generation input.
- Do not change production scoring from this pack.
- Do not loosen Stage 3-Green to improve recall.
- Do not invent contract values, customers, GWh, utilization, margin, SOH, FCF, EPS revision, or stage prices.
- Do not treat EV CAPA growth, ESS label, solid-state license, solar policy, or wind PPA as Green evidence by name alone.

## Verification

Focused Round-122 tests passed:

```bash
PYTHONPATH=src python -m unittest tests.test_round122_r3_loop7_battery_ev_green -v
```

Full test suite is run before committing this checkpoint.

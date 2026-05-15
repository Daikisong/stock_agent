# Checkpoint 28A Round 49: R9 Mobility / Transport / Leisure

## Scope

Round 49 converts `docs/round/round_49.md` into calibration-only data for the
R9 mobility, transport, and leisure sector.

This does not change production scoring. The new files are for case-library,
score-weight draft, Green guardrail, cycle/event cap, and price-path validation
work.

## Files Added

- `src/e2r/sector/round49_r9_mobility_transport_leisure.py`
- `src/e2r/cli/build_round49_r9_report.py`
- `tests/test_round49_r9_mobility_transport_leisure.py`
- `data/e2r_case_library/cases_r9_round49.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round49_r9_v1.csv`
- `output/e2r_round49_r9_mobility_transport_leisure/`

## Archetype Updates

New R9-specific canonical archetypes were added:

- `TIRE_AUTO_COMPONENT_SPREAD`
- `AIRLINE_TRAVEL_CYCLE`
- `CASINO_DUTYFREE_TOURISM`
- `LOGISTICS_PARCEL_FREIGHT`
- `RENTAL_USED_CAR_MOBILITY`
- `MOBILITY_RENTAL_MICROMOBILITY`
- `AUTO_COMPONENTS_EV_ADAS`
- `URBAN_AIR_DRONE`
- `SPACE_SUPPLYCHAIN`
- `SATELLITE_CONNECTIVITY_INFRA`

Existing R9 archetypes were also given more specific definitions:

- `AUTO_MOBILITY_COMPLETED_VEHICLE`
- `AUTO_MOBILITY_COMPONENTS`
- `SHIPPING_FREIGHT_CYCLE`
- `TRAVEL_LEISURE_REOPENING`

## R9 Principle

R9 is not a simple demand-recovery sector.

Simple example:

- A casino or duty-free stock can rise after visa-free tourism news.
- That is Stage 1 evidence.
- It is not Stage 3-Green until actual `casino_drop_amount`, `duty_free_sales`,
  visitor spend, ASP, and OPM are visible.

The same rule applies across R9:

- Auto value-up needs hybrid/mix, FCF, and shareholder return execution.
- Airlines need fuel/FX and integration-cost discipline.
- Shipping needs freight-rate and capacity-cycle checks.
- Rental and micromobility need residual value, repair cost, debt, and unit economics.
- eVTOL/drone needs certification, revenue, cash runway, and low dilution risk.
- Satellite connectivity needs real backlog and recurring connectivity revenue.

## Case Pack

Round 49 writes 13 calibration cases:

- `hyundai_hybrid_valueup_case`
- `toyota_hybrid_supply_bottleneck_case`
- `hyundai_mobis_lighting_restructuring_case`
- `korean_air_asiana_integration_case`
- `china_group_visa_tourism_case`
- `ses_airline_connectivity_case`
- `lime_ipo_micromobility_case`
- `maersk_overcapacity_rate_collapse_case`
- `hertz_ev_rental_failure_case`
- `michelin_tire_demand_cut_case`
- `joby_blade_acquisition_case`
- `joby_discounted_offering_case`
- `archer_part135_no_type_cert_case`

Counts:

- target_count: 14
- case_candidate_count: 13
- success_candidate_count: 6
- cyclical_success_count: 1
- event_premium_count: 2
- stage4c_case_count: 4
- green_possible_count: 2
- watch_yellow_first_count: 9
- redteam_first_count: 3

## Green Guardrails

The R9 pack explicitly blocks these shortcuts:

- Demand recovery alone is not Green evidence.
- Tourism policy headlines are not Green evidence.
- Freight-rate spikes are not Green evidence.
- EV fleet expansion is not Green evidence.
- Part 135 approval is not full eVTOL commercialization.
- SpaceX or space-theme labels are not score evidence.

Green requires source-backed operating evidence such as:

- OPM / FCF
- unit economics
- shareholder return execution
- fuel/FX risk control
- visitor spend and casino/drop metrics
- freight-rate and capacity discipline
- residual value and repair cost
- certification and cash runway
- backlog and recurring connectivity revenue

## Generated Reports

The CLI generated:

- `output/e2r_round49_r9_mobility_transport_leisure/round49_r9_mobility_transport_leisure_summary.md`
- `output/e2r_round49_r9_mobility_transport_leisure/round49_r9_case_matrix.csv`
- `output/e2r_round49_r9_mobility_transport_leisure/round49_r9_stage_date_plan.csv`
- `output/e2r_round49_r9_mobility_transport_leisure/round49_r9_green_guardrails.md`
- `output/e2r_round49_r9_mobility_transport_leisure/round49_r9_cycle_event_caps.md`
- `output/e2r_round49_r9_mobility_transport_leisure/round49_r9_price_validation_plan.md`
- `output/e2r_round49_r9_mobility_transport_leisure/round49_r9_price_fields.csv`

## Validation

Commands run:

```bash
PYTHONPATH=src python -m unittest tests/test_round49_r9_mobility_transport_leisure.py -v
PYTHONPATH=src python -m e2r.cli.build_round49_r9_report
```

Result:

- Round 49 tests passed.
- Report generation passed.

## Production Safety

- Production scoring was not changed.
- StageClassifier thresholds were not changed.
- Case records are not candidate-generation input.
- No API keys or paid data dependencies are introduced.
- The pack is calibration/evaluation material only.

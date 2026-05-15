# Round-49 R9 Price Validation Plan

## Method

1. Assign stage dates from source evidence only.
2. Store stage-date close prices from official price data.
3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.
4. Calculate MAE_30D / 90D / 180D / 1Y.
5. Calculate peak price, drawdown after peak, and below-stage3 flag.
6. Compare price paths with OPM, FCF, buyback/dividend, fuel/FX, tourist spend, freight rates, residual value, certification, backlog, capex/debt, and cash burn.

## Priority Case Checks

| case_id | stage candidate | check |
| --- | --- | --- |
| `hyundai_hybrid_valueup_case` | 2024-08-28 | needs_price_backfill |
| `toyota_hybrid_supply_bottleneck_case` | 2025-03-31 | needs_price_backfill |
| `hyundai_mobis_lighting_restructuring_case` | 2026-01-27 | needs_price_backfill |
| `korean_air_asiana_integration_case` | 2025-02-07 | needs_price_backfill |
| `china_group_visa_tourism_case` | 2025-08-06 | needs_price_backfill |
| `ses_airline_connectivity_case` | 2026-05-12 | needs_price_backfill |
| `lime_ipo_micromobility_case` | 2026-05-01 | needs_price_backfill |
| `maersk_overcapacity_rate_collapse_case` | 2025-10-03 | needs_price_backfill |
| `hertz_ev_rental_failure_case` | 2024-01-11 | needs_price_backfill |
| `michelin_tire_demand_cut_case` | 2025-10-13 | needs_price_backfill |
| `joby_blade_acquisition_case` | 2025-08-04 | needs_price_backfill |
| `joby_discounted_offering_case` | 2025-10-08 | needs_price_backfill |
| `archer_part135_no_type_cert_case` | 2024-06-05 | needs_price_backfill |

## Alignment Labels

- `aligned`: mix, FCF, capital return, backlog, or recurring revenue moves with price rerating.
- `cyclical_success`: airline, shipping, tire, or travel cycle improves but does not prove structural Green.
- `policy_event_premium`: visa, tourism, merger, or policy headline moves price before operating evidence.
- `unit_economics_failure`: fleet, rental, micromobility, or eVTOL revenue grows while residual value, debt, repair cost, or cash burn breaks.
- `thesis_break`: freight collapse, EV rental write-down, certification delay, discounted offering, fuel/FX shock, or major recall damages the thesis.

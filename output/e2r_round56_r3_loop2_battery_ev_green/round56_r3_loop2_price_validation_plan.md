# Round-56 R3 Loop-2 Price Validation Plan

## Method

1. Assign stage dates from source evidence only.
2. Store stage-date close prices from official price data.
3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.
4. Calculate MAE_30D / 90D / 180D / 1Y.
5. Compare EV demand, ESS contract, utilization, CAPEX, mineral prices, subsidies, customs/tariffs, and price path.
6. Mark plant idle, contract cancellation, customs detention, wind impairment, lithium crash, and EV fire regulation explicitly.

## Priority Case Checks

| case_id | target | stage marker | check |
| --- | --- | --- | --- |
| `lg_energy_solution_ess_shift_case` | `BATTERY_RECYCLING_ESS_SHIFT` | 2025-07-25 | needs_price_backfill |
| `lg_energy_tesla_lfp_ess_contract_case` | `BATTERY_RECYCLING_ESS_SHIFT` | 2025-07-30 | needs_price_backfill |
| `sk_on_flatiron_ess_7_2gwh_case` | `BATTERY_RECYCLING_ESS_SHIFT` | 2025-09-03 | needs_price_backfill |
| `redwood_recycling_energy_storage_case` | `BATTERY_RECYCLING_ESS_SHIFT` | 2025-10-23 | missing_public_price_data |
| `hyundai_hydrogen_fuel_cell_plant_case` | `HYDROGEN_FUEL_CELL_INFRA` | 2025-10-30 | needs_price_backfill |
| `eqt_kj_environment_waste_platform_case` | `WASTE_RECYCLING_ENVIRONMENT` | 2024-08-16 | missing_public_price_data |
| `gm_lg_ultium_ohio_idle_case` | `BATTERY_MATERIALS_CAPEX_OVERHEAT` | 2026-05-12 | needs_price_backfill |
| `ford_lges_ev_contract_cancel_case` | `BATTERY_MATERIALS_CAPEX_OVERHEAT` | 2025-12-17 | needs_price_backfill |
| `qcells_customs_detention_furlough_case` | `SOLAR_TARIFF_SUPPLYCHAIN` | 2025-11-08 | missing_public_price_data |
| `orsted_sunrise_wind_impairment_case` | `RENEWABLE_ENERGY_POLICY` | 2025-01-20 | needs_price_backfill |
| `lithium_price_86pct_crash_case` | `BATTERY_MATERIALS_CAPEX_OVERHEAT` | 2025-01-13 | missing_price_data |
| `albemarle_cost_cut_low_lithium_case` | `BATTERY_MATERIALS_CAPEX_OVERHEAT` | 2025-02-12 | needs_price_backfill |
| `korea_ev_battery_certification_fire_case` | `EV_FIRE_RISK_OVERLAY` | 2024-08-25 | missing_price_data |

## Alignment Labels

- `ess_contract_aligned`: contract value, duration, customer, ESS use case, and later price/EPS path align.
- `ess_shift_but_price_failed`: ESS transition exists but EV slowdown or subsidy risk suppresses price.
- `ev_capa_false_green`: CAPA expansion was scored positively before utilization or customer demand failed.
- `solar_policy_supplychain_4c`: policy/subsidy story failed because customs, UFLPA, tariff, or component supply broke production.
- `wind_project_impairment_4c`: policy/PPA story failed because project economics broke.
- `ev_fire_regulatory_overlay`: fire/certification/retrieval risk blocks unsafe Green.

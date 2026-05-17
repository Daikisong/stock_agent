# Round-135 R3 Loop-8 Price Validation Plan

## Method

1. Assign stage dates from source evidence only.
2. Store stage-date close prices from official price data.
3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.
4. Calculate MAE_30D / 90D / 180D / 1Y.
5. Compare EV demand, ESS contracts, factory utilization, CAPEX, mineral prices, subsidy/tariff, fire/certification, and SOH events with price path.
6. Mark plant idle, contract cancellation, customs detention, wind impairment, lithium crash, EV fire regulation, and SOH opacity explicitly.

## Priority Case Checks

| case_id | target | stage marker | check |
| --- | --- | --- | --- |
| `lg_energy_lfp_4_3b_contract_initial_case` | `BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE` | 2025-07-30 | needs_price_backfill |
| `tesla_lges_megapack3_lansing_case` | `ESS_TESLA_MEGAPACK_SUPPLY_CHAIN` | 2026-03-17 | needs_price_backfill |
| `sk_on_flatiron_ess_7_2gwh_case` | `ESS_LFP_GRID_STORAGE` | 2025-09-03 | needs_price_backfill |
| `gm_lg_ultium_ohio_idle_case` | `EV_TO_ESS_CAPACITY_REDEPLOYMENT` | 2026-05-12 | needs_price_backfill |
| `sk_on_ford_jv_dissolution_case` | `EV_BATTERY_JV_RESTRUCTURING` | 2025-12-11 | needs_price_backfill |
| `ford_energy_storage_pivot_case` | `ESS_AI_DATA_CENTER_STORAGE` | undated | needs_exact_stage_date_backfill |
| `ford_lges_ev_contract_cancel_case` | `EV_CAPA_CONTRACT_CANCELLATION` | 2025-12-17 | needs_price_backfill |
| `lges_freudenberg_contract_cancel_case` | `EV_CAPA_CONTRACT_CANCELLATION` | 2025-12-26 | needs_price_backfill |
| `redwood_recycling_energy_storage_case` | `BATTERY_RECYCLING_ESS_SHIFT` | 2025-10-23 | missing_public_price_data |
| `second_life_battery_grid_storage_reference_case` | `SECOND_LIFE_BATTERY_GRID_STORAGE` | undated | needs_exact_stage_date_backfill |
| `graphite_supply_security_case` | `BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY` | undated | needs_exact_stage_date_backfill |
| `eqt_kj_environment_waste_platform_case` | `WASTE_RECYCLING_ENVIRONMENT` | 2024-08-16 | missing_public_price_data |
| `hyundai_hydrogen_fuel_cell_plant_case` | `HYDROGEN_FUEL_CELL_INFRA` | 2025-10-30 | needs_price_backfill |
| `qcells_customs_detention_furlough_case` | `SOLAR_TARIFF_SUPPLYCHAIN` | 2025-11-08 | missing_public_price_data |
| `orsted_sunrise_wind_impairment_case` | `RENEWABLE_ENERGY_PROJECT_ECONOMICS` | 2025-01-20 | needs_price_backfill |
| `lithium_price_86pct_crash_case` | `LITHIUM_ESS_DEMAND_CYCLE` | 2025-01-13 | missing_price_data |
| `lithium_ess_demand_recovery_case` | `LITHIUM_ESS_DEMAND_CYCLE` | 2026-01-04 | missing_price_data |
| `sodium_ion_substitution_watch_case` | `SODIUM_ION_SUBSTITUTION_OVERLAY` | undated | needs_exact_stage_date_backfill |
| `korea_ev_battery_certification_fire_case` | `EV_FIRE_BESS_SAFETY_OVERLAY` | 2024-08-25 | missing_price_data |
| `moss_landing_bess_fire_case` | `BESS_SAFETY_PERMITTING` | 2025-01-17 | needs_exact_stage_date_backfill |
| `battery_soh_transparency_case` | `BATTERY_SOH_SECOND_LIFE_TRANSPARENCY` | undated | needs_exact_stage_date_backfill |
| `quantumscape_vw_solid_state_license_case` | `SOLID_STATE_COMMERCIALIZATION_LICENSE` | 2024-07-11 | needs_price_backfill |
| `speculative_solid_state_theme_case` | `SPECULATIVE_BATTERY_TECH` | undated | needs_exact_stage_date_backfill |

## Alignment Labels

- `ess_contract_aligned`: contract value, duration, customer, GWh, ESS use case, and later price/EPS path align.
- `ess_tesla_megapack_stage2_watch`: Tesla/Megapack confirmation improves visibility, but ramp-up, utilization, ESS OPM, and FCF are still open.
- `ess_disclosure_capped`: a large contract exists, but undisclosed customer/use-case/margin blocks Green.
- `ev_battery_contract_cancellation_hard_4c`: EV contract value becomes a thesis-break signal when cancellation removes expected revenue.
- `ev_capa_false_green_plus_ess_shift_watch`: EV CAPA is broken, while ESS conversion remains only Watch.
- `ev_to_ess_redeployment_watch`: EV assets move toward ESS, but conversion cost, customer, utilization, and margin are not proven.
- `ev_jv_restructuring_with_ess_pivot`: JV restructuring is not clean positive evidence until cost relief and ESS revenue/margin are visible.
- `recycling_plus_storage_structural_reference`: recycling, recovered metals, ESS/grid services, and customers connect.
- `graphite_security_but_cost_risk`: graphite supply security needs policy financing, offtake, cost path, and customers.
- `solid_state_license_stage2_but_commercialization_watch`: license is not commercialization before production, vehicle adoption, royalty revenue, cost, and yield.
- `solar_policy_supplychain_4c`: policy/subsidy story failed because customs, UFLPA, tariff, or component supply broke production.
- `wind_project_impairment_4c`: policy/PPA story failed because project economics broke.
- `battery_health_transparency_redteam`: SOH and residual-capacity opacity blocks unsafe second-life/recycling Green.
- `speculative_tech_price_moved_without_evidence`: technology theme moved before commercialization, customer evidence, production, and FCF.

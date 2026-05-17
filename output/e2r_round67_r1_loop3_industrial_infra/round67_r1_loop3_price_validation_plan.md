# Round-67 R1 Loop-3 Price Validation Plan

## Method

1. Assign stage dates from source evidence only.
2. Store stage-date close prices from official price data.
3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.
4. Calculate MAE_30D / 90D / 180D / 1Y.
5. Compare contract quality, backlog, margin, OP/EPS revision, FCF conversion, and price path.
6. Mark project delay, capital-allocation shock, low-margin backlog, MRO option-only, SMR policy false Green, and policy-to-contract failure explicitly.

## Priority Case Checks

| case_id | target | stage marker | check |
| --- | --- | --- | --- |
| `us_transformer_shortage_import_slots_case` | `GRID_TRANSFORMER_SHORTAGE` | 2026-05-11 | needs_price_backfill |
| `ge_vernova_data_center_orders_case` | `AI_DATA_CENTER_POWER_EQUIPMENT` | 2026-04-22 | needs_price_backfill |
| `data_center_local_opposition_grid_case` | `PROJECT_DELAY_CAPEX_OVERLAY` | 2026-05-13 | needs_price_backfill |
| `hanwha_aerospace_romania_k9_case` | `DEFENSE_GOVERNMENT_BACKLOG` | 2024-07-09 | needs_price_backfill |
| `hanwha_aerospace_europe_sales_visibility_case` | `DEFENSE_GOVERNMENT_BACKLOG` | 2024-10-07 | needs_price_backfill |
| `hanwha_aerospace_dilution_case` | `CAPITAL_ALLOCATION_DILUTION_OVERLAY` | 2025-03-27 | needs_price_backfill |
| `korean_shipbuilder_contract_rally_case` | `SHIPBUILDING_OFFSHORE_BACKLOG` | undated | needs_source_date_backfill |
| `hanwha_ocean_us_navy_mro_case` | `SHIPBUILDING_NAVAL_MRO` | 2025-05-05 | needs_price_backfill |
| `hyundai_rotem_morocco_rail_case` | `RAIL_INFRASTRUCTURE` | 2025-02-26 | needs_price_backfill |
| `meta_constellation_existing_nuclear_ppa_case` | `NUCLEAR_EXISTING_PPA` | 2025-06-03 | needs_price_backfill |
| `nuscale_uamps_smrcancel_case` | `NUCLEAR_SMR_GRID_POLICY` | 2023-11-01 | needs_price_backfill |
| `ukraine_reconstruction_policy_case` | `GEOPOLITICAL_RECONSTRUCTION` | undated | needs_price_backfill |
| `neom_city_policy_case` | `GEOPOLITICAL_RECONSTRUCTION` | undated | needs_price_backfill |

## Alignment Labels

- `CONTRACT_QUALITY_ALIGNED`: contract value/duration/counterparty/delivery/margin/EPS and price path align.
- `BACKLOG_WITHOUT_MARGIN`: backlog/order exists but margin or EPS conversion is not proven.
- `PROJECT_DELAY_RISK`: demand exists but project execution threatens order growth.
- `CAPITAL_ALLOCATION_SHOCK`: backlog remains attractive but dilution or funding damages price path.
- `SMR_POLICY_FALSE_GREEN`: policy and theme exist but cost/customer/permit/financing are missing.
- `POLICY_TO_CONTRACT_FAILED`: policy/MOU does not become funded order or revenue.

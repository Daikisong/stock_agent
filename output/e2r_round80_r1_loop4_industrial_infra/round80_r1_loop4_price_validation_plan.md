# Round-80 R1 Loop-4 Price Validation Plan

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
| `abb_medium_voltage_expansion_case` | `GRID_MEDIUM_VOLTAGE_EXPANSION` | 2026-05-11 | needs_price_backfill |
| `ge_vernova_data_center_orders_case` | `AI_DATA_CENTER_POWER_EQUIPMENT` | 2026-04-22 | needs_price_backfill |
| `perth_data_center_withdrawal_case` | `DATA_CENTER_GRID_PERMITTING_OVERLAY` | 2026-05-15 | needs_price_backfill |
| `seattle_indianapolis_data_center_moratorium_case` | `DATA_CENTER_GRID_PERMITTING_OVERLAY` | 2026-05-15 | needs_price_backfill |
| `hanwha_aerospace_romania_k9_case` | `DEFENSE_GOVERNMENT_BACKLOG` | 2024-07-09 | needs_price_backfill |
| `hanwha_aerospace_europe_sales_visibility_case` | `DEFENSE_LOCAL_PRODUCTION_PLATFORM` | 2024-10-07 | needs_price_backfill |
| `hanwha_aerospace_dilution_case` | `DEFENSE_CAPITAL_ALLOCATION_SHOCK` | 2025-03-27 | needs_price_backfill |
| `hanwha_ocean_us_shipbuilding_sanction_case` | `SHIPBUILDING_NAVAL_MRO` | undated | needs_source_date_backfill |
| `hanwha_vatn_underwater_drone_case` | `DEFENSE_UNMANNED_NAVAL_SYSTEMS` | 2025-12-10 | needs_price_backfill |
| `hyundai_rotem_morocco_rail_case` | `RAIL_INFRASTRUCTURE` | 2025-02-26 | needs_price_backfill |
| `meta_constellation_existing_nuclear_ppa_case` | `NUCLEAR_EXISTING_PPA_RESTART` | 2025-06-03 | needs_price_backfill |
| `constellation_tmi_microsoft_restart_case` | `NUCLEAR_EXISTING_PPA_RESTART` | 2026-05-11 | needs_price_backfill |
| `nuscale_uamps_smr_cancel_case` | `NUCLEAR_SMR_GRID_POLICY` | 2023-11-01 | needs_price_backfill |
| `ukraine_reconstruction_policy_case` | `GEOPOLITICAL_RECONSTRUCTION` | undated | needs_price_backfill |
| `neom_city_policy_case` | `GEOPOLITICAL_RECONSTRUCTION` | undated | needs_price_backfill |

## Alignment Labels

- `CONTRACT_QUALITY_ALIGNED`: contract value/duration/counterparty/delivery/margin/EPS and price path align.
- `BACKLOG_WITHOUT_MARGIN`: backlog/order exists but margin or EPS conversion is not proven.
- `PROJECT_DELAY_RISK`: demand exists but project execution threatens order growth.
- `CAPITAL_ALLOCATION_SHOCK`: backlog remains attractive but dilution or funding damages price path.
- `SMR_POLICY_FALSE_GREEN`: policy and theme exist but cost/customer/permit/financing are missing.
- `POLICY_TO_CONTRACT_FAILED`: policy/MOU does not become funded order or revenue.

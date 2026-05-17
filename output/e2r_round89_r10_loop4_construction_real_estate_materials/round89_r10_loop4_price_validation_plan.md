# Round-89 R10 Price Validation Plan

## Method

1. Assign stage dates from source evidence only.
2. Store stage-date close prices from official price data.
3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.
4. Calculate MAE_30D / 90D / 180D / 1Y.
5. Calculate peak price, drawdown after peak, and below-stage3 flag.
6. Compare price paths with PF exposure, unsold inventory, NOI/AFFO, dividend coverage, occupancy, LTV, funding cost, material volumes, price hikes, tenants, power, and contracts.

## Priority Case Checks

| case_id | stage candidate | check |
| --- | --- | --- |
| `korea_pf_delinquency_restructuring_case` | 2024-05-13 | needs_price_backfill |
| `korea_builder_support_relief_case` | 2024-03-27 | needs_price_backfill |
| `blackstone_mortgage_trust_dividend_cut_case` | 2024-07-24 | needs_price_backfill |
| `equinix_affo_integrity_short_case` | 2024-03-20 | needs_price_backfill |
| `equinix_ai_capex_burden_case` | 2025-06-26 | needs_price_backfill |
| `equinix_malaysia_ai_liquid_cooling_case` | 2026-05-12 | needs_price_backfill |
| `blackstone_data_center_reit_flat_debut_case` | 2026-05-14 | needs_price_backfill |
| `fermi_ai_data_center_no_revenue_case` | 2025-09-30 | needs_price_backfill |
| `fermi_no_tenant_net_loss_case` | 2026-03-30 | needs_price_backfill |
| `perth_datacenter_withdrawal_case` | 2026-05-15 | needs_price_backfill |
| `utah_stratos_datacenter_backlash_case` | 2026-05-13 | needs_price_backfill |
| `lineage_cold_storage_ipo_case` | 2024-07-25 | needs_price_backfill |
| `lineage_cold_storage_debt_occupancy_case` | 2025-10-01 | needs_price_backfill |
| `heidelberg_materials_price_cost_case` | 2025-11-06 | needs_price_backfill |
| `cemex_demand_slowdown_costcut_case` | 2025-02-06 | needs_price_backfill |
| `cemex_price_cost_restructuring_case` | 2025-10-27 | needs_price_backfill |
| `ukraine_reconstruction_event_watch_case` | 2025-01-01 | needs_price_backfill |
| `neom_city_event_watch_case` | 2025-01-01 | needs_price_backfill |
| `sejong_policy_theme_case` | 2025-01-01 | needs_price_backfill |

## Alignment Labels

- `policy_relief_rally`: government support or rate-cut expectations move price before credit repair.
- `credit_recovery_aligned`: PF risk, cash flow, and debt structure improve with price.
- `asset_cashflow_aligned`: REIT/real-asset price follows NOI/AFFO, occupancy, and dividend coverage.
- `building_materials_cycle_success`: price/cost/volume alignment works, but cycle risk remains.
- `theme_without_asset`: data-center, reconstruction, Neom, or disaster-rebuild theme lacks assets, tenants, contracts, or financing.
- `thesis_break`: PF delinquency, debt workout, dividend cut, vacancy, impairment, net loss, or refinancing failure breaks the case.

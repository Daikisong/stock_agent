# Round-103 R11 Loop-5 Price Validation Plan

## Method

1. Assign stage dates from source evidence only.
2. Store Stage 1 and Stage 2 event-date close prices from official price data.
3. Calculate MFE_5D / 20D / 60D / 90D / 180D and matching MAE windows.
4. Calculate peak_price and drawdown_after_peak.
5. Compare price moves with actual contracts, budgets, government orders, financing, construction starts, revenue, and EPS evidence.
6. If evidence is missing, classify as `price_moved_without_evidence`, `event_premium`, or `policy_relief_only`.

## Priority Case Checks

| case_id | stage candidate | check |
| --- | --- | --- |
| `bavarian_nordic_us_stockpile_contract_case` | 2026-05-11 | needs_price_backfill |
| `moderna_cepi_bird_flu_funding_case` | 2025-12-18 | needs_price_backfill |
| `moderna_barda_contract_cancel_case` | 2025-05-29 | needs_price_backfill |
| `bavarian_nordic_2024_mpox_order_case` | 2024-08-16 | needs_price_backfill |
| `ukraine_telecom_ebrd_ifc_case` | 2024-10-10 | needs_price_backfill |
| `ukraine_ebrd_power_port_concession_case` | 2026-05-15 | needs_price_backfill |
| `heatwave_ac_grid_stress_case` | 2025-07-18 | needs_price_backfill |
| `nyc_ac_battery_vpp_case` | 2026-05-01 | needs_price_backfill |
| `north_korea_kumgang_dismantle_case` | 2025-02-13 | needs_price_backfill |
| `lk99_superconductor_no_replication_case` | 2023-08-08 | needs_price_backfill |
| `lk99_cu2s_impurity_case` | 2023-11-01 | needs_price_backfill |
| `abbott_diagnostics_demand_wane_case` | 2025-10-15 | needs_price_backfill |
| `ai_citizen_dividend_policy_shock_case` | 2026-05-12 | needs_price_backfill |

## Alignment Labels

- `event_to_contract_stockpile_candidate`: event demand is backed by a government stockpile contract, but still needs recurrence and margin checks.
- `government_stockpile_contract_guidance_aligned_candidate`: stockpile contract raised guidance, yet repeat procurement and post-event FCF still decide higher stages.
- `public_health_procurement_funding_stage2`: public-health funding is enough for research routing, not durable revenue by itself.
- `procurement_reversal_4c`: government funding or procurement was withdrawn; this is a thesis-break warning for public-health event assumptions.
- `funded_geopolitical_infra_candidate`: financing exists; company-level contract and margin proof still decide scoring.
- `critical_infra_financing_aligned_candidate`: critical infrastructure financing exists; individual supplier revenue and margin still need validation.
- `event_to_infra_crossover_candidate`: climate/disaster demand crossed into grid, VPP, ESS, cooling, or rebuild infrastructure.
- `policy_tourism_event_stage1`: visa or tourism policy is Stage 1 routing until arrivals, spend, duty-free sales, casino drop, RevPAR, and OPM are verified.
- `price_moved_without_evidence`: science, policy, or disaster theme moved price before technical/customer/revenue evidence.
- `speculative_science_failure`: replication failure or impurity explanation breaks the thesis.
- `one_off_diagnostic_demand_normalized`: diagnostics revenue fell after temporary event demand normalized.
- `policy_market_shock_event`: policy comments changed market risk premium; this is RedTeam evidence unless company EPS/FCF impact is quantified.

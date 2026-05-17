# Round-65 R12 Loop-2 Price Validation Plan

## Method

1. Assign stage dates from source evidence only.
2. Store stage-date close prices from official price data.
3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.
4. Calculate MAE_30D / 90D / 180D / 1Y.
5. Compare price paths with farm income, equipment sales, commodity prices, disease events, recurring revenue, CAC, churn, regulatory scope, and FCF.

## Priority Case Checks

| case_id | stage candidate | check |
| --- | --- | --- |
| `deere_farm_equipment_demand_slowdown_case` | 2025-02-13 | needs_price_backfill |
| `zoetis_bird_flu_vaccine_conditional_case` | 2025-02-14 | needs_price_backfill |
| `calmaine_egg_price_profit_case` | 2025-04-09 | needs_price_backfill |
| `bowery_vertical_farming_shutdown_case` | 2024-11-05 | needs_price_backfill |
| `appharvest_chapter11_case` | 2023-07-24 | needs_price_backfill |
| `duolingo_ai_strategy_bookings_miss_case` | 2026-02-26 | needs_price_backfill |
| `chegg_ai_disruption_case` | 2023-05-02 | needs_price_backfill |
| `2u_chapter11_case` | 2024-07-25 | needs_price_backfill |
| `whirlpool_dividend_suspension_case` | 2026-05-07 | needs_price_backfill |
| `juul_fda_approval_case` | 2025-07-17 | needs_price_backfill |
| `cannabis_schedule3_limited_case` | 2026-05-12 | needs_price_backfill |

## Alignment Labels

- `smart_farm_unit_economics_aligned`: orders, utilization, energy cost, and FCF move together.
- `vertical_farming_4c`: shutdown, Chapter 11, premium-pricing failure, or CAPEX burden breaks the case.
- `agri_machinery_tech_but_cycle_watch`: technology exists, but farm income, financing, and equipment demand cap the case.
- `animal_health_event_to_contract`: disease event turns into vaccine approval, stockpile, and repeated use.
- `livestock_cyclical_success`: price spike generated profit, but structural durability is weak.
- `education_ai_disruption_4c`: AI replaces the core service or weakens traffic, subscribers, bookings, and revenue.
- `rental_recurring_success`: rental accounts, churn, care-service revenue, and FCF are confirmed.
- `regulated_consumer_approval_stage2`: FDA/DEA approval can create Stage 2, but scope and public-health gates remain.

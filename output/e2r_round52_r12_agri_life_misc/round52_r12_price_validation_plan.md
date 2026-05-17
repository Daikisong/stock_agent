# Round-52 R12 Price Validation Plan

## Method

1. Assign stage dates from source evidence only.
2. Store stage-date close prices from official price data.
3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.
4. Calculate MAE_30D / 90D / 180D / 1Y.
5. Compare price paths with farm income, equipment sales, commodity prices, disease events, recurring revenue, CAC, churn, and regulatory fields.

## Priority Case Checks

| case_id | stage candidate | check |
| --- | --- | --- |
| `deere_farm_equipment_demand_slowdown_case` | 2025-02-13 | needs_price_backfill |
| `zoetis_bird_flu_vaccine_conditional_case` | 2025-02-14 | needs_price_backfill |
| `calmaine_egg_price_profit_case` | 2025-04-09 | needs_price_backfill |
| `multiverse_ai_training_case` | 2026-05-01 | needs_price_backfill |
| `duolingo_ai_strategy_bookings_miss_case` | 2026-02-26 | needs_price_backfill |
| `juul_fda_approval_case` | 2025-07-17 | needs_price_backfill |
| `bowery_vertical_farming_shutdown_case` | 2024-11-05 | needs_price_backfill |
| `appharvest_chapter11_case` | 2023-07-24 | needs_price_backfill |
| `chegg_ai_disruption_case` | 2023-05-02 | needs_price_backfill |
| `2u_chapter11_case` | 2024-07-25 | needs_price_backfill |
| `whirlpool_dividend_suspension_case` | 2026-05-07 | needs_price_backfill |
| `cannabis_schedule3_limited_case` | 2026-05-12 | needs_price_backfill |

## Alignment Labels

- `aligned`: repeat contracts, repeat revenue, FCF, and price rerating move together.
- `cyclical_success`: livestock, food, egg, feed, or commodity prices drive profits but cycle risk remains.
- `event_to_contract`: disease or regulation event turns into actual government order, stockpile, approval, or contract.
- `theme_without_unit_economics`: smart farm, vertical farm, education app, or kiosk story lacks unit economics.
- `regulatory_approval_stage2`: approval changes sales possibility, but regulatory reversal risk remains.
- `thesis_break`: bankruptcy, AI substitution, dividend suspension, retailer retreat, regulation reversal, or price normalization breaks the case.

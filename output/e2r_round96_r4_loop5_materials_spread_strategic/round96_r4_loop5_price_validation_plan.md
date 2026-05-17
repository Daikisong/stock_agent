# Round-96 R4 Loop-5 Price Validation Plan

## Method

1. Assign stage dates from source evidence only.
2. Store stage-date close prices from official price data.
3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.
4. Calculate MAE_30D / 90D / 180D / 1Y.
5. Compare commodity price, product spread, inventory gain/loss, offtake, price floor, FCF, dividend/buyback, and price path.
6. Mark event premium, oversupply, supply restart, stockpile distortion, dividend cut, M&A remedies, and no commercialization explicitly.

## Priority Case Checks

| case_id | target | stage marker | check |
| --- | --- | --- | --- |
| `mp_materials_dod_price_floor_case` | `RARE_METALS_PRICE_FLOOR_OFFTAKE` | undated | needs_exact_stage_date_backfill |
| `mp_materials_apple_magnet_contract_case` | `RARE_EARTH_MAGNET_SUPPLY_CHAIN` | undated | needs_exact_stage_date_backfill |
| `china_heavy_rare_earth_export_control_case` | `RARE_METALS_EXPORT_CONTROL_EVENT` | 2026-05-13 | missing_direct_symbol_mapping |
| `china_yttrium_dysprosium_terbium_delay_case` | `RARE_METALS_EXPORT_CONTROL_EVENT` | 2026-05-15 | missing_direct_symbol_mapping |
| `copper_ai_grid_record_high_case` | `COPPER_AI_GRID_STRUCTURAL_DEMAND` | 2026-05-11 | missing_direct_symbol_mapping |
| `barrick_record_gold_buyback_case` | `PRECIOUS_METALS_SAFE_HAVEN_MINERS` | 2026-05-11 | needs_price_backfill |
| `equinox_orla_gold_jurisdiction_case` | `GOLD_MINER_JURISDICTION_RERATING` | 2026-05-13 | missing_direct_symbol_mapping |
| `posco_international_alaska_lng_20y_case` | `GENERAL_TRADING_RESOURCE_INFRA` | 2025-12-04 | needs_price_backfill |
| `sk_innovation_refining_recovery_case` | `REFINING_OIL_SPREAD` | 2026-05-13 | needs_price_backfill |
| `lg_chem_lotte_chemical_oversupply_case` | `CHEMICAL_SPREAD` | 2025-02-07 | needs_price_backfill |
| `lithium_price_86pct_crash_case` | `LITHIUM_ESS_DEMAND_CYCLE` | 2025-01-13 | missing_price_data |
| `bhp_iron_ore_profit_dividend_cut_case` | `IRON_ORE_CHINA_DEMAND_CYCLE` | 2025-02-18 | needs_price_backfill |
| `korea_zinc_tender_offer_event_case` | `EVENT_PREMIUM_GOVERNANCE_OVERLAY` | 2024-09-13 | needs_price_backfill |
| `korea_zinc_share_issue_probe_case` | `EVENT_PREMIUM_GOVERNANCE_OVERLAY` | 2024-10-31 | needs_price_backfill |
| `international_paper_ds_smith_divestment_case` | `PAPER_PACKAGING_CYCLE` | 2025-04-14 | missing_public_price_data |
| `graphene_mxene_superconductor_theme_case` | `ADVANCED_MATERIAL_SPECULATIVE_THEME` | undated | missing_price_data |

## Alignment Labels

- `price_floor_offtake_green_candidate`: price floor, offtake, government support, production, and FCF align.
- `rare_earth_magnet_supply_chain_aligned`: magnet production, Apple/DoD customers, feedstock, and qualification align.
- `geopolitical_bottleneck_reference`: export-control evidence is useful for routing, but not direct company-level Green.
- `export_control_event_only`: rare-earth approval delay remains macro event evidence without production/offtake.
- `commodity_cyclical_success`: price/spread worked, but structural durability remains unproven.
- `copper_ai_grid_watch`: AI-grid demand helps, but copper price distortions and supply response remain.
- `gold_miner_jurisdiction_rerating`: safer mining jurisdictions and M&A scale are a Watch-to-Green path only with FCF and capital return.
- `chemical_spread_green_hard_counterexample`: spread recovery failed due to oversupply and OP/FCF deterioration.
- `event_premium_misclassified`: event-day price reaction should not be scored as FCF rerating.
- `governance_event_capital_structure_4c_watch`: post-event capital structure or regulator risk can turn a premium into a thesis-break watch.
- `speculative_material_theme`: science/materials theme needs commercial product, customer validation, and revenue.

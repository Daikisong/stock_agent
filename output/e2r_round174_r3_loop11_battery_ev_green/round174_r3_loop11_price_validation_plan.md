# Round-174 R3 Loop-11 Price Validation Plan

## Method

1. Assign Stage 1/2/3/4B/4C dates from dated source evidence only.
2. Backfill KRX daily bars for `price_at_stage1` through `price_at_stage4c`.
3. Calculate 20D/60D/120D/252D returns and MFE/MAE after Stage 2.
4. Compare price speed against OP/EPS revision and utilization/margin evidence.
5. Separate contract-led Stage 2 from event-led 4B-watch and demand-break 4C-watch.
6. Keep non-binding, customer-undisclosed, policy/tariff, and commodity-cycle caps explicit.

## Priority Case Checks

| case_id | target | stage marker | check |
| --- | --- | --- | --- |
| `samsung_sdi_ess_lfp_stage2_case` | `ESS_LFP_GRID_STORAGE_KOREA` | 2025-12-09 | needs_price_backfill |
| `posco_future_m_graphite_tariff_4b_case` | `ANODE_GRAPHITE_SUPPLYCHAIN_KOREA` | 2024-02-29 | needs_price_backfill |
| `posco_holdings_lithium_resource_stage2_case` | `LITHIUM_RESOURCE_SECURITY_KOREA` | 2025-11-11 | needs_price_backfill |
| `lg_chem_cathode_toyota_stage2_case` | `CATHODE_LONG_CONTRACT_VISIBILITY` | 2025-09-08 | needs_price_backfill |
| `lg_chem_exxon_non_binding_lithium_case` | `LITHIUM_RESOURCE_SECURITY_KOREA` | 2024-11-20 | needs_price_backfill |
| `lnf_lithium_event_rally_case` | `EVENT_LITHIUM_PRICE_RALLY` | 2025-08-01 | needs_exact_stage_date_backfill |
| `skiet_separator_sale_review_4c_case` | `SEPARATOR_EV_DEMAND_CYCLE` | 2024-05-15 | needs_price_backfill |
| `ecopro_materials_ev_slowdown_4c_case` | `BATTERY_MATERIALS_CAPEX_OVERHEAT_KOREA` | 2023-11-17 | needs_price_backfill |
| `wcp_separator_watch_red_case` | `SEPARATOR_EV_DEMAND_CYCLE` | undated | needs_case_backfill |
| `enchem_electrolyte_capa_watch_case` | `ELECTROLYTE_CAPA_SUPPLYCHAIN` | undated | needs_case_backfill |
| `daejoo_silicon_anode_commercialization_case` | `SILICON_ANODE_COMMERCIALIZATION` | undated | needs_case_backfill |

## Alignment Labels

- `stage2_strong_not_green_yet`: contract evidence is strong but Stage 3 fields are missing.
- `supply_chain_event_not_green`: supply-chain evidence exists, but policy/tariff event rally must be cooled.
- `resource_security_with_cycle_cap`: resources are useful but commodity-cycle and FCF proof remain gates.
- `non_binding_cap_correct`: non-binding deals can route research, not Green.
- `event_rally_not_structural`: commodity price event is not structural evidence.
- `hard_redteam_alignment`: sale review, operating losses, customer strategy break, or utilization collapse blocks positive narrative.

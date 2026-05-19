# Round 215 R11 Loop 8 Policy Geopolitical Event Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_215.md
- large_sector: POLICY_GEOPOLITICAL_EVENT
- cases: 7
- success_candidate: 3
- event_premium: 2
- overheat: 1
- failed_rerating: 1
- price_moved_without_evidence: 3
- Stage 3 dated cases: 0
- 4B-watch cases: 7
- hard_4c_case_count: 1
- r11_default_stage3_bias: very_conservative
- full_ohlc_complete: false

## Case Matrix

| case | company | type | stage2 | stage3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r11_loop8_kogas_east_sea_resource_event | 한국가스공사 | event_premium |  |  | 2024-06-03 |  | price_moved_without_evidence | Resource estimate and drilling approval are Stage 1/event premium until commerciality and revenue conversion. |
| r11_loop8_doosan_nuclear_policy_to_contract | 두산에너빌리티 | success_candidate | 2025-06-04 |  | 2024-07-17 | 2025-05-06 | aligned | Policy-to-contract reached Stage 2; Doosan equipment backlog, margin, and EPS revision are required for Stage 3. |
| r11_loop8_hd_hyundai_masga_shipbuilding_event | HD현대중공업/HD현대미포 | success_candidate | 2025-08-27 |  | 2025-08-27 |  | price_moved_without_evidence | MASGA, merger, and MOU are Stage 2 and 4B-watch until funded orders and margins appear. |
| r11_loop8_poultry_bird_flu_import_ban_event | Poultry basket | event_premium |  |  | 2025-05-19 | 2025-06-23 | price_moved_without_evidence | Disease import ban is one-off Stage 1; restriction easing is event fade. |
| r11_loop8_lk99_speculative_science_break | LK-99 초전도체 basket | overheat |  |  | 2023-08-01 | 2023-08-07 | false_positive_score | Preprint is Stage 1; independent replication failure is 4C/thesis break. |
| r11_loop8_martial_law_macro_market_shock | Korea market macro shock | failed_rerating |  |  |  | 2024-12-04 | false_positive_score | Macro overlay; do not convert it into company-specific Stage 3/4C without direct exposure. |
| r11_loop8_short_selling_msci_market_structure | Short-selling / MSCI accessibility | success_candidate | 2025-06-20 |  |  |  | unknown | Market accessibility is Stage 2 overlay; company EPS or brokerage revenue is needed for Stage 3. |

## Interpretation
- R11 default is event premium, not Stage 3-Green.
- Korea Gas East Sea resource event is Stage 1/4B-watch until drilling and commerciality confirm.
- Doosan nuclear policy-to-contract can reach Stage 2, but equipment backlog and margin are still required.
- MASGA/shipbuilding policy, poultry disease events, and market-structure reform need company earnings conversion.
- LK-99 shows preprint-only science themes need independent replication before any promotion.
- Martial-law shock is macro RedTeam overlay, not a company-specific Stage 3 signal.

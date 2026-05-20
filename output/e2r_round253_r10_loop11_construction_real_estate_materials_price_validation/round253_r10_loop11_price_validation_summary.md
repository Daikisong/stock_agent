# Round 253 R10 Loop 11 Construction Real Estate Materials Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_253.md
- analyst_round_id: round_181
- large_sector: CONSTRUCTION_REAL_ESTATE_MATERIALS
- cases: 8
- success_candidate: 4
- event_premium: 1
- failed_rerating: 2
- Stage 3 dated cases: 0
- 4B-watch cases: 5
- 4C-watch cases: 2
- hard_4c_case_count: 1
- full_adjusted_ohlc_complete: false

## Case Matrix

| case | company | type | round_type | stage2 | stage3 | 4B | 4C | hard 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|---|---|
| r10_loop11_samsung_ea_fadhili_epc_4b | Samsung E&A | success_candidate | success_candidate_4b_watch | 2024-04-03 |  | 2024-04-03 |  | false | success_candidate_event_premium | Mega EPC contract is Stage 2 and 4B-watch; margin, progress revenue and cash collection are required before Green. |
| r10_loop11_hyundai_enc_jafurah_gas_infra | Hyundai E&C | success_candidate | success_candidate_gas_infra_delivery_watch | 2024-06-30 |  |  |  | false | success_candidate | Jafurah is gas-infra Stage 2; Hyundai E&C package, margin and cashflow are required before Green. |
| r10_loop11_ai_data_center_real_asset | SK/AWS·OpenAI·Samsung data-center real asset basket | success_candidate | success_candidate_event_premium | 2025-10-01 |  | 2025-06-20 |  | false | success_candidate_event_premium | AI data-center real asset is Stage 2; tenant, NOI/AFFO, power/water/permitting and capex per share are required. |
| r10_loop11_seoul_housing_policy_supply_watch | Seoul housing policy / construction basket | event_premium | event_premium_policy_watch | 2025-09-07 |  | 2025-09-07 |  | false | event_premium_policy_watch | Housing policy is event premium; presales, margin, PF stability, land cost and FCF are required before Green. |
| r10_loop11_pf_credit_break_taeyoung_basket | Taeyoung / construction PF stress basket | 4c_thesis_break | hard_4c_pf_credit_break |  |  |  | 2024-05-13 | true | thesis_break | PF delinquency spike and liquidity support are hard 4C/crisis relief, not Green. |
| r10_loop11_posco_dl_construction_safety_regulation | POSCO E&C / DL Construction safety regulation basket | failed_rerating | 4c_watch_operating_license_risk |  |  |  | 2025-09-15 | false | thesis_break_watch | Safety regulation is 4C-watch; repeated fatalities become hard 4C if fines, license risk or site shutdown materially impair business. |
| r10_loop11_hyundai_steel_rebar_construction_demand_watch | Hyundai Steel / rebar construction demand proxy | failed_rerating | 4c_watch_building_material_demand_cycle |  |  |  | 2024-06-21 | false | thesis_break_watch | Rebar and construction-demand weakness block building-material Green until demand, spread and margin stabilize. |
| r10_loop11_daewoo_enc_grand_faw_port_delivery | Daewoo E&C | success_candidate | success_candidate_infrastructure_delivery | 2024-11-12 |  |  |  | false | success_candidate | Dock completion is stronger than a mere order headline, but additional backlog, margin and cash collection are required before Stage 3. |

## Interpretation
- Samsung E&A Fadhili and Hyundai E&C Jafurah are Stage 2, not automatic Green.
- AI data-center real asset and Seoul housing policy remain event/policy watch until cash-flow evidence appears.
- PF credit break is confirmed hard 4C; safety regulation is 4C-watch until business impairment is confirmed.
- Hyundai Steel rebar weakness is a demand-cycle Green blocker.

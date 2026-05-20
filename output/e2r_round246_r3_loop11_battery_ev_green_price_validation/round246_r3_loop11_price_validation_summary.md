# Round 246 R3 Loop 11 Battery / EV / Green Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_246.md
- round_id: round_174
- large_sector: BATTERY_EV_GREEN
- cases: 8
- success_candidate: 5
- failed_rerating: 2
- hard_4c_case_count: 1
- 4C-watch cases: 4
- Stage 3 dated cases: 0
- full_ohlc_complete: false

## Case Matrix

| case | company | type | stage2 | stage3 | 4B | 4C | round alignment | note |
|---|---|---|---|---|---|---|---|---|
| r3_loop11_samsung_sdi_lfp_ess_us_contract | Samsung SDI America / Samsung SDI | success_candidate | 2025-12-09 |  | 2025-12-09 |  | Stage 2 | Strong ESS Stage 2; customer, delivery, utilization, OPM and FCF must confirm before Green. |
| r3_loop11_lges_tesla_lfp_ess_contract | LG Energy Solution | success_candidate | 2025-07-30 |  |  |  | Stage 2 | Strong ESS/localization Stage 2; official customer disclosure, delivery, utilization and margin required before Green. |
| r3_loop11_skon_flatiron_lfp_ess | SK On / SK Innovation exposure | success_candidate | 2025-09-03 |  |  |  | Stage 2 | ESS pivot is Stage 2; contract value, utilization, OPM and FCF required before Green. |
| r3_loop11_lges_ford_freudenberg_contract_hard_4c | LG Energy Solution | 4c_thesis_break |  |  |  | 2025-12-17 | contract break | Ford/Freudenberg cancellations are hard 4C; contract headline cannot be Green without actual call-off and utilization. |
| r3_loop11_posco_minres_lithium_resource_security | POSCO Holdings / MinRes lithium JV | success_candidate | 2025-11-11 |  |  |  | resource Stage 2 | Resource security is Stage 2; downstream margin, offtake economics and FCF required before Green. |
| r3_loop11_hanwha_qcells_customs_supply_chain_4c_watch | Hanwha Qcells / Hanwha Solutions exposure | success_candidate | 2024-08-08 |  |  | 2025-11-08 | supply-chain watch | Solar localization is Stage 2; customs/component disruption and furloughs create 4C-watch. |
| r3_loop11_ford_ev_retreat_supply_chain_shock | LGES / Samsung SDI / POSCO Future M / SKIET / EcoPro Materials basket | failed_rerating |  |  |  | 2025-12-16 | demand shock | Ford EV retreat shows demand shock across Korean battery/cathode supply chain. |
| r3_loop11_hyundai_lg_georgia_battery_raid_execution_watch | Hyundai-LG Georgia battery plant / HL-GA Battery | failed_rerating |  |  |  |  | factory execution risk | U.S. localization requires visa/skilled-worker/labor execution; construction alone is not Green. |

## Interpretation
- Samsung SDI, LGES/Tesla-source, and SK On/Flatiron ESS contracts are Stage 2 watch items, not Green before delivery, utilization, OPM and FCF.
- LGES Ford/Freudenberg cancellations are hard 4C because expected revenue disappeared after customer strategy changed.
- POSCO/MinRes lithium resource security is Stage 2, but lithium price cycle and downstream margin cap Green.
- Qcells and Hyundai-LG Georgia show why U.S. localization must pass customs, labor and visa execution risk.
- Ford EV retreat is a supply-chain demand shock that should block unsafe battery/cathode Green.

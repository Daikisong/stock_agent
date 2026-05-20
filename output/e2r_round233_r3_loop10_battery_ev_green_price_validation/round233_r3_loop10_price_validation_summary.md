# Round 233 R3 Loop 10 Battery / EV / Green Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_233.md
- large_sector: BATTERY_EV_GREEN
- cases: 8
- success_candidate: 6
- event_premium: 1
- 4C-watch cases: 3
- hard_4c_case_count: 0
- Stage 3 dated cases: 0
- price_moved_without_evidence: 1
- full_ohlc_complete: false

## Case Matrix

| case | company | type | stage3 | 4B | 4C | round alignment | note |
|---|---|---|---|---|---|---|---|
| r3_loop10_lges_ess_pivot_ev_utilization_watch | LG Energy Solution | success_candidate |  |  | 2026-05-12 | success_candidate_4C_watch | ESS pivot is Stage 2; EV plant restart uncertainty and utilization risk require 4C-watch. |
| r3_loop10_skon_flatiron_lfp_ess_order | SK Innovation / SK On | success_candidate |  |  |  | success_candidate | First LFP ESS order is Stage 2; contract value, utilization, OPM and FCF required before Green. |
| r3_loop10_samsung_sdi_gm_indiana_ev_jv | Samsung SDI | success_candidate |  |  |  | success_candidate_demand_watch | JV localization is Stage 2; GM demand cut and 2027 production timing block Green until utilization/margin/FCF confirm. |
| r3_loop10_lg_chem_toyota_cathode_derisking | LG Chem | success_candidate |  |  |  | success_candidate | Ownership derisking is Stage 2; cathode volume, customer offtake, OPM and FCF required before Green. |
| r3_loop10_hanwha_qcells_uflpa_supply_chain_watch | Hanwha Solutions / Qcells | success_candidate |  |  | 2025-11-01 | success_candidate_thesis_break_watch | Solar localization is Stage 2; UFLPA/customs disruption and furloughs create 4C-watch. |
| r3_loop10_ev_supply_chain_ford_shock_skiet_ecopro | SK IE Technology / EcoPro Materials / battery supply-chain basket | 4c_thesis_break |  |  | 2025-12-01 | thesis_break_watch | Ford EV retreat and hybrid pivot hit Korean battery supply chain; separator/precursor Green requires utilization and demand confirmation. |
| r3_loop10_posco_future_m_lnf_lithium_event | POSCO Future M / L&F | event_premium |  | 2025-08-11 |  | cyclical_success_event_premium | Lithium event is not Stage 3 without company-level call-off, OPM, FCF and inventory quality. |
| r3_loop10_hyundai_hydrogen_fuel_cell_capex | Hyundai Motor hydrogen fuel-cell plant | success_candidate |  |  |  | success_candidate | Hydrogen capex is Stage 2; utilization, orders, margin and FCF required before Green. |

## Interpretation
- LGES and SK On ESS pivots are valid Stage 2 watch items, not Green before utilization, OPM and FCF.
- Samsung SDI/GM and Hyundai hydrogen plant show why CAPEX/JV alone is not Stage 3.
- LG Chem/Toyota cathode derisking is useful Stage 2 evidence, but offtake and margin still matter.
- Qcells, SKIET and EcoPro Materials illustrate R3 4C-watch from customs disruption and EV demand shock.
- POSCO Future M / L&F lithium rally is a commodity event premium, not structural rerating.

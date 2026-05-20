# Round 285 R3 Loop 14 Secondary Battery EV Green Energy Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_285.md
- round_id: round_213
- large_sector: SECONDARY_BATTERY_EV_GREEN_ENERGY
- cases: 8
- Stage 3 dated candidates: 0
- stage4b_watch: 2
- stage4c_watch: 5
- hard_4c: 1
- hard_4c_watch: 4
- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r3_loop14_lges_ford_freudenberg_contract_cancellation_hard_4c | LG Energy Solution Ford/Freudenberg cancellation | hard 4C |  |  |  | 2025-12-26 | thesis_break | LGES is the hard 4C reference: contract value without customer call-off and utilization can disappear. |
| r3_loop14_samsung_sdi_gm_jv_stage2_ev_demand_watch | Samsung SDI GM JV EV-demand watch | success_candidate + 4C-watch | 2024-08-28 |  |  | 2025-03-05 | success_candidate_4C_watch | Samsung SDI/GM is Stage 2, but EV demand and operating losses block Green until utilization and margin appear. |
| r3_loop14_sk_innovation_skon_restructuring_ess_pivot | SK Innovation / SK On restructuring ESS pivot | success_candidate_policy_restructuring + 4C-watch | 2024-08-27 |  | 2025-09-03 | 2025-12-11 | success_candidate_restructuring_but_4C_watch | SK On needs ESS value, delivery, margin and loss reversal before the pivot can become structural. |
| r3_loop14_battery_material_supply_chain_ford_beta | EcoPro Materials / SK IE Technology / SK Innovation / LGES | 4C-watch |  |  |  | 2025-12-16 | thesis_break_watch | Battery-material suppliers need customer BEV volume and battery content, not only EV long-term growth. |
| r3_loop14_hanwha_qcells_solar_policy_customs_gate | Hanwha Solutions / Qcells solar policy customs gate | success_candidate + 4C-watch | 2024-08-08 |  |  | 2025-11-08 | success_candidate_4C_watch | Qcells needs customs clearance, component flow and factory utilization after policy support. |
| r3_loop14_hyundai_hydrogen_fuel_cell_capex_stage2 | Hyundai Motor hydrogen fuel-cell capex | success_candidate + capex gate | 2025-10-30 |  |  |  | success_candidate_but_capex_gate | Hydrogen capex is not customer demand; Green waits for utilization and unit economics. |
| r3_loop14_sk_group14_silicon_anode_stage2 | SK / Group14 silicon anode scale-up | success_candidate + insufficient evidence | 2025-08-20 |  |  |  | success_candidate_but_insufficient_evidence | Unlisted battery-material scale-up cannot become listed-stock Green without an explicit value bridge. |
| r3_loop14_korean_battery_ess_pivot_cross_reference | LGES / Samsung SDI / SK On ESS pivot basket | success_candidate + 4B-watch | 2025-09-03 |  | 2025-09-03 |  | success_candidate_4B_watch | ESS is a possible next-cycle path, but Green needs PO value, shipment, installation, margin and repeat orders. |

## Interpretation
- LGES Ford/Freudenberg cancellation is the R3 hard 4C reference.
- Samsung SDI/GM and SK On/ESS are Stage 2 examples, not Green, until call-off, utilization and margin close.
- Battery-material suppliers need customer model mix and battery content checks; EV long-term growth is not enough.
- Qcells, Hyundai hydrogen and SK/Group14 show policy/capex/funding evidence that remains below Green until utilization and unit economics confirm.

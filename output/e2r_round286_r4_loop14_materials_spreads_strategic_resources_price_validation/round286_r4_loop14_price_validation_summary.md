# Round 286 R4 Loop 14 Materials Spreads Strategic Resources Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_286.md
- round_id: round_214
- large_sector: MATERIALS_SPREADS_STRATEGIC_RESOURCES
- cases: 9
- Stage 3 dated candidates: 0
- stage4b_watch: 5
- stage4c_watch: 4
- hard_4c: 1
- hard_4c_watch: 3
- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r4_loop14_lotte_lgchem_petrochemical_spread_collapse | Lotte Chemical / LG Chem petrochemical spread collapse | failed_rerating + 4C-watch |  |  |  | 2025-02-07 | thesis_break_watch | Petrochemical oversupply is a RedTeam gate until spread, utilization and cash margin recover. |
| r4_loop14_lotte_hdhyundai_petrochemical_restructuring | Lotte Chemical / HD Hyundai Oilbank Daesan restructuring | success_candidate_policy_restructuring | 2026-02-24 |  | 2025-11-26 |  | success_candidate_policy_restructuring | Daesan restructuring is useful Stage 2 evidence, not Green before actual shutdown discipline and spread recovery. |
| r4_loop14_hyundai_posco_steel_spread_antidumping | Hyundai Steel / POSCO steel anti-dumping relief | event_premium_policy_relief | 2025-02-20 |  | 2025-02-20 | 2024-06-21 | event_premium_policy_relief | Steel anti-dumping relief is useful, but Green needs physical demand, ASP/spread and export risk control. |
| r4_loop14_korea_zinc_strategic_metal_control_premium | Korea Zinc / Young Poong strategic metal control premium | event_premium_4B_watch | 2024-09-13 |  | 2024-09-13 |  | event_premium_4B_watch | Korea Zinc is a control-premium price case; operating Green needs smelter margin, governance and dilution checks. |
| r4_loop14_posco_minres_lithium_resource_integration | POSCO / Mineral Resources lithium resource integration | success_candidate_resource_integration | 2025-11-11 |  | 2025-11-11 |  | success_candidate_but_price_data_unavailable | POSCO lithium resource integration needs offtake and processing utilization before it becomes structural evidence. |
| r4_loop14_posco_future_m_lnf_lithium_squeeze_rally | POSCO Future M / L&F / battery basket lithium squeeze | event_premium_lithium_squeeze | 2025-08-11 |  | 2025-08-11 |  | event_premium_lithium_squeeze | Lithium squeeze rallies need customer volume, ASP, pass-through and inventory checks before Green. |
| r4_loop14_lnf_tesla_4680_cathode_contract_collapse | L&F Tesla 4680 cathode contract collapse | hard 4C | 2023-01-01 |  |  | 2025-12-29 | thesis_break | L&F is the R4 hard 4C reference: signed contract value is not durable evidence without call-off. |
| r4_loop14_rare_earth_export_control_supply_chain | Korea strategic-materials basket rare-earth export controls | 4C-watch |  |  |  | 2025-10-22 | thesis_break_watch | Rare-earth controls should feed RedTeam and supply-chain 4C-watch, not automatic beneficiary scoring. |
| r4_loop14_lg_chem_cathode_supply_chain_rebalancing | LG Chem cathode supply-chain rebalancing | success_candidate_nonbinding_watch | 2025-09-08 |  |  |  | success_candidate_nonbinding_watch | LG Chem cathode rebalancing needs binding lithium terms, Tennessee ramp, customer call-off and margin. |

## Interpretation
- Petrochemical spread collapse and L&F contract collapse are thesis-break references, not Green inputs.
- Steel anti-dumping, lithium squeeze and Korea Zinc control premium are event-premium or 4B-watch unless FCF evidence appears.
- POSCO lithium integration, Daesan restructuring and LG Chem cathode rebalancing are Stage 2 candidates until utilization, binding terms, call-off and margin close.
- Rare-earth export controls are RedTeam supply-chain overlays; actual license and shipment continuity must be verified.

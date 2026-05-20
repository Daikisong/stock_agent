# Round 247 R4 Loop 11 Materials Spread Strategic Resources Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_247.md
- round_id: round_175
- large_sector: MATERIALS_SPREAD_STRATEGIC
- cases: 8
- success_candidate: 4
- event_premium: 1
- failed_rerating: 2
- hard_4c: 1
- Stage 3 dated cases: 0
- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r4_loop11_korea_zinc_critical_minerals_governance | Korea Zinc | success_candidate_governance_watch | 2026-03-12 |  |  | 2025-12-16 | success_candidate_governance_watch | Strategic minerals are Stage 2; FID/offtake/margin/FCF and governance/dilution must clear before Green. |
| r4_loop11_lotte_hd_petrochemical_restructuring | Lotte Chemical / HD Hyundai Chemical | failed_rerating_restructuring_relief | 2026-02-24 |  |  |  | failed_rerating_then_restructuring_watch | Capacity shutdown/support is Stage 2 relief; spread, OPM and FCF recovery required for Green. |
| r4_loop11_yncc_standalone_ncc_credit_watch | Yeochun NCC / DL Chemical / Hanwha Solutions exposure | 4C-watch |  |  |  | 2025-08-27 | thesis_break_watch | Weak financials and standalone NCC exposure require 4C-watch, not restructuring Green. |
| r4_loop11_hyundai_posco_steel_tariff_two_sided | Hyundai Steel / POSCO Holdings | event_premium_4C-watch | 2025-02-20 |  |  | 2025-06-02 | event_premium_tariff_4c_watch | Anti-dumping relief helps domestic spread but export tariff risk blocks Green until spread/margin/FCF confirm. |
| r4_loop11_lg_chem_toyota_cathode_derisking | LG Chem | success_candidate | 2025-09-09 |  |  |  | success_candidate | Ownership derisking is Stage 2; cathode volume, customer offtake, OPM and FCF required before Green. |
| r4_loop11_posco_minres_lithium_resource_security | POSCO Holdings / MinRes lithium JV | success_candidate_cyclical_watch | 2025-11-11 |  |  |  | success_candidate_cyclical_watch | Resource security is Stage 2; downstream margin, offtake economics and FCF required before Green. |
| r4_loop11_oci_non_china_polysilicon_spacex_watch | OCI Holdings / OCI TerraSus | success_candidate_event_premium | 2025-06-07 |  | 2026-04-14 |  | success_candidate_event_premium | U.S. expansion is Stage 2; unconfirmed SpaceX report is event premium until contract/offtake/margin/FCF confirm. |
| r4_loop11_lnf_tesla_cathode_contract_hard_4c | L&F | 4C-thesis-break |  |  |  | 2025-12-29 | thesis_break | Customer name and contract headline cannot be Green without actual call-off and volume/margin conversion. |

## Interpretation
- Korea Zinc is strategic-minerals Stage 2 plus governance/dilution watch, not Green before FID, offtake, margin and FCF.
- Petrochemical restructuring is relief unless product spread, OPM and FCF recover.
- YNCC is standalone NCC credit 4C-watch, not a restructuring winner.
- Steel policy is two-sided: domestic anti-dumping relief and export tariff risk must both be considered.
- LG Chem/Toyota and POSCO/MinRes are Stage 2 supply-chain/resource-security cases, not Green before margin and offtake.
- OCI is Stage 2 optionality, while the SpaceX item is unconfirmed media/event premium.
- L&F remains the hard 4C anchor for customer-name/material-contract false positives.

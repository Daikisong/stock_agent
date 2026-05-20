# Round 234 R4 Loop 10 Materials Spread Strategic Resources Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_234.md
- large_sector: MATERIALS_SPREAD_STRATEGIC
- cases: 8
- success_candidate: 3
- cyclical_success: 1
- event_premium: 1
- failed_rerating: 2
- hard_4c: 1
- Stage 3 dated cases: 0
- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r4_loop10_korea_zinc_strategic_minerals_governance | Korea Zinc | success_candidate | 2026-03-12 |  | 2026-03-12 | 2025-12-16 | success_candidate_governance_watch | Strategic minerals are Stage 2; dilution, governance, offtake and FCF must clear before Stage 3. |
| r4_loop10_lotte_hd_petrochemical_restructuring | Lotte Chemical / HD Hyundai Chemical | failed_rerating | 2026-02-24 |  |  |  | failed_rerating_then_restructuring_watch | Capacity shutdown/support is Stage 2 relief; spread, OPM and FCF recovery required for Green. |
| r4_loop10_sk_innovation_soil_refining_cycle | SK Innovation / S-Oil | cyclical_success | 2026-05-13 |  |  |  | cyclical_success | Refining rebound is cyclical; Stage 3 requires multi-quarter margin floor, FCF, deleveraging and battery-loss control. |
| r4_loop10_posco_minres_lithium_jv | POSCO Holdings / MinRes lithium JV | success_candidate | 2025-11-11 |  |  |  | success_candidate_cyclical_watch | Lithium mine stake is Stage 2; Stage 3 requires offtake economics, downstream margin and FCF. |
| r4_loop10_hyundai_steel_policy_capex_rebar_4c | Hyundai Steel | failed_rerating | 2025-03-25 |  |  | 2025-04-22 | false_positive_score_prevention | Tariff-hedge capex and weak rebar demand block Green; funding/margin clarity required. |
| r4_loop10_lnf_tesla_cathode_contract_hard_4c | L&F | 4c_thesis_break |  |  |  | 2025-12-29 | thesis_break | Customer name and contract headline cannot be Green without actual call-off, volume and margin conversion. |
| r4_loop10_oci_non_china_polysilicon_spacex_watch | OCI Holdings | success_candidate | 2025-06-07 |  | 2026-04-14 |  | success_candidate_event_premium | U.S. expansion is Stage 2; unconfirmed SpaceX report is event premium until contract terms, margin and FCF confirm. |
| r4_loop10_poongsan_hanwha_mna_rumor_fade | Poongsan | event_premium |  |  | 2026-04-03 | 2026-04-09 | event_premium | M&A rumor faded in six days; Stage 3 requires confirmed transaction or copper/ammunition margin and FCF. |

## Interpretation
- Korea Zinc is strategic-minerals Stage 2, but governance/dilution/offtake/FCF block Green.
- Lotte Chemical restructuring is relief, not Green before spread, OPM and FCF recovery.
- SK Innovation / S-Oil refining rebound is cyclical Stage 2 because battery drag and margin durability remain.
- POSCO lithium JV is resource-security Stage 2, but lithium cycle and downstream margin still matter.
- Hyundai Steel is false-positive prevention for policy CAPEX without funding and margin clarity.
- L&F is the hard 4C anchor: customer name and contract headline failed after value collapse.
- OCI and Poongsan separate real capacity/options from unconfirmed media or M&A event premium.

# Round 266 R10 Loop 12 Construction Real Estate Materials Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_266.md
- analyst_round_id: round_194
- large_sector: CONSTRUCTION_REAL_ESTATE_MATERIALS
- cases: 8
- success_candidate: 3
- event_premium: 2
- safety_hard_reference_count: 1
- hard_4c_case_count: 1
- direct_listed_hard_4c_case_count: 0
- Stage 3 dated cases: 0
- 4B-watch cases: 6
- 4C-watch cases: 3
- full_adjusted_ohlc_complete: false

## Case Matrix

| case | company | type | round type | stage2 | stage3 | 4B | 4C | hard 4C | direct listed hard 4C | round alignment | note |
|---|---|---|---|---|---|---|---|---|---|---|---|
| r10_loop12_czech_nuclear_preferred_bid_legal_watch | Doosan Enerbility / KEPCO E&C / KEPCO Plant S&E / Hyundai E&C read-through | success_candidate | success_candidate_plus_legal_4c_watch | 2024-07-17 |  | 2024-07-17 | 2024-08-27 | false | false | success_candidate_legal_4C_watch | Preferred bidder is Stage 2; final contract, legal clearance, listed-company scope, margin and cash collection required before Green. |
| r10_loop12_hyundai_ec_bulgaria_kozloduy_talks | Hyundai E&C | success_candidate | success_candidate_insufficient_price_data | 2024-02-23 |  | 2024-02-23 |  | false | false | success_candidate_but_insufficient_price_data | Parliament nod and talks are Stage 2; final EPC value, scope, margin, financing and payment schedule required. |
| r10_loop12_hyundai_engineering_anseong_bridge_collapse | Hyundai Engineering / Anseong bridge collapse | 4c_thesis_break | construction_safety_hard_reference |  |  |  | 2025-02-25 | true | false | thesis_break_reference | Fatal collapse is sector hard 4C reference; Hyundai Engineering is not directly listed. |
| r10_loop12_posco_dl_recurring_fatal_accident_regulation | POSCO E&C / DL Construction safety read-through | 4c_thesis_break | recurring_fatal_accident_regulatory_4c_watch |  |  |  | 2025-09-15 | false | false | thesis_break_watch | Repeated fatality regulation is 4C-watch; safety execution must override backlog and policy-score. |
| r10_loop12_seoul_housing_ltv_supply_policy | Seoul housing policy / construction basket | event_premium | event_premium_policy_watch | 2025-09-07 |  | 2025-09-07 |  | false | false | event_premium_policy_watch | Policy mix is Stage 2; presales, margin, PF stability, unsold inventory and FCF required before Green. |
| r10_loop12_sejong_presidential_office_public_infra | Sejong presidential office public-infra basket | event_premium | event_premium_insufficient_evidence | 2026-04-14 |  | 2026-04-14 |  | false | false | event_premium_insufficient_evidence | Public-infra headline is not Green without listed contractor, contract value, margin and cash collection. |
| r10_loop12_daewoo_ec_nghi_son_lng_candidate | Daewoo E&C / Nghi Son LNG candidate | success_candidate | success_candidate_insufficient_evidence | 2024-08-21 |  | 2024-08-21 |  | false | false | success_candidate_but_insufficient_evidence | Consortium candidate is not award; EPC scope, value, margin, financing and offtake required before Green. |
| r10_loop12_hyundai_steel_rebar_construction_demand_break | Hyundai Steel / rebar proxy | 4c_thesis_break | building_material_4c_watch |  |  | 2024-06-21 | 2024-06-21 | false | false | thesis_break_watch | Weak construction demand and rebar-price decline block building-material Green until spread, inventory and FCF recover. |

## Interpretation
- Czech nuclear is strong Stage 2 plus legal 4C-watch, not Green before final contract and legal clearance.
- Bulgaria Kozloduy is Stage 2 pipeline evidence; talks are not a final EPC contract.
- Anseong bridge collapse is an unlisted but sector-level hard safety reference.
- POSCO E&C / DL safety regulation is recurring fatality 4C-watch.
- Seoul housing policy is event premium until presales, margin, PF and unsold inventory confirm.
- Sejong presidential office is public-infra headline until listed award and contract value exist.
- Nghi Son LNG is a consortium option until award, EPC scope, financing and offtake confirm.
- Hyundai Steel rebar weakness is building-material demand 4C-watch.

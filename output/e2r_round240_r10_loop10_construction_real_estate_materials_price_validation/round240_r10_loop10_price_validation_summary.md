# Round 240 R10 Loop 10 Construction Real Estate Materials Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_240.md
- analyst_round_id: round_168
- large_sector: CONSTRUCTION_REAL_ESTATE_MATERIALS
- cases: 8
- success_candidate: 3
- event_premium: 1
- Stage 3 dated cases: 0
- 4B-watch cases: 6
- 4C-watch cases: 3
- hard_4c_case_count: 2
- full_ohlc_complete: false

## Case Matrix

| case | company | type | round_type | stage2 | stage3 | 4B | 4C | hard 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|---|---|
| r10_loop10_czech_nuclear_infra_korea_epc | 두산에너빌리티/한전기술/한전KPS/한국전력 | success_candidate | success_candidate_legal_watch | 2025-06-04 |  | 2024-07-17 | 2025-05-06 | false | success_candidate_legal_watch | Preferred bidder to signed contract is Stage 2; supplier package, margin and cash collection required before Green. |
| r10_loop10_daewoo_enc_grand_faw_port_delivery | 대우건설 | success_candidate | success_candidate_infrastructure_delivery | 2024-11-12 |  |  |  | false | success_candidate | Dock completion is stronger than an order headline, but additional backlog, margin and cash collection are required before Stage 3. |
| r10_loop10_seoul_housing_policy_supply_watch | 서울 주택공급/대출규제 건설 바스켓 | event_premium | event_premium_policy_watch | 2025-09-07 |  | 2025-09-07 |  | false | event_premium_policy_watch | Housing policy is Stage 1/2; presales, margin, PF stability and FCF are required before Green. |
| r10_loop10_taeyoung_pf_credit_hard_4c | 태영건설/건설 PF 스트레스 | 4c_thesis_break | hard_4c_pf_credit_break |  |  |  | 2024-05-13 | true | thesis_break | Debt reschedule and PF delinquency spike are hard 4C; liquidity support is relief, not Green. |
| r10_loop10_hyundai_engineering_bridge_collapse_sector_hard_4c | 현대엔지니어링 교량 붕괴 섹터 케이스 | 4c_thesis_break | sector_hard_4c_direct_listed_mapping_unclear |  |  |  | 2025-02-25 | true | thesis_break | Fatal bridge collapse is sector hard 4C; direct listed mapping is unclear. |
| r10_loop10_posco_dl_construction_safety_regulation | 포스코이앤씨/DL건설 안전 규제 | 4c_thesis_break | 4c_watch_recurring_fatality_regulation |  |  |  | 2025-09-15 | false | thesis_break_watch | Recurring fatal accidents and site shutdowns require 4C-watch and safety-trust gate. |
| r10_loop10_ai_data_center_real_asset_event | SK/AWS·OpenAI·삼성 데이터센터 real asset | success_candidate | success_candidate_event_premium | 2025-10-01 |  | 2025-06-20 |  | false | event_premium_success_candidate | AI data-center investment is Stage 1/2; tenant, NOI/AFFO, power/water/permitting and capex per share required before Green. |
| r10_loop10_hyundai_steel_rebar_construction_demand_watch | 현대제철/철근 건설수요 proxy | 4c_thesis_break | 4c_watch_building_material_demand_cycle |  |  |  | 2024-06-21 | false | thesis_break_watch | Rebar and construction-demand weakness block building-material Green until demand, spread and margin stabilize. |

## Interpretation
- Czech nuclear and Grand Faw Port are Stage 2 evidence, not automatic Green.
- Seoul housing policy and AI data-center events stay event/policy premium until company-level cash-flow evidence appears.
- PF credit break and fatal construction accident are hard 4C references.
- Workplace safety regulation and Hyundai Steel rebar weakness are 4C-watch blockers for R10 Green.

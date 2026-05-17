# Round-133 R1 Loop-8 Industrial Orders / Infrastructure Summary

- source_round: `docs/round/round_133.md`
- large_sector: `INDUSTRIAL_ORDERS_INFRA`
- loop: `R1 Loop 8 / v8.0`
- target_count: 24
- case_candidate_count: 28
- base_score_component_count: 7
- stage_cap_count: 5
- score_stage_price_alignment_count: 9
- structural_success_count: 1
- success_candidate_count: 11
- cyclical_success_count: 0
- event_premium_count: 3
- failed_rerating_count: 3
- stage4b_case_count: 4
- stage4c_case_count: 7
- green_possible_count: 5
- watch_yellow_first_count: 12
- redteam_first_count: 7
- hard_gate_target_count: 5
- production_scoring_changed: false
- case_records_are_candidate_generation_input: false

## Interpretation

- R1 Loop 8 narrows order/backlog candidates after the R13 Loop-7 RedTeam pass.
- Order size is not enough. Green needs contract amount, duration, counterparty, delivery schedule, margin, OP/EPS revision, FCF conversion, and price-path alignment.
- Loop 8 makes score-to-stage-to-price validation explicit: Stage 2 contracts are not Stage 3 until OP/EPS/FCF, margin, and price path line up.
- Loop 8 base score weights are EPS/FCF 25, visibility 22, bottleneck/pricing 18, mispricing 10, valuation room 7, capital discipline 10, information confidence 8.
- Loop 8 keeps EHV transformer export, backlog-to-FCF conversion, grid-flexibility context, nuclear restart approval gates, and data-center power/water gates.
- Example: transformer shortage is strong, but low-margin long-term contracts or data-center project delay can still block Green.
- Example: GE Vernova is score-to-stage-to-price aligned, but its large rerating requires 4B-watch.
- Example: LS Electric 525kV and Hyundai Rotem Morocco rail are Stage 2 until price, margin, OP/EPS, and FCF are backfilled.
- Example: defense backlog can be strong, but share issuance and unclear overseas CAPEX are capital-allocation shocks.
- Example: OpenDART list-only contract evidence is capped until amount, counterparty, duration, and margin detail are checked.
- Example: existing nuclear PPA and SMR policy are separated because cashflow visibility is different.

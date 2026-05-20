# Round 281 R12 Loop 13 Agriculture Life Service Other Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_281.md
- round_id: round_209
- large_sector: AGRICULTURE_LIFE_SERVICE_OTHER
- cases: 9
- success_candidate: 4
- event_premium: 2
- failed_rerating: 2
- hard_reference: 1
- hard_4c: 1
- direct_listed_hard_4c: 0
- Stage 3 dated cases: 0
- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r12_loop13_kimchi_cabbage_climate_food_input_cost | CJ CheilJedang / Daesang / Pulmuone food-input basket | 4C-watch |  |  |  | 2024-10-23 | thesis_break_watch | Food inflation headline is not Green without pass-through and margin stability. |
| r12_loop13_feed_wheat_tender_livestock_cost_watch | Harim / Easy Bio / livestock-feed basket | 4C-watch |  |  |  | 2026-05-13 | thesis_break_watch | Grain-cost event is a margin gate, not automatic livestock/feed Green. |
| r12_loop13_poultry_egg_birdflu_supply_shock | Harim / poultry and egg-food processors | event_premium + 4C-watch | 2025-06-23 |  | 2025-04-03 | 2025-06-09 | event_premium_4C_watch | Disease and import-policy shock can be both price support and cost/regulatory risk. |
| r12_loop13_daedong_tym_agri_machinery_labor_substitution | Daedong / TYM | success_candidate + insufficient_evidence |  |  |  |  | success_candidate_but_insufficient_evidence | Aging-farm theme is not Green until orders, dealer inventory, financing cost, FX and margin confirm. |
| r12_loop13_cj_logistics_shinsegae_alliance_unit_economics | CJ Logistics | success_candidate + evidence_good_but_price_failed | 2024-06-17 |  |  |  | evidence_good_but_price_failed | Revenue uplift estimate is Stage 2; logistics unit economics, automation productivity and cost control required. |
| r12_loop13_coupang_life_service_trust_break_reference | Coupang / Naver / E-Mart / CJ Logistics read-through | hard_4C_reference + competitor_event_premium | 2026-02-25 |  |  | 2026-02-25 | thesis_break_reference | Life-service trust break can move users/spending; competitor read-through is not automatic Green. |
| r12_loop13_waste_recycling_food_waste_rfid_platform | KJ Environment / Korean food-waste RFID system | success_candidate_policy_infra | 2025-12-18 |  |  |  | success_candidate_policy_infra | Recycling policy and infra scale are Stage 2; tipping fee, utilization, permit and FCF required. |
| r12_loop13_birthrate_rebound_childcare_education_event | Childcare / baby / education-service basket | event_premium + structural_watch | 2026-02-25 |  |  |  | event_premium_structural_watch | Birthrate rebound is not company Green until enrolment, ARPU, retention and margin confirm. |
| r12_loop13_dn_solutions_other_manufacturing_tools_ipo | DN Solutions | success_candidate + IPO_4B_watch | 2025-04-14 |  |  |  | success_candidate_IPO_4B_watch | IPO size and end-market exposure are Stage 2; listed demand, order book, export margin and tariff pass-through required. |

## Interpretation
- Cabbage and feed wheat are input-cost gates, not automatic food or livestock winners.
- Poultry/egg shortage is two-sided because disease, import rules and tariff risk travel with the price spike.
- Daedong/TYM need order backlog and dealer sell-through before Stage 3 review.
- CJ Logistics has Stage 2 contract evidence, but unit economics and margin remain open.
- Coupang is the R12 life-service trust hard reference; competitor read-through is not automatic Green.
- Waste/RFID and birthrate are Stage 2 policy/demographic evidence until fee, utilization, enrolment, ARPU and FCF close.
- DN Solutions IPO is a quality gate; IPO size is not aftermarket demand or margin evidence.

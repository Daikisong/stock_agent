# Round 268 R12 Loop 12 Agriculture / Life Service / Misc Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_268.md
- analyst_round_id: round_196
- raw_large_sector_label: AGRI_LIFE_SERVICE_MISC
- large_sector: EDUCATION_LIFE_AGRI_MISC
- cases: 8
- success_candidate: 2
- event_premium: 2
- failed_rerating: 3
- overheat: 1
- price_moved_without_evidence: 3
- Stage 3 dated cases: 0
- 4B-watch cases: 8
- 4C-watch cases: 4
- hard_4c_case_count: 0
- full_ohlc_complete: false

## Case Matrix

| case | company | type | round_type | stage2 | stage3 | 4B | 4C | hard 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|---|---|
| r12_loop12_nongshim_shin_export_capacity | Nongshim | success_candidate | structural_success_candidate_k_food_export_capacity | 2024-05-27 |  |  |  | false | success_candidate_but_price_data_unavailable | K-food export structure is strong Stage 2; Green requires overseas sell-through, capacity utilization, margin, FCF and price path. |
| r12_loop12_kimchi_cabbage_input_cost_watch | Daesang / CJ CheilJedang / kimchi processors | failed_rerating | 4c_watch_cabbage_climate_input_cost |  |  |  | 2024-10-23 | false | thesis_break_watch | Cabbage climate/input shock is 4C-watch unless processors prove pass-through and inventory control. |
| r12_loop12_feed_wheat_livestock_cost_watch | Harim / Farm Story / Maniker / feed-livestock basket | failed_rerating | 4c_watch_feed_wheat_cost |  |  |  | 2026-05-13 | false | thesis_break_watch | Feed wheat cost is 4C-watch for feed/livestock names until price pass-through and feed inventory buffer confirm. |
| r12_loop12_medical_quota_private_education_event | Megastudy / YBMNet / NE Neungyule / education basket | event_premium | event_premium_policy_watch | 2026-02-10 |  |  | 2025-03-07 | false | event_premium_policy_watch | Medical quota is Stage 2; paid enrollment, ARPU, repeat course, OPM and cash conversion required before Green. |
| r12_loop12_ai_textbook_edtech_policy_rollback | Woongjin Thinkbig / YBMNet / edtech basket | failed_rerating | 4c_watch_edtech_policy_rollback |  |  |  | 2025-08-04 | false | thesis_break_watch | AI education theme is blocked by policy rollback, teacher-preparation gap and classroom device restrictions. |
| r12_loop12_childcare_foreign_helper_fertility_policy | Childcare / foreign housekeeper / fertility basket | success_candidate | success_candidate_policy_event | 2026-02-25 |  |  |  | false | success_candidate_policy_event | Policy and fertility rebound are Stage 2; paid household demand, utilization, margin and cash conversion required before Green. |
| r12_loop12_dog_meat_ban_pet_welfare_transition | Dog-meat ban / pet-welfare transition basket | event_premium | event_premium_policy_watch | 2027-02-01 |  |  |  | false | event_premium_policy_watch | Dog-meat ban transition is policy event; pet-food/service revenue conversion and shelter capacity required before Green. |
| r12_loop12_kyochon_cherrybro_neuromeka_jensen_event | Kyochon F&B / Cherrybro / Neuromeka | overheat | overheat_price_moved_without_evidence |  |  | 2025-10-31 |  | false | price_moved_without_evidence | Celebrity food-service event is 4B/event premium until same-store sales, franchise margin and repeat demand confirm. |

## Interpretation
- Nongshim is K-food export Stage 2, not Green until sell-through, margin, FCF and price path close.
- Cabbage and feed-wheat shocks are input-cost 4C-watch cases.
- Medical quota, childcare, and pet-welfare policies are event/policy candidates until paid conversion and utilization appear.
- AI textbook rollback and classroom device restrictions block edtech Green.
- Jensen chicken event is price_moved_without_evidence: price moved before same-store sales or franchise margin evidence.
- Easy example: `fertility rebound + childcare basket rally` is watch; `paid service usage + utilization + margin + cash conversion` is needed before deeper Stage review.

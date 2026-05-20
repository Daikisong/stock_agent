# Round 255 R12 Loop 11 Agri Life Service Misc Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_255.md
- analyst_round_id: round_183
- raw_large_sector_label: AGRI_LIFE_SERVICE_MISC
- mapped_large_sector: EDUCATION_LIFE_AGRI_MISC
- cases: 8
- success_candidate: 2
- event_premium: 2
- failed_rerating: 3
- overheat: 1
- price_moved_without_evidence: 1
- Stage 3 dated cases: 0
- 4B-watch cases: 8
- 4C-watch cases: 3
- hard_4c_case_count: 0
- deep_sub_archetype_count: 8
- shadow_weight_row_count: 8
- r12_default_stage3_bias: conservative_except_verified_recurring_service
- full_ohlc_complete: false

## Case Matrix

| case | company | type | round_type | stage2 | stage3 | 4B | 4C | round alignment | note |
|---|---|---|---|---|---|---|---|---|---|
| r12_loop11_coway_recurring_rental_insufficient | Coway | success_candidate | structural_success_candidate_recurring_rental |  |  |  |  | success_candidate_but_insufficient_evidence | Recurring rental structure is R12 Stage 3 candidate, but rental accounts, churn, ARPU, OPM/FCF and OHLC are required. |
| r12_loop11_medical_quota_private_education_watch | Medical quota / private education basket | event_premium | event_premium_policy_watch | 2026-02-10 |  |  |  | event_premium_policy_watch | Medical quota is Stage 1/2; paid enrollment, repeat course, ARPU, OPM and cash conversion required before Green. |
| r12_loop11_edtech_ai_textbook_rollback_phone_ban | Edtech / AI textbook / classroom device regulation basket | failed_rerating | 4c_watch_edtech_policy_friction |  |  |  | 2025-08-01 | thesis_break_watch | AI education theme is blocked by textbook rollback and classroom-device regulation until actual school adoption and revenue are proven. |
| r12_loop11_childcare_fertility_policy_watch | Fertility / childcare / care-service basket | success_candidate | success_candidate_event_premium_demographic_policy | 2025-02-26 |  |  |  | success_candidate_event_premium | Fertility rebound and care policy are Stage 2; paid demand, utilization, margin and recurring revenue required before Green. |
| r12_loop11_kimchi_cabbage_input_cost_watch | Kimchi cabbage / agri-food input cost basket | failed_rerating | 4c_watch_food_input_cost |  |  |  | 2024-10-23 | thesis_break_watch | Cabbage climate/input shock is 4C-watch unless food processors prove pass-through and margin stability. |
| r12_loop11_feed_wheat_livestock_input_cost_watch | Feed wheat / livestock input-cost basket | failed_rerating | 4c_watch_feed_cost |  |  |  | 2026-05-13 | thesis_break_watch | High feed-wheat cost is 4C-watch for feed/livestock processors until pass-through and inventory quality confirm. |
| r12_loop11_dog_meat_ban_pet_welfare_transition | Dog-meat ban / pet-welfare transition basket | event_premium | event_premium_policy_watch | 2027-02-01 |  |  |  | event_premium_policy_watch | Dog-meat ban transition is Stage 1/2 policy event; pet-food/service revenue conversion required before Green. |
| r12_loop11_kyochon_cherrybro_neuromeka_jensen_event | Kyochon F&B / Cherrybro / Neuromeka | overheat | overheat_price_moved_without_evidence |  |  | 2025-10-31 |  | price_moved_without_evidence | Celebrity fried-chicken event is 4B/event premium until store traffic, same-store sales, franchise margin and repeat demand confirm. |

## Interpretation
- R12 Green needs recurring revenue, paid conversion, unit economics, price pass-through, and cash conversion.
- Coway is the cleanest recurring-service watch case, but accounts/churn/ARPU/FCF and OHLC are missing.
- Medical quota, fertility, and pet-welfare policies are Stage 1/2 routing signals until company revenue converts.
- AI textbook rollback, cabbage shock, and feed wheat cost are 4C-watch inputs.
- Jensen fried-chicken event is the clean price_moved_without_evidence example.

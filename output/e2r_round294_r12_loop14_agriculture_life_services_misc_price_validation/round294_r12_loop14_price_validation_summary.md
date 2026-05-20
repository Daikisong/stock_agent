# Round 294 R12 Loop 14 Agriculture Life Services Misc Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_294.md
- round_id: round_222
- large_sector: AGRICULTURE_LIFE_SERVICES_MISC
- cases: 8
- success_candidate: 4
- event_premium: 1
- watch_counterexample: 3
- hard_reference: 1
- direct_KRX_hard_4c_confirmed: false
- sector_hard_reference_confirmed: true
- Stage 3 dated cases: 0
- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r12_loop14_daedong_tym_agri_equipment_export_cycle | Daedong / TYM | 4C-watch | 2026-02-01 |  |  | 2024-11-08 | thesis_break_watch | Korean tractor export thesis needs farm income, dealer inventory, orders, export ASP and margin. |
| r12_loop14_food_input_cost_inflation_basket | CJ CheilJedang / Pulmuone / CJ Freshway / food-service basket | 4C-watch |  |  |  | 2025-12-01 | thesis_break_watch | Food input inflation is not pricing power unless pass-through, volume retention and margin confirm. |
| r12_loop14_fried_chicken_jensen_huang_meme_rally | Kyochon F&B / Cherrybro / Neuromeka | price_moved_without_evidence |  |  | 2025-10-31 |  | price_moved_without_evidence | Celebrity/AI visit moved stocks without same-store sales, royalty, or input-cost margin evidence. |
| r12_loop14_naver_uber_baemin_food_delivery_consolidation | Naver / Uber / Baemin / Delivery Hero | success_candidate_stage2 | 2026-05-18 |  |  |  | success_candidate_policy_deal_stage2 | Food-delivery M&A scale needs approval, take-rate, rider cost, merchant churn and integration economics. |
| r12_loop14_delivery_labor_service_continuity_reference | CJ Logistics / Hanjin / Coupang read-through | service_continuity_reference |  |  |  | 2025-06-03 | thesis_break_reference | Delivery speed moat needs labor continuity, service reliability and unit economics. |
| r12_loop14_waste_recycling_infra_stage2 | Insun ENT / KC Green / KJ Environment read-through | success_candidate_stage2 + 4C-watch | 2024-08-16 |  |  | 2024-11-22 | success_candidate_4C_watch | Waste infra EV is Stage 2; recycling yield, gate fee, utilization and cleanup-liability control are Green gates. |
| r12_loop14_birthrate_childcare_infant_goods_stage2 | Agabang / Zero to Seven / childcare and infant-goods read-through | success_candidate_stage2 | 2026-02-25 |  |  |  | success_candidate_demographic_stage2 | Birthrate rebound is Stage 2; actual sales, customer count, ARPU, subsidy capture and margin required. |
| r12_loop14_private_education_hagwon_demand_stage2 | MegaStudy Education / Chungdahm / private-education basket | success_candidate_stage2 + demographic_policy_4C_watch | 2025-03-16 |  |  | 2025-03-16 | success_candidate_4C_watch | Private education demand is strong but demographic burden and policy/regulatory risk remain. |

## Interpretation
- Daedong/TYM are agri-equipment export-cycle watch cases until global demand, dealer inventory, order and margin data turn.
- Food input inflation is a margin gate, not automatic pricing power.
- Jensen fried-chicken rally is price moved without evidence because Kkanbu is not listed and same-store sales were absent.
- Baemin/Naver/Uber is Stage 2 until approval, take-rate, rider cost and merchant churn are visible.
- Delivery labor pause is a service-continuity reference for logistics and quick-commerce moats.
- Waste/recycling is Stage 2 plus 4C-watch until yield, gate fee, utilization and cleanup liability close.
- Birthrate and hagwon demand are Stage 2 signals, but Green needs customer count, ARPU, margin, retention and policy durability.

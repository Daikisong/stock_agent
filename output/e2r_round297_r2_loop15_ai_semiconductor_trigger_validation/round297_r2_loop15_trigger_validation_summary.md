# Round 297 R2 Loop 15 AI/Semiconductor Trigger-Level Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_297.md
- round_id: round_225
- large_sector: AI_SEMICONDUCTOR_ELECTRONIC_PARTS
- method: trigger_level_backtest_v1
- cases: 8
- triggers: 10
- Stage2-Actionable candidates: 6
- Stage3-Yellow candidates: 4
- Stage3-Green candidates: 2
- Stage3-Green confirmed: 0
- 4B watch cases: 3
- 4C watch cases: 5
- price_validation_completed: partial_with_reported_event_price_anchors
- full_adjusted_ohlc_complete: false

## Case Matrix

| case | company | best trigger | candidate | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|
| r2_loop15_sk_hynix_hbm_first_mover | SK Hynix | T1/T2 | Stage2-Actionable_to_Stage3-Yellow_to_Green_candidate | 2025-09-12 | 2025-09-01 | missed_structural_if_old_gate_used | SK Hynix should not wait until record profit day; 2024 HBM mix, OP revision, mass production and relative strength were earlier triggers. |
| r2_loop15_hanmi_semiconductor_hbm_equipment | Hanmi Semiconductor | T1 | Stage2-Actionable_to_Stage3-Yellow_candidate |  |  | Stage2_promote_candidate | Named customer, named equipment, repeated wins and strong relative strength justify Stage2-Actionable, but not Green before revenue and margin. |
| r2_loop15_samsung_electronics_hbm_catchup_labor_watch | Samsung Electronics | T2/T3 | Stage2-Actionable_to_Stage3-Yellow_candidate |  | 2026-05-19 | Stage2-Actionable_but_not_Green | Samsung catch-up is investable research evidence, but it is not SK Hynix-style first-mover Green without allocation and labor continuity. |
| r2_loop15_sk_hynix_openai_asml_4b | SK Hynix | T1_before_full_4B | Stage3-Green_candidate_plus_4B-watch | 2026-03-24 |  | aligned_if_stage3_plus_4B_overlay_allowed | OpenAI and ASML validate demand, but after a parabolic move they must be written as Green candidate plus 4B overlay. |
| r2_loop15_memory_china_equipment_export_control | Samsung / SK Hynix / Hanmi / Hana Micron | T1 | 4C-watch |  | 2025-09-01 | thesis_break_watch | AI memory thesis can remain intact, but China fab equipment access is a separate 4C overlay. |
| r2_loop15_lg_innotek_apple_ai_upgrade | LG Innotek | T1 | Stage2-Actionable_to_Stage3-Yellow_pending_sellthrough |  | 2024-11-01 | Stage2_promote_candidate | Apple AI device upgrade plus OP estimate beat and +19% relative strength justify Stage2-Actionable, not Green before sell-through. |
| r2_loop15_lg_display_apple_oled_recovery | LG Display | T1_pending_price | Stage2 |  |  | evidence_good_but_price_data_incomplete | Apple OLED and loss beat are Stage2 evidence, but profitability guidance and price validation are missing. |
| r2_loop15_samsung_labor_supply_chain_4c | Samsung Electronics | T2 | 4C-watch |  | 2026-05-19 | thesis_break_watch | Labor continuity is a memory supply-chain 4C overlay even when the AI memory cycle is strong. |

## Interpretation
- SK Hynix is the key missed-structural case if HBM mix, OP revision and mass-production triggers stay plain Stage2.
- Hanmi Semiconductor shows named customer + HBM equipment + repeat order + relative strength can be Stage2-Actionable.
- Samsung Electronics is late catch-up; relative-strength discount and labor 4C overlay block Green.
- OpenAI/Stargate and ASML validate memory demand, but after a parabolic rally they require 4B overlay.
- Export-control and labor continuity are explicit 4C overlays in the AI-memory cycle.
- LG Innotek is Stage2-Actionable; LG Display remains Stage2 until sustained profitability and price validation appear.

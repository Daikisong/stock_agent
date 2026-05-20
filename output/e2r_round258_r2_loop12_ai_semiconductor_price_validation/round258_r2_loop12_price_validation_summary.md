# Round 258 R2 Loop 12 AI Semiconductor Electronics Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_258.md
- round_id: round_186
- large_sector: AI_SEMICONDUCTOR_ELECTRONICS
- cases: 8
- structural_success: 1
- success_candidate: 5
- event_premium: 1
- failed_rerating: 1
- hard_4c_case_count: 0
- Stage 3 dated cases: 1
- 4B-watch cases: 7
- price_moved_without_evidence: 2
- evidence_good_but_price_failed: 1
- price_data_unavailable: 2
- target_archetype_count: 8
- shadow_weight_row_count: 8
- full_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r2_loop12_sk_hynix_hbm4_structural_success_4b | SK Hynix | structural_success | 2025-09-12 | 2025-10-29 | 2026-05-14 |  | aligned_but_now_4B | HBM sold-out, HBM4, OP, EUV, packaging이 연결된 Stage 3 benchmark지만 현재는 massive MFE로 4B-watch다. |
| r2_loop12_samsung_hbm4_foundry_labor_export_watch | Samsung Electronics | success_candidate | 2026-01-25 |  | 2026-05-06 | 2025-09-01 | success_candidate_4C_watch | HBM4/foundry catch-up Stage 2지만 shipment/margin과 노동·중국 fab 리스크가 Green을 막는다. |
| r2_loop12_hanmi_hbm_bonder_order_rumor_4b | Hanmi Semiconductor | success_candidate | 2024-03-01 |  | 2024-03-28 | 2025-09-01 | success_candidate_4B_watch | 확정 SK하이닉스 주문은 Stage 2지만 Micron 미확정 보도 +22%는 4B-watch다. |
| r2_loop12_gaonchips_pfn_ai_design_house | Gaonchips | success_candidate | 2024-07-09 |  |  |  | success_candidate_but_insufficient_price_data | Design win은 Stage 2다. tape-out·양산·매출·마진 전 Green이 아니다. |
| r2_loop12_lg_innotek_apple_ai_aeva_lidar | LG Innotek | success_candidate | 2024-06-12 |  | 2024-06-12 |  | success_candidate_event_premium | Apple AI와 lidar optionality는 Stage 2다. 실제 물량·ASP·module margin·FCF가 필요하다. |
| r2_loop12_lg_display_lcd_exit_oled_turnaround | LG Display | success_candidate | 2024-07-25 |  |  |  | success_candidate_but_evidence_incomplete | 적자 축소와 LCD exit는 Stage 2다. 지속 OLED 이익·FCF·부채 감소 전 Green은 보류다. |
| r2_loop12_jusung_mirae_cxmt_relief_watch | Jusung Engineering / Mirae Corp | event_premium | 2024-12-03 |  |  | 2024-12-03 | event_premium_4C_watch | CXMT relief는 Green이 아니라 export-control relief다. 중국 고객 집중과 재규제 리스크가 남는다. |
| r2_loop12_export_control_overlay_samsung_skh_hana_hanmi | Samsung / SK Hynix / Hana Micron / Hanmi export-control basket | failed_rerating |  |  |  | 2025-09-01 | thesis_break_watch | 수출통제는 긍정 후보가 아니라 4C-watch overlay다. license denial이나 매출/기술 훼손 확인 전 hard 4C는 아니다. |

## Interpretation
- R2 Stage 3 is not `AI semiconductor beneficiary`. It needs confirmed customer order, generation transition, capacity bottleneck, shipment/revenue, margin, EPS/FCF revision, and post-evidence price path.
- SK Hynix remains the structural success benchmark, but current state is 4B-watch after massive reported return and market-cap milestone.
- Samsung, Hanmi, Gaonchips, LG Innotek, and LG Display show why catch-up, rumor, design win, optionality, and restructuring must stay Stage 2 until revenue/margin/FCF gates close.
- Export-control and labor disruption are 4C-watch overlays; this round does not force hard 4C without license denial, production halt, revenue impairment, or technology impairment.

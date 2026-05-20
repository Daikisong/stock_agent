# Round 245 R2 Loop 11 AI Semiconductor Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_245.md
- round_id: round_173
- large_sector: AI_SEMICONDUCTOR_ELECTRONICS
- cases: 8
- structural_success: 1
- success_candidate: 3
- event_premium: 3
- failed_rerating: 1
- hard_4c_case_count: 0
- Stage 3 dated cases: 1
- 4B-watch cases: 7
- price_moved_without_evidence: 3
- evidence_good_but_price_failed: 2
- target_archetype_count: 12
- shadow_weight_row_count: 9
- full_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r2_loop11_sk_hynix_euv_packaging_4b | SK Hynix | structural_success | 2024-06-25 | 2024-06-25 | 2026-05-14 |  | aligned_now_4B_watch | HBM/EUV/advanced packaging confirms structural success; current state is 4B-watch after massive reported MFE. |
| r2_loop11_samsung_hbm_foundry_strike_export_ip_watch | Samsung Electronics | success_candidate | 2025-07-28 |  |  | 2025-09-01 | success_candidate_4c_watch | Samsung has Stage 2 foundry/HBM evidence, but volume/margin/EPS plus labor/export/IP risks must clear before Green. |
| r2_loop11_hanmi_hbm_bonder_confirmed_order_rumor_4b | Hanmi Semiconductor | success_candidate | 2024-03-01 |  | 2024-03-28 |  | aligned_candidate_4B_watch | Confirmed SK Hynix order is good Stage 2 evidence; unconfirmed Micron media report is 4B-watch. |
| r2_loop11_jusung_mirae_cxmt_supplier_relief | Jusung Engineering / Mirae Corp | event_premium | 2024-12-03 |  |  | 2024-12-03 | event_premium_4C_watch | CXMT exclusion relief is Stage 2 event, not Green; export-control durability and customer diversification are required. |
| r2_loop11_gaonchips_pfn_design_win | Gaonchips | success_candidate | 2024-07-09 |  |  |  | unknown_insufficient_evidence | Design win is Stage 2; tape-out, mass production, revenue and margin are required for Stage 3. |
| r2_loop11_db_hitek_policy_foundry | DB HiTek / policy foundry exposure | event_premium |  |  |  |  | event_premium_policy_watch | Government foundry consultation is Stage 1/2, not company Green. |
| r2_loop11_hanwha_precision_hbm_equipment_spinoff | Hanwha Precision Machinery / Hanwha Aerospace spin-off exposure | event_premium | 2024-04-05 |  | 2024-04-05 |  | event_premium | HBM equipment optionality via spin-off is Stage 2/corporate-action event; order/revenue/margin are required before Green. |
| r2_loop11_export_control_ip_leak_redteam | Samsung/SK Hynix/Hana Micron/Hanmi export-control and IP-leak basket | failed_rerating |  |  |  | 2025-09-01 | thesis_break_watch | Export-control and IP leakage are R2 4C-watch; hard 4C requires production/revenue/competitive impairment confirmation. |

## Interpretation
- R2 Stage 3 is not `AI semiconductor beneficiary`. It requires customer order, HBM generation transition, CAPA bottleneck, margin, EPS/FCF revision, and post-evidence price path.
- SK Hynix remains a structural success benchmark, but after very large reported returns it is now 4B-watch.
- Samsung, Hanmi, Gaonchips, and DB HiTek show why confirmed order, design win, MoU, policy, and rumor must be separated.
- Export-control, labor disruption, and IP leakage are strong 4C-watch overlays, but this round does not force hard 4C without production/revenue/competitive impairment proof.

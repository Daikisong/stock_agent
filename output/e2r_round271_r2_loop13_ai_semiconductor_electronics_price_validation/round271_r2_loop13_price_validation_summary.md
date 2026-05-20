# Round 271 R2 Loop 13 AI Semiconductor Electronics Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_271.md
- round_id: round_199
- large_sector: AI_SEMICONDUCTOR_ELECTRONICS
- cases: 8
- structural_success: 1
- success_candidate: 3
- event_premium: 1
- failed_rerating: 2
- overheat: 1
- hard_4c_case_count: 0
- Stage 3 dated cases: 1
- 4B-watch cases: 7
- 4C-watch cases: 2
- price_data_unavailable: 1
- price_moved_without_evidence: 3
- aligned: 1
- full_adjusted_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r2_loop13_sk_hynix_hbm_success_now_4b | SK Hynix | structural_success_4B_watch | 2024-07-11 | 2024-07-24 | 2026-05-14 |  | aligned_but_now_4B | SK Hynix는 R2 structural success benchmark지만, 현재는 신규 Green보다 4B-watch다. |
| r2_loop13_samsung_hbm_lag_labor_4c_watch | Samsung Electronics | success_candidate_thesis_break_watch | 2024-07-05 |  |  | 2025-07-30 | success_candidate_plus_thesis_break_watch | 메모리 회복은 Stage 2지만 HBM lag, China curbs, 노동 리스크가 Green을 막는다. |
| r2_loop13_hanwha_precision_hbm_equipment_carveout | Hanwha Precision Machinery / Hanwha Aerospace parent | failed_rerating_success_candidate | 2024-04-05 |  | 2024-04-05 |  | failed_rerating_stage2 | HBM 장비 분사는 Stage 2지만 실제 장비 주문·매출 bridge 전에는 Green이 아니다. |
| r2_loop13_rebellions_sapeon_ai_chip_merger | Rebellions / Sapeon Korea | success_candidate_insufficient_price_data | 2024-08-18 |  |  |  | success_candidate_but_insufficient_price_data | 비상장 AI chip 합병은 Stage 2지만 상장사 EPS bridge 전에는 Green이 아니다. |
| r2_loop13_teraview_kosdaq_semiconductor_inspection_ipo | TeraView | overheat_success_candidate | 2025-12-08 |  | 2025-12-08 |  | overheat_success_candidate | 검사장비 story는 Stage 2지만 600x 청약과 P/E 40x는 납품·마진 전 4B다. |
| r2_loop13_korea_state_foundry_policy | Korea state-private foundry policy basket | success_candidate_policy_relief | 2025-12-10 |  |  |  | success_candidate_policy_relief | 정책 foundry는 Stage 2 relief지만 operator, utilization, 고객계약 전 Green이 아니다. |
| r2_loop13_nvidia_blackwell_korea_ai_infra | Nvidia Blackwell Korea AI infrastructure buyers | success_candidate_event_premium | 2025-10-31 |  |  |  | success_candidate_event_premium | Blackwell 칩을 사는 이벤트는 Stage 2다. 생산성·cloud revenue·capex ROI 전에는 EPS 증거가 아니다. |
| r2_loop13_china_fab_export_control_basket | Samsung / SK Hynix / Hana Micron / Hanmi China-fab export-control basket | 4C-watch |  |  |  | 2025-09-01 | thesis_break_watch | 중국 fab 수출통제는 hard 4C 확정은 아니지만 R2 Green을 막는 강한 4C-watch다. |

## Interpretation
- R2 Stage 3 is not the word AI, HBM, foundry, inspection equipment, IPO, policy, or Blackwell.
- SK Hynix remains the clean structural success benchmark, but current state is 4B-watch.
- Samsung recovery is Stage 2 while HBM lag, China curbs and labor strike risk remain open.
- Hanwha Precision, Rebellions/Sapeon, TeraView and Korea foundry policy are Stage 2/watch items before orders, utilization, margin and revenue bridge.
- Nvidia Blackwell Korea supply is AI-infra consumption, not Korean listed-company EPS proof by itself.
- China fab export-control is 4C-watch, not hard 4C until license denial or revenue impairment confirms.

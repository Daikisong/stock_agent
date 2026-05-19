# Round 219 R2 Loop 9 AI Semiconductor Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_219.md
- large_sector: AI_SEMICONDUCTOR_ELECTRONICS
- cases: 7
- structural_success: 1
- success_candidate: 3
- event_premium: 1
- 4B watch cases: 4
- 4C watch cases: 2
- hard_4c: 0
- reported_price_anchor_count: 5
- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C-watch | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r2_loop9_sk_hynix_hbm4_stage3_4b | SK하이닉스 | structural_success | 2024-06-25 | 2024-06-25 | 2026-05-04 |  | aligned | HBM dominance, HBM4 first mover and EPS revision produced large MFE; now it is 4B-watch/elevated, not a fresh Green. |
| r2_loop9_samsung_hbm_catchup_labor_watch | 삼성전자 | success_candidate | 2025-10-02 |  | 2026-05-06 | 2026-05-15 | unknown | Samsung has AI memory recovery and OpenAI demand validation, but HBM volume/margin proof is still needed and labor risk is 4C-watch. |
| r2_loop9_hanmi_hbm_bonder_confirmed_vs_rumor | 한미반도체 | success_candidate | 2024-03-26 |  | 2024-03-28 |  | aligned | Confirmed SK Hynix HBM equipment order is Stage 2/3 candidate evidence, but the Micron rumor rally is 4B-watch. |
| r2_loop9_gaonchips_pfn_design_win | 가온칩스 | success_candidate | 2024-07-09 |  |  |  | unknown | Design win is Stage 2; tape-out, mass production, revenue and margin are required for Stage 3. |
| r2_loop9_db_hitek_policy_foundry | DB하이텍 | event_premium |  |  |  |  | unknown | Government foundry consultation is Stage 1/2 attention, not company-level Green evidence. |
| r2_loop9_openai_stargate_memory_4b | SK하이닉스/삼성전자 | 4b_watch | 2025-10-02 |  | 2025-10-02 |  | aligned | Demand validation for leaders, but 4B-watch after large rerating; laggard Green is forbidden without company revenue and margin. |
| r2_loop9_export_control_china_fab_watch | Samsung/SK Hynix/Hana Micron/Hanmi | failed_rerating |  |  |  | 2025-09-01 | unknown | Export-control shock is 4C-watch; hard 4C requires confirmed production or revenue disruption. |

## Interpretation
- SK하이닉스는 HBM4/EPS revision 이후 큰 가격경로가 확인되지만 현재는 4B-watch/elevated다.
- 삼성전자는 OpenAI event와 Q3 OP 회복으로 Stage 2 후보지만 HBM volume/margin 전 Green은 보류한다.
- 한미반도체는 확인된 SK하이닉스 장비 수주는 좋지만 Micron 미확정 보도 +22%는 4B-watch다.
- 가온칩스 design win과 DB하이텍 foundry 정책 이벤트는 매출·마진 전 Stage 1~2로 제한한다.
- OpenAI/Stargate는 수요 검증이지만 후발주 Green 충분조건이 아니다.
- export-control과 labor risk는 hard 4C가 아니라 4C-watch로 두고 실제 생산/매출 차질 확인을 기다린다.

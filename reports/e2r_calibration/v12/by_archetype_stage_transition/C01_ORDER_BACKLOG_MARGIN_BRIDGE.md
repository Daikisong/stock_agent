# C01_ORDER_BACKLOG_MARGIN_BRIDGE Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `16`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C01_R1L87_044450_KSS_SHIPPING_BACKLOG_THEME | 044450 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| C01_R1L87_082740_HANWHA_ENGINE_ORDER_BACKLOG_MARGIN | 082740 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 9570.0 | None | None | 91.64 | None | stage2_actionable_best_entry |
| C01_R1L87_097230_HJ_SHIPBUILDING_BACKLOG_THEME | 097230 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| C01_R1L91_267270_2024_07_16 | 267270 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| C01_R1L96_210540_2024_02_01 | 210540 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 12600.0 | None | None | 10.5 | None | stage2_captured_most_upside |
| C01_R1L96_241560_2024_07_24 | 241560 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| C01_R1L96_267270_2024_02_01 | 267270 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 51700.0 | None | None | 32.5 | None | stage2_captured_most_upside |
| C01_R1L99_010660_2024_02_01 | 010660 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 3280.0 | None | None | 195.7 | None | stage2_captured_most_upside |
| C01_R1L99_054540_2024_02_01 | 054540 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 3985.0 | None | None | 53.3 | None | stage2_captured_most_upside |
| C01_R1L99_082740_2024_02_01 | 082740 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 8360.0 | None | None | 105.3 | None | stage2_captured_most_upside |
| R1L92_C01_DAECHANGSOL_2024_LNG_EQUIPMENT_THEME_FALSE_STAGE2 | 096350 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 464.0 | None | None | 16.38 | None | stage2_actionable_best_entry |
| R1L92_C01_HANWHAENGINE_2024_SHIP_ENGINE_ORDER_BACKLOG_MARGIN_BRIDGE_POSITIVE | 082740 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 9950.0 | None | None | 84.32 | None | stage2_actionable_best_entry |
| R1L92_C01_SEJINHEAVY_2024_SHIP_BLOCK_EVENT_CAP_4B | 075580 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | 9850.0 | None | None | 4b_good_peak_capture |
| R1L96_C01_CAPE_2024_SHIP_PARTS_ORDER_BACKLOG_FALSE_STAGE2 | 064820 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 5770.0 | None | None | 12.65 | None | stage2_actionable_best_entry |
| R1L96_C01_HANWHAENGINE_2024_SHIP_ENGINE_ORDER_BACKLOG_MARGIN_POSITIVE | 082740 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 11000.0 | None | None | 56.0 | None | stage2_actionable_best_entry |
| R1L96_C01_WOORIMPTS_2024_INDUSTRIAL_GEAR_EVENT_CAP_4B | 101170 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | 8390.0 | None | None | 4b_good_peak_capture |

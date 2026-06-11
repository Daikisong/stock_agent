# C01_ORDER_BACKLOG_MARGIN_BRIDGE Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `19`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C01_R1L111_000720_20240126 | 000720 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 33100.0 | None | None | 8.76 | None | stage2_captured_most_upside |
| C01_R1L111_006360_20240430 | 006360 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 16480.0 | None | None | 31.98 | None | stage2_actionable_best_entry |
| C01_R1L111_012450_20240214 | 012450 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| C01_R1L111_028050_20240228 | 028050 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 26000.0 | None | None | 8.27 | None | stage2_actionable_best_entry |
| C01_R1L111_047810_20240306 | 047810 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 53000.0 | None | None | 28.0 | None | stage2_actionable_best_entry |
| C01_R1L111_064350_20240222 | 064350 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 34500.0 | None | None | 97.1 | None | stage2_actionable_best_entry |
| C01_R1L111_079550_20240214 | 079550 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| C01_R1L112_004960_20240429_STAGE2_STATIC_TO_50_08 | 004960 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 6550.0 | None | None | 2.29 | None | stage2_captured_most_upside |
| C01_R1L112_012450_20240227_STAGE3GREEN_STATIC_TO_50_01 | 012450 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | 179100.0 | None | None | None | green_good_but_late |
| C01_R1L112_013580_20240429_STAGE2ACTIONABLE_STATIC_TO_50_07 | 013580 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 13700.0 | None | None | 13.07 | None | stage2_actionable_best_entry |
| C01_R1L112_016250_20240130_STAGE2_STATIC_TO_50_10 | 016250 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 18470.0 | None | None | 3.46 | None | stage2_captured_most_upside |
| C01_R1L112_033100_20240502_4BLOCALWATCH_STATIC_TO_50_12 | 033100 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | 76000.0 | None | None | no_valid_stage_transition |
| C01_R1L112_047040_20240717_4BLOCALWATCH_STATIC_TO_50_06 | 047040 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | 4355.0 | None | None | no_valid_stage_transition |
| C01_R1L112_053690_20240130_STAGE2_STATIC_TO_50_09 | 053690 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 19010.0 | None | None | 6.79 | None | stage2_captured_most_upside |
| C01_R1L112_064350_20240329_STAGE3YELLOW_STATIC_TO_50_03 | 064350 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| C01_R1L112_079550_20240306_STAGE4B_STATIC_TO_50_02 | 079550 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | 168500.0 | None | None | no_valid_stage_transition |
| C01_R1L112_272210_20240618_STAGE2_STATIC_TO_50_04 | 272210 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 21700.0 | None | None | 39.17 | None | stage2_captured_most_upside |
| C01_R1L112_294870_20240424_STAGE2ACTIONABLE_STATIC_TO_50_05 | 294870 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 17670.0 | None | None | 59.59 | None | stage2_actionable_best_entry |
| C01_R1L112_298040_20240328_STAGE2ACTIONABLE_STATIC_TO_50_11 | 298040 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 255000.0 | None | None | 109.0 | None | stage2_actionable_best_entry |

# C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `50`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 000720 | 000720 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 33100.0 | None | None | 8.8 | None | stage2_actionable_best_entry |
| 002990 | 002990 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| 004960 | 004960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| 006360 | 006360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 15640.0 | None | 15630.0 | 39.071 | -0.1636 | stage2_actionable_best_entry |
| 009410 | 009410 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| 014790 | 014790 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | 2010.0 | None | None | no_valid_stage_transition |
| 028050 | 028050 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| 047040 | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 4015.0 | None | 4250.0 | 23.7 | 24.6964 | stage2_actionable_best_entry |
| 294870 | 294870 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 17530.0 | None | 17920.0 | 60.8711 | 3.6549 | stage2_actionable_best_entry |
| 375500 | 375500 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 36650.0 | None | None | 7.779 | None | stage2_captured_most_upside |
| C30_P1_001 | 294870 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| C30_P1_002 | 006360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 15150.0 | None | None | 33.1 | None | stage2_actionable_best_entry |
| C30_P1_003 | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 4260.0 | None | None | 20.1 | None | stage2_captured_most_upside |
| C30_P1_004 | 000720 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| C30_P1_005 | 375500 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 38100.0 | None | None | 22.8 | None | stage2_actionable_best_entry |
| C30_P1_006 | 009410 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| C30_P1_007 | 004960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 6730.0 | None | None | 31.2 | None | stage2_captured_most_upside |
| C30_P1_008 | 013580 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 13960.0 | None | None | 12.8 | None | stage2_actionable_best_entry |
| C30_P1_009 | 005960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| C30_P1_010 | 002990 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 4040.0 | None | None | 8.5 | None | stage2_captured_most_upside |
| C30_P1_011 | 014790 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 2380.0 | None | None | 18.6 | None | stage2_actionable_best_entry |
| C30_P1_012 | 010780 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| C30_P1_013 | 003070 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 10300.0 | None | None | 13.5 | None | stage2_captured_most_upside |
| C30_P1_014 | 035890 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 1370.0 | None | None | 25.4 | None | stage2_actionable_best_entry |
| C30_P1_015 | 001470 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| C30_P1_016 | 002460 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 9480.0 | None | None | 20.9 | None | stage2_captured_most_upside |
| C30_P1_017 | 002780 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 1290.0 | None | None | 12.4 | None | stage2_captured_most_upside |
| C30_P1_018 | 013360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 1470.0 | None | None | 14.6 | None | stage2_actionable_best_entry |
| C30_P1_019 | 002410 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| C30_P1_020 | 028050 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 27000.0 | None | None | 24.1 | None | stage2_actionable_best_entry |
| C30_R10L100_002990_KUMHO_WEAK_LIQUIDITY_DECAY | 002990 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 5030.0 | None | None | 5.0 | None | stage2_actionable_best_entry |
| C30_R10L100_006360_20240403 | 006360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 15630.0 | None | None | 39.16 | None | stage2_actionable_best_entry |
| C30_R10L100_047040_20240403 | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 3805.0 | None | None | 6.44 | None | stage2_captured_most_upside |
| C30_R10L100_047040_DAEWOO_DELAYED_REBOUND | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 4015.0 | None | 4250.0 | 23.7 | 24.6964 | stage2_actionable_best_entry |
| C30_R10L100_294870_20240126 | 294870 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 17530.0 | None | 26700.0 | 66.003 | 79.2544 | stage2_actionable_best_entry |
| C30_R10L102_000720_20240126 | 000720 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 33100.0 | None | None | 8.76 | None | stage2_actionable_best_entry |
| C30_R10L102_006360_20240430 | 006360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 16480.0 | None | None | 31.98 | None | stage2_actionable_best_entry |
| C30_R10L102_028050_20240228 | 028050 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 26000.0 | None | None | 8.27 | None | stage2_actionable_best_entry |
| C30_R10L102_375500_20240429 | 375500 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 36650.0 | None | None | 7.78 | None | stage2_actionable_best_entry |
| C30_R10L104_004960_20240429 | 004960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 6550.0 | None | None | 2.29 | None | stage2_captured_most_upside |
| C30_R10L104_013580_20240429 | 013580 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 13700.0 | None | None | 13.07 | None | stage2_actionable_best_entry |
| C30_R10L104_047040_20240717 | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | 4355.0 | None | None | no_valid_stage_transition |
| C30_R10L104_294870_20240424 | 294870 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 17670.0 | None | None | 59.59 | None | stage2_actionable_best_entry |
| C30_R10L104_375500_20240613 | 375500 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | 39500.0 | None | None | no_valid_stage_transition |
| C30_R10L105_000720_20240126 | 000720 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 33100.0 | None | None | 8.76 | None | stage2_actionable_best_entry |
| C30_R10L105_006360_20240430 | 006360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 16480.0 | None | None | 31.98 | None | stage2_actionable_best_entry |
| C30_R10L105_028050_20240228 | 028050 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 26000.0 | None | None | 8.27 | None | stage2_actionable_best_entry |
| C30_R10L105_047040_20240403 | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 3805.0 | None | None | 6.44 | None | stage2_captured_most_upside |
| C30_R10L105_294870_20240826 | 294870 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | 26700.0 | None | None | no_valid_stage_transition |
| C30_R10L105_375500_20240429 | 375500 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 36650.0 | None | None | 7.78 | None | stage2_actionable_best_entry |

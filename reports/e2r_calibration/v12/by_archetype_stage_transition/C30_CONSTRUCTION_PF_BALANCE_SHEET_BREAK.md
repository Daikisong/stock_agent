# C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `32`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C30-R10-L100-001 | 006360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| C30-R10-L100-002 | 294870 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | 4c_too_late |
| C30-R10-L100-003 | 005960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| C30-R10-L100-004 | 035890 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 1319.0 | None | None | 27.37 | None | stage2_actionable_best_entry |
| C30-R10-L100-005 | 002990 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | 4810.0 | None | None | no_valid_stage_transition |
| C30_002990_20240327_pf_policy_proxy_false_positive | 002990 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 4520.0 | None | None | 5.75 | None | stage2_captured_most_upside |
| C30_005960_20250204_false_hard4c_after_reset | 005960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| C30_010780_20250210_opm_inventory_gap | 010780 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 19420.0 | None | None | 28.22 | None | stage2_captured_most_upside |
| C30_014790_20240507_project_order_repair | 014790 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 2005.0 | None | None | 43.64 | None | stage2_actionable_best_entry |
| C30_014790_20241125_late_headline_4b | 014790 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | 2405.0 | None | None | 4b_too_early |
| C30_021320_20250321_financial_quality_repair | 021320 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 3960.0 | None | None | 55.56 | None | stage2_actionable_best_entry |
| C30_035890_20240516_low_alpha_balance_quality | 035890 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 1360.0 | None | None | 23.53 | None | stage2_captured_most_upside |
| C30_CASE_01_034300 | 034300 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | 10580.0 | None | None | no_valid_stage_transition |
| C30_CASE_02_014790 | 014790 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| C30_CASE_03_010780 | 010780 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 25150.0 | None | None | 1.3917 | None | stage2_actionable_best_entry |
| C30_CASE_04_021320 | 021320 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | 4525.0 | None | None | no_valid_stage_transition |
| C30_CASE_05_000720 | 000720 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 35100.0 | None | None | 1.4245 | None | stage2_actionable_best_entry |
| C30_CASE_06_047040 | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| C30_CASE_07_375500 | 375500 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 35150.0 | None | None | 12.3755 | None | stage2_actionable_best_entry |
| C30_L208_01_004960_20240213 | 004960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | 7510.0 | None | None | no_valid_stage_transition |
| C30_L208_02_004960_20240517 | 004960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 6800.0 | None | None | 17.21 | None | stage2_captured_most_upside |
| C30_L208_03_097230_20241115 | 097230 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 2945.0 | None | None | 444.65 | None | stage2_actionable_best_entry |
| C30_L208_04_003070_20250319 | 003070 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| C30_L208_05_013120_20240322 | 013120 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 2765.0 | None | None | 5.06 | None | stage2_captured_most_upside |
| C30_L208_06_013120_20250325 | 013120 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| C30_L208_07_002460_20250320 | 002460 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 9660.0 | None | None | 41.61 | None | stage2_actionable_best_entry |
| C30_L208_08_013580_20250318 | 013580 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| C30_R10L124_006360_GS_GEOMDAN_REBUILD_COST_HARD_BREAK | 006360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| C30_R10L124_047040_DAEWOO_2025_Q1_PROFIT_BACKLOG_REPAIR | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 3520.0 | None | None | 63.64 | None | stage2_actionable_best_entry |
| C30_R10L124_047040_DAEWOO_RECORD_EARNINGS_NO_FOLLOW_THROUGH | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 4615.0 | None | None | 4.01 | None | stage2_actionable_best_entry |
| C30_R10L124_294870_HDC_GWANGJU_COLLAPSE_HARD_4C | 294870 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| C30_R10L124_375500_DLENC_COST_RATE_NET_CASH_REPAIR | 375500 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 31200.0 | None | 48200.0 | 91.35 | 59.6466 | stage2_actionable_best_entry |

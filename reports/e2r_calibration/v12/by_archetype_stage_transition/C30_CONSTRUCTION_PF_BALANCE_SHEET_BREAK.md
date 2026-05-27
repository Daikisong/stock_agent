# C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `18`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| R10L10_C30_000720_HDEC_2023_OVERSEAS_BACKLOG_BALANCE_SHEET_SAFE_HAVEN | 000720 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 38650.0 | None | None | 14.9 | None | stage2_actionable_best_entry |
| R10L10_C30_006360_GS_EC_2023_QUALITY_DEFECT_LEGAL_LOSS_BREAK | 006360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| R10L10_C30_028050_SAMSUNG_EA_2023_OVERSEAS_EPC_NET_CASH_PF_ESCAPE | 028050 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 25850.0 | None | None | 45.1373 | None | stage2_actionable_best_entry |
| R10L10_C30_294870_HDC_2022_COLLAPSE_LEGAL_THESIS_BREAK | 294870 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| R10L10_C30_DL_FALSE_GREEN | 375500 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | 4c_too_late |
| R10L10_C30_DL_FALSE_GREEN | None | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| R10L10_C30_GS_POS_4B | 006360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 16210.0 | None | None | 34.18 | None | stage2_actionable_best_entry |
| R10L10_C30_GS_POS_4B | None | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 16210.0 | None | None | 34.18 | None | stage2_actionable_best_entry |
| R10L10_C30_HDC_POS | 294870 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 17530.0 | None | None | 60.8702 | None | stage2_actionable_best_entry |
| R10L10_C30_HDC_POS | None | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 17530.0 | None | None | 60.87 | None | stage2_actionable_best_entry |
| R10L12_C30_006360_GS_GEOMDAN_REBUILD_20230706 | 006360 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| R10L12_C30_006360_GS_GEOMDAN_REBUILD_20230706 | None | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| R10L12_C30_047040_DAEWOO_PF_PANIC_20221031 | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| R10L12_C30_047040_DAEWOO_PF_PANIC_20221031 | None | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| R10L12_C30_294870_HDC_GWANGJU_COLLAPSE_20220112 | 294870 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| R10L12_C30_294870_HDC_GWANGJU_COLLAPSE_20220112 | None | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| R10L12_C30_375500_DLENC_PF_DISCOUNT_REVERSAL_20231010 | 375500 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |
| R10L12_C30_375500_DLENC_PF_DISCOUNT_REVERSAL_20231010 | None | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | None | None | None | None | None | no_valid_stage_transition |

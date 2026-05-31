# C01_ORDER_BACKLOG_MARGIN_BRIDGE Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `8`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C01_HDHE_20230413_GRID_ORDER_BACKLOG_MARGIN | 267260 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 45500.0 | None | None | 84.62 | None | stage2_actionable_best_entry |
| C01_LS_ELECTRIC_20240405_GRID_ORDER_MARGIN_BRIDGE | 010120 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 118600.0 | None | None | 131.45 | None | stage2_actionable_best_entry |
| C01_TAIHAN_20240513_CABLE_THEME_NO_MARGIN_BRIDGE | 001440 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 18110.0 | None | None | 15.68 | None | stage2_captured_most_upside |
| R1L14_C01_KSOE_PRICE_ONLY_4B_20230717 | 009540 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| R1L14_C01_KSOE_STAGE2_20230104 | 009540 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 74400.0 | None | None | 74.73 | None | stage2_actionable_best_entry |
| R1L14_C01_MIPO_PRICE_ONLY_4B_20240731 | 010620 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| R1L14_C01_MIPO_STAGE2_20240213 | 010620 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 62700.0 | None | None | 95.85 | None | stage2_actionable_best_entry |
| R1L14_C01_SHI_STAGE2_20230131 | 010140 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 5790.0 | None | None | 63.56 | None | stage2_actionable_best_entry |

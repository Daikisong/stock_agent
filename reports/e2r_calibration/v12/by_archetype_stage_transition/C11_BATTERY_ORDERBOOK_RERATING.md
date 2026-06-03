# C11_BATTERY_ORDERBOOK_RERATING Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `16`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 137400 | 137400 | C11_BATTERY_ORDERBOOK_RERATING | 53600.0 | None | None | 66.98 | None | stage2_actionable_best_entry |
| 217820 | 217820 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| 290670 | 290670 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| 299030 | 299030 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| 302430 | 302430 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| 372170 | 372170 | C11_BATTERY_ORDERBOOK_RERATING | 65400.0 | None | None | 39.91 | None | stage2_actionable_best_entry |
| R3L73_C11_003670_20230131_ORDERBOOK_SUCCESS | 003670 | C11_BATTERY_ORDERBOOK_RERATING | 224000.0 | None | 560000.0 | 209.825 | 71.4881 | 4b_good_peak_capture |
| R3L73_C11_247540_20231204_ORDERBOOK_COUNTER | 247540 | C11_BATTERY_ORDERBOOK_RERATING | 323000.0 | None | None | 9.6 | None | stage2_actionable_best_entry |
| R3L73_C11_348370_20240110_ORDERBOOK_RS_SUCCESS | 348370 | C11_BATTERY_ORDERBOOK_RERATING | 88200.0 | None | None | 347.28 | None | stage2_actionable_best_entry |
| R3L73_C11_393890_20240105_SEPARATOR_COUNTER | 393890 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| R3L76_C11_137400_20240221_BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE | 137400 | C11_BATTERY_ORDERBOOK_RERATING | 43500.0 | None | None | 105.75 | None | stage2_actionable_best_entry |
| R3L76_C11_299030_20240221_BATTERY_EQUIPMENT_ORDER_THEME_NO_DURABLE_MARGIN_BRIDGE | 299030 | C11_BATTERY_ORDERBOOK_RERATING | 62300.0 | None | None | 17.34 | None | stage2_actionable_best_entry |
| R3L76_C11_382840_20240221_BATTERY_FURNACE_EQUIPMENT_NO_BACKLOG_CASHFLOW_BRIDGE | 382840 | C11_BATTERY_ORDERBOOK_RERATING | 19110.0 | None | None | 8.06 | None | stage2_actionable_best_entry |
| R3L86-C11-01 | 006400 | C11_BATTERY_ORDERBOOK_RERATING | 391000.0 | None | None | 26.47 | None | stage2_actionable_best_entry |
| R3L86-C11-02 | 005070 | C11_BATTERY_ORDERBOOK_RERATING | 157100.0 | None | None | 23.68 | None | stage2_actionable_best_entry |
| R3L86-C11-03 | 001570 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |

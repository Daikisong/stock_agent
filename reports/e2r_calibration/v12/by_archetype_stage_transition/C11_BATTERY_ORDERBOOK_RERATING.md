# C11_BATTERY_ORDERBOOK_RERATING Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `9`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C11_ECOPROBM_2023_VERTICAL_ORDERBOOK_RERATING | 247540 | C11_BATTERY_ORDERBOOK_RERATING | 109200.0 | None | None | 434.8 | None | stage2_actionable_best_entry |
| C11_LNF_2023_TESLA_SINGLE_CUSTOMER_CALLOFF_RISK | 066970 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11_POSCOFUTUREM_2023_SDI_CATHODE_ORDERBOOK | 003670 | C11_BATTERY_ORDERBOOK_RERATING | 224000.0 | None | None | 209.825 | None | stage2_actionable_best_entry |
| CASE_R3L66_003670_POSCOFUTUREM_ORDERBOOK | 003670 | C11_BATTERY_ORDERBOOK_RERATING | 224000.0 | None | None | 209.82 | None | stage2_actionable_best_entry |
| CASE_R3L66_247540_ECOPROBM_ORDERBOOK | 247540 | C11_BATTERY_ORDERBOOK_RERATING | 114100.0 | None | None | 411.8442 | None | stage2_actionable_best_entry |
| CASE_R3L66_393890_WCP_SEPARATOR_COUNTER | 393890 | C11_BATTERY_ORDERBOOK_RERATING | 51200.0 | None | None | 70.9 | None | stage2_actionable_best_entry |
| R3L11_C11_247540_ECOPROBM | 247540 | C11_BATTERY_ORDERBOOK_RERATING | 315000.0 | None | None | 2.54 | None | stage2_actionable_best_entry |
| R3L11_C11_348370_ENCHEM | 348370 | C11_BATTERY_ORDERBOOK_RERATING | 84300.0 | None | None | 368.09 | None | stage2_actionable_best_entry |
| R3L11_C11_373220_LGES | 373220 | C11_BATTERY_ORDERBOOK_RERATING | 372000.0 | None | None | 19.35 | None | stage2_actionable_best_entry |

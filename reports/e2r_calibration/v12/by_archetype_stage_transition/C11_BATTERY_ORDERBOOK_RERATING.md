# C11_BATTERY_ORDERBOOK_RERATING Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `18`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C11_R3L107_002710_20240206_STAGE2 | 002710 | C11_BATTERY_ORDERBOOK_RERATING | 59500.0 | None | None | 41.8 | None | stage2_captured_most_upside |
| C11_R3L107_005070_20240216_STAGE4B | 005070 | C11_BATTERY_ORDERBOOK_RERATING | None | None | 175800.0 | None | None | no_valid_stage_transition |
| C11_R3L107_011790_20240405_STAGE2ACTIONABLE | 011790 | C11_BATTERY_ORDERBOOK_RERATING | 138100.0 | None | None | 44.82 | None | stage2_actionable_best_entry |
| C11_R3L107_020150_20240321_STAGE2ACTIONABLE | 020150 | C11_BATTERY_ORDERBOOK_RERATING | 47050.0 | None | None | 25.82 | None | stage2_actionable_best_entry |
| C11_R3L107_051910_20240216_STAGE4B | 051910 | C11_BATTERY_ORDERBOOK_RERATING | None | None | 504000.0 | None | None | no_valid_stage_transition |
| C11_R3L107_066970_20240322_STAGE2ACTIONABLE | 066970 | C11_BATTERY_ORDERBOOK_RERATING | 186100.0 | None | None | 6.93 | None | stage2_actionable_best_entry |
| C11_R3L107_078600_20240321_STAGE2ACTIONABLE | 078600 | C11_BATTERY_ORDERBOOK_RERATING | 83800.0 | None | None | 49.3 | None | stage2_actionable_best_entry |
| C11_R3L107_086520_20240202_STAGE4B | 086520 | C11_BATTERY_ORDERBOOK_RERATING | None | None | 540000.0 | None | None | no_valid_stage_transition |
| C11_R3L107_096770_20240129_STAGE2ACTIONABLE | 096770 | C11_BATTERY_ORDERBOOK_RERATING | 120300.0 | None | None | 8.81 | None | stage2_actionable_best_entry |
| C11_R3L107_121600_20240221_STAGE2ACTIONABLE | 121600 | C11_BATTERY_ORDERBOOK_RERATING | 134000.0 | None | None | 17.76 | None | stage2_actionable_best_entry |
| C11_R3L107_222080_20240312_STAGE4B | 222080 | C11_BATTERY_ORDERBOOK_RERATING | None | None | 14840.0 | None | None | no_valid_stage_transition |
| C11_R3L107_247540_20240122_STAGE4C | 247540 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11_R3L107_278280_20240221_STAGE4B | 278280 | C11_BATTERY_ORDERBOOK_RERATING | None | None | 95600.0 | None | None | no_valid_stage_transition |
| C11_R3L107_299030_20240308_STAGE4B | 299030 | C11_BATTERY_ORDERBOOK_RERATING | None | None | 67200.0 | None | None | no_valid_stage_transition |
| C11_R3L107_348370_20240115_STAGE2ACTIONABLE | 348370 | C11_BATTERY_ORDERBOOK_RERATING | 107000.0 | None | None | 268.69 | None | stage2_actionable_best_entry |
| C11_R3L107_361610_20240115_STAGE4C | 361610 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11_R3L107_373220_20240312_STAGE2ACTIONABLE | 373220 | C11_BATTERY_ORDERBOOK_RERATING | 419500.0 | None | None | 5.84 | None | stage2_actionable_best_entry |
| C11_R3L107_393890_20240213_STAGE4C | 393890 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |

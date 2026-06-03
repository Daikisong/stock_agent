# C13_BATTERY_JV_UTILIZATION_AMPC_IRA Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `19`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 005070 | 005070 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 161600.0 | None | None | 20.24 | None | stage2_actionable_best_entry |
| 006110 | 006110 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| 011790 | 011790 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 104500.0 | None | None | 91.39 | None | stage2_actionable_best_entry |
| 020150 | 020150 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 43000.0 | None | None | 37.67 | None | stage2_actionable_best_entry |
| 051910 | 051910 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 451000.0 | None | None | 15.3 | None | stage2_actionable_best_entry |
| 278280 | 278280 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| 361610 | 361610 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| R3L73_C13_002710_20230323_BATTERY_STEEL_CAPACITY_CUSTOMER_UTILIZATION_BRIDGE | 002710 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 22750.0 | None | None | 230.99 | None | stage2_actionable_best_entry |
| R3L73_C13_025900_20230303_ELECTROLYTE_JV_UTILIZATION_FALSE_START | 025900 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 62500.0 | None | None | 2.56 | None | stage2_actionable_best_entry |
| R3L73_C13_336370_20230222_COPPER_FOIL_UTILIZATION_FALSE_START | 336370 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 52200.0 | None | None | 3.45 | None | stage2_actionable_best_entry |
| R3L75_C13_003670_20230131_IRA_ORDERBOOK_UTILIZATION_SUCCESS | 003670 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 224000.0 | None | 560000.0 | 209.825 | 71.4881 | 4b_good_peak_capture |
| R3L75_C13_006400_20240131_CELL_JV_REBOUND_HIGH_MAE_SUCCESS | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 372500.0 | None | None | 32.75 | None | stage2_actionable_best_entry |
| R3L75_C13_247540_20231204_CAPACITY_CONTRACT_NO_UTILIZATION_COUNTER | 247540 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| R3L75_C13_348370_20240110_US_CAPACITY_IRA_SUCCESS | 348370 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 88200.0 | None | None | 347.28 | None | stage2_actionable_best_entry |
| R3L75_C13_373220_20240430_AMPC_JV_HEADLINE_FALSE_BREAK | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | 389000.0 | None | None | no_valid_stage_transition |
| R3L75_C13_393890_20240105_SEPARATOR_CAPACITY_UTILIZATION_COUNTER | 393890 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| R3L84-C13-01 | 348370 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 107000.0 | None | None | 268.69 | None | stage2_actionable_best_entry |
| R3L84-C13-02 | 005070 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| R3L84-C13-03 | 025900 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |

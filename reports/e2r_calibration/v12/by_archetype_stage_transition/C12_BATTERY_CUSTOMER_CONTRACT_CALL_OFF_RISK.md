# C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `32`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 006110 | 006110 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | 75500.0 | None | None | no_valid_stage_transition |
| 011790 | 011790 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | 117000.0 | None | None | no_valid_stage_transition |
| 018470 | 018470 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | None | None | None | no_valid_stage_transition |
| 361610 | 361610 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | None | None | None | no_valid_stage_transition |
| 373220 | 373220 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 332500.0 | None | None | 33.53 | None | stage2_actionable_best_entry |
| C12-LGES-20240725 | 373220 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 332500.0 | None | None | 30.98 | None | stage2_captured_most_upside |
| C12-SDI-20240628 | 006400 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 354000.0 | None | None | 11.16 | None | stage2_captured_most_upside |
| C12-SKIET-20240516 | 361610 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 57600.0 | None | None | 1.04 | None | stage2_captured_most_upside |
| C12_R3L105_003670_20240503_05 | 003670 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 307000.0 | None | None | 29.5 | None | stage2_actionable_best_entry |
| C12_R3L105_006400_20240129_02 | 006400 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 393000.0 | None | None | 5.1 | None | stage2_captured_most_upside |
| C12_R3L105_011790_20240618_07 | 011790 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 94300.0 | None | None | 20.4 | None | stage2_captured_most_upside |
| C12_R3L105_020150_20240607_10 | 020150 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 53000.0 | None | None | 42.0 | None | stage2_actionable_best_entry |
| C12_R3L105_066970_20240216_04 | 066970 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 177000.0 | None | None | 16.5 | None | stage2_captured_most_upside |
| C12_R3L105_089980_20240430_14 | 089980 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 23800.0 | None | None | 11.0 | None | stage2_captured_most_upside |
| C12_R3L105_121600_20240315_11 | 121600 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 115000.0 | None | None | 39.0 | None | stage2_actionable_best_entry |
| C12_R3L105_137400_20240613_13 | 137400 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | None | None | None | no_valid_stage_transition |
| C12_R3L105_222080_20240416_12 | 222080 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 10500.0 | None | None | 20.1 | None | stage2_captured_most_upside |
| C12_R3L105_247540_20240409_03 | 247540 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | None | None | None | no_valid_stage_transition |
| C12_R3L105_278280_20240503_08 | 278280 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 82600.0 | None | None | 14.5 | None | stage2_captured_most_upside |
| C12_R3L105_361610_20240412_06 | 361610 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | None | None | None | no_valid_stage_transition |
| C12_R3L105_373220_20241010_01 | 373220 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 410000.0 | None | None | 21.4 | None | stage2_actionable_best_entry |
| C12_R3L105_393890_20240322_09 | 393890 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 39200.0 | None | None | 6.7 | None | stage2_captured_most_upside |
| C12_R3_L102_CASE_001 | 373220 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 419500.0 | None | None | 5.84 | None | stage2_actionable_best_entry |
| C12_R3_L102_CASE_002 | 096770 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 120300.0 | None | None | 8.81 | None | stage2_actionable_best_entry |
| C12_R3_L102_CASE_003 | 011790 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 138100.0 | None | None | 44.82 | None | stage2_actionable_best_entry |
| C12_R3_L102_CASE_004 | 051910 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | 504000.0 | None | None | no_valid_stage_transition |
| C12_R3_L103_CASE_001 | 066970 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 186100.0 | None | None | 6.93 | None | stage2_actionable_best_entry |
| C12_R3_L103_CASE_002 | 005070 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | 175800.0 | None | None | no_valid_stage_transition |
| C12_R3_L103_CASE_003 | 020150 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 47050.0 | None | None | 25.82 | None | stage2_actionable_best_entry |
| C12_R3_L103_CASE_004 | 121600 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 134000.0 | None | None | 17.76 | None | stage2_actionable_best_entry |
| C12_R3_L103_CASE_005 | 222080 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | 14840.0 | None | None | no_valid_stage_transition |
| C12_R3_L103_CASE_006 | 299030 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | 67200.0 | None | None | no_valid_stage_transition |

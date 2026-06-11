# C13_BATTERY_JV_UTILIZATION_AMPC_IRA Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `58`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 006110 | 006110 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | 75500.0 | None | None | no_valid_stage_transition |
| 011790 | 011790 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | 117000.0 | None | None | no_valid_stage_transition |
| 018470 | 018470 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| 361610 | 361610 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| 373220 | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 332500.0 | None | None | 33.53 | None | stage2_actionable_best_entry |
| C13-102-01 | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 350000.0 | None | None | 26.86 | None | stage2_actionable_best_entry |
| C13-102-02 | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13-102-03 | 096770 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 117100.0 | None | None | 11.78 | None | stage2_actionable_best_entry |
| C13-102-04 | 003670 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13-R3-L100-01 | 348370 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 107000.0 | None | None | 268.69 | None | stage2_actionable_best_entry |
| C13-R3-L100-02 | 247540 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 248000.0 | None | None | 20.36 | None | stage2_captured_most_upside |
| C13-R3-L100-03 | 020150 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 34650.0 | None | None | 51.23 | None | stage2_actionable_best_entry |
| C13-R3-L100-04 | 278280 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 95000.0 | None | None | 5.05 | None | stage2_captured_most_upside |
| C13_006400_2024-06-28_SDI_EUROPE_CUSTOMER_EXPOSURE_UTILIZATION_RISK | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 354000.0 | None | None | 11.16 | None | stage2_captured_most_upside |
| C13_361610_2024-05-16_SKIET_SEPARATOR_UTILIZATION_FINANCING_STRESS | 361610 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 57600.0 | None | None | 1.04 | None | stage2_captured_most_upside |
| C13_373220_2024-07-25_LGES_AMPC_ESS_DIVERSIFIED_CUSTOMER_ESCAPE_HATCH | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 332500.0 | None | None | 33.53 | None | stage2_captured_most_upside |
| C13_R3L103_001570_20240226 | 001570 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | 93300.0 | None | None | 4b_good_peak_capture |
| C13_R3L103_002710_20240206 | 002710 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 59500.0 | None | None | 41.8 | None | stage2_captured_most_upside |
| C13_R3L103_005070_20240216 | 005070 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 151000.0 | None | None | 45.4 | None | stage2_actionable_best_entry |
| C13_R3L103_011790_20240207 | 011790 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 89000.0 | None | None | 22.4 | None | stage2_captured_most_upside |
| C13_R3L103_051910_20240201 | 051910 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 426500.0 | None | None | 24.6 | None | stage2_actionable_best_entry |
| C13_R3L103_066970_20240214 | 066970 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_R3L103_078600_20240321 | 078600 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 83800.0 | None | None | 49.3 | None | stage2_actionable_best_entry |
| C13_R3L103_086520_20240202 | 086520 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | 540000.0 | None | None | 4b_good_peak_capture |
| C13_R3L103_121600_20240314 | 121600 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_R3L103_243840_20240522 | 243840 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 10500.0 | None | None | 31.5 | None | stage2_actionable_best_entry |
| C13_R3L103_361610_20240131 | 361610 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 76000.0 | None | None | 15.2 | None | stage2_captured_most_upside |
| C13_R3L103_393890_20240213 | 393890 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 44200.0 | None | None | 12.7 | None | stage2_captured_most_upside |
| C13_R3L104_001570_20240226_STAGE2 | 001570 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 93300.0 | None | None | 37.9 | None | stage2_captured_most_upside |
| C13_R3L104_002710_20240206_STAGE4B | 002710 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | 59500.0 | None | None | no_valid_stage_transition |
| C13_R3L104_005070_20240216_STAGE3GREEN | 005070 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | 151000.0 | None | None | None | green_good_but_late |
| C13_R3L104_011790_20240207_STAGE4B | 011790 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | 89000.0 | None | None | no_valid_stage_transition |
| C13_R3L104_051910_20240201_STAGE3YELLOW | 051910 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_R3L104_066970_20240214_STAGE4B | 066970 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | 160700.0 | None | None | no_valid_stage_transition |
| C13_R3L104_078600_20240321_STAGE3GREEN | 078600 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | 83800.0 | None | None | None | green_good_but_late |
| C13_R3L104_086520_20240202_STAGE3YELLOW | 086520 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_R3L104_121600_20240314_STAGE4B | 121600 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | 113000.0 | None | None | no_valid_stage_transition |
| C13_R3L104_393890_20240213_STAGE4C | 393890 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_R3L105_001570_20240226_Stage4C_20 | 001570 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_R3L105_002710_20240206_Stage3Yellow_19 | 002710 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_R3L105_005070_20240216_Stage4B_09 | 005070 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | 175800.0 | None | None | no_valid_stage_transition |
| C13_R3L105_011790_20240405_Stage2Actionable_06 | 011790 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 138100.0 | None | None | 44.82 | None | stage2_actionable_best_entry |
| C13_R3L105_020150_20240321_Stage2Actionable_10 | 020150 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 47050.0 | None | None | 25.82 | None | stage2_actionable_best_entry |
| C13_R3L105_020150_20240321_Stage3Yellow_17 | 020150 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_R3L105_051910_20240216_Stage4B_07 | 051910 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | 504000.0 | None | None | no_valid_stage_transition |
| C13_R3L105_066970_20240322_Stage2Actionable_08 | 066970 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 186100.0 | None | None | 6.93 | None | stage2_actionable_best_entry |
| C13_R3L105_066970_20240322_Stage4C_16 | 066970 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_R3L105_096770_20240129_Stage2Actionable_05 | 096770 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 120300.0 | None | None | 8.81 | None | stage2_actionable_best_entry |
| C13_R3L105_121600_20240221_Stage2Actionable_11 | 121600 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 134000.0 | None | None | 17.76 | None | stage2_actionable_best_entry |
| C13_R3L105_121600_20240221_Stage3Yellow_18 | 121600 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_R3L105_222080_20240312_Stage4B_12 | 222080 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | 14840.0 | None | None | no_valid_stage_transition |
| C13_R3L105_247540_20240122_Stage4C_01 | 247540 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_R3L105_278280_20240221_Stage4B_03 | 278280 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | 95600.0 | None | None | no_valid_stage_transition |
| C13_R3L105_278280_20240221_Stage4C_14 | 278280 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_R3L105_299030_20240308_Stage4B_13 | 299030 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | 67200.0 | None | None | no_valid_stage_transition |
| C13_R3L105_299030_20240308_Stage4C_15 | 299030 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_R3L105_361610_20240115_Stage4C_02 | 361610 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_R3L105_373220_20240312_Stage2Actionable_04 | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 419500.0 | None | None | 5.84 | None | stage2_actionable_best_entry |

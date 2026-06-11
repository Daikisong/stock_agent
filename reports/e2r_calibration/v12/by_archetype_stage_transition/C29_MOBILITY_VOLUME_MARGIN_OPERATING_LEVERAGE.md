# C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `57`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 000240 | 000240 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | None | None | None | no_valid_stage_transition |
| 000270 | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 91600.0 | None | None | 58.08 | None | stage2_actionable_best_entry |
| 002350 | 002350 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | None | None | None | no_valid_stage_transition |
| 003620 | 003620 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | None | None | None | no_valid_stage_transition |
| 005380 | 005380 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 189000.0 | None | None | 52.38 | None | stage2_actionable_best_entry |
| 005850 | 005850 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | None | None | None | no_valid_stage_transition |
| 010690 | 010690 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 14500.0 | None | 11690.0 | 9.59 | -202.0783 | stage2_actionable_best_entry |
| 011210 | 011210 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 51600.0 | None | None | 29.875 | None | stage2_captured_most_upside |
| 012330 | 012330 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 244000.0 | None | None | 18.4439 | None | stage2_actionable_best_entry |
| 015750 | 015750 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | None | None | None | no_valid_stage_transition |
| 018880 | 018880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | None | None | None | no_valid_stage_transition |
| 064960 | 064960 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 46650.0 | None | None | 0.32 | None | stage2_actionable_best_entry |
| 073240 | 073240 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | 5600.0 | None | None | no_valid_stage_transition |
| 086280 | 086280 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 123900.0 | None | 123900.0 | 21.87 | 0.0 | stage2_captured_most_upside |
| 161390 | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 47500.0 | None | None | 36.84 | None | stage2_actionable_best_entry |
| 200880 | 200880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | None | None | None | no_valid_stage_transition |
| 204320 | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 38350.0 | None | 42500.0 | 48.6336 | 22.2508 | stage2_actionable_best_entry |
| C29_R9L100_000270_20240125 | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 93000.0 | None | None | 45.16 | None | stage2_actionable_best_entry |
| C29_R9L100_000270_KIA_VALUEUP_MIX_MARGIN | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 94400.0 | None | None | 43.0 | None | stage2_actionable_best_entry |
| C29_R9L100_005380_20240125 | 005380 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 188700.0 | None | None | 58.72 | None | stage2_actionable_best_entry |
| C29_R9L100_005380_HYUNDAI_VALUEUP_MIX_MARGIN | 005380 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 187300.0 | None | None | 59.9 | None | stage2_actionable_best_entry |
| C29_R9L100_011210_20240125 | 011210 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 58000.0 | None | None | 15.52 | None | stage2_captured_most_upside |
| C29_R9L100_204320_20240605 | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | 49600.0 | None | None | 4b_good_peak_capture |
| C29_R9L100_204320_HLMANDO_POST_SPIKE_WEAK_BRIDGE | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 47550.0 | None | 47550.0 | 2.8 | 0.0 | stage2_actionable_best_entry |
| C29_R9L104_002350_20240411_CANONICAL_STAGE2_REPAIR | 002350 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 9500.0 | None | None | 1.1 | None | stage2_captured_most_upside |
| C29_R9L104_005850_20240429_CANONICAL_STAGE3Y_REPAIR | 005850 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | None | None | None | no_valid_stage_transition |
| C29_R9L104_011210_20240202_CANONICAL_STAGE2_REPAIR | 011210 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 64500.0 | None | None | 3.9 | None | stage2_captured_most_upside |
| C29_R9L104_073240_20240411_CANONICAL_STAGE2A_REPAIR | 073240 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 6490.0 | None | None | 29.0 | None | stage2_actionable_best_entry |
| C29_R9L104_161390_20240125_CANONICAL_STAGE4B_REPAIR | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | 49450.0 | None | None | no_valid_stage_transition |
| C29_R9L105_000270_20240125_FINALPASS | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 93000.0 | None | None | 45.16 | None | stage2_actionable_best_entry |
| C29_R9L105_005380_20240125_FINALPASS | 005380 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 188700.0 | None | None | 58.72 | None | stage2_actionable_best_entry |
| C29_R9L105_010690_20240617_FINALPASS | 010690 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 14500.0 | None | None | 9.59 | None | stage2_actionable_best_entry |
| C29_R9L105_012330_20240219_FINALPASS | 012330 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 244000.0 | None | None | 10.66 | None | stage2_actionable_best_entry |
| C29_R9L105_018880_20240503_FINALPASS | 018880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 6490.0 | None | None | 4.78 | None | stage2_captured_most_upside |
| C29_R9L105_064960_20240306_FINALPASS | 064960 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 46650.0 | None | None | 0.32 | None | stage2_actionable_best_entry |
| C29_R9L105_200880_20240617_FINALPASS | 200880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | None | None | None | no_valid_stage_transition |
| C29_R9L105_204320_20240605_FINALPASS | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | 49600.0 | None | None | no_valid_stage_transition |
| C29_R9L106_000270_20240202_02 | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | None | None | None | no_valid_stage_transition |
| C29_R9L106_000270_20240614_17 | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | 125000.0 | None | None | None | green_good_but_late |
| C29_R9L106_002350_20240223_11 | 002350 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 9400.0 | None | None | 2.1 | None | stage2_captured_most_upside |
| C29_R9L106_003620_20240319_14 | 003620 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | None | None | None | no_valid_stage_transition |
| C29_R9L106_005380_20240202_01 | 005380 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | None | None | None | no_valid_stage_transition |
| C29_R9L106_005380_20240614_16 | 005380 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | 285000.0 | None | None | None | green_good_but_late |
| C29_R9L106_005850_20240612_10 | 005850 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | None | None | None | no_valid_stage_transition |
| C29_R9L106_005850_20240717_20 | 005850 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | 40150.0 | None | None | no_valid_stage_transition |
| C29_R9L106_010690_20240617_08 | 010690 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | 14500.0 | None | None | no_valid_stage_transition |
| C29_R9L106_011210_20240125_04 | 011210 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 58000.0 | None | None | 15.5 | None | stage2_captured_most_upside |
| C29_R9L106_012330_20240219_03 | 012330 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | None | None | None | no_valid_stage_transition |
| C29_R9L106_012330_20240618_18 | 012330 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | 235000.0 | None | None | no_valid_stage_transition |
| C29_R9L106_018880_20240503_06 | 018880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | None | None | None | no_valid_stage_transition |
| C29_R9L106_064960_20240306_07 | 064960 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 46650.0 | None | None | 0.3 | None | stage2_actionable_best_entry |
| C29_R9L106_073240_20240430_12 | 073240 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 7040.0 | None | None | 18.0 | None | stage2_actionable_best_entry |
| C29_R9L106_086280_20240618_15 | 086280 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 59400.0 | None | None | 15.0 | None | stage2_captured_most_upside |
| C29_R9L106_161390_20240430_13 | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 42950.0 | None | None | 20.4 | None | stage2_actionable_best_entry |
| C29_R9L106_200880_20240617_09 | 200880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | 20900.0 | None | None | no_valid_stage_transition |
| C29_R9L106_204320_20240605_05 | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | 49600.0 | None | None | no_valid_stage_transition |
| C29_R9L106_204320_20241112_19 | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | None | None | None | no_valid_stage_transition |

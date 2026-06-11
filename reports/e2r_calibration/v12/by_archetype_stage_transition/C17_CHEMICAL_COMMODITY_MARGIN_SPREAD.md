# C17_CHEMICAL_COMMODITY_MARGIN_SPREAD Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `58`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 002380 | 002380 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 244000.0 | None | None | 41.39 | None | stage2_actionable_best_entry |
| 006650 | 006650 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| 007690 | 007690 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| 009830 | 009830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 31800.0 | None | None | 7.86 | None | stage2_captured_most_upside |
| 010060 | 010060 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | 95100.0 | None | None | no_valid_stage_transition |
| 010950 | 010950 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 71500.0 | None | None | 18.1846 | None | stage2_actionable_best_entry |
| 011170 | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 107700.0 | None | None | 16.53 | None | stage2_actionable_best_entry |
| 011780 | 011780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 133600.0 | None | None | 31.29 | None | stage2_actionable_best_entry |
| 011790 | 011790 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 114700.0 | None | 117000.0 | 74.37 | 2.6963 | stage2_actionable_best_entry |
| 051910 | 051910 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 504000.0 | None | None | 3.17 | None | stage2_captured_most_upside |
| 161000 | 161000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | 14500.0 | None | None | no_valid_stage_transition |
| 298000 | 298000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| 298020 | 298020 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 324500.0 | None | None | 29.8937 | None | stage2_actionable_best_entry |
| C17_010950_REFINING_MARGIN_REBOUND_Q1_2024 | 010950 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| C17_051910_LOW_MARGIN_PETCHEM_OVERSUPPLY_2024 | 051910 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| C17_298000_PP_CHEMICAL_LABEL_SPIKE_HIGH_MAE_2024 | 298000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| C17_R4L105_01 | 161000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 13700.0 | None | None | 26.0 | None | stage2_actionable_best_entry |
| C17_R4L105_02 | 093370 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 9000.0 | None | None | 18.0 | None | stage2_captured_most_upside |
| C17_R4L105_03 | 004430 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 13300.0 | None | None | 34.0 | None | stage2_actionable_best_entry |
| C17_R4L105_04 | 285130 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 55100.0 | None | None | 19.0 | None | stage2_captured_most_upside |
| C17_R4L106_000880_20240605_STAGE2_20 | 000880 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 28100.0 | None | None | 21.5 | None | stage2_captured_most_upside |
| C17_R4L106_004000_20240516_STAGE2ACTIONABLE_13 | 004000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 47700.0 | None | None | 22.6 | None | stage2_actionable_best_entry |
| C17_R4L106_004430_20240517_STAGE2ACTIONABLE_09 | 004430 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 14200.0 | None | None | 34.0 | None | stage2_actionable_best_entry |
| C17_R4L106_005420_20240226_STAGE2_14 | 005420 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 36600.0 | None | None | 11.3 | None | stage2_captured_most_upside |
| C17_R4L106_005950_20240508_STAGE2ACTIONABLE_18 | 005950 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 12100.0 | None | None | 31.2 | None | stage2_actionable_best_entry |
| C17_R4L106_006650_20240415_STAGE2_12 | 006650 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 126500.0 | None | None | 14.0 | None | stage2_captured_most_upside |
| C17_R4L106_007690_20240402_STAGE2_19 | 007690 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 35300.0 | None | None | 13.6 | None | stage2_captured_most_upside |
| C17_R4L106_009830_20240220_STAGE2_17 | 009830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 27000.0 | None | None | 9.4 | None | stage2_captured_most_upside |
| C17_R4L106_010950_20240405_STAGE2_06 | 010950 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 83500.0 | None | None | 1.2 | None | stage2_captured_most_upside |
| C17_R4L106_011170_20240429_STAGE2_05 | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 107700.0 | None | None | 16.53 | None | stage2_captured_most_upside |
| C17_R4L106_011500_20240328_STAGE2_15 | 011500 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 15400.0 | None | None | 22.0 | None | stage2_captured_most_upside |
| C17_R4L106_011780_20240429_STAGE3YELLOW_04 | 011780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| C17_R4L106_011790_20240314_STAGE2ACTIONABLE_02 | 011790 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 114700.0 | None | None | 74.37 | None | stage2_actionable_best_entry |
| C17_R4L106_014680_20240321_STAGE2ACTIONABLE_11 | 014680 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 176000.0 | None | None | 28.4 | None | stage2_actionable_best_entry |
| C17_R4L106_051910_20240216_STAGE2_01 | 051910 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 504000.0 | None | None | 3.17 | None | stage2_captured_most_upside |
| C17_R4L106_093370_20240612_STAGE2_08 | 093370 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 7900.0 | None | None | 18.0 | None | stage2_captured_most_upside |
| C17_R4L106_120110_20240424_STAGE2ACTIONABLE_16 | 120110 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 42500.0 | None | None | 26.2 | None | stage2_actionable_best_entry |
| C17_R4L106_161000_20240522_STAGE2ACTIONABLE_07 | 161000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 11150.0 | None | None | 26.0 | None | stage2_actionable_best_entry |
| C17_R4L106_285130_20240603_STAGE2_10 | 285130 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 49800.0 | None | None | 19.0 | None | stage2_captured_most_upside |
| C17_R4L106_298020_20240417_STAGE3YELLOW_03 | 298020 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| C17_R4L107_000860_20240508_STAGE2_09 | 000860 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 20750.0 | None | None | 16.4 | None | stage2_captured_most_upside |
| C17_R4L107_001340_20240522_STAGE3YELLOW_03 | 001340 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| C17_R4L107_002360_20240502_STAGE2_18 | 002360 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 670.0 | None | None | 14.4 | None | stage2_captured_most_upside |
| C17_R4L107_002380_20240424_STAGE2ACTIONABLE_08 | 002380 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 238500.0 | None | None | 36.9 | None | stage2_actionable_best_entry |
| C17_R4L107_003240_20240516_STAGE2_05 | 003240 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 705000.0 | None | None | 15.2 | None | stage2_captured_most_upside |
| C17_R4L107_003650_20240328_STAGE2ACTIONABLE_07 | 003650 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 72200.0 | None | None | 25.5 | None | stage2_actionable_best_entry |
| C17_R4L107_009440_20240429_STAGE2_16 | 009440 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 3250.0 | None | None | 18.0 | None | stage2_captured_most_upside |
| C17_R4L107_011930_20240605_STAGE2_11 | 011930 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 2120.0 | None | None | 15.6 | None | stage2_captured_most_upside |
| C17_R4L107_014830_20240321_STAGE2ACTIONABLE_01 | 014830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 70300.0 | None | None | 31.2 | None | stage2_actionable_best_entry |
| C17_R4L107_024070_20240417_STAGE2_10 | 024070 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 2950.0 | None | None | 20.1 | None | stage2_captured_most_upside |
| C17_R4L107_025000_20240402_STAGE2_04 | 025000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 46800.0 | None | None | 13.4 | None | stage2_captured_most_upside |
| C17_R4L107_025860_20240327_STAGE2_15 | 025860 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 7520.0 | None | None | 21.8 | None | stage2_captured_most_upside |
| C17_R4L107_065130_20240529_STAGE2_14 | 065130 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 6800.0 | None | None | 18.7 | None | stage2_captured_most_upside |
| C17_R4L107_069260_20240425_STAGE2ACTIONABLE_02 | 069260 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 20100.0 | None | None | 28.7 | None | stage2_actionable_best_entry |
| C17_R4L107_102260_20240612_STAGE2_06 | 102260 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 4900.0 | None | None | 22.0 | None | stage2_captured_most_upside |
| C17_R4L107_104830_20240314_STAGE2ACTIONABLE_12 | 104830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 31100.0 | None | None | 42.8 | None | stage2_actionable_best_entry |
| C17_R4L107_161000_20240226_STAGE2ACTIONABLE_17 | 161000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 14450.0 | None | None | 30.6 | None | stage2_actionable_best_entry |
| C17_R4L107_357780_20240411_STAGE2ACTIONABLE_13 | 357780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 284000.0 | None | None | 32.1 | None | stage2_actionable_best_entry |

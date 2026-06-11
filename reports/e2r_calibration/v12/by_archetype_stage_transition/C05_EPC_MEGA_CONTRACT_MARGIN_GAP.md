# C05_EPC_MEGA_CONTRACT_MARGIN_GAP Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `44`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 000720 | 000720 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| 004960 | 004960 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| 006360 | 006360 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 15630.0 | None | None | 39.16 | None | stage2_actionable_best_entry |
| 028050 | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 25300.0 | None | None | 10.47 | None | stage2_actionable_best_entry |
| 047040 | 047040 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| 294870 | 294870 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| 375500 | 375500 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| C05_R1L108_000720_20240126_MARGIN_BACKLOG_REPAIR | 000720 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 33100.0 | None | None | 14.95 | None | stage2_actionable_best_entry |
| C05_R1L108_004960_20240429_SMALL_BUILDER_COUNTER | 004960 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 6550.0 | None | None | 6.1 | None | stage2_captured_most_upside |
| C05_R1L108_006360_20240430_COST_PROVISION_RECOVERY | 006360 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 16480.0 | None | None | 11.77 | None | stage2_actionable_best_entry |
| C05_R1L108_013580_20240429_REGIONAL_EPC_STAGE2_CAP | 013580 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 13700.0 | None | None | 13.43 | None | stage2_actionable_best_entry |
| C05_R1L108_016250_20240130_HEAVY_CIVIL_COUNTER | 016250 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 18470.0 | None | None | 3.46 | None | stage2_captured_most_upside |
| C05_R1L108_028050_20240228_PLANT_ORDER_MARGIN_GAP | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 26000.0 | None | None | 8.27 | None | stage2_actionable_best_entry |
| C05_R1L108_028050_20240626_POST_PEAK_LOCAL4B | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | 25200.0 | None | None | no_valid_stage_transition |
| C05_R1L108_047040_20240403_ORDERBOOK_LABEL_COUNTER | 047040 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 3805.0 | None | None | 14.45 | None | stage2_captured_most_upside |
| C05_R1L108_047040_20240717_POST_PEAK_LOCAL4B | 047040 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | 4355.0 | None | None | no_valid_stage_transition |
| C05_R1L108_294870_20240126_HOUSING_PF_CONTAMINANT | 294870 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 17530.0 | None | None | 28.24 | None | stage2_actionable_best_entry |
| C05_R1L108_294870_20240826_HDC_POST_SPIKE_WATCH | 294870 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | 26700.0 | None | None | no_valid_stage_transition |
| C05_R1L108_375500_20240429_LOW_PBR_EPC_REBOUND | 375500 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 36650.0 | None | None | 7.78 | None | stage2_actionable_best_entry |
| C05_R1L108_375500_20240613_EPC_LOCAL4B_DECAY | 375500 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | 39500.0 | None | None | no_valid_stage_transition |
| C05_R1L109_000720_20240202_BACKLOG_DELIVERY_MARGIN_BRIDGE | 000720 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| C05_R1L109_001470_20240201_POLITICAL_CONSTRUCTION_THEME_CONTAMINANT | 001470 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | 2410.0 | None | None | no_valid_stage_transition |
| C05_R1L109_002410_20240715_THIN_BUILDER_PRICE_SPIKE | 002410 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | 1630.0 | None | None | no_valid_stage_transition |
| C05_R1L109_002460_20240522_REGIONAL_BUILDER_CASH_BRIDGE_PARTIAL | 002460 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 9480.0 | None | None | 20.9 | None | stage2_captured_most_upside |
| C05_R1L109_002780_20240314_SMALL_BUILDER_BALANCE_SHEET_LABEL | 002780 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 1290.0 | None | None | 12.4 | None | stage2_captured_most_upside |
| C05_R1L109_002990_20240403_BUILDER_LABEL_HIGH_MAE | 002990 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 4040.0 | None | None | 8.5 | None | stage2_captured_most_upside |
| C05_R1L109_003070_20240612_POST_PEAK_HIGH_MAE_BUILDER_SPIKE | 003070 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 10300.0 | None | None | 13.5 | None | stage2_captured_most_upside |
| C05_R1L109_004960_20240328_SMALL_BUILDER_WORKING_CAPITAL_GUARD | 004960 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 6730.0 | None | None | 31.2 | None | stage2_captured_most_upside |
| C05_R1L109_005960_20240226_POST_SPIKE_LOCAL4B_HIGH_MAE | 005960 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | 4380.0 | None | None | no_valid_stage_transition |
| C05_R1L109_006360_20240201_COST_PROVISION_REPAIR_MARGIN_WATCH | 006360 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 15150.0 | None | None | 33.1 | None | stage2_actionable_best_entry |
| C05_R1L109_009410_20240103_WORKOUT_RECAPITALIZATION_HARD_BREAK | 009410 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| C05_R1L109_010780_20240207_MATERIALS_CONSTRUCTION_CASH_BRIDGE | 010780 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| C05_R1L109_013360_20240411_HOUSING_THEME_PRICE_ONLY | 013360 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 1470.0 | None | None | 14.6 | None | stage2_actionable_best_entry |
| C05_R1L109_013580_20240516_REGIONAL_BUILDER_PARTIAL_CASH_BRIDGE | 013580 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 13960.0 | None | None | 12.8 | None | stage2_actionable_best_entry |
| C05_R1L109_014790_20240429_REPAIR_BOUNCE_WITHOUT_FCF | 014790 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 2380.0 | None | None | 18.6 | None | stage2_actionable_best_entry |
| C05_R1L109_028050_20240424_EPC_PROJECT_MARGIN_BRIDGE | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 27000.0 | None | None | 24.1 | None | stage2_actionable_best_entry |
| C05_R1L109_035890_20240321_REGIONAL_PRE_SALE_CASH_BRIDGE | 035890 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 1370.0 | None | None | 25.4 | None | stage2_actionable_best_entry |
| C05_R1L109_047040_20240110_LARGE_BUILDER_ORDERBOOK_STAGE2_WATCH | 047040 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 4260.0 | None | None | 20.1 | None | stage2_captured_most_upside |
| C05_R1L109_294870_20240126_PF_BALANCE_SHEET_REPAIR_CONTAMINANT | 294870 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| C05_R1L109_375500_20240205_LOW_PBR_BUILDER_WITHOUT_PROJECT_MARGIN | 375500 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 38100.0 | None | None | 22.8 | None | stage2_actionable_best_entry |
| C05_R1L110_006360_20240808_STAGE2_POST_PEAK_REPAIR_PRICE_SPIKE_WITHOUT_MARGIN_REFRESH | 006360 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 18900.0 | None | None | 8.0 | None | stage2_captured_most_upside |
| C05_R1L110_028050_20240424_STAGE3YELLOW_PLANT_EPC_PROJECT_MARGIN_BRIDGE_POSITIVE | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| C05_R1L110_047040_20240712_STAGE2ACTIONABLE_CONSTRUCTION_EPC_PF_CONTAMINANT_MIXED | 047040 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 4200.0 | None | None | 20.0 | None | stage2_actionable_best_entry |
| C05_R1L110_375500_20240626_STAGE2ACTIONABLE_LOW_PBR_EPC_ORDERBOOK_WITHOUT_FCF_BRIDGE | 375500 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 35800.0 | None | None | 7.0 | None | stage2_actionable_best_entry |

# C05_EPC_MEGA_CONTRACT_MARGIN_GAP Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `33`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C05_R11L88_026150_TUKSU_CIVIL_WORKS_THEME | 026150 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| C05_R11L88_028100_DONGA_GEOTECH_CIVIL_WORKS_THEME | 028100 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| C05_R11L88_052690_KEPCO_ENGINEERING_NUCLEAR_EPC_SCOPE | 052690 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 59200.0 | None | None | 65.71 | None | stage2_actionable_best_entry |
| C05_R1L84_000720_HDC_EPC_BACKLOG_MARGIN_BRIDGE | 000720 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 28450.0 | None | None | 199.12 | None | stage2_actionable_best_entry |
| C05_R1L84_006360_GS_EC_MARGIN_REPAIR_CONTROL | 006360 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| C05_R1L84_028050_SAMSUNG_EA_MARGIN_GAP_COUNTEREXAMPLE | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| C05_R1L86_000720_HYUNDAICONST_CONTRACT_THEME_NO_MARGIN_CASH | 000720 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| C05_R1L86_028050_SAMSUNGEA_EPC_SELECTIVE_ORDER_MARGIN_RECOVERY | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 22300.0 | None | None | 31.39 | None | stage2_actionable_best_entry |
| C05_R1L86_047040_DAEWOO_EPC_THEME_NO_MARGIN_CONVERSION | 047040 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| C05_R1L91_028050_SAMSUNG_EA_EPC_REBRAND_DECAY | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| C05_R1L91_037350_SUNGDO_CLEANROOM_SPIKE_DECAY | 037350 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| C05_R1L91_100840_SNT_ENERGY_BACKLOG_MARGIN | 100840 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 10050.0 | None | None | 153.73 | None | stage2_actionable_best_entry |
| C05_R1L93_016250_2024_07_24 | 016250 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 14900.0 | None | None | 25.8 | None | stage2_captured_most_upside |
| C05_R1L93_028050_2024_02_28 | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| C05_R1L93_028100_2024_01_30 | 028100 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| C05_R1L98_014620_2024_02_01 | 014620 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 10790.0 | None | None | 56.6 | None | stage2_captured_most_upside |
| C05_R1L98_017960_2024_02_01 | 017960 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 10540.0 | None | None | 26.7 | None | stage2_captured_most_upside |
| C05_R1L98_105740_2024_07_29 | 105740 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| R11L90_C05_DAEWOOE_C_2024_OVERSEAS_EPC_POLICY_CONTRACT_MARGIN_BRIDGE_POSITIVE | 047040 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 3890.0 | None | None | 27.63 | None | stage2_actionable_best_entry |
| R11L90_C05_KEPCOE_C_2024_NUCLEAR_ENGINEERING_EPC_EVENT_CAP_4B | 052690 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | 71800.0 | None | None | 4b_good_peak_capture |
| R11L90_C05_SAMSUNGEA_2024_PLANT_EPC_MARGIN_GAP_FALSE_STAGE2 | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 26000.0 | None | None | 8.27 | None | stage2_actionable_best_entry |
| R1L88_C05_000720_NEGCTRL | 000720 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| R1L88_C05_006360_FADHILI | 006360 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| R1L88_C05_028050_FADHILI | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 25300.0 | None | None | 15.81 | None | stage2_actionable_best_entry |
| R1L88_C05_HANMIGLOBAL_2022_NEOM_PM_EVENT_CAP_4B | 053690 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | 33100.0 | None | None | 4b_good_peak_capture |
| R1L88_C05_HANYANGENG_2023_CLEANROOM_EPC_EVENT_CAP_4B | 045100 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | 24400.0 | None | None | 4b_good_peak_capture |
| R1L88_C05_SAMSUNGEA_2023_EPC_MARGIN_BRIDGE_POSITIVE | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 25850.0 | None | None | 46.23 | None | stage2_actionable_best_entry |
| R1L93_C05_ILJINPOWER_2024_POWER_PLANT_SERVICE_EPC_EVENT_CAP_4B | 094820 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | 14170.0 | None | None | 4b_good_peak_capture |
| R1L93_C05_SAMHODEV_2024_CIVIL_EPC_ORDER_CATCHUP_FALSE_STAGE2 | 010960 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 3410.0 | None | None | 7.04 | None | stage2_actionable_best_entry |
| R1L93_C05_SNTENERGY_2024_PLANT_EPC_EXPORT_ORDER_MARGIN_BRIDGE_POSITIVE | 100840 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 10050.0 | None | None | 232.34 | None | stage2_actionable_best_entry |
| R1L97_C05_HANYANGENG_2024_SEMICON_FACILITY_EPC_EVENT_CAP_4B | 045100 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | 20900.0 | None | None | 4b_good_peak_capture |
| R1L97_C05_SAMSUNGEA_2024_GLOBAL_EPC_MARGIN_GAP_FALSE_STAGE2 | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 25300.0 | None | None | 6.72 | None | stage2_actionable_best_entry |
| R1L97_C05_SNTENERGY_2024_HEAT_EXCHANGER_PLANT_EPC_ORDER_MARGIN_POSITIVE | 100840 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 10050.0 | None | None | 232.34 | None | stage2_actionable_best_entry |

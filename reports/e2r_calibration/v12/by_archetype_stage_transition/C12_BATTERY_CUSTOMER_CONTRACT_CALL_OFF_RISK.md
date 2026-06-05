# C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `27`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C12_R3L83_003670_POSCOFUTUREM_ORDERBOOK_CALL_OFF_RISK | 003670 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | None | None | None | no_valid_stage_transition |
| C12_R3L83_066970_LNF_CATHODE_OFFTAKE_CALL_OFF_BREAK | 066970 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | None | None | None | no_valid_stage_transition |
| C12_R3L83_348370_ENCHEM_ELECTROLYTE_CONTRACT_BRIDGE | 348370 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 93100.0 | None | None | 323.74 | None | stage2_actionable_best_entry |
| C12_R3L86_066970_LNF_CATHODE_CALLOFF_MARGIN_RISK | 066970 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | None | None | None | no_valid_stage_transition |
| C12_R3L86_317330_DUKSAN_BATTERY_MATERIAL_CUSTOMER_CAPACITY | 317330 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 23850.0 | None | None | 183.02 | None | stage2_actionable_best_entry |
| C12_R3L86_361610_SKIET_SEPARATOR_SHIPMENT_UTILIZATION_RISK | 361610 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | None | None | None | no_valid_stage_transition |
| C12_R3L90_114190_KANGWON_ENERGY_CALLOFF_BRIDGE | 114190 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 13290.0 | None | None | 64.41 | None | stage2_actionable_best_entry |
| C12_R3L90_417200_LS_MATERIALS_IPO_EV_THEME | 417200 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | None | None | None | no_valid_stage_transition |
| C12_R3L90_450080_ECOPRO_MATERIALS_PRECURSOR_REBOUND | 450080 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | None | None | None | no_valid_stage_transition |
| C12_R3L92_066970_2024_03_20 | 066970 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | None | None | None | no_valid_stage_transition |
| C12_R3L92_078600_2024_05_14 | 078600 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 100800.0 | None | None | 62.1 | None | stage2_actionable_best_entry |
| C12_R3L92_361610_2024_03_20 | 361610 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | None | None | None | no_valid_stage_transition |
| C12_R3L96_005070_2024_02_01 | 005070 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 139900.0 | None | None | 38.9 | None | stage2_captured_most_upside |
| C12_R3L96_011790_2024_02_01 | 011790 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 76900.0 | None | None | 122.9 | None | stage2_captured_most_upside |
| C12_R3L96_051910_2024_02_16 | 051910 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | None | None | None | no_valid_stage_transition |
| R3L88_C12_006400 | 006400 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 213500.0 | None | None | 66.0 | None | stage2_actionable_best_entry |
| R3L88_C12_361610 | 361610 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | None | None | None | no_valid_stage_transition |
| R3L88_C12_373220 | 373220 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | None | None | None | no_valid_stage_transition |
| R3L90_C12_DAEBOMAGNETIC_2024_CUSTOMER_CALLOFF_FALSE_STAGE2 | 290670 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 30400.0 | None | None | 9.21 | None | stage2_actionable_best_entry |
| R3L90_C12_SEAMECHANICS_2024_EV_PARTS_CUSTOMER_PROGRAM_EVENT_CAP_4B | 396300 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | 4080.0 | None | None | 4b_good_peak_capture |
| R3L90_C12_TCCSTEEL_2024_BATTERY_CAN_CUSTOMER_CONTRACT_BRIDGE_POSITIVE | 002710 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 47100.0 | None | None | 82.38 | None | stage2_actionable_best_entry |
| R3L94_C12_DAEJOO_2024_SILICON_ANODE_CALLOFF_EVENT_CAP_4B | 078600 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | 160000.0 | None | None | 4b_good_peak_capture |
| R3L94_C12_JEO_2024_CNT_MATERIAL_CALLOFF_FALSE_STAGE2 | 418550 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 26650.0 | None | None | 11.07 | None | stage2_actionable_best_entry |
| R3L94_C12_SOULBRAINHOLDINGS_2024_ELECTROLYTE_CUSTOMER_CALLOFF_CAPACITY_MARGIN_POSITIVE | 036830 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 45950.0 | None | None | 102.83 | None | stage2_actionable_best_entry |
| R3L97_C12_SAMGIEV_2024_BATTERY_CASE_EVENT_CAP_4B | 419050 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | 3320.0 | None | None | 4b_good_peak_capture |
| R3L97_C12_SHINHEUNGSEC_2024_BATTERY_CAP_CALLOFF_FALSE_STAGE2_POST_CA | 243840 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 9230.0 | None | None | 13.43 | None | stage2_actionable_best_entry |
| R3L97_C12_SKC_2024_COPPER_FOIL_CUSTOMER_CONTRACT_BRIDGE_POSITIVE | 011790 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 81100.0 | None | None | 146.61 | None | stage2_actionable_best_entry |

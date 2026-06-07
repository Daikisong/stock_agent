# C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `16`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C12-R3L98-001 | 003670 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | None | None | None | no_valid_stage_transition |
| C12-R3L98-002 | 005070 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | None | None | None | no_valid_stage_transition |
| C12-R3L98-003 | 020150 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | None | None | None | no_valid_stage_transition |
| C12-R3L98-004 | 078600 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | None | None | None | no_valid_stage_transition |
| C12_CHUNBO_278280_2024_02_21_ELECTROLYTE_CUSTOMER_CALL_OFF_RISK | 278280 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | None | None | None | 4c_too_late |
| C12_COSMOAM_005070_2024_03_06_CATHODE_CUSTOMER_CALL_OFF_MARGIN_FCF_HARD_4C | 005070 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | None | None | None | 4c_too_late |
| C12_DAEJOO_078600_2024_03_06_SILICON_ANODE_CONTRACT_OPTIONALITY_OVERBLOCK | 078600 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 78100.0 | None | None | 109.22 | None | stage2_captured_most_upside |
| C12_NANOMATERIALS_121600_2024_02_21_CNT_CUSTOMER_RAMP_STAGE2_FALSE_POSITIVE | 121600 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 134000.0 | None | None | 17.76 | None | stage2_captured_most_upside |
| C12_NANO_121600_2024_03_06_CNT_CUSTOMER_CONTRACT_CALL_OFF_4B_TO_4C | 121600 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | None | None | None | 4c_too_late |
| C12_R3L93_005070_COSMO_CATHODE_SPIKE_DECAY | 005070 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | None | None | None | no_valid_stage_transition |
| C12_R3L93_006400_SDI_PREMIUM_CELL_CALLOFF_PRESSURE | 006400 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | None | None | None | no_valid_stage_transition |
| C12_R3L93_373220_LGES_CALLOFF_STABILIZATION | 373220 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 379500.0 | None | None | 16.99 | None | stage2_actionable_best_entry |
| C12_WCP_393890_2024_02_21_SEPARATOR_CUSTOMER_CALL_OFF_RISK | 393890 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | None | None | None | 4c_too_late |
| R3L98_C12_ECOPROMATERIALS_2024_PRECURSOR_MATERIAL_CALLOFF_EVENT_CAP_4B | 450080 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | None | None | 240000.0 | None | None | 4b_good_peak_capture |
| R3L98_C12_ENCHEM_2024_ELECTROLYTE_CUSTOMER_CONTRACT_CAPA_BRIDGE_POSITIVE | 348370 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 107000.0 | None | None | 268.69 | None | stage2_actionable_best_entry |
| R3L98_C12_LOTTEEM_2024_COPPERFOIL_CALLOFF_FALSE_STAGE2 | 020150 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 56300.0 | None | None | 5.15 | None | stage2_actionable_best_entry |

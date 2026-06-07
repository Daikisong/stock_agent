# C11_BATTERY_ORDERBOOK_RERATING Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `31`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C11-L100-01 | 137400 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11-L100-02 | 137400 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11-L100-03 | 222080 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11-L100-04 | 222080 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11-L100-05 | 299030 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11-L100-06 | 393890 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11_006400_2024_ORDERBOOK_TO_FCF_FAILURE | 006400 | C11_BATTERY_ORDERBOOK_RERATING | 486000.0 | None | None | 1.7 | None | stage2_captured_most_upside |
| C11_247540_2023_CATHODE_ORDERBOOK_BLOWOFF_AUDIT | 247540 | C11_BATTERY_ORDERBOOK_RERATING | 166300.0 | None | 462000.0 | 251.2 | 70.7847 | stage2_actionable_best_entry |
| C11_373220_2023_CELL_ORDERBOOK_RERATING_SUCCESS | 373220 | C11_BATTERY_ORDERBOOK_RERATING | 517000.0 | None | None | 18.8 | None | stage2_actionable_best_entry |
| C11_CIS_222080_2024_03_05_BATTERY_EQUIPMENT_ORDERBOOK_FALSE_POSITIVE | 222080 | C11_BATTERY_ORDERBOOK_RERATING | 13150.0 | None | None | 14.9 | None | stage2_captured_most_upside |
| C11_CIS_222080_2024_03_06_BATTERY_EQUIPMENT_ORDERBOOK_BETA_FAIL | 222080 | C11_BATTERY_ORDERBOOK_RERATING | 13290.0 | None | None | 13.7 | None | stage2_captured_most_upside |
| C11_DAEJOO_078600_2024_02_21_SILICON_ANODE_ORDERBOOK_RERATING | 078600 | C11_BATTERY_ORDERBOOK_RERATING | 76000.0 | None | None | 115.0 | None | stage2_actionable_best_entry |
| C11_DYPNF_104460_2024_03_06_POWDER_HANDLING_BATTERY_MATERIAL_EQUIPMENT_4B | 104460 | C11_BATTERY_ORDERBOOK_RERATING | 19720.0 | None | None | 27.54 | None | stage2_actionable_best_entry |
| C11_ENCHEM_348370_2024_01_29_ELECTROLYTE_ORDERBOOK_RERATING_4B | 348370 | C11_BATTERY_ORDERBOOK_RERATING | 169500.0 | None | None | 132.74 | None | stage2_actionable_best_entry |
| C11_GITECH_382480_2024_03_06_SLOT_DIE_ORDERBOOK_FAIL | 382480 | C11_BATTERY_ORDERBOOK_RERATING | 3015.0 | None | None | 18.24 | None | stage2_captured_most_upside |
| C11_GITECH_382480_2024_03_12_BATTERY_PARTS_ORDERBOOK_FALSE_POSITIVE | 382480 | C11_BATTERY_ORDERBOOK_RERATING | 3365.0 | None | None | 5.94 | None | stage2_captured_most_upside |
| C11_HANATECH_299030_2024_03_06_BATTERY_EQUIPMENT_ORDERBOOK_BETA_FAIL | 299030 | C11_BATTERY_ORDERBOOK_RERATING | 61400.0 | None | None | 19.06 | None | stage2_captured_most_upside |
| C11_HANATECH_299030_2024_03_06_BATTERY_EQUIPMENT_ORDERBOOK_SPIKE_FAIL | 299030 | C11_BATTERY_ORDERBOOK_RERATING | 61400.0 | None | None | 19.06 | None | stage2_captured_most_upside |
| C11_PNT_137400_2024_03_05_BATTERY_EQUIPMENT_ORDERBOOK_RERATING_4B | 137400 | C11_BATTERY_ORDERBOOK_RERATING | 44050.0 | None | None | 103.18 | None | stage2_actionable_best_entry |
| C11_PNT_137400_2024_03_06_BATTERY_EQUIPMENT_ORDERBOOK_RERATING_4B | 137400 | C11_BATTERY_ORDERBOOK_RERATING | 45900.0 | None | None | 94.99 | None | stage2_actionable_best_entry |
| C11_POSCOFM_003670_2024_02_15_CATHODE_ORDERBOOK_MARGIN_BRIDGE_FAIL | 003670 | C11_BATTERY_ORDERBOOK_RERATING | 300500.0 | None | None | 13.48 | None | stage2_captured_most_upside |
| C11_R3L93_020150_LEM_COPPER_FOIL_DECAY | 020150 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11_R3L93_121600_NANO_CNT_SPIKE_NO_FCF | 121600 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11_R3L93_348370_ENCHEM_ELECTROLYTE_ORDERBOOK | 348370 | C11_BATTERY_ORDERBOOK_RERATING | 169500.0 | None | None | 132.74 | None | stage2_actionable_best_entry |
| C11_SKC_011790_2024_03_05_COPPER_FOIL_ORDERBOOK_RERATING_4B | 011790 | C11_BATTERY_ORDERBOOK_RERATING | 95800.0 | None | None | 108.77 | None | stage2_actionable_best_entry |
| C11_SOLUS_336370_2024_03_27_COPPER_FOIL_ORDERBOOK_RERATING_HIGH_DRAWDOWN | 336370 | C11_BATTERY_ORDERBOOK_RERATING | 16970.0 | None | None | 38.48 | None | stage2_actionable_best_entry |
| C11_WONJUN_382840_2024_03_06_PROCESS_EQUIPMENT_ORDERBOOK_FAIL | 382840 | C11_BATTERY_ORDERBOOK_RERATING | 18170.0 | None | None | 13.65 | None | stage2_captured_most_upside |
| C11_YUNSUNG_372170_2024_03_06_MIXING_EQUIPMENT_ORDERBOOK_FAIL | 372170 | C11_BATTERY_ORDERBOOK_RERATING | 94200.0 | None | None | 6.79 | None | stage2_captured_most_upside |
| R3L98_C11_NANOCHEM_2024_CNT_MATERIAL_ORDERBOOK_EVENT_CAP_4B | 121600 | C11_BATTERY_ORDERBOOK_RERATING | None | None | 138000.0 | None | None | 4b_good_peak_capture |
| R3L98_C11_PNT_2024_BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE_POSITIVE | 137400 | C11_BATTERY_ORDERBOOK_RERATING | 43500.0 | None | None | 105.75 | None | stage2_actionable_best_entry |
| R3L98_C11_SAMSUNGSDI_2024_CELLMAKER_ORDERBOOK_FALSE_STAGE2 | 006400 | C11_BATTERY_ORDERBOOK_RERATING | 486000.0 | None | None | 1.75 | None | stage2_actionable_best_entry |

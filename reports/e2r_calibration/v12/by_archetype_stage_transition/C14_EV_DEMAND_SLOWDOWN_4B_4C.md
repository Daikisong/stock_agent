# C14_EV_DEMAND_SLOWDOWN_4B_4C Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `38`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 066970 | 066970 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| 247540 | 247540 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| 361610 | 361610 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| 373220 | 373220 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14-ECOPROBM-2024-01-22-CATHODE_CALL_OFF_DECAY | 247540 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 248000.0 | None | None | 19.56 | None | stage2_captured_most_upside |
| C14-LGES-2024-01-22-EV_DEMAND_SLOWDOWN_HARD_4C_STRESS | 373220 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 372000.0 | None | None | 19.35 | None | stage2_captured_most_upside |
| C14-LNF-2024-01-29-MATERIAL_DEMAND_BREAK | 066970 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 145100.0 | None | None | 37.15 | None | stage2_captured_most_upside |
| C14-SKIET-2024-01-22-SEPARATOR_UTILIZATION_BREAK | 361610 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 72100.0 | None | None | 10.96 | None | stage2_captured_most_upside |
| C14_006400_2024_CELL_UTILIZATION_4C_SUCCESS | 006400 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | 4c_too_late |
| C14_247540_2024_CATHODE_4B_SUCCESS | 247540 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 291000.0 | None | None | 4b_good_peak_capture |
| C14_373220_2024_HEADLINE_ONLY_FALSE_BREAK | 373220 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_CHUNBO_278280_2024_02_21_ELECTROLYTE_EV_DEMAND_HARD_4C | 278280 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | 4c_too_late |
| C14_CHUNBO_278280_2024_03_06_ELECTROLYTE_ADDITIVE_UTILIZATION_HARD_4C | 278280 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | 4c_too_late |
| C14_COSMO_005070_2024_02_21_CATHODE_EV_DEMAND_SLOWDOWN_HARD_4C | 005070 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | 4c_too_late |
| C14_ECOPROBM_247540_2024_03_06_EV_CATHODE_UTILIZATION_DEMAND_SLOWDOWN_HARD_4C | 247540 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | 4c_too_late |
| C14_ECOPROBM_247540_2024_03_25_EV_DEMAND_SLOWDOWN_HARD_4C_SUCCESS | 247540 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | 4c_too_late |
| C14_LGCHEM_051910_2024_02_21_EV_DEMAND_SLOWDOWN_CHEM_BATTERY_HARD_4C | 051910 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | 4c_too_late |
| C14_LGES_373220_2024_03_06_CELL_UTILIZATION_SLOWDOWN_OVERBLOCK_COUNTEREXAMPLE | 373220 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 387000.0 | None | None | 14.73 | None | stage2_captured_most_upside |
| C14_LGES_373220_2024_04_08_EV_DEMAND_SLOWDOWN_FALSE_4C | 373220 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_LNF_066970_2024_03_06_EV_CATHODE_CUSTOMER_CALL_OFF_HARD_4C | 066970 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | 4c_too_late |
| C14_LOTTEEM_020150_2024_02_21_FALSE_4C_COPPER_FOIL_ORDERBOOK_OFFSET | 020150 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_LOTTEENERGYMATERIALS_020150_2024_03_06_COPPER_FOIL_4B_TIMING_OVERBLOCK | 020150 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 36050.0 | None | None | 64.22 | None | stage2_captured_most_upside |
| C14_PNT_137400_2024_03_05_FALSE_4C_BROAD_EV_SLOWDOWN_OVERBLOCK | 137400 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_POSCOFUTUREM_003670_2024_03_06_CATHODE_UTILIZATION_ASP_HARD_4C | 003670 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | 4c_too_late |
| C14_R3L92_006110_SAM_A_ALUMINUM_FOIL_4B | 006110 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_R3L92_101360_ECODREAM_PRECURSOR_RAMP_FALSE_OVERBLOCK | 101360 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_R3L92_282880_COWINTECH_EQUIPMENT_CAPEX_DELAY_4B | 282880 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_R3L93_091580_SANGSIN_PARTS_DECAY | 091580 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_R3L93_137400_PNT_FALSE_OVERBLOCK | 137400 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_R3L93_365340_SUNGIL_RECYCLING_DEMAND_DECAY | 365340 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_SAMSUNGSDI_006400_2024_03_06_CELL_PREMATURE_4C_TIMING_COUNTEREXAMPLE | 006400 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 364500.0 | None | None | 35.67 | None | stage2_captured_most_upside |
| C14_SDI_006400_2024_03_25_EV_DEMAND_SLOWDOWN_RELIEF_RALLY_FAIL | 006400 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | 4c_too_late |
| C14_SKC_011790_2024_03_06_COPPER_FOIL_EXTREME_4B_TIMING_OVERBLOCK | 011790 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 96300.0 | None | None | 107.68 | None | stage2_captured_most_upside |
| C14_SKIET_361610_2024_03_06_SEPARATOR_UTILIZATION_DEMAND_SLOWDOWN_HARD_4C | 361610 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | 4c_too_late |
| C14_WCP_393890_2024_02_21_SEPARATOR_EV_DEMAND_UTILIZATION_HARD_4C | 393890 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | 4c_too_late |
| R3L98_C14_ECOPROBM_2024_CATHODE_DEMAND_SLOWDOWN_HARD_4C_PROTECTION | 247540 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| R3L98_C14_LGES_2024_CELLMAKER_UTILIZATION_FALSE_STAGE2 | 373220 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 410000.0 | None | None | 8.29 | None | stage2_actionable_best_entry |
| R3L98_C14_POSCOFUTUREM_2024_CATHODE_EVENT_CAP_4B | 003670 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 300500.0 | None | None | 4b_good_peak_capture |

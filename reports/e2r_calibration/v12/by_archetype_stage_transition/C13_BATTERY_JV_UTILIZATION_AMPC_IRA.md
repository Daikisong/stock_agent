# C13_BATTERY_JV_UTILIZATION_AMPC_IRA Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `15`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 006400 | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| 051910 | 051910 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| 373220 | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_COSMO_005070_2024_02_02_CATHODE_CAPA_UTILIZATION_RERATING | 005070 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 146500.0 | None | None | 32.63 | None | stage2_actionable_best_entry |
| C13_ECOPROMAT_450080_2024_02_13_PRECURSOR_CAPA_UTILIZATION_FALSE_POSITIVE | 450080 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 209500.0 | None | None | 0.95 | None | stage2_captured_most_upside |
| C13_LGCHEM_051910_2024_03_06_PARENT_BATTERY_JV_AMPC_LOOKTHROUGH_FAIL | 051910 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | 4c_too_late |
| C13_LGES_373220_2024_03_06_CELL_SCALE_AMPC_BUFFER_OVERBLOCK_COUNTEREXAMPLE | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 387000.0 | None | None | 14.73 | None | stage2_captured_most_upside |
| C13_LNF_066970_2024_02_14_CATHODE_JV_UTILIZATION_IRA_RERATING | 066970 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 144700.0 | None | None | 37.53 | None | stage2_actionable_best_entry |
| C13_R3L93_003670_POSCO_FUTUREM_JV_UTILIZATION | 003670 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 251000.0 | None | None | 34.06 | None | stage2_actionable_best_entry |
| C13_R3L93_086520_ECOPRO_AMPC_HOLDCO_DECAY | 086520 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_R3L93_278280_CHUNBO_ELECTROLYTE_CAPACITY_DECAY | 278280 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_SKINNOVATION_096770_2024_03_06_SKON_JV_UTILIZATION_AMPC_CASH_CONVERSION_HARD_4C | 096770 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | 4c_too_late |
| R3L98_C13_HANNONG_2024_SOLID_STATE_ELECTROLYTE_EVENT_CAP_4B | 011500 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | 25750.0 | None | None | 4b_good_peak_capture |
| R3L98_C13_LF_2024_CATHODE_IRA_AMPC_HIGH_MAE_FALSE_STAGE2 | 066970 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 178500.0 | None | None | 11.48 | None | stage2_actionable_best_entry |
| R3L98_C13_SOLBRAINHOLDINGS_2024_ELECTROLYTE_HOLDCO_JV_UTILIZATION_AMPC_BRIDGE_POSITIVE | 036830 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 50700.0 | None | None | 83.83 | None | stage2_actionable_best_entry |

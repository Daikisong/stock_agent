# C31_POLICY_SUBSIDY_LEGISLATION_EVENT Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `24`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C31-001470-UKR-REBUILD | 001470 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | None | None | None | None | no_valid_stage_transition |
| C31-009830-IRA-SOLAR | 009830 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 46550.0 | None | None | 22.4541 | None | stage2_actionable_best_entry |
| C31-053290-POLICY-THEME | 053290 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | None | None | None | None | no_valid_stage_transition |
| C31-112610-IRA-WIND | 112610 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 63600.0 | None | None | 38.5257 | None | stage2_actionable_best_entry |
| C31-336260-HYDROGEN-POLICY | 336260 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | None | None | None | None | no_valid_stage_transition |
| C31_034020_202203 | 034020 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 21100.0 | None | None | 13.2749 | None | stage2_actionable_best_entry |
| C31_052690_202203 | 052690 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 89500.0 | None | None | 7.82 | None | stage2_actionable_best_entry |
| C31_112610_202208 | 112610 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 63600.0 | None | 82300.0 | 38.5257 | 76.3192 | 4b_good_peak_capture |
| C31_336260_202007 | 336260 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 38350.0 | None | None | 70.5404 | None | stage2_actionable_best_entry |
| R11L10C31_034020_20240718 | 034020 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 21000.0 | None | None | 47.14 | None | stage2_actionable_best_entry |
| R11L10C31_036460_20240603 | 036460 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | None | None | None | None | None | no_valid_stage_transition |
| R11L10C31_052690_20240718 | 052690 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 82000.0 | None | None | 19.63 | None | stage2_actionable_best_entry |
| R11L13_C31_CS_WIND_IRA_WIND_TOWER_POSITIVE | 112610 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 55500.0 | None | None | 45.05 | None | stage2_actionable_best_entry |
| R11L13_C31_DOOSAN_FUELCELL_HYDROGEN_POLICY_COUNTEREX | 336260 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 32900.0 | None | None | 25.38 | None | stage2_actionable_best_entry |
| R11L13_C31_HD_ENERGY_IRA_SOLAR_POSITIVE_HIGH_MAE | 322000 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 50500.0 | None | None | 70.69 | None | stage2_actionable_best_entry |
| R11L13_C31_KVU_HYUNDAI_005380_20240226 | 005380 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 238500.0 | None | None | 25.58 | None | stage2_actionable_best_entry |
| R11L13_C31_KVU_HYUNDAI_005380_20240226 | None | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 238500.0 | None | None | 25.58 | None | stage2_actionable_best_entry |
| R11L13_C31_KVU_KB_105560_20240226 | 105560 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 62400.0 | None | None | 66.51 | None | stage2_actionable_best_entry |
| R11L13_C31_KVU_KB_105560_20240226 | None | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 62400.0 | None | None | 66.51 | None | stage2_actionable_best_entry |
| R11L13_C31_KVU_KEPCO_015760_20240226 | 015760 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 24200.0 | None | None | 5.17 | None | stage2_actionable_best_entry |
| R11L13_C31_KVU_KEPCO_015760_20240226 | None | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 24200.0 | None | None | 5.17 | None | stage2_actionable_best_entry |
| R11L13_C31_KVU_SCT_028260_20240226 | 028260 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 147400.0 | None | None | 15.88 | None | stage2_actionable_best_entry |
| R11L13_C31_KVU_SCT_028260_20240226 | None | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 147400.0 | None | None | 15.88 | None | stage2_actionable_best_entry |
| R11L13_C31_UNISON_IRA_WIND_THEME_COUNTEREX | 018000 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 2515.0 | None | None | 14.31 | None | stage2_actionable_best_entry |

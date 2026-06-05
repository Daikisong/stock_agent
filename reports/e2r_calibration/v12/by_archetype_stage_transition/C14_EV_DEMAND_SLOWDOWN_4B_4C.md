# C14_EV_DEMAND_SLOWDOWN_4B_4C Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `21`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C14_R3L88_093370_FOOSUNG_ELECTROLYTE_DEMAND_SLOWDOWN | 093370 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 8640.0 | None | None | 4b_good_peak_capture |
| C14_R3L88_336370_SOLUS_COPPERFOIL_DEMAND_BLOWOFF | 336370 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_R3L88_382840_WONIK_BATTERY_EQUIPMENT_REBOUND | 382840 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_R3L93_014820_2024_03_07 | 014820 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 41600.0 | None | None | 30.3 | None | stage2_captured_most_upside |
| C14_R3L93_222080_2024_03_05 | 222080 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_R3L93_336370_2024_03_27 | 336370 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 16970.0 | None | None | 27.9 | None | stage2_captured_most_upside |
| C14_R3L97_079810_2024_02_01 | 079810 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 12540.0 | None | None | 38.9 | None | stage2_captured_most_upside |
| C14_R3L97_217820_2024_02_01 | 217820 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 5600.0 | None | None | 30.4 | None | stage2_captured_most_upside |
| C14_R3L97_382480_2024_03_12 | 382480 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| R3L88_C14_LGCHEM_2023_EV_MATERIALS_4B_TO_4C_SLOWDOWN | 051910 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 728000.0 | None | None | 4b_good_peak_capture |
| R3L88_C14_SKC_2024_COPPERFOIL_FALSE_HARD_4C_RECOVERY | 011790 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| R3L88_C14_SKIET_2024_SEPARATOR_UTILIZATION_TRUE_4C | 361610 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| R3L91_C14_LENF_2024_EV_DEMAND_SLOWDOWN_HARD_4C | 066970 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| R3L91_C14_SANGAFRONTEC_2024_EV_MEMBRANE_FALSE_4C_RECOVERY | 089980 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| R3L91_C14_SOLUS_2024_COPPER_FOIL_EV_DEMAND_EVENT_CAP_4B | 336370 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 19900.0 | None | None | 4b_good_peak_capture |
| R9L93_C14_CIS_2024_BATTERY_EQUIPMENT_CAPEX_SLOWDOWN_FALSE_STAGE2 | 222080 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 13150.0 | None | None | 14.9 | None | stage2_actionable_best_entry |
| R9L93_C14_ECOPRO_2024_PARENT_EV_DEMAND_SLOWDOWN_EVENT_CAP_4B | 086520 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 104400.0 | None | None | 4b_good_peak_capture |
| R9L93_C14_SKINNOVATION_2024_INTEGRATED_BATTERY_REFINING_FUNDING_BRIDGE_POSITIVE | 096770 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 112100.0 | None | None | 16.77 | None | stage2_actionable_best_entry |
| R9L95_C14_DONGWHA_2024_ELECTROLYTE_POST_CA_EV_DEMAND_EVENT_CAP_4B | 025900 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 19020.0 | None | None | 4b_good_peak_capture |
| R9L95_C14_SKIET_2024_SEPARATOR_DEMAND_SLOWDOWN_4C_GUARD_SUCCESS | 361610 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| R9L95_C14_WCP_2024_SEPARATOR_CAPACITY_RECOVERY_FALSE_STAGE2 | 393890 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 47100.0 | None | None | 5.1 | None | stage2_actionable_best_entry |

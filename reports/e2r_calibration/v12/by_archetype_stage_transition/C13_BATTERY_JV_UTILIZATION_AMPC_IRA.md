# C13_BATTERY_JV_UTILIZATION_AMPC_IRA Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `27`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C13_LGES_2024_04_25_AMPC_CUSHIONED_LOSS_BUT_CAPEX_UTILIZATION_BRIDGE | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 372500.0 | None | None | 19.2 | None | stage2_actionable_best_entry |
| C13_R3L84_051910_LGCHEM_HOLDCO_BATTERY_JV_DISCOUNT | 051910 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_R3L84_361610_SKIET_SEPARATOR_UTILIZATION_SHORTFALL | 361610 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_R3L84_373220_LGES_AMPC_JV_UTILIZATION_BRIDGE | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 350000.0 | None | None | 26.86 | None | stage2_actionable_best_entry |
| C13_R3L87_011790_SKC_COPPERFOIL_JV_THEME | 011790 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_R3L87_051910_LGCHEM_BATTERY_CHEM_THEME | 051910 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_R3L87_096770_SKINNOVATION_JV_AMPC_UTILIZATION | 096770 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 108300.0 | None | None | 20.87 | None | stage2_actionable_best_entry |
| C13_R3L91_014820_DONGWON_PACKAGING_CAN_MATERIALS | 014820 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_R3L91_036830_SOLBRAIN_HOLDINGS_ELECTROLYTE_JV | 036830 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 39550.0 | None | None | 122.0 | None | stage2_actionable_best_entry |
| C13_R3L91_095500_MIRAE_NANOTECH_LITHIUM_IRA_VOCABULARY | 095500 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_R3L94_121600_2024_02_21 | 121600 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 134000.0 | None | None | 17.8 | None | stage2_actionable_best_entry |
| C13_R3L94_393890_2024_02_21 | 393890 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_R3L94_450080_2024_02_01 | 450080 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 173600.0 | None | None | 21.8 | None | stage2_captured_most_upside |
| C13_R3L98_078600_2024_02_01 | 078600 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 71200.0 | None | None | 81.7 | None | stage2_captured_most_upside |
| C13_R3L98_357780_2024_02_01 | 357780 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 270000.0 | None | None | 19.3 | None | stage2_captured_most_upside |
| C13_R3L98_361610_2024_02_01 | 361610 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_SDI_2024_12_04_STARPLUS_DOE_LOAN_VS_SLOW_EV_DEMAND | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_SKI_2024_12_16_BLUEOVAL_LOAN_POST_CORPACT_UTILIZATION_RISK | 096770 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 121400.0 | None | None | 15.5 | None | stage2_captured_most_upside |
| R3L92_C13_LGES_2024_CELL_AMPC_UTILIZATION_FALSE_STAGE2 | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 410000.0 | None | None | 8.29 | None | stage2_actionable_best_entry |
| R3L92_C13_SAMSDI_2024_CELL_JV_UTILIZATION_AMPC_BRIDGE_POSITIVE | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 354000.0 | None | None | 39.69 | None | stage2_actionable_best_entry |
| R3L92_C13_WCP_2024_SEPARATOR_AMPC_EVENT_CAP_4B | 393890 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | 47100.0 | None | None | 4b_good_peak_capture |
| R3L95_C13_DONGWONSYSTEMS_2024_BATTERY_PACKAGING_CAN_JV_UTILIZATION_MARGIN_POSITIVE | 014820 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 34700.0 | None | None | 50.43 | None | stage2_actionable_best_entry |
| R3L95_C13_ECOPROMATERIALS_2024_PRECURSOR_IRA_EVENT_CAP_4B | 450080 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | 127000.0 | None | None | 4b_good_peak_capture |
| R3L95_C13_FOOSUNG_2024_ELECTROLYTE_FLUOROCHEM_AMPC_FALSE_STAGE2 | 093370 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 8970.0 | None | None | 3.01 | None | stage2_actionable_best_entry |
| R9L89_C13_SEBANG_2024_BATTERY_VOLUME_MARGIN_BRIDGE_POSITIVE | 004490 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 54600.0 | None | None | 124.36 | None | stage2_actionable_best_entry |
| R9L89_C13_SHINHEUNG_2024_BATTERY_PARTS_CALL_OFF_FALSE_STAGE2 | 243840 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 9640.0 | None | None | 8.61 | None | stage2_actionable_best_entry |
| R9L89_C13_WCP_2024_SEPARATOR_CUSTOMER_UTILIZATION_EVENT_CAP_4B | 393890 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | 47100.0 | None | None | 4b_good_peak_capture |

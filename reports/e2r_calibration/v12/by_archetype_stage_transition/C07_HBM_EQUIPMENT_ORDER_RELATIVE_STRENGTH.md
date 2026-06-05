# C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `18`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C07_R2L84_089790_JT_TEST_HANDLER_NO_ORDER_BRIDGE | 089790 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | None | None | None | None | None | no_valid_stage_transition |
| C07_R2L84_092870_EXICON_TESTER_REBOUND_NO_BRIDGE | 092870 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | None | None | None | None | None | no_valid_stage_transition |
| C07_R2L84_232140_YC_HBM_TESTER_ORDER_BRIDGE | 232140 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 7280.0 | None | None | 215.25 | None | stage2_actionable_best_entry |
| C07_R2L86_036930_JUSUNG_HBM_ALD_ORDER_BRIDGE | 036930 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 33800.0 | None | None | 22.63 | None | stage2_actionable_best_entry |
| C07_R2L86_084370_EUGENE_LATE_EXTENSION_NO_FRESH_ORDER | 084370 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | None | None | None | None | None | no_valid_stage_transition |
| C07_R2L86_240810_WONIKIPS_MEMORY_EQUIPMENT_BETA_SPIKE | 240810 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | None | None | None | None | None | no_valid_stage_transition |
| C07_R2L91_084370_EUGENE_TECH_HBM_DEPOSITION_ORDER_RAMP | 084370 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 37500.0 | None | None | 60.0 | None | stage2_actionable_best_entry |
| C07_R2L91_086390_UNITEST_MEMORY_TESTER_THEME | 086390 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | None | None | None | None | None | no_valid_stage_transition |
| C07_R2L91_217190_GENESSEM_BACKEND_HBM_POSTPROCESS | 217190 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | None | None | None | None | None | no_valid_stage_transition |
| C07_R2L95_039030_2024_02_28 | 039030 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 202000.0 | None | None | 39.1 | None | stage2_actionable_best_entry |
| C07_R2L95_083450_2024_08_26 | 083450 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 17500.0 | None | None | 9.4 | None | stage2_captured_most_upside |
| C07_R2L95_095610_2024_04_17 | 095610 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | None | None | None | None | None | no_valid_stage_transition |
| R2L90_C07_STI_2024_HBM_REFLOW_THEME_EVENT_CAP_4B | 039440 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | None | None | 38750.0 | None | None | 4b_good_peak_capture |
| R2L90_C07_UNISEM_2024_SCRUBBER_EQUIPMENT_THEME_FALSE_STAGE2 | 036200 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 11570.0 | None | None | 7.87 | None | stage2_actionable_best_entry |
| R2L90_C07_YC_2024_HBM_TEST_EQUIPMENT_ORDER_RS_POSITIVE | 232140 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 5900.0 | None | None | 227.12 | None | stage2_actionable_best_entry |
| R2L94_C07_NEOSEM_2024_MEMORY_TESTER_HEADLINE_FALSE_STAGE2 | 253590 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 15810.0 | None | None | 9.23 | None | stage2_actionable_best_entry |
| R2L94_C07_TECHWING_2024_HBM_TEST_HANDLER_ORDER_CAPACITY_POSITIVE | 089030 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 18900.0 | None | None | 274.6 | None | stage2_actionable_best_entry |
| R2L94_C07_TFE_2024_HBM_SOCKET_PACKAGE_EVENT_CAP_4B | 425420 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | None | None | 43100.0 | None | None | 4b_good_peak_capture |

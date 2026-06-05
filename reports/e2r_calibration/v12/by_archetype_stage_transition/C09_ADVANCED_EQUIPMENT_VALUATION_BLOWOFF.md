# C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `15`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C09_R2L83_140860_PARKSYSTEMS_AFM_REVENUE_BRIDGE | 140860 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 164600.0 | None | None | 51.88 | None | stage2_actionable_best_entry |
| C09_R2L83_240810_WONIKIPS_MEMORY_EQUIPMENT_ROUNDTRIP_4B_WATCH | 240810 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 32800.0 | None | None | 36.74 | None | stage2_actionable_best_entry |
| C09_R2L83_403870_HPSP_ADVANCED_EQUIPMENT_BLOWOFF_HIGH_MAE | 403870 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | None | None | None | None | None | no_valid_stage_transition |
| C09_R2L88_039030_EOTECH_ADVANCED_LASER_ORDER_MARGIN | 039030 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 202000.0 | None | None | 39.11 | None | stage2_actionable_best_entry |
| C09_R2L88_253590_NEOSEM_LATE_TESTER_VALUATION_EXTENSION | 253590 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | None | None | None | None | None | no_valid_stage_transition |
| C09_R2L88_412350_LASERSEL_THEME_BLOWOFF | 412350 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | None | None | None | None | None | no_valid_stage_transition |
| C09_R2L92_036810_2024_04_09 | 036810 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 27900.0 | None | None | 50.0 | None | stage2_captured_most_upside |
| C09_R2L92_084370_2024_03_21 | 084370 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 41450.0 | None | None | 44.8 | None | stage2_actionable_best_entry |
| C09_R2L92_240810_2024_03_20 | 240810 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | None | None | None | None | None | no_valid_stage_transition |
| C09_R2L97_036930_2024_02_22 | 036930 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 31900.0 | None | None | 29.9 | None | stage2_captured_most_upside |
| C09_R2L97_083310_2024_02_22 | 083310 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | None | None | None | None | None | no_valid_stage_transition |
| C09_R2L97_084370_2024_03_21 | 084370 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 41450.0 | None | None | 41.6 | None | stage2_captured_most_upside |
| R2L88_C09_EOTECH_2024_ADVANCED_EQUIPMENT_RERATING_POSITIVE | 039030 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 183900.0 | None | None | 52.8 | None | stage2_actionable_best_entry |
| R2L88_C09_PARKSYSTEMS_2024_ADVANCED_TOOL_VALUATION_FALSE_STAGE2 | 140860 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 187800.0 | None | None | 7.3 | None | stage2_actionable_best_entry |
| R2L88_C09_SNSTECH_2024_EUV_MASK_EVENT_CAP_4B | 101490 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | None | None | 48500.0 | None | None | 4b_good_peak_capture |

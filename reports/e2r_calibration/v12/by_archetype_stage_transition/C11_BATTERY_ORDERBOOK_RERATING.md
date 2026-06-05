# C11_BATTERY_ORDERBOOK_RERATING Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `23`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C11_R3L85_078600_DAEJOO_SILICON_ANODE_CUSTOMER_CAPACITY | 078600 | C11_BATTERY_ORDERBOOK_RERATING | 98900.0 | None | None | 65.22 | None | stage2_actionable_best_entry |
| C11_R3L85_247540_ECOPROBM_ORDERBOOK_HEADLINE_CALLOFF_RISK | 247540 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11_R3L85_393890_WCP_SEPARATOR_ORDERBOOK_THEME | 393890 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11_R3L89_089980_SANGA_SEPARATOR_MATERIALS_REBOUND | 089980 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11_R3L89_222080_CIS_BATTERY_EQUIPMENT_ORDERBOOK | 222080 | C11_BATTERY_ORDERBOOK_RERATING | 11000.0 | None | None | 37.36 | None | stage2_actionable_best_entry |
| C11_R3L89_290670_DAEBO_MAGNETIC_NO_FRESH_ORDER | 290670 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11_R3L91_006110_2024_02_20 | 006110 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11_R3L91_020150_2024_03_20 | 020150 | C11_BATTERY_ORDERBOOK_RERATING | 42350.0 | None | None | 23.7 | None | stage2_captured_most_upside |
| C11_R3L95_006110_2024_02_14 | 006110 | C11_BATTERY_ORDERBOOK_RERATING | 91300.0 | None | None | 27.5 | None | stage2_captured_most_upside |
| C11_R3L95_008730_2024_02_05 | 008730 | C11_BATTERY_ORDERBOOK_RERATING | 30850.0 | None | None | 59.2 | None | stage2_captured_most_upside |
| C11_R3L95_277880_2024_03_12 | 277880 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11_R3L99_282880_2024_02_01 | 282880 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11_R3L99_290670_2024_02_01 | 290670 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11_R3L99_382840_2024_09_23 | 382840 | C11_BATTERY_ORDERBOOK_RERATING | 12720.0 | None | None | 36.8 | None | stage2_captured_most_upside |
| R3L89_C11_DAEJOO_2024_SILICON_ANODE_ORDER_REVISION_POSITIVE | 078600 | C11_BATTERY_ORDERBOOK_RERATING | 76000.0 | None | None | 115.0 | None | stage2_actionable_best_entry |
| R3L89_C11_JEO_2024_CNT_CONDUCTIVE_ADDITIVE_EVENT_CAP_4B | 418550 | C11_BATTERY_ORDERBOOK_RERATING | None | None | 28050.0 | None | None | 4b_good_peak_capture |
| R3L89_C11_ONEJOON_2024_BATTERY_EQUIPMENT_FALSE_STAGE2 | 382840 | C11_BATTERY_ORDERBOOK_RERATING | 18910.0 | None | None | 12.64 | None | stage2_actionable_best_entry |
| R3L93_C11_DUKSAN_2024_ELECTROLYTE_ADDITIVE_CUSTOMER_ORDERBOOK_POSITIVE | 317330 | C11_BATTERY_ORDERBOOK_RERATING | 23850.0 | None | None | 183.02 | None | stage2_actionable_best_entry |
| R3L93_C11_WONJUN_2024_BATTERY_EQUIPMENT_ORDERBOOK_FALSE_STAGE2 | 382840 | C11_BATTERY_ORDERBOOK_RERATING | 19110.0 | None | None | 8.06 | None | stage2_actionable_best_entry |
| R3L93_C11_YULCHONCHEM_2024_POUCH_FILM_ORDERBOOK_EVENT_CAP_4B | 008730 | C11_BATTERY_ORDERBOOK_RERATING | None | None | 45250.0 | None | None | 4b_good_peak_capture |
| R3L96_C11_DENT_2024_BATTERY_EQUIPMENT_ORDERBOOK_FALSE_STAGE2 | 079810 | C11_BATTERY_ORDERBOOK_RERATING | 17000.0 | None | None | 2.47 | None | stage2_actionable_best_entry |
| R3L96_C11_NANOTIM_2024_THERMAL_MANAGEMENT_BATTERY_ORDER_EVENT_CAP_4B | 417010 | C11_BATTERY_ORDERBOOK_RERATING | None | None | 14790.0 | None | None | 4b_good_peak_capture |
| R3L96_C11_SAMAALUMINUM_2024_BATTERY_FOIL_ORDERBOOK_MARGIN_POSITIVE | 006110 | C11_BATTERY_ORDERBOOK_RERATING | 82100.0 | None | None | 41.78 | None | stage2_actionable_best_entry |

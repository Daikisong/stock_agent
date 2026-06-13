# C11_BATTERY_ORDERBOOK_RERATING Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `56`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 001530 | 001530 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| 002710 | 002710 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| 014820 | 014820 | C11_BATTERY_ORDERBOOK_RERATING | 43400.0 | None | None | 3.34 | None | stage2_actionable_best_entry |
| 089980 | 089980 | C11_BATTERY_ORDERBOOK_RERATING | None | None | 25950.0 | None | None | no_valid_stage_transition |
| 091580 | 091580 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| 093370 | 093370 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| 096770 | 096770 | C11_BATTERY_ORDERBOOK_RERATING | 177500.0 | None | None | 29.3 | None | stage2_actionable_best_entry |
| 101360 | 101360 | C11_BATTERY_ORDERBOOK_RERATING | 27700.0 | None | None | 6.3177 | None | stage2_actionable_best_entry |
| 278280 | 278280 | C11_BATTERY_ORDERBOOK_RERATING | None | None | 103400.0 | None | None | no_valid_stage_transition |
| 290670 | 290670 | C11_BATTERY_ORDERBOOK_RERATING | None | None | 24950.0 | None | None | no_valid_stage_transition |
| C11-217820-20231020-WONIKPNE-BACKLOG-MARGIN-QUALITY-FAIL | 217820 | C11_BATTERY_ORDERBOOK_RERATING | 6880.0 | None | None | 13.37 | None | stage2_actionable_best_entry |
| C11-220-01 | 083930 | C11_BATTERY_ORDERBOOK_RERATING | 13280.0 | None | None | 61.14 | None | stage2_actionable_best_entry |
| C11-220-02 | 302430 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11-220-03 | 302430 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11-220-04 | 302430 | C11_BATTERY_ORDERBOOK_RERATING | 8210.0 | None | None | 47.87 | None | stage2_actionable_best_entry |
| C11-220-05 | 382480 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11-220-06 | 382480 | C11_BATTERY_ORDERBOOK_RERATING | 2045.0 | None | None | 49.14 | None | stage2_actionable_best_entry |
| C11-220-07 | 452400 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11-220-08 | 452400 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11-220-09 | 254120 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11-220-10 | 254120 | C11_BATTERY_ORDERBOOK_RERATING | 1260.0 | None | None | 71.83 | None | stage2_actionable_best_entry |
| C11-220-11 | 079810 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11-220-12 | 079810 | C11_BATTERY_ORDERBOOK_RERATING | 5140.0 | None | None | 61.48 | None | stage2_actionable_best_entry |
| C11-277880-20240528-TSI-MIXING-BACKLOG-CHASM-4B | 277880 | C11_BATTERY_ORDERBOOK_RERATING | None | None | 8270.0 | None | None | no_valid_stage_transition |
| C11-282880-20230222-COWIN-BACKLOG-TURNKEY-MARGIN | 282880 | C11_BATTERY_ORDERBOOK_RERATING | 25100.0 | None | None | 87.25 | None | stage2_actionable_best_entry |
| C11-299030-20240304-HANATECH-BACKLOG-DELAY-QUALITY-FAIL | 299030 | C11_BATTERY_ORDERBOOK_RERATING | 60200.0 | None | None | 21.43 | None | stage2_actionable_best_entry |
| C11-372170-20221216-YUNSUNG-MIXING-BACKLOG-SKON | 372170 | C11_BATTERY_ORDERBOOK_RERATING | 45100.0 | None | None | 495.34 | None | stage2_actionable_best_entry |
| C11L148_251630_20240118_VONETECH_LGE_90B_INSPECTION_ORDER | 251630 | C11_BATTERY_ORDERBOOK_RERATING | 12200.0 | None | None | 3.28 | None | stage2_actionable_best_entry |
| C11L148_262260_20230511_APRO_ACTIVATION_EQUIPMENT_ORDER_CYCLE | 262260 | C11_BATTERY_ORDERBOOK_RERATING | 16390.0 | None | None | 37.28 | None | stage2_actionable_best_entry |
| C11L148_267320_20230403_NINETECH_LGE_207B_ORDER | 267320 | C11_BATTERY_ORDERBOOK_RERATING | 3820.0 | None | None | 63.61 | None | stage2_captured_most_upside |
| C11L148_333620_20240813_NSYS_Q2_ORDER_CONVERSION | 333620 | C11_BATTERY_ORDERBOOK_RERATING | 8950.0 | None | None | 46.15 | None | stage2_actionable_best_entry |
| C11L148_360070_20230308_TOPMATERIAL_693B_SYSTEM_ENGINEERING | 360070 | C11_BATTERY_ORDERBOOK_RERATING | 53000.0 | None | None | 80.38 | None | stage2_actionable_best_entry |
| C11L148_360070_20240513_TOPMATERIAL_NEW_ORDER_GROWTH_FORECAST | 360070 | C11_BATTERY_ORDERBOOK_RERATING | 52900.0 | None | None | 11.34 | None | stage2_captured_most_upside |
| C11L148_382840_20240422_WONJUN_HEAT_TREATMENT_TECHNOLOGY_EXPECTATION | 382840 | C11_BATTERY_ORDERBOOK_RERATING | 15580.0 | None | None | 11.68 | None | stage2_captured_most_upside |
| C11_003670_POSCO_FUTURE_M_20230215_SAMSUNG_SDI_CATHODE_10Y_CONTRACT | 003670 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11_011790_SKC_20230220_NORTHVOLT_COPPER_FOIL_ORDERBOOK_MARGIN_RISK | 011790 | C11_BATTERY_ORDERBOOK_RERATING | 97300.0 | None | None | 25.69 | None | stage2_actionable_best_entry |
| C11_066970_LNF_20230228_TESLA_CATHODE_ORDERBOOK_HIGH_MAE | 066970 | C11_BATTERY_ORDERBOOK_RERATING | None | None | 262000.0 | None | None | no_valid_stage_transition |
| C11_348370_ENCHEM_20230912_US_ELECTROLYTE_LOCALIZATION_CAPACITY | 348370 | C11_BATTERY_ORDERBOOK_RERATING | 62300.0 | None | None | 533.23 | None | stage2_actionable_best_entry |
| C11_393890_WCP_20230802_SAMSUNG_SDI_SEPARATOR_SUPPLY_HIGH_MAE | 393890 | C11_BATTERY_ORDERBOOK_RERATING | None | None | 79000.0 | None | None | no_valid_stage_transition |
| C11_L141_01_POSCO_FUTURE_M_20230130_SDI_40T | 003670 | C11_BATTERY_ORDERBOOK_RERATING | 224000.0 | None | None | 209.82 | None | stage2_actionable_best_entry |
| C11_L141_02_ECOPROBM_20231201_SDI_44T | 247540 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11_L141_03_PNT_20240416_ELECTRODE_EQUIPMENT_CONTRACT | 137400 | C11_BATTERY_ORDERBOOK_RERATING | 38650.0 | None | None | 131.57 | None | stage2_actionable_best_entry |
| C11_L141_04_CIS_20240327_BACKLOG_EXPECTATION | 222080 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11_L141_05_PHILENERGY_20231117_ADVANCED_STACKER_ORDER | 378340 | C11_BATTERY_ORDERBOOK_RERATING | 19160.0 | None | None | 86.33 | None | stage2_actionable_best_entry |
| C11_L141_06_MPLUS_20230817_BACKLOG_3X_SALES | 259630 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11_R3_L107_065350_신성델타테크_ORDERBOOK_BOUNDARY_2023-04-28 | 065350 | C11_BATTERY_ORDERBOOK_RERATING | None | None | 10930.0 | None | None | no_valid_stage_transition |
| C11_R3_L107_121600_나노신소재_ORDERBOOK_BOUNDARY_2024-07-23 | 121600 | C11_BATTERY_ORDERBOOK_RERATING | None | None | 95200.0 | None | None | no_valid_stage_transition |
| C11_R3_L107_251630_브이원텍_ORDERBOOK_BOUNDARY_2023-01-25 | 251630 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11_R3_L107_333620_엔시스_ORDERBOOK_BOUNDARY_2022-10-20 | 333620 | C11_BATTERY_ORDERBOOK_RERATING | 12250.0 | None | None | 34.5306 | None | stage2_actionable_best_entry |
| C11_R3_L107_396300_세아메카닉스_ORDERBOOK_BOUNDARY_2023-05-19 | 396300 | C11_BATTERY_ORDERBOOK_RERATING | None | None | 6610.0 | None | None | no_valid_stage_transition |
| C11_R3_L107_419050_삼기에너지솔루션즈_ORDERBOOK_BOUNDARY_2024-12-05 | 419050 | C11_BATTERY_ORDERBOOK_RERATING | 1850.0 | None | None | 41.3514 | None | stage2_actionable_best_entry |
| C11_R3_L108_008730_율촌화학_ORDERBOOK_BOUNDARY_2 | 008730 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11_R3_L108_024840_KBI메탈_ORDERBOOK_BOUNDARY_5 | 024840 | C11_BATTERY_ORDERBOOK_RERATING | None | None | 3035.0 | None | None | no_valid_stage_transition |
| C11_R3_L108_025820_이구산업_ORDERBOOK_BOUNDARY_4 | 025820 | C11_BATTERY_ORDERBOOK_RERATING | 4035.0 | None | None | 52.4164 | None | stage2_actionable_best_entry |
| C11_R3_L108_051980_중앙첨단소재_ORDERBOOK_BOUNDARY_1 | 051980 | C11_BATTERY_ORDERBOOK_RERATING | None | None | None | None | None | no_valid_stage_transition |
| C11_R3_L108_114190_강원에너지_ORDERBOOK_BOUNDARY_3 | 114190 | C11_BATTERY_ORDERBOOK_RERATING | 14790.0 | None | None | 54.1582 | None | stage2_actionable_best_entry |

# C19_BRAND_RETAIL_INVENTORY_MARGIN Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `30`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 004170 | 004170 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 159900.0 | None | None | 13.2 | None | stage2_actionable_best_entry |
| 007070 | 007070 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 18810.0 | None | None | 23.34 | None | stage2_actionable_best_entry |
| 008770 | 008770 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | None | None | None | no_valid_stage_transition |
| 020000 | 020000 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | None | None | None | no_valid_stage_transition |
| 093050 | 093050 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 13650.0 | None | None | 22.42 | None | stage2_actionable_best_entry |
| 139480 | 139480 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | None | None | None | no_valid_stage_transition |
| 282330 | 282330 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 118500.0 | None | None | 14.94 | None | stage2_actionable_best_entry |
| 337930 | 337930 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 5120.0 | None | None | 161.33 | None | stage2_actionable_best_entry |
| C19_CEX_031430_20230208_REOPENING_RETAIL_MARGIN_FALSE_PROMOTION | 031430 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | None | None | None | no_valid_stage_transition |
| C19_CEX_298540_20230418_NATIONALGEOGRAPHIC_INVENTORY_MARGIN_FADE | 298540 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | None | None | None | no_valid_stage_transition |
| C19_POS_036620_20230515_SNOWPEAK_RETAIL_SELLTHROUGH_MARGIN | 036620 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 3150.0 | None | 4600.0 | 56.83 | 80.999 | stage2_actionable_best_entry |
| C19_POS_337930_20240516_XEXYMIX_CHANNEL_MARGIN_RERATING | 337930 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 5080.0 | None | 8520.0 | 163.39 | 41.4447 | stage2_actionable_best_entry |
| C19_R5L71_BGFRETAIL_2024Q1_COST_WEATHER_MARGIN_BREAK | 282330 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | 127800.0 | None | None | 4b_too_early |
| C19_R5L71_GSRETAIL_2023Q1_TRAFFIC_MARGIN_FALSE_START | 007070 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 27600.0 | None | None | 1.4 | None | stage2_actionable_best_entry |
| C19_R5L71_LOTTE_2023Q3_MARGIN_RECOVERY | 023530 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 77700.0 | None | None | 18.5 | None | stage2_actionable_best_entry |
| R5L71_C19_071840_APPLIANCE_RETAIL_DEMAND_INVENTORY_BREAK_20220316 | 071840 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 25200.0 | None | None | 1.19 | None | stage2_captured_most_upside |
| R5L71_C19_139480_BIGBOX_MARGIN_FALSE_START_20230215 | 139480 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 115500.0 | None | None | 3.81 | None | stage2_captured_most_upside |
| R5L71_C19_282330_CU_CONVENIENCE_SELLTHROUGH_20220211 | 282330 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 167500.0 | None | None | 21.79 | None | stage2_actionable_best_entry |
| R5L73_C19_007070_20230208_RETAIL_OMNICHANNEL_MARGIN_FALSE_START | 007070 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 30600.0 | None | None | 0.98 | None | stage2_actionable_best_entry |
| R5L73_C19_139480_20230214_BIGBOX_INVENTORY_MARGIN_DEMAND_FALSE_START | 139480 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 110000.0 | None | None | 9.0 | None | stage2_actionable_best_entry |
| R5L73_C19_282330_20220316_CSTORE_DEFENSIVE_VOLUME_MARGIN_BRIDGE | 282330 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 179000.0 | None | None | 17.32 | None | stage2_actionable_best_entry |
| R5L76_C19_004170_20240129_DEPARTMENT_STORE_VALUEUP_MFE_NO_DURABLE_MARGIN_BRIDGE | 004170 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 170700.0 | None | None | 11.48 | None | stage2_actionable_best_entry |
| R5L76_C19_093050_20240129_APPAREL_BRAND_INVENTORY_MARGIN_CASHFLOW_BRIDGE | 093050 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 12890.0 | None | None | 29.64 | None | stage2_actionable_best_entry |
| R5L76_C19_282330_20240129_CONVENIENCE_RETAIL_MARGIN_THEME_LOW_MFE_HIGH_MAE | 282330 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 144600.0 | None | None | 1.73 | None | stage2_actionable_best_entry |
| R5L83-C19-01 | 282330 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 103900.0 | None | None | 20.31 | None | stage2_actionable_best_entry |
| R5L83-C19-02 | 004170 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | None | None | None | no_valid_stage_transition |
| R5L83-C19-03 | 093050 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | None | None | None | no_valid_stage_transition |
| R5L86-C19-01 | 337930 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 6290.0 | None | None | 112.72 | None | stage2_actionable_best_entry |
| R5L86-C19-02 | 093050 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 13640.0 | None | None | 16.72 | None | stage2_actionable_best_entry |
| R5L86-C19-03 | 031430 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | None | None | None | no_valid_stage_transition |

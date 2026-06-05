# C19_BRAND_RETAIL_INVENTORY_MARGIN Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `24`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C19_R5L87_008770_SHILLA_DUTYFREE_NO_MARGIN_BRIDGE | 008770 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | None | None | None | no_valid_stage_transition |
| C19_R5L87_031430_SI_FASHION_INVENTORY_NO_MARGIN | 031430 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | None | None | None | no_valid_stage_transition |
| C19_R5L87_069960_HYUNDAI_RETAIL_INVENTORY_MARGIN | 069960 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 51200.0 | None | None | 20.9 | None | stage2_actionable_best_entry |
| C19_R5L89_008770_20240401 | 008770 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | None | None | None | no_valid_stage_transition |
| C19_R5L89_023530_20240129 | 023530 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | None | None | None | no_valid_stage_transition |
| C19_R5L89_069960_20240129 | 069960 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | None | None | None | no_valid_stage_transition |
| C19_R5L90_020000_HANSOME_PREMIUM_APPAREL_REBOUND | 020000 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | None | None | None | no_valid_stage_transition |
| C19_R5L90_090430_AMORE_BEAUTY_CHANNEL_MARGIN | 090430 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 135000.0 | None | None | 48.52 | None | stage2_actionable_best_entry |
| C19_R5L90_383220_FNF_APPAREL_INVENTORY_DESTOCKING | 383220 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | None | None | None | no_valid_stage_transition |
| C19_R5L93_105630_2024_03_07 | 105630 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 18220.0 | None | None | 24.0 | None | stage2_actionable_best_entry |
| C19_R5L93_298540_2024_04_01 | 298540 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | None | None | None | no_valid_stage_transition |
| C19_R5L93_383220_2024_04_01 | 383220 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | None | None | None | no_valid_stage_transition |
| C19_R5L96_023530_2024_01_29 | 023530 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 79400.0 | None | None | 16.0 | None | stage2_actionable_best_entry |
| C19_R5L96_031430_2024_03_27 | 031430 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | None | None | None | no_valid_stage_transition |
| C19_R5L96_069960_2024_02_01 | 069960 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 58100.0 | None | None | 6.5 | None | stage2_captured_most_upside |
| R5L90_C19_09WOMEN_2024_SIZE_APPAREL_RETAIL_EVENT_CAP_4B | 366030 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | 6290.0 | None | None | 4b_good_peak_capture |
| R5L90_C19_GAMSUNG_2024_OUTDOOR_BRAND_REORDER_MARGIN_POSITIVE | 036620 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 2840.0 | None | None | 65.14 | None | stage2_actionable_best_entry |
| R5L90_C19_SI_2024_LUXURY_RETAIL_INVENTORY_FALSE_STAGE2 | 031430 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 18170.0 | None | None | 1.05 | None | stage2_actionable_best_entry |
| R5L93_C19_HANDSOME_2024_FASHION_RETAIL_INVENTORY_FALSE_STAGE2 | 020000 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 21550.0 | None | None | 0.46 | None | stage2_actionable_best_entry |
| R5L93_C19_HWASEUNGENTERPRISE_2024_FOOTWEAR_OEM_INVENTORY_RESTOCKING_MARGIN_POSITIVE | 241590 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 7630.0 | None | None | 33.16 | None | stage2_actionable_best_entry |
| R5L93_C19_NATUREHOLDINGS_2024_OUTDOOR_BRAND_INVENTORY_EVENT_CAP_4B | 298540 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | 16350.0 | None | None | 4b_good_peak_capture |
| R5L97_C19_FNF_2024_APPAREL_CHINA_INVENTORY_FALSE_STAGE2 | 383220 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 76500.0 | None | None | 1.18 | None | stage2_actionable_best_entry |
| R5L97_C19_HOTELSHILLA_2024_DUTY_FREE_RETAIL_EVENT_CAP_4B | 008770 | C19_BRAND_RETAIL_INVENTORY_MARGIN | None | None | 62900.0 | None | None | 4b_good_peak_capture |
| R5L97_C19_LOTTESHOPPING_2024_DEPARTMENT_STORE_RETAIL_INVENTORY_MARGIN_POSITIVE | 023530 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 71800.0 | None | None | 28.27 | None | stage2_actionable_best_entry |

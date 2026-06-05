# C18_CONSUMER_EXPORT_CHANNEL_REORDER Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `33`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C18_R5L84_005180_BINGGRAE_EXPORT_REORDER_BRIDGE | 005180 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 61900.0 | None | None | 91.28 | None | stage2_actionable_best_entry |
| C18_R5L84_005610_SPC_CHANNEL_SPIKE_NO_MARGIN_BRIDGE | 005610 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| C18_R5L84_011150_CJSEAFOOD_EXPORT_THEME_SPIKE | 011150 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| C18_R5L86_003230_SAMYANG_KFOOD_EXPORT_REORDER | 003230 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 183800.0 | None | None | 290.64 | None | stage2_actionable_best_entry |
| C18_R5L86_005610_SPC_DOMESTIC_FOOD_REBOUND_NO_REORDER | 005610 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| C18_R5L86_007310_OTTOGI_CHANNEL_THEME_NO_FRESH_REORDER | 007310 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| C18_R5L89_005180_BINGGRAE_EXPORT_CHANNEL_REORDER | 005180 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 61900.0 | None | None | 91.28 | None | stage2_actionable_best_entry |
| C18_R5L89_101530_HAITAI_SNACK_LATE_THEME | 101530 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| C18_R5L89_248170_SEMPIO_SAUCE_EXPORT_THEME | 248170 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| C18_R5L90_051900_2024_04_30 | 051900 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 420000.0 | None | None | 14.3 | None | stage2_captured_most_upside |
| C18_R5L90_090430_2024_04_30 | 090430 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 169500.0 | None | None | 18.3 | None | stage2_captured_most_upside |
| C18_R5L90_257720_2024_05_09 | 257720 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 20200.0 | None | None | 168.3 | None | stage2_actionable_best_entry |
| C18_R5L92_002790_2024_05_14 | 002790 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| C18_R5L92_018290_2024_05_14 | 018290 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 25500.0 | None | None | 56.9 | None | stage2_captured_most_upside |
| C18_R5L92_352480_2024_05_21 | 352480 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 91100.0 | None | None | 54.8 | None | stage2_actionable_best_entry |
| C18_R5L95_007980_2024_02_01 | 007980 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| C18_R5L95_081660_2024_07_24 | 081660 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 40750.0 | None | None | 10.3 | None | stage2_captured_most_upside |
| C18_R5L95_111770_2024_07_24 | 111770 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 39150.0 | None | None | 14.8 | None | stage2_captured_most_upside |
| C18_R5L98_004370_2024_02_01 | 004370 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 375000.0 | None | None | 59.7 | None | stage2_captured_most_upside |
| C18_R5L98_005180_2024_02_01 | 005180 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 52700.0 | None | None | 124.7 | None | stage2_captured_most_upside |
| C18_R5L98_290720_2024_02_01 | 290720 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| R5L89_C18_ABLECNC_2024_BEAUTY_EXPORT_THEME_FALSE_STAGE2 | 078520 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 9630.0 | None | None | 4.78 | None | stage2_actionable_best_entry |
| R5L89_C18_HANKOOKCOS_2024_KBEAUTY_THEME_EVENT_CAP_4B | 123690 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | 8930.0 | None | None | 4b_good_peak_capture |
| R5L89_C18_VT_2024_KBEAUTY_EXPORT_REORDER_POSITIVE | 018290 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 16750.0 | None | None | 138.81 | None | stage2_actionable_best_entry |
| R5L92_C18_NONGSHIM_2024_RAMEN_EXPORT_CHANNEL_REORDER_POSITIVE | 004370 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 371500.0 | None | None | 61.24 | None | stage2_actionable_best_entry |
| R5L92_C18_OTTOGI_2024_DOMESTIC_FOOD_CHANNEL_FALSE_STAGE2 | 007310 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 485500.0 | None | None | 5.66 | None | stage2_actionable_best_entry |
| R5L92_C18_SPCSAMLIP_2024_BAKERY_CHANNEL_EVENT_CAP_4B | 005610 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | 65500.0 | None | None | 4b_good_peak_capture |
| R5L94_C18_CJSEAFOOD_2024_SEAFOOD_KFOOD_EXPORT_EVENT_CAP_4B | 011150 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | 2905.0 | None | None | 4b_good_peak_capture |
| R5L94_C18_HAITAI_2024_SNACK_RETAIL_EXPORT_THEME_FALSE_STAGE2 | 101530 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 5450.0 | None | None | 2.94 | None | stage2_actionable_best_entry |
| R5L94_C18_SAMYANGFOODS_2024_KFOOD_EXPORT_REORDER_CHANNEL_MARGIN_POSITIVE | 003230 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 180900.0 | None | None | 296.9 | None | stage2_actionable_best_entry |
| R5L96_C18_BINGGRAE_2024_DAIRY_EXPORT_CHANNEL_REORDER_MARGIN_POSITIVE | 005180 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 61900.0 | None | None | 91.28 | None | stage2_actionable_best_entry |
| R5L96_C18_COSMAXNBT_2024_HEALTH_FUNCTIONAL_EXPORT_FALSE_STAGE2 | 222040 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 7230.0 | None | None | 0.28 | None | stage2_actionable_best_entry |
| R5L96_C18_WOOYANG_2024_HMR_KFOOD_EXPORT_EVENT_CAP_4B | 103840 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | 11220.0 | None | None | 4b_good_peak_capture |

# C18_CONSUMER_EXPORT_CHANNEL_REORDER Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `26`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C18_001680_20240806_jongga_kimchi_us_retail_reorder | 001680 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 23150.0 | None | None | 12.743 | None | stage2_actionable_best_entry |
| C18_007310_20240221_us_ramen_hmr_local_production | 007310 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 405500.0 | None | None | 26.5105 | None | stage2_actionable_best_entry |
| C18_017810_20250124_us_tofu_noodle_sales_growth | 017810 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| C18_267980_20240829_alibaba_health_formula_supply | 267980 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 39350.0 | None | None | 3.4307 | None | stage2_captured_most_upside |
| C18_271560_20230908_vietnam_dividend_capacity_recycle | 271560 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 123000.0 | None | None | 6.5041 | None | stage2_actionable_best_entry |
| C18_280360_20250415_pepero_india_export_record | 280360 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 119400.0 | None | None | 9.129 | None | stage2_actionable_best_entry |
| C18_L177_01_241590_2024-03-20 | 241590 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 7450.0 | None | None | 36.38 | None | stage2_actionable_best_entry |
| C18_L177_02_241590_2024-10-08 | 241590 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 8640.0 | None | None | 38.89 | None | stage2_actionable_best_entry |
| C18_L177_03_111770_2024-10-15 | 111770 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 43650.0 | None | None | 50.74 | None | stage2_captured_most_upside |
| C18_L177_04_111770_2025-03-04 | 111770 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 46850.0 | None | None | 102.77 | None | stage2_actionable_best_entry |
| C18_L177_05_007980_2024-08-14 | 007980 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 1470.0 | None | None | 5.37 | None | stage2_actionable_best_entry |
| C18_L177_06_105630_2025-02-25 | 105630 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 12460.0 | None | None | 5.22 | None | stage2_actionable_best_entry |
| C18_L177_07_111110_2025-04-21 | 111110 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 8120.0 | None | None | 13.18 | None | stage2_captured_most_upside |
| C18_L209_01_003230_2024-05-17 | 003230 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 446500.0 | None | None | 97.54 | None | stage2_actionable_best_entry |
| C18_L209_02_003230_2024-06-14 | 003230 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| C18_L209_03_004370_2024-05-28 | 004370 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 469000.0 | None | None | 27.72 | None | stage2_actionable_best_entry |
| C18_L209_04_004370_2025-02-12 | 004370 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | 349000.0 | None | None | no_valid_stage_transition |
| C18_L209_05_097950_2024-08-13 | 097950 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 370000.0 | None | None | 2.7 | None | stage2_actionable_best_entry |
| C18_L209_06_001680_2024-10-11 | 001680 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 20250.0 | None | None | 28.89 | None | stage2_captured_most_upside |
| C18_L209_07_017810_2024-08-16 | 017810 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 12630.0 | None | None | 52.97 | None | stage2_captured_most_upside |
| C18_L209_08_005300_2025-02-10 | 005300 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | 102700.0 | None | None | no_valid_stage_transition |
| C18_L209_09_267980_2024-08-29 | 267980 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 39350.0 | None | None | 3.43 | None | stage2_actionable_best_entry |
| C18_R5L121_005180_BINGGRAE_EXPORT_CHANNEL_20240719 | 005180 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 84000.0 | None | None | 19.52 | None | stage2_actionable_best_entry |
| C18_R5L121_105630_HANSAE_APPAREL_REORDER_20240229 | 105630 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 20400.0 | None | None | 24.26 | None | stage2_actionable_best_entry |
| C18_R5L121_271560_ORION_OVERSEAS_SUBSIDIARY_20241024 | 271560 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| C18_R5L121_280360_LOTTEWELLFOOD_PEPERO_EXPORT_20241024 | 280360 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 131100.0 | None | 131100.0 | 0.92 | 0.0 | stage2_captured_most_upside |

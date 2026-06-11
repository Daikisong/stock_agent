# C18_CONSUMER_EXPORT_CHANNEL_REORDER Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `66`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 003230 | 003230 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 446500.0 | None | 686000.0 | 110.5321 | 48.5284 | stage2_actionable_best_entry |
| 003960 | 003960 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | 47680.0 | None | None | no_valid_stage_transition |
| 004370 | 004370 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 469000.0 | None | 469000.0 | 27.72 | 0.0 | stage2_actionable_best_entry |
| 005180 | 005180 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 88300.0 | None | None | 34.09 | None | stage2_actionable_best_entry |
| 005390 | 005390 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 1957.0 | None | None | 45.12 | None | stage2_actionable_best_entry |
| 005610 | 005610 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 60300.0 | None | None | 13.4 | None | stage2_captured_most_upside |
| 006040 | 006040 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 33000.0 | None | None | 21.3 | None | stage2_actionable_best_entry |
| 007310 | 007310 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| 007980 | 007980 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 2015.0 | None | None | 4.96 | None | stage2_actionable_best_entry |
| 014710 | 014710 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | 4800.0 | None | None | no_valid_stage_transition |
| 020000 | 020000 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 21550.0 | None | None | 0.46 | None | stage2_captured_most_upside |
| 031430 | 031430 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| 036620 | 036620 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 3025.0 | None | None | 39.67 | None | stage2_actionable_best_entry |
| 049770 | 049770 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 34500.0 | None | None | 27.6 | None | stage2_actionable_best_entry |
| 069960 | 069960 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 51200.0 | None | None | 20.9 | None | stage2_actionable_best_entry |
| 081660 | 081660 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 38550.0 | None | 41900.0 | 16.6 | 52.3495 | stage2_actionable_best_entry |
| 090430 | 090430 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| 093050 | 093050 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 15620.0 | None | None | 6.98 | None | stage2_actionable_best_entry |
| 097950 | 097950 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| 105630 | 105630 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 21450.0 | None | None | 3.73 | None | stage2_actionable_best_entry |
| 111770 | 111770 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 44400.0 | None | None | 18.6927 | None | stage2_captured_most_upside |
| 136480 | 136480 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| 139480 | 139480 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| 145990 | 145990 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 42000.0 | None | None | 35.0619 | None | stage2_actionable_best_entry |
| 161890 | 161890 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 55200.0 | None | None | 35.87 | None | stage2_actionable_best_entry |
| 192820 | 192820 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 157700.0 | None | 157700.0 | 31.9 | 0.0 | stage2_actionable_best_entry |
| 248170 | 248170 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | 32950.0 | None | None | no_valid_stage_transition |
| 264900 | 264900 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| 278470 | 278470 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 60100.0 | None | 60100.0 | 365.06 | 0.0 | stage2_actionable_best_entry |
| 383220 | 383220 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | 74000.0 | None | None | no_valid_stage_transition |
| C18_R5L113_004370_20240528 | 004370 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 469000.0 | None | None | 27.72 | None | stage2_actionable_best_entry |
| C18_R5L113_005180_20240517 | 005180 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 88300.0 | None | 109000.0 | 34.09 | 68.7674 | stage2_actionable_best_entry |
| C18_R5L113_271560_20240116 | 271560 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 96600.0 | None | None | 10.46 | None | stage2_captured_most_upside |
| C18_R5_L141_003230_EXPORT_ASP_CAPACITY | 003230 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 686000.0 | None | None | 37.03 | None | stage2_actionable_best_entry |
| C18_R5_L141_004370_SHIN_CHANNEL_REORDER | 004370 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 469000.0 | None | None | 27.72 | None | stage2_actionable_best_entry |
| C18_R5_L141_097950_BIBIGO_CAPACITY_PROXY | 097950 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 272000.0 | None | None | 2.39 | None | stage2_captured_most_upside |
| C18_R5_L142_005180_MELONA_BANANA_MILK_EXPORT_THEME | 005180 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 88300.0 | None | None | 34.09 | None | stage2_actionable_best_entry |
| C18_R5_L142_271560_ORION_OVERSEAS_STABLE_REORDER | 271560 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 99600.0 | None | None | 23.99 | None | stage2_captured_most_upside |
| C18_R5_L142_280360_PEPERO_GLOBAL_CHANNEL_SPIKE | 280360 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 142000.0 | None | None | 46.83 | None | stage2_actionable_best_entry |
| C18_STATIC_TO50_R5L123_01_003230 | 003230 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| C18_STATIC_TO50_R5L123_02_271560 | 271560 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 91000.0 | None | None | 31.0 | None | stage2_actionable_best_entry |
| C18_STATIC_TO50_R5L123_03_097950 | 097950 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 355000.0 | None | None | 13.0 | None | stage2_captured_most_upside |
| C18_STATIC_TO50_R5L123_04_007310 | 007310 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 430000.0 | None | None | 9.0 | None | stage2_captured_most_upside |
| C18_STATIC_TO50_R5L123_05_049770 | 049770 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 35000.0 | None | None | 22.0 | None | stage2_actionable_best_entry |
| C18_STATIC_TO50_R5L123_06_005180 | 005180 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | 62000.0 | None | None | None | green_good_but_late |
| C18_STATIC_TO50_R5L123_07_280360 | 280360 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 145000.0 | None | None | 18.0 | None | stage2_actionable_best_entry |
| C18_STATIC_TO50_R5L123_08_003920 | 003920 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | 650000.0 | None | None | no_valid_stage_transition |
| C18_STATIC_TO50_R5L123_09_005610 | 005610 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 62000.0 | None | None | 5.0 | None | stage2_captured_most_upside |
| C18_STATIC_TO50_R5L123_10_011150 | 011150 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | 4050.0 | None | None | no_valid_stage_transition |
| C18_STATIC_TO50_R5L123_11_383220 | 383220 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 64500.0 | None | None | 27.0 | None | stage2_actionable_best_entry |
| C18_STATIC_TO50_R5L123_12_093050 | 093050 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 17500.0 | None | None | 4.0 | None | stage2_captured_most_upside |
| C18_STATIC_TO50_R5L123_13_020000 | 020000 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 17500.0 | None | None | 3.5 | None | stage2_captured_most_upside |
| C18_STATIC_TO50_R5L123_14_111770 | 111770 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| C18_STATIC_TO50_R5L123_15_105630 | 105630 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 24500.0 | None | None | 21.0 | None | stage2_actionable_best_entry |
| C18_STATIC_TO50_R5L123_16_005390 | 005390 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | 2300.0 | None | None | no_valid_stage_transition |
| C18_STATIC_TO50_R5L123_17_081660 | 081660 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 41500.0 | None | None | 24.0 | None | stage2_actionable_best_entry |
| C18_STATIC_TO50_R5L123_18_031430 | 031430 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 15500.0 | None | None | 4.0 | None | stage2_captured_most_upside |
| C18_STATIC_TO50_R5L123_19_214420 | 214420 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | 9200.0 | None | None | no_valid_stage_transition |
| C18_STATIC_TO50_R5L123_20_018250 | 018250 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 19000.0 | None | None | 10.0 | None | stage2_captured_most_upside |
| C18_STATIC_TO50_R5L123_21_192820 | 192820 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| C18_STATIC_TO50_R5L123_22_161890 | 161890 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 57000.0 | None | None | 32.0 | None | stage2_actionable_best_entry |
| C18_STATIC_TO50_R5L123_23_406820 | 406820 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | 17300.0 | None | None | no_valid_stage_transition |
| C18_STATIC_TO50_R5L123_24_298540 | 298540 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 12800.0 | None | None | 6.0 | None | stage2_captured_most_upside |
| C18_STATIC_TO50_R5L123_25_036620 | 036620 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | 3900.0 | None | None | no_valid_stage_transition |
| C18_STATIC_TO50_R5L123_26_248170 | 248170 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 30500.0 | None | None | 42.0 | None | stage2_actionable_best_entry |
| C18_STATIC_TO50_R5L123_27_007540 | 007540 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 42000.0 | None | None | 8.0 | None | stage2_captured_most_upside |

# C18_CONSUMER_EXPORT_CHANNEL_REORDER Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `35`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 001680 | 001680 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 21200.0 | None | None | 45.7555 | None | stage2_actionable_best_entry |
| 003960 | 003960 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 43850.0 | None | None | 150.63 | None | stage2_actionable_best_entry |
| 011150 | 011150 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| 014710 | 014710 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 4150.0 | None | None | 115.66 | None | stage2_actionable_best_entry |
| 049770 | 049770 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 38300.0 | None | None | 27.68 | None | stage2_actionable_best_entry |
| 271560 | 271560 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 92100.0 | None | None | 15.8547 | None | stage2_actionable_best_entry |
| 280360 | 280360 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 128800.0 | None | None | 61.884 | None | stage2_actionable_best_entry |
| C18_CEX_081660_20230214 | 081660 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 39750.0 | None | None | 2.89 | None | stage2_actionable_best_entry |
| C18_CEX_081660_20230214 | None | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 39750.0 | None | None | 2.89 | None | stage2_actionable_best_entry |
| C18_CEX_383220_20230118 | 383220 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 141000.0 | None | None | 10.28 | None | stage2_actionable_best_entry |
| C18_CEX_383220_20230118 | None | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 141000.0 | None | None | 10.28 | None | stage2_actionable_best_entry |
| C18_POS_003230_20240517 | 003230 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 446500.0 | None | None | 97.54 | None | stage2_actionable_best_entry |
| C18_POS_003230_20240517 | None | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 446500.0 | None | None | 97.54 | None | stage2_actionable_best_entry |
| C18_POS_005180_20240517 | 005180 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 88300.0 | None | None | 34.09 | None | stage2_actionable_best_entry |
| C18_POS_005180_20240517 | None | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 88300.0 | None | None | 34.09 | None | stage2_actionable_best_entry |
| R5L72_C18_001680_20240422_FOOD_EXPORT_CHANNEL_MARGIN_BRIDGE | 001680 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 21900.0 | None | None | 41.1 | None | stage2_actionable_best_entry |
| R5L72_C18_248170_20240618_FOOD_THEME_WITHOUT_REORDER_BRIDGE | 248170 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 40350.0 | None | None | 12.76 | None | stage2_actionable_best_entry |
| R5L72_C18_280360_20240422_KFOOD_EXPORT_CHANNEL_REORDER_BRIDGE | 280360 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 132100.0 | None | None | 57.83 | None | stage2_actionable_best_entry |
| R5L74_C18_011150_20240517_SEAWEED_PROXY_FALSE_PROMOTION | 011150 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| R5L74_C18_017810_20240517_US_TOFU_EXPORT_TURNAROUND | 017810 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 13760.0 | None | None | 33.79 | None | stage2_actionable_best_entry |
| R5L74_C18_103840_20240517_FROZEN_KIMBAP_THEME_BLOWOFF | 103840 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| R5L74_C18_271560_20240517_GLOBAL_STAPLE_REORDER_MISSED | 271560 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 91900.0 | None | None | 20.13 | None | stage2_actionable_best_entry |
| R5L75_C18_003960_20240201_KFOOD_EXPORT_REORDER_MARGIN_BRIDGE | 003960 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 37000.0 | None | None | 197.03 | None | stage2_actionable_best_entry |
| R5L75_C18_017810_20240401_HEALTH_FOOD_GLOBAL_CHANNEL_MARGIN_BRIDGE | 017810 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 11100.0 | None | None | 55.41 | None | stage2_actionable_best_entry |
| R5L75_C18_049770_20240401_LEGACY_FOOD_CHANNEL_THEME_NO_REORDER_MARGIN_BRIDGE | 049770 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 33850.0 | None | None | 36.04 | None | stage2_actionable_best_entry |
| R5L76_C18_001680_20240517_KFOOD_THEME_WITHOUT_DURABLE_REORDER_BRIDGE | 001680 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| R5L76_C18_004370_20240517_RAMEN_EXPORT_REORDER_HIGH_MAE_SUCCESS | 004370 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 399000.0 | None | None | 50.13 | None | stage2_actionable_best_entry |
| R5L76_C18_049770_20240517_STAPLE_FOOD_DISTRIBUTION_BETA_FADE | 049770 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| R5L76_C18_280360_20240517_CONFECTIONERY_EXPORT_MARGIN_HIGH_MAE_SUCCESS | 280360 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 142000.0 | None | None | 46.83 | None | stage2_actionable_best_entry |
| R5L84-C18-01 | 241710 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 38200.0 | None | None | 157.85 | None | stage2_actionable_best_entry |
| R5L84-C18-02 | 950140 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 15480.0 | None | None | 61.5 | None | stage2_actionable_best_entry |
| R5L84-C18-03 | 214420 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |
| R5L87-C18-01 | 214420 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 5960.0 | None | None | 128.19 | None | stage2_actionable_best_entry |
| R5L87-C18-02 | 950140 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 13790.0 | None | None | 81.29 | None | stage2_actionable_best_entry |
| R5L87-C18-03 | 007310 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | None | None | None | None | None | no_valid_stage_transition |

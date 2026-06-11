# C22_INSURANCE_RATE_CYCLE_RESERVE Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `50`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 003690 | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| 005830 | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | 95000.0 | None | None | 30.53 | None | stage2_actionable_best_entry |
| 032830 | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | 92200.0 | None | 94700.0 | 20.3881 | 13.2994 | stage2_actionable_best_entry |
| 088350 | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| 138040 | 138040 | C22_INSURANCE_RATE_CYCLE_RESERVE | 88800.0 | None | None | 43.47 | None | stage2_actionable_best_entry |
| 211050 | 211050 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | 4925.0 | None | None | no_valid_stage_transition |
| 244920 | 244920 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| C22-DB-005830-20240201 | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | 91900.0 | None | None | 34.9 | None | stage2_actionable_best_entry |
| C22-HGI-000370-20240201 | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | 5120.0 | None | None | 21.7 | None | stage2_captured_most_upside |
| C22-HL-088350-20240201 | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | 3355.0 | None | None | 13.7 | None | stage2_captured_most_upside |
| C22-SL-032830-20240201 | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | 76000.0 | None | None | 42.8 | None | stage2_actionable_best_entry |
| C22_000810_2024_04_26_stage3_yellow_csm_capital_return_positive | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| C22_001450_2024_05_14_stage2_reserve_quality_false_positive | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | 34200.0 | None | None | 7.16 | None | stage2_captured_most_upside |
| C22_005830_2024_04_26_stage2_actionable_rate_cycle_mixed_positive | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | 99900.0 | None | None | 24.12 | None | stage2_actionable_best_entry |
| C22_032830_2024-07-26_Stage2-Actionable_life_insurance_valueup_csm_capital_bridge | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | 94700.0 | None | None | 17.21 | None | stage2_actionable_best_entry |
| C22_032830_2024_02_23_stage3_yellow_life_insurance_drawdown_recovery | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| C22_088350_2024-07-11_Stage2-FalsePositive_life_insurance_valueup_label_without_reserve_capital_return_bridge | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | 3150.0 | None | None | 2.86 | None | stage2_captured_most_upside |
| C22_138040_2024-08-16_Stage2-Actionable_insurance_holding_capital_return_bridge | 138040 | C22_INSURANCE_RATE_CYCLE_RESERVE | 88800.0 | None | None | 43.47 | None | stage2_actionable_best_entry |
| C22_R6L105_000370_20240502_STAGE4B | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | 5350.0 | None | None | no_valid_stage_transition |
| C22_R6L105_000810_20240201_STAGE3GREEN | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | 267500.0 | None | None | None | green_good_but_late |
| C22_R6L105_001450_20240712_STAGE2ACTIONABLE | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | 32550.0 | None | None | 6.1 | None | stage2_actionable_best_entry |
| C22_R6L105_003690_20240201_STAGE2ACTIONABLE | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | 7830.0 | None | None | 12.0 | None | stage2_actionable_best_entry |
| C22_R6L105_005830_20240617_STAGE3GREEN | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | 105200.0 | None | None | None | green_good_but_late |
| C22_R6L105_088350_20240223_STAGE3YELLOW | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| C22_R6L106_000370_20240201_STAGE3YELLOW_SMALL_NONLIFE | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| C22_R6L106_000810_20240426_STAGE4B_GREEN_SPLIT | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | 311500.0 | None | None | no_valid_stage_transition |
| C22_R6L106_001450_20240514_STAGE3YELLOW_REJECT | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| C22_R6L106_003690_20240201_STAGE3YELLOW_REINSURANCE_CAP | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| C22_R6L106_005830_20240426_STAGE4B_LOCAL_CAP | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | 99900.0 | None | None | no_valid_stage_transition |
| C22_R6L106_032830_20240201_STAGE3GREEN_CAP | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | 76000.0 | None | None | None | green_good_but_late |
| C22_R6L107_001_000810_20240628_STAGE3YELLOW | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| C22_R6L107_002_005830_20240822_STAGE3YELLOW | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| C22_R6L107_003_032830_20240229_STAGE4BWATCH | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | 100000.0 | None | None | no_valid_stage_transition |
| C22_R6L107_004_088350_20240229_STAGE2ACTIONABLE | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | 3570.0 | None | None | 8.0 | None | stage2_actionable_best_entry |
| C22_R6L107_005_000370_20240229_STAGE4BWATCH | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | 6070.0 | None | None | no_valid_stage_transition |
| C22_R6L107_006_001450_20240820_STAGE3YELLOW | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| C22_R6L107_007_003690_20240426_STAGE2 | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | 8240.0 | None | None | 10.2 | None | stage2_captured_most_upside |
| C22_R6L107_008_085620_20240201_STAGE2 | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | 5230.0 | None | None | 15.5 | None | stage2_captured_most_upside |
| C22_R6L107_009_000540_20240201_STAGE2 | 000540 | C22_INSURANCE_RATE_CYCLE_RESERVE | 3850.0 | None | None | 21.0 | None | stage2_captured_most_upside |
| C22_R6L107_010_138040_20240201_STAGE3GREEN | 138040 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | 62000.0 | None | None | None | green_good_but_late |
| C22_R6L107_011_175330_20240201_STAGE2ACTIONABLE | 175330 | C22_INSURANCE_RATE_CYCLE_RESERVE | 12100.0 | None | None | 20.0 | None | stage2_actionable_best_entry |
| C22_R6L107_012_039490_20240201_STAGE2 | 039490 | C22_INSURANCE_RATE_CYCLE_RESERVE | 101000.0 | None | None | 22.0 | None | stage2_captured_most_upside |
| C22_R6L107_013_071050_20240201_STAGE2 | 071050 | C22_INSURANCE_RATE_CYCLE_RESERVE | 61000.0 | None | None | 16.0 | None | stage2_captured_most_upside |
| C22_R6L107_014_016360_20240201_STAGE2 | 016360 | C22_INSURANCE_RATE_CYCLE_RESERVE | 38100.0 | None | None | 17.5 | None | stage2_captured_most_upside |
| C22_R6L107_015_001500_20240201_STAGE2 | 001500 | C22_INSURANCE_RATE_CYCLE_RESERVE | 8500.0 | None | None | 11.5 | None | stage2_captured_most_upside |
| C22_R6L107_016_001450_20240201_STAGE2ACTIONABLE | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | 33150.0 | None | None | 11.8 | None | stage2_actionable_best_entry |
| C22_R6L107_017_000810_20240426_STAGE4BWATCH | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | 311500.0 | None | None | no_valid_stage_transition |
| C22_R6L107_018_005830_20240426_STAGE4BWATCH | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | 99900.0 | None | None | no_valid_stage_transition |
| C22_R6L107_019_088350_20240426_STAGE3YELLOW | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| C22_R6L107_020_003690_20240822_STAGE3YELLOW | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |

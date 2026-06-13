# C22_INSURANCE_RATE_CYCLE_RESERVE Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `23`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C22_000370_20241112_HANWHA_GENERAL_PROFIT_UP_EXPERIENCE_VARIANCE | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | 4550.0 | None | None | 79.1209 | None | stage2_actionable_best_entry |
| C22_000810_20240514_SAMSUNG_FIRE_KICS_CAPITAL_BUFFER | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| C22_001450_20241015_HYUNDAI_MARINE_FVPL_INVESTMENT_LOSS_GUARD | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | 31900.0 | None | None | no_valid_stage_transition |
| C22_003690_20240701_KOREAN_RE_REINSURANCE_HARD_MARKET | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| C22_005830_20240516_DB_INSURANCE_CAPITAL_RETURN_LOW_MFE_HIGH_MAE | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | 111500.0 | None | None | 11.2108 | None | stage2_actionable_best_entry |
| C22_088350_20241113_HANWHA_LIFE_CSM_APE_DELAYED_UNLOCK | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | 2750.0 | None | None | 58.3636 | None | stage2_actionable_best_entry |
| C22_R6_L162_000810_20250212 | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | 358500.0 | None | None | 46.72 | None | stage2_actionable_best_entry |
| C22_R6_L162_001450_20240319 | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| C22_R6_L162_003690_20240516 | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| C22_R6_L162_005830_20240516 | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| C22_R6_L162_032830_20240516 | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | 88900.0 | None | None | 24.86 | None | stage2_actionable_best_entry |
| C22_R6_L162_032830_20241115 | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| C22_R6_L162_088350_20240515 | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| C22_R6_L162_138040_20241114 | 138040 | C22_INSURANCE_RATE_CYCLE_RESERVE | 101800.0 | None | None | 25.15 | None | stage2_actionable_best_entry |
| C22_R6_L188_000370_20240423 | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | 4795.0 | None | None | 29.93 | None | stage2_actionable_best_entry |
| C22_R6_L188_000370_20250224 | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | 4100.0 | None | None | 98.78 | None | stage2_actionable_best_entry |
| C22_R6_L188_000400_20240516 | 000400 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| C22_R6_L188_000400_20250523 | 000400 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| C22_R6_L188_000540_20240516 | 000540 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| C22_R6_L188_000540_20250307 | 000540 | C22_INSURANCE_RATE_CYCLE_RESERVE | 3310.0 | None | None | 83.38 | None | stage2_actionable_best_entry |
| C22_R6_L188_082640_20241113 | 082640 | C22_INSURANCE_RATE_CYCLE_RESERVE | 5570.0 | None | None | 59.61 | None | stage2_actionable_best_entry |
| C22_R6_L188_082640_20250519 | 082640 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| C22_R6_L188_085620_20240523 | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |

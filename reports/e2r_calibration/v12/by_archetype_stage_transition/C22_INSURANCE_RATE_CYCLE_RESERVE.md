# C22_INSURANCE_RATE_CYCLE_RESERVE Stage Transition Report

v12 stage transition은 shadow-only 진단입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, default scoring did not change.

- stage_transition_summary_rows: `25`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 000810 | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | 308500.0 | None | None | 41.0025 | None | stage2_actionable_best_entry |
| 001450 | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | 34650.0 | None | None | 6.06 | None | stage2_actionable_best_entry |
| 005830 | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | 97800.0 | None | None | 26.79 | None | stage2_actionable_best_entry |
| 088350 | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | 3385.0 | None | None | 3.84 | None | stage2_actionable_best_entry |
| R13L17_C22_000810_SFM_RATE_RESERVE_2023Q1 | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | 227500.0 | None | None | 20.66 | None | stage2_actionable_best_entry |
| R13L17_C22_001450_HYUNDAI_RESERVE_GAP_2023Q1 | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | 34750.0 | None | None | 4.46 | None | stage2_actionable_best_entry |
| R13L17_C22_005830_DBI_RATE_RESERVE_2023Q1 | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | 76200.0 | None | None | 24.02 | None | stage2_actionable_best_entry |
| R13L17_C22_032830_SAMSUNG_LIFE_BLOWOFF_2024 | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | 105100.0 | None | None | 4b_good_peak_capture |
| R13L17_C22_088350_HANWHA_LIFE_EVENT_PREMIUM_2024 | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | 3355.0 | None | None | 13.71 | None | stage2_actionable_best_entry |
| R13L20_C22_000810 | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | 308500.0 | None | None | 41.0025 | None | stage2_actionable_best_entry |
| R13L20_C22_001450 | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | 34650.0 | None | None | 6.06 | None | stage2_actionable_best_entry |
| R13L20_C22_005830 | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | 97800.0 | None | None | 26.79 | None | stage2_actionable_best_entry |
| R13L20_C22_088350 | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | 3385.0 | None | None | 3.84 | None | stage2_actionable_best_entry |
| R13L21_C22_000810_2025_PNC_RESERVE_CAPITAL_RETURN | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | 392000.0 | 404500.0 | None | 60.7165 | None | green_good_but_late |
| R13L21_C22_001450_2025_RESERVE_QUALITY_GUARD | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | 24400.0 | None | None | 25.82 | None | stage2_actionable_best_entry |
| R13L21_C22_005830_2025_Q1_RESERVE_CAPITAL_RETURN | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | 97300.0 | None | None | 52.42 | None | stage2_actionable_best_entry |
| R13L21_C22_088350_2025_LIFE_RATE_BETA_WHIPSaw | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | 2700.0 | None | None | 61.3 | None | stage2_actionable_best_entry |
| R6L11_C22_000400 | 000400 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| R6L11_C22_000810 | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | 304000.0 | 370000.0 | None | 43.0951 | None | green_too_late |
| R6L11_C22_001450 | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| R6L11_C22_005830 | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | 100000.0 | 111500.0 | None | 20.7 | None | green_good_but_late |
| R6L13_C22_DBI_20240222_IFRS17_CAPITAL_RETURN | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | 97800.0 | None | None | 26.79 | None | stage2_actionable_best_entry |
| R6L13_C22_HANWHALIFE_20240222_POLICY_BETA_RESERVE_GAP | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| R6L13_C22_HYUNDAIMARINE_20240222_POLICY_BETA_RESERVE_GAP | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| R6L13_C22_SFMI_20240222_IFRS17_CAPITAL_RETURN | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | 308500.0 | None | None | 27.55 | None | stage2_actionable_best_entry |

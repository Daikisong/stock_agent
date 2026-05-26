# C22_INSURANCE_RATE_CYCLE_RESERVE Stage Transition Report

- stage_transition_summary_rows: `6`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 000810 | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | 308500.0 | 370000.0 | 389000.0 | 41.0109 | 63.627 | 4b_too_early |
| 005830 | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | 97800.0 | 111500.0 | 120600.0 | 26.7903 | 87.0198 | 4b_good_peak_capture |
| 088350 | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | 3385.0 | None | None | 3.84 | None | 4c_too_late |
| R6L41_C22_000810_SFM_CAPITAL_RETURN_IFRS17 | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | 308500.0 | 370000.0 | 389000.0 | 41.0109 | 63.627 | green_too_late |
| R6L41_C22_005830_DBI_CAPITAL_RETURN_ROE | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | 97800.0 | 111500.0 | 120600.0 | 26.7903 | 87.0198 | 4b_good_peak_capture |
| R6L41_C22_088350_HWL_POLICY_ONLY_FALSE_POSITIVE | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | 3385.0 | None | None | 3.84 | None | 4c_too_late |

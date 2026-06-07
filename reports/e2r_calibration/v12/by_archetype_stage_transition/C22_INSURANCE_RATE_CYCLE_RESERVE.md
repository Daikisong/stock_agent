# C22_INSURANCE_RATE_CYCLE_RESERVE Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `6`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C22_R6L92_001450_HYUNDAI_MARINE_PC_RESERVE | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | 31700.0 | None | None | 16.09 | None | stage2_actionable_best_entry |
| C22_R6L92_085620_MIRAE_LIFE_PRICE_SPIKE | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| C22_R6L92_138930_BNK_CROSSLABEL_RATE_PBR | 138930 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| R6L99_C22_HEUNGKUKFIRE_2024_SMALLCAP_INSURANCE_VALUEUP_EVENT_CAP_4B | 000540 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | 5570.0 | None | None | 4b_good_peak_capture |
| R6L99_C22_KOREANRE_2024_REINSURANCE_RATE_RESERVE_FALSE_STAGE2 | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | 8510.0 | None | None | 0.47 | None | stage2_actionable_best_entry |
| R6L99_C22_SAMSUNGFIRE_2024_PNC_RATE_RESERVE_CAPITAL_RETURN_BRIDGE_POSITIVE | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | 247500.0 | None | None | 58.99 | None | stage2_actionable_best_entry |

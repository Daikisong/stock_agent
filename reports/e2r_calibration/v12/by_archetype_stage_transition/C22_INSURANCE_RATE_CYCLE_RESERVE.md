# C22_INSURANCE_RATE_CYCLE_RESERVE Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `27`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 000370 | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | 5000.0 | None | 5370.0 | 24.5962 | 30.086 | stage2_actionable_best_entry |
| 003690 | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | 7410.0 | None | None | 20.9201 | None | stage2_actionable_best_entry |
| 082640 | 082640 | C22_INSURANCE_RATE_CYCLE_RESERVE | 4630.0 | None | None | 103.8884 | None | stage2_actionable_best_entry |
| 085620 | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| R6L72_C22_000370_20240129_SMALL_PNC_ROE_VALUEUP_BRIDGE | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | 4050.0 | None | None | 53.83 | None | stage2_actionable_best_entry |
| R6L72_C22_000540_20240213_SMALL_INSURER_PRICE_VALUEUP_BLOWOFF | 000540 | C22_INSURANCE_RATE_CYCLE_RESERVE | 5280.0 | None | None | 25.0 | None | stage2_actionable_best_entry |
| R6L72_C22_003690_20240124_REINSURANCE_RATE_CYCLE_STABLE_BRIDGE | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | 7160.0 | None | None | 19.41 | None | stage2_actionable_best_entry |
| R6L74_C22_000370_20240129_PNC_INSURANCE_RATE_CYCLE_CAPITAL_RETURN_BRIDGE | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | 4050.0 | None | None | 53.83 | None | stage2_actionable_best_entry |
| R6L74_C22_000540_20240214_SMALL_INSURANCE_THEME_NO_RESERVE_CAPITAL_BRIDGE | 000540 | C22_INSURANCE_RATE_CYCLE_RESERVE | 5570.0 | None | None | 18.49 | None | stage2_actionable_best_entry |
| R6L74_C22_000810_SAMSUNG_FIRE_20240223 | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | 308500.0 | 370000.0 | 389000.0 | 27.5567 | 94.6921 | green_too_late |
| R6L74_C22_001450_HYUNDAI_MARINE_20240223 | 001450 | C22_INSURANCE_RATE_CYCLE_RESERVE | 34650.0 | None | None | 6.06 | None | stage2_actionable_best_entry |
| R6L74_C22_005830_DB_INSURANCE_20240223 | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | 97800.0 | 111500.0 | 120600.0 | 26.7903 | 87.0198 | green_too_late |
| R6L74_C22_082640_20240129_LIFE_INSURANCE_RATE_CYCLE_PBR_REPAIR_BRIDGE | 082640 | C22_INSURANCE_RATE_CYCLE_RESERVE | 4630.0 | None | None | 103.89 | None | stage2_actionable_best_entry |
| R6L74_C22_088350_HANWHA_LIFE_20240223 | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | 3385.0 | None | None | 3.84 | None | stage2_actionable_best_entry |
| R6L75_C22_000400_LOTTE_INSURANCE_20240223_SALE_EVENT_RESERVE_RISK_FALSE_POSITIVE | 000400 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| R6L75_C22_003690_KOREAN_RE_20240223_REINSURANCE_RESERVE_STABLE_SUCCESS | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | 8020.0 | None | None | 12.22 | None | stage2_actionable_best_entry |
| R6L75_C22_032830_SAMSUNG_LIFE_20240223_LIFE_IFRS17_VALUEUP_HIGH_MAE_SUCCESS | 032830 | C22_INSURANCE_RATE_CYCLE_RESERVE | 95600.0 | None | None | 16.11 | None | stage2_actionable_best_entry |
| R6L75_C22_082640_TONGYANG_LIFE_20240223_CONTROL_PREMIUM_FALSE_POSITIVE | 082640 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| R6L76_C22_000400_20240213_SMALL_NONLIFE_MNA_THEME_NO_RESERVE_ROE_BRIDGE | 000400 | C22_INSURANCE_RATE_CYCLE_RESERVE | 3370.0 | None | None | 21.36 | None | stage2_actionable_best_entry |
| R6L76_C22_003690_20240129_REINSURANCE_UNDERWRITING_RATE_RESERVE_BRIDGE | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | 7400.0 | None | None | 25.27 | None | stage2_actionable_best_entry |
| R6L76_C22_138040_20240129_INSURANCE_HOLDCO_CAPITAL_RETURN_RESERVE_BUFFER_BRIDGE | 138040 | C22_INSURANCE_RATE_CYCLE_RESERVE | 64300.0 | None | None | 55.37 | None | stage2_actionable_best_entry |
| R6L84-C22-01 | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | 3970.0 | None | None | 56.93 | None | stage2_actionable_best_entry |
| R6L84-C22-02 | 082640 | C22_INSURANCE_RATE_CYCLE_RESERVE | 7000.0 | None | None | 34.86 | None | stage2_actionable_best_entry |
| R6L84-C22-03 | 000540 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| R6L86-C22-01 | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | 7910.0 | None | None | 20.73 | None | stage2_actionable_best_entry |
| R6L86-C22-02 | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |
| R6L86-C22-03 | 000540 | C22_INSURANCE_RATE_CYCLE_RESERVE | None | None | None | None | None | no_valid_stage_transition |

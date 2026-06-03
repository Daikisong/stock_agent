# C24_BIO_TRIAL_DATA_EVENT_RISK Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `28`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 087010 | 087010 | C24_BIO_TRIAL_DATA_EVENT_RISK | 37500.0 | None | None | 252.0 | None | stage2_actionable_best_entry |
| 206650 | 206650 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| 226950 | 226950 | C24_BIO_TRIAL_DATA_EVENT_RISK | 9300.0 | None | None | 252.15 | None | stage2_actionable_best_entry |
| 293780 | 293780 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| 298380 | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | 24550.0 | None | None | 56.82 | None | stage2_actionable_best_entry |
| 323990 | 323990 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | 19400.0 | None | None | no_valid_stage_transition |
| 358570 | 358570 | C24_BIO_TRIAL_DATA_EVENT_RISK | 11740.0 | None | None | 39.18 | None | stage2_actionable_best_entry |
| 397030 | 397030 | C24_BIO_TRIAL_DATA_EVENT_RISK | 15790.0 | None | None | 61.81 | None | stage2_actionable_best_entry |
| R7L71_C24_028300_20240517 | 028300 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | 4c_too_late |
| R7L71_C24_087010_20240627 | 087010 | C24_BIO_TRIAL_DATA_EVENT_RISK | 46500.0 | None | None | 124.73 | None | stage2_actionable_best_entry |
| R7L71_C24_196170_20240222 | 196170 | C24_BIO_TRIAL_DATA_EVENT_RISK | 131200.0 | None | None | 177.06 | None | stage2_actionable_best_entry |
| R7L71_C24_323990_20240325 | 323990 | C24_BIO_TRIAL_DATA_EVENT_RISK | 23350.0 | None | None | 3.85 | None | stage2_actionable_best_entry |
| R7L72_C24_007390_20230331_CELL_THERAPY_APPROVAL_EVENT_HARD_BREAK | 007390 | C24_BIO_TRIAL_DATA_EVENT_RISK | 18000.0 | None | None | 41.67 | None | stage2_actionable_best_entry |
| R7L72_C24_220100_20240423_PROSTATE_RADIOLIGAND_DATA_BRIDGE | 220100 | C24_BIO_TRIAL_DATA_EVENT_RISK | 11240.0 | None | None | 178.02 | None | stage2_actionable_best_entry |
| R7L72_C24_226950_20240227_RNAI_PLATFORM_DATA_FALSE_START | 226950 | C24_BIO_TRIAL_DATA_EVENT_RISK | 16810.0 | None | None | 9.99 | None | stage2_actionable_best_entry |
| R7L75_C24_007390_NATURECELL_JOINTSTEM_REJECTION_4C | 007390 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | 4c_too_late |
| R7L75_C24_141080_20240620_ADC_PLATFORM_DATA_LICENSING_BRIDGE | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | 75500.0 | None | None | 90.2 | None | stage2_actionable_best_entry |
| R7L75_C24_298380_ABL_SANOFI_LICENSEOUT_HIGH_MAE_SUCCESS | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | 26150.0 | None | None | 33.08 | None | stage2_actionable_best_entry |
| R7L75_C24_299660_20240826_VACCINE_TRIAL_EVENT_SPIKE_NO_DURABLE_DATA_BRIDGE | 299660 | C24_BIO_TRIAL_DATA_EVENT_RISK | 7720.0 | None | None | 18.13 | None | stage2_actionable_best_entry |
| R7L75_C24_310210_BORONOI_CLINICAL_OPTIONALITY_SUCCESS | 310210 | C24_BIO_TRIAL_DATA_EVENT_RISK | 49350.0 | None | None | 210.03 | None | stage2_actionable_best_entry |
| R7L75_C24_397030_APRILBIO_EVENT_SPIKE_FAILED_RERATING | 397030 | C24_BIO_TRIAL_DATA_EVENT_RISK | 19470.0 | None | None | 33.02 | None | stage2_actionable_best_entry |
| R7L75_C24_950220_20240129_IMMUNO_ONCOLOGY_TRIAL_OPTIONALITY_NO_DATA_BRIDGE | 950220 | C24_BIO_TRIAL_DATA_EVENT_RISK | 1696.0 | None | None | 16.57 | None | stage2_actionable_best_entry |
| R7L83-C24-01 | 237690 | C24_BIO_TRIAL_DATA_EVENT_RISK | 77600.0 | None | None | 55.67 | None | stage2_actionable_best_entry |
| R7L83-C24-02 | 310210 | C24_BIO_TRIAL_DATA_EVENT_RISK | 53000.0 | None | None | 188.68 | None | stage2_actionable_best_entry |
| R7L83-C24-03 | 235980 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| R7L86-C24-01 | 000250 | C24_BIO_TRIAL_DATA_EVENT_RISK | 86500.0 | None | None | 165.9 | None | stage2_actionable_best_entry |
| R7L86-C24-02 | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | 75500.0 | None | None | 74.17 | None | stage2_actionable_best_entry |
| R7L86-C24-03 | 174900 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |

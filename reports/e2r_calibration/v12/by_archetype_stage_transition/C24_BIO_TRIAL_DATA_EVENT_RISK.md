# C24_BIO_TRIAL_DATA_EVENT_RISK Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `13`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C24_ABL_298380_2024_03_06_BISPECIFIC_DATA_PLATFORM_RERATING | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | 27300.0 | None | None | 41.03 | None | stage2_actionable_best_entry |
| C24_HLB_028300_2024_05_16_FDA_BINARY_EVENT_RISK_4C | 028300 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | 4c_too_late |
| C24_QRI_115180_2024_03_06_CLINICAL_DATA_EVENT_FALSE_POSITIVE | 115180 | C24_BIO_TRIAL_DATA_EVENT_RISK | 4595.0 | None | None | 9.68 | None | stage2_captured_most_upside |
| C24_R7L93_028300_HLB_REGULATORY_CRL_HARD4C | 028300 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24_R7L93_141080_LCG_ADC_PLATFORM_FALSE_OVERBLOCK | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24_R7L93_298380_ABL_BISPECIFIC_ADC_DATA | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | 21250.0 | None | None | 45.88 | None | stage2_actionable_best_entry |
| C24_R7L97_001 | 028300 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24_R7L97_003 | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24_R7L97_004 | 039200 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24_R7L97_005 | 358570 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| R7L98_C24_HLB_2024_FDA_CRL_HARD_4C_TRIAL_EVENT_PROTECTION | 028300 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| R7L98_C24_SILLAJEN_2024_ONCOLYTIC_VIRUS_TRIAL_EVENT_CAP_4B | 215600 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | 3275.0 | None | None | 4b_good_peak_capture |
| R7L98_C24_VORONOI_2024_ONCOLOGY_TARGET_TRIAL_DATA_PARTNERING_BRIDGE_POSITIVE | 310210 | C24_BIO_TRIAL_DATA_EVENT_RISK | 33250.0 | None | None | 257.59 | None | stage2_actionable_best_entry |

# C24_BIO_TRIAL_DATA_EVENT_RISK Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `27`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C24_R7L84_095700_GENEXINE_TRIAL_REBOUND_NO_DATA_BRIDGE | 095700 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24_R7L84_196170_ALTEOGEN_PLATFORM_EVENT_VALIDATION_BRIDGE | 196170 | C24_BIO_TRIAL_DATA_EVENT_RISK | 105000.0 | None | None | 333.81 | None | stage2_actionable_best_entry |
| C24_R7L84_206650_EUBIOLOGICS_VACCINE_THEME_SPIKE_NO_COMMERCIAL_BRIDGE | 206650 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24_R7L87_196170_ALTEOGEN_PLATFORM_EVENT_BRIDGE | 196170 | C24_BIO_TRIAL_DATA_EVENT_RISK | 131200.0 | None | None | 247.18 | None | stage2_actionable_best_entry |
| C24_R7L87_206650_EUBIO_VACCINE_EVENT_NO_DURABLE_BRIDGE | 206650 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24_R7L87_950220_NEOIMMUNETECH_DATA_THEME_DECAY | 950220 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24_R7L90_028300_2024_05_16 | 028300 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24_R7L90_039200_2024_08_21 | 039200 | C24_BIO_TRIAL_DATA_EVENT_RISK | 36900.0 | None | None | 17.1 | None | stage2_captured_most_upside |
| C24_R7L90_196170_2024_11_20 | 196170 | C24_BIO_TRIAL_DATA_EVENT_RISK | 350500.0 | None | None | 31.1 | None | stage2_actionable_best_entry |
| C24_R7L90_237690_STPHARM_RNA_PLATFORM_BRIDGE | 237690 | C24_BIO_TRIAL_DATA_EVENT_RISK | 66300.0 | None | None | 71.19 | None | stage2_actionable_best_entry |
| C24_R7L90_256840_KOREA_BNC_THERAPEUTIC_EVENT_MOMENTUM | 256840 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24_R7L90_365270_CURACLE_VASCULAR_EVENT_SPIKE | 365270 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24_R7L93_196170_2024_02_22 | 196170 | C24_BIO_TRIAL_DATA_EVENT_RISK | 105000.0 | None | None | 282.9 | None | stage2_captured_most_upside |
| C24_R7L93_235980_2024_02_21 | 235980 | C24_BIO_TRIAL_DATA_EVENT_RISK | 11920.0 | None | None | 44.6 | None | stage2_captured_most_upside |
| C24_R7L93_950220_2024_03_22 | 950220 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24_R7L96_196170_2024_02_01 | 196170 | C24_BIO_TRIAL_DATA_EVENT_RISK | 71400.0 | None | None | 463.0 | None | stage2_captured_most_upside |
| C24_R7L96_217730_2024_04_25 | 217730 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24_R7L96_235980_2024_02_01 | 235980 | C24_BIO_TRIAL_DATA_EVENT_RISK | 10750.0 | None | None | 60.4 | None | stage2_captured_most_upside |
| R7L90_C24_APRILBIO_2024_TRIAL_DATA_LICENSING_BRIDGE_POSITIVE | 397030 | C24_BIO_TRIAL_DATA_EVENT_RISK | 14260.0 | None | None | 81.63 | None | stage2_actionable_best_entry |
| R7L90_C24_CURACLE_2024_TRIAL_DATA_FAILURE_FALSE_STAGE2 | 365270 | C24_BIO_TRIAL_DATA_EVENT_RISK | 18630.0 | None | None | 14.6 | None | stage2_actionable_best_entry |
| R7L90_C24_HLBBIO_2024_REGULATORY_TRIAL_EVENT_CAP_4B | 067630 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | 24300.0 | None | None | 4b_good_peak_capture |
| R7L93_C24_ABCLON_2024_CART_TRIAL_DATA_EVENT_CAP_4B | 174900 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | 21100.0 | None | None | 4b_good_peak_capture |
| R7L93_C24_NEOIMMUNETECH_2024_IMMUNO_ONCOLOGY_TRIAL_FALSE_STAGE2 | 950220 | C24_BIO_TRIAL_DATA_EVENT_RISK | 1665.0 | None | None | 18.74 | None | stage2_actionable_best_entry |
| R7L93_C24_OSCOTEC_2024_KINASE_PIPELINE_TRIAL_DATA_DURABILITY_POSITIVE | 039200 | C24_BIO_TRIAL_DATA_EVENT_RISK | 22050.0 | None | None | 102.27 | None | stage2_actionable_best_entry |
| R7L96_C24_ABION_2024_CLINICAL_DATA_EVENT_FALSE_STAGE2 | 203400 | C24_BIO_TRIAL_DATA_EVENT_RISK | 12390.0 | None | None | 4.92 | None | stage2_actionable_best_entry |
| R7L96_C24_HELIXMITH_2024_GENE_THERAPY_EVENT_CAP_4B | 084990 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | 5850.0 | None | None | 4b_good_peak_capture |
| R7L96_C24_VORONOI_2024_TARGETED_ONCOLOGY_PIPELINE_DATA_BRIDGE_POSITIVE | 310210 | C24_BIO_TRIAL_DATA_EVENT_RISK | 35050.0 | None | None | 239.23 | None | stage2_actionable_best_entry |

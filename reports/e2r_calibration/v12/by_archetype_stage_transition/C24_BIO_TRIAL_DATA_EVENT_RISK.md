# C24_BIO_TRIAL_DATA_EVENT_RISK Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `69`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 028300 | 028300 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| 069620 | 069620 | C24_BIO_TRIAL_DATA_EVENT_RISK | 123600.0 | None | None | 21.36 | None | stage2_captured_most_upside |
| 128940 | 128940 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| 141080 | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | 53500.0 | None | None | 94.4 | None | stage2_actionable_best_entry |
| 196170 | 196170 | C24_BIO_TRIAL_DATA_EVENT_RISK | 93900.0 | None | None | 287.11 | None | stage2_actionable_best_entry |
| 950160 | 950160 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | 11690.0 | None | None | no_valid_stage_transition |
| C24_R7L104_028300_20240425_HLB_PRE_FDA_BINARY_EVENT_SPIKE | 028300 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24_R7L104_140410_20240304_MEZZION_TRIAL_REDOSING_PATH | 140410 | C24_BIO_TRIAL_DATA_EVENT_RISK | 45250.0 | None | None | 10.94 | None | stage2_actionable_best_entry |
| C24_R7L104_215600_20240516_SILLAJEN_ONCOLYTIC_DATA_EVENT_SPIKE | 215600 | C24_BIO_TRIAL_DATA_EVENT_RISK | 4565.0 | None | None | 11.5 | None | stage2_actionable_best_entry |
| C24_R7L104_323990_20240517_VAXCELL_TRIAL_DATA_SPIKE_REVERSAL | 323990 | C24_BIO_TRIAL_DATA_EVENT_RISK | 17240.0 | None | None | 46.17 | None | stage2_actionable_best_entry |
| C24_R7L105_008930_20240130 | 008930 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | 46500.0 | None | None | no_valid_stage_transition |
| C24_R7L105_039200_20240226 | 039200 | C24_BIO_TRIAL_DATA_EVENT_RISK | 24900.0 | None | None | 21.0 | None | stage2_captured_most_upside |
| C24_R7L105_084990_20240202 | 084990 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | 4410.0 | None | None | no_valid_stage_transition |
| C24_R7L105_128940_20240115 | 128940 | C24_BIO_TRIAL_DATA_EVENT_RISK | 338000.0 | None | None | 11.39 | None | stage2_captured_most_upside |
| C24_R7L105_141080_20240129 | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | 53500.0 | None | None | 94.4 | None | stage2_actionable_best_entry |
| C24_R7L105_326030_20240229 | 326030 | C24_BIO_TRIAL_DATA_EVENT_RISK | 96900.0 | None | None | 23.32 | None | stage2_captured_most_upside |
| C24_R7L106_006280_20241021_S3Yellow | 006280 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24_R7L106_039840_20240314_S2 | 039840 | C24_BIO_TRIAL_DATA_EVENT_RISK | 20100.0 | None | None | 18.7 | None | stage2_captured_most_upside |
| C24_R7L106_041830_20240522_S3Yellow | 041830 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24_R7L106_060280_20240325_S2 | 060280 | C24_BIO_TRIAL_DATA_EVENT_RISK | 15460.0 | None | None | 9.4 | None | stage2_captured_most_upside |
| C24_R7L106_068270_20240701_S2 | 068270 | C24_BIO_TRIAL_DATA_EVENT_RISK | 184000.0 | None | None | 16.3 | None | stage2_captured_most_upside |
| C24_R7L106_069620_20240829_S2 | 069620 | C24_BIO_TRIAL_DATA_EVENT_RISK | 152000.0 | None | None | 8.55 | None | stage2_captured_most_upside |
| C24_R7L106_084990_20241115_S2 | 084990 | C24_BIO_TRIAL_DATA_EVENT_RISK | 3020.0 | None | None | 31.13 | None | stage2_captured_most_upside |
| C24_R7L106_099190_20240201_S2Actionable | 099190 | C24_BIO_TRIAL_DATA_EVENT_RISK | 21950.0 | None | None | 42.1 | None | stage2_actionable_best_entry |
| C24_R7L106_128940_20240805_S2 | 128940 | C24_BIO_TRIAL_DATA_EVENT_RISK | 258000.0 | None | None | 24.42 | None | stage2_captured_most_upside |
| C24_R7L106_141080_20240129_S3Yellow | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24_R7L106_196170_20240221_S3Green | 196170 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | 93900.0 | None | None | None | green_good_but_late |
| C24_R7L106_196170_20240920_S3Yellow | 196170 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24_R7L106_214680_20240226_S4B | 214680 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | 4860.0 | None | None | no_valid_stage_transition |
| C24_R7L106_253840_20240125_S4B | 253840 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | 6840.0 | None | None | no_valid_stage_transition |
| C24_R7L106_302550_20240321_S2 | 302550 | C24_BIO_TRIAL_DATA_EVENT_RISK | 8200.0 | None | None | 15.6 | None | stage2_captured_most_upside |
| C24_R7L106_326030_20240829_S2Actionable | 326030 | C24_BIO_TRIAL_DATA_EVENT_RISK | 119500.0 | None | None | 18.41 | None | stage2_actionable_best_entry |
| C24_R7L108_000250_20240311_STAGE3YELLOW_BIOSIMILAR_REGULATORY_LICENSE_BOUNDARY | 000250 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24_R7L108_006280_20240201_STAGE2_VACCINE_BIO_LABEL_WITHOUT_TRIAL_CATALYST | 006280 | C24_BIO_TRIAL_DATA_EVENT_RISK | 112000.0 | None | None | 8.0 | None | stage2_captured_most_upside |
| C24_R7L108_028300_20240517_LOCAL4BWATCH_NDA_CRL_BINARY_REGULATORY_BREAK_HIGH_MAE | 028300 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24_R7L108_068270_20240125_STAGE2_LARGECAP_COMMERCIAL_BIO_NOT_TRIAL_DATA | 068270 | C24_BIO_TRIAL_DATA_EVENT_RISK | 181000.0 | None | None | 10.0 | None | stage2_captured_most_upside |
| C24_R7L108_068760_20240527_STAGE2_COMMERCIAL_BIOSIMILAR_CONTAMINANT_C23 | 068760 | C24_BIO_TRIAL_DATA_EVENT_RISK | 89000.0 | None | None | 14.0 | None | stage2_captured_most_upside |
| C24_R7L108_084990_20240318_STAGE2_REDO_TRIAL_DELAY_4C_WATCH | 084990 | C24_BIO_TRIAL_DATA_EVENT_RISK | 5900.0 | None | None | 5.0 | None | stage2_captured_most_upside |
| C24_R7L108_086900_20240422_STAGE2ACTIONABLE_LEGAL_REGULATORY_BIO_EVENT_REROUTE | 086900 | C24_BIO_TRIAL_DATA_EVENT_RISK | 135000.0 | None | None | 11.0 | None | stage2_actionable_best_entry |
| C24_R7L108_140410_20240603_STAGE2ACTIONABLE_REGULATORY_RESUBMISSION_PROBABILITY_UPDATE | 140410 | C24_BIO_TRIAL_DATA_EVENT_RISK | 33000.0 | None | None | 30.0 | None | stage2_actionable_best_entry |
| C24_R7L108_141080_20240415_STAGE3YELLOW_ADC_PIPELINE_DATA_LICENSE_BOUNDARY | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24_R7L108_170900_20240408_STAGE2ACTIONABLE_PIPELINE_TRIAL_UPDATE_MIXED_ENDPOINT | 170900 | C24_BIO_TRIAL_DATA_EVENT_RISK | 65000.0 | None | None | 22.0 | None | stage2_actionable_best_entry |
| C24_R7L108_185750_20240129_STAGE2_COMMERCIAL_DRUG_REVENUE_REROUTE_C23 | 185750 | C24_BIO_TRIAL_DATA_EVENT_RISK | 116000.0 | None | None | 12.0 | None | stage2_captured_most_upside |
| C24_R7L108_196170_20240226_STAGE3YELLOW_PLATFORM_LICENSE_DATA_QUALITY_POSITIVE_BOUNDARY | 196170 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24_R7L108_214450_20240213_STAGE2_COMMERCIAL_MEDICAL_PRODUCT_CONTAMINANT_C25 | 214450 | C24_BIO_TRIAL_DATA_EVENT_RISK | 105000.0 | None | None | 16.0 | None | stage2_captured_most_upside |
| C24_R7L108_215600_20240226_STAGE2_TRIAL_RESUME_PRICE_SPIKE_WITHOUT_ENDPOINT | 215600 | C24_BIO_TRIAL_DATA_EVENT_RISK | 4700.0 | None | None | 8.0 | None | stage2_captured_most_upside |
| C24_R7L108_237690_20240304_STAGE2ACTIONABLE_OLIGO_CMO_PIPELINE_THEME_WITHOUT_ENDPOINT | 237690 | C24_BIO_TRIAL_DATA_EVENT_RISK | 76000.0 | None | None | 13.0 | None | stage2_actionable_best_entry |
| C24_R7L108_298380_20240321_STAGE2ACTIONABLE_PIPELINE_DATA_READOUT_WITHOUT_ENDPOINT_CASH | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | 21000.0 | None | None | 28.0 | None | stage2_actionable_best_entry |
| C24_R7L108_323990_20240502_STAGE2ACTIONABLE_CELL_THERAPY_DATA_EVENT_PRICE_SPIKE | 323990 | C24_BIO_TRIAL_DATA_EVENT_RISK | 18000.0 | None | None | 16.0 | None | stage2_actionable_best_entry |
| C24_R7_L107_001_141080_2024-01-29 | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | 53500.0 | None | None | 94.4 | None | stage2_actionable_best_entry |
| C24_R7_L107_002_039200_2024-02-26 | 039200 | C24_BIO_TRIAL_DATA_EVENT_RISK | 24900.0 | None | None | 21.0 | None | stage2_captured_most_upside |
| C24_R7_L107_003_008930_2024-01-30 | 008930 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | 46500.0 | None | None | no_valid_stage_transition |
| C24_R7_L107_004_128940_2024-01-15 | 128940 | C24_BIO_TRIAL_DATA_EVENT_RISK | 338000.0 | None | None | 11.39 | None | stage2_captured_most_upside |
| C24_R7_L107_005_084990_2024-02-02 | 084990 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | 4410.0 | None | None | no_valid_stage_transition |
| C24_R7_L107_006_326030_2024-02-29 | 326030 | C24_BIO_TRIAL_DATA_EVENT_RISK | 96900.0 | None | None | 23.32 | None | stage2_captured_most_upside |
| C24_R7_L107_007_196170_2024-02-21 | 196170 | C24_BIO_TRIAL_DATA_EVENT_RISK | 93900.0 | None | None | 287.11 | None | stage2_actionable_best_entry |
| C24_R7_L107_008_950160_2024-01-11 | 950160 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | 11690.0 | None | None | no_valid_stage_transition |
| C24_R7_L107_009_069620_2024-03-19 | 069620 | C24_BIO_TRIAL_DATA_EVENT_RISK | 123600.0 | None | None | 21.36 | None | stage2_captured_most_upside |
| C24_R7_L107_010_128940_2024-03-25 | 128940 | C24_BIO_TRIAL_DATA_EVENT_RISK | 347000.0 | None | None | 8.07 | None | stage2_captured_most_upside |
| C24_R7_L107_011_039840_2024-03-14 | 039840 | C24_BIO_TRIAL_DATA_EVENT_RISK | 20100.0 | None | None | 18.7 | None | stage2_captured_most_upside |
| C24_R7_L107_012_099190_2024-02-01 | 099190 | C24_BIO_TRIAL_DATA_EVENT_RISK | 21950.0 | None | None | 42.1 | None | stage2_actionable_best_entry |
| C24_R7_L107_013_214680_2024-02-26 | 214680 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | 4860.0 | None | None | no_valid_stage_transition |
| C24_R7_L107_014_060280_2024-03-25 | 060280 | C24_BIO_TRIAL_DATA_EVENT_RISK | 15460.0 | None | None | 9.4 | None | stage2_captured_most_upside |
| C24_R7_L107_015_041830_2024-05-22 | 041830 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24_R7_L107_016_100120_2024-06-12 | 100120 | C24_BIO_TRIAL_DATA_EVENT_RISK | 28750.0 | None | None | 26.4 | None | stage2_actionable_best_entry |
| C24_R7_L107_017_065510_2024-04-29 | 065510 | C24_BIO_TRIAL_DATA_EVENT_RISK | 15320.0 | None | None | 38.2 | None | stage2_actionable_best_entry |
| C24_R7_L107_018_104540_2024-02-02 | 104540 | C24_BIO_TRIAL_DATA_EVENT_RISK | 9870.0 | None | None | 11.6 | None | stage2_captured_most_upside |
| C24_R7_L107_019_253840_2024-01-25 | 253840 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | 6840.0 | None | None | no_valid_stage_transition |
| C24_R7_L107_020_149980_2024-05-17 | 149980 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |

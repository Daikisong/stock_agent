# C24_BIO_TRIAL_DATA_EVENT_RISK Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `60`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 141080 | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| 298380 | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| 950220 | 950220 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24-ALTEOGEN-KEYTRUDA-SC-NONINFERIOR-20241120 | 196170 | C24_BIO_TRIAL_DATA_EVENT_RISK | 350500.0 | None | None | 44.94 | None | stage2_actionable_best_entry |
| C24-HANALL-IMVT1402-PH1-20230927 | 009420 | C24_BIO_TRIAL_DATA_EVENT_RISK | 32650.0 | None | None | 43.19 | None | stage2_actionable_best_entry |
| C24-HLB-RIVOCERANIB-CRL-20240517 | 028300 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24-SHINPOONG-PYRAMAX-PH2-20210705 | 019170 | C24_BIO_TRIAL_DATA_EVENT_RISK | 95600.0 | None | None | 6.17 | None | stage2_actionable_best_entry |
| C24-YUHAN-MARIPOSA-DATA-20231004 | 000100 | C24_BIO_TRIAL_DATA_EVENT_RISK | 79000.0 | None | None | 11.9 | None | stage2_actionable_best_entry |
| C24_067630_HLBBIO_20240517_RIVOCERANIB_CRL_GROUP_EVENT_FALSE_GREEN | 067630 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24_084990_HELIXMITH_20190924_VM202_PHASE3_DATA_4C_WATCH | 084990 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| C24_215600_SILLAJEN_20190802_PEXAVEC_TRIAL_FUTILITY_HARD_4C | 215600 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| R13L32_C24_009420_HANALL_20230927_PARTNER_DATA_POSITIVE | 009420 | C24_BIO_TRIAL_DATA_EVENT_RISK | 32650.0 | 44300.0 | None | 43.19 | None | green_too_late |
| R13L32_C24_039200_OSCOTEC_20200921_DATA_POSITIVE_HIGH_MAE | 039200 | C24_BIO_TRIAL_DATA_EVENT_RISK | 46000.0 | None | None | 55.43 | None | 4c_too_late |
| R13L32_C24_215600_SILLAJEN_20190802_PHASE3_FUTILITY_4C | 215600 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | 4c_too_late |
| R13L32_C24_298380_ABL_20220112_LICENSE_EVENT_FALSE_POSITIVE | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | 26150.0 | None | 33050.0 | 33.0847 | 79.7536 | 4b_good_peak_capture |
| R7L11_C24_000100_YUHAN_20240821_POSITIVE | 000100 | C24_BIO_TRIAL_DATA_EVENT_RISK | 94300.0 | 145400.0 | None | 76.9933 | None | green_too_late |
| R7L11_C24_028300_HLB_20240520_4C | 028300 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | 4c_too_late |
| R7L11_C24_196170_ALTEOGEN_20240223_POSITIVE_4B | 196170 | C24_BIO_TRIAL_DATA_EVENT_RISK | 131200.0 | None | None | 247.18 | None | stage2_actionable_best_entry |
| R7L11_C24_302440_SKBIO_20220706_FALSE_POSITIVE | 302440 | C24_BIO_TRIAL_DATA_EVENT_RISK | 121500.0 | None | None | 28.81 | None | stage2_actionable_best_entry |
| R7L12-C24-000100-YUHAN-MARIPOSA-READOUT-HIGHMAE-SUCCESS | 000100 | C24_BIO_TRIAL_DATA_EVENT_RISK | 62000.0 | None | None | 59.03 | None | stage2_actionable_best_entry |
| R7L12-C24-019170-SHINPOONG-PYRAMAX-DATA-FAILURE | 019170 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | 4c_too_late |
| R7L12-C24-028300-HLB-BINARY-READOUT-REGULATORY-REUSE | 028300 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | 95800.0 | None | None | None | green_false_positive |
| R7L12-C24-039200-OSCOTEC-MARIPOSA-READOUT-RERATING | 039200 | C24_BIO_TRIAL_DATA_EVENT_RISK | 21850.0 | None | 43400.0 | 148.5221 | 66.4056 | stage2_actionable_best_entry |
| R7L13_C24_HANALL_IMVT1402_PHASE1 | 009420 | C24_BIO_TRIAL_DATA_EVENT_RISK | 32650.0 | None | None | 43.19 | None | stage2_actionable_best_entry |
| R7L13_C24_HLB_PDUFA_BINARY_RISK | 028300 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | 95800.0 | None | None | 4c_too_late |
| R7L13_C24_YUHAN_MARIPOSA_PHASE3 | 000100 | C24_BIO_TRIAL_DATA_EVENT_RISK | 62000.0 | None | None | 34.52 | None | stage2_actionable_best_entry |
| R7L15-C24-009420-HANALL-IMVT1402-PH1-HIGHMAE-SUCCESS | 009420 | C24_BIO_TRIAL_DATA_EVENT_RISK | 32650.0 | None | 44300.0 | 43.19 | 82.6151 | stage2_actionable_best_entry |
| R7L15-C24-215600-SILLAJEN-PEXAVEC-FUTILITY-4C | 215600 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | 44550.0 | None | None | None | 4c_too_late |
| R7L15-C24-220100-FUTURECHEM-RADIOPHARMA-DATA-20240522 | 220100 | C24_BIO_TRIAL_DATA_EVENT_RISK | 14850.0 | None | None | 109.76 | None | stage2_actionable_best_entry |
| R7L15-C24-220100-FUTURECHEM-RADIOPHARMA-DATA-20240522 | None | C24_BIO_TRIAL_DATA_EVENT_RISK | 14850.0 | None | None | 109.76 | None | stage2_actionable_best_entry |
| R7L15-C24-288330-BRIDGEBIO-BBT877-RESET-20230623 | 288330 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| R7L15-C24-288330-BRIDGEBIO-BBT877-RESET-20230623 | None | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| R7L15-C24-298380-ABL-SANOFI-ABL301-HIGHMAE-SUCCESS | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | 26150.0 | None | None | 33.08 | None | stage2_actionable_best_entry |
| R7L15-C24-310210-VORONOI-VRN11-DATA-20240524 | 310210 | C24_BIO_TRIAL_DATA_EVENT_RISK | 36600.0 | None | None | 237.43 | None | stage2_actionable_best_entry |
| R7L15-C24-310210-VORONOI-VRN11-DATA-20240524 | None | C24_BIO_TRIAL_DATA_EVENT_RISK | 36600.0 | None | None | 237.43 | None | stage2_actionable_best_entry |
| R7L15-C24-365270-CURACLE-CU06-DME-DATA-20240522 | 365270 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| R7L15-C24-365270-CURACLE-CU06-DME-DATA-20240522 | None | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| R7L16_C24_NEG_028300_20240517_FDA_CRL | 028300 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | 4c_too_late |
| R7L16_C24_NEG_293780_20220801_AMBIGUOUS_PHASE2_POP | 293780 | C24_BIO_TRIAL_DATA_EVENT_RISK | 25950.0 | None | None | 6.36 | None | stage2_actionable_best_entry |
| R7L16_C24_POS_000100_20240820_FDA_MARIPOSA_APPROVAL | 000100 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | 94000.0 | None | None | None | green_good_but_late |
| R7L16_C24_POS_039200_20240220_CODEV_TRIAL_OPTION | 039200 | C24_BIO_TRIAL_DATA_EVENT_RISK | 22050.0 | None | None | 107.94 | None | stage2_actionable_best_entry |
| R7L27-C24-000100-MARIPOSA | 000100 | C24_BIO_TRIAL_DATA_EVENT_RISK | 58000.0 | None | None | 73.1 | None | stage2_actionable_best_entry |
| R7L27-C24-039200-MARIPOSA | 039200 | C24_BIO_TRIAL_DATA_EVENT_RISK | 19670.0 | None | None | 128.27 | None | stage2_actionable_best_entry |
| R7L27-C24-084990-ENGENSIS | 084990 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| R7L27-C24-215600-PHOCUS | 215600 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| R7L71_C24_000100_LAZERTINIB_MARIPOSA_APPROVAL_BRIDGE | 000100 | C24_BIO_TRIAL_DATA_EVENT_RISK | 94000.0 | None | None | 77.55 | None | stage2_actionable_best_entry |
| R7L71_C24_084990_ENGENSIS_DPN_PHASE3_FAILURE | 084990 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | 4c_too_late |
| R7L71_C24_302440_SKY_COVIONE_PHASE3_DEMAND_TRAP | 302440 | C24_BIO_TRIAL_DATA_EVENT_RISK | 135500.0 | None | None | 15.5 | None | stage2_actionable_best_entry |
| R7L74-C24-141080-LCB-ADC-PLATFORM-DATA-DERISKING | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| R7L74-C24-298380-ABL-BISPECIFIC-PLATFORM-DATA-RERATING | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| R7L74-C24-950220-NEOIMMUNETECH-IMMUNOTHERAPY-TRIAL-HEADLINE-FADE | 950220 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| R7L76-C24-141080-LIGACHEM-ADC-TRIAL-DATA-POST-CA-LIFECYCLE | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | 68000.0 | None | None | 105.29 | None | stage2_actionable_best_entry |
| R7L76-C24-215600-SILLAJEN-ONCOLOGY-TRIAL-DATA-POST-CA-BETA-FADE | 215600 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| R7L76-C24-298380-ABL-BIO-BISPECIFIC-ADC-TRIAL-DATA-BRIDGE | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | 21500.0 | None | None | 101.4 | None | stage2_actionable_best_entry |
| R7L78-C24-141080-LIGACHEM-ADC-DATA-PARTNERING-POST-CA | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | 68000.0 | None | None | 105.29 | None | stage2_actionable_best_entry |
| R7L78-C24-220100-FUTURECHEM-RADIOPHARMA-TRIAL-DATA | 220100 | C24_BIO_TRIAL_DATA_EVENT_RISK | 8500.0 | None | None | 267.65 | None | stage2_actionable_best_entry |
| R7L78-C24-950220-NEOIMMUNETECH-IMMUNO-ONCOLOGY-DATA-FADE | 950220 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |
| R7L80-C24-141080-LIGACHEM-ADC-POSTCA-DATA-LICENSE-MILESTONE | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | 68000.0 | None | None | 111.18 | None | stage2_actionable_best_entry |
| R7L80-C24-298380-ABL-BIO-BIOPLATFORM-DATA-LICENSE-MILESTONE | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | 21700.0 | None | None | 99.54 | None | stage2_actionable_best_entry |
| R7L80-C24-323990-VAXCELL-TRIAL-THEME-FADE | 323990 | C24_BIO_TRIAL_DATA_EVENT_RISK | None | None | None | None | None | no_valid_stage_transition |

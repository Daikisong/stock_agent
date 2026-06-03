# C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `27`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 149980 | 149980 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | None | None | None | None | no_valid_stage_transition |
| 214680 | 214680 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | None | None | None | None | no_valid_stage_transition |
| 263690 | 263690 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | None | None | None | None | no_valid_stage_transition |
| 336570 | 336570 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 8400.0 | None | None | 42.86 | None | stage2_actionable_best_entry |
| 340570 | 340570 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 50500.0 | None | None | 52.48 | None | stage2_actionable_best_entry |
| R7L71_C25_060280_SURGICAL_ROBOT_EXPORT | 060280 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 9320.0 | None | None | 176.29 | None | stage2_actionable_best_entry |
| R7L71_C25_060280_SURGICAL_ROBOT_EXPORT | None | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 9320.0 | None | None | 176.29 | None | stage2_actionable_best_entry |
| R7L71_C25_099190_CGM_HYPE_4B | 099190 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | None | 32000.0 | None | None | no_valid_stage_transition |
| R7L71_C25_099190_CGM_HYPE_4B | None | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | None | 32000.0 | None | None | 4b_good_peak_capture |
| R7L71_C25_336570_AESTHETIC_DEVICE_EXPORT | 336570 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 5720.0 | None | None | 164.16 | None | stage2_actionable_best_entry |
| R7L71_C25_336570_AESTHETIC_DEVICE_EXPORT | None | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 5720.0 | None | None | 164.16 | None | stage2_actionable_best_entry |
| R7L71_C25_ISENS_CGM_REIMBURSEMENT_FALSE_GREEN_20240110 | 099190 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 29500.0 | None | None | 3.05 | None | stage2_actionable_best_entry |
| R7L71_C25_VATECH_DENTAL_EXPORT_STAGNATION_20240308 | 043150 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | None | None | None | None | no_valid_stage_transition |
| R7L71_C25_WONTECH_EXPORT_CONSUMABLE_PULLTHROUGH_20230213 | 336570 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 5490.0 | None | None | 175.23 | None | stage2_actionable_best_entry |
| R7L74_C25_060280_20240129_SURGICAL_ROBOT_DEVICE_THEME_NO_ORDER_REIMBURSEMENT_BRIDGE | 060280 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 15540.0 | None | None | 7.46 | None | stage2_actionable_best_entry |
| R7L74_C25_100120_VIEWORKS_IMAGING_EXPORT_COUNTER | 100120 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 39650.0 | None | None | 8.45 | None | stage2_captured_most_upside |
| R7L74_C25_145720_DENTIUM_CHINA_VBP_EXPORT_COUNTER | 145720 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 159200.0 | None | None | 18.41 | None | stage2_captured_most_upside |
| R7L74_C25_200670_20240401_MEDICAL_CONSUMABLE_EXPORT_MARGIN_BRIDGE | 200670 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 29250.0 | None | None | 57.95 | None | stage2_actionable_best_entry |
| R7L74_C25_214150_CLASSYS_EXPORT_CONSUMABLE_POS | 214150 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 32850.0 | None | 32850.0 | 85.69 | 0.0 | 4b_good_peak_capture |
| R7L74_C25_214450_20240401_MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE | 214450 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 108000.0 | None | None | 147.22 | None | stage2_actionable_best_entry |
| R7L74_C25_338220_VUNO_AI_REIMBURSEMENT_HIGH_MAE_POS | 338220 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 18900.0 | None | 18900.0 | 172.49 | 0.0 | stage2_actionable_best_entry |
| R7L84-C25-01 | 336570 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 7880.0 | None | None | 42.13 | None | stage2_actionable_best_entry |
| R7L84-C25-02 | 065510 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | None | None | None | None | no_valid_stage_transition |
| R7L84-C25-03 | 263690 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | None | None | None | None | no_valid_stage_transition |
| R7L87-C25-01 | 041830 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 25650.0 | None | None | 20.47 | None | stage2_actionable_best_entry |
| R7L87-C25-02 | 336570 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | None | None | None | None | no_valid_stage_transition |
| R7L87-C25-03 | 100120 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | None | None | None | None | no_valid_stage_transition |

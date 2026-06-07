# C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `6`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C25_R7L92_099190_ISENS_CGM_REIMBURSEMENT_DECAY | 099190 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | None | None | None | None | no_valid_stage_transition |
| C25_R7L92_145720_DENTIUM_DENTAL_IMPLANT_SPIKE_DECAY | 145720 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | None | None | None | None | no_valid_stage_transition |
| C25_R7L92_214150_CLASSYS_AESTHETIC_DEVICE_CONSUMABLE | 214150 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 30000.0 | None | None | 109.67 | None | stage2_actionable_best_entry |
| R7L99_C25_CLASSYS_2024_AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_POSITIVE | 214150 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 30000.0 | None | None | 109.67 | None | stage2_actionable_best_entry |
| R7L99_C25_DENTIUM_2024_DENTAL_EXPORT_REIMBURSEMENT_FALSE_STAGE2 | 145720 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 144200.0 | None | None | 2.98 | None | stage2_actionable_best_entry |
| R7L99_C25_WONTECH_2024_ENERGY_BASED_MEDICAL_DEVICE_EVENT_CAP_4B | 336570 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | None | None | 10850.0 | None | None | 4b_good_peak_capture |

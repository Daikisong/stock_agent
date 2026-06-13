# C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `26`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 000240 | 000240 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | None | 20750.0 | None | None | no_valid_stage_transition |
| 008930 | 008930 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | None | 43300.0 | None | None | no_valid_stage_transition |
| 010130 | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | 666000.0 | None | None | None | green_good_but_late |
| 011200 | 011200 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 17540.0 | None | None | 32.8392 | None | stage2_actionable_best_entry |
| 041510 | 041510 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | None | 149700.0 | None | None | no_valid_stage_transition |
| 241560 | 241560 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | None | 54600.0 | None | None | no_valid_stage_transition |
| C32_000990_20230330_DBHITEK_KCGI_ACTIVISM | 000990 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 61100.0 | None | None | 36.82 | None | stage2_actionable_best_entry |
| C32_008930_20240112_HANMI_OCI_MERGER_CONTROL_PREMIUM | 008930 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 38400.0 | None | None | 46.35 | None | stage2_actionable_best_entry |
| C32_008930_20240328_HANMI_OCI_SCRAPPED | 008930 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | None | None | None | None | 4c_too_late |
| C32_009240_20210714_HANSSEM_IMM_CONTROL_PREMIUM | 009240 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | None | 146500.0 | None | None | 4b_good_peak_capture |
| C32_010130_20241004_KOREA_ZINC_TENDER_ESCALATION | 010130 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 776000.0 | None | None | 210.18 | None | stage2_actionable_best_entry |
| C32_036560_20241002_YP_PRECISION_AFFILIATE_TENDER_CAP | 036560 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | None | 25450.0 | None | None | no_valid_stage_transition |
| C32_041510_20230210_SM_HYBE_INITIAL_TENDER | 041510 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 114700.0 | None | None | 40.54 | None | stage2_actionable_best_entry |
| C32_041510_20230307_SM_KAKAO_WHITE_KNIGHT_CAP | 041510 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | None | 149700.0 | None | None | no_valid_stage_transition |
| C32_180640_20201201_HANJIN_KAL_KDB_CONTROL_STABILIZATION | 180640 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | None | None | None | None | 4c_too_late |
| C32_BOBCAT_ANNOUNCE_MINORITY_CAPTURE_RISK | 241560 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | None | 52000.0 | None | None | no_valid_stage_transition |
| C32_BOBCAT_FINAL_SCRAP_PUBLIC_CAPTURE | 241560 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 43200.0 | None | None | 71.06 | None | stage2_actionable_best_entry |
| C32_BOBCAT_WITHDRAWAL_MINORITY_RELIEF | 241560 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | None | None | None | None | no_valid_stage_transition |
| C32_DOOSAN_ANNOUNCE_HOLDCO_OPTIONALITY | 000150 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | None | 241500.0 | None | None | no_valid_stage_transition |
| C32_DOOSAN_FINAL_SCRAP_HOLDCO_RERATING | 000150 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 214000.0 | None | None | 226.87 | None | stage2_actionable_best_entry |
| C32_DOOSAN_WITHDRAWAL_RELIEF_RESET | 000150 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 147900.0 | None | None | 251.59 | None | stage2_actionable_best_entry |
| C32_ROBOTICS_ANNOUNCE_DERIVATIVE_OPTIONALITY | 454910 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | None | 85300.0 | None | None | no_valid_stage_transition |
| C32_ROBOTICS_FINAL_SCRAP_NO_HARDBLOCK | 454910 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | None | None | None | None | no_valid_stage_transition |
| C32_ROBOTICS_WITHDRAWAL_OPTIONALITY_DECAY | 454910 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | None | 69300.0 | None | None | no_valid_stage_transition |
| C32_SAMSUNGCNT_ACTIVIST_PROPOSAL | 028260 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | None | None | None | None | no_valid_stage_transition |
| C32_SAMSUNGCNT_VOTE_DEFEAT | 028260 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | None | None | None | None | None | 4c_too_late |

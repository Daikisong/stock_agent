# C05_EPC_MEGA_CONTRACT_MARGIN_GAP Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `13`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C05_L92_000720_20240422_backlog_not_margin | 000720 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 34000.0 | None | None | 5.88 | None | stage2_actionable_best_entry |
| C05_L92_028050_20240228_margin_recovery_stress | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 26000.0 | None | None | 12.69 | None | stage2_actionable_best_entry |
| C05_L92_034020_20240311_plant_project_beta | 034020 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 16720.0 | None | None | 49.52 | None | stage2_actionable_best_entry |
| C05_L92_047040_20240110_contract_theme_decay | 047040 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| C05_R11L92_011930_SHINSUNG_CLEANROOM_EPC | 011930 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 1948.0 | None | None | 30.65 | None | stage2_actionable_best_entry |
| C05_R11L92_023350_KOREA_ENGINEERING_POLICY_PROJECT | 023350 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| C05_R11L92_023960_SCENG_SMALL_PLANT_EPC_LATE_SPIKE | 023960 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| C05_R1L83_CASE_000720_JAFURAH_20240630 | 000720 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 33200.0 | None | None | 13.1 | None | stage2_captured_most_upside |
| C05_R1L83_CASE_006360_FADHILI_20240402 | 006360 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 15630.0 | None | None | 39.16 | None | stage2_actionable_best_entry |
| C05_R1L83_CASE_028050_FADHILI_20240402 | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 25300.0 | None | None | 15.81 | None | stage2_captured_most_upside |
| R1L101_C05_DAEWOOE&C_2024_EPC_MARGIN_GAP_FALSE_STAGE2 | 047040 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 4260.0 | None | None | 16.55 | None | stage2_actionable_best_entry |
| R1L101_C05_DLENC_2024_EPC_EVENT_PREMIUM_MARGIN_GAP_4B | 375500 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | 40750.0 | None | None | 4b_good_peak_capture |
| R1L101_C05_HDCDEV_2024_LARGE_PROJECT_BACKLOG_MARGIN_BRIDGE_POSITIVE | 294870 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 15570.0 | None | None | 40.98 | None | stage2_actionable_best_entry |

# C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `10`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C09_R2L111_01_042700_20240201_Stage3Yellow | 042700 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | None | None | None | None | None | no_valid_stage_transition |
| C09_R2L111_02_089030_20240201_Stage3Yellow | 089030 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | None | None | None | None | None | no_valid_stage_transition |
| C09_R2L111_03_031980_20240201_Stage3Yellow | 031980 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | None | None | None | None | None | no_valid_stage_transition |
| C09_R2L111_04_232140_20240415_Stage2Actionable | 232140 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 14600.0 | None | None | 96.2 | None | stage2_actionable_best_entry |
| C09_R2L111_05_039030_20240223_Stage2Actionable | 039030 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 177000.0 | None | None | 48.3 | None | stage2_actionable_best_entry |
| C09_R2L111_06_403870_20240304_Stage4BLocal | 403870 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | None | None | 59300.0 | None | None | no_valid_stage_transition |
| C09_R2L111_07_101490_20240306_Stage4BLocal | 101490 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | None | None | 50700.0 | None | None | no_valid_stage_transition |
| C09_R2L111_08_036810_20240318_Stage4BLocal | 036810 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | None | None | 31900.0 | None | None | no_valid_stage_transition |
| C09_R2L111_09_079370_20240201_Stage2 | 079370 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 20900.0 | None | None | 24.4 | None | stage2_captured_most_upside |
| C09_R2L111_10_095610_20240215_Stage2 | 095610 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 22950.0 | None | None | 23.0 | None | stage2_captured_most_upside |

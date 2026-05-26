# C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `6`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| R13L13_C09_039030_ADVANCED_EQUIPMENT_4B | 039030 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 183900.0 | None | 273000.0 | 52.8 | 91.7618 | 4b_good_peak_capture |
| R13L13_C09_042700_VALUATION_4B_HOLDOUT | 042700 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 78500.0 | None | 179900.0 | 150.0 | 86.1146 | 4b_good_peak_capture |
| R13L13_C09_058470_QUALITY_BUT_NO_ORDER_CAP | 058470 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | None | None | None | None | None | no_valid_stage_transition |
| R13L13_C09_089030_VALUATION_4B_HOLDOUT | 089030 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 14600.0 | None | None | 384.93 | None | stage2_actionable_best_entry |
| R13L13_C09_095340_VALUATION_FALSE_GREEN | 095340 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | None | None | None | None | None | 4c_too_late |
| None | None | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 14600.0 | None | 273000.0 | 2016.3938 | 87.7737 | stage2_actionable_best_entry |

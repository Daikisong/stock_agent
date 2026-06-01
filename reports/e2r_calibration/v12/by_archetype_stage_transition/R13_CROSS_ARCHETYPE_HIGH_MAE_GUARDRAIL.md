# R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `23`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| R13L11_HIGHMAE_X01_011780_C17 | 011780 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 153500.0 | None | None | 94.46 | None | stage2_actionable_best_entry |
| R13L11_HIGHMAE_X02_218150_C31 | 218150 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 8090.0 | None | None | 59.46 | None | stage2_actionable_best_entry |
| R13L11_HIGHMAE_X03_192820_C20 | 192820 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 160500.0 | None | None | 29.6 | None | stage2_actionable_best_entry |
| R13L11_HIGHMAE_X04_028300_C23 | 028300 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | 95800.0 | None | None | None | green_false_positive |
| R13L11_HIGHMAE_X05_006650_C17 | 006650 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | 393500.0 | None | None | None | green_false_positive |
| R13L11_HIGHMAE_X06_066970_C14 | 066970 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | None | 263000.0 | None | None | no_valid_stage_transition |
| R13L11_HIGHMAE_X07_039610_C31 | 039610 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | None | None | None | None | no_valid_stage_transition |
| R13L11_HIGHMAE_X08_003070_C30 | 003070 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 9130.0 | None | None | 76.45 | None | stage2_actionable_best_entry |
| R13L14-G01-HIGH-MAE-SUCCESS-NOT-REJECT | 012450 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 79600.0 | None | None | 50.88 | None | stage2_actionable_best_entry |
| R13L14-G01-HIGH-MAE-SUCCESS-NOT-REJECT | 058470 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 234000.0 | None | None | 32.05 | None | stage2_actionable_best_entry |
| R13L14-G02-THEME-PROXY-FALSE-POSITIVE | 001390 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 36300.0 | None | None | 44.9 | None | stage2_actionable_best_entry |
| R13L14-G02-THEME-PROXY-FALSE-POSITIVE | 001570 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 152200.0 | None | None | 27.46 | None | stage2_actionable_best_entry |
| R13L14-G02-THEME-PROXY-FALSE-POSITIVE | 009520 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 39150.0 | None | None | 20.05 | None | stage2_actionable_best_entry |
| R13L14-G02-THEME-PROXY-FALSE-POSITIVE | 095340 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 93700.0 | None | None | 15.26 | None | stage2_actionable_best_entry |
| R13L14-G02-THEME-PROXY-FALSE-POSITIVE | 095660 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 34500.0 | None | None | 3.04 | None | stage2_actionable_best_entry |
| R13L14-G03-FALSE-GREEN-EVENT-RISK | 028300 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | 95800.0 | None | None | None | green_false_positive |
| R13L14-G04-PRICE-ONLY-4B-LOCAL-PEAK | 006220 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | None | None | None | None | no_valid_stage_transition |
| R13L14-G04-PRICE-ONLY-4B-LOCAL-PEAK | 041510 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | None | 149700.0 | None | None | 4b_good_peak_capture |
| R13L14-G05-4B-TOO-LATE-BLOWOFF | 003310 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | None | 5620.0 | None | None | no_valid_stage_transition |
| R13L14-G05-4B-TOO-LATE-BLOWOFF | 257720 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | None | 50700.0 | None | None | 4b_good_peak_capture |
| R13L14-G06-HARD-4C-THESIS-BREAK-LATE | 008930 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | None | None | None | None | 4c_too_late |
| R13L14-G06-HARD-4C-THESIS-BREAK-LATE | 028300 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | None | None | None | None | 4c_too_late |
| R13L14-G06-HARD-4C-THESIS-BREAK-LATE | 323410 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | None | None | None | None | no_valid_stage_transition |

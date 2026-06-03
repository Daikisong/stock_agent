# R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `30`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 000670 | 000670 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 487500.0 | None | None | 33.13 | None | stage2_actionable_best_entry |
| 002990 | 002990 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | None | None | None | None | no_valid_stage_transition |
| 008970 | 008970 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | None | 1175.0 | None | None | no_valid_stage_transition |
| 010690 | 010690 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 14600.0 | None | None | 55.48 | None | stage2_actionable_best_entry |
| 014790 | 014790 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | None | None | None | None | no_valid_stage_transition |
| 017040 | 017040 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | None | 2685.0 | None | None | no_valid_stage_transition |
| 020150 | 020150 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | None | None | None | None | no_valid_stage_transition |
| 036560 | 036560 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | None | 30500.0 | None | None | no_valid_stage_transition |
| 065450 | 065450 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | None | 6600.0 | None | None | no_valid_stage_transition |
| 089030 | 089030 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 18200.0 | None | None | 289.01 | None | stage2_actionable_best_entry |
| 149980 | 149980 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | None | None | None | None | no_valid_stage_transition |
| 225570 | 225570 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 18610.0 | None | None | 66.31 | None | stage2_actionable_best_entry |
| 299030 | 299030 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | None | None | None | None | no_valid_stage_transition |
| 340570 | 340570 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 50500.0 | None | None | 52.48 | None | stage2_actionable_best_entry |
| R13L71_HIGHMAE_C28_042510_20240126_SECURITY_POLICY_PRICE_ONLY | 042510 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 2940.0 | None | None | 4.25 | None | stage2_actionable_best_entry |
| R13L71_HIGHMAE_C30_014790_20230524_SMALL_BUILDER_ONE_DAY_SPIKE | 014790 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 2975.0 | None | None | 11.43 | None | stage2_actionable_best_entry |
| R13L71_HIGHMAE_C31_054050_20220315_SEED_POLICY_THEME | 054050 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 12150.0 | None | None | 19.34 | None | stage2_actionable_best_entry |
| R13L73_HMAE_CEX_006910 | 006910 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 6840.0 | None | None | 32.31 | None | stage2_actionable_best_entry |
| R13L73_HMAE_CEX_028300 | 028300 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | None | None | None | None | no_valid_stage_transition |
| R13L73_HMAE_CEX_053800 | 053800 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | None | None | None | None | None | no_valid_stage_transition |
| R13L73_HMAE_CEX_247540 | 247540 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 323000.0 | None | None | 9.6 | None | stage2_actionable_best_entry |
| R13L73_HMAE_POS_003230 | 003230 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 446500.0 | None | None | 85.44 | None | stage2_actionable_best_entry |
| R13L73_HMAE_POS_112610 | 112610 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 55500.0 | None | None | 45.05 | None | stage2_actionable_best_entry |
| R13L73_HMAE_POS_138040 | 138040 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 71800.0 | None | None | 49.3 | None | stage2_actionable_best_entry |
| R13L73_HMAE_POS_196170 | 196170 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 131200.0 | None | None | 247.18 | None | stage2_actionable_best_entry |
| R13L74_HIGHMAE_C30_002780_20240129_SMALL_BUILDER_PF_HIGH_MAE_FALSE_POSITIVE | 002780 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 1046.0 | None | None | 9.85 | None | stage2_actionable_best_entry |
| R13L74_HIGHMAE_C31_034230_20240129_CASINO_TOURISM_MFE_WITHOUT_MARGIN_BRIDGE | 034230 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 12750.0 | None | None | 22.9 | None | stage2_actionable_best_entry |
| R13L74_HIGHMAE_C31_039130_20240129_SERVICE_DEMAND_BRIDGE_POSITIVE_CONTROL | 039130 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 60900.0 | None | None | 15.93 | None | stage2_actionable_best_entry |
| R13L74_HIGHMAE_C31_080160_20240129_TOURISM_THEME_HIGH_MAE_FALSE_POSITIVE | 080160 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 17070.0 | None | None | 4.04 | None | stage2_actionable_best_entry |
| R13L74_HIGHMAE_C32_040300_20240205_PRIVATIZATION_EVENT_HIGH_MAE_FALSE_POSITIVE | 040300 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 5840.0 | None | None | 12.67 | None | stage2_actionable_best_entry |

# C13_BATTERY_JV_UTILIZATION_AMPC_IRA Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `27`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C13-LGES-2024Q2-AMPC-CAPACITY-PACING | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13-SDI-2024-STARPLUS-DOE-LOAN | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 261000.0 | None | None | 2.68 | None | stage2_actionable_best_entry |
| C13-SKI-2024-BLUEOVAL-FINAL-LOAN | 096770 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 121400.0 | None | None | 15.49 | None | stage2_actionable_best_entry |
| C13_003670_POSCOFUTUREM_20230331_CATHODE_JV_IRA_STAGE2 | 003670 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 272500.0 | None | None | 154.68 | None | stage2_actionable_best_entry |
| C13_005070_COSMOAMT_20230726_CATHODE_MATERIAL_UTILIZATION_4B | 005070 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | 190400.0 | None | None | no_valid_stage_transition |
| C13_006400_SAMSUNGSDI_20230411_AMPC_JV_UTILIZATION_FALSE_GREEN | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_006400_SDI_20230307_AMPC_JV_UTILIZATION_FALSE_GREEN | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_051910_LGCHEM_20230726_CATHODE_IRA_FALSE_GREEN | 051910 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_096770_SKINNOV_20230726_AMPC_JV_UTILIZATION_PRICE_PREMIUM_4B | 096770 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | 204500.0 | None | None | no_valid_stage_transition |
| C13_096770_SKINNO_20230330_SKON_AMPC_UTILIZATION_COUNTEREXAMPLE | 096770 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13_373220_LGES_20220812_IRA_AMPC_JV_STAGE2_SUCCESS | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 460500.0 | None | None | 36.59 | None | stage2_actionable_best_entry |
| C13_373220_LGES_20220816_IRA_AMPC_JV_CAPACITY_STAGE2 | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 460500.0 | None | None | 36.59 | None | stage2_actionable_best_entry |
| R3L10-C13-006400-STELLANTIS-KOKOMO-20231012 | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| R3L10-C13-373220-IRA-AMPC-20220817 | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 453500.0 | None | None | 38.7 | None | stage2_actionable_best_entry |
| R3L10-C13-373220-SLOW-EV-CAPEX-20240425 | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| R3L14_C13_LGES_20230411_AMPC_UTILIZATION_LAG | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| R3L14_C13_LOTTEEM_20230726_COPPERFOIL_LOCALIZATION_CAPEX | 020150 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| R3L14_C13_POSCO_FUTURE_M_20230126_IRA_LOCALIZATION | 003670 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 208500.0 | None | None | 232.85 | None | stage2_actionable_best_entry |
| R3L14_C13_SAMSUNGSDI_20230425_GM_JV_LONG_LEAD | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| R3L14_C13_SKINNOVATION_20230726_AMPC_CAPEX_PARENT_OVERHANG | 096770 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| R3L67_LGES_2024_Q1_AMPC_CAPEX_GUARD | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 372500.0 | None | None | 19.19 | None | stage2_actionable_best_entry |
| R3L67_LGES_2025_Q1_AMPC_MARGIN_BRIDGE | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 318000.0 | None | None | 65.72 | None | stage2_actionable_best_entry |
| R3L67_SDI_2024_GM_JV_DELAYED_RERATING | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 339500.0 | None | None | 15.91 | None | stage2_actionable_best_entry |
| R3L70_C13_006400_STELLANTIS_FIRST_KOKOMO | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 588000.0 | None | None | 33.16 | None | stage2_actionable_best_entry |
| R3L70_C13_006400_STELLANTIS_SECOND_KOKOMO | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 535000.0 | None | None | 0.75 | None | stage2_actionable_best_entry |
| R3L70_C13_096770_BLUEOVAL_SK_DOE_LOAN | 096770 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 182600.0 | None | None | 25.68 | None | stage2_actionable_best_entry |
| R3L70_C13_373220_IRA_ENACTMENT_STAGE2 | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 453500.0 | None | None | 38.7 | None | stage2_actionable_best_entry |

# C13_BATTERY_JV_UTILIZATION_AMPC_IRA Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `23`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C13-L161-CASE01-373220-LGES-Q1-2024-AMPC-CAPEX-CUT | None | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 372000.0 | None | None | 19.35 | None | stage2_captured_most_upside |
| C13-L161-CASE02-373220-LGES-Q2-2024-REVENUE-CUT-RESET | None | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13-L161-CASE03-373220-LGES-Q3-2024-IRA-OPTICAL-PROFIT | None | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 409000.0 | None | None | 6.48 | None | stage2_actionable_best_entry |
| C13-L161-CASE04-373220-LGES-Q1-2025-AMPC-ESS-RESET | None | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13-L161-CASE05-006400-SAMSUNGSDI-HUNGARY-UTILIZATION-2024 | None | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 372500.0 | None | None | 32.75 | None | stage2_actionable_best_entry |
| C13-L161-CASE06-006400-SAMSUNGSDI-STARPLUS-DOE-LOAN | None | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 259000.0 | None | None | 3.47 | None | stage2_captured_most_upside |
| C13-L161-CASE07-006400-SAMSUNGSDI-Q1-2025-LOSS-RESET | None | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | no_valid_stage_transition |
| C13-L191-001 | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 574000.0 | None | None | 8.01 | None | stage2_captured_most_upside |
| C13-L191-002 | 373220 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 467500.0 | None | None | 7.17 | None | stage2_captured_most_upside |
| C13-L191-003 | 051910 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | 504000.0 | None | None | no_valid_stage_transition |
| C13-L191-004 | 096770 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 182600.0 | None | None | 25.68 | None | stage2_actionable_best_entry |
| C13-L191-005 | 096770 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | 189500.0 | None | None | no_valid_stage_transition |
| C13-L191-006 | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 712000.0 | None | None | 3.23 | None | stage2_captured_most_upside |
| C13-L191-007 | 006400 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 452000.0 | None | None | 15.49 | None | stage2_actionable_best_entry |
| C13-L191-008 | 003670 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 380000.0 | None | None | 82.63 | None | stage2_actionable_best_entry |
| C13_R3_L100_011790_SKC_NORTHVOLT_COPPERFOIL | 011790 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 97300.0 | None | None | 25.6937 | None | stage2_actionable_best_entry |
| C13_R3_L100_014820_DONGWON_BATTERY_CAN_FACTORY | 014820 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 47150.0 | None | None | 25.5567 | None | stage2_captured_most_upside |
| C13_R3_L100_051910_LGCHEM_GM_TENNESSEE_CATHODE | 051910 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 470500.0 | None | None | 10.5207 | None | stage2_actionable_best_entry |
| C13_R3_L100_066970_LNF_SKON_SUPPLY_AMPC_PROXY | 066970 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 183100.0 | None | None | 6.0623 | None | stage2_actionable_best_entry |
| C13_R3_L100_078600_DAEJOO_SILICON_ANODE_CUSTOMER_PROXY | 078600 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 116700.0 | None | None | 3.6847 | None | stage2_captured_most_upside |
| C13_R3_L100_336370_SOLUS_CANADA_COPPERFOIL | 336370 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 11240.0 | None | None | 109.0747 | None | stage2_actionable_best_entry |
| C13_R3_L100_361610_SKIET_SEPARATOR_UTILIZATION_BREAK | 361610 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | None | None | None | 4c_too_late |
| C13_R3_L100_393890_WCP_SEPARATOR_COMPETITION_UTILIZATION | 393890 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | None | None | 34000.0 | None | None | no_valid_stage_transition |

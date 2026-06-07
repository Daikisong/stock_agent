# C01_ORDER_BACKLOG_MARGIN_BRIDGE Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `31`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C01_DAEWOOEANDC_047040_2024_03_06_CONSTRUCTION_BACKLOG_HEADLINE_MARGIN_FCF_FAIL | 047040 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 3860.0 | None | None | 28.63 | None | stage2_captured_most_upside |
| C01_DLEANDC_375500_2024_03_06_CONSTRUCTION_BACKLOG_MARGIN_FCF_FAIL | 375500 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 35300.0 | None | None | 7.08 | None | stage2_captured_most_upside |
| C01_GSENC_006360_2024_03_06_CONSTRUCTION_BACKLOG_HEADLINE_MARGIN_FCF_FAIL | 006360 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 15310.0 | None | None | 42.06 | None | stage2_captured_most_upside |
| C01_HANWHAOCEAN_042660_2024_03_06_SHIPBUILDING_DEFENSE_BACKLOG_MARGIN_RERATING | 042660 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 22300.0 | None | None | 58.3 | None | stage2_actionable_best_entry |
| C01_HDHYUNDAIELECTRIC_267260_2024_03_06_GRID_TRANSFORMER_BACKLOG_MARGIN_RERATING | 267260 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 136000.0 | None | None | 204.04 | None | stage2_actionable_best_entry |
| C01_HDI_042670_2024_02_02_EQUIPMENT_ORDER_CYCLE_FALSE_POSITIVE | 042670 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 8400.0 | None | None | 9.05 | None | stage2_captured_most_upside |
| C01_HDMIPO_010620_2024_03_06_SHIPBUILDING_BACKLOG_TURNAROUND_MARGIN_RERATING | 010620 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 61300.0 | None | None | 100.33 | None | stage2_actionable_best_entry |
| C01_HDMIPO_010620_2024_04_18_SHIPBUILDING_BACKLOG_MARGIN_BRIDGE | 010620 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 64900.0 | None | None | 89.21 | None | stage2_actionable_best_entry |
| C01_HHI_329180_2024_03_06_SHIPBUILDING_BACKLOG_MARGIN_BRIDGE_RERATING | 329180 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 111500.0 | None | None | 99.55 | None | stage2_actionable_best_entry |
| C01_HHI_329180_2024_04_18_SHIPBUILDING_BACKLOG_MARGIN_RERATING | 329180 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 120300.0 | None | None | 84.95 | None | stage2_actionable_best_entry |
| C01_HJSHIP_097230_2024_03_06_BACKLOG_HEADLINE_MARGIN_BRIDGE_FAIL | 097230 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 3405.0 | None | None | 11.16 | None | stage2_captured_most_upside |
| C01_HYOSUNGHEAVY_298040_2024_03_06_GRID_TRANSFORMER_BACKLOG_MARGIN_RERATING | 298040 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 232000.0 | None | None | 123.28 | None | stage2_actionable_best_entry |
| C01_HYUNDAIEANDC_000720_2024_03_06_CONSTRUCTION_BACKLOG_MARGIN_FCF_FAIL | 000720 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 33750.0 | None | None | 3.41 | None | stage2_captured_most_upside |
| C01_HYUNDAIROTEM_064350_2024_03_06_DEFENSE_RAIL_BACKLOG_MARGIN_RERATING | 064350 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 31950.0 | None | None | 117.53 | None | stage2_actionable_best_entry |
| C01_ILJINELECTRIC_103590_2024_03_06_GRID_CABLE_BACKLOG_MARGIN_RERATING | 103590 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 12930.0 | None | None | 133.57 | None | stage2_actionable_best_entry |
| C01_KSOE_009540_2024_03_06_SHIPBUILDING_BACKLOG_MARGIN_BRIDGE_RERATING | 009540 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 112400.0 | None | None | 89.5 | None | stage2_actionable_best_entry |
| C01_LIGNEX1_079550_2024_03_06_DEFENSE_BACKLOG_EXPORT_MARGIN_RERATING | 079550 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 168500.0 | None | None | 61.13 | None | stage2_actionable_best_entry |
| C01_LSELECTRIC_010120_2024_03_06_GRID_AUTOMATION_BACKLOG_MARGIN_RERATING | 010120 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 79100.0 | None | None | 247.03 | None | stage2_actionable_best_entry |
| C01_R1L100_010140_20240726 | 010140 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 11870.0 | None | None | 31.59 | None | stage2_captured_most_upside |
| C01_R1L100_010620_midsize_ship_backlog_margin_bridge | 010620 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 64900.0 | None | None | 61.17 | None | stage2_actionable_best_entry |
| C01_R1L100_042670_machinery_beta_no_backlog_margin_bridge | 042670 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| C01_R1L100_071970_20240424 | 071970 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 16500.0 | None | None | 78.18 | None | stage2_actionable_best_entry |
| C01_R1L100_071970_ship_engine_backlog_high_mae_success | 071970 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 13990.0 | None | None | 63.69 | None | stage2_actionable_best_entry |
| C01_R1L100_077970_20240424 | 077970 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 14860.0 | None | None | 71.94 | None | stage2_actionable_best_entry |
| C01_R1L100_329180_shipbuilding_backlog_margin_bridge | 329180 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 120300.0 | None | None | 84.95 | None | stage2_actionable_best_entry |
| C01_R1L93B_001440_TAIHAN_CABLE_MFE_DATAQUALITY | 001440 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| C01_R1L93B_006340_DAEWON_CABLE_BLOWOFF | 006340 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| C01_R1L93B_010120_LS_ELECTRIC_POWER_BACKLOG | 010120 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 63200.0 | None | None | 286.08 | None | stage2_actionable_best_entry |
| C01_R1L93_010620_HMD_FALSE_OVERBLOCK | 010620 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| C01_R1L93_097230_HJ_WEAK_BACKLOG_LATE_SPIKE | 097230 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| C01_R1L93_329180_HDHHI_SHIPBUILDING_BACKLOG | 329180 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 120300.0 | None | None | 148.55 | None | stage2_actionable_best_entry |

# C02_POWER_GRID_DATACENTER_CAPEX Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `54`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C02-214-001 | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | 123600.0 | None | None | 234.55 | None | stage2_actionable_best_entry |
| C02-214-002 | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 385000.0 | None | None | no_valid_stage_transition |
| C02-214-003 | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | 489500.0 | None | None | 407.25 | None | stage2_actionable_best_entry |
| C02-214-004 | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | 210500.0 | None | None | 44.18 | None | stage2_captured_most_upside |
| C02-214-005 | 103590 | C02_POWER_GRID_DATACENTER_CAPEX | 23550.0 | None | None | 88.54 | None | stage2_actionable_best_entry |
| C02-214-006 | 033100 | C02_POWER_GRID_DATACENTER_CAPEX | 31200.0 | None | None | 222.76 | None | stage2_actionable_best_entry |
| C02-214-007 | 009470 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 39700.0 | None | None | no_valid_stage_transition |
| C02-214-008 | 017040 | C02_POWER_GRID_DATACENTER_CAPEX | 2720.0 | None | None | 22.06 | None | stage2_captured_most_upside |
| C02-R1-L138-001440-20240920 | 001440 | C02_POWER_GRID_DATACENTER_CAPEX | 11700.0 | None | None | 49.15 | None | stage2_actionable_best_entry |
| C02-R1-L138-010120-20250423 | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | 180500.0 | None | None | 206.93 | None | stage2_actionable_best_entry |
| C02-R1-L138-017510-20240611 | 017510 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 5650.0 | None | None | no_valid_stage_transition |
| C02-R1-L138-189860-20250516 | 189860 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | None | None | None | no_valid_stage_transition |
| C02-R1-L138-229640-20250508 | 229640 | C02_POWER_GRID_DATACENTER_CAPEX | 33100.0 | None | None | 47.89 | None | stage2_actionable_best_entry |
| C02_001440_20241105_us_cable_long_supply_orders | 001440 | C02_POWER_GRID_DATACENTER_CAPEX | 11890.0 | None | None | 52.82 | None | stage2_actionable_best_entry |
| C02_006340_20240516_power_grid_theme_overhang_blowoff_counterexample | 006340 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 4910.0 | None | None | no_valid_stage_transition |
| C02_010120_20240701_us_growth_dc_power_equipment | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | 204500.0 | None | None | 48.41 | None | stage2_actionable_best_entry |
| C02_017040_20240408_eaton_legacy_switchgear_theme | 017040 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 2715.0 | None | None | 4b_too_early |
| C02_033100_20241204_distribution_transformer_competition_high_mae_counterexample | 033100 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 39600.0 | None | None | no_valid_stage_transition |
| C02_062040_20240729_transformer_ipo_ai_demand | 062040 | C02_POWER_GRID_DATACENTER_CAPEX | 50200.0 | None | None | 66.33 | None | stage2_actionable_best_entry |
| C02_103590_20250110_transformer_backlog_factory_expansion_high_mae_success | 103590 | C02_POWER_GRID_DATACENTER_CAPEX | 27850.0 | None | None | 59.43 | None | stage2_actionable_best_entry |
| C02_267260_20240517_power_equipment_mix_margin_bridge | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | None | None | None | no_valid_stage_transition |
| C02_298040_20250516_heavy_industry_power_grid_margin_step_up | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | None | None | None | no_valid_stage_transition |
| C02_388050_20240416_ai_distribution_board_datacenter_update | 388050 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 8590.0 | None | None | 4b_too_early |
| C02_R1L141_006910_POWER_INFRA_HVDC_THEME_NO_ORDER_MARGIN_BRIDGE_COUNTEREXAMPLE_20240520 | 006910 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 3915.0 | None | None | no_valid_stage_transition |
| C02_R1L141_017510_HVDC_TRANSMISSION_HARD_ORDER_HIGH_MAE_POSITIVE_20250113 | 017510 | C02_POWER_GRID_DATACENTER_CAPEX | 6580.0 | None | None | 94.83 | None | stage2_actionable_best_entry |
| C02_R1L141_042370_C02_C04_BOUNDARY_POWER_DISTRIBUTION_CONTRACT_HIGH_MAE_20250307 | 042370 | C02_POWER_GRID_DATACENTER_CAPEX | 8310.0 | None | None | 32.13 | None | stage2_actionable_best_entry |
| C02_R1L141_199820_EATON_SMART_BREAKER_DC_THEME_WITHOUT_ORDER_BRIDGE_4B_20240923 | 199820 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 9870.0 | None | None | no_valid_stage_transition |
| C02_R1L141_237750_DISTRIBUTION_AUTOMATION_GRID_IT_LOW_MAE_STAGE2_20250321 | 237750 | C02_POWER_GRID_DATACENTER_CAPEX | 3885.0 | None | None | 42.08 | None | stage2_actionable_best_entry |
| C02_R1L142_147830_C02_TRANSMISSION_DISTRIBUTION_MATERIALS_HIGH_MAE_WATCH_20240513 | 147830 | C02_POWER_GRID_DATACENTER_CAPEX | 6900.0 | None | None | 69.28 | None | stage2_actionable_best_entry |
| C02_R1L142_189860_C02_SWITCHGEAR_DATACENTER_DISTRIBUTION_PANEL_BOUNDARY_WATCH_20250515 | 189860 | C02_POWER_GRID_DATACENTER_CAPEX | 3975.0 | None | None | 30.06 | None | stage2_actionable_best_entry |
| C02_R1L142_229640_C02_CABLE_EXPORT_RESULT_LATE_CHASE_4B_COUNTEREXAMPLE_20250205 | 229640 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 44750.0 | None | None | no_valid_stage_transition |
| C02_R1L142_417200_C02_GRID_STABILITY_ULTRACAPACITOR_OPTIONALITY_4B_COUNTEREXAMPLE_20240415 | 417200 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 24200.0 | None | None | no_valid_stage_transition |
| C02_R1L142_453450_C02_GRID_TECH_IPO_DR_V2G_THEME_4B_COUNTEREXAMPLE_20240524 | 453450 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 49500.0 | None | None | no_valid_stage_transition |
| C02_R1L144_006340_C02_cable_grid_theme_event_premium_4b_counterexample_20240627 | 006340 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 4350.0 | None | None | no_valid_stage_transition |
| C02_R1L144_033100_C02_distribution_transformer_us_export_opm_positive_20240308 | 033100 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | None | None | None | no_valid_stage_transition |
| C02_R1L144_103590_C02_transformer_cable_backlog_factory_expansion_bridge_20240327 | 103590 | C02_POWER_GRID_DATACENTER_CAPEX | 20700.0 | None | None | 46.1353 | None | stage2_actionable_best_entry |
| C02_R1L144_267260_C02_transformer_backlog_margin_bridge_clean_positive_20240216 | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | None | 115900.0 | None | None | None | green_too_late |
| C02_R1L144_298040_C02_heavy_transformer_us_eu_backlog_margin_bridge_20241126 | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | None | None | None | no_valid_stage_transition |
| C02_R1_L125_006340_20240417_BLOCKDEAL_EARLY_WARNING_OVERLAY | 006340 | C02_POWER_GRID_DATACENTER_CAPEX | 2450.0 | None | None | 122.45 | None | stage2_captured_most_upside |
| C02_R1_L125_006340_20240516_POWER_SUPERCYCLE_BLOCKDEAL_COUNTER | 006340 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 4910.0 | None | None | no_valid_stage_transition |
| C02_R1_L125_024840_20240415_COPPER_AI_THEME_4B_COUNTER | 024840 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 2130.0 | None | None | no_valid_stage_transition |
| C02_R1_L125_267260_20240219_BACKLOG_CAPA_DATACENTER_POSITIVE | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | 123600.0 | None | None | 234.55 | None | stage2_actionable_best_entry |
| C02_R1_L125_298040_20250430_US_EU_ORDER_MARGIN_POSITIVE | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | 489500.0 | None | None | 407.25 | None | stage2_actionable_best_entry |
| C02_R1_L134_017040_20240801_GENERIC_POWER_SHORTAGE_COUNTER | 017040 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 2100.0 | None | None | no_valid_stage_transition |
| C02_R1_L134_033100_20240322_EXPORT_BACKLOG_MARGIN_POSITIVE | 033100 | C02_POWER_GRID_DATACENTER_CAPEX | 33100.0 | None | None | 204.23 | None | stage2_actionable_best_entry |
| C02_R1_L134_062040_20240729_IPO_BACKLOG_CAPA_HIGH_MAE | 062040 | C02_POWER_GRID_DATACENTER_CAPEX | 50200.0 | None | None | 66.33 | None | stage2_actionable_best_entry |
| C02_R1_L134_103590_20240322_HEAVY_ELECTRIC_ORDERBOOK_CAPEX_POSITIVE | 103590 | C02_POWER_GRID_DATACENTER_CAPEX | 19100.0 | None | None | 58.38 | None | stage2_actionable_best_entry |
| C02_R1_L134_147830_20240718_HVDC_POLICY_SPILLOVER_COUNTER | 147830 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 8820.0 | None | None | no_valid_stage_transition |
| C02_R1_L146_006260_20250117_LS_GRID_CAPEX_HOLDING_RERATING | 006260 | C02_POWER_GRID_DATACENTER_CAPEX | 117000.0 | None | None | 88.03 | None | stage2_actionable_best_entry |
| C02_R1_L146_060370_20240808_LS_MARINE_HVDC_INSTALLATION_CAPEX | 060370 | C02_POWER_GRID_DATACENTER_CAPEX | 16800.0 | None | None | 28.27 | None | stage2_captured_most_upside |
| C02_R1_L146_119850_20250407_GNC_DC_GENERATOR_CONTRACT | 119850 | C02_POWER_GRID_DATACENTER_CAPEX | 13750.0 | None | None | 240.0 | None | stage2_actionable_best_entry |
| C02_R1_L146_199820_20240923_CHEIL_EATON_SMART_BREAKER | 199820 | C02_POWER_GRID_DATACENTER_CAPEX | 9710.0 | None | None | 55.72 | None | stage2_actionable_best_entry |
| C02_R1_L146_237750_20240628_PNC_GOV_GRID_THEME | 237750 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 6130.0 | None | None | no_valid_stage_transition |
| C02_R1_L146_388050_20240502_G2POWER_TURNAROUND_REPORT | 388050 | C02_POWER_GRID_DATACENTER_CAPEX | 9080.0 | None | None | 40.31 | None | stage2_captured_most_upside |

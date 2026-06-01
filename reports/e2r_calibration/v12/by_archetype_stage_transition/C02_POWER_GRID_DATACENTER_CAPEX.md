# C02_POWER_GRID_DATACENTER_CAPEX Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `62`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 010120 | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 218000.0 | None | None | no_valid_stage_transition |
| 267260 | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | 229000.0 | None | None | 82.31 | None | stage2_actionable_best_entry |
| 298040 | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | 289000.0 | None | None | 69.55 | None | stage2_actionable_best_entry |
| C02_010120_LSELECTRIC_20240524_GRID_CAPEX_PRICE_PREMIUM_4B | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 231000.0 | None | None | no_valid_stage_transition |
| C02_010120_LSELECTRIC_20240724_GRID_EQUIPMENT_SECOND_WAVE_FALSE_GREEN | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | None | None | None | no_valid_stage_transition |
| C02_103590_ILJINELEC_20240529_TRANSFORMER_CABLE_FALSE_GREEN | 103590 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | None | None | None | no_valid_stage_transition |
| C02_103590_ILJINELEC_20240715_TRANSFORMER_CABLE_SECOND_WAVE_4B | 103590 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 29400.0 | None | None | no_valid_stage_transition |
| C02_267260_HDELECTRIC_20240123_TRANSFORMER_ORDERBOOK_STAGE2 | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | 100000.0 | None | None | 274.5 | None | stage2_actionable_best_entry |
| C02_267260_HDELECTRIC_20240724_TRANSFORMER_ORDERBOOK_SECOND_WAVE_4B | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 365500.0 | None | None | no_valid_stage_transition |
| C02_NO_REPEAT_001440_TAIHAN_CABLE_20240513_CABLE_THEME_HIGH_MAE | 001440 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | None | None | None | no_valid_stage_transition |
| C02_NO_REPEAT_010120_LS_ELECTRIC_20240305_GRID_DC_STAGE2 | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | 77800.0 | None | None | 252.8278 | None | stage2_actionable_best_entry |
| C02_NO_REPEAT_010120_LS_ELECTRIC_20240724_LOCAL_4B_PEAK | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 260000.0 | None | None | 4b_good_peak_capture |
| C02_NO_REPEAT_267260_HD_HYUNDAI_ELECTRIC_20230127_TRANSFORMER_STAGE2 | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | 38800.0 | None | None | 116.4948 | None | stage2_actionable_best_entry |
| R1L10_C02_010120_GRID_DATACENTER_HIGH_MAE_SUCCESS | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | 73500.0 | None | None | 273.47 | None | stage2_actionable_best_entry |
| R1L10_C02_010120_PRICE_ONLY_LOCAL_4B_TOO_EARLY | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 139700.0 | None | None | no_valid_stage_transition |
| R1L10_C02_267260_GRID_TRANSFORMER_SUCCESS | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | 85800.0 | None | None | 336.48 | None | stage2_actionable_best_entry |
| R1L10_C02_298040_GRID_HVDC_SUCCESS | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | 167900.0 | None | None | 179.33 | None | stage2_actionable_best_entry |
| R1L10_C02_HDHE_20230424 | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | 53000.0 | None | None | 81.89 | None | stage2_actionable_best_entry |
| R1L10_C02_HDHE_20240412_4B | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 235000.0 | None | None | no_valid_stage_transition |
| R1L10_C02_HYOSUNG_20230728 | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | 174500.0 | None | None | 104.58 | None | stage2_actionable_best_entry |
| R1L10_C02_KWANGMYUNG_20240507 | 017040 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | None | None | None | no_valid_stage_transition |
| R1L10_C02_LS_20240429 | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | 176600.0 | None | None | 55.44 | None | stage2_actionable_best_entry |
| R1L12_C02_DAEWON_006340_20240405 | 006340 | C02_POWER_GRID_DATACENTER_CAPEX | 2095.0 | None | 4885.0 | 160.1525 | 83.1546 | stage2_captured_most_upside |
| R1L12_C02_HDHE_267260_20240131 | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | 102700.0 | None | None | 264.65 | None | stage2_actionable_best_entry |
| R1L12_C02_HSHEAVY_298040_20240305 | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | 230000.0 | None | None | 103.91 | None | stage2_actionable_best_entry |
| R1L12_C02_LSE_010120_20240305 | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | 77800.0 | None | 231500.0 | 252.83 | 78.1386 | 4b_good_peak_capture |
| R1L13_C02_HDHE_PRICE_ONLY_4B_20240724 | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 365500.0 | None | None | no_valid_stage_transition |
| R1L13_C02_HDHE_STAGE2_20240103 | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | 85800.0 | None | None | 336.48 | None | stage2_actionable_best_entry |
| R1L13_C02_HYOSUNG_PRICE_ONLY_4B_20240528 | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 449500.0 | None | None | no_valid_stage_transition |
| R1L13_C02_HYOSUNG_STAGE2_20240103 | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | 167900.0 | None | None | 179.33 | None | stage2_actionable_best_entry |
| R1L13_C02_ILJIN_POST_CA_STAGE2_20240214 | 103590 | C02_POWER_GRID_DATACENTER_CAPEX | 11780.0 | None | None | 156.79 | None | stage2_actionable_best_entry |
| R1L13_C02_ILJIN_PRICE_ONLY_4B_20240529 | 103590 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 28600.0 | None | None | no_valid_stage_transition |
| R1L13_C02_LSE_PRICE_ONLY_4B_20240724 | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 260000.0 | None | None | no_valid_stage_transition |
| R1L13_C02_LSE_STAGE2_20240103 | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | 73500.0 | None | None | 273.47 | None | stage2_actionable_best_entry |
| R1L15_C02_DAEWON_20240513 | 006340 | C02_POWER_GRID_DATACENTER_CAPEX | None | 4885.0 | None | None | None | green_false_positive |
| R1L15_C02_HDHE_2024 | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | 85800.0 | None | None | 336.48 | None | stage2_actionable_best_entry |
| R1L15_C02_HYOSUNG_2024 | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | 167900.0 | None | None | 179.33 | None | stage2_actionable_best_entry |
| R1L15_C02_LSE_20240305 | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | 77800.0 | None | None | 213.62 | None | stage2_actionable_best_entry |
| R1L15_C02_LSE_20240524_LATEGREEN | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | None | 231000.0 | None | None | None | green_false_positive |
| R1L15_C02_LSE_20240717_4B | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | None | None | None | no_valid_stage_transition |
| R1L16_C02_DAEWONWIRE_20240510 | 006340 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | None | None | None | no_valid_stage_transition |
| R1L16_C02_HDHE_20240102 | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | 85800.0 | None | None | 336.48 | None | stage2_actionable_best_entry |
| R1L16_C02_HYOSUNGHI_20240102 | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | 167900.0 | None | None | 179.33 | None | stage2_actionable_best_entry |
| R1L16_C02_KWANGMYUNG_20240405 | 017040 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | None | None | None | no_valid_stage_transition |
| R1L1C02_HDHE_20230727 | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | 70600.0 | None | None | 218.7 | None | stage2_actionable_best_entry |
| R1L1C02_HDHE_20230727 | None | C02_POWER_GRID_DATACENTER_CAPEX | 70600.0 | None | None | 218.7 | None | stage2_actionable_best_entry |
| R1L1C02_LSE_20240701 | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | 204500.0 | None | None | 34.23 | None | stage2_actionable_best_entry |
| R1L1C02_LSE_20240701 | None | C02_POWER_GRID_DATACENTER_CAPEX | 204500.0 | None | None | 34.23 | None | stage2_actionable_best_entry |
| R1L1C02_LSE_20240723_4B | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 259000.0 | None | None | no_valid_stage_transition |
| R1L1C02_LSE_20240723_4B | None | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 259000.0 | None | None | 4b_too_early |
| R1L72-C02-010120-LS-ELECTRIC-US-DATACENTER-GROWTH-PRICE-ONLY-4B | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 218000.0 | None | None | no_valid_stage_transition |
| R1L72-C02-267260-HDHE-US-TRANSFORMER-BACKLOG-MARGIN-BRIDGE | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | 229000.0 | None | None | 82.31 | None | stage2_actionable_best_entry |
| R1L72-C02-298040-HYOSUNG-US-TRANSFORMER-HICO-BRIDGE | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | 289000.0 | None | None | 69.55 | None | stage2_actionable_best_entry |
| R1L76-C02-000500-GAON-CABLE-GRID-CAPEX-LIFECYCLE | 000500 | C02_POWER_GRID_DATACENTER_CAPEX | 21700.0 | None | None | 243.32 | None | stage2_actionable_best_entry |
| R1L76-C02-006340-DAEWON-CABLE-COPPER-GRID-THEME-FADE | 006340 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | None | None | None | no_valid_stage_transition |
| R1L76-C02-033100-JERYONG-TRANSFORMER-GRID-CAPEX-BACKLOG | 033100 | C02_POWER_GRID_DATACENTER_CAPEX | 21750.0 | None | None | 363.0 | None | stage2_actionable_best_entry |
| R1L78-C02-000500-GAON-CABLE-DATACENTER-GRID-CABLE-BACKLOG | 000500 | C02_POWER_GRID_DATACENTER_CAPEX | 22400.0 | None | None | 232.59 | None | stage2_actionable_best_entry |
| R1L78-C02-017040-KWANGMYUNG-ELECTRIC-SWITCHGEAR-THEME-FADE | 017040 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | None | None | None | no_valid_stage_transition |
| R1L78-C02-103590-ILJIN-ELECTRIC-POWER-CABLE-TRANSFORMER-POST-CA | 103590 | C02_POWER_GRID_DATACENTER_CAPEX | 11790.0 | None | None | 156.57 | None | stage2_actionable_best_entry |
| R1L80-C02-001440-DAEHAN-CABLE-POST-CA-GRID-CAPEX-BACKLOG | 001440 | C02_POWER_GRID_DATACENTER_CAPEX | 10830.0 | None | None | 93.44 | None | stage2_actionable_best_entry |
| R1L80-C02-189860-SEOJEON-ELECTRIC-SWITCHGEAR-THEME-BACKLOG-GAP | 189860 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | None | None | None | no_valid_stage_transition |
| R1L80-C02-199820-CHEIL-ELECTRIC-POST-CA-SWITCHGEAR-FADE | 199820 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | None | None | None | no_valid_stage_transition |

# C02_POWER_GRID_DATACENTER_CAPEX Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `24`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C02_R11L85_010120_LSELECTRIC_PRICE_ONLY_GRID_EXTENSION | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | None | None | None | no_valid_stage_transition |
| C02_R11L85_103590_ILJIN_WIRE_TRANSFORMER_BETA_EXTENSION | 103590 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | None | None | None | no_valid_stage_transition |
| C02_R11L85_267260_HDHE_TRANSFORMER_CAPEX_BRIDGE | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | 101200.0 | None | None | 308.6 | None | stage2_actionable_best_entry |
| C02_R11L89_006910_BOSUNG_POWER_POLICY_THEME | 006910 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | None | None | None | no_valid_stage_transition |
| C02_R11L89_199820_CHEIL_SWITCHGEAR_THEME | 199820 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | None | None | None | no_valid_stage_transition |
| C02_R11L89_229640_LS_ECO_POWER_CABLE_EXPORT_GRID_CAPEX | 229640 | C02_POWER_GRID_DATACENTER_CAPEX | 19600.0 | None | None | 131.12 | None | stage2_actionable_best_entry |
| C02_R1L88_147830_CHERYONG_LATE_GRID_EQUIPMENT_EXTENSION | 147830 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | None | None | None | no_valid_stage_transition |
| C02_R1L88_298040_HYOSUNG_HEAVY_TRANSFORMER_CAPEX | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | 222500.0 | None | None | 132.81 | None | stage2_actionable_best_entry |
| C02_R1L88_388050_G2POWER_GRID_THEME_NO_BRIDGE | 388050 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | None | None | None | no_valid_stage_transition |
| C02_R1L89_199820_20240628 | 199820 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | None | None | None | no_valid_stage_transition |
| C02_R1L89_267260_20240313 | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | None | None | None | no_valid_stage_transition |
| C02_R1L89_298040_20240304 | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | None | None | None | no_valid_stage_transition |
| C02_R1L94_103590_2024_02_26 | 103590 | C02_POWER_GRID_DATACENTER_CAPEX | 10820.0 | None | None | 179.6 | None | stage2_captured_most_upside |
| C02_R1L94_199820_2024_08_23 | 199820 | C02_POWER_GRID_DATACENTER_CAPEX | 7990.0 | None | None | 37.7 | None | stage2_actionable_best_entry |
| C02_R1L94_237750_2024_05_02 | 237750 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | None | None | None | no_valid_stage_transition |
| R1L89_C02_ILJIN_2024_GRID_CABLE_ORDER_MARGIN_POSITIVE | 103590 | C02_POWER_GRID_DATACENTER_CAPEX | 11780.0 | None | None | 156.79 | None | stage2_actionable_best_entry |
| R1L89_C02_JEIL_2024_BREAKER_EQUIPMENT_HIGH_MAE_FALSE_STAGE2 | 199820 | C02_POWER_GRID_DATACENTER_CAPEX | 10050.0 | None | None | 50.45 | None | stage2_actionable_best_entry |
| R1L89_C02_LSMARINE_2024_SUBSEA_CABLE_EVENT_CAP_4B | 060370 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 22700.0 | None | None | 4b_good_peak_capture |
| R1L91_C02_GNCENERGY_2024_BACKUP_POWER_THEME_HIGH_MAE_FALSE_STAGE2 | 119850 | C02_POWER_GRID_DATACENTER_CAPEX | 9950.0 | None | None | 88.64 | None | stage2_actionable_best_entry |
| R1L91_C02_HYOSUNGHEAVY_2024_TRANSFORMER_DATACENTER_CAPEX_POSITIVE | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | 186100.0 | None | None | 178.34 | None | stage2_actionable_best_entry |
| R1L91_C02_LSELECTRIC_2024_SWITCHGEAR_CAPEX_LOCAL_4B_TOO_EARLY | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 260000.0 | None | None | 4b_good_peak_capture |
| R1L95_C02_HDHYUNDAIELECTRIC_2024_TRANSFORMER_GRID_BACKLOG_DATACENTER_CAPEX_POSITIVE | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | 101200.0 | None | None | 270.06 | None | stage2_actionable_best_entry |
| R1L95_C02_PNCTECH_2024_GRID_AUTOMATION_CAPEX_FALSE_STAGE2 | 237750 | C02_POWER_GRID_DATACENTER_CAPEX | 6990.0 | None | None | 9.3 | None | stage2_actionable_best_entry |
| R1L95_C02_SEMYOUNGELECTRIC_2024_TRANSMISSION_FITTING_GRID_EVENT_CAP_4B | 017510 | C02_POWER_GRID_DATACENTER_CAPEX | None | None | 8780.0 | None | None | 4b_good_peak_capture |

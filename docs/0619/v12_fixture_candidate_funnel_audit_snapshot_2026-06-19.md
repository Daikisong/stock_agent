# V12 Fixture Candidate Funnel Audit

이 문서는 Green/guard fixture spec이 현재 runtime replay 후보까지 도달했는지 확인한다.
점수가 낮은 문제와 후보가 아예 없는 문제를 분리하기 위한 장부다.

## Summary

- spec_row_count: `60`
- runtime_discovered_candidate_count: `402`
- runtime_discovered_symbol_count: `12`
- fixture_funnel_status_counts: `{'exact_symbol_date_candidate_reached_runtime': 3, 'symbol_never_reached_current_runtime': 54, 'symbol_reached_runtime_but_not_fixture_date': 3}`
- funnel_root_cause_counts: `{'benchmark_universe_or_official_cheap_scan_funnel_gap': 54, 'candidate_reached_scoring_then_score_or_gate_decides': 3, 'monthly_schedule_or_fixture_date_mismatch': 3}`
- role_status_counts: `{'green:exact_symbol_date_candidate_reached_runtime': 3, 'green:symbol_never_reached_current_runtime': 25, 'green:symbol_reached_runtime_but_not_fixture_date': 2, 'guard:symbol_never_reached_current_runtime': 29, 'guard:symbol_reached_runtime_but_not_fixture_date': 1}`
- runtime_candidate_source_path_counts: `{'official_cheap_scan': 259, 'report_radar': 143}`
- replay_config_summary: `{'frequency': 'monthly', 'fixture_search': True, 'live_search': False, 'allow_snapshot_derived_universe': True, 'benchmark_label_path': 'data/benchmark_labels/e2r_known_winners.json', 'universe_count': {'min': 12, 'max': 13, 'latest': 13}, 'max_candidates_per_date': None, 'max_web_research_candidates_per_date': 0}`

## Fixture Rows

| role | archetype | fixture candidate | funnel status | symbol hits | nearest runtime rows | root cause |
| --- | --- | --- | --- | ---: | --- | --- |
| green | C02_POWER_GRID_DATACENTER_CAPEX | 267260 2024-02-16 C02_R1L144_267260_C02_transformer_backlog_margin_bridge_clean_positive_20240216 | exact_symbol_date_candidate_reached_runtime | 30 | 2024-02-16/1/14.1385/d0, 2024-02-21/1/14.1385/d5, 2024-02-07/1/14.1385/d9 | candidate_reached_scoring_then_score_or_gate_decides |
| green | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 000660 2024-04-25 C06_R2L108_000660_HBM3E_CUSTOMER_CAPACITY_SOLDOUT_20240425 | exact_symbol_date_candidate_reached_runtime | 46 | 2024-04-25/1/49.0179/d0, 2024-04-24/1/49.0179/d1, 2024-04-26/1/49.0179/d1 | candidate_reached_scoring_then_score_or_gate_decides |
| green | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 003230 2024-05-16 R13L41_C18_SAMYANG_003230_EXPORT_REORDER | exact_symbol_date_candidate_reached_runtime | 23 | 2024-05-16/1/40.5149/d0, 2024-05-21/1/40.5149/d5, 2024-06-01/1/40.5149/d16 | candidate_reached_scoring_then_score_or_gate_decides |
| green | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 010140 2025-02-06 C01-R1-L211-07 | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 103230 2024-05-16 C01_R1L214_005_103230_SNW_20240516_REPORT_BACKLOG_TEXT_FALSE_POSITIVE | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | C02_POWER_GRID_DATACENTER_CAPEX | 006340 2024-05-14 C02_006340_20240516_power_grid_theme_overhang_blowoff_counterexample | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| green | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 375500 2024-10-31 C05_L129_375500_20241031_STAGE3G | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 103230 2024-05-16 C05_R1L218_CASE003_103230_20240516 | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| green | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 131290 2024-04-26 R2L11_C08_131290_TSE_HBM_PROBE_CARD | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 098120 2024-04-26 C08_098120_MICROCONTACT_20240426_SECOND_WAVE_TEST_SOCKET_FALSE_GREEN | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| green | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 131290 2024-04-26 R2L14_C09_131290_TSE_LATE_GREEN_VALUATION_BLOWOFF | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 036930 2024-04-08 C09_036930_JUSUNG_20240408_DEPOSITION_EQUIPMENT_VALUATION_BLOWOFF | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| green | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 317330 2024-01-02 C10_L228_05_317330_ADVANCED_ELECTRONIC_MATERIALS_ROUTE_EARLY_RESET_WITH_STRONG_ASYMMETRY | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 089790 2024-07-22 C10_L232_08_089790 | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| green | C11_BATTERY_ORDERBOOK_RERATING | 121600 2023-02-09 C11_121600_NANOSINSO_20230209_CNT_ORDERBOOK_RERATING_GREEN | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | C11_BATTERY_ORDERBOOK_RERATING | 006110 2023-07-26 C11_006110_SAMAAL_20230726_ALUMINUMFOIL_ORDERBOOK_FALSE_GREEN | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| green | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 051490 2020-07-13 C13_R3L235_CASE006_051490 | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 006400 2023-04-25 C13_R3L190_006400_GM_JV_2023_LONG_LEAD_FALSE_POSITIVE | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| green | C15_MATERIAL_SPREAD_SUPERCYCLE | 298020 2021-01-14 C15_298020_HYOSUNG_TNC_20210114_SPANDEX_SPREAD_SUPERCYCLE | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | C15_MATERIAL_SPREAD_SUPERCYCLE | 004020 2024-02-07 C15_004020_20240207_STEEL_SPREAD_SUPERCYCLE_FALSE_POSITIVE | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| green | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 011780 2021-01-21 R4L11_C17_011780_KUMHO_NB_LATEX_SPREAD_SUPERCYCLE_20210121 | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 006650 2021-02-16 R4L11_C17_DAEHAN_NCC_SPREAD_FALSE_GREEN_2021 | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 097950 2024-05-16 R5L15-C18-097950-CJ-LEGACY-FOOD-FALSE-GREEN | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| green | C19_BRAND_RETAIL_INVENTORY_MARGIN | 036620 2024-05-21 R13L45_C19_036620_GAMSUNG_RETAIL_MARGIN_SUCCESS | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | C19_BRAND_RETAIL_INVENTORY_MARGIN | 383220 2023-05-16 R5L31_C19_FNF_20230516_CHINA_INVENTORY_FALSE_GREEN | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| green | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 192820 2025-02-24 C20-R5L135-02 | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 439090 2023-06-08 C20_R5L25_439090 | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| green | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 105560 2025-05-26 R13L22_C21_KBFG_105560_2025_CAPITAL_RETURN_CONFIRMED | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 323410 2024-02-26 R6L60_C21_KAKAOBANK_2024_POLICYONLY_COUNTEREXAMPLE | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| green | C22_INSURANCE_RATE_CYCLE_RESERVE | 032830 2024-02-21 R6L47_C22_032830_SAMSUNG_LIFE_VALUEUP_RESERVE_BRIDGE | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | C22_INSURANCE_RATE_CYCLE_RESERVE | 088350 2024-07-11 C22_088350_2024-07-11_Stage2-FalsePositive_life_insurance_valueup_label_without_reserve_capital_return_bridge | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| green | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 000100 2024-09-24 R7L10_C23_YUHAN_LAZCLUZE_FDA_20240821 | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 028300 2024-04-30 R7L10_C23_HLB_PRE_PDUFA_FALSE_GREEN_20240430 | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| green | C24_BIO_TRIAL_DATA_EVENT_RISK | 028300 2024-05-16 R7L12-C24-028300-HLB-BINARY-READOUT-REGULATORY-REUSE | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | C24_BIO_TRIAL_DATA_EVENT_RISK | 288330 2023-06-23 R7L15-C24-288330-BRIDGEBIO-BBT877-RESET-20230623 | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| green | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 335890 2023-01-13 C25_335890_VIOL_20230113_AESTHETIC_RF_EXPORT_CONSUMABLE_RERATING | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 145720 2024-02-29 C25_209_DENTIUM_4Q23_EXPORT_RECOVERY_FALSE_POSITIVE | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| green | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 067160 2021-07-27 C26_SOOP_2021_CREATOR_PLATFORM_OPERATING_LEVERAGE | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 035720 2021-06-24 R8L15_C26_KAKAO_2021_REG_CAP | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| green | C27_CONTENT_IP_GLOBAL_MONETIZATION | 194480 2021-01-21 C27_194480_DEVSISTERS_20210121_COOKIE_RUN_KINGDOM_GLOBAL_IP_RERATING | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | C27_CONTENT_IP_GLOBAL_MONETIZATION | 259960 2021-11-12 C27_259960_KRAFTON_20211112_GLOBAL_GAME_IP_RELEASE_FALSE_GREEN | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| green | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 058970 2023-03-15 C28_058970_EMRO_20230315_SCM_SAAS_CONTRACT_RERATING | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 030520 2024-01-10 R8L10_C28_CASE_003_HANCOM_2024_AI_OFFICE_FALSE_GREEN | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| green | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 000270 2023-04-26 R9L33-C29-000270-KIA-2023-FY22-VOLUME-MIX-MARGIN | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 011210 2024-01-26 R9L11_C29_011210_ENGINE_PARTS_FALSE_STAGE2 | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| green | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 000720 2021-05-27 R10L15_C30_000720_POS_20210405 | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 014790 2023-09-25 C30_014790_HLDNI_20230925_PF_BALANCE_SHEET_YELLOW_FALSE_GREEN | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| green | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 112610 2022-11-16 C31_112610_202208 | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 011930 2022-08-11 C31_011930_SHINSUNGENG_20220811_SOLAR_CLEANROOM_POLICY_FALSE_GREEN | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| green | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 010130 2024-09-13 | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 008930 2024-01-15 R13_C32_HANMI_008930_2024_OCI_FAMILY_CONTROL_DISPUTE | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| green | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 000100 2024-08-20 R13L11_XCASE__R7L11_C23_000100_YUHAN_LAZCLUZE_APPROVAL_COMMERCIALIZATION_20240820 | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 095340 2024-03-08 R13L11_XCASE__R2L11_C08_095340_ISC_SOCKET_BLOWOFF | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 090430 2021-05-12 R13L13_ACC_CASE_X07_090430_20210512 | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| green | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 373220 2024-10-28 R13-HMAE-L217-01-373220_20241029 | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 160980 2024-04-24 R13_HIGHMAE_C10_160980_20240425 | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 000100 2024-08-30 R13_STAGE2_FALSE_POSITIVE_L134_000100_2024-08-30_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | symbol_never_reached_current_runtime | 0 | none | benchmark_universe_or_official_cheap_scan_funnel_gap |
| guard | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 005930 2024-07-11 C06_005930_SAMSUNG_20240711_HBM_QUALIFICATION_LAG_FALSE_GREEN | symbol_reached_runtime_but_not_fixture_date | 21 | 2024-04-26/1/46.4468/d76, 2024-04-25/1/46.4468/d77, 2024-04-24/1/46.4468/d78 | monthly_schedule_or_fixture_date_mismatch |
| green | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 267260 2025-04-22 R13ATPV153_267260_HDHE_2025_ORDER_BACKLOG_EARNINGS_CONTROL | symbol_reached_runtime_but_not_fixture_date | 30 | 2024-06-01/1/14.1385/d325, 2024-05-21/1/14.1385/d336, 2024-05-16/1/14.1385/d341 | monthly_schedule_or_fixture_date_mismatch |
| green | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 267260 2025-04-22 R13SFP_267260_HDHE_ORDER_BACKLOG_CONTROL | symbol_reached_runtime_but_not_fixture_date | 30 | 2024-06-01/1/14.1385/d325, 2024-05-21/1/14.1385/d336, 2024-05-16/1/14.1385/d341 | monthly_schedule_or_fixture_date_mismatch |

## Easy Reading

- `exact_symbol_date_candidate_reached_runtime`: 그 fixture 날짜와 종목이 실제 점수 계산까지 갔다.
- `symbol_reached_runtime_but_not_fixture_date`: 종목은 후보가 됐지만, 연구 Green 날짜와 replay 날짜가 다르다.
- `symbol_never_reached_current_runtime`: current benchmark의 universe/cheap-scan 후보에 종목이 아예 없다.
- 쉬운 예: 하닉 `000660 2024-04-25`는 symbol은 있었지만 current benchmark는 월초 `2024-04-01/2024-05-01` 중심이라 exact fixture가 아니다.
- 쉬운 예: C21/C23/C28 주요 Green 후보는 symbol 자체가 current benchmark에 없어서 점수식을 테스트하지 못한다.

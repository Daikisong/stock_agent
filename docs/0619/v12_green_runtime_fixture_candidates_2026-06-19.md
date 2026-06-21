# V12 Green Runtime Fixture Candidates

이 보고서는 누적 연구 Green row를 runtime replay fixture로 고정하기 위한 후보 장부다.
여기 있는 후보는 production scoring 입력이 아니며, Green을 직접 만들지 않는다.

## Summary

- archetype_count: `36`
- green_archetype_count: `35`
- ready_archetype_count: `34`
- total_raw_stage3_green_rows: `381`
- total_green_rows: `327`
- total_clean_green_rows: `195`
- total_green_guard_marker_rows: `54`
- status_counts: `{'needs_green_row': 1, 'needs_verified_green_source': 1, 'ready_for_runtime_replay_fixture': 34}`
- ready_bridge_groups: `{'battery_mobility_contract_bridge': 5, 'bio_commercialization_reimbursement_bridge': 3, 'construction_pf_cash_bridge': 1, 'consumer_sellthrough_reorder_bridge': 3, 'cross_archetype_guard_bridge': 3, 'financial_capital_return_bridge': 1, 'governance_tender_cash_bridge': 1, 'industrial_backlog_margin_bridge': 4, 'insurance_reserve_capital_bridge': 1, 'materials_spread_supply_bridge': 3, 'policy_project_cash_bridge': 2, 'semiconductor_customer_capacity_bridge': 2, 'semiconductor_memory_recovery_bridge': 1, 'software_platform_recurring_revenue_bridge': 3, 'valuation_blowoff_guard_bridge': 1}`

`raw Stage3-Green`은 원본 trigger label 기준이고, `fixture Green`은 source-backed Stage3-Green 및 구조적 성공/too-late로 검증된 Green-equivalent 후보를 센다.
`fixture Green`에서도 `false_green`, `false_positive`, `policy_only`, `local_4B_watch` 같은 guard marker는 제외한다.
대표 fixture는 MFE가 가장 큰 row가 아니라 archetype/bridge primitive와 의미가 더 잘 맞는 row를 우선한다.

## Archetype Coverage

| archetype | bridge group | large sector | raw Green | fixture Green | clean Green | guard markers | guard | clean guard | status |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| C02_POWER_GRID_DATACENTER_CAPEX | industrial_backlog_margin_bridge | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 5 | 48 | 20 | -43 | 163 | 72 | ready_for_runtime_replay_fixture |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | financial_capital_return_bridge | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | 37 | 37 | 23 | 0 | 166 | 81 | ready_for_runtime_replay_fixture |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | bio_commercialization_reimbursement_bridge | L7_BIO_HEALTHCARE_MEDICAL | 30 | 27 | 15 | 3 | 147 | 81 | ready_for_runtime_replay_fixture |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | consumer_sellthrough_reorder_bridge | L5_CONSUMER_BRAND_DISTRIBUTION | 33 | 24 | 17 | 9 | 214 | 115 | ready_for_runtime_replay_fixture |
| C22_INSURANCE_RATE_CYCLE_RESERVE | insurance_reserve_capital_bridge | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | 28 | 23 | 13 | 5 | 180 | 87 | ready_for_runtime_replay_fixture |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | cross_archetype_guard_bridge | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 32 | 16 | 11 | 16 | 747 | 464 | ready_for_runtime_replay_fixture |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | software_platform_recurring_revenue_bridge | L8_PLATFORM_CONTENT_SW_SECURITY | 14 | 13 | 6 | 1 | 170 | 84 | ready_for_runtime_replay_fixture |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | software_platform_recurring_revenue_bridge | L8_PLATFORM_CONTENT_SW_SECURITY | 19 | 12 | 7 | 7 | 195 | 87 | ready_for_runtime_replay_fixture |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | policy_project_cash_bridge | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 12 | 11 | 3 | 1 | 284 | 161 | ready_for_runtime_replay_fixture |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | consumer_sellthrough_reorder_bridge | L5_CONSUMER_BRAND_DISTRIBUTION | 14 | 10 | 5 | 4 | 185 | 88 | ready_for_runtime_replay_fixture |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | software_platform_recurring_revenue_bridge | L8_PLATFORM_CONTENT_SW_SECURITY | 12 | 10 | 8 | 2 | 156 | 92 | ready_for_runtime_replay_fixture |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | semiconductor_customer_capacity_bridge | L2_AI_SEMICONDUCTOR_ELECTRONICS | 2 | 9 | 5 | -7 | 147 | 52 | ready_for_runtime_replay_fixture |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | materials_spread_supply_bridge | L4_MATERIALS_SPREAD_RESOURCE | 15 | 9 | 6 | 6 | 164 | 94 | ready_for_runtime_replay_fixture |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | bio_commercialization_reimbursement_bridge | L7_BIO_HEALTHCARE_MEDICAL | 12 | 9 | 7 | 3 | 152 | 77 | ready_for_runtime_replay_fixture |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | semiconductor_customer_capacity_bridge | L2_AI_SEMICONDUCTOR_ELECTRONICS | 9 | 8 | 5 | 1 | 134 | 65 | ready_for_runtime_replay_fixture |
| C24_BIO_TRIAL_DATA_EVENT_RISK | bio_commercialization_reimbursement_bridge | L7_BIO_HEALTHCARE_MEDICAL | 7 | 7 | 4 | 0 | 151 | 72 | ready_for_runtime_replay_fixture |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | industrial_backlog_margin_bridge | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 9 | 6 | 5 | 3 | 140 | 86 | ready_for_runtime_replay_fixture |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | industrial_backlog_margin_bridge | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 6 | 6 | 4 | 0 | 131 | 48 | ready_for_runtime_replay_fixture |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | industrial_backlog_margin_bridge | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 10 | 6 | 6 | 4 | 162 | 104 | ready_for_runtime_replay_fixture |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | battery_mobility_contract_bridge | L3_BATTERY_EV_GREEN_MOBILITY | 10 | 6 | 5 | 4 | 252 | 91 | ready_for_runtime_replay_fixture |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | battery_mobility_contract_bridge | L3_BATTERY_EV_GREEN_MOBILITY | 6 | 4 | 1 | 2 | 214 | 119 | ready_for_runtime_replay_fixture |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | cross_archetype_guard_bridge | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 8 | 4 | 2 | 4 | 402 | 324 | ready_for_runtime_replay_fixture |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | semiconductor_memory_recovery_bridge | L2_AI_SEMICONDUCTOR_ELECTRONICS | 4 | 3 | 3 | 1 | 220 | 148 | ready_for_runtime_replay_fixture |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | construction_pf_cash_bridge | L9_CONSTRUCTION_REALESTATE_HOUSING | 3 | 3 | 1 | 0 | 254 | 107 | ready_for_runtime_replay_fixture |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | policy_project_cash_bridge | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 0 | 2 | 2 | -2 | 134 | 67 | ready_for_runtime_replay_fixture |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | semiconductor_customer_capacity_bridge | L2_AI_SEMICONDUCTOR_ELECTRONICS | 10 | 2 | 0 | 8 | 152 | 61 | needs_verified_green_source |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | materials_spread_supply_bridge | L4_MATERIALS_SPREAD_RESOURCE | 0 | 2 | 2 | -2 | 125 | 77 | ready_for_runtime_replay_fixture |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | consumer_sellthrough_reorder_bridge | L5_CONSUMER_BRAND_DISTRIBUTION | 5 | 2 | 1 | 3 | 134 | 43 | ready_for_runtime_replay_fixture |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | cross_archetype_guard_bridge | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 5 | 2 | 2 | 3 | 369 | 222 | ready_for_runtime_replay_fixture |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | valuation_blowoff_guard_bridge | L2_AI_SEMICONDUCTOR_ELECTRONICS | 3 | 1 | 1 | 2 | 210 | 119 | ready_for_runtime_replay_fixture |
| C11_BATTERY_ORDERBOOK_RERATING | battery_mobility_contract_bridge | L3_BATTERY_EV_GREEN_MOBILITY | 2 | 1 | 1 | 1 | 190 | 95 | ready_for_runtime_replay_fixture |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | battery_mobility_contract_bridge | L3_BATTERY_EV_GREEN_MOBILITY | 0 | 1 | 1 | -1 | 188 | 106 | ready_for_runtime_replay_fixture |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | battery_mobility_contract_bridge | L3_BATTERY_EV_GREEN_MOBILITY | 1 | 1 | 1 | 0 | 243 | 140 | ready_for_runtime_replay_fixture |
| C15_MATERIAL_SPREAD_SUPERCYCLE | materials_spread_supply_bridge | L4_MATERIALS_SPREAD_RESOURCE | 12 | 1 | 1 | 11 | 214 | 130 | ready_for_runtime_replay_fixture |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | governance_tender_cash_bridge | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 1 | 1 | 1 | 0 | 242 | 130 | ready_for_runtime_replay_fixture |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | cross_archetype_guard_bridge | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 5 | 0 | 0 | 5 | 563 | 368 | needs_green_row |

## Replay Fixture Matrix

| archetype | Green fixture | guard fixture | expected runtime primitives | status |
| --- | --- | --- | --- | --- |
| C02_POWER_GRID_DATACENTER_CAPEX | 010120 2024-03-05 R1L12_C02_LSE_010120_20240305 | 006340 2024-06-27 C02_R1L144_006340_C02_cable_grid_theme_event_premium_4b_counterexample_20240627 | datacenter_customer, order_backlog_to_sales, lead_time_extended, capacity_constraint, pricing_power_confirmed | ready_for_runtime_replay_fixture |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 105560 2025-05-26 R13L22_C21_KBFG_105560_2025_CAPITAL_RETURN_CONFIRMED | 006220 2023-01-17 R6L14_C21_JEJUBANK_PRICEONLY_2023 | roe, pbr_e, treasury_share_cancellation, capital_return_execution, credit_cost_quality | ready_for_runtime_replay_fixture |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 000100 2024-09-24 R7L10_C23_YUHAN_LAZCLUZE_FDA_20240821 | 128940 2022-09-13 C23-R7L100-04 | regulatory_approval_confirmed, approval_to_revenue_bridge, royalty_route, partner_economics_visible, reimbursement_confirmed | ready_for_runtime_replay_fixture |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 192820 2025-02-24 C20-R5L135-02 | 362320 2023-01-19 R5L10_C20_362320_CHEONGDAM_GLOBAL_REOPENING_COUNTER_20230119 | export_growth_pct, platform_distribution_scale, brand_customer_diversification, repeat_order_confirmed, high_margin_mix_improvement | ready_for_runtime_replay_fixture |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 032830 2024-02-21 R6L47_C22_032830_SAMSUNG_LIFE_VALUEUP_RESERVE_BRIDGE | 088350 2024-07-11 C22_088350_2024-07-11_Stage2-FalsePositive_life_insurance_valueup_label_without_reserve_capital_return_bridge | csm_growth_visible, k_ics_ratio, reserve_quality_visible, loss_ratio_quality, capital_return_execution | ready_for_runtime_replay_fixture |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 000100 2024-08-20 R13L11_XCASE__R7L11_C23_000100_YUHAN_LAZCLUZE_APPROVAL_COMMERCIALIZATION_20240820 | 003230 2024-06-18 R13L10_CROSS_SAMYANG_003230_PRICE_ONLY_4B_TOO_EARLY | thesis_break_confirmed, contract_cancelled_or_delayed, revision_slowdown, accounting_trust_risk, valuation_overheat | ready_for_runtime_replay_fixture |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 058970 2023-03-15 C28_058970_EMRO_20230315_SCM_SAAS_CONTRACT_RERATING | 030520 2024-01-10 R8L10_C28_CASE_003_HANCOM_2024_AI_OFFICE_FALSE_GREEN | arr_growth_visible, nrr, retention_or_renewal, rpo_to_sales, recurring_margin_leverage | ready_for_runtime_replay_fixture |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 067160 2021-07-27 C26_SOOP_2021_CREATOR_PLATFORM_OPERATING_LEVERAGE | 035720 2021-06-24 R8L15_C26_KAKAO_2021_REG_CAP | arpu_growth_pct, ad_revenue_growth_pct, take_rate_improvement, operating_leverage_visible, regulatory_risk | ready_for_runtime_replay_fixture |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 112610 2022-11-16 C31_112610_202208 | 389260 2022-08-16 R11L15-C31-389260-IRA-DEVELOPER-HIGHMAE | policy_or_regulatory_confirmed, direct_company_cash_route, subsidy_capture_visible, implementation_timeline, policy_headline_only | ready_for_runtime_replay_fixture |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 003230 2024-05-16 R13L41_C18_SAMYANG_003230_EXPORT_REORDER | 017810 2024-06-28 C18_017810_PULMUONE_20240628_FROZEN_FOOD_EXPORT_CHANNEL_4B | export_growth_pct, sell_through_confirmed, repeat_order_confirmed, channel_reorder_confirmed, opm_expansion_pctp | ready_for_runtime_replay_fixture |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 194480 2021-01-21 C27_194480_DEVSISTERS_20210121_COOKIE_RUN_KINGDOM_GLOBAL_IP_RERATING | 253450 2021-11-19 C27_STUDIO_DRAGON_2021_OTT_NARRATIVE | ip_monetization_visible, global_launch_conversion, repeat_revenue, user_retention, token_or_theme_hype_risk | ready_for_runtime_replay_fixture |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 042700 2024-02-08 R2L12_C07_042700_HANMI_TCBONDER | 031980 2024-06-14 C07_031980_PSKH_20240614_HBM_PACKAGING_EQUIPMENT_PREMIUM_4B | hbm_customer_order, customer_contract_visible, equipment_order_backlog, advanced_packaging_bottleneck, relative_strength_score | ready_for_runtime_replay_fixture |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 011780 2021-01-21 R4L11_C17_011780_KUMHO_NB_LATEX_SPREAD_SUPERCYCLE_20210121 | 006650 2021-02-16 R4L11_C17_DAEHAN_NCC_SPREAD_FALSE_GREEN_2021 | spread_expansion, raw_material_cost_risk, utilization_rate, inventory_cycle, opm_expansion_pctp | ready_for_runtime_replay_fixture |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 335890 2023-01-13 C25_335890_VIOL_20230113_AESTHETIC_RF_EXPORT_CONSUMABLE_RERATING | 328130 2024-01-16 C25_209_LUNIT_SAMSUNG_DISTRIBUTION_HIGH_MAE | reimbursement_confirmed, procedure_volume_growth, export_growth_pct, consumable_repeat_revenue, gross_margin_bridge | ready_for_runtime_replay_fixture |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 000660 2024-04-25 C06_R2L108_000660_HBM3E_CUSTOMER_CAPACITY_SOLDOUT_20240425 | 000660 2024-07-11 C06_000660_SKHYNIX_20240711_HBM_CAPACITY_PRICE_PREMIUM_4B | customer_preorder_or_allocation, revenue_visibility_contract, hbm_capacity_constraint, hbm_capacity_pre_sold, memory_price_increase_mentioned | ready_for_runtime_replay_fixture |
| C24_BIO_TRIAL_DATA_EVENT_RISK | 039200 2024-02-20 R7L16_C24_POS_039200_20240220_CODEV_TRIAL_OPTION | 288330 2023-06-23 R7L15-C24-288330-BRIDGEBIO-BBT877-RESET-20230623 | trial_quality_visible, binary_event_unresolved, approval_not_confirmed, safety_signal, cash_runway_risk | ready_for_runtime_replay_fixture |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 010140 2025-02-06 C01-R1-L211-07 | 077970 2023-09-12 C01_R1L126_CASE_07_077970 | order_backlog_to_sales, named_customer_quality, contract_quality, delivery_schedule, opm_expansion_pctp | ready_for_runtime_replay_fixture |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 079550 2024-09-19 R1L13-C03-079550-LIG-IRAQ-MSAMI-20240919 | 272210 2022-07-29 C03_272210_HANWHASYSTEMS_20220729_DEFENSE_ELECTRONICS_EXPORT_FALSE_GREEN | export_contract, government_customer, order_backlog_to_sales, delivery_schedule, cost_overrun | ready_for_runtime_replay_fixture |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 375500 2024-10-31 C05_L129_375500_20241031_STAGE3G | 028050 2024-04-03 CASE_R1L127_C05_028050_20240403_FADHILI_CONTRACT_MARGIN_GAP | contract_amount_to_prior_sales, contract_duration_months, margin_bridge_visible, cost_overrun, delivery_schedule | ready_for_runtime_replay_fixture |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 000270 2023-04-26 R9L33-C29-000270-KIA-2023-FY22-VOLUME-MIX-MARGIN | 011210 2024-01-26 R9L11_C29_011210_ENGINE_PARTS_FALSE_STAGE2 | volume_growth_visible, mix_improvement, operating_leverage_visible, pricing_power_confirmed, fcf_quality_score | ready_for_runtime_replay_fixture |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 051490 2020-07-13 C13_R3L235_CASE006_051490 | 452400 2024-01-19 C13_L232_04_452400_IPO_BATTERY_SAFETY_PARTS_CUSTOMER_ROUTE_WITH_VALUATION_PHASE_TRAP | jv_utilization, ampc_or_subsidy_capture, ex_credit_margin, customer_contract, policy_reversal_risk | ready_for_runtime_replay_fixture |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 267260 2025-04-22 R13ATPV153_267260_HDHE_2025_ORDER_BACKLOG_EARNINGS_CONTROL | 001570 2024-03-05 R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_001570_2024-03-05_accounting_trust_v123 | auditor_or_disclosure_risk, restatement_risk, share_count_drift, price_only_blowoff, source_quality_conflict | ready_for_runtime_replay_fixture |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 317330 2024-01-02 C10_L228_05_317330_ADVANCED_ELECTRONIC_MATERIALS_ROUTE_EARLY_RESET_WITH_STRONG_ASYMMETRY | 033640 2024-05-20 C10_L229_05_033640_AI_ADVANCED_PACKAGING_POP_COMMERCIALIZATION_ROUTE_WITHOUT_REVENUE_CONVERSION | memory_price_increase_mentioned, supply_discipline_mentioned, cycle_demand_visibility, end_market_demand_visibility, supply_demand_tightness | ready_for_runtime_replay_fixture |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 000720 2021-05-27 R10L15_C30_000720_POS_20210405 | 004960 2023-09-15 C30_004960_HANSHIN_20230915_PF_CREDIT_PRICE_PREMIUM_4B | pf_exposure_reduced, balance_sheet_repair, cash_collection_visible, occupancy_or_presale_visible, funding_cost_risk | ready_for_runtime_replay_fixture |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 034020 2025-01-17 C04-142-CASE-01 | 189860 2024-07-18 C04_189860_SEOJEON_20240718_NUCLEAR_SWITCHGEAR_LEGAL_DELAY_4B | policy_or_regulatory_confirmed, project_award_confirmed, permit_or_legal_delay, direct_company_cash_route, cost_overrun | ready_for_runtime_replay_fixture |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 092870 2024-02-19 C08_R2L112_092870_20240219_STAGE3G_TEST_HANDLER_CUSTOMER_QUALITY_SUCCESS | 080580 2024-01-23 C08_080580_OKINS_20240123_TEST_SOCKET_PRICE_PREMIUM_4B | named_customer_quality, qualification_confirmed, repeat_order_confirmed, socket_or_test_demand_visible, margin_bridge_visible | needs_verified_green_source |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 010130 2024-08-07 C16_010130_20240807_Q2_MARGIN_BRIDGE | 000910 2023-07-04 R4L71_C16_000910_RARE_EARTH_POLICY_PRICE_ONLY_COUNTER | offtake_contract, supply_shortage, policy_supply_support, permit_status, direct_company_cash_route | ready_for_runtime_replay_fixture |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 337930 2024-08-09 R13L45_C19_337930_BRANDX_DTC_REORDER_SUCCESS_4B | 081660 2024-08-01 C19_081660_FILA_20240801_BRAND_INVENTORY_PRICE_PREMIUM_4B | inventory_spike, sell_through_confirmed, pricing_power_confirmed, channel_reorder_confirmed, raw_material_cost_risk | ready_for_runtime_replay_fixture |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 267260 2025-04-22 R13SFP_267260_HDHE_ORDER_BACKLOG_CONTROL | 000100 2024-08-30 R13_STAGE2_FALSE_POSITIVE_L134_000100_2024-08-30_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | price_only_blowoff, policy_headline_only, evidence_source_quality, missing_cashflow_bridge, theme_hype_without_revenue | ready_for_runtime_replay_fixture |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 131290 2024-04-26 R2L14_C09_131290_TSE_LATE_GREEN_VALUATION_BLOWOFF | 064760 2024-06-14 C09_064760_TCK_20240614_PARTS_VALUATION_BLOWOFF_4B | valuation_overheat, price_only_blowoff, order_to_revenue_bridge, customer_quality_visible, capex_cycle_risk | ready_for_runtime_replay_fixture |
| C11_BATTERY_ORDERBOOK_RERATING | 121600 2023-02-09 C11_121600_NANOSINSO_20230209_CNT_ORDERBOOK_RERATING_GREEN | 290670 2024-06-11 CASE_R3L130_C11_290670_20240611_06 | order_backlog_to_sales, customer_contract, call_off_risk, ex_credit_margin, fcf_quality_score | ready_for_runtime_replay_fixture |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 348370 2024-01-25 C12_R3_L106_348370_ENYCHEM_NORTH_AMERICA_ELECTROLYTE_CUSTOMER_SUPPLY_POSITIVE | 006110 2023-10-12 C12_006110_SAMAAL_20231012_ALUMINUMFOIL_CALLOFF_LATECYCLE_4C_WATCH | customer_contract, call_off_risk, customer_capex_decline, contract_cancelled_or_delayed, volume_visibility | ready_for_runtime_replay_fixture |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 078600 2024-04-02 C14_FU123_078600_20240402 | 003670 2024-01-23 C14_R3L127_003670_20240124 | ev_demand_slowdown, inventory_spike, price_cut_risk, customer_capex_decline, thesis_break_confirmed | ready_for_runtime_replay_fixture |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 298020 2021-01-14 C15_298020_HYOSUNG_TNC_20210114_SPANDEX_SPREAD_SUPERCYCLE | 018470 2021-07-13 R4L16_C15_018470_CHOIL_ALUMINUM_SUPERCYCLE_20210713 | spread_expansion, utilization_rate, inventory_cycle, pricing_power_confirmed, fcf_quality_score | ready_for_runtime_replay_fixture |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 010130 2024-09-13 | 008930 2024-01-15 C32_HANMI_2024_CONTROL_DISPUTE | tender_offer_confirmed, minority_cash_path, control_premium_floor, regulatory_approval_confirmed, event_spread_risk | ready_for_runtime_replay_fixture |

## Ready Examples

### C02_POWER_GRID_DATACENTER_CAPEX

- Bridge group: `industrial_backlog_margin_bridge`
- Expected runtime primitives: `datacenter_customer, order_backlog_to_sales, lead_time_extended, capacity_constraint, pricing_power_confirmed`
- Green candidate: `010120` `2024-03-05` `R1L12_C02_LSE_010120_20240305`
- Green evidence: Power-grid/datacenter CAPEX rerating route became tradable with order/backlog and relative-strength confirmation; margin bridge was visible but later Green confirmation lagged a large part of the move.
- Guard candidate: `006340` `2024-06-27` `C02_R1L144_006340_C02_cable_grid_theme_event_premium_4b_counterexample_20240627`
- Guard evidence: Mirae Asset AI-generated report dated 2024-06-27 summarized AI/datacenter power-management theme and cable-stock rally narratives, but without named order or margin bridge confirmation.

### C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN

- Bridge group: `financial_capital_return_bridge`
- Expected runtime primitives: `roe, pbr_e, treasury_share_cancellation, capital_return_execution, credit_cost_quality`
- Green candidate: `105560` `2025-05-26` `R13L22_C21_KBFG_105560_2025_CAPITAL_RETURN_CONFIRMED`
- Green evidence: Post-confirmation entry after stronger price/earnings confirmation; used as label comparison against the 2025-04-25 Stage2-Actionable entry.
- Guard candidate: `006220` `2023-01-17` `R6L14_C21_JEJUBANK_PRICEONLY_2023`
- Guard evidence: Price-only regional-bank/low-float financial theme. No verified capital-return, ROE/PBR, or shareholder-return evidence at trigger date.

### C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION

- Bridge group: `bio_commercialization_reimbursement_bridge`
- Expected runtime primitives: `regulatory_approval_confirmed, approval_to_revenue_bridge, royalty_route, partner_economics_visible, reimbursement_confirmed`
- Green candidate: `000100` `2024-09-24` `R7L10_C23_YUHAN_LAZCLUZE_FDA_20240821`
- Green evidence: FDA/J&J approval converted optionality into label-backed commercialization route; waiting for revision confirmation would enter after much of the first-leg MFE.
- Guard candidate: `128940` `2022-09-13` `C23-R7L100-04`
- Guard evidence: True

### C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION

- Bridge group: `consumer_sellthrough_reorder_bridge`
- Expected runtime primitives: `export_growth_pct, platform_distribution_scale, brand_customer_diversification, repeat_order_confirmed, high_margin_mix_improvement`
- Green candidate: `192820` `2025-02-24` `C20-R5L135-02`
- Green evidence: docs/round/achieve/achieve_v12/e2r_stock_web_v12_residual_round_R5_loop_135_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
- Guard candidate: `362320` `2023-01-19` `R5L10_C20_362320_CHEONGDAM_GLOBAL_REOPENING_COUNTER_20230119`
- Guard evidence: China/reopening/beauty-distribution story showed price response, but lacked multi-region reorder proof and margin/revision bridge.

### C22_INSURANCE_RATE_CYCLE_RESERVE

- Bridge group: `insurance_reserve_capital_bridge`
- Expected runtime primitives: `csm_growth_visible, k_ics_ratio, reserve_quality_visible, loss_ratio_quality, capital_return_execution`
- Green candidate: `032830` `2024-02-21` `R6L47_C22_032830_SAMSUNG_LIFE_VALUEUP_RESERVE_BRIDGE`
- Green evidence: Post-policy rerating had broadened into insurer-specific large-cap relative strength and capital-return/embedded-equity value interpretation.
- Guard candidate: `088350` `2024-07-11` `C22_088350_2024-07-11_Stage2-FalsePositive_life_insurance_valueup_label_without_reserve_capital_return_bridge`
- Guard evidence: life_insurance_valueup_label_without_reserve_quality_capital_return

### R13_CROSS_ARCHETYPE_4B_4C_REDTEAM

- Bridge group: `cross_archetype_guard_bridge`
- Expected runtime primitives: `thesis_break_confirmed, contract_cancelled_or_delayed, revision_slowdown, accounting_trust_risk, valuation_overheat`
- Green candidate: `000100` `2024-08-20` `R13L11_XCASE__R7L11_C23_000100_YUHAN_LAZCLUZE_APPROVAL_COMMERCIALIZATION_20240820`
- Green evidence: US FDA approval of the Rybrevant/Lazcluze combination created direct approval-to-commercialization evidence for the Korean originator/economics holder.
- Guard candidate: `003230` `2024-06-18` `R13L10_CROSS_SAMYANG_003230_PRICE_ONLY_4B_TOO_EARLY`
- Guard evidence: Price-only local high after explosive rerating; no non-price revision slowdown, channel saturation, or margin rollover evidence yet.

### C28_SOFTWARE_SECURITY_CONTRACT_RETENTION

- Bridge group: `software_platform_recurring_revenue_bridge`
- Expected runtime primitives: `arr_growth_visible, nrr, retention_or_renewal, rpo_to_sales, recurring_margin_leverage`
- Green candidate: `058970` `2023-03-15` `C28_058970_EMRO_20230315_SCM_SAAS_CONTRACT_RERATING`
- Green evidence: docs/round/achieve/achieve_v12/e2r_stock_web_v12_no_repeat_standalone_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_ai_office_security_contract_retention_2023_research.md
- Guard candidate: `030520` `2024-01-10` `R8L10_C28_CASE_003_HANCOM_2024_AI_OFFICE_FALSE_GREEN`
- Guard evidence: AI-office / platform option and sharp relative strength, but recurring enterprise retention and contract-quality proof was incomplete.

### C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE

- Bridge group: `software_platform_recurring_revenue_bridge`
- Expected runtime primitives: `arpu_growth_pct, ad_revenue_growth_pct, take_rate_improvement, operating_leverage_visible, regulatory_risk`
- Green candidate: `067160` `2021-07-27` `C26_SOOP_2021_CREATOR_PLATFORM_OPERATING_LEVERAGE`
- Green evidence: Later confirmed operating leverage and strong market reaction; used as Green lateness comparison.
- Guard candidate: `035720` `2021-06-24` `R8L15_C26_KAKAO_2021_REG_CAP`
- Guard evidence: Platform revenue growth and monetization momentum were visible, but valuation and take-rate/regulatory durability were already key red-team variables.

### C31_POLICY_SUBSIDY_LEGISLATION_EVENT

- Bridge group: `policy_project_cash_bridge`
- Expected runtime primitives: `policy_or_regulatory_confirmed, direct_company_cash_route, subsidy_capture_visible, implementation_timeline, policy_headline_only`
- Green candidate: `112610` `2022-11-16` `C31_112610_202208`
- Green evidence: Relative strength and policy-beneficiary discrimination after IRA; still requires company-level financial confirmation.
- Guard candidate: `389260` `2022-08-16` `R11L15-C31-389260-IRA-DEVELOPER-HIGHMAE`
- Guard evidence: IRA renewable subsidy event and local renewable developer optionality created fast repricing, but the forward path was price-volatility dominated and needed early 4B overlay.

### C18_CONSUMER_EXPORT_CHANNEL_REORDER

- Bridge group: `consumer_sellthrough_reorder_bridge`
- Expected runtime primitives: `export_growth_pct, sell_through_confirmed, repeat_order_confirmed, channel_reorder_confirmed, opm_expansion_pctp`
- Green candidate: `003230` `2024-05-16` `R13L41_C18_SAMYANG_003230_EXPORT_REORDER`
- Green evidence: Confirmed earnings/revision and margin bridge; price already far above Stage2 entry.
- Guard candidate: `017810` `2024-06-28` `C18_017810_PULMUONE_20240628_FROZEN_FOOD_EXPORT_CHANNEL_4B`
- Guard evidence: docs/round/achieve/achieve_v12/e2r_stock_web_v12_no_repeat_standalone_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_kfood_export_channel_reorder_2024_research.md

### C27_CONTENT_IP_GLOBAL_MONETIZATION

- Bridge group: `software_platform_recurring_revenue_bridge`
- Expected runtime primitives: `ip_monetization_visible, global_launch_conversion, repeat_revenue, user_retention, token_or_theme_hype_risk`
- Green candidate: `194480` `2021-01-21` `C27_194480_DEVSISTERS_20210121_COOKIE_RUN_KINGDOM_GLOBAL_IP_RERATING`
- Green evidence: docs/round/achieve/achieve_v12/e2r_stock_web_v12_no_repeat_standalone_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_game_ip_launch_monetization_2021_research.md
- Guard candidate: `253450` `2021-11-19` `C27_STUDIO_DRAGON_2021_OTT_NARRATIVE`
- Guard evidence: K-content/OTT narrative was highly visible after global Korean drama momentum, but margin bridge and owned-IP monetization visibility were weak.

### C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH

- Bridge group: `semiconductor_customer_capacity_bridge`
- Expected runtime primitives: `hbm_customer_order, customer_contract_visible, equipment_order_backlog, advanced_packaging_bottleneck, relative_strength_score, order_to_revenue_bridge`
- Green candidate: `042700` `2024-02-08` `R2L12_C07_042700_HANMI_TCBONDER`
- Green evidence: TC-bonder / HBM packaging equipment demand was already a public order-quality narrative. The price row shows the first decisive gap-up day; this trigger tests whether direct equipment route + relative strength deserved Yellow before strict Green confirmation.
- Guard candidate: `031980` `2024-06-14` `C07_031980_PSKH_20240614_HBM_PACKAGING_EQUIPMENT_PREMIUM_4B`
- Guard evidence: docs/round/achieve/achieve_v12/e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_di_yc_pskh_hbm_equipment_4b_2024_research.md

## How To Use

1. Ready archetype부터 Green/guard pair를 runtime replay fixture로 만든다.
2. Green pair는 source-backed primitive가 component/gate까지 올라오는지 검증한다.
3. Guard pair는 threshold 완화나 positive unlock 때문에 false positive가 열리지 않는지 검증한다.
4. 이 fixture를 통과하지 못하면 Green 기준을 낮추는 것이 아니라 parser/feature adapter/candidate funnel 중 어느 층이 끊겼는지 다시 본다.

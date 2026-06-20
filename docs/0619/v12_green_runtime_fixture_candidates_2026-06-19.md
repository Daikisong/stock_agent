# V12 Green Runtime Fixture Candidates

이 보고서는 누적 연구 Green row를 runtime replay fixture로 고정하기 위한 후보 장부다.
여기 있는 후보는 production scoring 입력이 아니며, Green을 직접 만들지 않는다.

## Summary

- archetype_count: `36`
- green_archetype_count: `33`
- ready_archetype_count: `30`
- total_raw_stage3_green_rows: `381`
- total_green_rows: `320`
- total_clean_green_rows: `206`
- total_green_guard_marker_rows: `61`
- status_counts: `{'needs_green_row': 3, 'needs_verified_green_source': 3, 'ready_for_runtime_replay_fixture': 30}`
- ready_bridge_groups: `{'battery_mobility_contract_bridge': 3, 'bio_commercialization_reimbursement_bridge': 3, 'construction_pf_cash_bridge': 1, 'consumer_sellthrough_reorder_bridge': 3, 'cross_archetype_guard_bridge': 4, 'financial_capital_return_bridge': 1, 'governance_tender_cash_bridge': 1, 'industrial_backlog_margin_bridge': 3, 'insurance_reserve_capital_bridge': 1, 'materials_spread_supply_bridge': 2, 'policy_project_cash_bridge': 1, 'semiconductor_customer_capacity_bridge': 2, 'semiconductor_memory_recovery_bridge': 1, 'software_platform_recurring_revenue_bridge': 3, 'valuation_blowoff_guard_bridge': 1}`

`raw Stage3-Green`은 원본 trigger label 기준이고, `fixture Green`은 `false_green`, `false_positive`, `policy_only` 같은 guard marker를 제외한 positive 후보만 센다.
대표 fixture는 MFE가 가장 큰 row가 아니라 archetype/bridge primitive와 의미가 더 잘 맞는 row를 우선한다.

## Archetype Coverage

| archetype | bridge group | large sector | raw Green | fixture Green | clean Green | guard markers | guard | clean guard | status |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | financial_capital_return_bridge | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | 37 | 37 | 23 | 0 | 139 | 65 | ready_for_runtime_replay_fixture |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | consumer_sellthrough_reorder_bridge | L5_CONSUMER_BRAND_DISTRIBUTION | 33 | 31 | 22 | 2 | 162 | 85 | ready_for_runtime_replay_fixture |
| C22_INSURANCE_RATE_CYCLE_RESERVE | insurance_reserve_capital_bridge | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | 28 | 25 | 15 | 3 | 142 | 59 | ready_for_runtime_replay_fixture |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | cross_archetype_guard_bridge | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 32 | 24 | 19 | 8 | 650 | 380 | ready_for_runtime_replay_fixture |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | bio_commercialization_reimbursement_bridge | L7_BIO_HEALTHCARE_MEDICAL | 30 | 22 | 16 | 8 | 122 | 59 | ready_for_runtime_replay_fixture |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | software_platform_recurring_revenue_bridge | L8_PLATFORM_CONTENT_SW_SECURITY | 19 | 17 | 11 | 2 | 163 | 74 | ready_for_runtime_replay_fixture |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | consumer_sellthrough_reorder_bridge | L5_CONSUMER_BRAND_DISTRIBUTION | 14 | 14 | 8 | 0 | 155 | 67 | ready_for_runtime_replay_fixture |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | software_platform_recurring_revenue_bridge | L8_PLATFORM_CONTENT_SW_SECURITY | 14 | 14 | 6 | 0 | 149 | 66 | ready_for_runtime_replay_fixture |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | policy_project_cash_bridge | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 12 | 12 | 4 | 0 | 232 | 123 | ready_for_runtime_replay_fixture |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | materials_spread_supply_bridge | L4_MATERIALS_SPREAD_RESOURCE | 15 | 11 | 8 | 4 | 134 | 74 | ready_for_runtime_replay_fixture |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | bio_commercialization_reimbursement_bridge | L7_BIO_HEALTHCARE_MEDICAL | 12 | 11 | 9 | 1 | 129 | 60 | ready_for_runtime_replay_fixture |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | software_platform_recurring_revenue_bridge | L8_PLATFORM_CONTENT_SW_SECURITY | 12 | 10 | 8 | 2 | 135 | 80 | ready_for_runtime_replay_fixture |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | industrial_backlog_margin_bridge | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 9 | 9 | 8 | 0 | 96 | 51 | ready_for_runtime_replay_fixture |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | industrial_backlog_margin_bridge | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 10 | 9 | 9 | 1 | 120 | 75 | ready_for_runtime_replay_fixture |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | semiconductor_customer_capacity_bridge | L2_AI_SEMICONDUCTOR_ELECTRONICS | 9 | 9 | 5 | 0 | 116 | 57 | ready_for_runtime_replay_fixture |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | battery_mobility_contract_bridge | L3_BATTERY_EV_GREEN_MOBILITY | 10 | 9 | 5 | 1 | 224 | 81 | ready_for_runtime_replay_fixture |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | semiconductor_customer_capacity_bridge | L2_AI_SEMICONDUCTOR_ELECTRONICS | 10 | 7 | 1 | 3 | 112 | 51 | ready_for_runtime_replay_fixture |
| C15_MATERIAL_SPREAD_SUPERCYCLE | materials_spread_supply_bridge | L4_MATERIALS_SPREAD_RESOURCE | 12 | 7 | 6 | 5 | 169 | 100 | ready_for_runtime_replay_fixture |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | industrial_backlog_margin_bridge | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 6 | 5 | 0 | 1 | 114 | 42 | needs_verified_green_source |
| C24_BIO_TRIAL_DATA_EVENT_RISK | bio_commercialization_reimbursement_bridge | L7_BIO_HEALTHCARE_MEDICAL | 7 | 5 | 2 | 2 | 111 | 56 | ready_for_runtime_replay_fixture |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | cross_archetype_guard_bridge | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 8 | 5 | 3 | 3 | 369 | 309 | ready_for_runtime_replay_fixture |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | semiconductor_memory_recovery_bridge | L2_AI_SEMICONDUCTOR_ELECTRONICS | 4 | 4 | 4 | 0 | 152 | 98 | ready_for_runtime_replay_fixture |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | battery_mobility_contract_bridge | L3_BATTERY_EV_GREEN_MOBILITY | 6 | 4 | 1 | 2 | 172 | 98 | ready_for_runtime_replay_fixture |
| C02_POWER_GRID_DATACENTER_CAPEX | industrial_backlog_margin_bridge | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 5 | 3 | 3 | 2 | 121 | 55 | ready_for_runtime_replay_fixture |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | consumer_sellthrough_reorder_bridge | L5_CONSUMER_BRAND_DISTRIBUTION | 5 | 3 | 2 | 2 | 112 | 37 | ready_for_runtime_replay_fixture |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | construction_pf_cash_bridge | L9_CONSTRUCTION_REALESTATE_HOUSING | 3 | 3 | 1 | 0 | 214 | 91 | ready_for_runtime_replay_fixture |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | valuation_blowoff_guard_bridge | L2_AI_SEMICONDUCTOR_ELECTRONICS | 3 | 2 | 1 | 1 | 187 | 104 | ready_for_runtime_replay_fixture |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | cross_archetype_guard_bridge | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 5 | 2 | 2 | 3 | 469 | 305 | ready_for_runtime_replay_fixture |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | cross_archetype_guard_bridge | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 5 | 2 | 2 | 3 | 304 | 194 | ready_for_runtime_replay_fixture |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | semiconductor_customer_capacity_bridge | L2_AI_SEMICONDUCTOR_ELECTRONICS | 2 | 1 | 0 | 1 | 136 | 45 | needs_verified_green_source |
| C11_BATTERY_ORDERBOOK_RERATING | battery_mobility_contract_bridge | L3_BATTERY_EV_GREEN_MOBILITY | 2 | 1 | 1 | 1 | 156 | 81 | ready_for_runtime_replay_fixture |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | battery_mobility_contract_bridge | L3_BATTERY_EV_GREEN_MOBILITY | 1 | 1 | 0 | 0 | 225 | 128 | needs_verified_green_source |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | governance_tender_cash_bridge | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 1 | 1 | 1 | 0 | 190 | 107 | ready_for_runtime_replay_fixture |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | policy_project_cash_bridge | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 0 | 0 | 0 | 0 | 120 | 56 | needs_green_row |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | battery_mobility_contract_bridge | L3_BATTERY_EV_GREEN_MOBILITY | 0 | 0 | 0 | 0 | 159 | 83 | needs_green_row |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | materials_spread_supply_bridge | L4_MATERIALS_SPREAD_RESOURCE | 0 | 0 | 0 | 0 | 112 | 65 | needs_green_row |

## Replay Fixture Matrix

| archetype | Green fixture | guard fixture | expected runtime primitives | status |
| --- | --- | --- | --- | --- |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 105560 2025-05-26 R13L22_C21_KBFG_105560_2025_CAPITAL_RETURN_CONFIRMED | 323410 2024-02-26 R6L60_C21_KAKAOBANK_2024_POLICYONLY_COUNTEREXAMPLE | roe, pbr_e, treasury_share_cancellation, capital_return_execution, credit_cost_quality | ready_for_runtime_replay_fixture |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 192820 2025-02-24 C20-R5L135-02 | 439090 2023-06-08 C20_R5L25_439090 | export_growth_pct, platform_distribution_scale, brand_customer_diversification, repeat_order_confirmed, high_margin_mix_improvement | ready_for_runtime_replay_fixture |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 032830 2024-02-21 R6L47_C22_032830_SAMSUNG_LIFE_VALUEUP_RESERVE_BRIDGE | 088350 2024-07-11 C22_088350_2024-07-11_Stage2-FalsePositive_life_insurance_valueup_label_without_reserve_capital_return_bridge | csm_growth_visible, k_ics_ratio, reserve_quality_visible, loss_ratio_quality, capital_return_execution | ready_for_runtime_replay_fixture |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 000100 2024-08-20 R13L11_XCASE__R7L11_C23_000100_YUHAN_LAZCLUZE_APPROVAL_COMMERCIALIZATION_20240820 | 095340 2024-03-08 R13L11_XCASE__R2L11_C08_095340_ISC_SOCKET_BLOWOFF | thesis_break_confirmed, contract_cancelled_or_delayed, revision_slowdown, accounting_trust_risk, valuation_overheat | ready_for_runtime_replay_fixture |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 000100 2024-09-24 R7L10_C23_YUHAN_LAZCLUZE_FDA_20240821 | 028300 2024-04-30 R7L10_C23_HLB_PRE_PDUFA_FALSE_GREEN_20240430 | regulatory_approval_confirmed, approval_to_revenue_bridge, royalty_route, partner_economics_visible, reimbursement_confirmed | ready_for_runtime_replay_fixture |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 067160 2021-07-27 C26_SOOP_2021_CREATOR_PLATFORM_OPERATING_LEVERAGE | 035720 2021-06-24 R8L15_C26_KAKAO_2021_REG_CAP | arpu_growth_pct, ad_revenue_growth_pct, take_rate_improvement, operating_leverage_visible, regulatory_risk | ready_for_runtime_replay_fixture |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 003230 2024-05-16 R13L41_C18_SAMYANG_003230_EXPORT_REORDER | 097950 2024-05-16 R5L15-C18-097950-CJ-LEGACY-FOOD-FALSE-GREEN | export_growth_pct, sell_through_confirmed, repeat_order_confirmed, channel_reorder_confirmed, opm_expansion_pctp | ready_for_runtime_replay_fixture |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 058970 2023-03-15 C28_058970_EMRO_20230315_SCM_SAAS_CONTRACT_RERATING | 030520 2024-01-10 R8L10_C28_CASE_003_HANCOM_2024_AI_OFFICE_FALSE_GREEN | arr_growth_visible, nrr, retention_or_renewal, rpo_to_sales, recurring_margin_leverage | ready_for_runtime_replay_fixture |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 112610 2022-11-16 C31_112610_202208 | 011930 2022-08-11 C31_011930_SHINSUNGENG_20220811_SOLAR_CLEANROOM_POLICY_FALSE_GREEN | policy_or_regulatory_confirmed, direct_company_cash_route, subsidy_capture_visible, implementation_timeline, policy_headline_only | ready_for_runtime_replay_fixture |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 011780 2021-01-21 R4L11_C17_011780_KUMHO_NB_LATEX_SPREAD_SUPERCYCLE_20210121 | 006650 2021-02-16 R4L11_C17_DAEHAN_NCC_SPREAD_FALSE_GREEN_2021 | spread_expansion, raw_material_cost_risk, utilization_rate, inventory_cycle, opm_expansion_pctp | ready_for_runtime_replay_fixture |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 335890 2023-01-13 C25_335890_VIOL_20230113_AESTHETIC_RF_EXPORT_CONSUMABLE_RERATING | 145720 2024-02-29 C25_209_DENTIUM_4Q23_EXPORT_RECOVERY_FALSE_POSITIVE | reimbursement_confirmed, procedure_volume_growth, export_growth_pct, consumable_repeat_revenue, gross_margin_bridge | ready_for_runtime_replay_fixture |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 194480 2021-01-21 C27_194480_DEVSISTERS_20210121_COOKIE_RUN_KINGDOM_GLOBAL_IP_RERATING | 259960 2021-11-12 C27_259960_KRAFTON_20211112_GLOBAL_GAME_IP_RELEASE_FALSE_GREEN | ip_monetization_visible, global_launch_conversion, repeat_revenue, user_retention, token_or_theme_hype_risk | ready_for_runtime_replay_fixture |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 010140 2025-02-06 C01-R1-L211-07 | 103230 2024-05-16 C01_R1L214_005_103230_SNW_20240516_REPORT_BACKLOG_TEXT_FALSE_POSITIVE | order_backlog_to_sales, named_customer_quality, contract_quality, delivery_schedule, opm_expansion_pctp | ready_for_runtime_replay_fixture |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 375500 2024-10-31 C05_L129_375500_20241031_STAGE3G | 103230 2024-05-16 C05_R1L218_CASE003_103230_20240516 | contract_amount_to_prior_sales, contract_duration_months, margin_bridge_visible, cost_overrun, delivery_schedule | ready_for_runtime_replay_fixture |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 000660 2024-04-25 C06_R2L108_000660_HBM3E_CUSTOMER_CAPACITY_SOLDOUT_20240425 | 005930 2024-07-11 C06_005930_SAMSUNG_20240711_HBM_QUALIFICATION_LAG_FALSE_GREEN | customer_preorder_or_allocation, revenue_visibility_contract, hbm_capacity_constraint, hbm_capacity_pre_sold, memory_price_increase_mentioned | ready_for_runtime_replay_fixture |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 000270 2023-04-26 R9L33-C29-000270-KIA-2023-FY22-VOLUME-MIX-MARGIN | 011210 2024-01-26 R9L11_C29_011210_ENGINE_PARTS_FALSE_STAGE2 | volume_growth_visible, mix_improvement, operating_leverage_visible, pricing_power_confirmed, fcf_quality_score | ready_for_runtime_replay_fixture |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 131290 2024-04-26 R2L11_C08_131290_TSE_HBM_PROBE_CARD | 098120 2024-04-26 C08_098120_MICROCONTACT_20240426_SECOND_WAVE_TEST_SOCKET_FALSE_GREEN | named_customer_quality, qualification_confirmed, repeat_order_confirmed, socket_or_test_demand_visible, margin_bridge_visible | ready_for_runtime_replay_fixture |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 298020 2021-01-14 C15_298020_HYOSUNG_TNC_20210114_SPANDEX_SPREAD_SUPERCYCLE | 004020 2024-02-07 C15_004020_20240207_STEEL_SPREAD_SUPERCYCLE_FALSE_POSITIVE | spread_expansion, utilization_rate, inventory_cycle, pricing_power_confirmed, fcf_quality_score | ready_for_runtime_replay_fixture |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 012450 2024-04-26 C03_R1L107_012450_20240426_STAGE3GREEN | 272210 2022-07-29 C03_272210_HANWHASYSTEMS_20220729_DEFENSE_ELECTRONICS_EXPORT_FALSE_GREEN | export_contract, government_customer, order_backlog_to_sales, delivery_schedule, cost_overrun | needs_verified_green_source |
| C24_BIO_TRIAL_DATA_EVENT_RISK | 028300 2024-05-16 R7L12-C24-028300-HLB-BINARY-READOUT-REGULATORY-REUSE | 288330 2023-06-23 R7L15-C24-288330-BRIDGEBIO-BBT877-RESET-20230623 | trial_quality_visible, binary_event_unresolved, approval_not_confirmed, safety_signal, cash_runway_risk | ready_for_runtime_replay_fixture |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 267260 2025-04-22 R13ATPV153_267260_HDHE_2025_ORDER_BACKLOG_EARNINGS_CONTROL | 090430 2021-05-12 R13L13_ACC_CASE_X07_090430_20210512 | auditor_or_disclosure_risk, restatement_risk, share_count_drift, price_only_blowoff, source_quality_conflict | ready_for_runtime_replay_fixture |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 317330 2024-01-02 C10_L228_05_317330_ADVANCED_ELECTRONIC_MATERIALS_ROUTE_EARLY_RESET_WITH_STRONG_ASYMMETRY | 089790 2024-07-22 C10_L232_08_089790 | memory_price_increase_mentioned, supply_discipline_mentioned, cycle_demand_visibility, end_market_demand_visibility, supply_demand_tightness | ready_for_runtime_replay_fixture |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 051490 2020-07-13 C13_R3L235_CASE006_051490 | 006400 2023-04-25 C13_R3L190_006400_GM_JV_2023_LONG_LEAD_FALSE_POSITIVE | jv_utilization, ampc_or_subsidy_capture, ex_credit_margin, customer_contract, policy_reversal_risk | ready_for_runtime_replay_fixture |
| C02_POWER_GRID_DATACENTER_CAPEX | 267260 2024-02-16 C02_R1L144_267260_C02_transformer_backlog_margin_bridge_clean_positive_20240216 | 006340 2024-05-14 C02_006340_20240516_power_grid_theme_overhang_blowoff_counterexample | datacenter_customer, order_backlog_to_sales, lead_time_extended, capacity_constraint, pricing_power_confirmed | ready_for_runtime_replay_fixture |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 036620 2024-05-21 R13L45_C19_036620_GAMSUNG_RETAIL_MARGIN_SUCCESS | 383220 2023-05-16 R5L31_C19_FNF_20230516_CHINA_INVENTORY_FALSE_GREEN | inventory_spike, sell_through_confirmed, pricing_power_confirmed, channel_reorder_confirmed, raw_material_cost_risk | ready_for_runtime_replay_fixture |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 000720 2021-05-27 R10L15_C30_000720_POS_20210405 | 014790 2023-09-25 C30_014790_HLDNI_20230925_PF_BALANCE_SHEET_YELLOW_FALSE_GREEN | pf_exposure_reduced, balance_sheet_repair, cash_collection_visible, occupancy_or_presale_visible, funding_cost_risk | ready_for_runtime_replay_fixture |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 131290 2024-04-26 R2L14_C09_131290_TSE_LATE_GREEN_VALUATION_BLOWOFF | 036930 2024-04-08 C09_036930_JUSUNG_20240408_DEPOSITION_EQUIPMENT_VALUATION_BLOWOFF | valuation_overheat, price_only_blowoff, order_to_revenue_bridge, customer_quality_visible, capex_cycle_risk | ready_for_runtime_replay_fixture |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 373220 2024-10-28 R13-HMAE-L217-01-373220_20241029 | 160980 2024-04-24 R13_HIGHMAE_C10_160980_20240425 | high_mae_history, valuation_overheat, liquidity_or_microcap_risk, execution_risk_score, positioning_reversal_risk | ready_for_runtime_replay_fixture |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 267260 2025-04-22 R13SFP_267260_HDHE_ORDER_BACKLOG_CONTROL | 000100 2024-08-30 R13_STAGE2_FALSE_POSITIVE_L134_000100_2024-08-30_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | price_only_blowoff, policy_headline_only, evidence_source_quality, missing_cashflow_bridge, theme_hype_without_revenue | ready_for_runtime_replay_fixture |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 042700 2024-03-28 R13L12_C07_HANMI_042700 | 031980 2024-06-14 C07_031980_PSKH_20240614_HBM_PACKAGING_EQUIPMENT_PREMIUM_4B | hbm_customer_order, customer_contract_visible, equipment_order_backlog, advanced_packaging_bottleneck, relative_strength_score | needs_verified_green_source |
| C11_BATTERY_ORDERBOOK_RERATING | 121600 2023-02-09 C11_121600_NANOSINSO_20230209_CNT_ORDERBOOK_RERATING_GREEN | 006110 2023-07-26 C11_006110_SAMAAL_20230726_ALUMINUMFOIL_ORDERBOOK_FALSE_GREEN | order_backlog_to_sales, customer_contract, call_off_risk, ex_credit_margin, fcf_quality_score | ready_for_runtime_replay_fixture |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 078600 2024-03-21 C14_R3L108_078600_20240321_STAGE3GREEN | 003670 2024-04-24 C14_R3_L95_003670_20240425 | ev_demand_slowdown, inventory_spike, price_cut_risk, customer_capex_decline, thesis_break_confirmed | needs_verified_green_source |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 010130 2024-09-13 | 008930 2024-01-15 R13_C32_HANMI_008930_2024_OCI_FAMILY_CONTROL_DISPUTE | tender_offer_confirmed, minority_cash_path, control_premium_floor, regulatory_approval_confirmed, event_spread_risk | ready_for_runtime_replay_fixture |

## Ready Examples

### C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN

- Bridge group: `financial_capital_return_bridge`
- Expected runtime primitives: `roe, pbr_e, treasury_share_cancellation, capital_return_execution, credit_cost_quality`
- Green candidate: `105560` `2025-05-26` `R13L22_C21_KBFG_105560_2025_CAPITAL_RETURN_CONFIRMED`
- Green evidence: Post-confirmation entry after stronger price/earnings confirmation; used as label comparison against the 2025-04-25 Stage2-Actionable entry.
- Guard candidate: `323410` `2024-02-26` `R6L60_C21_KAKAOBANK_2024_POLICYONLY_COUNTEREXAMPLE`
- Guard evidence: Policy/value-up narrative applied to financial names, but company-specific capital return and ROE-to-PBR bridge were not confirmed.

### C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION

- Bridge group: `consumer_sellthrough_reorder_bridge`
- Expected runtime primitives: `export_growth_pct, platform_distribution_scale, brand_customer_diversification, repeat_order_confirmed, high_margin_mix_improvement`
- Green candidate: `192820` `2025-02-24` `C20-R5L135-02`
- Green evidence: docs/round/achieve/achieve_v12/e2r_stock_web_v12_residual_round_R5_loop_135_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
- Guard candidate: `439090` `2023-06-08` `C20_R5L25_439090`
- Guard evidence: new listing and global K-beauty brand narrative; no repeat-order confirmation on trigger date

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
- Guard candidate: `095340` `2024-03-08` `R13L11_XCASE__R2L11_C08_095340_ISC_SOCKET_BLOWOFF`
- Guard evidence: HBM/test-socket narrative and sharp relative strength, but insufficient fresh customer mix/revision bridge; valuation/positioning risk dominated.

### C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION

- Bridge group: `bio_commercialization_reimbursement_bridge`
- Expected runtime primitives: `regulatory_approval_confirmed, approval_to_revenue_bridge, royalty_route, partner_economics_visible, reimbursement_confirmed`
- Green candidate: `000100` `2024-09-24` `R7L10_C23_YUHAN_LAZCLUZE_FDA_20240821`
- Green evidence: FDA/J&J approval converted optionality into label-backed commercialization route; waiting for revision confirmation would enter after much of the first-leg MFE.
- Guard candidate: `028300` `2024-04-30` `R7L10_C23_HLB_PRE_PDUFA_FALSE_GREEN_20240430`
- Guard evidence: Pre-PDUFA optionality and relative strength should not be allowed to become Green before label approval and commercialization economics are public.

### C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE

- Bridge group: `software_platform_recurring_revenue_bridge`
- Expected runtime primitives: `arpu_growth_pct, ad_revenue_growth_pct, take_rate_improvement, operating_leverage_visible, regulatory_risk`
- Green candidate: `067160` `2021-07-27` `C26_SOOP_2021_CREATOR_PLATFORM_OPERATING_LEVERAGE`
- Green evidence: Later confirmed operating leverage and strong market reaction; used as Green lateness comparison.
- Guard candidate: `035720` `2021-06-24` `R8L15_C26_KAKAO_2021_REG_CAP`
- Guard evidence: Platform revenue growth and monetization momentum were visible, but valuation and take-rate/regulatory durability were already key red-team variables.

### C18_CONSUMER_EXPORT_CHANNEL_REORDER

- Bridge group: `consumer_sellthrough_reorder_bridge`
- Expected runtime primitives: `export_growth_pct, sell_through_confirmed, repeat_order_confirmed, channel_reorder_confirmed, opm_expansion_pctp`
- Green candidate: `003230` `2024-05-16` `R13L41_C18_SAMYANG_003230_EXPORT_REORDER`
- Green evidence: Confirmed earnings/revision and margin bridge; price already far above Stage2 entry.
- Guard candidate: `097950` `2024-05-16` `R5L15-C18-097950-CJ-LEGACY-FOOD-FALSE-GREEN`
- Guard evidence: K-food/global brand distribution narrative and early result improvement visible, but channel reorder was not cleanly separable from legacy food, commodity, and base effects.

### C28_SOFTWARE_SECURITY_CONTRACT_RETENTION

- Bridge group: `software_platform_recurring_revenue_bridge`
- Expected runtime primitives: `arr_growth_visible, nrr, retention_or_renewal, rpo_to_sales, recurring_margin_leverage`
- Green candidate: `058970` `2023-03-15` `C28_058970_EMRO_20230315_SCM_SAAS_CONTRACT_RERATING`
- Green evidence: docs/round/achieve/achieve_v12/e2r_stock_web_v12_no_repeat_standalone_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_ai_office_security_contract_retention_2023_research.md
- Guard candidate: `030520` `2024-01-10` `R8L10_C28_CASE_003_HANCOM_2024_AI_OFFICE_FALSE_GREEN`
- Guard evidence: AI-office / platform option and sharp relative strength, but recurring enterprise retention and contract-quality proof was incomplete.

### C31_POLICY_SUBSIDY_LEGISLATION_EVENT

- Bridge group: `policy_project_cash_bridge`
- Expected runtime primitives: `policy_or_regulatory_confirmed, direct_company_cash_route, subsidy_capture_visible, implementation_timeline, policy_headline_only`
- Green candidate: `112610` `2022-11-16` `C31_112610_202208`
- Green evidence: Relative strength and policy-beneficiary discrimination after IRA; still requires company-level financial confirmation.
- Guard candidate: `011930` `2022-08-11` `C31_011930_SHINSUNGENG_20220811_SOLAR_CLEANROOM_POLICY_FALSE_GREEN`
- Guard evidence: docs/round/achieve/achieve_v12/e2r_stock_web_v12_no_repeat_standalone_L10_POLICY_SUBSIDY_GOVERNANCE_EVENT_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_ira_solar_manufacturing_tax_credit_4b_2022_research.md

### C17_CHEMICAL_COMMODITY_MARGIN_SPREAD

- Bridge group: `materials_spread_supply_bridge`
- Expected runtime primitives: `spread_expansion, raw_material_cost_risk, utilization_rate, inventory_cycle, opm_expansion_pctp`
- Green candidate: `011780` `2021-01-21` `R4L11_C17_011780_KUMHO_NB_LATEX_SPREAD_SUPERCYCLE_20210121`
- Green evidence: NB latex/synthetic rubber spread expansion, utilization pressure, and early revision bridge had become visible in the 2020-2021 chemical upcycle.
- Guard candidate: `006650` `2021-02-16` `R4L11_C17_DAEHAN_NCC_SPREAD_FALSE_GREEN_2021`
- Guard evidence: NCC spread recovery plus abrupt price/volume looked like Green, but the company had a commodity-only spread exposure without durable specialty-margin or customer-quality evidence; the entry was effectively at local spread-cycle exhaustion.

### C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT

- Bridge group: `bio_commercialization_reimbursement_bridge`
- Expected runtime primitives: `reimbursement_confirmed, procedure_volume_growth, export_growth_pct, consumable_repeat_revenue, gross_margin_bridge`
- Green candidate: `335890` `2023-01-13` `C25_335890_VIOL_20230113_AESTHETIC_RF_EXPORT_CONSUMABLE_RERATING`
- Green evidence: docs/round/achieve/achieve_v12/e2r_stock_web_v12_no_repeat_standalone_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_aesthetic_device_export_2023_research.md
- Guard candidate: `145720` `2024-02-29` `C25_209_DENTIUM_4Q23_EXPORT_RECOVERY_FALSE_POSITIVE`
- Guard evidence: Dentium 4Q23 looked strong on revenue/OP and export recovery, but dental implant export recovery still carried China/VBP and digital-dentistry quality risk.

### C27_CONTENT_IP_GLOBAL_MONETIZATION

- Bridge group: `software_platform_recurring_revenue_bridge`
- Expected runtime primitives: `ip_monetization_visible, global_launch_conversion, repeat_revenue, user_retention, token_or_theme_hype_risk`
- Green candidate: `194480` `2021-01-21` `C27_194480_DEVSISTERS_20210121_COOKIE_RUN_KINGDOM_GLOBAL_IP_RERATING`
- Green evidence: docs/round/achieve/achieve_v12/e2r_stock_web_v12_no_repeat_standalone_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_game_ip_launch_monetization_2021_research.md
- Guard candidate: `259960` `2021-11-12` `C27_259960_KRAFTON_20211112_GLOBAL_GAME_IP_RELEASE_FALSE_GREEN`
- Guard evidence: docs/round/achieve/achieve_v12/e2r_stock_web_v12_no_repeat_standalone_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_game_ip_launch_nft_retention_2021_2022_research.md

## How To Use

1. Ready archetype부터 Green/guard pair를 runtime replay fixture로 만든다.
2. Green pair는 source-backed primitive가 component/gate까지 올라오는지 검증한다.
3. Guard pair는 threshold 완화나 positive unlock 때문에 false positive가 열리지 않는지 검증한다.
4. 이 fixture를 통과하지 못하면 Green 기준을 낮추는 것이 아니라 parser/feature adapter/candidate funnel 중 어느 층이 끊겼는지 다시 본다.

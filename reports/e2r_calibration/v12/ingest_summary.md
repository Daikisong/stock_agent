# V12 Residual Calibration Ingest Summary

v12는 rolling calibration 입력입니다. `run-v12-calibration`은 검증된 apply_next_patch를 기본 profile에 반영합니다.
`run-v12-full`은 진단/감사용 ingest이며 active profile을 바꾸지 않습니다.
case_fixture나 과거 연구 재현 성공은 live discovery 증명이 아닙니다.
source proxy 또는 evidence URL 한계는 promotion blocker로 보고서에 남깁니다.

- md_input_root: `docs/round`
- include_archive: `True`
- v12_result_md_count: `2260`
- v12_parsed_document_count: `2260`
- v12_failed_document_count: `0`
- v12_raw_trigger_rows: `18736`
- v12_validated_trigger_rows: `13720`
- v12_representative_trigger_rows: `12453`
- v12_rejected_rows: `8177`
- v12_raw_aggregate_metric_rows: `949`
- v12_raw_shadow_weight_rows: `3740`
- large_sectors_covered: `['L10_POLICY_EVENT_CROSS_REDTEAM_MISC', 'L1_INDUSTRIALS_INFRA_DEFENSE_GRID', 'L2_AI_SEMICONDUCTOR_ELECTRONICS', 'L3_BATTERY_EV_GREEN_MOBILITY', 'L4_MATERIALS_SPREAD_RESOURCE', 'L5_CONSUMER_BRAND_DISTRIBUTION', 'L6_FINANCIAL_CAPITAL_RETURN_DIGITAL', 'L7_BIO_HEALTHCARE_MEDICAL', 'L8_PLATFORM_CONTENT_SW_SECURITY', 'L9_CONSTRUCTION_REALESTATE_HOUSING']`
- canonical_archetypes_covered: `['C01_ORDER_BACKLOG_MARGIN_BRIDGE', 'C02_POWER_GRID_DATACENTER_CAPEX', 'C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG', 'C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY', 'C05_EPC_MEGA_CONTRACT_MARGIN_GAP', 'C06_HBM_MEMORY_CUSTOMER_CAPACITY', 'C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH', 'C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY', 'C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF', 'C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE', 'C11_BATTERY_ORDERBOOK_RERATING', 'C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK', 'C13_BATTERY_JV_UTILIZATION_AMPC_IRA', 'C14_EV_DEMAND_SLOWDOWN_4B_4C', 'C15_MATERIAL_SPREAD_SUPERCYCLE', 'C16_STRATEGIC_RESOURCE_POLICY_SUPPLY', 'C17_CHEMICAL_COMMODITY_MARGIN_SPREAD', 'C18_CONSUMER_EXPORT_CHANNEL_REORDER', 'C19_BRAND_RETAIL_INVENTORY_MARGIN', 'C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION', 'C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN', 'C22_INSURANCE_RATE_CYCLE_RESERVE', 'C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION', 'C24_BIO_TRIAL_DATA_EVENT_RISK', 'C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT', 'C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE', 'C27_CONTENT_IP_GLOBAL_MONETIZATION', 'C28_SOFTWARE_SECURITY_CONTRACT_RETENTION', 'C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE', 'C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK', 'C31_POLICY_SUBSIDY_LEGISLATION_EVENT', 'C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP', 'R13_CROSS_ARCHETYPE_4B_4C_REDTEAM', 'R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION', 'R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL', 'R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW']`
- stage_transition_summary_rows: `10645`
- evidence_url_pending_count: `4188`
- source_proxy_only_count: `5118`
- active_default_profile_preserved: `True`
- production_default_scoring_changed: `False`
- archetype_weight_profile_path: `None`
- archetype_weight_report_path: `None`
- archetype_weight_count: `None`
- large_sector_weight_count: `None`

## Rejected Rows By Reason
- corporate_action_contaminated: 141
- insufficient_forward_window: 43
- invalid_price_source: 13
- missing_entry_date: 321
- missing_entry_price: 331
- missing_required_mfe_mae: 4337
- missing_trigger_type: 1238
- not_representative_for_aggregate: 3100
- not_usable_for_promotion: 1595
- price_only_no_evidence: 585
- raw_all_basis: 12

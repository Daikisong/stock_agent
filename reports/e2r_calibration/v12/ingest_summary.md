# V12 Residual Calibration Ingest Summary

v12는 sector/archetype shadow-only profile 생성용입니다. 기본 active profile은 변경하지 않습니다.
case_fixture나 과거 연구 재현 성공은 live discovery 증명이 아닙니다.
default scoring did not change. future active promotion requires a separate explicit task.
source proxy 또는 evidence URL 한계는 promotion blocker로 보고서에 남깁니다.

- md_input_root: `docs/round`
- v12_result_md_count: `87`
- v12_parsed_document_count: `87`
- v12_failed_document_count: `0`
- v12_raw_trigger_rows: `1456`
- v12_validated_trigger_rows: `960`
- v12_representative_trigger_rows: `748`
- v12_rejected_rows: `958`
- large_sectors_covered: `['L10_POLICY_EVENT_CROSS_REDTEAM_MISC', 'L1_INDUSTRIALS_INFRA_DEFENSE_GRID', 'L2_AI_SEMICONDUCTOR_ELECTRONICS', 'L3_BATTERY_EV_GREEN_MOBILITY', 'L4_MATERIALS_SPREAD_RESOURCE', 'L5_CONSUMER_BRAND_DISTRIBUTION', 'L6_FINANCIAL_CAPITAL_RETURN_DIGITAL', 'L7_BIO_HEALTHCARE_MEDICAL', 'L8_PLATFORM_CONTENT_SW_SECURITY', 'L9_CONSTRUCTION_REALESTATE_HOUSING']`
- canonical_archetypes_covered: `['C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG', 'C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY', 'C06_HBM_MEMORY_CUSTOMER_CAPACITY', 'C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH', 'C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF', 'C11_BATTERY_ORDERBOOK_RERATING', 'C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK', 'C13_BATTERY_JV_UTILIZATION_AMPC_IRA', 'C14_EV_DEMAND_SLOWDOWN_4B_4C', 'C15_MATERIAL_SPREAD_SUPERCYCLE', 'C16_STRATEGIC_RESOURCE_POLICY_SUPPLY', 'C17_CHEMICAL_COMMODITY_MARGIN_SPREAD', 'C18_CONSUMER_EXPORT_CHANNEL_REORDER', 'C19_BRAND_RETAIL_INVENTORY_MARGIN', 'C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION', 'C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN', 'C22_INSURANCE_RATE_CYCLE_RESERVE', 'C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION', 'C24_BIO_TRIAL_DATA_EVENT_RISK', 'C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT', 'C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE', 'C27_CONTENT_IP_GLOBAL_MONETIZATION', 'C28_SOFTWARE_SECURITY_CONTRACT_RETENTION', 'C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE', 'C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK', 'C31_POLICY_SUBSIDY_LEGISLATION_EVENT', 'C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP']`
- stage_transition_summary_rows: `410`
- evidence_url_pending_count: `0`
- source_proxy_only_count: `21`
- active_default_profile_preserved: `True`
- production_default_scoring_changed: `False`

## Rejected Rows By Reason
- insufficient_forward_window: 14
- missing_required_mfe_mae: 496
- not_representative_for_aggregate: 517
- not_usable_for_promotion: 223
- price_only_no_evidence: 50

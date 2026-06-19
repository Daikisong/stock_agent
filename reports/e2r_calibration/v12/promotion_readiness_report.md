# V12 Promotion Readiness Report

v12는 rolling calibration입니다. case_fixture나 historical research 성공은 live discovery 증명이 아닙니다.
`run-v12-calibration`은 safe patch만 scope 제한으로 기본 프로파일에 반영합니다.
source proxy / evidence URL 한계가 있으면 positive patch는 막고 guardrail만 허용합니다.

- active_profile_after_apply: `e2r_2_2_rolling_calibrated`
- production_default_scoring_changed_after_apply: `true`
- default_promotion_ready: `False`
- next_patch_ready: `True`
- apply_next_patch_count: `112`
- stage_transition_summary_rows: `10660`

## Promotion Decisions

| axis | scope | decision | promotion_type | ready_for_next_patch | missing_to_promote | recommended_next_action |
|---|---|---|---|---|---|---|
| stage2_required_bridge | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| full_4b_overlay_candidate | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | blocked_by_data_quality | Type1_safety_guardrail | False | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| earlier_thesis_break_watch | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| local_4b_watch_guard | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| earlier_thesis_break_watch | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | L2_AI_SEMICONDUCTOR_ELECTRONICS | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| local_4b_watch_guard | L2_AI_SEMICONDUCTOR_ELECTRONICS | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| earlier_thesis_break_watch | L2_AI_SEMICONDUCTOR_ELECTRONICS | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | L3_BATTERY_EV_GREEN_MOBILITY | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| local_4b_watch_guard | L3_BATTERY_EV_GREEN_MOBILITY | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| earlier_thesis_break_watch | L3_BATTERY_EV_GREEN_MOBILITY | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | L4_MATERIALS_SPREAD_RESOURCE | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| local_4b_watch_guard | L4_MATERIALS_SPREAD_RESOURCE | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| earlier_thesis_break_watch | L4_MATERIALS_SPREAD_RESOURCE | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | L5_CONSUMER_BRAND_DISTRIBUTION | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| full_4b_overlay_candidate | L5_CONSUMER_BRAND_DISTRIBUTION | blocked_by_data_quality | Type1_safety_guardrail | False | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| earlier_thesis_break_watch | L5_CONSUMER_BRAND_DISTRIBUTION | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| full_4b_overlay_candidate | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | blocked_by_data_quality | Type1_safety_guardrail | False | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| earlier_thesis_break_watch | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | L7_BIO_HEALTHCARE_MEDICAL | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| full_4b_overlay_candidate | L7_BIO_HEALTHCARE_MEDICAL | blocked_by_data_quality | Type1_safety_guardrail | False | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| earlier_thesis_break_watch | L7_BIO_HEALTHCARE_MEDICAL | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | L8_PLATFORM_CONTENT_SW_SECURITY | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| local_4b_watch_guard | L8_PLATFORM_CONTENT_SW_SECURITY | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| earlier_thesis_break_watch | L8_PLATFORM_CONTENT_SW_SECURITY | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | L9_CONSTRUCTION_REALESTATE_HOUSING | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| local_4b_watch_guard | L9_CONSTRUCTION_REALESTATE_HOUSING | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| earlier_thesis_break_watch | L9_CONSTRUCTION_REALESTATE_HOUSING | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C01_ORDER_BACKLOG_MARGIN_BRIDGE | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| local_4b_watch_guard | C01_ORDER_BACKLOG_MARGIN_BRIDGE | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| hard_4c_confirmation | C01_ORDER_BACKLOG_MARGIN_BRIDGE | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C02_POWER_GRID_DATACENTER_CAPEX | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| local_4b_watch_guard | C02_POWER_GRID_DATACENTER_CAPEX | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| full_4b_overlay_candidate | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | blocked_by_data_quality | Type1_safety_guardrail | False | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| earlier_thesis_break_watch | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| local_4b_watch_guard | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| full_4b_overlay_candidate | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | blocked_by_data_quality | Type1_safety_guardrail | False | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| earlier_thesis_break_watch | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C06_HBM_MEMORY_CUSTOMER_CAPACITY | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| local_4b_watch_guard | C06_HBM_MEMORY_CUSTOMER_CAPACITY | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| earlier_thesis_break_watch | C06_HBM_MEMORY_CUSTOMER_CAPACITY | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| full_4b_overlay_candidate | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | blocked_by_data_quality | Type1_safety_guardrail | False | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| stage2_required_bridge | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| local_4b_watch_guard | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| earlier_thesis_break_watch | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| local_4b_watch_guard | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| earlier_thesis_break_watch | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| local_4b_watch_guard | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| earlier_thesis_break_watch | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C11_BATTERY_ORDERBOOK_RERATING | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| local_4b_watch_guard | C11_BATTERY_ORDERBOOK_RERATING | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| earlier_thesis_break_watch | C11_BATTERY_ORDERBOOK_RERATING | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| full_4b_overlay_candidate | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | blocked_by_data_quality | Type1_safety_guardrail | False | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| earlier_thesis_break_watch | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| full_4b_overlay_candidate | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | blocked_by_data_quality | Type1_safety_guardrail | False | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| earlier_thesis_break_watch | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C14_EV_DEMAND_SLOWDOWN_4B_4C | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| local_4b_watch_guard | C14_EV_DEMAND_SLOWDOWN_4B_4C | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| earlier_thesis_break_watch | C14_EV_DEMAND_SLOWDOWN_4B_4C | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C15_MATERIAL_SPREAD_SUPERCYCLE | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| local_4b_watch_guard | C15_MATERIAL_SPREAD_SUPERCYCLE | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| earlier_thesis_break_watch | C15_MATERIAL_SPREAD_SUPERCYCLE | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| local_4b_watch_guard | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| full_4b_overlay_candidate | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | blocked_by_data_quality | Type1_safety_guardrail | False | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| earlier_thesis_break_watch | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C18_CONSUMER_EXPORT_CHANNEL_REORDER | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| local_4b_watch_guard | C18_CONSUMER_EXPORT_CHANNEL_REORDER | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| earlier_thesis_break_watch | C18_CONSUMER_EXPORT_CHANNEL_REORDER | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C19_BRAND_RETAIL_INVENTORY_MARGIN | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| full_4b_overlay_candidate | C19_BRAND_RETAIL_INVENTORY_MARGIN | blocked_by_data_quality | Type1_safety_guardrail | False | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| earlier_thesis_break_watch | C19_BRAND_RETAIL_INVENTORY_MARGIN | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| full_4b_overlay_candidate | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | blocked_by_data_quality | Type1_safety_guardrail | False | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| earlier_thesis_break_watch | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| full_4b_overlay_candidate | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | blocked_by_data_quality | Type1_safety_guardrail | False | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| earlier_thesis_break_watch | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C22_INSURANCE_RATE_CYCLE_RESERVE | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| local_4b_watch_guard | C22_INSURANCE_RATE_CYCLE_RESERVE | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| earlier_thesis_break_watch | C22_INSURANCE_RATE_CYCLE_RESERVE | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| full_4b_overlay_candidate | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | blocked_by_data_quality | Type1_safety_guardrail | False | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| earlier_thesis_break_watch | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C24_BIO_TRIAL_DATA_EVENT_RISK | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| local_4b_watch_guard | C24_BIO_TRIAL_DATA_EVENT_RISK | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| earlier_thesis_break_watch | C24_BIO_TRIAL_DATA_EVENT_RISK | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| full_4b_overlay_candidate | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | blocked_by_data_quality | Type1_safety_guardrail | False | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| earlier_thesis_break_watch | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| full_4b_overlay_candidate | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | blocked_by_data_quality | Type1_safety_guardrail | False | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| earlier_thesis_break_watch | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C27_CONTENT_IP_GLOBAL_MONETIZATION | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| full_4b_overlay_candidate | C27_CONTENT_IP_GLOBAL_MONETIZATION | blocked_by_data_quality | Type1_safety_guardrail | False | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| earlier_thesis_break_watch | C27_CONTENT_IP_GLOBAL_MONETIZATION | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| local_4b_watch_guard | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| earlier_thesis_break_watch | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| full_4b_overlay_candidate | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | blocked_by_data_quality | Type1_safety_guardrail | False | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| earlier_thesis_break_watch | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| local_4b_watch_guard | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| earlier_thesis_break_watch | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| local_4b_watch_guard | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| full_4b_overlay_candidate | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | blocked_by_data_quality | Type1_safety_guardrail | False | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| earlier_thesis_break_watch | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| local_4b_watch_guard | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| earlier_thesis_break_watch | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| local_4b_watch_guard | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| earlier_thesis_break_watch | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| full_4b_overlay_candidate | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | blocked_by_data_quality | Type1_safety_guardrail | False | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| earlier_thesis_break_watch | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| stage2_required_bridge | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |
| full_4b_overlay_candidate | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | blocked_by_data_quality | Type1_safety_guardrail | False | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| earlier_thesis_break_watch | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | apply_next_patch | Type1_safety_guardrail | True | none | implement_defensive_guardrail |

## Blockers
- evidence_url_pending: 3906 / v12 rows can support shadow analysis but need exact public evidence URLs before default promotion. / needed: Attach verified DART/IR/report/news URLs or mark rows as evidence-verified.
- source_proxy_only: 3723 / Some evidence is source-name-level historical event proxy, not verified production evidence. / needed: Replace proxy rows with verified as-of evidence records.
- rejected_rows: 8186 / Some rows failed validation or were not usable for shadow calibration. / needed: Fix missing sector/archetype IDs, price fields, or evidence flags.

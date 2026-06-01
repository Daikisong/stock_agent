# Archetype Weight Runtime Report

v12 연구와 가격경로 검증을 production scoring의 아키타입별 점수비중에 연결했습니다.
런타임 판단에는 미래 가격을 쓰지 않고, 과거 가격경로는 이 weight profile을 보정한 근거로만 남습니다.

- profile_id: `e2r_2_2_archetype_weight_runtime`
- enabled: `True`
- large_sector_weight_count: `10`
- canonical_archetype_weight_count: `36`

## Runtime Example

- C20 K-food/K-beauty: 계약공시보다 수출, 채널 확장, 반복수요, OPM, EPS revision 비중이 커집니다.
- C03 Defense/Grid: 정부 고객, 계약, 수주잔고, 납품 visibility가 약하면 Stage 3 쪽으로 쉽게 못 갑니다.
- C22 Insurance: 계약품질보다 ROE/PBR, reserve/rate cycle, 자본환원 비중이 커집니다.

## Top Archetype Weights

| archetype | EPS/FCF | visibility | bottleneck | mispricing | valuation | capital | info | support | green_policy |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 20.0 | 25.0 | 18.0 | 12.0 | 12.0 | 8.0 | 5.0 | 23 rows / 12 symbols | green_allowed_with_order_backlog_margin_and_fcf_bridge |
| C02_POWER_GRID_DATACENTER_CAPEX | 21.0 | 24.0 | 20.0 | 13.0 | 12.0 | 5.0 | 5.0 | 64 rows / 11 symbols | green_allowed_with_grid_capex_backlog_capacity_and_margin_visibility |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 20.0 | 24.0 | 17.0 | 14.0 | 14.0 | 6.0 | 5.0 | 89 rows / 13 symbols | green_allowed_with_government_backlog_and_delivery_visibility |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 15.0 | 22.0 | 10.0 | 15.0 | 18.0 | 10.0 | 10.0 | 62 rows / 14 symbols | watch_to_green_only_after_final_contract_and_legal_clarity |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 18.0 | 22.0 | 10.0 | 12.0 | 10.0 | 8.0 | 20.0 | 19 rows / 12 symbols | watch_to_green_only_after_contract_margin_and_working_capital_clarity |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 24.0 | 21.0 | 19.0 | 15.0 | 12.0 | 4.0 | 5.0 | 37 rows / 5 symbols | green_allowed_with_hbm_capacity_customer_and_revision |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 22.0 | 22.0 | 19.0 | 14.0 | 12.0 | 6.0 | 5.0 | 68 rows / 22 symbols | green_allowed_with_orders_and_revenue_conversion |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 22.0 | 21.0 | 16.0 | 14.0 | 12.0 | 6.0 | 9.0 | 78 rows / 13 symbols | green_allowed_with_customer_qualification_repeat_demand_and_margin_conversion |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 22.0 | 20.0 | 18.0 | 13.0 | 11.0 | 6.0 | 10.0 | 56 rows / 17 symbols | watch_to_green_with_valuation_blowoff_guard |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 22.0 | 18.0 | 14.0 | 12.0 | 10.0 | 5.0 | 19.0 | 31 rows / 10 symbols | watch_to_green_with_memory_recovery_order_and_cycle_reversal_guard |
| C11_BATTERY_ORDERBOOK_RERATING | 20.0 | 20.0 | 15.0 | 12.0 | 10.0 | 8.0 | 15.0 | 79 rows / 21 symbols | green_restricted_until_margin_and_fcf_after_capex |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 20.0 | 18.0 | 14.0 | 10.0 | 10.0 | 8.0 | 20.0 | 68 rows / 18 symbols | green_restricted_by_calloff_and_customer_demand_risk |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 20.0 | 18.0 | 14.0 | 12.0 | 10.0 | 10.0 | 16.0 | 43 rows / 11 symbols | watch_to_green_with_utilization_and_policy_durability |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 15.0 | 12.0 | 10.0 | 8.0 | 8.0 | 7.0 | 40.0 | 76 rows / 15 symbols | red_watch |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 20.0 | 12.0 | 20.0 | 10.0 | 10.0 | 8.0 | 20.0 | 71 rows / 25 symbols | green_restricted_by_cycle_reversal |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 18.0 | 18.0 | 18.0 | 12.0 | 12.0 | 7.0 | 15.0 | 67 rows / 23 symbols | watch_to_green_with_supply_contract_and_policy_durability |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 20.0 | 12.0 | 18.0 | 10.0 | 10.0 | 5.0 | 25.0 | 140 rows / 23 symbols | red_watch |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 22.0 | 23.0 | 12.0 | 16.0 | 13.0 | 4.0 | 10.0 | 126 rows / 20 symbols | green_allowed_with_export_channel_repeat_demand |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 18.0 | 18.0 | 8.0 | 15.0 | 14.0 | 7.0 | 20.0 | 89 rows / 17 symbols | watch_to_green_with_inventory_and_margin_proof |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 22.0 | 23.0 | 12.0 | 16.0 | 13.0 | 4.0 | 10.0 | 200 rows / 18 symbols | green_allowed_with_global_distribution_and_repeat_sellthrough |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 15.0 | 20.0 | 5.0 | 15.0 | 25.0 | 15.0 | 5.0 | 235 rows / 24 symbols | green_allowed_with_roe_pbr_and_executed_capital_return |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 12.0 | 22.0 | 5.0 | 14.0 | 24.0 | 18.0 | 5.0 | 162 rows / 11 symbols | green_allowed_with_reserve_rate_cycle_and_capital_return |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 12.0 | 24.0 | 5.0 | 12.0 | 10.0 | 7.0 | 30.0 | 139 rows / 15 symbols | watch_to_green_after_approval_revenue_or_royalty_conversion |
| C24_BIO_TRIAL_DATA_EVENT_RISK | 5.0 | 15.0 | 5.0 | 10.0 | 5.0 | 5.0 | 55.0 | 83 rows / 19 symbols | event_only_red_watch |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 20.0 | 22.0 | 13.0 | 14.0 | 12.0 | 9.0 | 10.0 | 101 rows / 21 symbols | green_allowed_with_export_reimbursement_and_repeat_consumable_revenue |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 20.0 | 22.0 | 8.0 | 16.0 | 14.0 | 10.0 | 10.0 | 137 rows / 16 symbols | green_allowed_with_arpu_monetization_and_op_leverage |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 20.0 | 18.0 | 8.0 | 14.0 | 12.0 | 8.0 | 20.0 | 114 rows / 25 symbols | watch_to_green_with_repeat_ip_monetization |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 20.0 | 24.0 | 8.0 | 16.0 | 14.0 | 8.0 | 10.0 | 102 rows / 22 symbols | green_allowed_with_arr_retention_and_margin_leverage |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 20.0 | 18.0 | 10.0 | 15.0 | 17.0 | 15.0 | 5.0 | 203 rows / 36 symbols | watch_to_green_with_mix_margin_and_capital_return |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 18.0 | 12.0 | 8.0 | 12.0 | 10.0 | 10.0 | 30.0 | 159 rows / 29 symbols | red_watch |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 12.0 | 15.0 | 8.0 | 15.0 | 15.0 | 10.0 | 25.0 | 206 rows / 77 symbols | event_only_until_cashflow_conversion |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 12.0 | 18.0 | 5.0 | 20.0 | 25.0 | 15.0 | 5.0 | 157 rows / 23 symbols | event_premium_not_structural_green_without_fcf_or_return |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 8.0 | 12.0 | 8.0 | 10.0 | 8.0 | 4.0 | 50.0 | 368 rows / 137 symbols | redteam_guardrail_scope_not_green_unlock |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 8.0 | 12.0 | 5.0 | 10.0 | 8.0 | 20.0 | 37.0 | 12 rows / 12 symbols | redteam_guardrail_scope_not_green_unlock |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 10.0 | 14.0 | 8.0 | 12.0 | 10.0 | 6.0 | 40.0 | 23 rows / 21 symbols | redteam_guardrail_scope_not_green_unlock |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 10.0 | 14.0 | 8.0 | 12.0 | 10.0 | 6.0 | 40.0 | 12 rows / 12 symbols | redteam_guardrail_scope_not_green_unlock |

## Guardrails

- 종목명은 weight 선택에 쓰지 않습니다.
- benchmark label과 case library는 후보 생성 input이 아닙니다.
- 미래 MFE/MAE/peak는 runtime 판단에 쓰지 않고, weight 보정 근거로만 사용합니다.
- rolling scoring은 large_sector_id와 canonical_archetype_id가 모두 직접 매칭될 때만 실행합니다.
- unknown canonical archetype을 large sector weight로 fallback하지 않습니다.
- Stage 3-Green 전역 total/revision 기준은 낮추지 않습니다.

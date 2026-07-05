# All Archetype Next Runtime Attempt Plan - 2026-07-05

이 문서는 전수 runtime status matrix의 `next_required_action`을 다음 실행 입력으로 바꾼다.

쉬운 예: 상태표가 'C08은 아직 production에서 검사하지 않았다'고 말하면, 이 문서는 'C08을 어떤 primitive와 source route로 다음 검사에 넣을지'를 적는다.

## Summary

- plan_row_count: `36`
- source_task_count: `111`
- seed_event_count: `111`
- attempt_type_counts: `{"PLANNER_TO_SOURCE_TASK_MATERIALIZATION": 8, "PROMOTED_SCORE_PATH_GAP_CLOSURE": 2, "REPLAY_TO_PRODUCTION_RUNTIME_ATTEMPT": 1, "SOURCE_EXECUTION_REPAIR": 25}`
- target_symbol_mode_counts: `{"ARCHETYPE_LEVEL_DISCOVERY": 32, "SYMBOL_SPECIFIC": 4}`
- all_tasks_score_blocked_before_execution: `True`
- all_tasks_require_llm_query_generation: `True`
- all_tasks_have_no_hardcoded_queries: `True`
- all_tasks_have_finite_budget: `True`

## Plan Rows

| archetype | priority | attempt type | symbol mode | primitives | current proof |
|---|---:|---|---|---|---|
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 10 | PROMOTED_SCORE_PATH_GAP_CLOSURE | SYMBOL_SPECIFIC | contract_amount_to_prior_sales, contract_duration_months, margin_bridge_visible | NOT_PROVEN_SCORE_PATH_ONLY |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 10 | PROMOTED_SCORE_PATH_GAP_CLOSURE | SYMBOL_SPECIFIC | customer_preorder_or_allocation, revenue_visibility_contract, hbm_capacity_constraint | NOT_PROVEN_SCORE_PATH_ONLY |
| C02_POWER_GRID_DATACENTER_CAPEX | 30 | SOURCE_EXECUTION_REPAIR | ARCHETYPE_LEVEL_DISCOVERY | datacenter_customer, order_backlog_to_sales, lead_time_extended | NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 30 | SOURCE_EXECUTION_REPAIR | ARCHETYPE_LEVEL_DISCOVERY | export_contract, government_customer, order_backlog_to_sales | NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 30 | SOURCE_EXECUTION_REPAIR | ARCHETYPE_LEVEL_DISCOVERY | policy_or_regulatory_confirmed, project_award_confirmed, permit_or_legal_delay | NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 30 | SOURCE_EXECUTION_REPAIR | ARCHETYPE_LEVEL_DISCOVERY | hbm_customer_order, customer_contract_visible, equipment_order_backlog | NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 30 | SOURCE_EXECUTION_REPAIR | ARCHETYPE_LEVEL_DISCOVERY | named_customer_quality, qualification_confirmed, repeat_order_confirmed | NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 30 | SOURCE_EXECUTION_REPAIR | ARCHETYPE_LEVEL_DISCOVERY | memory_price_increase_mentioned, supply_discipline_mentioned, cycle_demand_visibility | NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM |
| C11_BATTERY_ORDERBOOK_RERATING | 30 | SOURCE_EXECUTION_REPAIR | ARCHETYPE_LEVEL_DISCOVERY | order_backlog_to_sales, customer_contract, call_off_risk | NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 30 | SOURCE_EXECUTION_REPAIR | ARCHETYPE_LEVEL_DISCOVERY | jv_utilization, ampc_or_subsidy_capture, ex_credit_margin | NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 30 | SOURCE_EXECUTION_REPAIR | ARCHETYPE_LEVEL_DISCOVERY | spread_expansion, utilization_rate, inventory_cycle | NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 30 | SOURCE_EXECUTION_REPAIR | ARCHETYPE_LEVEL_DISCOVERY | offtake_contract, supply_shortage, policy_supply_support | NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 30 | SOURCE_EXECUTION_REPAIR | ARCHETYPE_LEVEL_DISCOVERY | inventory_spike, sell_through_confirmed, pricing_power_confirmed | NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 30 | SOURCE_EXECUTION_REPAIR | ARCHETYPE_LEVEL_DISCOVERY | export_growth_pct, platform_distribution_scale, brand_customer_diversification | NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 30 | SOURCE_EXECUTION_REPAIR | ARCHETYPE_LEVEL_DISCOVERY | roe, pbr_e, treasury_share_cancellation | NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 30 | SOURCE_EXECUTION_REPAIR | ARCHETYPE_LEVEL_DISCOVERY | csm_growth_visible, k_ics_ratio, reserve_quality_visible | NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 30 | SOURCE_EXECUTION_REPAIR | ARCHETYPE_LEVEL_DISCOVERY | regulatory_approval_confirmed, approval_to_revenue_bridge, royalty_route | NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM |
| C24_BIO_TRIAL_DATA_EVENT_RISK | 30 | SOURCE_EXECUTION_REPAIR | ARCHETYPE_LEVEL_DISCOVERY | trial_quality_visible, binary_event_unresolved, approval_not_confirmed | NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 30 | SOURCE_EXECUTION_REPAIR | ARCHETYPE_LEVEL_DISCOVERY | reimbursement_confirmed, procedure_volume_growth, export_growth_pct | NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 30 | SOURCE_EXECUTION_REPAIR | ARCHETYPE_LEVEL_DISCOVERY | arpu_growth_pct, ad_revenue_growth_pct, take_rate_improvement | NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 30 | SOURCE_EXECUTION_REPAIR | ARCHETYPE_LEVEL_DISCOVERY | ip_monetization_visible, global_launch_conversion, repeat_revenue | NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 30 | SOURCE_EXECUTION_REPAIR | ARCHETYPE_LEVEL_DISCOVERY | arr_growth_visible, nrr, retention_or_renewal | NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 30 | SOURCE_EXECUTION_REPAIR | SYMBOL_SPECIFIC | volume_growth_visible, mix_improvement, operating_leverage_visible | NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 30 | SOURCE_EXECUTION_REPAIR | ARCHETYPE_LEVEL_DISCOVERY | pf_exposure_reduced, balance_sheet_repair, cash_collection_visible | NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 30 | SOURCE_EXECUTION_REPAIR | ARCHETYPE_LEVEL_DISCOVERY | policy_or_regulatory_confirmed, direct_company_cash_route, subsidy_capture_visible | NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 30 | SOURCE_EXECUTION_REPAIR | ARCHETYPE_LEVEL_DISCOVERY | tender_offer_confirmed, minority_cash_path, control_premium_floor | NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 30 | SOURCE_EXECUTION_REPAIR | ARCHETYPE_LEVEL_DISCOVERY | price_only_blowoff, policy_headline_only, evidence_source_quality | NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 50 | PLANNER_TO_SOURCE_TASK_MATERIALIZATION | SYMBOL_SPECIFIC | order_backlog_to_sales, named_customer_quality, contract_quality | NOT_PROVEN_PLANNER_ONLY |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 50 | PLANNER_TO_SOURCE_TASK_MATERIALIZATION | ARCHETYPE_LEVEL_DISCOVERY | valuation_overheat, price_only_blowoff, order_to_revenue_bridge | NOT_PROVEN_PLANNER_ONLY |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 50 | PLANNER_TO_SOURCE_TASK_MATERIALIZATION | ARCHETYPE_LEVEL_DISCOVERY | customer_contract, call_off_risk, customer_capex_decline | NOT_PROVEN_PLANNER_ONLY |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 50 | PLANNER_TO_SOURCE_TASK_MATERIALIZATION | ARCHETYPE_LEVEL_DISCOVERY | ev_demand_slowdown, inventory_spike, price_cut_risk | NOT_PROVEN_PLANNER_ONLY |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 50 | PLANNER_TO_SOURCE_TASK_MATERIALIZATION | ARCHETYPE_LEVEL_DISCOVERY | spread_expansion, raw_material_cost_risk, utilization_rate | NOT_PROVEN_PLANNER_ONLY |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 50 | PLANNER_TO_SOURCE_TASK_MATERIALIZATION | ARCHETYPE_LEVEL_DISCOVERY | export_growth_pct, sell_through_confirmed, repeat_order_confirmed | NOT_PROVEN_PLANNER_ONLY |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 50 | PLANNER_TO_SOURCE_TASK_MATERIALIZATION | ARCHETYPE_LEVEL_DISCOVERY | auditor_or_disclosure_risk, restatement_risk, share_count_drift | NOT_PROVEN_PLANNER_ONLY |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 50 | PLANNER_TO_SOURCE_TASK_MATERIALIZATION | ARCHETYPE_LEVEL_DISCOVERY | high_mae_history, valuation_overheat, liquidity_or_microcap_risk | NOT_PROVEN_PLANNER_ONLY |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 60 | REPLAY_TO_PRODUCTION_RUNTIME_ATTEMPT | ARCHETYPE_LEVEL_DISCOVERY | thesis_break_confirmed, contract_cancelled_or_delayed, revision_slowdown | NOT_PROVEN_REPLAY_ONLY |

## Safety

이 plan은 점수를 만들지 않는다. 모든 source task는 LLM query generation과 source-backed Evidence OS claim을 요구하며, 실행 전 score/stage promotion은 금지된다.

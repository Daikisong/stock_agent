# V12 Runtime Replay Fixture Spec

이 문서는 누적 연구 Green/guard 후보를 다음 runtime replay fixture로 바꾸기 위한 실행 spec이다.
아직 production scoring 입력이 아니며, full point-in-time source fixture로 변환하기 전까지는 증명으로 쓰지 않는다.

## Summary

- spec_row_count: `68`
- ready_archetype_count: `34`
- role_counts: `{'green': 32, 'guard': 36}`
- current_runtime_gap_status_counts: `{'fixture_not_ready': 8, 'not_in_current_benchmark': 48, 'runtime_input_evidence_missing': 4, 'runtime_stage3_gate_blocked': 8}`
- skipped_archetypes: `2`

## Replay Rows

| role | archetype | symbol | as-of | expected outcome | current gap | missing axes | top failed gates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| green | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 010140 | 2025-02-06 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | runtime_input_evidence_missing | margin, backlog, contract, customer | failed_stage2_total_score:11, failed_stage2_eps_fcf:11, failed_stage2_valuation:11 |
| green | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 103230 | 2024-05-16 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | runtime_input_evidence_missing | margin, backlog, contract, customer | failed_stage2_total_score:11, failed_stage2_eps_fcf:11, failed_stage2_valuation:11 |
| guard | C02_POWER_GRID_DATACENTER_CAPEX | 267260 | 2024-02-16 | guard_candidate_must_not_reach_stage3_green | runtime_stage3_gate_blocked | none | failed_stage3_total_score:44, failed_stage3_bottleneck:44, failed_stage3_contract_quality:33 |
| guard | C02_POWER_GRID_DATACENTER_CAPEX | 006340 | 2024-05-14 | guard_candidate_must_not_reach_stage3_green | runtime_stage3_gate_blocked | none | failed_stage3_total_score:44, failed_stage3_bottleneck:44, failed_stage3_contract_quality:33 |
| green | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 079550 | 2024-09-19 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | fixture_not_ready | none | failed_stage2_total_score:12, failed_stage2_eps_fcf:12, failed_stage2_information_confidence:12 |
| guard | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 272210 | 2022-07-29 | guard_candidate_must_not_reach_stage3_green | fixture_not_ready | none | failed_stage2_total_score:12, failed_stage2_eps_fcf:12, failed_stage2_information_confidence:12 |
| green | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 034020 | 2025-01-17 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | fixture_not_ready | guard_risk, valuation_repricing, contract | none |
| guard | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 094820 | 2024-07-18 | guard_candidate_must_not_reach_stage3_green | fixture_not_ready | guard_risk, valuation_repricing, contract | none |
| green | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 375500 | 2024-10-31 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | not_in_current_benchmark | margin, backlog, contract, customer | none |
| guard | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 103230 | 2024-05-16 | guard_candidate_must_not_reach_stage3_green | not_in_current_benchmark | margin, backlog, contract, customer | none |
| green | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 000660 | 2024-04-25 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | runtime_stage3_gate_blocked | none | failed_stage3_total_score:19, failed_stage3_bottleneck:19, failed_stage2_information_confidence:7 |
| guard | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 005930 | 2024-07-11 | guard_candidate_must_not_reach_stage3_green | runtime_stage3_gate_blocked | none | failed_stage3_total_score:19, failed_stage3_bottleneck:19, failed_stage2_information_confidence:7 |
| green | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 042700 | 2024-02-08 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | fixture_not_ready | customer, backlog, contract, margin | none |
| guard | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 031980 | 2024-06-14 | guard_candidate_must_not_reach_stage3_green | fixture_not_ready | customer, backlog, contract, margin | none |
| green | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 131290 | 2024-04-26 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | not_in_current_benchmark | customer, backlog, contract, margin | none |
| guard | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 098120 | 2024-04-26 | guard_candidate_must_not_reach_stage3_green | not_in_current_benchmark | customer, backlog, contract, margin | none |
| green | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 131290 | 2024-04-26 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | not_in_current_benchmark | guard_risk, valuation_repricing, customer | none |
| guard | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 036930 | 2024-04-08 | guard_candidate_must_not_reach_stage3_green | not_in_current_benchmark | guard_risk, valuation_repricing, customer | none |
| green | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 317330 | 2024-01-02 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | runtime_stage3_gate_blocked | none | failed_stage3_total_score:1, failed_stage3_visibility:1, failed_stage3_bottleneck:1 |
| guard | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 089790 | 2024-07-22 | guard_candidate_must_not_reach_stage3_green | runtime_stage3_gate_blocked | none | failed_stage3_total_score:1, failed_stage3_visibility:1, failed_stage3_bottleneck:1 |
| green | C11_BATTERY_ORDERBOOK_RERATING | 121600 | 2023-02-09 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | not_in_current_benchmark | margin, backlog, contract, customer, guard_risk | none |
| guard | C11_BATTERY_ORDERBOOK_RERATING | 006110 | 2023-07-26 | guard_candidate_must_not_reach_stage3_green | not_in_current_benchmark | margin, backlog, contract, customer, guard_risk | none |
| green | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 051490 | 2020-07-13 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | not_in_current_benchmark | margin, backlog, contract, customer, guard_risk | none |
| guard | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 006400 | 2023-04-25 | guard_candidate_must_not_reach_stage3_green | not_in_current_benchmark | margin, backlog, contract, customer, guard_risk | none |
| green | C15_MATERIAL_SPREAD_SUPERCYCLE | 298020 | 2021-01-14 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | not_in_current_benchmark | margin, contract, guard_risk | none |
| guard | C15_MATERIAL_SPREAD_SUPERCYCLE | 004020 | 2024-02-07 | guard_candidate_must_not_reach_stage3_green | not_in_current_benchmark | margin, contract, guard_risk | none |
| green | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 010130 | 2024-08-07 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | fixture_not_ready | margin, contract, guard_risk | none |
| guard | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 005490 | 2023-10-20 | guard_candidate_must_not_reach_stage3_green | fixture_not_ready | margin, contract, guard_risk | none |
| green | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 011780 | 2021-01-21 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | not_in_current_benchmark | margin, contract, guard_risk | none |
| guard | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 006650 | 2021-02-16 | guard_candidate_must_not_reach_stage3_green | not_in_current_benchmark | margin, contract, guard_risk | none |
| green | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 003230 | 2024-05-16 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | not_in_current_benchmark | consumer_sell_through, margin, customer | none |
| guard | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 097950 | 2024-05-16 | guard_candidate_must_not_reach_stage3_green | not_in_current_benchmark | consumer_sell_through, margin, customer | none |
| green | C19_BRAND_RETAIL_INVENTORY_MARGIN | 036620 | 2024-05-21 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | not_in_current_benchmark | consumer_sell_through, margin, customer | none |
| guard | C19_BRAND_RETAIL_INVENTORY_MARGIN | 383220 | 2023-05-16 | guard_candidate_must_not_reach_stage3_green | not_in_current_benchmark | consumer_sell_through, margin, customer | none |
| green | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 192820 | 2025-02-24 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | runtime_stage3_gate_blocked | none | failed_stage2_total_score:22, failed_stage3_total_score:22, failed_stage3_visibility:22 |
| guard | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 439090 | 2023-06-08 | guard_candidate_must_not_reach_stage3_green | runtime_stage3_gate_blocked | none | failed_stage2_total_score:22, failed_stage3_total_score:22, failed_stage3_visibility:22 |
| green | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 105560 | 2025-05-26 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | not_in_current_benchmark | capital_return, valuation_repricing, guard_risk | none |
| guard | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 323410 | 2024-02-26 | guard_candidate_must_not_reach_stage3_green | not_in_current_benchmark | capital_return, valuation_repricing, guard_risk | none |
| green | C22_INSURANCE_RATE_CYCLE_RESERVE | 032830 | 2024-02-21 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | not_in_current_benchmark | insurance_quality, capital_return, guard_risk | none |
| guard | C22_INSURANCE_RATE_CYCLE_RESERVE | 088350 | 2024-07-11 | guard_candidate_must_not_reach_stage3_green | not_in_current_benchmark | insurance_quality, capital_return, guard_risk | none |
| green | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 000100 | 2024-08-20 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | not_in_current_benchmark | bio_commercialization, guard_risk | none |
| guard | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 028300 | 2024-04-30 | guard_candidate_must_not_reach_stage3_green | not_in_current_benchmark | bio_commercialization, guard_risk | none |
| guard | C24_BIO_TRIAL_DATA_EVENT_RISK | 028300 | 2024-05-16 | guard_candidate_must_not_reach_stage3_green | not_in_current_benchmark | bio_commercialization, guard_risk | none |
| guard | C24_BIO_TRIAL_DATA_EVENT_RISK | 288330 | 2023-06-23 | guard_candidate_must_not_reach_stage3_green | not_in_current_benchmark | bio_commercialization, guard_risk | none |
| green | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 335890 | 2023-01-13 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | not_in_current_benchmark | bio_commercialization, guard_risk | none |
| guard | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 145720 | 2024-02-29 | guard_candidate_must_not_reach_stage3_green | not_in_current_benchmark | bio_commercialization, guard_risk | none |
| green | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 067160 | 2021-07-27 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | not_in_current_benchmark | software_retention, customer, margin | none |
| guard | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 035720 | 2021-06-24 | guard_candidate_must_not_reach_stage3_green | not_in_current_benchmark | software_retention, customer, margin | none |
| green | C27_CONTENT_IP_GLOBAL_MONETIZATION | 194480 | 2021-01-21 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | not_in_current_benchmark | software_retention, customer, margin | none |
| guard | C27_CONTENT_IP_GLOBAL_MONETIZATION | 259960 | 2021-11-12 | guard_candidate_must_not_reach_stage3_green | not_in_current_benchmark | software_retention, customer, margin | none |
| green | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 058970 | 2023-03-15 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | not_in_current_benchmark | software_retention, customer, margin | none |
| guard | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 030520 | 2024-01-10 | guard_candidate_must_not_reach_stage3_green | not_in_current_benchmark | software_retention, customer, margin | none |
| green | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 000270 | 2023-04-26 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | not_in_current_benchmark | margin, backlog, contract, customer, guard_risk | none |
| guard | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 011210 | 2024-01-26 | guard_candidate_must_not_reach_stage3_green | not_in_current_benchmark | margin, backlog, contract, customer, guard_risk | none |
| green | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 000720 | 2021-05-27 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | not_in_current_benchmark | margin, contract, guard_risk | none |
| guard | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 014790 | 2023-09-25 | guard_candidate_must_not_reach_stage3_green | not_in_current_benchmark | margin, contract, guard_risk | none |
| green | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 112610 | 2022-11-16 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | not_in_current_benchmark | guard_risk, valuation_repricing, contract | none |
| guard | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 011930 | 2022-08-11 | guard_candidate_must_not_reach_stage3_green | not_in_current_benchmark | guard_risk, valuation_repricing, contract | none |
| green | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 010130 | 2024-09-13 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | not_in_current_benchmark | capital_return, guard_risk | none |
| guard | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 008930 | 2024-01-15 | guard_candidate_must_not_reach_stage3_green | not_in_current_benchmark | capital_return, guard_risk | none |
| green | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 000100 | 2024-08-20 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | not_in_current_benchmark | guard_risk | none |
| guard | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 095340 | 2024-03-08 | guard_candidate_must_not_reach_stage3_green | not_in_current_benchmark | guard_risk | none |
| green | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 267260 | 2025-04-22 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | not_in_current_benchmark | guard_risk | none |
| guard | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 090430 | 2021-05-12 | guard_candidate_must_not_reach_stage3_green | not_in_current_benchmark | guard_risk | none |
| guard | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 373220 | 2024-10-28 | guard_candidate_must_not_reach_stage3_green | not_in_current_benchmark | guard_risk | none |
| guard | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 160980 | 2024-04-24 | guard_candidate_must_not_reach_stage3_green | not_in_current_benchmark | guard_risk | none |
| green | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 267260 | 2025-04-22 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit | runtime_input_evidence_missing | guard_risk | failed_stage2_total_score:11, failed_stage2_eps_fcf:11, failed_stage2_valuation:11 |
| guard | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 000100 | 2024-08-30 | guard_candidate_must_not_reach_stage3_green | runtime_input_evidence_missing | guard_risk | failed_stage2_total_score:11, failed_stage2_eps_fcf:11, failed_stage2_valuation:11 |

## Conversion Rule

1. `green` row는 source-backed primitive가 component/gate까지 올라와야 한다.
2. `guard` row는 같은 primitive를 일부 갖더라도 false Green으로 열리면 안 된다.
3. 현재 `not_in_current_benchmark`인 row는 candidate funnel/replay coverage부터 고쳐야 한다.
4. 현재 `runtime_input_evidence_missing`인 row는 parser가 아니라 source-backed 입력 가족부터 채워야 한다.
5. 현재 `runtime_bridge_axes_missing`인 row는 parser/feature adapter에서 누락 primitive를 먼저 본다.

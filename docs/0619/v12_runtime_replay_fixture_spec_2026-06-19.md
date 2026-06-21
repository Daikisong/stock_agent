# V12 Runtime Replay Fixture Spec

이 문서는 누적 연구 Green/guard 후보를 다음 runtime replay fixture로 바꾸기 위한 실행 spec이다.
아직 production scoring 입력이 아니며, full point-in-time source fixture로 변환하기 전까지는 증명으로 쓰지 않는다.

## Summary

- spec_row_count: `62`
- ready_archetype_count: `34`
- covered_archetype_count: `36`
- role_counts: `{'green': 26, 'guard': 36}`
- current_runtime_gap_status_counts: `{None: 62}`
- skipped_archetypes: `10`

## Replay Rows

| role | archetype | symbol | as-of | expected outcome | current gap | missing axes | top failed gates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| green | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 010140 | 2025-02-06 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit |  | none | none |
| guard | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 077970 | 2023-09-12 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| guard | C02_POWER_GRID_DATACENTER_CAPEX | 006340 | 2024-06-27 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| guard | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 272210 | 2022-07-29 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| guard | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 189860 | 2024-07-18 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| green | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 375500 | 2024-10-31 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit |  | none | none |
| guard | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 028050 | 2024-04-03 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| green | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 000660 | 2024-04-25 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit |  | none | none |
| guard | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 000660 | 2024-07-11 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| guard | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 031980 | 2024-06-14 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| guard | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 080580 | 2024-01-23 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| green | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 131290 | 2024-04-26 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit |  | none | none |
| guard | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 064760 | 2024-06-14 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| green | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 317330 | 2024-01-02 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit |  | none | none |
| guard | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 033640 | 2024-05-20 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| green | C11_BATTERY_ORDERBOOK_RERATING | 121600 | 2023-02-09 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit |  | none | none |
| guard | C11_BATTERY_ORDERBOOK_RERATING | 290670 | 2024-06-11 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| guard | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 006110 | 2023-10-12 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| green | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 051490 | 2020-07-13 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit |  | none | none |
| guard | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 452400 | 2024-01-19 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| guard | C14_EV_DEMAND_SLOWDOWN_4B_4C | 003670 | 2024-01-23 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| green | C15_MATERIAL_SPREAD_SUPERCYCLE | 298020 | 2021-01-14 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit |  | none | none |
| guard | C15_MATERIAL_SPREAD_SUPERCYCLE | 018470 | 2021-07-13 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| guard | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 000910 | 2023-07-04 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| green | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 011780 | 2021-01-21 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit |  | none | none |
| guard | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 006650 | 2021-02-16 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| green | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 003230 | 2024-05-16 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit |  | none | none |
| guard | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 017810 | 2024-06-28 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| green | C19_BRAND_RETAIL_INVENTORY_MARGIN | 337930 | 2024-08-09 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit |  | none | none |
| guard | C19_BRAND_RETAIL_INVENTORY_MARGIN | 081660 | 2024-08-01 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| green | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 192820 | 2025-02-24 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit |  | none | none |
| guard | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 362320 | 2023-01-19 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| green | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 105560 | 2025-05-26 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit |  | none | none |
| guard | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 006220 | 2023-01-17 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| green | C22_INSURANCE_RATE_CYCLE_RESERVE | 032830 | 2024-02-21 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit |  | none | none |
| guard | C22_INSURANCE_RATE_CYCLE_RESERVE | 088350 | 2024-07-11 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| green | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 000100 | 2024-09-24 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit |  | none | none |
| guard | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 128940 | 2022-09-13 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| guard | C24_BIO_TRIAL_DATA_EVENT_RISK | 288330 | 2023-06-23 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| green | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 335890 | 2023-01-13 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit |  | none | none |
| guard | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 328130 | 2024-01-16 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| green | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 067160 | 2021-07-27 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit |  | none | none |
| guard | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 035720 | 2021-06-24 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| green | C27_CONTENT_IP_GLOBAL_MONETIZATION | 194480 | 2021-01-21 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit |  | none | none |
| guard | C27_CONTENT_IP_GLOBAL_MONETIZATION | 253450 | 2021-11-19 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| green | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 058970 | 2023-03-15 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit |  | none | none |
| guard | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 030520 | 2024-01-10 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| green | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 000270 | 2023-04-26 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit |  | none | none |
| guard | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 011210 | 2024-01-26 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| green | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 000720 | 2021-05-27 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit |  | none | none |
| guard | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 004960 | 2023-09-15 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| green | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 112610 | 2022-11-16 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit |  | none | none |
| guard | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 389260 | 2022-08-16 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| green | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 010130 | 2024-09-13 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit |  | none | none |
| guard | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 008930 | 2024-01-15 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| green | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 000100 | 2024-08-20 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit |  | none | none |
| guard | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 003230 | 2024-06-18 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| green | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 267260 | 2025-04-22 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit |  | none | none |
| guard | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 001570 | 2024-03-05 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| guard | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 003550 | 2024-02-26 | guard_candidate_must_not_reach_stage3_green |  | none | none |
| green | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 267260 | 2025-04-22 | green_candidate_should_reach_stage3_green_or_emit_field_level_deficit |  | none | none |
| guard | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 000100 | 2024-08-30 | guard_candidate_must_not_reach_stage3_green |  | none | none |

## Conversion Rule

1. `green` row는 source-backed primitive가 component/gate까지 올라와야 한다.
2. `guard` row는 같은 primitive를 일부 갖더라도 false Green으로 열리면 안 된다.
3. 현재 `not_in_current_benchmark`인 row는 candidate funnel/replay coverage부터 고쳐야 한다.
4. 현재 `runtime_input_evidence_missing`인 row는 parser가 아니라 source-backed 입력 가족부터 채워야 한다.
5. 현재 `runtime_bridge_axes_missing`인 row는 parser/feature adapter에서 누락 primitive를 먼저 본다.

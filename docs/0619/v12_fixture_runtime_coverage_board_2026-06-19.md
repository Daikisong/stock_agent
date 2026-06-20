# V12 Fixture Runtime Coverage Board

이 보고서는 누적 Green/guard fixture 후보가 현재 runtime benchmark에서 실제로 검증되고 있는지 대조한다.
여기서 `not_in_current_benchmark`는 점수식이 맞다/틀리다 이전에 해당 archetype fixture가 현재 replay 후보로 올라오지 않았다는 뜻이다.

## Summary

- archetype_count: `36`
- ready_fixture_archetype_count: `30`
- runtime_covered_archetype_count: `7`
- ready_fixture_not_in_current_benchmark_count: `24`
- ready_fixture_in_benchmark_no_runtime_green_count: `6`
- runtime_green_archetype_count: `0`
- exact_green_fixture_present_count: `0`
- exact_guard_fixture_present_count: `0`
- status_counts: `{'fixture_not_ready': 6, 'not_in_current_benchmark': 24, 'runtime_input_evidence_missing': 2, 'runtime_stage3_gate_blocked': 4}`
- missing_required_bridge_axis_counts: `{'backlog': 9, 'bio_commercialization': 3, 'capital_return': 3, 'consumer_sell_through': 2, 'contract': 15, 'customer': 15, 'guard_risk': 22, 'insurance_quality': 1, 'margin': 18, 'software_retention': 3, 'valuation_repricing': 4}`

## Archetype Board

| archetype | fixture | runtime candidates | stages | max score | missing required axes | top failed gates | status |
| --- | --- | ---: | --- | ---: | --- | --- | --- |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | needs_verified_green_source | 12 | {'1': 12} | 35.6473 | none | failed_stage2_total_score:12, failed_stage2_eps_fcf:12, failed_stage2_information_confidence:12, failed_stage3_total_score:12 | fixture_not_ready |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | needs_green_row | 0 | {} |  | guard_risk, valuation_repricing, contract | none | fixture_not_ready |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | needs_verified_green_source | 0 | {} |  | customer, backlog, contract, margin | none | fixture_not_ready |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | needs_green_row | 0 | {} |  | margin, backlog, contract, customer, guard_risk | none | fixture_not_ready |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | needs_verified_green_source | 0 | {} |  | margin, backlog, contract, customer, guard_risk | none | fixture_not_ready |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | needs_green_row | 0 | {} |  | margin, contract, guard_risk | none | fixture_not_ready |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | ready_for_runtime_replay_fixture | 0 | {} |  | margin, backlog, contract, customer | none | not_in_current_benchmark |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | ready_for_runtime_replay_fixture | 0 | {} |  | customer, backlog, contract, margin | none | not_in_current_benchmark |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | ready_for_runtime_replay_fixture | 0 | {} |  | guard_risk, valuation_repricing, customer | none | not_in_current_benchmark |
| C11_BATTERY_ORDERBOOK_RERATING | ready_for_runtime_replay_fixture | 0 | {} |  | margin, backlog, contract, customer, guard_risk | none | not_in_current_benchmark |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | ready_for_runtime_replay_fixture | 0 | {} |  | margin, backlog, contract, customer, guard_risk | none | not_in_current_benchmark |
| C15_MATERIAL_SPREAD_SUPERCYCLE | ready_for_runtime_replay_fixture | 0 | {} |  | margin, contract, guard_risk | none | not_in_current_benchmark |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | ready_for_runtime_replay_fixture | 0 | {} |  | margin, contract, guard_risk | none | not_in_current_benchmark |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | ready_for_runtime_replay_fixture | 0 | {} |  | consumer_sell_through, margin, customer | none | not_in_current_benchmark |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | ready_for_runtime_replay_fixture | 0 | {} |  | consumer_sell_through, margin, customer | none | not_in_current_benchmark |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | ready_for_runtime_replay_fixture | 0 | {} |  | capital_return, valuation_repricing, guard_risk | none | not_in_current_benchmark |
| C22_INSURANCE_RATE_CYCLE_RESERVE | ready_for_runtime_replay_fixture | 0 | {} |  | insurance_quality, capital_return, guard_risk | none | not_in_current_benchmark |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | ready_for_runtime_replay_fixture | 0 | {} |  | bio_commercialization, guard_risk | none | not_in_current_benchmark |
| C24_BIO_TRIAL_DATA_EVENT_RISK | ready_for_runtime_replay_fixture | 0 | {} |  | bio_commercialization, guard_risk | none | not_in_current_benchmark |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | ready_for_runtime_replay_fixture | 0 | {} |  | bio_commercialization, guard_risk | none | not_in_current_benchmark |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | ready_for_runtime_replay_fixture | 0 | {} |  | software_retention, customer, margin | none | not_in_current_benchmark |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | ready_for_runtime_replay_fixture | 0 | {} |  | software_retention, customer, margin | none | not_in_current_benchmark |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | ready_for_runtime_replay_fixture | 0 | {} |  | software_retention, customer, margin | none | not_in_current_benchmark |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | ready_for_runtime_replay_fixture | 0 | {} |  | margin, backlog, contract, customer, guard_risk | none | not_in_current_benchmark |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | ready_for_runtime_replay_fixture | 0 | {} |  | margin, contract, guard_risk | none | not_in_current_benchmark |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | ready_for_runtime_replay_fixture | 0 | {} |  | guard_risk, valuation_repricing, contract | none | not_in_current_benchmark |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | ready_for_runtime_replay_fixture | 0 | {} |  | capital_return, guard_risk | none | not_in_current_benchmark |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | ready_for_runtime_replay_fixture | 0 | {} |  | guard_risk | none | not_in_current_benchmark |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | ready_for_runtime_replay_fixture | 0 | {} |  | guard_risk | none | not_in_current_benchmark |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | ready_for_runtime_replay_fixture | 0 | {} |  | guard_risk | none | not_in_current_benchmark |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | ready_for_runtime_replay_fixture | 11 | {'0': 7, '1': 4} | 4.4554 | margin, backlog, contract, customer | failed_stage2_total_score:11, failed_stage2_eps_fcf:11, failed_stage2_valuation:11, failed_stage2_information_confidence:11 | runtime_input_evidence_missing |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | ready_for_runtime_replay_fixture | 11 | {'1': 11} | 9.308 | guard_risk | failed_stage2_total_score:11, failed_stage2_eps_fcf:11, failed_stage2_valuation:11, failed_stage2_information_confidence:11 | runtime_input_evidence_missing |
| C02_POWER_GRID_DATACENTER_CAPEX | ready_for_runtime_replay_fixture | 44 | {'1': 11, '2': 33} | 72.9252 | none | failed_stage3_total_score:44, failed_stage3_bottleneck:44, failed_stage3_contract_quality:33, failed_stage3_visibility:22 | runtime_stage3_gate_blocked |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | ready_for_runtime_replay_fixture | 22 | {'1': 22} | 64.161 | none | failed_stage2_total_score:22, failed_stage3_total_score:22, failed_stage3_visibility:22, failed_stage3_bottleneck:22 | runtime_stage3_gate_blocked |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | ready_for_runtime_replay_fixture | 19 | {'3-Yellow': 19} | 80.0131 | none | failed_stage3_total_score:19, failed_stage3_bottleneck:19, failed_stage2_information_confidence:7, failed_green_cross_evidence:7 | runtime_stage3_gate_blocked |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | ready_for_runtime_replay_fixture | 1 | {'2': 1} | 72.1181 | none | failed_stage3_total_score:1, failed_stage3_visibility:1, failed_stage3_bottleneck:1 | runtime_stage3_gate_blocked |

## Simple Reading

- `fixture_not_ready`: 연구 장부 쪽 positive source 또는 Green row가 아직 부족하다.
- `not_in_current_benchmark`: current benchmark 후보 생성/funnel 또는 replay coverage가 그 archetype을 검증하지 못한다.
- `runtime_input_evidence_missing`: 후보 row는 있지만 bridge를 판정할 리포트/뉴스/컨센서스/충분한 공시+재무 입력 가족이 부족하다.
- `runtime_bridge_axes_missing`: 후보는 올라왔지만 필요한 research-axis bridge가 runtime primitive로 충분히 살아나지 않는다.
- `runtime_stage3_gate_blocked`: bridge는 일부 살아도 total/bottleneck/visibility 같은 Stage3 gate에서 막힌다.

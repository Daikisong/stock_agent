# V12 Cross-Archetype Score Loss Trace

이 문서는 HBM에 점수를 더 주기 위한 문서가 아니다.
누적 연구 Green/guard 쌍이 전 아키타입에서 runtime 어디서 사라지는지 분해한다.

## Summary

- ready_archetype_count: `30`
- spec_row_count: `60`
- role_counts: `{'green': 30, 'guard': 30}`
- gap_status_counts_by_archetype: `{'not_in_current_benchmark': 24, 'runtime_input_evidence_missing': 2, 'runtime_stage3_gate_blocked': 4}`
- loss_layer_counts_by_archetype: `{'candidate_funnel_or_replay_coverage': 24, 'runtime_input_evidence_coverage': 2, 'weighted_component_or_stage3_gate': 4}`
- runtime_candidate_status_counts_by_archetype: `{'runtime_input_evidence_missing': 2, 'runtime_stage3_gate_blocked': 4}`
- missing_required_bridge_axis_counts: `{'backlog': 6, 'bio_commercialization': 3, 'capital_return': 3, 'consumer_sell_through': 2, 'contract': 10, 'customer': 12, 'guard_risk': 18, 'insurance_quality': 1, 'margin': 14, 'software_retention': 3, 'valuation_repricing': 3}`
- scoring_policy: `diagnostic_only_no_symbol_or_archetype_bonus`

## Loss Buckets

| status | loss layer | next action |
| --- | --- | --- |
| fixture_not_ready | research_fixture_source_readiness | Repair verified Green source rows before runtime scoring changes. |
| not_in_current_benchmark | candidate_funnel_or_replay_coverage | Materialize point-in-time replay fixtures before changing scoring weights. |
| runtime_bridge_axes_missing | research_axis_to_runtime_field_translation | Patch parser/feature adapters for the missing bridge axes and keep the guard pair closed. |
| runtime_input_evidence_missing | runtime_input_evidence_coverage | Repair replay input coverage or fixture archive before blaming parser or weights. |
| runtime_stage3_gate_blocked | weighted_component_or_stage3_gate | Inspect component formula and gate thresholds only with positive/guard replay evidence. |
| runtime_green_or_near_ready | near_ready_or_green | Run exact fixture replay and verify guard rows do not become false Green. |
| runtime_needs_review | manual_review | Review score rows, gate rows, and source-backed evidence ids. |

## Archetype Rows

| archetype | green | guard | status | layer | runtime candidates | max score | missing axes | failed gates |
| --- | --- | --- | --- | --- | ---: | ---: | --- | --- |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 375500 2024-10-31 | 103230 2024-05-16 | not_in_current_benchmark | candidate_funnel_or_replay_coverage | 0 |  | margin, backlog, contract, customer | none |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 131290 2024-04-26 | 098120 2024-04-26 | not_in_current_benchmark | candidate_funnel_or_replay_coverage | 0 |  | customer, backlog, contract, margin | none |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 131290 2024-04-26 | 036930 2024-04-08 | not_in_current_benchmark | candidate_funnel_or_replay_coverage | 0 |  | guard_risk, valuation_repricing, customer | none |
| C11_BATTERY_ORDERBOOK_RERATING | 121600 2023-02-09 | 006110 2023-07-26 | not_in_current_benchmark | candidate_funnel_or_replay_coverage | 0 |  | margin, backlog, contract, customer, guard_risk | none |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 051490 2020-07-13 | 006400 2023-04-25 | not_in_current_benchmark | candidate_funnel_or_replay_coverage | 0 |  | margin, backlog, contract, customer, guard_risk | none |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 298020 2021-01-14 | 004020 2024-02-07 | not_in_current_benchmark | candidate_funnel_or_replay_coverage | 0 |  | margin, contract, guard_risk | none |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 011780 2021-01-21 | 006650 2021-02-16 | not_in_current_benchmark | candidate_funnel_or_replay_coverage | 0 |  | margin, contract, guard_risk | none |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 003230 2024-05-16 | 097950 2024-05-16 | not_in_current_benchmark | candidate_funnel_or_replay_coverage | 0 |  | consumer_sell_through, margin, customer | none |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 036620 2024-05-21 | 383220 2023-05-16 | not_in_current_benchmark | candidate_funnel_or_replay_coverage | 0 |  | consumer_sell_through, margin, customer | none |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 105560 2025-05-26 | 323410 2024-02-26 | not_in_current_benchmark | candidate_funnel_or_replay_coverage | 0 |  | capital_return, valuation_repricing, guard_risk | none |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 032830 2024-02-21 | 088350 2024-07-11 | not_in_current_benchmark | candidate_funnel_or_replay_coverage | 0 |  | insurance_quality, capital_return, guard_risk | none |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 000100 2024-09-24 | 028300 2024-04-30 | not_in_current_benchmark | candidate_funnel_or_replay_coverage | 0 |  | bio_commercialization, guard_risk | none |
| C24_BIO_TRIAL_DATA_EVENT_RISK | 028300 2024-05-16 | 288330 2023-06-23 | not_in_current_benchmark | candidate_funnel_or_replay_coverage | 0 |  | bio_commercialization, guard_risk | none |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 335890 2023-01-13 | 145720 2024-02-29 | not_in_current_benchmark | candidate_funnel_or_replay_coverage | 0 |  | bio_commercialization, guard_risk | none |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 067160 2021-07-27 | 035720 2021-06-24 | not_in_current_benchmark | candidate_funnel_or_replay_coverage | 0 |  | software_retention, customer, margin | none |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 194480 2021-01-21 | 259960 2021-11-12 | not_in_current_benchmark | candidate_funnel_or_replay_coverage | 0 |  | software_retention, customer, margin | none |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 058970 2023-03-15 | 030520 2024-01-10 | not_in_current_benchmark | candidate_funnel_or_replay_coverage | 0 |  | software_retention, customer, margin | none |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 000270 2023-04-26 | 011210 2024-01-26 | not_in_current_benchmark | candidate_funnel_or_replay_coverage | 0 |  | margin, backlog, contract, customer, guard_risk | none |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 000720 2021-05-27 | 014790 2023-09-25 | not_in_current_benchmark | candidate_funnel_or_replay_coverage | 0 |  | margin, contract, guard_risk | none |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 112610 2022-11-16 | 011930 2022-08-11 | not_in_current_benchmark | candidate_funnel_or_replay_coverage | 0 |  | guard_risk, valuation_repricing, contract | none |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 010130 2024-09-13 | 008930 2024-01-15 | not_in_current_benchmark | candidate_funnel_or_replay_coverage | 0 |  | capital_return, guard_risk | none |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 000100 2024-08-20 | 095340 2024-03-08 | not_in_current_benchmark | candidate_funnel_or_replay_coverage | 0 |  | guard_risk | none |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 267260 2025-04-22 | 090430 2021-05-12 | not_in_current_benchmark | candidate_funnel_or_replay_coverage | 0 |  | guard_risk | none |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 373220 2024-10-28 | 160980 2024-04-24 | not_in_current_benchmark | candidate_funnel_or_replay_coverage | 0 |  | guard_risk | none |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 010140 2025-02-06 | 103230 2024-05-16 | runtime_input_evidence_missing | runtime_input_evidence_coverage | 11 | 4.4554 | margin, backlog, contract, customer | failed_stage2_total_score:11, failed_stage2_eps_fcf:11, failed_stage2_valuation:11 |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 267260 2025-04-22 | 000100 2024-08-30 | runtime_input_evidence_missing | runtime_input_evidence_coverage | 11 | 9.308 | guard_risk | failed_stage2_total_score:11, failed_stage2_eps_fcf:11, failed_stage2_valuation:11 |
| C02_POWER_GRID_DATACENTER_CAPEX | 267260 2024-02-16 | 006340 2024-05-14 | runtime_stage3_gate_blocked | weighted_component_or_stage3_gate | 44 | 72.9252 | none | failed_stage3_total_score:44, failed_stage3_bottleneck:44, failed_stage3_contract_quality:33 |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 192820 2025-02-24 | 439090 2023-06-08 | runtime_stage3_gate_blocked | weighted_component_or_stage3_gate | 22 | 64.161 | none | failed_stage2_total_score:22, failed_stage3_total_score:22, failed_stage3_visibility:22 |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 000660 2024-04-25 | 005930 2024-07-11 | runtime_stage3_gate_blocked | weighted_component_or_stage3_gate | 19 | 80.0131 | none | failed_stage3_total_score:19, failed_stage3_bottleneck:19, failed_stage2_information_confidence:7 |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 317330 2024-01-02 | 089790 2024-07-22 | runtime_stage3_gate_blocked | weighted_component_or_stage3_gate | 1 | 72.1181 | none | failed_stage3_total_score:1, failed_stage3_visibility:1, failed_stage3_bottleneck:1 |

## Easy Reading

- 하닉/삼전은 예시다. 같은 구조가 금융, 보험, 바이오, 소프트웨어, 소비재, 건설/정책 이벤트에서도 생긴다.
- `not_in_current_benchmark`는 좋은 연구 사례가 있어도 현재 replay가 그 아키타입을 아예 시험하지 않는다는 뜻이다.
- `runtime_input_evidence_missing`은 후보는 있지만 리포트/뉴스/컨센서스/충분한 공시+재무 입력이 없어 parser 실패인지 판단할 수 없다는 뜻이다.
- `runtime_bridge_axes_missing`은 후보는 올라왔지만 연구 문장이 `backlog`, `contract`, `capital_return`, `bio_commercialization` 같은 runtime field로 못 바뀐다는 뜻이다.
- `runtime_stage3_gate_blocked`는 field가 일부 살아도 weighted component와 Green gate가 아직 부족하다는 뜻이다.
- 쉬운 예: C10 삼성은 후보와 리포트는 있지만 customer/backlog/contract bridge가 약하고, C21 금융은 `capital_return/valuation_repricing` fixture가 benchmark에 안 들어오며, C23 바이오는 `approval`이 매출화 bridge로 검증되지 않을 수 있다.

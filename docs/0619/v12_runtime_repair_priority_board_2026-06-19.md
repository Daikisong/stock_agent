# V12 Runtime Repair Priority Board

이 문서는 누적 연구 Green이 runtime 점수로 내려오지 못하는 원인을 작업 순서로 바꾼 보드다.
HBM만 올리는 패치가 아니라, 후보 funnel, exact replay archive, parser/feature field contract, Green gate axis 정렬을 나눠 본다.

## Summary

- archetype_count: `36`
- repair_lane_counts: `{'candidate_funnel_or_benchmark_replay': 24, 'exact_fixture_archive': 36, 'gate_bridge_axis_alignment': 18, 'runtime_field_strength': 28, 'runtime_input_evidence_coverage': 2, 'source_backed_fixture_cleaning': 3, 'weighted_gate_threshold_or_component_balance': 4}`
- primary_repair_lane_counts: `{'candidate_funnel_or_benchmark_replay': 24, 'exact_fixture_archive': 3, 'runtime_input_evidence_coverage': 2, 'source_backed_fixture_cleaning': 3, 'weighted_gate_threshold_or_component_balance': 4}`
- pair_retrospective_ready_count: `0`
- pair_strict_pit_ready_count: `0`
- top_priority_archetypes: `[{'canonical_archetype_id': 'C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION', 'priority_score': 84.2, 'primary_repair_lane': 'weighted_gate_threshold_or_component_balance'}, {'canonical_archetype_id': 'C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN', 'priority_score': 83.8, 'primary_repair_lane': 'candidate_funnel_or_benchmark_replay'}, {'canonical_archetype_id': 'R13_CROSS_ARCHETYPE_4B_4C_REDTEAM', 'priority_score': 67.8, 'primary_repair_lane': 'candidate_funnel_or_benchmark_replay'}, {'canonical_archetype_id': 'C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION', 'priority_score': 65.0, 'primary_repair_lane': 'candidate_funnel_or_benchmark_replay'}, {'canonical_archetype_id': 'C22_INSURANCE_RATE_CYCLE_RESERVE', 'priority_score': 64.2, 'primary_repair_lane': 'candidate_funnel_or_benchmark_replay'}, {'canonical_archetype_id': 'C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE', 'priority_score': 54.6, 'primary_repair_lane': 'candidate_funnel_or_benchmark_replay'}, {'canonical_archetype_id': 'C05_EPC_MEGA_CONTRACT_MARGIN_GAP', 'priority_score': 49.0, 'primary_repair_lane': 'candidate_funnel_or_benchmark_replay'}, {'canonical_archetype_id': 'C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE', 'priority_score': 47.0, 'primary_repair_lane': 'candidate_funnel_or_benchmark_replay'}, {'canonical_archetype_id': 'C18_CONSUMER_EXPORT_CHANNEL_REORDER', 'priority_score': 46.6, 'primary_repair_lane': 'candidate_funnel_or_benchmark_replay'}, {'canonical_archetype_id': 'C27_CONTENT_IP_GLOBAL_MONETIZATION', 'priority_score': 45.8, 'primary_repair_lane': 'candidate_funnel_or_benchmark_replay'}]`

## Lane Meaning

- `candidate_funnel_or_benchmark_replay`: research Green fixture가 current runtime 후보로 안 들어옴
- `exact_fixture_archive`: Green/guard exact replay 입력 아카이브가 부족함
- `runtime_input_evidence_coverage`: 후보 row는 있지만 bridge 판정에 필요한 원천 입력 가족이 부족함
- `parser_feature_field_contract`: bridge primitive가 parser/feature field contract에 없음
- `gate_bridge_axis_alignment`: bridge spec과 Green gate required axis가 서로 안 맞음
- `runtime_field_strength`: bridge spec 축은 있지만 runtime row에서 field가 0이거나 약함
- `weighted_gate_threshold_or_component_balance`: field는 있는데 weighted Stage3 gate에서 막힘
- `source_backed_fixture_cleaning`: 연구 Green이 source-backed fixture로 깨끗하지 않음

## Priority Matrix

| rank | archetype | score | primary lane | Green clean/raw | runtime | missing axes | missing field contract | why low now |
| ---: | --- | ---: | --- | ---: | --- | --- | ---: | --- |
| 1 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 84.2 | weighted_gate_threshold_or_component_balance | 22/33 | runtime_stage3_gate_blocked candidates=22 max=64.161 | none | 0  | field는 들어왔지만 weighted Stage3-Green total/component gate를 넘지 못했다. |
| 2 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 83.8 | candidate_funnel_or_benchmark_replay | 23/37 | not_in_current_benchmark candidates=0 max=None | capital_return, valuation_repricing, guard_risk | 0  | Green 연구는 있지만 current benchmark 후보가 없어 runtime score 식을 아직 시험하지 못했다. |
| 3 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 67.8 | candidate_funnel_or_benchmark_replay | 19/32 | not_in_current_benchmark candidates=0 max=None | guard_risk | 0  | Green 연구는 있지만 current benchmark 후보가 없어 runtime score 식을 아직 시험하지 못했다. |
| 4 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 65.0 | candidate_funnel_or_benchmark_replay | 16/30 | not_in_current_benchmark candidates=0 max=None | bio_commercialization, guard_risk | 0  | Green 연구는 있지만 current benchmark 후보가 없어 runtime score 식을 아직 시험하지 못했다. |
| 5 | C22_INSURANCE_RATE_CYCLE_RESERVE | 64.2 | candidate_funnel_or_benchmark_replay | 15/28 | not_in_current_benchmark candidates=0 max=None | insurance_quality, capital_return, guard_risk | 0  | Green 연구는 있지만 current benchmark 후보가 없어 runtime score 식을 아직 시험하지 못했다. |
| 6 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 54.6 | candidate_funnel_or_benchmark_replay | 11/19 | not_in_current_benchmark candidates=0 max=None | software_retention, customer, margin | 0  | Green 연구는 있지만 current benchmark 후보가 없어 runtime score 식을 아직 시험하지 못했다. |
| 7 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 49.0 | candidate_funnel_or_benchmark_replay | 9/10 | not_in_current_benchmark candidates=0 max=None | margin, backlog, contract, customer | 0  | Green 연구는 있지만 current benchmark 후보가 없어 runtime score 식을 아직 시험하지 못했다. |
| 8 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 47.0 | candidate_funnel_or_benchmark_replay | 5/10 | not_in_current_benchmark candidates=0 max=None | margin, backlog, contract, customer, guard_risk | 0  | Green 연구는 있지만 current benchmark 후보가 없어 runtime score 식을 아직 시험하지 못했다. |
| 9 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 46.6 | candidate_funnel_or_benchmark_replay | 8/14 | not_in_current_benchmark candidates=0 max=None | consumer_sell_through, margin, customer | 0  | Green 연구는 있지만 current benchmark 후보가 없어 runtime score 식을 아직 시험하지 못했다. |
| 10 | C27_CONTENT_IP_GLOBAL_MONETIZATION | 45.8 | candidate_funnel_or_benchmark_replay | 8/12 | not_in_current_benchmark candidates=0 max=None | software_retention, customer, margin | 0  | Green 연구는 있지만 current benchmark 후보가 없어 runtime score 식을 아직 시험하지 못했다. |
| 11 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 45.0 | candidate_funnel_or_benchmark_replay | 8/15 | not_in_current_benchmark candidates=0 max=None | margin, contract, guard_risk | 0  | Green 연구는 있지만 current benchmark 후보가 없어 runtime score 식을 아직 시험하지 못했다. |
| 12 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 44.6 | runtime_input_evidence_coverage | 8/9 | runtime_input_evidence_missing candidates=11 max=4.4554 | margin, backlog, contract, customer | 0  | 후보 row는 있지만 리포트/뉴스/컨센서스/충분한 공시+재무 입력이 부족해 bridge 변환 실패인지 아직 판정할 수 없다. |
| 13 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 43.8 | candidate_funnel_or_benchmark_replay | 9/12 | not_in_current_benchmark candidates=0 max=None | bio_commercialization, guard_risk | 0  | Green 연구는 있지만 current benchmark 후보가 없어 runtime score 식을 아직 시험하지 못했다. |
| 14 | C15_MATERIAL_SPREAD_SUPERCYCLE | 41.8 | candidate_funnel_or_benchmark_replay | 6/12 | not_in_current_benchmark candidates=0 max=None | margin, contract, guard_risk | 0  | Green 연구는 있지만 current benchmark 후보가 없어 runtime score 식을 아직 시험하지 못했다. |
| 15 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 40.6 | candidate_funnel_or_benchmark_replay | 6/14 | not_in_current_benchmark candidates=0 max=None | software_retention, customer, margin | 0  | Green 연구는 있지만 current benchmark 후보가 없어 runtime score 식을 아직 시험하지 못했다. |
| 16 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 40.6 | weighted_gate_threshold_or_component_balance | 5/9 | runtime_stage3_gate_blocked candidates=19 max=80.0131 | none | 0  | field는 들어왔지만 weighted Stage3-Green total/component gate를 넘지 못했다. |
| 17 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 37.8 | candidate_funnel_or_benchmark_replay | 4/12 | not_in_current_benchmark candidates=0 max=None | guard_risk, valuation_repricing, contract | 0  | Green 연구는 있지만 current benchmark 후보가 없어 runtime score 식을 아직 시험하지 못했다. |
| 18 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 36.6 | weighted_gate_threshold_or_component_balance | 4/4 | runtime_stage3_gate_blocked candidates=1 max=72.1181 | none | 0  | field는 들어왔지만 weighted Stage3-Green total/component gate를 넘지 못했다. |
| 19 | C02_POWER_GRID_DATACENTER_CAPEX | 35.0 | weighted_gate_threshold_or_component_balance | 3/5 | runtime_stage3_gate_blocked candidates=44 max=72.9252 | none | 0  | field는 들어왔지만 weighted Stage3-Green total/component gate를 넘지 못했다. |
| 20 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 31.4 | candidate_funnel_or_benchmark_replay | 1/6 | not_in_current_benchmark candidates=0 max=None | margin, backlog, contract, customer, guard_risk | 0  | Green 연구는 있지만 current benchmark 후보가 없어 runtime score 식을 아직 시험하지 못했다. |
| 21 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 31.0 | candidate_funnel_or_benchmark_replay | 1/10 | not_in_current_benchmark candidates=0 max=None | customer, backlog, contract, margin | 0  | Green 연구는 있지만 current benchmark 후보가 없어 runtime score 식을 아직 시험하지 못했다. |
| 22 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 28.2 | candidate_funnel_or_benchmark_replay | 1/3 | not_in_current_benchmark candidates=0 max=None | margin, contract, guard_risk | 0  | Green 연구는 있지만 current benchmark 후보가 없어 runtime score 식을 아직 시험하지 못했다. |
| 23 | C11_BATTERY_ORDERBOOK_RERATING | 27.8 | candidate_funnel_or_benchmark_replay | 1/2 | not_in_current_benchmark candidates=0 max=None | margin, backlog, contract, customer, guard_risk | 0  | Green 연구는 있지만 current benchmark 후보가 없어 runtime score 식을 아직 시험하지 못했다. |
| 24 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 27.4 | source_backed_fixture_cleaning | 0/1 | fixture_not_ready candidates=0 max=None | margin, backlog, contract, customer, guard_risk | 0  | 연구 Green이 source-backed exact replay fixture로 쓰기에는 아직 깨끗하지 않다. |
| 25 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 27.0 | candidate_funnel_or_benchmark_replay | 2/5 | not_in_current_benchmark candidates=0 max=None | consumer_sell_through, margin, customer | 0  | Green 연구는 있지만 current benchmark 후보가 없어 runtime score 식을 아직 시험하지 못했다. |
| 26 | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 26.2 | candidate_funnel_or_benchmark_replay | 3/8 | not_in_current_benchmark candidates=0 max=None | guard_risk | 0  | Green 연구는 있지만 current benchmark 후보가 없어 runtime score 식을 아직 시험하지 못했다. |
| 27 | C24_BIO_TRIAL_DATA_EVENT_RISK | 25.8 | candidate_funnel_or_benchmark_replay | 2/7 | not_in_current_benchmark candidates=0 max=None | bio_commercialization, guard_risk | 0  | Green 연구는 있지만 current benchmark 후보가 없어 runtime score 식을 아직 시험하지 못했다. |
| 28 | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 25.0 | runtime_input_evidence_coverage | 2/5 | runtime_input_evidence_missing candidates=11 max=9.308 | guard_risk | 0  | 후보 row는 있지만 리포트/뉴스/컨센서스/충분한 공시+재무 입력이 부족해 bridge 변환 실패인지 아직 판정할 수 없다. |
| 29 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 24.2 | candidate_funnel_or_benchmark_replay | 1/3 | not_in_current_benchmark candidates=0 max=None | guard_risk, valuation_repricing, customer | 0  | Green 연구는 있지만 current benchmark 후보가 없어 runtime score 식을 아직 시험하지 못했다. |
| 30 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 23.8 | source_backed_fixture_cleaning | 0/2 | fixture_not_ready candidates=0 max=None | customer, backlog, contract, margin | 0  | 연구 Green이 source-backed exact replay fixture로 쓰기에는 아직 깨끗하지 않다. |
| 31 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 23.4 | candidate_funnel_or_benchmark_replay | 1/1 | not_in_current_benchmark candidates=0 max=None | capital_return, guard_risk | 0  | Green 연구는 있지만 current benchmark 후보가 없어 runtime score 식을 아직 시험하지 못했다. |
| 32 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 23.0 | candidate_funnel_or_benchmark_replay | 2/5 | not_in_current_benchmark candidates=0 max=None | guard_risk | 0  | Green 연구는 있지만 current benchmark 후보가 없어 runtime score 식을 아직 시험하지 못했다. |
| 33 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 15.4 | source_backed_fixture_cleaning | 0/6 | fixture_not_ready candidates=12 max=35.6473 | none | 0  | 연구 Green이 source-backed exact replay fixture로 쓰기에는 아직 깨끗하지 않다. |
| 34 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 7.0 | exact_fixture_archive | None/None |  candidates=None max=None | none | 0  | 자동 분류만으로는 충분하지 않아 수동 점검이 필요하다. |
| 35 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 7.0 | exact_fixture_archive | None/None |  candidates=None max=None | none | 0  | 자동 분류만으로는 충분하지 않아 수동 점검이 필요하다. |
| 36 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 7.0 | exact_fixture_archive | None/None |  candidates=None max=None | none | 0  | 자동 분류만으로는 충분하지 않아 수동 점검이 필요하다. |

## Easy Reading

- C06 하닉형 문제: 후보와 bridge field는 들어왔지만 Green total/bottleneck gate 검증이 남아 있다.
- C10 삼성형 문제: 후보와 리포트는 들어왔지만 customer/backlog/contract bridge field가 아직 약하다.
- C01/C19/R13 입력형 문제: 후보 row는 있지만 bridge를 판정할 리포트/뉴스/컨센서스/충분한 공시+재무 입력 가족이 부족하다.
- C21 금융형 문제: Green 연구는 많지만 current benchmark 후보가 없어 점수식 자체를 시험하지 못했다.
- C26 플랫폼형 문제: bridge spec primitive 이름이 parser/feature field contract와 아직 연결되지 않았다.
- 쉬운 예: 재료 창고에는 좋은 사과가 있는데, 계산대 목록에는 `사과`가 아니라 `과일A`로 적혀 있거나, 계산대까지 물건이 올라오지 않은 상태다. 가격표만 바꿔서는 해결되지 않는다.

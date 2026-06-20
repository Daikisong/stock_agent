# V12 Current Runtime Field Failure Census

이 문서는 현재 benchmark runtime 후보 전체에서 점수가 어디서 깎이는지 기계적으로 집계한다.
삼전/하닉만 보는 문서가 아니라, 실제 채점된 모든 후보의 field 0점과 Green gate 실패를 센다.

## Summary

- plain_answer: 현재 runtime benchmark는 후보 120개를 채점했지만 Green은 0개다. 전부 Stage3 total과 bottleneck gate에서 막히며, 원인은 아키타입별 bridge field 0점과 gate deficit이다.
- candidate_row_count: `120`
- symbol_count: `11`
- stage_counts: `{'0': 7, '1': 60, '2': 34, '3-Yellow': 19}`
- stage3_green_count: `0`
- runtime_exercised_archetype_count: `7`
- canonical_archetype_count_in_weight_profile: `36`
- runtime_unexercised_archetype_count: `29`
- all_candidates_failed_stage3_total: `True`
- all_candidates_failed_stage3_bottleneck: `True`
- global_zero_field_note: 전역 zero count는 모든 bridge family의 coverage census다. bio/finance/software field가 120/120 zero인 것은 현재 benchmark가 그 아키타입을 거의 채점하지 않았다는 뜻이며, 각 후보에 모두 필요한 필드라는 뜻은 아니다.
- coverage_caveat: 이 census는 현재 benchmark 후보가 실제 채점한 아키타입만 증명한다. 나머지 아키타입은 점수식보다 replay/archive coverage가 먼저 필요하다.

## Global Failure Counts

| failure kind | top counts |
| --- | --- |
| failed gates | failed_stage3_bottleneck:120, failed_stage3_total_score:120, failed_stage3_visibility:79, failed_stage2_total_score:67, failed_stage3_valuation:67, failed_stage2_information_confidence:63, failed_sector_bottleneck:56, failed_stage3_market_mispricing:56, failed_domain_specific_evidence:55, failed_stage2_eps_fcf:45, failed_stage3_eps_fcf:45, failed_sector_visibility:44 |
| zero fields | research_axis_bridge_bio_commercialization:120, research_axis_bridge_capital_return:120, research_axis_bridge_insurance_quality:120, research_axis_bridge_software_retention:120, research_axis_bridge_guard_risk:109, research_axis_bridge_consumer_sell_through:75, research_axis_bridge_contract:67, contract_quality:64, capa_constraint:56, research_axis_bridge_backlog:55, backlog_rpo_visibility:44, domain_specific_evidence_score:22 |

## Archetype Census

| archetype | rows | stages | max | avg | best row | bridge m/c/b/k | top zero fields | top failed gates | avg positive deficits | diagnosis |
| --- | ---: | --- | ---: | ---: | --- | --- | --- | --- | --- | --- |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 11 | {'0': 7, '1': 4} | 4.4554 | 2.8353 | 000660 SK하이닉스 2025-11-01 0/4.4554 | 0.0/0.0/0.0/0.0 | backlog_rpo_visibility:11, capa_constraint:11, contract_quality:11, domain_specific_evidence_score:11, research_axis_bridge_backlog:11, research_axis_bridge_bio_commercialization:11 | failed_domain_specific_evidence:11, failed_green_cross_evidence:11, failed_sector_bottleneck:11, failed_sector_visibility:11, failed_stage2_eps_fcf:11, failed_stage2_information_confidence:11 | stage3_total_deficit:84.16, stage3_revision_deficit:55, stage3_contract_quality_deficit:45, domain_specific_evidence_deficit:35, stage3_visibility_deficit:15.57 | 전력/인프라는 EPS와 일부 backlog는 보이지만 contract quality, margin delivery, bottleneck gate가 부족하다. |
| C02_POWER_GRID_DATACENTER_CAPEX | 44 | {'1': 11, '2': 33} | 72.9252 | 66.9741 | 267260 HD현대일렉트릭 2023-08-01 2/72.9252 | 100.0/100.0/100.0/100.0 | research_axis_bridge_bio_commercialization:44, research_axis_bridge_capital_return:44, research_axis_bridge_guard_risk:44, research_axis_bridge_insurance_quality:44, research_axis_bridge_software_retention:44, research_axis_bridge_consumer_sell_through:33 | failed_stage3_bottleneck:44, failed_stage3_total_score:44, failed_stage3_contract_quality:33, failed_domain_specific_evidence:22, failed_sector_visibility:22, failed_stage3_visibility:22 | stage3_contract_quality_deficit:31.17, stage3_total_deficit:20.03, stage3_visibility_deficit:6.36, stage3_bottleneck_deficit:6.35, domain_specific_evidence_deficit:1.67 | 전력/인프라는 EPS와 일부 backlog는 보이지만 contract quality, margin delivery, bottleneck gate가 부족하다. |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 12 | {'1': 12} | 35.6473 | 35.6473 | 012450 한화에어로스페이스 2024-08-01 1/35.6473 | 100.0/100.0/100.0/100.0 | capa_constraint:12, research_axis_bridge_bio_commercialization:12, research_axis_bridge_capital_return:12, research_axis_bridge_guard_risk:12, research_axis_bridge_insurance_quality:12, research_axis_bridge_software_retention:12 | failed_sector_bottleneck:12, failed_stage2_eps_fcf:12, failed_stage2_information_confidence:12, failed_stage2_total_score:12, failed_stage3_bottleneck:12, failed_stage3_eps_fcf:12 | stage3_total_deficit:51.35, stage3_bottleneck_deficit:10.37, stage3_visibility_deficit:3.47 | 방산은 contract/backlog가 있어도 납품-매출-마진 전환이 EPS/FCF와 bottleneck으로 약하게 들어간다. |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 19 | {'3-Yellow': 19} | 80.0131 | 78.5529 | 000660 SK하이닉스 2024-05-01 3-Yellow/80.0131 | 100.0/100.0/100.0/100.0 | contract_quality:19, research_axis_bridge_bio_commercialization:19, research_axis_bridge_capital_return:19, research_axis_bridge_consumer_sell_through:19, research_axis_bridge_guard_risk:19, research_axis_bridge_insurance_quality:19 | failed_stage3_bottleneck:19, failed_stage3_total_score:19, failed_green_cross_evidence:7, failed_stage2_information_confidence:7 | stage3_total_deficit:8.45, stage3_bottleneck_deficit:2.79 | HBM 전망/revision과 bridge field는 잡히지만 weighted total/bottleneck gate에서 아직 Green까지 부족하다. |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 1 | {'2': 1} | 72.1181 | 72.1181 | 005930 삼성전자 2024-04-01 2/72.1181 | 100.0/100.0/100.0/0.0 | contract_quality:1, research_axis_bridge_bio_commercialization:1, research_axis_bridge_capital_return:1, research_axis_bridge_consumer_sell_through:1, research_axis_bridge_contract:1, research_axis_bridge_guard_risk:1 | failed_stage3_bottleneck:1, failed_stage3_total_score:1, failed_stage3_visibility:1 | stage3_total_deficit:14.88, stage3_bottleneck_deficit:2.33, stage3_visibility_deficit:0.33 | 삼성 memory recovery route는 margin은 잡히지만 customer/backlog/contract가 비어 direct Green이 아니다. |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 22 | {'1': 22} | 64.161 | 54.4233 | 003230 삼양식품 2024-06-01 1/64.161 | 100.0/100.0/0.0/0.0 | capa_constraint:22, research_axis_bridge_backlog:22, research_axis_bridge_bio_commercialization:22, research_axis_bridge_capital_return:22, research_axis_bridge_contract:22, research_axis_bridge_insurance_quality:22 | failed_stage2_total_score:22, failed_stage3_bottleneck:22, failed_stage3_market_mispricing:22, failed_stage3_total_score:22, failed_stage3_valuation:22, failed_stage3_visibility:22 | stage3_total_deficit:32.58, domain_specific_evidence_deficit:20.71, stage3_bottleneck_deficit:4.53, stage3_visibility_deficit:1.97 | 소비재/수출은 channel reorder, sell-through, margin bridge가 Green component로 충분히 번역되지 않는다. |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 11 | {'1': 11} | 9.308 | 9.308 | 247540 에코프로비엠 2023-08-01 1/9.308 | 0.0/0.0/0.0/0.0 | backlog_rpo_visibility:11, capa_constraint:11, contract_quality:11, domain_specific_evidence_score:11, research_axis_bridge_backlog:11, research_axis_bridge_bio_commercialization:11 | failed_domain_specific_evidence:11, failed_green_cross_evidence:11, failed_sector_bottleneck:11, failed_sector_visibility:11, failed_stage2_eps_fcf:11, failed_stage2_information_confidence:11 | stage3_total_deficit:77.69, stage3_revision_deficit:55, domain_specific_evidence_deficit:35, stage3_visibility_deficit:10.50, stage3_bottleneck_deficit:5.47 | R13은 false-positive guard 성격이므로 낮은 점수 자체는 의도일 수 있지만, guard_risk source field도 명확히 남겨야 한다. |

## Sector Census

| sector | rows | stages | max | avg | top zero fields | top failed gates |
| --- | ---: | --- | ---: | ---: | --- | --- |
| DEFENSE | 12 | {'1': 12} | 35.6473 | 35.6473 | capa_constraint:12, research_axis_bridge_bio_commercialization:12, research_axis_bridge_capital_return:12, research_axis_bridge_guard_risk:12, research_axis_bridge_insurance_quality:12, research_axis_bridge_software_retention:12 | failed_sector_bottleneck:12, failed_stage2_eps_fcf:12, failed_stage2_information_confidence:12, failed_stage2_total_score:12, failed_stage3_bottleneck:12, failed_stage3_eps_fcf:12 |
| GENERIC | 29 | {'0': 7, '1': 22} | 64.161 | 28.943 | backlog_rpo_visibility:29, capa_constraint:29, research_axis_bridge_backlog:29, research_axis_bridge_bio_commercialization:29, research_axis_bridge_capital_return:29, research_axis_bridge_contract:29 | failed_domain_specific_evidence:29, failed_sector_bottleneck:29, failed_stage2_total_score:29, failed_stage3_bottleneck:29, failed_stage3_market_mispricing:29, failed_stage3_total_score:29 |
| K_BEAUTY_EXPORT | 11 | {'1': 11} | 44.6855 | 44.6855 | capa_constraint:11, research_axis_bridge_backlog:11, research_axis_bridge_bio_commercialization:11, research_axis_bridge_capital_return:11, research_axis_bridge_contract:11, research_axis_bridge_insurance_quality:11 | failed_green_cross_evidence:11, failed_stage2_eps_fcf:11, failed_stage2_information_confidence:11, failed_stage2_total_score:11, failed_stage3_bottleneck:11, failed_stage3_eps_fcf:11 |
| MEMORY_HBM | 20 | {'2': 1, '3-Yellow': 19} | 80.0131 | 78.2311 | contract_quality:20, research_axis_bridge_bio_commercialization:20, research_axis_bridge_capital_return:20, research_axis_bridge_consumer_sell_through:20, research_axis_bridge_guard_risk:20, research_axis_bridge_insurance_quality:20 | failed_stage3_bottleneck:20, failed_stage3_total_score:20, failed_green_cross_evidence:7, failed_stage2_information_confidence:7, failed_stage3_visibility:1 |
| POWER_EQUIPMENT | 48 | {'1': 15, '2': 33} | 72.9252 | 61.3929 | research_axis_bridge_bio_commercialization:48, research_axis_bridge_capital_return:48, research_axis_bridge_guard_risk:48, research_axis_bridge_insurance_quality:48, research_axis_bridge_software_retention:48, research_axis_bridge_consumer_sell_through:37 | failed_stage3_bottleneck:48, failed_stage3_total_score:48, failed_stage3_contract_quality:37, failed_domain_specific_evidence:26, failed_sector_visibility:26, failed_stage3_visibility:26 |

## Easy Reading

- 현재 채점된 후보 120개는 모두 Stage3 total과 bottleneck gate를 실패한다.
- 하닉은 전망/revision이 무시된 것이 아니라 bridge field가 채워진 뒤에도 total/bottleneck gate 검증이 남는다.
- 전력기기는 EPS와 일부 backlog가 살아도 contract quality와 delivery-to-margin bridge가 부족해 bottleneck이 낮다.
- 방산은 계약/수주잔고가 있어도 매출/마진 전환이 EPS/FCF와 bottleneck으로 약하게 들어간다.
- 소비재/수출은 반복 주문, sell-through, channel margin bridge가 충분히 source-backed field로 안 들어간다.
- 전체 36개 아키타입 중 현재 benchmark가 실제 채점한 것은 일부다. 채점되지 않은 아키타입은 먼저 replay fixture/archive를 만들어야 한다.

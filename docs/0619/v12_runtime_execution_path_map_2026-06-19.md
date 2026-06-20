# V12 Runtime Execution Path Map

이 문서는 삼전/하닉을 HBM 특례로 올리기 위한 문서가 아니다.
삼전/하닉에서 보인 낮은 점수를 예시로 삼아, 전체 아키타입에서 연구가 실제 runtime 점수로 바뀌는 경로를 분해한다.

## Short Answer

- main_conclusion: 누적 연구는 weight profile까지 반영됐지만, runtime feature/candidate/gate layer가 각 아키타입의 source-backed 증거를 아직 충분히 점수 field로 번역하지 못한다.
- research_support_rows: `12471`
- research_positive_cases: `1495`
- research_counterexamples: `2628`
- archetype_weight_count: `36`
- feature_layer_status_counts: `{'weight_supported_but_candidate_not_exercised': 24, 'weight_supported_but_fixture_not_source_backed': 3, 'weight_supported_but_runtime_input_evidence_missing': 2, 'weight_supported_but_weighted_gate_still_blocks': 4, 'weight_supported_runtime_needs_review': 3}`
- stop_layer_counts: `{'candidate_replay_archive': 29, 'manual_review': 3, 'stage_gate': 4}`
- repair_lane_counts: `{'candidate_funnel_or_benchmark_replay': 24, 'exact_fixture_archive': 36, 'gate_bridge_axis_alignment': 18, 'runtime_field_strength': 28, 'runtime_input_evidence_coverage': 2, 'source_backed_fixture_cleaning': 3, 'weighted_gate_threshold_or_component_balance': 4}`
- primitive_support_status_counts: `{'derived_runtime_metric': 2, 'feature_and_parser_literal_exact': 27, 'feature_literal_exact_parser_missing': 1, 'parser_output_exact_score_missing': 4, 'score_and_parser_exact': 132, 'score_input_exact_parser_missing': 23}`
- hbm_case_scores: `{'sk_hynix_max_score': 80.0131, 'samsung_max_score': 72.1181, 'sk_hynix_common_loss': 'bridge_fields_present_but_weighted_gate_still_short', 'samsung_common_loss': 'c10_memory_recovery_customer_backlog_contract_bridge_still_weak'}`

## Execution Path

| order | layer | role | key code | output | can fill feature fields | easy example |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | research_corpus | 누적 연구 row와 Green/guard 사례를 모은다. | src/e2r/calibration/archetype_weight_profile.py::build_archetype_weight_profile_payload | configs/e2r_archetype_weight_profile_v2_2.json | False | 시험 범위와 배점 근거를 모으는 단계다. 답안지의 실제 답은 아직 쓰지 않는다. |
| 2 | weight_profile | 아키타입별 7개 component 배점을 정한다. | src/e2r/scoring.py::_apply_archetype_runtime_weights | archetype_component_* weighted components | False | 수학 배점을 40점으로 정하는 단계다. 수학 답이 빈칸이면 40점을 받을 수 없다. |
| 3 | candidate_replay_archive | Green/guard 사례가 실제 replay 후보와 source-backed 입력으로 들어오는지 확인한다. | src/e2r/backtest/asof_stage_promotion_autopsy.py<br>src/e2r/pipeline/korea_live_lite.py | runtime candidate rows<br>as-of feature inputs | False | 시험을 봐야 점수를 낼 수 있다. 후보가 0개면 채점도 0번이다. |
| 4 | parser_feature_bridge | 리포트/공시/뉴스/재무 입력을 source-backed runtime field로 구조화한다. | src/e2r/research/report_parser.py<br>src/e2r/features.py::DeterministicFeatureEngineer.engineer<br>src/e2r/features.py::_sector_metrics<br>src/e2r/features.py::_industrial_sub_scores<br>src/e2r/features.py::_contract_quality_score<br>src/e2r/features.py::_backlog_rpo_visibility_score | contract_quality<br>backlog_rpo_visibility<br>capa_constraint_score<br>customer_quality_score<br>ScoringPayload components | True | 답안지에 실제 풀이를 쓰는 단계다. 여기서 빈칸이면 뒤의 배점은 살아 있어도 점수가 안 오른다. |
| 5 | deterministic_score | source-backed feature field를 component 점수로 합산한다. | src/e2r/scoring.py::DeterministicScorer.score<br>src/e2r/scoring.py::_apply_archetype_runtime_weights | ScoreSnapshot<br>weighted component scores | False | 답안지를 채점하는 단계다. 채점자가 빈칸에 임의로 점수를 줄 수 없다. |
| 6 | stage_gate | weighted score와 gate 조건으로 Stage 3-Green 여부를 결정한다. | src/e2r/staging.py::StageClassifier.classify<br>src/e2r/staging.py::StageClassifier._is_stage_3_green<br>src/e2r/stage_gate_diagnostics.py::diagnose_stage_gates | StageSnapshot<br>StageGateDiagnostics | False | 총점과 필수 과목 과락을 같이 본다. 총점이 높아도 필수 과목이 비면 Green이 막힌다. |

## Focus Examples

| archetype | why this matters | weight support | top weight axes | runtime status | stop layer | missing axes | code owners | next fix |
| --- | --- | ---: | --- | --- | --- | --- | --- | --- |
| C02_POWER_GRID_DATACENTER_CAPEX | field가 일부 있어도 weighted gate가 막는 예시 | 277 rows (+50 / guard 58) | earnings_visibility, eps_fcf_explosion, bottleneck_pricing | field는 일부 들어왔지만 weighted Stage3-Green 문턱에서 아직 부족하다. | stage_gate | none | src/e2r/scoring.py::_apply_archetype_runtime_weights<br>src/e2r/staging.py::StageClassifier._is_stage_3_green<br>src/e2r/stage_gate_diagnostics.py::diagnose_stage_gates | source-backed field가 들어온 뒤에도 Green이 막히는지 weighted gate threshold와 component balance를 검증한다. |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 하닉 HBM 예시이지만 HBM 특례가 아니라 bridge 이후 gate 검증까지 보는 문제 | 229 rows (+32 / guard 56) | eps_fcf_explosion, earnings_visibility, bottleneck_pricing | field는 일부 들어왔지만 weighted Stage3-Green 문턱에서 아직 부족하다. | stage_gate | none | src/e2r/scoring.py::_apply_archetype_runtime_weights<br>src/e2r/staging.py::StageClassifier._is_stage_3_green<br>src/e2r/stage_gate_diagnostics.py::diagnose_stage_gates | source-backed field가 들어온 뒤에도 Green이 막히는지 weighted gate threshold와 component balance를 검증한다. |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 삼성전자 memory recovery route 예시 | 366 rows (+60 / guard 79) | eps_fcf_explosion, information_confidence, earnings_visibility | field는 일부 들어왔지만 weighted Stage3-Green 문턱에서 아직 부족하다. | stage_gate | none | src/e2r/scoring.py::_apply_archetype_runtime_weights<br>src/e2r/staging.py::StageClassifier._is_stage_3_green<br>src/e2r/stage_gate_diagnostics.py::diagnose_stage_gates | source-backed field가 들어온 뒤에도 Green이 막히는지 weighted gate threshold와 component balance를 검증한다. |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 금융 capital return 후보/replay gap 예시 | 413 rows (+44 / guard 43) | valuation_rerating, earnings_visibility, eps_fcf_explosion | weight support는 있지만 current runtime 후보가 0개라 feature/scoring을 실행하지 못했다. | candidate_replay_archive | capital_return, valuation_repricing, guard_risk | src/e2r/backtest/asof_stage_promotion_autopsy.py<br>src/e2r/pipeline/korea_live_lite.py | Green/guard fixture를 local official/search/report archive와 exact symbol+date replay 후보로 고정한다. |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 바이오 approval-to-revenue 후보/replay gap 예시 | 269 rows (+27 / guard 24) | information_confidence, earnings_visibility, eps_fcf_explosion | weight support는 있지만 current runtime 후보가 0개라 feature/scoring을 실행하지 못했다. | candidate_replay_archive | bio_commercialization, guard_risk | src/e2r/backtest/asof_stage_promotion_autopsy.py<br>src/e2r/pipeline/korea_live_lite.py | Green/guard fixture를 local official/search/report archive와 exact symbol+date replay 후보로 고정한다. |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 플랫폼 광고/레버리지 후보/replay gap과 field contract 후속 예시 | 334 rows (+35 / guard 65) | earnings_visibility, eps_fcf_explosion, market_mispricing | weight support는 있지만 current runtime 후보가 0개라 feature/scoring을 실행하지 못했다. | candidate_replay_archive | software_retention, customer, margin | src/e2r/backtest/asof_stage_promotion_autopsy.py<br>src/e2r/pipeline/korea_live_lite.py | Green/guard fixture를 local official/search/report archive와 exact symbol+date replay 후보로 고정한다. |

## All Archetype Stop Layers

| archetype | support rows | feature status | runtime gap | stop layer | runtime candidates | max score | missing axes |
| --- | ---: | --- | --- | --- | ---: | ---: | --- |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 1023 | weight_supported_but_candidate_not_exercised | not_in_current_benchmark | candidate_replay_archive | 0 | None | guard_risk |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 715 | weight_supported_but_candidate_not_exercised | not_in_current_benchmark | candidate_replay_archive | 0 | None | guard_risk |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 619 | weight_supported_but_candidate_not_exercised | not_in_current_benchmark | candidate_replay_archive | 0 | None | guard_risk |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 478 | weight_supported_but_candidate_not_exercised | not_in_current_benchmark | candidate_replay_archive | 0 | None | guard_risk, valuation_repricing, contract |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 473 | weight_supported_but_runtime_input_evidence_missing | runtime_input_evidence_missing | candidate_replay_archive | 11 | 9.308 | guard_risk |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 413 | weight_supported_but_candidate_not_exercised | not_in_current_benchmark | candidate_replay_archive | 0 | None | capital_return, valuation_repricing, guard_risk |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 411 | weight_supported_but_candidate_not_exercised | not_in_current_benchmark | candidate_replay_archive | 0 | None | margin, backlog, contract, customer, guard_risk |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 378 | weight_supported_but_candidate_not_exercised | not_in_current_benchmark | candidate_replay_archive | 0 | None | capital_return, guard_risk |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 377 | weight_supported_but_candidate_not_exercised | not_in_current_benchmark | candidate_replay_archive | 0 | None | margin, contract, guard_risk |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 334 | weight_supported_but_candidate_not_exercised | not_in_current_benchmark | candidate_replay_archive | 0 | None | software_retention, customer, margin |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 327 | weight_supported_but_candidate_not_exercised | not_in_current_benchmark | candidate_replay_archive | 0 | None | insurance_quality, capital_return, guard_risk |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 324 | weight_supported_but_candidate_not_exercised | not_in_current_benchmark | candidate_replay_archive | 0 | None | margin, contract, guard_risk |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 308 | weight_supported_but_candidate_not_exercised | not_in_current_benchmark | candidate_replay_archive | 0 | None | consumer_sell_through, margin, customer |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 307 | weight_supported_but_candidate_not_exercised | not_in_current_benchmark | candidate_replay_archive | 0 | None | margin, backlog, contract, customer, guard_risk |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 305 | weight_supported_but_candidate_not_exercised | not_in_current_benchmark | candidate_replay_archive | 0 | None | guard_risk, valuation_repricing, customer |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 297 | weight_supported_but_candidate_not_exercised | not_in_current_benchmark | candidate_replay_archive | 0 | None | margin, contract, guard_risk |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 295 | weight_supported_but_candidate_not_exercised | not_in_current_benchmark | candidate_replay_archive | 0 | None | margin, backlog, contract, customer |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 288 | weight_supported_but_runtime_input_evidence_missing | runtime_input_evidence_missing | candidate_replay_archive | 11 | 4.4554 | margin, backlog, contract, customer |
| C11_BATTERY_ORDERBOOK_RERATING | 286 | weight_supported_but_candidate_not_exercised | not_in_current_benchmark | candidate_replay_archive | 0 | None | margin, backlog, contract, customer, guard_risk |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 285 | weight_supported_but_candidate_not_exercised | not_in_current_benchmark | candidate_replay_archive | 0 | None | software_retention, customer, margin |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 269 | weight_supported_but_candidate_not_exercised | not_in_current_benchmark | candidate_replay_archive | 0 | None | bio_commercialization, guard_risk |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 267 | weight_supported_but_fixture_not_source_backed | fixture_not_ready | candidate_replay_archive | 12 | 35.6473 | none |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 264 | weight_supported_but_fixture_not_source_backed | fixture_not_ready | candidate_replay_archive | 0 | None | margin, backlog, contract, customer, guard_risk |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 263 | weight_supported_but_candidate_not_exercised | not_in_current_benchmark | candidate_replay_archive | 0 | None | software_retention, customer, margin |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 259 | weight_supported_but_candidate_not_exercised | not_in_current_benchmark | candidate_replay_archive | 0 | None | bio_commercialization, guard_risk |
| C24_BIO_TRIAL_DATA_EVENT_RISK | 253 | weight_supported_but_candidate_not_exercised | not_in_current_benchmark | candidate_replay_archive | 0 | None | bio_commercialization, guard_risk |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 247 | weight_supported_but_candidate_not_exercised | not_in_current_benchmark | candidate_replay_archive | 0 | None | customer, backlog, contract, margin |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 237 | weight_supported_but_fixture_not_source_backed | fixture_not_ready | candidate_replay_archive | 0 | None | customer, backlog, contract, margin |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 223 | weight_supported_but_candidate_not_exercised | not_in_current_benchmark | candidate_replay_archive | 0 | None | consumer_sell_through, margin, customer |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 262 | weight_supported_runtime_needs_review |  | manual_review | None | None | none |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 234 | weight_supported_runtime_needs_review |  | manual_review | None | None | none |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 220 | weight_supported_runtime_needs_review |  | manual_review | None | None | none |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 366 | weight_supported_but_weighted_gate_still_blocks | runtime_stage3_gate_blocked | stage_gate | 1 | 72.1181 | none |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 358 | weight_supported_but_weighted_gate_still_blocks | runtime_stage3_gate_blocked | stage_gate | 22 | 64.161 | none |
| C02_POWER_GRID_DATACENTER_CAPEX | 277 | weight_supported_but_weighted_gate_still_blocks | runtime_stage3_gate_blocked | stage_gate | 44 | 72.9252 | none |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 229 | weight_supported_but_weighted_gate_still_blocks | runtime_stage3_gate_blocked | stage_gate | 19 | 80.0131 | none |

## Easy Reading

- 연구자료 누적은 배점표를 만드는 데 쓰였다. 이것은 `weight_profile` layer다.
- 실제 점수는 답안지에 해당하는 runtime field가 채워져야 올라간다. 이것은 `parser_feature_bridge` layer다.
- 하닉 예시는 `capacity lock`, `customer allocation`, `contract/order` 같은 신호가 field로 채워진 뒤에도 weighted gate까지 검증해야 함을 보여준다.
- 삼성/C10 예시는 후보와 리포트가 있어도 customer/backlog/contract bridge가 약하면 Stage2에 남는다는 점을 보여준다.
- C01/C19/R13 예시는 후보 row가 있어도 원천 입력 가족이 부족하면 parser-feature 실패로 단정하면 안 된다는 점을 보여준다.
- C21 같은 비-HBM 예시는 연구와 weight는 있는데 current runtime 후보가 0개라 채점 자체를 못 한 경우다.
- 쉬운 예: 시험 배점을 수학 40점으로 바꿔도, 학생 답안지의 수학 풀이가 빈칸이면 40점은 자동으로 들어오지 않는다.

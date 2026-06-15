# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round
## 0. Research Metadata
- selected_round: R1
- selected_loop: 100
- selected_priority_bucket: Priority 0
- selection_basis: docs/core/V12_Research_No_Repeat_Index.md
- round_schedule_status: coverage_index_selected
- round_sector_consistency: pass
- large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
- canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
- fine_archetype_id: NUCLEAR_FINAL_CONTRACT_ENGINEERING_SERVICE_BRIDGE_VS_POLICY_HEADLINE_LEGAL_DELAY_HIGH_MAE
- loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
- output_file: e2r_stock_web_v12_residual_round_R1_loop_100_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md

## 1. Current Calibrated Profile Assumption
before_profile_id = e2r_2_1_stock_web_calibrated_proxy

after_profile_id = proposed_C04_nuclear_contract_delay_shadow_profile

rollback_reference_profile_id = e2r_2_0_baseline_reference

C04 is not a generic nuclear-theme momentum bucket. It is a policy/project/legal-delay archetype. The useful bridge is final contract, project economics, engineering/service revenue conversion, or explicit legal-delay resolution. A Czech/UAE/SMR headline without such bridge is a Stage2-watch or local 4B candidate, not a Green unlock.

## 2. Round / Large Sector / Canonical Archetype Scope
| field | value |
|---|---|
| selected_round | R1 |
| large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID |
| canonical_archetype_id | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY |
| fine_archetype_id | NUCLEAR_FINAL_CONTRACT_ENGINEERING_SERVICE_BRIDGE_VS_POLICY_HEADLINE_LEGAL_DELAY_HIGH_MAE |
| round_sector_consistency | pass |

## 3. Previous Coverage / Duplicate Avoidance Check
No-Repeat Index shows C04 at 6 rows, 5 symbols, positive/counter = 0/2 and 4B/4C = 1/0. Covered symbols include 046120, 019990, 034020, 083650, and 126720. This loop avoids those covered symbols and uses three new symbols: 052690, 051600, and 105840. The 052690 second trigger is same-symbol but a distinct trigger family and entry date, so it is useful for 4B timing but not counted as a separate new symbol. Hard duplicate key is canonical_archetype_id + symbol + trigger_type + entry_date; none of the selected rows reuse that key.

## 4. Stock-Web OHLC Input / Price Source Validation
| field | value |
|---|---|
| price_source | Songdaiki/stock-web |
| manifest_path | atlas/manifest.json |
| schema_path | atlas/schema.json |
| stock_web_manifest_max_date | 2026-02-20 |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| shard_root | atlas/ohlcv_tradable_by_symbol_year |

## 5. Historical Eligibility Gate
| case | entry_date | forward_180D_available | corporate_action_window_status | calibration_usable |
|---|---:|---:|---|---:|
| C04_052690_20240221_KEPCO_ENGINEERING_NUCLEAR_DESIGN_BRIDGE | 2024-02-21 | true | clean_180D_window | true |
| C04_052690_20240712_KEPCO_ENGINEERING_CZECH_HEADLINE_4B | 2024-07-12 | true | clean_180D_window | true |
| C04_051600_20240527_KEPCO_KPS_SERVICE_MAINTENANCE_BRIDGE | 2024-05-27 | true | clean_180D_window | true |
| C04_105840_20240115_NUCLEAR_INSTRUMENTATION_POLICY_LABEL_HIGH_MAE | 2024-01-15 | true | clean_180D_window | true |

## 6. Canonical Archetype Compression Map
```text
C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  -> FINAL_CONTRACT_OR_ENGINEERING_DESIGN_BRIDGE
     -> 052690 한전기술: policy/project headline needs final-contract or project-economics bridge; early Stage2 survives but has large interim MAE
  -> NUCLEAR_PROJECT_HEADLINE_EVENT_CAP_4B
     -> 052690 2024-07-12: project headline spike should be treated as local 4B until final contract/legal delay is resolved
  -> NUCLEAR_MAINTENANCE_SERVICE_REVENUE_BRIDGE
     -> 051600 한전KPS: service/maintenance margin bridge is lower-volatility positive path
  -> INSTRUMENTATION_POLICY_LABEL_WITHOUT_CONTRACT
     -> 105840 우진: policy-label price spike without contract bridge is high-MAE false positive
```

## 7. Case Selection Summary
| case_id | symbol | company | role | new independent | reason |
|---|---:|---|---|---:|---|
| C04_052690_20240221_KEPCO_ENGINEERING_NUCLEAR_DESIGN_BRIDGE | 052690 | 한전기술 | positive | true | delayed_project_bridge_positive_with_large_interim_mae |
| C04_052690_20240712_KEPCO_ENGINEERING_CZECH_HEADLINE_4B | 052690 | 한전기술 | 4B_overlay | false | price_spike_then_event_cap_high_mae |
| C04_051600_20240527_KEPCO_KPS_SERVICE_MAINTENANCE_BRIDGE | 051600 | 한전KPS | positive | true | maintenance_service_bridge_positive |
| C04_105840_20240115_NUCLEAR_INSTRUMENTATION_POLICY_LABEL_HIGH_MAE | 105840 | 우진 | counterexample | true | false_positive_high_mae |

## 8. Positive vs Counterexample Balance
| count_type | count |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 1 |
| 4C_case_count | 0 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 4 |

## 9. Evidence Source Map
| case | evidence_available_at_that_date | evidence_source |
|---|---|---|
| 052690 2024-02-21 | nuclear engineering/design policy and project expectation was market-visible; final contract was not yet secured | public policy/project headline proxy; price path from stock-web |
| 052690 2024-07-12 | Czech/project headline and policy momentum were market-visible; final-contract/legal-delay risk remained | public nuclear project headline proxy; price path from stock-web |
| 051600 2024-05-27 | maintenance/service and overseas nuclear-service bridge was market-visible | public service/maintenance revenue bridge proxy; price path from stock-web |
| 105840 2024-01-15 | nuclear instrumentation/policy label was market-visible but contract bridge was weak | public policy-label headline proxy; price path from stock-web |

## 10. Price Data Source Map
| symbol | profile_path | price_shard_path |
|---:|---|---|
| 052690 | atlas/symbol_profiles/052/052690.json | atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv; 2025.csv |
| 051600 | atlas/symbol_profiles/051/051600.json | atlas/ohlcv_tradable_by_symbol_year/051/051600/2024.csv |
| 105840 | atlas/symbol_profiles/105/105840.json | atlas/ohlcv_tradable_by_symbol_year/105/105840/2024.csv |

## 11. Case-by-Case Trigger Grid
| trigger_id | trigger_type | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C04_052690_20240221_S2A | Stage2-Actionable | 2024-02-21 | 71500 | 7.41 | -6.57 | 7.41 | -24.76 | 37.2 | -24.76 | current_profile_stage2_survives_but_needs_delay_risk_penalty |
| C04_052690_20240712_4B | Stage4B | 2024-07-12 | 74500 | 31.68 | -17.32 | 31.68 | -17.32 | 31.68 | -28.99 | current_profile_4b_too_late_if_waits_for_price_only_reversal |
| C04_051600_20240527_S2A | Stage2-Actionable | 2024-05-27 | 37650 | 2.26 | -6.51 | 26.03 | -6.51 | 25.1 | -6.51 | current_profile_correct_but_should_require_service_margin_bridge |
| C04_105840_20240115_S2 | Stage2 | 2024-01-15 | 10050 | 4.48 | -19.9 | 4.48 | -23.18 | 4.48 | -23.18 | current_profile_false_positive_if_policy_label_overweighted |

## 12. Trigger-Level OHLC Backtest Method
MFE_N_pct = max(high over horizon) / entry_price - 1. MAE_N_pct = min(low over horizon) / entry_price - 1. Horizons are calculated from tradable_raw stock-web daily rows available in the selected symbol-year shards. All representative rows have entry date, entry price, 30D/90D/180D MFE, 30D/90D/180D MAE, peak date, peak price, and corporate-action window status.

## 13. Current Calibrated Profile Stress Test
1. Current profile handles 051600 reasonably if service/maintenance revenue conversion is recognized as the non-price bridge.
2. It can still over-promote 105840-style policy-label instrumentation spikes when no final contract, customer, or margin bridge exists.
3. 052690 demonstrates why C04 needs a local 4B event-cap overlay: the project headline can generate large MFE, but interim MAE and post-peak drawdown are too large for unconditional Stage3/Green promotion.
4. Existing price-only blowoff guard is strengthened, not weakened.
5. Full 4B non-price requirement is strengthened: final-contract absence, legal-delay risk, project economics uncertainty, and event-cap language are non-price 4B evidence in C04.

## 14. Stage2 / Yellow / Green Comparison
| case | Stage2 timing | Yellow/Green implication | green_lateness_ratio |
|---|---|---|---|
| 052690 early design bridge | Stage2-Actionable can appear before price peak but must carry delay-risk penalty | Green should wait for final contract/project economics | not_applicable |
| 052690 July project headline | Stage2 is already late; 4B overlay should appear near local peak | Green blocked until legal/final-contract confirmation | not_applicable |
| 051600 service bridge | Stage2-Actionable is cleaner because revenue/service bridge exists | Yellow/Green can wait for margin/service confirmation | not_applicable |
| 105840 policy label | Stage2 is too generous if contract bridge absent | Green blocked; watch/4B only | not_applicable |

## 15. 4B Local vs Full-window Timing Audit
| trigger_id | four_b_evidence_type | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---|---:|---:|---|
| C04_052690_20240712_4B | project_headline_without_final_contract_and_legal_delay_confirmation | 0.94 | 0.94 | good_full_window_4B_timing |
| C04_105840_20240115_S2 | policy_label_without_final_contract_or_margin_bridge | 0.99 | 0.99 | price-only theme spike should not be promoted |

## 16. 4C Protection Audit
No hard 4C trigger is proposed. The counterexample is not a liquidation/thesis-break case; it is a C04 false-positive/high-MAE case. C04 should block Stage3/Green without final contract, project economics, legal-delay resolution, or revenue/margin conversion, but it does not require hard 4C unless the nuclear thesis itself breaks.

## 17. Sector-Specific Rule Candidate
sector_specific_rule_candidate = true

For L1 industrials/infrastructure, nuclear policy headline should not be scored the same as confirmed backlog/margin conversion. Nuclear-specific evidence has longer legal/project lead time than ordinary order backlog, so the sector needs a delay-risk penalty and an explicit bridge requirement.

## 18. Canonical-Archetype Rule Candidate
canonical_archetype_rule_candidate = true

new_axis_proposed = C04_final_contract_or_service_margin_bridge_required

Rule: C04 Stage2-Actionable requires at least one of final contract, binding project economics, engineering/service revenue conversion, maintenance-margin bridge, or explicit legal-delay resolution. If absent, nuclear policy vocabulary is Stage2-watch only and can become a 4B event-cap overlay near local price peaks.

## 19. Before / After Backtest Comparison
| profile | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | score_return_alignment_verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 4 | 17.4 | -17.94 | 0.50 | too permissive on policy headline without final-contract bridge |
| P1 sector_specific_candidate_profile | 4 | 17.4 | -17.94 | 0.25 | better after C04 delay-risk / 4B overlay |
| P2 canonical_archetype_candidate_profile | 4 | 17.4 | -17.94 | 0.25 | best: final-contract/service-margin bridge required |

## 20. Score-Return Alignment Matrix
| case | raw_component_scores_before | weighted_before | stage_before | raw_component_scores_after | weighted_after | stage_after | explanation |
|---|---|---:|---|---|---:|---|---|
| C04_052690_20240221_KEPCO_ENGINEERING_NUCLEAR_DESIGN_BRIDGE | `{"EPS/FCF Explosion": 12, "Earnings Visibility and Quality": 17, "Bottleneck and Pricing Power": 10, "Market Mispricing": 12, "Valuation Rerating Runway": 13, "Capital Allocation": 4, "Information Confidence": 10}` | 72 | Stage2 | `{"EPS/FCF Explosion": 15, "Earnings Visibility and Quality": 22, "Bottleneck and Pricing Power": 12, "Market Mispricing": 12, "Valuation Rerating Runway": 13, "Capital Allocation": 4, "Information Confidence": 10}` | 78 | Stage2-Actionable | C04 requires final-contract/project-economics, service-margin, or legal-delay bridge; policy headline without such bridge is down-weighted or routed to 4B-watch. |
| C04_052690_20240712_KEPCO_ENGINEERING_CZECH_HEADLINE_4B | `{"EPS/FCF Explosion": 15, "Earnings Visibility and Quality": 22, "Bottleneck and Pricing Power": 12, "Market Mispricing": 16, "Valuation Rerating Runway": 18, "Capital Allocation": 4, "Information Confidence": 10}` | 77 | Stage3-Yellow candidate | `{"EPS/FCF Explosion": 12, "Earnings Visibility and Quality": 14, "Bottleneck and Pricing Power": 8, "Market Mispricing": 9, "Valuation Rerating Runway": 9, "Capital Allocation": 4, "Information Confidence": 18}` | 63 | Stage4B-watch | C04 requires final-contract/project-economics, service-margin, or legal-delay bridge; policy headline without such bridge is down-weighted or routed to 4B-watch. |
| C04_051600_20240527_KEPCO_KPS_SERVICE_MAINTENANCE_BRIDGE | `{"EPS/FCF Explosion": 12, "Earnings Visibility and Quality": 17, "Bottleneck and Pricing Power": 10, "Market Mispricing": 12, "Valuation Rerating Runway": 13, "Capital Allocation": 4, "Information Confidence": 10}` | 72 | Stage2 | `{"EPS/FCF Explosion": 15, "Earnings Visibility and Quality": 22, "Bottleneck and Pricing Power": 12, "Market Mispricing": 12, "Valuation Rerating Runway": 13, "Capital Allocation": 4, "Information Confidence": 10}` | 78 | Stage2-Actionable | C04 requires final-contract/project-economics, service-margin, or legal-delay bridge; policy headline without such bridge is down-weighted or routed to 4B-watch. |
| C04_105840_20240115_NUCLEAR_INSTRUMENTATION_POLICY_LABEL_HIGH_MAE | `{"EPS/FCF Explosion": 12, "Earnings Visibility and Quality": 18, "Bottleneck and Pricing Power": 10, "Market Mispricing": 14, "Valuation Rerating Runway": 14, "Capital Allocation": 3, "Information Confidence": 8}` | 68 | Stage2 | `{"EPS/FCF Explosion": 8, "Earnings Visibility and Quality": 10, "Bottleneck and Pricing Power": 7, "Market Mispricing": 8, "Valuation Rerating Runway": 8, "Capital Allocation": 3, "Information Confidence": 22}` | 55 | Stage1/Stage2-watch | C04 requires final-contract/project-economics, service-margin, or legal-delay bridge; policy headline without such bridge is down-weighted or routed to 4B-watch. |

## 21. Residual Contribution Summary
| field | value |
|---|---|
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| same_archetype_new_symbol_count | 3 |
| same_archetype_new_trigger_family_count | 4 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 4 |
| positive_case_count | 2 |
| counterexample_count | 1 |
| current_profile_error_count | 3 |
| loop_contribution_label | canonical_archetype_rule_candidate |
| new_axis_proposed | C04_final_contract_or_service_margin_bridge_required |
| existing_axis_strengthened | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence |
| existing_axis_weakened | null |
| do_not_propose_new_weight_delta | false |

## 22. Machine-Readable Rows JSONL
```jsonl
{"row_type":"case","case_id":"C04_052690_20240221_KEPCO_ENGINEERING_NUCLEAR_DESIGN_BRIDGE","symbol":"052690","company":"한전기술","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_FINAL_CONTRACT_ENGINEERING_SERVICE_BRIDGE_VS_POLICY_HEADLINE_LEGAL_DELAY_HIGH_MAE","trigger_family":"engineering_design_policy_to_project_bridge","entry_date":"2024-02-21","entry_price":71500,"MFE_90D_pct":7.41,"MAE_90D_pct":-24.76,"trigger_outcome_label":"delayed_project_bridge_positive_with_large_interim_mae","current_profile_verdict":"current_profile_stage2_survives_but_needs_delay_risk_penalty","is_new_independent_case":true}
{"row_type":"case","case_id":"C04_052690_20240712_KEPCO_ENGINEERING_CZECH_HEADLINE_4B","symbol":"052690","company":"한전기술","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_FINAL_CONTRACT_ENGINEERING_SERVICE_BRIDGE_VS_POLICY_HEADLINE_LEGAL_DELAY_HIGH_MAE","trigger_family":"nuclear_project_headline_event_cap_legal_delay_overlay","entry_date":"2024-07-12","entry_price":74500,"MFE_90D_pct":31.68,"MAE_90D_pct":-17.32,"trigger_outcome_label":"price_spike_then_event_cap_high_mae","current_profile_verdict":"current_profile_4b_too_late_if_waits_for_price_only_reversal","is_new_independent_case":false}
{"row_type":"case","case_id":"C04_051600_20240527_KEPCO_KPS_SERVICE_MAINTENANCE_BRIDGE","symbol":"051600","company":"한전KPS","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_FINAL_CONTRACT_ENGINEERING_SERVICE_BRIDGE_VS_POLICY_HEADLINE_LEGAL_DELAY_HIGH_MAE","trigger_family":"nuclear_maintenance_service_revenue_bridge","entry_date":"2024-05-27","entry_price":37650,"MFE_90D_pct":26.03,"MAE_90D_pct":-6.51,"trigger_outcome_label":"maintenance_service_bridge_positive","current_profile_verdict":"current_profile_correct_but_should_require_service_margin_bridge","is_new_independent_case":true}
{"row_type":"case","case_id":"C04_105840_20240115_NUCLEAR_INSTRUMENTATION_POLICY_LABEL_HIGH_MAE","symbol":"105840","company":"우진","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_FINAL_CONTRACT_ENGINEERING_SERVICE_BRIDGE_VS_POLICY_HEADLINE_LEGAL_DELAY_HIGH_MAE","trigger_family":"nuclear_instrumentation_policy_label_without_contract_bridge","entry_date":"2024-01-15","entry_price":10050,"MFE_90D_pct":4.48,"MAE_90D_pct":-23.18,"trigger_outcome_label":"false_positive_high_mae","current_profile_verdict":"current_profile_false_positive_if_policy_label_overweighted","is_new_independent_case":true}
{"row_type":"trigger","case_id":"C04_052690_20240221_KEPCO_ENGINEERING_NUCLEAR_DESIGN_BRIDGE","trigger_id":"C04_052690_20240221_S2A","symbol":"052690","company":"한전기술","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_FINAL_CONTRACT_ENGINEERING_SERVICE_BRIDGE_VS_POLICY_HEADLINE_LEGAL_DELAY_HIGH_MAE","trigger_type":"Stage2-Actionable","trigger_family":"engineering_design_policy_to_project_bridge","entry_date":"2024-02-21","entry_price":71500,"MFE_30D_pct":7.41,"MAE_30D_pct":-6.57,"MFE_90D_pct":7.41,"MAE_90D_pct":-24.76,"MFE_180D_pct":37.2,"MAE_180D_pct":-24.76,"MFE_1Y_pct":37.2,"MFE_2Y_pct":null,"MAE_1Y_pct":-30.21,"MAE_2Y_pct":null,"peak_date":"2024-07-18","peak_price":98100,"trough_date":"2024-04-19","trough_price":53800,"drawdown_after_peak_pct":-37.21,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":null,"four_c_protection_label":null,"trigger_outcome_label":"delayed_project_bridge_positive_with_large_interim_mae","current_profile_verdict":"current_profile_stage2_survives_but_needs_delay_risk_penalty","price_data_repo":"Songdaiki/stock-web","profile_path":"atlas/symbol_profiles/052/052690.json","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C04_052690_20240221","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","case_id":"C04_052690_20240712_KEPCO_ENGINEERING_CZECH_HEADLINE_4B","trigger_id":"C04_052690_20240712_4B","symbol":"052690","company":"한전기술","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_FINAL_CONTRACT_ENGINEERING_SERVICE_BRIDGE_VS_POLICY_HEADLINE_LEGAL_DELAY_HIGH_MAE","trigger_type":"Stage4B","trigger_family":"nuclear_project_headline_event_cap_legal_delay_overlay","entry_date":"2024-07-12","entry_price":74500,"MFE_30D_pct":31.68,"MAE_30D_pct":-17.32,"MFE_90D_pct":31.68,"MAE_90D_pct":-17.32,"MFE_180D_pct":31.68,"MAE_180D_pct":-28.99,"MFE_1Y_pct":31.68,"MFE_2Y_pct":null,"MAE_1Y_pct":-33.09,"MAE_2Y_pct":null,"peak_date":"2024-07-18","peak_price":98100,"trough_date":"2025-01-02","trough_price":52900,"drawdown_after_peak_pct":-46.08,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":0.94,"four_b_timing_verdict":"local_4b_required_before_final_contract_confirmation","four_b_evidence_type":"project_headline_without_final_contract_and_legal_delay_confirmation","four_c_protection_label":null,"trigger_outcome_label":"price_spike_then_event_cap_high_mae","current_profile_verdict":"current_profile_4b_too_late_if_waits_for_price_only_reversal","price_data_repo":"Songdaiki/stock-web","profile_path":"atlas/symbol_profiles/052/052690.json","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv|2025.csv","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C04_052690_20240712","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"same symbol as earlier C04_052690 but different trigger family and entry date; useful as 4B overlay, not a new symbol count","independent_evidence_weight":0.6,"do_not_count_as_new_case":false}
{"row_type":"trigger","case_id":"C04_051600_20240527_KEPCO_KPS_SERVICE_MAINTENANCE_BRIDGE","trigger_id":"C04_051600_20240527_S2A","symbol":"051600","company":"한전KPS","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_FINAL_CONTRACT_ENGINEERING_SERVICE_BRIDGE_VS_POLICY_HEADLINE_LEGAL_DELAY_HIGH_MAE","trigger_type":"Stage2-Actionable","trigger_family":"nuclear_maintenance_service_revenue_bridge","entry_date":"2024-05-27","entry_price":37650,"MFE_30D_pct":2.26,"MAE_30D_pct":-6.51,"MFE_90D_pct":26.03,"MAE_90D_pct":-6.51,"MFE_180D_pct":25.1,"MAE_180D_pct":-6.51,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"peak_date":"2024-07-18","peak_price":47450,"trough_date":"2024-06-05","trough_price":35200,"drawdown_after_peak_pct":-24.45,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":null,"four_c_protection_label":null,"trigger_outcome_label":"maintenance_service_bridge_positive","current_profile_verdict":"current_profile_correct_but_should_require_service_margin_bridge","price_data_repo":"Songdaiki/stock-web","profile_path":"atlas/symbol_profiles/051/051600.json","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051600/2024.csv","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C04_051600_20240527","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","case_id":"C04_105840_20240115_NUCLEAR_INSTRUMENTATION_POLICY_LABEL_HIGH_MAE","trigger_id":"C04_105840_20240115_S2","symbol":"105840","company":"우진","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_FINAL_CONTRACT_ENGINEERING_SERVICE_BRIDGE_VS_POLICY_HEADLINE_LEGAL_DELAY_HIGH_MAE","trigger_type":"Stage2","trigger_family":"nuclear_instrumentation_policy_label_without_contract_bridge","entry_date":"2024-01-15","entry_price":10050,"MFE_30D_pct":4.48,"MAE_30D_pct":-19.9,"MFE_90D_pct":4.48,"MAE_90D_pct":-23.18,"MFE_180D_pct":4.48,"MAE_180D_pct":-23.18,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"peak_date":"2024-01-24","peak_price":10500,"trough_date":"2024-04-11","trough_price":7720,"drawdown_after_peak_pct":-32.19,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.99,"four_b_full_window_peak_proximity":0.99,"four_b_timing_verdict":"price_only_theme_spike_should_not_be_promoted","four_b_evidence_type":"policy_label_without_final_contract_or_margin_bridge","four_c_protection_label":null,"trigger_outcome_label":"false_positive_high_mae","current_profile_verdict":"current_profile_false_positive_if_policy_label_overweighted","price_data_repo":"Songdaiki/stock-web","profile_path":"atlas/symbol_profiles/105/105840.json","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105840/2024.csv","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C04_105840_20240115","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C04_052690_20240221_KEPCO_ENGINEERING_NUCLEAR_DESIGN_BRIDGE","trigger_id":"C04_052690_20240221_S2A","symbol":"052690","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","raw_component_scores_before":{"EPS/FCF Explosion":12,"Earnings Visibility and Quality":17,"Bottleneck and Pricing Power":10,"Market Mispricing":12,"Valuation Rerating Runway":13,"Capital Allocation":4,"Information Confidence":10},"weighted_score_before":72,"stage_label_before":"Stage2","raw_component_scores_after":{"EPS/FCF Explosion":15,"Earnings Visibility and Quality":22,"Bottleneck and Pricing Power":12,"Market Mispricing":12,"Valuation Rerating Runway":13,"Capital Allocation":4,"Information Confidence":10},"weighted_score_after":78,"stage_label_after":"Stage2-Actionable","changed_components":["Earnings Visibility and Quality","Information Confidence","Valuation Rerating Runway"],"component_delta_explanation":"C04 requires final-contract/project-economics, service-margin, or legal-delay bridge; policy headline without such bridge is down-weighted or routed to 4B-watch.","MFE_90D_pct":7.41,"MAE_90D_pct":-24.76,"score_return_alignment_label":"aligned_positive_with_bridge","current_profile_verdict":"current_profile_stage2_survives_but_needs_delay_risk_penalty"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C04_052690_20240712_KEPCO_ENGINEERING_CZECH_HEADLINE_4B","trigger_id":"C04_052690_20240712_4B","symbol":"052690","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","raw_component_scores_before":{"EPS/FCF Explosion":15,"Earnings Visibility and Quality":22,"Bottleneck and Pricing Power":12,"Market Mispricing":16,"Valuation Rerating Runway":18,"Capital Allocation":4,"Information Confidence":10},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow candidate","raw_component_scores_after":{"EPS/FCF Explosion":12,"Earnings Visibility and Quality":14,"Bottleneck and Pricing Power":8,"Market Mispricing":9,"Valuation Rerating Runway":9,"Capital Allocation":4,"Information Confidence":18},"weighted_score_after":63,"stage_label_after":"Stage4B-watch","changed_components":["Earnings Visibility and Quality","Information Confidence","Valuation Rerating Runway"],"component_delta_explanation":"C04 requires final-contract/project-economics, service-margin, or legal-delay bridge; policy headline without such bridge is down-weighted or routed to 4B-watch.","MFE_90D_pct":31.68,"MAE_90D_pct":-17.32,"score_return_alignment_label":"event_cap_4b_overlay","current_profile_verdict":"current_profile_4b_too_late_if_waits_for_price_only_reversal"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C04_051600_20240527_KEPCO_KPS_SERVICE_MAINTENANCE_BRIDGE","trigger_id":"C04_051600_20240527_S2A","symbol":"051600","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","raw_component_scores_before":{"EPS/FCF Explosion":12,"Earnings Visibility and Quality":17,"Bottleneck and Pricing Power":10,"Market Mispricing":12,"Valuation Rerating Runway":13,"Capital Allocation":4,"Information Confidence":10},"weighted_score_before":72,"stage_label_before":"Stage2","raw_component_scores_after":{"EPS/FCF Explosion":15,"Earnings Visibility and Quality":22,"Bottleneck and Pricing Power":12,"Market Mispricing":12,"Valuation Rerating Runway":13,"Capital Allocation":4,"Information Confidence":10},"weighted_score_after":78,"stage_label_after":"Stage2-Actionable","changed_components":["Earnings Visibility and Quality","Information Confidence","Valuation Rerating Runway"],"component_delta_explanation":"C04 requires final-contract/project-economics, service-margin, or legal-delay bridge; policy headline without such bridge is down-weighted or routed to 4B-watch.","MFE_90D_pct":26.03,"MAE_90D_pct":-6.51,"score_return_alignment_label":"aligned_positive_with_bridge","current_profile_verdict":"current_profile_correct_but_should_require_service_margin_bridge"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C04_105840_20240115_NUCLEAR_INSTRUMENTATION_POLICY_LABEL_HIGH_MAE","trigger_id":"C04_105840_20240115_S2","symbol":"105840","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","raw_component_scores_before":{"EPS/FCF Explosion":12,"Earnings Visibility and Quality":18,"Bottleneck and Pricing Power":10,"Market Mispricing":14,"Valuation Rerating Runway":14,"Capital Allocation":3,"Information Confidence":8},"weighted_score_before":68,"stage_label_before":"Stage2","raw_component_scores_after":{"EPS/FCF Explosion":8,"Earnings Visibility and Quality":10,"Bottleneck and Pricing Power":7,"Market Mispricing":8,"Valuation Rerating Runway":8,"Capital Allocation":3,"Information Confidence":22},"weighted_score_after":55,"stage_label_after":"Stage1/Stage2-watch","changed_components":["Earnings Visibility and Quality","Information Confidence","Valuation Rerating Runway"],"component_delta_explanation":"C04 requires final-contract/project-economics, service-margin, or legal-delay bridge; policy headline without such bridge is down-weighted or routed to 4B-watch.","MFE_90D_pct":4.48,"MAE_90D_pct":-23.18,"score_return_alignment_label":"false_positive_high_mae_without_contract_bridge","current_profile_verdict":"current_profile_false_positive_if_policy_label_overweighted"}
{"row_type":"aggregate_metric","round":"R1","loop":"100","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_FINAL_CONTRACT_ENGINEERING_SERVICE_BRIDGE_VS_POLICY_HEADLINE_LEGAL_DELAY_HIGH_MAE","trigger_count":4,"case_count":3,"new_independent_case_count":3,"reused_case_count":0,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":1,"four_b_case_count":1,"four_c_case_count":0,"avg_MFE_90D_pct":17.4,"avg_MAE_90D_pct":-17.94,"false_positive_count":1,"current_profile_error_count":3,"calibration_usable_trigger_count":4}
{"row_type":"shadow_weight","round":"R1","loop":"100","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","proposed_shadow_axis":"C04_final_contract_or_service_margin_bridge_required","direction":"increase_information_confidence_penalty_when_policy_headline_lacks_final_contract","stage2_required_bridge":true,"local_4b_watch_guard":true,"hard_4c_confirmation":false,"do_not_propose_new_weight_delta":false,"weights_before":{"EPS":15,"Visibility":22,"Bottleneck":10,"Mispricing":15,"Valuation":18,"Capital":10,"Information":10},"weights_after_shadow":{"EPS":14,"Visibility":24,"Bottleneck":10,"Mispricing":13,"Valuation":16,"Capital":9,"Information":14},"rationale":"C04 needs non-price final-contract, project-economics, service-margin, or legal-delay evidence; otherwise policy headline spikes have high MAE and should remain watch/4B."}
{"row_type":"residual_contribution","round":"R1","loop":"100","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["nuclear_policy_headline_without_final_contract","legal_delay_event_cap_4b_too_late","service_margin_bridge_positive_underweighted"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 23. Deferred Coding Agent Handoff Prompt
### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules
- Use only calibration_usable=true rows for quantitative calibration.
- Do not count same-symbol 4B overlay rows as new symbol evidence, but retain them for 4B timing calibration.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- C04 positive score promotion requires non-price final-contract, project-economics, service-margin, or legal-delay resolution evidence.

### Suggested implementation target
Add or strengthen a C04 canonical guard named `C04_final_contract_or_service_margin_bridge_required`. This guard should lower Stage2-Actionable / Stage3 promotion when nuclear policy vocabulary is present but final contract, project economics, legal-delay resolution, engineering/service revenue conversion, or maintenance margin bridge is absent. It should allow local Stage4B watch when price spikes before the bridge is confirmed.

## 24. Completion State
```text
completed_round = R1
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id = NUCLEAR_FINAL_CONTRACT_ENGINEERING_SERVICE_BRIDGE_VS_POLICY_HEADLINE_LEGAL_DELAY_HIGH_MAE
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 4
calibration_usable_case_count = 3
calibration_usable_trigger_count = 4
positive_case_count = 2
counterexample_count = 1
current_profile_error_count = 3
auto_selected_coverage_gap = C04 rows 6 -> 9 if accepted; still Priority 0, need 21 to 30
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
next_recommended_archetypes = C15_MATERIAL_SPREAD_SUPERCYCLE, C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN, C22_INSURANCE_RATE_CYCLE_RESERVE, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
```

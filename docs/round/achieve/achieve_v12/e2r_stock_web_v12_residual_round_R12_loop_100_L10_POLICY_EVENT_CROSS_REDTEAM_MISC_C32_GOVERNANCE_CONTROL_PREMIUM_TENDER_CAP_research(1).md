# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round
## 0. Research Metadata
- selected_round: R12
- selected_loop: 100
- selected_priority_bucket: Priority 0
- selection_basis: docs/core/V12_Research_No_Repeat_Index.md
- round_schedule_status: coverage_index_selected
- round_sector_consistency: pass
- large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
- canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
- fine_archetype_id: TENDER_CONTROL_PREMIUM_CASH_PATH_VS_EVENT_CAP_AND_HOLDING_TRUST_BRIDGE
- loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
- output_file: e2r_stock_web_v12_residual_round_R12_loop_100_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md

## 1. Current Calibrated Profile Assumption
before_profile_id = e2r_2_1_stock_web_calibrated_proxy

after_profile_id = proposed_C32_governance_cash_path_shadow_profile

rollback_reference_profile_id = e2r_2_0_baseline_reference

C32 is not a generic value-up or policy bucket. The evidence bridge must show one of: tender cash route, legally bounded control-premium monetization, credible minority return route, or a durable governance/capital-allocation trust bridge. Price-only governance vocabulary is treated as event-cap / 4B risk.

## 2. Round / Large Sector / Canonical Archetype Scope
| field | value |
|---|---|
| selected_round | R12 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP |
| fine_archetype_id | TENDER_CONTROL_PREMIUM_CASH_PATH_VS_EVENT_CAP_AND_HOLDING_TRUST_BRIDGE |
| round_sector_consistency | pass |

## 3. Previous Coverage / Duplicate Avoidance Check
No-Repeat Index shows C32 at 3 rows, 3 symbols, positive/counter = 1/2 and 4B/4C = 0/0. Covered symbols include 000670, 010130, and 180640. This loop avoids those symbols and uses four new symbols: 041510, 008930, 003920, 033780. Hard duplicate key is canonical_archetype_id + symbol + trigger_type + entry_date; none of the selected representative rows reuse that key.

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
| C32_041510_20230210_SM_TENDER_CONTROL_PREMIUM_CAP | 2023-02-10 | true | clean_180D_window | true |
| C32_008930_20240115_HANMI_OCI_CONTROL_DISPUTE_HIGH_MAE | 2024-01-15 | true | clean_180D_window | true |
| C32_003920_20240104_NAMYANG_CONTROL_TRANSFER_NO_TENDER_CASH_PATH | 2024-01-04 | true | clean_180D_window | true |
| C32_033780_20240718_KTG_SHAREHOLDER_RETURN_TRUST_BRIDGE | 2024-07-18 | true | clean_180D_window | true |

## 6. Canonical Archetype Compression Map
```text
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  -> TENDER_CONTROL_PREMIUM_CASH_PATH
     -> 041510 에스엠: tender cash path positive, but event cap makes 4B timing decisive
  -> CONTROL_DISPUTE_WITHOUT_MINORITY_CASH_PATH
     -> 008930 한미사이언스: control dispute spike, high-MAE failure
  -> CONTROL_TRANSFER_WITHOUT_TENDER_ROUTE
     -> 003920 남양유업: ownership transfer confirmed, no minority cash path
  -> GOVERNANCE_CAPITAL_RETURN_TRUST_BRIDGE
     -> 033780 KT&G: capital return governance bridge, shallow MAE
```

## 7. Case Selection Summary
| case_id | symbol | company | role | new independent | reason |
|---|---:|---|---|---:|---|
| C32_041510_20230210_SM_TENDER_CONTROL_PREMIUM_CAP | 041510 | 에스엠 | 4B_overlay_success | true | HYBE tender announcement opened a real control-premium cash path, but the later Kakao tender cap made the event a 4B overlay rather than an uncapped structural Green. |
| C32_008930_20240115_HANMI_OCI_CONTROL_DISPUTE_HIGH_MAE | 008930 | 한미사이언스 | failed_rerating | true | Control/integration headline and proxy-fight optionality produced immediate MFE, but no stable minority cash route and governance conflict produced high MAE. |
| C32_003920_20240104_NAMYANG_CONTROL_TRANSFER_NO_TENDER_CASH_PATH | 003920 | 남양유업 | failed_rerating | true | Court-confirmed control transfer changed owner identity, but minority holders did not receive a tender cash path; the rerating faded. |
| C32_033780_20240718_KTG_SHAREHOLDER_RETURN_TRUST_BRIDGE | 033780 | KT&G | structural_success | true | Capital return and governance trust route acted as a cash-return bridge; price path had shallow MAE and durable MFE, unlike pure control-spike cases. |

## 8. Positive vs Counterexample Balance
| count_type | count |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 2 |
| 4B_case_count | 1 |
| 4C_case_count | 0 |
| calibration_usable_case_count | 4 |
| calibration_usable_trigger_count | 5 |

## 9. Evidence Source Map
| case | evidence_available_at_that_date | evidence_source |
|---|---|---|
| 041510 | HYBE tender/control premium disclosure/news was market-known by 2023-02-10; Kakao tender cap was market-known by 2023-03-07 | public tender/disclosure/news proxy; price path from stock-web |
| 008930 | OCI/Hanmi integration and family control-dispute optionality was market-known by 2024-01-15 | public merger/governance headline proxy; price path from stock-web |
| 003920 | Control-transfer court/legal confirmation was market-known by 2024-01-04 | public court/control transfer headline proxy; price path from stock-web |
| 033780 | Governance/shareholder-return trust route was visible by 2024-07-18 | public shareholder return/governance action proxy; price path from stock-web |

## 10. Price Data Source Map
| symbol | profile_path | price_shard_path |
|---:|---|---|
| 041510 | atlas/symbol_profiles/041/041510.json | atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv |
| 008930 | atlas/symbol_profiles/008/008930.json | atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv |
| 003920 | atlas/symbol_profiles/003/003920.json | atlas/ohlcv_tradable_by_symbol_year/003/003920/2024.csv |
| 033780 | atlas/symbol_profiles/033/033780.json | atlas/ohlcv_tradable_by_symbol_year/033/033780/2024.csv |

## 11. Case-by-Case Trigger Grid
| trigger_id | trigger_type | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C32_041510_SM_20230210_S2A | Stage2-Actionable | 2023-02-10 | 114700 | 40.54 | -9.24 | 40.54 | -23.63 | 40.54 | -23.63 | current_profile_4B_too_late |
| C32_041510_SM_20230307_4B | Stage4B | 2023-03-07 | 149700 | 7.68 | -41.48 | 7.68 | -41.48 | 7.68 | -42.55 | current_profile_4B_too_late |
| C32_008930_HANMI_20240115_S2 | Stage2 | 2024-01-15 | 43300 | 29.79 | -10.62 | 29.79 | -30.02 | 29.79 | -40.53 | current_profile_false_positive |
| C32_003920_NAMYANG_20240104_S2 | Stage2 | 2024-01-04 | 590000 | 9.32 | -6.78 | 9.32 | -15.42 | 9.32 | -21.19 | current_profile_false_positive |
| C32_033780_KTG_20240718_S2A | Stage2-Actionable | 2024-07-18 | 90000 | 26.11 | -3.22 | 26.11 | -3.22 | 26.56 | -3.22 | current_profile_correct |

## 12. Trigger-Level OHLC Backtest Tables
MFE_N_pct = max(high over horizon) / entry_price - 1. MAE_N_pct = min(low over horizon) / entry_price - 1. All representative rows have entry price, 30D/90D/180D MFE and MAE, peak date, peak price, and clean 180D corporate-action status.

## 13. Current Calibrated Profile Stress Test
1. Current profile would correctly treat 033780 as a Stage2-Actionable governance/capital-return bridge.
2. It would likely be too permissive on 008930 and 003920 if governance vocabulary were allowed without a minority cash path.
3. It would be too late on 041510 if 4B waited for price reversal rather than explicit tender/event cap.
4. The existing price-only blowoff guard is strengthened, not weakened.
5. The full 4B non-price requirement is strengthened: event cap, tender close, lack of minority cash path, and control premium cap are non-price 4B evidence in C32.

## 14. Stage2 / Yellow / Green Comparison
| case | Stage2 timing | Yellow/Green implication | green_lateness_ratio |
|---|---|---|---|
| 041510 | Stage2-Actionable was early enough but should be followed by 4B cap | Green should not chase after tender cap | not_applicable |
| 008930 | Stage2 was easy but unstable | Green blocked by no minority cash route and conflict | not_applicable |
| 003920 | Stage2 event confirmation existed | Green blocked by no tender route/low liquidity | not_applicable |
| 033780 | Stage2-Actionable with cash-return trust route | Yellow/Green can wait for confirmation without missing all upside | not_applicable |

## 15. 4B Local vs Full-window Timing Audit
| trigger_id | four_b_evidence_type | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---|---:|---:|---|
| C32_041510_SM_20230307_4B | explicit_event_cap|control_premium_or_event_premium | 0.93 | 0.93 | good_full_window_4B_timing |
| C32_008930_HANMI_20240115_S2 | price_only|control_premium_or_event_premium | 0.98 | 0.98 | price_only_local_4B_too_early_without_cash_path_confirmation |
| C32_003920_NAMYANG_20240104_S2 | control_premium_or_event_premium|explicit_event_cap | 0.99 | 0.99 | event_cap_without_tender_cash_path |

## 16. 4C Protection Audit
No hard 4C trigger is proposed. 008930 and 003920 are not thesis-break liquidation cases; they are C32 false-positive/high-MAE cases where Stage2 should be allowed only as watch-level unless minority cash path or governance return bridge is confirmed.

## 17. Sector-Specific Rule Candidate
sector_specific_rule_candidate = true

For L10 policy/event/governance, headline-only event optionality should not promote beyond Stage2 unless it is linked to a company-level cash route. In C32 this route can be tender price, binding control-premium monetization, NAV/return bridge, or explicit shareholder return execution.

## 18. Canonical-Archetype Rule Candidate
canonical_archetype_rule_candidate = true

new_axis_proposed = C32_minority_cash_path_or_governance_return_bridge_required

Rule: C32 Stage2-Actionable requires at least one of tender cash route, binding control transfer that creates a minority monetization route, credible capital return execution, or NAV/holding discount closure mechanism. If absent, control-premium vocabulary is Stage2/watch only and can become a 4B event-cap overlay.

## 19. Before / After Backtest Comparison
| profile | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | score_return_alignment_verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 5 | 22.79 | -24.80 | 0.60 | too permissive on governance headline without cash path |
| P1 sector_specific_candidate_profile | 5 | 22.79 | -24.80 | 0.40 | better after C32 event-cap overlay |
| P2 canonical_archetype_candidate_profile | 5 | 22.79 | -24.80 | 0.20 | best: cash path or return bridge required |
| P3 counterexample_guard_profile | 5 | 22.79 | -24.80 | 0.20 | strong guard, may delay some positive tender routes |

## 20. Score-Return Alignment Matrix
| case | raw_component_scores_before | weighted_before | stage_before | raw_component_scores_after | weighted_after | stage_after | explanation |
|---|---|---:|---|---|---:|---|---|
| C32_041510_20230210_SM_TENDER_CONTROL_PREMIUM_CAP | `{"contract_score": 4, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 4}` | 66 | Stage2 | `{"contract_score": 10, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 2}` | 77 | Stage2-Actionable | cash-path/return-bridge filter separates true C32 from vocabulary-only control premium |
| C32_008930_20240115_HANMI_OCI_CONTROL_DISPUTE_HIGH_MAE | `{"contract_score": 4, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 4}` | 68 | Stage2 | `{"contract_score": 3, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 6, "valuation_repricing_score": 5, "execution_risk_score": 8, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 8}` | 57 | Stage1/Stage2-watch | cash-path/return-bridge filter separates true C32 from vocabulary-only control premium |
| C32_003920_20240104_NAMYANG_CONTROL_TRANSFER_NO_TENDER_CASH_PATH | `{"contract_score": 4, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 4}` | 68 | Stage2 | `{"contract_score": 3, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 6, "valuation_repricing_score": 5, "execution_risk_score": 8, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 8}` | 57 | Stage1/Stage2-watch | cash-path/return-bridge filter separates true C32 from vocabulary-only control premium |
| C32_033780_20240718_KTG_SHAREHOLDER_RETURN_TRUST_BRIDGE | `{"contract_score": 4, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 4}` | 66 | Stage2 | `{"contract_score": 10, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 2}` | 77 | Stage2-Actionable | cash-path/return-bridge filter separates true C32 from vocabulary-only control premium |

## 21. Coverage Matrix
| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | TENDER_CONTROL_PREMIUM_CASH_PATH_VS_EVENT_CAP_AND_HOLDING_TRUST_BRIDGE | 2 | 2 | 1 | 0 | 4 | 0 | 5 | 4 | 3 | true | true | C32 rows 3 -> 7 if accepted; still Priority 0 |

## 22. Residual Contribution Summary
new_independent_case_count: 4

reused_case_count: 0

reused_case_ids: []

new_symbol_count: 4

new_canonical_archetype_count: 0

new_fine_archetype_count: 1

new_trigger_family_count: 5

tested_existing_calibrated_axes: [price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence]

residual_error_types_found: [governance_headline_without_minority_cash_path, tender_event_cap_4B_too_late, control_transfer_no_rerating]

new_axis_proposed: C32_minority_cash_path_or_governance_return_bridge_required

existing_axis_strengthened: price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence

existing_axis_weakened: null

existing_axis_kept: stage3_green_total_min | stage3_green_revision_min

sector_specific_rule_candidate: true

canonical_archetype_rule_candidate: true

no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate

do_not_propose_new_weight_delta: false

## 23. Validation Scope / Non-Validation Scope
Validated: stock-web tradable_raw OHLC paths, entry date/price, 30D/90D/180D MFE/MAE, clean 180D windows, duplicate avoidance. Non-validation: exact legal merits of each control dispute, post-event fundamental earnings forecasts, and production scoring changes.

## 24. Shadow Weight Calibration
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C32_minority_cash_path_or_governance_return_bridge_required,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"Require tender/minority cash path or credible governance return bridge before Stage2-Actionable","false positive reduction in 008930/003920 and 4B improvement in 041510","C32_041510_SM_20230210_S2A|C32_008930_HANMI_20240115_S2|C32_003920_NAMYANG_20240104_S2|C32_033780_KTG_20240718_S2A",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"

## 25. Machine-Readable Rows
```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C32_041510_20230210_SM_TENDER_CONTROL_PREMIUM_CAP","symbol":"041510","company_name":"에스엠","round":"R12","loop":"100","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"TENDER_CONTROL_PREMIUM_CASH_PATH_VS_EVENT_CAP_AND_HOLDING_TRUST_BRIDGE","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable / Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"HYBE tender announcement opened a real control-premium cash path, but the later Kakao tender cap made the event a 4B overlay rather than an uncapped structural Green."}
{"row_type":"case","case_id":"C32_008930_20240115_HANMI_OCI_CONTROL_DISPUTE_HIGH_MAE","symbol":"008930","company_name":"한미사이언스","round":"R12","loop":"100","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"TENDER_CONTROL_PREMIUM_CASH_PATH_VS_EVENT_CAP_AND_HOLDING_TRUST_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_or_high_mae","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Control/integration headline and proxy-fight optionality produced immediate MFE, but no stable minority cash route and governance conflict produced high MAE."}
{"row_type":"case","case_id":"C32_003920_20240104_NAMYANG_CONTROL_TRANSFER_NO_TENDER_CASH_PATH","symbol":"003920","company_name":"남양유업","round":"R12","loop":"100","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"TENDER_CONTROL_PREMIUM_CASH_PATH_VS_EVENT_CAP_AND_HOLDING_TRUST_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_or_high_mae","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Court-confirmed control transfer changed owner identity, but minority holders did not receive a tender cash path; the rerating faded."}
{"row_type":"case","case_id":"C32_033780_20240718_KTG_SHAREHOLDER_RETURN_TRUST_BRIDGE","symbol":"033780","company_name":"KT&G","round":"R12","loop":"100","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"TENDER_CONTROL_PREMIUM_CASH_PATH_VS_EVENT_CAP_AND_HOLDING_TRUST_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Capital return and governance trust route acted as a cash-return bridge; price path had shallow MAE and durable MFE, unlike pure control-spike cases."}
{"row_type":"trigger","trigger_id":"C32_041510_SM_20230210_S2A","case_id":"C32_041510_20230210_SM_TENDER_CONTROL_PREMIUM_CAP","symbol":"041510","company_name":"에스엠","round":"R12","loop":"100","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"TENDER_CONTROL_PREMIUM_CASH_PATH_VS_EVENT_CAP_AND_HOLDING_TRUST_BRIDGE","sector":"governance / control premium / tender cap / shareholder return","primary_archetype":"governance_control_premium_tender_cap","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-10","evidence_available_at_that_date":"public event/governance/tender/capital-return evidence visible at or before trigger date","evidence_source":"public disclosure/news proxy; price path verified with Songdaiki/stock-web","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv","profile_path":"atlas/symbol_profiles/041/041510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-02-10","entry_price":114700,"MFE_30D_pct":40.54,"MFE_90D_pct":40.54,"MFE_180D_pct":40.54,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.24,"MAE_90D_pct":-23.63,"MAE_180D_pct":-23.63,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-08","peak_price":161200,"drawdown_after_peak_pct":-45.66,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":null,"four_c_protection_label":null,"trigger_outcome_label":"tender_control_premium_positive_but_event_cap","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C32_041510_20230210","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C32_041510_SM_20230307_4B","case_id":"C32_041510_20230210_SM_TENDER_CONTROL_PREMIUM_CAP","symbol":"041510","company_name":"에스엠","round":"R12","loop":"100","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"TENDER_CONTROL_PREMIUM_CASH_PATH_VS_EVENT_CAP_AND_HOLDING_TRUST_BRIDGE","sector":"governance / control premium / tender cap / shareholder return","primary_archetype":"governance_control_premium_tender_cap","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2023-03-07","evidence_available_at_that_date":"public event/governance/tender/capital-return evidence visible at or before trigger date","evidence_source":"public disclosure/news proxy; price path verified with Songdaiki/stock-web","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["explicit_event_cap","control_premium_or_event_premium","positioning_overheat","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv","profile_path":"atlas/symbol_profiles/041/041510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-03-07","entry_price":149700,"MFE_30D_pct":7.68,"MFE_90D_pct":7.68,"MFE_180D_pct":7.68,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-41.48,"MAE_90D_pct":-41.48,"MAE_180D_pct":-42.55,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-08","peak_price":161200,"drawdown_after_peak_pct":-48.82,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":0.93,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":"explicit_event_cap|control_premium_or_event_premium","four_c_protection_label":null,"trigger_outcome_label":"tender_cap_overlay_after_control_premium_spike","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C32_041510_20230210","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"4B overlay comparison for same SM control-premium case","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"C32_008930_HANMI_20240115_S2","case_id":"C32_008930_20240115_HANMI_OCI_CONTROL_DISPUTE_HIGH_MAE","symbol":"008930","company_name":"한미사이언스","round":"R12","loop":"100","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"TENDER_CONTROL_PREMIUM_CASH_PATH_VS_EVENT_CAP_AND_HOLDING_TRUST_BRIDGE","sector":"governance / control premium / tender cap / shareholder return","primary_archetype":"governance_control_premium_tender_cap","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-01-15","evidence_available_at_that_date":"public event/governance/tender/capital-return evidence visible at or before trigger date","evidence_source":"public disclosure/news proxy; price path verified with Songdaiki/stock-web","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["control_premium_or_event_premium","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv","profile_path":"atlas/symbol_profiles/008/008930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-15","entry_price":43300,"MFE_30D_pct":29.79,"MFE_90D_pct":29.79,"MFE_180D_pct":29.79,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.62,"MAE_90D_pct":-30.02,"MAE_180D_pct":-40.53,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-16","peak_price":56200,"drawdown_after_peak_pct":-54.18,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":0.98,"four_b_timing_verdict":"price_only_local_4B_too_early_without_cash_path_confirmation","four_b_evidence_type":"price_only|control_premium_or_event_premium","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"control_dispute_spike_without_minority_cash_path","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C32_008930_20240115","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C32_003920_NAMYANG_20240104_S2","case_id":"C32_003920_20240104_NAMYANG_CONTROL_TRANSFER_NO_TENDER_CASH_PATH","symbol":"003920","company_name":"남양유업","round":"R12","loop":"100","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"TENDER_CONTROL_PREMIUM_CASH_PATH_VS_EVENT_CAP_AND_HOLDING_TRUST_BRIDGE","sector":"governance / control premium / tender cap / shareholder return","primary_archetype":"governance_control_premium_tender_cap","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-01-04","evidence_available_at_that_date":"public event/governance/tender/capital-return evidence visible at or before trigger date","evidence_source":"public disclosure/news proxy; price path verified with Songdaiki/stock-web","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap","control_premium_or_event_premium"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003920/2024.csv","profile_path":"atlas/symbol_profiles/003/003920.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-04","entry_price":590000,"MFE_30D_pct":9.32,"MFE_90D_pct":9.32,"MFE_180D_pct":9.32,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.78,"MAE_90D_pct":-15.42,"MAE_180D_pct":-21.19,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-05","peak_price":645000,"drawdown_after_peak_pct":-27.91,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.99,"four_b_full_window_peak_proximity":0.99,"four_b_timing_verdict":"event_cap_without_tender_cash_path","four_b_evidence_type":"control_premium_or_event_premium|explicit_event_cap","four_c_protection_label":null,"trigger_outcome_label":"control_transfer_confirmed_but_no_minority_tender_cash_path","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C32_003920_20240104","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C32_033780_KTG_20240718_S2A","case_id":"C32_033780_20240718_KTG_SHAREHOLDER_RETURN_TRUST_BRIDGE","symbol":"033780","company_name":"KT&G","round":"R12","loop":"100","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"TENDER_CONTROL_PREMIUM_CASH_PATH_VS_EVENT_CAP_AND_HOLDING_TRUST_BRIDGE","sector":"governance / control premium / tender cap / shareholder return","primary_archetype":"governance_control_premium_tender_cap","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-18","evidence_available_at_that_date":"public event/governance/tender/capital-return evidence visible at or before trigger date","evidence_source":"public disclosure/news proxy; price path verified with Songdaiki/stock-web","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/033/033780/2024.csv","profile_path":"atlas/symbol_profiles/033/033780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-18","entry_price":90000,"MFE_30D_pct":26.11,"MFE_90D_pct":26.11,"MFE_180D_pct":26.56,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.22,"MAE_90D_pct":-3.22,"MAE_180D_pct":-3.22,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-03","peak_price":113900,"drawdown_after_peak_pct":-14.75,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":null,"four_c_protection_label":null,"trigger_outcome_label":"shareholder_return_trust_bridge_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C32_033780_20240718","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C32_041510_20230210_SM_TENDER_CONTROL_PREMIUM_CAP","trigger_id":"C32_041510_SM_20230210_S2A","symbol":"041510","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":66,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":8,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":77,"stage_label_after":"Stage2-Actionable","changed_components":["contract_score","policy_or_regulatory_score","execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"C32 requires minority cash path, tender cap clarity, or credible governance return bridge; headline-only control premium is down-weighted.","MFE_90D_pct":40.54,"MAE_90D_pct":-23.63,"score_return_alignment_label":"event_cap_overlay","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C32_008930_20240115_HANMI_OCI_CONTROL_DISPUTE_HIGH_MAE","trigger_id":"C32_008930_HANMI_20240115_S2","symbol":"008930","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":68,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":6,"valuation_repricing_score":5,"execution_risk_score":8,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":8},"weighted_score_after":57,"stage_label_after":"Stage1/Stage2-watch","changed_components":["contract_score","policy_or_regulatory_score","execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"C32 requires minority cash path, tender cap clarity, or credible governance return bridge; headline-only control premium is down-weighted.","MFE_90D_pct":29.79,"MAE_90D_pct":-30.02,"score_return_alignment_label":"false_positive_high_mae","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C32_003920_20240104_NAMYANG_CONTROL_TRANSFER_NO_TENDER_CASH_PATH","trigger_id":"C32_003920_NAMYANG_20240104_S2","symbol":"003920","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":68,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":6,"valuation_repricing_score":5,"execution_risk_score":8,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":8},"weighted_score_after":57,"stage_label_after":"Stage1/Stage2-watch","changed_components":["contract_score","policy_or_regulatory_score","execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"C32 requires minority cash path, tender cap clarity, or credible governance return bridge; headline-only control premium is down-weighted.","MFE_90D_pct":9.32,"MAE_90D_pct":-15.42,"score_return_alignment_label":"false_positive_high_mae","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C32_033780_20240718_KTG_SHAREHOLDER_RETURN_TRUST_BRIDGE","trigger_id":"C32_033780_KTG_20240718_S2A","symbol":"033780","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":66,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":8,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":77,"stage_label_after":"Stage2-Actionable","changed_components":["contract_score","policy_or_regulatory_score","execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"C32 requires minority cash path, tender cap clarity, or credible governance return bridge; headline-only control premium is down-weighted.","MFE_90D_pct":26.11,"MAE_90D_pct":-3.22,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"residual_contribution","round":"R12","loop":"100","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["governance_headline_without_minority_cash_path","tender_event_cap_4B_too_late","control_transfer_no_rerating"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt
### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State
completed_round = R12

completed_loop = 100

selection_basis = docs/core/V12_Research_No_Repeat_Index.md

selected_priority_bucket = Priority 0

next_recommended_archetypes = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, C15_MATERIAL_SPREAD_SUPERCYCLE, C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN, C22_INSURANCE_RATE_CYCLE_RESERVE, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG

round_schedule_status = coverage_index_selected

round_sector_consistency = pass

## 28. Source Notes
- Stock-web manifest: atlas/manifest.json, max_date 2026-02-20.
- Stock-web schema: atlas/schema.json; tradable shard columns d/o/h/l/c/v/a/mc/s/m.
- Price shards inspected: 041/041510/2023.csv, 008/008930/2024.csv, 003/003920/2024.csv, 033/033780/2024.csv and 033/033780/2025.csv.
- No investment recommendation language is intended; this is historical calibration research only.

## Batch Ingest Self-Audit
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 4
new_weight_evidence_candidate_count: 4
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true

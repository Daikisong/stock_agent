# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R2
scheduled_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id = ADVANCED_AI_SEMI_EQUIPMENT_RERATING_VS_VALUATION_THEME_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R2_loop_88_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md
```

This loop continues loop 88 after R1. It adds 3 C09 cases: one advanced-equipment positive rerating case and two valuation/theme event-cap guardrail cases.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R2
scheduled_loop = 88
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
round_sector_consistency = pass
computed_next_round = R3
computed_next_loop = 88
```

R2 permits L2 AI/semiconductor/electronics research. C09 is the advanced-equipment valuation blowoff bucket. This loop separates real customer/order/revision rerating from advanced-equipment or EUV theme premium that should be capped as 4B/watch.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF = 17 rows / 11 symbols / good-bad Stage2 7-3 / 4B-4C 1-0
top covered symbols include 322310(3), 348210(3), 089030(2), 140860(2), 031980(1), 064290(1)
```

Selected rows:

```text
039030 / Stage2-Actionable / 2024-01-19
140860 / Stage2-Actionable / 2024-01-22
101490 / Stage4B / 2024-03-13
```

The 140860 row has soft-duplicate risk because the symbol appears in the C09 top list. It is retained only as a different false-Stage2 trigger family with reduced independent evidence weight.

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| manifest | atlas/manifest.json |
| stock_web_manifest_max_date | 2026-02-20 |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |

| symbol | profile path | CA window status |
|---|---|---|
| 039030 | atlas/symbol_profiles/039/039030.json | selected 2024 window clean; CA candidate is 2003-02-03 |
| 140860 | atlas/symbol_profiles/140/140860.json | no corporate-action candidate |
| 101490 | atlas/symbol_profiles/101/101490.json | selected 2024 window clean; CA candidate is 2009-04-30 |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R2L88_C09_EOTECH_2024_ADVANCED_EQUIPMENT_RERATING_POSITIVE | 039030 | 2024-01-19 | yes | 180 | yes | yes | true |
| R2L88_C09_PARKSYSTEMS_2024_ADVANCED_TOOL_VALUATION_FALSE_STAGE2 | 140860 | 2024-01-22 | yes | 180 | yes | yes | true |
| R2L88_C09_SNSTECH_2024_EUV_MASK_EVENT_CAP_4B | 101490 | 2024-03-13 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | ADVANCED_EQUIPMENT_CUSTOMER_ORDER_BRIDGE | Positive Stage2 requires customer/process relevance plus order/revision bridge. |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | ADVANCED_TOOL_QUALITY_FALSE_STAGE2 | High-quality advanced tool premium alone can produce weak MFE / high MAE false positives. |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | EUV_MASK_THEME_EVENT_CAP | EUV/advanced supply-chain theme spike should route to 4B unless bridge is verified. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R2L88_C09_EOTECH_2024_ADVANCED_EQUIPMENT_RERATING_POSITIVE | 039030 | 이오테크닉스 | positive | Customer/process equipment bridge produced high MFE90 with moderate MAE. |
| R2L88_C09_PARKSYSTEMS_2024_ADVANCED_TOOL_VALUATION_FALSE_STAGE2 | 140860 | 파크시스템스 | counterexample | Advanced-tool quality premium had weak MFE and material MAE. |
| R2L88_C09_SNSTECH_2024_EUV_MASK_EVENT_CAP_4B | 101490 | 에스앤에스텍 | counterexample / 4B | EUV mask theme premium capped quickly and drew down. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
```

## 9. Evidence Source Map

| case | evidence status | evidence_url_pending | source_proxy_only | usage |
|---|---|---|---|---|
| Eo Technics advanced-equipment rerating | historical public/report proxy | true | true | shadow-only positive |
| Park Systems valuation false Stage2 | historical public/report proxy | true | true | false-Stage2 guardrail |
| S&S Tech EUV mask event cap | historical public/report proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 039030 | atlas/ohlcv_tradable_by_symbol_year/039/039030/2024.csv | atlas/symbol_profiles/039/039030.json |
| 140860 | atlas/ohlcv_tradable_by_symbol_year/140/140860/2024.csv | atlas/symbol_profiles/140/140860.json |
| 101490 | atlas/ohlcv_tradable_by_symbol_year/101/101490/2024.csv | atlas/symbol_profiles/101/101490.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R2L88_C09_EOTECH_2024_STAGE2_ACTIONABLE_ADVANCED_EQUIPMENT_RERATING | 039030 | Stage2-Actionable | 2024-01-19 | 183900 | positive | advanced-equipment bridge worked |
| R2L88_C09_PARKSYSTEMS_2024_STAGE2_FALSE_POSITIVE_VALUATION_PREMIUM | 140860 | Stage2-Actionable | 2024-01-22 | 187800 | counterexample | quality/valuation premium without bridge |
| R2L88_C09_SNSTECH_2024_STAGE4B_EUV_MASK_VALUATION_EVENT_CAP | 101490 | Stage4B | 2024-03-13 | 48500 | counterexample/4B | EUV mask event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R2L88_C09_EOTECH_2024_STAGE2_ACTIONABLE_ADVANCED_EQUIPMENT_RERATING | 183900 | 18.27 | -11.15 | 52.80 | -11.15 | 52.80 | -11.15 | 2024-04-12 | 281000 | -39.36 |
| R2L88_C09_PARKSYSTEMS_2024_STAGE2_FALSE_POSITIVE_VALUATION_PREMIUM | 187800 | 3.78 | -15.66 | 3.78 | -19.60 | 7.30 | -20.39 | 2024-10-04 | 201500 | -20.40 |
| R2L88_C09_SNSTECH_2024_STAGE4B_EUV_MASK_VALUATION_EVENT_CAP | 48500 | 1.86 | -14.85 | 1.86 | -27.94 | 1.86 | -29.90 | 2024-03-13 | 49400 | -31.17 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C09 Stage2 needs customer/process/order/revision bridge |
| local_4b_watch_guard | strengthen: EUV/advanced-equipment theme premium should route to 4B watch |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is Stage2/4B quality:

| symbol | stage quality | explanation |
|---|---|---|
| 039030 | good_stage2 | Advanced equipment bridge produced strong MFE90. |
| 140860 | bad_stage2 | Advanced-tool quality premium was not enough without order/revision bridge. |
| 101490 | good_4B | EUV mask premium capped quickly and drew down. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 101490 EUV mask event cap | 1.00 | 1.00 | good_full_window_4B_timing_EUV_mask_theme_event_cap |
| 140860 advanced-tool premium | 0.04 | 0.07 | weak_MFE_high_MAE_false_stage2_advanced_tool_quality_premium |
| 039030 advanced-equipment bridge | n/a | n/a | positive Stage2; later valuation watch only |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for event-cap rows
```

No hard 4C candidate is proposed. C09 residual here is Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L2 advanced semiconductor equipment, Stage2 requires customer/process relevance plus order/revision bridge. Advanced-equipment label, EUV/HBM/AI theme, or valuation premium alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
rule = C09 should split customer/order bridge positives from valuation/theme premium caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 19.48 | -19.56 | 0.67 | mixed; C09 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 19.48 | -19.56 | 0.67 | weaker theme/valuation guard |
| P1 sector_specific_candidate_profile | L2 bridge required | 2 | 28.29 | -15.38 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C09 bridge vs valuation cap split | 2 | 28.29 | -15.38 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject valuation/theme caps as positive | 1 | 52.80 | -11.15 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 039030 advanced equipment bridge | 66 | Stage2-Watch | 73 | Stage2-Actionable | 52.80 | -11.15 | advanced_equipment_customer_bridge_positive |
| 140860 advanced tool premium | 67 | Stage2-Actionable | 55 | Stage1/Watch | 3.78 | -19.60 | advanced_tool_quality_without_order_bridge_false_stage2 |
| 101490 EUV mask premium | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 1.86 | -27.94 | EUV_mask_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_AI_SEMI_EQUIPMENT_RERATING_VS_VALUATION_THEME_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C09 advanced-equipment customer/order bridge positive vs advanced-tool/EUV theme valuation-cap guardrails."}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: advanced_equipment_label_without_customer_order_bridge, valuation_premium_false_stage2, EUV_mask_theme_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-web tradable raw OHLC path
- entry_date / entry_price
- MFE/MAE 30D/90D/180D
- corporate-action window cleanliness
- C09 advanced-equipment bridge vs valuation/theme cap split
```

Non-validation scope:

```text
- Exact as-of evidence URLs remain pending for all selected cases.
- No production scoring update.
- No live candidate scan.
- No investment recommendation.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,configured,advanced_equipment_requires_customer_order_revision_bridge,0,"C09 Stage2 needs customer/process/order/revision bridge, not advanced-equipment label or AI theme premium alone","Eo Technics worked; Park Systems and S&S Tech event/premium rows failed positive-stage promotion","R2L88_C09_EOTECH_2024_STAGE2_ACTIONABLE_ADVANCED_EQUIPMENT_RERATING|R2L88_C09_PARKSYSTEMS_2024_STAGE2_FALSE_POSITIVE_VALUATION_PREMIUM|R2L88_C09_SNSTECH_2024_STAGE4B_EUV_MASK_VALUATION_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,configured,cap_advanced_theme_premium_as_4B_watch,0,"Advanced equipment/EUV valuation premiums can peak early with weak MFE90 and high MAE90","S&S Tech 2024 had full-window 4B behavior; Park Systems showed weak-MFE/high-MAE false Stage2 behavior","R2L88_C09_PARKSYSTEMS_2024_STAGE2_FALSE_POSITIVE_VALUATION_PREMIUM|R2L88_C09_SNSTECH_2024_STAGE4B_EUV_MASK_VALUATION_EVENT_CAP",2,2,2,low,guardrail_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R2L88_C09_EOTECH_2024_ADVANCED_EQUIPMENT_RERATING_POSITIVE", "symbol": "039030", "company_name": "이오테크닉스", "round": "R2", "loop": "88", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_AI_SEMI_EQUIPMENT_RERATING_VS_VALUATION_THEME_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R2L88_C09_EOTECH_2024_STAGE2_ACTIONABLE_ADVANCED_EQUIPMENT_RERATING", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Advanced semiconductor equipment rerating worked when customer/process relevance and order/revision bridge were plausible; MFE90 was high with moderate MAE.", "current_profile_verdict": "current_profile_kept_but_requires_customer_order_bridge_not_AI_equipment_label_only", "price_source": "Songdaiki/stock-web", "notes": "Source-proxy only; exact as-of report/disclosure URLs remain pending, so no production weight delta."}
{"row_type": "case", "case_id": "R2L88_C09_PARKSYSTEMS_2024_ADVANCED_TOOL_VALUATION_FALSE_STAGE2", "symbol": "140860", "company_name": "파크시스템스", "round": "R2", "loop": "88", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_AI_SEMI_EQUIPMENT_RERATING_VS_VALUATION_THEME_EVENT_CAP", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R2L88_C09_PARKSYSTEMS_2024_STAGE2_FALSE_POSITIVE_VALUATION_PREMIUM", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "C09 top-covered symbol has prior rows, but this is a different trigger family / high-MAE false Stage2 review.", "independent_evidence_weight": 0.5, "score_price_alignment": "Advanced-tool quality alone did not justify positive-stage promotion from the January spike; weak 90D MFE and material MAE require bridge tightening.", "current_profile_verdict": "current_profile_false_positive_if_advanced_equipment_quality_counts_without_order_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Soft duplicate risk acknowledged; retained only as false Stage2 / guardrail evidence."}
{"row_type": "case", "case_id": "R2L88_C09_SNSTECH_2024_EUV_MASK_EVENT_CAP_4B", "symbol": "101490", "company_name": "에스앤에스텍", "round": "R2", "loop": "88", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_AI_SEMI_EQUIPMENT_RERATING_VS_VALUATION_THEME_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R2L88_C09_SNSTECH_2024_STAGE4B_EUV_MASK_VALUATION_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "EUV/advanced mask theme spike capped quickly; almost no forward MFE and deep MAE indicate 4B watch, not structural Green.", "current_profile_verdict": "current_profile_4B_too_late_if_EUV_mask_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "New C09 symbol; source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R2L88_C09_EOTECH_2024_STAGE2_ACTIONABLE_ADVANCED_EQUIPMENT_RERATING", "case_id": "R2L88_C09_EOTECH_2024_ADVANCED_EQUIPMENT_RERATING_POSITIVE", "symbol": "039030", "company_name": "이오테크닉스", "round": "R2", "loop": "88", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_AI_SEMI_EQUIPMENT_RERATING_VS_VALUATION_THEME_EVENT_CAP", "sector": "AI_semiconductor_advanced_equipment", "primary_archetype": "advanced_laser_process_equipment_customer_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-19", "entry_date": "2024-01-19", "entry_price": 183900.0, "evidence_available_at_that_date": "advanced process equipment / AI semi customer bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["advanced_process_equipment", "customer_process_relevance", "order_revision_bridge_proxy", "relative_strength"], "stage3_evidence_fields": ["high_MFE90", "continued_equipment_rerating"], "stage4b_evidence_fields": ["valuation_repricing_watch_after_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/039/039030/2024.csv", "profile_path": "atlas/symbol_profiles/039/039030.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 18.27, "MFE_90D_pct": 52.8, "MFE_180D_pct": 52.8, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -11.15, "MAE_90D_pct": -11.15, "MAE_180D_pct": -11.15, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-12", "peak_price": 281000.0, "drawdown_after_peak_pct": -39.36, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_valuation_watch_needed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_advanced_equipment_rerating_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R2L88_C09_039030_2024-01-19_183900", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R2L88_C09_PARKSYSTEMS_2024_STAGE2_FALSE_POSITIVE_VALUATION_PREMIUM", "case_id": "R2L88_C09_PARKSYSTEMS_2024_ADVANCED_TOOL_VALUATION_FALSE_STAGE2", "symbol": "140860", "company_name": "파크시스템스", "round": "R2", "loop": "88", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_AI_SEMI_EQUIPMENT_RERATING_VS_VALUATION_THEME_EVENT_CAP", "sector": "AI_semiconductor_advanced_metrology", "primary_archetype": "advanced_tool_quality_valuation_without_order_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-22", "entry_date": "2024-01-22", "entry_price": 187800.0, "evidence_available_at_that_date": "advanced metrology/tool quality premium proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["advanced_tool_quality", "relative_strength_spike", "AI_equipment_premium"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE90", "high_MAE90", "order_revision_bridge_missing"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/140/140860/2024.csv", "profile_path": "atlas/symbol_profiles/140/140860.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.78, "MFE_90D_pct": 3.78, "MFE_180D_pct": 7.3, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -15.66, "MAE_90D_pct": -19.6, "MAE_180D_pct": -20.39, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-04", "peak_price": 201500.0, "drawdown_after_peak_pct": -20.4, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.04, "four_b_full_window_peak_proximity": 0.07, "four_b_timing_verdict": "weak_MFE_high_MAE_false_stage2_advanced_tool_quality_premium", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "bad_stage2_advanced_equipment_quality_without_bridge", "current_profile_verdict": "current_profile_false_positive_if_quality_premium_counts_without_order_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R2L88_C09_140860_2024-01-22_187800", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same symbol appears in C09 top-covered list, but this row is a new false-Stage2 trigger family", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R2L88_C09_SNSTECH_2024_STAGE4B_EUV_MASK_VALUATION_EVENT_CAP", "case_id": "R2L88_C09_SNSTECH_2024_EUV_MASK_EVENT_CAP_4B", "symbol": "101490", "company_name": "에스앤에스텍", "round": "R2", "loop": "88", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_AI_SEMI_EQUIPMENT_RERATING_VS_VALUATION_THEME_EVENT_CAP", "sector": "EUV_mask_advanced_material_equipment", "primary_archetype": "EUV_mask_theme_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-03-13", "entry_date": "2024-03-13", "entry_price": 48500.0, "evidence_available_at_that_date": "EUV mask / advanced semiconductor theme premium proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["EUV_mask_theme", "advanced_process_supply_chain", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/101/101490/2024.csv", "profile_path": "atlas/symbol_profiles/101/101490.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.86, "MFE_90D_pct": 1.86, "MFE_180D_pct": 1.86, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -14.85, "MAE_90D_pct": -27.94, "MAE_180D_pct": -29.9, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-13", "peak_price": 49400.0, "drawdown_after_peak_pct": -31.17, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_EUV_mask_theme_event_cap", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_EUV_mask_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R2L88_C09_101490_2024-03-13_48500", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L88_C09_EOTECH_2024_ADVANCED_EQUIPMENT_RERATING_POSITIVE", "trigger_id": "R2L88_C09_EOTECH_2024_STAGE2_ACTIONABLE_ADVANCED_EQUIPMENT_RERATING", "symbol": "039030", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 35, "margin_bridge_score": 25, "revision_score": 35, "relative_strength_score": 75, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 50, "margin_bridge_score": 45, "revision_score": 50, "relative_strength_score": 70, "customer_quality_score": 45, "policy_or_regulatory_score": 0, "valuation_repricing_score": 55, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable", "changed_components": ["customer_quality_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "advanced_equipment_customer_bridge_positive", "MFE_90D_pct": 52.8, "MAE_90D_pct": -11.15, "score_return_alignment_label": "advanced_equipment_customer_bridge_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L88_C09_PARKSYSTEMS_2024_ADVANCED_TOOL_VALUATION_FALSE_STAGE2", "trigger_id": "R2L88_C09_PARKSYSTEMS_2024_STAGE2_FALSE_POSITIVE_VALUATION_PREMIUM", "symbol": "140860", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 35, "margin_bridge_score": 25, "revision_score": 35, "relative_strength_score": 75, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 67, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 35, "customer_quality_score": 25, "policy_or_regulatory_score": 0, "valuation_repricing_score": 35, "execution_risk_score": 75, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 55, "stage_label_after": "Stage1/Watch", "changed_components": ["customer_quality_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "advanced_tool_quality_without_order_bridge_false_stage2", "MFE_90D_pct": 3.78, "MAE_90D_pct": -19.6, "score_return_alignment_label": "advanced_tool_quality_without_order_bridge_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_quality_premium_counts_without_order_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L88_C09_SNSTECH_2024_EUV_MASK_EVENT_CAP_4B", "trigger_id": "R2L88_C09_SNSTECH_2024_STAGE4B_EUV_MASK_VALUATION_EVENT_CAP", "symbol": "101490", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 35, "margin_bridge_score": 25, "revision_score": 35, "relative_strength_score": 75, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 35, "customer_quality_score": 25, "policy_or_regulatory_score": 0, "valuation_repricing_score": 35, "execution_risk_score": 75, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["customer_quality_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "EUV_mask_event_cap_4B_guard", "MFE_90D_pct": 1.86, "MAE_90D_pct": -27.94, "score_return_alignment_label": "EUV_mask_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_EUV_mask_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R2", "loop": "88", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_AI_SEMI_EQUIPMENT_RERATING_VS_VALUATION_THEME_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["advanced_equipment_label_without_customer_order_bridge", "valuation_premium_false_stage2", "EUV_mask_theme_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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

```text
completed_round = R2
completed_loop = 88
next_round = R3
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.

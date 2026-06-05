# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R9
scheduled_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = TIRE_VOLUME_COST_MARGIN_BRIDGE_VS_FACTORY_FIRE_OPERATIONAL_BREAK_FALSE_4C
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R9_loop_87_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
```

This loop adds 3 new independent C29 tire/mobility cases, 2 counterexamples, and 2 current-profile residual errors for R9 / L3 / C29.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
```

Existing calibrated axes tested rather than globally reproposed:

```text
stage2_actionable_evidence_bonus = existing_axis_kept
stage2_required_bridge = existing_axis_strengthened_by_C29_margin_bridge_filter
hard_4c_thesis_break_routes_to_4c = existing_axis_weakened_for_one_off_operational_shock_without_durable_capacity_break
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R9
scheduled_loop = 87
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
round_sector_consistency = pass
computed_next_round = R10
computed_next_loop = 87
```

R9 permits mobility/transport style research. C29 maps to mobility volume / mix / margin operating leverage. This loop narrows C29 to tire makers where the correct bridge is not “auto theme + price strength” but **volume recovery + raw-material cost relief + margin conversion**, with a separate guard for one-off factory-fire 4C false breaks.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat screening used the hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected rows avoid the already-heavy C29 repeated symbols in the index by adding a tire-specific trigger-family split:

```text
new symbols = 002350, 073240
new trigger families =
- tire_volume_cost_margin_bridge
- tire_margin_rebound_false_stage2
- operational_shock_false_hard_4c
```

The 073240 symbol appears twice, but the 2025 row is allowed as a new trigger family / 4C false-break path, not as a duplicated Stage2 entry.

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
| symbol_profile_root | atlas/symbol_profiles |
| tradable_row_count | 14354401 |
| symbol_count | 5414 |

Corporate action windows:

| symbol | profile | corporate_action_candidate_dates | 180D window status |
|---|---|---|---|
| 073240 | atlas/symbol_profiles/073/073240.json | 2010-11-02; 2010-12-14; 2018-07-20 | clean for 2023 and 2025 windows |
| 002350 | atlas/symbol_profiles/002/002350.json | 1999-02-18; 1999-06-08; 1999-06-10; 2008-03-21 | clean for 2023 window |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in tradable shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R9L87_C29_KUMHO_2023_MARGIN_BRIDGE | 073240 | 2023-03-31 | yes | 180 | yes | yes | true |
| R9L87_C29_NEXEN_2023_HIGH_MAE_FALSE_STAGE2 | 002350 | 2023-05-15 | yes | 180 | yes | yes | true |
| R9L87_C29_KUMHO_2025_FACTORY_FIRE_FALSE_4C | 073240 | 2025-05-19 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep sub-archetype | compression rule |
|---|---|---|
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | TIRE_VOLUME_COST_MARGIN_BRIDGE | Positive Stage2 only when tire volume, raw material cost relief, utilization/mix, and margin conversion are visible. |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | TIRE_MARGIN_REBOUND_FALSE_STAGE2 | Headline rebound / price spike without durable bridge is high-MAE Stage2 false positive. |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | FACTORY_FIRE_OPERATIONAL_BREAK_FALSE_4C | One-off factory fire should be watch/4B/4C only when durable capacity loss, order loss, or guidance revision is confirmed. |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger family | reason selected |
|---|---|---|---|---|---|
| R9L87_C29_KUMHO_2023_MARGIN_BRIDGE | 073240 | 금호타이어 | positive | tire_volume_cost_margin_bridge | Strong MFE with low MAE after margin bridge entry. |
| R9L87_C29_NEXEN_2023_HIGH_MAE_FALSE_STAGE2 | 002350 | 넥센타이어 | counterexample | tire_margin_rebound_false_stage2 | Stage2-like spike failed; high 180D MAE. |
| R9L87_C29_KUMHO_2025_FACTORY_FIRE_FALSE_4C | 073240 | 금호타이어 | counterexample / 4C false break | operational_shock_false_hard_4c | Verified factory fire shock recovered strongly; hard 4C too aggressive without durable break confirmation. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 0
4C_case_count = 1
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
```

Balance is counterexample-heavy by design because C29 already has broad coverage and this loop targets residual false positives / false 4C rather than another auto-parts positive confirmation.

## 9. Evidence Source Map

| case | evidence source status | evidence_url_pending | source_proxy_only | note |
|---|---|---|---|---|
| Kumho 2023 margin bridge | source proxy | true | true | Exact as-of report/disclosure URL pending; usable for shadow only. |
| Nexen 2023 high-MAE false Stage2 | source proxy | true | true | Exact as-of report URL pending; usable as counterexample shadow only. |
| Kumho 2025 factory fire | verified public news | false | false | Reuters-reported factory fire, output capacity shock, stock reaction. |

## 10. Price Data Source Map

| symbol | shard(s) | profile |
|---|---|---|
| 073240 | atlas/ohlcv_tradable_by_symbol_year/073/073240/2023.csv; 2025.csv; 2026.csv | atlas/symbol_profiles/073/073240.json |
| 002350 | atlas/ohlcv_tradable_by_symbol_year/002/002350/2023.csv | atlas/symbol_profiles/002/002350.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | role | current_profile_verdict |
|---|---|---|---:|---:|---:|---|---|
| R9L87_C29_KUMHO_2023_STAGE2_ACTIONABLE_MARGIN_BRIDGE | 073240 | Stage2-Actionable | 2023-03-31 | 2023-03-31 | 3740 | positive | kept but source-proxy blocks positive delta |
| R9L87_C29_NEXEN_2023_STAGE2_FALSE_POSITIVE_HIGH_MAE | 002350 | Stage2-Actionable | 2023-05-15 | 2023-05-15 | 9290 | counterexample | false positive if Stage2 bonus ignores post-spike MAE |
| R9L87_C29_KUMHO_2025_STAGE4C_FALSE_BREAK_FACTORY_FIRE | 073240 | Stage4C | 2025-05-17 | 2025-05-19 | 4445 | counterexample | hard 4C too hard without durable thesis-break confirmation |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R9L87_C29_KUMHO_2023_STAGE2_ACTIONABLE_MARGIN_BRIDGE | 3740 | 41.18 | -6.42 | 41.18 | -6.42 | 56.42 | -6.42 | 2023-11-23 | 5850 | -14.19 |
| R9L87_C29_NEXEN_2023_STAGE2_FALSE_POSITIVE_HIGH_MAE | 9290 | 0.11 | -19.59 | 0.11 | -19.59 | 0.11 | -26.16 | 2023-05-15 | 9300 | -26.24 |
| R9L87_C29_KUMHO_2025_STAGE4C_FALSE_BREAK_FACTORY_FIRE | 4445 | 6.64 | -6.64 | 15.64 | -6.64 | 72.10 | -6.64 | 2026-02-11 | 7650 | -11.11 |

## 13. Current Calibrated Profile Stress Test

| axis | verdict |
|---|---|
| stage2_actionable_evidence_bonus | existing_axis_kept; do not add more while C29 tire evidence URLs are pending |
| stage2_required_bridge | existing_axis_strengthened for C29: require verified margin bridge, not price spike |
| full_4b_requires_non_price_evidence | existing_axis_kept |
| hard_4c_thesis_break_routes_to_4c | existing_axis_weakened only for one-off operational shock without durable capacity/order/guidance break |
| price_only_blowoff_blocks_positive_stage | existing_axis_kept |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is introduced in this loop. The audit is Stage2-entry quality:

| symbol | Stage2 entry quality | interpretation |
|---|---|---|
| 073240 | good_stage2 | Low-MAE positive asymmetry when margin bridge exists. |
| 002350 | bad_stage2 | Price/rebound spike captured almost no upside and produced high MAE. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| Nexen 2023 spike | 0.00 | 0.00 | stage2 spike was effectively the local/full peak; false positive |
| Kumho 2025 fire | 0.00 | 0.00 | event shock was not a good full-window 4B/4C exit; recovered later |

## 16. 4C Protection Audit

Kumho 2025 fire is the main 4C audit row.

```text
four_c_protection_label = false_break
reason = verified operational shock did not become durable thesis break within stock-web observed 180D window
```

The factory fire was real evidence, but hard 4C should require durable follow-through: unreplaced capacity loss, confirmed guidance cut, order/customer loss, financing stress, or sustained margin deterioration.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L3 mobility/tire cases, Stage2-Actionable cannot be promoted from relative-strength or headline recovery alone. It requires verified margin bridge evidence: volume recovery + raw-material/cost relief + utilization/mix + revision or OP margin confirmation.
proposal_status = shadow_only
blocker = evidence_url_pending/source_proxy_only for 2023 positive/counterexample rows
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
rule = C29 should split Stage2 tire positives into verified margin-bridge positives and rebound-spike false positives; one-off operational disruptions should be 4C-watch unless durable thesis-break evidence appears.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | selected entries | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | existing profile | 3 | 18.98 | -10.88 | 0.67 | mixed; C29 tire needs refinement |
| P0b e2r_2_0_baseline_reference | no stock-web calibrated guards | 3 | 18.98 | -10.88 | 0.67 | weaker guard language |
| P1 sector_specific_candidate_profile | L3 mobility tire bridge required | 2 | 20.65 | -13.01 | 0.50 | improved but source blocker remains |
| P2 canonical_archetype_candidate_profile | C29 tire split | 2 | 20.65 | -13.01 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject rebound spike / one-off hard 4C | 1 | 41.18 | -6.42 | 0.00 | safest, but too restrictive until more evidence |

## 20. Score-Return Alignment Matrix

| trigger | weighted_before | stage_before | weighted_after | stage_after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| Kumho 2023 | 66 | Stage2-Watch | 72 | Stage2-Actionable | 41.18 | -6.42 | aligned positive but source-proxy blocked |
| Nexen 2023 | 67 | Stage2-Actionable | 58 | Stage1/Watch | 0.11 | -19.59 | counterexample guard improves alignment |
| Kumho 2025 | 62 | Stage4C-watch | 54 | 4B-watch/false_break | 15.64 | -6.64 | hard 4C weakening improves alignment |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_VOLUME_COST_MARGIN_BRIDGE_VS_FACTORY_FIRE_OPERATIONAL_BREAK_FALSE_4C", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 0, "4C_case_count": 1, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "C29 tire-specific margin bridge vs operational false-break guard added; evidence URL/proxy blocker remains."}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 2
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_required_bridge, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence
residual_error_types_found: stage2_relative_strength_spike_false_positive, one_off_operational_shock_false_hard_4c
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c only for one-off operational shock without durable break confirmation
existing_axis_kept: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
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
- C29 tire/mobility residual pattern
```

Non-validation scope:

```text
- Exact 2023 as-of fundamental source URLs for Kumho/Nexen margin-bridge rows remain pending.
- No production scoring update.
- No live candidate scan.
- No investment recommendation.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,configured,keep_and_refine,0,"C29 tire/mobility Stage2 needs verified margin bridge, not relative-strength spike alone","positive Kumho 2023 worked; Nexen 2023 high-MAE failed; verified 2025 fire was false hard-4C","R9L87_C29_KUMHO_2023_STAGE2_ACTIONABLE_MARGIN_BRIDGE|R9L87_C29_NEXEN_2023_STAGE2_FALSE_POSITIVE_HIGH_MAE|R9L87_C29_KUMHO_2025_STAGE4C_FALSE_BREAK_FACTORY_FIRE",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,hard_4c_confirmation,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,configured,weaken_for_one_off_operational_shock,0,"Hard 4C should require durable capacity/revision/order thesis-break, not one-off factory fire alone","Kumho 2025 recovered from fire shock to 180D high","R9L87_C29_KUMHO_2025_STAGE4C_FALSE_BREAK_FACTORY_FIRE",1,1,1,low,guardrail_shadow_only,"existing_axis_weakened for one-off operational shock only; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "tradable_row_count": 14354401, "symbol_count": 5414, "corporate_action_candidate_count": 14435}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R9L87_C29_KUMHO_2023_MARGIN_BRIDGE", "symbol": "073240", "company_name": "금호타이어", "round": "R9", "loop": "87", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_VOLUME_COST_MARGIN_BRIDGE_VS_FACTORY_FIRE_OPERATIONAL_BREAK_FALSE_4C", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R9L87_C29_KUMHO_2023_STAGE2_ACTIONABLE_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Stage2 margin bridge aligned with strong 90D/180D upside and low MAE.", "current_profile_verdict": "current_profile_kept_but_should_require_margin_bridge_not_price_only", "price_source": "Songdaiki/stock-web", "notes": "Tire volume/cost normalization path: positive only as source-proxy historical evidence pending exact report/disclosure URLs."}
{"row_type": "case", "case_id": "R9L87_C29_NEXEN_2023_HIGH_MAE_FALSE_STAGE2", "symbol": "002350", "company_name": "넥센타이어", "round": "R9", "loop": "87", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_VOLUME_COST_MARGIN_BRIDGE_VS_FACTORY_FIRE_OPERATIONAL_BREAK_FALSE_4C", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R9L87_C29_NEXEN_2023_STAGE2_FALSE_POSITIVE_HIGH_MAE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Headline recovery spike failed to produce 90D upside and suffered high 180D MAE.", "current_profile_verdict": "current_profile_false_positive_if_stage2_bonus_ignores_post_spike_high_mae", "price_source": "Songdaiki/stock-web", "notes": "Used as counterexample for tire-margin rebound without durable sell-through / margin bridge confirmation."}
{"row_type": "case", "case_id": "R9L87_C29_KUMHO_2025_FACTORY_FIRE_FALSE_4C", "symbol": "073240", "company_name": "금호타이어", "round": "R9", "loop": "87", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_VOLUME_COST_MARGIN_BRIDGE_VS_FACTORY_FIRE_OPERATIONAL_BREAK_FALSE_4C", "case_type": "false_break", "positive_or_counterexample": "counterexample", "best_trigger": "R9L87_C29_KUMHO_2025_STAGE4C_FALSE_BREAK_FACTORY_FIRE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "same symbol as positive case, but different trigger family: operational fire / 4C false-break timing", "independent_evidence_weight": 0.5, "score_price_alignment": "Operational shock caused immediate drawdown but later recovered strongly; hard 4C needs durable thesis-break confirmation.", "current_profile_verdict": "current_profile_4C_too_hard_if_one_off_fire_without_durable_capacity_loss_confirmation", "price_source": "Songdaiki/stock-web", "notes": "Verified public news exists for the fire; treat as 4C guardrail/counterexample, not positive weight evidence."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R9L87_C29_KUMHO_2023_STAGE2_ACTIONABLE_MARGIN_BRIDGE", "case_id": "R9L87_C29_KUMHO_2023_MARGIN_BRIDGE", "symbol": "073240", "company_name": "금호타이어", "round": "R9", "loop": "87", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_VOLUME_COST_MARGIN_BRIDGE_VS_FACTORY_FIRE_OPERATIONAL_BREAK_FALSE_4C", "sector": "mobility_tire", "primary_archetype": "tire_volume_cost_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-03-31", "entry_date": "2023-03-31", "entry_price": 3740.0, "evidence_available_at_that_date": "2023 tire volume/cost margin bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["volume_recovery", "raw_material_cost_relief", "margin_bridge_proxy", "relative_strength"], "stage3_evidence_fields": ["confirmed_low_MAE_path", "continued_180D_upside"], "stage4b_evidence_fields": ["valuation_repricing_watch_after_180D_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/073/073240/2023.csv", "profile_path": "atlas/symbol_profiles/073/073240.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 41.18, "MFE_90D_pct": 41.18, "MFE_180D_pct": 56.42, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -6.42, "MAE_90D_pct": -6.42, "MAE_180D_pct": -6.42, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-11-23", "peak_price": 5850.0, "drawdown_after_peak_pct": -14.19, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_margin_bridge_low_mae_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R9L87_C29_KUMHO_2023_2023-03-31_3740", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R9L87_C29_NEXEN_2023_STAGE2_FALSE_POSITIVE_HIGH_MAE", "case_id": "R9L87_C29_NEXEN_2023_HIGH_MAE_FALSE_STAGE2", "symbol": "002350", "company_name": "넥센타이어", "round": "R9", "loop": "87", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_VOLUME_COST_MARGIN_BRIDGE_VS_FACTORY_FIRE_OPERATIONAL_BREAK_FALSE_4C", "sector": "mobility_tire", "primary_archetype": "tire_margin_rebound_false_stage2", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-15", "entry_date": "2023-05-15", "entry_price": 9290.0, "evidence_available_at_that_date": "headline earnings/rebound spike proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["headline_recovery", "relative_strength_spike", "margin_rebound_proxy"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["post_spike_high_mae", "weak_follow_through"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002350/2023.csv", "profile_path": "atlas/symbol_profiles/002/002350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.11, "MFE_90D_pct": 0.11, "MFE_180D_pct": 0.11, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -19.59, "MAE_90D_pct": -19.59, "MAE_180D_pct": -26.16, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-05-15", "peak_price": 9300.0, "drawdown_after_peak_pct": -26.24, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.0, "four_b_full_window_peak_proximity": 0.0, "four_b_timing_verdict": "stage2_spike_was_peak_false_positive", "four_b_evidence_type": ["positioning_overheat", "price_only"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "bad_stage2_high_mae_false_positive", "current_profile_verdict": "current_profile_false_positive_if_stage2_bonus_ignores_post_spike_mae", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R9L87_C29_NEXEN_2023_2023-05-15_9290", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R9L87_C29_KUMHO_2025_STAGE4C_FALSE_BREAK_FACTORY_FIRE", "case_id": "R9L87_C29_KUMHO_2025_FACTORY_FIRE_FALSE_4C", "symbol": "073240", "company_name": "금호타이어", "round": "R9", "loop": "87", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_VOLUME_COST_MARGIN_BRIDGE_VS_FACTORY_FIRE_OPERATIONAL_BREAK_FALSE_4C", "sector": "mobility_tire", "primary_archetype": "operational_shock_false_hard_4c", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression", "trigger_type": "Stage4C", "trigger_date": "2025-05-17", "entry_date": "2025-05-19", "entry_price": 4445.0, "evidence_available_at_that_date": "Reuters-reported Gwangju factory fire, immediate output capacity shock and stock-price drop.", "evidence_source": "Reuters 2025-05-19 verified public news", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_shock", "capacity_loss_risk"], "stage4c_evidence_fields": ["factory_fire", "possible_guidance_revision"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/073/073240/2025.csv|atlas/ohlcv_tradable_by_symbol_year/073/073240/2026.csv", "profile_path": "atlas/symbol_profiles/073/073240.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.64, "MFE_90D_pct": 15.64, "MFE_180D_pct": 72.1, "MFE_1Y_pct": "insufficient_forward_window_in_stock_web", "MFE_2Y_pct": "insufficient_forward_window_in_stock_web", "MAE_30D_pct": -6.64, "MAE_90D_pct": -6.64, "MAE_180D_pct": -6.64, "MAE_1Y_pct": "insufficient_forward_window_in_stock_web", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2026-02-11", "peak_price": 7650.0, "drawdown_after_peak_pct": -11.11, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.0, "four_b_full_window_peak_proximity": 0.0, "four_b_timing_verdict": "false_break_recovered_after_operational_shock", "four_b_evidence_type": ["contract_delay", "margin_or_backlog_slowdown"], "four_c_protection_label": "false_break", "trigger_outcome_label": "hard_4c_false_break_recovered_to_new_high", "current_profile_verdict": "current_profile_4C_too_hard_without_durable_non_price_thesis_break_confirmation", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R9L87_C29_KUMHO_2025_2025-05-19_4445", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": true, "reuse_reason": "same symbol as 2023 positive but new trigger family and 4C path", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "evidence_url_pending": false, "source_proxy_only": false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L87_C29_KUMHO_2023_MARGIN_BRIDGE", "trigger_id": "R9L87_C29_KUMHO_2023_STAGE2_ACTIONABLE_MARGIN_BRIDGE", "symbol": "073240", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 35, "margin_bridge_score": 45, "revision_score": 45, "relative_strength_score": 65, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 55, "execution_risk_score": 35, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 15, "backlog_visibility_score": 35, "margin_bridge_score": 65, "revision_score": 50, "relative_strength_score": 65, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 55, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 72, "stage_label_after": "Stage2-Actionable", "changed_components": ["margin_bridge_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "aligned_positive_but_source_proxy_blocked", "MFE_90D_pct": 41.18, "MAE_90D_pct": -6.42, "score_return_alignment_label": "aligned_positive_but_source_proxy_blocked", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L87_C29_NEXEN_2023_HIGH_MAE_FALSE_STAGE2", "trigger_id": "R9L87_C29_NEXEN_2023_STAGE2_FALSE_POSITIVE_HIGH_MAE", "symbol": "002350", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 15, "margin_bridge_score": 35, "revision_score": 40, "relative_strength_score": 80, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 67, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 15, "margin_bridge_score": 25, "revision_score": 35, "relative_strength_score": 45, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 45, "execution_risk_score": 70, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 58, "stage_label_after": "Stage1/Watch", "changed_components": ["margin_bridge_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "counterexample_high_mae_false_positive", "MFE_90D_pct": 0.11, "MAE_90D_pct": -19.59, "score_return_alignment_label": "counterexample_high_mae_false_positive", "current_profile_verdict": "current_profile_false_positive_if_stage2_bonus_ignores_post_spike_mae"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L87_C29_KUMHO_2025_FACTORY_FIRE_FALSE_4C", "trigger_id": "R9L87_C29_KUMHO_2025_STAGE4C_FALSE_BREAK_FACTORY_FIRE", "symbol": "073240", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 20, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 20, "execution_risk_score": 80, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 62, "stage_label_before": "Stage4C-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 20, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 20, "execution_risk_score": 55, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "4B-watch/false_break", "changed_components": ["margin_bridge_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "hard_4c_weakened_without_durable_break", "MFE_90D_pct": 15.64, "MAE_90D_pct": -6.64, "score_return_alignment_label": "hard_4c_weakened_without_durable_break", "current_profile_verdict": "current_profile_4C_too_hard_without_durable_non_price_thesis_break_confirmation"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R9", "loop": "87", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_VOLUME_COST_MARGIN_BRIDGE_VS_FACTORY_FIRE_OPERATIONAL_BREAK_FALSE_4C", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 2, "same_archetype_new_symbol_count": 2, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 0, "4C_case_count": 1, "tested_existing_calibrated_axes": ["stage2_required_bridge", "hard_4c_thesis_break_routes_to_4c", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["stage2_relative_strength_spike_false_positive", "one_off_operational_shock_false_hard_4c"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 2, "evidence_url_pending_count": 2}
```

### 25.6 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R9
completed_loop = 87
next_round = R10
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- External event verification: Reuters, 2025-05-19, Kumho Tire factory fire coverage.
- This file contains no investment recommendation and no production scoring change.

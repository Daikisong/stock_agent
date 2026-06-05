# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R12
scheduled_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = INSURANCE_SALE_CONTROL_PREMIUM_VS_BROADCAST_CONTROL_SALE_AND_CAPITAL_STRUCTURE_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R12_loop_88_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
```

This loop continues loop 88 after R11. It adds 3 C32 governance/control-premium cases: one active insurance sale premium positive, one broadcast control-sale event-cap 4B row, and one post-capital-structure false Stage2 row.

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
scheduled_round = R12
scheduled_loop = 88
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
round_sector_consistency = pass
computed_next_round = R13
computed_next_loop = 88
```

R12 permits L10 governance / tender / control-premium reinforcement. This loop avoids the previous R12 loop-87 symbols and the top repeated C32 combinations, then splits active control-premium expansion from capped control-sale/capital-structure events.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP = 41 rows / 22 symbols / good-bad Stage2 16-12 / 4B-4C 3-0
top covered symbols include 010130(4), 036560(4), 000150(3), 041510(3), 241560(3), 000990(2)
previous loop-87 symbols avoided: 180640, 003920, 009240
```

Selected rows:

```text
000400 / Stage2-Actionable / 2024-02-01
040300 / Stage4B / 2023-10-25
006040 / Stage2-Actionable / 2024-05-16
```

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
| 000400 | atlas/symbol_profiles/000/000400.json | selected 2024 window clean; CA candidates are 2019 or earlier |
| 040300 | atlas/symbol_profiles/040/040300.json | no corporate-action candidate |
| 006040 | atlas/symbol_profiles/006/006040.json | 2024-05-14 CA candidate blocked; selected post-CA 2024-05-16 window only |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R12L88_C32_LOTTEINS_2024_INSURANCE_SALE_CONTROL_PREMIUM_POSITIVE | 000400 | 2024-02-01 | yes | 180 | yes | yes | true |
| R12L88_C32_YTN_2023_BROADCAST_CONTROL_SALE_EVENT_CAP_4B | 040300 | 2023-10-25 | yes | 180 | yes | yes | true |
| R12L88_C32_DONGWON_2024_CAPITAL_STRUCTURE_FALSE_STAGE2 | 006040 | 2024-05-16 | yes | 180 | yes | yes-after-CA | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | INSURANCE_SALE_CONTROL_PREMIUM | Active sale/control-premium process can create real Stage2 asymmetry while the spread is still expanding. |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | BROADCAST_CONTROL_SALE_EVENT_CAP | Once control-sale premium is capped or transfer uncertainty dominates, route to 4B overlay. |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | CAPITAL_STRUCTURE_FALSE_STAGE2 | Capital-structure/corporate-action label without tender/control spread can be weak-MFE false Stage2. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R12L88_C32_LOTTEINS_2024_INSURANCE_SALE_CONTROL_PREMIUM_POSITIVE | 000400 | 롯데손해보험 | positive | Active insurance sale/control premium produced high MFE before event maturity. |
| R12L88_C32_YTN_2023_BROADCAST_CONTROL_SALE_EVENT_CAP_4B | 040300 | YTN | counterexample / 4B | Broadcast-control sale premium peaked at the event and then drew down deeply. |
| R12L88_C32_DONGWON_2024_CAPITAL_STRUCTURE_FALSE_STAGE2 | 006040 | 동원산업 | counterexample | Post-capital-structure event had weak MFE and persistent MAE. |

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
| Lotte Non-Life insurance sale | historical public/news proxy | true | true | shadow-only positive |
| YTN broadcast control sale | historical public/news proxy | true | true | 4B overlay counterexample |
| Dongwon capital structure | historical public/disclosure proxy | true | true | false-Stage2 guardrail |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 000400 | atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv | atlas/symbol_profiles/000/000400.json |
| 040300 | atlas/ohlcv_tradable_by_symbol_year/040/040300/2023.csv; 2024.csv | atlas/symbol_profiles/040/040300.json |
| 006040 | atlas/ohlcv_tradable_by_symbol_year/006/006040/2024.csv | atlas/symbol_profiles/006/006040.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R12L88_C32_LOTTEINS_2024_STAGE2_ACTIONABLE_INSURANCE_SALE_PREMIUM | 000400 | Stage2-Actionable | 2024-02-01 | 2610 | positive | active sale/control premium worked |
| R12L88_C32_YTN_2023_STAGE4B_BROADCAST_CONTROL_SALE_CAP | 040300 | Stage4B | 2023-10-25 | 7970 | counterexample/4B | control-sale event cap |
| R12L88_C32_DONGWON_2024_STAGE2_FALSE_POSITIVE_CAPITAL_STRUCTURE_EVENT | 006040 | Stage2-Actionable | 2024-05-16 | 37050 | counterexample | capital-structure false Stage2 |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R12L88_C32_LOTTEINS_2024_STAGE2_ACTIONABLE_INSURANCE_SALE_PREMIUM | 2610 | 40.61 | -4.60 | 40.61 | -4.60 | 56.70 | -16.67 | 2024-06-26 | 4090 | -46.82 |
| R12L88_C32_YTN_2023_STAGE4B_BROADCAST_CONTROL_SALE_CAP | 7970 | 20.45 | -32.12 | 20.45 | -39.08 | 20.45 | -50.19 | 2023-10-25 | 9600 | -58.65 |
| R12L88_C32_DONGWON_2024_STAGE2_FALSE_POSITIVE_CAPITAL_STRUCTURE_EVENT | 37050 | 3.64 | -9.04 | 3.64 | -21.32 | 3.64 | -23.08 | 2024-05-17 | 38400 | -24.09 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C32 Stage2 needs active sale/tender spread or real control-premium expansion |
| local_4b_watch_guard | strengthen: capped control-sale and capital-structure event premiums should route to 4B watch |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is event-stage quality:

| symbol | stage quality | explanation |
|---|---|---|
| 000400 | good_stage2 | Active sale premium was still expanding and produced high MFE. |
| 040300 | good_4B | Control-sale premium was capped and then drew down. |
| 006040 | bad_stage2 | Capital-structure event lacked tender/control spread and had weak MFE. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 040300 broadcast control sale cap | 1.00 | 1.00 | good_full_window_4B_timing_broadcast_control_sale_event_cap |
| 006040 capital structure event | 1.00 | 1.00 | capital_structure_event_was_false_stage2_event_cap |
| 000400 insurance sale premium | n/a | n/a | positive Stage2, but later event-premium 4B watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 040300 / 006040
```

No hard 4C candidate is proposed. R12 loop 88 is about Stage2 bridge quality and 4B event-cap timing, not hard thesis-break promotion.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L10 governance/control-premium cases, Stage2 requires active sale process, tender spread, control premium expansion, or credible value-realization bridge. Capped control-sale, capital-structure, or corporate-action labels should route to 4B/watch unless an independent operating rerating bridge exists.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
rule = C32 should split active sale/control-premium positives from capped broadcast-control sale and capital-structure false Stage2 rows. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 21.57 | -21.67 | 0.67 | mixed; C32 active-premium vs cap split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 21.57 | -21.67 | 0.67 | weaker event-cap guard |
| P1 sector_specific_candidate_profile | L10 active tender/control bridge required | 2 | 30.53 | -21.84 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C32 active premium vs cap split | 2 | 30.53 | -21.84 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject capped/non-spread events as positive | 1 | 40.61 | -4.60 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 000400 insurance sale | 66 | Stage2-Watch | 73 | Stage2-Actionable | 40.61 | -4.60 | insurance_sale_control_premium_positive |
| 040300 broadcast control sale | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 20.45 | -39.08 | broadcast_control_sale_event_cap_4B_guard |
| 006040 capital structure | 65 | Stage2-Actionable | 53 | Stage1/Watch | 3.64 | -21.32 | capital_structure_event_without_control_spread_false_stage2 |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "INSURANCE_SALE_CONTROL_PREMIUM_VS_BROADCAST_CONTROL_SALE_AND_CAPITAL_STRUCTURE_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C32 insurance sale active-premium positive, broadcast control-sale event-cap 4B, and capital-structure false Stage2 split using non-top-covered symbols."}
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
residual_error_types_found: insurance_sale_control_premium_positive, broadcast_control_sale_event_cap_4B, capital_structure_event_false_stage2
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
- C32 active control premium vs capped control-sale/capital-structure event split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,configured,C32_requires_active_sale_tender_spread_or_control_premium_bridge,0,"C32 Stage2 can work when an active sale/tender/control-premium spread is still expanding, but not when the event premium is already capped or when only a capital-structure label exists","Lotte Non-Life positive worked; YTN and Dongwon were cap/false-stage rows","R12L88_C32_LOTTEINS_2024_STAGE2_ACTIONABLE_INSURANCE_SALE_PREMIUM|R12L88_C32_YTN_2023_STAGE4B_BROADCAST_CONTROL_SALE_CAP|R12L88_C32_DONGWON_2024_STAGE2_FALSE_POSITIVE_CAPITAL_STRUCTURE_EVENT",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,configured,cap_control_sale_and_capital_structure_premiums_as_4B_watch,0,"Broadcast control-sale and capital-structure premiums can peak before durable tender/control spread or operating rerating is confirmed","YTN and Dongwon showed event-cap / false-stage behavior with high MAE after peak","R12L88_C32_YTN_2023_STAGE4B_BROADCAST_CONTROL_SALE_CAP|R12L88_C32_DONGWON_2024_STAGE2_FALSE_POSITIVE_CAPITAL_STRUCTURE_EVENT",2,2,2,low,guardrail_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R12L88_C32_LOTTEINS_2024_INSURANCE_SALE_CONTROL_PREMIUM_POSITIVE", "symbol": "000400", "company_name": "롯데손해보험", "round": "R12", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "INSURANCE_SALE_CONTROL_PREMIUM_VS_BROADCAST_CONTROL_SALE_AND_CAPITAL_STRUCTURE_EVENT_CAP", "case_type": "structural_event_success", "positive_or_counterexample": "positive", "best_trigger": "R12L88_C32_LOTTEINS_2024_STAGE2_ACTIONABLE_INSURANCE_SALE_PREMIUM", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Insurance sale/control-premium optionality produced high 30D/90D/180D MFE, but the later drawdown argues for a 4B overlay once the event premium matures.", "current_profile_verdict": "current_profile_kept_but_C32_positive_requires_active_sale_or_tender_spread_not_generic_governance_label", "price_source": "Songdaiki/stock-web", "notes": "Source-proxy only; exact as-of sale-process evidence URL remains pending, so no production weight delta."}
{"row_type": "case", "case_id": "R12L88_C32_YTN_2023_BROADCAST_CONTROL_SALE_EVENT_CAP_4B", "symbol": "040300", "company_name": "YTN", "round": "R12", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "INSURANCE_SALE_CONTROL_PREMIUM_VS_BROADCAST_CONTROL_SALE_AND_CAPITAL_STRUCTURE_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R12L88_C32_YTN_2023_STAGE4B_BROADCAST_CONTROL_SALE_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Broadcast-control sale premium peaked around the event and then produced deep MAE; capped control-sale premium should route to 4B overlay, not structural Green.", "current_profile_verdict": "current_profile_4B_too_late_if_control_sale_premium_cap_not_detected", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action caveat in profile; event-cap counterexample, source-proxy only."}
{"row_type": "case", "case_id": "R12L88_C32_DONGWON_2024_CAPITAL_STRUCTURE_FALSE_STAGE2", "symbol": "006040", "company_name": "동원산업", "round": "R12", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "INSURANCE_SALE_CONTROL_PREMIUM_VS_BROADCAST_CONTROL_SALE_AND_CAPITAL_STRUCTURE_EVENT_CAP", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R12L88_C32_DONGWON_2024_STAGE2_FALSE_POSITIVE_CAPITAL_STRUCTURE_EVENT", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "2024-05-14 corporate-action candidate was blocked; selected 2024-05-16 post-CA window only.", "independent_evidence_weight": 0.5, "score_price_alignment": "Post-capital-structure governance premium had low forward MFE and persistent MAE; C32 Stage2 should not promote capital action label without tender spread, control premium, or operating rerating bridge.", "current_profile_verdict": "current_profile_false_positive_if_capital_structure_event_counts_without_control_premium_or_cashflow_bridge", "price_source": "Songdaiki/stock-web", "notes": "Reduced independent evidence weight because selected row is post-CA window and event-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R12L88_C32_LOTTEINS_2024_STAGE2_ACTIONABLE_INSURANCE_SALE_PREMIUM", "case_id": "R12L88_C32_LOTTEINS_2024_INSURANCE_SALE_CONTROL_PREMIUM_POSITIVE", "symbol": "000400", "company_name": "롯데손해보험", "round": "R12", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "INSURANCE_SALE_CONTROL_PREMIUM_VS_BROADCAST_CONTROL_SALE_AND_CAPITAL_STRUCTURE_EVENT_CAP", "sector": "insurance_control_sale", "primary_archetype": "insurance_sale_control_premium_active_process", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 2610.0, "evidence_available_at_that_date": "insurance sale process / control-premium optionality proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["active_sale_process_proxy", "control_premium_optionality", "relative_strength_reversal", "tender_spread_watch"], "stage3_evidence_fields": ["high_MFE30", "high_MFE90", "active_control_premium_rerating_path"], "stage4b_evidence_fields": ["event_premium_maturity_watch", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv", "profile_path": "atlas/symbol_profiles/000/000400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 40.61, "MFE_90D_pct": 40.61, "MFE_180D_pct": 56.7, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -4.6, "MAE_90D_pct": -4.6, "MAE_180D_pct": -16.67, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 4090.0, "drawdown_after_peak_pct": -46.82, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_event_premium_4B_watch_needed", "four_b_evidence_type": ["control_premium_or_event_premium", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_insurance_sale_control_premium_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L88_C32_000400_2024-02-01_2610", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R12L88_C32_YTN_2023_STAGE4B_BROADCAST_CONTROL_SALE_CAP", "case_id": "R12L88_C32_YTN_2023_BROADCAST_CONTROL_SALE_EVENT_CAP_4B", "symbol": "040300", "company_name": "YTN", "round": "R12", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "INSURANCE_SALE_CONTROL_PREMIUM_VS_BROADCAST_CONTROL_SALE_AND_CAPITAL_STRUCTURE_EVENT_CAP", "sector": "broadcast_control_sale", "primary_archetype": "broadcast_control_sale_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2023-10-25", "entry_date": "2023-10-25", "entry_price": 7970.0, "evidence_available_at_that_date": "broadcast-control sale premium after successful bidder/event spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["control_sale_premium", "ownership_change_expectation", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "control_transfer_uncertainty", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/040/040300/2023.csv|atlas/ohlcv_tradable_by_symbol_year/040/040300/2024.csv", "profile_path": "atlas/symbol_profiles/040/040300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 20.45, "MFE_90D_pct": 20.45, "MFE_180D_pct": 20.45, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -32.12, "MAE_90D_pct": -39.08, "MAE_180D_pct": -50.19, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-10-25", "peak_price": 9600.0, "drawdown_after_peak_pct": -58.65, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_broadcast_control_sale_event_cap", "four_b_evidence_type": ["control_premium_or_event_premium", "legal_or_regulatory_block", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_control_sale_premium_cap_not_detected", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L88_C32_040300_2023-10-25_7970", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R12L88_C32_DONGWON_2024_STAGE2_FALSE_POSITIVE_CAPITAL_STRUCTURE_EVENT", "case_id": "R12L88_C32_DONGWON_2024_CAPITAL_STRUCTURE_FALSE_STAGE2", "symbol": "006040", "company_name": "동원산업", "round": "R12", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "INSURANCE_SALE_CONTROL_PREMIUM_VS_BROADCAST_CONTROL_SALE_AND_CAPITAL_STRUCTURE_EVENT_CAP", "sector": "holding_company_capital_structure", "primary_archetype": "capital_structure_event_without_control_premium_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-16", "entry_date": "2024-05-16", "entry_price": 37050.0, "evidence_available_at_that_date": "post-corporate-action capital-structure / governance premium proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_disclosure_proxy", "stage2_evidence_fields": ["capital_structure_event", "governance_discount_repair_watch", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE", "no_control_premium_spread", "post_event_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006040/2024.csv", "profile_path": "atlas/symbol_profiles/006/006040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.64, "MFE_90D_pct": 3.64, "MFE_180D_pct": 3.64, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -9.04, "MAE_90D_pct": -21.32, "MAE_180D_pct": -23.08, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-17", "peak_price": 38400.0, "drawdown_after_peak_pct": -24.09, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "capital_structure_event_was_false_stage2_event_cap", "four_b_evidence_type": ["control_premium_or_event_premium", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_capital_structure_event_false_positive", "current_profile_verdict": "current_profile_false_positive_if_capital_structure_event_counts_without_control_premium_or_cashflow_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_post_2024-05-14_CA_window", "same_entry_group_id": "R12L88_C32_006040_2024-05-16_37050", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "post-CA row only; 2024-05-14 corporate-action candidate blocked from entry selection", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L88_C32_LOTTEINS_2024_INSURANCE_SALE_CONTROL_PREMIUM_POSITIVE", "trigger_id": "R12L88_C32_LOTTEINS_2024_STAGE2_ACTIONABLE_INSURANCE_SALE_PREMIUM", "symbol": "000400", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 10, "revision_score": 15, "relative_strength_score": 70, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 70, "execution_risk_score": 45, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 30, "revision_score": 25, "relative_strength_score": 60, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 65, "execution_risk_score": 35, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score", "margin_bridge_score"], "component_delta_explanation": "insurance_sale_control_premium_positive", "MFE_90D_pct": 40.61, "MAE_90D_pct": -4.6, "score_return_alignment_label": "insurance_sale_control_premium_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L88_C32_YTN_2023_BROADCAST_CONTROL_SALE_EVENT_CAP_4B", "trigger_id": "R12L88_C32_YTN_2023_STAGE4B_BROADCAST_CONTROL_SALE_CAP", "symbol": "040300", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 10, "revision_score": 15, "relative_strength_score": 70, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 70, "execution_risk_score": 45, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 35, "execution_risk_score": 80, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score", "margin_bridge_score"], "component_delta_explanation": "broadcast_control_sale_event_cap_4B_guard", "MFE_90D_pct": 20.45, "MAE_90D_pct": -39.08, "score_return_alignment_label": "broadcast_control_sale_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_control_sale_premium_cap_not_detected"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L88_C32_DONGWON_2024_CAPITAL_STRUCTURE_FALSE_STAGE2", "trigger_id": "R12L88_C32_DONGWON_2024_STAGE2_FALSE_POSITIVE_CAPITAL_STRUCTURE_EVENT", "symbol": "006040", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 10, "revision_score": 15, "relative_strength_score": 70, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 70, "execution_risk_score": 45, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 65, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 35, "execution_risk_score": 80, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score", "margin_bridge_score"], "component_delta_explanation": "capital_structure_event_without_control_spread_false_stage2", "MFE_90D_pct": 3.64, "MAE_90D_pct": -21.32, "score_return_alignment_label": "capital_structure_event_without_control_spread_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_capital_structure_event_counts_without_control_premium_or_cashflow_bridge"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R12", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "INSURANCE_SALE_CONTROL_PREMIUM_VS_BROADCAST_CONTROL_SALE_AND_CAPITAL_STRUCTURE_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["insurance_sale_control_premium_positive", "broadcast_control_sale_event_cap_4B", "capital_structure_event_false_stage2"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","reason":"all selected rows have usable 180D stock-web windows; 006040 entry was shifted to the post-2024-05-14 corporate-action candidate window","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R12
completed_loop = 88
next_round = R13
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.

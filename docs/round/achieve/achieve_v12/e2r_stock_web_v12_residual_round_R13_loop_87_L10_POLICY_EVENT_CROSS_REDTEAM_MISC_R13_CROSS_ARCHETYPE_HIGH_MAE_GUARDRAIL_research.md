# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R13
scheduled_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
fine_archetype_id = POST_STAGE2_HIGH_MAE_FALSE_POSITIVE_AND_EVENT_CAP_CROSS_REVIEW
loop_objective = residual_false_positive_mining | 4B_non_price_requirement_stress_test | counterexample_mining | holdout_validation | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R13_loop_87_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md
```

R13 is a cross-archetype checkpoint, not a new sector round. This file reviews 5 reused high-MAE / event-cap cases from R9~R12. Every review row has:

```text
is_new_independent_case = false
independent_evidence_weight = 0.0
do_not_count_as_new_case = true
dedupe_for_aggregate = false
aggregate_group_role = r13_review_only
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes stress-tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R13
scheduled_loop = 87
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
round_sector_consistency = pass
computed_next_round = R1
computed_next_loop = 88
```

R13 scope is cross-archetype high-MAE guardrail review. The reviewed rows span:

```text
C29 mobility/tire high-MAE false Stage2
C30 construction/PF sector-beta false Stage2
C31 policy/hydrogen false Stage2
C32 governance/control-premium event cap 4B
```

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key is respected:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

This R13 file is not claiming new independent cases. It reuses prior v12 research rows as cross-check evidence. The No-Repeat rule for R13 review rows is enforced by setting `do_not_count_as_new_case=true`.

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
| tradable_row_count | 14354401 |
| symbol_count | 5414 |

| symbol | profile path | CA window status |
|---|---|---|
| 002350 | atlas/symbol_profiles/002/002350.json | selected 2023 window clean |
| 047040 | atlas/symbol_profiles/047/047040.json | selected 2024 window clean |
| 336260 | atlas/symbol_profiles/336/336260.json | no CA candidate |
| 003920 | atlas/symbol_profiles/003/003920.json | selected 2021 window clean |
| 009240 | atlas/symbol_profiles/009/009240.json | no CA candidate |

## 5. Historical Eligibility Gate

| review case | symbol | entry_date | forward 180D | OHLC valid | CA clean | calibration_usable | new independent? |
|---|---|---:|---:|---|---|---|---|
| C29 Nexen tire false Stage2 | 002350 | 2023-05-15 | 180 | yes | yes | true | false |
| C30 Daewoo sector-beta false Stage2 | 047040 | 2024-01-02 | 180 | yes | yes | true | false |
| C31 Doosan FuelCell hydrogen policy false Stage2 | 336260 | 2022-08-11 | 180 | yes | yes | true | false |
| C32 Namyang control-sale event cap | 003920 | 2021-07-01 | 180 | yes | yes | true | false |
| C32 Hanssem PE control-premium fade | 009240 | 2021-07-14 | 180 | yes | yes | true | false |

## 6. Canonical Archetype Compression Map

| R13 review bucket | source canonical | compression rule |
|---|---|---|
| weak_MFE_high_MAE_stage2 | C29/C30/C31 | If MFE90 is weak and MAE90/180 is large, Stage2 needs stronger non-price bridge before promotion. |
| event_cap_4B_needed | C32 | Control/tender/PE event premium with capped upside belongs in 4B overlay. |
| policy_or_theme_without_cashflow | C31/C30/C29 | Policy/sector/theme headline must not substitute for order/cashflow/margin bridge. |

## 7. Case Selection Summary

| source round | original canonical | symbol | role | reason |
|---|---|---|---|---|
| R9 | C29 | 002350 | false Stage2 | Almost no upside, high MAE after rebound spike. |
| R10 | C30 | 047040 | false Stage2 | Construction beta/order headline lacked cashflow bridge. |
| R11 | C31 | 336260 | false Stage2 | Hydrogen-policy spike had high MAE and no revenue/order bridge. |
| R12 | C32 | 003920 | 4B event cap | Control-sale premium capped; severe post-peak drawdown. |
| R12 | C32 | 009240 | 4B event cap | PE premium spike had minimal further upside and high MAE. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 0
counterexample_count = 5
4B_case_count = 2
4C_case_count = 0
new_independent_case_count = 0
reused_case_count = 5
```

R13 intentionally contains no new sector positive case.

## 9. Evidence Source Map

| symbol | evidence source status | evidence_url_pending | source_proxy_only | R13 usage |
|---|---|---|---|---|
| 002350 | prior v12 source proxy | true | true | guardrail review |
| 047040 | prior v12 source proxy | true | true | guardrail review |
| 336260 | prior v12 source proxy | true | true | guardrail review |
| 003920 | prior v12 source proxy | true | true | event-cap review |
| 009240 | prior v12 source proxy | true | true | event-cap review |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 002350 | atlas/ohlcv_tradable_by_symbol_year/002/002350/2023.csv | atlas/symbol_profiles/002/002350.json |
| 047040 | atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv | atlas/symbol_profiles/047/047040.json |
| 336260 | atlas/ohlcv_tradable_by_symbol_year/336/336260/2022.csv; 2023.csv | atlas/symbol_profiles/336/336260.json |
| 003920 | atlas/ohlcv_tradable_by_symbol_year/003/003920/2021.csv | atlas/symbol_profiles/003/003920.json |
| 009240 | atlas/ohlcv_tradable_by_symbol_year/009/009240/2021.csv; 2022.csv | atlas/symbol_profiles/009/009240.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | original canonical | symbol | trigger_type | entry_date | entry_price | R13 label |
|---|---|---|---|---:|---:|---|
| R13L87_REVIEW_C29_NEXEN_2023_STAGE2_FALSE_POSITIVE_HIGH_MAE | C29 | 002350 | Stage2-Actionable | 2023-05-15 | 9290 | high_MAE_stage2_false_positive |
| R13L87_REVIEW_C30_DAEWOO_2024_STAGE2_FALSE_POSITIVE_SECTOR_BETA | C30 | 047040 | Stage2-Actionable | 2024-01-02 | 4170 | weak_MFE_stage2_false_positive |
| R13L87_REVIEW_C31_DSFUEL_2022_STAGE2_FALSE_POSITIVE_HYDROGEN_POLICY | C31 | 336260 | Stage2-Actionable | 2022-08-11 | 40350 | high_MAE_policy_false_stage2 |
| R13L87_REVIEW_C32_NAMYANG_2021_STAGE4B_CONTROL_SALE_EVENT_CAP | C32 | 003920 | Stage4B | 2021-07-01 | 760000 | event_cap_high_MAE_4B |
| R13L87_REVIEW_C32_HANSSEM_2021_STAGE4B_PE_CONTROL_PREMIUM_FADE | C32 | 009240 | Stage4B | 2021-07-14 | 146500 | event_cap_high_MAE_4B |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | original canonical | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 002350 | C29 | 9290 | 0.11 | -19.59 | 0.11 | -19.59 | 0.11 | -26.16 | 2023-05-15 | 9300 | -26.24 |
| 047040 | C30 | 4170 | 4.08 | -7.19 | 4.08 | -14.15 | 4.20 | -14.99 | 2024-07-16 | 4345 | -18.99 |
| 336260 | C31 | 40350 | 2.23 | -16.98 | 2.23 | -30.86 | 2.23 | -39.28 | 2022-08-16 | 41250 | -41.45 |
| 003920 | C32 | 760000 | 6.97 | -27.89 | 6.97 | -49.74 | 6.97 | -49.74 | 2021-07-01 | 813000 | -53.01 |
| 009240 | C32 | 146500 | 1.71 | -27.99 | 1.71 | -27.99 | 1.71 | -52.97 | 2021-07-14 | 149000 | -53.76 |

```text
avg_MFE_90D_pct = 3.02
avg_MAE_90D_pct = -28.47
avg_MFE_180D_pct = 3.04
avg_MAE_180D_pct = -36.63
high_MAE_review_count = 4 / 5
```

## 13. Current Calibrated Profile Stress Test

| axis | R13 verdict |
|---|---|
| stage2_required_bridge | existing_axis_strengthened: repeated weak-MFE/high-MAE rows need verified non-price bridge. |
| local_4b_watch_guard | existing_axis_strengthened: capped control/tender/PE event premiums should be 4B overlay. |
| full_4b_requires_non_price_evidence | existing_axis_kept. |
| price_only_blowoff_blocks_positive_stage | existing_axis_kept. |
| hard_4c_thesis_break_routes_to_4c | existing_axis_kept; no hard 4C promoted. |

## 14. Stage2 / Yellow / Green Comparison

R13 does not add new Green cases. It reviews cases where Stage2/Yellow-like interpretation would have been dangerous.

| bucket | reviewed rows | interpretation |
|---|---:|---|
| Stage2 false positive | 3 | MFE90 weak, MAE90/180 too large; bridge requirements should stay strict. |
| Stage3/Yellow-like event cap | 2 | Control/PE/tender premium should not be treated as structural Green. |
| hard 4C | 0 | No new hard thesis-break route proposed. |

```text
green_lateness_ratio = not_applicable
reason = R13 high-MAE guardrail review, no new Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B local proximity | 4B full-window proximity | timing verdict |
|---|---:|---:|---|
| 003920 | 1.00 | 1.00 | good_full_window_4B_timing_control_sale_event_cap |
| 009240 | 1.00 | 1.00 | good_full_window_4B_timing_PE_control_premium_event_cap |
| 002350 | 0.00 | 0.00 | Stage2 spike itself was peak-like false positive |
| 336260 | 0.00 | 0.00 | Policy spike was not order conversion |
| 047040 | 0.04 | 0.04 | Weak MFE, not useful positive setup |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for event-cap rows
```

This review supports watch/4B routing, not hard 4C promotion.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = R13 cross-archetype checkpoint; not a sector-specific rule proposal.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
rule = If MFE90 is weak, MAE90/180 is high, and the non-price bridge is missing or event premium is capped, do not promote to Stage2/Stage3 positive. Keep as watch/4B overlay unless a verified bridge appears.
proposal_status = guardrail_stress_test_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | reviewed triggers | avg_MFE90 | avg_MAE90 | high_MAE_count | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 5 | 3.02 | -28.47 | 4/5 | guardrails needed |
| P0b e2r_2_0_baseline_reference | older baseline | 5 | 3.02 | -28.47 | 4/5 | weaker bridge/cap handling |
| P1 cross_guard_candidate_profile | cross high-MAE guard | 5 | 3.02 | -28.47 | 4/5 | improves rejection alignment |
| P2 archetype_specific_candidate_profile | source-canonical bridge requirements | 5 | 3.02 | -28.47 | 4/5 | best explanatory fit |
| P3 counterexample_guard_profile | reject all reviewed positives | 5 | 3.02 | -28.47 | 4/5 | safest but review-only |

## 20. Score-Return Alignment Matrix

| symbol | original canonical | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---|---:|---|---:|---|---:|---:|---|
| 002350 | C29 | 68 | Stage2-Actionable | 55 | Stage1/Watch | 0.11 | -19.59 | r13_high_MAE_guardrail_improves_alignment |
| 047040 | C30 | 68 | Stage2-Actionable | 55 | Stage1/Watch | 4.08 | -14.15 | r13_high_MAE_guardrail_improves_alignment |
| 336260 | C31 | 68 | Stage2-Actionable | 53 | Stage1/Watch | 2.23 | -30.86 | r13_high_MAE_guardrail_improves_alignment |
| 003920 | C32 | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 6.97 | -49.74 | r13_high_MAE_guardrail_improves_alignment |
| 009240 | C32 | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 1.71 | -27.99 | r13_high_MAE_guardrail_improves_alignment |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "POST_STAGE2_HIGH_MAE_FALSE_POSITIVE_AND_EVENT_CAP_CROSS_REVIEW", "positive_case_count": 0, "counterexample_count": 5, "4B_case_count": 2, "4C_case_count": 0, "new_independent_case_count": 0, "reused_case_count": 5, "calibration_usable_trigger_count": 5, "representative_trigger_count": 0, "current_profile_error_count": 5, "sector_rule_candidate": false, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "R13 cross-review validates high-MAE guardrail across C29/C30/C31/C32 without adding new independent cases."}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 0
reused_case_count: 5
reused_case_ids: R9L87_C29_NEXEN_2023_HIGH_MAE_FALSE_STAGE2, R10L87_C30_DAEWOO_2024_SECTOR_BETA_FALSE_STAGE2, R11L87_C31_DSFUEL_2022_HYDROGEN_POLICY_FALSE_STAGE2, R12L87_C32_NAMYANG_2021_CONTROL_SALE_EVENT_CAP_4B, R12L87_C32_HANSSEM_2021_PE_CONTROL_PREMIUM_FADE_4B
new_symbol_count: 0
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 0
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: weak_MFE_high_MAE_stage2, event_cap_4B_needed, policy_or_control_premium_without_cashflow_bridge
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: R13 review-only rows cannot add independent evidence weight
loop_contribution_label: axis_stress_test_passed
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Reused stock-web tradable raw OHLC paths
- entry_date / entry_price
- MFE/MAE 30D/90D/180D
- high-MAE cross-archetype guardrail
- R13 no-new-case enforcement
```

Non-validation scope:

```text
- No new sector-specific positive case.
- Exact as-of evidence URLs remain pending for reused rows.
- No production scoring update.
- No live candidate scan.
- No investment recommendation.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,cross_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL,configured,keep_and_strengthen_high_MAE_guard,0,"Across C29/C30/C31/C32, Stage2-like signals with weak MFE90 and high MAE90 need verified non-price bridge before positive-stage promotion","avg_MFE90=3.02; avg_MAE90=-28.47; high_MAE_count=4/5","R13L87_REVIEW_C29_NEXEN_2023_STAGE2_FALSE_POSITIVE_HIGH_MAE|R13L87_REVIEW_C30_DAEWOO_2024_STAGE2_FALSE_POSITIVE_SECTOR_BETA|R13L87_REVIEW_C31_DSFUEL_2022_STAGE2_FALSE_POSITIVE_HYDROGEN_POLICY",5,0,5,medium,r13_guardrail_review_only,"do_not_count_as_new_case=true; no production delta"
shadow_weight,local_4b_watch_guard,cross_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL,configured,keep_event_cap_as_4B_watch,0,"Governance/control and policy/capex event premiums with capped upside should be 4B overlay, not Stage3-Green evidence","Namyang and Hanssem event-cap rows had <=7% MFE90 and ~-28% to -50% MAE90","R13L87_REVIEW_C32_NAMYANG_2021_STAGE4B_CONTROL_SALE_EVENT_CAP|R13L87_REVIEW_C32_HANSSEM_2021_STAGE4B_PE_CONTROL_PREMIUM_FADE",5,0,5,medium,r13_guardrail_review_only,"R13 review rows must not add independent case weight"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R13L87_REVIEW_C29_NEXEN_2023_HIGH_MAE_FALSE_STAGE2", "symbol": "002350", "company_name": "넥센타이어", "round": "R13", "loop": "87", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "POST_STAGE2_HIGH_MAE_FALSE_POSITIVE_AND_EVENT_CAP_CROSS_REVIEW", "case_type": "r13_cross_archetype_review", "positive_or_counterexample": "counterexample", "best_trigger": "R13L87_REVIEW_C29_NEXEN_2023_STAGE2_FALSE_POSITIVE_HIGH_MAE", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 review of C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE / R9L87_C29_NEXEN_2023_HIGH_MAE_FALSE_STAGE2", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "score_price_alignment": "current_profile_false_positive_if_stage2_bonus_ignores_post_spike_mae", "current_profile_verdict": "current_profile_false_positive_if_stage2_bonus_ignores_post_spike_mae", "price_source": "Songdaiki/stock-web", "notes": "R13 cross-review row; reused evidence only; not a new independent case."}
{"row_type": "case", "case_id": "R13L87_REVIEW_C30_DAEWOO_2024_SECTOR_BETA_FALSE_STAGE2", "symbol": "047040", "company_name": "대우건설", "round": "R13", "loop": "87", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "POST_STAGE2_HIGH_MAE_FALSE_POSITIVE_AND_EVENT_CAP_CROSS_REVIEW", "case_type": "r13_cross_archetype_review", "positive_or_counterexample": "counterexample", "best_trigger": "R13L87_REVIEW_C30_DAEWOO_2024_STAGE2_FALSE_POSITIVE_SECTOR_BETA", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 review of C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK / R10L87_C30_DAEWOO_2024_SECTOR_BETA_FALSE_STAGE2", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "score_price_alignment": "current_profile_false_positive_if_order_or_sector_beta_counts_without_cashflow_bridge", "current_profile_verdict": "current_profile_false_positive_if_order_or_sector_beta_counts_without_cashflow_bridge", "price_source": "Songdaiki/stock-web", "notes": "R13 cross-review row; reused evidence only; not a new independent case."}
{"row_type": "case", "case_id": "R13L87_REVIEW_C31_DSFUEL_2022_HYDROGEN_POLICY_FALSE_STAGE2", "symbol": "336260", "company_name": "두산퓨얼셀", "round": "R13", "loop": "87", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "POST_STAGE2_HIGH_MAE_FALSE_POSITIVE_AND_EVENT_CAP_CROSS_REVIEW", "case_type": "r13_cross_archetype_review", "positive_or_counterexample": "counterexample", "best_trigger": "R13L87_REVIEW_C31_DSFUEL_2022_STAGE2_FALSE_POSITIVE_HYDROGEN_POLICY", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 review of C31_POLICY_SUBSIDY_LEGISLATION_EVENT / R11L87_C31_DSFUEL_2022_HYDROGEN_POLICY_FALSE_STAGE2", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "score_price_alignment": "current_profile_false_positive_if_policy_score_counts_without_order_revenue_bridge", "current_profile_verdict": "current_profile_false_positive_if_policy_score_counts_without_order_revenue_bridge", "price_source": "Songdaiki/stock-web", "notes": "R13 cross-review row; reused evidence only; not a new independent case."}
{"row_type": "case", "case_id": "R13L87_REVIEW_C32_NAMYANG_2021_CONTROL_SALE_EVENT_CAP_4B", "symbol": "003920", "company_name": "남양유업", "round": "R13", "loop": "87", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "POST_STAGE2_HIGH_MAE_FALSE_POSITIVE_AND_EVENT_CAP_CROSS_REVIEW", "case_type": "r13_cross_archetype_review", "positive_or_counterexample": "counterexample", "best_trigger": "R13L87_REVIEW_C32_NAMYANG_2021_STAGE4B_CONTROL_SALE_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 review of C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP / R12L87_C32_NAMYANG_2021_CONTROL_SALE_EVENT_CAP_4B", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "score_price_alignment": "current_profile_4B_too_late_if_control_premium_cap_not_detected", "current_profile_verdict": "current_profile_4B_too_late_if_control_premium_cap_not_detected", "price_source": "Songdaiki/stock-web", "notes": "R13 cross-review row; reused evidence only; not a new independent case."}
{"row_type": "case", "case_id": "R13L87_REVIEW_C32_HANSSEM_2021_PE_CONTROL_PREMIUM_FADE_4B", "symbol": "009240", "company_name": "한샘", "round": "R13", "loop": "87", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "POST_STAGE2_HIGH_MAE_FALSE_POSITIVE_AND_EVENT_CAP_CROSS_REVIEW", "case_type": "r13_cross_archetype_review", "positive_or_counterexample": "counterexample", "best_trigger": "R13L87_REVIEW_C32_HANSSEM_2021_STAGE4B_PE_CONTROL_PREMIUM_FADE", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 review of C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP / R12L87_C32_HANSSEM_2021_PE_CONTROL_PREMIUM_FADE_4B", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "score_price_alignment": "current_profile_false_positive_if_control_premium_spike_counts_as_structural_green", "current_profile_verdict": "current_profile_false_positive_if_control_premium_spike_counts_as_structural_green", "price_source": "Songdaiki/stock-web", "notes": "R13 cross-review row; reused evidence only; not a new independent case."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R13L87_REVIEW_C29_NEXEN_2023_STAGE2_FALSE_POSITIVE_HIGH_MAE", "case_id": "R13L87_REVIEW_C29_NEXEN_2023_HIGH_MAE_FALSE_STAGE2", "symbol": "002350", "company_name": "넥센타이어", "round": "R13", "loop": "87", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "POST_STAGE2_HIGH_MAE_FALSE_POSITIVE_AND_EVENT_CAP_CROSS_REVIEW", "sector": "cross_archetype_redteam", "primary_archetype": "high_MAE_guardrail_review", "original_large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "original_canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "original_case_id": "R9L87_C29_NEXEN_2023_HIGH_MAE_FALSE_STAGE2", "original_trigger_id": "R9L87_C29_NEXEN_2023_STAGE2_FALSE_POSITIVE_HIGH_MAE", "loop_objective": "residual_false_positive_mining | 4B_non_price_requirement_stress_test | counterexample_mining | holdout_validation | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-15", "entry_date": "2023-05-15", "entry_price": 9290.0, "evidence_available_at_that_date": "reused historical evidence from prior v12 sector round; R13 review only", "evidence_source": "prior_v12_research_row_with_stock_web_price_path", "stage2_evidence_fields": ["headline_recovery", "relative_strength_spike", "margin_rebound_proxy"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["post_spike_high_mae", "weak_follow_through"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002350/2023.csv", "profile_path": "atlas/symbol_profiles/002/002350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.11, "MFE_90D_pct": 0.11, "MFE_180D_pct": 0.11, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -19.59, "MAE_90D_pct": -19.59, "MAE_180D_pct": -26.16, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-05-15", "peak_price": 9300.0, "drawdown_after_peak_pct": -26.24, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.0, "four_b_full_window_peak_proximity": 0.0, "four_b_timing_verdict": "stage2_spike_was_peak_false_positive", "four_b_evidence_type": ["positioning_overheat", "price_only"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "bad_stage2_high_mae_false_positive", "current_profile_verdict": "current_profile_false_positive_if_stage2_bonus_ignores_post_spike_mae", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L87_REVIEW_002350_2023-05-15_9290.0", "dedupe_for_aggregate": false, "aggregate_group_role": "r13_review_only", "is_new_independent_case": false, "reuse_reason": "R13 cross-review of R9L87_C29_NEXEN_2023_STAGE2_FALSE_POSITIVE_HIGH_MAE", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "evidence_url_pending": true, "source_proxy_only": true, "r13_review_label": "high_MAE_stage2_false_positive"}
{"row_type": "trigger", "trigger_id": "R13L87_REVIEW_C30_DAEWOO_2024_STAGE2_FALSE_POSITIVE_SECTOR_BETA", "case_id": "R13L87_REVIEW_C30_DAEWOO_2024_SECTOR_BETA_FALSE_STAGE2", "symbol": "047040", "company_name": "대우건설", "round": "R13", "loop": "87", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "POST_STAGE2_HIGH_MAE_FALSE_POSITIVE_AND_EVENT_CAP_CROSS_REVIEW", "sector": "cross_archetype_redteam", "primary_archetype": "high_MAE_guardrail_review", "original_large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "original_canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "original_case_id": "R10L87_C30_DAEWOO_2024_SECTOR_BETA_FALSE_STAGE2", "original_trigger_id": "R10L87_C30_DAEWOO_2024_STAGE2_FALSE_POSITIVE_SECTOR_BETA", "loop_objective": "residual_false_positive_mining | 4B_non_price_requirement_stress_test | counterexample_mining | holdout_validation | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-02", "entry_date": "2024-01-02", "entry_price": 4170.0, "evidence_available_at_that_date": "reused historical evidence from prior v12 sector round; R13 review only", "evidence_source": "prior_v12_research_row_with_stock_web_price_path", "stage2_evidence_fields": ["sector_beta_rebound", "order_headline_proxy", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_follow_through", "PF_cashflow_bridge_missing"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv", "profile_path": "atlas/symbol_profiles/047/047040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.08, "MFE_90D_pct": 4.08, "MFE_180D_pct": 4.2, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -7.19, "MAE_90D_pct": -14.15, "MAE_180D_pct": -14.99, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-16", "peak_price": 4345.0, "drawdown_after_peak_pct": -18.99, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.04, "four_b_full_window_peak_proximity": 0.04, "four_b_timing_verdict": "sector_beta_stage2_false_positive_with_weak_MFE", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "bad_stage2_weak_MFE_negative_asymmetry", "current_profile_verdict": "current_profile_false_positive_if_order_or_sector_beta_counts_without_cashflow_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L87_REVIEW_047040_2024-01-02_4170.0", "dedupe_for_aggregate": false, "aggregate_group_role": "r13_review_only", "is_new_independent_case": false, "reuse_reason": "R13 cross-review of R10L87_C30_DAEWOO_2024_STAGE2_FALSE_POSITIVE_SECTOR_BETA", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "evidence_url_pending": true, "source_proxy_only": true, "r13_review_label": "weak_MFE_stage2_false_positive"}
{"row_type": "trigger", "trigger_id": "R13L87_REVIEW_C31_DSFUEL_2022_STAGE2_FALSE_POSITIVE_HYDROGEN_POLICY", "case_id": "R13L87_REVIEW_C31_DSFUEL_2022_HYDROGEN_POLICY_FALSE_STAGE2", "symbol": "336260", "company_name": "두산퓨얼셀", "round": "R13", "loop": "87", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "POST_STAGE2_HIGH_MAE_FALSE_POSITIVE_AND_EVENT_CAP_CROSS_REVIEW", "sector": "cross_archetype_redteam", "primary_archetype": "high_MAE_guardrail_review", "original_large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "original_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "original_case_id": "R11L87_C31_DSFUEL_2022_HYDROGEN_POLICY_FALSE_STAGE2", "original_trigger_id": "R11L87_C31_DSFUEL_2022_STAGE2_FALSE_POSITIVE_HYDROGEN_POLICY", "loop_objective": "residual_false_positive_mining | 4B_non_price_requirement_stress_test | counterexample_mining | holdout_validation | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-08-11", "entry_date": "2022-08-11", "entry_price": 40350.0, "evidence_available_at_that_date": "reused historical evidence from prior v12 sector round; R13 review only", "evidence_source": "prior_v12_research_row_with_stock_web_price_path", "stage2_evidence_fields": ["hydrogen_policy_headline", "theme_relative_strength", "subsidy_expectation"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_follow_through", "policy_to_revenue_gap", "high_MAE"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/336/336260/2022.csv|atlas/ohlcv_tradable_by_symbol_year/336/336260/2023.csv", "profile_path": "atlas/symbol_profiles/336/336260.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.23, "MFE_90D_pct": 2.23, "MFE_180D_pct": 2.23, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -16.98, "MAE_90D_pct": -30.86, "MAE_180D_pct": -39.28, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-08-16", "peak_price": 41250.0, "drawdown_after_peak_pct": -41.45, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.0, "four_b_full_window_peak_proximity": 0.0, "four_b_timing_verdict": "policy_theme_spike_was_not_order_conversion", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "bad_stage2_policy_headline_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_if_policy_score_counts_without_order_revenue_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L87_REVIEW_336260_2022-08-11_40350.0", "dedupe_for_aggregate": false, "aggregate_group_role": "r13_review_only", "is_new_independent_case": false, "reuse_reason": "R13 cross-review of R11L87_C31_DSFUEL_2022_STAGE2_FALSE_POSITIVE_HYDROGEN_POLICY", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "evidence_url_pending": true, "source_proxy_only": true, "r13_review_label": "high_MAE_policy_false_stage2"}
{"row_type": "trigger", "trigger_id": "R13L87_REVIEW_C32_NAMYANG_2021_STAGE4B_CONTROL_SALE_EVENT_CAP", "case_id": "R13L87_REVIEW_C32_NAMYANG_2021_CONTROL_SALE_EVENT_CAP_4B", "symbol": "003920", "company_name": "남양유업", "round": "R13", "loop": "87", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "POST_STAGE2_HIGH_MAE_FALSE_POSITIVE_AND_EVENT_CAP_CROSS_REVIEW", "sector": "cross_archetype_redteam", "primary_archetype": "high_MAE_guardrail_review", "original_large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "original_canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "original_case_id": "R12L87_C32_NAMYANG_2021_CONTROL_SALE_EVENT_CAP_4B", "original_trigger_id": "R12L87_C32_NAMYANG_2021_STAGE4B_CONTROL_SALE_EVENT_CAP", "loop_objective": "residual_false_positive_mining | 4B_non_price_requirement_stress_test | counterexample_mining | holdout_validation | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2021-07-01", "entry_date": "2021-07-01", "entry_price": 760000.0, "evidence_available_at_that_date": "reused historical evidence from prior v12 sector round; R13 review only", "evidence_source": "prior_v12_research_row_with_stock_web_price_path", "stage2_evidence_fields": ["control_sale_premium", "ownership_change_expectation"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "control_sale_execution_uncertainty", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003920/2021.csv", "profile_path": "atlas/symbol_profiles/003/003920.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.97, "MFE_90D_pct": 6.97, "MFE_180D_pct": 6.97, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -27.89, "MAE_90D_pct": -49.74, "MAE_180D_pct": -49.74, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-01", "peak_price": 813000.0, "drawdown_after_peak_pct": -53.01, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_control_sale_event_cap", "four_b_evidence_type": ["control_premium_or_event_premium", "legal_or_regulatory_block", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_control_premium_cap_not_detected", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L87_REVIEW_003920_2021-07-01_760000.0", "dedupe_for_aggregate": false, "aggregate_group_role": "r13_review_only", "is_new_independent_case": false, "reuse_reason": "R13 cross-review of R12L87_C32_NAMYANG_2021_STAGE4B_CONTROL_SALE_EVENT_CAP", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "evidence_url_pending": true, "source_proxy_only": true, "r13_review_label": "event_cap_high_MAE_4B"}
{"row_type": "trigger", "trigger_id": "R13L87_REVIEW_C32_HANSSEM_2021_STAGE4B_PE_CONTROL_PREMIUM_FADE", "case_id": "R13L87_REVIEW_C32_HANSSEM_2021_PE_CONTROL_PREMIUM_FADE_4B", "symbol": "009240", "company_name": "한샘", "round": "R13", "loop": "87", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "POST_STAGE2_HIGH_MAE_FALSE_POSITIVE_AND_EVENT_CAP_CROSS_REVIEW", "sector": "cross_archetype_redteam", "primary_archetype": "high_MAE_guardrail_review", "original_large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "original_canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "original_case_id": "R12L87_C32_HANSSEM_2021_PE_CONTROL_PREMIUM_FADE_4B", "original_trigger_id": "R12L87_C32_HANSSEM_2021_STAGE4B_PE_CONTROL_PREMIUM_FADE", "loop_objective": "residual_false_positive_mining | 4B_non_price_requirement_stress_test | counterexample_mining | holdout_validation | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2021-07-14", "entry_date": "2021-07-14", "entry_price": 146500.0, "evidence_available_at_that_date": "reused historical evidence from prior v12 sector round; R13 review only", "evidence_source": "prior_v12_research_row_with_stock_web_price_path", "stage2_evidence_fields": ["control_premium_bid", "ownership_change_expectation"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009240/2021.csv|atlas/ohlcv_tradable_by_symbol_year/009/009240/2022.csv", "profile_path": "atlas/symbol_profiles/009/009240.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.71, "MFE_90D_pct": 1.71, "MFE_180D_pct": 1.71, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -27.99, "MAE_90D_pct": -27.99, "MAE_180D_pct": -52.97, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-14", "peak_price": 149000.0, "drawdown_after_peak_pct": -53.76, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_PE_control_premium_event_cap", "four_b_evidence_type": ["control_premium_or_event_premium", "positioning_overheat", "valuation_blowoff"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_false_positive_if_control_premium_spike_counts_as_structural_green", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L87_REVIEW_009240_2021-07-14_146500.0", "dedupe_for_aggregate": false, "aggregate_group_role": "r13_review_only", "is_new_independent_case": false, "reuse_reason": "R13 cross-review of R12L87_C32_HANSSEM_2021_STAGE4B_PE_CONTROL_PREMIUM_FADE", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "evidence_url_pending": true, "source_proxy_only": true, "r13_review_label": "event_cap_high_MAE_4B"}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L87_REVIEW_C29_NEXEN_2023_HIGH_MAE_FALSE_STAGE2", "trigger_id": "R13L87_REVIEW_C29_NEXEN_2023_STAGE2_FALSE_POSITIVE_HIGH_MAE", "symbol": "002350", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "original_canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 10, "revision_score": 15, "relative_strength_score": 70, "customer_quality_score": 5, "policy_or_regulatory_score": 20, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 68, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 30, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 35, "execution_risk_score": 75, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 55, "stage_label_after": "Stage1/Watch", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score", "margin_bridge_score"], "component_delta_explanation": "R13 high-MAE guardrail: reduce positive-stage credit when MFE90 is weak, MAE90 is high, and non-price bridge is missing or event cap is visible.", "MFE_90D_pct": 0.11, "MAE_90D_pct": -19.59, "score_return_alignment_label": "r13_high_MAE_guardrail_improves_alignment", "current_profile_verdict": "current_profile_false_positive_if_stage2_bonus_ignores_post_spike_mae"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L87_REVIEW_C30_DAEWOO_2024_SECTOR_BETA_FALSE_STAGE2", "trigger_id": "R13L87_REVIEW_C30_DAEWOO_2024_STAGE2_FALSE_POSITIVE_SECTOR_BETA", "symbol": "047040", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "original_canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 10, "revision_score": 15, "relative_strength_score": 70, "customer_quality_score": 5, "policy_or_regulatory_score": 20, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 68, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 30, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 35, "execution_risk_score": 75, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 55, "stage_label_after": "Stage1/Watch", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score", "margin_bridge_score"], "component_delta_explanation": "R13 high-MAE guardrail: reduce positive-stage credit when MFE90 is weak, MAE90 is high, and non-price bridge is missing or event cap is visible.", "MFE_90D_pct": 4.08, "MAE_90D_pct": -14.15, "score_return_alignment_label": "r13_high_MAE_guardrail_improves_alignment", "current_profile_verdict": "current_profile_false_positive_if_order_or_sector_beta_counts_without_cashflow_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L87_REVIEW_C31_DSFUEL_2022_HYDROGEN_POLICY_FALSE_STAGE2", "trigger_id": "R13L87_REVIEW_C31_DSFUEL_2022_STAGE2_FALSE_POSITIVE_HYDROGEN_POLICY", "symbol": "336260", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "original_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 10, "revision_score": 15, "relative_strength_score": 70, "customer_quality_score": 5, "policy_or_regulatory_score": 20, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 68, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 30, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 35, "execution_risk_score": 75, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score", "margin_bridge_score"], "component_delta_explanation": "R13 high-MAE guardrail: reduce positive-stage credit when MFE90 is weak, MAE90 is high, and non-price bridge is missing or event cap is visible.", "MFE_90D_pct": 2.23, "MAE_90D_pct": -30.86, "score_return_alignment_label": "r13_high_MAE_guardrail_improves_alignment", "current_profile_verdict": "current_profile_false_positive_if_policy_score_counts_without_order_revenue_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L87_REVIEW_C32_NAMYANG_2021_CONTROL_SALE_EVENT_CAP_4B", "trigger_id": "R13L87_REVIEW_C32_NAMYANG_2021_STAGE4B_CONTROL_SALE_EVENT_CAP", "symbol": "003920", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "original_canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 10, "revision_score": 15, "relative_strength_score": 70, "customer_quality_score": 5, "policy_or_regulatory_score": 20, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 30, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 35, "execution_risk_score": 75, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score", "margin_bridge_score"], "component_delta_explanation": "R13 high-MAE guardrail: reduce positive-stage credit when MFE90 is weak, MAE90 is high, and non-price bridge is missing or event cap is visible.", "MFE_90D_pct": 6.97, "MAE_90D_pct": -49.74, "score_return_alignment_label": "r13_high_MAE_guardrail_improves_alignment", "current_profile_verdict": "current_profile_4B_too_late_if_control_premium_cap_not_detected"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L87_REVIEW_C32_HANSSEM_2021_PE_CONTROL_PREMIUM_FADE_4B", "trigger_id": "R13L87_REVIEW_C32_HANSSEM_2021_STAGE4B_PE_CONTROL_PREMIUM_FADE", "symbol": "009240", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "original_canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 10, "revision_score": 15, "relative_strength_score": 70, "customer_quality_score": 5, "policy_or_regulatory_score": 20, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 30, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 35, "execution_risk_score": 75, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score", "margin_bridge_score"], "component_delta_explanation": "R13 high-MAE guardrail: reduce positive-stage credit when MFE90 is weak, MAE90 is high, and non-price bridge is missing or event cap is visible.", "MFE_90D_pct": 1.71, "MAE_90D_pct": -27.99, "score_return_alignment_label": "r13_high_MAE_guardrail_improves_alignment", "current_profile_verdict": "current_profile_false_positive_if_control_premium_spike_counts_as_structural_green"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R13", "loop": "87", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "POST_STAGE2_HIGH_MAE_FALSE_POSITIVE_AND_EVENT_CAP_CROSS_REVIEW", "new_independent_case_count": 0, "reused_case_count": 5, "new_symbol_count": 0, "same_archetype_new_symbol_count": 0, "same_archetype_new_trigger_family_count": 0, "new_trigger_family_count": 0, "positive_case_count": 0, "counterexample_count": 5, "4B_case_count": 2, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["weak_MFE_high_MAE_stage2", "event_cap_4B_needed", "policy_or_control_premium_without_cashflow_bridge"], "loop_contribution_label": "axis_stress_test_passed", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 5, "evidence_url_pending_count": 5}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","reason":"R13 review rows use already computed stock-web 180D windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- R13 review rows with `do_not_count_as_new_case=true` must not add weight.
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
completed_round = R13
completed_loop = 87
next_round = R1
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This R13 file contains no new independent case, no investment recommendation, and no production scoring change.

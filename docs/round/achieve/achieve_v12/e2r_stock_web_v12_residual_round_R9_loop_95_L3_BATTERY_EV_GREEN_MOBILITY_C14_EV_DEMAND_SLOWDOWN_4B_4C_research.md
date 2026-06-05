# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R9
scheduled_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = SEPARATOR_DEMAND_SLOWDOWN_4C_GUARD_VS_SEPARATOR_CAPACITY_RECOVERY_FALSE_STAGE2_AND_ELECTROLYTE_POST_CA_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | 4B_4C_guardrail_stress_test | stage2_actionable_bonus_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R9_loop_95_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
```

This file is the corrected final output for this execution. The scheduler state after R8 loop 95 is R9 / loop 95. R9 allows either the L3 mobility route or L9 construction route. This run uses the L3 mobility route and fills C14 EV demand slowdown / 4B / 4C behavior rather than repeating the immediately preceding R9 loop 94 C29 mobility volume/margin file.

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
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R9
scheduled_loop = 95
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
round_sector_consistency = pass
computed_next_round = R10
computed_next_loop = 95
```

C14 is not a long-positive rerating archetype by default. It is the emergency brake for EV demand slowdown: when customer call-off recovery, utilization stabilization, ASP/mix, margin and revision bridge are absent, the setup should route to 4B or 4C instead of Stage2/Stage3 promotion.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C14_EV_DEMAND_SLOWDOWN_4B_4C = 21 rows / 14 symbols / good-bad Stage2 3-3 / 4B-4C 6-4
top covered symbols include 006400(3), 373220(3), 095500(2), 247540(2), 278280(2), 003670(1)
previous R3 loop-91 C14 symbols avoided: 066970, 089980, 336370
previous R9 loop-93 C14 symbols avoided: 096770, 222080, 086520
previous R9 loop-94 C29 symbols avoided: 015750, 009900, 123410
previous R8 loop-95 C26 symbols avoided: 214320, 236810, 417860
```

Selected rows avoid hard duplicates and top repeated C14 symbols:

```text
361610 / Stage4C / 2024-01-24
393890 / Stage2-Actionable / 2024-02-22
025900 / Stage4B / 2024-06-10
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
| 361610 | atlas/symbol_profiles/361/361610.json | no corporate-action candidate |
| 393890 | atlas/symbol_profiles/393/393890.json | no corporate-action candidate |
| 025900 | atlas/symbol_profiles/025/025900.json | entry after 2024-05-03 corporate-action candidate boundary; post-boundary 180D window used with caveat |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R9L95_C14_SKIET_2024_SEPARATOR_DEMAND_SLOWDOWN_4C_GUARD_SUCCESS | 361610 | 2024-01-24 | yes | 180 | yes | yes | true |
| R9L95_C14_WCP_2024_SEPARATOR_CAPACITY_RECOVERY_FALSE_STAGE2 | 393890 | 2024-02-22 | yes | 180 | yes | yes | true |
| R9L95_C14_DONGWHA_2024_ELECTROLYTE_POST_CA_EV_DEMAND_EVENT_CAP_4B | 025900 | 2024-06-10 | yes | 180 | yes | caveated-clean | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C14_EV_DEMAND_SLOWDOWN_4B_4C | SEPARATOR_DEMAND_SLOWDOWN_4C_GUARD | Broken separator demand / utilization bridge should route to 4C protection. |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | SEPARATOR_CAPACITY_RECOVERY_FALSE_STAGE2 | Capacity-recovery watch without customer call-off and utilization bridge can become false Stage2. |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | ELECTROLYTE_POST_CA_EVENT_CAP_4B | Post-CA electrolyte/EV-demand rebound premium should route to 4B when call-off/utilization/margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R9L95_C14_SKIET_2024_SEPARATOR_DEMAND_SLOWDOWN_4C_GUARD_SUCCESS | 361610 | SK아이이테크놀로지 | positive guardrail / 4C | Early demand-slowdown guardrail avoided a tiny-MFE / huge-MAE trap. |
| R9L95_C14_WCP_2024_SEPARATOR_CAPACITY_RECOVERY_FALSE_STAGE2 | 393890 | 더블유씨피 | counterexample | Separator capacity-recovery watch had limited MFE and severe drawdown. |
| R9L95_C14_DONGWHA_2024_ELECTROLYTE_POST_CA_EV_DEMAND_EVENT_CAP_4B | 025900 | 동화기업 | counterexample / 4B | Post-CA electrolyte rebound capped quickly and then bled into high MAE. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 1
4C_case_count = 1
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
```

The positive case here is a **positive guardrail case**, not a long-side Stage3 winner. In C14, a good outcome can be early protection.

## 9. Evidence Source Map

| case | evidence status | evidence_url_pending | source_proxy_only | usage |
|---|---|---|---|---|
| SKIET separator demand-slowdown 4C guard | historical public/report proxy | true | true | guardrail success |
| WCP separator capacity recovery false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Dongwha post-CA electrolyte event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 361610 | atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv | atlas/symbol_profiles/361/361610.json |
| 393890 | atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv | atlas/symbol_profiles/393/393890.json |
| 025900 | atlas/ohlcv_tradable_by_symbol_year/025/025900/2024.csv | atlas/symbol_profiles/025/025900.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R9L95_C14_SKIET_2024_STAGE4C_SEPARATOR_DEMAND_SLOWDOWN_THESIS_BREAK_GUARD | 361610 | Stage4C | 2024-01-24 | 77400 | guardrail success | separator demand-slowdown thesis-break protection worked |
| R9L95_C14_WCP_2024_STAGE2_FALSE_POSITIVE_SEPARATOR_CAPACITY_RECOVERY_WATCH | 393890 | Stage2-Actionable | 2024-02-22 | 47100 | counterexample | separator recovery false Stage2 |
| R9L95_C14_DONGWHA_2024_STAGE4B_ELECTROLYTE_POST_CA_EV_DEMAND_EVENT_CAP | 025900 | Stage4B | 2024-06-10 | 19020 | counterexample/4B | electrolyte post-CA rebound event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R9L95_C14_SKIET_2024_STAGE4C_SEPARATOR_DEMAND_SLOWDOWN_THESIS_BREAK_GUARD | 77400 | 4.39 | -15.89 | 4.39 | -44.83 | 4.39 | -61.18 | 2024-02-02 | 80800 | -62.81 |
| R9L95_C14_WCP_2024_STAGE2_FALSE_POSITIVE_SEPARATOR_CAPACITY_RECOVERY_WATCH | 47100 | 5.10 | -16.56 | 5.10 | -37.79 | 5.10 | -44.80 | 2024-03-07 | 49500 | -47.47 |
| R9L95_C14_DONGWHA_2024_STAGE4B_ELECTROLYTE_POST_CA_EV_DEMAND_EVENT_CAP | 19020 | 3.89 | -34.49 | 3.89 | -45.11 | 3.89 | -51.89 | 2024-06-10 | 19760 | -53.64 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| hard_4c_thesis_break_routes_to_4c | strengthen: C14 needs earlier 4C when customer call-off / utilization / margin bridge breaks. |
| stage2_required_bridge | strengthen: separator/electrolyte rebound labels cannot promote without call-off recovery and utilization bridge. |
| local_4b_watch_guard | strengthen: post-CA or event rebounds should route to 4B when evidence is price-only. |
| high_MAE_guardrail | strengthen: C14 high-MAE rows are decisive rejection evidence. |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B / 4C Comparison

No confirmed Stage3-Green row is introduced. C14 is a defensive archetype in this loop.

| symbol | stage quality | explanation |
|---|---|---|
| 361610 | good_4C_guard | Tiny MFE and huge 90D/180D MAE confirm early thesis-break protection. |
| 393890 | bad_stage2 | Separator recovery watch lacked call-off/utilization/margin bridge and produced high MAE. |
| 025900 | good_4B | Post-CA electrolyte rebound premium capped and then drew down sharply. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 361610 separator demand slowdown 4C | 0.96 | 0.96 | hard 4C guard should block positive-stage promotion |
| 393890 separator false Stage2 | 0.95 | 0.95 | false Stage2 due missing customer call-off / utilization / margin bridge |
| 025900 electrolyte post-CA cap | 0.96 | 0.96 | good 4B timing after post-CA EV-demand rebound event premium |

## 16. 4C Protection Audit

```text
4C_case_count = 1
four_c_protection_label = hard_4c_thesis_break_routes_to_4c for 361610
false_4C_avoidance_count = 0
```

R9 loop 95 explicitly strengthens C14 4C protection. This is useful because the archetype is not a normal “buy the dip” family; it is a demand-slowdown guardrail.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L3 EV demand-slowdown cases, Stage2 requires verified customer call-off recovery, utilization stabilization, ASP/mix, margin, or revision bridge. Separator, electrolyte, battery material, EV rebound, capacity recovery, IRA/AMPC or post-CA rebound label alone remains watch/4B/4C.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
rule = C14 should reward early 4B/4C protection when the customer call-off / utilization / margin bridge breaks. Tiny forward MFE plus high MAE is not a late-entry problem; it is confirmation that the row should never have been promoted as positive Stage2/Stage3.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 4.46 | -42.58 | 1.00 | C14 defensive routing remains necessary |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 4.46 | -42.58 | 1.00 | weaker 4B/4C separation |
| P1 sector_specific_candidate_profile | L3 call-off/utilization/margin bridge required | 2 | 4.50 | -41.45 | 1.00 | better rejection fit |
| P2 canonical_archetype_candidate_profile | C14 4B/4C guard-first profile | 3 | 4.46 | -42.58 | 1.00 | best explanatory fit |
| P3 hard_4c_guard_profile | route thesis-break rows directly to 4C | 1 | 4.39 | -44.83 | 1.00 | safest for separator demand slowdown |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 361610 separator demand slowdown | 62 | Stage2-Watch | 45 | Stage4C-protection | 4.39 | -44.83 | 4C_guardrail_success_separator_demand_slowdown |
| 393890 separator recovery false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 5.10 | -37.79 | separator_capacity_recovery_false_stage2 |
| 025900 electrolyte post-CA cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 3.89 | -45.11 | electrolyte_post_CA_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "SEPARATOR_DEMAND_SLOWDOWN_4C_GUARD_VS_SEPARATOR_CAPACITY_RECOVERY_FALSE_STAGE2_AND_ELECTROLYTE_POST_CA_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 1, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 1, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C14 SKIET separator demand-slowdown 4C guardrail success, WCP separator capacity-recovery false Stage2, and Dongwha electrolyte post-CA EV-demand event-cap 4B split while avoiding top repeated C14 and previous R9/R3 loop symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: separator_demand_slowdown_4C_guard_success, separator_capacity_recovery_false_stage2, electrolyte_post_CA_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
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
- C14 EV demand slowdown 4B/4C guardrail split
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
shadow_weight,hard_4c_thesis_break_routes_to_4c,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,configured,C14_routes_broken_customer_calloff_utilization_margin_bridge_to_4C_or_4B,0,"C14 should treat broken customer call-off, utilization and margin bridge as protection evidence, not as a positive Stage2/Stage3 setup","SKIET had MFE90=4.39 and MAE180=-61.18 after separator demand-slowdown thesis broke; WCP and Dongwha also showed high MAE after bridge-missing rebounds","R9L95_C14_SKIET_2024_STAGE4C_SEPARATOR_DEMAND_SLOWDOWN_THESIS_BREAK_GUARD|R9L95_C14_WCP_2024_STAGE2_FALSE_POSITIVE_SEPARATOR_CAPACITY_RECOVERY_WATCH|R9L95_C14_DONGWHA_2024_STAGE4B_ELECTROLYTE_POST_CA_EV_DEMAND_EVENT_CAP",3,3,2,medium,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,stage2_required_bridge,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,configured,C14_requires_customer_calloff_recovery_utilization_pricing_margin_revision_bridge_before_stage2_promotion,0,"EV demand recovery or separator/electrolyte rebound labels cannot promote without call-off recovery, utilization, ASP/mix, margin and revision bridge","WCP false Stage2 and Dongwha 4B event cap showed bridge-missing rebound failure","R9L95_C14_WCP_2024_STAGE2_FALSE_POSITIVE_SEPARATOR_CAPACITY_RECOVERY_WATCH|R9L95_C14_DONGWHA_2024_STAGE4B_ELECTROLYTE_POST_CA_EV_DEMAND_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"false Stage2 rows strengthen bridge requirement only"
shadow_weight,high_MAE_guardrail,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,configured,block_positive_stage_when_EV_demand_slowdown_theme_has_high_MAE_without_recovery_bridge,0,"High or persistent MAE after bridge-missing EV demand slowdown entries should block Stage2/Stage3 promotion unless customer call-off and utilization evidence survives","SKIET MAE90=-44.83; WCP MAE90=-37.79; Dongwha MAE90=-45.11","R9L95_C14_SKIET_2024_STAGE4C_SEPARATOR_DEMAND_SLOWDOWN_THESIS_BREAK_GUARD|R9L95_C14_WCP_2024_STAGE2_FALSE_POSITIVE_SEPARATOR_CAPACITY_RECOVERY_WATCH|R9L95_C14_DONGWHA_2024_STAGE4B_ELECTROLYTE_POST_CA_EV_DEMAND_EVENT_CAP",3,3,2,high,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R9L95_C14_SKIET_2024_SEPARATOR_DEMAND_SLOWDOWN_4C_GUARD_SUCCESS", "symbol": "361610", "company_name": "SK아이이테크놀로지", "round": "R9", "loop": "95", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "SEPARATOR_DEMAND_SLOWDOWN_4C_GUARD_VS_SEPARATOR_CAPACITY_RECOVERY_FALSE_STAGE2_AND_ELECTROLYTE_POST_CA_EVENT_CAP", "case_type": "guardrail_success_4C_thesis_break", "positive_or_counterexample": "positive_guardrail", "best_trigger": "R9L95_C14_SKIET_2024_STAGE4C_SEPARATOR_DEMAND_SLOWDOWN_THESIS_BREAK_GUARD", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "EV separator demand-slowdown / utilization thesis-break guard worked: forward MFE stayed tiny while 90D/180D MAE became severe. C14 should reward early protection, not positive-stage promotion, when customer volume, utilization and margin bridge breaks.", "current_profile_verdict": "current_profile_kept_but_C14_needs_earlier_4C_when_separator_utilization_and_customer_volume_bridge_breaks", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. This is a positive guardrail case, not a long positive rerating case."}
{"row_type": "case", "case_id": "R9L95_C14_WCP_2024_SEPARATOR_CAPACITY_RECOVERY_FALSE_STAGE2", "symbol": "393890", "company_name": "더블유씨피", "round": "R9", "loop": "95", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "SEPARATOR_DEMAND_SLOWDOWN_4C_GUARD_VS_SEPARATOR_CAPACITY_RECOVERY_FALSE_STAGE2_AND_ELECTROLYTE_POST_CA_EVENT_CAP", "case_type": "failed_rerating_separator_capacity_recovery_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R9L95_C14_WCP_2024_STAGE2_FALSE_POSITIVE_SEPARATOR_CAPACITY_RECOVERY_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Separator capacity-recovery watch produced only limited MFE and then deep MAE. C14 Stage2 should not be awarded without confirmed EV customer call-off recovery, utilization stabilization, pricing/mix, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_separator_capacity_recovery_watch_counts_without_customer_calloff_utilization_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Market segment changed to KOSDAQ GLOBAL in 2024 but OHLC remains tradable raw and usable."}
{"row_type": "case", "case_id": "R9L95_C14_DONGWHA_2024_ELECTROLYTE_POST_CA_EV_DEMAND_EVENT_CAP_4B", "symbol": "025900", "company_name": "동화기업", "round": "R9", "loop": "95", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "SEPARATOR_DEMAND_SLOWDOWN_4C_GUARD_VS_SEPARATOR_CAPACITY_RECOVERY_FALSE_STAGE2_AND_ELECTROLYTE_POST_CA_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R9L95_C14_DONGWHA_2024_STAGE4B_ELECTROLYTE_POST_CA_EV_DEMAND_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Post-2024-05-03 electrolyte/battery-material event premium capped after the June rebound and then de-rated. C14 should route bridge-missing electrolyte/EV-demand rebound rows to 4B when call-off, utilization, ASP/mix and margin bridge remain absent.", "current_profile_verdict": "current_profile_4B_too_late_if_electrolyte_post_CA_EV_demand_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Profile flags a 2024-05-03 corporate-action candidate. Entry is after that boundary, so the post-boundary 180D window is used with caveat."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R9L95_C14_SKIET_2024_STAGE4C_SEPARATOR_DEMAND_SLOWDOWN_THESIS_BREAK_GUARD", "case_id": "R9L95_C14_SKIET_2024_SEPARATOR_DEMAND_SLOWDOWN_4C_GUARD_SUCCESS", "symbol": "361610", "company_name": "SK아이이테크놀로지", "round": "R9", "loop": "95", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "SEPARATOR_DEMAND_SLOWDOWN_4C_GUARD_VS_SEPARATOR_CAPACITY_RECOVERY_FALSE_STAGE2_AND_ELECTROLYTE_POST_CA_EVENT_CAP", "sector": "EV_separator_customer_calloff_utilization_demand_slowdown", "primary_archetype": "separator_demand_slowdown_thesis_break_4C_guard", "loop_objective": "coverage_gap_fill | counterexample_mining | 4B_4C_guardrail_stress_test | stage2_actionable_bonus_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4C", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 77400.0, "evidence_available_at_that_date": "EV separator demand-slowdown / customer call-off / utilization-risk watch; bridge requires customer volume recovery, utilization stabilization, pricing/mix and margin revision, exact as-of URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["separator_customer_calloff_risk", "utilization_slowdown_watch", "margin_revision_risk"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_MFE90", "high_MAE90", "price_only_bounce_rejection"], "stage4c_evidence_fields": ["thesis_break_separator_utilization", "customer_volume_bridge_broken", "persistent_180D_drawdown"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv", "profile_path": "atlas/symbol_profiles/361/361610.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.39, "MFE_90D_pct": 4.39, "MFE_180D_pct": 4.39, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -15.89, "MAE_90D_pct": -44.83, "MAE_180D_pct": -61.18, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-02", "peak_price": 80800.0, "drawdown_after_peak_pct": -62.81, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "Stage4C_guard_success_separator_demand_slowdown_thesis_break_should_block_positive_stage", "four_b_evidence_type": ["separator_demand_slowdown", "high_MAE", "bridge_broken"], "four_c_protection_label": "hard_4c_thesis_break_routes_to_4c", "trigger_outcome_label": "good_4C_separator_demand_slowdown_guard_success", "current_profile_verdict": "current_profile_kept_but_C14_needs_earlier_4C_when_separator_utilization_and_customer_volume_bridge_breaks", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R9L95_C14_361610_2024-01-24_77400", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_guardrail_overlay", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R9L95_C14_WCP_2024_STAGE2_FALSE_POSITIVE_SEPARATOR_CAPACITY_RECOVERY_WATCH", "case_id": "R9L95_C14_WCP_2024_SEPARATOR_CAPACITY_RECOVERY_FALSE_STAGE2", "symbol": "393890", "company_name": "더블유씨피", "round": "R9", "loop": "95", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "SEPARATOR_DEMAND_SLOWDOWN_4C_GUARD_VS_SEPARATOR_CAPACITY_RECOVERY_FALSE_STAGE2_AND_ELECTROLYTE_POST_CA_EVENT_CAP", "sector": "EV_separator_capacity_recovery_calloff_watch", "primary_archetype": "separator_capacity_recovery_watch_without_customer_calloff_utilization_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | 4B_4C_guardrail_stress_test | stage2_actionable_bonus_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-22", "entry_date": "2024-02-22", "entry_price": 47100.0, "evidence_available_at_that_date": "EV separator capacity recovery / utilization rebound watch without confirmed customer call-off recovery, pricing/mix or margin revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["separator_capacity_recovery_watch", "EV_demand_rebound_theme", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["limited_MFE90", "deep_MAE90", "customer_calloff_utilization_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv", "profile_path": "atlas/symbol_profiles/393/393890.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.1, "MFE_90D_pct": 5.1, "MFE_180D_pct": 5.1, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -16.56, "MAE_90D_pct": -37.79, "MAE_180D_pct": -44.8, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-07", "peak_price": 49500.0, "drawdown_after_peak_pct": -47.47, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.95, "four_b_timing_verdict": "separator_capacity_recovery_watch_was_false_stage2_due_missing_customer_calloff_utilization_margin_bridge", "four_b_evidence_type": ["separator_recovery_premium", "bridge_missing", "high_MAE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_separator_capacity_recovery_without_utilization_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_separator_capacity_recovery_watch_counts_without_customer_calloff_utilization_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R9L95_C14_393890_2024-02-22_47100", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R9L95_C14_DONGWHA_2024_STAGE4B_ELECTROLYTE_POST_CA_EV_DEMAND_EVENT_CAP", "case_id": "R9L95_C14_DONGWHA_2024_ELECTROLYTE_POST_CA_EV_DEMAND_EVENT_CAP_4B", "symbol": "025900", "company_name": "동화기업", "round": "R9", "loop": "95", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "SEPARATOR_DEMAND_SLOWDOWN_4C_GUARD_VS_SEPARATOR_CAPACITY_RECOVERY_FALSE_STAGE2_AND_ELECTROLYTE_POST_CA_EVENT_CAP", "sector": "electrolyte_EV_demand_rebound_post_CA_event_premium", "primary_archetype": "electrolyte_post_CA_EV_demand_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | 4B_4C_guardrail_stress_test | stage2_actionable_bonus_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-06-10", "entry_date": "2024-06-10", "entry_price": 19020.0, "evidence_available_at_that_date": "post-2024-05-03 electrolyte / EV demand rebound event premium without confirmed customer call-off recovery, utilization or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["electrolyte_EV_demand_event", "post_CA_rebound_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE90", "calloff_utilization_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/025/025900/2024.csv", "profile_path": "atlas/symbol_profiles/025/025900.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.89, "MFE_90D_pct": 3.89, "MFE_180D_pct": 3.89, "MFE_1Y_pct": "not_calculated_due_post_CA_boundary_window", "MFE_2Y_pct": "not_calculated_due_post_CA_boundary_window", "MAE_30D_pct": -34.49, "MAE_90D_pct": -45.11, "MAE_180D_pct": -51.89, "MAE_1Y_pct": "not_calculated_due_post_CA_boundary_window", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-10", "peak_price": 19760.0, "drawdown_after_peak_pct": -53.64, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "good_full_window_4B_timing_electrolyte_post_CA_EV_demand_event_cap", "four_b_evidence_type": ["electrolyte_event_premium", "post_CA_rebound", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_electrolyte_post_CA_EV_demand_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_electrolyte_post_CA_EV_demand_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "post_2024-05-03_CA_candidate_boundary_clean_window_with_caveat", "same_entry_group_id": "R9L95_C14_025900_2024-06-10_19020", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L95_C14_SKIET_2024_SEPARATOR_DEMAND_SLOWDOWN_4C_GUARD_SUCCESS", "trigger_id": "R9L95_C14_SKIET_2024_STAGE4C_SEPARATOR_DEMAND_SLOWDOWN_THESIS_BREAK_GUARD", "symbol": "361610", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 60, "customer_quality_score": 40, "policy_or_regulatory_score": 20, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 62, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 10, "customer_quality_score": 15, "policy_or_regulatory_score": 10, "valuation_repricing_score": 20, "execution_risk_score": 95, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 45, "stage_label_after": "Stage4C-protection", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "separator_demand_slowdown_4C_guard_success", "MFE_90D_pct": 4.39, "MAE_90D_pct": -44.83, "score_return_alignment_label": "4C_guardrail_success_separator_demand_slowdown", "current_profile_verdict": "current_profile_kept_but_C14_needs_earlier_4C_when_separator_utilization_and_customer_volume_bridge_breaks"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L95_C14_WCP_2024_SEPARATOR_CAPACITY_RECOVERY_FALSE_STAGE2", "trigger_id": "R9L95_C14_WCP_2024_STAGE2_FALSE_POSITIVE_SEPARATOR_CAPACITY_RECOVERY_WATCH", "symbol": "393890", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 65, "customer_quality_score": 35, "policy_or_regulatory_score": 20, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 15, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "separator_capacity_recovery_false_stage2", "MFE_90D_pct": 5.1, "MAE_90D_pct": -37.79, "score_return_alignment_label": "separator_capacity_recovery_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_separator_capacity_recovery_watch_counts_without_customer_calloff_utilization_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L95_C14_DONGWHA_2024_ELECTROLYTE_POST_CA_EV_DEMAND_EVENT_CAP_4B", "trigger_id": "R9L95_C14_DONGWHA_2024_STAGE4B_ELECTROLYTE_POST_CA_EV_DEMAND_EVENT_CAP", "symbol": "025900", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 20, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "electrolyte_post_CA_EV_demand_event_cap_4B_guard", "MFE_90D_pct": 3.89, "MAE_90D_pct": -45.11, "score_return_alignment_label": "electrolyte_post_CA_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_electrolyte_post_CA_EV_demand_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R9", "loop": "95", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "SEPARATOR_DEMAND_SLOWDOWN_4C_GUARD_VS_SEPARATOR_CAPACITY_RECOVERY_FALSE_STAGE2_AND_ELECTROLYTE_POST_CA_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 1, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "hard_4c_thesis_break_routes_to_4c", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["separator_demand_slowdown_4C_guard_success", "separator_capacity_recovery_false_stage2", "electrolyte_post_CA_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- False-positive rows should strengthen bridge requirements, not generate positive promotion.
- C14 rows need explicit customer call-off recovery, utilization stabilization, ASP/mix, margin or revision bridge before Stage2 promotion.
- In C14, tiny MFE plus high MAE should strengthen 4B/4C routing, not dip-buy promotion.
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
10. Add tests that bridge-missing C14 rows cannot promote positive stages and can route to 4B/4C.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R9
completed_loop = 95
next_round = R10
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.

# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R5
scheduled_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = RAMEN_FOOD_EXPORT_CHANNEL_REORDER_BRIDGE_VS_DOMESTIC_FOOD_CHANNEL_FALSE_STAGE2_AND_BAKERY_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R5_loop_92_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
```

This file is the corrected final output for this execution. The scheduler state after R4 loop 92 is R5 / loop 92. It fills C18 consumer export channel reorder behavior after the prior R5 loop 91 used C20, loop 90 used C19, and loop 89 used C18 with different symbols.

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
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R5
scheduled_loop = 92
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
round_sector_consistency = pass
computed_next_round = R6
computed_next_loop = 92
```

R5 permits L5 consumer / brand / distribution research. This loop avoids the previous R5 C18/C19/C20 symbol sets and uses a fresh food export channel split.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C18_CONSUMER_EXPORT_CHANNEL_REORDER = 38 rows / 19 symbols / good-bad Stage2 17-9 / 4B-4C 0-0
top covered symbols include 001680(4), 280360(4), UNKNOWN_SYMBOL(4), 049770(3), 271560(3), 003960(2)
previous R5 loop-89 C18 symbols avoided: 018290, 078520, 123690
previous R5 loop-90 C19 symbols avoided: 036620, 031430, 366030
previous R5 loop-91 C20 symbols avoided: 090430, 051900, 097950
previous R4 loop-92 C16 symbols avoided: 006260, 012800, 025820
```

Selected rows avoid hard duplicates and top repeated C18 symbols:

```text
004370 / Stage2-Actionable / 2024-04-11
007310 / Stage2-Actionable / 2024-06-13
005610 / Stage4B / 2024-06-14
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
| 004370 | atlas/symbol_profiles/004/004370.json | selected 2024 window clean after old 1997/2000/2003 CA candidates |
| 007310 | atlas/symbol_profiles/007/007310.json | no corporate-action candidate |
| 005610 | atlas/symbol_profiles/005/005610.json | selected 2024 window clean after old 1996/1997/1999/2002 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R5L92_C18_NONGSHIM_2024_RAMEN_EXPORT_CHANNEL_REORDER_POSITIVE | 004370 | 2024-04-11 | yes | 180 | yes | yes | true |
| R5L92_C18_OTTOGI_2024_DOMESTIC_FOOD_CHANNEL_FALSE_STAGE2 | 007310 | 2024-06-13 | yes | 180 | yes | yes | true |
| R5L92_C18_SPCSAMLIP_2024_BAKERY_CHANNEL_EVENT_CAP_4B | 005610 | 2024-06-14 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | RAMEN_FOOD_EXPORT_CHANNEL_REORDER_BRIDGE | Positive Stage2 requires overseas sell-through, reorder, distribution expansion, ASP/mix, margin and revision bridge. |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | DOMESTIC_FOOD_CHANNEL_FALSE_STAGE2 | Domestic channel catch-up without export reorder bridge can become false Stage2. |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | BAKERY_CHANNEL_EVENT_CAP_4B | Food-channel event premium should route to 4B when sell-through and margin evidence are capped or missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R5L92_C18_NONGSHIM_2024_RAMEN_EXPORT_CHANNEL_REORDER_POSITIVE | 004370 | 농심 | positive | Food export channel/reorder bridge produced high MFE with shallow early MAE. |
| R5L92_C18_OTTOGI_2024_DOMESTIC_FOOD_CHANNEL_FALSE_STAGE2 | 007310 | 오뚜기 | counterexample | Domestic food channel catch-up spike had limited forward MFE and later drawdown. |
| R5L92_C18_SPCSAMLIP_2024_BAKERY_CHANNEL_EVENT_CAP_4B | 005610 | SPC삼립 | counterexample / 4B | Bakery/food channel event premium capped near the June spike and then de-rated. |

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
| Nongshim ramen export channel reorder | historical public/report proxy | true | true | shadow-only positive |
| Ottogi domestic food channel false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| SPC Samlip bakery channel event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 004370 | atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv | atlas/symbol_profiles/004/004370.json |
| 007310 | atlas/ohlcv_tradable_by_symbol_year/007/007310/2024.csv | atlas/symbol_profiles/007/007310.json |
| 005610 | atlas/ohlcv_tradable_by_symbol_year/005/005610/2024.csv | atlas/symbol_profiles/005/005610.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R5L92_C18_NONGSHIM_2024_STAGE2_ACTIONABLE_RAMEN_EXPORT_CHANNEL_REORDER | 004370 | Stage2-Actionable | 2024-04-11 | 371500 | positive | food export channel/reorder bridge worked |
| R5L92_C18_OTTOGI_2024_STAGE2_FALSE_POSITIVE_DOMESTIC_FOOD_CHANNEL_CATCHUP | 007310 | Stage2-Actionable | 2024-06-13 | 485500 | counterexample | domestic food channel false Stage2 |
| R5L92_C18_SPCSAMLIP_2024_STAGE4B_BAKERY_CHANNEL_EVENT_CAP | 005610 | Stage4B | 2024-06-14 | 65500 | counterexample/4B | bakery food-channel event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R5L92_C18_NONGSHIM_2024_STAGE2_ACTIONABLE_RAMEN_EXPORT_CHANNEL_REORDER | 371500 | 17.36 | -2.96 | 61.24 | -2.96 | 61.24 | -3.10 | 2024-06-13 | 599000 | -39.90 |
| R5L92_C18_OTTOGI_2024_STAGE2_FALSE_POSITIVE_DOMESTIC_FOOD_CHANNEL_CATCHUP | 485500 | 5.66 | -15.14 | 5.66 | -20.39 | 5.66 | -20.39 | 2024-06-13 | 513000 | -24.66 |
| R5L92_C18_SPCSAMLIP_2024_STAGE4B_BAKERY_CHANNEL_EVENT_CAP | 65500 | 1.83 | -17.25 | 1.83 | -25.42 | 1.83 | -25.42 | 2024-06-14 | 66700 | -26.76 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C18 Stage2 needs export sell-through / distributor reorder / margin / revision bridge |
| local_4b_watch_guard | strengthen: food-channel event premiums should route to 4B watch when bridge is missing |
| high_MAE_guardrail | strengthen: high/persistent MAE channel rows cannot promote without durable reorder bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is export-channel reorder bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 004370 | good_stage2 | Export sell-through/reorder bridge produced high MFE with shallow MAE. |
| 007310 | bad_stage2 | Domestic food channel catch-up lacked export reorder bridge and had limited MFE. |
| 005610 | good_4B | Food-channel event premium capped at the June spike. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 007310 domestic food channel false Stage2 | 0.95 | 0.95 | false Stage2 due missing export reorder/margin bridge |
| 005610 bakery channel cap | 0.98 | 0.98 | good full-window 4B timing |
| 004370 export channel bridge | n/a | n/a | positive Stage2, but later channel valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 007310 / 005610
```

No hard 4C candidate is proposed. R5 loop 92 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L5 consumer export channel reorder cases, Stage2 requires verified overseas sell-through, distributor reorder, channel expansion, ASP/mix, gross-margin recovery, or revision bridge. Food, ramen, bakery, domestic channel, export sympathy, or channel-recovery label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
rule = C18 should split true export-channel reorder positives from domestic channel false Stage2 and food-channel event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 22.91 | -16.26 | 0.67 | mixed; C18 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 22.91 | -16.26 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L5 export reorder/margin bridge required | 2 | 33.45 | -11.68 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C18 bridge vs event-cap split | 2 | 33.45 | -11.68 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing channel themes as positive | 1 | 61.24 | -2.96 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 004370 export channel bridge | 66 | Stage2-Watch | 75 | Stage2-Actionable | 61.24 | -2.96 | food_export_channel_reorder_positive |
| 007310 domestic false | 66 | Stage2-Actionable | 53 | Stage1/Watch | 5.66 | -20.39 | domestic_food_channel_false_stage2 |
| 005610 bakery channel cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 1.83 | -25.42 | bakery_food_channel_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "RAMEN_FOOD_EXPORT_CHANNEL_REORDER_BRIDGE_VS_DOMESTIC_FOOD_CHANNEL_FALSE_STAGE2_AND_BAKERY_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C18 food export channel reorder positive, domestic-food channel false Stage2, and bakery/food channel event-cap 4B split using non-top-covered symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: food_export_channel_reorder_positive, domestic_food_channel_false_stage2, bakery_food_channel_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail
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
- C18 consumer export channel reorder bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,configured,C18_requires_export_sellthrough_reorder_distribution_margin_revision_bridge,0,"C18 Stage2 should require overseas sell-through, reorder, distribution expansion, ASP/mix, margin, or revision bridge, not food/export/channel label alone","Nongshim positive worked; Ottogi and SPC Samlip event/watch rows failed positive-stage promotion","R5L92_C18_NONGSHIM_2024_STAGE2_ACTIONABLE_RAMEN_EXPORT_CHANNEL_REORDER|R5L92_C18_OTTOGI_2024_STAGE2_FALSE_POSITIVE_DOMESTIC_FOOD_CHANNEL_CATCHUP|R5L92_C18_SPCSAMLIP_2024_STAGE4B_BAKERY_CHANNEL_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,configured,cap_bridge_missing_food_channel_event_premiums_as_4B_watch,0,"Food/export/channel event premiums can peak before distributor reorder and margin bridge is proven","Ottogi had limited forward MFE after June catch-up spike; SPC Samlip showed event-cap behavior after June channel spike","R5L92_C18_OTTOGI_2024_STAGE2_FALSE_POSITIVE_DOMESTIC_FOOD_CHANNEL_CATCHUP|R5L92_C18_SPCSAMLIP_2024_STAGE4B_BAKERY_CHANNEL_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,configured,block_positive_stage_when_channel_theme_has_high_or_persistent_MAE_without_reorder_bridge,0,"High or persistent MAE after a bridge-missing consumer channel entry should block Stage2/Stage3 promotion unless export reorder and margin evidence survives","Ottogi MAE90=-20.39 and SPC Samlip MAE90=-25.42","R5L92_C18_OTTOGI_2024_STAGE2_FALSE_POSITIVE_DOMESTIC_FOOD_CHANNEL_CATCHUP|R5L92_C18_SPCSAMLIP_2024_STAGE4B_BAKERY_CHANNEL_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R5L92_C18_NONGSHIM_2024_RAMEN_EXPORT_CHANNEL_REORDER_POSITIVE", "symbol": "004370", "company_name": "농심", "round": "R5", "loop": "92", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "RAMEN_FOOD_EXPORT_CHANNEL_REORDER_BRIDGE_VS_DOMESTIC_FOOD_CHANNEL_FALSE_STAGE2_AND_BAKERY_EVENT_CAP", "case_type": "structural_success_with_later_channel_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R5L92_C18_NONGSHIM_2024_STAGE2_ACTIONABLE_RAMEN_EXPORT_CHANNEL_REORDER", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Ramen / food export channel reorder bridge produced high 30D/90D MFE with shallow initial MAE. C18 works when consumer export narrative maps into overseas sell-through, reorder, distribution channel expansion, margin and revision bridge, but later channel/valuation watch is still needed.", "current_profile_verdict": "current_profile_kept_but_C18_positive_requires_export_sellthrough_reorder_margin_revision_bridge_not_food_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1997/2000/2003 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R5L92_C18_OTTOGI_2024_DOMESTIC_FOOD_CHANNEL_FALSE_STAGE2", "symbol": "007310", "company_name": "오뚜기", "round": "R5", "loop": "92", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "RAMEN_FOOD_EXPORT_CHANNEL_REORDER_BRIDGE_VS_DOMESTIC_FOOD_CHANNEL_FALSE_STAGE2_AND_BAKERY_EVENT_CAP", "case_type": "failed_rerating_domestic_channel_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R5L92_C18_OTTOGI_2024_STAGE2_FALSE_POSITIVE_DOMESTIC_FOOD_CHANNEL_CATCHUP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Domestic food / ramen export catch-up watch had limited forward MFE after the June spike and then meaningful 90D MAE. C18 Stage2 should not be awarded without overseas sell-through, distributor reorder, ASP/mix, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_domestic_food_channel_catchup_counts_without_export_reorder_margin_bridge", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action caveat in selected window. Source-proxy only."}
{"row_type": "case", "case_id": "R5L92_C18_SPCSAMLIP_2024_BAKERY_CHANNEL_EVENT_CAP_4B", "symbol": "005610", "company_name": "SPC삼립", "round": "R5", "loop": "92", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "RAMEN_FOOD_EXPORT_CHANNEL_REORDER_BRIDGE_VS_DOMESTIC_FOOD_CHANNEL_FALSE_STAGE2_AND_BAKERY_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R5L92_C18_SPCSAMLIP_2024_STAGE4B_BAKERY_CHANNEL_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Bakery/food channel event premium capped around the June spike and then drew down. C18 should route bridge-missing consumer channel event premiums to 4B unless sell-through, reorder, distribution expansion, pricing and margin bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_bakery_food_channel_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1996/1997/1999/2002 CA candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R5L92_C18_NONGSHIM_2024_STAGE2_ACTIONABLE_RAMEN_EXPORT_CHANNEL_REORDER", "case_id": "R5L92_C18_NONGSHIM_2024_RAMEN_EXPORT_CHANNEL_REORDER_POSITIVE", "symbol": "004370", "company_name": "농심", "round": "R5", "loop": "92", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "RAMEN_FOOD_EXPORT_CHANNEL_REORDER_BRIDGE_VS_DOMESTIC_FOOD_CHANNEL_FALSE_STAGE2_AND_BAKERY_EVENT_CAP", "sector": "ramen_food_export_channel_reorder", "primary_archetype": "food_export_sellthrough_reorder_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-11", "entry_date": "2024-04-11", "entry_price": 371500.0, "evidence_available_at_that_date": "ramen/food export channel, overseas sell-through, reorder, distributor expansion, ASP/mix and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["export_channel_sellthrough_proxy", "overseas_reorder_bridge", "distribution_expansion_proxy", "margin_revision_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["positive_MFE30", "high_MFE90", "shallow_MAE90"], "stage4b_evidence_fields": ["later_channel_valuation_watch", "positioning_overheat_watch"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv", "profile_path": "atlas/symbol_profiles/004/004370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 17.36, "MFE_90D_pct": 61.24, "MFE_180D_pct": 61.24, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -2.96, "MAE_90D_pct": -2.96, "MAE_180D_pct": -3.1, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-13", "peak_price": 599000.0, "drawdown_after_peak_pct": -39.9, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_food_export_channel_valuation_watch_needed", "four_b_evidence_type": ["valuation_repricing", "positioning_overheat", "export_channel_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_food_export_channel_reorder_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_CA", "same_entry_group_id": "R5L92_C18_004370_2024-04-11_371500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R5L92_C18_OTTOGI_2024_STAGE2_FALSE_POSITIVE_DOMESTIC_FOOD_CHANNEL_CATCHUP", "case_id": "R5L92_C18_OTTOGI_2024_DOMESTIC_FOOD_CHANNEL_FALSE_STAGE2", "symbol": "007310", "company_name": "오뚜기", "round": "R5", "loop": "92", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "RAMEN_FOOD_EXPORT_CHANNEL_REORDER_BRIDGE_VS_DOMESTIC_FOOD_CHANNEL_FALSE_STAGE2_AND_BAKERY_EVENT_CAP", "sector": "domestic_food_channel_catchup_export_watch", "primary_archetype": "food_channel_catchup_without_export_reorder_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-06-13", "entry_date": "2024-06-13", "entry_price": 485500.0, "evidence_available_at_that_date": "domestic food / ramen export catch-up and channel recovery watch proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["food_channel_catchup_watch", "export_peer_sympathy", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["limited_MFE90", "export_reorder_margin_bridge_missing", "post_spike_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/007/007310/2024.csv", "profile_path": "atlas/symbol_profiles/007/007310.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.66, "MFE_90D_pct": 5.66, "MFE_180D_pct": 5.66, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -15.14, "MAE_90D_pct": -20.39, "MAE_180D_pct": -20.39, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-13", "peak_price": 513000.0, "drawdown_after_peak_pct": -24.66, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.95, "four_b_timing_verdict": "domestic_food_channel_catchup_was_false_stage2_due_missing_export_reorder_margin_bridge", "four_b_evidence_type": ["food_channel_catchup_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_domestic_food_channel_without_export_reorder_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_domestic_food_channel_catchup_counts_without_export_reorder_margin_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R5L92_C18_007310_2024-06-13_485500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R5L92_C18_SPCSAMLIP_2024_STAGE4B_BAKERY_CHANNEL_EVENT_CAP", "case_id": "R5L92_C18_SPCSAMLIP_2024_BAKERY_CHANNEL_EVENT_CAP_4B", "symbol": "005610", "company_name": "SPC삼립", "round": "R5", "loop": "92", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "RAMEN_FOOD_EXPORT_CHANNEL_REORDER_BRIDGE_VS_DOMESTIC_FOOD_CHANNEL_FALSE_STAGE2_AND_BAKERY_EVENT_CAP", "sector": "bakery_food_channel_event_premium", "primary_archetype": "bakery_food_channel_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-06-14", "entry_date": "2024-06-14", "entry_price": 65500.0, "evidence_available_at_that_date": "bakery/food channel event premium and distribution recovery watch after June spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["bakery_food_channel_event_premium", "distribution_recovery_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "limited_MFE90", "sellthrough_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005610/2024.csv", "profile_path": "atlas/symbol_profiles/005/005610.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.83, "MFE_90D_pct": 1.83, "MFE_180D_pct": 1.83, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -17.25, "MAE_90D_pct": -25.42, "MAE_180D_pct": -25.42, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-14", "peak_price": 66700.0, "drawdown_after_peak_pct": -26.76, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "good_full_window_4B_timing_bakery_food_channel_event_cap", "four_b_evidence_type": ["food_channel_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_bakery_food_channel_premium", "current_profile_verdict": "current_profile_4B_too_late_if_bakery_food_channel_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1996_1997_1999_2002_CA", "same_entry_group_id": "R5L92_C18_005610_2024-06-14_65500", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L92_C18_NONGSHIM_2024_RAMEN_EXPORT_CHANNEL_REORDER_POSITIVE", "trigger_id": "R5L92_C18_NONGSHIM_2024_STAGE2_ACTIONABLE_RAMEN_EXPORT_CHANNEL_REORDER", "symbol": "004370", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 55, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 55, "margin_bridge_score": 55, "revision_score": 50, "relative_strength_score": 70, "customer_quality_score": 45, "policy_or_regulatory_score": 0, "valuation_repricing_score": 55, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 75, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "food_export_channel_reorder_positive", "MFE_90D_pct": 61.24, "MAE_90D_pct": -2.96, "score_return_alignment_label": "food_export_channel_reorder_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L92_C18_OTTOGI_2024_DOMESTIC_FOOD_CHANNEL_FALSE_STAGE2", "trigger_id": "R5L92_C18_OTTOGI_2024_STAGE2_FALSE_POSITIVE_DOMESTIC_FOOD_CHANNEL_CATCHUP", "symbol": "007310", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 55, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 0, "valuation_repricing_score": 25, "execution_risk_score": 80, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "domestic_food_channel_false_stage2", "MFE_90D_pct": 5.66, "MAE_90D_pct": -20.39, "score_return_alignment_label": "domestic_food_channel_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_domestic_food_channel_catchup_counts_without_export_reorder_margin_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L92_C18_SPCSAMLIP_2024_BAKERY_CHANNEL_EVENT_CAP_4B", "trigger_id": "R5L92_C18_SPCSAMLIP_2024_STAGE4B_BAKERY_CHANNEL_EVENT_CAP", "symbol": "005610", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 55, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 0, "valuation_repricing_score": 25, "execution_risk_score": 80, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "bakery_food_channel_event_cap_4B_guard", "MFE_90D_pct": 1.83, "MAE_90D_pct": -25.42, "score_return_alignment_label": "bakery_food_channel_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_bakery_food_channel_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": "92", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "RAMEN_FOOD_EXPORT_CHANNEL_REORDER_BRIDGE_VS_DOMESTIC_FOOD_CHANNEL_FALSE_STAGE2_AND_BAKERY_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["food_export_channel_reorder_positive", "domestic_food_channel_false_stage2", "bakery_food_channel_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
10. Add tests that bridge-missing C18 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R5
completed_loop = 92
next_round = R6
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.

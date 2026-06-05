# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R5
scheduled_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = KFOOD_EXPORT_REORDER_CHANNEL_MARGIN_BRIDGE_VS_SNACK_RETAIL_FALSE_STAGE2_AND_SEAFOOD_KFOOD_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | low_MFE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R5_loop_94_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
```

This file is the corrected final output for this execution. The scheduler state after R4 loop 94 is R5 / loop 94. R5 is the L5 consumer/brand/distribution round, and this run fills C18 consumer export channel reorder rather than repeating the immediately preceding R5 loop 93 C19 inventory-margin file.

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
low_MFE_guardrail = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R5
scheduled_loop = 94
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
round_sector_consistency = pass
computed_next_round = R6
computed_next_loop = 94
```

C18 is a channel-compounding archetype. A K-food headline is just a billboard; the motor is reorder durability, overseas channel throughput, distributor sell-through, ASP/mix, operating leverage and margin revision.

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
previous R5 loop-92 C18 symbols avoided: 004370, 007310, 005610
previous R5 loop-93 C19 symbols avoided: 241590, 020000, 298540
previous R4 loop-94 C17 symbols avoided: 002380, 011170, 004090
```

Selected rows avoid hard duplicates and top repeated C18 symbols:

```text
003230 / Stage2-Actionable / 2024-02-02
101530 / Stage2-Actionable / 2024-02-01
011150 / Stage4B / 2024-01-25
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
| 003230 | atlas/symbol_profiles/003/003230.json | selected 2024 window clean after old 2003 CA candidate |
| 101530 | atlas/symbol_profiles/101/101530.json | selected 2024 window clean after old 2016 CA candidate |
| 011150 | atlas/symbol_profiles/011/011150.json | selected 2024 window clean after old 2004/2010 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R5L94_C18_SAMYANGFOODS_2024_KFOOD_EXPORT_REORDER_CHANNEL_MARGIN_POSITIVE | 003230 | 2024-02-02 | yes | 180 | yes | yes | true |
| R5L94_C18_HAITAI_2024_SNACK_RETAIL_EXPORT_THEME_FALSE_STAGE2 | 101530 | 2024-02-01 | yes | 180 | yes | yes | true |
| R5L94_C18_CJSEAFOOD_2024_SEAFOOD_KFOOD_EXPORT_EVENT_CAP_4B | 011150 | 2024-01-25 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | KFOOD_EXPORT_REORDER_CHANNEL_MARGIN_BRIDGE | Positive Stage2 requires overseas reorder, distributor/channel throughput, ASP/mix, operating leverage, margin and revision bridge. |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | SNACK_RETAIL_FALSE_STAGE2 | Snack/retail export sympathy without channel-reorder and margin bridge can become false Stage2. |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | SEAFOOD_KFOOD_EVENT_CAP_4B | Seafood/K-food export event premium should route to 4B when shipment/reorder/margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R5L94_C18_SAMYANGFOODS_2024_KFOOD_EXPORT_REORDER_CHANNEL_MARGIN_POSITIVE | 003230 | 삼양식품 | positive | Export reorder/channel-margin bridge produced extreme MFE after shallow early MAE. |
| R5L94_C18_HAITAI_2024_SNACK_RETAIL_EXPORT_THEME_FALSE_STAGE2 | 101530 | 해태제과식품 | counterexample | Snack-retail export sympathy had low MFE without channel-reorder proof. |
| R5L94_C18_CJSEAFOOD_2024_SEAFOOD_KFOOD_EXPORT_EVENT_CAP_4B | 011150 | CJ씨푸드 | counterexample / 4B | Seafood/K-food event premium capped after the January spike. |

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
| Samyang Foods K-food export reorder bridge | historical public/report proxy | true | true | shadow-only positive |
| Haitai snack-retail export false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| CJ Seafood seafood/K-food event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 003230 | atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv | atlas/symbol_profiles/003/003230.json |
| 101530 | atlas/ohlcv_tradable_by_symbol_year/101/101530/2024.csv | atlas/symbol_profiles/101/101530.json |
| 011150 | atlas/ohlcv_tradable_by_symbol_year/011/011150/2024.csv | atlas/symbol_profiles/011/011150.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R5L94_C18_SAMYANGFOODS_2024_STAGE2_ACTIONABLE_KFOOD_EXPORT_REORDER_CHANNEL_MARGIN | 003230 | Stage2-Actionable | 2024-02-02 | 180900 | positive | export reorder/channel-margin bridge worked |
| R5L94_C18_HAITAI_2024_STAGE2_FALSE_POSITIVE_SNACK_RETAIL_EXPORT_THEME | 101530 | Stage2-Actionable | 2024-02-01 | 5450 | counterexample | snack-retail export sympathy false Stage2 |
| R5L94_C18_CJSEAFOOD_2024_STAGE4B_SEAFOOD_KFOOD_EXPORT_EVENT_CAP | 011150 | Stage4B | 2024-01-25 | 2905 | counterexample/4B | seafood K-food event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R5L94_C18_SAMYANGFOODS_2024_STAGE2_ACTIONABLE_KFOOD_EXPORT_REORDER_CHANNEL_MARGIN | 180900 | 12.22 | -6.25 | 296.90 | -6.25 | 296.90 | -6.25 | 2024-06-19 | 718000 | -18.94 |
| R5L94_C18_HAITAI_2024_STAGE2_FALSE_POSITIVE_SNACK_RETAIL_EXPORT_THEME | 5450 | 2.39 | -4.95 | 2.94 | -6.06 | 2.94 | -9.17 | 2024-03-13 | 5610 | -11.05 |
| R5L94_C18_CJSEAFOOD_2024_STAGE4B_SEAFOOD_KFOOD_EXPORT_EVENT_CAP | 2905 | 8.61 | -7.40 | 8.61 | -10.50 | 8.61 | -15.15 | 2024-01-25 | 3155 | -18.23 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C18 Stage2 needs reorder/channel throughput/ASP/margin/revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing K-food export event premiums should route to 4B watch |
| low_MFE_guardrail | strengthen: low forward MFE blocks positive promotion when reorder bridge is missing |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is export-channel reorder bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 003230 | good_stage2_with_later_watch | Reorder/channel-margin bridge produced extreme MFE, but later valuation watch remains necessary. |
| 101530 | bad_stage2 | Snack-retail export sympathy lacked channel-reorder and margin bridge; forward MFE stayed low. |
| 011150 | good_4B | Seafood/K-food export premium capped after January event spike. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 101530 snack-retail false Stage2 | 0.97 | 0.97 | false Stage2 due missing reorder/channel/margin bridge |
| 011150 seafood K-food cap | 0.92 | 0.92 | acceptable 4B timing after January event premium |
| 003230 export reorder bridge | n/a | n/a | positive Stage2, but later K-food export valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 101530 / 011150
```

No hard 4C candidate is proposed. R5 loop 94 is about Stage2 bridge quality and first explicit C18 4B coverage.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L5 consumer export channel reorder cases, Stage2 requires verified export reorder durability, distributor/channel throughput, sell-through, ASP/mix, margin, or revision bridge. K-food, snack, seafood, export, reorder, retail or consumer sympathy label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
rule = C18 should split true export-reorder/channel-margin positives from K-food sympathy false Stage2 and event-cap rows. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 102.82 | -7.60 | 0.67 | mixed; C18 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 102.82 | -7.60 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L5 reorder/channel/margin bridge required | 2 | 149.92 | -6.16 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C18 bridge vs event-cap split | 2 | 149.92 | -6.16 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing K-food/export sympathy rows as positive | 1 | 296.90 | -6.25 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 003230 export reorder bridge | 66 | Stage2-Watch | 80 | Stage2-Actionable | 296.90 | -6.25 | K_food_export_reorder_channel_positive |
| 101530 snack-retail false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 2.94 | -6.06 | snack_retail_export_theme_false_stage2 |
| 011150 seafood K-food cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 8.61 | -10.50 | seafood_Kfood_export_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KFOOD_EXPORT_REORDER_CHANNEL_MARGIN_BRIDGE_VS_SNACK_RETAIL_FALSE_STAGE2_AND_SEAFOOD_KFOOD_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C18 Samyang Foods export-reorder positive, Haitai snack-retail export-theme false Stage2, and CJ Seafood K-food event-cap 4B split while avoiding top repeated C18 symbols and previous R5 symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, low_MFE_guardrail, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: K_food_export_reorder_channel_positive, snack_retail_export_theme_false_stage2, seafood_Kfood_export_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, low_MFE_guardrail
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
shadow_weight,stage2_required_bridge,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,configured,C18_requires_export_reorder_channel_throughput_ASP_margin_revision_bridge,0,"C18 Stage2 should require export reorder durability, overseas distributor/channel throughput, sell-through, ASP/mix, margin, or revision bridge, not K-food/export sympathy label alone","Samyang Foods positive worked; Haitai and CJ Seafood event/theme rows failed positive-stage promotion","R5L94_C18_SAMYANGFOODS_2024_STAGE2_ACTIONABLE_KFOOD_EXPORT_REORDER_CHANNEL_MARGIN|R5L94_C18_HAITAI_2024_STAGE2_FALSE_POSITIVE_SNACK_RETAIL_EXPORT_THEME|R5L94_C18_CJSEAFOOD_2024_STAGE4B_SEAFOOD_KFOOD_EXPORT_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,configured,cap_bridge_missing_Kfood_export_event_premiums_as_4B_watch,0,"K-food/export sympathy premiums can peak before shipment, distributor reorder and margin bridge is proven","Haitai had low forward MFE; CJ Seafood showed event-cap behavior after January spike","R5L94_C18_HAITAI_2024_STAGE2_FALSE_POSITIVE_SNACK_RETAIL_EXPORT_THEME|R5L94_C18_CJSEAFOOD_2024_STAGE4B_SEAFOOD_KFOOD_EXPORT_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,low_MFE_guardrail,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,configured,block_positive_stage_when_export_theme_has_low_forward_MFE_without_reorder_margin_bridge,0,"Low forward MFE after bridge-missing K-food/export entries should block Stage2/Stage3 promotion unless channel reorder and margin evidence survives","Haitai MFE90=2.94 and CJ Seafood MFE90=8.61","R5L94_C18_HAITAI_2024_STAGE2_FALSE_POSITIVE_SNACK_RETAIL_EXPORT_THEME|R5L94_C18_CJSEAFOOD_2024_STAGE4B_SEAFOOD_KFOOD_EXPORT_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R5L94_C18_SAMYANGFOODS_2024_KFOOD_EXPORT_REORDER_CHANNEL_MARGIN_POSITIVE", "symbol": "003230", "company_name": "삼양식품", "round": "R5", "loop": "94", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KFOOD_EXPORT_REORDER_CHANNEL_MARGIN_BRIDGE_VS_SNACK_RETAIL_FALSE_STAGE2_AND_SEAFOOD_KFOOD_EVENT_CAP", "case_type": "structural_success_with_later_export_channel_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R5L94_C18_SAMYANGFOODS_2024_STAGE2_ACTIONABLE_KFOOD_EXPORT_REORDER_CHANNEL_MARGIN", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "K-food export reorder / overseas channel expansion / product-mix margin bridge produced extreme 90D/180D MFE after a controlled early drawdown. C18 works when export-channel narrative maps into reorder durability, overseas distributor/channel throughput, ASP/mix, operating leverage, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C18_positive_requires_export_reorder_channel_throughput_ASP_margin_revision_bridge_not_K_food_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2003 corporate-action candidate. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R5L94_C18_HAITAI_2024_SNACK_RETAIL_EXPORT_THEME_FALSE_STAGE2", "symbol": "101530", "company_name": "해태제과식품", "round": "R5", "loop": "94", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KFOOD_EXPORT_REORDER_CHANNEL_MARGIN_BRIDGE_VS_SNACK_RETAIL_FALSE_STAGE2_AND_SEAFOOD_KFOOD_EVENT_CAP", "case_type": "failed_rerating_reorder_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R5L94_C18_HAITAI_2024_STAGE2_FALSE_POSITIVE_SNACK_RETAIL_EXPORT_THEME", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Snack/retail export sympathy watch had low forward MFE and no visible channel-reorder compounding. C18 Stage2 should not be awarded without shipment/reorder durability, distributor sell-through, overseas channel expansion, ASP/mix, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_snack_retail_export_theme_counts_without_reorder_channel_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2016 corporate-action candidate. Source-proxy only."}
{"row_type": "case", "case_id": "R5L94_C18_CJSEAFOOD_2024_SEAFOOD_KFOOD_EXPORT_EVENT_CAP_4B", "symbol": "011150", "company_name": "CJ씨푸드", "round": "R5", "loop": "94", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KFOOD_EXPORT_REORDER_CHANNEL_MARGIN_BRIDGE_VS_SNACK_RETAIL_FALSE_STAGE2_AND_SEAFOOD_KFOOD_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R5L94_C18_CJSEAFOOD_2024_STAGE4B_SEAFOOD_KFOOD_EXPORT_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Seafood/K-food export event premium capped after the January spike and failed to develop into a durable channel-reorder trend. C18 should route bridge-missing food export event premiums to 4B unless shipment volume, distributor reorder, ASP/mix, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_seafood_Kfood_export_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2004/2010 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R5L94_C18_SAMYANGFOODS_2024_STAGE2_ACTIONABLE_KFOOD_EXPORT_REORDER_CHANNEL_MARGIN", "case_id": "R5L94_C18_SAMYANGFOODS_2024_KFOOD_EXPORT_REORDER_CHANNEL_MARGIN_POSITIVE", "symbol": "003230", "company_name": "삼양식품", "round": "R5", "loop": "94", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KFOOD_EXPORT_REORDER_CHANNEL_MARGIN_BRIDGE_VS_SNACK_RETAIL_FALSE_STAGE2_AND_SEAFOOD_KFOOD_EVENT_CAP", "sector": "K_food_export_reorder_overseas_channel_margin", "primary_archetype": "export_reorder_channel_throughput_ASP_mix_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | low_MFE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-02", "entry_date": "2024-02-02", "entry_price": 180900.0, "evidence_available_at_that_date": "K-food export reorder, overseas channel expansion, distributor sell-through, ASP/mix, operating leverage and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["export_reorder_proxy", "overseas_channel_throughput_proxy", "distributor_sellthrough_proxy", "ASP_mix_bridge_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["positive_MFE30", "very_high_MFE90", "very_high_MFE180", "controlled_initial_MAE"], "stage4b_evidence_fields": ["later_K_food_valuation_watch", "post_peak_channel_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv", "profile_path": "atlas/symbol_profiles/003/003230.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 12.22, "MFE_90D_pct": 296.9, "MFE_180D_pct": 296.9, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -6.25, "MAE_90D_pct": -6.25, "MAE_180D_pct": -6.25, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-19", "peak_price": 718000.0, "drawdown_after_peak_pct": -18.94, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_K_food_export_valuation_4B_watch_needed", "four_b_evidence_type": ["export_channel_reorder_bridge", "margin_revision", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_K_food_export_reorder_channel_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2003_CA", "same_entry_group_id": "R5L94_C18_003230_2024-02-02_180900", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R5L94_C18_HAITAI_2024_STAGE2_FALSE_POSITIVE_SNACK_RETAIL_EXPORT_THEME", "case_id": "R5L94_C18_HAITAI_2024_SNACK_RETAIL_EXPORT_THEME_FALSE_STAGE2", "symbol": "101530", "company_name": "해태제과식품", "round": "R5", "loop": "94", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KFOOD_EXPORT_REORDER_CHANNEL_MARGIN_BRIDGE_VS_SNACK_RETAIL_FALSE_STAGE2_AND_SEAFOOD_KFOOD_EVENT_CAP", "sector": "snack_retail_export_theme_reorder_watch", "primary_archetype": "snack_retail_export_watch_without_channel_reorder_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | low_MFE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 5450.0, "evidence_available_at_that_date": "snack/retail K-food export sympathy watch without confirmed channel reorder, distributor sell-through or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["snack_retail_export_theme", "K_food_sympathy_watch", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_MFE90", "channel_reorder_margin_bridge_missing", "post_watch_stagnation"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/101/101530/2024.csv", "profile_path": "atlas/symbol_profiles/101/101530.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.39, "MFE_90D_pct": 2.94, "MFE_180D_pct": 2.94, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -4.95, "MAE_90D_pct": -6.06, "MAE_180D_pct": -9.17, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-13", "peak_price": 5610.0, "drawdown_after_peak_pct": -11.05, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.97, "four_b_full_window_peak_proximity": 0.97, "four_b_timing_verdict": "snack_retail_export_theme_was_false_stage2_due_missing_channel_reorder_margin_bridge", "four_b_evidence_type": ["K_food_sympathy_premium", "bridge_missing", "low_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_snack_retail_export_theme_without_channel_reorder_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_snack_retail_export_theme_counts_without_reorder_channel_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2016_CA", "same_entry_group_id": "R5L94_C18_101530_2024-02-01_5450", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R5L94_C18_CJSEAFOOD_2024_STAGE4B_SEAFOOD_KFOOD_EXPORT_EVENT_CAP", "case_id": "R5L94_C18_CJSEAFOOD_2024_SEAFOOD_KFOOD_EXPORT_EVENT_CAP_4B", "symbol": "011150", "company_name": "CJ씨푸드", "round": "R5", "loop": "94", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KFOOD_EXPORT_REORDER_CHANNEL_MARGIN_BRIDGE_VS_SNACK_RETAIL_FALSE_STAGE2_AND_SEAFOOD_KFOOD_EVENT_CAP", "sector": "seafood_K_food_export_event_premium", "primary_archetype": "seafood_K_food_export_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | low_MFE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-01-25", "entry_date": "2024-01-25", "entry_price": 2905.0, "evidence_available_at_that_date": "seafood/K-food export event premium and processed-food export sympathy after January spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["seafood_K_food_export_event", "processed_food_export_sympathy", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "low_sustainable_MFE", "shipment_reorder_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011150/2024.csv", "profile_path": "atlas/symbol_profiles/011/011150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.61, "MFE_90D_pct": 8.61, "MFE_180D_pct": 8.61, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -7.4, "MAE_90D_pct": -10.5, "MAE_180D_pct": -15.15, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-25", "peak_price": 3155.0, "drawdown_after_peak_pct": -18.23, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.92, "four_b_timing_verdict": "acceptable_full_window_4B_timing_seafood_Kfood_export_event_cap", "four_b_evidence_type": ["K_food_export_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_seafood_Kfood_export_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_seafood_Kfood_export_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2004_2010_CA", "same_entry_group_id": "R5L94_C18_011150_2024-01-25_2905", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L94_C18_SAMYANGFOODS_2024_KFOOD_EXPORT_REORDER_CHANNEL_MARGIN_POSITIVE", "trigger_id": "R5L94_C18_SAMYANGFOODS_2024_STAGE2_ACTIONABLE_KFOOD_EXPORT_REORDER_CHANNEL_MARGIN", "symbol": "003230", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 25, "backlog_visibility_score": 70, "margin_bridge_score": 65, "revision_score": 65, "relative_strength_score": 80, "customer_quality_score": 60, "policy_or_regulatory_score": 0, "valuation_repricing_score": 50, "execution_risk_score": 35, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "K_food_export_reorder_channel_positive", "MFE_90D_pct": 296.9, "MAE_90D_pct": -6.25, "score_return_alignment_label": "K_food_export_reorder_channel_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L94_C18_HAITAI_2024_SNACK_RETAIL_EXPORT_THEME_FALSE_STAGE2", "trigger_id": "R5L94_C18_HAITAI_2024_STAGE2_FALSE_POSITIVE_SNACK_RETAIL_EXPORT_THEME", "symbol": "101530", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 25, "execution_risk_score": 80, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "snack_retail_export_theme_false_stage2", "MFE_90D_pct": 2.94, "MAE_90D_pct": -6.06, "score_return_alignment_label": "snack_retail_export_theme_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_snack_retail_export_theme_counts_without_reorder_channel_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L94_C18_CJSEAFOOD_2024_SEAFOOD_KFOOD_EXPORT_EVENT_CAP_4B", "trigger_id": "R5L94_C18_CJSEAFOOD_2024_STAGE4B_SEAFOOD_KFOOD_EXPORT_EVENT_CAP", "symbol": "011150", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 25, "execution_risk_score": 80, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "seafood_Kfood_export_event_cap_4B_guard", "MFE_90D_pct": 8.61, "MAE_90D_pct": -10.5, "score_return_alignment_label": "seafood_Kfood_export_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_seafood_Kfood_export_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": "94", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KFOOD_EXPORT_REORDER_CHANNEL_MARGIN_BRIDGE_VS_SNACK_RETAIL_FALSE_STAGE2_AND_SEAFOOD_KFOOD_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "low_MFE_guardrail"], "residual_error_types_found": ["K_food_export_reorder_channel_positive", "snack_retail_export_theme_false_stage2", "seafood_Kfood_export_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
- C18 rows need explicit export reorder, overseas channel throughput, sell-through, ASP/mix, margin or revision bridge before positive promotion.
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
completed_loop = 94
next_round = R6
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.

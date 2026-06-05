# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R5
scheduled_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = KFOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_FOOD_THEME_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R5_loop_88_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
```

This loop continues loop 88 after R4. It adds 3 C20 K-food/global distribution cases: one export reorder/margin-bridge positive and two food theme / export premium 4B counterexamples.

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
scheduled_round = R5
scheduled_loop = 88
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
round_sector_consistency = pass
computed_next_round = R6
computed_next_loop = 88
```

R5 permits L5 consumer / brand / distribution research. C20 is relatively thinner than many adjacent consumer buckets in the current index, and the No-Repeat memo specifically warns not to repeat `C20 / 257720 / Stage3-Green / 2024-05-10`. This loop avoids that combination and also avoids the current C20 top-covered symbols.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION = 19 rows / 11 symbols / good-bad Stage2 8-2 / 4B-4C 4-0
top covered symbols include 226320(3), 161890(2), 192820(2), 214420(2), 241710(2), 439090(2)
explicit do-not-repeat memo: C20 / 257720 / Stage3-Green / 2024-05-10
```

Selected rows avoid those repeated combinations:

```text
003230 / Stage2-Actionable / 2024-03-04
005180 / Stage4B / 2024-06-26
011150 / Stage4B / 2024-06-14
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
| 003230 | atlas/symbol_profiles/003/003230.json | selected 2024 window clean; CA candidate is 2003-07-25 |
| 005180 | atlas/symbol_profiles/005/005180.json | selected 2024 window clean; CA candidates are pre-1999 |
| 011150 | atlas/symbol_profiles/011/011150.json | selected 2024 window clean; CA candidate is 2002-04-22 |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R5L88_C20_SAMYANG_2024_KFOOD_EXPORT_REORDER_POSITIVE | 003230 | 2024-03-04 | yes | 180 | yes | yes | true |
| R5L88_C20_BINGGRAE_2024_EXPORT_THEME_EVENT_CAP_4B | 005180 | 2024-06-26 | yes | 180 | yes | yes | true |
| R5L88_C20_CJSEAFOOD_2024_KFOOD_THEME_EVENT_CAP_4B | 011150 | 2024-06-14 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | KFOOD_EXPORT_REORDER_MARGIN_BRIDGE | Positive Stage2 requires export reorder, repeat channel demand, and margin/revision bridge. |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | FOOD_EXPORT_THEME_EVENT_CAP | Food export/brand premium can cap quickly if reorder/margin confirmation is missing. |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | SMALLCAP_KFOOD_THEME_EVENT_CAP | Small-cap K-food theme spikes are 4B/watch unless real distribution bridge appears. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R5L88_C20_SAMYANG_2024_KFOOD_EXPORT_REORDER_POSITIVE | 003230 | 삼양식품 | positive | Export reorder / global distribution bridge produced huge MFE with low early MAE. |
| R5L88_C20_BINGGRAE_2024_EXPORT_THEME_EVENT_CAP_4B | 005180 | 빙그레 | counterexample / 4B | Food export/brand premium capped; forward MFE was tiny and MAE large. |
| R5L88_C20_CJSEAFOOD_2024_KFOOD_THEME_EVENT_CAP_4B | 011150 | CJ씨푸드 | counterexample / 4B | Small-cap K-food theme spike faded sharply without distribution bridge. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 2
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
```

## 9. Evidence Source Map

| case | evidence status | evidence_url_pending | source_proxy_only | usage |
|---|---|---|---|---|
| Samyang Foods export reorder | historical public/report proxy | true | true | shadow-only positive |
| Binggrae food export theme | historical public/report proxy | true | true | 4B overlay counterexample |
| CJ Seafood K-food theme | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 003230 | atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv | atlas/symbol_profiles/003/003230.json |
| 005180 | atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv | atlas/symbol_profiles/005/005180.json |
| 011150 | atlas/ohlcv_tradable_by_symbol_year/011/011150/2024.csv | atlas/symbol_profiles/011/011150.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R5L88_C20_SAMYANG_2024_STAGE2_ACTIONABLE_KFOOD_EXPORT_REORDER | 003230 | Stage2-Actionable | 2024-03-04 | 191000 | positive | K-food export reorder bridge worked |
| R5L88_C20_BINGGRAE_2024_STAGE4B_KFOOD_EXPORT_THEME_CAP | 005180 | Stage4B | 2024-06-26 | 99800 | counterexample/4B | food export premium cap |
| R5L88_C20_CJSEAFOOD_2024_STAGE4B_KFOOD_THEME_EVENT_CAP | 011150 | Stage4B | 2024-06-14 | 6320 | counterexample/4B | small-cap K-food event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R5L88_C20_SAMYANG_2024_STAGE2_ACTIONABLE_KFOOD_EXPORT_REORDER | 191000 | 31.15 | -3.30 | 275.92 | -3.30 | 275.92 | -3.30 | 2024-06-19 | 718000 | -36.56 |
| R5L88_C20_BINGGRAE_2024_STAGE4B_KFOOD_EXPORT_THEME_CAP | 99800 | 1.60 | -22.95 | 1.60 | -40.08 | 1.60 | -40.08 | 2024-06-26 | 101400 | -41.03 |
| R5L88_C20_CJSEAFOOD_2024_STAGE4B_KFOOD_THEME_EVENT_CAP | 6320 | 2.69 | -33.86 | 2.69 | -51.03 | 2.69 | -51.03 | 2024-06-17 | 6490 | -52.31 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C20 Stage2 needs export reorder / channel repeat / margin or revision bridge |
| local_4b_watch_guard | strengthen: food export and K-food theme premium should route to 4B watch |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is Stage2/4B quality:

| symbol | stage quality | explanation |
|---|---|---|
| 003230 | good_stage2 | Export reorder / global distribution bridge produced massive upside. |
| 005180 | good_4B | Food export premium capped before repeat demand and margin bridge were verified. |
| 011150 | good_4B | Small-cap K-food theme spike had almost no forward upside and large drawdown. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 005180 food export theme cap | 1.00 | 1.00 | good_full_window_4B_timing_food_export_theme_event_cap |
| 011150 small-cap K-food theme cap | 0.97 | 0.97 | good_event_cap_4B_watch_smallcap_Kfood_theme |
| 003230 export reorder bridge | n/a | n/a | positive Stage2; later valuation watch only |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 005180 / 011150
```

No hard 4C candidate is proposed. C20 residual here is Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L5 consumer/food distribution cases, Stage2 requires verified export reorder, repeat channel demand, global distribution expansion, and margin/revision bridge. Brand or K-food theme momentum alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
rule = C20 should split K-food export reorder/margin-bridge positives from food export theme caps and small-cap K-food theme spikes. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 93.40 | -31.47 | 0.67 | mixed; C20 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 93.40 | -31.47 | 0.67 | weaker bridge/theme guard |
| P1 sector_specific_candidate_profile | L5 export reorder bridge required | 2 | 138.76 | -21.69 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C20 bridge vs event-cap split | 2 | 138.76 | -21.69 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject food-theme caps as positive | 1 | 275.92 | -3.30 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 003230 export reorder | 66 | Stage2-Watch | 76 | Stage2-Actionable | 275.92 | -3.30 | Kfood_export_reorder_margin_bridge_positive |
| 005180 food export cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 1.60 | -40.08 | food_export_theme_event_cap_4B_guard |
| 011150 K-food cap | 69 | Stage3-Yellow-like | 53 | Stage4B-watch | 2.69 | -51.03 | smallcap_Kfood_theme_event_cap_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "KFOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_FOOD_THEME_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 2, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 1, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C20 K-food export reorder positive vs food export/theme event-cap 4B split using non-top-covered symbols."}
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
residual_error_types_found: Kfood_export_reorder_margin_bridge_positive, food_export_theme_event_cap_4B, smallcap_Kfood_theme_false_distribution_rerating
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
- C20 K-food export reorder bridge vs food-theme event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,configured,Kfood_requires_export_reorder_margin_bridge,0,"C20 Stage2 should require verified export reorder, global channel expansion, repeat demand, and margin/revision bridge, not K-food theme momentum alone","Samyang Foods positive worked; Binggrae and CJ Seafood event/theme caps failed positive-stage promotion","R5L88_C20_SAMYANG_2024_STAGE2_ACTIONABLE_KFOOD_EXPORT_REORDER|R5L88_C20_BINGGRAE_2024_STAGE4B_KFOOD_EXPORT_THEME_CAP|R5L88_C20_CJSEAFOOD_2024_STAGE4B_KFOOD_THEME_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,configured,cap_food_theme_premium_as_4B_watch,0,"Food export/K-food theme premiums can peak before reorder and margin confirmation, then draw down heavily","Binggrae and CJ Seafood showed low MFE90 and high MAE90 after theme spikes","R5L88_C20_BINGGRAE_2024_STAGE4B_KFOOD_EXPORT_THEME_CAP|R5L88_C20_CJSEAFOOD_2024_STAGE4B_KFOOD_THEME_EVENT_CAP",2,2,2,low,guardrail_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R5L88_C20_SAMYANG_2024_KFOOD_EXPORT_REORDER_POSITIVE", "symbol": "003230", "company_name": "삼양식품", "round": "R5", "loop": "88", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "KFOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_FOOD_THEME_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R5L88_C20_SAMYANG_2024_STAGE2_ACTIONABLE_KFOOD_EXPORT_REORDER", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "K-food export reorder / global distribution bridge produced extremely strong 90D/180D MFE with shallow early MAE.", "current_profile_verdict": "current_profile_kept_but_C20_positive_requires_export_reorder_margin_bridge_not_food_theme_only", "price_source": "Songdaiki/stock-web", "notes": "Source-proxy only; exact as-of export/reorder evidence URL remains pending, so no production weight delta."}
{"row_type": "case", "case_id": "R5L88_C20_BINGGRAE_2024_EXPORT_THEME_EVENT_CAP_4B", "symbol": "005180", "company_name": "빙그레", "round": "R5", "loop": "88", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "KFOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_FOOD_THEME_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R5L88_C20_BINGGRAE_2024_STAGE4B_KFOOD_EXPORT_THEME_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Food export/brand premium capped quickly after a sharp run; low forward MFE and large MAE argue for 4B watch rather than structural Green.", "current_profile_verdict": "current_profile_4B_too_late_if_export_theme_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "New C20 symbol; source-proxy only."}
{"row_type": "case", "case_id": "R5L88_C20_CJSEAFOOD_2024_KFOOD_THEME_EVENT_CAP_4B", "symbol": "011150", "company_name": "CJ씨푸드", "round": "R5", "loop": "88", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "KFOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_FOOD_THEME_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R5L88_C20_CJSEAFOOD_2024_STAGE4B_KFOOD_THEME_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "K-food/seafood theme premium had almost no forward upside and deep drawdown; theme momentum without reorder/margin bridge should be capped as 4B.", "current_profile_verdict": "current_profile_false_positive_if_Kfood_theme_spike_counts_as_distribution_rerating", "price_source": "Songdaiki/stock-web", "notes": "Small-cap food theme event cap; source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R5L88_C20_SAMYANG_2024_STAGE2_ACTIONABLE_KFOOD_EXPORT_REORDER", "case_id": "R5L88_C20_SAMYANG_2024_KFOOD_EXPORT_REORDER_POSITIVE", "symbol": "003230", "company_name": "삼양식품", "round": "R5", "loop": "88", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "KFOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_FOOD_THEME_EVENT_CAP", "sector": "Kfood_global_distribution", "primary_archetype": "Kfood_export_reorder_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-04", "entry_date": "2024-03-04", "entry_price": 191000.0, "evidence_available_at_that_date": "K-food export reorder / global channel expansion and margin bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["export_reorder_proxy", "global_channel_expansion", "margin_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["very_high_MFE90", "low_MAE_to_reorder_rerating_path"], "stage4b_evidence_fields": ["valuation_repricing_watch_after_180D_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv", "profile_path": "atlas/symbol_profiles/003/003230.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 31.15, "MFE_90D_pct": 275.92, "MFE_180D_pct": 275.92, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -3.3, "MAE_90D_pct": -3.3, "MAE_180D_pct": -3.3, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-19", "peak_price": 718000.0, "drawdown_after_peak_pct": -36.56, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_valuation_watch_needed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_Kfood_export_reorder_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L88_C20_003230_2024-03-04_191000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R5L88_C20_BINGGRAE_2024_STAGE4B_KFOOD_EXPORT_THEME_CAP", "case_id": "R5L88_C20_BINGGRAE_2024_EXPORT_THEME_EVENT_CAP_4B", "symbol": "005180", "company_name": "빙그레", "round": "R5", "loop": "88", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "KFOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_FOOD_THEME_EVENT_CAP", "sector": "Kfood_brand_export_theme", "primary_archetype": "icecream_food_export_theme_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-06-26", "entry_date": "2024-06-26", "entry_price": 99800.0, "evidence_available_at_that_date": "food export/brand premium spike proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["food_export_theme", "brand_premium", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv", "profile_path": "atlas/symbol_profiles/005/005180.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.6, "MFE_90D_pct": 1.6, "MFE_180D_pct": 1.6, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -22.95, "MAE_90D_pct": -40.08, "MAE_180D_pct": -40.08, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 101400.0, "drawdown_after_peak_pct": -41.03, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_food_export_theme_event_cap", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_export_theme_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L88_C20_005180_2024-06-26_99800", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R5L88_C20_CJSEAFOOD_2024_STAGE4B_KFOOD_THEME_EVENT_CAP", "case_id": "R5L88_C20_CJSEAFOOD_2024_KFOOD_THEME_EVENT_CAP_4B", "symbol": "011150", "company_name": "CJ씨푸드", "round": "R5", "loop": "88", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "KFOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_FOOD_THEME_EVENT_CAP", "sector": "Kfood_smallcap_theme", "primary_archetype": "Kfood_seafood_theme_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-06-14", "entry_date": "2024-06-14", "entry_price": 6320.0, "evidence_available_at_that_date": "K-food/seafood theme premium spike proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["Kfood_theme", "smallcap_food_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011150/2024.csv", "profile_path": "atlas/symbol_profiles/011/011150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.69, "MFE_90D_pct": 2.69, "MFE_180D_pct": 2.69, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -33.86, "MAE_90D_pct": -51.03, "MAE_180D_pct": -51.03, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-17", "peak_price": 6490.0, "drawdown_after_peak_pct": -52.31, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.97, "four_b_full_window_peak_proximity": 0.97, "four_b_timing_verdict": "good_event_cap_4B_watch_smallcap_Kfood_theme", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_false_positive_if_Kfood_theme_spike_counts_as_distribution_rerating", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L88_C20_011150_2024-06-14_6320", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L88_C20_SAMYANG_2024_KFOOD_EXPORT_REORDER_POSITIVE", "trigger_id": "R5L88_C20_SAMYANG_2024_STAGE2_ACTIONABLE_KFOOD_EXPORT_REORDER", "symbol": "003230", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 75, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 55, "execution_risk_score": 40, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 55, "margin_bridge_score": 65, "revision_score": 60, "relative_strength_score": 75, "customer_quality_score": 55, "policy_or_regulatory_score": 0, "valuation_repricing_score": 50, "execution_risk_score": 25, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "Kfood_export_reorder_margin_bridge_positive", "MFE_90D_pct": 275.92, "MAE_90D_pct": -3.3, "score_return_alignment_label": "Kfood_export_reorder_margin_bridge_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L88_C20_BINGGRAE_2024_EXPORT_THEME_EVENT_CAP_4B", "trigger_id": "R5L88_C20_BINGGRAE_2024_STAGE4B_KFOOD_EXPORT_THEME_CAP", "symbol": "005180", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 75, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 55, "execution_risk_score": 40, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "food_export_theme_event_cap_4B_guard", "MFE_90D_pct": 1.6, "MAE_90D_pct": -40.08, "score_return_alignment_label": "food_export_theme_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_export_theme_premium_not_capped"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L88_C20_CJSEAFOOD_2024_KFOOD_THEME_EVENT_CAP_4B", "trigger_id": "R5L88_C20_CJSEAFOOD_2024_STAGE4B_KFOOD_THEME_EVENT_CAP", "symbol": "011150", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 75, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 55, "execution_risk_score": 40, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 69, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "smallcap_Kfood_theme_event_cap_guard", "MFE_90D_pct": 2.69, "MAE_90D_pct": -51.03, "score_return_alignment_label": "smallcap_Kfood_theme_event_cap_guard", "current_profile_verdict": "current_profile_false_positive_if_Kfood_theme_spike_counts_as_distribution_rerating"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": "88", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "KFOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_FOOD_THEME_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 2, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["Kfood_export_reorder_margin_bridge_positive", "food_export_theme_event_cap_4B", "smallcap_Kfood_theme_false_distribution_rerating"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R5
completed_loop = 88
next_round = R6
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.

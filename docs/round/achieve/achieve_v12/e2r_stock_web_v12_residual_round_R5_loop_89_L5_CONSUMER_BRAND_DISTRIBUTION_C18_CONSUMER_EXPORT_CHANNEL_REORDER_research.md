# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R5
scheduled_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = KBEAUTY_EXPORT_REORDER_MARGIN_BRIDGE_VS_BRAND_THEME_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R5_loop_89_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
```

This loop continues loop 89 after R4. It adds 3 C18 consumer export/channel reorder cases: one K-beauty export reorder positive, one beauty export theme false Stage2, and one K-beauty theme 4B event-cap counterexample.

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
scheduled_loop = 89
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
round_sector_consistency = pass
computed_next_round = R6
computed_next_loop = 89
```

R5 permits L5 consumer / brand / distribution research. Previous R5 loop-88 used C20, so this loop moves to C18 and tests whether consumer export narratives are backed by reorder, channel repeat demand, margin, and revision visibility.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C18_CONSUMER_EXPORT_CHANNEL_REORDER = 38 rows / 19 symbols / good-bad Stage2 17-9 / 4B-4C 0-0
top covered symbols include 001680(4), 280360(4), UNKNOWN_SYMBOL(4), 049770(3), 271560(3), 003960(2)
previous R5 loop-88 C20 symbols avoided: 003230, 005180, 011150
```

Selected rows avoid those repeated combinations:

```text
018290 / Stage2-Actionable / 2024-03-25
078520 / Stage2-Actionable / 2024-06-26
123690 / Stage4B / 2024-07-01
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
| 018290 | atlas/symbol_profiles/018/018290.json | selected 2024 window clean; CA candidates are 2019 or earlier |
| 078520 | atlas/symbol_profiles/078/078520.json | selected 2024 window clean; CA candidates are 2018 or earlier |
| 123690 | atlas/symbol_profiles/123/123690.json | no corporate-action candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R5L89_C18_VT_2024_KBEAUTY_EXPORT_REORDER_POSITIVE | 018290 | 2024-03-25 | yes | 180 | yes | yes | true |
| R5L89_C18_ABLECNC_2024_BEAUTY_EXPORT_THEME_FALSE_STAGE2 | 078520 | 2024-06-26 | yes | 180 | yes | yes | true |
| R5L89_C18_HANKOOKCOS_2024_KBEAUTY_THEME_EVENT_CAP_4B | 123690 | 2024-07-01 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | KBEAUTY_EXPORT_REORDER_MARGIN_BRIDGE | Positive Stage2 requires export reorder, repeat channel demand, margin/revision bridge. |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | BEAUTY_EXPORT_THEME_FALSE_STAGE2 | Export/brand theme without reorder bridge can become low-MFE high-MAE false Stage2. |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | KBEAUTY_THEME_EVENT_CAP_4B | K-beauty theme premium should route to 4B if reorder/margin confirmation is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R5L89_C18_VT_2024_KBEAUTY_EXPORT_REORDER_POSITIVE | 018290 | 브이티 | positive | Export/channel reorder bridge produced high MFE with low entry MAE. |
| R5L89_C18_ABLECNC_2024_BEAUTY_EXPORT_THEME_FALSE_STAGE2 | 078520 | 에이블씨엔씨 | counterexample | Beauty export theme premium had tiny forward MFE and deep drawdown. |
| R5L89_C18_HANKOOKCOS_2024_KBEAUTY_THEME_EVENT_CAP_4B | 123690 | 한국화장품 | counterexample / 4B | K-beauty theme spike capped quickly and then drew down. |

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
| VT export/reorder bridge | historical public/report proxy | true | true | shadow-only positive |
| Able C&C beauty export theme | historical public/report proxy | true | true | false-Stage2 guardrail |
| Hankook Cosmetics K-beauty cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 018290 | atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv | atlas/symbol_profiles/018/018290.json |
| 078520 | atlas/ohlcv_tradable_by_symbol_year/078/078520/2024.csv | atlas/symbol_profiles/078/078520.json |
| 123690 | atlas/ohlcv_tradable_by_symbol_year/123/123690/2024.csv | atlas/symbol_profiles/123/123690.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R5L89_C18_VT_2024_STAGE2_ACTIONABLE_KBEAUTY_EXPORT_REORDER | 018290 | Stage2-Actionable | 2024-03-25 | 16750 | positive | K-beauty export reorder bridge worked |
| R5L89_C18_ABLECNC_2024_STAGE2_FALSE_POSITIVE_BEAUTY_EXPORT_THEME | 078520 | Stage2-Actionable | 2024-06-26 | 9630 | counterexample | beauty export theme false Stage2 |
| R5L89_C18_HANKOOKCOS_2024_STAGE4B_KBEAUTY_THEME_CAP | 123690 | Stage4B | 2024-07-01 | 8930 | counterexample/4B | K-beauty theme event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R5L89_C18_VT_2024_STAGE2_ACTIONABLE_KBEAUTY_EXPORT_REORDER | 16750 | 54.63 | -3.94 | 138.81 | -3.94 | 138.81 | -3.94 | 2024-06-19 | 40000 | -35.00 |
| R5L89_C18_ABLECNC_2024_STAGE2_FALSE_POSITIVE_BEAUTY_EXPORT_THEME | 9630 | 4.78 | -32.50 | 4.78 | -32.50 | 4.78 | -32.50 | 2024-06-27 | 10090 | -35.58 |
| R5L89_C18_HANKOOKCOS_2024_STAGE4B_KBEAUTY_THEME_CAP | 8930 | 15.34 | -29.56 | 15.34 | -29.56 | 15.34 | -29.56 | 2024-07-01 | 10300 | -38.93 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C18 Stage2 needs export reorder / channel repeat / margin or revision bridge |
| local_4b_watch_guard | strengthen: beauty/K-consumer theme premium should route to 4B watch |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is Stage2/4B quality:

| symbol | stage quality | explanation |
|---|---|---|
| 018290 | good_stage2 | Export reorder / channel margin bridge produced strong upside. |
| 078520 | bad_stage2 | Beauty export theme label had little upside and high MAE. |
| 123690 | good_4B | K-beauty theme premium capped at the spike. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 078520 beauty export false Stage2 | 0.95 | 0.95 | beauty_export_theme_spike_was_false_stage2_event_cap |
| 123690 K-beauty cap | 1.00 | 1.00 | good_full_window_4B_timing_Kbeauty_theme_event_cap |
| 018290 export reorder bridge | n/a | n/a | positive Stage2, but later export valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 078520 / 123690
```

No hard 4C candidate is proposed. R5 loop 89 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L5 consumer export/channel cases, Stage2 requires verified export reorder, repeat channel demand, sell-through, distribution expansion, margin, or revision bridge. Beauty/K-consumer brand theme momentum alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
rule = C18 should split consumer export/reorder positives from beauty export theme false Stage2 and K-beauty event-cap rows. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 52.98 | -22.00 | 0.67 | mixed; C18 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 52.98 | -22.00 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L5 export reorder bridge required | 2 | 71.80 | -18.22 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C18 bridge vs event-cap split | 2 | 71.80 | -18.22 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing beauty themes as positive | 1 | 138.81 | -3.94 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 018290 export/reorder bridge | 66 | Stage2-Watch | 75 | Stage2-Actionable | 138.81 | -3.94 | Kbeauty_export_reorder_margin_positive |
| 078520 beauty export false | 66 | Stage2-Actionable | 53 | Stage1/Watch | 4.78 | -32.50 | beauty_export_theme_false_stage2 |
| 123690 K-beauty cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 15.34 | -29.56 | Kbeauty_theme_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KBEAUTY_EXPORT_REORDER_MARGIN_BRIDGE_VS_BRAND_THEME_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C18 K-beauty export/reorder positive, beauty export false Stage2, and K-beauty theme event-cap 4B split using non-top-covered symbols."}
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
residual_error_types_found: Kbeauty_export_reorder_margin_positive, beauty_export_theme_false_stage2, Kbeauty_theme_event_cap_4B
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
- C18 consumer export/channel reorder bridge vs beauty theme event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,configured,C18_requires_export_reorder_channel_margin_revision_bridge,0,"C18 Stage2 should require export reorder, repeat channel demand, channel expansion, margin, or revision bridge, not beauty/K-consumer theme label alone","VT positive worked; Able C&C and Hankook Cosmetics theme/event rows failed positive-stage promotion","R5L89_C18_VT_2024_STAGE2_ACTIONABLE_KBEAUTY_EXPORT_REORDER|R5L89_C18_ABLECNC_2024_STAGE2_FALSE_POSITIVE_BEAUTY_EXPORT_THEME|R5L89_C18_HANKOOKCOS_2024_STAGE4B_KBEAUTY_THEME_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,configured,cap_beauty_and_Kconsumer_theme_premiums_as_4B_watch,0,"Beauty/K-consumer theme premiums can peak before verified export reorder and margin conversion appears","Able C&C and Hankook Cosmetics showed low MFE90 with high MAE90 after theme spikes","R5L89_C18_ABLECNC_2024_STAGE2_FALSE_POSITIVE_BEAUTY_EXPORT_THEME|R5L89_C18_HANKOOKCOS_2024_STAGE4B_KBEAUTY_THEME_CAP",2,2,2,low,guardrail_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R5L89_C18_VT_2024_KBEAUTY_EXPORT_REORDER_POSITIVE", "symbol": "018290", "company_name": "브이티", "round": "R5", "loop": "89", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KBEAUTY_EXPORT_REORDER_MARGIN_BRIDGE_VS_BRAND_THEME_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R5L89_C18_VT_2024_STAGE2_ACTIONABLE_KBEAUTY_EXPORT_REORDER", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "K-beauty export/channel reorder bridge produced high 30D/90D/180D MFE with shallow early MAE; C18 works when repeat demand and margin/revision bridge are visible.", "current_profile_verdict": "current_profile_kept_but_C18_positive_requires_export_reorder_channel_margin_bridge_not_beauty_label_only", "price_source": "Songdaiki/stock-web", "notes": "Modern 2024 window is clean relative to old CA candidates; source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R5L89_C18_ABLECNC_2024_BEAUTY_EXPORT_THEME_FALSE_STAGE2", "symbol": "078520", "company_name": "에이블씨엔씨", "round": "R5", "loop": "89", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KBEAUTY_EXPORT_REORDER_MARGIN_BRIDGE_VS_BRAND_THEME_EVENT_CAP", "case_type": "failed_rerating_high_mae", "positive_or_counterexample": "counterexample", "best_trigger": "R5L89_C18_ABLECNC_2024_STAGE2_FALSE_POSITIVE_BEAUTY_EXPORT_THEME", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Beauty export/brand premium failed to convert into durable channel reorder; low forward MFE and deep MAE argue against positive-stage promotion.", "current_profile_verdict": "current_profile_false_positive_if_beauty_export_theme_counts_without_reorder_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "No modern CA caveat; source-proxy only."}
{"row_type": "case", "case_id": "R5L89_C18_HANKOOKCOS_2024_KBEAUTY_THEME_EVENT_CAP_4B", "symbol": "123690", "company_name": "한국화장품", "round": "R5", "loop": "89", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KBEAUTY_EXPORT_REORDER_MARGIN_BRIDGE_VS_BRAND_THEME_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R5L89_C18_HANKOOKCOS_2024_STAGE4B_KBEAUTY_THEME_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "K-beauty theme premium capped around the July spike and then drew down; theme premium should route to 4B unless verified export reorder and margin bridge appear.", "current_profile_verdict": "current_profile_4B_too_late_if_Kbeauty_theme_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action caveat; source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R5L89_C18_VT_2024_STAGE2_ACTIONABLE_KBEAUTY_EXPORT_REORDER", "case_id": "R5L89_C18_VT_2024_KBEAUTY_EXPORT_REORDER_POSITIVE", "symbol": "018290", "company_name": "브이티", "round": "R5", "loop": "89", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KBEAUTY_EXPORT_REORDER_MARGIN_BRIDGE_VS_BRAND_THEME_EVENT_CAP", "sector": "Kbeauty_export_channel_reorder", "primary_archetype": "Kbeauty_export_reorder_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-25", "entry_date": "2024-03-25", "entry_price": 16750.0, "evidence_available_at_that_date": "K-beauty export channel reorder, repeat demand, and margin/revision bridge proxy; exact as-of URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["export_reorder_proxy", "channel_repeat_demand", "margin_revision_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["high_MFE30", "very_high_MFE90", "low_entry_MAE"], "stage4b_evidence_fields": ["valuation_repricing_watch_after_export_rerating"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv", "profile_path": "atlas/symbol_profiles/018/018290.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 54.63, "MFE_90D_pct": 138.81, "MFE_180D_pct": 138.81, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -3.94, "MAE_90D_pct": -3.94, "MAE_180D_pct": -3.94, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-19", "peak_price": 40000.0, "drawdown_after_peak_pct": -35.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_export_valuation_watch_needed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_Kbeauty_export_reorder_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L89_C18_018290_2024-03-25_16750", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R5L89_C18_ABLECNC_2024_STAGE2_FALSE_POSITIVE_BEAUTY_EXPORT_THEME", "case_id": "R5L89_C18_ABLECNC_2024_BEAUTY_EXPORT_THEME_FALSE_STAGE2", "symbol": "078520", "company_name": "에이블씨엔씨", "round": "R5", "loop": "89", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KBEAUTY_EXPORT_REORDER_MARGIN_BRIDGE_VS_BRAND_THEME_EVENT_CAP", "sector": "beauty_brand_export_theme", "primary_archetype": "beauty_export_theme_without_reorder_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-06-26", "entry_date": "2024-06-26", "entry_price": 9630.0, "evidence_available_at_that_date": "beauty export / brand channel premium spike proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["beauty_export_theme", "brand_channel_premium", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE90", "deep_MAE90", "reorder_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/078/078520/2024.csv", "profile_path": "atlas/symbol_profiles/078/078520.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.78, "MFE_90D_pct": 4.78, "MFE_180D_pct": 4.78, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -32.5, "MAE_90D_pct": -32.5, "MAE_180D_pct": -32.5, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-27", "peak_price": 10090.0, "drawdown_after_peak_pct": -35.58, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.95, "four_b_timing_verdict": "beauty_export_theme_spike_was_false_stage2_event_cap", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_beauty_export_theme_without_bridge", "current_profile_verdict": "current_profile_false_positive_if_beauty_export_theme_counts_without_reorder_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L89_C18_078520_2024-06-26_9630", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R5L89_C18_HANKOOKCOS_2024_STAGE4B_KBEAUTY_THEME_CAP", "case_id": "R5L89_C18_HANKOOKCOS_2024_KBEAUTY_THEME_EVENT_CAP_4B", "symbol": "123690", "company_name": "한국화장품", "round": "R5", "loop": "89", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KBEAUTY_EXPORT_REORDER_MARGIN_BRIDGE_VS_BRAND_THEME_EVENT_CAP", "sector": "Kbeauty_theme", "primary_archetype": "Kbeauty_theme_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-07-01", "entry_date": "2024-07-01", "entry_price": 8930.0, "evidence_available_at_that_date": "K-beauty theme premium after July spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["Kbeauty_theme", "brand_export_premium", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/123/123690/2024.csv", "profile_path": "atlas/symbol_profiles/123/123690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 15.34, "MFE_90D_pct": 15.34, "MFE_180D_pct": 15.34, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -29.56, "MAE_90D_pct": -29.56, "MAE_180D_pct": -29.56, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-01", "peak_price": 10300.0, "drawdown_after_peak_pct": -38.93, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_Kbeauty_theme_event_cap", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_Kbeauty_theme_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L89_C18_123690_2024-07-01_8930", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L89_C18_VT_2024_KBEAUTY_EXPORT_REORDER_POSITIVE", "trigger_id": "R5L89_C18_VT_2024_STAGE2_ACTIONABLE_KBEAUTY_EXPORT_REORDER", "symbol": "018290", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 75, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 40, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 60, "margin_bridge_score": 60, "revision_score": 55, "relative_strength_score": 75, "customer_quality_score": 50, "policy_or_regulatory_score": 0, "valuation_repricing_score": 55, "execution_risk_score": 25, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 75, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "Kbeauty_export_reorder_margin_positive", "MFE_90D_pct": 138.81, "MAE_90D_pct": -3.94, "score_return_alignment_label": "Kbeauty_export_reorder_margin_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L89_C18_ABLECNC_2024_BEAUTY_EXPORT_THEME_FALSE_STAGE2", "trigger_id": "R5L89_C18_ABLECNC_2024_STAGE2_FALSE_POSITIVE_BEAUTY_EXPORT_THEME", "symbol": "078520", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 75, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 40, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 0, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "beauty_export_theme_false_stage2", "MFE_90D_pct": 4.78, "MAE_90D_pct": -32.5, "score_return_alignment_label": "beauty_export_theme_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_beauty_export_theme_counts_without_reorder_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L89_C18_HANKOOKCOS_2024_KBEAUTY_THEME_EVENT_CAP_4B", "trigger_id": "R5L89_C18_HANKOOKCOS_2024_STAGE4B_KBEAUTY_THEME_CAP", "symbol": "123690", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 75, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 40, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 0, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "Kbeauty_theme_event_cap_4B_guard", "MFE_90D_pct": 15.34, "MAE_90D_pct": -29.56, "score_return_alignment_label": "Kbeauty_theme_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_Kbeauty_theme_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": "89", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KBEAUTY_EXPORT_REORDER_MARGIN_BRIDGE_VS_BRAND_THEME_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["Kbeauty_export_reorder_margin_positive", "beauty_export_theme_false_stage2", "Kbeauty_theme_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
completed_loop = 89
next_round = R6
next_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.

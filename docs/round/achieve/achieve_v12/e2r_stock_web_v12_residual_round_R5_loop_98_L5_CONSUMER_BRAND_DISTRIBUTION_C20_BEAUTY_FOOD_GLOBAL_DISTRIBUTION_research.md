# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R5
scheduled_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_BRAND_EXPORT_DTC_REORDER_BRIDGE_VS_MASS_COSMETIC_CHANNEL_FALSE_STAGE2_AND_SMALL_CAP_BEAUTY_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | beauty_food_distribution_reorder_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R5_loop_98_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
```

This file is the corrected final output for this execution. The scheduler state after R4 loop 98 is R5 / loop 98. R5 is the L5 consumer / brand / distribution round, and this run fills C20 beauty/food global distribution rather than repeating the immediately preceding R5 loop 97 C19 retail inventory-margin file or the older R5 loop 95 C20 symbol set.

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
beauty_food_distribution_reorder_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R5
scheduled_loop = 98
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
round_sector_consistency = pass
computed_next_round = R6
computed_next_loop = 98
```

C20 is a beauty/food global distribution and reorder archetype. A K-beauty or global distribution label is the storefront; the signal becomes usable only when export sell-through, reorder cadence, inventory turn, channel efficiency, margin and revision are all connected.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION = 19 rows / 11 symbols / good-bad Stage2 8-2 / 4B-4C 4-0
top covered symbols include 226320(3), 161890(2), 192820(2), 214420(2), 241710(2), 439090(2)
previous R5 loop-88 C20 symbols avoided: 003230, 005180, 011150
previous R5 loop-91 C20 symbols avoided: 090430, 051900, 097950
previous R5 loop-95 C20 symbols avoided: 002790, 027050, 003350
previous R5 loop-97 C19 symbols avoided: 023530, 383220, 008770
previous R4 loop-98 C16 symbols avoided: 336370, 000910, 024890
```

Selected rows avoid hard duplicates and top repeated C20 symbols:

```text
114840 / Stage2-Actionable / 2024-03-25
237880 / Stage2-Actionable / 2024-06-13
406820 / Stage4B / 2024-05-31
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
| 114840 | atlas/symbol_profiles/114/114840.json | selected entry after 2024-02-28 and 2024-03-21 CA candidates; 180D forward window used as post-CA clean |
| 237880 | atlas/symbol_profiles/237/237880.json | no corporate-action candidate |
| 406820 | atlas/symbol_profiles/406/406820.json | 2024 window clean before 2026 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R5L98_C20_IFAMILYSC_2024_K_BEAUTY_EXPORT_DTC_REORDER_BRIDGE_POSITIVE | 114840 | 2024-03-25 | yes | 180 | yes | post-CA clean | true |
| R5L98_C20_CLIO_2024_MASS_COSMETIC_CHANNEL_FALSE_STAGE2 | 237880 | 2024-06-13 | yes | 180 | yes | yes | true |
| R5L98_C20_BEAUTYSKIN_2024_SMALL_CAP_K_BEAUTY_EVENT_CAP_4B | 406820 | 2024-05-31 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_BEAUTY_BRAND_EXPORT_DTC_REORDER_BRIDGE | Positive Stage2 requires export channel sell-through, DTC/platform traction, reorder cadence, inventory turn, margin and revision bridge. |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | MASS_COSMETIC_CHANNEL_FALSE_STAGE2 | Cosmetic channel watch without sell-through/reorder/margin bridge can become false Stage2. |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | SMALL_CAP_BEAUTY_EVENT_CAP_4B | Small-cap K-beauty event premium should route to 4B when reorder and margin bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R5L98_C20_IFAMILYSC_2024_K_BEAUTY_EXPORT_DTC_REORDER_BRIDGE_POSITIVE | 114840 | 아이패밀리에스씨 | positive | Post-CA K-beauty export/DTC reorder bridge produced very strong MFE with acceptable early MAE. |
| R5L98_C20_CLIO_2024_MASS_COSMETIC_CHANNEL_FALSE_STAGE2 | 237880 | 클리오 | counterexample | Mass-cosmetic channel watch had low forward MFE and high MAE without reorder/margin bridge. |
| R5L98_C20_BEAUTYSKIN_2024_SMALL_CAP_K_BEAUTY_EVENT_CAP_4B | 406820 | 뷰티스킨 | counterexample / 4B | Small-cap K-beauty premium capped near the late-May/early-June spike and then de-rated. |

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
| iFamilySC K-beauty export/DTC reorder bridge | historical public/report proxy | true | true | shadow-only positive |
| Clio mass-cosmetic channel false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| BeautySkin small-cap K-beauty event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 114840 | atlas/ohlcv_tradable_by_symbol_year/114/114840/2024.csv | atlas/symbol_profiles/114/114840.json |
| 237880 | atlas/ohlcv_tradable_by_symbol_year/237/237880/2024.csv | atlas/symbol_profiles/237/237880.json |
| 406820 | atlas/ohlcv_tradable_by_symbol_year/406/406820/2024.csv | atlas/symbol_profiles/406/406820.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R5L98_C20_IFAMILYSC_2024_STAGE2_ACTIONABLE_K_BEAUTY_EXPORT_DTC_REORDER_BRIDGE | 114840 | Stage2-Actionable | 2024-03-25 | 20150 | positive | K-beauty export/DTC reorder bridge worked |
| R5L98_C20_CLIO_2024_STAGE2_FALSE_POSITIVE_MASS_COSMETIC_CHANNEL_MARGIN_WATCH | 237880 | Stage2-Actionable | 2024-06-13 | 43100 | counterexample | mass-cosmetic channel false Stage2 |
| R5L98_C20_BEAUTYSKIN_2024_STAGE4B_SMALL_CAP_K_BEAUTY_EVENT_CAP | 406820 | Stage4B | 2024-05-31 | 25850 | counterexample/4B | small-cap K-beauty event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R5L98_C20_IFAMILYSC_2024_STAGE2_ACTIONABLE_K_BEAUTY_EXPORT_DTC_REORDER_BRIDGE | 20150 | 79.16 | -11.66 | 124.07 | -11.66 | 124.07 | -11.66 | 2024-06-03 | 45150 | -56.70 |
| R5L98_C20_CLIO_2024_STAGE2_FALSE_POSITIVE_MASS_COSMETIC_CHANNEL_MARGIN_WATCH | 43100 | 4.41 | -17.52 | 4.41 | -29.93 | 4.41 | -35.96 | 2024-06-13 | 45000 | -38.22 |
| R5L98_C20_BEAUTYSKIN_2024_STAGE4B_SMALL_CAP_K_BEAUTY_EVENT_CAP | 25850 | 12.77 | -19.92 | 12.77 | -35.24 | 12.77 | -53.42 | 2024-06-04 | 29150 | -62.26 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C20 Stage2 needs export sell-through / reorder / DTC-platform traction / inventory turn / margin / revision bridge |
| beauty_food_distribution_reorder_guardrail | strengthen: beauty/food/global distribution labels alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing cosmetic channel and small-cap beauty event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE C20 rows cannot promote without durable reorder/margin bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether beauty/food global distribution narrative becomes export sell-through, reorder and margin evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 114840 | good_stage2_with_later_watch | Export/DTC reorder bridge produced very strong MFE, but later channel valuation watch remains necessary. |
| 237880 | bad_stage2 | Cosmetic channel watch lacked confirmed reorder/margin bridge and suffered high MAE. |
| 406820 | good_4B | Small-cap K-beauty event premium peaked near the early-June high and later drew down deeply. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 237880 cosmetic channel false Stage2 | 0.96 | 0.96 | false Stage2 due missing sell-through / reorder / inventory / margin bridge |
| 406820 small-cap K-beauty cap | 0.89 | 0.89 | good full-window 4B timing after K-beauty event premium |
| 114840 K-beauty export bridge | n/a | n/a | positive Stage2, but later K-beauty channel valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 237880 / 406820
```

No hard 4C candidate is introduced in this R5 loop 98 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L5 beauty/food global distribution cases, Stage2 requires verified export sell-through, channel reorder cadence, DTC/platform traction, inventory turn, marketing efficiency, margin, or revision bridge. Beauty, food, global distribution, K-beauty, cosmetic channel, small-cap event or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
rule = C20 should split true export sell-through/reorder/margin positives from mass-cosmetic channel false Stage2 and small-cap K-beauty event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 47.08 | -25.61 | 0.67 | mixed; C20 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 47.08 | -25.61 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L5 export/reorder/margin bridge required | 2 | 64.24 | -20.80 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C20 bridge vs event-cap split | 2 | 64.24 | -20.80 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing beauty/food distribution themes as positive | 1 | 124.07 | -11.66 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 114840 K-beauty export/DTC bridge | 66 | Stage2-Watch | 79 | Stage2-Actionable | 124.07 | -11.66 | K_beauty_export_reorder_positive |
| 237880 cosmetic channel false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 4.41 | -29.93 | cosmetic_channel_false_stage2 |
| 406820 small-cap K-beauty cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 12.77 | -35.24 | small_cap_K_beauty_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_BRAND_EXPORT_DTC_REORDER_BRIDGE_VS_MASS_COSMETIC_CHANNEL_FALSE_STAGE2_AND_SMALL_CAP_BEAUTY_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds R5 loop98 C20: iFamilySC K-beauty export/DTC reorder positive, Clio mass-cosmetic channel false Stage2, and BeautySkin small-cap K-beauty event-cap 4B while avoiding top repeated C20 and previous R5/R4 loop symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, beauty_food_distribution_reorder_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: K_beauty_export_reorder_positive, cosmetic_channel_false_stage2, small_cap_K_beauty_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, beauty_food_distribution_reorder_guardrail, high_MAE_guardrail
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
- C20 beauty/food global distribution bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,configured,C20_requires_export_channel_sellthrough_reorder_inventory_margin_revision_bridge,0,"C20 Stage2 should require export sell-through, channel reorder cadence, DTC/platform traction, inventory turn, marketing efficiency, margin, or revision bridge, not beauty/food/global distribution label alone","iFamilySC positive worked; Clio and BeautySkin event/watch rows failed positive-stage promotion","R5L98_C20_IFAMILYSC_2024_STAGE2_ACTIONABLE_K_BEAUTY_EXPORT_DTC_REORDER_BRIDGE|R5L98_C20_CLIO_2024_STAGE2_FALSE_POSITIVE_MASS_COSMETIC_CHANNEL_MARGIN_WATCH|R5L98_C20_BEAUTYSKIN_2024_STAGE4B_SMALL_CAP_K_BEAUTY_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,configured,cap_bridge_missing_mass_cosmetic_and_small_cap_beauty_event_premiums_as_4B_watch,0,"Cosmetic channel and small-cap K-beauty premiums can peak before sell-through, reorder cadence, inventory turn and margin bridge is proven","Clio had low MFE and high MAE after channel watch; BeautySkin showed 4B event-cap behavior after the late-May K-beauty spike","R5L98_C20_CLIO_2024_STAGE2_FALSE_POSITIVE_MASS_COSMETIC_CHANNEL_MARGIN_WATCH|R5L98_C20_BEAUTYSKIN_2024_STAGE4B_SMALL_CAP_K_BEAUTY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,configured,block_positive_stage_when_beauty_food_theme_has_high_or_persistent_MAE_without_reorder_margin_bridge,0,"High or persistent MAE after bridge-missing C20 entries should block Stage2/Stage3 promotion unless export sell-through, reorder and margin evidence survives","Clio MAE90=-29.93 and BeautySkin MAE90=-35.24","R5L98_C20_CLIO_2024_STAGE2_FALSE_POSITIVE_MASS_COSMETIC_CHANNEL_MARGIN_WATCH|R5L98_C20_BEAUTYSKIN_2024_STAGE4B_SMALL_CAP_K_BEAUTY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R5L98_C20_IFAMILYSC_2024_K_BEAUTY_EXPORT_DTC_REORDER_BRIDGE_POSITIVE", "symbol": "114840", "company_name": "아이패밀리에스씨", "round": "R5", "loop": "98", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_BRAND_EXPORT_DTC_REORDER_BRIDGE_VS_MASS_COSMETIC_CHANNEL_FALSE_STAGE2_AND_SMALL_CAP_BEAUTY_EVENT_CAP", "case_type": "structural_success_with_later_K_beauty_valuation_and_channel_watch", "positive_or_counterexample": "positive", "best_trigger": "R5L98_C20_IFAMILYSC_2024_STAGE2_ACTIONABLE_K_BEAUTY_EXPORT_DTC_REORDER_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "K-beauty brand export / DTC reorder / channel expansion bridge produced very strong 30D/90D/180D MFE after the post-CA March base. The later valuation drawdown means C20 positives still need 4B valuation/channel watch rather than unconditional Green promotion.", "current_profile_verdict": "current_profile_kept_but_C20_positive_requires_export_channel_sellthrough_reorder_DTC_margin_revision_bridge_not_beauty_label_only", "price_source": "Songdaiki/stock-web", "notes": "Entry selected after 2024-02-28 and 2024-03-21 corporate-action candidate boundaries. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R5L98_C20_CLIO_2024_MASS_COSMETIC_CHANNEL_FALSE_STAGE2", "symbol": "237880", "company_name": "클리오", "round": "R5", "loop": "98", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_BRAND_EXPORT_DTC_REORDER_BRIDGE_VS_MASS_COSMETIC_CHANNEL_FALSE_STAGE2_AND_SMALL_CAP_BEAUTY_EVENT_CAP", "case_type": "failed_rerating_mass_cosmetic_channel_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R5L98_C20_CLIO_2024_STAGE2_FALSE_POSITIVE_MASS_COSMETIC_CHANNEL_MARGIN_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Mass cosmetic / channel-expansion watch near the June spike had only limited forward MFE and then high MAE. C20 Stage2 should not be awarded without confirmed export sell-through, channel reorder, inventory turn, marketing efficiency, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_cosmetic_channel_watch_counts_without_sellthrough_reorder_inventory_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
{"row_type": "case", "case_id": "R5L98_C20_BEAUTYSKIN_2024_SMALL_CAP_K_BEAUTY_EVENT_CAP_4B", "symbol": "406820", "company_name": "뷰티스킨", "round": "R5", "loop": "98", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_BRAND_EXPORT_DTC_REORDER_BRIDGE_VS_MASS_COSMETIC_CHANNEL_FALSE_STAGE2_AND_SMALL_CAP_BEAUTY_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R5L98_C20_BEAUTYSKIN_2024_STAGE4B_SMALL_CAP_K_BEAUTY_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Small-cap K-beauty event premium capped around the late-May/early-June spike and then de-rated sharply. C20 should route bridge-missing beauty event premiums to 4B unless export channel, reorder cadence, sell-through, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_small_cap_K_beauty_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "2024 window clean; profile flags only 2026 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R5L98_C20_IFAMILYSC_2024_STAGE2_ACTIONABLE_K_BEAUTY_EXPORT_DTC_REORDER_BRIDGE", "case_id": "R5L98_C20_IFAMILYSC_2024_K_BEAUTY_EXPORT_DTC_REORDER_BRIDGE_POSITIVE", "symbol": "114840", "company_name": "아이패밀리에스씨", "round": "R5", "loop": "98", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_BRAND_EXPORT_DTC_REORDER_BRIDGE_VS_MASS_COSMETIC_CHANNEL_FALSE_STAGE2_AND_SMALL_CAP_BEAUTY_EVENT_CAP", "sector": "K_beauty_brand_export_DTC_reorder_margin", "primary_archetype": "export_channel_sellthrough_reorder_DTC_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | beauty_food_distribution_reorder_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-25", "entry_date": "2024-03-25", "entry_price": 20150.0, "evidence_available_at_that_date": "K-beauty brand export, DTC/channel expansion, reorder cadence, sell-through and margin/revision bridge proxy after post-CA March base; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["export_channel_proxy", "DTC_channel_proxy", "sellthrough_reorder_proxy", "inventory_turn_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["very_strong_MFE30", "very_strong_MFE90", "post_CA_clean_window"], "stage4b_evidence_fields": ["later_K_beauty_valuation_watch", "channel_reorder_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/114/114840/2024.csv", "profile_path": "atlas/symbol_profiles/114/114840.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 79.16, "MFE_90D_pct": 124.07, "MFE_180D_pct": 124.07, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -11.66, "MAE_90D_pct": -11.66, "MAE_180D_pct": -11.66, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-03", "peak_price": 45150.0, "drawdown_after_peak_pct": -56.7, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_K_beauty_channel_valuation_4B_watch_needed", "four_b_evidence_type": ["K_beauty_export_reorder_bridge", "DTC_channel", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_K_beauty_export_DTC_reorder_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "post_2024-03-21_CA_boundary_clean_180D_window", "same_entry_group_id": "R5L98_C20_114840_2024-03-25_20150", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R5L98_C20_CLIO_2024_STAGE2_FALSE_POSITIVE_MASS_COSMETIC_CHANNEL_MARGIN_WATCH", "case_id": "R5L98_C20_CLIO_2024_MASS_COSMETIC_CHANNEL_FALSE_STAGE2", "symbol": "237880", "company_name": "클리오", "round": "R5", "loop": "98", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_BRAND_EXPORT_DTC_REORDER_BRIDGE_VS_MASS_COSMETIC_CHANNEL_FALSE_STAGE2_AND_SMALL_CAP_BEAUTY_EVENT_CAP", "sector": "mass_cosmetic_export_channel_margin_watch", "primary_archetype": "cosmetic_channel_watch_without_sellthrough_reorder_inventory_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | beauty_food_distribution_reorder_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-06-13", "entry_date": "2024-06-13", "entry_price": 43100.0, "evidence_available_at_that_date": "mass cosmetic / channel expansion watch near June K-beauty spike without confirmed reorder cadence, export sell-through, inventory turn, marketing efficiency or margin revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["cosmetic_channel_watch", "K_beauty_export_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["limited_MFE90", "high_MAE90", "sellthrough_reorder_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/237/237880/2024.csv", "profile_path": "atlas/symbol_profiles/237/237880.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.41, "MFE_90D_pct": 4.41, "MFE_180D_pct": 4.41, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -17.52, "MAE_90D_pct": -29.93, "MAE_180D_pct": -35.96, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-13", "peak_price": 45000.0, "drawdown_after_peak_pct": -38.22, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "cosmetic_channel_margin_watch_was_false_stage2_due_missing_sellthrough_reorder_inventory_margin_bridge", "four_b_evidence_type": ["K_beauty_channel_premium", "bridge_missing", "low_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_mass_cosmetic_channel_watch_without_reorder_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_cosmetic_channel_watch_counts_without_sellthrough_reorder_inventory_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R5L98_C20_237880_2024-06-13_43100", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R5L98_C20_BEAUTYSKIN_2024_STAGE4B_SMALL_CAP_K_BEAUTY_EVENT_CAP", "case_id": "R5L98_C20_BEAUTYSKIN_2024_SMALL_CAP_K_BEAUTY_EVENT_CAP_4B", "symbol": "406820", "company_name": "뷰티스킨", "round": "R5", "loop": "98", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_BRAND_EXPORT_DTC_REORDER_BRIDGE_VS_MASS_COSMETIC_CHANNEL_FALSE_STAGE2_AND_SMALL_CAP_BEAUTY_EVENT_CAP", "sector": "small_cap_K_beauty_export_event_premium", "primary_archetype": "small_cap_K_beauty_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | beauty_food_distribution_reorder_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-05-31", "entry_date": "2024-05-31", "entry_price": 25850.0, "evidence_available_at_that_date": "small-cap K-beauty event premium after export/channel theme spike without confirmed reorder cadence, overseas sell-through, inventory turn, margin or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["small_cap_K_beauty_event", "export_channel_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE90", "sellthrough_reorder_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/406/406820/2024.csv", "profile_path": "atlas/symbol_profiles/406/406820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 12.77, "MFE_90D_pct": 12.77, "MFE_180D_pct": 12.77, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -19.92, "MAE_90D_pct": -35.24, "MAE_180D_pct": -53.42, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-04", "peak_price": 29150.0, "drawdown_after_peak_pct": -62.26, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.89, "four_b_full_window_peak_proximity": 0.89, "four_b_timing_verdict": "good_full_window_4B_timing_small_cap_K_beauty_event_cap_due_missing_reorder_margin_bridge", "four_b_evidence_type": ["small_cap_K_beauty_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_small_cap_K_beauty_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_small_cap_K_beauty_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_before_2026_CA_candidates", "same_entry_group_id": "R5L98_C20_406820_2024-05-31_25850", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L98_C20_IFAMILYSC_2024_K_BEAUTY_EXPORT_DTC_REORDER_BRIDGE_POSITIVE", "trigger_id": "R5L98_C20_IFAMILYSC_2024_STAGE2_ACTIONABLE_K_BEAUTY_EXPORT_DTC_REORDER_BRIDGE", "symbol": "114840", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 65, "customer_quality_score": 45, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 50, "backlog_visibility_score": 60, "margin_bridge_score": 60, "revision_score": 60, "relative_strength_score": 80, "customer_quality_score": 60, "policy_or_regulatory_score": 10, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 79, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "K_beauty_export_DTC_reorder_positive", "MFE_90D_pct": 124.07, "MAE_90D_pct": -11.66, "score_return_alignment_label": "K_beauty_export_reorder_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L98_C20_CLIO_2024_MASS_COSMETIC_CHANNEL_FALSE_STAGE2", "trigger_id": "R5L98_C20_CLIO_2024_STAGE2_FALSE_POSITIVE_MASS_COSMETIC_CHANNEL_MARGIN_WATCH", "symbol": "237880", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 65, "execution_risk_score": 60, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "mass_cosmetic_channel_false_stage2", "MFE_90D_pct": 4.41, "MAE_90D_pct": -29.93, "score_return_alignment_label": "cosmetic_channel_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_cosmetic_channel_watch_counts_without_sellthrough_reorder_inventory_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L98_C20_BEAUTYSKIN_2024_SMALL_CAP_K_BEAUTY_EVENT_CAP_4B", "trigger_id": "R5L98_C20_BEAUTYSKIN_2024_STAGE4B_SMALL_CAP_K_BEAUTY_EVENT_CAP", "symbol": "406820", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 75, "customer_quality_score": 20, "policy_or_regulatory_score": 10, "valuation_repricing_score": 65, "execution_risk_score": 65, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "small_cap_K_beauty_event_cap_4B_guard", "MFE_90D_pct": 12.77, "MAE_90D_pct": -35.24, "score_return_alignment_label": "small_cap_K_beauty_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_small_cap_K_beauty_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": "98", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_BRAND_EXPORT_DTC_REORDER_BRIDGE_VS_MASS_COSMETIC_CHANNEL_FALSE_STAGE2_AND_SMALL_CAP_BEAUTY_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "beauty_food_distribution_reorder_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["K_beauty_export_reorder_positive", "cosmetic_channel_false_stage2", "small_cap_K_beauty_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- False-positive rows should strengthen bridge requirements, not generate positive promotion.
- C20 rows need explicit export sell-through, channel reorder cadence, DTC/platform traction, inventory turn, marketing efficiency, margin or revision bridge before positive promotion.
- In C20, bridge-missing beauty/food distribution event-premium rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C20 beauty/food global distribution rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R5
completed_loop = 98
next_round = R6
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.

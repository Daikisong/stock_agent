# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R5
scheduled_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_APPAREL_CHANNEL_INVENTORY_FALSE_STAGE2_AND_SEAFOOD_K_FOOD_EVENT_CAP
loop_objective = priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | export_channel_reorder_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R5_loop_99_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
```

This file is the corrected final output for this execution. The scheduler is coverage-index-first. C15 was the immediately preceding final artifact. Priority 1 already added C03, C16, C04, C05 and C15, so C18 is the next unsupplemented Priority 1 gap below the 50-row practical calibration zone. Since R5 loop98 was used locally for C19, this file uses R5 loop99 to avoid local round-loop collision.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_2_rolling_calibrated
previous_baseline_reference = e2r_2_1_stock_web_calibrated
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
export_channel_reorder_margin_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R5
scheduled_loop = 99
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
round_sector_consistency = pass
coverage_index_override_previous_round = true
```

C18 is a consumer export channel reorder archetype. First shipment is the storefront opening; the investable signal is whether customers reorder, overseas sell-through stays clean, channel inventory does not clog, and ASP/OPM/revision actually follow.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C18_CONSUMER_EXPORT_CHANNEL_REORDER = 33 rows / Priority 1
recent local Priority 0/1 artifacts accounted for: C08, C09, C01, C07, C06, C10, C14, C11, C02, C13, C19, C27, C12, C24, C28, C17, C23, C03, C16, C04, C05, C15
immediately preceding C15 artifact not duplicated
```

Selected rows avoid hard duplicates and add new C18 trigger families:

```text
003230 / Stage2-Actionable / 2024-02-15
383220 / Stage2-Actionable / 2024-01-02
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
| 003230 | atlas/symbol_profiles/003/003230.json | selected 2024 window clean after old 2003 CA candidate |
| 383220 | atlas/symbol_profiles/383/383220.json | selected 2024 window clean after old 2022 CA candidate |
| 011150 | atlas/symbol_profiles/011/011150.json | selected 2024 window clean after old 2002 CA candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R5L99_C18_SAMYANGFOODS_2024_K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE_POSITIVE | 003230 | 2024-02-15 | yes | 180 | yes | yes | true |
| R5L99_C18_FNF_2024_APPAREL_EXPORT_CHANNEL_INVENTORY_FALSE_STAGE2 | 383220 | 2024-01-02 | yes | 180 | yes | yes | true |
| R5L99_C18_CJSEAFOOD_2024_SEAFOOD_K_FOOD_EXPORT_EVENT_CAP_4B | 011150 | 2024-06-14 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE | Positive Stage2 requires repeat reorder, overseas sell-through, channel inventory discipline, ASP/mix, OPM and revision bridge. |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | APPAREL_CHANNEL_INVENTORY_FALSE_STAGE2 | Apparel export/channel watch without sell-through and inventory normalization can become false Stage2. |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | SEAFOOD_K_FOOD_EVENT_CAP_4B | K-food/seafood export premium should route to 4B when repeat reorder and margin bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R5L99_C18_SAMYANGFOODS_2024_K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE_POSITIVE | 003230 | 삼양식품 | positive | K-food export reorder/margin bridge produced extreme MFE with shallow early MAE. |
| R5L99_C18_FNF_2024_APPAREL_EXPORT_CHANNEL_INVENTORY_FALSE_STAGE2 | 383220 | F&F | counterexample | Apparel export/channel watch had tiny MFE and persistent drawdown without sell-through/inventory bridge. |
| R5L99_C18_CJSEAFOOD_2024_SEAFOOD_K_FOOD_EXPORT_EVENT_CAP_4B | 011150 | CJ씨푸드 | counterexample / 4B | K-food/seafood event premium capped after the June spike and then de-rated sharply. |

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
| F&F apparel export channel inventory false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| CJ Seafood K-food export event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 003230 | atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv | atlas/symbol_profiles/003/003230.json |
| 383220 | atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv | atlas/symbol_profiles/383/383220.json |
| 011150 | atlas/ohlcv_tradable_by_symbol_year/011/011150/2024.csv | atlas/symbol_profiles/011/011150.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R5L99_C18_SAMYANGFOODS_2024_STAGE2_ACTIONABLE_K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE | 003230 | Stage2-Actionable | 2024-02-15 | 177400 | positive | K-food export reorder bridge worked |
| R5L99_C18_FNF_2024_STAGE2_FALSE_POSITIVE_APPAREL_EXPORT_CHANNEL_INVENTORY_WATCH | 383220 | Stage2-Actionable | 2024-01-02 | 87300 | counterexample | apparel export/channel false Stage2 |
| R5L99_C18_CJSEAFOOD_2024_STAGE4B_SEAFOOD_K_FOOD_EXPORT_EVENT_CAP | 011150 | Stage4B | 2024-06-14 | 6320 | counterexample/4B | K-food seafood event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R5L99_C18_SAMYANGFOODS_2024_STAGE2_ACTIONABLE_K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE | 177400 | 21.48 | -4.40 | 304.74 | -4.40 | 304.74 | -4.40 | 2024-06-19 | 718000 | -32.31 |
| R5L99_C18_FNF_2024_STAGE2_FALSE_POSITIVE_APPAREL_EXPORT_CHANNEL_INVENTORY_WATCH | 87300 | 2.52 | -23.94 | 2.52 | -31.16 | 2.52 | -45.99 | 2024-01-02 | 89500 | -47.32 |
| R5L99_C18_CJSEAFOOD_2024_STAGE4B_SEAFOOD_K_FOOD_EXPORT_EVENT_CAP | 6320 | 2.69 | -33.86 | 2.69 | -33.86 | 2.69 | -33.86 | 2024-06-17 | 6490 | -35.59 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C18 Stage2 needs export reorder / overseas sell-through / channel inventory / ASP-mix / OPM / revision bridge |
| export_channel_reorder_margin_guardrail | strengthen: export, channel, K-food or apparel labels alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing apparel channel and K-food event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE C18 rows cannot promote without durable reorder/margin bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether export/channel narrative becomes repeat reorder, sell-through and OPM evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 003230 | good_stage2_with_later_watch | K-food export reorder bridge produced extreme MFE, but later valuation watch remains necessary. |
| 383220 | bad_stage2 | Apparel channel watch lacked sell-through/reorder inventory bridge and produced persistent drawdown. |
| 011150 | good_4B | K-food/seafood event premium peaked around June and later drew down without durable reorder bridge. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 383220 apparel export/channel false Stage2 | 0.98 | 0.98 | false Stage2 due missing sell-through / reorder / inventory / OPM bridge |
| 011150 K-food seafood event cap | 0.97 | 0.97 | good 4B timing after K-food export event premium |
| 003230 K-food export reorder bridge | n/a | n/a | positive Stage2, but later export valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = channel_inventory_break_watch_only for 383220 / 011150
```

No hard 4C candidate is introduced in this C18 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L5 consumer export channel-reorder cases, Stage2 requires verified repeat reorder, overseas sell-through, channel inventory discipline, ASP/mix, OPM and revision bridge. Export, K-food, apparel, channel expansion, overseas distributor or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
rule = C18 should split true export reorder/sell-through/margin positives from channel-inventory false Stage2 and K-food event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current profile | 3 | 103.32 | -23.14 | 0.67 | mixed; C18 reorder/margin bridge split needed |
| P0b e2r_2_1_stock_web_calibrated_reference | older calibrated baseline | 3 | 103.32 | -23.14 | 0.67 | weaker C18 bridge split |
| P1 sector_specific_candidate_profile | L5 export reorder/margin bridge required | 2 | 153.63 | -17.78 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C18 bridge vs event-cap split | 2 | 153.63 | -17.78 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing consumer export themes as positive | 1 | 304.74 | -4.40 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 003230 K-food export bridge | 66 | Stage2-Watch | 84 | Stage2-Actionable | 304.74 | -4.40 | consumer_export_reorder_positive |
| 383220 apparel channel false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 2.52 | -31.16 | apparel_channel_false_stage2 |
| 011150 K-food event cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 2.69 | -33.86 | K_food_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_APPAREL_CHANNEL_INVENTORY_FALSE_STAGE2_AND_SEAFOOD_K_FOOD_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "C18 is the next unsupplemented Priority 1 archetype after C03/C16/C04/C05/C15 and still remains below the practical 50-row calibration zone. This run adds Samyang Foods, F&F, and CJ Seafood while avoiding the immediately preceding C15 artifact and the C19 brand-retail file."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, export_channel_reorder_margin_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: consumer_export_reorder_positive, apparel_channel_false_stage2, K_food_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, export_channel_reorder_margin_guardrail, high_MAE_guardrail
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: priority1_canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-web tradable raw OHLC path
- entry_date / entry_price
- MFE/MAE 30D/90D/180D
- corporate-action window cleanliness
- C18 consumer export channel-reorder bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,configured,C18_requires_export_reorder_sellthrough_inventory_ASP_OPM_revision_bridge,0,"C18 Stage2 should require export reorder cadence, overseas sell-through, channel inventory discipline, ASP/mix, OPM and revision bridge, not export/channel/K-food label alone","Samyang Foods positive worked; F&F and CJ Seafood event/watch rows failed positive-stage promotion","R5L99_C18_SAMYANGFOODS_2024_STAGE2_ACTIONABLE_K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE|R5L99_C18_FNF_2024_STAGE2_FALSE_POSITIVE_APPAREL_EXPORT_CHANNEL_INVENTORY_WATCH|R5L99_C18_CJSEAFOOD_2024_STAGE4B_SEAFOOD_K_FOOD_EXPORT_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,configured,cap_bridge_missing_apparel_channel_and_K_food_event_premiums_as_4B_watch,0,"Apparel export/channel and K-food export premiums can peak before repeat reorder, sell-through, inventory and OPM bridge is proven","F&F had tiny MFE and persistent drawdown after January channel watch; CJ Seafood showed 4B event-cap behavior after June K-food/seafood premium","R5L99_C18_FNF_2024_STAGE2_FALSE_POSITIVE_APPAREL_EXPORT_CHANNEL_INVENTORY_WATCH|R5L99_C18_CJSEAFOOD_2024_STAGE4B_SEAFOOD_K_FOOD_EXPORT_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,configured,block_positive_stage_when_export_channel_theme_has_high_or_persistent_MAE_without_reorder_margin_bridge,0,"High or persistent MAE after bridge-missing C18 entries should block Stage2/Stage3 promotion unless sell-through, reorder and OPM evidence survives","F&F MAE90=-31.16 and CJ Seafood MAE90=-33.86","R5L99_C18_FNF_2024_STAGE2_FALSE_POSITIVE_APPAREL_EXPORT_CHANNEL_INVENTORY_WATCH|R5L99_C18_CJSEAFOOD_2024_STAGE4B_SEAFOOD_K_FOOD_EXPORT_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R5L99_C18_SAMYANGFOODS_2024_K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE_POSITIVE", "symbol": "003230", "company_name": "삼양식품", "round": "R5", "loop": "99", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_APPAREL_CHANNEL_INVENTORY_FALSE_STAGE2_AND_SEAFOOD_K_FOOD_EVENT_CAP", "case_type": "structural_success_with_later_export_channel_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R5L99_C18_SAMYANGFOODS_2024_STAGE2_ACTIONABLE_K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "K-food export / channel reorder / margin bridge produced extreme 90D MFE with shallow early MAE after the February base. C18 works when export momentum is tied to repeat reorder, distributor sell-through, channel inventory discipline, ASP/mix, OPM and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C18_positive_requires_export_reorder_sellthrough_inventory_ASP_OPM_revision_bridge_not_K_food_export_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2003 corporate-action candidate. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R5L99_C18_FNF_2024_APPAREL_EXPORT_CHANNEL_INVENTORY_FALSE_STAGE2", "symbol": "383220", "company_name": "F&F", "round": "R5", "loop": "99", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_APPAREL_CHANNEL_INVENTORY_FALSE_STAGE2_AND_SEAFOOD_K_FOOD_EVENT_CAP", "case_type": "failed_rerating_apparel_export_channel_inventory_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R5L99_C18_FNF_2024_STAGE2_FALSE_POSITIVE_APPAREL_EXPORT_CHANNEL_INVENTORY_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Apparel export/channel recovery watch at the January high had tiny MFE and then persistent drawdown. C18 Stage2 should not be awarded without sell-through recovery, reorder cadence, channel inventory normalization, China/overseas distributor quality, OPM and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_apparel_export_channel_watch_counts_without_sellthrough_reorder_inventory_OPM_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2022 corporate-action candidate. Source-proxy only."}
{"row_type": "case", "case_id": "R5L99_C18_CJSEAFOOD_2024_SEAFOOD_K_FOOD_EXPORT_EVENT_CAP_4B", "symbol": "011150", "company_name": "CJ씨푸드", "round": "R5", "loop": "99", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_APPAREL_CHANNEL_INVENTORY_FALSE_STAGE2_AND_SEAFOOD_K_FOOD_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R5L99_C18_CJSEAFOOD_2024_STAGE4B_SEAFOOD_K_FOOD_EXPORT_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Seafood/K-food export event premium capped after the June spike and then de-rated sharply. C18 should route bridge-missing K-food export premiums to 4B unless repeat reorder, sell-through, channel inventory, ASP/mix, OPM and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_K_food_export_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2002 corporate-action candidate. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R5L99_C18_SAMYANGFOODS_2024_STAGE2_ACTIONABLE_K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE", "case_id": "R5L99_C18_SAMYANGFOODS_2024_K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE_POSITIVE", "symbol": "003230", "company_name": "삼양식품", "round": "R5", "loop": "99", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_APPAREL_CHANNEL_INVENTORY_FALSE_STAGE2_AND_SEAFOOD_K_FOOD_EVENT_CAP", "sector": "K_food_export_reorder_channel_sellthrough_margin", "primary_archetype": "export_reorder_sellthrough_inventory_ASP_OPM_revision_bridge", "loop_objective": "priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | export_channel_reorder_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-15", "entry_date": "2024-02-15", "entry_price": 177400.0, "evidence_available_at_that_date": "K-food export channel reorder, overseas sell-through, distributor demand and OPM/revision bridge proxy after February base; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["export_reorder_proxy", "overseas_sellthrough_proxy", "channel_inventory_proxy", "ASP_mix_proxy", "OPM_revision_bridge_proxy"], "stage3_evidence_fields": ["positive_MFE30", "extreme_MFE90", "shallow_initial_MAE"], "stage4b_evidence_fields": ["later_K_food_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv", "profile_path": "atlas/symbol_profiles/003/003230.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 21.48, "MFE_90D_pct": 304.74, "MFE_180D_pct": 304.74, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -4.4, "MAE_90D_pct": -4.4, "MAE_180D_pct": -4.4, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-19", "peak_price": 718000.0, "drawdown_after_peak_pct": -32.31, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_K_food_export_valuation_4B_watch_needed", "four_b_evidence_type": ["export_reorder_margin_bridge", "sellthrough_inventory", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_K_food_export_reorder_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2003_CA", "same_entry_group_id": "R5L99_C18_003230_2024-02-15_177400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R5L99_C18_FNF_2024_STAGE2_FALSE_POSITIVE_APPAREL_EXPORT_CHANNEL_INVENTORY_WATCH", "case_id": "R5L99_C18_FNF_2024_APPAREL_EXPORT_CHANNEL_INVENTORY_FALSE_STAGE2", "symbol": "383220", "company_name": "F&F", "round": "R5", "loop": "99", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_APPAREL_CHANNEL_INVENTORY_FALSE_STAGE2_AND_SEAFOOD_K_FOOD_EVENT_CAP", "sector": "apparel_export_channel_inventory_reorder_watch", "primary_archetype": "apparel_export_watch_without_sellthrough_reorder_inventory_OPM_bridge", "loop_objective": "priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | export_channel_reorder_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-02", "entry_date": "2024-01-02", "entry_price": 87300.0, "evidence_available_at_that_date": "apparel export/channel recovery watch without confirmed sell-through recovery, reorder cadence, China/overseas channel inventory normalization, OPM or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["apparel_export_watch", "overseas_channel_theme", "old_premium"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["tiny_MFE90", "persistent_MAE90", "sellthrough_inventory_OPM_bridge_missing"], "stage4c_evidence_fields": ["channel_inventory_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv", "profile_path": "atlas/symbol_profiles/383/383220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.52, "MFE_90D_pct": 2.52, "MFE_180D_pct": 2.52, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -23.94, "MAE_90D_pct": -31.16, "MAE_180D_pct": -45.99, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-02", "peak_price": 89500.0, "drawdown_after_peak_pct": -47.32, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "apparel_export_channel_watch_was_false_stage2_due_missing_sellthrough_reorder_inventory_OPM_revision_bridge", "four_b_evidence_type": ["apparel_export_channel_premium", "bridge_missing", "tiny_MFE_high_MAE"], "four_c_protection_label": "channel_inventory_break_watch_only", "trigger_outcome_label": "bad_stage2_apparel_export_channel_watch_without_reorder_inventory_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_apparel_export_channel_watch_counts_without_sellthrough_reorder_inventory_OPM_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2022_CA", "same_entry_group_id": "R5L99_C18_383220_2024-01-02_87300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R5L99_C18_CJSEAFOOD_2024_STAGE4B_SEAFOOD_K_FOOD_EXPORT_EVENT_CAP", "case_id": "R5L99_C18_CJSEAFOOD_2024_SEAFOOD_K_FOOD_EXPORT_EVENT_CAP_4B", "symbol": "011150", "company_name": "CJ씨푸드", "round": "R5", "loop": "99", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_APPAREL_CHANNEL_INVENTORY_FALSE_STAGE2_AND_SEAFOOD_K_FOOD_EVENT_CAP", "sector": "seafood_K_food_export_event_premium", "primary_archetype": "seafood_K_food_export_event_cap_4B", "loop_objective": "priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | export_channel_reorder_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-06-14", "entry_date": "2024-06-14", "entry_price": 6320.0, "evidence_available_at_that_date": "seafood/K-food export event premium without confirmed repeat reorder, channel sell-through, inventory turn, ASP/mix, OPM or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["K_food_event", "seafood_export_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE30", "sellthrough_reorder_margin_bridge_recheck"], "stage4c_evidence_fields": ["channel_inventory_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011150/2024.csv", "profile_path": "atlas/symbol_profiles/011/011150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.69, "MFE_90D_pct": 2.69, "MFE_180D_pct": 2.69, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -33.86, "MAE_90D_pct": -33.86, "MAE_180D_pct": -33.86, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-17", "peak_price": 6490.0, "drawdown_after_peak_pct": -35.59, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.97, "four_b_full_window_peak_proximity": 0.97, "four_b_timing_verdict": "good_full_window_4B_timing_K_food_export_event_cap_due_missing_repeat_reorder_sellthrough_margin_bridge", "four_b_evidence_type": ["K_food_export_event_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "channel_inventory_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_K_food_export_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_K_food_export_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2002_CA", "same_entry_group_id": "R5L99_C18_011150_2024-06-14_6320", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R5L99_C18_SAMYANGFOODS_2024_K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE_POSITIVE", "trigger_id": "R5L99_C18_SAMYANGFOODS_2024_STAGE2_ACTIONABLE_K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE", "symbol": "003230", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 65, "customer_quality_score": 45, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 60, "margin_bridge_score": 70, "revision_score": 70, "relative_strength_score": 90, "customer_quality_score": 65, "policy_or_regulatory_score": 10, "valuation_repricing_score": 45, "execution_risk_score": 30, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "K_food_export_reorder_margin_positive", "MFE_90D_pct": 304.74, "MAE_90D_pct": -4.4, "score_return_alignment_label": "consumer_export_reorder_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R5L99_C18_FNF_2024_APPAREL_EXPORT_CHANNEL_INVENTORY_FALSE_STAGE2", "trigger_id": "R5L99_C18_FNF_2024_STAGE2_FALSE_POSITIVE_APPAREL_EXPORT_CHANNEL_INVENTORY_WATCH", "symbol": "383220", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 55, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 15, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "apparel_export_channel_inventory_false_stage2", "MFE_90D_pct": 2.52, "MAE_90D_pct": -31.16, "score_return_alignment_label": "apparel_channel_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_apparel_export_channel_watch_counts_without_sellthrough_reorder_inventory_OPM_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R5L99_C18_CJSEAFOOD_2024_SEAFOOD_K_FOOD_EXPORT_EVENT_CAP_4B", "trigger_id": "R5L99_C18_CJSEAFOOD_2024_STAGE4B_SEAFOOD_K_FOOD_EXPORT_EVENT_CAP", "symbol": "011150", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 75, "customer_quality_score": 20, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 65, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "K_food_export_event_cap_4B_guard", "MFE_90D_pct": 2.69, "MAE_90D_pct": -33.86, "score_return_alignment_label": "K_food_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_K_food_export_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": "99", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_REORDER_MARGIN_BRIDGE_VS_APPAREL_CHANNEL_INVENTORY_FALSE_STAGE2_AND_SEAFOOD_K_FOOD_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "export_channel_reorder_margin_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["consumer_export_reorder_positive", "apparel_channel_false_stage2", "K_food_event_cap_4B"], "loop_contribution_label": "priority1_canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied calibrated profile.

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
- C18 rows need explicit repeat reorder, overseas sell-through, channel inventory discipline, ASP/mix, OPM and revision bridge before positive promotion.
- In C18, bridge-missing consumer export channel rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C18 consumer export channel-reorder rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Selection State

```text
completed_round = R5
completed_loop = 99
completed_canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
coverage_scheduler_status = coverage_index_first
next_selection_rule = re-read V12_Research_No_Repeat_Index.md Priority 1 and local supplements
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.

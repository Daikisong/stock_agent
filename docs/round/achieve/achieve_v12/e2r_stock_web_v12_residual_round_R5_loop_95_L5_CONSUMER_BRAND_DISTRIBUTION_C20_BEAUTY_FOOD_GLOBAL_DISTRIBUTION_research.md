# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R5
scheduled_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = KBEAUTY_HOLDCO_CHANNEL_MARGIN_BRIDGE_VS_MASS_BEAUTY_SYMPATHY_FALSE_STAGE2_AND_COSMETICS_ODM_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R5_loop_95_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
```

This file is the corrected final output for this execution. The scheduler state after R4 loop 95 is R5 / loop 95. R5 is the L5 consumer/brand/distribution round, and this run fills C20 beauty/food global distribution rather than repeating the immediately preceding R5 loop 94 C18 export-channel file.

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
scheduled_loop = 95
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
round_sector_consistency = pass
computed_next_round = R6
computed_next_loop = 95
```

C20 is a channel-throughput and margin bridge archetype. A K-beauty or food-export label is the storefront sign; the cash register is overseas sell-through, distributor reorder, product mix, inventory normalization, ASP/mix, margin and revision.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION = 19 rows / 11 symbols / good-bad Stage2 8-2 / 4B-4C 4-0
top covered symbols include 226320(3), 161890(2), 192820(2), 214420(2), 241710(2), 439090(2)
previous R5 loop-89 C18 symbols avoided: 018290, 078520, 123690
previous R5 loop-90 C19 symbols avoided: 036620, 031430, 366030
previous R5 loop-91 C20 symbols avoided: 090430, 051900, 097950
previous R5 loop-92 C18 symbols avoided: 004370, 007310, 005610
previous R5 loop-93 C19 symbols avoided: 241590, 020000, 298540
previous R5 loop-94 C18 symbols avoided: 003230, 101530, 011150
previous R4 loop-95 C16 symbols avoided: 103140, 075970, 011810
```

Selected rows avoid hard duplicates and top repeated C20 symbols:

```text
002790 / Stage2-Actionable / 2024-04-01
027050 / Stage2-Actionable / 2024-05-24
003350 / Stage4B / 2024-09-03
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
| 002790 | atlas/symbol_profiles/002/002790.json | selected 2024 window clean after old CA/name-history candidates |
| 027050 | atlas/symbol_profiles/027/027050.json | no corporate-action candidate |
| 003350 | atlas/symbol_profiles/003/003350.json | selected 2024 window clean after old CA/name-history candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R5L95_C20_AMOREG_2024_KBEAUTY_HOLDCO_CHANNEL_MARGIN_POSITIVE | 002790 | 2024-04-01 | yes | 180 | yes | yes | true |
| R5L95_C20_COREANA_2024_MASS_BEAUTY_EXPORT_SYMPATHY_FALSE_STAGE2 | 027050 | 2024-05-24 | yes | 180 | yes | yes | true |
| R5L95_C20_HANKOOKCOSMETICSMFG_2024_COSMETICS_ODM_EXPORT_EVENT_CAP_4B | 003350 | 2024-09-03 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | KBEAUTY_HOLDCO_CHANNEL_MARGIN_BRIDGE | Positive Stage2 requires channel throughput, overseas sell-through, export mix, inventory normalization, margin and revision bridge. |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | MASS_BEAUTY_SYMPATHY_FALSE_STAGE2 | Mass-beauty export sympathy without reorder/channel and margin bridge can become false Stage2. |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | COSMETICS_ODM_EVENT_CAP_4B | Cosmetics ODM/K-beauty export event premium should route to 4B when customer/order/margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R5L95_C20_AMOREG_2024_KBEAUTY_HOLDCO_CHANNEL_MARGIN_POSITIVE | 002790 | 아모레퍼시픽홀딩스 | positive | K-beauty global channel recovery and margin bridge produced strong MFE with controlled MAE. |
| R5L95_C20_COREANA_2024_MASS_BEAUTY_EXPORT_SYMPATHY_FALSE_STAGE2 | 027050 | 코리아나 | counterexample | Export-sympathy spike lacked durable channel reorder and later drew down. |
| R5L95_C20_HANKOOKCOSMETICSMFG_2024_COSMETICS_ODM_EXPORT_EVENT_CAP_4B | 003350 | 한국화장품제조 | counterexample / 4B | ODM/K-beauty event premium capped near the September spike and later required 4B treatment. |

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
| AmoreG K-beauty holdco channel/margin bridge | historical public/report proxy | true | true | shadow-only positive |
| Coreana mass-beauty export false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Hankook Cosmetics Manufacturing ODM event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 002790 | atlas/ohlcv_tradable_by_symbol_year/002/002790/2024.csv | atlas/symbol_profiles/002/002790.json |
| 027050 | atlas/ohlcv_tradable_by_symbol_year/027/027050/2024.csv | atlas/symbol_profiles/027/027050.json |
| 003350 | atlas/ohlcv_tradable_by_symbol_year/003/003350/2024.csv | atlas/symbol_profiles/003/003350.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R5L95_C20_AMOREG_2024_STAGE2_ACTIONABLE_KBEAUTY_HOLDCO_CHANNEL_MARGIN_BRIDGE | 002790 | Stage2-Actionable | 2024-04-01 | 29250 | positive | K-beauty channel/margin bridge worked |
| R5L95_C20_COREANA_2024_STAGE2_FALSE_POSITIVE_MASS_BEAUTY_EXPORT_SYMPATHY | 027050 | Stage2-Actionable | 2024-05-24 | 3660 | counterexample | mass-beauty export sympathy false Stage2 |
| R5L95_C20_HANKOOKCOSMETICSMFG_2024_STAGE4B_COSMETICS_ODM_EXPORT_EVENT_CAP | 003350 | Stage4B | 2024-09-03 | 84400 | counterexample/4B | cosmetics ODM export event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R5L95_C20_AMOREG_2024_STAGE2_ACTIONABLE_KBEAUTY_HOLDCO_CHANNEL_MARGIN_BRIDGE | 29250 | 23.59 | -10.09 | 37.26 | -10.09 | 37.26 | -10.09 | 2024-05-31 | 40150 | -26.28 |
| R5L95_C20_COREANA_2024_STAGE2_FALSE_POSITIVE_MASS_BEAUTY_EXPORT_SYMPATHY | 3660 | 15.44 | -15.30 | 15.44 | -25.14 | 15.44 | -39.89 | 2024-05-24 | 4225 | -41.89 |
| R5L95_C20_HANKOOKCOSMETICSMFG_2024_STAGE4B_COSMETICS_ODM_EXPORT_EVENT_CAP | 84400 | 5.92 | -14.69 | 5.92 | -39.81 | 5.92 | -44.79 | 2024-09-03 | 89400 | -41.61 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C20 Stage2 needs channel throughput / export mix / sell-through / inventory normalization / margin / revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing K-beauty/cosmetics event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE beauty distribution rows cannot promote without durable channel/margin bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether beauty/food global distribution becomes sell-through, reorder and margin.

| symbol | stage quality | explanation |
|---|---|---|
| 002790 | good_stage2_with_later_watch | Global channel and margin bridge produced strong MFE with controlled MAE. |
| 027050 | bad_stage2 | Mass-beauty export-sympathy spike lacked channel reorder and later suffered high MAE. |
| 003350 | good_4B | Cosmetics ODM event premium capped around the September spike and then drew down sharply. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 027050 mass-beauty false Stage2 | 0.87 | 0.87 | false Stage2 due missing channel/reorder/margin bridge |
| 003350 cosmetics ODM cap | 0.94 | 0.94 | acceptable full-window 4B timing after September K-beauty export event spike |
| 002790 channel/margin bridge | n/a | n/a | positive Stage2, but later K-beauty holdco valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 027050 / 003350
```

No hard 4C candidate is proposed. R5 loop 95 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L5 beauty/food global distribution cases, Stage2 requires verified global channel throughput, distributor sell-through, reorder durability, export mix, inventory normalization, ASP/mix, margin, or revision bridge. K-beauty, cosmetics, food export, ODM, mass beauty, holdco, channel or distribution label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
rule = C20 should split true global-channel/reorder/margin positives from mass-beauty sympathy false Stage2 and cosmetics ODM event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 19.54 | -25.01 | 0.67 | mixed; C20 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 19.54 | -25.01 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L5 channel/reorder/margin bridge required | 2 | 26.35 | -17.62 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C20 bridge vs event-cap split | 2 | 26.35 | -17.62 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing K-beauty/global distribution themes as positive | 1 | 37.26 | -10.09 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 002790 channel/margin bridge | 66 | Stage2-Watch | 76 | Stage2-Actionable | 37.26 | -10.09 | Kbeauty_holdco_channel_margin_positive |
| 027050 mass-beauty false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 15.44 | -25.14 | mass_beauty_export_sympathy_false_stage2 |
| 003350 cosmetics ODM cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 5.92 | -39.81 | cosmetics_ODM_export_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "KBEAUTY_HOLDCO_CHANNEL_MARGIN_BRIDGE_VS_MASS_BEAUTY_SYMPATHY_FALSE_STAGE2_AND_COSMETICS_ODM_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C20 AmoreG K-beauty channel/margin positive, Coreana mass-beauty export-sympathy false Stage2, and Hankook Cosmetics Manufacturing ODM event-cap 4B split while avoiding top repeated C20 and previous R5/R4 loop symbols."}
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
residual_error_types_found: Kbeauty_holdco_channel_margin_positive, mass_beauty_export_sympathy_false_stage2, cosmetics_ODM_export_event_cap_4B
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
shadow_weight,stage2_required_bridge,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,configured,C20_requires_channel_throughput_export_mix_inventory_margin_revision_bridge,0,"C20 Stage2 should require global channel throughput, distributor sell-through, export mix, inventory normalization, ASP/mix, margin, or revision bridge, not K-beauty/food/global distribution label alone","AmoreG positive worked; Coreana and Hankook Cosmetics Manufacturing event/watch rows failed positive-stage promotion","R5L95_C20_AMOREG_2024_STAGE2_ACTIONABLE_KBEAUTY_HOLDCO_CHANNEL_MARGIN_BRIDGE|R5L95_C20_COREANA_2024_STAGE2_FALSE_POSITIVE_MASS_BEAUTY_EXPORT_SYMPATHY|R5L95_C20_HANKOOKCOSMETICSMFG_2024_STAGE4B_COSMETICS_ODM_EXPORT_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,configured,cap_bridge_missing_Kbeauty_cosmetics_export_event_premiums_as_4B_watch,0,"K-beauty/cosmetics ODM event premiums can peak before channel reorder and margin bridge is proven","Coreana had temporary MFE then high MAE; Hankook Cosmetics Manufacturing showed event-cap behavior after September K-beauty spike","R5L95_C20_COREANA_2024_STAGE2_FALSE_POSITIVE_MASS_BEAUTY_EXPORT_SYMPATHY|R5L95_C20_HANKOOKCOSMETICSMFG_2024_STAGE4B_COSMETICS_ODM_EXPORT_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,configured,block_positive_stage_when_beauty_distribution_theme_has_high_or_persistent_MAE_without_channel_margin_bridge,0,"High or persistent MAE after bridge-missing C20 entries should block Stage2/Stage3 promotion unless sell-through, reorder, inventory and margin evidence survives","Coreana MAE90=-25.14 and Hankook Cosmetics Manufacturing MAE90=-39.81","R5L95_C20_COREANA_2024_STAGE2_FALSE_POSITIVE_MASS_BEAUTY_EXPORT_SYMPATHY|R5L95_C20_HANKOOKCOSMETICSMFG_2024_STAGE4B_COSMETICS_ODM_EXPORT_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R5L95_C20_AMOREG_2024_KBEAUTY_HOLDCO_CHANNEL_MARGIN_POSITIVE", "symbol": "002790", "company_name": "아모레퍼시픽홀딩스", "round": "R5", "loop": "95", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "KBEAUTY_HOLDCO_CHANNEL_MARGIN_BRIDGE_VS_MASS_BEAUTY_SYMPATHY_FALSE_STAGE2_AND_COSMETICS_ODM_EVENT_CAP", "case_type": "structural_success_with_later_Kbeauty_holdco_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R5L95_C20_AMOREG_2024_STAGE2_ACTIONABLE_KBEAUTY_HOLDCO_CHANNEL_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "K-beauty global channel recovery, brand portfolio value, overseas sell-through and margin/revision bridge produced strong 30D/90D/180D MFE with controlled early MAE. C20 works when beauty/food global distribution narrative maps into channel throughput, export mix, inventory normalization, ASP/mix, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C20_positive_requires_channel_throughput_export_mix_inventory_margin_revision_bridge_not_Kbeauty_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old corporate-action/name-history candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R5L95_C20_COREANA_2024_MASS_BEAUTY_EXPORT_SYMPATHY_FALSE_STAGE2", "symbol": "027050", "company_name": "코리아나", "round": "R5", "loop": "95", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "KBEAUTY_HOLDCO_CHANNEL_MARGIN_BRIDGE_VS_MASS_BEAUTY_SYMPATHY_FALSE_STAGE2_AND_COSMETICS_ODM_EVENT_CAP", "case_type": "failed_rerating_mass_beauty_channel_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R5L95_C20_COREANA_2024_STAGE2_FALSE_POSITIVE_MASS_BEAUTY_EXPORT_SYMPATHY", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Mass-beauty / K-beauty export sympathy had an event rebound but did not prove durable channel throughput or margin revision. C20 Stage2 should not be awarded without verified overseas distributor sell-through, reorder durability, product mix, inventory normalization, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_mass_beauty_export_sympathy_counts_without_channel_reorder_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
{"row_type": "case", "case_id": "R5L95_C20_HANKOOKCOSMETICSMFG_2024_COSMETICS_ODM_EXPORT_EVENT_CAP_4B", "symbol": "003350", "company_name": "한국화장품제조", "round": "R5", "loop": "95", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "KBEAUTY_HOLDCO_CHANNEL_MARGIN_BRIDGE_VS_MASS_BEAUTY_SYMPATHY_FALSE_STAGE2_AND_COSMETICS_ODM_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R5L95_C20_HANKOOKCOSMETICSMFG_2024_STAGE4B_COSMETICS_ODM_EXPORT_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Cosmetics ODM / K-beauty export event premium capped near the September spike and then required 4B treatment. C20 should route bridge-missing cosmetics ODM event premiums to 4B unless customer reorder, channel throughput, inventory normalization, ASP/mix, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_cosmetics_ODM_export_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old corporate-action/name-history candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R5L95_C20_AMOREG_2024_STAGE2_ACTIONABLE_KBEAUTY_HOLDCO_CHANNEL_MARGIN_BRIDGE", "case_id": "R5L95_C20_AMOREG_2024_KBEAUTY_HOLDCO_CHANNEL_MARGIN_POSITIVE", "symbol": "002790", "company_name": "아모레퍼시픽홀딩스", "round": "R5", "loop": "95", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "KBEAUTY_HOLDCO_CHANNEL_MARGIN_BRIDGE_VS_MASS_BEAUTY_SYMPATHY_FALSE_STAGE2_AND_COSMETICS_ODM_EVENT_CAP", "sector": "K_beauty_global_channel_brand_portfolio_margin", "primary_archetype": "channel_throughput_export_mix_inventory_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-01", "entry_date": "2024-04-01", "entry_price": 29250.0, "evidence_available_at_that_date": "K-beauty global channel recovery, overseas sell-through, brand-portfolio value, inventory normalization and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["global_channel_recovery_proxy", "overseas_sellthrough_proxy", "inventory_normalization_proxy", "ASP_mix_bridge_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "strong_MFE90", "strong_MFE180", "controlled_initial_MAE"], "stage4b_evidence_fields": ["later_Kbeauty_holdco_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002790/2024.csv", "profile_path": "atlas/symbol_profiles/002/002790.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 23.59, "MFE_90D_pct": 37.26, "MFE_180D_pct": 37.26, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -10.09, "MAE_90D_pct": -10.09, "MAE_180D_pct": -10.09, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-31", "peak_price": 40150.0, "drawdown_after_peak_pct": -26.28, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_Kbeauty_holdco_valuation_4B_watch_needed", "four_b_evidence_type": ["global_channel_bridge", "margin_revision", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_Kbeauty_holdco_channel_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_CA_name_history_candidates", "same_entry_group_id": "R5L95_C20_002790_2024-04-01_29250", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R5L95_C20_COREANA_2024_STAGE2_FALSE_POSITIVE_MASS_BEAUTY_EXPORT_SYMPATHY", "case_id": "R5L95_C20_COREANA_2024_MASS_BEAUTY_EXPORT_SYMPATHY_FALSE_STAGE2", "symbol": "027050", "company_name": "코리아나", "round": "R5", "loop": "95", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "KBEAUTY_HOLDCO_CHANNEL_MARGIN_BRIDGE_VS_MASS_BEAUTY_SYMPATHY_FALSE_STAGE2_AND_COSMETICS_ODM_EVENT_CAP", "sector": "mass_beauty_Kbeauty_export_sympathy_watch", "primary_archetype": "mass_beauty_export_sympathy_without_channel_reorder_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-24", "entry_date": "2024-05-24", "entry_price": 3660.0, "evidence_available_at_that_date": "mass-beauty/K-beauty export sympathy and channel rebound watch without confirmed distributor sell-through, reorder durability or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["Kbeauty_export_sympathy", "mass_beauty_channel_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["temporary_MFE", "channel_reorder_margin_bridge_missing", "post_event_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/027/027050/2024.csv", "profile_path": "atlas/symbol_profiles/027/027050.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 15.44, "MFE_90D_pct": 15.44, "MFE_180D_pct": 15.44, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -15.3, "MAE_90D_pct": -25.14, "MAE_180D_pct": -39.89, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-24", "peak_price": 4225.0, "drawdown_after_peak_pct": -41.89, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.87, "four_b_full_window_peak_proximity": 0.87, "four_b_timing_verdict": "mass_beauty_export_sympathy_was_false_stage2_due_missing_channel_reorder_margin_bridge", "four_b_evidence_type": ["Kbeauty_sympathy_premium", "bridge_missing", "temporary_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_mass_beauty_export_sympathy_without_channel_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_mass_beauty_export_sympathy_counts_without_channel_reorder_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R5L95_C20_027050_2024-05-24_3660", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R5L95_C20_HANKOOKCOSMETICSMFG_2024_STAGE4B_COSMETICS_ODM_EXPORT_EVENT_CAP", "case_id": "R5L95_C20_HANKOOKCOSMETICSMFG_2024_COSMETICS_ODM_EXPORT_EVENT_CAP_4B", "symbol": "003350", "company_name": "한국화장품제조", "round": "R5", "loop": "95", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "KBEAUTY_HOLDCO_CHANNEL_MARGIN_BRIDGE_VS_MASS_BEAUTY_SYMPATHY_FALSE_STAGE2_AND_COSMETICS_ODM_EVENT_CAP", "sector": "cosmetics_ODM_Kbeauty_export_event_premium", "primary_archetype": "cosmetics_ODM_export_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-09-03", "entry_date": "2024-09-03", "entry_price": 84400.0, "evidence_available_at_that_date": "cosmetics ODM / K-beauty export event premium after late-summer spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["cosmetics_ODM_event", "Kbeauty_export_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "MAE_recheck", "channel_order_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003350/2024.csv", "profile_path": "atlas/symbol_profiles/003/003350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.92, "MFE_90D_pct": 5.92, "MFE_180D_pct": 5.92, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -14.69, "MAE_90D_pct": -39.81, "MAE_180D_pct": -44.79, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-09-03", "peak_price": 89400.0, "drawdown_after_peak_pct": -41.61, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "acceptable_full_window_4B_timing_cosmetics_ODM_export_event_cap", "four_b_evidence_type": ["cosmetics_ODM_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_cosmetics_ODM_export_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_cosmetics_ODM_export_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_CA_name_history_candidates", "same_entry_group_id": "R5L95_C20_003350_2024-09-03_84400", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L95_C20_AMOREG_2024_KBEAUTY_HOLDCO_CHANNEL_MARGIN_POSITIVE", "trigger_id": "R5L95_C20_AMOREG_2024_STAGE2_ACTIONABLE_KBEAUTY_HOLDCO_CHANNEL_MARGIN_BRIDGE", "symbol": "002790", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 25, "backlog_visibility_score": 55, "margin_bridge_score": 55, "revision_score": 55, "relative_strength_score": 70, "customer_quality_score": 50, "policy_or_regulatory_score": 5, "valuation_repricing_score": 50, "execution_risk_score": 35, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "Kbeauty_holdco_channel_margin_positive", "MFE_90D_pct": 37.26, "MAE_90D_pct": -10.09, "score_return_alignment_label": "Kbeauty_holdco_channel_margin_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L95_C20_COREANA_2024_MASS_BEAUTY_EXPORT_SYMPATHY_FALSE_STAGE2", "trigger_id": "R5L95_C20_COREANA_2024_STAGE2_FALSE_POSITIVE_MASS_BEAUTY_EXPORT_SYMPATHY", "symbol": "027050", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "mass_beauty_export_sympathy_false_stage2", "MFE_90D_pct": 15.44, "MAE_90D_pct": -25.14, "score_return_alignment_label": "mass_beauty_export_sympathy_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_mass_beauty_export_sympathy_counts_without_channel_reorder_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L95_C20_HANKOOKCOSMETICSMFG_2024_COSMETICS_ODM_EXPORT_EVENT_CAP_4B", "trigger_id": "R5L95_C20_HANKOOKCOSMETICSMFG_2024_STAGE4B_COSMETICS_ODM_EXPORT_EVENT_CAP", "symbol": "003350", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "cosmetics_ODM_export_event_cap_4B_guard", "MFE_90D_pct": 5.92, "MAE_90D_pct": -39.81, "score_return_alignment_label": "cosmetics_ODM_export_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_cosmetics_ODM_export_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": "95", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "KBEAUTY_HOLDCO_CHANNEL_MARGIN_BRIDGE_VS_MASS_BEAUTY_SYMPATHY_FALSE_STAGE2_AND_COSMETICS_ODM_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["Kbeauty_holdco_channel_margin_positive", "mass_beauty_export_sympathy_false_stage2", "cosmetics_ODM_export_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
- C20 rows need explicit global channel throughput, distributor sell-through, reorder durability, export mix, inventory normalization, ASP/mix, margin or revision bridge before positive promotion.
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
10. Add tests that bridge-missing C20 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R5
completed_loop = 95
next_round = R6
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.

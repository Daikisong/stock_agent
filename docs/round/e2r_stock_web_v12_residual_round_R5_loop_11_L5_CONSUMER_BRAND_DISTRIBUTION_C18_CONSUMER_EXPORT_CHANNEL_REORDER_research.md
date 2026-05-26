# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R5
loop = 11
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = K_FOOD_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF
selection_mode = auto_coverage_gap_fill
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
```

This MD is historical calibration research only. It is not a live stock screen, not an investment recommendation, and not a repository implementation patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The goal of this loop is not to re-prove the global Stage2 bonus or Green lateness axis. The residual question is narrower: in R5 consumer names, when does a food-export / overseas-channel narrative become a repeat-order margin bridge, and when is it merely a K-food theme spike that should be treated as a 4B overlay or blocked from positive promotion?

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R5 |
| loop | 11 |
| large_sector_id | L5_CONSUMER_BRAND_DISTRIBUTION |
| canonical_archetype_id | C18_CONSUMER_EXPORT_CHANNEL_REORDER |
| fine_archetype_id | K_FOOD_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF |
| loop_objective | sector_specific_rule_discovery; canonical_archetype_compression; counterexample_mining; 4B_non_price_requirement_stress_test; green_strictness_stress_test |
| preferred_rule_scope | canonical_archetype_specific |

## 3. Previous Coverage / Duplicate Avoidance Check

Only allowed research artifacts were consulted for coverage context. No `src/e2r` code was opened.

Existing calibration ingest coverage already spans all R1~R13 rounds and loops 1~9, with 107 parsed calibration documents, 1,940 validated trigger rows, and 1,376 aggregate representative rows. The applied profile already moved Stage2, Yellow, Green, and 4B/4C global guardrail axes, so this loop avoids re-proposing those as global rules.

Repository search for `C18_CONSUMER_EXPORT_CHANNEL_REORDER` returned no direct prior artifact hit in the accessible search layer, so this loop treats C18 as a coverage-gap fill inside R5 rather than a duplicate of the immediately preceding C20 beauty-distribution loop.

Duplicate avoidance result:

```text
auto_selected_coverage_gap = R5/L5 C18 food-export channel reorder vs price-only theme blowoff
same_symbol_same_trigger_reuse = none
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest validation:

| field | value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |
| inactive_or_delisted_like_symbol_count | 2,546 |
| markets | KONEX; KOSDAQ; KOSDAQ GLOBAL; KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Schema validation:

```text
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
raw_shard_columns = d,o,h,l,c,v,a,mc,s,m,rs
calibration_basis = tradable_raw
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

All representative triggers below satisfy the 180-trading-day historical gate using Stock-Web manifest max date `2026-02-20`. None of the selected 2023~2025 windows overlap the corporate-action candidate dates listed in the symbol profiles.

| symbol | company | profile_path | profile last_date | corporate-action candidate dates | 180D status |
|---|---|---|---:|---|---|
| 003230 | 삼양식품 | atlas/symbol_profiles/003/003230.json | 2026-02-20 | 2003-07-25 | clean_180D_window |
| 005180 | 빙그레 | atlas/symbol_profiles/005/005180.json | 2026-02-20 | 1995-09-29; 1996-09-25; 1998-12-15 | clean_180D_window |
| 004370 | 농심 | atlas/symbol_profiles/004/004370.json | 2026-02-20 | 1997-05-08; 1997-07-21; 2000-07-28; 2003-07-18 | clean_180D_window |
| 097950 | CJ제일제당 | atlas/symbol_profiles/097/097950.json | 2026-02-20 | none | clean_180D_window |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine_archetype_id | compression note |
|---|---|---|
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | K_FOOD_GLOBAL_CHANNEL_REORDER | Repeat order / export mix / overseas channel evidence that closes into earnings and margin bridge. |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | K_FOOD_THEME_PRICE_BLOWOFF | K-food or global brand narrative where price moves faster than confirmed reorder and margin evidence. |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | K_FOOD_CONGLOMERATE_DILUTION | Overseas food evidence diluted by conglomerate/commodity/logistics segments; weak pure-play rerating. |

The proposed rule compresses these into one canonical C18 decision: promotion requires channel reorder evidence plus margin/revision closure. Price-only global food theme is not enough.

## 7. Case Selection Summary

| case_id | symbol | company | role | positive_or_counterexample | best_trigger | reason selected |
|---|---:|---|---|---|---|---|
| R5L11-C18-001 | 003230 | 삼양식품 | structural_success | positive | R5L11-C18-001-S2A-2023-11-15 | Early export/brand evidence later closed into a major 2024 earnings rerating. |
| R5L11-C18-002 | 005180 | 빙그레 | high_mae_success | positive | R5L11-C18-002-S2A-2024-05-17 | Overseas/seasonal channel evidence produced a sharp rerating, but drawdown shows the need for 4B overlay. |
| R5L11-C18-003 | 004370 | 농심 | price_moved_without_evidence | counterexample | R5L11-C18-003-S2A-2024-05-17 | Theme-driven K-food move produced high MFE but later failed durability without a Samyang-like margin bridge. |
| R5L11-C18-004 | 097950 | CJ제일제당 | failed_rerating | counterexample | R5L11-C18-004-S2A-2024-05-17 | Overseas food narrative diluted by conglomerate structure and weak pure-play channel-to-margin conversion. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 4
4C_case_count = 0
calibration_usable_case_count = 4
new_independent_case_count = 4
minimum_new_independent_case_ratio = 1.00
```

The useful contrast is not “food exports good / not good.” It is more like a pipe system. The export order is the water pressure, but the rerating appears only if the pipe is narrow, clean, and connected to the margin tank. A pure-play, repeat-order channel can fill earnings quickly; a broad conglomerate pipe leaks through unrelated divisions; a theme-only pipe makes noise at the valve but does not refill the tank.

## 9. Evidence Source Map

| case_id | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|
| R5L11-C18-001 | Public earnings / export mix / brand demand evidence by 2023-11-14~15 | 2024 revision/margin bridge visible after confirmed earnings | valuation_blowoff; positioning_overheat around 2024-06 peak | none |
| R5L11-C18-002 | Public earnings / overseas ice-cream distribution evidence by 2024-05-16~17 | margin/revision partial; seasonality remains | price-only local peak; valuation_blowoff around 2024-06 | none |
| R5L11-C18-003 | K-food / overseas ramen narrative and Q1 earnings around 2024-05-16~17 | revision quality less durable than price move | price-only local peak around 2024-06 | none |
| R5L11-C18-004 | overseas food / Bibigo narrative and Q1 result window around 2024-05-16~17 | weak pure-play revision closure | conglomerate dilution; margin bridge slowdown | none |

Evidence timing rule applied: when disclosure timing was ambiguous or after close, entry_date is the next Stock-Web tradable close.

## 10. Price Data Source Map

| symbol | entry_year_shard | profile_path | stock_web_manifest_max_date | price_basis |
|---:|---|---|---|---|
| 003230 | atlas/ohlcv_tradable_by_symbol_year/003/003230/2023.csv | atlas/symbol_profiles/003/003230.json | 2026-02-20 | tradable_raw |
| 005180 | atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv | atlas/symbol_profiles/005/005180.json | 2026-02-20 | tradable_raw |
| 004370 | atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv | atlas/symbol_profiles/004/004370.json | 2026-02-20 | tradable_raw |
| 097950 | atlas/ohlcv_tradable_by_symbol_year/097/097950/2024.csv | atlas/symbol_profiles/097/097950.json | 2026-02-20 | tradable_raw |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | company | trigger_type | trigger_date | entry_date | entry_price | stage2 fields | stage3 fields | 4B fields | current_profile_verdict |
|---|---|---:|---|---|---|---|---:|---|---|---|---|
| R5L11-C18-001-S2A-2023-11-15 | R5L11-C18-001 | 003230 | 삼양식품 | Stage2-Actionable | 2023-11-14 | 2023-11-15 | 199600 | public_event_or_disclosure; customer_or_order_quality; capacity_or_volume_route; early_revision_signal | later confirmed_revision; margin_bridge | none | current_profile_correct |
| R5L11-C18-001-4B-2024-06-18 | R5L11-C18-001 | 003230 | 삼양식품 | Stage4B | 2024-06-18 | 2024-06-18 | 712000 | none | none | valuation_blowoff; positioning_overheat | current_profile_4B_correct_overlay |
| R5L11-C18-002-S2A-2024-05-17 | R5L11-C18-002 | 005180 | 빙그레 | Stage2-Actionable | 2024-05-16 | 2024-05-17 | 88300 | public_event_or_disclosure; customer_or_order_quality; early_revision_signal | margin_bridge_partial | none | current_profile_too_early_if_green |
| R5L11-C18-002-4B-2024-06-10 | R5L11-C18-002 | 005180 | 빙그레 | Stage4B | 2024-06-10 | 2024-06-10 | 112100 | none | none | price_only_local_peak; valuation_blowoff | current_profile_4B_correct_overlay |
| R5L11-C18-003-S2A-2024-05-17 | R5L11-C18-003 | 004370 | 농심 | Stage2-Actionable | 2024-05-16 | 2024-05-17 | 399000 | public_event_or_disclosure; relative_strength; theme_channel_narrative | weak_confirmed_revision | price_only_local_peak | current_profile_false_positive_if_promoted_green |
| R5L11-C18-003-4B-2024-06-13 | R5L11-C18-003 | 004370 | 농심 | Stage4B | 2024-06-13 | 2024-06-13 | 547000 | none | none | price_only; valuation_blowoff | current_profile_4B_correct_overlay |
| R5L11-C18-004-S2A-2024-05-17 | R5L11-C18-004 | 097950 | CJ제일제당 | Stage2-Actionable | 2024-05-16 | 2024-05-17 | 333500 | public_event_or_disclosure; overseas_food_narrative | weak_margin_bridge; conglomerate_dilution | margin_or_backlog_slowdown | current_profile_false_positive_if_promoted_yellow |

## 12. Trigger-Level OHLC Backtest Tables

Representative trigger rows are deduped for aggregate. 4B rows are overlay-only and do not train positive entry weights.

| trigger_id | symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | calibration_usable |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| R5L11-C18-001-S2A-2023-11-15 | 003230 | 2023-11-15 | 199600 | 16.98 | -5.11 | 19.99 | -15.13 | 259.72 | -15.13 | 2024-06-19 | 718000 | -20.19 | true |
| R5L11-C18-002-S2A-2024-05-17 | 005180 | 2024-05-17 | 88300 | 34.09 | -9.29 | 34.09 | -32.96 | 34.09 | -32.96 | 2024-06-11 | 118400 | -50.00 | true |
| R5L11-C18-003-S2A-2024-05-17 | 004370 | 2024-05-17 | 399000 | 50.13 | -1.75 | 50.13 | -9.65 | 50.13 | -20.55 | 2024-06-13 | 599000 | -47.08 | true |
| R5L11-C18-004-S2A-2024-05-17 | 097950 | 2024-05-17 | 333500 | 22.19 | -0.30 | 22.19 | -10.04 | 22.19 | -28.34 | 2024-06-26 | 407500 | -41.35 | true |

Calculation notes:

- 003230 entry row: 2023-11-15 close 199,600; 180D peak high 718,000 on 2024-06-19; 90D low 169,400 on 2024-02-01.
- 005180 entry row: 2024-05-17 close 88,300; local/full 180D peak high 118,400 on 2024-06-11; post-peak low 59,200 on 2024-09-09.
- 004370 entry row: 2024-05-17 close 399,000; peak high 599,000 on 2024-06-13; 180D low 317,000 on 2024-11-15.
- 097950 entry row: 2024-05-17 close 333,500; peak high 407,500 on 2024-06-26; 180D low 239,000 on 2024-11-15.

## 13. Current Calibrated Profile Stress Test

| case_id | current calibrated profile likely decision | actual price alignment | verdict |
|---|---|---|---|
| R5L11-C18-001 | Stage2-Actionable / later Green only after revision | Strongly aligned; early channel evidence captured a structural rerating before Green confirmation | current_profile_correct |
| R5L11-C18-002 | Stage2-Actionable or Yellow; Green should be cautious due seasonality | Early upside worked, but high MAE and -50% post-peak drawdown require 4B overlay | current_profile_too_early_if_green |
| R5L11-C18-003 | Could be over-promoted if relative strength/theme is treated as channel proof | High local MFE but weak durability; price-only blowoff should not train positive weights | current_profile_false_positive_if_promoted_green |
| R5L11-C18-004 | Could be Yellow on brand/export narrative | MFE modest and 180D MAE severe; conglomerate dilution blocks pure C18 promotion | current_profile_false_positive_if_promoted_yellow |

Axis stress answers:

1. Stage2 bonus is useful for 003230 and 005180, but dangerous for 004370/097950 unless channel quality is explicit.
2. Yellow threshold 75 is acceptable only when margin/revision closure exists. Theme-only C18 should be pushed below Yellow.
3. Green threshold 87 and revision 55 remain necessary; this loop strengthens, not weakens, Green strictness for C18.
4. Price-only blowoff guard is strengthened: 004370 and 005180 show local spikes that should be overlay/risk rows, not positive entries.
5. Full 4B non-price requirement is kept. Price-only local peaks are usable for overlay timing but not as full thesis-exit unless paired with non-price fatigue.
6. Hard 4C routing not tested; no thesis-break cancellation or accounting/trust break was used.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2-Actionable entry | hypothetical Green entry | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| R5L11-C18-001 | 199600 | 343500 on 2024-05-16 revision confirmation proxy | 0.277 | Green not fatally late, but Stage2 captured much more upside. |
| R5L11-C18-002 | 88300 | not_applicable | not_applicable | No durable Green trigger; keep as Stage2/Yellow with 4B overlay. |
| R5L11-C18-003 | 399000 | not_applicable | not_applicable | Price peak without durable Green evidence; do not invent Green after outcome. |
| R5L11-C18-004 | 333500 | not_applicable | not_applicable | Weak margin/revision closure; Green should remain blocked. |

Formula for 003230:

```text
green_lateness_ratio = (343500 - 199600) / (718000 - 199600) = 0.277
```

## 15. 4B Local vs Full-window Timing Audit

| case_id | Stage2 entry | 4B proxy date | 4B entry_price | local_peak_price | full_window_peak_price | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---|---:|---|---:|---:|---:|---:|---:|---|
| R5L11-C18-001 | 199600 | 2024-06-18 | 712000 | 718000 | 718000 | 0.988 | 0.988 | good_full_window_4B_timing; non-price confirmation still preferred |
| R5L11-C18-002 | 88300 | 2024-06-10 | 112100 | 118400 | 118400 | 0.791 | 0.791 | price_only_local_4B_overlay_useful |
| R5L11-C18-003 | 399000 | 2024-06-13 | 547000 | 599000 | 599000 | 0.740 | 0.740 | price_only_theme_4B_overlay; not positive training |
| R5L11-C18-004 | 333500 | 2024-06-26 | 398000 | 407500 | 407500 | 0.872 | 0.872 | modest rerating then failure; use as guard evidence |

## 16. 4C Protection Audit

No hard 4C thesis-break row is proposed in this loop. The downside paths are 4B overlay / guard evidence, not contract cancellation, regulatory rejection, accounting trust break, or forced liquidation.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_success = not_tested
hard_4c_late = not_tested
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = C18_channel_reorder_quality_gate
direction = positive promotion requires channel reorder + margin/revision bridge
proposal_type = archetype_shadow_only
production_scoring_changed = false
```

Rule candidate:

```text
For C18_CONSUMER_EXPORT_CHANNEL_REORDER:
  If evidence is only brand/theme/relative-strength, cap positive promotion at Stage2-watch / low Yellow.
  Promote to Stage2-Actionable or Yellow only when at least two of the following are present:
    - repeat-order or overseas channel data,
    - export/customer mix improvement,
    - confirmed margin bridge,
    - early or confirmed earnings revision,
    - pure-play exposure rather than conglomerate dilution.
  Green requires confirmed_revision + margin_bridge; price momentum cannot substitute.
```

## 18. Canonical-Archetype Rule Candidate

C18 is not simply a consumer export label. It has two internal gears:

1. **Reorder gear**: repeat demand, channel expansion, export mix, and margin bridge mesh together. This produced the 003230 path.
2. **Theme gear**: price sees the story before earnings quality arrives. This produced the 004370 and 097950 guard cases, and the 005180 high-MAE success case.

The shadow rule should reward the first gear and quarantine the second as 4B overlay / watch-only until revision evidence arrives.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | profile_hypothesis | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | global current | Existing global guardrails; no C18-specific channel-quality gate | 4 | 4 | 31.60 | -16.95 | 91.53 | -24.25 | 0.50 | 0 | 1 | mixed; too permissive for theme-only C18 |
| P0b_e2r_2_0_baseline_reference | global baseline | Earlier looser Green / no full calibrated guardrails | 4 | 4 | 31.60 | -16.95 | 91.53 | -24.25 | 0.75 | 0 | 0 | weak; likely over-promotes price/theme evidence |
| P1_L5_sector_candidate_profile | sector_specific | R5 export names need channel + margin bridge | 4 | 3 | 34.74 | -19.25 | 114.65 | -22.88 | 0.33 | 0 | 1 | better but still broad |
| P2_C18_archetype_candidate_profile | canonical_archetype_specific | C18 promotion requires reorder quality and pure-play margin bridge | 4 | 2 | 27.04 | -24.05 | 146.91 | -24.05 | 0.00 | 0 | 1 | best explanatory alignment; accepts positive cases and blocks guard cases |
| P3_counterexample_guard_profile | canonical_archetype_specific | Theme-only / conglomerate-diluted C18 capped below positive promotion | 4 | 2 positive + 2 guard | 27.04 positive-only | -24.05 positive-only | 146.91 positive-only | -24.05 positive-only | 0.00 | 0 | 1 | recommended as shadow guard, not production |

## 20. Score-Return Alignment Matrix

| case_id | P0 stage | P0 weighted proxy | proposed P2 stage | P2 weighted proxy | MFE_90D_pct | MAE_90D_pct | alignment label |
|---|---|---:|---|---:|---:|---:|---|
| R5L11-C18-001 | Stage2-Actionable | 84 | Stage2-Actionable / later Green candidate | 88 | 19.99 | -15.13 | aligned_structural_success |
| R5L11-C18-002 | Stage3-Yellow | 78 | Stage2-Actionable with 4B overlay | 80 | 34.09 | -32.96 | aligned_but_high_mae |
| R5L11-C18-003 | Stage3-Yellow risk | 79 | Stage2-watch / 4B overlay only | 68 | 50.13 | -9.65 | price_moved_without_durable_evidence |
| R5L11-C18-004 | Stage3-Yellow risk | 76 | narrative_only / Stage2-watch | 65 | 22.19 | -10.04 | failed_rerating_guard |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C18_CONSUMER_EXPORT_CHANNEL_REORDER | K_FOOD_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF | 2 | 2 | 4 | 0 | 4 | 0 | 7 | 4 | 2 | true | true | Needs future holdout: non-food C18 export-channel reorder and 2025 C18 cases |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
positive_case_count: 2
counterexample_count: 2
current_profile_error_count: 2
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - theme_only_channel_narrative_false_positive
  - conglomerate_dilution_blocks_pure_c18_rerating
  - high_mae_success_requires_4b_overlay
new_axis_proposed:
  - C18_channel_reorder_quality_gate
  - C18_conglomerate_dilution_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
diversity_score_summary: new_symbol=4; new_trigger_family=4; counterexample=2; positive=2; reused=0; duplicate_penalty=0
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest and schema were checked.
- Symbol profile files were checked for all four symbols.
- Actual Stock-Web tradable OHLC rows were used for entry price, high/low windows, MFE/MAE, peak and drawdown.
- 180D forward windows are available and clean for selected triggers.
- Same-entry dedupe was applied: representative trigger rows only are aggregated.
```

Not validated:

```text
- No stock_agent production code was opened.
- No live scan was run.
- No current 2026 candidate list was generated.
- No brokerage or auto-trading workflow was touched.
- Evidence timestamps are treated at public-result-window granularity; precise intraday disclosure timestamps are not used for same-day entries.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C18_channel_reorder_quality_gate,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"C18 needs repeat-order/channel evidence plus margin/revision bridge; theme-only evidence created false-positive risk.","Blocks 004370/097950 positive promotion while keeping 003230/005180 as actionable or overlay cases.","R5L11-C18-001-S2A-2023-11-15|R5L11-C18-002-S2A-2024-05-17|R5L11-C18-003-S2A-2024-05-17|R5L11-C18-004-S2A-2024-05-17",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C18_conglomerate_dilution_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"Overseas food narrative inside conglomerate structure did not behave like pure-play channel reorder.","097950 MFE_180 only 22.19 with MAE_180 -28.34; cap below Yellow unless pure segment margin bridge is explicit.","R5L11-C18-004-S2A-2024-05-17",1,1,1,low,canonical_shadow_only,"needs more holdout cases"
shadow_weight,C18_price_only_theme_4b_overlay,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"Price-only K-food spike can produce local MFE but later drawdown; use as overlay not positive training.","004370 and 005180 both show local peak proximity useful for 4B timing but not full 4B without non-price fatigue.","R5L11-C18-002-4B-2024-06-10|R5L11-C18-003-4B-2024-06-13",2,2,1,medium,canonical_shadow_only,"strengthens existing 4B guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R5L11-C18-001","symbol":"003230","company_name":"삼양식품","round":"R5","loop":"11","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R5L11-C18-001-S2A-2023-11-15","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_structural_success","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Pure-play export/channel evidence later closed into a 2024 earnings rerating."}
{"row_type":"case","case_id":"R5L11-C18-002","symbol":"005180","company_name":"빙그레","round":"R5","loop":"11","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R5L11-C18-002-S2A-2024-05-17","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_but_high_mae","current_profile_verdict":"current_profile_too_early_if_green","price_source":"Songdaiki/stock-web","notes":"Channel/export evidence produced a local rerating but required 4B overlay due drawdown."}
{"row_type":"case","case_id":"R5L11-C18-003","symbol":"004370","company_name":"농심","round":"R5","loop":"11","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"R5L11-C18-003-S2A-2024-05-17","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"price_moved_without_durable_evidence","current_profile_verdict":"current_profile_false_positive_if_promoted_green","price_source":"Songdaiki/stock-web","notes":"Theme/relative-strength evidence created local MFE but weak durability; useful as guard case."}
{"row_type":"case","case_id":"R5L11-C18-004","symbol":"097950","company_name":"CJ제일제당","round":"R5","loop":"11","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R5L11-C18-004-S2A-2024-05-17","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"failed_rerating_guard","current_profile_verdict":"current_profile_false_positive_if_promoted_yellow","price_source":"Songdaiki/stock-web","notes":"Overseas food narrative diluted by conglomerate structure; weak 180D alignment."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R5L11-C18-001-S2A-2023-11-15","case_id":"R5L11-C18-001","symbol":"003230","company_name":"삼양식품","round":"R5","loop":"11","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF","sector":"소비재·유통·브랜드","primary_archetype":"consumer_export_channel_reorder","loop_objective":"sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2023-11-14","entry_date":"2023-11-15","entry_price":199600,"evidence_available_at_that_date":"public earnings/export mix and brand demand evidence; timing treated as next-tradable-day entry","evidence_source":"company disclosure/earnings-window evidence; historical research proxy","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision_later","margin_bridge_later"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2023.csv","profile_path":"atlas/symbol_profiles/003/003230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.98,"MFE_90D_pct":19.99,"MFE_180D_pct":259.72,"MFE_1Y_pct":259.72,"MFE_2Y_pct":null,"MAE_30D_pct":-5.11,"MAE_90D_pct":-15.13,"MAE_180D_pct":-15.13,"MAE_1Y_pct":-15.13,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":718000,"drawdown_after_peak_pct":-20.19,"green_lateness_ratio":0.277,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_tested","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L11-C18-001-2023-11-15-199600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L11-C18-001-4B-2024-06-18","case_id":"R5L11-C18-001","symbol":"003230","company_name":"삼양식품","round":"R5","loop":"11","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF","sector":"소비재·유통·브랜드","primary_archetype":"consumer_export_channel_reorder","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-06-18","entry_date":"2024-06-18","entry_price":712000,"evidence_available_at_that_date":"local valuation/positioning overheat proxy near full observed peak","evidence_source":"Stock-Web OHLC overlay; non-price fatigue not asserted as full 4B","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv","profile_path":"atlas/symbol_profiles/003/003230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.84,"MFE_90D_pct":0.84,"MFE_180D_pct":0.84,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-19.52,"MAE_90D_pct":-25.98,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":718000,"drawdown_after_peak_pct":-20.19,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.988,"four_b_full_window_peak_proximity":0.988,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_tested","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_correct_overlay","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L11-C18-001-2024-06-18-712000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L11-C18-002-S2A-2024-05-17","case_id":"R5L11-C18-002","symbol":"005180","company_name":"빙그레","round":"R5","loop":"11","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF","sector":"소비재·유통·브랜드","primary_archetype":"consumer_export_channel_reorder","loop_objective":"sector_specific_rule_discovery;4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-16","entry_date":"2024-05-17","entry_price":88300,"evidence_available_at_that_date":"public result-window evidence for overseas/seasonal channel growth; next-tradable-day entry","evidence_source":"company disclosure/earnings-window evidence; historical research proxy","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["margin_bridge_partial"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv","profile_path":"atlas/symbol_profiles/005/005180.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":34.09,"MFE_90D_pct":34.09,"MFE_180D_pct":34.09,"MFE_1Y_pct":34.09,"MFE_2Y_pct":null,"MAE_30D_pct":-9.29,"MAE_90D_pct":-32.96,"MAE_180D_pct":-32.96,"MAE_1Y_pct":-32.96,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-11","peak_price":118400,"drawdown_after_peak_pct":-50.00,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_tested","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_too_early_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L11-C18-002-2024-05-17-88300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L11-C18-002-4B-2024-06-10","case_id":"R5L11-C18-002","symbol":"005180","company_name":"빙그레","round":"R5","loop":"11","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF","sector":"소비재·유통·브랜드","primary_archetype":"consumer_export_channel_reorder","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-06-10","entry_date":"2024-06-10","entry_price":112100,"evidence_available_at_that_date":"price/valuation local peak proxy; non-price fatigue not asserted","evidence_source":"Stock-Web OHLC overlay","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv","profile_path":"atlas/symbol_profiles/005/005180.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.62,"MFE_90D_pct":5.62,"MFE_180D_pct":5.62,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-22.84,"MAE_90D_pct":-47.19,"MAE_180D_pct":-47.19,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-11","peak_price":118400,"drawdown_after_peak_pct":-50.00,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.791,"four_b_full_window_peak_proximity":0.791,"four_b_timing_verdict":"price_only_local_4B_overlay_useful","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"not_tested","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_correct_overlay","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L11-C18-002-2024-06-10-112100","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L11-C18-003-S2A-2024-05-17","case_id":"R5L11-C18-003","symbol":"004370","company_name":"농심","round":"R5","loop":"11","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF","sector":"소비재·유통·브랜드","primary_archetype":"consumer_export_channel_reorder","loop_objective":"counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-16","entry_date":"2024-05-17","entry_price":399000,"evidence_available_at_that_date":"K-food/overseas ramen result-window narrative; channel quality less pure than structural success cases","evidence_source":"company disclosure/earnings-window evidence; historical research proxy","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","theme_channel_narrative"],"stage3_evidence_fields":["weak_confirmed_revision"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv","profile_path":"atlas/symbol_profiles/004/004370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":50.13,"MFE_90D_pct":50.13,"MFE_180D_pct":50.13,"MFE_1Y_pct":50.13,"MFE_2Y_pct":null,"MAE_30D_pct":-1.75,"MAE_90D_pct":-9.65,"MAE_180D_pct":-20.55,"MAE_1Y_pct":-20.55,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-13","peak_price":599000,"drawdown_after_peak_pct":-47.08,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_tested","trigger_outcome_label":"price_moved_without_durable_evidence","current_profile_verdict":"current_profile_false_positive_if_promoted_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L11-C18-003-2024-05-17-399000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L11-C18-003-4B-2024-06-13","case_id":"R5L11-C18-003","symbol":"004370","company_name":"농심","round":"R5","loop":"11","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF","sector":"소비재·유통·브랜드","primary_archetype":"consumer_export_channel_reorder","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-06-13","entry_date":"2024-06-13","entry_price":547000,"evidence_available_at_that_date":"price-only local overheat near K-food theme peak","evidence_source":"Stock-Web OHLC overlay","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv","profile_path":"atlas/symbol_profiles/004/004370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.51,"MFE_90D_pct":9.51,"MFE_180D_pct":9.51,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.43,"MAE_90D_pct":-33.18,"MAE_180D_pct":-42.05,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-13","peak_price":599000,"drawdown_after_peak_pct":-47.08,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.740,"four_b_full_window_peak_proximity":0.740,"four_b_timing_verdict":"price_only_theme_4B_overlay_not_full_4B","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"not_tested","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_correct_overlay","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L11-C18-003-2024-06-13-547000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L11-C18-004-S2A-2024-05-17","case_id":"R5L11-C18-004","symbol":"097950","company_name":"CJ제일제당","round":"R5","loop":"11","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_GLOBAL_CHANNEL_REORDER_VS_THEME_BLOWOFF","sector":"소비재·유통·브랜드","primary_archetype":"consumer_export_channel_reorder","loop_objective":"counterexample_mining;canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-16","entry_date":"2024-05-17","entry_price":333500,"evidence_available_at_that_date":"overseas food result-window narrative, but conglomerate dilution and weak pure-play channel conversion","evidence_source":"company disclosure/earnings-window evidence; historical research proxy","stage2_evidence_fields":["public_event_or_disclosure","overseas_food_narrative"],"stage3_evidence_fields":["weak_margin_bridge","conglomerate_dilution"],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/097/097950/2024.csv","profile_path":"atlas/symbol_profiles/097/097950.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":22.19,"MFE_90D_pct":22.19,"MFE_180D_pct":22.19,"MFE_1Y_pct":22.19,"MFE_2Y_pct":null,"MAE_30D_pct":-0.30,"MAE_90D_pct":-10.04,"MAE_180D_pct":-28.34,"MAE_1Y_pct":-28.34,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-26","peak_price":407500,"drawdown_after_peak_pct":-41.35,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.872,"four_b_full_window_peak_proximity":0.872,"four_b_timing_verdict":"modest_4B_overlay_then_failed_rerating","four_b_evidence_type":["margin_or_backlog_slowdown","conglomerate_dilution"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating_guard","current_profile_verdict":"current_profile_false_positive_if_promoted_yellow","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L11-C18-004-2024-05-17-333500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L11-C18-001","trigger_id":"R5L11-C18-001-S2A-2023-11-15","symbol":"003230","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":6,"revision_score":7,"relative_strength_score":6,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":8},"weighted_score_before":84,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":8,"revision_score":8,"relative_strength_score":6,"customer_quality_score":9,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":9},"weighted_score_after":88,"stage_label_after":"Stage2-Actionable_later_Green_candidate","changed_components":["margin_bridge_score","revision_score","customer_quality_score","channel_reorder_score"],"component_delta_explanation":"Pure channel reorder evidence plus later margin/revision closure merits C18 positive promotion.","MFE_90D_pct":19.99,"MAE_90D_pct":-15.13,"score_return_alignment_label":"aligned_structural_success","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L11-C18-002","trigger_id":"R5L11-C18-002-S2A-2024-05-17","symbol":"005180","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":7,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":7},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow_risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":6,"revision_score":5,"relative_strength_score":7,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":8},"weighted_score_after":80,"stage_label_after":"Stage2-Actionable_with_4B_overlay","changed_components":["margin_bridge_score","customer_quality_score","channel_reorder_score","execution_risk_score"],"component_delta_explanation":"Positive channel evidence remains usable, but high MAE and local peak require overlay rather than Green.","MFE_90D_pct":34.09,"MAE_90D_pct":-32.96,"score_return_alignment_label":"aligned_but_high_mae","current_profile_verdict":"current_profile_too_early_if_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L11-C18-003","trigger_id":"R5L11-C18-003-S2A-2024-05-17","symbol":"004370","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":5},"weighted_score_before":79,"stage_label_before":"Stage3-Yellow_risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":3},"weighted_score_after":68,"stage_label_after":"Stage2-watch_4B_overlay_only","changed_components":["margin_bridge_score","revision_score","customer_quality_score","channel_reorder_score","execution_risk_score"],"component_delta_explanation":"Theme/relative strength is not channel reorder proof; block positive promotion unless margin/revision closes.","MFE_90D_pct":50.13,"MAE_90D_pct":-9.65,"score_return_alignment_label":"price_moved_without_durable_evidence","current_profile_verdict":"current_profile_false_positive_if_promoted_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L11-C18-004","trigger_id":"R5L11-C18-004-S2A-2024-05-17","symbol":"097950","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":5,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":5,"conglomerate_dilution_score":8},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow_risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":3,"conglomerate_dilution_score":9},"weighted_score_after":65,"stage_label_after":"narrative_only_or_Stage2-watch","changed_components":["margin_bridge_score","revision_score","customer_quality_score","channel_reorder_score","execution_risk_score","conglomerate_dilution_score"],"component_delta_explanation":"Conglomerate structure dilutes pure C18 signal; cap unless segment-level export margin bridge is explicit.","MFE_90D_pct":22.19,"MAE_90D_pct":-10.04,"score_return_alignment_label":"failed_rerating_guard","current_profile_verdict":"current_profile_false_positive_if_promoted_yellow"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C18_channel_reorder_quality_gate,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"C18 needs repeat-order/channel evidence plus margin/revision bridge; theme-only evidence created false-positive risk.","Blocks 004370/097950 positive promotion while keeping 003230/005180 as actionable or overlay cases.","R5L11-C18-001-S2A-2023-11-15|R5L11-C18-002-S2A-2024-05-17|R5L11-C18-003-S2A-2024-05-17|R5L11-C18-004-S2A-2024-05-17",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C18_conglomerate_dilution_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"Overseas food narrative inside conglomerate structure did not behave like pure-play channel reorder.","097950 MFE_180 only 22.19 with MAE_180 -28.34; cap below Yellow unless pure segment margin bridge is explicit.","R5L11-C18-004-S2A-2024-05-17",1,1,1,low,canonical_shadow_only,"needs more holdout cases"
shadow_weight,C18_price_only_theme_4b_overlay,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"Price-only K-food spike can produce local MFE but later drawdown; use as overlay not positive training.","004370 and 005180 both show local peak proximity useful for 4B timing but not full 4B without non-price fatigue.","R5L11-C18-002-4B-2024-06-10|R5L11-C18-003-4B-2024-06-13",2,2,1,medium,canonical_shadow_only,"strengthens existing 4B guardrail"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R5","loop":"11","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_canonical_archetype_count":1,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["theme_only_channel_narrative_false_positive","conglomerate_dilution_blocks_pure_c18_rerating","high_mae_success_requires_4b_overlay"],"diversity_score_summary":"new_symbol=4; new_trigger_family=4; counterexample=2; positive=2; reused=0; duplicate_penalty=0","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"R5/L5 C18 food-export channel reorder vs price-only theme blowoff"}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R5L11-C18-future-holdout-nonfood-export","symbol":null,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","reason":"future holdout should test non-food consumer export-channel reorder to avoid overfitting C18 to ramen/ice-cream cases","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- Price-only rows cannot promote Stage2/Stage3.
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
next_round = R5_loop_12_or_R5_C18_holdout
recommended_next_scope = C18 non-food consumer export-channel reorder holdout OR C19 brand retail inventory margin
reason = current loop adds food-export positives/counterexamples, but C18 needs non-food validation to avoid flavor-specific overfit
```

## 28. Source Notes

Stock-Web files inspected:

- atlas/manifest.json
- atlas/schema.json
- atlas/symbol_profiles/003/003230.json
- atlas/symbol_profiles/005/005180.json
- atlas/symbol_profiles/004/004370.json
- atlas/symbol_profiles/097/097950.json
- atlas/ohlcv_tradable_by_symbol_year/003/003230/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/005/005180/2025.csv
- atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/004/004370/2025.csv
- atlas/ohlcv_tradable_by_symbol_year/097/097950/2024.csv

Allowed stock_agent research artifacts inspected:

- reports/e2r_calibration/ingest_summary.md
- repository search for C18_CONSUMER_EXPORT_CHANNEL_REORDER coverage

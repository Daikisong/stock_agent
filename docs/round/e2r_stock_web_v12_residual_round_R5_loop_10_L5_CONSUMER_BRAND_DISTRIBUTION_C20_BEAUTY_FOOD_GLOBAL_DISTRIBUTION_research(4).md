# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R5
loop = 10
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_GLOBAL_PLATFORM_REORDER
loop_objective = coverage_gap_fill | counterexample_mining | canonical_archetype_compression | 4B_non_price_requirement_stress_test | residual_false_positive_mining
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This MD is historical calibration research only. It is not a live watchlist, not a current stock discovery run, not an auto-trading instruction, and not a `stock_agent` code patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The test here is not whether Stage2 is earlier than Green in general. The test is whether C20 needs its own split between **platform/distributor-led repeat reorder** and broad **beauty/China-reopening narrative**.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| round | R5 |
| loop | 10 |
| large_sector_id | L5_CONSUMER_BRAND_DISTRIBUTION |
| canonical_archetype_id | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION |
| fine_archetype_id | K_BEAUTY_GLOBAL_PLATFORM_REORDER |
| selection_mode | auto_coverage_gap_fill |
| auto_selected_coverage_gap | L5/C20 had useful unresolved positive/counterexample split: K-beauty global reorder winners vs China-reopening/incumbent false positives. |

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifacts were used only for coverage/duplication orientation. `reports/e2r_calibration/ingest_summary.md` showed broad historical coverage across R1~R13 and 1,376 aggregate representative trigger rows, but this MD intentionally does **not** open `src/e2r` or infer production scoring code.

This loop avoids the immediately previous C32 governance/tender-cap run and selects a different large sector and canonical archetype.

```text
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
new_canonical_archetype_count = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

| Field | Value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| active_like_symbol_count | 2868 |
| inactive_or_delisted_like_symbol_count | 2546 |
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

`stock_web_manifest_max_date = 2026-02-20`. All forward windows in this MD are judged against this manifest date, not the current calendar date.

## 5. Historical Eligibility Gate

| case_id | symbol | profile_path | first/last availability note | corporate_action_window_status | calibration_usable |
|---|---:|---|---|---|---|
| R5L10_C20_SILICON2_2024Q1_REORDER | 257720 | atlas/symbol_profiles/257/257720.json | available through 2026-02-20; corporate-action candidates only in 2022 | clean_180D_window | true |
| R5L10_C20_VT_2024Q1_REEDLESHOT | 018290 | atlas/symbol_profiles/018/018290.json | available through 2026-02-20; modern window clean after 2019 candidates | clean_180D_window | true |
| R5L10_C20_CLIO_2024Q1_CHANNEL_STALL | 237880 | atlas/symbol_profiles/237/237880.json | available through 2026-02-20; no profile CA candidate | clean_180D_window | true |
| R5L10_C20_AMORE_2024_COSRX_CHINA_REVERSAL | 090430 | atlas/symbol_profiles/090/090430.json | available through 2026-02-20; CA candidate is 2015 only | clean_180D_window | true |

## 6. Canonical Archetype Compression Map

```text
fine_archetype: K_BEAUTY_GLOBAL_PLATFORM_REORDER
maps_to: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
large_sector: L5_CONSUMER_BRAND_DISTRIBUTION
```

Compression rule: all beauty/export/channel cases in this loop stay under C20. The proposed rule is not a new global axis.

## 7. Case Selection Summary

| case_id | symbol | company | role | pos/counter | best_trigger | entry | MFE90 | MAE90 | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R5L10_C20_SILICON2_2024Q1_REORDER | 257720 | 실리콘투 | structural_success | positive | R5L10_C20_SILICON2_STAGE2A_20240509 | 2024-05-10 @ 26250 | 106.48 | -17.9 | current_profile_missed_structural |
| R5L10_C20_VT_2024Q1_REEDLESHOT | 018290 | 브이티 | structural_success | positive | R5L10_C20_VT_STAGE2A_20240509 | 2024-05-10 @ 25400 | 57.48 | -12.6 | current_profile_correct |
| R5L10_C20_CLIO_2024Q1_CHANNEL_STALL | 237880 | 클리오 | high_mae_success | counterexample | R5L10_C20_CLIO_STAGE2_20240509 | 2024-05-10 @ 34850 | 29.12 | -13.34 | current_profile_false_positive |
| R5L10_C20_AMORE_2024_COSRX_CHINA_REVERSAL | 090430 | 아모레퍼시픽 | false_positive_green | counterexample | R5L10_C20_AMORE_STAGE2_20240429 | 2024-04-30 @ 169500 | 18.29 | -31.62 | current_profile_4C_too_late |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 1
4C_case_count = 1
calibration_usable_case_count = 4
calibration_usable_trigger_count = 6
```

The useful split is not “K-beauty good / K-beauty bad.” The split is more like a warehouse belt sorting packages: **the same category label enters the belt, but the parcels with real reorder density, route diversity, and margin bridge exit on a different lane**. Silicon2 and VT had evidence that the engine was already turning; Clio and Amore show why a generic beauty narrative should not receive the same promotion.

## 9. Evidence Source Map

| case_id | evidence_available_at_that_date | stage2 | stage3 | 4B | 4C |
|---|---|---|---|---|---|
| R5L10_C20_SILICON2_2024Q1_REORDER | 2024Q1 revenue/profit acceleration and global K-beauty distributor/platform identity; price response confirms market saw evidence as order/reorder, not just brand narrative. | customer_or_order_quality, capacity_or_volume_route, relative_strength, early_revision_signal | confirmed_revision, financial_visibility, multiple_public_sources, repeat_order_or_conversion | valuation_blowoff, positioning_overheat | - |
| R5L10_C20_VT_2024Q1_REEDLESHOT | Reedle Shot/overseas beauty sales quality and operating margin expansion; not a one-day price-only theme. | customer_or_order_quality, relative_strength, early_revision_signal | confirmed_revision, margin_bridge, financial_visibility, durable_customer_confirmation | positioning_overheat, valuation_blowoff | - |
| R5L10_C20_CLIO_2024Q1_CHANNEL_STALL | Brand/channel story existed, but later margin and growth durability did not match Silicon2/VT quality. It is a counterexample against broad K-beauty equal-weight promotion. | public_event_or_disclosure, relative_strength | multiple_public_sources | margin_or_backlog_slowdown, positioning_overheat | - |
| R5L10_C20_AMORE_2024_COSRX_CHINA_REVERSAL | COSRX acquisition and global portfolio narrative existed, but China exposure and post-Q2 miss broke the positive rerating thesis. | public_event_or_disclosure, policy_or_regulatory_optionality, early_revision_signal | financial_visibility | explicit_event_cap, margin_or_backlog_slowdown | thesis_evidence_broken |

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | price_basis | adjustment |
|---:|---|---|---|---|---|
| 257720 | 실리콘투 | `atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv` | `atlas/symbol_profiles/257/257720.json` | tradable_raw | raw_unadjusted_marcap |
| 018290 | 브이티 | `atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv` | `atlas/symbol_profiles/018/018290.json` | tradable_raw | raw_unadjusted_marcap |
| 237880 | 클리오 | `atlas/ohlcv_tradable_by_symbol_year/237/237880/2024.csv` | `atlas/symbol_profiles/237/237880.json` | tradable_raw | raw_unadjusted_marcap |
| 090430 | 아모레퍼시픽 | `atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv` | `atlas/symbol_profiles/090/090430.json` | tradable_raw | raw_unadjusted_marcap |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | representative? | stage outcome |
|---|---|---|---|---|---:|---|---|
| R5L10_C20_SILICON2_STAGE2A_20240509 | R5L10_C20_SILICON2_2024Q1_REORDER | Stage2-Actionable | 2024-05-09 | 2024-05-10 | 26250 | True | structural_reorder_success |
| R5L10_C20_VT_STAGE2A_20240509 | R5L10_C20_VT_2024Q1_REEDLESHOT | Stage2-Actionable | 2024-05-09 | 2024-05-10 | 25400 | True | structural_reorder_success |
| R5L10_C20_CLIO_STAGE2_20240509 | R5L10_C20_CLIO_2024Q1_CHANNEL_STALL | Stage2 | 2024-05-09 | 2024-05-10 | 34850 | True | failed_sustained_rerating |
| R5L10_C20_AMORE_STAGE2_20240429 | R5L10_C20_AMORE_2024_COSRX_CHINA_REVERSAL | Stage2 | 2024-04-29 | 2024-04-30 | 169500 | True | false_positive_green_then_4c |
| R5L10_C20_SILICON2_4B_20240619 | R5L10_C20_SILICON2_2024Q1_REORDER | Stage4B-Overlay | 2024-06-19 | 2024-06-19 | 50700 | False | 4B_overlay_success |
| R5L10_C20_AMORE_4C_20240807 | R5L10_C20_AMORE_2024_COSRX_CHINA_REVERSAL | Stage4C | 2024-08-07 | 2024-08-07 | 124500 | False | 4C_success |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| R5L10_C20_SILICON2_STAGE2A_20240509 | 26250 | 106.48 | -17.9 | 106.48 | -17.9 | 106.48 | -17.9 | 2024-06-19 | 54200 | -47.79 |
| R5L10_C20_VT_STAGE2A_20240509 | 25400 | 57.48 | -12.6 | 57.48 | -12.6 | 57.48 | -12.6 | 2024-06-19 | 40000 | -35.0 |
| R5L10_C20_CLIO_STAGE2_20240509 | 34850 | 29.12 | -4.45 | 29.12 | -13.34 | 29.12 | -15.93 | 2024-06-13 | 45000 | -34.89 |
| R5L10_C20_AMORE_STAGE2_20240429 | 169500 | 18.29 | -4.84 | 18.29 | -31.62 | 18.29 | -31.62 | 2024-05-31 | 200500 | -42.19 |
| R5L10_C20_SILICON2_4B_20240619 | 50700 | 6.11 | -20.61 | 6.11 | -44.18 | 6.11 | -44.18 | 2024-06-19 | 54200 | -47.79 |
| R5L10_C20_AMORE_4C_20240807 | 124500 | 2.01 | -6.91 | 20.4 | -6.91 | 20.4 | -6.91 | 2024-05-31 | 200500 | -42.19 |

## 13. Current Calibrated Profile Stress Test

| case_id | current_profile_verdict | test result | interpretation |
|---|---|---|---|
| R5L10_C20_SILICON2_2024Q1_REORDER | current_profile_missed_structural | MFE90 +106.48% after clean Stage2A | Current global Green strictness can be late when the reorder route itself is already a financial visibility proxy. |
| R5L10_C20_VT_2024Q1_REEDLESHOT | current_profile_correct | MFE90 +57.48%, MAE90 -12.60% | Current profile works when product velocity, margin bridge, and overseas sell-through align. |
| R5L10_C20_CLIO_2024Q1_CHANNEL_STALL | current_profile_false_positive | MFE90 +29.12%, MAE180 -15.93%, drawdown -34.89% | Generic channel/global language without repeat reorder should not be upgraded to Green. |
| R5L10_C20_AMORE_2024_COSRX_CHINA_REVERSAL | current_profile_4C_too_late | MFE90 +18.29%, MAE90 -31.62%, drawdown -42.19% | China exposure/margin break required faster hard 4C routing after 2024-08 evidence break. |

Answers to the profile questions:

1. Current profile would likely rate Silicon2/VT as high Yellow to Green, Clio/Amore as Yellow if broad beauty revision language was over-weighted.
2. It matches VT, is too late for Silicon2, and too permissive for Clio/Amore.
3. Stage2 bonus is useful, but C20 needs a quality gate.
4. Yellow 75 is acceptable.
5. Green 87/revision 55 is too strict for distributor platform reorder, but not for brand-only narratives.
6. Price-only blowoff guard is appropriate and strengthened.
7. Full 4B non-price requirement is appropriate and strengthened.
8. Hard 4C routing should be faster when China/incumbent thesis break appears after a prior event-premium rally.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | proposed Green entry | green_lateness_ratio | verdict |
|---|---|---|---:|---|
| Silicon2 | 2024-05-10 @ 26,250 | same row after C20 reorder bonus | 0.00 | C20-specific rule prevents late Green. |
| VT | 2024-05-10 @ 25,400 | same row after product/reorder bonus | 0.00 | Green not late because evidence is already margin-backed. |
| Clio | 2024-05-10 @ 34,850 | blocked | not_applicable | Do not promote broad channel language to Green. |
| Amorepacific | 2024-04-30 @ 169,500 | blocked | not_applicable | COSRX/global narrative lacks clean non-China repeat-order proof and later breaks. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_evidence_type | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---|---:|---:|---|
| R5L10_C20_SILICON2_4B_20240619 | valuation_blowoff, positioning_overheat | 0.875 | 0.875 | good_full_window_4B_timing |
| R5L10_C20_AMORE_STAGE2_20240429 | explicit_event_cap, margin_or_backlog_slowdown | 0.797 | 0.797 | event premium faded; full 4B should require non-price margin/geography evidence |

## 16. 4C Protection Audit

| trigger_id | prior peak | 4C entry | MAE90 after 4C | label |
|---|---:|---:|---:|---|
| R5L10_C20_AMORE_4C_20240807 | 200,500 | 124,500 | -6.91 | hard_4c_success |
| Clio implied 4C/watch | 45,000 | no hard break row | -15.93 from Stage2 | thesis_break_watch_only |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = the loop is concentrated in one canonical archetype; promote as C20 canonical shadow rule first.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
```

Proposed C20 shadow rule:

```text
if channel_reorder_score >= strong
and margin_bridge_score >= visible
and route_quality in [platform_distributor, product_velocity_overseas, non_china_repeat_reorder]
then add c20_distributor_platform_reorder_bonus = +3

if thesis is broad China reopening / incumbent portfolio recovery
and channel_reorder_score is not supported by repeat reorder or margin bridge
then apply c20_china_reopening_incumbent_discount = -4

if channel breadth exists but margin bridge or reorder proof is weak
then cap at Stage2-Watch or Stage3-Yellow, not Green

if prior event premium is high and margin/geography evidence breaks
then route to hard_4c_thesis_break faster
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible | avg_MFE90 | avg_MAE90 | false_positive_rate | missed_structural | verdict |
|---|---|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | global_current | 4 | 52.84 | -18.86 | 0.50 | 1 | mixed: high positive returns but two broad-beauty false positives |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 4 | 52.84 | -18.86 | 0.50 | 0 | worse guard quality; counterexamples remain exposed |
| P1_L5_sector_specific_candidate | sector_specific | 3 | 64.36 | -14.61 | 0.33 | 0 | improves but still too broad |
| P2_C20_canonical_archetype_candidate | canonical_archetype_specific | 2 | 81.98 | -15.25 | 0.00 | 0 | best score-return alignment in this loop |
| P3_C20_counterexample_guard | guard_profile | 4 | 52.84 | -18.86 | 0.00 | 0 | best false-positive control; may need more positives to avoid over-filtering |

## 20. Score-Return Alignment Matrix

| case_id | before_score | before_label | after_score | after_label | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| R5L10_C20_SILICON2_2024Q1_REORDER | 84.5 | Stage3-Yellow | 90.5 | Stage3-Green | 106.48 | -17.9 | improved |
| R5L10_C20_VT_2024Q1_REEDLESHOT | 83.0 | Stage3-Yellow | 88.5 | Stage3-Green | 57.48 | -12.6 | improved |
| R5L10_C20_CLIO_2024Q1_CHANNEL_STALL | 79.0 | Stage3-Yellow | 72.0 | Stage2-Watch | 29.12 | -13.34 | improved |
| R5L10_C20_AMORE_2024_COSRX_CHINA_REVERSAL | 81.0 | Stage3-Yellow | 68.5 | Stage2-Watch / 4C after break | 18.29 | -31.62 | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_BEAUTY_GLOBAL_PLATFORM_REORDER | 2 | 2 | 1 | 1 | 4 | 0 | 6 | 4 | 3 | false | true | Need holdout in food export and non-beauty consumer channel cases. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage3_cross_evidence_green_buffer
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - missed_structural_distributor_reorder
  - broad_beauty_false_positive
  - china_reopening_narrative_false_positive
  - late_4c_after_margin_break
new_axis_proposed:
  - c20_distributor_platform_reorder_bonus
  - c20_china_reopening_incumbent_discount
  - c20_channel_breadth_without_reorder_guard
  - c20_overheat_4b_overlay_after_100pct_mfe
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest max_date and raw/unadjusted price basis.
- Four symbol profile availability and corporate-action caveat status.
- Four representative Stage2/Stage2A rows and two overlay rows.
- 30D/90D/180D MFE/MAE from stock-web tradable OHLC rows.
- C20 positive/counterexample balance.
```

Not validated:

```text
- No current/live stock recommendation.
- No 2026 current candidate scan.
- No production scoring change.
- No `stock_agent/src/e2r` code opened.
- No broker/API/trading action.
- 1Y/2Y fields are not used for this loop's weight decision; 180D clean windows drive quantitative inclusion.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c20_distributor_platform_reorder_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,+3,+3,"Silicon2/VT show high MFE when reorder is distributor/platform-led and margin bridge is visible","P2 avg MFE90 81.98 vs P0 false-positive mixed set",R5L10_C20_SILICON2_STAGE2A_20240509|R5L10_C20_VT_STAGE2A_20240509,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c20_china_reopening_incumbent_discount,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,-4,-4,"Amore shows broad China/COSRX narrative can fail after margin/geography break","reduces broad-beauty false positive",R5L10_C20_AMORE_STAGE2_20240429,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c20_channel_breadth_without_reorder_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,-3,-3,"Clio shows global/channel language without repeat reorder and margin bridge should stay below Green","reduces false Green without blocking Stage2 watch",R5L10_C20_CLIO_STAGE2_20240509,4,4,2,low,canonical_shadow_only,"needs more holdout"
shadow_weight,c20_overheat_4b_overlay_after_100pct_mfe,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,+1,+1,"Silicon2 4B overlay close to full-window peak when valuation+positioning evidence exists","risk overlay not positive promotion",R5L10_C20_SILICON2_4B_20240619,1,1,0,low,overlay_only,"not production; 4B only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R5L10_C20_SILICON2_2024Q1_REORDER", "symbol": "257720", "company_name": "실리콘투", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_PLATFORM_REORDER", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R5L10_C20_SILICON2_STAGE2A_20240509", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "Old global profile can wait for confirmed revision; C20 should allow distributor reorder + margin jump to promote earlier when channel quality is non-China and repeated."}
{"row_type": "case", "case_id": "R5L10_C20_VT_2024Q1_REEDLESHOT", "symbol": "018290", "company_name": "브이티", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_PLATFORM_REORDER", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R5L10_C20_VT_STAGE2A_20240509", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "C20 rule should credit product-led overseas sell-through when margin bridge is already visible."}
{"row_type": "case", "case_id": "R5L10_C20_CLIO_2024Q1_CHANNEL_STALL", "symbol": "237880", "company_name": "클리오", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_PLATFORM_REORDER", "case_type": "high_mae_success", "positive_or_counterexample": "counterexample", "best_trigger": "R5L10_C20_CLIO_STAGE2_20240509", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_or_guard_needed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "C20 should penalize channel breadth without repeat reorder, distributor leverage, or margin bridge."}
{"row_type": "case", "case_id": "R5L10_C20_AMORE_2024_COSRX_CHINA_REVERSAL", "symbol": "090430", "company_name": "아모레퍼시픽", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_PLATFORM_REORDER", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R5L10_C20_AMORE_STAGE2_20240429", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_or_guard_needed", "current_profile_verdict": "current_profile_4C_too_late", "price_source": "Songdaiki/stock-web", "notes": "C20 must distinguish non-China indie-brand export flywheel from incumbent China-recovery narrative."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R5L10_C20_SILICON2_STAGE2A_20240509", "case_id": "R5L10_C20_SILICON2_2024Q1_REORDER", "symbol": "257720", "company_name": "실리콘투", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_PLATFORM_REORDER", "sector": "소비재·유통·브랜드", "primary_archetype": "K-beauty global distribution/reorder", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-09", "evidence_available_at_that_date": "2024Q1 revenue/profit acceleration and global K-beauty distributor/platform identity; price response confirms market saw evidence as order/reorder, not just brand narrative.", "evidence_source": "2024Q1 earnings/disclosure + Naver/FnGuide financial table + stock-web OHLC", "stage2_evidence_fields": ["customer_or_order_quality", "capacity_or_volume_route", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources", "repeat_order_or_conversion"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv", "profile_path": "atlas/symbol_profiles/257/257720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-10", "entry_price": 26250, "MFE_30D_pct": 106.48, "MFE_90D_pct": 106.48, "MFE_180D_pct": 106.48, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -17.9, "MAE_90D_pct": -17.9, "MAE_180D_pct": -17.9, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-19", "peak_price": 54200, "drawdown_after_peak_pct": -47.79, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_reorder_success", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L10_C20_SILICON2_20240510", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L10_C20_VT_STAGE2A_20240509", "case_id": "R5L10_C20_VT_2024Q1_REEDLESHOT", "symbol": "018290", "company_name": "브이티", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_PLATFORM_REORDER", "sector": "소비재·유통·브랜드", "primary_archetype": "K-beauty global distribution/reorder", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-09", "evidence_available_at_that_date": "Reedle Shot/overseas beauty sales quality and operating margin expansion; not a one-day price-only theme.", "evidence_source": "2024Q1 earnings/disclosure + Naver/FnGuide financial table + stock-web OHLC", "stage2_evidence_fields": ["customer_or_order_quality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": ["positioning_overheat", "valuation_blowoff"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv", "profile_path": "atlas/symbol_profiles/018/018290.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-10", "entry_price": 25400, "MFE_30D_pct": 57.48, "MFE_90D_pct": 57.48, "MFE_180D_pct": 57.48, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -12.6, "MAE_90D_pct": -12.6, "MAE_180D_pct": -12.6, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-19", "peak_price": 40000, "drawdown_after_peak_pct": -35.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": ["positioning_overheat", "valuation_blowoff"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_reorder_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L10_C20_VT_20240510", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L10_C20_CLIO_STAGE2_20240509", "case_id": "R5L10_C20_CLIO_2024Q1_CHANNEL_STALL", "symbol": "237880", "company_name": "클리오", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_PLATFORM_REORDER", "sector": "소비재·유통·브랜드", "primary_archetype": "K-beauty global distribution/reorder", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2", "trigger_date": "2024-05-09", "evidence_available_at_that_date": "Brand/channel story existed, but later margin and growth durability did not match Silicon2/VT quality. It is a counterexample against broad K-beauty equal-weight promotion.", "evidence_source": "2024Q1 earnings/disclosure + Naver/FnGuide financial table + stock-web OHLC", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/237/237880/2024.csv", "profile_path": "atlas/symbol_profiles/237/237880.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-10", "entry_price": 34850, "MFE_30D_pct": 29.12, "MFE_90D_pct": 29.12, "MFE_180D_pct": 29.12, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.45, "MAE_90D_pct": -13.34, "MAE_180D_pct": -15.93, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-13", "peak_price": 45000, "drawdown_after_peak_pct": -34.89, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": ["margin_or_backlog_slowdown", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "failed_sustained_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L10_C20_CLIO_20240510", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L10_C20_AMORE_STAGE2_20240429", "case_id": "R5L10_C20_AMORE_2024_COSRX_CHINA_REVERSAL", "symbol": "090430", "company_name": "아모레퍼시픽", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_PLATFORM_REORDER", "sector": "소비재·유통·브랜드", "primary_archetype": "K-beauty global distribution/reorder", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2", "trigger_date": "2024-04-29", "evidence_available_at_that_date": "COSRX acquisition and global portfolio narrative existed, but China exposure and post-Q2 miss broke the positive rerating thesis.", "evidence_source": "2024Q1/Q2 earnings/disclosure + FT China beauty weakness commentary + Naver/FnGuide profile/financial table + stock-web OHLC", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["explicit_event_cap", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv", "profile_path": "atlas/symbol_profiles/090/090430.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-30", "entry_price": 169500, "MFE_30D_pct": 18.29, "MFE_90D_pct": 18.29, "MFE_180D_pct": 18.29, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.84, "MAE_90D_pct": -31.62, "MAE_180D_pct": -31.62, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-31", "peak_price": 200500, "drawdown_after_peak_pct": -42.19, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": ["explicit_event_cap", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "false_positive_green_then_4c", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L10_C20_AMORE_20240430", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L10_C20_SILICON2_4B_20240619", "case_id": "R5L10_C20_SILICON2_2024Q1_REORDER", "symbol": "257720", "company_name": "실리콘투", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_PLATFORM_REORDER", "sector": "소비재·유통·브랜드", "primary_archetype": "K-beauty global distribution/reorder", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-Overlay", "trigger_date": "2024-06-19", "evidence_available_at_that_date": "2024Q1 revenue/profit acceleration and global K-beauty distributor/platform identity; price response confirms market saw evidence as order/reorder, not just brand narrative.", "evidence_source": "2024Q1 earnings/disclosure + Naver/FnGuide financial table + stock-web OHLC", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv", "profile_path": "atlas/symbol_profiles/257/257720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-19", "entry_price": 50700, "MFE_30D_pct": 6.11, "MFE_90D_pct": 6.11, "MFE_180D_pct": 6.11, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -20.61, "MAE_90D_pct": -44.18, "MAE_180D_pct": -44.18, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-19", "peak_price": 54200, "drawdown_after_peak_pct": -47.79, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.875, "four_b_full_window_peak_proximity": 0.875, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L10_C20_SILICON2_20240619_4B", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L10_C20_AMORE_4C_20240807", "case_id": "R5L10_C20_AMORE_2024_COSRX_CHINA_REVERSAL", "symbol": "090430", "company_name": "아모레퍼시픽", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_PLATFORM_REORDER", "sector": "소비재·유통·브랜드", "primary_archetype": "K-beauty global distribution/reorder", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage4C", "trigger_date": "2024-08-07", "evidence_available_at_that_date": "COSRX acquisition and global portfolio narrative existed, but China exposure and post-Q2 miss broke the positive rerating thesis.", "evidence_source": "2024Q1/Q2 earnings/disclosure + FT China beauty weakness commentary + Naver/FnGuide profile/financial table + stock-web OHLC", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken", "margin_or_backlog_slowdown"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv", "profile_path": "atlas/symbol_profiles/090/090430.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-08-07", "entry_price": 124500, "MFE_30D_pct": 2.01, "MFE_90D_pct": 20.4, "MFE_180D_pct": 20.4, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.91, "MAE_90D_pct": -6.91, "MAE_180D_pct": -6.91, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-31", "peak_price": 200500, "drawdown_after_peak_pct": -42.19, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4C_success", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L10_C20_AMORE_20240807_4C", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c20_shadow", "case_id": "R5L10_C20_SILICON2_2024Q1_REORDER", "trigger_id": "R5L10_C20_SILICON2_STAGE2A_20240509", "symbol": "257720", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 15, "revision_score": 18, "relative_strength_score": 14, "customer_quality_score": 15, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 16, "platform_distribution_score": 15}, "weighted_score_before": 84.5, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 15, "revision_score": 18, "relative_strength_score": 14, "customer_quality_score": 16, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 19, "platform_distribution_score": 17}, "weighted_score_after": 90.5, "stage_label_after": "Stage3-Green", "changed_components": ["channel_reorder_score", "platform_distribution_score", "customer_quality_score"], "component_delta_explanation": "Old global profile can wait for confirmed revision; C20 should allow distributor reorder + margin jump to promote earlier when channel quality is non-China and repeated.", "MFE_90D_pct": 106.48, "MAE_90D_pct": -17.9, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c20_shadow", "case_id": "R5L10_C20_VT_2024Q1_REEDLESHOT", "trigger_id": "R5L10_C20_VT_STAGE2A_20240509", "symbol": "018290", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 16, "revision_score": 17, "relative_strength_score": 14, "customer_quality_score": 16, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 13, "product_velocity_score": 15}, "weighted_score_before": 83.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 17, "revision_score": 17, "relative_strength_score": 14, "customer_quality_score": 16, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 15, "product_velocity_score": 18}, "weighted_score_after": 88.5, "stage_label_after": "Stage3-Green", "changed_components": ["channel_reorder_score", "product_velocity_score", "margin_bridge_score"], "component_delta_explanation": "C20 rule should credit product-led overseas sell-through when margin bridge is already visible.", "MFE_90D_pct": 57.48, "MAE_90D_pct": -12.6, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c20_shadow", "case_id": "R5L10_C20_CLIO_2024Q1_CHANNEL_STALL", "trigger_id": "R5L10_C20_CLIO_STAGE2_20240509", "symbol": "237880", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 9, "revision_score": 12, "relative_strength_score": 12, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 9, "channel_concentration_risk_score": 8}, "weighted_score_before": 79.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 9, "revision_score": 12, "relative_strength_score": 12, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 11, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 5, "channel_concentration_risk_score": 11}, "weighted_score_after": 72.0, "stage_label_after": "Stage2-Watch", "changed_components": ["channel_reorder_score", "execution_risk_score", "channel_concentration_risk_score"], "component_delta_explanation": "C20 should penalize channel breadth without repeat reorder, distributor leverage, or margin bridge.", "MFE_90D_pct": 29.12, "MAE_90D_pct": -13.34, "score_return_alignment_label": "guard_improves_alignment", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c20_shadow", "case_id": "R5L10_C20_AMORE_2024_COSRX_CHINA_REVERSAL", "trigger_id": "R5L10_C20_AMORE_STAGE2_20240429", "symbol": "090430", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 14, "relative_strength_score": 10, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 9, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 7, "china_reopening_exposure_risk_score": 12}, "weighted_score_before": 81.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 14, "relative_strength_score": 10, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 13, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 2, "china_reopening_exposure_risk_score": 17}, "weighted_score_after": 68.5, "stage_label_after": "Stage2-Watch / 4C after break", "changed_components": ["channel_reorder_score", "execution_risk_score", "china_reopening_exposure_risk_score"], "component_delta_explanation": "C20 must distinguish non-China indie-brand export flywheel from incumbent China-recovery narrative.", "MFE_90D_pct": 18.29, "MAE_90D_pct": -31.62, "score_return_alignment_label": "guard_improves_alignment", "current_profile_verdict": "current_profile_4C_too_late"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c20_distributor_platform_reorder_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,+3,+3,"Silicon2/VT show high MFE when reorder is distributor/platform-led and margin bridge is visible","P2 avg MFE90 81.98 vs P0 false-positive mixed set",R5L10_C20_SILICON2_STAGE2A_20240509|R5L10_C20_VT_STAGE2A_20240509,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c20_china_reopening_incumbent_discount,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,-4,-4,"Amore shows broad China/COSRX narrative can fail after margin/geography break","reduces broad-beauty false positive",R5L10_C20_AMORE_STAGE2_20240429,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c20_channel_breadth_without_reorder_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,-3,-3,"Clio shows global/channel language without repeat reorder and margin bridge should stay below Green","reduces false Green without blocking Stage2 watch",R5L10_C20_CLIO_STAGE2_20240509,4,4,2,low,canonical_shadow_only,"needs more holdout"
shadow_weight,c20_overheat_4b_overlay_after_100pct_mfe,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,+1,+1,"Silicon2 4B overlay close to full-window peak when valuation+positioning evidence exists","risk overlay not positive promotion",R5L10_C20_SILICON2_4B_20240619,1,1,0,low,overlay_only,"not production; 4B only"
```

### 25.6 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": "10", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_canonical_archetype_count": 0, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 3, "tested_existing_calibrated_axes": ["stage3_cross_evidence_green_buffer", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["missed_structural_distributor_reorder", "broad_beauty_false_positive", "china_reopening_narrative_false_positive", "late_4c_after_margin_break"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "auto_selected_coverage_gap": "L5/C20 undercovered: positive+counterexample channel-quality split"}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"NONE","symbol":null,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","reason":"all selected cases had usable 180D forward windows; no narrative-only case needed","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
next_round = R5 or R13
recommended_next_scope = C20 holdout validation across non-beauty consumer export / food distribution, or R13 cross-archetype red-team for channel-reorder false positives
avoid_duplicate = do not repeat Silicon2 2024-05-10 or VT 2024-05-10 as representative Stage2A unless used only as holdout with independent_evidence_weight <= 0.25
```

## 28. Source Notes

- Stock-Web manifest: `atlas/manifest.json` in `Songdaiki/stock-web`. Manifest max date used in this MD is `2026-02-20`.
- Stock-Web rows cited by path:
  - `atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv`: Silicon2 2024-05-09~2024-06-28 rows show the Stage2 entry, >100% MFE, and post-peak drawdown zone.
  - `atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv`: VT 2024-05-09~2024-11-15 rows show product-led K-beauty rerating and 4B-style overheat/fade.
  - `atlas/ohlcv_tradable_by_symbol_year/237/237880/2024.csv`: Clio 2024-05-09~2024-09-19 rows show a weaker channel-reorder path and drawdown after initial run.
  - `atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv`: Amorepacific 2024-04-29~2024-09-13 rows show a COSRX/global portfolio rally followed by 2024-08 thesis break.
- Profile paths:
  - `atlas/symbol_profiles/257/257720.json`, `atlas/symbol_profiles/018/018290.json`, `atlas/symbol_profiles/237/237880.json`, `atlas/symbol_profiles/090/090430.json`.
- Business/fundamental context sources consulted:
  - Naver/FnGuide pages for Silicon2, VT, Clio, Amorepacific business profiles and current financial tables.
  - Reuters 2025 K-beauty export/ecommerce context and Silicon2 CEO quote, used only as sector background, not as a 2024 trigger source.
  - FT 2024 Asia beauty/Amorepacific China weakness context, used as counterexample support for incumbent China-exposure risk.

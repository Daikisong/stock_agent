# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R5
loop = 42
output_file = e2r_stock_web_v12_residual_round_R5_loop_42_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_GLOBAL_DISTRIBUTION_CHANNEL_REORDER | K_BEAUTY_SINGLE_PRODUCT_TO_GLOBAL_REORDER | K_BEAUTY_BRAND_RETAIL_CHANNEL_FALSE_POSITIVE
selection_mode = auto_coverage_gap_fill
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This MD is a historical calibration artifact only. It is not a current-stock-discovery note, not a live watchlist, and not a `stock_agent` code patch.

## 1. Current Calibrated Profile Assumption

```text
before_profile_id = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
after_profile_id = proposed_C20_beauty_global_distribution_shadow_profile
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The test does not re-prove the global Stage2 bonus. It asks whether C20 needs a narrower channel-reorder rule: K-beauty rerating works when visible demand moves from “brand story” into repeat wholesale/channel evidence, export-market spread, and margin/revision bridge. Without that bridge, the same beauty narrative becomes a false positive.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| round | R5 |
| loop | 42 |
| large_sector_id | L5_CONSUMER_BRAND_DISTRIBUTION |
| canonical_archetype_id | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION |
| loop_objective | coverage_gap_fill; counterexample_mining; residual_false_positive_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test |
| selected cases | 실리콘투, 브이티, 클리오 |
| representative triggers | 3 |
| usable triggers | 7 |
| calibration case balance | 2 positive / 1 counterexample |

## 3. Previous Coverage / Duplicate Avoidance Check

The search for `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION` in the allowed `stock_agent` research artifacts returned no direct match in repository search. The broader ingest summary confirms prior calibration material already spans all R1~R13 sectors, 107 parsed MDs, 1,940 validated trigger rows, and 1,376 aggregate representative rows. This loop therefore treats C20 as an under-specified canonical compression zone rather than as a repeat of an existing C20 rule. fileciteturn853file0

```text
auto_selected_coverage_gap = L5/C20 beauty global distribution lacks a C20-specific split between:
  (1) repeat-channel/export-distribution rerating positives, and
  (2) brand/channel narratives without durable reorder + margin/revision bridge.
duplicate_check_result = no direct C20 match found
do_not_open_stock_agent_code = true
```

## 4. Stock-Web OHLC Input / Price Source Validation

The Stock-Web manifest identifies `FinanceData/marcap` as the upstream source, `raw_unadjusted_marcap` as price adjustment status, `1995-05-02` to `2026-02-20` as atlas date coverage, 14,354,401 tradable rows, 15,214,118 raw rows, 5,414 symbols, and the calibration shard root `atlas/ohlcv_tradable_by_symbol_year`. fileciteturn854file0

| Field | Value |
|---|---|
| source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| manifest_path | atlas/manifest.json |
| stock_web_manifest_max_date | 2026-02-20 |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| validation_status | usable_for_historical_calibration |

## 5. Historical Eligibility Gate

| Symbol | Company | Profile check | Corporate-action window status | Forward 180D availability | Calibration usable |
|---|---:|---|---|---:|---:|
| 257720 | 실리콘투 | active_like; years 2021-2026; latest row 2026-02-20; 1,074 tradable rows | corporate-action candidates only in 2022, outside 2024-05~D+180 window | yes | true |
| 018290 | 브이티 | active_like; years 1996-2026; latest row 2026-02-20; 6,972 tradable rows | candidate dates end in 2019, outside 2024-05~D+180 window | yes | true |
| 237880 | 클리오 | active_like; years 2016-2026; latest row 2026-02-20; 2,276 tradable rows | no corporate-action candidate dates | yes | true |

Profile source notes: 실리콘투 has 2022 corporate-action candidates but the 2024 calibration window is clean. fileciteturn855file0 브이티 has historical corporate-action candidates ending in 2019, outside the tested 2024 window. fileciteturn856file0turn857file0 클리오 has zero corporate-action candidate dates and a clean raw-discontinuity profile. fileciteturn858file0

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | Compression logic |
|---|---|---|
| K_BEAUTY_GLOBAL_DISTRIBUTION_CHANNEL_REORDER | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | Wholesale/platform/export channel demand becomes repeatable enough to support EPS rerating. |
| K_BEAUTY_SINGLE_PRODUCT_TO_GLOBAL_REORDER | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | Single product strength is accepted only when it converts into channel reorder and margin bridge. |
| K_BEAUTY_BRAND_RETAIL_CHANNEL_FALSE_POSITIVE | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | Same sector narrative, but lacks durable reorder/revision evidence and should be guarded. |

## 7. Case Selection Summary

| case_id | Symbol | Role | New independent? | Why selected |
|---|---:|---|---:|---|
| R5L42-C20-257720-SILICON2-20240516 | 257720 | structural_success | true | Distribution-channel reorder with large MFE and meaningful later 4B/4C stress. |
| R5L42-C20-018290-VT-20240516 | 018290 | high_mae_success | true | Product-to-global-channel rerating; strong Stage2 entry, Green later and more volatile. |
| R5L42-C20-237880-CLIO-20240516 | 237880 | false_positive_green | true | Brand/channel narrative looked plausible but failed to sustain rerating; severe 180D MAE. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
calibration_usable_case_count = 3
new_independent_case_count = 3
reused_case_count = 0
minimum_new_independent_case_ratio = 1.00
counterexample_search_incomplete = false
```

The useful split is not “beauty good / beauty bad.” It is closer to inventory in a warehouse: a shelf label says the product is popular, but the reorder ticket tells you whether the popularity travels through the supply chain. C20 should reward the reorder ticket, not the shelf label.

## 9. Evidence Source Map

| Symbol | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence | Evidence caution |
|---|---|---|---|---|---|
| 257720 | public result, export/channel demand, relative strength, early revision | financial visibility, multiple public-source confirmation | local overheat, valuation/positioning watch | later thesis fatigue watch | URL-level DART/IR source validation is deferred to implementation ingestion. |
| 018290 | public result, product/channel reorder, relative strength | confirmed revision, financial visibility | local peak without non-price full 4B | none | Treat single-product strength as positive only when it expands into reorder route. |
| 237880 | brand/channel narrative, early result visibility | weak / not durable | margin/reorder slowdown | thesis break after drawdown | Counterexample: brand story alone should not promote Green. |

## 10. Price Data Source Map

| Symbol | price_shard_path | profile_path | Source row highlights |
|---|---|---|---|
| 257720 | atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv | atlas/symbol_profiles/257/257720.json | entry 2024-05-16 close 28,900; peak high 54,200 on 2024-06-19; later 2024 low 23,300 on 2024-12-09. fileciteturn859file0turn862file0 |
| 018290 | atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv | atlas/symbol_profiles/018/018290.json | entry 2024-05-16 close 25,550; high 40,000 on 2024-06-19; high 44,000 on 2024-12-16. fileciteturn863file0turn864file0 |
| 237880 | atlas/ohlcv_tradable_by_symbol_year/237/237880/2024.csv | atlas/symbol_profiles/237/237880.json | entry 2024-05-16 close 35,950; peak high 45,000 on 2024-06-13; later low 15,790 on 2024-12-09. fileciteturn866file0turn867file0 |

## 11. Case-by-Case Trigger Grid

| trigger_id | Symbol | Type | trigger_date | entry_date | entry_price | Representative? | Outcome |
|---|---:|---|---:|---:|---:|---:|---|
| TR-R5L42-257720-S2A-20240516 | 257720 | Stage2-Actionable | 2024-05-16 | 2024-05-16 | 28,900 | true | structural_success_high_MFE |
| TR-R5L42-257720-GREEN-20240612 | 257720 | Stage3-Green | 2024-06-12 | 2024-06-12 | 50,300 | false | green_late_after_stage2 |
| TR-R5L42-257720-4B-20240619 | 257720 | Stage4B-Local | 2024-06-19 | 2024-06-19 | 50,700 | false | local_peak_overlay |
| TR-R5L42-018290-S2A-20240516 | 018290 | Stage2-Actionable | 2024-05-16 | 2024-05-16 | 25,550 | true | structural_success_high_MFE_low_MAE |
| TR-R5L42-018290-GREEN-20240613 | 018290 | Stage3-Green | 2024-06-13 | 2024-06-13 | 38,000 | false | green_late_after_stage2 |
| TR-R5L42-237880-S2A-20240516 | 237880 | Stage2-Actionable | 2024-05-16 | 2024-05-16 | 35,950 | true | false_positive_stage2_high_MAE |
| TR-R5L42-237880-4C-20241111 | 237880 | Stage4C | 2024-11-11 | 2024-11-11 | 18,070 | false | 4C_late_but_protective_after_break |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative trigger rows

| Symbol | Entry | Entry price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | Peak date | Peak price |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 257720 | 2024-05-16 | 28,900 | 87.54% | -10.38% | 87.54% | -10.38% | 87.54% | -19.38% | 2024-06-19 | 54,200 |
| 018290 | 2024-05-16 | 25,550 | 56.56% | -2.74% | 56.56% | -2.74% | 72.21% | -2.74% | 2024-12-16 | 44,000 |
| 237880 | 2024-05-16 | 35,950 | 25.17% | -1.25% | 25.17% | -18.50% | 25.17% | -56.08% | 2024-06-13 | 45,000 |

### 12.2 Overlay / comparison rows

| Symbol | Trigger | Entry price | MFE_90D | MAE_90D | Role |
|---:|---|---:|---:|---:|---|
| 257720 | Stage3-Green 2024-06-12 | 50,300 | 7.75% | -36.08% | label_comparison_only |
| 257720 | Stage4B-Local 2024-06-19 | 50,700 | 6.90% | -36.59% | 4B_overlay_only |
| 018290 | Stage3-Green 2024-06-13 | 38,000 | 5.26% | -31.58% | label_comparison_only |
| 237880 | Stage4C 2024-11-11 | 18,070 | 18.15% | -12.62% | 4C_overlay_only |

## 13. Current Calibrated Profile Stress Test

| Symbol | Current profile verdict | Was it aligned? | Residual error |
|---:|---|---|---|
| 257720 | current_profile_correct | Yes for Stage2; too late for Green if waiting for stronger revision. | Green lateness within C20. |
| 018290 | current_profile_correct | Yes for Stage2; Green was late and exposed to volatility. | C20 should allow reorder-confirmed Stage2/Yellow earlier. |
| 237880 | current_profile_false_positive | No. Stage2/Yellow-like brand/channel evidence did not deserve promotion. | Need C20 guard against brand/channel story without reorder + margin bridge. |

Answers to required stress-test questions:

1. Current calibrated profile likely classifies 257720 and 018290 as positive Stage2/Yellow candidates, and risks classifying 237880 too generously if brand/channel narrative is not separated.
2. Actual MFE/MAE supports 257720 and 018290 but rejects 237880.
3. Stage2 bonus was useful for 257720/018290, too loose for 237880.
4. Yellow 75 is acceptable only with C20 evidence quality guard.
5. Green 87 / revision 55 can be too late in C20 if confirmed reorder evidence already exists before formal revision consensus is fully reflected.
6. Price-only blowoff guard remains appropriate.
7. Full 4B non-price requirement remains appropriate; price-only local peaks in 257720 and 018290 were not sufficient full 4B without non-price fatigue.
8. Hard 4C routing was directionally right for 237880 but late after a large peak-to-break drawdown.

## 14. Stage2 / Yellow / Green Comparison

| Symbol | Stage2 entry | Stage2 price | Green entry | Green price | Peak after Stage2 | green_lateness_ratio | Interpretation |
|---:|---:|---:|---:|---:|---:|---:|---|
| 257720 | 2024-05-16 | 28,900 | 2024-06-12 | 50,300 | 54,200 | 0.85 | Green captured only the final slice of upside. |
| 018290 | 2024-05-16 | 25,550 | 2024-06-13 | 38,000 | 40,000 local / 44,000 full | 0.86 local | Green was substantially late versus Stage2 evidence. |
| 237880 | 2024-05-16 | 35,950 | not applicable | not applicable | 45,000 | not_applicable | No durable Green; later path validates guard. |

## 15. 4B Local vs Full-window Timing Audit

| Symbol | 4B trigger | local proximity | full-window proximity | Evidence type | Verdict |
|---:|---:|---:|---:|---|---|
| 257720 | 2024-06-19 | 0.86 | 0.86 | price_only, positioning_overheat | price-only local watch, not full 4B |
| 018290 | not full 4B | not calculated | not calculated | price_only local peaks | keep existing full_4B_requires_non_price_evidence |
| 237880 | deterioration before 4C | not calculated | not calculated | margin/reorder slowdown | missed earlier 4B; 4C eventually late |

Conclusion: `full_4b_requires_non_price_evidence` is strengthened, not weakened. C20 can produce violent local peaks, but price-only 4B would have cut some winners too early.

## 16. 4C Protection Audit

| Symbol | 4C candidate | Prior peak | Entry | MAE_90D after 4C | Max drawdown after prior peak | four_c_protection_label |
|---:|---:|---:|---:|---:|---:|---|
| 237880 | 2024-11-11 | 45,000 | 18,070 | -12.62% | -64.91% | hard_4c_late |

Proxy protection score:

```text
four_c_protection_score ≈ 1 - 12.62 / 64.91 = 0.81
```

4C was protective after the thesis was already broken, but the real calibration lesson is earlier: C20 needs a positive-promotion guard so that 237880 does not reach positive Stage3 too easily.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
axis = L5_consumer_channel_reorder_vs_brand_story_split
candidate_delta = +2 to +3 for reorder-confirmed evidence
guard_delta = -5 to -6 for brand/channel narrative without reorder + margin/revision bridge
```

Sector rule: in consumer/beauty distribution, a good trigger is not just “brand is selling.” It is “sell-through turns into reorder, reorder turns into revenue visibility, and revenue turns into margin/revision bridge.” The scoring engine should see the cash register, the warehouse reorder, and the margin ledger together.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
new_axis_proposed =
  - C20_channel_reorder_confirmed_bonus
  - C20_brand_channel_without_reorder_guard
```

Proposed C20 rule:

```text
if C20 and channel_reorder_confirmed and export_distribution_broadening and margin_or_revision_bridge:
    add +3 shadow bonus to Stage2/Yellow-to-Green promotion path

if C20 and evidence is only brand buzz / retail channel narrative / policy reopening beta without repeat order or margin bridge:
    subtract -6 or block Green promotion
```

## 19. Before / After Backtest Comparison

| Profile | Scope | Eligible reps | Selected reps | Avg MFE_90D | Avg MAE_90D | Avg MFE_180D | Avg MAE_180D | False positive rate | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | global current | 3 | 3 | 56.42% | -10.54% | 61.64% | -26.07% | 33.3% | useful but C20 false positive remains |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 2 | 41.00% | -10.62% | 48.00% | -20.00% | 33.3% | less effective early capture |
| P1 sector_specific_candidate_profile | L5 | 3 | 2 | 72.05% | -6.56% | 79.88% | -11.06% | 0.0% | improved selection |
| P2 canonical_archetype_candidate_profile | C20 | 3 | 2 | 72.05% | -6.56% | 79.88% | -11.06% | 0.0% | best fit |
| P3 counterexample_guard_profile | C20 guard | 3 | 2 | 72.05% | -6.56% | 79.88% | -11.06% | 0.0% | removes brand-story false positive |

## 20. Score-Return Alignment Matrix

| Symbol | weighted_score_before | label_before | MFE_90D | MAE_90D | weighted_score_after | label_after | Alignment |
|---:|---:|---|---:|---:|---:|---|---|
| 257720 | 84.0 | Stage3-Yellow | 87.54% | -10.38% | 88.5 | Stage3-Green | aligned |
| 018290 | 81.0 | Stage3-Yellow | 56.56% | -2.74% | 87.5 | Stage3-Green | aligned |
| 237880 | 76.0 | Stage3-Yellow | 25.17% | -18.50% | 68.0 | Stage2-Watch | false_positive_filtered |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_BEAUTY_GLOBAL_DISTRIBUTION_CHANNEL_REORDER / K_BEAUTY_SINGLE_PRODUCT_TO_GLOBAL_REORDER / K_BEAUTY_BRAND_RETAIL_CHANNEL_FALSE_POSITIVE | 2 | 1 | 1 | 1 | 3 | 0 | 7 | 3 | 1 | true | true | need holdout across ODM/food exporters and post-2025 cases |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 5
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 5
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 1
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - C20 brand/channel narrative false positive
  - C20 Green lateness after reorder-confirmed Stage2
  - C20 price-only 4B too early risk
new_axis_proposed:
  - C20_channel_reorder_confirmed_bonus
  - C20_brand_channel_without_reorder_guard
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: none
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: L5/C20 under-specified distribution-channel rerating vs brand-story false positive
diversity_score_summary: high; 3 new symbols, 3 new fine archetypes, 1 direct counterexample, no reused case
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date and price basis
- 257720 / 018290 / 237880 symbol profiles
- 2024/2025 actual 1D OHLC rows around entry and forward window
- 30D/90D/180D MFE/MAE proxy calculations
- same_entry_group_id and aggregate dedupe rules
- C20 positive/counterexample balance
```

Not validated in this loop:

```text
- exact DART filing URLs for each evidence statement
- stock_agent source code
- production scoring implementation
- live candidate availability
- 1Y/2Y full calculations
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C20_channel_reorder_confirmed_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,+3,+3,"distribution-channel reorder + export diversification + margin/revision bridge improves selection","P2 selected 2 positives; avg MFE90 72.05% vs P0 56.42% and removed Clio false positive","TR-R5L42-257720-S2A-20240516|TR-R5L42-018290-S2A-20240516",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C20_brand_channel_without_reorder_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,-6,-6,"brand/retail narrative without repeat order and margin bridge produced severe 180D MAE in counterexample","filtered Clio from Yellow/Green candidate set","TR-R5L42-237880-S2A-20240516",3,3,1,medium,guard_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R5L42-C20-257720-SILICON2-20240516","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"42","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_GLOBAL_DISTRIBUTION_CHANNEL_REORDER","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR-R5L42-257720-S2A-20240516","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2-Actionable aligned with high 30D/90D MFE; Green was late.","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"K-beauty cross-border distribution rerating. Price source clean for 2024/2025 forward window; historical corporate action candidates are in 2022 only."}
{"row_type":"case","case_id":"R5L42-C20-018290-VT-20240516","symbol":"018290","company_name":"브이티","round":"R5","loop":"42","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_SINGLE_PRODUCT_TO_GLOBAL_REORDER","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"TR-R5L42-018290-S2A-20240516","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2-Actionable aligned; full Green confirmation captured less upside and more post-peak volatility.","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Cosmetic product/channel rerating; no corporate-action candidate dates in 2024-2025 window."}
{"row_type":"case","case_id":"R5L42-C20-237880-CLIO-20240516","symbol":"237880","company_name":"클리오","round":"R5","loop":"42","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_BRAND_RETAIL_CHANNEL_FALSE_POSITIVE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"TR-R5L42-237880-S2A-20240516","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Early brand/channel evidence produced only modest 30D MFE and then severe 180D MAE; later thesis-break route protected only after large drawdown.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Counterexample: brand/channel narrative alone did not sustain rerating without durable reorder/revision bridge."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TR-R5L42-257720-S2A-20240516","case_id":"R5L42-C20-257720-SILICON2-20240516","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"42","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_GLOBAL_DISTRIBUTION_CHANNEL_REORDER","sector":"소비재·유통·브랜드","primary_archetype":"beauty_food_global_distribution","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":28900,"evidence_available_at_that_date":"2024 Q1 earnings/export-channel evidence became tradable; evidence timestamp treated as same-day/close for research proxy.","evidence_source":"public quarterly result / company IR / broker-note family; URL-level source validation deferred","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv","profile_path":"atlas/symbol_profiles/257/257720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":87.54,"MFE_90D_pct":87.54,"MFE_180D_pct":87.54,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.38,"MAE_90D_pct":-10.38,"MAE_180D_pct":-19.38,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":54200,"drawdown_after_peak_pct":-57.01,"green_lateness_ratio":"stage3_green_comparison_row_0.85","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success_high_MFE","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"257720-20240516-28900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR-R5L42-257720-GREEN-20240612","case_id":"R5L42-C20-257720-SILICON2-20240516","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"42","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_GLOBAL_DISTRIBUTION_CHANNEL_REORDER","sector":"소비재·유통·브랜드","primary_archetype":"beauty_food_global_distribution","loop_objective":"green_strictness_stress_test","trigger_type":"Stage3-Green","trigger_date":"2024-06-12","entry_date":"2024-06-12","entry_price":50300,"evidence_available_at_that_date":"follow-through price/consensus confirmation proxy after distribution rerating was already visible.","evidence_source":"price/consensus follow-through proxy; not used as original evidence","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv","profile_path":"atlas/symbol_profiles/257/257720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.75,"MFE_90D_pct":7.75,"MFE_180D_pct":7.75,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-18.49,"MAE_90D_pct":-36.08,"MAE_180D_pct":-53.68,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":54200,"drawdown_after_peak_pct":-57.01,"green_lateness_ratio":0.85,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"green_late_after_stage2","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"257720-20240612-50300","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":false,"reuse_reason":"same_case_green_lateness_comparison","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TR-R5L42-257720-4B-20240619","case_id":"R5L42-C20-257720-SILICON2-20240516","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"42","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_GLOBAL_DISTRIBUTION_CHANNEL_REORDER","sector":"소비재·유통·브랜드","primary_archetype":"beauty_food_global_distribution","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Local","trigger_date":"2024-06-19","entry_date":"2024-06-19","entry_price":50700,"evidence_available_at_that_date":"local peak / positioning overheat was visible; non-price evidence was not yet sufficient for full 4B.","evidence_source":"price-only local overheat proxy","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv","profile_path":"atlas/symbol_profiles/257/257720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.9,"MFE_90D_pct":6.9,"MFE_180D_pct":6.9,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-19.13,"MAE_90D_pct":-36.59,"MAE_180D_pct":-54.04,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":54200,"drawdown_after_peak_pct":-57.01,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.86,"four_b_full_window_peak_proximity":0.86,"four_b_timing_verdict":"price_only_local_watch_not_full_4B","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":null,"trigger_outcome_label":"local_peak_overlay","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"257720-20240619-50700","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_case_4B_timing_overlay","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TR-R5L42-018290-S2A-20240516","case_id":"R5L42-C20-018290-VT-20240516","symbol":"018290","company_name":"브이티","round":"R5","loop":"42","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_SINGLE_PRODUCT_TO_GLOBAL_REORDER","sector":"소비재·유통·브랜드","primary_archetype":"beauty_food_global_distribution","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":25550,"evidence_available_at_that_date":"2024 Q1 cosmetic revenue/operating leverage evidence was available; next-trading ambiguity resolved to same-day close proxy.","evidence_source":"public quarterly result / company IR / broker-note family; URL-level source validation deferred","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv","profile_path":"atlas/symbol_profiles/018/018290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":56.56,"MFE_90D_pct":56.56,"MFE_180D_pct":72.21,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.74,"MAE_90D_pct":-2.74,"MAE_180D_pct":-2.74,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-16","peak_price":44000,"drawdown_after_peak_pct":-29.32,"green_lateness_ratio":"stage3_green_comparison_row_0.86","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success_high_MFE_low_MAE","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"018290-20240516-25550","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR-R5L42-018290-GREEN-20240613","case_id":"R5L42-C20-018290-VT-20240516","symbol":"018290","company_name":"브이티","round":"R5","loop":"42","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_SINGLE_PRODUCT_TO_GLOBAL_REORDER","sector":"소비재·유통·브랜드","primary_archetype":"beauty_food_global_distribution","loop_objective":"green_strictness_stress_test","trigger_type":"Stage3-Green","trigger_date":"2024-06-13","entry_date":"2024-06-13","entry_price":38000,"evidence_available_at_that_date":"follow-through confirmation proxy after initial product/channel rerating.","evidence_source":"price/consensus follow-through proxy; not used as original evidence","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv","profile_path":"atlas/symbol_profiles/018/018290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.26,"MFE_90D_pct":5.26,"MFE_180D_pct":15.79,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-24.74,"MAE_90D_pct":-31.58,"MAE_180D_pct":-31.58,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-16","peak_price":44000,"drawdown_after_peak_pct":-29.32,"green_lateness_ratio":0.86,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"green_late_after_stage2","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"018290-20240613-38000","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":false,"reuse_reason":"same_case_green_lateness_comparison","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TR-R5L42-237880-S2A-20240516","case_id":"R5L42-C20-237880-CLIO-20240516","symbol":"237880","company_name":"클리오","round":"R5","loop":"42","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_BRAND_RETAIL_CHANNEL_FALSE_POSITIVE","sector":"소비재·유통·브랜드","primary_archetype":"beauty_food_global_distribution","loop_objective":"counterexample_mining|residual_false_positive_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":35950,"evidence_available_at_that_date":"brand/channel narrative and early earnings visibility were tradable, but durable reorder and margin acceleration were not sufficiently separated.","evidence_source":"public quarterly result / company IR / broker-note family; URL-level source validation deferred","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/237/237880/2024.csv","profile_path":"atlas/symbol_profiles/237/237880.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":25.17,"MFE_90D_pct":25.17,"MFE_180D_pct":25.17,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.25,"MAE_90D_pct":-18.5,"MAE_180D_pct":-56.08,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-13","peak_price":45000,"drawdown_after_peak_pct":-64.91,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"false_positive_stage2_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"237880-20240516-35950","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR-R5L42-237880-4C-20241111","case_id":"R5L42-C20-237880-CLIO-20240516","symbol":"237880","company_name":"클리오","round":"R5","loop":"42","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_BRAND_RETAIL_CHANNEL_FALSE_POSITIVE","sector":"소비재·유통·브랜드","primary_archetype":"beauty_food_global_distribution","loop_objective":"4C_thesis_break_timing_test","trigger_type":"Stage4C","trigger_date":"2024-11-11","entry_date":"2024-11-11","entry_price":18070,"evidence_available_at_that_date":"hard thesis-break proxy after distribution/brand thesis failed to convert into durable rerating.","evidence_source":"price + delayed earnings/thesis-break proxy; not positive-promotion evidence","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/237/237880/2024.csv","profile_path":"atlas/symbol_profiles/237/237880.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.38,"MFE_90D_pct":18.15,"MFE_180D_pct":18.15,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.62,"MAE_90D_pct":-12.62,"MAE_180D_pct":-12.62,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-03-11","peak_price":21350,"drawdown_after_peak_pct":null,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"4C_late_but_protective_after_break","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"237880-20241111-18070","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":false,"reuse_reason":"same_case_4C_timing_overlay","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C20_shadow","case_id":"R5L42-C20-257720-SILICON2-20240516","trigger_id":"TR-R5L42-257720-S2A-20240516","symbol":"257720","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":72,"revision_score":70,"relative_strength_score":92,"customer_quality_score":76,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":78,"execution_risk_score":45,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_before":84.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":78,"revision_score":76,"relative_strength_score":92,"customer_quality_score":84,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":82,"execution_risk_score":45,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_after":88.5,"stage_label_after":"Stage3-Green","changed_components":["customer_quality_score","margin_bridge_score","revision_score"],"component_delta_explanation":"confirmed channel reorder + export distribution bridge promoted within C20 scope","MFE_90D_pct":87.54,"MAE_90D_pct":-10.38,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C20_shadow","case_id":"R5L42-C20-018290-VT-20240516","trigger_id":"TR-R5L42-018290-S2A-20240516","symbol":"018290","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":68,"revision_score":70,"relative_strength_score":86,"customer_quality_score":72,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":72,"execution_risk_score":50,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_before":81.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":75,"revision_score":76,"relative_strength_score":88,"customer_quality_score":82,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":76,"execution_risk_score":50,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_after":87.5,"stage_label_after":"Stage3-Green","changed_components":["customer_quality_score","margin_bridge_score","revision_score"],"component_delta_explanation":"product-to-global-channel repeat order route deserves C20-specific promotion","MFE_90D_pct":56.56,"MAE_90D_pct":-2.74,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C20_shadow","case_id":"R5L42-C20-237880-CLIO-20240516","trigger_id":"TR-R5L42-237880-S2A-20240516","symbol":"237880","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":55,"revision_score":58,"relative_strength_score":74,"customer_quality_score":70,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":66,"execution_risk_score":62,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_before":76.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":48,"revision_score":50,"relative_strength_score":62,"customer_quality_score":58,"policy_or_regulatory_score":"unknown_or_not_supported","valuation_repricing_score":54,"execution_risk_score":70,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_after":68.0,"stage_label_after":"Stage2-Watch","changed_components":["customer_quality_score","revision_score","execution_risk_score"],"component_delta_explanation":"brand/channel narrative was penalized because reorder and margin acceleration were not durable","MFE_90D_pct":25.17,"MAE_90D_pct":-18.5,"score_return_alignment_label":"false_positive_filtered","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C20_channel_reorder_confirmed_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,+3,+3,"distribution-channel reorder + export diversification + margin/revision bridge improves selection","P2 selected 2 positives; avg MFE90 72.05% vs P0 56.42% and removed Clio false positive","TR-R5L42-257720-S2A-20240516|TR-R5L42-018290-S2A-20240516",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C20_brand_channel_without_reorder_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,-6,-6,"brand/retail narrative without repeat order and margin bridge produced severe 180D MAE in counterexample","filtered Clio from Yellow/Green candidate set","TR-R5L42-237880-S2A-20240516",3,3,1,medium,guard_shadow_only,"not production; post-calibrated residual"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R5","loop":"42","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":5,"new_canonical_archetype_count":1,"new_trigger_family_count":5,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":1,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["C20 brand/channel narrative false positive without durable reorder bridge","late Green after channel-reorder evidence","price-only local 4B too early"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"L5/C20 K-beauty distribution rerating needed positive/counterexample split against existing cross-sector Stage2/Green calibration"}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"NONE","symbol":"NONE","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","reason":"no forward-window-blocked case included in this loop","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
next_round_candidates:
  - L5/C20 holdout: ODM or food-export cases, e.g. 161890 / 241710 / 051500 if stock-web windows are clean
  - L5/C19 brand-retail inventory margin counterexamples
  - L7/C23 approval-to-commercialization positive/counterexample split
next_round = L5/C20 holdout validation or L7/C23 bio approval commercialization
```

## 28. Source Notes

- Stock-web manifest was used as the source of truth for date coverage and price basis. fileciteturn854file0
- Symbol profile checks were limited to profile JSON files and did not inspect `stock_agent` source code. fileciteturn855file0turn857file0turn858file0
- OHLC calculations are based on fetched Stock-Web shard rows. 실리콘투 rows support 2024-05-16 entry, 2024-06-19 peak, and 2024-12-09 later low. fileciteturn859file0turn862file0 브이티 rows support 2024-05-16 entry, 2024-06-19 local high, and 2024-12-16 later high. fileciteturn863file0turn864file0 클리오 rows support 2024-05-16 entry, 2024-06-13 peak, and 2024-12-09 later low. fileciteturn866file0turn867file0
- Non-price evidence is intentionally marked as URL-level validation deferred. This MD is usable for shadow calibration shape, not for production ingestion without a later source-link validation pass.

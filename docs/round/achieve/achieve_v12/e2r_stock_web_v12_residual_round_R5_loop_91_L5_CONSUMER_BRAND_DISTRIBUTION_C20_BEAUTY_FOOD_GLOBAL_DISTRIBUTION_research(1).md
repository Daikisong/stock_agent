# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R5
scheduled_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_GLOBAL_CHANNEL_REORDER_BRIDGE_VS_LUXURY_CHINA_RECOVERY_AND_FOOD_GLOBAL_MARGIN_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R5_loop_91_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
```

This file is the corrected final output for this execution. The actual scheduler state after R4 loop 91 is R5 / loop 91. It fills the C20 beauty/food global distribution archetype with a K-beauty global-channel positive, a luxury/China recovery false Stage2, and a global food margin/distribution 4B event-cap row.

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
scheduled_loop = 91
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
round_sector_consistency = pass
computed_next_round = R6
computed_next_loop = 91
```

R5 permits L5 consumer / brand / distribution research. Previous R5 loop 89 used C18, loop 90 used C19, and earlier C20 rows used other symbols. This loop returns to C20 with a fresh symbol set.

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
previous R5 loop-89 C18 symbols avoided: 018290, 078520, 123690
previous R5 loop-90 C19 symbols avoided: 036620, 031430, 366030
previous R4 loop-91 C17 symbols avoided: 010060, 007690, 298000
```

Selected rows avoid hard duplicates and top repeated C20 symbols:

```text
090430 / Stage2-Actionable / 2024-04-11
051900 / Stage2-Actionable / 2024-05-10
097950 / Stage4B / 2024-06-26
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
| 090430 | atlas/symbol_profiles/090/090430.json | selected 2024 window clean after 2015 CA candidate |
| 051900 | atlas/symbol_profiles/051/051900.json | no corporate-action candidate |
| 097950 | atlas/symbol_profiles/097/097950.json | no corporate-action candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R5L91_C20_AMOREPACIFIC_2024_KBEAUTY_GLOBAL_CHANNEL_REORDER_POSITIVE | 090430 | 2024-04-11 | yes | 180 | yes | yes | true |
| R5L91_C20_LGHNH_2024_LUXURY_CHINA_RECOVERY_FALSE_STAGE2 | 051900 | 2024-05-10 | yes | 180 | yes | yes | true |
| R5L91_C20_CJFOOD_2024_GLOBAL_FOOD_MARGIN_DISTRIBUTION_EVENT_CAP_4B | 097950 | 2024-06-26 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_BEAUTY_GLOBAL_CHANNEL_REORDER_BRIDGE | Positive Stage2 requires overseas sell-through, reorder, distribution expansion, margin, and revision bridge. |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | LUXURY_CHINA_RECOVERY_FALSE_STAGE2 | Luxury/China recovery label without reorder/margin bridge can become false Stage2. |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | FOOD_GLOBAL_MARGIN_DISTRIBUTION_EVENT_CAP_4B | Global food distribution premium should route to 4B when margin bridge is capped or unverified. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R5L91_C20_AMOREPACIFIC_2024_KBEAUTY_GLOBAL_CHANNEL_REORDER_POSITIVE | 090430 | 아모레퍼시픽 | positive | K-beauty overseas channel/reorder bridge produced high MFE with controlled early MAE. |
| R5L91_C20_LGHNH_2024_LUXURY_CHINA_RECOVERY_FALSE_STAGE2 | 051900 | LG생활건강 | counterexample | Luxury/China recovery spike had almost no forward MFE and deep MAE. |
| R5L91_C20_CJFOOD_2024_GLOBAL_FOOD_MARGIN_DISTRIBUTION_EVENT_CAP_4B | 097950 | CJ제일제당 | counterexample / 4B | Global food distribution/margin premium capped near the June spike. |

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
| AmorePacific K-beauty reorder bridge | historical public/report proxy | true | true | shadow-only positive |
| LG H&H luxury/China recovery false Stage2 | historical public/report proxy | true | true | false-Stage2 guardrail |
| CJ CheilJedang food distribution cap | historical public/report proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 090430 | atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv | atlas/symbol_profiles/090/090430.json |
| 051900 | atlas/ohlcv_tradable_by_symbol_year/051/051900/2024.csv; 2025.csv | atlas/symbol_profiles/051/051900.json |
| 097950 | atlas/ohlcv_tradable_by_symbol_year/097/097950/2024.csv; 2025.csv | atlas/symbol_profiles/097/097950.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R5L91_C20_AMOREPACIFIC_2024_STAGE2_ACTIONABLE_KBEAUTY_GLOBAL_CHANNEL_REORDER | 090430 | Stage2-Actionable | 2024-04-11 | 127400 | positive | K-beauty channel/reorder bridge worked |
| R5L91_C20_LGHNH_2024_STAGE2_FALSE_POSITIVE_LUXURY_CHINA_RECOVERY | 051900 | Stage2-Actionable | 2024-05-10 | 466000 | counterexample | luxury/China recovery false Stage2 |
| R5L91_C20_CJFOOD_2024_STAGE4B_GLOBAL_FOOD_MARGIN_DISTRIBUTION_CAP | 097950 | Stage4B | 2024-06-26 | 398000 | counterexample/4B | global food margin/distribution event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R5L91_C20_AMOREPACIFIC_2024_STAGE2_ACTIONABLE_KBEAUTY_GLOBAL_CHANNEL_REORDER | 127400 | 51.49 | -3.06 | 57.38 | -9.03 | 57.38 | -9.03 | 2024-05-31 | 200500 | -42.19 |
| R5L91_C20_LGHNH_2024_STAGE2_FALSE_POSITIVE_LUXURY_CHINA_RECOVERY | 466000 | 3.00 | -22.85 | 3.00 | -31.97 | 3.00 | -41.42 | 2024-05-23 | 480000 | -43.13 |
| R5L91_C20_CJFOOD_2024_STAGE4B_GLOBAL_FOOD_MARGIN_DISTRIBUTION_CAP | 398000 | 2.39 | -15.83 | 2.39 | -31.41 | 2.39 | -31.41 | 2024-06-26 | 407500 | -33.01 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C20 Stage2 needs global channel reorder / sell-through / margin / revision bridge |
| local_4b_watch_guard | strengthen: beauty/food recovery premiums should route to 4B watch when bridge is missing |
| high_MAE_guardrail | strengthen: high-MAE channel recovery spikes cannot promote without durable bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is global-channel conversion quality:

| symbol | stage quality | explanation |
|---|---|---|
| 090430 | good_stage2 | K-beauty overseas channel/reorder bridge produced high MFE. |
| 051900 | bad_stage2 | Luxury/China recovery label had low forward MFE and high MAE. |
| 097950 | good_4B | Food distribution/margin premium capped near the June spike. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 051900 luxury/China false Stage2 | 0.97 | 0.97 | recovery spike was false Stage2 due missing reorder/margin bridge |
| 097950 food distribution cap | 1.00 | 1.00 | good full-window 4B timing |
| 090430 K-beauty reorder bridge | n/a | n/a | positive Stage2, but later K-beauty valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 051900 / 097950
```

No hard 4C candidate is proposed. R5 loop 91 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L5 beauty/food global distribution cases, Stage2 requires verified overseas channel sell-through, reorder, distribution expansion, pricing, raw-material cost pass-through, margin, or revision bridge. Beauty, China recovery, luxury, global food, or distribution label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
rule = C20 should split real global-channel reorder positives from luxury/China recovery false Stage2 and global food margin/distribution event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 20.92 | -24.14 | 0.67 | mixed; C20 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 20.92 | -24.14 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L5 global-channel bridge required | 2 | 30.19 | -20.50 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C20 bridge vs event-cap split | 2 | 30.19 | -20.50 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing beauty/food themes as positive | 1 | 57.38 | -9.03 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 090430 K-beauty bridge | 66 | Stage2-Watch | 75 | Stage2-Actionable | 57.38 | -9.03 | Kbeauty_global_channel_reorder_positive |
| 051900 luxury/China false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 3.00 | -31.97 | luxury_china_recovery_false_stage2 |
| 097950 global food cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 2.39 | -31.41 | global_food_margin_distribution_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_BRIDGE_VS_LUXURY_CHINA_RECOVERY_AND_FOOD_GLOBAL_MARGIN_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C20 K-beauty global channel reorder positive, luxury/China recovery false Stage2, and global food distribution margin event-cap 4B split using non-top-covered symbols."}
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
residual_error_types_found: Kbeauty_global_channel_reorder_positive, luxury_china_recovery_false_stage2, global_food_margin_distribution_event_cap_4B
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
- C20 beauty/food global distribution bridge vs event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,configured,C20_requires_global_channel_reorder_sellthrough_margin_revision_bridge,0,"C20 Stage2 should require overseas channel sell-through, reorder, distribution expansion, margin, or revision bridge, not beauty/food/global label alone","AmorePacific positive worked; LG H&H and CJ CheilJedang event/theme rows failed positive-stage promotion","R5L91_C20_AMOREPACIFIC_2024_STAGE2_ACTIONABLE_KBEAUTY_GLOBAL_CHANNEL_REORDER|R5L91_C20_LGHNH_2024_STAGE2_FALSE_POSITIVE_LUXURY_CHINA_RECOVERY|R5L91_C20_CJFOOD_2024_STAGE4B_GLOBAL_FOOD_MARGIN_DISTRIBUTION_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,configured,cap_luxury_china_and_food_distribution_event_premiums_as_4B_watch,0,"Beauty/food global distribution premiums can peak before reorder and margin bridge is proven","LG H&H had low forward MFE and deep MAE; CJ CheilJedang showed full-window event-cap behavior after June spike","R5L91_C20_LGHNH_2024_STAGE2_FALSE_POSITIVE_LUXURY_CHINA_RECOVERY|R5L91_C20_CJFOOD_2024_STAGE4B_GLOBAL_FOOD_MARGIN_DISTRIBUTION_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,configured,block_positive_stage_when_channel_recovery_has_high_MAE_without_reorder_margin_bridge,0,"High MAE after a beauty/food global channel recovery spike should block Stage2/Stage3 promotion unless reorder/margin evidence survives","LG H&H MAE90=-31.97 and CJ CheilJedang MAE90=-31.41","R5L91_C20_LGHNH_2024_STAGE2_FALSE_POSITIVE_LUXURY_CHINA_RECOVERY|R5L91_C20_CJFOOD_2024_STAGE4B_GLOBAL_FOOD_MARGIN_DISTRIBUTION_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R5L91_C20_AMOREPACIFIC_2024_KBEAUTY_GLOBAL_CHANNEL_REORDER_POSITIVE", "symbol": "090430", "company_name": "아모레퍼시픽", "round": "R5", "loop": "91", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_BRIDGE_VS_LUXURY_CHINA_RECOVERY_AND_FOOD_GLOBAL_MARGIN_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R5L91_C20_AMOREPACIFIC_2024_STAGE2_ACTIONABLE_KBEAUTY_GLOBAL_CHANNEL_REORDER", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "K-beauty global channel reorder / overseas distribution recovery bridge produced high 30D/90D MFE with controlled early MAE. C20 works when brand demand maps into channel sell-through, overseas reorder, margin, and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C20_positive_requires_global_channel_reorder_margin_revision_bridge_not_beauty_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2015 CA candidate. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R5L91_C20_LGHNH_2024_LUXURY_CHINA_RECOVERY_FALSE_STAGE2", "symbol": "051900", "company_name": "LG생활건강", "round": "R5", "loop": "91", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_BRIDGE_VS_LUXURY_CHINA_RECOVERY_AND_FOOD_GLOBAL_MARGIN_EVENT_CAP", "case_type": "failed_rerating_channel_recovery", "positive_or_counterexample": "counterexample", "best_trigger": "R5L91_C20_LGHNH_2024_STAGE2_FALSE_POSITIVE_LUXURY_CHINA_RECOVERY", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Luxury/China beauty-channel recovery premium had almost no forward MFE after the spike entry and then deep 90D/180D MAE. C20 Stage2 should not be awarded without actual reorder, sell-through, margin, and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_luxury_china_channel_recovery_counts_without_reorder_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action caveat in profile; source-proxy only."}
{"row_type": "case", "case_id": "R5L91_C20_CJFOOD_2024_GLOBAL_FOOD_MARGIN_DISTRIBUTION_EVENT_CAP_4B", "symbol": "097950", "company_name": "CJ제일제당", "round": "R5", "loop": "91", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_BRIDGE_VS_LUXURY_CHINA_RECOVERY_AND_FOOD_GLOBAL_MARGIN_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R5L91_C20_CJFOOD_2024_STAGE4B_GLOBAL_FOOD_MARGIN_DISTRIBUTION_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Global food distribution / margin recovery premium capped around the late-June spike and then drew down. C20 food distribution premium should route to 4B unless overseas volume, pricing, raw material cost, and margin/revision bridge continue.", "current_profile_verdict": "current_profile_4B_too_late_if_global_food_margin_distribution_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action caveat in profile; source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R5L91_C20_AMOREPACIFIC_2024_STAGE2_ACTIONABLE_KBEAUTY_GLOBAL_CHANNEL_REORDER", "case_id": "R5L91_C20_AMOREPACIFIC_2024_KBEAUTY_GLOBAL_CHANNEL_REORDER_POSITIVE", "symbol": "090430", "company_name": "아모레퍼시픽", "round": "R5", "loop": "91", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_BRIDGE_VS_LUXURY_CHINA_RECOVERY_AND_FOOD_GLOBAL_MARGIN_EVENT_CAP", "sector": "Kbeauty_global_channel_reorder", "primary_archetype": "global_channel_sellthrough_reorder_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-11", "entry_date": "2024-04-11", "entry_price": 127400.0, "evidence_available_at_that_date": "K-beauty global channel, overseas sell-through, reorder, margin and revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["Kbeauty_global_channel_recovery", "overseas_sellthrough_proxy", "reorder_bridge_proxy", "margin_revision_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["high_MFE30", "high_MFE90", "controlled_entry_MAE"], "stage4b_evidence_fields": ["valuation_watch_after_Kbeauty_channel_rerating"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv", "profile_path": "atlas/symbol_profiles/090/090430.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 51.49, "MFE_90D_pct": 57.38, "MFE_180D_pct": 57.38, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -3.06, "MAE_90D_pct": -9.03, "MAE_180D_pct": -9.03, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-31", "peak_price": 200500.0, "drawdown_after_peak_pct": -42.19, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_Kbeauty_valuation_watch_needed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "Kbeauty_channel_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_Kbeauty_global_channel_reorder_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2015_CA", "same_entry_group_id": "R5L91_C20_090430_2024-04-11_127400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R5L91_C20_LGHNH_2024_STAGE2_FALSE_POSITIVE_LUXURY_CHINA_RECOVERY", "case_id": "R5L91_C20_LGHNH_2024_LUXURY_CHINA_RECOVERY_FALSE_STAGE2", "symbol": "051900", "company_name": "LG생활건강", "round": "R5", "loop": "91", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_BRIDGE_VS_LUXURY_CHINA_RECOVERY_AND_FOOD_GLOBAL_MARGIN_EVENT_CAP", "sector": "luxury_beauty_China_channel_recovery", "primary_archetype": "luxury_china_recovery_without_reorder_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-10", "entry_date": "2024-05-10", "entry_price": 466000.0, "evidence_available_at_that_date": "luxury/China beauty channel recovery and brand normalization premium proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["luxury_china_channel_recovery", "brand_normalization_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_forward_MFE", "reorder_margin_revision_bridge_missing", "post_spike_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/051/051900/2024.csv|atlas/ohlcv_tradable_by_symbol_year/051/051900/2025.csv", "profile_path": "atlas/symbol_profiles/051/051900.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.0, "MFE_90D_pct": 3.0, "MFE_180D_pct": 3.0, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -22.85, "MAE_90D_pct": -31.97, "MAE_180D_pct": -41.42, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-23", "peak_price": 480000.0, "drawdown_after_peak_pct": -43.13, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.97, "four_b_full_window_peak_proximity": 0.97, "four_b_timing_verdict": "luxury_china_recovery_spike_was_false_stage2_due_missing_reorder_margin_bridge", "four_b_evidence_type": ["brand_recovery_premium", "positioning_overheat", "reorder_margin_bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_luxury_china_beauty_recovery_without_reorder_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_luxury_china_channel_recovery_counts_without_reorder_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L91_C20_051900_2024-05-10_466000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R5L91_C20_CJFOOD_2024_STAGE4B_GLOBAL_FOOD_MARGIN_DISTRIBUTION_CAP", "case_id": "R5L91_C20_CJFOOD_2024_GLOBAL_FOOD_MARGIN_DISTRIBUTION_EVENT_CAP_4B", "symbol": "097950", "company_name": "CJ제일제당", "round": "R5", "loop": "91", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_BRIDGE_VS_LUXURY_CHINA_RECOVERY_AND_FOOD_GLOBAL_MARGIN_EVENT_CAP", "sector": "global_food_distribution_margin", "primary_archetype": "food_global_distribution_margin_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-06-26", "entry_date": "2024-06-26", "entry_price": 398000.0, "evidence_available_at_that_date": "global food distribution / pricing and margin recovery premium after June spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["global_food_distribution_premium", "pricing_margin_recovery_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_forward_MFE", "raw_material_cost_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/097/097950/2024.csv|atlas/ohlcv_tradable_by_symbol_year/097/097950/2025.csv", "profile_path": "atlas/symbol_profiles/097/097950.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.39, "MFE_90D_pct": 2.39, "MFE_180D_pct": 2.39, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -15.83, "MAE_90D_pct": -31.41, "MAE_180D_pct": -31.41, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 407500.0, "drawdown_after_peak_pct": -33.01, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_global_food_margin_distribution_event_cap", "four_b_evidence_type": ["food_distribution_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_global_food_distribution_margin_premium", "current_profile_verdict": "current_profile_4B_too_late_if_global_food_margin_distribution_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L91_C20_097950_2024-06-26_398000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L91_C20_AMOREPACIFIC_2024_KBEAUTY_GLOBAL_CHANNEL_REORDER_POSITIVE", "trigger_id": "R5L91_C20_AMOREPACIFIC_2024_STAGE2_ACTIONABLE_KBEAUTY_GLOBAL_CHANNEL_REORDER", "symbol": "090430", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 55, "margin_bridge_score": 55, "revision_score": 50, "relative_strength_score": 70, "customer_quality_score": 45, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 75, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "Kbeauty_global_channel_reorder_positive", "MFE_90D_pct": 57.38, "MAE_90D_pct": -9.03, "score_return_alignment_label": "Kbeauty_global_channel_reorder_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L91_C20_LGHNH_2024_LUXURY_CHINA_RECOVERY_FALSE_STAGE2", "trigger_id": "R5L91_C20_LGHNH_2024_STAGE2_FALSE_POSITIVE_LUXURY_CHINA_RECOVERY", "symbol": "051900", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "luxury_china_recovery_false_stage2", "MFE_90D_pct": 3.0, "MAE_90D_pct": -31.97, "score_return_alignment_label": "luxury_china_recovery_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_luxury_china_channel_recovery_counts_without_reorder_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L91_C20_CJFOOD_2024_GLOBAL_FOOD_MARGIN_DISTRIBUTION_EVENT_CAP_4B", "trigger_id": "R5L91_C20_CJFOOD_2024_STAGE4B_GLOBAL_FOOD_MARGIN_DISTRIBUTION_CAP", "symbol": "097950", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "global_food_margin_distribution_event_cap_4B_guard", "MFE_90D_pct": 2.39, "MAE_90D_pct": -31.41, "score_return_alignment_label": "global_food_margin_distribution_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_global_food_margin_distribution_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": "91", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_BRIDGE_VS_LUXURY_CHINA_RECOVERY_AND_FOOD_GLOBAL_MARGIN_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["Kbeauty_global_channel_reorder_positive", "luxury_china_recovery_false_stage2", "global_food_margin_distribution_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
completed_loop = 91
next_round = R6
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.

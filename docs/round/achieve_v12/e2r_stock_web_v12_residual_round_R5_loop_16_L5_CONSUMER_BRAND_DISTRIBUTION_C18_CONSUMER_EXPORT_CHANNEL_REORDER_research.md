# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```json
{
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "output_file": "e2r_stock_web_v12_residual_round_R5_loop_16_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md",
  "scheduled_round": "R5",
  "scheduled_loop": 16,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R5",
  "completed_loop": 16,
  "computed_next_round": "R6",
  "computed_next_loop": 16,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
  "fine_archetype_id": "K_FOOD_EXPORT_REORDER_CHANNEL_SELL_THROUGH_GUARD",
  "loop_objective": [
    "coverage_gap_fill",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "counterexample_mining",
    "stage2_actionable_bonus_stress_test",
    "green_strictness_stress_test",
    "4B_non_price_requirement_stress_test"
  ],
  "price_source": "Songdaiki/stock-web",
  "stock_web_manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "new_independent_case_count": 4,
  "reused_case_count": 0,
  "new_symbol_count": 4,
  "same_archetype_new_symbol_count": 4,
  "same_archetype_new_trigger_family_count": 4,
  "new_trigger_family_count": 4,
  "calibration_usable_case_count": 4,
  "calibration_usable_trigger_count": 5,
  "positive_case_count": 2,
  "counterexample_count": 2,
  "current_profile_error_count": 4,
  "diversity_score_summary": "estimated +65; wrong_round_penalty=0; same_archetype_new_symbol_bonus=+16; counterexample_gap_bonus=+8; residual_error_bonus=+20; prior R5 C18 covered apparel/OEM, this loop adds K-food/export-channel symbols",
  "do_not_propose_new_weight_delta": false,
  "auto_selected_coverage_gap": "R5 prior local coverage is C20-heavy and the only C18 file used apparel/footwear OEM; this loop fills food/export-channel reorder coverage.",
  "sector_specific_rule_candidate": true,
  "canonical_archetype_rule_candidate": true,
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "new_axis_proposed": [
    "C18_verified_sell_through_reorder_bonus",
    "C18_unverified_restock_inventory_guard",
    "C18_margin_cost_offset_guard"
  ],
  "existing_axis_strengthened": [
    "price_only_blowoff_blocks_positive_stage",
    "full_4b_requires_non_price_evidence"
  ],
  "existing_axis_weakened": null
}
```

This loop adds **4** new independent cases, **2** counterexamples, and **4** residual errors for **R5/L5_CONSUMER_BRAND_DISTRIBUTION/C18_CONSUMER_EXPORT_CHANNEL_REORDER**.

No current/live candidate scan was performed. No stock_agent production scoring was changed. This is a standalone historical residual calibration file.

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

This loop does not re-propose the already applied global axes. It stress-tests them inside C18 and proposes only shadow, C18/L5-scoped adjustments.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R5 |
| scheduled_loop | 16 |
| round_schedule_status | valid |
| round_sector_consistency | pass |
| large_sector_id | L5_CONSUMER_BRAND_DISTRIBUTION |
| canonical_archetype_id | C18_CONSUMER_EXPORT_CHANNEL_REORDER |
| fine_archetype_id | K_FOOD_EXPORT_REORDER_CHANNEL_SELL_THROUGH_GUARD |
| allowed round-sector pair | R5 -> L5_CONSUMER_BRAND_DISTRIBUTION |
| selected canonical gap | C18_CONSUMER_EXPORT_CHANNEL_REORDER |

R5 consistency passes because the selected large sector is L5. The selected canonical archetype is C18 rather than C20 because prior local R5 outputs were C20-heavy and the single C18 file in the local ledger focused on apparel/footwear OEM, not K-food/export-channel reorder.

## 3. Previous Coverage / Duplicate Avoidance Check

| prior local R5 loop | canonical_archetype_id | observed theme | duplicate decision |
|---:|---|---|---|
| 10 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | beauty/food global distribution | avoid; C20 already repeated |
| 11 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | beauty/food global distribution | avoid |
| 12 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | apparel/footwear OEM reorder | same canonical allowed, but new symbols/family required |
| 13 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | beauty/food global distribution | avoid |
| 14 | C19_BRAND_RETAIL_INVENTORY_MARGIN | retail inventory/margin | not selected |
| 15 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | beauty/food global distribution | avoid |

New symbols used here are `003230`, `004370`, `271560`, and `097950`; none overlaps the prior C18 apparel/OEM symbols `105630`, `111770`, and `241590`. Therefore this is not schema rematerialization.

## 4. Stock-Web OHLC Input / Price Source Validation

| manifest field | checked value |
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

The manifest confirms raw/unadjusted OHLC and that zero-volume / invalid OHLC rows are excluded from the calibration shards. All forward-window judgments in this MD stop at manifest `max_date = 2026-02-20`.

Sampled OHLC rows used for anchor validation:

```text
003230 2023-11-15,210000.0,211500.0,194000.0,199600.0,...,KOSPI
003230 2024-06-19,695000.0,718000.0,651000.0,673000.0,...,KOSPI
004370 2020-03-17,252000.0,273000.0,251500.0,268000.0,...,KOSPI
004370 2020-05-18,330000.0,342000.0,323000.0,327000.0,...,KOSPI
271560 2021-08-18,116000.0,118000.0,115500.0,117500.0,...,KOSPI
271560 2021-09-15,127000.0,130000.0,125000.0,129500.0,...,KOSPI
097950 2021-08-09,482000.0,494500.0,480500.0,489500.0,...,KOSPI
097950 2021-10-06,398000.0,401500.0,391000.0,391000.0,...,KOSPI
```

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D forward window | corporate action window | calibration_usable | block reason |
|---|---:|---|---:|---|---|---|
| R5L16-C18-003230-20231115 | 003230 | 2023-11-15 | 180 | clean_180D_window | true | none |
| R5L16-C18-004370-20200317 | 004370 | 2020-03-17 | 180 | clean_180D_window | true | none |
| R5L16-C18-271560-20210818 | 271560 | 2021-08-18 | 180 | clean_180D_window | true | none |
| R5L16-C18-097950-20210809 | 097950 | 2021-08-09 | 180 | clean_180D_window | true | none |

All representative rows have at least 180 trading days available before the stock-web manifest max date. No representative 180D window overlaps symbol-profile corporate-action candidate dates.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression reason |
|---|---|---|
| K_FOOD_EXPORT_REORDER_CHANNEL_SELL_THROUGH_GUARD | C18_CONSUMER_EXPORT_CHANNEL_REORDER | K-food and packaged food cases are compressed into C18 because the relevant mechanism is export-channel sell-through -> reorder -> revision/margin conversion, not generic food popularity or brand halo. |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger family | new? | current profile verdict |
|---|---:|---|---|---|---|---|
| R5L16-C18-003230-20231115 | 003230 | 삼양식품 | positive / structural_success | export_sell_through_reorder_to_margin_revision | true | current_profile_missed_structural |
| R5L16-C18-004370-20200317 | 004370 | 농심 | positive / structural_success | demand_shock_reorder_sell_through | true | current_profile_too_late |
| R5L16-C18-271560-20210818 | 271560 | 오리온 | counterexample / failed_rerating | unverified_china_channel_restock_base_effect | true | current_profile_false_positive |
| R5L16-C18-097950-20210809 | 097950 | CJ제일제당 | counterexample / false_positive_green | global_food_channel_signal_margin_cost_offset | true | current_profile_false_positive |

The case set is intentionally balanced: two positive reorder-to-margin/revision cases and two counterexamples where channel or brand narrative was not enough.

## 8. Positive vs Counterexample Balance

| bucket | count | cases |
|---|---:|---|
| positive_structural_success | 2 | 삼양식품, 농심 |
| counterexample_or_failed_rerating | 2 | 오리온, CJ제일제당 |
| 4B_or_4C_case | 1 | 삼양식품 2024-06 local 4B overlay |
| calibration_usable_case_count | 4 | all representative rows |

## 9. Evidence Source Map

| trigger_id | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence | evidence timing note |
|---|---|---|---|---|---|
| R5L16-C18-003230-T1 | public_event_or_disclosure, customer_or_order_quality, relative_strength, capacity_or_volume_route, early_revision_signal | confirmed_revision, margin_bridge, multiple_public_sources, financial_visibility, repeat_order_or_conversion | - | - | Q3/export sell-through and reorder signal was visible enough to use the same-day close as a historical Stage2-Actionable |
| R5L16-C18-003230-T4B | - | confirmed_revision, financial_visibility | valuation_blowoff, positioning_overheat, price_only_local_peak | - | Post-rerating valuation/positioning overheat after multi-month export reorder success; this is an overlay row, not a new |
| R5L16-C18-004370-T1 | public_event_or_disclosure, customer_or_order_quality, capacity_or_volume_route, early_revision_signal | margin_bridge, financial_visibility, repeat_order_or_conversion | - | - | Demand shock, channel depletion and reorder visibility were tradable before full revision confirmation; same-day close i |
| R5L16-C18-271560-T1 | public_event_or_disclosure, customer_or_order_quality | - | margin_or_backlog_slowdown | - | Overseas/China channel restock narrative was visible, but sell-through duration and revision conversion were not strong  |
| R5L16-C18-097950-T1 | public_event_or_disclosure, customer_or_order_quality, policy_or_regulatory_optionality | - | margin_or_backlog_slowdown | - | Global packaged-food/K-food channel signal existed, but commodity/input-cost and non-channel margin risk offset the expo |

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | profile status | corporate action candidate status |
|---:|---|---|---|---|---|
| 003230 | 삼양식품 | atlas/ohlcv_tradable_by_symbol_year/003/003230/2023.csv | atlas/symbol_profiles/003/003230.json | active_like; tradable_ohlcv=7704; corporate_action_candidate_dates=[2003-07-25] | clean 180D window |
| 004370 | 농심 | atlas/ohlcv_tradable_by_symbol_year/004/004370/2020.csv | atlas/symbol_profiles/004/004370.json | active_like; tradable_ohlcv=7742; corporate_action_candidate_dates=[1997-05-08,1997-07-21,2000-07-28,2003-07-18] | clean 180D window |
| 271560 | 오리온 | atlas/ohlcv_tradable_by_symbol_year/271/271560/2021.csv | atlas/symbol_profiles/271/271560.json | active_like; tradable_ohlcv=2113; corporate_action_candidate_dates=[] | clean 180D window |
| 097950 | CJ제일제당 | atlas/ohlcv_tradable_by_symbol_year/097/097950/2021.csv | atlas/symbol_profiles/097/097950.json | active_like; tradable_ohlcv=4536; corporate_action_candidate_dates=[] | clean 180D window |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | type | trigger_date | entry_date | entry_price | outcome | current verdict | aggregate role |
|---|---|---|---|---|---:|---|---|---|
| R5L16-C18-003230-T1 | R5L16-C18-003230-20231115 | Stage2-Actionable | 2023-11-15 | 2023-11-15 | 199600 | structural_success_high_MFE_after_verified_channel_reorder | current_profile_missed_structural | representative |
| R5L16-C18-003230-T4B | R5L16-C18-003230-20231115 | Stage4B-Overlay | 2024-06-14 | 2024-06-14 | 647000 | 4B_overlay_success_local_risk_reduction_not_thesis_break | current_profile_4B_too_late | 4B_overlay_only |
| R5L16-C18-004370-T1 | R5L16-C18-004370-20200317 | Stage2-Actionable | 2020-03-17 | 2020-03-17 | 268000 | channel_reorder_positive_moderate_MFE | current_profile_too_late | representative |
| R5L16-C18-271560-T1 | R5L16-C18-271560-20210818 | Stage2-Actionable-candidate | 2021-08-18 | 2021-08-18 | 117500 | failed_rerating_restock_without_revision | current_profile_false_positive | representative |
| R5L16-C18-097950-T1 | R5L16-C18-097950-20210809 | Stage2-Actionable-candidate | 2021-08-09 | 2021-08-09 | 489500 | false_positive_green_margin_cost_offset | current_profile_false_positive | representative |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| R5L16-C18-003230-T1 | 199600 | 16.98 | -5.11 | 19.99 | -15.13 | 259.72 | -15.13 | 2024-06-19 | 718000 | -32.31 |
| R5L16-C18-003230-T4B | 647000 | 11.0 | -8.66 | 11.0 | -24.88 | 11.0 | -27.43 | 2024-06-19 | 718000 | -32.31 |
| R5L16-C18-004370-T1 | 268000 | 20.9 | -7.65 | 27.61 | -7.65 | 36.57 | -7.65 | 2020-05-18 | 342000 | -17.25 |
| R5L16-C18-271560-T1 | 117500 | 10.64 | -2.13 | 10.64 | -8.09 | 10.64 | -21.28 | 2021-09-15 | 130000 | -16.92 |
| R5L16-C18-097950-T1 | 489500 | 1.84 | -13.89 | 1.84 | -21.15 | 1.84 | -27.68 | 2021-08-10 | 498500 | -21.57 |

Representative aggregate inclusion uses only rows with `dedupe_for_aggregate=true` and `aggregate_group_role=representative`. The 4B row is overlay-only and excluded from MFE/MAE aggregate entry statistics.

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely label | actual MFE/MAE alignment | Stage2 bonus | Yellow 75 | Green 87/revision 55 | blowoff guard | 4B non-price | hard 4C | verdict |
|---|---|---|---|---|---|---|---|---|---|
| R5L16-C18-003230-20231115 | Yellow / slow Green | MFE_180D +259.72 means P0 under-promoted | 부족 | Yellow too conservative | Green too strict for verified reorder conversion | kept | kept | not needed | current_profile_missed_structural |
| R5L16-C18-004370-20200317 | Yellow / delayed | MFE_90D +27.61 with manageable MAE | 적절 but needs C18 nuance | slightly too late | Green too late for short-cycle reorder | kept | kept | not needed | current_profile_too_late |
| R5L16-C18-271560-20210818 | Yellow candidate | MFE capped and MAE worsened | 과함 if restock unverified | too permissive | should not Green | kept | kept | watch only | current_profile_false_positive |
| R5L16-C18-097950-20210809 | Yellow/possible Green narrative | MFE_90D +1.84, MAE_90D -21.15 | 과함 under margin offset | too permissive | should not Green | kept | kept | watch only | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 actionable price | Stage3 Green proxy price | peak_price | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|---|
| 003230 | 199600 | 360000 proxy after confirmed export-revision conversion | 718000 | 0.31 | Green moderately late but not useless; C18 promotion should occur only after sell-through+margin bridge. |
| 004370 | 268000 | 304000 proxy after short-cycle demand proof | 342000 | 0.49 | Green was late for a short-cycle consumer reorder. |
| 271560 | 117500 | n/a | 130000 | not_applicable | No confirmed Green trigger; restock failed to sustain. |
| 097950 | 489500 | n/a | 498500 | not_applicable | No valid Green; channel narrative was offset by margin/cost. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | evidence type | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| R5L16-C18-003230-T4B | valuation_blowoff, positioning_overheat | 0.863 | 0.464 | Local 4B was useful for risk reduction, but full-window cycle later extended; do not treat price-only local peak as full 4B without non-price overheat. |
| other triggers | none | n/a | n/a | no 4B overlay |

## 16. 4C Protection Audit

| case_id | 4C label | explanation |
|---|---|---|
| 003230 | thesis_break_watch_only | 4B risk overlay did not break export reorder thesis. |
| 004370 | not_applicable | short-cycle demand/order case; no hard thesis break. |
| 271560 | false_break | restock narrative weakened but not a clean hard 4C event. |
| 097950 | thesis_break_watch_only | margin/cost offset capped stage; not a forced 4C. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L5_C18_food_export_verified_reorder_sell_through_bonus
tested_delta = +4
guard_axis_1 = L5_C18_unverified_restock_inventory_guard
guard_delta_1 = -8
guard_axis_2 = L5_C18_margin_cost_offset_guard
guard_delta_2 = -12
proposal_type = shadow_weight_only
confidence = medium
```

Mechanism: consumer export-channel reorder behaves like water pressure in a pipe. A one-time restock only fills the pipe once; verified sell-through plus repeat orders means the pipe keeps pulling product through. The sector rule should reward the second condition, not the first.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
positive promotion requires: sell_through_duration >= 2 reporting periods OR repeat_order_conversion evidence, plus margin_bridge or revision signal
guard if: overseas restock/base-effect only, inventory rebuild without sell-through, or channel narrative offset by input-cost/margin risk
```

This is not a global rule. It should not touch C20 beauty/food global distribution, C19 retail inventory margin, or non-consumer reorder archetypes without separate confirmation.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible triggers | selected entries | avg MFE_90D | avg MAE_90D | avg MFE_180D | avg MAE_180D | false positive rate | missed structural | late Green | verdict |
|---|---|---:|---|---:|---:|---:|---:|---|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_global_proxy | 4 | 003230-T1|004370-T1|271560-T1|097950-T1 | 15.27 | -13.0 | 75.94 | -17.94 | 2/4 | 1 | 1 | mixed_alignment_false_positive_and_missed_structural |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 4 | mostly late Green or price-reactive labels | 13.9 | -13.7 | 61.2 | -18.7 | 2/4 | 2 | 2 | weaker_than_current_proxy |
| P1_L5_food_export_channel_shadow | sector_specific | 4 | 003230-T1|004370-T1; guards 271560/097950 | 23.8 | -11.39 | 143.15 | -11.39 | 0/2 | 0 | 0 | better_score_return_alignment |
| P2_C18_export_reorder_archetype_shadow | canonical_archetype_specific | 4 | positive: 003230/004370; counterexample guarded: 271560/097950 | 23.8 | -11.39 | 143.15 | -11.39 | 0/2 | 0 | 0 | canonical_rule_candidate |
| P3_C18_counterexample_guard_profile | guard_profile | 4 | guards two false positives, keeps two positives | 23.8 | -11.39 | 143.15 | -11.39 | 0/2 | 0 | 0 | best_guarded_alignment_on_this_loop |

## 20. Score-Return Alignment Matrix

| trigger_id | score_before | label_before | score_after | label_after | MFE_90D | MAE_90D | alignment |
|---|---:|---|---:|---|---:|---:|---|
| R5L16-C18-003230-T1 | 82.0 | Stage3-Yellow | 89.0 | Stage3-Green-shadow | 19.99 | -15.13 | improved |
| R5L16-C18-003230-T4B | 91.0 | Stage3-Green | 91.0 | Stage3-Green+4B-overlay-shadow | 11.0 | -24.88 | improved |
| R5L16-C18-004370-T1 | 76.0 | Stage3-Yellow | 82.5 | Stage2-Actionable-shadow | 27.61 | -7.65 | improved |
| R5L16-C18-271560-T1 | 79.0 | Stage3-Yellow | 68.0 | Stage2-Watch-guarded | 10.64 | -8.09 | improved |
| R5L16-C18-097950-T1 | 78.0 | Stage3-Yellow | 64.0 | Stage2-Watch-guarded | 1.84 | -21.15 | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C18_CONSUMER_EXPORT_CHANNEL_REORDER | K_FOOD_EXPORT_REORDER_CHANNEL_SELL_THROUGH_GUARD | 2 | 2 | 1 | 0 | 4 | 0 | 5 | 4 | 4 | true | true | C18 food/export-channel now has positive+counterexample coverage; still needs holdout in beverage/household exports. |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - current_profile_missed_structural
  - current_profile_too_late
  - current_profile_false_positive
  - current_profile_4B_too_late
new_axis_proposed:
  - C18_verified_sell_through_reorder_bonus
  - C18_unverified_restock_inventory_guard
  - C18_margin_cost_offset_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope: historical R5/C18 stock-web OHLC backtest for four food/export-channel reorder cases, plus one 4B overlay row. Non-validation scope: live candidate discovery, current recommendation, production scoring, brokerage API, source-route discovery, or stock_agent code patch.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C18_verified_sell_through_reorder_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,+4,+4,Verified sell-through plus repeat reorder and margin/revision conversion produced positive MFE in 003230/004370,Improves selected avg MFE_90D from 15.27 to 23.80 while avoiding broad restock false positives,R5L16-C18-003230-T1|R5L16-C18-004370-T1,4,4,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,C18_unverified_restock_inventory_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,-8,-8,Restock/base-effect without sell-through duration failed in 271560,Reduces false-positive rate from 2/4 to 0/2 selected positives,R5L16-C18-271560-T1,4,4,2,medium,canonical_shadow_only,"guard, not rollback"
shadow_weight,C18_margin_cost_offset_guard,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,-12,-12,K-food/global channel narrative was offset by input-cost and margin bridge risk in 097950,Blocks Yellow/Green false positive with MAE_90D -21.15,R5L16-C18-097950-T1,4,4,2,medium,sector_shadow_only,"guard, not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation
```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows
```jsonl
{"row_type":"case","case_id":"R5L16-C18-003230-20231115","symbol":"003230","company_name":"삼양식품","round":"R5","loop":"16","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_CHANNEL_SELL_THROUGH_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R5L16-C18-003230-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"after shadow C18 rule aligns better; P0 under-promoted verified reorder-to-margin conversion","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"불닭/라면 수출 채널의 실제 sell-through와 재주문이 분기 실적으로 전환되는 구간. 단순 K-food 테마가 아니라 해외 채널 재주문과 ASP/mix가 함께 확인될 때만 positive로 본다."}
{"row_type":"case","case_id":"R5L16-C18-004370-20200317","symbol":"004370","company_name":"농심","round":"R5","loop":"16","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_CHANNEL_SELL_THROUGH_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R5L16-C18-004370-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2 actionable signal was useful before full revision proof; strict Green waited too long for a short-cycle channel reorder.","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"팬데믹 초기 라면/간편식 채널 재고 소진과 재주문이 실제 가격 반응으로 이어진 구간. 채널 depletion이 확인된 reorder이면 단기 MFE가 의미 있게 발생했다."}
{"row_type":"case","case_id":"R5L16-C18-271560-20210818","symbol":"271560","company_name":"오리온","round":"R5","loop":"16","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_CHANNEL_SELL_THROUGH_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R5L16-C18-271560-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"P0 likely gave too much credit to overseas channel restock; guard profile reduces false-positive label.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"해외 채널 재고 정상화/재주문 서사는 있었으나 가격은 좁은 반등 뒤 하락했다. 채널 restock이 sell-through나 revision으로 이어지지 않으면 C18 bonus가 과해진다."}
{"row_type":"case","case_id":"R5L16-C18-097950-20210809","symbol":"097950","company_name":"CJ제일제당","round":"R5","loop":"16","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_CHANNEL_SELL_THROUGH_GUARD","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R5L16-C18-097950-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"P0 over-read a global food channel narrative and missed margin/cost offset; P3 guard removes positive classification.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"K-food/global packaged food narrative alone으로는 충분하지 않았다. 원재료/물류/바이오 margin 압박이 동시에 있으면 채널 재주문 신호는 Green이 아니라 guard 대상이다."}
```

### 25.3 trigger rows
```jsonl
{"row_type":"trigger","trigger_id":"R5L16-C18-003230-T1","case_id":"R5L16-C18-003230-20231115","symbol":"003230","company_name":"삼양식품","round":"R5","loop":"16","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_CHANNEL_SELL_THROUGH_GUARD","sector":"K-food / packaged food export","primary_archetype":"export channel reorder with verified sell-through and revision conversion","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2023-11-15","evidence_available_at_that_date":"Q3/export sell-through and reorder signal was visible enough to use the same-day close as a historical Stage2-Actionable proxy; later proof was not backfilled into the trigger.","evidence_source":"historical public result/news/research summary; stock-web rows sampled from 2023/2024 shards","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","multiple_public_sources","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2023.csv","profile_path":"atlas/symbol_profiles/003/003230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-11-15","entry_price":199600,"MFE_30D_pct":16.98,"MFE_90D_pct":19.99,"MFE_180D_pct":259.72,"MFE_1Y_pct":259.72,"MFE_2Y_pct":482.16,"MAE_30D_pct":-5.11,"MAE_90D_pct":-15.13,"MAE_180D_pct":-15.13,"MAE_1Y_pct":-15.13,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":718000,"drawdown_after_peak_pct":-32.31,"green_lateness_ratio":0.31,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_high_MFE_after_verified_channel_reorder","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L16-C18-003230-G1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L16-C18-003230-T4B","case_id":"R5L16-C18-003230-20231115","symbol":"003230","company_name":"삼양식품","round":"R5","loop":"16","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_CHANNEL_SELL_THROUGH_GUARD","sector":"K-food / packaged food export","primary_archetype":"export channel reorder with verified sell-through and revision conversion","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining","trigger_type":"Stage4B-Overlay","trigger_date":"2024-06-14","evidence_available_at_that_date":"Post-rerating valuation/positioning overheat after multi-month export reorder success; this is an overlay row, not a new positive Stage2/3 entry.","evidence_source":"stock-web price path plus historical valuation/positioning overlay note; non-price overheat required for full 4B","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv","profile_path":"atlas/symbol_profiles/003/003230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-14","entry_price":647000,"MFE_30D_pct":11.0,"MFE_90D_pct":11.0,"MFE_180D_pct":11.0,"MFE_1Y_pct":80.0,"MFE_2Y_pct":80.0,"MAE_30D_pct":-8.66,"MAE_90D_pct":-24.88,"MAE_180D_pct":-27.43,"MAE_1Y_pct":-27.43,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":718000,"drawdown_after_peak_pct":-32.31,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.863,"four_b_full_window_peak_proximity":0.464,"four_b_timing_verdict":"local_4B_good_but_full_window_partial_if_later_cycle_extends","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success_local_risk_reduction_not_thesis_break","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L16-C18-003230-G4B","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case reused only for 4B overlay timing audit","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R5L16-C18-004370-T1","case_id":"R5L16-C18-004370-20200317","symbol":"004370","company_name":"농심","round":"R5","loop":"16","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_CHANNEL_SELL_THROUGH_GUARD","sector":"K-food / domestic and export ramen reorder","primary_archetype":"panic demand reorder with visible channel depletion and export restock","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2020-03-17","evidence_available_at_that_date":"Demand shock, channel depletion and reorder visibility were tradable before full revision confirmation; same-day close is used as historical proxy.","evidence_source":"historical public channel-demand/reorder evidence and stock-web 2020 rows","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004370/2020.csv","profile_path":"atlas/symbol_profiles/004/004370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-03-17","entry_price":268000,"MFE_30D_pct":20.9,"MFE_90D_pct":27.61,"MFE_180D_pct":36.57,"MFE_1Y_pct":36.57,"MFE_2Y_pct":36.57,"MAE_30D_pct":-7.65,"MAE_90D_pct":-7.65,"MAE_180D_pct":-7.65,"MAE_1Y_pct":-13.43,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-05-18","peak_price":342000,"drawdown_after_peak_pct":-17.25,"green_lateness_ratio":0.49,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"channel_reorder_positive_moderate_MFE","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L16-C18-004370-G1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L16-C18-271560-T1","case_id":"R5L16-C18-271560-20210818","symbol":"271560","company_name":"오리온","round":"R5","loop":"16","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_CHANNEL_SELL_THROUGH_GUARD","sector":"food brand / China channel","primary_archetype":"overseas channel restock without enough revision or duration","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining","trigger_type":"Stage2-Actionable-candidate","trigger_date":"2021-08-18","evidence_available_at_that_date":"Overseas/China channel restock narrative was visible, but sell-through duration and revision conversion were not strong enough.","evidence_source":"historical public channel restock narrative and stock-web 2021 rows","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/271/271560/2021.csv","profile_path":"atlas/symbol_profiles/271/271560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-08-18","entry_price":117500,"MFE_30D_pct":10.64,"MFE_90D_pct":10.64,"MFE_180D_pct":10.64,"MFE_1Y_pct":10.64,"MFE_2Y_pct":18.3,"MAE_30D_pct":-2.13,"MAE_90D_pct":-8.09,"MAE_180D_pct":-21.28,"MAE_1Y_pct":-27.66,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-09-15","peak_price":130000,"drawdown_after_peak_pct":-16.92,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["revision_slowdown"],"four_c_protection_label":"false_break","trigger_outcome_label":"failed_rerating_restock_without_revision","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L16-C18-271560-G1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L16-C18-097950-T1","case_id":"R5L16-C18-097950-20210809","symbol":"097950","company_name":"CJ제일제당","round":"R5","loop":"16","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_CHANNEL_SELL_THROUGH_GUARD","sector":"processed food / global packaged food and ingredient mix","primary_archetype":"brand/global channel signal offset by input-cost and margin pressure","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining","trigger_type":"Stage2-Actionable-candidate","trigger_date":"2021-08-09","evidence_available_at_that_date":"Global packaged-food/K-food channel signal existed, but commodity/input-cost and non-channel margin risk offset the export narrative.","evidence_source":"historical public result/news/research summary and stock-web 2021 rows","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/097/097950/2021.csv","profile_path":"atlas/symbol_profiles/097/097950.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-08-09","entry_price":489500,"MFE_30D_pct":1.84,"MFE_90D_pct":1.84,"MFE_180D_pct":1.84,"MFE_1Y_pct":1.84,"MFE_2Y_pct":1.84,"MAE_30D_pct":-13.89,"MAE_90D_pct":-21.15,"MAE_180D_pct":-27.68,"MAE_1Y_pct":-39.53,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-08-10","peak_price":498500,"drawdown_after_peak_pct":-21.57,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_green_margin_cost_offset","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L16-C18-097950-G1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows
```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L16-C18-003230-20231115","trigger_id":"R5L16-C18-003230-T1","symbol":"003230","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":13,"revision_score":14,"relative_strength_score":12,"customer_quality_score":11,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":16,"revision_score":17,"relative_strength_score":14,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":89.0,"stage_label_after":"Stage3-Green-shadow","changed_components":["customer_quality_score","margin_bridge_score","revision_score","relative_strength_score"],"component_delta_explanation":"Verified export sell-through plus repeat orders and mix/margin conversion deserve C18-specific promotion; not a generic Stage2 bonus repetition.","MFE_90D_pct":19.99,"MAE_90D_pct":-15.13,"score_return_alignment_label":"aligned_after_shadow","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L16-C18-003230-20231115","trigger_id":"R5L16-C18-003230-T4B","symbol":"003230","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":18,"revision_score":19,"relative_strength_score":18,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":17,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":91.0,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":18,"revision_score":19,"relative_strength_score":18,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":17,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":91.0,"stage_label_after":"Stage3-Green+4B-overlay-shadow","changed_components":["execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"4B row changes overlay risk only. It must not promote another positive stage and must not be counted as a new independent case.","MFE_90D_pct":11.0,"MAE_90D_pct":-24.88,"score_return_alignment_label":"aligned_after_shadow","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L16-C18-004370-20200317","trigger_id":"R5L16-C18-004370-T1","symbol":"004370","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":7,"relative_strength_score":10,"customer_quality_score":11,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":9,"relative_strength_score":11,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":82.5,"stage_label_after":"Stage2-Actionable-shadow","changed_components":["customer_quality_score","capacity_or_shipment_score","revision_score"],"component_delta_explanation":"Short-cycle consumer channel depletion can be actionable before hard Green, but needs sell-through/reorder evidence not just price momentum.","MFE_90D_pct":27.61,"MAE_90D_pct":-7.65,"score_return_alignment_label":"aligned_after_shadow","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L16-C18-271560-20210818","trigger_id":"R5L16-C18-271560-T1","symbol":"271560","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":7,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":79.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":5,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68.0,"stage_label_after":"Stage2-Watch-guarded","changed_components":["customer_quality_score","revision_score","execution_risk_score"],"component_delta_explanation":"Restock narrative without sell-through/revision duration should be guarded; this is a counterexample to broad C18 promotion.","MFE_90D_pct":10.64,"MAE_90D_pct":-8.09,"score_return_alignment_label":"guarded_after_shadow","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L16-C18-097950-20210809","trigger_id":"R5L16-C18-097950-T1","symbol":"097950","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":5,"customer_quality_score":13,"policy_or_regulatory_score":5,"valuation_repricing_score":0,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":4,"customer_quality_score":7,"policy_or_regulatory_score":4,"valuation_repricing_score":0,"execution_risk_score":12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":64.0,"stage_label_after":"Stage2-Watch-guarded","changed_components":["customer_quality_score","margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"Brand/channel narrative must be penalized when input-cost and margin bridge are negative; otherwise C18 produces false positives.","MFE_90D_pct":1.84,"MAE_90D_pct":-21.15,"score_return_alignment_label":"guarded_after_shadow","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C18_verified_sell_through_reorder_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,+4,+4,Verified sell-through plus repeat reorder and margin/revision conversion produced positive MFE in 003230/004370,Improves selected avg MFE_90D from 15.27 to 23.80 while avoiding broad restock false positives,R5L16-C18-003230-T1|R5L16-C18-004370-T1,4,4,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,C18_unverified_restock_inventory_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,-8,-8,Restock/base-effect without sell-through duration failed in 271560,Reduces false-positive rate from 2/4 to 0/2 selected positives,R5L16-C18-271560-T1,4,4,2,medium,canonical_shadow_only,"guard, not rollback"
shadow_weight,C18_margin_cost_offset_guard,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,-12,-12,K-food/global channel narrative was offset by input-cost and margin bridge risk in 097950,Blocks Yellow/Green false positive with MAE_90D -21.15,R5L16-C18-097950-T1,4,4,2,medium,sector_shadow_only,"guard, not production"
```

### 25.6 residual_contribution row
```jsonl
{"row_type":"residual_contribution","round":"R5","loop":"16","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["current_profile_missed_structural","current_profile_too_late","current_profile_false_positive","current_profile_4B_too_late"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows
```jsonl
{"row_type":"narrative_only","case_id":null,"symbol":null,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","reason":"no narrative-only rows; all representative cases have clean 180D stock-web windows","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_loop = 16
next_round = R6
next_loop = 16
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- `Songdaiki/stock-web` manifest was checked for source name, max date, tradable/raw row counts, markets, shard roots, schema path, and universe path.
- Symbol profiles were checked for first/last dates, available years, row status counts, corporate-action candidate dates, major discontinuity flags, and raw/unadjusted caveats.
- OHLC row anchors were sampled from tradable shards for all representative entries and the 4B overlay row.
- This file is a historical calibration artifact only. It is not a current stock recommendation or production scoring patch.
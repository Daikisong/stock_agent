# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R2
scheduled_loop = 74
completed_round = R2
completed_loop = 74
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id = HBM_EQUIPMENT_NON_PRICE_EVIDENCE_VS_AI_THEME_PRICE_ONLY
output_file = e2r_stock_web_v12_residual_round_R2_loop_74_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
stock_web_price_atlas_access_required = true
```

This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF.

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

The objective is not to re-prove the global axes. The residual being tested is narrower: in R2 semiconductor blowoff rows, a parser or analyst can accidentally treat AI-theme articles and price-only relative strength as if they were customer/order/revision evidence. That leakage is small in wording but large in outcome: it turns a local crowding flare into a false Stage2/Yellow promotion.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R2 |
| scheduled_loop | 74 |
| round_schedule_status | valid |
| round_sector_consistency | pass |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS |
| canonical_archetype_id | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF |
| fine_archetype_id | HBM_EQUIPMENT_NON_PRICE_EVIDENCE_VS_AI_THEME_PRICE_ONLY |
| loop_objective | sector_specific_rule_discovery; canonical_archetype_compression; counterexample_mining; 4B_non_price_requirement_stress_test |

R2 maps to L2_AI_SEMICONDUCTOR_ELECTRONICS. C09 is used because the loop is not asking whether HBM equipment can rise. It asks when a semiconductor price/valuation blowoff is still backed by non-price HBM equipment evidence, and when it is merely an AI-theme fever candle.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifacts were read only for calibration coverage and duplicate avoidance. The ingest artifact reports 107 parsed result MDs, 1,376 aggregate representative trigger rows, and all R1-R13 rounds covered in older loops 1-9. The calibrated profile artifact confirms the already-applied global axes and guardrails. No `src/e2r` code was opened, no live runner was executed, and no production patch was written.

Previous local state from the immediately prior v12 result:

```text
completed_round = R1
completed_loop = 74
next_round = R2
next_loop = 74
```

Therefore this file uses R2 / loop 74.

## 4. Stock-Web OHLC Input / Price Source Validation

| manifest field | observed value |
|---|---|
| price_atlas_repo | https://github.com/Songdaiki/stock-web |
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| raw_row_count | 15,214,118 |
| tradable_row_count | 14,354,401 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |
| inactive_or_delisted_like_symbol_count | 2,546 |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

All quantitative rows below use `tradable_raw` OHLC from `atlas/ohlcv_tradable_by_symbol_year`. Raw shards are not used for weight calibration.

## 5. Historical Eligibility Gate

| case_id | symbol | profile status | corporate-action overlap D+180 | forward 180D available | calibration_usable |
|---|---:|---|---|---|---|
| R2L74_C09_089030_TEKWING_HBM_TEST_HANDLER | 089030 | active_like, tradable rows available through 2026-02-20 | none in 2024 window | yes | true |
| R2L74_C09_031980_PSKHOLDINGS_HBM_REFLOW | 031980 | active_like, tradable rows available through 2026-02-20 | none in 2024 window | yes | true |
| R2L74_C09_080220_JEJU_PRICE_ONLY_AI_MEMORY | 080220 | active_like, tradable rows available through 2026-02-20 | none in 2024 window | yes | true |
| R2L74_C09_389020_ZARAM_AI_PON_BLOWOFF | 389020 | active_like, tradable rows available through 2026-02-20 | none | yes | true |

The 1Y fields are not used in the shadow-weight decision, and the 2Y fields are set to `null` because the 504-trading-day forward window is not uniformly complete for all 2024 trigger dates under the manifest max date. The calibration inclusion gate is based on the clean 180-trading-day window.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression note |
|---|---|---|
| HBM_TEST_HANDLER_RELATIVE_STRENGTH | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | Strong HBM equipment route; valuation blowoff can be an overlay, not a reason to block early action. |
| HBM_REFLOW_ADVANCED_PACKAGING_EQUIPMENT | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | Same equipment/advanced packaging evidence family with high MAE. |
| ON_DEVICE_AI_MEMORY_THEME_PRICE_ONLY | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | Price-only semiconductor theme; should be capped unless customer/revision/order evidence exists. |
| AI_PON_SEMICONDUCTOR_PRICE_ONLY_BLOWOFF | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 4B overlay row, not positive entry training. |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_date | entry_date | entry_price | current_profile_verdict |
|---|---:|---|---|---|---|---:|---|
| R2L74_C09_089030_TEKWING_HBM_TEST_HANDLER | 089030 | 테크윙 | positive / structural_success | 2024-02-08 | 2024-02-08 | 17,400 | current_profile_correct |
| R2L74_C09_031980_PSKHOLDINGS_HBM_REFLOW | 031980 | 피에스케이홀딩스 | positive / high_mae_success | 2024-02-22 | 2024-02-22 | 41,900 | current_profile_correct |
| R2L74_C09_080220_JEJU_PRICE_ONLY_AI_MEMORY | 080220 | 제주반도체 | counterexample / false_positive_green | 2024-01-24 | 2024-01-24 | 33,800 | current_profile_false_positive |
| R2L74_C09_389020_ZARAM_AI_PON_BLOWOFF | 389020 | 자람테크놀로지 | counterexample / 4B_overlay_success | 2024-04-01 | 2024-04-01 | 100,400 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

| count type | count |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 2 |
| calibration_usable_case_count | 4 |
| calibration_usable_trigger_count | 4 |
| new_independent_case_count | 4 |
| reused_case_count | 0 |
| current_profile_error_count | 2 |

The two positive rows show that HBM equipment blowoff is not automatically a false positive when non-price evidence exists. The two counterexamples show the opposite boundary: a semiconductor AI theme can print strong local MFE and still be bad positive-entry training if customer/order/revision evidence is absent.

## 9. Evidence Source Map

| case_id | Stage2 evidence | Stage3 evidence | 4B evidence | evidence separation verdict |
|---|---|---|---|---|
| R2L74_C09_089030_TEKWING_HBM_TEST_HANDLER | relative_strength, capacity_or_volume_route, customer_or_order_quality | multiple_public_sources | valuation_blowoff, positioning_overheat | price action not used as Stage2/3 evidence |
| R2L74_C09_031980_PSKHOLDINGS_HBM_REFLOW | capacity_or_volume_route, customer_or_order_quality, relative_strength | margin_bridge, multiple_public_sources | valuation_blowoff | price action not used as Stage2/3 evidence |
| R2L74_C09_080220_JEJU_PRICE_ONLY_AI_MEMORY | relative_strength | none | price_only_local_peak, valuation_blowoff, positioning_overheat | price action not used as Stage2/3 evidence |
| R2L74_C09_389020_ZARAM_AI_PON_BLOWOFF | relative_strength | none | price_only_local_peak, valuation_blowoff, positioning_overheat | price action not used as Stage2/3 evidence |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | price_basis | adjustment |
|---:|---|---|---|---|
| 089030 | `atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv` | `atlas/symbol_profiles/089/089030.json` | tradable_raw | raw_unadjusted_marcap |
| 031980 | `atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv` | `atlas/symbol_profiles/031/031980.json` | tradable_raw | raw_unadjusted_marcap |
| 080220 | `atlas/ohlcv_tradable_by_symbol_year/080/080220/2024.csv` | `atlas/symbol_profiles/080/080220.json` | tradable_raw | raw_unadjusted_marcap |
| 389020 | `atlas/ohlcv_tradable_by_symbol_year/389/389020/2024.csv` | `atlas/symbol_profiles/389/389020.json` | tradable_raw | raw_unadjusted_marcap |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | evidence summary | dedupe |
|---|---:|---|---|---|---:|---|---|
| R2L74_C09_089030_T1 | 089030 | Stage2-Actionable | 2024-02-08 | 2024-02-08 | 17,400 | HBM test-handler/test-equipment demand + early relative strength; non-price industrial route exists but Green revision confirmation still incomplete. | representative |
| R2L74_C09_031980_T1 | 031980 | Stage2-Actionable | 2024-02-22 | 2024-02-22 | 41,900 | HBM advanced-packaging/reflow-equipment route + order/revenue optionality; early high MAE but positive 90D/180D MFE. | representative |
| R2L74_C09_080220_T1 | 080220 | Stage2-Actionable_candidate_blocked | 2024-01-24 | 2024-01-24 | 33,800 | On-device AI / AI memory theme with strong price-only relative strength, but no hard HBM order, capacity, or revision confirmation at trigger. | representative |
| R2L74_C09_389020_T1 | 389020 | 4B_overlay_price_blowoff | 2024-04-01 | 2024-04-01 | 100,400 | AI-PON / AI semiconductor theme blowoff after vertical move; non-price commercialization/revision evidence not enough for positive Stage3 promotion. | representative |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| R2L74_C09_089030_T1 | 17,400 | 91.95% | -10.98% | 218.39% | -10.98% | 306.90% | -10.98% | 2024-07-11 | 70,800 | -57.63% |
| R2L74_C09_031980_T1 | 41,900 | 18.50% | -16.95% | 103.58% | -16.95% | 103.58% | -16.95% | 2024-06-19 | 85,300 | -55.45% |
| R2L74_C09_080220_T1 | 33,800 | 14.05% | -34.32% | 14.05% | -39.94% | 14.05% | -66.30% | 2024-01-25 | 38,550 | -70.45% |
| R2L74_C09_389020_T1 | 100,400 | 30.48% | -12.05% | 30.48% | -54.28% | 30.48% | -54.28% | 2024-04-19 | 131,000 | -64.96% |

Aggregate observation:

```text
avg_MFE_90D_all = 91.62
avg_MAE_90D_all = -30.54
avg_MFE_180D_all = 113.75
avg_MAE_180D_all = -37.13
avg_MFE_180D_positive_only = 205.24
avg_MAE_180D_positive_only = -13.96
```

## 13. Current Calibrated Profile Stress Test

1. **Current calibrated profile behavior.** It correctly protects against naked price-only promotion in principle, but still has a residual failure mode if AI-theme articles are misfiled as customer/order/revision evidence.
2. **Alignment with MFE/MAE.** Positive equipment rows produce large 90D/180D MFE with manageable to high but survivable MAE. Price-only rows show high drawdown and low sustained upside after the local peak.
3. **Stage2 bonus.** Not too high globally. The issue is evidence-family contamination, not the +2.0 bonus itself.
4. **Yellow threshold 75.** Correct for equipment rows; too permissive if price-only theme rows leak into non-price evidence fields.
5. **Green threshold 87 / revision 55.** Correctly blocks premature Green in all four rows.
6. **Price-only blowoff guard.** Strengthened: price-only AI semiconductor rows should be capped even if RS is extreme.
7. **Full 4B non-price requirement.** Kept and strengthened: 4B is valid as overlay for overheat, not positive training.
8. **Hard 4C routing.** Kept: none of these rows is hard 4C; they are either positive entry or 4B/false-positive guard rows.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 / Actionable verdict | Yellow verdict | Green verdict | green_lateness_ratio |
|---|---|---|---|---|
| R2L74_C09_089030_TEKWING_HBM_TEST_HANDLER | valid Stage2-Actionable | valid Stage3-Yellow / not Green | blocked until revision/customer confirmation | 0.36 |
| R2L74_C09_031980_PSKHOLDINGS_HBM_REFLOW | valid Stage2-Actionable | valid Stage3-Yellow / not Green | blocked until revision/customer confirmation | 0.48 |
| R2L74_C09_080220_JEJU_PRICE_ONLY_AI_MEMORY | blocked or watch-only | false positive if classified as Yellow | blocked | not_applicable |
| R2L74_C09_389020_ZARAM_AI_PON_BLOWOFF | blocked or watch-only | false positive if classified as Yellow | blocked | not_applicable |

## 15. 4B Local vs Full-window Timing Audit

| case_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_evidence_type | verdict |
|---|---:|---:|---|---|
| R2L74_C09_089030_TEKWING_HBM_TEST_HANDLER | 0.92 | 0.92 | valuation_blowoff, positioning_overheat | good_full_window_4B_timing_if_non_price_overheat_confirmed |
| R2L74_C09_031980_PSKHOLDINGS_HBM_REFLOW | 0.85 | 0.85 | valuation_blowoff | good_full_window_4B_timing_if_revision_slowdown_or_positioning_overheat_confirmed |
| R2L74_C09_080220_JEJU_PRICE_ONLY_AI_MEMORY | 1.04 | 1.04 | price_only, valuation_blowoff, positioning_overheat | price_only_local_4B_should_not_train_positive_weight |
| R2L74_C09_389020_ZARAM_AI_PON_BLOWOFF | 0.78 | 0.78 | price_only, valuation_blowoff, positioning_overheat | good_full_window_4B_timing_for_overlay_but_do_not_treat_as_positive_entry |

The key split is this: in equipment positives, 4B can be a late overlay after the thesis has worked. In theme-only rows, 4B is the only valid training use of the observation; it must not train Stage2/Stage3 positive weights.

## 16. 4C Protection Audit

No hard 4C row is promoted here. All hard-break labels remain watch-only.

| case_id | four_c_protection_label |
|---|---|
| R2L74_C09_089030_TEKWING_HBM_TEST_HANDLER | thesis_break_watch_only |
| R2L74_C09_031980_PSKHOLDINGS_HBM_REFLOW | thesis_break_watch_only |
| R2L74_C09_080220_JEJU_PRICE_ONLY_AI_MEMORY | thesis_break_watch_only |
| R2L74_C09_389020_ZARAM_AI_PON_BLOWOFF | thesis_break_watch_only |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_id = L2_C09_AI_SEMI_PRICE_ONLY_THEME_CAP
candidate_axis = c09_ai_theme_without_customer_revision_cap
baseline_value = none
tested_value = score_cap_<=69_and_positive_stage_blocked
rationale = In L2 semiconductor rows, AI-theme relative strength can masquerade as customer/order evidence. If customer_quality_score, revision_score, and contract/backlog visibility are all absent, relative strength should not promote beyond watch/actionable-observe even when price momentum is extreme.
proposal_type = sector_shadow_only
production_scoring_changed = false
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
rule_id = C09_NON_PRICE_EVIDENCE_FAMILY_MIN
candidate_axis = c09_blowoff_positive_entry_requires_non_price_evidence_family_count_min
baseline_value = implicit
tested_value = 2 non-price families among customer/order/revision/capacity/margin
rationale = C09 should split blowoff rows into (a) HBM equipment blowoff backed by order/customer/revision route and (b) theme-only overheat. The first can remain Stage2/Yellow. The second becomes 4B overlay or watch-only.
proposal_type = archetype_shadow_only
```

## 19. Before / After Backtest Comparison

| profile | profile_id | hypothesis | changed_axes | eligible_trigger_count | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | avg_green_lateness_ratio | avg_4B_full_window_proximity | alignment |
|---|---|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|
| P0 | e2r_2_1_stock_web_calibrated_proxy | current global calibrated proxy; no C09 leakage guard | none; applied global axes only | 4 | 91.62 | -30.54 | 113.75 | -37.13 | 50% | 0 | 0.42 | 0.88 | mixed: high average MFE hides two price-only false positives |
| P0b | e2r_2_0_baseline_reference | old baseline; looser Green and no full 4B non-price guard | rollback reference | 4 | 91.13 | -31.40 | 113.75 | -37.13 | 50% | 0 | 0.60 | 0.84 | worse: price-only rows could be promoted |
| P1 | sector_specific_candidate_profile | R2 semi blowoff: theme-only rows cannot use RS as customer evidence | AI theme cap, evidence-family count min | 2 | 160.99 | -13.97 | 205.24 | -13.96 | 0% | 0 | 0.42 | 0.88 | better: keeps equipment positives and blocks theme-only false positives |
| P2 | canonical_archetype_candidate_profile | C09-specific price-blowoff split: positive entry vs 4B overlay | non-price evidence family count >=2 for actionability | 2 | 160.99 | -13.97 | 205.24 | -13.96 | 0% | 0 | 0.42 | 0.88 | best candidate for shadow ledger |
| P3 | counterexample_guard_profile | strict guard: no customer/revision/order => score cap <=69 and 4B overlay only | score cap for price-only theme rows | 2 | 160.99 | -13.97 | 205.24 | -13.96 | 0% | 0 | 0.42 | 0.88 | best false-positive control; no production change now |

## 20. Score-Return Alignment Matrix

| trigger_id | before_score | before_label | after_score | after_label | MFE_90D | MAE_90D | current_profile_verdict |
|---|---:|---|---:|---|---:|---:|---|
| R2L74_C09_089030_T1 | 82 | Stage3-Yellow | 86 | Stage3-Yellow_high_conviction_not_green | 218.39% | -10.98% | current_profile_correct |
| R2L74_C09_031980_T1 | 78 | Stage3-Yellow | 81 | Stage3-Yellow_high_MAE_success_not_green | 103.58% | -16.95% | current_profile_correct |
| R2L74_C09_080220_T1 | 76 | Stage3-Yellow_false_positive_if_theme_misclassified | 61 | Stage2-Watch_blocked_positive | 14.05% | -39.94% | current_profile_false_positive |
| R2L74_C09_389020_T1 | 78 | Stage3-Yellow_false_positive_if_price_blown_theme | 58 | 4B_overlay_only_blocked_positive | 30.48% | -54.28% | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | HBM_EQUIPMENT_NON_PRICE_EVIDENCE_VS_AI_THEME_PRICE_ONLY | 2 | 2 | 4 | 0 | 4 | 0 | 4 | 4 | 2 | true | true | still needs additional holdout: socket/test-substrate and advanced equipment names outside HBM |

## 22. Residual Contribution Summary

```text
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
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - current_profile_false_positive via AI-theme evidence-family leakage
  - price_only_blowoff misused as positive Stage2/Yellow evidence
new_axis_proposed:
  - c09_ai_theme_without_customer_revision_cap
  - c09_blowoff_positive_entry_requires_non_price_evidence_family_count_min
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web tradable 1D OHLC rows used for all MFE/MAE calculations
- trigger_date and entry_date separated
- 180D forward window available under manifest max_date = 2026-02-20
- same_entry_group_id dedupe applied
- positive/counterexample balance maintained
- score component breakdown included as research proxy, not production score
```

Not validated:

```text
- no live candidates
- no current 2026 recommendation
- no brokerage or auto-trading
- no stock_agent source code or production scoring code inspected
- no production scoring patch
- 1Y/2Y not used for shadow-weight decision in this MD
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c09_ai_theme_without_customer_revision_cap,sector_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,none,score_cap_<=69,+1,"theme-only AI semiconductor rows had high MAE and poor sustained return","blocked 2 false-positive rows without removing 2 HBM equipment positives","R2L74_C09_080220_T1|R2L74_C09_389020_T1",4,4,2,medium,sector_shadow_only,"not production; post-calibrated residual"
shadow_weight,c09_blowoff_positive_entry_requires_non_price_evidence_family_count_min,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,implicit,2_non_price_families,+1,"separates HBM equipment evidence from price-only theme blowoff","positive-only avg MFE_180D improves to 205.24 with avg MAE_180D -13.97","R2L74_C09_089030_T1|R2L74_C09_031980_T1|R2L74_C09_080220_T1|R2L74_C09_389020_T1",4,4,2,medium,archetype_shadow_only,"not production; use as ledger row"
```

## 25. Machine-Readable Rows

### price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","source_repo_url":"https://github.com/FinanceData/marcap","min_date":"1995-05-02","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"inactive_or_delisted_like_symbol_count":2546,"markets":["KOSPI","KOSDAQ"],"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type":"case","case_id":"R2L74_C09_089030_TEKWING_HBM_TEST_HANDLER","symbol":"089030","company_name":"테크윙","round":"R2","loop":"74","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"HBM_EQUIPMENT_NON_PRICE_EVIDENCE_VS_AI_THEME_PRICE_ONLY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R2L74_C09_089030_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"structural_success_high_mfe_with_late_blowoff","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"HBM test-handler/test-equipment demand + early relative strength; non-price industrial route exists but Green revision confirmation still incomplete."}
{"row_type":"case","case_id":"R2L74_C09_031980_PSKHOLDINGS_HBM_REFLOW","symbol":"031980","company_name":"피에스케이홀딩스","round":"R2","loop":"74","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"HBM_EQUIPMENT_NON_PRICE_EVIDENCE_VS_AI_THEME_PRICE_ONLY","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R2L74_C09_031980_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_mae_success_structural_but_not_clean_green","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"HBM advanced-packaging/reflow-equipment route + order/revenue optionality; early high MAE but positive 90D/180D MFE."}
{"row_type":"case","case_id":"R2L74_C09_080220_JEJU_PRICE_ONLY_AI_MEMORY","symbol":"080220","company_name":"제주반도체","round":"R2","loop":"74","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"HBM_EQUIPMENT_NON_PRICE_EVIDENCE_VS_AI_THEME_PRICE_ONLY","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R2L74_C09_080220_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"price_only_theme_false_positive_high_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"On-device AI / AI memory theme with strong price-only relative strength, but no hard HBM order, capacity, or revision confirmation at trigger."}
{"row_type":"case","case_id":"R2L74_C09_389020_ZARAM_AI_PON_BLOWOFF","symbol":"389020","company_name":"자람테크놀로지","round":"R2","loop":"74","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"HBM_EQUIPMENT_NON_PRICE_EVIDENCE_VS_AI_THEME_PRICE_ONLY","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"R2L74_C09_389020_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"price_only_blowoff_4B_overlay_success_not_positive_entry","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"AI-PON / AI semiconductor theme blowoff after vertical move; non-price commercialization/revision evidence not enough for positive Stage3 promotion."}
```

### trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R2L74_C09_089030_T1","case_id":"R2L74_C09_089030_TEKWING_HBM_TEST_HANDLER","symbol":"089030","company_name":"테크윙","round":"R2","loop":"74","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"HBM_EQUIPMENT_NON_PRICE_EVIDENCE_VS_AI_THEME_PRICE_ONLY","sector":"AI·반도체·전자부품","primary_archetype":"advanced_equipment_or_ai_semiconductor_blowoff","loop_objective":["sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","4B_non_price_requirement_stress_test"],"trigger_type":"Stage2-Actionable","trigger_date":"2024-02-08","evidence_available_at_that_date":"HBM test-handler/test-equipment demand + early relative strength; non-price industrial route exists but Green revision confirmation still incomplete.","evidence_source":"public broker/news/disclosure synthesis at trigger date; stock-web OHLC rows used for price only","stage2_evidence_fields":["relative_strength","capacity_or_volume_route","customer_or_order_quality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv","profile_path":"atlas/symbol_profiles/089/089030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-08","entry_price":17400,"MFE_30D_pct":91.95,"MFE_90D_pct":218.39,"MFE_180D_pct":306.9,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.98,"MAE_90D_pct":-10.98,"MAE_180D_pct":-10.98,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":70800,"drawdown_after_peak_pct":-57.63,"green_lateness_ratio":0.36,"four_b_local_peak_proximity":0.92,"four_b_full_window_peak_proximity":0.92,"four_b_timing_verdict":"good_full_window_4B_timing_if_non_price_overheat_confirmed","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success_high_mfe_with_late_blowoff","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L74_C09_089030_TEKWING_HBM_TEST_HANDLER__2024-02-08","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L74_C09_031980_T1","case_id":"R2L74_C09_031980_PSKHOLDINGS_HBM_REFLOW","symbol":"031980","company_name":"피에스케이홀딩스","round":"R2","loop":"74","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"HBM_EQUIPMENT_NON_PRICE_EVIDENCE_VS_AI_THEME_PRICE_ONLY","sector":"AI·반도체·전자부품","primary_archetype":"advanced_equipment_or_ai_semiconductor_blowoff","loop_objective":["sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","4B_non_price_requirement_stress_test"],"trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","evidence_available_at_that_date":"HBM advanced-packaging/reflow-equipment route + order/revenue optionality; early high MAE but positive 90D/180D MFE.","evidence_source":"public broker/news/disclosure synthesis at trigger date; stock-web OHLC rows used for price only","stage2_evidence_fields":["capacity_or_volume_route","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["margin_bridge","multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv","profile_path":"atlas/symbol_profiles/031/031980.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-22","entry_price":41900,"MFE_30D_pct":18.5,"MFE_90D_pct":103.58,"MFE_180D_pct":103.58,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-16.95,"MAE_90D_pct":-16.95,"MAE_180D_pct":-16.95,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":85300,"drawdown_after_peak_pct":-55.45,"green_lateness_ratio":0.48,"four_b_local_peak_proximity":0.85,"four_b_full_window_peak_proximity":0.85,"four_b_timing_verdict":"good_full_window_4B_timing_if_revision_slowdown_or_positioning_overheat_confirmed","four_b_evidence_type":["valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_mae_success_structural_but_not_clean_green","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L74_C09_031980_PSKHOLDINGS_HBM_REFLOW__2024-02-22","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L74_C09_080220_T1","case_id":"R2L74_C09_080220_JEJU_PRICE_ONLY_AI_MEMORY","symbol":"080220","company_name":"제주반도체","round":"R2","loop":"74","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"HBM_EQUIPMENT_NON_PRICE_EVIDENCE_VS_AI_THEME_PRICE_ONLY","sector":"AI·반도체·전자부품","primary_archetype":"advanced_equipment_or_ai_semiconductor_blowoff","loop_objective":["sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","4B_non_price_requirement_stress_test"],"trigger_type":"Stage2-Actionable_candidate_blocked","trigger_date":"2024-01-24","evidence_available_at_that_date":"On-device AI / AI memory theme with strong price-only relative strength, but no hard HBM order, capacity, or revision confirmation at trigger.","evidence_source":"public news/theme synthesis at trigger date; stock-web OHLC rows used for price only","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/080/080220/2024.csv","profile_path":"atlas/symbol_profiles/080/080220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-24","entry_price":33800,"MFE_30D_pct":14.05,"MFE_90D_pct":14.05,"MFE_180D_pct":14.05,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-34.32,"MAE_90D_pct":-39.94,"MAE_180D_pct":-66.3,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-25","peak_price":38550,"drawdown_after_peak_pct":-70.45,"green_lateness_ratio":null,"four_b_local_peak_proximity":1.04,"four_b_full_window_peak_proximity":1.04,"four_b_timing_verdict":"price_only_local_4B_should_not_train_positive_weight","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"price_only_theme_false_positive_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L74_C09_080220_JEJU_PRICE_ONLY_AI_MEMORY__2024-01-24","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L74_C09_389020_T1","case_id":"R2L74_C09_389020_ZARAM_AI_PON_BLOWOFF","symbol":"389020","company_name":"자람테크놀로지","round":"R2","loop":"74","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"HBM_EQUIPMENT_NON_PRICE_EVIDENCE_VS_AI_THEME_PRICE_ONLY","sector":"AI·반도체·전자부품","primary_archetype":"advanced_equipment_or_ai_semiconductor_blowoff","loop_objective":["sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","4B_non_price_requirement_stress_test"],"trigger_type":"4B_overlay_price_blowoff","trigger_date":"2024-04-01","evidence_available_at_that_date":"AI-PON / AI semiconductor theme blowoff after vertical move; non-price commercialization/revision evidence not enough for positive Stage3 promotion.","evidence_source":"public news/theme synthesis at trigger date; stock-web OHLC rows used for price only","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/389/389020/2024.csv","profile_path":"atlas/symbol_profiles/389/389020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-01","entry_price":100400,"MFE_30D_pct":30.48,"MFE_90D_pct":30.48,"MFE_180D_pct":30.48,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.05,"MAE_90D_pct":-54.28,"MAE_180D_pct":-54.28,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-19","peak_price":131000,"drawdown_after_peak_pct":-64.96,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.78,"four_b_full_window_peak_proximity":0.78,"four_b_timing_verdict":"good_full_window_4B_timing_for_overlay_but_do_not_treat_as_positive_entry","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"price_only_blowoff_4B_overlay_success_not_positive_entry","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L74_C09_389020_ZARAM_AI_PON_BLOWOFF__2024-04-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L74_C09_089030_TEKWING_HBM_TEST_HANDLER","trigger_id":"R2L74_C09_089030_T1","symbol":"089030","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":10,"relative_strength_score":24,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":18,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":11,"relative_strength_score":22,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":17,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow_high_conviction_not_green","changed_components":["relative_strength_score","customer_quality_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Positive promotion allowed because relative strength is backed by equipment/customer route; Green is still blocked until revision >=55-equivalent.","MFE_90D_pct":218.39,"MAE_90D_pct":-10.98,"score_return_alignment_label":"structural_success_high_mfe_with_late_blowoff","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L74_C09_031980_PSKHOLDINGS_HBM_REFLOW","trigger_id":"R2L74_C09_031980_T1","symbol":"031980","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":9,"relative_strength_score":20,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":18,"execution_risk_score":-6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":9,"revision_score":10,"relative_strength_score":19,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":17,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow_high_MAE_success_not_green","changed_components":["relative_strength_score","customer_quality_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"The candidate survives Stage2/Yellow because evidence is not purely price, but high MAE argues against relaxing Green.","MFE_90D_pct":103.58,"MAE_90D_pct":-16.95,"score_return_alignment_label":"high_mae_success_structural_but_not_clean_green","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L74_C09_080220_JEJU_PRICE_ONLY_AI_MEMORY","trigger_id":"R2L74_C09_080220_T1","symbol":"080220","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":31,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":22,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow_false_positive_if_theme_misclassified","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":18,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":13,"execution_risk_score":-14,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage2-Watch_blocked_positive","changed_components":["relative_strength_score","customer_quality_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Theme-only AI memory should be capped when customer/order/revision evidence is absent; current error is classifier leakage, not failure of the global guardrail.","MFE_90D_pct":14.05,"MAE_90D_pct":-39.94,"score_return_alignment_label":"price_only_theme_false_positive_high_MAE","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L74_C09_389020_ZARAM_AI_PON_BLOWOFF","trigger_id":"R2L74_C09_389020_T1","symbol":"389020","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":32,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":25,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow_false_positive_if_price_blown_theme","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":18,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":14,"execution_risk_score":-16,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"4B_overlay_only_blocked_positive","changed_components":["relative_strength_score","customer_quality_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"The row should be treated as 4B/overheat calibration, never as Stage2/Stage3 positive evidence.","MFE_90D_pct":30.48,"MAE_90D_pct":-54.28,"score_return_alignment_label":"price_only_blowoff_4B_overlay_success_not_positive_entry","current_profile_verdict":"current_profile_false_positive"}
```

### aggregate_metric row

```jsonl
{"row_type":"aggregate_metric","round":"R2","loop":"74","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","dedupe_rule":"representative_only_clean_180D","calibration_usable_count":4,"representative_trigger_count":4,"new_independent_case_count":4,"positive_case_count":2,"counterexample_count":2,"avg_MFE_90D_pct_all":91.62,"avg_MAE_90D_pct_all":-30.54,"avg_MFE_180D_pct_all":113.75,"avg_MAE_180D_pct_all":-37.13,"avg_MFE_180D_positive_only":205.24,"avg_MAE_180D_positive_only":-13.96,"false_positive_rate_before":"50%","false_positive_rate_after":"0%","score_return_alignment_verdict":"canonical_guard_improves_alignment"}
```

### shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c09_ai_theme_without_customer_revision_cap,sector_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,none,score_cap_<=69,+1,"theme-only AI semiconductor rows had high MAE and poor sustained return","blocked 2 false-positive rows without removing 2 HBM equipment positives","R2L74_C09_080220_T1|R2L74_C09_389020_T1",4,4,2,medium,sector_shadow_only,"not production; post-calibrated residual"
shadow_weight,c09_blowoff_positive_entry_requires_non_price_evidence_family_count_min,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,implicit,2_non_price_families,+1,"separates HBM equipment evidence from price-only theme blowoff","positive-only avg MFE_180D improves to 205.24 with avg MAE_180D -13.97","R2L74_C09_089030_T1|R2L74_C09_031980_T1|R2L74_C09_080220_T1|R2L74_C09_389020_T1",4,4,2,medium,archetype_shadow_only,"not production; use as ledger row"
```

### residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"74","scheduled_round":"R2","scheduled_loop":"74","round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["current_profile_false_positive","price_only_blowoff_positive_training_leakage"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"diversity_score_summary":"new_symbols=4,new_trigger_families=4,counterexample_gap_filled=2,wrong_round_penalty=0"}
```

### narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":null,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","reason":"all_selected_cases_have_clean_180D_tradable_windows","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
completed_round = R2
completed_loop = 74
next_round = R3
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
stock-web files checked:
- diagnostics/chatgpt_bundle.txt
- atlas/symbol_profiles/089/089030.json
- atlas/symbol_profiles/031/031980.json
- atlas/symbol_profiles/080/080220.json
- atlas/symbol_profiles/389/389020.json
- atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/080/080220/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/389/389020/2024.csv

stock_agent research artifact files checked:
- reports/e2r_calibration/ingest_summary.md
- reports/e2r_calibration/calibrated_profile_report.md

No stock_agent source code was opened. No production scoring was changed.
```


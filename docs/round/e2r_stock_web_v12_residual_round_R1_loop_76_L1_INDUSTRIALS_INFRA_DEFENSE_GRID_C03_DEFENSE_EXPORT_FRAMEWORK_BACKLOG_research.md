# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
repo_session = later_batch_implementation_only
output_file = e2r_stock_web_v12_residual_round_R1_loop_76_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md
scheduled_round = R1
scheduled_loop = 76
completed_round = R1
completed_loop = 76
next_round = R2
next_loop = 76
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id = DEFENSE_REPEAT_EXPORT_BACKLOG_VS_FORMAL_CONTRACT_AND_THEME_BETA
loop_objective = residual_false_positive_mining | residual_missed_structural_mining | stage2_actionable_bonus_stress_test | green_strictness_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression | counterexample_mining | coverage_gap_fill
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 4 new independent cases, 2 counterexamples, and 4 residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG.

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

This MD does not re-prove those global axes. It asks a narrower R1/C03 question: when a defense event has a named platform and sovereign counterparty, what extra evidence separates repeat export backlog from a one-day defense-theme rope bridge?

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R1 |
| scheduled_loop | 76 |
| large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID |
| canonical_archetype_id | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG |
| fine_archetype_id | DEFENSE_REPEAT_EXPORT_BACKLOG_VS_FORMAL_CONTRACT_AND_THEME_BETA |
| round_schedule_status | valid |
| round_sector_consistency | pass |

R1 maps to `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`, so the file is valid under the hard round/sector gate. The canonical scope is C03, not a general policy or price-theme file.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts and local generated v12 registry were used only for schedule and duplicate avoidance. The immediately previous file completed R13/Loop 75 and computed next state R1/Loop 76. Recent R1 local files covered C02 power-grid/datacenter, C04 nuclear policy delay, and C01 shipbuilding backlog. Earlier defense C03 rows in R11 used 064350, 012450, 065450, 013810, and 010820. This run avoids those hard duplicate keys and adds new C03 symbols/triggers: 079550, 047810, 024740, plus 103140 as a reused-symbol/new-trigger-family compression from R4/C15 into C03.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
duplicate_key_conflict = 0
new_independent_case_ratio = 1.00 for calibration inclusion; 103140 is reused symbol but new trigger family and not a same C03 duplicate
minimum_new_symbol_count = pass
positive_case_count = 2
counterexample_count = 2
```

## 4. Stock-Web OHLC Input / Price Source Validation

The stock-web manifest and schema were checked for this run. The atlas is raw/unadjusted FinanceData/marcap; forward windows are bounded by manifest `max_date = 2026-02-20`, not by the chat date. Tradable shards exclude zero-volume, zero-OHLC, missing-OHLC, and inconsistent-OHLC rows; raw shards retain row status for diagnostics only.

| field | value |
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
| markets | KONEX; KOSDAQ; KOSDAQ GLOBAL; KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Schema columns used for backtest: `d,o,h,l,c,v,a,mc,s,m`; raw shards add `rs`. MFE/MAE are calculated only on `tradable_raw` rows.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | forward_180D_available | corporate_action_window_status | calibration_usable |
|---|---:|---:|---:|---|---:|
| R1L76_C03_POS_079550_20240920_CHEONGUNG_REPEAT_EXPORT_BACKLOG | 079550 | 2024-09-20 | true | clean_180D_window | true |
| R1L76_C03_POS_103140_20240222_AMMUNITION_MARGIN_EXPORT_BRIDGE | 103140 | 2024-02-22 | true | clean_180D_window | true |
| R1L76_C03_CEX_047810_20220916_FA50_FORMAL_CONTRACT_HIGH_MAE | 047810 | 2022-09-16 | true | clean_180D_window | true |
| R1L76_C03_CEX_024740_20221004_NK_MISSILE_THEME_ONLY | 024740 | 2022-10-04 | true | clean_180D_window; profile CA dates are pre-2022 and outside window | true |

Profiles checked in stock-web: 079550 has no corporate-action candidate dates; 047810 has no corporate-action candidate dates; 024740 has historical CA candidates ending 2018-03-16, outside the 2022-10-04 forward window; 103140 was previously validated in a clean 2024 window. Therefore all representative rows are calibration-usable for 30D/90D/180D.

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression rationale |
|---|---|---|
| repeat_air_defense_export_system | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | Named system + repeat sovereign buyer + prior foreign operators can behave like backlog conversion even when filing detail is confidential. |
| ammunition_export_margin_bridge | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | Defense demand only counts when producer-level margin/order conversion is visible, not when it is just commodity beta. |
| formal_contract_without_margin_confirmation | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | A formal contract can still be too late or high-MAE if the framework was already priced and configuration/delivery/margin timing is unresolved. |
| geopolitical_theme_only | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG negative guard | Headline/RS alone must remain watch-only or 4B/4C overlay, not positive Stage2/3 evidence. |

## 7. Case Selection Summary

| role | case_id | symbol | company | trigger | current_profile_verdict | outcome |
|---|---|---:|---|---|---|---|
| positive | R1L76_C03_POS_079550_20240920_CHEONGUNG_REPEAT_EXPORT_BACKLOG | 079550 | LIG넥스원 | Stage2-Actionable 2024-09-20 | current_profile_too_late | structural_success_repeat_export_backlog |
| positive | R1L76_C03_POS_103140_20240222_AMMUNITION_MARGIN_EXPORT_BRIDGE | 103140 | 풍산 | Stage2-Actionable 2024-02-22 | current_profile_missed_structural | structural_success_margin_export_bridge |
| counterexample | R1L76_C03_CEX_047810_20220916_FA50_FORMAL_CONTRACT_HIGH_MAE | 047810 | 한국항공우주 | Stage2-Actionable-formal-contract 2022-09-16 | current_profile_too_early | formal_contract_high_MAE_counterexample |
| counterexample | R1L76_C03_CEX_024740_20221004_NK_MISSILE_THEME_ONLY | 024740 | 한일단조 | Stage2-Theme / geopolitical headline-only 2022-10-04 | current_profile_false_positive | theme_only_failed_rerating |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 2 |
| 4B_case_count | 3 |
| 4C_case_count | 1 |
| calibration_usable_case_count | 4 |
| representative_trigger_count | 4 |
| new_independent_case_count | 4 |
| reused_case_count | 1 |

Balance is acceptable for a canonical shadow candidate. The two positives show export/backlog conversion; the two counterexamples show that even formal contracts or geopolitical defense themes can be high-MAE unless delivery/margin/revision conversion is visible.

## 9. Evidence Source Map

| case_id | evidence_available_at_that_date | stage2_evidence_fields | stage3_evidence_fields | stage4b_evidence_fields | stage4c_evidence_fields |
|---|---|---|---|---|---|
| R1L76_C03_POS_079550_20240920_CHEONGUNG_REPEAT_EXPORT_BACKLOG | Iraq Cheongung-II export order following Saudi/UAE demand; named air-defense platform, sovereign buyer, repeat export system, and regulatory filing route despite confidentiality. | public_event_or_disclosure, customer_or_order_quality, policy_or_regulatory_optionality, backlog_or_delivery_visibility, relative_strength | multiple_public_sources, durable_customer_confirmation, financial_visibility, repeat_order_or_conversion | valuation_blowoff, positioning_overheat | - |
| R1L76_C03_POS_103140_20240222_AMMUNITION_MARGIN_EXPORT_BRIDGE | Ammunition/defense demand plus copper spread and producer margin bridge; not a pure commodity beta because defense order/margin conversion was visible before the 2024 rerating. | public_event_or_disclosure, capacity_or_volume_route, backlog_or_delivery_visibility, early_revision_signal, relative_strength | confirmed_revision, margin_bridge, financial_visibility, durable_customer_confirmation, low_red_team_risk | valuation_blowoff, positioning_overheat, margin_or_backlog_slowdown | - |
| R1L76_C03_CEX_047810_20220916_FA50_FORMAL_CONTRACT_HIGH_MAE | Poland FA-50 formal contract had named platform and buyer, but the trade was late relative to the July framework and was still exposed to configuration/delivery/margin-timing uncertainty. | public_event_or_disclosure, customer_or_order_quality, policy_or_regulatory_optionality, backlog_or_delivery_visibility | multiple_public_sources | contract_delay, margin_or_backlog_slowdown, price_only_local_peak | - |
| R1L76_C03_CEX_024740_20221004_NK_MISSILE_THEME_ONLY | North Korea missile/geopolitical shock moved defense-theme small caps; no company-specific export framework, sovereign buyer, order size, delivery route, or margin bridge was visible. | public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality | - | price_only_local_peak, positioning_overheat | thesis_evidence_broken |

Evidence is frozen to trigger date. Price action validates the subsequent return path only; it is not used to create Stage2 or Stage3 evidence.

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | price_basis | price_adjustment_status |
|---:|---|---|---|---|---|
| 079550 | LIG넥스원 | `atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv|atlas/ohlcv_tradable_by_symbol_year/079/079550/2025.csv` | `atlas/symbol_profiles/079/079550.json` | tradable_raw | raw_unadjusted_marcap |
| 103140 | 풍산 | `atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv` | `atlas/symbol_profiles/103/103140.json` | tradable_raw | raw_unadjusted_marcap |
| 047810 | 한국항공우주 | `atlas/ohlcv_tradable_by_symbol_year/047/047810/2022.csv|atlas/ohlcv_tradable_by_symbol_year/047/047810/2023.csv` | `atlas/symbol_profiles/047/047810.json` | tradable_raw | raw_unadjusted_marcap |
| 024740 | 한일단조 | `atlas/ohlcv_tradable_by_symbol_year/024/024740/2022.csv|atlas/ohlcv_tradable_by_symbol_year/024/024740/2023.csv` | `atlas/symbol_profiles/024/024740.json` | tradable_raw | raw_unadjusted_marcap |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | same_entry_group_id | dedupe_for_aggregate | aggregate_group_role |
|---|---:|---|---:|---:|---:|---|---:|---|
| R1L76_C03_079550_20240920_STAGE2A_REPEAT_EXPORT | 079550 | Stage2-Actionable | 2024-09-20 | 2024-09-20 | 211,000 | R1L76_C03_POS_079550_20240920_CHEONGUNG_REPEAT_EXPORT_BACKLOG::2024-09-20::211000 | true | representative |
| R1L76_C03_103140_20240222_STAGE2A_AMMO_EXPORT_MARGIN | 103140 | Stage2-Actionable | 2024-02-22 | 2024-02-22 | 42,200 | R1L76_C03_POS_103140_20240222_AMMUNITION_MARGIN_EXPORT_BRIDGE::2024-02-22::42200 | true | representative |
| R1L76_C03_047810_20220916_STAGE2A_FORMAL_CONTRACT_GUARD | 047810 | Stage2-Actionable-formal-contract | 2022-09-16 | 2022-09-16 | 50,300 | R1L76_C03_CEX_047810_20220916_FA50_FORMAL_CONTRACT_HIGH_MAE::2022-09-16::50300 | true | representative |
| R1L76_C03_024740_20221004_STAGE2_THEME_REJECTED | 024740 | Stage2-Theme / geopolitical headline-only | 2022-10-04 | 2022-10-04 | 3,035 | R1L76_C03_CEX_024740_20221004_NK_MISSILE_THEME_ONLY::2022-10-04::3035 | true | representative |

## 12. Trigger-Level OHLC Backtest Tables

MFE/MAE are computed from stock-web tradable raw 1D OHLC windows. 1Y/2Y fields are present in machine rows but not used for this loop because the rule candidate is 180D-trigger calibration.

| trigger_id | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | outcome |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| R1L76_C03_079550_20240920_STAGE2A_REPEAT_EXPORT | 211,000 | 25.59 | -1.42 | 28.67 | -13.18 | 163.98 | -13.18 | 2025-06-16 | 557,000 | -3.95 | structural_success_repeat_export_backlog |
| R1L76_C03_103140_20240222_STAGE2A_AMMO_EXPORT_MARGIN | 42,200 | 26.07 | -7.70 | 86.97 | -7.70 | 86.97 | -7.70 | 2024-05-14 | 78,900 | -40.43 | structural_success_margin_export_bridge |
| R1L76_C03_047810_20220916_STAGE2A_FORMAL_CONTRACT_GUARD | 50,300 | 4.77 | -20.48 | 4.77 | -20.48 | 15.31 | -20.48 | 2023-06-19 | 58,000 | -18.97 | formal_contract_high_MAE_counterexample |
| R1L76_C03_024740_20221004_STAGE2_THEME_REJECTED | 3,035 | 10.71 | -9.23 | 10.71 | -12.52 | 10.71 | -18.29 | 2022-10-11 | 3,360 | -26.19 | theme_only_failed_rerating |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely decision | backtest alignment | current_profile_verdict |
|---|---|---|---|
| R1L76_C03_POS_079550_20240920_CHEONGUNG_REPEAT_EXPORT_BACKLOG | P0 may hesitate because filing detail is confidential and revision evidence is not yet mature. | 180D MFE +163.98% with manageable MAE; named repeat system/buyer should be actionable earlier. | current_profile_too_late |
| R1L76_C03_POS_103140_20240222_AMMUNITION_MARGIN_EXPORT_BRIDGE | P0 may classify mainly as materials spread, missing the defense/ammunition conversion layer. | 90D/180D MFE +86.97% with clean -7.70% MAE; bridge evidence aligned. | current_profile_missed_structural |
| R1L76_C03_CEX_047810_20220916_FA50_FORMAL_CONTRACT_HIGH_MAE | P0 may over-promote a formal sovereign contract. | 30D/90D MFE only +4.77% while MAE hit -20.48%; formal contract was too late without margin/revision bridge. | current_profile_too_early |
| R1L76_C03_CEX_024740_20221004_NK_MISSILE_THEME_ONLY | P0 may let RS plus geopolitical defense theme look like policy optionality. | 180D MFE only +10.71% with MAE -18.29%; no backlog/customer bridge. | current_profile_false_positive |

Existing-axis status:

```text
stage2_actionable_evidence_bonus = existing_axis_tested
stage3_yellow_total_min = existing_axis_kept
stage3_green_total_min = existing_axis_kept
stage3_green_revision_min = existing_axis_kept
stage3_cross_evidence_green_buffer = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_strengthened
```

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2/actionable timing | Yellow/Green issue | green_lateness_ratio | verdict |
|---|---|---|---:|---|
| 079550 | Repeat Cheongung export framework became actionable at 2024-09-20 close. | Waiting for full Green/revision misses a large part of the 180D rerating. | 0.43 | Stage2-Actionable useful; Green not too strict but late. |
| 103140 | Producer conversion and defense/ammunition margin bridge visible at 2024-02-22. | Green can be later but still aligned when margin bridge is present. | 0.32 | Stage2-Actionable plus margin bridge works. |
| 047810 | Formal contract date was not enough because framework had been known and execution/margin bridge lagged. | Any Green at the formal contract date would be premature. | n/a | require delivery/margin confirmation. |
| 024740 | No true Stage2; theme-only RS. | Any Yellow/Green would be false positive. | n/a | block positive stage. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_evidence_type | four_b_timing_verdict |
|---|---:|---:|---|---|
| R1L76_C03_079550_20240920_STAGE2A_REPEAT_EXPORT | 1.0 | 0.46 | valuation_blowoff, positioning_overheat | price_only_local_4B_too_early_before_full_window_export_rerating |
| R1L76_C03_103140_20240222_STAGE2A_AMMO_EXPORT_MARGIN | 0.815 | 0.815 | valuation_blowoff, positioning_overheat, margin_or_backlog_slowdown | good_full_window_4B_timing_when_revision_slowdown_and_valuation_blowoff_appear |
| R1L76_C03_047810_20220916_STAGE2A_FORMAL_CONTRACT_GUARD | 0.33 | 0.33 | contract_delay, margin_or_backlog_slowdown, price_only_local_peak | formal_contract_not_enough_without_margin_or_revision_bridge |
| R1L76_C03_024740_20221004_STAGE2_THEME_REJECTED | 1.0 | 1.0 | price_only_local_peak, positioning_overheat | price_only_local_4B_rejection_not_positive_stage |

The residual is asymmetric: price-only 4B on LIG or 풍산 can be too early before full-window rerating, but price-only/RS theme moves in 한일단조 should be treated as rejected positive-stage candidates from the start.

## 16. 4C Protection Audit

| case_id | four_c_protection_label | interpretation |
|---|---|---|
| 079550 | false_break | Volatility after local peaks did not break the repeat-export system thesis. |
| 103140 | thesis_break_watch_only | 4B overlay was appropriate after valuation/revision slowdown; no hard 4C in the 180D window. |
| 047810 | thesis_break_watch_only | Formal contract survived, but entry was early/late-cycle awkward; route to watch rather than hard 4C. |
| 024740 | hard_4c_success | No company-specific export framework; theme evidence broken for positive-stage use. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L1_defense_export_conversion_gate
scope = L1_INDUSTRIALS_INFRA_DEFENSE_GRID / C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
proposal_type = sector_shadow_only
baseline_value = policy/geopolitical optionality plus relative strength can support Stage2
tested_value = Stage2-Actionable promotion requires at least two non-price conversion anchors: named sovereign buyer, named platform/system, repeat export operator base, order/backlog amount or delivery route, and margin/revision bridge. Theme-only RS is capped at watch/4B overlay.
```

This is not a global delta. It is a narrower R1 defense-export gate: the event must carry its own bridge from headline to backlog and then from backlog to earnings.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = C03_repeat_export_backlog_conversion_bonus_and_theme_cap
positive_gate = named platform + sovereign buyer + order/backlog/delivery route + repeat system/customer quality
counterexample_guard = formal contract without margin/revision bridge is not automatically Green; geopolitical theme-only is blocked from positive Stage2/3
shadow_delta = +2 to repeat_export_backlog_conversion_bonus; -8 to theme_beta_positive_stage_cap
confidence = medium
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current | 4 | all four if uncapped | 32.78 | -13.47 | 69.24 | -14.91 | 0.50 | 2 | mixed: positives captured late, counterexamples over-promoted |
| P0b_e2r_2_0_baseline_reference | rollback reference | 4 | likely even looser RS/theme promotion | 32.78 | -13.47 | 69.24 | -14.91 | 0.50+ | 1 | worse false-positive control |
| P1_sector_specific_candidate_profile | L1 sector shadow | 2 | 079550,103140 only | 57.82 | -10.44 | 125.47 | -10.44 | 0.00 | 0 | better alignment: formal/theme traps excluded |
| P2_canonical_archetype_candidate_profile | C03 canonical shadow | 2 | 079550,103140 only | 57.82 | -10.44 | 125.47 | -10.44 | 0.00 | 0 | best compression for C03 ledger |
| P3_counterexample_guard_profile | guard only | 0 positive entries from 047810/024740 | blocks KAI/한일단조 | null | null | null | null | 0.00 | 0 | guard prevents two C03 residual false positives |

## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| R1L76_C03_POS_079550_20240920_CHEONGUNG_REPEAT_EXPORT_BACKLOG | 84.0 | Stage3-Yellow / actionable_watch | 89.0 | Stage3-Green / Stage2-Actionable-confirmed | 28.67 | -13.18 | aligned_positive |
| R1L76_C03_POS_103140_20240222_AMMUNITION_MARGIN_EXPORT_BRIDGE | 78.0 | Stage3-Yellow / non-C03 classification risk | 84.0 | Stage3-Yellow / Stage2-Actionable-confirmed | 86.97 | -7.70 | aligned_positive |
| R1L76_C03_CEX_047810_20220916_FA50_FORMAL_CONTRACT_HIGH_MAE | 80.0 | Stage3-Yellow false-positive risk | 67.0 | Stage2-Watch / margin-confirmation-required | 4.77 | -20.48 | after_guard_aligns_by_blocking_false_positive_or_high_MAE_entry |
| R1L76_C03_CEX_024740_20221004_NK_MISSILE_THEME_ONLY | 76.0 | Stage3-Yellow false-positive risk | 55.0 | Stage2-Watch / positive-stage-blocked | 10.71 | -12.52 | after_guard_aligns_by_blocking_false_positive_or_high_MAE_entry |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | DEFENSE_REPEAT_EXPORT_BACKLOG_VS_FORMAL_CONTRACT_AND_THEME_BETA | 2 | 2 | 3 | 1 | 4 | 1 | 4 | 4 | 4 | true | true | C03 now has repeat-export positive, formal-contract high-MAE, and geopolitical-theme guard coverage in R1/Loop76. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 1
reused_case_ids: [R1L76_C03_POS_103140_20240222_AMMUNITION_MARGIN_EXPORT_BRIDGE]
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [current_profile_too_late, current_profile_missed_structural, current_profile_too_early, current_profile_false_positive]
new_axis_proposed: C03_repeat_export_backlog_conversion_bonus_and_theme_cap
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope: stock-web tradable raw 1D OHLC rows for 079550, 103140, 047810, and 024740; 30D/90D/180D MFE/MAE; profile corporate-action window check; C03 evidence-field separation. Non-validation scope: live stock selection, current watchlist, production code patch, broker API, and any price after stock-web manifest max date.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C03_repeat_export_backlog_conversion_bonus,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,0,+2,+2,"Repeat sovereign export with named system/platform and backlog/delivery route should be actionable earlier than full Green revision confirmation.","Retains 079550 and 103140 positives while not promoting KAI/한일단조 traps.","R1L76_C03_079550_20240920_STAGE2A_REPEAT_EXPORT|R1L76_C03_103140_20240222_STAGE2A_AMMO_EXPORT_MARGIN",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C03_theme_beta_positive_stage_cap,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,off,on,+1,"Defense geopolitical headline and relative strength without company-specific order/backlog/customer bridge must be capped.","Blocks 024740 and reduces KAI formal-contract overpromotion until margin/revision bridge appears.","R1L76_C03_047810_20220916_STAGE2A_FORMAL_CONTRACT_GUARD|R1L76_C03_024740_20221004_STAGE2_THEME_REJECTED",4,4,2,medium,canonical_shadow_only,"supports existing price-only positive block and full-4B non-price requirement"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation
```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows
```jsonl
{"row_type": "case", "case_id": "R1L76_C03_POS_079550_20240920_CHEONGUNG_REPEAT_EXPORT_BACKLOG", "symbol": "079550", "company_name": "LIG넥스원", "round": "R1", "loop": "76", "scheduled_round": "R1", "scheduled_loop": "76", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_REPEAT_EXPORT_BACKLOG_VS_FORMAL_CONTRACT_AND_THEME_BETA", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R1L76_C03_079550_20240920_STAGE2A_REPEAT_EXPORT", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Iraq Cheongung-II export order following Saudi/UAE demand; named air-defense platform, sovereign buyer, repeat export system, and regulatory filing route despite confidentiality."}
{"row_type": "case", "case_id": "R1L76_C03_POS_103140_20240222_AMMUNITION_MARGIN_EXPORT_BRIDGE", "symbol": "103140", "company_name": "풍산", "round": "R1", "loop": "76", "scheduled_round": "R1", "scheduled_loop": "76", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_REPEAT_EXPORT_BACKLOG_VS_FORMAL_CONTRACT_AND_THEME_BETA", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R1L76_C03_103140_20240222_STAGE2A_AMMO_EXPORT_MARGIN", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "same symbol was used in R4/C15 materials spread; reused here only as new C03 trigger-family compression from commodity spread to ammunition/export margin bridge", "independent_evidence_weight": 0.5, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "Ammunition/defense demand plus copper spread and producer margin bridge; not a pure commodity beta because defense order/margin conversion was visible before the 2024 rerating."}
{"row_type": "case", "case_id": "R1L76_C03_CEX_047810_20220916_FA50_FORMAL_CONTRACT_HIGH_MAE", "symbol": "047810", "company_name": "한국항공우주", "round": "R1", "loop": "76", "scheduled_round": "R1", "scheduled_loop": "76", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_REPEAT_EXPORT_BACKLOG_VS_FORMAL_CONTRACT_AND_THEME_BETA", "case_type": "high_mae_success", "positive_or_counterexample": "counterexample", "best_trigger": "R1L76_C03_047810_20220916_STAGE2A_FORMAL_CONTRACT_GUARD", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_or_guardrail", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "Poland FA-50 formal contract had named platform and buyer, but the trade was late relative to the July framework and was still exposed to configuration/delivery/margin-timing uncertainty."}
{"row_type": "case", "case_id": "R1L76_C03_CEX_024740_20221004_NK_MISSILE_THEME_ONLY", "symbol": "024740", "company_name": "한일단조", "round": "R1", "loop": "76", "scheduled_round": "R1", "scheduled_loop": "76", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_REPEAT_EXPORT_BACKLOG_VS_FORMAL_CONTRACT_AND_THEME_BETA", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "R1L76_C03_024740_20221004_STAGE2_THEME_REJECTED", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_or_guardrail", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "North Korea missile/geopolitical shock moved defense-theme small caps; no company-specific export framework, sovereign buyer, order size, delivery route, or margin bridge was visible."}
```

### 25.3 trigger rows
```jsonl
{"row_type": "trigger", "trigger_id": "R1L76_C03_079550_20240920_STAGE2A_REPEAT_EXPORT", "case_id": "R1L76_C03_POS_079550_20240920_CHEONGUNG_REPEAT_EXPORT_BACKLOG", "symbol": "079550", "company_name": "LIG넥스원", "round": "R1", "loop": "76", "scheduled_round": "R1", "scheduled_loop": "76", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_REPEAT_EXPORT_BACKLOG_VS_FORMAL_CONTRACT_AND_THEME_BETA", "sector": "industrials_defense_export", "primary_archetype": "defense_export_framework_backlog", "loop_objective": "residual_false_positive_mining|residual_missed_structural_mining|stage2_actionable_bonus_stress_test|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-09-20", "evidence_available_at_that_date": "Iraq Cheongung-II export order following Saudi/UAE demand; named air-defense platform, sovereign buyer, repeat export system, and regulatory filing route despite confidentiality.", "evidence_source": "Reuters 2024-09-20; stock-web 079550 2024/2025 shards", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "policy_or_regulatory_optionality", "backlog_or_delivery_visibility", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources", "durable_customer_confirmation", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv|atlas/ohlcv_tradable_by_symbol_year/079/079550/2025.csv", "profile_path": "atlas/symbol_profiles/079/079550.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-09-20", "entry_price": 211000, "MFE_30D_pct": 25.59, "MFE_90D_pct": 28.67, "MFE_180D_pct": 163.98, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.42, "MAE_90D_pct": -13.18, "MAE_180D_pct": -13.18, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-06-16", "peak_price": 557000, "drawdown_after_peak_pct": -3.95, "green_lateness_ratio": 0.43, "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 0.46, "four_b_timing_verdict": "price_only_local_4B_too_early_before_full_window_export_rerating", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "false_break", "trigger_outcome_label": "structural_success_repeat_export_backlog", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L76_C03_POS_079550_20240920_CHEONGUNG_REPEAT_EXPORT_BACKLOG::2024-09-20::211000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L76_C03_103140_20240222_STAGE2A_AMMO_EXPORT_MARGIN", "case_id": "R1L76_C03_POS_103140_20240222_AMMUNITION_MARGIN_EXPORT_BRIDGE", "symbol": "103140", "company_name": "풍산", "round": "R1", "loop": "76", "scheduled_round": "R1", "scheduled_loop": "76", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_REPEAT_EXPORT_BACKLOG_VS_FORMAL_CONTRACT_AND_THEME_BETA", "sector": "industrials_defense_export", "primary_archetype": "defense_export_framework_backlog", "loop_objective": "residual_false_positive_mining|residual_missed_structural_mining|stage2_actionable_bonus_stress_test|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-22", "evidence_available_at_that_date": "Ammunition/defense demand plus copper spread and producer margin bridge; not a pure commodity beta because defense order/margin conversion was visible before the 2024 rerating.", "evidence_source": "Prior stock-web R4/C15 producer-conversion row reclassified as C03 secondary defense-export margin bridge; 103140 2024 shard", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route", "backlog_or_delivery_visibility", "early_revision_signal", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "durable_customer_confirmation", "low_red_team_risk"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv", "profile_path": "atlas/symbol_profiles/103/103140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-22", "entry_price": 42200, "MFE_30D_pct": 26.07, "MFE_90D_pct": 86.97, "MFE_180D_pct": 86.97, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.7, "MAE_90D_pct": -7.7, "MAE_180D_pct": -7.7, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-14", "peak_price": 78900, "drawdown_after_peak_pct": -40.43, "green_lateness_ratio": 0.32, "four_b_local_peak_proximity": 0.815, "four_b_full_window_peak_proximity": 0.815, "four_b_timing_verdict": "good_full_window_4B_timing_when_revision_slowdown_and_valuation_blowoff_appear", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success_margin_export_bridge", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L76_C03_POS_103140_20240222_AMMUNITION_MARGIN_EXPORT_BRIDGE::2024-02-22::42200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same symbol was used in R4/C15 materials spread; reused here only as new C03 trigger-family compression from commodity spread to ammunition/export margin bridge", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L76_C03_047810_20220916_STAGE2A_FORMAL_CONTRACT_GUARD", "case_id": "R1L76_C03_CEX_047810_20220916_FA50_FORMAL_CONTRACT_HIGH_MAE", "symbol": "047810", "company_name": "한국항공우주", "round": "R1", "loop": "76", "scheduled_round": "R1", "scheduled_loop": "76", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_REPEAT_EXPORT_BACKLOG_VS_FORMAL_CONTRACT_AND_THEME_BETA", "sector": "industrials_defense_export", "primary_archetype": "defense_export_framework_backlog", "loop_objective": "residual_false_positive_mining|residual_missed_structural_mining|stage2_actionable_bonus_stress_test|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable-formal-contract", "trigger_date": "2022-09-16", "evidence_available_at_that_date": "Poland FA-50 formal contract had named platform and buyer, but the trade was late relative to the July framework and was still exposed to configuration/delivery/margin-timing uncertainty.", "evidence_source": "KAI/Poland FA-50 contract public-source proxy; stock-web 047810 2022/2023 shards", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "policy_or_regulatory_optionality", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["contract_delay", "margin_or_backlog_slowdown", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047810/2022.csv|atlas/ohlcv_tradable_by_symbol_year/047/047810/2023.csv", "profile_path": "atlas/symbol_profiles/047/047810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-09-16", "entry_price": 50300, "MFE_30D_pct": 4.77, "MFE_90D_pct": 4.77, "MFE_180D_pct": 15.31, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -20.48, "MAE_90D_pct": -20.48, "MAE_180D_pct": -20.48, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-19", "peak_price": 58000, "drawdown_after_peak_pct": -18.97, "green_lateness_ratio": "not_applicable_contract_already_repriced", "four_b_local_peak_proximity": 0.33, "four_b_full_window_peak_proximity": 0.33, "four_b_timing_verdict": "formal_contract_not_enough_without_margin_or_revision_bridge", "four_b_evidence_type": ["contract_delay", "margin_or_backlog_slowdown", "price_only_local_peak"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "formal_contract_high_MAE_counterexample", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L76_C03_CEX_047810_20220916_FA50_FORMAL_CONTRACT_HIGH_MAE::2022-09-16::50300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L76_C03_024740_20221004_STAGE2_THEME_REJECTED", "case_id": "R1L76_C03_CEX_024740_20221004_NK_MISSILE_THEME_ONLY", "symbol": "024740", "company_name": "한일단조", "round": "R1", "loop": "76", "scheduled_round": "R1", "scheduled_loop": "76", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_REPEAT_EXPORT_BACKLOG_VS_FORMAL_CONTRACT_AND_THEME_BETA", "sector": "industrials_defense_export", "primary_archetype": "defense_export_framework_backlog", "loop_objective": "residual_false_positive_mining|residual_missed_structural_mining|stage2_actionable_bonus_stress_test|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Theme / geopolitical headline-only", "trigger_date": "2022-10-04", "evidence_available_at_that_date": "North Korea missile/geopolitical shock moved defense-theme small caps; no company-specific export framework, sovereign buyer, order size, delivery route, or margin bridge was visible.", "evidence_source": "Historical geopolitical headline family, 2022-10-04; stock-web 024740 2022/2023 shards", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/024/024740/2022.csv|atlas/ohlcv_tradable_by_symbol_year/024/024740/2023.csv", "profile_path": "atlas/symbol_profiles/024/024740.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-10-04", "entry_price": 3035, "MFE_30D_pct": 10.71, "MFE_90D_pct": 10.71, "MFE_180D_pct": 10.71, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.23, "MAE_90D_pct": -12.52, "MAE_180D_pct": -18.29, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-10-11", "peak_price": 3360, "drawdown_after_peak_pct": -26.19, "green_lateness_ratio": "not_applicable_headline_only", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_rejection_not_positive_stage", "four_b_evidence_type": ["price_only_local_peak", "positioning_overheat"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "theme_only_failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L76_C03_CEX_024740_20221004_NK_MISSILE_THEME_ONLY::2022-10-04::3035", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

### 25.4 score_simulation rows
```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L76_C03_POS_079550_20240920_CHEONGUNG_REPEAT_EXPORT_BACKLOG", "trigger_id": "R1L76_C03_079550_20240920_STAGE2A_REPEAT_EXPORT", "symbol": "079550", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 12, "backlog_visibility_score": 12, "margin_bridge_score": 5, "revision_score": 4, "relative_strength_score": 10, "customer_quality_score": 12, "policy_or_regulatory_score": 8, "valuation_repricing_score": 5, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "export_framework_score": 12, "repeat_system_score": 10}, "weighted_score_before": 84.0, "stage_label_before": "Stage3-Yellow / actionable_watch", "raw_component_scores_after": {"contract_score": 13, "backlog_visibility_score": 14, "margin_bridge_score": 5, "revision_score": 4, "relative_strength_score": 10, "customer_quality_score": 13, "policy_or_regulatory_score": 9, "valuation_repricing_score": 5, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "export_framework_score": 15, "repeat_system_score": 13}, "weighted_score_after": 89.0, "stage_label_after": "Stage3-Green / Stage2-Actionable-confirmed", "changed_components": ["export_framework_score", "repeat_system_score", "backlog_visibility_score", "customer_quality_score"], "component_delta_explanation": "C03 shadow rewards repeat sovereign export backlog conversion but caps formal-contract/high-MAE and geopolitical theme-only positive promotion.", "MFE_90D_pct": 28.67, "MAE_90D_pct": -13.18, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L76_C03_POS_103140_20240222_AMMUNITION_MARGIN_EXPORT_BRIDGE", "trigger_id": "R1L76_C03_103140_20240222_STAGE2A_AMMO_EXPORT_MARGIN", "symbol": "103140", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 6, "margin_bridge_score": 6, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 4, "policy_or_regulatory_score": 3, "valuation_repricing_score": 2, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "export_framework_score": 4, "producer_conversion_score": 8}, "weighted_score_before": 78.0, "stage_label_before": "Stage3-Yellow / non-C03 classification risk", "raw_component_scores_after": {"contract_score": 6, "backlog_visibility_score": 7, "margin_bridge_score": 8, "revision_score": 5, "relative_strength_score": 7, "customer_quality_score": 5, "policy_or_regulatory_score": 3, "valuation_repricing_score": 2, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "export_framework_score": 6, "producer_conversion_score": 9}, "weighted_score_after": 84.0, "stage_label_after": "Stage3-Yellow / Stage2-Actionable-confirmed", "changed_components": ["margin_bridge_score", "producer_conversion_score", "export_framework_score"], "component_delta_explanation": "C03 shadow rewards repeat sovereign export backlog conversion but caps formal-contract/high-MAE and geopolitical theme-only positive promotion.", "MFE_90D_pct": 86.97, "MAE_90D_pct": -7.7, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L76_C03_CEX_047810_20220916_FA50_FORMAL_CONTRACT_HIGH_MAE", "trigger_id": "R1L76_C03_047810_20220916_STAGE2A_FORMAL_CONTRACT_GUARD", "symbol": "047810", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 12, "backlog_visibility_score": 10, "margin_bridge_score": 2, "revision_score": 1, "relative_strength_score": 5, "customer_quality_score": 10, "policy_or_regulatory_score": 8, "valuation_repricing_score": 4, "execution_risk_score": -5, "legal_or_contract_risk_score": -1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "export_framework_score": 10, "delivery_execution_score": 3}, "weighted_score_before": 80.0, "stage_label_before": "Stage3-Yellow false-positive risk", "raw_component_scores_after": {"contract_score": 11, "backlog_visibility_score": 8, "margin_bridge_score": 2, "revision_score": 1, "relative_strength_score": 3, "customer_quality_score": 10, "policy_or_regulatory_score": 8, "valuation_repricing_score": 3, "execution_risk_score": -8, "legal_or_contract_risk_score": -1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "export_framework_score": 8, "delivery_execution_score": 0}, "weighted_score_after": 67.0, "stage_label_after": "Stage2-Watch / margin-confirmation-required", "changed_components": ["execution_risk_score", "delivery_execution_score", "export_framework_score_cap", "relative_strength_score_cap"], "component_delta_explanation": "C03 shadow rewards repeat sovereign export backlog conversion but caps formal-contract/high-MAE and geopolitical theme-only positive promotion.", "MFE_90D_pct": 4.77, "MAE_90D_pct": -20.48, "score_return_alignment_label": "after_guard_aligns_by_blocking_false_positive_or_high_MAE_entry", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L76_C03_CEX_024740_20221004_NK_MISSILE_THEME_ONLY", "trigger_id": "R1L76_C03_024740_20221004_STAGE2_THEME_REJECTED", "symbol": "024740", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 5, "valuation_repricing_score": 4, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "export_framework_score": 0, "theme_beta_score": 10}, "weighted_score_before": 76.0, "stage_label_before": "Stage3-Yellow false-positive risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 6, "customer_quality_score": 0, "policy_or_regulatory_score": 3, "valuation_repricing_score": 2, "execution_risk_score": -10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "export_framework_score": 0, "theme_beta_score": 2}, "weighted_score_after": 55.0, "stage_label_after": "Stage2-Watch / positive-stage-blocked", "changed_components": ["relative_strength_score_cap", "theme_beta_score_block", "policy_or_regulatory_score_cap"], "component_delta_explanation": "C03 shadow rewards repeat sovereign export backlog conversion but caps formal-contract/high-MAE and geopolitical theme-only positive promotion.", "MFE_90D_pct": 10.71, "MAE_90D_pct": -12.52, "score_return_alignment_label": "after_guard_aligns_by_blocking_false_positive_or_high_MAE_entry", "current_profile_verdict": "current_profile_false_positive"}
```

### 25.5 shadow_weight rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C03_repeat_export_backlog_conversion_bonus,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,0,+2,+2,"repeat sovereign export with named platform/system and backlog route","positive rows keep high 180D MFE while formal/theme traps are excluded","R1L76_C03_079550_20240920_STAGE2A_REPEAT_EXPORT|R1L76_C03_103140_20240222_STAGE2A_AMMO_EXPORT_MARGIN",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C03_theme_beta_positive_stage_cap,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,off,on,+1,"formal contract without conversion and geopolitical theme-only RS must be capped","blocks 047810 high-MAE and 024740 theme-only false positive","R1L76_C03_047810_20220916_STAGE2A_FORMAL_CONTRACT_GUARD|R1L76_C03_024740_20221004_STAGE2_THEME_REJECTED",4,4,2,medium,canonical_shadow_only,"supports existing positive-stage price-only block"
```

### 25.6 residual_contribution row
```jsonl
{"row_type": "residual_contribution", "round": "R1", "loop": "76", "scheduled_round": "R1", "scheduled_loop": "76", "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "new_independent_case_count": 4, "reused_case_count": 1, "new_symbol_count": 3, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["current_profile_too_late", "current_profile_missed_structural", "current_profile_too_early", "current_profile_false_positive"], "diversity_score_summary": "same_archetype_new_symbol_bonus=+12; counterexample_gap_bonus=+8; residual_error_bonus=+20; wrong_round_penalty=0; duplicate_key_conflict=0", "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only rows
```jsonl
{"row_type": "narrative_only", "case_id": "none", "symbol": null, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "reason": "all selected representative triggers had clean 180D stock-web windows; no narrative-only case needed", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
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
completed_round = R1
completed_loop = 76
next_round = R2
next_loop = 76
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-web manifest: `atlas/manifest.json`; checked fields include `max_date=2026-02-20`, `tradable_row_count=14354401`, `raw_row_count=15214118`, and `price_adjustment_status=raw_unadjusted_marcap`.
- Stock-web schema: `atlas/schema.json`; MFE/MAE formula and calibration usability rules follow schema text.
- 079550 source event: Reuters reported on 2024-09-20 that LIG Nex1 won a 3.71 trillion won Iraq missile-defense order and referenced the earlier Saudi Cheongung-II deal.
- 047810 source event: public Poland FA-50 sources record the 2022 Poland FA-50 order/contract route; stock-web price path shows high-MAE/late-entry behavior rather than immediate structural success from the formal contract date.
- 103140 source event: reused from prior stock-web C15 producer-conversion row as a new C03 defense/ammunition export-margin bridge compression; independent evidence weight is 0.5, not 1.0.
- 024740 source event: treated as geopolitical headline/theme-only proxy; no company-specific export/backlog/customer bridge was used for positive-stage evidence.


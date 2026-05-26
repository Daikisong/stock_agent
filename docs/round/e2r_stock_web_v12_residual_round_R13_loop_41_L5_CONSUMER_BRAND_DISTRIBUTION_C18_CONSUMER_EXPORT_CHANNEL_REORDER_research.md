# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata


mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
round: R13
loop: 41
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: K_FOOD_BULDAK_GLOBAL_REORDER_MARGIN_BRIDGE / K_FOOD_ICECREAM_GLOBAL_REORDER_SEASONAL_EXPORT / K_FOOD_MATURE_GLOBAL_CAPACITY_WITHOUT_RERATING / APPAREL_CHINA_CHANNEL_INVENTORY_REORDER_RISK
output_file: e2r_stock_web_v12_residual_round_R13_loop_41_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_web_price_atlas_access_required: true

## 1. Current Calibrated Profile Assumption

Current proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`. Existing global axes are kept, not re-proposed: `stage2_actionable_evidence_bonus`, Stage3 Yellow/Green thresholds, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`, and hard 4C thesis-break routing. This loop tests whether C18 needs a narrower channel-reorder rule.

## 2. Round / Large Sector / Canonical Archetype Scope

Scope is L5 consumer brands/distribution, canonical archetype C18. The loop deliberately avoids repeating the previous C20 beauty/global distribution file. C18 is treated as a broader consumer export-channel problem: food export reorder, seasonal consumer export rerating, mature global footprint, and concentrated apparel/China-channel risk.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifact check used only ingest-level coverage. The ingest summary reported 107 parsed result MDs, 1,940 validated trigger rows, 1,376 aggregate representative rows, R1~R13 coverage and loop 1~9 coverage. This loop uses four new symbols and is therefore independent from the immediately preceding C20 beauty file. The new independent case ratio is 1.00, above the required 0.60.

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
| --- | --- |
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

Schema basis: tradable shards use `d,o,h,l,c,v,a,mc,s,m`; MFE/MAE follows `(max high or min low from entry_date through N tradable rows / entry_price - 1) * 100`. The manifest max date is 2026-02-20, so every 180D window used here is observable inside stock-web.

## 5. Historical Eligibility Gate

| case_id | symbol | profile_path | 180D window | corporate action overlap | calibration_usable |
| --- | --- | --- | --- | --- | --- |
| R13L41_C18_SAMYANG_003230_EXPORT_REORDER | 003230 | atlas/symbol_profiles/003/003230.json | available | none in entry~D+180 | True |
| R13L41_C18_BINGGRAE_005180_EXPORT_REORDER | 005180 | atlas/symbol_profiles/005/005180.json | available | none in entry~D+180 | True |
| R13L41_C18_NONGSHIM_004370_GLOBAL_MATURE | 004370 | atlas/symbol_profiles/004/004370.json | available | none in entry~D+180 | True |
| R13L41_C18_FNF_383220_CHINA_CHANNEL_RISK | 383220 | atlas/symbol_profiles/383/383220.json | available | none in entry~D+180 | True |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression note |
| --- | --- | --- |
| K_FOOD_BULDAK_GLOBAL_REORDER_MARGIN_BRIDGE | C18_CONSUMER_EXPORT_CHANNEL_REORDER | repeat global reorder + margin bridge |
| K_FOOD_ICECREAM_GLOBAL_REORDER_SEASONAL_EXPORT | C18_CONSUMER_EXPORT_CHANNEL_REORDER | valid reorder but seasonal/positioning constrained |
| K_FOOD_MATURE_GLOBAL_CAPACITY_WITHOUT_RERATING | C18_CONSUMER_EXPORT_CHANNEL_REORDER | mature global presence, weak reorder acceleration |
| APPAREL_CHINA_CHANNEL_INVENTORY_REORDER_RISK | C18_CONSUMER_EXPORT_CHANNEL_REORDER | channel concentration/inventory counterexample |

## 7. Case Selection Summary

| case_id | symbol | company | case_type | positive/counterexample | best_trigger | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- |
| R13L41_C18_SAMYANG_003230_EXPORT_REORDER | 003230 | 삼양식품 | structural_success | positive | R13L41_C18_SAMYANG_STAGE2_2023_11_16 | current_profile_too_late |
| R13L41_C18_BINGGRAE_005180_EXPORT_REORDER | 005180 | 빙그레 | high_mae_success | positive | R13L41_C18_BINGGRAE_STAGE2_2024_05_16 | current_profile_4B_too_late |
| R13L41_C18_NONGSHIM_004370_GLOBAL_MATURE | 004370 | 농심 | failed_rerating | counterexample | R13L41_C18_NONGSHIM_STAGE2_2023_08_11 | current_profile_false_positive |
| R13L41_C18_FNF_383220_CHINA_CHANNEL_RISK | 383220 | F&F | false_positive_green | counterexample | R13L41_C18_FNF_STAGE2_2023_08_01 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

Positive structural / high-MFE cases: Samyang Foods and Binggrae. Counterexamples: Nongshim as mature overseas footprint without rerating, and F&F as concentrated overseas channel/inventory risk. Balance: positive_case_count=2, counterexample_count=2, 4B/4C overlay cases=4.

## 9. Evidence Source Map

| symbol | trigger family | Stage2 evidence | Stage3 evidence | 4B/4C evidence separation |
| --- | --- | --- | --- | --- |
| 003230 | Stage2-Actionable | public_event_or_disclosure, customer_or_order_quality, capacity_or_volume_route, early_revision_signal | financial_visibility |  |
| 003230 | Stage3-Green | relative_strength, early_revision_signal | confirmed_revision, margin_bridge, multiple_public_sources, financial_visibility |  |
| 003230 | 4B |  | confirmed_revision, margin_bridge | valuation_blowoff, positioning_overheat, price_only_local_peak |
| 005180 | Stage2-Actionable | public_event_or_disclosure, customer_or_order_quality, relative_strength, early_revision_signal | financial_visibility |  |
| 005180 | 4B |  | financial_visibility | valuation_blowoff, positioning_overheat, margin_or_backlog_slowdown |
| 004370 | Stage2-Actionable | public_event_or_disclosure, capacity_or_volume_route | financial_visibility |  |
| 004370 | 4C-watch |  |  | thesis_evidence_broken |
| 383220 | Stage2-Actionable | public_event_or_disclosure, customer_or_order_quality | financial_visibility | margin_or_backlog_slowdown |
| 383220 | 4C |  |  | margin_or_backlog_slowdown, call_off_or_order_cut, thesis_evidence_broken |

## 10. Price Data Source Map

| symbol | company | profile | main shard paths used |
| --- | --- | --- | --- |
| 003230 | 삼양식품 | atlas/symbol_profiles/003/003230.json | atlas/ohlcv_tradable_by_symbol_year/003/003230/2023.csv / atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv |
| 005180 | 빙그레 | atlas/symbol_profiles/005/005180.json | atlas/ohlcv_tradable_by_symbol_year/005/005180/2023.csv / atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv |
| 004370 | 농심 | atlas/symbol_profiles/004/004370.json | atlas/ohlcv_tradable_by_symbol_year/004/004370/2023.csv / atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv |
| 383220 | F&F | atlas/symbol_profiles/383/383220.json | atlas/ohlcv_tradable_by_symbol_year/383/383220/2023.csv / atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | type | trigger_date | entry_date | entry_price | dedupe | role |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R13L41_C18_SAMYANG_STAGE2_2023_11_16 | R13L41_C18_SAMYANG_003230_EXPORT_REORDER | Stage2-Actionable | 2023-11-15 | 2023-11-16 | 197600 | True | representative |
| R13L41_C18_SAMYANG_GREEN_2024_05_17 | R13L41_C18_SAMYANG_003230_EXPORT_REORDER | Stage3-Green | 2024-05-16 | 2024-05-17 | 446500 | False | label_comparison_only |
| R13L41_C18_SAMYANG_4B_2024_06_18 | R13L41_C18_SAMYANG_003230_EXPORT_REORDER | 4B | 2024-06-18 | 2024-06-18 | 712000 | False | 4B_overlay_only |
| R13L41_C18_BINGGRAE_STAGE2_2024_05_16 | R13L41_C18_BINGGRAE_005180_EXPORT_REORDER | Stage2-Actionable | 2024-05-16 | 2024-05-16 | 75600 | True | representative |
| R13L41_C18_BINGGRAE_4B_2024_06_10 | R13L41_C18_BINGGRAE_005180_EXPORT_REORDER | 4B | 2024-06-10 | 2024-06-10 | 112100 | False | 4B_overlay_only |
| R13L41_C18_NONGSHIM_STAGE2_2023_08_11 | R13L41_C18_NONGSHIM_004370_GLOBAL_MATURE | Stage2-Actionable | 2023-08-11 | 2023-08-11 | 459000 | True | representative |
| R13L41_C18_NONGSHIM_4C_WATCH_2024_02_29 | R13L41_C18_NONGSHIM_004370_GLOBAL_MATURE | 4C-watch | 2024-02-29 | 2024-02-29 | 348000 | False | 4C_overlay_only |
| R13L41_C18_FNF_STAGE2_2023_08_01 | R13L41_C18_FNF_383220_CHINA_CHANNEL_RISK | Stage2-Actionable | 2023-08-01 | 2023-08-01 | 104000 | True | representative |
| R13L41_C18_FNF_4C_2024_01_15 | R13L41_C18_FNF_383220_CHINA_CHANNEL_RISK | 4C | 2024-01-15 | 2024-01-15 | 76400 | False | 4C_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | drawdown_after_peak |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13L41_C18_SAMYANG_STAGE2_2023_11_16 | 2023-11-16 @ 197600 | 18.17 | -4.15 | 21.2 | -14.17 | 263.36 | -14.17 | 2024-06-19 @ 718000 | -34.56 |
| R13L41_C18_SAMYANG_GREEN_2024_05_17 | 2024-05-17 @ 446500 | 60.81 | 0.0 | 60.81 | 0.0 | 60.81 | 0.0 | 2024-06-19 @ 718000 | -34.56 |
| R13L41_C18_SAMYANG_4B_2024_06_18 | 2024-06-18 @ 712000 | 0.84 | -18.4 | 0.84 | -36.03 | 0.84 | -36.03 | 2024-06-19 @ 718000 | -34.56 |
| R13L41_C18_BINGGRAE_STAGE2_2024_05_16 | 2024-05-16 @ 75600 | 56.61 | -5.56 | 56.61 | -21.69 | 56.61 | -21.69 | 2024-06-11 @ 118400 | -50.0 |
| R13L41_C18_BINGGRAE_4B_2024_06_10 | 2024-06-10 @ 112100 | 5.62 | -20.52 | 5.62 | -47.19 | 5.62 | -47.19 | 2024-06-11 @ 118400 | -50.0 |
| R13L41_C18_NONGSHIM_STAGE2_2023_08_11 | 2023-08-11 @ 459000 | 6.75 | -6.32 | 8.93 | -13.18 | 8.93 | -24.29 | 2023-10-10 @ 500000 | -30.5 |
| R13L41_C18_NONGSHIM_4C_WATCH_2024_02_29 | 2024-02-29 @ 348000 | 11.06 | -0.14 | 57.76 | -0.14 | 57.76 | -0.14 | 2024-06-11 @ 549000 | -18.03 |
| R13L41_C18_FNF_STAGE2_2023_08_01 | 2023-08-01 @ 104000 | 14.81 | -6.63 | 15.38 | -23.75 | 15.38 | -40.67 | 2023-09-19 @ 120000 | -48.58 |
| R13L41_C18_FNF_4C_2024_01_15 | 2024-01-15 @ 76400 | 1.31 | -13.09 | 1.31 | -19.24 | 1.31 | -28.66 | 2024-04-01 @ 77400 | -29.59 |

## 13. Current Calibrated Profile Stress Test

| case | current judgment | MFE/MAE fit | axis stress result |
| --- | --- | --- | --- |
| R13L41_C18_SAMYANG_003230_EXPORT_REORDER | current_profile_too_late | early export/reorder evidence captured very large 180D upside; Green confirmation arrived after a large part of the move had begun | Stage2 bonus is useful only with real reorder; Yellow/Green too loose for mature channel, too late for fast reorder |
| R13L41_C18_BINGGRAE_005180_EXPORT_REORDER | current_profile_4B_too_late | rapid export/channel rerating worked, but only as a short-cycle run; 4B overlay needed faster seasonal/positioning recognition | Stage2 bonus is useful only with real reorder; Yellow/Green too loose for mature channel, too late for fast reorder |
| R13L41_C18_NONGSHIM_004370_GLOBAL_MATURE | current_profile_false_positive | global footprint was real but mature; upside was single-digit while 180D drawdown exceeded 20% | Stage2 bonus is useful only with real reorder; Yellow/Green too loose for mature channel, too late for fast reorder |
| R13L41_C18_FNF_383220_CHINA_CHANNEL_RISK | current_profile_false_positive | brand/channel export story produced brief rallies but later price path punished inventory/channel concentration risk | Stage2 bonus is useful only with real reorder; Yellow/Green too loose for mature channel, too late for fast reorder |

## 14. Stage2 / Yellow / Green Comparison

Samyang shows that a strict Green can arrive late in fast export-reorder cycles: Stage2 entry 197,600 vs Green entry 446,500, with local 180D peak 718,000. Green lateness ratio is recorded as 0.52, meaning Green missed roughly half of the Stage2-to-peak upside. Binggrae shows a different pattern: Stage2 was effective, but confirmation should not imply long-duration Green when seasonal export and positioning risk dominate.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | local proximity | full-window proximity | verdict | evidence_type |
| --- | --- | --- | --- | --- |
| R13L41_C18_SAMYANG_4B_2024_06_18 | 0.99 | 0.52 | price_only_local_4B_too_early | price_only|valuation_blowoff|positioning_overheat |
| R13L41_C18_BINGGRAE_4B_2024_06_10 | 0.96 | 0.96 | good_full_window_4B_timing | valuation_blowoff|positioning_overheat|margin_or_backlog_slowdown |

Interpretation: Samyang's June 2024 4B was a local blowoff, not a full-cycle thesis exit. Binggrae's June 2024 4B was much closer to a full-window peak because the price reversed with seasonality and positioning risk. Therefore C18 needs a sector-specific seasonal 4B overlay, but it must not demote structural Buldak-style reorder too early.

## 16. 4C Protection Audit

F&F is the clean hard-4C example: after the 2024-01-15 thesis-break route, MFE_90D was only 1.31% while MAE_90D was -19.24% and MAE_180D was -28.66%. Nongshim is the false-break counterexample: price weakness alone in February 2024 would have misrouted a mature export case to hard 4C before recovery, so hard 4C must require evidence break, not price-only drawdown.

## 17. Sector-Specific Rule Candidate

`L5_seasonal_consumer_export_4B_overlay`: for consumer export cycles with seasonal product mix and short-channel inventory, add a 4B overlay when valuation/positioning blowoff aligns with seasonality or channel margin peak. Do not apply as a full exit when repeat reorder remains structurally expanding across multiple regions.

## 18. Canonical-Archetype Rule Candidate

`C18_repeat_reorder_sell_through_bonus`: promotion above Stage2/Yellow requires at least two of: repeat reorder evidence, sell-through/channel velocity, multi-region channel expansion, revision/margin bridge. `C18_mature_overseas_presence_cap` penalizes global footprint without acceleration. `C18_single_channel_inventory_risk_guard` blocks Green when one geography/channel drives the story and inventory/sell-through is unresolved.

## 19. Before / After Backtest Comparison

| profile | scope | eligible | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | FP rate | missed | late Green | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 4 | 25.08 | -18.45 | 86.99 | -25.2 | 0.5 | 1 | 1 | mixed; catches some Stage2 but overpromotes mature/global-channel narratives |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 4 | 25.08 | -18.45 | 86.99 | -25.2 | 0.5 | 2 | 2 | worse; too many narrative positives and late 4B |
| P1_L5_sector_export_channel_shadow | sector_specific | 4 | 35.03 | -13.9 | 159.99 | -17.93 | 0.25 | 1 | 1 | better positive/counterexample separation |
| P2_C18_canonical_reorder_shadow | canonical_archetype_specific | 4 | 35.03 | -13.9 | 159.99 | -17.93 | 0.25 | 0 | 0 | best explanatory profile for this loop |
| P3_C18_counterexample_guard | counterexample_guard | 4 | 35.03 | -10.7 | 159.99 | -15.2 | 0.0 | 1 | 0 | best false-positive guard, slightly stricter on positives |

## 20. Score-Return Alignment Matrix

| trigger_id | score_before | label_before | score_after | label_after | MFE90 | MAE90 | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R13L41_C18_SAMYANG_STAGE2_2023_11_16 | 78.0 | Stage3-Yellow | 84.0 | Stage3-Yellow+Actionable | 21.2 | -14.17 | structural_success |
| R13L41_C18_SAMYANG_GREEN_2024_05_17 | 90.0 | Stage3-Green | 92.0 | Stage3-Green | 60.81 | 0.0 | late_green_but_success |
| R13L41_C18_SAMYANG_4B_2024_06_18 | 88.0 | 4B-watch | 86.0 | 4B-local-only | 0.84 | -36.03 | 4B_local_peak_but_full_cycle_too_early |
| R13L41_C18_BINGGRAE_STAGE2_2024_05_16 | 77.0 | Stage3-Yellow | 82.0 | Stage2-Actionable/Yellow | 56.61 | -21.69 | high_mfe_success_with_high_mae_after_peak |
| R13L41_C18_BINGGRAE_4B_2024_06_10 | 83.0 | Stage3-Yellow/4B-watch | 80.0 | 4B-full-window | 5.62 | -47.19 | 4B_overlay_success |
| R13L41_C18_NONGSHIM_STAGE2_2023_08_11 | 72.0 | Stage2 | 66.0 | Stage2-capped | 8.93 | -13.18 | failed_rerating |
| R13L41_C18_NONGSHIM_4C_WATCH_2024_02_29 | 58.0 | 4C-watch | 62.0 | false-break-watch | 57.76 | -0.14 | false_break_not_4C |
| R13L41_C18_FNF_STAGE2_2023_08_01 | 76.0 | Stage3-Yellow | 64.0 | Stage2-capped | 15.38 | -23.75 | false_positive_green |
| R13L41_C18_FNF_4C_2024_01_15 | 61.0 | 4B/4C-watch | 55.0 | 4C-route | 1.31 | -19.24 | 4C_success |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L5_CONSUMER_BRAND_DISTRIBUTION | C18_CONSUMER_EXPORT_CHANNEL_REORDER | multiple | 2 | 2 | 2 | 2 | 4 | 0 | 9 | 4 | 4 | True | True | Need C18 across non-food consumer exports and online-only brands |

## 22. Residual Contribution Summary


new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 4
new_trigger_family_count: 5
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: mature_export_false_positive, seasonal_export_4B_too_late, green_confirmation_late_for_fast_reorder, single_channel_inventory_false_positive
new_axis_proposed: C18_repeat_reorder_sell_through_bonus, C18_mature_overseas_presence_cap, C18_single_channel_inventory_risk_guard, L5_seasonal_consumer_export_4B_overlay
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus, Yellow/Green thresholds
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate

## 23. Validation Scope / Non-Validation Scope

Validated: actual stock-web tradable OHLC rows, entry prices, MFE/MAE 30/90/180D, clean 180D corporate-action windows, L5/C18 coverage, positive/counterexample balance, same-entry dedupe. Not validated: live candidate discovery, broker API, current recommendation, production scoring code, exact analyst-consensus feed, intraday disclosure timestamps beyond conservative next-trading-day assumptions.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C18_repeat_reorder_sell_through_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,+2,+2,"Repeat reorder plus sell-through separates Samyang/Binggrae from mature or concentrated channels","raises positive Stage2/Yellow while preserving non-price evidence gate","R13L41_C18_SAMYANG_STAGE2_2023_11_16|R13L41_C18_BINGGRAE_STAGE2_2024_05_16",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C18_mature_overseas_presence_cap,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,-2,-2,"Global footprint without acceleration failed on Nongshim-like mature export narratives","reduces false positive green/yellow promotion","R13L41_C18_NONGSHIM_STAGE2_2023_08_11",4,4,2,medium,counterexample_guard,"not production; post-calibrated residual"
shadow_weight,C18_single_channel_inventory_risk_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,-3,-3,"China/apparel channel concentration and inventory risk broke F&F-style export stories","blocks false positive promotion and improves 4C routing","R13L41_C18_FNF_STAGE2_2023_08_01|R13L41_C18_FNF_4C_2024_01_15",4,4,2,medium,counterexample_guard,"not production; post-calibrated residual"
shadow_weight,L5_seasonal_consumer_export_4B_overlay,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,+1,+1,"Seasonal food export reratings can peak before confirmed long-cycle revision fades","improves Binggrae 4B timing without weakening Samyang structural case","R13L41_C18_BINGGRAE_4B_2024_06_10",4,4,2,low,sector_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation
```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows
```jsonl
{"row_type":"case","case_id":"R13L41_C18_SAMYANG_003230_EXPORT_REORDER","symbol":"003230","company_name":"삼양식품","round":"R13","loop":"41","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_BULDAK_GLOBAL_REORDER_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R13L41_C18_SAMYANG_STAGE2_2023_11_16","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"early export/reorder evidence captured very large 180D upside; Green confirmation arrived after a large part of the move had begun","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Buldak-led global reorder and export mix improvement acted like an operating-leverage flywheel; price path validates Stage2-Actionable earlier than Green."}
{"row_type":"case","case_id":"R13L41_C18_BINGGRAE_005180_EXPORT_REORDER","symbol":"005180","company_name":"빙그레","round":"R13","loop":"41","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_ICECREAM_GLOBAL_REORDER_SEASONAL_EXPORT","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R13L41_C18_BINGGRAE_STAGE2_2024_05_16","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"rapid export/channel rerating worked, but only as a short-cycle run; 4B overlay needed faster seasonal/positioning recognition","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Strong MFE came quickly, then reversed; this is a good example of C18 where reorder signal is valid but seasonality and valuation cap the holding window."}
{"row_type":"case","case_id":"R13L41_C18_NONGSHIM_004370_GLOBAL_MATURE","symbol":"004370","company_name":"농심","round":"R13","loop":"41","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_MATURE_GLOBAL_CAPACITY_WITHOUT_RERATING","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R13L41_C18_NONGSHIM_STAGE2_2023_08_11","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"global footprint was real but mature; upside was single-digit while 180D drawdown exceeded 20%","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Overseas sales and capacity are not sufficient when the channel signal is mature rather than accelerating reorder."}
{"row_type":"case","case_id":"R13L41_C18_FNF_383220_CHINA_CHANNEL_RISK","symbol":"383220","company_name":"F&F","round":"R13","loop":"41","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"APPAREL_CHINA_CHANNEL_INVENTORY_REORDER_RISK","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R13L41_C18_FNF_STAGE2_2023_08_01","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"brand/channel export story produced brief rallies but later price path punished inventory/channel concentration risk","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"The case is a counterexample to treating overseas brand presence as durable reorder evidence without sell-through and inventory confirmation."}
```

### 25.3 trigger rows
```jsonl
{"row_type":"trigger","trigger_id":"R13L41_C18_SAMYANG_STAGE2_2023_11_16","case_id":"R13L41_C18_SAMYANG_003230_EXPORT_REORDER","symbol":"003230","company_name":"삼양식품","round":"R13","loop":"41","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_BULDAK_GLOBAL_REORDER_MARGIN_BRIDGE","sector":"소비재·유통·브랜드","primary_archetype":"consumer_export_channel_reorder","loop_objective":"holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-11-15","evidence_available_at_that_date":"Q3/reorder/export mix became visible; next-trading-day entry used because public timing was not assumed intraday.","evidence_source":"public earnings/disclosure/news context plus stock-web price rows; no live scan used","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2023.csv","profile_path":"atlas/symbol_profiles/003/003230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-11-16","entry_price":197600,"MFE_30D_pct":18.17,"MFE_90D_pct":21.2,"MFE_180D_pct":263.36,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.15,"MAE_90D_pct":-14.17,"MAE_180D_pct":-14.17,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":718000,"drawdown_after_peak_pct":-34.56,"green_lateness_ratio":"0.00","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SAMYANG_2023_11_16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L41_C18_SAMYANG_GREEN_2024_05_17","case_id":"R13L41_C18_SAMYANG_003230_EXPORT_REORDER","symbol":"003230","company_name":"삼양식품","round":"R13","loop":"41","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_BULDAK_GLOBAL_REORDER_MARGIN_BRIDGE","sector":"소비재·유통·브랜드","primary_archetype":"consumer_export_channel_reorder","loop_objective":"holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage3-Green","trigger_date":"2024-05-16","evidence_available_at_that_date":"Confirmed earnings/revision and margin bridge; price already far above Stage2 entry.","evidence_source":"public earnings/disclosure/news context plus stock-web price rows; no live scan used","stage2_evidence_fields":["relative_strength","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv","profile_path":"atlas/symbol_profiles/003/003230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-17","entry_price":446500,"MFE_30D_pct":60.81,"MFE_90D_pct":60.81,"MFE_180D_pct":60.81,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":0.0,"MAE_90D_pct":0.0,"MAE_180D_pct":0.0,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-06-19","peak_price":718000,"drawdown_after_peak_pct":-34.56,"green_lateness_ratio":"0.52","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_green_but_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SAMYANG_2024_05_17","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L41_C18_SAMYANG_4B_2024_06_18","case_id":"R13L41_C18_SAMYANG_003230_EXPORT_REORDER","symbol":"003230","company_name":"삼양식품","round":"R13","loop":"41","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_BULDAK_GLOBAL_REORDER_MARGIN_BRIDGE","sector":"소비재·유통·브랜드","primary_archetype":"consumer_export_channel_reorder","loop_objective":"holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"4B","trigger_date":"2024-06-18","evidence_available_at_that_date":"Local blowoff and valuation/positioning stress after a vertical move; not a thesis break.","evidence_source":"public earnings/disclosure/news context plus stock-web price rows; no live scan used","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","margin_bridge"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv","profile_path":"atlas/symbol_profiles/003/003230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-18","entry_price":712000,"MFE_30D_pct":0.84,"MFE_90D_pct":0.84,"MFE_180D_pct":0.84,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-18.4,"MAE_90D_pct":-36.03,"MAE_180D_pct":-36.03,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":718000,"drawdown_after_peak_pct":-34.56,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.99,"four_b_full_window_peak_proximity":0.52,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_local_peak_but_full_cycle_too_early","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SAMYANG_2024_06_18","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L41_C18_BINGGRAE_STAGE2_2024_05_16","case_id":"R13L41_C18_BINGGRAE_005180_EXPORT_REORDER","symbol":"005180","company_name":"빙그레","round":"R13","loop":"41","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_ICECREAM_GLOBAL_REORDER_SEASONAL_EXPORT","sector":"소비재·유통·브랜드","primary_archetype":"consumer_export_channel_reorder","loop_objective":"holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-16","evidence_available_at_that_date":"Export/reorder and seasonal margin route became tradable; same-day entry because price reacted during market session.","evidence_source":"public earnings/disclosure/news context plus stock-web price rows; no live scan used","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv","profile_path":"atlas/symbol_profiles/005/005180.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-16","entry_price":75600,"MFE_30D_pct":56.61,"MFE_90D_pct":56.61,"MFE_180D_pct":56.61,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.56,"MAE_90D_pct":-21.69,"MAE_180D_pct":-21.69,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-11","peak_price":118400,"drawdown_after_peak_pct":-50.0,"green_lateness_ratio":"0.00","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"high_mfe_success_with_high_mae_after_peak","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"BINGGRAE_2024_05_16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L41_C18_BINGGRAE_4B_2024_06_10","case_id":"R13L41_C18_BINGGRAE_005180_EXPORT_REORDER","symbol":"005180","company_name":"빙그레","round":"R13","loop":"41","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_ICECREAM_GLOBAL_REORDER_SEASONAL_EXPORT","sector":"소비재·유통·브랜드","primary_archetype":"consumer_export_channel_reorder","loop_objective":"holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"4B","trigger_date":"2024-06-10","evidence_available_at_that_date":"Vertical repricing after export-seasonality narrative; non-price 4B supported by stretched valuation and seasonal/positioning cap.","evidence_source":"public earnings/disclosure/news context plus stock-web price rows; no live scan used","stage2_evidence_fields":[],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv","profile_path":"atlas/symbol_profiles/005/005180.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-10","entry_price":112100,"MFE_30D_pct":5.62,"MFE_90D_pct":5.62,"MFE_180D_pct":5.62,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-20.52,"MAE_90D_pct":-47.19,"MAE_180D_pct":-47.19,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-11","peak_price":118400,"drawdown_after_peak_pct":-50.0,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":0.96,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"BINGGRAE_2024_06_10","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L41_C18_NONGSHIM_STAGE2_2023_08_11","case_id":"R13L41_C18_NONGSHIM_004370_GLOBAL_MATURE","symbol":"004370","company_name":"농심","round":"R13","loop":"41","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_MATURE_GLOBAL_CAPACITY_WITHOUT_RERATING","sector":"소비재·유통·브랜드","primary_archetype":"consumer_export_channel_reorder","loop_objective":"holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-08-11","evidence_available_at_that_date":"US/global expansion and earnings existed, but the signal was mature overseas penetration rather than new accelerating reorder.","evidence_source":"public earnings/disclosure/news context plus stock-web price rows; no live scan used","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004370/2023.csv","profile_path":"atlas/symbol_profiles/004/004370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-08-11","entry_price":459000,"MFE_30D_pct":6.75,"MFE_90D_pct":8.93,"MFE_180D_pct":8.93,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.32,"MAE_90D_pct":-13.18,"MAE_180D_pct":-24.29,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-10-10","peak_price":500000,"drawdown_after_peak_pct":-30.5,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"NONGSHIM_2023_08_11","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L41_C18_NONGSHIM_4C_WATCH_2024_02_29","case_id":"R13L41_C18_NONGSHIM_004370_GLOBAL_MATURE","symbol":"004370","company_name":"농심","round":"R13","loop":"41","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_MATURE_GLOBAL_CAPACITY_WITHOUT_RERATING","sector":"소비재·유통·브랜드","primary_archetype":"consumer_export_channel_reorder","loop_objective":"holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"4C-watch","trigger_date":"2024-02-29","evidence_available_at_that_date":"Drawdown after failed rerating looked thesis-broken, but later recovery shows mature export names can mean-revert; hard 4C should need evidence break, not price alone.","evidence_source":"public earnings/disclosure/news context plus stock-web price rows; no live scan used","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv","profile_path":"atlas/symbol_profiles/004/004370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-29","entry_price":348000,"MFE_30D_pct":11.06,"MFE_90D_pct":57.76,"MFE_180D_pct":57.76,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-0.14,"MAE_90D_pct":-0.14,"MAE_180D_pct":-0.14,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-11","peak_price":549000,"drawdown_after_peak_pct":-18.03,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"false_break","trigger_outcome_label":"false_break_not_4C","current_profile_verdict":"current_profile_data_insufficient","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"NONGSHIM_2024_02_29","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L41_C18_FNF_STAGE2_2023_08_01","case_id":"R13L41_C18_FNF_383220_CHINA_CHANNEL_RISK","symbol":"383220","company_name":"F&F","round":"R13","loop":"41","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"APPAREL_CHINA_CHANNEL_INVENTORY_REORDER_RISK","sector":"소비재·유통·브랜드","primary_archetype":"consumer_export_channel_reorder","loop_objective":"holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-08-01","evidence_available_at_that_date":"Overseas brand/channel story existed, but sell-through and inventory proof were insufficient; price path exposed a false promotion risk.","evidence_source":"public earnings/disclosure/news context plus stock-web price rows; no live scan used","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/383/383220/2023.csv","profile_path":"atlas/symbol_profiles/383/383220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-08-01","entry_price":104000,"MFE_30D_pct":14.81,"MFE_90D_pct":15.38,"MFE_180D_pct":15.38,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.63,"MAE_90D_pct":-23.75,"MAE_180D_pct":-40.67,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-09-19","peak_price":120000,"drawdown_after_peak_pct":-48.58,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"FNF_2023_08_01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L41_C18_FNF_4C_2024_01_15","case_id":"R13L41_C18_FNF_383220_CHINA_CHANNEL_RISK","symbol":"383220","company_name":"F&F","round":"R13","loop":"41","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"APPAREL_CHINA_CHANNEL_INVENTORY_REORDER_RISK","sector":"소비재·유통·브랜드","primary_archetype":"consumer_export_channel_reorder","loop_objective":"holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"4C","trigger_date":"2024-01-15","evidence_available_at_that_date":"Channel/inventory risk moved from watch to thesis break; protection label is useful because subsequent MFE was only 1.31% while 180D MAE was -28.66%.","evidence_source":"public earnings/disclosure/news context plus stock-web price rows; no live scan used","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv","profile_path":"atlas/symbol_profiles/383/383220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-15","entry_price":76400,"MFE_30D_pct":1.31,"MFE_90D_pct":1.31,"MFE_180D_pct":1.31,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-13.09,"MAE_90D_pct":-19.24,"MAE_180D_pct":-28.66,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-01","peak_price":77400,"drawdown_after_peak_pct":-29.59,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"FNF_2024_01_15","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows
```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L41_C18_SAMYANG_003230_EXPORT_REORDER","trigger_id":"R13L41_C18_SAMYANG_STAGE2_2023_11_16","symbol":"003230","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":10,"relative_strength_score":10,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":11,"revision_score":12,"relative_strength_score":11,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84.0,"stage_label_after":"Stage3-Yellow+Actionable","changed_components":["customer_quality_score","revision_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C18 shadow profile rewards repeat reorder/sell-through and penalizes mature or concentrated channel risk; scores are research proxy only.","MFE_90D_pct":21.2,"MAE_90D_pct":-14.17,"score_return_alignment_label":"structural_success","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L41_C18_SAMYANG_003230_EXPORT_REORDER","trigger_id":"R13L41_C18_SAMYANG_GREEN_2024_05_17","symbol":"003230","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":17,"revision_score":18,"relative_strength_score":16,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":90.0,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":18,"revision_score":19,"relative_strength_score":16,"customer_quality_score":17,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":92.0,"stage_label_after":"Stage3-Green","changed_components":["customer_quality_score","revision_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C18 shadow profile rewards repeat reorder/sell-through and penalizes mature or concentrated channel risk; scores are research proxy only.","MFE_90D_pct":60.81,"MAE_90D_pct":0.0,"score_return_alignment_label":"late_green_but_success","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L41_C18_SAMYANG_003230_EXPORT_REORDER","trigger_id":"R13L41_C18_SAMYANG_4B_2024_06_18","symbol":"003230","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":18,"revision_score":19,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":20,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":88.0,"stage_label_before":"4B-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":18,"revision_score":19,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":20,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":86.0,"stage_label_after":"4B-local-only","changed_components":["customer_quality_score","revision_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C18 shadow profile rewards repeat reorder/sell-through and penalizes mature or concentrated channel risk; scores are research proxy only.","MFE_90D_pct":0.84,"MAE_90D_pct":-36.03,"score_return_alignment_label":"4B_local_peak_but_full_cycle_too_early","current_profile_verdict":"current_profile_4B_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L41_C18_BINGGRAE_005180_EXPORT_REORDER","trigger_id":"R13L41_C18_BINGGRAE_STAGE2_2024_05_16","symbol":"005180","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":9,"revision_score":10,"relative_strength_score":13,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":77.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":11,"relative_strength_score":14,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":82.0,"stage_label_after":"Stage2-Actionable/Yellow","changed_components":["customer_quality_score","revision_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C18 shadow profile rewards repeat reorder/sell-through and penalizes mature or concentrated channel risk; scores are research proxy only.","MFE_90D_pct":56.61,"MAE_90D_pct":-21.69,"score_return_alignment_label":"high_mfe_success_with_high_mae_after_peak","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L41_C18_BINGGRAE_005180_EXPORT_REORDER","trigger_id":"R13L41_C18_BINGGRAE_4B_2024_06_10","symbol":"005180","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":18,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":18,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":83.0,"stage_label_before":"Stage3-Yellow/4B-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":18,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":20,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":80.0,"stage_label_after":"4B-full-window","changed_components":["customer_quality_score","revision_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C18 shadow profile rewards repeat reorder/sell-through and penalizes mature or concentrated channel risk; scores are research proxy only.","MFE_90D_pct":5.62,"MAE_90D_pct":-47.19,"score_return_alignment_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L41_C18_NONGSHIM_004370_GLOBAL_MATURE","trigger_id":"R13L41_C18_NONGSHIM_STAGE2_2023_08_11","symbol":"004370","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":6,"customer_quality_score":9,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72.0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":7,"relative_strength_score":5,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":66.0,"stage_label_after":"Stage2-capped","changed_components":["customer_quality_score","revision_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C18 shadow profile rewards repeat reorder/sell-through and penalizes mature or concentrated channel risk; scores are research proxy only.","MFE_90D_pct":8.93,"MAE_90D_pct":-13.18,"score_return_alignment_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L41_C18_NONGSHIM_004370_GLOBAL_MATURE","trigger_id":"R13L41_C18_NONGSHIM_4C_WATCH_2024_02_29","symbol":"004370","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":58.0,"stage_label_before":"4C-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":62.0,"stage_label_after":"false-break-watch","changed_components":["customer_quality_score","revision_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C18 shadow profile rewards repeat reorder/sell-through and penalizes mature or concentrated channel risk; scores are research proxy only.","MFE_90D_pct":57.76,"MAE_90D_pct":-0.14,"score_return_alignment_label":"false_break_not_4C","current_profile_verdict":"current_profile_data_insufficient"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L41_C18_FNF_383220_CHINA_CHANNEL_RISK","trigger_id":"R13L41_C18_FNF_STAGE2_2023_08_01","symbol":"383220","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":7,"relative_strength_score":9,"customer_quality_score":11,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":5,"relative_strength_score":7,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":64.0,"stage_label_after":"Stage2-capped","changed_components":["customer_quality_score","revision_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C18 shadow profile rewards repeat reorder/sell-through and penalizes mature or concentrated channel risk; scores are research proxy only.","MFE_90D_pct":15.38,"MAE_90D_pct":-23.75,"score_return_alignment_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L41_C18_FNF_383220_CHINA_CHANNEL_RISK","trigger_id":"R13L41_C18_FNF_4C_2024_01_15","symbol":"383220","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":12,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":61.0,"stage_label_before":"4B/4C-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":15,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":55.0,"stage_label_after":"4C-route","changed_components":["customer_quality_score","revision_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C18 shadow profile rewards repeat reorder/sell-through and penalizes mature or concentrated channel risk; scores are research proxy only.","MFE_90D_pct":1.31,"MAE_90D_pct":-19.24,"score_return_alignment_label":"4C_success","current_profile_verdict":"current_profile_4C_too_late"}
```

### 25.5 shadow_weight rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C18_repeat_reorder_sell_through_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,+2,+2,"Repeat reorder plus sell-through separates Samyang/Binggrae from mature or concentrated channels","raises positive Stage2/Yellow while preserving non-price evidence gate","R13L41_C18_SAMYANG_STAGE2_2023_11_16|R13L41_C18_BINGGRAE_STAGE2_2024_05_16",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C18_mature_overseas_presence_cap,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,-2,-2,"Global footprint without acceleration failed on Nongshim-like mature export narratives","reduces false positive green/yellow promotion","R13L41_C18_NONGSHIM_STAGE2_2023_08_11",4,4,2,medium,counterexample_guard,"not production; post-calibrated residual"
shadow_weight,C18_single_channel_inventory_risk_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,-3,-3,"China/apparel channel concentration and inventory risk broke F&F-style export stories","blocks false positive promotion and improves 4C routing","R13L41_C18_FNF_STAGE2_2023_08_01|R13L41_C18_FNF_4C_2024_01_15",4,4,2,medium,counterexample_guard,"not production; post-calibrated residual"
shadow_weight,L5_seasonal_consumer_export_4B_overlay,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,+1,+1,"Seasonal food export reratings can peak before confirmed long-cycle revision fades","improves Binggrae 4B timing without weakening Samyang structural case","R13L41_C18_BINGGRAE_4B_2024_06_10",4,4,2,low,sector_shadow_only,"not production; post-calibrated residual"
```

### 25.6 residual_contribution row
```jsonl
{"row_type":"residual_contribution","round":"R13","loop":"41","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["mature_export_false_positive","seasonal_export_4B_too_late","green_confirmation_late_for_fast_reorder","single_channel_inventory_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows
```jsonl
# none; all selected rows have stock-web 180D forward windows and clean 180D corporate-action status
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

next_round: R13_loop_42 — L5_CONSUMER_BRAND_DISTRIBUTION / C19_BRAND_RETAIL_INVENTORY_MARGIN. Suggested focus: retail inventory/margin counterexamples, not export-channel reorder.

## 28. Source Notes


- Stock-Web manifest checked: `atlas/manifest.json`; max_date `2026-02-20`, raw/unadjusted marcap, tradable shard root `atlas/ohlcv_tradable_by_symbol_year`.
- Stock-Web schema checked: `atlas/schema.json`; MFE/MAE formulas and clean tradable row rules followed.
- Symbol profiles checked: `003230`, `005180`, `004370`, `383220`; no corporate-action candidate dates overlap selected 180D windows.
- OHLC rows checked from the relevant 2023/2024 tradable shards for each case.
- Evidence is historical and used only to label trigger families; no live candidate discovery, current recommendation, or production patch was performed.

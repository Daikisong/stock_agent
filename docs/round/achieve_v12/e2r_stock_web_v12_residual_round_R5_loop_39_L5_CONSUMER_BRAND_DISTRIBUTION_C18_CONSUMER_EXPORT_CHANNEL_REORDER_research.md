# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R5
loop = 39
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = K_FOOD_GLOBAL_REORDER_BULDAK_EXPORT_CAPACITY | K_FOOD_ICECREAM_US_EXPORT_SEASONAL_REORDER | CHINA_BRAND_REOPENING_RESTOCK_WITHOUT_REVISION
loop_objective = coverage_gap_fill; counterexample_mining; residual_false_positive_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
```

## 1. Current Calibrated Profile Assumption

This MD treats `e2r_2_1_stock_web_calibrated_proxy` as the active current profile and uses `e2r_2_0_baseline_reference` only as a rollback comparison. The already-applied axes are not re-proposed globally. This loop tests whether C18 needs a canonical-archetype guard that distinguishes real export reorder conversion from brand/reopening restock narratives.

Existing calibrated axes tested: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, stage3_cross_evidence_green_buffer, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| round | R5 |
| large_sector_id | L5_CONSUMER_BRAND_DISTRIBUTION |
| canonical_archetype_id | C18_CONSUMER_EXPORT_CHANNEL_REORDER |
| target question | When does consumer export/channel evidence deserve Stage2-Actionable promotion, and when should it be capped because reorder durability/margin revision is not proven? |
| non-validation scope | live candidate discovery, stock recommendation, production patch, auto-trading |

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research-artifact access was limited to calibration reports/registries. A repository search for `C18_CONSUMER_EXPORT_CHANNEL_REORDER` returned no direct hit in the accessible research artifact index during this loop. The calibration ingest summary still showed broad R1-R13 coverage and 1,376 aggregate representative trigger rows, so this loop deliberately avoids R1/R2 representative sets and fills an R5/C18 consumer-export gap.

Novelty decision: all three representative cases are new independent symbols within C18 for this loop. No case is reused from the immediately preceding C20 MD.

## 4. Stock-Web OHLC Input / Price Source Validation

| Manifest field | Value |
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
| markets | ['KONEX', 'KOSDAQ', 'KOSDAQ GLOBAL', 'KOSPI'] |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Stock-Web schema basis: tradable shards use `d,o,h,l,c,v,a,mc,s,m`; raw shards add `rs`. Calibration uses `tradable_raw`; raw/unadjusted OHLC is not split-adjusted. Corporate-action candidate windows are blocked by default.

## 5. Historical Eligibility Gate

| case_id | entry_date | 180D forward window | corporate action window | calibration_usable | reason |
|---|---:|---:|---|---:|---|
| R5L39_C18_003230_SYF_EXPORT_REORDER | 2024-05-17 | available through stock-web max_date 2026-02-20 | clean_180D_window; only profile corporate action candidate is 2003-07-25 | true | clean 180D tradable window |
| R5L39_C18_005180_BINGGRAE_EXPORT_REORDER | 2024-05-17 | available through stock-web max_date 2026-02-20 | clean_180D_window; corporate action candidates are pre-1999 only | true | clean 180D tradable window |
| R5L39_C18_383220_FNF_CHINA_REOPENING_FALSE_REORDER | 2024-05-03 | available through stock-web max_date 2026-02-20 | clean_180D_window; only profile corporate action candidate is 2022-04-13 | true | clean 180D tradable window |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | Compression note |
|---|---|---|
| K_FOOD_GLOBAL_REORDER_BULDAK_EXPORT_CAPACITY | C18_CONSUMER_EXPORT_CHANNEL_REORDER | Export reorder became margin/revision evidence, not just popularity narrative. |
| K_FOOD_ICECREAM_US_EXPORT_SEASONAL_REORDER | C18_CONSUMER_EXPORT_CHANNEL_REORDER | Export/seasonal channel evidence can work, but durability must be capped unless repeat reorder is confirmed. |
| CHINA_BRAND_REOPENING_RESTOCK_WITHOUT_REVISION | C18_CONSUMER_EXPORT_CHANNEL_REORDER | Reopening/restock narrative without margin/revision is a C18 counterexample, not a Green route. |

## 7. Case Selection Summary

| case_id | symbol | company | role | best_trigger | 90D MFE | 90D MAE | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---|
| R5L39_C18_003230_SYF_EXPORT_REORDER | 003230 | 삼양식품 | structural_success / positive | R5L39_C18_003230_STAGE2A_20240517 | 60.81% | 0.00% | current_profile_correct |
| R5L39_C18_005180_BINGGRAE_EXPORT_REORDER | 005180 | 빙그레 | high_mae_success / positive | R5L39_C18_005180_STAGE2A_20240517 | 34.09% | -32.96% | current_profile_correct |
| R5L39_C18_383220_FNF_CHINA_REOPENING_FALSE_REORDER | 383220 | F&F | failed_rerating / counterexample | R5L39_C18_383220_STAGE2_FALSE_20240503 | 4.95% | -35.23% | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

Positive structural/high-MAE successes: 2. Counterexamples: 1. Calibration-usable representative cases: 3. The set meets the v12 minimum balance, but confidence remains medium-low because it is one canonical archetype and one large sector.

## 9. Evidence Source Map

This loop separates price evidence from non-price evidence. Price action is never used by itself to create Stage2/Stage3 evidence.

| case | trigger evidence available at date | evidence families | source handling |
|---|---|---|---|
| 삼양식품 | Q1/Q2 export-led earnings surprise; Buldak global reorder; capacity/ASP/margin bridge became visible before full Green confirmation. | public_event_or_disclosure; customer_or_order_quality; capacity_or_volume_route; early_revision_signal; margin_bridge | public earnings/analyst notes; stock-web only for OHLC. |
| 빙그레 | Export/ice-cream seasonal reorder and strong Q1 price response; later drawdown shows seasonality and repeat-order durability must be checked before Green. | public_event_or_disclosure; customer_or_order_quality; relative_strength; early_revision_signal | public earnings/industry export narrative; stock-web only for OHLC. |
| F&F | China/brand reopening restock narrative had relative strength but did not close through durable margin/revision evidence. | public_event_or_disclosure; customer_or_order_quality; relative_strength; thesis_evidence_broken | public earnings/retail narrative; stock-web only for OHLC. |

## 10. Price Data Source Map

| symbol | profile_path | price_shard_path | profile caveat |
|---:|---|---|---|
| 003230 | atlas/symbol_profiles/003/003230.json | atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv|atlas/ohlcv_tradable_by_symbol_year/003/003230/2025.csv | clean_180D_window; only profile corporate action candidate is 2003-07-25 |
| 005180 | atlas/symbol_profiles/005/005180.json | atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv|atlas/ohlcv_tradable_by_symbol_year/005/005180/2025.csv | clean_180D_window; corporate action candidates are pre-1999 only |
| 383220 | atlas/symbol_profiles/383/383220.json | atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv|atlas/ohlcv_tradable_by_symbol_year/383/383220/2025.csv | clean_180D_window; only profile corporate action candidate is 2022-04-13 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | stage2_fields | stage3_fields | 4B_fields | 4C_fields | dedupe | role |
|---|---:|---|---:|---:|---:|---|---|---|---|---:|---|
| R5L39_C18_003230_STAGE2A_20240517 | 003230 | Stage2-Actionable | 2024-05-16 | 2024-05-17 | 446500 | public_event_or_disclosure, customer_or_order_quality, relative_strength, capacity_or_volume_route, early_revision_signal | confirmed_revision, margin_bridge, financial_visibility, multiple_public_sources |  |  | true | representative |
| R5L39_C18_003230_STAGE3G_20240614 | 003230 | Stage3-Green | 2024-06-14 | 2024-06-14 | 647000 | public_event_or_disclosure, relative_strength | confirmed_revision, margin_bridge, financial_visibility, multiple_public_sources |  |  | false | label_comparison_only |
| R5L39_C18_003230_4BLOCAL_20240619 | 003230 | 4B-overlay | 2024-06-19 | 2024-06-19 | 673000 |  | confirmed_revision | price_only_local_peak, valuation_blowoff, positioning_overheat |  | false | 4B_overlay_only |
| R5L39_C18_005180_STAGE2A_20240517 | 005180 | Stage2-Actionable | 2024-05-16 | 2024-05-17 | 88300 | public_event_or_disclosure, customer_or_order_quality, relative_strength, early_revision_signal | margin_bridge, financial_visibility |  |  | true | representative |
| R5L39_C18_005180_4B_20240611 | 005180 | 4B-overlay | 2024-06-11 | 2024-06-11 | 109000 |  | financial_visibility | valuation_blowoff, positioning_overheat, margin_or_backlog_slowdown |  | false | 4B_overlay_only |
| R5L39_C18_383220_STAGE2_FALSE_20240503 | 383220 | Stage2-Actionable-candidate | 2024-05-02 | 2024-05-03 | 72800 | public_event_or_disclosure, customer_or_order_quality, relative_strength |  |  | thesis_evidence_broken | true | representative |
| R5L39_C18_383220_4CWATCH_20240805 | 383220 | 4C-watch | 2024-08-05 | 2024-08-05 | 48000 |  |  | margin_or_backlog_slowdown | thesis_evidence_broken | false | 4C_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak | below_entry_90D |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| R5L39_C18_003230_STAGE2A_20240517 | 446500 | 60.81% | 0.00% | 60.81% | 0.00% | 87.46% | 0.00% | 2025-02-12 | 837000 | -4.78% | false |
| R5L39_C18_003230_STAGE3G_20240614 | 647000 | 10.97% | -8.66% | 11.00% | -29.60% | 29.37% | -29.60% | 2025-02-12 | 837000 | -4.78% | true |
| R5L39_C18_003230_4BLOCAL_20240619 | 673000 | 6.69% | -13.67% | 6.69% | -32.32% | 24.37% | -32.32% | 2025-02-12 | 837000 | -4.78% | true |
| R5L39_C18_005180_STAGE2A_20240517 | 88300 | 34.09% | -9.29% | 34.09% | -32.96% | 34.09% | -32.96% | 2024-06-11 | 118400 | -50.00% | true |
| R5L39_C18_005180_4B_20240611 | 109000 | 8.62% | -18.72% | 8.62% | -45.69% | 8.62% | -45.69% | 2024-06-11 | 118400 | -50.00% | true |
| R5L39_C18_383220_STAGE2_FALSE_20240503 | 72800 | 0.96% | -13.05% | 4.95% | -35.23% | 4.95% | -35.23% | 2024-07-17 | 76400 | -38.29% | true |
| R5L39_C18_383220_4CWATCH_20240805 | 48000 | 22.50% | -1.77% | 50.21% | -1.77% | 55.83% | -1.77% | 2025-02-20 | 74800 | -38.29% | true |

## 13. Current Calibrated Profile Stress Test

1. The current profile correctly promotes 삼양식품 and 빙그레 as Stage2-Actionable because both had non-price evidence. 2. It is too permissive if F&F-style China/brand reopening evidence is allowed to become Stage3-Green without revision/margin closure. 3. The Stage2 bonus is not globally too high; it is too high only for C18 cases where reorder is inferred from brand heat instead of confirmed sell-through/revision. 4. Yellow threshold 75 remains useful for 삼양식품; F&F should remain below Yellow. 5. Green threshold 87/revision 55 should be kept; C18 should add a specific `repeat_reorder_or_margin_bridge` Green gate. 6. Price-only blowoff guard is strengthened by 삼양식품 local peak and Binggrae reversal. 7. Full 4B non-price requirement is kept. 8. Hard 4C routing is kept, but 4C must not transform a late rebound into positive training.

Current profile error count: 1 representative case, F&F false-positive promotion risk.

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Stage3/Green comparison | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| 삼양식품 | 446,500 on 2024-05-17 | 647,000 on 2024-06-14 | 0.513 | Green captured the move but gave up roughly half of measured 180D upside from the first actionable trigger. |
| 빙그레 | 88,300 on 2024-05-17 | no durable confirmed Green row | n/a | Strong Stage2 but Green should wait for repeat-order durability due to -32.96% 90D MAE. |
| F&F | 72,800 candidate on 2024-05-03 | no confirmed Green row | n/a | Current profile must block brand/reopening narrative from Green without revision and margin evidence. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---|---:|---:|---|
| R5L39_C18_003230_4BLOCAL_20240619 | 0.834 | 0.580 | price_only_local_4B_too_early; local peak proximity was high but full-window upside remained. |
| R5L39_C18_005180_4B_20240611 | 0.688 | 0.688 | good local 4B overlay; not positive-entry training. |
| R5L39_C18_383220_STAGE2_FALSE_20240503 | n/a | n/a | Failed rerating; 4B/4C should act as thesis-break guard, not promotion. |

## 16. 4C Protection Audit

F&F shows that late 4C labels can become false breaks if applied after the bulk of drawdown. The useful C18 guard is earlier: block Stage3-Green when export/channel restock has no repeat reorder, margin bridge, or revision evidence. 4C row is therefore `thesis_break_watch_only`, not a positive or negative weight source.

## 17. Sector-Specific Rule Candidate

`c18_consumer_export_reorder_durability_gate`: within L5, Stage2-Actionable can be promoted on export/channel evidence, but Stage3-Green requires at least two of: confirmed revision, repeat reorder or channel sell-through, margin bridge, durable customer/channel confirmation. Reopening/restock narratives without these remain capped at Watch/Stage2.

## 18. Canonical-Archetype Rule Candidate

`C18_repeat_reorder_margin_bridge_bonus`: +1 to +2 shadow-only bonus when export/channel reorder is paired with margin bridge and early revision; `C18_brand_reopening_without_revision_cap`: cap Green when the evidence is brand heat or China reopening restock without revision/margin bridge.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_triggers | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | false_positive_rate | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current global | 3 | 33.28% | -22.73% | 42.16% | 33.3% | useful but vulnerable to F&F-style false reorder. |
| P0b e2r_2_0_baseline_reference | rollback reference | 3 | 33.28% | -22.73% | 42.16% | 33.3% | less explicit guard; same false-positive risk. |
| P1 sector_specific_candidate_profile | L5 | 2 selected, 1 blocked | 47.45% | -16.48% | 60.77% | 0.0% | better alignment after blocking brand-reopening false positive. |
| P2 canonical_archetype_candidate_profile | C18 | 2 selected, 1 blocked | 47.45% | -16.48% | 60.77% | 0.0% | best explanatory profile for C18. |
| P3 counterexample_guard_profile | C18 guard | 2 selected, 1 blocked | 47.45% | -16.48% | 60.77% | 0.0% | same return filter with stronger false-Green cap. |

## 20. Score-Return Alignment Matrix

| trigger_id | weighted_score_before | stage_before | weighted_score_after | stage_after | 90D return alignment |
|---|---:|---|---:|---|---|
| R5L39_C18_003230_STAGE2A_20240517 | 78 | Stage3-Yellow | 84 | Stage3-Yellow-high | MFE 60.81% / MAE 0.00% / current_profile_correct |
| R5L39_C18_005180_STAGE2A_20240517 | 74 | Stage2-Actionable | 74 | Stage2-Actionable | MFE 34.09% / MAE -32.96% / current_profile_correct |
| R5L39_C18_383220_STAGE2_FALSE_20240503 | 68 | Stage2-Watch | 55 | Watch-Guarded | MFE 4.95% / MAE -35.23% / current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C18_CONSUMER_EXPORT_CHANNEL_REORDER | mixed C18 export/channel fine types | 2 | 1 | 2 | 1 | 3 | 0 | 7 | 3 | 1 | true | true | More C18 counterexamples needed in non-food branded goods and distributor/channel cases. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, stage3_cross_evidence_green_buffer, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [brand_reopening_restock_false_positive, high_mae_export_success, price_only_local_4B_too_early]
new_axis_proposed: C18_repeat_reorder_margin_bridge_bonus; C18_brand_reopening_without_revision_cap
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: none
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated: historical OHLC from stock-web tradable shards; 30D/90D/180D MFE/MAE; corporate-action window status; representative trigger dedupe; current-profile stress test. Not validated: live candidates, broker execution, production score code, post-2026-02-20 OHLC, intraday timestamp precision, exact analyst consensus ledger.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C18_repeat_reorder_margin_bridge_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,export/channel reorder works when paired with margin bridge and revision,blocked F&F false positive while preserving 삼양식품/빙그레 Stage2,R5L39_C18_003230_STAGE2A_20240517|R5L39_C18_005180_STAGE2A_20240517|R5L39_C18_383220_STAGE2_FALSE_20240503,3,3,1,medium_low,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,C18_brand_reopening_without_revision_cap,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,brand heat or China reopening restock should not become Green without revision/margin bridge,false-positive rate falls from 33.3% to 0% in this small holdout,R5L39_C18_383220_STAGE2_FALSE_20240503,3,3,1,medium_low,counterexample_guard,not production; needs more C18 holdout
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation
```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows
```jsonl
{"row_type": "case", "case_id": "R5L39_C18_003230_SYF_EXPORT_REORDER", "symbol": "003230", "company_name": "삼양식품", "round": "R5", "loop": "39", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_GLOBAL_REORDER_BULDAK_EXPORT_CAPACITY", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R5L39_C18_003230_STAGE2A_20240517", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "current_profile_correct", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Q1/Q2 export-led earnings and Buldak global channel reorder closed through margin/revision; Green confirmation was still meaningfully later than first actionable evidence."}
{"row_type": "case", "case_id": "R5L39_C18_005180_BINGGRAE_EXPORT_REORDER", "symbol": "005180", "company_name": "빙그레", "round": "R5", "loop": "39", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_ICECREAM_US_EXPORT_SEASONAL_REORDER", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "R5L39_C18_005180_STAGE2A_20240517", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "current_profile_correct", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Export and seasonal ice-cream channel evidence was sufficient for Stage2-Actionable, but 90D/180D MAE says this archetype needs a seasonal/reorder durability cap before Green."}
{"row_type": "case", "case_id": "R5L39_C18_383220_FNF_CHINA_REOPENING_FALSE_REORDER", "symbol": "383220", "company_name": "F&F", "round": "R5", "loop": "39", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "CHINA_BRAND_REOPENING_RESTOCK_WITHOUT_REVISION", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R5L39_C18_383220_STAGE2_FALSE_20240503", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "current_profile_false_positive", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Brand/channel reopening narrative could look like a reorder thesis, but margin/revision/customer-channel durability did not close; current profile should cap this below Stage3-Green."}
```

### 25.3 trigger rows
```jsonl
{"row_type": "trigger", "trigger_id": "R5L39_C18_003230_STAGE2A_20240517", "case_id": "R5L39_C18_003230_SYF_EXPORT_REORDER", "symbol": "003230", "company_name": "삼양식품", "round": "R5", "loop": "39", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_GLOBAL_REORDER_BULDAK_EXPORT_CAPACITY", "sector": "소비재·유통·브랜드", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-16", "evidence_available_at_that_date": "non-price historical evidence separated by stage fields; no price-only promotion", "evidence_source": "public earnings/disclosure and analyst/narrative evidence; stock-web only for OHLC", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv|atlas/ohlcv_tradable_by_symbol_year/003/003230/2025.csv", "profile_path": "atlas/symbol_profiles/003/003230.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-17", "entry_price": 446500, "MFE_30D_pct": 60.81, "MFE_90D_pct": 60.81, "MFE_180D_pct": 87.46, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": 0.0, "MAE_1Y_pct": null, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2025-02-12", "peak_price": 837000, "drawdown_after_peak_pct": -4.78, "green_lateness_ratio": "not_applicable_to_stage2_row", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L39_C18_003230_20240517_446500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L39_C18_003230_STAGE3G_20240614", "case_id": "R5L39_C18_003230_SYF_EXPORT_REORDER", "symbol": "003230", "company_name": "삼양식품", "round": "R5", "loop": "39", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_GLOBAL_REORDER_BULDAK_EXPORT_CAPACITY", "sector": "소비재·유통·브랜드", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery", "trigger_type": "Stage3-Green", "trigger_date": "2024-06-14", "evidence_available_at_that_date": "non-price historical evidence separated by stage fields; no price-only promotion", "evidence_source": "public earnings/disclosure and analyst/narrative evidence; stock-web only for OHLC", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv|atlas/ohlcv_tradable_by_symbol_year/003/003230/2025.csv", "profile_path": "atlas/symbol_profiles/003/003230.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-14", "entry_price": 647000, "MFE_30D_pct": 10.97, "MFE_90D_pct": 11.0, "MFE_180D_pct": 29.37, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.66, "MAE_90D_pct": -29.6, "MAE_180D_pct": -29.6, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-12", "peak_price": 837000, "drawdown_after_peak_pct": -4.78, "green_lateness_ratio": 0.513, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_green_comparison", "current_profile_verdict": "current_profile_correct_but_green_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L39_C18_003230_20240614_647000", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": "label_or_overlay_comparison_same_loop", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R5L39_C18_003230_4BLOCAL_20240619", "case_id": "R5L39_C18_003230_SYF_EXPORT_REORDER", "symbol": "003230", "company_name": "삼양식품", "round": "R5", "loop": "39", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_GLOBAL_REORDER_BULDAK_EXPORT_CAPACITY", "sector": "소비재·유통·브랜드", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery", "trigger_type": "4B-overlay", "trigger_date": "2024-06-19", "evidence_available_at_that_date": "non-price historical evidence separated by stage fields; no price-only promotion", "evidence_source": "public earnings/disclosure and analyst/narrative evidence; stock-web only for OHLC", "stage2_evidence_fields": [], "stage3_evidence_fields": ["confirmed_revision"], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv|atlas/ohlcv_tradable_by_symbol_year/003/003230/2025.csv", "profile_path": "atlas/symbol_profiles/003/003230.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-19", "entry_price": 673000, "MFE_30D_pct": 6.69, "MFE_90D_pct": 6.69, "MFE_180D_pct": 24.37, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -13.67, "MAE_90D_pct": -32.32, "MAE_180D_pct": -32.32, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-12", "peak_price": 837000, "drawdown_after_peak_pct": -4.78, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.834, "four_b_full_window_peak_proximity": 0.58, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_too_early", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L39_C18_003230_20240619_673000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "label_or_overlay_comparison_same_loop", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R5L39_C18_005180_STAGE2A_20240517", "case_id": "R5L39_C18_005180_BINGGRAE_EXPORT_REORDER", "symbol": "005180", "company_name": "빙그레", "round": "R5", "loop": "39", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_ICECREAM_US_EXPORT_SEASONAL_REORDER", "sector": "소비재·유통·브랜드", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-16", "evidence_available_at_that_date": "non-price historical evidence separated by stage fields; no price-only promotion", "evidence_source": "public earnings/disclosure and analyst/narrative evidence; stock-web only for OHLC", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv|atlas/ohlcv_tradable_by_symbol_year/005/005180/2025.csv", "profile_path": "atlas/symbol_profiles/005/005180.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-17", "entry_price": 88300, "MFE_30D_pct": 34.09, "MFE_90D_pct": 34.09, "MFE_180D_pct": 34.09, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.29, "MAE_90D_pct": -32.96, "MAE_180D_pct": -32.96, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-11", "peak_price": 118400, "drawdown_after_peak_pct": -50.0, "green_lateness_ratio": "not_applicable_to_stage2_row", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "high_mae_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L39_C18_005180_20240517_88300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L39_C18_005180_4B_20240611", "case_id": "R5L39_C18_005180_BINGGRAE_EXPORT_REORDER", "symbol": "005180", "company_name": "빙그레", "round": "R5", "loop": "39", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_ICECREAM_US_EXPORT_SEASONAL_REORDER", "sector": "소비재·유통·브랜드", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery", "trigger_type": "4B-overlay", "trigger_date": "2024-06-11", "evidence_available_at_that_date": "non-price historical evidence separated by stage fields; no price-only promotion", "evidence_source": "public earnings/disclosure and analyst/narrative evidence; stock-web only for OHLC", "stage2_evidence_fields": [], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv|atlas/ohlcv_tradable_by_symbol_year/005/005180/2025.csv", "profile_path": "atlas/symbol_profiles/005/005180.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-11", "entry_price": 109000, "MFE_30D_pct": 8.62, "MFE_90D_pct": 8.62, "MFE_180D_pct": 8.62, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -18.72, "MAE_90D_pct": -45.69, "MAE_180D_pct": -45.69, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-11", "peak_price": 118400, "drawdown_after_peak_pct": -50.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.688, "four_b_full_window_peak_proximity": 0.688, "four_b_timing_verdict": "good_local_4B_timing_but_not_positive_training", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L39_C18_005180_20240611_109000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "label_or_overlay_comparison_same_loop", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R5L39_C18_383220_STAGE2_FALSE_20240503", "case_id": "R5L39_C18_383220_FNF_CHINA_REOPENING_FALSE_REORDER", "symbol": "383220", "company_name": "F&F", "round": "R5", "loop": "39", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "CHINA_BRAND_REOPENING_RESTOCK_WITHOUT_REVISION", "sector": "소비재·유통·브랜드", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable-candidate", "trigger_date": "2024-05-02", "evidence_available_at_that_date": "non-price historical evidence separated by stage fields; no price-only promotion", "evidence_source": "public earnings/disclosure and analyst/narrative evidence; stock-web only for OHLC", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv|atlas/ohlcv_tradable_by_symbol_year/383/383220/2025.csv", "profile_path": "atlas/symbol_profiles/383/383220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-03", "entry_price": 72800, "MFE_30D_pct": 0.96, "MFE_90D_pct": 4.95, "MFE_180D_pct": 4.95, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -13.05, "MAE_90D_pct": -35.23, "MAE_180D_pct": -35.23, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-17", "peak_price": 76400, "drawdown_after_peak_pct": -38.29, "green_lateness_ratio": "no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L39_C18_383220_20240503_72800", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R5L39_C18_383220_4CWATCH_20240805", "case_id": "R5L39_C18_383220_FNF_CHINA_REOPENING_FALSE_REORDER", "symbol": "383220", "company_name": "F&F", "round": "R5", "loop": "39", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "CHINA_BRAND_REOPENING_RESTOCK_WITHOUT_REVISION", "sector": "소비재·유통·브랜드", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery", "trigger_type": "4C-watch", "trigger_date": "2024-08-05", "evidence_available_at_that_date": "non-price historical evidence separated by stage fields; no price-only promotion", "evidence_source": "public earnings/disclosure and analyst/narrative evidence; stock-web only for OHLC", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv|atlas/ohlcv_tradable_by_symbol_year/383/383220/2025.csv", "profile_path": "atlas/symbol_profiles/383/383220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-08-05", "entry_price": 48000, "MFE_30D_pct": 22.5, "MFE_90D_pct": 50.21, "MFE_180D_pct": 55.83, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.77, "MAE_90D_pct": -1.77, "MAE_180D_pct": -1.77, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-20", "peak_price": 74800, "drawdown_after_peak_pct": -38.29, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_a_positive_entry_signal", "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "false_break_or_late_watch_only", "trigger_outcome_label": "4C_late_watch_only", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R5L39_C18_383220_20240805_48000", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": false, "reuse_reason": "label_or_overlay_comparison_same_loop", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
```

### 25.4 score_simulation rows
```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L39_C18_003230_SYF_EXPORT_REORDER", "trigger_id": "R5L39_C18_003230_STAGE2A_20240517", "symbol": "003230", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 18, "revision_score": 18, "relative_strength_score": 14, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 14, "customer_quality_score": 14, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow-high", "changed_components": ["margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "C18 shadow gate rewards repeat reorder + margin bridge and caps reopening/restock without revision.", "MFE_90D_pct": 60.81, "MAE_90D_pct": 0.0, "score_return_alignment_label": "current_profile_correct", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L39_C18_005180_BINGGRAE_EXPORT_REORDER", "trigger_id": "R5L39_C18_005180_STAGE2A_20240517", "symbol": "005180", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 14, "revision_score": 12, "relative_strength_score": 14, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 14, "revision_score": 12, "relative_strength_score": 14, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": ["margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "C18 shadow gate rewards repeat reorder + margin bridge and caps reopening/restock without revision.", "MFE_90D_pct": 34.09, "MAE_90D_pct": -32.96, "score_return_alignment_label": "current_profile_correct", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L39_C18_383220_FNF_CHINA_REOPENING_FALSE_REORDER", "trigger_id": "R5L39_C18_383220_STAGE2_FALSE_20240503", "symbol": "383220", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 12, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 68, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 1, "relative_strength_score": 8, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 18, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 55, "stage_label_after": "Watch-Guarded", "changed_components": ["margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "C18 shadow gate rewards repeat reorder + margin bridge and caps reopening/restock without revision.", "MFE_90D_pct": 4.95, "MAE_90D_pct": -35.23, "score_return_alignment_label": "current_profile_false_positive", "current_profile_verdict": "current_profile_false_positive"}
```

### 25.5 shadow_weight rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C18_repeat_reorder_margin_bridge_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,export reorder plus margin bridge/revision improves alignment,avg90 MFE improves to 47.45 after blocking false positive,R5L39_C18_003230_STAGE2A_20240517|R5L39_C18_005180_STAGE2A_20240517,3,3,1,medium_low,canonical_shadow_only,not production
shadow_weight,C18_brand_reopening_without_revision_cap,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,brand/channel restock without revision produced F&F false positive,false positive rate 33.3% to 0% in small set,R5L39_C18_383220_STAGE2_FALSE_20240503,3,3,1,medium_low,counterexample_guard,not production
```

### 25.6 residual_contribution row
```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": "39", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min", "stage3_cross_evidence_green_buffer", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["brand_reopening_restock_false_positive", "high_mae_export_success", "price_only_local_4B_too_early"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "auto_selected_coverage_gap": "L5/C18 consumer export channel reorder"}
```

### 25.7 narrative_only rows
```jsonl
{"row_type": "narrative_only", "case_id": "none", "symbol": "000000", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "reason": "all selected representative cases had clean 180D stock-web windows; no narrative-only rows used for calibration", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
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

Recommended next coverage: R5/C19 brand retail inventory margin counterexamples, R5/C20 additional non-food beauty distributor false positives, or R6/C21 financial ROE/PBR capital-return holdout.

## 28. Source Notes

Stock-web files consulted: atlas/manifest.json; atlas/schema.json; atlas/symbol_profiles/003/003230.json; atlas/symbol_profiles/005/005180.json; atlas/symbol_profiles/383/383220.json; atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv; atlas/ohlcv_tradable_by_symbol_year/003/003230/2025.csv; atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv; atlas/ohlcv_tradable_by_symbol_year/005/005180/2025.csv; atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv; atlas/ohlcv_tradable_by_symbol_year/383/383220/2025.csv.

Research artifact files consulted for duplicate avoidance: reports/e2r_calibration/ingest_summary.md and repository search for C18_CONSUMER_EXPORT_CHANNEL_REORDER. No stock_agent source code was opened.

This document is historical calibration research only. It is not a current/live stock recommendation and does not change production scoring.

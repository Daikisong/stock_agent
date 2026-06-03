# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
scheduled_round: R5
scheduled_loop: 74
completed_round: R5
completed_loop: 74
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: EXPORT_REORDER_QUALITY_VS_KFOOD_THEME_PROXY
output_file: e2r_stock_web_v12_residual_round_R5_loop_74_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_web_price_atlas_access_required: true
```

This loop adds 4 new independent cases, 2 counterexamples, and 4 residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C18_CONSUMER_EXPORT_CHANNEL_REORDER.

## 1. Current Calibrated Profile Assumption

- current_default_profile_proxy: `e2r_2_1_stock_web_calibrated`
- rollback_reference_profile_id: `e2r_2_0_baseline_reference`
- Existing applied axes are treated as already applied and tested only for residual behavior: `stage2_actionable_evidence_bonus`, `stage3_yellow_total_min`, `stage3_green_total_min`, `stage3_green_revision_min`, `stage3_cross_evidence_green_buffer`, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`, `hard_4c_thesis_break_routes_to_4c`.
- Existing-axis result: `existing_axis_strengthened` for price-only blowoff and non-price 4B requirement; `existing_axis_kept` for global Stage2/Yellow/Green thresholds.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R5 |
| scheduled_loop | 74 |
| required_large_sector_id | L5_CONSUMER_BRAND_DISTRIBUTION |
| selected_canonical_archetype_id | C18_CONSUMER_EXPORT_CHANNEL_REORDER |
| fine_archetype_id | EXPORT_REORDER_QUALITY_VS_KFOOD_THEME_PROXY |
| round_schedule_status | valid |
| round_sector_consistency | pass |
| loop_objective | sector_specific_rule_discovery, canonical_archetype_compression, counterexample_mining, 4B_non_price_requirement_stress_test, coverage_gap_fill |

## 3. Previous Coverage / Duplicate Avoidance Check

Local previous R5 outputs in the working set used C20 loop 71 (`192820, 161890, 214420, 226320`), C18 loop 72 (`003230, 005180, 383220, 081660`), and C19 loop 73 (`036620, 337930, 298540, 031430`). This loop deliberately uses `017810, 271560, 103840, 011150`, so the hard duplicate key is not repeated.

| duplicate gate | result |
|---|---|
| same canonical allowed | yes |
| previous R5 selected symbol reuse | 0 |
| new_symbol_count | 4 |
| new_trigger_family_count | 4 |
| reused_case_count | 0 |
| schema_rematerialization_only | false |

## 4. Stock-Web OHLC Input / Price Source Validation

| manifest field | value |
|---|---|
| source_name | `FinanceData/marcap` |
| source_repo_url | `https://github.com/FinanceData/marcap` |
| price_adjustment_status | `raw_unadjusted_marcap` |
| min_date | `1995-05-02` |
| max_date | `2026-02-20` |
| tradable_row_count | `14354401` |
| raw_row_count | `15214118` |
| symbol_count | `5414` |
| active_like_symbol_count | `2868` |
| inactive_or_delisted_like_symbol_count | `2546` |
| markets | `['KONEX', 'KOSDAQ', 'KOSDAQ GLOBAL', 'KOSPI']` |
| calibration_shard_root | `atlas/ohlcv_tradable_by_symbol_year` |
| raw_shard_root | `atlas/ohlcv_raw_by_symbol_year` |
| schema_path | `atlas/schema.json` |
| universe_path | `atlas/universe/all_symbols.csv` |

The stock-web manifest max date is `2026-02-20`, so every 2024 trigger below has at least a 180-trading-day forward window. The schema basis is `tradable_raw`; tradable shards contain `d,o,h,l,c,v,a,mc,s,m`, while raw shards add `rs`. No adjusted-price inference is used.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry row exists | >=180 forward tradable days | corporate_action_window_status | calibration_usable |
|---|---:|---|---|---|---|---|
| R5L74_C18_017810_20240517_US_TOFU_EXPORT_TURNAROUND | 017810 | 2024-05-17 | true | true | clean_180D_window; historical corporate candidates outside 2024 window | true |
| R5L74_C18_271560_20240517_GLOBAL_STAPLE_REORDER_MISSED | 271560 | 2024-05-17 | true | true | clean_180D_window | true |
| R5L74_C18_103840_20240517_FROZEN_KIMBAP_THEME_BLOWOFF | 103840 | 2024-05-17 | true | true | clean_180D_window | true |
| R5L74_C18_011150_20240517_SEAWEED_PROXY_FALSE_PROMOTION | 011150 | 2024-05-17 | true | true | clean_180D_window; historical corporate candidate outside 2024 window | true |

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression logic |
|---|---|---|
| EXPORT_REORDER_QUALITY_VS_KFOOD_THEME_PROXY | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18 is compressed around **reorder quality**, not theme heat: verified repeat sell-through + channel/inventory/margin bridge is promotable; K-food/ingredient proxy without conversion is watch-only even if MFE is high. |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_family | current_profile_verdict |
|---|---:|---|---|---|---|
| R5L74_C18_017810_20240517_US_TOFU_EXPORT_TURNAROUND | 017810 | 풀무원 | high_mae_success / positive | overseas_channel_margin_turnaround_with_earnings_confirmation | current_profile_4B_too_late |
| R5L74_C18_271560_20240517_GLOBAL_STAPLE_REORDER_MISSED | 271560 | 오리온 | missed_structural / positive | largecap_global_reorder_low_drawdown_slow_rerating | current_profile_missed_structural |
| R5L74_C18_103840_20240517_FROZEN_KIMBAP_THEME_BLOWOFF | 103840 | 우양 | 4B_overlay_success / counterexample | smallcap_export_theme_without_repeat_reorder_proof | current_profile_4B_too_late |
| R5L74_C18_011150_20240517_SEAWEED_PROXY_FALSE_PROMOTION | 011150 | CJ씨푸드 | failed_rerating / counterexample | ingredient_proxy_without_channel_margin_bridge | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

| positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | calibration_usable_case_count |
|---:|---:|---:|---:|---:|
| 2 | 2 | 3 | 2 | 4 |

The positive side covers a high-MFE/high-MAE export turnaround and a slower low-MAE global reorder compounder. The counterexample side covers smallcap K-food theme heat and ingredient/export proxy heat. This creates a cleaner gate than a generic “consumer export up” rule.

## 9. Evidence Source Map

| trigger_id | evidence source status | Stage2 fields | Stage3 fields | 4B fields | 4C fields |
|---|---|---|---|---|---|
| R5L74_C18_017810_STAGE2A_20240517_US_EXPORT_MARGIN | source_proxy_only_research_note + stock-web verified OHLC rows: 017/017810/2024.csv | `public_event_or_disclosure,customer_or_order_quality,capacity_or_volume_route,early_revision_signal,relative_strength` | `confirmed_revision,margin_bridge,financial_visibility,repeat_order_or_conversion` | `valuation_blowoff,positioning_overheat,margin_or_backlog_slowdown` | `` |
| R5L74_C18_271560_STAGE2A_20240517_GLOBAL_REORDER_LOW_MAE | source_proxy_only_research_note + stock-web verified OHLC rows: 271/271560/2024.csv and 2025.csv | `public_event_or_disclosure,customer_or_order_quality,capacity_or_volume_route,early_revision_signal` | `confirmed_revision,margin_bridge,multiple_public_sources,financial_visibility,repeat_order_or_conversion,low_red_team_risk` | `` | `` |
| R5L74_C18_103840_STAGE2_THEME_20240517_KFOOD_PRICE_SPIKE | source_proxy_only_research_note + stock-web verified OHLC rows: 103/103840/2024.csv | `relative_strength,policy_or_regulatory_optionality` | `` | `price_only_local_peak,valuation_blowoff,positioning_overheat` | `thesis_evidence_broken` |
| R5L74_C18_011150_STAGE2_THEME_20240517_SEAWEED_KFOOD_PROXY | source_proxy_only_research_note + stock-web verified OHLC rows: 011/011150/2024.csv | `relative_strength,policy_or_regulatory_optionality` | `` | `price_only_local_peak,valuation_blowoff,positioning_overheat` | `thesis_evidence_broken` |

## 10. Price Data Source Map

| symbol | company | entry row source | profile_path | price_basis | adjustment |
|---:|---|---|---|---|---|
| 017810 | 풀무원 | `atlas/ohlcv_tradable_by_symbol_year/017/017810/2024.csv` | `atlas/symbol_profiles/017/017810.json` | tradable_raw | raw_unadjusted_marcap |
| 271560 | 오리온 | `atlas/ohlcv_tradable_by_symbol_year/271/271560/2024.csv|atlas/ohlcv_tradable_by_symbol_year/271/271560/2025.csv` | `atlas/symbol_profiles/271/271560.json` | tradable_raw | raw_unadjusted_marcap |
| 103840 | 우양 | `atlas/ohlcv_tradable_by_symbol_year/103/103840/2024.csv` | `atlas/symbol_profiles/103/103840.json` | tradable_raw | raw_unadjusted_marcap |
| 011150 | CJ씨푸드 | `atlas/ohlcv_tradable_by_symbol_year/011/011150/2024.csv` | `atlas/symbol_profiles/011/011150.json` | tradable_raw | raw_unadjusted_marcap |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | entry | score_before -> after | label_before -> after | outcome |
|---|---|---:|---:|---|---|
| R5L74_C18_017810_STAGE2A_20240517_US_EXPORT_MARGIN | Stage2-Actionable | 2024-05-17 / 13760 | 84 -> 88 | Stage3-Yellow -> Stage3-Green+4B-Watch | positive_high_mfe_but_high_mae_requires_4b_overlay |
| R5L74_C18_271560_STAGE2A_20240517_GLOBAL_REORDER_LOW_MAE | Stage2-Actionable | 2024-05-17 / 91900 | 74 -> 80 | Stage2-Actionable / below Yellow -> Stage3-Yellow / low-MAE compounder | slow_structural_success_low_mae |
| R5L74_C18_103840_STAGE2_THEME_20240517_KFOOD_PRICE_SPIKE | Stage2-PriceOnlyWatch | 2024-05-17 / 4830 | 76 -> 60 | Stage3-Yellow / false promotion risk -> Stage2-Watch / price-only blocked | theme_blowoff_high_mfe_high_mae_roundtrip |
| R5L74_C18_011150_STAGE2_THEME_20240517_SEAWEED_KFOOD_PROXY | Stage2-FalsePositive | 2024-05-17 / 3985 | 75 -> 58 | Stage3-Yellow / false promotion risk -> Stage2-Watch / proxy blocked | false_positive_export_proxy_roundtrip |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak | below_entry_30D | below_entry_90D |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|---|
| R5L74_C18_017810_STAGE2A_20240517_US_EXPORT_MARGIN | 13760 | 33.79% | -6.32% | 33.79% | -27.25% | 33.79% | -30.96% | 2024-06-14 | 18410 | -48.40% | true | true |
| R5L74_C18_271560_STAGE2A_20240517_GLOBAL_REORDER_LOW_MAE | 91900 | 16.10% | -1.31% | 16.10% | -10.99% | 20.13% | -10.99% | 2025-02-14 | 110400 | -8.06% | true | true |
| R5L74_C18_103840_STAGE2_THEME_20240517_KFOOD_PRICE_SPIKE | 4830 | 156.31% | -10.97% | 156.31% | -15.32% | 156.31% | -43.79% | 2024-06-13 | 12380 | -78.07% | true | true |
| R5L74_C18_011150_STAGE2_THEME_20240517_SEAWEED_KFOOD_PROXY | 3985 | 62.86% | -5.90% | 62.86% | -22.33% | 62.86% | -36.51% | 2024-06-17 | 6490 | -61.02% | true | true |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely judgment | actual MFE/MAE alignment | current_profile_verdict | residual |
|---|---|---|---|---|
| R5L74_C18_017810_20240517_US_TOFU_EXPORT_TURNAROUND | Correctly promotes Stage2, but likely lets 4B arrive late. | +33.79% MFE but -30.96% 180D MAE after peak. | current_profile_4B_too_late | Need 4B-watch when rerating is already near full local peak. |
| R5L74_C18_271560_20240517_GLOBAL_STAPLE_REORDER_MISSED | May stay below Yellow because move is slow and not explosive. | +20.13% 180D MFE with only -10.99% MAE. | current_profile_missed_structural | Low-MAE global reorder compounder should get C18 reorder-quality bonus. |
| R5L74_C18_103840_20240517_FROZEN_KIMBAP_THEME_BLOWOFF | May over-promote because early MFE is huge. | +156.31% MFE but -43.79% MAE and -78.07% post-peak drawdown. | current_profile_4B_too_late | Theme-only K-food proxy needs positive-stage cap. |
| R5L74_C18_011150_20240517_SEAWEED_PROXY_FALSE_PROMOTION | May over-promote export/ingredient proxy. | +62.86% MFE but -36.51% MAE and -61.02% post-peak drawdown. | current_profile_false_positive | Ingredient proxy lacks branded reorder/margin bridge. |

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 Actionable entry | Stage3/Green issue | green_lateness_ratio | interpretation |
|---|---|---|---|---|
| R5L74_C18_017810_20240517_US_TOFU_EXPORT_TURNAROUND | 2024-05-17 @ 13760 | Stage3-Green+4B-Watch | not_applicable:no_confirmed_Stage3_Green_trigger_before_peak | current_profile_4B_too_late |
| R5L74_C18_271560_20240517_GLOBAL_STAPLE_REORDER_MISSED | 2024-05-17 @ 91900 | Stage3-Yellow / low-MAE compounder | not_applicable:slow_compounder_no_single_green_shock | current_profile_missed_structural |
| R5L74_C18_103840_20240517_FROZEN_KIMBAP_THEME_BLOWOFF | 2024-05-17 @ 4830 | Stage2-Watch / price-only blocked | not_applicable:no_confirmed_Stage3_Green_trigger | current_profile_4B_too_late |
| R5L74_C18_011150_20240517_SEAWEED_PROXY_FALSE_PROMOTION | 2024-05-17 @ 3985 | Stage2-Watch / proxy blocked | not_applicable:no_confirmed_Stage3_Green_trigger | current_profile_false_positive |

## 15. 4B Local vs Full-window Timing Audit

| case_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | evidence_type | timing verdict |
|---|---:|---:|---|---|
| R5L74_C18_017810_20240517_US_TOFU_EXPORT_TURNAROUND | 0.83 | 0.83 | `valuation_blowoff,positioning_overheat,revision_slowdown` | good_full_window_4B_watch_but_not_stage_exit |
| R5L74_C18_271560_20240517_GLOBAL_STAPLE_REORDER_MISSED | null | null | `` | not_applicable |
| R5L74_C18_103840_20240517_FROZEN_KIMBAP_THEME_BLOWOFF | 0.85 | 0.85 | `price_only,valuation_blowoff,positioning_overheat` | price_only_local_4B_watch_not_full_4B |
| R5L74_C18_011150_20240517_SEAWEED_PROXY_FALSE_PROMOTION | 0.93 | 0.93 | `price_only,valuation_blowoff,positioning_overheat` | price_only_local_4B_watch_not_full_4B |

Interpretation: `017810` has enough non-price evidence to be a 4B-watch overlay on top of a real thesis. `103840` and `011150` have price-only/theme-heavy local peaks, so those rows should not become full positive Stage3/Green.

## 16. 4C Protection Audit

| case_id | 4C protection label | thesis-break reading |
|---|---|---|
| R5L74_C18_017810_20240517_US_TOFU_EXPORT_TURNAROUND | thesis_break_watch_only | watch only / no hard break |
| R5L74_C18_271560_20240517_GLOBAL_STAPLE_REORDER_MISSED | not_applicable | watch only / no hard break |
| R5L74_C18_103840_20240517_FROZEN_KIMBAP_THEME_BLOWOFF | hard_4c_success_after_theme_fade | hard proxy fade |
| R5L74_C18_011150_20240517_SEAWEED_PROXY_FALSE_PROMOTION | hard_4c_success_after_proxy_fade | hard proxy fade |

## 17. Sector-Specific Rule Candidate

**Rule candidate: `l5_consumer_export_reorder_quality_gate`.** In R5, export/channel evidence should be promoted only when at least one of the following is present before or at trigger date: repeat sell-through, channel reorder confirmation, inventory-quality improvement, or margin bridge. If evidence is only K-food/ingredient theme + relative strength, cap at Stage2-Watch and allow only 4B overlay rows.

## 18. Canonical-Archetype Rule Candidate

**Canonical candidate: `c18_reorder_quality_bonus` and `c18_theme_proxy_positive_stage_cap`.** C18 should reward durable reorder quality even when price action is slower (`271560`), but should not promote smallcap/ingredient proxies even when MFE is explosive (`103840`, `011150`).

## 19. Before / After Backtest Comparison

| profile_id | eligible_trigger_count | selected entries | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | 4 | 017810|271560|103840|011150 | 67.27 | -18.97 | 68.27 | -30.56 | 0.5 | 1 | mixed: positives align, but proxy false positives and 4B lateness remain |
| P0b_e2r_2_0_baseline_reference | 4 | 017810|271560|103840|011150 | 67.27 | -18.97 | 68.27 | -30.56 | 0.25 | 2 | too conservative on true reorder, insufficient overlay model for blowoffs |
| P1_L5_consumer_reorder_quality_shadow | 4 | 017810|271560|103840|011150 | 24.95 | -19.12 | 26.96 | -20.98 | 0.0 | 0 | better separation: keeps 017810/271560 and blocks 103840/011150 positive promotion |
| P2_C18_export_reorder_shadow | 4 | 017810|271560|103840|011150 | 24.95 | -19.12 | 26.96 | -20.98 | 0.0 | 0 | canonical rule candidate improves score-return alignment |
| P3_counterexample_guard_profile | 2 | 103840|011150 | 109.59 | -18.82 | 109.59 | -40.15 | 0.0 | 0 | guard catches high-MAE roundtrip proxies |

## 20. Score-Return Alignment Matrix

| case_id | before score/label | after score/label | MFE_90D | MAE_90D | alignment |
|---|---|---|---:|---:|---|
| R5L74_C18_017810_20240517_US_TOFU_EXPORT_TURNAROUND | 84 / Stage3-Yellow | 88 / Stage3-Green+4B-Watch | 33.79 | -27.25 | positive_high_mfe_but_high_mae_requires_4b_overlay |
| R5L74_C18_271560_20240517_GLOBAL_STAPLE_REORDER_MISSED | 74 / Stage2-Actionable / below Yellow | 80 / Stage3-Yellow / low-MAE compounder | 16.10 | -10.99 | slow_structural_success_low_mae |
| R5L74_C18_103840_20240517_FROZEN_KIMBAP_THEME_BLOWOFF | 76 / Stage3-Yellow / false promotion risk | 60 / Stage2-Watch / price-only blocked | 156.31 | -15.32 | theme_blowoff_high_mfe_high_mae_roundtrip |
| R5L74_C18_011150_20240517_SEAWEED_PROXY_FALSE_PROMOTION | 75 / Stage3-Yellow / false promotion risk | 58 / Stage2-Watch / proxy blocked | 62.86 | -22.33 | false_positive_export_proxy_roundtrip |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C18_CONSUMER_EXPORT_CHANNEL_REORDER | EXPORT_REORDER_QUALITY_VS_KFOOD_THEME_PROXY | 2 | 2 | 3 | 2 | 4 | 0 | 7 | 4 | 4 | true | true | C18 now has additional K-food proxy false-positive and low-MAE reorder compounder coverage. |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"]
residual_error_types_found: ["kfood_theme_proxy_false_positive", "ingredient_export_proxy_roundtrip", "positive_high_mae_4b_late", "slow_low_mae_reorder_missed_structural"]
new_axis_proposed: ["c18_reorder_quality_bonus", "c18_theme_proxy_positive_stage_cap"]
existing_axis_strengthened: ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"]
existing_axis_weakened: []
existing_axis_kept: ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min"]
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: "canonical_archetype_rule_candidate"
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated: stock-web manifest/schema basis, symbol profiles, tradable shard paths, 2024/2025 entry rows, 30D/90D/180D MFE/MAE, peak and drawdown audit, 4B local-vs-full proximity split, novelty and duplicate-avoidance fields. Not validated: production source URLs for every earnings/news claim; these are `source_proxy_only` and must be replaced by DART/IR/news URLs before promotion. No stock_agent code was opened or patched.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c18_reorder_quality_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,+3,+3,"Verified repeat sell-through, channel reorder quality, and inventory/margin bridge separated 017810/271560 from K-food theme proxies","Retains two positives while reducing missed structural count; does not relax Green globally","R5L74_C18_017810_STAGE2A_20240517_US_EXPORT_MARGIN|R5L74_C18_271560_STAGE2A_20240517_GLOBAL_REORDER_LOW_MAE",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c18_theme_proxy_positive_stage_cap,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,none,Stage2-Watch,cap,"Smallcap K-food or ingredient/export proxy without company-specific reorder conversion produced large MFE but severe MAE/drawdown","Blocks 103840 and 011150 from positive promotion while preserving 4B watch information","R5L74_C18_103840_STAGE2_THEME_20240517_KFOOD_PRICE_SPIKE|R5L74_C18_011150_STAGE2_THEME_20240517_SEAWEED_KFOOD_PROXY",4,4,2,medium,canonical_shadow_only,"strengthens existing price-only blowoff and non-price 4B requirements"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation
```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","upstream_source":"FinanceData/marcap","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","manifest_min_date":"1995-05-02","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"inactive_or_delisted_like_symbol_count":2546,"markets":["KONEX","KOSDAQ","KOSDAQ GLOBAL","KOSPI"],"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows
```jsonl
{"row_type":"case","case_id":"R5L74_C18_017810_20240517_US_TOFU_EXPORT_TURNAROUND","symbol":"017810","company_name":"풀무원","round":"R5","loop":"74","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"EXPORT_REORDER_QUALITY_VS_KFOOD_THEME_PROXY","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R5L74_C18_017810_STAGE2A_20240517_US_EXPORT_MARGIN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_mfe_but_high_mae_requires_4b_overlay","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"source_proxy_only: quarterly earnings/overseas turnaround and export-channel narrative were visible around the trigger; price row confirms a non-price evidence shock, not a pure chart-only spike."}
{"row_type":"case","case_id":"R5L74_C18_271560_20240517_GLOBAL_STAPLE_REORDER_MISSED","symbol":"271560","company_name":"오리온","round":"R5","loop":"74","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"EXPORT_REORDER_QUALITY_VS_KFOOD_THEME_PROXY","case_type":"missed_structural","positive_or_counterexample":"positive","best_trigger":"R5L74_C18_271560_STAGE2A_20240517_GLOBAL_REORDER_LOW_MAE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"slow_structural_success_low_mae","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"source_proxy_only: global channel sell-through and steady country-level sales/margin narrative; not a one-day export theme. The stock-web path is slow but low-MAE, so strict Green timing can miss a structural consumer compounder."}
{"row_type":"case","case_id":"R5L74_C18_103840_20240517_FROZEN_KIMBAP_THEME_BLOWOFF","symbol":"103840","company_name":"우양","round":"R5","loop":"74","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"EXPORT_REORDER_QUALITY_VS_KFOOD_THEME_PROXY","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"R5L74_C18_103840_STAGE2_THEME_20240517_KFOOD_PRICE_SPIKE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"theme_blowoff_high_mfe_high_mae_roundtrip","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"source_proxy_only: frozen kimbap/K-food export attention and price/volume shock were visible; durable repeat reorder, customer concentration, and capacity-conversion proof were not sufficiently confirmed at trigger date."}
{"row_type":"case","case_id":"R5L74_C18_011150_20240517_SEAWEED_PROXY_FALSE_PROMOTION","symbol":"011150","company_name":"CJ씨푸드","round":"R5","loop":"74","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"EXPORT_REORDER_QUALITY_VS_KFOOD_THEME_PROXY","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R5L74_C18_011150_STAGE2_THEME_20240517_SEAWEED_KFOOD_PROXY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_export_proxy_roundtrip","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"source_proxy_only: seaweed/K-food export and ingredient proxy attention was visible, but the trigger lacked branded sell-through, repeat order, and margin-conversion evidence."}
```

### 25.3 trigger rows
```jsonl
{"row_type":"trigger","trigger_id":"R5L74_C18_017810_STAGE2A_20240517_US_EXPORT_MARGIN","case_id":"R5L74_C18_017810_20240517_US_TOFU_EXPORT_TURNAROUND","symbol":"017810","company_name":"풀무원","round":"R5","loop":"74","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"EXPORT_REORDER_QUALITY_VS_KFOOD_THEME_PROXY","sector":"food_export_fresh_processed","primary_archetype":"US tofu / overseas channel reorder + margin bridge","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-16","entry_date":"2024-05-17","entry_price":13760,"evidence_available_at_that_date":"source_proxy_only: quarterly earnings/overseas turnaround and export-channel narrative were visible around the trigger; price row confirms a non-price evidence shock, not a pure chart-only spike.","evidence_source":"source_proxy_only_research_note + stock-web verified OHLC rows: 017/017810/2024.csv","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal","relative_strength"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/017/017810/2024.csv","profile_path":"atlas/symbol_profiles/017/017810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":33.79,"MFE_90D_pct":33.79,"MFE_180D_pct":33.79,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.32,"MAE_90D_pct":-27.25,"MAE_180D_pct":-30.96,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-14","peak_price":18410,"drawdown_after_peak_pct":-48.4,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger_before_peak","four_b_local_peak_proximity":0.828,"four_b_full_window_peak_proximity":0.828,"four_b_timing_verdict":"good_full_window_4B_watch_but_not_stage_exit","four_b_evidence_type":["valuation_blowoff","positioning_overheat","revision_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_but_high_mae_requires_4b_overlay","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; historical corporate candidates outside 2024 window","same_entry_group_id":"R5L74_C18_017810_20240517_US_TOFU_EXPORT_TURNAROUND_2024-05-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L74_C18_271560_STAGE2A_20240517_GLOBAL_REORDER_LOW_MAE","case_id":"R5L74_C18_271560_20240517_GLOBAL_STAPLE_REORDER_MISSED","symbol":"271560","company_name":"오리온","round":"R5","loop":"74","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"EXPORT_REORDER_QUALITY_VS_KFOOD_THEME_PROXY","sector":"global_snack_distribution","primary_archetype":"multi-country staple sell-through / repeat reorder","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-16","entry_date":"2024-05-17","entry_price":91900,"evidence_available_at_that_date":"source_proxy_only: global channel sell-through and steady country-level sales/margin narrative; not a one-day export theme. The stock-web path is slow but low-MAE, so strict Green timing can miss a structural consumer compounder.","evidence_source":"source_proxy_only_research_note + stock-web verified OHLC rows: 271/271560/2024.csv and 2025.csv","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","multiple_public_sources","financial_visibility","repeat_order_or_conversion","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/271/271560/2024.csv|atlas/ohlcv_tradable_by_symbol_year/271/271560/2025.csv","profile_path":"atlas/symbol_profiles/271/271560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.1,"MFE_90D_pct":16.1,"MFE_180D_pct":20.13,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.31,"MAE_90D_pct":-10.99,"MAE_180D_pct":-10.99,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-14","peak_price":110400,"drawdown_after_peak_pct":-8.06,"green_lateness_ratio":"not_applicable:slow_compounder_no_single_green_shock","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"slow_structural_success_low_mae","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L74_C18_271560_20240517_GLOBAL_STAPLE_REORDER_MISSED_2024-05-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L74_C18_103840_STAGE2_THEME_20240517_KFOOD_PRICE_SPIKE","case_id":"R5L74_C18_103840_20240517_FROZEN_KIMBAP_THEME_BLOWOFF","symbol":"103840","company_name":"우양","round":"R5","loop":"74","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"EXPORT_REORDER_QUALITY_VS_KFOOD_THEME_PROXY","sector":"kfood_smallcap_export_theme","primary_archetype":"frozen kimbap / K-food channel theme without durable order visibility","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage2-PriceOnlyWatch","trigger_date":"2024-05-17","entry_date":"2024-05-17","entry_price":4830,"evidence_available_at_that_date":"source_proxy_only: frozen kimbap/K-food export attention and price/volume shock were visible; durable repeat reorder, customer concentration, and capacity-conversion proof were not sufficiently confirmed at trigger date.","evidence_source":"source_proxy_only_research_note + stock-web verified OHLC rows: 103/103840/2024.csv","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/103/103840/2024.csv","profile_path":"atlas/symbol_profiles/103/103840.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":156.31,"MFE_90D_pct":156.31,"MFE_180D_pct":156.31,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.97,"MAE_90D_pct":-15.32,"MAE_180D_pct":-43.79,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-13","peak_price":12380,"drawdown_after_peak_pct":-78.07,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.846,"four_b_full_window_peak_proximity":0.846,"four_b_timing_verdict":"price_only_local_4B_watch_not_full_4B","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"hard_4c_success_after_theme_fade","trigger_outcome_label":"theme_blowoff_high_mfe_high_mae_roundtrip","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L74_C18_103840_20240517_FROZEN_KIMBAP_THEME_BLOWOFF_2024-05-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L74_C18_011150_STAGE2_THEME_20240517_SEAWEED_KFOOD_PROXY","case_id":"R5L74_C18_011150_20240517_SEAWEED_PROXY_FALSE_PROMOTION","symbol":"011150","company_name":"CJ씨푸드","round":"R5","loop":"74","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"EXPORT_REORDER_QUALITY_VS_KFOOD_THEME_PROXY","sector":"seaweed_kfood_supply_proxy","primary_archetype":"ingredient/export proxy without brand reorder conversion","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage2-FalsePositive","trigger_date":"2024-05-17","entry_date":"2024-05-17","entry_price":3985,"evidence_available_at_that_date":"source_proxy_only: seaweed/K-food export and ingredient proxy attention was visible, but the trigger lacked branded sell-through, repeat order, and margin-conversion evidence.","evidence_source":"source_proxy_only_research_note + stock-web verified OHLC rows: 011/011150/2024.csv","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011150/2024.csv","profile_path":"atlas/symbol_profiles/011/011150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":62.86,"MFE_90D_pct":62.86,"MFE_180D_pct":62.86,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.9,"MAE_90D_pct":-22.33,"MAE_180D_pct":-36.51,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-17","peak_price":6490,"drawdown_after_peak_pct":-61.02,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.932,"four_b_full_window_peak_proximity":0.932,"four_b_timing_verdict":"price_only_local_4B_watch_not_full_4B","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"hard_4c_success_after_proxy_fade","trigger_outcome_label":"false_positive_export_proxy_roundtrip","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; historical corporate candidate outside 2024 window","same_entry_group_id":"R5L74_C18_011150_20240517_SEAWEED_PROXY_FALSE_PROMOTION_2024-05-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L74_C18_017810_4B_OVERLAY_20240517_US_EXPORT_MARGIN","case_id":"R5L74_C18_017810_20240517_US_TOFU_EXPORT_TURNAROUND","symbol":"017810","company_name":"풀무원","round":"R5","loop":"74","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"EXPORT_REORDER_QUALITY_VS_KFOOD_THEME_PROXY","sector":"food_export_fresh_processed","primary_archetype":"US tofu / overseas channel reorder + margin bridge","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2024-06-14","entry_date":"2024-06-14","entry_price":null,"evidence_available_at_that_date":"overlay comparison only: 4B timing measured against prior Stage2 Actionable entry and full observed peak","evidence_source":"stock-web price rows plus source_proxy_only risk evidence","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/017/017810/2024.csv","profile_path":"atlas/symbol_profiles/017/017810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":null,"MFE_90D_pct":null,"MFE_180D_pct":null,"MAE_30D_pct":null,"MAE_90D_pct":null,"MAE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":null,"below_entry_price_flag_90D":null,"peak_date":"2024-06-14","peak_price":18410,"drawdown_after_peak_pct":-48.4,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger_before_peak","four_b_local_peak_proximity":0.828,"four_b_full_window_peak_proximity":0.828,"four_b_timing_verdict":"good_full_window_4B_watch_but_not_stage_exit","four_b_evidence_type":["valuation_blowoff","positioning_overheat","revision_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_only","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; historical corporate candidates outside 2024 window","same_entry_group_id":"R5L74_C18_017810_20240517_US_TOFU_EXPORT_TURNAROUND_2024-06-14","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"4B_overlay_comparison_only","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R5L74_C18_103840_4B_OVERLAY_20240517_KFOOD_PRICE_SPIKE","case_id":"R5L74_C18_103840_20240517_FROZEN_KIMBAP_THEME_BLOWOFF","symbol":"103840","company_name":"우양","round":"R5","loop":"74","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"EXPORT_REORDER_QUALITY_VS_KFOOD_THEME_PROXY","sector":"kfood_smallcap_export_theme","primary_archetype":"frozen kimbap / K-food channel theme without durable order visibility","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2024-06-13","entry_date":"2024-06-13","entry_price":null,"evidence_available_at_that_date":"overlay comparison only: 4B timing measured against prior Stage2 Actionable entry and full observed peak","evidence_source":"stock-web price rows plus source_proxy_only risk evidence","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/103/103840/2024.csv","profile_path":"atlas/symbol_profiles/103/103840.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":null,"MFE_90D_pct":null,"MFE_180D_pct":null,"MAE_30D_pct":null,"MAE_90D_pct":null,"MAE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":null,"below_entry_price_flag_90D":null,"peak_date":"2024-06-13","peak_price":12380,"drawdown_after_peak_pct":-78.07,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.846,"four_b_full_window_peak_proximity":0.846,"four_b_timing_verdict":"price_only_local_4B_watch_not_full_4B","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"hard_4c_success_after_theme_fade","trigger_outcome_label":"4B_overlay_only","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L74_C18_103840_20240517_FROZEN_KIMBAP_THEME_BLOWOFF_2024-06-13","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"4B_overlay_comparison_only","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R5L74_C18_011150_4B_OVERLAY_20240517_SEAWEED_KFOOD_PROXY","case_id":"R5L74_C18_011150_20240517_SEAWEED_PROXY_FALSE_PROMOTION","symbol":"011150","company_name":"CJ씨푸드","round":"R5","loop":"74","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"EXPORT_REORDER_QUALITY_VS_KFOOD_THEME_PROXY","sector":"seaweed_kfood_supply_proxy","primary_archetype":"ingredient/export proxy without brand reorder conversion","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2024-06-17","entry_date":"2024-06-17","entry_price":null,"evidence_available_at_that_date":"overlay comparison only: 4B timing measured against prior Stage2 Actionable entry and full observed peak","evidence_source":"stock-web price rows plus source_proxy_only risk evidence","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011150/2024.csv","profile_path":"atlas/symbol_profiles/011/011150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":null,"MFE_90D_pct":null,"MFE_180D_pct":null,"MAE_30D_pct":null,"MAE_90D_pct":null,"MAE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":null,"below_entry_price_flag_90D":null,"peak_date":"2024-06-17","peak_price":6490,"drawdown_after_peak_pct":-61.02,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.932,"four_b_full_window_peak_proximity":0.932,"four_b_timing_verdict":"price_only_local_4B_watch_not_full_4B","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"hard_4c_success_after_proxy_fade","trigger_outcome_label":"4B_overlay_only","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; historical corporate candidate outside 2024 window","same_entry_group_id":"R5L74_C18_011150_20240517_SEAWEED_PROXY_FALSE_PROMOTION_2024-06-17","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"4B_overlay_comparison_only","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
```

### 25.4 score_simulation rows
```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C18_shadow","case_id":"R5L74_C18_017810_20240517_US_TOFU_EXPORT_TURNAROUND","trigger_id":"R5L74_C18_017810_STAGE2A_20240517_US_EXPORT_MARGIN","symbol":"017810","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":14,"revision_score":12,"relative_strength_score":15,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":13,"sellthrough_score":12,"inventory_quality_score":8,"gross_margin_score":13,"brand_heat_score":5,"positioning_overheat_score":-3,"thesis_break_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":17,"revision_score":14,"relative_strength_score":15,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":17,"sellthrough_score":15,"inventory_quality_score":10,"gross_margin_score":16,"brand_heat_score":4,"positioning_overheat_score":-10,"thesis_break_score":0},"weighted_score_after":88,"stage_label_after":"Stage3-Green+4B-Watch","changed_components":["channel_reorder_score","sellthrough_score","inventory_quality_score","gross_margin_score","positioning_overheat_score","thesis_break_score"],"component_delta_explanation":"C18 shadow rewards verified repeat sell-through, reorder quality, inventory quality, and margin bridge; caps ingredient/smallcap K-food theme proxies without channel conversion.","MFE_90D_pct":33.79,"MAE_90D_pct":-27.25,"score_return_alignment_label":"positive_high_mfe_but_high_mae_requires_4b_overlay","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C18_shadow","case_id":"R5L74_C18_271560_20240517_GLOBAL_STAPLE_REORDER_MISSED","trigger_id":"R5L74_C18_271560_STAGE2A_20240517_GLOBAL_REORDER_LOW_MAE","symbol":"271560","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":11,"revision_score":9,"relative_strength_score":5,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":13,"sellthrough_score":13,"inventory_quality_score":12,"gross_margin_score":11,"brand_heat_score":2,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable / below Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":13,"revision_score":11,"relative_strength_score":5,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":16,"sellthrough_score":16,"inventory_quality_score":14,"gross_margin_score":13,"brand_heat_score":1,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow / low-MAE compounder","changed_components":["channel_reorder_score","sellthrough_score","inventory_quality_score","gross_margin_score","positioning_overheat_score","thesis_break_score"],"component_delta_explanation":"C18 shadow rewards verified repeat sell-through, reorder quality, inventory quality, and margin bridge; caps ingredient/smallcap K-food theme proxies without channel conversion.","MFE_90D_pct":16.1,"MAE_90D_pct":-10.99,"score_return_alignment_label":"slow_structural_success_low_mae","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C18_shadow","case_id":"R5L74_C18_103840_20240517_FROZEN_KIMBAP_THEME_BLOWOFF","trigger_id":"R5L74_C18_103840_STAGE2_THEME_20240517_KFOOD_PRICE_SPIKE","symbol":"103840","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":18,"customer_quality_score":3,"policy_or_regulatory_score":6,"valuation_repricing_score":14,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":5,"sellthrough_score":4,"inventory_quality_score":0,"gross_margin_score":2,"brand_heat_score":9,"positioning_overheat_score":-3,"thesis_break_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow / false promotion risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":14,"customer_quality_score":2,"policy_or_regulatory_score":3,"valuation_repricing_score":7,"execution_risk_score":-12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":1,"sellthrough_score":1,"inventory_quality_score":-8,"gross_margin_score":0,"brand_heat_score":3,"positioning_overheat_score":-15,"thesis_break_score":-8},"weighted_score_after":60,"stage_label_after":"Stage2-Watch / price-only blocked","changed_components":["channel_reorder_score","sellthrough_score","inventory_quality_score","gross_margin_score","positioning_overheat_score","thesis_break_score"],"component_delta_explanation":"C18 shadow rewards verified repeat sell-through, reorder quality, inventory quality, and margin bridge; caps ingredient/smallcap K-food theme proxies without channel conversion.","MFE_90D_pct":156.31,"MAE_90D_pct":-15.32,"score_return_alignment_label":"theme_blowoff_high_mfe_high_mae_roundtrip","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C18_shadow","case_id":"R5L74_C18_011150_20240517_SEAWEED_PROXY_FALSE_PROMOTION","trigger_id":"R5L74_C18_011150_STAGE2_THEME_20240517_SEAWEED_KFOOD_PROXY","symbol":"011150","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":16,"customer_quality_score":3,"policy_or_regulatory_score":6,"valuation_repricing_score":13,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":4,"sellthrough_score":3,"inventory_quality_score":0,"gross_margin_score":2,"brand_heat_score":7,"positioning_overheat_score":-3,"thesis_break_score":0},"weighted_score_before":75,"stage_label_before":"Stage3-Yellow / false promotion risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":12,"customer_quality_score":1,"policy_or_regulatory_score":3,"valuation_repricing_score":6,"execution_risk_score":-10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":0,"sellthrough_score":0,"inventory_quality_score":-7,"gross_margin_score":0,"brand_heat_score":2,"positioning_overheat_score":-13,"thesis_break_score":-8},"weighted_score_after":58,"stage_label_after":"Stage2-Watch / proxy blocked","changed_components":["channel_reorder_score","sellthrough_score","inventory_quality_score","gross_margin_score","positioning_overheat_score","thesis_break_score"],"component_delta_explanation":"C18 shadow rewards verified repeat sell-through, reorder quality, inventory quality, and margin bridge; caps ingredient/smallcap K-food theme proxies without channel conversion.","MFE_90D_pct":62.86,"MAE_90D_pct":-22.33,"score_return_alignment_label":"false_positive_export_proxy_roundtrip","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"profile_aggregate","round":"R5","loop":"74","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_global_proxy","profile_hypothesis":"Current profile recognizes Stage2 evidence but still lets smallcap/ingredient export theme proxies become too promotable and can be too slow on low-MAE global reorder compounders.","changed_axes":[],"changed_thresholds":{},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"017810|271560|103840|011150","avg_MFE_90D_pct":67.27,"avg_MAE_90D_pct":-18.97,"avg_MFE_180D_pct":68.27,"avg_MAE_180D_pct":-30.56,"false_positive_rate":0.5,"missed_structural_count":1,"late_green_count":1,"avg_green_lateness_ratio":"not_applicable_mixed","avg_four_b_local_peak_proximity":0.869,"avg_four_b_full_window_peak_proximity":0.869,"score_return_alignment_verdict":"mixed: positives align, but proxy false positives and 4B lateness remain"}
{"row_type":"profile_aggregate","round":"R5","loop":"74","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_id":"P0b_e2r_2_0_baseline_reference","profile_scope":"rollback_reference","profile_hypothesis":"Older baseline under-recognizes Stage2 actionable non-price consumer channel evidence and gives less structure to 4B proxy blowoffs.","changed_axes":["rollback_reference_only"],"changed_thresholds":{},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"017810|271560|103840|011150","avg_MFE_90D_pct":67.27,"avg_MAE_90D_pct":-18.97,"avg_MFE_180D_pct":68.27,"avg_MAE_180D_pct":-30.56,"false_positive_rate":0.25,"missed_structural_count":2,"late_green_count":2,"avg_green_lateness_ratio":"not_applicable_mixed","avg_four_b_local_peak_proximity":0.869,"avg_four_b_full_window_peak_proximity":0.869,"score_return_alignment_verdict":"too conservative on true reorder, insufficient overlay model for blowoffs"}
{"row_type":"profile_aggregate","round":"R5","loop":"74","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_id":"P1_L5_consumer_reorder_quality_shadow","profile_scope":"sector_specific","profile_hypothesis":"In R5, only verified repeat sell-through + inventory/margin quality should unlock Stage3; K-food or ingredient theme proxies should remain Stage2-Watch even when MFE is large.","changed_axes":["repeat_sellthrough_quality_gate","smallcap_theme_proxy_cap","inventory_margin_bridge_bonus"],"changed_thresholds":{"consumer_stage3_yellow_requires_reorder_or_margin_bridge":true},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"017810|271560|103840|011150","avg_MFE_90D_pct":24.95,"avg_MAE_90D_pct":-19.12,"avg_MFE_180D_pct":26.96,"avg_MAE_180D_pct":-20.98,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable_mixed","avg_four_b_local_peak_proximity":0.869,"avg_four_b_full_window_peak_proximity":0.869,"score_return_alignment_verdict":"better separation: keeps 017810/271560 and blocks 103840/011150 positive promotion"}
{"row_type":"profile_aggregate","round":"R5","loop":"74","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_id":"P2_C18_export_reorder_shadow","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C18 should compress food export and brand export cases by reorder quality, not by theme heat. Ingredient/smallcap proxies need a conversion bridge before promotion.","changed_axes":["c18_reorder_quality_bonus","c18_proxy_without_conversion_cap"],"changed_thresholds":{"min_channel_reorder_score_for_stage3":12,"proxy_cap_stage_label":"Stage2-Watch"},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"017810|271560|103840|011150","avg_MFE_90D_pct":24.95,"avg_MAE_90D_pct":-19.12,"avg_MFE_180D_pct":26.96,"avg_MAE_180D_pct":-20.98,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable_mixed","avg_four_b_local_peak_proximity":0.869,"avg_four_b_full_window_peak_proximity":0.869,"score_return_alignment_verdict":"canonical rule candidate improves score-return alignment"}
{"row_type":"profile_aggregate","round":"R5","loop":"74","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_id":"P3_counterexample_guard_profile","profile_scope":"counterexample_guard","profile_hypothesis":"If evidence is only price/volume + K-food theme/ingredient proxy, keep as watch/4B overlay regardless of early MFE.","changed_axes":["theme_proxy_false_positive_guard","price_only_4b_watch"],"changed_thresholds":{"full_4b_requires_non_price_evidence":"kept","price_only_blowoff_blocks_positive_stage":"strengthened"},"eligible_trigger_count":2,"selected_entry_trigger_per_case":"103840|011150","avg_MFE_90D_pct":109.59,"avg_MAE_90D_pct":-18.82,"avg_MFE_180D_pct":109.59,"avg_MAE_180D_pct":-40.15,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":0.889,"avg_four_b_full_window_peak_proximity":0.889,"score_return_alignment_verdict":"guard catches high-MAE roundtrip proxies"}
```

### 25.5 shadow_weight rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c18_reorder_quality_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,+3,+3,"Verified repeat sell-through, channel reorder quality, and inventory/margin bridge separated 017810/271560 from K-food theme proxies","Retains two positives while reducing missed structural count; does not relax Green globally","R5L74_C18_017810_STAGE2A_20240517_US_EXPORT_MARGIN|R5L74_C18_271560_STAGE2A_20240517_GLOBAL_REORDER_LOW_MAE",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c18_theme_proxy_positive_stage_cap,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,none,Stage2-Watch,cap,"Smallcap K-food or ingredient/export proxy without company-specific reorder conversion produced large MFE but severe MAE/drawdown","Blocks 103840 and 011150 from positive promotion while preserving 4B watch information","R5L74_C18_103840_STAGE2_THEME_20240517_KFOOD_PRICE_SPIKE|R5L74_C18_011150_STAGE2_THEME_20240517_SEAWEED_KFOOD_PROXY",4,4,2,medium,canonical_shadow_only,"strengthens existing price-only blowoff and non-price 4B requirements"
```

### 25.6 residual_contribution row
```jsonl
{"row_type":"residual_contribution","round":"R5","loop":"74","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["kfood_theme_proxy_false_positive","ingredient_export_proxy_roundtrip","positive_high_mae_4b_late","slow_low_mae_reorder_missed_structural"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows
```jsonl
{"row_type":"narrative_only","case_id":null,"symbol":null,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","reason":"none; all four representative cases have usable 180D stock-web windows; evidence source URLs are still source_proxy_only before production promotion","price_source":"Songdaiki/stock-web","usage":"research_note"}
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
completed_loop = 74
next_round = R6
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-web manifest checked: `atlas/manifest.json`; max_date `2026-02-20`; tradable row count `14,354,401`; raw/unadjusted marcap basis.
- Stock-web schema checked: `atlas/schema.json`; MFE/MAE definitions use max high / min low over tradable rows.
- Symbol profiles checked: `017/017810`, `271/271560`, `103/103840`, `011/011150`.
- Price shards checked: `017/017810/2024.csv`, `271/271560/2024.csv`, `271/271560/2025.csv`, `103/103840/2024.csv`, `011/011150/2024.csv`.
- Evidence claims are research-proxy-only; production promotion must attach DART/IR/news URLs.

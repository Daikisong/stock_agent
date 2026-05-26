# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R13
loop = 44
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = ODM_GLOBAL_BRAND_REORDER_MARGIN_BRIDGE / BRAND_CHANNEL_REORDER_INVENTORY_MARGIN_GUARD / CHINA_APPAREL_CHANNEL_REORDER_INVENTORY_GUARD
loop_objective = holdout_validation | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | residual_false_positive_mining | coverage_gap_fill
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
```

This file is historical calibration research only. It is not a current-stock scan, not a stock recommendation, and not a coding patch.

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

The purpose here is not to re-prove the existing global axes. The residual question is narrower: **within C18, when does a consumer export channel narrative become real reorder evidence, and when is it just a price spike wearing a channel costume?**

## 2. Round / Large Sector / Canonical Archetype Scope

- large_sector_id: `L5_CONSUMER_BRAND_DISTRIBUTION`
- canonical_archetype_id: `C18_CONSUMER_EXPORT_CHANNEL_REORDER`
- primary theme: consumer export channel reorder, especially beauty ODM/brand and apparel China-channel paths.
- case set:
  - positive structural: 코스맥스, 한국콜마
  - counterexample / failed rerating: 클리오, F&F
  - overlay: price-only local 4B and late 4C watch rows

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifact check was limited to `stock_agent` calibration artifacts. The available `md_registry.jsonl` was readable, and repository search for this loop’s four symbols in the existing calibration artifacts returned no direct hits for `192820` or `161890`; this loop therefore treats all four representative cases as new independent evidence.

```text
required_new_independent_case_ratio = 0.60
calibration_usable_case_count = 4
new_independent_case_count = 4
new_independent_case_ratio = 1.00
loop_contribution_label = canonical_archetype_rule_candidate
```

## 4. Stock-Web OHLC Input / Price Source Validation

The Stock-Web manifest was read directly from `Songdaiki/stock-web` before computing forward windows.

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
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

The schema confirms the calibration columns as `d,o,h,l,c,v,a,mc,s,m`, and defines MFE/MAE on tradable raw rows. The atlas caveat is material: these are **raw/unadjusted marcap OHLC rows**, so corporate-action windows are blocked.

## 5. Historical Eligibility Gate

All representative triggers pass the 180-trading-day gate.

| symbol | company | profile_path | profile last_date | corporate_action_candidate_dates | 180D status |
|---|---:|---|---|---|---|
| 192820 | 코스맥스 | atlas/symbol_profiles/192/192820.json | 2026-02-20 | [] | clean |
| 161890 | 한국콜마 | atlas/symbol_profiles/161/161890.json | 2026-02-20 | [] | clean |
| 237880 | 클리오 | atlas/symbol_profiles/237/237880.json | 2026-02-20 | [] | clean |
| 383220 | F&F | atlas/symbol_profiles/383/383220.json | 2026-02-20 | 2022-04-13 only | clean for 2024 trigger windows |

## 6. Canonical Archetype Compression Map

C18 is compressed into three fine routes for this loop:

| fine_archetype_id | canonical_archetype_id | mechanism |
|---|---|---|
| ODM_GLOBAL_BRAND_REORDER_MARGIN_BRIDGE | C18_CONSUMER_EXPORT_CHANNEL_REORDER | customer reorder + utilization + margin bridge |
| BRAND_CHANNEL_REORDER_INVENTORY_MARGIN_GUARD | C18_CONSUMER_EXPORT_CHANNEL_REORDER | brand/export channel narrative must pass inventory/sell-through guard |
| CHINA_APPAREL_CHANNEL_REORDER_INVENTORY_GUARD | C18_CONSUMER_EXPORT_CHANNEL_REORDER | China channel rebound without inventory normalization is a false-positive risk |

## 7. Case Selection Summary

| case_id | symbol | company_name | role | best_trigger | entry | MFE90 | MAE90 | MFE180 | MAE180 | current_profile | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C18-R13L44-192820-COSMAX | 192820 | 코스맥스 | positive | C18-R13L44-192820-T1-stage2 | 2024-05-14 | 29.60 | -27.73 | 29.60 | -27.73 | current_profile_too_late | ODM형 C18에서는 sell-through/reorder + margin bridge가 같이 보일 때 Stage2가 Green보다 정보효율이 좋음. |
| C18-R13L44-161890-KOLMAR | 161890 | 한국콜마 | positive | C18-R13L44-161890-T1-stage2 | 2024-05-31 | 22.40 | -17.57 | 22.40 | -22.94 | current_profile_too_late | 재주문과 가동률/마진 bridge가 함께 있을 때 구조적이나, Green은 upside를 일부 소진. |
| C18-R13L44-237880-CLIO | 237880 | 클리오 | counterexample | C18-R13L44-237880-T1-stage2 | 2024-05-24 | 12.22 | -26.93 | 12.22 | -60.62 | current_profile_false_positive | 가격 강도만으로 채널 재주문을 인정하면 180D MAE가 과도해짐. |
| C18-R13L44-383220-FNF | 383220 | F&F | counterexample | C18-R13L44-383220-T1-stage2 | 2024-07-17 | 3.24 | -36.28 | 3.24 | -36.28 | current_profile_false_positive | 중국 채널 기대/이벤트성 spike는 sell-through·재고 정상화 없이 positive stage 승격 금지. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 2
4C_case_count = 2
minimum_calibration_usable_case_count = 4
```

The split is deliberately balanced. The two positive cases show that C18 can work when channel reorder is tied to margin bridge and customer quality. The two counterexamples show why channel narrative alone is dangerous: the stock can move first, but without inventory normalization and sell-through evidence the path becomes a trapdoor.

## 9. Evidence Source Map

| case | Stage2 evidence | Stage3 evidence | 4B / 4C evidence |
|---|---|---|---|
| 코스맥스 | global customer order quality, ODM delivery visibility, early revision | confirmed margin bridge and multiple public sources | local valuation/positioning watch, not full 4B |
| 한국콜마 | ODM customer mix, reorder route, utilization, early revision | confirmed revision and financial visibility | 2024 local 4B was too early versus 2025 full-window peak |
| 클리오 | channel expectation and relative strength | missing: margin bridge, sell-through, durable customer proof | later thesis break; hard 4C late |
| F&F | China channel rebound narrative and price spike | missing: sell-through, inventory normalization, durable margin bridge | price-only local spike; thesis-break watch |

## 10. Price Data Source Map

| symbol | price_shard_2024 | price_shard_2025 | profile |
|---|---|---|---|
| 192820 | atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv | atlas/ohlcv_tradable_by_symbol_year/192/192820/2025.csv | atlas/symbol_profiles/192/192820.json |
| 161890 | atlas/ohlcv_tradable_by_symbol_year/161/161890/2024.csv | atlas/ohlcv_tradable_by_symbol_year/161/161890/2025.csv | atlas/symbol_profiles/161/161890.json |
| 237880 | atlas/ohlcv_tradable_by_symbol_year/237/237880/2024.csv | atlas/ohlcv_tradable_by_symbol_year/237/237880/2025.csv | atlas/symbol_profiles/237/237880.json |
| 383220 | atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv | atlas/ohlcv_tradable_by_symbol_year/383/383220/2025.csv | atlas/symbol_profiles/383/383220.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | trigger_outcome_label | current_profile_verdict | aggregate_group_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C18-R13L44-192820-T1-stage2 | 192820 | Stage2-Actionable | 2024-05-14 | 160500 | 29.60 | -27.73 | 29.60 | -27.73 | structural_success_high_mae | current_profile_too_late | representative |
| C18-R13L44-161890-T1-stage2 | 161890 | Stage2-Actionable | 2024-05-31 | 64300 | 22.40 | -17.57 | 22.40 | -22.94 | structural_success_high_mae | current_profile_too_late | representative |
| C18-R13L44-237880-T1-stage2 | 237880 | Stage2-Actionable | 2024-05-24 | 40100 | 12.22 | -26.93 | 12.22 | -60.62 | failed_rerating_4c_late | current_profile_false_positive | representative |
| C18-R13L44-383220-T1-stage2 | 383220 | Stage2-Actionable | 2024-07-17 | 74000 | 3.24 | -36.28 | 3.24 | -36.28 | false_positive_green_or_stage2 | current_profile_false_positive | representative |
| C18-R13L44-192820-T2-green | 192820 | Stage3-Green | 2024-06-13 | 184100 | 12.98 | -36.99 | 12.98 | -36.99 | late_green_high_mae | current_profile_too_late | label_comparison_only |
| C18-R13L44-192820-T3-4b | 192820 | Stage4B-Watch | 2024-06-14 | 184900 | 12.49 | -37.26 | 12.49 | -37.26 | 4B_overlay_watch | current_profile_4B_too_early | 4B_overlay_only |
| C18-R13L44-161890-T2-green | 161890 | Stage3-Green | 2024-09-10 | 76200 | 3.28 | -34.97 | 15.49 | -34.97 | late_green_but_still_profitable | current_profile_too_late | label_comparison_only |
| C18-R13L44-161890-T3-4b | 161890 | Stage4B-Watch | 2024-09-30 | 74400 | 5.78 | -33.40 | 18.28 | -33.40 | price_only_local_4B_too_early | current_profile_4B_too_early | 4B_overlay_only |
| C18-R13L44-237880-T2-green-fp | 237880 | Stage3-Yellow/Green-FP | 2024-06-12 | 43150 | 4.29 | -32.10 | 4.29 | -63.41 | false_positive_green | current_profile_false_positive | label_comparison_only |
| C18-R13L44-237880-T3-4c | 237880 | Stage4C | 2024-11-11 | 18070 | 13.17 | -12.62 | 26.45 | -15.22 | 4C_late | current_profile_4C_too_late | 4C_overlay_only |
| C18-R13L44-383220-T2-4c | 383220 | Stage4C-Watch | 2024-08-05 | 48000 | 50.21 | -1.77 | 55.83 | -1.77 | thesis_break_watch_only | current_profile_4C_too_late | 4C_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | peak_date | drawdown_after_peak_pct | current_profile_verdict | aggregate_group_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C18-R13L44-192820-T1-stage2 | 192820 | Stage2-Actionable | 2024-05-14 | 160500 | 29.60 | 29.60 | 29.60 | -3.86 | -27.73 | -27.73 | 2024-06-14 | -44.23 | current_profile_too_late | representative |
| C18-R13L44-161890-T1-stage2 | 161890 | Stage2-Actionable | 2024-05-31 | 64300 | 16.64 | 22.40 | 22.40 | -6.84 | -17.57 | -22.94 | 2024-09-30 | -37.04 | current_profile_too_late | representative |
| C18-R13L44-237880-T1-stage2 | 237880 | Stage2-Actionable | 2024-05-24 | 40100 | 12.22 | 12.22 | 12.22 | -11.47 | -26.93 | -60.62 | 2024-06-13 | -65.96 | current_profile_false_positive | representative |
| C18-R13L44-383220-T1-stage2 | 383220 | Stage2-Actionable | 2024-07-17 | 74000 | 3.24 | 3.24 | 3.24 | -36.28 | -36.28 | -36.28 | 2024-07-17 | -38.29 | current_profile_false_positive | representative |
| C18-R13L44-192820-T2-green | 192820 | Stage3-Green | 2024-06-13 | 184100 | 12.98 | 12.98 | 12.98 | -20.10 | -36.99 | -36.99 | 2024-06-14 | -44.23 | current_profile_too_late | label_comparison_only |
| C18-R13L44-192820-T3-4b | 192820 | Stage4B-Watch | 2024-06-14 | 184900 | 12.49 | 12.49 | 12.49 | -20.44 | -37.26 | -37.26 | 2024-06-14 | -44.23 | current_profile_4B_too_early | 4B_overlay_only |
| C18-R13L44-161890-T2-green | 161890 | Stage3-Green | 2024-09-10 | 76200 | 3.28 | 3.28 | 15.49 | -11.55 | -34.97 | -34.97 | 2025-05-09 | -43.69 | current_profile_too_late | label_comparison_only |
| C18-R13L44-161890-T3-4b | 161890 | Stage4B-Watch | 2024-09-30 | 74400 | 5.78 | 5.78 | 18.28 | -11.96 | -33.40 | -33.40 | 2025-05-09 | -43.69 | current_profile_4B_too_early | 4B_overlay_only |
| C18-R13L44-237880-T2-green-fp | 237880 | Stage3-Yellow/Green-FP | 2024-06-12 | 43150 | 4.29 | 4.29 | 4.29 | -17.73 | -32.10 | -63.41 | 2024-06-13 | -65.96 | current_profile_false_positive | label_comparison_only |
| C18-R13L44-237880-T3-4c | 237880 | Stage4C | 2024-11-11 | 18070 | 5.04 | 13.17 | 26.45 | -12.62 | -12.62 | -15.22 | 2025-03-14 | -32.95 | current_profile_4C_too_late | 4C_overlay_only |
| C18-R13L44-383220-T2-4c | 383220 | Stage4C-Watch | 2024-08-05 | 48000 | 23.33 | 50.21 | 55.83 | -1.77 | -1.77 | -1.77 | 2025-02-20 | -36.97 | current_profile_4C_too_late | 4C_overlay_only |

Representative aggregate:

```text
representative_trigger_count = 4
avg_MFE_90D_pct = 16.87
avg_MAE_90D_pct = -27.13
avg_MFE_180D_pct = 16.87
avg_MAE_180D_pct = -36.89
positive_rep_avg_MFE_90D_pct = 26.00
positive_rep_avg_MAE_90D_pct = -22.65
counterexample_rep_avg_MFE_90D_pct = 7.73
counterexample_rep_avg_MAE_90D_pct = -31.61
```

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual path | verdict |
|---|---|---|---|
| 코스맥스 | waits for stronger confirmed revision / Green | Stage2 had +29.60% 90D MFE but also high MAE after peak | current_profile_too_late |
| 한국콜마 | waits for confirmed revision / Green | Stage2 had +22.40% 90D MFE; Green arrived later and more volatile | current_profile_too_late |
| 클리오 | may allow Stage2/Y if channel narrative + RS dominates | 180D MAE -60.62%; thesis broke | current_profile_false_positive |
| F&F | may allow Stage2/Y on price spike + channel hope | 90D/180D MFE only +3.24%, MAE -36.28% | current_profile_false_positive |

Answers to the required stress-test questions:

1. The current profile would generally keep 코스맥스/한국콜마 safer but later; this preserves precision but misses early C18 reorder entry quality.
2. The positive cases had strong MFE, but high MAE after the first peak means C18 requires a separate 4B/hold discipline.
3. Stage2 bonus is useful only when reorder is tied to sell-through or margin bridge. It is too permissive for pure channel narrative.
4. Yellow 75 is acceptable globally, but C18 should penalize inventory/margin absence before Yellow.
5. Green 87 / revision 55 is too late for ODM reorder cases if customer quality and margin bridge are already visible.
6. price-only blowoff guard is appropriate and should be kept.
7. full 4B non-price requirement is appropriate; 한국콜마 shows price-only local 4B can be too early.
8. hard 4C routing can be too late in brand/channel failures; a C18 thesis-break watch layer is needed before hard 4C.

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Green/late trigger | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| 코스맥스 | 160,500 | 184,100 | 0.50 | Green captures only mid-cycle confirmation; Stage2 reorder signal was earlier. |
| 한국콜마 | 64,300 | 76,200 | 0.50 | Green was not unusable, but half of the confirmed upside to 2025 full-window peak had already been consumed. |
| 클리오 | 40,100 | 43,150 | 0.62 | Late positive label would be near local peak and becomes false-positive. |
| F&F | 74,000 | none | not_applicable | No confirmed Green should be allowed without sell-through/inventory bridge. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---:|---:|---|
| C18-R13L44-192820-T3-4b | 0.51 | 0.44 | local 4B watch, not full 4B |
| C18-R13L44-161890-T3-4b | 0.70 | 0.43 | price-only local 4B too early |
| C18-R13L44-383220-T1-stage2 | n/a | n/a | price-only local spike cannot promote positive stage |

The 한국콜마 row is the cleanest residual: a price-only local peak in 2024 looked like 4B, but the full observed peak arrived later in 2025. In C18, 4B needs non-price evidence such as inventory overhang, margin slowdown, channel saturation, or explicit sell-through deceleration.

## 16. 4C Protection Audit

| case | 4C trigger | label | protection interpretation |
|---|---|---|---|
| 클리오 | 2024-11-11 | hard_4c_late | The peak-to-low drawdown had already unfolded; hard 4C protected only from later residual downside. |
| F&F | 2024-08-05 | thesis_break_watch_only | The collapse warned that channel thesis was unstable, but later rebound means watch-layer is safer than hard 4C. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L5_price_only_channel_spike_4B_watch
proposal = Do not let price-only consumer-channel spikes promote Stage2/3 or full 4B without reorder/sell-through/inventory evidence.
delta = -2 shadow-only guard
confidence = low_to_medium
```

Mechanism: consumer channel narratives are like a shop window. A crowded window can look like demand, but the cash register is the real evidence. C18 should reward the register: reorder, sell-through, customer-quality, and margin bridge.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
new_axis_proposed:
  - C18_sell_through_repeat_order_bonus: +3
  - C18_inventory_margin_absence_guard: -4
```

Positive promotion requires at least two of:

```text
customer_or_order_quality
repeat_order_or_conversion
sell_through_score
margin_bridge_score
financial_visibility
```

Counterexample guard activates if two of these are true:

```text
inventory_risk_score < 0
margin_bridge_score <= 0
sell_through_score <= 1
price spike or valuation repricing without confirmed revision
```

## 19. Before / After Backtest Comparison

| profile_id | scope | selected representatives | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | global current | 4 | 16.87 | -27.13 | 16.87 | -36.89 | 0.50 | correct global guards, but C18 residual FPs remain |
| P0b e2r_2_0_baseline_reference | rollback | 4 | 16.87 | -27.13 | 16.87 | -36.89 | 0.50+ | too permissive on channel narrative |
| P1 sector_specific_candidate_profile | L5 | 3 | 18.75 | -23.63 | 18.75 | -28.98 | 0.33 | improves by blocking price-only channel spike |
| P2 canonical_archetype_candidate_profile | C18 | 2 | 26.00 | -22.65 | 26.00 | -25.34 | 0.00 | best score-return alignment |
| P3 counterexample_guard_profile | C18 guard | 2 blocked | 7.73 | -31.61 | 7.73 | -48.45 | blocked | guard explains failures |

## 20. Score-Return Alignment Matrix

| case | score before | score after | stage before | stage after | realized alignment |
|---|---:|---:|---|---|---|
| 코스맥스 | 110.0 | 119.0 | Stage3-Green | Stage3-Green | positive structural, but needs MAE-aware hold discipline |
| 한국콜마 | 104.0 | 112.0 | Stage3-Green | Stage3-Green | positive structural, volatile path |
| 클리오 | 25.0 | 12.0 | No Positive Stage | Stage4C/Reject | blocked false-positive |
| F&F | 6.0 | -4.0 | Stage4C/Reject | Stage4C/Reject | blocked false-positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L5_CONSUMER_BRAND_DISTRIBUTION | C18_CONSUMER_EXPORT_CHANNEL_REORDER | ODM_GLOBAL_BRAND_REORDER_MARGIN_BRIDGE / BRAND_CHANNEL_REORDER_INVENTORY_MARGIN_GUARD / CHINA_APPAREL_CHANNEL_REORDER_INVENTORY_GUARD | 2 | 2 | 2 | 2 | 4 | 0 | 11 | 4 | 4 | true | true | C18 now has positive ODM reorder coverage and brand/channel false-positive guards; still needs C18 holdout in non-beauty consumer export. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - C18_channel_narrative_without_sellthrough_false_positive
  - Green_late_after_reorder_confirmed
  - price_only_local_4B_too_early
  - hard_4C_late_after_inventory_margin_break
new_axis_proposed:
  - C18_sell_through_repeat_order_bonus
  - C18_inventory_margin_absence_guard
  - L5_price_only_channel_spike_4B_watch
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- actual Songdaiki/stock-web tradable_raw OHLC rows
- trigger-level entry_date and entry_price
- MFE/MAE 30D/90D/180D
- clean 180D corporate-action windows
- current calibrated proxy stress test
- same_entry_group_id / aggregate dedupe
```

Not validated:

```text
- live 2026 candidate scan
- broker/API execution
- production scoring code
- exact analyst consensus database values
- intraday disclosure timestamps where unavailable
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C18_sell_through_repeat_order_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,+3,+3,"C18 positive cases required channel reorder plus sell-through/margin bridge; channel narrative alone failed","positive representatives MFE90 avg 26.00 vs counterexample MFE90 avg 7.73","C18-R13L44-192820-T1-stage2|C18-R13L44-161890-T1-stage2",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C18_inventory_margin_absence_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,-4,-4,"counterexamples showed inventory/margin absence dominated price-only channel narrative","counterexample representatives MAE180 avg -48.45","C18-R13L44-237880-T1-stage2|C18-R13L44-383220-T1-stage2",4,4,2,medium,canonical_shadow_only,"guard for brand/distribution cases"
shadow_weight,L5_price_only_channel_spike_4B_watch,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,-2,-2,"price-only local spikes often reversed or later whipsawed; require non-price 4B evidence for full exit overlay","F&F spike MFE90 3.24 / MAE90 -36.28; Kolmar price-only local 4B too early", "C18-R13L44-383220-T1-stage2|C18-R13L44-161890-T3-4b",4,4,2,low,sector_shadow_only,"do not promote global delta"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "C18-R13L44-192820-COSMAX", "symbol": "192820", "company_name": "코스맥스", "round": "R13", "loop": "44", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER_SUBSET", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "C18-R13L44-192820-T1-stage2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_but_high_mae_after_late_green", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "ODM형 C18에서는 sell-through/reorder + margin bridge가 같이 보일 때 Stage2가 Green보다 정보효율이 좋음."}
{"row_type": "case", "case_id": "C18-R13L44-161890-KOLMAR", "symbol": "161890", "company_name": "한국콜마", "round": "R13", "loop": "44", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER_SUBSET", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "C18-R13L44-161890-T1-stage2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_but_path_volatile", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "재주문과 가동률/마진 bridge가 함께 있을 때 구조적이나, Green은 upside를 일부 소진."}
{"row_type": "case", "case_id": "C18-R13L44-237880-CLIO", "symbol": "237880", "company_name": "클리오", "round": "R13", "loop": "44", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER_SUBSET", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "C18-R13L44-237880-T1-stage2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "channel_narrative_without_inventory_margin_bridge_failed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "가격 강도만으로 채널 재주문을 인정하면 180D MAE가 과도해짐."}
{"row_type": "case", "case_id": "C18-R13L44-383220-FNF", "symbol": "383220", "company_name": "F&F", "round": "R13", "loop": "44", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER_SUBSET", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "C18-R13L44-383220-T1-stage2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "china_channel_rebound_without_inventory_sellthrough_failed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "중국 채널 기대/이벤트성 spike는 sell-through·재고 정상화 없이 positive stage 승격 금지."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "C18-R13L44-192820-T1-stage2", "case_id": "C18-R13L44-192820-COSMAX", "symbol": "192820", "company_name": "코스맥스", "round": "R13", "loop": "44", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "ODM_GLOBAL_BRAND_REORDER_MARGIN_BRIDGE", "sector": "화장품 ODM / 글로벌 브랜드 재주문", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "holdout_validation|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-14", "evidence_available_at_that_date": "1Q24 실적 확인 이후 글로벌/미국 고객사 주문 증가와 ODM 마진 개선이 동시에 보인 채널 재주문형 trigger.", "evidence_source": "public quarterly earnings / sell-side report cluster around 2024-05-13~14; price row: atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "backlog_or_delivery_visibility", "early_revision_signal"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv", "profile_path": "atlas/symbol_profiles/192/192820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-14", "entry_price": 160500, "MFE_30D_pct": 29.6, "MFE_90D_pct": 29.6, "MFE_180D_pct": 29.6, "MFE_1Y_pct": 34.89, "MFE_2Y_pct": null, "MAE_30D_pct": -3.86, "MAE_90D_pct": -27.73, "MAE_180D_pct": -27.73, "MAE_1Y_pct": -27.73, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-14", "peak_price": 208000, "drawdown_after_peak_pct": -44.23, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_high_mae", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C18-R13L44-192820-20240514", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C18-R13L44-161890-T1-stage2", "case_id": "C18-R13L44-161890-KOLMAR", "symbol": "161890", "company_name": "한국콜마", "round": "R13", "loop": "44", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "ODM_GLOBAL_BRAND_REORDER_MARGIN_BRIDGE", "sector": "화장품 ODM / 글로벌 브랜드 재주문", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "holdout_validation|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-31", "evidence_available_at_that_date": "5월 말 실적·리포트 흐름에서 글로벌 고객사 재주문, 수출 고객 믹스, 국내외 ODM 가동률 개선이 동시에 확인된 trigger.", "evidence_source": "public earnings/report cluster around 2024-05-30~31; price row: atlas/ohlcv_tradable_by_symbol_year/161/161890/2024.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/161/161890/2024.csv", "profile_path": "atlas/symbol_profiles/161/161890.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-31", "entry_price": 64300, "MFE_30D_pct": 16.64, "MFE_90D_pct": 22.4, "MFE_180D_pct": 22.4, "MFE_1Y_pct": 36.86, "MFE_2Y_pct": null, "MAE_30D_pct": -6.84, "MAE_90D_pct": -17.57, "MAE_180D_pct": -22.94, "MAE_1Y_pct": -22.94, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-09-30", "peak_price": 78700, "drawdown_after_peak_pct": -37.04, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_high_mae", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C18-R13L44-161890-20240531", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C18-R13L44-237880-T1-stage2", "case_id": "C18-R13L44-237880-CLIO", "symbol": "237880", "company_name": "클리오", "round": "R13", "loop": "44", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "BRAND_CHANNEL_REORDER_INVENTORY_MARGIN_GUARD", "sector": "색조 브랜드 / 채널 재주문·재고", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "holdout_validation|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-24", "evidence_available_at_that_date": "일본·미국·온라인 채널 기대가 가격에 반영됐지만, 재주문 지속성과 재고/마진 bridge가 충분히 확인되지 않은 채널 기대형 trigger.", "evidence_source": "public channel/reorder narrative around 2024-05; price row: atlas/ohlcv_tradable_by_symbol_year/237/237880/2024.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "customer_or_order_quality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/237/237880/2024.csv", "profile_path": "atlas/symbol_profiles/237/237880.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-24", "entry_price": 40100, "MFE_30D_pct": 12.22, "MFE_90D_pct": 12.22, "MFE_180D_pct": 12.22, "MFE_1Y_pct": 12.22, "MFE_2Y_pct": null, "MAE_30D_pct": -11.47, "MAE_90D_pct": -26.93, "MAE_180D_pct": -60.62, "MAE_1Y_pct": -61.8, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-13", "peak_price": 45000, "drawdown_after_peak_pct": -65.96, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "failed_rerating_4c_late", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C18-R13L44-237880-20240524", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C18-R13L44-383220-T1-stage2", "case_id": "C18-R13L44-383220-FNF", "symbol": "383220", "company_name": "F&F", "round": "R13", "loop": "44", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "CHINA_APPAREL_CHANNEL_REORDER_INVENTORY_GUARD", "sector": "의류 브랜드 / 중국 채널 재고", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "holdout_validation|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-17", "evidence_available_at_that_date": "중국 채널 반등 기대와 단기 이벤트성 거래대금이 붙었지만, 재주문 sell-through·재고 정상화·마진 bridge가 부족했던 false-positive trigger.", "evidence_source": "public channel rebound / corporate action-like narrative around 2024-07-17; price row: atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv", "profile_path": "atlas/symbol_profiles/383/383220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-17", "entry_price": 74000, "MFE_30D_pct": 3.24, "MFE_90D_pct": 3.24, "MFE_180D_pct": 3.24, "MFE_1Y_pct": 3.24, "MFE_2Y_pct": null, "MAE_30D_pct": -36.28, "MAE_90D_pct": -36.28, "MAE_180D_pct": -36.28, "MAE_1Y_pct": -36.28, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-17", "peak_price": 76400, "drawdown_after_peak_pct": -38.29, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "false_positive_green_or_stage2", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C18-R13L44-383220-20240717", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C18-R13L44-192820-T2-green", "case_id": "C18-R13L44-192820-COSMAX", "symbol": "192820", "company_name": "코스맥스", "round": "R13", "loop": "44", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "ODM_GLOBAL_BRAND_REORDER_MARGIN_BRIDGE", "sector": "화장품 ODM / 글로벌 브랜드 재주문", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "holdout_validation|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage3-Green", "trigger_date": "2024-06-13", "evidence_available_at_that_date": "글로벌 고객사 주문·마진 bridge가 확인됐지만, Stage2 대비 진입가가 이미 상승한 Green trigger.", "evidence_source": "public earnings/revision cluster; price row: atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv", "stage2_evidence_fields": ["customer_or_order_quality", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv", "profile_path": "atlas/symbol_profiles/192/192820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-13", "entry_price": 184100, "MFE_30D_pct": 12.98, "MFE_90D_pct": 12.98, "MFE_180D_pct": 12.98, "MFE_1Y_pct": 17.6, "MFE_2Y_pct": null, "MAE_30D_pct": -20.1, "MAE_90D_pct": -36.99, "MAE_180D_pct": -36.99, "MAE_1Y_pct": -36.99, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-14", "peak_price": 208000, "drawdown_after_peak_pct": -44.23, "green_lateness_ratio": 0.5, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_green_high_mae", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C18-R13L44-192820-20240613", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C18-R13L44-192820-T3-4b", "case_id": "C18-R13L44-192820-COSMAX", "symbol": "192820", "company_name": "코스맥스", "round": "R13", "loop": "44", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "ODM_GLOBAL_BRAND_REORDER_MARGIN_BRIDGE", "sector": "화장품 ODM / 글로벌 브랜드 재주문", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "holdout_validation|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4B-Watch", "trigger_date": "2024-06-14", "evidence_available_at_that_date": "단기 valuation/positioning 과열은 관찰됐으나 full-cycle peak와는 거리가 있어 full 4B라기보다 local watch.", "evidence_source": "price/valuation overlay; price row: atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv", "profile_path": "atlas/symbol_profiles/192/192820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-14", "entry_price": 184900, "MFE_30D_pct": 12.49, "MFE_90D_pct": 12.49, "MFE_180D_pct": 12.49, "MFE_1Y_pct": 17.09, "MFE_2Y_pct": null, "MAE_30D_pct": -20.44, "MAE_90D_pct": -37.26, "MAE_180D_pct": -37.26, "MAE_1Y_pct": -37.26, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-14", "peak_price": 208000, "drawdown_after_peak_pct": -44.23, "green_lateness_ratio": null, "four_b_local_peak_proximity": 0.51, "four_b_full_window_peak_proximity": 0.44, "four_b_timing_verdict": "local_4B_watch_not_full_4B", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_overlay_watch", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C18-R13L44-192820-20240614", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C18-R13L44-161890-T2-green", "case_id": "C18-R13L44-161890-KOLMAR", "symbol": "161890", "company_name": "한국콜마", "round": "R13", "loop": "44", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "ODM_GLOBAL_BRAND_REORDER_MARGIN_BRIDGE", "sector": "화장품 ODM / 글로벌 브랜드 재주문", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "holdout_validation|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage3-Green", "trigger_date": "2024-09-10", "evidence_available_at_that_date": "누적 revision·주가 강도가 확인된 Green trigger지만 Stage2 대비 upside 일부를 소진.", "evidence_source": "public revision/relative-strength cluster; price row: atlas/ohlcv_tradable_by_symbol_year/161/161890/2024.csv", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/161/161890/2024.csv", "profile_path": "atlas/symbol_profiles/161/161890.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-09-10", "entry_price": 76200, "MFE_30D_pct": 3.28, "MFE_90D_pct": 3.28, "MFE_180D_pct": 15.49, "MFE_1Y_pct": 15.49, "MFE_2Y_pct": null, "MAE_30D_pct": -11.55, "MAE_90D_pct": -34.97, "MAE_180D_pct": -34.97, "MAE_1Y_pct": -34.97, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-05-09", "peak_price": 88000, "drawdown_after_peak_pct": -43.69, "green_lateness_ratio": 0.5, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_green_but_still_profitable", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C18-R13L44-161890-20240910", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C18-R13L44-161890-T3-4b", "case_id": "C18-R13L44-161890-KOLMAR", "symbol": "161890", "company_name": "한국콜마", "round": "R13", "loop": "44", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "ODM_GLOBAL_BRAND_REORDER_MARGIN_BRIDGE", "sector": "화장품 ODM / 글로벌 브랜드 재주문", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "holdout_validation|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4B-Watch", "trigger_date": "2024-09-30", "evidence_available_at_that_date": "2024년 9월 local peak 부근 과열이 보였지만 2025년 full-window peak가 더 높아 price-only local 4B는 이른 편.", "evidence_source": "price-only local peak overlay; price row: atlas/ohlcv_tradable_by_symbol_year/161/161890/2024.csv", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/161/161890/2024.csv", "profile_path": "atlas/symbol_profiles/161/161890.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-09-30", "entry_price": 74400, "MFE_30D_pct": 5.78, "MFE_90D_pct": 5.78, "MFE_180D_pct": 18.28, "MFE_1Y_pct": 18.28, "MFE_2Y_pct": null, "MAE_30D_pct": -11.96, "MAE_90D_pct": -33.4, "MAE_180D_pct": -33.4, "MAE_1Y_pct": -33.4, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-05-09", "peak_price": 88000, "drawdown_after_peak_pct": -43.69, "green_lateness_ratio": null, "four_b_local_peak_proximity": 0.7, "four_b_full_window_peak_proximity": 0.43, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "price_only_local_4B_too_early", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C18-R13L44-161890-20240930", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C18-R13L44-237880-T2-green-fp", "case_id": "C18-R13L44-237880-CLIO", "symbol": "237880", "company_name": "클리오", "round": "R13", "loop": "44", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "BRAND_CHANNEL_REORDER_INVENTORY_MARGIN_GUARD", "sector": "색조 브랜드 / 채널 재주문·재고", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "holdout_validation|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage3-Yellow/Green-FP", "trigger_date": "2024-06-12", "evidence_available_at_that_date": "가격 강도와 채널 기대는 있었지만 재고·마진·sell-through bridge가 없는 상태에서 Green으로 올리면 late false-positive가 됨.", "evidence_source": "price row and narrative-only channel expectation; price row: atlas/ohlcv_tradable_by_symbol_year/237/237880/2024.csv", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/237/237880/2024.csv", "profile_path": "atlas/symbol_profiles/237/237880.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-12", "entry_price": 43150, "MFE_30D_pct": 4.29, "MFE_90D_pct": 4.29, "MFE_180D_pct": 4.29, "MFE_1Y_pct": 4.29, "MFE_2Y_pct": null, "MAE_30D_pct": -17.73, "MAE_90D_pct": -32.1, "MAE_180D_pct": -63.41, "MAE_1Y_pct": -64.5, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-13", "peak_price": 45000, "drawdown_after_peak_pct": -65.96, "green_lateness_ratio": 0.62, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "false_positive_green", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C18-R13L44-237880-20240612", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C18-R13L44-237880-T3-4c", "case_id": "C18-R13L44-237880-CLIO", "symbol": "237880", "company_name": "클리오", "round": "R13", "loop": "44", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "BRAND_CHANNEL_REORDER_INVENTORY_MARGIN_GUARD", "sector": "색조 브랜드 / 채널 재주문·재고", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "holdout_validation|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4C", "trigger_date": "2024-11-11", "evidence_available_at_that_date": "재주문 thesis가 무너진 뒤 hard 4C가 잡히는 지점. 이미 peak 대비 하락 폭이 커 방어는 late지만 추가 하락을 일부 제한.", "evidence_source": "hard thesis break / price row: atlas/ohlcv_tradable_by_symbol_year/237/237880/2024.csv and 2025.csv", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken", "forced_liquidation_or_crash"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/237/237880/2024.csv", "profile_path": "atlas/symbol_profiles/237/237880.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-11-11", "entry_price": 18070, "MFE_30D_pct": 5.04, "MFE_90D_pct": 13.17, "MFE_180D_pct": 26.45, "MFE_1Y_pct": 26.45, "MFE_2Y_pct": null, "MAE_30D_pct": -12.62, "MAE_90D_pct": -12.62, "MAE_180D_pct": -15.22, "MAE_1Y_pct": -15.22, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-03-14", "peak_price": 22850, "drawdown_after_peak_pct": -32.95, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "4C_late", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C18-R13L44-237880-20241111", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C18-R13L44-383220-T2-4c", "case_id": "C18-R13L44-383220-FNF", "symbol": "383220", "company_name": "F&F", "round": "R13", "loop": "44", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "CHINA_APPAREL_CHANNEL_REORDER_INVENTORY_GUARD", "sector": "의류 브랜드 / 중국 채널 재고", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "holdout_validation|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4C-Watch", "trigger_date": "2024-08-05", "evidence_available_at_that_date": "단기 collapse는 thesis-break watch로 볼 수 있으나 이후 반등도 발생해 hard 4C보다는 channel-inventory watch로 처리하는 것이 안전.", "evidence_source": "price row: atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv and 2025.csv", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv", "profile_path": "atlas/symbol_profiles/383/383220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-08-05", "entry_price": 48000, "MFE_30D_pct": 23.33, "MFE_90D_pct": 50.21, "MFE_180D_pct": 55.83, "MFE_1Y_pct": 55.83, "MFE_2Y_pct": null, "MAE_30D_pct": -1.77, "MAE_90D_pct": -1.77, "MAE_180D_pct": -1.77, "MAE_1Y_pct": -1.77, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-20", "peak_price": 74800, "drawdown_after_peak_pct": -36.97, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "thesis_break_watch_only", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C18-R13L44-383220-20240805", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C18-R13L44-192820-COSMAX", "trigger_id": "C18-R13L44-192820-T1-stage2", "symbol": "192820", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 6, "margin_bridge_score": 15, "revision_score": 13, "relative_strength_score": 9, "customer_quality_score": 15, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 13, "inventory_risk_score": -2, "sell_through_score": 7, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 110.0, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 6, "margin_bridge_score": 17, "revision_score": 13, "relative_strength_score": 9, "customer_quality_score": 15, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 16, "inventory_risk_score": -2, "sell_through_score": 11, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 119.0, "stage_label_after": "Stage3-Green", "changed_components": ["channel_reorder_score", "sell_through_score", "inventory_risk_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C18에서는 channel reorder alone이 아니라 sell-through + repeat-order + margin bridge 동시 충족을 가점하고, 재고/마진 미확인은 감점.", "MFE_90D_pct": 29.6, "MAE_90D_pct": -27.73, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C18-R13L44-161890-KOLMAR", "trigger_id": "C18-R13L44-161890-T1-stage2", "symbol": "161890", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 5, "margin_bridge_score": 14, "revision_score": 12, "relative_strength_score": 8, "customer_quality_score": 14, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 12, "inventory_risk_score": -2, "sell_through_score": 8, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 104.0, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 5, "margin_bridge_score": 16, "revision_score": 12, "relative_strength_score": 8, "customer_quality_score": 14, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 15, "inventory_risk_score": -2, "sell_through_score": 11, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 112.0, "stage_label_after": "Stage3-Green", "changed_components": ["channel_reorder_score", "sell_through_score", "inventory_risk_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C18에서는 channel reorder alone이 아니라 sell-through + repeat-order + margin bridge 동시 충족을 가점하고, 재고/마진 미확인은 감점.", "MFE_90D_pct": 22.4, "MAE_90D_pct": -17.57, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C18-R13L44-237880-CLIO", "trigger_id": "C18-R13L44-237880-T1-stage2", "symbol": "237880", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 8, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 6, "inventory_risk_score": -13, "sell_through_score": 1, "positioning_overheat_score": -6, "thesis_break_score": 0}, "weighted_score_before": 25.0, "stage_label_before": "No Positive Stage", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 8, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": -12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 2, "inventory_risk_score": -18, "sell_through_score": 1, "positioning_overheat_score": -6, "thesis_break_score": 0}, "weighted_score_after": 12.0, "stage_label_after": "Stage4C/Reject", "changed_components": ["channel_reorder_score", "sell_through_score", "inventory_risk_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C18에서는 channel reorder alone이 아니라 sell-through + repeat-order + margin bridge 동시 충족을 가점하고, 재고/마진 미확인은 감점.", "MFE_90D_pct": 12.22, "MAE_90D_pct": -26.93, "score_return_alignment_label": "false_positive_blocked_by_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C18-R13L44-383220-FNF", "trigger_id": "C18-R13L44-383220-T1-stage2", "symbol": "383220", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": -2, "revision_score": 0, "relative_strength_score": 7, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": -9, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 3, "inventory_risk_score": -18, "sell_through_score": 0, "positioning_overheat_score": -7, "thesis_break_score": 0}, "weighted_score_before": 6.0, "stage_label_before": "Stage4C/Reject", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": -2, "revision_score": 0, "relative_strength_score": 7, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": -12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 0, "inventory_risk_score": -22, "sell_through_score": 0, "positioning_overheat_score": -7, "thesis_break_score": 0}, "weighted_score_after": -4.0, "stage_label_after": "Stage4C/Reject", "changed_components": ["channel_reorder_score", "sell_through_score", "inventory_risk_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C18에서는 channel reorder alone이 아니라 sell-through + repeat-order + margin bridge 동시 충족을 가점하고, 재고/마진 미확인은 감점.", "MFE_90D_pct": 3.24, "MAE_90D_pct": -36.28, "score_return_alignment_label": "false_positive_blocked_by_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C18-R13L44-192820-COSMAX", "trigger_id": "C18-R13L44-192820-T2-green", "symbol": "192820", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 6, "margin_bridge_score": 15, "revision_score": 13, "relative_strength_score": 9, "customer_quality_score": 15, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 13, "inventory_risk_score": -2, "sell_through_score": 7, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 110.0, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 6, "margin_bridge_score": 17, "revision_score": 13, "relative_strength_score": 9, "customer_quality_score": 15, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 16, "inventory_risk_score": -2, "sell_through_score": 11, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 119.0, "stage_label_after": "Stage3-Green", "changed_components": ["channel_reorder_score", "sell_through_score", "inventory_risk_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C18에서는 channel reorder alone이 아니라 sell-through + repeat-order + margin bridge 동시 충족을 가점하고, 재고/마진 미확인은 감점.", "MFE_90D_pct": 12.98, "MAE_90D_pct": -36.99, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C18-R13L44-192820-COSMAX", "trigger_id": "C18-R13L44-192820-T3-4b", "symbol": "192820", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 6, "margin_bridge_score": 15, "revision_score": 13, "relative_strength_score": 9, "customer_quality_score": 15, "policy_or_regulatory_score": 0, "valuation_repricing_score": 11, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 13, "inventory_risk_score": -2, "sell_through_score": 7, "positioning_overheat_score": -7, "thesis_break_score": 0}, "weighted_score_before": 106.0, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 6, "margin_bridge_score": 17, "revision_score": 13, "relative_strength_score": 9, "customer_quality_score": 15, "policy_or_regulatory_score": 0, "valuation_repricing_score": 11, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 16, "inventory_risk_score": -2, "sell_through_score": 11, "positioning_overheat_score": -7, "thesis_break_score": 0}, "weighted_score_after": 115.0, "stage_label_after": "Stage3-Green", "changed_components": ["channel_reorder_score", "sell_through_score", "inventory_risk_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C18에서는 channel reorder alone이 아니라 sell-through + repeat-order + margin bridge 동시 충족을 가점하고, 재고/마진 미확인은 감점.", "MFE_90D_pct": 12.49, "MAE_90D_pct": -37.26, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_4B_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C18-R13L44-161890-KOLMAR", "trigger_id": "C18-R13L44-161890-T2-green", "symbol": "161890", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 5, "margin_bridge_score": 14, "revision_score": 12, "relative_strength_score": 8, "customer_quality_score": 14, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 12, "inventory_risk_score": -2, "sell_through_score": 8, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 104.0, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 5, "margin_bridge_score": 16, "revision_score": 12, "relative_strength_score": 8, "customer_quality_score": 14, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 15, "inventory_risk_score": -2, "sell_through_score": 11, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 112.0, "stage_label_after": "Stage3-Green", "changed_components": ["channel_reorder_score", "sell_through_score", "inventory_risk_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C18에서는 channel reorder alone이 아니라 sell-through + repeat-order + margin bridge 동시 충족을 가점하고, 재고/마진 미확인은 감점.", "MFE_90D_pct": 3.28, "MAE_90D_pct": -34.97, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C18-R13L44-161890-KOLMAR", "trigger_id": "C18-R13L44-161890-T3-4b", "symbol": "161890", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 5, "margin_bridge_score": 14, "revision_score": 12, "relative_strength_score": 8, "customer_quality_score": 14, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 12, "inventory_risk_score": -2, "sell_through_score": 8, "positioning_overheat_score": -7, "thesis_break_score": 0}, "weighted_score_before": 100.0, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 5, "margin_bridge_score": 16, "revision_score": 12, "relative_strength_score": 8, "customer_quality_score": 14, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 15, "inventory_risk_score": -2, "sell_through_score": 11, "positioning_overheat_score": -7, "thesis_break_score": 0}, "weighted_score_after": 108.0, "stage_label_after": "Stage3-Green", "changed_components": ["channel_reorder_score", "sell_through_score", "inventory_risk_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C18에서는 channel reorder alone이 아니라 sell-through + repeat-order + margin bridge 동시 충족을 가점하고, 재고/마진 미확인은 감점.", "MFE_90D_pct": 5.78, "MAE_90D_pct": -33.4, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_4B_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C18-R13L44-237880-CLIO", "trigger_id": "C18-R13L44-237880-T2-green-fp", "symbol": "237880", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 8, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 6, "inventory_risk_score": -13, "sell_through_score": 1, "positioning_overheat_score": -6, "thesis_break_score": 0}, "weighted_score_before": 25.0, "stage_label_before": "No Positive Stage", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 8, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": -12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 2, "inventory_risk_score": -18, "sell_through_score": 1, "positioning_overheat_score": -6, "thesis_break_score": 0}, "weighted_score_after": 12.0, "stage_label_after": "Stage4C/Reject", "changed_components": ["channel_reorder_score", "sell_through_score", "inventory_risk_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C18에서는 channel reorder alone이 아니라 sell-through + repeat-order + margin bridge 동시 충족을 가점하고, 재고/마진 미확인은 감점.", "MFE_90D_pct": 4.29, "MAE_90D_pct": -32.1, "score_return_alignment_label": "false_positive_blocked_by_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C18-R13L44-237880-CLIO", "trigger_id": "C18-R13L44-237880-T3-4c", "symbol": "237880", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 8, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": -13, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 6, "inventory_risk_score": -13, "sell_through_score": 1, "positioning_overheat_score": -6, "thesis_break_score": -20}, "weighted_score_before": 0.0, "stage_label_before": "Stage4C/Reject", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 8, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": -17, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 2, "inventory_risk_score": -18, "sell_through_score": 1, "positioning_overheat_score": -6, "thesis_break_score": -20}, "weighted_score_after": -13.0, "stage_label_after": "Stage4C/Reject", "changed_components": ["channel_reorder_score", "sell_through_score", "inventory_risk_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C18에서는 channel reorder alone이 아니라 sell-through + repeat-order + margin bridge 동시 충족을 가점하고, 재고/마진 미확인은 감점.", "MFE_90D_pct": 13.17, "MAE_90D_pct": -12.62, "score_return_alignment_label": "false_positive_blocked_by_guard", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C18-R13L44-383220-FNF", "trigger_id": "C18-R13L44-383220-T2-4c", "symbol": "383220", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": -2, "revision_score": 0, "relative_strength_score": 7, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": -14, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 3, "inventory_risk_score": -18, "sell_through_score": 0, "positioning_overheat_score": -7, "thesis_break_score": -20}, "weighted_score_before": -19.0, "stage_label_before": "Stage4C/Reject", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": -2, "revision_score": 0, "relative_strength_score": 7, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": -17, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 0, "inventory_risk_score": -22, "sell_through_score": 0, "positioning_overheat_score": -7, "thesis_break_score": -20}, "weighted_score_after": -29.0, "stage_label_after": "Stage4C/Reject", "changed_components": ["channel_reorder_score", "sell_through_score", "inventory_risk_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C18에서는 channel reorder alone이 아니라 sell-through + repeat-order + margin bridge 동시 충족을 가점하고, 재고/마진 미확인은 감점.", "MFE_90D_pct": 50.21, "MAE_90D_pct": -1.77, "score_return_alignment_label": "false_positive_blocked_by_guard", "current_profile_verdict": "current_profile_4C_too_late"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C18_sell_through_repeat_order_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,+3,+3,"C18 positive cases required channel reorder plus sell-through/margin bridge; channel narrative alone failed","positive representatives MFE90 avg 26.00 vs counterexample MFE90 avg 7.73","C18-R13L44-192820-T1-stage2|C18-R13L44-161890-T1-stage2",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C18_inventory_margin_absence_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,-4,-4,"counterexamples showed inventory/margin absence dominated price-only channel narrative","counterexample representatives MAE180 avg -48.45","C18-R13L44-237880-T1-stage2|C18-R13L44-383220-T1-stage2",4,4,2,medium,canonical_shadow_only,"guard for brand/distribution cases"
shadow_weight,L5_price_only_channel_spike_4B_watch,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,-2,-2,"price-only local spikes often reversed or later whipsawed; require non-price 4B evidence for full exit overlay","F&F spike MFE90 3.24 / MAE90 -36.28; Kolmar price-only local 4B too early", "C18-R13L44-383220-T1-stage2|C18-R13L44-161890-T3-4b",4,4,2,low,sector_shadow_only,"do not promote global delta"
```

### 25.6 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R13", "loop": "44", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 5, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["C18_channel_narrative_without_sellthrough_false_positive", "Green_late_after_reorder_confirmed", "price_only_local_4B_too_early", "hard_4C_late_after_inventory_margin_break"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":null,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","reason":"all selected cases have clean 180D forward windows; no narrative-only case used for weight calibration","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
next_round = R13_loop_45
suggested_large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
suggested_canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
reason = C18 now separates reorder success from channel-narrative false positives; C19 should isolate inventory/margin mechanics directly.
```

## 28. Source Notes

- Stock-Web manifest: `atlas/manifest.json`, max_date `2026-02-20`.
- Stock-Web schema: `atlas/schema.json`, MFE/MAE formulas and tradable_raw caveats.
- Profile files checked:
  - `atlas/symbol_profiles/192/192820.json`
  - `atlas/symbol_profiles/161/161890.json`
  - `atlas/symbol_profiles/237/237880.json`
  - `atlas/symbol_profiles/383/383220.json`
- OHLC shard files checked:
  - `atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/192/192820/2025.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/161/161890/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/161/161890/2025.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/237/237880/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/237/237880/2025.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/383/383220/2025.csv`

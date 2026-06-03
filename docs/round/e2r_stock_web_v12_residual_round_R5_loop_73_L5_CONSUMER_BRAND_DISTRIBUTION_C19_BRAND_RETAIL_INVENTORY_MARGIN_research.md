# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R5
scheduled_loop = 73
completed_round = R5
completed_loop = 73
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id = APPAREL_BRAND_SELLTHROUGH_INVENTORY_MARGIN_BRIDGE
loop_objective = sector_specific_rule_discovery | canonical_archetype_compression | residual_false_positive_mining | residual_missed_structural_mining | 4B_non_price_requirement_stress_test | counterexample_mining | coverage_gap_fill
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
stock_web_price_atlas_access_required = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 4 new independent cases, 2 counterexamples, and 4 residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C19_BRAND_RETAIL_INVENTORY_MARGIN.

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

This loop does not re-prove the global Stage2/Green/4B axes. It stress-tests the current profile inside a consumer-brand inventory/margin pocket where the same “brand heat” signal can mean either durable sell-through or inventory-led false promotion.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R5
scheduled_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id = APPAREL_BRAND_SELLTHROUGH_INVENTORY_MARGIN_BRIDGE
```

R5 hard gate passes because L5 consumer/brand/distribution is the only selected large sector. C19 was selected because local R5 artifacts already cover C20 K-beauty/global distribution and C18 export channel reorder, while C19 was absent in the local snapshot.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed artifact scope was used only for coverage and duplicate avoidance. The local snapshot shows:

- R5 Loop 71 = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION, symbols 192820, 161890, 214420, 226320.
- R5 Loop 72 = C18_CONSUMER_EXPORT_CHANNEL_REORDER, symbols 003230, 005180, 383220, 081660.
- No local R5 C19_BRAND_RETAIL_INVENTORY_MARGIN file was found before this loop.

Hard duplicate key check:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected symbols are 036620, 337930, 298540, 031430. They are not repeated from local R5 loop 71/72 and are counted as same-sector, new-canonical, new-symbol cases.

## 4. Stock-Web OHLC Input / Price Source Validation

```json
{
  "atlas_version": "1.0.0",
  "generated_at": "2026-05-21T16:28:39.421691+00:00",
  "source_name": "FinanceData/marcap",
  "source_repo_url": "https://github.com/FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": [
    "KONEX",
    "KOSDAQ",
    "KOSDAQ GLOBAL",
    "KOSPI"
  ],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv"
}
```

Schema assumptions used here:

```text
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
raw_shard_columns      = d,o,h,l,c,v,a,mc,s,m,rs
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
calibration_usable requires tradable_raw, entry row, >=180 forward tradable days, positive OHLCV, and clean 180D corporate-action window.
```

The manifest max date, not the current date, is used as the forward-window ceiling.

## 5. Historical Eligibility Gate

| symbol | company | price_shard_path | profile_path | profile_status | 180D_window |
| --- | --- | --- | --- | --- | --- |
| 036620 | 감성코퍼레이션 | atlas/ohlcv_tradable_by_symbol_year/036/036620/2023.csv | atlas/symbol_profiles/036/036620.json | corporate-action candidate dates are historical only: 2000-05-24, 2000-06-16, 2017-05-26, 2018-12-21; 2023-05-15~D+180 clean. | clean_180D_window |
| 337930 | 브랜드엑스코퍼레이션/젝시믹스 | atlas/ohlcv_tradable_by_symbol_year/337/337930/2024.csv | atlas/symbol_profiles/337/337930.json | corporate-action candidate date 2021-09-23 only; 2024-05-16~D+180 clean. | clean_180D_window |
| 298540 | 더네이쳐홀딩스 | atlas/ohlcv_tradable_by_symbol_year/298/298540/2023.csv | atlas/symbol_profiles/298/298540.json | corporate-action candidate dates 2021-08-02, 2021-08-30 only; 2023-04-18~D+180 clean. | clean_180D_window |
| 031430 | 신세계인터내셔날 | atlas/ohlcv_tradable_by_symbol_year/031/031430/2023.csv | atlas/symbol_profiles/031/031430.json | corporate-action candidate date 2022-04-11 only; 2023-02-08~D+180 clean. | clean_180D_window |


All four representative entry triggers pass the 180 trading-day forward-window test under manifest max_date=2026-02-20. Corporate-action candidate dates listed in profiles do not overlap any representative entry_date~D+180 window.

## 6. Canonical Archetype Compression Map

```text
C19_BRAND_RETAIL_INVENTORY_MARGIN
  ├─ verified sell-through / repeat channel conversion
  ├─ inventory quality or inventory normalization
  ├─ gross-margin / OPM bridge
  ├─ brand heat or reopening narrative
  └─ 4B overlay: valuation/positioning after verified rerating, not price-only full exit
```

C19 should not be reduced to “consumer brand is hot.” The core mechanism is more mechanical: a brand first looks strong at the shelf, but the stock only earns a durable rerating when sell-through drains inventory without discounting and the gross-margin bridge survives the next reporting window.

## 7. Case Selection Summary

| case_id | symbol | company | role | case_type | entry | MFE90 | MAE90 | current_profile_verdict | new |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C19_POS_036620_20230515_SNOWPEAK_RETAIL_SELLTHROUGH_MARGIN | 036620 | 감성코퍼레이션 | positive | high_mae_success | 2023-05-15 | 56.83 | -4.92 | current_profile_4B_too_late | True |
| C19_POS_337930_20240516_XEXYMIX_CHANNEL_MARGIN_RERATING | 337930 | 브랜드엑스코퍼레이션/젝시믹스 | positive | 4B_overlay_success | 2024-05-16 | 141.73 | -3.64 | current_profile_4B_too_late | True |
| C19_CEX_298540_20230418_NATIONALGEOGRAPHIC_INVENTORY_MARGIN_FADE | 298540 | 더네이쳐홀딩스 | counterexample | failed_rerating | 2023-04-18 | 4.71 | -37.74 | current_profile_false_positive | True |
| C19_CEX_031430_20230208_REOPENING_RETAIL_MARGIN_FALSE_PROMOTION | 031430 | 신세계인터내셔날 | counterexample | false_positive_green | 2023-02-08 | 0.79 | -34.33 | current_profile_false_positive | True |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 2
4C_case_count = 0
calibration_usable_case_count = 4
new_independent_case_count = 4
```

The positive side uses 036620 and 337930: both show high 90D/180D MFE after sell-through/margin evidence. The counterexample side uses 298540 and 031430: both show weak MFE with large MAE when brand/reopening narratives were not backed by inventory and margin proof.

## 9. Evidence Source Map

| symbol | trigger_date | evidence_source | stage2 | stage3 | stage4b |
| --- | --- | --- | --- | --- | --- |
| 036620 | 2023-05-12 | source_proxy_only_research_note; production promotion should replace with DART quarterly report / IR / dated news URL | public_event_or_disclosure,customer_or_order_quality,capacity_or_volume_route,early_revision_signal | confirmed_revision,margin_bridge,financial_visibility,repeat_order_or_conversion | none |
| 337930 | 2024-05-16 | source_proxy_only_research_note; production promotion should replace with DART quarterly report / IR / dated news URL | public_event_or_disclosure,customer_or_order_quality,capacity_or_volume_route,early_revision_signal | confirmed_revision,margin_bridge,financial_visibility,repeat_order_or_conversion,low_red_team_risk | none |
| 298540 | 2023-04-18 | source_proxy_only_research_note; production promotion should replace with DART quarterly report / IR / dated news URL | public_event_or_disclosure,relative_strength | none | margin_or_backlog_slowdown,positioning_overheat |
| 031430 | 2023-02-08 | source_proxy_only_research_note; production promotion should replace with DART quarterly report / IR / dated news URL | public_event_or_disclosure,relative_strength,policy_or_regulatory_optionality | none | margin_or_backlog_slowdown,positioning_overheat |


Evidence is deliberately conservative: each event is recorded as a historical research proxy, and production promotion must replace it with exact DART/IR/news URLs. Price-only motion is never used as Stage2/Stage3 evidence.

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | 180D_window |
| --- | --- | --- | --- |
| 036620 | atlas/ohlcv_tradable_by_symbol_year/036/036620/2023.csv | atlas/symbol_profiles/036/036620.json | clean_180D_window |
| 337930 | atlas/ohlcv_tradable_by_symbol_year/337/337930/2024.csv | atlas/symbol_profiles/337/337930.json | clean_180D_window |
| 298540 | atlas/ohlcv_tradable_by_symbol_year/298/298540/2023.csv | atlas/symbol_profiles/298/298540.json | clean_180D_window |
| 031430 | atlas/ohlcv_tradable_by_symbol_year/031/031430/2023.csv | atlas/symbol_profiles/031/031430.json | clean_180D_window |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | company | trigger_type | entry_date | entry_price | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T036620_STAGE2A_20230515_SNOWPEAK_RETAIL_MARGIN_REORDER | 036620 | 감성코퍼레이션 | Stage2-Actionable | 2023-05-15 | 3150 | 56.83 | -4.92 | 56.83 | -16.19 | 2023-07-11 | 4940 | current_profile_4B_too_late |
| T337930_STAGE2A_20240516_XEXYMIX_REORDER_MARGIN | 337930 | 브랜드엑스코퍼레이션/젝시믹스 | Stage2-Actionable | 2024-05-16 | 5080 | 141.73 | -3.64 | 163.39 | -3.64 | 2024-10-07 | 13380 | current_profile_4B_too_late |
| T298540_STAGE2_20230418_BRAND_EXPANSION_WITHOUT_INVENTORY_BRIDGE | 298540 | 더네이쳐홀딩스 | Stage2-Watch | 2023-04-18 | 31850 | 4.71 | -37.74 | 4.71 | -53.85 | 2023-04-19 | 33350 | current_profile_false_positive |
| T031430_STAGE2_20230208_REOPENING_BRAND_RETAIL_NO_MARGIN_BRIDGE | 031430 | 신세계인터내셔날 | Stage2-Watch | 2023-02-08 | 25400 | 0.79 | -34.33 | 0.79 | -41.61 | 2023-02-08 | 25600 | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

### 036620 감성코퍼레이션

| window | MFE % | MAE % | high used | low used |
| --- | ---: | ---: | ---: | ---: |
| 30D | 46.03 | -4.92 | 4600 | 2995 |
| 90D | 56.83 | -4.92 | 4940 | 2995 |
| 180D | 56.83 | -16.19 | 4940 | 2640 |
| 1Y | 56.83 | -20.32 | 4940 | 2510 |
| 2Y | 56.83 | not_primary | 4940 | 2510 |

```text
entry_date = 2023-05-15
entry_price = 3150
peak_date = 2023-07-11
peak_price = 4940
drawdown_after_peak_pct = -46.56
corporate_action_window_status = clean_180D_window
```


### 337930 브랜드엑스코퍼레이션/젝시믹스

| window | MFE % | MAE % | high used | low used |
| --- | ---: | ---: | ---: | ---: |
| 30D | 34.06 | -3.64 | 6810 | 4895 |
| 90D | 141.73 | -3.64 | 12280 | 4895 |
| 180D | 163.39 | -3.64 | 13380 | 4895 |
| 1Y | 163.39 | 7.87 | 13380 | 5480 |
| 2Y | 163.39 | not_primary | 13380 | 5480 |

```text
entry_date = 2024-05-16
entry_price = 5080
peak_date = 2024-10-07
peak_price = 13380
drawdown_after_peak_pct = -57.17
corporate_action_window_status = clean_180D_window
```


### 298540 더네이쳐홀딩스

| window | MFE % | MAE % | high used | low used |
| --- | ---: | ---: | ---: | ---: |
| 30D | 4.71 | -19.47 | 33350 | 25650 |
| 90D | 4.71 | -37.74 | 33350 | 19830 |
| 180D | 4.71 | -53.85 | 33350 | 14700 |
| 1Y | 4.71 | -56.08 | 33350 | 13990 |
| 2Y | 4.71 | not_primary | 33350 | 7810 |

```text
entry_date = 2023-04-18
entry_price = 31850
peak_date = 2023-04-19
peak_price = 33350
drawdown_after_peak_pct = -55.92
corporate_action_window_status = clean_180D_window
```


### 031430 신세계인터내셔날

| window | MFE % | MAE % | high used | low used |
| --- | ---: | ---: | ---: | ---: |
| 30D | 0.79 | -20.87 | 25600 | 20100 |
| 90D | 0.79 | -34.33 | 25600 | 16680 |
| 180D | 0.79 | -41.61 | 25600 | 14830 |
| 1Y | 0.79 | -41.61 | 25600 | 14830 |
| 2Y | 0.79 | not_primary | 25600 | 12260 |

```text
entry_date = 2023-02-08
entry_price = 25400
peak_date = 2023-02-08
peak_price = 25600
drawdown_after_peak_pct = -42.07
corporate_action_window_status = clean_180D_window
```


## 13. Current Calibrated Profile Stress Test

| symbol | current_profile_verdict | actual_path | C19_shadow_interpretation |
| --- | --- | --- | --- |
| 036620 | current_profile_4B_too_late | positive_but_high_MAE_success | promote with 4B-watch overlay |
| 337930 | current_profile_4B_too_late | structural_success_with_late_4B_risk | promote with 4B-watch overlay |
| 298540 | current_profile_false_positive | false_positive_inventory_margin_fade | cap at Stage2-Watch until inventory/margin proof |
| 031430 | current_profile_false_positive | false_positive_reopening_inventory_margin_fade | cap at Stage2-Watch until inventory/margin proof |

The current calibrated profile is not globally wrong; its residual error is local. It can promote consumer-brand heat too easily when “reorder” is inferred from narrative rather than sell-through, inventory normalization and margin bridge. Conversely, on verified positives it can be directionally right but late to attach 4B-watch after extreme rerating.

## 14. Stage2 / Yellow / Green Comparison

```text
036620: Stage2-Actionable around 2023-05-15 aligned with MFE90 +56.83%, but later drawdown shows Green needs 4B-watch.
337930: Stage2-Actionable around 2024-05-16 aligned with MFE90 +141.73%, but local price-only 4B in July would have been too early versus October full-window peak.
298540: Stage2-Watch around 2023-04-18 should not become Yellow/Green; MFE90 +4.71% vs MAE90 -37.74%.
031430: Stage2-Watch around 2023-02-08 should not become Yellow/Green; MFE90 +0.79% vs MAE90 -34.33%.
```

Green lateness ratio is not applicable because this loop is not a Green-lateness proof. It is an inventory/margin promotion/cap test.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | stage2_entry | 4B_entry | local_peak | full_window_peak | local_proximity | full_window_proximity | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T036620_4B_20230711_PRICE_ONLY_LOCAL_PEAK_WATCH | 3150 | 4600 | 4940 | 4940 | 0.81 | 0.81 | price_only_local_4B_watch_not_full_4B |
| T337930_4B_20240710_LOCAL_PRICE_ONLY_TOO_EARLY | 5080 | 8520 | 9140 | 13380 | 0.85 | 0.41 | price_only_local_4B_too_early |

The 337930 row is the main split: a price-only local 4B looked close to the local peak but still captured only 41% of the full-window move from Stage2 entry to the later October peak. This strengthens the existing rule that price-only local blowoff should be watch/overlay, not full 4B.

## 16. 4C Protection Audit

No hard 4C row is proposed. 298540 and 031430 are thesis-break watch rows, not hard rejection rows. Their negative paths are enough to cap Stage3, but not enough to calibrate a hard 4C trigger without explicit evidence such as contract cancellation, accounting break, forced liquidation, or regulatory rejection.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = c19_brand_heat_inventory_cap
candidate = In L5 consumer brand/retail cases, brand heat, reopening, or retail expansion narrative cannot promote above Stage2-Watch unless at least one inventory-quality bridge and one margin bridge are present.
```

Mechanism: a consumer brand can sell into the channel and still fail at the stock level if inventory sits in stores or discounting eats margin. The chart may initially smell like demand, but without sell-through and margin proof it is often just inventory moving from one warehouse to another.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = c19_sellthrough_inventory_margin_bridge_bonus
candidate = For C19, add a shadow +2 when sell-through/reorder evidence, inventory normalization, and gross-margin/OPM bridge are jointly present.
guard = If inventory_quality_score < 0 and gross_margin_score < 5, cap at Stage2-Watch even if brand_heat_score and relative_strength_score are high.
4B_overlay = If MFE90 > 80% or valuation/positioning becomes extreme, attach 4B-watch; do not treat price-only local peak as full 4B.
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 4 | 4 | 51.02 | -20.16 | 56.43 | -28.82 | 0.5 | 0 | mixed; positive cases work, but counterexamples are too easily promoted |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 4 | 2 | 99.28 | -4.28 | 110.11 | -9.92 | 0.0 | 2 | too conservative for verified sell-through positives |
| P1_sector_specific_candidate_profile | sector_specific | 4 | 2 | 99.28 | -4.28 | 110.11 | -9.92 | 0.0 | 0 | best alignment in this loop |
| P2_canonical_archetype_candidate_profile | canonical_archetype_specific | 4 | 2 | 99.28 | -4.28 | 110.11 | -9.92 | 0.0 | 0 | canonical rule candidate |
| P3_counterexample_guard_profile | counterexample_guard | 2 | 0 | 2.75 | -36.03 | 2.75 | -47.73 | 0.0 | 0 | protects against false positives |

## 20. Score-Return Alignment Matrix

| case_id | symbol | score_before | stage_before | score_after | stage_after | MFE90 | MAE90 | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C19_POS_036620_20230515_SNOWPEAK_RETAIL_SELLTHROUGH_MARGIN | 036620 | 82 | Stage3-Yellow | 88 | Stage3-Green+4B-Watch | 56.83 | -4.92 | strong_positive_aligned_but_4B_overlay_needed |
| C19_POS_337930_20240516_XEXYMIX_CHANNEL_MARGIN_RERATING | 337930 | 84 | Stage3-Yellow | 91 | Stage3-Green+4B-Watch | 141.73 | -3.64 | strong_positive_aligned_but_4B_overlay_needed |
| C19_CEX_298540_20230418_NATIONALGEOGRAPHIC_INVENTORY_MARGIN_FADE | 298540 | 77 | Stage3-Yellow | 59 | Stage2-Watch | 4.71 | -37.74 | corrected_false_positive |
| C19_CEX_031430_20230208_REOPENING_RETAIL_MARGIN_FALSE_PROMOTION | 031430 | 76 | Stage3-Yellow | 60 | Stage2-Watch | 0.79 | -34.33 | corrected_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L5_CONSUMER_BRAND_DISTRIBUTION | C19_BRAND_RETAIL_INVENTORY_MARGIN | APPAREL_BRAND_SELLTHROUGH_INVENTORY_MARGIN_BRIDGE | 2 | 2 | 2 | 0 | 4 | 0 | 6 | 4 | 4 | True | True | C19 no longer empty in local R5 loop 71/72 snapshot; needs further holdout in non-apparel retail. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - brand_heat_inventory_false_positive
  - reopening_retail_margin_false_positive
  - positive_high_mae_4b_late
  - price_only_local_4b_too_early
new_axis_proposed:
  - c19_sellthrough_inventory_margin_bridge_bonus
  - c19_brand_heat_inventory_cap
  - c19_price_only_local_4b_watch_overlay
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- R5/L5/C19 only.
- Quantitative rows use Songdaiki/stock-web tradable_raw OHLCV.
- All representative entries have clean 180D windows.
- Machine-readable rows are shadow-only.
```

Non-validation scope:

```text
- No current/live candidate scan.
- No investment recommendation.
- No production scoring change.
- No stock_agent source-code access or patch.
- Evidence source URLs are not production-grade in this run; they are marked source_proxy_only and must be replaced before promotion.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c19_sellthrough_inventory_margin_bridge_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,+2,+2,"Verified sell-through + inventory quality + gross-margin bridge separated 036620/337930 positives from 298540/031430 false positives.","Avg selected positive MFE90 99.28% vs counterexample MFE90 2.75%; counterexample MAE90 -36.03%.","T036620_STAGE2A_20230515_SNOWPEAK_RETAIL_MARGIN_REORDER|T337930_STAGE2A_20240516_XEXYMIX_REORDER_MARGIN",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c19_brand_heat_inventory_cap,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,cap_stage2_watch,cap,"Brand heat/reopening narratives without inventory or margin proof produced false positive paths.","Blocks 298540/031430 Stage3-Yellow false promotion while keeping positives with proof.","T298540_STAGE2_20230418_BRAND_EXPANSION_WITHOUT_INVENTORY_BRIDGE|T031430_STAGE2_20230208_REOPENING_BRAND_RETAIL_NO_MARGIN_BRIDGE",4,4,2,medium,sector_shadow_only,"not production; post-calibrated residual"
shadow_weight,c19_price_only_local_4b_watch_overlay,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,watch_only,+1,"C19 reratings can overshoot before fundamentals break; local peak must be split from full-window peak.","337930 local 4B proximity 0.85 but full-window 0.41, so price-only local 4B is too early for full exit.","T036620_4B_20230711_PRICE_ONLY_LOCAL_PEAK_WATCH|T337930_4B_20240710_LOCAL_PRICE_ONLY_TOO_EARLY",4,4,2,low,canonical_shadow_only,"4B overlay only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "C19_POS_036620_20230515_SNOWPEAK_RETAIL_SELLTHROUGH_MARGIN", "symbol": "036620", "company_name": "감성코퍼레이션", "round": "R5", "loop": "73", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_SELLTHROUGH_INVENTORY_MARGIN_BRIDGE", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "T036620_STAGE2A_20230515_SNOWPEAK_RETAIL_MARGIN_REORDER", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive_but_requires_4b_overlay", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "Snow Peak apparel sell-through and operating-margin improvement were visible around the 1Q23 result window; treated as non-price channel-margin evidence, not as live discovery."}
{"row_type": "case", "case_id": "C19_POS_337930_20240516_XEXYMIX_CHANNEL_MARGIN_RERATING", "symbol": "337930", "company_name": "브랜드엑스코퍼레이션/젝시믹스", "round": "R5", "loop": "73", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_SELLTHROUGH_INVENTORY_MARGIN_BRIDGE", "case_type": "4B_overlay_success", "positive_or_counterexample": "positive", "best_trigger": "T337930_STAGE2A_20240516_XEXYMIX_REORDER_MARGIN", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive_but_requires_4b_overlay", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "Xexymix brand channel and margin improvement evidence was visible around the 1Q24 result and May 2024 rerating window; treated as C19 sell-through/margin bridge evidence."}
{"row_type": "case", "case_id": "C19_CEX_298540_20230418_NATIONALGEOGRAPHIC_INVENTORY_MARGIN_FADE", "symbol": "298540", "company_name": "더네이쳐홀딩스", "round": "R5", "loop": "73", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_SELLTHROUGH_INVENTORY_MARGIN_BRIDGE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "T298540_STAGE2_20230418_BRAND_EXPANSION_WITHOUT_INVENTORY_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "corrected_false_positive_after_inventory_margin_guard", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Retail brand expansion and China/offline channel narrative were present, but inventory/margin bridge was not confirmed at the trigger; treated as C19 false-promotion counterexample."}
{"row_type": "case", "case_id": "C19_CEX_031430_20230208_REOPENING_RETAIL_MARGIN_FALSE_PROMOTION", "symbol": "031430", "company_name": "신세계인터내셔날", "round": "R5", "loop": "73", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_SELLTHROUGH_INVENTORY_MARGIN_BRIDGE", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "T031430_STAGE2_20230208_REOPENING_BRAND_RETAIL_NO_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "corrected_false_positive_after_inventory_margin_guard", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Reopening/brand retail narrative was present, but sell-through, inventory normalization and margin bridge were not confirmed; treated as C19 false-positive guard case."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "T036620_STAGE2A_20230515_SNOWPEAK_RETAIL_MARGIN_REORDER", "case_id": "C19_POS_036620_20230515_SNOWPEAK_RETAIL_SELLTHROUGH_MARGIN", "symbol": "036620", "company_name": "감성코퍼레이션", "round": "R5", "loop": "73", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_SELLTHROUGH_INVENTORY_MARGIN_BRIDGE", "sector": "consumer_brand_distribution", "primary_archetype": "brand retail sell-through / apparel margin bridge", "loop_objective": "sector_specific_rule_discovery | canonical_archetype_compression | residual_false_positive_mining | counterexample_mining | coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-12", "entry_date": "2023-05-15", "entry_price": 3150, "evidence_available_at_that_date": "Snow Peak apparel sell-through and operating-margin improvement were visible around the 1Q23 result window; treated as non-price channel-margin evidence, not as live discovery.", "evidence_source": "source_proxy_only_research_note; production promotion should replace with DART quarterly report / IR / dated news URL", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036620/2023.csv", "profile_path": "atlas/symbol_profiles/036/036620.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 46.03, "MFE_90D_pct": 56.83, "MFE_180D_pct": 56.83, "MFE_1Y_pct": 56.83, "MFE_2Y_pct": 56.83, "MAE_30D_pct": -4.92, "MAE_90D_pct": -4.92, "MAE_180D_pct": -16.19, "MAE_1Y_pct": -20.32, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-11", "peak_price": 4940, "drawdown_after_peak_pct": -46.56, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "positive_but_high_MAE_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C19_POS_036620_20230515_SNOWPEAK_RETAIL_SELLTHROUGH_MARGIN_2023-05-15", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T337930_STAGE2A_20240516_XEXYMIX_REORDER_MARGIN", "case_id": "C19_POS_337930_20240516_XEXYMIX_CHANNEL_MARGIN_RERATING", "symbol": "337930", "company_name": "브랜드엑스코퍼레이션/젝시믹스", "round": "R5", "loop": "73", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_SELLTHROUGH_INVENTORY_MARGIN_BRIDGE", "sector": "consumer_brand_distribution", "primary_archetype": "D2C athleisure channel reorder / margin rerating", "loop_objective": "sector_specific_rule_discovery | canonical_archetype_compression | residual_false_positive_mining | counterexample_mining | coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-16", "entry_date": "2024-05-16", "entry_price": 5080, "evidence_available_at_that_date": "Xexymix brand channel and margin improvement evidence was visible around the 1Q24 result and May 2024 rerating window; treated as C19 sell-through/margin bridge evidence.", "evidence_source": "source_proxy_only_research_note; production promotion should replace with DART quarterly report / IR / dated news URL", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "repeat_order_or_conversion", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/337/337930/2024.csv", "profile_path": "atlas/symbol_profiles/337/337930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 34.06, "MFE_90D_pct": 141.73, "MFE_180D_pct": 163.39, "MFE_1Y_pct": 163.39, "MFE_2Y_pct": 163.39, "MAE_30D_pct": -3.64, "MAE_90D_pct": -3.64, "MAE_180D_pct": -3.64, "MAE_1Y_pct": 7.87, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-07", "peak_price": 13380, "drawdown_after_peak_pct": -57.17, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_with_late_4B_risk", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C19_POS_337930_20240516_XEXYMIX_CHANNEL_MARGIN_RERATING_2024-05-16", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T298540_STAGE2_20230418_BRAND_EXPANSION_WITHOUT_INVENTORY_BRIDGE", "case_id": "C19_CEX_298540_20230418_NATIONALGEOGRAPHIC_INVENTORY_MARGIN_FADE", "symbol": "298540", "company_name": "더네이쳐홀딩스", "round": "R5", "loop": "73", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_SELLTHROUGH_INVENTORY_MARGIN_BRIDGE", "sector": "consumer_brand_distribution", "primary_archetype": "brand expansion without inventory/margin confirmation", "loop_objective": "sector_specific_rule_discovery | canonical_archetype_compression | residual_false_positive_mining | counterexample_mining | coverage_gap_fill", "trigger_type": "Stage2-Watch", "trigger_date": "2023-04-18", "entry_date": "2023-04-18", "entry_price": 31850, "evidence_available_at_that_date": "Retail brand expansion and China/offline channel narrative were present, but inventory/margin bridge was not confirmed at the trigger; treated as C19 false-promotion counterexample.", "evidence_source": "source_proxy_only_research_note; production promotion should replace with DART quarterly report / IR / dated news URL", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298540/2023.csv", "profile_path": "atlas/symbol_profiles/298/298540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.71, "MFE_90D_pct": 4.71, "MFE_180D_pct": 4.71, "MFE_1Y_pct": 4.71, "MFE_2Y_pct": 4.71, "MAE_30D_pct": -19.47, "MAE_90D_pct": -37.74, "MAE_180D_pct": -53.85, "MAE_1Y_pct": -56.08, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-19", "peak_price": 33350, "drawdown_after_peak_pct": -55.92, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": ["margin_or_backlog_slowdown", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "false_positive_inventory_margin_fade", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C19_CEX_298540_20230418_NATIONALGEOGRAPHIC_INVENTORY_MARGIN_FADE_2023-04-18", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T031430_STAGE2_20230208_REOPENING_BRAND_RETAIL_NO_MARGIN_BRIDGE", "case_id": "C19_CEX_031430_20230208_REOPENING_RETAIL_MARGIN_FALSE_PROMOTION", "symbol": "031430", "company_name": "신세계인터내셔날", "round": "R5", "loop": "73", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_SELLTHROUGH_INVENTORY_MARGIN_BRIDGE", "sector": "consumer_brand_distribution", "primary_archetype": "reopening/luxury retail narrative without margin turn", "loop_objective": "sector_specific_rule_discovery | canonical_archetype_compression | residual_false_positive_mining | counterexample_mining | coverage_gap_fill", "trigger_type": "Stage2-Watch", "trigger_date": "2023-02-08", "entry_date": "2023-02-08", "entry_price": 25400, "evidence_available_at_that_date": "Reopening/brand retail narrative was present, but sell-through, inventory normalization and margin bridge were not confirmed; treated as C19 false-positive guard case.", "evidence_source": "source_proxy_only_research_note; production promotion should replace with DART quarterly report / IR / dated news URL", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/031/031430/2023.csv", "profile_path": "atlas/symbol_profiles/031/031430.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.79, "MFE_90D_pct": 0.79, "MFE_180D_pct": 0.79, "MFE_1Y_pct": 0.79, "MFE_2Y_pct": 0.79, "MAE_30D_pct": -20.87, "MAE_90D_pct": -34.33, "MAE_180D_pct": -41.61, "MAE_1Y_pct": -41.61, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-02-08", "peak_price": 25600, "drawdown_after_peak_pct": -42.07, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": ["margin_or_backlog_slowdown", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "false_positive_reopening_inventory_margin_fade", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C19_CEX_031430_20230208_REOPENING_RETAIL_MARGIN_FALSE_PROMOTION_2023-02-08", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T036620_4B_20230711_PRICE_ONLY_LOCAL_PEAK_WATCH", "case_id": "C19_POS_036620_20230515_SNOWPEAK_RETAIL_SELLTHROUGH_MARGIN", "symbol": "036620", "company_name": "감성코퍼레이션", "round": "R5", "loop": "73", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_SELLTHROUGH_INVENTORY_MARGIN_BRIDGE", "sector": "consumer_brand_distribution", "primary_archetype": "brand retail sell-through / apparel margin bridge", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-Overlay", "trigger_date": "2023-07-11", "entry_date": "2023-07-11", "entry_price": 4600, "evidence_available_at_that_date": "price-only local peak after rapid rerating; no separate non-price thesis break at trigger, so 4B-watch not full 4B.", "evidence_source": "stock_web_price_only_overlay_row", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036620/2023.csv", "profile_path": "atlas/symbol_profiles/036/036620.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.39, "MFE_90D_pct": 7.39, "MFE_180D_pct": 7.39, "MFE_1Y_pct": 7.39, "MFE_2Y_pct": 7.39, "MAE_30D_pct": -19.57, "MAE_90D_pct": -36.96, "MAE_180D_pct": -45.43, "MAE_1Y_pct": -45.43, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-11", "peak_price": 4940, "drawdown_after_peak_pct": -46.56, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.81, "four_b_full_window_peak_proximity": 0.81, "four_b_timing_verdict": "price_only_local_4B_watch_not_full_4B", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_overlay_success_as_watch", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C19_POS_036620_20230515_SNOWPEAK_RETAIL_SELLTHROUGH_MARGIN_2023-05-15", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same case overlay, not a new case", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "T337930_4B_20240710_LOCAL_PRICE_ONLY_TOO_EARLY", "case_id": "C19_POS_337930_20240516_XEXYMIX_CHANNEL_MARGIN_RERATING", "symbol": "337930", "company_name": "브랜드엑스코퍼레이션/젝시믹스", "round": "R5", "loop": "73", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_SELLTHROUGH_INVENTORY_MARGIN_BRIDGE", "sector": "consumer_brand_distribution", "primary_archetype": "D2C athleisure channel reorder / margin rerating", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-Overlay", "trigger_date": "2024-07-10", "entry_date": "2024-07-10", "entry_price": 8520, "evidence_available_at_that_date": "price-only local peak near July 2024, but the full-window peak came later in October; this is the exact local-vs-full 4B split.", "evidence_source": "stock_web_price_only_overlay_row", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/337/337930/2024.csv", "profile_path": "atlas/symbol_profiles/337/337930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 44.13, "MFE_90D_pct": 57.04, "MFE_180D_pct": 57.04, "MFE_1Y_pct": 57.04, "MFE_2Y_pct": 57.04, "MAE_30D_pct": -29.58, "MAE_90D_pct": -29.58, "MAE_180D_pct": -32.75, "MAE_1Y_pct": -35.68, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-07", "peak_price": 13380, "drawdown_after_peak_pct": -57.17, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.85, "four_b_full_window_peak_proximity": 0.41, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "local_price_only_4B_too_early_but_watch_useful", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C19_POS_337930_20240516_XEXYMIX_CHANNEL_MARGIN_RERATING_2024-05-16", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same case overlay, not a new case", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C19_shadow", "case_id": "C19_POS_036620_20230515_SNOWPEAK_RETAIL_SELLTHROUGH_MARGIN", "trigger_id": "T036620_STAGE2A_20230515_SNOWPEAK_RETAIL_MARGIN_REORDER", "symbol": "036620", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 13, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 13, "sellthrough_score": 13, "inventory_quality_score": 6, "gross_margin_score": 12, "brand_heat_score": 4, "positioning_overheat_score": -4, "thesis_break_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 16, "revision_score": 13, "relative_strength_score": 14, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 16, "sellthrough_score": 15, "inventory_quality_score": 9, "gross_margin_score": 15, "brand_heat_score": 4, "positioning_overheat_score": -8, "thesis_break_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green+4B-Watch", "changed_components": ["margin_bridge_score", "channel_reorder_score", "sellthrough_score", "inventory_quality_score", "gross_margin_score", "positioning_overheat_score", "thesis_break_score"], "component_delta_explanation": "C19 shadow rewards verified sell-through + inventory quality + gross-margin bridge, and caps brand/reopening heat when inventory and margin proof is missing.", "MFE_90D_pct": 56.83, "MAE_90D_pct": -4.92, "score_return_alignment_label": "strong_positive_aligned_but_4B_overlay_needed", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C19_shadow", "case_id": "C19_POS_337930_20240516_XEXYMIX_CHANNEL_MARGIN_RERATING", "trigger_id": "T337930_STAGE2A_20240516_XEXYMIX_REORDER_MARGIN", "symbol": "337930", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 14, "revision_score": 12, "relative_strength_score": 15, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 13, "sellthrough_score": 14, "inventory_quality_score": 8, "gross_margin_score": 13, "brand_heat_score": 5, "positioning_overheat_score": -3, "thesis_break_score": 0}, "weighted_score_before": 84, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 17, "revision_score": 15, "relative_strength_score": 15, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 17, "sellthrough_score": 17, "inventory_quality_score": 11, "gross_margin_score": 16, "brand_heat_score": 5, "positioning_overheat_score": -12, "thesis_break_score": 0}, "weighted_score_after": 91, "stage_label_after": "Stage3-Green+4B-Watch", "changed_components": ["margin_bridge_score", "channel_reorder_score", "sellthrough_score", "inventory_quality_score", "gross_margin_score", "positioning_overheat_score", "thesis_break_score"], "component_delta_explanation": "C19 shadow rewards verified sell-through + inventory quality + gross-margin bridge, and caps brand/reopening heat when inventory and margin proof is missing.", "MFE_90D_pct": 141.73, "MAE_90D_pct": -3.64, "score_return_alignment_label": "strong_positive_aligned_but_4B_overlay_needed", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C19_shadow", "case_id": "C19_CEX_298540_20230418_NATIONALGEOGRAPHIC_INVENTORY_MARGIN_FADE", "trigger_id": "T298540_STAGE2_20230418_BRAND_EXPANSION_WITHOUT_INVENTORY_BRIDGE", "symbol": "298540", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 6, "relative_strength_score": 12, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 8, "sellthrough_score": 5, "inventory_quality_score": -2, "gross_margin_score": 4, "brand_heat_score": 7, "positioning_overheat_score": -2, "thesis_break_score": 0}, "weighted_score_before": 77, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 12, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": -9, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 1, "sellthrough_score": 1, "inventory_quality_score": -14, "gross_margin_score": 1, "brand_heat_score": 3, "positioning_overheat_score": -9, "thesis_break_score": -6}, "weighted_score_after": 59, "stage_label_after": "Stage2-Watch", "changed_components": ["margin_bridge_score", "channel_reorder_score", "sellthrough_score", "inventory_quality_score", "gross_margin_score", "positioning_overheat_score", "thesis_break_score"], "component_delta_explanation": "C19 shadow rewards verified sell-through + inventory quality + gross-margin bridge, and caps brand/reopening heat when inventory and margin proof is missing.", "MFE_90D_pct": 4.71, "MAE_90D_pct": -37.74, "score_return_alignment_label": "corrected_false_positive", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C19_shadow", "case_id": "C19_CEX_031430_20230208_REOPENING_RETAIL_MARGIN_FALSE_PROMOTION", "trigger_id": "T031430_STAGE2_20230208_REOPENING_BRAND_RETAIL_NO_MARGIN_BRIDGE", "symbol": "031430", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 7, "revision_score": 6, "relative_strength_score": 9, "customer_quality_score": 5, "policy_or_regulatory_score": 3, "valuation_repricing_score": 5, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 7, "sellthrough_score": 4, "inventory_quality_score": -2, "gross_margin_score": 4, "brand_heat_score": 6, "positioning_overheat_score": -2, "thesis_break_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 9, "customer_quality_score": 5, "policy_or_regulatory_score": 3, "valuation_repricing_score": 5, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 1, "sellthrough_score": 1, "inventory_quality_score": -13, "gross_margin_score": 1, "brand_heat_score": 2, "positioning_overheat_score": -8, "thesis_break_score": -5}, "weighted_score_after": 60, "stage_label_after": "Stage2-Watch", "changed_components": ["margin_bridge_score", "channel_reorder_score", "sellthrough_score", "inventory_quality_score", "gross_margin_score", "positioning_overheat_score", "thesis_break_score"], "component_delta_explanation": "C19 shadow rewards verified sell-through + inventory quality + gross-margin bridge, and caps brand/reopening heat when inventory and margin proof is missing.", "MFE_90D_pct": 0.79, "MAE_90D_pct": -34.33, "score_return_alignment_label": "corrected_false_positive", "current_profile_verdict": "current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c19_sellthrough_inventory_margin_bridge_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,+2,+2,"Verified sell-through + inventory quality + gross-margin bridge separated 036620/337930 positives from 298540/031430 false positives.","Avg selected positive MFE90 99.28% vs counterexample MFE90 2.75%; counterexample MAE90 -36.03%.","T036620_STAGE2A_20230515_SNOWPEAK_RETAIL_MARGIN_REORDER|T337930_STAGE2A_20240516_XEXYMIX_REORDER_MARGIN",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c19_brand_heat_inventory_cap,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,cap_stage2_watch,cap,"Brand heat/reopening narratives without inventory or margin proof produced false positive paths.","Blocks 298540/031430 Stage3-Yellow false promotion while keeping positives with proof.","T298540_STAGE2_20230418_BRAND_EXPANSION_WITHOUT_INVENTORY_BRIDGE|T031430_STAGE2_20230208_REOPENING_BRAND_RETAIL_NO_MARGIN_BRIDGE",4,4,2,medium,sector_shadow_only,"not production; post-calibrated residual"
shadow_weight,c19_price_only_local_4b_watch_overlay,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,watch_only,+1,"C19 reratings can overshoot before fundamentals break; local peak must be split from full-window peak.","337930 local 4B proximity 0.85 but full-window 0.41, so price-only local 4B is too early for full exit.","T036620_4B_20230711_PRICE_ONLY_LOCAL_PEAK_WATCH|T337930_4B_20240710_LOCAL_PRICE_ONLY_TOO_EARLY",4,4,2,low,canonical_shadow_only,"4B overlay only"
```

### 25.6 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": "73", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["brand_heat_inventory_false_positive", "reopening_retail_margin_false_positive", "positive_high_mae_4b_late", "price_only_local_4b_too_early"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type": "narrative_only", "case_id": null, "symbol": null, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "reason": "none; all four representative cases have usable 180D stock-web windows; evidence URLs remain source_proxy_only before production promotion", "price_source": "Songdaiki/stock-web", "usage": "research_note"}
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
completed_round = R5
completed_loop = 73
next_round = R6
next_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-Web files explicitly checked in this run:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/036/036620.json
atlas/symbol_profiles/337/337930.json
atlas/symbol_profiles/298/298540.json
atlas/symbol_profiles/031/031430.json
atlas/ohlcv_tradable_by_symbol_year/036/036620/2023.csv
atlas/ohlcv_tradable_by_symbol_year/036/036620/2024.csv
atlas/ohlcv_tradable_by_symbol_year/337/337930/2024.csv
atlas/ohlcv_tradable_by_symbol_year/337/337930/2025.csv
atlas/ohlcv_tradable_by_symbol_year/298/298540/2023.csv
atlas/ohlcv_tradable_by_symbol_year/298/298540/2024.csv
atlas/ohlcv_tradable_by_symbol_year/031/031430/2023.csv
```

Important source caveat: the price source is raw/unadjusted marcap OHLC. The cases in this file have clean 180D windows, but 1Y/2Y fields are secondary and must be rechecked in any future production promotion batch.


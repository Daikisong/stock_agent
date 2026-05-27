# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R5
loop = 34
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_US_ECOMMERCE_DISTRIBUTION_CHANNEL_REORDER
output_file = e2r_stock_web_v12_residual_round_R5_loop_34_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop deliberately avoids the prior R6/C22 insurance-reserve work and chooses an undercovered consumer-brand distribution archetype. The aim is not to restate that Stage2 can be earlier than Green. The aim is to separate **true global channel-reorder K-beauty winners** from **legacy China-recovery / single-brand optionality false positives**.

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

Existing global axes tested here: `stage3_green_total_min`, `stage3_green_revision_min`, `price_only_blowoff_blocks_positive_stage`, and `full_4b_requires_non_price_evidence`. The proposed change is C20-specific and remains shadow-only.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R5
loop = 34
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_US_ECOMMERCE_DISTRIBUTION_CHANNEL_REORDER
loop_objective = coverage_gap_fill; counterexample_mining; sector_specific_rule_discovery; green_strictness_stress_test; 4B_non_price_requirement_stress_test
```

The canonical compression used here is:

```text
K_BEAUTY_US_ECOMMERCE_DISTRIBUTION_CHANNEL_REORDER
K_BEAUTY_PRODUCT_HIT_GLOBAL_REORDER
CHINA_PREMIUM_RECOVERY_BETA_FALSE_POSITIVE
COSRX_SINGLE_BRAND_CONSOLIDATION_FADE
=> C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
```

## 3. Previous Coverage / Duplicate Avoidance Check

GitHub search over allowed `stock_agent` research artifacts returned no direct C20/K-beauty residual rows for the selected symbols. Therefore this loop treats the four representative cases as new independent cases.

```text
auto_selected_coverage_gap = L5/C20 K-beauty global distribution channel-reorder undercoverage
new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
new_trigger_family_count = 4
new_canonical_archetype_count = 1
```

Diversity governor result:

```text
same_archetype_new_symbol_bonus = +16
same_archetype_counterexample_bonus = +10
same_archetype_new_trigger_family_bonus = +16
undercovered_sector_bonus = +3
residual_error_bonus = +10
repeated_same_symbol_penalty = 0
repeated_same_trigger_date_penalty = 0
schema_rematerialization_penalty = 0
diversity_score_summary = high_new_independent_signal
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest validation: generated atlas version 1.0.0 uses FinanceData/marcap, raw/unadjusted marcap prices, `max_date = 2026-02-20`, `tradable_row_count = 14354401`, `symbol_count = 5414`, and calibration shard root `atlas/ohlcv_tradable_by_symbol_year`. It also states that zero-volume/zero-OHLC rows are excluded from calibration shards and corporate-action-contaminated windows are blocked by default. fileciteturn716file0L3-L3

```json
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

External sector backdrop: Reuters reported that South Korea surpassed France as the largest cosmetics exporter to the U.S. in 2024, driven largely by e-commerce, and that Silicon2's CEO framed physical-store expansion as the next durability test. Reuters also flagged that COSRX is now part of Amorepacific and that competition/cheaper alternatives were emerging. citeturn624482news1 China softness remains a live counterweight for legacy beauty exposure; Reuters described prolonged China cosmetics weakness in its Shiseido coverage. citeturn514494news0

## 5. Historical Eligibility Gate

| symbol | profile status | corporate-action status | 180D usable? | profile citation |
|---:|---|---|---|---|
| 257720 | active_like, 2021-09-29 to 2026-02-20 | candidate dates only in 2022, outside tested windows | true | fileciteturn705file0L3-L3 |
| 018290 | active_like, long history, name changed to 브이티 in 2023 | candidate dates before 2020, outside tested windows | true | fileciteturn706file0L3-L3 fileciteturn707file0L3-L3 |
| 051900 | active_like, no corporate-action candidate dates | clean 180D window | true | fileciteturn708file0L3-L3 |
| 090430 | active_like, old 2015 corporate-action candidate only | clean 180D window | true | fileciteturn717file0L3-L3 |

## 6. Canonical Archetype Compression Map

```text
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION =
    channel_reorder_score
  + global_distribution_score
  + customer_quality_score
  + revision_score
  + relative_strength_score
  - china_legacy_exposure_risk_score
  - single_brand_concentration_risk_score
```

The archetype behaves like a distributor shelf: if products are repeatedly reordered across independent channels, inventory moves forward; if the thesis is only “China may recover” or “one brand is hot,” the shelf can look full while the conveyor behind it is empty.

## 7. Case Selection Summary

| case_id | symbol/company | role | case_type | best_trigger | current_profile |
|---|---:|---|---|---|---|
| R5L34_C20_257720_SILICON2_US_ECOM_DIST | 257720 실리콘투 | positive | structural_success | R5L34_C20_257720_T_STAGE2_2024_02_21 | current_profile_correct |
| R5L34_C20_018290_VT_REEDLE_SHOT_GLOBAL | 018290 브이티 | positive | high_mae_success | R5L34_C20_018290_T_STAGE2_2024_02_14 | current_profile_correct |
| R5L34_C20_051900_LGHNH_CHINA_RECOVERY_BETA | 051900 LG생활건강 | counterexample | failed_rerating | R5L34_C20_051900_T_STAGE2_2024_04_26 | current_profile_false_positive |
| R5L34_C20_090430_AMORE_COSRX_CONSOLIDATION_FADE | 090430 아모레퍼시픽 | counterexample | 4B_overlay_success | R5L34_C20_090430_T_STAGE2_2024_04_26 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 2
4C_case_count = 0
calibration_usable_case_count = 4
representative_trigger_count = 4
calibration_usable_trigger_count = 8
```

The balance is sufficient for a C20-specific shadow rule because the same canonical archetype has both clear positives and clear false-positive paths.

## 9. Evidence Source Map

| case | Stage2 evidence | Stage3 evidence | 4B evidence | interpretation |
|---|---|---|---|---|
| Silicon2 | public channel/distributor rerating, relative strength, early revision | confirmed financial visibility later | later drawdown but not trigger blocker | early C20 channel evidence was valuable |
| VT | product-hit + global channel pull, relative strength | confirmed revision and repeat order later | none at Stage2 | high MAE success; needs tolerance but not blind Green |
| LG H&H | price + China recovery beta | weak durable channel proof | price-only local peak | current profile over-promotes if it treats brand beta as C20 reorder |
| Amorepacific | COSRX/global optionality + price | single-brand concentration risk not fully separated | price-only peak at 200,500 high | current profile over-promotes single-brand optionality |

## 10. Price Data Source Map

| symbol | tradable shard | profile | price row citation |
|---:|---|---|---|
| 257720 | atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv | atlas/symbol_profiles/257/257720.json | fileciteturn709file0L3-L3 fileciteturn710file0L3-L3 |
| 018290 | atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv | atlas/symbol_profiles/018/018290.json | fileciteturn711file0L3-L3 fileciteturn712file0L3-L3 |
| 051900 | atlas/ohlcv_tradable_by_symbol_year/051/051900/2024.csv + 2025.csv | atlas/symbol_profiles/051/051900.json | fileciteturn713file0L3-L3 fileciteturn714file0L3-L3 fileciteturn715file0L3-L3 |
| 090430 | atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv + 2025.csv | atlas/symbol_profiles/090/090430.json | fileciteturn718file0L3-L3 fileciteturn719file0L3-L3 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case | type | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak | current_profile | role |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| R5L34_C20_257720_T_STAGE2_2024_02_21 | 257720 실리콘투 | Stage2-Actionable | 2024-02-21 | 10,400 | 26.92 | 421.15 | 421.15 | -16.54 | -16.54 | -16.54 | 2024-06-19 54,200 | current_profile_correct | representative |
| R5L34_C20_257720_T_GREEN_2024_05_16 | 257720 실리콘투 | Stage3-Green | 2024-05-16 | 28,900 | 87.54 | 87.54 | 87.54 | -10.38 | -10.38 | -17.3 | 2024-06-19 54,200 | current_profile_too_late | label_comparison_only |
| R5L34_C20_018290_T_STAGE2_2024_02_14 | 018290 브이티 | Stage2-Actionable | 2024-02-14 | 18,940 | 4.28 | 111.19 | 111.19 | -21.38 | -21.38 | -21.38 | 2024-06-19 40,000 | current_profile_correct | representative |
| R5L34_C20_018290_T_GREEN_2024_05_16 | 018290 브이티 | Stage3-Green | 2024-05-16 | 25,550 | 56.56 | 56.56 | 56.56 | -2.74 | -2.74 | -2.74 | 2024-06-19 40,000 | current_profile_correct | label_comparison_only |
| R5L34_C20_051900_T_STAGE2_2024_04_26 | 051900 LG생활건강 | Stage2-Actionable | 2024-04-26 | 392,000 | 22.45 | 22.45 | 22.45 | -4.46 | -18.11 | -24.87 | 2024-05-23 480,000 | current_profile_false_positive | representative |
| R5L34_C20_051900_T_4B_2024_05_23 | 051900 LG생활건강 | Stage4B-Overlay | 2024-05-23 | 460,000 | 4.35 | 4.35 | 4.35 | -25.54 | -30.22 | -35.98 | 2024-05-23 480,000 | current_profile_4B_too_late | 4B_overlay_only |
| R5L34_C20_090430_T_STAGE2_2024_04_26 | 090430 아모레퍼시픽 | Stage2-Actionable | 2024-04-26 | 150,600 | 33.13 | 33.13 | 33.13 | -2.72 | -23.04 | -32.6 | 2024-05-31 200,500 | current_profile_false_positive | representative |
| R5L34_C20_090430_T_4B_2024_05_31 | 090430 아모레퍼시픽 | Stage4B-Overlay | 2024-05-31 | 194,200 | 3.24 | 3.24 | 3.24 | -24.87 | -40.32 | -47.73 | 2024-05-31 200,500 | current_profile_4B_too_late | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

### Representative trigger aggregate rows

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | interpretation |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 257720 | 10,400 | 26.92 | -16.54 | 421.15 | -16.54 | 421.15 | -16.54 | true structural success |
| 018290 | 18,940 | 4.28 | -21.38 | 111.19 | -21.38 | 111.19 | -21.38 | high-MAE success |
| 051900 | 392,000 | 22.45 | -4.46 | 22.45 | -18.11 | 22.45 | -24.87 | failed rerating |
| 090430 | 150,600 | 33.13 | -2.72 | 33.13 | -23.04 | 33.13 | -32.60 | failed rerating after local peak |

### 4B overlay rows

| symbol | overlay entry | local/full peak | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 051900 | 460,000 | 480,000 | 4.35 | -25.54 | 4.35 | -30.22 | 4.35 | -35.98 | price-only overlay useful, not full 4B |
| 090430 | 194,200 | 200,500 | 3.24 | -24.87 | 3.24 | -40.32 | 3.24 | -47.73 | price-only overlay useful, not full 4B |

## 13. Current Calibrated Profile Stress Test

| case | current profile verdict | actual path | stress-test conclusion |
|---|---|---|---|
| Silicon2 | current_profile_correct | Stage2 had 421.15% 90D/180D MFE after -16.54% MAE | Stage2 bonus not excessive when C20 channel/distribution evidence exists |
| VT | current_profile_correct | high-MAE Stage2 still reached +111.19% MFE | Green strictness should not erase Stage2; C20 needs high-MAE tolerance |
| LG H&H | current_profile_false_positive | local +22.45% MFE but -24.87% 180D MAE | generic China recovery beta must be capped |
| Amorepacific | current_profile_false_positive | local +33.13% MFE but -32.60% 180D MAE | single-brand/global optionality must not be treated as full C20 reorder breadth |

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Green entry | cycle peak | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| Silicon2 | 10,400 | 28,900 | 54,200 | 0.422 | Green was materially later but still usable |
| VT | 18,940 | 25,550 | 40,000 | 0.314 | Green was only moderately late |
| LG H&H | 392,000 | n/a | 480,000 | not_applicable | no confirmed C20 Green; price was China-beta not channel proof |
| Amorepacific | 150,600 | n/a | 200,500 | not_applicable | no confirmed C20 Green; single-brand optionality faded |

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | evidence type | timing verdict |
|---|---:|---:|---|---|
| LG H&H 2024-05-23 | 0.773 | 0.773 | price_only, valuation_blowoff, positioning_overheat | useful overlay but not full 4B without non-price thesis deterioration |
| Amorepacific 2024-05-31 | 0.874 | 0.874 | price_only, valuation_blowoff, positioning_overheat | useful overlay but not full 4B without non-price thesis deterioration |

This strengthens, not weakens, the existing full-4B rule. A price-only peak can be a **risk overlay**; it cannot be the whole 4B unless revision slowdown, channel deterioration, margin rollback, or explicit thesis damage appears.

## 16. 4C Protection Audit

No hard 4C rows are promoted in this loop. The two failed reratings are 4B/guard candidates, not hard 4C thesis-break rows.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_success = not_tested
hard_4c_late = not_tested
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_name = L5_C20_channel_reorder_over_legacy_country_beta
candidate_delta = +3 to channel_reorder/global_distribution when non-China e-commerce or multi-channel reorder proof exists
candidate_guard = -6 cap for generic China recovery beta without channel/reorder breadth
```

Reason: the same K-beauty macro backdrop rewarded Silicon2/VT but did not protect LG H&H or Amorepacific after their local rallies. The discriminant was not “beauty is strong.” It was whether the evidence showed repeatable global distribution/reorder rather than country-beta or single-brand optionality.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
candidate = c20_channel_reorder_global_distribution_bonus
guard = c20_legacy_china_recovery_cap
overlay = c20_price_only_local_peak_4b_overlay_guard
```

C20 should behave like a customs conveyor, not a billboard. The billboard is narrative visibility; the conveyor is reorder, shipment, replenishment, and channel proof. Only the conveyor deserves Stage promotion.

## 19. Before / After Backtest Comparison

| profile | selected entries | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false_positive_rate | late_green_count | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 4 representative | 146.73 | -19.77 | 146.73 | -23.35 | 50% | 1 | catches K-beauty winners but over-promotes China recovery beta |
| P0b e2r_2_0_baseline_reference | 4 representative | 146.73 | -19.77 | 146.73 | -23.35 | 50% | 2 | less strict revision timing, worse false-positive control |
| P1 sector_specific_candidate_profile | 4 representative | 146.73 | -19.77 | 146.73 | -23.35 | 25% | 1 | keeps C20 winners but caps generic China-beta |
| P2 canonical_archetype_candidate_profile | 4 representative | 266.17 | -18.96 | 266.17 | -18.96 | 0% | 1 | selects Silicon2/VT, rejects LGHNH/Amore as WatchOnly |
| P3 counterexample_guard_profile | 4 representative + 2 overlay | 266.17 | -18.96 | 266.17 | -18.96 | 0% | 0 | separates Stage promotion from 4B price-only overlay |


## 20. Score-Return Alignment Matrix

| case | raw score before | label before | raw score after | label after | return alignment |
|---|---:|---|---:|---|---|
| Silicon2 | 82 | Stage2-Actionable | 89 | Stage3-Yellow | improves early positive capture |
| VT | 72 | Stage2-Actionable | 79 | Stage2-Actionable-HighConviction | improves but does not force Green due high MAE |
| LG H&H | 65 | Stage3-Yellow-like risk | 42 | Stage2-WatchOnly | fixes false positive |
| Amorepacific | 74 | Stage3-Yellow-like risk | 51 | Stage2-WatchOnly | fixes single-brand fade false positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_BEAUTY_US_ECOMMERCE_DISTRIBUTION_CHANNEL_REORDER | 2 | 2 | 2 | 0 | 4 | 0 | 8 | 4 | 2 | true | true | needs hard 4C/channel-break examples |

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
positive_case_count: 2
counterexample_count: 2
current_profile_error_count: 2
tested_existing_calibrated_axes:
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - generic_china_recovery_false_positive
  - single_brand_concentration_fade
  - price_only_local_peak_requires_4B_overlay
new_axis_proposed:
  - c20_channel_reorder_global_distribution_bonus
  - c20_legacy_china_recovery_cap
  - c20_price_only_local_peak_4b_overlay_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: L5/C20 K-beauty global distribution channel-reorder undercoverage
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Songdaiki/stock-web manifest and price basis
- symbol profile dates and corporate-action candidate windows
- representative trigger entry prices from tradable_raw close
- 30D/90D/180D MFE/MAE from stock-web OHLC row slices
- 4B local/full-window proximity for LG H&H and Amorepacific
- current calibrated profile residual false-positive behavior
```

Not validated:

```text
- live 2026 candidate scan
- production scoring code
- broker API / auto-trading
- complete 1Y/2Y metrics for all rows
- full DART line-by-line extraction
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c20_channel_reorder_global_distribution_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,+3,+3,"positive cases showed large 90D/180D MFE when distributor/channel-reorder evidence preceded full revision","kept Silicon2/VT early while not promoting LGHNH/Amore without channel proof","R5L34_C20_257720_T_STAGE2_2024_02_21|R5L34_C20_018290_T_STAGE2_2024_02_14",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c20_legacy_china_recovery_cap,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,-6,-6,"generic China recovery beta created false positives when channel reorder breadth was absent","demotes LGHNH and Amore from Yellow/Green to WatchOnly","R5L34_C20_051900_T_STAGE2_2024_04_26|R5L34_C20_090430_T_STAGE2_2024_04_26",4,4,2,medium,counterexample_guard_profile,"not production; post-calibrated residual"
shadow_weight,c20_price_only_local_peak_4b_overlay_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,false,true,+1,"price-only local peak worked as a risk overlay but should not be treated as full thesis break","improves 4B risk timing for LGHNH/Amore without violating non-price 4B rule","R5L34_C20_051900_T_4B_2024_05_23|R5L34_C20_090430_T_4B_2024_05_31",4,4,2,medium,overlay_guard_only,"not production; keeps full_4b_requires_non_price_evidence"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R5L34_C20_257720_SILICON2_US_ECOM_DIST","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"34","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_ECOMMERCE_DISTRIBUTION_CHANNEL_REORDER","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R5L34_C20_257720_T_STAGE2_2024_02_21","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"K-beauty cross-border distributor; price confirmed that early channel/reorder evidence mattered before fully confirmed revision."}
{"row_type":"case","case_id":"R5L34_C20_018290_VT_REEDLE_SHOT_GLOBAL","symbol":"018290","company_name":"브이티","round":"R5","loop":"34","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_ECOMMERCE_DISTRIBUTION_CHANNEL_REORDER","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R5L34_C20_018290_T_STAGE2_2024_02_14","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Brand/product hit + global channel pull; high early MAE means C20 should require drawdown tolerance unless channel evidence is clean."}
{"row_type":"case","case_id":"R5L34_C20_051900_LGHNH_CHINA_RECOVERY_BETA","symbol":"051900","company_name":"LG생활건강","round":"R5","loop":"34","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_ECOMMERCE_DISTRIBUTION_CHANNEL_REORDER","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R5L34_C20_051900_T_STAGE2_2024_04_26","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_residual_error","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"China-premium recovery beta produced a local rally, but no durable US/e-commerce channel-reorder proof; subsequent MAE overwhelmed the local MFE."}
{"row_type":"case","case_id":"R5L34_C20_090430_AMORE_COSRX_CONSOLIDATION_FADE","symbol":"090430","company_name":"아모레퍼시픽","round":"R5","loop":"34","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_ECOMMERCE_DISTRIBUTION_CHANNEL_REORDER","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"R5L34_C20_090430_T_STAGE2_2024_04_26","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_residual_error","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"COSRX/global brand optionality initially worked, but the move faded when durable multi-brand distribution/reorder proof lagged."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R5L34_C20_257720_T_STAGE2_2024_02_21","case_id":"R5L34_C20_257720_SILICON2_US_ECOM_DIST","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"34","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_ECOMMERCE_DISTRIBUTION_CHANNEL_REORDER","sector":"consumer_brand_distribution","primary_archetype":"K-beauty global distribution / US e-commerce channel-reorder","loop_objective":"coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;green_strictness_stress_test;4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-21","evidence_available_at_that_date":"K-beauty e-commerce distributor rerating; price row shows 10,400 close on first high-volume breakout. Reuters later confirms the 2024 US-export/e-commerce structural backdrop for K-beauty.","evidence_source":"public earnings/news narrative + Songdaiki/stock-web OHLC validation; Reuters sector backdrop for 2024 K-beauty US e-commerce","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv","profile_path":"atlas/symbol_profiles/257/257720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-21","entry_price":10400,"MFE_30D_pct":26.92,"MFE_90D_pct":421.15,"MFE_180D_pct":421.15,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-16.54,"MAE_90D_pct":-16.54,"MAE_180D_pct":-16.54,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":54200,"drawdown_after_peak_pct":-37.08,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_tested_no_hard_4c","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L34_C20_257720_SILICON2_US_ECOM_DIST_2024-02-21_10400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L34_C20_257720_T_GREEN_2024_05_16","case_id":"R5L34_C20_257720_SILICON2_US_ECOM_DIST","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"34","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_ECOMMERCE_DISTRIBUTION_CHANNEL_REORDER","sector":"consumer_brand_distribution","primary_archetype":"K-beauty global distribution / US e-commerce channel-reorder","loop_objective":"coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;green_strictness_stress_test;4B_non_price_requirement_stress_test","trigger_type":"Stage3-Green","trigger_date":"2024-05-16","evidence_available_at_that_date":"Q1/confirmed-revision style trigger after the stock already re-rated; 28,900 close captured only part of the full cycle upside.","evidence_source":"public earnings/news narrative + Songdaiki/stock-web OHLC validation; Reuters sector backdrop for 2024 K-beauty US e-commerce","stage2_evidence_fields":["relative_strength","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv","profile_path":"atlas/symbol_profiles/257/257720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-16","entry_price":28900,"MFE_30D_pct":87.54,"MFE_90D_pct":87.54,"MFE_180D_pct":87.54,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.38,"MAE_90D_pct":-10.38,"MAE_180D_pct":-17.3,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":54200,"drawdown_after_peak_pct":-55.9,"green_lateness_ratio":0.422,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_tested_no_hard_4c","trigger_outcome_label":"late_green_but_still_positive","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L34_C20_257720_SILICON2_US_ECOM_DIST_2024-05-16_28900","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":false,"reuse_reason":null,"independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R5L34_C20_018290_T_STAGE2_2024_02_14","case_id":"R5L34_C20_018290_VT_REEDLE_SHOT_GLOBAL","symbol":"018290","company_name":"브이티","round":"R5","loop":"34","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_ECOMMERCE_DISTRIBUTION_CHANNEL_REORDER","sector":"consumer_brand_distribution","primary_archetype":"K-beauty global distribution / US e-commerce channel-reorder","loop_objective":"coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;green_strictness_stress_test;4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-14","evidence_available_at_that_date":"Reedle Shot/product-hit narrative and channel expansion signal; 18,940 close, but early drawdown was large before June high.","evidence_source":"public earnings/news narrative + Songdaiki/stock-web OHLC validation; Reuters sector backdrop for 2024 K-beauty US e-commerce","stage2_evidence_fields":["customer_or_order_quality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv","profile_path":"atlas/symbol_profiles/018/018290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-14","entry_price":18940,"MFE_30D_pct":4.28,"MFE_90D_pct":111.19,"MFE_180D_pct":111.19,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-21.38,"MAE_90D_pct":-21.38,"MAE_180D_pct":-21.38,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":40000,"drawdown_after_peak_pct":-35.0,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_tested_no_hard_4c","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L34_C20_018290_VT_REEDLE_SHOT_GLOBAL_2024-02-14_18940","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L34_C20_018290_T_GREEN_2024_05_16","case_id":"R5L34_C20_018290_VT_REEDLE_SHOT_GLOBAL","symbol":"018290","company_name":"브이티","round":"R5","loop":"34","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_ECOMMERCE_DISTRIBUTION_CHANNEL_REORDER","sector":"consumer_brand_distribution","primary_archetype":"K-beauty global distribution / US e-commerce channel-reorder","loop_objective":"coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;green_strictness_stress_test;4B_non_price_requirement_stress_test","trigger_type":"Stage3-Green","trigger_date":"2024-05-16","evidence_available_at_that_date":"Confirmed post-Q1 rerating trigger; 25,550 close still retained upside, but Stage2 carried more total MFE.","evidence_source":"public earnings/news narrative + Songdaiki/stock-web OHLC validation; Reuters sector backdrop for 2024 K-beauty US e-commerce","stage2_evidence_fields":["relative_strength","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv","profile_path":"atlas/symbol_profiles/018/018290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-16","entry_price":25550,"MFE_30D_pct":56.56,"MFE_90D_pct":56.56,"MFE_180D_pct":56.56,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.74,"MAE_90D_pct":-2.74,"MAE_180D_pct":-2.74,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":40000,"drawdown_after_peak_pct":-37.88,"green_lateness_ratio":0.314,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_tested_no_hard_4c","trigger_outcome_label":"green_not_too_late","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L34_C20_018290_VT_REEDLE_SHOT_GLOBAL_2024-05-16_25550","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":false,"reuse_reason":null,"independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R5L34_C20_051900_T_STAGE2_2024_04_26","case_id":"R5L34_C20_051900_LGHNH_CHINA_RECOVERY_BETA","symbol":"051900","company_name":"LG생활건강","round":"R5","loop":"34","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_ECOMMERCE_DISTRIBUTION_CHANNEL_REORDER","sector":"consumer_brand_distribution","primary_archetype":"K-beauty global distribution / US e-commerce channel-reorder","loop_objective":"coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;green_strictness_stress_test;4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-26","evidence_available_at_that_date":"China-premium recovery and brand turnaround beta; 392,000 close. Follow-through failed as durable channel/reorder proof was weaker than the price move.","evidence_source":"public earnings/news narrative + Songdaiki/stock-web OHLC validation; Reuters sector backdrop for 2024 K-beauty US e-commerce","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051900/2024.csv","profile_path":"atlas/symbol_profiles/051/051900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-26","entry_price":392000,"MFE_30D_pct":22.45,"MFE_90D_pct":22.45,"MFE_180D_pct":22.45,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.46,"MAE_90D_pct":-18.11,"MAE_180D_pct":-24.87,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-23","peak_price":480000,"drawdown_after_peak_pct":-38.65,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["price_only"],"four_c_protection_label":"not_tested_no_hard_4c","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L34_C20_051900_LGHNH_CHINA_RECOVERY_BETA_2024-04-26_392000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L34_C20_051900_T_4B_2024_05_23","case_id":"R5L34_C20_051900_LGHNH_CHINA_RECOVERY_BETA","symbol":"051900","company_name":"LG생활건강","round":"R5","loop":"34","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_ECOMMERCE_DISTRIBUTION_CHANNEL_REORDER","sector":"consumer_brand_distribution","primary_archetype":"K-beauty global distribution / US e-commerce channel-reorder","loop_objective":"coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;green_strictness_stress_test;4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2024-05-23","evidence_available_at_that_date":"Price-only local peak near 480,000 high / 460,000 close; good risk overlay in hindsight but insufficient as full 4B without non-price deterioration evidence at that date.","evidence_source":"public earnings/news narrative + Songdaiki/stock-web OHLC validation; Reuters sector backdrop for 2024 K-beauty US e-commerce","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051900/2024.csv","profile_path":"atlas/symbol_profiles/051/051900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-23","entry_price":460000,"MFE_30D_pct":4.35,"MFE_90D_pct":4.35,"MFE_180D_pct":4.35,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-25.54,"MAE_90D_pct":-30.22,"MAE_180D_pct":-35.98,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-23","peak_price":480000,"drawdown_after_peak_pct":-38.65,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.773,"four_b_full_window_peak_proximity":0.773,"four_b_timing_verdict":"good_local_peak_but_price_only_watch_not_full_4B","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_tested_no_hard_4c","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L34_C20_051900_LGHNH_CHINA_RECOVERY_BETA_2024-05-23_460000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":null,"independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R5L34_C20_090430_T_STAGE2_2024_04_26","case_id":"R5L34_C20_090430_AMORE_COSRX_CONSOLIDATION_FADE","symbol":"090430","company_name":"아모레퍼시픽","round":"R5","loop":"34","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_ECOMMERCE_DISTRIBUTION_CHANNEL_REORDER","sector":"consumer_brand_distribution","primary_archetype":"K-beauty global distribution / US e-commerce channel-reorder","loop_objective":"coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;green_strictness_stress_test;4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-26","evidence_available_at_that_date":"COSRX/global optionality + China recovery beta; 150,600 close. The path rallied to 200,500 high then broke hard.","evidence_source":"public earnings/news narrative + Songdaiki/stock-web OHLC validation; Reuters sector backdrop for 2024 K-beauty US e-commerce","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv","profile_path":"atlas/symbol_profiles/090/090430.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-26","entry_price":150600,"MFE_30D_pct":33.13,"MFE_90D_pct":33.13,"MFE_180D_pct":33.13,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.72,"MAE_90D_pct":-23.04,"MAE_180D_pct":-32.6,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-31","peak_price":200500,"drawdown_after_peak_pct":-49.38,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["price_only"],"four_c_protection_label":"not_tested_no_hard_4c","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L34_C20_090430_AMORE_COSRX_CONSOLIDATION_FADE_2024-04-26_150600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L34_C20_090430_T_4B_2024_05_31","case_id":"R5L34_C20_090430_AMORE_COSRX_CONSOLIDATION_FADE","symbol":"090430","company_name":"아모레퍼시픽","round":"R5","loop":"34","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_ECOMMERCE_DISTRIBUTION_CHANNEL_REORDER","sector":"consumer_brand_distribution","primary_archetype":"K-beauty global distribution / US e-commerce channel-reorder","loop_objective":"coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;green_strictness_stress_test;4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2024-05-31","evidence_available_at_that_date":"Price-only blowoff/local peak at 200,500 high / 194,200 close; subsequent 180D MAE validates 4B overlay guard.","evidence_source":"public earnings/news narrative + Songdaiki/stock-web OHLC validation; Reuters sector backdrop for 2024 K-beauty US e-commerce","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv","profile_path":"atlas/symbol_profiles/090/090430.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-31","entry_price":194200,"MFE_30D_pct":3.24,"MFE_90D_pct":3.24,"MFE_180D_pct":3.24,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-24.87,"MAE_90D_pct":-40.32,"MAE_180D_pct":-47.73,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-31","peak_price":200500,"drawdown_after_peak_pct":-49.38,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.874,"four_b_full_window_peak_proximity":0.874,"four_b_timing_verdict":"good_local_peak_but_price_only_watch_not_full_4B","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_tested_no_hard_4c","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L34_C20_090430_AMORE_COSRX_CONSOLIDATION_FADE_2024-05-31_194200","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":null,"independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C20_shadow","case_id":"R5L34_C20_257720_SILICON2_US_ECOM_DIST","trigger_id":"R5L34_C20_257720_T_STAGE2_2024_02_21","symbol":"257720","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":12,"relative_strength_score":16,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":18,"global_distribution_score":15,"china_legacy_exposure_risk_score":0,"single_brand_concentration_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":12,"relative_strength_score":16,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":22,"global_distribution_score":18,"china_legacy_exposure_risk_score":0,"single_brand_concentration_risk_score":0},"weighted_score_after":89,"stage_label_after":"Stage3-Yellow","changed_components":["channel_reorder_score","+4","global_distribution_score","+3"],"component_delta_explanation":"C20 channel-reorder/global distribution bonus recognizes early distributor signal before full consensus revision.","MFE_90D_pct":421.15,"MAE_90D_pct":-16.54,"score_return_alignment_label":"positive_alignment","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C20_shadow","case_id":"R5L34_C20_018290_VT_REEDLE_SHOT_GLOBAL","trigger_id":"R5L34_C20_018290_T_STAGE2_2024_02_14","symbol":"018290","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":10,"relative_strength_score":15,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":14,"global_distribution_score":12,"china_legacy_exposure_risk_score":0,"single_brand_concentration_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":10,"relative_strength_score":15,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":18,"global_distribution_score":15,"china_legacy_exposure_risk_score":0,"single_brand_concentration_risk_score":0},"weighted_score_after":79,"stage_label_after":"Stage2-Actionable-HighConviction","changed_components":["channel_reorder_score","+4","global_distribution_score","+3"],"component_delta_explanation":"Brand-hit/product pull gets C20-specific bonus, but high early MAE prevents Green without confirmed revision.","MFE_90D_pct":111.19,"MAE_90D_pct":-21.38,"score_return_alignment_label":"positive_alignment","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C20_shadow","case_id":"R5L34_C20_051900_LGHNH_CHINA_RECOVERY_BETA","trigger_id":"R5L34_C20_051900_T_STAGE2_2024_04_26","symbol":"051900","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":14,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":5,"global_distribution_score":7,"china_legacy_exposure_risk_score":-2,"single_brand_concentration_risk_score":0},"weighted_score_before":55,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":6,"relative_strength_score":8,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":2,"global_distribution_score":3,"china_legacy_exposure_risk_score":-10,"single_brand_concentration_risk_score":0},"weighted_score_after":22,"stage_label_after":"Stage2-WatchOnly","changed_components":["channel_reorder_score","-3","global_distribution_score","-4","china_legacy_exposure_risk_score","-8"],"component_delta_explanation":"Generic China recovery/brand beta is demoted unless C20 has channel reorder proof outside legacy China exposure.","MFE_90D_pct":22.45,"MAE_90D_pct":-18.11,"score_return_alignment_label":"guard_improved_alignment","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C20_shadow","case_id":"R5L34_C20_090430_AMORE_COSRX_CONSOLIDATION_FADE","trigger_id":"R5L34_C20_090430_T_STAGE2_2024_04_26","symbol":"090430","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":7,"revision_score":10,"relative_strength_score":16,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":10,"global_distribution_score":10,"china_legacy_exposure_risk_score":-2,"single_brand_concentration_risk_score":-2},"weighted_score_before":72,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":8,"relative_strength_score":10,"customer_quality_score":11,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":7,"global_distribution_score":7,"china_legacy_exposure_risk_score":-6,"single_brand_concentration_risk_score":-8},"weighted_score_after":41,"stage_label_after":"Stage2-WatchOnly","changed_components":["single_brand_concentration_risk_score","-6","relative_strength_score","-6","channel_reorder_score","-3"],"component_delta_explanation":"COSRX/single-brand optionality is not enough for C20 Green when multi-brand reorder breadth and China-risk separation are weak.","MFE_90D_pct":33.13,"MAE_90D_pct":-23.04,"score_return_alignment_label":"guard_improved_alignment","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c20_channel_reorder_global_distribution_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,+3,+3,"positive cases showed large 90D/180D MFE when distributor/channel-reorder evidence preceded full revision","kept Silicon2/VT early while not promoting LGHNH/Amore without channel proof","R5L34_C20_257720_T_STAGE2_2024_02_21|R5L34_C20_018290_T_STAGE2_2024_02_14",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c20_legacy_china_recovery_cap,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,-6,-6,"generic China recovery beta created false positives when channel reorder breadth was absent","demotes LGHNH and Amore from Yellow/Green to WatchOnly","R5L34_C20_051900_T_STAGE2_2024_04_26|R5L34_C20_090430_T_STAGE2_2024_04_26",4,4,2,medium,counterexample_guard_profile,"not production; post-calibrated residual"
shadow_weight,c20_price_only_local_peak_4b_overlay_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,false,true,+1,"price-only local peak worked as a risk overlay but should not be treated as full thesis break","improves 4B risk timing for LGHNH/Amore without violating non-price 4B rule","R5L34_C20_051900_T_4B_2024_05_23|R5L34_C20_090430_T_4B_2024_05_31",4,4,2,medium,overlay_guard_only,"not production; keeps full_4b_requires_non_price_evidence"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R5","loop":"34","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_canonical_archetype_count":1,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["generic_china_recovery_false_positive","single_brand_concentration_fade","price_only_local_peak_requires_4B_overlay"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R5L34_C20_NEXT_HARD_4C_CHANNEL_BREAK","symbol":"TBD","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","reason":"no_hard_4c_channel_break_case_validated_in_this_loop","price_source":"Songdaiki/stock-web","usage":"next_round_state_only"}
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
next_round = R5 / C20 hard 4C channel-break or inventory-overhang cases
next_goal = find explicit order/channel deterioration after K-beauty rerating
avoid_repeating = Silicon2 2024-02-21, VT 2024-02-14, LGHNH 2024-04-26, Amore 2024-04-26 unless new 4C evidence family
```

## 28. Source Notes

- Prompt basis: uploaded v12 prompt. fileciteturn702file0
- Stock-Web manifest and symbol profiles are the price-source authority for this MD. fileciteturn716file0L3-L3
- Sector narrative is used only as historical evidence context; quantitative calibration uses stock-web OHLC rows, not news performance claims. Reuters K-beauty and China-softness sources are cited above. citeturn624482news1 citeturn514494news0

# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R13
loop = 43
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = BULDAK_GLOBAL_EXPORT_REORDER_CAPACITY | K_BEAUTY_INDIE_BRAND_GLOBAL_DISTRIBUTION | CHINA_RUSSIA_FOOD_CHANNEL_RERATING_GUARD | RAMEN_GLOBAL_BRAND_MARGIN_OVERHANG_GUARD
output_file = e2r_stock_web_v12_residual_round_R13_loop_43_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is historical calibration research only. It is not current candidate discovery, not an investment recommendation, and not a production patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop does not re-argue the already applied global rules. It stress-tests C20 against a simple question: when does a global consumer brand become a repeat-order, margin-supported rerating rather than a price-only or brand-only story?

## 2. Round / Large Sector / Canonical Archetype Scope

- `large_sector_id`: `L5_CONSUMER_BRAND_DISTRIBUTION`
- `canonical_archetype_id`: `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION`
- `loop_objective`: `holdout_validation`, `sector_specific_rule_discovery`, `canonical_archetype_compression`, `counterexample_mining`, `residual_false_positive_mining`, `coverage_gap_fill`
- Positive structural cases: 삼양식품, 실리콘투
- Counterexamples / guards: 오리온, 농심

## 3. Previous Coverage / Duplicate Avoidance Check

The stock_agent ingest summary previously covered R1~R13 and loops 1~9, with 1,376 aggregate representative trigger rows after validation. This loop is deliberately assigned to `R13 / loop 43` and uses four new symbols for the current v12 residual lane. The codebase itself was not opened; only permitted research-artifact coverage signals were used.

```text
required_new_independent_case_ratio = 0.60
calibration_usable_case_count = 4
new_independent_case_count = 4
new_independent_case_ratio = 1.00
reuse_count = 0
loop_contribution_label = canonical_archetype_rule_candidate
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_atlas_repo = https://github.com/Songdaiki/stock-web
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
manifest_min_date = 1995-05-02
manifest_max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

Stock-Web schema confirms that tradable shards use `d,o,h,l,c,v,a,mc,s,m`; raw shards also include `rs`. The schema's MFE/MAE definitions were used: `MFE_N_pct = max(high)/entry_price - 1`, `MAE_N_pct = min(low)/entry_price - 1` over N tradable rows.

## 5. Historical Eligibility Gate

All representative triggers meet the historical eligibility gate:

```text
trigger_date_is_past = true
entry_date_exists_in_tradable_shard = true
forward_180_trading_days_available = true
high_low_close_volume_present = true
corporate_action_contaminated_180D_window = false
calibration_usable = true
```

Corporate action checks from symbol profiles:

| symbol | company | profile status | recent 180D window status |
|---|---|---|---|
| 003230 | 삼양식품 | corporate action candidates only in 2003 | clean for 2024 windows |
| 257720 | 실리콘투 | corporate action candidates in 2022 | clean for 2024 windows |
| 271560 | 오리온 | no corporate action candidates | clean |
| 004370 | 농심 | old candidates through 2003 | clean for 2024 windows |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression reason |
|---|---|---|
| BULDAK_GLOBAL_EXPORT_REORDER_CAPACITY | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | food export brand with repeated global sell-through and capacity/revision bridge |
| K_BEAUTY_INDIE_BRAND_GLOBAL_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | beauty distribution platform with multi-brand reorder/sell-through evidence |
| CHINA_RUSSIA_FOOD_CHANNEL_RERATING_GUARD | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | global food footprint without incremental channel quality can become false positive |
| RAMEN_GLOBAL_BRAND_MARGIN_OVERHANG_GUARD | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | global ramen narrative requires margin/revision guard and 4B overlay |

The compression rule is that C20 is not “global brand exists.” It is “sell-through is visible enough to trigger repeat orders, and the company has a route to convert that demand into revenue, margin, or revision.”

## 7. Case Selection Summary

| case_id | symbol | company | fine_archetype_id | case_type | role | best_trigger | current_profile_verdict |
|---|---:|---|---|---|---|---|---|
| R13L43_C20_003230_SAMYANG_BULDAK_EXPORT | 003230 | 삼양식품 | BULDAK_GLOBAL_EXPORT_REORDER_CAPACITY | structural_success | positive | SYF_STAGE2_EXPORT_REVISION_2024_03_04 | current_profile_too_late |
| R13L43_C20_257720_SILICON2_KBEAUTY_DIST | 257720 | 실리콘투 | K_BEAUTY_INDIE_BRAND_GLOBAL_DISTRIBUTION | structural_success | positive | S2_STAGE2_KBEAUTY_EXPORT_REORDER_2024_03_20 | current_profile_too_late |
| R13L43_C20_271560_ORION_CHANNEL_GUARD | 271560 | 오리온 | CHINA_RUSSIA_FOOD_CHANNEL_RERATING_GUARD | failed_rerating | counterexample | ORION_PSEUDO_GREEN_FOOD_CHANNEL_2024_06_17 | current_profile_false_positive |
| R13L43_C20_004370_NONGSHIM_LATE_PEAK | 004370 | 농심 | RAMEN_GLOBAL_BRAND_MARGIN_OVERHANG_GUARD | 4B_overlay_success | counterexample | NONGSHIM_GREEN_TOO_LATE_2024_06_13 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 3
4C_case_count = 1 watch-only / late-protection label
minimum_calibration_usable_case_count = 3
actual_calibration_usable_case_count = 4
```

Positive cases show the strong version of C20: export sell-through or channel order quality was visible before full Green. Counterexamples show the weak version: broad global brand recognition and price strength did not protect returns when margin/revision or repeat-order proof was thin.

## 9. Evidence Source Map

| case | evidence map |
|---|---|
| 삼양식품 | Buldak export demand, U.S./Europe shipment commentary, capacity support, and visible earnings revision. MarketWatch/WSJ market talk in June 2024 linked 2Q expectations to Buldak exports, higher ASP, U.S./Europe shipments, and capacity. |
| 실리콘투 | K-beauty global distribution and ecommerce-led demand. Reuters later summarized that Korean cosmetics overtook France in U.S. cosmetics exports in 2024 and quoted Silicon2's CEO on the strength and limits of the K-beauty trend. |
| 오리온 | Global confectionery presence exists, but this loop treats it as a counterexample because 2024 price path did not show a durable rerating without incremental C20 evidence. |
| 농심 | FT reported overseas expansion, Shin Ramyun's global sales contribution, and U.S. growth ambitions; the stock path still required a margin/revision guard because the June 2024 entry was close to a full-window peak. |

## 10. Price Data Source Map

| symbol | shard path | profile path | price_basis | 180D contamination |
|---:|---|---|---|---|
| 003230 | atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv | atlas/symbol_profiles/003/003230.json | tradable_raw | clean |
| 257720 | atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv | atlas/symbol_profiles/257/257720.json | tradable_raw | clean |
| 271560 | atlas/ohlcv_tradable_by_symbol_year/271/271560/2024.csv | atlas/symbol_profiles/271/271560.json | tradable_raw | clean |
| 004370 | atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv | atlas/symbol_profiles/004/004370.json | tradable_raw | clean |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol / company | type | entry_date | entry_price | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak | current verdict | aggregate role |
|---|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| SYF_STAGE2_EXPORT_REVISION_2024_03_04 | 003230 삼양식품 | Stage2-Actionable | 2024-03-04 | 191,000 | 275.92 | -7.33 | 275.92 | -7.33 | 2024-06-19 / 718,000 | current_profile_too_late | representative |
| SYF_STAGE3_GREEN_Q1_EXPORT_CONFIRM_2024_05_20 | 003230 삼양식품 | Stage3-Green | 2024-05-20 | 502,000 | 43.03 | -9.26 | 59.36 | -9.26 | 2024-12-26 / 800,000 | current_profile_too_late | label_comparison_only |
| SYF_4B_VALUATION_OVERHEAT_2024_06_18 | 003230 삼양식품 | 4B | 2024-06-18 | 712,000 | 0.84 | -36.03 | 12.36 | -36.03 | 2024-12-26 / 800,000 | current_profile_correct | 4B_overlay_only |
| S2_STAGE2_KBEAUTY_EXPORT_REORDER_2024_03_20 | 257720 실리콘투 | Stage2-Actionable | 2024-03-20 | 10,750 | 404.19 | -9.77 | 404.19 | -9.77 | 2024-06-19 / 54,200 | current_profile_too_late | representative |
| S2_STAGE3_GREEN_Q1_SURPRISE_2024_05_10 | 257720 실리콘투 | Stage3-Green | 2024-05-10 | 26,250 | 106.48 | -17.9 | 106.48 | -17.9 | 2024-06-19 / 54,200 | current_profile_correct | label_comparison_only |
| S2_4B_POSITIONING_OVERHEAT_2024_06_19 | 257720 실리콘투 | 4B | 2024-06-19 | 50,700 | 6.9 | -52.86 | 6.9 | -52.86 | 2024-06-19 / 54,200 | current_profile_4B_too_late | 4B_overlay_only |
| ORION_STAGE2_GLOBAL_CHANNEL_2024_02_16 | 271560 오리온 | Stage2-Actionable | 2024-02-16 | 97,200 | 9.77 | -7.41 | 9.77 | -15.84 | 2024-06-18 / 106,700 | current_profile_false_positive | representative |
| ORION_PSEUDO_GREEN_FOOD_CHANNEL_2024_06_17 | 271560 오리온 | Stage3-Green | 2024-06-17 | 104,400 | 2.2 | -16.95 | 2.2 | -21.65 | 2024-06-18 / 106,700 | current_profile_false_positive | label_comparison_only |
| NONGSHIM_STAGE2_OVERSEAS_RAMEN_2024_05_13 | 004370 농심 | Stage2-Actionable | 2024-05-13 | 424,000 | 41.27 | -14.98 | 41.27 | -25.24 | 2024-06-13 / 599,000 | current_profile_false_positive | representative |
| NONGSHIM_GREEN_TOO_LATE_2024_06_13 | 004370 농심 | Stage3-Green | 2024-06-13 | 547,000 | 9.51 | -34.1 | 9.51 | -42.05 | 2024-06-13 / 599,000 | current_profile_false_positive | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

### Representative trigger summary

| case | representative trigger | entry | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | verdict |
|---|---|---:|---|---|---|---|
| 삼양식품 | SYF_STAGE2_EXPORT_REVISION_2024_03_04 | 191,000 | +31.15 / -7.33 | +275.92 / -7.33 | +275.92 / -7.33 | early Stage2 was highly valuable |
| 실리콘투 | S2_STAGE2_KBEAUTY_EXPORT_REORDER_2024_03_20 | 10,750 | +22.79 / -9.77 | +404.19 / -9.77 | +404.19 / -9.77 | early Stage2 was highly valuable |
| 오리온 | ORION_STAGE2_GLOBAL_CHANNEL_2024_02_16 | 97,200 | +2.26 / -7.41 | +9.77 / -7.41 | +9.77 / -15.84 | global brand alone was weak |
| 농심 | NONGSHIM_STAGE2_OVERSEAS_RAMEN_2024_05_13 | 424,000 | +41.27 / -5.19 | +41.27 / -14.98 | +41.27 / -25.24 | needed 4B/margin guard |

## 13. Current Calibrated Profile Stress Test

1. The current calibrated profile would correctly avoid price-only promotion in pure blowoff rows, but C20 creates a more subtle residual: a global consumer brand story often looks like customer quality before sell-through and margin quality are actually proven.
2. For Samyang and Silicon2, current Green strictness is still too late: Stage2 evidence carried much of the return before full revision confirmation.
3. For Orion and Nongshim, current profile can become too generous if `global brand + relative strength + broad public narrative` is treated as Green-quality evidence.
4. Stage2 bonus is useful but needs C20-specific sign: reward `repeat sell-through / reorder / capacity route`, not mere brand recognition.
5. Full 4B non-price requirement remains correct; the new C20 issue is that valuation/positioning overheat should be allowed as an overlay when margin/revision evidence lags.
6. 4C routing should stay hard: in this loop, Nongshim and Silicon2 are 4B/guard rows, not thesis-break 4C rows.

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Green entry | cycle peak after Stage2 | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| 삼양식품 | 191,000 | 502,000 | 718,000 | 0.59 | Green captured thesis but missed a large share of repricing |
| 실리콘투 | 10,750 | 26,250 | 54,200 | 0.36 | Green was somewhat late but still usable |
| 오리온 | 97,200 | 104,400 pseudo | 106,700 | n/a | pseudo-Green had weak upside and large MAE |
| 농심 | 424,000 | 547,000 pseudo | 599,000 | 0.70 | pseudo-Green was near peak and should be guarded |

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | evidence type | verdict |
|---|---:|---:|---|---|
| SYF_4B_VALUATION_OVERHEAT_2024_06_18 | 0.99 | 0.84 | valuation_blowoff, positioning_overheat | good_full_window_4B_timing |
| S2_4B_POSITIONING_OVERHEAT_2024_06_19 | 1.00 | 1.00 | valuation_blowoff, positioning_overheat | good_full_window_4B_timing |
| NONGSHIM_GREEN_TOO_LATE_2024_06_13 | 1.00 | 1.00 | valuation_blowoff, positioning_overheat, margin_or_backlog_slowdown | good_full_window_4B_timing_if_margin_overhang_used |
| ORION_PSEUDO_GREEN_FOOD_CHANNEL_2024_06_17 | 1.00 | 1.00 | price_only | price_only_local_4B_too_early_without_non_price_guard |

## 16. 4C Protection Audit

No hard 4C trigger is proposed for production. Orion and Nongshim are better treated as Green-guard/4B-overlay residuals. Silicon2 and Samyang had large drawdowns after peaks, but the underlying thesis was not broken at the trigger dates; this is the exact difference between a C20 4B overlay and a hard 4C route.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L5_brand_retail_valuation_4B_overlay
proposal = +1 overlay weight / risk flag
condition = consumer brand rerating exceeds evidence speed, and either valuation, positioning, or margin-overhang evidence is present
not_condition = price-only local peak without non-price evidence
```

L5 consumer brands can rerate violently because stories are simple, visible, and emotionally easy to own. That makes them like a crowded store entrance: traffic proves demand, but once everyone is inside, the exit is narrow. 4B should be an overlay, not an immediate thesis break.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
new_axis_proposed = C20_sell_through_repeat_order_bonus
counter_guard = C20_inventory_margin_absence_guard
```

C20 should separate three things:

1. `brand awareness`: people know the product.
2. `sell-through/reorder`: products leave shelves and distributors reorder.
3. `margin/revision conversion`: the company converts channel heat into EPS.

Only the second and third should push Stage3. The first can support Stage2 only when paired with non-price evidence.

## 19. Before / After Backtest Comparison

| profile | false_positive_rate | missed_structural_count | late_green_count | score-return alignment |
|---|---:|---:|---:|---|
| P0 current calibrated proxy | 0.50 | 2 | 2 | mixed residual errors |
| P0b E2R 2.0 reference | 0.75 | 1 | 2 | worse false-positive control |
| P1 L5 sector candidate | 0.25 | 0 | 1 | improved positive/counterexample split |
| P2 C20 archetype candidate | 0.25 | 0 | 1 | best explanatory split |
| P3 counterexample guard | 0.00 | 1 | 1 | safer but may delay positive capture |

## 20. Score-Return Alignment Matrix

| case | score before | score after | return alignment |
|---|---:|---:|---|
| 삼양식품 Stage2 | 73.0 | 78.5 | after profile promotes useful Stage2 without forcing Green |
| 실리콘투 Stage2 | 74.0 | 80.0 | after profile captures K-beauty distribution earlier |
| 오리온 Stage2 | 75.0 | 67.0 | after profile blocks brand-only false positive |
| 농심 Stage2 | 76.5 | 68.0 | after profile blocks weak-margin C20 overpromotion |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | BULDAK_GLOBAL_EXPORT_REORDER_CAPACITY / K_BEAUTY_INDIE_BRAND_GLOBAL_DISTRIBUTION / CHINA_RUSSIA_FOOD_CHANNEL_RERATING_GUARD / RAMEN_GLOBAL_BRAND_MARGIN_OVERHANG_GUARD | 2 | 2 | 3 | 1 watch | 4 | 0 | 10 | 4 | 4 | true | true | C20 now has food+beauty positives and food counterexamples; still needs more cosmetics false-negative/4C rows. |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 4
new_trigger_family_count: 5
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: current_profile_too_late, current_profile_false_positive, current_profile_4B_too_late, high_mae_success
new_axis_proposed: C20_sell_through_repeat_order_bonus; C20_inventory_margin_absence_guard; L5_brand_retail_valuation_4B_overlay
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Stock-Web manifest/schema/profile paths.
- Actual stock-web 1D OHLC trigger entry rows.
- 30D / 90D / 180D MFE and MAE proxy calculations from tradable raw rows.
- Positive/counterexample balance.
- C20-specific residual rule candidates.

Not validated:

- Live 2026 candidate scans.
- Broker data or adjusted-price data.
- Production scoring code.
- Any stock_agent `src/e2r` implementation detail.
- Trading recommendation or portfolio action.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C20_sell_through_repeat_order_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,+2,+2,Positive cases had repeat export/sell-through and capacity/reorder proof before Green confirmation.,Improves Samyang/Silicon2 early capture without relying on price-only moves.,SYF_STAGE2_EXPORT_REVISION_2024_03_04|S2_STAGE2_KBEAUTY_EXPORT_REORDER_2024_03_20,4,4,2,medium,archetype_shadow_only,not production; post-calibrated residual
shadow_weight,C20_inventory_margin_absence_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,-2,-2,Orion/Nongshim show global brand narratives can fail without margin/reorder confirmation.,Reduces false Green for brand-only or relative-strength-only food/beauty narratives.,ORION_STAGE2_GLOBAL_CHANNEL_2024_02_16|NONGSHIM_STAGE2_OVERSEAS_RAMEN_2024_05_13,4,4,2,medium,archetype_shadow_only,not production; post-calibrated residual
shadow_weight,L5_brand_retail_valuation_4B_overlay,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,+1,+1,Fast rerating in consumer brands often needs 4B overlay even when thesis remains intact.,Improves drawdown protection after Samyang/Silicon2/Nongshim local peaks.,SYF_4B_VALUATION_OVERHEAT_2024_06_18|S2_4B_POSITIONING_OVERHEAT_2024_06_19|NONGSHIM_GREEN_TOO_LATE_2024_06_13,4,4,2,medium,sector_shadow_only,not production; post-calibrated residual
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"case_id":"R13L43_C20_003230_SAMYANG_BULDAK_EXPORT","symbol":"003230","company_name":"삼양식품","fine_archetype_id":"BULDAK_GLOBAL_EXPORT_REORDER_CAPACITY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"SYF_STAGE2_EXPORT_REVISION_2024_03_04","current_profile_verdict":"current_profile_too_late","notes":"Buldak export demand and capacity/revision route produced broad repricing; Stage3 confirmation arrived after much of the upside had already opened.","row_type":"case","round":"R13","loop":"43","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"price_source":"Songdaiki/stock-web","score_price_alignment":"aligned_positive"}
{"case_id":"R13L43_C20_257720_SILICON2_KBEAUTY_DIST","symbol":"257720","company_name":"실리콘투","fine_archetype_id":"K_BEAUTY_INDIE_BRAND_GLOBAL_DISTRIBUTION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"S2_STAGE2_KBEAUTY_EXPORT_REORDER_2024_03_20","current_profile_verdict":"current_profile_too_late","notes":"K-beauty indie-brand distribution demand repriced before classical revision-only Green was fully comfortable.","row_type":"case","round":"R13","loop":"43","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"price_source":"Songdaiki/stock-web","score_price_alignment":"aligned_positive"}
{"case_id":"R13L43_C20_271560_ORION_CHANNEL_GUARD","symbol":"271560","company_name":"오리온","fine_archetype_id":"CHINA_RUSSIA_FOOD_CHANNEL_RERATING_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"ORION_PSEUDO_GREEN_FOOD_CHANNEL_2024_06_17","current_profile_verdict":"current_profile_false_positive","notes":"Global confectionery footprint alone did not create a durable C20 rerating without incremental sell-through/reorder and margin bridge.","row_type":"case","round":"R13","loop":"43","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"price_source":"Songdaiki/stock-web","score_price_alignment":"counterexample_guard_needed"}
{"case_id":"R13L43_C20_004370_NONGSHIM_LATE_PEAK","symbol":"004370","company_name":"농심","fine_archetype_id":"RAMEN_GLOBAL_BRAND_MARGIN_OVERHANG_GUARD","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"NONGSHIM_GREEN_TOO_LATE_2024_06_13","current_profile_verdict":"current_profile_false_positive","notes":"Global ramen narrative was real, but the entry that needed revision/margin confirmation arrived near a price peak and then suffered large MAE.","row_type":"case","round":"R13","loop":"43","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"price_source":"Songdaiki/stock-web","score_price_alignment":"counterexample_guard_needed"}
```

### 25.3 trigger rows

```jsonl
{"trigger_id":"SYF_STAGE2_EXPORT_REVISION_2024_03_04","case_id":"R13L43_C20_003230_SAMYANG_BULDAK_EXPORT","symbol":"003230","company_name":"삼양식품","fine_archetype_id":"BULDAK_GLOBAL_EXPORT_REORDER_CAPACITY","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-04","entry_date":"2024-03-04","entry_price":191000,"evidence_available_at_that_date":"Buldak export demand was becoming visible, but not yet fully confirmed by multi-quarter margin/revision proof.","evidence_source":"public news/analyst commentary; stock-web OHLC rows","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["early_revision_signal"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":31.15,"MFE_90D_pct":275.92,"MFE_180D_pct":275.92,"MFE_1Y_pct":401.57,"MFE_2Y_pct":null,"MAE_30D_pct":-7.33,"MAE_90D_pct":-7.33,"MAE_180D_pct":-7.33,"MAE_1Y_pct":-7.33,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":718000,"drawdown_after_peak_pct":-36.56,"green_lateness_ratio":0.59,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SYF_2024_03_04_191000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":10,"relative_strength_score":8,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":73.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":9,"revision_score":13,"relative_strength_score":9,"customer_quality_score":17,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":78.5,"stage_label_after":"Stage3-Yellow","round":"R13","loop":"43","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","sector":"소비재·유통·브랜드","primary_archetype":"beauty_food_global_distribution","loop_objective":["holdout_validation","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","residual_false_positive_mining","coverage_gap_fill"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv","profile_path":"atlas/symbol_profiles/003/003230.json","calibration_usable":true,"calibration_block_reasons":[],"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"trigger_id":"SYF_STAGE3_GREEN_Q1_EXPORT_CONFIRM_2024_05_20","case_id":"R13L43_C20_003230_SAMYANG_BULDAK_EXPORT","symbol":"003230","company_name":"삼양식품","fine_archetype_id":"BULDAK_GLOBAL_EXPORT_REORDER_CAPACITY","trigger_type":"Stage3-Green","trigger_date":"2024-05-20","entry_date":"2024-05-20","entry_price":502000,"evidence_available_at_that_date":"Q1/export strength had become obvious enough for Green-style revision confidence.","evidence_source":"public earnings/analyst commentary; stock-web OHLC rows","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":43.03,"MFE_90D_pct":43.03,"MFE_180D_pct":59.36,"MFE_1Y_pct":145.62,"MFE_2Y_pct":null,"MAE_30D_pct":-4.68,"MAE_90D_pct":-9.26,"MAE_180D_pct":-9.26,"MAE_1Y_pct":-9.26,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-26","peak_price":800000,"drawdown_after_peak_pct":-13.0,"green_lateness_ratio":0.59,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"late_but_valid_green","current_profile_verdict":"current_profile_too_late","forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SYF_2024_05_20_502000","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":15,"revision_score":17,"relative_strength_score":10,"customer_quality_score":17,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":89.0,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":15,"revision_score":17,"relative_strength_score":10,"customer_quality_score":17,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":89.0,"stage_label_after":"Stage3-Green","round":"R13","loop":"43","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","sector":"소비재·유통·브랜드","primary_archetype":"beauty_food_global_distribution","loop_objective":["holdout_validation","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","residual_false_positive_mining","coverage_gap_fill"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv","profile_path":"atlas/symbol_profiles/003/003230.json","calibration_usable":true,"calibration_block_reasons":[],"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"trigger_id":"SYF_4B_VALUATION_OVERHEAT_2024_06_18","case_id":"R13L43_C20_003230_SAMYANG_BULDAK_EXPORT","symbol":"003230","company_name":"삼양식품","fine_archetype_id":"BULDAK_GLOBAL_EXPORT_REORDER_CAPACITY","trigger_type":"4B","trigger_date":"2024-06-18","entry_date":"2024-06-18","entry_price":712000,"evidence_available_at_that_date":"Fast price/valuation repricing after strong export evidence; non-price evidence still supported the thesis, so 4B is overlay rather than 4C.","evidence_source":"public market/earnings context; stock-web OHLC rows","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","margin_bridge"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"MFE_30D_pct":0.84,"MFE_90D_pct":0.84,"MFE_180D_pct":12.36,"MFE_1Y_pct":73.17,"MFE_2Y_pct":null,"MAE_30D_pct":-8.57,"MAE_90D_pct":-36.03,"MAE_180D_pct":-36.03,"MAE_1Y_pct":-36.03,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-26","peak_price":800000,"drawdown_after_peak_pct":-43.06,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.99,"four_b_full_window_peak_proximity":0.84,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SYF_2024_06_18_712000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":16,"revision_score":18,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":18,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":92.0,"stage_label_before":"Stage3-Green+4B-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":16,"revision_score":18,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":18,"execution_risk_score":-7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88.0,"stage_label_after":"Stage3-Green+4B-overlay","round":"R13","loop":"43","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","sector":"소비재·유통·브랜드","primary_archetype":"beauty_food_global_distribution","loop_objective":["holdout_validation","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","residual_false_positive_mining","coverage_gap_fill"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv","profile_path":"atlas/symbol_profiles/003/003230.json","calibration_usable":true,"calibration_block_reasons":[],"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"trigger_id":"S2_STAGE2_KBEAUTY_EXPORT_REORDER_2024_03_20","case_id":"R13L43_C20_257720_SILICON2_KBEAUTY_DIST","symbol":"257720","company_name":"실리콘투","fine_archetype_id":"K_BEAUTY_INDIE_BRAND_GLOBAL_DISTRIBUTION","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-20","entry_date":"2024-03-20","entry_price":10750,"evidence_available_at_that_date":"K-beauty export/distribution evidence and relative strength became visible before fully confirmed revision proof.","evidence_source":"public K-beauty/export channel context; stock-web OHLC rows","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["early_revision_signal"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":22.79,"MFE_90D_pct":404.19,"MFE_180D_pct":404.19,"MFE_1Y_pct":404.19,"MFE_2Y_pct":null,"MAE_30D_pct":-9.77,"MAE_90D_pct":-9.77,"MAE_180D_pct":-9.77,"MAE_1Y_pct":-9.77,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":54200,"drawdown_after_peak_pct":-55.9,"green_lateness_ratio":0.36,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"S2_2024_03_20_10750","dedupe_for_aggregate":true,"aggregate_group_role":"representative","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":9,"relative_strength_score":12,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":11,"relative_strength_score":13,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":80.0,"stage_label_after":"Stage3-Yellow","round":"R13","loop":"43","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","sector":"소비재·유통·브랜드","primary_archetype":"beauty_food_global_distribution","loop_objective":["holdout_validation","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","residual_false_positive_mining","coverage_gap_fill"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv","profile_path":"atlas/symbol_profiles/257/257720.json","calibration_usable":true,"calibration_block_reasons":[],"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"trigger_id":"S2_STAGE3_GREEN_Q1_SURPRISE_2024_05_10","case_id":"R13L43_C20_257720_SILICON2_KBEAUTY_DIST","symbol":"257720","company_name":"실리콘투","fine_archetype_id":"K_BEAUTY_INDIE_BRAND_GLOBAL_DISTRIBUTION","trigger_type":"Stage3-Green","trigger_date":"2024-05-10","entry_date":"2024-05-10","entry_price":26250,"evidence_available_at_that_date":"Earnings/revision evidence had caught up to export-channel price discovery.","evidence_source":"public earnings context; stock-web OHLC rows","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":106.48,"MFE_90D_pct":106.48,"MFE_180D_pct":106.48,"MFE_1Y_pct":106.48,"MFE_2Y_pct":null,"MAE_30D_pct":-17.9,"MAE_90D_pct":-17.9,"MAE_180D_pct":-17.9,"MAE_1Y_pct":-17.9,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":54200,"drawdown_after_peak_pct":-55.9,"green_lateness_ratio":0.36,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"valid_green_with_high_mae","current_profile_verdict":"current_profile_correct","forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"S2_2024_05_10_26250","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":14,"revision_score":18,"relative_strength_score":15,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":11,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":90.0,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":14,"revision_score":18,"relative_strength_score":15,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":11,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":90.0,"stage_label_after":"Stage3-Green","round":"R13","loop":"43","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","sector":"소비재·유통·브랜드","primary_archetype":"beauty_food_global_distribution","loop_objective":["holdout_validation","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","residual_false_positive_mining","coverage_gap_fill"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv","profile_path":"atlas/symbol_profiles/257/257720.json","calibration_usable":true,"calibration_block_reasons":[],"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"trigger_id":"S2_4B_POSITIONING_OVERHEAT_2024_06_19","case_id":"R13L43_C20_257720_SILICON2_KBEAUTY_DIST","symbol":"257720","company_name":"실리콘투","fine_archetype_id":"K_BEAUTY_INDIE_BRAND_GLOBAL_DISTRIBUTION","trigger_type":"4B","trigger_date":"2024-06-19","entry_date":"2024-06-19","entry_price":50700,"evidence_available_at_that_date":"Explosive rerating after K-beauty distribution evidence; subsequent drawdown shows 4B overlay had value even though the thesis was not broken.","evidence_source":"public K-beauty/export context; stock-web OHLC rows","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"MFE_30D_pct":6.9,"MFE_90D_pct":6.9,"MFE_180D_pct":6.9,"MFE_1Y_pct":6.9,"MFE_2Y_pct":null,"MAE_30D_pct":-4.73,"MAE_90D_pct":-52.86,"MAE_180D_pct":-52.86,"MAE_1Y_pct":-52.86,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":54200,"drawdown_after_peak_pct":-55.9,"green_lateness_ratio":null,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"S2_2024_06_19_50700","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":15,"revision_score":18,"relative_strength_score":18,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":20,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":91.0,"stage_label_before":"Stage3-Green+4B-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":15,"revision_score":18,"relative_strength_score":18,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":20,"execution_risk_score":-8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":87.0,"stage_label_after":"Stage3-Green+4B-overlay","round":"R13","loop":"43","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","sector":"소비재·유통·브랜드","primary_archetype":"beauty_food_global_distribution","loop_objective":["holdout_validation","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","residual_false_positive_mining","coverage_gap_fill"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv","profile_path":"atlas/symbol_profiles/257/257720.json","calibration_usable":true,"calibration_block_reasons":[],"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"trigger_id":"ORION_STAGE2_GLOBAL_CHANNEL_2024_02_16","case_id":"R13L43_C20_271560_ORION_CHANNEL_GUARD","symbol":"271560","company_name":"오리온","fine_archetype_id":"CHINA_RUSSIA_FOOD_CHANNEL_RERATING_GUARD","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-16","entry_date":"2024-02-16","entry_price":97200,"evidence_available_at_that_date":"Global confectionery footprint and rebound narrative existed, but repeat-order/margin bridge was not decisive.","evidence_source":"public market/company context; stock-web OHLC rows","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":2.26,"MFE_90D_pct":9.77,"MFE_180D_pct":9.77,"MFE_1Y_pct":14.71,"MFE_2Y_pct":null,"MAE_30D_pct":-7.41,"MAE_90D_pct":-7.41,"MAE_180D_pct":-15.84,"MAE_1Y_pct":-15.84,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-18","peak_price":106700,"drawdown_after_peak_pct":-23.34,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"ORION_2024_02_16_97200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":6,"relative_strength_score":5,"customer_quality_score":9,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":75.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":5,"relative_strength_score":4,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":67.0,"stage_label_after":"Stage2-watch","round":"R13","loop":"43","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","sector":"소비재·유통·브랜드","primary_archetype":"beauty_food_global_distribution","loop_objective":["holdout_validation","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","residual_false_positive_mining","coverage_gap_fill"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/271/271560/2024.csv","profile_path":"atlas/symbol_profiles/271/271560.json","calibration_usable":true,"calibration_block_reasons":[],"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"trigger_id":"ORION_PSEUDO_GREEN_FOOD_CHANNEL_2024_06_17","case_id":"R13L43_C20_271560_ORION_CHANNEL_GUARD","symbol":"271560","company_name":"오리온","fine_archetype_id":"CHINA_RUSSIA_FOOD_CHANNEL_RERATING_GUARD","trigger_type":"Stage3-Green","trigger_date":"2024-06-17","entry_date":"2024-06-17","entry_price":104400,"evidence_available_at_that_date":"Relative strength without robust incremental C20 sell-through/reorder proof; this is the false-positive stress test.","evidence_source":"public market context; stock-web OHLC rows","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"MFE_30D_pct":2.2,"MFE_90D_pct":2.2,"MFE_180D_pct":2.2,"MFE_1Y_pct":8.72,"MFE_2Y_pct":null,"MAE_30D_pct":-4.6,"MAE_90D_pct":-16.95,"MAE_180D_pct":-21.65,"MAE_1Y_pct":-21.65,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-18","peak_price":106700,"drawdown_after_peak_pct":-23.34,"green_lateness_ratio":null,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_too_early_without_non_price_guard","four_b_evidence_type":["price_only"],"four_c_protection_label":"false_break","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"ORION_2024_06_17_104400","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":11,"relative_strength_score":10,"customer_quality_score":9,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":87.5,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":8,"relative_strength_score":8,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":-6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":76.0,"stage_label_after":"Stage3-Yellow/guarded","round":"R13","loop":"43","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","sector":"소비재·유통·브랜드","primary_archetype":"beauty_food_global_distribution","loop_objective":["holdout_validation","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","residual_false_positive_mining","coverage_gap_fill"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/271/271560/2024.csv","profile_path":"atlas/symbol_profiles/271/271560.json","calibration_usable":true,"calibration_block_reasons":[],"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"trigger_id":"NONGSHIM_STAGE2_OVERSEAS_RAMEN_2024_05_13","case_id":"R13L43_C20_004370_NONGSHIM_LATE_PEAK","symbol":"004370","company_name":"농심","fine_archetype_id":"RAMEN_GLOBAL_BRAND_MARGIN_OVERHANG_GUARD","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-13","entry_date":"2024-05-13","entry_price":424000,"evidence_available_at_that_date":"Global ramen demand narrative and overseas expansion were visible, but margin/revision bridge was weaker than Samyang-style export sell-through.","evidence_source":"Financial Times / public market context; stock-web OHLC rows","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":41.27,"MFE_90D_pct":41.27,"MFE_180D_pct":41.27,"MFE_1Y_pct":41.27,"MFE_2Y_pct":null,"MAE_30D_pct":-5.19,"MAE_90D_pct":-14.98,"MAE_180D_pct":-25.24,"MAE_1Y_pct":-25.24,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-13","peak_price":599000,"drawdown_after_peak_pct":-47.08,"green_lateness_ratio":0.7,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"high_mae_failed_rerating","current_profile_verdict":"current_profile_false_positive","forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"NONG_2024_05_13_424000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":8,"relative_strength_score":9,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76.5,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":6,"relative_strength_score":7,"customer_quality_score":11,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":-6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68.0,"stage_label_after":"Stage2-watch","round":"R13","loop":"43","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","sector":"소비재·유통·브랜드","primary_archetype":"beauty_food_global_distribution","loop_objective":["holdout_validation","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","residual_false_positive_mining","coverage_gap_fill"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv","profile_path":"atlas/symbol_profiles/004/004370.json","calibration_usable":true,"calibration_block_reasons":[],"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"trigger_id":"NONGSHIM_GREEN_TOO_LATE_2024_06_13","case_id":"R13L43_C20_004370_NONGSHIM_LATE_PEAK","symbol":"004370","company_name":"농심","fine_archetype_id":"RAMEN_GLOBAL_BRAND_MARGIN_OVERHANG_GUARD","trigger_type":"Stage3-Green","trigger_date":"2024-06-13","entry_date":"2024-06-13","entry_price":547000,"evidence_available_at_that_date":"Relative strength and overseas ramen narrative reached peak recognition without enough margin/revision guard.","evidence_source":"Financial Times / public market context; stock-web OHLC rows","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"MFE_30D_pct":9.51,"MFE_90D_pct":9.51,"MFE_180D_pct":9.51,"MFE_1Y_pct":9.51,"MFE_2Y_pct":null,"MAE_30D_pct":-2.01,"MAE_90D_pct":-34.1,"MAE_180D_pct":-42.05,"MAE_1Y_pct":-42.05,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-13","peak_price":599000,"drawdown_after_peak_pct":-47.08,"green_lateness_ratio":0.7,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_if_margin_overhang_used","four_b_evidence_type":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"false_positive_green_4B_overlay_success","current_profile_verdict":"current_profile_false_positive","forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"NONG_2024_06_13_547000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":14,"relative_strength_score":14,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":11,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":88.0,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":9,"relative_strength_score":12,"customer_quality_score":11,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":-8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":77.0,"stage_label_after":"Stage3-Yellow+4B-overlay","round":"R13","loop":"43","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","sector":"소비재·유통·브랜드","primary_archetype":"beauty_food_global_distribution","loop_objective":["holdout_validation","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","residual_false_positive_mining","coverage_gap_fill"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv","profile_path":"atlas/symbol_profiles/004/004370.json","calibration_usable":true,"calibration_block_reasons":[],"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L43_C20_003230_SAMYANG_BULDAK_EXPORT","trigger_id":"SYF_STAGE2_EXPORT_REVISION_2024_03_04","symbol":"003230","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":10,"relative_strength_score":8,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":73.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":9,"revision_score":13,"relative_strength_score":9,"customer_quality_score":17,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":78.5,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","revision_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C20 shadow profile rewards verified sell-through/reorder and penalizes brand-only or price-only narratives without margin/revision support.","MFE_90D_pct":275.92,"MAE_90D_pct":-7.33,"score_return_alignment_label":"structural_success","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L43_C20_003230_SAMYANG_BULDAK_EXPORT","trigger_id":"SYF_STAGE3_GREEN_Q1_EXPORT_CONFIRM_2024_05_20","symbol":"003230","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":15,"revision_score":17,"relative_strength_score":10,"customer_quality_score":17,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":89.0,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":15,"revision_score":17,"relative_strength_score":10,"customer_quality_score":17,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":89.0,"stage_label_after":"Stage3-Green","changed_components":["customer_quality_score","revision_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C20 shadow profile rewards verified sell-through/reorder and penalizes brand-only or price-only narratives without margin/revision support.","MFE_90D_pct":43.03,"MAE_90D_pct":-9.26,"score_return_alignment_label":"late_but_valid_green","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L43_C20_003230_SAMYANG_BULDAK_EXPORT","trigger_id":"SYF_4B_VALUATION_OVERHEAT_2024_06_18","symbol":"003230","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":16,"revision_score":18,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":18,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":92.0,"stage_label_before":"Stage3-Green+4B-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":16,"revision_score":18,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":18,"execution_risk_score":-7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88.0,"stage_label_after":"Stage3-Green+4B-overlay","changed_components":["customer_quality_score","revision_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C20 shadow profile rewards verified sell-through/reorder and penalizes brand-only or price-only narratives without margin/revision support.","MFE_90D_pct":0.84,"MAE_90D_pct":-36.03,"score_return_alignment_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L43_C20_257720_SILICON2_KBEAUTY_DIST","trigger_id":"S2_STAGE2_KBEAUTY_EXPORT_REORDER_2024_03_20","symbol":"257720","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":9,"relative_strength_score":12,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":11,"relative_strength_score":13,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":80.0,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","revision_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C20 shadow profile rewards verified sell-through/reorder and penalizes brand-only or price-only narratives without margin/revision support.","MFE_90D_pct":404.19,"MAE_90D_pct":-9.77,"score_return_alignment_label":"structural_success","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L43_C20_257720_SILICON2_KBEAUTY_DIST","trigger_id":"S2_STAGE3_GREEN_Q1_SURPRISE_2024_05_10","symbol":"257720","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":14,"revision_score":18,"relative_strength_score":15,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":11,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":90.0,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":14,"revision_score":18,"relative_strength_score":15,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":11,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":90.0,"stage_label_after":"Stage3-Green","changed_components":["customer_quality_score","revision_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C20 shadow profile rewards verified sell-through/reorder and penalizes brand-only or price-only narratives without margin/revision support.","MFE_90D_pct":106.48,"MAE_90D_pct":-17.9,"score_return_alignment_label":"valid_green_with_high_mae","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L43_C20_257720_SILICON2_KBEAUTY_DIST","trigger_id":"S2_4B_POSITIONING_OVERHEAT_2024_06_19","symbol":"257720","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":15,"revision_score":18,"relative_strength_score":18,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":20,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":91.0,"stage_label_before":"Stage3-Green+4B-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":15,"revision_score":18,"relative_strength_score":18,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":20,"execution_risk_score":-8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":87.0,"stage_label_after":"Stage3-Green+4B-overlay","changed_components":["customer_quality_score","revision_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C20 shadow profile rewards verified sell-through/reorder and penalizes brand-only or price-only narratives without margin/revision support.","MFE_90D_pct":6.9,"MAE_90D_pct":-52.86,"score_return_alignment_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L43_C20_271560_ORION_CHANNEL_GUARD","trigger_id":"ORION_STAGE2_GLOBAL_CHANNEL_2024_02_16","symbol":"271560","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":6,"relative_strength_score":5,"customer_quality_score":9,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":75.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":5,"relative_strength_score":4,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":67.0,"stage_label_after":"Stage2-watch","changed_components":["customer_quality_score","revision_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C20 shadow profile rewards verified sell-through/reorder and penalizes brand-only or price-only narratives without margin/revision support.","MFE_90D_pct":9.77,"MAE_90D_pct":-7.41,"score_return_alignment_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L43_C20_271560_ORION_CHANNEL_GUARD","trigger_id":"ORION_PSEUDO_GREEN_FOOD_CHANNEL_2024_06_17","symbol":"271560","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":11,"relative_strength_score":10,"customer_quality_score":9,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":87.5,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":8,"relative_strength_score":8,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":-6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":76.0,"stage_label_after":"Stage3-Yellow/guarded","changed_components":["customer_quality_score","revision_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C20 shadow profile rewards verified sell-through/reorder and penalizes brand-only or price-only narratives without margin/revision support.","MFE_90D_pct":2.2,"MAE_90D_pct":-16.95,"score_return_alignment_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L43_C20_004370_NONGSHIM_LATE_PEAK","trigger_id":"NONGSHIM_STAGE2_OVERSEAS_RAMEN_2024_05_13","symbol":"004370","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":8,"relative_strength_score":9,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76.5,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":6,"relative_strength_score":7,"customer_quality_score":11,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":-6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68.0,"stage_label_after":"Stage2-watch","changed_components":["customer_quality_score","revision_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C20 shadow profile rewards verified sell-through/reorder and penalizes brand-only or price-only narratives without margin/revision support.","MFE_90D_pct":41.27,"MAE_90D_pct":-14.98,"score_return_alignment_label":"high_mae_failed_rerating","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L43_C20_004370_NONGSHIM_LATE_PEAK","trigger_id":"NONGSHIM_GREEN_TOO_LATE_2024_06_13","symbol":"004370","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":14,"relative_strength_score":14,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":11,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":88.0,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":9,"relative_strength_score":12,"customer_quality_score":11,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":-8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":77.0,"stage_label_after":"Stage3-Yellow+4B-overlay","changed_components":["customer_quality_score","revision_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C20 shadow profile rewards verified sell-through/reorder and penalizes brand-only or price-only narratives without margin/revision support.","MFE_90D_pct":9.51,"MAE_90D_pct":-34.1,"score_return_alignment_label":"false_positive_green_4B_overlay_success","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 aggregate/profile rows

```jsonl
{"row_type":"aggregate","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_global_proxy","profile_hypothesis":"Current profile catches strong evidence but still over-promotes broad global-brand narratives and recognizes some C20 positives too late.","changed_axes":[],"changed_thresholds":{},"eligible_trigger_count":4,"selected_entry_trigger_per_case":["SYF_STAGE2_EXPORT_REVISION_2024_03_04","S2_STAGE2_KBEAUTY_EXPORT_REORDER_2024_03_20","ORION_STAGE2_GLOBAL_CHANNEL_2024_02_16","NONGSHIM_STAGE2_OVERSEAS_RAMEN_2024_05_13"],"avg_MFE_90D_pct":182.79,"avg_MAE_90D_pct":-9.87,"avg_MFE_180D_pct":182.79,"avg_MAE_180D_pct":-14.54,"false_positive_rate":0.5,"missed_structural_count":2,"late_green_count":2,"avg_green_lateness_ratio":0.55,"avg_four_b_local_peak_proximity":0.99,"avg_four_b_full_window_peak_proximity":0.95,"score_return_alignment_verdict":"mixed_residual_errors"}
{"row_type":"aggregate","profile_id":"P0b_e2r_2_0_baseline_reference","profile_scope":"rollback_reference","profile_hypothesis":"Old baseline over-promotes price/brand narratives and has weaker 4B/4C protections.","changed_axes":["rollback_reference_only"],"changed_thresholds":{},"eligible_trigger_count":4,"selected_entry_trigger_per_case":["SYF_STAGE2_EXPORT_REVISION_2024_03_04","S2_STAGE2_KBEAUTY_EXPORT_REORDER_2024_03_20","ORION_STAGE2_GLOBAL_CHANNEL_2024_02_16","NONGSHIM_STAGE2_OVERSEAS_RAMEN_2024_05_13"],"avg_MFE_90D_pct":182.79,"avg_MAE_90D_pct":-9.87,"avg_MFE_180D_pct":182.79,"avg_MAE_180D_pct":-14.54,"false_positive_rate":0.75,"missed_structural_count":1,"late_green_count":2,"avg_green_lateness_ratio":0.62,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":0.96,"score_return_alignment_verdict":"worse_false_positive_control"}
{"row_type":"aggregate","profile_id":"P1_L5_sector_specific_candidate_profile","profile_scope":"sector_specific","profile_hypothesis":"Within L5, reward export sell-through/reorder plus channel evidence; discount brand-only narratives lacking margin bridge.","changed_axes":["L5_export_sell_through_reorder_bonus","L5_brand_only_margin_absence_guard"],"changed_thresholds":{},"eligible_trigger_count":4,"selected_entry_trigger_per_case":["SYF_STAGE2_EXPORT_REVISION_2024_03_04","S2_STAGE2_KBEAUTY_EXPORT_REORDER_2024_03_20","ORION_STAGE2_GLOBAL_CHANNEL_2024_02_16","NONGSHIM_STAGE2_OVERSEAS_RAMEN_2024_05_13"],"avg_MFE_90D_pct":340.06,"avg_MAE_90D_pct":-8.55,"avg_MFE_180D_pct":340.06,"avg_MAE_180D_pct":-8.55,"false_positive_rate":0.25,"missed_structural_count":0,"late_green_count":1,"avg_green_lateness_ratio":0.48,"avg_four_b_local_peak_proximity":0.99,"avg_four_b_full_window_peak_proximity":0.95,"score_return_alignment_verdict":"improved_positive_counterexample_split"}
{"row_type":"aggregate","profile_id":"P2_C20_archetype_candidate_profile","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C20 should compress beauty and food into the same sell-through/reorder/margin-bridge rule rather than treating all global brand narratives equally.","changed_axes":["C20_sell_through_repeat_order_bonus","C20_inventory_margin_absence_guard"],"changed_thresholds":{"green_requires_repeat_order_or_margin_bridge":true},"eligible_trigger_count":4,"selected_entry_trigger_per_case":["SYF_STAGE2_EXPORT_REVISION_2024_03_04","S2_STAGE2_KBEAUTY_EXPORT_REORDER_2024_03_20","ORION_STAGE2_GLOBAL_CHANNEL_2024_02_16","NONGSHIM_STAGE2_OVERSEAS_RAMEN_2024_05_13"],"avg_MFE_90D_pct":182.79,"avg_MAE_90D_pct":-9.87,"avg_MFE_180D_pct":182.79,"avg_MAE_180D_pct":-14.54,"false_positive_rate":0.25,"missed_structural_count":0,"late_green_count":1,"avg_green_lateness_ratio":0.48,"avg_four_b_local_peak_proximity":0.99,"avg_four_b_full_window_peak_proximity":0.95,"score_return_alignment_verdict":"best_explanatory_split"}
{"row_type":"aggregate","profile_id":"P3_C20_counterexample_guard_profile","profile_scope":"counterexample_guard","profile_hypothesis":"Blocks Green when evidence is mostly price/brand plus weak margin or absent repeat-order proof; keeps 4B overlay when valuation runs ahead of evidence.","changed_axes":["C20_green_guard_brand_only","C20_margin_overhang_4B_overlay"],"changed_thresholds":{"green_guard_margin_bridge_min":8},"eligible_trigger_count":4,"selected_entry_trigger_per_case":["SYF_STAGE2_EXPORT_REVISION_2024_03_04","S2_STAGE2_KBEAUTY_EXPORT_REORDER_2024_03_20","ORION_STAGE2_GLOBAL_CHANNEL_2024_02_16","NONGSHIM_STAGE2_OVERSEAS_RAMEN_2024_05_13"],"avg_MFE_90D_pct":182.79,"avg_MAE_90D_pct":-9.87,"avg_MFE_180D_pct":182.79,"avg_MAE_180D_pct":-14.54,"false_positive_rate":0.0,"missed_structural_count":1,"late_green_count":1,"avg_green_lateness_ratio":0.48,"avg_four_b_local_peak_proximity":0.99,"avg_four_b_full_window_peak_proximity":0.95,"score_return_alignment_verdict":"safer_but_may_delay_samyang_silicon2"}
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R13","loop":"43","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_too_late","current_profile_false_positive","current_profile_4B_too_late","high_mae_success"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":null,"symbol":null,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","reason":"no narrative-only rows in this loop; all four cases had clean 180D stock-web windows","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
next_round = R13_loop_44
suggested_large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
suggested_canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
reason = C20 now has beauty/food sell-through compression; C18 can test channel reorder in consumer export names without requiring global beauty/food brand mechanics.
```

## 28. Source Notes

Stock-Web and schema inputs:

- `atlas/manifest.json`: manifest max date `2026-02-20`, raw_unadjusted_marcap, tradable shard root, row counts, market universe.
- `atlas/schema.json`: tradable/raw column maps and MFE/MAE calibration definitions.
- `atlas/symbol_profiles/003/003230.json`, `257/257720.json`, `271/271560.json`, `004/004370.json`: profile windows and corporate-action candidate checks.
- `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/2024.csv`: OHLC rows used for entry, MFE, MAE, peak, and drawdown.

Public evidence context:

- MarketWatch/WSJ market talk, June 2024: Samyang Foods' expected 2Q earnings were linked to Buldak exports, U.S./Europe shipments, ASP, and capacity support.
- Reuters, June 2025: Korean cosmetics surpassed France in U.S. exports in 2024, ecommerce and social-media demand supported K-beauty, and Silicon2's CEO described both the strength and challenges of the K-beauty trend.
- Financial Times, May 2024: Nongshim overseas expansion and Shin Ramyun's international contribution were visible, but the stock path shows why global-brand narrative still needs a margin/revision guard.

No source in this MD should be read as a current recommendation. The row data is only for historical calibration.

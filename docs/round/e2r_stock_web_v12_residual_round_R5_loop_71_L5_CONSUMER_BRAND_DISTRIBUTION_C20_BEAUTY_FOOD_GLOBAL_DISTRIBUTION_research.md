# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
round = R5
loop = 71
scheduled_round = R5
scheduled_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
schedule_source = previous_generated_md_next_round_state
completed_previous_round = R4
completed_previous_loop = 71
next_round_after_this_md = R6
next_loop_after_this_md = 71
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_US_PHYSICAL_RETAIL_GLOBAL_DISTRIBUTION_VS_LEGACY_BRAND_PLATEAU
loop_objective = coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R5_loop_71_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
```

## 1. Current Calibrated Profile Assumption

```text
before_profile_id = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
production_scoring_changed = false
shadow_weight_only = true
```

Already-applied global axes are treated as baseline, not re-proposed globally:

```text
stage2_actionable_evidence_bonus
stage3_yellow_total_min
stage3_green_total_min
stage3_green_revision_min
stage3_cross_evidence_green_buffer
price_only_blowoff_blocks_positive_stage
full_4b_requires_non_price_evidence
hard_4c_thesis_break_routes_to_4c
```

## 2. Round / Large Sector / Canonical Archetype Scope

R5 hard-gates to `L5_CONSUMER_BRAND_DISTRIBUTION`. This run uses:

```text
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_US_PHYSICAL_RETAIL_GLOBAL_DISTRIBUTION_VS_LEGACY_BRAND_PLATEAU
```

The canonical compression target is not "K-beauty headline = Green." It is:

```text
K-beauty global distribution / US shelf expansion
→ ODM or distribution exposure gets Stage2 credit
→ legacy brand plateau and tariff/physical-channel execution risk block Green
→ full-window 4B should activate after local peak when non-price risk is already visible
```

## 3. Previous Coverage / Duplicate Avoidance Check

`V12_Research_No_Repeat_Index.md` snapshot says `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION` already has 133 rows, 16 symbols, `good/bad S2 = 47/8`, `4B/4C = 11/5`, and top covered symbols include `257720`, `018290`, `003230`, `090430`, and `237880`.

Duplicate policy applied:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
no key reused from the No-Repeat examples
same canonical allowed
same symbol allowed only with new trigger family / new entry date / counterexample purpose
```

Selected novelty:

```text
new symbols in this C20 loop:
- 192820 코스맥스
- 161890 한국콜마

same canonical but new trigger family:
- 090430 아모레퍼시픽: 2025 US K-beauty plateau / COSRX competition trigger, not the prior 2024 C20 rerating rows
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest facts used in this run:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
```

Per-symbol profile checks:

| symbol | company | profile_path | corporate_action_candidate_dates | 180D status |
|---|---|---|---|---|
| 192820 | 코스맥스 | `atlas/symbol_profiles/192/192820.json` | none | clean |
| 161890 | 한국콜마 | `atlas/symbol_profiles/161/161890.json` | none | clean |
| 090430 | 아모레퍼시픽 | `atlas/symbol_profiles/090/090430.json` | 2015-05-08 only | clean for 2025-06-05~D+180 |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward_window_trading_days | 180D clean | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R5L71-C20-01 | 192820 | 2025-06-05 | 224500 | 180 | yes | true |
| R5L71-C20-02 | 161890 | 2025-06-05 | 85000 | 180 | yes | true |
| R5L71-C20-03 | 090430 | 2025-06-05 | 137300 | 180 | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep path | Stage2 bridge | Green blocker | 4B/4C use |
|---|---|---|---|---|
| C20 | ODM manufacturer exposure | US shelf expansion + outsourcing to Cosmax/Kolmar | tariff, physical retail execution, competition, plateau risk | full-window 4B watch after local peak |
| C20 | legacy brand / acquired brand plateau | K-beauty headline only | no direct repeat-order / margin / revision bridge | counterexample / Watch |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger | why selected |
|---|---:|---|---|---|---|
| R5L71-C20-01 | 192820 | 코스맥스 | positive + 4B audit | Reuters 2025-06-05 K-beauty US expansion / ODM outsourcing | new symbol in C20 context; strong 30D/90D MFE but later severe drawdown |
| R5L71-C20-02 | 161890 | 한국콜마 | positive + 4B audit | Reuters 2025-06-05 K-beauty US expansion / ODM outsourcing | new symbol in C20 context; strong 30D/90D MFE but later severe drawdown |
| R5L71-C20-03 | 090430 | 아모레퍼시픽 | counterexample | Reuters 2025-06-05 COSRX plateau / competition note | same broad K-beauty headline, weaker direct channel/ODM translation |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 4
```

This loop meets the minimum positive/counterexample balance. It should not loosen Green. Its useful signal is narrower: C20 Stage2 can credit US shelf/channel/ODM evidence, but C20 needs faster 4B watch once local peak appears while tariff/physical-channel risk remains open.

## 9. Evidence Source Map

| evidence_date | source | usable_at_trigger | what it supports |
|---|---|---|---|
| 2025-06-05 | Reuters, “Korean beauty startups bet booming US demand outlasts tariff pain” | yes | US shelf expansion, Sephora/Ulta/Target/Costco talks, Cosmax/Kolmar outsourcing model, Korea replacing France as top US cosmetics exporter in 2024, COSRX plateau warning |
| 2025-07-25 | AP, “Tariffs on South Korea's products threaten the K-beauty boom in the US” | risk cross-check only | confirms tariff pressure and US-import dependency; not used to set the 2025-06-05 entry |

Source URLs:

```text
https://www.reuters.com/world/asia-pacific/korean-beauty-startups-bet-booming-us-demand-outlasts-tariff-pain-2025-06-05/
https://apnews.com/article/77e528d9b0011034bcf593ba056b4077
```

## 10. Price Data Source Map

| symbol | 2025 shard | 2026 shard | profile |
|---|---|---|---|
| 192820 | `atlas/ohlcv_tradable_by_symbol_year/192/192820/2025.csv` | `atlas/ohlcv_tradable_by_symbol_year/192/192820/2026.csv` | `atlas/symbol_profiles/192/192820.json` |
| 161890 | `atlas/ohlcv_tradable_by_symbol_year/161/161890/2025.csv` | `atlas/ohlcv_tradable_by_symbol_year/161/161890/2026.csv` | `atlas/symbol_profiles/161/161890.json` |
| 090430 | `atlas/ohlcv_tradable_by_symbol_year/090/090430/2025.csv` | `atlas/ohlcv_tradable_by_symbol_year/090/090430/2026.csv` | `atlas/symbol_profiles/090/090430.json` |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | type | trigger_date | entry_date | entry_price | representative | role |
|---|---:|---|---|---|---:|---|---|
| R5L71-C20-01-T1 | 192820 | Stage2-Actionable | 2025-06-05 | 2025-06-05 | 224500 | true | positive structural ODM rerating |
| R5L71-C20-01-T2 | 192820 | Stage4B | 2025-06-25 | 2025-06-25 | 282000 | false | 4B overlay timing |
| R5L71-C20-02-T1 | 161890 | Stage2-Actionable | 2025-06-05 | 2025-06-05 | 85000 | true | positive structural ODM rerating |
| R5L71-C20-03-T1 | 090430 | Stage2-Watch | 2025-06-05 | 2025-06-05 | 137300 | true | counterexample / legacy plateau |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---|---:|---:|
| R5L71-C20-01-T1 | 27.84 | -1.34 | 27.84 | -15.90 | 27.84 | -30.87 | 2025-06-25 | 287000 | -45.92 |
| R5L71-C20-01-T2 | 1.77 | -16.67 | 1.77 | -33.05 | 1.77 | -44.96 | 2025-06-25 | 287000 | -45.92 |
| R5L71-C20-02-T1 | 30.24 | -0.82 | 30.24 | -12.71 | 30.24 | -27.41 | 2025-07-16 | 110700 | -44.26 |
| R5L71-C20-03-T1 | 8.01 | -5.32 | 8.01 | -15.37 | 23.09 | -15.37 | 2026-02-09 | 169000 | -8.11 |

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely action | actual path | verdict |
|---|---|---|---|
| R5L71-C20-01 | Stage2-Actionable, later 4B only after evidence deterioration | 27.84% MFE then -30.87% MAE180 | current_profile_4B_too_late |
| R5L71-C20-02 | Stage2-Actionable, later 4B only after evidence deterioration | 30.24% MFE then -27.41% MAE180 | current_profile_4B_too_late |
| R5L71-C20-03 | broad K-beauty headline could over-promote | 90D MFE only 8.01%, below-entry path | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is asserted in this loop. Green is intentionally withheld.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

Interpretation:

```text
C20 K-beauty US shelf / global distribution evidence can create Stage2, but Green requires company-specific repeat-order, margin bridge, and revision confirmation.
```

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---:|---:|---|
| R5L71-C20-01-T2 | 0.92 | 0.92 | good_full_window_4B_timing |

The 4B overlay is not price-only. It attaches to non-price risks already visible in the 2025-06-05 evidence pack: tariff pain, physical-store execution requirement, and competition/plateau risk.

## 16. 4C Protection Audit

No hard 4C is proposed. The observed drawdowns are large, but the thesis did not have a single disclosed cancellation, regulatory rejection, or accounting/trust break in the available evidence set.

```text
four_c_protection_label = thesis_break_watch_only
```

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
candidate = L5 K-beauty distribution Stage2 requires non-price channel/ODM evidence; do not promote legacy K-beauty headline to Green without company-specific revision/margin bridge.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
candidate_axis = C20_channel_reorder_plus_4B_watch_guard
proposal = Stage2 credit is allowed for US shelf/channel/ODM evidence, but full-window 4B watch should activate near local peak when tariff/physical-channel/competition risk is already visible.
new_axis_proposed = null
existing_axis_strengthened = full_4b_requires_non_price_evidence; price_only_blowoff_blocks_positive_stage
```

## 19. Before / After Backtest Comparison

| profile | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive rate | verdict |
|---|---:|---:|---:|---:|---:|---|
| P0 current proxy | 22.03 | -14.66 | 27.06 | -24.55 | 0.333 | Stage2 useful, but 4B too late |
| P2 C20 archetype candidate | 22.03 | -14.66 | 27.06 | -24.55 | 0.333 | Same entries, better label discipline: Stage2 yes, Green no, 4B watch earlier |

## 20. Score-Return Alignment Matrix

| component | positive ODM cases | legacy/plateau counterexample | interpretation |
|---|---|---|---|
| channel_reorder_score | high | medium | US shelf/channel matters only when company monetizes it directly |
| customer_quality_score | high | mixed | ODM outsourcing creates clearer customer route than broad legacy brand ownership |
| margin_bridge_score | medium | low | Green needs margin/revision evidence, not just export headline |
| execution_risk_score | medium-high risk | high risk | tariff and physical shelf conversion are 4B watch inputs |
| valuation_repricing_score | initially high | insufficient | rerating without repeat-order bridge becomes false positive risk |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new_independent | reused | usable_triggers | representative |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_BEAUTY_US_PHYSICAL_RETAIL_GLOBAL_DISTRIBUTION_VS_LEGACY_BRAND_PLATEAU | 2 | 1 | 1 | 0 | 3 | 0 | 4 | 3 |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 2
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- full_4b_requires_non_price_evidence
- price_only_blowoff_blocks_positive_stage
residual_error_types_found:
- current_profile_4B_too_late
- current_profile_false_positive
new_axis_proposed: null
existing_axis_strengthened:
- full_4b_requires_non_price_evidence
- price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
existing_axis_kept:
- stage2_actionable_evidence_bonus
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

One-line contribution:

```text
This loop adds 3 new independent cases, 1 counterexample, and 3 residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION.
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- stock-web tradable OHLC rows
- 2025/2026 shards for 192820, 161890, 090430
- symbol profiles and corporate-action candidate dates
- Reuters 2025-06-05 evidence available at trigger date
```

Non-validation scope:

```text
- no live candidate scan
- no production scoring patch
- no brokerage/API/trading action
- no future data used to assign trigger label
- AP tariff article used only as later risk cross-check, not as trigger-date entry evidence
```

## 24. Shadow Weight Calibration

```text
rule_scope = canonical_archetype_specific
candidate_axis = C20_channel_reorder_plus_4B_watch_guard
application_scope = sector_shadow_only
promotion_decision = hold_for_batch_calibration
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R5L71-C20-01","symbol":"192820","company_name":"코스맥스","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_PHYSICAL_RETAIL_GLOBAL_DISTRIBUTION_VS_LEGACY_BRAND_PLATEAU","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_90D_but_requires_4B_overlay","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Reuters가 K-beauty indie brand의 US shelf expansion과 Cosmax/Kolmar 같은 ODM outsourcing model을 언급한 날, stock-web상 초기 30D/90D MFE는 강했지만 이후 180D MAE가 커져 4B overlay가 필요했다."}
{"row_type":"case","case_id":"R5L71-C20-02","symbol":"161890","company_name":"한국콜마","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_PHYSICAL_RETAIL_GLOBAL_DISTRIBUTION_VS_LEGACY_BRAND_PLATEAU","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_90D_but_requires_4B_overlay","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"K-beauty global distribution theme가 ODM leverage로 번역된 positive case. 하지만 90D 이후 수익률이 급격히 훼손되어 full-window 4B non-price requirement를 강화하는 근거가 된다."}
{"row_type":"case","case_id":"R5L71-C20-03","symbol":"090430","company_name":"아모레퍼시픽","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_PHYSICAL_RETAIL_GLOBAL_DISTRIBUTION_VS_LEGACY_BRAND_PLATEAU","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Watch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same_canonical_symbol_previously_seen_but_new_2025_US_K_beauty_plateau_trigger_family","independent_evidence_weight":0.5,"score_price_alignment":"legacy_brand_plateau_counterexample_90D_failed_later_rescue_not_green_quality","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Reuters가 COSRX plateau risk를 AmorePacific과 연결해 언급했다. 같은 K-beauty headline이라도 legacy/plateau exposure는 90D rerating quality가 약했다."}
{"row_type":"trigger","trigger_id":"R5L71-C20-01-T1","case_id":"R5L71-C20-01","symbol":"192820","company_name":"코스맥스","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_PHYSICAL_RETAIL_GLOBAL_DISTRIBUTION_VS_LEGACY_BRAND_PLATEAU","sector":"consumer brand distribution","primary_archetype":"K-beauty global distribution and US retail/channel reorder","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2025-06-05","evidence_available_at_that_date":"Reuters: K-beauty startups expand US shelves; brands outsource production to Cosmax/Kolmar; Korea became the largest US cosmetics exporter in 2024; ecommerce/Amazon channel drove gains.","evidence_source":"Reuters 2025-06-05; AP 2025-07 tariff context used only as risk cross-check","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["multiple_public_sources","repeat_order_or_conversion"],"stage4b_evidence_fields":["tariff_or_physical_shelf_execution_risk","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/192/192820/2025.csv","profile_path":"atlas/symbol_profiles/192/192820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-06-05","entry_price":224500,"MFE_30D_pct":27.84,"MFE_90D_pct":27.84,"MFE_180D_pct":27.84,"MFE_1Y_pct":"contaminated_or_unavailable","MFE_2Y_pct":"contaminated_or_unavailable","MAE_30D_pct":-1.34,"MAE_90D_pct":-15.9,"MAE_180D_pct":-30.87,"MAE_1Y_pct":"contaminated_or_unavailable","below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2025-06-25","peak_price":287000,"drawdown_after_peak_pct":-45.92,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_stage2_trigger","four_b_evidence_type":null,"four_c_protection_label":"not_applicable","trigger_outcome_label":"good_stage2_high_mae_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_no_overlap","same_entry_group_id":"R5L71-C20-01:2025-06-05:224500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L71-C20-01-T2","case_id":"R5L71-C20-01","symbol":"192820","company_name":"코스맥스","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_PHYSICAL_RETAIL_GLOBAL_DISTRIBUTION_VS_LEGACY_BRAND_PLATEAU","sector":"consumer brand distribution","primary_archetype":"K-beauty global distribution and US retail/channel reorder","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2025-06-25","evidence_available_at_that_date":"Non-price risk already visible in the same Reuters evidence set: tariffs, physical retail execution, and saturation/plateau risk; price then reached local peak.","evidence_source":"Reuters 2025-06-05; AP 2025-07 tariff context used only as risk cross-check","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","tariff_or_physical_shelf_execution_risk"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/192/192820/2025.csv","profile_path":"atlas/symbol_profiles/192/192820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-06-25","entry_price":282000,"MFE_30D_pct":1.77,"MFE_90D_pct":1.77,"MFE_180D_pct":1.77,"MFE_1Y_pct":"contaminated_or_unavailable","MFE_2Y_pct":"contaminated_or_unavailable","MAE_30D_pct":-16.67,"MAE_90D_pct":-33.05,"MAE_180D_pct":-44.96,"MAE_1Y_pct":"contaminated_or_unavailable","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-25","peak_price":287000,"drawdown_after_peak_pct":-45.92,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":0.92,"four_b_full_window_peak_proximity":0.92,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":"valuation_blowoff|positioning_overheat|tariff_or_physical_shelf_execution_risk","four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_no_overlap","same_entry_group_id":"R5L71-C20-01:2025-06-25:282000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same_case_overlay_not_representative","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R5L71-C20-02-T1","case_id":"R5L71-C20-02","symbol":"161890","company_name":"한국콜마","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_PHYSICAL_RETAIL_GLOBAL_DISTRIBUTION_VS_LEGACY_BRAND_PLATEAU","sector":"consumer brand distribution","primary_archetype":"K-beauty global distribution and US retail/channel reorder","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2025-06-05","evidence_available_at_that_date":"Reuters: Korean brands outsource production to Cosmax and Kolmar; Korean brands seek Sephora/Ulta/Target/Costco shelf expansion.","evidence_source":"Reuters 2025-06-05; AP 2025-07 tariff context used only as risk cross-check","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["multiple_public_sources","repeat_order_or_conversion"],"stage4b_evidence_fields":["tariff_or_physical_shelf_execution_risk","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/161/161890/2025.csv","profile_path":"atlas/symbol_profiles/161/161890.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-06-05","entry_price":85000,"MFE_30D_pct":30.24,"MFE_90D_pct":30.24,"MFE_180D_pct":30.24,"MFE_1Y_pct":"contaminated_or_unavailable","MFE_2Y_pct":"contaminated_or_unavailable","MAE_30D_pct":-0.82,"MAE_90D_pct":-12.71,"MAE_180D_pct":-27.41,"MAE_1Y_pct":"contaminated_or_unavailable","below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2025-07-16","peak_price":110700,"drawdown_after_peak_pct":-44.26,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_stage2_trigger","four_b_evidence_type":null,"four_c_protection_label":"not_applicable","trigger_outcome_label":"good_stage2_high_mae_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_no_overlap","same_entry_group_id":"R5L71-C20-02:2025-06-05:85000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L71-C20-03-T1","case_id":"R5L71-C20-03","symbol":"090430","company_name":"아모레퍼시픽","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_PHYSICAL_RETAIL_GLOBAL_DISTRIBUTION_VS_LEGACY_BRAND_PLATEAU","sector":"consumer brand distribution","primary_archetype":"K-beauty global distribution and US retail/channel reorder","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression","trigger_type":"Stage2-Watch","trigger_date":"2025-06-05","evidence_available_at_that_date":"Reuters: COSRX, now part of AmorePacific, showed signs of growth plateauing as competition heats up and cheaper alternatives emerge.","evidence_source":"Reuters 2025-06-05; AP 2025-07 tariff context used only as risk cross-check","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/090/090430/2025.csv","profile_path":"atlas/symbol_profiles/090/090430.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-06-05","entry_price":137300,"MFE_30D_pct":8.01,"MFE_90D_pct":8.01,"MFE_180D_pct":23.09,"MFE_1Y_pct":"contaminated_or_unavailable","MFE_2Y_pct":"contaminated_or_unavailable","MAE_30D_pct":-5.32,"MAE_90D_pct":-15.37,"MAE_180D_pct":-15.37,"MAE_1Y_pct":"contaminated_or_unavailable","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2026-02-09","peak_price":169000,"drawdown_after_peak_pct":-8.11,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_watch_counterexample","four_b_evidence_type":null,"four_c_protection_label":"not_applicable","trigger_outcome_label":"counterexample_90D_failed_later_rescue","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_no_overlap","same_entry_group_id":"R5L71-C20-03:2025-06-05:137300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same_canonical_symbol_previously_seen_but_new_2025_US_K_beauty_plateau_trigger_family","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","round":"R5","loop":"71","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_proxy","profile_hypothesis":"global Stage2 evidence bonus helps C20 but misses full-window 4B after K-beauty blowoff","changed_axes":["existing_axis_tested:stage2_actionable_evidence_bonus","existing_axis_tested:full_4b_requires_non_price_evidence"],"eligible_trigger_count":3,"selected_entry_trigger_per_case":["R5L71-C20-01-T1","R5L71-C20-02-T1","R5L71-C20-03-T1"],"avg_MFE_90D_pct":22.03,"avg_MAE_90D_pct":-14.66,"avg_MFE_180D_pct":27.06,"avg_MAE_180D_pct":-24.55,"false_positive_rate":0.333,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":0.92,"avg_four_b_full_window_peak_proximity":0.92,"score_return_alignment_verdict":"Stage2 useful but 4B watch should activate once ODM/distribution names overshoot while tariff/physical-channel risks remain open","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":45,"margin_bridge_score":55,"revision_score":50,"relative_strength_score":70,"customer_quality_score":75,"policy_or_regulatory_score":55,"valuation_repricing_score":68,"execution_risk_score":45,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable/Yellow watch","raw_component_scores_after":{"channel_reorder_score":80,"customer_quality_score":80,"execution_risk_score":60,"positioning_overheat_score":70},"weighted_score_after":75,"stage_label_after":"Stage2-Actionable with 4B watch guard","component_delta_explanation":"C20 should credit US shelf/channel reorder and ODM exposure, but once price reaches local peak with tariff/retail execution risk, 4B watch should not wait for earnings deterioration."}
{"row_type":"score_simulation","round":"R5","loop":"71","profile_id":"P2_C20_archetype_candidate_profile","profile_scope":"canonical_archetype_specific","profile_hypothesis":"K-beauty global distribution should weight channel reorder/customer quality higher and legacy-brand plateau lower","changed_axes":["existing_axis_strengthened:full_4b_requires_non_price_evidence","existing_axis_strengthened:price_only_blowoff_blocks_positive_stage"],"eligible_trigger_count":3,"selected_entry_trigger_per_case":["R5L71-C20-01-T1","R5L71-C20-02-T1","R5L71-C20-03-T1"],"avg_MFE_90D_pct":22.03,"avg_MAE_90D_pct":-14.66,"avg_MFE_180D_pct":27.06,"avg_MAE_180D_pct":-24.55,"false_positive_rate":0.333,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":0.92,"avg_four_b_full_window_peak_proximity":0.92,"score_return_alignment_verdict":"archetype-specific split improves positive/counterexample discrimination","raw_component_scores_before":{"channel_reorder_score":70,"customer_quality_score":70,"execution_risk_score":40,"valuation_repricing_score":65},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"channel_reorder_score":85,"customer_quality_score":82,"execution_risk_score":65,"valuation_repricing_score":58},"weighted_score_after":78,"stage_label_after":"Stage2-Actionable; 4B-watch after local peak","component_delta_explanation":"ODM names get channel/customer credit; legacy plateau name stays Watch unless repeat-order/revision confirms."}
{"row_type":"coverage_matrix","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_PHYSICAL_RETAIL_GLOBAL_DISTRIBUTION_VS_LEGACY_BRAND_PLATEAU","positive_case_count":2,"counterexample_count":1,"4B_case_count":1,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":4,"representative_trigger_count":3,"current_profile_error_count":3,"sector_rule_candidate":true,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C20 remains positive-heavy; this loop adds 2025 US physical-retail/tariff/legacy plateau differentiation."}
{"row_type":"shadow_weight","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_PHYSICAL_RETAIL_GLOBAL_DISTRIBUTION_VS_LEGACY_BRAND_PLATEAU","rule_scope":"canonical_archetype_specific","candidate_axis":"C20_channel_reorder_plus_4B_watch_guard","proposed_delta":"+0 to Stage2; strengthen 4B watch, not Green","supporting_case_ids":["R5L71-C20-01","R5L71-C20-02","R5L71-C20-03"],"positive_case_count":2,"counterexample_count":1,"4B_case_count":1,"risk_level":"medium","application_scope":"sector_shadow_only","notes":"Not a production patch; C20 already has broad coverage, so this row is a residual differentiation candidate."}
{"row_type":"residual_contribution","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":2,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 71
next_round = R6
next_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-web:

```text
https://github.com/Songdaiki/stock-web
atlas/manifest.json
atlas/schema.json
atlas/ohlcv_tradable_by_symbol_year/192/192820/2025.csv
atlas/ohlcv_tradable_by_symbol_year/192/192820/2026.csv
atlas/ohlcv_tradable_by_symbol_year/161/161890/2025.csv
atlas/ohlcv_tradable_by_symbol_year/161/161890/2026.csv
atlas/ohlcv_tradable_by_symbol_year/090/090430/2025.csv
atlas/ohlcv_tradable_by_symbol_year/090/090430/2026.csv
```

Evidence:

```text
Reuters, 2025-06-05, Korean beauty startups bet booming US demand outlasts tariff pain.
AP, 2025-07-25, Tariffs on South Korea's products threaten the K-beauty boom in the US.
```


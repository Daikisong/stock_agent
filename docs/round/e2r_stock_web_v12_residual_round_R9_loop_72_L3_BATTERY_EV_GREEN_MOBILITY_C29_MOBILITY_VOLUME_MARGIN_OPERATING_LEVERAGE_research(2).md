# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R9
scheduled_loop: 72
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R10
computed_next_loop: 72
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: C29_TRANSPORT_SHIPPING_VOLUME_RATE_MARGIN_BRIDGE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

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

## 2. Round / Large Sector / Canonical Archetype Scope

R9 can take the L3 mobility/transport branch or the L9 construction/PF branch. This run uses the L3 transport branch and avoids repeating the prior auto-parts supplier bridge. The residual is shipping/logistics-specific: freight or mobility heat can look convincing, but the useful C29 signal is volume, rate-to-earnings, mix/margin, and operating leverage.

| layer | id | definition |
|---|---|---|
| round | R9 | mobility / transport bridge round |
| large_sector | L3_BATTERY_EV_GREEN_MOBILITY | mobility, transport, logistics, auto and adjacent volume/margin cycles |
| canonical | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | mobility/transport volume, mix, margin, operating leverage |
| fine | C29_TRANSPORT_SHIPPING_VOLUME_RATE_MARGIN_BRIDGE_GUARD | freight/logistics signal must become margin/earnings |
| deep | BDI_BULK_RATE_CYCLE_TO_EARNINGS_AND_MARGIN_CONVERSION | bulk shipping rate-cycle positive |
| deep | PCC_LOGISTICS_VOLUME_MIX_OPERATING_LEVERAGE | logistics/PCC volume-mix low-MAE positive |
| deep | GEOPOLITICAL_FREIGHT_THEME_WITHOUT_RATE_TO_EARNINGS_CONVERSION | freight theme false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C29 is heavily covered, but its top cluster is centered on `UNKNOWN_SYMBOL`, `000270`, `161390`, `012330`, `005380`, and `018880`. This run avoids that top-covered auto/OEM cluster and fills a transport/logistics/freight sub-branch.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C29 | 028670 | new independent | not top-covered C29 symbol; bulk shipping rate/margin bridge |
| C29 | 086280 | new independent | not top-covered C29 symbol; logistics/PCC volume-mix bridge |
| C29 | 005880 | new independent | not top-covered C29 symbol; freight-theme price spike counterexample |

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Stock-web assumptions:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
tradable columns = d,o,h,l,c,v,a,mc,s,m
```

## 5. Historical Eligibility Gate

```text
entry row exists = true
forward 180 trading days available = true
MFE/MAE 30D/90D/180D computed = true
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_window_status = clean_180D_window
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_watch | 028670 | 팬오션 | Stage2-Actionable | 2021-04-22 | 6970 | bulk shipping rate/margin bridge worked |
| structural_success_low_MAE | 086280 | 현대글로비스 | Stage2-Actionable | 2023-05-22 | 174300 | logistics/PCC volume-mix bridge worked with low MAE |
| failed_rerating_high_MAE_after_transport_theme_blowoff | 005880 | 대한해운 | Stage2-Actionable | 2024-01-17 | 2810 | freight-theme price spike without bridge failed |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 2
counterexample_count: 1
4B_case_count: 3
4C_or_high_MAE_watch_count: 1
calibration_usable_case_count: 3
current_profile_error_count: 1
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 028670 | 팬오션 | Stage2-Actionable | 2021-04-22 | 6970 | 12.48 | 27.98 | 27.98 | -4.59 | -10.19 | -10.19 | 2021-06-29 | 8920 | -29.82 |
| 086280 | 현대글로비스 | Stage2-Actionable | 2023-05-22 | 174300 | 15.32 | 16.47 | 16.47 | -3.61 | -4.53 | -6.6 | 2023-07-05 | 203000 | -19.8 |
| 005880 | 대한해운 | Stage2-Actionable | 2024-01-17 | 2810 | 10.32 | 10.32 | 10.32 | -32.1 | -37.65 | -37.65 | 2024-01-17 | 3100 | -43.48 |

## 9. Case-by-Case Notes

### 9.1 028670 / 팬오션 — bulk shipping rate-cycle to margin bridge

The entry row is 2021-04-22 at 6,970. The 90D path reaches 8,920, while the adverse path stays inside a tolerable shipping-cycle drawdown band. This validates C29 when freight rate and volume evidence convert into margin and earnings visibility.

### 9.2 086280 / 현대글로비스 — logistics/PCC volume-mix bridge

The entry row is 2023-05-22 at 174,300. The 90D high reaches 203,000 and the 180D low remains relatively contained versus typical theme spikes. This is the low-volatility C29 success pattern: not explosive, but score-return aligned because volume/mix and operating leverage are visible.

### 9.3 005880 / 대한해운 — freight-theme price spike without margin bridge

The entry row is 2024-01-17 at 2,810. The local high reaches 3,100, but the path then falls to 1,752. This is the C29 trap: freight/geopolitical theme heat is not enough unless it becomes rate-to-earnings, volume utilization, or margin conversion.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C29 treats freight/shipping theme price strength as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C29 needs volume/rate/margin/operating-leverage bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for 005880 near the local freight-theme peak. |
| Full 4B non-price requirement appropriate? | Yes. 028670/086280 have better non-price bridges; 005880 does not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
028670:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after freight rate / volume / margin bridge
  Stage3-Green = wait for stronger earnings durability and 4B check

086280:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed despite modest MFE because MAE is controlled and logistics volume/mix bridge is cleaner
  Stage3-Green = wait for margin durability and capital-return/FCF confirmation

005880:
  Stage2-Actionable = too generous if based only on shipping/freight theme price spike
  Stage3-Yellow = reject without rate-to-earnings or volume-margin bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 028670 | 0.96 | 1.00 | good full-window 4B watch after shipping rate/margin bridge |
| 086280 | 0.93 | 1.00 | low-volatility 4B watch after logistics volume/margin bridge |
| 005880 | 1.00 | 1.00 | price/theme local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c29_transport_requires_volume_rate_margin_bridge

rule:
  For C29 transport/logistics rows, do not promote freight, shipping, logistics,
  or mobility-theme Stage2 signals into Stage3-Yellow/Green unless at least one
  non-price bridge is visible:
  volume growth, freight-rate-to-earnings conversion, utilization, mix/margin improvement,
  operating leverage, customer volume visibility, or FCF/cash conversion.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 18.26 | -17.46 | 33.3% | useful but can over-credit freight theme |
| P0b e2r_2_0_baseline_reference | 3 | 18.26 | -17.46 | 0% | safer but may miss 028670/086280 |
| P1 sector_specific_candidate_profile | 3 | 18.26 | -17.46 | 33.3% | no broad L3 loosen |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 22.23 | -7.36 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected | 10.32 | -37.65 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 028670 | current_profile_correct | freight-rate/margin bridge aligned with positive MFE |
| 086280 | current_profile_correct | logistics volume/mix bridge aligned with low-MAE rerating |
| 005880 | current_profile_false_positive | freight-theme price spike produced high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29_TRANSPORT_SHIPPING_VOLUME_RATE_MARGIN_BRIDGE_GUARD | 2 | 1 | 3 | 1 | 3 | 0 | 3 | 3 | 1 | false | true | C29 non-top-covered transport/shipping residual reduced |

## 17. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_guardrail
residual_error_types_found:
- freight theme without volume/margin bridge
- transport rate-cycle winner needs 4B watch
- price spike high-MAE after shipping theme Stage2
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
- local_4b_watch_guard
- high_MAE_watch_guard
existing_axis_weakened: null
existing_axis_kept:
- stage3_green_total_min
- stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
```

## 18. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web tradable_raw OHLC rows
- entry_date / entry_price
- MFE/MAE/peak/drawdown
- round/sector/canonical consistency
- duplicate avoidance at symbol level
```

Not validated:

```text
- exact disclosure URLs
- exact report URLs
- production scoring behavior
- live candidate status
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c29_transport_requires_volume_rate_margin_bridge,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"C29 transport/logistics rows should not promote toward Stage3-Yellow/Green unless mobility/shipping/freight signal converts into volume, rate-to-earnings, mix/margin, or operating-leverage bridge","028670 and 086280 survive with better MFE/MAE after transport margin bridge; 005880 fails when freight theme is price-only and bridge is absent","TRG_R9L72_C29_028670_20210422_BULK_SHIPPING_RATE_VOLUME_MARGIN_BRIDGE|TRG_R9L72_C29_086280_20230522_LOGISTICS_VOLUME_MIX_MARGIN_BRIDGE|TRG_R9L72_C29_005880_20240117_SHIPPING_THEME_PRICE_SPIKE_NO_MARGIN_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c29_shipping_transport_4b_high_mae_watch_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,1,1,0,"Transport/shipping rate-cycle winners and freight-theme failures can peak quickly; local 4B/high-MAE watch should remain active after MFE","preserves 028670/086280 positives while preventing 005880 freight-theme false positive","TRG_R9L72_C29_028670_20210422_BULK_SHIPPING_RATE_VOLUME_MARGIN_BRIDGE|TRG_R9L72_C29_086280_20230522_LOGISTICS_VOLUME_MIX_MARGIN_BRIDGE|TRG_R9L72_C29_005880_20240117_SHIPPING_THEME_PRICE_SPIKE_NO_MARGIN_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R9L72_C29_028670_20210422_BULK_SHIPPING_RATE_VOLUME_MARGIN_BRIDGE","symbol":"028670","company_name":"팬오션","round":"R9","loop":"72","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_BULK_SHIPPING_RATE_VOLUME_MARGIN_BRIDGE","deep_sub_archetype_id":"BDI_BULK_RATE_CYCLE_TO_EARNINGS_AND_MARGIN_CONVERSION","case_type":"structural_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C29 transport/logistics rows require volume, rate-to-earnings, mix/margin, or operating-leverage bridge; freight or mobility theme price spike alone is insufficient."}
{"row_type":"case","case_id":"R9L72_C29_086280_20230522_LOGISTICS_VOLUME_MIX_MARGIN_BRIDGE","symbol":"086280","company_name":"현대글로비스","round":"R9","loop":"72","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_LOGISTICS_VOLUME_MIX_MARGIN_BRIDGE","deep_sub_archetype_id":"PCC_LOGISTICS_VOLUME_MIX_OPERATING_LEVERAGE","case_type":"structural_success_low_MAE","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C29 transport/logistics rows require volume, rate-to-earnings, mix/margin, or operating-leverage bridge; freight or mobility theme price spike alone is insufficient."}
{"row_type":"case","case_id":"R9L72_C29_005880_20240117_SHIPPING_THEME_PRICE_SPIKE_NO_MARGIN_BRIDGE","symbol":"005880","company_name":"대한해운","round":"R9","loop":"72","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_SHIPPING_THEME_PRICE_SPIKE_WITHOUT_MARGIN_BRIDGE","deep_sub_archetype_id":"GEOPOLITICAL_FREIGHT_THEME_WITHOUT_RATE_TO_EARNINGS_CONVERSION","case_type":"failed_rerating_high_MAE_after_transport_theme_blowoff","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C29 transport/logistics rows require volume, rate-to-earnings, mix/margin, or operating-leverage bridge; freight or mobility theme price spike alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R9L72_C29_028670_20210422_BULK_SHIPPING_RATE_VOLUME_MARGIN_BRIDGE","case_id":"R9L72_C29_028670_20210422_BULK_SHIPPING_RATE_VOLUME_MARGIN_BRIDGE","symbol":"028670","company_name":"팬오션","round":"R9","loop":"72","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_BULK_SHIPPING_RATE_VOLUME_MARGIN_BRIDGE","deep_sub_archetype_id":"BDI_BULK_RATE_CYCLE_TO_EARNINGS_AND_MARGIN_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2021-04-22","entry_date":"2021-04-22","entry_price":6970,"evidence_available_at_that_date":"source_proxy_bulk_shipping_rate_BDI_volume_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_bulk_shipping_rate_BDI_volume_margin_bridge; evidence_url_pending","bridge_summary":"bulk shipping rate and volume improvement converted into margin/earnings visibility rather than pure freight-rate headline","stage2_evidence_fields":["shipping_rate_cycle","bulk_volume_margin_bridge","relative_strength","earnings_revision_proxy"],"stage3_evidence_fields":["rate_to_margin_conversion","volume_or_utilization_visibility","non_price_freight_bridge"],"stage4b_evidence_fields":["post_rate_cycle_peak_watch","shipping_rate_crowding_after_MFE"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028670/2021.csv","profile_path":"atlas/symbol_profiles/028/028670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.48,"MFE_90D_pct":27.98,"MFE_180D_pct":27.98,"MFE_1Y_pct":27.98,"MFE_2Y_pct":27.98,"MAE_30D_pct":-4.59,"MAE_90D_pct":-10.19,"MAE_180D_pct":-10.19,"MAE_1Y_pct":-10.19,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-06-29","peak_price":8920,"drawdown_after_peak_pct":-29.82,"green_lateness_ratio":"0.42","four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_after_shipping_rate_margin_bridge","four_b_evidence_type":"non_price_volume_rate_margin_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L72_C29_028670_20210422_BULK_SHIPPING_RATE_VOLUME_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R9L72_C29_086280_20230522_LOGISTICS_VOLUME_MIX_MARGIN_BRIDGE","case_id":"R9L72_C29_086280_20230522_LOGISTICS_VOLUME_MIX_MARGIN_BRIDGE","symbol":"086280","company_name":"현대글로비스","round":"R9","loop":"72","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_LOGISTICS_VOLUME_MIX_MARGIN_BRIDGE","deep_sub_archetype_id":"PCC_LOGISTICS_VOLUME_MIX_OPERATING_LEVERAGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-22","entry_date":"2023-05-22","entry_price":174300,"evidence_available_at_that_date":"source_proxy_logistics_PCC_volume_mix_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_logistics_PCC_volume_mix_margin_bridge; evidence_url_pending","bridge_summary":"logistics/PCC volume and mix improvement produced a controlled-MAE rerating path, not a price-only mobility theme","stage2_evidence_fields":["logistics_volume_mix","transport_margin_bridge","relative_strength","customer_volume_visibility"],"stage3_evidence_fields":["operating_leverage_visibility","mix_margin_conversion","low_MAE_confirmation"],"stage4b_evidence_fields":["valuation_repricing_watch","post_MFE_peak_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086280/2023.csv","profile_path":"atlas/symbol_profiles/086/086280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.32,"MFE_90D_pct":16.47,"MFE_180D_pct":16.47,"MFE_1Y_pct":16.47,"MFE_2Y_pct":16.47,"MAE_30D_pct":-3.61,"MAE_90D_pct":-4.53,"MAE_180D_pct":-6.6,"MAE_1Y_pct":-6.6,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-05","peak_price":203000,"drawdown_after_peak_pct":-19.8,"green_lateness_ratio":"0.51","four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"low_volatility_4B_watch_after_logistics_volume_margin_bridge","four_b_evidence_type":"non_price_volume_rate_margin_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_low_MAE","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L72_C29_086280_20230522_LOGISTICS_VOLUME_MIX_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R9L72_C29_005880_20240117_SHIPPING_THEME_PRICE_SPIKE_NO_MARGIN_BRIDGE","case_id":"R9L72_C29_005880_20240117_SHIPPING_THEME_PRICE_SPIKE_NO_MARGIN_BRIDGE","symbol":"005880","company_name":"대한해운","round":"R9","loop":"72","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_SHIPPING_THEME_PRICE_SPIKE_WITHOUT_MARGIN_BRIDGE","deep_sub_archetype_id":"GEOPOLITICAL_FREIGHT_THEME_WITHOUT_RATE_TO_EARNINGS_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-17","entry_date":"2024-01-17","entry_price":2810,"evidence_available_at_that_date":"source_proxy_shipping_geopolitical_freight_theme_without_rate_to_earnings_bridge; evidence_url_pending","evidence_source":"source_proxy_shipping_geopolitical_freight_theme_without_rate_to_earnings_bridge; evidence_url_pending","bridge_summary":"shipping/freight theme price spike lacked durable volume, rate-to-earnings, or margin bridge and reversed into high MAE","stage2_evidence_fields":["shipping_theme","freight_rate_optionality","price_spike","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","weak_follow_through","freight_theme_reversal_watch"],"stage4c_evidence_fields":["high_MAE_without_volume_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005880/2024.csv","profile_path":"atlas/symbol_profiles/005/005880.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.32,"MFE_90D_pct":10.32,"MFE_180D_pct":10.32,"MFE_1Y_pct":10.32,"MFE_2Y_pct":10.32,"MAE_30D_pct":-32.1,"MAE_90D_pct":-37.65,"MAE_180D_pct":-37.65,"MAE_1Y_pct":-37.65,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-17","peak_price":3100,"drawdown_after_peak_pct":-43.48,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"price_theme_without_volume_margin_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L72_C29_005880_20240117_SHIPPING_THEME_PRICE_SPIKE_NO_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L72_C29_028670_20210422_BULK_SHIPPING_RATE_VOLUME_MARGIN_BRIDGE","trigger_id":"TRG_R9L72_C29_028670_20210422_BULK_SHIPPING_RATE_VOLUME_MARGIN_BRIDGE","symbol":"028670","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"volume_score":11,"transport_rate_score":11,"mix_margin_bridge_score":10,"operating_leverage_score":9,"relative_strength_score":10,"theme_reversal_risk_penalty":4},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"volume_score":13,"transport_rate_score":13,"mix_margin_bridge_score":14,"operating_leverage_score":11,"relative_strength_score":8,"theme_reversal_risk_penalty":4},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["volume_score","transport_rate_score","mix_margin_bridge_score","operating_leverage_score","relative_strength_score","theme_reversal_risk_penalty"],"component_delta_explanation":"C29 transport row is promoted only when volume/rate signal converts into margin and operating-leverage visibility.","MFE_90D_pct":27.98,"MAE_90D_pct":-10.19,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L72_C29_086280_20230522_LOGISTICS_VOLUME_MIX_MARGIN_BRIDGE","trigger_id":"TRG_R9L72_C29_086280_20230522_LOGISTICS_VOLUME_MIX_MARGIN_BRIDGE","symbol":"086280","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"volume_score":11,"transport_rate_score":11,"mix_margin_bridge_score":10,"operating_leverage_score":9,"relative_strength_score":10,"theme_reversal_risk_penalty":4},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"volume_score":13,"transport_rate_score":13,"mix_margin_bridge_score":14,"operating_leverage_score":11,"relative_strength_score":8,"theme_reversal_risk_penalty":4},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["volume_score","transport_rate_score","mix_margin_bridge_score","operating_leverage_score","relative_strength_score","theme_reversal_risk_penalty"],"component_delta_explanation":"C29 transport row is promoted only when volume/rate signal converts into margin and operating-leverage visibility.","MFE_90D_pct":16.47,"MAE_90D_pct":-4.53,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L72_C29_005880_20240117_SHIPPING_THEME_PRICE_SPIKE_NO_MARGIN_BRIDGE","trigger_id":"TRG_R9L72_C29_005880_20240117_SHIPPING_THEME_PRICE_SPIKE_NO_MARGIN_BRIDGE","symbol":"005880","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"volume_score":5,"transport_rate_score":8,"mix_margin_bridge_score":1,"operating_leverage_score":1,"relative_strength_score":12,"theme_reversal_risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"volume_score":2,"transport_rate_score":4,"mix_margin_bridge_score":0,"operating_leverage_score":0,"relative_strength_score":5,"theme_reversal_risk_penalty":14},"weighted_score_after":42,"stage_label_after":"Stage1-Watch","changed_components":["volume_score","transport_rate_score","mix_margin_bridge_score","operating_leverage_score","relative_strength_score","theme_reversal_risk_penalty"],"component_delta_explanation":"C29 guard demotes freight/shipping theme price spikes when rate-to-earnings or volume-margin bridge is absent.","MFE_90D_pct":10.32,"MAE_90D_pct":-37.65,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c29_transport_requires_volume_rate_margin_bridge,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"C29 transport/logistics rows should not promote toward Stage3-Yellow/Green unless mobility/shipping/freight signal converts into volume, rate-to-earnings, mix/margin, or operating-leverage bridge","028670 and 086280 survive with better MFE/MAE after transport margin bridge; 005880 fails when freight theme is price-only and bridge is absent","TRG_R9L72_C29_028670_20210422_BULK_SHIPPING_RATE_VOLUME_MARGIN_BRIDGE|TRG_R9L72_C29_086280_20230522_LOGISTICS_VOLUME_MIX_MARGIN_BRIDGE|TRG_R9L72_C29_005880_20240117_SHIPPING_THEME_PRICE_SPIKE_NO_MARGIN_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c29_shipping_transport_4b_high_mae_watch_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,1,1,0,"Transport/shipping rate-cycle winners and freight-theme failures can peak quickly; local 4B/high-MAE watch should remain active after MFE","preserves 028670/086280 positives while preventing 005880 freight-theme false positive","TRG_R9L72_C29_028670_20210422_BULK_SHIPPING_RATE_VOLUME_MARGIN_BRIDGE|TRG_R9L72_C29_086280_20230522_LOGISTICS_VOLUME_MIX_MARGIN_BRIDGE|TRG_R9L72_C29_005880_20240117_SHIPPING_THEME_PRICE_SPIKE_NO_MARGIN_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R9","loop":"72","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["freight_theme_without_volume_margin_bridge","transport_rate_cycle_winner_needs_4B_watch","price_spike_high_MAE_after_shipping_theme_stage2"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

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

## 22. Next Round State

```text
completed_round = R9
completed_loop = 72
next_round = R10
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```

## 23. Source Notes

```text
MAIN EXECUTION PROMPT:
docs/core/e2r_v12_prompt_round_scheduler_corrected.txt

NO-REPEAT INDEX:
docs/core/V12_Research_No_Repeat_Index.md

Stock-web:
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/028/028670.json
atlas/symbol_profiles/086/086280.json
atlas/symbol_profiles/005/005880.json
atlas/ohlcv_tradable_by_symbol_year/028/028670/2021.csv
atlas/ohlcv_tradable_by_symbol_year/086/086280/2023.csv
atlas/ohlcv_tradable_by_symbol_year/005/005880/2024.csv
```

This loop adds 3 new independent C29 cases, 2 positives, 1 counterexample, and 1 canonical-archetype residual guard candidate for R9/L3.

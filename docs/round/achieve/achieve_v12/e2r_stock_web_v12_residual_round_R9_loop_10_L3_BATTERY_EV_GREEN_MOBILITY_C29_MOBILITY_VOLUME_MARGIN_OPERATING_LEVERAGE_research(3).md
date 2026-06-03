# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R9_loop_10_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
scheduled_round: R9
scheduled_loop: 10
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_VOLUME_MIX_EXPORT_MARGIN_OPERATING_LEVERAGE
loop_objective:
  - coverage_gap_fill
  - sector_specific_rule_discovery
  - canonical_archetype_compression
  - stage2_actionable_bonus_stress_test
  - green_strictness_stress_test
  - 4B_non_price_requirement_stress_test
  - counterexample_mining
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds **3 new independent cases**, **1 counterexample**, and **1 residual error** for **R9 / L3_BATTERY_EV_GREEN_MOBILITY / C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE**.

## 1. Current Calibrated Profile Assumption

Current profile proxy:

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

This MD does not re-propose the global calibrated axes. It stress-tests whether the already calibrated profile still over-rewards mobility supplier / headline volume cases when margin bridge and mix durability are weaker than OEM-level evidence.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| scheduled_round | R9 |
| scheduled_loop | 10 |
| allowed large sector | L3_BATTERY_EV_GREEN_MOBILITY or L9_CONSTRUCTION_REALESTATE_HOUSING |
| selected large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE |
| fine_archetype_id | AUTO_VOLUME_MIX_EXPORT_MARGIN_OPERATING_LEVERAGE |
| round_sector_consistency | pass |

R9 is treated here as passenger vehicle / auto-mobility volume, mix, ASP, margin, export, and operating leverage. It is not a live auto stock scan and not a 2026 recommendation list.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts show R1~R13 and loops 1~9 covered. Therefore the next sequential target is R9 / Loop 10 after the already completed R8 / Loop 10 session state. Existing historical R9 files are treated as prior coverage; this MD avoids simple rematerialization by using a focused C29 compression: OEM volume/mix margin winners vs. supplier volume narratives with weak margin translation.

Duplicate avoidance decision:

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = avoided
same_symbol_new_trigger_family = not used
new_symbol_count = 3
reused_case_count = 0
minimum_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Manifest validation:

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Symbol profile checks:

| Symbol | Company | Profile path | Relevant corporate-action status | Calibration treatment |
|---|---|---|---|---|
| 005380 | 현대차 | atlas/symbol_profiles/005/005380.json | old corporate-action candidates only, no 2023 contamination | clean 180D window |
| 000270 | 기아 | atlas/symbol_profiles/000/000270.json | old corporate-action candidates only, no 2023 contamination | clean 180D window |
| 204320 | HL만도 | atlas/symbol_profiles/204/204320.json | 2018 corporate-action candidate only, no 2023 contamination | clean 180D window |

## 5. Historical Eligibility Gate

All representative rows below satisfy:

```text
trigger_date is historical
entry_date exists in stock-web tradable shard
forward 180D window exists before manifest max_date
high / low / close / volume exist
MFE_30D / 90D / 180D and MAE_30D / 90D / 180D calculated from stock-web rows
no corporate-action candidate overlaps entry_date~D+180
```

## 6. Canonical Archetype Compression Map

| Fine signal | Canonical compression | Treatment |
|---|---|---|
| OEM global volume + SUV/US mix + FX/margin bridge | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | positive bridge |
| OEM volume + shareholder value-up noise but weak margin separation | C29, but not enough alone for Green | Stage2 only unless revision and margin confirm |
| Parts supplier volume/ADAS/EV order narrative without pass-through margin | C29 counterexample subpath | cap positive promotion |
| Price-only local peak after OEM margin rerating | C29 4B overlay only | do not treat as full 4B without non-price evidence |

## 7. Case Selection Summary

| case_id | Symbol | Company | Role | Trigger | Entry | Entry price | Outcome |
|---|---:|---|---|---|---|---:|---|
| R9L10_C29_005380_STAGE2 | 005380 | 현대차 | structural_success | 2023-01-26 earnings / margin-mix trigger | 2023-01-27 | 173900 | C29 positive, OEM margin bridge worked |
| R9L10_C29_000270_STAGE2 | 000270 | 기아 | structural_success | 2023-01-26 earnings / mix-margin trigger | 2023-01-27 | 68700 | C29 positive, stronger MFE than Hyundai |
| R9L10_C29_204320_STAGE2 | 204320 | HL만도 | failed_rerating | 2023-02-10 supplier volume / EV-ADAS narrative | 2023-02-10 | 47600 | counterexample: supplier volume did not sustain margin rerating |
| R9L10_C29_000270_4B | 000270 | 기아 | 4B_overlay_success | 2023-05-11 local valuation/positioning watch | 2023-05-11 | 90100 | 4B overlay only, not full exit rule |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 4
new_independent_case_count = 3
```

The positive cases are OEM-level volume/mix/margin cases. The counterexample is a parts supplier / platform-supplier style mobility case where volume headline alone does not guarantee pass-through margin and operating leverage.

## 9. Evidence Source Map

| Symbol | Stage2 evidence family | Stage3 evidence family | 4B / 4C evidence family | Evidence URL status |
|---|---|---|---|---|
| 005380 | public earnings / volume mix / margin | confirmed revision and margin visibility | valuation and price local peak only | exact original URL enrichment required |
| 000270 | public earnings / strong operating margin / model mix | confirmed margin and revision | 2023-05 local valuation/positioning watch | exact original URL enrichment required |
| 204320 | auto parts volume / ADAS / EV narrative | margin bridge weaker than OEMs | later drawdown without durable margin confirmation | exact original URL enrichment required |

The exact primary news / disclosure URL enrichment is deferred. The purpose of this MD is residual price-shape and rule-candidate calibration, not production source ingestion.

## 10. Price Data Source Map

| Symbol | price_shard_path | profile_path | Entry date | Entry price |
|---|---|---|---|---:|
| 005380 | atlas/ohlcv_tradable_by_symbol_year/005/005380/2023.csv | atlas/symbol_profiles/005/005380.json | 2023-01-27 | 173900 |
| 000270 | atlas/ohlcv_tradable_by_symbol_year/000/000270/2023.csv | atlas/symbol_profiles/000/000270.json | 2023-01-27 | 68700 |
| 204320 | atlas/ohlcv_tradable_by_symbol_year/204/204320/2023.csv | atlas/symbol_profiles/204/204320.json | 2023-02-10 | 47600 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | stage2 fields | stage3 fields | 4B fields | 4C fields | calibration_usable |
|---|---|---|---|---|---|---|---|---|---|
| T_R9L10_005380_STAGE2 | R9L10_C29_005380 | Stage2-Actionable | 2023-01-26 | 2023-01-27 | public_event_or_disclosure, capacity_or_volume_route, early_revision_signal | margin_bridge, financial_visibility | [] | [] | true |
| T_R9L10_000270_STAGE2 | R9L10_C29_000270 | Stage2-Actionable | 2023-01-26 | 2023-01-27 | public_event_or_disclosure, capacity_or_volume_route, relative_strength | margin_bridge, confirmed_revision | [] | [] | true |
| T_R9L10_204320_STAGE2 | R9L10_C29_204320 | Stage2-Actionable | 2023-02-10 | 2023-02-10 | public_event_or_disclosure, capacity_or_volume_route | [] | margin_or_backlog_slowdown | [] | true |
| T_R9L10_000270_4B | R9L10_C29_000270 | Stage4B-Overlay | 2023-05-11 | 2023-05-11 | [] | [] | valuation_blowoff, positioning_overheat | [] | true |

## 12. Trigger-Level OHLC Backtest Tables

Approximate calculations use stock-web raw/unadjusted `h/l/c` rows and representative forward windows. Values are stored as research-calibration proxy numbers, not production scoring outputs.

| trigger_id | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| T_R9L10_005380_STAGE2 | 173900 | 3.74 | -3.97 | 21.33 | -3.97 | 21.33 | -3.97 | 2023-05-10 | 211000 | -13.70 |
| T_R9L10_000270_STAGE2 | 68700 | 15.28 | -2.77 | 33.77 | -2.77 | 33.77 | -2.77 | 2023-05-11 | 91900 | -15.99 |
| T_R9L10_204320_STAGE2 | 47600 | 8.40 | -7.56 | 14.50 | -7.56 | 14.50 | -26.37 | 2023-06-30 | 54500 | -35.69 |
| T_R9L10_000270_4B | 90100 | 1.33 | -9.99 | 1.33 | -9.99 | 1.33 | -14.43 | 2023-05-11 | 91900 | -15.99 |

## 13. Current Calibrated Profile Stress Test

| case_id | Current profile likely verdict | Actual price outcome | Verdict |
|---|---|---|---|
| R9L10_C29_005380 | Stage2/Yellow appropriate; Green only after margin/revision confirmation | MFE_90/180 ~ +21%, low MAE | current_profile_correct |
| R9L10_C29_000270 | Stage2/Yellow appropriate; Green after margin and revision | MFE_90/180 ~ +34%, low MAE | current_profile_correct |
| R9L10_C29_204320 | May over-promote if supplier volume is treated like OEM mix/margin | MFE existed but MAE_180 ~ -26% | current_profile_false_positive |

Stress-test conclusions:

```text
stage2_actionable_evidence_bonus: useful for OEM cases, too permissive for supplier narrative without margin pass-through
stage3_yellow_total_min_75: generally appropriate
stage3_green_total_min_87: appropriate; should not be relaxed for C29 supplier cases
stage3_green_revision_min_55: appropriate
price_only_blowoff_blocks_positive_stage: kept
full_4b_requires_non_price_evidence: strengthened
hard_4c_thesis_break_routes_to_4c: kept; no hard 4C case added in this loop
```

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Stage3-Yellow proxy | Stage3-Green proxy | green_lateness_ratio | Interpretation |
|---|---:|---:|---:|---:|---|
| R9L10_C29_005380 | 173900 | 198200 | 210000 | 0.67 | Green would catch much less upside if waiting for full confirmation |
| R9L10_C29_000270 | 68700 | 86100 | 90100 | 0.92 | Green risks being near local peak in fast OEM rerating |
| R9L10_C29_204320 | 47600 | not confirmed | not confirmed | not_applicable | no durable margin-confirmed Green trigger |

Interpretation: C29 OEM cases can rerate quickly once mix/margin proof appears. However, this should not become a global Green relaxation because the HL만도 counterexample shows that parts supplier volume narratives can give a small MFE and then large MAE.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | Stage2 reference | 4B entry | local_peak | full_window_peak | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| T_R9L10_000270_4B | 68700 | 90100 | 91900 | 91900 | 0.92 | 0.92 | good_overlay_watch_but_needs_non_price_evidence |
| T_R9L10_204320_STAGE2 | 47600 | not_applicable | 54500 | 54500 | not_applicable | not_applicable | not full 4B; failed Stage2/Yellow candidate |

4B conclusion: in C29, price-only local peak should stay overlay-only unless valuation, revision slowdown, margin deterioration, inventory, or demand evidence confirms non-price risk.

## 16. 4C Protection Audit

No clean hard 4C trigger is promoted in this loop. HL만도 is treated as a failed-rerating / high-MAE counterexample, not a fully validated 4C thesis-break row. C29 4C should require one of:

```text
volume thesis broken
margin bridge reversed
inventory / incentive pressure visible
order cut or demand slowdown visible
accounting or trust break
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
rule_candidate = l3_mobility_oem_mix_margin_bridge_required
```

Candidate rule:

```text
Within L3/C29, OEM volume or global sales growth can receive Stage2/Yellow support only when at least one of mix, ASP, FX/margin, utilization, or confirmed revision bridge is visible. Supplier volume / ADAS / EV platform narratives without explicit pass-through margin or operating leverage confirmation should be capped below Stage3-Green and flagged for high-MAE watch.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
rule_candidate = c29_oem_mix_margin_bridge_bonus_and_supplier_margin_cap
```

Proposed C29 shadow axes:

```text
c29_oem_mix_margin_bridge_bonus = +1 shadow-only when OEM volume + mix + margin/revision confirm
c29_supplier_volume_without_pass_through_cap = cap Stage2/Yellow if supplier evidence lacks pass-through margin or customer economics
c29_price_only_mobility_local_peak_overlay_only = 4B watch but not full 4B unless non-price evidence exists
```

## 19. Before / After Backtest Comparison

| Profile | Hypothesis | eligible triggers | avg MFE_90 | avg MAE_90 | avg MFE_180 | avg MAE_180 | false positive count | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current calibrated proxy | 3 | 23.20 | -4.77 | 23.20 | -11.04 | 1 | good but supplier cap needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 23.20 | -4.77 | 23.20 | -11.04 | 1 | less precise evidence separation |
| P1 sector_specific_candidate_profile | require OEM mix/margin bridge | 3 | 27.55 | -3.37 | 27.55 | -3.37 | 0 | better alignment |
| P2 canonical_archetype_candidate_profile | C29 OEM bonus + supplier cap | 3 | 27.55 | -3.37 | 27.55 | -3.37 | 0 | best shadow candidate |
| P3 counterexample_guard_profile | strict supplier cap | 3 | 27.55 | -3.37 | 27.55 | -3.37 | 0 | useful guard, not standalone entry booster |

## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | score_return_alignment |
|---|---:|---|---:|---|---|
| R9L10_C29_005380 | 79 | Stage3-Yellow | 82 | Stage3-Yellow+ | aligned_positive |
| R9L10_C29_000270 | 82 | Stage3-Yellow | 85 | Stage3-Yellow+ | aligned_positive |
| R9L10_C29_204320 | 76 | Stage3-Yellow | 68 | Stage2-Watch | improved_false_positive_control |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | AUTO_VOLUME_MIX_EXPORT_MARGIN_OPERATING_LEVERAGE | 2 | 1 | 1 | 0 | 3 | 0 | 4 | 3 | 1 | true | true | need non-OEM mobility and transport cases in later R9 loops |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - supplier_volume_without_margin_pass_through_false_positive
new_axis_proposed:
  - c29_oem_mix_margin_bridge_bonus
  - c29_supplier_volume_without_pass_through_cap
  - c29_price_only_mobility_local_peak_overlay_only
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
existing_axis_kept:
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date and price basis
- symbol profile availability and corporate-action window status
- entry_date / entry_price from tradable shards
- representative OHLC MFE/MAE path shape
- duplicate / novelty fields
- sector and canonical archetype consistency
```

Not validated in this MD:

```text
- exact original disclosure/news URLs
- production scoring code behavior
- live market status
- current watchlist or investment recommendation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c29_oem_mix_margin_bridge_bonus,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"OEM volume+mix+margin bridge separated positives from supplier narrative","positive OEM cases retained, supplier false positive reduced","T_R9L10_005380_STAGE2|T_R9L10_000270_STAGE2|T_R9L10_204320_STAGE2",3,3,1,medium,canonical_shadow_only,"not production; exact evidence URL enrichment required"
shadow_weight,c29_supplier_volume_without_pass_through_cap,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"supplier volume narrative had high MAE without durable margin proof","false positive control improved","T_R9L10_204320_STAGE2",1,1,1,medium,canonical_shadow_only,"not production"
shadow_weight,c29_price_only_mobility_local_peak_overlay_only,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"price-only local peak should not become full 4B","keeps overlay separate from full 4B","T_R9L10_000270_4B",1,1,0,low,overlay_shadow_only,"not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R9L10_C29_005380","symbol":"005380","company_name":"현대차","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_VOLUME_MIX_EXPORT_MARGIN_OPERATING_LEVERAGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_R9L10_005380_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"OEM volume/mix/margin bridge positive"}
{"row_type":"case","case_id":"R9L10_C29_000270","symbol":"000270","company_name":"기아","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_VOLUME_MIX_EXPORT_MARGIN_OPERATING_LEVERAGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_R9L10_000270_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"OEM margin and relative strength positive"}
{"row_type":"case","case_id":"R9L10_C29_204320","symbol":"204320","company_name":"HL만도","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_SUPPLIER_VOLUME_WITHOUT_MARGIN_PASS_THROUGH","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"T_R9L10_204320_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misaligned_false_positive_control_needed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"supplier volume narrative had high MAE without durable margin bridge"}
{"row_type":"trigger","trigger_id":"T_R9L10_005380_STAGE2","case_id":"R9L10_C29_005380","symbol":"005380","company_name":"현대차","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_VOLUME_MIX_EXPORT_MARGIN_OPERATING_LEVERAGE","sector":"모빌리티·운송·레저","primary_archetype":"OEM volume mix margin operating leverage","loop_objective":"sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-26","entry_date":"2023-01-27","entry_price":173900,"evidence_available_at_that_date":"earnings and mix/margin signal; exact URL pending","evidence_source":"exact_source_url_pending","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2023.csv","profile_path":"atlas/symbol_profiles/005/005380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.74,"MFE_90D_pct":21.33,"MFE_180D_pct":21.33,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.97,"MAE_90D_pct":-3.97,"MAE_180D_pct":-3.97,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-10","peak_price":211000,"drawdown_after_peak_pct":-13.70,"green_lateness_ratio":0.67,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L10_005380_2023-01-27_173900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R9L10_000270_STAGE2","case_id":"R9L10_C29_000270","symbol":"000270","company_name":"기아","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_VOLUME_MIX_EXPORT_MARGIN_OPERATING_LEVERAGE","sector":"모빌리티·운송·레저","primary_archetype":"OEM volume mix margin operating leverage","loop_objective":"sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-26","entry_date":"2023-01-27","entry_price":68700,"evidence_available_at_that_date":"earnings and margin signal; exact URL pending","evidence_source":"exact_source_url_pending","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["margin_bridge","confirmed_revision"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2023.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.28,"MFE_90D_pct":33.77,"MFE_180D_pct":33.77,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.77,"MAE_90D_pct":-2.77,"MAE_180D_pct":-2.77,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-11","peak_price":91900,"drawdown_after_peak_pct":-15.99,"green_lateness_ratio":0.92,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L10_000270_2023-01-27_68700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R9L10_204320_STAGE2","case_id":"R9L10_C29_204320","symbol":"204320","company_name":"HL만도","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_SUPPLIER_VOLUME_WITHOUT_MARGIN_PASS_THROUGH","sector":"모빌리티·운송·레저","primary_archetype":"supplier volume without margin bridge","loop_objective":"counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-10","entry_date":"2023-02-10","entry_price":47600,"evidence_available_at_that_date":"supplier volume / ADAS / EV narrative; exact URL pending","evidence_source":"exact_source_url_pending","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/204/204320/2023.csv","profile_path":"atlas/symbol_profiles/204/204320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.40,"MFE_90D_pct":14.50,"MFE_180D_pct":14.50,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.56,"MAE_90D_pct":-7.56,"MAE_180D_pct":-26.37,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-30","peak_price":54500,"drawdown_after_peak_pct":-35.69,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_full_4B_failed_rerating","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L10_204320_2023-02-10_47600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R9L10_000270_4B","case_id":"R9L10_C29_000270","symbol":"000270","company_name":"기아","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_VOLUME_MIX_EXPORT_MARGIN_OPERATING_LEVERAGE","sector":"모빌리티·운송·레저","primary_archetype":"price local 4B overlay","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2023-05-11","entry_date":"2023-05-11","entry_price":90100,"evidence_available_at_that_date":"local valuation/positioning watch; price-only risk not full 4B","evidence_source":"stock_web_price_path_plus_exact_source_url_pending","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2023.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.33,"MFE_90D_pct":1.33,"MFE_180D_pct":1.33,"MAE_30D_pct":-9.99,"MAE_90D_pct":-9.99,"MAE_180D_pct":-14.43,"peak_date":"2023-05-11","peak_price":91900,"drawdown_after_peak_pct":-15.99,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.92,"four_b_full_window_peak_proximity":0.92,"four_b_timing_verdict":"good_overlay_watch_but_needs_non_price_evidence","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L10_000270_2023-05-11_90100","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same symbol as Kia representative but new 4B timing path","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L10_C29_005380","trigger_id":"T_R9L10_005380_STAGE2","symbol":"005380","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":17,"revision_score":13,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":14},"weighted_score_before":79,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":19,"revision_score":13,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":15},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow+","changed_components":["margin_bridge_score","capacity_or_shipment_score"],"component_delta_explanation":"OEM mix/margin bridge receives C29-specific bonus","MFE_90D_pct":21.33,"MAE_90D_pct":-3.97,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L10_C29_000270","trigger_id":"T_R9L10_000270_STAGE2","symbol":"000270","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":19,"revision_score":14,"relative_strength_score":12,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":14},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":21,"revision_score":14,"relative_strength_score":12,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":15},"weighted_score_after":85,"stage_label_after":"Stage3-Yellow+","changed_components":["margin_bridge_score","capacity_or_shipment_score"],"component_delta_explanation":"stronger OEM margin/mix evidence, but not automatic Green relaxation","MFE_90D_pct":33.77,"MAE_90D_pct":-2.77,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L10_C29_204320","trigger_id":"T_R9L10_204320_STAGE2","symbol":"204320","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":6,"relative_strength_score":7,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":14},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":-9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":12},"weighted_score_after":68,"stage_label_after":"Stage2-Watch","changed_components":["margin_bridge_score","revision_score","execution_risk_score","capacity_or_shipment_score"],"component_delta_explanation":"supplier volume without margin pass-through capped below Stage3-Green/Yellow promotion","MFE_90D_pct":14.50,"MAE_90D_pct":-7.56,"score_return_alignment_label":"improved_false_positive_control","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","full_4b_requires_non_price_evidence"],"residual_error_types_found":["supplier_volume_without_margin_pass_through_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R9
completed_loop = 10
next_round = R10
next_loop = 10
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
Stock-web checked files:
- atlas/manifest.json
- atlas/symbol_profiles/005/005380.json
- atlas/symbol_profiles/000/000270.json
- atlas/symbol_profiles/204/204320.json
- atlas/ohlcv_tradable_by_symbol_year/005/005380/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/000/000270/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/204/204320/2023.csv

Stock-agent research artifacts checked:
- reports/e2r_calibration/ingest_summary.md
- data/e2r/calibration/md_registry.jsonl
```


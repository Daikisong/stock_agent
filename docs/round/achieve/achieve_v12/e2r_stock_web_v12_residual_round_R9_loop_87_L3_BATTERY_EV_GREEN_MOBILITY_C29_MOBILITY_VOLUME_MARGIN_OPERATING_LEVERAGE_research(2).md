# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
filename = e2r_stock_web_v12_residual_round_R9_loop_87_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R9
scheduled_loop = 87
completed_round = R9
completed_loop = 87
next_round = R10
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = SECOND_TIER_AUTO_PARTS_LIGHTING_BRAKE_MOTOR_VOLUME_MARGIN_BRIDGE_VS_THEME_FADE
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Current Calibrated Profile Assumption

```text
before_profile_id = e2r_2_1_stock_web_calibrated_proxy
after_profile_id = proposed_C29_second_tier_auto_parts_shadow_profile
rollback_reference_profile_id = e2r_2_0_baseline_reference
```

The current calibrated profile already blocks price-only blowoff from positive Stage promotion, requires non-price evidence for full 4B, and routes hard thesis-break evidence to 4C. This R9 loop does not repeat those global rules as a new global claim. It stress-tests whether C29 second-tier auto-parts triggers need a narrower bridge: volume/mix/margin evidence must be separated from generic auto-parts beta and EV/mobility theme spillover.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R9
allowed_large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY or L9_CONSTRUCTION_REALESTATE_HOUSING depending on mobility/transport nature
selected_large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```

R9 was selected because the latest visible registry state has completed R13 loop 86 and R1/R2/R4/R5/R7/R8 loop 87, while R9 loop 87 was not yet present in the inspected registry slice. R9 C29 remains valid when the research object is mobility/transport/auto-parts volume and margin operating leverage rather than construction/PF.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

The No-Repeat Index shows C29 already has broad coverage and high repetition in large OEM/first-tier names. Therefore this loop avoids the dominant repeated C29 symbols visible in the index, especially `000270`, `005380`, `012330`, `018880`, `161390`, and `UNKNOWN_SYMBOL`, and selects three different C29 symbols:

| symbol | company_name | duplicate status | reason selected |
|---|---|---|---|
| 064960 | SNT모티브 | no hard duplicate observed in inspected No-Repeat / registry excerpts | lower-MAE motor/defense/auto-part mix case; useful C29 positive/control |
| 005850 | 에스엘 | no hard duplicate observed in inspected C29 top repeated list | lighting/ADAS auto-parts operating leverage with local blowoff and later fade |
| 204320 | HL만도 | no hard duplicate observed in inspected C29 top repeated list | large auto-parts supplier where generic mobility beta can overstate Stage2 quality |

```text
minimum_new_symbol_count = 3
minimum_counterexample_count = 2
minimum_positive_case_count = 1
hard_duplicate_status = no_hard_duplicate_observed_in_inspected_registry_and_no_repeat_excerpt
```

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","source_name":"FinanceData/marcap","validation_status":"usable_for_historical_calibration_with_batch_recalc_recommended"}
```

Stock-web manifest fields inspected:

| field | value |
|---|---|
| source_name | FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |

Important caveat: stock-web OHLC is raw/unadjusted. Corporate-action-contaminated windows are blocked. The three selected 2023 entry windows do not overlap the corporate-action candidate dates visible in the fetched symbol profiles.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | profile status | 180D forward window | corporate action window | eligibility |
|---|---|---:|---|---|---|---|
| C29_R9L87_064960_POSITIVE_CONTROL | 064960 | 2023-05-16 | active_like; years include 2023/2024/2025/2026 | available before manifest max date | profile CA dates 2002-12-24, 2012-12-26, 2025-01-24, 2025-02-26; no 2023~early-2024 overlap | calibration_usable=true |
| C29_R9L87_005850_HIGH_MAE_FADE | 005850 | 2023-05-16 | active_like; years include 2023/2024/2025/2026 | available before manifest max date | profile CA dates 2002-07-30, 2003-12-16, 2007-10-22, 2019-04-16; no 2023~early-2024 overlap | calibration_usable=true |
| C29_R9L87_204320_FALSE_POSITIVE | 204320 | 2023-07-31 | active_like; years include 2023/2024/2025/2026 | available before manifest max date | profile CA date 2018-05-08; no 2023~early-2024 overlap | calibration_usable=true |

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = SECOND_TIER_AUTO_PARTS_LIGHTING_BRAKE_MOTOR_VOLUME_MARGIN_BRIDGE_VS_THEME_FADE
```

Fine/deep compression:

| fine/deep pattern | canonical compression | Stage2 bridge required |
|---|---|---|
| auto lighting / ADAS order momentum | C29 | shipment or order conversion plus OPM/mix evidence |
| EV motor / defense-auto mixed exposure | C29, with C03 caution if defense evidence dominates | distinguish mobility volume margin from defense backlog |
| braking / steering / chassis large supplier beta | C29 | margin bridge and customer volume evidence must beat generic OEM beta |
| auto-parts theme spike without margin proof | C29 | treat as Stage2-Watch or false-positive candidate |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger type | entry date | thesis |
|---|---|---|---|---|---:|---|
| C29_R9L87_064960_POSITIVE_CONTROL | 064960 | SNT모티브 | structural_success / low-MAE control | Stage2-Actionable | 2023-05-16 | C29 can work when auto component demand is not merely beta, and drawdown remains shallow while high/low confirms a controlled rerating path. |
| C29_R9L87_005850_HIGH_MAE_FADE | 005850 | 에스엘 | high_mae_success / local 4B watch | Stage2-Actionable | 2023-05-16 | Lighting/ADAS theme can create quick upside, but a local peak without confirmed durable margin bridge should be watched as 4B-local, not promoted to full Green. |
| C29_R9L87_204320_FALSE_POSITIVE | 204320 | HL만도 | failed_rerating / false_positive candidate | Stage2-FalsePositive-Candidate | 2023-07-31 | Generic mobility/auto-parts beta can overstate operating leverage when customer/mix/margin evidence is not strong enough. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
current_profile_error_count = 2
```

The positive/control case is not used to loosen global Stage2 or Green thresholds. The contribution is instead a C29 guard: require verified margin/mix bridge before treating a second-tier mobility supplier theme spike as structural rerating.

## 9. Evidence Source Map

This research uses source-proxy evidence descriptions because the execution environment inspected stock-web price rows and existing v12 artifacts, but did not fetch primary DART/IR source URLs for every event. Therefore all proposed calibration rows are marked `evidence_url_pending=true` and `source_proxy_only=true`; the handoff batch should either attach primary DART/IR/earnings-release URLs or keep the rows out of promotion.

| case_id | evidence_available_at_that_date | evidence_source | source_proxy_only | evidence_url_pending |
|---|---|---|---:|---:|
| C29_R9L87_064960_POSITIVE_CONTROL | 2023 auto-parts earnings/volume/mix read-through and low-drawdown price confirmation | source_proxy: company earnings/IR/DART check required | true | true |
| C29_R9L87_005850_HIGH_MAE_FADE | 2023 auto-lighting/ADAS operating leverage theme and fast local price response | source_proxy: company earnings/IR/DART check required | true | true |
| C29_R9L87_204320_FALSE_POSITIVE | 2023 mobility supplier beta after weak price path and margin concern | source_proxy: company earnings/IR/DART check required | true | true |

## 10. Price Data Source Map

| symbol | prefix | price_shard_path | profile_path | profile caveat |
|---|---|---|---|---|
| 064960 | 064 | atlas/ohlcv_tradable_by_symbol_year/064/064960/2023.csv | atlas/symbol_profiles/064/064960.json | raw/unadjusted; CA candidates outside 2023~early-2024 window |
| 005850 | 005 | atlas/ohlcv_tradable_by_symbol_year/005/005850/2023.csv | atlas/symbol_profiles/005/005850.json | raw/unadjusted; CA candidates outside 2023~early-2024 window |
| 204320 | 204 | atlas/ohlcv_tradable_by_symbol_year/204/204320/2023.csv | atlas/symbol_profiles/204/204320.json | raw/unadjusted; CA candidate 2018-05-08 only |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | stage2 fields | stage3 fields | 4B fields | outcome |
|---|---|---|---|---:|---:|---:|---|---|---|---|
| C29_R9L87_TRG_064960_S2 | C29_R9L87_064960_POSITIVE_CONTROL | 064960 | Stage2-Actionable | 2023-05-16 | 2023-05-16 | 50300 | customer_quality, capacity_or_volume_route, relative_strength | margin_bridge_pending, financial_visibility_pending | none | structural_success_low_MAE |
| C29_R9L87_TRG_005850_S2 | C29_R9L87_005850_HIGH_MAE_FADE | 005850 | Stage2-Actionable | 2023-05-16 | 2023-05-16 | 37500 | capacity_or_volume_route, relative_strength | margin_bridge_pending | price_only_local_peak | high_mae_success_local_4B_watch |
| C29_R9L87_TRG_204320_S2 | C29_R9L87_204320_FALSE_POSITIVE | 204320 | Stage2-FalsePositive-Candidate | 2023-07-31 | 2023-07-31 | 46150 | relative_strength, capacity_or_volume_route_pending | none | margin_or_backlog_slowdown_pending | failed_rerating |

## 12. Trigger-Level OHLC Backtest Tables

MFE/MAE values below are rounded manual calculations from stock-web tradable shard rows inspected during this run. Batch ingestion should recompute from the full shard before promotion. Entry price is the stock-web close `c` on `entry_date`.

| trigger_id | entry | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak | notes |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C29_R9L87_TRG_064960_S2 | 50300 | 7.2 | -2.6 | 11.1 | -6.4 | 11.1 | -7.5 | 2023-07-06 | 55900 | -15.7 | low-MAE control; shallower drawdown than theme spikes |
| C29_R9L87_TRG_005850_S2 | 37500 | 6.4 | -11.6 | 13.1 | -11.9 | 13.1 | -11.9 | 2023-07-17 | 42400 | -22.1 | local peak, then fade; not full 4B without non-price overheat evidence |
| C29_R9L87_TRG_204320_S2 | 46150 | 4.9 | -11.4 | 4.9 | -13.4 | 4.9 | -13.4 | 2023-07-31 | 48400 | -17.5 | generic beta signal did not produce strong MFE; false-positive candidate |

## 13. Current Calibrated Profile Stress Test

| case_id | current_profile_expected_judgment | price alignment | verdict |
|---|---|---|---|
| C29_R9L87_064960_POSITIVE_CONTROL | Stage2-Actionable allowed but not Green without confirmed revision/margin | MFE/MAE acceptable; Green still needs stronger evidence | current_profile_correct |
| C29_R9L87_005850_HIGH_MAE_FADE | Stage2-Actionable likely allowed; Green should wait | quick MFE but drawdown/fade argues for local 4B watch | current_profile_4B_too_late |
| C29_R9L87_204320_FALSE_POSITIVE | Stage2 may be too easy if generic mobility beta is over-weighted | weak MFE and meaningful MAE | current_profile_false_positive |

Stress-test answers:

```text
stage2_actionable_evidence_bonus = kept, but C29 second-tier names require verified margin/mix bridge
stage3_yellow_total_min = kept
stage3_green_total_min = kept
stage3_green_revision_min = kept
price_only_blowoff_blocks_positive_stage = strengthened conceptually for C29 local peak rows
full_4b_requires_non_price_evidence = kept
hard_4c_thesis_break_routes_to_4c = kept
```

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is asserted in this loop. The C29 second-tier auto-parts evidence set is deliberately treated as Stage2 or Stage2-Watch only until primary source evidence confirms margin bridge, customer order conversion, and earnings revision durability.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| C29_R9L87_TRG_005850_S2 | 1.00 | 1.00 | price_only_local_peak | price_only_local_4B_watch_only |
| C29_R9L87_TRG_204320_S2 | 1.00 | 1.00 | margin_or_backlog_slowdown_pending | not_full_4B; false-positive guard candidate |

Price-only local peak without non-price evidence is not full 4B. It is a watch overlay and should not be used as an exit rule unless valuation/revision/capital/contract evidence appears.

## 16. 4C Protection Audit

```text
4C trigger count = 0
four_c_protection_label = not_applicable
reason = no hard thesis-break trigger asserted; this loop is Stage2 false-positive / local 4B watch calibration
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_rule
sector_specific_rule_candidate = false
reason = evidence_url_pending and source_proxy_only prevent promotion
```

Directional sector observation: in L3/R9 mobility C29, second-tier supplier rallies should not be promoted by OEM beta alone. The required bridge is actual volume/mix/order conversion and visible margin/FCF durability.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = false
candidate_label = C29_SECOND_TIER_AUTO_PARTS_MARGIN_BRIDGE_GUARD_HOLD
proposal_type = hold_for_primary_evidence
```

If primary evidence is later attached, a safe canonical rule candidate would be:

```text
For C29 second-tier auto-parts, Stage2-Actionable requires at least two of:
1. explicit customer/order/volume conversion,
2. mix/ASP/FX or cost-spread margin bridge,
3. actual earnings revision or OPM bridge,
4. low-MAE relative strength that is not merely OEM beta.
Otherwise classify as Stage2-Watch or Stage2-FalsePositive-Candidate.
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | score-return alignment |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 9.7 | -10.6 | 0.33 | mixed |
| P0b e2r_2_0_baseline_reference | 3 | 9.7 | -10.6 | 0.67 | too early in beta cases |
| P1 sector_specific_candidate_profile | 3 | 9.7 | -10.6 | 0.33 | kept; not promoted |
| P2 canonical_archetype_candidate_profile | 3 | 9.7 | -10.6 | 0.33 | hold pending evidence URL |
| P3 counterexample_guard_profile | 3 | 9.7 | -10.6 | 0.00 if weak bridge rows are demoted to Watch | best directional fit but not promoted |

## 20. Score-Return Alignment Matrix

| case_id | raw component summary | P0 score/stage | proposed guard score/stage | alignment |
|---|---|---|---|---|
| C29_R9L87_064960_POSITIVE_CONTROL | volume/mix moderate, customer quality moderate, margin bridge pending, low-MAE supportive | 72 / Stage2-Actionable | 72 / Stage2-Actionable | aligned |
| C29_R9L87_005850_HIGH_MAE_FADE | relative strength high, local peak, margin bridge pending | 73 / Stage2-Actionable | 66 / Stage2-Watch | proposed guard better avoids Green drift |
| C29_R9L87_204320_FALSE_POSITIVE | beta/relative strength only, weak MFE, margin evidence pending | 68 / Stage2-Actionable | 59 / Stage1-Watch | proposed guard better |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | SECOND_TIER_AUTO_PARTS_LIGHTING_BRAKE_MOTOR_VOLUME_MARGIN_BRIDGE_VS_THEME_FADE | 1 | 2 | 1 | 0 | 3 | 0 | 3 | 3 | 2 | false | false | still needs primary evidence URL and full-shard batch recomputation |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 2
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence]
residual_error_types_found: [C29_generic_beta_false_positive, C29_local_4B_watch_without_non_price_evidence]
new_axis_proposed: null
existing_axis_strengthened: null
existing_axis_weakened: null
existing_axis_kept: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: evidence_url_pending_and_source_proxy_only; batch_recalc_required_before_promotion
loop_contribution_label: counterexample_added
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- stock-web manifest and symbol profiles inspected
- tradable shard rows inspected for selected entry windows
- entry_date / entry_price separated from trigger_date
- MFE/MAE directional values calculated from visible stock-web rows and rounded
- corporate action candidate overlap checked against fetched profiles
```

Non-validation scope:

```text
- no live candidate scan
- no production scoring patch
- no brokerage/API execution
- no global threshold change
- primary DART/IR/evidence URLs not attached in this pass
- full 180D MFE/MAE should be recomputed by batch parser from complete CSV shards before promotion
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C29_margin_bridge_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Second-tier auto-parts beta creates weak-MFE/high-MAE false positives unless volume/mix/margin bridge is verified","Directional improvement but blocked from promotion by source_proxy_only","C29_R9L87_TRG_064960_S2|C29_R9L87_TRG_005850_S2|C29_R9L87_TRG_204320_S2",3,3,2,low,hold_for_primary_evidence,"not production; batch recomputation and evidence URL required"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration_with_batch_recalc_recommended"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C29_R9L87_064960_POSITIVE_CONTROL","symbol":"064960","company_name":"SNT모티브","round":"R9","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"SECOND_TIER_AUTO_PARTS_LIGHTING_BRAKE_MOTOR_VOLUME_MARGIN_BRIDGE_VS_THEME_FADE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C29_R9L87_TRG_064960_S2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_low_MAE_control","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"source_proxy_only; evidence URL required before promotion"}
{"row_type":"case","case_id":"C29_R9L87_005850_HIGH_MAE_FADE","symbol":"005850","company_name":"에스엘","round":"R9","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"SECOND_TIER_AUTO_PARTS_LIGHTING_BRAKE_MOTOR_VOLUME_MARGIN_BRIDGE_VS_THEME_FADE","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"C29_R9L87_TRG_005850_S2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"mixed_quick_MFE_then_fade","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"local 4B watch; not full 4B without non-price evidence"}
{"row_type":"case","case_id":"C29_R9L87_204320_FALSE_POSITIVE","symbol":"204320","company_name":"HL만도","round":"R9","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"SECOND_TIER_AUTO_PARTS_LIGHTING_BRAKE_MOTOR_VOLUME_MARGIN_BRIDGE_VS_THEME_FADE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C29_R9L87_TRG_204320_S2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"weak_MFE_high_MAE_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"generic mobility beta insufficient"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"C29_R9L87_TRG_064960_S2","case_id":"C29_R9L87_064960_POSITIVE_CONTROL","symbol":"064960","company_name":"SNT모티브","round":"R9","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"SECOND_TIER_AUTO_PARTS_LIGHTING_BRAKE_MOTOR_VOLUME_MARGIN_BRIDGE_VS_THEME_FADE","sector":"auto_parts_mobility","primary_archetype":"C29 volume/mix/margin bridge","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-16","entry_date":"2023-05-16","entry_price":50300,"evidence_available_at_that_date":"source-proxy: auto component volume/mix and controlled price path; primary DART/IR URL pending","evidence_source":"source_proxy_pending_primary_url","stage2_evidence_fields":["customer_or_order_quality","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["margin_bridge_pending","financial_visibility_pending"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064960/2023.csv","profile_path":"atlas/symbol_profiles/064/064960.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.2,"MFE_90D_pct":11.1,"MFE_180D_pct":11.1,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.6,"MAE_90D_pct":-6.4,"MAE_180D_pct":-7.5,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-06","peak_price":55900,"drawdown_after_peak_pct":-15.7,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_low_MAE_control","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29_R9L87_064960_2023-05-16_50300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"evidence_url_pending":true,"source_proxy_only":true,"batch_recalc_required":true}
{"row_type":"trigger","trigger_id":"C29_R9L87_TRG_005850_S2","case_id":"C29_R9L87_005850_HIGH_MAE_FADE","symbol":"005850","company_name":"에스엘","round":"R9","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"SECOND_TIER_AUTO_PARTS_LIGHTING_BRAKE_MOTOR_VOLUME_MARGIN_BRIDGE_VS_THEME_FADE","sector":"auto_parts_mobility","primary_archetype":"C29 local blowoff watch","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-16","entry_date":"2023-05-16","entry_price":37500,"evidence_available_at_that_date":"source-proxy: lighting/ADAS auto-parts operating leverage theme; primary DART/IR URL pending","evidence_source":"source_proxy_pending_primary_url","stage2_evidence_fields":["capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["margin_bridge_pending"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005850/2023.csv","profile_path":"atlas/symbol_profiles/005/005850.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.4,"MFE_90D_pct":13.1,"MFE_180D_pct":13.1,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.6,"MAE_90D_pct":-11.9,"MAE_180D_pct":-11.9,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-17","peak_price":42400,"drawdown_after_peak_pct":-22.1,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_watch_only","four_b_evidence_type":["price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"high_mae_success_local_4B_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29_R9L87_005850_2023-05-16_37500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"evidence_url_pending":true,"source_proxy_only":true,"batch_recalc_required":true}
{"row_type":"trigger","trigger_id":"C29_R9L87_TRG_204320_S2","case_id":"C29_R9L87_204320_FALSE_POSITIVE","symbol":"204320","company_name":"HL만도","round":"R9","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"SECOND_TIER_AUTO_PARTS_LIGHTING_BRAKE_MOTOR_VOLUME_MARGIN_BRIDGE_VS_THEME_FADE","sector":"auto_parts_mobility","primary_archetype":"C29 generic beta false-positive guard","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-FalsePositive-Candidate","trigger_date":"2023-07-31","entry_date":"2023-07-31","entry_price":46150,"evidence_available_at_that_date":"source-proxy: generic mobility supplier beta with unverified margin bridge; primary DART/IR URL pending","evidence_source":"source_proxy_pending_primary_url","stage2_evidence_fields":["relative_strength","capacity_or_volume_route_pending"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/204/204320/2023.csv","profile_path":"atlas/symbol_profiles/204/204320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.9,"MFE_90D_pct":4.9,"MFE_180D_pct":4.9,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.4,"MAE_90D_pct":-13.4,"MAE_180D_pct":-13.4,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-31","peak_price":48400,"drawdown_after_peak_pct":-17.5,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"false_positive_guard_candidate","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"failed_rerating_generic_beta","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29_R9L87_204320_2023-07-31_46150","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"evidence_url_pending":true,"source_proxy_only":true,"batch_recalc_required":true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9L87_064960_POSITIVE_CONTROL","trigger_id":"C29_R9L87_TRG_064960_S2","symbol":"064960","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":7,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":7,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable","changed_components":[],"component_delta_explanation":"low-MAE control does not justify new promotion without primary evidence URL","MFE_90D_pct":11.1,"MAE_90D_pct":-6.4,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"C29_counterexample_guard_profile","case_id":"C29_R9L87_005850_HIGH_MAE_FADE","trigger_id":"C29_R9L87_TRG_005850_S2","symbol":"005850","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":9,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":7,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":66,"stage_label_after":"Stage2-Watch","changed_components":["margin_bridge_score","revision_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"quick price response without verified margin bridge becomes local 4B watch, not Green path","MFE_90D_pct":13.1,"MAE_90D_pct":-11.9,"score_return_alignment_label":"mixed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"C29_counterexample_guard_profile","case_id":"C29_R9L87_204320_FALSE_POSITIVE","trigger_id":"C29_R9L87_TRG_204320_S2","symbol":"204320","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":7,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":68,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":59,"stage_label_after":"Stage1-Watch","changed_components":["margin_bridge_score","revision_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"generic mobility beta with weak MFE and double-digit MAE should not receive actionable bridge credit","MFE_90D_pct":4.9,"MAE_90D_pct":-13.4,"score_return_alignment_label":"proposed_guard_better","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight row

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C29_margin_bridge_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Require volume/mix/margin bridge for second-tier auto-parts Stage2-Actionable","weak-MFE/high-MAE false-positive rows improve if demoted to Watch","C29_R9L87_TRG_064960_S2|C29_R9L87_TRG_005850_S2|C29_R9L87_TRG_204320_S2",3,3,2,low,hold_for_primary_evidence,"do_not_propose_new_weight_delta=true"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R9","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["C29_generic_beta_false_positive","C29_local_4B_watch_without_non_price_evidence"],"loop_contribution_label":"counterexample_added","do_not_propose_new_weight_delta":true}
```

### 25.7 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"C29_R9L87_PRIMARY_EVIDENCE_TODO","symbol":"MULTI","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reason":"primary DART/IR evidence URLs were not attached in this run; keep shadow rows out of promotion until evidence_url_pending=false and source_proxy_only=false","price_source":"Songdaiki/stock-web","usage":"not_weight_promotion"}
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
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/&lt;prefix&gt;/&lt;ticker&gt;/&lt;year&gt;.csv.
- Symbol profile pattern: atlas/symbol_profiles/&lt;prefix&gt;/&lt;ticker&gt;.json.

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
11. For this MD specifically, recompute MFE/MAE from the complete CSV shards before any promotion and attach primary DART/IR/earnings URLs.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R9
completed_loop = 87
next_round = R10
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
computed_next_round = R10
computed_next_loop = 87
```

## 28. Source Notes

Source files inspected during this run:

```text
MAIN EXECUTION PROMPT:
https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt

NO-REPEAT INDEX:
https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md

stock_agent registry:
data/e2r/calibration/v12/v12_md_registry.jsonl

stock-web manifest:
atlas/manifest.json

stock-web profiles:
atlas/symbol_profiles/064/064960.json
atlas/symbol_profiles/005/005850.json
atlas/symbol_profiles/204/204320.json

stock-web price shards:
atlas/ohlcv_tradable_by_symbol_year/064/064960/2023.csv
atlas/ohlcv_tradable_by_symbol_year/005/005850/2023.csv
atlas/ohlcv_tradable_by_symbol_year/204/204320/2023.csv
```

This MD is a historical calibration artifact, not an investment recommendation and not a production scoring patch.

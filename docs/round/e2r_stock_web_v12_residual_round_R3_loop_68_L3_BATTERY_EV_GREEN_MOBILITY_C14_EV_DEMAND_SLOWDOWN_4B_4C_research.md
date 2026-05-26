# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R3
loop = 68
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = EU_EV_DEMAND_SLOWDOWN_SINGLE_QUARTER_GUIDANCE, CATHODE_DEMAND_POLICY_HARD4C_AFTER_PRICE_ONLY_BLOWOFF, CATHODE_CUSTOMER_DEMAND_AND_MARGIN_REPEATED_BREAK, CELL_DEMAND_SLOWDOWN_WITH_POLICY_ESS_RECOVERY_OPTIONALITY
loop_objective = coverage_gap_fill / counterexample_mining / 4C_thesis_break_timing_test / 4B_non_price_requirement_stress_test / sector_specific_rule_discovery
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is historical calibration research only. It is not a current/live candidate scan, not a recommendation, not an auto-trading instruction, and not a repository patch.

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

The loop does not re-prove the global guard that price-only blowoff must not promote Stage2/Stage3. It stress-tests a residual C14 issue: in battery/EV names, **generic EV-demand slowdown evidence is not the same thing as a hard thesis break**. A first demand warning is often a flashing amber light, not a collapsed bridge. Hard 4C needs the road surface itself to give way: repeated margin break, utilization deterioration, customer/order cut, or policy/customer route failure.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R3
loop = 68
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
selection_mode = auto_coverage_gap_fill
auto_selected_coverage_gap = C14_EV_DEMAND_SLOWDOWN_4B_4C had insufficient positive/counterexample split after C13 AMPC/JV work.
```

## 3. Previous Coverage / Duplicate Avoidance Check

The immediately prior MD in this local run covered `C13_BATTERY_JV_UTILIZATION_AMPC_IRA`, so this loop deliberately moves into `C14_EV_DEMAND_SLOWDOWN_4B_4C`. Some large-cap battery symbols overlap the sector universe, but the trigger family is different: this file evaluates demand-slowdown 4B/4C timing, not AMPC/JV utilization promotion.

```text
same_canonical_archetype_research = allowed_and_required
same_symbol_same_trigger_date_research = low_value_or_duplicate
new_canonical_archetype_count = 1
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
reused_case_count = 0
duplicate_low_value_loop = false
```

## 4. Stock-Web OHLC Input / Price Source Validation

| source | source_url | manifest_path | schema_path | universe_path | manifest_max_date | price_basis | price_adjustment_status | calibration_shard_root | raw_shard_root | tradable_row_count | raw_row_count | symbol_count | markets |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Songdaiki/stock-web | https://github.com/Songdaiki/stock-web | atlas/manifest.json | atlas/schema.json | atlas/universe/all_symbols.csv | 2026-02-20 | tradable_raw | raw_unadjusted_marcap | atlas/ohlcv_tradable_by_symbol_year | atlas/ohlcv_raw_by_symbol_year | 14354401 | 15214118 | 5414 | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |

Validation notes:

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

## 5. Historical Eligibility Gate

All representative rows below satisfy:

```text
- trigger_date is historical.
- entry_date exists in the stock-web tradable shard.
- at least 180 forward trading rows are available by manifest max_date.
- high / low / close / volume are present.
- MFE/MAE 30D, 90D, and 180D were calculated.
- No profile-level corporate-action candidate overlaps the 180D calibration window.
```

1Y/2Y fields are not used for weight calibration in this loop. The core calibration window is 180D.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | maps_to_canonical_archetype_id | interpretation |
|---|---|---|
| EU_EV_DEMAND_SLOWDOWN_SINGLE_QUARTER_GUIDANCE | C14_EV_DEMAND_SLOWDOWN_4B_4C | First demand warning; generally 4B/watch unless repeated break follows. |
| CATHODE_DEMAND_POLICY_HARD4C_AFTER_PRICE_ONLY_BLOWOFF | C14_EV_DEMAND_SLOWDOWN_4B_4C | Cathode-name hard 4C after policy/demand risk joins broken relative strength. |
| CATHODE_CUSTOMER_DEMAND_AND_MARGIN_REPEATED_BREAK | C14_EV_DEMAND_SLOWDOWN_4B_4C | Hard 4C after repeated margin/customer-demand break. |
| CELL_DEMAND_SLOWDOWN_WITH_POLICY_ESS_RECOVERY_OPTIONALITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | Cell-maker slowdown with recovery optionality; guard against premature hard 4C. |

## 7. Case Selection Summary

| case_id | symbol | company_name | role | case_type | best_trigger | current_profile_verdict | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R3L68_C14_006400_20240731_EU_DEMAND_GUIDANCE_TOO_EARLY_4C | 006400 | 삼성SDI | counterexample | 4B_too_early | TR_C14_006400_20240731_STAGE4B_TOO_EARLY | current_profile_false_positive | Counterexample to immediate hard 4C from single-quarter EV-demand pressure. |
| R3L68_C14_247540_20241106_CATHODE_POLICY_DEMAND_HARD4C | 247540 | 에코프로비엠 | positive | 4C_success | TR_C14_247540_20241106_HARD4C | current_profile_correct | Positive hard-4C protection case after demand/policy risk joined broken cathode momentum. |
| R3L68_C14_066970_20241220_REPEATED_MARGIN_HARD4C | 066970 | 엘앤에프 | positive | 4C_success | TR_C14_066970_20241220_HARD4C | current_profile_correct | Positive hard-4C case and contrast to the earlier 2024-11-07 4B watch row. |
| R3L68_C14_373220_20241115_CELL_DEMAND_HARD4C_COUNTEREXAMPLE | 373220 | LG에너지솔루션 | counterexample | 4B_too_early | TR_C14_373220_20241115_STAGE4B_COUNTER | current_profile_4B_too_early | Counterexample: cell makers retain policy/ESS/customer recovery optionality; generic EV demand pressure routes to 4B watch first. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
calibration_usable_case_count = 4
calibration_usable_trigger_count = 5
representative_trigger_count = 4
```

The balance is deliberate. C14 can be dangerous in both directions. If the model ignores demand slowdown, it holds broken cathode names too long. If it treats every slowdown headline as hard 4C, it can exit or penalize cell makers too early while the stock still has a rebound window.

## 9. Evidence Source Map

| symbol | evidence family | stage separation |
|---|---|---|
| 006400 | Europe/EV-demand slowdown and shipment/margin pressure around 2Q24 commentary | 4B watch only; single-quarter guidance evidence was not enough for hard 4C. |
| 247540 | Cathode demand/policy risk after relative-strength break and prior valuation blowoff | Hard 4C positive. |
| 066970 | Initial margin/customer-demand warning followed by repeated break | 2024-11-07 is 4B watch; 2024-12-20 becomes hard 4C. |
| 373220 | Cell-maker EV demand pressure with policy/ESS/customer recovery optionality | 4B watch / counterexample to generic hard 4C. |

## 10. Price Data Source Map

| symbol | profile_path | key_price_rows | window_status |
| --- | --- | --- | --- |
| 006400 | atlas/symbol_profiles/006/006400.json | 2024-07-31 c=319500; 2024-09-30 h=393500; 2025-04-09 l≈170000 | clean_180D_window |
| 247540 | atlas/symbol_profiles/247/247540.json | 2024-11-06 c=163100; 2024-11-08 h=167200; 2025-05-27 l=81100 | clean_180D_window |
| 066970 | atlas/symbol_profiles/066/066970.json | 2024-11-07 c=106000; 2024-12-20 c=90700; 2025-05-26 l=47000 | clean_180D_window |
| 373220 | atlas/symbol_profiles/373/373220.json | 2024-11-15 c=371000; 2024-11-25 h=425000; 2025-05-23 l≈266000 | clean_180D_window |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | verdict | aggregate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TR_C14_006400_20240731_STAGE4B_TOO_EARLY | 006400 | Stage4B-Watch | 2024-07-30 | 2024-07-31 | 319500 | 23.16 | -26.29 | 23.16 | -46.79 | current_profile_false_positive | representative |
| TR_C14_247540_20241106_HARD4C | 247540 | Hard4C | 2024-11-06 | 2024-11-06 | 163100 | 2.51 | -31.82 | 2.51 | -50.28 | current_profile_correct | representative |
| TR_C14_066970_20241107_STAGE4B_WATCH | 066970 | Stage4B-Watch | 2024-11-07 | 2024-11-07 | 106000 | 19.15 | -36.04 | 19.15 | -55.66 | current_profile_4C_too_early | label_comparison_only |
| TR_C14_066970_20241220_HARD4C | 066970 | Hard4C | 2024-12-20 | 2024-12-20 | 90700 | 3.64 | -40.68 | 3.64 | -48.18 | current_profile_correct | representative |
| TR_C14_373220_20241115_STAGE4B_COUNTER | 373220 | Stage4B-Watch | 2024-11-15 | 2024-11-15 | 371000 | 14.56 | -11.46 | 14.56 | -28.3 | current_profile_4B_too_early | representative |

## 12. Trigger-Level OHLC Backtest Tables

Representative aggregation includes rows where `dedupe_for_aggregate=true`, `aggregate_group_role=representative`, and `calibration_usable=true`.

| trigger_id | entry | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | peak | drawdown after peak | conclusion |
|---|---:|---:|---:|---:|---|---:|---|
| TR_C14_006400_20240731_STAGE4B_TOO_EARLY | 319,500 | +18.94 / -5.16 | +23.16 / -26.29 | +23.16 / -46.79 | 393,500 on 2024-09-30 | -56.80 | Hard 4C too early; 4B watch was right. |
| TR_C14_247540_20241106_HARD4C | 163,100 | +2.51 / -27.53 | +2.51 / -31.82 | +2.51 / -50.28 | 167,200 on 2024-11-08 | -51.50 | Hard 4C protection worked. |
| TR_C14_066970_20241107_STAGE4B_WATCH | 106,000 | +19.15 / -23.58 | +19.15 / -36.04 | +19.15 / -55.66 | 126,300 on 2024-11-12 | -62.79 | First warning still had bounce risk; 4B watch only. |
| TR_C14_066970_20241220_HARD4C | 90,700 | +3.64 / -15.44 | +3.64 / -40.68 | +3.64 / -48.18 | 94,000 on 2025-01-21 | -50.00 | Repeated break made hard 4C cleaner. |
| TR_C14_373220_20241115_STAGE4B_COUNTER | 371,000 | +14.56 / -8.22 | +14.56 / -11.46 | +14.56 / -28.30 | 425,000 on 2024-11-25 | -37.41 | Cell-maker hard 4C too early; watch only. |

## 13. Current Calibrated Profile Stress Test

| question | answer |
|---|---|
| How would current profile judge these? | It should block price-only 4B, but may still over-promote generic EV-demand slowdown to hard 4C unless C14-specific evidence gates exist. |
| Did that align with MFE/MAE? | Mixed. 247540/066970 hard 4C aligned. 006400/373220 hard 4C would be false-positive or too early because post-trigger MFE was meaningful. |
| Was Stage2 bonus too high? | Not central. These are 4B/4C risk rows, not Stage2 promotion rows. |
| Yellow threshold 75? | Not central. The issue is thesis-break routing, not Yellow promotion. |
| Green threshold 87 / revision 55? | Not central. No Stage3-Green promotion is proposed. |
| Price-only blowoff guard? | Kept and strengthened. It is necessary but insufficient for C14; non-price risk must be typed by evidence family. |
| Full 4B non-price requirement? | Strengthened. 4B should accept non-price slowdown evidence, but not automatically become hard 4C. |
| Hard 4C routing? | Needs C14-specific guard: repeated margin/utilization/customer-order break, not generic demand commentary. |

## 14. Stage2 / Yellow / Green Comparison

No Stage2/Stage3 promotion is proposed. Stage3-Green lateness is therefore not the active axis in this loop.

```text
green_lateness_ratio = not_applicable
reason = C14 loop is 4B/4C risk-routing calibration, not positive Stage3-Green timing.
```

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| TR_C14_006400_20240731_STAGE4B_TOO_EARLY | 0.00 | 0.00 | Hard 4C too early; 4B watch only. |
| TR_C14_247540_20241106_HARD4C | null | null | Hard 4C row after non-price evidence; not a pure 4B timing row. |
| TR_C14_066970_20241107_STAGE4B_WATCH | 0.00 | 0.00 | Initial margin break too early for hard 4C. |
| TR_C14_066970_20241220_HARD4C | null | null | Hard 4C after repeated margin/customer-demand break. |
| TR_C14_373220_20241115_STAGE4B_COUNTER | 0.00 | 0.00 | Generic cell demand slowdown is 4B watch, not hard 4C. |

## 16. 4C Protection Audit

| trigger_id | protection label | interpretation |
|---|---|---|
| TR_C14_247540_20241106_HARD4C | hard_4c_success | Low MFE and deep 180D MAE validate hard 4C. |
| TR_C14_066970_20241220_HARD4C | hard_4c_success | Waiting for repeated break reduced MFE and still captured large downside. |
| TR_C14_006400_20240731_STAGE4B_TOO_EARLY | thesis_break_watch_only | Later downside existed, but hard 4C at first warning would have been premature. |
| TR_C14_066970_20241107_STAGE4B_WATCH | thesis_break_watch_only | Initial row was not yet hard 4C. |
| TR_C14_373220_20241115_STAGE4B_COUNTER | thesis_break_watch_only | Cell-maker recovery optionality blocks hard 4C. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L3_EV_DEMAND_SLOWDOWN_HARD4C_REQUIRES_MARGIN_OR_UTILIZATION_BREAK
proposal_type = sector_shadow_only
production_scoring_changed = false
```

Candidate rule:

> In L3 battery/EV names, generic EV demand slowdown evidence routes to Stage4B-watch unless at least one hard thesis-break family is present: repeated margin bridge failure, utilization/capex cut evidence, customer/order cut, qualification failure, or policy/customer route break.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
```

Candidate C14 rule:

```text
if evidence_family == single_quarter_guidance_or_generic_demand_slowdown:
    route = Stage4B-Watch
    block_hard_4C = true unless repeated_margin_or_utilization_break == true

if evidence_family includes repeated_margin_break OR utilization_cut OR customer_order_cut OR thesis_evidence_broken:
    route = Hard4C candidate

if issuer_type == battery_cell_maker and recovery_optionality in [policy, ESS, customer_model_cadence, AMPC]:
    require additional hard evidence before Hard4C
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | profile_hypothesis | changed_axes | changed_thresholds | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | avg_four_b_local_peak_proximity | avg_four_b_full_window_peak_proximity | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | Uses current global guards but lacks C14-specific separation of single-quarter EV slowdown vs repeated margin/utilization break. | none | none | 4 | 006400:2024-07-31/247540:2024-11-06/066970:2024-11-07_or_2024-12-20/373220:2024-11-15 | 10.97 | -27.56 | 10.97 | -43.39 | 2/4 if generic demand slowdown promotes hard 4C | 0 | 0 | not_applicable | 0.0 | 0.0 | mixed_without_C14_guard |
| P0b_e2r_2_0_baseline_reference | rollback_reference | Would likely under-block price/narrative blowoff and over-react to generic EV slowdown. | rollback | legacy | 4 | earlier and noisier | 10.97 | -27.56 | 10.97 | -43.39 | likely higher than P0 | 1 | 0 | not_applicable | 0.0 | 0.0 | worse |
| P1_L3_sector_specific_candidate_profile | sector_specific | For L3, EV-demand slowdown routes to 4B unless margin/utilization/customer-order break closes hard 4C. | c14_guidance_only_to_4b_watch/c14_repeated_margin_break_to_hard4c | hard_4c_requires_margin_or_utilization_break=true | 4 | 006400:4B watch/247540:Hard4C/066970:Hard4C only after 2024-12-20/373220:4B watch | 6.21 | -28.56 | 6.21 | -43.89 | 0/4 in this small sample | 0 | 0 | not_applicable | 0.0 | 0.0 | improves_signal_selectivity |
| P2_C14_canonical_archetype_candidate_profile | canonical_archetype_specific | C14 differentiates cathode hard-4C from cell-maker 4B watch due recovery optionality. | cathode_repeated_margin_break_bonus/cell_maker_recovery_optionality_guard | hard_4c_repeated_break_min=2_evidence_families | 4 | same as P1 | 6.21 | -28.56 | 6.21 | -43.89 | 0/4 in this small sample | 0 | 0 | not_applicable | 0.0 | 0.0 | best_for_C14 |
| P3_C14_counterexample_guard_profile | counterexample_guard | Blocks hard 4C if first demand-warning row has high rebound optionality and lacks margin/customer-order break. | high_MFE_counterexample_guard | hard_4c_block_if_guidance_only_and_MFE90_counterexample_family=true | 4 | 006400/373220 stay watch; 247540/066970 hard 4C | 6.21 | -28.56 | 6.21 | -43.89 | 0/4 in this small sample | 0 | 0 | not_applicable | 0.0 | 0.0 | guard_useful_but_sample_small |

## 20. Score-Return Alignment Matrix

| trigger_id | stage_label_after | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | alignment |
| --- | --- | --- | --- | --- | --- | --- |
| TR_C14_006400_20240731_STAGE4B_TOO_EARLY | Stage4B-Watch | 23.16 | -26.29 | 23.16 | -46.79 | early_4b_counterexample_high_MFE_before_breakdown |
| TR_C14_247540_20241106_HARD4C | Hard4C | 2.51 | -31.82 | 2.51 | -50.28 | hard_4c_protection_success |
| TR_C14_066970_20241107_STAGE4B_WATCH | Stage4B-Watch | 19.15 | -36.04 | 19.15 | -55.66 | initial_4b_watch_high_MFE_before_confirmed_break |
| TR_C14_066970_20241220_HARD4C | Hard4C | 3.64 | -40.68 | 3.64 | -48.18 | hard_4c_protection_success |
| TR_C14_373220_20241115_STAGE4B_COUNTER | Stage4B-Watch | 14.56 | -11.46 | 14.56 | -28.3 | cell_maker_4b_counterexample |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | multiple_C14_fine_archetypes | 2 | 2 | 3 | 2 | 4 | 0 | 5 | 4 | 2 | True | True | C14 now has positive hard-4C and counterexample 4B-watch coverage; still needs C12/C14 customer call-off split in next loop. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 4
new_trigger_family_count: 4
positive_case_count: 2
counterexample_count: 2
current_profile_error_count: 2
tested_existing_calibrated_axes:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - price_only_blowoff_blocks_positive_stage
residual_error_types_found:
  - guidance_only_hard4c_false_positive
  - initial_margin_break_too_early_for_hard4c
  - cell_maker_recovery_optionality_counterexample
new_axis_proposed:
  - c14_guidance_only_ev_slowdown_routes_to_4b_watch
  - c14_repeated_margin_or_utilization_break_required_for_hard4c
  - c14_cell_maker_recovery_optionality_guard
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
diversity_score_summary: avg=34.0; new canonical C14; 4 symbols; 4 trigger families; no duplicate same symbol+trigger+entry group
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-web manifest and schema assumptions.
- Symbol profile availability and 180D forward windows.
- Actual OHLC entry rows and forward high/low windows from stock-web tradable shards.
- Representative trigger-level 30D/90D/180D MFE/MAE.
- Dedupe by same_entry_group_id.
- Positive/counterexample split.
```

Not validated in this MD:

```text
- No production scoring code was opened.
- No source runner or live scan was executed.
- No brokerage/API connection was used.
- Exact intraday disclosure timestamps are not used; if timestamp is uncertain, next-trading-day entry is preferred or the row is treated conservatively.
- 1Y/2Y windows are not used for weight calibration in this loop.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c14_guidance_only_ev_slowdown_routes_to_4b_watch,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,false,true,+1,Single-quarter EV demand/guidance pressure produced high MFE in 006400 and 373220; hard 4C should wait for thesis break.,reduced false positives without weakening hard 4C positives,"TR_C14_006400_20240731_STAGE4B_TOO_EARLY|TR_C14_373220_20241115_STAGE4B_COUNTER",4,4,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,c14_repeated_margin_or_utilization_break_required_for_hard4c,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,not_explicit,explicit,+1,247540 and 066970 hard 4C rows had low MFE and large MAE after repeated/non-price evidence.,improved hard 4C precision,"TR_C14_247540_20241106_HARD4C|TR_C14_066970_20241220_HARD4C",4,4,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,c14_cell_maker_recovery_optionality_guard,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,false,true,+1,Cell-maker demand slowdown retained policy/ESS/customer optionality; generic slowdown should not auto-hard-4C.,blocked LGES-style false hard 4C,TR_C14_373220_20241115_STAGE4B_COUNTER,4,4,2,low,sector_shadow_only,not production; post-calibrated residual
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","source_name":"FinanceData/marcap","min_date":"1995-05-02","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"inactive_or_delisted_like_symbol_count":2546,"markets":["KONEX","KOSDAQ","KOSDAQ GLOBAL","KOSPI"],"validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R3L68_C14_006400_20240731_EU_DEMAND_GUIDANCE_TOO_EARLY_4C","symbol":"006400","company_name":"삼성SDI","round":"R3","loop":"68","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EU_EV_DEMAND_SLOWDOWN_SINGLE_QUARTER_GUIDANCE","case_type":"4B_too_early","positive_or_counterexample":"counterexample","best_trigger":"TR_C14_006400_20240731_STAGE4B_TOO_EARLY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Guidance-only demand slowdown had +23.16% 90D MFE before later breakdown; hard 4C would be too early.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Counterexample to immediate hard 4C from single-quarter EV-demand pressure."}
{"row_type":"case","case_id":"R3L68_C14_247540_20241106_CATHODE_POLICY_DEMAND_HARD4C","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"68","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_DEMAND_POLICY_HARD4C_AFTER_PRICE_ONLY_BLOWOFF","case_type":"4C_success","positive_or_counterexample":"positive","best_trigger":"TR_C14_247540_20241106_HARD4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Hard 4C had only +2.51% 90D MFE and -31.82% 90D MAE; 180D MAE reached -50.28%.","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Positive hard-4C protection case after demand/policy risk joined broken cathode momentum."}
{"row_type":"case","case_id":"R3L68_C14_066970_20241220_REPEATED_MARGIN_HARD4C","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"68","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_CUSTOMER_DEMAND_AND_MARGIN_REPEATED_BREAK","case_type":"4C_success","positive_or_counterexample":"positive","best_trigger":"TR_C14_066970_20241220_HARD4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Waiting for repeated margin/demand break reduced MFE to +3.64% while 180D MAE remained -48.18%.","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Positive hard-4C case and contrast to the earlier 2024-11-07 4B watch row."}
{"row_type":"case","case_id":"R3L68_C14_373220_20241115_CELL_DEMAND_HARD4C_COUNTEREXAMPLE","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"68","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CELL_DEMAND_SLOWDOWN_WITH_POLICY_ESS_RECOVERY_OPTIONALITY","case_type":"4B_too_early","positive_or_counterexample":"counterexample","best_trigger":"TR_C14_373220_20241115_STAGE4B_COUNTER","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Cell maker demand-pressure evidence produced material drawdown, but +14.56% MFE before the drawdown means hard 4C was too early.","current_profile_verdict":"current_profile_4B_too_early","price_source":"Songdaiki/stock-web","notes":"Counterexample: cell makers retain policy/ESS/customer recovery optionality; generic EV demand pressure routes to 4B watch first."}
{"row_type":"trigger","trigger_id":"TR_C14_006400_20240731_STAGE4B_TOO_EARLY","case_id":"R3L68_C14_006400_20240731_EU_DEMAND_GUIDANCE_TOO_EARLY_4C","symbol":"006400","company_name":"삼성SDI","round":"R3","loop":"68","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EU_EV_DEMAND_SLOWDOWN_SINGLE_QUARTER_GUIDANCE","sector":"battery_cell","primary_archetype":"EV demand slowdown 4B/4C timing","loop_objective":"counterexample_mining|4C_thesis_break_timing_test|sector_specific_rule_discovery","trigger_type":"Stage4B-Watch","trigger_date":"2024-07-30","entry_date":"2024-07-31","entry_price":319500,"evidence_available_at_that_date":"2Q24/Europe EV-demand slowdown and battery shipment pressure were visible, but the evidence did not yet close a hard thesis-break route.","evidence_source":"public quarterly earnings / EV demand slowdown commentary family; stock-web OHLC validation is the quantitative source","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv","profile_path":"atlas/symbol_profiles/006/006400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.94,"MFE_90D_pct":23.16,"MFE_180D_pct":23.16,"MFE_1Y_pct":"not_computed_for_weight","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-5.16,"MAE_90D_pct":-26.29,"MAE_180D_pct":-46.79,"MAE_1Y_pct":"not_computed_for_weight","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-30","peak_price":393500,"drawdown_after_peak_pct":-56.8,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"hard_4c_too_early_stage4b_watch_only","four_b_evidence_type":["revision_slowdown","margin_or_backlog_slowdown","price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"early_4b_counterexample_high_MFE_before_breakdown","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"006400_20240731_319500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_C14_247540_20241106_HARD4C","case_id":"R3L68_C14_247540_20241106_CATHODE_POLICY_DEMAND_HARD4C","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"68","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_DEMAND_POLICY_HARD4C_AFTER_PRICE_ONLY_BLOWOFF","sector":"battery_cathode","primary_archetype":"EV demand slowdown 4B/4C timing","loop_objective":"4C_thesis_break_timing_test|sector_specific_rule_discovery|coverage_gap_fill","trigger_type":"Hard4C","trigger_date":"2024-11-06","entry_date":"2024-11-06","entry_price":163100,"evidence_available_at_that_date":"Post-bubble cathode path had already lost relative strength; EV-demand and policy-risk overlay turned prior price blowoff into thesis-break risk.","evidence_source":"public earnings / cathode demand slowdown / policy-risk evidence family; stock-web OHLC validation is the quantitative source","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.51,"MFE_90D_pct":2.51,"MFE_180D_pct":2.51,"MFE_1Y_pct":"not_computed_for_weight","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-27.53,"MAE_90D_pct":-31.82,"MAE_180D_pct":-50.28,"MAE_1Y_pct":"not_computed_for_weight","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-08","peak_price":167200,"drawdown_after_peak_pct":-51.5,"green_lateness_ratio":"not_applicable_4C_overlay_row","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"good_full_window_4C_after_non_price_evidence","four_b_evidence_type":["valuation_blowoff","revision_slowdown","positioning_overheat"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"hard_4c_protection_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"247540_20241106_163100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_C14_066970_20241107_STAGE4B_WATCH","case_id":"R3L68_C14_066970_20241220_REPEATED_MARGIN_HARD4C","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"68","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_CUSTOMER_DEMAND_AND_MARGIN_REPEATED_BREAK","sector":"battery_cathode","primary_archetype":"EV demand slowdown 4B/4C timing","loop_objective":"4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage4B-Watch","trigger_date":"2024-11-07","entry_date":"2024-11-07","entry_price":106000,"evidence_available_at_that_date":"Initial cathode customer-demand/margin risk was visible, but near-term bounce risk remained large.","evidence_source":"public earnings / customer-demand and cathode-margin evidence family; stock-web OHLC validation is the quantitative source","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":19.15,"MFE_90D_pct":19.15,"MFE_180D_pct":19.15,"MFE_1Y_pct":"not_computed_for_weight","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-23.58,"MAE_90D_pct":-36.04,"MAE_180D_pct":-55.66,"MAE_1Y_pct":"not_computed_for_weight","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-12","peak_price":126300,"drawdown_after_peak_pct":-62.79,"green_lateness_ratio":"not_applicable_4B_overlay_row","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"price_only_or_initial_margin_4B_too_early_for_hard_4C","four_b_evidence_type":["revision_slowdown","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"initial_4b_watch_high_MFE_before_confirmed_break","current_profile_verdict":"current_profile_4C_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"066970_20241107_106000","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":"same_case_label_comparison_pre_hard4c","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_C14_066970_20241220_HARD4C","case_id":"R3L68_C14_066970_20241220_REPEATED_MARGIN_HARD4C","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"68","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_CUSTOMER_DEMAND_AND_MARGIN_REPEATED_BREAK","sector":"battery_cathode","primary_archetype":"EV demand slowdown 4B/4C timing","loop_objective":"4C_thesis_break_timing_test|sector_specific_rule_discovery","trigger_type":"Hard4C","trigger_date":"2024-12-20","entry_date":"2024-12-20","entry_price":90700,"evidence_available_at_that_date":"The earlier bounce had failed; repeated margin/customer-demand weakness and broken relative strength made hard 4C more defensible.","evidence_source":"public earnings / repeated cathode-margin weakness evidence family; stock-web OHLC validation is the quantitative source","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.64,"MFE_90D_pct":3.64,"MFE_180D_pct":3.64,"MFE_1Y_pct":"not_computed_for_weight","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-15.44,"MAE_90D_pct":-40.68,"MAE_180D_pct":-48.18,"MAE_1Y_pct":"not_computed_for_weight","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-01-21","peak_price":94000,"drawdown_after_peak_pct":-50.0,"green_lateness_ratio":"not_applicable_4C_overlay_row","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"good_full_window_4C_after_repeated_margin_break","four_b_evidence_type":["revision_slowdown","margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"hard_4c_protection_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"066970_20241220_90700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_C14_373220_20241115_STAGE4B_COUNTER","case_id":"R3L68_C14_373220_20241115_CELL_DEMAND_HARD4C_COUNTEREXAMPLE","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"68","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CELL_DEMAND_SLOWDOWN_WITH_POLICY_ESS_RECOVERY_OPTIONALITY","sector":"battery_cell","primary_archetype":"EV demand slowdown 4B/4C timing","loop_objective":"counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage4B-Watch","trigger_date":"2024-11-15","entry_date":"2024-11-15","entry_price":371000,"evidence_available_at_that_date":"EV demand pressure and cell-margin risk were visible; however, cell makers retained policy/ESS/customer recovery optionality, so hard 4C was not fully closed.","evidence_source":"public battery-cell demand slowdown / capex-prudence evidence family; stock-web OHLC validation is the quantitative source","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv","profile_path":"atlas/symbol_profiles/373/373220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.56,"MFE_90D_pct":14.56,"MFE_180D_pct":14.56,"MFE_1Y_pct":"not_computed_for_weight","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-8.22,"MAE_90D_pct":-11.46,"MAE_180D_pct":-28.3,"MAE_1Y_pct":"not_computed_for_weight","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-25","peak_price":425000,"drawdown_after_peak_pct":-37.41,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"hard_4c_too_early_cell_recovery_optionality","four_b_evidence_type":["revision_slowdown","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"cell_maker_4b_counterexample","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"373220_20241115_371000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C14_shadow","case_id":"R3L68_C14_006400_20240731_EU_DEMAND_GUIDANCE_TOO_EARLY_4C","trigger_id":"TR_C14_006400_20240731_STAGE4B_TOO_EARLY","symbol":"006400","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":36,"revision_score":46,"relative_strength_score":42,"customer_quality_score":48,"policy_or_regulatory_score":0,"valuation_repricing_score":58,"execution_risk_score":55,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":79.0,"stage_label_before":"Hard4C_or_Red","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":36,"revision_score":42,"relative_strength_score":40,"customer_quality_score":48,"policy_or_regulatory_score":0,"valuation_repricing_score":50,"execution_risk_score":55,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68.0,"stage_label_after":"Stage4B-Watch","changed_components":["hard_4c_requires_actual_margin_or_utilization_break","guidance_only_to_4b_watch"],"component_delta_explanation":"Guidance-only EV slowdown is downgraded from hard 4C to 4B watch because 90D MFE was +23.16%.","MFE_90D_pct":23.16,"MAE_90D_pct":-26.29,"score_return_alignment_label":"early_4b_counterexample_high_MFE_before_breakdown","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C14_shadow","case_id":"R3L68_C14_247540_20241106_CATHODE_POLICY_DEMAND_HARD4C","trigger_id":"TR_C14_247540_20241106_HARD4C","symbol":"247540","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":58,"revision_score":62,"relative_strength_score":22,"customer_quality_score":35,"policy_or_regulatory_score":64,"valuation_repricing_score":78,"execution_risk_score":72,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":88.0,"stage_label_before":"Hard4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":62,"revision_score":64,"relative_strength_score":20,"customer_quality_score":34,"policy_or_regulatory_score":66,"valuation_repricing_score":78,"execution_risk_score":74,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":91.0,"stage_label_after":"Hard4C","changed_components":["cathode_policy_demand_hard4c_confirmed"],"component_delta_explanation":"Demand/policy risk sits on top of broken cathode relative strength; hard 4C remains valid.","MFE_90D_pct":2.51,"MAE_90D_pct":-31.82,"score_return_alignment_label":"hard_4c_protection_success","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C14_shadow","case_id":"R3L68_C14_066970_20241220_REPEATED_MARGIN_HARD4C","trigger_id":"TR_C14_066970_20241107_STAGE4B_WATCH","symbol":"066970","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":55,"revision_score":52,"relative_strength_score":35,"customer_quality_score":40,"policy_or_regulatory_score":0,"valuation_repricing_score":50,"execution_risk_score":64,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82.0,"stage_label_before":"Hard4C_or_Red","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":52,"revision_score":50,"relative_strength_score":35,"customer_quality_score":40,"policy_or_regulatory_score":0,"valuation_repricing_score":46,"execution_risk_score":62,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":70.0,"stage_label_after":"Stage4B-Watch","changed_components":["initial_margin_break_not_enough_for_hard4c"],"component_delta_explanation":"The 2024-11-07 trigger still had +19.15% MFE; first margin signal should be 4B watch.","MFE_90D_pct":19.15,"MAE_90D_pct":-36.04,"score_return_alignment_label":"initial_4b_watch_high_MFE_before_confirmed_break","current_profile_verdict":"current_profile_4C_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C14_shadow","case_id":"R3L68_C14_066970_20241220_REPEATED_MARGIN_HARD4C","trigger_id":"TR_C14_066970_20241220_HARD4C","symbol":"066970","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":66,"revision_score":64,"relative_strength_score":20,"customer_quality_score":30,"policy_or_regulatory_score":0,"valuation_repricing_score":54,"execution_risk_score":72,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":88.0,"stage_label_before":"Hard4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":68,"revision_score":66,"relative_strength_score":18,"customer_quality_score":30,"policy_or_regulatory_score":0,"valuation_repricing_score":56,"execution_risk_score":74,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":91.0,"stage_label_after":"Hard4C","changed_components":["repeated_margin_break_confirms_hard4c"],"component_delta_explanation":"Repeated margin/customer-demand break reduces false-positive risk; 180D MAE was -48.18%.","MFE_90D_pct":3.64,"MAE_90D_pct":-40.68,"score_return_alignment_label":"hard_4c_protection_success","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C14_shadow","case_id":"R3L68_C14_373220_20241115_CELL_DEMAND_HARD4C_COUNTEREXAMPLE","trigger_id":"TR_C14_373220_20241115_STAGE4B_COUNTER","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":44,"revision_score":50,"relative_strength_score":44,"customer_quality_score":56,"policy_or_regulatory_score":58,"valuation_repricing_score":48,"execution_risk_score":58,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":80.0,"stage_label_before":"Hard4C_or_Red","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":40,"revision_score":46,"relative_strength_score":44,"customer_quality_score":56,"policy_or_regulatory_score":60,"valuation_repricing_score":45,"execution_risk_score":56,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":69.0,"stage_label_after":"Stage4B-Watch","changed_components":["cell_maker_recovery_optionality_guard","generic_EV_slowdown_to_4b_watch"],"component_delta_explanation":"Cell makers retain policy/ESS/customer recovery optionality; hard 4C requires thesis break, not just weak demand.","MFE_90D_pct":14.56,"MAE_90D_pct":-11.46,"score_return_alignment_label":"cell_maker_4b_counterexample","current_profile_verdict":"current_profile_4B_too_early"}
{"row_type":"aggregate","round":"R3","loop":"68","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","representative_trigger_count":4,"avg_MFE_90D_pct":10.97,"avg_MAE_90D_pct":-27.56,"avg_MFE_180D_pct":10.97,"avg_MAE_180D_pct":-43.39,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":2,"dedupe_rule":"same_entry_group_id representative only"}
{"row_type":"residual_contribution","round":"R3","loop":"68","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_canonical_archetype_count":1,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":2,"tested_existing_calibrated_axes":["full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["guidance_only_hard4c_false_positive","cell_maker_recovery_optionality_counterexample","initial_margin_break_too_early_for_hard4c"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"C14_EV_DEMAND_SLOWDOWN_4B_4C","diversity_score_summary":"avg=34.0; new canonical C14; 4 symbols; 4 trigger families; no same symbol+trigger+entry duplicate"}
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
next_round = R3_loop_69_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
reason = C14 created a demand-slowdown 4B/4C split; next residual gap is customer contract/call-off risk versus generic EV-demand weakness.
```

## 28. Source Notes

Stock-web paths inspected in this loop or carried over from the same stock-web atlas session:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/006/006400.json
atlas/symbol_profiles/247/247540.json
atlas/symbol_profiles/066/066970.json
atlas/symbol_profiles/373/373220.json
atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv
atlas/ohlcv_tradable_by_symbol_year/006/006400/2025.csv
atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv
atlas/ohlcv_tradable_by_symbol_year/247/247540/2025.csv
atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv
atlas/ohlcv_tradable_by_symbol_year/066/066970/2025.csv
atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv
atlas/ohlcv_tradable_by_symbol_year/373/373220/2025.csv
```

External evidence in this MD is used as historical event-family labeling only. The quantitative calibration basis is the stock-web OHLC atlas.

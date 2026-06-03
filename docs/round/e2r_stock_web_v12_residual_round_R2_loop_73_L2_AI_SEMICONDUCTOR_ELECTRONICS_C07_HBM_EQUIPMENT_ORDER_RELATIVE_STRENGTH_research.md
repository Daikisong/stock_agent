# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R2
scheduled_loop = 73
completed_round = R2
completed_loop = 73
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id = HBM_TCBONDER_TEST_HANDLER_RELATIVE_STRENGTH_AND_THEME_GUARD
output_file = e2r_stock_web_v12_residual_round_R2_loop_73_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 4 new independent cases, 1 counterexamples, and 4 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH.

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

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R2
scheduled_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id = HBM_TCBONDER_TEST_HANDLER_RELATIVE_STRENGTH_AND_THEME_GUARD
loop_objective = sector_specific_rule_discovery | canonical_archetype_compression | residual_missed_structural_mining | residual_false_positive_mining | 4B_non_price_requirement_stress_test | counterexample_mining | coverage_gap_fill
```

R2 is constrained to `L2_AI_SEMICONDUCTOR_ELECTRONICS`; this MD does not jump to another sector even if other coverage gaps exist.

## 3. Previous Coverage / Duplicate Avoidance Check

- Schedule source: previous local R1 Loop 73 output had `next_round=R2`, `next_loop=73`.
- Allowed stock_agent registry access was used only as a duplicate/coverage sanity check; no `src/e2r` code was opened.
- Duplicate key checked: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- Selected rows use new C07 symbols/trigger families for this loop: 042700, 089030, 003160, 036540.
- `duplicate_key_conflict = 0`.
- `schema_rematerialization_only = false`.

## 4. Stock-Web OHLC Input / Price Source Validation

```json
{
  "row_type": "price_source_validation",
  "source": "Songdaiki/stock-web",
  "source_url": "https://github.com/Songdaiki/stock-web",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
  "manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "validation_status": "usable_for_historical_calibration"
}
```

Stock-Web is treated as the price atlas, not the stock_agent research repository. Price basis is raw/unadjusted `tradable_raw`; corporate-action windows are blocked by default.

## 5. Historical Eligibility Gate

| gate | status |
|---|---|
| trigger_date is historical | pass |
| entry_date exists in tradable shard | pass for all representative rows |
| at least 180 forward trading days available | pass |
| OHLCV positive and present | pass |
| 30D/90D/180D MFE/MAE computed | pass |
| corporate-action contamination in 180D window | clean for selected 2024 rows |
| live candidate scan | not performed |

## 6. Canonical Archetype Compression Map

`HBM_TCBONDER_TEST_HANDLER_RELATIVE_STRENGTH_AND_THEME_GUARD` is compressed into `C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH`. The compression rule is:

```text
HBM equipment order/customer route + relative strength => C07 promote-to-Yellow candidate
broad semiconductor/OSAT packaging beta without order bridge => C07 guard / Stage2-watch cap
post-rerating price/valuation peak without order slowdown => 4B overlay only, not full 4B
```

## 7. Case Selection Summary

|case_id|symbol|company_name|case_type|positive_or_counterexample|best_trigger|current_profile_verdict|is_new_independent_case|independent_evidence_weight|
|---|---|---|---|---|---|---|---|---|
|R2L73_C07_042700_HANMI_20240213_TCBONDER_ORDER_RS|042700|한미반도체|structural_success|positive|R2L73_T042700_20240213_STAGE2A|current_profile_missed_structural|True|1.0|
|R2L73_C07_089030_TECHWING_20240213_HBM_TEST_HANDLER_RS|089030|테크윙|structural_success|positive|R2L73_T089030_20240213_STAGE2A|current_profile_missed_structural|True|1.0|
|R2L73_C07_003160_DI_20240213_MEMORY_TESTER_RS_HIGH_MAE|003160|디아이|high_mae_success|positive|R2L73_T003160_20240213_STAGE2A|current_profile_4B_too_late|True|1.0|
|R2L73_C07_036540_SFASEMI_20240213_PACKAGING_THEME_COUNTEREXAMPLE|036540|SFA반도체|failed_rerating|counterexample|R2L73_T036540_20240213_STAGE2_THEME|current_profile_false_positive|True|1.0|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 1
calibration_usable_case_count = 4
minimum_positive_case_count = pass
minimum_counterexample_count = pass
minimum_calibration_usable_case_count = pass
```

The positive set separates HBM equipment/order routes from generic semiconductor beta. SFA반도체 is the counterexample: broad OSAT/packaging narrative existed, but no C07 order/customer-quality bridge was visible at the trigger.

## 9. Evidence Source Map

| symbol | evidence family | Stage2 evidence | Stage3 evidence | 4B/4C evidence |
|---|---|---|---|---|
| 042700 | HBM TC-bonder order/customer route | public event, customer/order quality, relative strength | multiple sources, visibility; no Green by outcome | valuation/positioning overlay after peak |
| 089030 | HBM test handler/prober route | public event, equipment route, relative strength | multiple sources; no confirmed revision at trigger | later positioning risk only |
| 003160 | memory/HBM tester route | public event, relative strength, early signal | weak-to-moderate; high-MAE success | 4B overlay needed after peak |
| 036540 | broad OSAT/packaging theme | theme headline, price movement | none | price-only local peak; not full 4B |

## 10. Price Data Source Map

| symbol | company_name | price_shard_path | profile_path | corporate_action_window_status |
|---|---|---|---|---|
| 042700 | 한미반도체 | atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv | atlas/symbol_profiles/042/042700.json | clean_180D_window |
| 089030 | 테크윙 | atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv | atlas/symbol_profiles/089/089030.json | clean_180D_window |
| 003160 | 디아이 | atlas/ohlcv_tradable_by_symbol_year/003/003160/2024.csv | atlas/symbol_profiles/003/003160.json | clean_180D_window |
| 036540 | SFA반도체 | atlas/ohlcv_tradable_by_symbol_year/036/036540/2024.csv | atlas/symbol_profiles/036/036540.json | clean_180D_window |

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|company_name|trigger_type|trigger_date|entry_date|entry_price|MFE_30D_pct|MFE_90D_pct|MFE_180D_pct|MAE_30D_pct|MAE_90D_pct|MAE_180D_pct|peak_date|peak_price|current_profile_verdict|trigger_outcome_label|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R2L73_T042700_20240213_STAGE2A|042700|한미반도체|Stage2-Actionable|2024-02-08|2024-02-13|81000|44.81|142.22|142.22|-12.72|-12.72|-12.72|2024-06-14|196200|current_profile_missed_structural|structural_success_high_MFE_order_RS|
|R2L73_T089030_20240213_STAGE2A|089030|테크윙|Stage2-Actionable|2024-02-08|2024-02-13|18690|78.71|196.42|278.81|-6.04|-6.04|-6.04|2024-07-11|70800|current_profile_missed_structural|structural_success_very_high_MFE_test_handler|
|R2L73_T003160_20240213_STAGE2A|003160|디아이|Stage2-Actionable|2024-02-13|2024-02-13|6160|103.73|400.0|400.0|-2.27|-2.27|-2.27|2024-06-27|30800|current_profile_4B_too_late|high_mae_success_memory_tester_RS|
|R2L73_T036540_20240213_STAGE2_THEME|036540|SFA반도체|Stage2-Theme|2024-02-13|2024-02-13|6650|2.86|2.86|2.86|-14.29|-19.55|-32.63|2024-02-15|6840|current_profile_false_positive|failed_rerating_theme_without_order_bridge|
|R2L73_T042700_20240614_4B_OVERLAY|042700|한미반도체|Stage4B-Overlay|2024-06-14|2024-06-14|179900|9.06|9.06|9.06|-7.56|-45.25|-50.19|2024-06-14|196200|current_profile_4B_too_late|4B_overlay_success_not_full_exit|

## 12. Trigger-Level OHLC Backtest Tables

|trigger_id|symbol|company_name|trigger_type|trigger_date|entry_date|entry_price|MFE_30D_pct|MFE_90D_pct|MFE_180D_pct|MAE_30D_pct|MAE_90D_pct|MAE_180D_pct|peak_date|peak_price|current_profile_verdict|trigger_outcome_label|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R2L73_T042700_20240213_STAGE2A|042700|한미반도체|Stage2-Actionable|2024-02-08|2024-02-13|81000|44.81|142.22|142.22|-12.72|-12.72|-12.72|2024-06-14|196200|current_profile_missed_structural|structural_success_high_MFE_order_RS|
|R2L73_T089030_20240213_STAGE2A|089030|테크윙|Stage2-Actionable|2024-02-08|2024-02-13|18690|78.71|196.42|278.81|-6.04|-6.04|-6.04|2024-07-11|70800|current_profile_missed_structural|structural_success_very_high_MFE_test_handler|
|R2L73_T003160_20240213_STAGE2A|003160|디아이|Stage2-Actionable|2024-02-13|2024-02-13|6160|103.73|400.0|400.0|-2.27|-2.27|-2.27|2024-06-27|30800|current_profile_4B_too_late|high_mae_success_memory_tester_RS|
|R2L73_T036540_20240213_STAGE2_THEME|036540|SFA반도체|Stage2-Theme|2024-02-13|2024-02-13|6650|2.86|2.86|2.86|-14.29|-19.55|-32.63|2024-02-15|6840|current_profile_false_positive|failed_rerating_theme_without_order_bridge|
|R2L73_T042700_20240614_4B_OVERLAY|042700|한미반도체|Stage4B-Overlay|2024-06-14|2024-06-14|179900|9.06|9.06|9.06|-7.56|-45.25|-50.19|2024-06-14|196200|current_profile_4B_too_late|4B_overlay_success_not_full_exit|

Representative rows are deduped by `same_entry_group_id`. The 042700 4B overlay row is excluded from aggregate entry metrics.

## 13. Current Calibrated Profile Stress Test

| case | current_profile_verdict | stress result |
|---|---|---|
| 042700 | current_profile_missed_structural | Stage2 bonus alone may be too weak for C07 order/customer route plus relative strength. Yellow is appropriate; Green still blocked. |
| 089030 | current_profile_missed_structural | Similar to 042700, but smaller initial score. C07 needs a specific bridge for HBM test-handler/prober evidence. |
| 003160 | current_profile_4B_too_late | Entry worked, but price/positioning overlay should appear earlier after high-MFE move. |
| 036540 | current_profile_false_positive | Generic semiconductor/OSAT beta should not inherit C07 equipment-order score. |

Existing axis status:

```text
stage2_actionable_evidence_bonus = existing_axis_tested
stage3_yellow_total_min = existing_axis_tested
stage3_green_total_min = existing_axis_kept
stage3_green_revision_min = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 14. Stage2 / Yellow / Green Comparison

- Stage2-Actionable is the useful early gate for C07 when order/customer route and relative strength appear together.
- Stage3-Yellow should be permitted for 042700/089030 style cases when the evidence is not just price but not yet confirmed revision.
- Stage3-Green remains too strict to assign at the early trigger date. That strictness is kept because SFA shows how a broad theme can fade without order/customer bridge.
- `green_lateness_ratio = not_applicable` because this loop focuses on early Stage2/Yellow compression rather than confirmed Green dates.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---|---:|---:|---|
| R2L73_T042700_20240614_4B_OVERLAY | 0.90 | 0.90 | good local overlay; not full 4B without non-price thesis cap |
| R2L73_T036540_20240213_STAGE2_THEME | 1.00 | 0.16 | price-only local 4B too early; cannot become full 4B or positive stage |

The rule candidate strengthens the existing split: C07 can have true structural entries and violent post-peak drawdowns. Price-only peak is a risk overlay, not a production downgrade unless order, margin, delay, dilution, or thesis evidence breaks.

## 16. 4C Protection Audit

No hard 4C row is proposed. The correct label is `thesis_break_watch_only` for equipment winners and `false_break` for the SFA theme counterexample. Hard 4C routing is kept.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule_name = L2_HBM_equipment_order_route_plus_relative_strength_bridge
```

Within L2, HBM equipment/order route plus relative strength should receive a limited bridge from Stage2-Actionable toward Yellow. The bridge is not global: it depends on the combination of customer/order quality, equipment category, and relative strength.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_rule_name = C07_HBM_equipment_order_RS_bridge_with_theme_guard
```

Candidate rule:

```text
if canonical_archetype_id == C07
and evidence has customer_or_order_quality or capacity_or_volume_route
and relative_strength confirms the trigger
then allow Stage2-Actionable -> Stage3-Yellow bridge
but keep Green blocked until confirmed revision / repeat order / durable customer confirmation.

if evidence is only broad semiconductor/OSAT/HBM theme
and no C07 equipment order/customer-quality bridge exists
then cap at Stage2-Watch or low Stage2-Actionable.
```

## 19. Before / After Backtest Comparison

|profile_id|profile_scope|eligible_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|missed_structural_count|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|current_proxy|4|185.38|-10.14|205.97|-13.42|0.25|2|mixed; under-promotes HBM equipment winners and may over-read generic packaging beta|
|P0b_e2r_2_0_baseline_reference|rollback_reference|4|185.38|-10.14|205.97|-13.42|0.5|3|worse; too blunt on early HBM evidence|
|P1_C07_HBM_equipment_order_RS_bridge|canonical_archetype_specific|4|185.38|-10.14|205.97|-13.42|0.0|0|best shadow profile for C07; captures Hanmi/Techwing and rejects SFA theme-only|
|P2_C07_counterexample_guard_profile|counterexample_guard|1|2.86|-19.55|2.86|-32.63|0.0|0|guard works; avoids false positive|
|P3_C07_4B_overlay_profile|4B_overlay_guard|1|9.06|-45.25|9.06|-50.19|0.0|0|good overlay; not a standalone Stage downgrade|

## 20. Score-Return Alignment Matrix

| case_id | before_score | before_stage | after_score | after_stage | alignment |
|---|---:|---|---:|---|---|
| R2L73_C07_042700_HANMI_20240213_TCBONDER_ORDER_RS | 77 | Stage3-Yellow | 84 | Stage3-Yellow | positive high-MFE path; current proxy can under-promote equipment order quality before confirmed revision appears |
| R2L73_C07_089030_TECHWING_20240213_HBM_TEST_HANDLER_RS | 72 | Stage2-Actionable | 79 | Stage3-Yellow | positive very-high MFE with clean 180D window; order route + equipment category mattered more than generic semiconductor beta |
| R2L73_C07_003160_DI_20240213_MEMORY_TESTER_RS_HIGH_MAE | 69 | Stage2-Actionable | 64 | Stage2-Actionable | large MFE but violent post-peak drawdown; the entry signal worked, while 4B overlay needed valuation/positioning separation |
| R2L73_C07_036540_SFASEMI_20240213_PACKAGING_THEME_COUNTEREXAMPLE | 48 | Stage2-Watch | 34 | Stage1/Watch | low MFE and negative MAE path despite broad HBM/packaging narrative; no C07 equipment order/customer-quality bridge |

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L2_AI_SEMICONDUCTOR_ELECTRONICS|C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|HBM_TCBONDER_TEST_HANDLER_RELATIVE_STRENGTH_AND_THEME_GUARD|3|1|1|0|4|0|5|4|4|True|True|C07 now has order-RS positives, high-MAE success, and one theme-only counterexample; still needs additional non-price 4C and more OSAT holdouts|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: current_profile_missed_structural, current_profile_false_positive, current_profile_4B_too_late
new_axis_proposed: hbm_equipment_order_rs_bridge_bonus, generic_packaging_theme_stage_cap
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min, stage3_green_revision_min, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Historical C07 R2 cases only.
- Stock-Web tradable_raw OHLC only.
- 30D/90D/180D MFE/MAE, drawdown, and 4B overlay stress.
- Shadow-only scoring proxy.

Non-validation scope:

- No live candidate discovery.
- No current recommendation.
- No stock_agent source-code inspection.
- No production scoring change.
- No broker/API/autotrading use.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
"shadow_weight","hbm_equipment_order_rs_bridge_bonus","canonical_archetype_specific","L2_AI_SEMICONDUCTOR_ELECTRONICS","C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","0","1","+1","order/customer-quality route plus relative strength separated Hanmi/Techwing from broad semiconductor beta","higher MFE and lower false-positive rate after requiring order-route evidence","R2L73_T042700_20240213_STAGE2A|R2L73_T089030_20240213_STAGE2A|R2L73_T003160_20240213_STAGE2A","4","4","1","medium","canonical_archetype_shadow_only","not production; post-calibrated residual"
"shadow_weight","generic_packaging_theme_stage_cap","canonical_archetype_specific_guard","L2_AI_SEMICONDUCTOR_ELECTRONICS","C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","0","1","+1","SFA-style packaging beta did not behave like C07 equipment order winners","blocks false positive Stage2/Yellow promotion when only broad theme evidence exists","R2L73_T036540_20240213_STAGE2_THEME","1","1","1","low_to_medium","guard_shadow_only","not production; needs more holdout rows"
"shadow_weight","4b_overlay_not_full_4b_without_non_price_slowdown","canonical_archetype_specific","L2_AI_SEMICONDUCTOR_ELECTRONICS","C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","full_4b_requires_non_price_evidence=true","strengthened_for_C07","0","C07 winners can have violent valuation peaks before thesis break; price-only local peak should not erase structural thesis","preserves structural winners while flagging risk overlay","R2L73_T042700_20240614_4B_OVERLAY","1","0","0","medium","existing_axis_strengthened","not production; overlay only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"case_id": "R2L73_C07_042700_HANMI_20240213_TCBONDER_ORDER_RS", "symbol": "042700", "company_name": "한미반도체", "sector": "HBM equipment", "primary_archetype": "HBM TC-bonder order/customer relative-strength bridge", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R2L73_T042700_20240213_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "current_profile_verdict": "current_profile_missed_structural", "score_price_alignment": "positive high-MFE path; current proxy can under-promote equipment order quality before confirmed revision appears", "notes": "New R2/C07 symbol in this loop. The signal is not price-only: it combines HBM equipment/customer-route news with rapid relative-strength confirmation. Green remains blocked until durable revision/order conversion.", "row_type": "case", "round": "R2", "loop": "73", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TCBONDER_TEST_HANDLER_RELATIVE_STRENGTH_AND_THEME_GUARD", "price_source": "Songdaiki/stock-web"}
{"case_id": "R2L73_C07_089030_TECHWING_20240213_HBM_TEST_HANDLER_RS", "symbol": "089030", "company_name": "테크윙", "sector": "HBM test equipment", "primary_archetype": "HBM test handler/prober relative-strength bridge", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R2L73_T089030_20240213_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "current_profile_verdict": "current_profile_missed_structural", "score_price_alignment": "positive very-high MFE with clean 180D window; order route + equipment category mattered more than generic semiconductor beta", "notes": "New R2/C07 symbol. HBM test-handler/prober exposure with strong price confirmation produced a large MFE, but later drawdown argues for overlay-only 4B treatment when evidence is only valuation/positioning.", "row_type": "case", "round": "R2", "loop": "73", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TCBONDER_TEST_HANDLER_RELATIVE_STRENGTH_AND_THEME_GUARD", "price_source": "Songdaiki/stock-web"}
{"case_id": "R2L73_C07_003160_DI_20240213_MEMORY_TESTER_RS_HIGH_MAE", "symbol": "003160", "company_name": "디아이", "sector": "memory test equipment", "primary_archetype": "memory tester/HBM test equipment relative-strength bridge", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "R2L73_T003160_20240213_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "current_profile_verdict": "current_profile_4B_too_late", "score_price_alignment": "large MFE but violent post-peak drawdown; the entry signal worked, while 4B overlay needed valuation/positioning separation", "notes": "New R2/C07 symbol. Included as a positive high-MAE success rather than a clean structural success. It stresses that C07 should not turn every fast equipment move into Green.", "row_type": "case", "round": "R2", "loop": "73", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TCBONDER_TEST_HANDLER_RELATIVE_STRENGTH_AND_THEME_GUARD", "price_source": "Songdaiki/stock-web"}
{"case_id": "R2L73_C07_036540_SFASEMI_20240213_PACKAGING_THEME_COUNTEREXAMPLE", "symbol": "036540", "company_name": "SFA반도체", "sector": "semiconductor packaging / OSAT theme", "primary_archetype": "packaging theme without HBM equipment order confirmation", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R2L73_T036540_20240213_STAGE2_THEME", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "current_profile_verdict": "current_profile_false_positive", "score_price_alignment": "low MFE and negative MAE path despite broad HBM/packaging narrative; no C07 equipment order/customer-quality bridge", "notes": "New counterexample. The signal intentionally looks like a broad semiconductor/HBM beta trade, but lacks the order-relative-strength bridge required for C07 promotion.", "row_type": "case", "round": "R2", "loop": "73", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TCBONDER_TEST_HANDLER_RELATIVE_STRENGTH_AND_THEME_GUARD", "price_source": "Songdaiki/stock-web"}
{"trigger_id": "R2L73_T042700_20240213_STAGE2A", "case_id": "R2L73_C07_042700_HANMI_20240213_TCBONDER_ORDER_RS", "symbol": "042700", "company_name": "한미반도체", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-08", "entry_date": "2024-02-13", "entry_price": 81000, "evidence_available_at_that_date": "HBM TC-bonder/customer-route news had become visible; the first post-holiday tradable close after the 2024-02-08 price/volume break is used to avoid same-day gap lookahead.", "evidence_source": "public HBM TC-bonder/customer-route news and stock-web 042700 2024 tradable shard", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv", "profile_path": "atlas/symbol_profiles/042/042700.json", "MFE_30D_pct": 44.81, "MFE_90D_pct": 142.22, "MFE_180D_pct": 142.22, "MFE_1Y_pct": 142.22, "MFE_2Y_pct": null, "MAE_30D_pct": -12.72, "MAE_90D_pct": -12.72, "MAE_180D_pct": -12.72, "MAE_1Y_pct": -12.72, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-14", "peak_price": 196200, "drawdown_after_peak_pct": -54.33, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_stage2", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success_high_MFE_order_RS", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R2L73_G042700_20240213_81000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "row_type": "trigger", "round": "R2", "loop": "73", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TCBONDER_TEST_HANDLER_RELATIVE_STRENGTH_AND_THEME_GUARD", "sector": "semiconductor_hbm_equipment", "primary_archetype": "HBM equipment order + relative strength", "loop_objective": "sector_specific_rule_discovery | canonical_archetype_compression | residual_missed_structural_mining | residual_false_positive_mining | 4B_non_price_requirement_stress_test | counterexample_mining | coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"trigger_id": "R2L73_T089030_20240213_STAGE2A", "case_id": "R2L73_C07_089030_TECHWING_20240213_HBM_TEST_HANDLER_RS", "symbol": "089030", "company_name": "테크윙", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-08", "entry_date": "2024-02-13", "entry_price": 18690, "evidence_available_at_that_date": "HBM test-handler/prober route and strong relative strength were visible by the post-holiday close; no confirmed full-year revision was assumed at trigger date.", "evidence_source": "public HBM test equipment coverage and stock-web 089030 2024 tradable shard", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv", "profile_path": "atlas/symbol_profiles/089/089030.json", "MFE_30D_pct": 78.71, "MFE_90D_pct": 196.42, "MFE_180D_pct": 278.81, "MFE_1Y_pct": 278.81, "MFE_2Y_pct": null, "MAE_30D_pct": -6.04, "MAE_90D_pct": -6.04, "MAE_180D_pct": -6.04, "MAE_1Y_pct": -6.04, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 70800, "drawdown_after_peak_pct": -56.92, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_stage2", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success_very_high_MFE_test_handler", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R2L73_G089030_20240213_18690", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "row_type": "trigger", "round": "R2", "loop": "73", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TCBONDER_TEST_HANDLER_RELATIVE_STRENGTH_AND_THEME_GUARD", "sector": "semiconductor_hbm_equipment", "primary_archetype": "HBM equipment order + relative strength", "loop_objective": "sector_specific_rule_discovery | canonical_archetype_compression | residual_missed_structural_mining | residual_false_positive_mining | 4B_non_price_requirement_stress_test | counterexample_mining | coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"trigger_id": "R2L73_T003160_20240213_STAGE2A", "case_id": "R2L73_C07_003160_DI_20240213_MEMORY_TESTER_RS_HIGH_MAE", "symbol": "003160", "company_name": "디아이", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "entry_date": "2024-02-13", "entry_price": 6160, "evidence_available_at_that_date": "Memory/HBM tester route was known and early relative-strength pickup started before formal broad revision confirmation; treated as C07 high-MAE success.", "evidence_source": "public memory test-equipment coverage and stock-web 003160 2024 tradable shard", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003160/2024.csv", "profile_path": "atlas/symbol_profiles/003/003160.json", "MFE_30D_pct": 103.73, "MFE_90D_pct": 400.0, "MFE_180D_pct": 400.0, "MFE_1Y_pct": 400.0, "MFE_2Y_pct": null, "MAE_30D_pct": -2.27, "MAE_90D_pct": -2.27, "MAE_180D_pct": -2.27, "MAE_1Y_pct": -2.27, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2024-06-27", "peak_price": 30800, "drawdown_after_peak_pct": -42.86, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_stage2", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "high_mae_success_memory_tester_RS", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R2L73_G003160_20240213_6160", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "row_type": "trigger", "round": "R2", "loop": "73", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TCBONDER_TEST_HANDLER_RELATIVE_STRENGTH_AND_THEME_GUARD", "sector": "semiconductor_hbm_equipment", "primary_archetype": "HBM equipment order + relative strength", "loop_objective": "sector_specific_rule_discovery | canonical_archetype_compression | residual_missed_structural_mining | residual_false_positive_mining | 4B_non_price_requirement_stress_test | counterexample_mining | coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"trigger_id": "R2L73_T036540_20240213_STAGE2_THEME", "case_id": "R2L73_C07_036540_SFASEMI_20240213_PACKAGING_THEME_COUNTEREXAMPLE", "symbol": "036540", "company_name": "SFA반도체", "trigger_type": "Stage2-Theme", "trigger_date": "2024-02-13", "entry_date": "2024-02-13", "entry_price": 6650, "evidence_available_at_that_date": "Broad semiconductor/HBM packaging beta without confirmed C07 equipment-order or customer-quality bridge.", "evidence_source": "broad OSAT/packaging theme coverage and stock-web 036540 2024 tradable shard", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036540/2024.csv", "profile_path": "atlas/symbol_profiles/036/036540.json", "MFE_30D_pct": 2.86, "MFE_90D_pct": 2.86, "MFE_180D_pct": 2.86, "MFE_1Y_pct": 9.92, "MFE_2Y_pct": null, "MAE_30D_pct": -14.29, "MAE_90D_pct": -19.55, "MAE_180D_pct": -32.63, "MAE_1Y_pct": -32.63, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-15", "peak_price": 6840, "drawdown_after_peak_pct": -34.94, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 0.16, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "false_break", "trigger_outcome_label": "failed_rerating_theme_without_order_bridge", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R2L73_G036540_20240213_6650", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "row_type": "trigger", "round": "R2", "loop": "73", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TCBONDER_TEST_HANDLER_RELATIVE_STRENGTH_AND_THEME_GUARD", "sector": "semiconductor_hbm_equipment", "primary_archetype": "HBM equipment order + relative strength", "loop_objective": "sector_specific_rule_discovery | canonical_archetype_compression | residual_missed_structural_mining | residual_false_positive_mining | 4B_non_price_requirement_stress_test | counterexample_mining | coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"trigger_id": "R2L73_T042700_20240614_4B_OVERLAY", "case_id": "R2L73_C07_042700_HANMI_20240213_TCBONDER_ORDER_RS", "symbol": "042700", "company_name": "한미반도체", "trigger_type": "Stage4B-Overlay", "trigger_date": "2024-06-14", "entry_date": "2024-06-14", "entry_price": 179900, "evidence_available_at_that_date": "Local price/valuation/positioning overheat after a multi-month equipment re-rating. No thesis-break evidence; not a full 4B exit signal.", "evidence_source": "stock-web 042700 2024 tradable shard; price/valuation overlay only", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv", "profile_path": "atlas/symbol_profiles/042/042700.json", "MFE_30D_pct": 9.06, "MFE_90D_pct": 9.06, "MFE_180D_pct": 9.06, "MFE_1Y_pct": 11.45, "MFE_2Y_pct": null, "MAE_30D_pct": -7.56, "MAE_90D_pct": -45.25, "MAE_180D_pct": -50.19, "MAE_1Y_pct": -50.19, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-14", "peak_price": 196200, "drawdown_after_peak_pct": -54.33, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.9, "four_b_full_window_peak_proximity": 0.9, "four_b_timing_verdict": "good_local_4B_overlay_but_not_full_4B_without_non_price_thesis_cap", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success_not_full_exit", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R2L73_G042700_20240614_179900", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "row_type": "trigger", "round": "R2", "loop": "73", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TCBONDER_TEST_HANDLER_RELATIVE_STRENGTH_AND_THEME_GUARD", "sector": "semiconductor_hbm_equipment", "primary_archetype": "HBM equipment order + relative strength", "loop_objective": "sector_specific_rule_discovery | canonical_archetype_compression | residual_missed_structural_mining | residual_false_positive_mining | 4B_non_price_requirement_stress_test | counterexample_mining | coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L73_C07_042700_HANMI_20240213_TCBONDER_ORDER_RS", "trigger_id": "R2L73_T042700_20240213_STAGE2A", "symbol": "042700", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"contract_score": 14, "backlog_visibility_score": 12, "margin_bridge_score": 6, "revision_score": 10, "relative_strength_score": 22, "customer_quality_score": 18, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 77, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 17, "backlog_visibility_score": 14, "margin_bridge_score": 7, "revision_score": 13, "relative_strength_score": 22, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow", "changed_components": ["customer_quality_score", "backlog_visibility_score", "relative_strength_score", "theme_only_stage_cap", "positioning_overheat_overlay"], "component_delta_explanation": "Shadow-only C07 adjustment: reward HBM equipment route when order/customer quality and relative strength coincide; cap generic OSAT/packaging beta without equipment-order bridge; treat valuation/positioning as 4B overlay only.", "MFE_90D_pct": 142.22, "MAE_90D_pct": -12.72, "score_return_alignment_label": "positive high-MFE path; current proxy can under-promote equipment order quality before confirmed revision appears", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L73_C07_089030_TECHWING_20240213_HBM_TEST_HANDLER_RS", "trigger_id": "R2L73_T089030_20240213_STAGE2A", "symbol": "089030", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 4, "revision_score": 8, "relative_strength_score": 22, "customer_quality_score": 15, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 11, "backlog_visibility_score": 12, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 22, "customer_quality_score": 18, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 79, "stage_label_after": "Stage3-Yellow", "changed_components": ["customer_quality_score", "backlog_visibility_score", "relative_strength_score", "theme_only_stage_cap", "positioning_overheat_overlay"], "component_delta_explanation": "Shadow-only C07 adjustment: reward HBM equipment route when order/customer quality and relative strength coincide; cap generic OSAT/packaging beta without equipment-order bridge; treat valuation/positioning as 4B overlay only.", "MFE_90D_pct": 196.42, "MAE_90D_pct": -6.04, "score_return_alignment_label": "positive very-high MFE with clean 180D window; order route + equipment category mattered more than generic semiconductor beta", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L73_C07_003160_DI_20240213_MEMORY_TESTER_RS_HIGH_MAE", "trigger_id": "R2L73_T003160_20240213_STAGE2A", "symbol": "003160", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 6, "margin_bridge_score": 3, "revision_score": 6, "relative_strength_score": 24, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 69, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 6, "backlog_visibility_score": 7, "margin_bridge_score": 3, "revision_score": 7, "relative_strength_score": 22, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 16, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 64, "stage_label_after": "Stage2-Actionable", "changed_components": ["customer_quality_score", "backlog_visibility_score", "relative_strength_score", "theme_only_stage_cap", "positioning_overheat_overlay"], "component_delta_explanation": "Shadow-only C07 adjustment: reward HBM equipment route when order/customer quality and relative strength coincide; cap generic OSAT/packaging beta without equipment-order bridge; treat valuation/positioning as 4B overlay only.", "MFE_90D_pct": 400.0, "MAE_90D_pct": -2.27, "score_return_alignment_label": "large MFE but violent post-peak drawdown; the entry signal worked, while 4B overlay needed valuation/positioning separation", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L73_C07_036540_SFASEMI_20240213_PACKAGING_THEME_COUNTEREXAMPLE", "trigger_id": "R2L73_T036540_20240213_STAGE2_THEME", "symbol": "036540", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 2, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 14, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 48, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 8, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 16, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 34, "stage_label_after": "Stage1/Watch", "changed_components": ["customer_quality_score", "backlog_visibility_score", "relative_strength_score", "theme_only_stage_cap", "positioning_overheat_overlay"], "component_delta_explanation": "Shadow-only C07 adjustment: reward HBM equipment route when order/customer quality and relative strength coincide; cap generic OSAT/packaging beta without equipment-order bridge; treat valuation/positioning as 4B overlay only.", "MFE_90D_pct": 2.86, "MAE_90D_pct": -19.55, "score_return_alignment_label": "low MFE and negative MAE path despite broad HBM/packaging narrative; no C07 equipment order/customer-quality bridge", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R2", "loop": "73", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "scheduled_round": "R2", "scheduled_loop": "73", "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 3, "counterexample_count": 1, "current_profile_error_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["current_profile_missed_structural", "current_profile_false_positive", "current_profile_4B_too_late"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "diversity_score_summary": "new_symbols=4; same_archetype_new_symbol=4; new_trigger_family=4; counterexamples=1; wrong_round_penalty=0; duplicate_key_conflict=0"}
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
completed_round = R2
completed_loop = 73
next_round = R3
next_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest confirmed `max_date=2026-02-20`, `tradable_row_count=14354401`, `symbol_count=5414`, `price_adjustment_status=raw_unadjusted_marcap`.
- Stock-Web schema confirms tradable shard columns `d,o,h,l,c,v,a,mc,s,m`, raw shard `rs`, and MFE/MAE definitions.
- 042700 profile: latest name 한미반도체; 2024 tradable shard rows include entry 2024-02-13 close 81,000 and 2024-06-14 high 196,200.
- 089030 profile: latest name 테크윙; 2024 tradable shard rows include entry 2024-02-13 close 18,690 and 2024-07-11 high 70,800.
- 003160 profile: latest name 디아이; 2024 tradable shard rows include entry 2024-02-13 close 6,160 and 2024-06-27 high 30,800.
- 036540 profile: latest name SFA반도체; 2024 tradable shard rows include entry 2024-02-13 close 6,650 and weak follow-through vs large negative MAE.
- Evidence labels are historical research proxies. They are not live candidate discovery, not trading advice, and not production scoring.


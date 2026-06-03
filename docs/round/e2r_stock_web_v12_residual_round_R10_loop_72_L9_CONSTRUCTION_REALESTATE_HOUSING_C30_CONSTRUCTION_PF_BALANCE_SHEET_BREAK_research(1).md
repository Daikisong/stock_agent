# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R10
scheduled_loop = 72
completed_round = R10
completed_loop = 72
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = PF_BALANCE_SHEET_TRUST_BREAK_VS_RECOVERY_GUARD
output_file = e2r_stock_web_v12_residual_round_R10_loop_72_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 4 new independent cases, 3 counterexamples, and 3 residual errors for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.

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

The residual question here is narrower than the global profile: in construction, a contract/backlog headline is often not the same thing as a clean balance-sheet rerating. The sector behaves like a bridge whose load-bearing pillar is trust. If execution trust or PF funding trust cracks, headline order value alone does not hold the structure.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round_scheduler_priority = sequential_round_cycle_first
previous_completed_round = R9
previous_completed_loop = 72
scheduled_round = R10
scheduled_loop = 72
round_sector_consistency = pass
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

R10 maps to L9 construction/real-estate/housing. The selected canonical archetype is C30 because the observed residual error is not just project backlog. It is balance-sheet and trust translation: PF exposure, execution credibility, accounting hit, and the possibility of post-4C recovery after evidence improves.

## 3. Previous Coverage / Duplicate Avoidance Check

Prior state was taken from the immediately preceding generated MD handoff: completed R9 / loop 72, next R10 / loop 72. No stock_agent source code was opened. This run avoids repeating R9 mobility/tire evidence and stays inside scheduled R10.

Novelty basis:

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = avoided
new_symbol_count = 3
new_trigger_family_count = 4
new_independent_case_ratio = 1.00
reused_case_count = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest was checked before case selection.

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Relevant profile checks:

|symbol|company|profile_path|profile last_date|corporate_action_candidate_dates used for gate|180D status|
|---|---|---|---|---|---|
|294870|HDC현대산업개발|atlas/symbol_profiles/294/294870.json|2026-02-20|2020-03-26 only|clean for 2022/2023 trigger windows|
|006360|GS건설|atlas/symbol_profiles/006/006360.json|2026-02-20|1999-05-07|1999-12-01|2014-06-25|clean for 2023 trigger window|
|000720|현대건설|atlas/symbol_profiles/000/000720.json|2026-02-20|pre-2005 candidates only|clean for 2023 trigger window|
|009410|태영건설|atlas/symbol_profiles/009/009410.json|2026-02-20|2024-10-31 overlaps forward observation|blocked/narrative-only|

## 5. Historical Eligibility Gate

Representative trigger inclusion requires: historical trigger, stock-web tradable entry row, clean 180 trading-day forward window, OHLCV fields present, and no corporate-action contamination over the 180D window.

|case_id|symbol|entry_date|forward_180D_available|corporate_action_window_status|calibration_usable|reason|
|---|---|---|---|---|---|---|
|R10L72_C30_HDC_20220112_4C|294870|2022-01-12|true|clean_180D_window|true|tradable row and 180D row path usable|
|R10L72_C30_GS_20230705_4C|006360|2023-07-05|true|clean_180D_window|true|tradable row and 180D row path usable|
|R10L72_C30_HDC_20231027_RECOVERY|294870|2023-10-27|true|clean_180D_window|true|tradable row and 180D row path usable|
|R10L72_C30_HDEC_20230626_CONTRACT_COUNTER|000720|2023-06-26|true|clean_180D_window|true|tradable row and 180D row path usable|
|R10L72_C30_TY_20231228_WORKOUT_NARRATIVE|009410|2023-12-28|blocked by suspension/corp action|contaminated_or_unavailable|false|narrative_only|

## 6. Canonical Archetype Compression Map

```text
fine_archetype_id = PF_BALANCE_SHEET_TRUST_BREAK_VS_RECOVERY_GUARD
maps_to = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

Compression rule: construction cases should not be split endlessly into accident, PF, contract, and recovery micro-labels. They compress into one C30 mechanism: when trust breaks, liquidity and valuation contract together; when trust repairs with visible cash/margins, the same sector can re-rate even before a perfect Green confirmation.

## 7. Case Selection Summary

|case_id|symbol|company|case_role|positive/counter|entry_date|entry_price|MFE90|MAE90|MFE180|MAE180|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|
|R10L72_C30_HDC_20220112_4C|294870|HDC현대산업개발|4C_success|counterexample|2022-01-12|20850|8.87|-36.93|8.87|-50.84|current_profile_correct|
|R10L72_C30_GS_20230705_4C|006360|GS건설|4C_late|counterexample|2023-07-05|18030|5.1|-29.73|5.1|-29.73|current_profile_4C_too_late|
|R10L72_C30_HDC_20231027_RECOVERY|294870|HDC현대산업개발|structural_success|positive|2023-10-27|11700|77.35|-6.15|87.61|-6.15|current_profile_missed_structural|
|R10L72_C30_HDEC_20230626_CONTRACT_COUNTER|000720|현대건설|failed_rerating|counterexample|2023-06-26|40800|8.82|-17.89|8.82|-18.5|current_profile_false_positive|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 3
4B_case_count = 2
4C_case_count = 3 including narrative-only Taeyoung
calibration_usable_case_count = 4
```

The sample is intentionally counterexample-heavy because the scheduled C30 gap is a guardrail gap. HDC 2023 is the recovery positive: it shows that C30 cannot be a permanent exclusion label. GS 2023 and HDC 2022 show trust-break drawdowns. Hyundai E&C 2023 shows that a mega-contract headline can be a false positive if the margin/PF bridge remains weak.

## 9. Evidence Source Map

|case_id|trigger_date|evidence available at that date|stage path|
|---|---|---|---|
|R10L72_C30_HDC_20220112_4C|2022-01-11|Gwangju Hwajeong I-Park collapse occurred after market close; next-trading-day entry used|4C trust break|
|R10L72_C30_GS_20230705_4C|2023-07-05|Geomdan apartment reconstruction/cost event and execution trust break|4C / 4B-to-4C|
|R10L72_C30_HDC_20231027_RECOVERY|2023-10-27|Post-accident normalization and price/earnings recovery evidence, used as Stage2-Actionable recovery trigger|Stage2-Actionable to Green|
|R10L72_C30_HDEC_20230626_CONTRACT_COUNTER|2023-06-26|Saudi Amiral mega-contract headline, but margin/PF conversion not confirmed|Stage2 headline false-positive stress|
|R10L72_C30_TY_20231228_WORKOUT_NARRATIVE|2023-12-28|Workout application/liquidity break; blocked from weight calibration due stock-web contamination|narrative-only 4C|

## 10. Price Data Source Map

|symbol|entry shard|profile path|price basis|adjustment status|
|---|---|---|---|---|
|294870|atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv | 2023.csv | 2024.csv|atlas/symbol_profiles/294/294870.json|tradable_raw|raw_unadjusted_marcap|
|006360|atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv | 2024.csv|atlas/symbol_profiles/006/006360.json|tradable_raw|raw_unadjusted_marcap|
|000720|atlas/ohlcv_tradable_by_symbol_year/000/000720/2023.csv|atlas/symbol_profiles/000/000720.json|tradable_raw|raw_unadjusted_marcap|
|009410|atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv | 2024.csv|atlas/symbol_profiles/009/009410.json|tradable_raw|raw_unadjusted_marcap|

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|trigger_type|trigger_date|entry_date|entry_price|MFE30|MAE30|MFE90|MAE90|MFE180|MAE180|aggregate_role|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|T_HDC_20220112_4C|294870|Stage4C|2022-01-11|2022-01-12|20850|8.87|-35.25|8.87|-36.93|8.87|-50.84|representative|current_profile_correct|
|T_GS_20230705_4C|006360|Stage4C|2023-07-05|2023-07-05|18030|5.1|-25.85|5.1|-29.73|5.1|-29.73|representative|current_profile_4C_too_late|
|T_HDC_20231027_RECOVERY|294870|Stage2-Actionable|2023-10-27|2023-10-27|11700|37.86|-6.15|77.35|-6.15|87.61|-6.15|representative|current_profile_missed_structural|
|T_HDEC_20230626_CONTRACT_COUNTER|000720|Stage2-Actionable|2023-06-26|2023-06-26|40800|8.82|-15.32|8.82|-17.89|8.82|-18.5|representative|current_profile_false_positive|
|T_HDC_20240228_STAGE3_GREEN_LABEL|294870|Stage3-Green|2024-02-28|2024-02-28|20400|1.72|-21.23|7.6|-21.23|38.24|-21.23|label_comparison_only|current_profile_too_late|

## 12. Trigger-Level OHLC Backtest Tables

Representative entries are deduped by same_entry_group_id. HDC recovery has a separate Stage3-Green label-comparison row; it is not aggregate counted.

|representative case|entry close|best high used|worst low used|peak date|drawdown after peak|interpretation|
|---|---|---|---|---|---|---|
|HDC 2022 4C|20,850|22,700|10,250 within 180D|2022-01-12|-56.87%|trust-break avoided only if hard 4C was immediate|
|GS 2023 4C|18,030|18,950|12,670 within 90/180D|2023-07-05|-33.14%|hard trust/event loss outweighed backlog|
|HDC 2023 recovery|11,700|21,950 within 180D|10,980|2024-07-17|-12.98%|clean recovery can re-enter after prior 4C|
|Hyundai E&C 2023 contract|40,800|44,400|33,250|2023-06-26|-25.11%|contract-only headline failed to sustain rerating|

## 13. Current Calibrated Profile Stress Test

|case|current profile likely label|actual alignment|residual verdict|
|---|---|---|---|
|HDC 2022 collapse|hard 4C if evidence captured|aligned: MAE180 about -50.8%|current_profile_correct|
|GS 2023 Geomdan|4B/4C may be late if waiting for accounting quantification|drawdown arrived immediately|current_profile_4C_too_late|
|HDC 2023 recovery|prior trust break may keep score too suppressed|MFE90 +77.35% with shallow early MAE|current_profile_missed_structural|
|Hyundai E&C 2023 Amiral|contract/backlog score can promote too early|MFE capped while MAE widened|current_profile_false_positive|

Existing axis status:

```text
stage2_actionable_evidence_bonus = existing_axis_tested
stage3_yellow_total_min = existing_axis_tested
stage3_green_total_min = existing_axis_tested
price_only_blowoff_blocks_positive_stage = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_strengthened
```

## 14. Stage2 / Yellow / Green Comparison

HDC recovery is the useful late-Green example. The Stage2-Actionable entry on 2023-10-27 had an entry close of 11,700 and an observed 180D peak of 21,950. A later Stage3-Green label on 2024-02-28 entered at 20,400. The Green lateness ratio is therefore about:

```text
green_lateness_ratio = (20400 - 11700) / (21950 - 11700) = 0.85
```

This is late, but not a reason to weaken the global Green strictness. It is a reason to create a C30 re-entry rule: after a hard trust break, early recovery must require low-MAE normalization and financial visibility before it can move from watch to actionable.

## 15. 4B Local vs Full-window Timing Audit

For HDC 2022 and GS 2023, the correct overlay is not price-only 4B. The trigger is non-price: construction safety/trust break, explicit cost/reconstruction risk, and credibility loss. Therefore `full_4b_requires_non_price_evidence` is strengthened.

|case|four_b_local_peak_proximity|four_b_full_window_peak_proximity|four_b_evidence_type|verdict|
|---|---|---|---|---|
|HDC 2022|n/a|n/a|legal_or_regulatory_block|accounting_or_trust_break|full 4C rather than local 4B|
|GS 2023|n/a|n/a|explicit_event_cap|legal_or_regulatory_block|4C should not wait for price confirmation|
|Hyundai E&C 2023|low|low|margin_or_backlog_slowdown|contract headline should stay Stage2-watch|
|HDC 2023 recovery|n/a|n/a|recovery, not 4B|no 4B|

## 16. 4C Protection Audit

HDC 2022 and GS 2023 support hard 4C routing when the non-price thesis is broken. Taeyoung 2023 is narrative-only but directionally consistent: once liquidity/workout evidence appears, trading suspension/corporate-action contamination makes it unusable for weight calibration, not irrelevant for guardrail narrative.

```text
HDC 2022 four_c_protection_label = hard_4c_success
GS 2023 four_c_protection_label = hard_4c_success_but_current_profile_may_be_late
Taeyoung 2023 four_c_protection_label = narrative_only_hard_4c
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_candidate = L9_C30_construction_trust_break_and_reentry_guard
```

Proposed sector shadow rule:

1. If construction trust/accounting/legal evidence breaks, route to 4C even when backlog or contract headline remains high.
2. For clean recovery after 4C, require at least two of: low-MAE price normalization, confirmed margin/cash recovery, reduced legal/execution red-team risk, and non-housing or low-PF visibility.
3. Mega-contract headlines should not promote to Stage3-Yellow unless there is a margin bridge or balance-sheet bridge. In construction, a contract can be a tall crane; without foundation, it does not carry the building.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
candidate_axes:
- C30_trust_break_hard_4c_guard
- C30_clean_recovery_after_4c_reentry_bonus
- C30_headline_contract_without_margin_bridge_penalty
```

The canonical rule is preferred over a global rule. The sample is C30-specific and should not be generalized into semiconductors, consumer exports, or financial capital return.

## 19. Before / After Backtest Comparison

|profile_id|scope|hypothesis|changed_axes|eligible_trigger_count|avg_MFE90|avg_MAE90|avg_MFE180|avg_MAE180|false_positive_rate|missed_structural|late_green|avg_green_lateness|avg_4B_local|avg_4B_full|alignment|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|P0 e2r_2_1_stock_web_calibrated_proxy|global current|keeps global Stage2/Green/4C axes; C30 specifics absent|none|4 reps|25.0|-22.7|25.0|-25.1|0.50|1|1|0.85|n/a|n/a|mixed: contract headlines still over-score|
|P0b e2r_2_0_baseline_reference|rollback reference|looser Stage2 and Green path|rollback|4 reps|25.0|-22.7|25.0|-25.1|0.75|1|2|0.91|n/a|n/a|worse false positives|
|P1 sector_specific_candidate_profile|L9 sector|add construction trust/PF guard and re-entry condition|C30 trust guard + clean recovery re-entry|4 reps|33.2|-14.9|33.2|-16.7|0.25|0|1|0.72|n/a|n/a|improves score-return alignment|
|P2 canonical_archetype_candidate_profile|C30 canonical|separate hard trust break, clean recovery, and headline-contract-only cases|three C30 axes|4 reps|33.2|-14.9|33.2|-16.7|0.25|0|1|0.72|n/a|n/a|best candidate, shadow-only|
|P3 counterexample_guard_profile|C30 guard|aggressive contract headline penalty without clean margin bridge|stricter contract/margin thresholds|4 reps|20.9|-13.0|20.9|-15.4|0.00|1|1|0.65|n/a|n/a|too conservative; may miss HDC-style recovery|

## 20. Score-Return Alignment Matrix

|case|P0 alignment|P2 C30 shadow alignment|explanation|
|---|---|---|---|
|HDC 2022 4C|correct if hard 4C captured|correct|trust break dominates all positives|
|GS 2023 4C|too late if waiting for quantified charge|better|event-level reconstruction/trust break is enough for 4C watch|
|HDC 2023 recovery|missed structural|better|recovery evidence plus low MAE permits re-entry|
|Hyundai E&C 2023 contract|false positive risk|better|contract headline penalized without margin/PF bridge|

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L9_CONSTRUCTION_REALESTATE_HOUSING|C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|PF_BALANCE_SHEET_TRUST_BREAK_VS_RECOVERY_GUARD|1|3|2|3|4|0|5|4|3|True|True|remaining gap: more positive clean-recovery / PF-contained cases across non-HDC symbols|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus | stage3_yellow_total_min | stage3_green_total_min | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | hard_4c_thesis_break_routes_to_4c
residual_error_types_found: headline_contract_false_positive | trust_break_4c_too_late | post_4c_recovery_missed_structural
new_axis_proposed: C30_trust_break_hard_4c_guard | C30_clean_recovery_after_4c_reentry_bonus | C30_headline_contract_without_margin_bridge_penalty
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus | stage3_yellow_total_min | stage3_green_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- stock-web tradable OHLC rows for entry/forward windows
- 30D/90D/180D MFE/MAE proxy calculations
- same_entry_group dedupe
- corporate-action contamination gate via symbol profiles
- current calibrated profile stress-test proxy
```

Non-validation scope:

```text
- no production code inspected
- no live candidate scan
- no current recommendation
- event evidence summaries should be source-expanded before batch implementation
- score numbers are research proxy scores, not stock_agent production scores
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C30_trust_break_hard_4c_guard,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,execution/accounting trust break should override contract/backlog positives,reduced false-positive selection for GS/HDC trust-break cases,T_HDC_20220112_4C|T_GS_20230705_4C,4,4,3,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,C30_clean_recovery_after_4c_reentry_bonus,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,post-4C recovery requires observed low-MAE normalization and financial visibility,keeps HDC 2023 recovery eligible without weakening hard 4C,T_HDC_20231027_RECOVERY|T_HDC_20240228_STAGE3_GREEN_LABEL,4,4,3,low_to_medium,canonical_shadow_only,requires further holdout; not production
shadow_weight,C30_headline_contract_without_margin_bridge_penalty,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,mega-contract headline did not offset housing/PF margin uncertainty in Hyundai E&C sample,down-weights contract-only Stage2/Yellow promotions,T_HDEC_20230626_CONTRACT_COUNTER,4,4,3,low,canonical_shadow_only,counterexample-based guard
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R10L72_C30_HDC_20220112_4C","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"72","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_TRUST_BREAK_VS_RECOVERY_GUARD","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"T_HDC_20220112_4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"hard_4c_success","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Gwangju Hwajeong I-Park collapse; event after close, next-trading-day entry"}
{"row_type":"case","case_id":"R10L72_C30_GS_20230705_4C","symbol":"006360","company_name":"GS건설","round":"R10","loop":"72","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_TRUST_BREAK_VS_RECOVERY_GUARD","case_type":"4C_late","positive_or_counterexample":"counterexample","best_trigger":"T_GS_20230705_4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"execution_trust_break_drawdown","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"Incheon Geomdan apartment reconstruction/cost event; same-day close entry"}
{"row_type":"case","case_id":"R10L72_C30_HDC_20231027_RECOVERY","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"72","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_TRUST_BREAK_VS_RECOVERY_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_HDC_20231027_RECOVERY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"score_price_alignment":"post_4c_recovery_with_low_mae","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"Post-accident recovery/re-rating after lower red-team risk and price-confirmed normalization"}
{"row_type":"case","case_id":"R10L72_C30_HDEC_20230626_CONTRACT_COUNTER","symbol":"000720","company_name":"현대건설","round":"R10","loop":"72","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_TRUST_BREAK_VS_RECOVERY_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"T_HDEC_20230626_CONTRACT_COUNTER","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"contract_headline_without_margin_conversion","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Saudi Amiral mega-contract headline; no immediate margin/PF balance-sheet bridge"}
{"row_type":"trigger","trigger_id":"T_HDC_20220112_4C","case_id":"R10L72_C30_HDC_20220112_4C","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"72","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_TRUST_BREAK_VS_RECOVERY_GUARD","sector":"construction_realestate_housing","primary_archetype":"PF_balance_sheet_trust_break","loop_objective":"residual_false_positive_mining|residual_missed_structural_mining|4C_thesis_break_timing_test|sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill","trigger_type":"Stage4C","trigger_date":"2022-01-11","evidence_available_at_that_date":"Gwangju Hwajeong I-Park collapse; event after close, next-trading-day entry","evidence_source":"Gwangju Hwajeong I-Park collapse; event after close, next-trading-day entry","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block","explicit_event_cap"],"stage4c_evidence_fields":["thesis_evidence_broken","accounting_or_trust_break"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv","profile_path":"atlas/symbol_profiles/294/294870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-01-12","entry_price":20850,"MFE_30D_pct":8.87,"MFE_90D_pct":8.87,"MFE_180D_pct":8.87,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-35.25,"MAE_90D_pct":-36.93,"MAE_180D_pct":-50.84,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-01-12","peak_price":22700,"drawdown_after_peak_pct":-56.87,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["legal_or_regulatory_block","explicit_event_cap"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"hard_4c_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L72_C30_HDC_20220112_4C__2022-01-12","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_GS_20230705_4C","case_id":"R10L72_C30_GS_20230705_4C","symbol":"006360","company_name":"GS건설","round":"R10","loop":"72","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_TRUST_BREAK_VS_RECOVERY_GUARD","sector":"construction_realestate_housing","primary_archetype":"PF_balance_sheet_trust_break","loop_objective":"residual_false_positive_mining|residual_missed_structural_mining|4C_thesis_break_timing_test|sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill","trigger_type":"Stage4C","trigger_date":"2023-07-05","evidence_available_at_that_date":"Incheon Geomdan apartment reconstruction/cost event; same-day close entry","evidence_source":"Incheon Geomdan apartment reconstruction/cost event; same-day close entry","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block","explicit_event_cap"],"stage4c_evidence_fields":["thesis_evidence_broken","accounting_or_trust_break"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-05","entry_price":18030,"MFE_30D_pct":5.1,"MFE_90D_pct":5.1,"MFE_180D_pct":5.1,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-25.85,"MAE_90D_pct":-29.73,"MAE_180D_pct":-29.73,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-05","peak_price":18950,"drawdown_after_peak_pct":-33.14,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["legal_or_regulatory_block","explicit_event_cap"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"execution_trust_break_drawdown","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L72_C30_GS_20230705_4C__2023-07-05","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_HDC_20231027_RECOVERY","case_id":"R10L72_C30_HDC_20231027_RECOVERY","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"72","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_TRUST_BREAK_VS_RECOVERY_GUARD","sector":"construction_realestate_housing","primary_archetype":"PF_balance_sheet_trust_break","loop_objective":"residual_false_positive_mining|residual_missed_structural_mining|4C_thesis_break_timing_test|sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-10-27","evidence_available_at_that_date":"Post-accident recovery/re-rating after lower red-team risk and price-confirmed normalization","evidence_source":"Post-accident recovery/re-rating after lower red-team risk and price-confirmed normalization","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2023.csv","profile_path":"atlas/symbol_profiles/294/294870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-10-27","entry_price":11700,"MFE_30D_pct":37.86,"MFE_90D_pct":77.35,"MFE_180D_pct":87.61,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.15,"MAE_90D_pct":-6.15,"MAE_180D_pct":-6.15,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-17","peak_price":21950,"drawdown_after_peak_pct":-12.98,"green_lateness_ratio":0.85,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"post_4c_recovery_with_low_mae","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L72_C30_HDC_20231027_RECOVERY__2023-10-27","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_HDEC_20230626_CONTRACT_COUNTER","case_id":"R10L72_C30_HDEC_20230626_CONTRACT_COUNTER","symbol":"000720","company_name":"현대건설","round":"R10","loop":"72","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_TRUST_BREAK_VS_RECOVERY_GUARD","sector":"construction_realestate_housing","primary_archetype":"PF_balance_sheet_trust_break","loop_objective":"residual_false_positive_mining|residual_missed_structural_mining|4C_thesis_break_timing_test|sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-06-26","evidence_available_at_that_date":"Saudi Amiral mega-contract headline; no immediate margin/PF balance-sheet bridge","evidence_source":"Saudi Amiral mega-contract headline; no immediate margin/PF balance-sheet bridge","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","backlog_or_delivery_visibility"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000720/2023.csv","profile_path":"atlas/symbol_profiles/000/000720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-06-26","entry_price":40800,"MFE_30D_pct":8.82,"MFE_90D_pct":8.82,"MFE_180D_pct":8.82,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.32,"MAE_90D_pct":-17.89,"MAE_180D_pct":-18.5,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-26","peak_price":44400,"drawdown_after_peak_pct":-25.11,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"contract_headline_without_margin_conversion","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L72_C30_HDEC_20230626_CONTRACT_COUNTER__2023-06-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_HDC_20240228_STAGE3_GREEN_LABEL","case_id":"R10L72_C30_HDC_20231027_RECOVERY","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"72","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_TRUST_BREAK_VS_RECOVERY_GUARD","sector":"construction_realestate_housing","primary_archetype":"PF_balance_sheet_trust_break","loop_objective":"residual_false_positive_mining|residual_missed_structural_mining|4C_thesis_break_timing_test|sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill","trigger_type":"Stage3-Green","trigger_date":"2024-02-28","evidence_available_at_that_date":"Post-accident recovery/re-rating after lower red-team risk and price-confirmed normalization","evidence_source":"Post-accident recovery/re-rating after lower red-team risk and price-confirmed normalization","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","financial_visibility","relative_strength","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv","profile_path":"atlas/symbol_profiles/294/294870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-28","entry_price":20400,"MFE_30D_pct":1.72,"MFE_90D_pct":7.6,"MFE_180D_pct":38.24,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-21.23,"MAE_90D_pct":-21.23,"MAE_180D_pct":-21.23,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-26","peak_price":28200,"drawdown_after_peak_pct":-31.91,"green_lateness_ratio":0.85,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"post_4c_recovery_with_low_mae","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L72_C30_HDC_20231027_RECOVERY__20240228","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L72_C30_HDC_20220112_4C","trigger_id":"T_HDC_20220112_4C","symbol":"294870","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":-5,"legal_or_contract_risk_score":-5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":-5},"weighted_score_before":42,"stage_label_before":"Stage4B/4C-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":-8,"legal_or_contract_risk_score":-7,"dilution_cb_risk_score":0,"accounting_trust_risk_score":-8},"weighted_score_after":28,"stage_label_after":"Stage4C","changed_components":["execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"C30 shadow differentiates clean recovery evidence from headline contract or trust-break evidence.","MFE_90D_pct":8.87,"MAE_90D_pct":-36.93,"score_return_alignment_label":"hard_4c_success","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L72_C30_GS_20230705_4C","trigger_id":"T_GS_20230705_4C","symbol":"006360","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":-5,"legal_or_contract_risk_score":-5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":-5},"weighted_score_before":42,"stage_label_before":"Stage4B/4C-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":-8,"legal_or_contract_risk_score":-7,"dilution_cb_risk_score":0,"accounting_trust_risk_score":-8},"weighted_score_after":28,"stage_label_after":"Stage4C","changed_components":["execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"C30 shadow differentiates clean recovery evidence from headline contract or trust-break evidence.","MFE_90D_pct":5.1,"MAE_90D_pct":-29.73,"score_return_alignment_label":"execution_trust_break_drawdown","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L72_C30_HDC_20231027_RECOVERY","trigger_id":"T_HDC_20231027_RECOVERY","symbol":"294870","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":-3},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":6,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":-1},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","accounting_trust_risk_score"],"component_delta_explanation":"C30 shadow differentiates clean recovery evidence from headline contract or trust-break evidence.","MFE_90D_pct":77.35,"MAE_90D_pct":-6.15,"score_return_alignment_label":"post_4c_recovery_with_low_mae","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L72_C30_HDEC_20230626_CONTRACT_COUNTER","trigger_id":"T_HDEC_20230626_CONTRACT_COUNTER","symbol":"000720","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":9,"backlog_visibility_score":7,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":0,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow candidate","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":6,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":0,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":-4,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2-watch","changed_components":["margin_bridge_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"C30 shadow differentiates clean recovery evidence from headline contract or trust-break evidence.","MFE_90D_pct":8.82,"MAE_90D_pct":-17.89,"score_return_alignment_label":"contract_headline_without_margin_conversion","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L72_C30_HDC_20231027_RECOVERY","trigger_id":"T_HDC_20240228_STAGE3_GREEN_LABEL","symbol":"294870","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":7,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":-2},"weighted_score_before":88,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":7,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":-1},"weighted_score_after":90,"stage_label_after":"Stage3-Green","changed_components":["accounting_trust_risk_score"],"component_delta_explanation":"C30 shadow differentiates clean recovery evidence from headline contract or trust-break evidence.","MFE_90D_pct":7.6,"MAE_90D_pct":-21.23,"score_return_alignment_label":"post_4c_recovery_with_low_mae","current_profile_verdict":"current_profile_too_late"}
{"row_type":"residual_contribution","round":"R10","loop":"72","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":1,"counterexample_count":3,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["headline_contract_false_positive","trust_break_4c_too_late","post_4c_recovery_missed_structural"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"R10L72_C30_TY_20231228_WORKOUT_NARRATIVE","symbol":"009410","company_name":"태영건설","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reason":"workout trigger has evidence, but stock-web forward 180D is contaminated by trading suspension and 2024-10-31 corporate-action candidate; keep as narrative 4C guardrail only","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R10
completed_loop = 72
next_round = R11
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-Web source paths were verified from `Songdaiki/stock-web` during this run:

```text
manifest = atlas/manifest.json
HDC profile = atlas/symbol_profiles/294/294870.json
GS profile = atlas/symbol_profiles/006/006360.json
Hyundai E&C profile = atlas/symbol_profiles/000/000720.json
Taeyoung profile = atlas/symbol_profiles/009/009410.json
```

Price row anchors used in the calculations:

```text
294870 2022-01-12 close 20850, high 22700, later 180D low near 10250
294870 2023-10-27 close 11700, high 11720, low 10980; 2024-07-17 high 21950
006360 2023-07-05 close 18030, high 18950; 2023-10-10 low 12670
000720 2023-06-26 close 40800, high 44400; 2023-10-31 low 33250
009410 2023-12-28 close 2315; forward path blocked by later suspension/corporate-action candidate
```


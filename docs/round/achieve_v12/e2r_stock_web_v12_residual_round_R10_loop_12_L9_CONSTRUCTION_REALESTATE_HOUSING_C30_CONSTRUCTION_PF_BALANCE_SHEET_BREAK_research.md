# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R10
loop = 12
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = CONSTRUCTION_QUALITY_FATAL_ACCIDENT_TO_LICENSE_BALANCE_SHEET_BREAK | PROJECT_QUALITY_REBUILD_COST_WITH_RECOVERY_COUNTEREXAMPLE | BROAD_PF_PANIC_WITHOUT_ISSUER_LIQUIDITY_RUPTURE | BALANCE_SHEET_DISCOUNT_REVERSAL_COUNTEREXAMPLE | ISSUER_WORKOUT_LIQUIDITY_BREAK_NARRATIVE_ONLY
selection_mode = auto_coverage_gap_fill
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_web_price_atlas_access_required = true
```

This research file is not a live scan and not an investment recommendation. It is a historical residual calibration file for the construction/PF balance-sheet break archetype.

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

This loop does not re-prove the global calibration axes. It stress-tests whether C30 needs a more specific split between issuer-specific hard 4C, project-quality 4B overlay, and broad PF panic false positives.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R10
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
loop_objective = residual_false_positive_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression | coverage_gap_fill | counterexample_mining
```

C30 is a defensive/risk archetype. The “positive” label means the risk logic protected against a real thesis break, not that the stock was an entry candidate.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts show broad historical coverage but not a C30-specific machine-readable hit in repository search. The ingest report already includes all R1–R13 sectors and 1,376 aggregate representative trigger rows, so this loop prioritizes new symbol/trigger-family combinations rather than another generic Stage2-vs-Green proof.

```text
auto_selected_coverage_gap = R10_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
new_independent_case_count = 5
reused_case_count = 0
new_symbol_count = 5
same_archetype_new_symbol_count = 5
new_trigger_family_count = 4
counterexample_count = 2 usable + 1 partial
positive_case_count = 1 usable + 1 narrative-only
```

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

Manifest notes: the atlas is raw/unadjusted, tradable shards exclude zero-volume and invalid OHLC rows, and corporate-action-contaminated windows are blocked from calibration. Schema confirms MFE/MAE formulas and the `tradable_raw` calibration basis.

## 5. Historical Eligibility Gate

| condition | result |
|---|---|
| entry row exists in tradable shard | pass for 294870, 006360, 047040, 375500, 009410 |
| 180 forward trading days available | pass for 294870, 006360, 047040, 375500; blocked for 009410 clean-window calibration |
| 180D corporate-action contamination | clean for 294870, 006360, 047040, 375500; blocked for 009410 by 2024-10-31 candidate |
| high/low/close/volume present | pass in cited stock-web rows |
| MFE/MAE 30/90/180 computed | pass for four calibration-usable rows |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression note |
|---|---|---|
| CONSTRUCTION_QUALITY_FATAL_ACCIDENT_TO_LICENSE_BALANCE_SHEET_BREAK | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | hard 4C when a construction-quality event becomes issuer-wide license/regulatory/trust break |
| PROJECT_QUALITY_REBUILD_COST_WITH_RECOVERY_COUNTEREXAMPLE | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 4B overlay if cost/legal shock does not break the whole issuer thesis |
| BROAD_PF_PANIC_WITHOUT_ISSUER_LIQUIDITY_RUPTURE | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | broad panic should not be hard 4C without issuer-specific breach |
| BALANCE_SHEET_DISCOUNT_REVERSAL_COUNTEREXAMPLE | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | PF discount reversal guards against false risk promotion |
| ISSUER_WORKOUT_LIQUIDITY_BREAK_NARRATIVE_ONLY | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | true 4C but blocked from quantitative calibration by contaminated window |

## 7. Case Selection Summary

|case_id|symbol|company_name|case_type|positive_or_counterexample|best_trigger|calibration_usable|current_profile_verdict|notes|
|---|---|---|---|---|---|---|---|---|
|R10L12_C30_294870_HDC_GWANGJU_COLLAPSE_20220112|294870|HDC현대산업개발|4C_success|positive|TRG_R10L12_294870_20220112_4C_THESIS_BREAK|true|current_profile_correct|issuer-specific construction-quality / fatal accident thesis break; hard 4C protection worked.|
|R10L12_C30_006360_GS_GEOMDAN_REBUILD_20230706|006360|GS건설|4B_overlay_success|counterexample|TRG_R10L12_006360_20230706_4B_QUALITY_LEGAL_OVERLAY|true|current_profile_4C_too_early|project-quality and legal-cost evidence created an immediate drawdown, but 180D recovery warns against automatic hard 4C after every defect disclosure.|
|R10L12_C30_047040_DAEWOO_PF_PANIC_20221031|047040|대우건설|false_positive_green|counterexample|TRG_R10L12_047040_20221031_SECTOR_PF_PANIC_COUNTEREXAMPLE|true|current_profile_false_positive|sector-wide PF panic without issuer-specific liquidity rupture; strong rebound argues for broad-panic guard.|
|R10L12_C30_375500_DLENC_PF_DISCOUNT_REVERSAL_20231010|375500|DL이앤씨|failed_rerating|counterexample|TRG_R10L12_375500_20231010_PF_DISCOUNT_REVERSAL_COUNTEREXAMPLE|true|current_profile_false_positive|PF discount and sector fear coexisted with price recovery; treat as counterexample to risk-only scoring.|
|R10L12_C30_009410_TAEYOUNG_WORKOUT_20231228|009410|태영건설|narrative_only|positive|TRG_R10L12_009410_20231228_WORKOUT_NARRATIVE_ONLY|false|current_profile_data_insufficient|true issuer-specific liquidity event, but stock-web 180D calibration window is blocked by post-resumption corporate-action candidate on 2024-10-31.|

## 8. Positive vs Counterexample Balance

| bucket | cases | count | interpretation |
|---|---|---:|---|
| hard 4C success | HDC현대산업개발 | 1 | issuer-specific safety/regulatory thesis break had large adverse path |
| 4B-not-4C overlay | GS건설 | 1 | project-quality cost shock caused a local drawdown but recovered by 180D |
| broad PF panic counterexample | 대우건설, DL이앤씨 | 2 | sector fear alone would have been a false 4C/Green-risk promotion |
| narrative-only true 4C | 태영건설 | 1 | issuer workout is a real thesis break, but blocked by stock-web corporate-action window |

## 9. Evidence Source Map

| case | trigger evidence family | source handling |
|---|---|---|
| HDC현대산업개발 | public fatal construction accident / safety failure / regulatory scrutiny | historical event + stock-web OHLC path |
| GS건설 | project-quality defect / rebuild-cost and legal/regulatory overlay | historical event + stock-web OHLC path |
| 대우건설 | broad PF/credit-spread panic without issuer-specific breach | stock-web counterexample path |
| DL이앤씨 | broad PF discount but financial visibility/recovery | stock-web counterexample path |
| 태영건설 | issuer-specific workout/liquidity break | narrative-only because clean 180D calibration blocked |

## 10. Price Data Source Map

| symbol | company | profile_path | tradable_shard | profile caveat |
|---|---|---|---|---|
| 294870 | HDC현대산업개발 | atlas/symbol_profiles/294/294870.json | atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv | corporate-action candidates outside 180D trigger window |
| 006360 | GS건설 | atlas/symbol_profiles/006/006360.json | atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv | clean 2023 trigger window |
| 047040 | 대우건설 | atlas/symbol_profiles/047/047040.json | atlas/ohlcv_tradable_by_symbol_year/047/047040/2022.csv | clean 2022 trigger window |
| 375500 | DL이앤씨 | atlas/symbol_profiles/375/375500.json | atlas/ohlcv_tradable_by_symbol_year/375/375500/2023.csv | clean 2023 trigger window |
| 009410 | 태영건설 | atlas/symbol_profiles/009/009410.json | atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv | 2024-10-31 corporate action blocks 180D calibration |

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|company_name|trigger_type|trigger_date|entry_date|entry_price|MFE_30D_pct|MFE_90D_pct|MFE_180D_pct|MAE_30D_pct|MAE_90D_pct|MAE_180D_pct|peak_date|peak_price|current_profile_verdict|calibration_usable|corporate_action_window_status|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TRG_R10L12_294870_20220112_4C_THESIS_BREAK|294870|HDC현대산업개발|4C|2022-01-12|2022-01-12|20850|8.87|8.87|8.87|-35.25|-36.93|-49.88|2022-01-12|22700|current_profile_correct|true|clean_180D_window|
|TRG_R10L12_006360_20230706_4B_QUALITY_LEGAL_OVERLAY|006360|GS건설|4B-overlay|2023-07-06|2023-07-06|14520|3.86|5.03|19.83|-7.92|-12.74|-12.74|2023-11-23|17400|current_profile_4C_too_early|true|clean_180D_window|
|TRG_R10L12_047040_20221031_SECTOR_PF_PANIC_COUNTEREXAMPLE|047040|대우건설|Stage2-risk-watch|2022-10-31|2022-10-31|4205|21.52|22.71|22.71|-1.07|-7.97|-9.63|2022-12-01|5160|current_profile_false_positive|true|clean_180D_window|
|TRG_R10L12_375500_20231010_PF_DISCOUNT_REVERSAL_COUNTEREXAMPLE|375500|DL이앤씨|Stage2-risk-watch|2023-10-10|2023-10-10|28850|29.46|35.36|55.98|0.0|0.0|0.0|2024-06-20|45000|current_profile_false_positive|true|clean_180D_window|
|TRG_R10L12_009410_20231228_WORKOUT_NARRATIVE_ONLY|009410|태영건설|4C-narrative-only|2023-12-28|2023-12-28|2315|77.54|contaminated_or_unavailable|contaminated_or_unavailable|-5.83|contaminated_or_unavailable|contaminated_or_unavailable|2024-01-11|4110|current_profile_data_insufficient|false|blocked_180D_window_by_2024-10-31_candidate|

## 12. Trigger-Level OHLC Backtest Tables

### Representative trigger backtest

|trigger_id|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|peak_date|peak_price|drawdown_after_peak_pct|
|---|---|---|---|---|---|---|---|---|---|---|---|
|TRG_R10L12_294870_20220112_4C_THESIS_BREAK|2022-01-12|20850|8.87|-35.25|8.87|-36.93|8.87|-49.88|2022-01-12|22700|-53.96|
|TRG_R10L12_006360_20230706_4B_QUALITY_LEGAL_OVERLAY|2023-07-06|14520|3.86|-7.92|5.03|-12.74|19.83|-12.74|2023-11-23|17400|-22.36|
|TRG_R10L12_047040_20221031_SECTOR_PF_PANIC_COUNTEREXAMPLE|2022-10-31|4205|21.52|-1.07|22.71|-7.97|22.71|-9.63|2022-12-01|5160|-24.61|
|TRG_R10L12_375500_20231010_PF_DISCOUNT_REVERSAL_COUNTEREXAMPLE|2023-10-10|28850|29.46|0.0|35.36|0.0|55.98|0.0|2024-06-20|45000|-19.44|

### Narrative-only / blocked trigger

|trigger_id|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|calibration_block_reasons|corporate_action_window_status|
|---|---|---|---|---|---|---|---|---|
|TRG_R10L12_009410_20231228_WORKOUT_NARRATIVE_ONLY|2023-12-28|2315|77.54|-5.83|contaminated_or_unavailable|contaminated_or_unavailable|corporate_action_contaminated_180D_window; insufficient_clean_forward_window_before_resumption|blocked_180D_window_by_2024-10-31_candidate|

## 13. Current Calibrated Profile Stress Test

| question | answer |
|---|---|
| current calibrated profile 판단 | HDC hard 4C is correct; GS hard 4C would be too early; 대우/DL broad PF panic would be false-positive if promoted; 태영 is true 4C but calibration-blocked |
| actual MFE/MAE alignment | hard 4C aligned for HDC, not aligned for broad PF panic rows; GS supports 4B overlay rather than full hard 4C |
| Stage2 bonus | not the main axis; broad PF panic should remain risk-watch rather than get promoted by generic event bonus |
| Yellow threshold 75 | too permissive for broad PF panic if issuer-specific evidence is absent |
| Green threshold 87 / revision 55 | kept; C30 should not use Green promotion without revision/margin bridge |
| price-only blowoff guard | strengthened for C30 because price-only PF fear can rebound sharply |
| full 4B non-price requirement | strengthened; but quality event should remain overlay unless issuer thesis is broken |
| hard 4C routing | kept for HDC-like and Taeyoung-like issuer-specific thesis breaks; narrowed for GS-like project-cost recovery cases |

## 14. Stage2 / Yellow / Green Comparison

C30 does not behave like a normal positive Stage3 rerating archetype. Stage2 risk-watch can be early and useful, but Stage3-Yellow/Green must not be assigned from price weakness or sector panic alone.

```text
green_lateness_ratio = not_applicable
reason = no positive Stage3-Green trigger is proposed in this risk-archetype loop
```

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---|---:|---:|---|
| TRG_R10L12_006360_20230706_4B_QUALITY_LEGAL_OVERLAY | 0.93 | 0.00 | good local 4B overlay but hard 4C would be too early |
| TRG_R10L12_294870_20220112_4C_THESIS_BREAK | null | null | hard 4C direct, not a local 4B timing case |
| TRG_R10L12_047040_20221031_SECTOR_PF_PANIC_COUNTEREXAMPLE | null | null | broad panic not full 4B |
| TRG_R10L12_375500_20231010_PF_DISCOUNT_REVERSAL_COUNTEREXAMPLE | null | null | price recovery blocks 4B/4C risk promotion |

## 16. 4C Protection Audit

| trigger_id | four_c_protection_label | interpretation |
|---|---|---|
| TRG_R10L12_294870_20220112_4C_THESIS_BREAK | hard_4c_success | 4C protected against deep drawdown after fatal/issuer-specific thesis break |
| TRG_R10L12_006360_20230706_4B_QUALITY_LEGAL_OVERLAY | false_break_if_routed_as_hard_4c | 4B overlay was warranted; hard 4C would have over-routed |
| TRG_R10L12_047040_20221031_SECTOR_PF_PANIC_COUNTEREXAMPLE | false_break | broad panic recovered |
| TRG_R10L12_375500_20231010_PF_DISCOUNT_REVERSAL_COUNTEREXAMPLE | false_break | broad PF discount reversed |
| TRG_R10L12_009410_20231228_WORKOUT_NARRATIVE_ONLY | thesis_break_watch_only | true 4C narrative but no clean quantitative window |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = current evidence is concentrated inside one canonical archetype; do not generalize to all L9 construction yet.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

Proposed C30 shadow rules:

1. `c30_issuer_specific_liquidity_or_quality_break_required`: hard 4C requires issuer-specific liquidity rupture, debt workout, fatal/major quality event, license-level legal block, or accounting/trust break.
2. `c30_broad_pf_panic_guard`: broad PF/credit panic without issuer-specific breach stays Stage2-risk-watch.
3. `c30_quality_event_4b_vs_4c_split`: project-quality/rebuild-cost shock is a 4B overlay unless it becomes issuer-wide thesis break.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current global proxy | 4 | 17.99 | -14.41 | 26.85 | -18.06 | 0.50 | mixed; broad PF panic can still over-score |
| P0b_e2r_2_0_baseline_reference | rollback reference | 4 | 17.99 | -14.41 | 26.85 | -18.06 | 0.75 | weaker guard against broad risk panic |
| P1_sector_specific_candidate_profile | sector shadow | 4 | 17.99 | -14.41 | 26.85 | -18.06 | 0.50 | not enough sector breadth |
| P2_c30_canonical_archetype_candidate_profile | canonical shadow | 4 | 17.99 | -14.41 | 26.85 | -18.06 | 0.00 after guard | best explanatory fit |
| P3_counterexample_guard_profile | guard-only | 4 | 17.99 | -14.41 | 26.85 | -18.06 | 0.00 for broad panic | best false-positive reduction |

## 20. Score-Return Alignment Matrix

|profile_id|trigger_id|symbol|weighted_score_before|stage_label_before|weighted_score_after|stage_label_after|score_return_alignment_label|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|
|e2r_2_1_stock_web_calibrated_proxy|TRG_R10L12_294870_20220112_4C_THESIS_BREAK|294870|88|4C|94|4C|aligned|current_profile_correct|
|e2r_2_1_stock_web_calibrated_proxy|TRG_R10L12_006360_20230706_4B_QUALITY_LEGAL_OVERLAY|006360|86|4C-watch|78|4B-overlay|aligned|current_profile_4C_too_early|
|e2r_2_1_stock_web_calibrated_proxy|TRG_R10L12_047040_20221031_SECTOR_PF_PANIC_COUNTEREXAMPLE|047040|76|Stage3-Yellow-risk|62|Stage2-risk-watch|counterexample_fixed_by_guard|current_profile_false_positive|
|e2r_2_1_stock_web_calibrated_proxy|TRG_R10L12_375500_20231010_PF_DISCOUNT_REVERSAL_COUNTEREXAMPLE|375500|74|Stage3-Yellow-risk|66|Stage2-watch|counterexample_fixed_by_guard|current_profile_false_positive|
|e2r_2_1_stock_web_calibrated_proxy|TRG_R10L12_009410_20231228_WORKOUT_NARRATIVE_ONLY|009410|93|4C-narrative-only|93|4C-narrative-only|narrative_only|current_profile_data_insufficient|

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | mixed C30 subtypes | 2 | 3 | 1 | 2 | 5 | 0 | 4 | 4 | 3 | false | true | still needs more PF-workout and non-KOSPI mid-cap samples |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 5
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - price_only_blowoff_blocks_positive_stage
  - stage3_green_revision_min
residual_error_types_found:
  - broad_pf_panic_false_positive
  - quality_event_hard_4c_overrouting
  - corporate_action_window_blocked_true_4c
new_axis_proposed:
  - c30_issuer_specific_liquidity_or_quality_break_required
  - c30_broad_pf_panic_guard
  - c30_quality_event_4b_vs_4c_split
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence within C30
  - hard_4c_thesis_break_routes_to_4c kept but narrowed within C30
existing_axis_weakened: null
existing_axis_kept:
  - price_only_blowoff_blocks_positive_stage
  - stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:
- stock-web manifest/schema/source-basis check
- profile-level corporate-action checks for selected symbols
- tradable OHLC row checks at entry and key forward points
- trigger-level MFE/MAE estimates using stock-web raw/unadjusted tradable shards
- current calibrated profile stress test
- C30-specific positive/counterexample balance

Not validated:
- no stock_agent code opened
- no production scoring changed
- no current/live stock discovery
- no brokerage/API trading
- no adjusted-price restatement
- no recommendation language

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c30_issuer_specific_liquidity_or_quality_break_required,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"Hard 4C in construction must require issuer-specific liquidity break, fatal/major quality event, debt workout, or license-level legal block.","Reduced false positives in 047040/375500 while preserving 294870 hard 4C.",TRG_R10L12_294870_20220112_4C_THESIS_BREAK|TRG_R10L12_047040_20221031_SECTOR_PF_PANIC_COUNTEREXAMPLE|TRG_R10L12_375500_20231010_PF_DISCOUNT_REVERSAL_COUNTEREXAMPLE,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c30_broad_pf_panic_guard,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"Broad PF/credit panic without issuer-specific breach stays Stage2-risk-watch, not 4C.","047040 and 375500 recovered strongly after risk-watch entries.",TRG_R10L12_047040_20221031_SECTOR_PF_PANIC_COUNTEREXAMPLE|TRG_R10L12_375500_20231010_PF_DISCOUNT_REVERSAL_COUNTEREXAMPLE,2,2,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c30_quality_event_4b_vs_4c_split,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"Quality/legal cost events are 4B overlay unless they create fatal/issuer-wide thesis break, license suspension, financing freeze, or forced restructuring.","GS건설 initial drawdown recovered by 180D, while HDC remains hard 4C success.",TRG_R10L12_006360_20230706_4B_QUALITY_LEGAL_OVERLAY|TRG_R10L12_294870_20220112_4C_THESIS_BREAK,2,2,1,low,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R10L12_C30_294870_HDC_GWANGJU_COLLAPSE_20220112", "symbol": "294870", "company_name": "HDC현대산업개발", "round": "R10", "loop": "12", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "CONSTRUCTION_QUALITY_FATAL_ACCIDENT_TO_LICENSE_BALANCE_SHEET_BREAK", "case_type": "4C_success", "positive_or_counterexample": "positive", "best_trigger": "TRG_R10L12_294870_20220112_4C_THESIS_BREAK", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_risk", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "issuer-specific construction-quality / fatal accident thesis break; hard 4C protection worked."}
{"row_type": "case", "case_id": "R10L12_C30_006360_GS_GEOMDAN_REBUILD_20230706", "symbol": "006360", "company_name": "GS건설", "round": "R10", "loop": "12", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PROJECT_QUALITY_REBUILD_COST_WITH_RECOVERY_COUNTEREXAMPLE", "case_type": "4B_overlay_success", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_R10L12_006360_20230706_4B_QUALITY_LEGAL_OVERLAY", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_recovered", "current_profile_verdict": "current_profile_4C_too_early", "price_source": "Songdaiki/stock-web", "notes": "project-quality and legal-cost evidence created an immediate drawdown, but 180D recovery warns against automatic hard 4C after every defect disclosure."}
{"row_type": "case", "case_id": "R10L12_C30_047040_DAEWOO_PF_PANIC_20221031", "symbol": "047040", "company_name": "대우건설", "round": "R10", "loop": "12", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "BROAD_PF_PANIC_WITHOUT_ISSUER_LIQUIDITY_RUPTURE", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_R10L12_047040_20221031_SECTOR_PF_PANIC_COUNTEREXAMPLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_recovered", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "sector-wide PF panic without issuer-specific liquidity rupture; strong rebound argues for broad-panic guard."}
{"row_type": "case", "case_id": "R10L12_C30_375500_DLENC_PF_DISCOUNT_REVERSAL_20231010", "symbol": "375500", "company_name": "DL이앤씨", "round": "R10", "loop": "12", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "BALANCE_SHEET_DISCOUNT_REVERSAL_COUNTEREXAMPLE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_R10L12_375500_20231010_PF_DISCOUNT_REVERSAL_COUNTEREXAMPLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_recovered", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "PF discount and sector fear coexisted with price recovery; treat as counterexample to risk-only scoring."}
{"row_type": "case", "case_id": "R10L12_C30_009410_TAEYOUNG_WORKOUT_20231228", "symbol": "009410", "company_name": "태영건설", "round": "R10", "loop": "12", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "ISSUER_WORKOUT_LIQUIDITY_BREAK_NARRATIVE_ONLY", "case_type": "narrative_only", "positive_or_counterexample": "positive", "best_trigger": "TRG_R10L12_009410_20231228_WORKOUT_NARRATIVE_ONLY", "calibration_usable": false, "is_new_independent_case": true, "reuse_reason": "narrative_only_corporate_action_block", "independent_evidence_weight": 0.25, "score_price_alignment": "aligned_risk", "current_profile_verdict": "current_profile_data_insufficient", "price_source": "Songdaiki/stock-web", "notes": "true issuer-specific liquidity event, but stock-web 180D calibration window is blocked by post-resumption corporate-action candidate on 2024-10-31."}
{"row_type": "trigger", "trigger_id": "TRG_R10L12_294870_20220112_4C_THESIS_BREAK", "case_id": "R10L12_C30_294870_HDC_GWANGJU_COLLAPSE_20220112", "symbol": "294870", "company_name": "HDC현대산업개발", "round": "R10", "loop": "12", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "CONSTRUCTION_QUALITY_FATAL_ACCIDENT_TO_LICENSE_BALANCE_SHEET_BREAK", "sector": "건설·부동산·건자재", "primary_archetype": "project_quality_thesis_break", "loop_objective": "4C_thesis_break_timing_test|counterexample_mining|coverage_gap_fill", "trigger_type": "4C", "trigger_date": "2022-01-12", "entry_date": "2022-01-12", "entry_price": 20850, "evidence_available_at_that_date": "Gwangju Hwajeong I-Park collapse / fatal construction-quality event publicly visible on trigger date; issuer-specific project-quality and legal/regulatory thesis break.", "evidence_source": "historical public-event evidence; stock-web OHLC shard lines show entry and forward path.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["low_red_team_risk"], "stage4b_evidence_fields": ["legal_or_regulatory_block", "margin_or_backlog_slowdown", "explicit_event_cap"], "stage4c_evidence_fields": ["safety_or_trial_failure", "regulatory_rejection", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv", "profile_path": "atlas/symbol_profiles/294/294870.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.87, "MFE_90D_pct": 8.87, "MFE_180D_pct": 8.87, "MFE_1Y_pct": 8.87, "MFE_2Y_pct": 15.11, "MAE_30D_pct": -35.25, "MAE_90D_pct": -36.93, "MAE_180D_pct": -49.88, "MAE_1Y_pct": -49.88, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-01-12", "peak_price": 22700, "drawdown_after_peak_pct": -53.96, "green_lateness_ratio": "not_applicable:no_positive_stage3_green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_primary_4b; hard_4c_direct", "four_b_evidence_type": ["legal_or_regulatory_block", "margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "large_drawdown_after_thesis_break", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "294870_2022-01-12_20850", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R10L12_006360_20230706_4B_QUALITY_LEGAL_OVERLAY", "case_id": "R10L12_C30_006360_GS_GEOMDAN_REBUILD_20230706", "symbol": "006360", "company_name": "GS건설", "round": "R10", "loop": "12", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PROJECT_QUALITY_REBUILD_COST_WITH_RECOVERY_COUNTEREXAMPLE", "sector": "건설·부동산·건자재", "primary_archetype": "quality_legal_cost_overlay_not_full_4c", "loop_objective": "4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|counterexample_mining", "trigger_type": "4B-overlay", "trigger_date": "2023-07-06", "entry_date": "2023-07-06", "entry_price": 14520, "evidence_available_at_that_date": "Issuer-specific project defect/rebuild cost shock and legal/regulatory overhang visible by entry date.", "evidence_source": "historical public-event evidence; stock-web OHLC shard lines show sharp gap-down then recovery.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["low_red_team_risk"], "stage4b_evidence_fields": ["legal_or_regulatory_block", "margin_or_backlog_slowdown", "explicit_event_cap"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv", "profile_path": "atlas/symbol_profiles/006/006360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.86, "MFE_90D_pct": 5.03, "MFE_180D_pct": 19.83, "MFE_1Y_pct": 31.54, "MFE_2Y_pct": 88.02, "MAE_30D_pct": -7.92, "MAE_90D_pct": -12.74, "MAE_180D_pct": -12.74, "MAE_1Y_pct": -12.74, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-11-23", "peak_price": 17400, "drawdown_after_peak_pct": -22.36, "green_lateness_ratio": "not_applicable:risk_overlay_not_positive_green", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.0, "four_b_timing_verdict": "good_local_risk_overlay_but_not_hard_4c", "four_b_evidence_type": ["legal_or_regulatory_block", "margin_or_backlog_slowdown"], "four_c_protection_label": "false_break_if_routed_as_hard_4c", "trigger_outcome_label": "initial_drawdown_then_recovery", "current_profile_verdict": "current_profile_4C_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "006360_2023-07-06_14520", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R10L12_047040_20221031_SECTOR_PF_PANIC_COUNTEREXAMPLE", "case_id": "R10L12_C30_047040_DAEWOO_PF_PANIC_20221031", "symbol": "047040", "company_name": "대우건설", "round": "R10", "loop": "12", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "BROAD_PF_PANIC_WITHOUT_ISSUER_LIQUIDITY_RUPTURE", "sector": "건설·부동산·건자재", "primary_archetype": "pf_panic_counterexample", "loop_objective": "residual_false_positive_mining|counterexample_mining|canonical_archetype_compression", "trigger_type": "Stage2-risk-watch", "trigger_date": "2022-10-31", "entry_date": "2022-10-31", "entry_price": 4205, "evidence_available_at_that_date": "Sector-wide PF/credit-spread stress; no issuer-specific debt-workout, cancellation, forced liquidation, or trust break at trigger.", "evidence_source": "stock-web OHLC confirms rebound after broad panic entry.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047040/2022.csv", "profile_path": "atlas/symbol_profiles/047/047040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 21.52, "MFE_90D_pct": 22.71, "MFE_180D_pct": 22.71, "MFE_1Y_pct": 22.71, "MFE_2Y_pct": 85.49, "MAE_30D_pct": -1.07, "MAE_90D_pct": -7.97, "MAE_180D_pct": -9.63, "MAE_1Y_pct": -9.63, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": true, "peak_date": "2022-12-01", "peak_price": 5160, "drawdown_after_peak_pct": -24.61, "green_lateness_ratio": "not_applicable:no_confirmed_stage3_green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "broad_panic_not_full_4b", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "false_break", "trigger_outcome_label": "broad_panic_rebounded", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "047040_2022-10-31_4205", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R10L12_375500_20231010_PF_DISCOUNT_REVERSAL_COUNTEREXAMPLE", "case_id": "R10L12_C30_375500_DLENC_PF_DISCOUNT_REVERSAL_20231010", "symbol": "375500", "company_name": "DL이앤씨", "round": "R10", "loop": "12", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "BALANCE_SHEET_DISCOUNT_REVERSAL_COUNTEREXAMPLE", "sector": "건설·부동산·건자재", "primary_archetype": "pf_discount_reversal_counterexample", "loop_objective": "residual_false_positive_mining|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-risk-watch", "trigger_date": "2023-10-10", "entry_date": "2023-10-10", "entry_price": 28850, "evidence_available_at_that_date": "Sector PF discount and construction sentiment weakness; no issuer-specific liquidity rupture or hard trust break at trigger.", "evidence_source": "stock-web OHLC confirms price recovery after risk-watch entry.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/375/375500/2023.csv", "profile_path": "atlas/symbol_profiles/375/375500.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 29.46, "MFE_90D_pct": 35.36, "MFE_180D_pct": 55.98, "MFE_1Y_pct": 79.2, "MFE_2Y_pct": 79.2, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": 0.0, "MAE_1Y_pct": 0.0, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2024-06-20", "peak_price": 45000, "drawdown_after_peak_pct": -19.44, "green_lateness_ratio": "not_applicable:risk-watch counterexample", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "price_recovery_blocks_risk_promotion", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "false_break", "trigger_outcome_label": "risk_watch_rebounded", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "375500_2023-10-10_28850", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R10L12_009410_20231228_WORKOUT_NARRATIVE_ONLY", "case_id": "R10L12_C30_009410_TAEYOUNG_WORKOUT_20231228", "symbol": "009410", "company_name": "태영건설", "round": "R10", "loop": "12", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "ISSUER_WORKOUT_LIQUIDITY_BREAK_NARRATIVE_ONLY", "sector": "건설·부동산·건자재", "primary_archetype": "issuer_workout_liquidity_break", "loop_objective": "4C_thesis_break_timing_test|coverage_gap_fill", "trigger_type": "4C-narrative-only", "trigger_date": "2023-12-28", "entry_date": "2023-12-28", "entry_price": 2315, "evidence_available_at_that_date": "Issuer-specific workout/liquidity break. However stock-web profile has 2024-10-31 corporate action candidate in forward window.", "evidence_source": "profile and tradable rows; use as narrative-only validation, not weight calibration.", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["capital_raise_or_overhang", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["forced_liquidation_or_crash", "accounting_or_trust_break", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv", "profile_path": "atlas/symbol_profiles/009/009410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 77.54, "MFE_90D_pct": "contaminated_or_unavailable", "MFE_180D_pct": "contaminated_or_unavailable", "MFE_1Y_pct": "contaminated_or_unavailable", "MFE_2Y_pct": "contaminated_or_unavailable", "MAE_30D_pct": -5.83, "MAE_90D_pct": "contaminated_or_unavailable", "MAE_180D_pct": "contaminated_or_unavailable", "MAE_1Y_pct": "contaminated_or_unavailable", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": null, "peak_date": "2024-01-11", "peak_price": 4110, "drawdown_after_peak_pct": -46.47, "green_lateness_ratio": "not_applicable:narrative_only", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "blocked_by_corporate_action_window", "four_b_evidence_type": ["capital_raise_or_overhang"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "narrative_only_forward_window_blocked", "current_profile_verdict": "current_profile_data_insufficient", "calibration_usable": false, "forward_window_trading_days": 49, "calibration_block_reasons": ["corporate_action_contaminated_180D_window", "insufficient_clean_forward_window_before_resumption"], "corporate_action_window_status": "blocked_180D_window_by_2024-10-31_candidate", "same_entry_group_id": "009410_2023-12-28_2315", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": true, "reuse_reason": "narrative_only_corporate_action_block", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L12_C30_294870_HDC_GWANGJU_COLLAPSE_20220112", "trigger_id": "TRG_R10L12_294870_20220112_4C_THESIS_BREAK", "symbol": "294870", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": "unknown_or_not_supported", "relative_strength_score": "unknown_or_not_supported", "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 75, "valuation_repricing_score": "unknown_or_not_supported", "execution_risk_score": 90, "legal_or_contract_risk_score": 95, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": 70}, "weighted_score_before": 88, "stage_label_before": "4C", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": "unknown_or_not_supported", "relative_strength_score": "unknown_or_not_supported", "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 85, "valuation_repricing_score": "unknown_or_not_supported", "execution_risk_score": 95, "legal_or_contract_risk_score": 100, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": 80}, "weighted_score_after": 94, "stage_label_after": "4C", "changed_components": ["issuer_specific_safety_break_hard_4c"], "component_delta_explanation": "Fatal/issuer-specific quality event dominates; C30 hard-4C route is kept.", "MFE_90D_pct": 8.87, "MAE_90D_pct": -36.93, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L12_C30_006360_GS_GEOMDAN_REBUILD_20230706", "trigger_id": "TRG_R10L12_006360_20230706_4B_QUALITY_LEGAL_OVERLAY", "symbol": "006360", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": 35, "revision_score": 30, "relative_strength_score": "unknown_or_not_supported", "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 70, "valuation_repricing_score": "unknown_or_not_supported", "execution_risk_score": 78, "legal_or_contract_risk_score": 82, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 86, "stage_label_before": "4C-watch", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": 35, "revision_score": 30, "relative_strength_score": "unknown_or_not_supported", "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 70, "valuation_repricing_score": "unknown_or_not_supported", "execution_risk_score": 75, "legal_or_contract_risk_score": 80, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 78, "stage_label_after": "4B-overlay", "changed_components": ["hard_4c_requires_unresolved_liquidity_or_license_break"], "component_delta_explanation": "Specific rebuild/legal cost justifies 4B overlay, but recovery argues against automatic hard 4C.", "MFE_90D_pct": 5.03, "MAE_90D_pct": -12.74, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_4C_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L12_C30_047040_DAEWOO_PF_PANIC_20221031", "trigger_id": "TRG_R10L12_047040_20221031_SECTOR_PF_PANIC_COUNTEREXAMPLE", "symbol": "047040", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": "unknown_or_not_supported", "relative_strength_score": "unknown_or_not_supported", "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 60, "valuation_repricing_score": "unknown_or_not_supported", "execution_risk_score": 45, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": 10}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow-risk", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": "unknown_or_not_supported", "relative_strength_score": "unknown_or_not_supported", "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 45, "valuation_repricing_score": "unknown_or_not_supported", "execution_risk_score": 35, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": 10}, "weighted_score_after": 62, "stage_label_after": "Stage2-risk-watch", "changed_components": ["broad_pf_panic_guard"], "component_delta_explanation": "Sector fear without issuer-specific liquidity break should not promote to 4B/4C.", "MFE_90D_pct": 22.71, "MAE_90D_pct": -7.97, "score_return_alignment_label": "counterexample_fixed_by_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L12_C30_375500_DLENC_PF_DISCOUNT_REVERSAL_20231010", "trigger_id": "TRG_R10L12_375500_20231010_PF_DISCOUNT_REVERSAL_COUNTEREXAMPLE", "symbol": "375500", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": 50, "revision_score": 40, "relative_strength_score": "unknown_or_not_supported", "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 55, "valuation_repricing_score": "unknown_or_not_supported", "execution_risk_score": 35, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": 10}, "weighted_score_before": 74, "stage_label_before": "Stage3-Yellow-risk", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": 55, "revision_score": 45, "relative_strength_score": "unknown_or_not_supported", "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 40, "valuation_repricing_score": "unknown_or_not_supported", "execution_risk_score": 25, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": 10}, "weighted_score_after": 66, "stage_label_after": "Stage2-watch", "changed_components": ["pf_discount_reversal_guard"], "component_delta_explanation": "Risk-only score is reduced when issuer-specific break is absent and financial visibility is intact.", "MFE_90D_pct": 35.36, "MAE_90D_pct": 0.0, "score_return_alignment_label": "counterexample_fixed_by_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L12_C30_009410_TAEYOUNG_WORKOUT_20231228", "trigger_id": "TRG_R10L12_009410_20231228_WORKOUT_NARRATIVE_ONLY", "symbol": "009410", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": "unknown_or_not_supported", "relative_strength_score": "unknown_or_not_supported", "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": "unknown_or_not_supported", "valuation_repricing_score": "unknown_or_not_supported", "execution_risk_score": 95, "legal_or_contract_risk_score": 95, "dilution_cb_risk_score": 80, "accounting_trust_risk_score": 85}, "weighted_score_before": 93, "stage_label_before": "4C-narrative-only", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": "unknown_or_not_supported", "relative_strength_score": "unknown_or_not_supported", "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": "unknown_or_not_supported", "valuation_repricing_score": "unknown_or_not_supported", "execution_risk_score": 95, "legal_or_contract_risk_score": 95, "dilution_cb_risk_score": 80, "accounting_trust_risk_score": 85}, "weighted_score_after": 93, "stage_label_after": "4C-narrative-only", "changed_components": ["blocked_from_weight_calibration"], "component_delta_explanation": "True liquidity-break narrative but contaminated forward window; record as narrative only.", "MFE_90D_pct": "contaminated_or_unavailable", "MAE_90D_pct": "contaminated_or_unavailable", "score_return_alignment_label": "narrative_only", "current_profile_verdict": "current_profile_data_insufficient"}
{"row_type": "residual_contribution", "round": "R10", "loop": "12", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "same_archetype_new_symbol_count": 5, "same_archetype_new_trigger_family_count": 4, "new_canonical_archetype_count": 0, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "price_only_blowoff_blocks_positive_stage", "stage3_green_revision_min"], "residual_error_types_found": ["broad_pf_panic_false_positive", "quality_event_hard_4c_overrouting", "corporate_action_window_blocked_true_4c"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
{"row_type": "narrative_only", "case_id": "R10L12_C30_009410_TAEYOUNG_WORKOUT_20231228", "symbol": "009410", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "reason": "true issuer-specific liquidity-break evidence, but forward 180D is blocked by stock-web profile corporate_action_candidate_date 2024-10-31", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
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
next_round = R11_C31_POLICY_SUBSIDY_LEGISLATION_EVENT
next_priority = find policy-event counterexamples where legislation headlines did not become EPS/revision evidence
carry_forward = C30 needs more samples from 금호건설, 신세계건설-like credit stress, and post-workout clean windows when stock-web corporate action no longer blocks calibration
```

## 28. Source Notes

- Prompt basis: E2R Historical Calibration Prompt v12 supplied in-session.
- Price atlas manifest: `Songdaiki/stock-web/atlas/manifest.json`, max_date `2026-02-20`.
- Schema: `Songdaiki/stock-web/atlas/schema.json`, calibration basis `tradable_raw`.
- Stock profiles used: `006360`, `294870`, `047040`, `375500`, `009410`.
- Representative tradable shards used:
  - `atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/047/047040/2022.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/047/047040/2023.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/375/375500/2023.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/009/009410/2024.csv`

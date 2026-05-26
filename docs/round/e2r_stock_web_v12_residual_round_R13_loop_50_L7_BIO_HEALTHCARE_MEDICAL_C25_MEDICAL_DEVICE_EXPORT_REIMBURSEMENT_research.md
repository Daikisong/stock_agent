# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R13
loop = 50
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id = AESTHETIC_DEVICE_EXPORT_CONSUMABLE_ROUTE | BODY_COMPOSITION_DEVICE_GLOBAL_CHANNEL | DENTAL_DIGITAL_EXPORT_EXECUTION_RISK | MEDICAL_AI_REIMBURSEMENT_PREMIUM_GUARD
selection_mode = auto_coverage_gap_fill
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This MD is not a live stock screen and not a `stock_agent` patch. It is a historical residual calibration research file for L7/C25. The loop was auto-selected as a C25 follow-up because an earlier C25 file already covered Classys/Dentium/JLK/Lunit, while same-archetype new-symbol coverage remained useful for aesthetic device export, body-composition device channels, dental digital export execution risk, and medical-AI reimbursement premium guards.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference

stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The residual question is narrow: C25 should not treat all “medical device” evidence equally. Export-installed-base devices and consumable routes behave differently from medical-AI reimbursement optionality. In practice, the former can justify earlier Stage2/Yellow promotion if margin and channel evidence exist; the latter needs a stronger conversion gate because the price path can be a sharp event premium with severe MAE.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R13
loop = 50
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
loop_objective = auto_coverage_gap_fill, sector_specific_rule_discovery, canonical_archetype_compression, counterexample_mining, 4B_non_price_requirement_stress_test, 4C_thesis_break_timing_test
```

C25 is the medical-device export/reimbursement archetype. This loop keeps the canonical archetype the same but changes the symbol set and trigger families.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed artifact-style duplicate search was limited to the prescribed research-artifact intent. No `stock_agent` source code was opened. Local duplicate avoidance also checked the earlier C25 row set and avoided:

```text
avoided_prior_symbols = 214150_CLASSYS, 145720_DENTIUM, 322510_JLK, 328130_LUNIT
new_symbols = 335890_BIOL, 041830_INBODY, 228670_RAY, 338220_VUNO
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = avoided
same_symbol_same_entry_group_research = avoided
new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest was checked directly in `Songdaiki/stock-web`.

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
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Price-basis caveat:

```text
price_data_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

## 5. Historical Eligibility Gate

All representative rows pass the 180D historical eligibility gate.

```text
entry_date_exists_in_tradable_shard = true
forward_180D_available_by_manifest_max_date = true
MFE_MAE_30D_90D_180D_computed = true
corporate_action_contaminated_180D_window = false
calibration_usable = true
```

Symbol profile checks:

- 335890 비올: row_status_counts tradable_ohlcv=1399, non_tradable_zero_volume=79; corporate_action_candidate_dates=[2020-11-26], outside calibration window; latest row 2025-12-09 and status_inferred=inactive_or_delisted_like, but 2023~2024 forward windows are available and clean.
- 041830 인바디: row_status_counts tradable_ohlcv=6209; corporate_action_candidate_dates=[2010-04-23, 2010-05-18], outside calibration window; 2023 forward window is clean.
- 228670 레이: row_status_counts tradable_ohlcv=1603; corporate_action_candidate_dates=[2021-06-03, 2021-06-23], outside calibration window; 2023 forward window is clean.
- 338220 뷰노: row_status_counts tradable_ohlcv=1221; corporate_action_candidate_count=0; 2023~2024 forward windows are clean.

## 6. Canonical Archetype Compression Map

```text
AESTHETIC_DEVICE_EXPORT_CONSUMABLE_ROUTE -> C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
BODY_COMPOSITION_DEVICE_GLOBAL_CHANNEL -> C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
DENTAL_DIGITAL_EXPORT_EXECUTION_RISK -> C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
MEDICAL_AI_REIMBURSEMENT_PREMIUM_GUARD -> C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
```

The compression point is that these are all C25, but their score behavior is not identical. The research proposal is not to split production stages now; it is to store a shadow subroute tag so later batch implementation can weight export/installed-base device routes differently from AI reimbursement option premium.

## 7. Case Selection Summary

|case_id|symbol|company|case_type|role|best_trigger|current_profile_verdict|
|---|---|---|---|---|---|---|
|R13L50_C25_335890_BIOL_2023_AESTHETIC_EXPORT_CONSUMABLE_SUCCESS|335890|비올|structural_success|positive|R13L50_C25_335890_T1_STAGE2|current_profile_too_late|
|R13L50_C25_041830_INBODY_2023_GLOBAL_DEVICE_CHANNEL_MODERATE_SUCCESS|041830|인바디|stage2_promote_candidate|positive|R13L50_C25_041830_T1_STAGE2|current_profile_correct|
|R13L50_C25_228670_RAY_2023_DENTAL_DIGITAL_EXPORT_FALSE_POSITIVE|228670|레이|failed_rerating|counterexample|R13L50_C25_228670_T1_STAGE2|current_profile_false_positive|
|R13L50_C25_338220_VUNO_2023_AI_REIMBURSEMENT_PREMIUM_HIGH_MAE|338220|뷰노|high_mae_success|counterexample|R13L50_C25_338220_T1_STAGE2|current_profile_false_positive|


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 2
4C_case_count = 2
calibration_usable_case_count = 4
```

Positive rows are not generic “devices went up.” They have tangible device/export/channel evidence. Counterexample rows isolate where the same C25 headline can mislead: dental digital export without durable execution/margin conversion, and medical-AI reimbursement optionality without reimbursed revenue and margin bridge.

## 9. Evidence Source Map

|symbol|trigger_date|evidence bucket|stage2 fields|stage3 fields|4B/4C fields|
|---|---|---|---|---|---|
|335890|2023-05-02|Aesthetic RF/microneedle device export visibility and consumable/installed-base path were visible before the later revision-confirmed device rerating. This is not price-only; it is a device + recurring consumable route.|capacity_or_volume_route, customer_or_order_quality, relative_strength, early_revision_signal|financial_visibility, margin_bridge, multiple_public_sources||
|041830|2023-02-10|Medical/body-composition device channel demand created a moderate but clean rerating path. Unlike AI-reimbursement premium, this had a tangible device/export channel route, but the slope was not explosive enough to justify Green without confirmed revision.|customer_or_order_quality, capacity_or_volume_route, early_revision_signal|financial_visibility, multiple_public_sources||
|228670|2023-03-17|Dental digital-device export/reopening narrative produced a tradable move, but execution/margin durability did not hold. The early device-export thesis needed a stronger margin/order conversion gate, because later drawdown erased the initial MFE.|customer_or_order_quality, capacity_or_volume_route, relative_strength|multiple_public_sources|margin_or_backlog_slowdown, valuation_blowoff, positioning_overheat, thesis_evidence_broken|
|338220|2023-06-20|AI medical-device reimbursement optionality created a very large price move, but the path had severe drawdown and a valuation/event-premium character. The row is useful as a counterexample guard: reimbursement code alone should not be scored like an export installed-base device with margin conversion.|policy_or_regulatory_optionality, relative_strength, customer_or_order_quality|multiple_public_sources|valuation_blowoff, positioning_overheat, capital_raise_or_overhang, thesis_evidence_broken|


## 10. Price Data Source Map

|symbol|profile_path|price_shard_path|entry_date|entry_price|corporate_action_window_status|
|---|---|---|---|---|---|
|335890|atlas/symbol_profiles/335/335890.json|atlas/ohlcv_tradable_by_symbol_year/335/335890/2023.csv|2023-05-02|5910|clean_180D_window|
|041830|atlas/symbol_profiles/041/041830.json|atlas/ohlcv_tradable_by_symbol_year/041/041830/2023.csv|2023-02-10|24200|clean_180D_window|
|228670|atlas/symbol_profiles/228/228670.json|atlas/ohlcv_tradable_by_symbol_year/228/228670/2023.csv|2023-03-17|30950|clean_180D_window|
|338220|atlas/symbol_profiles/338/338220.json|atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv|2023-06-20|33600|clean_180D_window|


## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|company|trigger_type|trigger_date|entry_date|entry_price|MFE_90D|MAE_90D|MFE_180D|MAE_180D|outcome|current_profile_verdict|dedupe_for_aggregate|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R13L50_C25_335890_T1_STAGE2|335890|비올|Stage2-Actionable|2023-05-02|2023-05-02|5910|50.93|-3.89|69.2|-3.89|export_consumable_route_success|current_profile_too_late|True|
|R13L50_C25_041830_T1_STAGE2|041830|인바디|Stage2-Actionable|2023-02-10|2023-02-10|24200|34.5|-7.44|34.5|-7.44|moderate_device_channel_success|current_profile_correct|True|
|R13L50_C25_228670_T1_STAGE2|228670|레이|Stage2-Actionable|2023-03-17|2023-03-17|30950|36.19|-7.43|36.19|-37.32|device_export_narrative_failed_to_convert|current_profile_false_positive|True|
|R13L50_C25_338220_T1_STAGE2|338220|뷰노|Stage2-Actionable|2023-06-20|2023-06-20|33600|106.85|-28.87|106.85|-28.87|AI_reimbursement_premium_high_MAE_success|current_profile_false_positive|True|
|R13L50_C25_338220_T2_4B|338220|뷰노|Stage4B|2023-09-05|2023-09-05|64200|8.26|-62.77|8.26|-62.77|4B_overlay_success|current_profile_4B_too_late|False|
|R13L50_C25_228670_T2_4B|228670|레이|Stage4B|2023-07-20|2023-07-20|37700|10.48|-48.54|10.48|-48.54|4B_overlay_success|current_profile_4B_too_late|False|


## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative trigger metrics

|symbol|entry|entry_price|MFE30|MAE30|MFE90|MAE90|MFE180|MAE180|MFE1Y|MAE1Y|peak_date|peak_price|drawdown_after_peak|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|335890|2023-05-02|5910|31.64|-3.89|50.93|-3.89|69.2|-3.89|103.55|-3.89|2024-04-01|12030|-22.61|
|041830|2023-02-10|24200|25.83|-7.44|34.5|-7.44|34.5|-7.44|34.5|-7.44|2023-04-11|32550|-19.36|
|228670|2023-03-17|30950|27.63|-7.43|36.19|-7.43|36.19|-37.32|36.19|-37.32|2023-06-15|42150|-53.97|
|338220|2023-06-20|33600|35.12|-19.49|106.85|-28.87|106.85|-28.87|106.85|-28.87|2023-09-07|69500|-65.61|


### 12.2 Raw OHLC audit rows used

```text
- `335890/2023`: entry row `2023-05-02,5270,5940,5270,5910`; 30D high `2023-06-13 h=7780`; 90D high `2023-08-08 h=8920`; 180D high `2024-01-09 h=10000`; 180D low `2023-05-08 l=5680`.
- `041830/2023`: entry row `2023-02-10,22900,28850,22400,24200`; 30D high `2023-03-06 h=30450`; 90D/180D high `2023-04-11 h=32550`; 180D low `2023-02-10 l=22400`.
- `228670/2023`: entry row `2023-03-17,29450,31050,28650,30950`; 90D/180D high `2023-06-15 h=42150`; 180D low `2023-10-31 l=19400`; 4B overlay row `2023-07-20,39500,41650,37550,37700`.
- `338220/2023`: entry row `2023-06-20,28900,34900,28550,33600`; 30D high `2023-07-19 h=45400`; 90D/180D high `2023-09-07 h=69500`; 180D low `2023-10-24 l=23900`; 4B overlay row `2023-09-05,54400,68200,53800,64200`.
```

## 13. Current Calibrated Profile Stress Test

1. Current profile likely keeps BIOL and InBody from premature Green, but it can still be too late in BIOL because the export/consumable route was already visible before full revision confirmation.
2. Current profile can still over-score Ray if dental export narrative and relative strength are treated as enough evidence without execution/margin conversion.
3. Current profile can still over-score VUNO if reimbursement optionality and relative strength are scored like durable device installed-base economics.
4. Stage2 actionable bonus is useful for BIOL/InBody, but too generous for VUNO unless an AI reimbursement premium guard is present.
5. Yellow threshold 75 remains broadly acceptable, but C25 needs subroute-specific evidence caps.
6. Green threshold 87 / revision 55 should remain strict for AI reimbursement and dental digital export narratives.
7. Price-only blowoff guard is kept and strengthened by VUNO/Ray.
8. Full 4B non-price requirement is kept and strengthened: VUNO’s valuation/positioning/capital-overhang evidence and Ray’s execution/margin slowdown evidence matter more than price alone.
9. Hard 4C routing is kept and strengthened when thesis conversion breaks.

## 14. Stage2 / Yellow / Green Comparison

```text
BIOL: Stage2/Yellow entry at 5910 captured the move from export/consumable evidence. A later Green-like confirmation near the 2024 rerating would have captured less of the total cycle. green_lateness_ratio_proxy = 0.42.
InBody: Stage2 entry was adequate but should not jump to Green; MFE was moderate and MAE controlled.
Ray: Stage2 looked plausible but later 180D MAE of -37.32% argues for a stronger execution/margin conversion guard.
VUNO: Stage2 captured MFE, but the row is not a clean positive calibration row because 90D/180D MAE was -28.87% and post-peak drawdown was -65.61%.
```

## 15. 4B Local vs Full-window Timing Audit

|symbol|4B trigger|entry_price|local_peak_proximity|full_window_peak_proximity|evidence_type|timing_verdict|
|---|---|---|---|---|---|---|
|338220|R13L50_C25_338220_T2_4B|64200|0.85|0.85|valuation_blowoff, positioning_overheat, capital_raise_or_overhang|good_full_window_4B_timing|
|228670|R13L50_C25_228670_T2_4B|37700|0.6|0.6|margin_or_backlog_slowdown, valuation_blowoff|good_4B_if_non_price_slowdown_confirmed|


Key result: the 4B rows only become useful when non-price evidence is present. VUNO’s price peak alone is not a Stage3-positive reason; it is a valuation/positioning 4B overlay. Ray’s peak proximity is not enough by itself; the reason to apply 4B is the execution/margin slowdown overlay.

## 16. 4C Protection Audit

```text
VUNO: hard_4c_success label; after peak 69500, the path reached 23900 inside the observed calibration window, implying a -65.61% drawdown. Earlier thesis-break/overheat routing would have protected capital.
Ray: hard_4c_success label; after peak 42150, the path reached 19400, implying a -53.97% drawdown. The C25 export thesis broke when execution/margin conversion did not follow the narrative.
BIOL: no hard 4C row; positive device/consumable thesis remained intact in the observed window.
InBody: no hard 4C row; moderate device channel success rather than thesis break.
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
sector_specific_rule_candidate = true
axis = L7_C25_device_export_installed_base_bridge_vs_AI_reimbursement_premium_guard
```

Candidate rule:

```text
For L7/C25, Stage2/Yellow promotion may be nudged up only when the evidence contains at least one tangible conversion bridge:
- export-channel demand with repeat/installed-base logic,
- recurring consumable/cartridge economics,
- reimbursed product usage that is visible in revenue,
- or margin bridge evidence.

If the evidence is mainly medical-AI reimbursement optionality, conference/approval headline, or relative strength, cap the positive-stage score unless revenue conversion and margin bridge are also present.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_rule_candidate = true
new_axis_proposed = C25_subroute_conversion_bridge
```

Canonical C25 should store subroute tags:

```text
C25_export_installed_base_consumable = positive bridge candidate
C25_body_composition_channel = moderate positive, Yellow cap unless revision confirms
C25_dental_digital_export_execution = execution/margin guard required
C25_medical_AI_reimbursement = event-premium guard required
```

## 19. Before / After Backtest Comparison

|profile_id|scope|eligible|avg_MFE90|avg_MAE90|avg_MFE180|avg_MAE180|false_positive_rate|missed_structural|verdict|
|---|---|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|current_proxy|4|57.12|-11.91|61.69|-19.38|0.5|1|mixed|
|P0b_e2r_2_0_baseline_reference|rollback_reference|4|57.12|-11.91|61.69|-19.38|0.5|2|weaker_than_P0|
|P1_sector_specific_candidate_profile|L7 sector-specific|4|57.12|-11.91|61.69|-19.38|0.25|0|improved|
|P2_canonical_archetype_candidate_profile|C25 canonical-archetype-specific|4|57.12|-11.91|61.69|-19.38|0.25|0|best_candidate|
|P3_counterexample_guard_profile|guard|4|57.12|-11.91|61.69|-19.38|0.25|1|better_risk_control|


## 20. Score-Return Alignment Matrix

|case|symbol|P0 score/stage|P2 score/stage|MFE90|MAE90|alignment|
|---|---|---|---|---|---|---|
|R13L50_C25_335890_BIOL_2023_AESTHETIC_EXPORT_CONSUMABLE_SUCCESS|335890|78 / Stage3-Yellow|84 / Stage3-Yellow|50.93|-3.89|aligned|
|R13L50_C25_041830_INBODY_2023_GLOBAL_DEVICE_CHANNEL_MODERATE_SUCCESS|041830|73 / Stage2-Actionable|77 / Stage3-Yellow|34.5|-7.44|aligned|
|R13L50_C25_228670_RAY_2023_DENTAL_DIGITAL_EXPORT_FALSE_POSITIVE|228670|76 / Stage3-Yellow|61 / Stage2-watch|36.19|-7.43|guard_needed|
|R13L50_C25_338220_VUNO_2023_AI_REIMBURSEMENT_PREMIUM_HIGH_MAE|338220|77 / Stage3-Yellow|60 / Stage2-watch|106.85|-28.87|guard_needed|


## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L7_BIO_HEALTHCARE_MEDICAL|C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|AESTHETIC_DEVICE_EXPORT_CONSUMABLE_ROUTE | BODY_COMPOSITION_DEVICE_GLOBAL_CHANNEL | DENTAL_DIGITAL_EXPORT_EXECUTION_RISK | MEDICAL_AI_REIMBURSEMENT_PREMIUM_GUARD|2|2|2|2|4|0|6|4|3|True|True|C25 now has additional same-archetype new-symbol coverage beyond Classys/Dentium/JLK/Lunit; still useful to add global medical-device reimbursement examples outside Korea later.|


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage3_green_revision_min, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: AI_reimbursement_event_premium_overpromotion, dental_digital_export_execution_false_positive, late_positive_for_aesthetic_export_consumable_route
new_axis_proposed: C25_subroute_conversion_bridge, C25_AI_reimbursement_event_premium_guard
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
diversity_score_summary: avg=22.0; four new C25 symbols and four new trigger families; no same symbol/date/entry reuse
auto_selected_coverage_gap: C25 follow-up after earlier Classys/Dentium/JLK/Lunit set
do_not_propose_new_weight_delta: false
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest max_date and price basis.
- Symbol profile corporate-action windows.
- Representative trigger OHLC entry price, MFE/MAE 30D/90D/180D.
- Positive/counterexample balance.
- C25-specific conversion-bridge vs event-premium distinction.
```

Not validated:

```text
- No stock_agent source code was opened.
- No production scoring patch was written.
- No live/current stock discovery was performed.
- No broker/API/auto-trading action was performed.
- Evidence-source details are represented as historical filing/report clusters; this MD is for calibration, not a new investment report.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C25_export_installed_base_consumable_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"Positive rows with device/export/consumable route had clean MFE and controlled MAE.","BIOL/InBody positive rows improve positive selection without relying on price-only evidence.","R13L50_C25_335890_T1_STAGE2|R13L50_C25_041830_T1_STAGE2",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C25_AI_reimbursement_event_premium_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"AI reimbursement optionality produced large MFE but high MAE/drawdown; should not equal installed-base device evidence.","VUNO row remains tradable but no positive weight promotion without revenue/margin conversion.","R13L50_C25_338220_T1_STAGE2|R13L50_C25_338220_T2_4B",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C25_execution_margin_slowdown_4B_overlay,sector_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"Dental/device export narratives can fail when execution/margin durability is missing.","Ray 4B overlay would have protected from the full-window drawdown.","R13L50_C25_228670_T1_STAGE2|R13L50_C25_228670_T2_4B",4,4,2,medium,sector_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R13L50_C25_335890_BIOL_2023_AESTHETIC_EXPORT_CONSUMABLE_SUCCESS","symbol":"335890","company_name":"비올","round":"R13","loop":"50","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_CONSUMABLE_ROUTE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R13L50_C25_335890_T1_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Aesthetic RF/microneedle device export visibility and consumable/installed-base path were visible before the later revision-confirmed device rerating. This is not price-only; it is a device + recurring consumable route."}
{"row_type":"case","case_id":"R13L50_C25_041830_INBODY_2023_GLOBAL_DEVICE_CHANNEL_MODERATE_SUCCESS","symbol":"041830","company_name":"인바디","round":"R13","loop":"50","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"BODY_COMPOSITION_DEVICE_GLOBAL_CHANNEL","case_type":"stage2_promote_candidate","positive_or_counterexample":"positive","best_trigger":"R13L50_C25_041830_T1_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Medical/body-composition device channel demand created a moderate but clean rerating path. Unlike AI-reimbursement premium, this had a tangible device/export channel route, but the slope was not explosive enough to justify Green without confirmed revision."}
{"row_type":"case","case_id":"R13L50_C25_228670_RAY_2023_DENTAL_DIGITAL_EXPORT_FALSE_POSITIVE","symbol":"228670","company_name":"레이","round":"R13","loop":"50","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_DIGITAL_EXPORT_EXECUTION_RISK","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R13L50_C25_228670_T1_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"overpromoted_without_conversion","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Dental digital-device export/reopening narrative produced a tradable move, but execution/margin durability did not hold. The early device-export thesis needed a stronger margin/order conversion gate, because later drawdown erased the initial MFE."}
{"row_type":"case","case_id":"R13L50_C25_338220_VUNO_2023_AI_REIMBURSEMENT_PREMIUM_HIGH_MAE","symbol":"338220","company_name":"뷰노","round":"R13","loop":"50","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_AI_REIMBURSEMENT_PREMIUM_GUARD","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"R13L50_C25_338220_T1_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"overpromoted_without_conversion","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"AI medical-device reimbursement optionality created a very large price move, but the path had severe drawdown and a valuation/event-premium character. The row is useful as a counterexample guard: reimbursement code alone should not be scored like an export installed-base device with margin conversion."}
{"row_type":"trigger","trigger_id":"R13L50_C25_335890_T1_STAGE2","case_id":"R13L50_C25_335890_BIOL_2023_AESTHETIC_EXPORT_CONSUMABLE_SUCCESS","symbol":"335890","company_name":"비올","round":"R13","loop":"50","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_CONSUMABLE_ROUTE","sector":"바이오·헬스케어·의료기기","primary_archetype":"medical_device_export_reimbursement","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-02","evidence_available_at_that_date":"Aesthetic RF/microneedle device export visibility and consumable/installed-base path were visible before the later revision-confirmed device rerating. This is not price-only; it is a device + recurring consumable route.","evidence_source":"historical public filing/report cluster; stock-web OHLC rows checked in cited shard/profile paths","stage2_evidence_fields":["capacity_or_volume_route","customer_or_order_quality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","margin_bridge","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/335/335890/2023.csv","profile_path":"atlas/symbol_profiles/335/335890.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-05-02","entry_price":5910,"MFE_30D_pct":31.64,"MFE_90D_pct":50.93,"MFE_180D_pct":69.2,"MFE_1Y_pct":103.55,"MFE_2Y_pct":null,"MAE_30D_pct":-3.89,"MAE_90D_pct":-3.89,"MAE_180D_pct":-3.89,"MAE_1Y_pct":-3.89,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-01","peak_price":12030,"drawdown_after_peak_pct":-22.61,"green_lateness_ratio":0.42,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"export_consumable_route_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_335890_2023_05_02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L50_C25_041830_T1_STAGE2","case_id":"R13L50_C25_041830_INBODY_2023_GLOBAL_DEVICE_CHANNEL_MODERATE_SUCCESS","symbol":"041830","company_name":"인바디","round":"R13","loop":"50","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"BODY_COMPOSITION_DEVICE_GLOBAL_CHANNEL","sector":"바이오·헬스케어·의료기기","primary_archetype":"medical_device_export_reimbursement","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-10","evidence_available_at_that_date":"Medical/body-composition device channel demand created a moderate but clean rerating path. Unlike AI-reimbursement premium, this had a tangible device/export channel route, but the slope was not explosive enough to justify Green without confirmed revision.","evidence_source":"historical public filing/report cluster; stock-web OHLC rows checked in cited shard/profile paths","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/041/041830/2023.csv","profile_path":"atlas/symbol_profiles/041/041830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-02-10","entry_price":24200,"MFE_30D_pct":25.83,"MFE_90D_pct":34.5,"MFE_180D_pct":34.5,"MFE_1Y_pct":34.5,"MFE_2Y_pct":null,"MAE_30D_pct":-7.44,"MAE_90D_pct":-7.44,"MAE_180D_pct":-7.44,"MAE_1Y_pct":-7.44,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-11","peak_price":32550,"drawdown_after_peak_pct":-19.36,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"moderate_device_channel_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_041830_2023_02_10","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L50_C25_228670_T1_STAGE2","case_id":"R13L50_C25_228670_RAY_2023_DENTAL_DIGITAL_EXPORT_FALSE_POSITIVE","symbol":"228670","company_name":"레이","round":"R13","loop":"50","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_DIGITAL_EXPORT_EXECUTION_RISK","sector":"바이오·헬스케어·의료기기","primary_archetype":"medical_device_export_reimbursement","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-03-17","evidence_available_at_that_date":"Dental digital-device export/reopening narrative produced a tradable move, but execution/margin durability did not hold. The early device-export thesis needed a stronger margin/order conversion gate, because later drawdown erased the initial MFE.","evidence_source":"historical public filing/report cluster; stock-web OHLC rows checked in cited shard/profile paths","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/228/228670/2023.csv","profile_path":"atlas/symbol_profiles/228/228670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-03-17","entry_price":30950,"MFE_30D_pct":27.63,"MFE_90D_pct":36.19,"MFE_180D_pct":36.19,"MFE_1Y_pct":36.19,"MFE_2Y_pct":null,"MAE_30D_pct":-7.43,"MAE_90D_pct":-7.43,"MAE_180D_pct":-37.32,"MAE_1Y_pct":-37.32,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-15","peak_price":42150,"drawdown_after_peak_pct":-53.97,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.6,"four_b_full_window_peak_proximity":0.6,"four_b_timing_verdict":"good_full_window_4B_timing_if_margin_slowdown_confirmed","four_b_evidence_type":["margin_or_backlog_slowdown","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"device_export_narrative_failed_to_convert","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_228670_2023_03_17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L50_C25_338220_T1_STAGE2","case_id":"R13L50_C25_338220_VUNO_2023_AI_REIMBURSEMENT_PREMIUM_HIGH_MAE","symbol":"338220","company_name":"뷰노","round":"R13","loop":"50","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_AI_REIMBURSEMENT_PREMIUM_GUARD","sector":"바이오·헬스케어·의료기기","primary_archetype":"medical_device_export_reimbursement","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-06-20","evidence_available_at_that_date":"AI medical-device reimbursement optionality created a very large price move, but the path had severe drawdown and a valuation/event-premium character. The row is useful as a counterexample guard: reimbursement code alone should not be scored like an export installed-base device with margin conversion.","evidence_source":"historical public filing/report cluster; stock-web OHLC rows checked in cited shard/profile paths","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","customer_or_order_quality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","capital_raise_or_overhang"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv","profile_path":"atlas/symbol_profiles/338/338220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-06-20","entry_price":33600,"MFE_30D_pct":35.12,"MFE_90D_pct":106.85,"MFE_180D_pct":106.85,"MFE_1Y_pct":106.85,"MFE_2Y_pct":null,"MAE_30D_pct":-19.49,"MAE_90D_pct":-28.87,"MAE_180D_pct":-28.87,"MAE_1Y_pct":-28.87,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-09-07","peak_price":69500,"drawdown_after_peak_pct":-65.61,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.85,"four_b_full_window_peak_proximity":0.85,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","capital_raise_or_overhang"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"AI_reimbursement_premium_high_MAE_success","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_338220_2023_06_20","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L50_C25_338220_T2_4B","case_id":"R13L50_C25_338220_VUNO_2023_AI_REIMBURSEMENT_PREMIUM_HIGH_MAE","symbol":"338220","company_name":"뷰노","round":"R13","loop":"50","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_AI_REIMBURSEMENT_PREMIUM_GUARD","sector":"바이오·헬스케어·의료기기","primary_archetype":"medical_device_export_reimbursement","loop_objective":"4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage4B","trigger_date":"2023-09-05","evidence_available_at_that_date":"After a reimbursement/medical-AI premium run, valuation/positioning overheat became a better 4B overlay than a new positive-stage confirmation.","evidence_source":"historical public filing/report cluster; stock-web OHLC rows checked in cited shard/profile paths","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","capital_raise_or_overhang"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv","profile_path":"atlas/symbol_profiles/338/338220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-09-05","entry_price":64200,"MFE_30D_pct":8.26,"MFE_90D_pct":8.26,"MFE_180D_pct":8.26,"MFE_1Y_pct":8.26,"MFE_2Y_pct":null,"MAE_30D_pct":-42.83,"MAE_90D_pct":-62.77,"MAE_180D_pct":-62.77,"MAE_1Y_pct":-62.77,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-09-07","peak_price":69500,"drawdown_after_peak_pct":-65.61,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.85,"four_b_full_window_peak_proximity":0.85,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","capital_raise_or_overhang"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_338220_2023_09_05","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_symbol_new_4B_overlay","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L50_C25_228670_T2_4B","case_id":"R13L50_C25_228670_RAY_2023_DENTAL_DIGITAL_EXPORT_FALSE_POSITIVE","symbol":"228670","company_name":"레이","round":"R13","loop":"50","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_DIGITAL_EXPORT_EXECUTION_RISK","sector":"바이오·헬스케어·의료기기","primary_archetype":"medical_device_export_reimbursement","loop_objective":"4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage4B","trigger_date":"2023-07-20","evidence_available_at_that_date":"Execution/margin-risk overlay after the dental-device export move. This row is overlay-only, not a fresh positive entry.","evidence_source":"historical public filing/report cluster; stock-web OHLC rows checked in cited shard/profile paths","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","valuation_blowoff"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/228/228670/2023.csv","profile_path":"atlas/symbol_profiles/228/228670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-20","entry_price":37700,"MFE_30D_pct":10.48,"MFE_90D_pct":10.48,"MFE_180D_pct":10.48,"MFE_1Y_pct":10.48,"MFE_2Y_pct":null,"MAE_30D_pct":-29.58,"MAE_90D_pct":-48.54,"MAE_180D_pct":-48.54,"MAE_1Y_pct":-48.54,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-20","peak_price":41650,"drawdown_after_peak_pct":-53.42,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.6,"four_b_full_window_peak_proximity":0.6,"four_b_timing_verdict":"good_4B_if_non_price_slowdown_confirmed","four_b_evidence_type":["margin_or_backlog_slowdown","valuation_blowoff"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G_228670_2023_07_20","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_symbol_new_4B_overlay","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L50_C25_335890_BIOL_2023_AESTHETIC_EXPORT_CONSUMABLE_SUCCESS","trigger_id":"R13L50_C25_335890_T1_STAGE2","symbol":"335890","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":50,"margin_bridge_score":62,"revision_score":58,"relative_strength_score":64,"customer_quality_score":68,"policy_or_regulatory_score":0,"valuation_repricing_score":54,"execution_risk_score":24,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":62,"margin_bridge_score":72,"revision_score":64,"relative_strength_score":64,"customer_quality_score":76,"policy_or_regulatory_score":0,"valuation_repricing_score":58,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"installed-base consumable export route earns a C25 archetype boost without forcing Green","MFE_90D_pct":50.93,"MAE_90D_pct":-3.89,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L50_C25_041830_INBODY_2023_GLOBAL_DEVICE_CHANNEL_MODERATE_SUCCESS","trigger_id":"R13L50_C25_041830_T1_STAGE2","symbol":"041830","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":38,"margin_bridge_score":55,"revision_score":48,"relative_strength_score":58,"customer_quality_score":62,"policy_or_regulatory_score":0,"valuation_repricing_score":42,"execution_risk_score":22,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":45,"margin_bridge_score":60,"revision_score":52,"relative_strength_score":58,"customer_quality_score":66,"policy_or_regulatory_score":0,"valuation_repricing_score":44,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":77,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"moderate global device channel supports Yellow but not Green","MFE_90D_pct":34.5,"MAE_90D_pct":-7.44,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L50_C25_228670_RAY_2023_DENTAL_DIGITAL_EXPORT_FALSE_POSITIVE","trigger_id":"R13L50_C25_228670_T1_STAGE2","symbol":"228670","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":44,"margin_bridge_score":42,"revision_score":44,"relative_strength_score":60,"customer_quality_score":60,"policy_or_regulatory_score":0,"valuation_repricing_score":55,"execution_risk_score":42,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":34,"margin_bridge_score":28,"revision_score":34,"relative_strength_score":52,"customer_quality_score":48,"policy_or_regulatory_score":0,"valuation_repricing_score":43,"execution_risk_score":68,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage2-watch","changed_components":["customer_quality_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"export narrative loses score when order conversion and margin durability are not confirmed","MFE_90D_pct":36.19,"MAE_90D_pct":-7.43,"score_return_alignment_label":"guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L50_C25_338220_VUNO_2023_AI_REIMBURSEMENT_PREMIUM_HIGH_MAE","trigger_id":"R13L50_C25_338220_T1_STAGE2","symbol":"338220","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":15,"revision_score":22,"relative_strength_score":86,"customer_quality_score":38,"policy_or_regulatory_score":78,"valuation_repricing_score":70,"execution_risk_score":58,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":12,"margin_bridge_score":10,"revision_score":16,"relative_strength_score":70,"customer_quality_score":30,"policy_or_regulatory_score":62,"valuation_repricing_score":45,"execution_risk_score":80,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":20,"accounting_trust_risk_score":0},"weighted_score_after":60,"stage_label_after":"Stage2-watch","changed_components":["customer_quality_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"medical-AI reimbursement optionality is capped unless reimbursed revenue and margin bridge convert","MFE_90D_pct":106.85,"MAE_90D_pct":-28.87,"score_return_alignment_label":"guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R13","loop":"50","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage3_green_revision_min","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["AI_reimbursement_event_premium_overpromotion","dental_digital_export_execution_false_positive","late_positive_for_aesthetic_export_consumable_route"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"diversity_score_summary":"avg=22.0; four new C25 symbols and four new trigger families; no same symbol/date/entry reuse","auto_selected_coverage_gap":"C25 follow-up after earlier Classys/Dentium/JLK/Lunit set; add BIOL/InBody/Ray/VUNO same-archetype new-symbol coverage"}
```

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C25_export_installed_base_consumable_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"Positive rows with device/export/consumable route had clean MFE and controlled MAE.","BIOL/InBody positive rows improve positive selection without relying on price-only evidence.","R13L50_C25_335890_T1_STAGE2|R13L50_C25_041830_T1_STAGE2",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C25_AI_reimbursement_event_premium_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"AI reimbursement optionality produced large MFE but high MAE/drawdown; should not equal installed-base device evidence.","VUNO row remains tradable but no positive weight promotion without revenue/margin conversion.","R13L50_C25_338220_T1_STAGE2|R13L50_C25_338220_T2_4B",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C25_execution_margin_slowdown_4B_overlay,sector_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"Dental/device export narratives can fail when execution/margin durability is missing.","Ray 4B overlay would have protected from the full-window drawdown.","R13L50_C25_228670_T1_STAGE2|R13L50_C25_228670_T2_4B",4,4,2,medium,sector_shadow_only,"not production; post-calibrated residual"
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
next_round = R13_loop_51
recommended_large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
recommended_canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
reason = continue residual coverage outside already-repeated L7 medical-device/trial clusters; look for positive/counterexample balance in recurring software/security contract retention.
```

## 28. Source Notes

```text
stock_web_manifest = atlas/manifest.json
stock_web_schema = atlas/schema.json
stock_web_manifest_max_date = 2026-02-20
stock_web_price_basis = tradable_raw
stock_web_price_adjustment_status = raw_unadjusted_marcap
profile_paths = atlas/symbol_profiles/335/335890.json | atlas/symbol_profiles/041/041830.json | atlas/symbol_profiles/228/228670.json | atlas/symbol_profiles/338/338220.json
price_shards = atlas/ohlcv_tradable_by_symbol_year/335/335890/2023.csv | atlas/ohlcv_tradable_by_symbol_year/335/335890/2024.csv | atlas/ohlcv_tradable_by_symbol_year/041/041830/2023.csv | atlas/ohlcv_tradable_by_symbol_year/228/228670/2023.csv | atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv | atlas/ohlcv_tradable_by_symbol_year/338/338220/2024.csv
stock_agent_code_accessed = false
stock_agent_code_patch_written = false
production_scoring_changed = false
```

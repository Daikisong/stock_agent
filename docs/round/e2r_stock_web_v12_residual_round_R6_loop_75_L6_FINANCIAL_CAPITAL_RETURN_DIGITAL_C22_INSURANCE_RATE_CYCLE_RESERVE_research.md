# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
scheduled_round: R6
scheduled_loop: 75
completed_round: R6
completed_loop: 75
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: LIFE_REINSURANCE_EVENT_PREMIUM_VS_RESERVE_QUALITY
output_file: e2r_stock_web_v12_residual_round_R6_loop_75_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_web_price_atlas_access_required: true
```

This loop adds 4 new independent cases, 2 counterexamples, and 4 residual errors for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C22_INSURANCE_RATE_CYCLE_RESERVE.

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

The global axes are not re-proposed. They are stress-tested inside C22, where policy/value-up beta, IFRS17 reserve quality, and M&A/control-premium heat can look alike on the first candle but separate later like ink in water.

## 2. Round / Large Sector / Canonical Archetype Scope

|field|value|
|---|---|
|scheduled_round|R6|
|scheduled_loop|75|
|required_large_sector_id|L6_FINANCIAL_CAPITAL_RETURN_DIGITAL|
|canonical_archetype_id|C22_INSURANCE_RATE_CYCLE_RESERVE|
|fine_archetype_id|LIFE_REINSURANCE_EVENT_PREMIUM_VS_RESERVE_QUALITY|
|round_schedule_status|valid|
|round_sector_consistency|pass|
|loop_objective|residual_false_positive_mining | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill | 4B_non_price_requirement_stress_test | green_strictness_stress_test|

## 3. Previous Coverage / Duplicate Avoidance Check

No `stock_agent` source code was opened. Local v12 outputs show R6 loop 71–73 concentrated in C21 and R6 loop 74 in C22 using `000810`, `005830`, `001450`, and `088350`. This loop stays in scheduled R6 but avoids those C22 symbols and tests four new C22 symbols: `032830`, `003690`, `082640`, and `000400`.

|symbol|duplicate stance|reason|
|---|---|---|
|032830|new independent|new C22 life-insurer high-MAE success path|
|003690|new independent|new C22 reinsurer reserve-quality stable path|
|082640|new independent|new C22/C32 boundary, control-premium counterexample|
|000400|new independent|new sale-event/reserve-risk counterexample|

## 4. Stock-Web OHLC Input / Price Source Validation

`Songdaiki/stock-web` manifest anchor: `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, `min_date=1995-05-02`, `max_date=2026-02-20`, `tradable_row_count=14,354,401`, `symbol_count=5,414`, `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year`. The manifest notes that raw/unadjusted OHLC is used, zero-volume/zero-OHLC rows are excluded from calibration shards, and corporate-action contaminated windows are blocked by default.

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

|symbol|entry_date|profile_path|180D forward|corporate_action_window_status|calibration_usable|
|---|---|---|---|---|---|
|032830|2024-02-23|atlas/symbol_profiles/032/032830.json|available|clean_180D_window|true|
|003690|2024-02-23|atlas/symbol_profiles/003/003690.json|available|clean_180D_window|true|
|082640|2024-02-23|atlas/symbol_profiles/082/082640.json|available|clean_180D_window|true|
|000400|2024-02-23|atlas/symbol_profiles/000/000400.json|available|clean_180D_window|true|

The selected 2024 windows avoid each symbol profile's corporate-action candidate dates. The stock-web profile caveat is respected: raw/unadjusted prices are suitable for these windows only because no candidate date overlaps the D+180 calibration window.

## 6. Canonical Archetype Compression Map

`C22_INSURANCE_RATE_CYCLE_RESERVE` is split into three machine-useful sub-paths:

1. **IFRS17 / reserve-quality path**: reserve visibility, CSM/earnings quality, capital adequacy, and capital return are present. This supports `032830` and `003690`.
2. **Life-insurer high-MAE path**: positive re-rating can still have rate/capital sensitivity, so the entry may be usable while 4B watch must remain awake.
3. **Event/control-premium path**: stock can move a lot, but the move is not evidence of C22 reserve quality. `082640` and `000400` are therefore counterexamples for C22, even though their MFE is high.

## 7. Case Selection Summary

|case_id|symbol|company|role|pos/counter|entry|price|MFE90|MAE90|MFE180|MAE180|current|
|---|---|---|---|---|---|---|---|---|---|---|---|
|R6L75_C22_032830_SAMSUNG_LIFE_20240223_LIFE_IFRS17_VALUEUP_HIGH_MAE_SUCCESS|032830|삼성생명|high_mae_success|positive|2024-02-23|95600|13.49%|-15.27%|16.11%|-15.27%|current_profile_4B_too_late|
|R6L75_C22_003690_KOREAN_RE_20240223_REINSURANCE_RESERVE_STABLE_SUCCESS|003690|코리안리|structural_success|positive|2024-02-23|8020|6.61%|-6.48%|12.22%|-6.48%|current_profile_too_late|
|R6L75_C22_082640_TONGYANG_LIFE_20240223_CONTROL_PREMIUM_FALSE_POSITIVE|082640|동양생명|price_moved_without_evidence|counterexample|2024-02-23|5480|70.44%|-11.86%|72.26%|-11.86%|current_profile_false_positive|
|R6L75_C22_000400_LOTTE_INSURANCE_20240223_SALE_EVENT_RESERVE_RISK_FALSE_POSITIVE|000400|롯데손해보험|4B_overlay_success|counterexample|2024-02-23|3050|34.10%|-11.48%|34.10%|-28.69%|current_profile_false_positive|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
calibration_usable_case_count = 4
new_independent_case_ratio = 1.00
```

Positive cases are not simply "insurance stocks went up". They have enough reserve/ROE/capital-quality evidence to remain C22 candidates. Counterexamples are precisely the opposite: the price moved, but the engine under the hood was event premium or sale expectation rather than reserve quality.

## 9. Evidence Source Map

|symbol|stage2|stage3|4B|4C|evidence_source|
|---|---|---|---|---|---|
|032830|public_event_or_disclosure,policy_or_regulatory_optionality,early_revision_signal,relative_strength|confirmed_revision,financial_visibility,low_red_team_risk|positioning_overheat,price_only_local_peak||Reuters Korea value-up policy coverage; stock-web 032830 profile and 2024 tradable shard; production promotion should attach dated company IR/DART if required.|
|003690|public_event_or_disclosure,policy_or_regulatory_optionality,early_revision_signal|financial_visibility,low_red_team_risk,durable_customer_confirmation|||Reuters Korea value-up policy coverage; stock-web 003690 profile and 2024 tradable shard; production promotion should attach dated company filings/IR if required.|
|082640|public_event_or_disclosure,policy_or_regulatory_optionality,relative_strength||valuation_blowoff,positioning_overheat,explicit_event_cap,price_only_local_peak|thesis_evidence_broken|Reuters Korea value-up policy coverage; Woori/Tongyang Life acquisition context; stock-web 082640 profile and 2024 tradable shard.|
|000400|public_event_or_disclosure,policy_or_regulatory_optionality,relative_strength||valuation_blowoff,positioning_overheat,explicit_event_cap,price_only_local_peak|thesis_evidence_broken|Reuters Korea value-up policy coverage; stock-web 000400 profile and 2024 tradable shard; production promotion should attach dated sale/auction and company filing evidence if required.|

## 10. Price Data Source Map

|symbol|company|tradable_shard_path|profile_path|price_basis|adjustment|
|---|---|---|---|---|---|
|032830|삼성생명|atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv|atlas/symbol_profiles/032/032830.json|tradable_raw|raw_unadjusted_marcap|
|003690|코리안리|atlas/ohlcv_tradable_by_symbol_year/003/003690/2024.csv|atlas/symbol_profiles/003/003690.json|tradable_raw|raw_unadjusted_marcap|
|082640|동양생명|atlas/ohlcv_tradable_by_symbol_year/082/082640/2024.csv|atlas/symbol_profiles/082/082640.json|tradable_raw|raw_unadjusted_marcap|
|000400|롯데손해보험|atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv|atlas/symbol_profiles/000/000400.json|tradable_raw|raw_unadjusted_marcap|

## 11. Case-by-Case Trigger Grid

|trigger_id|case_id|symbol|trigger_type|trigger_date|entry_date|entry_price|dedupe_for_aggregate|aggregate_group_role|
|---|---|---|---|---|---|---|---|---|
|R6L75_T_032830_STAGE2A_20240223_LIFE_IFRS17_VALUEUP|R6L75_C22_032830_SAMSUNG_LIFE_20240223_LIFE_IFRS17_VALUEUP_HIGH_MAE_SUCCESS|032830|Stage2-Actionable|2024-02-22|2024-02-23|95600|True|representative|
|R6L75_T_003690_STAGE2A_20240223_REINSURANCE_RESERVE_QUALITY|R6L75_C22_003690_KOREAN_RE_20240223_REINSURANCE_RESERVE_STABLE_SUCCESS|003690|Stage2-Actionable|2024-02-22|2024-02-23|8020|True|representative|
|R6L75_T_082640_STAGE2_FP_20240223_LIFE_POLICY_BETA_CONTROL_PREMIUM|R6L75_C22_082640_TONGYANG_LIFE_20240223_CONTROL_PREMIUM_FALSE_POSITIVE|082640|Stage2-FalsePositive|2024-02-22|2024-02-23|5480|True|representative|
|R6L75_T_000400_STAGE2_FP_20240223_SALE_EVENT_RESERVE_RISK|R6L75_C22_000400_LOTTE_INSURANCE_20240223_SALE_EVENT_RESERVE_RISK_FALSE_POSITIVE|000400|Stage2-FalsePositive|2024-02-22|2024-02-23|3050|True|representative|

## 12. Trigger-Level OHLC Backtest Tables

|symbol|company|entry_date|entry_price|MFE_30D|MAE_30D|MFE_90D|MAE_90D|MFE_180D|MAE_180D|peak_date|peak_price|drawdown_after_peak|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|032830|삼성생명|2024-02-23|95600|13.49%|-8.47%|13.49%|-15.27%|16.11%|-15.27%|2024-11-18|111000|-11.71%|
|003690|코리안리|2024-02-23|8020|6.61%|-6.48%|6.61%|-6.48%|12.22%|-6.48%|2024-08-26|9000|-9.00%|
|082640|동양생명|2024-02-23|5480|18.61%|-6.93%|70.44%|-11.86%|72.26%|-11.86%|2024-07-31|9440|-44.70%|
|000400|롯데손해보험|2024-02-23|3050|19.02%|-11.48%|34.10%|-11.48%|34.10%|-28.69%|2024-06-26|4090|-46.82%|

## 13. Current Calibrated Profile Stress Test

|symbol|current_profile_verdict|actual_path|lesson|
|---|---|---|---|
|032830|current_profile_4B_too_late|life_insurer_valueup_positive_high_mae|positive but high-MAE; needs 4B watch, not lower global Green threshold|
|003690|current_profile_too_late|reserve_quality_stable_positive|modest but clean positive; current profile can underweight non-flashy reserve-quality compounding|
|082640|current_profile_false_positive|control_premium_false_positive_for_C22|high MFE is not proof of C22 reserve-quality rule; it belongs to event-premium overlay|
|000400|current_profile_false_positive|sale_event_reserve_risk_false_positive|good example where price-only rise must be capped by event/reserve guard|

Key residual: current global proxy can read `082640` and `000400` as C22 strength because the return path is large. The shadow rule makes the tape answer a narrower question: was the move caused by reserve/ROE/capital quality, or by a sale/event premium that belongs in a different drawer?

## 14. Stage2 / Yellow / Green Comparison

|symbol|Stage2 entry|Stage3/Green proxy|green_lateness_ratio|interpretation|
|---|---|---|---|---|
|032830|2024-02-23 / 95,600|2024-05-16 / 95,000|0.25|Green was not very late, but the path had high MAE; 4B watch matters more than earlier promotion.|
|003690|2024-02-23 / 8,020|2024-08-26 / 8,930|0.54|Waiting for full reserve-quality confirmation consumes about half the upside.|
|082640|2024-02-23 / 5,480|not_applicable|not_applicable|No confirmed Stage3-Green because move is event/control-premium dominant.|
|000400|2024-02-23 / 3,050|not_applicable|not_applicable|No confirmed Stage3-Green because sale-event heat and reserve risk dominate.|

## 15. 4B Local vs Full-window Timing Audit

|symbol|4B_trigger|4B_entry_price|local_proximity|full_window_proximity|verdict|
|---|---|---|---|---|---|
|032830|2024-11-18|108800|0.92|0.92|price_only_local_4B_not_full_4B_until_non_price_slowdown|
|003690|n/a|n/a|n/a|n/a|not_applicable|
|082640|2024-07-02|8450|0.75|0.75|event_premium_4B_overlay_success_not_C22_pure_quality|
|000400|2024-06-26|4000|0.91|0.91|good_full_window_4B_timing_when_event_premium_and_reserve_risk_visible|

The lesson is not to weaken full-4B non-price evidence. It is to classify the non-price evidence correctly: sale/event premium, control-premium cap, and reserve uncertainty are 4B overlays, not C22 positive evidence.

## 16. 4C Protection Audit

|symbol|four_c_protection_label|reason|
|---|---|---|
|032830|thesis_break_watch_only|High-MAE life-insurer positive; no hard thesis break in 180D.|
|003690|not_applicable|Stable positive/reinsurance reserve-quality path.|
|082640|hard_4c_success|Post-peak drawdown of about -44.70% confirms event-premium protection value.|
|000400|hard_4c_success|Post-peak drawdown of about -46.82% confirms sale-event/reserve-risk guard value.|

## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate = true`: Within L6, value-up/policy beta must be split from executed capital-return quality. The same government policy candle can lift many financial names, but only some become durable rerating. The others are policy steam: visible, hot, and gone when pressure drops.

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate = true`: For C22, add a shadow gate:

```text
if insurance_signal and (ifrs17_csm_quality + reserve_quality + kics_capital + capital_return_execution) is supported:
    allow Stage2-Actionable / Yellow promotion
elif insurance_signal is dominated by M&A, sale process, control-premium, or price-only heat:
    route to event_overlay / 4B watch, not positive C22 calibration
```

## 19. Before / After Backtest Comparison

|profile_id|scope|eligible|selected_entry|avg_MFE_90D|avg_MAE_90D|avg_MFE_180D|avg_MAE_180D|false_positive_rate|missed_structural_count|late_green_count|avg_green_lateness_ratio|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|current_global_proxy|4|Stage2/Yellow mixed|31.16|-11.27|33.67|-15.57|2/4|2|1|0.40 on applicable positives|mixed; event-premium and reserve-quality are conflated|
|P0b_e2r_2_0_baseline_reference|rollback_reference|4|Stage3-heavy|10.05|-10.88|14.17|-10.88|lower but misses positives|2|2|0.60+|too late for reinsurance/life-insurer positives|
|P1_L6_sector_specific_candidate_profile|sector_specific|4|quality-gated Stage2; event overlay separated|10.05|-10.88|14.17|-10.88|0/2 after guard|0|1|0.40|improves L6 split|
|P2_C22_canonical_archetype_candidate_profile|canonical_archetype_specific|4|C22 reserve/ROE quality only; control premium is 4B/C32 overlay|10.05|-10.88|14.17|-10.88|0/2 after guard|0|1|0.40|best explanatory compression|
|P3_counterexample_guard_profile|guardrail|2|counterexample guard only|52.27|-11.67|53.18|-20.28|0/2 promoted|0|0|n/a|prevents event-premium winners from becoming C22 quality evidence|

## 20. Score-Return Alignment Matrix

|symbol|weighted_before|stage_before|weighted_after|stage_after|MFE180|MAE180|alignment|
|---|---|---|---|---|---|---|---|
|032830|86|Stage3-Yellow|84|Stage3-Yellow+4B-watch|16.11%|-15.27%|aligned_after_shadow_split|
|003690|73|Stage2-Actionable|77|Stage3-Yellow|12.22%|-6.48%|aligned_after_shadow_split|
|082640|76|Stage3-Yellow|62|Stage2-Watch/EventOverlayOnly|72.26%|-11.86%|aligned_after_shadow_split|
|000400|78|Stage3-Yellow|56|Stage2-Watch/EventOverlayOnly|34.10%|-28.69%|aligned_after_shadow_split|

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L6_FINANCIAL_CAPITAL_RETURN_DIGITAL|C22_INSURANCE_RATE_CYCLE_RESERVE|LIFE_REINSURANCE_EVENT_PREMIUM_VS_RESERVE_QUALITY|2|2|3|2|4|0|4|4|4|True|True|C22 now has life insurer, reinsurer, M&A/control-premium and sale-event reserve-risk holdout cases; next C22 pass should add long-tail reserve shock cases if available.|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: life_insurer_high_mae_success, reinsurance_stable_positive_missed, control_premium_false_positive_for_C22, sale_event_reserve_risk_false_positive
new_axis_proposed: C22_ifrs17_reserve_quality_gate; C22_event_premium_control_premium_cap; C22_life_insurer_high_mae_4b_watch
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated: stock-web manifest fields, symbol profiles, selected 2024 tradable OHLC rows, entry prices, MFE/MAE proxy calculations, peak/drawdown proxy calculations, corporate-action overlap status, same-entry dedupe. Not validated: production scoring implementation, live candidates, adjusted-price returns, brokerage/API behavior, or exact future promotion batch code.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C22_ifrs17_reserve_quality_gate,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Promote only when IFRS17/CSM/reserve quality and capital-return execution are visible, not merely policy beta","keeps 032830/003690 as eligible quality positives",R6L75_T_032830_STAGE2A_20240223_LIFE_IFRS17_VALUEUP|R6L75_T_003690_STAGE2A_20240223_REINSURANCE_RESERVE_QUALITY,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C22_event_premium_control_premium_cap,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Move driven by M&A/sale/control premium is 4B/event overlay or C32 boundary, not pure C22 reserve quality","blocks 082640/000400 from positive C22 calibration despite high MFE",R6L75_T_082640_STAGE2_FP_20240223_LIFE_POLICY_BETA_CONTROL_PREMIUM|R6L75_T_000400_STAGE2_FP_20240223_SALE_EVENT_RESERVE_RISK,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C22_life_insurer_high_mae_4b_watch,sector_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Life-insurer winners can still carry rate/capital sensitivity; attach 4B watch when price outruns non-price quality","captures 032830 high-MAE success without weakening global full-4B non-price requirement",R6L75_T_032830_STAGE2A_20240223_LIFE_IFRS17_VALUEUP,4,4,2,low,sector_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type":"case","case_id":"R6L75_C22_032830_SAMSUNG_LIFE_20240223_LIFE_IFRS17_VALUEUP_HIGH_MAE_SUCCESS","symbol":"032830","company_name":"삼성생명","round":"R6","loop":"75","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_REINSURANCE_EVENT_PREMIUM_VS_RESERVE_QUALITY","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R6L75_T_032830_STAGE2A_20240223_LIFE_IFRS17_VALUEUP","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_after_C22_quality_event_split","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"positive but high-MAE; needs 4B watch, not lower global Green threshold"}
{"row_type":"case","case_id":"R6L75_C22_003690_KOREAN_RE_20240223_REINSURANCE_RESERVE_STABLE_SUCCESS","symbol":"003690","company_name":"코리안리","round":"R6","loop":"75","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_REINSURANCE_EVENT_PREMIUM_VS_RESERVE_QUALITY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L75_T_003690_STAGE2A_20240223_REINSURANCE_RESERVE_QUALITY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_after_C22_quality_event_split","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"modest but clean positive; current profile can underweight non-flashy reserve-quality compounding"}
{"row_type":"case","case_id":"R6L75_C22_082640_TONGYANG_LIFE_20240223_CONTROL_PREMIUM_FALSE_POSITIVE","symbol":"082640","company_name":"동양생명","round":"R6","loop":"75","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_REINSURANCE_EVENT_PREMIUM_VS_RESERVE_QUALITY","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"R6L75_T_082640_STAGE2_FP_20240223_LIFE_POLICY_BETA_CONTROL_PREMIUM","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_after_C22_quality_event_split","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"high MFE is not proof of C22 reserve-quality rule; it belongs to event-premium overlay"}
{"row_type":"case","case_id":"R6L75_C22_000400_LOTTE_INSURANCE_20240223_SALE_EVENT_RESERVE_RISK_FALSE_POSITIVE","symbol":"000400","company_name":"롯데손해보험","round":"R6","loop":"75","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_REINSURANCE_EVENT_PREMIUM_VS_RESERVE_QUALITY","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"R6L75_T_000400_STAGE2_FP_20240223_SALE_EVENT_RESERVE_RISK","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_after_C22_quality_event_split","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"good example where price-only rise must be capped by event/reserve guard"}
```

### trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R6L75_T_032830_STAGE2A_20240223_LIFE_IFRS17_VALUEUP","case_id":"R6L75_C22_032830_SAMSUNG_LIFE_20240223_LIFE_IFRS17_VALUEUP_HIGH_MAE_SUCCESS","symbol":"032830","company_name":"삼성생명","round":"R6","loop":"75","scheduled_round":"R6","scheduled_loop":75,"round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_REINSURANCE_EVENT_PREMIUM_VS_RESERVE_QUALITY","sector":"financial_insurance","primary_archetype":"insurance_rate_cycle_reserve","loop_objective":"residual_false_positive_mining | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill | 4B_non_price_requirement_stress_test | green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","evidence_available_at_that_date":"FY2023/IFRS17 life-insurer value-up and shareholder-return expectation was visible before the next-trading-day entry; quality was partly real but still rate/capital-sensitive.","evidence_source":"Reuters Korea value-up policy coverage; stock-web 032830 profile and 2024 tradable shard; production promotion should attach dated company IR/DART if required.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","early_revision_signal","relative_strength"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv","profile_path":"atlas/symbol_profiles/032/032830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-23","entry_price":95600,"MFE_30D_pct":13.49,"MFE_90D_pct":13.49,"MFE_180D_pct":16.11,"MFE_1Y_pct":16.11,"MFE_2Y_pct":null,"MAE_30D_pct":-8.47,"MAE_90D_pct":-15.27,"MAE_180D_pct":-15.27,"MAE_1Y_pct":-15.27,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-18","peak_price":111000,"drawdown_after_peak_pct":-11.71,"green_lateness_ratio":"0.25","four_b_local_peak_proximity":0.92,"four_b_full_window_peak_proximity":0.92,"four_b_timing_verdict":"price_only_local_4B_not_full_4B_until_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"life_insurer_valueup_positive_high_mae","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L75_C22_032830_SAMSUNG_LIFE_20240223_LIFE_IFRS17_VALUEUP_HIGH_MAE_SUCCESS__2024-02-23","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L75_T_003690_STAGE2A_20240223_REINSURANCE_RESERVE_QUALITY","case_id":"R6L75_C22_003690_KOREAN_RE_20240223_REINSURANCE_RESERVE_STABLE_SUCCESS","symbol":"003690","company_name":"코리안리","round":"R6","loop":"75","scheduled_round":"R6","scheduled_loop":75,"round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_REINSURANCE_EVENT_PREMIUM_VS_RESERVE_QUALITY","sector":"financial_insurance","primary_archetype":"insurance_rate_cycle_reserve","loop_objective":"residual_false_positive_mining | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill | 4B_non_price_requirement_stress_test | green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","evidence_available_at_that_date":"Reinsurance/rate-cycle reserve quality plus value-up sector tailwind was visible; unlike policy-only beta, the stock-web path had modest MFE with controlled MAE.","evidence_source":"Reuters Korea value-up policy coverage; stock-web 003690 profile and 2024 tradable shard; production promotion should attach dated company filings/IR if required.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","low_red_team_risk","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003690/2024.csv","profile_path":"atlas/symbol_profiles/003/003690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-23","entry_price":8020,"MFE_30D_pct":6.61,"MFE_90D_pct":6.61,"MFE_180D_pct":12.22,"MFE_1Y_pct":18.45,"MFE_2Y_pct":null,"MAE_30D_pct":-6.48,"MAE_90D_pct":-6.48,"MAE_180D_pct":-6.48,"MAE_1Y_pct":-6.48,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-26","peak_price":9000,"drawdown_after_peak_pct":-9.0,"green_lateness_ratio":"0.54","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"reserve_quality_stable_positive","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L75_C22_003690_KOREAN_RE_20240223_REINSURANCE_RESERVE_STABLE_SUCCESS__2024-02-23","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L75_T_082640_STAGE2_FP_20240223_LIFE_POLICY_BETA_CONTROL_PREMIUM","case_id":"R6L75_C22_082640_TONGYANG_LIFE_20240223_CONTROL_PREMIUM_FALSE_POSITIVE","symbol":"082640","company_name":"동양생명","round":"R6","loop":"75","scheduled_round":"R6","scheduled_loop":75,"round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_REINSURANCE_EVENT_PREMIUM_VS_RESERVE_QUALITY","sector":"financial_insurance","primary_archetype":"insurance_rate_cycle_reserve","loop_objective":"residual_false_positive_mining | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill | 4B_non_price_requirement_stress_test | green_strictness_stress_test","trigger_type":"Stage2-FalsePositive","trigger_date":"2024-02-22","evidence_available_at_that_date":"Life-insurer value-up/rate-cycle beta existed, but the later large move was dominated by acquisition/control-premium optionality rather than reserve/ROE quality; this is a C22/C32 boundary counterexample.","evidence_source":"Reuters Korea value-up policy coverage; Woori/Tongyang Life acquisition context; stock-web 082640 profile and 2024 tradable shard.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","explicit_event_cap","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/082/082640/2024.csv","profile_path":"atlas/symbol_profiles/082/082640.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-23","entry_price":5480,"MFE_30D_pct":18.61,"MFE_90D_pct":70.44,"MFE_180D_pct":72.26,"MFE_1Y_pct":72.26,"MFE_2Y_pct":null,"MAE_30D_pct":-6.93,"MAE_90D_pct":-11.86,"MAE_180D_pct":-11.86,"MAE_1Y_pct":-11.86,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-31","peak_price":9440,"drawdown_after_peak_pct":-44.7,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.75,"four_b_full_window_peak_proximity":0.75,"four_b_timing_verdict":"event_premium_4B_overlay_success_not_C22_pure_quality","four_b_evidence_type":["valuation_blowoff","control_premium_or_event_premium","positioning_overheat"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"control_premium_false_positive_for_C22","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L75_C22_082640_TONGYANG_LIFE_20240223_CONTROL_PREMIUM_FALSE_POSITIVE__2024-02-23","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L75_T_000400_STAGE2_FP_20240223_SALE_EVENT_RESERVE_RISK","case_id":"R6L75_C22_000400_LOTTE_INSURANCE_20240223_SALE_EVENT_RESERVE_RISK_FALSE_POSITIVE","symbol":"000400","company_name":"롯데손해보험","round":"R6","loop":"75","scheduled_round":"R6","scheduled_loop":75,"round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_REINSURANCE_EVENT_PREMIUM_VS_RESERVE_QUALITY","sector":"financial_insurance","primary_archetype":"insurance_rate_cycle_reserve","loop_objective":"residual_false_positive_mining | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill | 4B_non_price_requirement_stress_test | green_strictness_stress_test","trigger_type":"Stage2-FalsePositive","trigger_date":"2024-02-22","evidence_available_at_that_date":"Insurer value-up and sale/event attention produced a strong move, but stock-web shows the full-window path was event-premium then unwind; reserve/capital quality was not clean enough for positive C22 promotion.","evidence_source":"Reuters Korea value-up policy coverage; stock-web 000400 profile and 2024 tradable shard; production promotion should attach dated sale/auction and company filing evidence if required.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","explicit_event_cap","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv","profile_path":"atlas/symbol_profiles/000/000400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-23","entry_price":3050,"MFE_30D_pct":19.02,"MFE_90D_pct":34.1,"MFE_180D_pct":34.1,"MFE_1Y_pct":34.1,"MFE_2Y_pct":null,"MAE_30D_pct":-11.48,"MAE_90D_pct":-11.48,"MAE_180D_pct":-28.69,"MAE_1Y_pct":-28.69,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-26","peak_price":4090,"drawdown_after_peak_pct":-46.82,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.91,"four_b_full_window_peak_proximity":0.91,"four_b_timing_verdict":"good_full_window_4B_timing_when_event_premium_and_reserve_risk_visible","four_b_evidence_type":["valuation_blowoff","control_premium_or_event_premium","positioning_overheat"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"sale_event_reserve_risk_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L75_C22_000400_LOTTE_INSURANCE_20240223_SALE_EVENT_RESERVE_RISK_FALSE_POSITIVE__2024-02-23","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L75_C22_032830_SAMSUNG_LIFE_20240223_LIFE_IFRS17_VALUEUP_HIGH_MAE_SUCCESS","trigger_id":"R6L75_T_032830_STAGE2A_20240223_LIFE_IFRS17_VALUEUP","symbol":"032830","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":12,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":7,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_quality_score":10,"capital_return_score":7,"ifrs17_csm_quality_score":9,"reserve_quality_score":8,"kics_capital_score":8,"rate_sensitivity_score":8,"event_premium_score":0,"mna_control_premium_score":0,"loss_ratio_risk_score":0,"positioning_overheat_score":-4,"thesis_break_score":0},"weighted_score_before":86,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":12,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":7,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_quality_score":12,"capital_return_score":8,"ifrs17_csm_quality_score":10,"reserve_quality_score":9,"kics_capital_score":8,"rate_sensitivity_score":5,"event_premium_score":0,"mna_control_premium_score":0,"loss_ratio_risk_score":0,"positioning_overheat_score":-8,"thesis_break_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow+4B-watch","changed_components":["C22_ifrs17_reserve_quality_gate","C22_event_premium_cap","C22_life_rate_sensitivity_penalty"],"component_delta_explanation":"After profile distinguishes reserve/ROE/capital quality from event/control-premium beta; positive quality cases remain eligible while event-premium moves are 4B/event-overlay only.","MFE_90D_pct":13.49,"MAE_90D_pct":-15.27,"score_return_alignment_label":"aligned_after_shadow_split","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L75_C22_003690_KOREAN_RE_20240223_REINSURANCE_RESERVE_STABLE_SUCCESS","trigger_id":"R6L75_T_003690_STAGE2A_20240223_REINSURANCE_RESERVE_QUALITY","symbol":"003690","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":7,"relative_strength_score":7,"customer_quality_score":0,"policy_or_regulatory_score":6,"valuation_repricing_score":4,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_quality_score":7,"capital_return_score":5,"ifrs17_csm_quality_score":6,"reserve_quality_score":12,"kics_capital_score":9,"rate_sensitivity_score":5,"event_premium_score":0,"mna_control_premium_score":0,"loss_ratio_risk_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":7,"relative_strength_score":7,"customer_quality_score":0,"policy_or_regulatory_score":6,"valuation_repricing_score":4,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_quality_score":8,"capital_return_score":6,"ifrs17_csm_quality_score":7,"reserve_quality_score":15,"kics_capital_score":10,"rate_sensitivity_score":4,"event_premium_score":0,"mna_control_premium_score":0,"loss_ratio_risk_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":77,"stage_label_after":"Stage3-Yellow","changed_components":["C22_ifrs17_reserve_quality_gate","C22_event_premium_cap","C22_life_rate_sensitivity_penalty"],"component_delta_explanation":"After profile distinguishes reserve/ROE/capital quality from event/control-premium beta; positive quality cases remain eligible while event-premium moves are 4B/event-overlay only.","MFE_90D_pct":6.61,"MAE_90D_pct":-6.48,"score_return_alignment_label":"aligned_after_shadow_split","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L75_C22_082640_TONGYANG_LIFE_20240223_CONTROL_PREMIUM_FALSE_POSITIVE","trigger_id":"R6L75_T_082640_STAGE2_FP_20240223_LIFE_POLICY_BETA_CONTROL_PREMIUM","symbol":"082640","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":8,"execution_risk_score":-8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_quality_score":4,"capital_return_score":3,"ifrs17_csm_quality_score":3,"reserve_quality_score":3,"kics_capital_score":3,"rate_sensitivity_score":9,"event_premium_score":16,"mna_control_premium_score":18,"loss_ratio_risk_score":0,"positioning_overheat_score":-10,"thesis_break_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":6,"customer_quality_score":0,"policy_or_regulatory_score":5,"valuation_repricing_score":4,"execution_risk_score":-12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_quality_score":2,"capital_return_score":1,"ifrs17_csm_quality_score":2,"reserve_quality_score":2,"kics_capital_score":2,"rate_sensitivity_score":4,"event_premium_score":18,"mna_control_premium_score":20,"loss_ratio_risk_score":0,"positioning_overheat_score":-14,"thesis_break_score":-8},"weighted_score_after":62,"stage_label_after":"Stage2-Watch/EventOverlayOnly","changed_components":["C22_ifrs17_reserve_quality_gate","C22_event_premium_cap","C22_life_rate_sensitivity_penalty"],"component_delta_explanation":"After profile distinguishes reserve/ROE/capital quality from event/control-premium beta; positive quality cases remain eligible while event-premium moves are 4B/event-overlay only.","MFE_90D_pct":70.44,"MAE_90D_pct":-11.86,"score_return_alignment_label":"aligned_after_shadow_split","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L75_C22_000400_LOTTE_INSURANCE_20240223_SALE_EVENT_RESERVE_RISK_FALSE_POSITIVE","trigger_id":"R6L75_T_000400_STAGE2_FP_20240223_SALE_EVENT_RESERVE_RISK","symbol":"000400","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":9,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":9,"execution_risk_score":-10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_quality_score":3,"capital_return_score":2,"ifrs17_csm_quality_score":3,"reserve_quality_score":2,"kics_capital_score":2,"rate_sensitivity_score":0,"event_premium_score":18,"mna_control_premium_score":14,"loss_ratio_risk_score":-10,"positioning_overheat_score":-12,"thesis_break_score":-8},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":6,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":3,"execution_risk_score":-14,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_quality_score":1,"capital_return_score":0,"ifrs17_csm_quality_score":1,"reserve_quality_score":1,"kics_capital_score":1,"rate_sensitivity_score":0,"event_premium_score":19,"mna_control_premium_score":16,"loss_ratio_risk_score":-14,"positioning_overheat_score":-16,"thesis_break_score":-12},"weighted_score_after":56,"stage_label_after":"Stage2-Watch/EventOverlayOnly","changed_components":["C22_ifrs17_reserve_quality_gate","C22_event_premium_cap","C22_life_rate_sensitivity_penalty"],"component_delta_explanation":"After profile distinguishes reserve/ROE/capital quality from event/control-premium beta; positive quality cases remain eligible while event-premium moves are 4B/event-overlay only.","MFE_90D_pct":34.1,"MAE_90D_pct":-11.48,"score_return_alignment_label":"aligned_after_shadow_split","current_profile_verdict":"current_profile_false_positive"}
```

### residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R6","loop":"75","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","scheduled_round":"R6","scheduled_loop":75,"round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":4,"diversity_score_summary":"same_archetype_new_symbol=4;new_trigger_family=4;counterexample_gap=2;residual_error=4;wrong_round_penalty=0","tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["life_insurer_high_mae_success","reinsurance_stable_positive_missed","control_premium_false_positive_for_C22","sale_event_reserve_risk_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### narrative_only rows

```jsonl

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
completed_round = R6
completed_loop = 75
next_round = R7
next_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-web manifest: `atlas/manifest.json`, max_date `2026-02-20`, price basis `tradable_raw`, `raw_unadjusted_marcap`.
- Stock-web profile anchors used: `032830`, `003690`, `082640`, `000400` symbol profiles.
- Stock-web OHLC anchors used: the selected 2024 tradable shards for each symbol.
- External historical context: Reuters February-May 2024 Korea corporate value-up coverage; Woori/Tongyang Life acquisition context is treated as event/control-premium evidence, not C22 reserve-quality evidence.


# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
scheduled_round: R6
scheduled_loop: 74
completed_round: R6
completed_loop: 74
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: IFRS17_INSURANCE_ROE_CAPITAL_RETURN_RESERVE_QUALITY
output_file: e2r_stock_web_v12_residual_round_R6_loop_74_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_web_price_atlas_access_required: true
```

This loop adds 4 new independent cases, 2 counterexamples, and 4 residual errors for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C22_INSURANCE_RATE_CYCLE_RESERVE.

## 1. Current Calibrated Profile Assumption

- current_default_profile_proxy: `e2r_2_1_stock_web_calibrated`
- rollback_reference_profile_id: `e2r_2_0_baseline_reference`
- Existing applied axes are not re-proposed globally. They are stress-tested only: `stage2_actionable_evidence_bonus`, `stage3_yellow_total_min`, `stage3_green_total_min`, `stage3_green_revision_min`, `stage3_cross_evidence_green_buffer`, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`, `hard_4c_thesis_break_routes_to_4c`.
- Existing-axis result: `existing_axis_strengthened` for `full_4b_requires_non_price_evidence` and `price_only_blowoff_blocks_positive_stage`; `existing_axis_kept` for global Stage2/Yellow/Green thresholds.

## 2. Round / Large Sector / Canonical Archetype Scope

|field|value|
|---|---|
|scheduled_round|R6|
|scheduled_loop|74|
|required_large_sector_id|L6_FINANCIAL_CAPITAL_RETURN_DIGITAL|
|selected_canonical_archetype_id|C22_INSURANCE_RATE_CYCLE_RESERVE|
|fine_archetype_id|IFRS17_INSURANCE_ROE_CAPITAL_RETURN_RESERVE_QUALITY|
|round_schedule_status|valid|
|round_sector_consistency|pass|

## 3. Previous Coverage / Duplicate Avoidance Check

The allowed stock_agent registry was checked for calibration artifacts, but the registry available in-repo is legacy/sparse for current v12 residual loops. Local prior outputs show R6 loop 71–73 concentrated in C21, while the immediately prior R5 loop 74 file sets `next_round=R6`, `next_loop=74`. This run therefore fills the scheduled R6 slot with C22 instead of rematerializing C21.


|source|path|result|
|---|---|---|
|manifest|atlas/manifest.json|max_date=2026-02-20; tradable_row_count=14,354,401; raw_unadjusted_marcap|
|schema|atlas/schema.json|tradable columns d/o/h/l/c/v/a/mc/s/m; MFE/MAE formulas confirmed|
|registry|stock_agent/data/e2r/calibration/md_registry.jsonl|legacy/sparse; local previous MD next_state used for schedule|

Novelty gate result: 4/4 calibration-usable cases are new independent symbols for this C22 loop; no case reuses the same symbol/trigger/entry/evidence family from the local R6 loop 71–73 C21 set.

## 4. Stock-Web OHLC Input / Price Source Validation

|field|value|
|---|---|
|source_name|FinanceData/marcap|
|source_repo_url|https://github.com/FinanceData/marcap|
|price_adjustment_status|raw_unadjusted_marcap|
|min_date|1995-05-02|
|max_date|2026-02-20|
|tradable_row_count|14354401|
|raw_row_count|15214118|
|symbol_count|5414|
|active_like_symbol_count|2868|
|inactive_or_delisted_like_symbol_count|2546|
|markets|KONEX,KOSDAQ,KOSDAQ GLOBAL,KOSPI|
|calibration_shard_root|atlas/ohlcv_tradable_by_symbol_year|
|raw_shard_root|atlas/ohlcv_raw_by_symbol_year|
|schema_path|atlas/schema.json|
|universe_path|atlas/universe/all_symbols.csv|

Stock-web schema confirms tradable columns `d,o,h,l,c,v,a,mc,s,m` and MFE/MAE formulas using max high / min low across forward tradable rows. The price basis is `tradable_raw`, raw/unadjusted marcap; no adjusted-price route was introduced.

## 5. Historical Eligibility Gate

|symbol|entry_date|180D forward window|OHLC present|corporate action overlap|calibration_usable|
|---|---|---|---|---|---|
|000810|2024-02-23|available by manifest max_date 2026-02-20|yes|clean_180D_window|true|
|005830|2024-02-23|available by manifest max_date 2026-02-20|yes|clean_180D_window|true|
|001450|2024-02-23|available by manifest max_date 2026-02-20|yes|clean_180D_window|true|
|088350|2024-02-23|available by manifest max_date 2026-02-20|yes|clean_180D_window|true|

## 6. Canonical Archetype Compression Map

- `C22_INSURANCE_RATE_CYCLE_RESERVE` compresses three fine paths: P/C insurer ROE/capital-return quality, reserve/loss-ratio risk, and life-insurer capital sensitivity.
- The proposed compression is not a global financial value-up rule; it is a C22-specific split between executed quality and policy-only beta.

## 7. Case Selection Summary

|case_id|symbol|company|positive/counterexample|case_type|entry_date|entry_price|MFE_90D|MAE_90D|MFE_180D|MAE_180D|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|
|R6L74_C22_000810_SAMSUNG_FIRE_20240223|000810|삼성화재|positive|structural_success|2024-02-23|308500|27.55|-11.67|27.55|-11.67|current_profile_missed_structural|
|R6L74_C22_005830_DB_INSURANCE_20240223|005830|DB손해보험|positive|structural_success|2024-02-23|97800|23.42|-11.86|26.79|-11.86|current_profile_missed_structural|
|R6L74_C22_001450_HYUNDAI_MARINE_20240223|001450|현대해상|counterexample|failed_rerating|2024-02-23|34650|3.46|-17.89|6.06|-21.36|current_profile_false_positive|
|R6L74_C22_088350_HANWHA_LIFE_20240223|088350|한화생명|counterexample|false_positive_green|2024-02-23|3385|3.84|-23.78|3.84|-24.52|current_profile_false_positive|

## 8. Positive vs Counterexample Balance

- Positive structural successes: 삼성화재, DB손해보험.
- Counterexamples / failed rerating: 현대해상, 한화생명.
- The positive/counterexample split is explained by reserve/capital sensitivity and whether capital-return/ROE quality was executable rather than merely policy-thematic.

## 9. Evidence Source Map

|symbol|stage2 evidence|stage3 evidence|4B/4C evidence|evidence note|
|---|---|---|---|---|
|000810|public_event_or_disclosure; policy_or_regulatory_optionality; early_revision_signal|confirmed_revision; financial_visibility; low_red_team_risk|none|FY2023/IFRS17 earnings-capital-return and value-up policy evidence was available before next-trading-day entry; research proxy pending exact DART/IR URL attachment.|
|005830|public_event_or_disclosure; policy_or_regulatory_optionality; early_revision_signal|confirmed_revision; financial_visibility; low_red_team_risk|none|FY2023/IFRS17 earnings-capital-return and value-up policy evidence was available before next-trading-day entry; research proxy pending exact DART/IR URL attachment.|
|001450|public_event_or_disclosure; policy_or_regulatory_optionality|none|margin_or_backlog_slowdown; thesis_evidence_broken|Same sector/policy evidence existed, but reserve/loss-ratio/capital-return quality was weaker; research proxy pending exact DART/IR URL attachment.|
|088350|public_event_or_disclosure; policy_or_regulatory_optionality|none|margin_or_backlog_slowdown; thesis_evidence_broken|Life-insurer value-up/policy evidence existed, but capital sensitivity and absent executed return made the signal non-structural; research proxy pending exact DART/IR URL attachment.|

## 10. Price Data Source Map

|symbol|company|profile_path|tradable_shard_path|corporate_action_window_status|corporate_action_candidate_dates|
|---|---|---|---|---|---|
|000810|삼성화재|atlas/symbol_profiles/000/000810.json|atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv|clean_180D_window|1999-02-01,1999-07-05,2000-02-15|
|005830|DB손해보험|atlas/symbol_profiles/005/005830.json|atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv|clean_180D_window|1999-07-20|
|001450|현대해상|atlas/symbol_profiles/001/001450.json|atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv|clean_180D_window|2004-07-13|
|088350|한화생명|atlas/symbol_profiles/088/088350.json|atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv|clean_180D_window|none|

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|trigger_type|trigger_date|entry_date|entry_price|dedupe_for_aggregate|aggregate_role|
|---|---|---|---|---|---|---|---|
|R6L74_T_000810_STAGE2_ACTIONABLE_20240223|000810|Stage2-Actionable|2024-02-22|2024-02-23|308500|True|representative|
|R6L74_T_005830_STAGE2_ACTIONABLE_20240223|005830|Stage2-Actionable|2024-02-22|2024-02-23|97800|True|representative|
|R6L74_T_001450_STAGE2_ACTIONABLE_20240223|001450|Stage2-Actionable|2024-02-22|2024-02-23|34650|True|representative|
|R6L74_T_088350_STAGE2_ACTIONABLE_20240223|088350|Stage2-Actionable|2024-02-22|2024-02-23|3385|True|representative|
|R6L74_T_000810_STAGE3_GREEN_20240516|000810|Stage3-Green|2024-05-16|2024-05-16|370000|False|label_comparison_only|
|R6L74_T_005830_STAGE3_GREEN_20240516|005830|Stage3-Green|2024-05-16|2024-05-16|111500|False|label_comparison_only|
|R6L74_T_000810_4B_PRICE_ONLY_20240628|000810|Stage4B-PriceOnlyLocal|2024-06-28|2024-06-28|389000|False|4B_overlay_only|
|R6L74_T_005830_4B_PRICE_ONLY_20240822|005830|Stage4B-PriceOnlyLocal|2024-08-22|2024-08-22|120600|False|4B_overlay_only|

## 12. Trigger-Level OHLC Backtest Tables

|symbol|company|entry_date|entry_price|MFE_30D|MAE_30D|MFE_90D|MAE_90D|MFE_180D|MAE_180D|peak_date|peak_price|drawdown_after_peak|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|000810|삼성화재|2024-02-23|308500|12.16|-7.46|27.55|-11.67|27.55|-11.67|2024-06-28|393500|-17.66|
|005830|DB손해보험|2024-02-23|97800|12.47|-6.85|23.42|-11.86|26.79|-11.86|2024-08-22|124000|-24.11|
|001450|현대해상|2024-02-23|34650|3.46|-12.41|3.46|-17.89|6.06|-21.36|2024-07-31|36750|-25.85|
|088350|한화생명|2024-02-23|3385|3.84|-17.13|3.84|-23.78|3.84|-24.52|2024-02-23|3515|-27.31|

## 13. Current Calibrated Profile Stress Test

|symbol|current verdict|stress result|axis lesson|
|---|---|---|---|
|000810|current_profile_missed_structural|missed quality-positive|Keep global axis; add C22 quality/reserve split|
|005830|current_profile_missed_structural|missed quality-positive|Keep global axis; add C22 quality/reserve split|
|001450|current_profile_false_positive|false positive without C22 guard|Keep global axis; add C22 quality/reserve split|
|088350|current_profile_false_positive|false positive without C22 guard|Keep global axis; add C22 quality/reserve split|

## 14. Stage2 / Yellow / Green Comparison

- 삼성화재 Stage3-Green comparison entry: 2024-05-16 close 370,000; green_lateness_ratio 0.724.
- DB손해보험 Stage3-Green comparison entry: 2024-05-16 close 111,500; green_lateness_ratio 0.523.
- Interpretation: waiting for full Green confirmation captured cleaner evidence but consumed much of the available upside in the two winners. The C22 shadow rule should not lower global Green thresholds; it should identify high-quality insurance Stage2 earlier.

## 15. 4B Local vs Full-window Timing Audit

|symbol|4B trigger|entry_price|local_peak_proximity|full_window_peak_proximity|verdict|
|---|---|---|---|---|---|
|000810|2024-06-28 price-only local peak|389000|0.947|0.947|price_only_local_4B_not_full_4B|
|005830|2024-08-22 price-only local peak|120600|0.87|0.87|price_only_local_4B_not_full_4B|

Price-only local peaks were close to full-window peaks, but because no non-price slowdown/dilution/legal event was attached, the existing full-4B non-price requirement is strengthened, not weakened.

## 16. 4C Protection Audit

|symbol|4C label|reason|
|---|---|---|
|001450|thesis_break_watch_only|180D MFE 6.06 vs MAE -21.36 after weak reserve/capital-return split|
|088350|thesis_break_watch_only|entry-near-peak and MAE -24.52 under life-insurer capital sensitivity|
|000810|not_applicable|positive path; no hard thesis break in 180D|
|005830|not_applicable|positive path; no hard thesis break in 180D|

## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate = true`: For L6 financials, policy/value-up exposure must be gated by executed capital-return/ROE quality. However, because this loop is insurance-only, the rule should remain sector-shadow until more banks/securities/nonlife/life cases support the same axis.

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate = true`: For C22, add a shadow `ifrs17_quality_bonus` only when ROE/margin quality and capital-return execution are visible, and add a `policy_only_reserve_risk_cap` when the signal is merely policy beta or reserve/capital sensitivity is unresolved.

## 19. Before / After Backtest Comparison

|profile_id|scope|eligible|selected_entry|avg_MFE_90D|avg_MAE_90D|avg_MFE_180D|avg_MAE_180D|false_positive_rate|missed_structural|late_green|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|current_global_proxy|4|Stage2-Actionable|14.57|-16.3|16.06|-17.35|2/4|2|2|mixed; over-promotes sector beta and under-recognizes executed capital-return quality|
|P0b_e2r_2_0_baseline_reference|rollback_reference|4|Stage3-heavy|25.48|-11.77|27.17|-11.77|lower but misses positives|2|2|too late for insurance rerating winners|
|P1_L6_sector_specific_candidate_profile|sector_specific|4|Stage2-Actionable when quality gate passes|25.48|-11.77|27.17|-11.77|0/2 selected|0|1|better alignment; still watch high-MAE winners|
|P2_C22_canonical_archetype_candidate_profile|canonical_archetype_specific|4|quality-filtered Stage2|25.48|-11.77|27.17|-11.77|0/2 selected|0|1|best explanatory compression for C22|
|P3_counterexample_guard_profile|guardrail|2|counterexample guard only|3.65|-20.84|4.95|-22.94|0/2 after guard|0|0|protects from high-MAE false positives|

## 20. Score-Return Alignment Matrix

|symbol|weighted_score_before|stage_before|weighted_score_after|stage_after|MFE_180D|MAE_180D|alignment_after|
|---|---|---|---|---|---|---|---|
|000810|82|Stage3-Yellow|88|Stage3-Green|27.55|-11.67|aligned|
|005830|80|Stage3-Yellow|87|Stage3-Green|26.79|-11.86|aligned|
|001450|76|Stage3-Yellow|68|Stage2-Watch|6.06|-21.36|aligned|
|088350|78|Stage3-Yellow|64|Stage2-Watch|3.84|-24.52|aligned|

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L6_FINANCIAL_CAPITAL_RETURN_DIGITAL|C22_INSURANCE_RATE_CYCLE_RESERVE|IFRS17_INSURANCE_ROE_CAPITAL_RETURN_RESERVE_QUALITY|2|2|2|2|4|0|8|4|4|True|True|C22 now has positive/counterexample split; still needs more life-insurer/long-tail reserve holdout cases|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: current_profile_missed_structural, current_profile_false_positive, high_MAE_policy_only_signal, price_only_local_4B_not_full_4B
new_axis_proposed: C22_ifrs17_quality_bonus; C22_policy_only_reserve_risk_cap
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated: stock-web manifest/schema, symbol profiles, 2024 tradable OHLC shards, entry/peak/MFE/MAE/drawdown, corporate-action overlap check, same-entry dedupe. Not validated: production scorer implementation, live candidate discovery, exact company disclosure URLs, adjusted-price return series, broker/API behavior.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C22_ifrs17_quality_bonus,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"executed capital-return/ROE quality separated positive insurers from policy-only beta","selected positives avg MFE_180D 27.17 vs counterexamples avg MFE_180D 4.95",R6L74_T_000810_STAGE2_ACTIONABLE_20240223|R6L74_T_005830_STAGE2_ACTIONABLE_20240223,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C22_policy_only_reserve_risk_cap,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"policy-only value-up exposure failed when reserve/capital sensitivity was unresolved","blocked 2 high-MAE counterexamples without suppressing the 2 quality positives",R6L74_T_001450_STAGE2_ACTIONABLE_20240223|R6L74_T_088350_STAGE2_ACTIONABLE_20240223,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation
```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows
```jsonl
{"row_type": "case", "case_id": "R6L74_C22_000810_SAMSUNG_FIRE_20240223", "symbol": "000810", "company_name": "삼성화재", "round": "R6", "loop": "74", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "IFRS17_INSURANCE_ROE_CAPITAL_RETURN_RESERVE_QUALITY", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L74_T_000810_STAGE2_ACTIONABLE_20240223", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "Large, clean P/C insurer showed the value-up/IFRS17 rerating path with tolerable MAE and persistent 180D MFE."}
{"row_type": "case", "case_id": "R6L74_C22_005830_DB_INSURANCE_20240223", "symbol": "005830", "company_name": "DB손해보험", "round": "R6", "loop": "74", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "IFRS17_INSURANCE_ROE_CAPITAL_RETURN_RESERVE_QUALITY", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L74_T_005830_STAGE2_ACTIONABLE_20240223", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "Capital-return/ROE quality produced a durable rerating despite mid-window volatility."}
{"row_type": "case", "case_id": "R6L74_C22_001450_HYUNDAI_MARINE_20240223", "symbol": "001450", "company_name": "현대해상", "round": "R6", "loop": "74", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "IFRS17_INSURANCE_ROE_CAPITAL_RETURN_RESERVE_QUALITY", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R6L74_T_001450_STAGE2_ACTIONABLE_20240223", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "misaligned_without_guard", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Policy-only or sector-beta promotion would have over-scored the case; 180D MAE dominated the weak MFE."}
{"row_type": "case", "case_id": "R6L74_C22_088350_HANWHA_LIFE_20240223", "symbol": "088350", "company_name": "한화생명", "round": "R6", "loop": "74", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "IFRS17_INSURANCE_ROE_CAPITAL_RETURN_RESERVE_QUALITY", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R6L74_T_088350_STAGE2_ACTIONABLE_20240223", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "misaligned_without_guard", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "The peak occurred on/near entry; policy-only value-up exposure did not protect against reserve/capital sensitivity."}
```

### 25.3 trigger rows
```jsonl
{"row_type": "trigger", "trigger_id": "R6L74_T_000810_STAGE2_ACTIONABLE_20240223", "case_id": "R6L74_C22_000810_SAMSUNG_FIRE_20240223", "symbol": "000810", "company_name": "삼성화재", "round": "R6", "loop": "74", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "IFRS17_INSURANCE_ROE_CAPITAL_RETURN_RESERVE_QUALITY", "sector": "손해보험", "primary_archetype": "insurance IFRS17 rate/reserve/capital-return quality", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-22", "evidence_available_at_that_date": "FY2023/IFRS17 earnings-capital-return and value-up policy evidence was available before next-trading-day entry; research proxy pending exact DART/IR URL attachment.", "evidence_source": "historical DART/IR/news family; exact URL deferred for coding-agent ledger attachment", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv", "profile_path": "atlas/symbol_profiles/000/000810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-23", "entry_price": 308500, "MFE_30D_pct": 12.16, "MFE_90D_pct": 27.55, "MFE_180D_pct": 27.55, "MFE_1Y_pct": "contaminated_or_unavailable_not_used", "MFE_2Y_pct": "contaminated_or_unavailable_not_used", "MAE_30D_pct": -7.46, "MAE_90D_pct": -11.67, "MAE_180D_pct": -11.67, "MAE_1Y_pct": "contaminated_or_unavailable_not_used", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-28", "peak_price": 393500, "drawdown_after_peak_pct": -17.66, "green_lateness_ratio": "not_applicable_for_representative_stage2", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_for_stage2", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L74_G_000810_20240223", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L74_T_005830_STAGE2_ACTIONABLE_20240223", "case_id": "R6L74_C22_005830_DB_INSURANCE_20240223", "symbol": "005830", "company_name": "DB손해보험", "round": "R6", "loop": "74", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "IFRS17_INSURANCE_ROE_CAPITAL_RETURN_RESERVE_QUALITY", "sector": "손해보험", "primary_archetype": "insurance IFRS17 rate/reserve/capital-return quality", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-22", "evidence_available_at_that_date": "FY2023/IFRS17 earnings-capital-return and value-up policy evidence was available before next-trading-day entry; research proxy pending exact DART/IR URL attachment.", "evidence_source": "historical DART/IR/news family; exact URL deferred for coding-agent ledger attachment", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv", "profile_path": "atlas/symbol_profiles/005/005830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-23", "entry_price": 97800, "MFE_30D_pct": 12.47, "MFE_90D_pct": 23.42, "MFE_180D_pct": 26.79, "MFE_1Y_pct": "contaminated_or_unavailable_not_used", "MFE_2Y_pct": "contaminated_or_unavailable_not_used", "MAE_30D_pct": -6.85, "MAE_90D_pct": -11.86, "MAE_180D_pct": -11.86, "MAE_1Y_pct": "contaminated_or_unavailable_not_used", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-22", "peak_price": 124000, "drawdown_after_peak_pct": -24.11, "green_lateness_ratio": "not_applicable_for_representative_stage2", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_for_stage2", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L74_G_005830_20240223", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L74_T_001450_STAGE2_ACTIONABLE_20240223", "case_id": "R6L74_C22_001450_HYUNDAI_MARINE_20240223", "symbol": "001450", "company_name": "현대해상", "round": "R6", "loop": "74", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "IFRS17_INSURANCE_ROE_CAPITAL_RETURN_RESERVE_QUALITY", "sector": "손해보험", "primary_archetype": "insurance IFRS17 rate/reserve/capital-return quality", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-22", "evidence_available_at_that_date": "Same sector/policy evidence existed, but reserve/loss-ratio/capital-return quality was weaker; research proxy pending exact DART/IR URL attachment.", "evidence_source": "historical DART/IR/news family; exact URL deferred for coding-agent ledger attachment", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv", "profile_path": "atlas/symbol_profiles/001/001450.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-23", "entry_price": 34650, "MFE_30D_pct": 3.46, "MFE_90D_pct": 3.46, "MFE_180D_pct": 6.06, "MFE_1Y_pct": "contaminated_or_unavailable_not_used", "MFE_2Y_pct": "contaminated_or_unavailable_not_used", "MAE_30D_pct": -12.41, "MAE_90D_pct": -17.89, "MAE_180D_pct": -21.36, "MAE_1Y_pct": "contaminated_or_unavailable_not_used", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-31", "peak_price": 36750, "drawdown_after_peak_pct": -25.85, "green_lateness_ratio": "not_applicable_for_representative_stage2", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_for_stage2", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L74_G_001450_20240223", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L74_T_088350_STAGE2_ACTIONABLE_20240223", "case_id": "R6L74_C22_088350_HANWHA_LIFE_20240223", "symbol": "088350", "company_name": "한화생명", "round": "R6", "loop": "74", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "IFRS17_INSURANCE_ROE_CAPITAL_RETURN_RESERVE_QUALITY", "sector": "생명보험", "primary_archetype": "insurance IFRS17 rate/reserve/capital-return quality", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-22", "evidence_available_at_that_date": "Life-insurer value-up/policy evidence existed, but capital sensitivity and absent executed return made the signal non-structural; research proxy pending exact DART/IR URL attachment.", "evidence_source": "historical DART/IR/news family; exact URL deferred for coding-agent ledger attachment", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv", "profile_path": "atlas/symbol_profiles/088/088350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-23", "entry_price": 3385, "MFE_30D_pct": 3.84, "MFE_90D_pct": 3.84, "MFE_180D_pct": 3.84, "MFE_1Y_pct": "contaminated_or_unavailable_not_used", "MFE_2Y_pct": "contaminated_or_unavailable_not_used", "MAE_30D_pct": -17.13, "MAE_90D_pct": -23.78, "MAE_180D_pct": -24.52, "MAE_1Y_pct": "contaminated_or_unavailable_not_used", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-23", "peak_price": 3515, "drawdown_after_peak_pct": -27.31, "green_lateness_ratio": "not_applicable_for_representative_stage2", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_for_stage2", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "false_positive_green", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L74_G_088350_20240223", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L74_T_000810_STAGE3_GREEN_20240516", "case_id": "R6L74_C22_000810_SAMSUNG_FIRE_20240223", "symbol": "000810", "company_name": "삼성화재", "round": "R6", "loop": "74", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "IFRS17_INSURANCE_ROE_CAPITAL_RETURN_RESERVE_QUALITY", "sector": "손해보험", "primary_archetype": "insurance IFRS17 rate/reserve/capital-return quality", "loop_objective": "stage2_yellow_green_comparison|4B_non_price_requirement_stress_test", "trigger_type": "Stage3-Green", "trigger_date": "2024-05-16", "evidence_available_at_that_date": "label comparison / overlay timing row derived from public price and research proxy evidence family", "evidence_source": "stock-web OHLC overlay; non-price evidence not assumed for price-only 4B rows", "stage2_evidence_fields": [], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv", "profile_path": "atlas/symbol_profiles/000/000810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-16", "entry_price": 370000, "MFE_30D_pct": 6.35, "MFE_90D_pct": 6.35, "MFE_180D_pct": 6.35, "MFE_1Y_pct": "contaminated_or_unavailable_not_used", "MFE_2Y_pct": "contaminated_or_unavailable_not_used", "MAE_30D_pct": -10.27, "MAE_90D_pct": -12.43, "MAE_180D_pct": -12.43, "MAE_1Y_pct": "contaminated_or_unavailable_not_used", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-28", "peak_price": 393500, "drawdown_after_peak_pct": -17.66, "green_lateness_ratio": 0.724, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "label_comparison", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L74_G_000810_20240223", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": "same case label/timing comparison only", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R6L74_T_005830_STAGE3_GREEN_20240516", "case_id": "R6L74_C22_005830_DB_INSURANCE_20240223", "symbol": "005830", "company_name": "DB손해보험", "round": "R6", "loop": "74", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "IFRS17_INSURANCE_ROE_CAPITAL_RETURN_RESERVE_QUALITY", "sector": "손해보험", "primary_archetype": "insurance IFRS17 rate/reserve/capital-return quality", "loop_objective": "stage2_yellow_green_comparison|4B_non_price_requirement_stress_test", "trigger_type": "Stage3-Green", "trigger_date": "2024-05-16", "evidence_available_at_that_date": "label comparison / overlay timing row derived from public price and research proxy evidence family", "evidence_source": "stock-web OHLC overlay; non-price evidence not assumed for price-only 4B rows", "stage2_evidence_fields": [], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv", "profile_path": "atlas/symbol_profiles/005/005830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-16", "entry_price": 111500, "MFE_30D_pct": 3.5, "MFE_90D_pct": 11.21, "MFE_180D_pct": 11.21, "MFE_1Y_pct": "contaminated_or_unavailable_not_used", "MFE_2Y_pct": "contaminated_or_unavailable_not_used", "MAE_30D_pct": -10.04, "MAE_90D_pct": -15.61, "MAE_180D_pct": -15.61, "MAE_1Y_pct": "contaminated_or_unavailable_not_used", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-22", "peak_price": 124000, "drawdown_after_peak_pct": -24.11, "green_lateness_ratio": 0.523, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "label_comparison", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L74_G_005830_20240223", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": "same case label/timing comparison only", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R6L74_T_000810_4B_PRICE_ONLY_20240628", "case_id": "R6L74_C22_000810_SAMSUNG_FIRE_20240223", "symbol": "000810", "company_name": "삼성화재", "round": "R6", "loop": "74", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "IFRS17_INSURANCE_ROE_CAPITAL_RETURN_RESERVE_QUALITY", "sector": "손해보험", "primary_archetype": "insurance IFRS17 rate/reserve/capital-return quality", "loop_objective": "stage2_yellow_green_comparison|4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-PriceOnlyLocal", "trigger_date": "2024-06-28", "evidence_available_at_that_date": "label comparison / overlay timing row derived from public price and research proxy evidence family", "evidence_source": "stock-web OHLC overlay; non-price evidence not assumed for price-only 4B rows", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv", "profile_path": "atlas/symbol_profiles/000/000810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-28", "entry_price": 389000, "MFE_30D_pct": 1.16, "MFE_90D_pct": 1.16, "MFE_180D_pct": 1.16, "MFE_1Y_pct": "contaminated_or_unavailable_not_used", "MFE_2Y_pct": "contaminated_or_unavailable_not_used", "MAE_30D_pct": -16.71, "MAE_90D_pct": -16.71, "MAE_180D_pct": -16.71, "MAE_1Y_pct": "contaminated_or_unavailable_not_used", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-28", "peak_price": 393500, "drawdown_after_peak_pct": -17.66, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.947, "four_b_full_window_peak_proximity": 0.947, "four_b_timing_verdict": "price_only_local_4B_not_full_4B", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_overlay_price_only", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L74_G_000810_20240223", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same case label/timing comparison only", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R6L74_T_005830_4B_PRICE_ONLY_20240822", "case_id": "R6L74_C22_005830_DB_INSURANCE_20240223", "symbol": "005830", "company_name": "DB손해보험", "round": "R6", "loop": "74", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "IFRS17_INSURANCE_ROE_CAPITAL_RETURN_RESERVE_QUALITY", "sector": "손해보험", "primary_archetype": "insurance IFRS17 rate/reserve/capital-return quality", "loop_objective": "stage2_yellow_green_comparison|4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-PriceOnlyLocal", "trigger_date": "2024-08-22", "evidence_available_at_that_date": "label comparison / overlay timing row derived from public price and research proxy evidence family", "evidence_source": "stock-web OHLC overlay; non-price evidence not assumed for price-only 4B rows", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv", "profile_path": "atlas/symbol_profiles/005/005830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-08-22", "entry_price": 120600, "MFE_30D_pct": 2.82, "MFE_90D_pct": 2.82, "MFE_180D_pct": 2.82, "MFE_1Y_pct": "contaminated_or_unavailable_not_used", "MFE_2Y_pct": "contaminated_or_unavailable_not_used", "MAE_30D_pct": -11.69, "MAE_90D_pct": -15.59, "MAE_180D_pct": -15.59, "MAE_1Y_pct": "contaminated_or_unavailable_not_used", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-22", "peak_price": 124000, "drawdown_after_peak_pct": -24.11, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.87, "four_b_full_window_peak_proximity": 0.87, "four_b_timing_verdict": "price_only_local_4B_not_full_4B", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_overlay_price_only", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L74_G_005830_20240223", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same case label/timing comparison only", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
```

### 25.4 score_simulation rows
```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L74_C22_000810_SAMSUNG_FIRE_20240223", "trigger_id": "R6L74_T_000810_STAGE2_ACTIONABLE_20240223", "symbol": "000810", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 16, "revision_score": 18, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 11, "valuation_repricing_score": 10, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 3}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 16, "revision_score": 18, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 11, "valuation_repricing_score": 10, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 3}, "weighted_score_after": 82, "stage_label_after": "Stage3-Yellow", "changed_components": [], "component_delta_explanation": "Current calibrated proxy without C22-specific insurance quality/reserve gate.", "MFE_90D_pct": 27.55, "MAE_90D_pct": -11.67, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "C22_insurance_quality_shadow_profile", "case_id": "R6L74_C22_000810_SAMSUNG_FIRE_20240223", "trigger_id": "R6L74_T_000810_STAGE2_ACTIONABLE_20240223", "symbol": "000810", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 16, "revision_score": 18, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 11, "valuation_repricing_score": 10, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 3}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 18, "revision_score": 20, "relative_strength_score": 15, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 12, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 4}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green", "changed_components": ["margin_bridge_score", "revision_score", "valuation_repricing_score", "execution_risk_score", "accounting_trust_risk_score"], "component_delta_explanation": "C22 shadow rewards executed insurer ROE/capital-return quality and penalizes reserve/capital sensitivity without executed return.", "MFE_90D_pct": 27.55, "MAE_90D_pct": -11.67, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L74_C22_005830_DB_INSURANCE_20240223", "trigger_id": "R6L74_T_005830_STAGE2_ACTIONABLE_20240223", "symbol": "005830", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 15, "revision_score": 17, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 11, "valuation_repricing_score": 10, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 3}, "weighted_score_before": 80, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 15, "revision_score": 17, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 11, "valuation_repricing_score": 10, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 3}, "weighted_score_after": 80, "stage_label_after": "Stage3-Yellow", "changed_components": [], "component_delta_explanation": "Current calibrated proxy without C22-specific insurance quality/reserve gate.", "MFE_90D_pct": 23.42, "MAE_90D_pct": -11.86, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "C22_insurance_quality_shadow_profile", "case_id": "R6L74_C22_005830_DB_INSURANCE_20240223", "trigger_id": "R6L74_T_005830_STAGE2_ACTIONABLE_20240223", "symbol": "005830", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 15, "revision_score": 17, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 11, "valuation_repricing_score": 10, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 3}, "weighted_score_before": 80, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 17, "revision_score": 19, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 12, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 4}, "weighted_score_after": 87, "stage_label_after": "Stage3-Green", "changed_components": ["margin_bridge_score", "revision_score", "valuation_repricing_score", "execution_risk_score", "accounting_trust_risk_score"], "component_delta_explanation": "C22 shadow rewards executed insurer ROE/capital-return quality and penalizes reserve/capital sensitivity without executed return.", "MFE_90D_pct": 23.42, "MAE_90D_pct": -11.86, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L74_C22_001450_HYUNDAI_MARINE_20240223", "trigger_id": "R6L74_T_001450_STAGE2_ACTIONABLE_20240223", "symbol": "001450", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 9, "revision_score": 9, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 11, "valuation_repricing_score": 8, "execution_risk_score": -5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 9, "revision_score": 9, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 11, "valuation_repricing_score": 8, "execution_risk_score": -5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage3-Yellow", "changed_components": [], "component_delta_explanation": "Current calibrated proxy without C22-specific insurance quality/reserve gate.", "MFE_90D_pct": 3.46, "MAE_90D_pct": -17.89, "score_return_alignment_label": "misaligned", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "C22_insurance_quality_shadow_profile", "case_id": "R6L74_C22_001450_HYUNDAI_MARINE_20240223", "trigger_id": "R6L74_T_001450_STAGE2_ACTIONABLE_20240223", "symbol": "001450", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 9, "revision_score": 9, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 11, "valuation_repricing_score": 8, "execution_risk_score": -5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 7, "revision_score": 7, "relative_strength_score": 5, "customer_quality_score": 0, "policy_or_regulatory_score": 9, "valuation_repricing_score": 5, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -2}, "weighted_score_after": 68, "stage_label_after": "Stage2-Watch", "changed_components": ["margin_bridge_score", "revision_score", "valuation_repricing_score", "execution_risk_score", "accounting_trust_risk_score"], "component_delta_explanation": "C22 shadow rewards executed insurer ROE/capital-return quality and penalizes reserve/capital sensitivity without executed return.", "MFE_90D_pct": 3.46, "MAE_90D_pct": -17.89, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L74_C22_088350_HANWHA_LIFE_20240223", "trigger_id": "R6L74_T_088350_STAGE2_ACTIONABLE_20240223", "symbol": "088350", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 8, "relative_strength_score": 7, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 10, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 8, "relative_strength_score": 7, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 10, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage3-Yellow", "changed_components": [], "component_delta_explanation": "Current calibrated proxy without C22-specific insurance quality/reserve gate.", "MFE_90D_pct": 3.84, "MAE_90D_pct": -23.78, "score_return_alignment_label": "misaligned", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "C22_insurance_quality_shadow_profile", "case_id": "R6L74_C22_088350_HANWHA_LIFE_20240223", "trigger_id": "R6L74_T_088350_STAGE2_ACTIONABLE_20240223", "symbol": "088350", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 8, "relative_strength_score": 7, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 10, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 6, "revision_score": 5, "relative_strength_score": 4, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 5, "execution_risk_score": -10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -2}, "weighted_score_after": 64, "stage_label_after": "Stage2-Watch", "changed_components": ["margin_bridge_score", "revision_score", "valuation_repricing_score", "execution_risk_score", "accounting_trust_risk_score"], "component_delta_explanation": "C22 shadow rewards executed insurer ROE/capital-return quality and penalizes reserve/capital sensitivity without executed return.", "MFE_90D_pct": 3.84, "MAE_90D_pct": -23.78, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_false_positive"}
```

### 25.5 shadow_weight rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C22_ifrs17_quality_bonus,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"executed capital-return/ROE quality separated positive insurers from policy-only beta","selected positives avg MFE_180D 27.17 vs counterexamples avg MFE_180D 4.95",R6L74_T_000810_STAGE2_ACTIONABLE_20240223|R6L74_T_005830_STAGE2_ACTIONABLE_20240223,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C22_policy_only_reserve_risk_cap,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"policy-only value-up exposure failed when reserve/capital sensitivity was unresolved","blocked 2 high-MAE counterexamples without suppressing the 2 quality positives",R6L74_T_001450_STAGE2_ACTIONABLE_20240223|R6L74_T_088350_STAGE2_ACTIONABLE_20240223,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

### 25.6 residual_contribution row
```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": "74", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["current_profile_missed_structural", "current_profile_false_positive", "high_MAE_policy_only_signal", "price_only_local_4B_not_full_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only rows
```jsonl
{"row_type": "narrative_only", "case_id": "none", "symbol": null, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "reason": "all selected cases have usable 180D stock-web windows; no narrative-only case used for weight calibration", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
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
completed_loop = 74
next_round = R7
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-web manifest checked: `atlas/manifest.json`; max_date `2026-02-20`; tradable row count `14,354,401`; raw/unadjusted marcap basis.
- Stock-web schema checked: `atlas/schema.json`; MFE/MAE definitions use max high / min low over tradable rows.
- Stock-agent allowed artifact checked: `data/e2r/calibration/md_registry.jsonl`; current registry appears sparse/legacy for local v12 residual loop state.
- Symbol profiles checked: `000/000810`, `005/005830`, `001/001450`, `088/088350`.
- Price shards checked: `000/000810/2024.csv`, `005/005830/2024.csv`, `001/001450/2024.csv`, `088/088350/2024.csv`.
- Evidence claims are research-proxy-only; production promotion must attach exact DART/IR/news URLs.


# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R7
loop = 15
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id = ONCOLOGY_CLINICAL_DATA_EVENT_BINARY_RISK_AND_DURABLE_SIGNAL_GATE
output_format = one_standalone_markdown_file
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
production_scoring_changed = false
shadow_weight_only = true
```

This file is not a live candidate scan, not an investment recommendation, and not a production scoring patch. It is a historical residual calibration artifact using stock-web OHLC rows.

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

This loop does not re-prove the global Green threshold or price-only blowoff guard. It asks a narrower C24 question: when does a clinical-data event become a real rerating signal, and when is it only a binary-risk trap?

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R7
loop = 15
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id = ONCOLOGY_CLINICAL_DATA_EVENT_BINARY_RISK_AND_DURABLE_SIGNAL_GATE
loop_objective = sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|green_strictness_stress_test|4C_thesis_break_timing_test|coverage_gap_fill
```

The canonical compression is intentionally C24. The fine archetype captures oncology / radiopharma / ophthalmology data-event paths, but scoring handoff should stay compressed under `C24_BIO_TRIAL_DATA_EVENT_RISK`.

## 3. Previous Coverage / Duplicate Avoidance Check

Prior C24 rows already included 유한양행, 알테오젠, HLB, SK바이오사이언스, 한올바이오파마, 오스코텍, 신라젠, 에이비엘바이오, and 신풍제약. This loop avoids those symbol + trigger families and uses four new independent symbols:

```text
new_symbols = 310210, 220100, 365270, 288330
new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
required_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

```json
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "source_name": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546, "markets": ["KONEX", "KOSDAQ", "KOSDAQ GLOBAL", "KOSPI"], "validation_status": "usable_for_historical_calibration"}
```

Manifest validation used:

```text
source_name = FinanceData/marcap
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

## 5. Historical Eligibility Gate

All representative triggers below have historical trigger dates, stock-web tradable entry rows, at least 180 observed trading days by the stock-web max date, and no corporate-action contamination flagged in the inspected profile/window.

|symbol|company|profile_path|price_shard_path|corporate_action_window_status|calibration_usable|
|---:|---|---|---|---|---|
|310210|보로노이|atlas/symbol_profiles/310/310210.json|atlas/ohlcv_tradable_by_symbol_year/310/310210/2024.csv; 2025.csv|clean_180D_window|true|
|220100|퓨쳐켐|atlas/symbol_profiles/220/220100.json|atlas/ohlcv_tradable_by_symbol_year/220/220100/2024.csv; 2025.csv|clean_180D_window|true|
|365270|큐라클|atlas/symbol_profiles/365/365270.json|atlas/ohlcv_tradable_by_symbol_year/365/365270/2024.csv|clean_180D_window|true|
|288330|브릿지바이오테라퓨틱스|atlas/symbol_profiles/288/288330.json|atlas/ohlcv_tradable_by_symbol_year/288/288330/2023.csv|clean_180D_window|true|

## 6. Canonical Archetype Compression Map

|fine path|canonical_archetype_id|reason|
|---|---|---|
|oncology clinical-data follow-through|C24_BIO_TRIAL_DATA_EVENT_RISK|Data-event positive case, but only when follow-through/economic route exists.|
|radiopharma clinical-data optionality|C24_BIO_TRIAL_DATA_EVENT_RISK|Clinical data can rerate, but 4B risk rises after valuation stretch.|
|ophthalmology endpoint disappointment|C24_BIO_TRIAL_DATA_EVENT_RISK|Trial-data failure / endpoint ambiguity is a hard 4C route.|
|clinical-program reset / damaged data route|C24_BIO_TRIAL_DATA_EVENT_RISK|Local bounce cannot repair a broken data thesis.|

## 7. Case Selection Summary

|case_id|symbol|company|role|pos/counter|best_trigger|MFE90|MAE90|current_profile|
|---|---:|---|---|---|---|---:|---:|---|
|R7L15-C24-310210-VORONOI-VRN11-DATA-20240524|310210|보로노이|structural_success|positive|R7L15-C24-310210-T1|189.07|-7.38|current_profile_too_late|
|R7L15-C24-220100-FUTURECHEM-RADIOPHARMA-DATA-20240522|220100|퓨쳐켐|high_mae_success|positive|R7L15-C24-220100-T1|88.55|-9.02|current_profile_correct|
|R7L15-C24-365270-CURACLE-CU06-DME-DATA-20240522|365270|큐라클|4C_success|counterexample|R7L15-C24-365270-T1|2.97|-39.31|current_profile_4C_too_late|
|R7L15-C24-288330-BRIDGEBIO-BBT877-RESET-20230623|288330|브릿지바이오테라퓨틱스|failed_rerating|counterexample|R7L15-C24-288330-T1|24.17|-41.23|current_profile_false_positive|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 2
4C_case_count = 2
calibration_usable_case_count = 4
```

The balance is useful because C24 is naturally a binary-event archetype. The positive cases show that trial data can be a real signal; the counterexamples show that data disappointment or program reset turns the same-looking event into a trapdoor.

## 9. Evidence Source Map

|case_id|evidence_available_at_trigger_date|stage2 evidence|stage3 evidence|4B/4C evidence|
|---|---|---|---|---|
|R7L15-C24-310210-VORONOI-VRN11-DATA-20240524|Clinical-data catalyst and repeated post-event accumulation.|public_event_or_disclosure, relative_strength, early_revision_signal|multiple_public_sources, financial_visibility, low_red_team_risk|later 4B only|
|R7L15-C24-220100-FUTURECHEM-RADIOPHARMA-DATA-20240522|Radiopharma/prostate-cancer data-commercial optionality.|public_event_or_disclosure, policy_or_regulatory_optionality, early_revision_signal|multiple_public_sources, financial_visibility|later valuation/positioning 4B|
|R7L15-C24-365270-CURACLE-CU06-DME-DATA-20240522|Data disappointment / endpoint-risk shock.|none after event shock|none|trial_failure, thesis_evidence_broken|
|R7L15-C24-288330-BRIDGEBIO-BBT877-RESET-20230623|Clinical-program reset / damaged data route.|headline + local rebound only|none|program reset, thesis break watch|

## 10. Price Data Source Map

|symbol|entry_date|price_shard_path|profile_path|basis|
|---:|---|---|---|---|
|310210|2024-05-24|atlas/ohlcv_tradable_by_symbol_year/310/310210/2024.csv; 2025.csv|atlas/symbol_profiles/310/310210.json|tradable_raw|
|220100|2024-05-22|atlas/ohlcv_tradable_by_symbol_year/220/220100/2024.csv; 2025.csv|atlas/symbol_profiles/220/220100.json|tradable_raw|
|365270|2024-05-22|atlas/ohlcv_tradable_by_symbol_year/365/365270/2024.csv|atlas/symbol_profiles/365/365270.json|tradable_raw|
|288330|2023-06-23|atlas/ohlcv_tradable_by_symbol_year/288/288330/2023.csv|atlas/symbol_profiles/288/288330.json|tradable_raw|

## 11. Case-by-Case Trigger Grid

|trigger_id|case_id|trigger_type|trigger_date|entry_date|entry_price|MFE30|MAE30|MFE90|MAE90|MFE180|MAE180|outcome|
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
|R7L15-C24-310210-T1|R7L15-C24-310210-VORONOI-VRN11-DATA-20240524|Stage2-Actionable|2024-05-24|2024-05-24|36600|72.68|-7.38|189.07|-7.38|237.43|-7.38|structural_success|
|R7L15-C24-310210-T2|R7L15-C24-310210-VORONOI-VRN11-DATA-20240524|Stage4B-Overlay|2025-02-17|2025-02-17|121400|8.61|-12.77|26.03|-15.24|||4B_overlay_success|
|R7L15-C24-220100-T1|R7L15-C24-220100-FUTURECHEM-RADIOPHARMA-DATA-20240522|Stage2-Actionable|2024-05-22|2024-05-22|14850|22.56|-9.02|88.55|-9.02|109.76|-9.02|high_mae_success|
|R7L15-C24-220100-T2|R7L15-C24-220100-FUTURECHEM-RADIOPHARMA-DATA-20240522|Stage4B-Overlay|2024-10-15|2024-10-15|30900|1.13|-37.15|1.13|-51.46|||4B_overlay_success|
|R7L15-C24-365270-T1|R7L15-C24-365270-CURACLE-CU06-DME-DATA-20240522|4C|2024-05-22|2024-05-22|8750|2.97|-35.66|2.97|-39.31|2.97|-41.37|4C_success|
|R7L15-C24-288330-T1|R7L15-C24-288330-BRIDGEBIO-BBT877-RESET-20230623|Stage2-FalsePositive|2023-06-23|2023-06-23|6040|18.71|-31.29|24.17|-41.23|24.17|-56.79|failed_rerating|

## 12. Trigger-Level OHLC Backtest Tables

Representative triggers only:

|symbol|entry|entry_price|30D MFE/MAE|90D MFE/MAE|180D MFE/MAE|peak|drawdown after peak|score-return alignment|
|---:|---|---:|---|---|---|---|---:|---|
|310210|2024-05-24|36600|72.68 / -7.38|189.07 / -7.38|237.43 / -7.38|2025-02-17 / 123500|-14.25|strong positive; current profile too late|
|220100|2024-05-22|14850|22.56 / -9.02|88.55 / -9.02|109.76 / -9.02|2024-10-15 / 31150|-51.85|positive but 4B required|
|365270|2024-05-22|8750|2.97 / -35.66|2.97 / -39.31|2.97 / -41.37|2024-05-22 / 9010|-43.06|hard 4C success|
|288330|2023-06-23|6040|18.71 / -31.29|24.17 / -41.23|24.17 / -56.79|2023-08-10 / 7500|-65.20|local bounce false positive|

## 13. Current Calibrated Profile Stress Test

|case|current calibrated judgment|actual path|verdict|
|---|---|---|---|
|310210|Likely Yellow until repeat evidence / revision becomes obvious.|MFE180 +237.43 with low MAE.|current_profile_too_late|
|220100|Yellow is acceptable; Green should require more than event enthusiasm.|MFE180 +109.76 but drawdown after peak -51.85.|current_profile_correct|
|365270|Would need hard 4C once data disappointment is clear.|MFE180 +2.97 vs MAE180 -41.37.|current_profile_4C_too_late|
|288330|Stage2/local rebound could be over-credited without program-reset guard.|MFE180 +24.17 vs MAE180 -56.79.|current_profile_false_positive|

Existing axes:

```text
stage2_actionable_evidence_bonus = kept but C24-gated
stage3_yellow_total_min = kept
stage3_green_total_min = kept
stage3_green_revision_min = kept
stage3_cross_evidence_green_buffer = kept
price_only_blowoff_blocks_positive_stage = strengthened
full_4b_requires_non_price_evidence = strengthened
hard_4c_thesis_break_routes_to_4c = strengthened
```

## 14. Stage2 / Yellow / Green Comparison

C24 should not lower the global Green threshold. The improvement is a component gate:

```text
if trial_data_quality_score high
and repeated post-event follow-through exists
and no endpoint/program reset red flag:
    allow C24-specific follow-through bonus
else:
    cap at Yellow or route to 4C
```

Green lateness ratios:

|case|Stage2_Actionable_entry|Stage3_Green_proxy|peak|green_lateness_ratio|interpretation|
|---|---:|---:|---:|---:|---|
|310210|36600|110600|123500|0.852|Green too late; C24 follow-through bonus useful|
|220100|14850|30900|31150|0.985|Green near peak; keep Yellow until stronger evidence|
|365270|not applicable|not applicable|9010|not_applicable|4C route|
|288330|6040|not applicable|7500|not_applicable|local bounce false positive|

## 15. 4B Local vs Full-window Timing Audit

|trigger_id|4B evidence type|local proximity|full-window proximity|verdict|
|---|---|---:|---:|---|
|R7L15-C24-310210-T2|valuation_blowoff, positioning_overheat|0.95|0.95|good_full_window_4B_timing|
|R7L15-C24-220100-T2|valuation_blowoff, positioning_overheat|0.98|0.98|good_full_window_4B_timing|
|R7L15-C24-365270-T1|hard 4C; no 4B required|null|null|hard_4C_overrides_4B|
|R7L15-C24-288330-T1|local bounce after damaged program|null|null|false_positive_local_bounce_not_full_recovery|

## 16. 4C Protection Audit

|case|4C label|post-event MAE90|protection interpretation|
|---|---|---:|---|
|365270|hard_4c_success|-39.31|4C routing protects against the bulk of downside after trial-data disappointment.|
|288330|thesis_break_watch_to_4c|-41.23|Program reset should not wait for prolonged price confirmation.|
|310210|not applicable|-7.38|Positive data path; no hard 4C.|
|220100|not applicable|-9.02|Positive but later 4B risk, not 4C.|

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_name = L7_bio_trial_data_requires_data_quality_and_follow_through
candidate_delta = shadow_only
```

Mechanism: in biotech, an event is like opening a sealed lab result. The market does not only ask “was there a headline?” It asks whether the result can travel through the corridor from data → regulator/partner → commercial economics. If that corridor is visible, Stage2/Yellow can move forward. If the corridor collapses, the same event becomes a trapdoor and should route to 4C.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
candidate_rules =
  1. C24_trial_data_quality_follow_through_bonus
  2. C24_trial_failure_or_endpoint_disappointment_to_4C
  3. C24_local_bounce_after_program_reset_guard
```

This is not a global rule. It should not affect order backlog, grid equipment, consumer export, or financial capital-return archetypes.

## 19. Before / After Backtest Comparison

|profile_id|scope|changed_axes|eligible_triggers|avg_MFE90|avg_MAE90|false_positive_rate|late_green|verdict|
|---|---|---|---:|---:|---:|---:|---:|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|current_global_proxy|existing axes only|4|76.19|-24.23|0.25|2|mixed: false positive on 288330 and late on 310210|
|P0b_e2r_2_0_baseline_reference|rollback_reference|legacy baseline|4|76.19|-24.23|0.5|0|worse: promotes 288330/365270-style event risk too easily|
|P1_L7_bio_trial_event_shadow_profile|sector_specific|C24_data_quality_bridge_bonus + hard_trial_failure_4C|4|76.19|-24.23|0.0|1|better: separates 310210/220100 from 365270/288330|
|P2_C24_trial_data_candidate_profile|canonical_archetype_specific|trial_data_follow_through_bonus + local_bounce_guard|4|76.19|-24.23|0.0|1|best fit for this loop|
|P3_C24_counterexample_guard_profile|canonical_archetype_specific|hard_trial_failure_to_4C + program_reset_penalty|4|76.19|-24.23|0.0|0|best risk guard|

## 20. Score-Return Alignment Matrix

|case|P0 score label|P2 shadow label|MFE90|MAE90|alignment|
|---|---|---|---:|---:|---|
|310210|Stage3-Yellow|Stage3-Green candidate|189.07|-7.38|shadow improves missed structural|
|220100|Stage3-Yellow|Stage3-Yellow keep|88.55|-9.02|shadow avoids peak Green|
|365270|Stage2-Watch late 4C|4C|2.97|-39.31|shadow improves downside protection|
|288330|Stage2-Actionable false positive|Stage2-Watch/4C-risk|24.17|-41.23|shadow reduces false positive|

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
|L7_BIO_HEALTHCARE_MEDICAL|C24_BIO_TRIAL_DATA_EVENT_RISK|ONCOLOGY_CLINICAL_DATA_EVENT_BINARY_RISK_AND_DURABLE_SIGNAL_GATE|2|2|2|2|4|0|6|4|3|true|true|C24 now has additional non-duplicative trial-data positives and hard-failure counterexamples; next gap is C25 device/export reimbursement.|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
positive_case_count: 2
counterexample_count: 2
current_profile_error_count: 3
tested_existing_calibrated_axes:
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - trial_data_follow_through_missed_structural
  - trial_failure_4C_too_late
  - local_bounce_false_positive
  - 4B_after_data_rerating_needed
new_axis_proposed:
  - C24_trial_data_quality_follow_through_bonus
  - C24_trial_failure_or_endpoint_disappointment_to_4C
  - C24_local_bounce_after_program_reset_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: R7/L7 C24 needed additional non-duplicative trial-data positive/counterexample rows
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date and source fields
- actual stock-web tradable OHLC rows for all representative triggers
- entry_date / entry_price from c column
- 30D / 90D / 180D MFE and MAE research-proxy calculations
- duplicate avoidance versus local prior C24 artifacts
- shadow-only sector/canonical rule framing
```

Not validated:

```text
- live candidate status
- current 2026 investability
- broker/order execution
- production scoring code
- exact repository implementation structure
- legal/regulatory interpretation beyond public event-family summary
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C24_trial_data_quality_follow_through_bonus,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,+2,+2,"Clinical-data events that keep accumulating through repeat high-volume rows and visible clinical/economic route should be promoted earlier than pure one-day event spikes.","Reduces missed structural on 310210 while keeping 220100 Yellow until Green-quality evidence closes.","R7L15-C24-310210-T1|R7L15-C24-220100-T1",4,4,2,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,C24_trial_failure_or_endpoint_disappointment_to_4C,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,+1,+1,"Hard trial-data disappointment / endpoint ambiguity with large immediate MAE should route to 4C rather than slow watch.","Correctly handles 365270 and lowers false positive survival of failed event thesis.","R7L15-C24-365270-T1",4,4,2,medium,archetype_shadow_only,"not production; thesis-break protection"
shadow_weight,C24_local_bounce_after_program_reset_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,+1,+1,"Local bounce after a damaged clinical program should not count as durable Stage2/3 evidence.","Reduces 288330-style false positives where MFE exists but MAE and drawdown dominate.","R7L15-C24-288330-T1",4,4,2,medium,archetype_shadow_only,"not production; local-bounce guard"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "source_name": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546, "markets": ["KONEX", "KOSDAQ", "KOSDAQ GLOBAL", "KOSPI"], "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R7L15-C24-310210-VORONOI-VRN11-DATA-20240524", "symbol": "310210", "company_name": "보로노이", "round": "R7", "loop": "15", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ONCOLOGY_CLINICAL_DATA_EVENT_BINARY_RISK_AND_DURABLE_SIGNAL_GATE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R7L15-C24-310210-T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "strong_positive_alignment", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Trial-data/pipeline evidence with repeated post-event bid converted into durable rerating; the case argues for C24-specific data-quality + follow-through bonus, not global Green loosening."}
{"row_type": "case", "case_id": "R7L15-C24-220100-FUTURECHEM-RADIOPHARMA-DATA-20240522", "symbol": "220100", "company_name": "퓨쳐켐", "round": "R7", "loop": "15", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ONCOLOGY_CLINICAL_DATA_EVENT_BINARY_RISK_AND_DURABLE_SIGNAL_GATE", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "R7L15-C24-220100-T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_but_4b_needed", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Radiopharma/prostate-cancer data-commercial optionality produced large MFE, but the later 4B/positioning drawdown shows why C24 Green should wait for durable evidence, not one presentation."}
{"row_type": "case", "case_id": "R7L15-C24-365270-CURACLE-CU06-DME-DATA-20240522", "symbol": "365270", "company_name": "큐라클", "round": "R7", "loop": "15", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ONCOLOGY_CLINICAL_DATA_EVENT_BINARY_RISK_AND_DURABLE_SIGNAL_GATE", "case_type": "4C_success", "positive_or_counterexample": "counterexample", "best_trigger": "R7L15-C24-365270-T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "hard_counterexample_alignment", "current_profile_verdict": "current_profile_4C_too_late", "price_source": "Songdaiki/stock-web", "notes": "Data disappointment / endpoint-risk case. Entry already had event shock and then suffered large MAE with little recoverable MFE; hard 4C routing should be immediate."}
{"row_type": "case", "case_id": "R7L15-C24-288330-BRIDGEBIO-BBT877-RESET-20230623", "symbol": "288330", "company_name": "브릿지바이오테라퓨틱스", "round": "R7", "loop": "15", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ONCOLOGY_CLINICAL_DATA_EVENT_BINARY_RISK_AND_DURABLE_SIGNAL_GATE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R7L15-C24-288330-T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "failed_rerating_alignment", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Clinical program reset / execution-risk case. Short local bounce did not repair the structural damage; C24 should punish program discontinuity or data-quality ambiguity even when price bounces."}
{"row_type": "trigger", "trigger_id": "R7L15-C24-310210-T1", "case_id": "R7L15-C24-310210-VORONOI-VRN11-DATA-20240524", "symbol": "310210", "company_name": "보로노이", "round": "R7", "loop": "15", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ONCOLOGY_CLINICAL_DATA_EVENT_BINARY_RISK_AND_DURABLE_SIGNAL_GATE", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "bio_trial_data_event_risk", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|green_strictness_stress_test|4C_thesis_break_timing_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-24", "entry_date": "2024-05-24", "entry_price": 36600, "evidence_available_at_that_date": "VRN11 / oncology-pipeline clinical-data catalyst became public enough for market reaction; subsequent rows show repeated accumulation rather than one-day price-only spike.", "evidence_source": "public clinical-data/news-flow summary; stock-web OHLC rows for 310210 2024/2025", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/310/310210/2024.csv; atlas/ohlcv_tradable_by_symbol_year/310/310210/2025.csv", "profile_path": "atlas/symbol_profiles/310/310210.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 72.68, "MFE_90D_pct": 189.07, "MFE_180D_pct": 237.43, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.38, "MAE_90D_pct": -7.38, "MAE_180D_pct": -7.38, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": false, "peak_date": "2025-02-17", "peak_price": 123500, "drawdown_after_peak_pct": -14.25, "green_lateness_ratio": 0.852, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L15-C24-310210-2024-05-24", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R7L15-C24-310210-T2", "case_id": "R7L15-C24-310210-VORONOI-VRN11-DATA-20240524", "symbol": "310210", "company_name": "보로노이", "round": "R7", "loop": "15", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ONCOLOGY_CLINICAL_DATA_EVENT_BINARY_RISK_AND_DURABLE_SIGNAL_GATE", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "bio_trial_data_event_risk", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|green_strictness_stress_test|4C_thesis_break_timing_test|coverage_gap_fill", "trigger_type": "Stage4B-Overlay", "trigger_date": "2025-02-17", "entry_date": "2025-02-17", "entry_price": 121400, "evidence_available_at_that_date": "Late-cycle valuation/positioning overheat after multi-month data rerating; no thesis break, but upside capture had already occurred.", "evidence_source": "stock-web OHLC path; overlay-only timing row", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/310/310210/2025.csv", "profile_path": "atlas/symbol_profiles/310/310210.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.61, "MFE_90D_pct": 26.03, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -12.77, "MAE_90D_pct": -15.24, "MAE_180D_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-03-10", "peak_price": 153000, "drawdown_after_peak_pct": -28.76, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.95, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": null, "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 90, "calibration_block_reasons": [], "corporate_action_window_status": "clean_90D_window", "same_entry_group_id": "R7L15-C24-310210-2025-02-17", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R7L15-C24-220100-T1", "case_id": "R7L15-C24-220100-FUTURECHEM-RADIOPHARMA-DATA-20240522", "symbol": "220100", "company_name": "퓨쳐켐", "round": "R7", "loop": "15", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ONCOLOGY_CLINICAL_DATA_EVENT_BINARY_RISK_AND_DURABLE_SIGNAL_GATE", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "bio_trial_data_event_risk", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|green_strictness_stress_test|4C_thesis_break_timing_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-22", "entry_date": "2024-05-22", "entry_price": 14850, "evidence_available_at_that_date": "Radiopharma/prostate-cancer clinical-data and commercialization optionality became visible; price path shows multi-month rerating but later severe 4B drawdown.", "evidence_source": "public clinical-data/news-flow summary; stock-web OHLC rows for 220100 2024/2025", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/220/220100/2024.csv; atlas/ohlcv_tradable_by_symbol_year/220/220100/2025.csv", "profile_path": "atlas/symbol_profiles/220/220100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 22.56, "MFE_90D_pct": 88.55, "MFE_180D_pct": 109.76, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.02, "MAE_90D_pct": -9.02, "MAE_180D_pct": -9.02, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-15", "peak_price": 31150, "drawdown_after_peak_pct": -51.85, "green_lateness_ratio": 0.62, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "high_mae_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L15-C24-220100-2024-05-22", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R7L15-C24-220100-T2", "case_id": "R7L15-C24-220100-FUTURECHEM-RADIOPHARMA-DATA-20240522", "symbol": "220100", "company_name": "퓨쳐켐", "round": "R7", "loop": "15", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ONCOLOGY_CLINICAL_DATA_EVENT_BINARY_RISK_AND_DURABLE_SIGNAL_GATE", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "bio_trial_data_event_risk", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|green_strictness_stress_test|4C_thesis_break_timing_test|coverage_gap_fill", "trigger_type": "Stage4B-Overlay", "trigger_date": "2024-10-15", "entry_date": "2024-10-15", "entry_price": 30900, "evidence_available_at_that_date": "Post-data rerating reached valuation/positioning overheat. The follow-on drawdown argues for 4B overlay near the full-window peak.", "evidence_source": "stock-web OHLC path; overlay-only timing row", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/220/220100/2024.csv", "profile_path": "atlas/symbol_profiles/220/220100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.13, "MFE_90D_pct": 1.13, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -37.15, "MAE_90D_pct": -51.46, "MAE_180D_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-16", "peak_price": 31250, "drawdown_after_peak_pct": -52.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": null, "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 90, "calibration_block_reasons": [], "corporate_action_window_status": "clean_90D_window", "same_entry_group_id": "R7L15-C24-220100-2024-10-15", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R7L15-C24-365270-T1", "case_id": "R7L15-C24-365270-CURACLE-CU06-DME-DATA-20240522", "symbol": "365270", "company_name": "큐라클", "round": "R7", "loop": "15", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ONCOLOGY_CLINICAL_DATA_EVENT_BINARY_RISK_AND_DURABLE_SIGNAL_GATE", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "bio_trial_data_event_risk", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|green_strictness_stress_test|4C_thesis_break_timing_test|coverage_gap_fill", "trigger_type": "4C", "trigger_date": "2024-05-22", "entry_date": "2024-05-22", "entry_price": 8750, "evidence_available_at_that_date": "CU06/DME data-risk shock: the event failed to supply a durable clinical/commercial bridge and immediately broke the prior event thesis.", "evidence_source": "public trial-data/news-flow summary; stock-web OHLC rows for 365270 2024", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["explicit_event_cap"], "stage4c_evidence_fields": ["safety_or_trial_failure", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/365/365270/2024.csv", "profile_path": "atlas/symbol_profiles/365/365270.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.97, "MFE_90D_pct": 2.97, "MFE_180D_pct": 2.97, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -35.66, "MAE_90D_pct": -39.31, "MAE_180D_pct": -41.37, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-22", "peak_price": 9010, "drawdown_after_peak_pct": -43.06, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "hard_4C_overrides_4B", "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4C_success", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L15-C24-365270-2024-05-22", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R7L15-C24-288330-T1", "case_id": "R7L15-C24-288330-BRIDGEBIO-BBT877-RESET-20230623", "symbol": "288330", "company_name": "브릿지바이오테라퓨틱스", "round": "R7", "loop": "15", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ONCOLOGY_CLINICAL_DATA_EVENT_BINARY_RISK_AND_DURABLE_SIGNAL_GATE", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "bio_trial_data_event_risk", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|green_strictness_stress_test|4C_thesis_break_timing_test|coverage_gap_fill", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2023-06-23", "entry_date": "2023-06-23", "entry_price": 6040, "evidence_available_at_that_date": "Clinical-program reset / execution-risk event left only a local rebound. The data/program quality did not close into a durable Stage3 route.", "evidence_source": "public clinical-program/news-flow summary; stock-web OHLC rows for 288330 2023", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "legal_or_contract_risk_score"], "stage4c_evidence_fields": ["qualification_failure", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/288/288330/2023.csv", "profile_path": "atlas/symbol_profiles/288/288330.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 18.71, "MFE_90D_pct": 24.17, "MFE_180D_pct": 24.17, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -31.29, "MAE_90D_pct": -41.23, "MAE_180D_pct": -56.79, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-08-10", "peak_price": 7500, "drawdown_after_peak_pct": -65.2, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "false_positive_local_bounce_not_full_recovery", "four_b_evidence_type": ["execution_risk_score"], "four_c_protection_label": "thesis_break_watch_to_4c", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L15-C24-288330-2023-06-23", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L15-C24-310210-VORONOI-VRN11-DATA-20240524", "trigger_id": "R7L15-C24-310210-T1", "symbol": "310210", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 3, "margin_bridge_score": 3, "revision_score": 6, "relative_strength_score": 9, "customer_quality_score": 6, "policy_or_regulatory_score": 6, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 4, "margin_bridge_score": 4, "revision_score": 7, "relative_strength_score": 9, "customer_quality_score": 7, "policy_or_regulatory_score": 7, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "trial_data_quality_score": 9, "follow_through_score": 10}, "weighted_score_after": 89, "stage_label_after": "Stage3-Green", "changed_components": ["trial_data_quality_score", "follow_through_score"], "component_delta_explanation": "C24-specific follow-through after clinical data supports earlier Green without lowering the global threshold.", "MFE_90D_pct": 189.07, "MAE_90D_pct": -7.38, "score_return_alignment_label": "aligned_after_shadow", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L15-C24-220100-FUTURECHEM-RADIOPHARMA-DATA-20240522", "trigger_id": "R7L15-C24-220100-T1", "symbol": "220100", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 3, "margin_bridge_score": 3, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 5, "policy_or_regulatory_score": 7, "valuation_repricing_score": 7, "execution_risk_score": 4, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 3, "margin_bridge_score": 3, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 6, "policy_or_regulatory_score": 7, "valuation_repricing_score": 7, "execution_risk_score": 4, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "trial_data_quality_score": 7, "commercialization_optionality_score": 7}, "weighted_score_after": 82, "stage_label_after": "Stage3-Yellow", "changed_components": ["trial_data_quality_score", "commercialization_optionality_score"], "component_delta_explanation": "Positive, but later 4B drawdown argues against automatic Green from one clinical-data event.", "MFE_90D_pct": 88.55, "MAE_90D_pct": -9.02, "score_return_alignment_label": "aligned_after_shadow", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L15-C24-365270-CURACLE-CU06-DME-DATA-20240522", "trigger_id": "R7L15-C24-365270-T1", "symbol": "365270", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 4, "customer_quality_score": 1, "policy_or_regulatory_score": 4, "valuation_repricing_score": 3, "execution_risk_score": 8, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 64, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 1, "customer_quality_score": 0, "policy_or_regulatory_score": 2, "valuation_repricing_score": 1, "execution_risk_score": 10, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "trial_failure_score": 10, "thesis_break_score": 10}, "weighted_score_after": 42, "stage_label_after": "4C", "changed_components": ["trial_failure_score", "thesis_break_score", "execution_risk_score"], "component_delta_explanation": "Hard trial-data disappointment should route to 4C immediately rather than waiting for price confirmation.", "MFE_90D_pct": 2.97, "MAE_90D_pct": -39.31, "score_return_alignment_label": "guard_needed", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L15-C24-288330-BRIDGEBIO-BBT877-RESET-20230623", "trigger_id": "R7L15-C24-288330-T1", "symbol": "288330", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 1, "margin_bridge_score": 1, "revision_score": 2, "relative_strength_score": 5, "customer_quality_score": 2, "policy_or_regulatory_score": 4, "valuation_repricing_score": 3, "execution_risk_score": 7, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 1, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 3, "customer_quality_score": 1, "policy_or_regulatory_score": 3, "valuation_repricing_score": 2, "execution_risk_score": 9, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 1, "accounting_trust_risk_score": 0, "program_reset_penalty": 10, "local_bounce_guard_score": 9}, "weighted_score_after": 50, "stage_label_after": "Stage2-Watch/4C-Risk", "changed_components": ["program_reset_penalty", "local_bounce_guard_score", "execution_risk_score"], "component_delta_explanation": "Local rebound after program reset should not be treated as structural rerating.", "MFE_90D_pct": 24.17, "MAE_90D_pct": -41.23, "score_return_alignment_label": "guard_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R7", "loop": "15", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_canonical_archetype_count": 0, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 3, "diversity_score_summary": "avg 21.0; new symbols 4, counterexamples 2, 4B/4C paths 3, no reused triggers", "tested_existing_calibrated_axes": ["stage3_green_total_min", "stage3_green_revision_min", "stage3_cross_evidence_green_buffer", "price_only_blowoff_blocks_positive_stage", "hard_4c_thesis_break_routes_to_4c", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["trial_data_follow_through_missed_structural", "trial_failure_4C_too_late", "local_bounce_false_positive", "4B_after_data_rerating_needed"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "auto_selected_coverage_gap": "R7/L7 C24 needed additional non-duplicative trial-data positive/counterexample rows after R7 loop11 and R13 C24 holdouts"}
```

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C24_trial_data_quality_follow_through_bonus,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,+2,+2,"Clinical-data events that keep accumulating through repeat high-volume rows and visible clinical/economic route should be promoted earlier than pure one-day event spikes.","Reduces missed structural on 310210 while keeping 220100 Yellow until Green-quality evidence closes.","R7L15-C24-310210-T1|R7L15-C24-220100-T1",4,4,2,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,C24_trial_failure_or_endpoint_disappointment_to_4C,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,+1,+1,"Hard trial-data disappointment / endpoint ambiguity with large immediate MAE should route to 4C rather than slow watch.","Correctly handles 365270 and lowers false positive survival of failed event thesis.","R7L15-C24-365270-T1",4,4,2,medium,archetype_shadow_only,"not production; thesis-break protection"
shadow_weight,C24_local_bounce_after_program_reset_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,+1,+1,"Local bounce after a damaged clinical program should not count as durable Stage2/3 evidence.","Reduces 288330-style false positives where MFE exists but MAE and drawdown dominate.","R7L15-C24-288330-T1",4,4,2,medium,archetype_shadow_only,"not production; local-bounce guard"
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
next_round = R7_loop_16_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
reason = C24 now has added non-duplicative trial-data positives and counterexamples; next L7 gap is C25 device/export/reimbursement coverage.
```

## 28. Source Notes

- Stock-web manifest and shard paths were inspected directly in this session.
- Key OHLC validation rows came from stock-web shards for 310210, 220100, 365270, and 288330.
- Symbol profile inspection confirmed active/history rows and clean windows for the representative cases.
- Evidence labels are historical event-family summaries. They are used for calibration research, not for live recommendation or legal/regulatory interpretation.

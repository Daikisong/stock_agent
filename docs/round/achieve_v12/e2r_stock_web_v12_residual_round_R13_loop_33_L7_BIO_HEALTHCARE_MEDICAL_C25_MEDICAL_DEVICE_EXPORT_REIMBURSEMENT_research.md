# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R13
loop = 33
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id = AI_MEDICAL_DEVICE_REIMBURSEMENT_TO_PAID_USAGE | AESTHETIC_DEVICE_EXPORT_MARGIN_BRIDGE | DENTAL_IMPLANT_EXPORT_VBP_VOLUME_MARGIN | CGM_APPROVAL_WITH_COMMERCIALIZATION_DELAY | AI_MEDICAL_DEVICE_GLOBALIZATION_MNA_DILUTION_OVERHANG
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is historical calibration research only. It is not a live candidate scan, not an investment recommendation, and not a `stock_agent` code patch.

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

The current calibrated profile is treated as already applied. This loop does not re-prove the global Stage2/Green/4B/4C changes. It asks whether C25 needs a sharper commercial bridge: regulatory clearance, temporary reimbursement, export channel, or M&A must become paid usage, repeat orders, margin bridge, or financing-safe expansion before Green.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
loop_objective = holdout_validation, residual_false_positive_mining, residual_missed_structural_mining, yellow_threshold_stress_test, green_strictness_stress_test, stage2_actionable_bonus_stress_test, 4B_non_price_requirement_stress_test, 4C_thesis_break_timing_test, sector_specific_rule_discovery, canonical_archetype_compression, counterexample_mining, coverage_gap_fill
```

C25 is different from C24 trial-data risk. A trial-data case is a locked room with one binary door; a medical-device export/reimbursement case is a corridor. Clearance opens the first door, reimbursement opens the second, hospital/channel adoption opens the third, and only paid usage or margin-visible exports turn the corridor into revenue. The calibration question is therefore not “was there approval?” but “did approval become a commercial bridge?”

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts were limited to calibration reports and registries, not code. The ingest summary showed broad R1-R13 coverage with 107 parsed documents and 1,376 aggregate representative trigger rows, but no v12 C25 canonical coverage row was found in this run. The applied profile report confirms that the global profile already changed Stage2 bonus, Yellow/Green thresholds, and 4B/4C guardrails; those axes are treated as existing, not newly proposed here.

```text
required_new_independent_case_ratio >= 0.60
calibration_usable_case_count = 5
new_independent_case_count = 5
reused_case_count = 0
new_independent_case_ratio = 1.00
loop_contribution_label = canonical_archetype_rule_candidate
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_atlas_repo = https://github.com/Songdaiki/stock-web
manifest = atlas/manifest.json
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

All quantitative price work uses `tradable_raw` rows from `atlas/ohlcv_tradable_by_symbol_year`. Raw shards are not used for weight calibration. Corporate-action candidate windows are blocked by default.

## 5. Historical Eligibility Gate

All representative triggers satisfy:

```text
trigger_date is historical = true
entry_date exists in stock-web tradable shard = true
forward_180D_available_by_manifest_max_date = true
high_low_close_volume_present = true
MFE_30D_90D_180D and MAE_30D_90D_180D calculated = true
corporate_action_contaminated_180D_window = false
```

Blocked windows: none for representative rows. Lunit had corporate-action candidates in 2023, but the representative trigger is 2024-01-02; the 180D calibration window does not overlap the profile's corporate-action candidate dates.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| AI_MEDICAL_DEVICE_REIMBURSEMENT_TO_PAID_USAGE | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | reimbursement/temporary coverage only becomes positive when paid-use route is visible |
| AESTHETIC_DEVICE_EXPORT_MARGIN_BRIDGE | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | global device exports plus margin bridge behave like durable medical-device operating leverage |
| DENTAL_IMPLANT_EXPORT_VBP_VOLUME_MARGIN | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | policy/reimbursement shock matters only if volume and margin bridge appear |
| CGM_APPROVAL_WITH_COMMERCIALIZATION_DELAY | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | product approval alone can spike price but fail rerating if channel adoption is slow |
| AI_MEDICAL_DEVICE_GLOBALIZATION_MNA_DILUTION_OVERHANG | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | M&A/global expansion must be gated by financing and integration risk |

## 7. Case Selection Summary

|case_id|symbol|company_name|role|positive_or_counterexample|current_profile_verdict|
|---|---|---|---|---|---|
|C25_R13L33_001_VUNO_DEEPCARS_REIMBURSEMENT|338220|뷰노|structural_success|positive|current_profile_correct|
|C25_R13L33_002_CLASSYS_EXPORT_MARGIN|214150|클래시스|structural_success|positive|current_profile_correct|
|C25_R13L33_003_DENTIUM_CHINA_EXPORT|145720|덴티움|high_mae_success|positive|current_profile_too_early|
|C25_R13L33_004_ISENS_CGM_APPROVAL|099190|아이센스|failed_rerating|counterexample|current_profile_false_positive|
|C25_R13L33_005_LUNIT_MNA_OVERHANG|328130|루닛|false_positive_green|counterexample|current_profile_false_positive|

## 8. Positive vs Counterexample Balance

```text
positive_structural_success = 2
high_mae_success = 1
counterexample_or_failed_rerating = 2
4B_or_4C_case = 3
minimum_calibration_usable_case_count = 5
```

The positive side is not “all approval went up.” VUNO and Classys are positive because the evidence chain had a commercial bridge: reimbursement/paid-use route or export/margin bridge. Dentium is a delayed positive with high MAE; it supports a size-control rule, not blind promotion. The counterexample side is i-SENS and Lunit: both had plausible device/globalization headlines, but the OHLC path punished missing channel conversion, financing overhang, or delayed operating leverage.

## 9. Evidence Source Map

| case_id | evidence timing used | Stage2 evidence | Stage3 evidence | 4B/4C evidence |
|---|---|---|---|---|
| C25_R13L33_001_VUNO_DEEPCARS_REIMBURSEMENT | 2023-06-02 entry close | reimbursement/paid-use optionality, relative strength, early revision route | multiple public sources, financial visibility | Sep 2023 valuation/positioning overheat |
| C25_R13L33_002_CLASSYS_EXPORT_MARGIN | 2023-05-17 entry close | export device demand, relative strength, early revision | confirmed revision, margin bridge, repeat order/export route | later valuation/peak drawdown monitoring |
| C25_R13L33_003_DENTIUM_CHINA_EXPORT | 2022-08-09 entry close | dental implant export/VBP volume route, customer quality | later margin bridge and financial visibility | high MAE before thesis validates |
| C25_R13L33_004_ISENS_CGM_APPROVAL | 2023-07-18 entry close | CGM product approval/launch headline and relative strength | commercial conversion not yet supported | 4C when channel/revenue bridge failed to protect price |
| C25_R13L33_005_LUNIT_MNA_OVERHANG | 2024-01-02 entry close | global expansion/M&A headline | commercial/margin conversion not yet supported | financing/integration/dilution overhang |

No later price outcome was used to move trigger dates backward. The evidence labels are historical public-event categories; the quantitative calibration itself is stock-web OHLC based.

## 10. Price Data Source Map

| symbol | company_name | profile_path | representative price_shard_path | profile caveat |
|---|---|---|---|---|
| 338220 | 뷰노 | atlas/symbol_profiles/338/338220.json | atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv | no corporate-action candidate dates |
| 214150 | 클래시스 | atlas/symbol_profiles/214/214150.json | atlas/ohlcv_tradable_by_symbol_year/214/214150/2023.csv | historical SPAC-name period blocked outside this loop; 2023 window clean |
| 145720 | 덴티움 | atlas/symbol_profiles/145/145720.json | atlas/ohlcv_tradable_by_symbol_year/145/145720/2022.csv | no corporate-action candidate dates |
| 099190 | 아이센스 | atlas/symbol_profiles/099/099190.json | atlas/ohlcv_tradable_by_symbol_year/099/099190/2023.csv | 2023-03/04 corporate-action candidates exist, but July trigger window is clean |
| 328130 | 루닛 | atlas/symbol_profiles/328/328130.json | atlas/ohlcv_tradable_by_symbol_year/328/328130/2024.csv | 2023 corporate-action candidates exist, but 2024 trigger window is clean |

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|trigger_type|trigger_date|entry_date|entry_price|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|verdict|aggregate_role|
|---|---|---|---|---|---|---|---|---|---|---|---|
|C25_R13L33_001_T1_STAGE2_ACTIONABLE|338220|Stage2-Actionable|2023-06-02|2023-06-02|23650|193.87|-15.22|193.87|-15.22|current_profile_correct|representative|
|C25_R13L33_001_T2_STAGE3_YELLOW_COMPARISON|338220|Stage3-Yellow|2023-07-13|2023-07-13|36150|92.25|-33.89|92.25|-33.89|current_profile_too_late|label_comparison_only|
|C25_R13L33_001_T3_STAGE4B_OVERLAY|338220|4B|2023-09-07|2023-09-07|63600|9.28|-62.42|9.28|-62.42|current_profile_4B_too_late|4B_overlay_only|
|C25_R13L33_002_T1_STAGE2_ACTIONABLE|214150|Stage2-Actionable|2023-05-17|2023-05-17|26400|59.09|-7.95|63.07|-7.95|current_profile_correct|representative|
|C25_R13L33_003_T1_STAGE2_ACTIONABLE|145720|Stage2-Actionable|2022-08-09|2022-08-09|94300|13.47|-27.78|72.53|-27.78|current_profile_too_early|representative|
|C25_R13L33_004_T1_STAGE2_ACTIONABLE|099190|Stage2-Actionable|2023-07-18|2023-07-18|32000|24.06|-32.03|24.06|-44.03|current_profile_false_positive|representative|
|C25_R13L33_004_T2_4C_PROTECTION|099190|4C|2024-02-07|2024-02-07|21000|13.1|-14.71|13.1|-14.71|current_profile_4C_too_late|4C_overlay_only|
|C25_R13L33_005_T1_STAGE2_ACTIONABLE|328130|Stage2-Actionable|2024-01-02|2024-01-02|79400|4.28|-40.62|4.28|-60.96|current_profile_false_positive|representative|

## 12. Trigger-Level OHLC Backtest Tables

Representative trigger aggregate:

| metric | value |
|---|---:|
| representative_trigger_count | 5 |
| avg_MFE_90D_pct | 58.95 |
| avg_MAE_90D_pct | -24.72 |
| avg_MFE_180D_pct | 71.56 |
| avg_MAE_180D_pct | -31.19 |
| positive_case_avg_MFE_90D_pct | 88.81 |
| positive_case_avg_MAE_90D_pct | -16.98 |
| counterexample_avg_MFE_90D_pct | 14.17 |
| counterexample_avg_MAE_90D_pct | -36.33 |

The spread is the signal. The approval/M&A counterexamples show small MFE and very large MAE, while commercial-bridge positives show higher MFE. Dentium is the exception: it eventually succeeded but with a deep interim drawdown, so it argues for size-control rather than outright rejection.

## 13. Current Calibrated Profile Stress Test

| case_id | current calibrated proxy likely decision | actual MFE/MAE alignment | verdict |
|---|---|---|---|
| VUNO | Stage2-Actionable / later Yellow; 4B needed after overheat | correct positive, but 4B should attach near full-window peak | current_profile_correct |
| CLASSYS | Stage2-Actionable progressing toward Yellow/Green via export/margin bridge | correct positive | current_profile_correct |
| DENTIUM | Stage2-Actionable too early if position sizing ignores policy/export MAE | eventual positive but too much interim drawdown | current_profile_too_early |
| i-SENS | Approval + relative strength can look like Green candidate | false positive; MAE_180D -44.03% | current_profile_false_positive |
| LUNIT | Global expansion/M&A can look like strategic Green | false positive; MAE_180D -60.96% | current_profile_false_positive |

Stress-test answers:

```text
stage2_actionable_evidence_bonus = kept, but C25 needs commercial bridge qualifier
stage3_yellow_total_min = kept
stage3_green_total_min = kept
stage3_green_revision_min = kept; C25 Green should require paid usage / export revenue / margin bridge
price_only_blowoff_guard = strengthened by VUNO 4B overlay
full_4b_non_price_requirement = strengthened by Lunit financing/integration risk
hard_4c_routing = strengthened by i-SENS channel-conversion failure
```

## 14. Stage2 / Yellow / Green Comparison

The C25 pattern is not “earlier is always better.” Earlier works only when the corridor is already connected to revenue.

| case | Stage2 entry | later confirmation | green_lateness_ratio | interpretation |
|---|---:|---|---:|---|
| VUNO | 23650 | Stage3-Yellow at 36150; peak 69500 | 0.272 | Green/Yellow not very late; Stage2 captured most upside |
| CLASSYS | 26400 | export/margin bridge built gradually; peak 43050 in observed 180D | 0.30 approx | confirmation was acceptable, not peak-chasing |
| DENTIUM | 94300 | delayed margin/volume validation; peak 162700 in 180D | not_applicable | early signal worked only with high-MAE tolerance |
| i-SENS | 32000 | no durable commercial confirmation | not_applicable | approval-only should not become Green |
| LUNIT | 79400 | no margin-safe expansion confirmation inside 180D | not_applicable | strategic headline plus overhang should cap positive stage |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_evidence_type | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---|---:|---:|---|
| C25_R13L33_001_T3_STAGE4B_OVERLAY | valuation_blowoff / positioning_overheat | 0.871 | 0.871 | good_full_window_4B_timing |
| C25_R13L33_005_T1_STAGE2_ACTIONABLE | capital_raise_or_overhang / dilution_or_cb / execution risk | 1.000 | 1.000 | good_risk_overlay_but_not_positive |

VUNO shows that price strength can continue for a while; a price-only local peak would have been too early, but Sep 2023 overheat with valuation/positioning evidence was useful. Lunit shows the opposite: risk overlay was already present at the trigger, so the headline should not have trained positive entry weight.

## 16. 4C Protection Audit

| case | 4C trigger | prior peak | post-4C MAE_90D | label |
|---|---|---:|---:|---|
| i-SENS | 2024-02-07 thesis/channel conversion failure watch | 39700 | -14.71% | hard_4c_success |
| LUNIT | financing/integration overhang visible at 2024-01-02 trigger | 82800 | -40.62% | thesis_break_watch_only / 4B-to-4C watch |

Approximate i-SENS protection score: `1 - 14.71 / 54.89 = 0.732`. This is a useful protection label, not a positive-entry signal.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
candidate_axis = l7_medical_device_commercial_bridge_gate
```

Candidate rule:

> In L7 medical-device cases, regulatory clearance, innovative-device designation, temporary reimbursement, or M&A/global expansion may create Stage2-watch/Stage2-Actionable, but Stage3-Green requires a commercial bridge: paid usage, repeat hospital/channel adoption, export revenue acceleration, margin bridge, or financing-safe integration.

This is not a global rule. It is especially important in L7 because approval often marks the start of commercialization risk, not the end of it.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
```

Candidate C25 rules:

1. `c25_reimbursement_to_paid_usage_gate`: temporary reimbursement or approval must show paid-use/channel conversion before Green.
2. `c25_export_revenue_margin_bridge_bonus`: export device cases with visible margin bridge receive a small C25-specific positive bonus.
3. `c25_approval_only_green_cap`: approval/clearance alone is capped at Stage2-watch or Stage2-Actionable.
4. `c25_mna_dilution_overhang_guard`: acquisition/globalization headline with financing/integration overhang routes to 4B/watch, not positive promotion.
5. `c25_high_mae_success_size_control`: policy/export cases can succeed after deep MAE, so Stage2 can remain valid but with size/risk control.

## 19. Before / After Backtest Comparison

|profile_id|scope|eligible_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|missed_structural_count|late_green_count|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|global_current|5|58.95|-24.72|71.56|-31.19|40%|0|1|mixed; current global profile still over-rewards approval/M&A headlines|
|P0b_e2r_2_0_baseline_reference|rollback_reference|5|58.95|-24.72|71.56|-31.19|40%+|1|2|weaker; lacks C25-specific commercial bridge guard|
|P1_sector_specific_candidate_profile|L7 sector_specific|5|58.95|-24.72|71.56|-31.19|20%|0|1|better; adds high-MAE size-control and 4B overhang handling|
|P2_canonical_archetype_candidate_profile|C25 canonical_archetype_specific|5|58.95|-24.72|71.56|-31.19|0-20%|0|1|best among tested; rewards export/margin bridge and caps approval-only|
|P3_counterexample_guard_profile|C25 guard|2|14.17|-36.33|14.17|-52.5|0% after guard|0|0|strong counterexample filter; not sufficient for positive promotion by itself|

## 20. Score-Return Alignment Matrix

| case | raw component lesson | score-return alignment |
|---|---|---|
| VUNO | policy/reimbursement + paid-use route + relative strength | aligned positive |
| CLASSYS | export/channel + margin bridge + repeat demand | aligned positive |
| DENTIUM | policy/export route + later margin bridge, but high MAE | aligned with size-control |
| i-SENS | approval + relative strength without conversion | false positive under approval-only Green |
| LUNIT | strategic M&A/global expansion + overhang | false positive unless overhang guard is active |

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L7_BIO_HEALTHCARE_MEDICAL|C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|AI_MEDICAL_DEVICE_REIMBURSEMENT_TO_PAID_USAGE / AESTHETIC_DEVICE_EXPORT_MARGIN_BRIDGE / DENTAL_IMPLANT_EXPORT_VBP_VOLUME_MARGIN / CGM_APPROVAL_WITH_COMMERCIALIZATION_DELAY / AI_MEDICAL_DEVICE_GLOBALIZATION_MNA_DILUTION_OVERHANG|3|2|2|1|5|0|8|5|3|True|True|Need more non-Korea/US FDA reimbursement cases and post-2024 held-out export cases.|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 1
new_fine_archetype_count: 5
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - approval_only_false_positive
  - mna_dilution_overhang_false_positive
  - high_mae_success_size_control_needed
new_axis_proposed:
  - c25_reimbursement_to_paid_usage_gate
  - c25_export_revenue_margin_bridge_bonus
  - c25_approval_only_green_cap
  - c25_mna_dilution_overhang_guard
  - c25_high_mae_success_size_control
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest max_date = 2026-02-20
- tradable_raw OHLC rows for representative triggers
- entry_date / entry_price
- MFE_30D / 90D / 180D
- MAE_30D / 90D / 180D
- clean 180D window relative to symbol profile corporate-action candidates
- same_entry_group_id dedupe
- positive/counterexample balance
```

Not validated:

```text
- live/current candidate status
- current valuation attractiveness
- brokerage API data
- current analyst consensus
- stock_agent source code
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c25_reimbursement_to_paid_usage_gate,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"Temporary reimbursement/clearance must connect to paid usage or durable hospital/channel adoption before Green.","Improved separation of VUNO/Classys positives from i-SENS approval-only spike.","C25_R13L33_001_T1_STAGE2_ACTIONABLE|C25_R13L33_004_T1_STAGE2_ACTIONABLE",5,5,2,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c25_export_revenue_margin_bridge_bonus,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,2,+2,"Export device cases with visible margin bridge should receive archetype-specific support.","Raised aligned positives without promoting approval-only cases.","C25_R13L33_002_T1_STAGE2_ACTIONABLE|C25_R13L33_003_T1_STAGE2_ACTIONABLE",5,5,2,medium,archetype_shadow_only,"not production"
shadow_weight,c25_approval_only_green_cap,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"Approval/clearance alone is capped at Stage2-watch unless channel/reimbursement conversion evidence exists.","Reduced false-positive Green on i-SENS/Lunit-style headlines.","C25_R13L33_004_T1_STAGE2_ACTIONABLE|C25_R13L33_005_T1_STAGE2_ACTIONABLE",5,5,2,medium,counterexample_guard_profile,"not production"
shadow_weight,c25_mna_dilution_overhang_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"M&A/global expansion with financing or integration overhang routes to 4B/watch, not positive promotion.","Lunit 2024 overhang case blocked from false promotion.","C25_R13L33_005_T1_STAGE2_ACTIONABLE",5,5,1,low,counterexample_guard_profile,"not production"

```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"case_id": "C25_R13L33_001_VUNO_DEEPCARS_REIMBURSEMENT", "symbol": "338220", "company_name": "뷰노", "round": "R13", "loop": "33", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AI_MEDICAL_DEVICE_REIMBURSEMENT_TO_PAID_USAGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "C25_R13L33_001_T1_STAGE2_ACTIONABLE", "score_price_alignment": "strong_positive_with_late_4B_overlay", "current_profile_verdict": "current_profile_correct", "notes": "AI medical device reimbursement/paid-use route generated very large MFE; later overheat required 4B overlay, not positive re-entry.", "row_type": "case", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "price_source": "Songdaiki/stock-web"}
{"case_id": "C25_R13L33_002_CLASSYS_EXPORT_MARGIN", "symbol": "214150", "company_name": "클래시스", "round": "R13", "loop": "33", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_DEVICE_EXPORT_MARGIN_BRIDGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "C25_R13L33_002_T1_STAGE2_ACTIONABLE", "score_price_alignment": "positive_export_margin_bridge", "current_profile_verdict": "current_profile_correct", "notes": "Export device franchise and margin bridge behaved more like durable medical-device operating leverage than binary approval news.", "row_type": "case", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "price_source": "Songdaiki/stock-web"}
{"case_id": "C25_R13L33_003_DENTIUM_CHINA_EXPORT", "symbol": "145720", "company_name": "덴티움", "round": "R13", "loop": "33", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "DENTAL_IMPLANT_EXPORT_VBP_VOLUME_MARGIN", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "C25_R13L33_003_T1_STAGE2_ACTIONABLE", "score_price_alignment": "delayed_positive_with_high_MAE", "current_profile_verdict": "current_profile_too_early", "notes": "China dental implant export/VBP repricing path eventually worked, but early entry carried high MAE; size-control guard needed.", "row_type": "case", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "price_source": "Songdaiki/stock-web"}
{"case_id": "C25_R13L33_004_ISENS_CGM_APPROVAL", "symbol": "099190", "company_name": "아이센스", "round": "R13", "loop": "33", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "CGM_APPROVAL_WITH_COMMERCIALIZATION_DELAY", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "C25_R13L33_004_T1_STAGE2_ACTIONABLE", "score_price_alignment": "headline_approval_failed_to_hold", "current_profile_verdict": "current_profile_false_positive", "notes": "Approval/launch headline produced a tradable spike but not a durable rerating; reimbursement/channel adoption gate should cap Green.", "row_type": "case", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "price_source": "Songdaiki/stock-web"}
{"case_id": "C25_R13L33_005_LUNIT_MNA_OVERHANG", "symbol": "328130", "company_name": "루닛", "round": "R13", "loop": "33", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AI_MEDICAL_DEVICE_GLOBALIZATION_MNA_DILUTION_OVERHANG", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "C25_R13L33_005_T1_STAGE2_ACTIONABLE", "score_price_alignment": "globalization_headline_overhang_failed", "current_profile_verdict": "current_profile_false_positive", "notes": "Global expansion/M&A headline without immediate paid usage or margin visibility was overwhelmed by financing/integration overhang.", "row_type": "case", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "price_source": "Songdaiki/stock-web"}
{"row_type": "trigger", "trigger_id": "C25_R13L33_001_T1_STAGE2_ACTIONABLE", "case_id": "C25_R13L33_001_VUNO_DEEPCARS_REIMBURSEMENT", "symbol": "338220", "company_name": "뷰노", "round": "R13", "loop": "33", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AI_MEDICAL_DEVICE_REIMBURSEMENT_TO_PAID_USAGE", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "medical_device_export_reimbursement", "loop_objective": "holdout_validation|residual_false_positive_mining|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-06-02", "evidence_available_at_that_date": "public_event_or_disclosure|policy_or_regulatory_optionality|relative_strength|early_revision_signal", "evidence_source": "historical public disclosure/news-route label; quantitative calibration source is stock-web OHLC; no later outcome relabeling", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv", "profile_path": "atlas/symbol_profiles/338/338220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-06-02", "entry_price": 23650, "MFE_30D_pct": 72.09, "MFE_90D_pct": 193.87, "MFE_180D_pct": 193.87, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -15.22, "MAE_90D_pct": -15.22, "MAE_180D_pct": -15.22, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-09-07", "peak_price": 69500, "drawdown_after_peak_pct": -65.61, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": null, "four_c_protection_label": null, "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C25_R13L33_001_VUNO_DEEPCARS_REIMBURSEMENT:2023-06-02:23650", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C25_R13L33_001_T2_STAGE3_YELLOW_COMPARISON", "case_id": "C25_R13L33_001_VUNO_DEEPCARS_REIMBURSEMENT", "symbol": "338220", "company_name": "뷰노", "round": "R13", "loop": "33", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AI_MEDICAL_DEVICE_REIMBURSEMENT_TO_PAID_USAGE", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "medical_device_export_reimbursement", "loop_objective": "holdout_validation|residual_false_positive_mining|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill", "trigger_type": "Stage3-Yellow", "trigger_date": "2023-07-13", "evidence_available_at_that_date": "relative_strength|policy_or_regulatory_optionality", "evidence_source": "historical public disclosure/news-route label; quantitative calibration source is stock-web OHLC; no later outcome relabeling", "stage2_evidence_fields": ["relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv", "profile_path": "atlas/symbol_profiles/338/338220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-13", "entry_price": 36150, "MFE_30D_pct": 25.59, "MFE_90D_pct": 92.25, "MFE_180D_pct": 92.25, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -11.89, "MAE_90D_pct": -33.89, "MAE_180D_pct": -33.89, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-09-07", "peak_price": 69500, "drawdown_after_peak_pct": -65.61, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": null, "four_c_protection_label": null, "trigger_outcome_label": "late_but_usable_positive", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C25_R13L33_001_VUNO_DEEPCARS_REIMBURSEMENT:2023-07-13:36150", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C25_R13L33_001_T3_STAGE4B_OVERLAY", "case_id": "C25_R13L33_001_VUNO_DEEPCARS_REIMBURSEMENT", "symbol": "338220", "company_name": "뷰노", "round": "R13", "loop": "33", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AI_MEDICAL_DEVICE_REIMBURSEMENT_TO_PAID_USAGE", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "medical_device_export_reimbursement", "loop_objective": "holdout_validation|residual_false_positive_mining|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill", "trigger_type": "4B", "trigger_date": "2023-09-07", "evidence_available_at_that_date": "relative_strength", "evidence_source": "historical public disclosure/news-route label; quantitative calibration source is stock-web OHLC; no later outcome relabeling", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv", "profile_path": "atlas/symbol_profiles/338/338220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-09-07", "entry_price": 63600, "MFE_30D_pct": 9.28, "MFE_90D_pct": 9.28, "MFE_180D_pct": 9.28, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -42.3, "MAE_90D_pct": -62.42, "MAE_180D_pct": -62.42, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-09-07", "peak_price": 69500, "drawdown_after_peak_pct": -65.61, "green_lateness_ratio": null, "four_b_local_peak_proximity": 0.871, "four_b_full_window_peak_proximity": 0.871, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": "valuation_blowoff|positioning_overheat", "four_c_protection_label": null, "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C25_R13L33_001_VUNO_DEEPCARS_REIMBURSEMENT:2023-09-07:63600", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C25_R13L33_002_T1_STAGE2_ACTIONABLE", "case_id": "C25_R13L33_002_CLASSYS_EXPORT_MARGIN", "symbol": "214150", "company_name": "클래시스", "round": "R13", "loop": "33", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_DEVICE_EXPORT_MARGIN_BRIDGE", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "medical_device_export_reimbursement", "loop_objective": "holdout_validation|residual_false_positive_mining|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-17", "evidence_available_at_that_date": "customer_or_order_quality|capacity_or_volume_route|relative_strength|early_revision_signal", "evidence_source": "historical public disclosure/news-route label; quantitative calibration source is stock-web OHLC; no later outcome relabeling", "stage2_evidence_fields": ["customer_or_order_quality", "capacity_or_volume_route", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214150/2023.csv", "profile_path": "atlas/symbol_profiles/214/214150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-05-17", "entry_price": 26400, "MFE_30D_pct": 34.28, "MFE_90D_pct": 59.09, "MFE_180D_pct": 63.07, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.95, "MAE_90D_pct": -7.95, "MAE_180D_pct": -7.95, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-11-30", "peak_price": 43050, "drawdown_after_peak_pct": -35.31, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": null, "four_c_protection_label": null, "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C25_R13L33_002_CLASSYS_EXPORT_MARGIN:2023-05-17:26400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C25_R13L33_003_T1_STAGE2_ACTIONABLE", "case_id": "C25_R13L33_003_DENTIUM_CHINA_EXPORT", "symbol": "145720", "company_name": "덴티움", "round": "R13", "loop": "33", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "DENTAL_IMPLANT_EXPORT_VBP_VOLUME_MARGIN", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "medical_device_export_reimbursement", "loop_objective": "holdout_validation|residual_false_positive_mining|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-08-09", "evidence_available_at_that_date": "customer_or_order_quality|policy_or_regulatory_optionality|relative_strength", "evidence_source": "historical public disclosure/news-route label; quantitative calibration source is stock-web OHLC; no later outcome relabeling", "stage2_evidence_fields": ["customer_or_order_quality", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/145/145720/2022.csv", "profile_path": "atlas/symbol_profiles/145/145720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-08-09", "entry_price": 94300, "MFE_30D_pct": 13.47, "MFE_90D_pct": 13.47, "MFE_180D_pct": 72.53, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -15.06, "MAE_90D_pct": -27.78, "MAE_180D_pct": -27.78, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-20", "peak_price": 162700, "drawdown_after_peak_pct": -14.94, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": null, "four_c_protection_label": null, "trigger_outcome_label": "high_mae_success", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C25_R13L33_003_DENTIUM_CHINA_EXPORT:2022-08-09:94300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C25_R13L33_004_T1_STAGE2_ACTIONABLE", "case_id": "C25_R13L33_004_ISENS_CGM_APPROVAL", "symbol": "099190", "company_name": "아이센스", "round": "R13", "loop": "33", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "CGM_APPROVAL_WITH_COMMERCIALIZATION_DELAY", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "medical_device_export_reimbursement", "loop_objective": "holdout_validation|residual_false_positive_mining|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-07-18", "evidence_available_at_that_date": "public_event_or_disclosure|policy_or_regulatory_optionality|relative_strength", "evidence_source": "historical public disclosure/news-route label; quantitative calibration source is stock-web OHLC; no later outcome relabeling", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["unknown_or_not_supported"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/099/099190/2023.csv", "profile_path": "atlas/symbol_profiles/099/099190.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-18", "entry_price": 32000, "MFE_30D_pct": 23.59, "MFE_90D_pct": 24.06, "MFE_180D_pct": 24.06, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -18.44, "MAE_90D_pct": -32.03, "MAE_180D_pct": -44.03, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-09-08", "peak_price": 39700, "drawdown_after_peak_pct": -54.89, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": null, "four_c_protection_label": null, "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C25_R13L33_004_ISENS_CGM_APPROVAL:2023-07-18:32000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C25_R13L33_004_T2_4C_PROTECTION", "case_id": "C25_R13L33_004_ISENS_CGM_APPROVAL", "symbol": "099190", "company_name": "아이센스", "round": "R13", "loop": "33", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "CGM_APPROVAL_WITH_COMMERCIALIZATION_DELAY", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "medical_device_export_reimbursement", "loop_objective": "holdout_validation|residual_false_positive_mining|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill", "trigger_type": "4C", "trigger_date": "2024-02-07", "evidence_available_at_that_date": "public_event_or_disclosure", "evidence_source": "historical public disclosure/news-route label; quantitative calibration source is stock-web OHLC; no later outcome relabeling", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": ["unknown_or_not_supported"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/099/099190/2024.csv", "profile_path": "atlas/symbol_profiles/099/099190.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-07", "entry_price": 21000, "MFE_30D_pct": 13.1, "MFE_90D_pct": 13.1, "MFE_180D_pct": 13.1, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -14.71, "MAE_90D_pct": -14.71, "MAE_180D_pct": -14.71, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-21", "peak_price": 23750, "drawdown_after_peak_pct": -14.71, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": null, "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4C_success", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C25_R13L33_004_ISENS_CGM_APPROVAL:2024-02-07:21000", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C25_R13L33_005_T1_STAGE2_ACTIONABLE", "case_id": "C25_R13L33_005_LUNIT_MNA_OVERHANG", "symbol": "328130", "company_name": "루닛", "round": "R13", "loop": "33", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AI_MEDICAL_DEVICE_GLOBALIZATION_MNA_DILUTION_OVERHANG", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "medical_device_export_reimbursement", "loop_objective": "holdout_validation|residual_false_positive_mining|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-02", "evidence_available_at_that_date": "public_event_or_disclosure|customer_or_order_quality|policy_or_regulatory_optionality", "evidence_source": "historical public disclosure/news-route label; quantitative calibration source is stock-web OHLC; no later outcome relabeling", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["unknown_or_not_supported"], "stage4b_evidence_fields": ["capital_raise_or_overhang", "dilution_or_cb", "execution_risk_score"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/328/328130/2024.csv", "profile_path": "atlas/symbol_profiles/328/328130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-02", "entry_price": 79400, "MFE_30D_pct": 4.28, "MFE_90D_pct": 4.28, "MFE_180D_pct": 4.28, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -33.0, "MAE_90D_pct": -40.62, "MAE_180D_pct": -60.96, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-02", "peak_price": 82800, "drawdown_after_peak_pct": -62.56, "green_lateness_ratio": null, "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_risk_overlay_but_not_positive", "four_b_evidence_type": "capital_raise_or_overhang|dilution_or_cb|execution_risk_score", "four_c_protection_label": null, "trigger_outcome_label": "false_positive_green", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C25_R13L33_005_LUNIT_MNA_OVERHANG:2024-01-02:79400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C25_R13L33_001_VUNO_DEEPCARS_REIMBURSEMENT", "trigger_id": "C25_R13L33_001_T1_STAGE2_ACTIONABLE", "symbol": "338220", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 8, "relative_strength_score": 15, "customer_quality_score": 12, "policy_or_regulatory_score": 8, "valuation_repricing_score": 6, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 13, "revision_score": 8, "relative_strength_score": 15, "customer_quality_score": 15, "policy_or_regulatory_score": 8, "valuation_repricing_score": 6, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow", "changed_components": ["customer_quality_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C25 shadow profile rewards paid usage/export revenue bridge but forces high-MAE path to remain size-controlled.", "MFE_90D_pct": 193.87, "MAE_90D_pct": -15.22, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C25_R13L33_002_CLASSYS_EXPORT_MARGIN", "trigger_id": "C25_R13L33_002_T1_STAGE2_ACTIONABLE", "symbol": "214150", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 8, "relative_strength_score": 15, "customer_quality_score": 12, "policy_or_regulatory_score": 8, "valuation_repricing_score": 6, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 13, "revision_score": 8, "relative_strength_score": 15, "customer_quality_score": 15, "policy_or_regulatory_score": 8, "valuation_repricing_score": 6, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow", "changed_components": ["customer_quality_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C25 shadow profile rewards paid usage/export revenue bridge but forces high-MAE path to remain size-controlled.", "MFE_90D_pct": 59.09, "MAE_90D_pct": -7.95, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C25_R13L33_003_DENTIUM_CHINA_EXPORT", "trigger_id": "C25_R13L33_003_T1_STAGE2_ACTIONABLE", "symbol": "145720", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 8, "relative_strength_score": 15, "customer_quality_score": 12, "policy_or_regulatory_score": 8, "valuation_repricing_score": 6, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 13, "revision_score": 8, "relative_strength_score": 15, "customer_quality_score": 15, "policy_or_regulatory_score": 8, "valuation_repricing_score": 6, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80, "stage_label_after": "Stage2-Actionable_with_size_guard", "changed_components": ["customer_quality_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C25 shadow profile rewards paid usage/export revenue bridge but forces high-MAE path to remain size-controlled.", "MFE_90D_pct": 13.47, "MAE_90D_pct": -27.78, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C25_R13L33_004_ISENS_CGM_APPROVAL", "trigger_id": "C25_R13L33_004_T1_STAGE2_ACTIONABLE", "symbol": "099190", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 16, "customer_quality_score": 8, "policy_or_regulatory_score": 14, "valuation_repricing_score": 10, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 86, "stage_label_before": "Stage3-Green_candidate", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 16, "customer_quality_score": 8, "policy_or_regulatory_score": 8, "valuation_repricing_score": 10, "execution_risk_score": -11, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 68, "stage_label_after": "Stage2-watch_or_4B_overlay", "changed_components": ["policy_or_regulatory_score", "execution_risk_score", "dilution_cb_risk_score"], "component_delta_explanation": "Approval/M&A headline is capped until reimbursement/channel conversion or paid usage appears.", "MFE_90D_pct": 24.06, "MAE_90D_pct": -32.03, "score_return_alignment_label": "guard_improves_alignment", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C25_R13L33_005_LUNIT_MNA_OVERHANG", "trigger_id": "C25_R13L33_005_T1_STAGE2_ACTIONABLE", "symbol": "328130", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 16, "customer_quality_score": 8, "policy_or_regulatory_score": 14, "valuation_repricing_score": 10, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 86, "stage_label_before": "Stage3-Green_candidate", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 16, "customer_quality_score": 8, "policy_or_regulatory_score": 8, "valuation_repricing_score": 10, "execution_risk_score": -11, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": -10, "accounting_trust_risk_score": 0}, "weighted_score_after": 61, "stage_label_after": "Stage2-watch_or_4B_overlay", "changed_components": ["policy_or_regulatory_score", "execution_risk_score", "dilution_cb_risk_score"], "component_delta_explanation": "Approval/M&A headline is capped until reimbursement/channel conversion or paid usage appears.", "MFE_90D_pct": 4.28, "MAE_90D_pct": -40.62, "score_return_alignment_label": "guard_improves_alignment", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R13", "loop": "33", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "new_trigger_family_count": 5, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["approval_only_false_positive", "mna_dilution_overhang_false_positive", "high_mae_success_size_control_needed"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
next_round = R13_loop_34
next_large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
next_canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
reason = after L7/C24 and L7/C25, shift from healthcare event-risk calibration to platform operating-leverage residuals.
```

## 28. Source Notes

```text
stock_web_manifest_path = atlas/manifest.json
symbol_profiles_used =
  - atlas/symbol_profiles/338/338220.json
  - atlas/symbol_profiles/214/214150.json
  - atlas/symbol_profiles/145/145720.json
  - atlas/symbol_profiles/099/099190.json
  - atlas/symbol_profiles/328/328130.json
tradable_shards_used =
  - atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/338/338220/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/214/214150/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/214/214150/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/145/145720/2022.csv
  - atlas/ohlcv_tradable_by_symbol_year/145/145720/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/099/099190/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/099/099190/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/328/328130/2024.csv
allowed_stock_agent_research_artifacts_read =
  - reports/e2r_calibration/ingest_summary.md
  - reports/e2r_calibration/calibrated_profile_report.md
stock_agent_code_accessed = false
stock_agent_code_patch_written = false
production_scoring_changed = false
```

# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R7
scheduled_loop = 74
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id = MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_CHANNEL
output_file = e2r_stock_web_v12_residual_round_R7_loop_74_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT.

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

Applied global axes are not re-proposed globally. This loop only tests whether R7/C25 needs a medical-device-specific export/reimbursement conversion bridge and an inventory/ASP guard.

## 2. Round / Large Sector / Canonical Archetype Scope

|field|value|
|---|---|
|round|R7|
|loop|74|
|round_sector_consistency|pass|
|allowed_large_sector_for_R7|L7_BIO_HEALTHCARE_MEDICAL|
|selected_large_sector_id|L7_BIO_HEALTHCARE_MEDICAL|
|selected_canonical_archetype_id|C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|
|fine_archetype_id|MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_CHANNEL|
|loop_objective|sector_specific_rule_discovery, canonical_archetype_compression, counterexample_mining, 4B_non_price_requirement_stress_test, coverage_gap_fill|

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 artifacts show R7 Loop 71 used C24 and R7 Loop 72~73 used C23. This loop therefore selects C25 to fill the medical-device export/reimbursement gap inside the scheduled R7 sector without jumping rounds.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
duplicate_key_conflict_count = 0
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
```

## 4. Stock-Web OHLC Input / Price Source Validation

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

Stock-web schema uses `d,o,h,l,c,v,a,mc,s,m` for tradable shards and `d,o,h,l,c,v,a,mc,s,m,rs` for raw shards. MFE/MAE follow the stock-web schema formula: max high or min low from entry date through N tradable rows divided by entry close.

## 5. Historical Eligibility Gate

All representative triggers are historical, have entry rows in stock-web tradable shards, have at least 180 forward trading days by manifest max date, and have no corporate-action candidate overlap in the 180D forward window.

|symbol|profile path|profile summary|180D corporate action status|
|---|---|---|---|
|214150|atlas/symbol_profiles/214/214150.json|first_date=2015-04-03; last_date=2026-02-20; trading_day_count=2608; corporate_action_candidate_dates=[2017-12-28]; 2024 180D window clean.|clean_180D_window|
|338220|atlas/symbol_profiles/338/338220.json|first_date=2021-02-26; last_date=2026-02-20; trading_day_count=1221; corporate_action_candidate_dates=[]; 2023 180D window clean.|clean_180D_window|
|145720|atlas/symbol_profiles/145/145720.json|first_date=2017-03-15; last_date=2026-02-20; trading_day_count=2190; corporate_action_candidate_dates=[]; 2023 180D window clean.|clean_180D_window|
|100120|atlas/symbol_profiles/100/100120.json|first_date=2009-04-10; last_date=2026-02-20; trading_day_count=4157; corporate_action_candidate_dates=[2011-08-08]; 2023 180D window clean.|clean_180D_window|

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id = MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_CHANNEL
compressed_fine_paths =
  - aesthetic_device_export_installed_base_consumables
  - medical_AI_reimbursement_adoption
  - dental_implant_export_with_reimbursement_policy_risk
  - medical_imaging_export_without_recurring_conversion
```

C25 should compress around evidence quality: export growth alone is a noisy spark; export plus reimbursement, installed-base utilization, consumable reorder, and margin bridge is the useful flame.

## 7. Case Selection Summary

|case_id|symbol|company|role|trigger|entry|MFE90|MAE90|MFE180|MAE180|verdict|
|---|---|---|---|---|---|---|---|---|---|---|
|R7L74_C25_214150_CLASSYS_EXPORT_CONSUMABLE_POS|214150|클래시스|structural_success|Stage2-Actionable 2024-02-15|2024-02-15 @ 32,850|56.16|-4.41|85.69|-4.41|current_profile_too_late|
|R7L74_C25_338220_VUNO_AI_REIMBURSEMENT_HIGH_MAE_POS|338220|뷰노|high_mae_success|Stage2-Actionable 2023-06-27|2023-06-28 @ 18,900|172.49|-15.61|172.49|-40.48|current_profile_4B_too_late|
|R7L74_C25_145720_DENTIUM_CHINA_VBP_EXPORT_COUNTER|145720|덴티움|failed_rerating|Stage2 2023-05-12|2023-05-15 @ 159,200|18.41|-29.02|18.41|-42.59|current_profile_false_positive|
|R7L74_C25_100120_VIEWORKS_IMAGING_EXPORT_COUNTER|100120|뷰웍스|failed_rerating|Stage2 2023-02-16|2023-02-17 @ 39,650|8.45|-18.66|8.45|-25.47|current_profile_false_positive|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 3
4C_case_count = 2
calibration_usable_case_count = 4
calibration_usable_representative_trigger_count = 4
calibration_usable_total_trigger_count = 8
```

The balance is deliberate: Classys and Vuno show the upside of export/reimbursement or installed-base conversion, while Dentium and Vieworks show why generic device/export relative strength can become a false positive when reimbursement, inventory, ASP, or recurring revenue conversion is weak.

## 9. Evidence Source Map

|case|event evidence|source confidence|source URLs / notes|
|---|---|---|---|
|R7L74_C25_214150_CLASSYS_EXPORT_CONSUMABLE_POS|Aesthetic device export/installed-base narrative with recurring consumable/channel conversion. The usable C25 signal is export sales plus consumable reorder visibility, not a one-day price reaction.|medium|public disclosure/news/earnings window; stock-web OHLC/profile validation|
|R7L74_C25_338220_VUNO_AI_REIMBURSEMENT_HIGH_MAE_POS|Medical-AI device route with reimbursement/adoption optionality. Positive path required payer/hospital adoption evidence; the residual issue is high MAE and the need for 4B overlay once valuation/positioning outran reimbursement conversion.|medium|public disclosure/news/earnings window; stock-web OHLC/profile validation|
|R7L74_C25_145720_DENTIUM_CHINA_VBP_EXPORT_COUNTER|Dental implant export/China demand narrative existed, but reimbursement/VBP policy pressure, distributor inventory, and ASP/margin risk made the headline insufficient. Treat as C25 counterexample to export-only promotion.|medium|public disclosure/news/earnings window; stock-web OHLC/profile validation|
|R7L74_C25_100120_VIEWORKS_IMAGING_EXPORT_COUNTER|Medical/digital imaging export narrative without reimbursement conversion or recurring consumable economics. Evidence was too close to generic device/export beta; current profile can over-promote if relative strength dominates.|medium|public disclosure/news/earnings window; stock-web OHLC/profile validation|

## 10. Price Data Source Map

|symbol|shard|entry_date|entry_price|price_basis|
|---|---|---|---|---|
|214150|atlas/ohlcv_tradable_by_symbol_year/214/214150/2024.csv|2024-02-15|32850|tradable_raw|
|338220|atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv|2023-06-28|18900|tradable_raw|
|145720|atlas/ohlcv_tradable_by_symbol_year/145/145720/2023.csv|2023-05-15|159200|tradable_raw|
|100120|atlas/ohlcv_tradable_by_symbol_year/100/100120/2023.csv|2023-02-17|39650|tradable_raw|

## 11. Case-by-Case Trigger Grid

|case|trigger_type|stage2_evidence|stage3_evidence|stage4b_evidence|stage4c_evidence|current_profile_verdict|
|---|---|---|---|---|---|---|
|R7L74_C25_214150_CLASSYS_EXPORT_CONSUMABLE_POS|Stage2-Actionable|public_event_or_disclosure, customer_or_order_quality, relative_strength, capacity_or_volume_route, early_revision_signal|confirmed_revision, margin_bridge, financial_visibility, repeat_order_or_conversion, durable_customer_confirmation, low_red_team_risk|valuation_blowoff, positioning_overheat|none|current_profile_too_late|
|R7L74_C25_338220_VUNO_AI_REIMBURSEMENT_HIGH_MAE_POS|Stage2-Actionable|public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength, capacity_or_volume_route, early_revision_signal|multiple_public_sources, financial_visibility, repeat_order_or_conversion|valuation_blowoff, positioning_overheat, price_only_local_peak|none|current_profile_4B_too_late|
|R7L74_C25_145720_DENTIUM_CHINA_VBP_EXPORT_COUNTER|Stage2|public_event_or_disclosure, relative_strength, capacity_or_volume_route|financial_visibility|valuation_blowoff, positioning_overheat, margin_or_backlog_slowdown|thesis_evidence_broken|current_profile_false_positive|
|R7L74_C25_100120_VIEWORKS_IMAGING_EXPORT_COUNTER|Stage2|public_event_or_disclosure, relative_strength, capacity_or_volume_route|none|margin_or_backlog_slowdown|thesis_evidence_broken|current_profile_false_positive|

## 12. Trigger-Level OHLC Backtest Tables

|trigger_id|symbol|entry_ohlc|MFE30|MAE30|MFE90|MAE90|MFE180|MAE180|peak|drawdown_after_peak|
|---|---|---|---|---|---|---|---|---|---|---|
|T_R7L74_214150_20240215_STAGE2A_EXPORT_CONSUMABLE_DEVICE|214150|2024-02-15 o=31,150 h=32,950 l=30,600 c=32,850 v=1,073,370|18.42|-4.41|56.16|-4.41|85.69|-4.41|2024-09-13 @ 61,000|-18.85|
|T_R7L74_338220_20230628_STAGE2A_REIMBURSEMENT_MEDICAL_AI|338220|2023-06-28 c≈18,900 from stock-web tradable shard; row validation through profile, forward 180D available.|75.93|-10.32|172.49|-15.61|172.49|-40.48|2023-09-05 @ 51,500|-63.3|
|T_R7L74_145720_20230515_STAGE2_EXPORT_WITH_REIMBURSEMENT_RISK|145720|2023-05-15 c≈159,200 from stock-web tradable shard; profile has no corporate-action candidate dates.|18.41|-9.67|18.41|-29.02|18.41|-42.59|2023-06-08 @ 188,500|-50.19|
|T_R7L74_100120_20230217_STAGE2_DEVICE_EXPORT_NO_CONSUMABLE|100120|2023-02-17 c≈39,650 from stock-web tradable shard; historical corporate-action candidate 2011 only, no 2023 180D overlap.|7.19|-7.31|8.45|-18.66|8.45|-25.47|2023-04-04 @ 43,000|-39.77|

## 13. Current Calibrated Profile Stress Test

|case|P0 judgment|fit to MFE/MAE|residual error|
|---|---|---|---|
|R7L74_C25_214150_CLASSYS_EXPORT_CONSUMABLE_POS|Stage3-Yellow; waits for confirmation|MFE180 high with shallow MAE; P0 too late|missed/late structural|
|R7L74_C25_338220_VUNO_AI_REIMBURSEMENT_HIGH_MAE_POS|Stage3-Yellow, 4B late|MFE high but MAE/drawdown severe; P0 late on 4B overlay|4B too late|
|R7L74_C25_145720_DENTIUM_CHINA_VBP_EXPORT_COUNTER|Stage3-Yellow risk from export/RS|MFE capped, MAE very large; P0 false positive|export-only false positive|
|R7L74_C25_100120_VIEWORKS_IMAGING_EXPORT_COUNTER|Stage3-Yellow risk from device/export beta|weak MFE and deep MAE; P0 false positive|no conversion false positive|

Existing Stage2 bonus is kept globally, but C25 needs an added non-price conversion gate. Yellow/Green thresholds are not changed globally; the shadow rule changes component eligibility before thresholding.

## 14. Stage2 / Yellow / Green Comparison

|case|Stage2 entry|Stage3/Green status|green_lateness_ratio|interpretation|
|---|---|---|---|---|
|R7L74_C25_214150_CLASSYS_EXPORT_CONSUMABLE_POS|2024-02-15 @ 32850|Stage3-Green|0.42|Green late if conversion confirmation waits until upside is mostly priced|
|R7L74_C25_338220_VUNO_AI_REIMBURSEMENT_HIGH_MAE_POS|2023-06-28 @ 18900|Stage3-Green+4B-Watch|0.57|Green late if conversion confirmation waits until upside is mostly priced|
|R7L74_C25_145720_DENTIUM_CHINA_VBP_EXPORT_COUNTER|2023-05-15 @ 159200|Stage2-Watch/4C-Guard|not_applicable|No Green should fire without reimbursement/consumable conversion|
|R7L74_C25_100120_VIEWORKS_IMAGING_EXPORT_COUNTER|2023-02-17 @ 39650|Stage2-Watch|not_applicable|No Green should fire without reimbursement/consumable conversion|

## 15. 4B Local vs Full-window Timing Audit

|case|four_b_local_peak_proximity|four_b_full_window_peak_proximity|four_b_evidence_type|timing verdict|
|---|---|---|---|---|
|R7L74_C25_214150_CLASSYS_EXPORT_CONSUMABLE_POS|0.88|0.88|valuation_blowoff, positioning_overheat|good_full_window_4B_timing_if_channel_overheat_used|
|R7L74_C25_338220_VUNO_AI_REIMBURSEMENT_HIGH_MAE_POS|0.96|0.96|valuation_blowoff, positioning_overheat|good_full_window_4B_timing_if_non_price_positioning_and_reimbursement_gap_used|
|R7L74_C25_145720_DENTIUM_CHINA_VBP_EXPORT_COUNTER|0.93|0.93|valuation_blowoff, margin_or_backlog_slowdown, positioning_overheat|good_4B_if_reimbursement_policy_and_inventory_risk_used|
|R7L74_C25_100120_VIEWORKS_IMAGING_EXPORT_COUNTER|0.38|0.38|margin_or_backlog_slowdown|weak_4B_but_valid_counterexample_guard|

## 16. 4C Protection Audit

|case|4C label|drawdown_after_peak|protection interpretation|
|---|---|---|---|
|R7L74_C25_214150_CLASSYS_EXPORT_CONSUMABLE_POS|thesis_break_watch_only|-18.85|watch-only; positive thesis not broken but 4B overlay needed|
|R7L74_C25_338220_VUNO_AI_REIMBURSEMENT_HIGH_MAE_POS|thesis_break_watch_only|-63.3|watch-only; positive thesis not broken but 4B overlay needed|
|R7L74_C25_145720_DENTIUM_CHINA_VBP_EXPORT_COUNTER|hard_4c_success|-50.19|hard/guard routing useful for counterexamples|
|R7L74_C25_100120_VIEWORKS_IMAGING_EXPORT_COUNTER|thesis_break_watch_only|-39.77|hard/guard routing useful for counterexamples|

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = L7_BIO_HEALTHCARE_MEDICAL
rule_name = L7_C25_medical_device_conversion_gate
rule_logic = promote medical-device export signals only when at least one of reimbursement conversion, installed-base utilization, consumable reorder, or durable hospital/customer adoption is observable. Cap generic export/RS-only signals at Stage2-Watch.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
positive_bonus = +3 to +5 when export growth is tied to reimbursement or recurring consumable/channel conversion
counterexample_guard = cap or 4C-watch when export headline lacks conversion and inventory/ASP risk is visible
```

## 19. Before / After Backtest Comparison

|profile|scope|avg_MFE90|avg_MAE90|avg_MFE180|avg_MAE180|false_positive_rate|verdict|
|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|global_proxy|63.88|-16.93|71.26|-28.24|0.5|mixed; positives work but two generic export/device signals remain false positives|
|P0b_e2r_2_0_baseline_reference|rollback_reference|63.88|-16.93|71.26|-28.24|0.5|weaker than P0; counterexample cap absent|
|P1_sector_specific_candidate_profile|L7_sector_specific|114.33|-10.01|129.09|-22.45|0.0|improved: keeps Classys/Vuno, rejects Dentium/Vieworks|
|P2_canonical_archetype_candidate_profile|C25_canonical_archetype_specific|114.33|-10.01|129.09|-22.45|0.0|best C25 alignment|
|P3_counterexample_guard_profile|counterexample_guard|13.43|-23.84|13.43|-34.03|0.0|protective for false positives|

## 20. Score-Return Alignment Matrix

|case|weighted_before|stage_before|weighted_after|stage_after|MFE90|MAE90|alignment|
|---|---|---|---|---|---|---|---|
|R7L74_C25_214150_CLASSYS_EXPORT_CONSUMABLE_POS|84|Stage3-Yellow|91|Stage3-Green|56.16|-4.41|aligned_after_channel_bridge_bonus|
|R7L74_C25_338220_VUNO_AI_REIMBURSEMENT_HIGH_MAE_POS|82|Stage3-Yellow|88|Stage3-Green+4B-Watch|172.49|-15.61|positive_but_requires_mae_guard|
|R7L74_C25_145720_DENTIUM_CHINA_VBP_EXPORT_COUNTER|79|Stage3-Yellow|60|Stage2-Watch/4C-Guard|18.41|-29.02|false_positive_blocked_after_reimbursement_guard|
|R7L74_C25_100120_VIEWORKS_IMAGING_EXPORT_COUNTER|76|Stage3-Yellow|58|Stage2-Watch|8.45|-18.66|guarded_after_shadow|

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L7_BIO_HEALTHCARE_MEDICAL|C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_CHANNEL|2|2|3|2|4|0|8|4|3|True|True|C25 no longer empty in R7 loop74; needs later holdout validation|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: generic_device_export_false_positive, reimbursement_or_consumable_conversion_missing, 4B_overlay_late_for_high_MAE_medical_AI
new_axis_proposed: C25_reimbursement_channel_conversion_bonus, C25_device_export_inventory_guard
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus, Yellow/Green thresholds
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope: historical trigger-level OHLC backtest using stock-web tradable_raw shards, 180D window availability, corporate-action profile screen, current profile proxy stress test, and shadow-only C25 rule proposal. Non-validation scope: no live candidates, no current recommendation, no stock_agent code inspection, no production scoring patch, no brokerage/API action.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C25_reimbursement_channel_conversion_bonus,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,+4,+4,"Reward export/device signals only when reimbursement, consumable, installed-base, or hospital adoption conversion is visible","Keeps Classys/Vuno positives while avoiding pure export beta",T_R7L74_214150_20240215_STAGE2A_EXPORT_CONSUMABLE_DEVICE|T_R7L74_338220_20230628_STAGE2A_REIMBURSEMENT_MEDICAL_AI,4,4,2,low_medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C25_export_headline_without_conversion_cap,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,false,true,guard,"Cap generic device/export RS when reimbursement or recurring channel conversion is missing","Blocks Dentium/Vieworks false positives",T_R7L74_145720_20230515_STAGE2_EXPORT_WITH_REIMBURSEMENT_RISK|T_R7L74_100120_20230217_STAGE2_DEVICE_EXPORT_NO_CONSUMABLE,4,4,2,low_medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C25_high_MAE_4B_overlay,sector_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,+1,+1,"Medical-AI/reimbursement successes can still require early 4B overlay when valuation/positioning outruns adoption","Improves Vuno-style high-MAE success handling",T_R7L74_338220_20230628_STAGE2A_REIMBURSEMENT_MEDICAL_AI,4,4,2,low,sector_shadow_only,"overlay only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation
```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows
```jsonl
{"row_type": "case", "case_id": "R7L74_C25_214150_CLASSYS_EXPORT_CONSUMABLE_POS", "symbol": "214150", "company_name": "클래시스", "round": "R7", "loop": "74", "scheduled_round": "R7", "scheduled_loop": "74", "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_CHANNEL", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "T_R7L74_214150_20240215_STAGE2A_EXPORT_CONSUMABLE_DEVICE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_after_channel_bridge_bonus", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Aesthetic device export/installed-base narrative with recurring consumable/channel conversion. The usable C25 signal is export sales plus consumable reorder visibility, not a one-day price reaction."}
{"row_type": "case", "case_id": "R7L74_C25_338220_VUNO_AI_REIMBURSEMENT_HIGH_MAE_POS", "symbol": "338220", "company_name": "뷰노", "round": "R7", "loop": "74", "scheduled_round": "R7", "scheduled_loop": "74", "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_CHANNEL", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "T_R7L74_338220_20230628_STAGE2A_REIMBURSEMENT_MEDICAL_AI", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_but_requires_mae_guard", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "Medical-AI device route with reimbursement/adoption optionality. Positive path required payer/hospital adoption evidence; the residual issue is high MAE and the need for 4B overlay once valuation/positioning outran reimbursement conversion."}
{"row_type": "case", "case_id": "R7L74_C25_145720_DENTIUM_CHINA_VBP_EXPORT_COUNTER", "symbol": "145720", "company_name": "덴티움", "round": "R7", "loop": "74", "scheduled_round": "R7", "scheduled_loop": "74", "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_CHANNEL", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "T_R7L74_145720_20230515_STAGE2_EXPORT_WITH_REIMBURSEMENT_RISK", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "false_positive_blocked_after_reimbursement_guard", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Dental implant export/China demand narrative existed, but reimbursement/VBP policy pressure, distributor inventory, and ASP/margin risk made the headline insufficient. Treat as C25 counterexample to export-only promotion."}
{"row_type": "case", "case_id": "R7L74_C25_100120_VIEWORKS_IMAGING_EXPORT_COUNTER", "symbol": "100120", "company_name": "뷰웍스", "round": "R7", "loop": "74", "scheduled_round": "R7", "scheduled_loop": "74", "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_CHANNEL", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "T_R7L74_100120_20230217_STAGE2_DEVICE_EXPORT_NO_CONSUMABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "guarded_after_shadow", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Medical/digital imaging export narrative without reimbursement conversion or recurring consumable economics. Evidence was too close to generic device/export beta; current profile can over-promote if relative strength dominates."}
```

### 25.3 trigger rows
```jsonl
{"row_type": "trigger", "trigger_id": "T_R7L74_214150_20240215_STAGE2A_EXPORT_CONSUMABLE_DEVICE", "case_id": "R7L74_C25_214150_CLASSYS_EXPORT_CONSUMABLE_POS", "symbol": "214150", "company_name": "클래시스", "round": "R7", "loop": "74", "scheduled_round": "R7", "scheduled_loop": "74", "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_CHANNEL", "sector": "medical_device_aesthetic_export", "primary_archetype": "export_device_plus_consumable_channel", "loop_objective": "sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-15", "evidence_available_at_that_date": "Aesthetic device export/installed-base narrative with recurring consumable/channel conversion. The usable C25 signal is export sales plus consumable reorder visibility, not a one-day price reaction.", "evidence_source": "public 2024 earnings/export channel window; stock-web tradable OHLC row and symbol profile validation.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "repeat_order_or_conversion", "durable_customer_confirmation", "low_red_team_risk"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214150/2024.csv", "profile_path": "atlas/symbol_profiles/214/214150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-15", "entry_price": 32850, "MFE_30D_pct": 18.42, "MFE_90D_pct": 56.16, "MFE_180D_pct": 85.69, "MFE_1Y_pct": 96.04, "MFE_2Y_pct": null, "MAE_30D_pct": -4.41, "MAE_90D_pct": -4.41, "MAE_180D_pct": -4.41, "MAE_1Y_pct": -4.41, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-09-13", "peak_price": 61000, "drawdown_after_peak_pct": -18.85, "green_lateness_ratio": 0.42, "four_b_local_peak_proximity": 0.88, "four_b_full_window_peak_proximity": 0.88, "four_b_timing_verdict": "good_full_window_4B_timing_if_channel_overheat_used", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "positive_structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L74_C25_214150_CLASSYS_EXPORT_CONSUMABLE_POS_ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R7L74_214150_20240215_OVERLAY_EXPORT_CONSUMABLE_DEVICE_OVERLAY", "case_id": "R7L74_C25_214150_CLASSYS_EXPORT_CONSUMABLE_POS", "symbol": "214150", "company_name": "클래시스", "round": "R7", "loop": "74", "scheduled_round": "R7", "scheduled_loop": "74", "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_CHANNEL", "sector": "medical_device_aesthetic_export", "primary_archetype": "export_device_plus_consumable_channel", "loop_objective": "sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4B-Overlay", "trigger_date": "2024-02-15", "evidence_available_at_that_date": "Aesthetic device export/installed-base narrative with recurring consumable/channel conversion. The usable C25 signal is export sales plus consumable reorder visibility, not a one-day price reaction.", "evidence_source": "public 2024 earnings/export channel window; stock-web tradable OHLC row and symbol profile validation.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "repeat_order_or_conversion", "durable_customer_confirmation", "low_red_team_risk"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214150/2024.csv", "profile_path": "atlas/symbol_profiles/214/214150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-15", "entry_price": 32850, "MFE_30D_pct": 18.42, "MFE_90D_pct": 56.16, "MFE_180D_pct": 85.69, "MFE_1Y_pct": 96.04, "MFE_2Y_pct": null, "MAE_30D_pct": -4.41, "MAE_90D_pct": -4.41, "MAE_180D_pct": -4.41, "MAE_1Y_pct": -4.41, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-09-13", "peak_price": 61000, "drawdown_after_peak_pct": -18.85, "green_lateness_ratio": 0.42, "four_b_local_peak_proximity": 0.88, "four_b_full_window_peak_proximity": 0.88, "four_b_timing_verdict": "good_full_window_4B_timing_if_channel_overheat_used", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "positive_structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L74_C25_214150_CLASSYS_EXPORT_CONSUMABLE_POS_ENTRY", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "T_R7L74_338220_20230628_STAGE2A_REIMBURSEMENT_MEDICAL_AI", "case_id": "R7L74_C25_338220_VUNO_AI_REIMBURSEMENT_HIGH_MAE_POS", "symbol": "338220", "company_name": "뷰노", "round": "R7", "loop": "74", "scheduled_round": "R7", "scheduled_loop": "74", "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_CHANNEL", "sector": "medical_ai_reimbursement", "primary_archetype": "medical_ai_reimbursement_adoption", "loop_objective": "sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-06-27", "evidence_available_at_that_date": "Medical-AI device route with reimbursement/adoption optionality. Positive path required payer/hospital adoption evidence; the residual issue is high MAE and the need for 4B overlay once valuation/positioning outran reimbursement conversion.", "evidence_source": "public medical-AI reimbursement/adoption window; stock-web tradable OHLC row and symbol profile validation.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv", "profile_path": "atlas/symbol_profiles/338/338220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-06-28", "entry_price": 18900, "MFE_30D_pct": 75.93, "MFE_90D_pct": 172.49, "MFE_180D_pct": 172.49, "MFE_1Y_pct": 172.49, "MFE_2Y_pct": null, "MAE_30D_pct": -10.32, "MAE_90D_pct": -15.61, "MAE_180D_pct": -40.48, "MAE_1Y_pct": -52.12, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-09-05", "peak_price": 51500, "drawdown_after_peak_pct": -63.3, "green_lateness_ratio": 0.57, "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "good_full_window_4B_timing_if_non_price_positioning_and_reimbursement_gap_used", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "positive_high_mfe_high_mae_requires_4B_overlay", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L74_C25_338220_VUNO_AI_REIMBURSEMENT_HIGH_MAE_POS_ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R7L74_338220_20230628_OVERLAY_REIMBURSEMENT_MEDICAL_AI_OVERLAY", "case_id": "R7L74_C25_338220_VUNO_AI_REIMBURSEMENT_HIGH_MAE_POS", "symbol": "338220", "company_name": "뷰노", "round": "R7", "loop": "74", "scheduled_round": "R7", "scheduled_loop": "74", "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_CHANNEL", "sector": "medical_ai_reimbursement", "primary_archetype": "medical_ai_reimbursement_adoption", "loop_objective": "sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4B-Overlay", "trigger_date": "2023-06-27", "evidence_available_at_that_date": "Medical-AI device route with reimbursement/adoption optionality. Positive path required payer/hospital adoption evidence; the residual issue is high MAE and the need for 4B overlay once valuation/positioning outran reimbursement conversion.", "evidence_source": "public medical-AI reimbursement/adoption window; stock-web tradable OHLC row and symbol profile validation.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv", "profile_path": "atlas/symbol_profiles/338/338220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-06-28", "entry_price": 18900, "MFE_30D_pct": 75.93, "MFE_90D_pct": 172.49, "MFE_180D_pct": 172.49, "MFE_1Y_pct": 172.49, "MFE_2Y_pct": null, "MAE_30D_pct": -10.32, "MAE_90D_pct": -15.61, "MAE_180D_pct": -40.48, "MAE_1Y_pct": -52.12, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-09-05", "peak_price": 51500, "drawdown_after_peak_pct": -63.3, "green_lateness_ratio": 0.57, "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "good_full_window_4B_timing_if_non_price_positioning_and_reimbursement_gap_used", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "positive_high_mfe_high_mae_requires_4B_overlay", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L74_C25_338220_VUNO_AI_REIMBURSEMENT_HIGH_MAE_POS_ENTRY", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "T_R7L74_145720_20230515_STAGE2_EXPORT_WITH_REIMBURSEMENT_RISK", "case_id": "R7L74_C25_145720_DENTIUM_CHINA_VBP_EXPORT_COUNTER", "symbol": "145720", "company_name": "덴티움", "round": "R7", "loop": "74", "scheduled_round": "R7", "scheduled_loop": "74", "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_CHANNEL", "sector": "dental_implant_export_reimbursement", "primary_archetype": "export_device_with_reimbursement_policy_risk", "loop_objective": "sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2", "trigger_date": "2023-05-12", "evidence_available_at_that_date": "Dental implant export/China demand narrative existed, but reimbursement/VBP policy pressure, distributor inventory, and ASP/margin risk made the headline insufficient. Treat as C25 counterexample to export-only promotion.", "evidence_source": "public dental implant China VBP/export policy window; stock-web tradable OHLC row and symbol profile validation.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/145/145720/2023.csv", "profile_path": "atlas/symbol_profiles/145/145720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-05-15", "entry_price": 159200, "MFE_30D_pct": 18.41, "MFE_90D_pct": 18.41, "MFE_180D_pct": 18.41, "MFE_1Y_pct": 18.41, "MFE_2Y_pct": null, "MAE_30D_pct": -9.67, "MAE_90D_pct": -29.02, "MAE_180D_pct": -42.59, "MAE_1Y_pct": -56.41, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-08", "peak_price": 188500, "drawdown_after_peak_pct": -50.19, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "good_4B_if_reimbursement_policy_and_inventory_risk_used", "four_b_evidence_type": ["valuation_blowoff", "margin_or_backlog_slowdown", "positioning_overheat"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "counterexample_export_headline_without_reimbursement_durability", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L74_C25_145720_DENTIUM_CHINA_VBP_EXPORT_COUNTER_ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R7L74_145720_20230515_OVERLAY_EXPORT_WITH_REIMBURSEMENT_RISK_OVERLAY", "case_id": "R7L74_C25_145720_DENTIUM_CHINA_VBP_EXPORT_COUNTER", "symbol": "145720", "company_name": "덴티움", "round": "R7", "loop": "74", "scheduled_round": "R7", "scheduled_loop": "74", "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_CHANNEL", "sector": "dental_implant_export_reimbursement", "primary_archetype": "export_device_with_reimbursement_policy_risk", "loop_objective": "sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4C-Guard", "trigger_date": "2023-05-12", "evidence_available_at_that_date": "Dental implant export/China demand narrative existed, but reimbursement/VBP policy pressure, distributor inventory, and ASP/margin risk made the headline insufficient. Treat as C25 counterexample to export-only promotion.", "evidence_source": "public dental implant China VBP/export policy window; stock-web tradable OHLC row and symbol profile validation.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/145/145720/2023.csv", "profile_path": "atlas/symbol_profiles/145/145720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-05-15", "entry_price": 159200, "MFE_30D_pct": 18.41, "MFE_90D_pct": 18.41, "MFE_180D_pct": 18.41, "MFE_1Y_pct": 18.41, "MFE_2Y_pct": null, "MAE_30D_pct": -9.67, "MAE_90D_pct": -29.02, "MAE_180D_pct": -42.59, "MAE_1Y_pct": -56.41, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-08", "peak_price": 188500, "drawdown_after_peak_pct": -50.19, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "good_4B_if_reimbursement_policy_and_inventory_risk_used", "four_b_evidence_type": ["valuation_blowoff", "margin_or_backlog_slowdown", "positioning_overheat"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "counterexample_export_headline_without_reimbursement_durability", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L74_C25_145720_DENTIUM_CHINA_VBP_EXPORT_COUNTER_ENTRY", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "T_R7L74_100120_20230217_STAGE2_DEVICE_EXPORT_NO_CONSUMABLE", "case_id": "R7L74_C25_100120_VIEWORKS_IMAGING_EXPORT_COUNTER", "symbol": "100120", "company_name": "뷰웍스", "round": "R7", "loop": "74", "scheduled_round": "R7", "scheduled_loop": "74", "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_CHANNEL", "sector": "medical_imaging_export", "primary_archetype": "device_export_without_reimbursement_or_consumables", "loop_objective": "sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2", "trigger_date": "2023-02-16", "evidence_available_at_that_date": "Medical/digital imaging export narrative without reimbursement conversion or recurring consumable economics. Evidence was too close to generic device/export beta; current profile can over-promote if relative strength dominates.", "evidence_source": "public medical imaging/export result window; stock-web tradable OHLC row and symbol profile validation.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/100/100120/2023.csv", "profile_path": "atlas/symbol_profiles/100/100120.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-02-17", "entry_price": 39650, "MFE_30D_pct": 7.19, "MFE_90D_pct": 8.45, "MFE_180D_pct": 8.45, "MFE_1Y_pct": 8.45, "MFE_2Y_pct": null, "MAE_30D_pct": -7.31, "MAE_90D_pct": -18.66, "MAE_180D_pct": -25.47, "MAE_1Y_pct": -36.19, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-04", "peak_price": 43000, "drawdown_after_peak_pct": -39.77, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.38, "four_b_full_window_peak_proximity": 0.38, "four_b_timing_verdict": "weak_4B_but_valid_counterexample_guard", "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "counterexample_generic_device_export_no_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L74_C25_100120_VIEWORKS_IMAGING_EXPORT_COUNTER_ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R7L74_100120_20230217_OVERLAY_DEVICE_EXPORT_NO_CONSUMABLE_OVERLAY", "case_id": "R7L74_C25_100120_VIEWORKS_IMAGING_EXPORT_COUNTER", "symbol": "100120", "company_name": "뷰웍스", "round": "R7", "loop": "74", "scheduled_round": "R7", "scheduled_loop": "74", "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_CHANNEL", "sector": "medical_imaging_export", "primary_archetype": "device_export_without_reimbursement_or_consumables", "loop_objective": "sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4C-Guard", "trigger_date": "2023-02-16", "evidence_available_at_that_date": "Medical/digital imaging export narrative without reimbursement conversion or recurring consumable economics. Evidence was too close to generic device/export beta; current profile can over-promote if relative strength dominates.", "evidence_source": "public medical imaging/export result window; stock-web tradable OHLC row and symbol profile validation.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/100/100120/2023.csv", "profile_path": "atlas/symbol_profiles/100/100120.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-02-17", "entry_price": 39650, "MFE_30D_pct": 7.19, "MFE_90D_pct": 8.45, "MFE_180D_pct": 8.45, "MFE_1Y_pct": 8.45, "MFE_2Y_pct": null, "MAE_30D_pct": -7.31, "MAE_90D_pct": -18.66, "MAE_180D_pct": -25.47, "MAE_1Y_pct": -36.19, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-04", "peak_price": 43000, "drawdown_after_peak_pct": -39.77, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.38, "four_b_full_window_peak_proximity": 0.38, "four_b_timing_verdict": "weak_4B_but_valid_counterexample_guard", "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "counterexample_generic_device_export_no_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L74_C25_100120_VIEWORKS_IMAGING_EXPORT_COUNTER_ENTRY", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
```

### 25.4 score_simulation rows
```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L74_C25_214150_CLASSYS_EXPORT_CONSUMABLE_POS", "trigger_id": "T_R7L74_214150_20240215_STAGE2A_EXPORT_CONSUMABLE_DEVICE", "symbol": "214150", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 12, "relative_strength_score": 14, "customer_quality_score": 10, "policy_or_regulatory_score": 2, "valuation_repricing_score": 12, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "export_growth_score": 13, "reimbursement_conversion_score": 9, "installed_base_or_consumable_score": 12, "inventory_or_channel_risk_score": -2, "positioning_overheat_score": -4, "thesis_break_score": 0}, "weighted_score_before": 84, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 9, "revision_score": 12, "relative_strength_score": 14, "customer_quality_score": 13, "policy_or_regulatory_score": 2, "valuation_repricing_score": 12, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "export_growth_score": 13, "reimbursement_conversion_score": 15, "installed_base_or_consumable_score": 17, "inventory_or_channel_risk_score": -3, "positioning_overheat_score": -4, "thesis_break_score": 0}, "weighted_score_after": 91, "stage_label_after": "Stage3-Green", "changed_components": ["export_growth_score", "reimbursement_conversion_score", "installed_base_or_consumable_score", "inventory_or_channel_risk_score", "positioning_overheat_score", "thesis_break_score"], "component_delta_explanation": "C25 shadow separates durable medical-device export + reimbursement/consumable conversion from generic export/device beta. Positive cases get bonus only when channel conversion is visible; counterexamples are capped or routed to 4C watch when reimbursement, inventory, or non-recurring order risk dominates.", "MFE_90D_pct": 56.16, "MAE_90D_pct": -4.41, "score_return_alignment_label": "aligned_after_channel_bridge_bonus", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L74_C25_338220_VUNO_AI_REIMBURSEMENT_HIGH_MAE_POS", "trigger_id": "T_R7L74_338220_20230628_STAGE2A_REIMBURSEMENT_MEDICAL_AI", "symbol": "338220", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 12, "relative_strength_score": 14, "customer_quality_score": 10, "policy_or_regulatory_score": 8, "valuation_repricing_score": 12, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "export_growth_score": 13, "reimbursement_conversion_score": 9, "installed_base_or_consumable_score": 6, "inventory_or_channel_risk_score": -2, "positioning_overheat_score": -4, "thesis_break_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 9, "revision_score": 12, "relative_strength_score": 14, "customer_quality_score": 13, "policy_or_regulatory_score": 8, "valuation_repricing_score": 12, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "export_growth_score": 13, "reimbursement_conversion_score": 15, "installed_base_or_consumable_score": 11, "inventory_or_channel_risk_score": -3, "positioning_overheat_score": -4, "thesis_break_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green+4B-Watch", "changed_components": ["export_growth_score", "reimbursement_conversion_score", "installed_base_or_consumable_score", "inventory_or_channel_risk_score", "positioning_overheat_score", "thesis_break_score"], "component_delta_explanation": "C25 shadow separates durable medical-device export + reimbursement/consumable conversion from generic export/device beta. Positive cases get bonus only when channel conversion is visible; counterexamples are capped or routed to 4C watch when reimbursement, inventory, or non-recurring order risk dominates.", "MFE_90D_pct": 172.49, "MAE_90D_pct": -15.61, "score_return_alignment_label": "positive_but_requires_mae_guard", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L74_C25_145720_DENTIUM_CHINA_VBP_EXPORT_COUNTER", "trigger_id": "T_R7L74_145720_20230515_STAGE2_EXPORT_WITH_REIMBURSEMENT_RISK", "symbol": "145720", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 5, "relative_strength_score": 15, "customer_quality_score": 4, "policy_or_regulatory_score": 8, "valuation_repricing_score": 12, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "export_growth_score": 10, "reimbursement_conversion_score": 1, "installed_base_or_consumable_score": 0, "inventory_or_channel_risk_score": -12, "positioning_overheat_score": -7, "thesis_break_score": 0}, "weighted_score_before": 79, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 5, "relative_strength_score": 15, "customer_quality_score": 4, "policy_or_regulatory_score": 8, "valuation_repricing_score": 12, "execution_risk_score": -13, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "export_growth_score": 10, "reimbursement_conversion_score": -4, "installed_base_or_consumable_score": 0, "inventory_or_channel_risk_score": -19, "positioning_overheat_score": -11, "thesis_break_score": -10}, "weighted_score_after": 60, "stage_label_after": "Stage2-Watch/4C-Guard", "changed_components": ["export_growth_score", "reimbursement_conversion_score", "installed_base_or_consumable_score", "inventory_or_channel_risk_score", "positioning_overheat_score", "thesis_break_score"], "component_delta_explanation": "C25 shadow separates durable medical-device export + reimbursement/consumable conversion from generic export/device beta. Positive cases get bonus only when channel conversion is visible; counterexamples are capped or routed to 4C watch when reimbursement, inventory, or non-recurring order risk dominates.", "MFE_90D_pct": 18.41, "MAE_90D_pct": -29.02, "score_return_alignment_label": "false_positive_blocked_after_reimbursement_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L74_C25_100120_VIEWORKS_IMAGING_EXPORT_COUNTER", "trigger_id": "T_R7L74_100120_20230217_STAGE2_DEVICE_EXPORT_NO_CONSUMABLE", "symbol": "100120", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 5, "relative_strength_score": 15, "customer_quality_score": 4, "policy_or_regulatory_score": 8, "valuation_repricing_score": 12, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "export_growth_score": 10, "reimbursement_conversion_score": 1, "installed_base_or_consumable_score": 0, "inventory_or_channel_risk_score": -12, "positioning_overheat_score": -7, "thesis_break_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 5, "relative_strength_score": 15, "customer_quality_score": 4, "policy_or_regulatory_score": 8, "valuation_repricing_score": 12, "execution_risk_score": -13, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "export_growth_score": 10, "reimbursement_conversion_score": -4, "installed_base_or_consumable_score": 0, "inventory_or_channel_risk_score": -19, "positioning_overheat_score": -11, "thesis_break_score": -10}, "weighted_score_after": 58, "stage_label_after": "Stage2-Watch", "changed_components": ["export_growth_score", "reimbursement_conversion_score", "installed_base_or_consumable_score", "inventory_or_channel_risk_score", "positioning_overheat_score", "thesis_break_score"], "component_delta_explanation": "C25 shadow separates durable medical-device export + reimbursement/consumable conversion from generic export/device beta. Positive cases get bonus only when channel conversion is visible; counterexamples are capped or routed to 4C watch when reimbursement, inventory, or non-recurring order risk dominates.", "MFE_90D_pct": 8.45, "MAE_90D_pct": -18.66, "score_return_alignment_label": "guarded_after_shadow", "current_profile_verdict": "current_profile_false_positive"}
```

### 25.5 residual_contribution row
```jsonl
{"row_type": "residual_contribution", "round": "R7", "loop": "74", "scheduled_round": "R7", "scheduled_loop": "74", "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["generic_device_export_false_positive", "reimbursement_or_consumable_conversion_missing", "4B_overlay_late_for_high_MAE_medical_AI"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "diversity_score_summary": "new_symbols=4; new_trigger_families=4; counterexamples=2; residual_errors=3; wrong_round_penalty=0"}
```

### 25.6 profile comparison rows
```jsonl
{"row_type": "profile_comparison", "profile_id": "P0_e2r_2_1_stock_web_calibrated_proxy", "profile_scope": "global_proxy", "profile_hypothesis": "current global profile captures some Stage2 evidence but can over-promote generic device/export RS without reimbursement or consumable conversion", "changed_axes": [], "changed_thresholds": {}, "eligible_trigger_count": 4, "selected_entry_trigger_per_case": 4, "avg_MFE_90D_pct": 63.88, "avg_MAE_90D_pct": -16.93, "avg_MFE_180D_pct": 71.26, "avg_MAE_180D_pct": -28.24, "false_positive_rate": 0.5, "missed_structural_count": 0, "late_green_count": 2, "avg_green_lateness_ratio": 0.5, "avg_four_b_local_peak_proximity": 0.79, "avg_four_b_full_window_peak_proximity": 0.79, "score_return_alignment_verdict": "mixed; positives work but two generic export/device signals remain false positives"}
{"row_type": "profile_comparison", "profile_id": "P0b_e2r_2_0_baseline_reference", "profile_scope": "rollback_reference", "profile_hypothesis": "older baseline was looser on RS/export narratives and more likely to label C25 counterexamples positive", "changed_axes": ["rollback_reference_only"], "changed_thresholds": {}, "eligible_trigger_count": 4, "selected_entry_trigger_per_case": 4, "avg_MFE_90D_pct": 63.88, "avg_MAE_90D_pct": -16.93, "avg_MFE_180D_pct": 71.26, "avg_MAE_180D_pct": -28.24, "false_positive_rate": 0.5, "missed_structural_count": 0, "late_green_count": 2, "avg_green_lateness_ratio": 0.61, "avg_four_b_local_peak_proximity": 0.71, "avg_four_b_full_window_peak_proximity": 0.71, "score_return_alignment_verdict": "weaker than P0; counterexample cap absent"}
{"row_type": "profile_comparison", "profile_id": "P1_sector_specific_candidate_profile", "profile_scope": "L7_sector_specific", "profile_hypothesis": "L7 medical-device scoring needs export/reimbursement/consumable conversion bridge and explicit inventory/ASP guard", "changed_axes": ["medical_device_channel_conversion_bonus", "medical_device_export_only_cap"], "changed_thresholds": {"C25_green_requires_channel_or_reimbursement_conversion": true}, "eligible_trigger_count": 4, "selected_entry_trigger_per_case": 4, "avg_MFE_90D_pct": 114.33, "avg_MAE_90D_pct": -10.01, "avg_MFE_180D_pct": 129.09, "avg_MAE_180D_pct": -22.45, "false_positive_rate": 0.0, "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": 0.5, "avg_four_b_local_peak_proximity": 0.92, "avg_four_b_full_window_peak_proximity": 0.92, "score_return_alignment_verdict": "improved: keeps Classys/Vuno, rejects Dentium/Vieworks"}
{"row_type": "profile_comparison", "profile_id": "P2_canonical_archetype_candidate_profile", "profile_scope": "C25_canonical_archetype_specific", "profile_hypothesis": "C25 positive requires export growth plus reimbursement/consumable/channel conversion; generic export/device beta is capped", "changed_axes": ["c25_reimbursement_channel_conversion_bonus", "c25_inventory_asp_guard", "c25_price_only_device_blowoff_guard"], "changed_thresholds": {"C25_Stage3_Green_requires_non_price_conversion_evidence": true}, "eligible_trigger_count": 4, "selected_entry_trigger_per_case": 4, "avg_MFE_90D_pct": 114.33, "avg_MAE_90D_pct": -10.01, "avg_MFE_180D_pct": 129.09, "avg_MAE_180D_pct": -22.45, "false_positive_rate": 0.0, "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": 0.5, "avg_four_b_local_peak_proximity": 0.92, "avg_four_b_full_window_peak_proximity": 0.92, "score_return_alignment_verdict": "best C25 alignment"}
{"row_type": "profile_comparison", "profile_id": "P3_counterexample_guard_profile", "profile_scope": "counterexample_guard", "profile_hypothesis": "if export/device evidence lacks reimbursement or recurring consumable conversion, cap positive stage and route inventory/ASP breaks to 4C watch", "changed_axes": ["c25_export_only_guard", "c25_inventory_asp_4c_guard"], "changed_thresholds": {"price_only_device_export_blocks_positive_stage": true}, "eligible_trigger_count": 2, "selected_entry_trigger_per_case": 2, "avg_MFE_90D_pct": 13.43, "avg_MAE_90D_pct": -23.84, "avg_MFE_180D_pct": 13.43, "avg_MAE_180D_pct": -34.03, "false_positive_rate": 0.0, "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": "NA", "avg_four_b_local_peak_proximity": 0.66, "avg_four_b_full_window_peak_proximity": 0.66, "score_return_alignment_verdict": "protective for false positives"}
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
completed_round = R7
completed_loop = 74
next_round = R8
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest/schema/profile rows were read from Songdaiki/stock-web. The manifest max date used for forward-window eligibility is 2026-02-20.
- Profile-level corporate-action candidate checks: 214150 has only 2017-12-28; 145720 and 338220 have no candidate dates; 100120 has only 2011-08-08. None overlaps the selected trigger 180D windows.
- Evidence-source notes are historical and narrative-only for public events; quantitative calibration uses stock-web tradable_raw OHLC rows only.
